# A Dirichlet character of $\mathbb F_q(t)$: the finite case with every item of the ladder

Author: `claude:opus-5.5`, 2026-10-06, lane J of an orchestrated session.

Status: **a record, not a round; nothing registered in db/claims.tsv; no REFUTE review; no shard.** Each statement carries one of the labels
*standard* (classical, quoted from memory: `refs/src/` is absent in this container), *proved here*, *checked* (`checks/check_ff_dirichlet.py`),
*sketched*, *heuristic*, *open* or *negative finding*. Checks: `checks/check_ff_dirichlet.py`, output `checks/output_ff_dirichlet.txt`,
**118 of 118 pass** (about 35 s; python-flint, mpmath at 50 digits, PARI/GP for `hyperellcharpoly`).

Fills the rung asked for in `data-ladder.md` §§0, 4.3 and the "Unresolved/Next" item of `gate-phases.md` ("a function-field shadow ... where the
root number is a product of local Gauss sums over finite fields"). Conventions follow `adelic-gkp.md`, `gate-phases.md` and `zn-flux.md`.

**Verdict.**

- **All the items at once (checked, six examples, $q=3,5,7$, $N=2,3,4$, $\deg f=3,4$).** A power-residue character $\chi$ of $\mathbb F_q(t)$ modulo $f$
  has a polynomial $L$-function satisfying RH. Its root number is a product of local gate phases: a Gauss sum over $\mathbb F_q[t]/P$ at each $P\mid f$,
  and a Gauss sum over $\mathbb F_q$ at $\infty$ when $\chi$ is non-trivial on $\mathbb F_q^\times$. Its zeros are the eigenvalues of an integral step $F$ on
  a lattice $R=\mathbb Z[\zeta_N][F,V]$. That lattice carries an alternating integral similitude form $\Omega_+$, a Weil form $\tfrac12\mathrm{Tr}(x\,\sigma y)$ that
  is positive, and an invariant vacuum $J$. It is the $\chi$-isotypic part of $H_1$ of the Jacobian of the cyclic cover $y^N=c\,f(t)$.
- **The root number is a lattice datum here (proved here, elementary; checked).** $W=(-1)^n\det_{\mathbb Q(\zeta_N)}(F)/q^{n/2}$, where $n=\deg\Lambda$. So
  $W$ is the phase of the determinant of the step on the $\chi$-part. Over $\mathbb Z$ the phase is invisible ($\det F=q^{D/2}$). It does constrain the
  lattice: the companion lattice $\mathbb Z[\zeta_N][F]$ is $V$-stable for $n=2$ only when $W$ is a root of unity, and never for $n\ge3$.
- **The gate phases do not enter positivity (proved here; checked, with a control).** The involution $\sigma$ ($\zeta\mapsto\zeta^{-1}$, $F\mapsto q/F$)
  and the form $\Omega_+$ exist by the functional equation alone. The Weil form is positive if and only if $\sigma$ is complex conjugation in every
  embedding, that is, if and only if RH holds. $|W|=1$ follows from the functional equation with or without RH.
- **For $N=2$ the rung is not new (negative finding, checked).** A quadratic character of $\mathbb F_q(t)$ has $W=+1$. Its lattice is $H_1$ of the whole
  hyperelliptic Jacobian, so it is a curve of the existing rung read over the base $\mathbb F_q(t)$. Its local phases are non-trivial but cancel; in
  example X5 they are $+i$ at $f$ and $-i$ at $\infty$. The new content is $N\ge3$: a genuine phase $W\notin\{\pm1\}$ and a lattice with CM by $\mathbb Z[\zeta_N]$.
  In the zeta of the cover, which is a curve, the phases of the $\chi^j$-parts always cancel ($\prod_jW(\chi^j)=1$, checked).

---------------------------------------------------------------------------------------------------------------------

## 0. Conventions

- **Field.** $K=\mathbb F_q(t)$ with $q=p$ prime, and $A=\mathbb F_q[t]$. Here $f=\prod_iP_i$ is a product of distinct monic irreducibles, and
  $\chi=\prod_i(\cdot/P_i)_N$ with $N\mid q-1$. $(a/P)_N=a^{(Q-1)/N}\bmod P\in\mu_N(\mathbb F_q)$ is the $N$-th power-residue symbol, with $Q=q^{\deg P}$.
  It is sent to $\mathbb C$ by $g_q^j\mapsto e^{2\pi ij/(q-1)}$ for a fixed generator $g_q$ of $\mathbb F_q^\times$.
- **Parity.** On constants $\chi(c)=c^{(q-1)\deg f/N}$. Call $\chi$ *even* if it is trivial on $\mathbb F_q^\times$ ($N\mid\deg f$ for irreducible $f$), and *odd*
  otherwise.
- **$L$-function.** $L(u,\chi)=\sum_{m\text{ monic}}\chi(m)u^{\deg m}$. Put $\Lambda=L$ for odd $\chi$ and $\Lambda=L/(1-u)$ for even $\chi$. Write
  $\Lambda(u)=\sum_{k=0}^nc_ku^k=\prod_i(1-\alpha_iu)$ and $P_\chi(x)=x^n\Lambda(1/x)$.
- **Additive character.** $\psi=\prod_v\psi_v$ with $\psi_v(x)=\psi_0(\mathrm{Res}_v(x\,dt))$ and $\psi_0(a)=e^{2\pi ia/p}$. It is trivial on $K$ by the
  residue theorem (*standard*).
  - $dt$ has no zeros or poles at finite places, so $\psi_P$ is unramified ($d_P=0$), with $\psi_P(a/P)=\psi_0(\text{coefficient of }t^{\deg P-1}\text{ in }a\bmod P)$.
  - At $\infty$ ($\pi=1/t$, $dt=-\pi^{-2}d\pi$) we have $\psi_\infty(x)=\psi_0(-x_1)$, with conductor $\mathfrak p_\infty^{2}$, so $d_\infty=-2$.
  - Self-dual measures have $\mathrm{vol}(\mathcal O_v)=q_v^{-d_v/2}$: 1 at finite places and $q$ at $\infty$.
  - Gate: $F\Phi(y)=\int\Phi(x)\psi(xy)\,dx$. Squeeze: $D_cf(x)=|c|^{1/2}f(cx)$.
- **Idele class character (derived here from the product formula; checked through B3).**
  - At unramified $Q$: $\chi_Q(\text{uniformiser})=\chi(Q)$.
  - At $P_i\mid f$: $\chi_{P_i}=\bar\chi_i$ on $\mathcal O_{P_i}^\times$, where $\chi_i=(\cdot/P_i)_N$.
  - At $\infty$: $\chi_\infty=\chi$ on $\mathbb F_q^\times$ and $\chi_\infty(1/t)=1$.
  - At a ramified place, the value on its own uniformiser is $\chi_{P_i}(P_i)=\prod_{j\ne i}\chi_j(P_i)$. This is the analogue of $\psi_7(\sqrt{-7})=i$ in
    `gate-phases.md` §1.1.
- **The code and its overlaps (proved here, definitional).** $\Theta_K=\sum_{x\in K}\delta_x$. Consider the product state $\Phi^{(k)}$ with
  - the charged state $\chi_i1_{\mathcal O_{P_i}^\times}$ at each $P_i$,
  - $1_{t^k(1+\mathfrak p_\infty)}$ at $\infty$,
  - qunaughts $1_{\mathcal O_v}$ elsewhere.

  Then $\langle\Theta_K,\Phi^{(k)}\rangle=\sum_{m\text{ monic},\deg m=k}\chi(m)$, because the $x\in K$ in the support are exactly the monic polynomials of
  degree $k$ prime to $f$. So the coefficients of $L$ are overlaps of the code with product states charged at $f$. This is the twisted version of
  `curve-bridge.md` §3.

**Examples** (the $P_i$ low degree first; $z=\zeta_N$):

| | $q$ | $N$ | $f$ | parity | $\Lambda(u)$ | $W$ |
|---|---|---|---|---|---|---|
| X1 | 5 | 4 | $t^3+t+1$ | odd | $1+(-2+i)u+(3-4i)u^2$ | $(3-4i)/5$ |
| X2 | 5 | 4 | $t\,(t^2+2)$ | odd | $1-(4+3i)u^2$ | $-(4+3i)/5$ |
| X3 | 7 | 3 | $t^4+t^3+1$ | odd | $1+(2+2z)u-(2+6z)u^2+(14-7z)u^3$ | $(2-z)/\sqrt7$ |
| X4 | 7 | 3 | $t^3+t+1$ | even | $1+(3+2z)u$ | $(3+2z)/\sqrt7$ |
| X5 | 7 | 2 | $t^3+t+1$ | odd | $1+3u+7u^2$ | $1$ |
| X6 | 3 | 2 | $t^4+t^3+t^2+1$ | even | $1+2u+3u^2$ | $1$ |

## 1. The $L$-functions

**1.1 Polynomial and degree (standard, from memory: M. Rosen, *Number Theory in Function Fields*, Ch. 4; checked A1, A2).** For non-trivial
$\chi$, $\sum_{\deg m=k}\chi(m)=0$ once $k\ge\deg f$, because each residue class mod $f$ occurs $q^{k-\deg f}$ times. So $\deg L\le d-1$, where $d=\deg f$. For
even $\chi$, $L(1,\chi)=0$, so $\Lambda=L/(1-u)$ has degree $d-2$; for odd $\chi$, $\deg L=d-1$ (when $\chi$ is primitive, as all examples are).

- A1 checks $S_d=S_{d+1}=0$, the stated degree, the parity, and the exact coefficients in $\mathbb Z[\zeta_N]$.
- A2 checks the Euler product over monic irreducibles prime to $f$ against the sum over monics, to $u^d$.

**1.2 RH (standard, Weil, from memory: A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent*, 1948; checked A3, B6).**

- All reciprocal roots satisfy $|\alpha|=\sqrt q$ to 50 digits in X1–X6.
- The same holds in a census of every monic irreducible $f$ for $(q,N,\deg f)=(5,4,3),(5,4,4),(7,3,3),(7,2,3),(3,2,4),(5,2,3)$, and for 60 random quartics
  at $(7,3,4)$: 532 characters, all ok.

**1.3 The functional equation and the root number (proved here, elementary; checked A4, A5).** In the form found by comparing coefficients,

$$
\Lambda(u)=W\,(\sqrt q\,u)^{n}\,\overline\Lambda\bigl(1/(qu)\bigr),\qquad W=c_n/q^{n/2},\qquad |W|=1,
$$

with $\overline\Lambda$ the polynomial with conjugated coefficients, which is $\Lambda(u,\bar\chi)$. Comparing the coefficients of $u^n$ and $u^0$ gives
$|W|^2=1$ from the functional equation alone. In terms of $G(\chi)=\sum_{a\bmod f}\chi(a)\psi_0(\text{coefficient of }t^{d-1}\text{ in }a)$ and
$g=\sum_{c\in\mathbb F_q^\times}\chi(c)\psi_0(c)$:

$$
W=\frac{G(\chi)}{q^{d/2}}\quad(\chi\text{ even}),\qquad W=\frac{G(\chi)/q^{d/2}}{g/\sqrt q}\quad(\chi\text{ odd}).
$$

*Proof.* Split the sum defining $G$ by the degree of $a$, and write $a=cm$ with $m$ monic and $c\in\mathbb F_q^\times$.

- For odd $\chi$: the terms with $\deg a<d-1$ have $\psi=1$ and sum to zero, since $\sum_c\chi(c)=0$. So $G=g\cdot S_{d-1}$, where $S_{d-1}=c_{d-1}$.
- For even $\chi$: those terms give $(q-1)\sum_{k<d-1}S_k=-(q-1)S_{d-1}$, using $L(1)=0$. The top degree gives $-S_{d-1}$. So $G=-qS_{d-1}$, which is $q$ times the
  top coefficient of $\Lambda$. ∎

**This answers the brief's question about the exact form.** $W=G/\sqrt{q^{\deg f}}$ holds for even $\chi$, and then only for $\Lambda=L/(1-u)$ of degree $d-2$, not for $L$
itself. For odd $\chi$ there is a second factor, the normalised Gauss sum of $\chi|_{\mathbb F_q^\times}$, which is the phase at $\infty$ (§3).

**Digits.**

- The functional equation with $W=c_n/q^{n/2}$ holds exactly for X1, X2, X5 and X6 (integer and Gaussian-integer arithmetic), and to $10^{-51}$ for X3 and
  X4. With $-W$ the relative residual is 2.0.
- $W$ from the Gauss sums agrees with $c_n/q^{n/2}$ to 49–51 digits; $|G|^2=q^d$ exactly.

## 2. The lattice state

**2.1 The algebra and the involution (proved here; checked C2).** Let $E=\mathbb Q(\zeta_N)[x]/(P_\chi)$, a $\mathbb Q$-algebra of dimension $D=n\varphi(N)$, with $F=x$
and $V=q/F$. Let $\sigma$ be the map $\zeta\mapsto\zeta^{-1}$, $F\mapsto V$.

- $\sigma$ is a well-defined ring involution of $E$ if and only if $P_\chi$ divides the numerator of $\overline{P_\chi}(q/x)$. That is the multiset identity
  $\{\bar\alpha_i\}=\{q/\alpha_i\}$, which is the functional equation, not RH.
- Under RH, $\bar\alpha_i=q/\alpha_i$ holds root by root, and $\sigma$ is complex conjugation in every embedding.

**2.2 The order and the companion lattice (proved here; checked C1).** Let $R=\mathbb Z[\zeta_N][F,V]$, found by Hermite normal form inside $E$. It is
stable under $F$, $V$ and $\zeta$, with $FV=q$.

- The characteristic polynomial of $V$ over $\mathbb Q(\zeta_N)$ is $\overline{P_\chi}$, which has integral coefficients by the functional equation. So $R$ is an
  order, free of rank $n$ over $\mathbb Z[\zeta_N]$ (a PID for $N\le4$).
- The companion lattice $\mathbb Z[\zeta_N][F]$ is $V$-stable if and only if $q/c_n\in\mathbb Z[\zeta_N]$. Since $|q/c_n|=q^{1-n/2}$ in every embedding:
  - $n=1$: always stable;
  - $n=2$: stable if and only if $W=c_n/q$ is a root of unity in $\mathbb Q(\zeta_N)$;
  - $n\ge3$: never stable (the norm is less than 1).

  Observed indices $[R:\mathbb Z[\zeta][F]]$: 5, 5, 7 for X1, X2, X3, where $W=(3-4i)/5$, $-(4+3i)/5$, $(2-z)/\sqrt7$ are not roots of unity. The index is 1 for X4, X5, X6.
- **So the gate phase decides whether the naive step lattice also carries $V$.**

**2.3 The form and the Weil form (proved here; checked C3, C4, C7).** Define $\Omega_+(x,y)=\mathrm{Tr}_{E/\mathbb Q}\bigl(x\,\sigma(y)/(V-F)\bigr)$, the form of
`cone-bridge.md`.

- It is alternating, $\zeta$-invariant, and a $q$-similitude of $F$. These use only $\sigma$, so only the functional equation.
- Its Weil form is exactly $\tfrac12\Omega_+(x,(F-V)y)=\tfrac12\mathrm{Tr}_{E/\mathbb Q}(x\,\sigma y)$, because $\sigma(F-V)=V-F$.
- This trace form is positive definite if $\sigma$ is complex conjugation in every embedding ($\sum|x|^2$). If it is not, $\sigma$ pairs two different
  embeddings and the form contains a hyperbolic plane (*sketched*). So **positivity is RH**. The phase $W$ plays no part.
- Exact leading minors of the Weil form:

  | | leading minors |
  |---|---|
  | X1 | 4, 16, 240, 3600 |
  | X2 | 4, 16, 320, 6400 |
  | X3 | 6, 27, 1062, 31329, 4780062, 546993027 |
  | X4 | 2, 3 |
  | X5 | 2, 19 |
  | X6 | 2, 8 |

- **Control C7.** $x^2-6x+5$ with $q=5$ (roots 1 and 5) has the functional equation but not RH. $\sigma$ and $\Omega_+$ still exist, and the Weil form has
  minors $2,-16$.
- **Integrality.** On $R$, $\Omega_+$ has denominator 11 (X1), 1 (X2), 29 (X3), 2 (X4), 1 (X5, X6). The elementary divisors of its primitive integral multiple
  are:

  | | elementary divisors | principal? |
  |---|---|---|
  | X1 | $1,1,33,33$ | no |
  | X2 | $1,1,2,2$ | no |
  | X3 | $1,1,29,29,55941,55941$ | no |
  | X4, X5, X6 | $1,1$ | yes |

  As in `cone-bridge.md`, $\Omega_+$ is one point of the cone of compatible forms. Which point is the polarisation of the abelian variety is not
  decided here.

**2.4 The vacuum (checked C5).** $J=(F-V)\bigl(4q-(F+V)^2\bigr)^{-1/2}$ on $R$, the formula of `zn-flux.md` Prop. 2.1(5).

- The spectrum of $F+V$ is real and lies in $(-2\sqrt q,2\sqrt q)$, which is RH.
- $J^2=-1$, $JF=FJ$ and $J\zeta=\zeta J$.
- $\Omega J$ is symmetric positive definite: residuals at most $7\times10^{-12}$, smallest eigenvalue between 0.21 and 2.

**2.5 Galois orbit, ordinariness, Deligne module (standard: Deligne, *Variétés abéliennes ordinaires sur un corps fini*, 1969; Centeleghe–Stix,
*Categories of abelian varieties over finite fields I*, 2015; from memory; checked C6).**

- $\mathrm{charpoly}_{\mathbb Z}(F|R)=\prod_{j\in(\mathbb Z/N)^\times}P_{\chi^j}$, with each $L(u,\chi^j)$ recomputed from its own character sums:

  | | $\mathrm{charpoly}_{\mathbb Z}(F\vert R)$ |
  |---|---|
  | X1 | $x^4-4x^3+11x^2-20x+25$ |
  | X2 | $x^4-8x^2+25$ |
  | X3 | $x^6+2x^5+6x^4+19x^3+42x^2+98x+343$ |
  | X4 | $x^2+4x+7$ |
  | X5 | $x^2+3x+7$ |
  | X6 | $x^2+2x+3$ |

- The middle coefficients 11, $-8$, 19, 4, 3, 2 are prime to $p$, so all six are ordinary and $(R,F,V)$ is a Deligne module.
- Since $q=p$, Centeleghe–Stix would cover non-ordinary cases as well.
- $\mathbb Z[\zeta_N]$ acts as complex multiplication, as in `zn-flux.md` §2. For X1–X4 the characteristic polynomial is not a square, because $\chi$ and
  $\bar\chi$ have different (conjugate) $L$-functions. This differs from the graph rung, where it was always a square.

**2.6 The abelian variety (standard, from memory: the $N$-th power reciprocity law of $\mathbb F_q[t]$, Rosen Ch. 3; checked D1–D3).** $\chi$ cuts out the
Kummer extension $K(\sqrt[N]{cf})$.

- **Which $c$.** Reciprocity, $(Q/P)_N=(-1)^{\frac{q-1}N\deg P\deg Q}(P/Q)_N$, fixes $c$ by $c^{(q-1)/N}=(-1)^{(q-1)d/N}$. That gives $c=-1$ for X1, X2, X5 and
  $c=1$ for X3, X4, X6.
- **D1.** The zeta numerator of the smooth projective curve $C:y^N=cf$ equals $\prod_{j=1}^{N-1}\Lambda(u,\chi^j)$ exactly. It was computed by point counts over
  $\mathbb F_{q^r}$, $r\le g$, for $N=3,4$, and by `hyperellcharpoly` for $N=2$.
  - Example: X1 gives $1-u+4u^2-7u^3+20u^4-25u^5+125u^6$, genus 3.
  - Control: with $c$ multiplied by a non-$N$-th power (an unramified twist $u\mapsto\zeta u$), the match fails in all six.
- **D2, D3.** $\mathrm{charpoly}(F|R)$ divides the numerator. The $\chi$-part is:

  | | $\chi$-part |
  |---|---|
  | X1, X2 | an abelian surface with CM by $\mathbb Z[i]$, the complement in $\mathrm{Jac}(y^4=-f)$ of the elliptic curve $y^2=-f$ (Prym-type); $\Lambda(u,\chi^2)=1+3u+5u^2$ (X1), $1-4u+5u^2$ (X2), as `hyperellcharpoly` gives |
  | X3 | the whole Jacobian of $y^3=t^4+t^3+1$ over $\mathbb F_7$: genus 3, CM by $\mathbb Z[\zeta_3]$ |
  | X4 | the elliptic curve $y^3=t^3+t+1$ over $\mathbb F_7$ ($j=0$): $F=-(3+2\zeta_3)$ |
  | X5, X6 | the whole Jacobian of the genus-1 curves $y^2=-(t^3+t+1)$ over $\mathbb F_7$ and $y^2=t^4+t^3+t^2+1$ over $\mathbb F_3$ |

- **What is not settled (open).** $R$ is one Deligne module in the isogeny class: the one with endomorphism ring exactly $R$. The page does not show which
  lattice is $H_1$ of the actual $\chi$-part, nor its polarisation. This is the class question of `curve-bridge.md` and `overlap-data.md`, unchanged.

**2.7 The root number as the determinant of the step (proved here; checked C8).** From $c_n=(-1)^n\prod\alpha_i$ and §1.3,

$$
W=(-1)^n\,\frac{\det_{\mathbb Q(\zeta_N)}F}{q^{n/2}} .
$$

- The gate phase is the normalised top exterior power of the step on the $\chi$-isotypic part.
- After restriction of scalars, $\det_{\mathbb Z}F=\prod_\sigma\sigma(\det F)=q^{D/2}$, so the phase cannot be seen without the CM action.
- For $n=1$ (X4), $W=-\alpha/\sqrt q$ is the normalised zero itself. The Frobenius of the CM elliptic curve $y^3=f$ is a normalised cubic Gauss sum over
  $\mathbb F_{343}$, as in the classical Gauss–Jacobi-sum description of Fermat-type curves (*standard*, from memory).

## 3. The gate phases

**3.1 Local identities (proved here; checked B1, B2).** At every place the local state is a Fourier eigenvector up to a squeeze, $F\Phi_v=\lambda_vD_{c_v}\Phi_v^\vee$,
with $\Phi^\vee$ the conjugate charge. The local root number is $\varepsilon_v(\tfrac12)=\chi_v(c_v)\lambda_v$, and $v(c_v)=a_v+d_v$.

- **$P\mid f$ ($Q=q^{\deg P}$, tame, $a_P=1$, $d_P=0$).** The state is $\Phi_P=\chi_i1_{\mathcal O_P^\times}$.
  - $\Phi_P$ is $\mathfrak p$-periodic and supported on $\mathcal O_P$, so $F\Phi_P$ lives on $\mathfrak p^{-1}/\mathcal O_P$. There
    $F\Phi_P(b/P)=Q^{-1}\bar\chi_i(b)\,G_P$, with $G_P=\sum_{x\bmod P}\chi_i(x)\psi_0(\text{coefficient of }t^{\deg P-1}\text{ in }x)$.
  - Hence $F\Phi_P=\frac{G_P}{\sqrt Q}\,D_P\bigl(\bar\chi_i1_{\mathcal O_P^\times}\bigr)$, and

$$
\varepsilon_P=\chi_P(P)\,G_P/\sqrt Q,\qquad N_P=Q .
$$

- **$\infty$, odd $\chi$ ($a_\infty=1$, $d_\infty=-2$).** The state is $\Phi_\infty=\bar\chi_\infty1_{\mathcal O_\infty^\times}$, a charged state at infinity.
  - $F\Phi_\infty$ is supported on $\mathfrak p_\infty/\mathfrak p_\infty^2$, where $F\Phi_\infty(\pi y_1)=\chi(-y_1)\,g(\bar\chi)$.
  - Hence $F\Phi_\infty=\lambda_\infty D_{1/\pi}\Phi_\infty^\vee$ with $\lambda_\infty=\bar g/\sqrt q$, and since $\chi_\infty(1/\pi)=1$:

$$
\varepsilon_\infty=\bar g/\sqrt q,\qquad N_\infty=q^{-1} .
$$

- **$\infty$, even $\chi$.** The state is the qunaught. $F1_{\mathcal O_\infty}=q\,1_{\mathfrak p_\infty^2}=D_{\pi^{-2}}1_{\mathcal O_\infty}$: a pure squeeze by the different of $dt$,
  with $\varepsilon_\infty=1$ and $N_\infty=q^{-2}$.
- **Every other place.** The state is the qunaught $1_{\mathcal O_v}$, with $F1_{\mathcal O_v}=1_{\mathcal O_v}$ and phase 1.

**Checks.**

- B1 sums the Fourier transform directly on $\mathfrak p^{-1}/\mathcal O$; residual at most $2\times10^{-16}$, including $Q=2401$.
- B2 works on $\mathfrak p^{-1}/\mathfrak p^3$ against the Laurent model, without using the support argument; residual at most $5\times10^{-15}$.
- Both compute the Tate ratio $Z(F\Phi,\chi_v^{-1},1-s)/Z(\Phi,\chi_v,s)=\varepsilon_vN_v^{1/2-s}$ at $s=\tfrac12$, $0.3+0.7i$ and $1.7-0.4i$, to $10^{-49}$.

**3.2 Products (checked B3, B4, B6, B7).**

| | phase at $f$ | phase at $\infty$ | product $=W$ | conductor exponent $\sum_v(a_v+d_v)\deg v$ |
|---|---|---|---|---|
| X1 | $0.99596+0.08981i$ | $0.52573-0.85065i$ | $0.6-0.8i$ | $3+1-2=2$ |
| X2 | $t$: $-0.85065-0.52573i$; $t^2+2$: $0.44721+0.89443i$ | $0.52573-0.85065i$ | $-0.8-0.6i$ | $1+2+1-2=2$ |
| X3 | $0.70121-0.71295i$ | $0.89595+0.44415i$ | $0.94491-0.32733i$ | $4+1-2=3$ |
| X4 | $0.75593+0.65465i$ | $1$ (qunaught, squeeze only) | $0.75593+0.65465i$ | $3-2=1$ |
| X5 | $+i$ | $-i$ | $1$ | $3+1-2=2$ |
| X6 | $1$ | $1$ (qunaught) | $1$ | $4-2=2$ |

- The products equal $c_n/q^{n/2}$ to 49–51 digits. The conductor exponent equals $\deg\Lambda$ in every case.
- Tate's global functional equation assembled only from local data, $\Lambda(u)=\bigl(\prod\varepsilon_v\bigr)(\sqrt qu)^{\sum\log_qN_v}\overline\Lambda(1/(qu))$, holds to
  $10^{-50}$ at three complex points (B4). Tate's thesis for function fields is *standard* (from memory: Weil, *Basic Number Theory*, Ch. VII).
- In the census (532 characters, B6) the product is $W$ every time.
- For X2 the global Gauss sum factorises as $G=\chi_1(P_2)\chi_2(P_1)G_1G_2$ (B5).
- **The factors $\chi_{P_i}(P_i)$ are needed (B7).** These are the ramified characters on their own uniformisers. Dropping them gives the wrong $W$ for 30 of the
  50 products $f=P_1P_2$ (degree $1\times2$) at $q=5$, $N=4$.

**3.3 Comparison with the arithmetic rung (checked B8; reading mine).**

- **X5 has the pattern of 49a1.** The phase is $+i$ at the conductor and $-i$ at infinity, with product $+1$ (`gate-phases.md` §3.1). At $\infty$ the $-i$
  is the normalised quadratic Gauss sum $\overline{g_7}/\sqrt7$ of the charged state $\bar\chi_\infty1_{\mathcal O^\times}$. That is the function-field counterpart
  of the Hermite phase of $x\,e^{-\pi x^2}$.
- **X1 at infinity.** $\chi|_{\mathbb F_5^\times}=\bar\chi_D$, where $\chi_D$ is the quartic Dirichlet character mod 5 with $\chi_D(2)=i$, and

$$
\varepsilon_\infty(\text{X1})=-\tau(\chi_D)/\sqrt5=-i\,W(\chi_D),\qquad W(\chi_D)=0.85065+0.52573i,
$$

  which is the root number of `gate-phases.md` D3. The same Gauss sum of $\mathbb F_5$ sits at the place $\infty$ of $\mathbb F_5(t)$ and at the finite place 5
  of $\mathbb Q$.

**3.4 The GKP table (local identities proved here and checked; reading mine).**

| place | local state | gate | phase |
|---|---|---|---|
| $P\nmid f$, finite | qunaught $1_{\mathcal O_P}$ | $1_{\mathcal O_P}$ | 1 |
| $P\mid f$ | charged $\chi_i1_{\mathcal O_P^\times}$ | $(G_P/\sqrt Q)\,D_P(\bar\chi_i1_{\mathcal O_P^\times})$ | $\chi_P(P)G_P/\sqrt Q$ |
| $\infty$, $\chi$ even | qunaught $1_{\mathcal O_\infty}$ | $D_{\pi^{-2}}1_{\mathcal O_\infty}$ | 1 |
| $\infty$, $\chi$ odd | charged $\bar\chi_\infty1_{\mathcal O_\infty^\times}$ | $(\bar g/\sqrt q)\,D_{1/\pi}(\chi_\infty1_{\mathcal O_\infty^\times})$ | $\bar g/\sqrt q$ |
| global | $\Theta_K$, Poisson-invariant | | $W=\prod_v$, $=(-1)^n\det F/q^{n/2}$ |

**3.5 The phases cancel in the cover (checked D4).**

- $\prod_{j=1}^{N-1}W(\chi^j)=1$ in all six examples; here $W(\chi^{N-j})=\overline{W(\chi^j)}$. This is forced: by D1 the product of the $\Lambda(\chi^j)$ is the zeta
  numerator of a curve, and its root number is $+1$ (`gate-phases.md` §5.1).
- The gate-phase item is "trivial for curves" only because the curve's zeta is the product over the whole Galois orbit, with the CM action forgotten. In
  the $\chi$-isotypic parts the phases are there.
- For $N=2$ the orbit is $\{\chi\}$, so $W(\chi)=1$ for every quadratic character of $\mathbb F_q(t)$. The census gives one value of $W$ for each of the
  three quadratic families (*negative finding* for "new rung" at $N=2$).

## 4. Conclusion

1. (*checked*) The Dirichlet characters of $\mathbb F_q(t)$ of order $N\ge3$ are the first understood case on the ladder with both a global
   lattice-with-step ($R$, $F$, $V$, $\Omega_+$, $J$) and non-trivial local gate phases, with $W\notin\{\pm1\}$ (X1–X4).
2. (*proved here; checked*) The gate phases are not an obstacle to the lattice. The charged local states at $f$ and at $\infty$ coexist with an integral
   step of norm $q$ on $R$, and $W$ is the normalised determinant of that step on the $\chi$-part.
3. (*proved here*) The phase does constrain the choice of lattice. The companion lattice $\mathbb Z[\zeta_N][F]$ carries $V$ only if $n\le1$, or if $n=2$ and $W$ is a
   root of unity. The order $\mathbb Z[\zeta_N][F,V]$ always carries $V$.
4. (*standard; checked*) The lattice is the $\chi$-isotypic part of $H_1$ of the Jacobian of $y^N=cf$, with $c$ fixed by reciprocity. Its counts are the point
   counts of that curve over $\mathbb F_{q^r}$, and the coefficients of $L$ are overlaps of $\Theta_K$ with product states charged at $f$. It is a Deligne
   module (all six are ordinary), and for $q=p$ a Centeleghe–Stix object in any case.
5. (*proved here; checked with a control*) The gate phases do not enter the positivity. $\sigma$ and $\Omega_+$ exist by the functional equation alone. The
   Weil form $\tfrac12\mathrm{Tr}(x\sigma y)$ is positive exactly when RH holds. So RH is still the vacuum, the non-emptiness of the cone, and $|W|=1$ holds with or without it.
6. (*checked*) The phases of the $\chi^j$-parts cancel in the zeta of the cover. So the curve rung's trivial phases and this rung's non-trivial ones
   are the same objects, seen without or with the CM action.
7. (*negative finding*) For $N=2$ the rung adds nothing new: $W=1$, the lattice is the whole hyperelliptic $H_1$, and the local phases (for example $i$ and $-i$ in X5)
   cancel.
8. (*checked*) The local phases have the shape of the arithmetic rung. They are Gauss sums over the residue fields at the conductor, and at $\infty$ for
   odd $\chi$ a Gauss sum of $\mathbb F_q$, which plays the role of the Hermite phase. X5 reproduces 49a1's $(+i,-i)$, and X1's $\varepsilon_\infty$ is $-i$ times the root number
   of the quartic character mod 5.
9. (*heuristic*) For Dirichlet $L$ over $\mathbb Q$, the local charged states and their phases are present on both sides with the same Gauss-sum
   structure. The missing item is the same as for $\zeta$: the global lattice-with-step. The determinant reading of $W$ (item 2) has no counterpart over
   $\mathbb Q$ because that step is missing.
10. (*open*) Which Deligne module in the isogeny class is $H_1$ of the $\chi$-part, and which point of the cone is its polarisation.

## 5. Remarks on existing pages

- `zn-flux.md` §5 item 4 says that the finite rung has no non-self-dual character, "and this item has no finite analogue". That is true for graphs. The
  function-field rung supplies one: for X1–X4, $\Lambda(u,\bar\chi)=\overline{\Lambda(u,\chi)}\ne\Lambda(u,\chi)$, and the zeros are reflected
  ($\alpha\mapsto\bar\alpha=q/\alpha$). This is an addition, not an error.
- `data-ladder.md` §4 item 3 lists the gate phases as "trivial for curves over $\mathbb F_q$". That is right for a curve's zeta. §3.5 above refines it: a
  curve with a $\mu_N$-action carries non-trivial phases on its isotypic parts, and they cancel in the product.
- `gate-phases.md` "Next" asks for "a quadratic twist of a curve over $\mathbb F_q$". This page gives ramified characters of $\mathbb F_q(t)$, which are twists of
  the trivial motive. A ramified twist of an elliptic curve over $\mathbb F_q(t)$ (an $L$-function of degree 2 over the base) is not done here.
- The brief's form "$W(\chi)=$ Gauss sum$/\sqrt{q^{\deg f}}$" holds only for even $\chi$, and for $\Lambda=L/(1-u)$. For odd $\chi$ divide by the normalised Gauss
  sum of $\chi|_{\mathbb F_q^\times}$ (§1.3).

## 6. Status and checks

*Review corrections 2026-10-06 (`notes/reviews/adelic-gkp-ff-family-2026-10-06.md`, 14 VALID / 3 MINOR / 0 INVALID):* (1) "positivity is RH" needs $P_\chi$ squarefree: for $q=5$, $N=4$, $f=t^4+1$ (the Fermat quartic) $P_\chi=(x+1+2i)^2$, RH holds, the trace form on $R$ has rank 2 of 4, $\Omega_+$ is degenerate, $F$ is not semisimple and there is no vacuum; repeated roots also at $(7,3,4)$, $(7,3,5)$, $(5,4,5)$, $(3,2,6)$, all with reducible $f$. (2) The leading-minor table of §2.3 lists minors of the trace form $\mathrm{Tr}(x\sigma y)$ (twice the Weil form) on the companion lattice $\mathbb Z[\zeta][F]$, not on $R$; on $R$ the determinants are 144, 256, 11163123, 3, 19, 8. (3) For $N=2$, X6's local phases are both 1, and "its lattice is $H_1$" holds up to isogeny only, failing when $\Lambda=(1+2u+3u^2)^2$.


| statement | status | check |
|---|---|---|
| $L(u,\chi)$ is a polynomial of degree $d-1$ (odd) or $(1-u)\times$ degree $d-2$ (even); Euler product | standard; checked | A1, A2 |
| RH, $\lvert\alpha\rvert=\sqrt q$ (six examples, census of 532) | standard (Weil); checked | A3, B6 |
| FE $\Lambda(u)=W(\sqrt qu)^n\overline\Lambda(1/(qu))$, $W=c_n/q^{n/2}$, $\lvert W\rvert=1$; fails with $-W$ | proved here; checked (exact, or 51 digits) | A4 |
| $W=G/q^{d/2}$ (even), $W=(G/q^{d/2})/(g/\sqrt q)$ (odd) | proved here; checked (49–51 digits) | A5 |
| local identities $F\Phi_v=\lambda_vD_{c_v}\Phi_v^\vee$; $\varepsilon_P=\chi_P(P)G_P/\sqrt Q$, $\varepsilon_\infty=\bar g/\sqrt q$ or 1 | proved here; checked | B1, B2 |
| $\prod_v\varepsilon_v=W$; conductor exponent $=\deg\Lambda$; global FE from local data | standard (Tate); checked (49–51 digits) | B3, B4, B6 |
| CRT factorisation of $G$; the factors $\chi_P(P)$ needed (30 of 50 fail without) | proved here; checked | B5, B7 |
| X1's $\varepsilon_\infty=-i\,W(\chi_D)$, $\chi_D$ quartic mod 5 | checked | B8 |
| $R=\mathbb Z[\zeta][F,V]$ stable; companion lattice $V$-stable iff $q/c_n$ integral (index 5, 5, 7, 1, 1, 1) | proved here; checked | C1 |
| $\sigma$ exists by the FE | proved here; checked | C2 |
| $\Omega_+$ alternating, $\zeta$-invariant, similitude; integrality data | proved here; checked | C3 |
| Weil form $=\tfrac12\mathrm{Tr}(x\sigma y)$, positive iff RH; control $x^2-6x+5$ indefinite | proved here; checked | C4, C7 |
| vacuum $J$ | checked (float) | C5 |
| $\mathrm{charpoly}_{\mathbb Z}=\prod_{j\in(\mathbb Z/N)^\times}P_{\chi^j}$; all six ordinary | standard (Deligne); checked | C6 |
| $W=(-1)^n\det_{\mathbb Q(\zeta)}F/q^{n/2}$; $\det_{\mathbb Z}F=q^{D/2}$ | proved here; checked | C8 |
| zeta of $y^N=cf$ $=\prod_j\Lambda(\chi^j)$, $c$ from reciprocity; twisted $c$ fails; $\chi$-part divides; $\chi^2$-part $=y^2=cf$ | standard (Rosen, from memory); checked | D1–D3 |
| $\prod_jW(\chi^j)=1$; $W=1$ for quadratic $\chi$ | proved here (from D1 and the curve FE); checked | D4, B6 |
| coefficients of $L$ as overlaps of $\Theta_K$ with charged product states | proved here (definitional) | – |
| which lattice is $H_1$ of the $\chi$-part; its polarisation | open | – |
| for Dirichlet $L$ over $\mathbb Q$ the missing item is the global lattice | heuristic | – |

## 7. Next

- A ramified twist of a curve: $E\otimes\chi$ over $\mathbb F_q(t)$ for an elliptic curve $E/\mathbb F_q$ (constant) and a ramified $\chi$. This is an $L$-function of
  degree $2\deg$ with phases at $f$ and at $\infty$. It is the closer shadow of 441d1 asked for in `gate-phases.md`.
- Decide which Deligne module in the isogeny class of the $\chi$-part is $H_1$ of the Prym of $y^4=-f$ (X1), for example by the Weil pairing as in `overlap-data.md`.
- Wild characters ($N=p$, Artin–Schreier covers), where the local gate at $P\mid f$ has conductor exponent at least 2 and the squeeze is not by $P$ alone.
- Fold a row "Dirichlet character of $\mathbb F_q(t)$" into `data-ladder.md` §0 when the synthesis is next revised (not done here; existing pages untouched).
