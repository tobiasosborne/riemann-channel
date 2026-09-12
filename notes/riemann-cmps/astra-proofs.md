# The Phantasm: spectral rigidity, obstructions, and corrected finite-field transfers

Author: codex:gpt-6-astra

This note uses the three requested local context files, `HANDOFF.md`, and the supplied finite-field module. No web access was used. Only this file was written; Python checks were run from standard input with bytecode writing disabled. The earlier note's Dyson ring-norm theorem is **T4.4** in the file currently on disk, not T4.3.

`proved-here` means that the stated conclusion is proved below from its explicitly listed premises and elementary mathematics. `conditional-on H-*` identifies external mathematical or operator-realization inputs; it does not mean that a proof conditional on those inputs is omitted. `sketched` identifies a formal interpretation or an unresolved passage. None of these labels means independently reviewed.

Multisets carry multiplicities throughout. Distributional pairings are linear in the test function. Ordinary operator traces, distributional spectral traces, supertraces, and Hilbert-space norms are different objects. In particular, assigning a negative spectral multiplicity does not construct a fermionic cMPS or identify a supertrace with its ordinary norm.

## T1. Distributional rigidity and the forced net spectrum

A **graded spectral datum** is the datum in the question: pairs $(\lambda,\epsilon)$, $\epsilon\in\{+1,-1\}$, with positive integer multiplicities, satisfying

$$
\tag{G1}\operatorname{Re}\lambda\leq c,
\qquad
\tag{G2}\sum_{\lambda,\epsilon}m(\lambda,\epsilon)(1+|\lambda|)^{-N}<\infty
$$

for some real $c$ and some nonnegative integer $N$. Increasing an originally specified real exponent to an integer loses nothing. Its net multiplicity is $\nu(\lambda)=m(\lambda,+1)-m(\lambda,-1)$. Missing multiplicities are zero. Equivalent data have the same $\nu$; their Jordan structures, Hilbert-space geometries, and possible operator domains are not part of this equivalence.

**H-ZEF-T (explicit formula in trace form; supplied statement).** “For $u>0$, as distributions on $(0,\infty)$,
$$
\sum_\rho e^{\rho u}=e^u-\operatorname{comb}(u)-\frac1{e^{2u}-1},
$$
the zero sum taken in symmetric order $|\gamma|<T$, $T\to\infty$; equivalently, from
$$
\psi_0(x)=x-\sum_\rho\frac{x^\rho}{\rho}-\log 2\pi-\frac12\log(1-x^{-2})
$$
for $x>1$ by differentiating in $x$ and substituting $x=e^u$.” Here $\psi_0$ gives the midpoint value at jumps; that convention does not affect its distributional derivative. The equivalence concerning differentiation presupposes the distributional interpretation of the displayed zero series; differentiation alone recovers the antiderivative only up to a constant.

**H-ZERO-COUNT (Riemann--von Mangoldt; supplied statement).** “$N(T)=(T/2\pi)\log(T/2\pi e)+O(\log T)$.” The unambiguous fraction notation is $N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}+O(\log T)$. Precisely, $N(T)$ counts zeros with $0<\operatorname{Im}\rho\leq T$, with multiplicity, and this is an asymptotic statement as $T\to\infty$; any endpoint convention changes it only within the stated error.

**H-ZETA-LOC (standard zero location and symmetries; additional explicit input).** The nontrivial zeros satisfy $0<\operatorname{Re}\rho<1$, have nonzero imaginary part, and form a locally finite multiset invariant, with multiplicity, under conjugation and $\rho\mapsto1-\rho$. These facts are used as zeta input, without assuming RH.

**Lemma T1.1 (existence of the supertrace distribution).**

Hypotheses: (G1), (G2).

Claim: $\sum\epsilon m e^{\lambda t}$ converges absolutely after pairing with every $\phi\in C_c^\infty(0,\infty)$ and defines a distribution there. The tested sum is independent of ordering.

Status: `proved-here`.

⟨1⟩1. **Obtain decay in the full complex spectral parameter.**

PROOF: If $\operatorname{supp}\phi\subset[a,b]\subset(0,\infty)$ and $\lambda\ne0$, integration by parts $p$ times gives
$$
\int e^{\lambda t}\phi(t)\,dt
=(-\lambda)^{-p}\int e^{\lambda t}\phi^{(p)}(t)\,dt.
$$
There are no boundary terms. On this support, $|e^{\lambda t}|\leq\max(e^{ca},e^{cb})$, even when $\operatorname{Re}\lambda$ is very negative. Combining this bound for $|\lambda|\geq1$ with the direct integral bound for $|\lambda|<1$ gives
$$
\left|\int e^{\lambda t}\phi(t)\,dt\right|
\leq C_{a,b,c,p}(1+|\lambda|)^{-p}
\big(\|\phi\|_\infty+\|\phi^{(p)}\|_\infty\big).
$$
Using the full $\lambda$ avoids the nonuniform derivatives of $e^{(\operatorname{Re}\lambda)t}$ in the draft's imaginary-part-only argument.

⟨1⟩2. **Sum the seminorm estimate.**

PROOF: Choose $p\geq N$, for example $p=N+2$. (G2) makes the absolute sum finite and bounds it by a fixed test-function seminorm on every fixed compact support. This proves distributional continuity and absolute convergence. Also (G2) implies finitely many spectral occurrences in every bounded subset of $\mathbb C$; in particular every multiplicity is finite. $\square$

**Theorem T1.2 (rigidity up to cancelling pairs).**

Hypotheses: two graded data satisfying (G1), (G2), with identical distributions on $(0,\infty)$.

Claim: their net multiplicities agree at every $\lambda\in\mathbb C$.

Status: `proved-here`.

⟨1⟩1. **Construct and justify a weighted Laplace pairing.**

PROOF: Use a common $c,N$, choose $c_0>c$, and choose an integer $k\geq N+1$. Let $\chi$ be smooth, zero on $(-\infty,1]$, and one on $[2,\infty)$; let $\eta$ be smooth, one on $[0,1]$, and zero on $[2,\infty)$. They may be chosen between zero and one and monotone in their transition regions. Put
$$
h_{\varepsilon,R,s}(t)=\chi(t/\varepsilon)\eta(t/R)t^ke^{-st},
\qquad 0<\varepsilon<1<R.
$$
For $\operatorname{Re}s>c_0$, write the integrand for a mode as
$e^{-(c_0-\lambda)t}[\chi\eta\,t^ke^{-(s-c_0)t}]$ and integrate by parts $p=k+1$ times. The $L^1$ norms of the derivatives of the bracket are bounded uniformly in $\varepsilon,R$, locally uniformly in this half-plane. At the lower cutoff a term with $j$ derivatives on $\chi$ and $l$ on $t^k$ is bounded in integral by a constant times $\varepsilon^{k-l-j+1}$, whose exponent is nonnegative since $l+j\leq k+1$; terms differentiating $t^k$ more than $k$ times vanish. At the upper cutoff the exponential dominates every power of $R$. Thus
$$
\left|\int e^{\lambda t}h_{\varepsilon,R,s}(t)\,dt\right|
\leq C_s|c_0-\lambda|^{-k-1}
\leq C'_s(1+|\lambda|)^{-k-1}.
$$
The last comparison uses $\operatorname{Re}\lambda\leq c<c_0$. For each mode, dominated convergence in the ordinary integral gives
$$
\lim_{\varepsilon\downarrow0,\,R\uparrow\infty}
\int e^{\lambda t}h_{\varepsilon,R,s}(t)\,dt
=\int_0^\infty t^ke^{-(s-\lambda)t}\,dt
=\frac{k!}{(s-\lambda)^{k+1}}.
$$
(G2) and the uniform estimate justify taking this limit inside the spectral sum. This defines the noncompact pairing by the same cutoffs for both distributions, rather than assuming that arbitrary distributions act on noncompact tests.

⟨1⟩2. **Continue the resulting function meromorphically.**

PROOF: The result is
$$
R_k(s)=k!\sum_\lambda\frac{\nu(\lambda)}{(s-\lambda)^{k+1}}.
$$
On any compact set avoiding the spectral values, sufficiently large $|\lambda|$ satisfy $|s-\lambda|\geq|\lambda|/2$ uniformly. (G2) therefore gives absolute, locally uniform convergence of the tail. There are only finitely many remaining values. Consequently $R_k$ is meromorphic on all of $\mathbb C$, and its complete principal part at $\lambda$ is
$$
k!\nu(\lambda)(s-\lambda)^{-k-1}.
$$

⟨1⟩3. **Compare principal parts.**

PROOF: Equality of the distributions gives equality of every cutoff pairing, hence equality of $R_k$ in $\operatorname{Re}s>c_0$. The identity theorem for meromorphic functions on $\mathbb C$ gives equality everywhere. The displayed principal parts identify every $\nu(\lambda)$. Possible distributions supported at $t=0$ have not been implicitly identified: the common cutoff limit and sufficient vanishing of $t^k$ are exactly what make the argument work from positive-time data. $\square$

**Lemma T1.3 (differentiating the explicit formula and changing time).**

Hypotheses: H-ZEF-T in its antiderivative form with distributional convergence, H-ZERO-COUNT, H-ZETA-LOC.

Claims: the trace form of H-ZEF-T has the displayed negative archimedean term, and
$$
\operatorname{comb}(t/2)=2\sum_{n\geq2}\Lambda(n)\delta(t-2\log n).
$$

Status: `conditional-on H-ZEF-T, H-ZERO-COUNT, H-ZETA-LOC`.

⟨1⟩1. **Differentiate with respect to $x$.**

PROOF: On $x>1$, $\psi_0'=\sum_{n\geq2}\Lambda(n)\delta(x-n)$, and
$$
\frac{d}{dx}\left[-\frac12\log(1-x^{-2})\right]
=-\frac{x^{-3}}{1-x^{-2}}.
$$
Hence multiplying the differentiated identity by $x$ gives
$$
\sum_\rho x^\rho
=x-x\sum_n\Lambda(n)\delta(x-n)-\frac1{x^2-1}.
$$
After pullback by $x=e^u$, $e^u\delta(e^u-n)=\delta(u-\log n)$, giving H-ZEF-T. On a compact subset of $u>0$,
$1/(e^{2u}-1)=\sum_{k\geq1}e^{-2ku}$ with all derivatives converging locally uniformly. H-ZERO-COUNT and T1.1 justify differentiating the zero sum in the indicated distributional sense. The constant $-\log2\pi$ disappears.

⟨1⟩2. **Check the half-time Jacobian.**

PROOF: $\delta(t/2-a)=2\delta(t-2a)$ by testing and substitution. Apply this atom by atom; only finitely many prime-power atoms meet a compact time interval. $\square$

**Corollary T1.4 (the forced arithmetic net spectra).**

Hypotheses: (G1), (G2), H-ZEF-T, H-ZERO-COUNT, H-ZETA-LOC.

Claims: if the supertrace is $\operatorname{comb}(u)$, its only nonzero net multiplicities are
$$
\nu(1)=1,\qquad \nu(\rho)=-m_\rho,\qquad \nu(-2k)=-1\quad(k\geq1).
$$
If the supertrace is $2P_+(t)$, its only nonzero net multiplicities are
$$
\nu(0)=1,\qquad \nu(-\overline\rho/2)=-m_\rho,
\qquad \nu(-(k+1/2))=-1\quad(k\geq1).
$$

Status: `conditional-on H-ZEF-T, H-ZERO-COUNT, H-ZETA-LOC`.

⟨1⟩1. **Exhibit a reference datum for the comb.**

PROOF: Rearrange H-ZEF-T and expand the geometric series. H-ZERO-COUNT gives (G2), for instance with $N=3$, for the zero multiset; the real ladder also satisfies it. The strip gives (G1). The three classes of spectral values are disjoint. T1.2 proves uniqueness of their net multiplicities.

⟨1⟩2. **Transport the reference datum.**

PROOF: Multiply that identity at $u=t/2$ by $e^{-t/2}$. Its left side is $2P_+$ by T1.3 and $e^{-t/2}=1/n$ at $t=2\log n$. Its right side is
$$
1-\sum_\rho e^{(\rho-1)t/2}-\sum_{k\geq1}e^{-(k+1/2)t}.
$$
Conjugation and reflection identify $\{\rho-1\}=\{-\overline\rho\}$ with multiplicities. Apply T1.2 again. This transports whole distributions; it is not a termwise evaluation of a divergent zero trace. $\square$

## T2. What positivity does and does not force

**H-SCHWARTZ (positive distributions).** A distribution $T\in\mathcal D'(0,\infty)$ satisfying $\langle T,\phi\rangle\geq0$ for every real nonnegative $\phi\in C_c^\infty(0,\infty)$ is integration against a unique positive Radon measure on $(0,\infty)$. Conversely every positive Radon measure defines such a distribution. This is positivity, not positive definiteness on convolutions.

**H-LANDAU (Landau's singularity theorem; supplied statement).** “The Laplace transform of a positive measure on $(0,\infty)$ with finite abscissa of convergence $\sigma_c$ has a singularity at $s=\sigma_c$.” Here the transform is $\int e^{-st}\,d\mu(t)$, assumed finite on some real right half-line; a singularity means no holomorphic continuation through the real point $\sigma_c$. A measure with abscissa $-\infty$ is outside this assertion.

Assign one common parity to all copies at a given spectral value in $\{1\}\uplus\{\rho\}\uplus\{-2k:k\geq1\}$. The reference parity is even at $1$ and odd elsewhere. Write $F_Z$ for the flipped nontrivial zeros, $F_T\subset\mathbb N_{\geq1}$ for flipped trivial zeros, and $b=1$ or $0$ according as the pole is flipped or not. By T1.1 the resulting distribution is
$$
\tag{2.1}
\mu=\operatorname{comb}+f,\qquad
f=-2be^u+2\sum_{\rho\in F_Z}m_\rho e^{\rho u}
       +2\sum_{k\in F_T}e^{-2ku}.
$$
The zero sum is distributional. The last sum is a smooth function on $u>0$, even when $F_T$ is infinite.

**Lemma T2.1 (reality of a parity assignment).**

Hypotheses: H-ZERO-COUNT, H-ZETA-LOC; the one-parity-per-value convention above.

Claim: the supertrace is real if and only if $F_Z$ is invariant under conjugation, equivalently the whole flip set is conjugation invariant.

Status: `conditional-on H-ZERO-COUNT, H-ZETA-LOC`.

⟨1⟩1. **Prove sufficiency.**

PROOF: Conjugation permutes the modes and preserves their multiplicities and assigned signs. Absolute convergence of tested sums from T1.1 permits this reindexing and proves reality.

⟨1⟩2. **Prove necessity.**

PROOF: The conjugate distribution is the supertrace of the conjugated datum. Reality and T1.2 imply equality of their net multiplicities. At a zero, these multiplicities are precisely $\pm m_\rho$, and $m_\rho=m_{\overline\rho}$. Thus the assigned signs coincide at conjugate values. Real spectral values cause no constraint. $\square$

**Theorem T2.2 (finite changes to zero parities).**

Hypotheses: H-ZEF-T, H-ZERO-COUNT, H-ZETA-LOC, H-SCHWARTZ; $F_Z$ is finite. The set $F_T$ may be arbitrary, including infinite.

Claim: $\mu$ is positive if and only if $b=0$ and $F_Z=\varnothing$. Thus the draft's finite-$F$ assertion holds, and it extends to arbitrary changes of trivial-zero parities with finitely many nontrivial-zero changes.

Status: `conditional-on H-ZEF-T, H-ZERO-COUNT, H-ZETA-LOC, H-SCHWARTZ`.

⟨1⟩1. **Extract the sign of the continuous part.**

PROOF: Positivity implies reality, hence conjugation invariance by T2.1. Now $f$ in (2.1) is real and continuous, indeed real analytic. If $f(u_0)<0$, it is negative on an interval. The prime-power support is locally finite, so some smaller open interval contains no atom and still has $f<0$. A nonzero nonnegative smooth test there makes $\mu$ negative. Thus $f\geq0$ pointwise.

⟨1⟩2. **Exclude a flipped pole.**

PROOF: If $b=1$, every exponential in the finite zero sum has real exponent strictly less than $1$; the trivial sum is at most $2e^{-2u}/(1-e^{-2u})$. Therefore $e^{-u}f(u)\to-2$, contradicting step ⟨1⟩1.

⟨1⟩3. **Prove the oscillation needed to exclude flipped zeros.**

PROOF: Suppose $F_Z\ne\varnothing$ and let $\sigma_*>0$ be the largest real part in it. Then
$$
e^{-\sigma_*u}f(u)=A(u)+o(1),\qquad
A(u)=2\sum_{\substack{\rho\in F_Z\\\operatorname{Re}\rho=\sigma_*}}
m_\rho e^{i\operatorname{Im}\rho\,u}.
$$
The finite trigonometric polynomial $A$ is real, has no constant term, and is nonzero. Elementary integration of exponentials gives
$$
\frac1T\int_0^T A(u)\,du\longrightarrow0,
\qquad
\frac1T\int_0^T A(u)^2\,du\longrightarrow C>0.
$$
It cannot have $\liminf_{u\to\infty}A(u)\geq0$: if $|A|\leq M$ and eventually $A\geq-\delta$, then the vanishing first mean gives $\limsup T^{-1}\int A_+\leq\delta$, while $A^2\leq M A_++\delta^2$ eventually. This would imply $C\leq M\delta+\delta^2$ for every $\delta>0$. Hence $A(u_j)\leq-\delta_0$ along an unbounded sequence for some $\delta_0>0$. The $o(1)$ remainder makes $f(u_j)<0$ eventually, a contradiction. This proves the required oscillation for the entire leading-frequency sum, rather than inferring it from a single cosine in isolation.

⟨1⟩4. **Prove sufficiency.**

PROOF: With no pole or nontrivial-zero flips,
$$
\mu=\operatorname{comb}+2\sum_{k\in F_T}e^{-2ku}\geq0.
$$
Both terms are positive Radon measures on the open half-line. $\square$

**Proposition T2.3 (an infinite-case theorem with an explicit additional premise).**

Hypotheses: those of T2.2 except finiteness of $F_Z$; additionally $\mu\geq\operatorname{comb}$ as measures, and H-LANDAU.

Claim: $b=0$ and $F_Z=\varnothing$; $F_T$ remains arbitrary.

Status: `conditional-on H-ZEF-T, H-ZERO-COUNT, H-ZETA-LOC, H-SCHWARTZ, H-LANDAU, the measure domination premise`.

⟨1⟩1. **Take a positive weighted Laplace transform.**

PROOF: The added premise says $f\geq0$ as a measure. Choose $k$ as in T1.2 and use its nonnegative monotone cutoffs for real $s>1$. Monotone convergence and the finite limit in T1.2 prove that $u^k f(du)$ has finite Laplace transform there, given by
$$
R(s)=2k!\left[-\frac{b}{(s-1)^{k+1}}
+\sum_{\rho\in F_Z}\frac{m_\rho}{(s-\rho)^{k+1}}
+\sum_{j\in F_T}\frac1{(s+2j)^{k+1}}\right].
$$
It extends meromorphically to $\mathbb C$ by T1.2.

⟨1⟩2. **Exclude the pole and then the zero poles.**

PROOF: If $b=1$, $R(s)\to-\infty$ as real $s\downarrow1$; the other terms are holomorphic near $1$. This contradicts positivity of the transform. If some $\rho\in F_Z$, its nonremovable pole implies that the abscissa of convergence of this positive measure is at least $\operatorname{Re}\rho>0$, since a Laplace transform is holomorphic in its half-plane of convergence. That abscissa is at most $1$. But with $b=0$ the meromorphic formula is holomorphic at every positive real point. This contradicts H-LANDAU. $\square$

**Remark T2.4 (the unrestricted infinite question remains open here).**

Hypotheses: only those in the question for infinite $F$ and positivity of $\mu$.

Status: `sketched` (scope statement; no theorem asserting full parity rigidity).

⟨1⟩1. **Locate the precise missing step.**

PROOF: H-SCHWARTZ makes $f=\mu-\operatorname{comb}$ a signed Radon measure. Its diffuse part is nonnegative, but at a prime-power atom its mass can be negative, down to minus that atom's comb mass. Thus $f$ need not be positive, and T2.3's extra premise does not follow. The transform of $\mu+\operatorname{comb}$ is positive but has the real pole at $1$ from the comb; Landau then supplies no obstruction to additional poles at zeros further left. The diffuse-part transform has not been shown to have exactly the poles of the flipped spectral subseries: extracting atomic and diffuse parts is not the same as selecting spectral terms. That separation, or another argument controlling the atoms, is missing. No assertion that positivity forces all infinitely assigned zero parities is made. Exact equality to the prescribed prime measure is nevertheless rigid by T1. $\square$

## T3. Ordinary trace obstructions and numerator spectra

**H-LIDSKII (Lidskii's theorem; supplied statement).** “For a trace-class operator on a separable Hilbert space, $\operatorname{Tr}E^n=\sum_i\lambda_i^n$ for $n\geq1$ with $\sum_i|\lambda_i|<\infty$, eigenvalues with algebraic multiplicity.” Zero eigenvalues need not be listed; the nonzero spectrum of a compact operator is discrete with finite algebraic multiplicities and can accumulate only at zero. Each $E^n$ is trace class.

**H-WEIL (Weil's curve theorem; additional supplied input made explicit).** For a smooth projective geometrically connected curve $C/\mathbb F_q$ of genus $g$, there are $2g$ nonzero algebraic numbers $\alpha_j$, counted with multiplicity, such that
$$
\#C(\mathbb F_{q^n})=1+q^n-\sum_{j=1}^{2g}\alpha_j^n,
\qquad |\alpha_j|=\sqrt q
$$
under every complex embedding. Its zeta function is $\prod_j(1-\alpha_j u)/[(1-u)(1-qu)]$, and the $\alpha_j$ are the eigenvalues of the Frobenius action on $H^1$ in the convention giving this trace formula. Geometric connectedness is included because the displayed two even eigenvalues would otherwise need modification.

**Theorem T3.1 (finite and trace-class no-go).**

Hypotheses: finite multisets of nonzero numbers $\{b_i\}_{i=1}^P$ and $\{\alpha_j\}_{j=1}^Z$ are disjoint after common occurrences have been cancelled, $Z\geq1$, and
$$
N_n=\sum_i b_i^n-\sum_j\alpha_j^n\quad(n\geq1).
$$
For the infinite-dimensional assertion also assume H-LIDSKII.

Claims: no finite matrix, and no trace-class operator on a separable Hilbert space, has $\operatorname{Tr}E^n=N_n$ for every $n\geq1$.

Status: finite assertion `proved-here`; trace-class assertion `conditional-on H-LIDSKII`.

⟨1⟩1. **Compare ordinary moment-generating functions.**

PROOF: For sufficiently small $|u|$, a hypothetical trace-class realization gives
$$
\sum_{n\geq1}N_nu^n
=\sum_\lambda m_E(\lambda)\frac{\lambda u}{1-\lambda u}.
$$
Indeed $\sum|\lambda|<\infty$ and $|u|\sup|\lambda|<1$ justify both summations. The left side also equals
$$
\sum_i\frac{b_i u}{1-b_i u}-\sum_j\frac{\alpha_j u}{1-\alpha_j u}.
$$
The hypothetical right side is meromorphic on $\mathbb C$: on each compact set only finitely many denominators can be small, and the remaining terms are bounded by $C_K|\lambda|$. Its poles are locally finite.

⟨1⟩2. **Compare a forbidden residue.**

PROOF: At $u=1/\alpha$, the residue of $\alpha u/(1-\alpha u)$ is $-1/\alpha$. Thus the prescribed function has residue $+m_\alpha/\alpha$, while an ordinary trace function has residue $-m_E(\alpha)/\alpha$, with $m_E(\alpha)\geq0$. Disjointness removes every positive prescribed $b$-contribution at that value. Meromorphic uniqueness would require $m_E(\alpha)=-m_\alpha$, impossible. For a finite matrix the same proof is finite algebra and uses no H-LIDSKII. Jordan blocks change neither power traces nor these residues. $\square$

**Proposition T3.2 (trace and supertrace criteria).**

Hypotheses: a complex sequence $(N_n)_{n\geq1}$; form the formal germ
$$
\mathcal Z(u)=\exp\left(\sum_{n\geq1}\frac{N_nu^n}{n}\right),\qquad \mathcal Z(0)=1.
$$

Claims:

1. It is the trace sequence of a trace-class operator if and only if, as a germ,
   $$
   \mathcal Z(u)=\prod_i(1-\lambda_i u)^{-1},\qquad \sum_i|\lambda_i|<\infty.
   $$
   Equivalently $1/\mathcal Z$ is exactly a normalized genus-zero canonical product with absolutely summable reciprocal zeros. No nonconstant zero-free exponential factor is allowed.
2. It is the supertrace sequence of a finite graded matrix if and only if $\mathcal Z$ is a rational function regular at zero with value one. Its nonzero net even spectrum is the multiset of reciprocal poles, and its nonzero net odd spectrum the multiset of reciprocal zeros, after cancellation.

Status: first necessity `conditional-on H-LIDSKII`; the other assertions `proved-here`.

⟨1⟩1. **Prove the trace-class criterion in both directions.**

PROOF: H-LIDSKII and the absolutely convergent expansion $-\log(1-z)=\sum_{n\geq1}z^n/n$ give necessity near zero. The product converges normally to an entire function in the denominator because $\sum|\lambda_i|<\infty$. Conversely the diagonal operator with these $\lambda_i$ on $\ell^2$ is trace class and has the claimed power traces by absolute summation. A finite or empty family is allowed. Formal equality implies convergence of the germ in this situation, so no convergence of the original sequence was silently assumed.

⟨1⟩2. **Prove the graded criterion.**

PROOF: A finite grading-preserving matrix $E=E_+\oplus E_-$ gives
$$
\mathcal Z(u)=\frac{\det(1-uE_-)}{\det(1-uE_+)}.
$$
Conversely factor a rational function normalized at zero into factors $1-\lambda u$. Put reciprocal poles in a diagonal even block and reciprocal zeros in a diagonal odd block. Logarithmic differentiation proves every required moment. The residue argument of T3.1 identifies net multiplicities uniquely. Eigenvalue zero, its parity, and nilpotent blocks are invisible to all positive powers, so no criterion here determines them. $\square$

**Corollary T3.3 (curves, MPS ring norms, and graphs).**

Hypotheses: H-WEIL, $g\geq1$, $q>1$ for the curve statements; H-LIDSKII for the trace-class conclusion. For the MPS statement, use a fixed finite family of finite matrices $A_s$ and periodic amplitudes $\operatorname{Tr}(A_{s_n}\cdots A_{s_1})$. For the graph statement, let $T$ be the finite non-backtracking adjacency matrix on directed edges of a finite graph (in particular a $(q+1)$-regular graph).

Claims: the curve counts have no finite ordinary trace or trace-class realization. They have the graded realization with even block $\operatorname{diag}(q,1)$ and odd block $\operatorname{Frob}|H^1$. Their odd **net spectral multiset** is forced to be $\{\alpha_j\}$. No fixed finite-bond translation-invariant ordinary MPS can have these ring norms for all $n$. In contrast, the non-backtracking graph counts $\operatorname{Tr}T^l$ are ordinary trace counts, and their Ihara zeta $\det(1-uT)^{-1}$ has no finite zeros.

Status: curve conclusions `conditional-on H-WEIL` (and H-LIDSKII where specified); MPS contraction and graph conclusions `proved-here`.

⟨1⟩1. **Apply the obstruction and construct the grading.**

PROOF: $|\alpha_j|=\sqrt q$ is different from both $1$ and $q$, so no cancellation is possible and $2g\geq2$. T3.1 applies. H-WEIL itself supplies the displayed supertrace realization, and T3.2 supplies its forced nonzero net spectrum.

⟨1⟩2. **Contract an ordinary MPS ring.**

PROOF: Expanding the norm squared and using $\operatorname{Tr}(A\otimes\overline A)=|\operatorname{Tr}A|^2$ gives
$$
\langle\Psi_n|\Psi_n\rangle
=\sum_{s_1,\ldots,s_n}|\operatorname{Tr}(A_{s_n}\cdots A_{s_1})|^2
=\operatorname{Tr}\left(\sum_s A_s\otimes\overline{A_s}\right)^n.
$$
The finite matrix in parentheses is therefore excluded by step ⟨1⟩1. This excludes an ordinary fixed local tensor even in the quadratic Artin--Schreier family of positive genus; a complex partition-function transfer is not an MPS norm transfer.

⟨1⟩3. **Evaluate the graph zeta.**

PROOF: A closed non-backtracking directed-edge walk of length $l$, with a marked starting edge, contributes exactly one to $\operatorname{Tr}T^l$. Expanding the determinant logarithm gives the reciprocal determinant zeta. The numerator is the constant one, so there are no finite zeros, although there may be a zero at infinity as a rational function on the sphere. Thus in these two trace dictionaries the curve numerator requires negative net multiplicities and the graph reciprocal determinant does not. This is the precise spectral content of the notebook's “sign” language; it is not a general criterion for physical fermions. $\square$

## T4. The Riemann channel as a prescribed odd sector

**H-LP (Lax--Phillips/model-space input; supplied statement).** “$Z(t)=e^{tB}$ is a strongly continuous contraction semigroup on $K_S$ whose generator $B$ has pure point spectrum $\{-\overline\rho/2\}$, one eigenvector per zero, and $Z(t)\to0$ strongly; take as given.” All zero occurrences are counted with the specified multiplicities. This is assumed operator data, not a consequence proved from the symbol $S(\tau)=\xi(1-2i\tau)/\xi(1+2i\tau)$ here. In particular nothing below independently establishes innerness of that symbol, completeness of its asserted modes, or the asserted geometric identification.

**H-TRACE (prescribed distributional trace; supplied statement).** “The distributional trace $\operatorname{Tr}Z(t):=\sum_\rho e^{-\overline\rho t/2}$, a distribution on $(0,\infty)$ by H-ZERO-COUNT; this is a definition by fiat.” Precisely, H-ZETA-LOC and T1.1 are also used for the convergence. This is not an application of Lidskii to $Z(t)$.

To avoid using $B$ for both a space and an operator, write
$$
\mathscr B=\mathbb C_+\oplus(K_S\oplus\ell^2(\mathbb N_{\geq1}))_-,
\qquad G=0\oplus B\oplus D,
\qquad De_k=-(k+1/2)e_k.
$$
Its domain is $\mathbb C\oplus\mathcal D(B)\oplus\{x:\sum(k+1/2)^2|x_k|^2<\infty\}$.

**Proposition T4.1 (the exact prime-measure supertrace).**

Hypotheses: H-LP, H-TRACE, H-ZEF-T, H-ZERO-COUNT, H-ZETA-LOC.

Claims: $e^{tG}=1\oplus Z(t)\oplus\operatorname{diag}(e^{-(k+1/2)t})$ is a strongly continuous contraction semigroup. Its common fixed-vector space is exactly the even line. Its prescribed supertrace on $t>0$ is
$$
\tag{4.1}
\operatorname{str}e^{tG}
=1-\operatorname{Tr}_{\rm dist}Z(t)-\sum_{k\geq1}e^{-(k+1/2)t}
=2P_+(t)=2\sum_{n\geq2}\frac{\Lambda(n)}n\delta(t-2\log n).
$$

Status: `conditional-on H-LP, H-TRACE, H-ZEF-T, H-ZERO-COUNT, H-ZETA-LOC`.

⟨1⟩1. **Verify the operator statements.**

PROOF: Each diagonal ladder factor has modulus at most one, and dominated convergence of $\sum|x_k|^2|e^{-(k+1/2)t}-1|^2$ gives strong continuity at zero. The direct sum with H-LP and the constant line is a strongly continuous contraction semigroup with the stated generator domain. A fixed vector in $K_S$ is zero by strong stability, and no ladder coordinate is fixed. The constant line is fixed pointwise.

⟨1⟩2. **Evaluate the zero trace with all signs.**

PROOF: Reindexing by conjugation and reflection, justified by T1.1, gives
$$
\sum_\rho e^{-\overline\rho t/2}
=\sum_\rho e^{-\rho t/2}
=e^{-t/2}\sum_\rho e^{\rho t/2}.
$$
H-ZEF-T at $u=t/2$ therefore gives
$$
\tag{4.2}
\operatorname{Tr}_{\rm dist}Z(t)
=1-2P_+(t)-\frac{e^{-t/2}}{e^t-1}.
$$
Indeed $e^{-t/2}\operatorname{comb}(t/2)=2P_+$, and
$$
A(t):=\frac{e^{-t/2}}{e^t-1}
=\sum_{k\geq1}e^{-(k+1/2)t}.
$$
Substitution into the definition of the supertrace proves (4.1). The ungraded zero trace has prime atoms with coefficient $-2\Lambda(n)/n$, as in the report's correction observation; it is not supported solely on those atoms. $\square$

**Proposition T4.2 (ladder alternatives and rigidity).**

Hypotheses: those of T4.1 for the operator realizations; only (G1), (G2), H-ZEF-T, H-ZERO-COUNT, H-ZETA-LOC for the rigidity assertion.

Claims: the even line plus odd $K_S$ has supertrace $2P_++A(t)$; putting the ladder in the even sector gives $2P_++2A(t)$. Both are positive. Exact equality to $2P_+$ forces the net spectral multiplicities of $G$, up to cancelling pairs. In particular there is no all-even graded spectral datum satisfying (G1), (G2) with supertrace $2P_+$ or with supertrace $\operatorname{comb}$.

Status: `conditional-on the explicitly listed zeta/operator inputs`.

⟨1⟩1. **Compute the variants.**

PROOF: Remove $-A$ from (4.1), or replace it by $+A$. Since $A(t)>0$, positivity follows directly. Thus positivity alone does not fix the ladder's parity.

⟨1⟩2. **Use exact spectral uniqueness.**

PROOF: T1.4 identifies every net multiplicity for exact equality. At each zero and each ladder value the required net multiplicity is negative. An all-even datum has only nonnegative net multiplicities, a contradiction. The direct sum in T4.1 realizes this forced single-particle datum under H-LP. It is a Hilbert-space semigroup; it has not been shown to be a trace-preserving generator on an operator algebra. $\square$

**Remark T4.3 (scope of the Phantasm interpretation).**

Hypotheses: H-LP and H-ZETA-LOC for the spectral sentence. The geometric descriptions in the next paragraph are interpretive identifications, not new hypotheses used in proofs.

Status: spectral equivalence `conditional-on H-LP, H-ZETA-LOC`; geometric and physical identifications `sketched`.

RH is exactly the assertion that every odd $K_S$ generator mode has real part $-1/4$. It does not make the extra odd ladder lie on that line. The added fixed line is even by construction and represents the pole term after the transformation in T1.4. The usual geometric names are the constant function on the modular surface and the residue of the Eisenstein series at $s=1$. Identifying that line with those geometric objects is not a construction made here. The completed $\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ is entire; it has no pole at $1$. The pole being represented belongs to $\zeta$ (or the completion before multiplying by $s(s-1)$).

For every fixed $t>0$, the infinitely many asserted eigenvalues of $Z(t)$ have modulus at least $e^{-t/2}$. Thus $Z(t)$ cannot be trace class, or compact with that eigenvalue list. A finite-dimensional ordinary cMPS transfer has an analytic ring-norm function of length, by the finite Dyson theorem in the earlier file, and cannot equal a nonzero pure atomic prime measure as a distribution. The distributional construction (4.1) supplies an exact graded spectral identity. It does not supply a cMPS tensor whose Hilbert norm is that identity. A supertrace is generally signed: for example an even eigenvalue $1$ and an odd eigenvalue $2$ give supertrace $-1$ at the first power. A parity insertion requires a specified physical construction and boundary convention before any norm claim can be made.

## T5. Vacuum decay: a genuine channel, with additional even modes

**H-CMPS (canonical cMPS Schmidt-spectrum fact; additional input).** For a translation-invariant pure infinite cMPS in canonical form with left transfer fixed point $I$ and normalized right fixed point $\rho$, the nonzero eigenvalues of the half-chain reduced density operator are the nonzero eigenvalues of $\rho$, with multiplicity, in the canonical state selected by that fixed point. More generally the bond expression is the normalized $\sqrt l\,r\sqrt l$. This statement concerns equality of nonzero spectra, or identification of Schmidt supports by an isometry, not literal equality of operators on different Hilbert spaces. In the rank-deficient case one restricts to the support selected by the state. This is the precise version of the requested “the half-chain reduced density matrix is the fixed point” fact.

**Theorem T5.1 (finite vacuum-decay Lindbladian and multiplicities).**

Hypotheses: $H$ is finite dimensional, $B\in\mathcal B(H)$,
$$
-(B+B^\dagger)=|j\rangle\langle j|,
\qquad e^{tB}\longrightarrow0.
$$
Let $\mathscr H=\mathbb C\mathrm{vac}\oplus H$, $\bar B=0\oplus B$, $J=|\mathrm{vac}\rangle\langle j|$, and use the Schrödinger convention
$$
\mathcal L(x)=\bar Bx+x\bar B^\dagger+JxJ^\dagger.
$$
The vacuum line is even and $H$ odd. Let $b_1,\ldots,b_d$ list the eigenvalues of $B$ with algebraic multiplicity.

Claims: $\mathcal L$ is a trace-preserving GKLS generator. Its unique stationary density matrix is $\Omega=|\mathrm{vac}\rangle\langle\mathrm{vac}|$, and its entire fixed-operator space is $\mathbb C\Omega$. Its spectral multiset is
$$
\tag{5.1}
\{0\}\uplus\{b_i\}_{i=1}^d\uplus\{\overline b_i\}_{i=1}^d
\uplus\{b_i+\overline b_j:1\leq i,j\leq d\}.
$$
The middle two lists are odd, and the first and last lists even.

Status: `proved-here`.

⟨1⟩1. **Put the generator in GKLS form.**

PROOF: $\bar B+\bar B^\dagger=-J^\dagger J$. The Hermitian operator $H_0=(\bar B^\dagger-\bar B)/(2i)$ gives
$$
\bar B=-iH_0-\tfrac12J^\dagger J,
\qquad
\mathcal L(x)=-i[H_0,x]+JxJ^\dagger-\tfrac12\{J^\dagger J,x\}.
$$
Cyclicity gives $\operatorname{Tr}\mathcal L(x)=0$. Complete positivity also follows directly from the channel formula in the next step (so no external GKLS existence theorem is needed).

⟨1⟩2. **Solve all four blocks.**

PROOF: For $x=\begin{pmatrix}a&r\\l&X\end{pmatrix}$,
$$
\mathcal L(x)=
\begin{pmatrix}\langle j,Xj\rangle&rB^\dagger\\Bl&BX+XB^\dagger\end{pmatrix}.
$$
Writing $Z_t=e^{tB}$, integration gives
$$
\tag{5.2}
e^{t\mathcal L}(x)=
\begin{pmatrix}
 a+\operatorname{Tr}X-\operatorname{Tr}(Z_tXZ_t^\dagger)&rZ_t^\dagger\\
 Z_tl&Z_tXZ_t^\dagger
\end{pmatrix}.
$$
To check the feed, differentiate $\operatorname{Tr}(Z_tXZ_t^\dagger)$ and use $B+B^\dagger=-|j\rangle\langle j|$. Also $I-Z_t^\dagger Z_t\geq0$. Formula (5.2) is the sum of conjugation by $1\oplus Z_t$ and the completely positive map $X\mapsto\operatorname{Tr}[(I-Z_t^\dagger Z_t)X]\Omega$, proving complete positivity. The total trace is $a+\operatorname{Tr}X$.

⟨1⟩3. **Determine fixed points.**

PROOF: Finite-dimensional stability gives $Z_t\to0$ in norm. Formula (5.2) therefore converges to $x\mapsto\operatorname{Tr}(x)\Omega$. Every fixed operator is a multiple of $\Omega$, and among trace-one positive operators there is exactly one. “Unique fixed point” must mean unique stationary density matrix, since linearity always gives all scalar multiples as fixed operators.

⟨1⟩4. **Count the whole spectrum without diagonalizability.**

PROOF: The block map is triangular, with diagonal blocks $0$, right multiplication by $B^\dagger$, left multiplication by $B$, and $X\mapsto BX+XB^\dagger$. Triangularizing $B$ and the conjugate matrix, or using their Kronecker sum, shows that the last block has the pair sums $b_i+\overline b_j$ with ordered pairs of indices. Thus
$$
\chi_{\mathcal L}(z)=z\prod_i(z-b_i)(z-\overline b_i)
\prod_{i,j}(z-b_i-\overline b_j).
$$
All $\operatorname{Re}b_i<0$, so no other factor vanishes at zero and its algebraic multiplicity is one. At any other value $\lambda$, its multiplicity is the sum of the occurrence counts in the three lists; collisions add. In distinct-value notation a pair $(b,c)$ contributes $m_B(b)m_B(c)$ copies of $b+\overline c$. The total dimension is $1+2d+d^2=(d+1)^2$.

⟨1⟩5. **Identify the grading.**

PROOF: The grading on operators is $x\mapsto\Gamma x\Gamma$ with $\Gamma=1\oplus(-I_H)$. The off-diagonal vacuum--$H$ blocks are odd; both population blocks are even. Although $J$ is odd, $x\mapsto JxJ^\dagger$ preserves this operator grading. The spectral lists therefore have exactly the asserted parities. $\square$

**Corollary T5.2 (finite traces and the distinction from $G$).**

Hypotheses: T5.1.

Claims:
$$
\operatorname{Tr}_{\operatorname{End}\mathscr H}e^{t\mathcal L}
=|1+\operatorname{Tr}_H Z_t|^2,
\qquad
\operatorname{str}_{\operatorname{End}\mathscr H}e^{t\mathcal L}
=|1-\operatorname{Tr}_H Z_t|^2.
$$
In particular the vacuum-decay transfer is not the single-particle generator $0\oplus B$: it includes both coherence lists and all pair sums.

Status: `proved-here`.

⟨1⟩1. **Sum the four block traces.**

PROOF: Their traces are respectively $1$, $\overline{\operatorname{Tr}Z_t}$, $\operatorname{Tr}Z_t$, and $|\operatorname{Tr}Z_t|^2$. Add all signs positively for the ordinary trace and negate the two coherence traces for the supertrace. This proves both formulas, including $t=0$, where the values are $(d+1)^2$ and $(1-d)^2$. $\square$

**Proposition T5.3 (an infinite-dimensional absorbing-vacuum channel).**

Hypotheses: a strongly continuous contraction semigroup $Z_t$ on a separable Hilbert space $H$, with $Z_t\to0$ strongly. For the Riemann interpretation these are supplied by H-LP.

Claim: formula (5.2) defines a strongly continuous completely positive trace-preserving semigroup on the trace-class operators on $\mathbb C\oplus H$, with unique stationary density matrix $\Omega$ and exact odd coherence evolution $l\mapsto Z_tl$, $r\mapsto rZ_t^\dagger$. This construction needs no bounded rank-one exit vector. Its generator need not have the bounded single-jump formula of T5.1.

Status: `proved-here` for the stated semigroup premises; Riemann specialization `conditional-on H-LP`.

⟨1⟩1. **Construct the maps.**

PROOF: For $D_t=I-Z_t^\dagger Z_t\geq0$, the feed $X\mapsto\operatorname{Tr}(D_tX)\Omega$ is normal and completely positive; for example use Kraus rows $|\mathrm{vac}\rangle\langle e_j|D_t^{1/2}$ and an orthonormal basis, with convergence on positive trace-class inputs. Adding conjugation by $1\oplus Z_t$ gives exactly (5.2) and preserves total trace. Composing two such maps telescopes the population loss and uses $Z_{t+s}=Z_tZ_s$, proving the semigroup law.

⟨1⟩2. **Prove continuity, stability, and uniqueness.**

PROOF: Strong continuity of $Z_t$, uniform boundedness, and finite-rank approximation imply trace-norm continuity of $Z_tXZ_t^\dagger$ for trace-class $X$. For positive $X=\sum a_j|v_j\rangle\langle v_j|$, dominated convergence gives $\operatorname{Tr}(Z_tXZ_t^\dagger)=\sum a_j\|Z_tv_j\|^2\to0$ under strong stability. Decomposition into four positive trace-class operators handles arbitrary $X$. The vector coherence blocks converge to zero as well. Formula (5.2) then converges in trace norm to $\operatorname{Tr}(x)\Omega$, proving uniqueness. $\square$

**Remark T5.4 (the formal zero coherence and population spectra).**

Hypotheses: H-LP, H-TRACE, H-ZETA-LOC. No rank-one generator-domain identity in infinite dimension is assumed.

Status: coherence realization `conditional-on H-LP`; full spectral bookkeeping and the form factor `sketched` (formal only).

For $H=K_S$, T5.3 realizes the Riemann channel in the odd coherence blocks. A mode $b_n=-\overline\rho_n/2$ appears on $|v_n\rangle\langle\mathrm{vac}|$, and its conjugate on $|\mathrm{vac}\rangle\langle v_n|$. Because the zeta list is itself conjugation invariant, a given spectral value in that list occurs twice in the combined formal odd list, with total multiplicity $2m_\rho$. The even rank-one population modes $|v_n\rangle\langle v_m|$ have exponents
$$
-\frac{\overline\rho_n+\rho_m}{2}.
$$
This lists eigenmodes, not the complete spectrum of an infinite-dimensional generator on every possible operator space. The symbol
$$
\sum_{n,m}e^{-(\overline\rho_n+\rho_m)t/2}
\quad\text{or}\quad |\operatorname{Tr}_{\rm dist}Z(t)|^2
$$
is a formal form factor, or an equality for finite spectral cutoffs. It is not a defined product of distributions here. In fact the pair list already has infinitely many diagonal values $-\operatorname{Re}\rho_n$ in a bounded interval, violating (G2). H-TRACE does not make that double sum a distribution, and multiplication of its prime delta contributions is not defined by ordinary distribution theory. No pair-correlation conclusion follows.

**Proposition T5.5 (the renewal correction and trivial Schmidt spectrum).**

Hypotheses: T5.1; H-CMPS for the half-chain spectrum assertion.

Claims: the jump sends every emitted population into $\Omega$, but the proposed renewal formula with rebound state $\Omega$ does not define a finite stationary integral. The canonical infinite cMPS state selected by this stationary bond state has only one nonzero Schmidt weight, equal to one; its half-chain entanglement is trivial.

Status: renewal and absorbing-state assertions `proved-here`; canonical half-chain assertion `conditional-on H-CMPS`.

⟨1⟩1. **Check reinsertion and the failed integral.**

PROOF: $JxJ^\dagger=\langle j,Xj\rangle\Omega$ does reinsert into the vacuum, but $J\Omega=0$ and $e^{t\bar B}\Omega e^{t\bar B^\dagger}=\Omega$. Consequently
$$
\int_0^T e^{t\bar B}\Omega e^{t\bar B^\dagger}\,dt=T\Omega,
$$
whose trace tends to infinity. The integral in the original $H$ is not even typed, since $\Omega$ lives in the added line. In the enlarged space it diverges. Normalizing a finite cutoff gives $\Omega$, but that is not a finite renewal solution. The no-event semigroup on the enlarged space is not strongly stable: the vacuum is an absorbing, nonemitting state with infinite holding time. Thus this model does not solve HANDOFF's finite-occupation renewal equation for a nontrivial rebound inside $K_S$.

⟨1⟩2. **Compute the Schmidt weights and check the output directly.**

PROOF: Trace preservation supplies left fixed point $I$ and T5.1 supplies right fixed point $\Omega$, of rank one. H-CMPS gives exactly the nonzero Schmidt spectrum $\{1\}$. Directly, every ring amplitude containing a jump has zero trace: a jump maps into the vacuum, further jumps annihilate it, and the no-event operator preserves the two blocks. The only possible periodic field configuration is therefore the field vacuum, with no-event amplitude $\operatorname{Tr}e^{t\bar B}$. For lengths at which that amplitude is nonzero the normalized ring state is the vacuum; if it vanishes the ring vector is zero and cannot be normalized. Since it tends to one at large length, this exception causes no ambiguity in the stationary infinite state. $\square$

## T6. The prime chain and the limits of its thermal dynamics

**H-BC (Bost--Connes; supplied wording, with scope correction below).** “The Hamiltonian $H=\log N$ on $\ell^2(\mathbb N)$, $N|n\rangle=n|n\rangle$, generating $\sigma_t=\operatorname{Ad}(N^{it})$; the KMS$_\beta$ states for $\beta>1$ are the Gibbs states of $H$ in the standard representation; for $\beta\leq1$ there is a unique KMS$_\beta$ state and it is a factor state of type III$_1$ — take as given, cite as Bost--Connes 1995.”

The supplied wording requires two qualifications. The arithmetic system is the **Bost--Connes $C^*$-algebra**, not all of $\mathcal B(\ell^2(\mathbb N))$. Above one, its extremal KMS states are Gibbs states in the standard representations labelled by the arithmetic boundary parameter, and general KMS states are mixtures. In one fixed representation on all bounded operators there is only one normal Gibbs state. The standard positive-temperature high-temperature assertion has range $0<\beta\leq1$, not all real $\beta\leq1$.

**H-BC-POS (operational Bost--Connes input).** For the Bost--Connes $C^*$-dynamical system, at $0<\beta\leq1$ the unique KMS$_\beta$ state has type III$_1$ GNS von Neumann algebra. At $\beta>1$ extremal KMS states are the Gibbs states with Hamiltonian $\log N$ in the standard arithmetic family of representations, and all KMS states are their probability mixtures. Attribution: J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory* (1995), as supplied; no external source was consulted. Only this corrected positive-temperature version of H-BC is used as an arithmetic input.

**H-MM1 (M/M/1 spectral theorem; supplied statement).** “The birth--death generator on $\mathbb N$ with constant up-rate $\lambda$ and down-rate $\mu$ has spectrum $\{0\}\cup[-(\sqrt\lambda+\sqrt\mu)^2,-(\sqrt\lambda-\sqrt\mu)^2]$ on $\ell^2$ with the stationary weight, when $\lambda<\mu$.” Precisely use occupations $k\in\mathbb N_0$, omit the down jump at $k=0$, use the backward generator on functions, and use $\pi_k=(1-\lambda/\mu)(\lambda/\mu)^k$ in $L^2(\pi)$. The forward generator on densities has the same spectrum on $\ell^2(\pi^{-1})$. This theorem is proved below.

**Proposition T6.1 (normal KMS states and the product purification).**

Hypotheses: $\alpha_t=\operatorname{Ad}(N^{it})$ on $\mathcal B(\ell^2(\mathbb N))$; normal KMS means the usual normal $W^*$ KMS condition (equivalently its strip condition and analytic matrix-unit identities). Let $\beta\in\mathbb R$. H-BC-POS is needed only for the comparison with the arithmetic system.

Claims: a normal KMS$_\beta$ state exists if and only if $\beta>1$, and then it is uniquely
$$
\rho_\beta=\frac{N^{-\beta}}{\zeta(\beta)}.
$$
The spectrum of $-\log\rho_\beta$ is $\{\beta\log n+\log\zeta(\beta):n\geq1\}$. Its thermofield-double purification is a product over prime sites and has bond dimension one along that chain.

Status: normal-state and factorization assertions `proved-here`; type III comparison `conditional-on H-BC-POS`.

⟨1⟩1. **Use analytic matrix units to force the density.**

PROOF: A KMS state is invariant. Since the eigenvalues $\log n$ are distinct, invariance of a normal density makes it diagonal, say $p_n$. For matrix units $e_{mn}$, $\alpha_{i\beta}(e_{nm})=(n/m)^{-\beta}e_{nm}$. The identity $\omega(A\alpha_{i\beta}(B))=\omega(BA)$ with $A=e_{mn}$, $B=e_{nm}$ gives
$$
p_n=(n/m)^{-\beta}p_m.
$$
Thus $p_n=Cn^{-\beta}$. Normalization is possible exactly when $\sum n^{-\beta}<\infty$, namely $\beta>1$, and forces $C=1/\zeta(\beta)$. Conversely the Gibbs density satisfies the KMS identity by cyclicity on analytic finite matrix combinations; finite spectral projections and the Gibbs trace bounds extend its strip condition to the normal $W^*$ dynamics. Equivalently its modular action is $x\mapsto\rho_\beta^{it}x\rho_\beta^{-it}=\alpha_{-\beta t}(x)$, which is the normal KMS characterization. No point-norm continuity of $\alpha$ on all of $\mathcal B(\ell^2)$ is asserted.

⟨1⟩2. **Factor the density and its purification.**

PROOF: Unique prime factorization identifies the basis vector $|n\rangle$ with occupations $(v_p(n))_p$ of finite support. For $\beta>1$, the Euler product follows by monotone limits of finite prime products and the convergent Dirichlet series. Hence
$$
\rho_\beta=\bigotimes_p\left[(1-p^{-\beta})\sum_{k\geq0}p^{-\beta k}|k\rangle\langle k|\right],
$$
$$
|\mathrm{TFD}_\beta\rangle
=\frac1{\sqrt{\zeta(\beta)}}\sum_{n\geq1}n^{-\beta/2}|n\rangle_L|n\rangle_R
=\bigotimes_p\left[\sqrt{1-p^{-\beta}}\sum_{k\geq0}p^{-\beta k/2}|k\rangle_{p,L}|k\rangle_{p,R}\right].
$$
The product is a well-defined vector in the paired vacuum incomplete tensor product: $\sum_p p^{-\beta}<\infty$, and its coefficients are the displayed summable vector. It has entanglement between left and right at each site, but none between different prime sites. Taking the logarithm of the eigenvalues of $\rho_\beta$ gives the asserted entanglement energies. These are $\beta\log n$ plus a constant; in T4's ring time the corresponding lengths are $2\log n$, so the two conventions differ by that factor.

⟨1⟩3. **Separate the critical arithmetic state from a normal density.**

PROOF: The nonexistence just proved is on all bounded operators in this fixed Hilbert representation. H-BC-POS describes a state on the arithmetic algebra with its own GNS completion. Its type III$_1$ property supplies no trace-class density on this $\ell^2(\mathbb N)$, and in particular no normal bond density equal to a putative $\rho_1$. $\square$

**Lemma T6.2 (proof of H-MM1).**

Hypotheses: $0<\lambda<\mu$, occupations $k\geq0$, stationary weights $\pi_k=(1-\lambda/\mu)(\lambda/\mu)^k$.

Claim: H-MM1 holds, with a simple stationary eigenvalue zero and no other spectral points outside the displayed band.

Status: `proved-here`.

⟨1⟩1. **Conjugate to a Jacobi matrix.**

PROOF: Detailed balance $\pi_k\lambda=\pi_{k+1}\mu$ makes the backward generator self-adjoint in $L^2(\pi)$. Conjugation by $f_k\mapsto\sqrt{\pi_k}f_k$ yields off-diagonal entries $a=\sqrt{\lambda\mu}$, diagonal $-(\lambda+\mu)$ at $k\geq1$, and diagonal $-\lambda$ at zero. The constant-diagonal half-line matrix $K$ has spectrum $[-(\lambda+\mu)-2a,-(\lambda+\mu)+2a]$: the sine transform maps it to multiplication by $-(\lambda+\mu)+2a\cos\theta$ on $0<\theta<\pi$. Truncated plane waves supported arbitrarily far from the boundary give approximate eigenvectors for every point of this band for the modified matrix as well. Its difference from $K$ is $\mu|e_0\rangle\langle e_0|$. The following resolvent calculation accounts for all points outside the band.

⟨1⟩2. **Solve the outside-band recurrence and boundary equation.**

PROOF: For a real eigenvalue $x$ outside the band, the square-summable recurrence solution is $v_k=Cz^k$, $|z|<1$, with
$$
x=-(\lambda+\mu)+a(z+z^{-1}).
$$
The boundary equation is $x=-\lambda+az$. Equating gives $az^{-1}=\mu$, so $z=\sqrt{\lambda/\mu}$ and $x=0$. This solution is square summable, unique up to scalar, and corresponds to the constant function in $L^2(\pi)$. To exclude other spectral points, let $R_0=(x-K)^{-1}$. Solving the first-column recurrence gives $m(x)=\langle e_0,R_0e_0\rangle=z/a$. Direct multiplication verifies the rank-one resolvent formula
$$
(x-K-\mu|e_0\rangle\langle e_0|)^{-1}
=R_0+\frac{\mu}{1-\mu m(x)}R_0|e_0\rangle\langle e_0|R_0.
$$
It is bounded unless $z=a/\mu$, exactly the eigenvalue already found. At the band endpoints the band already accounts for the spectrum. Self-adjointness excludes nonreal spectrum. This proves H-MM1. $\square$

**Proposition T6.3 (the classical prime-by-prime dynamics).**

Hypotheses: $\beta>1$, $r_p>0$, $\sum_p r_p<\infty$. Let $\mu_p|n\rangle=|pn\rangle$ and put $\lambda_p=r_p$, $\mu^{\rm rate}_p=r_pp^\beta$. The displayed Lindblad expression is read in the Schrödinger convention on densities:
$$
\tag{6.1}
\mathcal L_\beta(x)=\sum_p r_p\left(\mu_px\mu_p^\dagger-\tfrac12\{\mu_p^\dagger\mu_p,x\}\right)
+\sum_p r_pp^\beta\left(\mu_p^\dagger x\mu_p-\tfrac12\{\mu_p\mu_p^\dagger,x\}\right).
$$
For merely summable $r_p$, (6.1) is initially a formal expression, not a bounded map on all bounded operators. Its diagonal part is defined by the conservative process below. If a norm-convergent quantum generator is wanted, impose the additional condition $\sum_pr_pp^\beta<\infty$.

Claims: the diagonal process has rates $n\to pn$ equal to $r_p$ and $n\to n/p$ equal to $r_pp^\beta$ when $p\mid n$. It is the independent product of the occupation birth--death chains. It is nonexplosive on finite-support occupation configurations, has unique stationary distribution $\pi(n)=n^{-\beta}/\zeta(\beta)$, and its self-adjoint backward generator on $L^2(\pi)$ has spectrum
$$
\tag{6.2}
\overline{\ \{0\}\ \cup\!
\bigcup_{\substack{A\subset\{\text{primes}\}\\0<|A|<\infty}}
\left(\sum_{p\in A} I_p\right)\ },
\qquad
I_p=[-r_p(p^{\beta/2}+1)^2,-r_p(p^{\beta/2}-1)^2].
$$
The sums in (6.2) are Minkowski sums; the outer closure is essential. This spectrum is real and therefore cannot contain the nonreal Riemann zero generator modes.

Status: `proved-here`, using the proved H-MM1 in T6.2.

⟨1⟩1. **Compute the diagonal rates and prove existence.**

PROOF: $\mu_p^\dagger\mu_p=I$, whereas $\mu_p\mu_p^\dagger$ projects onto numbers divisible by $p$. Thus on the finite-support diagonal density core, with masses $x_n$,
$$
(\mathcal L_\beta x)_n
=\sum_p\left[r_p\mathbf1_{p\mid n}x_{n/p}-r_px_n
+r_pp^\beta x_{pn}-r_pp^\beta\mathbf1_{p\mid n}x_n\right].
$$
At a fixed configuration only finitely many down rates are active. The total up rate is $\sum r_p<\infty$, so in every finite time interval there are almost surely finitely many births. Each death removes one occupation, so the number of deaths is at most the initial total occupation plus the number of births. This proves nonexplosion. Constructing independent single-prime clocks gives the product description and the same rates.

⟨1⟩2. **Check stationarity and uniqueness.**

PROOF: $\pi(n)r_p=\pi(pn)r_pp^\beta$, so detailed balance holds. Equivalently the product of local geometric stationary distributions is the probability in T6.1, supported on finite-support configurations. For a finite set of prime coordinates, T6.2 gives a positive gap above the stationary constants in every factor, hence in their finite tensor product. A point mass has square-integrable density relative to that finite product probability, so the spectral theorem gives convergence to the product law in $L^2$, and then in total variation by Cauchy--Schwarz. Mixing point masses and dominated convergence gives the same convergence from every initial probability. Thus that finite product is its unique stationary law. Every stationary probability on integer configurations must have precisely these stationary finite-coordinate marginals. The marginals determine the product probability, proving uniqueness without invoking an additional recurrence theorem.

⟨1⟩3. **Give the exact Hilbert-space spectral decomposition.**

PROOF: Write each factor $L^2(\pi_p)=\mathbb C1\oplus H_p^0$. Finite cylinder functions are dense in the product $L^2(\pi)$, and expansion into mean and mean-zero components gives the orthogonal direct sum over finite subsets $A$ of primes of $\bigotimes_{p\in A}H_p^0$, with $A=\varnothing$ the constants. Each component is invariant. On it the generator is the finite sum of the bounded commuting single-prime generators acting on separate factors. By T6.2 their spectra on $H_p^0$ are $I_p$; the tensor spectral theorem gives the full Minkowski sum on that component. The self-adjoint direct sum of these restrictions has domain $\{f:\sum_A\|L_A f_A\|^2<\infty\}$ and spectrum the closure of the union of their spectra, proving (6.2). This also defines the generator rigorously even when the down-rate coefficients are not summable. $\square$

**Proposition T6.4 (what can be said about off-diagonal entries).**

Hypotheses: T6.3 and the stronger rate condition $\sum_p r_pp^\beta<\infty$. A valid example is $r_p=p^{-(\beta+2)}$. Use the Hilbert space completion of finite matrix combinations with norm
$$
\|x\|_\beta^2=\sum_{m,n}\frac{|x_{mn}|^2}{\sqrt{\pi(m)\pi(n)}}
=\|\rho_\beta^{-1/4}x\rho_\beta^{-1/4}\|_{\rm HS}^2.
$$

Claims: (6.1) defines a bounded trace-preserving completely positive semigroup on trace-class operators; $\rho_\beta$ is stationary. On the displayed weighted Hilbert space its generator is bounded self-adjoint and nonpositive, including the off-diagonal sectors. Its spectrum there is real. This does not assert the same spectral theorem on the unweighted Banach space of all bounded operators.

Status: `proved-here`.

⟨1⟩1. **Make the quantum sum converge.**

PROOF: Every shift has norm one and each dissipator has norm at most twice its coefficient on trace class. The stronger condition makes the series converge in operator norm. Finite prime sums are standard bounded jump generators; their completely positive trace-preserving semigroups follow, for example, from the Dyson expansion with loss term $-\tfrac12\sum J^\dagger J$. Norm convergence of generators gives convergence of their semigroups and preserves these properties. Each prime dissipator pair annihilates the diagonal Gibbs density by detailed balance, so the limit does as well.

⟨1⟩2. **Verify the off-diagonal weighted symmetry directly.**

PROOF: On a single prime factor, matrix units $|k\rangle\langle l|$ shift together up at rate $\lambda$ and together down at rate $\mu$ when both indices are positive. Their loss coefficient is
$$
-\lambda-\frac\mu2(\mathbf1_{k>0}+\mathbf1_{l>0}).
$$
Conjugating coefficients by $(\pi_k\pi_l)^{-1/4}$ turns both hopping coefficients into $\sqrt{\lambda\mu}$. Sectors of fixed difference $k-l$ are therefore real symmetric half-line Jacobi matrices. For difference zero this is T6.2. For nonzero difference the interior diagonal remains $-(\lambda+\mu)$ and the boundary is $-\lambda-\mu/2$, which is less than the diagonal-sector boundary $-\lambda$. Thus each such operator is nonpositive as well, by quadratic-form comparison with T6.2. Their norms are bounded by a constant times $\lambda+\mu$. The tensor-prime sum converges in this Hilbert operator norm under the stronger rate condition, and is self-adjoint and nonpositive. This proves the assertion including off-diagonal sectors. $\square$

For the draft's example $r_p=p^{-\beta}$, the up rates are summable for $\beta>1$ but every down-rate coefficient is one, so the stronger condition fails. T6.3 still proves the full classical assertion. This note does not claim norm convergence of (6.1) on all quantum operators for that example, nor use it to infer an off-diagonal spectral assertion without a separately specified closure.

**Corollary T6.5 (delocalization, with the dynamical language corrected).**

Hypotheses: T6.1; T6.3 for the classical fixed-point interpretation; H-BC-POS for the comparison across the arithmetic transition.

Claims: as $\beta\downarrow1$, $\rho_\beta$ has no trace-norm limit which is a normal state, and its mass on every fixed finite-rank projection tends to zero. The prime occupation process at $0<\beta\leq1$, with positive summable up rates and down rates $r_pp^\beta$, has no stationary probability on finite-support configurations. These statements do not prove “ergodicity breaking” of a Riemann Lindbladian.

Status: analytic and classical assertions `proved-here`; arithmetic comparison `conditional-on H-BC-POS`.

⟨1⟩1. **Show escape of the Gibbs mass.**

PROOF: Monotone convergence of $\sum n^{-\beta}$ to the divergent harmonic series gives $\zeta(\beta)\to\infty$. Also $\|\rho_\beta\|\leq1/\zeta(\beta)$. Thus for every finite-rank projection $P$, $\operatorname{Tr}(P\rho_\beta)\leq\operatorname{rank}(P)/\zeta(\beta)\to0$. A trace-norm limit would have trace one and vanish on all finite-rank projections, impossible for a positive trace-class operator. In fact its pairing with every compact operator tends to zero by finite-rank approximation.

⟨1⟩2. **Exclude a normal classical stationary law below the threshold.**

PROOF: Stationarity would force every finite collection of occupations to have its product geometric law with occupancy probabilities $p^{-\beta}$. For $0<\beta\leq1$, $\sum_p p^{-\beta}=\infty$. At $\beta=1$ this follows from the Euler product and divergence of the harmonic series: if $\sum_p1/p$ converged, the products $\prod_{p\leq P}(1-1/p)^{-1}$ would be bounded, while they eventually dominate every harmonic partial sum. Smaller positive $\beta$ only increases the sum. Independence then implies infinitely many occupied primes almost surely: the probability that all primes outside any fixed finite set are empty is the product $\prod(1-p^{-\beta})=0$, and take a countable union over those sets. This contradicts support on integers. At $\beta\leq0$, even one local chain has no summable stationary geometric law. A stationary density for a quantum extension preserving this diagonal dynamics would in particular give a stationary diagonal probability, so cannot exist either.

⟨1⟩3. **State what the transition establishes.**

PROOF: Loss of normalizability of a stationary law is a precise conclusion. It is not a proof of a spectral-gap closing, multiple stationary states of a specified Lindbladian, or its loss of dynamical ergodicity. H-BC-POS's unique high-temperature arithmetic state lives in a different representation. In particular it cannot be identified with the pure absorbing vacuum density of T5, or with a normal critical bond density by this calculation. The prime Gibbs chain supplies ring-length energies and an independent reversible relaxation model; it supplies no construction of the Riemann zero bond in T4. $\square$

## T7. Artin--Schreier: a general sign law and a corrected super-transfer

The supplied module `scripts/artin_schreier_mps.py` was read before these calculations. Its matrix convention is **output row, input column**. Its docstring's point count is affine; the projective count below includes the additional one. Throughout $q$ is an odd prime, $\psi(c)=\exp(2\pi i c/q)$, $\eta$ is the quadratic character, and
$$
g(x)=\sum_{j=0}^J a_jx^{1+q^j},\qquad a_J\ne0.
$$
For $J\geq1$ use exactly the matrix in the question, acting by
$$
\tag{7.1}
E_g|s_1,\ldots,s_J\rangle
=\sum_{x\in\mathbb F_q}\psi\left(a_0x^2+\sum_{j=1}^Ja_js_{J+1-j}x\right)
|s_2,\ldots,s_J,x\rangle.
$$
For $J=0$ there is one bond state and the correct matrix is the scalar
$E_g=\sum_x\psi(a_0x^2)$. The module instead retains a redundant $q$-state register when $J=0$; its positive-power traces agree with this scalar but it has extra zero eigenvalues. All $q^J$-dimensional and scaled-unitary assertions use the minimal convention just specified.

**H-GAUSS (quadratic Gauss sums; supplied statement).** “For $q$ an odd prime and a quadratic form $Q$ on $\mathbb F_q^n$ of rank $r$,
$$
\sum_x\psi(Q(x))=q^{n-r}\eta(\det Q_{\rm nd})\,\mathfrak g(\psi)^r,
$$
with $Q_{\rm nd}$ the nondegenerate part, $\eta$ the quadratic character of $\mathbb F_q^*$, $\mathfrak g(\psi)=\sum_c\psi(c^2)$, $\mathfrak g(\psi)^2=\eta(-1)q$, $\overline{\mathfrak g(\psi)}=\eta(-1)\mathfrak g(\psi)$.” For rank zero the determinant and its character are one. We use the determinant of the matrix in $Q(x)=x^tAx$, not the determinant of $2A$.

**H-STICK (Stickelberger; supplied statement).** “The discriminant of the trace form of $\mathbb F_{q^n}/\mathbb F_q$, $q$ odd, is a square in $\mathbb F_q$ iff $n$ is odd; equivalently $\eta(\operatorname{disc})=(-1)^{n-1}$ = the sign of the $n$-cycle by which Frobenius permutes the conjugates.” This will follow from the embedding-matrix calculation below, conditional on a normal basis.

**H-NORMAL (normal-basis theorem; supplied statement).** “Normal basis theorem; the self-dual normal basis exists for $n$ odd ($q$ odd).” Precisely, $\mathbb F_{q^n}$ has an $\mathbb F_q$-basis $\theta,\theta^q,\ldots,\theta^{q^{n-1}}$; for odd $n$ it can be chosen with $\operatorname{tr}(\theta^{q^i}\theta^{q^j})=\delta_{ij}$. Only the normal-basis part is needed for the general sign proof.

**H-WEIL-REP (finite Weil representation; supplied wording).** “The Weil representation $W$ of $\operatorname{Sp}(2J,\mathbb F_q)$, $q$ odd, on $L^2(\mathbb F_q^J)$: a genuine unitary representation, characterised up to a character by $W(M)X_vW(M)^{-1}=(\mathrm{phase})X_{Mv}$ for the Weyl (Heisenberg) operators $X_v$, $v\in\mathbb F_q^{2J}$; its character satisfies $|\operatorname{Tr}W(M)|^2=q^{\dim\ker(M-1)}$.”

The arbitrary word “phase” in that characterization is insufficient: multiplication by a noncentral Weyl displacement preserves such a projective covariance statement and can change traces. The precise input used for the identification with $W$ is the following standard normalization.

**H-WEIL-EXACT (centered Weyl covariance; additional precision).** With centered Weyl operators
$$
X_{u,v}|s\rangle=\psi\big(v\cdot(s+u/2)\big)|s+u\rangle,
$$
there exists a genuine unitary Weil representation satisfying
$$
W(M)X_{u,v}W(M)^{-1}=X_{M(u,v)}
$$
exactly. For a fixed $M$, its implementer is unique up to a scalar of modulus one. The character-modulus formula in H-WEIL-REP will be proved directly for every such implementer below, without assuming it separately.

**H-AS (additive-character polynomiality; supplied context made explicit).** For the specified polynomial of degree $d=q^J+1$, prime to $q$, and every $a\in\mathbb F_q^*$,
$$
L(ag,T)=\exp\left(\sum_{n\geq1}\frac{S_n(ag)T^n}{n}\right)
$$
is a polynomial over $\mathbb C$ of degree exactly $d-1=q^J$, with constant term one. This is the standard Artin--Schreier character $L$-polynomial theorem. Polynomiality is arithmetic input; it is not assumed to follow from an incorrect transfer sign. We do not assume the sizes of its reciprocal roots in H-AS.

**H-FROB-SS (semisimplicity for curve $H^1$; additional input only for operator similarity).** The Frobenius action on $H^1$ of a smooth projective curve over a finite field is semisimple over an algebraic closure of the coefficient field. After choosing a complex realization of its algebraic eigenvalues and transporting its Jordan form, the resulting complex matrix is therefore similar to a diagonal matrix with those eigenvalues. No positive Hermitian metric on the original cohomological realization is part of this hypothesis.

**Lemma T7.1 (Gauss evaluation, including nonvanishing).**

Hypotheses: $q$ odd, a homogeneous quadratic form on $\mathbb F_q^n$.

Claim: H-GAUSS holds. In particular every such sum is nonzero and, with $d=\dim\operatorname{rad}Q=n-r$,
$$
|\sum_x\psi(Q(x))|^2=q^{n+d},
\qquad
\overline{\sum_x\psi(Q(x))}=\eta(-1)^r\sum_x\psi(Q(x)).
$$

Status: `proved-here`.

⟨1⟩1. **Diagonalize by congruence.**

PROOF: A symmetric matrix over a field of odd characteristic can be reduced to diagonal form by successively splitting off a vector with nonzero quadratic value. If a nonzero symmetric matrix has no nonzero diagonal value in a current basis but has a nonzero off-diagonal entry, the sum of the corresponding basis vectors has nonzero quadratic value because $2\ne0$. Splitting its orthogonal complement and continuing yields $r$ nonzero diagonal entries and $n-r$ zero entries. Basis changes change their product only by a square.

⟨1⟩2. **Evaluate one-dimensional sums and their phase.**

PROOF: For $a\ne0$, counting the two square roots of each nonzero square gives
$$
\sum_x\psi(ax^2)=\sum_{y\in\mathbb F_q}(1+\eta(y))\psi(ay)
=\eta(a)\mathfrak g(\psi),
$$
where $\eta(0)=0$ and $\sum_y\psi(ay)=0$. Taking $a=-1$ gives $\overline{\mathfrak g}=\eta(-1)\mathfrak g$. The bijection $(x,y)\mapsto(x-y,x+y)$ gives
$$
|\mathfrak g|^2=\sum_{x,y}\psi(x^2-y^2)=\sum_{u,v}\psi(uv)=q.
$$
Together these give $\mathfrak g^2=\eta(-1)q$. Multiplying the one-dimensional sums, with a factor $q$ per radical coordinate, proves all assertions. $\square$

**Lemma T7.2 (ring and trace quadratic forms for every $n$).**

Hypotheses: (7.1), H-NORMAL, any integer $n\geq1$. On $V=\mathbb F_q^n$ use cyclic indices modulo $n$, let $(Sx)_i=x_{i+1}$, and put
$$
P(z)=\sum_{j=0}^J\frac{a_j}{2}(z^j+z^{-j}),\qquad M=P(S).
$$
Choose a normal generator $\theta$, set $c_m=\operatorname{tr}(\theta\theta^{q^m})$, and let $C_{ik}=c_{k-i}$. Then $C$ is symmetric, invertible, and commutes with $S$ and $M$.

Claims:
$$
\tag{7.2}
t_n:=\operatorname{Tr}E_g^n=\sum_{x\in V}\psi(Q_g^\circ(x)),
\qquad
Q_g^\circ(x)=\sum_{j=0}^Ja_j\sum_{i\bmod n}x_ix_{i+j}=x^tMx,
$$
$$
\tag{7.3}
S_n(g)=\sum_{x\in V}\psi(Q_g^{\rm tr}(x)),\qquad
Q_g^{\rm tr}(x)=\sum_{j=0}^Ja_j\sum_{i,k\bmod n}x_ix_kc_{k+j-i}
=x^tCMx.
$$
Their radicals have common dimension $d_n=\dim\ker M$. Consequently the $d_n$ defined by $\log_q(|S_n(g)|^2/q^n)$ is always this nonnegative integer, and $|S_n(g)|=|t_n|$.

Status: ring formula `proved-here`; normal-coordinate and rank assertions `conditional-on H-NORMAL`.

⟨1⟩1. **Enumerate cyclic transfer paths, including short rings.**

PROOF: A closed path of $n$ transitions in (7.1) is determined by the ordered list of newly inserted spins $(x_i)_{i\bmod n}$. Its state just before inserting $x_i$ must be $(x_{i-J},\ldots,x_{i-1})$. Conversely these states define a closed path for every list of spins. This is a bijection of marked cyclic paths and ordered configurations, also for $n\leq J$: repeated indices then impose precisely the required wraparound repetitions. Summing the transition phases gives $\sum_i[a_0x_i^2+\sum_{j\geq1}a_jx_{i-j}x_i]$, which equals $Q_g^\circ$. No division by $n$ or by a stabilizer is appropriate for a matrix trace. For $J=0$ the scalar transfer gives the same independent-site sum.

⟨1⟩2. **Compute the normal-basis coefficients.**

PROOF: For $z=\sum_i x_i\theta^{q^i}$,
$$
\operatorname{tr}(z z^{q^j})
=\sum_{i,k}x_ix_k\operatorname{tr}(\theta^{q^i}\theta^{q^{k+j}})
=\sum_{i,k}x_ix_kc_{k+j-i}.
$$
The trace pairing is nondegenerate for the separable finite-field extension, and $C$ is its Gram matrix in a basis, hence invertible. This can also be seen from the invertible conjugate-embedding matrix used in T7.3. Trace invariance gives $c_m=c_{-m}$, proving symmetry; the dependence only on $k-i$ proves the commuting circulant assertion. The unsymmetrized $j$ term has matrix $CS^{-j}$ in this shift convention. Its symmetric part is $C(S^j+S^{-j})/2$, proving the last equality in (7.3) and all factors of two.

⟨1⟩3. **Compare radicals and magnitudes.**

PROOF: Since $C$ is invertible and commutes with $M$, $\ker(CM)=\ker M$. Apply T7.1 to the two rank-$n-d_n$ forms to get magnitude squared $q^{n+d_n}$ for each. In particular neither trace vanishes, so every sign ratio used below is defined. $\square$

**Theorem T7.3 (the corrected sign law, including $q\mid n$).**

Hypotheses: those of T7.2. Let $R_n=\ker P(S)$ and let
$$
\delta_n=\det(S|R_n)\in\{+1,-1\},
$$
with determinant one when $R_n=0$. The signs are regarded as the integers $\pm1$ when multiplying complex sums.

Claim:
$$
\boxed{\displaystyle
\tag{7.4}
S_n(g)=(-1)^{n-1}\delta_n\operatorname{Tr}E_g^n.}
$$
Equivalently, with $r_n=n-d_n$ and $E_{-g}=\overline{E_g}$ entrywise,
$$
\tag{7.5}
S_n(g)=(-1)^{n-1}\delta_n\eta(-1)^{n-d_n}\operatorname{Tr}E_{-g}^n.
$$
The draft's law is valid at a particular $n$ if and only if $\delta_n=\eta(-1)^{d_n}$. That equality is not automatic.

Status: `conditional-on H-NORMAL`; H-GAUSS and H-STICK are proved here, rather than additional independent inputs to this result.

⟨1⟩1. **Construct a square root of the Gram matrix over the algebraic closure.**

PROOF: Regard all conjugates of $\theta$ in $\overline{\mathbb F}_q$ and form the symmetric matrix
$$
A_{ri}=\theta^{q^{r+i}},\qquad r,i\bmod n.
$$
It is invertible. Indeed the distinct field embeddings are linearly independent as functions on the extension: a shortest nonzero relation among embeddings, evaluated at $xy$ and subtracted from one of its values at $x$ times the relation at $y$, would shorten it by choosing $x$ on which two embeddings differ. A relation among the rows of $A$ on the basis would be such a relation on the whole field. Direct multiplication gives
$$
A^t=A,\qquad A^2=C,\qquad A^{[q]}=SA,\qquad AS=S^{-1}A,
$$
where $[q]$ means entrywise Frobenius. These identities are valid even when $q\mid n$; they use cyclic indices, not diagonalization of $S$.

⟨1⟩2. **Compute determinant square classes on the radical.**

PROOF: $P(S^{-1})=P(S)$, so $A$ preserves $R_n\otimes\overline{\mathbb F}_q$. Choose an $\mathbb F_q$-basis of $R_n$ and write $D=\det(A|R_n)$ in that basis. Then
$$
\det(C|R_n)=D^2,\qquad D^q=\det(S|R_n)D.
$$
It follows that
$$
\eta(\det(C|R_n))=(D^2)^{(q-1)/2}=D^{q-1}=\det(S|R_n).
$$
In particular the last determinant is indeed $\pm1$. Applying the same argument to all of $V$ gives
$$
\eta(\det C)=\det S=(-1)^{n-1},
$$
which proves H-STICK from H-NORMAL and elementary embedding algebra. This proof also treats the potentially degenerate restriction of the ordinary dot product to $R_n$: no nondegenerate dot-product restriction has been assumed.

⟨1⟩3. **Compare the nondegenerate quotient forms.**

PROOF: Both forms in T7.2 descend to nondegenerate forms on $V/R_n$. The second is obtained from the first by applying the induced $\overline C$ in one argument. Thus the ratio of their determinants, in a common quotient basis, is $\det\overline C$. Since $C$ preserves $R_n$,
$$
\det\overline C=\frac{\det C}{\det(C|R_n)},
\qquad
\eta(\det\overline C)=(-1)^{n-1}\delta_n.
$$
The two Gauss sums have the same radical factor and the same power $\mathfrak g^{r_n}$, so T7.1 gives (7.4). Conjugating $t_n$ multiplies it by $\eta(-1)^{r_n}$, giving (7.5). Simplifying the draft's expression $-(-\eta(-1))^n\overline{t_n}$ yields $(-1)^{n-1}\eta(-1)^{d_n}t_n$; comparison with (7.4) proves the exact criterion. $\square$

**Corollary T7.4 (an explicit periodic sign and the exact endpoint conditions).**

Hypotheses: T7.3. Define the nonzero polynomial
$$
f(z)=z^JP(z),
$$
using $f=a_0$ if $J=0$. Let $v_-$ and $v_+$ be its vanishing orders at $-1$ and $1$. Let $h=q^a$ be the smallest power of $q$ strictly greater than $v_-$ (in particular $h=1$ when $v_-=0$).

Claims:
$$
\tag{7.6}
\delta_n=
\begin{cases}
1,&n\text{ odd},\\
(-1)^{\min(v_-,q^{v_q(n)})},&n\text{ even},
\end{cases}
\qquad
\boxed{\displaystyle S_n(g)=(1-2\mathbf1_{2h\mid n})t_n.}
$$
The orders $v_\pm$ are even. The original notebook claim $\alpha_i=-\lambda_i(E_g)$ for the character $L$-polynomial holds for every $n$ exactly when
$$
\tag{7.7}
P(-1)=\sum_j(-1)^ja_j\ne0.
$$
The draft's replacement $S_n(g)=-(-\eta(-1))^n\operatorname{Tr}E_{-g}^n$ holds for all $n$ exactly when
$$
\tag{7.8}
P(-\eta(-1))\ne0.
$$
For the claim involving $\alpha_i$ use H-AS as well.

Status: sign assertions `conditional-on H-NORMAL`; $L$-polynomial identification additionally `conditional-on H-AS`.

⟨1⟩1. **Compute the radical as a cyclic module.**

PROOF: $S$ is a cyclic operator with characteristic and minimal polynomial $z^n-1$, so $V\simeq\mathbb F_q[z]/(z^n-1)$. The kernel of multiplication by $P(S)$ is the kernel of multiplication by $f(S)$, since $S$ is invertible. On a primary factor $(z-\xi)^e$ over the algebraic closure, the kernel has dimension $\min(\operatorname{ord}_\xi f,e)$ and the restricted shift has that many occurrences of eigenvalue $\xi$. This follows directly by multiplying powers of $z-\xi$ in the local quotient, so includes nonsemisimple factors. The characteristic polynomial of $S|R_n$ is therefore the monic $\gcd(f,z^n-1)$.

⟨1⟩2. **Isolate the minus-one contribution.**

PROOF: $P(z)=P(z^{-1})$. Away from $\pm1$, roots of $f$ occur in inverse pairs with equal orders; roots of $z^n-1$ do too. Their contributions to $\det(S|R_n)$ multiply to one. Eigenvalue $1$ contributes one. If $n$ is even, $-1$ has multiplicity $e=q^{v_q(n)}$ in $z^n-1$, because $z^n-1=(z^{n/e}-1)^e$ and $q\nmid n/e$. This proves the first formula in (7.6); for odd $n$ there is no minus-one root.

Near $1$, the parameter $w=(z-1)/(z+1)$ changes to $-w$ under inversion; near $-1$ use $w=(z+1)/(z-1)$. The denominators are units because $q$ is odd. Invariance of $P$ makes its local series even in $w$, so each finite vanishing order $v_\pm$ is even. Multiplication by the local unit $z^J$ does not change the order. Since $e$ is odd, $\min(v_-,e)$ is odd precisely when $e<v_-$, equivalently $e\leq v_-$, whereas it is even when $e>v_-$. By the definition of $h$, $e>v_-$ is equivalent to $h\mid n$. Combining with $(-1)^{n-1}$ in (7.4) proves the boxed periodic sign.

⟨1⟩3. **Prove the two endpoint criteria.**

PROOF: The identity $S_n=(-1)^{n-1}t_n$ holds for all $n$ if $v_-=0$. If $v_->0$, then at $n=2$ the radical minus-one multiplicity is one, so the sign is $+1$ instead of $-1$; $t_2\ne0$ by T7.2. This proves (7.7) as a trace identity and, using the determinant logarithm and H-AS, as a Frobenius eigenvalue identity.

If $\eta(-1)=1$, the draft's law requires $\delta_n=1$ for all $n$, exactly the same condition $v_-=0$. If $\eta(-1)=-1$, its condition is $\delta_n=(-1)^{d_n}$. All roots other than $\pm1$ contribute an even total dimension to $R_n$, so
$$
d_n\equiv \min(v_+,q^{v_q(n)})+mathbf1_{2\mid n}\min(v_-,q^{v_q(n)})\pmod2.
$$
Thus $v_+=0$ suffices. If $v_+>0$, at $n=1$ the radical is one dimensional, so $\delta_1=1\ne-1=(-1)^{d_1}$. This proves (7.8). The criterion is a property of the coefficients, not a prohibition on $q\mid n$. $\square$

**Proposition T7.5 (decisive counterexamples and bounded numerical checks).**

Hypotheses: the explicitly specified small fields and polynomials; the formulas above for the general interpretation.

Claims: both proposed universal sign laws in the question are false without the endpoint restriction (7.8). The failure already occurs for $n$ prime to $q$.

Status: counterexamples `proved-here`; floating-point comparisons are sanity checks, not proof inputs.

⟨1⟩1. **Give an exact one-site counterexample.**

PROOF: For $q=3$, $a=(2,1)$ and $n=1$, $g(x)=2x^2+x^4=0$ as a function on $\mathbb F_3$. Therefore $S_1=3$. The one-site cyclic energy is $(2+1)x^2=0$, so $t_1=3$ as well and $d_1=1$. Since $\eta(-1)=-1$, the draft's conjugated expression is $-\overline{t_1}=-3$. Here $P(1)=0$, $P(-1)=1$, so the actual uniform law is the original alternating one, $S_n=(-1)^{n-1}t_n$.

⟨1⟩2. **Give a counterexample in the other quadratic-character class.**

PROOF: For $q=5$, $a=(1,1)$ and $n=2$,
$$
Q^\circ(x_0,x_1)=(x_0+x_1)^2,
\qquad t_2=5\sqrt5.
$$
Writing $z=a+b\sqrt2$ in $\mathbb F_{25}$, Frobenius sends $\sqrt2$ to $-\sqrt2$. Then $\operatorname{tr}(z^2+z^6)=4a^2$, giving $S_2=5\sqrt5$ as well. The asserted law for $\eta(-1)=1$ would give $-5\sqrt5$. This time $P(-1)=0$, $v_-=2$, $h=5$; the correct sign changes to minus exactly when $10\mid n$.

⟨1⟩3. **Record the actual computations.**

PROOF: Direct calls to the supplied `S_bruteforce` and `transfer` confirmed the preceding cases and the following additional values (the displayed radicals give their exact interpretations):

| $q$ | coefficients | $n$ | $S_n$ | $t_n$ | $d_n$ |
|---|---|---:|---:|---:|---:|
| 3 | $(2,1)$ | 1 | $3$ | $3$ | 1 |
| 3 | $(2,1)$ | 2 | $3i\sqrt3$ | $-3i\sqrt3$ | 1 |
| 3 | $(1,1)$ | 2 | $3i\sqrt3$ | $3i\sqrt3$ | 1 |
| 3 | $(1,1)$ | 6 | $81$ | $-81$ | 2 |
| 3 | $(0,1,1)$ | 6 | $-81i\sqrt3$ | $-81i\sqrt3$ | 3 |
| 5 | $(1,1)$ | 2 | $5\sqrt5$ | $5\sqrt5$ | 1 |

A further standard-input Python check built the exact trace quadratic matrices in polynomial bases, using the module's irreducible polynomials, field multiplication, Frobenius powers, and traces. Modular congruence elimination gave their ranks and determinants; T7.1 evaluated their sums. These were compared with the transfer traces and the sign $1-2\mathbf1_{2h\mid n}$. The test covered all $6$ degree-range-one coefficient tuples and all $18$ range-two tuples over $\mathbb F_3$ for $1\leq n\leq9$, all $20$ range-one tuples over $\mathbb F_5$ for $1\leq n\leq8$, and all $42$ range-one tuples over $\mathbb F_7$ for $1\leq n\leq6$: **628 comparisons**, including characteristic-divisible $n$. The largest relative numerical residual was $8.30\times10^{-15}$. The exact proof is T7.3--T7.4, and does not extrapolate these tests. $\square$

**Theorem T7.6 (scaled unitarity with complete indices).**

Hypotheses: $q$ odd, (7.1), $a_J\ne0$, using the minimal $J=0$ convention.

Claim: $E_gE_g^\dagger=qI_{q^J}$. Thus $E_g/\sqrt q$ is unitary and its $q^J$ eigenvalues are all nonzero, semisimple, and of modulus $\sqrt q$. Also $E_{-g}=\overline{E_g}$ entrywise.

Status: `proved-here`.

⟨1⟩1. **Compute the row inner products when $J\geq1$.**

PROOF: Write an output state as $y=(u_1,\ldots,u_{J-1},x)$. Its possible input columns are exactly $s=(z,u_1,\ldots,u_{J-1})$, $z\in\mathbb F_q$. Two rows $y=(u,x)$ and $y'=(u',x')$ have common nonzero columns only if $u=u'$. When this holds their inner product is
$$
\begin{aligned}
(E_gE_g^\dagger)_{y,y'}
={}&\psi\left(a_0(x^2-x'^2)
+(x-x')\sum_{j=1}^{J-1}a_j u_{J-j}\right)
\sum_{z\in\mathbb F_q}\psi\big(a_Jz(x-x')\big).
\end{aligned}
$$
The last sum is $q\mathbf1_{x=x'}$ because $a_J\ne0$. If $x=x'$ the preceding phase is one. Hence the product is $q\mathbf1_{y=y'}$. For $J=1$ the $u$ tuple and its sum are empty and the same calculation applies. This is $EE^\dagger$ in the output-row convention; the index being summed is precisely the oldest input spin $z$.

⟨1⟩2. **Handle range zero and the remaining assertions.**

PROOF: For $J=0$, T7.1 gives $|E_g|^2=q$. In every case the square matrix satisfying $EE^\dagger=qI$ has inverse $E^\dagger/q$, so it is $\sqrt q$ times a unitary. The finite-dimensional unitary spectral theorem gives the asserted eigenvalue properties. Complex conjugation negates every phase in (7.1), and also in the range-zero sum. $\square$

**Theorem T7.7 (the corrected polynomial and an explicit fixed Frobenius spectrum).**

Hypotheses: H-NORMAL, H-AS, the coefficient conditions of T7.4; use the proved T7.6. Write $D=q^J$, $D_g(T)=\det(I-TE_g)$, and let $m_E(z)$ be the spectral multiplicity of $z$ in $E_g$ (zero outside its spectrum). Retain the integer $h$ from T7.4.

Claims:
$$
\boxed{\displaystyle
\tag{7.9}
L(g,T)^h=
\frac{\prod_{\omega^{2h}=1}D_g(\omega T)}{D_g(T)^h}.}
$$
Equivalently, $[L(g,T)D_g(T)]^h=\det(I-T^{2h}E_g^{2h})$.
The polynomial $L(g,T)$ is the unique germ at zero with value one satisfying (7.9). Its reciprocal-root multiplicity at $z\ne0$ is exactly
$$
\boxed{\displaystyle
\tag{7.10}
m_{F_g}(z)=\frac1h\sum_{\omega^{2h}=1}m_E(\omega^{-1}z)-m_E(z).}
$$
These are nonnegative integers, supported on finitely many numbers of modulus $\sqrt q$, and sum to $D$. Thus a concrete corrected character transfer is the diagonal $D\times D$ matrix $F_g$ with multiplicities (7.10); it satisfies
$$
F_gF_g^\dagger=qI,
\qquad
L(g,T)=\det(I-TF_g),
\qquad
S_n(g)=-\operatorname{Tr}F_g^n\quad(n\geq1).
$$
The construction is finite: diagonalize the given finite $E_g$, rotate its eigenvalue multiset by the $2h$ roots of unity, and use (7.10). The integrality and absence of negative multiplicities use H-AS.

If $P(-1)\ne0$, one can simply take $F_g=-E_g$, and $L(g,T)=\det(I+TE_g)$. If the weaker/different endpoint condition $P(-\eta(-1))\ne0$ holds, one can take $F_g=-\eta(-1)E_{-g}$, giving the draft's determinant
$$
L(g,T)=\det(I+\eta(-1)TE_{-g}).
$$
That latter formula is not an unconditional identity.

Status: `conditional-on H-NORMAL, H-AS`; no Weil root-size input is used.

⟨1⟩1. **Filter powers by roots of unity.**

PROOF: For $|T|$ small enough,
$$
\log D_g(T)=-\sum_{n\geq1}\frac{t_nT^n}{n},
\qquad
\sum_{\omega^{2h}=1}\omega^n=2h\mathbf1_{2h\mid n}.
$$
Using the sign in (7.6) gives
$$
\log L(g,T)
=-\log D_g(T)+\frac1h\sum_{\omega^{2h}=1}\log D_g(\omega T).
$$
Exponentiate $h$ times to obtain (7.9) as a germ. The scalar identity $\prod_{\omega^{2h}=1}(1-\omega z)=1-z^{2h}$, applied to every eigenvalue, gives the equivalent determinant with $E_g^{2h}$. Since H-AS makes $L$ a polynomial, this is a rational-function identity globally. A normalized analytic $h$th root near zero is unique, by its logarithm or the implicit-function theorem.

⟨1⟩2. **Read every multiplicity.**

PROOF: At $T=1/z$, the order of $D_g(\omega T)$ is $m_E(\omega^{-1}z)$. Taking orders in (7.9) yields (7.10). H-AS says that the left side has only nonnegative orders divisible by $h$, proving the claimed integrality and nonnegativity. Every possible support value is a roots-of-unity rotation of an eigenvalue of $E_g$; T7.6 puts it on the $\sqrt q$ circle. Summing (7.10) over its finite support gives
$$
\sum_zm_{F_g}(z)=\frac{2h}{h}D-D=D.
$$
Thus the constructed matrix has exactly the required size and is scaled unitary. Its determinant and $L$ have the same zeros, degree, and value at zero, so agree. Taking logarithms gives every trace identity. Without polynomiality, (7.9) alone would give rational multiplicities that could in principle be negative or nonintegral; that arithmetic step has not been concealed.

⟨1⟩3. **Recover and delimit the simpler formulas.**

PROOF: When $h=1$, (7.9) reduces to $L=D_g(-T)$, or use (7.7) directly. Under (7.8), (7.5) has the draft's simpler constant-phase form and determinant logarithms give its determinant formula. In this restricted situation the requested comparison with the original notebook formula is valid algebra:
$$
\{-\lambda_i(E_g)\}=\{-\eta(-1)\overline{\lambda_i(E_g)}\}
$$
if and only if $\operatorname{spec}E_g$ is conjugation invariant for $\eta(-1)=1$, or equals $-\overline{\operatorname{spec}E_g}$ for $\eta(-1)=-1$, with multiplicities. Without (7.8) the premise identifying the second multiset with Frobenius is false, so those tests are not unconditional tests for the notebook claim. Its unconditional coefficient criterion is (7.7). $\square$

For clarity, both directions of the proposed unconditional spectral test can fail. For $q=5$, $a=(1,1)$, T7.1 makes every $t_n$ real, so finite power-trace uniqueness makes $\operatorname{spec}E_g$ conjugation invariant; nevertheless $P(-1)=0$ and the original notebook claim fails. For $q=3$, $a=(2,1)$, $P(-1)\ne0$ makes the original claim true, while $\operatorname{Tr}E_g=3\ne-3=\operatorname{Tr}(-\overline{E_g})$, so the proposed spectral symmetry fails.

**Theorem T7.8 (a corrected projective super-transfer).**

Hypotheses: H-NORMAL, H-AS; the preceding finite-field definitions. For the identification with cohomology also use H-WEIL, and for similarity of operators also H-FROB-SS. Let $E_0$ be the zero-phase de Bruijn adjacency matrix of memory $J$, or the scalar $q$ when $J=0$. For each $a\in\mathbb F_q^*$ construct $F_{ag}$ by T7.7, and set
$$
\tag{7.11}
\mathbb E=(E_0\oplus1)_{\rm even}\oplus
\left(\bigoplus_{a\in\mathbb F_q^*}F_{ag}\right)_{\rm odd}.
$$

Claims: the smooth projective curve $C:y^q-y=g(x)$ has one rational point at infinity and
$$
\tag{7.12}
N_n=\#C(\mathbb F_{q^n})=1+q^n+\sum_{a\ne0}S_n(ag)
=\operatorname{str}\mathbb E^n\quad(n\geq1).
$$
The odd block $F$ in (7.11) satisfies $FF^\dagger=qI_{(q-1)q^J}$. Its multiset is exactly the $2g(C)=(q-1)q^J$ Frobenius eigenvalue multiset, with no nonzero even--odd cancellation. The even block $E_0$ can be reduced, as far as positive-power traces are concerned, to the scalar $q$; its extra zero eigenvalues are invisible. Under H-FROB-SS the complex odd operator is similar to the Frobenius realization on $H^1$.

Under the extra endpoint condition (7.8), the draft's simpler odd block $-\eta(-1)\bigoplus_{a\ne0}E_{ag}$ is valid as well. It is false in general under $a_J\ne0$ alone.

Status: counting and transfer construction `conditional-on H-NORMAL, H-AS`; identification with $H^1$ additionally `conditional-on H-WEIL`; operator similarity additionally `conditional-on H-FROB-SS`.

⟨1⟩1. **Prove the affine count directly.**

PROOF: On $\mathbb F_{q^n}$ the map $y\mapsto y^q-y$ is $\mathbb F_q$-linear with kernel $\mathbb F_q$, hence image of dimension $n-1$. Its image has trace zero by telescoping. The trace map is nonzero: for a normal generator, $\operatorname{tr}\theta=\sum_i\theta^{q^i}\ne0$ by linear independence of the normal basis. Thus its kernel also has dimension $n-1$, so it is exactly that image. Every fiber over an image point has $q$ elements. Character orthogonality then gives
$$
q\mathbf1_{\operatorname{tr}g(x)=0}
=\sum_{a\in\mathbb F_q}\psi(a\operatorname{tr}g(x)).
$$
Sum over $x$ to obtain the affine count $q^n+\sum_{a\ne0}S_n(ag)$. This proves the required additive Hilbert-90 assertion in this case.

⟨1⟩2. **Account for infinity.**

PROOF: The polynomial has degree $d=q^J+1$ prime to $q$. It cannot equal $h^q-h$ for a rational function over $\overline{\mathbb F}_q$: a pole of $h$ of order $m>0$ would give a pole of order $qm$, whereas the sole pole of $g$ is of order $d$. The Artin--Schreier polynomial is therefore irreducible over $\overline{\mathbb F}_q(x)$: for prime $q$, translations of a root by $\mathbb F_q$ give a Galois group whose only possible orders are $1$ and $q$, and order one would give such a rational root. The curve is geometrically connected. At a place above the pole of $x$, with ramification index $e$, $y$ has a pole and the equation gives $q\operatorname{ord}(y)=-de$. Since $q\nmid d$, this forces $q\mid e$, hence $e=q$. The degree-$q$ extension can therefore have only one such place, with residue degree one. It supplies one rational point on the smooth projective normalization, over every extension field. This proves the additional one in (7.12).

⟨1⟩3. **Compute the zero-phase trace.**

PROOF: The closed-path bijection of T7.2 with every weight one gives $\operatorname{Tr}E_0^n=q^n$, including $n\leq J$. For $J\geq1$, after $J$ transitions any input word can reach any output word by exactly one prescribed sequence of inserted letters, so $E_0^J$ is the all-ones matrix. Moreover $E_0^{J+1}=qE_0^J$. Thus the only possible nonzero eigenvalue is $q$ and it has multiplicity one (also forced by the first trace); all other eigenvalues are zero, possibly with nilpotent blocks. For $J=0$, $E_0=q$ by definition.

⟨1⟩4. **Assemble the count and check multiplicities.**

PROOF: T7.7 gives $-\operatorname{Tr}F_{ag}^n=S_n(ag)$, and step ⟨1⟩3 gives the even traces. This proves (7.12), and the direct sum of the identities $F_{ag}F_{ag}^\dagger=qI_D$ gives scaled unitarity of the odd block. Exponentiating (7.12) gives
$$
Z_C(T)=\frac{\prod_{a\ne0}L(ag,T)}{(1-T)(1-qT)}.
$$
The numerator has degree $(q-1)D$ and all reciprocal roots have modulus $\sqrt q$, so none cancels with either denominator factor. Comparing with H-WEIL identifies this numerator with the Frobenius polynomial and gives $2g(C)=(q-1)D$. T3.2 forces the same nonzero net odd multiset in any finite graded realization of these counts. Semisimplicity of the explicitly built $F$ is automatic; turning spectral equality into similarity with the cohomological operator additionally uses H-FROB-SS. Trace identities alone never determine Jordan blocks.

⟨1⟩5. **Delimit the draft's block and disprove its unrestricted version.**

PROOF: Under (7.8), one may use $F_{ag}=-\eta(-1)E_{-ag}$. Since $a\mapsto-a$ permutes $\mathbb F_q^*$, the full direct sum is, after a block permutation, the draft's $-\eta(-1)\bigoplus_aE_{ag}$. Its unitarity follows from T7.6.

Without that condition take $q=3$ and $g=2x^2+x^4$. At $n=1$ all three $x$ have $g(x)=0$, and all three $y$ satisfy $y^3-y=0$, so $N_1=9+1=10$. Both nonzero character sums and both corresponding transfer traces are $3$. The draft puts the two $E$ blocks in the odd sector with scalar $-\eta(-1)=+1$, and would give $3+1-3-3=-2$. This exact count disproves that proposed universal super-transfer. The corrected (7.11), here with $F_{ag}=-E_{ag}$, gives $3+1+3+3=10$. $\square$

**Theorem T7.9 (the explicit symplectic map and Weil implementer).**

Hypotheses: $J\geq1$, $a_J\ne0$, $q$ odd, the centered Weyl convention in H-WEIL-EXACT. For identification with the named representation assume H-WEIL-EXACT. Put $c=a_J$ and $U_g=E_g/\sqrt q$.

Claim: $U_gX_{u,v}U_g^{-1}=X_{M_g(u,v)}$ exactly, where the explicit linear map $M_g$ is
$$
\tag{7.13}
\begin{aligned}
u'_k&=u_{k+1} &&(1\leq k<J),& u'_J&=-v_1/c,\\
v'_k&=v_{k+1}+a_{J-k}u'_J &&(1\leq k<J),&
v'_J&=cu_1+\sum_{k=2}^Ja_{J+1-k}u_k+2a_0u'_J.
\end{aligned}
$$
All coefficients and inverses in (7.13) are in $\mathbb F_q$. This formula specifies the full $2J\times2J$ matrix. It preserves the symplectic form $u\cdot\widetilde v-v\cdot\widetilde u$. In consequence, under H-WEIL-EXACT,
$$
U_g=e^{i\theta_g}W(M_g)
$$
for some scalar phase independent of the power $n$.

Status: exact covariance and symplecticity `proved-here`; identification with $W$ `conditional-on H-WEIL-EXACT`.

⟨1⟩1. **Factor the transfer into three elementary unitary maps.**

PROOF: First apply the normalized Fourier transform on the first register, with kernel $q^{-1/2}\psi(cs_1x)$; leave all other registers unchanged. Denote the intermediate coordinates by $r=(x,s_2,\ldots,s_J)$. Next multiply by
$$
\psi\left(a_0r_1^2+\sum_{k=2}^Ja_{J+1-k}r_1r_k\right).
$$
Finally permute $(r_1,r_2,\ldots,r_J)$ to $(r_2,\ldots,r_J,r_1)$. The resulting kernel is exactly (7.1) divided by $\sqrt q$. This fixes both the direction of the cyclic permutation and the sign of the Fourier kernel.

⟨1⟩2. **Calculate centered Weyl covariance and symplecticity.**

PROOF: The Fourier transform maps the first pair of Weyl labels to $(-v_1/c,cu_1)$; a direct substitution in its kernel proves this without a residual phase. The quadratic multiplier maps $(u,v)$ to $(u,v+Ku)$, where $K$ is symmetric with
$$
K_{11}=2a_0,\qquad K_{1k}=K_{k1}=a_{J+1-k}\ (k\geq2),
\qquad K_{kl}=0\ (k,l\geq2).
$$
Indeed the difference of the quadratic phase at $s+u$ and $s$ is $(Ku)\cdot(s+u/2)$, exactly the centered Weyl exponent. The final permutation acts equally on position and momentum labels. Composing these three actions gives (7.13). The scaled Fourier pair map preserves $u_1\widetilde v_1-v_1\widetilde u_1$, a shear $v\mapsto v+Ku$ preserves the full form because $K$ is symmetric, and simultaneous coordinate permutations preserve it as well. Thus $M_g$ is symplectic, with an explicit verification independent of a character formula.

⟨1⟩3. **Identify the scalar ambiguity.**

PROOF: Under H-WEIL-EXACT, $U_g$ and $W(M_g)$ implement the same exact covariance, so their quotient commutes with every $X_{u,v}$. An operator commuting with every phase $X_{0,v}$ is diagonal in the computational basis, and commuting with every shift $X_{u,0}$ makes all its diagonal entries equal. Their quotient is therefore scalar; unitarity makes that scalar a phase. This argument would fail with arbitrary label-dependent phases in the covariance equation, which is why the normalization of the hypothesis matters. $\square$

**Corollary T7.10 (fixed spaces, the Weil bound, and the permutation sign).**

Hypotheses: T7.2, T7.3, and the exact covariance proved in T7.9. No existence or character theorem for the named Weil representation is necessary for the numerical trace identity below. For $J=0$ use the unique zero-dimensional symplectic space and the scalar transfer.

Claims: for every $n\geq1$,
$$
\tag{7.14}
|\operatorname{Tr}E_g^n|^2=q^{n+\dim\ker(M_g^n-I)},
\qquad
 d_n=\dim\ker(M_g^n-I)\leq2J.
$$
Consequently
$$
|S_n(g)|\leq q^Jq^{n/2},
\qquad
|S_n(g)|=q^Jq^{n/2}\quad\Longleftrightarrow\quad M_g^n=I.
$$
When $d_n=0$ the sign is exactly the Frobenius $n$-cycle sign:
$$
S_n(g)=(-1)^{n-1}\operatorname{Tr}E_g^n.
$$
For general $n$ the correction is $\det(S|R_n)$ as in (7.4), and it equals $\eta(-1)^{d_n}$ only under the condition specified in T7.3. Equality of the dimensions in (7.14) by itself does not identify determinant actions on the two different fixed spaces.

Status: `conditional-on H-NORMAL` for comparison with field sums; covariance trace and fixed-space assertions `proved-here`.

⟨1⟩1. **Prove the character-modulus identity directly.**

PROOF: The $q^{2J}$ centered Weyl matrices form a basis of $\operatorname{End}(\mathbb C^{q^J})$: their Hilbert--Schmidt inner products vanish for distinct labels, since a nontrivial shift has zero diagonal trace and a nontrivial phase has zero character sum. Exact covariance makes $\operatorname{Ad}(U_g^n)$ a permutation of this basis by $M_g^n$, with coefficient one on every fixed label. Therefore
$$
\operatorname{Tr}\operatorname{Ad}(U_g^n)
=\#\ker(M_g^n-I)=q^{\dim\ker(M_g^n-I)}.
$$
For a unitary finite matrix $V$, $\operatorname{Tr}\operatorname{Ad}(V)=|\operatorname{Tr}V|^2$, as follows on matrix units or by vectorization. Since $E_g^n=q^{n/2}U_g^n$, this proves (7.14)'s trace formula and also proves the modulus assertion in H-WEIL-REP whenever exact Weyl covariance holds.

⟨1⟩2. **Identify the dimension and saturation condition.**

PROOF: T7.2 gives the same trace magnitude $q^{n+d_n}$. Comparing powers of $q$ gives the dimension identity. A linear map on a $2J$-dimensional space has kernel of dimension $2J$ precisely when it is zero, so saturation is exactly $M_g^n-I=0$. Independently $d_n\leq2J$ follows from the gcd description in T7.4 and $\deg(z^JP(z))=2J$. For $J=0$, the trace form is nondegenerate, $d_n=0$, and the scalar unitary has trace of modulus one, so every assertion has the same interpretation. Absolute-value saturation of one character sum is not by itself a claim that the whole projective curve is maximal or minimal: the sum over all characters and its real sign still matter.

⟨1⟩3. **Check the requested example and permutation interpretation.**

PROOF: For $q=3$, $a=(0,1)$, (7.13) gives
$$
M_g=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad M_g^2=-I,\qquad M_g^4=I.
$$
It has order four, $\ker(M_g^2-I)=0$, and $\dim\ker(M_g^4-I)=2=2J$. Thus $d_2=0$ and $d_4=2$, as in the data. When $d_n=0$, $R_n=0$ so (7.4) reduces to $(-1)^{n-1}$, the sign of the Frobenius permutation of the $n$ conjugates and the discriminant character in H-STICK. This is a precise finite-field permutation sign. For nonzero radical the general determinant correction in T7.3 replaces the draft's universal fixed-dimension correction. $\square$

A separate bounded Python check verified (7.13)'s symplectic identity and centered Weyl covariance for $(q,a)=(3,(0,1)),(3,(2,1)),(3,(0,1,1)),(5,(1,1)),(5,(1,2,1))$. It tested every Weyl label in the three $q=3$ cases and the position/momentum basis labels in the two $q=5$ cases: **105 covariance comparisons**, with maximum entrywise residual approximately $7.55\times10^{-16}$. This checks the explicit matrix and Fourier orientation; the exact proof is T7.9. An exact SymPy calculation for $q=3$, $a=(1,1)$, $h=3$ additionally verified $[L(g,T)D_g(T)]^3=\det(I-T^6E_g^6)$ with
$$
L(g,T)=1-i\sqrt3\,T+\frac{-3+3i\sqrt3}{2}T^2+\frac{9+3i\sqrt3}{2}T^3.
$$

## T8. CORRECTION LEDGER and what is established

Author: codex:gpt-6-astra

The ledger includes false statements, necessary extra hypotheses, and distinctions that change the meaning of a claimed realization. An entry saying that a formula survives with its signs checked is distinguished from an actual correction.

| Draft or contextual claim | Correction, qualification, or verified replacement |
|---|---|
| Earlier notebook “T4.3 is the Dyson theorem” | The current file labels the Dyson theorem T4.4. T4.3 there is the line-duality theorem. |
| T1(a), uniform integration by parts using only the imaginary part | Use the full complex parameter $\lambda$; derivatives of $e^{\operatorname{Re}\lambda t}$ are not uniformly bounded merely from an upper bound on $\operatorname{Re}\lambda$. T1.1 supplies the correct estimate. |
| T1(b), pairing with $t^ke^{-st}$ | A distribution on the open half-line does not automatically act on that test. T1.2 constructs common cutoffs, proves a summable uniform estimate, and then proves the meromorphic principal-part argument. The rigidity theorem itself is true. |
| T1(c), the explicit formula and reflected spectrum | Verified: the archimedean term is $-1/(e^{2u}-1)$ in the zero trace; the reflected ladder is $-(k+1/2)$, $k\geq1$; the half-time delta Jacobian is two. There is one even constant mode after the weight $e^{-t/2}$. |
| T2(a), reality | True with the specified common parity for all copies at a given value. In a more general datum only the conjugation symmetry of net multiplicities is forced. |
| T2(b), “a cosine is negative somewhere” | A cosine cannot be considered independently of other terms of the same growth. T2.2 uses the mean and mean square of the entire leading trigonometric polynomial. The theorem extends to arbitrary trivial-zero flips when the nontrivial flip set is finite. |
| T2(c), an infinite positivity theorem from Landau | Not proved under positivity alone. The possible negative prime atoms of $\mu-\operatorname{comb}$ prevent the proposed positive-measure argument. T2.3 proves a precise theorem under the stronger domination $\mu\geq\operatorname{comb}$; T2.4 identifies the missing step in the unrestricted case. |
| T3(a),(b), the no-go | True. Residues require a negative eigenvalue multiplicity at every uncancelled numerator root. Algebraic multiplicities and the possibility of matching hypothetical eigenvalues are explicitly handled. |
| T3(c), the entire-function criterion | Require an exact normalized genus-zero canonical product, with no nonconstant zero-free exponential factor. Interpret the original series as a germ (or initially a formal germ). Eigenvalue zero and nilpotent blocks are invisible to positive-power traces. |
| T3(d)(i), curve hypotheses and forced odd modes | Add geometric connectedness for the even list $\{1,q\}$. Frobenius root sizes ensure that the $H^1$ roots cannot cancel those even values. Spectral uniqueness does not determine Jordan blocks. |
| T3(d)(ii), ordinary MPS norms | The no-go excludes every fixed finite local tensor for positive-genus curve counts, including the quadratic Artin--Schreier family. Its complex transfer partition function must not be called an ordinary ring norm. |
| T3(d)(iii), graph zeta has no zeros | True on the finite complex plane for $1/\det(1-uT)$; a rational-function zero at infinity is not excluded. Graph counts need no negative net multiplicities. |
| T4, the original report's positive zero trace | Replace it by $\operatorname{Tr}_{\rm dist}Z=1-2P_+-e^{-t/2}/(e^t-1)$. Its prime part is negative and its full distribution is not supported only at prime lengths. The augmented supertrace is exactly $2P_+$. |
| T4, a forced physical grading from positivity | Exact trace equality forces the **net graded spectral datum**. Positivity alone does not fix the ladder, and unrestricted infinite parity rigidity is not established. None of these identities by itself constructs a fermionic cMPS norm. |
| T4, the pole and RH language | $\xi$ as defined is entire. The new even line represents the zeta pole contribution; it is added to $K_S$. The geometric names are recorded as an interpretation. RH refers only to the odd $K_S$ modes, not the odd ladder. |
| T4, an operator trace | H-TRACE is explicitly a definition by fiat. The asserted infinite eigenvalue list precludes compactness and trace class of $Z(t)$ at $t>0$. |
| T5(a), “unique fixed point” | There is a unique stationary **density matrix**; the fixed-operator space is $\mathbb C\Omega$. All block equations and the CPTP channel are proved. |
| T5(b),(c), spectrum and parity | Use ordered pair sums with multiplicities $m_B(b)m_B(c)$ and add multiplicities at collisions. Coherences are odd; populations and the vacuum are even. There is only one algebraic zero eigenvalue in the finite model. |
| T5(d), one odd appearance per zero | There is one coherence appearance and one conjugate appearance. Since the zero multiset is conjugation invariant, the combined formal odd list has multiplicity $2m_\rho$ at each zero-mode value. It is not T4's single-copy graded datum. |
| T5(d), H-LP implies a rank-one Lindblad formula in infinite dimension | H-LP supplies no bounded exit vector or generator-domain identity. T5.3 instead constructs a genuine absorbing-vacuum CPTP semigroup from any strongly continuous stable contraction semigroup. The finite rank-one formula is not asserted for its infinite-dimensional generator. |
| T5(d), the population trace $\lvert\operatorname{Tr}Z\rvert^2$ | Only a formal expression or a finite-cutoff equality. The pair spectral list violates (G2), and a product of the distributional traces is not defined here. No form-factor or pair-correlation limit is claimed. |
| T5(e), the rebound integral is solved by $\Omega$ | False: $\Omega$ is outside the original $K_S$, and in the enlarged space the integral equals $T\Omega$ up to cutoff $T$ and diverges. The vacuum is absorbing, not a finite-holding-time renewal state. |
| T5(e), half-chain state equals the bond state | The precise canonical fact is equality of nonzero Schmidt spectra, or identification of supports by an isometry. Here that spectrum is $\{1\}$; the stationary output is the vacuum. This does not realize a critical Bost--Connes entanglement spectrum. |
| H-BC and T6(a), all KMS states are Gibbs in one representation | Distinguish one normal Gibbs state on all bounded operators from the arithmetic family of extremal Gibbs states and their mixtures on the Bost--Connes algebra. The supplied type III$_1$ assertion is used only for $0<\beta\leq1$ on that arithmetic algebra. |
| T6(a), representation and temperature | Use the normal $W^*$ KMS condition for $\operatorname{Ad}(N^{it})$ on bounded operators. No point-norm-continuous $C^*$ dynamics on all of that algebra is assumed. Normal Gibbs states exist exactly for $\beta>1$. |
| T6(a), entanglement energies and ring lengths | The energies are $\beta\log n+\log\zeta(\beta)$. T4's time lengths are $2\log n$. The purification has bond dimension one along primes, but has left--right entanglement within each paired prime site. |
| T6(b), the displayed infinite Lindbladian acts on all bounded operators | Its formula is in the Schrödinger convention. Summable up rates alone do not give a bounded quantum generator. The diagonal process is nevertheless well defined and nonexplosive. A norm-convergent quantum model is proved with $\sum_pr_pp^\beta<\infty$. |
| T6(b), the example $r_p=p^{-\beta}$ | Valid for summable up rates when $\beta>1$; it has nonsummable down coefficients equal to one. It is not an example of the bounded quantum sum used in T6.4. |
| T6(b), infinite diagonal spectrum | It is the **closure of the union of finite Minkowski sums** of the bands, together with zero, on the specified stationary weighted space. The closure and the choice of function/density Hilbert space cannot be omitted. H-MM1 is proved here. |
| T6(b), off-diagonal zeros | For summable down coefficients the full quantum generator is real-spectral on an explicitly specified weighted Hilbert space, proved by its matrix-unit blocks. No assertion is transferred to unspecified unweighted operator spaces or unbounded closures. |
| T6(c), “the transition is ergodicity breaking” | Proven content: escape of normal Gibbs mass and absence of a stationary probability on integer configurations below the threshold. A claim about a Riemann Lindbladian's ergodicity, gap, or multiple steady states needs a specified generator and is not established. |
| T7, affine versus projective count | The projective count has the additional one. The unique point at infinity and the additive Hilbert-90 count are proved in T7.8. |
| T7, memory zero | For $J=0$ the minimal transfer is the scalar quadratic Gauss sum and $E_0=q$. The module's redundant register adds zero eigenvalues and is not the claimed one-dimensional scaled unitary. |
| T7(a), short rings and a normal basis | The closed-path formula is valid for every $n$, including $n\leq J$. In a general normal basis the trace form is $CM$, not $M$; self-duality cannot be assumed for even $n$. |
| T7(b), the proposed universal conjugated sign | False. The correct law is $S_n=(-1)^{n-1}\det(S\vert\ker P(S))\operatorname{Tr}E_g^n$, proved for every $n$, including $q\mid n$. Exact counterexamples occur at $(q,a,n)=(3,(2,1),1)$ and $(5,(1,1),2)$. |
| T7(b), dependence on rank alone | The correction is the determinant of the cyclic shift on the radical, not universally $\eta(-1)^{d_n}$. T7.4 computes it from the minus-one primary factor, including its nonsemisimple multiplicity. Equivalently it is the periodic sign $1-2\mathbf1_{2h\mid n}$. |
| T7(b), when the draft's law is actually valid | For the whole sequence the exact necessary and sufficient condition is $P(-\eta(-1))\ne0$. A failure is not confined to characteristic-divisible extension degrees. |
| T7(c), $L=\det(1+\eta(-1)TE_{-g})$ and the claimed conjugate Frobenius spectrum | These hold under that endpoint condition. In general use (7.9) and the explicit reciprocal-root multiplicities (7.10). H-AS is used openly to ensure the latter are nonnegative integers. |
| T7(c), the original notebook claim and its spectral test | Its unconditional coefficient criterion is $P(-1)\ne0$. The draft's tests involving conjugation of $\operatorname{spec}E_g$ are valid only after establishing its proposed Frobenius identification, hence with the stated additional endpoint condition. |
| T7(d), the proposed universal odd block | False: the $q=3$, $g=2x^2+x^4$ example gives its claimed supertrace $-2$ when the actual projective count is $10$. Replace each character block by $F_{ag}$ from (7.10); the simpler block survives under the stated endpoint condition. |
| T7(d), $E_0$ and cancelling pairs | $\operatorname{Tr}E_0^n=q^n$ for all $n$. Its nonzero spectrum is just $q$ once, with $q^J-1$ extra invisible zero eigenvalues for $J\geq1$. There are no **nonzero** even--odd cancellations in the corrected count. |
| T7(d), “conjugate to Frobenius up to cancelling pairs” | Equality of net multisets is forced by traces; operator similarity also needs semisimplicity. H-FROB-SS states exactly the additional input for similarity. The odd dimension is checked as $(q-1)q^J=2g(C)$. |
| T7(d), scaled unitarity | True. T7.6 supplies the full output-row index calculation and handles $J=0$ separately. The corrected odd block is also scaled unitary, by its explicitly constructed spectrum. |
| H-WEIL-REP and T7(e), arbitrary phases in Weyl covariance | Arbitrary label-dependent phases allow Weyl displacements, so do not characterize a Weil implementer up to scalar. With centered exact covariance, T7.9 gives the explicit symplectic map (7.13) and proves the scalar-phase identification. |
| T7(e), $d_n$ and saturation | True for the original complex transfer: $d_n=\dim\ker(M_g^n-I)$, proved by taking the trace of its exact Weyl permutation. The character-modulus identity is proved directly. Absolute saturation of one character sum is not an assertion that the whole curve is maximal. |
| T7(f), Frobenius permutation sign | True when $d_n=0$. For general $n$ use the determinant correction in (7.4), not a universal $\eta(-1)^{d_n}$. The general sign problem T7(b) is closed in this note; it is not left as an unresolved nonsemisimple case. |

The complete H-* inventory is as follows. Supplied statements with an overbroad clause were recorded before their operational correction, so an invalid premise is never silently used.

| Label | Exact role and status |
|---|---|
| H-ZEF-T | External positive-time zeta explicit formula. Its derivative, sign, archimedean expansion, and change-of-variable normalization are verified; the zeta formula itself is assumed. |
| H-ZERO-COUNT | External Riemann--von Mangoldt count, used for tested spectral convergence and finite order. |
| H-ZETA-LOC | Added explicit strip, nonrealness, local finiteness, and zero-multiset symmetry input. No RH premise. |
| H-SCHWARTZ | External equivalence of positive distributions and positive Radon measures. |
| H-LANDAU | External real-axis singularity theorem for a positive Laplace transform with finite abscissa; used only in T2.3 with the added domination premise. |
| H-LIDSKII | External trace/eigenvalue theorem for trace-class operators. Only the infinite ordinary-trace necessity uses it. |
| H-WEIL | External curve point-count and Frobenius theorem, including root sizes; used for the general curve obstruction and the cohomological identification. Artin--Schreier root sizes are obtained from the transfer without using this size assertion. |
| H-LP | Assumed Riemann model-space contraction semigroup, spectral modes, and strong stability. Not constructed or analytically validated here. |
| H-TRACE | Definition by fiat of its spectral distributional trace; distinct from ordinary traces. |
| H-CMPS | External canonical cMPS Schmidt-spectrum fact, stated with its support and normalization convention. The particular vacuum output is also checked directly. |
| H-BC | Supplied Bost--Connes wording, recorded with its representation, mixture, and temperature qualifications; not used in its overbroad literal form. |
| H-BC-POS | Correct operational positive-temperature Bost--Connes theorem, attributed to Bost--Connes 1995 as requested. Only the arithmetic type III comparison uses it. |
| H-MM1 | Supplied birth--death spectrum; proved in T6.2 on the precise stationary weighted space. |
| H-GAUSS | Supplied quadratic Gauss evaluation and phase identities; proved in T7.1. |
| H-STICK | Supplied discriminant sign; proved in T7.3 from H-NORMAL and embedding matrices. |
| H-NORMAL | External normal-basis theorem and its odd-degree self-dual version. The general sign proof needs only existence of a normal basis. |
| H-WEIL-REP | Supplied genuine Weil representation and character statement; its covariance wording is sharpened by H-WEIL-EXACT, and the character-modulus conclusion is proved directly for exact implementers. |
| H-WEIL-EXACT | Added precise centered Weyl normalization and existence of a genuine exact implementer. Used only to identify the explicitly constructed Clifford unitary with the named Weil representation. |
| H-AS | Supplied character $L$-polynomial polynomiality and degree made explicit. It ensures the finite spectral recipe (7.10) has nonnegative integral multiplicities. No Frobenius modulus is assumed in this input. |
| H-FROB-SS | Added cohomological Frobenius semisimplicity input, needed only for operator similarity, not for forced net spectra or the constructed transfer. |

**Proposition T8.1 (the established scope of the Phantasm).**

Hypotheses: exactly the premises listed for the referenced results above; in particular the zeta operator statements retain H-LP and H-TRACE, and the arithmetic polynomial realization retains H-AS.

Claim: these data force and realize a graded single-particle **spectral** version of the Phantasm, and realize a genuine absorbing-vacuum channel with the zero channel in its odd coherences. They do not establish a nontrivial cMPS whose norm is the prime measure and whose stationary bond density is a normal critical Bost--Connes state.

Status: `conditional-on the hypotheses of T1.4, T4.1, T5.3, T6.1, T7.7--T7.8`; assertion about remaining gaps is a scope audit.

⟨1⟩1. **Combine the positive and negative results.**

PROOF: T1.4 fixes the net spectral list, and T4.1 realizes it by a graded contraction semigroup with one fixed even line. T3 excludes ordinary finite and trace-class realizations of positive-genus curve counts and T4.2 excludes all-even spectral data for the prime measure. T5.3 supplies a true CPTP absorbing-vacuum extension with exact zero coherences, but T5.1--T5.5 show its extra population modes, doubled coherence list, and pure stationary density. T6.1 excludes a normal critical KMS density in the prime Hamiltonian representation. None of these deductions identifies that absorbing state with the critical arithmetic state or its cMPS entanglement spectrum.

⟨1⟩2. **State the unresolved work without rounding up.**

PROOF: Unrestricted infinite parity rigidity under positivity alone remains open here (T2.4). H-LP's analytic realization from the report's scattering symbol is assumed, and H-TRACE remains a prescribed spectral distribution. An ordinary physical norm interpretation of the prime supertrace, a nontrivial stationary entangled bond with a critical arithmetic interpretation, and the prime-jump/renewal realization in the original compressed space have not been constructed. An unbounded quantum closure of the prime-generator example $r_p=p^{-\beta}$ is not provided by the bounded proof of T6.4. The finite-field sign law has no remaining exceptional class of extension degrees: T7.3--T7.4 prove it for all $n$, while T7.7--T7.8 explicitly retain the supplied arithmetic polynomiality and cohomology hypotheses where needed. $\square$

**RESULT:** `proved-here`: general distributional existence and rigidity T1.1--T1.2; finite ordinary-trace obstruction and the elementary parts of T3.1--T3.3; the finite vacuum-decay model and finite trace formulas T5.1--T5.2; the absorbing extension T5.3 for an abstract stable contraction; the renewal obstruction; normal Gibbs classification and prime factorization; the M/M/1 theorem and the specified classical/quantum prime-chain results T6.1--T6.5; Gauss evaluation, transfer unitarity, exact symplectic covariance, and its character-modulus formula. `conditional-on` the stated zeta inputs: the forced arithmetic spectra, finite-flip positivity theorem, the dominated infinite-flip theorem, and T4's Riemann supertrace realization. `conditional-on H-NORMAL`: the complete general Artin--Schreier sign law, endpoint criteria, and comparison of field sums with symplectic fixed spaces; additionally `conditional-on H-AS`: the corrected finite character and projective super-transfers; additionally H-WEIL/H-FROB-SS only for the stated cohomological identification/similarity. `sketched`: the geometric pole names, full infinite population spectral/form-factor notation, and a physical Phantasm interpretation. Open here: unrestricted T2(c), validation of the assumed Riemann operator input, and the nontrivial critical cMPS/renewal/prime-jump realization. T7(b) is resolved with a corrected law, including $q\mid n$; neither RH nor the existence of the full physical Phantasm is proved.
