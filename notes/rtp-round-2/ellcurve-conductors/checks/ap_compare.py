#!/usr/bin/env python3
"""Compare zst_ell_ap (checks/ap_zst.out) with PARI ellap (checks/check_models.out), p < 200. claude:opus."""
from pathlib import Path
h = Path(__file__).resolve().parent
pari = {l.split()[0]: l.split()[-1] for l in (h/'check_models.out').read_text().splitlines() if l[:1].isdigit() and len(l.split()) == 6}
zst = {l.split()[0]: l.split()[1] for l in (h/'ap_zst.out').read_text().splitlines()}
bad = [k for k in pari if zst.get(k) != pari[k]]
print(f'curves compared: {len(pari)}; a_p for the 46 primes < 200 each; mismatches: {bad}')
print(f'# checks: {len(pari)} run, {len(bad)} failed')
