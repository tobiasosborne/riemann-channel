# H-THETA-1: proof and correction ledger

Author: codex:gpt-6-astra

| Claim | Verdict | Result |
|---|---|---|
| T1 | SHARPENED | Cauchy criterion proved; Hardy pole and finite-time defect corrected |
| T2 | PROVED | First-slot Gram is i/(w_j−conj(w_i)); loss matrix is all ones |
| T3 | SHARPENED | Augmented cosine space; critical-line real Gram; numerator test refuted |
| T4 | REFUTED | Exact three-zero obstruction; explicit Gram scheme and numerical negative loss eigenvalue |
| T5 | SHARPENED | All admissible norms are Cauchy Gram norms with diagonal/jet freedom |
| T6 | SHARPENED | Scalar generator exit; reset-dependent holding laws; sampled loss has full finite rank |
| T7 | SHARPENED | Damped length-two chain, explicit matrices and reset laws; square comes from two radiation maps |

**Main verdict: H-THETA-1 is REFUTED in the prescribed Sonine norm, by an exact three-zero argument (T4).**

Inner products are linear in the first slot. Source citations refer to the local files and their line numbers. The progress file is the explicit exception required by the brief's durability clause.

## T1 — SHARPENED: the continuous-time Cauchy criterion

**PROVED.** Use \(\langle f,h\rangle=\int f\overline h\). For nonzero eigenvectors with \(\Re d_i<0\), a scalar exit form forces
\[
N_{ij}:=-(d_i+\overline{d_j})G_{ij}=c_i\overline{c_j},\qquad c_i=j(e_i)\ne0.
\tag{1}
\]
Indeed substitute the eigenvectors in the form; the diagonal gives \(|c_i|^2=-2\Re d_i\|e_i\|^2>0\). No stability assumption is needed for this necessity.

Conversely suppose (1) holds. Define on the algebraic span
\[
We_i(X)=c_i e^{d_iX},\quad X>0,\qquad
\langle We_i,We_j\rangle=\frac{c_i\overline{c_j}}{-(d_i+\overline{d_j})}=G_{ij}.
\tag{2}
\]
The equality of Gram forms makes this well-defined and isometric, including any linear relations. Its closed image \(M\subset L^2(0,\infty)\) is invariant under the backward translations \(S_tf(X)=f(X+t)\). Their restriction is a strongly continuous, strongly stable contraction semigroup and has the prescribed eigenvalues. Strong stability follows from the vanishing tail integral. Its generator is \(f'\) on \(M\cap H^1(0,\infty)\); integration by parts gives the exit \(j(f)=f(0)\). Thus on a nonempty finite family the one-exit realization in the specified Gram norm exists **if and only if** \(N\) is positive of rank one.

The regular translation group dilates this semigroup after extending functions by zero to the negative half-line (the compressed group is backward translation). It is minimal: translates of any one nonzero exponential span \(L^2(\mathbb R)\), since its Fourier transform has no real zero and Fourier uniqueness applies. Reflection changes this group into the notebook's forward \(U_t\). This asserts unitary equivalence of minimal dilations, not equality of the original Sonine embedding with this observation embedding.

**SHARPENED (kernel convention).** The brief's \(1/(z-\bar d)\) has a pole *inside* the left half-plane when \(\Re d<0\), so is not its Hardy kernel. One safe equivalent is the right-half-plane Laplace transform with boundary measure \(du/(2\pi)\): (2) transforms to \(c_i/(z-d_i)\), the kernel at \(-\bar d_i\). In the notebook upper-half-plane transform it is \(ic_i k_{i\bar d_i}\), where \(k_w(u)=1/(u-\bar w)\). These maps, rather than the incorrectly located pole, give the claimed Cauchy model.

**PROVED (jets).** For the brief's chain \(Ae_{i,k}=d_i e_{i,k}+(k/2)e_{i,k-1}\), put \(c_{i,k}=j(e_{i,k})\). The exact finite test is
\[
-(d_i+\bar d_j)G_{ik,jl}-\frac k2G_{i,k-1;j,l}-\frac l2G_{i,k;j,l-1}
=c_{i,k}\overline{c_{j,l}},
\tag{3}
\]
with negative-index terms omitted. Equivalently its Gram matrix is that of
\[
q_{i,k}(X)=e^{d_iX}\sum_{r=0}^k\binom kr (X/2)^{k-r}c_{i,r},
\]
\[
G_{ik,jl}=\sum_{r=0}^k\sum_{v=0}^l
\binom kr\binom lv\frac{c_{i,r}\overline{c_{j,v}}(k+l-r-v)!}
{2^{k+l-r-v}[-(d_i+\bar d_j)]^{k+l-r-v+1}}.
\tag{4}
\]
To prove the equivalence, integrate the derivative of
\(\langle e^{tA}f,e^{tA}h\rangle\) on the finite stable root space from zero to infinity. The polynomial times exponential decay removes the boundary term at infinity. Conversely differentiation of the displayed \(q\)'s gives the specified chain and integration by parts gives (3). A nondegenerate chain requires \(c_{i,0}\ne0\); this follows from the eigenvector diagonal in (3). These arguments also construct the infinite completion whenever one coherent exit family satisfies all finite tests.

## T2 — PROVED: the Riemann model passes identically

**PROVED, with the first-slot convention retained.** Set \(X=\log y\), use \(dX\) and \(du/(2\pi)\), and put \(w_i=\gamma_i/2+i(1-\sigma_i)/2\). The actual evaluation kernel of \(H^2(\mathbb C_+)\) is \(\kappa_w(z)=i/(z-\bar w)\); the notebook calls \(k_w=\kappa_w/i\) its kernel. Projection gives
\[
\kappa_w^\Theta(z)=\frac{i[1-\overline{\Theta(w)}\Theta(z)]}{z-\bar w},\qquad
\langle\kappa_w^\Theta,\kappa_v^\Theta\rangle
=\frac{i[1-\overline{\Theta(w)}\Theta(v)]}{v-\bar w}.
\tag{5}
\]
For example evaluation follows directly by contour integration, and the subtracted term is the kernel of \(\Theta H^2\); this proves the projection formula. At zeros of \(\Theta\),
\[
\mathcal F^{-1}k_{w_i}(X)=-i e^{-i\bar w_iX}1_{X>0},\quad
G^{\rm mod}_{ij}=\frac{i}{w_j-\bar w_i}
=\frac{1}{-(d_i+\bar d_j)},\quad d_i=-i\bar w_i,
\]
\[
j(k_{w_i})=-i,\qquad N^{\rm mod}_{ij}=1.
\tag{6}
\]
These are eigenvectors of \(C_t=(P_KU_t|_K)^*\), not generally of \(Z_t=P_KU_t|_K\). The generator exit identity follows by integration by parts as in T1. Zeros with multiplicities use (3)–(4). The pure Blaschke result in `report/sections/04q_h_theta.tex`, `thm:symbol-edge-quotient`, proves completeness of these jets.

**SHARPENED (transposition).** With an inner product linear in the first slot, (6) is \(i/(w_j-\bar w_i)\). The frequently printed \(i/(w_i-\bar w_j)\) is its transpose and is the coordinate metric \(H\) in \(\|\sum x_i k_i\|^2=x^*Hx\). This explains the convention difference in 04h's numerical matrix identity. For three critical zeros the diagonal of \(G^{\rm mod}\) is \(2\), and the loss matrix has eigenvalues \(3,0,0\) exactly.

## T3 — SHARPENED: the actual Sonine space and the missing shift

### 1. Which evaluators, which completion

**PROVED from the definitions.** Write \(\mathcal C=\mathcal F_+\),
\(\chi(s)=\pi^{s-1/2}\Gamma((1-s)/2)/\Gamma(s/2)\),
\(m(s)=\pi^{-s/2}\Gamma(s/2)\), and
\[
\widehat f(s)=\int_0^\infty f(x)x^{-s}\,dx,\qquad M_f(s)=m(s)\widehat f(s).
\tag{7}
\]
The transform is the **right** Mellin transform; \(\mathcal C\) is a real unitary involution with kernel \(2\cos(2\pi xy)\). These exact conventions are in `refs/src/math/0112254/fzforumc.tex:2134–2171`. The spaces in the conjecture are \(L_a\): both functions and cosine transforms are constant below \(a\), whereas \(K_a\) requires both constants to vanish (`refs/src/math/0203120/main.tex:413–434`). In \(L_a\), \(M_f\) is meromorphic with possible simple poles at 0 and 1, and
\[
M_{\mathcal C f}(s)=M_f(1-s),\qquad
\langle f,\overline{Y^a_{s,k}}\rangle=M_f^{(k)}(s).
\tag{8}
\]
Byte sources: `refs/src/math/0203120/main.tex:460–484`; equivalently `refs/src/math/0112254/fzforumc.tex:2416–2475`, where these augmented-space evaluators are called \(W\), not \(Y\). Thus the conjecture's \(Y\) notation comes from **0203120**, whose title is *Two complete and minimal systems associated with the zeros of the Riemann zeta function* ([primary metadata](https://arxiv.org/abs/math/0203120)); 0112254 is *On Fourier and Zeta('s)* (`refs/src/math/0602425/main.tex:5306–5309`). The gamma factor in (7) is already included in \(Y\).

**PROVED (entire-function repair).** Put \(p(s)=s(s-1)\). The space
\[
\mathscr H_a=\{F_f(s)=p(s)M_f(s): f\in L_a\},\qquad \|F_f\|=\|f\|_{L^2(dx)}
\tag{9}
\]
is a de Branges space with symmetry axis \(\Re s=1/2\) and positive side \(\Re s>1/2\). Here is a verification, so no identification with the unaugmented space is smuggled in. Evaluation continuity, including the removed poles, follows from (8) and the bounded residue functionals. The antiunitary \(\mathcal A f=\mathcal C\overline f\) induces \(F^\#(s)=\overline{F(1-\bar s)}\), since \(p(1-s)=p(s)\). If \(F_f(w)=0\), the division theorem `refs/src/math/0203120/main.tex:711–730` gives \(\widehat f(s)/(s-w)\in\widehat L_a\). Multiplication by \((s-(1-\bar w))/(s-w)\) therefore preserves the space and the norm, as this factor has modulus one on the symmetry line. These are precisely the axioms stated in `refs/src/math/0208121/main.tex:125–147`, which supply an isometric structure function \(E_a^L\). There are no common zeros: repeated division of a nonzero entire function would contradict its finite order of vanishing at a proposed common zero. In particular the structure function can have no zero on the symmetry line.

The space of \(M_f\) for \(f\in K_a\) is already entire and de Branges (`refs/src/math/0112254/fzforumc.tex:2289–2305`). It has a different structure function \(E_a^K\). In fact \(\dim(L_a/K_a)=2\) (`refs/src/math/0203120/main.tex:760–776`). Using \(E_1^K\) as the structure function for the conjecture's evaluators would change the space.

### 2. The kernel and its variable

**PROVED.** Choose \(E=E_a^L\) real on the real \(s\)-axis, so \(E^\#(s)=E(1-s)\), and use Burnol's measure \(|ds|/(2\pi)\). The existence of this choice and the kernel formula are byte-cited at `refs/src/math/0208121/main.tex:150–181`. If \(v_s=\overline{Y^a_{s,0}}\), then
\[
G_{ij}=\langle v_{s_i},v_{s_j}\rangle
=\frac{\overline{E(s_i)}E(s_j)-\overline{E^\#(s_i)}E^\#(s_j)}
{(\bar s_i+s_j-1)\overline{p(s_i)}p(s_j)},
\tag{10}
\]
with removable diagonal values taken by differentiation. Indeed the reproducer for \(F_f(s_i)\) corresponds to \(\overline{p(s_i)}v_{s_i}\). Multiplication by \(R\) is unitary and leaves this Gram unchanged. Derivative evaluators for \(M\) are the derivatives of the kernel divided by \(p\), hence triangular combinations of the entire-space derivative kernels, not merely a common scalar times every jet.

For comparison with the usual upper-half-plane formula, set
\[
z=\frac{i}{2}(s-\tfrac12),\quad s=\tfrac12-2iz,\quad
\mathcal E(z)=E(\tfrac12-2iz),\quad d_s=-\tfrac14+i\bar z.
\tag{11}
\]
Critical zeros map to **real** \(z=-\gamma/2\). The standard de Branges kernel with norm \(\int|F/\mathcal E|^2du\) is
\[
K(w,z)=\frac{\mathcal E(z)\overline{\mathcal E(w)}-
\mathcal E^\#(z)\overline{\mathcal E^\#(w)}}{2\pi i(\bar w-z)}.
\tag{12}
\]
The sign is positive: for \(\mathcal E(z)=z+i\), (12) equals \(1/\pi\). Burnol's change of measure gives \(|ds|/(2\pi)=du/\pi\), so the same \(\mathcal E\) in the transported space has kernel \(\pi K\). Formula (10) is that normalization in \(s\). The rotation in (11) is also explicitly suggested in `refs/src/math/0112254/fzforumc.tex:2300–2305`.

**REFUTED (the proposed rank-two numerator).** Put \(x_{ij}=\bar s_i+s_j\). The multiplier converting (10) to the conjecture's loss matrix is
\[
N_{ij}=\frac{2-x_{ij}}{2(x_{ij}-1)}\,
\frac{\overline{E(s_i)}E(s_j)-\overline{E^\#(s_i)}E^\#(s_j)}
{\overline{p(s_i)}p(s_j)}.
\tag{13}
\]
It is **not constant**. Its removable values use (10), not separate evaluation of the singular prefactor. The de Branges denominator measures distance from \(\Re s=1/2\); the decay eigenvalue measures distance from \(\Re s=1\). Consequently \(N\) is not generally a difference of two rank-one forms.

**PROVED (the isolated linear-algebra lemma).** For \(a\ne0\), \(aa^*-cc^*\) is positive of rank one iff \(c=\lambda a\) with \(|\lambda|<1\). Positivity tested on \(a^\perp\) forces \(c\perp a^\perp\); substitution proves the rest. This is true even in dimension one, but (13) prevents its application here. At every critical-line point \(|E^\#/E|=1\), not less than one.

### 3. The structural fact needed for T4

**PROVED.** Every Gram entry in (10) is real when \(s_i,s_j\) lie on the critical line. A proof independent of the structure function is stronger: (8) implies
\[
M_{\mathcal A f}(s)=\overline{M_f(1-\bar s)},\qquad
\mathcal A v_s=v_s\quad(\Re s=1/2).
\tag{14}
\]
The second identity follows by uniqueness of the Riesz representative and antiunitarity. Hence
\(\langle v_s,v_t\rangle=\langle\mathcal A v_s,\mathcal A v_t\rangle
=\overline{\langle v_s,v_t\rangle}\).
No RH, de Branges formula, or explicit Fredholm determinant is required.

**SHARPENED (source scope).** The C. R. note is actually the locally available 2002 paper **0208121**, not a missing 2003 paper (`refs/src/math/0112254/fzforumc.tex:3395–3397`). Its explicit cosine-space structure function is at `refs/src/math/0208121/main.tex:393–402`. Paper **0602425** treats the different kernel \(J_0(2\sqrt{xy})\) and the factor \(\Gamma(1-s)/\Gamma(s)\), as its own abstract states (`refs/src/math/0602425/main.tex:110–127`; [primary metadata](https://arxiv.org/abs/math/0602425)). Those closed Hankel formulae cannot be transplanted into the cosine \(L_1\) problem. The cosine functional equation is also verified for distributions in `refs/src/math/0407443/main.tex:709–719`; the distinction between real \(\Gamma(s/2)\) and complex \(\Gamma(s)\) archimedean factors appears explicitly in `refs/src/math/9809119/main.tex:194–200`.

## T4 — REFUTED: H-THETA-1 in Burnol's norm

### 1. An exact three-point obstruction

**PROVED.** Let \(e_1,e_2,e_3\) be nonzero vectors with a real Gram matrix and prescribe \(d_i=-a+ib_i\), where \(a>0\) and the three \(b_i\)'s are distinct. Then \(N_{ij}=-(d_i+\bar d_j)G_{ij}\) cannot be positive of rank one.

If it were, write \(N_{ij}=c_i\bar c_j\). Its diagonal is positive, so every \(c_i\ne0\), hence every \(G_{ij}\ne0\). But the cyclic product must satisfy
\[
N_{12}N_{23}N_{31}=|c_1c_2c_3|^2>0.
\tag{15}
\]
Put \(q_{ij}=b_j-b_i\), so \(q_{12}+q_{23}+q_{31}=0\). Direct multiplication gives
\[
\Im\!\left[(2a+iq_{12})(2a+iq_{23})(2a+iq_{31})\right]
=-q_{12}q_{23}q_{31}\ne0.
\tag{16}
\]
Multiplication by the nonzero real number \(G_{12}G_{23}G_{31}\) cannot make this product real. This contradicts (15). If any off-diagonal Gram entry is zero, rank one already contradicts the positive diagonal. This exhausts all cases.

Apply (14) with any three distinct critical-line zeta zeros, \(a=1/4\), \(b_i=-\gamma_i/2\). Such zeros exist unconditionally; the first three specified in the brief suffice. Simplicity is unnecessary: the \(k=0\) vector at a multiple zero is still an eigenvector. The evaluators are nonzero (indeed all finite subfamilies are independent) by the complete minimal theorem at level one, `refs/src/math/0203120/main.tex:516–524`. Thus no scalar exit form exists even on these three ordinary evaluators. No closure, domain extension, regular dilation, or treatment of the remaining zeros can repair this finite contradiction.

**Verdict: `conj:h-theta-1` is REFUTED unconditionally in its stated Sonine norm.** The proof refutes its scalar-exit requirement; alone it does not refute contractivity without a scalar exit.

### 2. What happened to the proposed structure-function question

**REFUTED as a route to the conjecture.** A common ratio of modulus less than one is already excluded by a single critical-line point: \(|E_1^\#/E_1|=1\). Nonconstancy of the phase is not needed for the three-point proof. Constancy, if it happened on a finite set, would give orthogonal boundary evaluators by (10), which still fails the scalar-exit test. Numerical phase and Gram values, using an explicit normalization of the correct augmented-space structure function, are supplied below; there is no appeal to the intuition that the structure function “has nothing to do” with zeta.

### 3. A computable Gram formula for the correct space

**PROVED (compact-resolvent scheme).** This is an elementary augmented-space version of the two-projection method in `refs/src/math/0208121/main.tex:259–290,318–327`. It computes \(L_1\), not \(K_1\). All the integrals below are on \((0,1)\). Let \(P\) restrict to this interval, \(Q=P-|1_{(0,1)}\rangle\langle1_{(0,1)}|\), and
\[
T=Q\mathcal C Q\quad\hbox{on }L^2_0(0,1),\qquad
q_s(x)=\frac{1_{x<1}}{1-s}+x^{-s}1_{x>1}.
\]
For \(\Re s>1/2\), \(q_s\in L^2\). The orthogonal complement of \(L_1\) is the range of
\(D(u,v)=u+\mathcal Cv\), \(u,v\in L^2_0(0,1)\), and
\[
D^*D=\begin{pmatrix}I&T\\T&I\end{pmatrix},\qquad
D^*q_s=(0,r_s),\quad r_s=Q\mathcal Cq_s.
\]
The operator \(T\) is compact and has norm less than one: equality would give a nonzero compactly supported function with compactly supported Fourier transform; its entire Fourier extension rules that out. Thus the range is closed, \(I-T^2\) is invertible, and projection gives the **bilinear**, uncompleted kernel
\[
H(s,t)=\frac1{(1-s)(1-t)}+\frac1{s+t-1}
-\int_0^1r_s(x)[(I-T^2)^{-1}r_t](x)\,dx.
\tag{17}
\]
Initially \(\Re s,\Re t>1/2\). This follows by subtracting
\(D(D^*D)^{-1}D^*\) from the identity; the lower-right block of the inverse is \((I-T^2)^{-1}\). It proves both the sign and the absence of an extra factor two.

One well-conditioned continuation avoids a diagonal infinity-minus-infinity. Fix \(t=2\), solve the single real integral equation
\[
v=(I-T^2)^{-1}r_2,
\]
then continue (17) in \(s\) using
\[
\mathcal Cq_s(x)=\frac{\sin(2\pi x)}{\pi x(1-s)}+
\chi(s)x^{s-1}-2\sum_{n=0}^{\infty}
\frac{(-1)^n(2\pi x)^{2n}}{(2n)!(2n+1-s)}.
\tag{18}
\]
For \(0<\Re s<1\), (18) follows from the cosine transform of \(x^{-s}\) and subtraction of its integral on \((0,1)\); elsewhere use continuation at removable values. In particular it is regular at \(s=2\), with \(\chi(2)=-2\pi^2\). Since \(v\) has mean zero, \(\int r_s v=\int(\mathcal Cq_s)v\). The solution \(v\) is smooth, and the only endpoint singularity in this integral is the integrable \(x^{s-1}\); thus (17) continues to \(\Re s>0\) away from its stated poles.

Let
\[
F(s)=p(s)p(2)m(s)m(2)H(s,2),\qquad
b=\sqrt{3F(2)},\qquad E_*(s)=\frac{(s+1)F(s)}b.
\tag{19}
\]
This is a structure function for (9), with the explicit normalization
\(E_*(2)=b>0\), \(E_*(-1)=0\). To see this, start with any real structure function \(E\). At 2 it has real values \(a=E(2),c=E(-1)\), with \(a^2-c^2=3F(2)>0\). The real hyperbolic change
\(E_*=(aE-cE^\#)/\sqrt{a^2-c^2}\) preserves its kernel and Hermite–Biehler inequality; the kernel at 2 gives exactly (19). This also proves its entire continuation without guessing a Fredholm determinant.

The desired Gram is now (10) with \(E=E_*\), including the diagonal limit
\[
G_{ii}=\frac{E_*(\bar\rho_i)E_*'(\rho_i)+
 E_*(1-\bar\rho_i)E_*'(1-\rho_i)}{|p(\rho_i)|^2}
\quad(\Re\rho_i=1/2).
\tag{20}
\]
Thus (17)–(20) are a convergent, fully specified substitute for a closed form. A particularly stable integration rule expands \(v\) in shifted Legendre polynomials and uses the exact moment
\[
\int_0^1x^{s-1}P_n(2x-1)\,dx
=\frac1s\prod_{k=1}^n\frac{s-k}{s+k}.
\tag{21}
\]
Integration by parts in Rodrigues' formula proves (21), first for \(\Re s>n\), then for \(\Re s>0\) by continuation. Polynomial cosine-kernel approximations converge in operator norm; since \(\|T\|<1\), their resolvents converge. The smooth anchor solution and (21) then give convergent scalar integrals, locally uniformly near the three points and for their derivatives. This gives a certifiable scheme independently of any floating-point implementation.

**Numerical check, not used as proof.** `checks/sonine.py` implements this scheme with 45-digit scalar arithmetic and double-precision Gauss–Legendre linear algebra. At 24, 40 and 64 nodes the displayed results agree to substantially more digits than the eight retained here. In the normalization (19), at the three zeros in the brief,
\[
\frac{E_*^\#(\rho_n)}{E_*(\rho_n)}\simeq
\begin{cases}
-0.99880741-0.04882370i,&n=1,\\
-0.99983369+0.01823721i,&n=2,\\
-0.99790571-0.06468528i,&n=3.
\end{cases}
\tag{22}
\]
All have modulus one, as required. The normalized Sonine Gram and its loss spectrum are
\[
O\simeq\begin{pmatrix}
1&-0.12772518&-0.01980716\\
-0.12772518&1&0.19503489\\
-0.01980716&0.19503489&1
\end{pmatrix},\qquad
\operatorname{spec}(-(d_i+\bar d_j)O_{ij})
\simeq(-0.09239752,\ 0.46931541,\ 1.12308212).
\tag{23}
\]
**OPEN (only the stronger numerical assertions as certified theorems).** These computations strongly indicate distinct phases and failure even of dissipativity. A rigorous enclosure of the resolvent and scalar evaluations in (17)–(21) is still required to register either numerical conclusion as a proved theorem. Neither is required for the exact scalar-exit refutation (15)–(16). The statement that the ratio is constant with modulus less than one is already analytically refuted; constancy with arbitrary modulus on all zeros is numerically refuted by (22), but is not asserted here as an interval-certified result.

## T5 — SHARPENED: classification, not a unique numerical norm

**PROVED.** On an algebraically independent family of simple modes with prescribed distinct \(d_i\), all Hilbert norms satisfying the scalar-exit tests are exactly
\[
G_{ij}=\frac{c_i\bar c_j}{-(d_i+\bar d_j)},\qquad c_i\ne0.
\tag{24}
\]
If every finite loss matrix is positive of rank one, the factors can be chosen coherently: fix an index 0, set \(c_0=\sqrt{N_{00}}\) and \(c_i=N_{i0}/c_0\); rank-one minors give (24). T1 constructs the completion and semigroup. Conversely T1 proves necessity. The phase of the entire family \(c\) is irrelevant; otherwise there is genuine diagonal freedom in the norm. There is no unique norm on the *fixed named vectors*.

Under the notebook transform the completion is the closed span of kernels at \(w_i=i\bar d_i\). When these points satisfy the Blaschke condition it equals \(K_B\), for the Blaschke product having precisely this divisor: an element perpendicular to the kernels vanishes on the divisor and its quotient by \(B\) is in \(H^2\). With multiple zeros use all jets and (3)–(4); the freedom is the exit values on the chain, a triangular change within each root space. For the zeta divisor the Blaschke condition and the absence of a singular or delay factor were proved in 04q, `thm:symbol-edge-quotient`. Consequently the full model is \(K_S\) **unconditionally**, if multiplicities are included; with only simple-mode vectors this conclusion assumes that the full zero set is simple. RH is unnecessary. No unspecified outer multiplier is required.

The map (2) constructs an abstract mode-preserving unitary. It does not prove a bounded identification with Burnol's existing norm, nor prescribe an arithmetic or geometric construction of that map. Thus “empty” is an interpretation of an inverse problem where the norm is freely defined; the precise mathematical conclusion is (24), not literal uniqueness of a norm. The substantive prescribed-norm assertion H-THETA-1 is refuted by T4.

## T6 — SHARPENED: bad-zero renewal, with the clock and reset specified

### 1. The finite synthetic model and its two time orientations

**DEFINITION (synthetic data).** Start with finitely many hypothetical right-hand zeros \(\rho_i=\sigma_i+i\gamma_i\), \(1/2<\sigma_i<1\), including their conjugates and multiplicities. The full hypothetical zeta set also includes \(1-\rho_i,1-\bar\rho_i\). The Blaschke factor \(B_{\rm bad}\) includes **only** the right-hand zeros, not their left-hand partners. This is Burnol's rule `refs/src/math/0001013/main.tex:628–631`, transported in 04q. Set
\[
\delta_i=\sigma_i-\tfrac12,\quad \beta_i=\delta_i/2,\quad a_i=\gamma_i/2,\quad
w_i=a_i+i\beta_i,\qquad
B(z)=\prod_i\frac{z-w_i}{z-\bar w_i}.
\tag{25}
\]
Pairing \(\gamma\) and \(-\gamma\) gives \(B(-\bar z)=\overline{B(z)}\) and \(B(0)=1\). “Real on the axis” means this real-structure symmetry; it does not mean that every boundary value on the real axis is real.

**PROVED.** On \(K_B\), forward compression is \(Z_t=P_{K_B}U_t|_{K_B}\). Its ordinary eigenvectors and Gram are
\[
h_i(z)=\frac{B(z)}{z-w_i},\quad Z_th_i=e^{iw_it}h_i,\quad
d_i^+=iw_i=-\beta_i+ia_i,\quad
\langle h_i,h_j\rangle=\frac{i}{w_i-\bar w_j}.
\tag{26}
\]
For the eigenvalue identity, subtract \(e^{iw_it}h_i\); the difference belongs to \(BH^2\). The Gram follows by a single residue or by the model conjugation \(F\mapsto B\bar F\), which sends \(k_{w_i}\) to \(h_i\). The adjoint compression \(C_t\) has \(k_{w_i}\), eigenvalues \(-i\bar w_i\), as in T2. Both orientations decay at rate \(\beta_i\), and both have a scalar generator exit. Choose its phase so \(j_+h_i=1\); for normalized forward modes the amplitude is \(\sqrt{2\beta_i}=\sqrt{\delta_i}\). Formula (1) proves the exit identity for (26); polarization extends it to the finite-dimensional space. For repeated points differentiate the root vectors, giving one chain per repeated zero.

**REFUTED (finite-time rank one).** The exact finite-time loss is
\[
I-Z_t^*Z_t=\int_0^t Z_s^*j_+^*j_+Z_s\,ds=J_t^*J_t,
\quad (J_tf)(s)=j_+Z_sf\in L^2(0,t).
\tag{27}
\]
For every \(t>0\) it is positive definite on a nonzero finite model, so has rank \(\dim K_B\). Indeed if its quadratic form is zero, the scalar exponential polynomial \(j_+Z_sf\) vanishes on an interval, hence everywhere. Integration to infinity and stability give \(\|f\|^2=0\). The exit is one scalar **per instant**; its history on an interval is not one scalar. This is precisely why the discrete disk-shift statement in 04l cannot be applied unchanged to sampled continuous time.

### 2. Continuous holding times and stationary states

**DEFINITION.** For a density \(\Omega\) on a nonzero finite \(K_B\), the continuous renewal generator is
\[
\mathcal L_\Omega(\varrho)=A\varrho+\varrho A^*
+\operatorname{Tr}(j_+\varrho j_+^*)\Omega,
\quad A=\left.\frac d{dt}Z_t\right|_{t=0}.
\tag{28}
\]
This is the continuous counterpart of 04l's fixed reset, already defined in 04h. Factoring \(\Omega\) into pure states makes (28) a finite-dimensional Lindblad generator; its anticommutator term is correct because \(A+A^*=-j_+^*j_+\).

**PROVED.** Its holding density, mean, and unique stationary density are
\[
S_\Omega(t)=\operatorname{Tr}(Z_t\Omega Z_t^*),\quad
m_\Omega(t)=-S_\Omega'(t)=\operatorname{Tr}(j_+Z_t\Omega Z_t^*j_+^*),
\]
\[
\bar t=\int_0^\infty S_\Omega(t)\,dt,\quad
X=\int_0^\infty Z_t\Omega Z_t^*dt,\quad
\varrho_\infty=X/\operatorname{Tr}X.
\tag{29}
\]
Stability and finite dimension prove convergence, total holding probability one, and \(AX+XA^*=-\Omega\). Taking traces gives unit exit flux for \(X\), proving stationarity. Conversely any stationary density satisfies the same Lyapunov equation with right side a scalar times \(-\Omega\); integration along \(Z_t\) yields a scalar times \(X\). Trace one fixes that scalar. This proves uniqueness without a faithfulness or irreducibility assumption.

For simple modes use the forward basis in (26), put
\(\alpha_{ij}=-(d_i^++\bar d_j^+)=(\delta_i+\delta_j-i(\gamma_i-\gamma_j))/2\), and write
\(\Omega=\sum q_{ij}|h_i\rangle\langle h_j|\), \(q\ge0\). Here \(|u\rangle\langle v|\) sends \(f\) to \(\langle f,v\rangle u\), so its trace is \(\langle u,v\rangle\), in our convention. Explicitly,
\[
\sum_{ij}\frac{q_{ij}}{\alpha_{ij}}=1,\qquad
S_\Omega(t)=\sum_{ij}\frac{q_{ij}}{\alpha_{ij}}e^{-\alpha_{ij}t},\qquad
m_\Omega(t)=\sum_{ij}q_{ij}e^{-\alpha_{ij}t},\qquad
\bar t=\sum_{ij}\frac{q_{ij}}{\alpha_{ij}^2}.
\tag{30}
\]
This is the general rational formula; it depends on the reset, including its coherences. For a modal mixture of normalized eigenvectors with weights \(p_i\), it reduces to
\[
\bar t=\sum_i\frac{p_i}{\delta_i},\qquad
\varrho_\infty=\frac{\sum_i(p_i/\delta_i)|\widetilde h_i\rangle\langle\widetilde h_i|}
{\sum_i p_i/\delta_i}.
\tag{31}
\]
The weights alone do not give the density's spectrum, because the modes need not be orthogonal.

For **one** zero the reset is unique: \(m(t)=\delta e^{-\delta t}\), \(\bar t=1/\delta\). A singleton with nonzero \(\gamma\) omits the reality partner and is a legitimate complex model, not the real synthetic zeta set. For **two** distinct zeros the completely general formula is
\[
\bar t=\frac{q_{11}}{\delta_1^2}+\frac{q_{22}}{\delta_2^2}
+8\Re\frac{q_{12}}{(\delta_1+\delta_2-i(\gamma_1-\gamma_2))^2},
\]
\[
\frac{q_{11}}{\delta_1}+\frac{q_{22}}{\delta_2}
+4\Re\frac{q_{12}}{\delta_1+\delta_2-i(\gamma_1-\gamma_2)}=1.
\tag{32}
\]
For a conjugate pair \((\sigma,\pm\gamma)\) every modal mixture has mean \(1/\delta\). A coherent reset need not. For multiple zeros (29) remains valid and its entries are integrals of polynomials times exponentials, evaluated by \(\int_0^\infty t^n e^{-\alpha t}dt=n!/\alpha^{n+1}\).

### 3. The discrete formula in the brief

**SHARPENED.** Specify a step \(\Delta>0\). With \(Z=Z_\Delta\), \(J=J_\Delta\) from (27), the displayed channel in the brief is CPTP and has the unique stationary state
\[
\mathcal E_\Omega(\varrho)=Z\varrho Z^*+
\operatorname{Tr}[(I-Z^*Z)\varrho]\Omega,\quad
\varrho_\infty^{\rm disc}=\frac{\sum_{n\ge0}Z^n\Omega Z^{*n}}{\bar n},
\quad
\bar n=\sum_{ij}\frac{q_{ij}}{\alpha_{ij}(1-e^{-\alpha_{ij}\Delta})}.
\tag{33}
\]
The same telescoping and geometric-series proof establishes all three assertions. The physical mean is \(\Delta\bar n\), not (30); even the one-zero formula is \(\Delta/(1-e^{-\delta\Delta})\), which is not rational in \(\sigma,\gamma\).

If a **discrete scalar** exit and a rational modal mean are desired, define instead the Cayley cogenerator, for \(h>0\),
\[
V=(I+hA)(I-hA)^{-1},\qquad
I-V^*V=2h(I-hA^*)^{-1}j_+^*j_+(I-hA)^{-1}.
\tag{34}
\]
This has rank one, eigenvalues \((1+hd_i^+)/(1-hd_i^+)\), and the fixed-reset theorem of 04l applies literally. A modal reset has mean in **Cayley steps**
\[
\bar n_{\rm Cayley}=\sum_i p_i
\frac{(1+h\delta_i/2)^2+h^2\gamma_i^2/4}{2h\delta_i}.
\tag{35}
\]
This is a separately defined clock, not a formula for holding time under the regular forward dilation. One or two modes are obtained by keeping one or two terms. Equation (34) follows by expanding the difference of the two squared factors \((I-hA)\) and \((I+hA)\).

### 4. The boundary limit

**PROVED, with its topology specified.** For one mode, \(\bar t=1/(\sigma-1/2)\) exactly. As \(\delta\downarrow0\), its normalized physical wave \(\sqrt\delta e^{-\delta X/2-iaX}1_{X>0}\) tends weakly to zero: test first against compactly supported functions, then use density. Thus its rank-one projection tends strongly to zero. A fixed finite collection with distinct limiting ordinates has the same projection limit, because its normalized Gram tends to the identity. The limiting Blaschke function is 1 and its model space is \(\{0\}\).

**REFUTED (a density channel on a zero-dimensional bond).** There is no trace-one density and no reset on \(\{0\}\). If instead one identifies each one-dimensional moving mode space with \(\mathbb C\) before taking the limit, the no-event semigroup tends to a unitary phase and the density dynamics tends to the identity on a **one-dimensional** space; indeed its reset density channel was already the identity. These are different limits. “Under RH the bad-zero model is absent” is a precise consequence of the definition and Burnol's closure theorem, not a limiting renewal channel with a stationary state on \(\{0\}\).

## T7 — SHARPENED: a damped length-two chain, not two constant terms

### 1. The actual physical model

**PROVED.** With \(\beta=1/4\), \(v_+(z)=(z-i\beta)/(z+i\beta)\),
\[
\mathcal F^{-1}K_{v_+^2}
=\operatorname{span}\{e^{-\beta X},Xe^{-\beta X}\}1_{X>0}
=\operatorname{span}\{y^{-1/4},(\log y)y^{-1/4}\}1_{y>1}.
\tag{36}
\]
The zero is \(w=i\beta\) of order two, so its kernels are \((z+i\beta)^{-1}\) and \((z+i\beta)^{-2}\); their inverse transforms are \(-ie^{-\beta X}\) and \(-Xe^{-\beta X}\). The derivative identity follows by differentiating the elementary Laplace integral. These two independent vectors span because the Blaschke degree is two.

**REFUTED (both proposed undamped identifications).** Neither \(1_{y>1}\) nor \((\log y)1_{y>1}\) is in the bond \(L^2(dy/y)\). The pair \(1_{y>1},y^{-1/2}1_{y>1}\) is therefore not this model either. In Burnol's original \(L^2(dx)\) coordinates, applying \(R^{-1}\) to (36) gives the span of \(x^{-1}1_{x>1}\) and \((\log x)x^{-1}1_{x>1}\), up to nonzero constants.

The error comes from mixing the two zero dictionaries. For the bad-zero dictionary \(w=\gamma/2+i(\sigma-1/2)/2\), \(w=i/4\) corresponds formally to \((\sigma,\gamma)=(1,0)\) and its kernel wave is \(-iy^{-(\sigma-1/2)/2-i\gamma/2}\). The formula \(-iy^{-(1-\sigma)/2-i\gamma/2}\) quoted in the brief is the **different Riemann-channel** dictionary. In that dictionary \(w=i/4\) corresponds to \(\sigma=1/2\), not 1.

### 2. Matrices, exit, holding law

**PROVED.** An orthonormal basis in \(X\)-space is
\[
b_0=\sqrt{2\beta}e^{-\beta X},\qquad
b_1=\sqrt{2\beta}(1-2\beta X)e^{-\beta X}.
\]
Integrating the first three exponential moments proves orthonormality. Backward translation and forward compression respectively have
\[
A_C=\begin{pmatrix}-\beta&-2\beta\\0&-\beta\end{pmatrix},\quad
C_t=e^{-\beta t}\begin{pmatrix}1&-2\beta t\\0&1\end{pmatrix},\qquad
A_Z=A_C^*,\quad Z_t=C_t^*.
\tag{37}
\]
Their scalar generator exit can have the same row
\[
j=\sqrt{2\beta}(1,1),\qquad -(A_C+A_C^*)=j^*j=2\beta\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\tag{38}
\]
In particular the eigenvalue is \(-1/4\) in both orientations and the off-diagonal entry is \(-1/2\). The finite-time loss for \(C_t\) is
\[
I-C_t^*C_t=
I-e^{-2\beta t}\begin{pmatrix}1&-2\beta t\\-2\beta t&1+4\beta^2t^2\end{pmatrix}.
\tag{39}
\]
Its determinant is \((1-e^{-2\beta t})^2-(2\beta t)^2e^{-2\beta t}>0\) for \(t>0\), since \(2\sinh(\beta t)>2\beta t\). Thus even this two-dimensional example directly refutes finite-time rank one.

**PROVED (all reset laws, explicitly conditional on the reset).** For backward translation, let the density in this orthonormal basis be
\(\Omega=\begin{pmatrix}p&c\\\bar c&1-p\end{pmatrix}\), \(0\le p\le1\), \(|c|^2\le p(1-p)\). Matrix multiplication gives
\[
S_\Omega(t)=e^{-2\beta t}[1-4\beta t\Re c+4\beta^2t^2(1-p)],
\]
\[
m_\Omega(t)=2\beta e^{-2\beta t}
[p+(1-p)(1-2\beta t)^2+2\Re c(1-2\beta t)],\qquad
\bar t=\frac{1+2(1-p)-2\Re c}{2\beta}.
\tag{40}
\]
For forward compression swap \(p\) and \(1-p\); the real part of \(c\) is unchanged. The first basis vector reset for \(C_t\) has mean 2 and law \(\tfrac12e^{-t/2}\); the second has mean 6 and law \(\tfrac12e^{-t/2}(1-t/2)^2\). A Jordan block therefore does not prescribe a unique holding law.

A concrete symmetric choice is the **defined** exit reset \(\Omega_j=j^*j/\operatorname{Tr}(j^*j)=\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\). For either orientation it gives
\[
S_j(t)=e^{-t/2}(1-t/2+t^2/8),\qquad
m_j(t)=e^{-t/2}(1-t/4)^2,\qquad \bar t_j=2,\qquad
\varrho_\infty=I_2/2.
\tag{41}
\]
The last equality also follows without integration: \(A+A^*=-j^*j\) implies
\(\int_0^\infty e^{tA}j^*je^{tA^*}dt=I\). T6 proves uniqueness. No assertion that arithmetic selects this reset is made.

### 3. Where the square comes from, and the even-sector dictionary

**PROVED from the source definitions.** Burnol defines \(A\) as convolution with \(\sqrt{|u|}1_{|u|\le1}\) in the number-field case and \(V=1-A\) (`refs/src/math/0001013/main.tex:275–288`); his multiplier is \((s-1)/s\) (`refs/src/math/0001013/main.tex:586–595`). His two radiation identifications contain the factors \(V^{-1}B\) and \(VB^{-1}\), respectively. Consequently
\[
S=(V^{-1}B)^{-1}(VB^{-1})=V^2B^{-2};
\qquad S=ZV^2B^{-2}\text{ adelically, with }Z=1\text{ over a number field}.
\tag{42}
\]
The Euclidean identity is `refs/src/math/0001013/main.tex:500–514`; the adelic one and the meaning of \(Z\) are `refs/src/math/0001013/main.tex:682–699`. This \(Z\) is an elementary unitary multiplier, not our compressed \(Z_t\). The square comes from the quotient of the incoming and outgoing identifications. It is not an instruction to apply \(V\) twice to one theta vector. Burnol's earlier scattering discussion also explicitly defines scattering as the quotient of two intertwiners (`refs/src/math/9911175/main.tex:133–144`).

In the outgoing variable \(s=1/2-2i\tau\), \((s-1)/s=v_+(\tau)\). It has one zero \(s=1\) and its reflected pole \(s=0\); squaring doubles this **one Blaschke factor**, giving a single length-two chain. By contrast 04r, `prop:siegel-constant-term`, gives
\[
\varphi_E(\tfrac12+i\tau)=r(\tau)/\Theta(\tau),\qquad
r(\tau)=\frac{\tau-i/2}{\tau+i/2}.
\tag{43}
\]
The elementary \(r\) has one upper-half-plane zero, so \(\dim K_r=1\); its physical model is \(\operatorname{span}\{y^{-1/2}1_{y>1}\}\) with eigenvalue \(-1/2\). “One dimension per pole” must not count both the upper zero and its reflected lower pole as two independent modes. Also \(\xi\) itself is entire; the poles at 0 and 1 belong to the meromorphic completed zeta/the theta Mellin transform, with \(\xi\)'s factors having removed them.

**REFUTED (invisibility of the second endpoint).** In the unreflected theta variable \(s=1/2+2i\tau\), the completed theta transform has poles at \(\tau=i/4\) for \(s=0\) and at \(\tau=-i/4\) for \(s=1\). The unweighted constant terms are 1 and \(y^{-1/2}\), respectively. After the unitary symmetric weighting their asymptotic tails are \(y^{1/4}\) at zero and \(y^{-1/4}\) at infinity. Both are present: the Euclidean source formula explicitly gives a constant endpoint term near zero and an inverse-linear tail at infinity (`refs/src/math/0001013/main.tex:464–475`); its adelic subtraction is `refs/src/math/0001013/main.tex:204–207`. The Euclidean and adelic images differ by normalization and weighting, not by deletion of one of these two endpoint poles. Reflection transports the two ends into the common outgoing representation; their radiation normalizations yield (42). Thus the two graded theta constant terms, a double Blaschke zero, and two endpoint poles are three distinct notions.

**The corrected even-sector dictionary is PROVED:** GL\(_1\) Burnol scattering under RH has elementary symbol \(v_+^2\), degree two, eigenvalue \(-1/4\), and one length-two chain (36); the GL\(_2\) Eisenstein elementary factor is \(r\), degree one, eigenvalue \(-1/2\). Neither assertion identifies those model spaces with the formal two-dimensional graded span of the unweighted theta constant terms. Away from RH, \(v_+^2B_{\rm bad}^{-2}\) is not inner; (36) remains the model of its elementary inner factor, not a claimed causal model of the entire non-inner multiplier.

## Numerical checks for the blind lane

Author: codex:gpt-6-astra

**PROVED formulas; numerical expected values.** The following decimals are reproducibility targets, not interval certificates. Use `python3 notes/h-theta-1/checks/sonine.py` and `python3 notes/h-theta-1/checks/check_models.py`. Neither script writes any output files. The latter completed 74 checks; the former used 24, 40 and 64 quadrature nodes and an additional independent anchor at 4. The anchor-4 structure function has different phases, as it should, but returns the same Gram to the displayed accuracy. The scripts recompute the first three zeros with mpmath rather than silently truncating their ordinates to the decimals in the brief.

1. **Zero inputs (24 significant digits):**
   \[
   \gamma_1=14.13472514173469379045725,\quad
   \gamma_2=21.02203963877155499262848,\quad
   \gamma_3=25.01085758014568876321379.
   \]
   Use \(\rho_n=1/2+i\gamma_n\), \(d_n=-1/4-i\gamma_n/2\). For the Riemann channel use \(w_n=\gamma_n/2+i/4\); for the Sonine de Branges variable use the **real** \(z_n=-\gamma_n/2\).

2. **Cauchy Gram, first-slot convention (eight decimals):**
   \[
   G^{\rm mod}\simeq\begin{pmatrix}
   2&0.04129237+0.28439352i&0.01676583+0.18234737i\\
   0.04129237-0.28439352i&2&0.11826854+0.47175165i\\
   0.01676583-0.18234737i&0.11826854-0.47175165i&2
   \end{pmatrix}.
   \]
   Multiply entrywise by \(-(d_i+\bar d_j)\): every entry must be 1. If a coordinate implementation uses \(x^*Hx\), use \(H=(G^{\rm mod})^T\).

3. **Exact obstruction's scalar prefactor:**
   \[
   \prod_{(i,j)=(1,2),(2,3),(3,1)}[-(d_i+\bar d_j)]
   =11.4772516480-37.3489700175i.
   \]
   Its nonzero imaginary part, together with reality of the Sonine Gram, is the analytical test. Zero off-diagonal entries separately preclude rank one with positive diagonal.

4. **Actual completed Sonine evaluator Gram (ten significant digits):**
   \[
   G^{\rm Son}\simeq\begin{pmatrix}
   2.5372715234\,10^{-10}&-1.5861671773\,10^{-13}&-1.0949051346\,10^{-15}\\
   -1.5861671773\,10^{-13}&6.0782412665\,10^{-15}&5.2768178534\,10^{-17}\\
   -1.0949051346\,10^{-15}&5.2768178534\,10^{-17}&1.2043193735\,10^{-17}
   \end{pmatrix}.
   \]
   Normalize **before** testing the loss spectrum; the gamma completion makes the raw diagonal vary by seven orders of magnitude. Recover (23) to eight decimals and the phases (22) in the anchor-2 normalization. The numerical resolvent has \(T\)'s extreme eigenvalues about \(-0.4710777795,0.5623175942\). These are diagnostics, not substituted spectral bounds. The code keeps 24 shifted-Legendre coefficients to suppress double-precision noise; a rigorous implementation should bound its tail instead. Change the anchor from 2 to 4 and verify that the Gram, but not the individual phase values, stays fixed.

5. **A synthetic real bad-zero pair:** take \(\rho_\pm=0.7\pm1.5i\), so \(\delta=0.2\), \(w_\pm=\pm0.75+0.1i\). The continuous modal law is \(0.2e^{-0.2t}\), mean \(5\), for every modal mixture. At sampling step \(\Delta=1\), the mean is \((1-e^{-0.2})^{-1}\); for Cayley parameter \(h=1\) it is \(((1.1)^2+1.5^2/4)/0.4=4.43125\) steps. These clocks give different means.

6. **A coherent two-zero reset:** the script uses \(d=(-0.1+0.75i,-0.2-1.25i)\), \(u=(1,0.3+0.2i)\), and \(q=uu^*/\sum_{ij}(uu^*)_{ij}/\alpha_{ij}\). Equation (30) gives \(\bar t=4.61864473922355\), agreeing with direct integration. Its ordinates correspond to a complex two-mode example; add conjugate partners if imposing the real synthetic-zeta symmetry.

7. **The double elementary zero:** use \(\beta=1/4\). At \(t=1\),
   \[
   I-C_1^*C_1\simeq
   \begin{pmatrix}0.39346934&0.30326533\\0.30326533&0.24183668\end{pmatrix},
   \quad\operatorname{spec}\simeq(0.00505426,0.63025175).
   \]
   Both eigenvalues are positive. For the exit reset, \(S_j(1)=0.379081662320396\), \(m_j(1)=0.341173496088356\), \(\int m_j=1\), \(\bar t_j=2\), and the stationary matrix is \(I_2/2\). For the two basis resets the means are 2 and 6 for \(C_t\), reversed for \(Z_t\).

8. **A jet check:** with \(d=-0.3+0.7i\), \(c_0=1+0.4i\), \(c_1=0.2-0.3i\), integrate the two functions \(q_0=e^{dX}c_0\), \(q_1=e^{dX}(c_1+Xc_0/2)\). Their Gram satisfies (3) with the two lowering coefficients \(1/2\). This checks the brief's particular jet normalization, not a unit-superdiagonal Jordan convention.

## Corrections to the brief

Author: codex:gpt-6-astra

All entries below are **SHARPENED** corrections or **REFUTED** assertions as established in the cited T-section; the remaining certification task is explicitly **OPEN**.

1. The proposed left-half-plane kernel has its pole in the wrong half-plane. Use (2) and its Laplace transform, or the notebook's upper-half-plane kernels.
2. A finite Gram criterion realizes the specified finite dynamics and its minimal dilation up to unitary equivalence; it does not identify the original Sonine embedding inside the bond with the observation embedding.
3. With the first slot linear, the notebook kernel Gram is \(i/(w_j-\bar w_i)\). The commonly used coordinate metric is its transpose.
4. The Cauchy kernels diagonalize the **adjoint** compression. Forward compression uses \(B(z)/(z-w_i)\) and conjugated frequencies.
5. The file 0112254 is not the paper entitled *Two complete and minimal systems*; that paper is 0203120. The conjecture's \(Y\) notation is the latter's. The former calls the augmented-space evaluators \(W\).
6. H-THETA-1 concerns augmented cosine \(L_1\), not vanishing cosine \(K_1\). Their quotient has dimension two. Kernel formulae for the latter cannot simply be substituted for the former.
7. The evaluators already include \(\pi^{-s/2}\Gamma(s/2)\). Passing to an entire augmented space additionally multiplies by \(s(s-1)\); for jets this is triangular, not a single scalar factor.
8. The correct symmetry is \(s\mapsto1-\bar s\). Critical zeros are boundary points of this de Branges space, not interior points with inner ratio of modulus less than one.
9. The generator's denominator is \(2-\bar\rho-\rho'\); the Sonine kernel's denominator is \(\bar\rho+\rho'-1\). Their quotient is not constant, so the asserted difference-of-two-rank-one loss formula is false.
10. The isolated positive-difference lemma is true, but it is inapplicable to the actual loss matrix. On the critical line the diagonal kernel formula also requires a derivative limit.
11. The requested C. R. Sonine note is present as 0208121 and is from 2002. The different 2003 note concerns Dirac and Schrödinger equations.
12. The explicit \(\Gamma(1-s)/\Gamma(s)\) formulae in 0602425 concern a Hankel transform, not this cosine transform. Use (17)–(21) for the correct augmented cosine space.
13. Structure functions are not unique even for a fixed norm. Numerical phase values require a normalization, here (19). Equality versus inequality of phase values is preserved under the corresponding injective disk automorphisms.
14. The conjecture is refuted without assuming RH or simplicity and without numerical Gram values. Any three distinct critical zeros suffice, including the ordinary vector at a multiple zero.
15. The numerical negative loss eigenvalue is stronger evidence than the rank obstruction, but it is not used to label contractivity alone refuted; a certified error enclosure remains open.
16. Cauchy norms have arbitrary nonzero modal scalars (and triangular jet freedom). Their classification does not assert a unique numerical norm on the named evaluators.
17. The identification of the complete Cauchy model with \(K_S\) is unconditional with full multiplicities. RH and an unspecified outer multiplier are unnecessary.
18. The bad-zero Blaschke product includes right-hand zeros and their conjugates, not the left-hand functional-equation partners. Reality is a reflection symmetry, not real-valuedness everywhere on the boundary.
19. Scalar generator loss does not imply scalar finite-time loss. On every nonzero finite model, \(I-Z_t^*Z_t\) has full rank for \(t>0\).
20. A holding time requires a reset and a clock. The continuous generator, sampled fixed-reset channel, and Cayley-step channel have different means. Equations (30), (33), and (35) specify them.
21. For a general reset, coherences contribute to the mean. A zero-only sum without reset weights is not defined; the weighted modal sum is (31).
22. The one-zero mean is exactly \(1/(\sigma-1/2)\) in continuous \(y\)-time. The zero-dimensional limiting model has no density or reset. The identity density dynamics belongs to a different, one-dimensional identification of the moving spaces.
23. The bad-zero kernel exponent and Riemann-channel kernel exponent cannot be interchanged at the pole. The physical model is (36), with \(y^{-1/4}\) damping.
24. An undamped outgoing constant and its logarithm are not bond Hilbert vectors. Nor can the pair of unweighted theta constant terms be identified with this two-dimensional model.
25. The exponent two in Burnol's scattering comes from the quotient of two radiation identifications. Its double zero gives one length-two chain, not two independent eigenvectors.
26. The GL\(_2\) factor \(r\) has degree one: its upper zero and reflected lower pole do not each contribute a mode. The meromorphic completed zeta has the pole pair; \(\xi\) is entire.
27. Burnol's subtraction does not make the other endpoint pole invisible. Both endpoint asymptotics survive in the theta image; reflection and the two radiation maps explain their role.
28. The double elementary zero does not prescribe a reset or a unique holding law. Formula (40) gives all reset laws; (41) is an explicitly chosen exit reset.

## What this changes in the notebook

Author: codex:gpt-6-astra

The following are proposed registrations only; `db/claims.tsv` and the report were not edited.

| Claim / proposed identifier | Status | One-sentence statement to register |
|---|---|---|
| T1 / `thm:continuous-one-exit-cauchy` | `proved` | Stable eigenvalue data admit a scalar-exit realization in a given Gram norm exactly when the loss Gram is positive of rank one, with the derivative version (3) for jets. |
| T2 / `thm:riemann-one-exit-gram` | `proved` | In the notebook measure and first-slot convention, the Riemann kernels have Gram \(i/(w_j-\bar w_i)\) and loss Gram identically one. |
| T3 / `prop:sonine-critical-gram-real` | `proved` | Completed augmented Sonine evaluators at critical-line points are fixed by cosine transform followed by conjugation, hence have a real Gram matrix. |
| T3 / proposed de Branges numerator test | `refuted` | The Sonine kernel denominator and H-THETA-1 decay denominator differ by a half-plane shift, so the loss is not a constant multiple of a rank-two numerator. |
| T4 / `conj:h-theta-1` | `refuted` | Three distinct critical-line zeta evaluators in Burnol's level-one norm cannot satisfy the scalar-exit Gram identity, by the nonreal cyclic-product obstruction. |
| T4 / `prop:sonine-augmented-gram-resolvent` | `proved` | Equations (17)–(21) reconstruct the augmented cosine \(L_1\) evaluator Gram from one compact integral equation on \((0,1)\). |
| T4 / stronger noncontractivity test | `open` | A rigorous enclosure of the first-three-zero Gram is required to upgrade the computed negative loss eigenvalue \(-0.09239752\) to a theorem excluding contractivity itself. |
| T4 / structure-phase nonconstancy | `open` | The explicit anchor-normalized phases (22) are distinct numerically; a certified enclosure would prove their nonconstancy on the zeta zero set. |
| T5 / `thm:sonine-one-exit-norm-classification` | `sharpened` | Every admissible norm is a diagonally rescaled Cauchy norm, with triangular jet freedom, and the completed full zeta divisor gives \(K_S\) without RH. |
| T6 / `thm:gl1-bad-zero-renewal` | `sharpened` | A finite synthetic bad-zero model has scalar instantaneous exit and unique fixed-reset stationary state, with mean (30), while sampled finite-time defects have full model rank. |
| T6 / boundary interpretation | `sharpened` | Bad-zero mode projections can vanish strongly as widths approach zero, but the zero-dimensional limit carries no density renewal channel. |
| T7 / `thm:gl1-bad-zero-defect` part (c), elementary-factor interpretation | `sharpened` | Under RH the degree-two elementary symbol \(v_+^2\) gives a single damped length-two chain, with matrices (37)–(38), rather than a basis of two theta constant terms. |
| T7 / `prop:burnol-even-sector-dictionary` | `proved` | Burnol's two radiation maps produce \(v_+^2\), whereas the Eisenstein elementary factor \(r\) has degree one; neither model is the formal graded span of both unweighted theta constants. |

**Replacement open question on this lead:** Can a certified enclosure of the explicitly computable Sonine Gram exclude even a contraction realization of the prescribed evaluator dynamics when the scalar-exit requirement is dropped?
