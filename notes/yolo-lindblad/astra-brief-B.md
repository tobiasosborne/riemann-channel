# Brief B (finite model, constructive): hunt the zeros in the phase-side Lindbladian.

You are the constructive-verification lane of a research notebook (repo root = your working
directory). Read `HANDOFF.md` (sections "CENTRAL PRIORITY", "Back to basics"),
`report/sections/03b_graded_permutation.tex`, `scripts/graded_permutation.py` (style of checks),
`scripts/bcmpo.py` (Bost-Connes phase operators as MPOs) and `notes/yolo-lindblad/astra-brief-A.md`
(the conventions and drafted statements S1-S8; use the SAME symbols). python3 with numpy, mpmath,
sympy, scipy is available; `data/zeros3000.npy` holds the first 3000 imaginary parts of the zeta
zeros; `mpmath.zetazero(n)` gives more. Write scripts to `notes/yolo-lindblad/finite/` (you own
that directory) and your report to `notes/yolo-lindblad/astra-finite-model.md`. Every numerical
claim in the report must be reproducible by a named script with a fixed seed; print check tallies.
Nothing may be put in by hand: never use the zeros as INPUT to a construction; they are only used
to COMPARE against outputs.

## The finite model to build

- Shell ladder G_B: basis |b>, b ranging over the divisors of B (B = 2^a 3^c 5^d 7^e ..., choose
  several B up to a few thousand states) or over b <= Bmax; matrix elements of V_p, V_p^+ from S2 of
  brief A (verify S2 first, directly, on L2(Z/N) with the Fourier basis for N a multiple of pb:
  define V_p there as f -> sqrt(p) f(x/p) 1_{p | x} between L2(Z/(N/p)) and L2(Z/N), or in the
  Fourier picture as the p-preimage map; make sure the isometry and the shell formulas hold to
  1e-12 before using them).
- Truncation: drop |pb> when pb is outside the basis (record the truncation error).
- Doubled space G_B (x) conj G_B, grading Pi = +1 on |1>, -1 on b > 1; Gamma_b = Pi (x) Pi.
- Generator T = sum_{p <= P} lambda_p (V_p (x) conj V_p - 1) with lambda_p = 1/p (also try
  p^{-beta} for beta slightly above 1 and the detailed-balance variant with reverse jumps).
- Archimedean length: each jump at p carries length log p. Build BOTH: (i) the continuous-time
  generator above (no lengths) and (ii) the length-resolved transfer: the Laplace transform in the
  archimedean length, K(s) = sum_p lambda_p p^{-s} V_p (x) conj V_p, and the resolvent
  (1 - K(s))^{-1}; also the multiset/Euler-product version prod_p (1 - lambda_p p^{-s} V_p (x)
  conj V_p)^{-1} if the V_p (x) conj V_p commute (check). Optionally add a truncated harmonic
  oscillator (levels k = 0..K) on the archimedean side with translation T_{log p} realised as
  exp(log p * (a - a^+)) or as the shift on a grid; report what you did.

## Questions to answer, in order

N1. Verify S1, S2 numerically (isometry, shell formulas, commutation V_p U_a, V_p V_q = V_q V_p).
N2. Verify S3: on the Gauss vectors g_chi (build all Dirichlet characters mod b for b | B with
    sympy or by hand), V_p^+ acts as a scalar p^{-1/2} conj(chi(p)); compute the generator's
    action on the coherences |e_0><g_chi| and compare the real parts with the partial Euler
    products of log zeta(beta) - log L(beta, chi) at beta = lambda exponent; compare with the
    Bost-Connes transfer eigenvalues L(beta, conj chi)/zeta(beta) (scripts/bcmpo.py computes them).
N3. Verify S4 and S5 exactly (sympy rationals): <c_b>_beta formula; c_b(1) = mu(b);
    sum_b c_b(n) b^{-s} = sigma_{1-s}(n)/zeta(s) at s = 2, 3 for n <= 30 on B-smooth b.
N4. THE HUNT. On the Galois-trivial doubled sector, compute the vacuum-coherence generating
    functions: F(s) = <1,1| (1 - K(s))^{-1} |1,1>, the Euler-product version, and the
    vacuum-to-shell overlaps <1,b| ... |1,1>. Locate their poles/zeros in s numerically (argument
    principle or root finding on Re s in [0.3, 1.2], Im s in [0, 40]) as P and B grow. Compare with
    zeta: are there poles converging to s = 1 (the pole), and do any singularities move toward
    1/2 + i gamma_n (gamma_1 = 14.1347, gamma_2 = 21.0220, gamma_3 = 25.0109)? Also compute the
    ratio F(s) / (1/zeta_P(s)) where zeta_P is the partial Euler product, to see whether 1/zeta
    appears as a factor. Report honestly, including a clean negative.
N5. Spectrum of the continuous-time generator T on the even-odd coherence block for lambda_p =
    1/p, primes up to P = 5, 7, 11, ..., 47 and shells up to B: real parts, imaginary parts, and
    whether any structure (uniform real part, line) emerges; then add Galois dephasing (the
    unitaries U_a, a in (Z/B)^x, at total rate gamma) and confirm the uniform shift -gamma of
    cross-character coherences, zero within a sector, and no shift on the Galois-trivial sector.
N6. Detailed balance: with reverse jumps V_p^+ at rate lambda_p p^{-beta}, verify the Gibbs
    weights on shells are stationary for beta > 1 and describe what happens as beta -> 1+.

## Deliverables

`notes/yolo-lindblad/astra-finite-model.md` with: the model as built (exact formulas), a table of
check tallies per script, the hunt results (tables of singularities vs P, B), figures optional
(save as PNG in the same directory), and a one-paragraph verdict per question N1-N6. Then a final
section "Verdict on the guess" in at most ten lines: what the finite model supports, what it
refutes, what it cannot decide.
