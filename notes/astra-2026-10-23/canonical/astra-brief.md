# Lane C: Weil positivity as a Schur–Cohn test — the Casoratian is the Szegő transfer matrix, on three rungs

You are `codex:gpt-6-astra`, a prover and constructive verifier in a mathematical research notebook (git repo, current
directory). Read `notes/astra-2026-10-23/brief.md` first (binding). Then read: `HANDOFF.md` session 2026-10-22 and
`docs/worklog/2026-10-22.md` (the new Section 6 of the tutorial: the labelling (f, g) ↦ σf + τg has rank 2n − 1, the phase space
is the label space, M is the second-order recurrence f_{k+2} = A f_{k+1} − q f_k, Ω is its Casoratian, M^T Ω M = qΩ is Abel's
formula, S = M/√q is the damping-removed Chebyshev recurrence); `notes/adelic-gkp/graph-ihara.md` §4–§6 and §8 item 2 (the
Weil form as the Casoratian; the explicit formula with the sign flipped); `notes/adelic-gkp/window-similitude.md` (lane R:
on the zeta window the prime steps are exact similitudes of Weil's form — the Toeplitz shift); `notes/adelic-gkp/ff-dirichlet.md`
(lane J: Dirichlet characters of F_q(t) have every ladder item); the Carathéodory–Toeplitz adjudication in
`notes/reviews/adelic-gkp-rsu-fable-2026-10-06.md` (search "Toeplitz", "full rank"); `notes/weil-bond-analytic/analytic.md` §10
and §13 (the two-period Wronskian metric, canonical systems, the Casoratian for genus one). The zeta-window Weil form is
implemented in `zst/` (formula sheet `notes/zeta-spectral-triples/plan.md` §1; `zst/include/zst.h`); you may call its tools or
re-implement the window form in python from primes (state which). Standard references to cite from memory: B. Simon, "Orthogonal
Polynomials on the Unit Circle" (Verblunsky coefficients, Szegő recursion, paraorthogonal polynomials, Geronimus theorem);
Schur–Cohn / Jury stability test; de Branges, "Hilbert spaces of entire functions". Write only
`notes/astra-2026-10-23/canonical/{astra-proofs.md,progress.txt,checks/}`.

## 0. The claim to make precise

Tutorial 6c: for a mode λ, the recurrence y_{k+2} = λ y_{k+1} − q y_k has Casoratian C(y, z) = y_k z_{k+1} − y_{k+1} z_k with
C_{k+1} = q C_k (Abel); the substitution y_k = q^{k/2} x_k removes the damping and gives the Chebyshev recurrence
x_{k+2} = (λ/√q) x_{k+1} − x_k whose transfer matrix S_λ = ((λ/√q, −1), (1, 0)) is symplectic; RH for the mode is |λ/√q| ≤ 2, i.e.
S_λ elliptic (rotation), and the Weil form ½Ω(M − V) is positive on the mode iff S_λ is a rotation. The conjecture of this lane
is that this is one instance of a general structure: the Weil form on every rung is the Toeplitz form of a moment sequence, the
step is the shift, Weil positivity is the Schur–Cohn stability test of the damping-removed recurrence, and the Schur
(Verblunsky) parameters are a new set of coordinates on the "counts" in which RH is |α_k| < 1.

## 1. Graph rung (theorems; prove them)

C1. Let Y be (q+1)-regular with Ihara polynomial P(u) = det(1 − Au + qu²) = Π_λ (1 − λu + qu²) and set z = √q u, so
p(z) = Π_λ (1 − (λ/√q) z + z²), a self-reciprocal polynomial of degree 2n. Define the moments c_k = q^{−k/2} Tr(M^k) for k ≥ 0 (M
the step; Tr M^k = Σ_λ (μ_λ^k + μ̄_λ^k) with μ_λ the roots of μ² − λμ + q), c_{−k} = c_k, and the Toeplitz matrices
T_N = (c_{j−k})_{0 ≤ j,k ≤ N}. Prove: (i) c_k = Tr(S^k) with S = M/√q, hence c_k is the trace of the k-th power of the
damping-removed step, and c_k = Tr(B^k) q^{−k/2} + (correction from the (1 − u²)^{m−n} factor: make it exact); (ii) Y is
Ramanujan (all nontrivial λ in [−2√q, 2√q]) iff the sequence (c_k) restricted to the nontrivial modes is positive definite in the
Toeplitz sense (T_N ⪰ 0 for all N), and this is the record's Weil positivity ½Ω(M − V) ≥ 0 on the trace Weil form of 08b (quote
the registered statement and show the identification; the handoff says "08b's trace Weil form on a window of length 2g is twice
the lattice Weil form"); (iii) the Schur algorithm applied to the measure dν = Σ_λ (δ_{θ_λ} + δ_{−θ_λ}) on the circle (θ_λ the
argument of μ_λ/√q) gives Verblunsky coefficients α_0, …, α_{2n−2} with |α_k| < 1 and the polynomial p is (up to normalisation)
the paraorthogonal polynomial Φ_{2n}^{(β)} for the right β; compute the α_k for K_4, the Petersen graph, K_5, the cube and the
prism, print them, and state the exact relation between (α_k) and (c_k) (the Schur algorithm = the Levinson recursion on T_N) and
between the Szegő transfer matrix ((z, −ᾱ_k), (−α_k z, 1)) and the Casoratian structure of Section 6 (the Casoratian of the
Szegő recursion is 1 − |α_k|²; the record's Ω is the k = 0 instance). What happens to the α_k at a non-Ramanujan graph (some
|α_k| ≥ 1, which k first): make it a theorem (the index of the first bad α is a function of the number of out-of-band modes?) or a
numerical observation on a family (the prisms, the Möbius–Kantor graph, K_n for n = 4..9 with q = n − 2).

## 2. Function-field rung (theorems)

C2. For a primitive Dirichlet character χ mod f over F_q(t) (lane J's data: `check_ff_dirichlet.py` has the L-polynomials; recompute
them from scratch, char sums Σ_{deg D = k} χ(D)), with z = √q u and p_χ(z) the normalised L-polynomial (self-reciprocal after the
root-number normalisation; say exactly how), the moments c_k are the normalised character sums q^{−k/2} Σ_{deg D = k, D monic}
Λ_χ-type data — identify the right moment sequence (the traces of Frobenius powers, i.e. the logarithmic derivative, not the
coefficients) and prove: Weil's RH for χ ⟺ Toeplitz positivity of (c_k) ⟺ the Schur parameters satisfy |α_k| < 1 for k < d − 1
and |α_{d−1}| = 1 (paraorthogonal). Compute the α_k for every primitive χ mod f for q = 3, 5 and deg f ≤ 4, print them, and look
for structure: C2' (conjecture, test it): the α_k of L(u, χ) are, up to the root-number phase, determined by the character sums
over squarefree (or over prime) D of degree ≤ k+1 only — i.e. there is a "non-backtracking" expression for α_k analogous to the
graph's matching/prime-cycle expansion. If false, say what the α_k are not.

## 3. Zeta rung (numerical, primes only; RH never assumed)

C3. Lane R: on a window the prime step by log p is an exact similitude of the Weil form, so the restriction of the window Weil
form W to the span of the shifts g_j = g(· − j log p), j = 0..N, of a fixed smooth window function g is a Toeplitz matrix
T_p^{(N)}(g) = (W(g_j, g_k))_{j,k} with symbol computable from primes, the pole and the archimedean factor (rule 3). Define its
Schur parameters α_k(p; g). Conjecture C3: (i) T_p^{(N)}(g) ⪰ 0 for all N and all g supported in a window of length L is implied
by RH and is a finite, prime-only computation for each (p, N, g); (ii) the Schur parameters α_k(p; g) converge as the window
grows, |α_k(p; g)| < 1 uniformly, and the limit sequence depends on p through the local factor at p only — test the dependence
on p for p = 2, 3, 5, 7 and on g; (iii) the Szegő product Π_k (1 − |α_k|²) converges and its limit is a prime-only invariant
(conjecture its value; the first guess is a quantity like (1 − 1/p) or ζ-type Euler factor at p — compute it and say what it is,
or that the data do not decide). Use lane R's setup for the window and the form (its `check_window_similitude.py`); if the Toeplitz
structure is only approximate at finite window length, quantify the defect (‖T − Toeplitz part‖) and work with the exact
Toeplitz symbol it converges to.

## 4. Output

`astra-proofs.md`: §1 C1 (i)–(iii) PROVED with the tables of α_k; §2 C2 PROVED, C2' decided; §3 C3 NUMERICAL with the tables of
α_k(p; g) for p = 2, 3, 5, 7, the convergence in N and L, and a stated conjecture for the limit; correction ledger; "Numerical
checks for the blind lane" (the α_k of K_4; one α_k of a Dirichlet character; one α_k(2; g) at a stated window); "What this changes
in the notebook" (candidate rows; the one-line annotation `graph-ihara.md` §8 item 2 and §9 need: "Ω is the Casoratian,
Q = ½Ω(M − qM^{-1})"; whether the Schur coordinates are the right coordinates for the data ladder's "finite rank per mode" item).
`progress.txt`: C1i, C1ii, C1iii, C2, C2p, C3i, C3ii, C3iii, NUM.
