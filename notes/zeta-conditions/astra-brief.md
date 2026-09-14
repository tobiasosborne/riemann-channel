# Brief: impose the zeta conditions factor by factor on MPS / cMPS ring norms. Concrete examples only.

You are the constructive lane of a research notebook (repo root = working directory). Read
`HANDOFF.md` ("CENTRAL PRIORITY", "Back to basics", "The yolo Lindbladian" sections), then
`report/sections/03b_graded_permutation.tex` (physical letters, the sign lives in even-odd
coherences), `02g_definitions_ring_norm_tensor.tex` and `06g_ring_norm_examples.tex` (graded lattice
tensors, one MPS per genus, conventions), `08b_weil_positivity.tex` (inverse pairing gives the
functional equation, adjoint pairing gives reality), `02f_definitions_graded_cmps.tex` and
`04f_cmps_twisted_supertrace.tex` (cMPS: twisted ring norm = supertrace, ring zeta 1/sdet), and
`scripts/ring_norm_examples.py` for code conventions. python3 with numpy, sympy, mpmath, scipy.
Write scripts to `notes/zeta-conditions/finite/` (you own it) and the report to
`notes/zeta-conditions/astra-constructions.md`. Every numerical claim must be reproducible by a
named script with printed check tallies; every explicit matrix must be printed in the report.

TJO's request, verbatim: "line up all the conditions we want a zeta to obey: functional equation,
rh/ramanujan, unique fixed point etc etc and try to impose them factor by factor on the cMPS ring
norm. I suppose it makes sense to include tiny L functions etc. ... I want to see completely
concrete MPS/cMPS that any practitioner would understand that yield interesting zeta data."

## Conventions

- Graded lattice tensor: letters A_s on the bond C^{D_+ | D_-}, bond parity Pi = diag(+1, -1),
  doubled transfer E_d = sum_s A_s (x) conj(A_s), Gamma_b = Pi (x) conj Pi. Ramond (parity-closed)
  ring of length n: Psi_Pi = sum_w Tr(Pi A_{w_n} ... A_{w_1}) |w>, N_n := ||Psi_Pi||^2 = Tr[Gamma_b E_d^n].
  Untwisted ring: B = 1. Zeta: Z(u) = exp(sum_n N_n u^n / n) = 1/sdet(1 - u E_d) restricted to the
  support. Amplitude version (one letter, physical dimension 1): N_n := str(A^n).
- Prime counts: a_d = (1/d) sum_{e | d} mu(d/e) N_e; Euler product Z(u) = prod_d (1 - u^d)^{-a_d}.
- cMPS: (Q, R_a) on a graded bond, T = Q (x) 1 + 1 (x) conj Q + sum_a R_a (x) conj R_a,
  N(L) = Tr[Gamma_b e^{L T}], ring zeta 1/sdet(z - T). Lindblad reading: Q = -iH - 1/2 sum R^+ R
  makes the even transfer trace preserving; the "unique fixed point" is the unique stationary
  state of that channel.
- "Curve normal form": Z(u) = P(u) / ((1 - u)(1 - q u)), P(u) = prod_{j=1}^{2g} (1 - alpha_j u).

## The condition ledger (state each as an exact algebraic condition on (A_s, Pi) and on (Q, R))

C1 Positivity and integrality: N_n in N (lattice) / N(L) >= 0 (cMPS). Ramond norms are >= 0
   automatically; integrality is not.
C2 Genuine gas: a_d >= 0 for all d (Euler product with bosonic primes). Not automatic.
C3 Rationality: automatic for finite bond; state the degree bookkeeping (poles = even spectrum,
   zeros = odd spectrum, net multiplicities).
C4 Functional equation: Z(1/(q u)) = +- q^{chi/2} u^{chi} Z(u)-type symmetry; on the spectrum,
   closure under lambda -> q / lambda parity-preserving with multiplicities. Realisations: inverse
   pairing of letters (08b), a bond duality J with J E_d J^{-1} ~ q E_d^{-1} on the support, or the
   Hodge/Poincare pairing of 06d. Give at least one explicit tensor where the FE holds by a visible
   mechanism, and one where it fails.
C5 RH / Ramanujan: every odd eigenvalue has modulus sqrt q (curves) or every nontrivial even
   eigenvalue has modulus sqrt q (graphs, poles). Mechanisms: E_- = sqrt q times a unitary in some
   metric (Artin-Schreier); "the odd sector is a sub-system with half the entropy"; Weil positivity
   (08b). Give explicit tensors where RH holds by a visible mechanism and one where it fails by a
   visible mechanism.
C6 Unique fixed point / ergodicity: the even sector has a simple Perron root q (one pole at 1/q,
   unique stationary state of the normalised even channel), the other even eigenvalue being the
   trivial 1 (H^0) or absent. State it for the transfer channel and for the Lindbladian.
C7 Galois grading and L-functions: a finite group G acting on letters/bond commuting with the
   tensor; character decomposition N_n = sum_chi dim(chi) N_n^chi with L(u, chi); Z = prod_chi
   L(u,chi)^{dim chi}; the notebook's pattern "even = trivial character, odd = nontrivial characters"
   (Artin-Schreier, 06b). Tiny L-functions to construct EXPLICITLY as MPS (bond and letters written
   out, character as boundary vector or as a twist): (a) the Z/2 swap on the pair shift below
   (is it an Artin L-function? correct the draft D5); (b) Dirichlet L-functions over F_2[x] modulo
   M = x^3 + x + 1 (group F_8^x = Z/7; L(u, chi) = (1 - u)(1 - alpha u) with |alpha| = sqrt 2?) and
   over F_3[x] modulo x^2 + 1 (F_9^x = Z/8; degree-1 L-functions 1 - alpha u with |alpha| = sqrt 3
   for odd characters?), built from the Horner transfer f -> x f + c mod M on the bond F_q[x]/M with
   letters c in F_q; explain the open-chain (sum over monic f, side A) versus ring (Frobenius
   orbits, side B) presentations and relate them; (c) Gauss and Kloosterman sums as L-functions of
   degree 1 and 2 over the affine line (L = 1 - G u, |G| = sqrt q; L = 1 - a u + q u^2 with
   |a| <= 2 sqrt q): is there an MPS whose Ramond norm is q^n - Kl_n-type counts, and what is its
   bond? (d) the Artin L-function of a small graph cover (Ihara), one example.
C8 Sign structure: zeros odd, poles even, supertrace (established in 04b/04f); check on each example.
C9 Physical realisability: the tensor is an honest MPS (Ramond norm = count, orthonormal words),
   letters coarser than the grading (03b), and for cMPS a regular (Q, R) with the Lindblad
   normalisation for the even sector.
C10 Continuum / length quantisation: the cMPS version: which of the lattice examples have a cMPS
   analogue (Q, R on C^{1|1}, C^{1|2}, ...), what the ring zeta 1/sdet(z - T) is, and what
   "incommensurable lengths" would mean there.

## Drafted constructions and statements (deliberately slightly too strong: prove or correct)

D1 (the sub-system rule). If the odd sector is a sub-MPS of the even one (a subset of letters with
   equal amplitudes, so Psi_- is a sub-sum of Psi_+), then Psi_Pi = Psi_+ - Psi_- is a sum of
   orthonormal words, N_n = N_n^+ - N_n^-, and a_d = a_d^+ - a_d^- >= 0: the zeros of Z are the
   poles of the sub-system's zeta, and the gas is genuine (C1, C2 hold).
D2 (E0: one zero, one pole). Pair shift on m^2 letters (a, b) with the diagonal (a, a) odd:
   A_{(a,b)} = diag(1, [a = b]) on C^{1|1}; N_n = m^{2n} - m^n; Z = (1 - m u)/(1 - m^2 u); RH holds
   because the odd sector has half the entropy; for m = 2 it is Z(A^1/F_4)/Z(A^1/F_2) and the odd
   sector is the fixed locus of the Galois involution (swap). No functional equation.
D3 (the ladder). (1 - m u)/(1 - m^2 u) [1 zero, 1 pole] -> (1 - a u + q u^2)/(1 - q u) [affine
   elliptic curve, 2 zeros 1 pole] -> (1 - a u + q u^2)/((1 - u)(1 - q u)) [projective elliptic
   curve, 2 and 2; FE holds] -> y^2 + y = x^3 over F_4 with P = (1 + 2u)^2 [FE, real double zero].
   Write the explicit graded tensors for each rung (the elliptic ones with the diag(1, pi)-type
   letters of 06g), state which of C1-C10 hold, and give the mechanism behind each.
D4 (FE by inverse pairing). Letters closed under B -> B^{-1} (08b) give the FE for the ring zeta;
   construct the smallest graded example where inverse pairing produces alpha -> q/alpha on the
   odd sector together with the {1, q} even pair.
D5 (Z/2 L-function of the pair shift). With the swap sigma, N_n^sigma = Tr[(sigma (x) conj sigma)...]
   = number of swap-fixed words = m^n; Artin L-functions L(u, 1) and L(u, sgn) from
   (N_n +- N_n^sigma)/2; draft: L(u, sgn) = ((1 - m u)/(1 - m^2 u))^{1/2}. This is probably wrong
   because the pair shift is not a Z/2 cover; find the correct tiny Z/2 example (a genuine double
   cover of a shift or graph) and its L-function.
D6 (unique fixed point selects the poles). For an honest MPS with even sector normalised to a
   channel, C6 holds iff the even spectrum is {q} plus eigenvalues of modulus < q, and the pole
   at u = 1 (H^0) is the boundary/vacuum contribution of a second, decoupled even block. Decide
   whether "unique fixed point" can be imposed independently of the FE and RH, and exhibit tensors
   with each combination of (C4, C5, C6) holding or failing.
D7 (cMPS analogue of E0). On C^{1|1}: Q = diag(0, 0)?, R_a = ... : find (Q, R) whose Ramond ring
   norm is e^{lambda_+ L} - e^{lambda_- L} with lambda_- = lambda_+ / 2 (the continuum "half
   entropy"), and the C^{1|1} cMPS whose ring zeta is (z - lambda_-)/(z - lambda_+). Then the cMPS
   with the FE (poles at 0 and lambda, zeros at lambda/2 +- i omega).
D8 (what a "tiny Riemann" would need). Using the ledger, state the minimal list of conditions that
   forces an Euler product over infinitely many primes with a single simple pole, zeros in the
   strip, FE and RH, and say which of them a finite bond can never satisfy (cite the no-go of
   06e/04b: no finite or trace-class operator has a genus >= 1 count sequence as a plain trace;
   a finite bond gives rational Z). Be precise about what "factor by factor" can and cannot reach.

## Deliverables

`notes/zeta-conditions/astra-constructions.md`:
1. The condition ledger C1-C10, each with its exact form on (A_s, Pi) and (Q, R), and which are
   automatic, which are constraints, which are mutually independent (with examples).
2. A catalogue of explicit examples, in increasing complexity, each with: the matrices printed
   in full (numbers), the count sequence N_n for n <= 6, Z(u) factored, poles and zeros, the
   prime counts a_d, a table of which conditions hold, the physical reading (unique fixed point?
   correlation lengths? what the odd sector is), and a script name. Minimum: E0 pair shift; the
   three curve rungs; two tiny Dirichlet L-functions over F_q[x]; one Gauss/Kloosterman example;
   one graph-cover Artin L-function; two cMPS examples (C^{1|1} half-entropy, and one with FE).
3. A correction ledger for D1-D8 (PROVED / PROVED-CONDITIONAL with hypotheses / CORRECTED with
   counterexample / OPEN).
4. A closing section "What a practitioner can build tonight and what nobody can": at most one page.
Scripts: one per example under `notes/zeta-conditions/finite/`, plus `run_all.py` printing the
total tally. Fixed seeds; no zeta zeros as input anywhere.
