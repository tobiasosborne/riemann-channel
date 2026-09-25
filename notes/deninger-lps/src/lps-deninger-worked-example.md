**An explicit LPS square complex and its graded Bass model**

Parameters: horizontal prime 13, transverse prime 17, congruence modulus 5.

The quaternionic faces are constructed, rather than chosen by an arbitrary
embedding. The resulting finite complex has 120 vertices, 840 horizontal edges,
1,080 vertical edges, and 7,560 squares. The construction below produces an
exactly verified odd spectral space, a determinant with its spectrum in the
numerator, a graded orbit formula, a positive pairing, and a self-adjoint
continuous-time suspension.

There are two precise scope distinctions. First, the relevant cohomology is
horizontal (a finite analogue of leafwise cohomology), not total cohomology.
Second, the quadratic Bass construction doubles that horizontal space. The
finite model has a rational zeta function of one variable and commensurate
periods. It does not construct the Riemann zeta function or its prime periods.

All counts and polynomial certificates below were computed from the explicit
integer data. The scripts and all cells accompany this note.

**1. Vertices and quaternion generators.**

Use quaternions with

\[
i^2=j^2=k^2=ijk=-1,
\qquad N(a_0+a_1i+a_2j+a_3k)=\sum_{r=0}^3a_r^2.
\]

For \(p\in\{13,17\}\), set

\[
S_p=\{a_0+a_1i+a_2j+a_3k:N(a)=p,\ a_0>0\text{ odd},\ a_1,a_2,a_3\text{ even}\}.
\]

Every sign in the following descriptions is independent:

\[
S_{13}=\{3\pm2i,3\pm2j,3\pm2k\}
\ \cup\ \{1\pm2i\pm2j\pm2k\},
\]

\[
\begin{split}
S_{17}={}&\{1\pm4i,1\pm4j,1\pm4k\}\\
&\cup\{3\pm2i\pm2j,\ 3\pm2i\pm2k,\ 3\pm2j\pm2k\}.
\end{split}
\]

Thus \(|S_{13}|=14\), \(|S_{17}|=18\). Quaternion conjugation supplies the
inverse projective generator in each set.

The vertex set is

\[
V=\operatorname{PGL}_2(\mathbb F_5)
=\{M\in M_2(\mathbb F_5):\det M\ne0\}/\mathbb F_5^\times.
\]

Its size is \((25-1)(25-5)/4=120\). A unique representative is obtained by
scaling the first nonzero entry, read row by row, to 1. Order those four-entry
tuples lexicographically; this completely specifies the vertex labels.

Since \(2^2=-1\pmod5\), reduce a quaternion by

\[
\phi(a)=
\left[\begin{pmatrix}
a_0+2a_1&a_2+2a_3\\
-a_2+2a_3&a_0-2a_1
\end{pmatrix}\right].
\]

This respects multiplication projectively and has determinant \(N(a)\bmod5\).
All generators are invertible. The script checks that each color has distinct
generators, no loops, and no repeated edges within that color.

**2. Every edge.**

A horizontal directed edge is \((g,a):g\to g\phi(a)\), with \(a\in S_{13}\).
A vertical directed edge is \((g,b):g\to g\phi(b)\), with \(b\in S_{17}\).
Identify

\[
(g,a)^{-1}=(g\phi(a),\bar a),
\]

and similarly vertically. The numbers of undirected edges are

\[
E_h=120\cdot14/2=840,\qquad E_v=120\cdot18/2=1080.
\]

The colors are retained even if they connect the same vertex pair. Consequently
the combined graph is a colored multigraph. The individual color graphs are
the simple LPS graphs \(X^{13,5}\) and \(X^{17,5}\).

All eigenvalue multiplicities are certified by integer characteristic
polynomials:

| Adjacency | Eigenvalues and multiplicities |
|---|---|
| \(A_{13}\) | \(\pm14\) each 1; \(\pm4\) each 34; \(\pm2\) each 25 |
| \(A_{17}\) | \(\pm18\) each 1; \(\pm6\) each 10; \(\pm5\) each 12; \(\pm3\) each 4; \(\pm2\) each 15; \(0\) multiplicity 36 |
| \(A_{13}+A_{17}\) | \(\pm32\) each 1; \(\pm9\) each 12; \(\pm7\) each 4; \(\pm4\) each 28; \(0\) multiplicity 30 |

The three graphs are connected and bipartite. The nontrivial spectral bounds
are respectively \(4<2\sqrt{13}\), \(6<2\sqrt{17}\), and
\(9<2\sqrt{31}\). Thus even the combined 32-regular multigraph is Ramanujan
in the adjacency sense. Bipartiteness is the determinant square-class character
of \(\operatorname{PGL}_2(\mathbb F_5)\): both 13 and 17 reduce to nonsquares.

**3. Every face, from a finite reordering table.**

For each \((a,b)\in S_{13}\times S_{17}\), there is a unique
\((b',a')\in S_{17}\times S_{13}\) such that

\[
ab=\pm b'a'.
\]

For these particular sets this is verified exhaustively in exact integer
arithmetic: form the 252 products \(b'a'\), normalize their central sign, and
check that they are distinct and give exactly the 252 normalized products
\(ab\). No general factorization theorem is required to certify this example.

The square based at \(g\) has boundary

\[
\partial_2[g;a,b]
=e_h(g,a)+e_v(g\phi(a),b)
-e_h(g\phi(b'),a')-e_v(g,b').
\]

The endpoint identity follows from the quaternion identity. The four corners
are

\[
g,\quad g\phi(a),\quad g\phi(a)\phi(b)=g\phi(b')\phi(a'),\quad g\phi(b').
\]

The four descriptions obtained from the four corners describe one unoriented
square. The program verifies that every face has exactly four such
representatives. Thus

\[
F=120\cdot14\cdot18/4=7560.
\]

The link at every vertex has one corner for each horizontal/vertical edge pair,
so is \(K_{14,18}\). This is the local product-of-trees square structure, not
a surface mesh: an edge has more than two incident faces.

For an explicit noncommuting square, take

\[
\begin{array}{ll}
a=1-2i-2j-2k,&b=1-4i,\\
b'=1+4j,&a'=1+2i+2j-2k.
\end{array}
\]

Both products are exactly \(-7-6i+6j-10k\). At the identity vertex the four
corners, as normalized matrices modulo 5, are

\[
I,\quad
\begin{pmatrix}1&2\\4&0\end{pmatrix},\quad
\begin{pmatrix}1&1\\4&0\end{pmatrix},\quad
\begin{pmatrix}1&4\\1&1\end{pmatrix}.
\]

`faces.csv` lists every face as four signed edge numbers. `square_rules.csv`
lists every one of the 252 integer quaternion reordering rules. These two files
are also an unambiguous specification of all attaching maps.

**4. The full graded complex, and why we retain only horizontal derivatives.**

Let \(B_1\) and \(B_2\) be the chain boundary matrices, with sizes

\[
B_1:120\times1920,\qquad B_2:1920\times7560.
\]

Each edge column of \(B_1\) has \(-1\) at its tail and \(+1\) at its head.
Each face column of \(B_2\) is the signed boundary just specified. The exact
identity \(B_1B_2=0\) is verified. The total cochain complex is

\[
\mathbb R^{120}\xrightarrow{B_1^t}\mathbb R^{1920}
\xrightarrow{B_2^t}\mathbb R^{7560}.
\]

Its rational Betti numbers are

\[
(b_0,b_1,b_2)=(1,0,5759).
\]

Certificate: connectedness gives \(\operatorname{rank}B_1=119\).
Elimination modulo 101 gives \(\operatorname{rank}_{\mathbb F_{101}}B_2=1801\).
Hence its rational rank is at least 1801. The identity \(B_1B_2=0\) gives the
opposite inequality \(\operatorname{rank}_{\mathbb Q}B_2\le1920-119=1801\).
This proves the stated Betti numbers, rather than merely suggesting them
numerically.

Deninger's leafwise analogy requires keeping the evolution direction separate.
Here differentiate only horizontally:

\[
D:\mathbb R^{120}\to\mathbb R^{840},\qquad
(Df)(g,a)=f(g\phi(a))-f(g).
\]

Then

\[
H_h^0=\ker D=\mathbb R,\qquad
H_h^1=\mathbb R^{840}/\operatorname{im}D\cong K:=\ker D^t,
\]

and \(\dim K=840-119=721\). The last isomorphism uses the ordinary positive
edge inner product and selects the representative orthogonal to gradients.
No horizontal faces are present: each actual square has one horizontal and one
transverse direction. The full face differential is not imposed on \(K\).

Thus the vanishing of total \(H^1\) does not eliminate the relevant odd space.
It is a reason to distinguish total and partial cohomology carefully.

**5. The squares supply transverse transport, not just topology.**

Define \(T_0=A_{17}\) on vertex functions. On antisymmetric horizontal edge
fields define

\[
(T_1\omega)(g,a)=\sum_{b\in S_{17}}\omega(g\phi(b'),a'),
\qquad ab=\pm b'a'.
\]

This compares a horizontal edge with its opposite edge in every incident
square, with the orientation signs retained. It is independent of choosing a
representative of an unoriented edge and is symmetric for the usual edge inner
product. Both statements are verified as integer matrix identities.

For a vertex function,

\[
\begin{split}
(T_1Df)(g,a)
&=\sum_b[f(g\phi(b')\phi(a'))-f(g\phi(b'))]\\
&=\sum_bf(g\phi(a)\phi(b))-\sum_{b'}f(g\phi(b'))\\
&=(DT_0f)(g,a).
\end{split}
\]

The reordering map uses every \(b'\) once, as checked by the table. Therefore

\[
T_1D=DT_0,\qquad T_1^t=T_1.
\]

Taking adjoints proves that \(K=\ker D^t\) is invariant. Write
\(T=T_1|_K\). It is self-adjoint. The induced action on \(H_h^0\) is 18.

This is a concrete use of the faces that cannot be supplied by assigning parity
labels to an arbitrary adjacency matrix.

**6. A fully explicit basis and exact spectral certificate.**

Use the identity vertex as root, choose the breadth-first spanning tree with
neighbors ordered by vertex label, and order the 721 remaining horizontal
edges by edge label. For each such chord take the cycle consisting of that edge
followed by the tree path back to its tail. Let \(Z\) be the resulting
\(840\times721\) integer matrix of signed cycles.

It satisfies \(D^tZ=0\), and its rows at chord positions form the identity.
Thus it is a basis of \(K\). Put

\[
M=Z^tZ,\qquad L=(T_1Z)_{\text{chord rows}}.
\]

Then, exactly,

\[
T_1Z=ZL,\qquad L^tM=ML,\qquad M>0.
\]

All of \(Z,M,L\) are provided in Matrix Market format. This specifies the
operator in an actual basis, not only through its eigenvalues.

Since \(D\) identifies mean-zero vertex functions with gradients, the
characteristic polynomial is

\[
\chi_T(x)=\frac{\chi_{T_1}(x)(x-18)}{\chi_{A_{17}}(x)}.
\]

The script computes both sides independently with exact integer matrices,
including \(\chi_L\), and verifies equality. The complete factorization of
\(\chi_T\) is appended below. Rational Sturm counts verify that every root of
every factor lies strictly in \((-8,8)\). Therefore

\[
\boxed{\|T\|<8<2\sqrt{17}.}
\]

This certifies the relevant Ramanujan bound on the odd space itself, rather than
assuming the vertex Ramanujan bound automatically survives passage to edges.

**7. Bass doubling and the even/odd spaces.**

Define the degree-two Bass pencil

\[
Q_u(A)=I-uA+17u^2I.
\]

The inverse superdeterminant on the horizontal complex is

\[
\mathcal Z(u)=\frac{\det Q_u(T_1)}{\det Q_u(T_0)}.
\]

Cancellation of gradients gives

\[
\boxed{\mathcal Z(u)=
\frac{\det_K(I-uT+17u^2I)}{(1-u)(1-17u)}.}
\]

To make it a first-order evolution define

\[
\mathcal H^0=\mathbb R,\qquad
\mathcal H^1=K\oplus K,\qquad
\mathcal H^2=\mathbb R,
\]

and

\[
F_0=1,\qquad
F_1=\begin{pmatrix}T&-17I\\I&0\end{pmatrix},\qquad F_2=17.
\]

Then \(\dim\mathcal H^1=1442\) and

\[
\mathcal Z(u)=\frac{\det(I-uF_1)}{\det(I-uF_0)\det(I-uF_2)}.
\]

This linearization is itself compatible with the differential: take
\(\widetilde D=\operatorname{diag}(D,D)\) and the same companion construction
on both \(C_h^0\oplus C_h^0\) and \(C_h^1\oplus C_h^1\).
It commutes with \(\widetilde D\). Its two-dimensional even cohomology has
eigenvalues 1 and 17; those eigenlines are labeled degrees 0 and 2. The labels
express their spectral weights. They are not an assertion that total
\(H^2\) of the square complex is one-dimensional.

Writing \(\chi_T(x)=\prod_f f(x)^{m_f}\), the numerator is explicitly

\[
P(u)=\prod_f\big[u^{\deg f}f(u^{-1}+17u)\big]^{m_f}.
\]

It has degree 1442, constant term 1, and leading coefficient \(17^{721}\).
This factor formula avoids printing thousands of large integer coefficients.

**8. The complete graded Euler product, including its correction.**

Let \(G_v\) be the 18-regular vertical graph on 120 vertices. Let \(G_e\)
have the 840 unoriented horizontal edges as its vertices. Each square becomes
an edge of \(G_e\) joining its two opposite horizontal edges. Its sign is +1
when the transport preserves the chosen orientations and -1 otherwise. Thus
\(G_e\) is an 18-regular signed multigraph with 7,560 edges and signed
adjacency \(T_1\). The script independently reconstructs \(T_1\) this way.

For a primitive reduced closed walk \(c\) of \(G_e\), let \(\epsilon(c)\)
be the product of its edge signs. Define

\[
Z_v(u)=\prod_{c\text{ primitive in }G_v}(1-u^{\ell(c)})^{-1},
\]

\[
Z_e(u)=\prod_{c\text{ primitive in }G_e}
(1-\epsilon(c)u^{\ell(c)})^{-1}.
\]

Walks are cyclically identified, immediate reversals and tails are excluded,
and reverse orientations are distinct, as in Ihara zeta.

The signed Bass identity is the ordinary edge-reversal determinant elimination
with reciprocal edge weights \(\pm1\). It gives

\[
Z_v(u)^{-1}=(1-u^2)^{1080-120}\det Q_u(T_0),
\]

\[
Z_e(u)^{-1}=(1-u^2)^{7560-840}\det Q_u(T_1).
\]

Consequently the exact orbit formula for our function is

\[
\boxed{\mathcal Z(u)=(1-u^2)^{-5760}\frac{Z_v(u)}{Z_e(u)}.}
\]

The 5760 is \(\chi(X)=120-1920+7560\). This correction must not be dropped:
the raw graded non-backtracking zeta \(Z_v/Z_e\) has an extra factor
\((1-u^2)^{5760}\). Dividing out that explicit factor is part of the
definition of the completed finite model.

Equivalently, with \(B_v,B_e\) the (signed) non-backtracking operators,

\[
N_n:=1+17^n-\operatorname{Tr}F_1^n
=\operatorname{Tr}B_v^n-\operatorname{Tr}B_e^n
+5760(1+(-1)^n),
\]

and

\[
\mathcal Z(u)=\exp\sum_{n\ge1}\frac{N_n}{n}u^n.
\]

This is an explicit graded Euler product. The minus sign of the odd space is
present for every repetition; the additional \(\epsilon(c)^r\) describes
orientation transport around repeated walks. Those two signs are distinct.

The first coefficients are

| \(n\) | \(N_n\) | Formal primitive exponent \(b_n=\frac1n\sum_{d\mid n}\mu(d)N_{n/d}\) |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 11520 | 5760 |
| 3 | 10080 | 3360 |
| 4 | 126720 | 28800 |
| 5 | 1209600 | 241920 |
| 6 | 23886720 | 3977520 |

The first 30 are supplied. Their observed positivity is not used to assert an
unsigned geometric orbit model; the proven local interpretation is the
displayed signed/graded product.

**9. The positive pairing and the critical circle.**

On \(K\oplus K\), in orthonormal edge-field coordinates, put

\[
\Omega=\begin{pmatrix}0&I\\-I&0\end{pmatrix},\qquad
G=\begin{pmatrix}I&-T/2\\-T/2&17I\end{pmatrix}.
\]

Direct block multiplication gives

\[
F_1^t\Omega F_1=17\Omega,\qquad F_1^tG F_1=17G.
\]

The Schur complement of the upper-left block of \(G\) is

\[
17I-T^2/4>I,
\]

using the certified strict bound \(\|T\|<8\). Hence \(G>0\), and
\(U=F_1/\sqrt{17}\) is orthogonal in this metric.

In the exported integral cycle coordinates the same forms are

\[
\Omega_M=\begin{pmatrix}0&M\\-M&0\end{pmatrix},\qquad
G_M=\begin{pmatrix}M&-ML/2\\-ML/2&17M\end{pmatrix}.
\]

Thus all entries of the positive form are explicitly rational; \(2G_M\) is
integer. The evolution is \(\begin{pmatrix}L&-17I\\I&0\end{pmatrix}\).

For an explicit compatible quarter-turn, let

\[
R=(17I-T^2/4)^{1/2},\quad
\mathsf J=\begin{pmatrix}T/2&-17I\\I&-T/2\end{pmatrix}
\operatorname{diag}(R^{-1},R^{-1}).
\]

Then \(\mathsf J^2=-I\), \(\mathsf JF_1=F_1\mathsf J\), and
\(\Omega\mathsf J=G\operatorname{diag}(R^{-1},R^{-1})>0\).
This realizes the pairing-plus-star algebra directly.

If \(\lambda\) is an eigenvalue of \(T\), the corresponding eigenvalues of
\(F_1\) are

\[
\alpha_\pm=\frac{\lambda\pm i\sqrt{68-\lambda^2}}2
=\sqrt{17}e^{\pm i\theta},\qquad
\theta=\arccos\frac{\lambda}{2\sqrt{17}}\in(0,\pi).
\]

Therefore every numerator zero has \(|u|=17^{-1/2}\). With \(u=17^{-s}\),
all numerator zeros lie on \(\Re s=1/2\). The even poles are on
\(\Re s=0,1\). There is no cancellation between these loci.

The reciprocal functional equation is also exact:

\[
\mathcal Z(1/(17u))=17^{-720}u^{-1440}\mathcal Z(u).
\]

Equivalently \(17^{720s}\mathcal Z(17^{-s})\) is invariant under
\(s\mapsto1-s\).

The logical role of the positivity step is explicit: for this companion matrix,
positivity of \(G\) is equivalent to the strict Ramanujan inequality on \(T\).
It is established here by the exact finite spectral certificate. It is not a
new route proving Ramanujan bounds without input.

**10. Continuous time, the Hamiltonian and the regularized determinant.**

Set \(\ell_0=\log17\). A finite logarithm of the discrete evolution is

\[
\Theta_{\mathrm{fin}}=\tfrac12I+
\frac1{\ell_0}\operatorname{diag}(\theta(T),\theta(T))\mathsf J,
\qquad \theta(T)=\arccos(T/(2\sqrt{17})),
\]

so \(e^{\ell_0\Theta_{\mathrm{fin}}}=F_1\). Its centered generator is
skew-adjoint in the positive metric. A finite logarithm only selects one
representative from each vertical arithmetic progression of zeros.

To recover every zero, use a suspension. Complexify \(K\oplus K\), use the
positive \(G\)-inner product, and set

\[
\mathscr H=L^2([0,\ell_0],K_{\mathbb C}\oplus K_{\mathbb C};G).
\]

Define

\[
H=-i\frac{d}{dx},\qquad
\operatorname{Dom}H=\{\psi\in H^1([0,\ell_0]):\psi(\ell_0)=U\psi(0)\}.
\]

Because \(U\) is unitary in the same positive metric, this boundary condition
makes \(H\) self-adjoint. One can verify it either by integration by parts and
the maximal boundary condition, or by diagonalizing the finite unitary \(U\)
and obtaining a direct sum of scalar twisted periodic derivative operators.
Its eigenvalues are exactly

\[
E_{\lambda,\pm,k}=\frac{\pm\theta(\lambda)+2\pi k}{\log17},\qquad k\in\mathbb Z.
\]

Thus \(\Theta_1=1/2+iH\) has the complete numerator zero spectrum.
The even suspension generators are \(\Theta_0=d/dx\) and
\(\Theta_2=1+d/dx\), each on a scalar periodic circle of length \(\ell_0\).
They reproduce the full vertical progressions of even poles.

For completeness the scalar regularized determinant can be fixed without an
unspecified zero-free factor. For the spectral progression
\(\mu+2\pi ik/\ell_0\), use the principal logarithm of
\(s-\mu-2\pi ik/\ell_0\), initially \(\Re(s-\mu)>0\), and define the
determinant by spectral zeta continuation. Write
\(\omega=2\pi/\ell_0\), \(a=(s-\mu)/(i\omega)\). Splitting the progression
into the two half-lines gives

\[
\eta(w)=(i\omega)^{-w}\zeta_H(w,a)
+(-i\omega)^{-w}\zeta_H(w,1-a).
\]

Here \(\zeta_H(w,a)=\sum_{n\ge0}(n+a)^{-w}\), continued analytically.
Its identities
\(\zeta_H(0,a)=1/2-a\),
\(\zeta'_H(0,a)=\log\Gamma(a)-\tfrac12\log(2\pi)\), together with the
Gamma reflection identity, give

\[
\det_{\rm reg}(s-\Theta_\mu)=1-e^{-\ell_0(s-\mu)}.
\]

Also \(\eta(0)=0\), so dividing the operator by \(2\pi\) does not change
this determinant. Applying it to every finite eigenvalue block gives exactly

\[
\mathcal Z(17^{-s})=
\frac{\det_{\rm reg}((s-\Theta_1)/(2\pi))}
{\det_{\rm reg}((s-\Theta_0)/(2\pi))\det_{\rm reg}((s-\Theta_2)/(2\pi))}.
\]

No free normalization factor remains with this prescription. The equalities
are first obtained in a right half-plane and then continued.

The corresponding positive-time trace formula is

\[
\operatorname{Str}(e^{t\Theta})=
\ell_0\sum_{n\ge1}N_n\delta(t-n\ell_0),\qquad t>0,
\]

as a distribution. It follows from the Fourier comb for each suspended
eigenvalue progression. Combining it with the graded orbit formula in part 8
expresses the same distribution in terms of primitive non-backtracking walks,
their orientation signs, and the explicit correction term.

**11. What this realizes, and what remains different from arithmetic.**

| Requirement | Realization in this example |
|---|---|
| Explicit expanding graph | Both LPS color graphs, and their combined colored multigraph |
| Faces derived from arithmetic relations | All 252 quaternionic rules and 7,560 square cells |
| Differential and cancellation | Exact horizontal differential and chain-compatible transport |
| Odd spectrum | The Bass doubling of the 721-dimensional horizontal cohomology |
| Even poles | The two eigenlines 1 and 17 in doubled horizontal degree zero |
| Euler product | Explicit signed/graded Ihara quotient with its required correction |
| Functional equation | Reciprocal polynomial identity |
| Positive pairing | Explicit rational metric, positivity certified by exact spectral bounds |
| Compatible star | The displayed \(\mathsf J\) |
| Self-adjoint Hamiltonian | Twisted periodic derivative on an explicitly specified Hilbert space |
| Regularized determinant and trace formula | Exact formulas in part 10 |

This finite construction uses horizontal cohomology, then a quadratic Bass
linearization and a normalization of the graded orbit product. It does not
identify that construction with ordinary total cohomology of the square
complex. Nor is the quarter-turn an initially given rotation of local surface
edges: it is constructed by functional calculus from the certified transverse
operator.

After suspension all periods are integer multiples of \(\log17\); the
Riemann prime periods \(\log p\) are not. The finite model has linearly growing
zero count in height, not the Riemann \(T\log T\) law. Both even suspension
spaces are infinite-dimensional and generate repeated poles, whereas the
completed Riemann zeta target has only the two poles at 0 and 1. There is no
Riemann archimedean gamma contribution in this example.

Thus the actual accomplishment is a concrete realization of the finite graded
trace/determinant/positivity mechanism, with every edge and face specified.
Passing from it to Deninger's arithmetic target still requires independently
constructing the arithmetic periods, spaces, trace formula and positive
compatible pairing in one system.

The distinction also addresses whether unification merely restates a spectral
bound: the square transport and chain cancellation are additional structural
information, while positivity of the companion metric is precisely the
Ramanujan constraint expressed in another form.

**12. Sources and computational provenance.**

The LPS quaternionic construction originates in
[Lubotzky, Phillips and Sarnak, *Ramanujan graphs* (1988)](https://doi.org/10.1007/BF02126799).
The product-of-trees generalization, partial cohomology and Ramanujan bounds on
cell spaces are developed by
[Jordan and Livne, *The Ramanujan property for regular cubical complexes*](https://arxiv.org/abs/math/9907214).
Quaternionic square relations and their edge permutations are also treated in
[Rattaggi, *Anti-tori in square complex groups*](https://arxiv.org/abs/math/0411547).
The determinant/positivity target is described in
[Deninger, *The Hilbert–Polya strategy and height pairings*](https://arxiv.org/abs/1001.1621),
and the dynamical interpretation in
[Deninger, *Number theory and dynamical systems on foliated spaces*](https://arxiv.org/abs/math/0204110).

The particular level-5 calculations, basis choices, exported face list,
polynomial factorizations, graded quotient and verifications in this note were
worked out directly here. The references supply context, not numerical
certificates for the reported matrices. No claim of novelty is made.

The verifier generates all data from the quaternion sets. Its exact checks
include boundary-square zero, commuting vertex adjacencies, symmetry and
chain compatibility of transport, the integral horizontal cycle basis,
independent characteristic polynomials, the rational root bound, and the
maximum-rank face boundary certificate modulo 101. The Hamiltonian and pairing
identities follow from the displayed block algebra and the certified bound.

**13. Complete characteristic factorization on the 721-dimensional odd precursor.**

The following table specifies \(\chi_T(x)=\prod f(x)^m\) exactly. The sum of
\(m\deg f\) is 721. Every factor has all of its roots in \((-8,8)\), verified
by rational Sturm counts.

| Factor \(f(x)\) | Multiplicity \(m\) |
|---|---:|
| \(x-7\) | 4 |
| \(x+7\) | 4 |
| \(x^3-4x^2-43x+188\) | 6 |
| \(x+1\) | 8 |
| \(x^2+3x-6\) | 8 |
| \(x+3\) | 6 |
| \(x^3-2x^2-36x-24\) | 10 |
| \(x^2+x-18\) | 12 |
| \(x^2+2x-39\) | 12 |
| \(x^3-10x^2+20x+8\) | 12 |
| \(x^4-3x^3-31x^2+103x+2\) | 12 |
| \(x^2+4x-20\) | 15 |
| \(x^2-12\) | 15 |
| \(x^2-8x+4\) | 15 |
| \(x^2-4x-4\) | 15 |
| \(x-4\) | 18 |
| \(x^2+x-38\) | 18 |
| \(x^3+6x^2-4x-40\) | 18 |
| \(x^5+6x^4-15x^3-58x^2+140x-72\) | 18 |
| \(x+5\) | 12 |
| \(x-6\) | 15 |
| \(x+6\) | 17 |
| \(x-2\) | 20 |
| \(x-3\) | 44 |
| \(x+2\) | 77 |
