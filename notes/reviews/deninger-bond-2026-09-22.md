# REFUTE review: Deninger's package on the GL_1 bond (lane `notes/deninger-bond`)

Reviewer: `claude:fable-5.1` (hostile REFUTE protocol). Author under review: `codex:gpt-6-astra`. Date: 2026-09-22.
Files: `notes/deninger-bond/astra-brief.md` (the brief, author `claude:fable-5.1`), `notes/deninger-bond/astra-proofs.md`
(660 lines, C1–C7, Sections 0–10). Notebook sources consulted: `report/sections/04q_h_theta.tex`, `04r_h_theta_channels.tex`,
`04p_gl1_bond.tex`, `04l_elliptic_cavity_channel.tex`, `04k_elliptic_cavity_scattering.tex`, `04b_phantasm_forced.tex`,
`02h_definitions_graded_ramanujan.tex`, `08b_weil_positivity.tex`, `08c_weil_positivity_continuous.tex`,
`notes/h-theta/astra-proofs.md`, `notes/weil-positivity.md`, `notes/weil-positivity/astra-proofs.md`,
`notes/deninger-lps/src/manuscript.txt`; external sources `refs/src/math/9811068` (Connes), `0311468` (Meyer),
`0001013` (Burnol).

Independent checks: 51 numerical assertions in three scratch scripts written from the text before opening the
author's `checks/check_identities.py` (mpmath zeros from `zetazero`, not the data file, for the Weil form; the
data file only for the smallest-gap statistic), 30 byte-cited line ranges read against the local files, 5
convention checks against 04q/04r/04h. Author's script opened afterwards and found to test the same identities
by the same route (six-mode matrices, synthetic jets, Gaussian Weil form, CM counts); my checks are independent
implementations.

## Conventions (Section 0)

Checked line by line against `04q_h_theta.tex:26–39` and `04r_h_theta_channels.tex:77–92`: `U_t f(y) = f(e^{-t} y)`,
Mellin image `e^{it tau}`, outgoing half `X > 0` ↔ `H^2(C_+)`, `Z_t = P_K M_{e^{itu}}|_K` forward, `C_t = Z_t^*`
carrying the damped modes `m_rho = e^{lambda_rho X} 1_{X>0}`, `lambda_rho = (conj(rho) - 1)/2 = -i conj(w_rho)`,
`hat m_rho = i k_rho` (verified symbolically and numerically). The brief's placement of the damped modes on `Z_t`
was indeed wrong; the author's correction agrees with `thm:model-space-jets` ("`C_t` acts by `e^{-it conj w}` on
the ordinary modes"). Riemann–von Mangoldt is correctly identified as the analytic input recorded in
`04b_phantasm_forced.tex:96–101` (`asm:zero-count-location`, no RH).

## C1 — VALID (sharpened)

`U_t 1 = 1`, `U_t y^{-1/2} = e^{t/2} y^{-1/2}`; the decaying rates `0, -1/2` belong to `U_{-t}`, i.e. to the left
translation `C_t`; `q_t = e^{-t/2}` is the ratio of exponentiated reference rates, midpoint `-1/4` (checked against
`02h:41–46`). (1.2) is immediate. The functional equation (1.3) was verified on a random real symplectic
similitude of genus 3 with `q = 0.37 < 1` (relative residual `< 1e-9`), confirming that the finite note's
determinant proof extends to contraction time; the author is right that Theorem 6.2's hypothesis `q > 1`
(`manuscript.txt:648–659`) is not literally satisfied. The remark that the cup product `x ⌣ y = Omega(x, y) eta`
produces only the algebraic shape of Definition 6.1 (`manuscript.txt:644–647`) is correct and appropriately
modest.

## C2 — VALID (sharpened)

Existence: `Omega(C_t x, C_t y) = q_t Omega(x, y)` for all `t` forces `lambda_rho + lambda_nu = -1/2`, i.e.
`nu = 1 - rho` (checked). Formula (2.1): I implemented the jet action (0.1) and the anti-diagonal alternating
pairing independently for a synthetic off-line partner pair `rho = 0.7 + 2.1i`, `1 - rho`, chain lengths
`m = 1, 2, 3, 4`; the similitude `C_t^T Omega C_t = e^{-t/2} Omega` holds to `5e-17` and the form is alternating for
every `m`. Reality: conjugating `rho` conjugates `(-i sgn gamma)^m`; the brief's `sgn gamma` is anti-real
(`Omega(R x, R y) = -conj Omega(x, y)`), so the author's correction stands. `xi` has no real zeros
(`04q:93–97`), so no root is fixed by `rho -> 1 - rho`. The Hankel/model-conjugation argument (2.5)–(2.6) is
correct: `R` preserves `K` because `conj(Theta(-u)) = Theta(u)` (verified numerically at two points with
mpmath `xi`, `|Theta| = 1`), `H_Theta = C_Theta R` is a linear unitary involution and intertwines `C_t` with `Z_t`,
not with `q_t C_t^{-1}`; the naive Poisson form (2.4) vanishes on `K x K` (supports disjoint). The Burnol quote
`0001013/main.tex:230–235` (E intertwines Fourier with inversion) is verbatim. Verdict: the brief's "Poisson
supplies the pairing" is correctly refuted; (2.1)/(2.3) is a genuine construction on the algebraic jet span.

## C3 — VALID (proved with qualifications)

Necessity (3.2): `lambda_rho + conj(lambda_nu) = -1/2` iff `nu = 1 - conj(rho)`; positivity on the diagonal forces
`sigma = 1/2`. Jordan obstruction: for a critical double zero I computed `q_t^{-1} ||C_t e_1||^2 = 1 + t^2`
(`1.25, 2, 5` at `t = 0.5, 1, 2`), so no invariant positive form exists on a jet of length two. Transcription of
Theorem 5.2: the two-sided-powers point (`manuscript.txt:530–599`) is correctly noted; the finite symplectic
argument that forward boundedness suffices (spectrum of an `Omega`-Hamiltonian is symmetric under
`mu -> -mu`) is right. The star: in the real basis `u = (e_+ + e_-)/sqrt2`, `v = i(e_+ - e_-)/sqrt2` I get
`Omega(u, v) = -1`, and the construction (3.3) from the certificate `G = g I` returns `J = -Omega`, `J u = -v`,
`J v = u`, `Omega J = G R = I` for `g = 1` and `g = 3.7` alike: the compatible metric is fixed by `Omega`, the
certificate weights are free, exactly as stated. The refutation of the brief's "no symmetry acts transitively" by
the diagonal commutant is a fair reading of an ambiguous sentence; the substantive point (the listed symmetries
preserve `|gamma|` and cannot equate different weights, unlike the D2 parity of `04l:160–164`) is correct.

## C4 — VALID (proved; the load-bearing result is confirmed and sharp)

4.1: Step 1 (restriction to finite root spans forces RH and simplicity by C3), Step 2 (`G`-orthogonality of
`C_t`-eigenvectors with distinct unimodular eigenphases), Step 3 (bounded equivalence + orthogonality +
completeness = Riesz basis, contradicting `04r:94–105`) are all correct. `||k_{a + i/4}||^2 = 2` with `du/2pi`
verified (`2.000000000000000`). 4.2, the new theorem `sup_t e^{t/4} ||Z_t|| = infinity` unconditionally: the
three-case split is complete (off-line zero: `e^{t(sigma - 1/2)/2}` growth; multiple zero: jet growth `1 + t^2`;
RH with simple zeros: close pairs). For the close-pair case I computed the exact operator norm of `e^{t/4} C_t`
restricted to the two-mode span in the energy metric (generalised eigenproblem with the Gram
`M_ab = 2/(1 + i(s_a - s_b))`, itself verified against a direct integral): at `t_* = 2 pi/|gamma - delta|` it
equals `sqrt((1 + r)/(1 - r))` to six decimals for the first two zeros (`1.155680`) and for the closest pair among
the first 3000 ordinates (gap `0.0975` at `1977.17`, `r = 0.99528`, norm `20.560930`). So (4.4) is not only a
lower bound, it is attained on the two-mode span. Gaps tending to zero under bounded multiplicity is
`04r:99–103` / `notes/h-theta/astra-proofs.md:745–774` (verified present), which rests on `N(T) ~ T log T`. Hence
"unconditionally" is earned modulo `asm:zero-count-location`, which the author names. 4.3 (a uniformly bounded
semigroup with dense unimodular eigenvectors unitarises) is a correct proof: recurrence of finitely many phases
gives `||f|| <= M ||T_s f||`, closed range plus dense range gives a bounded group, Cesàro averaging gives the
invariant metric. 4.4 (bounded injective non-coercive invariant forms exist; the unit-weight form is a closed
unbounded form) is correct and is the right qualification of the brief's "unbounded metric".

## C5 — VALID (refuted as stated; corrected statements proved)

Normalisation: `F_f(s) = int f(t) e^{(s - 1/2) t/2} dt` and `F_h = F_f(s) conj F_f(1 - conj s)` for
`h = f * tilde f` match `08c:109–121` (`hat g_zeta`), `notes/weil-positivity.md:13–18` and
`notes/weil-positivity/astra-proofs.md:877–890` (H-ZEF, which is (5.3) verbatim); I verified the convolution
identity symbolically at a complex point. The explicit formula (5.3) was rebalanced independently for the
Gaussian `a = 1/50`: zero side `2 sum e^{-a gamma^2/2}` with 60 zeros from `mpmath.zetazero` gives
`0.29939602250755915578916...`; analytic side (`2 e^{a/8} = 2.00500625521159017`, `-2 log(pi) h(0) =
-3.22922338786021838`, gamma integral `1.52362995414787428`, prime powers to 1000 `-1.6799e-5`) gives the same
number, difference `2.5e-31`; the author's `0.2993960225075590798` from the float64 data file differs by `7.6e-17`,
as it says. The Weil criterion is stated as external and matches `cit:weil-criterion` (`08c:128–138`) and Meyer
`0311468/main.tex:270–287` (verbatim: "positive definite if and only if the spectrum of `pi_-` is contained in the
critical line"). The argument that a trace cannot select diagonal weights (rescaling `e_rho -> e_rho/sqrt g_rho`
leaves every entry `F_h(rho)` unchanged) is argued, not asserted, and is correct; the brief's "canonical point =
Weil's form, forced by the trace formula" is therefore rightly refuted. The three-space distinction (full jets:
RH + simplicity; diagonal semisimplification: RH only, with a genuine unitary group `e^{t/4} T_t`; Weil test
quotient: blind to jets, `manuscript.txt:733–758`, `08c:89–105`) is correct. Connes quotes `9811068/main.tex:755–765`
(the weighted representation is not unitary), `873–885` (Theorem 1, multiplicity `n < (1 + delta)/2`), `2549–2556`
(`delta = 0`: surjective isometry) and Meyer `208–227`, `249–269`, `298–316` are verbatim. `thm:kraus-weil-criterion`
is indeed the finite discrete theorem at `08b:159–170`. 5.4 (the kernel-analysis map is closed, injective, densely
defined, unbounded both ways; not Bessel by the `T log T` clustering) is correct.

## C6 — VALID (refuted literally; open as a programme)

`Z log p + Z log r` is dense in `R` (irrational ratio), so the two-prime orbit quotient is non-Hausdorff; the
brief's "solenoid" is wrong as stated, and the `S`-adic solenoid `(R x Q_p x Q_r)/Z[1/pr]` is the standard
replacement. The Koszul complex of two commuting transports is the natural meaning of "horizontal cohomology"
and is correctly left OPEN. The Bass-doubling warning transcribes Proposition 9.3 (`manuscript.txt:1188–1254`).

## C7 — VALID (proved with qualifications)

Point counts of `y^2 = x^3 - x` by exhaustive enumeration: `#E(F_5) = 8`, `#E(F_13) = 8`, `#E(F_17) = 16`; the
primary generators (`a` odd, `b` even, `a + b = 1 mod 4`, i.e. `pi = 1 mod (1 + i)^3`) are `-1 +- 2i`, `3 +- 2i`,
`1 +- 4i`, and `#E = p + 1 - 2a = |pi - 1|^2` in every case; the author's table (7.3)/(8.3) is reproduced,
including the negative real part at `p = 5` (choosing `1 + 2i` would give `#E = 4`, a twist). The eight listed
points of `ker[(1 + i)^3]` lie on the curve over `F_13` with `i = 5`. The torus identities (7.1) (`A^T Omega A =
q Omega`, `A J = J A`, `Omega J = I`, `A^T A = q I`) and `det(A^n - I) = |alpha^n - 1|^2` for `n = 1, 2, 3` hold for
all three `alpha`, so (7.2) is proved as stated (`manuscript.txt:765–820` matches). The scope statements
(equality of zetas is not an identification of the class-group bond `l^2(Pic^0) (x) l^2(Z)` with the
two-dimensional `H^1`; the flat metric lives on the complex lift; D2 is `y^2 + y = x^3 + x + 1` over `F_2`,
`04k:35–40`, not the singular `y^2 = x^3 - x`; the genus-one ray comparison is the vacuous case of `04p:112–121`)
are all correct.

## Verdict lines

```
VERDICT C1: VALID
VERDICT C2: VALID
VERDICT C3: VALID
VERDICT C4: VALID
VERDICT C5: VALID
VERDICT C6: VALID
VERDICT C7: VALID
```

## MINOR fixes (wording and registration only; no verdict is MINOR)

1. C4 registration: list `asm:zero-count-location` (04b) among the dependencies of the unboundedness theorem
   (the RH-with-simple-zeros case uses `N(T) ~ T log T` through `04r:99–103`); the gate will then derive
   `proved-conditional`, which is the honest status.
2. C4 (4.4): the text presents `sqrt((1 + r)/(1 - r))` as a lower bound; it is the exact operator norm of
   `e^{t_*/4} C_{t_*}` on the two-mode span (checked to six decimals), which could be stated.
3. Section 8.2: say explicitly that "3000 zeros" are the positive ordinates of the float64 data file and that the
   `7.6e-17` residual is that file's rounding (the author's own footnote implies it; an mpmath recomputation with
   60 zeros closes the gap to `2.5e-31`).
4. (7.3): "up to conjugation" should be read as "the two primes above `p` give `pi` and `conj pi`"; my enumeration
   lists both, consistent with the author's table.

## Assessment

The corrected statements are sound. Of the brief's original claims, the following are now settled negatively:
the Poisson involution alone does not supply the invariant pairing (it maps `K` into `H^2_-`); the Weil form is
not selected as "the canonical metric" by the trace formula (the trace is blind to diagonal weights) and the full
jet realisation needs simplicity beyond RH; the two-prime orbit quotient is not a solenoid; the genus-one
torus/Hodge comparison is vacuous. Settled positively, and stronger than the brief asked: on the model space with
the bond norm there is no boundedly equivalent invariant positive metric even under RH with simple zeros, and
`sup_t e^{t/4} ||Z_t|| = infinity` unconditionally, with an elementary two-mode proof whose bound is sharp. The
transcription of the finite polarization criterion to the jet span (positive invariant metric iff critical and
simple; the star `J e_rho = -i sgn(gamma) e_rho` with `Omega J = I` fixed by the normalised pairing) is correct and
registrable. The CM torus identification is exact at split primes with the primary Frobenius.
