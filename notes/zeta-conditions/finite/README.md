# Finite constructions

Run from any working directory:

```bash
python3 /path/to/riemann-channel/notes/zeta-conditions/finite/run_all.py
```

Dependencies: Python 3, NumPy, SymPy, SciPy. No downloads, random sampling, or zero tables.
Each of the 13 example scripts also runs independently and prints a check tally.
`common.py` and `dirichlet_common.py` contain shared arithmetic and contraction routines.

`results/*.json` stores exact matrices, sequences, formulas and tallies;
`results/*.txt` stores the full standalone output. `run_all.py` regenerates
`results/evidence.md` and the marked evidence appendix of `../astra-constructions.md`
only after every example succeeds. The report before the marker is written by hand.

The checks include exact Kraus identities, finite-field enumeration, direct word norms,
character-weighted irreducible-polynomial Euler coefficients, graph-cover determinants,
and numerical cMPS exponentials. All-degree claims use the proofs and qualifications in
the report; a finite tally alone does not establish them.
