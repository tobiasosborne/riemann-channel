# Lane A2: RH on average for the hyperelliptic ensemble over F_q(t), every genus — prove or refute H-half

You are `codex:gpt-6-astra`, a prover and constructive verifier. Read `notes/astra-2026-10-25/brief.md` first (binding), then
`notes/astra-2026-10-23/brief.md`, then lane A of the previous round in full: `notes/astra-2026-10-23/average/astra-brief.md`,
`astra-proofs.md` (§1 the exact Euler-product formula (1)–(5), §2 the functional equation and H-half, the certified ranges,
the cubic refutation §3, the level ensembles), `checks/avg_hyperelliptic.py`, `avg_extended.py`, `summarize_outputs.py` and the
saved outputs. Background: `notes/adelic-gkp/ff-dirichlet.md`, `notes/adelic-gkp/graph-super.md` §9. Literature from memory:
Katz–Sarnak (the hyperelliptic ensemble has USp(2g) monodromy; the Haar average of det(1 − zU) over USp(2g) is Σ_{m=0}^g z^{2m}, all
roots on |z| = 1); Rudnick, "Traces of high powers of the Frobenius class in the hyperelliptic ensemble" (Acta Arith. 2010: exact
formulas for the average of tr Frob^k over H_{2g+1,q}; the square-contribution term and the −1 at even k); Andrade–Keating (mean
values of L(1/2, χ_D) over the hyperelliptic ensemble; the square-vs-nonsquare split); Bucur–David–Feigon–Lalín (statistics for
cyclic trigonal covers); Rosen, Number Theory in Function Fields. Write only in `notes/astra-2026-10-25/hhalf/`.

## 0. The object

q odd, H_d the monic squarefree D of degree d = 2g + 1 (|H_d| = q^d − q^{d−1}), χ_D(f) = (f/D), L(u, χ_D) = Σ_{f monic} χ_D(f) u^{deg f}
a polynomial of degree 2g (odd d: χ_D is odd, no completion needed), L̄_{q,g}(u) = |H_d|^{−1} Σ_{D ∈ H_d} L(u, χ_D). Lane A proved
L̄_{q,g}(u) = B_{q,g}(w), w = q u², B of degree g with the exact coefficients (3)–(5) (square part c_{d,m}, nonsquare remainder R_d),
reciprocal (b_{g−m} = b_m), b_0 = 1, and showed: all roots of B on |w| = 1 (⟺ A1: all roots of L̄ on |u| = q^{−1/2}) for g ≤ 3 and
in the certified ranges (3, 1:12), (5, 1:8), (7, 1:6); in every case the stronger inequality 1 = b_0 ≥ b_1 ≥ … ≥ b_{⌊g/2⌋} > 0 held.
By Rudnick, the average of tr Frob^k over H_{2g+1} is −1 for even k ≤ 2g (minus a correction from squares of degree k/2 that
vanishes… — recover his exact formula and the range where it is exact) and o(1) for odd k; this gives the coefficients of
log B̄ and so of B in closed form up to a controlled error — the route to a uniform proof.

## 1. The conjectures (in order of priority)

A2-1 (H-half for all (q, g)). Prove: for every odd q and g ≥ 1 the coefficients of B_{q,g} satisfy 1 = b_0 ≥ b_1 ≥ … ≥ b_{⌊g/2⌋} > 0.
Routes: (i) from the exact square density (5): c_{d,m} is a coefficient of an explicit rational generating function — extract
b_m = main term (from squares, a q-adically small perturbation of 1) + remainder (nonsquares, of size O(q^{−something}·…)); show the
main term is decreasing in m for m ≤ g/2 and dominates the remainder; (ii) from Rudnick's trace formula: write B(w) = exp(Σ_k
(−1)^{?} s_k w^k / k) with s_k = average of tr Frob^k, s_k = −1 + O(q^{−k/2}… ) exactly known for k ≤ 2g; then B is a perturbation of
Σ_{m} w^m = (1 − w^{g+1})/(1 − w) — prove its coefficients stay monotone. Also try to find a counterexample: large g at q = 3 (compute
B_{3,g} exactly by (3)–(5) for g up to 20–30 with python-flint rationals — the Euler product only needs primes of degree ≤ 2g), q = 9
(prime power — check the formulas allow it), q = 11, 13 at g ≤ 6. If monotonicity fails somewhere but A1 still holds (check roots
exactly by a Schur–Cohn / self-inversive criterion), say so: then H-half is the wrong sufficient condition and the right one is …
A2-2 (A1 itself for all (q, g)). If A2-1 resists, prove A1 directly: B is self-inversive of degree g; all roots on |w| = 1 iff (Cohn)
B' has all roots in |w| ≤ 1 iff … ; or via the Katz–Sarnak limit plus an exact error bound; or via a Rudnick-type exact formula for
the average of the whole polynomial (not only traces). Also the even case d = 2g + 2 (χ_D even; the completed L̄*): extend.
A2-3 (whole-curve cubic averages — the OPEN item of lane A). For q ≡ 1 mod 3, the cyclic trigonal covers y³ = f(t), f monic
squarefree (or cube-free with fixed ramification type) of degree d: the average of the FULL numerator of the curve's zeta
(product of L(u, χ) over both nontrivial cubic characters), not the isotypic average (which lane A refuted with 1 + u at degree 3).
Compute exactly at q = 7 for d = 3, 4, 5 (and q = 13 at d = 3, 4) by enumeration and decide whether all roots lie on |u| = q^{−1/2}.
Formulate the sharp conjecture (which ensembles of covers have RH-on-average: conjecture — exactly those whose monodromy is a
symplectic or unitary group whose Haar-averaged characteristic polynomial is Σ z^{2m}, i.e. where the exact correction terms are
"square-like"; make this precise and test).
A2-4 (the graph side, short). Lane A's `obs:common-vacuum-average-det` and graph-super §9: give the one-paragraph statement of what
the hyperelliptic theorem does and does not say for the ladder (`data-ladder.md` §2/§4).

## 2. Numerics (checks/)

`checks/hhalf_exact.py` (B_{q,g} by (3)–(5) in exact rationals for the (q, g) grid above; prints coefficients, monotonicity verdict,
and an exact self-inversive root-on-circle test); `checks/hhalf_rudnick.py` (Rudnick's trace averages recomputed by enumeration at
small (q, g) and the closed form); `checks/cubic_whole.py` (A2-3). Outputs to `checks/output_*.txt`.

## 3. Output

`astra-proofs.md`: §1 A2-1 (PROVED / REFUTED with the smallest counterexample / PARTIAL with the exact range certified and the
obstruction named); §2 A2-2; §3 A2-3; §4 A2-4; correction ledger; "Numerical checks for the blind lane"; "What this changes in the
notebook" (candidate rows `thm:hyperelliptic-average-all-genus` or `cex:…`; annotations to `ff-dirichlet.md`, `graph-super.md` §9,
`data-ladder.md`). `progress.txt`: A2-0, A2-1, A2-2, A2-3, A2-4, NUM.
