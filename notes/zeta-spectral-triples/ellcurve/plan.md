# MVP-3: the Connes-Consani-Moscovici construction on the L-function of an elliptic curve over Q

Orchestrator's draft, 2026-09-18 (night), REVIEWED AND CORRECTED by the codex `gpt-6-astra` lane
(brief `astra-brief.md`, report `astra-review.md`, checks under `checks/`). Section 1 below is
superseded by the review's "Formula sheet for the workers" (F1-F18), which is AUTHORITATIVE for the
implementation; Section 1 is kept as the draft with the corrections marked. Section 2-4 and 6 are
rewritten per the review (see "Review outcome" at the end). Parent plan: `../plan.md` (Sections 1.1-1.5 are the formula sheet this draft extends;
Section 3.2 is the data model this MVP implements; Section 6.3 anticipated this case). Sibling MVPs:
`../../../zst/` (Riemann zeta, M1-M2 done, benchmark to x = 50), `../../../ihz/` (Ihara zeta of
graphs and the finite F_5 curve, G1-G3 done).

## 0. Why this object

TJO wants to understand the CCM construction on a zeta with zeros that differs from Riemann's in
some structural way, "the simplest, e.g. elliptic curves". Two readings:

- The Hasse-Weil zeta of an elliptic curve over F_q: degree-2 numerator, two zeros, finite divisor.
  DONE in `ihz/` (`--counts 0,8,32,104,640 --q 5`): the construction degenerates to an exact
  Caratheodory-Fejer identity at the critical window, no archimedean term, no second truncation.
  Nothing left to learn about CCM there.
- The L-function of an elliptic curve over Q, `L(E, s)`: infinitely many zeros, an archimedean term
  of a NEW shape (`Gamma_C(s + 1/2)` instead of `Gamma_R(s)`), a conductor `N`, bad primes with
  degree-one Euler factors, NO pole (so the rank-two term `W_{0,2}` of the zeta case is absent), and
  the one feature Riemann's zeta cannot show: a central zero of prescribed multiplicity (the analytic
  rank), of ODD multiplicity when the root number is `w = -1`. This is the object of this MVP.

It exercises exactly the parts of the CCM machine that the zeta MVP could not: the generic
explicit-formula data model (parent plan M3: kernels derived, not typed), the absence of the pole
term, and the interaction of the even/odd symmetry of the construction with a zero at the centre.
Selberg (compact or modular) is the next infinite object after this one; its data (length spectrum,
cusp comb) is a project of its own and is deferred (parent plan 6.5).

## 1. The object and its explicit-formula distribution

Conventions (analytic normalisation throughout; centre `1/2`, zeros `rho = 1/2 + i gamma`).

`E/Q` given by a global minimal Weierstrass model `[a1, a2, a3, a4, a6]`, conductor `N`. For a
prime `p`: `a_p = p + 1 - #E~(F_p)` where `#E~(F_p)` counts the affine solutions of
`y^2 + a1 x y + a3 y = x^3 + a2 x^2 + a4 x + a6` over `F_p` PLUS the point at infinity, singular
point included. This single naive count is correct for good AND bad primes of a minimal model:
good `p`: `|a_p| <= 2 sqrt p`; split multiplicative `a_p = 1`; non-split `a_p = -1`; additive
`a_p = 0` (H-COUNT: `#E~_ns(F_p) = p - 1, p + 1, p` respectively and the singular point adds one).
Cross-check: PARI `ellap` (available here through `cypari2`, scratch venv; see Section 5).

Local Satake data. Good `p`: `alpha_p + beta_p = a_p`, `alpha_p beta_p = p`; the normalised power
sums `c_m(p) = (alpha_p^m + beta_p^m) p^{-m/2}` satisfy `c_0 = 2`, `c_1 = a_p/sqrt p`,
`c_m = (a_p/sqrt p) c_{m-1} - c_{m-2}` (H-LUCAS). Bad `p`: Euler factor `(1 - a_p p^{-s})^{-1}`,
so `c_m(p) = a_p^m p^{-m/2}` (`alpha = a_p, beta = 0`).

Completed L-function: `Lambda(E, s) = N^{s/2} Gamma_C(s + 1/2) L(E, s + 1/2)` in the analytic
normalisation, `Gamma_C(s) = 2 (2 pi)^{-s} Gamma(s)`, `Lambda(E, s) = w Lambda(E, 1 - s)`,
`w = +-1` the root number (H-FE: modularity, Wiles et al.; standard). `Lambda` is ENTIRE: no pole.
Trivial zeros of `L(E, s + 1/2)` at `s = -1/2, -3/2, ...` are the poles of `Gamma(s + 1/2)`; in the
explicit formula they live inside the archimedean term, exactly as the trivial zeros of zeta live
inside `W_R`. The root number `w` does NOT appear in the explicit formula (`Lambda'/Lambda` is odd
about the centre for either sign); it is encoded in the atoms through the zero set.

Window distribution (the parent plan's `D` on `[0, L]`, `L = 2 log lambda`; Loewner data
`b_n = -(1/pi) int sin(omega_n y) D(y) dy`, `a_n = 2 int (1 - y/L) cos(omega_n y) D(y) dy`,
`omega_n = 2 pi n / L`, parent 1.1). The claim of this draft is that `D_E = D_atoms + D_arch +
D_shift` with:

    D_atoms = sum_{p^m <= lambda^2, m >= 1}  w_{p,m} delta(y - m log p),
              w_{p,m} = - c_m(p) log p * p^{-m/2}  = - t_m log p / p^m          (D1, CORRECTED)
              (t_m = alpha^m + beta^m unnormalised; the draft omitted p^{-m/2}. Bad p: -(a_p/p)^m log p.)

(zeta: `c_m = 1` for every `p`, weight `-Lambda(p^m) p^{-m/2}`: parent 1.2, `refs/src/2511.22755/
mc2arXiv.tex` eq. `bomp`. Same sign: these are ZEROS, the sign flip of `ihz` belongs to poles.)

    D_arch: kernel family of the parent data model, `rho_{d,mu}(x) = sum_{k>=0} e^{-(dk+mu)x}`.
            zeta:   Gamma_R(s)        -> (d, mu) = (2, 1/2), coefficient -1  (parent 1.2)
            E/Q:    Gamma_C(s + 1/2)  -> (d, mu) = (1, 1),   coefficient -1,
                    equivalently (2, 1) + (2, 2) by Legendre duplication
                    Gamma_C(s+1/2) = Gamma_R(s+1/2) Gamma_R(s+3/2)          (D2)

Derivation sketch (to be checked by the reviewer against the TeX, Prop. `computearch`): on the
critical line `s = 1/2 + i tau`, Gauss's integral `psi(z) = int_0^inf (e^{-t}/t - e^{-zt}/(1 -
e^{-t})) dt` with `z = (s + kappa)/2` for `Gamma_R(s + kappa)` gives, after `t = 2x`, the kernel
`sum_k e^{-(2k + 1/2 + kappa) x}`; `kappa = 0` is zeta's `(2, 1/2)`; `kappa = 1/2, 3/2` give
`(2, 1), (2, 2)`, whose sum is `sum_{j>=1} e^{-jx} = 1/(e^x - 1) = rho_{1,1}`.

    D_shift = s_E(L) * (identity):  conductor `log N`, the `(2 pi)^{-s}` and `pi^{-s/2}`
              constants, the Euler-constant of the psi regularisation, the window-edge constants
              `w(L)`, `C(L)` of parent 1.2 recomputed for the new kernel.                  (D3)

`D3` moves `eps_N` only; `xi` and the spectrum do not see it (parent 1.2, the `c(L)` typo finding).
The reviewer is asked to DERIVE `s_E(L)` (parent plan risk list: "derivation, not transcription").

Window integrals for a general kernel `(d, mu)`, `P = 1` (D4; the parent's closed forms with
`2 -> d`, `1/4 -> mu/d`; `A_n = (mu - i omega_n)/d`, `z = e^{-dL}`, `e = e^{-mu L}`,
`S_1(n) = sum_k z^k/(k + A_n)`, `S_2(n) = sum_k z^k/(k + A_n)^2`, `S_1(0) = sum_k z^k/(k + mu/d)`;
uses `e^{i omega_n L} = 1`):

    I_1 = int_0^L sin(omega_n x) rho dx        = -(1/d) Im psi(A_n) - (e/d) Im S_1(n)
    I_2 = int_0^L x cos(omega_n x) rho dx      = (1/d^2) Re psi'(A_n) - (e/d^2) Re S_2(n) - (eL/d) Re S_1(n)
    I_3 = int_0^L (cos(omega_n x) - 1) rho dx  = (1/d)[psi(mu/d) - Re psi(A_n)] - (e/d) Re S_1(n) + (e/d) S_1(0)

    b_n^{(R)} = I_1/pi,   a_n^{(R)} = -2 [ I_3 - I_2/L ] + (constants, D3)                 (D5)

For `d = 2, mu = 1/2` these are the parent's formulas verbatim (regression anchor, Section 4, G1).
Consistency test built into the design: kernel `(1, 1)` must equal `(2, 1) + (2, 2)` to all digits.

Totals: `b_n = b^{(p)} + b^{(R)}`, `a_n = a^{(p)} + a^{(R)} + s_E(L)`. NO `W_{0,2}` term (D6).
Everything downstream (even/odd blocks, `eps_N`, `xi`, `D'' `, the secular function `g(s) = sum_j
xi_j/(j - s)`, real spectrum, `2N` roots) is the parent's, unchanged: the paper's theorems hold for
any real `D` (parent 1.1, Lemma `basics`). Recovered spectrum `= { gamma }` scaled by `2 pi / L`.

## 2. The scientific questions (what the tracer bullet is for)

Q1 (central zero; the point of choosing this object). For `w = -1` the zero set is symmetric about
`0` with a zero AT `0` of odd multiplicity `r`. CCM's spectrum is the `2N` real roots of an odd
`g`, symmetric, with a POLE at `0` unless `xi_0 = 0`. Hypotheses, mutually exclusive:
  H-a: the even-simple hypothesis FAILS for `w = -1` (the minimal eigenvector of the full Weil form
       is odd); the construction as stated does not apply and an odd-block variant is needed
       (parent Section 7, item 6). Then `w` would be visible as the parity of the minimal
       eigenvector: a striking statement, testable exactly (certified `min spec E` vs `min spec O`).
  H-b: even-simple holds; `xi_0 -> 0` and the smallest pair `+-s_1 -> 0` as `lambda` grows, so the
       odd-order central zero is represented as a pair straddling the pole at `0` (multiplicity
       doubled): a defect of the construction at the centre, quantified by the rate of `s_1`.
  H-c: something else (e.g. the count `2N` changes; a root at exactly `0` for a structural reason).
Rank `2` (`389a1`, `w = +1`): the double zero at `0` can be represented by a pair `+-s_1 -> 0`
without conflict; compare the rate with rank `1` and rank `0`.

Q2 (universality of the accuracy law). For zeta, `|z_1 - gamma_1| ~ 5e4 (1 - chi_4(lambda))`,
`e^{-4 pi x}` in `x = lambda^2`, N-independent for `N > 7.5 x`; the paper's heuristic ties this to the
prolate eigenvalue `1 - chi_4(lambda)` which does not know the L-function. Prediction to test: the
same exponential rate for `L(E, s)`, with a prefactor depending on `N` (through the atoms only) and on
the height of the zero (`10^{0.37 gamma}` law). If the rate differs between `N = 11` and `N = 389`,
the prolate heuristic is not universal.

Q3 (the conductor). Does the construction see `N` other than through `a_p`? By `D3`, only `eps_N`
does. Check: the spectra for two curves of different conductor but identical `a_p` for `p <= lambda^2`
(none among the test curves; construct by hand: replace the atoms of `11a1` by those of a fake with
shift `log 389`) must coincide to all digits.

Q4 (`eps_N`). Under GRH for `L(E, s)` the truncated form is positive; `eps_N > 0` certified, and its
decay in `lambda`. For zeta `eps_N ~ 10 (1 - chi_4(lambda))`. Same law? Sign of `eps_N` for a
rank-1 curve (Weil positivity includes `r |F(1/2)|^2 >= 0`, so still positive).

Q5 (bad primes). The degree-one Euler factors at `p | N` are atoms with weights `-a_p^m log p
p^{-m/2}`, `a_p in {0, +-1}`; `14a1` has two of them (`a_2 = -1, a_7 = +1`). Wrong bad-prime
handling shifts every zero; the pipeline must resolve it (test: drop the bad atoms and watch the
error).

## 3. Test curves (PARI, `cypari2` in the scratch venv; all pins to be regenerated by `tools/pari_ref.py`)

| label | `[a1,a2,a3,a4,a6]` | `N` | `w` | rank | `a_p`, `p = 2,3,5,7,11,13` | first zeros `gamma` |
|---|---|---|---|---|---|---|
| 11a1 | `[0,-1,1,-10,-20]` | 11 | +1 | 0 | -2,-1,1,-2,1,4 | 6.362613894713088702, 8.603539619290756001 |
| 14a1 | `[1,0,1,4,-6]` | 14 | +1 | 0 | -1,-2,0,1,0,-4 | 5.579286817429504275, 7.575711000888679021, 9.765547119459919408 |
| 37a1 | `[0,0,1,-1,0]` | 37 | -1 | 1 | -2,-3,-2,-1,-5,-2 | 0, 5.003170014006658696, 6.870391216954431949, 8.014330807872879223 |
| 389a1 | `[0,1,1,-2,0]` | 389 | +1 | 2 | -2,-2,-3,-5,-4,-3 | 0, 0, 2.876099071260465202, 4.416896083665257829, 5.793402633928365272 |

(`a_11 = 1` for `11a1`: split multiplicative; `a_37 = -1` for `37a1` (non-split; the draft said +1,
corrected by PARI); `a_389 = 1`; `14a1`: `a_2 = -1` non-split, `a_7 = 1` split. None of the four is
additive and all are good at 3: add a conductor-32 or -36 curve for additive reduction in char 2/3.) The zeros are lower than zeta's (`14.13`) and
denser for larger `N` (`9` zeros below `10` for `389a1`): windows will need to be larger in `N` for the
same accuracy at the same height; the prototype fixes the `(lambda, N)` map.

## 4. Deliverables, lanes, acceptance (one session, after the astra review)

Contract first (orchestrator): additions to `zst/include/zst.h` (the `zst_weil_t` data model of the
parent plan 3.2 restricted to `P = 1` kernels, plus `zst_weil_riemann`, `zst_weil_ellcurve`,
`zst_weil_ab`, `zst_ell_ap`, `zst_kernel_I123`), fixed before the workers start; the Makefile and
CLI flags. Workers on disjoint file sets, as for `ihz`.

- Lane A (Opus, prototype): `ell_proto.py` (mpmath; reuses `../ccm_proto.py` linear algebra): `a_p`
  by counting, `D1-D5` Loewner data with every closed form cross-checked against direct quadrature,
  even/odd blocks, `eps`, `xi`, secular roots; comparison with PARI zeros. Runs: four curves at
  `lambda^2 = 13, 30`, `N = 120`; the Q1 scan (`xi_0`, `s_1`, `min E` vs `min O`) for `37a1` and
  `389a1` over `lambda^2 = 8..40`; the Q3 shift test. Output: run records, and the 50-digit pins
  `(a_n, b_n)` for the C tests. Delivers first (the others pin to it).
- Lane B (Opus, C data model): `src/weil_data.c` (`zst_weil_t`, `zst_weil_ab`, constructors),
  `src/kernel.c` (`zst_kernel_I123`, general `(d, mu)`, polygamma + `z`-series with rigorous
  geometric tail via `mag`), `src/ellcurve.c` (`zst_ell_ap` by counting in `nmod`, minimal-model
  input; Satake power sums), tests `test_weil.c` (G1 regression: `zst_weil_riemann` vs the existing
  `zst_riemann_ab` at `x = 13, N = 40`, overlap within `1e-40`; the `(1,1) = (2,1)+(2,2)` identity),
  `test_ellcurve.c` (`a_p` vs PARI pins for all `p <= 100` on four curves; `(a_n, b_n)` vs Lane A's
  50-digit pins).
- Lane C (Opus, C pipeline and CLI): `src/ell_ref.c` (reference zeros loaded from
  `tests/data/ell_zeros.txt`, produced by `tools/pari_ref.py` with the PARI version and the command
  recorded), CLI `tools/zst.c --curve <label|a1,a2,a3,a4,a6> --x --N` printing the comparison table
  of the zeta driver, `--scan-central` (Q1 columns: certified `min E`, `min O`, `xi_0`, `s_1`, per
  `lambda`), `test_pipeline_ell.c` (G2 end-to-end anchor pinned to Lane A's numbers). Starts on the
  header, links against B at integration.
- Orchestrator: integration, `make check`, the report `report-ell.md` (Q1-Q5 answered or bounded,
  the `(lambda, N)` map, accuracy law vs zeta), worklog, HANDOFF.

Acceptance:
- G1: regression, zeta through the general data model reproduces `zst_riemann_ab` and `test_ab` pins.
- G2: `11a1`, `x = 13`, `N = 120`: certified even-simple, `2N` certified roots, `gamma_1 = 6.3626...`
  matched to the accuracy Lane A predicts (pinned), all zeros below `20` matched within their balls.
- G3: `37a1` and `389a1` `--scan-central` tables; a one-paragraph answer to Q1 with the certified
  numbers (H-a / H-b / H-c).
- G4 (optional, if the kernel builder is done early): real Dirichlet character `chi_{-4}`
  (`Gamma_R(s + 1)`, kernel `(2, 3/2)`, no pole, conductor `4`) against `acb_dirichlet_hardy_z` zeros:
  a second independent instance of D2/D3 with FLINT's own ground truth.
- Rules of the house as in `zst/README.md` (TDD; mutation and fuzz relaxed for the tracer bullet, as
  TJO allowed for `ihz`, to be done once the API settles; every formula cites the TeX by file and line
  or the prototype run record).

## 5. Environment notes

- PARI via `cypari2` in the scratch venv `$SCRATCH/venv` (`pip install cypari2` worked, wheels bundle
  PARI); not in the repo. `tools/pari_ref.py` must record the PARI version string and be runnable with
  any `python` that has `cypari2`; its output files are committed so the C tests never need PARI.
- `refs/src/2511.22755/mc2arXiv.tex` and `refs/src/2511.23257/Araki-final-oct25.tex` fetched,
  sha256 matches `refs/manifest.sha256`.
- FLINT 3.0.1 system-wide; `zst` and `ihz` build and pass here (2026-09-18).
- LMFDB's API is behind a captcha from this machine; PARI is the ground truth instead.

## 6. Risks and what would make this MVP fail

- The constants `s_E(L)` (D3) wrong: `eps_N` off by a constant, the spectrum unaffected; detectable by
  Q4 (sign/decay) and by the reviewer's derivation. Acceptable for G2, not for Q4.
- The kernel normalisation (coefficient of `D2`, or a missing factor `2` from `Gamma_C`) wrong: every
  zero shifts; caught by G2 against PARI. The `(2,1)+(2,2)` identity catches only internal errors.
- `H-a` true: the even-block pipeline returns nonsense for `37a1`; that IS the result, and the odd-block
  variant becomes the follow-up.
- The `(lambda, N)` regime for `N = 389` needs `N` beyond the tracer-bullet budget; then report `11a1`,
  `14a1`, `37a1` only.


## Review outcome (astra, 2026-09-18) and the revised plan

Full report: `astra-review.md` (698 lines; formula sheet F1-F18, derivation audit with TeX lines,
run records in `checks/`, Q1 analysis, 22-row correction ledger, hypothesis ledger, 7 recommendations).
What changed:

- **D1 corrected** (weights `-t_m log p / p^m`); **D3 derived** (F8/F9: `s_E(L) = log C_E - 2 log 2pi
  - 2 gamma_E - 2 log(1 - e^{-L})`, conductor enters as `+log C_E` on every `a_n`; the zeta constants
  of `riemann_ab.c` come out of the same general formula F10/F12); D2, D4, D5, D6 confirmed; the kernel
  is the SUBTRACTED functional `-int (q(y) - q(0)) rho(y) dy` (F2/F6), and a `(d, mu)` pair alone does
  not fix the constants: the data model must carry `(Q, d, mu, multiplicity)` per gamma factor and the
  conductor. Rigorous series tail F15.
- **Q1 answered structurally and numerically.** Under the paper's hypotheses `D''` is INVERTIBLE
  (`xi_0 = prod s_k^2/(N!)^2 > 0`): the construction cannot produce a central zero at finite `N` at
  all. Numerically the even-simple hypothesis FAILS for 37a1 at `x = 8, 13, 20` (`N = 60`) AND for
  389a1 at `x = 13`: the global minimum of the Weil form is in the ODD block (H-a supported, but it is
  not a root-number theorem: 389a1 has `w = +1`). The central multiplicity-`r` term is `r L |V_0><V_0|`,
  penalising only the even block. A `beta/B` odd-radical variant exists (derived, two central zero
  modes, loses the Fourier-determinant reading); an antiperiodic half-integer grid is the promising
  follow-up (H-HALF-GRID, open).
- **Accuracy is NOT zeta's.** 11a1 first zero: error `4.1e-4` at `x = 13, N = 60` (`N = 120` changes
  it by `3e-6`), `2.1e-9` at `x = 30, N = 120`: about 5.3 digits over `x = 13 -> 30`, versus zeta's
  92. Natural scale `sqrt(x / C_E)` (weight-2 Mellin kernel), H-RATE open. Q3 is an exact
  invariance (a unit test with predicted shift `log(C_new/C_old)`), Q4 needs `min O` for 37a1,
  Q5 needs a window above 37 for 37a1's bad prime.

Revised lanes (two Opus workers; Lane A of the draft is absorbed: `checks/ell_check.py` is the
independent prototype and produces the pins):

- **Lane B (C data model, `zst/src/kernel.c`, `weil_data.c`, `ellcurve.c`, `dirichlet.c`; tests
  `test_kernel.c`, `test_weil.c`, `test_ellcurve.c`).** Implement F2-F17 exactly: `zst_weil_t` with
  gamma factors `(Q, d, mu, mult)`, conductor, atoms, poles; `zst_kernel_I123` with the F15 tail;
  `zst_weil_ab`; constructors `zst_weil_riemann` (G1: reproduces `zst_riemann_ab` to `1e-40` at
  `x = 9, 13`, `N = 40`, INCLUDING the shift, i.e. the full `a_n`), `zst_weil_dirichlet` (real
  primitive character mod `q` by Kronecker symbol, `Gamma_R(s + kappa)`, `Q = pi^{-1/2}`, no pole,
  conductor `q`), `zst_weil_ellcurve` (F4/F5, conductor given), `zst_ell_ap` (F4). Pins: run
  `checks/ell_check.py` (or a small dump script beside it, in `checks/`) to 50 digits for 11a1 at
  `x = 13`, `N = 8`, and for `chi_{-4}`, `chi_{-3}`, `chi_5` likewise; test the `(1,1) = (2,1) + (2,2)`
  kernel identity; test the Q3 shift invariance with the predicted translation.
- **Lane C (pipeline, `zst/src/parity.c`, `ell_ref.c`, CLI, `test_parity.c`, `test_pipeline_ell.c`,
  `test_dirichlet_pipeline.c`).** `zst_block_min` (certified MINIMUM eigenpair of a block, not the
  smallest modulus: shift by a Frobenius bound first, as `ihz` does); `zst_parity` returning
  {min E, min O certified, which is smaller, gap}; the construction proceeds (sum normalisation,
  `xi_0 > 0` check, secular roots) ONLY when even-simple certifies, otherwise the CLI prints the
  parity result as the outcome ("odd minimum: construction inapplicable") with L2-normalised
  coefficients. CLI `--curve <label>` (labels from `tests/data/ell_ref.txt`, which carries the
  minimal model and conductor; no free-form models), `--chi <D>` (fundamental discriminant),
  `--scan-parity` (per `x`: min E, min O, parity, and for even-simple cases the first roots).
  G2 (rewritten): 11a1 at `x = 13, N = 60`: even-simple certified, `2N` roots complete, first zero
  within `5e-4` of PARI (measured `4.07e-4`); at `x = 30, N = 120` within `5e-9`. G2' (Dirichlet):
  `chi_{-4}` at `x = 13`: first zero `6.0209...` against `acb_dirichlet_hardy_z` root finding (or the
  PARI pin) within the tolerance the prototype measures. G3 (rewritten): parity scan of 37a1 and
  389a1 at `x = 8, 13, 20` reproducing the review's table (`min E, min O`) as certified balls; the
  odd minimum is the RESULT. Zeta regression `make check` stays green.
- Orchestrator: header contract (done, revised), integration, `report-ell.md` with the parity
  tables, the 11a1 accuracy points and the H-RATE fit on `sqrt(x/C_E)` vs `x`, worklog, HANDOFF.

Deferred (separate research questions, not this MVP): the odd/antiperiodic construction
(H-HALF-GRID), a universal accuracy law, faithful central multiplicity.
