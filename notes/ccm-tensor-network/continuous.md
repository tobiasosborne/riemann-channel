# Continuous CCM as a transfer-insertion quotient

Author lane: continuous; 2026-09-18. This is the author draft; the integrated
scopes were independently adjudicated in `notes/reviews/ccm-tensor-continuous-r1.md`.
Current statuses are in `db/claims.tsv`; the optional C9 limit remains SKETCH.
This is a merge proposal, not a second claims or
definitions registry. The authoritative registries remain `db/*.tsv`.
Applied workflow: `/home/tobias/.claude/skills/rk-light/SKILL.md`.

## C0. Conclusion and source map

The continuous CCM input is a form on **test functions of the logarithmic
length**, not an already constructed physical bond. A supplied unitary
transfer flow would realize this form as the Gram matrix of **smeared
operators on the transfer space**. Without that input, the form and its
minimal eigenvector still construct a finite positive quotient and a
self-adjoint operator. This is a precise tensor contraction and an inverse
spectral construction, but it does not reconstruct unspecified local cMPS
letters, their auxiliary Hilbert space, or an existing Riemann generator.

Primary sources, with the local files authoritative for line references:

* `refs/src/2511.22755/mc2arXiv.tex` [CCM]: `bombtest`, lines 464–470;
  `weilQexp`, 496–527; `formN`, `basicexpli`, 810–833; `basics`, `key`,
  835–936; `dirichlet1`, `pertscal`, 977–1003; `four`, `finmain`, 1066–1123.
* `refs/src/2511.23257/Araki-final-oct25.tex` [CvS]: `qua0`, 993–1032;
  `matrixcomp`, 1033–1076; `nuance`, 1121–1122; `form2`, 1124–1133;
  `basics-general`–`prop:finmain`, 1313–1361; `main`, 1363–1392.
* Existing lab-book claims reused: `thm:cmps-ring-norms`,
  `thm:weil-positivity-continuous`, `thm:weil-line-duality`,
  `prop:hp-inner-product-continuous`, `prop:weil-blind-jordan` in 08c.
  Graded cMPS claims in 04e–04f remain at their current conditional/sketched
  status; this lane does not promote them by citation.

The word **kernel** has three different meanings here: the distributional
Schwartz kernel of the form, its algebraic nullspace/radical, and the
Dirichlet kernel representing truncated boundary evaluation. They must not
be interchanged.

## C1. Proposed definitions for centralisation in 02i

**D-C1 (continuous test form; proposed `def:ccm-tn-continuous-form`).**
Use the usual inner product antilinear in its first variable. For a
translation-invariant distribution \(W\) on \(\mathbb R\), and test functions
for which the pairing is defined, put
\[
 f^*(x)=\overline{f(-x)},\qquad
 W(f,g)=W(f^**g),\qquad
 (f^**g)(y)=\int\overline{f(x)}g(x+y)\,dx.
\]
The same letter on the left denotes the form and on the right the linear
distribution; explicitly state this convention at first use. When \(W\)
has density \(F\), its Schwartz kernel is \(K(x,y)=F(y-x)\), meaning
\(W(f,g)=\iint\overline{f(x)}K(x,y)g(y)\,dx\,dy\).
For a genuine distribution this is an equality of pairings, not a claim
that \(K\) is a function or a bounded integral operator.

**D-C2 (CCM window data; proposed `def:ccm-tn-loewner-window`).**
Fix \(L>0\), \(N\ge1\), \(I=[0,L]\), and
\(U_j(x)=L^{-1/2}e^{2\pi ijx/L}\), extended by zero outside \(I\).
Let \(E_N=\operatorname{span}\{U_j:|j|\le N\}\). A real distribution
\(\mathcal D\) on the **closed half interval** \([0,L]\), acting on
\(C^\infty([0,L])\), defines
\[
 Q(f,g)=\mathcal D\big((f^**g)(y)+(f^**g)(-y)\big),\qquad f,g\in E_N.
\]
This one-sided prescription is part of the definition. In CCM,
\(L=2\log\lambda\), \(\mathcal D=\log_*\Psi^\sharp\), and
\(Q_N=(Q(U_i,U_j))\) is the restricted Weil form.

**D-C3 (shifted metric and quotient; proposed
`def:ccm-tn-loewner-quotient`).** Write
\[
 D U_j=jU_j,\quad \gamma U_j=U_{-j},\quad
 \eta=\sum_{j=-N}^N U_j,\quad \epsilon=\lambda_{\min}(Q_N),\quad
 T=Q_N-\epsilon I.
\]
Assume the lowest eigenvalue is simple and its eigenvector is even under
\(\gamma\). Normalize this eigenvector \(\xi\) by
\(\langle\eta,\xi\rangle=1\); nonvanishing is proved in C4. The quotient is
\[
 \mathcal H_N=E_N/\mathbb C\xi,\qquad
 \langle[f],[g]\rangle_T=f^\dagger T g.
\]
This \(\gamma\) is Fourier reflection. It is **not** the physical bond
grading \(P\), nor doubled-bond parity \(P\otimes\bar P\).

**D-C4 (smeared transfer feature; proposed
`def:ccm-tn-smeared-feature`).** Given, additionally, a self-adjoint
operator \(H\) on a specified transfer Hilbert space \(\mathcal V\), put
\(U(t)=e^{-itH}\), \(\widehat f(s)=\int f(t)e^{-ist}dt\), and
\(A_f=\widehat f(H)\). Only call \(A_f\) a Hilbert–Schmidt feature when
\(\operatorname{Tr}|\widehat f(H)|^2<\infty\).

## C2. The natural insertion network and its hypotheses

**Proposed `prop:ccm-tn-continuous-smeared-gram` (SKETCH).**
ASSUME \(\mathcal V\) is finite-dimensional and \(H=H^\dagger\).
PROVE, with \(F(t)=\operatorname{Tr}_{\mathcal V}e^{-itH}\),
\[
 W(f,g)=\iint\overline{f(x)}g(y)F(y-x)\,dx\,dy
       =\operatorname{Tr}_{\mathcal V}(A_f^\dagger A_g).
 \tag{C2.1}
\]

* ⟨1⟩1. By the group law and adjoint identity,
  \(U(x)^\dagger U(y)=U(y-x)\). Insert
  \(A_f=\int f(x)U(x)dx\) into the finite trace. Fubini is valid for
  \(f,g\in L^1\), proving C2.1.
* ⟨1⟩2. In a basis of \(\mathcal V\), the actual contraction is
  \[
   W(f,g)=\sum_{a,b}\overline{(A_f)_{ab}}(A_g)_{ab}.
  \]
  It is a bra and ket transfer network with their two open transfer indices
  joined and their lengths smeared independently. The smearing is an
  insertion on the transfer space. No claim that it is a local physical
  field insertion follows.
* ⟨1⟩3. For a test basis \(f_j\),
  \(Q_{jk}=\langle A_{f_j},A_{f_k}\rangle_{HS}\).
  Thus \(\sum_jc_jf_j\) is in its radical exactly when
  \(\sum_jc_jA_{f_j}=0\). This statement concerns the **unshifted** Gram
  matrix. It does not apply to \(\ker(Q_N-\epsilon I)\) when
  \(\epsilon\ne0\).

Space accounting is essential. If a physical cMPS has auxiliary space
\(\mathcal B\), its transfer generator acts on
\(\mathcal V=\mathcal B\otimes\overline{\mathcal B}\simeq
\operatorname{End}(\mathcal B)\). The operators \(A_f\) are elements of
\(\operatorname{End}(\mathcal V)\), a further doubled space with four
auxiliary indices. Their span/Gram quotient is a moment space. Neither
\(\mathcal B\) nor all of \(\mathcal V\) is recovered from this contraction.
For finite \(H\), the span of all functions of \(H\) has one dimension per
distinct visible spectral value, irrespective of its multiplicity.

An existing centred transfer generator \(\mathcal L-aI=-iH\) supplies
C2.1 only if it is skew-adjoint in the chosen positive metric. If such a
metric is changed, use its induced adjoint and Hilbert–Schmidt norm, not
the original physical Hilbert–Schmidt norm. Existing 08c separates
positive definiteness (a half-plane bound), duality (upgrading to the
line), and semisimplicity (needed for a positive unitarising metric).
Trace data do not see Jordan blocks. None of those gaps disappears upon
drawing a tensor network.

The unconditional CCM input already has an exact contraction:
\[
 Q_N(i,j)=\Psi(V_i^**V_j).
\]
This contracts the test-function bra/ket against the arithmetic
distribution. Calling it a **positive Hilbert-space Gram contraction**
requires positivity; calling it a contraction on a specified physical
bond requires a realization theorem. After the scalar subtraction,
\(T\) always has the finite Gram realization
\(T_{ij}=\langle T^{1/2}e_i,T^{1/2}e_j\rangle\), but that realizes the
constructed quotient, not arithmetic local letters.

## C3. Loewner structure is the finite boundary defect

**Proposed `prop:ccm-tn-loewner-displacement` (SKETCH).**
ASSUME D-C2. PROVE
\[
 (Q_N)_{ii}=a_i,\qquad (Q_N)_{ij}=\frac{b_i-b_j}{i-j}\quad(i\ne j),
 \tag{C3.1}
\]
where
\[
 a_j=\mathcal D\big(2(1-y/L)\cos(2\pi jy/L)\big),\qquad
 b_j=-\pi^{-1}\mathcal D\big(\sin(2\pi jy/L)\big).
\]
Consequently \(a_{-j}=a_j\), \(b_{-j}=-b_j\),
\(Q_N\gamma=\gamma Q_N\), and, with \(\beta=\sum_jb_jU_j\),
\[
 [D,Q_N]=[D,T]=|\beta\rangle\langle\eta|
                    -|\eta\rangle\langle\beta|.
 \tag{C3.2}
\]
The displacement has rank **at most** two, possibly zero.

* ⟨1⟩1. For \(0\le y\le L\), integrate the two zero-extended
  exponentials over their overlap \([y,L]\). If \(m\ne n\),
  \[
  (U_m^**U_n)(y)=
   \frac{e^{2\pi imy/L}-e^{2\pi iny/L}}{2\pi i(n-m)}.
  \]
  Adding its value at \(-y\) gives
  \((\sin(2\pi my/L)-\sin(2\pi ny/L))/(\pi(n-m))\).
  The diagonal sum is \(2(1-y/L)\cos(2\pi ny/L)\).
  Applying \(\mathcal D\) proves C3.1, including all signs.
* ⟨1⟩2. The parity identities follow directly. Entrywise,
  \([D,Q_N]_{ij}=(i-j)(Q_N)_{ij}=b_i-b_j\), also on the diagonal.
  This proves C3.2. Subtracting \(\epsilon I\) leaves it unchanged.
* ⟨1⟩3. \(\eta^\dagger f=\sqrt L f(0)=\sqrt L f(L)\) for
  \(f\in E_N\). Thus the two terms of C3.2 are boundary covectors and
  their response vectors. This is the concrete boundary defect in the
  attempted symmetry of differentiation under the new form.

The matrix is Loewner in the Fourier basis, generally **not Toeplitz in
the Fourier indices**. Translation invariance of the distribution in
position space does not eliminate the finite interval boundary.

Endpoint discipline:

* \(\mathcal D=\delta_0\) gives \(Q_N=2I\). Thus
  \(T=Q_N-\epsilon I\) corresponds on this window to replacing
  \(\mathcal D\) by \(\mathcal D-(\epsilon/2)\delta_0\).
* \(\mathcal D=\delta'_0\) gives
  \(Q_N=(2/L)|\eta\rangle\langle\eta|\), because every derivative
  at \(0+\) of the symmetrized correlation above is \(-2/L\).
  Its symmetrization as an ordinary distribution on smooth full-line
  functions is zero. The correlations of zero-extended periodic functions
  have a corner at zero; the one-sided prescription sees it. This proves
  why a globally even Schwartz distribution alone does not encode every
  half-interval form (CvS, `nuance`).
* An order-zero atom at \(y=L\) contributes zero since all those
  correlations vanish at \(L\). In particular a prime power exactly at
  the cutoff \(\log n=L\) contributes zero to this finite form.
  Derivatives of an endpoint atom need not vanish.

## C4. Full finite proof of the correction, metric and characteristic polynomial

**Proposed `thm:ccm-tn-loewner-quotient` (SKETCH).**
ASSUME the real symmetric Loewner data of C3, and D-C3's simple even
lowest eigenvalue. PROVE that
\[
 D'=D-|D\xi\rangle\langle\eta|
 \tag{C4.1}
\]
induces a self-adjoint operator \(D''\) on \(\mathcal H_N\), with
\[
 \det(D''-sI)=P_N(s)
 =\sum_{j=-N}^N\xi_j\prod_{k\ne j}(k-s).
 \tag{C4.2}
\]
All \(2N\) roots, counted with multiplicity, are real. This hypothesis
does **not** assume \(\epsilon\ge0\).

* ⟨1⟩1. **Positive metric with one radical.** By the spectral theorem,
  \(T\ge0\) and \(\ker T=\mathbb C\xi\). Choose \(\xi\) real.
  Parity gives \(\beta^\dagger\xi=0\), since \(\beta\) is odd and
  \(\xi\) is even.
* ⟨1⟩2. **Boundary normalization exists.** If \(D\xi=0\), the simple
  zero eigenspace of \(D\) gives \(\xi\in\mathbb C U_0\), so its
  overlap with \(\eta\) is nonzero. Otherwise \(D\xi\) is a nonzero
  odd vector, hence outside \(\ker T\), and \(TD\xi\ne0\).
  Applying C3.2 to \(\xi\) gives
  \(-TD\xi=\beta(\eta^\dagger\xi)\). Therefore
  \(\eta^\dagger\xi\ne0\), and rescaling gives one. In that
  normalization,
  \[
     TD\xi=-\beta. \tag{C4.3}
  \]
* ⟨1⟩3. **Unique boundary correction.**
  \(P_0=I-|\xi\rangle\langle\eta|\) is an idempotent onto
  \(\ker\eta^\dagger\), with kernel \(\mathbb C\xi\).
  Equation C4.1 is \(D'=DP_0\). It kills \(\xi\) and agrees with
  \(D\) on \(\ker\eta^\dagger\). These two complementary subspaces
  span \(E_N\), proving uniqueness. A network implementation adds one
  rank-one boundary tensor: output \(D\xi\), input \(\eta^\dagger\).
* ⟨1⟩4. **Metric symmetry.** By C4.3,
  \[
  TD'=TD+\beta\eta^\dagger,
  \qquad D'^\dagger T=DT+\eta\beta^\dagger.
  \]
  C3.2 makes these equal. Since \(D'\xi=0\), \(D'\) descends to
  the quotient. Its descended form is positive definite by ⟨1⟩1, and
  finite-dimensional symmetry is self-adjointness. In particular its
  spectrum is real and it is diagonalizable in that metric.
* ⟨1⟩5. **An explicit Euclidean implementation.** Let \(C\) have
  orthonormal columns spanning \(\xi^\perp\), put
  \(G=C^\dagger TC>0\), \(B=C^\dagger D'C\). Then
  \(TC=CG\) and ⟨1⟩4 give \(GB=B^\dagger G\). Thus
  \(G^{1/2}BG^{-1/2}\) is an ordinary Hermitian representative.
  Using merely \(C^\dagger DC\), or declaring \(B\) Hermitian in
  the Euclidean metric, implements a different operator.
* ⟨1⟩6. **Determinant away from poles.** For \(s\notin\{-N,\ldots,N\}\),
  the rank-one determinant identity gives
  \[
  \begin{split}
  \det(D'-sI)
   &=\det(D-sI)\bigl(1-\eta^\dagger(D-sI)^{-1}D\xi\bigr)\\
   &=-s\det(D-sI)\eta^\dagger(D-sI)^{-1}\xi.
  \end{split}
  \]
  The last equality uses
  \((D-sI)^{-1}D\xi=\xi+s(D-sI)^{-1}\xi\) and
  \(\eta^\dagger\xi=1\).
* ⟨1⟩7. **Removing the killed line.** In a basis beginning with
  \(\xi\) and continuing with lifts of a quotient basis, \(D'\)
  is block upper triangular with diagonal blocks \(0,D''\).
  Hence \(\det(D'-sI)=-s\det(D''-sI)\). Cancel \(-s\) away
  from zero and the poles, then extend the resulting polynomial identity
  to every \(s\). This proves C4.2, including \(s=0\) and the grid.
* ⟨1⟩8. **Degree and symmetry.** Because \(\sum_j\xi_j=1\), C4.2
  has degree \(2N\) and leading coefficient one. Relabelling
  \(j\mapsto-j\) proves \(P_N(-s)=P_N(s)\). Roots come in opposite
  pairs; zero, if present, has even multiplicity. Do not assert there
  are \(N\) strictly positive roots without excluding zero.

The scalar \(\epsilon\) is a variational threshold. It is not a spectral
frequency, a shift of \(D\), or evidence that the original Weil form is
positive. Adding \(cI\) to \(Q_N\) adds \(c\) to \(\epsilon\) and
leaves \(T,\xi,D',D''\) unchanged.

**The nullvector–Hamiltonian connection.** \(T\) itself is a positive
Hamiltonian on the Fourier coefficient/length space: its energy is
\(f^\dagger T f\), and its unique zero-energy line is \(\mathbb C\xi\).
This gives a precise ground-state meaning to the minimal-eigenvector
prescription. \(D''\) is a second Hamiltonian, a self-adjoint frequency
operator on a different Hilbert space with metric \(T\). It is built
from that ground-state constraint and then **removes** the ground-state
line. Thus the killed vector is not a physical zero-frequency eigenstate
of \(D''\). Its Fourier transform instead supplies the characteristic
function whose zeros are the new frequencies (C5). Neither positive
matrix \(T\) nor rank-one \(D'\) supplies local physical-site terms of
an MPS parent Hamiltonian without an additional locality/realization
argument. The root's `hamiltonian.md` gives separate length-clock and
history-state Hamiltonians, with their own spaces and zero vectors.

## C5. Secular roots, endpoints, and the entire transform

Away from the Fourier grid the quotient spectrum is given by
\[
 g_N(s)=\sum_{j=-N}^N\frac{\xi_j}{j-s}=0.
 \tag{C5.1}
\]
The universally valid object is the polynomial C4.2, not this meromorphic
display. At a grid point \(s=j\),
\[
 P_N(j)=\xi_j\prod_{k\ne j}(k-j).
 \tag{C5.2}
\]
Thus \(j\) is a quotient eigenvalue iff \(\xi_j=0\). The apparent pole
then disappears from \(g_N\), but the zero from \(\det(D-sI)\) remains
in \(P_N\); further coincidence with a zero of the analytic continuation
of \(g_N\) raises its multiplicity. This includes \(j=0\).
The unquotiented \(D'\) always has the additional killed zero mode.

There is no positive-residue hypothesis on \(\xi_j\), so
\(g_N'(s)=\sum_j\xi_j/(j-s)^2\) need not be positive. Roots can be
multiple, share a pole interval, and lie outside the extreme poles.
One sign change per interval is not a completeness certificate; neither
is searching only \([-N,N]\).

**Exact counterexample / proposed `prop:ccm-tn-no-naive-compression`
(SKETCH).** In the ordered basis \((-1,0,1)\), take
\[
 T=Q_N=\begin{pmatrix}6&2&2\\2&1&2\\2&2&6\end{pmatrix},\quad
 D=\operatorname{diag}(-1,0,1),\quad
 \xi=(-1/2,2,-1/2)^t,\quad\beta=(-2,0,2)^t.
 \tag{C5.3}
\]
ASSUME these displayed matrices. PROVE all C4 hypotheses and failure of
ordinary compression/interlacing.

* ⟨1⟩1. Direct multiplication gives \(T\xi=0\),
  \(T(1,0,-1)^t=4(1,0,-1)^t\), and
  \(T(2,1,2)^t=9(2,1,2)^t\). The three independent vectors prove
  positivity and the simple even radical. Its normalized coordinate sum
  is one. Entrywise C3.1 holds with the stated \(\beta\).
* ⟨1⟩2. C4.2 gives \(P_N(s)=s^2-2\). Its roots
  \(\pm\sqrt2\) lie beyond \(\pm1\).
* ⟨1⟩3. Every ordinary orthogonal compression of the Hermitian
  \(D\) has Rayleigh quotients in \([-1,1]\). Therefore this \(D''\)
  is not such a compression. It is the quotient of the corrected
  \(D'\) in the new metric.
* ⟨1⟩4. Replacing \(Q_N\) by \(Q_N-10I\) makes it negative
  definite and makes its smallest eigenvalue \(-10\), without changing
  \(T\) or the real quotient spectrum. Thus real CCM output does not
  establish unshifted Weil positivity, even at a single finite window.

For the multiplicative window, \(\omega_j=2\pi j/L\) and
\(V_j(u)=U_j(\log(\lambda u))\). The zero extension of
\(\xi(u)=\sum_j\xi_jV_j(u)\) has entire Mellin–Fourier transform
\[
 \widehat\xi(z)=\frac2{\sqrt L}\sin(zL/2)
                 \sum_{j=-N}^N\frac{\xi_j}{z-\omega_j}.
 \tag{C5.4}
\]
This follows by integrating each exponential; no RH assumption is used.
At an included grid point,
\(\widehat\xi(\omega_j)=\sqrt L(-1)^j\xi_j\), with the limit understood.
For \(|j|>N\), the sine factor supplies the unchanged Fourier-tail
eigenvalue; if the rational numerator also vanishes there, multiplicities
add. The complete self-adjoint operator consists of
\((2\pi/L)D''\) on \(\mathcal H_N\) and the periodic differentiation
operator on \(E_N^\perp\). Its spectrum is exactly the zeros of C5.4,
including tail and removable-pole cases. The rank-one perturbation on
the original periodic \(H^1\) domain is bounded, but the self-adjoint
statement is on the specified quotient-plus-tail Hilbert space.

With the source's alternative normalization
\(\delta_N=\eta/\sqrt L\), \(\delta_N(\xi_b)=1\), one has
\(\xi_b=\sqrt L\xi\) and
\[
 D_{\log}'=D_{\log}-|D_{\log}\xi_b\rangle\langle\delta_N|,
 \qquad
 \det_{\mathrm{reg}}(D_{\log}'-z)
       =-i e^{-izL/2}\widehat\xi_b(z).
\]
The determinant identity uses CCM's spectral-cut convention and denotes
the quotient-plus-tail operator; it is not the determinant of the
unquotiented matrix with its extra zero. It is cited from CCM `finmain`,
not needed for the finite proof above.

## C6. Infinite trace: a valid smeared statement and an invalid raw one

**Proposed `prop:ccm-tn-infinite-smeared-gram` (SKETCH).**
ASSUME \(H\) has an orthonormal eigenbasis with real eigenvalues
\(\gamma_r\), repeated with multiplicity, and the locally finite counting
measure \(\mu=\sum_r\delta_{\gamma_r}\) has polynomial growth. For
\(f,g\in C_c^\infty(\mathbb R)\), PROVE
\[
 W(f,g)=\int\overline{\widehat f(t)}\widehat g(t)\,d\mu(t)
       =\operatorname{Tr}(A_f^\dagger A_g),\qquad
 W(f,f)=\|A_f\|_{HS}^2.
 \tag{C6.1}
\]

* ⟨1⟩1. Repeated integration by parts makes \(\widehat f\) and
  \(\widehat g\) rapidly decreasing. Polynomial counting growth gives
  \(\sum_r|\widehat f(\gamma_r)|^2<\infty\) and similarly for
  \(g\). Spectral calculus therefore gives Hilbert–Schmidt diagonal
  operators \(A_f,A_g\).
* ⟨1⟩2. Cauchy–Schwarz makes the displayed scalar cross sum absolutely
  convergent. The product of the two Hilbert–Schmidt operators is trace
  class and its diagonal trace gives C6.1.
* ⟨1⟩3. Define the tempered distribution
  \(W(h)=\int\widehat h(t)d\mu(t)\). Since
  \(\widehat{f^**g}=\overline{\widehat f}\widehat g\) on the real
  line, this is exactly the form of D-C1. One never needs a finite
  pointwise \(\operatorname{Tr}U(t)\).
* ⟨1⟩4. If \(\mathcal V\) is infinite-dimensional, every unitary
  \(U(t)\) satisfies \(\|U(t)\|_{HS}^2=\operatorname{Tr}I=\infty\).
  Therefore the proposed raw Gram matrix
  \(\operatorname{Tr}(U(s)^\dagger U(t))\) is undefined at least on
  its diagonal, and \(U(t)\) is never trace class. Oscillatory formal
  traces require a distributional interpretation. Smearing only the
  outer double integral does not justify an intermediate infinite
  pointwise trace; C6.1 supplies the valid order of operations.

A general positive tempered measure also gives the feature space
\(L^2(\mu)\), with feature \(\widehat f\), without supplying a trace on
any physical bond. The completion of the test quotient is the closure of
those features; no density assertion beyond that closure is needed.
When \(\mu(\mathbb R)=\infty\), the constant feature is not in
\(L^2(\mu)\), so this is not an ordinary finite-measure cyclic-vector
construction with \(\delta_0\) as a normalized vector.

For zeta, the explicit formula defines the form without RH. Its zero-side
pairing, with \(F_f(\rho)=\int f(x)e^{(\rho-1/2)x}dx\), is
\[
 QW(f,g)=\sum_\rho
    \overline{F_f(1-\bar\rho)}F_g(\rho).
 \tag{C6.2}
\]
On a smooth compactly supported test class the transform decays rapidly
in vertical strips, making the zero pairing absolutely convergent using
the usual zero-counting growth. RH makes the paired arguments equal;
then C6.2 becomes a sum of squares. With the Fourier convention of D-C4
the associated real counting measure sits at \(-\operatorname{Im}\rho\);
zeta's conjugation symmetry makes this the same multiset as the ordinates.
Thus C6.1 is a **conditional** spectral realization of the Riemann form,
not a derivation of RH. The full Weil converse is the already cited
`cit:weil-criterion`; finite CCM self-adjointness is a different statement.

The zero-extended Fourier-window functions are not \(C_c^\infty\).
Do not silently invoke C6.1 for them. One must use the source's stated
closed form/domain or prove the corresponding summability separately.
For a real discrete zero spectrum with \(N(T)=O(T\log T)\), their
\(O((1+|t|)^{-1})\) transforms do give square summability, so the
Hilbert–Schmidt feature statement extends to this particular class.
The form-domain and endpoint prescription still must be specified.

## C7. Why this is not yet a compression of the Riemann bond

There are three different established or conditional operations:

1. \(Q_N\) restricts the Weil **form operator** to a finite test space.
2. \(D''\) is a quotient of the rank-one-corrected differentiation
   operator \(D'\), with metric \(Q_N-\epsilon I\).
3. A compression of a supplied physical transfer generator would require
   a specified isometry from that quotient into the physical transfer
   space (or its operator feature space), domain control, and an identity
   relating the two generators.

Only (1) and (2) are in the source construction. (3) is not proved by their
existence. Even under a positive spectral realization of the **unshifted**
form, its natural feature map \(A:E_N\to HS(\mathcal V)\) satisfies
\[
 \|A\xi\|_{HS}^2=\xi^\dagger Q_N\xi
                  =\epsilon\|\xi\|_2^2.
 \tag{C7.1}
\]
For \(\epsilon>0\), this map does not kill \(\xi\), so it does not
even descend to the CCM quotient. Replacing \(Q_N\) by its shifted
metric has changed the data to be represented. Globally, subtracting
\(\epsilon\langle f,g\rangle_{L^2}\) would replace a spectral measure
\(\mu\) by \(\mu-\epsilon\,dt/(2\pi)\), using Plancherel in the
present convention. Positivity on a finite test space does not make this
a positive measure on all tests.

There is a precise surviving conditional intertwining statement.
ASSUME all even-simple CCM hypotheses of C4 (in particular the simple radical),
and a finite-dimensional self-adjoint \(H\) realizes the unshifted
form by C2.1, \(\epsilon=0\), and use \([0,L]\) coordinates with
\(\xi_b(0)=\xi_b(L)=1\). PROVE that the feature isometry descends and
intertwines the physical differentiation correction with left
multiplication by \(H\):
\[
 A(D_{\log}'f)=H A(f),\qquad f\in E_N.
 \tag{C7.2}
\]

* ⟨1⟩1. Integration by parts gives
  \[
  A(-if')=H A(f)-i f(0)(e^{-iLH}-I)
  \]
  for periodic \(f\in E_N\).
* ⟨1⟩2. Equation C7.1 with \(\epsilon=0\) gives \(A(\xi_b)=0\).
  Apply ⟨1⟩1 to \(\xi_b\):
  \(A(-i\xi_b')=-i(e^{-iLH}-I)\). Subtract \(f(0)\) times
  this identity from ⟨1⟩1, proving C7.2.
* ⟨1⟩3. C2.1 identifies the radical with \(\ker A\), so the quotient
  maps isometrically onto \(A(E_N)\). Equation C7.2 makes this range
  invariant under the self-adjoint superoperator \(B\mapsto HB\)
  on \(HS(\mathcal V)\). Its restriction is the actual representation
  of CCM in this special exact case. This recovers a function-of-\(H\)
  module, not the full physical multiplicity space.

For an infinite \(H\), C7.2 requires the additional domain and
Hilbert–Schmidt summability needed for \(HA(f)\); do not transfer the
finite integration-by-parts proof without them. For \(\epsilon\ne0\),
the same formal calculation leaves the defect
\(-f(0)HA(\xi_b)\). The source gives no vanishing theorem for it.

## C8. Conditional cMPS and graded readings

For a finite physical auxiliary space \(\mathcal B\), matrices \(K,R_a\)
give the doubled transfer
\[
 \mathcal L=K\otimes I+I\otimes\bar K+
                 \sum_aR_a\otimes\bar R_a.
\]
The ring contraction of length \(t\ge0\) is
\(\operatorname{Tr}_{\mathcal V}e^{t\mathcal L}\). The Dyson formula
of existing `thm:cmps-ring-norms` writes it as integrals of
\( |\operatorname{Tr}(e^{(t-t_n)K}R_{a_n}\cdots
R_{a_1}e^{t_1K})|^2\). These are local propagators and jumps on
\(\mathcal B\). The squared amplitudes are positive, but their trace
as a function of positive length is not automatically a positive-definite
function on all signed lengths. Centering, removal of specified modes,
line duality, and a metric/semisimplicity input remain separate.

If a bond involution \(P\) makes \(K\) even and each \(R_a\)
homogeneous, the transfer parity is \(\Gamma=P\otimes\bar P\).
Existing 04f gives, under its stated finite cMPS hypotheses,
\[
 \|\Psi_P(t)\|^2=\operatorname{Tr}(\Gamma e^{t\mathcal L})
 =\operatorname{Tr}(e^{t\mathcal L}|_{\mathcal V_+})
  -\operatorname{Tr}(e^{t\mathcal L}|_{\mathcal V_-}).
\]
For a unitary flow commuting with \(\Gamma\), the **signed** spectral
form is correspondingly
\(\|A_f|_{\mathcal V_+}\|_{HS}^2-
\|A_f|_{\mathcal V_-}\|_{HS}^2\). It is not an ordinary positive
Gram form. To obtain the odd-sector positive form, one must supply and
subtract the known even trace: \(\operatorname{Tr}U_-=\operatorname{Tr}U_+
-\operatorname{str}U\). Equal even/odd eigenvalues cancel in supertrace
data, so the full hidden parity sectors cannot be inferred from them.

For a Riemann application, identifying the pole and archimedean terms
with specified even transfer modes is an extra theorem, not a relabelling
licensed by the explicit formula. In the existing compressed zeta
semigroup dictionary those terms lie on the geometric side and are not
eigenmodes of that semigroup (08c `obs:weil-zeta-dictionary`). Nor does
Fourier reflection \(\gamma\) make the CCM quotient the odd physical
block. Its even-simple hypothesis refers to reflection, not fermion
parity, and supplies no Schmidt or entanglement spectrum interpretation.

## C9. What the continuous limit does prove

**Proposed `prop:ccm-tn-fixed-window-limit` (SKETCH; optional shard).**
ASSUME the real reflection-invariant half-interval form of D-C2 closes to a semibounded closed form \(Q\)
on \(L^2([0,L])\), the trigonometric polynomials are a form core, and
its associated self-adjoint operator has a simple isolated lowest
eigenvalue \(\epsilon\), with an even normalized eigenfunction \(\xi\).
PROVE that normalized lowest eigenvectors of the Fourier restrictions
eventually are simple and even, converge in norm after phase choice to
\(\xi\), and that the zero-extended Fourier transform of \(\xi\) has
only real zeros.

* ⟨1⟩1. The variational principle and the nested form core give
  \(\epsilon_N\downarrow\epsilon\). If the spectral gap is
  \(\delta>0\), then on \(\xi^\perp\) the form is at least
  \((\epsilon+\delta)\|f\|^2\).
* ⟨1⟩2. Min–max applied to \(E_N\cap\xi^\perp\) makes the second
  eigenvalue of \(Q_N\) at least \(\epsilon+\delta\). For all
  sufficiently large \(N\), \(\epsilon_N<\epsilon+\delta\), so its
  lowest eigenvalue is simple. Its normalized eigenvector satisfies
  \(1-|\langle\xi,\xi_N\rangle|^2\le
  (\epsilon_N-\epsilon)/\delta\), giving convergence after phase
  choice.
* ⟨1⟩3. Since \(Q_N\) commutes with reflection, the simple eigenvector
  has definite parity. If it were odd, it would be orthogonal to the even
  \(\xi\), contradicting the gap bound. Thus it is even. Closeness to
  a closed even subspace alone would not prove this; the commutation and
  gap are used.
* ⟨1⟩4. C4–C5 imply that each sufficiently late
  \(\widehat\xi_N\) has only real zeros. On a compact set of \(z\),
  Cauchy–Schwarz bounds
  \(|\widehat\xi_N(z)-\widehat\xi(z)|\) by a uniform constant times
  \(\|\xi_N-\xi\|_2\). Thus convergence is locally uniform, the
  limit is not identically zero, and Hurwitz on each open half plane
  proves the assertion.

This is a fixed-window statement, matching the scope of CvS `main` with
explicit form-core hypotheses. It does not establish simple even ground
states at every Riemann window or identify the transform with completed
zeta. Passing \(L\to\infty\) would require new control. For example,
locally uniform convergence of appropriately normalized real-zero entire
approximants to the entire completed zeta function would prove RH by
Hurwitz, but no such theorem follows from the finite construction.
Approximation to many known critical-line zeros alone cannot exclude an
unseen off-line zero.

## C10. Merge/status and provenance proposals

Suggested main shard: `08g_ccm_continuous_tensor.tex`, containing C2,
C3–C5, C6, and the no-identification conclusion of C7–C8, referring to
central definitions. Keep the fixed-window limit separate if needed to
meet the 320-line shard budget. All new rows start `sketched`.

| Proposed id | Statement scope | Argument |
|---|---|---|
| `prop:ccm-tn-continuous-smeared-gram` | Finite unitary transfer insertion contraction | C2 ⟨1⟩1–3 |
| `prop:ccm-tn-loewner-displacement` | Half-interval form, rank-at-most-two boundary displacement | C3 ⟨1⟩1–3 |
| `thm:ccm-tn-loewner-quotient` | Simple even minimum, shifted quotient metric, real spectrum and polynomial | C4 ⟨1⟩1–8 |
| `prop:ccm-tn-no-naive-compression` | Exact outer-root/orthogonal-compression/positivity counterexample | C5 ⟨1⟩1–4 |
| `prop:ccm-tn-infinite-smeared-gram` | Discrete real polynomial-counting spectrum and smooth tests; raw unitary divergence | C6 ⟨1⟩1–4 |
| `prop:ccm-tn-exact-continuous-intertwiner` | Existing finite H, unshifted Gram and epsilon zero | C7 ⟨1⟩1–3 |
| `prop:ccm-tn-fixed-window-limit` | Closed form, form core, isolated simple even minimum | C9 ⟨1⟩1–4 |

Retain the following stronger formulations as explicit negative records:
“CCM is an ordinary compression of the input scaling generator” (refuted
by C5); “real finite CCM spectrum proves unshifted Weil positivity”
(refuted by C5); “an infinite unitary flow has a finite raw HS Gram”
(refuted by C6). The Riemann-bond identification is **unestablished**, not
refuted: no existing physical-bond realization/intertwiner is supplied.
“CCM reflection-even means physical odd” is an unsupported identification
of different involutions, not an established theorem.

Short, exact, contiguous quotation candidates (line references already
checked; source LaTeX retained):

| Provenance proposal | File / label / lines | Exact excerpt |
|---|---|---|
| `prov:ccm25-convolution-form` | CCM `bombtest`, 466 | `QW(f,g)=\Psi(f^**g), \ \` |
| `prov:ccm25-rank-two` | CCM `QD`, 840 | `D\,	T-T\, D=\vert \beta\rangle\langle \eta\vert -\vert \eta\rangle\langle \beta\vert` |
| `prov:ccm25-quotient-selfadjoint` | CCM `key`, 865 | `as quotient by null vectors` |
| `prov:ccm25-convergence-numerical` | CCM abstract, 270 | `Numerical experiments show that the spectra of the operators` |
| `prov:cvs25-endpoint-nuance` | CvS `nuance`, 1121 | `the associated even distribution obtained by symmetrisation is equal to $0$` |
| `prov:cvs25-limit-hypotheses` | CvS `main`, 1366 | `a simple, isolated eigenvalue` |

These excerpts are deliberately short; the precise mathematical scope
comes from the identified theorem/definition and the checked argument,
not from expanding a fragment into a stronger claim. Source [CCM]
`dirichlet1` has the correct normalization \(\delta_N=L^{-1/2}\sum V_n\);
its proof's line 989 misidentifies the unnormalized Dirichlet sum by a
factor of \(L\). C3/C5 use the directly verified boundary evaluation,
not that erroneous intermediate line. Source [CvS] `basics-general`
also requires \(a_{-j}=a_j\) to conclude \(Q\gamma=\gamma Q\);
C3 states it explicitly. No source typo is used as a hypothesis.
