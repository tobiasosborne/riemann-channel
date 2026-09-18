# Finite critic regressions: parents, conjugated histories, and unary clock

Status: **SKETCH with exact checks**. This shard records the finite defect
classes from the first critic round. It does not promote a claim.

## C1. Physical parent space uses the adjoint kernel

⟨1⟩1 **ASSUME.** Take the one-site block map
\[
 \Gamma:\mathbb C\longrightarrow\mathbb C^2,\qquad
 \Gamma(x)=(x,0).
\]
It is the block map of the labelled one-dimensional-bond letters
\((A_0,A_1)=(1,0)\).

⟨1⟩2 **PROVE.** The matrix of \(\Gamma\) is
\(\left(\begin{smallmatrix}1\\0\end{smallmatrix}\right)\), so
\(\ker\Gamma=0\). This kernel describes redundant boundary data.

⟨1⟩3 Its adjoint is \(\Gamma^\dagger=(1,0)\), hence
\[
 \ker\Gamma^\dagger=\operatorname{span}\{(0,1)^T\}
 =(\operatorname{im}\Gamma)^\perp.
\]
This is the physical parent subspace. The exact parent projector
\(h=|1\rangle\langle1|\) is nonzero, has rank one, and obeys
\(h\Gamma=0\).

⟨1⟩4 **SURVIVING STATEMENT.** The physical local parent space is
\(\ker\Gamma^\dagger\), while \(\ker\Gamma\) measures boundary
noninjectivity. The two kernels live in different spaces and cannot be
interchanged.

## C2. Literal and conjugated-feature histories

⟨2⟩1 **ASSUME.** Let \(F|j\rangle=v_j\), let \(W=F^\dagger F\), and set
\[
 |\Omega\rangle=\sum_j|j\rangle\otimes v_j,\qquad
 |\bar\Omega\rangle=\sum_j|j\rangle\otimes\bar v_j.
\]
The inner product is conjugate-linear in the first variable.

⟨2⟩2 **PROVE.** Direct partial trace gives
\[
 [\rho_{\rm clock}(\Omega)]_{jk}
 =\langle v_k,v_j\rangle=W_{kj},
 \qquad
 [\rho_{\rm clock}(\bar\Omega)]_{jk}
 =\langle\bar v_k,\bar v_j\rangle=W_{jk}.
\]
Therefore the literal history has marginal \(W^T\), while the
conjugated-feature history has marginal \(W\).

⟨2⟩3 The exact phase fixture \(E=\operatorname{diag}(1,i)\), with
\(v_j=\operatorname{vec}(E^j)\) for \(j=0,1,2\), has
\[
 W_{01}=1+i,\qquad [\rho_{\rm clock}(\Omega)]_{01}=1-i.
\]
Thus the two conventions cannot accidentally agree.

⟨2⟩4 The Gram nullvector is
\(\xi=(i,-1-i,1)^T\), the coefficients of
\((z-1)(z-i)\). Since \(F\xi=0\),
\[
 (|\xi\rangle\langle\xi|\otimes I)|\bar\Omega\rangle=0.
\]
For the literal history the annihilating clock projector is instead onto
\(\bar\xi\). This is a global length-register constraint, not a physical
MPS parent term.

## C3. Exact unary-clock automaton

⟨3⟩1 **ASSUME.** Use \(U=\operatorname{diag}(1,i)\), spectral projectors
\(P_1,P_2\), \(N=3\), \(Z=\operatorname{diag}(1,i)\), and virtual matrices
\[
 M_1=\begin{pmatrix}Z&0\\0&0\end{pmatrix},\qquad
 M_0=\begin{pmatrix}0&I\\0&I\end{pmatrix}.
\]
The start row is \((1,1;0,0)\). The endpoint sends either copy of \(e_a\)
to \(|P_a\rangle\!\rangle\).

⟨3⟩2 **PROVE.** \(M_0M_1=0\), so every binary word containing `01` has
zero amplitude. Among three-bit words the accepted language is exactly
\[
 000,\quad100,\quad110,\quad111.
\]

⟨3⟩3 A word \(1^j0^{3-j}\) reaches the endpoint with coefficients
\((1,i^j)\), so its feature is
\[
 |P_1\rangle\!\rangle+i^j|P_2\rangle\!\rangle
 =|U^j\rangle\!\rangle.
\]
The checker enumerates all eight words and checks every zero or endpoint
exactly. The virtual bond is \(2q=4\), independent of the clock length in
the general construction.

## C4. Pinned conjugated history

⟨4⟩1 **ASSUME.** Let \(V\bar v_j=\bar v_{j+1}\) and let the three-clock
propagation Hamiltonian be
\[
 H_{\rm prop}=\sum_{j=0}^{1}\left[
 (|j\rangle\langle j|+|j+1\rangle\langle j+1|)\otimes I
 -|j+1\rangle\langle j|\otimes V
 -|j\rangle\langle j+1|\otimes V^\dagger\right].
\]

⟨4⟩2 **PROVE.** Each local term satisfies \(h_j^2=2h_j\), hence is positive.
The propagation equations leave one free four-dimensional initial feature,
and the exact \(12\times12\) matrix has rank eight.

⟨4⟩3 Put
\[
 w_*=\overline{\operatorname{vec}I}/\sqrt2,\qquad
 H_{\rm pin}=|0\rangle\langle0|\otimes(I-|w_*\rangle\langle w_*|).
\]
Then \((H_{\rm prop}+H_{\rm pin})|\bar\Omega\rangle=0\), and the exact
pinned matrix has rank eleven. Its kernel is therefore precisely the target
history line.

## C5. Red capability

The second copied mutation changes `CLOCK_FEATURE_MODE` from `conjugated` to
`literal`. The mutation probe runs only C2/C4, reaches the complex off-diagonal
fixture, and must exit nonzero with the named clock failure. This catches an
omitted feature conjugation or an untracked Gram transpose. The pre-existing
CCM boundary mutation remains independent.
