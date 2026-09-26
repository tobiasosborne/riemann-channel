# Lane L verification artifacts

Author: `codex:gpt-6-astra`.

Run `python3 scripts/rtp2_lattice_box.py` from the repository root. The generated C bridge links the existing `zst/build/libzst.a`; it does not build or modify zst. NumPy/SciPy provide deterministic double searches, mpmath provides 200-digit searches and 260-digit supported-system audits, and the bridge provides 1280-bit Arb certificates. No numerical zeros are used.

- `bridge.c`: generated, reviewable C bridge; the canonical source is embedded in the Python script. `bridge` is its locally compiled executable.
- `x*_N*.data`: zst prime-side coefficient midpoints, positive Cholesky flags, QR Rayleigh values, and atom sensitivities, printed to 220 digits.
- `x*_N*.balls`: exact Arb serialization of the Rayleigh costs and sensitivities for fixed dyadic test vectors. The first two integers are the number of coordinates and cuts.
- `x*_N*.bases`: the support of each coordinate/sign dual. These are also the primal active constraints.
- `x*_N*.certificates`: independently reconstructed interval dual solutions and primal feasibility certificates (`OPT=1`). `CERT` sign +1 bounds the negative displacement, sign -1 the positive displacement.
- `x*_N*.json`: every relative coordinate interval, HiGHS diagnostic, exact decimal outward width bound, basis, and high-precision dual coefficients. Saved bases are warm starts only: every run solves and audits them again, including the separate Arb verification.
- `x*_N*.minima_v3`: independently enclosed minimum eigenpairs with rank-one minimality certificates. The suffix distinguishes the stable rank-one method from an earlier discarded LDL diagnostic.
- `scan_x*.data`: a Cholesky scan through N=200; prefix sums of log pivots give the total log determinant at every smaller cutoff.
- `recession.in`, `.json`, `.certificates`: search witnesses and the ball verifier's results. Dual matrices are projected exactly onto the atom-orthogonal space using an interval linear solve before positive definiteness is tested.
- `sections_N*.in`, `.json`, `.certificates`: two-coordinate section primal points and rank-two duals. The C verifier reconstructs the original, unwhitened matrices.
- `replay.txt`: a full repeated run for byte comparison with `outputs/rtp2_lattice_box.txt`.
- `audit.py` / `audit.txt`: six cold-versus-warm LP audits and twelve comparisons of the reported minimum with its independently certified even eigenvalue enclosure and the larger odd minimum.

The script has `--case x N`, `--sections N`, `--recession`, and `--produce x N` modes. It caches zst data and warm bases under this directory; deleting a case's artifacts requests reconstruction. Ball certificates, rather than residual tolerances or HiGHS values, establish the reported bounds. The full SDP boxes with every coordinate free were not computed.
