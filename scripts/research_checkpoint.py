#!/usr/bin/env python3
"""Create atomic, checksummed offline snapshots, including gitignored sources.

No network or third-party packages required. Archives exclude .git, .recovery,
Python caches and symlinks. A full snapshot restores the working tree, not Git
history. During active work each file is captured once; files are not captured
at one simultaneous instant. Completed snapshots are never overwritten.
"""
import argparse
import datetime as dt
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import tarfile

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {".git", ".recovery", "__pycache__"}


def atomic_write(path, data):
    tmp = path.with_name(path.name + ".partial")
    with tmp.open("wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(tmp, path)
    descriptor = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def digest_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify(archive):
    sidecar = archive.with_name(archive.name + ".sha256")
    if sidecar.exists() and sidecar.read_text().split()[0] != digest_file(archive):
        raise ValueError("Archive checksum mismatch")
    actual = {}
    with tarfile.open(archive, "r:gz") as bundle:
        for member in bundle:
            path = Path(member.name)
            if path.is_absolute() or ".." in path.parts or not member.isfile():
                raise ValueError("Unsafe archive entry: " + member.name)
            if member.name in actual:
                raise ValueError("Duplicate archive entry: " + member.name)
            body = bundle.extractfile(member).read()
            if member.name == "RECOVERY-MANIFEST.json":
                manifest = json.loads(body)
            else:
                actual[member.name] = {"sha256": hashlib.sha256(body).hexdigest(),
                                       "bytes": len(body)}
    if actual != manifest["files"]:
        raise ValueError("Per-file manifest mismatch")
    return manifest


def snapshot(scope, session):
    session_path = (ROOT / session).resolve()
    session_path.relative_to(ROOT)
    if scope == "session" and not session_path.is_dir():
        raise ValueError("Session directory does not exist")
    destination = ROOT / ".recovery"
    destination.mkdir(exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    archive = destination / (stamp + "-" + scope + ".tar.gz")
    temporary = archive.with_name(archive.name + ".partial")
    try:
        revision = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True,
            stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        revision = None
    manifest = {"created_utc": stamp, "scope": scope, "base_commit": revision,
                "session": session, "files": {}, "skipped_symlinks": []}
    base = ROOT if scope == "full" else session_path
    candidates = []
    for directory, directories, filenames in os.walk(base, followlinks=False):
        directories[:] = sorted(d for d in directories if d not in EXCLUDED)
        for filename in sorted(filenames):
            path = Path(directory) / filename
            if path.is_symlink():
                manifest["skipped_symlinks"].append(str(path.relative_to(ROOT)))
            elif path.is_file() and path.suffix != ".pyc":
                candidates.append(path)
    with temporary.open("wb") as raw:
        with tarfile.open(fileobj=raw, mode="w:gz", compresslevel=3) as bundle:
            for path in sorted(candidates):
                body = path.read_bytes()
                name = str(path.relative_to(ROOT))
                entry = bundle.gettarinfo(str(path), arcname=name)
                entry.size = len(body)
                bundle.addfile(entry, io.BytesIO(body))
                manifest["files"][name] = {
                    "sha256": hashlib.sha256(body).hexdigest(), "bytes": len(body)}
            body = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
            entry = tarfile.TarInfo("RECOVERY-MANIFEST.json")
            entry.size = len(body)
            bundle.addfile(entry, io.BytesIO(body))
        raw.flush()
        os.fsync(raw.fileno())
    # Re-read every archived byte before advertising a completed checkpoint.
    verify(temporary)
    checksum = digest_file(temporary)
    os.replace(temporary, archive)
    atomic_write(archive.with_name(archive.name + ".sha256"),
                 (checksum + "  " + archive.name + "\n").encode())
    pointer = {"archive": str(archive.relative_to(ROOT)), "sha256": checksum,
               "files": len(manifest["files"]), "created_utc": stamp}
    atomic_write(destination / ("LATEST-" + scope + ".json"),
                 (json.dumps(pointer, indent=2) + "\n").encode())
    print(json.dumps(pointer, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scope", choices=("full", "session"), default="session")
    parser.add_argument("--session", default="notes/rh-strategy-2026-09-19")
    parser.add_argument("--verify", type=Path)
    args = parser.parse_args()
    if args.verify:
        manifest = verify(args.verify)
        print("Verified", len(manifest["files"]), "files in", args.verify)
    else:
        snapshot(args.scope, args.session)


if __name__ == "__main__":
    main()
