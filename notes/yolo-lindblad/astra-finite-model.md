# Finite phase-side Lindbladian: constructive verification and zero hunt

The specified phase jumps pass the quotient and shell checks, but this finite construction does **not** produce the zeta zeros. Its vacuum resolvents can be computed exactly: the ordered-word answer is a prime-sum resolvent, and the multiset answer is a **shifted** partial zeta function. The proposed scalar coherence action, invariant parity block, and shell Gibbs fixed point each fail. These failures are tested directly below, including an exact rational counterexample to detailed balance.

## Reproduction and check tallies

From the repository root:

```bash
python3 notes/yolo-lindblad/finite/run_all.py
```

Every scientific entry script uses the fixed seed `20260914` through `finite_common.Checks`, asserts its checks, and prints a tally. Most calculations are deterministic; random shell pairs and coherence probes use that seed. The runner fixes BLAS thread counts and `PYTHONHASHSEED`, saves complete assertion logs as `finite/<script>.txt`, machine-readable results as `finite/<script>.json`, and regenerates this report from `finite/report_template.md` using `finite/render_report.py`. A failed check stops the run. These are assertions of the **corrected** statements and counterexamples, not claims that every draft statement passed.

| Script | Scope | Passed / failed |
| --- | --- | --- |
| [verify_phase.py](finite/verify_phase.py) | N1: direct quotient and shell checks | 93 / 0 |
| [verify_characters.py](finite/verify_characters.py) | N2: characters, coherence counterexample, BC transfer | 149 / 0 |
| [verify_ramanujan.py](finite/verify_ramanujan.py) | N3: exact Ramanujan and Gibbs identities | 576 / 0 |
| [hunt.py](finite/hunt.py) | N4: doubled model, truncation, pole/zero hunt | 357 / 0 |
| [spectrum.py](finite/spectrum.py) | N5: spectrum, parity leakage, Galois shifts | 87 / 0 |
| [balance.py](finite/balance.py) | N6: exact counterexample and stationary states | 89 / 0 |
| **Total** | Scientific assertions | **1351 / 0** |

Recorded environment: python `3.12.3`; numpy `1.26.4`; scipy `1.11.4`; sympy `1.14.0`; mpmath `1.3.0`.

Only `hunt.py` reads `data/zeros3000.npy`, **after** all operators, contour scans, and pole searches have been constructed and completed. The first six ordinates are comparison points only. No zero is a seed, coefficient, fitted parameter, or imposed eigenvalue. `mpmath.zeta` is used only for Gibbs normalization comparisons in `balance.py`. The BC comparison extracts the actual `transfer` function from `scripts/bcmpo.py` without running its demonstration code; prime cutoffs in this report are inclusive.

## Model as built

Use Brief A's Haar Fourier basis $e_r$, Ramanujan shells $|b\rangle=c_b/\sqrt{\phi(b)}$, $V_p$, $U_a$, $\Pi$, and $\Gamma_b=\Pi\otimes\bar\Pi$. For a finite divisor-closed set $\mathcal B$, let $P_B$ be its projection and write $V_{p,B}=P_BV_pP_B$. The matrix is

\[
V_{p,B}|b\rangle=
\begin{cases}
p^{-1/2}|b\rangle+\sqrt{(p-1)/p}\,|pb\rangle,&p\nmid b,\\
|pb\rangle,&p\mid b,
\end{cases}
\]

with the $|pb\rangle$ term deleted when $pb\notin\mathcal B$. Its adjoint is the transpose. The initial quotient verification uses rectangular maps between Haar $L^2(\mathbb Z/(N/p))$ and $L^2(\mathbb Z/N)$; it does not assume these shell formulas. Divisor models are used in the algebra and balance checks. The main hunt uses $\mathcal B=\{1,\ldots,B_{\max}\}$, reaching the sizes in the table below. The character verification uses every $b\mid120$.

Explicitly, the adjoint on the retained shells is

\[
V_{p,B}^\dagger|b\rangle=
\begin{cases}
p^{-1/2}|b\rangle,&p\nmid b,\\
\sqrt{\phi(b)/(p\phi(b/p))}\,|b/p\rangle,&p\mid b.
\end{cases}
\]

Set $A_p=V_{p,B}\otimes\bar V_{p,B}$, $\lambda_p=p^{-\beta}$, and $\Lambda_P=\sum_{p\le P}\lambda_p$. The requested objects are

\[
T=\sum_{p\le P}\lambda_p(A_p-I),\qquad
K(s)=\sum_{p\le P}\lambda_pp^{-s}A_p,\qquad
R(s)=(I-K(s))^{-1},\qquad
R_E(s)=\prod_{p\le P}(I-\lambda_pp^{-s}A_p)^{-1}.
\]

The continuous-time model has no archimedean lengths; the second model attaches $\log p$ through $p^{-s}$. Baseline $\beta=1$ and perturbations $\beta=1.05,1.2$ are tested. No harmonic oscillator or archimedean Hamiltonian is added. Doubled vectors use row-major vectorization of density matrices, so $A_p$ implements $\rho\mapsto V_{p,B}\rho V_{p,B}^\dagger$.

**Truncation is measurable and substantial.** Orthogonality of the columns gives

\[
I-V_{p,B}^\dagger V_{p,B}=\operatorname{diag}_{b\in\mathcal B}\delta_p(b),\quad
\delta_p(b)=
\begin{cases}
0,&pb\in\mathcal B,\\
1-1/p,&pb\notin\mathcal B,\ p\nmid b,\\
1,&pb\notin\mathcal B,\ p\mid b.
\end{cases}
\]

The table reports the maximum squared norm loss and its uniform-shell average, averaged over primes with weights $\lambda_p/\Lambda_P$. It is not an error bar claiming convergence in operator norm.

| P | Bmax = shell states | Doubled dimension | Max norm² loss | Rate-weighted mean loss |
| --- | --- | --- | --- | --- |
| 5 | 64 | 4096 | 1.0 | 0.481317 |
| 7 | 256 | 65536 | 1.0 | 0.512595 |
| 13 | 1024 | 1048576 | 1.0 | 0.553808 |
| 31 | 2048 | 4194304 | 1.0 | 0.604307 |
| 47 | 3072 | 9437184 | 1.0 | 0.624380 |

Consequently the semigroup generated by the requested finite $T$ is completely positive and trace **decreasing**, rather than trace preserving. For a finite CPTP comparison, `balance.py` instead uses the genuine dissipator

\[
\mathcal D[A](\rho)=A\rho A^\dagger-\tfrac12\{A^\dagger A,\rho\},\qquad
\mathcal L_{\rm db}=\sum_p\lambda_p\bigl(\mathcal D[V_{p,B}]+p^{-\beta}\mathcal D[V_{p,B}^\dagger]\bigr).
\]

The anticommutators are retained for **both** jumps. Even before truncation, $V_pV_p^\dagger\ne I$, so a reverse dissipator cannot be replaced by $\operatorname{Ad}(V_p^\dagger)-I$.

## N1 — quotient isometries, shells, and covariance

In normalized Euclidean coordinates for Haar $L^2$, the direct position-space map is the rectangular embedding $J[p y,y]=1$. In function values this is exactly $\sqrt p f(x/p)1_{p\mid x}$. Fourier conjugation gives $V_pe_r=p^{-1/2}\sum_{ps=r}e_s$, hence $V_p^\dagger e_r=p^{-1/2}e_{pr}$. The script tests complete Fourier matrices on compatible quotients, both shell directions using position-space transforms, every available finite unit $a$, and compositions between compatible quotient sizes. At primes coprime to a denominator the adjoint's frequency permutation is the Shor map **with** its $p^{-1/2}$ factor; it is not a finite unitary on that denominator space.

| Direct check | Maximum absolute error |
| --- | --- |
| isometry | 0.000e+00 |
| fourier | 1.460e-14 |
| shell forward | 2.223e-16 |
| shell adjoint | 2.229e-16 |
| covariance | 0.000e+00 |
| commute | 0.000e+00 |

**Verdict N1.** S1 and S2 pass in their properly normalized, compatible-quotient meaning. Finite shell compressions commute because multiplication only increases divisibility: once a path leaves a divisor-closed cutoff it cannot return. All shell and doubled commutators tested vanish to the stated tolerance. The compressed jumps cease to be isometries precisely by the diagonal deficit above; this is a boundary effect, not a failure of S2.

Every direct quotient error is below $10^{-12}$, and the hunt checks the saved successful quotient result before building its shell operators.

## N2 — Gauss vectors: the adjoint scalar does not make a Lindblad eigenmode

`verify_characters.py` explicitly builds all local unit-group characters, using cyclic groups at odd prime powers and the generators $-1,5$ at powers of two, and combines them by CRT. The complete collection over $b\mid120$ is an orthonormal Gauss basis. Write the normalized vector as $\widehat g_\chi=g_\chi/\sqrt{\phi(b)}$. Direct quotient calculations give

\[
U_a\widehat g_\chi=\chi(a)\widehat g_\chi,\qquad
V_p^\dagger\widehat g_\chi=p^{-1/2}\overline{\chi(p)}\widehat g_\chi\quad(p\nmid b).
\]

But $V_pe_0\notin\mathbb C e_0$. For $b>1$, the Hilbert–Schmidt projection of $T\rho_\chi$, $\rho_\chi=|e_0\rangle\langle\widehat g_\chi|$, back onto $\rho_\chi$ is

\[
\alpha_\chi=\langle\rho_\chi,T\rho_\chi\rangle_{\rm HS}
=\sum_{p\le P}p^{-\beta}\left(\frac{\overline{\chi(p)}}p-1\right),
\]

where Dirichlet characters are extended by zero at bad primes. A prime dividing $b$ contributes $-p^{-\beta}$: $V_p$ moves that exact denominator shell out of itself. `coherence_action` computes the **untruncated, finite-support** action and its orthogonal residual by Gram matrices. Thus its nonzero residual is not caused by a shell boundary.

For comparison, define the scalar drafted in S3, $a^{\rm draft}_\chi=-\sum_pp^{-\beta}(1-\bar\chi(p))$. With locally summed logarithms,

\[
\Delta_P(\beta,\chi)=\log\zeta_P(\beta)-\log L_P(\beta,\bar\chi)
=\sum_{p\le P}\sum_{k\ge1}\frac{1-\bar\chi(p)^k}{k p^{k\beta}}
=-a^{\rm draft}_\chi+C_{\ge2}.
\]

This includes bad primes and every prime-power term. The real part is branch independent. The code compares exact finite Euler logarithms with the power series through its documented, negligible tail. It also verifies the BC **units-block** eigenvalue

\[
\eta_\chi=\prod_{p\le P}\frac{1-p^{-\beta}}{1-\bar\chi(p)p^{-\beta}}
=\frac{L_P(\beta,\bar\chi)}{\zeta_P(\beta)}=e^{-\Delta_P}.
\]

The units block is a compression: primes dividing $b$ can send mass to nonunits. This BC transfer is a different operator from the phase-side Lindblad generator. For the character modulo $5$ defined by $\chi(2)=i$, and $P=47$:

| β | Re αχ | Im αχ | Orthogonal residual | Re aχ draft | Re ΔP | Re C≥2 |
| --- | --- | --- | --- | --- | --- | --- |
| 1.0 | -1.655706 | -0.155592 | 0.610719 | -1.601203 | 2.088651 | 0.487448 |
| 1.05 | -1.525228 | -0.151545 | 0.578067 | -1.477036 | 1.916577 | 0.439541 |
| 1.2 | -1.208334 | -0.139993 | 0.494751 | -1.174791 | 1.501638 | 0.326847 |
| 2.0 | -0.447757 | -0.090561 | 0.244921 | -0.442429 | 0.524524 | 0.082094 |

All 120 characters were included. Maximum errors: adjoint scalar `9.256e-16`, Galois diagonalization `1.602e-15`, BC units-block eigenvalue `5.551e-16`.

**Verdict N2.** S3's adjoint eigenvector identity is verified, including the conjugation convention. Its inference about Lindblad coherence eigenvectors is false: both the extra $1/p$ in the projected scalar and the nonzero orthogonal residual matter. The prime-power logarithm and BC transfer identities hold for their respective arithmetic operators; they do not supply the spectrum of $T$. At $\beta=1$, only the finite partial-product comparisons are asserted.

## N3 — exact Ramanujan identities and what they actually generate

`verify_ramanujan.py` reduces the Fourier sum modulo the cyclotomic polynomial in $\mathbb Q[x]$, independently checking

\[
c_b(n)=\sum_{d\mid(b,n)}d\mu(b/d),\qquad c_b(1)=\mu(b).
\]

For $\beta=2,3$, exact rational summation over independent geometric prime valuations, including their infinite tails, verifies

\[
\langle c_b\rangle_\beta
=\sum_{d\mid b}\mu(b/d)d^{1-\beta}
=b^{1-\beta}\prod_{p\mid b}(1-p^{\beta-1}).
\]

This is the **phase observable expectation** in the number Gibbs state, not a proposed diagonal density on the Ramanujan-shell basis. The critical limit is zero for $b>1$, and one for $b=1$. The Haar state on the phase algebra is represented by the vector $e_0$; calling it pure on $C(\widehat{\mathbb Z})$ would be wrong. The vector state is pure on the full $B(L^2)$, while its restriction to that commutative algebra is Haar integration, not point evaluation.

For the smooth series, let $n_P=\prod_{p\le P}p^{v_p(n)}$. The exact finite-prime identity is

\[
\sum_{\substack{b\ge1\\b\ P\text{-smooth}}}c_b(n)b^{-s}
=\frac{\sigma_{1-s}(n_P)}{\zeta_P(s)}.
\]

It is a **finite** exact sum for fixed $n,P$: $c_{p^k}(n)=0$ for $k>v_p(n)+1$. The script enumerates every remaining smooth $b$, at $s=2,3$, for $n\le30$ and $P=5,7,13,31$. At $P=31$, $n_P=n$ for every tested $n$. Replacing $n_P$ by $n$ for smaller $P$ would generally be false. This is a smooth infinite-exponent identity, not an assertion that an arbitrary finite divisor cutoff contains all nonzero terms.

| P | n | nP | s | Nonzero-support terms enumerated | Exact series value |
| --- | --- | --- | --- | --- | --- |
| 5 | 1 | 1 | 2 | 8 | 16/25 |
| 5 | 1 | 1 | 3 | 8 | 2821/3375 |
| 5 | 6 | 6 | 2 | 18 | 32/25 |
| 5 | 6 | 6 | 3 | 18 | 2821/2430 |
| 5 | 29 | 1 | 2 | 8 | 16/25 |
| 5 | 29 | 1 | 3 | 8 | 2821/3375 |

**Verdict N3.** The arithmetic content of S4 and the Ramanujan-series part of S5 pass exactly. They exhibit $1/\zeta$ in a generating function built from the evaluation $c_b(n)$. They do not identify that signed evaluation with a vacuum-to-shell coefficient of the prime-jump resolvent. N4 computes those coefficients directly and obtains a different answer.

## N4 — the hunt

Put $z=s+\beta+1$, $w_p=p^{-z}$, and $S_P(z)=\sum_{p\le P}p^{-z}$. Every $A_p$ is lower triangular in the shell-pair ordering. Its vacuum diagonal entry is $1/p$, so the vacuum row closes and

\[
\boxed{F(s)=\langle1,1|R(s)|1,1\rangle=\frac1{1-S_P(s+\beta+1)}},\qquad
\boxed{F_E(s)=\langle1,1|R_E(s)|1,1\rangle=\zeta_P(s+\beta+1)}.
\]

Commutation permits collecting ordered words by their prime multiplicities, but the resolvent retains their multinomial multiplicities. It does **not** turn their sum into a multiset Euler product. For the latter, $V_ne_0=n^{-1/2}\sum_{b\mid n}\sqrt{\phi(b)}|b\rangle$ gives, for reachable $b$,

\[
F_{E,b}(s)=\langle1,b|R_E(s)|1,1\rangle
=\sqrt{\phi(b)}b^{-z}\zeta_P(z).
\]

For ordered words write $J_b=\langle1,b|R(s)|1,1\rangle/\sqrt{\phi(b)}$. An exact recursion is

\[
\left(1-\sum_{p\nmid b}w_p\right)J_b
=1_{b=1}+\sum_{p\mid b}w_pJ_{b/p}.
\]

Both formulas are unchanged by enlarging a divisor-closed cutoff once it contains the target shell. Unreachable shells have identically zero overlap and are excluded from isolated-zero counts. The implementation validates these formulas against explicit sparse **doubled** resolvents and Euler-factor solves, then uses the exact row reduction at the largest sizes. It does not pretend to diagonalize a dense matrix of the largest doubled dimension.

Maximum doubled-solve/formula discrepancy: `2.225e-16` (`hunt.py`).

**Pole exclusion is analytic, not just a failed root search.** At a shell pair $(b,c)$, the diagonal of $K(s)$ is $\sum_{p\nmid bc}p^{-z}$. Throughout the requested rectangle, its absolute value is at most $S_P(\beta+1.3)<1$. Triangularity then excludes every pole of the full finite resolvent there. This remains uniform in $P$: for $\beta\ge1$, the elementary majorant $\sum_{n\ge2}n^{-2.3}\le2^{-2.3}+2^{-1.3}/1.3<1$ suffices. The scalar vacuum $F$ never has a zero. The Euler overlaps have no zeros anywhere and their individual factor poles lie at

\[
\Re s=-\beta-1,\qquad \Im s=\frac{2\pi k}{\log p},\quad k\in\mathbb Z.
\]

For ordered shell-overlap zeros, the code computes argument-principle windings on the full rectangle boundary at steps $0.04$ and $0.02$, and samples the interior on a $19\times401$ mesh. Targets are $b=1,2,4,6,12,30,210$ when present and reachable. It normalizes by the nonvanishing factor $\sqrt{\phi(b)}b^{-z}$ before winding. All windings are zero at both refinements, with small consecutive phase increments. This is floating-point evidence for the selected overlaps, not an interval-certified exclusion for every shell.

For $\beta=1$, the real ordered pole outside the search rectangle is found by bracketed root finding, without consulting zero data:

| P | Bmax | Ordered real pole | Euler factor pole Re s | Rectangle poles | Tested overlap zeros |
| --- | --- | --- | --- | --- | --- |
| 5 | 64 | -0.967187734 | -2.00 | 0 | 0 |
| 7 | 256 | -0.852661588 | -2.00 | 0 | 0 |
| 13 | 1024 | -0.761991340 | -2.00 | 0 | 0 |
| 31 | 2048 | -0.687557487 | -2.00 | 0 | 0 |
| 47 | 3072 | -0.666449308 | -2.00 | 0 | 0 |

The Euler pole column specifies the real part of every individual factor pole; the table does not claim to enumerate every complex ordered pole outside the rectangle. Increasing $\beta$ translates these poles left by the same increment:

| P | Bmax | β | Ordered real pole | Euler factor pole Re s |
| --- | --- | --- | --- | --- |
| 47 | 3072 | 1.0 | -0.666449308 | -2.00 |
| 47 | 3072 | 1.05 | -0.716449308 | -2.05 |
| 47 | 3072 | 1.2 | -0.866449308 | -2.20 |

At fixed $P=47$, independent sparse row solves for $B_{\max}=64,256,1024,3072$ also verify exact cutoff independence of the common targets. In particular, no pole moves toward $s=1$:

| P | F(1) | FE(1) |
| --- | --- | --- |
| 5 | 1.204873042 | 1.196384261 |
| 7 | 1.209120379 | 1.199882460 |
| 13 | 1.210886797 | 1.201331433 |
| 31 | 1.211629311 | 1.201939617 |
| 47 | 1.211712204 | 1.202007482 |

Only after completing the hunt, evaluate the outputs at the known zero locations. For $P=47,\beta=1$:

| n | γn (comparison only) | abs F | abs FE | abs(1 − SP) |
| --- | --- | --- | --- | --- |
| 1 | 14.134725142 | 0.799702750 | 0.789413764 | 1.250464626 |
| 2 | 21.022039639 | 0.884869838 | 0.874739646 | 1.130109715 |
| 3 | 25.010857580 | 0.943078015 | 0.934032640 | 1.060357663 |

The requested ratio is exactly

\[
\frac{F(s)}{1/\zeta_P(s)}=\frac{\zeta_P(s)}{1-S_P(s+\beta+1)}.
\]

Its modulus at the first comparison zero is:

| P | abs(F / (1/ζP)) at 1/2+iγ1 |
| --- | --- |
| 5 | 0.224367124 |
| 7 | 0.172073488 |
| 13 | 0.136845991 |
| 31 | 0.100185307 |
| 47 | 0.082032824 |

A decreasing value of this ratio is not extraction of a hidden reciprocal-zeta factor. It multiplies the regular constructed $F$ by a partial Euler product evaluated outside its half-plane of absolute convergence. Such products do not provide a justified approximation to analytically continued $\zeta(s)$ in this strip. Here the exact formulas, pole locations, and uniform pole bound are decisive. In the half-plane where the infinite products converge, the multiset vacuum limit is $\zeta(s+\beta+1)$; its meromorphic continuation has its pole at $s=-\beta$ and its zeta zeros at $s=\rho-\beta-1$, not at the requested coordinates. This statement about continuation must not be confused with convergence of finite-product poles or zeros there.

**Verdict N4.** A clean negative for the specified vacuum generating functions: neither $s=1$ nor the nontrivial zeta zeros appear as their poles, and no tested shell overlap develops a zero in the search rectangle. The shift by $\beta+1$ follows from the rate and the two vacuum amplitudes; it cannot be discarded. The Ramanujan $1/\zeta(s)$ identity belongs to a different boundary evaluation. Parity supplies no alteration of the $F,F_b$ defined in the question, since no parity trace is inserted in them.

## N5 — continuous-time spectrum and Galois dephasing

The grading does not commute with this $T$. `spectrum.py` explicitly computes $(I-P_{\rm odd})TP_{\rm odd}\ne0$; hence an invariant even–odd restriction is unavailable. It nevertheless computes the requested compression $P_{\rm odd}TP_{\rm odd}$ and labels it accordingly. Its two triangular diagonal blocks have eigenvalues

\[
\tau_b=-\Lambda_P+\sum_{\substack{p\le P\\p\nmid b}}p^{-\beta-1},\qquad b>1,
\]

each repeated for the two coherence orientations. The full finite doubled $T$ is also triangular, with eigenvalues $-\Lambda_P+\sum_{p\nmid bc}p^{-\beta-1}$. Thus both spectra are real by construction; imaginary parts are not being rounded away. Explicit dense eigensolves on a small doubled model independently check the formulas.

For the explicit `Bmax=30, P=5` test, the largest odd-to-even matrix element is `0.353553391`, the largest grading commutator entry is `0.707106781`, and the largest trace defect entry is `1.033333333`.

At $B_{\max}=3072,\beta=1$, the odd compression has the following ranges. `spectrum.json` also contains every row at $B_{\max}=64,256,1024$.

| P | β | Min Re τ | Max Re τ | Distinct real values | Max abs Im τ |
| --- | --- | --- | --- | --- | --- |
| 5 | 1.0 | -1.033333333 | -0.632222222 | 8 | 0 (exact) |
| 7 | 1.0 | -1.176190476 | -0.754671202 | 16 | 0 (exact) |
| 11 | 1.0 | -1.267099567 | -0.837315830 | 32 | 0 (exact) |
| 13 | 1.0 | -1.338105484 | -0.908321747 | 58 | 0 (exact) |
| 17 | 1.0 | -1.393468806 | -0.963685069 | 90 | 0 (exact) |
| 19 | 1.0 | -1.443330302 | -1.013546565 | 127 | 0 (exact) |
| 23 | 1.0 | -1.484918204 | -1.055134466 | 168 | 0 (exact) |
| 29 | 1.0 | -1.518211902 | -1.088428164 | 207 | 0 (exact) |
| 31 | 1.0 | -1.549429383 | -1.119645646 | 247 | 0 (exact) |
| 37 | 1.0 | -1.575725950 | -1.145942213 | 285 | 0 (exact) |
| 41 | 1.0 | -1.599521310 | -1.169737573 | 323 | 0 (exact) |
| 43 | 1.0 | -1.622236291 | -1.192452554 | 361 | 0 (exact) |
| 47 | 1.0 | -1.643060193 | -1.213276456 | 397 | 0 (exact) |

| P | β | Min Re τ | Max Re τ | Distinct real values | Max abs Im τ |
| --- | --- | --- | --- | --- | --- |
| 47 | 1.05 | -1.514511462 | -1.105101062 | 397 | 0 (exact) |
| 47 | 1.2 | -1.201827759 | -0.847060565 | 397 | 0 (exact) |

For the Galois test it would be vacuous to use only $G_B$, where all $U_a=I$. Instead, the script constructs the full Gauss basis of $L^2(\mathbb Z/120)$, including repeated occurrences of the same character at different denominator shells, and averages the actual $U_a$ over $a\in(\mathbb Z/120)^\times$. With total rate $\gamma$,

\[
\mathcal D_{\rm Gal}=\frac\gamma{|G|}\sum_{a\in G}\operatorname{Ad}(U_a)-\gamma I,
\qquad
\mathcal D_{\rm Gal}(|\chi\rangle\langle\chi'|)=
\begin{cases}0,&\chi=\chi',\\-\gamma|\chi\rangle\langle\chi'|,&\chi\ne\chi'.\end{cases}
\]

Character equality here means equality as characters of the **common** group, not equality of modulus labels. The phase compressions preserve these character sectors, so addition really translates each cross-character block's spectrum by $-\gamma$. It leaves the entire Galois-trivial doubled shell space untouched.

With `γ=0.125`, the maximum dephasing coefficient error is `5.561e-17`. The test includes 770 same-character and 13630 cross-character Gauss-basis coherences, and 16 trivial shell vectors. Maximum character-sector leakage of the compressed phase jumps is `4.036e-16`; seeded direct unitary-average checks agree with the coefficient calculation.

**Verdict N5.** The continuous-time construction supplies real decay parameters with a spread of real parts, not a vertical line of relaxation frequencies. More fundamentally, the chosen parity sector is not invariant. Uniform Galois dephasing is verified exactly in its proper character-block meaning, but cannot generate frequencies and cannot alter this Galois-trivial hunt. At $\beta=1$, the finite-cutoff statements also do not define an unrestricted infinite-prime generator: $\sum_p1/p$ diverges, so a domain or renormalization would need separate justification.

## N6 — detailed balance fails for the stated phase jumps

With forward rate $\lambda_p$ and reverse rate $\lambda_pp^{-\beta}$, the population rate ratio along $b\to pb$ is $p^{\beta}$. The same matrix-element magnitude occurs in both directions, including the special first edge. Thus the classical diagonal projection balances weights $b^{+\beta}$, not $b^{-\beta}$. Moreover, diagonal shell populations are not a closed quantum subsystem: the vacuum stay term creates coherences.

An exact counterexample already has $\mathcal B=\{1,2\}$, $p=2,\lambda_2=1/2,\beta=2$:

\[
V_{2,B}=\frac1{\sqrt2}\begin{pmatrix}1&0\\1&0\end{pmatrix},\qquad
\rho_{\rm Gibbs}=\operatorname{diag}(4/5,1/5),\qquad
\mathcal L_{\rm db}(\rho_{\rm Gibbs})=
\begin{pmatrix}-3/16&27/160\\27/160&3/16\end{pmatrix}\ne0.
\]

`balance.py` verifies this with SymPy rationals. Swapping the rate orientation, to upward $\lambda_pp^{-\beta}$ and downward $\lambda_p$, fixes the diagonal population equation but still creates an off-diagonal component. If the local vacuum and first-shell weights are $w_0,w_1=p^{-\beta}w_0$, that component is

\[
\lambda_p\frac{\sqrt{p-1}}p\,\frac{p^{-\beta}-1}{2}\,w_0\ne0.
\]

For $p=2$ and levels $k=0,\ldots,6$, the script solves the actual finite GKSL stationary density, checks its trace, positivity and residual, and measures the proposed Gibbs residual in Hilbert–Schmidt norm:

| β | Gibbs residual, stated rates | Gibbs residual, swapped rates | Actual vacuum population | Actual top population |
| --- | --- | --- | --- | --- |
| 2.0 | 0.305493967 | 0.099442961 | 0.000194331 | 0.750037366 |
| 1.2 | 0.190500426 | 0.056543956 | 0.004238029 | 0.566182103 |
| 1.05 | 0.164760457 | 0.047547732 | 0.007314065 | 0.519847851 |
| 1.01 | 0.157736654 | 0.045142800 | 0.008436478 | 0.506802587 |
| 1.001 | 0.156148708 | 0.044602208 | 0.008710324 | 0.503827913 |
| 1.0 | 0.155972109 | 0.044542159 | 0.008741259 | 0.503496503 |

The stationary state concentrates toward the upper boundary. A divisor model $B=2^3 3^2 5$ gives the same obstruction:

| B | Shell states | β | Proposed Gibbs residual | Actual vacuum | Actual top |
| --- | --- | --- | --- | --- | --- |
| 360 | 24 | 2.0 | 0.489990850 | 0.000005424 | 0.643620987 |
| 360 | 24 | 1.2 | 0.267873701 | 0.000381809 | 0.378111399 |
| 360 | 24 | 1.05 | 0.224386943 | 0.000797884 | 0.321475440 |
| 360 | 24 | 1.01 | 0.213048645 | 0.000966496 | 0.306454250 |
| 360 | 24 | 1.0 | 0.210236688 | 0.001013596 | 0.302713117 |

A constructive **different model** does have the proposed Gibbs fixed point: resolve each edge into its own jump $A_{p,b}=|pb\rangle\langle b|$, with rates $\lambda_pp^{-\beta}$ upward and $\lambda_p$ downward. Every edge then obeys $w_{pb}=p^{-\beta}w_b$, and its separate dissipator preserves diagonal densities. The code verifies $b^{-\beta}/Z_B$ is stationary under this repaired generator. With only finitely many primes on a contiguous cutoff, disconnected components can give additional stationary densities; uniqueness is not asserted.

At every fixed finite cutoff, $\beta\to1^+$ is regular, including for the actual phase-jump stationary density. Even with unbounded occupations and a **fixed finite prime set**, the number Gibbs partition $\prod_{p\le P}(1-p^{-\beta})^{-1}$ is finite at $\beta=1$. The divergent Gibbs normalization belongs to removing the prime/state cutoff: $\sum_b b^{-1}=\infty$. For the number-shell Gibbs family, at $B_{\max}=3072$:

| β | ZB(β) | Captured infinite Gibbs mass | Finite Gibbs vacuum weight |
| --- | --- | --- | --- |
| 2.0 | 1.644608599 | 0.999802139 | 0.608047411 |
| 1.2 | 4.588188150 | 0.820552715 | 0.217950957 |
| 1.05 | 7.194703125 | 0.349582506 | 0.138991141 |
| 1.01 | 8.294225835 | 0.082465654 | 0.120565803 |
| 1.0 | 8.607462511 | — | 0.116178258 |

The captured-mass column is $Z_B(\beta)/\zeta(\beta)$, for $\beta>1$; the dash at the endpoint denotes an unnormalizable infinite number Gibbs weight. These cutoff data concern that specified Gibbs family, not an identification of it with the phase generator's stationary density.

**Verdict N6.** The requested Gibbs stationarity claim is refuted, first by the direction of detailed balance and then by quantum coherence creation even after reversing that direction. Finite GKSL stationary densities exist and are computed, but they are different, boundary-sensitive states. Resolved edge jumps with corrected rates give a verified Gibbs construction; they change the model. The finite calculation does not construct an infinite critical stationary phase state or a boundary condition at infinity.

## Verdict on the guess

The prime-preimage isometries, Ramanujan shells, and Galois covariance are supported.
The arithmetic Ramanujan evaluation produces a reciprocal-zeta series, but the tested dynamical overlaps do not identify with it.
The ordered vacuum resolvent is $1/(1-S_P(s+\beta+1))$; the multiset one is $\zeta_P(s+\beta+1)$.
Their target-strip pole exclusion is exact for every finite cutoff, and uniform in the prime cutoff for these scalar outputs.
The tested shell overlaps show no target-strip zeros; this contour evidence is finite and numerical.
The scalar-coherence inference, invariant parity block, and proposed phase-shell Gibbs fixed point are refuted.
Galois dephasing supplies a uniform cross-character shift, with no frequencies and no effect on the trivial sector.
The proposed phase-only finite model supplies neither the pole at $1$ nor the critical-line relaxation modes.
An additional archimedean operator, different boundary functional, or justified infinite-domain construction remains undecided; none was inserted here.
