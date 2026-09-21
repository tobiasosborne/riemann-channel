# Rebound inside the Riemann model space

Author: `codex:gpt-6-astra`

The reset construction works. Several proposed spectral conclusions do not: the modes are nonorthogonal, an arbitrary rebound need not preserve parity, and the added vacuum prevents uniqueness of a mixed stationary state on the graded space. There is nevertheless an explicit construction of every finite stationary density spectrum, without RH, using invariant flags rather than modal mixture weights.

## Hypotheses and scope

The following labels distinguish inputs from conclusions. A hypothesis is used only where indicated; listing H-RH does **not** assume RH throughout.

- **H-MODEL:** $\Theta$ is a nonconstant scalar inner function on $\mathbb C_+$ with the stated nonempty zero multiset $w_\rho=\gamma/2+i(1-\sigma)/2$, $0<\sigma<1$. For the arithmetic interpretation it is the quotient $\xi(1+2i\tau)/\xi(1-2i\tau)$ in the brief. Innerness and identification of its divisor are inputs, not proved here. Additional inner factors are not excluded.
- **H-SYM:** The arithmetic zero multiset is invariant, with multiplicity, under $\rho\mapsto1-\bar\rho$ and complex conjugation. In particular $(x,y)\mapsto(x,1/2-y)$ preserves the model zero multiset. This familiar zeta symmetry is declared explicitly rather than silently imported.
- **H-INFINITE:** There are infinitely many distinct model zeros. Used for arbitrary finite ranks and the infinite Gibbs-spectrum construction.
- **H-ZCOUNT:** The number $N_+(T)$ of arithmetic zeros with $0<\gamma\le T$, counted with multiplicity, satisfies $N_+(T)/T\to\infty$. This weak consequence of the Riemann--von Mangoldt counting theorem is an additional arithmetic input, not proved here. It implies H-INFINITE and is used, with H-SYM, to construct an infinite-mean rebound.
- **H-FINITE:** A specified calculation is on $V=\operatorname{span}\{k_{w_1},\ldots,k_{w_N}\}$ for distinct selected zeros, and the rebound is supported on $V$. A claim about the *full finite spectrum* means the restriction to $\mathcal T(V)$, not the generator on all of $\mathcal T(K)$.
- **H-SIMPLE:** All zeros under discussion are simple. Needed only to replace generalized chains by one ordinary eigenvector per zero counted with multiplicity. Finite calculations with distinct selected kernels do not require global simplicity.
- **H-RH:** Every arithmetic zero has $\sigma=1/2$, equivalently every model zero has $y:=\operatorname{Im}w=1/4$.
- **H-MEAN:** The specified rebound has finite mean $\mu_\Omega$. This is a checkable condition, proved automatically under H-FINITE.
- **H-UES:** There exist $M,\omega>0$ with $\|C_t\|\le M e^{-\omega t}$. This is only a comparison hypothesis; it is never assumed for the Riemann model.

The Paley--Wiener theorem, the scalar Blackwell renewal theorem, and elementary semigroup facts are standard (no local source). The SHW construction is invoked as its stated theorem, with its assumptions verified below; there is no additional unverified H-SHW. All operator states below are trace-class Schrödinger states. Their dual channels act on bounded operators. A density spectrum means the nonzero eigenvalues of the density; `def:bond-entanglement` actually calls the corresponding **negative logarithms** the entanglement spectrum.

## 0. Conventions and the exit channel

Use inner products antilinear in the first variable and Hardy boundary norm $\|f\|^2=\int_{\mathbb R}|f(\tau)|^2d\tau$. Fix the Paley--Wiener unitary by

$$
f(\tau)=\frac1{\sqrt{2\pi}}\int_0^\infty e^{i\tau x}(Ff)(x)\,dx.
$$

Then multiplication $M_t f=e^{it\tau}f$, $t\ge0$, becomes the right shift with zero fill, and $M_t^*$ becomes $B_tg(x)=g(x+t)$. Put $K=H^2\ominus\Theta H^2$, $\mathcal M=FK$, $Z_t=P_KM_t|_K$, and $C_t=Z_t^*=M_t^*|_K$. The last equality holds because $\Theta H^2$ is $M_t$-invariant. Thus $\mathcal M$ is $B_t$-invariant. We identify $K$ and $\mathcal M$ when writing derivatives and boundary values, and write $B=K_{\rm gen}$, $C_t=e^{tB}$. The notebook's expression $\rho\mapsto Z_t^*\rho Z_t=C_t\rho C_t^*$, here acting on trace class, is the no-event semigroup of `1707.02266:TORUN.tex:172–173`; its dual on bounded observables is $X\mapsto C_t^*XC_t$.

The scattering convention is $S(\tau)=\xi(1-2i\tau)/\xi(1+2i\tau)$, inner in the lower half plane, and $\Theta(\tau)=S(-\tau)=\xi(1+2i\tau)/\xi(1-2i\tau)$, inner in the upper half plane. Algebraically the numerator of $S$ vanishes at $\tau=-\gamma/2-i(1-\sigma)/2$; that of $\Theta$ vanishes at $w_\rho=\gamma/2+i(1-\sigma)/2$. The respective poles are reflected into the opposite half plane under H-MODEL. The lower-half-plane formula in `report/sections/04_riemann_channel.tex:71–75` has an adjoint/sign error: for $\lambda=x-iy$, $|e^{-it\bar\lambda}|=e^{yt}$. In the upper-half-plane convention used here the decaying formula is $C_tk_w=e^{-it\bar w}k_w$. If keeping that shard's lower-half-plane compression, its correct kernel formula is $Z_tk_\lambda=e^{it\bar\lambda}k_\lambda$, with $Z_t$, not $Z_t^*$. See C-SIGN in the ledger.

### C1. Kernels, eigenvalues, and Fourier sign

**STATUS: CORRECTED** under H-MODEL. The membership and upper-half-plane eigenvalue assertions are correct. The requested time function $e^{iwx}$ must be replaced by $e^{-i\bar w x}$ with the specified *linear* Fourier unitary.

For $k_w(\tau)=(\tau-\bar w)^{-1}$, Cauchy's formula and a residue calculation give

$$
\langle k_w,f\rangle=2\pi i f(w),\qquad
\langle k_w,k_v\rangle=\frac{2\pi i}{w-\bar v},\qquad
\|k_w\|^2=\frac\pi{\operatorname{Im}w}.
$$

Thus the exactly reproducing vector is $i k_w/(2\pi)$. Orthogonality to every $\Theta h$ is equivalent to $\Theta(w)h(w)=0$ for every $h\in H^2$, hence to $\Theta(w)=0$. Adjointing the evaluation identity for $M_t$ yields

$$
C_tk_w=e^{-it\bar w}k_w,\qquad Bk_w=b_wk_w,
\quad b_w=-i\bar w=-y-ix.
$$

Directly from the fixed transform,

$$
(Fk_w)(x)=-i\sqrt{2\pi}\,e^{-i\bar w x},\qquad x>0.
$$

Backward translation multiplies this function by $e^{-it\bar w}$, checking both signs. Its decay rate is $y=(1-\sigma)/2$; the assertion that **every** zero mode has rate $1/4$ is exactly H-RH. The alternative $e^{iwx}$ has the opposite frequency and cannot be the Fourier image of this same kernel under these conventions.

### C2. Domain and one-dimensional exit

**STATUS: PROVED** under H-MODEL. Precisely,

$$
D(B)=\mathcal M\cap H^1(0,\infty),\qquad Bg=g',\qquad jg=g(0).
$$

There is no zero boundary condition. Indeed the generator of the backward shift on the full half-line has domain $H^1$. Its part on an invariant closed subspace has domain those $g\in\mathcal M\cap H^1$ with $g'\in\mathcal M$; the latter membership follows automatically by taking the $L^2$ limit of the invariant difference quotients. Conversely a derivative limit in $\mathcal M$ is the same limit in $L^2$, proving the domain assertion. This domain is dense by the general generator theorem.

Integration by parts, using the vanishing boundary limit of $H^1\cap L^2$ functions at infinity, proves

$$
-\big(\langle B\psi,\phi\rangle+\langle\psi,B\phi\rangle\big)
=\overline{\psi(0)}\phi(0)=\langle j\psi,j\phi\rangle.
$$

Also $|g(0)|^2\le2\|g\|\|g'\|$, so $j$ is graph-norm continuous. It is nonzero, since $jk_w=-i\sqrt{2\pi}$. Consequently its minimal exit space is exactly $E=\mathbb C$. The notation $-(B+B^*)=j^*j$ denotes this **form identity on $D(B)\times D(B)$**; it does not assert that evaluation is a bounded Hilbert-space covector or that $D(B)\subset D(B^*)$. This is the restriction of SHW's half-sided shift example, `1707.02266:TORUN.tex:442–450`, with the exit definition at `1707.02266:TORUN.tex:203–208`.

### C3. Strong stability and no dark zero mode

**STATUS: PROVED** under H-MODEL. For every $g\in\mathcal M$,

$$
\|C_tg\|^2=\int_t^\infty|g(x)|^2dx\longrightarrow0.
$$

On $D(B)$, $(Jg)(t)=jC_tg=g(t)$, so $J$ extends to the isometric inclusion $\mathcal M\hookrightarrow L^2(\mathbb R_+)$. This also directly proves SHW's equality case in `1707.02266:TORUN.tex:213–215`. The nonzero value $jk_w=-i\sqrt{2\pi}$ is the **time-domain** value at zero, not evaluation of $k_w(\tau)$ at spectral parameter $\tau=0$. Every zero mode couples to the exit. Arbitrary superpositions can have $jg=0$ instantaneously; this is not an invariant dark subspace, since $J$ is an isometry.

### C4. Strong versus uniform stability

**STATUS: PROVED** as the following scope statement. No assertion $\|C_t\|=1$ for all $t$ is proved or used here. C1–C3, conservativity, the domain/resolvent formulas, the stationary-state criterion, odd-mode protection, and the inverse criterion need only the proved strong stability. Convergence in T2 additionally needs H-MEAN. Finite modal spaces have exponential stability by their finite matrix exponential; this is not a bound uniform in the space or its dimension.

H-UES would imply $\mu_\Omega\le M^2/(2\omega)$ for **every** density. Strong stability alone does not imply this; T2 constructs an infinite-mean density under the declared counting input, even if H-RH is added. We prove trace-norm convergence for each initial state, not convergence in the operator norm of the channel maps, and give no uniform exponential mixing rate. Even H-UES for the no-event semigroup is not being used as an unexplained quantitative renewal theorem.

## 1. Definition of the reset generator; T1 (conservativity)

Write $\mathcal T(K)$ for trace class, $T_t^0\rho=C_t\rho C_t^*$, and $A$ for its generator, with its precise Banach-space domain

$$
D(A)=\left\{\rho:\lim_{h\downarrow0}\frac{T_h^0\rho-\rho}{h}
\text{ exists in trace norm}\right\}.
$$

On the core $\mathcal D=\operatorname{span}\{|\psi\rangle\langle\phi|:\psi,\phi\in D(B)\}$,

$$
A(|\psi\rangle\langle\phi|)=|B\psi\rangle\langle\phi|+|\psi\rangle\langle B\phi|,
\quad
\ell(|\psi\rangle\langle\phi|)=j\psi\,\overline{j\phi}.
$$

The exit functional extends to $D(A)$ as $\ell(\rho)=-\operatorname{Tr}(A\rho)$. It is positive on positive elements of this domain and graph-norm continuous. These assertions and the core property also follow from `1707.02266:TORUN.tex:249–262`. Thus $\langle\rho\rangle_j$ means $\ell(\rho)$ on $D(A)$, not a generally defined trace of an unbounded operator against every density.

For any density $\Omega$ on $K$, define the reinsertion $\mathcal R_\Omega(c)=c\Omega$, $c\in\mathcal T(\mathbb C)$. Given an orthonormal basis $(h_\alpha)$ of $K$, let $v_\alpha=\Omega^{1/2}h_\alpha$ and $M_\alpha c=cv_\alpha$. Then

$$
\sum_\alpha|v_\alpha\rangle\langle v_\alpha|=\Omega,
\quad L_\alpha\psi=v_\alpha j\psi,
\quad \sum_\alpha\|L_\alpha\psi\|^2=|j\psi|^2.
$$

This verifies the SHW normalization inequality with equality and realizes exactly the reinsertion/Kraus correspondence at `1707.02266:TORUN.tex:246,253–254`; the domain convention is `1707.02266:TORUN.tex:189–198`. Define $T_t^\Omega$ to be the SHW minimal semigroup for $A+P_\Omega$, $P_\Omega\rho=\ell(\rho)\Omega$, as in `1707.02266:TORUN.tex:317–321`. We will prove its generator has precisely domain $D(A)$, so in this example

$$
\mathcal L_\Omega\rho=A\rho+\ell(\rho)\Omega,\qquad D(\mathcal L_\Omega)=D(A).
$$

For a density $\rho=\sum_a q_a|\psi_a\rangle\langle\psi_a|$, put $g_a=F\psi_a$ and

$$
A_\rho(t)=T_t^0\rho,\quad
m_\rho(t)=\sum_aq_a|g_a(t)|^2,\quad
S_\rho(t)=\operatorname{Tr}A_\rho(t)=\int_t^\infty m_\rho(s)ds.
$$

The sum defines an $L^1$ density independently of the decomposition. In particular $m_\rho=-S_\rho'$ **almost everywhere**, $\int m_\rho=1$, and there is no atom at zero. For general densities $jC_t\psi_a$ is an $L^2$ output defined almost everywhere, not necessarily classical point evaluation. Let $\widehat m_\Omega(z)=\int_0^\infty e^{-zt}m_\Omega(t)dt$ for $\operatorname{Re}z\ge0$.

### T1

**STATUS: PROVED** under H-MODEL, for every density $\Omega$; no finite-mean assumption.

The holding times after the first event are independent with common density $m_\Omega$. The first holding density is $m_\rho$ if the initial state is $\rho$. Their strict positivity and properness imply nonexplosion: choose $\varepsilon>0$ with $\Pr(H\ge\varepsilon)>0$; infinitely many independent holding times exceed $\varepsilon$ almost surely, so their partial sums diverge. The same argument works with infinite mean.

More explicitly, SHW's event expansion (`1707.02266:TORUN.tex:228–234`) is

$$
T_t^\Omega\rho=A_\rho(t)
+\sum_{n\ge1}\big(m_\rho*m_\Omega^{*(n-1)}*A_\Omega\big)(t).
$$

Each term is completely positive and its trace is the probability of exactly $n$ events by $t$. Nonexplosion makes their traces sum to one. The series therefore converges in trace norm for positive inputs; extension by linearity gives a CPTP semigroup. Its strong continuity at zero follows from $A_\rho(t)\to\rho$ and the bound $1-S_\rho(t)\to0$ on the jumped mass. This is the minimal event construction, so proves conservativity of the specified object rather than of some larger extension.

Here is a useful independent domain check. For real $z>0$ let $R_0(z)=(z-A)^{-1}$ and $f_z=\ell R_0(z)$. Integration by parts gives, on densities,

$$
f_z(\rho)=\widehat m_\rho(z)
=\operatorname{Tr}\rho-z\operatorname{Tr}R_0(z)\rho.
$$

Thus $f_z$ is a bounded positive functional of norm at most one, and $q_z=f_z(\Omega)=\widehat m_\Omega(z)<1$. Since $(P_\Omega R_0(z))^n=q_z^{n-1}P_\Omega R_0(z)$, SHW's resolvent series (`1707.02266:TORUN.tex:311–313`) converges in operator norm and yields

$$
R_\Omega(z)\rho=R_0(z)\rho+
\frac{f_z(\rho)}{1-\widehat m_\Omega(z)}R_0(z)\Omega. \tag{1}
$$

Equivalently $R_\Omega=R_0(I-P_\Omega R_0)^{-1}$, with the second factor a bounded bijection. Therefore $\operatorname{ran}R_\Omega=\operatorname{ran}R_0=D(A)$. This also verifies SHW's finite-rank perturbation lemma, `1707.02266:TORUN.tex:346–347`, even when $\Omega$ has infinite Hilbert-space rank.

No extra SHW conservativity condition is needed. We used the specific renewal law to exclude finite-time loss; cancellation of generator traces on a small core would not suffice in general. That distinction is precisely SHW's warning at `1707.02266:TORUN.tex:147` and the mechanism discussed at `1707.02266:TORUN.tex:646–650`.

### The graded definition

On $\widetilde K=\mathbb C\mathrm{vac}\oplus K$ use $\widetilde C_t=1\oplus C_t$, $\widetilde B=0\oplus B$, and $\widetilde j(c,g)=jg$. For a density $\widetilde\Omega$ on $\widetilde K$ apply the same reinsertion construction with $\widetilde\ell$. It again gives a conservative minimal semigroup and the same domain argument, since $\widehat m_{\widetilde\Omega}(z)<1$ for $z>0$. A holding time can now be infinite: if $q=\langle\mathrm{vac},\widetilde\Omega\mathrm{vac}\rangle$, its finite-time density has mass $1-q$. The infinite holding time is absorption, not explosion. The vacuum-decay generator is $\widetilde\Omega=|\mathrm{vac}\rangle\langle\mathrm{vac}|$. Whether this is actually a parity-preserving generator is addressed in T3.

## 2. T2: stationary states and the renewal theorem

### T2(a). Existence, uniqueness, and convergence on $K$

**STATUS: PROVED** under H-MODEL, with H-MEAN exactly the existence condition. Tonelli gives

$$
\mu_\Omega=\int_0^\infty S_\Omega(t)dt
=\int_0^\infty t\,m_\Omega(t)dt.
$$

If $\mu_\Omega<\infty$, the positive Bochner integral $R=\int_0^\infty A_\Omega(t)dt$ exists in trace norm, has trace $\mu_\Omega>0$, and satisfies

$$
\frac{T_h^0R-R}{h}=-\frac1h\int_0^h A_\Omega(t)dt\longrightarrow-\Omega.
$$

Hence $R\in D(A)$, $AR=-\Omega$, $\ell(R)=1$, and

$$
\rho_\infty=\mu_\Omega^{-1}\int_0^\infty C_t\Omega C_t^*dt \tag{2}
$$

is stationary. Its support is the closed span of $C_t\operatorname{supp}\Omega$, $t\ge0$: test the positive integral against a vector and use continuity at every time. In particular it is mixed whenever $\Omega$ is mixed. Conversely any stationary density $\sigma$ belongs to $D(\mathcal L_\Omega)=D(A)$. Writing $r=\ell(\sigma)\ge0$ gives $A\sigma=-r\Omega$ and

$$
T_t^0\sigma=\sigma-r\int_0^t A_\Omega(s)ds.
$$

Strong stability of $C_t$ implies $\|T_t^0\sigma\|_1\to0$ (first for finite-rank approximants, then by contraction). If $r=0$, this contradicts $\operatorname{Tr}\sigma=1$. Taking traces and then the limit proves $1=r\mu_\Omega$ and (2). Thus there is exactly one stationary density when the mean is finite, and none when it is infinite.

For completeness the renewal theorem gives **trace-norm convergence for every initial density**. Let $U=\sum_{n\ge0}m_\Omega^{*n}$ be the renewal measure, with the $n=0$ term $\delta_0$. The event expansion gives $T_t^\Omega\Omega=(U*A_\Omega)(t)$. The holding law is absolutely continuous and proper, hence nonlattice; lattice concentration cannot occur. Blackwell's renewal theorem says $U((t-a,t-b])\to(a-b)/\mu_\Omega$ for fixed $a>b$. It applies here in trace norm to the continuous function $A_\Omega$: its norm is the decreasing integrable envelope $S_\Omega$.

To spell out this last step, approximate $A_\Omega$ on a compact interval by trace-class-valued step functions. Blackwell handles each step. Renewal masses of intervals of a fixed length are uniformly bounded: after the first renewal in such an interval the remaining expected count is bounded by the ordinary renewal count for that length. The latter is finite, since for $z>0$, $U([0,h])\le e^{zh}\sum_{n\ge0}\widehat m_\Omega(z)^n<\infty$. The remaining tail is bounded by a constant times $\sum_{k\ge L}S_\Omega(k)$, which tends to zero. This proves $(U*A_\Omega)(t)\to R/\mu_\Omega$ in trace norm. Finally

$$
T_t^\Omega\rho=A_\rho(t)+\int_0^t m_\rho(s)T_{t-s}^\Omega\Omega\,ds
\longrightarrow\rho_\infty
$$

by dominated convergence and $\int m_\rho=1$. No pointwise convergence of the renewal *density*, no smoothness of $m_\Omega$, and no uniform exponential stability were assumed.

### T2(b). Finite modal formula

**STATUS: PROVED-CONDITIONAL** on H-FINITE. Set $e_n=k_{w_n}/\|k_{w_n}\|$, $w_n=x_n+iy_n$, and

$$
b_n=-i\bar w_n,\quad a_n=-b_n=i\bar w_n=y_n+ix_n,\quad
G_{nm}=\langle e_n,e_m\rangle=\frac{2i\sqrt{y_ny_m}}{w_n-\bar w_m}.
$$

These are linearly independent vectors (finite distinct exponentials, or distinct rational poles), so their Gram matrix is positive definite. Write uniquely

$$
\Omega=\sum_{n,m}\omega_{nm}|e_n\rangle\langle e_m|,
\quad W=(\omega_{nm})\ge0,\quad \operatorname{Tr}(WG)=1.
$$

The coefficients are expansion coefficients, not generally the matrix elements $\langle e_n,\Omega e_m\rangle$. Define

$$
\lambda_{nm}=b_n+\bar b_m=-i\bar w_n+iw_m=-(a_n+\bar a_m).
$$

Every real part is negative. Direct integration gives

$$
\mu_\Omega=\sum_{n,m}\frac{\omega_{nm}G_{mn}}{a_n+\bar a_m},\qquad
\rho_\infty=\frac1{\mu_\Omega}
\sum_{n,m}\frac{\omega_{nm}}{a_n+\bar a_m}|e_n\rangle\langle e_m|. \tag{3}
$$

The sum for $\mu_\Omega$ is real and positive because it is the integral of survival probabilities; individual cross terms need not be real or positive. Exponential decay of a finite sum proves its finiteness.

### T2(c). An explicit infinite-mean rebound

**STATUS: PROVED-CONDITIONAL** on H-MODEL, H-SYM, H-ZCOUNT; also valid if H-RH is added. This is a construction on $K$, not on the unrestricted half-line space.

First a finite calculation. Select any finite zero list $z_1,\ldots,z_N$ of $\Theta$, respecting multiplicities, and put

$$
f_N(\tau)=\sqrt{\frac{\operatorname{Im}z_N}{\pi}}
\frac1{\tau-\bar z_N}
\prod_{k<N}\frac{\tau-z_k}{\tau-\bar z_k}.
$$

This is a normalized Takenaka--Malmquist vector in the model space of the finite Blaschke product dividing $\Theta$, hence belongs to $K$. One can check membership without a basis theorem: $K_{UV}=K_U\oplus U K_V$ for inner $U,V$, and the final kernel spans the one-factor model space. Repeated zeros are permitted; they use generalized modes. By Plancherel, multiplication by time is $-i\partial_\tau$ on the Fourier side. Differentiating the finite product and integrating its Poisson kernels gives

$$
\int_0^\infty t|(Ff_N)(t)|^2dt
=\frac1{2\operatorname{Im}z_N}
+\sum_{k<N}
\frac{2(\operatorname{Im}z_N+\operatorname{Im}z_k)}
{(\operatorname{Re}z_N-\operatorname{Re}z_k)^2+
 (\operatorname{Im}z_N+\operatorname{Im}z_k)^2}. \tag{4}
$$

Indeed $-i\overline{B_{N-1}}B_{N-1}'$ on the real line is the sum of $2\operatorname{Im}z_k/|\tau-z_k|^2$; integrating each against $|e_{z_N}(\tau)|^2$ is the elementary Poisson convolution with summed widths. The first term is the single-kernel mean.

H-SYM moves at least half of any zero count, with multiplicity, into $1/4\le\operatorname{Im}z<1/2$ without changing the real coordinate. H-ZCOUNT and pigeonholing imply arbitrarily large finite zero lists in a real interval of length one in this strip: a uniform bound per interval would give $N_+(T)=O(T)$. For such a list each summand in (4) is at least $1/2$, since the numerator is at least one and the denominator at most two. Thus choose, for each $r\ge1$, a list with $N_r\ge2\cdot4^r+1$ and its vector $f_r$; its mean is at least $4^r$. Then

$$
\Omega_\infty=\sum_{r\ge1}2^{-r}|f_r\rangle\langle f_r|
$$

is a density on $K$ and $\mu_{\Omega_\infty}\ge\sum_{r\ge1}2^{-r}4^r=\infty$. Orthogonality between the $f_r$ is unnecessary. This supplies the requested example with every additional arithmetic input exposed. For a completely arbitrary inner function H-MODEL without the arithmetic counting input, infinite mean need not be available: a finite Blaschke model, for example, has uniformly bounded means.

The vacuum comparison needs a qualification. On the graded space, survival of the vacuum is identically one and its renewal integral diverges, as in `prop:vacuum-renewal-trivial-entanglement`. But its holding law has mass zero on finite times and an atom at infinity; the no-event semigroup is not strongly stable there. It is an **absorbing boundary case**, not a counterexample to the “infinite mean implies no stationary density” theorem on $K$.

## 3. T3: protected coherences and the grading

### T3(a). Odd eigenoperators

**STATUS: CORRECTED.** For every rebound density on the graded space, including one with vacuum--$K$ coherences,

$$
\widetilde{\mathcal L}_{\widetilde\Omega}
(|e_n\rangle\langle\mathrm{vac}|)=b_n|e_n\rangle\langle\mathrm{vac}|,
\qquad
\widetilde{\mathcal L}_{\widetilde\Omega}
(|\mathrm{vac}\rangle\langle e_n|)=\bar b_n|\mathrm{vac}\rangle\langle e_n|. \tag{5}
$$

Thus the eigenvalues are $-i\bar w_n$ for **$|e_n\rangle\langle\mathrm{vac}|$**, and $iw_n$ for its adjoint. The draft assigned them to the opposite orientations. The exit functional of either operator is zero because $\widetilde j\mathrm{vac}=0$; the formula follows on the domain core, and the semigroup acts there exactly by these exponentials. This proves protection, including the rate $y_n$, independently of $\widetilde\Omega$.

More generally the entire odd space is invariant under the evolution, with its two blocks $C_t$ and its conjugate action. Its generator point eigenmodes are exactly the stated zero kernels: an eigenfunction of differentiation in $L^2(0,\infty)$ must be a decaying exponential, and C1 characterizes when that exponential belongs to $\mathcal M$. At a zero of order $m$, the reproducing derivative kernels of orders $0,\ldots,m-1$ lie in $K$ and give the corresponding polynomial-times-exponential Jordan chain. The next derivative kernel fails membership because it detects a nonzero derivative of $\Theta$. Hence multiplicity is encoded by a chain, not by $m$ independent kernel eigenvectors. Under H-SIMPLE each zero contributes one eigenvector in each odd block; conjugate eigenvalue coincidences between labels do not remove their block multiplicities. No completeness or absence of continuous spectrum is inferred.

### T3(b). When this is a graded Lindbladian

**STATUS: CORRECTED.** Put $P=1\oplus(-1_K)$. The generator commutes with $\rho\mapsto P\rho P$ **iff** $P\widetilde\Omega P=\widetilde\Omega$. Indeed the no-event part commutes with parity and $\widetilde\ell(P\rho P)=\widetilde\ell(\rho)$; equality for the reset term, for an input of nonzero exit flux, is precisely that condition. An arbitrary non-even rebound sends some even inputs into odd outputs. The odd subspace still evolves autonomously, but the whole generator is not parity preserving. Freedom of an **even** rebound acts only on the even sector.

### T3(c). Stationarity on the graded space

**STATUS: CORRECTED.** The vacuum is stationary for every rebound. If $\widetilde\Omega=0\oplus\Omega$ and H-MEAN holds, all stationary densities are

$$
q|\mathrm{vac}\rangle\langle\mathrm{vac}|+(1-q)(0\oplus\rho_\infty),
\qquad 0\le q\le1. \tag{6}
$$

For an arbitrary initial density the vacuum mass $q$ is conserved, its $K$ block converges by T2, and its odd block tends to zero by strong stability, proving convergence to (6). This also proves completeness of this stationary list. If the mean is infinite, the vacuum is the only stationary density, but states initially supported on $K$ cannot converge to it in trace norm because their $K$ mass stays one.

If instead $\langle\mathrm{vac},\widetilde\Omega\mathrm{vac}\rangle=q>0$, the vacuum is the unique stationary density and attracts every state. After a reset there is probability $q$ of no further event; the number of finite excursions before absorption is geometrically bounded, and on the final no-event excursion all $K$ components and coherences vanish. Splitting the event expansion at a fixed event count, then letting that count tend to infinity, makes this argument a trace-norm convergence proof. Positivity implies that $q=0$ forces the rebound's vacuum row and column to vanish, so these cases exhaust all densities. In particular, a mixed attracting stationary state on the **entire** graded space is not obtained while retaining the uncoupled vacuum.

## 4. T4: rank-one perturbation, persistence, and the secular equation

### T4(a). Correct persistence criterion

**STATUS: CORRECTED**, with an exact finite answer under H-FINITE. On $\mathcal T(V)$ let $E_{nm}=|e_n\rangle\langle e_m|$. Then

$$
AE_{nm}=\lambda_{nm}E_{nm},\qquad
\ell(E_{nm})=q_{nm}:=2\sqrt{y_ny_m}\ne0,
\quad
\mathcal L_\Omega=A+\Omega\ell. \tag{7}
$$

The frequency of $E_{nm}$ is $x_m-x_n$, with decay $y_n+y_m$. Swapping $n,m$ gives the conjugate frequency and the draft's numerical eigenvalue list, but not its association to $E_{nm}$.

Let $e^n$ be the dual basis, $\langle e^n,e_m\rangle=\delta_{nm}$. The dual coordinate functionals are $\eta_{nm}(X)=\langle e^n,Xe^m\rangle$, so “the component of $\Omega$ along $E_{nm}$” means $\omega_{nm}=\eta_{nm}(\Omega)$.

A particular eigenoperator $X$ of $A$ remains the **same eigenoperator with the same eigenvalue** iff $\ell(X)=0$, because $(\mathcal L_\Omega-z)X=\Omega\ell(X)$. Vanishing of a rebound coefficient is not a second way for that operator to persist. If $z$ is a **simple eigenvalue of $A$**, its eigenvalue persists iff $\ell(X)\eta_X(\Omega)=0$. The surviving eigenvector may have changed.

Simplicity of the $w_n$ does not make all $\lambda_{nm}$ distinct. For a distinct value $\lambda$ let $d_\lambda$ be its multiplicity, $P_\lambda$ its coordinate spectral projection for $A$, and $r_\lambda=\ell(P_\lambda\Omega)$. The determinant lemma gives the exact formula

$$
\det(z-\mathcal L_\Omega)
=\prod_\lambda(z-\lambda)^{d_\lambda}
\left(1-\sum_\lambda\frac{r_\lambda}{z-\lambda}\right). \tag{8}
$$

The right side is read after cancellation as a polynomial. If $r_\lambda\ne0$, the old eigenvalue has algebraic multiplicity exactly $d_\lambda-1$. If $r_\lambda=0$, its multiplicity is $d_\lambda$ plus the order of vanishing at $\lambda$ of $1-\sum_{\nu\ne\lambda}r_\nu/(z-\nu)$. In particular every eigenspace of dimension at least two supplies at least $d_\lambda-1$ unchanged eigenvectors in $\ker\ell$. This proves the claimed simple-eigenvalue criterion and the necessary degenerate replacement. Generalized eigenvectors individually have no proposed “iff” criterion; one uses the determinant/resolvent with its higher-order poles if $A$ has Jordan blocks. The selected-kernel finite $A$ here is diagonalizable, although the perturbation can create Jordan blocks.

### T4(b). Secular roots and their domain of validity

**STATUS: CORRECTED.** Away from the old finite spectrum the new eigenvalues are exactly

$$
1=\ell(z-A)^{-1}\Omega=\widehat m_\Omega(z), \tag{9}
$$

where the last expression outside the integral's convergence half plane means its rational continuation. If (9) holds, $X=(z-A)^{-1}\Omega$ is a nonzero eigenoperator: $(z-\mathcal L_\Omega)X=\Omega(1-\ell X)=0$. Conversely an eigenoperator at $z\notin\operatorname{spec}A$ must have nonzero exit functional and is proportional to this $X$. Formula (8) handles values at poles, including cancellations, which must not be decided by plugging infinity into (9).

On the full trace class the same statement holds for $z\in\rho(A)$, with $\ell R_0(z)\Omega$ in place of a presumed Laplace continuation. Formula (1) proves it. It does **not** describe the whole spectrum at $z\in\operatorname{spec}A$, nor establish meromorphicity there. A warning is already supplied by T2: $\widehat m_\Omega(0)=1$ for every rebound on $K$, but when $\mu_\Omega=\infty$ there is no stationary density. At such a point the requisite trace-class eigenoperator integral does not exist. H-FINITE for the rebound does not turn the infinite Hilbert space into the finite restriction $V$.

### T4(c). Explicit Gram formula

**STATUS: PROVED-CONDITIONAL** on H-FINITE. In the notation of T2(b),

$$
S_\Omega(t)=\sum_{n,m}\omega_{nm}G_{mn}e^{\lambda_{nm}t},\qquad
m_\Omega(t)=\sum_{n,m}\omega_{nm}q_{nm}e^{\lambda_{nm}t},
$$

because $-\lambda_{nm}G_{mn}=q_{nm}$. Consequently

$$
\widehat m_\Omega(z)
=\sum_{n,m}\frac{2\sqrt{y_ny_m}\,\omega_{nm}}{z+i\bar w_n-iw_m}
=\sum_{n,m}\frac{2\sqrt{y_ny_m}\,\omega_{mn}}{z-iw_n+i\bar w_m}. \tag{10}
$$

It is a rational function with possible cancellations; the integral agrees with it, for example, when $\operatorname{Re}z>-2\min y_n$. The unnormalized kernel Gram constant requested in the brief is $c=2\pi i$. For $\operatorname{Re}z>0$, $|\widehat m_\Omega(z)|<1$. On the imaginary axis equality $\widehat m_\Omega(iu)=1$ forces $u=0$, since a probability density cannot be supported on the discrete set where $e^{-iut}=1$. Thus the finite stationary eigenvalue is the only imaginary-axis secular root.

The scalar “one equals a sum of fractions” shape is a universal determinant identity for a rank-one perturbation. No identification with a Connes--Consani--Moscovici operator, coefficients, or arithmetic construction has been proved; resemblance of this shape supplies none.

For an even rebound supported on $K$, the finite graded **even** spectrum additionally has the independent vacuum eigenvalue zero. If the rebound has vacuum weight, the $K$ reset block is substochastic instead; if it has odd coherences, the even space is not invariant. Equations (7)–(10) concern the recurrent $K$ block as stated.

## 5. T5: modal mixtures, RH, and the nonorthogonal Gram matrix

### T5(a). Fixed rebound and stationary density

**STATUS: CORRECTED.** For a finite mixture $\Omega=\sum_n p_n|e_n\rangle\langle e_n|$, $p_n\ge0$, $\sum p_n=1$, equation (3) gives

$$
\mu=\sum_n\frac{p_n}{2y_n},\qquad
\rho_\infty=\sum_n\frac{p_n/(2y_n)}{\mu}|e_n\rangle\langle e_n|. \tag{11}
$$

For a specified family of distinct zeros, equality $\rho_\infty=\Omega$ for **every finitely supported probability vector** on that family is equivalent to all its widths being the same. Sufficiency is immediate. For necessity take a mixture with positive weights on any two indices. Linear independence of their rank-one operators forces $1/(2y_n)=1/(2y_m)$. A singleton gives no test at all.

Equality of widths in an arbitrary selected family does not force the value $1/4$. With H-SYM and the quantifier over **all** arithmetic zeros, a common width must equal its reflected width $1/2-y$, hence must be $1/4$. Therefore

$$
\text{H-RH}\quad\Longleftrightarrow\quad
\rho_\infty=\Omega\ \text{for every finite modal mixture over all arithmetic zeros}.
$$

The same implication holds for a nonempty reflection-closed finite family, interpreted as RH for that family. This is a renewal-channel reformulation of the already known equal-rate criterion in C1, not an additional mechanism or evidence for RH.

### T5(b). The density spectrum is not the list of weights

**STATUS: CORRECTED.** Put $r_n=p_n/(2y_n\mu)$ and $D_r=\operatorname{diag}(r_n)$. The nonzero eigenvalues of (11) are

$$
\operatorname{spec}_{\ne0}(D_r^{1/2}G D_r^{1/2}), \tag{12}
$$

equivalently those of $G^{1/2}D_rG^{1/2}$. This follows by applying the equality of nonzero spectra of $TT^*$ and $T^*T$ to the synthesis map with columns $\sqrt{r_n}e_n$. Distinct kernels have **nonzero** inner products, so their probability weights are not in general eigenvalues. Under H-RH the *operators* $\rho_\infty$ and $\Omega$ coincide, and hence so do their true spectra; neither spectrum need be $\{p_n\}$.

For example $w_1=i/4$, $w_2=1+i/4$, $p_1=p_2=1/2$ give $|G_{12}|=1/\sqrt5$ and density eigenvalues $(1\pm1/\sqrt5)/2$, approximately $0.7236067977,0.2763932023$, rather than $1/2,1/2$. In the repository's convention the entanglement energies are the negative logarithms of (12).

### T5(c). Complete finite spectrum of a modal reset

**STATUS: PROVED-CONDITIONAL** on H-FINITE, with the following corrections to persistence. Let $r_n^{\rm exit}=2y_n$, denoted $h_n$ in this paragraph to avoid confusion with (12). In diagonal/off-diagonal **coefficient** blocks the generator is triangular: the diagonal block is

$$
M=-\operatorname{diag}(h_n)+p h^T,
$$

while each off-diagonal coordinate has diagonal entry $\lambda_{nm}$, $n\ne m$. Off-diagonal coordinates can feed the diagonal block, so their original $E_{nm}$ are generally not eigenoperators of the perturbed generator. The characteristic polynomial is exactly

$$
\prod_{n\ne m}(z-\lambda_{nm})\,
\prod_n(z+h_n)\left(1-\sum_n\frac{p_n h_n}{z+h_n}\right). \tag{13}
$$

Thus all off-diagonal eigenvalues persist as eigenvalues, with their indicated factors. Formula (13) also handles zero weights. If all weights are positive, group the distinct exit rates as $h^{(j)}$, with multiplicities $g_j$ and group masses $P_j$. Each old diagonal value $-h^{(j)}$ persists $g_j-1$ times; the remaining roots solve $1=\sum_jP_jh^{(j)}/(z+h^{(j)})$. They are zero and one simple negative real root strictly between each two successive poles. This follows from the strictly negative derivative of the sum on every pole-free real interval and its limits at the poles. There are exactly as many roots as distinct rates, by (13).

Under H-RH,

$$
\widehat m(z)=\frac{1/2}{z+1/2},\qquad
\operatorname{spec}(\mathcal L_\Omega|_{\mathcal T(V)})
=\{0\}\uplus\{-1/2\}^{N-1}
\uplus\{-1/2+i(x_m-x_n):n\ne m\}. \tag{14}
$$

The only new eigenvalue is zero and it is simple in this $K$ block. These statements are about the finite restriction; they are not a computation of the full infinite-channel spectrum. The graded finite model with rebound inside $K$ has a second zero eigenvalue from the vacuum.

## 6. T6: inverse problem and realizable spectra

### T6(a). Exact admissibility criterion and uniqueness of the rebound

**STATUS: PROVED** under H-MODEL with the precise domain condition stated here. A density $\sigma$ on $K$ is stationary for some reset density iff

$$
\sigma\in D(A),\qquad Q_\sigma:=-A\sigma\ge0. \tag{15}
$$

In that case $r=\operatorname{Tr}Q_\sigma=\ell(\sigma)>0$ and the unique choice is

$$
\Omega=Q_\sigma/r,\qquad \mu_\Omega=1/r. \tag{16}
$$

Necessity follows from $D(\mathcal L_\Omega)=D(A)$ and stationarity. Sufficiency is immediate from (16); positivity and $r=0$ would imply $A\sigma=0$, contradicted by strong stability. T2 then proves the mean statement and uniqueness of the stationary density on $K$. In (15), $A\sigma=B\sigma+\sigma B^*$ means the generator derivative; separately defined trace-class products are a sufficient interpretation, not a necessary extra assumption.

An equivalent semigroup formulation is $T_t^0\sigma\le\sigma$ for every $t\ge0$, **retaining** the condition $\sigma\in D(A)$. Differentiation gives necessity of $-A\sigma\ge0$, and integrating $T_t^0Q_\sigma$ proves sufficiency. In particular the support of an admissible density is $C_t$-invariant, since $C_t\sigma C_t^*\le\sigma$ forces $C_t\overline{\operatorname{ran}\sigma}\subset\overline{\operatorname{ran}\sigma}$. This already restricts choices of prescribed eigenvectors.

### T6(b). What the orbit-cone statement means

**STATUS: CORRECTED.** For a unit vector of finite lifetime set $\Phi(\psi)=\int_0^\infty|C_t\psi\rangle\langle C_t\psi|dt$. The admissible densities are exactly the trace-norm sums

$$
\sigma=\sum_\alpha c_\alpha\Phi(\psi_\alpha),\qquad
c_\alpha\ge0,\quad 0<\sum_\alpha c_\alpha<\infty,\quad
\sum_\alpha c_\alpha\operatorname{Tr}\Phi(\psi_\alpha)=1. \tag{17}
$$

To prove necessity, spectrally decompose $Q_\sigma=r\Omega$ and use (2) and Tonelli; every component with positive weight has finite lifetime. Conversely the partial sums in (17) converge in trace norm and their $A$-images converge to $-\sum c_\alpha|\psi_\alpha\rangle\langle\psi_\alpha|$. Closedness of $A$ proves (15). If using normalized orbit states $\Phi(\psi)/\mu_\psi$, the corresponding convex weights $v_\alpha$ must satisfy $\sum v_\alpha/\mu_{\psi_\alpha}<\infty$. An unspecified closed cone or arbitrary infinite convex combination omits this finite-flux domain condition.

### T6(c). Finite Schur test and prescribed eigenvectors

**STATUS: CORRECTED**, proved under H-FINITE. For $\sigma=\sum s_{nm}|e_n\rangle\langle e_m|$, let $S=(s_{nm})\ge0$ and $\operatorname{Tr}(SG)=1$. Since synthesis by independent vectors is invertible onto $V$, positivity of an operator is equivalent to positivity of its coefficient matrix. Consequently (15) is exactly

$$
\big((a_n+\bar a_m)s_{nm}\big)_{nm}\ge0,
\qquad a_n=i\bar w_n=y_n+ix_n. \tag{18}
$$

This corrects the draft's conjugation. The Hermitian matrix $(a_n+\bar a_m)$ has rank at most two, and is indefinite for at least two distinct modes: its two-index determinant is

$$
4y_ny_m-|a_n+\bar a_m|^2
=-(y_n-y_m)^2-(x_n-x_m)^2<0.
$$

It is rank one and positive when there is only one mode. Thus (18) is a genuine restriction, not automatic positivity preservation. In particular every admissible coefficient matrix must satisfy

$$
|s_{nm}|^2\big((y_n+y_m)^2+(x_n-x_m)^2\big)
\le4y_ny_m s_{nn}s_{mm}. \tag{19}
$$

For prescribed orthonormal eigenvectors $u_i\in V$ and weights $d_i$, put $c_{ni}=\langle e^n,u_i\rangle$, so $s_{nm}=\sum_i d_i c_{ni}\bar c_{mi}$. Equations (18)–(19) give an explicit condition on that choice of eigenvectors in terms of the modes. They answer “which $\sigma$” exactly in finite dimension; the two-by-two inequalities alone are only necessary in larger dimension. An isometry cannot map different standard basis vectors to the normalized kernels themselves, because $G_{nm}\ne0$.

A further sharp restriction illustrates this: an admissible pure state must span a $B$-invariant line, hence be a mode. Indeed the support argument in T6(a) makes its line $C_t$-invariant; the continuous scalar semigroup on that line is $e^{bt}$, which puts its spanning vector in $D(B)$ and makes it a $B$-eigenvector. A nonmodal coherent superposition is therefore not admissible as a pure stationary state. Modal *mixtures* are admissible: the matrix in (18) is diagonal positive for them. This does not make their mixture weights their density eigenvalues.

### T6(d). Every finite density spectrum is attainable, without RH

**STATUS: PROVED-CONDITIONAL** on the availability of $N$ distinct modes (H-INFINITE supplies all $N$). This replaces the incorrect purported trivial deduction from T5.

Order any $N$ distinct modes and let $V_k$ be the span of the first $k$, $P_k$ its orthogonal projection, and $u_1,\ldots,u_N$ the Gram--Schmidt basis adapted to this invariant flag. Each $V_k$ is $B$-invariant. Therefore

$$
Q_k:=-(BP_k+P_kB^*)\ge0,
\qquad Q_k=j_k^*j_k\ \text{on }V_k,
\qquad \operatorname{Tr}Q_k=2\sum_{n\le k}y_n, \tag{20}
$$

where $j_k=j|_{V_k}$. These are finite-rank trace-class operators on $K$, with zero extension outside $V_k$. To check (20), $BP_k$ and its adjoint are supported on $V_k$, where C2 applies; the trace equals minus twice the real part of the trace of $B|_{V_k}$, whose eigenvalues are $b_1,\ldots,b_k$.

Sort the requested nonzero eigenvalues $p_1\ge\cdots\ge p_N>0$, $\sum p_i=1$, and put $p_{N+1}=0$. Then

$$
\sigma=\sum_{i=1}^Np_i|u_i\rangle\langle u_i|
=\sum_{k=1}^N(p_k-p_{k+1})P_k,
\qquad
Q_\sigma=\sum_{k=1}^N(p_k-p_{k+1})Q_k\ge0. \tag{21}
$$

It has exactly the requested density spectrum. Its unique rebound is $Q_\sigma/r$, with $r=2\sum_{n=1}^Np_ny_n$. No RH and no orthogonality of the original modes were used. Its prescribed entanglement energies are $-\log p_i$ in the notebook's terminology.

The rebound need not be mixed. In fact for a maximally mixed finite-rank stationary density $P_N/N$, the unique rebound is $Q_N/\operatorname{Tr}Q_N$, which is **pure**, because the exit has dimension one. This holds for any admissible flat finite-rank density: its support is invariant, and its finite-dimensional semigroup restriction puts that support in $D(B)$, where the same exit calculation applies. Thus mixed stationary states do not require mixed rebounds. A demand that *every* prescribed finite spectrum, including a flat one, be achieved by a mixed rebound would be false in this fixed one-exit construction. For the flag construction, the rebound rank is exactly the number of positive differences $p_k-p_{k+1}$: the Riesz vectors of $j_k$ have nonzero $k$th coordinate, since $|ju_k|^2=\operatorname{Tr}Q_k-\operatorname{Tr}Q_{k-1}=2y_k$. The selected Riesz vectors are therefore independent. In particular a nonflat positive finite spectrum gives a mixed rebound.

### T6(e). Infinite Gibbs weights and the condition on $U$

**STATUS: PROVED-CONDITIONAL** on H-MODEL and H-INFINITE for the construction; **OPEN** for a distinguished arithmetic identification. Let $D_\beta=\operatorname{diag}(d_n)$, $d_n=n^{-\beta}/\zeta(\beta)$, $\beta>1$. For a specified isometry $U:\ell^2(\mathbb N)\to K$, the exact criterion is

$$
UD_\beta U^*\in D(A),\qquad -A(UD_\beta U^*)\ge0. \tag{22}
$$

For vectors in $D(B)$ and convergent trace-class products this is precisely $-(BUD_\beta U^*+UD_\beta U^*B^*)\ge0$. For example $Ue_n\in D(B)$ and $\sum d_n\|BUe_n\|<\infty$ is a sufficient product-domain condition, but is not necessary. Its support $\operatorname{ran}U$ must be $C_t$-invariant. In any finite modal realization the necessary inequalities (19), with $s_{nm}=\sum_i d_i\langle e^n,Ue_i\rangle\overline{\langle e^m,Ue_i\rangle}$, are explicit modal restrictions on $U$. More generally (22) requires $-2\operatorname{Re}\langle B^*v,UD_\beta U^*v\rangle\ge0$ for every $v\in D(B^*)$.

Existence of **some** such $U$ can be proved rather than left as an obstacle. Enumerate distinct modes and Gram--Schmidt their invariant flag as above; let $Ue_n=u_n$. For any decreasing probability sequence $(d_n)$, not just Gibbs weights, set $\Delta_k=d_k-d_{k+1}$. Then

$$
\sigma=UDU^*=\sum_{k\ge1}\Delta_kP_k,
\qquad Q=\sum_{k\ge1}\Delta_kQ_k,
\qquad r=\operatorname{Tr}Q=2\sum_{n\ge1}d_ny_n\in(0,1). \tag{23}
$$

All sums converge in trace norm. For $\sigma$, positivity and $\sum k\Delta_k=\sum d_n=1$ suffice (a decreasing summable sequence has $nd_n\to0$). For $Q$, use (20), Tonelli, and $0<y_n<1/2$ to get $\sum\Delta_k\operatorname{Tr}Q_k=2\sum d_ny_n<1$. The partial sums have $A$-images $-\sum\Delta_kQ_k$, so closedness of $A$ proves (22), without separately summing the possibly enormous imaginary frequencies. Equations (16) and (23) now construct the rebound and stationary state with exactly the Gibbs density spectrum. For Gibbs weights every $\Delta_k$ is positive, so the independence argument after (21) makes the rebound infinite-rank, in particular mixed. Completeness of the kernels in all of $K$ is not required: $U$ is an isometry onto their closed span.

Under H-RH this whole flag family has $r=1/2$ and $\mu_\Omega=2$, for **every** $\beta>1$. Thus the critical normal-state obstruction is not forced to appear as a diverging holding time. At $\beta=1$, $\sum_n n^{-1}=\infty$, so the proposed normal Gibbs density does not exist before one asks about positivity or renewal time. This is the trace-normalization obstruction of `prop:normal-kms-gibbs`, distinct from both failure of (22) for a prescribed $U$ and the infinite-mean example in T2.

What remains open is to identify this freely chosen flag isometry with the Bost--Connes arithmetic representation, its observables and dynamics, rather than merely transport a list of Gibbs eigenvalues. No distinguished $U$, prime action, detailed balance, or critical nonnormal state is furnished by (23).

## 7. T7: what this buys for the two-halves conjecture

**STATUS: CORRECTED**, with the constructive claims proved above and the arithmetic identification **OPEN**. Rebounding inside $K$ gives a conservative renewal Lindbladian with a unique stationary density on $K$ whenever the rebound has finite mean, and that density is mixed whenever the rebound is mixed; finite invariant flags let one prescribe every finite density spectrum, and an infinite flag gives the Gibbs spectrum for $\beta>1$. Adjoining an uncoupled even vacuum and keeping the rebound inside $K$ gives a parity-preserving generator carrying that stationary density and all zero coherences plus their conjugates, with multiplicities interpreted by T3, but also the separate stationary vacuum and their convex mixtures: there is no unique mixed attractor on the whole graded space. A chosen mixed rebound has the stationary spectrum calculated by (2), not automatically its modal mixture weights; prescribing the spectrum uses the inverse construction, whose rebound may even be pure for a flat target. The spectrum and isometry have been supplied by hand, with no arithmetic selection of $\Omega$, no identification with the Bost--Connes bond/algebra, and no normal critical KMS state. In finite modal restrictions the nonstationary even spectrum comprises surviving pair modes and the changes specified by the secular determinant; this is not an assertion that the infinite even spectrum has been exhausted. Consequently, once this construction is included, “no construction in this book has both” in `obs:complementary-halves` is false if “both” means zeros as odd modes and a stationary density with the desired Gibbs **eigenvalue list** (or just nontrivial entanglement). T3+T5 alone only establish the weaker coexistence with a mixed stationary state; T6 supplies the prescribed spectrum. The observation and `conj:phantasm-both-halves` remain unresolved in their substantive arithmetic sense: a Bost--Connes KMS state with the required algebraic identification, especially at the critical temperature, has not been constructed here.

## Correction ledger

| No. / item | Draft problem or missing qualification | Correct statement / location |
|---|---|---|
| 1 / **C-SIGN** | `04_riemann_channel.tex:71–75` puts $e^{-it\bar\lambda}$ on a lower-half-plane kernel and calls it decay. | It grows. Here $C_tk_w=e^{-it\bar w}k_w$ for $w\in\mathbb C_+$. Keeping the lower-half-plane compression instead gives $Z_tk_\lambda=e^{it\bar\lambda}k_\lambda$. Section 0. |
| 2 / C1-Fourier | The specified linear Fourier convention and $Fk_w\propto e^{iwx}$ are incompatible. | $Fk_w=-i\sqrt{2\pi}e^{-i\bar w x}$. C1. |
| 3 / C2-domain | $j$ was treated as a Hilbert-space vector and $B+B^*$ as an everywhere defined operator. | $D(B)=\mathcal M\cap H^1$; evaluation is a graph-continuous exit form. C2. |
| 4 / C3-boundary | “$k_w(0)$” confuses time and spectral evaluation. | The exit is $(Fk_w)(0)=-i\sqrt{2\pi}$. C3. |
| 5 / C4-norm | Strong stability, constant modal widths, and uniform exponential stability are different statements. | No $\|C_t\|=1$ assertion is used; H-UES is only a comparison. C4, T2(c). |
| 6 / T1-law | A derivative at every time and iid holding times including an arbitrary initial state were implicit. | Density and derivative are a.e.; the first law is $m_\rho$, subsequent laws $m_\Omega$. Section 1. |
| 7 / T1-SHW | Formal trace cancellation does not prove conservativity or specify a domain. | Nonexplosion plus the rank-one resolvent prove conservativity and $D(\mathcal L)=D(A)$. T1. |
| 8 / T2-global | Finite mean and the mode of convergence require specification. | Exactly finite mean gives the unique density on $K$ and convergence of every state in trace norm. T2(a). |
| 9 / T2-infinite-example | Infinite mean is not automatic for an arbitrary model space. | The construction uses explicitly H-SYM and H-ZCOUNT; it works even under RH. T2(c). |
| 10 / T2-vacuum | The vacuum's divergent integral was presented as the same recurrent infinite-mean case. | Its holding law is defective and strong stability fails; an absorbing stationary vacuum can exist. T2(c), T3(c). |
| 11 / T3-orientation | The two odd eigenvalues were assigned to the opposite rank-one operators. | Equation (5). |
| 12 / T3-parity | Every rebound was called graded and said to affect only the even sector. | Parity is preserved iff the rebound is even. Arbitrary rebounds still leave odd inputs autonomous. T3(b). |
| 13 / T3-stationarity | Uniqueness on $K$ was liable to be inherited by the graded extension. | Vacuum remains stationary; internal rebound gives the whole segment (6). Positive vacuum rebound weight restores the unique pure-vacuum attractor. T3(c). |
| 14 / T3-multiplicity | Repeated zeros were treated as ordinary repeated kernel eigenvectors. | They give generalized derivative-kernel chains; H-SIMPLE is needed for the ordinary-vector wording. T3(a). |
| 15 / T4-pair-sign | $iw_n-i\bar w_m$ was assigned to $\lvert e_n\rangle\langle e_m\rvert$. | The eigenvalue is $-i\bar w_n+iw_m$; the pair multiset is the same after swapping indices. T4(a). |
| 16 / T4-persistence | Persistence of a specified eigenoperator was conflated with persistence of its eigenvalue. | The former requires $\ell(X)=0$; the simple-eigenvalue criterion is $\ell(X)\eta_X(\Omega)=0$. T4(a). |
| 17 / T4-degeneracy | Simple zeros were assumed to make pair eigenvalues simple; generalized cases were assigned the same iff. | Pair collisions occur even for simple zeros. Use multiplicities/residues in (8), and higher resolvent poles for Jordan blocks. T4(a). |
| 18 / T4-secular | All infinite-channel spectral points were implicitly covered by a Laplace root. | Use (9) off the old spectrum, finite rational continuation where justified, and the determinant at poles. $\widehat m(0)=1$ alone does not give a normal stationary state. T4(b). |
| 19 / T4-finite | Finite support of $\Omega$ was equated with a finite-dimensional full generator. | Full finite formulas apply on the invariant restriction $\mathcal T(V)$; an infinite complement remains. T4(b). |
| 20 / T4-arithmetic | The secular shape suggested a proved CCM identification. | Only the universal rank-one determinant identity is established. T4(c). |
| 21 / T5-RH | Equality of all widths in any selected set was equated with width $1/4$. | Need all-zero quantification and H-SYM, or a reflection-closed selected family. A singleton gives no test. T5(a). |
| 22 / T5-spectrum | Modal mixture weights were called density eigenvalues. | Use the Gram spectrum (12); distinct kernels are nonorthogonal. T5(b). |
| 23 / T5-entanglement | The brief's weights were called the spectrum in `def:bond-entanglement`. | That definition uses $-\log$ of the density eigenvalues. Preamble, T5(b). |
| 24 / T5-even | Persistence and the new root were given without pole multiplicities or restriction of scope. | The exact finite characteristic polynomial is (13), reducing to (14) under RH; the graded vacuum adds another zero. |
| 25 / T6-domain | $-(B\sigma+\sigma B^*)\ge0$ was asserted without a precise domain or positive finite flux. | Use $\sigma\in D(A)$ and $Q_\sigma=-A\sigma\ge0$; flux is then strictly positive and finite. T6(a). |
| 26 / T6-cone | An unrestricted “cone generated by orbit states” omits convergence of the input flux. | The exact countable cone is (17); arbitrary closure is not asserted. T6(b). |
| 27 / T6-Schur | $a_n=-iw_n$ uses the other frequency convention; rank two/indefiniteness has a one-mode exception. | Here $a_n=i\bar w_n$; the matrix has rank at most two and is indefinite for distinct pairs. T6(c). |
| 28 / T6-spectra | Arbitrary spectra were declared trivial from T5 under RH. | T5 does not give arbitrary eigenvalues. The invariant-flag proof (21) gives every finite spectrum without RH. |
| 29 / T6-U | Finding any abstract isometry with Gibbs spectrum was conflated with identifying the arithmetic bond. | (23) constructs an admissible isometry; arithmetic observables, dynamics, and a distinguished choice remain open. |
| 30 / T6-critical | Failure at $\beta=1$ was offered as either infinite mean or positivity failure. | The candidate is not trace class. Under RH the constructed $\beta>1$ family has mean exactly two. T6(e). |
| 31 / T7-mixed-reset | A mixed stationary state was tacitly taken to require a mixed rebound, or every target to allow one. | A finite flat stationary spectrum forces a pure rebound in this one-exit model. T6(d). |
| 32 / T7-both-halves | Coexistence of a prescribed spectrum and odd modes was liable to be identified with the full conjecture. | The literal spectral-only obstruction is removed; arithmetic KMS identification, critical normality, and a unique mixed graded attractor are not. T7. |

## Numerical checks

Author of the check: `codex:gpt-6-astra`. One in-memory `python3` run used NumPy and SciPy; it wrote no files. It tested synthetic points, not actual zeta zeros. The following is the code run (formatting condensed only):

```python
import numpy as np
from scipy.linalg import cholesky
from scipy.integrate import quad
from scipy.special import eval_laguerre
np.set_printoptions(precision=10, suppress=True)
for w,p in [(np.array([0+.25j,1+.25j]),np.array([.5,.5])),
            (np.array([0+.2j,1+.4j]),np.array([.3,.7]))]:
    y=w.imag
    G=2j*np.sqrt(y[:,None]*y[None,:])/(w[:,None]-w.conj()[None,:])
    R=cholesky(G,lower=False)
    b=-1j*w.conj()
    B=R@np.diag(b)@np.linalg.inv(R)
    j=(-1j*np.sqrt(2*y))@np.linalg.inv(R)
    Om=R@np.diag(p)@R.conj().T
    mu=np.sum(p/(2*y))
    sig=R@np.diag(p/(2*y)/mu)@R.conj().T
    Q=np.outer(j.conj(),j)
    L=(np.kron(np.eye(2),B)+np.kron(B.conj(),np.eye(2))
       +np.outer(Om.reshape(-1,order='F'),Q.T.reshape(-1,order='F')))
    eig=np.linalg.eigvals(L)
    eig=eig[np.lexsort((eig.imag,np.round(eig.real,8)))]
    print('w =',w,'p =',p)
    print('Gram =',G)
    print('exit residual =',np.linalg.norm(B+B.conj().T+Q))
    print('mu =',mu,'stationary spectrum =',np.linalg.eigvalsh(sig))
    print('L spectrum =',eig)
    print('stationarity residual =',np.linalg.norm(
        B@sig+sig@B.conj().T+np.trace(Q@sig)*Om))
    if np.allclose(y,.25):
        target=np.diag([.7,.3])
        A=-(B@target+target@B.conj().T)
        print('flag target loss eigenvalues =',np.linalg.eigvalsh(A),
              'rate =',np.trace(A))
        psi=R@np.ones(2); psi=psi/np.linalg.norm(psi)
        pure=np.outer(psi,psi.conj())
        print('nonmodal pure loss eigenvalues =',np.linalg.eigvalsh(
            -(B@pure+pure@B.conj().T)))
y=.25; N=4
mean=quad(lambda t:t*2*y*np.exp(-2*y*t)
          *eval_laguerre(N-1,2*y*t)**2,0,np.inf)[0]
print('repeated-zero TM mean (N=4, y=.25) =',mean,
      'formula =',(2*N-1)/(2*y))
print('old lower-half-plane modulus =',np.exp(.25),
      'correct upper-half-plane modulus =',np.exp(-.25))
```

| Check | Result |
|---|---|
| Equal widths $w=(i/4,1+i/4)$, $p=(1/2,1/2)$ | $\mu=2$; stationary density eigenvalues $0.2763932023,0.7236067977$; generator eigenvalues $0,-0.5,-0.5\pm i$. |
| Unequal widths $w=(0.2i,1+0.4i)$, $p=(0.3,0.7)$ | $\mu=1.625$; stationary density eigenvalues $0.2551434070,0.7448565930$; generator eigenvalues $0,-0.52,-0.6\pm i$. |
| Exit-form and stationarity residuals, both cases | At most $2.85\times10^{-16}$ and $1.41\times10^{-16}$ respectively. |
| Flag target spectrum $(0.7,0.3)$, equal-width case | Loss eigenvalues $0.0697224362,0.4302775638$; trace flux $0.5$. |
| Pure nonmodal superposition of the two modes | Loss eigenvalues $-0.1423503277,0.9756836610$; positivity fails. |
| Four repeated zeros at $i/4$, last TM vector | Numerical mean $13.999999999999995$; formula (4) gives $14$. |
| Old versus corrected modulus, width $1/4$, time one | $1.2840254167$ versus $0.7788007831$. |

## What a refuter should attack first

- The exact domain identity $D(\mathcal L_\Omega)=D(A)$ from the rank-one resolvent; the inverse theorem depends on it.
- The trace-norm renewal limit for a merely $L^1$ holding density, especially the uniform interval-mass bound and integrable survival envelope.
- The one-exit projection identity (20) and the closed-generator limit in (23), which carry the prescribed-spectrum construction.
- The sign and index conventions in (3), (7), and (10); compare physical Gram matrices, not orthonormal-coordinate guesses.
- Any attempted upgrade from Gibbs eigenvalues to a Bost--Connes KMS identification, or from finite secular formulas to the whole infinite spectrum.
