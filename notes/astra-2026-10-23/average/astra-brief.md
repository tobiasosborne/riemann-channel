# Lane A: RH on average over F_q(t), exactly — the geometric (cover) ensembles versus the level ensembles

You are `codex:gpt-6-astra`, a prover and constructive verifier in a mathematical research notebook (git repo, current
directory). Read `notes/astra-2026-10-23/brief.md` first (binding). Then read `notes/adelic-gkp/graph-super.md` §6 and §9 ("RH on
average over fluxes": the average over all Z_2 fluxes of det(x − A_s) is the matching polynomial, real-rooted in the band; §9
"Averaging for zeta: the flux average is an average over characters of H_1. Ask what the analogue is for the adelic code: an
average over a family of Hecke characters whose averaged zeta is manifestly on the line"), `notes/adelic-gkp/zn-flux.md` (Z_N
fluxes: the N-torsion average is the matching polynomial for every N), `notes/adelic-gkp/ff-dirichlet.md` (lane J: Dirichlet
characters of F_q(t), the L-polynomials, `checks/check_ff_dirichlet.py`), `notes/adelic-gkp/family-vacuum.md` (lane M: CM-type
commuting families share a vacuum; Hecke-type families do not). Literature to cite from memory: Rudnick, "Traces of high powers
of the Frobenius class in the hyperelliptic ensemble" (Acta Arith. 2010); Katz–Sarnak (the hyperelliptic ensemble, symplectic
symmetry); Bucur–David–Feigon–Lalín (cyclic ℓ-covers, unitary symmetry); Rosen, "Number theory in function fields" (quadratic
reciprocity in F_q[x], squarefree counts); Eneström–Kakeya theorem on the roots of polynomials with positive monotone coefficients;
Heilmann–Lieb / Godsil for the matching polynomial. Write only `notes/astra-2026-10-23/average/{astra-proofs.md,progress.txt,checks/}`.

## 0. The analogy to make exact

On a graph the family of Z_2 fluxes is the family of double covers; the flux average of the characteristic polynomial is the
matching polynomial, whose roots are real and in the band for every graph ("RH on average"), and the mechanism is that every
cycle averages to zero. Over F_q(t) the family of double covers of P^1 is the hyperelliptic ensemble y² = D(x), D monic squarefree
of degree d, with L-polynomial L(u, χ_D) of degree d − 1 (d odd: 2g = d − 1; d even: say what happens at infinity and fix one
convention, e.g. d = 2g + 1 throughout, and treat d = 2g + 2 as a check). The analogue of "RH on average" is:

A1 (hyperelliptic ensemble). For q odd and every g ≥ 1 the average L̄_{q,g}(u) = |H|^{-1} Σ_{D ∈ H} L(u, χ_D) over H = {D monic
squarefree of degree 2g + 1} has all its 2g roots on the circle |u| = q^{−1/2}. (Note: this is not implied by Weil's RH for the
individual L(u, χ_D): an average of polynomials with roots on a circle need not have its roots on it. The claim is a statement
about the family, like the matching polynomial.)

A2 (the exact average). Derive L̄_{q,g}(u) exactly: L(u, χ_D) = Σ_{f monic, deg f ≤ 2g} χ_D(f) u^{deg f}; swap the sums; the
average ⟨χ_D(f)⟩_D over squarefree D of degree 2g + 1 is: for f = g_0² h with h squarefree, χ_D(f) = 1_{(D, g_0) = 1} χ_D(h), and
Σ_D χ_D(h) over squarefree D of fixed degree is a character sum which quadratic reciprocity turns into a sum of χ_h(D) over
squarefree D, whose generating function in u is L(u, χ_h) / L(u², χ_h²)-type (derive it: Σ_{D squarefree} χ_h(D) u^{deg D} =
L(u, χ_h)/L(u², χ_h^2) with the right local corrections at the primes dividing h; and Σ_{D squarefree, (D, g_0) = 1} u^{deg D} =
(1 − q^{-1}... give the exact rational function). So L̄ is an exact finite expression: a main term from the squares f = g_0²
(Σ_{m ≤ g} c_m (q u²)^m with c_m the density of squarefree D coprime to a random monic g_0 of degree m, computed exactly) plus
an exact "non-square" remainder that is itself a sum over h of L(u, χ_h)-type terms of lower degree. Write both down, prove the
formula, and verify it against brute force (enumerate H for q = 3, 5, 7 and g = 1, 2, 3, i.e. up to 7^7 ≈ 8·10^5 polynomials;
point-count y² = D(x) over F_{q^k}, k ≤ g, to get L(u, χ_D) exactly, or compute the character sums directly).

A3 (proof route for A1). The average inherits the functional equation L̄(u) = (q u²)^g L̄(1/(qu)) from each member. If the
coefficients of L̄ in the variable w = q u² (after showing the odd-degree coefficients vanish or handling them) are positive and
monotone, Eneström–Kakeya puts all roots in |w| ≥ 1, and the functional equation reflects them to |w| = 1, i.e. |u| = q^{−1/2}.
Decide whether the exact coefficients of A2 are monotone, for which (q, g); prove A1 where they are; where the Eneström–Kakeya
route fails, test A1 numerically to high precision and find the right proof or the counterexample. State the result as a
theorem with its exact hypotheses.

A4 (the other ensembles; the dichotomy). Compute the same average for: (i) the even-degree hyperelliptic ensemble d = 2g + 2;
(ii) the cyclic cubic ensemble y³ = D(x) over F_q with q ≡ 1 mod 3 (characters of order 3; the Z_3-flux analogue; L(u, χ_D) of
the cubic character, degree d − 1 or so): is the average on the circle; (iii) the LEVEL ensemble: all non-trivial characters χ mod
f for a fixed irreducible f of degree d (the "Dirichlet characters mod f" family of lane J): the orchestrator computed that
Σ_{χ ≠ 1} L(u, χ) = N(u)/(1 − qu) with N(u) = q^d u^d − (q^{d+1} − q) u + (q^d − 2) for f irreducible of degree d, q the field
size (re-derive; it uses only that L(u, χ_0) = (1 − u^d)/(1 − qu) and orthogonality: Σ_χ χ(D) = φ(f) 1_{D ≡ 1 mod f}); its roots are
NOT on the circle in general (check d = 2, 3, q = 3, 5): RH on average fails for the level ensemble; (iv) the ensemble of all
primitive characters of order exactly N mod f (the Z_N "fluxes at level f"): on the circle or not. Conjecture A4: RH on average
holds exactly for the geometric ensembles (covers of P^1 parametrised by the branch divisor D: double, cyclic, and conjecturally
every family of covers with fixed Galois group as D varies) and fails for the level ensembles (characters of a fixed modulus),
in exact parallel with lane M's finding that commuting CM-type families share a vacuum and Hecke-type families do not. Prove
as much of A4 as you can (the geometric case by the A2–A3 mechanism; the level case by the explicit formula above) and say
exactly what the dichotomy is in the ladder's terms (which average is "over the fluxes of a fixed H_1" and which is not).

A5 (for zeta; reading only, no computation needed beyond a formula). The analogue over Q of the hyperelliptic ensemble is the
family of quadratic Dirichlet L-functions L(s, χ_d) over fundamental discriminants |d| ≤ X. State what "RH on average" would mean
there (the average of the completed L-function's ... there is no polynomial; propose the right object: the average of
Λ(s, χ_d) over the family as a function of s, or the average of the zero-counting measure, or the average of the Weil form) and
what A1–A3 predict about it. One page, labelled OPEN/HEURISTIC. Do not use zeros.

## 2. Numerics (checks/)

`checks/avg_hyperelliptic.py` (brute-force averages, q = 3, 5, 7, g = 1, 2, 3; roots and |u|√q to 12 digits; the exact formula
of A2 evaluated and compared), `checks/avg_cubic.py` (q = 7, 13; d ≤ 4), `checks/avg_level.py` (the level ensemble, exact
rational-function check). Exact arithmetic (fractions / sympy) for the formulas; numpy roots with a condition-number check for the
roots. Outputs to `checks/output_*.txt`.

## 3. Output

`astra-proofs.md`: §1 A2 (PROVED, the exact formula, brute-force agreement table); §2 A1/A3 (PROVED with hypotheses, or REFUTED
with the smallest (q, g) and the off-circle root); §3 A4 per ensemble with verdicts; §4 A5; correction ledger; "Numerical checks for
the blind lane" (L̄_{3,1}(u) and L̄_{5,2}(u) as exact polynomials; the maximal | |u|√q − 1 | over the roots); "What this changes
in the notebook" (candidate rows; the line `graph-super.md` §9 "Averaging for zeta" should now carry; whether the dichotomy belongs in
`data-ladder.md` §2 as a negative finding or §4 as a positive one).
`progress.txt`: A2, A1, A3, A4i, A4ii, A4iii, A4iv, A5, NUM.
