# Finite tensor-network and CCM checks

Status: **SKETCH with exact and numerical checks**. The executable checks are
evidence and regression certificates, not promotions of any project claim.

Run from the repository root:

```text
python3 scripts/ccm_tensor_network.py --self-test
python3 -O scripts/ccm_tensor_network.py --self-test
```

Both commands must exit zero. The self-test runs two mutations in temporary
copies and requires both to exit nonzero. The recorded green output is in
`outputs/ccm_tensor_network.txt`.

## 1. Four distinct spaces

⟨1⟩1 **ASSUME.** Let \(B\) be the physical MPS auxiliary space and
\(A_s\in\operatorname{End}(B)\) its letters.

⟨1⟩2 The doubled transfer space is
\(X=B\otimes\overline B\simeq\operatorname{End}(B)\), and the transfer is
\(E=\sum_s A_s\otimes\overline{A_s}\in\operatorname{End}(X)\).

⟨1⟩3 Powers used as feature vectors live one level higher, in
\(\mathcal L(X)\), with native Hilbert--Schmidt form

\[
 \langle E^j,E^k\rangle_{\rm HS}
 =\operatorname{Tr}((E^j)^\dagger E^k).
\]

This operator Hilbert space has dimension \((\dim X)^2\); it is not \(X\).

⟨1⟩4 Given only moments \(\nu_n\), the cyclic moment/GNS space is Laurent
polynomials modulo the nullspace of
\(\langle z^j,z^k\rangle_\nu=\nu_{k-j}\). It remembers the cyclic semisimple
model visible to the moments. It need not remember Jordan structure, unused
invariant subspaces, \(X\), or \(B\).

⟨1⟩5 **PROVE (scope).** Finite CCM reconstructs an operator on
\(E_N/\mathbb C\xi\), with the shifted Weil metric. It therefore reconstructs
a finite cyclic moment quotient. It does not reconstruct \(B\), all of \(X\),
or MPS letters. The source defines this quotient at
`refs/src/2511.22755/mc2arXiv.tex:910`.

## 2. Moment Gram convention

⟨2⟩1 **ASSUME.** \(U\) is finite-dimensional unitary and
\(\nu_n=\operatorname{Tr}(U^n)\) for every integer \(n\).

⟨2⟩2 **PROVE.**
\[
 W_{jk}=\nu_{k-j}
 =\operatorname{Tr}((U^j)^\dagger U^k)
 =\langle U^j,U^k\rangle_{\rm HS}.
\]
Thus \(W\) is a Gram matrix. Reversing the inner-product convention
transposes it; the clock check below makes that transpose visible.

⟨2⟩3 If \(E=SUS^{-1}\), put \(Q=S^{-\dagger}S^{-1}>0\). The metric adjoint
is \(A^\sharp=Q^{-1}A^\dagger Q\), and
\[
 \langle A,B\rangle_{{\rm HS},Q}
 =\operatorname{Tr}(Q^{-1}A^\dagger QB).
\]
Cyclicity gives
\(\langle E^j,E^k\rangle_{{\rm HS},Q}=\operatorname{Tr}(U^{k-j})\).
Native Hilbert--Schmidt equality is not similarity invariant.

## 3. Exact finite fixtures

### 3.1 The permutation \((12)(345)\)

⟨3⟩1 **ASSUME.** \(P\) is the five-dimensional permutation matrix of
\((12)(345)\).

⟨3⟩2 Its counts for \(n=0,\ldots,6\) are
\([5,0,2,3,2,0,5]\). The \(5\times5\) Gram of
\(1,P,\ldots,P^4\) has rank four and nullvector
\((-1,-1,0,1,1)\):
\[
 p(z)=z^4+z^3-z-1=(z^2-1)(z^2+z+1),\qquad p(P)=0.
\]

⟨3⟩3 On quotient basis \(1,z,z^2,z^3\), multiplication by \(z\) is
\[
 C=\begin{pmatrix}
 0&0&0&1\\1&0&0&1\\0&1&0&0\\0&0&1&-1
 \end{pmatrix},\qquad C^T H C=H,
\]
where \(H\) is the leading Gram block. Its characteristic polynomial is
\(p\). The quotient dimension is four although the original transfer
dimension is five.

### 3.2 Nonnormal retained Pauli block

⟨4⟩1 **ASSUME.** Use the retained \(\mathbb F_5\) Pauli/curve fixture
\[
 U=\frac1{\sqrt5}\begin{pmatrix}0&-5\\1&-2\end{pmatrix},\qquad
 G=\begin{pmatrix}1&-1\\-1&5\end{pmatrix}>0.
\]

⟨4⟩2 Exact multiplication gives \(U^TGU=G\), while \(U^TU\ne UU^T\).
Thus \(U\) is nonnormal natively and similar to a unitary in the \(G\)-metric.

⟨4⟩3 Its moments through order two are
\((2,-2/\sqrt5,-6/5)\). The \(3\times3\) moment Toeplitz matrix has spectrum
\(\{0,14/5,16/5\}\) and nullvector
\((1,2/\sqrt5,1)\), the annihilating polynomial's coefficients.

⟨4⟩4 The corrected operator Gram equals this Toeplitz matrix. The native
Gram does not: \(\|U\|_{\rm HS}^2=6\), while
\(\|U\|_{{\rm HS},G}^2=2=\nu_0\). This refutes “positive moments imply
native Hilbert--Schmidt unitarity.”

### 3.3 Jordan blindness

⟨5⟩1 **ASSUME.**
\(J=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\) and \(I=I_2\).

⟨5⟩2 Algebraically,
\(\operatorname{Tr}J^n=\operatorname{Tr}I^n=2\) for every \(n\ge0\), so their
moment matrices coincide. The moment-null polynomial \(p(z)=z-1\) kills the
diagonal cyclic model, but \(p(J)=J-I\ne0\), with HS norm squared one. A
moment-kernel polynomial need not annihilate the original nonsemisimple
transfer.

### 3.4 Positive Toeplitz needs duality

⟨6⟩1 **ASSUME.** \(r=1/2\) and \(W_{jk}=r^{|j-k|}\) for \(0\le j,k\le3\).

⟨6⟩2 Its leading minors are \(1,3/4,9/16,27/64\), so \(W>0\), although the
mode lies strictly inside the unit circle. Reflection sends \(r\) to
\(1/\bar r=2\), absent from the retained set. Positivity gives a disk bound;
reflection/functional-equation duality is the extra input for a boundary
statement. The native powers Gram is \(r^{j+k}\), not \(r^{|j-k|}\).

### 3.5 Underresolved minimum

⟨7⟩1 **ASSUME.** Let
\(U=\operatorname{diag}(1,\omega,\omega^2)\), where \(\omega^3=1\).
The window containing only \(1,U\) has moment Gram \(W_{\rm short}=3I_2\).
Its minimum is doubly degenerate and \(W_{\rm short}-3I_2=0\).

⟨7⟩2 Every coefficient vector is therefore “minimal.” The permitted choice
\(\xi=(1,-1/2)\) gives \(1-z/2\), whose root \(2\) is outside the true
unit-circle support and whose polynomial does not annihilate \(U\).

⟨7⟩3 Extending through \(U^3\) gives Gram rank three and the true kernel
\((-1,0,0,1)\), namely \(z^3-1\). Exact finite reconstruction needs a
resolved window and the stated simple-kernel hypothesis. An underresolved
minimal vector is only a fit and can return spurious roots.

### 3.6 Signed grading

⟨8⟩1 **ASSUME.** The even sector is the trivial eigenvalue \(1\), and the odd
sector is \(\operatorname{diag}(i,-i)\).

⟨8⟩2 The raw form \(G_{\rm even}-G_{\rm odd}\) is indefinite: its values on
\((1,0,0)\) and \((1,0,1)\) are \(-1\) and \(4\).

⟨8⟩3 Write \(s_n=t_n-o_n\), with \(t_n\) the trivial even contribution.
The arranged moments \(t_n-s_n=o_n\) give exactly the positive odd Gram. It
has rank two and kernel \(z^2+1\). Positivity belongs to the arranged form,
after specifying the trivial sector and sign.

## 4. Clock register and Hamiltonians

⟨9⟩1 **ASSUME.** Let \(F|j\rangle=v_j=|E^j\rangle\!\rangle\),
\(W=F^\dagger F\), and define literal and conjugated-feature histories
\[
 |\Omega\rangle=\sum_j|j\rangle\otimes v_j,\qquad
 |\bar\Omega\rangle=\sum_j|j\rangle\otimes\bar v_j.
\]

⟨9⟩2 **PROVE.** Direct contraction gives
\[
 \rho_{\rm clock}(\Omega)=W^T,\qquad
 \rho_{\rm clock}(\bar\Omega)=W.
\]
For
\(E=\operatorname{diag}(1,i)\), \((\rho_{\rm clock})_{01}=1-i\) whereas
\(W_{01}=1+i\). This fixture detects either omitted conjugation or transpose.

⟨9⟩3 If \(W\xi=0\), then \(F\xi=0\), hence
\[
 (|\xi\rangle\langle\xi|\otimes1)|\bar\Omega\rangle=0.
\]
For the literal history the corresponding projector is onto \(\bar\xi\).
Here \(\xi=(i,-1-i,1)\), so the two conventions differ detectably.

⟨9⟩4 With \(V\bar v_j=\bar v_{j+1}\), the distinct propagation Hamiltonian is
\[
 H_{\rm FK}=\sum_{j=0}^{m-1}\left(
 |j\rangle\langle j|+|j+1\rangle\langle j+1|
 -|j+1\rangle\langle j|\otimes V
 -|j\rangle\langle j+1|\otimes V^\dagger\right).
\]
Each local term obeys \(h_j^2=2h_j\), enforces
\(\psi_{j+1}=V\psi_j\), and annihilates \(\bar\Omega\). The exact
three-clock fixture has rank eight. Pinning its initial feature to
\(\overline{\operatorname{vec}I}\) raises the rank to eleven, leaving exactly
the target history line.

The physical-parent and unary-clock regressions are detailed in
`notes/ccm-tensor-network/checks/finite_followup.md`: for
\(\Gamma(x)=(x,0)\), \(\ker\Gamma=0\) while
\(\ker\Gamma^\dagger=\operatorname{span}\{|1\rangle\}\); the two-phase
three-bit unary automaton has bond four and accepts exactly
`000,100,110,111`.

## 5. Exact CCM Loewner correction

These are the finite identities of CCM Lemmas `basics` and `key`: displacement
at `refs/src/2511.22755/mc2arXiv.tex:837`, normalization at line 855,
self-adjointness at lines 863--910, and the determinant at lines 866--930.

⟨10⟩1 **ASSUME.** On indices \((-1,0,1)\), take
\[
 D=\operatorname{diag}(-1,0,1),\quad
 M=\begin{pmatrix}6&2&2\\2&1&2\\2&2&6\end{pmatrix},\quad
 \beta=(-2,0,2)^T,\quad\eta=(1,1,1)^T.
\]
The reversal-even matrix \(M\) comes from the real signed point distribution
on \([0,2\pi]\) with nodes \(\pi/2,\pi,3\pi/2\) and weights
\[
 ((7-\pi)/2,\,-6,\,(7+3\pi)/2).
\]
Substitution in the CCM Fourier formulas gives
\(b=(-2,0,2)\) and \(a=(6,1,6)\) exactly.

For real \(c\), set \(\tau=M+cI\) and \(\epsilon=c\). Its off-diagonal
entries are \((b_i-b_j)/(i-j)\), and
\[
 D\tau-\tau D=|\beta\rangle\langle\eta|
              -|\eta\rangle\langle\beta|.
\]

⟨10⟩2 **PROVE.** \(M=\tau-\epsilon I\) has eigenvalues \(0,4,9\) and
\[
 \xi=(-1/2,2,-1/2)^T,\qquad M\xi=0,\qquad\eta^T\xi=1.
\]
Adding \(cI\) changes the minimum but not \(M,\xi\), or reconstruction.

⟨10⟩3 For \(D'=D-|D\xi\rangle\langle\eta|\), exact multiplication gives
\[
 D'=\begin{pmatrix}-3/2&-1/2&-1/2\\0&0&0\\1/2&1/2&3/2\end{pmatrix},
 \qquad D'\xi=0,\qquad MD'=D'^TM.
\]

⟨10⟩4 Using quotient representatives \(e_{-1},e_1\),
\[
 G_q=\begin{pmatrix}6&2\\2&6\end{pmatrix},\qquad
 A_q=\begin{pmatrix}-3/2&-1/2\\1/2&3/2\end{pmatrix}.
\]
Then \(G_qA_q=A_q^TG_q\), \(\det(A_q-sI)=s^2-2\), and
\[
 \det(D-sI)\sum_{j=-1}^{1}\frac{\xi_j}{j-s}=s^2-2.
\]
Reality here is an exact finite consequence of the quotient metric. It has no
zeta convergence content.

⟨10⟩5 **Boundary countercheck.** The functional
\(\ell=(0,1/2,0)^T\) still has \(\ell^T\xi=1\), and
\(D_{\rm bad}=D-|D\xi\rangle\langle\ell|\) still kills \(\xi\). Nevertheless,
\[
 \|MD_{\rm bad}-D_{\rm bad}^TM\|_F^2=36.
\]
Normalization and kernel preservation alone do not suffice; the displacement
boundary \(\eta\) is essential.

## 6. Preserved negative results

The checker permanently records these stronger statements as false:

1. Positive moments imply native HS unitarity (Pauli and scalar fixtures).
2. Trace counts detect Jordan blocks (the \(J_2(1)\) fixture).
3. A moment-null polynomial always kills the original transfer (same fixture).
4. The cyclic quotient recovers the full transfer or physical bond
   (permutation dimension \(5\to4\)).
5. Any finite-window minimal vector reconstructs the support (underresolved
   three-mode fixture gives a spurious root \(2\)).
6. A raw supertrace form is automatically positive (graded fixture).
7. Any normalized boundary gives CCM self-adjointness (residual squared 36).
8. A real finite CCM spectrum proves RH (the toy roots have no convergence
   content).

The checks supply no evidence that an unregularized trace or HS norm of an
infinite unitary flow is finite.

## 7. Exact checks, numerical evidence, and red capability

SymPy recomputes the displayed finite identities over exact rationals,
\(i\), and \(\sqrt5\). These are reproducible certificates for the fixtures;
they support, but do not replace, the derivations above.

NumPy independently checks the CCM quotient roots against
\(\pm\sqrt2\) to \(10^{-14}\). That line is numerical evidence only.

One red test changes `CCM_BOUNDARY_MODE` from `eta` to the normalized center
functional. A second changes `CLOCK_FEATURE_MODE` from `conjugated` to
`literal` and must fail at the complex clock marginal. Both mutate temporary
copies, require a specific nonzero failure, and never alter shared source.
