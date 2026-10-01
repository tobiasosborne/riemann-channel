# Weil positivity and the Weyl–Heisenberg bond: analytic arguments

Author: `claude:fable-5.1`, 2026-10-01, working alone at TJO's request ("I want analytical proof techniques to connect
Weil positivity with the bond space"; "elaborate and investigate; work alone, no subagents; record learnings durably").
Status: **a record, not a round.** Nothing is registered in `db/claims.tsv`; no REFUTE review has run. Each statement
carries its own status: *proved here*, *sketched*, *cited* (with a byte address on disk), *heuristic*, or *open*.
Classical facts without a local source are marked "not byte-cited". Connes 1998 is on disk at
`refs/src/math/9811068/main.tex` and is cited by line.

Conventions. $\mathbb A$ = adeles of $\mathbb Q$; $\psi$ the standard character of $\mathbb A/\mathbb Q$; $\mathcal S(\mathbb A)$ Schwartz–Bruhat;
$\hat f$ the self-dual Fourier transform. $C_{\mathbb Q}=\mathbb A^\times/\mathbb Q^\times$; in the units-invariant trivial-character
sector, functions on $C_{\mathbb Q}$ are functions on $\mathbb R_+^\times$. $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$, $\Xi(t)=\xi(\tfrac12+it)$.
For $h\in C_c^\infty(\mathbb R_+^\times)$: $\hat h(s)=\int h(x)x^s\,d^\times x$, $\tilde h(x)=x^{-1}\overline{h(1/x)}$, $g=h*\tilde h$, so
$\hat g(s)=\hat h(s)\overline{\hat h(1-\bar s)}$. Weil's zero form $Z(h)=\sum_\rho\hat g(\rho)$, pole form $P(h)=\hat g(0)+\hat g(1)=2\,\mathrm{Re}\,\hat h(0)\overline{\hat h(1)}$,
local form $\mathrm{Loc}(h)=\sum_v W_v(g)$; explicit formula $Z=P-\mathrm{Loc}$ (`cit:weil-criterion`; Connes's Theorem 6,
`main.tex:4788-4800`). RH $\iff Z\ge0$.

---------------------------------------------------------------------------------------------------------------------

## 0. Learnings in one page

- **L1 (where the bond's positivity lives).** The bond's canonical Hilbert structures give the weighted orbit norms
  $B_\sigma(f)=\int_{C_{\mathbb Q}}|Ef|^2|a|^{2\sigma-1}d^\times a=\tfrac1{2\pi}\int|Z(f,\sigma+it)|^2dt$. These are log-convex in $\sigma$ and
  symmetric under $f\mapsto\hat f$, $\sigma\mapsto1-\sigma$. So the orbit norm increases away from the unitary axis, *averaged over $t$*. Proved (§1).
- **L2 (RH is the pointwise version of L1).** RH $\iff\mathrm{Re}\,\xi'/\xi(\sigma+it)>0$ on $\sigma>\tfrac12$ $\iff$ $\sigma\mapsto|\xi(\sigma+it)|$ is strictly
  increasing on $[\tfrac12,\infty)$ for every $t$. Proved (§2).
- **L3 (blindness).** Every statement of L1 type holds for every entire function with the same symmetry and growth,
  wherever its zeros are. So no inequality among vertical-line norms (Connes's polynomial weights, exponential weights, the
  energy/Hardy metric) can detect an off-line zero. Localising in $t$ at width $\delta$ costs a factor $e^{\eta^2/\delta^2}$, which
  always beats the gain $(\delta/\eta)^2$. Proved (§3).
- **L4 (the cutoff limit is the harmonic-measure form).** Connes's cutoff traces converge, in function fields, to
  $\Delta_\infty(f)=\sum_\rho\int\hat f\,d\mu_\rho$, with $\mu_\rho$ the harmonic measure of $\rho$ on the critical line (cited, `main.tex:2644-2660`).
  This form is positive for every zero; Weil's form evaluates at $\rho$; RH $\iff$ they agree. In the cutoff space an off-line zero
  is an **edge-localised vector** whose diagonal matrix elements are Poisson coefficients, not eigenvalue powers. Proved (§4).
- **L5 (correction of a statement made in chat on 2026-10-01).** Positivity is *not* lost in Connes's renormalisation. The
  counterterm $2f(1)\log'\Lambda$ is $\mathrm{Tr}(S_\Lambda V(f))$ for a projection $S_\Lambda$ dominating the cutoff projection
  ($Q'_{\Lambda,0}\le S_\Lambda$, `main.tex:2589`). So the renormalised trace is of positive type for every $\Lambda$ (`main.tex:2591-2600`). The hard
  input is the asymptotic identity (the trace formula (16), `main.tex:2500-2506`), which Connes could prove directly only for
  $h$ supported on $C_{k,1}$ (`main.tex:2508-2510`), even in function fields (§5).
- **L6 (the pole plane is the one permitted edge pair; $\Pi_1$).** Connes's two linear conditions $\mathcal S(\mathbb A)\to\mathbb C\oplus\mathbb C(1)$
  (`main.tex:964-967`) are the two constant terms of $\Theta$. RH $\iff-\mathrm{Loc}\ge0$ on the kernel of *one* of the two pole
  functionals. Under RH the local form has negative index exactly one. Proved (§6).
- **L7 (zero-free edge criterion, function fields).** With $C_N$ the Riemann–Roch cokernel of Connes's cutoff, RH for
  $L(\chi,\cdot)$ $\iff$ the degree shift leaks vanishing Hilbert–Schmidt mass out of $C_N$ $\iff$ $C_N$ carries vanishing weight on the
  window edges. The leakage operator has rank $\le3$, and its main term is the edge diagonal entry of the cokernel projection. Proved
  given Connes's description of $C_N$; multiplicities sketched (§7).
- **L8 (the archimedean blocker, sharpened).** For $\mathbb Q$ there is no exact Riemann–Roch at $\infty$: no nonzero $f$ has $f$ and $\hat f$
  both compactly supported (`main.tex:2746-2749`). The LPS plunge has width $\asymp\log\Lambda$ (`main.tex:2810-2814`), the same order as
  the main term $2\log'\Lambda$. So the $O(1)$ Weil term sits beneath an $O(\log\Lambda)$ transition layer, and the cokernel depends on
  where one cuts inside it. In edge language: the archimedean place supplies its own edge layer at exactly the location where
  off-line zeros would appear. Heuristic in part (§8).
- **L9 (group averages of theta are blind).** The torus average of $|\Theta(D_a v)|^2$ is $B_{1/2}$ (blind by L3). The full
  $\mathrm{Mp}_2$ average is the $L^2(\mathbb A)$ inner product (Schur), a product of local overlaps (blind by `obs:prime-by-prime-blind`).
  Connes's cutoff pair $(P_\Lambda,\hat P_\Lambda)$ is the one structure that uses the Weyl element without averaging, and that is where
  everything nontrivial lives. Sketched (§9).
- **L10 (a two-period metric).** RH $\iff E=\Xi+i\Xi'$ is Hermite–Biehler $\iff$ the Wronskian kernel
  $K(w,z)=\big(\Xi'(z)\overline{\Xi(w)}-\Xi(z)\overline{\Xi'(w)}\big)/(\pi(\bar w-z))$ is positive definite. Its real diagonal is the
  Laguerre inequality $\Xi'^2-\Xi\Xi''\ge0$. $\Xi$ and $\Xi'$ are the toric periods of $f_0$ and $(\log|x|)f_0$. Through de Branges's
  theorem, RH $\iff$ $\Xi$ is the corner entry of a positive $2\times2$ canonical system: a bond-dimension-two transfer matrix. Proved (the
  HB equivalence) / cited (de Branges, not byte-cited) / heuristic (the bond reading) (§10).
- **L11 (positivity-free route).** CCM window polynomials are real-rooted unconditionally. Even real-rooted polynomials $P$ satisfy
  $|P(z)|\le P(0)e^{\sigma_2|z|^2/2}$. Hence RH follows if $\sigma_2$ stays bounded and $\sigma_{2k}\to\sigma_{2k}(\Xi)$ for every $k\ge2$. The window
  $\sigma_2$ is one linear functional of the ground state. The ground state is, to overlap $1-6\cdot10^{-6}$, the truncated theta orbit
  function, which lies in the radical of $Z$ unconditionally. Proved (lemma, corollary, identity) / numerical (overlap) (§11).
- **L12 (N1, the calibration; §13).** In every genus the trivial-character Riemann–Roch cokernel of Connes's cutoff is the solution space of
  the order-$2g$ recurrence with characteristic roots the Frobenius eigenvalues: an MPS of bond dimension $2g$ with transfer matrix the
  Frobenius companion matrix, derived from $h^0$ data alone. For genus one its invariant similitude form is the Casoratian
  $Y_j^2-aY_jY_{j-1}+qY_{j-1}^2=\deg(m-nF)$. RH (Hasse) is positivity of that form. The single input missing from the bond is that this form is
  a count of kernel points on $E[n]$ (Weil pairing, Mumford's Heisenberg group). For $\mathbb Q$ the analogue of the form is the Wronskian kernel of
  L10. Proved (cokernel, Casoratian, equivalence) / cited, standard (degree identification).
- **L13 (N1′; §14).** The cokernel is the dual of the Frobenius algebra $\mathbb R[F]$, and its natural similitude metric is the Rosati form
  $\mathcal T(\varphi,\varphi)=\sum_i\varphi(\alpha_i)\varphi(q/\alpha_i)$. Positivity on $\mathbb R[F]$ is RH in every genus, with no tower (correcting §13), and it comes from
  the ampleness of $\Theta$. Exact dictionary: $\mathbb R[F]\leftrightarrow$ test algebra, Rosati $\leftrightarrow h\mapsto\tilde h$, $\mathcal T\leftrightarrow$ Weil's $Z$, Lefschetz $\leftrightarrow$
  explicit formula, and Hodge index $\leftrightarrow\Pi_1$, so the pole plane is the plane of the two fibre classes. For $\mathbb Q$ the blocker is a polarisation,
  not a tower.
- **The core blocker, restated.** The bond determines what is null in the Weil form (the theta orbit, §11.3) and its one negative
  direction (the pole plane, §6). Its own norms see only the harmonic-measure (Poisson) form (§§3–4). What remains is to show that the
  cutoff cokernel has no edge content beyond the pole plane: in function fields that is equivalent to RH and is supplied in Weil's proof by the
  polarisation of the theta divisor; for $\mathbb Q$ it is entangled with the archimedean plunge layer (§8).

---------------------------------------------------------------------------------------------------------------------

## 1. The bond's positivity: weighted orbit norms

Bond: $\mathcal S(\mathbb A)$ with the Schrödinger representation of $H(\mathbb A)$ and the Weil representation of $\mathrm{Mp}_2(\mathbb A)$.
$\Theta=\sum_{q\in\mathbb Q}\delta_q$ is fixed by $W(\mathbb Q^2)$ (a discrete, cocompact, self-dual Lagrangian: an adelic GKP state) and
by $\mathrm{SL}_2(\mathbb Q)$. $f_0=e^{-\pi y^2}\otimes1_{\hat{\mathbb Z}}$ is the vacuum. Dilations $D_af(y)=|a|^{1/2}f(ay)$. Connes's orbit map
(`main.tex:2549-2552`, his (18)):
$$Ef(a)=|a|^{1/2}\sum_{q\in\mathbb Q^\times}f(qa)=|a|^{1/2}\big(\langle\Theta,f(a\,\cdot)\rangle-f(0)\big).$$
For $f\in\mathcal S(\mathbb A)_0=\{f(0)=\hat f(0)=0\}$, $Ef$ is rapidly decreasing at both ends of $C_{\mathbb Q}$: at $|a|\to\infty$ directly, at
$|a|\to0$ by Poisson summation (not byte-cited; standard). Its Mellin transform is Tate's integral,
$\int Ef(a)|a|^{s-1/2}d^\times a=Z(f,s)$, entire in $s$.

**Theorem 1 (weighted orbit norms; proved here).** For $f\in\mathcal S(\mathbb A)_0$ and $\sigma\in\mathbb R$ put
$B_\sigma(f)=\int_{C_{\mathbb Q}}|Ef(a)|^2|a|^{2\sigma-1}d^\times a$. Then:

1. $B_\sigma(f)=\frac1{2\pi}\int_{\mathbb R}|Z(f,\sigma+it)|^2dt<\infty$;
2. $\sigma\mapsto\log B_\sigma(f)$ is convex;
3. $B_\sigma(\hat f)=B_{1-\sigma}(f)$;
4. if $\hat f=f$, then $B_\sigma(f)$ is minimal at $\sigma=\frac12$ and non-decreasing on $[\frac12,\infty)$.

*Proof.*
1. This is Mellin–Plancherel applied to $Ef(a)|a|^{\sigma-1/2}$.
2. For $\sigma=\theta\sigma_1+(1-\theta)\sigma_2$, Hölder with exponents $1/\theta$, $1/(1-\theta)$ applied to
   $|Ef|^{2\theta}|a|^{\theta(2\sigma_1-1)}\cdot|Ef|^{2(1-\theta)}|a|^{(1-\theta)(2\sigma_2-1)}$ gives
   $B_\sigma\le B_{\sigma_1}^\theta B_{\sigma_2}^{1-\theta}$.
3. Poisson summation for $x\mapsto f(x/a)$ on $\mathbb A/\mathbb Q$ gives $\sum_{q\in\mathbb Q}\hat f(qa)=|a|^{-1}\sum_{q\in\mathbb Q}f(q/a)$. With
   $f(0)=\hat f(0)=0$ this is $E\hat f(a)=Ef(a^{-1})$. Substitute $b=a^{-1}$.
4. A convex function symmetric about $\frac12$ is minimal there and non-decreasing to the right. ∎

For unramified $f$, $Z(f,s)=\xi(s)F_f(s)$ with $F_f$ entire (the local factors divided by $\Gamma_{\mathbb R}$, and the factor $s(s-1)$
absorbed by the two vanishing conditions). So item 4 says: $t\mapsto|\xi F_f|^2(\sigma+it)$ has $t$-integral non-decreasing in $\sigma\ge\frac12$.

## 2. RH as pointwise monotonicity (the Herglotz criterion)

**Proposition 2 (proved here).** The following are equivalent:

- (i) RH;
- (ii) $\mathrm{Re}\,\frac{\xi'}{\xi}(\sigma+it)>0$ for all $\sigma>\frac12$, $t\in\mathbb R$;
- (iii) for every $t$, $\sigma\mapsto|\xi(\sigma+it)|$ is strictly increasing on $[\frac12,\infty)$.

Equivalently, $z\mapsto i\frac{\xi'}{\xi}(\frac12-iz)$ is a Nevanlinna function on the upper half-plane.

*Proof.* Hadamard, with the zeros grouped in conjugate pairs: $\mathrm{Re}\frac{\xi'}{\xi}(s)=\sum_\rho\frac{\sigma-\beta}{(\sigma-\beta)^2+(t-\gamma)^2}$, and
$\partial_\sigma\log|\xi|=\mathrm{Re}\,\xi'/\xi$ gives (ii)$\iff$(iii).

- (i)$\Rightarrow$(ii): every term equals $(\sigma-\frac12)/|s-\rho|^2>0$.
- (ii)$\Rightarrow$(i): if $\beta_0>\frac12$, then along $t=\gamma_0$, $\sigma\uparrow\beta_0$ the term $1/(s-\rho_0)$ dominates. Its real part
  $(\sigma-\beta_0)/|s-\rho_0|^2\to-\infty$ at points with $\sigma>\frac12$. ∎

The statement is classical (Lagarias 1999; Sondow–Dumitrescu 2010; neither byte-cited). The point recorded here is its
relation to Theorem 1. With $f$ unramified and Fourier-even, Theorem 1.4 is
$$\int\partial_\sigma\big(|\xi(\sigma+it)|^2|F_f(\sigma+it)|^2\big)dt\ \ge\ 0\quad(\sigma\ge\tfrac12),$$
and RH is the same inequality without the $t$-integral and without $F_f$. The bond proves the averaged statement.

## 3. Blindness of vertical-line norms

**Theorem 3 (proved here).** Let $G$ be entire with $\int|G(\sigma+it)|^2dt<\infty$ for every $\sigma$, locally uniformly in $\sigma$, and
$G(\sigma+it)\to0$ as $|t|\to\infty$ uniformly for $\sigma$ in compacts. Then $\sigma\mapsto\log\int|G(\sigma+it)|^2dt$ is convex. If moreover $\overline{G(1-\bar s)}=G(s)$, the integral is non-decreasing on $[\frac12,\infty)$.

*Proof.* Under the hypotheses, $g(x)=\frac1{2\pi i}\int_{(\sigma)}G(s)x^{-s}ds$ is independent of $\sigma$ (contour shift). By Plancherel,
$\int|G(\sigma+it)|^2dt=2\pi\int|g|^2x^{-2\sigma}d^\times x$. Then argue as in Theorem 1. ∎

**Consequence.** Let $\xi_*$ be any entire function with the functional equation and reality of $\xi$, the same growth, and an off-line
quadruple of zeros. Replacing $\xi$ by $\xi_*$ in $Z(f,s)=\xi F_f$ leaves every conclusion of Theorem 1 intact. So **no inequality among the
$B_\sigma$, or among any vertical-line norms of the orbit transforms, separates $\xi$ from $\xi_*$.** This covers Connes's polynomial weights
(shard 04y, `thm:connes-norm-transported`), the energy/Hardy metric, and every exponential weight.

**Localisation cost (proved here).** Take an off-line pair $\rho_0=\frac12+\eta+i\gamma_0$, $1-\bar\rho_0$, with $|\xi(s)|\approx C|s-\rho_0||s-(1-\bar\rho_0)|$
locally. The best entire localiser in $t$ at width $\delta$ is $F(s)=e^{(s-s_0)^2/2\delta^2}$ with $s_0=\frac12+i\gamma_0$, for which
$|F(\sigma+it)|^2=e^{((\sigma-1/2)^2-\tau^2)/\delta^2}$, $\tau=t-\gamma_0$. For $\delta\ll\eta$:
$$\frac{B_{1/2+\eta}}{B_{1/2}}\approx\frac{e^{\eta^2/\delta^2}\cdot4\eta^2\cdot\sqrt\pi\delta^3/2}{\eta^4\cdot\sqrt\pi\delta}=2\Big(\frac\delta\eta\Big)^2e^{\eta^2/\delta^2}\ge2e.$$
The vertical growth $e^{\eta^2/\delta^2}$ that entire localisers must carry beats the gain $(\delta/\eta)^2$ from the zero, uniformly. This is the
quantitative content of L3, and the analytic reason `obs:prime-by-prime-blind` extends to every multiplier (Mellin-diagonal) construction.

## 4. The cutoff limit is the harmonic-measure form; off-line zeros are edge vectors

Cited (Connes, function fields; `main.tex:2644-2660`, Lemma 3): $\lim_\Lambda\Delta_\Lambda(f)=\sum_\rho N_\rho\int_{i\mathbb R}\hat f(\tilde\chi,z)\,d\mu_\rho(z)$,
where $\mu_\rho$ is the harmonic measure of $\rho$ with respect to the critical line, and it equals $\delta_\rho$ when $\rho$ is on the line.
Each $\mu_\rho$ is a positive probability measure. So $\Delta_\infty(f*f^*)=\sum_\rho N_\rho\int|\hat f|^2d\mu_\rho\ge0$ unconditionally. Weil's form
evaluates $\hat f$ at $\rho$. **RH $\iff\Delta_\infty$ equals the Weil distribution** (this is Connes's Theorem 5, b$\Rightarrow$a by Lemma 3,
a$\Rightarrow$b by positivity; `main.tex:2523-2560`). Connes calls the non-critical zeros "resonances" (`main.tex:2715-2717`).

**Proposition 4 (edge vectors; proved here).** On $\ell^2(\mathbb Z)$ with shift $(V\xi)_n=\xi_{n-1}$, let $\eta^{(N)}_z(n)=c_N\bar z^n$ on $[-N,N]$, normalised.
- If $|z|>1$, then $\langle\eta,V^k\eta\rangle\to w^k$ for $k\ge0$ and $\to\bar w^{|k|}$ for $k<0$, where $w=1/\bar z$.
- If $|z|=1$, then $\langle\eta,V^k\eta\rangle\to\bar z^{-k}$ for all $k$.

*Proof.* $\langle\eta,V^k\eta\rangle=c_N^2\bar z^{-k}\sum_n|z|^{2n}$ over $n\in[-N,N]\cap[-N+k,N+k]$, with $c_N^2\sim(1-|z|^{-2})|z|^{-2N}$. For $k\ge0$ the sum
keeps the top terms; for $k<0$ it loses the top $|k|$ terms, giving the factor $|z|^{2k}$, and $|z|^{2k}\bar z^{-k}=z^k$. ∎

The off-circle limits are the Fourier coefficients of the Poisson kernel at $w$, inside the disc. They form a positive-definite
sequence that decays in both directions. The "eigenvalue" reading $w^k$ for all $k$ would blow up for $k<0$. This is Connes's (29)
(`main.tex:2703-2707`). The mass of $\eta_z$ concentrates on the top edge ($|z|>1$) or the bottom edge ($|z|<1$) of the window.

**Reading.** In every cutoff of the bond, a critical zero is a bulk-extended exponential and an off-line zero is an edge mode. The
positive limit form sees an edge mode through its Poisson profile. RH is the absence of edge modes beyond those forced by the poles (§6).

## 5. Where Connes's argument actually needs input (correction L5)

Cited (`main.tex:2580-2600`): $E(B_{\Lambda,0})\subset S_\Lambda$, hence $Q'_{\Lambda,0}\le S_\Lambda$, hence
$\Delta_\Lambda(f)=\mathrm{Tr}\big((S_\Lambda-Q'_{\Lambda,0})V(f)\big)$ is of positive type for every $\Lambda$. And $\mathrm{Tr}(S_\Lambda V(f))=2f(1)\log'\Lambda$ (`main.tex:2612`). So
the counterterm is the trace of a projection that dominates the cutoff, and renormalisation preserves positivity. The pole plane
enters as the difference between $B_\Lambda$ and $B_{\Lambda,0}$ (`main.tex:2615-2616`).

What is not available is the asymptotic identity (16) (`main.tex:2500-2506`). "We can prove directly that (16) holds when $h$ is
supported by $C_{k,1}$ but are not able to prove (16) directly for arbitrary $h$" (`main.tex:2508-2510`). That is a statement about a
function field, where RH is Weil's theorem. **Even for curves, the bond route has not produced an independent proof.** That makes
function fields the calibration case (§12, N1).

Lemma 6 isolates what the asymptotic identity requires.

**Lemma 6 (compression of a unitary; proved here).** Let $U$ be unitary, $P$ an orthogonal projection of finite rank $d$, $T=PUP|_{\mathrm{ran}P}$,
$\ell=\|(1-P)UP\|_{HS}$ and $\ell_*=\|(1-P)U^*P\|_{HS}$. Then:

- (a) $k\mapsto\mathrm{Tr}(PU^k)$ is positive definite.
- (b) $|\mathrm{Tr}(PU^kP)-\mathrm{Tr}\,T^k|\le\frac{k(k-1)}2\,\ell\,\ell_*$ for $k\ge1$.
- (c) Every eigenvalue $\lambda$ of $T$ satisfies $1-|\lambda|^2\le\ell^2$.
- (d) $\ell^2=d-\|T\|_{HS}^2$.

*Proof.*
- (a) $\sum c_j\bar c_k\mathrm{Tr}(PU^{j-k})=\mathrm{Tr}(PXX^*)\ge0$ with $X=\sum c_jU^j$.
- (b) $PU^kP-T^k=\sum_{j=0}^{k-2}T^jPU(1-P)U^{k-1-j}P$. Telescoping gives $\|(1-P)U^mP\|_{HS}\le m\ell$, and $\|PU(1-P)\|_{HS}=\ell_*$.
- (c) On $\mathrm{ran}P$, $T^*T=P-PU^*(1-P)UP$. Hence $\prod_i|\lambda_i|^2=\det T^*T\ge1-\mathrm{Tr}(PU^*(1-P)UP)=1-\ell^2$, using $\prod(1-a_i)\ge1-\sum a_i$ for
  $a_i\in[0,1]$. Each $|\lambda_i|\le1$, so each $|\lambda_i|^2$ is at least the product.
- (d) Take the trace of the identity in (c). ∎

So the positive cutoff trace (a) equals the Lefschetz power trace $\mathrm{Tr}\,T^k$ up to $O(\ell\ell_*)$, and small leakage forces the compressed
spectrum onto the circle (c). The asymptotic trace formula and RH are both statements that the zero-cokernel is asymptotically invariant.

## 6. The pole plane and the $\Pi_1$ structure

**Proposition 7 (proved here).**

- (a) RH $\iff-\mathrm{Loc}\ge0$ on $\ker\ell_1=\{\hat h(1)=0\}$ $\iff-\mathrm{Loc}\ge0$ on $\ker\ell_0=\{\hat h(0)=0\}$.
- (b) Under RH, $-\mathrm{Loc}$ has negative index exactly $1$ on $C_c^\infty(\mathbb R_+^\times)$.

*Proof.*
- (a) If RH holds, $Z\ge0$; on $\ker\ell_1$ we have $P=0$, so $-\mathrm{Loc}=Z\ge0$. Conversely, positivity on $\ker\ell_1$ gives $Z\ge0$ on
  $\ker\ell_0\cap\ker\ell_1$, which is Weil's criterion. The same argument works for $\ker\ell_0$.
- (b) $-\mathrm{Loc}=Z-P$ with $Z\ge0$ and $P$ of signature $(1,1)$, so the negative index is at most 1. A witness gives at least 1: on the
  CCM window $x=13$, $N=20$, at 60 digits, $v_+^T(H-P)v_+=-5.836$ with data error below $10^{-50}$ (`checks/output.txt`, A3).
  The window vectors are trigonometric polynomials on $[0,L]$, in the domain of the window form of `def:ccm-tn-window-form`.
  Approximating them by $C_c^\infty$ test functions supported in the window keeps the value negative, by continuity of that form (sketch). ∎

The two pole functionals pair $h$ with the two constant terms of the theta orbit: the position zero-mode ($q=0$ term, $\delta_0$) and the
momentum zero-mode (its Fourier image, the constant $1$). The Weyl element exchanges them. This is Connes's
$0\to\mathcal S(\mathbb A)_0\to\mathcal S(\mathbb A)\to\mathbb C\oplus\mathbb C(1)\to0$ (`main.tex:964-967`) and the signs in his (34) (`main.tex:983-986`):
$\hat h(0)+\hat h(1)-\sum_{\rm crit}\hat h(\rho)$. In edge language (§4), the poles at $s=0,1$ have $|z|\neq1$: **the pole pair is the one
permitted pair of edge modes**, and $\Pi_1$ is its operator-theoretic shadow. The Heisenberg (additive) structure enters Tate's computation only
through Poisson summation. It supplies the functional equation and this rank-two piece, and nothing else.

Practical consequence: any positivity argument needs to cover only one Lagrangian hyperplane of the pole plane. For example, it suffices
to treat vectors with vanishing momentum zero-mode.

## 7. A zero-free edge criterion in function fields

Setting, cited from Connes (`main.tex:2523-2530` and the proof of Lemma 3, `main.tex:2664-2700`):
- $k$ is a function field over $\mathbb F_q$, $\chi$ a character of $C_{k,1}$ of ramification $f$, $\Lambda=q^N$.
- $S_{N,\chi}\cong\ell^2([-N,N])$ (degree window), $\dim=2N+1$.
- $E(B_{\Lambda,\chi})\subset S_{N,\chi}$ has codimension $d=2g-2+f$ for $\chi\ne1$ and large $N$.
- It is cut out by the conditions $\sum_n\xi(n)z^n=0$, $z\in F$, where $F\subset\mathbb C^*$ is the multiset attached to the zeros of
  $L(\chi,\cdot)$, with $|z|=1$ iff the zero is critical.

Write $C_N=S_{N,\chi}\ominus E(B_{\Lambda,\chi})$ (the **Riemann–Roch cokernel**) and $P_N$ for its projection. $P_N$ is built from
Riemann–Roch spaces alone: no zero enters its definition. Then $C_N=\mathrm{span}\{\eta^{(N)}_z:z\in F\}$ (for simple $F$).

**Theorem 8 (edge criterion; proved here for simple $F$ given the cited description, multiplicities sketched).** With $V$ the shift by a
degree-one idele, $\ell_N=\|(1-P_N)VP_N\|_{HS}$ and $\ell_{*N}=\|(1-P_N)V^*P_N\|_{HS}$, the following are equivalent:

- (i) RH for $L(\chi,\cdot)$;
- (ii) $\ell_N\to0$ and $\ell_{*N}\to0$;
- (iii) for every fixed $m$, the edge weight $\omega_N(m)=\sum_{N-m\le|n|\le N}(P_N)_{nn}\to0$.

*Proof.*
- (i)$\Rightarrow$(ii),(iii). Distinct unimodular $z$ give asymptotically orthonormal $\eta_z$ (the Gram entries are Dirichlet kernels over
  $2N+1$). Also $V\eta_z-\bar z^{-1}\eta_z$ has two entries of size $(2N+1)^{-1/2}$, so
  $\ell_N^2\le C\sum_z\|V\eta_z-\bar z^{-1}\eta_z\|^2=O(d/N)$; similarly for $\ell_{*N}$ and $\omega_N(m)=O(dm/N)$.
- not (i) $\Rightarrow$ not (ii). If some $|z|>1$, then $V\eta_z$ has the component $c_N\bar z^N e_{N+1}$, orthogonal to $S_N\supset C_N$, of squared modulus
  $\to1-|z|^{-2}$. So $\ell_N^2\ge1-|z|^{-2}-o(1)$. For $|z|<1$, use $V^*$ and the bottom edge.
- not (i) $\Rightarrow$ not (iii). The edge-localised vectors of $C_N$ restricted to an edge block of width $m\ge\#\{$off-circle $z\}$ form an
  asymptotically injective Vandermonde system, so $\omega_N(m)\ge c>0$. ∎

**Structure of the leakage (proved here).** For $c\in C_N$ and $w'\in W_{N-1}:=E(B_{\Lambda/q})$: covariance (`main.tex:2556`, his (19))
gives $VW_{N-1}\subset W_N:=E(B_\Lambda)$, and $W_{N-1}\subset W_N$. So $\langle Vc,Vw'\rangle=\langle c,w'\rangle=0$, i.e. $Vc\perp VW_{N-1}$. The
component of $Vc$ outside $C_N$ therefore lies in $\mathbb Ce_{N+1}\oplus(W_N\ominus VW_{N-1})$, a space of dimension $\le3$. **The leakage
operator has rank $\le3$, independent of $N$ and $g$**, and
$$\ell_N^2=(P_N)_{NN}+\sum_{w\in\mathrm{ONB}(W_N\ominus VW_{N-1})}\|P_NV^*w\|^2.$$
So RH for curves is governed by a bounded number of explicit Riemann–Roch quantities at the window edge. The leading one is the diagonal
entry $(P_N)_{NN}=1-\sup\{|w(N)|^2:w\in W_N,\|w\|=1\}$: RH $\iff$ the Riemann–Roch image contains unit vectors concentrated, asymptotically
entirely, on the top degree. Through $E(1_{\mathcal O(D)})(g)\propto|g|^{1/2}(q^{h^0(D+\mathrm{div}\,g)}-1)$ these are statements about $h^0$ of divisors
near the edge degree, i.e. about the special part of the class-group bond state of shard 04p (`prop:theta-functional-bond-state`).

For the trivial character, the pole vectors ($|z|=q^{\pm1/2}$ in the normalised variable) are two explicit edge modes. Remove them first
(the analogue of $B_{\Lambda,0}$, §6). With them kept, the limit of $(P_N)_{NN}$ is the pole contribution, and RH says it is no larger.

**A negative finding recorded.** The transfer maps between successive cokernels, $M_N=P_{S_N}V^*|_{C_{N+1}}:C_{N+1}\to C_N$, are
asymptotically unitary *whether or not* RH holds. Indeed $P_{S_N}V^*\eta^{(N+1)}_z=(c_{N+1}/c_N)\bar z\,\eta^{(N)}_z$ exactly, and the
normalisation ratio tends to $|z|^{-1}$ off the circle, so the factor is unimodular. Growing windows absorb the growth. **RH is visible in the
fixed-window compression, not in the cokernel bundle.**

## 8. The archimedean blocker for $\mathbb Q$

Cited: "when $v$ is an Archimedian place there exists no non-zero function on $k_v$ which vanishes as well as its Fourier transform
for $|x|>\Lambda$" (`main.tex:2746-2749`). Connes substitutes the Landau–Pollak–Slepian prolate subspace: the eigenvalues of
$P_\Lambda\hat P_\Lambda P_\Lambda$ "are decreasing very slowly from $\lambda_0\simeq1$ until the value $n\simeq4\Lambda^2$ of the index $n$, they then
decrease from $\simeq1$ to $\simeq0$ in an interval of length $\simeq\log(\Lambda)$" (`main.tex:2810-2814`). He takes $B_\Lambda=\mathrm{span}\{\psi_n:n\le4\Lambda^2\}\otimes1_{\hat{\mathbb Z}}$
and asserts the analogues of Lemma 1, Theorem 5 and Lemma 3 (`main.tex:2814-2833`).

Analytic consequences:

1. **Order count.** The plunge layer contains $\asymp\log\Lambda$ states. The main term is $2\log'\Lambda$ and the Weil term is $O(1)$. A
   cutoff that is sharp to $o(1)$ in the trace must resolve the plunge layer to relative accuracy $o(1/\log\Lambda)$. Function fields have no
   plunge layer: Riemann–Roch is exact.
2. **Cut dependence.** Moving the cut index by $m$ inside the plunge changes $\mathrm{Tr}(Q_\Lambda U(h))$ by $\sum_{\text{moved}}\langle\psi_n,U(h)\psi_n\rangle$,
   which is $O(m)$ unless these matrix elements cancel. The $O(1)$ term of the trace formula is therefore not determined by the leading
   asymptotics. It depends on a choice of order $\log\Lambda$ states.
3. **Edge reading (heuristic, not checked).** Semiclassically, the plunge states sit near the corners of the time–frequency box,
   $|x|\approx\Lambda$, $|p|\approx\Lambda$. In the dilation variable $\log|x|$ this is the window edge. So the archimedean place contributes its
   own $O(\log\Lambda)$-dimensional edge layer at exactly the location where §§4 and 7 detect off-line zeros. In function fields the edge
   content of the cokernel is the pole plane plus nothing (under RH). For $\mathbb Q$ the target statement is: **the edge content of the global
   cutoff cokernel equals the archimedean plunge content plus the pole plane, with no excess.**
4. The semi-local trace formula (Connes's Theorem 4, `main.tex:1893-1906`, proved for finite $S$) says this local–global additivity holds
   for every finite set of places. The global step is the open one. In edge language, it is an additivity of edge content over places that
   must survive the infinite product.

Status: 1 and 2 are elementary consequences of the cited LPS facts. 3 is heuristic and needs the LPS corner-localisation statement checked
against a source. 4 is a reformulation.

## 9. Group averages of the theta vector are blind (sketched)

- **Torus average.** $\int_{C_{\mathbb Q}}|\langle\Theta,D_av\rangle-\text{(constant terms)}|^2d^\times a=B_{1/2}(v)$: Theorem 1, blind by Theorem 3.
- **Full average.** The even Weil representation of $\mathrm{Mp}_2(\mathbb A)$ is irreducible (restricted tensor product of irreducible local even
  Weil representations; not byte-cited), and $f\mapsto\theta_f$ is an intertwiner into $L^2(\mathrm{Mp}_2(\mathbb Q)\backslash\mathrm{Mp}_2(\mathbb A))$. By Schur,
  $\langle\theta_f,\theta_{f'}\rangle_{\rm Pet}=c\langle f,f'\rangle_{L^2(\mathbb A)}$. On dilation orbits of $f_0$ this is $\langle f_0,D_af_0\rangle$, a product of local
  overlaps, and blind by `obs:prime-by-prime-blind`.

So positive forms of the shape "average of $|\text{matrix coefficient of }\Theta|^2$ over a subgroup" are RH-blind in both extreme cases.
Connes's cutoff pair $(P_\Lambda,\hat P_\Lambda=FP_\Lambda F^{-1})$ uses the Weyl element $F$ without averaging, so it is not Mellin-diagonal. It is
the one structure on the bond that escapes Theorem 3, and §§5–8 show that everything nontrivial happens there. The "escape route" proposed in chat
on 2026-10-01 (non-Mellin-diagonal Heisenberg operators) is therefore Connes's programme, not a new one.

## 10. A two-period metric and canonical systems

**Proposition 9 (proved here).** RH $\iff E:=\Xi+i\Xi'$ is Hermite–Biehler ($|E(\bar z)|<|E(z)|$ for $\mathrm{Im}\,z>0$). In that case the de Branges
kernel is
$$K(w,z)=\frac{\Xi'(z)\overline{\Xi(w)}-\Xi(z)\overline{\Xi'(w)}}{\pi(\bar w-z)},\qquad K(x,x)=\frac{\Xi'(x)^2-\Xi(x)\Xi''(x)}{\pi}\ (x\in\mathbb R).$$

*Proof.*
- ($\Rightarrow$) Under RH, $\Xi(z)=\Xi(0)\prod(1-z^2/\gamma^2)$, so $w=\Xi'/\Xi=\sum_\gamma(z-\gamma)^{-1}$ has $\mathrm{Im}\,w<0$ on $\mathrm{Im}\,z>0$. Then
  $|E|^2-|E^\#|^2=|\Xi|^2(|1+iw|^2-|1-iw|^2)=-4|\Xi|^2\mathrm{Im}\,w>0$.
- ($\Leftarrow$) If $E$ is HB then $\Xi=(E+E^\#)/2$ has only real zeros: at a zero, $|E(z)|=|E^\#(z)|$, which forces $z$ real.
- The kernel is the standard $\big(E(z)\overline{E(w)}-E^\#(z)\overline{E^\#(w)}\big)/(2\pi i(\bar w-z))$ expanded. ∎

The real diagonal $K(x,x)\ge0$ is the Laguerre inequality, which is necessary only. Positivity on the complex diagonal is Proposition 2(ii)
rotated, and full positive definiteness follows from HB (de Branges; not byte-cited).

**Bond reading.** $\Xi$ is the toric period of $f_0$. $\Xi'$ is the toric period of $(\log|x|)f_0$, since $\partial_s$ under Mellin is multiplication by
$\log|x|$. **The candidate metric is the Wronskian of two theta periods.** Any pair $(f,g)$ in the bond whose periods $(A,B)$ form an HB pair
$A-iB$ forces RH (all zeros of $A$ real). Conversely, RH makes $(f_0,(\log|x|)f_0)$ such a pair. So RH $\iff$ some pair of bond vectors has
HB periods. The de Branges translate spaces of `thm:symbol-edge-quotient` are other choices of the second vector.

**Canonical systems (cited, not byte-cited: de Branges's inverse theorem).** Every HB function, suitably normalised, is the endpoint of a
canonical system $y'=zJH(t)y$ with $H(t)\ge0$ a $2\times2$ Hamiltonian. So RH $\iff\Xi$ is the corner entry of the endpoint transfer matrix of a
positive $2\times2$ canonical system: a **bond-dimension-two transfer matrix with positive generator**.

*Heuristic only.* The dilation in the Weil representation is $\exp(t\,\mathrm{diag}(1,-1))=\exp(tJH_0)$ with $H_0=J^{-1}\mathrm{diag}(1,-1)$ indefinite:
a hyperbolic, indefinite "canonical system". A positive system has $\det H\ge0$, i.e. an elliptic or parabolic generator. This is the
hyperbolic-versus-elliptic gap of the chat discussion: no flow-invariant positive complex structure exists at any place where the flow acts,
because $\tau\mapsto a^2\tau$ has no fixed point in the Siegel half-plane and a hyperbolic element fixes no vertex of the Bruhat–Tits tree. Read
this way, RH asks for a $t$-dependent gauge that turns the bond's indefinite dilation system into a positive one. The variables of
the two systems (dilation time versus de Branges time, Mellin versus de Branges spectral parameter) have not been matched. Do not cite this
paragraph as anything but a direction.

## 11. The positivity-free route (Hurwitz/Laguerre–Pólya) and the theta radical

**Lemma 10 (Laguerre–Pólya growth; proved here).** Let $p$ be an even polynomial with real roots $x_j\ne0$ and $\sigma_2=\sum_jx_j^{-2}$. Then
$|p(z)|\le p(0)e^{\sigma_2|z|^2/2}$.

*Proof.* $|1-w|^2=1-2\mathrm{Re}\,w+|w|^2\le e^{-2\mathrm{Re}\,w+|w|^2}$. Sum $\log|1-z/x_j|\le-\mathrm{Re}(z/x_j)+|z|^2/(2x_j^2)$ over roots; the linear terms
cancel in $\pm$ pairs. ∎

**Corollary 11 (proved here).** Let $P_n$ be even real-rooted polynomials (in the frequency variable), $P_n(0)\to\Xi(0)$, with $\sup_n\sigma_2(P_n)<\infty$
and $\sigma_{2k}(P_n)\to\sigma_{2k}(\Xi):=-2k\,[t^{2k}]\log\Xi$ for every $k\ge2$. Then RH holds.

*Proof.* Lemma 10 and Montel give normality. A subsequential limit $G$ has only real zeros (Hurwitz) and $\log G-\log\Xi=ct^2$ near $0$.
Hence $G=\Xi e^{ct^2}$ and the zeros coincide. ∎

The targets $\sigma_{2k}(\Xi)$ come from the Taylor series of $\log\xi$ at $\frac12$: no zeros are used. The CCM window polynomials
$P_N(s)=\sum_j\xi_j\prod_{k\ne j}(k-s)$ are real-rooted unconditionally (`thm:ccm-tn-loewner-quotient`; the metric $T=Q_N-\varepsilon I\ge0$ is
manufactured by the spectral shift). For even ground states $\xi$ (proved here by expanding $\log P_N$):
$$\sigma_2(\text{window})=\Big(\frac L{2\pi}\Big)^2\Big[2\sum_{j=1}^Nj^{-2}+\frac4{\xi_0}\sum_{j=1}^N\xi_j\,j^{-2}\Big].$$
This is one linear functional of the ground state. Its two terms grow like $L^2$ and must cancel; at $x=13$, $N=20$ they are $+0.532$ and $-0.502$.

**The theta radical (proved here).** Riemann's $\Phi$ is the theta orbit function with both constant terms (the pole plane) removed by a
second-order Euler operator. In the variable $y$ of `prop:riemann-theta-dilation-bond`, $\mathcal D=y\,d/dy$ kills $1$, $2\mathcal D+1$ kills $y^{-1/2}$, and
$\mathcal D(2\mathcal D+1)$ multiplies the Mellin transform by a multiple of $s(s-1)$. This turns $4\xi(s)/(s(s-1))$ into a multiple of $\xi$, whose
restriction to the critical line is $\Xi$. For every $k$, $\widehat{\Phi*k}=\Xi\hat k$
vanishes at every zero, on or off the line. So **$\Phi*C_c^\infty\subset\mathrm{rad}\,Z$ unconditionally.** Since the theta orbit is dense in the bond
(`thm:theta-vector-cyclic`), $Z$ is a form on the quotient by a dense subspace and inherits no metric from $L^2$. The jets $\Phi^{(m)}$
($\widehat{\ }=(it)^m\Xi$) are further radical elements. Heuristically, they account for the ladder of near-null window eigenvalues
($4.9\cdot10^{-48},1.2\cdot10^{-44},1.6\cdot10^{-41},\dots$ at $x=13$, $N=30$), and they rule out any spectral-gap (Davis–Kahan) argument for the
ground state.

Numerics (`checks/output.txt`; reviewer's window helpers; no zeros used except in the labelled comparison table):
- $\sigma_4,\sigma_6,\sigma_8$ converge to $\sigma_{2k}(\Xi)$ with relative errors $1.7\cdot10^{-3}$, $1.2\cdot10^{-5}$, $9.5\cdot10^{-8}$ at $x=13$, $N=56$.
- $\sigma_2$ stays below $\sigma_2(\Xi)=0.04621$. The deficit tracks the Riemann–von Mangoldt tail above the frequency cutoff $2\pi N/L$
  ($0.0090$ against $0.0095$).
- All $2N$ roots are real; at $x=13$, $N=30$ the first zero is reproduced to $1.6\cdot10^{-39}$, and unresolved roots escape upward.
- The ground state has overlap $1-6.4\cdot10^{-6}$ with the sampled $(-1)^j\Xi(2\pi j/L)$ at $x=13$, $N=20$ (Rayleigh quotient
  $3.3\cdot10^{-28}$ against $\lambda_{\min}=1.6\cdot10^{-39}$).

## 12. Next analytic steps, in order

- **N1 (calibration: a bond proof of RH for an elliptic curve).** Take a genus-one function field with a ramified class character (so $d=f$),
  or the trivial character with the pole vectors removed. Write $(P_N)_{NN}$ and the two other leakage terms of §7 through $h^0$ of divisors
  near the edge degree. Try to prove $\ell_N\to0$ from Riemann–Roch plus one geometric input. Then identify that input: it should be the
  polarisation of the theta divisor (Rosati / Hodge index), and the place where it enters is the place where $\mathbb Q$ needs a substitute. This
  is the cleanest test of whether the bond can carry a proof at all. Connes did not have one (§5).
- **N2 ($\mathbb Q$: edge content).** Define the weighted edge content $\mathrm{Tr}(P^{\rm coker}_\Lambda1_{\rm edge}V(h)V(h)^*)$ with the LPS cut. Compute the
  archimedean contribution exactly: Connes's Theorem 3 is local and proved, `main.tex:1408-1418`. Formulate RH as additivity of edge content
  over places plus the pole plane (§8.3–4). First check the LPS corner-localisation statement against a source.
- **N3 (exits).** Compare the leakage operator of §7 (rank $\le3$) with the notebook's exits: `lem:exit-one-dimensional`,
  `thm:arithmetic-metric` ("one exit per zero mode"), `prop:two-exits-two-metrics`. The rank bound suggests that the arithmetic exits
  are a fixed small number per window edge, not one per mode.
- **N4 (two-period metric).** Search for a pair $(f,g)$ in the bond, other than $(f_0,(\log|x|)f_0)$, whose period pair is HB for a structural
  reason (a positivity of the toric period of $f+ig$). Test the canonical-system reading on the genus-one class-group bond, where RH is known.

Dead ends recorded by this investigation:
- vertical-line norms of orbit transforms (Theorem 3);
- subgroup averages of $|\Theta|^2$ (§9);
- transfer maps between growing cutoff cokernels (§7, negative finding);
- Davis–Kahan around the theta vector (§11, radical ladder).

---------------------------------------------------------------------------------------------------------------------

## 13. N1 carried out: the Riemann–Roch cokernel is the Frobenius transfer matrix; for genus one the metric is the degree form

Added 2026-10-01, the same session (TJO: "go for it" on N1). Everything below is **proved here** unless marked.

Setting. $k$ is the function field of a smooth projective curve $C/\mathbb F_q$ of genus $g$ with class number $h$. We work in the
units-invariant, trivial-character sector: functions on $C_k$ that depend only on the degree. Write $m=\log_q|g|$, so $S_N=\ell^2([-N,N])$. Let
$a_n$ be the number of effective divisors of degree $n$, so $Z(T)=\sum a_nT^n=P(T)/((1-T)(1-qT))$ with $P(T)=\prod_{i=1}^{2g}(1-\alpha_iT)$
(`prop:class-group-bond`). Let $K$ be a canonical divisor and choose $\psi$ with conductor $K$, so that $\widehat{1_{\mathcal O(D)}}=q^{\deg D+1-g}1_{\mathcal O(K-D)}$
(Tate; not byte-cited).

**Step 1 (the orbit transform of a divisor lattice).** For $f=1_{\mathcal O(D)}$ with $\deg D=j$, Connes's $Ef(g)=|g|^{1/2}\sum_{a\in k^\times}f(ag)$ counts
$a\in L(D+\mathrm{div}\,g)\setminus0$, so $Ef(g)=|g|^{1/2}(q^{\ell(D+\mathrm{div}\,g)}-1)$. Averaged over the $\mathrm{Pic}^0$-fibre of fixed degree (the trivial-character
projection),
$$E1_{\mathcal O(D)}(m)=q^{m/2}\,A(j-m),\qquad A(n)=\frac1h\sum_{c\in\mathrm{Pic}^n}(q^{\ell(c)}-1)=\frac{q-1}h\,a_n .$$
So **the cutoff kernel of the bond is the effective-divisor generating function**: $\sum_nA(n)z^n=\frac{q-1}hZ(z)$.

**Step 2 (the cutoff image).** Take $f=\sum_jc_j1_{\mathcal O(jP_0)}$ with $j\in[2g-2-N,N]$. This range is exactly the condition that $f$ and $\hat f$ are supported in
$|x|\le q^N$. Impose $f(0)=\sum c_j=0$ and $\hat f(0)\propto\sum c_jq^j=0$ (the pole plane, §6).
- For $m<-N$, the Riemann–Roch value $A(n)=q^{n+1-g}-1$ ($n>2g-2$) and the two conditions give $Ef(m)=0$. For $m>N$, $A(j-m)=0$. So
  $Ef\in S_N$.
- These $f$ span a space of dimension $2N-2g+1$, of codimension $2g$ in $S_N$. The map $c\mapsto Ef$ is injective: it is triangular, with
  diagonal entries $A(0)=(q-1)/h\ne0$. Connes's conditions (28) (`main.tex:2674-2684`, stated there for $\chi\ne1$; the
  necessity part, via his Appendix 1 Lemma 3, does not depend on the character, so it applies here with the pole plane removed; sketch) give codimension at least $2g$. Hence **this family is all of $E(B_{q^N,0})$ in this sector.**

**Theorem 12 (the cokernel; all genera).** Put $Y(m)=\overline{y(m)}\,q^{m/2}$. Then $y\in C_N:=S_N\ominus E(B_{q^N,0})$ if and only if
$$\sum_{i=0}^{2g}p_i\,Y(j-i)=0\qquad\text{for all }j\in[2g-N,\,N],\qquad P(T)=\sum_{i=0}^{2g}p_iT^i .$$
That is, the cutoff cokernel is the full solution space, on the window, of the order-$2g$ linear recurrence whose characteristic roots are the
Frobenius eigenvalues $\alpha_i$. Equivalently, $Y(m)=\langle l|M^m|r\rangle$ with $M$ the companion matrix of $\prod(\lambda-\alpha_i)$. **The cokernel is an
MPS of bond dimension $2g$ whose transfer matrix is the Frobenius companion matrix.**

*Proof.* $y\perp Ef$ for all admissible $c$ means: $T(j):=\sum_mY(m)A(j-m)$ lies in $\mathrm{span}\{1,q^j\}$ on $j\in[2g-2-N,N]$. In generating functions,
$$(1-z)(1-qz)\,\hat T(z)=\tfrac{q-1}h\,P(z)\,\hat Y(z).$$
$(1-z)(1-qz)$ annihilates $\alpha+\beta q^j$, so the coefficients of $P\hat Y$ must vanish for $j\in[2g-N,N]$. Each such coefficient involves only
$Y(j-2g),\dots,Y(j)$, all inside the window. That gives $2N-2g+1$ independent equations on $2N+1$ unknowns, so the solution space has dimension
$2g=\operatorname{codim}$. ∎

Remarks.
- No zero was used. $P$ enters only through $Z(T)$, i.e. through $h^0$ of divisors: the special part of the class-group bond state of
  shard 04p.
- This derives Connes's description ($C_N=\mathrm{span}\,\eta_z$, $z=\bar\alpha_i/\sqrt q$) from Riemann–Roch for the trivial character.
- The edge criterion of Theorem 8 becomes: **RH for $C$ $\iff$ $M/\sqrt q$ has all eigenvalues on the unit circle.** An eigenvalue with $|\alpha|>\sqrt q$ is a
  top-edge mode; its partner $q/\bar\alpha$ is a bottom-edge mode.

**Corollary 13 (genus one: the metric is the degree form).** Let $g=1$ and $a=q+1-h$, so the recurrence is $Y_j=aY_{j-1}-qY_{j-2}$. Define the
Casoratian form
$$\mathcal Q(Y_j,Y_{j-1})=Y_j^2-aY_jY_{j-1}+qY_{j-1}^2 .$$
Then:
1. **Similitude.** $\mathcal Q(Y_{j+1},Y_j)=q\,\mathcal Q(Y_j,Y_{j-1})$ along every solution. Equivalently,
   $\mathcal Q(Y_j,Y_{j-1})=q\,(Y_{j-1}^2-Y_jY_{j-2})$, a discrete Turán/Laguerre expression.
2. **Positivity.** $\mathcal Q$ is positive semidefinite $\iff a^2\le4q\iff$ the cokernel has no edge modes $\iff$ RH for $C$ (Hasse's bound).
3. **Identification.** $\mathcal Q(m,n)=m^2-amn+qn^2=\deg(m-nF)$ on $\mathbb Z[F]\subset\mathrm{End}(E)$ (standard; not byte-cited): the degree is the
   determinant of $m-nF$ on the Tate module. Positivity is "degree $\ge0$". For separable $m-nF$ this is $\#\ker(m-nF)\ge0$, and homogeneity and
   density then give $\mathcal Q\ge0$ on $\mathbb R^2$.

*Proof.* (1) Substitute $Y_j=aY_{j-1}-qY_{j-2}$ twice. (2) A binary form with positive leading coefficient is semidefinite iff its discriminant
$a^2-4q\le0$. When $a^2<4q$ the roots of $\lambda^2-a\lambda+q$ are conjugate with product $q$, so of modulus $\sqrt q$. When $a^2=4q$ there is a double root
$\pm\sqrt q$, with jets but no edge mode. When $a^2>4q$ the real roots satisfy $|\alpha_1|>\sqrt q>|\alpha_2|$. ∎

**Calibration verdict.**
- The adelic bond plus Riemann–Roch on $C$ yields the cokernel, the transfer matrix $M$, and the *formula* of the invariant metric, namely the
  Casoratian $\mathcal Q$.
- It does not yield positivity. The "fake curve" $q=2$, $h=6$ (`obs:gl1-bond-no-metric`) is consistent with every Riemann–Roch input used here,
  and gives $\mathcal Q(m,n)=m^2+3mn+2n^2$ with $\mathcal Q(-3,2)=-1$: "an isogeny of degree $-1$". Its cokernel has edge weight $\to1-\alpha_2^2/q=\frac12$ at
  each edge.
- **The one missing input is: the Casoratian of the bond's Frobenius transfer matrix is a degree, i.e. a count.** That count lives on the
  torsion $E[n]$ over $\overline{\mathbb F}_q$. There the Weil pairing, the commutator form of Mumford's finite Heisenberg group, has multiplier
  $\deg\varphi$ under $\varphi$. This is the "second Heisenberg group" of the chat discussion, now pinned down. It is not on the adelic bond over
  $\mathbb F_q$: the bond sees $\mathrm{tr}F$ through $h$, and it sees $\det F=q$, but it does not see $F$ as an endomorphism whose integer
  combinations have kernels to count.
- For $g\ge2$ the similitude forms of $M$ form a cone (`thm:arithmetic-metric`, `prop:hp-inner-product-discrete`). *Corrected in §14:* the
  earlier sentence here, that Weil's Rosati form bounds only traces and so needs the tower $r\to\infty$, holds only if the form is restricted to
  $\mathbb Z+\mathbb ZF$. On all of $\mathbb R[F]$ the Rosati form gives RH directly, in every genus, with no tower.

**What this says for $\mathbb Q$ (direction, not a result).**
- The analogue of Theorem 12 is that the cutoff cokernel of the adelic bond is a cMPS whose generator has the zeros as spectrum. The
  LPS plunge (§8) replaces the exact window equations.
- The analogue of the Casoratian $\mathcal Q$ is the Wronskian kernel of Proposition 9, $K(w,z)\propto\big(\Xi'(z)\overline{\Xi(w)}-\Xi(z)\overline{\Xi'(w)}\big)/(\bar w-z)$. Its real
  diagonal $\Xi'^2-\Xi\Xi''$ is the continuous form of $Y_{j-1}^2-Y_jY_{j-2}$.
- So the genus-one calibration converts the $\mathbb Q$ question into: **find an arithmetic object whose "degree" (a positive count) is the
  de Branges–Wronskian kernel of $\Xi$.** This is the operator-side shadow of Connes–Consani's programme: "the Schwartz kernel of the
  scaling operator corresponds geometrically to the divisor of the Frobenius correspondence" (`refs/src/2006.13771/weil-compo.tex:151`), with an
  intersection theory "on the square of the Scaling Site" still "not yet in shape to handle the delicate principal values"
  (`:149`). What the present computation adds is the precise target: positivity of a two-point Casoratian/Wronskian form on the cokernel
  phase space, with the genus-one degree form as the model.

Next, refined:
- **N1′.** Genus two, on a curve with known $P$ (shard 04w): write the Rosati-form candidate on the four-dimensional cokernel phase space
  explicitly in the recurrence coordinates. Test whether a counting interpretation, $\deg$ of $m+nF+\ell V$ with $V$ the Verschiebung, survives without the tower.
- **N2′.** For $\mathbb Q$: compute the Wronskian kernel $K$ in the dilation variable as an explicit functional of the theta orbit (Proposition 9), and
  look for a count it equals on the prime-content windows of RTP rounds 1–2.


---------------------------------------------------------------------------------------------------------------------

## 14. N1′ (all genera): the cokernel metric is the Rosati form on $\mathbb R[F]$, the tower is not needed, and $\Pi_1$ is the Hodge-index signature

Added 2026-10-01, the same session (TJO: "go for it", i.e. continue). Statuses are marked per item.

**Proposition 14 (duality; proved here).** Let $\chi_F(\lambda)=\prod_i(\lambda-\alpha_i)$, with $\deg\chi_F=2g$. The solution space $C_N$ of Theorem 12 is
canonically the dual of $\mathbb R[\lambda]/(\chi_F)$: a solution is $Y(j)=\ell(\lambda^j)$ for a linear functional $\ell$. Under this identification the
window shift $M$ is the transpose of multiplication by $\lambda$. When $\chi_F$ is also the minimal polynomial of $F$ on $H^1$ (for instance, distinct
$\alpha_i$), $\mathbb R[\lambda]/(\chi_F)\cong\mathbb R[F]\subset\mathrm{End}(J)\otimes\mathbb R$. So **the cutoff cokernel of the bond is the dual of the Frobenius algebra
$\mathbb R[F]$, with the transfer matrix dual to multiplication by $F$.**

*Proof.* The recurrence of Theorem 12 says exactly that $\ell(\lambda^{j-2g}\chi_F(\lambda))=0$. Both spaces have dimension $2g$. ∎

**Proposition 15 (Rosati form; proved here, given Rosati positivity).** For $\varphi,\psi\in\mathbb R[F]$ put $\mathcal T(\varphi,\psi)=\mathrm{Tr}_{H^1}\big(\varphi(F)\,\psi(V)\big)$, with
$V=qF^{-1}$ (the Verschiebung, the Rosati dual of $F$). Then:
1. $\mathcal T(\varphi,\psi)=\sum_i\varphi(\alpha_i)\psi(q/\alpha_i)$, and $\mathcal T(F\varphi,F\psi)=q\,\mathcal T(\varphi,\psi)$: a similitude form for the transfer, with
   multiplier $q$.
2. $\mathcal T\ge0$ on $\mathbb R[F]$ $\iff$ every $|\alpha_i|=\sqrt q$ (RH for $C$).
3. For $g=1$, $\mathcal T(m-nF,m-nF)=2\deg(m-nF)$, which is twice the Casoratian of Corollary 13.

*Proof.*
1. The eigenvalues of $\varphi(F)\psi(V)$ are $\varphi(\alpha_i)\psi(q/\alpha_i)$, and $F\cdot V=q$.
2. ($\Leftarrow$) If $q/\alpha_i=\bar\alpha_i$, each term is $|\varphi(\alpha_i)|^2$.
   ($\Rightarrow$) The multiset $\{\alpha_i\}$ is closed under $\alpha\mapsto q/\alpha$ (functional equation) and under conjugation, unconditionally.
   - If $\alpha$ is real with $\alpha\ne\pm\sqrt q$: take a real interpolating $\varphi$ with $\varphi(\alpha)=1$, $\varphi(q/\alpha)=-1$, and $\varphi=0$ at the other
     eigenvalues. Then $\mathcal T(\varphi,\varphi)=-2\cdot\mathrm{mult}<0$.
   - If $\alpha$ is non-real with $|\alpha|\ne\sqrt q$: the four points $\alpha,\bar\alpha,q/\alpha,q/\bar\alpha$ are distinct. Take $\varphi$ real with $\varphi(\alpha)=1$,
     $\varphi(q/\alpha)=-1$, and $0$ elsewhere. Then $\mathcal T(\varphi,\varphi)=-4\cdot\mathrm{mult}<0$.
3. Here $q/\alpha_1=\alpha_2$. ∎

Rosati positivity, $\mathrm{Tr}(\varphi\varphi^\dagger)>0$ on $\mathrm{End}(J)\otimes\mathbb Q\setminus0$ and so $\ge0$ on $\mathbb R[F]$, is a theorem. It comes from the ampleness of the theta
divisor: $\mathrm{Tr}(\varphi\varphi^\dagger)=\frac{2g}{(\Theta^g)}(\Theta^{g-1}\cdot\varphi^*\Theta)$ (Mumford, *Abelian Varieties* §21; not byte-cited). So, in every genus:

**RH for curves = positivity of the Rosati similitude form on the dual of the bond's cutoff cokernel, and that positivity is ampleness of $\Theta$.**

**Correction (L12, §13).** The constant-field tower is *not* needed. Restricting to $\mathbb Z+\mathbb ZF$ bounds only $\mathrm{Tr}\,F$, which is why
Castelnuovo–Severi-style arguments iterate over $F^r$. Using the whole commutative algebra $\mathbb R[F]$ gives RH at once (Proposition 15.2). So **the
absence of the tower is not the blocker for $\mathbb Q$. The absence of a polarisation (an ample "$\Theta$") is.**

**The dictionary, made exact by the calibration** (the analogy is classical, cf. Weil, Haran, Deninger, Connes–Consani; what is new here is
that the left column is derived from the bond's cutoff):

- **$\mathbb R[F]$ $\leftrightarrow$ the convolution algebra of test functions $h$ on $C_{\mathbb Q}$.** For curves, $\varphi=\sum c_kF^k$ is $h=\sum c_k\delta_{q^{-k}}$ on the degree
  group.
- **Rosati involution $\varphi(F)\mapsto\varphi(qF^{-1})$ $\leftrightarrow$ $h\mapsto\tilde h$, $\tilde h(x)=x^{-1}\overline{h(1/x)}$.**
- **$\mathcal T(\varphi,\varphi)=\sum_i\varphi(\alpha_i)\varphi(q/\alpha_i)$ $\leftrightarrow$ Weil's $Z(h)=\sum_\rho\hat h(\rho)\overline{\hat h(1-\bar\rho)}$.** Under
  $\alpha_i\leftrightarrow q^{\rho}$ these are the same formula.
- **Lefschetz** $\mathrm{Tr}_{H^1}=\mathrm{Tr}_{H^0}+\mathrm{Tr}_{H^2}-\#\mathrm{Fix}$ $\leftrightarrow$ **the explicit formula** $Z=P-\mathrm{Loc}$. The pole form $P$ is $H^0\oplus H^2$, and $\mathrm{Loc}$
  is the fixed-point count.
- **Hodge index on $C\times C$** (signature $(1,\rho-1)$ on $NS$, the positive direction in the plane of the two fibre classes) $\leftrightarrow$
  **Proposition 7** (the local form has negative index exactly $1$, the negative direction in the pole plane). Up to the overall sign
  convention, **$\Pi_1$ is the Hodge-index signature, and the pole plane spanned by the two constant terms of $\Theta$ is the hyperbolic plane of the two
  fibre classes.** Status: the correspondences are proved for curves by Propositions 14–15 and §6. For $\mathbb Q$ the right-hand column is the
  definition, and the left-hand objects (a "surface" whose Néron–Severi carries the test algebra) do not exist. That is Connes–Consani's
  square of the scaling site (`refs/src/2006.13771/weil-compo.tex:149-151`).

**What changes for $\mathbb Q$ (N2′, revised).** The earlier target, a counting interpretation of the de Branges–Wronskian kernel (L10), is the
reproducing-kernel shadow of the real target. Under RH, the Wronskian kernel of $\Xi$ is the reproducing kernel of a Hilbert space on which Weil's form
is the norm, just as the Casoratian is the genus-one Rosati form. The primary target is the Rosati one:

> Exhibit Weil's form $Z(h)$ as $\mathrm{Tr}(\varphi_h\varphi_h^\dagger)$ for an involutive algebra whose trace is positive for a *structural* reason: the
> analogue of $\Theta$ being ample.

In bond terms, the function-field $\Theta$ is the support $\{h^0>0\}\subset\mathrm{Pic}^{g-1}$ of the special part of the bond state $q^{h^0}$ (shard 04p). For
$\mathbb Q$ the special part of the theta orbit is Riemann's $\Phi$ (the part of $\vartheta$ beyond the two constant terms). Heuristic, not a claim: the
missing "ampleness" should be a positivity property of $\Phi$ as a divisor-like object on the adele class space, which the bond's
$L^2$ structure does not see (§§3, 9). This is where the next round of thinking should go. Concretely:
- **(a)** Write Mumford's formula $\mathrm{Tr}(\varphi\varphi^\dagger)\propto\Theta^{g-1}\cdot\varphi^*\Theta$ for genus one and two in class-group-bond coordinates, i.e. as sums over
  $\mathrm{Pic}$ weighted by $q^{h^0}$. This is computable from the data of shard 04p.
- **(b)** Read off the $\mathbb Q$-shaped expression, with $\Theta\to\Phi$, $\mathrm{Pic}\to C_{\mathbb Q}$, intersection $\to$ a two-point pairing on the orbit, and test it against
  the explicit formula.

Status of the new learning: Propositions 14 and 15 are proved (15 given the cited Rosati positivity). The dictionary is proved on the curve side and
definitional on the $\mathbb Q$ side. The $\Theta\to\Phi$ "ampleness" reading is heuristic.
