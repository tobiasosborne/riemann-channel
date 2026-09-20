Author: `codex:gpt-6-astra`

# 0. Conventions, hypotheses, and the scattering calculation

The requested geometric T1 needs a correction in the presence of bound states: deleting their data does not preserve orthogonality of the local incoming and outgoing spaces. Below, T1 gives an explicit counterexample, then repairs the construction by intersecting the projected outgoing space with the orthocomplement of the projected incoming space. This produces exactly the pole-removed scattering model. T3–T6 apply to that corrected contraction. The correction is necessary even for the pure cusp.

Hypotheses used, only where named:

- **H-SETUP:** $n\geq1$, $T_X=T_X^{\mathsf T}$ is real, $e_0$ is a unit coordinate vector, $P_0=e_0e_0^*$, and $c>0$. The formulas in $q$ require $q>1$; for the actual $\mathbb F_q[T]$ quotient, $q$ is a prime power.
- **H-LOCAL:** there are no *visible* bound states outside $[-2,2]$, after deleting the core modes invisible at $e_0$. This is used for identifying the local wave compression with the Hardy model without changing the radiation spaces.
- **H-SIMPLE:** the retained resonance roots are distinct. Only eigenbasis formulas require this; the model itself allows multiplicities.
- **H-NONEMPTY:** the retained model space has positive dimension. A zero-dimensional space has no density matrices.
- **H-INVERT:** $c^2\ne1$, when expanding $\log p$ at zero without first extracting its zero there.
- **H-REG:** for the Bass comparison only, $A_X$ is the adjacency matrix of a $(q+1)$-regular finite graph and $T_X=A_X/\sqrt q$.
- **H-CONTRACTION:** in T3–T5, $K$ is finite dimensional and nonzero, $C^m\to0$, and $I-C^*C=jj^*$. The flag argument also works with an arbitrary positive defect.
- **H-APERIODIC:** $\gcd\{m\geq1:m_\Omega(m)>0\}=1$.
- **H-PERRON:** when using the literal Perron terminology in T7, the weighted graph is nonnegative and connected. If there is no isolated positive eigenvalue above $2$, there is no positive $\ell^2$ Perron mode to exempt. A negative twin is exempted only for a bipartite graph.
- **H-ARITH:** the unproved arithmetic identifications specified in Section 8. None is used in Sections 0–7.

Inner products are conjugate linear in the first argument. Algebraic multiplicities are counted. A resonance at $z=0$ means a zero of the rational scattering function at zero; it is a delay mode, not a finite value of $\lambda=z+z^{-1}$.

The Hilbert space and operator are

$$
\mathcal H=\mathbb C^n\oplus\ell^2(\mathbb N),\qquad
T=T_X\oplus T_{\rm ray}+c(|e_0\rangle\langle r_1|+|r_1\rangle\langle e_0|),
$$

where $(T_{\rm ray}g)_1=g_2$ and $(T_{\rm ray}g)_k=g_{k-1}+g_{k+1}$ for $k\geq2$. It is bounded and self-adjoint, being a bounded self-adjoint direct sum plus a symmetric rank-two operator. Throughout $\lambda=z+z^{-1}$.

## C1. Normalisation and reflection — STATUS: CORRECTED

**Tree normalisation.** Detailed balance requires

$$
m_0(q+1)=m_1q,\qquad m_n=m_{n+1}q\quad(n\geq1).
$$

Thus, with $m_0=1$, $m_n=(q+1)q^{-n}$ for $n\geq1$. Under $g_n=\sqrt{m_n}f_n$, a directed coefficient $a_{ij}$ becomes $\sqrt{m_i/m_j}\,a_{ij}$. The interior coefficients become $\sqrt q$, and the junction coefficient becomes $\sqrt{q(q+1)}$. Dividing by $\sqrt q$ gives the stated ray and **$c^2=q+1$**, as proposed. This proves the normalisation directly from the stated edge indices; Serre's quotient description itself is standard (no local source).

The substitution $z=q^{s-1/2}$ has the stated disk/half-plane correspondence and imaginary period $2\pi/\log q$. But the height assertion needs orientation care. With the quotient index $n$ increasing up the cusp, solutions in the original weighted space are $f_n=q^{sn}$ and $q^{(1-s)n}$, up to constants; they become $g_n=z^n$ and $z^{-n}$. Indeed the original recurrence gives eigenvalue $q^s+q^{1-s}$. The algebraic identity $q^{-sh}=q^{-h/2}z^{-h}$ is true, but $q^{-sn}$ is not a solution with that eigenvalue for the stated quotient recurrence. The tree convention $q^{-sh}$ must use $h=-n$ here.

**Reflection.** Put $G(\lambda)=e_0^*(\lambda-T_X)^{-1}e_0$. Substitution of $g_k=z^{-k}+Rz^k$ at $r_1$ and on the core gives

$$
cg_0=1+R,\qquad
g_X=c(z^{-1}+Rz)(\lambda-T_X)^{-1}e_0,
$$

and consequently

$$
R(z)=\frac{1-c^2G(\lambda)z^{-1}}{c^2G(\lambda)z-1}
=-\frac{\det(\lambda-T_X-c^2z^{-1}P_0)}{\det(\lambda-T_X-c^2zP_0)}
=-\frac{p(z)}{\widetilde p(z)},                                      \tag{0.1}
$$

$$
p(z)=\det((1+z^2)I-zT_X-c^2P_0),\qquad
\widetilde p(z)=\det((1+z^2)I-zT_X-c^2z^2P_0)=z^{2n}p(1/z).
$$

There is a **minus sign and no extra power of $z$**. The determinant lemma proves (0.1) off the finitely many core eigenvalues; rational continuation proves it everywhere it is defined. Both polynomials have real coefficients, $p$ is monic of degree $2n$, $p(0)=1-c^2$, and $\widetilde p(0)=1$. Hence

$$
R(z)R(1/z)=1,\qquad R(\bar z)=\overline{R(z)}.
$$

On $|z|=1$, $1/z=\bar z$, so $|R|=1$. Apparent exceptional points are interpreted after cancellation; there are no remaining unit-circle poles. The exact rational degree is $2d-\tau$, with $d$ and $\tau$ defined next. In particular it need not be $2n$.

## C2. What scattering sees — STATUS: CORRECTED

Let

$$
X_b=\operatorname{span}\{T_X^ke_0:k\geq0\},\quad d=\dim X_b,\quad X_c=X_b^\perp.
$$

The subspace $X_c$ is invariant. It is exactly the direct sum of the core eigenspaces consisting of vectors vanishing at $e_0$. Write their dimensions as $m_c(t)$ and set

$$
D_c(z)=\prod_t(1-tz+z^2)^{m_c(t)},\qquad \sum_t m_c(t)=n-d.
$$

Restricting to $X_b$ gives polynomials $p_b,\widetilde p_b$ with $p=D_cp_b$ and $\widetilde p=D_c\widetilde p_b$. The spectral measure of $e_0$ on $X_b$ has positive weights at $d$ distinct eigenvalues. Consequently its characteristic polynomial $D(\lambda)$ and the numerator $B(\lambda)$ of $G=B/D$ are coprime.

**C2(i–ii). Visible bound states.** The poles of the reduced $R$ in the open disk are simple, real, nonzero numbers $\beta\in(-1,1)$, in bijection with the eigenfunctions of $T$ outside the band that have a nonzero ray component. They satisfy

$$
(\lambda-T_X-c^2\beta P_0)x=0,\qquad
g_k=cx_0\beta^k,\qquad \lambda=\beta+\beta^{-1}.             \tag{0.2}
$$

To prove this, eliminate the decaying ray solution. Conversely (0.2) constructs an $\ell^2$ eigenfunction. A nonreal disk root of the denominator would give a nonreal eigenvalue, since
$\operatorname{Im}(z+z^{-1})=\operatorname{Im}z(1-|z|^{-2})$, contradicting self-adjointness. A visible eigenspace has dimension one: any linear combination cancelling $x_0$ also cancels the ray and is a cusp form. In the cyclic sector the scalar resolvent has a simple pole with nonzero positive spectral mass; $d\lambda/dz\ne0$ at $\beta$, so the scattering pole is simple. Core cusp forms outside the band are additional $\ell^2$ eigenfunctions and are **not** poles of $R$. Calling all visible bound states “trivial” is a bookkeeping convention, not a Perron theorem.

**C2(iii). Exact cancellation.** Define

$$
E_{\rm th}=\{\epsilon\in\{1,-1\}:p_b(\epsilon)=0\},\qquad
\tau=|E_{\rm th}|,\qquad H(z)=\prod_{\epsilon\in E_{\rm th}}(z-\epsilon).
$$

Then, up to a nonzero constant,

$$
\gcd(p,\widetilde p)=D_cH.                                  \tag{0.3}
$$

Indeed, away from $0,\pm1$, a common zero would give simultaneously
$D(\lambda)-c^2z^{-1}B(\lambda)=D(\lambda)-c^2zB(\lambda)=0$,
contradicting coprimality. At zero $\widetilde p_b=1$. At $\epsilon=\pm1$, a common zero is a threshold solution. Here $B(2\epsilon)\ne0$, and differentiating $z^d[D(z+z^{-1})-c^2z^{-1}B(z+z^{-1})]$ shows that the zero of $p_b$ is simple; the same holds for $\widetilde p_b$. These solutions have constant or alternating, nondecaying tails and are not $\ell^2$ eigenfunctions. Thus common factors are **not only cusp forms**. For example $n=1$, $a=T_X=3/2$, $c^2=1/2$ gives $p=(z-1)(z-1/2)$ and $\widetilde p=(z-1)(z-2)/2$.

There are no other unit-circle roots of $p_b$: for $z\ne\pm1$ the imaginary part of the effective equation forces $x_0=0$, and cyclicity excludes the resulting core eigenvector. Cusp forms extend by zero to eigenfunctions of $T$, inside or outside the band; an $\ell^2$ solution in the band must have zero tail and hence be such a form. This also covers the endpoints.

**C2(iv). Resonances and their number.** Let $b$ be the number of visible bound states and let $z_1,\ldots,z_N$ be the zeros of reduced $R$ in $|z|<1$. For $z_i\ne0$ they are exactly the noncancelled solutions

$$
(T_X+c^2z_i^{-1}P_0)x=(z_i+z_i^{-1})x.                      \tag{0.4}
$$

The continued tail is $g_k=cx_0z_i^{-k}$. It grows spatially; with time factor $z_i^m$ it is outgoing, $z_i^{-(k-m)}$. Equation (0.2) uses the decaying, physical resolvent branch; (0.4) uses its continuation to the other sheet. Complex roots occur in conjugate pairs. The exterior roots of $p_b$ are precisely $\beta^{-1}$, by reciprocity. Therefore

$$
\boxed{N=2d-b-\tau=2n-2\sum_t m_c(t)-b-\tau.}              \tag{0.5}
$$

This counts zero roots. If finite-$\lambda$ resonances alone are desired, subtract $\operatorname{ord}_0p$. Under H-INVERT this order is zero. The rational degree of $R$ is $2d-\tau$, since its reduced numerator still has that degree, even when the denominator has lower degree.

## C3. The pure cusp and the meaning of $\phi$ — STATUS: CORRECTED

For $T_X=[0]$, $c^2=q+1$,

$$
R(z)=\frac{z^2-q}{qz^2-1},\quad
\beta=\pm q^{-1/2},\quad z_{\rm zero}=\pm q^{1/2},\quad N=0.
$$

The bound eigenvalues are $\pm(q+1)/\sqrt q$. The positive eigenfunction is $g=\sqrt m$, corresponding to the constant function in $L^2(Y,m)$; alternating its signs gives the negative one. This verifies all the proposed roots.

For $\zeta_K(s)=((1-q^{-s})(1-q^{1-s}))^{-1}$, cancellation gives exactly

$$
q\frac{\zeta_K(2s-1)}{\zeta_K(2s)}
=q\frac{1-q^{-2s}}{1-q^{2-2s}}
=\frac{qz^2-1}{z^2-q}=\frac1{R(z)}.                         \tag{0.6}
$$

Thus **$\phi=1/R$** is the convention having the pole at $s=1$ and zero at $s=0$. There are their translates by $\pi i/\log q$, not just one pole and zero in the entire $s$-plane. There are no further ones modulo this period. On the principal logarithm sheet the positive and negative $z$ roots account for these two translates in a $2\pi i/\log q$ strip.

Incoming/outgoing labels must include a time convention. With $u_m=z^mg$, $z^{-k}$ is outgoing and $z^k$ incoming; the ansatz in the brief then has incoming/outgoing ratio $R$, and outgoing/incoming ratio $\phi$. Reversing time reverses those words. In the Hardy contraction convention below, the relevant *inner function* is $R$ with its disk poles removed, not the meromorphic $\phi$ and not the unmodified meromorphic $R$.

One additional continuous normalisation caveat: the entire $\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ printed in `sec:riemann-channel`, `report/sections/04_riemann_channel.tex:27`, differs from the meromorphic completion $\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$. The usual modular coefficient is $\Lambda(2s-1)/\Lambda(2s)$, whereas $\xi(2s-1)/\xi(2s)=(s-1)\phi_{\rm modular}(s)/s$. The factors controlling the pole at $1$ cannot be suppressed in that comparison. The usual coefficient convention is standard (no local source); this algebra is immediate.

# 1. T1: wave dynamics and the specified contraction

## T1(a). Energy and local radiation — STATUS: CORRECTED

For pairs $(u,v)=(u_0,u_{-1})$, polarise the given energy as

$$
\langle(u,v),(x,y)\rangle_E
=\langle u,x\rangle+\langle v,y\rangle
-\tfrac12(\langle u,Ty\rangle+\langle v,Tx\rangle).
$$

Expanding $E(Tu-v,u)$ and using $T=T^*$ gives $E(Tu-v,u)=E(u,v)$. Also $W^{-1}(u,v)=(v,Tv-u)$. On every ray region unaffected by the junction,
$u_m(k)=F(k+m)+B(k-m)$ solves the equation by substitution. Conversely the difference equations for $F$ and $B$ determine them separately on the two parity classes from two adjacent time slices, up to the cancelling parity constants. Iterating the nearest-neighbour recurrence proves propagation speed one along the ray. A general weighted core need not have a meaningful metric of speed one except its edge metric.

Let $S$ be the unilateral shift on ray sequences. Initially use finitely supported profiles, extended by zero to nonpositive indices. Local radiation data are

$$
D_+^0=\{(B,S^*B):B_1=0,\ \text{core data }0\},\qquad
D_-^0=\{(F,SF):\text{core data }0\}.
$$

Here $WD_+^0\subset D_+^0$ and $W^{-1}D_-^0\subset D_-^0$, not invariance in both time directions. On $D_+^0$, $W$ shifts $B$ upwards; on $D_-^0$, $W^{-1}$ shifts $F$ upwards. Their energies are

$$
E(B,S^*B)=\tfrac12\sum_{k\geq0}|B_{k+2}-B_k|^2,
\qquad E(F,SF)=\tfrac12\sum_{k\geq1}|F_k-F_{k-2}|^2.          \tag{1.1}
$$

The two difference maps have dense range in $\ell^2(\mathbb N_0)$: the adjoint of $I-S^2$ has no nonzero $\ell^2$ kernel. They intertwine the respective forward evolutions with the unilateral shift. Their completions therefore have multiplicity **one**. Direct substitution into the polarised energy gives $D_+^0\perp_E D_-^0$. Energy completion, rather than the counting-measure norm of profiles, matters in these statements.

## T1(b). The positive wave space — STATUS: PROVED

Delete *all* point-spectrum data in each component: visible bound states and every cusp form, including any cusp forms outside the band. Equivalently take $\mathcal H_{\rm ac}\oplus\mathcal H_{\rm ac}$ and complete in $E$; call the result $\mathcal H_E$. This definition also avoids taking a possibly degenerate energy orthocomplement of a threshold cusp form. Away from thresholds it agrees with deleting the full two-dimensional wave blocks in the energy sense.

There is no singular continuous spectrum here. For example, finite Schur elimination expresses the resolvent of the cyclic part rationally in $\lambda$ and $\sqrt{\lambda^2-4}$; its measure on the open band has a smooth density except at finitely many points, and any remaining singular support is finite and hence atomic. The invisible part is finite dimensional.

On the spectral fibre of $T$ with parameter $\lambda\in(-2,2)$, the energy matrix is

$$
\begin{pmatrix}1&-\lambda/2\\-\lambda/2&1\end{pmatrix},
$$

with positive eigenvalues $1\pm\lambda/2$. Thus $E>0$ on nonzero data in the point-spectrum complement, although it is not uniformly equivalent to the original norm at the band edges. Energy invariance and the inverse formula extend $W$ to a unitary on $\mathcal H_E$. Diagonalising each fibre gives time eigenvalues $e^{\pm i\theta}$ for $\lambda=2\cos\theta$. The cyclic continuous spectrum has multiplicity one, so together these two arcs give a scalar bilateral-shift representation $W\simeq M_w$ on $L^2(\mathbb T)$.

## T1(c). The geometric obstruction and its repair — STATUS: CORRECTED

The local $D_\pm^0$ generally do not belong to $\mathcal H_E$. Nor can one simply project them there and retain their orthogonality. Here is an exact counterexample. In the pure cusp with $q=2$, take

$$
a=(r_2,r_1)\in D_+^0,\qquad b=(r_2,r_3)\in D_-^0.
$$

Their energy pairing is zero. Let $Q$ delete both normalised bound eigenfunctions in each component. For a bound parameter $\beta=\pm1/\sqrt2$, its normalised ray values are $f_k=f_1\beta^{k-1}$, $|f_1|^2=3/8$. Its contribution to the pairing of $a,b$ is

$$
f_2^2+f_1f_3-\tfrac\lambda2(f_2f_3+f_1f_2)
=-\tfrac12f_1^2(1-\beta^2)^2=-3/64.
$$

Consequently $\langle Qa,Qb\rangle_E=3/32\ne0$. The proposed orthogonal sum $D_+\oplus D_-$ after this deletion is unavailable. A general discrete wave scattering construction with indefinite energy likewise distinguishes the original radiation data from their projections; see the discussion preceding Lemma 5 of [Kurasov, *Scattering from an Impurity: Lax–Phillips approach*](https://staff.math.su.se/kurasov/PDFARCHIV/LAXFINAL.pdf). The counterexample above is independent of that reference.

Here is the exact replacement used for the rest of this note. First write the scattering factorisation. For $a\in\mathbb D$, let $b_a(w)=(w-a)/(1-\bar a w)$, and set

$$
B_{\rm bd}(w)=\prod_{\beta}b_\beta(w),\qquad
\Theta(w)=\eta\,R(w)B_{\rm bd}(w)=\prod_{i=1}^N b_{z_i}(w),   \tag{1.2}
$$

where $|\eta|=1$ fixes the displayed normalisation. The divisor calculation in C2 proves (1.2): all disk poles cancel, the remaining disk zeros are precisely the resonances, and a rational function without remaining zeros or poles and with unit boundary modulus is constant. The zero factor $b_0(w)=w$ is included. Since the roots are conjugation closed, $\Theta$ can and will have real coefficients.

We now identify the required change of radiation spaces geometrically. Let $Q$ delete the full point-spectrum blocks, and write $\mathcal O_\pm$ for the energy-completed images of $D_\pm^0$ under $Q$. These images are still isometric shifts. To see this without an indefinite-space projection estimate, let $f$ be a bound eigenfunction with parameter $\beta$. For outgoing data the two coefficients along $f$ are $(a,a/\beta)$; for incoming data they are $(a,\beta a)$. In either case their bound-block energy is zero, since $\lambda=\beta+\beta^{-1}$. The same calculation for two profiles shows that deleting the bound block preserves the entire inner product on each radiation space separately. Cusp forms have zero pairing with either space. Thus $Q$ extends isometrically on each of the completions in (1.1), even though it does not preserve their cross pairing.

Choose the incoming translation representation $U:\mathcal H_E\to L^2(\mathbb T)$ so that

$$
UWU^{-1}=M_w,\qquad U\mathcal O_-=L^2\ominus H^2.
$$

Here is also a direct way to fix the phase and delay. The unit wandering profiles in (1.1) are $B_{2l+2}=\sqrt2$, $B_{2l+1}=0$ for the outgoing space and $F_{2l+1}=\sqrt2$, $F_{2l+2}=0$ for the incoming space, $l\geq0$. They are understood as energy limits of tapered profiles. Denote their projected data by $\gamma_+,\gamma_-$. Set $U\gamma_-=w^{-1}$. The wave eigenfunction $g_k=w^{-k}+R(w)w^k$ with temporal factor $w^m$ gives, by the polarised energy and geometric summation of these profiles,

$$
\frac{(U\gamma_+)(w)}{(U\gamma_-)(w)}=-wR(w),\qquad
U\gamma_+=-R(w).                                          \tag{1.2a}
$$

For clarity, the common spectral factor cancels: the pairings are proportional to $-(1-w^2)$ and $(1-w^2)\overline{R(w)}w^{-1}$, respectively. The sums may first be Abel-regularised; the result holds almost everywhere on the circle. This also proves completeness of the incoming translates: the displayed incoming amplitude is nonzero almost everywhere in the single continuous wave channel. Their orthonormality follows from the wandering-vector property and unitarity. Consequently $U\mathcal O_+=R H^2$; (1.2a) shows that no unrecorded power of $w$ is present.

Keep the projected incoming space, and take the largest subspace of projected outgoing data orthogonal to it:

$$
D_-=\mathcal O_-,\qquad D_+=\mathcal O_+\cap\mathcal O_-^\perp. \tag{1.2b}
$$

In translation coordinates,

$$
UD_+=RH^2\cap H^2=\Theta H^2.
$$

Indeed $Rf$ is analytic in the disk exactly when $f$ vanishes at every pole $\beta$, equivalently $f\in B_{\rm bd}H^2$; numerator and denominator have no common disk root. Thus (1.2b) imposes exactly $b$ independent scalar conditions on outgoing profiles. It is forward invariant, is a multiplicity-one shift, and its bilateral translates are complete. This is a concrete correction of the local construction, not a mere assignment of an arbitrary scattering phase. Under H-LOCAL no correction is needed, because $B_{\rm bd}=1$.

Define, equivalently in these translation coordinates,

$$
\mathcal K_\Theta=H^2\ominus\Theta H^2,\quad
D_-^{\rm mod}=L^2\ominus H^2,\quad D_+^{\rm mod}=\Theta H^2,
\quad Z=P_{\mathcal K_\Theta}M_w|_{\mathcal K_\Theta},\quad C=Z^*.
$$

These are exactly the orthogonal Lax–Phillips spaces obtained in (1.2b). On the wave space set $K=\mathcal H_E\ominus(D_+\oplus D_-)$; its compression is carried by $U$ to $Z$ above. The use of (1.2b), rather than just projecting both local spaces, is essential.

The model has

$$
\dim\mathcal K_\Theta=N,\qquad \operatorname{spec}Z=\{z_i\},
\qquad\operatorname{spec}C=\{\bar z_i\}=\{z_i\},\qquad Z^m,C^m\longrightarrow0.
$$

For completeness, $K_{\theta_1\theta_2}=K_{\theta_1}\oplus\theta_1K_{\theta_2}$, and each single Blaschke factor has a one-dimensional model space. This proves the dimension. Reproducing kernels at the zeros, and their derivatives at repeated zeros, give the eigenvalues with their Jordan multiplicities. Finite dimension and $|z_i|<1$ prove norm decay.

We use **$C=Z^*$** for the renewal channel. Its defects have the explicit vectors

$$
j=P_{\mathcal K_\Theta}1=1-\overline{\Theta(0)}\Theta,
\qquad j'=S^*\Theta=\frac{\Theta(w)-\Theta(0)}w,
$$

$$
I-C^*C=jj^*,\qquad I-CC^*=j'j'^*.                           \tag{1.3}
$$

Indeed $C=S^*|_{\mathcal K_\Theta}$, so $\|f\|^2-\|Cf\|^2=|f(0)|^2$. For the other identity, the only component of $wf$ outside $\mathcal K_\Theta$ is its component along $\Theta$, equal to $\langle S^*\Theta,f\rangle\Theta$. These prove (1.3). For $Z$ the two vectors are interchanged. The “first ray datum” in (1.3) is the first **normalised translation coordinate**, $1$ in $H^2$, not the unnormalised vertex vector $r_1$: on the wave space it is explicitly $j=P_KW\gamma_-$. The other vector is $P_KW^{-1}\gamma_+^{\rm new}$, where $U\gamma_+^{\rm new}=\Theta$ is the unit wandering datum of the restricted outgoing space.

Under H-SIMPLE, label eigenvectors of $C$ by

$$
k_i(w)=\frac1{1-z_iw},\quad Ck_i=z_ik_i,\quad
G_{ij}=\langle k_i,k_j\rangle=\frac1{1-\bar z_i z_j},\quad
\langle j,k_i\rangle=1.                                    \tag{1.4}
$$

These kernels belong to $K_\Theta$ because $\Theta(\bar z_i)=0$. If $V$ has columns $k_i$, the coordinate vector of $j$ is $G^{-1}\mathbf1$: $j=VG^{-1}\mathbf1$. Normalised modes $e_i=\sqrt{1-|z_i|^2}\,k_i$ have exit amplitude $\sqrt{1-|z_i|^2}>0$. In coordinates (1.3) is $G-D^*GD=\mathbf1\mathbf1^*$, $D=\operatorname{diag}(z_i)$. More generally an eigenvector with zero exit would satisfy $\|Cv\|=\|v\|$ and $|z|<1$, an impossibility. Derivative kernels replace (1.4) at repeated roots, with differentiated Gram entries.

## T1(d). Precisely which standard theorem is used — STATUS: CORRECTED

The discrete Lax–Phillips/Sz.-Nagy–Foias model theorem is standard (no local source): a minimal scalar unitary scattering system with orthogonal incoming/outgoing shift spaces and inner transfer symbol $\Theta$ has compression unitarily equivalent to $P_{H^2\ominus\Theta H^2}M_w$, whose characteristic function is $\Theta$ up to constant phases. Conversely this Hardy construction is such a scattering system. The direct construction (1.2a–b) verifies its hypotheses here and identifies the characteristic function with the pole-removed $\eta RB_{\rm bd}$. Under H-LOCAL this is simply $R$ up to a constant phase.

Here the Lax–Phillips scattering multiplier takes outgoing translation coordinates to incoming translation coordinates. This specifies why it is the inverse of the outgoing/incoming amplitude convention $\phi$ in C3.

Without H-LOCAL, the theorem cannot be applied to the projected local spaces as an orthogonal pair; (1.2b) is the additional step. Calling $R$ or $1/R$ itself a characteristic function in the bound-state case would be false. The eigenvectors in (1.4) belong to the adjoint compression convention, just as in `obs:model-modes-sign`, `report/sections/04h_rebound_state.tex:36`; compare the model identification in `prop:functional-model-modes`, `report/sections/04_riemann_channel.tex:68`.

# 2. T2: walks, determinants, and the cusp term

## T2(a). Explicit walk series and power sums — STATUS: CORRECTED

Under H-REG, $u=z/\sqrt q$ gives the Bass vertex determinant $\det(I-uA_X+qu^2I)=\det(I-zT_X+z^2I)$. The full Ihara–Bass formula also has the factor $(1-u^2)^{|E|-|V|}$; it must not be silently equated with this vertex determinant. The notebook's analogous inverse-pairing convention is `cor:qihara-unitary`, `report/sections/08_quantum_ihara_general.tex:100`. For an arbitrary weighted core only the displayed determinant identity, not a regular-graph Ihara interpretation, is being asserted.

Write $A=T_X$ and $D=I-c^2P_0$. Near zero,

$$
\log\widetilde p(z)=-\sum_{\ell\geq1}\frac1\ell
\operatorname{tr}(zA-z^2D)^\ell.                            \tag{2.1}
$$

Under H-INVERT, a local branch also gives

$$
\log p(z)=\log\det D-\sum_{\ell\geq1}\frac1\ell
\operatorname{tr}(zD^{-1}A-z^2D^{-1})^\ell.                 \tag{2.2}
$$

The proof is $\log\det(I-M)=-\sum_{\ell\geq1}\operatorname{tr}M^\ell/\ell$, initially for $\|M\|<1$. Each trace expands as the sum over cyclic vertex sequences and all ordered choices of the two displayed matrix factors. An $A$ factor traverses a weighted core edge, a diagonal factor stays at its vertex with the displayed sign and weight, and its $P_0$ part marks an insertion at the junction. These are **signed weighted walks**, not necessarily nonnegative counts. Matrix-factor order is retained; a scalar binomial expansion is not valid.

An equivalent insertion expansion makes the Bass determinant explicit. For $H_0(z)=I-zA+z^2I$ and $h(z)=e_0^*H_0(z)^{-1}e_0$,

$$
\log p=\log\det H_0+\log(1-c^2h),\qquad
\log\widetilde p=\log\det H_0+\log(1-c^2z^2h).             \tag{2.3}
$$

Expand $H_0^{-1}=\sum_{r\geq0}(zA-z^2I)^r$ and $\log(1-x)=-\sum_{r\geq1}x^r/r$ where convergent. The first insertion series is not convergent near zero when $c^2>1$; there use (2.2), or regard (2.3) as a coupling-variable expansion followed by rational continuation. If $c^2=1$, factor $p=z^\ell p_0$, $p_0(0)\ne0$, and expand $\log p_0+\ell\log z$ instead.

There is a particularly useful formula that needs no H-INVERT. Since $p$ is monic,

$$
\log\widetilde p(w)=\log(w^{2n}p(1/w))
=-\sum_{m\geq1}\frac{w^m}{m}\sum_{p(\alpha)=0}\alpha^m.
$$

Let $a_t,a_t^{-1}$ be the roots of $1-tz+z^2$. Then, for $m\geq1$,

$$
\boxed{\sum_{i=1}^Nz_i^m
=-m[w^m]\log\widetilde p(w)
-\sum_t m_c(t)(a_t^m+a_t^{-m})
-\sum_{\epsilon\in E_{\rm th}}\epsilon^m
-\sum_{\beta}\beta^{-m}.}                                 \tag{2.4}
$$

This follows simply by partitioning the roots of $p$ as in C2. Expanding $\log p$ at zero instead gives inverse-root sums; confusing these with the positive power sums reverses the trace formula. Zero roots contribute zero to (2.4); their number must be obtained from the degree/count formula.

## T2(b). Logarithmic derivative — STATUS: PROVED

$$
-\frac{R'(z)}{R(z)}=-\frac{p'(z)}{p(z)}+
\frac{\widetilde p'(z)}{\widetilde p(z)}.                    \tag{2.5}
$$

Differentiating (2.1)–(2.2) proves the requested difference of walk expansions; the common Bass term cancels in (2.3). For $c^2=1$ the $-\ell/z$ term must be retained. Alternatively (1.2) gives a short resonance/bound-state formula:

$$
-R'/R=-\sum_i\left(\frac1{z-z_i}+\frac{\bar z_i}{1-\bar z_i z}\right)
+\sum_\beta\left(\frac1{z-\beta}+\frac{\beta}{1-\beta z}\right).
$$

This is a finite rational cusp contribution, not a prime comb. The notebook's arithmetic comb is `prop:cusp-prime-comb`, `report/sections/09c_selberg_tower_cusp.tex:78`.

## T2(c). Which ray excursions are summed — STATUS: CORRECTED

The physical half-line Weyl function is

$$
m_{\rm ray}(\lambda)=\langle r_1,(\lambda-T_{\rm ray})^{-1}r_1\rangle
=\frac{\lambda-\sqrt{\lambda^2-4}}2=z,\quad |z|<1.
$$

Indeed deleting $r_1$ leaves the same half-line, so $m=(\lambda-m)^{-1}$; the branch $m\sim\lambda^{-1}$ selects this solution. For $|\lambda|>2$,

$$
z=\sum_{r\geq0}\frac{{\rm Cat}_r}{\lambda^{2r+1}},\qquad
{\rm Cat}_r=\frac1{r+1}\binom{2r}r.
$$

The coefficient counts walks of length $2r$ from $r_1$ to $r_1$ staying on the ray. Adding the two junction edges produces a core-to-core excursion of length $2r+2$, weight $c^2{\rm Cat}_r$, and Schur self-energy $c^2z$. Repeated excursions are then summed by the core resolvent/determinant insertion series. The expression $c^2/z$ is the **second-sheet analytic continuation**, not another convergent positive walk sum at infinity: $c^2/z=c^2\lambda-c^2z$. Nothing in these Catalan excursions labels monic irreducibles. Such labels would have to enter through the arithmetic core, stabiliser weights and global scattering calculation.

# 3. T3: the discrete renewal channel

The following uses H-CONTRACTION, and for the graph model H-NONEMPTY. The no-event operator is $C=Z^*$ as in (1.3). The notebook counterparts are `def:rebound-renewal-generator`, `report/sections/04h_rebound_state.tex:62`, and `thm:rebound-renewal`, `report/sections/04h_rebound_state.tex:78`.

## T3(a). Complete positivity and conservation — STATUS: PROVED

For a density $\Omega=\sum_i p_i|\omega_i\rangle\langle\omega_i|$, define

$$
\mathcal E_\Omega(X)=CXC^*+\ell(X)\Omega,\qquad
\ell(X)=\langle j,Xj\rangle.
$$

The Kraus operators are $C$ and $\sqrt{p_i}|\omega_i\rangle\langle j|$. Their adjoint products sum to $C^*C+jj^*=I$, proving CPTP. There is no GKLS limit being assumed.

## T3(b). Holding times — STATUS: PROVED

Let $s_m=\operatorname{Tr}(C^m\Omega C^{*m})$. The defect identity gives

$$
m_\Omega(m)=\ell(C^{m-1}\Omega C^{*(m-1)})=s_{m-1}-s_m.
$$

Here $s_0=1$, $s_m\downarrow0$. Telescoping proves total mass one and the tail-sum formula

$$
\mu_\Omega=\sum_{m\geq1}m\,m_\Omega(m)=\sum_{m\geq0}s_m<\infty.
$$

Finite-dimensional stability bounds $\|C^m\|$ by a polynomial times $r^m$ for some $r<1$, proving finiteness. Thus the infinite-mean phenomenon of `prop:infinite-mean-rebound`, `report/sections/04h_rebound_state.tex:101`, cannot occur in this finite toy.

## T3(c). Stationarity, uniqueness, and periodicity — STATUS: CORRECTED

Put $\mathcal E_0(X)=CXC^*$ and

$$
S_\Omega=(I-\mathcal E_0)^{-1}\Omega
=\sum_{m\geq0}C^m\Omega C^{*m},\qquad
\rho_\infty=S_\Omega/\mu_\Omega.                            \tag{3.1}
$$

Telescoping gives $(I-\mathcal E_0)S_\Omega=\Omega$ and $\ell(S_\Omega)=1$, proving stationarity. Conversely any stationary density satisfies $\rho=\ell(\rho)S_\Omega$, and trace one forces (3.1). **Uniqueness holds even for a periodic law.** Attraction of every density holds exactly under H-APERIODIC.

Here is a finite-dimensional proof of the last assertion, without a renewal-limit assumption. On $|u|=1$, $I-u\mathcal E_0$ is invertible. The determinant identity in T3(e) says that a peripheral eigenvalue $\lambda=u^{-1}$ occurs exactly when

$$
1=\widehat m_\Omega(u)=\sum_{m\geq1}m_\Omega(m)u^m.
$$

Equality in the triangle inequality forces $u^m=1$ on the support, equivalently $u^d=1$, where $d$ is its gcd. Each such zero of $1-\widehat m$ is simple, because $\widehat m'(u)=\mu_\Omega/u$. Thus the peripheral eigenvalues are exactly the $d$th roots of unity, each simple. All other eigenvalues are strictly inside the disk. For $d=1$ this proves convergence to the unique stationary state. For $d>1$, a peripheral eigenoperator gives a nonconvergent Hermitian traceless perturbation of a sufficiently positive density, so attraction of every density fails.

Periodicity is possible even with nonreal resonances. For $0<r<1$, take

$$
C=\begin{pmatrix}0&1\\-r^2&0\end{pmatrix},\quad
j=\sqrt{1-r^4}\binom10,\quad \Omega=|e_2\rangle\langle e_2|.
$$

Its eigenvalues are $\pm ir$, $m(2k)=(1-r^4)r^{4(k-1)}$, $m(2k-1)=0$, and $\rho_\infty=I/2$. The channel swaps the two coordinate pure states. Therefore a nonzero modal expansion or overlap with a nonreal mode does not imply aperiodicity. If, more strongly, the range of $\Omega$ **contains an eigenvector** of $C$, then $m(1)>0$: otherwise $j$ would be orthogonal to that range, contradicting the nonzero exit of an eigenvector. In particular every modal mixture, and every pure resonance eigenstate, is aperiodic. These meanings of “support on a resonance” must be distinguished.

## T3(d). When the stationary density is pure — STATUS: PROVED

The range of $S_\Omega$ is the span of all $C^m\operatorname{ran}\Omega$, since it is a sum of positive matrices. Thus $\rho_\infty$ is pure iff $\Omega=|v\rangle\langle v|$ and $Cv=av$ for some $|a|<1$, allowing $a=0$. Every other rebound gives a mixed stationary density, including pure rebounds whose rays are not invariant.

## T3(e). Secular equation and persistence — STATUS: PROVED

The matrix determinant lemma on the $N^2$-dimensional operator space gives

$$
\det(I-u\mathcal E_\Omega)
=\det(I-u\mathcal E_0)\,[1-\widehat m_\Omega(u)],\qquad
\widehat m_\Omega(u)=u\ell((I-u\mathcal E_0)^{-1}\Omega).     \tag{3.2}
$$

This is a rational identity with the indicated cancellations, initially a convergent series near zero. For simple modes, $X_{ab}=|k_a\rangle\langle k_b|$ has unperturbed eigenvalue $\nu_{ab}=z_a\bar z_b$, and $\ell(X_{ab})=1$. If a product eigenvalue $\nu$ is simple on operator space, with dual left eigenfunctional $L_{ab}(X_{ab})=1$, it persists iff

$$
\ell(X_{ab})L_{ab}(\Omega)=0.                              \tag{3.3}
$$

Proof: in $\det(t-\mathcal E_0)[1-\ell((t-\mathcal E_0)^{-1}\Omega)]$, evaluate at a simple $\nu$ using its resolvent residue $X_{ab}L_{ab}$. The original eigenoperator itself persists iff $\ell(X_{ab})=0$, which never holds here. At a semisimple collision of multiplicity $h$, let $\Pi_\nu$ be its spectral projection. If $\ell(\Pi_\nu\Omega)\ne0$, the multiplicity drops to $h-1$; if it vanishes, the old factor of order $h$ remains and can increase if the regular secular factor also vanishes. Jordan collisions require the full Laurent expansion of (3.2), not a coordinate-zero rule. This is exactly the limitation in `prop:rebound-persistence-secular`, `report/sections/04h_rebound_state.tex:143`.

Explicitly, under H-SIMPLE, if $\Omega=\sum_{a,b}A_{ab}|k_a\rangle\langle k_b|$ with $A\geq0$ and $\operatorname{Tr}(AG)=1$, then $\widehat m_\Omega(u)=u\sum_{a,b}A_{ab}/(1-u z_a\bar z_b)$. The coefficients are biorthogonal expansion coefficients, not ordinary matrix elements in the nonorthogonal mode list.

# 4. T4: modal rebounds and the common-radius test

## T4(a–b). Modal formula and equivalence — STATUS: PROVED-CONDITIONAL (H-SIMPLE for the stated modal family)

For $\Omega=\sum_i p_i|e_i\rangle\langle e_i|$, with normalised distinct eigenvectors,

$$
\mu_\Omega=\sum_i\frac{p_i}{1-|z_i|^2},\qquad
\rho_\infty=\frac1{\mu_\Omega}\sum_i
\frac{p_i}{1-|z_i|^2}|e_i\rangle\langle e_i|.                \tag{4.1}
$$

This follows by summing $C^m\Omega C^{*m}=\sum_i p_i|z_i|^{2m}|e_i\rangle\langle e_i|$. The rank-one projectors of linearly independent eigenvectors are linearly independent: apply their biorthogonal vectors on both sides. Consequently (4.1) equals $\Omega$ for every probability vector on a family iff all $|z_i|$ coincide. Necessity already follows by putting positive weights on any two modes. A singleton gives no test. For the empty family the assertion is vacuous and determines no radius.

If the common radius is $r$, then $\mu_\Omega=(1-r^2)^{-1}$, independent of the weights. Substitution of the additional arithmetic value $r=q^{-1/4}$ yields $(1-q^{-1/2})^{-1}$. In the continuous model amplitude rate $1/4$ gives survival rate $1/2$ and mean $2$; these are different time conventions, not equal numerical means. See `prop:mode-diagonal-rebound-rh`, `report/sections/04h_rebound_state.tex:160`.

## T4(c). The density spectrum — STATUS: PROVED

Let $O_{ij}=\langle e_i,e_j\rangle$ and $w_i=p_i/((1-|z_i|^2)\mu_\Omega)$. The nonzero spectrum of $\rho_\infty$ is that of
$\operatorname{diag}(\sqrt w)O\operatorname{diag}(\sqrt w)$, equivalently $O^{1/2}\operatorname{diag}(w)O^{1/2}$. This is the identity of nonzero spectra of $AA^*$ and $A^*A$. It is generally not the weight list. Formula (1.4) gives nonzero overlaps for every pair of distinct modes. This is the same Gram-spectrum issue explicitly recorded at `report/sections/04h_rebound_state.tex:171` in that proposition.

# 5. T5: admissibility, flags, and the Schur form

## T5(a). Inverting stationarity — STATUS: PROVED

A density $\sigma$ is stationary for some rebound iff

$$
Q_\sigma=\sigma-C\sigma C^*\geq0.
$$

In that event $\operatorname{Tr}Q_\sigma=\ell(\sigma)>0$ and the unique rebound is

$$
\Omega=Q_\sigma/\operatorname{Tr}Q_\sigma.                   \tag{5.1}
$$

Necessity and sufficiency follow from the stationarity equation. If the positive loss had trace zero, it would vanish, giving $\sigma=C^m\sigma C^{*m}\to0$, a contradiction. This is `thm:rebound-admissibility`, `report/sections/04h_rebound_state.tex:180`, with a difference replacing a derivative.

## T5(b). Every finite density spectrum — STATUS: PROVED

For a $C$-invariant subspace $V$ with orthogonal projection $P$, $CPC^*$ is supported on $V$, and $CPC^*\leq P$: restrict to $V$, where $C|_V$ is a contraction. Thus $Q_P=P-CPC^*\geq0$. A full invariant flag exists for every complex finite matrix by Schur triangularisation; it does not require a simple spectrum or a complete eigenbasis. For a flag $V_1\subset\cdots\subset V_N$, $\dim V_k=k$, and numbers $p_1\geq\cdots\geq p_N\geq0$, $\sum p_i=1$, put $p_{N+1}=0$. Then

$$
\sigma=\sum_{k=1}^N(p_k-p_{k+1})P_k,\qquad
Q_\sigma=\sum_{k=1}^N(p_k-p_{k+1})(P_k-CP_kC^*)\geq0.
$$

In an orthonormal flag basis $\sigma$ has exactly the prescribed eigenvalues $p_i$, and (5.1) supplies its rebound. **No graph or arithmetic is used.** Even the rank-one defect is unnecessary: with an arbitrary stable contraction, use total loss $\operatorname{Tr}((I-C^*C)\rho)$ and a common rebound density. This is the discrete form of `thm:flag-spectrum-attainable`, `report/sections/04h_rebound_state.tex:195`.

## T5(c). Coordinates in the resonance basis — STATUS: PROVED-CONDITIONAL (H-SIMPLE)

Write $\sigma=VAV^*$ with $V=(k_1,\ldots,k_N)$ and $G=V^*V$ from (1.4). Then

$$
\sigma\geq0\iff A\geq0,\quad \operatorname{Tr}\sigma=\operatorname{Tr}(AG),\quad
Q_\sigma\geq0\iff\big((1-z_i\bar z_j)A_{ij}\big)_{ij}\geq0. \tag{5.2}
$$

These are coefficient matrices in the expansion into $|k_i\rangle\langle k_j|$, not matrix elements $\langle k_i,\sigma k_j\rangle$, which equal $(GAG)_{ij}$. Moreover $\operatorname{Tr}Q_\sigma=\mathbf1^*A\mathbf1$, because $G_{ji}(1-z_i\bar z_j)=1$. Equations (5.2) follow by the invertible congruence $V$; the Schur factor itself need not be positive. At repeated roots the safe formula is $A-JAJ^*\geq0$ in a Jordan basis, with its corresponding Gram matrix.

# 6. T6: odd modes and the proposed graph vacuum

## T6(a). Protected odd operators — STATUS: PROVED

On $\widetilde K=\mathbb C\mathrm{vac}\oplus K$, set $\widetilde C=1\oplus C$, $\widetilde j=0\oplus j$, and for any density $\widetilde\Omega$ define

$$
\widetilde{\mathcal E}(X)=\widetilde C X\widetilde C^*
+\langle\widetilde j,X\widetilde j\rangle\widetilde\Omega.
$$

The same Kraus proof makes it CPTP. The exit functional vanishes on the odd off-diagonal blocks. Hence

$$
\widetilde{\mathcal E}(|k_i\rangle\langle\mathrm{vac}|)
=z_i|k_i\rangle\langle\mathrm{vac}|,
$$

and the adjoint operator has eigenvalue $\bar z_i$. Repeated roots give the corresponding chains. For nonzero $K$ the map preserves parity iff $\widetilde\Omega$ is even; odd outputs from even inputs are otherwise possible. This is `prop:odd-modes-protected`, `report/sections/04h_rebound_state.tex:118`.

## T6(b). The bound state is not a stationary wave vacuum — STATUS: CORRECTED

An eigenfunction $Tf=\lambda f$ gives wave eigen-data $(f,t^{-1}f)$ with $t+t^{-1}=\lambda$. For a visible bound state these time eigenvalues are $\beta$ and $\beta^{-1}$, **not $1$**. Their individual energy is zero, and their joint two-dimensional energy form is indefinite. Thus the constant function of the pure quotient is stationary for an appropriately normalised adjacency Markov operator, but not for the wave operator $W$ in this problem. Its pure-cusp time multipliers are $\pm q^{-1/2}$ and $\pm q^{1/2}$.

There is no positive definite $W$-invariant inner product on that block: an eigenvalue of modulus different from one rules it out. Modifying an indefinite energy may be useful in a different scattering construction, but it does not by itself supply a Hilbert-space CPTP completion. One can choose a normalised bound eigenfunction as the *label* for an even line and decree $\widetilde C\mathrm{vac}=\mathrm{vac}$; that changes its dynamics and remains an added prescription. Keeping only its decaying wave branch instead gives it a defect, but then an odd coherence has eigenvalue $z_i\bar\beta$, not $z_i$, before any further modification.

With the $1\oplus C$ construction the vacuum is always stationary and never leaks. If $\widetilde\Omega$ is entirely in $K$, the stationary densities form the segment between the vacuum and $0\oplus\rho_\infty$; stability kills stationary odd coherences. If $\widetilde\Omega$ has positive vacuum weight, any stationary density must have zero flux from $K$, and stability forces it to be the vacuum. Thus a unique mixed stationary density on the whole graded space needs an exit from the even line, together with new dynamics compatible with the desired odd eigenvalues. The energy indefiniteness supplies neither. Compare `prop:graded-stationary-segment`, `report/sections/04h_rebound_state.tex:129`.

# 7. T7: RAM, resonance RH, and explicit small cores

Under H-PERRON define **RAM(Y)** as in the question: all $\ell^2$ eigenvalues except the positive Perron eigenvalue, if present, and its genuine bipartite twin lie in $[-2,2]$. For signed arbitrary matrices, a distinguished exempt set must instead be specified; “Perron” is otherwise undefined. Define **RH(Y)** to mean that all retained resonance roots have one modulus $r$. For $N=0$ this is vacuous and supplies no $r$; for nonzero resonances $0<r<1$. This RH terminology is local to the question. It is not the notebook's graded *divisor* definition, which also specifies an even/odd cancellation and a functional equation: `def:graded-rh-fe-ramanujan`, `report/sections/02h_definitions_graded_ramanujan.tex:60`.

## T7(a). Independence — STATUS: PROVED

For a one-vertex core $T_X=[a]$,

$$
p=z^2-az+1-c^2,\qquad \widetilde p=1-az+(1-c^2)z^2.         \tag{7.1}
$$

Take $a=29/20$, $c^2=1/2$. The two roots are

$$
z_\pm=(29\pm\sqrt{41})/40
=0.8850781059\ldots,\ 0.5649218941\ldots.
$$

Both are in the disk, with unequal moduli. There are no bound states and no cusp forms. This connected nonnegative graph has RAM and fails RH.

For the reverse direction take the connected, nonnegative two-vertex core

$$
T_X=\begin{pmatrix}2/5&\sqrt{51}/5\\\sqrt{51}/5&1/10\end{pmatrix},
\quad v_0=1,\quad c^2=5/2.
$$

Direct expansion gives

$$
p(z)=(z^2+1/2)(z-2)(z+3/2).
$$

It is cyclic at $v_0$ and has no threshold cancellation. Its only resonances are $\pm i/\sqrt2$, so RH holds nonvacuously. Its visible bound parameters are $1/2$ and $-2/3$, giving eigenvalues $5/2$ and $-13/6$. The former is Perron. The latter is outside the band and is not an exempt twin: the graph has positive loops and is not bipartite. RAM fails. Thus neither implication holds, even for connected nonnegative weighted cores and nonempty resonance sets.

## T7(b). What determines the radius — STATUS: CORRECTED

The product of **all** $2n$ roots of the monic $p$ is exactly $1-c^2$. It is not in general the product of the retained resonances. Factoring out cusp, exterior and threshold roots gives

$$
\prod_i z_i=(1-c^2)\frac{\prod_\beta\beta}{\prod_{\epsilon\in E_{\rm th}}\epsilon}.
$$

Consequently, if $N>0$, H-INVERT and RH hold,

$$
r^N=|1-c^2|\prod_\beta|\beta|.                             \tag{7.2}
$$

This determines a radius from the actual graph parameters, not a universal arithmetic radius. Already (7.1) with $a=0$, $0<c^2<1$ has $r=\sqrt{1-c^2}$, which can be any number in $(0,1)$. If $c^2=1$, zero roots occur; RH then requires that every resonance be zero or, if zero modes are excluded by a different definition, requires recomputing the retained polynomial. The reciprocity $R(z)R(1/z)=1$ exchanges zeros and poles. It does not reflect the resonance set into itself about a smaller circle. Nothing generic forces $q^{-1/4}$.

## T7(c). Checkable criteria — STATUS: PROVED

Let $Q(z)=\prod_i(z-z_i)$ be the monic resonance polynomial, obtained by the explicit cancellations and root separation in C2. If $N>0$ and $Q(0)\ne0$, a necessary radius is $r=|Q(0)|^{1/N}$. Put $F(w)=r^{-N}Q(rw)$. A necessary condition is

$$
F(w)=F(0)w^N\overline{F(1/\bar w)},\qquad |F(0)|=1.         \tag{7.3}
$$

This follows by pairing the roots on the unit circle and comparing leading coefficients. It is not sufficient: $(w-2)(w-1/2)$ is self-reciprocal and fails the unit-circle test. Scaled versions with roots $0.8,0.2$ demonstrate the same failure with both original roots in the disk.

An exact necessary and sufficient check, including multiple roots, is (7.3) plus real-rootedness of the Cayley transform

$$
H(x)=\kappa(x+i)^N F\!\left(\frac{x-i}{x+i}\right),         \tag{7.4}
$$

where a constant phase $\kappa$ makes the coefficients real. Such a phase exists by (7.3). Require every root of this real polynomial to be real; a degree drop counts roots at infinity, corresponding exactly to $w=1$. The Cayley map is a bijection from the extended real line to the unit circle, proving the criterion. Polynomial gcds and real-root tests make this checkable from $(T_X,v_0,c)$; it is a verification criterion, not a structural reason for RH.

Under H-SIMPLE there is another necessary and sufficient check: for the companion matrix $M_Q$, find a positive definite Hermitian $H$ satisfying $M_Q^*HM_Q=r^2H$. Necessity follows by diagonalising $M_Q$ and pulling back the Euclidean norm; sufficiency follows by conjugating $M_Q/r$ to a unitary. Without H-SIMPLE a companion matrix with repeated roots has Jordan blocks and this last criterion is too strong.

## T7(d). Smallest cores — STATUS: PROVED

One vertex already suffices for both questions. In (7.1), choose $0<c^2<1$ and $a^2<4(1-c^2)$. The two roots are a nonreal conjugate pair of modulus $\sqrt{1-c^2}<1$, so both are resonances and RH holds. For instance $a=0,c^2=1/2$ gives $\pm i/\sqrt2$. A smaller nonempty core with a distinguished vertex does not exist. If the junction were additionally constrained to the pure-cusp value $c^2=q+1$, this example would be disallowed; that constraint is not H-SETUP for a general core.

# 8. T8: what the arithmetic round must supply

**T8 — STATUS: OPEN (H-ARITH); the following generic scope is proved above.** Finite-core self-adjoint scattering, Schur self-energies, rational reflection, the separation of invisible modes and thresholds, energy conservation and the positive continuous wave space are generic; with $h$ rays the amplitudes and scattering function are matrix-valued and the radiation multiplicity is $h$. The corrected orthogonalisation $D_+=\mathcal O_+\cap\mathcal O_-^\perp$ also has a matrix Hardy-space formulation: analytic cancellation conditions replace the scalar factor $B_{\rm bd}$, and the resulting minimal inner model has defect rank at most $h$; determinant cancellation alone does not specify all matrix pole/zero directions. T3–T6 are generic contraction facts: for several exits they retain the scalar renewal formulas only when every exit reinserts the same density, with loss $\operatorname{Tr}((I-C^*C)\rho)$; different exit-dependent rebounds require a matrix renewal equation, and the scalar uniqueness/gcd criterion cannot simply be copied. The multi-exit Gram numerator is the inner product of exit-amplitude vectors, rather than the constant $1$ in (1.4). T7 supplies definitions, independence and tests, not a generic RH conclusion. **H-ARITH**, to be verified from sources in the next round, must identify the actual $h\times h$ scattering matrix for $\Gamma_0(N)$, including the cusp junctions, time/height normalisation, threshold and bound-state factors and cancellations, with specified ratios of Dirichlet $L$-functions over $\mathbb F_q[T]$; prove that its retained resonances are the relevant $L$-zeros at $|z|=q^{-1/4}$, with multiplicities and no extra retained modes; identify the diamond/Galois action and its level-$N$ grading on the model; and derive the logarithmic-derivative comb over monic irreducibles. The $L$-function identification is a hypothesis here, not a conclusion. Arithmetic must also justify any chosen rebound or even-sector dynamics if those are claimed to be canonical.

# Correction ledger

| No. | Draft issue | Correct statement |
|---:|---|---|
| 1 | Geometric weights at the first vertex were implicit. | $m_0=1$, $m_n=(q+1)q^{-n}$; indeed $c^2=q+1$. |
| 2 | The upward height and $q^{-sh}$ were combined with the wrong quotient recurrence. | For upward index $n$, use $q^{sn},q^{(1-s)n}$; the stated tree Busemann convention uses $h=-n$. |
| 3 | Determinant reflection formula had no minus sign. | $R=-\det(\lambda-T_X-c^2z^{-1}P_0)/\det(\lambda-T_X-c^2zP_0)=-p/\widetilde p$. |
| 4 | Degree implicitly depended only on $n$. | Reduced rational degree is $2d-\tau$. |
| 5 | All outside-band eigenvalues were claimed to be poles. | Only modes with nonzero ray component are visible; outside-band cusp forms are invisible too. |
| 6 | Common factors were exactly cusp forms. | Also cancel simple cyclic threshold factors at $z=\pm1$. |
| 7 | Resonance count omitted thresholds and invisible dimensions. | $N=2n-2\sum m_c-b-\tau$. |
| 8 | Every disk zero was assigned finite $\lambda$. | $z=0$ is a delay mode; exclude it for a finite-energy-parameter resonance count. |
| 9 | Pure-cusp poles/zeros were described without periods. | The $s$-divisor repeats with period $\pi i/\log q$ in the pure case. |
| 10 | $R$, $\phi$ and an inner characteristic function were interchangeable. | $\phi=1/R$; the contraction uses the pole-removed $\Theta=\eta RB_{\rm bd}$. |
| 11 | Entire $\xi$ and the meromorphic completion were conflated. | Their modular ratios differ by $(s-1)/s$, affecting the pole at $1$. |
| 12 | Both radiation spaces were called $W$-invariant unilateral shifts. | Outgoing is forward invariant; incoming is backward invariant. |
| 13 | Removing bound states preserved the local orthogonal radiation pair. | False: the pure $q=2$ cusp gives projected cross energy $3/32$. |
| 14 | The geometric local compression was asserted without orthogonalisation. | Replace outgoing data by $\mathcal O_+\cap\mathcal O_-^\perp$; this cancels exactly the bound-state poles and gives $\Theta=\eta RB_{\rm bd}$. |
| 15 | The defect vector was an unnormalised site datum. | It is the compression of the first translation coordinate; for $C=Z^*$ it is $P_K1$. |
| 16 | An eigenbasis was used at arbitrary multiplicity. | H-SIMPLE for that basis; derivative kernels/Jordan chains otherwise. |
| 17 | Every general core determinant was an Ihara determinant. | H-REG gives the Bass interpretation, with its separate edge factor. |
| 18 | Zero-centred $\log p$ supplied positive root power sums. | It supplies inverse powers; positive powers come from $\log\widetilde p$, then (2.4). |
| 19 | Walk expansions were unqualified counts. | They are signed weighted sums with ordered insertions and convergence restrictions. |
| 20 | Both $c^2z$ and $c^2/z$ literally summed returning ray walks. | Only the physical branch has the convergent Catalan expansion; the other is its continuation. |
| 21 | Uniqueness of the renewal stationary state required aperiodicity. | Uniqueness is unconditional under stability; attraction requires aperiodicity. |
| 22 | Nonreal modal overlap might ensure aperiodicity. | The $\pm ir$ example is periodic; containing an eigenvector in the rebound range does suffice. |
| 23 | Mixedness criterion was incomplete. | The stationary density is pure exactly for a pure rebound on an invariant eigenvector ray. |
| 24 | Persistence could be stated per pair at collisions. | The simple-product criterion needs a simple operator-space eigenvalue; use residues at collisions. |
| 25 | Modal weights were treated as density eigenvalues. | The spectrum is the associated Gram spectrum. |
| 26 | Flag attainability suggested graph/arithmetic content. | It holds for every finite stable contraction, with arbitrary defect rank. |
| 27 | Bound wave data were called stationary. | Their time multipliers are $\beta,\beta^{-1}$; the energy block is indefinite. |
| 28 | A graph bound state automatically supplied a suitable vacuum. | Declaring it stationary changes the dynamics; a unique mixed graded stationary state still needs an even exit. |
| 29 | Perron terminology applied to arbitrary real symmetric cores. | Use H-PERRON or explicitly choose the exempt set. |
| 30 | RAM might constrain the resonance radii. | The connected one- and two-vertex examples prove independence. |
| 31 | The root product might universally force the critical radius. | Use the retained product (7.2); no universal $q^{-1/4}$ follows. |
| 32 | Scaled self-reciprocity might suffice for RH. | It is necessary; add the Cayley real-root test or an equivalent circle test. |
| 33 | All scalar statements had an automatic multi-cusp extension. | Rank, matrix scattering and reset rules matter; distinct rebounds do not obey one scalar renewal law. |
| 34 | Arithmetic identifications could be inferred from the toy. | All four requested identifications are explicitly H-ARITH. |

# Numerical checks

Python 3 with NumPy and SymPy was run in memory; no auxiliary files were written. The following consolidates the computations run, including the exploratory small cores. Values use $c^2$ so there is no ambiguity about square roots of couplings.

| $a$ | $c^2$ | Roots of $p$ for the one-vertex core |
|---:|---:|---|
| $0$ | $3$ | $\pm1.414213562373$; poles $\pm0.707106781187$; no resonances |
| $0$ | $1/2$ | $\pm0.707106781187i$ |
| $1/4$ | $1/2$ | $0.125\pm0.695970545354i$ |
| $3/2$ | $1/2$ | $0.5,1$; common factor $z-1$ |
| $0$ | $1$ | $0,0$; $R=-z^2$ |
| $1$ | $1$ | $0,1$; common factor $z-1$ |
| $7/5$ | $1/2$ | $0.7\pm0.1i$ |
| $29/20$ | $1/2$ | $0.564921894064,0.885078105936$ |

For $T_X=\left(\begin{smallmatrix}3&1/5\\1/5&-3\end{smallmatrix}\right)$, $c^2=1/2$, the roots were $-2.626081522436,-0.380516983804,0.176821704555,2.829776801685$. For $T_X=\left(\begin{smallmatrix}0&t\\t&0\end{smallmatrix}\right)$, $c^2=1/2$, $t=1$ gave $\pm0.478072578792\pm0.691775534833i$, and $t=3$ gave $\pm2.726303351732,\pm0.259364674418$. These agree with the corresponding quartics $z^4-377z^2/50-3z/2+1/2$, $z^4+z^2/2+1/2$, and $z^4-15z^2/2+1/2$.

The random four-vertex core used seed `20260920`, $c^2=3/5$, and

$$
T_X=\begin{pmatrix}
0&-1/5&1/5&-3/5\\-1/5&0&1&0\\1/5&1&4/5&1/10\\-3/5&0&1/10&-3/5
\end{pmatrix}.
$$

It gave

$$
p=z^8-z^7/5+147z^6/100-88z^5/125+2047z^4/1250-28z^3/125+291z^2/250-2z/25+2/5.
$$

The four conjugate resonance pairs were $-0.49793845\pm0.72183735i$, $-0.30781707\pm0.94871953i$, $0.16538760\pm0.70416216i$, $0.74036792\pm0.67173619i$, with radii $0.87692181,0.99740668,0.72332386,0.99968703$. No denominator root was inside the disk. Across 400 unit-circle points the maximum modulus and functional-equation residuals were $1.94\cdot10^{-14}$ and $3.58\cdot10^{-14}$. The Gram minimum eigenvalue was $0.963914019844$ and $\|G-D^*GD-\mathbf1\mathbf1^*\|_{\max}=9.36\cdot10^{-14}$. With weights proportional to $1,\ldots,8$ in SymPy's returned root order, $\mu=704.318523610$.

For the independent RAM/RH example, symbolic factorisation returned $(z-2)(2z+3)(2z^2+1)/4$ exactly. For the periodic example at $r=0.7$, the eigenvalues were $\pm0.7i$ and the first six holding probabilities were $(0,0.7599,0,0.18245199,0,0.043806722799)$. At $z=0.37+0.23i$, the pure-cusp identity (0.6) had residuals $7.86\cdot10^{-17},2.01\cdot10^{-16},5.73\cdot10^{-17}$ for $q=2,3,5$ respectively. A 200-site evaluation of the explicitly known bound-state projections gave the cross energy $0.09374999999999989$, versus $3/32$ exactly.

The Abel-regularised radiation ratio in (1.2a) simplified exactly to $-wR$. For the same $r=0.7$ contraction with the nonmodal rebound $\Omega=vv^*$, $v=(1,i)/\sqrt2$, solving the four-dimensional renewal equation gave $\mu=2.131925253323$, stationarity residual $2.01\cdot10^{-16}$, and zero numerical determinant-identity residual at $u=0.23+0.19i$.

Reproduction code for these checks (the earlier short invocations are consolidated here):

```python
# Author: codex:gpt-6-astra
import numpy as np
import sympy as s
z = s.symbols('z')
R = s.Rational

def poly(A, c2):
    n = A.rows
    P = s.zeros(n); P[0, 0] = 1
    return s.Poly((s.eye(n)*(1+z*z)-z*A-c2*P).det(), z)

for a, c2 in [(0,3),(0,R(1,2)),(R(1,4),R(1,2)),
              (R(3,2),R(1,2)),(0,1),(1,1),
              (R(7,5),R(1,2)),(R(29,20),R(1,2))]:
    p = z*z-a*z+1-c2
    t = 1-a*z+(1-c2)*z*z
    print(a, c2, s.nroots(p), s.gcd(p,t))
    if s.degree(t,z)>0: print('denominator roots', s.nroots(t))
for A in [s.Matrix([[3,R(1,5)],[R(1,5),-3]]),
          s.Matrix([[0,1],[1,0]]), s.Matrix([[0,3],[3,0]])]:
    p = poly(A,R(1,2)); print(p.as_expr(), s.nroots(p))

rng = np.random.default_rng(20260920)
M = rng.integers(-5,6,(4,4))
A = s.Matrix((M+M.T).tolist())/10
p = poly(A,R(3,5))
t = s.Poly(s.expand(z**8*p.as_expr().subs(z,1/z)),z)
roots = np.array([complex(v) for v in s.nroots(p,maxsteps=200)])
poles = np.array([complex(v) for v in s.nroots(t,maxsteps=200)])
print(A, p.as_expr(), roots, abs(roots), poles[abs(poles)<1])
f = s.lambdify(z,-p.as_expr()/t.as_expr(),'numpy')
zz = np.exp(1j*np.linspace(.04,6.24,400))
print(max(abs(abs(f(zz))-1)), max(abs(f(zz)*f(1/zz)-1)))
zr = roots[abs(roots)<1]
G = 1/(1-np.conj(zr[:,None])*zr[None,:]); D = np.diag(zr)
print(np.linalg.eigvalsh(G)[0], np.max(abs(G-D.conj().T@G@D-1)))
weights = np.arange(1,len(zr)+1,dtype=float); weights /= sum(weights)
print(sum(weights/(1-abs(zr)**2)))

A = s.Matrix([[R(2,5),s.sqrt(51)/5],[s.sqrt(51)/5,R(1,10)]])
print(s.factor(poly(A,R(5,2)).as_expr()))
r = .7; C = np.array([[0,1],[-r*r,0.]])
Om = np.diag([0.,1.]); j = np.array([np.sqrt(1-r**4),0.])
print(np.linalg.eigvals(C),
      [j@np.linalg.matrix_power(C,m)@Om@
       np.linalg.matrix_power(C.T,m)@j for m in range(6)])
for q in [2,3,5]:
    x = .37+.23j; ss = .5+np.log(x)/np.log(q)
    zet = lambda t: 1/((1-q**(-t))*(1-q**(1-t)))
    rr = (x*x-q)/(q*x*x-1)
    print(q, [-q**-.5,q**-.5], abs(1/rr-q*zet(2*ss-1)/zet(2*ss)))

L = 200; q = 2; c = np.sqrt(q+1)
T = np.diag(np.ones(L-1),1)+np.diag(np.ones(L-1),-1)
T[0,1] = T[1,0] = c
V = []
for beta in [q**-.5,-q**-.5]:
    v = np.r_[1.,c*beta**np.arange(1,L)]
    V.append(v/np.linalg.norm(v))
P = np.eye(L)-np.array(V).T@np.array(V)
u,v,x,y = [np.eye(L)[:,k] for k in [2,1,2,3]]
energy = lambda u,v,x,y: u@x+v@y-(u@T@y+v@T@x)/2
print(energy(P@u,P@v,P@x,P@y))

w,t,rr = s.symbols('w t R', nonzero=True)
a = (w*w-1)/(1-t*w*w)
b = (1-w**-2)*w**-1/(rr*(1-t*w**-2))
print(s.factor(s.limit(a/b,t,1)))
r = .7; C = np.array([[0,1],[-r*r,0.]],complex)
j = np.array([np.sqrt(1-r**4),0.]); v = np.array([1,1j])/np.sqrt(2)
Om = np.outer(v,v.conj()); J = np.outer(j,j)
vec = lambda X: X.reshape(-1,order='F')
E0 = np.kron(C.conj(),C); E = E0+np.outer(vec(Om),vec(J).conj())
S = np.linalg.solve(np.eye(4)-E0,vec(Om)).reshape((2,2),order='F')
rho = S/np.trace(S); u = .23+.19j
mh = u*vec(J).conj()@np.linalg.solve(np.eye(4)-u*E0,vec(Om))
print(np.trace(S).real, np.linalg.norm(E@vec(rho)-vec(rho)))
print(abs(np.linalg.det(np.eye(4)-u*E)-
          np.linalg.det(np.eye(4)-u*E0)*(1-mh)))
```

# What a refuter should attack first

- The $3/32$ obstruction for projected local waves, and the phase, completeness and intersection arguments in (1.2a–b) repairing it.
- Threshold cancellation and zero-delay multiplicities in the count $N=2d-b-\tau$.
- The time/height orientation, zero-delay modes and the claimed characteristic-function convention.
- H-ARITH: the precise scattering normalisation and retained divisor must be proved before importing any $L$-zero radius.
