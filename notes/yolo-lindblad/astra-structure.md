# Brief A: audit of the phase-side Riemann Lindbladian

All mathematical assertions below belong to an explicitly labelled result. Definitions specify objects, not additional hypotheses about arithmetic spectra. `CORRECTED` includes a counterexample and a proved replacement; `PROVED-CONDITIONAL` explicitly lists its hypotheses. `OPEN` never supplies a premise for a proof. No operator is defined using zeta zeros, RH, or a Hilbert–Pólya operator.

Context read: the three requested portions of `HANDOFF.md`, its item 2 under “What was established” as requested in S3, and shards 03b, 04b, 04c. The reference in S6 was checked against Connes's original paper. No other research files were used. The reported Gram numbers are treated as supplied observations, not independently verified data.

**CORRECTED — overall verdict.** The proposed rates do not give a normal cutoff Lindbladian on the stated bond; finite-cutoff prime jumps also fail the specified grading. Their actual vacuum resolvent has a prime-sum denominator. An exact reciprocal-zeta matrix element exists for the inverse of a separately defined multiset sum, with the shifts in §5.3, but no identification with the guessed generator's spectrum follows.

**PROVED — finite verification only.** `python3 notes/yolo-lindblad/finite/structure_checks.py` passes 492 exact rational checks of the Fourier shell identities, bad-prime character examples, the failure of grading and shell Gibbs stationarity, and a conserved coherence observable. These checks use no zeta-zero data. The general proofs below do not depend on the checks.

## 0. Definitions, domains, and the status of the guess

Write \(\mathcal H=L^2(\widehat{\mathbb Z},dx)\), with Haar probability, \(v=e_0=|1\rangle\), \(P_0=|v\rangle\langle v|\), \(P_-=I-P_0\), and \(\Pi=P_0-P_-\). Identify the doubled bond with Hilbert–Schmidt operators by \(f\otimes\bar g\leftrightarrow|f\rangle\langle g|\); then \(\Gamma_b X=\Pi X\Pi\). A density means a positive trace-class operator of trace one. The Lindblad convention is the Schrödinger convention in the question. Throughout, \(\mathcal G\) denotes the Galois-fixed Hilbert subspace, and \(F\) a finite set of primes. Unless stated otherwise, rates are nonnegative and the Hamiltonian in phase-only calculations is zero.

### 0.1 CORRECTED — the displayed infinite-prime expression is not yet a Lindbladian

For a finite \(F\), set
\[
 J_p(X)=V_pXV_p^*,\quad \Lambda_F=\sum_{p\in F}\lambda_p,
 \qquad \mathcal L_F=\sum_{p\in F}\lambda_p(J_p-I).
\tag{0.1}
\]
This is a bounded, trace-preserving GKLS generator on trace class, and a bounded operator on Hilbert–Schmidt class. The same construction works for \(\sum_p\lambda_p<\infty\), because \(\|J_p\|=1\) in both norms and the generator series converges in operator norm. Its exponential is CPTP: expand it as a positive Poisson mixture of compositions of the channels \(J_p\); the coefficients sum to one. This also proves strong continuity.

At \(\lambda_p=1/p\), however, \(\sum R_p^*R_p=(\sum1/p)I\) has infinite quadratic form on every nonzero vector. There is no densely defined no-jump operator obtained from that displayed sum. This is more than a formal objection: in §5.5 we prove that the natural finite-prime semigroups, applied to \(P_0\), have **no trace-norm limit at any positive time**. Thus that cutoff prescription does not define a normal strongly continuous CPTP semigroup on the specified bond. Other limiting algebras or renormalizations require new definitions.

For completeness, \(\sum_p1/p=\infty\) follows without prime asymptotics. If it converged, \(\prod_p(1-1/p)^{-1}\) would be finite, since \(-\log(1-u)\leq 2u\) for \(0\leq u\leq1/2\). But every finite partial harmonic sum is bounded above by the Euler product over the primes appearing in it, a contradiction.

### 0.2 CORRECTED — the archimedean Hamiltonian needs a measure and a factor of \(i\)

On \(L^2(\mathbb R_+,dx)\), the unitary logarithmic transform
\[
 (Wf)(y)=e^{y/2}f(e^y)
\]
takes the closure of \(D=x\partial_x+\tfrac12\), initially on compactly supported smooth functions, to \(\partial_y\) with domain \(H^1(\mathbb R)\). Fourier transformation takes this to multiplication by \(i\xi\); hence \(D^*=-D\), and \(H=-iD\), rather than \(D\), is self-adjoint. Translation is
\[
 T_u=e^{-uD},\qquad (T_uf)(x)=e^{-u/2}f(e^{-u}x).
\]
On multiplicative Haar space \(L^2(\mathbb R_+,dx/x)\), the corresponding skew-adjoint generator is \(x\partial_x\), without \(1/2\), and \(T_uf(x)=f(e^{-u}x)\). Thus interpreting the drafted \(D\) literally as a Hamiltonian is false under either usual measure convention. For example, under the first convention it has imaginary Fourier multipliers, whereas a Hamiltonian must have real ones.

### 0.3 OPEN — the unspecified archimedean additions

A “Gamma-factor harmonic-oscillator ladder” does not specify its jump operators, rates, grading, domains, or a trace prescription. An oscillator heat trace and a Lindblad transfer trace are different objects. No theorem below identifies this unspecified addition with a Gamma factor. The cMPS parameter \(t\) and the auxiliary logarithmic coordinate must also be distinguished until an identification is actually constructed. Neither a Hamiltonian nor a trace-preserving ladder acting only on the archimedean tensor factor changes the phase marginal in (0.1); consequently such additions do not cure the phase cutoff obstruction proved below.

## 1. S1: prime isometries and the finite Shor map

### 1.1 PROVED — the isometry, adjoint, Fourier formulas, and covariance

Multiplication by \(p\) maps \(\widehat{\mathbb Z}\) bijectively onto \(p\widehat{\mathbb Z}\), a subgroup of Haar measure \(1/p\). Therefore
\[
 \|V_pf\|^2=p\int_{p\widehat{\mathbb Z}}|f(x/p)|^2dx=\|f\|^2,
 \qquad (V_p^*g)(y)=p^{-1/2}g(py).
\tag{1.1}
\]
The substitution proves the adjoint identity first for bounded functions, then for all \(L^2\) functions by density. In particular,
\[
 V_p^*e_r=p^{-1/2}e_{pr},\qquad
 V_pe_r=p^{-1/2}\sum_{ps=r}e_s.
\tag{1.2}
\]
To prove the second formula, its Fourier coefficient at \(s\) is
\(\langle e_s,V_pe_r\rangle=\langle V_p^*e_s,e_r\rangle=p^{-1/2}[ps=r]\).
Multiplication by \(p\) on \(\mathbb Q/\mathbb Z\) has a kernel of order \(p\), so there are exactly \(p\) preimages. Also
\[
 V_p^*V_p=I,\qquad V_pV_p^*=M_{1_{p\widehat{\mathbb Z}}}.
\tag{1.3}
\]
For a profinite unit \(a\), multiplication by \(a\) preserves Haar measure and \(p\widehat{\mathbb Z}\). Substitution into the definitions gives
\(V_pU_a=U_aV_p\). Taking adjoints, and replacing \(a\) by \(a^{-1}\), gives covariance of \(V_p^*\) as well. Locally, multiplication by \(p\) is a unit automorphism of \(\mathbb Z_\ell\) for \(\ell\ne p\), and raises the \(p\)-adic valuation by one at \(p\).

### 1.2 CORRECTED — “prime jump = Galois away from \(p\)” includes a compression and normalization

Let \(\mathcal H[b]=\operatorname{span}\{e_{a/b}:a\in\mathbb Z/b\}\). For \((p,b)=1\),
\[
 \sqrt p\,V_p^*|_{\mathcal H[b]}:e_r\longmapsto e_{pr}
\tag{1.4}
\]
is the unitary Shor permutation. It is the restriction of \(U_a\) for any profinite unit satisfying \(a\equiv p^{-1}\pmod b\). In contrast, \(V_p^*\) itself has norm \(p^{-1/2}\) there, and \(V_p\) does not preserve this finite-level subspace. Already \(V_pe_0\) has nonzero Fourier modes of denominator \(p\). Thus no finite quotient identifies the full \(V_p\) with a Galois unitary; only the normalized backward map on a level coprime to \(p\) does so.

## 2. S2: the Ramanujan shells and the specified grading

### 2.1 PROVED — \(\mathcal G\) and all the drafted shell formulas

The unit group acts transitively on the Fourier characters of each exact denominator \(b\): reduction \(\widehat{\mathbb Z}^{\times}\to(\mathbb Z/b)^{\times}\) is surjective, by choosing units in the finitely many relevant local factors. Consequently its fixed vectors have constant Fourier coefficients on each such orbit. Orthogonality of the Fourier basis gives
\[
 \mathcal G=\mathcal H^{\widehat{\mathbb Z}^{\times}}
 =\overline{\operatorname{span}}\{|b\rangle:b\geq1\},\qquad
 \langle b|c\rangle=\delta_{bc}.
\tag{2.1}
\]
Covariance in §1 makes \(\mathcal G\) reducing for both \(V_p\) and \(V_p^*\).

If \(p\nmid b\), the preimages under multiplication by \(p\) of the exact-denominator-\(b\) characters consist of every character of exact denominator \(b\) once and every character of exact denominator \(pb\) once. If \(p\mid b\), all preimages have exact denominator \(pb\), each once. Hence
\[
 V_pc_b=\begin{cases}(c_b+c_{pb})/\sqrt p,&p\nmid b,\\c_{pb}/\sqrt p,&p\mid b.\end{cases}
\]
Using \(\varphi(pb)=(p-1)\varphi(b)\) in the first case and \(p\varphi(b)\) in the second yields exactly
\[
 V_p|b\rangle=\begin{cases}
 p^{-1/2}|b\rangle+\sqrt{(p-1)/p}\,|pb\rangle,&p\nmid b,\\
 |pb\rangle,&p\mid b.
 \end{cases}
\tag{2.2}
\]
In the backward direction, multiplication by \(p\) permutes the units modulo \(b\) if \(p\nmid b\). If \(p\mid b\), reduction of units modulo \(b\) to units modulo \(b/p\) is surjective with all fibers of size \(\varphi(b)/\varphi(b/p)\). Thus
\[
 V_p^*|b\rangle=\begin{cases}
 p^{-1/2}|b\rangle,&p\nmid b,\\
 p^{-1/2}\sqrt{\varphi(b)/\varphi(b/p)}\,|b/p\rangle,&p\mid b.
 \end{cases}
\tag{2.3}
\]
In particular \(V_p|1\rangle=p^{-1/2}|1\rangle+\sqrt{(p-1)/p}|p\rangle\), so the vacuum is not invariant. The exceptional downward coefficient for \(p\parallel b\) is \(\sqrt{(p-1)/p}\); it is one for \(p^2\mid b\).

### 2.2 CORRECTED — Galois covariance does not preserve the drafted even–odd splitting

The trivial Galois representation occurs on **all of \(\mathcal G\)**, not just on \(\mathbb Cv\). Hence “even = Galois-trivial” would be a different grading from the fixed one in the brief.

For the fixed grading, \(V_p\) is neither even nor odd. More decisively, (2.2) gives
\[
 \mathcal L_{\{p\}}(P_0)=\lambda_p\left[
 -\frac{p-1}{p}|1\rangle\langle1|
 +\frac{p-1}{p}|p\rangle\langle p|
 +\frac{\sqrt{p-1}}p\bigl(|1\rangle\langle p|+|p\rangle\langle1|\bigr)
 \right].
\tag{2.4}
\]
The input is \(\Gamma_b\)-even but the last terms are odd. Therefore \([\mathcal L_{\{p\}},\Gamma_b]\ne0\). Distinct primes give distinct nonzero cross terms, so this failure persists for every nonempty finite positive-rate set. In particular a restriction of this generator to “the even–odd coherences” is not defined as an invariant operator. Archimedean-only terms cannot cancel (2.4).

## 3. S3: Gauss vectors, genuine dephasing, and the BC transfer

### 3.1 PROVED — exact normalization and the bad-prime formula

For a Dirichlet character \(\chi\) modulo \(b\), set
\[
 g_\chi=\sum_{a\in(\mathbb Z/b)^\times}\chi(a)e_{a/b},\qquad
 \widehat g_\chi=g_\chi/\sqrt{\varphi(b)}.
\]
All its summands are orthogonal of modulus-one coefficient, so \(\|g_\chi\|^2=\varphi(b)\), whether or not \(\chi\) is primitive. For \(p\nmid b\), substitute \(c=pa\) in (1.2):
\[
 V_p^*\widehat g_\chi=p^{-1/2}\overline{\chi(p)}\,\widehat g_\chi.
\tag{3.1}
\]
There is no additional Gauss-sum normalization. Directly, \(U_a\widehat g_\chi=\chi(a)\widehat g_\chi\).

For \(p\mid b\), put \(d=b/p\). Sum \(\chi\) over each fiber of \((\mathbb Z/b)^\times\to(\mathbb Z/d)^\times\). A nontrivial character on the kernel has sum zero, since multiplication by an element whose character value differs from one multiplies that sum without changing it. It follows that
\[
 V_p^*\widehat g_\chi=
 \begin{cases}
 0,&\chi\text{ does not descend to }(\mathbb Z/d)^\times,\\
 p^{-1/2}\sqrt{\varphi(b)/\varphi(d)}\,\widehat g_\eta,
 &\chi=\eta\circ\mathrm{red}_{b,d}.
 \end{cases}
\tag{3.2}
\]
This gives every bad-prime contribution explicitly; it is in general a change of denominator, not a scalar correction.

### 3.2 CORRECTED — an eigenvector of \(V_p^*\) is not a dephasing eigenoperator for \(\mathrm{Ad}(V_p)\)

The actual formula is
\[
 \mathcal L_{\{p\}}(|f\rangle\langle g|)
 =\lambda_p\bigl(|V_pf\rangle\langle V_pg|-|f\rangle\langle g|\bigr).
\tag{3.3}
\]
It involves \(V_pf,V_pg\), not their backward images. Take the nontrivial character modulo 3, \(g=e_{1/3}-e_{2/3}\), and \(p=2\). Then
\[
 V_2g=2^{-1/2}(e_{1/6}+e_{2/3}-e_{1/3}-e_{5/6}),\quad
 V_2v=2^{-1/2}(e_0+e_{1/2}).
\]
The recycling term of \(|v\rangle\langle g|\) has a nonzero
\(|e_{1/2}\rangle\langle e_{1/6}|\) coefficient, absent from the original operator. Thus the drafted scalar action is false. The same obstruction applies to cross-character coherences: covariance preserves isotypic blocks, which contain many denominators, and does not scalarize their multiplicity spaces.

One can calculate a **compression**, but must not mistake it for invariant evolution. Let \(P_b^{\rm ex}\) project onto exact denominator \(b\). For \(p\nmid b\),
\(P_b^{\rm ex}V_p\widehat g_\chi=p^{-1/2}\chi(p)\widehat g_\chi\); for \(p\mid b\) it is zero. Hence the one-dimensional Hilbert–Schmidt compression onto \(|\widehat g_{\chi'}\rangle\langle\widehat g_\chi|\) has coefficient
\[
 \sum_{p\nmid b}\lambda_p\left(p^{-1}\chi'(p)\overline{\chi(p)}-1\right)
 -\sum_{p\mid b}\lambda_p.
\tag{3.4}
\]
For \(|v\rangle\langle\widehat g_\chi|\), with \(\chi\) nontrivial, replace the character product by \(\bar\chi(p)\). Formula (3.4) follows by taking the matrix coefficient of (3.3); the missing directions are precisely the leakage. For rates \(p^{-\beta}\), its real part is
\(-\sum_p p^{-\beta}+\operatorname{Re}\sum_p\psi(p)p^{-(\beta+1)}\), with \(\psi=\chi'\bar\chi\) extended by zero at bad primes. This differs even from the proposed prime dephasing rate by the factor \(1/p\).

### 3.3 PROVED — the exact logarithmic identity, including prime powers and bad primes

Here \(\beta>1\), and \(\psi\) is any Dirichlet character modulo \(b\), extended by zero off the units. Define the absolutely convergent arithmetic scalar
\[
 A_\beta(\psi)=\sum_p\frac{\psi(p)-1}{p^\beta}.
\]
Unique factorization and absolute convergence give the Euler products for
\(\zeta(\beta)=\sum n^{-\beta}\) and \(L(\beta,\psi)=\sum\psi(n)n^{-\beta}\). Expanding \(-\log(1-z)=\sum_{k\geq1}z^k/k\), with the branch fixed by these convergent series, proves
\[
 A_\beta(\psi)=\log L(\beta,\psi)-\log\zeta(\beta)
 +\sum_p\sum_{k\geq2}\frac{1-\psi(p)^k}{k p^{k\beta}}.
\tag{3.5}
\]
Consequently
\[
 \operatorname{Re}A_\beta(\psi)
 =-\log\zeta(\beta)+\log|L(\beta,\psi)|
 +\sum_p\sum_{k\geq2}\frac{1-\operatorname{Re}\psi(p)^k}{k p^{k\beta}}.
\tag{3.6}
\]
Every \(p\mid b\) contributes \(-p^{-\beta}\) to \(A_\beta\); its contribution to the double sum is \(\sum_{k\geq2}p^{-k\beta}/k\). There are no omitted bad-prime terms. Absolute convergence of the double sum follows from comparison with \(\sum_{n\geq2}n^{-2\beta}/(1-n^{-\beta})\).

For actual Galois-unitary jumps, choose units \(a_p\equiv p\pmod b\) when \(p\nmid b\). Their action on the above cross-character coherence is \(\lambda_p(\psi(p)-1)\), so the good-prime part is genuine dephasing. When \(p\mid b\), such a unit does not exist. An arbitrary chosen unit \(a_p\) instead contributes \(\lambda_p(\chi'(a_p)\bar\chi(a_p)-1)\). The arithmetic zero convention at bad primes describes killing or leakage, not a unitary Galois jump. Thus (3.5) is not a formula for the original \(V_p\)-Lindbladian.

Also, asymmetric weights on character-diagonal unitary jumps can produce imaginary parts \(\sum\lambda_p\operatorname{Im}\psi(p)\). Symmetric weights under inversion, including a uniform full-group average, make the scalar real. The unconditional phrase “Galois jumps cannot produce frequencies” needs this symmetry qualification.

### 3.4 PROVED — the precise BC transfer eigenvalue and its relation to (3.5)

Define on \(\mathcal H[b]\) the finite-dimensional maps \(M_ne_{a/b}=e_{na/b}\). Their norms are bounded by \(\sqrt b\), so
\[
 B_{\beta,b}=\frac1{\zeta(\beta)}\sum_{n\geq1}n^{-\beta}M_n
\tag{3.7}
\]
converges in norm. Exact denominators can only decrease under \(M_n\). On the exact-denominator-\(b\) diagonal block, the induced map is the permutation when \((n,b)=1\), and zero otherwise. Denote these induced maps by \(K_n\); they obey \(K_mK_n=K_{mn}\). Equivalently this is the quotient by the sum of all proper-denominator spaces. On this block,
\[
 K_n\widehat g_\chi=\bar\chi(n)\widehat g_\chi,\qquad
 \frac1{\zeta(\beta)}\sum_n n^{-\beta}K_n\widehat g_\chi
 =\frac{L(\beta,\bar\chi)}{\zeta(\beta)}\widehat g_\chi.
\tag{3.8}
\]
This proves the transfer eigenvalue in HANDOFF item 2 with its normalization and its boundary convention. On the full finite phase transfer, the diagonal blocks supply eigenvalues, but the displayed Gauss vectors need not themselves be eigenvectors: for an imprimitive character bad primes can produce the lower-denominator terms of (3.2). For example modulo 6, the nontrivial character induced from modulo 3 gives \(M_2(e_{1/6}-e_{5/6})=e_{1/3}-e_{2/3}\ne0\). When \(\chi\) is primitive, every nonunit \(n\) kills its Gauss vector and (3.8) is a full eigenvector identity too.

The exact transfer logarithm is
\[
 \log\frac{L(\beta,\bar\chi)}{\zeta(\beta)}
 =\sum_p\sum_{k\geq1}\frac{\bar\chi(p)^k-1}{k p^{k\beta}}.
\tag{3.9}
\]
Thus it is the exponent of a **prime-power** compound-Poisson generator, with rates \(p^{-k\beta}/k\), on the killed finite residue block. Keeping only \(k=1\) gives (3.5), not (3.9). Alternatively each independent prime exponent has geometric law \((1-p^{-\beta})p^{-k\beta}\), and averaging its permutation produces the same product. Neither description uses the phase-isometry recycling map.

For nontrivial \(\chi\), sums \(\sum_{n\leq N}\chi(n)\) are bounded by \(b\), since a complete period sums to zero. Summation by parts bounds \(L(\beta,\chi)\) uniformly as \(\beta\downarrow1\). Since \(\zeta(\beta)\to\infty\), (3.8) tends to zero. The principal character modulo \(b>1\), in contrast, has ratio \(\prod_{p\mid b}(1-p^{-\beta})\to\varphi(b)/b\). This distinguishes character labels from the single even vacuum.

## 4. S4: the critical phase state

### 4.1 PROVED — the Ramanujan expectation formula and its limit

Partition the characters of the cyclic group of order \(m\) by exact denominator:
\[
 \sum_{d\mid m}c_d(x)=\sum_{a=0}^{m-1}e_{a/m}(x)=m\,1_{m\widehat{\mathbb Z}}(x).
\]
The last equality is the finite geometric sum. Inverting divisors gives
\[
 c_b(x)=\sum_{d\mid b}\mu(b/d)\,d\,1_{d\widehat{\mathbb Z}}(x).
\tag{4.1}
\]
Here the inversion follows directly from \(\sum_{d\mid m}\mu(d)=[m=1]\), whose prime-factor expansion is \(\prod_{p\mid m}(1-1)\) for \(m>1\). For integers \(n\geq1\), (4.1) yields
\[
 \frac1{\zeta(\beta)}\sum_{n\geq1}n^{-\beta}c_b(n)
 =\sum_{d\mid b}\mu(b/d)d^{1-\beta}
 =b^{1-\beta}\prod_{p\mid b}(1-p^{\beta-1}).
\tag{4.2}
\]
Indeed the multiples of \(d\) have weighted sum \(d^{-\beta}\zeta(\beta)\); the remaining sum is finite and factors prime by prime. Its limit is zero exactly when \(b>1\); it equals one for \(b=1\).

### 4.2 CORRECTED — Haar is a vector state, but is not a pure state of the phase algebra

Represent \(C(\widehat{\mathbb Z})\) by multiplication operators. Its Haar state is
\[
 \omega_{\rm Haar}(f)=\int f\,dx=\langle v,M_fv\rangle.
\tag{4.3}
\]
It is the restriction of the pure rank-one state \(P_0\) on \(B(\mathcal H)\), but is **not pure on \(C(\widehat{\mathbb Z})\)**. For example, the clopen set \(A=2\widehat{\mathbb Z}\) and its complement both have measure \(1/2\), and Haar is the nontrivial equal mixture of normalized Haar restricted to these two sets. These states differ on \(1_A\). Equivalently a pure state on this commutative algebra is point evaluation, whereas \(\omega(1_A)=1/2\ne\omega(1_A)^2\). Being represented by one GNS vector is not purity.

The convergence of the Gibbs phase states is genuinely weak-* convergence on the **whole** phase algebra, not just on Ramanujan sums. For a residue class modulo \(b\), write its positive elements as \(b(k+\theta)\), where \(0<\theta\leq1\). The difference
\(\sum_{k\geq0}(k+\theta)^{-\beta}-\zeta(\beta)\) stays bounded for \(1<\beta\leq2\): its tail is bounded by a constant times \(\sum_{k\geq1}k^{-\beta-1}\) by the mean value theorem. Its normalized mass therefore tends to \(b^{-1}\). Every locally constant function consequently converges to its Haar expectation. Such functions uniformly approximate continuous functions on the profinite compact space, and all states have norm one, which proves weak-* convergence. In this sense the critical BC phase restriction is Haar. It does not follow that \(P_0\) is stationary under the guessed dynamics; (2.4) disproves that.

## 5. S5: exactly where an Euler product does and does not occur

### 5.1 PROVED — the arithmetic Ramanujan series

For a fixed positive integer \(n\), (4.1) gives \(c_b(1)=\mu(b)\) and
\[
 \sum_{b\geq1}\frac{c_b(n)}{b^s}
 =\sum_{d\mid n}d^{1-s}\sum_{k\geq1}\frac{\mu(k)}{k^s}
 =\frac{\sigma_{1-s}(n)}{\zeta(s)},\qquad \operatorname{Re}s>1.
\tag{5.1}
\]
All interchanges are absolute: \(|c_b(n)|\leq\sum_{d\mid n}d\), and the outer divisor sum is finite. The reciprocal identity follows by multiplying the two absolutely convergent Dirichlet series and using \(\sum_{d\mid m}\mu(d)=[m=1]\). In particular this argument derives the reciprocal from divisibility, not from spectral data.

### 5.2 CORRECTED — shell values at 1 are not vacuum-to-shell jump overlaps

Define, for every integer \(n\geq1\),
\[
 (V_nf)(x)=\sqrt n\,f(x/n)1_{n\widehat{\mathbb Z}}(x).
\]
Substitution proves \(V_mV_n=V_{mn}=V_nV_m\). Formula (4.1) and finite Fourier inversion give
\[
 V_nv=\frac1{\sqrt n}\sum_{b\mid n}\sqrt{\varphi(b)}\,|b\rangle,
 \qquad \langle b|V_n|1\rangle
 =\sqrt{\frac{\varphi(b)}n}\,[b\mid n].
\tag{5.2}
\]
Thus every such overlap is nonnegative. For example \(c_p(1)=-1\), whereas \(\langle p|V_p|1\rangle=\sqrt{(p-1)/p}>0\). The exact overlap Dirichlet series is
\[
 \sum_{n\geq1}n^{-s}\langle b|V_n|1\rangle
 =\sqrt{\varphi(b)}\,b^{-(s+1/2)}\zeta(s+1/2),
 \qquad\operatorname{Re}s>1/2.
\tag{5.3}
\]
This has zeta in the **numerator**. For unweighted recycling maps \(J_n=\operatorname{Ad}(V_n)\), the analogous shell population is
\[
 \langle b|J_n(P_0)|b\rangle=\frac{\varphi(b)}n[b\mid n],\qquad
 \sum_n n^{-s}\langle b|J_n(P_0)|b\rangle
 =\varphi(b)b^{-s-1}\zeta(s+1).
\tag{5.4}
\]
These identities follow simply by writing \(n=bm\); their convergence domains are the domains of the scalar sums, independent of any operator-norm convergence assertion.

The exact inverse relation is instead
\[
 c_b=\sum_{d\mid b}\mu(b/d)\sqrt d\,V_dv.
\tag{5.5}
\]
It is Möbius inversion of (5.2), not an evolution equation. There is also a useful vector identity:
\[
 C(s):=\sum_b b^{-s}c_b
 =\frac1{\zeta(s)}\sum_d d^{1/2-s}V_dv,
 \qquad\operatorname{Re}s>1.
\tag{5.6}
\]
The left side converges in \(\mathcal H\), since its squared norm is
\(\sum_b\varphi(b)b^{-2\operatorname{Re}s}\leq\sum_b b^{1-2\operatorname{Re}s}<\infty\).
For the right-hand vector series, its shell coefficients converge to
\(\sqrt{\varphi(b)}b^{-s}\zeta(s)\). The absolute values of all partial-sum coefficients are bounded by
\(\sqrt{\varphi(b)}b^{-\operatorname{Re}s}\zeta(\operatorname{Re}s)\), a square-summable sequence. Dominated convergence in \(\ell^2\) proves the identity. In every individual shell coefficient of (5.6), the apparent denominator cancels.

Point evaluation at the integer \(n\) is not a bounded functional on \(L^2(\widehat{\mathbb Z})\). Already the functions \(\sqrt m\,1_{n+m\widehat{\mathbb Z}}\) have norm one and value \(\sqrt m\) at \(n\). Even on \(\mathcal G\), evaluation at 1 is unbounded: the normalized indicator of being a unit at every prime in \(F\) has norm one and value
\(\prod_{p\in F}(1-1/p)^{-1/2}\to\infty\). These are radial cylinder functions and hence belong to \(\mathcal G\). Therefore evaluating (5.6) at 1 cannot turn it into a bounded vacuum matrix element by continuity. Equation (5.1) is a separate, valid scalar arithmetic identity.

### 5.3 PROVED — an exact reciprocal-zeta operator matrix element, with its actual meaning

For \(\operatorname{Re}w>1\), define the **multiset operator sum** on \(\mathcal G\) (or on \(\mathcal H\)):
\[
 \mathcal A(w)=\sum_{n\geq1}n^{-w}V_n
 =\prod_p(I-p^{-w}V_p)^{-1}.
\tag{5.7}
\]
The sum and product converge in operator norm. Each finite product expands by geometric series, and the remaining norm errors are bounded by the tails of \(\sum n^{-\operatorname{Re}w}\). Absolute Dirichlet convolution proves
\[
 \mathcal A(w)^{-1}=\sum_{n\geq1}\mu(n)n^{-w}V_n
 =\prod_p(I-p^{-w}V_p).
\tag{5.8}
\]
Both product identities are inverses as bounded operators, since convolution gives exactly the coefficient \([n=1]\). Using \(\langle v,V_nv\rangle=n^{-1/2}\) yields
\[
 \boxed{\ \langle v,\mathcal A(w)^{-1}v\rangle=\frac1{\zeta(w+1/2)}\ },
 \qquad \langle v,\mathcal A(w)v\rangle=\zeta(w+1/2).
\tag{5.9}
\]
Equivalently, \(\langle v,\mathcal A(s-1/2)^{-1}v\rangle=1/\zeta(s)\) on the initial operator-norm domain \(\operatorname{Re}s>3/2\). This is an exact operator statement derived from the jumps. It is the matrix element of the inverse of a deliberately specified **sum over one copy of each integer**, not a resolvent or time Laplace transform of \(\mathcal L\).

The normalizations for the proposed rates are as follows. Products of the jump amplitudes obey \(R_{p_1}\cdots R_{p_m}=n^{-1/2}V_n\), apart from the archimedean translation by \(\log n\). Products of recycling maps carry weight \(n^{-1}\). Consequently the analogous multiset sum and its inverse have these vacuum matrix elements (initially in their domains of absolute operator-norm convergence):

| Multiset summand, with an additional length weight \(n^{-s}\) | Sum matrix element | Inverse-sum matrix element | Absolute operator-norm domain |
| --- | --- | --- | --- |
| \(V_n\), vector vacuum \(v\) | \(\zeta(s+1/2)\) | \(1/\zeta(s+1/2)\) | \(\operatorname{Re}s>1\) |
| \(n^{-1/2}V_n\), vector vacuum \(v\) | \(\zeta(s+1)\) | \(1/\zeta(s+1)\) | \(\operatorname{Re}s>1/2\) |
| \(n^{-1}J_n\), doubled vacuum \(P_0\) | \(\zeta(s+2)\) | \(1/\zeta(s+2)\) | \(\operatorname{Re}s>0\) |

For the third row use \(J_mJ_n=J_{mn}\), \(\|J_n\|_{\rm HS}=1\), and \(\langle P_0,J_nP_0\rangle_{\rm HS}=1/n\); the same absolute-convolution proof applies. Thus removing shifts to display \(1/\zeta(s)\) requires explicitly changing the length weights. It does not establish the desired spectral normalization. If the recorded length is \(2\log p\) rather than \(\log p\), replace \(s\) by \(2s\) in the length weights; no factor of two is implicit.

### 5.4 PROVED — the actual ordered-word and continuous-time formulas

For finite \(F\), put \(\lambda(n)=\prod_{p\in F}\lambda_p^{k_p}\) when \(n=\prod_{p\in F}p^{k_p}\), and \(\Omega(n)=\sum k_p\). Commutativity gives
\[
 e^{t\mathcal L_F}
 =e^{-\Lambda_Ft}\sum_{n\ F\text{-smooth}}
 \left(\prod_{p\in F}\frac{(t\lambda_p)^{k_p}}{k_p!}\right)J_n.
\tag{5.10}
\]
Indeed the exponential of the sum of commuting bounded maps is the product of their exponentials. Its coefficient of a multiset is a product of Poisson weights, not a product of geometric weights.

For comparison, if \(K_F(s)=\sum_{p\in F}\lambda_p p^{-s}J_p\) and \(|u|\sum\lambda_pp^{-\operatorname{Re}s}<1\), then
\[
 (I-uK_F(s))^{-1}
 =\sum_n u^{\Omega(n)}\frac{\Omega(n)!}{\prod_p k_p!}
 \lambda(n)n^{-s}J_n.
\tag{5.11}
\]
The factor \(\Omega(n)!/\prod k_p!\) counts words with the same product. For example \(pq\), \(p\ne q\), occurs twice in the length-two word sum but once in a multiset Euler product. This is already a finite counterexample to the proposed identification.

Here is an exact resolvent answer for a natural observable. Set
\[
 \mathcal L_F(s)=\sum_{p\in F}\lambda_p p^{-s}J_p-\Lambda_F I.
\]
This is the tilted generator for recording an additional classical length increment \(\log p\) at a jump and taking its Laplace transform. At \(s=0\) it is the actual Lindbladian. Since \(V_p^*v=p^{-1/2}v\), for every trace-class \(X\),
\[
 \langle v,J_p(X)v\rangle=p^{-1}\langle v,Xv\rangle.
\tag{5.12}
\]
It follows either term by term or by solving this scalar differential equation that
\[
 \langle v,e^{t\mathcal L_F(s)}(P_0)v\rangle
 =\exp\left[t\left(\sum_{p\in F}\lambda_pp^{-s-1}-\Lambda_F\right)\right].
\tag{5.13}
\]
Taking the time Laplace transform, in particular for
\(\operatorname{Re}(z+\Lambda_F)>\sum_{p\in F}\lambda_pp^{-\operatorname{Re}s}\), gives the actual resolvent matrix element
\[
 \boxed{\ \langle P_0,(z-\mathcal L_F(s))^{-1}P_0\rangle_{
 \rm HS}=
 \frac1{z+\Lambda_F-\sum_{p\in F}\lambda_pp^{-s-1}}\ }.
\tag{5.14}
\]
For \(\lambda_p=1/p\), its prime sum is \(\sum_{p\in F}p^{-s-2}\). This has a prime-sum denominator, not an Euler-product denominator. Similarly (5.11) has vacuum element
\(1/(1-u\sum_{p\in F}\lambda_pp^{-s-1})\).

For unitary translations on an unrestricted logarithmic auxiliary line, Fourier transformation of the center coordinate produces the weights \(p^{-i\xi}\); a real Laplace weight additionally requires a domain or the explicit classical record just defined. One must not apply a non-\(L^2\) exponential functional to that line without this qualification.

**CORRECTED — an additional spectral distinction from the reversible prime chain.** A single forward prime already has Hilbert–Schmidt spectrum
\[
 \operatorname{spec}\mathcal L_{\{p\}}
 =\{\lambda_p(z-1):|z|\leq1\}\quad(\lambda_p>0),
\]
not a real set of isolated modes. For an elementary proof, take the normalized radial annulus indicators \(h_k\) of (8.6), with all other local factors constant, and put \(F_k=|h_k\rangle\langle h_k|\). They are orthonormal in Hilbert–Schmidt norm and obey \(J_pF_k=F_{k+1}\), \(J_p^*F_0=0\), \(J_p^*F_{k+1}=F_k\). Their closed span is a reducing unilateral-shift subspace. For every \(|z|<1\), \(\sum_{k\geq0}z^kF_k\) is a nonzero eigenvector of \(J_p^*\) with eigenvalue \(z\), so \(\bar z-J_p\) has nondense range and is not invertible. Closure supplies the unit circle; conversely \(\|J_p\|=1\) and the Neumann series exclude spectrum outside the closed disk. Finally \(\mathcal L_{\{p\}}=\lambda_p(J_p-I)\) gives the displayed spectrum by direct affine rescaling of its resolvent. This does not contradict the real spectrum of a different, reversible occupation-chain generator in shard 04c.

### 5.5 CORRECTED — the critical cutoff dynamics escape every finite shell subspace

Let \(\rho_F(t)=e^{t\mathcal L_F}P_0\), with \(\lambda_p=1/p\). Formula (5.10) is the law of independent Poisson variables \(N_p\) of means \(t/p\), followed by the pure state \(V_nv\), \(n=\prod p^{N_p}\). For a fixed shell \(b\), once \(F\) includes its prime divisors, (5.2) gives
\[
 0\leq\langle b|\rho_F(t)|b\rangle
 =\varphi(b)\,\mathbb E\left[n^{-1}[b\mid n]\right]
 \leq\varphi(b)\exp\left[-t\sum_{p\in F,\ p\nmid b}\frac{1-1/p}{p}\right].
\tag{5.15}
\]
The bound uses \(p^{-N_p}[N_p\geq v_p(b)]\leq1\) for the finitely many primes dividing \(b\), and \(\mathbb E[p^{-N_p}]=\exp[(t/p)(p^{-1}-1)]\) for the others. The exponent tends to \(-\infty\) for every \(t>0\). Every fixed shell diagonal entry therefore tends to zero.

All \(\rho_F(t)\) are supported in \(\mathcal G\), positive, and of trace one. If they had a trace-norm limit, that limit would share these properties and have zero diagonal in the complete basis \(|b\rangle\); positivity and the trace formula would give trace zero, a contradiction. In particular the vacuum survival probability is exactly
\[
 \langle v,\rho_F(t)v\rangle
 =\exp\left[-t\sum_{p\in F}\frac{1-1/p}{p}\right]\longrightarrow0.
\tag{5.16}
\]
Partial trace is trace-norm continuous. Since translating the archimedean factor, or applying a trace-preserving archimedean dynamics, leaves precisely this phase marginal, the same obstruction applies to the proposed tensor-product jumps with those independent additions.

### 5.6 CORRECTED — the ring trace is not defined even by the finite-prime phase cutoff

On the infinite-dimensional doubled \(\mathcal G\), \(\mathcal L_F\) is bounded, so \(e^{t\mathcal L_F}\) has bounded inverse \(e^{-t\mathcal L_F}\). It cannot be compact: otherwise the product with that inverse would make the identity compact. In particular it is not trace class. Multiplication by the unitary \(\Gamma_b\) cannot change trace-class membership. Thus
\[
 \operatorname{Tr}[\Gamma_b e^{t\mathcal L_F}]
\]
is not an ordinary operator trace. A finite prime cutoff alone is not a finite bond cutoff. A subtraction, distributional trace, or other regularization needs its own definition and proof; parity supplies none. The absence of \([\mathcal L_F,\Gamma_b]=0\) is a separate obstruction to reading this as the difference of two invariant-sector heat traces.

### 5.7 PROVED — what restores the Euler product, and what it says about poles

The operation restoring the multiset weights is precisely replacement of the word sum or Poisson exponential by \(\prod_p(I-z_pV_p)^{-1}\), or by an occupation-space trace. Commutativity permits these constructions; it does **not** change the multiplicities in (5.10)–(5.11). The stay term in (2.2) determines overlap factors such as \(p^{-1/2}\); it does not divide by word multiplicities. A parity insertion changes a trace functional; it does not replace \(\Omega(n)!/\prod k_p!\) by one.

For an independent elementary construction, take one occupation coordinate \(k_p\in\mathbb N_0\) per prime with finite support. Unique factorization identifies its orthonormal basis with integers \(n\), and the energy \(\sum k_p\log p\) is \(\log n\). Its thermal trace is \(\sum n^{-s}=\zeta(s)\) for real \(s>1\). Taking instead only occupancies 0 and 1 and giving a configuration parity \((-1)^{\sum k_p}\) gives the absolutely convergent signed trace
\(\sum\mu(n)n^{-s}=\prod_p(1-p^{-s})=1/\zeta(s)\) for \(\operatorname{Re}s>1\). This is an exterior occupation-space parity. It is different from the fixed doubled-bond parity in this brief.

There is no inference from the zeros of the individual finite factors \(1-p^{-s}\) to the zeros of the analytically continued infinite product: those factor zeros have \(\operatorname{Re}s=0\), outside the half-plane of this product's convergence. In particular the shard's “all primes fermionic, zeros on \(\operatorname{Re}s=0\)” is correct for the individual factors and finite products, but is not a statement about the analytic zero or pole set of \(1/\zeta\).

For precision about analytic continuation, it can be constructed without any zero input. Let \(B_j(x)\) be the Bernoulli polynomials, defined by
\(te^{xt}/(e^t-1)=\sum_j B_j(x)t^j/j!\), and write \((s)_r=s(s+1)\cdots(s+r-1)\). Repeated integration by parts on the intervals between successive integers gives, initially for \(\operatorname{Re}s>1\),
\[
 \zeta(s)=\frac1{s-1}+\frac12+
 \sum_{r=1}^{M}\frac{B_{2r}(0)}{(2r)!}(s)_{2r-1}
 -\frac{(s)_{2M}}{(2M)!}
 \int_1^\infty B_{2M}(\{x\})x^{-s-2M}\,dx.
\tag{5.17}
\]
To check the summation step explicitly, integrating \((x-n-1/2)f'(x)\) on \([n,n+1]\) gives \((f(n)+f(n+1))/2-\int_n^{n+1}f\). Sum, take \(f(x)=x^{-s}\), and move that integral to obtain the first periodic-Bernoulli remainder. Then use \(B_j'=jB_{j-1}\) successively; the endpoint equalities \(B_j(1)=B_j(0)\) for \(j\ne1\), and \(B_{2r+1}(0)=0\) for \(r\geq1\), follow from the defining generating function and give exactly (5.17). The remainder is holomorphic for \(\operatorname{Re}s>1-2M\), since the periodic polynomial is bounded. Varying \(M\) gives a meromorphic continuation to the plane, with its only possible pole at 1. These continuations agree on overlaps by their equality on the initial half-plane.

For any meromorphic function, local factorization at a zero of order \(m\) writes it as \((s-s_0)^m h(s)\), \(h(s_0)\ne0\). Its reciprocal has a pole of order \(m\). Accordingly the scalar continuations in (5.1) and (5.9) have reciprocal-zeta poles, allowing numerator cancellations and the stated shifts. This is an implication about the continuation of a scalar function, not an assertion of a resolvent spectrum.

In fact (5.1) has **no numerator cancellations in \(0<\operatorname{Re}s<1\)**: for \(n=\prod p^{a_p}\), its numerator is \(\prod_p(1+p^{1-s}+\cdots+p^{a_p(1-s)})\), and a zero of a nonconstant geometric polynomial has its argument on the unit circle. Its numerator zeros therefore all have \(\operatorname{Re}s=1\). Thus inside the open critical strip the poles are exactly the zeros of zeta there, with their orders, without assuming any zero exists or where it lies inside the strip.

Globally, “poles exactly the nontrivial zeros” is false for these functions. For example putting \(s=-2\), \(M=2\) in (5.17) gives \(-1/3+1/2-1/6=0\), all the remaining terms having a zero rising-factorial factor. Thus \(\zeta(-2)=0\), whereas \(\sigma_3(n)>0\): (5.1) has a pole at \(-2\) too. Removing such poles requires an additional completion, not supplied by the prime jumps.

### 5.8 OPEN — the central identification that remains missing

There is presently **no defined ring norm of the full guess**, and no proof that a resolvent or a length Laplace transform of its invariant dynamics on \(\mathcal G\) has poles at the nontrivial zeta zeros. The finite-cutoff dynamics instead give the explicit prime-sum expression (5.14). Equations (5.8)–(5.9) supply an exact reciprocal-zeta matrix element of a different, fully specified operator family. Extending its scalar identity meromorphically does not extend that family in operator norm, establish a closed generator, or make its poles generator eigenvalues. These are the missing steps, not hidden consequences of commutation or parity.

## 6. S6: adeles, the rational quotient, and closing a ring

### 6.1 PROVED — rational scaling before and after the quotient

Normalize additive Haar measure on \(\mathbb A_{\mathbb Q}\) by Lebesgue measure at infinity and \(\operatorname{vol}(\mathbb Z_\ell)=1\) at finite primes. If \(q=\pm\prod_\ell\ell^{m_\ell}\in\mathbb Q^\times\), then
\[
 |q|_{\mathbb A}=|q|_\infty\prod_\ell|q|_\ell
 =\left(\prod_\ell\ell^{m_\ell}\right)
   \left(\prod_\ell\ell^{-m_\ell}\right)=1.
\tag{6.1}
\]
The change of variables in additive Haar measure therefore makes
\((W_qf)(x)=f(q^{-1}x)\) unitary on \(L^2(\mathbb A_{\mathbb Q})\). On the set-theoretic multiplicative quotient \(X=\mathbb A_{\mathbb Q}/\mathbb Q^\times\), \([qx]=[x]\) by definition. Thus rational scalings act identically on functions of classes whenever such functions are defined. This is not a construction of an ordinary quotient \(L^2\) space, and it does not say that the implementing elements of a crossed-product algebra become the identity. In particular \(V_p\) is a proper isometry of a compact finite-adele region, not the unitary \(W_p\) on all adeles.

### 6.2 CORRECTED — a parity closure is not a quotient by \(\mathbb Q^\times\)

For a finite bond and Kraus words \(A_w\), the closure changes each amplitude from \(\operatorname{Tr}A_w\) to \(\operatorname{Tr}(\Pi A_w)\). The doubled contraction is
\[
 \sum_w|\operatorname{Tr}(\Pi A_w)|^2
 =\operatorname{Tr}\left[(\Pi\otimes\bar\Pi)
                      \sum_w A_w\otimes\bar A_w\right].
\tag{6.2}
\]
The identity follows by expanding each trace in an orthonormal basis. Continuous-time formulas follow by the same convergent word expansion when the requisite trace exists. This is a change of boundary functional. There is no averaging or constraint imposing \(W_q=I\).

A finite counterexample isolates the issue. Represent \(q\in\mathbb Q^\times\) by
\(W_q=\operatorname{diag}(1,e^{i\theta v_p(q)})\) and let \(\Pi=\operatorname{diag}(1,-1)\). These commute, but the parity-closed norm of the one-letter word \(W_p\) is \(|1-e^{i\theta}|^2\), whereas that of the identity is zero. Thus parity closure does not identify the action of a rational prime with the identity even in a perfectly well-defined finite representation. Cyclic trace invariance under conjugation is a different property from quotienting left multiplication.

### 6.3 PROVED — the geometric prime periods require an actual adelic quotient

The idele class group \(C_{\mathbb Q}=\mathbb A_{\mathbb Q}^\times/\mathbb Q^\times\) acts on \(X\). Let \(x^{(p)}\) have component zero at \(p\) and component one at every other place. Its stabilizer is the image of the local multiplicative group \(\mathbb Q_p^\times\), embedded as ideles with all other components one. Indeed \(a x^{(p)}=q x^{(p)}\) forces \(a_v=q\) at every \(v\ne p\); dividing by the diagonal idele \(q\) leaves only the local \(p\)-component free. Conversely every such local idele fixes \(x^{(p)}\).

For \(\mathbb Q\), the norm kernel \(K\subset C_{\mathbb Q}\) is compact and is represented by finite units with positive real component one: divide an idele by a rational with its finitely many finite valuations, and absorb the real sign by \(-1\). Its remaining real component is its norm. After also quotienting the orbit by \(K\), its norm coordinate is therefore
\[
 \mathbb R_+/|\mathbb Q_p^\times|_p
 =\mathbb R_+/p^{\mathbb Z},
\tag{6.3}
\]
with logarithmic period \(\log p\). This calculation specifies the sense in which prime periods occur. It uses the adele-class orbit, its local stabilizer, and the compact norm-kernel quotient. Merely translating an auxiliary logarithmic line and inserting \(\Pi\) performs none of these operations. A pure real-coordinate flow on the unquotiented orbit should not be silently substituted for (6.3).

### 6.4 CORRECTED — precise scope of the Connes citation

**Verified source statement, not an invoked spectral premise:** Connes's 1998 preprint, published in 1999, proves a local cutoff trace formula in §V, Theorem 3, and a finite-set-of-places formula in §VII, Theorem 4. These use space and Fourier cutoffs and local principal-value terms. The introduction and §VIII distinguish the global trace-formula problem and its relation to RH; the paper does not provide an unconditional ordinary heat trace of the proposed Lindbladian. See [Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*](https://arxiv.org/pdf/math/9811068), especially PDF pp. 2–3, 22, 31, and §VIII.

No formula from that paper is being substituted into this construction. Equations (6.1)–(6.3) have independent elementary proofs above. For the guess, (2.4), (5.15), and §5.6's trace obstruction already prevent the claimed identification with a parity-closed normal transfer trace. No statement here rests on **UNVERIFIED-MEMORY**.

### 6.5 OPEN — the absent intertwiner and trace prescription

To identify a ring observable with the adelic orbit trace requires a specified quotient or correspondence, an intertwiner for the relevant actions, a test-function trace regularization, and equality of the resulting distributions with all local normalizations. None is provided by the guess. The geometric calculation of periods alone does not construct any of them.

## 7. S7: uniform dephasing and the required converse

### 7.1 PROVED — parity and finite-group dephasing

For \(R=\sqrt\gamma\Pi\), \(R^*R=\gamma I\). Its dissipator is exactly
\[
 \mathcal D_R(X)=\gamma(\Pi X\Pi-X)=\gamma(\Gamma_b-I)X.
\tag{7.1}
\]
It is zero on \(\Gamma_b\)-even operators and \(-2\gamma\) on odd operators. If a base generator preserves both sectors, adding (7.1) leaves its even restriction unchanged and subtracts \(2\gamma I\) from its odd restriction. If it does not preserve them, the addition is still (7.1), but there is no sector spectrum to shift. This is why the computation does not apply to the unmodified prime guess.

For a finite abelian group \(A\) with \(U_a|_{\mathcal H_\chi}=\chi(a)I\), jumps \(\sqrt{\gamma/|A|}U_a\) give, on \(X:\mathcal H_{\chi'}\to\mathcal H_\chi\),
\[
 \gamma\left(\frac1{|A|}\sum_{a\in A}\chi(a)\overline{\chi'(a)}-1\right)X
 =\gamma(\delta_{\chi\chi'}-1)X.
\tag{7.2}
\]
To verify orthogonality, multiply the sum of the nontrivial character \(\chi\bar\chi'\) by any group element where its value is not one; the sum is unchanged and must vanish. Multiplicities of each character are allowed. Thus a full group average at one time step removes cross-character blocks; its Poisson generator damps those blocks at rate \(\gamma\).

### 7.2 PROVED-CONDITIONAL — the forward spectral-line statement, with the necessary operator hypothesis

Hypotheses:

- **H-INV:** the chosen coherence Hilbert space is invariant and carries a closed generator \(T_{\rm odd}\).
- **H-SA:** \(T_{\rm odd}=B-2\gamma I\), where \(B\) is **skew-adjoint** on that Hilbert space, not merely formally skew-symmetric.

Then \(\operatorname{spec}T_{\rm odd}\subset-2\gamma+i\mathbb R\), and
\(\|e^{tT_{\rm odd}}x\|=e^{-2\gamma t}\|x\|\). Proof: \(-iB\) is self-adjoint, hence has real spectral measure and unitary exponentials. Translating its multiplication representation by \(-2\gamma\) gives both conclusions. In finite dimension this is the elementary unitary diagonalization of an anti-Hermitian matrix.

The skew-adjoint qualification cannot be deleted. On \(L^2(0,\infty)\), \(B=-\partial_x\) with domain \(H^1_0(0,\infty)\) is closed and skew-symmetric, but generates the right-shift isometries \(f(x)\mapsto1_{x\geq t}f(x-t)\). Its spectrum contains every \(\lambda\) with \(\operatorname{Re}\lambda<0\): the adjoint \(\partial_x\) has the nonzero eigenfunction \(e^{\bar\lambda x}\), so \(\lambda-B\) cannot have dense range. Thus formal anti-Hermiticity alone need not constrain the spectrum to a line.

This theorem contains no arithmetic spectral identification. Choosing \(2\gamma=1/4\) implements that rate in a grading-preserving model; it does not identify any frequencies with zeta zeros.

### 7.3 PROVED — the exact finite-dimensional metric converse

For a finite matrix \(T\), the following are equivalent:

1. \(T\) is diagonalizable and every eigenvalue has real part \(-2\gamma\).
2. There is a positive-definite matrix \(M\) such that, with \(B=T+2\gamma I\),
   \(B^*M+MB=0\).

Proof: in (1), write \(B=S\operatorname{diag}(i\omega_j)S^{-1}\), with real \(\omega_j\), and take \(M=(S^{-1})^*S^{-1}\). Substitution proves (2). Conversely \(M^{1/2}BM^{-1/2}\) is skew-Hermitian, hence unitarily diagonalizable with imaginary eigenvalues. The required metric need not be the original Hilbert–Schmidt metric. Changing it is also not a proof that a chosen generator is completely positive in a different physical representation.

A spectral line by itself is insufficient. The matrix
\[
 T=-2\gamma I+\begin{pmatrix}i\omega&1\\0&i\omega\end{pmatrix}
\tag{7.3}
\]
has that spectrum and a Jordan block. Its shifted exponential has a term linear in \(t\), impossible for an operator skew-Hermitian in any positive-definite metric.

### 7.4 PROVED-CONDITIONAL — an infinite-dimensional sufficient converse

Hypotheses:

- **H-RIESZ:** normalized eigenvectors \(u_j\) form a Riesz basis: for all finite scalar families,
  \(a\sum|c_j|^2\leq\|\sum c_ju_j\|^2\leq b\sum|c_j|^2\), with fixed \(0<a\leq b<\infty\).
- **H-FREQ:** their eigenvalues are \(-2\gamma+i\omega_j\), with \(\omega_j\in\mathbb R\).
- **H-DOM:** under the synthesis isomorphism \(S:\ell^2\to\mathcal H_{\rm odd}\), the generator is the maximal diagonal realization, with domain
  \(S\{c:\sum_j\omega_j^2|c_j|^2<\infty\}\).

Then \(M=(S^{-1})^*S^{-1}\) is bounded, positive, and boundedly invertible, and the shifted generator is skew-adjoint in its metric. Proof: the Riesz inequalities give boundedness and bounded invertibility of \(S\). The diagonal operator \(c_j\mapsto i\omega_jc_j\) is skew-adjoint on precisely the stated maximal domain, as is checked coordinatewise in its adjoint definition. Conjugation by \(S\) establishes the assertion. Equivalently \(M^{1/2}BM^{-1/2}\) is skew-adjoint in the original metric.

The properly general converse asks for a bounded and boundedly invertible positive \(M\) with this **domain-level skew-adjointness**; a formal equality of quadratic forms on eigenvectors is not enough. Continuous spectrum would require a spectral representation instead of H-RIESZ. Neither a list of eigenvalues nor algebraic diagonalizability supplies these uniform bounds or domains.

### 7.5 PROVED-CONDITIONAL — what the supplied Gram observation implies

**H-GRAM:** the quoted condition numbers 10 and 700 refer to Gram matrices of initial finite sets of the same normalized candidate eigenvectors, with meaningful numerical accuracy.

For a Riesz basis its Gram matrices have all eigenvalues in \([a,b]\), by applying the inequalities of H-RIESZ to finitely supported coefficients. Thus their condition numbers are uniformly bounded by \(b/a\). The quoted increase is evidence that uniform bounds need investigation, but two finite values do not prove divergence. If the Gram condition numbers diverge for these normalized vectors, they do not form a Riesz basis, and this candidate cannot be made an orthonormal eigenbasis by a bounded, boundedly invertible metric.

For each finite span, the synthesis condition number is the square root of the Gram condition number: approximately 3.16 versus 26.46 for the supplied values. The particular metric making these supplied vectors orthonormal has condition number equal to the Gram condition number. Other eigenvector scalings can change finite optimizations; they do not remove the requirement for uniform Riesz bounds on normalized eigenvectors. A growing finite Gram number concerns the Hilbert-space geometry that a trace or a spectral list cannot determine. No zero data have been imported into an operator here.

### 7.6 OPEN — the arithmetic forward implication is missing its premise

To obtain an RH implication one must first construct, independently of zeros, a grading-preserving generator and prove an arithmetic identification of its odd spectrum (or an appropriate determinant/trace identity), including multiplicities and possible cancellations. One must then verify H-SA in the intended metric, or prove the bounded metric converse with its hypotheses. S1–S6 do not establish the first step, and the supplied Gram observation does not establish the second.

## 8. S8: populations, reversibility, critical objects, and coherences

### 8.1 CORRECTED — shell populations are not a closed Markov chain for these jumps

For \(p\nmid b\), (2.2) sends a shell projector to
\[
 J_p(|b\rangle\langle b|)=\frac1p|b\rangle\langle b|
 +\frac{p-1}{p}|pb\rangle\langle pb|
 +\frac{\sqrt{p-1}}p\bigl(|b\rangle\langle pb|+|pb\rangle\langle b|\bigr).
\tag{8.1}
\]
Thus the shell-diagonal algebra of densities is not preserved. Pinching in the shell basis after every infinitesimal step defines a **different** classical evolution: its upward rate is \(\lambda_p(p-1)/p\) if \(p\nmid b\), and \(\lambda_p\) if \(p\mid b\). The first case has a jump outcome staying at \(b\) with probability \(1/p\). Even the pinched chain is not the stated constant-rate chain \(b\to pb\). Off-diagonal inputs can subsequently affect populations in the original quantum evolution, so recording only the initial diagonal derivatives does not close its equations.

### 8.2 PROVED — the well-defined forward phase dynamics have no stationary density

Assume finite nonempty \(F\), or \(\sum\lambda_p<\infty\), and choose a prime with \(\lambda_p>0\). Let \(E_{p,k}\) be multiplication by \(1_{v_p(x)=k}\), for \(k\geq0\). The set \(x_p=0\) has Haar measure zero, so \(\sum_{k\geq0}E_{p,k}=I\) strongly. Formula (1.1) gives
\[
 \mathcal L^*(E_{p,k})=\lambda_p(E_{p,k-1}-E_{p,k}),\qquad E_{p,-1}=0.
\tag{8.2}
\]
Indeed multiplication by any other prime leaves \(v_p\) unchanged; multiplication by \(p\) raises it by one. If \(\rho\) were a stationary density, its nonnegative probabilities \(a_k=\operatorname{Tr}(\rho E_{p,k})\) would satisfy \(a_0=0\) and then \(a_k=a_{k-1}=0\). Normality implies \(\sum a_k=1\), a contradiction. This proof works on \(\mathcal H\), on \(\mathcal G\), and with an additional tensor factor by partial trace.

It is a dynamical absence of a normal fixed point for forward jumps at **any** nonzero well-defined rates. It is not the same assertion as the absence of a trace-class Gibbs density for the different energy \(\log N\) at \(\beta=1\). At the exact drafted rates \(1/p\), one must first address §5.5; there is no normal cutoff semigroup whose stationary density could be tested.

### 8.3 CORRECTED — reverse rates and shell Gibbs weights

At one prime let the forward rate be \(u>0\), the reverse rate \(d>0\), and write
\(a=p^{-1/2}\), \(c=\sqrt{1-1/p}\). In the local shell basis \(|0\rangle=|1\rangle\), \(|k\rangle=|p^k\rangle\),
\[
 V|0\rangle=a|0\rangle+c|1\rangle,\qquad V|k\rangle=|k+1\rangle\ (k\geq1),
\]
\[
 VV^*|_{\{0,1\}}=\begin{pmatrix}a^2&ac\\ac&c^2\end{pmatrix},
 \qquad VV^*|_{\{2,3,\ldots\}}=I.
\tag{8.3}
\]
For the **pinched** birth–death chain, the edge \(0\leftrightarrow1\) has rates \(uc^2,dc^2\), and every later edge has rates \(u,d\). Detailed balance therefore requires the probability ratio \(q=u/d\) on every edge. Gibbs ratios \(q=p^{-\beta}\) require
\[
 \boxed{\ d=u p^\beta\ },
\tag{8.4}
\]
not \(u/p\). Choosing \(d=u/p\) gives \(q=p>1\), which has no summable stationary probability even at one prime.

Even with (8.4), the actual quantum generator does not fix the shell-diagonal geometric density. If \(\rho=\sum_k w_k|k\rangle\langle k|\), its \((0,1)\) derivative is
\[
 \langle0|\mathcal L\rho|1\rangle
 =ac\left(uw_0-\frac d2(w_0+w_1)\right).
\tag{8.5}
\]
The forward recycling gives \(uacw_0\); reverse recycling is diagonal; its anticommutator gives the remaining term in (8.5). For \(w_1=qw_0\), \(q=u/d<1\), this is \(acuw_0(q-1)/(2q)\ne0\). In particular for the global shell density
\(\zeta(\beta)^{-1}\sum_b b^{-\beta}|b\rangle\langle b|\), the \((1,p)\) entry has this nonzero value; no other prime contributes to that entry. This is an explicit counterexample for every \(\beta>1\) at any finite prime cutoff containing \(p\).

### 8.4 PROVED — the basis in which phase jumps really are occupation shifts

On the radial local space \(\mathcal G_p=L^2(\mathbb Z_p)^{\mathbb Z_p^\times}\), define normalized annulus indicators
\[
 h_{p,k}=\frac{1_{v_p(x)=k}}{\sqrt{(1-1/p)p^{-k}}},\qquad k\geq0.
\tag{8.6}
\]
The annuli partition the space up to a null set, so these are an orthonormal basis of the radial space. Direct substitution shows \(V_ph_{p,k}=h_{p,k+1}\). The local constant vector is instead
\[
 v_p=\sqrt{1-1/p}\sum_{k\geq0}p^{-k/2}h_{p,k}.
\tag{8.7}
\]
Thus the backward-eigenvector vacuum of the brief is a geometric superposition in the actual shift basis; it is not the occupation-zero vector.

Radial functions of finitely many local coordinates are dense in \(\mathcal G\). The Chinese remainder theorem gives \(c_{mn}=c_mc_n\) for \((m,n)=1\) (decompose the additive characters; the unit factors merely permute the summands). Therefore \(\mathcal G\) is the incomplete Hilbert tensor product of the local \(\mathcal G_p\) with reference vectors **\(v_p\)**. On this space \(V_p\) acts as the local shift (8.6): its multiplication by a unit at every other prime fixes radial functions. This explicit identification also proves that a tensor product using the references \(h_{p,0}\) is a different representation of these infinitely many shifts. The reference overlaps are \(\langle h_{p,0},v_p\rangle=\sqrt{1-1/p}\), whose product vanishes.

### 8.5 PROVED — the true one-prime reversible density

Let \(S h_k=h_{k+1}\), and let \(0<q=u/d<1\). Then
\[
 \sigma_p=(1-q)\sum_{k\geq0}q^k|h_{p,k}\rangle\langle h_{p,k}|
\tag{8.8}
\]
is the unique normal stationary density for \(u\mathcal D_S+d\mathcal D_{S^*}\). On diagonal entries this is the constant-rate birth–death chain with boundary equation \(dw_1=uw_0\) and interior equation \(uw_{k-1}+dw_{k+1}-(u+d)w_k=0\). Summability forces its geometric solution, normalized by \(1-q\); substitution proves stationarity.

Here is also a proof that no stationary coherences have been omitted. For an offset \(r\geq1\), write \(x_j=\langle h_j,\rho h_{j+r}\rangle\). The stationary equations are
\[
 ux_{j-1}+dx_{j+1}-(u+d)x_j=0\ (j\geq1),\qquad
 dx_1-(u+d/2)x_0=0.
\]
The interior characteristic roots are 1 and \(q\). A trace-class operator is compact, so \(x_j\to0\), leaving \(x_j=Cq^j\). The boundary equation becomes \(-dC/2=0\). All off-diagonals vanish; their conjugates cover the other half of the matrix. This proves uniqueness. For \(q\geq1\), the diagonal equations already rule out a stationary density.

This reversible state is diagonal in annuli, not in the Ramanujan shells. It is a state constructed from the prime isometry alone; it is not the shell Gibbs density falsified in (8.5).

### 8.6 PROVED — the critical reversible state on the radial local algebra, and why it is not normal on \(\mathcal G\)

Define the radial local algebra as the norm closure of the union of finite tensor products \(\bigotimes_{p\in F}B(\mathcal G_p)\), embedded with identities outside \(F\) and represented on \(\mathcal G\). At each prime take the two jumps with \(d_p=u_pp^\beta\), \(u_p>0\), and the state (8.8) with \(q_p=p^{-\beta}\). Finite products of the one-prime semigroups agree on overlaps. They are unital completely positive contractions in the Heisenberg picture, so they extend to this norm closure. Strong continuity follows first on each finite local algebra, then on its norm-dense union using the contraction bound. The product of the states (8.8) is stationary, since this is so on every finite local algebra. This construction does not require summability of all rates: a local observable is affected by only finitely many of these **radial** generators.

In particular \(\beta=1\), \(u_p=1/p\), \(d_p=1\) gives a precise corrected reversible local dynamics and stationary product state. Its valuation distribution is
\[
 \nu_1=\bigotimes_p\left((1-1/p)p^{-k}\right)_{k\geq0},
\tag{8.9}
\]
which is exactly the valuation distribution of Haar measure on \(\widehat{\mathbb Z}\). Thus on the radial multiplication algebra it agrees with the critical phase state. This is an algebraic stationary state, not a normal stationary density of the original infinite-prime guess on its specified Hilbert bond.

In fact the product state (8.8) has **no normal extension to \(B(\mathcal G)\) for any \(\beta>0\)**. To prove this explicitly, its expectation of the local reference-vector projection is, by (8.7),
\[
 a_p:=\langle v_p,\sigma_pv_p\rangle
 =\frac{(1-1/p)(1-q_p)}{1-q_p/p}\leq1-1/p.
\tag{8.10}
\]
For finite \(F\), let \(P_F\) be the projection onto arbitrary local vectors at the primes of \(F\) with the reference vector at every other prime. These projections increase strongly to \(I\). For any finite \(K\supset F\),
\[
 P_F\leq\prod_{p\in K\setminus F}|v_p\rangle\langle v_p|.
\]
A normal extension \(\rho\) of the product state would consequently obey
\(\operatorname{Tr}(\rho P_F)\leq\prod_{p\in K\setminus F}a_p\to0\).
But normality also gives \(\operatorname{Tr}(\rho P_F)\uparrow1\), a contradiction. This proof does not assert that every possible stationary extension has been classified; it establishes precisely the non-normality of the constructed product state.

The distinction from \(\ell^2(\mathbb N)\) is now explicit. That occupation representation uses references \(h_{p,0}\); the phase-Haar representation uses (8.7). An abstract bijection between two countable orthonormal bases does not intertwine these infinitely many prime shifts and their selected vacua.

### 8.7 PROVED-CONDITIONAL — the Gibbs density and critical weight in the occupation model of shard 04c

Hypotheses defining this comparison model:

- **H-OCC:** on \(\ell^2(\mathbb N)\), \(S_p|n\rangle=|pn\rangle\), with occupation vacuum \(|1\rangle\).
- **H-DB:** forward and reverse rates are \(u_p\) and \(d_p=u_pp^\beta\), respectively.
- **H-RATES:** \(\sum_pu_p(1+p^\beta)<\infty\), so the full GKLS series is bounded both on trace class and on bounded operators.

Let \(W_\beta=\operatorname{diag}(n^{-\beta})\) and \(F_p=S_pS_p^*\), the projection onto multiples of \(p\). Directly on basis vectors,
\[
 S_pW_\beta S_p^*=p^\beta W_\beta F_p,\quad
 S_p^*W_\beta S_p=p^{-\beta}W_\beta,\quad
 [F_p,W_\beta]=0.
\]
Inserting these into the forward and reverse dissipators gives \(\mathcal L_p(W_\beta)=0\) term by term. H-RATES allows summation in operator norm. For \(\beta>1\), its trace is \(\zeta(\beta)\), so \(W_\beta/\zeta(\beta)\) is a stationary density. For \(\beta=1\), it instead defines the normal faithful semifinite weight
\[
 \Phi_1(A)=\sum_{n\geq1}\frac1n\langle n|A|n\rangle,
 \qquad A\geq0,
\tag{8.11}
\]
with \(\Phi_1(I)=\infty\). Finite-rank cutoffs make it semifinite, and strict positivity of every coefficient makes it faithful.

This weight is invariant under the corresponding Heisenberg semigroup. One way to justify the infinite trace, without interchanging signed infinities, is to let \(W_{\beta,N}\uparrow W_\beta\) be its finite diagonal cutoffs. Normal positivity of the Schrödinger extension on bounded operators gives
\(e^{t\mathcal L}(W_{\beta,N})\uparrow W_\beta\), since \(e^{t\mathcal L}W_\beta=W_\beta\). For any positive \(A\), trace duality for the trace-class cutoffs followed by monotone convergence gives \(\Phi_\beta(e^{t\mathcal L^*}A)=\Phi_\beta(A)\). The weight is not a probability state and is in the occupation representation, not the phase shell density of S8.

There is also an independent KMS obstruction for the occupation energy \(H|n\rangle=(\log n)|n\rangle\). A normal \(\beta\)-KMS state for \(\alpha_t=\operatorname{Ad}(N^{it})\) is invariant, so its density is diagonal because these energies are distinct. Applying the KMS identity to the analytic matrix units \(E_{mn},E_{nm}\) gives \(m^\beta\rho_{mm}=n^\beta\rho_{nn}\). Hence its density must be a constant multiple of \(W_\beta\), which cannot be normalized at \(\beta=1\). This is a statement about the Hamiltonian KMS condition; stationarity for a GKLS generator alone is not a KMS condition.

### 8.8 PROVED — the completed occupation boundary and the meaning of “\(b\to\infty\)”

For every \(\beta>0\), the product of geometric distributions
\[
 \nu_\beta=\bigotimes_p (1-p^{-\beta})p^{-k\beta},\qquad k\in\mathbb N_0,
\tag{8.12}
\]
is a probability on \(\prod_p\mathbb N_0\). Consistent probabilities on cylinder sets define it by the usual countable product construction; each coordinate law is invariant for its birth–death chain, and hence every finite product law is invariant for the independent product dynamics. The probability that a coordinate is nonzero is \(p^{-\beta}\).

For \(\beta>1\), \(\sum_p p^{-\beta}<\infty\); the union bound on tail coordinates shows that almost surely only finitely many are nonzero. For \(0<\beta\leq1\), the sum diverges, and independence gives zero probability of all tail coordinates being zero: the relevant tail product of \(1-p^{-\beta}\) vanishes. Taking the countable union over finite initial prime sets shows that finite-support configurations have probability zero. In the former case unique factorization and the Euler product give the mass \(n^{-\beta}/\zeta(\beta)\) on each integer. At \(\beta=1\), (8.12) is (8.9), supported on configurations with infinitely many occupied primes, rather than on integer shells.

The product law is also the only possible stationary law for these independent coordinates with positive up and down rates. Here are details avoiding an independence assumption about a proposed stationary law. A finite set of coordinates has invariant full-support product probability \(m\) by detailed balance, and its time-\(t\) transition matrix \(P_t\), for \(t>0\), has strictly positive entries: any two configurations can be joined by finitely many allowed jumps in that interval. It is reversible with respect to \(m\), since uniformizing the bounded finite-coordinate generator preserves detailed balance in each power of its transition matrix. If \(\pi\) were another stationary probability, \(h=\pi/m\) would satisfy \(h=P_th\) by reversibility. Apply strict Jensen to the integrable strictly convex function \(\sqrt{1+h^2}\leq1+h\) and integrate with respect to \(m\). Stationarity of \(m\) forces equality in Jensen at every state, hence \(h\) is constant because all transition entries are positive. Its mean is one, so \(\pi=m\). Every finite marginal of an infinite stationary law must therefore be this product marginal; cylinder sets determine the full law. At \(\beta=1\) no stationary probability can consequently be supported on finite-support integer configurations.

This is a precise probability on a completed configuration space, different from the infinite measure \(\sum_n n^{-1}\delta_n\) on finite configurations. It is not an unspecified boundary condition at a single point called infinity. The unnormalized occupation weight, the completed product probability, and Haar on the phase algebra must not be conflated, even though some restricted formulas agree.

### 8.9 PROVED — forward dynamics also have singular stationary objects, but no distinguished critical Gibbs state

For a summable family of forward rates, the Heisenberg action on phase multipliers is
\(J_p^*(M_f)=M_{f(p\,\cdot)}\). This is the classical random multiplication process. The point state at \(x=0\) is stationary, since \(p0=0\). If every prime has positive rate, each prime exponent in the multiplication record tends to infinity almost surely as \(t\to\infty\); for any fixed modulus only finitely many primes are relevant. Thus the process tends to zero in the profinite topology, and every initial phase probability converges weak-* to \(\delta_0\). A stationary probability must therefore be \(\delta_0\). Its phase restriction is not Haar: \(\delta_0(c_b)=\varphi(b)\).

Stationary singular states on the larger bounded-operator algebra also exist for this regularized dynamics. Take the time averages of any normal initial state, regarded as states on \(B(\mathcal G)\). Weak-* compactness supplies cluster states. Translating an averaging interval by fixed time \(s\) changes its value on a norm-one observable by at most \(2s/T\), so each cluster state is stationary. By §8.2 none is normal. This is an existence proof of stationary boundary states, not uniqueness or a BC identification.

At the original nonsummable rates, the radial local forward semigroups can instead be constructed as in §8.6 without reverse jumps, but this changes the algebra on which continuity is asserted. Their boundary behavior requires that algebra to be specified; §5.5 forbids treating their states as the claimed normal finite-cutoff limit on the phase bond. No uniquely selected normal “critical KMS fixed point” follows.

### 8.10 CORRECTED — vacuum coherences leave the odd sector; their full information need not decay

For \(b>1\), the generator applied to \(X_b=|1\rangle\langle b|\) is (3.3). For \(p\nmid b\), its recycling part is explicitly
\[
 J_pX_b=a^2|1\rangle\langle b|+ac|1\rangle\langle pb|
       +ac|p\rangle\langle b|+c^2|p\rangle\langle pb|.
\tag{8.13}
\]
For \(p\mid b\), it is \(a|1\rangle\langle pb|+c|p\rangle\langle pb|\). These formulas prove that the coherence is neither an absorbing mode nor generally a scalar decay mode.

There is nevertheless a quantitative statement about its **projection back onto vacuum coherences**. For finite or summable rates, \(V_p\) maps \(v^\perp\) into itself because \(V_p^*v=p^{-1/2}v\). Using the word expansion,
\[
 P_0e^{t\mathcal L}(X_b)P_-
 =|v\rangle\left\langle
  \exp\!\left[t\left(\sum_p\lambda_pp^{-1/2}V_p-\Lambda I\right)\right]b
 \right|,
\tag{8.14}
\]
where \(|b\rangle\) is the vector inside the exponential. Taking the operator-norm bound for that exponential gives
\[
 \|P_0e^{t\mathcal L}(X_b)P_-\|_1
 \leq\exp\left[-t\sum_p\lambda_p(1-p^{-1/2})\right].
\tag{8.15}
\]
This is decay of a projected block, with transfer of information to other blocks.

In fact the **full operator cannot decay to zero in trace norm**. Every \(V_n\) is a fixed Heisenberg observable for the forward dynamics:
\[
 J_p^*(V_n)=V_p^*V_nV_p=V_p^*V_pV_n=V_n,
\tag{8.16}
\]
using commutativity of the isometries. Trace duality and \(\|V_b\|=1\) imply
\[
 \|e^{t\mathcal L}X_b\|_1
 \geq|\operatorname{Tr}(V_b e^{t\mathcal L}X_b)|
 =|\langle b|V_b|1\rangle|
 =\sqrt{\varphi(b)/b}>0.
\tag{8.17}
\]
Thus “vacuum coherences decay” is true in the projected sense (8.15), and false as a claim of full trace-norm decay for these jumps. Meanwhile (2.4) shows that the vacuum population immediately emits into other shells: it is not absorbing or stationary.

### 8.11 PROVED-CONDITIONAL — the contrast with the vacuum-decay model in shard 04c

**H-CONTRACTION:** let \(Z_t\) be any strongly continuous contraction semigroup on a Hilbert space \(\mathcal K\), with \(Z_t\to0\) strongly. No arithmetic definition is assumed. On \(\mathbb Cv\oplus\mathcal K\), set \(A_t=1\oplus Z_t\) and
\[
 \mathcal E_t(\rho)=A_t\rho A_t^*
 +\operatorname{Tr}[(I-Z_t^*Z_t)\rho_{--}]P_0.
\tag{8.18}
\]
Both terms are completely positive: the second is a positive functional followed by preparation of \(P_0\). Their traces add to \(\operatorname{Tr}\rho\). The semigroup identity follows from
\(I-Z_{t+s}^*Z_{t+s}=(I-Z_s^*Z_s)+Z_s^*(I-Z_t^*Z_t)Z_s\).
Strong continuity on trace class follows first on finite-rank operators and then by approximation and contractivity. Its vacuum is fixed, and its coherences obey
\(\mathcal E_t(|v\rangle\langle g|)=|v\rangle\langle Z_tg|\), which tend to zero in trace norm. If a density is stationary, its \(--\) block is \(Z_t\rho_{--}Z_t^*\), whose trace tends to zero by finite-rank approximation; positivity then also forces the cross blocks to vanish. Thus the only stationary density is \(P_0\).

This proves the absorbing-vacuum comparison without importing the zero-built model space of the shard. It has the opposite population direction and different fixed observables from (8.1) and (8.16). Substituting a semigroup already specified by zeta zeros would not solve the present brief and has not been done here.

## What the guess gets right, what it gets wrong, what to compute next

**PROVED.** The prime isometries, their Galois covariance, and the Ramanujan shell formulas are exact. Divisor inversion produces Möbius coefficients and a reciprocal-zeta scalar series. An inverse multiset operator sum has the exact vacuum matrix element (5.9). Parity jumps implement uniform dephasing on an already invariant odd sector. None of these constructions takes zeros as input.

**CORRECTED.** The proposed jumps do not preserve the fixed grading, make Gauss coherences scalar, preserve shell diagonality, or fix the vacuum. Their ordered records retain word or Poisson multiplicities despite commutation. At rates \(1/p\), the proposed cutoff evolution has no normal positive-time limit; even a finite prime set does not make the doubled phase heat operator trace class. Haar is a vector state but is mixed on the phase algebra. Neither a parity insertion nor an auxiliary translation implements the rational adelic quotient. Shell Gibbs weights are not stationary under the proposed forward and reverse quantum jumps. Full vacuum coherences retain nonzero conserved expectations even when their projected odd block decays.

**OPEN — concrete next computations.** First select the algebra and the limiting dynamics: a summable-rate phase model or the precisely defined radial local model of §8.6 is available. At a finite bond cutoff, explicitly record any changed isometry relations and test grading invariance, complete positivity, and the stationary density. Next compare the three actual generating functions—word resolvent, Poisson evolution, and multiset inverse—using (5.10)–(5.14) as exact controls; matching an arithmetic scalar after a changed functional must not be called a spectral realization. Finally, an adelic route needs its quotient, intertwiner, and regularized trace before one can ask for a metric making its odd generator skew-adjoint. The present guess supplies no such identification; importing an operator built from zeros would bypass the central problem.

## CORRECTION LEDGER

The rows enumerate the drafted assertions and their requested extensions; references point to the proofs or the exact missing hypotheses above.

| Drafted statement | Verdict | Exact replacement / reference |
| --- | --- | --- |
| S1: \(V_p\) is an isometry; the two Fourier formulas have coefficient \(p^{-1/2}\). | **PROVED** | (1.1)–(1.3). |
| S1: \(V_p\) commutes with every \(U_a\). | **PROVED** | §1.1; adjoints commute too. |
| S1: multiplication by \(p\) is a unit away from \(p\) and a valuation shift at \(p\). | **PROVED** | §1.1. |
| S1: on a coprime finite quotient \(V_p^*\) is the Shor map / prime jump equals Galois. | **CORRECTED** | \(\sqrt p V_p^*\), restricted to that level, is the unitary permutation; \(V_p\) leaves the level, §1.2. |
| S2: Galois-fixed sector is the closed span of the normalized Ramanujan shells. | **PROVED** | (2.1). |
| S2: this sector reduces every forward and backward prime jump. | **PROVED** | Covariance, §2.1. |
| S2: both cases of the forward shell formula. | **PROVED** | (2.2), including \(p\nmid b\). |
| S2: both cases of the backward shell formula. | **PROVED** | (2.3), including \(p\parallel b\) versus \(p^2\mid b\). |
| S2: the vacuum is not invariant. | **PROVED** | (2.2) and (2.4). |
| Grading convention's implicit identification of the even line with the trivial Galois sector. | **CORRECTED** | The trivial sector is all of \(\mathcal G\); the fixed grading is not preserved, §2.2. |
| S3: good-prime backward eigenvalue of a Gauss vector. | **PROVED** | (3.1); norm is exactly \(\sqrt{\varphi(b)}\). |
| S3: bad primes contribute only a scalar adjustment to this action. | **CORRECTED** | Exact fiber sum (3.2): zero or a lower-denominator Gauss vector. |
| S3: the specified prime Lindbladian acts scalarly on vacuum/Gauss or Gauss/Gauss coherences. | **CORRECTED** | Explicit modulo-3, prime-2 counterexample, §3.2. |
| S3: the scalar real part for these jumps is the proposed character prime sum. | **CORRECTED** | No invariant scalar; even its one-dimensional compression is (3.4), with an extra \(1/p\). |
| S3: the corresponding arithmetic prime sum is a log-zeta/log-L difference up to prime powers. | **PROVED** | Exact complex and real identities (3.5)–(3.6); bad primes included. |
| S3: this prime-sum identity describes unitary Galois dephasing. | **CORRECTED** | Good primes do; zero values at bad primes describe killing, not unitaries, §3.3. |
| Context claim: character-diagonal unitary jumps can never supply imaginary frequencies. | **CORRECTED** | Real scalars require inversion-symmetric weights, §3.3. |
| S3: BC transfer eigenvalue \(L(\beta,\bar\chi)/\zeta(\beta)\). | **PROVED** | Exact finite-level quotient/block formulation (3.7)–(3.8); primitive vectors also satisfy the full identity. |
| S3: relation between that transfer and a prime-only generator. | **CORRECTED** | Its exact logarithm includes all prime powers with rates \(p^{-k\beta}/k\), (3.9). |
| S4: the three formulas for \(\langle c_b\rangle_\beta\), and vanishing iff \(b>1\). | **PROVED** | (4.1)–(4.2). |
| S4: the critical phase state is the pure vector state of \(e_0\) on \(C(\widehat{\mathbb Z})\). | **CORRECTED** | Haar is represented by \(e_0\), but is not pure on that algebra; weak-* convergence proved in §4.2. |
| S5: \(c_b(1)=\mu(b)\) and the Ramanujan Dirichlet series is \(\sigma_{1-s}(n)/\zeta(s)\). | **PROVED** | (5.1), absolute for \(\operatorname{Re}s>1\). |
| S5: these values are the vacuum-to-shell jump overlaps. | **CORRECTED** | Positive divisor overlaps (5.2), with zeta in the numerator in (5.3)–(5.4). |
| S5: an exact operator expression derived from the prime jumps can contain reciprocal zeta. | **PROVED** | Inverse multiset sum (5.7)–(5.9), with all rate/length shifts tabulated. |
| S5: that expression is a resolvent or length Laplace transform of the proposed Lindbladian. | **CORRECTED** | Actual finite-cutoff resolvent is (5.14); word multiplicities are (5.11). |
| Context identification of forward phase-prime dynamics with the real-spectrum reversible prime chain. | **CORRECTED** | A single forward phase prime has the full spectral disk described in §5.4. |
| S5: commuting jumps already restore one-copy-per-multiset Euler weights. | **CORRECTED** | \(pq\) occurs twice as an ordered two-letter word; (5.10)–(5.11). |
| S5: the shell stay term or parity closure restores Euler weights. | **CORRECTED** | Neither changes word multiplicities; the multiset product or occupation trace does, §5.7. |
| S5: scalar reciprocal-zeta poles are exactly nontrivial zeros everywhere. | **CORRECTED** | Locally they are reciprocal zeros with shifts/cancellations; (5.1) has no cancellation inside the strip but also a pole at \(-2\), §5.7. |
| Context claim: all-prime fermionic product has its analytic zeros only on \(\operatorname{Re}s=0\). | **CORRECTED** | True of finite local factors, not a conclusion about the continued infinite product, §5.7. |
| S5: a generating function of the full guessed generator has exactly the desired nontrivial-zero poles as operator spectrum. | **OPEN** | No full normal generator, defined trace, or operator continuation/intertwiner; §5.8. |
| S6: rational multiplication is unitary on additive adelic \(L^2\) by the product formula. | **PROVED** | (6.1). |
| S6: it becomes identity on \(\mathbb A_{\mathbb Q}/\mathbb Q^\times\). | **PROVED** | On classes and class functions, with the algebraic qualifications of §6.1. |
| S6: parity closing performs or imposes that rational quotient. | **CORRECTED** | Two-dimensional counterexample, §6.2. |
| S6: prime periods can be described in the adele-class action. | **PROVED** | Stabilizer and norm-kernel quotient yield \(\mathbb R_+/p^{\mathbb Z}\), §6.3. |
| S6: Connes's 1999 work identifies this guessed ring norm with an unconditional ordinary periodic-orbit trace. | **CORRECTED** | Verified source scope in §6.4; no such identification is supplied. |
| S6: construct the ring/adelic trace identification. | **OPEN** | Quotient, intertwiner, test-function regularization, and trace equality missing, §6.5. |
| S7: \(T_0-2\gamma\) with anti-Hermitian \(T_0\) has spectrum on one vertical line. | **PROVED-CONDITIONAL** | H-INV and H-SA: skew-adjointness, not only formal skew-symmetry, §7.2. |
| S7: a parity jump realizes exactly \(-2\gamma\) on odd coherences. | **PROVED** | (7.1); an existing invariant-sector spectrum is shifted only when that sector is preserved. |
| S7: uniform finite-abelian-group jumps realize character dephasing. | **PROVED** | (7.2). |
| S7: a spectral line alone conversely supplies anti-Hermiticity. | **CORRECTED** | Finite dimension requires diagonalizability and allows a changed positive metric; Jordan counterexample (7.3). |
| S7: sufficient infinite-dimensional metric converse. | **PROVED-CONDITIONAL** | H-RIESZ, H-FREQ, H-DOM, §7.4. |
| S7: significance of the recorded Gram growth 10 to 700. | **PROVED-CONDITIONAL** | H-GRAM; it motivates a uniform-bound test, while only unbounded growth disproves the candidate Riesz property, §7.5. |
| S7: apply uniform dephasing to obtain the requested arithmetic spectral conclusion. | **OPEN** | Independent arithmetic identification and metric/domain estimates absent, §7.6. |
| S8: forward shell populations are a closed chain \(b\to pb\). | **CORRECTED** | Coherences appear in (8.1); the pinched chain has a bottom-edge factor \((p-1)/p\). |
| S8: the stated forward dynamics have no normal stationary density. | **CORRECTED** | Proved for finite or summable rates in §8.2; the original \(1/p\) cutoff fails to define that dynamics in §5.5. |
| S8: no normal occupation-energy KMS state at \(\beta=1\). | **PROVED** | KMS matrix-unit ratios force nonnormalizable \(W_1\), §8.7. This does not define stationarity of the guess. |
| S8: reverse rates of the proposed smaller size restore detailed balance. | **CORRECTED** | Required ratio is \(d_p/u_p=p^\beta\), (8.4). |
| S8: shell-diagonal Gibbs weights are stationary under \(V_p,V_p^*\). | **CORRECTED** | Explicit nonzero off-diagonal derivative (8.5). |
| S8: a reversible phase object can be constructed from these isometries. | **PROVED** | Annulus shifts and their local stationary density, §§8.4–8.5. |
| S8: the corrected critical reversible object is a normal phase-bond density. | **CORRECTED** | Stationary radial product state exists, but has no normal extension to \(B(\mathcal G)\), §8.6. |
| S8: Gibbs occupation weights are stationary for the prime chain of 04c. | **PROVED-CONDITIONAL** | H-OCC, H-DB, H-RATES; density above criticality and invariant semifinite weight at criticality, §8.7. |
| S8: specify a critical occupation boundary probability. | **PROVED** | Completed product (8.12), with infinitely many occupied primes at \(\beta=1\); it is not a probability on integer shells. |
| S8: forward dynamics select the critical Haar state as an absorbing state. | **CORRECTED** | Regularized full phase multiplication tends to \(\delta_0\), and no normal quantum fixed point exists, §§8.2, 8.9. |
| S8: vacuum coherences are scalar decays or absorbing. | **CORRECTED** | They leak out of the odd block, obey the projected bound (8.15), and retain the full-norm lower bound (8.17). |
| S8: comparison with absorbing-vacuum Lindbladian of 04c. | **PROVED-CONDITIONAL** | H-CONTRACTION yields (8.18), a fixed vacuum and true coherence decay; no zero-defined semigroup is assumed. |
| Overall guess: \(\sum_p(1/p)\mathcal D_{V_p\otimes T_{\log p}}\) is an already defined normal Lindbladian. | **CORRECTED** | Infinite no-jump quadratic form and no positive-time trace-norm cutoff limit, §§0.1, 5.5. |
| Overall guess: a finite prime cutoff makes its phase ring supertrace an ordinary trace. | **CORRECTED** | Bounded exponential is invertible and noncompact on the infinite doubled bond, §5.6. |
| Overall guess: \(D=x\partial_x+1/2\) is the specified archimedean Hamiltonian. | **CORRECTED** | Fix the measure and take the self-adjoint \(-iD\), or its Haar-measure variant, §0.2. |
| Overall guess: the unspecified oscillator ladder supplies the completed Gamma factor and resolves these problems. | **OPEN** | Actual jumps, domains, grading, and trace/arithmetical identification are missing, §0.3. |
