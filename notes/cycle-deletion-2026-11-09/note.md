# The cycle-deletion polynomial: a sharp window, a proof on cactus graphs

Author: `claude:fable-5.2`, 2026-11-09, one session. **A record, not a round. Nothing registered; no REFUTE review.** Statuses per item: PROVED-HERE (argument below, unreviewed), EXACT (rigorous computer check on a finite set), MC (Monte Carlo only), OPEN.

Starting point: `conj:conformal-sp4-average-real-rooted` of `notes/astra-2026-10-25/irreps/astra-proofs.md` §3.2: the polynomial
Φ(Y) = Σ_C μ_{4, Y∖V(C)} (sum over collections C of vertex-disjoint simple cycles; μ_d the Hall–Puder–Sawin d-matching polynomial) is real-rooted on every finite simple graph.

## 1. The object, with a weight

For d ≥ 1 and a weight w_c on every simple cycle c of Y put

    P_w(Y) = Σ_C Π_{c∈C} w_c · μ_{d, Y∖V(C)}.

Φ is d = 4, all w_c = 1. On a single cycle C_l, P_w = F_w(D_l(x)) with F_w(t) = U_d(t/2) + w, D_l = 2T_l(x/2).
**Cycle window** W_d: the w for which F_w has d real roots in [−2, 2]. W_1 = [−2, 2], W_2 = [−3, 1], W_3 = [−1.0887, 1.0887] (±(4/3)√(2/3)), W_4 = [−1, 5/4], W_5 = [−1.0363, 1.0363].

## 2. Findings

1. **Unicyclic graphs (PROVED-HERE, three lines).** If Y has one cycle c and F = Y∖V(c) (a forest), then with r = μ(Y)/μ(F):
   P_w(Y) = μ(F)^d · F_w(r) = Π_i (μ(Y) − ρ_i μ(F)), ρ_i the roots of F_w. Each factor is the characteristic polynomial of Y with a U(1) flux θ_i, 2cos θ_i = ρ_i. So P_w is real-rooted for w ∈ W_d, and for d = 4 it fails immediately outside [−1, 5/4]. **The lane's w = 1 sits inside a sharp window [−1, 5/4]; the endpoints are attained by every unicyclic graph.**

2. **Cactus graphs (PROVED-HERE, §3).** If every edge of Y lies in at most one cycle, P_w(Y) is real-rooted for all independent choices w_c ∈ W_d, every d ≥ 1. More: it is real stable in vertex potentials. This proves the conjecture on all cactus graphs.

3. **All graphs, d = 4 (EXACT, finite).** For all 971 connected cyclic graphs with ≤ 7 vertices the window of real-rootedness in a common w contains [−1, 5/4]; equality exactly for the 54 unicyclic ones; the smallest upper threshold among cycle rank ≥ 2 is 1.2532. With independent per-cycle weights in {−1, 5/4} (all corners when ≤ 6 cycles, else 40 random) and random interior points: 0 failures on 917 graphs ≤ 7 vertices; 0 failures on 40 000 random sparse graphs with 8–11 vertices, cycle rank 2–5. Theta graphs with one long path approach [−1, 5/4] from outside (θ(1,2,9): [−1.0026, 1.2517]).

4. **A dichotomy in d (EXACT, finite).** Complete graphs K_n, common w:
   - d = 1: upper threshold falls (K_4 0.618, K_6 0.126) though W_1 = [−2, 2]. d = 2: lower threshold falls (K_4 −1.55, K_6 −0.94, K_8 −0.83) though W_2 = [−3, 1].
   - d = 3, 4, 5: the window **grows** with n (d = 3: K_11 [−20.6, 35.8]; d = 4: K_11 [−358, 462]; d = 5: K_10 [−2302, 2272]).
   So for d ≤ 2 the cycle window is not the answer on dense graphs; for d ≥ 3 the worst graphs seen are the sparsest ones, where §3 is a proof. Heuristic: the cycle-window ends for d ≥ 3 are collisions of roots in the interior of the band, for d ≤ 2 they are band edges.

5. **Identities.** d = 2, w = 1: Σ_C μ_{2,Y∖V(C)} = μ(Y)² (EXACT on 143 graphs ≤ 6 vertices; it is the U(1)×U(1) ⊂ U(2) average). Windmills (k triangles at a hub): P_w = (x²−1)^{(k−1)d} · [F_{w_1} ⊞_d ⋯ ⊞_d F_{w_k}](x³ − (2k+1)x), ⊞_d the finite free additive convolution of Marcus–Spielman–Srivastava (EXACT for k, d small). U(2)⊗U(2) acting on C²⊗C² gives a polynomial close to Φ (that of U(1)·USp(4)) and far from μ_4, **equality consistent with Monte Carlo, not proved** (MC on K_4, three seeds 0, 7, 11, 2·10⁶ samples each; seeds 7 and 11 saved as `checks/output_mc_u2u2_seed*.txt`, seed 0 only in the session transcript. At x = 0: 21.81, 21.69, 21.74 against Φ(0) = 21.75, μ_4(0) = 18.75. At x = 0.5: −9.53, −9.57, −9.65 against Φ = −9.618, μ_4 = −12.87. At x = 1: 0.73, 0.78, 0.71 against Φ = 0.75, μ_4 = −6.25. The per-run error bars of 0.01–0.05, from 10 batches with heavy tails, understate the seed-to-seed scatter of about 0.06). Suggested kernel reason (the extra rank-one kernel is the normalised Λ²₊ − Λ²₋) is a sketch; an exact contraction as in the lane's `symplectic4.py` would settle it.

**Sharpened conjecture (OPEN).** For d ≥ 3, every finite simple graph and every choice w_c ∈ W_d: P_w(Y) is real-rooted. (False for d = 1, 2.)

## 3. Proof on cactus graphs

Notation: z_v = x + y_v (a potential y_v at each vertex). R(z; τ) = det(Z − A_θ), the characteristic polynomial of Y with a U(1) flux θ_c through each cycle, τ_c = 2cos θ_c. On a cactus R = Σ_S Π_{c∈S}(−τ_c) μ(Y∖V(S)) (S: vertex-disjoint cycles), affine in each τ_c.

*Polarisation.* For monic real-rooted F_c(t) = Π_i (t − τ_{c,i}) of degree d, Pol_F[R^d] means: in R^d replace τ_c^k by e_k(τ_{c,1..d})/C(d,k), for every c.

**Step 1 (identity).** Pol_F[R^d] with F_c = U_d(t/2) + w_c equals P_w(Y).
Reason: put a holonomy V_c D_c V_c^* (D_c diagonal, V_c Haar in U(d), independent) on one edge of each cycle, next to the cycle's attachment vertex p_c. Take a matrix-valued cycle c whose descendants in the block tree are scalar. Eliminating its private part B (the rest of c, plus what hangs off it; scalar ⊗ I_d) gives the self-energy (G_11 + G_mm) I + G_1m (U + U^*) at p_c, because G is symmetric. The V_c-average of a determinant det(M − g Π V T V^* Π) is Σ_k (−g)^k e_k(T) C(d,k)^{-1} Σ_{|S|=k} det M_{S^c}, linear in the e_k(T): it is the polarisation in τ_c. Induct from the leaves. With Haar classes E e_k gives U_d(t/2), so μ_d(Y) = Pol at the Chebyshev class; shifting e_d by (−1)^d w_c adds w_c · (coefficient of τ_c^d) = w_c · R(Y∖V(c))^d. Checked exactly: `checks/output_verify.txt` (a), four cacti, d = 1..4, random rational weights.

**Step 2 (stability).** Claim: S(z) = Pol_F[R(z;τ)^d] ≠ 0 whenever all Im z_v > 0 and all roots of all F_c lie in [−2, 2]. Induction on the number of cycles. No cycle: det(Z − A)^d. Otherwise take a leaf cycle c with attachment vertex p, private forest B, G = (Z_B − A_B)^{-1}. Then R = b · R'(z_p → z_p − σ(τ_c)), b = det(Z_B − A_B) ≠ 0, σ(τ) = G_11 + G_mm + τ G_1m, R' the polynomial of Y∖B. Polarising the other cycles: b^d S'(z_p − σ(τ_c)), S' nonvanishing on the upper half-plane by induction. Im G is negative definite and G symmetric, so for τ = 2cos θ ∈ [−2,2]: σ(τ) = v^*Gv with v = e_1 + e^{iθ}e_m, hence Im σ < 0. σ is affine in τ, so H = {τ : Im σ(τ) < 0} is an open half-plane (or all of C) containing [−2, 2], and on H the polynomial τ ↦ b^d S'(z_p − σ(τ)) of degree ≤ d has no zero. Grace–Walsh–Szegő (convex circular region): its polarisation has no zero for τ_{c,1..d} ∈ H ⊇ [−2,2]. ∎

Set all y_v = 0: P_w(Y)(x) ≠ 0 for Im x > 0, real coefficients, so real-rooted.

Where it stops: for overlapping cycles (theta graph, K_4) the holonomies are products, the cycle classes cannot be prescribed independently, and P_w is not a polarisation of R^d. What survives for every graph: with 𝔡_c = Π_{v∈c} ∂_{y_v}^d/d! and 𝓓_e = Σ_k (−1)^k (d−k)!/(d! k!) ∂_u^k ∂_v^k,

    P_w(Y) = Π_{cycles c} (1 + w_c 𝔡_c) · Π_{edges e} 𝓓_e · Π_v (x + y_v)^d,

and the edge recurrence P_w(Y) = 𝓓_e P_w(Y−e) + Σ_{paths π: u→v in Y−e} w_{π+e} 𝔡_π P_w(Y−e). Each 𝓓_e preserves real stability (symbol (uu' − 1)^d), which re-proves real-rootedness of μ_d; the factors (1 + w𝔡_c) do not, one at a time.

## 4. Checks (`checks/`, python-flint + networkx + sympy in a uv venv; every root count is rigorous via `fmpz_poly.complex_roots`)

`sp4.py`, `cdp.py` (general d) — the DP for μ_d and P_w; reproduce the lane's K_4 and C_3 polynomials. `atlas_windows_d4.py 7`, `cdp.py d 6`, `percycle.py 7`, `families.py 4 13`, `random_scan.py d N`, `complete.py d n`, `verify.py`, `mc_u2u2.py`. Outputs `output_*.txt` beside them. The venv was in the session scratchpad: rebuild with `uv venv; uv pip install python-flint networkx sympy numpy mpmath`.

## 5. Next

1. REFUTE review of §3 (the Schur step, G symmetric with scalar-flux descendants, the Grace–Walsh–Szegő hypothesis).
2. The theta graph: the first non-cactus case; P_w = Θ_d(s(x)) + Σw for equal paths, Θ_d the expected characteristic polynomial of |U_1+U_2+U_3|².
3. A proof for d ≥ 3 must use d: find the inequality that fails at d = 2 on K_6.
4. Prove the U(2)⊗U(2) = U(1)·USp(4) identity; all nauty graphs on 8 vertices.
