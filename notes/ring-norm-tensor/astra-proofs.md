# Ring norms, Frobenius, and graded tensors

Author: codex:gpt-6-astra

Date: 2026-09-14. All proofs, corrections, computations, and proposed constructions in this file have the author above. The supplied numerical files are prior evidence, not exact certificates. No web sources were consulted. Computations reported below were run by `python3` under `timeout`, with bytecode writing disabled and without creating scratch files.

The main conclusions are these. The ordinary elliptic construction is exact and has an elementary finite physical tensor. The bosonic genus bound without cancellation is true, but its drafted Hilbert--Schmidt proof is false. A rational contraction certificate proves an exact two-even, one-odd tensor for the supplied ordinary simple genus-two curve over $\mathbb F_5$. There is also an explicit nine-species formula for every prime power $q\ge16$, including that curve after base change to $\mathbb F_{25}$. A natural three-species formula for arbitrary ordinary genus-two data, and universal existence over the remaining smaller fields, remain open. The certificate, rather than numerical convergence alone, proves the particular $\mathbb F_5$ existence theorem.

Throughout, $\mathcal E$ denotes a doubled transfer matrix when confusion with an elliptic curve $E$ is possible. Tensor products in $\mathcal E=\sum_s A_s\otimes\overline{A_s}$ are ordinary Kronecker products. The statistics are those of H-TWIST; no additional minus sign is inserted into this formula. Spectra include algebraic multiplicity. A zero primary subspace may have nontrivial nilpotent Jordan blocks.

## T0. The quadratic family, its scope, and the amplitude obstruction

### Hypothesis register

The requested hypotheses are recorded below. For the lengthy named arithmetic inputs, the wording of the brief is retained; qualifications following them specify how they are used. An external theorem remains an input even when it is standard. “Conditional-on” records such inputs; “proved-here” is reserved for algebraic, analytic, or combinatorial implications proved in this file.

**H-WEIL (RH for curves and abelian varieties over $\mathbb F_q$).** For a smooth projective geometrically connected curve $C/\mathbb F_q$ of genus $g$,
$$
N_n=1+q^n-\sum_{j=1}^{2g}\alpha_j^n,\qquad |\alpha_j|=\sqrt q
$$
in every complex embedding; the $\alpha_j$ are the Frobenius eigenvalues on $H^1$, with multiplicity. For an abelian variety the Frobenius eigenvalues on $H^1$ likewise have absolute value $\sqrt q$ in every complex embedding.

**H-HASSE.** “for elliptic curves: #E(F_q) = q + 1 - a, |a| <= 2 sqrt(q), the Frobenius pi satisfying pi^2 - a pi + q = 0”. Here $a\in\mathbb Z$. The ordinary-case bound is derived below from lifting and degree, without using the inequality in H-HASSE.

**H-DEURING.** “Deuring lifting: for an ordinary elliptic curve E/F_q with Frobenius pi and End(E) = O an order in the imaginary quadratic field K = Q(pi), there is an elliptic curve E~ over a number field, with good reduction to E at a prime above p, whose endomorphism ring is O and whose reduction map End(E~) -> End(E) is an isomorphism taking an element pi~ to pi; over C, E~(C) = C/Lambda with Lambda a proper O-ideal, and pi~ is multiplication by the complex number pi”.

**H-DEG.** “the degree of the isogeny z -> pi z on C/Lambda is [Lambda : pi Lambda] = |pi|^2 = N_{K/Q}(pi), and degree is preserved under good reduction, so |pi|^2 = deg(Frobenius) = q”.

**H-LEF.** “Lefschetz fixed-point theorem for a self-map f of a compact manifold whose fixed points are nondegenerate: sum_{x = f(x)} sign det(1 - df_x) = sum_i (-1)^i Tr(f^* | H^i)”. We use smooth self-maps of compact oriented real manifolds with finitely many fixed points; cohomology has complex coefficients.

**H-LENSTRA.** “Lenstra 1996, "Complex multiplication structure of elliptic curves": for E ordinary over F_q with End(E) = O, E(F_{q^n}) is isomorphic as an O-module to O/(pi^n - 1)”. No canonical choice of these isomorphisms, compatible for all $n$, is part of this input.

**H-LM.** “Latimer--MacDuffee: for a monic f in Z[x] irreducible of degree d, the GL_d(Z)-conjugacy classes of integer matrices with characteristic polynomial f are in bijection with the ideal classes of fractional ideals of Z[x]/(f), an ideal I mapping to the matrix of multiplication by x on a Z-basis of I”. Here “ideal classes” must mean **all full ideal lattices modulo multiplication by $K^\times$**, not only invertible ideals or the Picard group of the displayed order. This distinction is essential for nonmaximal orders.

**H-WAT.** “Waterhouse 1969: the isomorphism classes of elliptic curves over F_q in the ordinary isogeny class with Frobenius pi are in bijection with the ideal classes of the orders O with Z[pi] <= O <= O_K, the curve with End = O corresponding to the ideal classes of O”. We use the ordinary classification over the specified finite field: for a fixed endomorphism order, the relevant classes form a torsor for $\operatorname{Pic}(O)$, and a labeling requires a base choice. An unmarked complex tensor is not this integral classification.

**H-CM.** “for a simple ordinary abelian variety A/F_q of dimension g with Frobenius pi, K = Q(pi) is a CM field of degree 2g, End(A) (x) Q = K, and the canonical (Serre--Tate) lift A~ to characteristic 0 has H^1(A~(C), C) = (+)_{phi: K -> C} C_phi with H^{1,0} = (+)_{phi in Phi} C_phi for a CM type Phi (one embedding from each complex-conjugate pair), pi~ acting on C_phi by phi(pi)”. A complex realization of the lift is chosen. Endomorphisms here are over $\mathbb F_q$; additional geometric endomorphisms after field extension are not excluded by this statement.

**H-ROSATI.** “the Rosati involution of a polarised abelian variety is positive: Tr(x x^dagger) > 0 for x != 0 in End(A) (x) R, and the Frobenius satisfies pi pi^dagger = q”. In the commutative simple ordinary case $\operatorname{Tr}$ is the regular field trace, extended to $K\otimes\mathbb R$; positive scalar normalizations make no difference. Polarization of this quadratic form gives $\langle x,y\rangle_R=\operatorname{Tr}(x y^\dagger)$, a real inner product.

**H-LIDSKII (Lidskii's theorem).** A trace-class operator $S$ on a separable complex Hilbert space is compact, its nonzero eigenvalues have finite algebraic multiplicity, their absolute values have finite sum, and $\operatorname{Tr}S$ equals their sum with algebraic multiplicity. This applies to every positive integer power of a trace-class bounded operator.

**H-SCHUR.** “sum_i |mu_i|^2 <= ||M||_HS^2 for the eigenvalues of a finite matrix, with equality iff M is normal”. Here $\|M\|_{\rm HS}^2=\operatorname{Tr}(M^*M)$. A proof is given in T3.1.

**H-CS (Cauchy--Schwarz).** In a complex Hilbert space, $|\langle x,y\rangle|^2\le\langle x,x\rangle\langle y,y\rangle$, with equality exactly when $x,y$ are linearly dependent, including the zero cases. The convention is conjugate-linearity in the first argument.

**H-TWIST (the specified ring-norm theorem).** For a finite graded bond with $P^2=1$ and homogeneous tensors $PA_sP=\eta_s A_s$, put $\Gamma=P\otimes\bar P$ and $\mathcal E=\sum_s A_s\otimes\bar A_s$. The physical periodic fermion ring closed with $P$ has
$$
\|\Psi_P(n)\|^2=\operatorname{str}_{\Gamma}\mathcal E^n
=\sum_{s_1,\ldots,s_n}|\operatorname{Tr}(PA_{s_1}\cdots A_{s_n})|^2.
$$
For the continuum data $PQP=Q$, $PR_aP=\eta_aR_a$, the corresponding assertion is $\|\Psi_P(L)\|^2=\operatorname{str}_\Gamma e^{LT}$. The finite-bond assertion is the input from shards 02f and 04f; this is not an infinite-bond existence theorem.

The following additional inputs are used, with their exact scope.

**H-FROB (cohomological point-count formula, without RH).** Curve counts have the formula in H-WEIL with nonzero algebraic Frobenius eigenvalues, without assuming their absolute values. For an elliptic curve these are the roots of $X^2-aX+q$, where $a=q+1-\#E(\mathbb F_q)$, and the Frobenius endomorphism satisfies this polynomial. This is the non-RH part of H-WEIL/H-HASSE, separated to make the degree argument noncircular.

**H-AS-WEIL (the exact implementer statement of shard 06b).** For its stated scope, $q$ an odd prime, $J\ge1$, $a_J\ne0$, the normalized quadratic transfer $U_g=E_g/\sqrt q$ factors into a normalized one-register Fourier transform, diagonal additive-character quadratic phases, and a register permutation. It implements the centered Weyl action of the displayed $M_g\in\operatorname{Sp}(2J,\mathbb F_q)$ and equals $c_g W(M_g)$ for a genuine finite-dimensional unitary representation $W$, with $|c_g|=1$.

For explicitness, the symplectic map supplied by that shard is, for $k<J$,
$$u'_k=u_{k+1},\quad u'_J=-v_1/a_J,\quad
v'_k=v_{k+1}+a_{J-k}u'_J,\quad
v'_J=a_Ju_1+\sum_{k=2}^J a_{J+1-k}u_k+2a_0u'_J.$$

**H-AS-SUPER.** The odd block $F$ of shard 06b's super-transfer matrix has as multiset exactly the Frobenius eigenvalues on $H^1$ of the smooth projective curve. Its count is $1+q^n-\operatorname{Tr}F^n$.

**H-AS-FILTER (the corrected roots-of-unity filter in shard 06b).** For each nontrivial additive character there is an integer $h\ge1$ such that
$$
m_F(z)=\frac1h\sum_{\omega^{2h}=1}m_{E_g}(\omega^{-1}z)-m_{E_g}(z)
$$
is a nonnegative integral multiplicity; the full odd block is the sum of these character blocks. In particular its support is contained in root-of-unity multiples of the transfer spectra. H-AS-SUPER alone would not imply this support assertion.

**H-SS-NP (the standard supersingularity criterion).** An abelian variety over a finite field has all Newton slopes $1/2$ if and only if all its complex Frobenius eigenvalues are $\sqrt q$ times roots of unity. A curve is called supersingular when its Jacobian has this property. This equivalence is cited, not proved here.

**H-AB-COH (cohomology and counts of abelian varieties).** $H^*(A)=\Lambda^*H^1(A)$, Frobenius acts by the induced exterior powers, and $\#A(\mathbb F_{q^n})=\det(1-F^n\mid H^1(A))$. The relevant statements can be made in $\ell$-adic cohomology and transported to a complex characteristic-zero realization.

**H-CM-POL (polarized lift and Hodge metric).** A polarization lifts along the canonical ordinary lift, and the lifted endomorphisms and polarization identify Rosati adjunction with adjunction for the positive Hodge Hermitian form on $H^{1,0}$ (and its conjugate on $H^{0,1}$). For an Abel--Jacobi embedding $i:C\hookrightarrow J(C)$, $i^*:H^1(J)\to H^1(C)$ is an isomorphism, $[C]$ is the principal polarization class in dimension two, and $\int_C i^*\xi=\int_J\xi\smile[C]$. These are the polarization/comparison inputs used in T4.

For the normalization in T4.6 we also include the principal-polarization intersection formula $\int_J\theta^2=2$ on an abelian surface, with $\theta=c_1$ of the principal polarization.

**H-AV-FUNCTOR (Frobenius functoriality and Newton slopes).** For an exact sequence of abelian varieties over a finite field, their rational $\ell$-adic $H^1$ representations give the corresponding product identity for Frobenius characteristic polynomials. In particular a proper positive-dimensional abelian subvariety gives a proper factor over $\mathbb Q$. Newton slopes are the $p$-adic valuations of the Frobenius eigenvalues divided by $v_p(q)$; an ordinary abelian variety of dimension $g$ has $g$ slopes zero and $g$ slopes one. Under finite base extension the eigenvalues are raised to the extension degree, so these normalized slopes are unchanged. This standard functoriality input is used only to discuss simplicity and preserved ordinarity in T4.4, and to distinguish ordinary from supersingular in T1.6.

**H-RCF (real closed field transfer).** A finite system of polynomial equalities and inequalities over the real algebraic numbers which has a solution in $\mathbb R$ has a solution in the field of real algebraic numbers. This is the existential consequence of quantifier elimination for real closed fields.

**H-ZERO (zero count and location).** The nontrivial Riemann zeros, with multiplicity, are locally finite, satisfy $0<\Re\rho<1$, are invariant under conjugation and $\rho\mapsto1-\rho$, and their positive-height counting function is $\frac{T}{2\pi}\log\frac{T}{2\pi e}+O(\log T)$. No RH is included.

**H-KRAUS-HS (analytic setting for T3.6).** $H_+,H_-$ are separable Hilbert spaces. At each fixed $t>0$ there is a normal completely positive map on $B(H_+\oplus H_-)$ with a countable bounded Kraus family $K_s=a_s\oplus B_s$ and weakly convergent Kraus expansion. Its induced blocks on Hilbert--Schmidt operators extend to bounded operators $S_+(t),S_-(t),M(t)$; the first two are trace class. Compression to finite bond subspaces agrees with compression of this Kraus expansion. The odd semigroup has the stipulated zero modes as eigenvectors with their multiplicities. This regularity is an explicit hypothesis, not a consequence proved here for an unbounded cMPS generator.

### Theorem T0.1 (finite order in the shard's scope)

**Hypotheses:** H-AS-WEIL, H-AS-FILTER, H-AS-SUPER; $q$ odd prime, $J\ge1$, $a_J\ne0$.

**Statement.** $U_g=E_g/\sqrt q$ has finite order. Its eigenvalues are roots of unity. Every Frobenius eigenvalue of the corresponding quadratic Artin--Schreier curve is $\sqrt q$ times a root of unity; hence the curve is supersingular in the spectral definition, and also in the Newton-polygon definition under H-SS-NP.

**PROOF.**

<1>1. The determinant of each factor of $U_g$ is a root of unity.

<2>1. A normalized finite Fourier matrix $F_a=(q^{-1/2}\psi(a xy))_{x,y\in\mathbb F_q}$ satisfies $F_a^2 f(x)=f(-x)$ by character orthogonality. Thus $F_a^4=1$, and $\det F_a$ is a fourth root of unity. Tensoring with identities preserves the root-of-unity property of the determinant.

<2>2. Each diagonal phase is a root of unity because an additive character of a finite field has finite image. A register permutation has determinant $\pm1$. Multiplicativity of determinants proves the claim.

<1>2. Set $d=q^J$. Since $\operatorname{Sp}(2J,\mathbb F_q)$ is finite, $W(M_g)^h=1$ for some $h\ge1$, and $\det W(M_g)$ is a root of unity. Consequently
$$c_g^d=\det U_g/\det W(M_g)$$
is a root of unity, so $c_g$ itself is a root of unity. Hence a common multiple of its order and $h$ is an order of $U_g$.

<1>3. Every eigenvalue of $E_g$ is $\sqrt q$ times a root of unity. Apply the same argument to all nontrivial character twists. H-AS-FILTER shows that every eigenvalue retained in $F$ is another root-of-unity multiple of one of these eigenvalues. H-AS-SUPER identifies that multiset with the Frobenius multiset. H-SS-NP supplies the final equivalence. $\square$

**Correction.** The proof of the scalar phase is not “the entries are roots of unity, therefore the phase is.” The matrix has zero entries as well, and normalization introduces $q^{-1/2}$. The exact Fourier--phase--permutation factorization proves the needed determinant statement. Also, 06b explicitly assumes an odd prime; its genuine centered symplectic representation cannot silently be imported into characteristic two. For $J=0$ in odd characteristic, the effective scalar transfer is a quadratic Gauss sum, not a $1\times1$ root-of-unity entry; its normalized value is a fourth root of unity by the usual one-variable Gauss calculation.

**Status:** conditional-on H-AS-WEIL, H-AS-FILTER, H-AS-SUPER; Newton interpretation additionally conditional-on H-SS-NP.

### Proposition T0.2 (supersingularity over general finite fields, without a characteristic-two implementer claim)

**Hypotheses:** H-FROB; $q=p^r$, $J\ge1$, $a_J\ne0$, $g(X)=\sum_{j=0}^J a_jX^{1+q^j}$. Take the smooth projective geometrically connected model of $y^q-y=g(x)$.

**Statement.** This curve is spectrally supersingular for arbitrary $p$. The nonzero $J=0$ case is also supersingular in odd characteristic, and has genus zero in characteristic two. This assertion does not assert that a genuine representation of $\operatorname{Sp}(2J,\mathbb F_q)$ gives the normalized transfer in characteristic two.

**PROOF.**

<1>1. For $b\in\mathbb F_q^\times$, put
$$Q_{b,n}(x)=\operatorname{Tr}_{\mathbb F_{q^n}/\mathbb F_p}(b g(x)),\qquad
S_{b,n}=\sum_x e^{2\pi i Q_{b,n}(x)/p}.$$
This is a quadratic polynomial function on the $rn$-dimensional $\mathbb F_p$-space. In characteristic two, “quadratic” allows a linear part.

<1>2. Its polar radical has $\mathbb F_p$-dimension at most $2rJ$. Indeed nondegeneracy of the absolute trace pairing identifies that radical with the kernel on $\mathbb F_{q^n}$ of the $q$-linear expression
$$2ba_0x+\sum_{j=1}^J ba_j(x^{q^j}+x^{q^{-j}}).$$
Here negative exponents denote inverse Frobenius automorphisms. Raising this expression to the $q^J$ power gives the fixed nonzero polynomial
$$R_b(X)=2ba_0X^{q^J}+\sum_{j=1}^J ba_j(X^{q^{J+j}}+X^{q^{J-j}}),$$
of degree $q^{2J}$. Thus its root space has at most $q^{2J}$ elements. The same reasoning covers $p=2$, where the displayed $2ba_0$ term vanishes.

<1>3. A quadratic Gauss sum on an $m$-dimensional $\mathbb F_p$-space with radical dimension $d$ is zero if the character is nontrivial on the radical; otherwise its modulus is $p^{(m+d)/2}$. For odd $p$, diagonalize the nondegenerate form. The one-dimensional sum $G=\sum_x\exp(2\pi i x^2/p)$ satisfies $|G|^2=p$ by character orthogonality and $\bar G=\eta(-1)G$ by writing $G=\sum_t\eta(t)\exp(2\pi i t/p)$ and replacing $t$ by $-t$. Hence $G^2=\eta(-1)p$, and its normalized phase is in $\{1,-1,i,-i\}$. Rescaling a square coefficient multiplies $G$ by the corresponding quadratic character. For $p=2$ the sum is real and its nonzero normalized phase is $\pm1$. The modulus assertion also follows directly by expanding $|S|^2$, setting one summation variable equal to the other plus $h$, and using character orthogonality; only radical $h$ survive. In characteristic two the residual nondegenerate alternating form splits into two-dimensional symplectic planes, giving the stated sign and modulus.

<1>4. Consequently $S_{b,n}/q^{n/2}$ belongs to a finite set independent of $n$: the possible values are zero or $p^{d/2}$ times one of these phases, with $0\le d\le2rJ$. The polynomial degree $q^J+1$ is prime to $p$, so the projective model has one point at infinity. Character orthogonality in $y^q-y=g(x)$ gives
$$\sum_j(\alpha_j/\sqrt q)^n=-\sum_{b\ne0}S_{b,n}/q^{n/2}.$$
Thus the normalized Frobenius power sums take values in a finite set.

<1>5. If the Frobenius multiset is empty there is nothing to prove. Otherwise a sequence of power sums of finitely many nonzero complex numbers satisfies a fixed linear recurrence. Its consecutive state vectors, of length equal to that recurrence order, lie in a finite set. Deterministic evolution therefore makes the sequence eventually periodic. If its period is $h$ and its distinct bases are $\beta_1,\ldots,\beta_d$ with multiplicities $m_i>0$, then for every sufficiently large $n$,
$$\sum_i m_i(\beta_i^h-1)\beta_i^n=0.$$
An invertible Vandermonde matrix, using $d$ consecutive $n$, gives $\beta_i^h=1$ for every $i$. Set $\beta_i=\alpha_i/\sqrt q$. No RH modulus premise was used.

<1>6. If $J=0$ and $a_0\ne0$ in odd characteristic, the trace-pairing radical is zero for every character twist, so steps 3--5 apply with $d=0$. In characteristic two, choose $b\in\mathbb F_q$ with $b^2=a_0$ and set $t=bx+y^{q/2}$. The equation implies $t^2=y$ and $bx=t+t^q$. Its function field is therefore $\mathbb F_q(t)$ and its smooth projective model is $\mathbb P^1$, of genus zero. The identically zero polynomial is excluded from a geometrically connected nontrivial-cover discussion. $\square$

**Status:** conditional-on H-FROB; the Gauss-sum and recurrence arguments are proved-here. The Newton-polygon interpretation additionally uses H-SS-NP.

### Proposition T0.3 (the correct cut-rank bound)

**Hypotheses:** Finite matrices $A_s\in M_D(\mathbb C)$ and the periodic amplitude $f(s_1,\ldots,s_n)=\operatorname{Tr}(A_{s_1}\cdots A_{s_n})$.

**Statement.** Across a bipartition into two contiguous nonempty arcs the complex flattening rank is at most $D^2$, not $D$. Across an arbitrary bipartition it is at most $D^b$, where $b$ is the number of virtual edges crossing the bipartition. The $D$ bound applies to an open chain cut across a single virtual edge.

**PROOF.**

<1>1. For two arcs write their matrix products as $X(u)$ and $Y(v)$. Then
$$f(u,v)=\sum_{i,j=1}^D X(u)_{ij}Y(v)_{ji},$$
a sum of at most $D^2$ separated functions.

<1>2. The bound cannot be replaced by $D$: take the alphabet of all matrix units $e_{ij}$ and $n=2$. The flattening $\operatorname{Tr}(e_{ij}e_{kl})=\delta_{jk}\delta_{il}$ has rank $D^2$.

Even unit-modulus amplitudes do not repair the general ring bound. With $D=2$, take $A_0=|0\rangle(\langle0|+\langle1|)$ and $A_1=|1\rangle(\langle0|-\langle1|)$. Every ring word has amplitude $(-1)^{\sum_i s_i s_{i+1}}$. At $n=4$, the $2|2$ cut has rank four: after removing signs internal to each arc, its bilinear cross form is $s_2s_3+s_1s_4$, of binary rank two. This is a general tensor counterexample, not an assertion that this tensor gives the specified normal-basis field amplitudes for all $n$.

<1>3. For a general bipartition expose the $b$ cut virtual indices. Each assignment contributes a separated function, and there are $D^b$ assignments. $\square$

**Status:** proved-here.

### Proposition T0.4 (the requested binary experiment)

**Hypotheses:** $q=2$, $g(x)=x^3$, additive character $(-1)^t$, and the normal bases specified below. Coordinates are ordered $(\beta,\beta^2,\ldots,\beta^{2^{n-1}})$.

**Statement.** The complex ranks across cuts after positions $1,\ldots,n-1$ are:

| $n$ | irreducible polynomial, increasing-power convention understood | $\beta$ | cut ranks |
|---:|---|---|---|
| 1 | $X$ | $1$ | no nontrivial cut |
| 2 | $X^2+X+1$ | $X$ | $1$ |
| 3 | $X^3+X^2+1$ | $X^2$ | $2,2$ |
| 4 | $X^4+X^3+1$ | $X^3$ | $2,4,2$ |
| 5 | $X^5+X^3+1$ | $1+X^4$ | $2,2,2,2$ |
| 6 | $X^6+X^5+1$ | $X^5$ | $2,4,4,4,2$ |
| 7 | $X^7+X^6+1$ | $X^6$ | $2,4,8,8,4,2$ |
| 8 | $X^8+X^7+X^5+X^4+1$ | $X^7$ | $2,4,8,16,8,4,2$ |

**PROOF / reproducible computation.**

<1>1. Enumerate irreducible moduli and field elements in the order used by `scripts/artin_schreier_mps.py`; choose the first $\beta$ whose conjugate-coordinate matrix has binary rank $n$. These choices give the displayed moduli and generators.

<1>2. $Q(x)=\operatorname{Tr}(x^3)$ is a **quadratic** binary form: $x^3=x^{1+2}$. Across a cut, write $Q(u,v)=Q_U(u)+Q_V(v)+u^TBv$. Multiplying rows and columns by signs reduces the amplitude matrix to $((-1)^{u^TBv})_{u,v}$. Its distinct rows are orthogonal characters and their number is $2^{\operatorname{rank}_{\mathbb F_2}B}$. Its exact complex rank is therefore that number.

<1>3. Direct binary elimination on $B$ gave, respectively,
$$(),\ (0),\ (1,1),\ (1,2,1),\ (1,1,1,1),\ (1,2,2,2,1),\ (1,2,3,3,2,1),\ (1,2,3,4,3,2,1).$$
Exhaustive construction of the sign flattenings and their numerical ranks agreed. The decisive computation is binary elimination, not a tolerance choice in a singular-value test. The following kernel specifies the calculation exactly:

```python
# Author: codex:gpt-6-astra
# Run with PYTHONDONTWRITEBYTECODE=1 timeout 35s python3, from the repo root.
import sys, itertools
sys.path.insert(0, 'scripts')
from artin_schreier_mps import irreducible, polypow, trace

def rank2(rows):
    a = [list(r) for r in rows]
    r = 0
    for j in range(len(a[0]) if a else 0):
        p = next((i for i in range(r, len(a)) if a[i][j]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        for i in range(len(a)):
            if i != r and a[i][j]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
    return r

for n in range(1, 9):
    f = irreducible(2, n)
    for beta in itertools.product(range(2), repeat=n):
        basis = [polypow(list(beta), 2**j, f, 2) for j in range(n)]
        if rank2(list(zip(*basis))) == n:
            break
    def Q(bits):
        x = [sum(bits[j]*basis[j][i] for j in range(n)) % 2
             for i in range(n)]
        return trace(polypow(x, 3, f, 2), f, 2, n)
    e = [[int(i == j) for i in range(n)] for j in range(n)]
    ranks = []
    for k in range(1, n):
        B = [[Q([x ^ y for x, y in zip(e[i], e[j])]) ^ Q(e[i]) ^ Q(e[j])
              for j in range(k, n)] for i in range(k)]
        ranks.append(2**rank2(B))
    print(n, f, beta, ranks)
```

<1>4. These eight cases have maximum rank $16$; they do **not** prove an asymptotic bound or unboundedness. The chosen normal bases vary with $n$, and a change of normal basis can be nonlocal with respect to a cut. The calculation is not evidence that a nonquadratic trace polynomial requires growing bond dimension, since this example is quadratic. $\square$

**Status:** proved-here for the finite computation and its rank interpretation; asymptotic boundedness for this basis prescription is open here.

**Conjecture T0.C (restricted amplitude locality).** After specifying a normal-basis prescription for every $n$ and quotienting the polynomial data by trace-invisible Artin--Schreier coboundaries, a fixed finite tensor with the particular amplitudes $\psi(\operatorname{Tr}g(x))$ for every $n$ can exist only if those trace functions have quadratic degree (allowing lower degree) over the prime field. **Status: open.** This is a necessity conjecture, not a theorem or a sufficiency assertion. The basis prescription matters, “quadratic” means degree of a function rather than ordinary polynomial degree, and supersingularity is a consequence for the quadratic family, not an equivalent definition of belonging to that family. In particular this conjecture says nothing against the finite ordinary-elliptic **norm** tensor constructed next. A coboundary $h^q-h$ can give a nonquadratic polynomial with the very same amplitudes as a quadratic one.

## T1. Tier A: ordinary elliptic curves

### Theorem T1.1 (Frobenius on the lifted torus and the ring norm of an ideal)

**Hypotheses:** H-DEURING, H-DEG, H-FROB, H-LEF; $E/\mathbb F_q$ ordinary. The quotient-module identification additionally assumes H-LENSTRA.

**Statement.** Let $M$ be the integral matrix of multiplication by $\pi$ on a $\mathbb Z$-basis of $\Lambda$. Then $\chi_M(X)=X^2-aX+q$, and for every $n\ge1$,
$$
\#\operatorname{Fix}(M^n:\mathbb T^2\to\mathbb T^2)
=\det(1-M^n)=|1-\pi^n|^2
=N_{K/\mathbb Q}(1-\pi^n)=N_n.
$$
Every fixed point is nondegenerate and has index $+1$. Also
$$N_n=|O/(\pi^n-1)O|,$$
and under H-LENSTRA this quotient is the actual point group as an $O$-module. “Ideal norm” here means the index of the principal ideal in the possibly nonmaximal order.

**PROOF.**

<1>1. Multiplication by $\pi$ preserves $\Lambda$, so $M$ is integral. The real-linear map on $\mathbb C$ has eigenvalues $\pi,\bar\pi$. Its determinant is $|\pi|^2=q$ by H-DEG, and its trace is $a$ by H-FROB and the lifted endomorphism relation. Thus it has the displayed characteristic polynomial.

<1>2. $|\pi|=\sqrt q>1$, so neither eigenvalue of $M^n$ is $1$. The fixed-point group is
$$ (M^n-1)^{-1}\mathbb Z^2/\mathbb Z^2
\simeq\mathbb Z^2/(M^n-1)\mathbb Z^2.$$
Smith normal form, or the ratio of covolumes, gives its cardinality $|\det(M^n-1)|$.

<1>3. The derivative is the same matrix $M^n$ at every fixed point and
$$\det(1-M^n)=(1-\pi^n)(1-\bar\pi^n)>0.$$
Every point is therefore nondegenerate with index $+1$.

<1>4. The cohomological actions in degrees $0,1,2$ are $1,M^T,q$, respectively. H-LEF gives
$$\#\operatorname{Fix}(M^n)=1-\operatorname{Tr}(M^n)+q^n
=1-\pi^n-\bar\pi^n+q^n=N_n.$$
The last equality uses H-FROB without its RH strengthening.

<1>5. The product in step 3 is the field norm. Multiplication by $1-\pi^n$ on the rank-two lattice $O$ has this determinant and nonzero finite index. Thus its index is $N_n$ even without H-LENSTRA. H-LENSTRA upgrades equality of cardinalities to an $O$-module identification with $E(\mathbb F_{q^n})$. $\square$

**Status:** conditional-on H-DEURING, H-DEG, H-FROB, H-LEF; point-module interpretation additionally conditional-on H-LENSTRA.

### Theorem T1.2 (dynamical and Hasse--Weil zeta)

**Hypotheses:** T1.1 and the Frobenius action on $E(\overline{\mathbb F}_q)$.

**Statement.** As formal power series, and analytically for $|u|<q^{-1}$,
$$
\exp\left(\sum_{n\ge1}\#\operatorname{Fix}(M^n)\frac{u^n}{n}\right)
=\frac{1-au+qu^2}{(1-u)(1-qu)}=Z(E,u).
$$
There are equally many primitive toral periodic orbits of each length and closed points of each degree on $E$. This yields a length-preserving bijection after choices, not a canonical arithmetic correspondence supplied by the zeta identity.

**PROOF.**

<1>1. Insert T1.1 and use $\sum_{n\ge1}z^n/n=-\log(1-z)$ formally. Exponentiation gives
$$\frac{(1-\pi u)(1-\bar\pi u)}{(1-u)(1-qu)},$$
which is the displayed rational function.

<1>2. If $c_d$ denotes the number of primitive periodic orbits of length $d$, then $\#\operatorname{Fix}(M^n)=\sum_{d\mid n}d c_d$: a cycle of length $d$ contributes its $d$ points precisely when $d\mid n$. The same identity holds for Frobenius cycles, with fixed-point count $N_n$. Möbius inversion therefore gives equal $c_d$ for both systems.

<1>3. Expanding $\prod_d(1-u^d)^{-c_d}$ logarithmically gives the same fixed-point series. Thus the gas Euler product and cohomological transfer expression are both realized by this toral dynamical system. Equal finite orbit counts permit a bijection for each $d$, but do not select one. $\square$

**Status:** conditional-on the inputs of T1.1; the orbit-count and zeta implications are proved-here.

### Theorem T1.3 (Hodge doubling, the actual finite tensor, and its physical state)

**Hypotheses:** T1.1; H-TWIST for the physical interpretation. Choose a complex embedding of the lift and any finite unit vector $\phi=\sum_s a_s|s\rangle$, $\sum_s|a_s|^2=1$.

**Statement.** The natural ket bond is
$$V=\Lambda^*(H^{1,0})=\mathbb C\oplus\mathbb C\,dz=\mathbb C^{1|1},\qquad P=\operatorname{diag}(1,-1).$$
The tensors
$$A_s=a_s\begin{pmatrix}1&0\\0&\pi\end{pmatrix}$$
are all even, hence all physical species can be bosonic. Their doubled bond is the cohomology of the torus, with parity equal to total form degree. They satisfy
$$\Psi_P(n)=(1-\pi^n)\phi^{\otimes n},\qquad
\|\Psi_P(n)\|^2=N_n,$$
and the untwisted norm is $|1+\pi^n|^2$. A singleton alphabet, $a_0=1$, already suffices.

**PROOF.**

<1>1. On $\mathbb C/\Lambda$, the lifted map is $z\mapsto\pi z$, so $M^*dz=\pi dz$ and $M^*d\bar z=\bar\pi d\bar z$. Constant differential forms compute torus cohomology; the exterior algebra has dimensions $1,2,1$ in degrees $0,1,2$.

<1>2. The ordered exterior-product map
$$\Lambda^*(\mathbb C dz)\otimes\Lambda^*(\mathbb C d\bar z)
\longrightarrow\Lambda^*(\mathbb C dz\oplus\mathbb C d\bar z)$$
is an isomorphism of graded vector spaces, intertwining the even Frobenius actions. The usual Koszul convention is used if one compares algebra products. It does not change the ordinary Kronecker transfer convention.

<1>3. In the ordered doubled basis $(1\otimes1,1\otimes d\bar z,dz\otimes1,dz\otimes d\bar z)$, the transfer is
$$\mathcal E=\operatorname{diag}(1,\bar\pi,\pi,q),\qquad
\Gamma=\operatorname{diag}(1,-1,-1,1).$$
The $(+,+)$ line is $H^0$; the two mixed lines are $H^{0,1},H^{1,0}$; the $(-,-)$ line is $H^2$ and has eigenvalue $\pi\bar\pi=q$, the degree. Its supertrace is precisely the Lefschetz number.

<1>4. For every word, $\operatorname{Tr}(PA_{s_1}\cdots A_{s_n})=(1-\pi^n)\prod_i a_{s_i}$. Squaring and summing gives $|1-\pi^n|^2$ directly. With $P$ replaced by $1$, replace the minus by a plus. T1.1 identifies the former with $N_n$ and T1.2 gives its ring zeta. $\square$

The odd-degree **bond/cohomology modes** are fermionic in the grading. The physical letters of this tensor are even. These are different uses of “fermionic.” The physical vector has Schmidt rank one; its norm realizes the counts, but its basis configurations do not enumerate the points of the curve. Its dependence on the isogeny data is canonical up to the complex embedding, gauge, and the inessential choice of a unit physical vector.

**Status:** conditional-on the arithmetic inputs of T1.1; the tensor and norm identities are proved-here (and agree with H-TWIST).

### Theorem T1.4 (Fourier pullback is an injection, and its flat trace)

**Hypotheses:** T1.1; normalized Haar measure on $\mathbb T^2$. The “flat supertrace” below is defined by the specified Fourier diagonal, not by a trace-class assertion.

**Statement.** For $e_k(x)=e^{2\pi i k\cdot x}$ and a constant form $\omega$,
$$U(e_k\otimes\omega)=e_{M^Tk}\otimes\Lambda^*(M^T)\omega.$$
The map $k\mapsto M^Tk$ on $\mathbb Z^2$ is injective of index $q$, **not a permutation**. Its only finite orbit is $\{0\}$. The Fourier-diagonal flat supertrace is
$$\operatorname{str}^{\flat}U^n
:=\sum_{k:M^{nT}k=k}\operatorname{str}\Lambda^*(M^{nT})
=N_n.$$

**PROOF.**

<1>1. $e_k(Mx)=e_{M^Tk}(x)$. A column of covector coefficients pulls back by $M^T$, proving both transposes in the formula.

<1>2. $\det M=q$ makes $M^T$ injective on $\mathbb Z^2$ with cokernel of order $q>1$. Haar pullback on functions is an isometry, but is not surjective: its Fourier range has labels in $M^T\mathbb Z^2$.

<1>3. A finite orbit of an injection is periodic. If $M^{nT}k=k$, invertibility of $M^{nT}-1$ over $\mathbb R$, hence over $\mathbb Q$, gives $k=0$.

<1>4. The displayed flat trace has one term. The exterior-algebra identity $\operatorname{str}\Lambda^*B=\det(1-B)$ follows by triangularizing $B$ and multiplying $\prod_i(1-\lambda_i)$. Apply it to $M^{nT}$ and use T1.1. This is also the distributional Lefschetz trace: each fixed point contributes $\operatorname{str}\Lambda^*(M^{nT})/|\det(1-M^n)|=1$. It is not an ordinary Hilbert-space trace of $U^n$. $\square$

**Status:** conditional-on T1.1; the operator and flat-trace calculation are proved-here.

### Proposition T1.5 (what a Fourier physical-index tensor actually gives)

**Hypotheses:** T1.3--T1.4. Let $F=\operatorname{diag}(1,\pi)$ on the holomorphic ket bond.

**Statement.** One can make an honest, but redundant, infinite-label lattice tensor on $\ell^2(\mathbb Z^2)\otimes V$ by
$$\mathsf A_k=|M^Tk\rangle\langle k|\otimes F,\qquad k\in\mathbb Z^2.$$
Its parity-closed ring amplitudes vanish unless every physical label is $0$, and the surviving amplitude is $1-\pi^n$. Its ring vector is therefore $(1-\pi^n)|0,\ldots,0\rangle$ and has norm $N_n$.

**PROOF.**

<1>1. A product of the label matrix units has nonzero trace only when the labels form a cycle of the injection $k\mapsto M^Tk$ (with orientation reversed if the word is read right to left). By T1.4 this cycle is the constant zero cycle.

<1>2. The remaining ket trace is $\operatorname{Tr}(PF^n)=1-\pi^n$. Every word product has finite-rank label support, so this trace and the resulting one-supported ring vector are well defined without an infinite trace interchange. $\square$

The sum of the label matrix units is the unilateral Fourier shift. Tensored with the **full** exterior fibre it gives $U$, an operator kernel with input and output labels, not by itself a finite-bond physical MPS tensor. The ket-fibre formula above supplies the missing tensor distinction; doubling its fibre gives the full exterior fibre. Doubling the full cohomology fibre a second time would instead square the wrong quantity. This construction adds no pointwise arithmetic information to the singleton tensor in T1.3. It does not realize the exponential-sum amplitudes of T0.C.

**Status:** conditional-on T1.1; the explicit infinite-label ring-vector construction is proved-here.

### Theorem T1.6 (the PH unitary, degree positivity, and the ordinary Hasse bound)

**Hypotheses:** H-DEURING, H-DEG, H-FROB. Use the flat complex torus and its positive Hodge metric. No RH inequality in H-HASSE or H-WEIL is used. The final comparison with supersingularity uses H-SS-NP and H-AV-FUNCTOR.

**Statement.** The PH Hilbert space can be taken to be $H^1(\mathbb T^2,\mathbb C)$ with its Hodge Hermitian metric, and the PH unitary is
$$U_{\rm PH}=q^{-1/2}M^*\mid H^1.$$
It is unitary because the lifted Frobenius is a conformal similarity of ratio $\sqrt q$. Consequently the two nontrivial doubled-transfer eigenvalues in T1.3 have absolute value $\sqrt q$ (the Ramanujan property here), and $|a|\le2\sqrt q$; in the ordinary imaginary-quadratic case the inequality is strict.

**PROOF.**

<1>1. Harmonic $1$-forms are constant, and the Hodge splitting is orthogonal. On $H^{1,0}$ and $H^{0,1}$, pullback multiplies by $\pi$ and $\bar\pi$. Thus $\langle M^*\omega,M^*\eta\rangle=q\langle\omega,\eta\rangle$ by H-DEG. This proves unitarity after dividing by $\sqrt q$ and the eigenvalue assertion.

<1>2. The map on the universal cover is literally $z\mapsto\pi z$. Its Euclidean length ratio is $|\pi|$ and its oriented area ratio, hence its covering degree, is $|\pi|^2=q$. Positivity is supplied by the Euclidean/Hodge metric; it is not supplied by eigenvalue counting alone.

<1>3. On the order, degree is the positive definite norm form
$$\deg(m+n\pi)=|m+n\pi|^2=m^2+a mn+q n^2.$$
Since $1,\pi$ form a real basis of $\mathbb C$, this form is positive definite on $\mathbb R^2$. Its determinant is $q-a^2/4>0$. Hence $a^2<4q$; $N_1=q+1-a$ is H-FROB. This proves the ordinary portion of H-HASSE from the stated lift and degree inputs. The full Hasse theorem for supersingular curves is not proved by an ordinary-only lifting hypothesis.

<1>4. The real vector space $K\otimes_\mathbb Q\mathbb R\simeq\mathbb C$ with inner product $\Re(x\bar y)$ is an equivalent real model of $H^1(\mathbb T^2,\mathbb R)$ after choosing a lattice/Hodge normalization. The Rosati trace form is $2\Re(x\bar y)$, differing by a positive factor. Complexifying this real model gives the two-dimensional complex $H^1$ with eigenvalues $\pi,\bar\pi$. The uncomplexified real space $K\otimes\mathbb R$ must not be identified dimensionally with the complex Hilbert space $H^1(\mathbb T^2,\mathbb C)$. $\square$

If a self-adjoint “Hamiltonian” rather than a unitary is required, choose a spectral logarithm $H_{\rm PH}$ with $e^{iH_{\rm PH}}=U_{\rm PH}$. Its phases are defined modulo $2\pi$; the curve does not specify that branch. An ordinary elliptic curve is outside the supersingular quadratic class: in the Newton definition an ordinary elliptic curve has slopes $0,1$, whereas H-SS-NP gives slopes $1/2$ in T0. The PH unitary here is obtained from the lifted arithmetic endomorphism, not from an equation-local Gauss transfer.

**Status:** conditional-on H-DEURING, H-DEG, H-FROB; the metric, positivity, and discriminant implications are proved-here. The ordinary/supersingular comparison additionally uses H-SS-NP and H-AV-FUNCTOR. This is an implication from strong lifting inputs, not a claim that their usual proofs are historically independent of Hasse or Weil theory.

### Proposition T1.7 (integral markings versus MPS gauge)

**Hypotheses:** H-DEURING, H-LM, H-WAT; ordinary elliptic isogeny class with fixed $\pi$.

**Statement.** Integral multiplication matrices change by $\mathrm{GL}_2(\mathbb Z)$ conjugacy under a change of lattice basis. Their classes are ideal-lattice classes for $\mathbb Z[\pi]$; the multiplier order of a lattice is its endomorphism order. The ordinary curve classification is recovered from these integral data as in H-WAT. Complex spectral data forget these ideal classes. This is not a classification of graded MPS gauge orbits.

**PROOF.**

<1>1. If a basis changes by $S\in\mathrm{GL}_2(\mathbb Z)$, multiplication changes from $M$ to $S^{-1}MS$. Conversely, an integral conjugacy intertwines the $\mathbb Z[\pi]$-lattice structures. H-LM gives exactly this interpretation; noninvertible lattices over $\mathbb Z[\pi]$ are needed to include larger multiplier orders.

<1>2. H-WAT associates the endomorphism-order strata with the appropriate ideal classes. This retains information absent from the characteristic polynomial. It is an arithmetic classification with integral structures, not a consequence of the complex tensor's gauge freedom.

<1>3. Since $\pi\ne\bar\pi$, every complex $2\times2$ matrix in this isogeny class is diagonalizable with the same eigenvalues. All such matrices are $\mathrm{GL}_2(\mathbb C)$-conjugate. On $H^1$ the actual integral pullback matrix is $M^T$, acting on the dual lattice; transposition should not be confused with the original ideal marking. An orthonormal Hodge basis diagonalizes and unitarizes it after normalization.

<1>4. MPS gauge acts instead on the ket $V$ by an even $G\in\mathrm{GL}(1|1)$ and on the double by $G\otimes\bar G$. The tensor in T1.3, with fixed embedding and physical vector, is already identical throughout the isogeny class. General complex conjugations of $H^1$ need not lift to this restricted ket gauge. Exchanging the two Hodge embeddings replaces $\pi$ by $\bar\pi$ and is not an even ket gauge of $\operatorname{diag}(1,\pi)$.

<1>5. In any dimension, $\operatorname{Tr}(PGXG^{-1})=\operatorname{Tr}(PX)$ for even $G$, and
$$\mathcal E\longmapsto(G\otimes\bar G)\mathcal E(G^{-1}\otimes\bar G^{-1}).$$
Thus all ring amplitudes, norms, and zeta functions are gauge invariant. A nonunitary gauge need not preserve a displayed Hilbert--Schmidt norm or normality in the old metric; the metric must be transported. $\square$

**Status:** conditional-on H-DEURING, H-LM, H-WAT; the distinctions and gauge calculations are proved-here.

## T2. Digits and finite carries

### Proposition T2.1 (ordinary digit expansions, cyclic fibres, and bounded carries)

**Hypotheses:** $O$ is the ordinary elliptic order, $\pi\in O$, $|\pi|^2=q>1$, and $D\subset O$ is a complete set of representatives of $O/\pi O$.

**Statement.** $|D|=q$, and every class in $O/\pi^nO$ has exactly one expansion $\sum_{i=0}^{n-1}d_i\pi^i$ with $d_i\in D$. For the cyclic quotient, the map
$$D^n\longrightarrow O/(\pi^n-1)O$$
need not be onto, even if the target has fewer than $q^n$ elements. Two words $d,e$ have the same image exactly when they admit integral cyclic carries
$$d_i-e_i=\pi c_{i+1}-c_i,\qquad c_n=c_0,\qquad c_i\in O.$$
These carries are unique for a given pair and obey the uniform bound
$$|c_i|\le \frac{C_D}{|\pi|-1},\qquad C_D=\max_{d,e\in D}|d-e|.$$
Thus the cyclic equivalence relation itself has a finite carry automaton.

**PROOF.**

<1>1. Multiplication by $\pi$ has index $q$. Given $x\in O$, select the unique $d_0\in D$ congruent to $x$ modulo $\pi O$, and divide $x-d_0$ by $\pi$. Repetition gives existence modulo $\pi^n$. If two expansions agree modulo $\pi^n$, reduction modulo $\pi$ makes their first digits equal, after which division and induction prove uniqueness.

<1>2. Equality in the cyclic quotient means
$$\sum_{i=0}^{n-1}(d_i-e_i)\pi^i=(\pi^n-1)c_0$$
for a unique $c_0\in O$. Reduction modulo $\pi$ shows that $c_0+d_0-e_0$ is divisible by $\pi$. Defining $c_{i+1}=(c_i+d_i-e_i)/\pi$ recursively gives integral carries; the same congruence argument applies at each step. Telescoping the displayed sum gives $c_n=c_0$. Conversely, integral cyclic carries telescope to equality in the quotient.

<1>3. Let $R=\max_i|c_i|$. The recursion gives $|\pi|R\le R+C_D$, using cyclicity to take the maximum on both sides. Hence $R\le C_D/(|\pi|-1)$. A lattice has finitely many points in this disk, so the relation is recognized by a fixed finite graph with edges labeled by digit pairs.

<1>4. Surjectivity already fails for $O=\mathbb Z[i]$, $\pi=1+2i$, $q=5$, $D=\{0,1,-1,2,-2\}$. These digits are distinct modulo $\pi$, since $O/\pi O\simeq\mathbb F_5$. But $O/(\pi-1)O=O/(2i)\simeq O/(2)$ has four classes and the integer digits represent only two of them. For the same $\pi$, $|1-\pi^2|^2=32>25$, so no five-digit alphabet can surject at $n=2$, regardless of representatives. These are actual ordinary elliptic data: $y^2=x^3+x$ over $\mathbb F_5$ has four points, Frobenius roots $1\pm2i$, and endomorphism order $\mathbb Z[i]$ (the order already contains multiplication by $i$). $\square$

**Status:** proved-here given the order and degree data; the example's point count is direct.

### Proposition T2.2 (what finite carries do not count)

**Hypotheses:** T2.1; a positive-genus curve count sequence with nonempty net numerator as in H-FROB, with numerator and denominator spectra disjoint. The latter follows from H-WEIL for a curve. The trace-class extension uses H-LIDSKII.

**Statement.** No finite weighted adjacency matrix, even with arbitrary complex weights, has its ordinary closed-walk traces equal to $N_n$ for every $n$. Nor does any trace-class operator have this power-trace sequence. In particular no finite automaton with nonnegative transition counts can count all the cyclic quotient classes by its unweighted rings. This is compatible with the finite carry relation in T2.1.

**PROOF.**

<1>1. For a finite matrix $B$,
$$\sum_{n\ge1}\operatorname{Tr}(B^n)u^n
=\sum_{\lambda\ne0}m_B(\lambda)\frac{\lambda u}{1-\lambda u}.$$
Its residue at $u=1/\lambda$ is $-m_B(\lambda)/\lambda$, with nonnegative integral multiplicity. A curve numerator eigenvalue $\alpha$ instead contributes residue $+m_C(\alpha)/\alpha$. Distinct poles cannot change each other's residues. This is the proof of `thm:no-ungraded-trace` specialized to finite dimension.

For a trace-class operator, H-LIDSKII gives the same series with absolutely summable nonzero eigenvalues. Its rational summands converge locally uniformly away from their poles: for sufficiently small $|\lambda|$ on a fixed compact $u$-set, $|1-\lambda u|\ge1/2$, and the tails are bounded by a constant times $\sum|\lambda|$. Thus it is meromorphic with the same nonnegative-multiplicity residues. The identical contradiction applies.

<1>2. The carry automaton counts pairs of words with equal represented value, with their allowed carry cycles. It does not count equivalence classes of words with unit weight, nor does its domain represent every element of the cyclic quotient. Fibres have the exact description in T2.1, but no uniform fibre size follows. Taking a quotient of a recognized relation is not the same operation as taking the trace of its adjacency matrix.

<1>3. A finite **graded weighted** transfer does suffice: on an abstract $2|2$ transfer space take $\operatorname{diag}(1,q)$ even and the integral Frobenius matrix $M$ odd. Its supertrace is $N_n$. If one calls this a signed automaton, signs can occur both through the grading and through entries of $M$. It is not a nonnegative carry enumeration. A supermatrix alone is also not a proof of a doubled-Kraus factorization; the elliptic tensor in T1.3 separately provides that factorization over $\mathbb C$. $\square$

**Correction.** In this expanding complex-base problem, cyclic carries are **bounded**. The failure is not forced unboundedness of carries. It is the difference between recognizing equality of digit words and counting all quotient elements with weight one.

**Status:** proved-here in finite dimension; trace-class extension conditional-on H-LIDSKII; the interpretation as elliptic point modules additionally uses H-LENSTRA.

## T3. Bosonic no-go, minimal dimension, and infinite-bond qualifications

### Theorem T3.1 (block structure and the corrected Hilbert--Schmidt bounds)

**Hypotheses:** Finitely many even tensors $A_s=a_s\oplus B_s$ on $\mathbb C^{m|k}$. Use the ordinary Hilbert--Schmidt metrics in the displayed bases.

**Statement.** With $H_{\epsilon\delta}=V_\epsilon\otimes\bar V_\delta$,
$$S_+=\mathcal E_{++}=\sum_s a_s\otimes\bar a_s,\quad
S_-=\mathcal E_{--}=\sum_s B_s\otimes\bar B_s,\quad
M=\sum_s a_s\otimes\bar B_s.$$
The even block is $S_+\oplus S_-$; the odd block is $M\oplus\bar M$, where a fixed tensor-factor flip identifies the second mixed sector with the conjugate of the first. Define
$$\tau_+=\sum_s\|a_s\|_{\rm HS}^2,\qquad \tau_-=\sum_s\|B_s\|_{\rm HS}^2.$$
Then
$$
\sum_{\mu\in\operatorname{spec}\mathcal E_o}|\mu|^2
=2\sum_{\mu\in\operatorname{spec}M}|\mu|^2
\le2\|M\|_{\rm HS}^2
\le2\tau_+\tau_-,                                           \tag{3.1}
$$
and the useful alternative bound is
$$\|M\|_{\rm HS}^2\le\|S_+\|_{\rm HS}\|S_-\|_{\rm HS}.       \tag{3.2}$$
In general $\tau_\pm\ne\operatorname{Tr}S_\pm$; actually
$$\operatorname{Tr}S_+=\sum_s|\operatorname{Tr}a_s|^2,\qquad
\operatorname{Tr}S_-=\sum_s|\operatorname{Tr}B_s|^2.           \tag{3.3}$$
Thus the drafted bound with $2\operatorname{Tr}S_+\operatorname{Tr}S_-$ is false.

**PROOF.**

<1>1. An even matrix preserves $V_+$ and $V_-$. Its double therefore preserves all four $H_{\epsilon\delta}$ and restricts to the displayed Kronecker products. On $H_{-+}$ the restriction is $\sum_s B_s\otimes\bar a_s$; flip the factors to obtain $\bar M$. This proves the block and multiplicity statements.

<1>2. For completeness, Schur triangularization writes a finite matrix as $UTU^*$ with $U$ unitary and $T$ triangular. Its squared Hilbert--Schmidt norm is the sum of squared moduli of all entries of $T$, whereas the squared eigenvalue sum counts just the diagonal. Equality means that $T$ is diagonal, equivalently the matrix is normal. This proves H-SCHUR in the form used here.

<1>3. The triangle inequality for the Hilbert--Schmidt norm and then H-CS give
$$\|M\|_{\rm HS}\le\sum_s\|a_s\|_{\rm HS}\|B_s\|_{\rm HS}
\le\sqrt{\tau_+\tau_-}.$$
Together with step 2 this proves (3.1).

<1>4. Put $C_{st}=\operatorname{Tr}(a_s^*a_t)$ and $D_{st}=\operatorname{Tr}(B_s^*B_t)$. Direct expansion gives
$$\|M\|_{\rm HS}^2=\sum_{s,t}C_{st}\overline{D_{st}},\quad
\|S_+\|_{\rm HS}^2=\sum_{s,t}|C_{st}|^2,\quad
\|S_-\|_{\rm HS}^2=\sum_{s,t}|D_{st}|^2.$$
H-CS on the Gram-matrix entries proves (3.2). Formula (3.3) is $\operatorname{Tr}(A\otimes\bar A)=|\operatorname{Tr}A|^2$.

<1>5. An exact counterexample to the drafted trace bound is one species with $m=k=2$ and $a=B=\operatorname{diag}(1,-1)$. Both $S_\pm$ have trace zero. But $M=a\otimes a$ has four eigenvalues of modulus one, so the odd squared eigenvalue sum is $8>0$. Also a nonzero nilpotent $a=e_{12}$ has $\operatorname{Tr}(a\otimes\bar a)=0$; zero trace does not force zero Kraus tensors. $\square$

The supplied `weil_ring_norm_check.py` computes `tpp` and `tmm` as sums of squared Frobenius norms, while its comments call them traces of the doubled blocks. Its random inequalities validate (3.1), not the drafted trace inequality. No numerical fact about those random tests supplies the missing equality.

**Status:** proved-here, using H-CS; H-SCHUR is proved-here.

### Lemma T3.2 (a bound for all power traces)

**Hypotheses:** T3.1. Set $s_\pm(n)=\operatorname{Tr}S_\pm^n$.

**Statement.** For every $n\ge1$,
$$s_\pm(n)\ge0,\qquad
|\operatorname{Tr}M^n|^2\le s_+(n)s_-(n).                    \tag{3.4}$$
If equality holds, the vectors of traces of length-$n$ words in the two block tensors are proportional (with the usual zero-vector exception).

**PROOF.**

<1>1. For a word $w=(s_1,\ldots,s_n)$ put $a_w=a_{s_1}\cdots a_{s_n}$ and $B_w=B_{s_1}\cdots B_{s_n}$. Expansion of powers and tensor traces gives
$$s_+(n)=\sum_w|\operatorname{Tr}a_w|^2,\quad
s_-(n)=\sum_w|\operatorname{Tr}B_w|^2,\quad
\operatorname{Tr}M^n=\sum_w\operatorname{Tr}a_w\,\overline{\operatorname{Tr}B_w}.$$

<1>2. These are two squared vector norms and their inner product. H-CS proves the inequality and its equality statement. $\square$

**Status:** proved-here, using H-CS.

### Theorem T3.3 (the genus bound survives, without the false trace estimate)

**Hypotheses:** T3.1; the nonzero even spectrum is exactly $\{1,q\}$ and there is no even--odd cancellation; the nonzero odd spectrum is precisely the $2g$ Frobenius values, all of modulus $\sqrt q$, with $g\ge1$.

**Statement.** $g\le1$. Moreover $\{\operatorname{Tr}S_+,\operatorname{Tr}S_-\}=\{1,q\}$. For $m=k=1$, $g=1$ forces the two physical coefficient vectors to be proportional, and gives T1.3 after scaling and choice of the conjugate eigenvalue. The corresponding matrix proportionality and normality assertions for arbitrary $m,k$ are false without further minimality and metric hypotheses.

**PROOF.**

<1>1. The two nonzero even eigenvalues partition between the two blocks. If either block had no nonzero eigenvalue, all of its positive-power traces would vanish. By (3.4), $\operatorname{Tr}M^n=0$ for all $n$. A Vandermonde argument on the distinct nonzero eigenvalues of $M$ would then force $M$ to have none, contrary to the nonempty odd spectrum. Thus each even block contains one of $1,q$. In particular its traces of all powers are $1$ or $q^n$.

<1>2. The nonzero spectrum of $M$ has exactly $g$ entries with multiplicity. Write them as $\sqrt q\,\beta_1,\ldots,\sqrt q\,\beta_g$, with $|\beta_j|=1$. Equation (3.4) becomes
$$\left|\sum_{j=1}^g\beta_j^n\right|^2\le1\qquad(n\ge1).    \tag{3.5}$$

<1>3. Average the left side over $1\le n\le N$. For distinct unit complex numbers $\beta,\gamma$, the Cesàro mean of $(\beta\bar\gamma)^n$ tends to zero by summing a geometric progression. If the distinct $\beta$'s have multiplicities $m_1,\ldots,m_r$, the limit of the average is $\sum_i m_i^2\ge\sum_i m_i=g$. Equation (3.5) bounds that limit by one. Hence $g\le1$.

<1>4. For $m=k=1$, set $a=(a_s)$ and $b=(B_s)$. The even eigenvalues are $\|a\|^2,\|b\|^2$ and the odd ones are $\langle a,b\rangle$ and its conjugate. Their squared modulus is $q=\|a\|^2\|b\|^2$. Equality in H-CS gives $b=c a$. Choosing the even assignment $\|a\|^2=1$ gives $|c|^2=q$.

<1>5. This does not extend to a literal matrix proportionality claim. For example, take $m=1,k=3$, let $N=e_{12}$ on a two-dimensional transient subspace, and take two even species with
$$a_0=1,\ a_1=0,\qquad B_0=\pi\oplus0_2,\quad B_1=0\oplus N.$$
The only nonzero even eigenvalues are $1,q$ and the only nonzero odd ones are $\pi,\bar\pi$. Nevertheless $B_1\ne0$ while $a_1=0$. All positive-power traces are the elliptic ones. Also with $m=1,k=2$, a single $B_0=\left(\begin{smallmatrix}\pi&b\\0&0\end{smallmatrix}\right)$, $b\ne0$, gives the same spectra and a nonnormal $M=\bar B_0$. Normality in a specified Euclidean gauge is not forced by these trace identities. $\square$

For $g=1$ in general dimensions, the valid equality conclusion from (3.4) is proportionality of the **word-trace vectors at every length**, not equality of the block matrices themselves. Nilpotent transient data are invisible to these traces.

**Status:** proved-here under the stated spectral-modulus hypothesis; for curve spectra that hypothesis is conditional-on H-WEIL.

### Proposition T3.4 (Euler characteristic and the correct minimum)

**Hypotheses:** A finite graded tensor on $\mathbb C^{m|k}$ has $\operatorname{str}\mathcal E^n=N_n$ for all $n\ge1$, with curve net spectrum $\{1,q\}_+-\{\alpha_1,\ldots,\alpha_{2g}\}_-$. Let $z_e,z_o$ count zero eigenvalues algebraically.

**Statement.**
$$ (m-k)^2-(z_e-z_o)=2-2g.                                 \tag{3.6}$$
Necessarily $mk\ge g$. If the odd dimension is exactly $2g$, then $mk=g$, there are no odd zero modes and no nonzero cancellations, and the even zero primary subspace has dimension $m^2+k^2-2$. Under the additional choice $m=1$, this is $g^2-1$ on $\mathbb C^{1|g}$. The minimum bond dimension for the dimension constraint $mk\ge g$ is
$$\min_{m,k\ge1,\ mk\ge g}(m+k),$$
not generally $g+1$. If one also requires $mk=g$, minimize over factor pairs of $g$. These are dimension bounds, not general existence theorems.

**PROOF.**

<1>1. Equality of positive-power supertraces determines the net multiplicity at every nonzero eigenvalue: apply partial fractions to $\sum_{n\ge1}\operatorname{str}\mathcal E^n u^n$. Its net nonzero multiplicity sum is therefore $2-2g$.

<1>2. Independently, that sum is
$$[m^2+k^2-z_e]-[2mk-z_o]=(m-k)^2-(z_e-z_o),$$
which proves (3.6). This is not an assertion about $\operatorname{str}\mathcal E^0$, where zero modes reappear.

<1>3. The $2g$ required nonzero odd eigenvalues need $2mk\ge2g$ dimensions. If equality holds, all odd dimensions are already used; no additional odd zero or cancelling nonzero eigenvalues fit. The even block then has just two nonzero eigenvalues, so $z_e=m^2+k^2-2$. Its restriction to the zero primary subspace is nilpotent by Cayley--Hamilton.

<1>4. The dimension minimizations are immediate integer optimization. For example, at $g=4$, $2|2$ has dimension four, whereas $1|4$ has dimension five. At genus two, the only factor pairs are $(1,2),(2,1)$ and bond dimension three is necessary. $\square$

**Status:** proved-here.

### Proposition T3.5 (odd species and cancellations)

**Hypotheses:** Homogeneous tensors, with even tensors $a_s\oplus B_s$ and odd tensors $\left(\begin{smallmatrix}0&c_f\\d_f&0\end{smallmatrix}\right)$. For the cancellation statement suppose all tensors are even and the common nonzero multiset is $X$.

**Statement.** Odd species add off-diagonal couplings between $H_{++}$ and $H_{--}$ in the even transfer and between the two mixed sectors in the odd transfer. The former couplings have zero trace as blocks of the whole even matrix; the latter invalidate the decoupled mixed-block argument. With bosonic cancellation, one has
$$s_+(n)+s_-(n)=1+q^n+\sum_{x\in X}x^n,
\qquad |\operatorname{Tr}M^n|^2\le s_+(n)s_-(n),             \tag{3.7}$$
and in particular $\operatorname{Tr}S_++\operatorname{Tr}S_-=1+q+\sum X$. These do not imply a genus bound independent of $X$.

**PROOF.**

<1>1. $c_f:V_-\to V_+$ and $d_f:V_+\to V_-$. Hence the even off-diagonal blocks are $\sum_f c_f\otimes\bar c_f$ and $\sum_f d_f\otimes\bar d_f$. They do not enter the ordinary trace at length one, although they do enter traces of higher powers.

<1>2. The mixed off-diagonal blocks are $\sum_f c_f\otimes\bar d_f$ and $\sum_f d_f\otimes\bar c_f$. Thus the odd transfer is no longer $M\oplus\bar M$ and (3.4) does not bound its full spectrum.

<1>3. In the purely even case with cancellation, expand the known even spectrum and use T3.2. Also
$$\left|\sum_j\alpha_j^n+\sum_{x\in X}x^n\right|
=|2\Re\operatorname{Tr}M^n|
\le2\sqrt{s_+(n)s_-(n)}\le s_+(n)+s_-(n).$$
The $s_\pm(n)$ are nonnegative by the word formula, even if the individual eigenvalues are complex. The added spectrum can contribute to both the allowed growth and the oscillatory sums. Neither $\tau_+\tau_-$ in (3.1) nor the two factors in (3.7) are fixed by the sum at $n=1$. $\square$

This proves that physical fermions are necessary on the minimal genus-two bond $1|2$, because that bond has no room for cancellation. It does not prove necessity for every larger bond with arbitrary cancellation. The unsuccessful bosonic $2|2$ search is not a nonexistence certificate.

**Status:** proved-here; the minimal curve application uses the hypotheses of T3.3--T3.4.

### Theorem T3.6 (the infinite-bond no-go with a justified constant)

**Hypotheses:** H-KRAUS-HS and H-ZERO. Suppose the odd eigenmodes at time $t$ include $e^{t\mu_\rho}$ with multiplicities, where either $\mu_\rho=\rho$ or the notebook's $\mu_\rho=-\bar\rho/2$ (more generally the real parts lie in a fixed bounded interval).

**Statement.** Such a purely bosonic Kraus realization cannot exist. The correct general bound would be
$$
\sum_\rho e^{2t\Re\mu_\rho}
\le\|\mathcal E_o(t)\|_{\rm HS}^2
\le2\|S_+(t)\|_{\rm HS}\|S_-(t)\|_{\rm HS}<\infty.        \tag{3.8}
$$
The draft's smaller-looking expression $2\operatorname{Tr}S_+\operatorname{Tr}S_-$ is justified, for example, if $S_\pm$ are additionally positive self-adjoint operators on their Hilbert--Schmidt spaces. Complete positivity of the underlying Kraus map alone does not imply that extra property.

**PROOF.**

<1>1. Compress the bond to finite-dimensional subspaces in $H_+,H_-$, increasing strongly to the identities. The compressed Kraus matrices have finite total squared Hilbert--Schmidt norm: it is a finite sum of matrix elements of the normal CP image of a finite-rank projection. Thus the finite-dimensional Gram argument in T3.1 applies also to their countable Kraus sums, by convergence of the corresponding Gram matrices.

<1>2. Let $M_N,S_{+,N},S_{-,N}$ be the resulting compressed blocks. By the compression compatibility in H-KRAUS-HS,
$$\|M_N\|_{\rm HS}^2\le\|S_{+,N}\|_{\rm HS}\|S_{-,N}\|_{\rm HS}
\le\|S_+\|_{\rm HS}\|S_-\|_{\rm HS}.$$
Squared Hilbert--Schmidt norms of the increasing matrix corners of $M$ increase to the sum of squares of all its entries. This bound makes that sum finite and proves that $M$ is Hilbert--Schmidt, with the same inequality. The second mixed block is its conjugate, so its contribution supplies the factor two.

<1>3. For a Hilbert--Schmidt operator, the squared eigenvalue sum is bounded by the squared Hilbert--Schmidt norm. One can derive the needed version by applying finite-dimensional Schur to invariant subspaces spanned by any finite collection of generalized eigenvectors of this compact operator, and then increasing the collection. This gives the first inequality in (3.8), including algebraic multiplicity.

<1>4. For fixed $t>0$, $e^{2t\Re\mu_\rho}$ is bounded below by a positive constant. In the notebook normalization it exceeds $e^{-t}$; in the unshifted normalization it exceeds $1$. H-ZERO gives infinitely many such terms, so the left side diverges, contradicting step 3.

<1>5. If $S_\pm$ are positive self-adjoint and trace class, their nonnegative eigenvalues imply $\|S_\pm\|_{\rm HS}\le\operatorname{Tr}S_\pm$. This proves the optional trace version. In general the finite-dimensional counterexample T3.1 rules out that substitution. $\square$

Neither no-cancellation nor Lidskii is needed for this corrected Hilbert--Schmidt obstruction. H-LIDSKII does justify the separate trace-class spectral assertions in shard 04b. The conclusion is that fermionic species are necessary **if this analytic setting is retained**; an infinite-bond construction could instead fail the trace-class/CP-extension assumptions. Establishing those assumptions for a proposed Riemann cMPS, or constructing a fermionic one, is not done here.

**Status:** conditional-on H-KRAUS-HS and H-ZERO; the compression and divergence argument is proved-here.

## T4. Tier B: ordinary genus two

Let $C/\mathbb F_q$ have genus two and simple ordinary Jacobian. Under H-CM, write $H=H^{1,0}(\widetilde J)$, choose a CM eigenbasis, and put
$$D=\operatorname{diag}(\pi_1,\pi_2),\qquad
\chi_F(z)=z^4-a z^3+b z^2-qa z+q^2.$$
Here the complete root multiset is $\{\pi_1,\pi_2,\bar\pi_1,\bar\pi_2\}$, $a,b\in\mathbb Z$, and $|\pi_j|^2=q$. The proposed ket vector space $V=\mathbb C\oplus H$ has grading $1|2$. Unlike the elliptic case, it is the exterior algebra **truncated after degree one**. Its double has even dimension five and odd dimension four; it is not already the cohomology of the curve.

### Lemma T4.1 (the block equations, with conjugations fixed)

**Hypotheses:** Even tensors $A_s=\left(\begin{smallmatrix}a_s&0\\0&B_s\end{smallmatrix}\right)$ and odd tensors $A_f=\left(\begin{smallmatrix}0&c_f\\d_f&0\end{smallmatrix}\right)$ on $1|2$, with $c_f$ a $1\times2$ row and $d_f$ a $2\times1$ column. Order the odd basis as $(|0\rangle\otimes|\bar j\rangle)_{j=1,2}$, then $(|i\rangle\otimes|\bar0\rangle)_{i=1,2}$; use row-major vectorization on the $2\times2$ block.

**Statement.**
$$
\mathcal E_o=\begin{pmatrix}M&N\\\bar N&\bar M\end{pmatrix},
\quad M=\sum_s a_s\bar B_s,
\quad N=\sum_f\bar d_f c_f,                                \tag{4.1}
$$
and
$$
\mathcal E_e=\begin{pmatrix}t&u\\v&W\end{pmatrix},\quad
t=\sum_s|a_s|^2,\quad
u=\sum_f c_f\otimes\bar c_f,\quad
v=\sum_f d_f\otimes\bar d_f,\quad
W=\sum_s B_s\otimes\bar B_s.                              \tag{4.2}
$$
Here $u$ is a $1\times4$ row and $v$ a $4\times1$ column; later scalar parameters denoted $h$ will avoid confusing them with scalar jump rates. The tensor notation $c_f\otimes\bar d_f$ for the mixed coupling means, in the indicated bases, the matrix $\bar d_f c_f$.

**PROOF.**

<1>1. Under $|i\rangle\otimes|\bar j\rangle\leftrightarrow|i\rangle\langle j|$, the double of $A$ acts by $X\mapsto AXA^*$. An even $A$ sends the off-diagonal row $X_{0j}$ to $a_s\sum_l\bar B_{s,jl}X_{0l}$, giving $M$. Its action on the lower block is the conjugate.

<1>2. For an odd $A_f$, the coefficient from $X_{i0}$ to the output entry $(0,j)$ is $c_{f,i}\bar d_{f,j}$. This is $(\bar d_fc_f)_{ji}$, giving $N$ and its conjugate in (4.1).

<1>3. On an even operator $x\oplus X$, the complete CP map is
$$
\Phi(x\oplus X)=
\left(t x+\sum_f c_f X c_f^*\right)
\oplus\left(\sum_f d_f x d_f^*+\sum_s B_sXB_s^*\right).
$$
Vectorization gives exactly (4.2). No Koszul sign is added to this computation: H-TWIST has already specified the norm transfer as an ordinary Kronecker sum. $\square$

**Status:** proved-here.

### Proposition T4.2 (the literal geometric placement and the suggested vacuum ansatz fail)

**Hypotheses:** T4.1; the nonzero odd spectrum is the four Frobenius values and the even spectrum is $\{1,q,0,0,0\}$.

**Statement.** The $q$-eigenvector cannot be the pure trace-line operator $0\oplus I_2$. The vacuum line cannot itself be an invariant line carrying the eigenvalue $1$. The suggested two-even, one-odd ansatz
$$a_1=1,\ B_1=0,\ a_2=0,\ B_2=B$$
cannot have the desired odd spectrum, for any $B,c,d$. Thus the geometric ket-space proposal is compatible with a tensor only after allowing mixing in the two nonzero even modes.

**PROOF.**

<1>1. If $0\oplus I_2$ were a $q$-eigenvector, its vacuum output in (4.2) would vanish:
$$\sum_f c_f I_2 c_f^*=\sum_f\|c_f\|^2=0.$$
Hence every $c_f=0$, and $N=0$. The even block is triangular with diagonal blocks $t,W$; the odd block is $M\oplus\bar M$. Deleting all odd species leaves exactly these diagonal blocks and the same spectra. It would therefore produce a purely bosonic genus-two tensor without cancellation, contradicting T3.3.

<1>2. Invariance of the vacuum line requires $\sum_f d_fd_f^*=0$, which forces all $d_f=0$. The same triangular-deletion argument again contradicts T3.3. This also shows that both directions of fermionic coupling must occur somewhere in any such realization.

<1>3. In the suggested vacuum ansatz, $M=0$. For one odd species, $N=\bar d c$ has rank at most one. Therefore $\mathcal E_o=\left(\begin{smallmatrix}0&N\\\bar N&0\end{smallmatrix}\right)$ has rank at most two and at least two zero eigenvalues, whereas all four Frobenius eigenvalues are nonzero. Even with more odd species, $M=0$ forces a spectrum symmetric under $z\mapsto-z$ and trace zero, so it still cannot give the supplied trace-$3$ example. $\square$

The vector-space identification of the $(-,-)$ sector with $H\otimes\bar H$ is valid. Identifying its pure trace line with an invariant $q$-line of the full CP transfer is the invalid extra demand. The count spectrum alone also does not locate the three zero modes in the traceless subspace. The construction next does put them there, while mixing vacuum and trace in the two surviving modes.

**Status:** proved-here under the modulus hypothesis used in T3.3.

### Theorem T4.3 (explicit genus-two tensors for $q+1\ge4\sqrt q$)

**Hypotheses:** $q>1$, complex algebraic numbers $\pi_1,\pi_2$ with $|\pi_j|^2=q$, and
$$q+1\ge4\sqrt q\quad\text{equivalently}\quad q\ge7+4\sqrt3. \tag{4.3}$$
For a curve-count interpretation assume H-FROB with these four conjugate-paired eigenvalues, and H-TWIST. For prime powers, every $q\ge16$ satisfies (4.3). No simplicity assumption is needed for the matrix construction.

**Statement.** There are explicit algebraic tensors on $\mathbb C^{1|2}$ with **five even letters and four odd letters** such that
$$\operatorname{spec}\mathcal E_e=\{1,q,0,0,0\},\qquad
\mathcal E_o=\operatorname{diag}(\bar D,D).                 \tag{4.4}$$
The three zero modes are exactly the traceless $2\times2$ operators and are killed in one step. In an orthonormal doubled basis the full transfer is normal. Consequently, for every $n\ge1$,
$$\|\Psi_P(n)\|^2=1+q^n-\sum_{j=1}^2(\pi_j^n+\bar\pi_j^n)=N_n(C),$$
and
$$Z_{\rm ring}(u)=\frac{\prod_{j=1}^2(1-\pi_j u)(1-\bar\pi_j u)}{(1-u)(1-qu)}=Z(C,u).$$
This is a proved replacement with more species and a field-size hypothesis, not a proof of the drafted three-species theorem for every $q$.

**Construction.** Put
$$t=\frac{q+1}{2},\qquad w=\frac{q+1}{4},\qquad
h=\frac{q-1}{2\sqrt2},\qquad B_0=D/\sqrt t,$$
and let $b_0=\operatorname{vec}(B_0)\in\mathbb C^4$, using the vectorization in T4.1. Set
$$\nu=b_0^*b_0=\frac{2q}{t},\qquad R=wI_4-b_0b_0^*.$$
Condition (4.3) is precisely $w\ge\nu$. The positive square root has the elementary closed form
$$S=R^{1/2}=\sqrt w\,I_4+
\frac{\sqrt{w-\nu}-\sqrt w}{\nu}\,b_0b_0^*.                \tag{4.5}$$
For $\ell=1,\ldots,4$, define $B_\ell=\operatorname{unvec}(S e_\ell)$. The even tensors are
$$A_0=\begin{pmatrix}\sqrt t&0\\0&B_0\end{pmatrix},\qquad
A_\ell=\begin{pmatrix}0&0\\0&B_\ell\end{pmatrix}\quad(1\le\ell\le4).$$
For the standard real basis $e_1,e_2$ of $\mathbb C^2$, the four odd tensors are
$$A_{\uparrow j}=\begin{pmatrix}0&\sqrt h\,e_j^T\\0&0_2\end{pmatrix},\qquad
A_{\downarrow j}=\begin{pmatrix}0&0\\\sqrt h\,e_j&0_2\end{pmatrix},\quad j=1,2. \tag{4.6}$$
All square roots of real nonnegative scalars in these formulas denote their nonnegative roots. Zero Kraus matrices, if any at the endpoint, may be omitted. The entries lie in an algebraic extension of $\mathbb Q(\pi_1,\pi_2)$; they are not claimed to lie in that field itself.

**PROOF.**

<1>1. Since $b_0b_0^*$ has eigenvalue $\nu$ on its range and zero on its orthogonal complement, $R\ge0$ exactly when $w\ge\nu$. Equation (4.5) is its square root on these two subspaces. Moreover
$$\sum_{\ell=0}^4\operatorname{vec}(B_\ell)\operatorname{vec}(B_\ell)^*=wI_4.$$
In indices this reads
$$\sum_{\ell=0}^4 (B_\ell)_{ij}\overline{(B_\ell)_{kl}}
=w\delta_{ik}\delta_{jl}.$$
Consequently the even Kraus matrices realize the depolarizing lower-block map
$$\sum_{\ell=0}^4 B_\ell X B_\ell^*=w\operatorname{Tr}(X)I_2. \tag{4.7}$$

<1>2. Only $A_0$ has a nonzero scalar even entry. Thus $M=\sqrt t\,\bar B_0=\bar D$. In every individual odd species in (4.6), either $c$ or $d$ vanishes, so $N=0$. Formula (4.1) gives the odd block in (4.4).

<1>3. Equations (4.6)--(4.7) give, on the even sector,
$$\Phi(x\oplus X)=(t x+h\operatorname{Tr}X)
\oplus(hx I_2+w\operatorname{Tr}X I_2).                    \tag{4.8}$$
It kills every $0\oplus X$ with $\operatorname{Tr}X=0$. On the orthonormal basis consisting of the vacuum matrix unit and $I_2/\sqrt2$, its remaining matrix is
$$\begin{pmatrix}t&\sqrt2h\\\sqrt2h&2w\end{pmatrix}
=\begin{pmatrix}(q+1)/2&(q-1)/2\\(q-1)/2&(q+1)/2\end{pmatrix}.$$
This real symmetric matrix has eigenvalues $q,1$. In the coordinates $x\oplus yI_2$, their eigenvectors can be taken as $(\sqrt2,I_2)$ and $(-\sqrt2,I_2)$, respectively. Neither is the pure vacuum or the pure polarization trace line.

<1>4. The even block is self-adjoint in this metric and the odd block is diagonal, so the whole transfer is normal. Its positive-power supertrace is therefore the displayed sum; the same identity would follow from the characteristic polynomials without normality. H-TWIST identifies it with a physical Hilbert norm, and H-FROB identifies it with the count. Taking formal logarithms gives the stated ring zeta.

<1>5. Algebraicity follows from (4.5)--(4.6), since $\bar\pi_j=q/\pi_j$ and only algebraic scalar operations and square roots occur. The inequality needed for a positive Kraus covariance is exactly the stated field-size hypothesis. No optimization result or small numerical residual is used in this proof. $\square$

The construction is determined by Frobenius on the chosen Hodge space and its Hermitian metric, followed by a specified positive square root. A different orthonormal Hodge basis changes the bond gauge together with inessential unitary choices of same-parity physical letters; a different square-root factorization of the same covariance only mixes even physical letters unitarily, after harmless zero-letter padding. Thus it gives a reproducible cohomological tensor, although no equation-local geometric meaning for its nine letters has been established. Physical species number is not claimed minimal.

The same calculation on $\mathbb C^{1|g}$ works with $t=(q+1)/2$, $w=(q+1)/(2g)$, $h=(q-1)/(2\sqrt g)$, $g^2+1$ even and $2g$ odd letters whenever $q+1\ge2g\sqrt q$. This is an immediate dimensional extension of the proof, not a claim for small $q$ at fixed $g$.

**Status:** proved-here as a matrix and norm construction under (4.3) and the stated eigenvalue moduli; conditional-on H-FROB and H-TWIST for the curve interpretation. H-WEIL supplies the moduli, or T4.7 supplies them from H-CM and H-ROSATI.

### Proposition T4.4 (a concrete base change of the supplied curve)

**Hypotheses:** The supplied exact curve and Frobenius polynomial
$$C:\ y^2=x^5+x^3+x^2-2\quad\text{over }\mathbb F_5,\qquad
\chi_F(z)=z^4-3z^3+7z^2-15z+25,$$
and H-FROB. The input polynomial agrees with the supplied direct counts $3,31,117,619$.

**Statement.** Over $\mathbb F_{25}$ the same curve has Frobenius polynomial
$$\chi_{F^2}(z)=z^4+5z^3+9z^2+125z+625,$$
and T4.3 gives an exact nine-letter $1|2$ tensor for all its point counts. Its first six norms are
$$31,\quad619,\quad15991,\quad390739,\quad9759526,\quad244128859.$$
Its even characteristic polynomial is $z^3(z-1)(z-25)$ and its odd characteristic polynomial is the displayed quartic.

**PROOF.**

<1>1. Base change squares the Frobenius eigenvalues. Their trace becomes $a'=a^2-2b=-5$. Their second elementary symmetric function becomes $b'=b^2-2a(qa)+2q^2=9$, and their new norm parameter is $25$. This gives the displayed polynomial.

<1>2. $25$ satisfies (4.3). Choose one eigenvalue from each conjugate pair of the original quartic, square them to define $D$, and apply the explicit formulas (4.5)--(4.6) with $q=25$. T4.3 proves both characteristic polynomials and all ring counts. Newton's identities applied to the quartic give the six integers above.

<1>3. A floating-point sanity check of these exact formulas gave minimum eigenvalue $2.65384615384615$ for $R$, normality residual $7.5\times10^{-14}$ or less, and relative errors below $2\times10^{-16}$ in the first six counts. Those figures check implementation, not the mathematical proof. Unlike the rounded tensors in the supplied $\mathbb F_5$ output, (4.5)--(4.6) specify the entries exactly. $\square$

The original quartic and its squared-eigenvalue quartic are irreducible over $\mathbb Q$: both reduce modulo $2$ to $z^4+z^3+z^2+z+1$, which has no linear factor and is not divisible by the sole irreducible quadratic $z^2+z+1$. Thus, using the standard functoriality that a proper abelian subvariety gives a proper Frobenius-polynomial factor, both Jacobians are simple over their stated fields. Ordinarity is preserved by finite base extension: the $p$-adic eigenvalue valuations and $v_p(q)$ are both multiplied by the extension degree, so Newton slopes are unchanged. This uses the supplied ordinarity of the original example and does not assert absolute simplicity.

**Status:** conditional-on the supplied Frobenius polynomial, its supplied ordinarity for that interpretation, H-FROB, and H-AV-FUNCTOR for the simplicity/ordinarity assertions; the base-change polynomial and tensor identities are proved-here.

### Proposition T4.5 (an exact feasibility problem, and what the $\mathbb F_5$ numerics do not prove)

**Hypotheses:** T4.1, with exactly two even species and one odd species; prescribed quartic $\chi_F$. For the algebraic-point implication assume H-RCF.

**Statement.** Existence of this tensor class is equivalent to the finite real polynomial feasibility problem
$$\det(zI_5-\mathcal E_e)=z^3(z-1)(z-q),\qquad
\det(zI_4-\mathcal E_o)=\chi_F(z).                         \tag{4.9}$$
The unknowns are the real and imaginary parts of $a_1,a_2,B_1,B_2,c,d$: $28$ real unknowns. If any exact complex solution exists, an algebraic solution exists. Theorem T4.5a below proves exact existence for the supplied $\mathbb F_5$ polynomial by a rational certificate.

**PROOF.**

<1>1. Every entry in (4.1)--(4.2) is polynomial of degree two in these real variables. Each block preserves the relevant conjugation/adjoint real structure, so its characteristic polynomial is real. Equality of their coefficients in (4.9) is a finite system of real polynomial equations with integer coefficients for an actual curve. There are five even and four odd coefficient conditions, some of which can become dependent on special strata.

<1>2. A solution has exactly the requested spectra, including all zero multiplicities, and therefore gives $N_n$ for every $n$ by the trace-of-powers identity and H-TWIST. Conversely, on a $1|2$ bond the four required nonzero odd roots use all four odd dimensions, so T3.4 forbids cancellation or odd zero modes. An all-$n$ realization must therefore satisfy (4.9).

<1>3. H-RCF transfers any real solution of these equations to the real algebraic numbers. Combining its real and imaginary coordinates gives algebraic tensor entries. Thus one cannot legitimately claim that “only transcendental tensor entries work” for this fixed finite species class. Algebraicity conditional on existence is much weaker than an explicit normal form or a construction from the equation.

<1>4. The supplied search reports residual approximately $4.145\times10^{-24}$ in a power-sum least-squares objective, but prints the matrices only to four decimal places. It also reports three small even eigenvalues, not exact zeros. Those observations do not certify (4.9). Fitting many positive powers is compatible with small unwanted eigenvalues and with poorly conditioned nilpotent limits. Failures of the one-even search variants likewise do not prove their nonexistence. $\square$

For the supplied example, (4.9) is explicitly
$$\chi_e(z)=z^5-6z^4+5z^3,\qquad
\chi_o(z)=z^4-3z^3+7z^2-15z+25.$$
A reviewable proof over $\mathbb F_5$ requires, for example, algebraic entries verifying these two identities, or a certified existence argument for this real polynomial system. Theorem T4.5a provides the latter, specifying the entries by a unique algebraic root in a rational box. The constrained real and partially complex ansätze tested during this write-up did not yield that certificate; their failure is not used as an obstruction. The general positive-covariance formula in T4.3 is a separate construction.

**Status:** proved-here for the equivalence; algebraic-point implication conditional-on H-RCF. Exact $\mathbb F_5$ existence is proved in T4.5a; the universal theorem, natural selection, and optimal species counts remain open.

**Conjecture T4.C (a universal three-species educated guess).** For every ordinary simple genus-two curve, (4.9) has a solution with two even letters and one odd letter. The supplied $\mathbb F_5$ example is proved in T4.5a, but there is no proof or universal numerical evidence for this broader conjecture here. Whether those entries can be selected naturally from the equation or the polarized CM data is a further unresolved requirement. **Status: open.**

### Theorem T4.5a (a certified exact three-letter tensor for the supplied curve)

**Hypotheses:** The supplied $\mathbb F_5$ Frobenius polynomial; H-FROB and H-TWIST for its arithmetic norm interpretation. H-RCF is used only to conclude algebraicity of the uniquely specified entries. The rational certificate below is part of the construction.

**Statement.** There exist two even tensors and one odd tensor on $\mathbb C^{1|2}$ with
$$\chi_e(z)=z^3(z-1)(z-5),\qquad
\chi_o(z)=z^4-3z^3+7z^2-15z+25.$$
Their parity-closed ring norm is therefore exactly $N_n(C)$ for **every** $n\ge1$. The entries have an exact algebraic specification by the unique root in the rational box below. This is a computer-assisted algebraic construction for this particular curve, not a formula in radicals for arbitrary genus-two Frobenius data. It proves existence with three letters on the minimum bond; it does not prove that three letters are the minimum possible.

**Definition of the tensors.** In lexicographic order, place complex entries in
$$(0,0,0),(0,1,1),(0,1,2),(0,2,1),(0,2,2),
(1,0,0),(1,1,1),(1,1,2),(1,2,1),(1,2,2),
(2,0,1),(2,0,2),(2,1,0),(2,2,0),$$
where a triple specifies (species, row, column), all numbered from zero. If a position is number $\ell$ in this list, its entry is $x_{2\ell}+i x_{2\ell+1}$; all other entries vanish. Thus species 0 and 1 are even, and species 2 is odd. Start with the 28 rational decimal coordinates in the verifier's base_text. Freeze all except the nine coordinates with indices
$$I=(18,15,11,19,14,2,22,4,3).$$
In this order let the active coordinates be $y\in\mathbb R^9$ and let their rational center $y_0$ be the nine exact decimal strings in the verifier's active list. Set $r=10^{-30}$. Define
$$
f(y)=\big(
 \operatorname{Tr}\mathcal E_e^n-(1+5^n)\ (n=1,\ldots,5);\
 \operatorname{Tr}\mathcal E_o^n-p_n\ (n=1,\ldots,4)
\big),\quad(p_1,p_2,p_3,p_4)=(3,-5,9,7).
$$
The exact tensor uses the **unique zero of $f$ in $\|y-y_0\|_\infty\le r$**, whose existence is proved next. This root specification, the rational box, and the frozen entries determine the tensors without treating their displayed decimal approximations as exact solutions.

**PROOF (rational contraction certificate).**

<1>1. Each $f_i$ is a real polynomial of degree at most ten with rational coefficients. Put $J=Df(y_0)$. The verifier computes $f(y_0)$ and $J$ exactly using pairs of rational numbers for complex entries and
$$\partial_j\operatorname{Tr}(T^n)=n\operatorname{Tr}(T^{n-1}\partial_jT).$$
It obtains a rational approximate inverse $B$ by rounding a proposed high-precision inverse, then verifies the following bounds by **exact rational comparisons**:
$$
\|B\|_\infty<2,\qquad
\|Bf(y_0)\|_\infty<10^{-70},\qquad
\|I-BJ\|_\infty<10^{-50}.                                 \tag{4.10}
$$
Here the matrix norm is the maximum absolute row sum. Numerical inversion only proposes $B$; none of these verified inequalities depends on trusting its floating-point accuracy.

<1>2. On the larger box where every real parameter has absolute value at most 3, every complex tensor entry has absolute value less than 5, and every $3\times3$ tensor has row-sum norm at most 15. Consequently
$$\|\mathcal E\|_\infty<1000,\qquad
\|\partial_j\mathcal E\|_\infty\le30,\qquad
\|\partial_i\partial_j\mathcal E\|_\infty\le2.$$
The same bounds hold on the two invariant principal sectors. For $n\ge2$ and sector dimension $d\le5$, cyclic differentiation bounds each second derivative of $\operatorname{Tr}(T^n)$ by
$$d n\big((n-1)1000^{n-2}30^2+2\,1000^{n-1}\big).$$
For $n\le5$ this is at most $1.4\times10^{14}$; for $n=1$ the bound is at most 10. Hence the uniform bound $H=10^{16}$ for every second partial derivative is valid. All center coordinates have absolute value less than 2, and the radius-$r$ box lies in this larger box.

<1>3. For $y$ in the radius-$r$ box, the mean-value theorem in nine variables gives
$$\|Df(y)-J\|_\infty\le81Hr.$$
Thus the derivative norm of the fixed-point map $\mathcal N(y)=y-Bf(y)$ is at most
$$\kappa:=10^{-50}+2\cdot81\cdot10^{16}10^{-30}<2\cdot10^{-12}<\tfrac14.$$
Also $\|\mathcal N(y_0)-y_0\|_\infty<10^{-70}$, so
$$\|\mathcal N(y)-y_0\|_\infty\le10^{-70}+\kappa r<r.$$
The map is a strict contraction of the closed box into itself. Iteration is Cauchy because successive differences are bounded by a geometric series; completeness gives a fixed point, and the contraction estimate gives uniqueness. Since $\|I-BJ\|_\infty<1$, $BJ$ and hence $B$ are invertible. The fixed point therefore satisfies $f(y)=0$.

<1>4. Newton's identities determine the characteristic polynomial of a $d\times d$ matrix from its first $d$ power traces. The five even and four odd equations therefore give the two characteristic polynomials in the statement, including the three exact even zero roots. Their positive-power supertraces agree with the entire curve-count sequence, regardless of the Jordan structure at zero. H-TWIST supplies the physical norm interpretation.

<1>5. The polynomial equations and rational box form a semialgebraic set over $\mathbb Q$ with exactly one real point. H-RCF supplies an algebraic point in it, so uniqueness implies that the specified point itself is algebraic. This proves the asserted type of exact entries. $\square$

**Reproducible certificate.** This code was run with bytecode writing disabled under a 55-second python3 timeout from the repository root. The concluding norm comparisons are rational. The reported diagnostic values were
$$\|B\|_\infty\simeq1.49913,\quad
\|Bf(y_0)\|_\infty\simeq1.01\times10^{-90},\quad
\|I-BJ\|_\infty\simeq3.52\times10^{-58}.$$

```python
# Author: codex:gpt-6-astra
import mpmath as mp
mp.mp.dps=110
base_text="0.26071183 -0.77630597 0.1256142 0.57129743 0.23357458 -0.48921698 -1.34760956 -0.05591677 -0.94940643 -0.38739751 -0.67840262 -1.61862569 0.09572017 -0.36950433 -0.80102781 0.32500101 -1.0690133 -0.50378403 0.0903946 -0.85610066 -0.89848953 -0.00971177 -0.9517933 -0.63028434 0.30058661 1.43919288 0.38038457 -1.21909557".split()
sel=[18,15,11,19,14,2,22,4,3]
pos=[(s,i,j) for s in range(3) for i in range(3) for j in range(3) if (s<2)==((i==0)==(j==0))]
idxs=([0,4,5,7,8],[1,2,3,6]); ns=(5,4);target=[6,26,126,626,3126,3,-5,9,7]
active = [
    '0.0903946022326197086918581936003652642108422681757834121198569509935751292079285209190880028',
    '0.325001015712151197553026743073611383028909263869300480901353211781331926553983584722142652',
    '-1.61862568848573412561085612335033964354282729706378489347434769629526938804341538871295182',
    '-0.856100671883734631506405289461842300801039252464833047343784570879130428726933907333213827',
    '-0.80102781481057057826927943665335609983310469191396383065095317561795085119201793039066329',
    '0.125614201299343247797946104304359812581511668431930091377412797232085492448163457526247418',
    '-0.951793304521566588362992674206553375775973049960369410863894719514069329407054372830229032',
    '0.233574566527024915170370648357379441749679527579971848850435885749412325417262635189600452',
    '0.571297437238715211680159923446246584732241927298292338354479377560643476028340257150472248'
]
from fractions import Fraction as F
zero=(F(0),F(0));one=(F(1),F(0))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def matmul(a,b):
 out=[[zero for _ in b[0]] for _ in a]
 for i in range(len(a)):
  for k in range(len(b)):
   if a[i][k]==zero:continue
   for j in range(len(b[0])):
    if b[k][j]!=zero:out[i][j]=add(out[i][j],mul(a[i][k],b[k][j]))
 return out
def trace(a):
 z=zero
 for i in range(len(a)):z=add(z,a[i][i])
 assert z[1]==0
 return z[0]
def traced_product(a,b):
 z=zero
 for i in range(len(a)):
  for j in range(len(a)):z=add(z,mul(a[i][j],b[j][i]))
 assert z[1]==0
 return z[0]
x=list(map(F,base_text))
for l,v in zip(sel,active):x[l]=F(v)
As=[[[zero]*3 for _ in range(3)] for _ in range(3)]
for l,(s,i,j) in enumerate(pos):As[s][i][j]=(x[2*l],x[2*l+1])
Es=[]
for idx in idxs:
 E=[]
 for r in idx:
  row=[]
  for c in idx:
   z=zero
   for A in As:z=add(z,mul(A[r//3][c//3],conj(A[r%3][c%3])))
   row.append(z)
  E.append(row)
 Es.append(E)
ps=[]
for E,n in zip(Es,ns):
 p=[[[one if i==j else zero for j in range(len(E))] for i in range(len(E))]]
 for _ in range(n):p.append(matmul(p[-1],E))
 ps.append(p)
f=[trace(p[n])-t for (p,n),t in zip(((p,n) for p,nn in zip(ps,ns) for n in range(1,nn+1)),target)]
J=[[F(0)]*9 for _ in range(9)]
for col,l in enumerate(sel):
 s,i,j=pos[l//2];d=[[zero]*3 for _ in range(3)];d[i][j]=one if l%2==0 else (F(0),F(1));A=As[s]
 des=[[[add(mul(d[r//3][c//3],conj(A[r%3][c%3])),mul(A[r//3][c//3],conj(d[r%3][c%3]))) for c in idx] for r in idx] for idx in idxs]
 vals=[n*traced_product(p[n-1],de) for p,de,nn in zip(ps,des,ns) for n in range(1,nn+1)]
 for row,v in enumerate(vals):J[row][col]=v
print("exact F,J evaluated",flush=True)
to_mp=lambda z:mp.mpf(z.numerator)/z.denominator
BM=mp.inverse(mp.matrix([[to_mp(z) for z in row] for row in J]))
B=[[F(mp.nstr(BM[i,j],60)) for j in range(9)] for i in range(9)]
bn=max(sum(map(abs,row)) for row in B)
eta=max(abs(sum(B[i][j]*f[j] for j in range(9))) for i in range(9))
eps=max(sum(abs(F(i==j)-sum(B[i][k]*J[k][j] for k in range(9))) for j in range(9)) for i in range(9))
radius=F(1,10**30);H=F(10**16);kappa=eps+bn*81*H*radius
assert max(map(abs,x))<2
assert bn<2
assert eta<F(1,10**70)
assert eps<F(1,10**50)
assert kappa<F(1,4)
assert eta+kappa*radius<radius
print("CERTIFIED", "B norm",float(bn),"eta",float(eta),"eps",float(eps),"kappa",float(kappa),flush=True)
```

The numerical search was used to choose frozen rational parameters and a center. The proof is the rational residual/inverse-defect test plus the explicit uniform Hessian bound. This upgrades the supplied approximate witness to an exact existence result. It does not give the frozen entries a natural geometric meaning, identify a canonical physical alphabet, or settle a universal three-species formula.

**Status:** proved-here by the displayed computer-assisted rational certificate; arithmetic interpretation conditional-on H-FROB and H-TWIST; algebraicity conditional-on H-RCF.


### Proposition T4.6 (Jacobian product states and the curve projector)

**Hypotheses:** H-AB-COH, H-CM-POL, H-FROB, the four conjugate-paired eigenvalues, and H-TWIST for the product tensor's norm.

**Statement.** The tensor product of the two elliptic-form bonds with singleton tensors $\operatorname{diag}(1,\pi_j)$ gives
$$\|\Psi_{P_J}(n)\|^2=\prod_{j=1}^2|1-\pi_j^n|^2
=\#J(\mathbb F_{q^n}).$$
Its ket is $V_J=\Lambda^*H^{1,0}$, with dimension $2|2$, and its double is $H^*(J)=\Lambda^*H^1(J)$. There is a Frobenius-invariant graded subspace
$$\mathcal S=\mathbb C1\oplus H^1(J)\oplus\mathbb C\omega,$$
where $\omega$ is a nonzero polarization class in $H^2(J)$ and $F\omega=q\omega$, on which $\operatorname{str}F^n=N_n(C)$. The projector selecting exactly this subspace is not a product $B\otimes\bar B'$ on $V_J\otimes\bar V_J$.

**PROOF.**

<1>1. Exterior multiplication identifies $V_J$ with the tensor product of the two one-mode exterior algebras, and similarly for the bra. The parity-closed ket amplitude is
$$\operatorname{Tr}(P_J(\Lambda^*D)^n)=(1-\pi_1^n)(1-\pi_2^n).$$
Its squared modulus is the stated product. H-AB-COH identifies it with the determinant point count of $J$.

<1>2. Choose symplectically normalized eigenforms $e_1,e_2$ of type $(1,0)$ and $f_1,f_2$ of type $(0,1)$. The polarization line can be represented, up to a nonzero scalar and the conventional factors of $i$, by
$$\omega=e_1\wedge f_1+e_2\wedge f_2.$$
Since $F e_j=\pi_j e_j$ and $F f_j=\bar\pi_j f_j$, both summands have eigenvalue $q$. The restriction to $\mathcal S$ has eigenvalues $1,q$ even and the four Frobenius values odd, hence has supertrace $N_n(C)$.

<1>3. This is a graded Frobenius-module realization of curve cohomology, not a subalgebra identification. The actual map is pullback $i^*:H^2(J)\to H^2(C)$; after integration its value is cup product with $[C]$ in $H^4(J)$. These two maps should not be conflated. For the principal polarization $\theta=[C]$ on a genus-two Jacobian, $\int_J\theta^2=2$, so $i^*\theta=2[\mathrm{pt}]$ under the normalization $\int_C[\mathrm{pt}]=1$. The line, not its unscaled generator, identifies with $H^2(C)$; one may use $\theta/2$ for that normalization.

<1>4. In the doubled exterior basis, the range of the desired projector contains
$$1\otimes1,\quad e_1\otimes1,\quad e_2\otimes1,\quad
1\otimes f_1,\quad1\otimes f_2,$$
as well as the one polarization combination. Thus it has dimension six. If this range were $\operatorname{ran}B\otimes\operatorname{ran}\bar B'$, the first three vectors force the first factor to contain $1,e_1,e_2$, and the corresponding bra vectors force the second factor to contain $1,f_1,f_2$. A product range would have dimension at least nine, a contradiction.

<1>5. A Frobenius-commuting projector $\Pi_\mathcal S$ exists by choosing the polarization line and its invariant complement in the diagonal Hodge basis. Then
$$\operatorname{str}(\Pi_\mathcal S F^n)=N_n(C).$$
Step 4 proves this **particular extraction of curve cohomology** requires a non-product doubled boundary. It does not prove that every other boundary producing the same scalar trace sequence must equal this projector. T4.3 supplies a single ordinary $P$-closed MPS instead, with fermionic species and mixed even eigenvectors, under its field-size hypothesis. T4.5a supplies the requested two-even, one-odd single-ring realization for the particular $\mathbb F_5$ curve. $\square$

**Status:** conditional-on H-AB-COH, H-CM-POL, H-FROB, H-TWIST; the product-tensor and non-product-projector arguments are proved-here.

### Theorem T4.7 (Rosati proves the placewise modulus and supplies the PH metric)

**Hypotheses:** H-CM, H-ROSATI, H-CM-POL; a simple ordinary polarized abelian variety of dimension $g$ (in particular $g=2$). No modulus premise of H-WEIL is needed in the proof.

**Statement.** Rosati acts as complex conjugation in each factor of
$$K\otimes_\mathbb Q\mathbb R\simeq\prod_{j=1}^g\mathbb C.$$
Consequently $|\phi_j(\pi)|^2=q$ at every place, and $q^{-1/2}\widetilde\pi^*$ is unitary on $H^{1,0}$ and on $H^1(\widetilde J,\mathbb C)$ with their Hodge metrics. This proves the ordinary simple instance of the modulus assertion H-WEIL from these positivity inputs.

The equivalent real PH models are $H^1(\widetilde J,\mathbb R)$ and $K\otimes\mathbb R$ with its Rosati trace form, after a module generator and positive metric weights have been chosen. Equivalently one can use the underlying real space of $H^{1,0}\simeq\mathbb C^g$. Their complexification is $H^1(\widetilde J,\mathbb C)$; it is not the uncomplexified $2g$-dimensional real endomorphism space.

**PROOF.**

<1>1. Since $K$ is commutative, Rosati is a real algebra involution on $K\otimes\mathbb R=\mathbb C^g$. Let $e_j$ be a primitive real central idempotent. If Rosati sent it to a different $e_k$, then $\operatorname{Tr}(e_j e_j^\dagger)=0$, contradicting positivity. Thus it preserves each factor.

<1>2. The real algebra automorphisms of $\mathbb C$ are identity and conjugation. If Rosati were identity on a factor, the element $i e_j$ would have $x x^\dagger=-e_j$ and negative regular trace. Positivity excludes this. It is therefore conjugation on each factor, and the trace form is
$$\langle x,y\rangle_R=2\sum_j\Re(x_j\bar y_j).$$
This argument identifies exactly where positivity rules out the wrong involutions.

<1>3. Apply each embedding to $\pi\pi^\dagger=q$. Step 2 gives $\phi_j(\pi)\overline{\phi_j(\pi)}=q$. H-CM-POL identifies Rosati with Hodge adjunction, so the same equation says $(\widetilde\pi^*)^*\widetilde\pi^*=qI$ on the Hodge space. In a Hodge orthonormal eigenbasis it is the elementary diagonal assertion $|\pi_j|^2=q$.

<1>4. By H-CM, $H^1$ has one complex eigenline for each embedding of $K$. Therefore its rational module has rank one over $K$; choosing a generator identifies its real form with $K\otimes\mathbb R$. The compatible positive Hodge form is, on the CM-type half, of the form
$$\sum_j w_j z_j\bar v_j,\qquad w_j>0.$$
The real Rosati form has constant positive weights $2$. Multiplication by positive scalars on each factor identifies the two metrics and commutes with multiplication by $\pi$. Thus these are equivalent representations with positive metrics, not a canonical equality of differently typed vector spaces. The choice of CM type chooses which embedding in each conjugate pair is called holomorphic.

<1>5. The normalized operator has eigenvalues $\pi_j/\sqrt q$ and their conjugates and is unitary. As in T1.6, a self-adjoint logarithm requires phase choices modulo $2\pi$. The PH operator specified intrinsically by this discussion is the unitary Frobenius normalization, with its arithmetic positive metric. $\square$

For the tensor of T4.3, the odd transfer is already $\operatorname{diag}(\bar D,D)$; hence it is $\sqrt q$ times a unitary by construction. RH is made manifest **after** the Frobenius eigenvalues and their moduli have been supplied. The structural arithmetic proof of those moduli is Rosati positivity, not complete positivity of an arbitrary MPS transfer. Total degree in dimension two would only give $|\pi_1|^2|\pi_2|^2=q^2$; it does not supply the two separate equalities. On curves, the corresponding intersection-form positivity is the familiar Hodge-index route on $C\times C$; no separate tensor derivation of that positivity is established here. For the certified tensor in T4.5a, the distinct odd roots imply complex similarity to $\sqrt5$ times a unitary and the exact Ramanujan eigenvalue property. Its polynomial equations do not specify the arithmetic Hodge metric or show that this similarity is induced by an even ket gauge. That missing metric identification is distinct from the now-proved count identity.

**Status:** conditional-on H-CM, H-ROSATI, H-CM-POL; the placewise involution and modulus implication is proved-here. No independent use of H-WEIL in this theorem.

### Proposition T4.8 (gauge and the marking by a CM type)

**Hypotheses:** A graded bond $1|2$ with an identified Hodge space; for the explicit formulas use T4.3.

**Statement.** Even bond gauge is $G=\operatorname{diag}(g_0,H)$ with $g_0\in\mathbb C^\times$, $H\in\mathrm{GL}_2(\mathbb C)$. It acts by
$$a_s\mapsto a_s,\quad B_s\mapsto H B_sH^{-1},\quad
c_f\mapsto g_0c_fH^{-1},\quad d_f\mapsto H d_f g_0^{-1}.$$
It conjugates the full transfer and preserves all ring norms. The CM-type assignment is additional marking, not generally an even gauge freedom. An orthonormal Hodge basis gives the unitary gauge for the cohomological Frobenius operator.

**PROOF.**

<1>1. Multiply the block matrices by $G$ and $G^{-1}$ to obtain the displayed formulas. The transfer and trace assertions follow from T1.7, step 5.

<1>2. For T4.3, $N=0$ and $M=\bar D$. Even gauge conjugates this mixed-sector block by $\bar H$ (the scalar $g_0$ cancels). It cannot change its two eigenvalues. Replacing one selected $\pi_j$ by $\bar\pi_j$, when the selected multisets differ, changes those eigenvalues and is not such a gauge. Replacing the whole CM type exchanges the holomorphic and antiholomorphic assignments; changing only part of the type exchanges the corresponding lines, not necessarily the entire mixed sectors. Coincident spectra require the evident qualification.

<1>3. The canonical ordinary lift has a CM type determined by its arithmetic and the chosen characteristic-zero realization. One should not assume that every abstract CM type is the same lift in another gauge. For a general solution of (4.9) with $N\ne0$, the odd eigenmodes can mix the two coherences. Counts alone do not recover a marked CM-type half from that tensor.

<1>4. Same-parity unitary rotations among physical species leave $\sum A_s\otimes\bar A_s$ exactly unchanged. These are useful additional physical-basis choices, distinct from virtual gauge. Nonunitary virtual gauges transport the Hodge metric and need not preserve Euclidean normality. $\square$

**Status:** proved-here given the indicated Hodge marking; that marking is conditional-on H-CM and H-CM-POL.

## T5. Assessment for the Phantasm

**Observation T5.1 (candidate grading; conjugation is not the full functional equation).**

**Hypotheses for the comparison:** H-ZERO and the finite-curve constructions above.

<1>1. A plausible ket space is $\mathbb C\oplus H_{>0}$, where $H_{>0}$ has one odd mode per positive-height nontrivial zero, with multiplicity. The bra would supply conjugate modes. This is a proposed organization of a spectrum, not a construction of a doubled CP operator. Its $(-,-)$ sector is much larger than the desired pole sector; what kills, cancels, or regularizes those modes remains unspecified. Archimedean/trivial-zero modes require their own bookkeeping.

<1>2. Ket/bra exchange gives complex conjugation. The functional equation also involves $\rho\mapsto1-\rho$. These coincide on individual conjugate pairs only on the critical line. Treating the full functional equation as automatic ket/bra exchange would put RH into the interpretation. An additional duality is needed before that inference is available.

**Status:** open for the candidate bond and required duality; the comparisons are observations.

**Observation T5.2 (when fermionic jumps are necessary).**

**Hypotheses for the comparison:** H-KRAUS-HS and H-ZERO.

<1>1. T3.6 excludes the all-even Kraus class in that analytic setting. Thus a realization retaining those assumptions needs odd jumps. It does not follow that odd jumps suffice, that their number is finite, or that a distributional regularization is an ordinary Hilbert norm. The finite-bond theorem H-TWIST supplies none of these infinite-dimensional assertions.

**Status:** conditional-on H-KRAUS-HS and H-ZERO for the obstruction; existence is open.

**Observation T5.3 (what the toral example actually contributes).**

**Hypotheses for the comparison:** T1.4--T1.5 and T4.6.

<1>1. For an ordinary elliptic curve, lifted Frobenius gives an injective Fourier shift whose only finite cycle is the zero label; the flat Lefschetz supertrace sits in that fibre. The corresponding physical-label state is supported on one configuration. This does not give a general principle that every variety's physical tensor is a permutation: even in this example the shift is not surjective, and for an abelian surface the full torus counts the Jacobian, not the curve. The curve requires the cohomological extraction or a different tensor such as T4.3.

<1>2. No analogous lifted Riemann dynamics, positive Hodge/Rosati metric, or physical-label construction is established. That missing dynamics and positivity, rather than the formal notation for a supertrace, is the substantive break in the analogy.

**Status:** sketched comparison; the proposed Riemann lift is open.

**Observation T5.4 (the locality dichotomy must be restricted).**

**Hypotheses for the comparison:** T0.1--T0.C, T1.3, T4.3, H-ZERO.

<1>1. The literal claim “fixed finite lattice tensors give only supersingular zetas” is false: T1.3 gives ordinary elliptic counts with a fixed two-dimensional bond, and T4.3 gives ordinary genus-two examples with a fixed three-dimensional bond. The equation-local exponential-sum amplitude question is different and remains the restricted conjecture T0.C. Dwork's infinite-dimensional arithmetic transfer is one established framework in the background; no theorem here makes it necessary for every ordinary norm realization or identifies it with a Hilbert-space MPS bond.

<1>2. Infinitely many distinct zeta zeros themselves motivate an infinite spectral space. Dilation time motivates a continuous formulation. Together they make an infinite-bond cMPS a reasonable research target, but neither supplies the missing analytic domains, regularized trace, tensor factorization, or positivity. Those remain concrete conjectural requirements.

**Status:** sketched observation and research suggestion; no new existence theorem is claimed.

## T6. Correction ledger and what is established

### CORRECTION LEDGER

1. **Scope of the exact Weil implementer.** Shard 06b assumes $q$ is an odd prime. T0.1 stays in that scope. T0.2 proves spectral supersingularity over arbitrary finite fields by quadratic sums and finite-valued recurrences, without asserting a characteristic-two genuine symplectic implementer.
2. **Root-of-unity phase.** Roots of unity among the nonzero transfer entries are not the supplied proof of the normalized scalar phase. The Fourier--phase--permutation determinant calculation supplies the missing step. Zero entries and normalization must be kept. The $J=0$ effective scalar is a Gauss sum.
3. **Transfer roots versus Frobenius roots.** H-AS-SUPER only identifies the corrected odd block with Frobenius. H-AS-FILTER is also needed to propagate the transfer's root-of-unity support. The failed uniform minus-sign law is not reused.
4. **Cut rank.** A contiguous ring bipartition cuts two virtual edges: the bound is $D^2$, sharply, not $D$. An arbitrary noncontiguous bipartition uses $D^b$ with its actual number of cut edges.
5. **The binary cubic test.** $x^3=x^{1+2}$ is quadratic over $\mathbb F_2$. The ranks through $n=8$ are basis-dependent finite computations, with maximum $16$ for the stated prescription. They prove neither a uniform asymptotic bound nor unboundedness.
6. **Amplitude-locality conjecture.** Normal bases must be prescribed, trace-invisible coboundaries removed, and quadratic degree interpreted as function degree over the prime field. Necessity remains a conjecture. “Quadratic family” is not equivalent to the entire supersingular class.
7. **Orbit correspondence.** Equality of toral and Frobenius orbit counts gives a noncanonical length-preserving bijection. The zeta identity does not supply a canonical arithmetic matching.
8. **Fourier permutation.** $M^T\mathbb Z^2$ has index $q$; the Fourier shift is injective but not a permutation of $\mathbb Z^2$, and Koopman pullback on functions is an isometry but not a unitary surjection.
9. **Fourier trace and physical tensor.** The Fourier-diagonal Lefschetz trace is flat, not trace class. An operator kernel with two Fourier labels is not itself a finite physical-index tensor. T1.5 gives an explicit infinite-label ket tensor and proves its one-supported state directly, without applying H-TWIST outside finite dimension.
10. **Do not double cohomology twice.** The ket exterior half doubles to full cohomology. Using full cohomology as the ket and then taking a norm produces the wrong squared object.
11. **Bond grading versus physical statistics.** Odd-degree forms explain odd bond/cohomology modes; the elliptic physical letters are all bosonic. Its exact state is a product vector, not a uniform enumeration of rational points.
12. **PH spaces have types and dimensions.** $K\otimes\mathbb R$ is a real space; it is equivalent to real $H^1$, or to the realification of $H^{1,0}$ after choices. Its complexification is complex $H^1$. They are not literally the same unqualified vector space. A Hamiltonian logarithm also requires a phase branch.
13. **What proves Hasse here.** The ordinary inequality follows from the positive degree norm and lifting. An ordinary-only lifting argument is not a proof of the full supersingular portion of H-HASSE. The root-size part of H-FROB is deliberately not assumed in that derivation.
14. **Integral ideal classes are not complex MPS gauge orbits.** H-LM requires full ideal lattices for a nonmaximal order, not just its invertible ideal class group. H-WAT is an arithmetic classification with choices. Complex tensors in T1.3 forget ideal classes. The cohomology matrix is $M^T$ on the dual lattice, and arbitrary $\mathrm{GL}_2(\mathbb C)$ conjugations need not be doubled even ket gauges.
15. **Cyclic digit maps need not be onto.** Both cardinality obstructions and a four-element target represented by only two of five digits occur for $\pi=1+2i$.
16. **Cyclic carries are bounded here.** The exact bound is $C_D/(\sqrt q-1)$. The finite automaton recognizes equal represented words. It does not count all quotient classes once each. The no-ungraded-trace theorem therefore does not imply unbounded cyclic carries.
17. **A signed transfer is not automatically a norm tensor.** A finite graded integer Frobenius matrix provides signed spectral counts; a doubled-Kraus factorization requires its own proof. The elliptic case has such a proof.
18. **The central Hilbert--Schmidt/trace error.** $\operatorname{Tr}\sum A_s\otimes\bar A_s=\sum|\operatorname{Tr}A_s|^2$, not $\sum\|A_s\|_{\rm HS}^2$. The numerical script calculated the latter. The drafted inequality with the two doubled traces is false, with an exact Pauli-diagonal counterexample.
19. **Zero trace does not kill Kraus matrices.** Traceless matrices and nilpotent matrices give counterexamples. The needed nonempty spectral partition in T3.3 follows instead from the all-power word-trace inequality.
20. **The bosonic genus theorem is repaired, not discarded.** The exact inequality $|\operatorname{Tr}M^n|^2\le\operatorname{Tr}S_+^n\operatorname{Tr}S_-^n$, at every $n$, and a Cesàro power-sum argument prove $g\le1$ without cancellation.
21. **Equality is not arbitrary matrix proportionality.** The scalar $1|1$ case forces proportional coefficient vectors. Higher-dimensional nilpotent transients and nonunitary gauges refute the drafted universal proportionality/normality conclusion. The exact general conclusion concerns word-trace vectors.
22. **The minimum bond claim.** $1|g$ is natural when the even ket is stipulated to be a single vacuum line, not generally dimension-minimal. The condition is $mk\ge g$; with exact odd dimension it is $mk=g$. Genus two does have minimum dimension three. Euler bookkeeping is a nonzero spectral statement and subtracts zero multiplicities.
23. **Cancellation is not a demonstrated construction.** Equations (3.7) are the correct modified bounds. They leave larger purely bosonic realizations with cancellation unexcluded; unsuccessful searches do not exclude them. Fermionic species are proved necessary on the minimal genus-two bond, not on every larger one.
24. **Fermionic couplings and trace.** Odd jumps add off-diagonal even blocks with zero length-one trace, but their products affect higher traces. They invalidate the decoupled mixed-block argument; no negative sign is inserted into the Kraus sum.
25. **Infinite-bond constant and domains.** The general bound uses $2\|S_+\|_{\rm HS}\|S_-\|_{\rm HS}$. A bound with ordinary traces requires additional positivity as operators on the Hilbert--Schmidt spaces. H-KRAUS-HS makes the compression argument precise. It is not proved for an arbitrary unbounded cMPS. No-cancellation is unnecessary for the repaired obstruction.
26. **Genus-two cohomological placement.** The double of $\mathbb C\oplus H^{1,0}$ has three excess even dimensions. Spectra do not locate these modes canonically. A pure polarization trace-line $q$-eigenvector or an invariant vacuum $1$-line would eliminate a needed jump direction and contradict the bosonic no-go. The surviving even eigenvectors must mix in this minimal setting.
27. **The suggested vacuum ansatz is impossible.** It makes $M=0$; one odd letter gives rank at most two in the four-dimensional odd sector. More odd letters with $M=0$ still force spectral symmetry under negation and zero trace.
28. **The universal three-letter theorem is not proved; the particular example is.** T4.5a proves exact existence over $\mathbb F_5$ by a rational contraction certificate, with entries specified as a unique algebraic root. Rounded output and tiny least-squares residuals alone are not certificates. A general formula or natural geometric selection remains Conjecture T4.C and its additional selection problem. Failed smaller-species searches prove no lower bound on species count.
29. **What the closed-form theorem actually covers.** T4.3 is explicit with five even and four odd letters under $q+1\ge4\sqrt q$, hence for prime powers $q\ge16$. It includes the given ordinary simple curve over $\mathbb F_{25}$. T4.5a separately certifies three letters over $\mathbb F_5$. Neither settles all fields or optimal species number.
30. **Algebraic entries.** Under H-RCF, existence of a finite species solution to the real polynomial equations implies existence with algebraic entries. Nonexistence of an attractive closed form does not imply nonexistence over an algebraic extension. T4.3 supplies exact algebraic entries directly.
31. **Curve versus Jacobian cohomology.** The Jacobian product tensor counts $J$, not $C$. The polarization-selected six-dimensional subspace is a graded Frobenius module, not generally a subalgebra. The actual map to $H^2(C)$ is restriction; integration identifies it with cupping $[C]$ in $H^4(J)$. The principal class restricts to $2[\mathrm{pt}]$, so its generator requires normalization.
32. **Boundary nonfactorization has a stated scope.** The rank-six curve-cohomology projector is not $B\otimes\bar B'$, by the product-range argument. This is not a theorem that every alternative scalar-count boundary must be that projector. Available single-ring replacements have four odd letters in the general large-field formula and one odd letter in the certified $\mathbb F_5$ example.
33. **Genus-two PH positivity.** Positive Rosati forces complex conjugation at each CM place and proves the root sizes. Hodge/endomorphism metric equivalences require realification or complexification and positive weights. In the constructed tensor the diagonal odd roots are inputs; CP alone is not a new proof of RH.
34. **CM type and gauge.** A CM type is arithmetic/Hodge marking. Changing a selected half is not in general an even ket gauge; partial changes exchange selected lines rather than always the whole mixed sectors. A general coupled tensor need not recover a CM-type half from its counts.
35. **Functional equation versus conjugation.** Bra conjugation alone does not implement $\rho\mapsto1-\rho$ off the critical line. Identifying them prematurely assumes the conclusion sought.
36. **No broad supersingular-versus-finite-tensor dichotomy.** Finite ordinary norm tensors are explicit here. Only the much narrower equation-amplitude locality conjecture survives. Infinite Riemann spectral data motivate, but do not construct or prove necessity of, a particular cMPS architecture.

### Hypotheses used and dependencies

All H-labels introduced in this file are listed here; their exact statements are in the T0 register.

| Hypothesis | Role and status in this notebook |
|---|---|
| H-WEIL | Supplied general modulus theorem; used as an input for general curve spectral applications. Ordinary elliptic and simple ordinary CM modulus implications are independently derived from stronger geometric positivity inputs. |
| H-HASSE | Supplied elliptic theorem; ordinary bound derived in T1.6 without assuming that bound. |
| H-DEURING | External ordinary elliptic lifting input. |
| H-DEG | External good-reduction degree input; positivity/metric consequences proved in T1.1 and T1.6. |
| H-LEF | External Lefschetz fixed-point theorem. |
| H-LENSTRA | External $O$-module point-group identification; unnecessary for the cardinality determinant itself. |
| H-LM | External integral matrix/ideal-lattice classification, with noninvertible lattices included. |
| H-WAT | External ordinary finite-field elliptic classification, distinguished from complex gauge. |
| H-CM | External ordinary simple CM-lift and eigenspace decomposition. |
| H-ROSATI | External positive involution and $\pi\pi^\dagger=q$; placewise conjugation and modulus derived in T4.7. |
| H-LIDSKII | External spectral trace theorem, used for the trace-class no-ungraded extension. |
| H-SCHUR | Finite matrix inequality and equality criterion proved in T3.1; needed compact HS extension proved in T3.6. |
| H-CS | Elementary Hilbert-space inequality used in the finite and compressed Gram arguments. |
| H-TWIST | Supplied finite-bond physical norm/supertrace identification; not promoted to infinite dimension. |
| H-FROB | Non-RH cohomological count and elliptic characteristic-polynomial input, separated from root sizes. |
| H-AS-WEIL | Supplied exact odd-prime implementer and Fourier factorization from shard 06b. |
| H-AS-SUPER | Supplied identification of the corrected odd multiset with Frobenius. |
| H-AS-FILTER | Supplied roots-of-unity support/multiplicity filter from shard 06b. |
| H-SS-NP | External equivalence of spectral and Newton supersingularity. |
| H-AB-COH | External exterior-algebra cohomology and determinant point count for abelian varieties. |
| H-CM-POL | External polarized-lift/Hodge adjunction, Jacobian restriction, and principal-polarization intersection normalization. |
| H-AV-FUNCTOR | External Frobenius-polynomial functoriality and normalized Newton-slope criterion; used for the arithmetic nature of the examples. |
| H-RCF | External real closed field transfer; used for conditional algebraic existence and algebraicity of the unique certified root. The real existence certificate itself does not require it. |
| H-ZERO | Supplied standard zero count, strip, and symmetries, without RH. |
| H-KRAUS-HS | Explicit added analytic hypothesis for the infinite-bond obstruction; not established for a Riemann cMPS. |

The compact torus exterior-cohomology and finite-index determinant calculations were supplied with elementary proofs in T1; quadratic Gauss-sum reduction and the finite-valued recurrence argument were supplied in T0.2. No additional unlisted conjectural arithmetic lift or “tensor positivity implies RH” principle is used.

### What is established

- **Proved-here:** T0.3--T0.4 (finite cut statements and exact finite computation); the algebraic tensor calculations in T1.3 and T1.5; T2.1 and the finite part of T2.2; T3.1--T3.5 under their explicit spectral hypotheses; T4.1--T4.2, the explicit construction T4.3 under its stated modulus/field-size hypotheses, the polynomial and tensor calculations in T4.4, the feasibility equivalence T4.5, the exact rational existence certificate and all-power trace identity T4.5a, the non-product range argument in T4.6, and the gauge calculations in T1.7/T4.8.
- **Conditional-on the listed standard inputs:** T0.1--T0.2 as arithmetic supersingularity assertions; T1.1--T1.7 as assertions about ordinary elliptic curves and their PH model; the trace-class part of T2.2; the curve application of T3.3 and the analytic no-go T3.6; the arithmetic interpretations of T4.3--T4.4, the algebraic-point implication T4.5, the arithmetic norm interpretation and algebraicity conclusion of T4.5a, the cohomological Jacobian comparison T4.6, and the Rosati/Hodge theorem T4.7. These have full implication proofs; “conditional” is not being used to disguise a gap in an algebraic calculation.
- **Sketched:** only the broader Phantasm architecture and the background analogy to Dwork/Hodge-index approaches in the assessment; no new mathematical existence claim rests on those sketches.
- **Open:** T0.C, asymptotic ranks for the chosen normal bases, the universal three-species conjecture T4.C, natural geometric selection of its tensors, general small-field genus-two existence beyond the certified example and species optimality, purely bosonic genus-two realizations with extra cancelling spectrum, and a Riemann lifted dynamics/positive metric/infinite-bond norm construction satisfying the needed analytic assumptions.

**RESULT:** Tier A is an exact finite graded MPS theorem conditional on the explicitly named lifting, degree, and Frobenius inputs, with PH unitarity derived from positivity. The no-cancellation bosonic genus bound is proved by all-power traces, replacing the false Hilbert--Schmidt/trace argument. Tier B has a certified exact two-even, one-odd $1|2$ tensor for the supplied ordinary simple curve over $\mathbb F_5$, and an explicit algebraic nine-species formula for all $q\ge16$. Both give all ring norms and the correct ring zeta; the particular certificate does not provide a natural equation-based formula, and the universal three-species theorem remains open. The Riemann conclusions remain conditional obstructions and conjectural architecture.
