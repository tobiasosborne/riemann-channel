# RQ — REFUTE review of Q1 and Q2

Author: `codex:gpt-6-astra` (reviewer), 2026-10-25.

**Result:** 32 VALID, 3 MINOR, 0 INVALID, 5 UNVERIFIED (the five explicitly open proposals). The substantive repair is Q1's missing parentheses in the 7/8 parameter P_x; the core requested Q1/Q2 numerical claims reproduce.

This is a same-family review. The record also requires a second-family review before promotion. Nothing is registered or edited outside this directory. Source claims and reports of formalisation are audited as provenance; this review does not certify an entire number-field proof or a Lean build. H-MS is left to lane Q3.

Source line numbers below count newline characters (as `nl -ba` does), including form feeds within lines. O11, O7, L, K, CT and DR denote the six supplied text sources in `../../astra-2026-10-23/qrh/sources/`.

## Verification method

Original inputs are read-only. Copies in `checks/replayed/` rerun the lane scripts without writing their original output files or Numba caches. Only the record scanner's ROOT and exclusion LANE paths are adjusted to retain its original inputs. Independent scripts in `checks/` use different calculations; replay alone is not an independent certificate.

## Q1-1 — exponent arithmetic and the source's amplifier

**VALID / PROVED algebraically.** This is a statement about the actual source's displayed extraction, not merely Q2's transposition. O11 §2, lines 210–213, displays (2.3)

\[
\sum_{0<Nu\le H}|A_u(D)|^2\ll_{\nu,W,\vartheta,\varepsilon}D^{1+\varepsilon}H,
\qquad H=D^{1+\vartheta},\quad 0<\vartheta\le1/10.
\]

O11 lines 226–230 display (2.4), \(A_{p^6}(D)=A_1(D)+O_W(D/Y)\). Lines 232–235 use \(J\asymp Y/\log Y\), \(Y=H^{1/6}\), and display (2.5):

\[
|A_1(D)|^2\ll D^{1+\varepsilon}H^{5/6}+D^2H^{-1/3}.
\]

The detailed proof repeats precisely this argument in lines 661–677, ending with (3.2), \(D^{11/6+5\vartheta/6+\varepsilon}+D^{5/3-\vartheta/3}\). Taking square roots and choosing a separate small positive \(\vartheta\) for each requested loss gives \(11/12\). At \(H=D\), the two square exponents are \(11/6\) and \(5/3\), not equal. For hypothetical \(H=D^a\), the unchanged inequality gives

\[
\theta(a)=\max\{1/2+5a/12,\;1-a/6\};\qquad
\min_{a>0}\theta(a)=\theta(6/7)=6/7.
\]

`independent_scalars.py` independently solves the intersection. The source's §3 does **not** secretly replace the deletion estimate by a stronger recurrence. Thus Q1's carefully qualified “unaltered (Q1.1)” assertion is right about O11 itself. It is not a universal lower bound on every use of a hypothetical all-length mean square. Indeed the exact identity
\(A_1(D)=A_{p^6}(D)-\nu(p)A_{p^6}(D/Np)\)
follows by splitting squarefree ideals into those divisible by \(p\) and those not divisible by \(p\). A new argument could use it. The ledger correctly identifies sparse extraction as the dominant loss at the *proved* scales; its claim should retain these qualifications, rather than say sparse extraction is the only obstruction in all variants.

## Q1-2 — Liu's cubic and boundary

**VALID / PROVED scalar computation, source-labelled analytic theorem.** L lines 118–132 define the family supremum and Main theorem, with the cubic at **line 130**. The source's own derivation is at lines 244–255: set

\[
(216\kappa-18)x^2-(468\kappa-57)x+150\kappa-20=0,
\quad \kappa=2B(x)-1=\frac{18x+5}{18x+9}.
\]

Eliminating \(\kappa\) by a polynomial resultant gives, up to a nonzero scalar,
\(1188x^3-2160x^2+171x+190\). This reconstructs the cubic from the source equations rather than treating Q1's number as input. On \((0.38858,0.38859)\), the derivative is negative and the endpoint signs are opposite. Independent exact rational root isolation in `independent_scalars.py` gives

\[
\xi=0.388583354266034666797427991064892817399675\ldots,
\quad B=0.874957019420098946128603850561452982307152\ldots.
\]

The displayed digits are rounded from a certified rational enclosure; the boundary enclosure has width below \(1.37\cdot10^{-73}\). The improvement over \(7/8\) is \(0.000042980579901053871396149438547017693\ldots\). This checks the arithmetic, not all analytic estimates leading to the bound. L lines 145–147 and its final optimality discussion restrict optimality to the specified comparison system.

## Q1-3 — what the ladder identifications actually establish

**VALID with the qualifications already present in Q1; no broader identification is proved.**

* **Poisson/Fourier.** For \(\omega=(-1+i\sqrt3)/2\), the pairing \(e(zy)=\exp(4\pi i\operatorname{Im}(zy)/\sqrt3)\) has integral unimodular matrix \(\left(\begin{smallmatrix}0&1\\1&-1\end{smallmatrix}\right)\) in the basis \(1,\omega\): its determinant is \(-1\). The lattice is self-dual, and \((2/\sqrt3)dx\,dy\) gives covolume one. Poisson is therefore exactly the Fourier operator identity used in the gate pages, after fixing character and measure. O11's subsequent multiplicative identities, cusp changes, and mean-square estimates are extra arithmetic. The **full** theta transformation is only analogous to an existing gate construction.
* **D-Theta.** Taking the generator 3 of \(\mathbb F_7^\times\), the zero-extended cubic charge has entries \((0,1,\omega^2,\omega,\omega,\omega^2,1)\). Its support is exactly six; the independent script also finds Fourier support six. A pure one-qudit stabiliser state in dimension seven is either a coordinate vector (a nontrivial diagonal Pauli stabiliser) or has all seven coordinates nonzero (the eigenvector recurrence for a Pauli with nonzero translation). Weyl displacement and Clifford gates preserve the stabiliser property. This refutes the **explicit local displaced-stabiliser formulation** chosen in Q1. It does not refute the brief's deliberately vague word “analogue”, nor prove that Kubota theta has no enlarged charged-state realisation. Q1 explicitly preserves that distinction. Do not shorten its verdict to “all Z3-qunaught analogies refuted.”
* **Large sieve.** Writing the character array as \(T\), the estimate is exactly \(\|T\|^2\lesssim(M+L)(ML)^\varepsilon\). The Gram matrix \(T^*T\) is positive automatically; that fact alone gives no such norm estimate. One column forces the row-size term and a vector aligned with a row forces the column-size term. The comparison to Hilbert/Bessel positivity is legitimate, while identification with the target Weil functional or its Toeplitz matrices is unsupported. Q1 says this, rather than deriving the sieve from mere positivity.
* **D-G.** A scale-growing twist family is not a fixed spectral H1. The independent script verifies \(M^T\Omega M=5\Omega\) for \(M=((5,-5),(1,0))\), with characteristic polynomial \(X^2-5X+5\) and largest root \((5+\sqrt5)/2>\sqrt5\). Finite rank plus an integral similitude does not force RH. Separately, the one-dimensional space spanned by the delta function at the trivial flux has evaluation/average ratio equal to the number of fluxes. These refute the stated sufficiency of rank for bounded evaluation. They do not refute a construction that also supplies a positive polarisation. The exact assertion “the gap is average versus pointwise” was not a defined numerical theorem; Q1 properly replaces it with an additional evaluation inequality rather than claiming a universal impossibility theorem.

## Q1-4 — the 04v mode-depth interval

**VALID / PROVED, conditional only on the cited zero-free theorem.** The precise definition is `notes/deninger-cusp/astra-proofs.md:415–418`, (D4.11):
\(w_\rho=\gamma/2+i(1-\beta)/2\), with D5.3 applying it to the arithmetic zero jets. The shard's `thm:level-model-decomposition` at `report/sections/04v_deninger_cusp.tex:146–154` uses these arithmetic modes and states the GRH equivalence for common damping.

The open exclusion \(\beta>7/8\), together with functional equation and conjugation (or the theorem for the dual character), gives the **closed** range \(1/8\le\beta\le7/8\) for nontrivial arithmetic zeros. Applying the decreasing affine map \((1-\beta)/2\) gives exactly \([1/16,7/16]\). The endpoints cannot be discarded by an open zero-free theorem. `independent_scalars.py` checks both endpoints exactly. This is a statement about arithmetic mode depths, not the delay states or local scattering factors (whose extra modes are explicitly separated in D5), and gives neither simplicity, a bounded equivalent metric, nor an operator-norm decay theorem. Q1's annotation retains these restrictions.

## Q1-5 — exact graph L2 sampling

**VALID / PROVED (`Q1-SAMPLE`).** Gauge-fix a spanning tree and attach variables \(x_1,\ldots,x_g\) to cotree edges, with inverse variables on reversed edges. In the permutation expansion of \(\det(I-zA_x+(\deg-1)z^2)\), every component is a fixed vertex, a dimer, or an oriented simple cycle. A cotree edge appears at most once in a cycle; a dimer contributes \(x_jx_j^{-1}=1\). The extra Bass factor is independent of flux. Thus each coefficient of \(Q_x=\det(I-zB_x)\), and any fixed linear combination \(F\) of them, has Laurent support in \(\{-1,0,1\}^g\). The support of \(F\overline F\) lies in \(\{-2,-1,0,1,2\}^g\). Haar averaging selects exponent zero; N-torsion averaging selects exponents divisible by N. For N≥3 these are identical. The argument works for simple nonregular graphs as well, with the usual diagonal degree matrix in Bass.

`independent_graphs.py` enumerates **vertex permutations**, rather than Q2's primitive-cycle DFS, and retains the full integral Laurent exponents. It checks all coefficient degrees 0–13 for K4, 0–25 for the cube, and the mixed function \(F=\sum_D2^D[z^D]Q_x\), at **N=2,3,4,5**. Selected normalized energies:

| graph, coefficient | Haar | N=2 | N=3 | N=4 | N=5 |
|---|---:|---:|---:|---:|---:|
| K4, D=3 | 8 | 16 | 8 | 8 | 8 |
| K4, D=12 | 256 | 256 | 256 | 256 | 256 |
| cube, D=4 | 12 | 24 | 12 | 12 | 12 |
| cube, D=12 | 1452 | 3512 | 1452 | 1452 | 1452 |
| cube, D=24 | 65536 | 65536 | 65536 | 65536 | 65536 |

This also shows N=3 is a sharp universal sufficient threshold: N=2 already fails on a coefficient of K4, not merely on an abstract Laurent polynomial. This is a coefficient sampling theorem; it says nothing analogous about arbitrarily long trace powers or unsigned ideal counts.

## Q1-6 — citation scopes and formalisation provenance

**The mathematical scope notes are accurate as source reports. The CT numbering needs a provenance qualification (MINOR).** None of the citation-row verdicts below certifies a full analytic proof or a Lean build.

| candidate | adjudication and independent source inspection |
|---|---|
| `cit:openai-qrh-seven-eighths` | **VALID.** O7 lines 177–184 state the three families, open boundary, principal pole, and no RH conclusion. L lines 111–115 independently report the publisher's formalisation scope: zeta, Dirichlet, finite-order Hecke, principal poles excluded, applications excluded. This is evidence of a **reported** formalisation; it is not a build. |
| `cit:openai-qrh-eleven-twelfths` | **VALID.** O11 lines 55–61 state the same families and distinguish the companion 7/8 proof. No Lean/formalisation assertion occurs in the supplied O11 text. A stronger formalised conclusion would not formalise this proof. The amplifier derivation was independently checked above. |
| `cit:kintali-qrh-47-48` | **VALID.** K lines 19–32 give Theorem **1**, primitive/imprimitive scope, principal pole, open boundary, and the unconditional theta/sieve/density inputs; the conditional DR prime theorem is explicitly excluded. No Lean claim occurs in the supplied manuscript. |
| `cit:liu-qrh-cubic-bound` | **VALID.** L lines 125–147 and 2916–2928 identify the new Main theorem/Theorem 27.1 and system-specific optimum; Theorem 1.1 at lines 338–342 restates O7. Lines 307–312 report Lean for all three improvements. Lines 4096–4105 name PartIV.lean, namespace CombineV22, the four exported conclusions, and reported axiom audit. All are reports, not locally checked files. The independent cubic certificate is Q1-2. |
| `cit:cureton-thorner-qrh-31-32` | **MINOR.** The supplied CT **abstract** states every number field's Dedekind zeta and finite-order Hecke corollary for Re s>31/32, wherever holomorphic; lines 140–142 explicitly attribute proofs and Lean formalisation to AxiomProver. The source contains neither “Theorem 1.1” nor “Corollary 1.2”, nor the author README's axiom inventory. Q1 says it inspected that external README, but it is not among the supplied files. Use “CT abstract, Dedekind statement and finite-order Hecke corollary” until the exact version of the manuscript/README is archived. Its mathematical scope and metadata limitation are otherwise right. |
| `cit:dunn-radziwill-cubic-theta` | **VALID as a citation of the unconditional input.** DR §5 begins at line 866; its group, cubic multiplier, cusp coefficients and transformation statements carry no GRH hypothesis. O7 lines 185–190 explicitly distinguish these formulas from the conditional prime asymptotic. The supplied CT bibliography identifies the Annals 2024 publication. No Lean assertion is supplied. |
| `cit:dunn-radziwill-prime-bias-conditional` | **VALID as a conditional citation.** DR lines 117–126 explicitly assume Hecke GRH over Q(omega); the displayed main constant, weight integral, X^(5/6)/log X, and rational-prime range agree. Fixed-strip quasi-RH does not discharge that assumption. |

`QuasiRiemannHypothesis.lean` has exactly one theorem (lines 5–7):

```lean
theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0 := by
  sorry
```

It quantifies over complex s and asserts **only zeta** nonvanishing when Re s>7/8. It has no explicit s≠1 hypothesis, no Dirichlet or Hecke statement, and no proof term beyond `sorry`. Lean's total function at the classical pole is a library convention, not a claim that the meromorphic pole is holomorphic. The distinction between this comparator, external reports, and a kernel-checked build is essential; Q1 makes it. The supplied file alone cannot substantiate any full formalisation claim.

## Q2-1 — `prop:ff-sextic-amplifier`

**VALID / PROVED-conditional on H-MS.** In (2), zero extension gives \(\chi_n(p^6)=1_{p\nmid n}\) even when p divides the conductor of nu. Every monic degree-D multiple of a monic degree-k p is p times one of exactly q^(D-k) monic polynomials; \(|\mu\nu|\le1\). If k>D the error is zero. This proves both the identity and the inequality with constant one.

For (4), p↦p^6 is injective on monic primes by unique factorisation, although its images represent the same trivial Kummer class away from their different zero masks. They are **distinct polynomial rows**, all of degree 6k≤h. The exact formula is
\(\pi_q(k)=k^{-1}\sum_{d\mid k}\mu_{\mathbb Z}(d)q^{k/d}\), with leading constant **1**, not 6 or q−1. For q≥7, the sum of proper terms is bounded by \(\sum_{j\le k/2}q^j\); for k≥2 this gives the sufficient explicit bound \(\pi_q(k)\ge(5/6)q^k/k\), and k=1 is exact. Thus the displayed coefficient 2/π_q(k) follows directly from the two-term square inequality; the implied constant C may absorb at most 12/5 here, along with the H-MS constant. There is no factor of six from prime generators because monicity removes units.

Write h=(1+vartheta)D+O(1) and k=h/6+O(1). The two square exponents are \((11/6+5\vartheta/6+\varepsilon)D+O(1)\) and \((5/3-\vartheta/3)D+O(1)\). Taking square roots gives precisely (5), with sqrt(k) on the first term. Fixed q,nu and sufficiently small fixed positive vartheta,epsilon give every positive loss above 11/12. The ball has q^(h+1) rows; its factor q can be absorbed only because q is fixed in the proposition, as stated.

For Littlewood, \(\sum A_1(D)z^D=1/L(z,\nu)\) near zero. A coefficient bound gives convergence on the **open disk**, hence no zero of L there. Conversely Cauchy on every smaller circle gives an epsilon loss; a pole of order r of 1/L on the boundary can produce D^(r−1). No exact O(q^(theta D)) converse without that qualification is asserted. The conclusion is |zero|≥q^(−11/12), including the boundary as a possible zero location, or |reciprocal root|≤q^(11/12). For primitive even characters Weil concerns L/(1−z). Q2 correctly separates this completed polynomial, imprimitive Euler factors, and the principal rational function. The functional-equation annulus is a separate deduction for nontrivial factors and the conjugate character.

Independent checks: `independent_ff.py` factors the columns and evaluates residue-field characters directly, checks all seven linear prime rows at D=2 and the exact two-scale deletion repair, and prints π_7(k), k=1,…,6. The first values are 7,21,112,588. This is no proof of H-MS; Q3 retains that task.

## Q2-2 — `prop:ff-complete-row-ms`

**VALID / PROVED.** Let l=lcm(n,m) have degree L≤2D. Division by monic l maps the vector space deg u≤h onto R/(l) with fibres of size q^(h+1−L) exactly when **h+1≥L**, including equality. When h=L−1, the ball is precisely the canonical residue representatives: requiring h≥L would waste a whole degree. For distinct squarefree n,m, a prime in their symmetric difference carries a nontrivial order-six character with exponent +1 or −1, so the full residue sum vanishes. For n=m it is the unit indicator, with φ(n) nonzero residues. Thus (6) holds for h≥2D−1 for every fixed nu. The upper bound follows from at most q^D columns and φ(n)≤q^D. It is not a short-row theorem.

The independent script uses nu=(·/(t^3+t+1))_2, **literal enumeration of all polynomials**, and factorisation/residue-field exponentiation rather than the lane's resultant/Pellet routine. There are 42 squarefree degree-two columns and weighted diagonal 1764. Its entire requested table is:

| h | rows q^(h+1) | brute-force S(2,h) | q^(h−1)·1764 |
|---:|---:|---:|---:|
| 0 | 7 | 24 | 252 |
| 1 | 49 | 1080 | 1764 |
| 2 | 343 | 11844 | 12348 |
| 3 | 2401 | 86436 | 86436 |
| 4 | 16807 | 605052 | 605052 |

The h=2 failure and h=3 equality make the off-by-one issue directly visible. The formula can accidentally hold below its sufficient threshold in other examples; the threshold assertion concerns complete coverage for every possible modulus, not a claimed iff for the scalar value S.

## Q2-3 — `prop:ff-gauss-discriminant-absorption`

**VALID / PROVED using the named Hasse–Davenport identity, with an exhaustive exact finite check.** With the lane's additive character \(e_n(x)=\psi_0([t^{-1}]x/n)\), partial fractions at the roots give local trace character \(\psi_0(\operatorname{Tr}(x(a)/n'(a)))\). On the degree-d residue field, the normalized lift is **(−1)^(d−1) tau_j^d**. Substituting x=n'(a)y contributes kappa(Norm n'(a))^j with positive exponent. Multiplication over primes gives sign (−1)^(D−#P)=mu(n)(−1)^D and norm product
\(R_n=\prod_{n(a)=0}n'(a)=\operatorname{Res}(n,n')\).
This yields (8) exactly. Swapping the two resultant arguments happens to give the same value, since D(D−1) is even; replacing the resultant by the **discriminant** does not: disc(n)=(−1)^(D(D−1)/2)R_n.

Frobenius permutes the D roots with #P cycles. A Vandermonde square root of disc changes by (−1)^(D−#P), so eta(disc n)=(−1)^D mu(n). Hence
\(\operatorname{eta}(R_n)=(−1)^D\operatorname{eta}((−1)^{D(D−1)/2})\mu(n)\).
Taking the ratio of (8) for j=−1 (i.e. 5) and j=2 gives (9), with the lane's precise c_D; no inverse resultant or missing degree sign is allowed. Nontrivial finite-field Gauss sums have modulus sqrt(q), hence |c_D|=1. Cubing the j=2 formula also gives \(\gamma_2(n)^3=\mu(n)(-\tau_2^3)^D\).

`independent_ff.py` does **not** obtain the direct Gauss sums from (8). It enumerates every residue x mod n; characters come from exponentiation modulo each irreducible factor, and the additive phase is the top coefficient of x. It computes R_n separately as the product of norms of n' at the residue roots. All identities are compared as integer coefficient vectors in Z[zeta_42], with normalization cancelling algebraically.

| degree | squarefree monics checked | factorisation types and counts |
|---:|---:|---|
| 1 | 7 | (1): 7 |
| 2 | 42 | (1,1): 21; (2): 21 |
| 3 | 294 | (1,1,1): 35; (1,2): 147; (3): 112 |

All **1715** positive-degree comparisons (five j values for each of 343 moduli) and all **343** absorption comparisons pass. The unit modulus n=1 has a one-term Gauss sum 1 and both formulas reduce to 1=1. Omitting the Hasse–Davenport sign fails in **840** comparisons; using disc in place of R fails in **1008**. The exhaustive check is stronger than the lane's sampled 30 checks at q=7, but is still only finite evidence for the general formula, whose proof is the preceding factorisation argument.

## Q2-4 — graph Möbius obstruction, trace criterion, signed mean square

**VALID (`obs:graph-mobius-littlewood-fails`, `prop:graph-flux-signed-ms`).** Enumerating rooted cyclically nonbacktracking closed walks gives \(zZ_s'/Z_s=\sum_{k\ge1}\operatorname{Tr}(B_s^k)z^k\). The determinant has the same logarithmic derivative and constant term, so the Euler product is 1/Q_s and its Möbius series is Q_s. The latter is a degree-at-most-2m polynomial, regardless of its zero locations. Q1's graph identity Q1.6 follows by finite character orthogonality for any fixed multiplicative coefficients nu; **polynomial vanishing requires nu itself to be a graph flux**, as Q1 explicitly says. Q2 uses nu=1 throughout.

Our permutation enumeration gives for zero-flux K4
\[
Q_0(z)=(1-z^2)^2(1-3z+2z^2)(1+z+2z^2)^3,
\]
with Q_0(1/2)=0 and [z^13]Q_0=0. Thus the claimed coefficient-growth/zero-location equivalence is false, even with theta=0. Removing trivial factors still leaves a polynomial whose reciprocal eigenvalues have modulus sqrt(2)>1. This is a refutation of the proposed spectral inference, not a claim that K4 is non-Ramanujan.

For (14), if rho(B_s)≤q^theta, the trace of each Jordan block is its multiplicity times its eigenvalue to the kth power, giving the bound with constant 2m. Conversely, that trace bound continues −zQ_s'/Q_s into |z|<q^(−theta). At any nonzero zero r of Q_s of multiplicity e, the residue is −er≠0, so there can be no such zero in the disk. This proves the exact exponent criterion without a semisimplicity hypothesis. Known trivial powers must be subtracted before applying the Ramanujan version, including the parity sector. The inverse-series version needs an epsilon allowance at multiple boundary poles, as Q2 says.

For (15), expanding the square and averaging a character difference leaves exactly homologous **signed** pairs. Their off-diagonal terms can be negative. Since Q_s has degree at most 2m, every character Fourier coefficient b_D vanishes for D>2m, giving exact cancellation of the positive diagonal. Our independent determinant enumeration followed by rational division of Q_0(z^2)/Q_0(z) gives:

| K4, N=2 | C_D | mean square | diagonal 8 C_D | off-diagonal |
|---|---:|---:|---:|---:|
| D=12 | 1368 | 2048 | 10944 | −8896 |
| D=13 | 3840 | 0 | 30720 | −30720 |

The normalized N≥3 assertion in this candidate is exactly the sampling theorem reviewed in Q1-5. No matching-polynomial theorem is inferred from this quadratic average.

## Q2-5 — unsigned parity and the surface obstruction

**VALID (`prop:graph-squarefree-flux-parity`, `prop:surface-sixfold-no-amplifier`).** Factorwise, (1+x)=(1−x^2)/(1−x), so
\(C_s(z)=Q_{2s}(z^2)/Q_s(z)\). This is an identity of formal series; there is no collision correction missing. Its zero-flux dominant poles are 1/q and, exactly for a bipartite graph, −1/q, both simple. The numerator cannot cancel them: q^(−2) is strictly inside the zero-free disk of Q_0. Regularity, connectedness and q>1 are used here. Cauchy–Schwarz on at most min(N^g,(2D+1)^g) occupied homology classes proves (17); taking absolute values of signed off-diagonal weights gives its second inequality.

For a unitary scalar flux t, the Bass quadratic and Hermiticity imply that an eigenvalue of B_t of modulus q must be ±q: writing it as q exp(i alpha), reality of \(\mu+q/\mu\) gives (q−1)sin(alpha)=0. Equality in the adjacency triangle inequality forces gauge equivalence to all plus or all minus edges. The latter class is epsilon, the length-parity character. Consequently all other fluxes have strictly smaller spectral radius. Applying the order-r root-of-unity filter gives exactly the lane's three cases:

* nonbipartite, epsilon outside the subgroup generated by s: limit 1/r;
* nonbipartite, epsilon in that subgroup: main term (1+(−1)^D)/r, with r even;
* bipartite: limit 1/r along even D, no ideals in odd D.

This concerns a **fixed** graph and fixed flux, with constants depending on them, not uniformity as N grows. For s=epsilon the even/odd statement is exact. More generally, when epsilon lies in the subgroup, odd-degree triviality is exactly impossible because raising chi_s(n)=1 to r/2 would contradict (−1)^D=−1; the lane's O(c^D) formulation is valid but weaker there.

The independent calculation enumerates vertex cycle covers and divides the associated rational series rather than enumerating primitive primes. At K4,D=16 it gives C_D=27216 and C_(0,0,1),D=−176. Thus the count with trivial value is (27216−176)/2=13520, and **13520/27216=845/1701**. The parity flux (1,1,1) has 27216/27216 at degree 16 and 0/3840 at degree 13. All six other nonzero order-two fluxes have 845/1701 at degree 16. The cube's odd-degree counts vanish in the independently computed entire table.

For a genus-a surface, multiplication by six on (Z/N)^(2a) has kernel of size gcd(N,6)^(2a). The perfect intersection pairing identifies every element of this kernel with the same zero character. For N coprime to six the operation permutes all rows, and for N dividing six every image is zero. Counting duplicates also repeats their contribution to the norm budget, so no amplifier gain results. Our torus enumeration gives (row count, distinct image rows, zero rows) equal to (4,1,4), (9,1,9), (36,1,36), (49,49,1), (144,4,36) for N=2,3,6,7,12. The claim refutes this **literal** linear surface construction; it does not prohibit an enriched arithmetic kernel with additional data.

The unrelated local-limit conjecture remains OPEN. Its finite projected-homology statistics are independently reproduced by integral Laurent series division: at D=8,12,16 the zero counts/total counts are 3/33, 84/1368, 1188/27216, giving D·Pr(0)=8/11,14/19,44/63. This verifies the evidence, not the asymptotic (19).

## Additional body claims omitted from the candidate tables

The protocol also requires the PROVED/REFUTED body items. Where Q1 supplies no candidate ID, the aliases below are review-local, and their scope is stated explicitly.

### Q1-seven-eighths-synopsis — MINOR: a missing pair of parentheses breaks the printed certificate

**REFUTED as printed; corrected scalar certificate PROVED.** Q1 `astra-proofs.md:286` writes
\(P_x=2-(8x/9)(1-x)\). O7 Proposition 19.2, **lines 11137–11143**, actually defines

\[
\boxed{P_x=(2-8x/9)(1-x).}
\]

This is independently confirmed by O7 lines 11701–11706: after y=1/2−x, \(P_x=(7+18y+8y^2)/9\). Q1's `checks/exponents.py` uses this **correct** latter polynomial, so its passing check did not test the prose's formula.

Keeping the rest of Q1's definitions of J, R and E unchanged, `independent_scalars.py` computes at \(\delta=2/5,x=1/2\)

\[
E_{\rm source}=-41/155760<0,
\qquad E_{\rm Q1\ printed}=6709/207600>0.
\]

Thus the prose as written does not prove its asserted negative endpoint margin. The minimal fix is the boxed parenthesization; no change to the source theorem or Q1's scalar program is needed. With that fix, independent polynomial expansion verifies O7 (20.9) exactly. Its completed-square terms are nonnegative on 0≤y≤1/2, 0≤delta≤5/6; \(v=51+41y\le17(3+5y)\) and \(J\le5/2\) give \(-E\ge49/440640>1/10000\), just as O7 lines 11723–11742 state. The low comparison remains \(17/96+1/96=3/16=7/8-11/16\). The full analytic moment/contour argument remains a cited source claim, not independently proved by this scalar check.

### Other Q1 body claims

| alias | verdict and derivation / limitation |
|---|---|
| `Q1-smoothed-Littlewood` | **VALID.** Substitution y=Nn/D in the Mellin integral gives the factor (Nn)^(−s) and the transform int W(y)y^s dy/y, so the reciprocal-L identity has the correct sign of s. For a proposed zero rho, W(y)=y^(−rho)phi(y) makes its transform strictly positive. Compact support removes small D, and every epsilon loss can be chosen below the distance of a compact set from the asserted boundary. O11 lines 686–714 contain the same argument. Principal poles are not zeros. |
| `Q1-Gauss-bars` | **VALID.** Starting from gamma_2^3=mu·alpha, gamma_1 gamma_2=mu·alpha·G and gamma_1 gamma_(−1)=chi(−1), division gives mu gamma_(−1)=chi(−1)G^(−1)bar(alpha)gamma_2. G=bar(chi(4))gamma_3. The archived images `theta-05.png` and `theta-06.png` were visually inspected: both conjugation bars are present. `independent_scalars.py` now verifies all four local identities **exactly** in Q(zeta_42) at the norm-seven primary prime −2−3omega, after clearing square-root normalizations; the unbarred version leaves an explicitly printed nonzero polynomial. This independently strengthens the lane's 80-digit check. |
| `Q1-theta-coefficients` | **VALID as a source-dependent identification.** The coefficient in O11 (2.10) is that of **bar(theta)** and includes bar(chi_n(lambda)^2), as the image confirms. Substitution into (2.11) cancels this character factor. In (2.12), splitting alpha(nb^3), xi(nb^3) and the residue character, and using sqrt(Nb)/sqrt(X)=(Nb)^(−1)/sqrt(X/(Nb)^3), gives the asserted completed coefficient expansion. No coprimality between n and b is required (O11 lines 1116–1118); only n is squarefree. DR lines 890–911 and 930–975 establish the stated subgroup/cubic multiplier versus the full group's cusp components. This is not a proof from scratch of Patterson's coefficient theorem. |
| `Q1-cube-inversion` | **MINOR.** Complete multiplicativity makes the coefficient of a total cube index b equal to w(b) times sum_(d|b)mu(d); this is 1 for b=1 and 0 otherwise, proving the exact inversion. Q1's displayed `overline{alpha(b)}^{,3}` at line 220 has a stray comma: write `overline{alpha(b)}^3`. This is a notation fix. Discarding cube contributions by positivity would be invalid; Q1 explicitly avoids it. |
| `Q1-transfer-synopsis` | **VALID as a conditional reduction/source synopsis.** O11 (5.5), lines 1134–1145, has the extra Nf; (5.11)–(5.12), lines 1276–1289, have H'≤HL/(Sigma F), H'/Sigma'≤H/Sigma and Sigma'≤L, with the stated test enlargement and 4m+12 derivative order. Q1 records these. In the schematic F=1 case H_c^3=X^2/H^2, L=X/(Nb)^3 and Nb>H_c imply H'<H^3/X^2: at H/X=D^(−vartheta), the contraction is D^(−2vartheta). Fixed positive vartheta makes the iteration finite; setting vartheta=0 would not. This verifies the reduction given the cited transformation bounds, not an independent proof of the omitted analytic estimates. |
| `Q1-kintali-synopsis` | **VALID as source synopsis and scalar calculation.** For a≤4/5, a+(1/2)min(1,5(1−a))−1/3=a+1/6≤29/30; for a≥4/5 it is 13/6−3a/2≤29/30. Therefore the central margin against 47/48 is exactly 1/80, independently printed. K lines 884–915 use this bound and the 501/1000 cutoff to obtain 1/4800. K lines 308–328 give the twelve-row multiplicity claim. This is a report of those analytic inputs, not a fresh conductor/density proof. |
| `Q1-base-change` | **VALID.** At split rational primes the two local factors coincide; at inert primes (1−a p^(−s))(1+a p^(−s))=1−a^2 p^(−2s). Together with finitely many deleted factors this derives the quadratic base-change identity in O11 lines 715–723. At s=1 a principal factor's pole requires Dirichlet nonvanishing for the other factor. This involves finite-order norm-pullback characters, not the elliptic infinity-type characters over Q(sqrt(−7)). |
| `Q1-record-audit` | **VALID as a dated keyword inventory and limited non-promotion audit.** Every archived file/text pair in its 225-row scan is present in the relocated rerun. New review files add matches; occurrence IDs and current hit totals are not immutable mathematical facts. The mode-depth inference is independently checked in Q1-4. A fixed strip alone cannot force critical-line positivity (a hypothetical functional-equation-symmetric quartet at real parts 1/4 and 3/4 obeys the strip but violates the critical-line condition), simplicity, or a bounded metric. Finite-order scope excludes nonzero infinity type. Those are the reasons no listed GRH/positivity claim is promoted. The keyword scan is not a proof that every implicit assumption in the repository was located. |
| `Q1-arithmetic-consequences` | **VALID as accurately attributed source claims, not independent certification of the applications.** O11 lines 75–93 explicitly list the nonresidue, deterministic square-root/Miller, class-number and idoneal consequences. The square-root algorithm implication follows by searching up to the asserted polylogarithmic nonresidue bound and applying Tonelli–Shanks. The fixed-strip explicit-formula bound gives a power saving rather than square-root error. A logarithmic near-one region with c=(log 3)/8 and conductor at least 3 lies inside Re s>7/8 (with the same open boundary convention); nothing excludes all real zeros in (0,1). Q1 distinguishes these applications from the reported Lean scope. |

**OPEN / UNVERIFIED proposals.** `Q1-THETA` is an explicitly conjectural enlarged charged-state construction; the six-support obstruction does not prove it. `Q1-EVAL` is an explicitly conjectural evaluation/lower-energy statement; its sufficient condition is sound: for conductor degree m=o(d), the coefficient bound from labelled Weil is q^(d/2) binomial(d+O(m),O(m))=q^(d/2+o(d)), but no short-family lower bound has been proved here. `Q1-TRACE` is explicitly conjectural: the required nondegenerate Hessian and uniform control of the dominant eigenvalue contributions are not supplied by coefficient sampling. These stay OPEN; their UNVERIFIED verdicts do not refute them. Likewise `conj:ff-short-row-ms` remains OPEN in this review and is assigned to Q3, while `conj:surface-squarefree-local-limit` requires an actual uniform local-limit proof, not three finite statistics.

### Other Q2 body claims

`Q2-power-reciprocity` is **VALID**: for monic polynomials the residue symbol is kappa(Res(denominator,numerator)); swapping the resultant arguments contributes kappa(−1)^(deg a deg b)=(−1)^(((q−1)/6)deg a deg b). The independent residue-field script checks all coprime ordered pairs of monic degree one or two over F7, including the nontrivial sign.

`Q2-finite-poisson` is **VALID**: for h<M−1, the degree ball is an (h+1)-dimensional additive subspace in the M-dimensional residue ring. Its annihilator has size q^(M−h−1). Summing the positive-sign Fourier transform over that annihilator selects −V_h=V_h, giving exactly the factor q^(h+1−M) in (7). For a primitive character, changing x to v^(−1)x at units gives bar(chi(v))G(chi); primitivity makes the nonunit transform zero. This identity does not estimate the remaining character sums. Formula (8) leaves a discriminant character, so Q2's refusal to infer H-MS from individual Gauss evaluations is correct.

`Q2-exponent-comparison` is **VALID**: the function theta(alpha) in (11) is precisely the one independently optimized in Q1-1. At alpha=2 it gives 4/3, explaining why the proved complete rows do not yield the desired theorem; at alpha=3/4 it gives max(13/16,7/8)=7/8. These are deductions from hypothetical bounds at those scales, not claimed available bounds. Neither the geometric comparison nor the graph counterexamples establishes a universal necessity theorem for H1.

## Q2-6 — proposed notebook annotations

These adjudications concern the proposed sentences, not permission to modify the pages. No record page is edited.

| proposed destination | decision | wording / reason |
|---|---|---|
| Q2 `data-ladder.md` §2 | **AGREE.** | Keep “conditional on its function-field short-row analogue”, fixed q and fixed nu. Many distinct polynomial/arithmetic representatives with small divisibility masks matter; a quotient flux repeated many times is not an amplifier. The signed graph coefficient average eventually vanishes and is not a spectral criterion. |
| Q2 `data-ladder.md` §4 | **AGREE.** | A quantitative family estimate can give a partial exclusion region without constructing the proposed integral H1. It does not provide the target polarisation positivity. The contrast between geometric arithmetic structures and proof methods is accurately qualified. |
| Q2 `graph-super.md` §6 | **AGREE-WITH-CHANGE.** | “The linear characteristic-polynomial average is the matching polynomial. The quadratic average of coefficients of det(1−zB_s) is a different signed-pair identity, with exact N≥3 sampling and no large-degree spectral content. Interlacing selects an upper spectral bound; bipartite symmetry supplies a simultaneous lower bound.” The last qualification prevents ‘one unnamed flux is RH’ from being read as a general nonbipartite two-sided theorem. |
| Q2 `zn-flux.md` §4 | **AGREE.** | Explicitly retain both thresholds: N≥2 for the **linear** determinant average, N≥3 for arbitrary **squared coefficient** averages. The sampling proof does not alter Theorem 4.1's N≥2 statement. |
| Q2 `gauge-groups.md`, HPS | **AGREE-WITH-CHANGE.** | “Hall–Puder–Sawin gives covers with a one-sided bound on the **new** adjacency spectrum for general loopless base graphs; bipartite symmetry gives a two-sided bound for a bipartite base. The cover retains the base spectrum.” A real-rooted averaged polynomial alone does not select one member controlling both ends. As an exact warning, the all-negative K4 has eigenvalues −3,1,1,1, so it satisfies the upper tree-band bound while violating the lower one. The cited HPS source directory is absent in this checkout despite its manifest entry; retain this as a bibliographic scope correction, not a newly byte-verified HPS theorem. |
| Q2 `ff-dirichlet.md` | **AGREE.** | The existing §0 defines Lambda=L/(1−z) for even characters correctly. Preserve that notation in future briefs and in the quasi-bound comparison; no correction to that definition is needed. |

Q1's proposed record corrections are also adjudicated individually:

| proposed destination | decision | scope to preserve |
|---|---|---|
| `data-ladder.md` §§2,4,4b | **AGREE-WITH-CHANGE.** | Attribute the number-field strip to the cited preprints and reported formalisation, keep the review gate, and distinguish Gram positivity from Weil positivity. Phrase the 6/7 statement as the optimum of the **unchanged displayed amplifier inequality**, not a general theorem about all-length mean squares. |
| `zn-flux.md` §§4–5; `graph-super.md` §6 | **AGREE-WITH-CHANGE.** | Use the separate linear/quadratic thresholds and one-sided interlacing wording above. Trace averages have no bounded Laurent-support theorem at fixed N. |
| `functional-equation-gate.md` §3; `gate-phases.md` §3 | **AGREE.** | Poisson is exact after the additive character/measure are specified; cubic metaplectic reflection requires extra charge/cocycle/cusp data. Only the literal displaced-stabiliser formulation was refuted. |
| `family-vacuum.md` §3; `cm-lift.md` §§2.5,4 | **AGREE.** | An auxiliary family of character sums is not a commuting family of symplectic similitudes. Finite-order Hecke scope does not cover nonzero elliptic infinity type. |
| `window-similitude.md` §3 | **AGREE.** | Finite rank counts distinct spectral atoms and alone implies neither RH nor positivity. No quasi-RH metric upgrade follows. |
| `notes/what-rh-has-become.md` §5; shard 03 hierarchy | **AGREE-WITH-CHANGE.** | Add a source-labelled fixed-strip/power-saving rung; do not present this review as an independent certification of the cited number-field proofs. Keep the distinction from square-root error. |
| `notes/metric-tomography/metric-as-state.md` §4.4 | **AGREE-WITH-CHANGE.** | Update the reported analytic results with their provenance, and distinguish near-one exclusion from critical-line proportions or simplicity. |
| shard 04v; `deninger-cusp/astra-proofs.md` D5 | **AGREE.** | The interval is [1/16,7/16] for the **individual arithmetic modes** only, conditional on the cited strip; no common damping value or operator-norm assertion. |
| `notes/adeles/software-and-algorithmic-scope.md` | **AGREE.** | Fixed-strip consequences do not automatically preserve algorithms' GRH-dependent quantitative complexity or certification thresholds. A revised algorithmic claim needs its own proof. |

## Replay audit and correction ledger

`checks/audit_replays.py` compares every output line, not just the highlighted examples. All six mathematical output files are byte-identical to their archives: Q1 exponents (23 lines), Q1 structural checks (15), Q2 function-field output and run output (107 each), Q2 graph output and run output (1429 each). Every original source SHA-256 matches. The relocated record scan preserves all 225 archived file/text entries; newly written review pages add entries, so its total is time-dependent. The original scripts and outputs were not rewritten.

The independent work uses different routes: exact source-derived polynomial elimination/root isolation and cyclotomic Gauss identities; literal finite-field rows via factorisation and residue-field exponentiation; graph vertex-permutation determinants and formal rational-series division. No number-field zeros or RH assumptions enter these checks. Weil occurs only in explicitly labelled comparison/sufficient-condition discussions.

Three repairs are required before copying Q1's material:

1. **Substantive transcription repair:** P_x=(2−8x/9)(1−x), not 2−(8x/9)(1−x). The wrong expression gives a positive endpoint error at the printed exact test point; the lane's own scalar script already uses the correct one.
2. **Notation repair:** remove the stray comma from the exponent of bar(alpha(b)) in the cube-inversion display.
3. **Provenance repair:** cite the supplied CT abstract for its two scope statements unless the manuscript/README supporting the theorem numbering and axiom inventory is archived. No Lean build was performed here.

The Q1-1 balance, Q1-4 interval, Q1-SAMPLE threshold, and all seven proved/refuted Q2 candidate rows survive. The narrow interpretations of D-Theta and D-G must survive too: neither is a prohibition on every richer state construction or every possible RH proof. H-MS and the open new constructions are not settled by this review.

## Verdict lines

VERDICT Q1-1: VALID — 11/12 and the restricted 6/7 optimization follow from the source's own amplifier inequality.
VERDICT Q1-2: VALID — source-derived elimination and exact root isolation reproduce Liu's cubic boundary.
VERDICT Q1-poisson-gate: VALID — Fourier duality is exact with specified pairing and measure, while the full arithmetic reflection adds data.
VERDICT D-Theta: VALID — the six-point support refutes the specified displaced-stabiliser model, not every theta analogy.
VERDICT Q1-large-sieve-positivity: VALID — the sieve is a quantitative Gram norm bound and is not Weil positivity.
VERDICT D-G: VALID — finite rank alone supplies neither critical spectrum nor bounded point evaluation.
VERDICT Q1-4: VALID — the open 7/8 exclusion and functional equation give closed arithmetic depths [1/16,7/16].
VERDICT Q1-SAMPLE: VALID — exact Laurent enumeration confirms Haar equality for N=3,4,5 and failures at N=2.
VERDICT cit:openai-qrh-seven-eighths: VALID — the cited family scope and reported formalisation are distinguished from the sorry comparator.
VERDICT cit:openai-qrh-eleven-twelfths: VALID — the source states the same families and does not report formalising this proof.
VERDICT cit:kintali-qrh-47-48: VALID — Theorem 1 has the stated primitive/imprimitive scope and no supplied Lean claim.
VERDICT cit:liu-qrh-cubic-bound: VALID — the source reports Lean for the cubic bound and restricts optimality to its comparison system.
VERDICT cit:cureton-thorner-qrh-31-32: MINOR — the supplied abstract supports scope and Lean provenance but not the quoted theorem numbering.
VERDICT cit:dunn-radziwill-cubic-theta: VALID — the unconditional Section 5 input is separated from the conditional prime theorem.
VERDICT cit:dunn-radziwill-prime-bias-conditional: VALID — the explicit Hecke-GRH hypothesis is retained and is not discharged by a fixed strip.
VERDICT Q1-smoothed-Littlewood: VALID — the Mellin transform and nonzero test transform give the stated open-half-plane implication.
VERDICT Q1-Gauss-bars: VALID — exact norm-seven cyclotomic identities confirm both required conjugations.
VERDICT Q1-theta-coefficients: VALID — the source-normalized conjugate-theta coefficients give the stated completion with cube factors.
VERDICT Q1-cube-inversion: MINOR — remove the stray comma in the exponent while retaining the valid multiplicative inversion.
VERDICT Q1-transfer-synopsis: VALID — the stated scale contraction follows conditionally from the correctly transcribed source bounds.
VERDICT Q1-seven-eighths-synopsis: MINOR — P_x must be (2−8x/9)(1−x), since the printed parentheses destroy the negative endpoint margin.
VERDICT Q1-kintali-synopsis: VALID — the source-level synopsis and exact 1/80 central margin agree.
VERDICT Q1-base-change: VALID — the Euler-factor identity has the stated finite-order scope and separate pole bookkeeping.
VERDICT Q1-record-audit: VALID — the archived keyword inventory reproduces and its listed GRH claims receive no unjustified promotion.
VERDICT Q1-arithmetic-consequences: VALID — these are accurate source attributions with applications excluded from the reported Lean scope.
VERDICT Q1-THETA: UNVERIFIED — the repaired charged-state construction is an open proposal without a global compatibility proof.
VERDICT Q1-EVAL: UNVERIFIED — the proposed short-family evaluation or lower-energy estimate remains open here.
VERDICT Q1-TRACE: UNVERIFIED — the proposed trace asymptotic still needs its Hessian and uniform spectral analysis.
VERDICT prop:ff-sextic-amplifier: VALID — H-MS gives the displayed bounds with distinct monic prime-power rows and an open zero-free disk.
VERDICT prop:ff-complete-row-ms: VALID — h+1≥deg lcm gives the exact threshold 2D−1 and the brute-force F7 table agrees.
VERDICT prop:ff-gauss-discriminant-absorption: VALID — all positive-degree Gauss and absorption identities through degree three agree exactly over F7.
VERDICT obs:graph-mobius-littlewood-fails: VALID — K4 refutes the polynomial-coefficient criterion and the logarithmic-derivative trace criterion is correct.
VERDICT prop:graph-flux-signed-ms: VALID — independent determinant enumeration reproduces 2048=10944−8896 and exact degree-13 cancellation.
VERDICT prop:graph-squarefree-flux-parity: VALID — rational-series counts reproduce 845/1701 and the fixed-flux parity exception is correct.
VERDICT prop:surface-sixfold-no-amplifier: VALID — multiplication by six creates duplicate trivial rows without an amplification gain.
VERDICT conj:ff-short-row-ms: UNVERIFIED — the conjecture is left to Q3 and is not established by complete-row identities.
VERDICT conj:surface-squarefree-local-limit: UNVERIFIED — the independent finite statistics reproduce but do not prove a uniform local limit.
VERDICT Q2-power-reciprocity: VALID — resultant interchange gives the stated sign and direct residue-field comparisons agree.
VERDICT Q2-finite-poisson: VALID — the subspace-annihilator identity has the correct normalization and implies no missing short-row estimate.
VERDICT Q2-exponent-comparison: VALID — the conditional scale function and its 6/7 minimum have the stated limited scope.

## Numerical checks for the blind lane

Run from `notes/astra-2026-10-25/review-qrh/`. All quoted exact checks are reproducible with plain `python3` and the installed libraries.

| independent command | number / certificate to recompute |
|---|---|
| `python3 checks/independent_scalars.py` | Liu: xi=0.3885833542660346667974279910648928174… and B=0.8749570194200989461286038505614529823…, with exact rational root enclosure. |
| `python3 checks/independent_scalars.py` | Q1's parentheses error: at delta=2/5,x=1/2, source E=−41/155760 but printed E=6709/207600; corrected O7 certificate residual is exactly zero. |
| `python3 checks/independent_ff.py` | q=7,D=2,h=0,1,2,3,4 gives S=24,1080,11844,86436,605052, respectively, by literal all-row enumeration. |
| `python3 checks/independent_ff.py` | 1715 exact positive-degree Gauss comparisons and 343 absorption comparisons pass; wrong Hasse–Davenport sign fails 840 times and wrong discriminant substitution 1008 times. |
| `python3 checks/independent_graphs.py` | K4,N=2,D=12: 2048=10944−8896; D=13: 0=30720−30720; D=16: 13520/27216=845/1701. |
| `python3 checks/independent_graphs.py` | Cube,D=12 normalized energies for Haar,N=2,3,4,5 are 1452,3512,1452,1452,1452; all coefficients and a mixed polynomial are tested. |

Saved results are `checks/output_independent_scalars.txt`, `checks/output_independent_ff.txt`, and `checks/output_independent_graphs.txt`. `checks/audit_replays.py` checks the archived/replayed outputs and source fingerprints. To regenerate the safe replays, run the three Q1 scripts and two Q2 scripts under `checks/replayed/`, redirecting their stdout to the correspondingly named `output_replay_*.txt` files if desired. The Q2 copies write their own files beside the copies. The Q1 record scanner has explicit repository/exclusion paths so moving it does not change the files it audits.

## What this changes in the notebook

The main Q1 and Q2 mathematical conclusions survive. The review adds a concrete correction to Q1's 7/8 exposition: **P_x=(2−8x/9)(1−x)**. Its own test program had silently used the correct polynomial. Remove the cube-exponent comma, and attach the missing CT manuscript/README before using its theorem numbers as locally checked provenance.

| candidate group | proposed disposition after this review |
|---|---|
| Q1-SAMPLE | PROVED candidate; exact N≥3 sampling, with N=2 counterexamples on both requested graphs. |
| `prop:ff-sextic-amplifier` | PROVED-conditional on H-MS, fixed q and nu; no unconditional short-row result is added. |
| `prop:ff-complete-row-ms`, `prop:ff-gauss-discriminant-absorption` | PROVED candidates with independent exact certificates; preserve h≥2D−1 and the resultant/sign conventions. |
| `obs:graph-mobius-littlewood-fails`, `prop:graph-flux-signed-ms` | Retain the refutation and corrected trace/orthogonality statements; the signed diagonal is not a lower bound. |
| `prop:graph-squarefree-flux-parity`, `prop:surface-sixfold-no-amplifier` | PROVED candidates with fixed-flux/parity qualifications; no claim uniform in growing N or against richer arithmetic constructions. |
| Seven `cit:` rows | Source-labelled citation proposals only; retain reported-formalisation and proof-audit caveats, with the CT locator repair. |
| Q1-THETA, Q1-EVAL, Q1-TRACE, `conj:ff-short-row-ms`, `conj:surface-squarefree-local-limit` | OPEN; the UNVERIFIED verdicts record the absence of a proof, not a negative result. |

The annotation decisions above are ready for the notebook owner, with explicit wording for the one-sided **new-spectrum** HPS/interlacing statement and the different N≥2/N≥3 averages. No registry or record page has been modified. The next review step is the required **second-family** check, particularly of the exact scalar correction and the scope of the source reports. Lane Q3 owns H-MS; this review supplies complete-row and Gauss-sign controls without duplicating that attack.
