# Exact averages over function-field characters (lane A)

Author: `codex:gpt-6-astra`, 2026-10-23.

Status: record, not a registration. **A4's proposed geometric/level dichotomy is REFUTED**, already by the completed cubic isotypic average \(1+u\) at \((q,d)=(7,3)\). A1 holds in the cases proved below; its unrestricted form is not assumed. All computations use coefficients and finite-field character sums, never number-field zeros. The functional equation is used as an algebraic theorem, independently of Weil RH.

## 1. A2 — exact squarefree average

**PROVED (Euler-product formula).** Write \(\epsilon=(-1)^{(q-1)/2}\), \(H_d=q^d-q^{d-1}\) for \(d\ge2\), and let \(f=a^2h\), with \(a,h\) monic and \(h\) squarefree (they need not be coprime). Put \(\chi_h(B)=(B/h)\). For \(h=1\) interpret \(L(t,\chi_1)=(1-qt)^{-1}\). Quadratic reciprocity gives

\[
T_d(a,h):=\sum_{D\in\mathcal H_d}\chi_D(a^2h)
=\epsilon^{d\deg h}[t^d]\frac{L(t,\chi_h)}{L(t^2,\chi_h^2)}
\prod_{P\mid a,\ P\nmid h}(1+\chi_h(P)t^{\deg P})^{-1}.                 \tag{1}
\]

Indeed the squarefree Euler factor is \(1+\chi_h(P)t^{\deg P}\); primes dividing \(h\) already have factor 1, and primes dividing \(a\) are forbidden. For \(h\ne1\),

\[
L(t^2,\chi_h^2)=\frac{\prod_{P\mid h}(1-t^{2\deg P})}{1-qt^2}.
\]

For squares the exact coprimality count is

\[
T_d(a,1)=[t^d]\frac{1-qt^2}{1-qt}\prod_{P\mid a}(1+t^{\deg P})^{-1}.       \tag{2}
\]

Thus, for odd \(d=2g+1\),

\[
\overline L_{q,g}(u)=\sum_{m=0}^g c_{d,m}(qu^2)^m+R_{d}(u),\qquad
c_{d,m}=\frac1{H_d q^m}\sum_{\deg a=m}T_d(a,1),                         \tag{3}
\]
\[
R_d(u)=\frac1{H_d}\sum_{\substack{a,h\ \text{monic},\ h\ \text{squarefree},\ \deg h>0\\2\deg a+\deg h\le2g}}T_d(a,h)u^{2\deg a+\deg h}.                   \tag{4}
\]

These are finite exact formulas, including the non-square remainder; no replacement of a finite-degree coprimality density by its limit is made. In (1) the primitive numerator has degree \(\deg h-1\), with its trivial factor retained when \(\deg h\) is even. Swapping the two finite sums in the Dirichlet polynomial proves (3)–(4).

**PROVED (a second exact formula for the square density).** If \(z\) marks \(\deg a\), summing (2) over all monic \(a\) gives

\[
c_{d,m}=\frac{[t^dz^m]}{H_dq^m}
\prod_P\left(1+t^{\deg P}+\frac{z^{\deg P}}{1-z^{\deg P}}\right)
=\frac{[t^dz^m]}{H_dq^m}\frac{1-qt^2}{(1-qt)(1-qz)}
\prod_P\left(1-\frac{(tz)^{\deg P}}{1+t^{\deg P}}\right).             \tag{5}
\]

The products are formal power series, so each indicated coefficient requires only finitely many primes. In particular the main term is computable by exact finite arithmetic. The finite density \(c_{d,m}\) is not a root-location theorem for the full average.

**NUMERICAL / exact coefficient verification.** `checks/avg_hyperelliptic.py` enumerates every squarefree \(D\), computes the coefficients through genus using finite-field Euler factors, and uses the algebraic functional equation for the remaining coefficients. Independently it evaluates (1)–(4) through the *full* raw degree with lower-conductor Jacobi sums (odd coefficients at odd \(d\) use the proved symmetry below); those auxiliary primitive polynomials use their own algebraic functional equations above their midpoint. The resulting full A2 coefficients agree and obey the functional equation. Thus the comparison is independent at the character-sum level, not a second proof of the functional equation. Counts and coefficients are integers or rational numbers; the root diagnostics are floating point followed by 80-digit Newton refinement. `checks/audit_identities.py` adds full direct Dirichlet sums, with no midpoint reconstruction, for \((q,g)=(3,1),(3,2),(5,1),(5,2)\), and the even case \((3,1)\); it also independently checks squarefreeness by polynomial gcd.

| \(q\) | \(g\) | \(|\mathcal H_{2g+1}|\) | exact average | A2 comparison |
|---|---:|---:|---|---|
| 3 | 1 | 18 | \(1+3u^2\) | exact |
| 3 | 2 | 162 | \(1+\frac{62}{27}u^2+9u^4\) | exact |
| 3 | 3 | 1458 | \(1+\frac{551}{243}u^2+\frac{551}{81}u^4+27u^6\) | exact |
| 5 | 1 | 100 | \(1+5u^2\) | exact |
| 5 | 2 | 2500 | \(1+\frac{524}{125}u^2+25u^4\) | exact |
| 5 | 3 | 62500 | \(1+\frac{13029}{3125}u^2+\frac{13029}{625}u^4+125u^6\) | exact |
| 7 | 1 | 294 | \(1+7u^2\) | exact |
| 7 | 2 | 14406 | \(1+\frac{2106}{343}u^2+49u^4\) | exact |
| 7 | 3 | 705894 | \(1+\frac{102955}{16807}u^2+\frac{102955}{2401}u^4+343u^6\) | exact |

For example, at \((q,g)=(5,2)\), the square and nonsquare contributions to \([u^2]\overline L\) are respectively \(521/125\) and \(3/125\). **The nonsquares do not cancel.** This already distinguishes (1) from the graph's constant-term projection.

## 2. A1/A3 — what the functional equation does prove

**REFUTED (A3's global monotonicity premise, for every odd \(q\) and \(g\ge2\)).** The normalized coefficients are palindromic, with endpoints 1; a monotone sequence with equal endpoints must be constant. In fact its next coefficient is strictly less than 1, as calculated below. This refutes that proof route, not A1.

**PROVED (odd coefficients vanish).** For \(b\in\mathbb F_q^\times\), the map \(D(x)\mapsto b^{-d}D(bx)\) permutes \(\mathcal H_d\). Substituting the corresponding monic \(f\)'s in the Jacobi sum multiplies its degree-\(n\) coefficient by \(\eta(b)^{dn}\), where \(\eta\) is the quadratic character of the constant field. For odd \(d\), choose nonsquare \(b\); all odd coefficients average to zero. Hence

\[
\overline L_{q,g}(u)=B_{q,g}(w),\quad w=qu^2,\quad
B_{q,g}(w)=\sum_{m=0}^g b_mw^m,\quad b_m=b_{g-m},\quad b_0=b_g=1.       \tag{6}
\]

The reciprocity sign in (1) also explains the convention issue: \((f/D)=\epsilon^{d\deg f}(D/f)\). For odd \(d\) and \(q\equiv3\pmod4\) the Jacobi convention in the brief gives the constant quadratic twist of \(y^2=D\); its individual numerator is obtained by \(u\mapsto-u\). The average in (6) is unchanged. For even \(d\) the two conventions coincide.

**PROVED (first nontrivial coefficient for all genus).** For \(d=2g+1\),

\[
b_1=\frac{q}{q+1}+q^{-2g}
\left(\frac1{q+1}+\frac{(q-1)g-1+\delta_g}{2}\right),\qquad
\delta_g=\begin{cases}q&g\text{ odd},\\-1&g\text{ even}.\end{cases}   \tag{7}
\]

To prove this without an asymptotic estimate, the \(q\) linear squares contribute
\(q^2/(q+1)+q^{1-2g}/(q+1)\) to \([u^2]\overline L\). The \(q(q-1)/2\) products of two distinct linear primes have \(L(t,\chi_h)=1-t\) and denominator \((1-t^2)^2\) in (1); each contributes \((q-1)g-1\) to the unnormalized squarefree sum. The equally numerous irreducible quadratics have denominator \(1-t^4\) and contribute \(\delta_g\). Division by \(H_dq\) gives (7). It yields \(b_1=1\) for \(g=1\) and \(0<b_1<1\) for every \(g\ge2\): the bracket is at most \((q-1)(g+1)/2+1/(q+1)\), and \(q^{2g}>1+(q^2-1)(g+1)/2\) for \(q\ge3,g\ge2\) (base \(g=2\), then induction).

**PROVED (a corrected half-polynomial criterion).** Let \(g\ge1\) and let \(B(w)=\sum_{m=0}^g b_mw^m\) be real, reciprocal, with \(b_0=1\). Put

\[
P(w)=\begin{cases}
\sum_{m=0}^{(g-1)/2}b_mw^m,&g\text{ odd},\\
\sum_{m=0}^{g/2-1}b_mw^m+\tfrac12b_{g/2}w^{g/2},&g\text{ even}.
\end{cases}
\]

**H-half:** the coefficients of \(P\) are nonnegative, nonincreasing, with constant coefficient strictly larger than the coefficient of \(w\) when \(\deg P>0\), and its last nonzero coefficient positive. Under H-half every root of \(B\) lies on \(|w|=1\).

Proof: Eneström–Kakeya gives no root of \(P\) in the open disk. For the boundary, with \(k=\deg P\), \((1-w)P(w)=p_0-\sum_{j=1}^{k}(p_{j-1}-p_j)w^j-p_kw^{k+1}\); equality in the triangle inequality, together with \(p_0>p_1\), forces \(w=1\), where \(P(1)>0\). Thus \(P\) has no root on the closed disk. The function \(R(w)=w^gP(1/w)/P(w)\) is analytic there, has modulus 1 on the boundary and is nonconstant with \(R(0)=0\). The maximum modulus principle gives \(|R|<1\) inside, so \(B=P(1+R)\) has no root inside. Reciprocity excludes roots outside. Constant \(P\) gives the same conclusion directly. This is the elementary self-reciprocal variant of the Eneström–Kakeya argument, also associated with Chen–Chinen; the proof here includes the halved central coefficient.

**PROVED (unconditional A1 in low genus).** A1 holds for every odd prime power \(q\) and \(1\le g\le3\). For \(g=1\), \(B=1+w\). For \(g=2\), \(B=1+b_1w+w^2\) with \(0<b_1<1\), and for \(g=3\), \(B=(1+w)(1+(b_1-1)w+w^2)\). Each has all its roots on the unit circle; alternatively H-half applies.

**PROVED-conditional (general A1).** For every odd prime power \(q\) and \(g\ge1\), A1 follows from H-half for the exact coefficients (1)–(6). This is a finite rational-inequality certificate, not an RH hypothesis. The unrestricted assertion that H-half, or A1 itself, holds for all \((q,g)\) remains **OPEN here**; numerical evidence is not promoted to a universal proof.

**PROVED (finite extensions by exact certificates).** `checks/avg_extended.py` verifies H-half as exact rational inequalities for every genus in these ranges:

| field size | odd-degree genera proved by exact arithmetic | completed even-degree genera proved by exact arithmetic |
|---:|---|---|
| 3 | 1–12 | 1–6 |
| 5 | 1–8 | 1–4 |
| 7 | 1–6 | 1–4 |

It independently forms the rational polynomial \(R(x)\) with \(P(u)=u^gR(qu+u^{-1})\), using \(S_0=2,S_1=x,S_{k+1}=xS_k-qS_{k-1}\). Rational Sturm isolation verifies that all \(g\) roots of \(R\), counted with multiplicity, lie in \((-2\sqrt q,2\sqrt q)\): each isolating interval's rational endpoints have square less than \(4q\). This supplies an exact band certificate for both parities, separate from floating-point root finding. The extended cases use A2 plus the functional equation, not brute-force enumeration of \(\mathcal H_d\). No counterexample to A1 was found.

**OPEN (corrected sufficient conjecture).** The exact coefficients satisfy \(1=b_0\ge b_1\ge\cdots\ge b_{\lfloor g/2\rfloor}>0\) for every odd \(q\) and every \(g\). This stronger version of H-half holds in all 26 listed odd-degree cases (`checks/summarize_outputs.py`). Proving this arithmetic inequality, or finding its failure and then testing A1 by the independent band criterion, is the remaining universal step. The symplectic Haar model gives \(\int_{USp(2g)}\det(1-zU)\,dU=\sum_{m=0}^g z^{2m}\) (the invariant exterior powers have dimension one in even degree and zero in odd degree); it is a useful **HEURISTIC** for the average but does not remove the exact arithmetic corrections in (1) and (7).

## 3. A4 — ensemble verdicts

### 3.1 Even-degree hyperelliptic covers

**SHARPENED.** For monic squarefree \(D\) of degree \(2g+2\), infinity splits into two rational points. The raw Dirichlet polynomial has degree \(2g+1\) and a factor \(1-u\); the curve numerator is \(P_D=L(u,\chi_D)/(1-u)\), of degree \(2g\). Its average inherits the curve functional equation. Formula (1) applies with even \(d\); divide the resulting average by \(1-u\). The odd coefficients need not vanish, because scaling \(x\) now preserves the square class of the leading coefficient.

**PROVED (genus one, all odd \(q\)).** The completed average is
\[
\overline P_{q,1}^{\rm even}(u)=1+(1-q^{-2})u+qu^2.                  \tag{8}
\]
For a linear \(h\), \(L(t,\chi_h)=1\), so (1) becomes \((1-qt^2)/(1-t^2)\). Its coefficient at even positive \(d\) is \(1-q\). Summing over the \(q\) linear \(h\)'s yields \([u]\overline L=-q^{2-d}\), and division by \(1-u\) gives (8). Its discriminant is negative and its root product is \(1/q\), proving the circle statement. More generally \([u]\overline P=1-q^{-2g}\).

**PROVED (genus two, all odd \(q\)).** Put \(A=1-q^{-4}\) and \(B=q+q^{-1}-q^{-2}-q^{-3}\). Then
\[
\overline P_{q,2}^{\rm even}(u)=1+Au+Bu^2+qAu^3+q^2u^4.              \tag{8a}
\]
For the raw \(u^2\) coefficient the square part is \(q^2/(q+1)-q^{-4}/(q+1)\). In (1), split squarefree quadratics contribute \(4-3q\), and irreducible quadratics contribute \(-q\), giving nonsquare part \(-2(q-1)q^{-4}\). Add the raw constant and linear coefficients to divide by \(1-u\), obtaining \(B\). Set \(z=\sqrt q\,u\) and \(y=z+z^{-1}\). The normalized polynomial divided by \(z^2\) is
\(y^2+(A/\sqrt q)y+(B/q-2)\). Its value at 0 is negative, and at both \(\pm2\) is positive, since \(-1<B/q-2<0\) and \(0<A/\sqrt q<1/\sqrt q\). Thus its two real roots are in \((-2,2)\), proving the circle statement.

**NUMERICAL with exact coefficients.** The script enumerates all \(D\) for \(q=3,5,7\) and \(g=1,2\), checking (8) and (8a) against A2. For example,
\[
\overline P^{\rm even}_{3,2}=1+\frac{80}{81}u+\frac{86}{27}u^2+\frac{80}{27}u^3+9u^4.
\]
The raw averages always have the extra off-circle root \(u=1\). That trivial factor is not counted as a counterexample to geometric RH. The unrestricted completed even-degree assertion is **OPEN here**.

### 3.2 Cyclic cubic covers

**REFUTED (A4ii and the claimed geometric/level dichotomy).** For every odd prime power \(q\equiv1\pmod3\), take all monic squarefree \(D\) of degree 3 and one fixed embedding of \(\mu_3\) in \(\mathbb C\). For the cubic character \(\chi_D(f)=\prod_{P\mid D}(f/P)_3\),
\[
\overline L(u)=1-u^2,\qquad \overline{L^*}(u)=1+u.                  \tag{9}
\]
Thus the completed average has the off-circle root \(u=-1\), with \(|u|\sqrt q=\sqrt q\). The smallest odd field allowed is \(q=7\); degrees 1 and 2 have constant average, so degree 3 is the first nonconstant counterexample in this family.

Proof: the cubic reciprocity sign is trivial. For a linear test polynomial \(h\), both nontrivial characters \(\chi_h\) and \(\chi_h^2\) have raw \(L\)-polynomial 1, so
\[
\sum_{D\ \text{monic squarefree}}\chi_h(D)t^{\deg D}
=\frac{L(t,\chi_h)}{L(t^2,\chi_h^2)}=1.
\]
Consequently the average coefficient of \(u\) is zero, in every positive degree. For degree 3 the character is even, and every raw polynomial has degree 2 and vanishes at 1. Its average is therefore \(1-u^2\), proving (9). At degree 2 the same vanishing gives average 1 although each member has degree 1: **degree collapse**, not evidence of a degree-preserving circle theorem.

**PROVED by exact enumeration (a counterexample with ramified infinity too).** At both \(q=7,13\), degree 4 gives
\(\overline L=1+qu^3\). Here the character is odd, so no factor is removed. The three roots have normalized radius \(q^{1/6}>1\). This is verified exactly by `checks/avg_cubic.py`; (9), rather than an unproved formula in degree 4 for all \(q\), supplies the general refutation.

**SHARPENED (isotypic versus whole-curve average).** The whole numerator of \(y^3=D\) is \(L^*(u,\chi_D)L^*(u,\overline\chi_D)\). Averaging this product is different from multiplying the averages. The checked whole-curve averages are \(1+qu^2\) in degree 2, \(1+2u+qu^2\) in degree 3, and, at \(q=7,13\),
\[
1+(q-1+q^{-1})u^2+2qu^3+(q^2-q+1)u^4+q^3u^6
\]
in degree 4. For \(q=7,13\), degrees 1–4, the whole-curve circle statements are **PROVED by exact enumeration and rational Sturm certificates** in the cubic script; its numerical roots are only a diagnostic. Degrees 2 and 3 also follow for all the stated \(q\) from the vanishing average linear character sum above, the genus-one functional equation, and the resulting negative discriminant. The general assertion about averages of *whole* curve numerators over arbitrary cover families is **OPEN here**, and is not refuted by changing the object in (9). The conjecture as asked, which specifies the cubic-character \(L\), is refuted.

The individual cubic functional equations have varying root numbers and conjugate characters. They cannot be averaged into (6). The unitary symmetry of a non-real isotypic family does not predict a nonconstant averaged characteristic polynomial with unit-circle roots: the Haar average on \(U(n)\) is 1. Symplectic symmetry and unitary symmetry must not be conflated.

### 3.3 All nontrivial characters of one irreducible modulus

**PROVED (formula in the brief, and failure).** Let \(f\) be irreducible of degree \(d\ge2\), \(Q=q^d\). Orthogonality gives
\[
\sum_\chi L(u,\chi)=(Q-1)\left(1+\frac{u^d}{1-qu}\right).
\]
Indeed the monic polynomials congruent to 1 modulo \(f\) consist of 1 and \(1+fB\) with \(B\) monic. Subtract \(L(u,\chi_0)=(1-u^d)/(1-qu)\) to obtain
\[
S_f(u)=\sum_{\chi\ne1}L(u,\chi)
=\frac{Q u^d-(qQ-q)u+(Q-2)}{1-qu}
=(Q-2)-\sum_{n=1}^{d-1}q^nu^n.                                    \tag{10}
\]
The apparent singularity at \(u=1/q\) cancels; it is not a root of \(S_f\). The average is \(S_f/(Q-2)\), independent of the choice of irreducible \(f\). Its leading coefficient has magnitude \(q^{d-1}/(Q-2)\), whereas a polynomial with constant coefficient 1, degree \(d-1\), and every root of modulus \(q^{-1/2}\) must have leading-coefficient magnitude \(q^{(d-1)/2}\). These differ for all \(q\ge3,d\ge2\). So failure is general, not just numerical.

For \((q,d)=(3,2)\), the sum is \(7-3u\), with root \(7/3\). For \((3,3)\), it is \(25-3u-9u^2\), with roots \((-1\pm\sqrt{101})/6\). The script also checks \(q=5\), both requested degrees, by constructing the finite residue field.

**PROVED (removing the even-character factors does not rescue it).** Put \(M=(Q-1)/(q-1)\); there are \(M-1\) nontrivial even characters. Orthogonality on \(\mathbb F_Q^\times/\mathbb F_q^\times\) gives their raw sum \((M-1)-\sum_{n=1}^{d-1}q^nu^n\), and the odd-character raw sum is the constant \(Q-1-M\). Consequently
\[
\sum_{\chi\ne1}L^*(u,\chi)
=(Q-2)+\sum_{n=1}^{d-2}\frac{Q-q^{n+1}}{q-1}u^n.                  \tag{11}
\]
It is constant for \(d=2\); at \(d=3\), the root is \(-(q^3-2)/q^2\), still off circle. More generally for \(d\ge3\) the same leading-coefficient magnitude test refutes the circle property. This is a sum of different member degrees, so the degree collapse must also be recorded.

### 3.4 Primitive characters of exact order \(N\) at a fixed irreducible level

**PROVED (exact formula; no uniform yes/no verdict).** Assume \(N>1\) divides \(Q-1\); otherwise the family is empty. All such characters are primitive because the modulus is irreducible. Fix a generator \(\gamma\) of \(\mathbb F_Q^\times\), write \(\ell(A)=\log_\gamma(A\bmod f)\), and let
\[
c_N(k)=\sum_{a\in(\mathbb Z/N)^\times}e^{2\pi iak/N}
=\sum_{r\mid(N,k)}r\mu(N/r).
\]
Then the exact raw average is
\[
\frac1{\varphi(N)}\sum_{n=0}^{d-1}\left(\sum_{A\ \text{monic},\deg A=n}c_N(\ell(A))\right)u^n.       \tag{12}
\]
Every member is even iff \(N\mid (Q-1)/(q-1)\); in that case divide (12) by \(1-u\). These statements follow directly from the cyclic character group and the restriction to the subgroup \(\mathbb F_q^\times\).

For \(N=2\) there is just one primitive quadratic character; its completed polynomial satisfies Weil RH (labelled use of **Weil's theorem**, not an averaging theorem). Thus an assertion that *all* level ensembles fail is already false. Genuine multi-member failures include:

- \(q=5,f=x^2+2,N=4\): average \(1+2u\), root \(-1/2\), normalized radius \(\sqrt5/2\).
- \(q=7,f=x^2+1,N=3\): average \(1-2u\), root \(1/2\), normalized radius \(\sqrt7/2\).
- \(q=3,f=x^3+2x+1,N=13\): completed average \(1+3u/4\), root \(-4/3\).

All are exact Ramanujan-sum calculations in `checks/avg_level.py`. Some other orders have constant averages. Exact order is not a character subgroup: deleting the trivial character or selecting primitive orders changes orthogonality into Ramanujan sums, so this is not the graph's average over every element of \(H^1(Y,\mathbb Z/N)\).

### 3.5 What is actually fixed in the three averages?

**SHARPENED (ladder interpretation).** On the graph, \(Y\), its integral cycle lattice \(H_1(Y,\mathbb Z)\), and the determinant template are fixed. The full character group \(\operatorname{Hom}(H_1,\mu_N)\), including the identity, is averaged. The determinant expansion has exponents only \(0,\pm1\) in each cotree variable, so every nonconstant cycle term disappears and the matching polynomial remains. Heilmann–Lieb then supplies the band theorem.

At fixed function-field level, one really is varying characters of a fixed ray-class quotient (or rank-one local systems on one punctured base). This is the closer character-group analogue of a fixed graph, but its Dirichlet polynomial is not a multiaffine graph determinant; its divisor expansion and its trivial member have different behavior. At varying squarefree \(D\), both the punctured base and ramification data vary, and the covers' cohomologies vary. This is **not** the full dual of one fixed \(H_1\), even though the genus can be held fixed.

Lane M concerns commuting linear operators on one fixed symplectic space and their common invariant complex structure. It does not identify the Frobenius operators of different curves on one canonically fixed lattice. Even a common vacuum would not make the average of their characteristic polynomials real-rooted/on-circle. Hence neither implication of the proposed "exact parallel" is justified. The surviving distinction is between a proven determinant cancellation mechanism, an arithmetic family satisfying extra coefficient inequalities, and an unstructured linear average; "geometric versus level" is not a theorem.

**PROVED (explicit obstruction to the vacuum inference).** The normalized steps \(I_4\) and \(-I_4\) commute and preserve every compatible vacuum. Nevertheless their average determinant is
\(\tfrac12((1-z)^4+(1+z)^4)=1+6z^2+z^4\), whose root moduli are \(\sqrt2-1\) and \(\sqrt2+1\). This elementary example, printed by the independent audit, separates a common invariant metric from a theorem about an average determinant.

## 4. A5 — number fields (OPEN / HEURISTIC; no zero data)

Let \(\mathcal F_X\) be the nontrivial fundamental discriminants \(1<|d|\le X\), \(a_d=(1-\chi_d(-1))/2\), and
\[
\Lambda_d(s)=\left(\frac{|d|}{\pi}\right)^{(s+a_d)/2}
\Gamma\left(\frac{s+a_d}{2}\right)L(s,\chi_d),\qquad
\mathcal A_X(s)=\frac1{|\mathcal F_X|}\sum_{d\in\mathcal F_X}\Lambda_d(s).       \tag{13}
\]
Each nontrivial primitive quadratic completion is entire with root number +1, so \(\mathcal A_X(s)=\mathcal A_X(1-s)\). The direct determinant-average analogue would assert that every zero of this entire function lies on \(\Re s=1/2\). This is a well-defined **OPEN proposal**, not a consequence of the members' functional equations, nor a theorem established by the finite-field calculations. The normalization matters: the conductor-dependent completion weights the members very differently. Restricting to one parity and a conductor interval, or replacing \(\Lambda_d\) by \(\Lambda_d/\Lambda_d(2)\), defines a different plausible experiment; the latter normalization uses an absolutely convergent Euler product at 2, not zero data.

A second, prime-defined object is better aligned with the notebook's positivity rung. For \(h\in C_c^\infty(\mathbb R)\), set \(f=h*\widetilde h\), \(\widetilde h(x)=\overline{h(-x)}\), and \(\widehat f(t)=\int f(x)e^{itx}\,dx\). Define the averaged Weil form by
\[
\begin{split}
\mathcal W_X(h)={}&f(0)\left\langle\log\frac{|d|}{\pi}\right\rangle
+\frac1{2\pi}\int_{\mathbb R}\widehat f(t)
\left\langle\Re\psi\left(\frac14+\frac{a_d}{2}+\frac{it}{2}\right)\right\rangle dt\\
&-\sum_{n\ge2}\frac{\Lambda_{\rm vM}(n)}{\sqrt n}
\langle\chi_d(n)\rangle\,[f(\log n)+f(-\log n)].
\end{split}                                                               \tag{14}
\]
Here \(\psi=\Gamma'/\Gamma\), \(\Lambda_{\rm vM}\) is von Mangoldt's function, and the compact support makes the prime-power sum finite. All inputs are conductors, parity, primes, and the archimedean factor. There is no pole term because the principal character was excluded; adding \(\zeta\) requires its explicit pole contribution. The positivity proposal is \(\mathcal W_X(h)\ge0\) for every such \(h\). This averages a linear explicit-formula functional; it corresponds to a sum of logarithmic derivatives, hence to a product of completed functions, **not** to the logarithmic derivative of (13). It is a different question from RH for the sum (13).

The finite-field evidence predicts only that self-duality plus a suitable *additional coefficient or positivity mechanism* can make an average special. It supplies no replacement for that mechanism over \(\mathbb Q\): there is no fixed-degree reciprocal polynomial, no proven H-half inequality for (13), and nonsquare character sums do not vanish exactly. The cubic counterexample rules out the blanket prediction from being a family of covers. Averaging a zero-counting measure would instead concern the members' spectra; it would not test (13), and no such measure is used here. None of these averaged questions transfers positivity to the individual \(\zeta\) functional without a further argument.

## Correction ledger

1. The brief's primitive-even degree convention suppresses the factor \(1-u\). Raw \(L\) has degree \(d-1\); completed \(L^*\) has degree \(d-2\). Even hyperelliptic infinity splits for monic \(D\).
2. With \(\chi_D(f)=(f/D)\), odd-degree \(D\) over \(q\equiv3\pmod4\) describes the constant quadratic twist of the stated affine model. This does not change its even average, but the individual convention must be stated.
3. The quadratic nonsquare terms do not all average to zero. The finite squarefree and coprimality restrictions in (1) are essential.
4. Global positive monotonicity in \(w\) is impossible for the nonconstant palindromic coefficient sequences at \(g\ge2\). A half-polynomial version repairs the sufficient criterion, but a universal arithmetic proof of its hypothesis is not supplied.
5. Geometric cubic **isotypic** averages fail even after completion; they do not share a fixed root number. Whole-curve products are distinct and remain open in general.
6. Removing the trivial character or selecting exact order is not the full \(N\)-torsion average of the graph theorem. In particular \(N=2\) at irreducible level is a singleton success, not a failure.
7. Varying the branch divisor does not keep one \(H_1\) fixed. Lane M's common-vacuum theorem does not imply a polynomial-average theorem.
8. Statistical symplectic/unitary symmetry is not an exact finite-field coefficient identity. Rudnick's trace averages are not the average of the characteristic polynomial: expectation commutes with trace, but generally not with exponentiation, determinant, or logarithm.

## Literature and provenance

Bibliographic references requested in the brief are cited from standard knowledge, with primary-source links checked for identity and scope; no external text is quoted. The exact ensemble calculations and proofs above are given in full and do not depend on interpreting an asymptotic result as an exact one.

- Z. Rudnick, *Traces of high powers of the Frobenius class in the hyperelliptic ensemble*, Acta Arith. **143** (2010), 81–99: character-sum framework and comparison of trace statistics with the symplectic group, not an exact average-polynomial RH theorem. [Author's paper](https://www.math.tau.ac.il/~rudnick/papers/acta2010.pdf).
- N. Katz and P. Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*, AMS Colloquium Publications **45** (1999): monodromy/equidistribution and symmetry types. [AMS](https://doi.org/10.1090/coll/045).
- A. Bucur, C. David, B. Feigon and M. Lalín, *Statistics for traces of cyclic trigonal curves over finite fields*, IMRN (2010), no. 5, 932–967: non-real cubic components and complex trace statistics; the general cyclic-cover moduli space has ramification multiplicity components, whereas this note fixes the squarefree component. [Preprint](https://arxiv.org/abs/0907.5434).
- M. Rosen, *Number Theory in Function Fields*, GTM **210**, Springer (2002): reciprocity, characters and squarefree generating series. [Publisher](https://link.springer.com/book/10.1007/978-1-4757-6046-0).
- Eneström–Kakeya's classical coefficient theorem; K. Chinen, *An abundance of invariant polynomials satisfying the Riemann hypothesis*, especially the self-reciprocal analogue in §5. The elementary argument used here is stated and proved in §2. [Chinen preprint](https://arxiv.org/abs/0704.3903).
- O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Comm. Math. Phys. **25** (1972), 190–232, for matching-polynomial root location. [DOI](https://doi.org/10.1007/BF01877590). C. D. Godsil and I. Gutman, *On the matching polynomial of a graph*, in *Algebraic Methods in Graph Theory* (1981), 241–249, for the signing-average identity; title and pagination are listed in [Gutman's bibliography](https://www.pmf.kg.ac.rs/gutman/p001-250.pdf). The determinant argument is already in `notes/adelic-gkp/zn-flux.md` §4.

## Numerical checks for the blind lane

All files live in this lane. From the repository root run:

```bash
python3 notes/astra-2026-10-23/average/checks/avg_hyperelliptic.py
python3 notes/astra-2026-10-23/average/checks/avg_cubic.py
python3 notes/astra-2026-10-23/average/checks/avg_level.py
python3 notes/astra-2026-10-23/average/checks/avg_extended.py
python3 notes/astra-2026-10-23/average/checks/audit_identities.py
python3 notes/astra-2026-10-23/average/checks/summarize_outputs.py
```

The scripts write `checks/output_hyperelliptic.txt`, `output_cubic.txt`, `output_level.txt`, `output_extended.txt`, `output_audit.txt`, and `output_summary.txt` respectively. The prescribed three scripts cover every requested parameter. The extended script is the slower optional certificate run. Dependencies are Python, NumPy, SymPy, mpmath and python-flint; the computations use prime \(q\), while the all-\(q\) proofs explicitly allow odd prime powers. No number-field zeros or individual Weil-RH assertions enter these computations.

Five blind checks, all printed by the scripts:

1. \(\boxed{\overline L_{3,1}(u)=1+3u^2}\). Exact maximum \(\max_j\bigl||u_j|\sqrt3-1\bigr|=0\); NumPy deviation \(3.331\times10^{-16}\).
2. \(\boxed{\overline L_{5,2}(u)=1+\frac{524}{125}u^2+25u^4}\). Roots \(u=\pm0.240997925302\pm0.376722709695i\), independently signed. Exact maximum radial deviation is 0; NumPy deviation \(6.661\times10^{-16}\).
3. Over **all nine requested odd-degree averages**, NumPy's maximum radial deviation is \(1.776\times10^{-15}\); 80-digit refinement gives at most \(1.055\times10^{-81}\). Their circle property is proved above, rather than inferred from those small errors. The largest reported componentwise relative root condition number is 1; the maximum NumPy-to-refined displacement is \(1.913\times10^{-15}\).
4. Cubic \((q,d)=(7,3)\): completed average \(1+u\), root \(-1\), normalized radius \(\sqrt7=2.645751311065\). At degree 4 the normalized radius is \(7^{1/6}=1.383087554268\), so the obstruction also occurs with no infinity factor to remove.
5. Level \((q,d)=(3,2)\): raw sum \(7-3u\), root \(7/3\), normalized radius \(4.041451884327\). Removing all even-character trivial factors gives the constant sum 7 at this degree; the completed failure first appears at degree 3, as (11) records.

For a normalized polynomial \(p(z)=\sum a_kz^k\), the printed condition diagnostic is \(\kappa(z)=\sum_k|a_kz^k|/|zp'(z)|\). Root residuals are computed at 80 digits; a repeated or merged root causes the script to stop instead of silently reporting a small radial error. These are numerical diagnostics, not interval enclosures. The H-half inequalities and rational Sturm tests supply the exact certificates. The full direct-sum audit agrees, and the saved-output audit checks every reported residual and condition diagnostic.

## What this changes in the notebook

Nothing outside this lane was edited; nothing was registered. Suggested rows for review:

| candidate | proposed status | precise statement |
|---|---|---|
| `prop:sf-quadratic-average-exact` | PROVED | Equations (1)–(5), including the finite square density and nonsquare remainder. |
| `lem:reciprocal-half-stability` | PROVED | H-half plus reciprocal symmetry forces all roots onto the unit circle. |
| `thm:hyperelliptic-average-low-genus` | PROVED | A1 for every odd prime power and genera 1–3; completed even-degree counterpart for genera 1–2. |
| `obs:hyperelliptic-average-certificates` | PROVED by exact computation | Odd-degree ranges \((3,1\!:\!12),(5,1\!:\!8),(7,1\!:\!6)\); even-degree ranges in the table above. |
| `conj:hyperelliptic-average-all-genus` | OPEN | A1 universally; the stronger decreasing-first-half coefficient conjecture would suffice. |
| `obs:geometric-level-average-dichotomy` | REFUTED | Cubic geometric isotypic average \(1+u\) versus quadratic singleton level successes; no geometric/level iff. |
| `prop:ff-irreducible-level-average` | PROVED | Raw and completed sums (10)–(11), and exact-order Ramanujan-sum formula (12). |
| `obs:common-vacuum-average-det` | PROVED negative finding | A common invariant vacuum does not force an averaged determinant to satisfy RH. |

Recommended annotation to `graph-super.md` §9, **Averaging for zeta**:

> The graph's full character average has a special multiaffine determinant cancellation. Over \(\mathbb F_q(t)\), exact hyperelliptic averages satisfy RH in proved ranges and under an explicit half-coefficient condition, but cubic geometric isotypic averages and fixed-level averages can fail; a family of characters or covers alone does not supply an averaged RH theorem.

The failed geometric/level dichotomy belongs in `data-ladder.md` **§2 as a negative finding**. The low-genus theorem and H-half certificate can be cross-linked from §4 as finite positive examples; they do not supply a new positive datum for \(\zeta\). `ff-dirichlet.md` should keep its raw/completed distinction explicit; `zn-flux.md` should emphasize the full character subgroup, including its trivial element; `family-vacuum.md` needs no theorem change, only a warning against the determinant-average inference.

Next mathematical step: prove or refute the exact first-half coefficient inequality uniformly in \((q,g)\), retaining the nonsquare remainder. Independently, investigate the different conjecture for averages of **whole** cyclic-cover numerators, with ramification multiplicities, infinity behavior, and weighting fixed. Neither open problem is settled by the finite certifications recorded here.
