# Brief A (structure): the phase-side Riemann Lindbladian. Prove or correct.

You are the prover lane of a research notebook (repo root = your working directory). Read
`HANDOFF.md` (sections "CENTRAL PRIORITY", "Back to basics", "Programme status after the night
campaign") and `report/sections/03b_graded_permutation.tex`, `04b_phantasm_forced.tex`,
`04c_phantasm_channels.tex` for context. Do not read anything else unless you need a definition.
Write your full report to `notes/yolo-lindblad/astra-structure.md` (create it; you own it).
Nothing may be put in by hand: no statement may assume the zeros of zeta, RH, or the Hilbert-Polya
operator. Every claim gets one of the labels: PROVED (complete proof), PROVED-CONDITIONAL (list
the hypotheses H-*), CORRECTED (the drafted statement was false; give the counterexample and the
true statement), OPEN (what is missing). End with a CORRECTION LEDGER listing every drafted
statement and its verdict. Work at the highest rigour; elementary and explicit beats slick.

## Conventions (fixed; use these symbols)

- Zhat = prod_l Z_l (profinite integers) with Haar probability measure; L2(Zhat). Fourier basis
  e_r(x) = exp(2 pi i r x), r in Q/Z (well defined via Zhat -> Z/b). {e_r} is an orthonormal basis.
- Prime jump: (V_p f)(x) = sqrt(p) f(x/p) 1_{p Zhat}(x). Galois: (U_a f)(x) = f(a^{-1} x), a in Zhat^x.
- Ramanujan sums: c_b = sum_{a in (Z/b)^x} e_{a/b} (b >= 1, c_1 = e_0), |b> = c_b / sqrt(phi(b)).
- Grading: even = span{e_0} (the constant function = the Bost-Connes critical KMS state on the
  phases, i.e. the Haar state), odd = its orthogonal complement. Doubled bond L2 (x) conj L2 with
  Gamma_b = Pi (x) conj Pi; "even-odd coherences" = the Gamma_b-odd subspace.
- A graded Lindbladian on the bond: L(rho) = -i[H, rho] + sum_alpha (R_alpha rho R_alpha^+ -
  1/2 {R_alpha^+ R_alpha, rho}); its doubled-bond matrix is T = Q (x) 1 + 1 (x) conj Q + sum R (x)
  conj R with Q = -iH - 1/2 sum R^+ R. Ring norm with the parity (Ramond) closure = Tr[Gamma_b e^{tT}].
- The guess under investigation (the "phase-side Lindbladian"): jumps R_p = sqrt(lambda_p) V_p
  (x) T_{log p} on L2(Zhat) (x) L2(R_+^*), lambda_p = 1/p, T_u = translation by u on the archimedean
  line R_+^* in the variable log x; plus the Gamma-factor (harmonic-oscillator) ladder on L2(R_+^*);
  plus a Hamiltonian D = x d/dx + 1/2 on L2(R_+^*). The physical cMPS runs along the archimedean
  coordinate; the letters are the primes.

## Drafted statements (deliberately slightly too strong; prove or correct each)

S1 (prime jump = Galois away from p). V_p is an isometry with V_p^+ e_r = p^{-1/2} e_{pr} and
   V_p e_r = p^{-1/2} sum_{s: ps = r} e_s (p preimages). V_p U_a = U_a V_p for all a. On Zhat =
   prod Z_l, multiplication by p is a unit at every l != p and the shift at p. On the finite
   quotient Z/b with p coprime to b, V_p^+ acts on the Fourier modes as the Shor map r -> pr.
S2 (Ramanujan shells). The Galois-trivial sector G = closed span{|b> : b >= 1} is invariant under
   all V_p, V_p^+, and: p not dividing b: V_p |b> = p^{-1/2} (sqrt(p-1) |pb> + |b>), V_p^+ |b> =
   p^{-1/2} |b>; p dividing b: V_p |b> = |pb>, V_p^+ |b> = p^{-1/2} sqrt(phi(b)/phi(b/p)) |b/p>.
   The vacuum |1> is NOT invariant: V_p |1> = p^{-1/2}(sqrt(p-1)|p> + |1>).
S3 (character dephasing). For a nontrivial Dirichlet character chi mod b and its Gauss vector
   g_chi = sum_{a in (Z/b)^x} chi(a) e_{a/b}, and p coprime to b: V_p^+ g_chi = p^{-1/2}
   conj(chi(p)) g_chi (up to the stated normalisation; fix it). Hence, under the jumps R_p =
   sqrt(lambda_p) V_p restricted to the coherence |e_0><g_chi| (or |g_chi'><g_chi|), the generator
   acts as a scalar, and for chi != chi' the real part of that scalar is
   -sum_p lambda_p (1 - Re(chi conj chi')(p)) + (correction from primes dividing b). With
   lambda_p = p^{-beta} this is -(log zeta(beta) - log L(beta, chi conj chi')) up to prime-power
   terms; make the statement exact, including the p | b primes and the prime-power terms, and
   relate it to the Bost-Connes transfer eigenvalue L(beta, conj chi)/zeta(beta) of the phase
   operators (HANDOFF item 2 under "What was established").
S4 (critical vanishing). The Gibbs expectation of c_b at inverse temperature beta > 1 is
   <c_b>_beta = zeta(beta)^{-1} sum_n n^{-beta} c_b(n) = sum_{d | b} mu(b/d) d^{1-beta} =
   b^{1-beta} prod_{p | b} (1 - p^{beta-1}), which -> 0 as beta -> 1+ iff b > 1. State precisely
   in what sense the critical state is the pure vector state of e_0 on the phase algebra C(Zhat).
S5 (where zeta enters without being inserted). c_b(1) = mu(b) and sum_b c_b(n) b^{-s} =
   sigma_{1-s}(n)/zeta(s) (Re s > 1). Reformulate: the Dirichlet series of the vacuum-to-shell
   overlaps of the prime-jump dynamics on G has 1/zeta(s) as a factor. Find the EXACT operator
   statement: which generating function (resolvent, Laplace transform in the archimedean length,
   or ring norm) of the phase-side Lindbladian restricted to G has zeta(s) in a denominator, with
   all normalisations, and whether its poles are exactly the nontrivial zeros. If the free
   (ordered-word) structure gives 1/(1 - sum_p lambda_p p^{-s} ...) instead of 1/zeta, say so and
   identify what restores the multiset (Euler product) structure (commutation of the V_p? the
   stay term in S2? the parity closure?). This is the central question of the brief.
S6 (the closed ring and the quotient by Q^x). On L2(A_Q) multiplication by p in Q^x is unitary
   with |p|_A = 1 (product formula); on the adele class space A_Q/Q^x it is the identity. State
   exactly what "closing the ring with the parity insertion" does to the Q^x action, and whether
   the ring norm of the guess at archimedean length t is a trace over the periodic orbits of the
   idele-class-group action (Connes' trace formula, 1999). Cite only what you can state precisely;
   label anything from memory as UNVERIFIED-MEMORY.
S7 (RH as uniform dephasing, forward direction only). If the generator restricted to the
   even-odd coherences has the form T_0 - 2 gamma with T_0 anti-Hermitian, its spectrum lies on
   Re = -2 gamma; a parity jump sqrt(gamma) Pi realises the -2 gamma exactly, and a finite abelian
   group of character-diagonal unitary jumps realises character dephasing. State the precise
   converse that would be needed (metric, diagonalisability, Riesz basis) and why the recorded
   obstruction "Gram condition number 10 -> 700 across 3000 zeros" bears on it.
S8 (fixed point and absorbing-ness). With jumps V_p only (rates lambda_p = 1/p), the shell
   populations perform a Markov chain b -> pb with no stationary distribution (no normal KMS state
   at beta = 1); with reverse jumps V_p^+ at rates lambda_p p^{-1}... (detailed balance) the Gibbs
   weights n^{-beta} on the shells are stationary for beta > 1. Determine what stationary object
   exists at beta = 1 (a weight, a boundary condition at b -> infinity) and whether the vacuum
   coherences |1><b| decay or are absorbing. Compare with the vacuum-decay Lindbladian of shard 04c.

## Deliverables

1. `notes/yolo-lindblad/astra-structure.md`: statements, proofs, ledger, and a final section
   "What the guess gets right, what it gets wrong, what to compute next" (at most one page).
2. If you write any scratch code, put it under `notes/yolo-lindblad/finite/structure_*.py`.
