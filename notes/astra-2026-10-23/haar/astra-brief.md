# Lane H: RH on average for every compact gauge group — exact Haar averages of twisted characteristic polynomials

You are `codex:gpt-6-astra`, a prover and constructive verifier in a mathematical research notebook (git repo, current
directory). Read `notes/astra-2026-10-23/brief.md` first (binding). Then read `notes/adelic-gkp/zn-flux.md` (the Z_N result: the
average over all Z_N fluxes of det(x − A_ρ) is the matching polynomial, for every N), `notes/adelic-gkp/graph-super.md` §6 (RH on
average, Z_2), `notes/adelic-gkp/gauge-groups.md` (SU(2), U(d), S_d paragraph: "the U(d) Haar average is not the matching
polynomial (balanced tree-like trails survive)"; "Next": compute the exact SU(2) and U(2) Haar averages for K_4 by Weingarten before
saying anything about their roots), and `notes/adelic-gkp/checks/check_zn_flux.py`. Known literature (cite from memory with
author, title, year; if `refs/src/` has it, cite by line): Godsil–Gutman and Heilmann–Lieb (the matching polynomial of a
(q+1)-regular graph is real-rooted with roots in (−2√q, 2√q)); Hall–Puder–Sawin, "Ramanujan coverings of graphs" (Adv. Math.
2018): the expected characteristic polynomial of the new part of a random d-cover (S_d, standard representation) is the
d-matching polynomial, real-rooted with roots in the band; Bordenave–Collins (2019): strong convergence of random U(d) or S_d
lifts. Write only `notes/astra-2026-10-23/haar/{astra-proofs.md,progress.txt,checks/}`.

## 0. Setting

Y finite connected (q+1)-regular, n vertices, m edges, cycle rank g = m − n + 1. G a compact group, ρ: G → U(d) an irreducible
unitary representation, nontrivial. A G-gauge field assigns s(e) ∈ G to oriented edges with s(ē) = s(e)^{-1}; the twisted adjacency
A_s^ρ acts on C^n ⊗ C^d by (A f)(x) = Σ_{e: x→y} ρ(s(e)) f(y) (Hermitian). Gauge-fix on a spanning tree: the field is determined up
to gauge by its holonomies (h_1, …, h_g) ∈ G^g around a fundamental cycle basis, and Haar measure on G^g is the gauge-invariant
average. Define the ρ-averaged polynomial p_{Y,ρ}(x) = ∫_{G^g} det(x − A_s^ρ) dh. For G = Z_N and ρ a faithful character the
record says p = (matching polynomial)^? — check the exact statement in `zn-flux.md` (degree n for the character; the average of
det(x − A_ρ) over the N^g fluxes equals the matching polynomial μ_Y(x) of Y, with the trivial mode gone).

## 1. The conjectures

H1 (RH on average for every compact gauge group). For every Y, G, ρ as above, p_{Y,ρ}(x) is real-rooted and all its roots lie in
[−2√q, 2√q]. (For d = 1 this is Godsil–Gutman/Heilmann–Lieb; for S_d standard it is Hall–Puder–Sawin; the conjecture is the
claim for every compact G and irreducible ρ, in particular U(d) Haar for every d and SU(2) with its spin-j representations.) Prove
it, or refute it with the smallest exact counterexample.

H2 (the ρ-trail polynomial). p_{Y,ρ}(x) = Σ_k (−1)^k c_k(ρ) x^{nd − 2k}... derive the correct expansion: expand det(x − A) as a sum
over permutations / over "cycle covers" of the vertex set, write the Haar integral of each term as a product over the closed
walks of the cover of ∫ χ-type expressions (use ∫_G ρ(h)_{ij} ρ(h)_{kl}^* dh = δ_{ik}δ_{jl}/d (Schur orthogonality) and Weingarten
for higher moments), and identify p_{Y,ρ} as a signed count of subgraphs whose components are edges and cycles with a weight
w_ρ(C) per cycle. For d = 1 the cycle weight is ∫ χ(h)^{wind} = 0 unless the holonomy is trivial, which kills every cycle and leaves
the matchings; for d ≥ 2 the cycle weights are the moments of ρ. Give the exact formula for SU(2), spin 1/2, on K_4 (Weingarten in
the three cycle variables is small: do it symbolically with sympy or by exact character integration) and for U(2) Haar, and compare
with the matching polynomial and with the Hall–Puder–Sawin 2-matching polynomial.

H3 (the large-d limit). For G = U(d), ρ the defining representation, the roots of p_{Y,ρ} (nd of them) have an empirical
distribution that converges, as d → ∞, to the Kesten–McKay law of the (q+1)-regular tree, and all roots stay in the band for every
d (= H1 for U(d)). State what is provable from strong convergence (Bordenave–Collins) and what is not (an expected characteristic
polynomial is not the characteristic polynomial of the expected measure).

H4 (finite groups, exact). For G finite and ρ irreducible, p_{Y,ρ} is an exact finite sum over G^g. Conjecture: it depends on ρ only
through the sequence of "cycle moments" m_k(ρ) = ∫ χ_ρ(h^k)... no — through the full moment data of ρ (H2); and H1 holds for every
finite G. Test exactly (integer arithmetic over cyclotomic fields or floating with error bounds) on: Q_8 (2-dim irrep), S_3
(2-dim), the binary tetrahedral group 2T of order 24 (its 2-dim faithful irreps: these are nonabelian subgroups of SU(2), so this
is the exact SU(2)-subgroup version of H1), 2O (48) if the sums are small enough, and A_5 (3-dim) if feasible, on K_4 (g = 3),
K_{3,3} (g = 4), the cube (g = 5), the Petersen graph (g = 6: 24^6 ≈ 2·10^8 terms of 20×20 determinants is too many for python;
sample or use the cycle structure of H2 to reduce). For each, print the polynomial exactly (or to 12 digits), its roots, and the
verdict on real-rootedness and the band.

## 2. Numerics (checks/)

`checks/haar_finite.py` (H4, exact), `checks/haar_mc.py` (U(2), SU(2) spin 1/2 and spin 1, U(3): Monte Carlo of E det(x − A) with
10^5–10^6 samples on K_4 and the Petersen graph, with standard errors, and the roots of the estimated polynomial with error
bars; this is a check of H1, not a proof), `checks/haar_weingarten.py` (H2: the exact SU(2) and U(2) averages for K_4 by
Weingarten/character integration; compare with the Monte Carlo). Outputs to `checks/output_*.txt`.

## 3. Output

`astra-proofs.md`: §0 setting and the gauge-fixing lemma (PROVED); §1 H2 the exact formula (PROVED, with the K_4 polynomials
printed); §2 H1: proof or counterexample (if a proof: via interlacing families / real stability (Marcus–Spielman–Srivastava,
Hall–Puder–Sawin) or via a positivity of the cycle weights; if a counterexample: the exact group, representation, graph and the
root outside the band or off the real axis, certified); §3 H3; §4 H4 tables; correction ledger; "Numerical checks for the blind
lane"; "What this changes in the notebook" (candidate rows; the correction to `gauge-groups.md`'s U(d)/SU(2) paragraph; whether
"RH on average" is a property of the group or of the graph).
`progress.txt`: H0, H2, H1, H3, H4, NUM.
