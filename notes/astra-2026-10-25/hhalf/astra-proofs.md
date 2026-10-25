# Hyperelliptic half-coefficients and whole-cover averages (lane A2)

Author: `codex:gpt-6-astra`, 2026-10-25.

Status: **PARTIAL for the unrestricted H-half and A1 conjectures.** H-half is proved for all odd prime powers through genus 7; A1 is proved through genus 7 for both odd conductor and completed even conductor. The finite grids below and all five requested whole-cubic cells pass exact root certificates. No counterexample to H-half or A1 was found. Nothing is registered, and these proofs still require the notebook's review gate. All files are confined to this lane; the previous lane is a read-only input.

## 1. A2-1 — H-half

**PARTIAL globally; PROVED for every odd prime power and genera 1–7.** No counterexample to the all-genus conjecture is established. The proposed condition here is the stronger, unhalved inequality
\(1=b_0\ge b_1\ge\cdots\ge b_{\lfloor g/2\rfloor}>0\). The previous lane's sufficient condition halves the central coefficient when \(g\) is even; these are distinct conditions.

### Exact degree reduction for the nonsquare terms

**PROVED (a constructive formula).** Write \(S_{d,n}=\sum_{D\in\mathcal H_d}[u^n]L(u,\chi_D)\), and \(\epsilon=(-1)^{(q-1)/2}\). The previous lane's formulas (1)–(5) are retained exactly. The following rearrangement makes them much faster without dropping nonsquares.

For \(a\) monic and \(h\ne1\) squarefree, let \(A=\deg a\), \(H=\deg h=n-2A\). Since \(\chi_h(P)=0\) for \(P\mid h\), the local identity
\[
\frac{L(t,\chi_h)}{\prod_{P\mid h}(1-t^{2\deg P})}
\prod_{P\mid a,P\nmid h}(1+\chi_h(P)t^{\deg P})^{-1}
=
\frac{L(t,\chi_h)\sum_{b\mid\operatorname{rad}a}\mu(b)\chi_h(b)t^{\deg b}}
 {\prod_{P\mid ah}(1-t^{2\deg P})}
\tag{A}
\]
is exact. Multiplication by \(1-qt^2\), coefficient extraction, and the reciprocity factor \(\epsilon^{dH}\) give the summand of \(S_{d,n}\).

Let \(\ell_{h,j}=[t^j]L(t,\chi_h)=\sum_{\deg f=j}(f/h)\). The algebraic functional equation reconstructs
\[
L(t,\chi_h)=\sum_{j=0}^{\lfloor(H-1)/2\rfloor}\ell_{h,j}E_{H,j}(t),
\tag{B}
\]
where for \(H=2r\),
\[
E_{2r,j}(t)=(1-t)\left(\sum_{i=j}^{r-1}t^i+
\sum_{i=j}^{r-2}q^{r-1-i}t^{2r-2-i}\right),\quad 0\le j\le r-1,
\]
and for \(H=2r+1\), \(E_{H,j}=t^j+q^{r-j}t^{2r-j}\) if \(j<r\), while \(E_{H,r}=t^r\).

For each \(F=fb\), introduce the finite-coefficient Euler product
\[
W_{H,F,a}(v)=[z^H]
\prod_{P\mid a}(1+\chi_F(P)z^{\deg P})
\prod_{P\nmid a}\left(1+\frac{\chi_F(P)z^{\deg P}}{1-v^{\deg P}}\right),
\quad \chi_F(P)=(P/F).
\tag{C}
\]
Quadratic reciprocity says that the inner sum over \(h\) in (A)–(B), with its denominator outside \(a\), is
\(\epsilon^{H\deg F}W_{H,F,a}(t^2)\). Thus the exact nonsquare contribution is
\[
S^{\rm ns}_{d,n}=\epsilon^{dn}[t^d](1-qt^2)
\sum_{A=0}^{\lfloor(n-1)/2\rfloor}\sum_{\deg a=A}
\frac{\displaystyle\sum_{b\mid\operatorname{rad}a}\mu(b)t^{\deg b}
\sum_{j=0}^{\lfloor(H-1)/2\rfloor} E_{H,j}(t)
\sum_{\deg f=j}\epsilon^{H(j+\deg b)}W_{H,fb,a}(t^2)}
 {\displaystyle\prod_{P\mid a}(1-t^{2\deg P})},\quad H=n-2A.
\tag{D}
\]
For even \(n=2m\), every \(H\) is even, both signs disappear, and \(\deg(fb)\le m-1\). This is the degree reduction: the character modulus needed in (C) has degree at most \(m-1\), whereas the original nonsquare formula enumerated \(h\) up to degree \(2m\). The square part remains exactly formula (5) of the previous lane.

To evaluate (C), one need not enumerate its primes. Put \(N_r=\#\{P:\deg P=r\}\), \(Z_r=\#\{P\mid F:\deg P=r\}\), and \(A_r=\sum_{\deg P=r}\chi_F(P)\). From the logarithmic derivative of the *actual imprimitive* \(L(t,\chi_F)\), compute \(C_k=[t^k]tL'/L\). Then
\[
rA_r=C_r-\sum_{s\mid r,\ s<r}s
\begin{cases}N_s-Z_s,&r/s\text{ even},\\A_s,&r/s\text{ odd}.
\end{cases}
\tag{E}
\]
There are \((N_r-Z_r\pm A_r)/2\) primes with signs \(\pm1\). Separate the finitely many primes of \(a\), and group the remaining factors of (C) by these counts. Principal \(\chi_F\) is handled by \(L=(1-qt)^{-1}\prod_{P\mid F}(1-t^{\deg P})\). Nothing in (A)–(E) assumes RH. The code uses FLINT integer polynomials for the truncated series and rational numbers only at final normalization.

`checks/exact_core.py` implements (A)–(E). Translation of the variable permits normalizing the subleading coefficient of \(a\), or of \(f\), when its degree is nonzero in the constant field; this multiplies the orbit contribution by \(q\). For even \(H\), simultaneously reversing signs at odd-degree primes leaves (C) unchanged by \(z\mapsto-z\). These are exact optimizations. The \(q=9\) code uses \(\mathbb F_3[a]/(a^2+2a+2)\), **not** arithmetic modulo 9.

### What can be proved uniformly about the square part

**PROVED (uniform positivity, and an exact fixed-coefficient limit).** For every \(d\ge2,m\ge0\), the exact square density of the prior lane satisfies
\[
c_{d,m}\ge1-\frac{q}{(q-1)^2}\ge\frac14.
\tag{I}
\]
Indeed for independent uniform \(D\in\mathcal H_d\) and monic \(a\) of degree \(m\), a union bound over common prime divisors gives
\[
1-c_{d,m}\le\frac{q}{q-1}\sum_{r\ge1}N_rq^{-2r}
\le\frac{q}{q-1}\sum_{r\ge1}\frac{q^{-r}}r
\le\frac{q}{(q-1)^2}.
\]
Primes of degree too large to divide either polynomial contribute zero, so extending the sum is harmless.

For fixed \(q,m\), taking the simple pole at \(t=1/q\) in the exact squarefree generating function yields
\[
\lim_{g\to\infty}b_m(q,g)=C_{q,m},\qquad
\sum_{m\ge0}C_{q,m}w^m=
\frac1{1-w}\prod_{r\ge1}\left(1-\frac{w^r}{q^r(q^r+1)}\right)^{N_r}.
\tag{J}
\]
Here the nonsquare term tends to zero: for fixed \(m\), its rational generating functions in (A) have only roots of unity as poles, so their coefficients grow at most polynomially in \(d\), while the normalization is exponential. The same observation justifies extracting the square main term rather than replacing a finite density without an error statement. Equivalently,
\(C_{q,m}=q^{-m}\sum_{\deg a=m}\prod_{P\mid a}|P|/(|P|+1)\), and another union bound gives \(C_{q,m}\ge1-1/(q-1)\ge1/2\).

The first limiting gaps are exactly
\[
C_0-C_1=\frac1{q+1},\quad
C_1-C_2=\frac{q-1}{(q+1)^2(q^2+1)},\quad
C_2-C_3=\frac{(q-1)(2q^2+1)}{q(q+1)^3(q^2+1)(q^2-q+1)}.
\]
`checks/square_density.py` computes further gaps in FLINT rationals, explicitly labelled **limit only**. Neither (I) nor (J) controls the sign of adjacent coefficients when \(m\) grows with \(g\); those diagnostics are not counted as H-half certificates.

The exact representation-theoretic form of the missing inequality is also useful. For \(2m\le g\), symplectic Lefschetz decomposition gives \(\wedge^{2m}V=\wedge^{2m-2}V\oplus\wedge^{2m}_0V\). Hence
\[
b_m-b_{m-1}=\left\langle\operatorname{tr}\left(\Theta_D\mid\wedge^{2m}_0V\right)\right\rangle.
\]
H-half asks for nonpositive averages of these **primitive exterior-power characters**, together with positivity of \(b_m\). These are nonlinear trace statistics; single power traces do not recover them.

### A uniform theorem through genus seven

**PROVED.** For every odd prime power \(q\) and \(1\le g\le7\),
\[
1=b_0>b_1>\cdots>b_{\lfloor g/2\rfloor}>0
\]
when the displayed chain has a nonconstant term. In particular H-half and A1 hold in this range.

Here is a finite algebraic proof with an independently reproducible positivity certificate. For \(n=2,4,6\), (D) only needs \(\deg F\le2\) and \(A+j\le2\). The primitive character numerators at those degrees are respectively 1 (linear conductor) and \(1-t\) (squarefree quadratic conductor), including both split and irreducible quadratics. Thus the counts in (E) are rational polynomials in \(q\), determined by the factorization type of \(F\).

The multiplicities and exceptional-prime signs in (C) are also polynomial in \(q\): the quadratic types have multiplicities \(q\), \(q(q-1)/2\), \(q(q-1)/2\) (linear square, distinct linear pair, irreducible). The only additional nonzero sign to count is the character of the difference of two distinct rational roots. Among ordered distinct pairs, each sign occurs \(q(q-1)/2\) times. The remaining cases have \(F=1\), \(F\mid\operatorname{rad}a\), or identical linear factors, giving signs 1 or 0. This exhausts \(A+j\le2\); no elliptic numerator or characteristic-dependent trace distribution enters. Binomial expansion of the grouped Euler factors therefore proves that, for each fixed \(d\), \(S_{d,n}\) is one rational polynomial in \(q\), valid for **all odd prime powers**.

The elementary bound \(|S_{d,n}|\le q^{d+n}\) proves that its degree is at most \(d+n\): otherwise its growth on the unbounded set of odd primes would contradict the bound. For \(g\le7\), \(d\le15\), \(n\le6\), the degree is at most 21. Consequently its values at the 22 odd primes from 3 through 83 determine it **exactly**, rather than merely suggest an interpolation. `checks/hhalf_low_genus.py` computes these values by (A)–(E), interpolates over \(\mathbb Q\), and checks the additional fields 9, 89 and 97. Those extra checks are redundant for unisolvence.

Let \(P_m(q)=S_{2g+1,2m}\), \(P_0=(q-1)q^{2g}\). The script prints all coefficient formulas and verifies that both
\[
P_m(x+3),\qquad (qP_{m-1}(q)-P_m(q))\big|_{q=x+3}
\tag{F}
\]
have nonnegative rational coefficients and strictly positive constant term. Dividing by \((q-1)q^{2g+m}>0\) proves positivity and strict decrease for every real \(q\ge3\), hence for every required field. For example,
\[
b_{2}\big|_{g=4}=
\frac{q^9-q^8+q^7-2q^6+4q^5-3q^4-q^3+3q^2-3q-1}{q^9},
\]
and the ascending coefficient vector of the *unscaled* gap numerator \(qP_1-P_2\) after \(q=x+3\) is
\[
(1212,4022,5886,4923,2561,846,173,20,1).
\]
The corresponding new last-gap vectors for \((g,m)=(5,2),(6,3),(7,3)\) are
\[
\begin{split}
&(12846,50677,89523,93302,63564,29593,9540,2104,304,26,1),\\
&(70122,303277,594484,696750,542353,294370,113679,31237,5986,762,58,2),\\
&(712596,3513856,7972137,11019581,10355505,6987959,3484584,1300473,363370,75103,11165,1131,70,2).
\end{split}
\]
All earlier gaps and all positivity vectors are verified by the same exact code. This proof uses a proved polynomiality/degree bound; it is not extrapolation from a grid of fields.

**OPEN beyond this theorem.** For \(m\ge4\), (D) brings in genuine positive-genus character numerators. The genus-zero classification used above no longer proves polynomiality in \(q\). The current obstruction is a uniform signed bound for the nonsquare term at adjacent coefficients, small enough to preserve the rapidly shrinking square-density gaps. Neither individual Weil RH nor the single-trace formula supplies that bound.

### The trace shortcut is false

**REFUTED (a proposed route, not H-half).** For \(P_D(z)=\det(1-z\Theta_D)\),
\[
\langle\log P_D(z)\rangle=-\sum_{n\ge1}\langle\operatorname{tr}\Theta_D^n\rangle z^n/n,
\]
but generally \(\log\langle P_D\rangle\ne\langle\log P_D\rangle\). Already the coefficient of \(z^2\) in the averaged determinant is
\(\frac12\langle(\operatorname{tr}\Theta_D)^2-\operatorname{tr}\Theta_D^2\rangle\). Single-trace averages do not determine it. At \((q,g)=(3,1)\), `checks/hhalf_rudnick.py` prints \(\langle\operatorname{tr}\Theta_D^2\rangle=-10/9\), \(\langle(\operatorname{tr}\Theta_D)^2\rangle=8/9\), and hence coefficient 1 for the true mean versus \(5/9\) for the exponential of the mean logarithm.

Rudnick's Theorem 1 (Acta Arith. 143 (2010), p.83) is an asymptotic with a persistent small-power correction, not the asserted exact identity. For \(\eta_n=1_{2\mid n}\), it gives
\[
\langle\operatorname{tr}\Theta_D^n\rangle=
\begin{cases}-\eta_n&0<n<2g,\\-1-(q-1)^{-1}&n=2g,\\0&n>2g\end{cases}
+\eta_n q^{-n/2}\sum_{\deg P\mid n/2}\frac{\deg P}{|P|+1}
+O_q(nq^{n/2-2g}+gq^{-g}).
\]
In particular the correction for \(n=2\) is \(1/(q+1)\), which does not vanish as \(g\to\infty\) with \(q\) fixed. The endpoint \(n=2g\) has the additional \(-1/(q-1)\). Source: [published paper, Theorem 1 and §5](https://www.impan.pl/shop/en/publication/transaction/download/product/83137). No estimate from this paper is silently treated as an exact coefficient formula.

For completeness, the finite trace formula used in the check is exact in every degree, not just an asymptotic range. Write
\[
\rho_{d,r}=\frac1{H_d}[t^d]\frac{1-qt^2}{(1-qt)(1+t^r)},\qquad
\sigma_r(a)=[x^a]\frac{1-qx}{1-x^r},
\]
and \(U_r(\beta)=\sum_{\deg P=r}[t^\beta]L(t,\chi_P)\), with coefficients beyond the raw degree interpreted as zero. For even \(n\),
\[
\langle\operatorname{tr}\Theta_D^n\rangle=
-q^{-n/2}\sum_{r\mid n/2}rN_r\rho_{d,r}
-\frac{q^{-n/2}}{H_d}\sum_{\substack{r\mid n\\n/r\ \mathrm{odd}}}r
\sum_{a=0}^{g}\sigma_r(a)U_r(d-2a),\qquad d=2g+1.
\tag{H}
\]
This follows by expanding the logarithmic derivative into prime powers and then the squarefree Euler factors. All \(r\) in the second sum are even, so the Jacobi reciprocity sign is 1. For odd \(n\), the mean is **exactly zero** by the nonsquare scaling involution, in every degree. The asserted exact identity \(\langle\operatorname{tr}\Theta_D^n\rangle=-1\) on all even \(0<n\le2g\) is false: already \(n=2,g=2,q=3\) gives \(-20/27\). Rudnick's corollary gives Haar agreement up to \(o(1/g)\) when \(3\log_qg<n<4g-5\log_qg\), excluding \(n=2g\); it is not exact equality. Formula (H), including the finite \(\rho_{d,r}\), is what the script compares to member-by-member Newton sums.

## 2. A2-2 — circle property

**PARTIAL globally; PROVED for every odd prime power in odd-conductor genera 1–7 and completed even-conductor genera 1–7.** The finite-field extensions are listed below. No failure of A1 is found, and no all-genus theorem is claimed.

### Why the coefficient theorem implies A1

For a real reciprocal \(B\), form the first-half polynomial \(P\), halving its last coefficient when \(g\) is even. The inequalities of §1 imply positive decreasing coefficients of \(P\), with \(p_0>p_1\) unless \(P\) is constant. From
\[
(1-w)P(w)=p_0-\sum_{j=1}^{k}(p_{j-1}-p_j)w^j-p_kw^{k+1}
\]
the triangle inequality excludes zeros in \(|w|<1\); equality on the boundary forces \(w=1\), where \(P(1)>0\). Thus \(P\) has no zero in the closed disk. Since \(B=P+w^gP(1/w)\), the quotient of the reflected term by \(P\) is analytic in the disk, has modulus one on the boundary, and vanishes at zero. The maximum principle excludes zeros of \(B\) in the open disk; reciprocity excludes zeros outside. This repeats the previous lane's sufficient theorem with its hypotheses actually proved through genus seven.

### Completed even conductor: a uniform theorem through genus seven

**PROVED by exact algebraic sign certificates.** For every odd prime power \(q\) and \(1\le g\le7\), the average of \(L(u,\chi_D)/(1-u)\) over monic squarefree \(D\) of degree \(2g+2\) has every root on the critical circle. The raw average retains its trivial root at \(u=1\).

Formula (D) applies also to odd raw degrees. For \(n\le6\), its low-conductor data again have \(A+j\le2\). When \(H\) is odd and \(\deg F\) is odd, scaling all polynomials by a nonsquare change of variable reverses the sign of the summand in (C); the sum of that orbit is zero. The surviving \(F\)'s have even degree, so the reciprocity sign in (D) is 1. Thus the same degree-at-most-\(d+n\) polynomiality argument holds for every \(n\le6\), independent of \(q\bmod4\). It also extends to \(n=7\): the odd-degree \(F\)'s cancel, and the surviving conductors still have degree at most 2, with \(A+j\le3\). The new nonprincipal exceptional configurations are a quadratic conductor evaluated at a rational point, or three distinct rational roots. For distinct \(a,b\),
\[
\sum_{x\in\mathbb F_q}\eta((x-a)(x-b))=-1,
\]
and the same sum is \(-1\) for a monic irreducible quadratic. Consequently the nonzero signs in the split case occur \((q-3)/2,(q-1)/2\) times off the two roots, and in the irreducible case \((q-1)/2,(q+1)/2\) times. Repeated-root conductors give the principal signs 0 or 1. Along with the polynomial counts of cubic factorization types, these exhaust the new \(A+j=3\) cases and prove polynomiality for \(n=7\) as well. These odd raw coefficients need not themselves vanish.

Set \(d=2g+2\), \(H_d=(q-1)q^{d-1}\), \(S_n=S_{d,n}\), and \(C_i=\sum_{n=0}^iS_n\), with \(S_0=H_d\). These are the unnormalized completed coefficients through the middle. Let \(t=\sqrt q\), \(y=\sqrt q\,u+(\sqrt q\,u)^{-1}\), and \(T_0=2,T_1=y,T_{k+1}=yT_k-T_{k-1}\). If \(R(y)\) is the normalized band polynomial, then
\[
H_dt^g R(y)=N_g(y,t):=C_g(t^2)+\sum_{i=0}^{g-1}C_i(t^2)t^{g-i}T_{g-i}(y).
\tag{G}
\]
Here \(H_dt^g>0\). The script `checks/hhalf_even_uniform.py` interpolates each \(S_n\) using the proved degree bound (at most 23), with the 24 odd primes from 3 through 97 and the three extra fields 9, 101 and 103. It then proves alternating signs of (G) at the following rational \(y\)'s for **every** \(t\ge\sqrt3\):

| genus | increasing sign-test points |
|---:|---|
| 1 | \(-2,2\) |
| 2 | \(-2,0,2\) |
| 3 | \(-2,-1,1,2\) |
| 4 | \(-2,-6/5,0,1,2\) |
| 5 | \(-2,-3/2,-1/2,1/2,7/5,2\) |
| 6 | \(-2,-8/5,-1,0,4/5,3/2,2\) |
| 7 | \(-2,-33/20,-11/10,-2/5,2/5,1,8/5,2\) |

For the \(i\)-th point (indexing from zero), the polynomial \((-1)^{g-i}N_g(y_i,s+\sqrt3)\) has nonnegative coefficients in \(\mathbb Q(\sqrt3)[s]\) and positive constant term. Every comparison is exact. The script prints the raw polynomials and the certificate for every point; no floating root is used in this proof. Alternating signs give \(g\) distinct roots of \(R\) in \((-2,2)\), hence exactly the desired \(2g\) circle roots.

### Exact finite-field ranges and the independent root test

The finite grid is evaluated by (A)–(E), not by exponentiating trace means. `hhalf_exact.py` prints each full rational coefficient vector, the unhalved monotonicity verdict, and an independent Sturm certificate. For \(B\) of odd degree, remove the forced factor \(1+w\); for the remaining reciprocal degree \(2k\) polynomial, write \(B(w)/(1+w)^{g\bmod2}=w^kR(w+w^{-1})\). All roots are on the circle **iff** all roots of \(R\), counted with multiplicity, lie in \([-2,2]\). The script isolates every real root over \(\mathbb Q\), checks their total multiplicity is \(k\), and checks the rational intervals against those endpoints. For completed even conductor it instead uses \(P(u)=u^gR(qu+u^{-1})\) and certifies the band \([-2\sqrt q,2\sqrt q]\) by rational endpoint squares.

**PROVED by exact arithmetic (final finite ranges).** Every genus from 1 to the displayed endpoint is included.

| field size | odd conductor: H-half and circle | completed even conductor: circle |
|---:|---:|---:|
| 3 | 1–25 | 1–16 |
| 5 | 1–10 | 1–10 |
| 7 | 1–8 | 1–8 |
| 9 | 1–8 | 1–8 |
| 11 | 1–6 | 1–6 |
| 13 | 1–6 | 1–6 |

These are 63 odd and 54 completed-even certificates. Every odd first-half inequality is strict when nonvacuous. The attempted next \(q=3\) coefficient (\(m=13\), needed for genera 26–27) was interrupted before its full series was obtained; it is explicitly marked unfinished in its log and contributes **no** certified case. In particular neither genus 30 nor all genera are inferred from the limiting-density diagnostics.

### A fixed-genus, sufficiently-large-field consequence

**PROVED, with no explicit threshold claimed.** For each fixed genus \(g\), A1 holds for both conductor parities for all sufficiently large odd prime powers \(q\). This is not a statement uniform in \(g\).

One can establish the needed limit directly from the exact formulas. For \(n=2m\le g\), the square density differs from 1 by \(O_g(q^{-1})\), by a union bound over the primes of \(a\). In (A), bound every raw coefficient of \(L_h\) by the number \(q^j\) of monic test polynomials. The denominator coefficient counts depend only on \(g\), and the terms of fixed \(A\) in the normalized nonsquare sum are \(O_g(q^{3m-d-3A})\). Since \(d=2g+1\) or \(2g+2\), these tend to zero. For general \(n\le g\), the same bound is \(O_g(q^{3n/2-d-3A})\). Division by \(1-u\) in the even case adds only lower normalized terms, which vanish in the limit when their degree is smaller. Functional equations now show that both normalized averages converge coefficientwise to
\(1+z^2+\cdots+z^{2g}\), \(z=\sqrt q\,u\).

This limiting polynomial has simple unit-circle roots. Around each root choose a small disjoint angular-annular neighborhood invariant under \(z\mapsto1/\overline z\). Nearby polynomials have exactly one root in each neighborhood. Real reciprocal symmetry sends that root to another root in the same neighborhood, so uniqueness forces it to be fixed by the involution. Its modulus is therefore exactly 1. This proves the stated eventual result by root continuity. The argument gives neither H-half for large \(g\) nor a computable uniform range without explicit error and separation constants.

## 3. A2-3 — whole cubic covers

**PROVED by exact enumeration (all five requested cells).** The ensemble is uniform on *monic squarefree polynomials*, not on isomorphism classes. The completed full numerator is the product of the two conjugate cubic factors for each individual polynomial before averaging. Infinity is ramified when \(3\nmid d\); when \(3\mid d\), each raw character factor is divided by \(1-u\). The genera are \(d-1\) and \(d-2\), respectively.

`checks/cubic_whole.py` computes in \(\mathbb Z[\omega]\), \(\omega^2+\omega+1=0\), and obtains:

| \(q,d\) | family size | full average |
|---|---:|---|
| 7,3 | 294 | \(1+2u+7u^2\) |
| 7,4 | 2058 | \(1+43u^2/7+14u^3+43u^4+343u^6\) |
| 7,5 | 14406 | \(1+300u^2/49+86u^3/7+304u^4/7+86u^5+300u^6+2401u^8\) |
| 13,3 | 2028 | \(1+2u+13u^2\) |
| 13,4 | 26364 | \(1+157u^2/13+26u^3+157u^4+2197u^6\) |

All five satisfy the circle property by **rational Sturm isolation**, independently of the numerical roots. For the new cell \((7,5)\), the polynomial \(R\) defined by \(\overline P(u)=u^4R(7u+u^{-1})\) is
\[
R(x)=x^4-\frac{1072}{49}x^2+\frac{86}{7}x+\frac{390}{7}.
\]
The lower-degree formulas and the new degree-five result do not settle arbitrary degree or other ramification types.

**PROVED (the correct unitary Haar comparison).** For the standard representation \(V\) of \(U(r)\), the isotypic Haar average is 1. For the *whole* representation \(V\oplus\overline V\), however,
\[
\int_{U(r)}\det(1-zU)\det(1-z\overline U)\,dU=\sum_{j=0}^{r}z^{2j}.
\]
Indeed the exterior powers \(\wedge^jV\) are pairwise inequivalent irreducibles, and character orthogonality leaves only the pairs \(i=j\). The representation, and whether conjugate factors are multiplied before averaging, therefore matter as much as the name of the compact group.

**OPEN (a precise surviving family conjecture).** For every odd prime power \(q\equiv1\pmod3\) and \(d\ge2\), the uniform monic-squarefree full numerator average for \(y^3=f\), with the infinity convention above, has all roots on \(|u|=q^{-1/2}\). This lane proves only the five cells in the table (and inherits the previous genus-one argument). Fixed cube-free ramification-type components are different ensembles and are not silently included.

**SHARPENED (no monodromy-only iff).** A general exact finite-field criterion cannot simply be “symplectic or unitary monodromy.” The Haar limit predicts a limiting polynomial, and simple circle roots make that prediction stable within the self-reciprocal class for sufficiently large fields; it supplies no all-field error bound. Even on \(USp(4)\), the full-support probability measure \((1-\varepsilon)\,dU+\varepsilon(\delta_I+\delta_{-I})/2\) has averaged determinant \(1+(1+5\varepsilon)z^2+z^4\), which fails the circle property for \(\varepsilon>1/5\). This is an obstruction to inferring an exact theorem from the compact group alone, not a claimed counterexample among the specified cubic covers. Conversely, constant genus-one curve families satisfy the circle property by Weil and have trivial geometric monodromy, so the proposed “exactly” needs exclusions even as a necessity statement.

## 4. A2-4 — the graph and the ladder

**SHARPENED (scope).** The hyperelliptic result concerns one explicitly weighted arithmetic average of characteristic polynomials; its proof uses reciprocity, squarefree Euler factors, functional equations and coefficient inequalities. The graph theorem instead averages the full dual of a fixed cycle lattice and cancels every nonmatching determinant term. Varying branch divisors varies cohomology and does not identify a fixed integral lattice or a common invariant vacuum. Nor does a common vacuum prove an average theorem: the commuting normalized steps \(I_4,-I_4\) preserve the same vacuum but average to \(1+6z^2+z^4\), with radii \(\sqrt2\pm1\). Consequently these function-field results are finite positive examples for `data-ladder.md` §4, while the failure of the common-vacuum and monodromy-only inferences belongs in §2. They do not supply the missing integral global object or positivity statement for the individual Riemann zeta function. This is the annotation warranted for `graph-super.md` §9; the graph theorem itself needs no change.

## Correction ledger

1. Averaged traces are coefficients of the averaged logarithm, not of the logarithm of the averaged polynomial.
2. Rudnick's even-power formula has both a nonzero square correction at small powers and a special endpoint at \(2g\).
3. The unhalved monotonicity requested in this round is stronger than the previous lane's sufficient H-half criterion.

4. The Haar average on the standard \(U(r)\) representation is 1; the sum \(\sum z^{2j}\) arises on \(V\oplus\overline V\). Group names without the representation and averaging convention do not determine the polynomial.
5. Knowing only the number of primes of each degree evaluates the square part, but not the full nonsquare term. Formula (E) also needs actual lower-conductor character polynomials. “Only primes up to a finite degree” is not a polynomial-time all-genus computation by itself.
6. The formulas allow odd prime powers. The old numerical helper was prime-field only; replacing its modulus by 9 would not define \(\mathbb F_9\). The new extension-field implementation is independently enumerated in `audit_lane.py`.
7. Completion and conventions remain essential: even quadratic conductor requires division by \(1-u\); a cubic conductor divisible by 3 requires division in both character factors. For odd quadratic conductor and \(q\equiv3\pmod4\), the stated Jacobi convention is the constant twist of \(y^2=D\); even traces and the averaged even polynomial agree with the curve convention.

## Numerical checks for the blind lane

From the repository root, all of the following write only within this lane:

```bash
python3 notes/astra-2026-10-25/hhalf/checks/hhalf_exact.py
python3 notes/astra-2026-10-25/hhalf/checks/hhalf_exact.py --even --grid 3:16,5:10,7:8,9:8,11:6,13:6
python3 notes/astra-2026-10-25/hhalf/checks/hhalf_low_genus.py
python3 notes/astra-2026-10-25/hhalf/checks/hhalf_even_uniform.py
python3 notes/astra-2026-10-25/hhalf/checks/hhalf_rudnick.py
python3 notes/astra-2026-10-25/hhalf/checks/cubic_whole.py
python3 notes/astra-2026-10-25/hhalf/checks/audit_lane.py
python3 notes/astra-2026-10-25/hhalf/checks/square_density.py
```

Dependencies: Python, python-flint, SymPy, NumPy and mpmath; PARI is not needed. The default exact grid is the final odd-conductor table. Integer `series_q*_*.json` files cache exact coefficient series; removing a cache causes recomputation by `exact_core.py`. The universal symbolic proofs do not rely on these caches. The larger uncached coefficient calculations take substantially longer than the small-field enumeration.

Six blind checks, all printed in the saved outputs:

1. At \((q,g)=(3,4)\), \(b_2=14570/19683\) and \(b_1-b_2=202/19683\). The universal genus-four gap certificate is the positive vector displayed after (F).
2. At \((3,25)\),
   \[
   b_{12}=\frac{10374538959518283947503733404}{14130386091738734504764811067},\qquad
   \min_{1\le m\le12}(b_{m-1}-b_m)=
   \frac{1005197384760100172}{14130386091738734504764811067}>0.
   \]
   The independent Sturm test accounts for all 25 roots of \(B\), including its forced root \(-1\).
3. Independent enumeration over \(\mathbb F_9\) gives \(|\mathcal H_5|=52488\) and
   \(\overline L_{9,2}=1+(5912/729)u^2+81u^4\).
4. For completed even conductor at \((q,g)=(3,7)\), the coefficient of \(u\) is \(4782968/4782969\). The uniform seven-root bracket certificate uses the last row of the table following (G).
5. The new whole-cubic cell \((7,5)\) has \(14406\) members and the full average in §3; its band polynomial is \(x^4-1072x^2/49+86x/7+390/7\), with all four roots in \((-2\sqrt7,2\sqrt7)\).
6. At \((q,g)=(3,1)\), the true averaged normalized determinant is \(1+z^2\), whereas exponentiating the mean logarithm gives coefficient \(5/9\) at \(z^2\). The exact mean second trace is \(-10/9\).

`checks/reproduced/` contains byte-identical copies of all six prior computational scripts and their helper. They were rerun there, including the saved-output summary. `output_audit_lane.txt` records source hashes and exact-line agreement with the read-only old outputs; it also checks the optimized dual calculation against the original dual series, the auxiliary primitive numerators against direct Jacobi sums, 18 odd-raw-coefficient comparisons with the original A2 formula, and 78 cross-degree family functional equations. The direct \(\mathbb F_9\) enumeration is separate from the grouped-prime evaluation. No number-field zeros enter any calculation. Floating cubic roots are diagnostics; the rational Sturm and symbolic sign certificates carry the conclusions.

## What this changes in the notebook

No record page or claim database was edited. Proposed rows, subject to review:

| candidate | status | precise scope |
|---|---|---|
| `prop:quadratic-average-degree-reduction` | PROVED | Exact formulas (A)–(E); raw degree \(2m\) reduces to character moduli of degree at most \(m-1\). |
| `thm:hyperelliptic-average-genus-seven` | PROVED by exact algebraic certificate | H-half and A1 for every odd prime power and \(1\le g\le7\). |
| `thm:even-hyperelliptic-average-genus-seven` | PROVED by exact algebraic certificate | Completed even-conductor A1 for every odd prime power and \(1\le g\le7\). |
| `obs:hyperelliptic-average-extended-certificates` | PROVED by exact computation | The final 63-case odd and 54-case completed-even tables in §2. |
| `lem:square-density-uniform-positive` | PROVED | Bounds (I) and the exact fixed-coefficient limit (J); no full-average monotonicity inference. |
| `prop:hyperelliptic-average-fixed-genus-large-field` | PROVED | For each fixed genus, both conductor parities have A1 for sufficiently large \(q\); no explicit or genus-uniform threshold supplied. |
| `obs:cubic-whole-average-degree-five` | PROVED by exact computation | Whole monic-squarefree cyclic cubic average at \((7,5)\), plus reproduction of the four requested degree-3/4 cases. |
| `conj:hyperelliptic-average-all-genus` | OPEN / PARTIAL | Neither unrestricted H-half nor unrestricted A1 is proved or refuted here. Do **not** register `thm:hyperelliptic-average-all-genus`. |
| `conj:whole-squarefree-cubic-average` | OPEN | The precise uniform monic-squarefree, whole-numerator conjecture in §3; other ramification types excluded. |

Suggested one-line annotations:

- `ff-dirichlet.md`: “Exact hyperelliptic averages satisfy RH for all odd field sizes through genus 7 in both conductor parities after completion, with larger finite certificates; the all-genus assertion remains open, and mean power traces cannot be exponentiated to obtain the mean polynomial.”
- `graph-super.md` §9: “Hyperelliptic and whole-cubic averages provide further exact finite-field examples, but their arithmetic coefficient mechanism differs from the graph's fixed-lattice character cancellation; monodromy and a common vacuum alone do not prove an average theorem.”
- `data-ladder.md` §2: retain the failed geometric/level dichotomy and add the common-vacuum/average-determinant obstruction; §4 may link the uniform genus-seven theorems and finite tables as positive examples, without claiming new positivity data for \(\zeta\).

The next uniform step is to control the **difference of adjacent nonsquare corrections** in (D), or equivalently the averages of primitive exterior-power characters, at \(m\) proportional to \(g\). The fixed-\(m\) limit and the stable first moment do not supply that estimate. The next computational step is to finish the \(m=13\) grouped series and then test genera 26–27; no prediction about those cells is substituted for a certificate.
