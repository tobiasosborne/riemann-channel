# Final validation record

Run by the root after the second-round reviews, 2026-09-18.

- `make check`: **PASS**, 377 claims, 91 definitions, 207 notation rows,
  153 provenance rows, 137 proved; zero errors and zero warnings.
- Fresh LaTeX build: **PASS**, no undefined citations/references or duplicate
  labels. `report.pdf` includes all seven new shards. The Gram-network and
  Hamiltonian pages were rendered and visually inspected.
- `python3 scripts/ccm_tensor_network.py` and `python3 -O ...`: **PASS**,
  157 conditions and two rejected mutations on temporary copies. Both outputs
  byte-match `outputs/ccm_tensor_network.txt`.
- Independent finite critic checker, rerun by root under `python -O`:
  **PASS**, 37 conditions and two rejected copied mutations.
- Independent continuous critic checker, rerun by root under `python -O`:
  **PASS**, 26 conditions. Its copied sign mutation exits 1 with
  `24 PASS / 2 FAIL`, as required.
- Source cache: restored 117 ignored archives; all 226 manifest entries and
  all 153 contiguous provenance quotations validate. No tracked manifest or
  fetch script was changed.
- `git diff --check` and staged whitespace check: **PASS**.

## Full local CI limitation

`make ci` passes the parity gate, fresh build/log scan and source manifest,
then stops at its literal saved-output comparison for the unchanged legacy
script `scripts/qihara_general.py`:

    saved: trace formula m=1..4: max error 5.5e-12
    fresh: trace formula m=1..4: max error 3.7e-12

Root subsequently ran every one of the 13 evidence scripts named by CI,
recording exit codes independently of output comparisons. All exited zero.
Nine matched their saved output; four unchanged legacy scripts differed:
`qihara_general.py`, `weil_positivity.py`, `graded_ramanujan.py`, and
`selberg_letters.py`. The new `ccm_tensor_network.py` matched exactly.
Those old snapshots and scripts were not modified to conceal the mismatch.
Accordingly the full snapshot-based CI is **not claimed green**, despite
the successful mathematical checkers and clean lab-book gate.

## Scope of the checkpoint

The checkpoint includes the new research, seven shards, databases, compiled
report, checker/CI registration, and this turn's focus/worklog additions.
Earlier uncommitted zst, elliptic-curve and tutorial changes are excluded.
The original 357 claim rows are preserved byte-for-byte before the 20 new
rows. Promotions follow the two independent r2 verdict files; no statement
is promoted solely from numerical evidence.
