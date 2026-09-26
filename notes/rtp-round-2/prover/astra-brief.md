# Brief for lane P (RTP-2): four proofs for the tomography programme. The bordering lemma in full; the Baker grading of the finite-prime language; the FNW exclusion theorem in Tarski–Seidenberg form; an effective Diophantine learning-rate bound

You are `codex:gpt-6-astra`, the prover in a mathematical research notebook (git repo, current directory). Read
`notes/rtp-round-2/brief.md` first (game rules, conventions, output protocol; binding). Then read:
`report/sections/08i_riemann_tomography.tex` (`lem:bordering-interval`, status sketched, and its context),
`notes/rtp-round-1/lane-A1.md` section 1 (lemma A1.1 and A1.1' with their proofs, which the review accepted as
sketches; the review's C1 item in `notes/reviews/rtp-round-1-2026-09-24.md`), `report/sections/08g_weil_window_extension.tex`
(`prop:extension-disc`), `notes/metric-tomography/finite-prime-language.md` (sections 2, 3, 4 and 7: Proposition A,
the quantitative remark, the language `L_S`, future directions 1–3), `notes/metric-tomography/metric-as-state.md`
section 7, `db/claims.tsv` rows `lem:bordering-interval`, `prop:extension-disc`, `obs:prime-by-prime-blind`,
`thm:weil-positivity-finite`, `prop:trace-supertrace-criterion`, `obs:factor-by-factor-limits` (use `grep -P '^<id>\t'`),
and `notes/zeta-spectral-triples/plan.md` section 1 (the Loewner data of the window form). Sources that are on
disk (cite by file and line where you quote): `refs/src/2511.22755/mc2arXiv.tex` (CCM), `refs/src/` for
Lagarias/Bombieri–Lagarias if present (`ls refs/src`), and `refs/ocr/` for the round-1 non-arXiv OCR texts. For
Baker's theorem, Tarski–Seidenberg, Basu–Pollack–Roy and the transcendence measure of `log 2` no local source
exists: state each as a named hypothesis `H-BAKER`, `H-TS`, `H-BPR`, `H-LOG2` with the precise form you use and a
standard reference (author, year, theorem number as best you know it, flagged "from memory, to be byte-cited"), so
the results are PROVED-conditional on those. Write only `notes/rtp-round-2/prover/astra-proofs.md`,
`progress.txt` and `checks/` (python3 with numpy, mpmath, sympy for any check). Do not run git.

## P1. `lem:bordering-interval`, proved in full (upgrade from sketched)

Statement in the shard: (i) bordering a positive-definite Hermitian `G_K` by column `c` and diagonal `d`: PSD iff
`d - c^* G_K^{-1} c >= 0`; with `d` known the maximum-determinant completion is `c = 0`; the log-det gain
`Delta I = log(d/(d - c^* G_K^{-1} c)) >= 0` is twice the mutual information of the corresponding real centred
Gaussian. (ii) In the window form the bordering `|n| <= N -> N+1` adds one even and one odd basis vector whose
columns and diagonals are affine in the single new datum `b_{N+1}` once `a_{N+1}` is given; each block's Schur
complement is a concave quadratic in `b_{N+1}`, so each block's admissible set is an interval whose centre is that
block's maximum-determinant value and whose endpoints are the singular enlargements; the joint admissible set is
the intersection of the two intervals, and the joint maximum-determinant point (the maximiser of `s_e s_o` on it)
is in general not its centre. (iii) `c = 0` is not a Loewner column unless `b_1 = ... = b_{N+1} = 0`.

Tasks: prove (i)–(iii) with complete hierarchical proofs, fixing every convention from the formula sheet (basis
normalisation of the even/odd vectors, the exact vectors `w_e`, `w_o`, `u_e`, `u_o` of lemma A1.1', the sign of `l`).
Make "in general not its centre" precise: prove that the joint max-det point equals the centre of the intersection
iff an explicit condition on `(s_e*, s_o*, beta_e*, beta_o*, C_e, C_o)` holds, and exhibit a rational `2 x 2`/`1 x 1`
example where it fails (with the offset computed exactly in `checks/`). Check the mutual-information identity for
complex (circular) Gaussians as well and say which is the right one here (the forms are real). Correct anything in
the shard's wording that is false or ambiguous, in the ledger.

## P2. The Baker grading of the finite-prime language (future direction 3 of `finite-prime-language.md`)

Define, for a finite set `S` of primes, `L_S = Q-bar-span{1, log p (p in S), A}` with `A` the archimedean values
named in the note (`gamma`, `pi`, logs of algebraic numbers, `psi^(n)(r)` at rational `r`). Formulate and prove
the cleanest true theorem of the form: **for test functions in the discrete class of the notebook (finite
combinations of point masses at positions `log n`, `n` an `S`-smooth integer, with algebraic coefficients; or the
lattice-bump class if its archimedean integrals can be shown to lie in `A`, which you must check and probably
cannot), the value `W(f * f~)` lies in `L_S`, and its `p`-coordinate in the Baker direct sum is the local term at
`p`.** Under `H-BAKER` (`1, log p_1, ..., log p_r, i pi` linearly independent over `Q-bar`; state the exact
consequence of Baker's theorem you use, and prove the `Q`-independence part from unique factorisation yourself),
show the direct-sum decomposition is well defined and that the map `f -> (p-coordinates)` is exactly the
prime-content filtration of `metric-as-state.md` section 3. Then prove the corollary that makes
`obs:prime-by-prime-blind` exact at the level of numbers: a family of test functions whose values lie in `L_S` for a
fixed finite `S` is blind (in the precise sense you define) to every prime outside `S`. Be careful about the
archimedean term: the pole term `2 cosh(D/2)` at `D = log(n/m)` is algebraic times ... check what it is; the
archimedean term for point masses needs `rho(y)` at `y = log(n/m)`, which is algebraic; the `W_R` diagonal involves
`log 4 pi + gamma` and possibly an integral. Say exactly which test class makes the theorem true and label
anything conditional.

## P3. The FNW exclusion theorem (Proposition A of `finite-prime-language.md`), proved

State and prove: fix a bond dimension `d` and a finite-range interaction `h` with real algebraic matrix entries;
the set `F_d` of translation-invariant finitely correlated states with auxiliary algebra of dimension at most `d`
is semialgebraic over the real algebraic numbers (parametrise it explicitly: Kraus tensors or the Choi matrix of
the generating CP unital map, the fixed-point equations, normalisation; say why each constraint is a polynomial
equation or inequality over `Q-bar cap R`, and handle the "algebra of dimension at most `d`" quantifier); the energy
density is a semialgebraic function with algebraic coefficients; hence `e_d = inf_{F_d} e` is a real algebraic
number (under `H-TS`: Tarski–Seidenberg, plus the lemma that a semialgebraic subset of `R` defined over a real
closed subfield `F` has its endpoints in `F`; prove that lemma from quantifier elimination); hence a transcendental
ground-state energy density excludes finitely correlated ground states for every `d` and gives `e_d > e_0` strictly.
Also prove the infimum is attained (compactness of `F_d` after fixing the gauge; say what gauge) so that `e_d` is a
minimum, or explain why attainment is not needed. Then state the notebook transposition in section 4 of the note
(every optimum over a finite bond of an algebraic variational functional is algebraic) as a corollary with its exact
hypotheses.

## P4. The effective Diophantine learning-rate bound (future direction 2)

Under `H-BPR` (effective quantifier elimination: the endpoints of the projection of a semialgebraic set described
by `s` polynomials of degree at most `deg` in `k` variables are algebraic of degree at most `D(s, deg, k)` and
height at most `H(s, deg, k, height of the input)`; state the explicit bound you use, from Basu–Pollack–Roy's book
if you can recall the theorem, flagged for byte-citing) and `H-LOG2` (a transcendence measure for `log 2`:
`|log 2 - alpha| > exp(-c(D) log H(alpha))` or whatever form you can state precisely for algebraic `alpha` of degree
`D` and height `H`; give the best form you know with its source), derive an explicit lower bound
`e_d - e_0 >= B(d)` for the spin-1/2 Heisenberg antiferromagnet (`e_0 = 1/4 - log 2` per site, `H-HULTHEN`) as a
function of `d`. Work out the count `k` of parameters and the degrees for the parametrisation you used in P3, push
the numbers through, and report the resulting `B(d)` for `d = 2, 3, 4, 8` as a decimal (it will be astronomically
small; say how small, e.g. `10^{-10^{...}}`). State clearly that this is the first rigorous lower bound on
matrix-product convergence obtained from transcendence rather than analysis, or find and cite the precedent if
you know one. Then say in one paragraph what the analogue for the metric problem would need (the note's section 4:
an invariant of the true metric known to be transcendental), and confirm or correct the note's list of open
inputs (irrationality of a zero ordinate, transcendence of `gamma`, of a Stieltjes constant).

## Output format

`notes/rtp-round-2/prover/astra-proofs.md`: ledger; P1–P4 as theorems/propositions with hierarchical proofs and
declared hypotheses (PROVED / PROVED-conditional / REFUTED / SHARPENED / OPEN); a section "Numerical checks for the
blind lane" (the P1 offset example with exact numbers; a 3-atom instance of P2's direct sum; P4's `B(d)` values);
"What this changes in the notebook" (which claim rows change status, which new rows to add with kind and status,
what remains to byte-cite). Write incrementally, item by item; `progress.txt` lines P1..P4.
