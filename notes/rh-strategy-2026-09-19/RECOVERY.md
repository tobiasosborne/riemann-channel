# Offline recovery for this session

Agents write their working reports directly into this directory, beginning
before analysis and extending them at each substantive finding. The reports,
source receipts, scripts and outputs are the research record; chat is not
needed to reconstruct the conclusions.

`scripts/research_checkpoint.py` also creates immutable local snapshots in
`.recovery/`. `LATEST-full.json` identifies the most recent complete working-tree
snapshot, including **gitignored `refs/src/`**, data, reports, scripts and source
archives. `LATEST-session.json` identifies the latest small snapshot of this
session. Each completed snapshot has an external SHA-256 receipt and an embedded
per-file hash manifest. A snapshot is published only after every archived file
has been read back and verified. Partial archives do not replace a completed
snapshot. Python's standard library is sufficient to create or verify one.

From the repository root:

```sh
python3 scripts/research_checkpoint.py --scope session
python3 scripts/research_checkpoint.py --scope full
python3 scripts/research_checkpoint.py --verify .recovery/ARCHIVE.tar.gz
```

To recover without network access, read the latest pointer, verify its archive,
and extract into a **new empty directory**. The archive paths are relative to the
repository root:

```sh
mkdir -p /tmp/riemann-recovered
tar -xzf .recovery/ARCHIVE.tar.gz -C /tmp/riemann-recovered
```

If restoring an initial full snapshot plus a later session snapshot, extract the
full snapshot first and then overlay the session snapshot. A final full snapshot
is self-contained. The source cache includes original TeX and tar archives;
ordinary source use and the provenance checks do not require arXiv access.

Full snapshots capture each regular file once, not every file at a simultaneous
instant. They exclude Git metadata, `.recovery/`, Python bytecode/cache directories
and symlinks. They restore the working tree, not Git history. The embedded base
commit identifies the original Git revision. The final full snapshot is taken
after the agents finish writing.

These local snapshots protect against network/session loss. They are on the same
disk as the repository, so they do not protect against disk loss. Copy a completed
archive and its `.sha256` receipt to another disk for that protection. `.recovery/`
is Git-ignored to avoid publishing cached third-party sources in the public repo.
The session notes and source receipts remain ordinary versionable files.

Current cached source hashes were checked against `refs/manifest.sha256` before
research began. New source downloads have their own local provenance receipts;
only complete, validated downloads are renamed from `.partial` to final names.
