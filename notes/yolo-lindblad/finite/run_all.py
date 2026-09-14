#!/usr/bin/env python3
"""Reproduce every finite-lane result and render the report; no network access."""
import json
import os
from pathlib import Path
import subprocess
import sys
import numpy as np
import scipy
import sympy
import mpmath
from finite_common import HERE, SEED

SCRIPTS = ("verify_phase", "verify_characters", "verify_ramanujan", "hunt", "spectrum", "balance")


def main():
    env = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1", PYTHONHASHSEED=str(SEED))
    tallies = {}
    print(f"finite lane; fixed seed={SEED}", flush=True)
    for name in SCRIPTS:
        with (HERE/f"{name}.txt").open("w") as log:
            process = subprocess.run([sys.executable, str(HERE/f"{name}.py")],
                                     env=env, stdout=log, stderr=subprocess.STDOUT)
        if process.returncode:
            print((HERE/f"{name}.txt").read_text()[-5000:])
            raise SystemExit(process.returncode)
        result = json.loads((HERE/f"{name}.json").read_text())
        assert result["seed"] == SEED
        tallies[name] = result["checks"]
        print(f"{name}.py: {result['checks']} checks passed", flush=True)
    versions = dict(python=sys.version.split()[0], numpy=np.__version__, scipy=scipy.__version__,
                    sympy=sympy.__version__, mpmath=mpmath.__version__)
    (HERE/"manifest.json").write_text(json.dumps(dict(seed=SEED, tallies=tallies,
                                                     total=sum(tallies.values()), versions=versions), indent=2)+"\n")
    subprocess.run([sys.executable, str(HERE/"render_report.py")], env=env, check=True)
    print(f"all {sum(tallies.values())} scientific checks passed; report rendered", flush=True)


if __name__ == "__main__":
    main()
