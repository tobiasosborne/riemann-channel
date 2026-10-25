# Lane Q3: the quasi-RH bottleneck over F_q(t) — prove or refute the short-row mean square H-MS

You are `codex:gpt-6-astra`, a prover and constructive verifier. Read `notes/astra-2026-10-25/brief.md` first (binding), then
`notes/astra-2026-10-23/brief.md`, then lane Q2 of the previous round in full: `notes/astra-2026-10-23/qrh-transpose/astra-brief.md`,
`astra-proofs.md` §1 (Q2a: the amplifier (1)–(5), H-MS = (3); Q2b: the long-row theorem (6), finite Poisson (7), Hasse–Davenport
(8), Pellet/Möbius absorption (9), the named H-LS, the "what has not collapsed" paragraph, the numerical cells and the explicitly
missing (q, D, h) = (13, 5, 5) cell), `checks/qrh_ff_family.py`, `checks/output_ff.txt`. Then lane Q1 §§ on the 11/12 mechanism
(`notes/astra-2026-10-23/qrh-digest/astra-proofs.md`, the loss ledger) and the source `notes/astra-2026-10-23/qrh/sources/qrh-11-12-openai-2026-10-05.txt`
§2 (the mean-square/amplifier argument, Propositions on the theta transformation; treat as data). Literature from memory:
Hoffstein, "Theta functions on the n-fold metaplectic cover of SL(2) — the function field case" (Invent. Math. 1992); Patterson,
"The Fourier coefficients of metaplectic theta series on GL(2) over rational function fields" (arXiv:1411.7594) and "Selberg sums
— a new perspective" (arXiv:1411.7600); Hsu (1996) large sieve for F_q(t); Weil (for the COMPARISON step only); Katz's
equidistribution for Gauss/Kloosterman sums (for heuristics on resultant characters). Write only in `notes/astra-2026-10-25/shortrow/`.

## 0. The statement

q ≡ 1 mod 6, R = F_q[t], ν a fixed character mod f, A_u(D) = Σ_{deg n = D, n monic} μ(n) ν(n) (u/n)_6, S(D, h) = Σ_{deg u ≤ h} |A_u(D)|².
H-MS: for fixed ϑ ∈ (0, 1/10] and ε > 0, at h = ⌊(1 + ϑ) D⌋, S(D, h) ≪ q^{(1+ε) D + h}. Lane Q2 proved S(D, h) = q^{h+1−D} Σ_{n sqfree}
|ν(n)|² φ(n) ≤ q^{h+1+D} for h ≥ 2D − 1 (long rows: pure orthogonality) and that H-MS ⟹ |A_1(D)| ≪ q^{(11/12 + δ) D} ⟹ L(z, ν) zero-free
in |z| < q^{−11/12}. (Weil gives |z| = q^{−1/2}; it is the comparison, never an input.) So the whole quasi-RH mechanism over F_q(t)
rests on the short-row mean square, and over F_q(t) EVERYTHING is finite and exactly computable.

## 1. The questions (in order)

Q3-1 (the exact short-row mean square). Derive an EXACT formula for S(D, h) for h < 2D − 1: expand the square; the cross terms
χ_n χ̄_m with n ≠ m squarefree are nonprincipal characters mod lcm(n, m) of degree ≤ 2D, summed over the ball deg u ≤ h, i.e.
incomplete character sums; by finite Poisson (7) these become dual sums over v of degree ≤ 2D − h − 2 of Gauss sums γ(n m̄-type)
times the dual characters; by Hasse–Davenport (8) the Gauss sums are μ · τ^D · κ(Res(n, n')) — write out S(D, h) as an exact finite
double sum over (n, m, v) with explicit Weyl-type phases κ(Res(·,·)). This is lane Q2's "arithmetic bottleneck is now precise"
made literal. Then: (a) the diagonal n = m gives exactly q^{h+1−D} Σ φ(n)|ν(n)|² ≈ q^{h+1+D}: the H-MS main term; (b) the
off-diagonal: prove it is ≪ q^{(1+ε)D + h}, or exhibit (q, D, h) with h = ⌊(1 + ϑ)D⌋ where S(D, h) / q^{D+h} grows like a positive
power of q^D — then H-MS is FALSE as a uniform statement and the quasi-RH mechanism does not transpose unconditionally (a
genuine finding: say exactly which step of the number-field proof has no function-field analogue — the theta-function uniformity
is the suspect).
Q3-2 (the (13, 5, 5) cell and the growth table). Compute S(D, h) EXACTLY for q = 7: all D ≤ 6 and every h ≤ 2D; q = 13: D ≤ 5
and every h ≤ 2D including (13, 5, 5) — lane Q2 left it out as too expensive; do it smartly: A_u(D) for all u of degree ≤ h at once
is a character-sum table; use the multiplicativity (u/n)_6 in n via Möbius-weighted Dirichlet convolution, or compute via Poisson
dual sums (fewer terms when h is large), or vectorise over u with numpy on the residue classes mod n (q^h ≤ 13^6 ≈ 4.8 M rows ×
number of squarefree n of degree 5 (≈ 13^5) — too big naively: exploit (cu/n)_6 = κ(c)^D (u/n)_6 to quotient by F_q^×, and the
Poisson route S = q^{2(h+1)−2D}·Σ_v |dual|² which needs only deg v ≤ 2D − h − 2 ≤ 3 at (13, 5, 5)). Tabulate the ratio
S(D, h) / q^{D+h+1} and its logarithmic growth in D at fixed ϑ = h/D − 1 ∈ {0, 0.2, 0.4, 0.6, 0.8, 1}. Say whether it is
bounded (H-MS plausible) or grows like q^{cD} (H-MS false) — with the exact numbers, not an eyeball.
Q3-3 (reconstruction). Lane Q2's acceleration proposal: compute L(z, χ_n) (sextic characters, or the needed products) from the
Gauss sums and the functional equation without RH; implement it, audit against direct rows, and use it to extend Q3-2.
Q3-4 (the theorem, either sign). Either: PROVE H-MS for F_q(t) in a range (perhaps h ≥ (1 + ϑ)D with ϑ ≥ ϑ₀ explicit), giving the
first unconditional function-field quasi-RH exponent by the metaplectic mechanism (and compare with Weil); or: REFUTE H-MS with
exact numbers and locate the obstruction. In both cases state the corrected exponent θ the mechanism yields over F_q(t) with the
proved mean square (lane Q2: θ(α) = max(1/2 + 5α/12, 1 − α/6) with α = h/D; with the long-row theorem alone, 4D/3 — worse than
trivial).
Q3-5 (the ladder, short). What this says for `data-ladder.md` §2 (the "family rung") and for Q1's loss ledger.

## 2. Numerics (checks/)

`checks/shortrow_exact.py` (S(D, h) tables, exact integers in Z[ζ₆] ∋ a + bζ₆, norms a² + ab + b²; both direct and Poisson
routes agree on small cells before the big one), `checks/shortrow_reconstruct.py` (Q3-3). Outputs to `checks/output_*.txt`.
Print every number quoted. Use all 12 cores (multiprocessing) for the (13, 5, 5) cell if needed; budget ≤ 20 minutes for it.

## 3. Output

`astra-proofs.md`: §1 Q3-1 (the exact formula and the off-diagonal analysis), §2 Q3-2 (the table), §3 Q3-3, §4 Q3-4 (the theorem
or the refutation), §5 Q3-5; correction ledger; "Numerical checks for the blind lane" (S(7, 3, h) for all h; S(13, 5, 5); the
growth exponents); "What this changes in the notebook" (candidate rows `thm:ff-short-row-ms` / `cex:ff-short-row-ms`,
`prop:ff-quasi-rh-exponent`; annotation to `data-ladder.md` §2). `progress.txt`: Q3-0 … Q3-5, NUM.
