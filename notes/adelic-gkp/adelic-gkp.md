# The theta state as an adelic GKP code, and the RH programme in quantum-information language

Author: `claude:fable-5.1`, 2026-10-02, in discussion with TJO ("the Theta state as a sum of deltas on the rationals ... is a
Gottesman–Kitaev–Preskill state ... what are the errors this GKP state corrects? ... what is the corresponding gaussian
version?"; then "please write this up. then, using this quantum info language please walk me through the RH approach, and weil
positivity").

Status: **a record, not a round.** Nothing is registered in `db/claims.tsv`; no REFUTE review has run; no shard. Each statement
carries a status: *standard* (classical, not byte-cited here), *proved here*, *checked* (numerically, `checks/`), *sketched*,
*heuristic*, or *open*. Part I is the GKP picture. Part II is a walk through the notebook's RH programme in that language; it
reorganises material from `notes/weil-bond-analytic/analytic.md` (cited as "analytic §n") and shard 04p, and adds a few
dictionary entries. Checks: `checks/check_adelic_gkp.py`, output `checks/output.txt` (73/73 pass). §14 (added 2026-10-05, TJO: "What about
if I take a field extension of Q, eg sqrt2 and ask the same questions again"): `checks/check_quadratic.py`, output
`checks/output_quadratic.txt` (14/14 pass).
Companion pages (2026-10-05, local session; index in §15): `functional-equation-gate.md`, `weil-positivity-spectroscopy.md`, `graph-ihara.md`,
`graph-super.md`, `lattice-tower.md`, `howe-positivity.md`, `sign-vector.md`, `locks.md`.

Conventions as in analytic.md. $\mathbb A$ the adeles of $\mathbb Q$, $\mathbb A_f$ the finite adeles, $\hat{\mathbb Z}=\prod_p\mathbb Z_p$.
Tate's character $\psi=\psi_\infty\prod_p\psi_p$ with $\psi_\infty(x)=e^{-2\pi ix}$, $\psi_p(x)=e^{2\pi i\{x\}_p}$; it is trivial on $\mathbb Q$, so
$\psi_f(r)=e^{2\pi ir}$ for $r\in\mathbb Q$. Self-dual measures, $\mathrm{vol}(\hat{\mathbb Z})=1$, $\mathrm{vol}(\mathbb A/\mathbb Q)=1$. $\Theta=\sum_{q\in\mathbb Q}\delta_q$.
$f_0=e^{-\pi x_\infty^2}\otimes1_{\hat{\mathbb Z}}$. $D_af(x)=|a|^{1/2}f(ax)$ for $a\in\mathbb A^\times$.

---------------------------------------------------------------------------------------------------------------------

## 0. Summary

- **G1 (the code).** $\Theta$ is the GKP stabiliser state of the lattice $\mathbb Q\times\mathbb Q\subset\mathbb A\times\mathbb A$, which is discrete, cocompact
  and Lagrangian (self-dual). So $\Theta$ is an adelic GKP *qunaught*: code dimension one. Poisson summation is $\hat\Theta=\Theta$. Standard
  (Tate, Weil); this is `prop:theta-functional-bond-state` of shard 04p and the remark recorded in HANDOFF 2026-09-26.
- **G2 (rationals are stabiliser-preserving Cliffords).** $D_a$ conjugates $W(u,v)$ to $W(u/a,av)$; for $a\in\mathbb Q^\times$ it preserves
  $\mathbb Q^2$, and $D_a\Theta=\Theta$ by the product formula. The full stabiliser-preserving Clifford group is $H(\mathbb Q)⋊\mathrm{SL}_2(\mathbb Q)$
  (Weil). With a one-dimensional code every such Clifford acts trivially. Proved here / standard.
- **G3 (rigidity).** No lattice commensurable with $\mathbb Q^2$ other than $\mathbb Q^2$ itself exists in $\mathbb A^2$: $\mathbb Q$ is divisible and $\mathbb A$
  is a $\mathbb Q$-vector space. So the sublattice trick that makes GKP qudits is unavailable: the global code is forced to be a qunaught.
  Proved here.
- **G4 (level $N$: a Bell pair across places).** On $\mathcal S(\mathbb R)\otimes\mathcal C_N$, with $\mathcal C_N$ the finite-adelic GKP code of
  dimension $N^2$, $\Theta$ is the maximally entangled state between an ordinary real GKP qudit of dimension $N^2$ and the finite-adelic qudit
  $\mathbb Z/N^2$. $\Theta$ is the inductive limit of these Bell pairs. Proved here, checked (C1, C2).
- **G5 (Gaussians).** At $p$ the role of the Gaussian is played by $1_{\mathbb Z_p}$, which is *itself* a normalisable GKP qunaught (compact
  open self-dual lattice $\mathbb Z_p^2$); $p$-adic GKP codes encode exact qudits. At $\infty$ there is no compact open subgroup and the vacuum is a
  genuine Gaussian. Overlaps of $\Theta$ with the Gaussian states give Jacobi's $\vartheta(\tau)$, $\tau$ in the Siegel upper half-plane of
  pure Gaussian states; Riemann's $\vartheta(t)$ is $\tau=it$; the theta group (not $\mathrm{SL}_2(\mathbb Z)$) is forced by the 2-adic vacuum.
  Standard / proved here / checked (C3–C5).
- **G6 (RH in this language).** $\zeta$ is the Mellin transform of the overlap of the code with the squeezed product vacuum. Euler product =
  product structure of the vacuum; functional equation = Fourier (S-gate) symmetry of code and vacuum; zeros = squeeze frequencies missing from
  every overlap profile; Weil positivity = the squeeze correlation functional being a *state*, whose GNS space would carry the
  Hilbert–Pólya operator as the squeeze generator. The explicit formula = zero-mode term minus a sum of single-mode squeeze traces
  (Lefschetz at the origin of each local phase space). Reorganisation of standard material plus analytic.md.
- **G7 (where the curve case gets its positivity, in this language).** Over a function field every place has a stabiliser vacuum, so overlaps
  of $\Theta_K$ with product stabiliser states are *counts* ($q^{h^0(D)}$), Riemann–Roch is the GKP self-duality, the cutoff is exact, the
  cokernel is a $2g$-dimensional logical space and the metric is Rosati, positive by ampleness of $\Theta$ (analytic §14). Over $\mathbb Q$ the
  real place has no stabiliser vacuum: overlaps are Gaussian sums, not counts, the cutoff has a plunge layer (analytic §8), and nothing
  plays the polarisation. Standard / reformulation; the "counts versus Gaussian sums" reading of the archimedean blocker is the new
  emphasis, heuristic as a diagnosis.
- **G8 (a field extension, §14).** For $K=\mathbb Q(\sqrt2)$ the code is $\Theta_K=\Theta\otimes\Theta$ in a $\mathbb Q$-basis: the same two-mode qunaught
  for every quadratic field. The field is a choice of torus $T_K=\mathrm{Res}_{K/\mathbb Q}\mathbb G_m$ of mode-mixing squeezes, and $\zeta_K$ is the Mellin
  transform along its orbit. New: units are lattice-preserving two-mode squeezes between the real places (a cat map; regulator
  $\log(1+\sqrt2)$); the vacuum is squeezed at the ramified prime (the different, $|d_K|^{s/2}$); the archimedean blocker doubles.
  $\zeta_K=\zeta\,L(\chi_8)$, so RH for $K$ contains RH for $\mathbb Q$. Standard / reformulation / checked (Q1–Q6).
- **G9 (naming; `functional-equation-gate.md`).** The gate behind the functional equation is the Fourier transform: the modular-group $S$, which in
  GKP gate notation is the Hadamard, not the phase gate. $\Theta$ is a qunaught because $\mathbb Q^2$ is Lagrangian; the absence of finite-index
  sublattices (G3) is the separate reason it cannot be made into a qubit.
- **G10 (Weil positivity as spectroscopy; `weil-positivity-spectroscopy.md`).** Echo form of the explicit formula; seven equivalent forms of Weil
  positivity (weight, echo bound, Gram matrix, spectrum, unitary dynamics, channel, response function); off-line zero = gain–loss pair, Weil form
  versus Lorentzian form. Checked (29/29). **TJO is not convinced by the overlap/filter reading of the standard zeta (§1 of that page).**
- **G11 (plain Ihara zeta; `graph-ihara.md`).** No GKP code for a graph. On two quadratures per vertex the non-backtracking step is
  $M=\bigl(\begin{smallmatrix}0&-1\\q&A\end{smallmatrix}\bigr)$, a symplectic similitude that factors as CZ along every edge, Hadamard on every mode, squeeze by
  $\sqrt q$; the Weil form is $\bigl(\begin{smallmatrix}q&A/2\\A/2&1\end{smallmatrix}\bigr)$ and Weil positivity is $A^2\le4q$ off the uniform mode. Lines are bright.
  $N_k(K_4)+3\,\#E(\mathbb F_{2^k})=4(2^k+1)+2(1+(-1)^k)$ for $E:y^2+xy=x^3+1$. Elementary / checked (56/56); literature for the factorisation not searched.
- **G12 (super Ihara zeta; `graph-super.md`).** Graph plus $\mathbb Z_2$ flux (2-cover): $Z_s=\det(1-A_su+qu^2)/\det(1-Au+qu^2)$, the notebook's graded quantum
  Ihara zeta in graph form. (i) The flux is a GKP qubit on the period lattice $H_1(Y,\mathbb Z)$ of the maximal abelian cover; super count $=2\times$ walks of
  odd flux. (ii) The fermionic step preserves $\mathbb Z^{2n}$; points are periodic syndromes of $n$ qunaught modes, the cohomology of the syndrome torus is the
  fermionic Fock space, and for one fermionic mode the super zeta is the zeta of the toral map (the Pauli-qubit elliptic curve of shard 03c is the syndrome
  torus of one mode). (iii) The flux-averaged fermionic numerator is the matching polynomial, so RH holds on average over fluxes (Godsil–Gutman,
  Heilmann–Lieb, quoted from memory). Standard / reformulation / checked (50/50).
- **G13 (the tower; `lattice-tower.md`).** For an integer step $M$ on $L=\mathbb Z^{2n}$ with $M^T\Omega M=q\Omega$ and $V=qM^{-1}$: the lattice $(1-V^k)L$ is the
  stabiliser lattice of a GKP code with basis the qunaught displaced by the period-$k$ syndromes, dimension $\det(1-M^k)$, logical Paulis the Heisenberg group of
  $L/(1-M^k)L$, and the step a logical Clifford of order $k$ whose orbits are the places; Lefschetz reads "code trace $=$ Fock supertrace". **The tower is blind to
  RH** (a hyperbolic step has all of it). RH (with semisimplicity) $\iff$ the normalised step has an invariant Gaussian vacuum; then the zeros are oscillator
  frequencies, the lattice has complex multiplication (one mode: the form $qx^2+\lambda xy+y^2$, discriminant $\lambda^2-4q$) and the tower is self-similar. In the
  ordinary case $(L,M)$ is a Deligne module, hence an ordinary abelian variety over $\mathbb F_q$ (Goresky–Tai `1701.07742:main.tex:561-591`). Elementary / standard /
  cited / checked (45/45); Howe's polarisation positivity: G14.
- **G14 (Howe's positivity; `howe-positivity.md`).** $\Omega$ is positive for the CM type $\Phi_+=\{\mathrm{Im}\,\varphi(F)>0\}$; it is a polarisation of Deligne's
  abelian variety iff $\Phi_+=\Phi_\varepsilon=\{\mathrm{val}_p\varphi(F)>0\}$ for some $\varepsilon$. One mode: yes, up to the sign of $\Omega$. **If $\lambda$ and $-\lambda$ both
  occur, never** (proved): $K_4$ with one negative edge fails at all four primes above 2. Repair: all compatible forms are $\Omega(x,p(A_s)y)$; $\Omega(x,A_sy)$ has
  degree 25 (a GKP code of dimension 5); a unit $P\in\mathbb Q[A_s]\cap M_4(\mathbb Z)$ with eigenvalues $1,-1,\varphi^{-3},-\varphi^{3}$ gives a principal polarisation. A $K_6$
  flux ($q=5$, six modes, no $\pm\lambda$ pair) is principally polarised by $\Omega$ itself at one of 16 primes. So the vacuum $J_+$ and the arithmetic complex
  structure $J_\varepsilon$ differ by a sign per mode; this corrects one sentence of `lattice-tower.md` §6. Cited / proved / computed with PARI (14/14).
- **G15 (the per-mode sign; `sign-vector.md`).** One mode: the sign is free (it compares rotation at the real place with attraction at $p$: the recursion
  $u\mapsto\lambda-q/u$ is elliptic at $\infty$ and hyperbolic at $p$). Several modes: with $D_j=\lambda_j^2-4q$ and $N^+$ the real field of the eigenvalues, the sign
  vectors realised above a prime $\mathfrak{p}^+$ are exactly the solutions of $\prod_{j\in I}\sigma_j=\tau_I$ over the sets $I$ with $\prod_ID_j$ a square in $N^+$, where
  $\tau_I$ is the residue of $(-1)^{|I|/2}\sqrt{\prod_ID_j}/\prod_I\lambda_j$ (proved). So $\Omega$ is a polarisation iff every lock sign is $+1$. Rational case:
  locked iff same squarefree part of $4q-\lambda^2=dm^2$, sign $+1$ iff $\lambda/m\equiv\lambda'/m'$ mod $p$ (e.g. $q=5$: 2 and 4 are anti-locked). Agrees with PARI on 13
  spectra; of the 527 ordinary Ramanujan flux classes of $K_4$, $K_5$, the cube and $K_6$ only 120 (one $K_6$ spectrum and its mirror) pass. Proved / computed (19/19).
- **G16 (where locks come from; `locks.md`).** With one prime of $N^+$ above $p$, two ordinary modes are locked iff $\mu'_+=\zeta\mu_\pm$ for a root of unity $\zeta$;
  sign $+1$ for a rotation, $-1$ for a rotation with a reflection (proved). Integer eigenvalues: only the half turn ($\pm\lambda$), the quarter turn ($\mathbb Q(i)$:
  $\lambda^2+(\lambda')^2=4q$) and the sixth turn ($\mathbb Q(\sqrt{-3})$). A cyclic quartic field gives a lock whose sign depends on the prime and does not obstruct.
  **Bipartite graphs:** $D=\pm1$ by side gives $\Gamma=\mathrm{diag}(D,-D)$, an antisymplectic involution anticommuting with the step; the half lattice (functions on
  one side as positions, on the other as momenta) carries the signed biadjacency form $B_s$ and $F^2$ over $\mathbb F_{q^2}$; on it all 31 ordinary Ramanujan fluxes of
  the cube are polarised, 15 principally. Scan (21069 classes on small regular graphs): lock-free fluxes exist from 8 vertices on; $K_7$ has third-turn locks of both
  signs. Proved / computed (7/7); "no graph symmetry behind quarter and sixth turns" is a negative finding only.

---------------------------------------------------------------------------------------------------------------------

# Part I. The adelic GKP code

## 1. Phase space, Weyl operators, the lattice

On $L^2(\mathbb A)$ (Schwartz–Bruhat core $\mathcal S(\mathbb A)$) put $W(u,v)f(x)=\psi(vx)f(x+u)$ for $u,v\in\mathbb A$. Then
$$W(u,v)W(u',v')=\psi(uv'-vu')\,W(u',v')W(u,v),$$
so phase space is $\mathbb A^2$ with symplectic pairing $\psi(\omega)$, $\omega((u,v),(u',v'))=uv'-vu'$. Proved here (two lines).

Facts about $\mathbb Q\subset\mathbb A$ (standard; Tate's thesis; not byte-cited):
- $\mathbb Q$ is **discrete**: $\mathbb Q\cap\big((-\tfrac12,\tfrac12)\times\hat{\mathbb Z}\big)=\{0\}$.
- $\mathbb Q$ is **cocompact**: $\mathbb A=\mathbb Q+\big([0,1)\times\hat{\mathbb Z}\big)$, so $\mathbb A/\mathbb Q\cong(\mathbb R\times\hat{\mathbb Z})/\mathbb Z$ (the solenoid), of volume one.
- $\mathbb Q$ is **self-dual**: $\mathbb Q^\perp=\{x:\psi(xq)=1\ \forall q\in\mathbb Q\}=\mathbb Q$.

So $\mathbb Q$ is a lattice in the locally compact sense (not a finite-rank $\mathbb Z$-module), and $L=\mathbb Q\times\mathbb Q$ is a lattice in
$\mathbb A^2$ whose symplectic complement is $\mathbb Q^\perp\times\mathbb Q^\perp=L$: **a Lagrangian lattice**.

**Proposition 1 (the code).** $\langle\Theta,f(\cdot+q)\rangle=\langle\Theta,f\rangle$ and $\langle\Theta,\psi(q'\,\cdot)f\rangle=\langle\Theta,f\rangle$ for $q,q'\in\mathbb Q$, and
$\langle\Theta,\hat f\rangle=\langle\Theta,f\rangle$. Up to scale, $\Theta$ is the only tempered distribution with the two invariances.

*Proof.* The invariances: $\sum_r f(r+q)=\sum_r f(r)$, and $\psi(q'r)=1$. Fourier: Poisson summation on $\mathbb A/\mathbb Q$ with
$\mathbb Q^\perp=\mathbb Q$ and volume one (standard). Uniqueness (sketched): $\psi(q'\cdot)$-invariance for all $q'$ forces support in
$\mathbb Q^\perp=\mathbb Q$, a discrete set, so the distribution is $\sum_q c_q\delta_q$ (no derivatives at the finite places, and the real
derivatives are excluded by the modulation invariance in the real variable); translation invariance makes $c_q$ constant. ∎

In GKP terms: $\Theta$ is the joint $+1$ eigen-"state" of the stabiliser group $\{W(\lambda):\lambda\in L\}$ (up to the usual
phase convention for $W$ on $L$, trivial here because $\psi(qq')=1$). The code dimension of a GKP code is
$\sqrt{[L^\perp:L]}$; here it is $1$. **$\Theta$ is the adelic GKP qunaught.** The real analogue is $\sum_{n\in\mathbb Z}\delta_n$ with
$\psi_\infty$, i.e. the square lattice of spacing $\sqrt{2\pi}$ when $\hbar=1$ and the phase is $e^{iuv}$.

## 2. Cliffords: rationals, $\mathrm{SL}_2(\mathbb Q)$, ideles

**Proposition 2 (proved here).** $D_aW(u,v)D_a^{-1}=W(a^{-1}u,\,av)$ for $a\in\mathbb A^\times$. So $D_a$ is a Clifford (it normalises the Weyl
group), the symplectic squeeze $\mathrm{diag}(a^{-1},a)$. For $a\in\mathbb Q^\times$, $D_a$ maps $L$ to $L$ and $D_a\Theta=\Theta$.

*Proof.* $D_aW(u,v)D_a^{-1}f(x)=\psi(avx)f(x+u/a)$. For the second claim, $\langle\Theta,D_af\rangle=|a|^{1/2}\sum_qf(aq)=|a|_{\mathbb A}^{1/2}\langle\Theta,f\rangle$,
and $|a|_{\mathbb A}=1$ for $a\in\mathbb Q^\times$ (product formula). ∎

More generally (standard; Weil 1964, not byte-cited): the metaplectic cover $\mathrm{Mp}_2(\mathbb A)\to\mathrm{SL}_2(\mathbb A)$ splits over
$\mathrm{SL}_2(\mathbb Q)$, and $\Theta$ is fixed by the Weil representation of $\mathrm{SL}_2(\mathbb Q)$. The shear by $t\in\mathbb Q$ multiplies by
$\psi(tx^2/2)$, which is $1$ on $\mathbb Q$; the Weyl element is the Fourier transform. So the stabiliser-preserving Clifford group of the code
is $H(\mathbb Q)⋊\mathrm{SL}_2(\mathbb Q)$. This invariance *is* the automorphy of theta.

**Correction to the chat phrasing "logical operations".** With a one-dimensional code there is no logical space; every stabiliser-preserving
Clifford acts as a scalar, here trivially. Multiplication by rationals is a symmetry of the code, not a gate.

**Ideles.** For $x\in\mathbb A^\times\setminus\mathbb Q^\times$, $D_x\Theta$ is the GKP qunaught of the squeezed lattice $x^{-1}\mathbb Q\times x\mathbb Q$,
with net squeeze $|x|_{\mathbb A}$. Since $\mathbb Q^\times$ acts trivially, the squeeze orbit of the code is parametrised by
$C_{\mathbb Q}=\mathbb A^\times/\mathbb Q^\times$. All of the arithmetic lives on this orbit (Part II).

## 3. What it corrects

**Detection (standard GKP reasoning).** For a displacement error $W(e)$, $e\in\mathbb A^2$, each stabiliser $W(\lambda)$ acquires the eigenvalue
$\psi(\omega(\lambda,e))$. The syndrome is therefore the character $\lambda\mapsto\psi(\omega(\lambda,e))$ of $L$, i.e. the class of $e$ in
$\mathbb A^2/L=(\mathbb A/\mathbb Q)^2$, which is the Pontryagin dual of $L$. Applying $W(-e')$ for any $e'$ in the class leaves an element of
$L$, which fixes $\Theta$. So **every displacement is detected and undone**; with nothing encoded, "correction" means a perfect displacement
sensor modulo the lattice, as for the real qunaught.

The syndrome space is adelic: by strong approximation each class has a representative with real part in $[0,1)$ and finite part in
$\hat{\mathbb Z}$. A $p$-adic error $p^{-k}u$ ($u\in\mathbb Z_p^\times$) is equivalent modulo $L$ to a displacement by $p^{-k}u-r$ for a rational
$r\in p^{-k}\mathbb Z$ with $r\equiv p^{-k}u$ mod $\mathbb Z_p$, i.e. to a real displacement by $-r$ plus an error in $\hat{\mathbb Z}$. The code
converts $p$-adic errors into real ones with denominators.

**Proposition 3 (rigidity; proved here).** Let $M\subset\mathbb A^2$ be a subgroup commensurable with $L=\mathbb Q^2$ (i.e. $M\cap L$ has finite
index in both). Then $M=L$.

*Proof.* $L$ is divisible, and a divisible abelian group has no proper subgroup of finite index (the quotient would be finite and
divisible, hence trivial). So $M\cap L=L$, i.e. $L\subset M$ with $M/L$ finite. $\mathbb A$ is a $\mathbb Q$-vector space, so $nx\in\mathbb Q^2$
implies $x\in\mathbb Q^2$: $\mathbb A^2/L$ is torsion-free, and the finite group $M/L$ is trivial. ∎

So a GKP code with $d>1$ cannot be built by passing to a sublattice or superlattice of $\mathbb Q^2$, unlike $\mathbb Z^2\subset\mathbb R^2$. The
squeezed lattices $D_x L$ are Lagrangian too. **Every global code in this family is a qunaught.** Nontrivial codes appear only after
truncation, §4, or locally, §5.

## 4. Level $N$: the code is a Bell pair across places

Fix $N\ge1$. At the finite places take the GKP code with lattice $N\hat{\mathbb Z}\times N\hat{\mathbb Z}\subset\mathbb A_f^2$. Its symplectic
complement is $N^{-1}\hat{\mathbb Z}\times N^{-1}\hat{\mathbb Z}$ (because $\hat{\mathbb Z}^\perp=\hat{\mathbb Z}$), so its code space
$$\mathcal C_N=\{\varphi:\ \mathrm{supp}\,\varphi\subset N^{-1}\hat{\mathbb Z},\ \varphi(\cdot+N\hat{\mathbb Z})=\varphi\},\qquad e_a=1_{a+N\hat{\mathbb Z}},\ a\in N^{-1}\hat{\mathbb Z}/N\hat{\mathbb Z}\cong\mathbb Z/N^2,$$
has dimension $N^2$, and it is spanned by normalisable vectors. At the real place take the ideal GKP code with lattice $N\mathbb Z\times N\mathbb Z$
(pairing $\psi_\infty$): code dimension $N^2$, basis the combs $c_a=\sum_{n\in\mathbb Z}\delta_{a+Nn}$, $a\in N^{-1}\mathbb Z/N\mathbb Z$.

**Theorem 4 (proved here; checked C1, C2).**
1. For $g\in\mathcal S(\mathbb R)$ and $\varphi=\sum_a\varphi_ae_a\in\mathcal C_N$: $\ \langle\Theta,g\otimes\varphi\rangle=\sum_a\varphi_a\,\langle c_a,g\rangle$. That is,
   $$\Theta\big|_{\mathcal S(\mathbb R)\otimes\mathcal C_N}=\sum_{a\in\mathbb Z/N^2}c_a\otimes e_a^*,$$
   the maximally entangled state between the real GKP qudit and the finite-adelic qudit, in the code bases.
2. It is stabilised by $X_b\otimes X_b$ and $Z_b\otimes Z_b^{-1}$, $b\in N^{-1}\mathbb Z$ (these are the Weyl operators $W(b,0)$, $W(0,b)$ of
   $L$, split across places).
3. $\mathcal S(\mathbb A)=\bigcup_N\mathcal S(\mathbb R)\otimes\mathcal C_N$, increasing along divisibility. So $\Theta$ is the inductive limit of the Bell pairs.

*Proof.*
1. $\mathbb Q\cap N\hat{\mathbb Z}=N\mathbb Z$, so $\mathbb Q\cap(a+N\hat{\mathbb Z})=a+N\mathbb Z$ for $a\in N^{-1}\mathbb Z$. Hence $\langle\Theta,g\otimes e_a\rangle=\sum_ng(a+Nn)$.
2. Translation by $b$ permutes the labels on both sides identically. Modulation by $\psi(bx)=\psi_\infty(bx_\infty)\psi_f(bx_f)$ multiplies $e_a$
   by $e^{2\pi iab}$ (constant on $a+N\hat{\mathbb Z}$ since $bN\hat{\mathbb Z}\subset\hat{\mathbb Z}$) and the real side by $e^{-2\pi ibx}$, which equals
   $e^{-2\pi iab}$ on the support of $c_a$.
3. An element of $\mathcal S(\mathbb A_f)$ is locally constant with compact support, hence in some $\mathcal C_N$. ∎

C1 checks the stronger self-duality at level $N$ ($\langle\Theta,f\rangle=\langle\Theta,\hat f\rangle$ with the finite Fourier transform
$\hat e_a=N^{-1}\psi_f(a\,\cdot)1_{N^{-1}\hat{\mathbb Z}}$) for $N=1,2,3,6,12$ to $10^{-25}$.

**Reading.** At every finite resolution the adelic qunaught is a Bell pair between the real oscillator and the finite places. Local errors at
one place are detected against the other half, through the joint stabilisers. The real factor alone is an ordinary GKP code whose logical
spacing is $1/N$: resolving the finite places to level $N$ shrinks the real displacements it can correct on its own to $|\epsilon|<1/2N$. In the
limit nothing is encoded and everything is sensed. At $N=1$ the finite factor is one-dimensional ($1_{\hat{\mathbb Z}}$) and the real factor is
the qunaught $\sum_n\delta_n$: **projecting the finite places onto their vacua turns the adelic code into the ordinary real GKP qunaught.**

Heuristic remark: the squeezes $D_p$ at a finite place do not preserve the level ($D_p\mathcal C_N\subset\mathcal C_{pN}$ up to relabelling). Whether
the local terms of the explicit formula can be read as the leakage between levels $N$ and $pN$, in the sense of the compression lemma
(analytic §5, Lemma 6), is open.

## 5. Gaussians

**Local vacua.** The real Gaussian $e^{-\pi x^2}$ is characterised (among other ways) as the vector fixed by the maximal compact
$\mathrm{SO}(2)$ (metaplectic $\mathrm U(1)$) of the Weil representation: the oscillator ground state, Fourier self-dual. At $p$ the maximal compact
is $\mathrm{SL}_2(\mathbb Z_p)$ and its fixed vector is $1_{\mathbb Z_p}$, also Fourier self-dual (standard; Weil). So
$$f_0=e^{-\pi x_\infty^2}\otimes\bigotimes_p1_{\mathbb Z_p}$$
is the adelic vacuum, Tate's standard vector.

**Proposition 5 ($p$-adic GKP codes; proved here).** For integers $a,b$ with $a+b\ge0$, the lattice $L_{a,b}=p^a\mathbb Z_p\times p^b\mathbb Z_p\subset\mathbb Q_p^2$
is isotropic, with complement $p^{-b}\mathbb Z_p\times p^{-a}\mathbb Z_p$; its code space is the functions supported on $p^{-b}\mathbb Z_p$ and
$p^a\mathbb Z_p$-periodic, of dimension $p^{a+b}$, spanned by normalisable vectors, with logical Pauli group that of $\mathbb Z/p^{a+b}$. For
$a=b=0$ the code is one-dimensional and its state is $1_{\mathbb Z_p}$.

*Proof.* $\psi_p$ is trivial exactly on $\mathbb Z_p$, so $(p^k\mathbb Z_p)^\perp=p^{-k}\mathbb Z_p$, and the support/periodicity description follows
as in Proposition 1. The dimension is $[p^{-b}\mathbb Z_p:p^a\mathbb Z_p]=p^{a+b}$. ∎

So **at the finite places "Gaussian", "vacuum" and "GKP qunaught" are the same state, and it is normalisable.** The obstruction that makes ideal
GKP states unphysical over $\mathbb R$ (no compact open subgroup, so no normalisable lattice state) is absent over $\mathbb Q_p$. Over $\mathbb R$ it
is present: no nonzero $f$ has $f$ and $\hat f$ both compactly supported (Connes, `main.tex:2746-2749`, quoted in analytic §8). That single
fact is the archimedean blocker of analytic §8 in GKP language.

**Gaussian states and theta functions (standard; checked C3–C5).** The pure one-mode Gaussian states (up to displacement) are
$\gamma_\tau(x)=e^{\pi i\tau x^2}$, $\tau$ in the upper half-plane $\mathbb H=\mathrm{SL}_2(\mathbb R)/\mathrm{SO}(2)$ (the Siegel half-space for one mode).
Overlaps of the code with the adelic Gaussian states are Jacobi's theta function:
$$\big\langle\Theta,\ \gamma_\tau\otimes1_{\hat{\mathbb Z}}\big\rangle=\sum_{q\in\mathbb Q\cap\hat{\mathbb Z}}e^{\pi i\tau q^2}=\sum_{n\in\mathbb Z}e^{\pi i\tau n^2}=\vartheta(\tau).$$
Riemann's $\vartheta(t)=\sum_ne^{-\pi n^2t}$ is $\tau=it$: **the overlap of the ideal adelic GKP state with the vacuum squeezed at the real place.**
Its modular laws are Cliffords moving the Gaussian while $\Theta$ stays fixed:
- $S$: $\vartheta(-1/\tau)=\sqrt{\tau/i}\,\vartheta(\tau)$, from $\hat\Theta=\Theta$, $\hat1_{\hat{\mathbb Z}}=1_{\hat{\mathbb Z}}$ and $\hat\gamma_\tau\propto\gamma_{-1/\tau}$.
- $T$ fails, $T^2$ holds: the shear by $1$ multiplies the real factor by $\psi_\infty(x^2/2)$ (shifting $\tau$ by one unit) and the 2-adic vacuum by
  $\psi_2(x^2/2)=(-1)^x$ on $\mathbb Z$ (C4), while the odd-$p$ vacua are invariant ($x^2/2\in\mathbb Z_p$). So $\vartheta(\tau+1)=\sum(-1)^ne^{\pi i\tau n^2}\ne\vartheta(\tau)$
  and $\vartheta(\tau+2)=\vartheta(\tau)$ (C3). **The theta group $\Gamma_\theta=\langle S,T^2\rangle$, rather than $\mathrm{SL}_2(\mathbb Z)$, is forced by the 2-adic vacuum** (that $\Gamma_\theta$ is
  exactly the stabiliser, up to phase, of $1_{\mathbb Z_2}$ inside $\mathrm{SL}_2(\mathbb Z)$ is sketched, not proved here).

**Finite-energy GKP.** The realistic GKP state at the real place is $e^{-\beta\hat n}$ applied to the ideal comb, an element of Howe's oscillator
semigroup (the contraction semigroup of complexified symplectic maps); its wavefunction is a Gaussian-enveloped comb of Gaussians, a Jacobi theta
function in $x$ (standard). The adelic finite-energy code is: level $N$ at the finite places (exact, §4) and the oscillator semigroup at $\infty$.
At $p$ there is no continuous energy, since $\mathrm{SL}_2(\mathbb Z_p)$ has no one-parameter subgroup; **the $p$-adic analogue of energy is the level
(the conductor)**, and the $p$-adic regulator is exact.

Connes's cutoff $P_\Lambda\hat P_\Lambda$ (position and momentum both bounded by $\Lambda$) is the dilation-covariant finite-energy regulator. It is exact
at the finite places ($\Lambda$-boxes are compact open lattices) and approximate at $\infty$, where the prolate (LPS) truncation has a plunge layer
of $\asymp\log\Lambda$ states (analytic §8).

---------------------------------------------------------------------------------------------------------------------

# Part II. The RH programme, walked through in this language

## 6. Dictionary

| arithmetic / notebook | quantum information |
|---|---|
| $\mathbb A$, $\mathbb A^2$ with $\psi\circ\omega$ | one adelic mode and its phase space |
| $\Theta=\sum_{q\in\mathbb Q}\delta_q$ | ideal GKP qunaught of the Lagrangian lattice $\mathbb Q^2$ |
| Poisson summation, $\hat\Theta=\Theta$ | self-duality of the code (S-gate symmetry) |
| $\mathrm{SL}_2(\mathbb Q)$-automorphy of theta | stabiliser-preserving Clifford group |
| $f_0=e^{-\pi x^2}\otimes1_{\hat{\mathbb Z}}$ | product vacuum (Gaussian at $\infty$, local qunaughts at $p$) |
| $C_{\mathbb Q}=\mathbb A^\times/\mathbb Q^\times$, $D_x$ | the group of squeezes modulo those fixing the code |
| Connes's $Ef(a)=|a|^{1/2}\sum_{q\ne0}f(qa)$ | overlap profile of a test state with the squeezed code, zero-mode removed |
| Tate's $Z(f,s)$ | Mellin transform of the overlap profile in the squeeze |
| the pole terms $\hat h(0),\hat h(1)$ | the two zero modes of the comb: $q=0$ and its Fourier partner |
| local terms $W_v$ | single-mode squeeze traces (Lefschetz at the origin of each local phase space) |
| Weil's form $Z(h*\tilde h)$ | the squeeze correlation functional of the code |
| Weil positivity | that functional is a state |
| "the metric" | its GNS inner product |
| Hilbert–Pólya operator | the squeeze generator in the GNS space |
| level $N$ / conductor | $p$-adic energy cutoff (exact) |
| Connes's $P_\Lambda\hat P_\Lambda$ | finite-energy truncation (exact at $p$, plunge layer at $\infty$) |

## 7. The zeta function is an overlap

Tate (standard; check C5 for $f_0$): for $f\in\mathcal S(\mathbb A)$ and $\mathrm{Re}\,s>1$,
$$Z(f,s)=\int_{\mathbb A^\times}f(x)|x|^s\,d^\times x=\int_{C_{\mathbb Q}}\Big(\sum_{q\in\mathbb Q^\times}f(qx)\Big)|x|^s\,d^\times x .$$
Read the two sides:
- **Left: a product.** For $f=f_0$ the integral factorises over places: $\int_{\mathbb R^\times}e^{-\pi x^2}|x|^sd^\times x=\pi^{-s/2}\Gamma(s/2)$ and
  $\int_{\mathbb Q_p^\times}1_{\mathbb Z_p}|x|^sd^\times x=(1-p^{-s})^{-1}$. Each local factor is the Mellin profile of the local vacuum. **The Euler product
  is the product structure of the vacuum.** This is side A of the notebook (the gas; the primes do not talk), and it is a product state.
- **Right: the code.** The inner sum is $\langle\Theta,f(x\,\cdot)\rangle-f(0)$, the overlap of the squeezed test state with the code, zero
  mode removed. This is where the global lattice, which entangles the places (§4), enters.

The identity of the two is "unfolding": the integral over all of $\mathbb A^\times$ is the integral over the squeeze orbit of the code. With
$Ef(a)=|a|^{1/2}\sum_{q\ne0}f(qa)$, $Z(f,s)=\int Ef(a)|a|^{s-1/2}d^\times a$ (analytic §1).

## 8. The functional equation is the S-gate

(Naming, 2026-10-05: $S$ here is the modular-group $S$, the Fourier transform. In GKP gate notation that is the Hadamard; the GKP phase gate
$S$ is the shear, modular $T$. See `functional-equation-gate.md`.)

The Fourier transform fixes $\Theta$ and $f_0$ and conjugates $D_a$ to $D_{a^{-1}}$. Poisson summation then gives $Z(f,s)=Z(\hat f,1-s)$ up to the
two pole terms, which come from the two zero modes of the comb ($q=0$ and the constant; Connes's $\mathbb C\oplus\mathbb C(1)$, analytic §6).
In decay-rate language: a mode $\rho=\beta+i\gamma$ pairs with $1-\bar\rho$, rates $(\beta,1-\beta)$ (`what-rh-has-become.md` §5). The
symmetry is a Clifford symmetry of code and vacuum; **RH is not a symmetry statement** and does not follow from it.

## 9. The zeros are what the overlaps cannot contain

In the trivial-character sector $Z(f,s)=\xi(s)F_f(s)$ with $F_f$ entire for $f\in\mathcal S(\mathbb A)_0$ (analytic §1). So the Mellin transform of
**every** overlap profile $Ef$ vanishes at every zero $\rho$: the zeros are squeeze frequencies absent from all overlap profiles. Connes's
spectral realisation is the cokernel of $E$: in $L^2(C_{\mathbb Q})$, the orthogonal complement of the overlap profiles carries the squeeze
action with spectrum the critical zeros (Connes 1998, `refs/src/math/9811068/main.tex`; not re-cited here by line). An off-line zero would be a non-unitary mode $|a|^{\rho-1/2}$, not in
$L^2$; in any cutoff it is an edge mode (analytic §4, Proposition 4). So the plain $L^2$ picture sees only critical zeros; it is blind to
exactly the thing in question (analytic L3).

## 10. Weil positivity: is the squeeze correlation functional a state?

Let $\mathcal A=C_c^\infty(\mathbb R_+^\times)$ (trivial-character sector) with convolution (composition of squeezes) and the involution
$\tilde h(x)=x^{-1}\overline{h(1/x)}$, which is the adjoint for the squeeze representation normalised so that $\mathrm{Re}\,s=\tfrac12$ is the
unitary axis. Define the Hermitian functional
$$\omega(h)=\sum_\rho\hat h(\rho),\qquad\omega(h*\tilde h)=Z(h)=\sum_\rho\hat h(\rho)\overline{\hat h(1-\bar\rho)} .$$

- **Weil's criterion** (cited, `cit:weil-criterion`): RH $\iff\omega(h*\tilde h)\ge0$ for all $h$, i.e. **$\omega$ is a (non-normalised) state on the
  squeeze algebra.**
- **GNS (standard reformulation).** If $\omega$ is positive, the GNS construction gives a Hilbert space $\mathcal H_\omega$ on which the squeezes act
  unitarily. Under RH, $\omega(h)=\sum_\gamma\hat h(\tfrac12+i\gamma)$ is a sum of unitary characters, so $\mathcal H_\omega\cong\ell^2(\text{zeros})$ and the
  squeeze generator has spectrum $\{\gamma\}$: **the Hilbert–Pólya operator is the squeeze generator in the GNS space of $\omega$, and "the metric" is
  the GNS inner product.** The notebook's Gram-of-open-transfer-strips form (`prop:ccm-tn-operator-gram`) is this Gram matrix in window
  coordinates. Note that GNS here is tautological: it produces the space only once positivity is known. The content of RH is to produce
  $\mathcal H_\omega$ a priori.
- **What failure looks like.** An off-line pair $\{\rho,1-\bar\rho\}$ contributes $2\,\mathrm{Re}\,z\bar w$ with $z=\hat h(\rho)$, $w=\hat h(1-\bar\rho)$
  independent: a hyperbolic plane, signature $(1,1)$ (C6). Then $\omega$ is a Krein-space "state" with one negative direction per off-line pair.
- **The explicit formula** splits $\omega$ into computable pieces: $Z=P-\mathrm{Loc}$ (analytic, conventions).
  - $P(h)=\hat g(0)+\hat g(1)$, $g=h*\tilde h$: the **two zero modes of the comb**, rank two, signature $(1,1)$.
  - $\mathrm{Loc}=\sum_vW_v$: at each place a **single-mode squeeze trace**. The distributional trace of $D_\lambda$ on $L^2(\mathbb Q_v)$ is
    $\int|\lambda|^{1/2}\delta((\lambda-1)x)\,dx=|\lambda|_v^{1/2}/|1-\lambda|_v$: Lefschetz at the fixed point $x=0$. These are Connes's local
    terms up to normalisation (sketched; his Theorem 4, `main.tex:1893-1906`, semi-local trace formula). At $p$, $\lambda=p^{\pm k}$ gives the
    $\log p\cdot p^{-k/2}$ terms of the prime side; at $\infty$ the integral gives the Gamma term.
  - So **Weil positivity says: zero-mode term minus the sum over places of local squeeze traces is a positive form.** Proposition 7 of analytic
    §6 sharpens it: one pole functional can be killed, and then RH $\iff-\mathrm{Loc}\ge0$ on its kernel.
- **Connes's route in this language.** Truncate to finite energy with $Q_\Lambda=P_\Lambda\hat P_\Lambda$. The trace of a squeeze on the truncated
  code-complement is (Connes's conjectured global trace formula) $2h(1)\log\Lambda+\sum_v W_v(h)+o(1)$: a phase-space volume term (the number of states
  in the box, measured in squeeze coordinates) plus the local fixed-point traces. The renormalised trace is of positive type at every $\Lambda$
  (analytic L5), and its limit is the harmonic-measure form, positive unconditionally; RH $\iff$ that limit equals Weil's $\omega$
  (analytic L4). The missing input is the asymptotic trace formula itself.

## 11. Calibration: the curve case, where it works

Let $K$ be a function field of genus $g$ over $\mathbb F_q$, $\Theta_K=\sum_{x\in K}\delta_x$ on $\mathbb A_K$, again a self-dual GKP qunaught. Now every
place is non-archimedean, so every place has a stabiliser vacuum.

- **Overlaps are counts.** For a divisor $D=\sum d_vv$, the product of local qunaughts $1_D=\bigotimes_v1_{\pi_v^{-d_v}\mathcal O_v}$ has
  $\langle\Theta_K,1_D\rangle=\#\{x\in K:v(x)\ge-d_v\ \forall v\}=\#L(D)=q^{h^0(D)}$ (standard). The overlap of two stabiliser states counts the
  common lattice points, as in finite-dimensional stabiliser theory.
- **Riemann–Roch is the self-duality of the code.** $\hat\Theta_K=\Theta_K$ and $\hat1_D\propto1_{K_c-D}$ (the dual lattice; $K_c$ canonical) give
  $q^{h^0(D)}=q^{\deg D+1-g}q^{h^0(K_c-D)}$ (standard: Tate/Weil).
- **The cutoff is exact,** the cokernel of the overlap map is a $2g$-dimensional logical space, the degree squeeze acts on it as the Frobenius
  companion matrix (an MPS of bond dimension $2g$), and its similitude metric is the Rosati form $\sum_i\varphi(\alpha_i)\varphi(q/\alpha_i)$
  (analytic §§13–14). Weil positivity is positivity of that form, and it holds because $\Theta$ (the theta divisor, the support of $h^0>0$
  in $\mathrm{Pic}^{g-1}$, i.e. where overlaps of the code with product stabiliser states are nontrivial) is ample. **For curves the GNS space of
  §10 exists a priori: it is $H^1$, finite-dimensional, with a positive metric supplied by geometry, and the Hilbert–Pólya operator is
  $F/\sqrt q$, unitary.**

## 12. What is missing for $\mathbb Q$, in this language

1. **No stabiliser vacuum at $\infty$.** Overlaps of $\Theta$ with product states are Gaussian sums ($\vartheta$), not counts ($q^{h^0}$). There is no
   exact Riemann–Roch, the finite-energy regulator has a plunge layer of $\asymp\log\Lambda$ states at the window edge, exactly where off-line
   zeros would show as edge modes (analytic L8). Diagnosis, heuristic: **the curve proof's positivity is a positivity of counts; at the real place
   there is nothing to count.**
2. **No polarisation.** Even granting a cutoff, nothing in the code supplies a structural reason for $\omega$ to be a state; the bond's own
   norms are blind (analytic L3, L9). The target, restated: realise $\omega(h*\tilde h)$ as a squared norm (a fidelity, a probability, a
   $\mathrm{Tr}(\varphi_h\varphi_h^\dagger)$) in a space where the squeezes act unitarily and the two zero modes have been removed, built before
   the zeros are known. This is the "Stinespring form with prime dilations as Kraus operators" question of the README, and analytic §14's
   "ample $\Phi$".
3. **The level structure is suggestive, not yet useful.** At each finite level the code is a Bell pair between the real oscillator and the
   finite places (§4). A positivity argument that runs level by level would need the archimedean half of the pair to be controlled exactly,
   which point 1 forbids. Open: whether the explicit formula's prime terms are the leakage between levels (§4 remark), and whether
   anything about the Bell structure survives the squeeze orbit beyond the Euler/theta unfolding of §7.

The language does not supply the positivity. It relocates the problem cleanly: **RH $\iff$ the squeeze correlation functional of the adelic GKP
qunaught, with its two zero modes removed, is a state.** For curves it is one because overlaps are counts and the theta divisor is ample.

## 13. Checks

`checks/check_adelic_gkp.py` (mpmath, 40 digits), output `checks/output.txt`, 73/73 pass:
C1 level-$N$ Poisson/self-duality ($N=1,2,3,6,12$, random Gaussians and random level-$N$ finite parts); C2 joint logical Paulis
$X_b\otimes X_b$, $Z_b\otimes Z_b^{-1}$; C3 $S$ and $T^2$ laws and the failure of $T$; C4 $\psi_2(x^2/2)=(-1)^x$ on $\mathbb Z$; C5 Tate's integral
$\int_0^\infty(\vartheta(ia^2)-1)a^s\,da/a=\pi^{-s/2}\Gamma(s/2)\zeta(s)$ at three points; C6 the signature of the off-line block.


## 14. A field extension: $K=\mathbb Q(\sqrt2)$

Added 2026-10-05 (TJO: "What about if I take a field extension of Q, eg sqrt2 and ask the same questions again"). Data: two real places,
$\mathcal O_K=\mathbb Z[\sqrt2]$, $h_K=1$, $d_K=8$, fundamental unit $\varepsilon=1+\sqrt2$ with $N\varepsilon=-1$, $\zeta_K=\zeta\cdot L(\cdot,\chi_8)$ with
$\chi_8(p)=(2/p)$. Character $\psi_K=\psi\circ\mathrm{Tr}_{K/\mathbb Q}$.

**14.1 The code is the same; the field is a torus (standard; phrasing mine).**
- $K\subset\mathbb A_K$ is discrete, cocompact and self-dual for $\psi_K$ (Tate), so $\Theta_K=\sum_{x\in K}\delta_x$ is a qunaught; Proposition 3's
  rigidity argument applies verbatim ($K$ divisible, $\mathbb A_K$ a $K$-vector space). Same answer to "what does it correct": nothing is
  encoded, every displacement is sensed modulo $K^2$.
- In the basis $\{1,\sqrt2\}$, $x=a+b\sqrt2$, one has $\mathbb A_K\cong\mathbb A^2$ and $\Theta_K=\Theta\otimes\Theta$. Phase space is canonically
  $V\oplus V^*$ with $V=K$ as a $\mathbb Q$-space; the trace form only identifies $V^*\cong V$. **As a two-mode adelic GKP state, $\Theta_K$ is the
  same for every quadratic field.**
- The stabiliser-preserving Clifford group of the two-mode code is $H(\mathbb Q^2)⋊\mathrm{Sp}_4(\mathbb Q)$, which contains $\mathrm{SL}_2(K)$
  (Hilbert modular symmetries, via restriction of scalars and the trace form) as the part commuting with $K$.
- Multiplication by $\alpha\in K^\times$ is a matrix in $\mathrm{GL}_2(\mathbb Q)$ on $(a,b)$: $\sqrt2\mapsto\begin{pmatrix}0&2\\1&0\end{pmatrix}$,
  $\varepsilon\mapsto\begin{pmatrix}1&2\\1&1\end{pmatrix}$ (Q3). The idelic squeezes of $K$ form the maximal torus $T_K(\mathbb A)\subset\mathrm{GL}_2(\mathbb A)$,
  and **$\zeta_K$ is the Mellin transform of the overlap with $\Theta\otimes\Theta$ along the $T_K$-orbit.** Quadratic fields correspond to
  conjugacy classes of non-split maximal tori; the split torus $\mathbb G_m\times\mathbb G_m$ gives $\zeta(s)^2$.

**14.2 Units: lattice-preserving squeezes between the real places (standard; checked Q3).** In the real embeddings $x\mapsto(\sigma_1x,\sigma_2x)$,
$\varepsilon$ acts as $\mathrm{diag}(1+\sqrt2,\ 1-\sqrt2)$: a two-mode squeeze, up to a sign, with net $|N\varepsilon|=1$. It is integral at every finite
place, so it fixes both the code and the finite vacuum $1_{\hat{\mathcal O}_K}$. On $\mathcal O_K\cong\mathbb Z^2$ it is the hyperbolic toral automorphism
$\begin{pmatrix}1&2\\1&1\end{pmatrix}$, a quantum cat map. Over $\mathbb Q$ the only such symmetries are $\pm1$. By Dirichlet, the unit squeezes
compactify the trace-zero archimedean squeeze direction to a circle of length $R_K=\log(1+\sqrt2)$ (up to a factor two from signs). Consequences:
the regulator enters the residue, $\mathrm{res}_{s=1}\zeta_K=2^{r_1}h_KR_K/(w_K\sqrt{|d_K|})=L(1,\chi_8)=\log(1+\sqrt2)/\sqrt2$ (Q1); and the Fourier modes on
that circle are Hecke's Grössencharaktere, a $\mathbb Z$-indexed family of $L$-functions on the same orbit. The dilation RH is about, $|x|_{\mathbb A_K}$,
is the norm direction, which units do not touch.

**14.3 Local vacua; the ramified prime is squeezed (standard; checked Q2, Q5, Q6).**
- Split $p\equiv\pm1\ (8)$: $K_p=\mathbb Q_p^2$, vacuum $1_{\mathbb Z_p}\otimes1_{\mathbb Z_p}$, local factor $(1-p^{-s})^{-2}$.
- Inert $p\equiv\pm3\ (8)$: $K_p=\mathbb Q_{p^2}$, vacuum $1_{\mathbb Z_{p^2}}$, local factor $(1-p^{-2s})^{-1}$.
- Ramified $p=2$: $K_2=\mathbb Q_2(\sqrt2)$, local factor $(1-2^{-s})^{-1}$. Here $\psi_{K,2}$ has conductor $\mathfrak{d}^{-1}$, $\mathfrak{d}=(2\sqrt2)=(\sqrt2)^3$,
  $N\mathfrak{d}=8$. The vacuum $1_{\mathcal O_2}$ is the qunaught of the **asymmetric** lattice $\mathcal O_2\times\mathfrak{d}_2^{-1}$, and Fourier maps it to
  $\propto1_{\mathfrak{d}^{-1}}$. A Fourier-symmetric $1_{\mathfrak{a}}$ would need $\mathfrak{a}^2=\mathfrak{d}^{-1}$, impossible with exponent $3$ odd (Q6).
  (Asymmetric qunaughts $1_M$, lattice $M\times M^\vee$, exist for every lattice $M$; what fails is symmetry under the S-gate.)

The Euler product by splitting type reproduces $\zeta(2)L(2,\chi_8)$ (Q2, relative error $4\times10^{-7}$ at primes $<2\times10^5$). **The discriminant
is the leftover squeeze of the vacuum**, and it is exactly the factor $|d_K|^{s/2}$ in the completed functional equation: Fourier maps $f_0^K$ to a
squeezed copy of itself, the squeeze being by a finite idele generating $\mathfrak{d}$. Minkowski's theorem that every proper extension of $\mathbb Q$ ramifies
reads: **every extension carries a squeezed local vacuum somewhere.** This is the number-field shadow of "no unramified (constant-field) tower";
analytic §14 argues the tower is not the blocker anyway.

**14.4 The archimedean side (standard; checked Q4, Q5).** Projecting the finite places onto their vacua gives, since $K\cap\hat{\mathcal O}_K=\mathcal O_K$, the
real two-mode qunaught on the Minkowski lattice $\sigma(\mathcal O_K)\times\sigma(\mathfrak{d}^{-1})\subset\mathbb R^2\times\mathbb R^2$, with
$\mathfrak{d}^{-1}=\frac1{2\sqrt2}\mathcal O_K$ the trace dual (Q5). Overlaps with Gaussian states are Hecke–Hilbert theta functions on $\mathbb H\times\mathbb H$,
e.g. $\sum_{x\in\mathcal O_K}e^{-\pi(t_1\sigma_1(x)^2+t_2\sigma_2(x)^2)}$. In $(a,b)$ the trace form is $\mathrm{diag}(2,4)$, $\sigma_1^2+\sigma_2^2=2a^2+4b^2$ (Q4), and
$1_{\hat{\mathcal O}_K}=1_{\hat{\mathbb Z}}(a)1_{\hat{\mathbb Z}}(b)$, so the $K$-vacuum is a product of two squeezed $\mathbb Q$-vacua and all the entangling sits in the
torus. This is a coincidence of $\mathbb Z[\sqrt2]$: for $\mathbb Z[\frac{1+\sqrt5}2]$ the trace form $\begin{pmatrix}2&1\\1&3\end{pmatrix}$ is not diagonal over $\mathbb Z$.
Either way there are two places with Gaussian sums instead of counts: **the archimedean blocker of §12 doubles.**

**14.5 For RH (standard).** $\zeta_K=\zeta\cdot L(\chi_8)$, so RH for $\zeta_K$ is RH for $\zeta$ together with GRH for $L(\chi_8)$: the extension contains
the original problem. In squeeze-state terms the push-forward of the $T_K$-orbit to the $\mathbb Q$ squeeze group along the norm splits into the trivial
sector ($\zeta$) and the $\chi_8$ sector, $\chi_8$ being the character of $C_{\mathbb Q}/N(C_K)\cong\mathrm{Gal}(K/\mathbb Q)$ (class field theory). The Galois
automorphism $b\mapsto-b$ is a parity Clifford that swaps the real places. Weil positivity for $K$ has the structure of §10: two zero modes, minus
local squeeze traces, now with two archimedean terms and the $|d_K|$ shift.

**Reading (heuristic).** The one structurally new resource is an infinite discrete group of lattice-preserving archimedean squeezes (units). That is
the closest a number field comes to symmetries a polarisation would provide; but units act only in the trace-zero directions, and RH is about the norm
direction. Open: whether the Grössencharakter family on the regulator circle (all of whose members satisfy GRH conjecturally) gives a positivity
statement uniform in the angular frequency that is easier than the trivial-character one.


## 15. Companion pages of 2026-10-05 (local session), and a steer on method

Eight pages written in one session with TJO, each with its own status table; rendered HTML next to each source.

| file | question (TJO) | result in one line | checks |
|---|---|---|---|
| `functional-equation-gate.md` | is $\Theta$ a qunaught because $\mathbb Q$ has no index-2 subgroup; is the functional equation an "S" gate? | Lagrangian gives the qunaught, divisibility gives rigidity; the gate is the Fourier gate (GKP Hadamard) | none |
| `weil-positivity-spectroscopy.md` | what does Weil positivity say in the most QI-friendly way? | the place-by-place echo is the autocorrelation of a unitary evolution; every line is sharp | `checks/check_weil_qi.py`, 29/29 |
| `graph-ihara.md` | redo it for a Ramanujan graph and the Ihara zeta: does the analogy hold or break? | breaks at the code, holds after; the step is CZ·Hadamard·squeeze; Weil positivity is $A^2\le4q$; lines are bright | `checks/check_graph_gkp.py`, 56/56 |
| `graph-super.md` | redo it for the super zeta, zeros from fermionic modes; find a lattice-like state in a bigger space | flux qubit on the period lattice; syndrome torus of the fermionic sector; RH on average over fluxes | `checks/check_super_gkp.py`, 50/50 |
| `lattice-tower.md` | investigate the tower of lattices | a tower of GKP codes with the step as a logical Clifford; blind to RH; RH is an invariant vacuum; ordinary case is a Deligne module | `checks/check_lattice_tower.py`, 45/45 |
| `howe-positivity.md` | take the next step: Howe's positivity on the ordinary examples | $\Omega$ is a polarisation for one mode and for a $K_6$ flux, never when $\pm\lambda$ both occur; explicit principal polarisation $\Omega(x,Py)$ for $K_4$ with one negative edge; vacuum $\ne$ arithmetic complex structure in general | `checks/check_howe_positivity.py` (needs cypari2), 14/14 |
| `sign-vector.md` | study what on the signed graph decides the per-mode sign | a single sign is free; the graph decides locks between modes whose Weil-form determinants agree up to squares, with an explicit residue sign; criterion for $\Omega$ to be a polarisation | `checks/check_sign_vector.py` (needs cypari2), 19/19 |
| `locks.md` | investigate the two open questions: a symmetry behind the locks; which fluxes have none | locks are finite-order rotations (half, quarter, sixth turns for integer spectra); only the half turn is a graph symmetry; bipartite graphs resolve on a Lagrangian half lattice with the biadjacency form; scan of 21069 flux classes | `checks/check_locks.py` (needs cypari2, networkx), 7/7 |

**Steer (TJO, 2026-10-05, verbatim).** "Let us find the natural QI interpreations on the cases we understand *then* try to match to corresponding analogous setting
for standard RH. Not the other way around. I am not convincd by the overlap thing in the case of standard zeta." Consequences for this note: Part II (§§6–12)
and `weil-positivity-spectroscopy.md` §1 start from the standard zeta and are to be read as provisional; `graph-super.md` and `lattice-tower.md` are the pages to build on.

Figures `fig_*.png` are written by the check scripts into this directory. Nothing registered; no REFUTE review; no shard.
