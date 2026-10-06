# The local Fourier-gate phases and the root number

Author: `claude:opus-5.5`, 2026-10-06, lane I of an orchestrated session.

Status: **a record, not a round; nothing registered in `db/claims.tsv`; no REFUTE review; no shard.** Each statement carries one of the labels *standard* (classical; quoted from memory, since `refs/src/` is absent in this container), *proved here*, *checked* (numerically, `checks/check_gate_phases.py`), *sketched*, *heuristic*, *open* or *negative finding*. Checks: `checks/check_gate_phases.py`, output `checks/output_gate_phases.txt` (32 of 32 pass; needs PARI/GP with elldata, about 20 s).

Companion to `cm-lift.md` (lane C). That page's "Unresolved" item was the local phases of the Fourier gate. This page computes them for 49a1 and 441d1 and checks that their product is the root number.

Conventions are those of `adelic-gkp.md` and `cm-lift.md`.

- **The field.** $K=\mathbb Q(\sqrt{-7})$, $\pi=\sqrt{-7}$, embedded as $i\sqrt7$, and $w=\tfrac{1+\pi}2$.
- **Additive characters.** $\psi_\infty(x)=e^{-2\pi ix}$ and $\psi_p(x)=e^{2\pi i\{x\}_p}$. On $K$ the additive character is $\psi\circ\mathrm{Tr}$; at the complex place this is $e^{-4\pi i\,\mathrm{Re}(zw)}$.
- **Measures.** All measures are self-dual: $2\,dx\,dy$ on $\mathbb C$, and $\mathrm{vol}(\mathcal O_v)=N\mathfrak d_v^{-1/2}$ at a finite place, so $\mathrm{vol}(\mathcal O_7)=7^{-1/2}$.
- **Gates.** The Fourier gate is $F\Phi(y)=\int\Phi(x)\psi(\mathrm{Tr}\,xy)\,dx$, the GKP Hadamard of `functional-equation-gate.md`. The squeeze is $D_cf(x)=|c|^{1/2}f(cx)$.
- **Normalisation of $s$.** I work with the unitary character $\psi_u(\mathfrak a)=\psi(\mathfrak a)/N\mathfrak a^{1/2}$, centre $s=\tfrac12$. PARI's motivic $s$ is this $s$ plus $\tfrac12$.

**Verdict.**

- **The gate phases (proved here; checked to 15–50 digits).** The local root numbers $\varepsilon_v=\varepsilon_v(\tfrac12,\psi_{u,v},\psi_{K,v})$ over the places of $K$ are:

  | curve | $\infty$ | $7$ | $3$ | every other place |
  |---|---|---|---|---|
  | 49a1 | $-i$ (Hermite phase) | $+i$ (Gauss sum) | $1$ | $1$ |
  | 441d1 | $-i$ | $+i$ | $-1$ | $1$ |

  The products are $+1$ and $-1$. These equal `ellrootno` and `lfunrootres`.
- **The functional equation is checked independently of PARI.** With $W=\prod_v\varepsilon_v$ and conductor $\prod_vN_v$, the theta overlap of lane C satisfies its functional equation to 31 digits (49a1) and 30 digits (441d1), using only the $a_n$. With $-W$ it fails at order one.
- **The GKP reading (proved here, as a reorganisation of Tate's thesis, which is *standard*).** Every local test state is a Fourier eigenvector up to a squeeze. The phase is $1$ on the qunaughts $1_{\mathcal O_v}$, and it is a Gauss-sum or Hermite phase on the charged states. The global gate fixes $\Theta_K$ by Poisson summation, so the root number is the product of the local eigenphases, each corrected by the character's value on the squeeze.
- **The twist (proved here; checked).** Twisting by $\chi_{-3}$ changes one local state: at 3 the qunaught $1_{\mathcal O_3}$ becomes the charged state $\eta\,1_{\mathcal O_3^\times}$, with $\eta$ the quadratic character of $\mathbb F_9^\times$. Its gate phase is $-1$, and this flips $W$. The step at 3 does not change sign in any invariant sense. It stops being an invariant at all, because a ramified character has no well-defined value on "the" uniformiser. **The datum that tells the twins apart lives in the Hilbert space of the local mode at 3 (a charge and its gate phase), not on the lattice $\mathcal O_K$ or in the vacuum $J_K$.**
- **Limitation (negative finding, elementary).** The gate phases live only at the ramified places and at $\infty$. The root number therefore cannot see the sign pattern $\chi_{-3}(p)$ at the split primes, which is the larger part of the difference between the twins found by lane C. What it fixes is the parity of the order of the central zero, not the zeros.

---------------------------------------------------------------------------------------------------------------------

## 1. The local components of $\psi$ and $\psi'$

**1.1 From the ideal character to the idele class character (standard; the values derived here; checked B1).** Lane C's character is $\psi_u((\alpha))=\varepsilon(\alpha)\alpha/|\alpha|$ on ideals prime to $\pi$, with $\varepsilon$ the Legendre symbol modulo $\pi$. Write $\psi_u=\prod_v\psi_v$, trivial on $K^\times$. At an unramified place $\psi_v$ is unramified, with $\psi_v(\varpi_v)=\psi_u(\mathfrak p_v)$.

- For $\alpha$ prime to 7, triviality on $K^\times$ gives $\psi_\infty(\alpha)\psi_7(\alpha)=\bigl(\varepsilon(\alpha)\alpha/|\alpha|\bigr)^{-1}$. Hence

$$
\psi_\infty(z)=\frac{|z|}{z},\qquad \psi_7\big|_{\mathcal O_7^\times}=\varepsilon .
$$

- $\pi$ is a unit at every place except 7 and $\infty$. Hence

$$
\psi_7(\pi)=\psi_\infty(\pi)^{-1}=\frac{i\sqrt7}{\sqrt7}=i .
$$

  **The ramified character takes the value of a quarter turn on the uniformiser $\sqrt{-7}$, and the archimedean component fixes that value.** This is the step $\sqrt{-7}=$ quarter turn $\times\sqrt7$ of `cm-lift.md` §1.5. Lane C found that step to be "absent" from the Euler factor, and it reappears here inside the local character.
- Consistency: $\psi_7(-1)=\varepsilon(-1)=-1=\psi_\infty(-1)$, and $\psi_7(7)=\psi_7(-1)\,\psi_7(\pi)^2=1$.
- Check B1 computes $\prod_v\psi_v(\alpha)$ for 301 elements $\alpha\in\mathcal O_K$, taking the unramified part from the prime factorisation of $(\alpha)$. The product is 1 to $7\times10^{-16}$. With $\psi_7(\pi)=-i$ instead, the 33 elements with odd $v_\pi(\alpha)$ fail.

**1.2 The twist (standard; values derived here).** $\psi'=\psi\cdot(\chi_{-3}\circ N_{K/\mathbb Q})$. The local components of $\chi_{-3}\circ N$ are:

- **at $\infty$:** $\chi_{-3,\infty}=\mathrm{sign}$ and $N(z)=|z|^2>0$, so trivial;
- **at 7:** $\chi_{-3,7}$ is unramified, with $\chi_{-3,7}(N\pi)=\chi_{-3,7}(7)=\bigl(\tfrac{-3}7\bigr)=+1$, so trivial on $K_7^\times$, and $\psi'_7=\psi_7$;
- **at a split $p\ne3$:** the sign $\chi_{-3}(p)$, i.e. lane C's half turn;
- **at 3:** 3 is inert, so $K_3=\mathbb Q_9$. On units, $\chi_{-3,3}\circ N=\eta$, where $\eta(u)=\bigl(\tfrac{Nu}3\bigr)$ is the quadratic character of $\mathbb F_9^\times$ (C1). On the uniformiser, $\chi_{-3,3}(N3)=\chi_{-3,3}(3)^2=1$. So $\psi'_3(3)=\psi_3(3)=\psi_u((3))=\bigl(\tfrac37\bigr)=-1$: the inert half turn of `cm-lift.md` §1.4.

## 2. The local epsilon factors

**2.1 Definition (standard, Tate's local functional equation, from memory).** For a test function $\Phi_v$ and a character $\chi_v$, let $Z(\Phi_v,\chi_v,s)=\int\Phi_v(x)\chi_v(x)|x|^s\,d^\times x$. Then

$$
Z(F\Phi_v,\chi_v^{-1},1-s)=\varepsilon_v(s,\chi_v,\psi_v)\,\frac{L_v(1-s,\chi_v^{-1})}{L_v(s,\chi_v)}\;Z(\Phi_v,\chi_v,s),
$$

and $\varepsilon_v(s)=\varepsilon_v(\tfrac12)\,N_v^{1/2-s}$, where $N_v$ is the norm of $\mathfrak f_v\mathfrak d_v$ (conductor times different).

- If $\chi_v$, $\psi_v$ and the measure are all unramified, $\varepsilon_v=1$.
- If $\chi_v$ is ramified, take $c$ of valuation $a(\chi_v)+d_v$. Then $\varepsilon_v(\tfrac12)=\chi_v(c)\cdot\tau$, where $\tau$ is the Gauss sum $N_v^{-1/2}\sum_{u}\chi_v^{-1}(u)\psi_v(u/c)$, normalised to modulus 1 (*standard*).
- Changing $c\mapsto cu$ multiplies $\chi_v(c)$ by $\chi_v(u)$ and $\tau$ by $\chi_v(u)^{-1}$. **So $\varepsilon_v$ is independent of the uniformiser, although neither factor is.**

At the centre the squeeze drops out, because $D_c$ is unitary. $\varepsilon_v(\tfrac12)$ is then the ratio of the centre overlaps of the Fourier-transformed state and the original state:

$$
\varepsilon_v(\tfrac12)=\frac{Z(F\Phi_v,\chi_v^{-1},\tfrac12)}{Z(\Phi_v,\chi_v,\tfrac12)}\qquad(\text{when }L_v(\tfrac12,\chi_v^{\pm1})\text{ agree, as here}).
$$

This is the definition of "gate phase" used below.

**2.2 The place 7 (proved here; checked B2–B4).** The local state is lane C's charged state $\Phi_7=\varepsilon\,1_{\mathcal O_7^\times}$. It is constant modulo $\mathfrak p=(\pi)$ and supported on $\mathcal O_7$, and $\psi_{K,7}$ has conductor $\mathfrak d^{-1}=\mathfrak p^{-1}$. So $F\Phi_7$ is $\mathfrak p^{-1}$-periodic and supported on $\mathfrak p^{-2}=\tfrac17\mathcal O_7$. For $y=t/7$:

$$
F\Phi_7(t/7)=\mathrm{vol}(\mathfrak p)\sum_{u\in\mathbb F_7^\times}\Bigl(\frac u7\Bigr)e^{2\pi iu\,\mathrm{Tr}(t)/7}
=7^{-3/2}\Bigl(\frac{\mathrm{Tr}\,t}7\Bigr)g_7,\qquad g_7=\sum_u\Bigl(\frac u7\Bigr)e^{2\pi iu/7}=i\sqrt7 .
$$

- Since $\mathrm{Tr}\,t\equiv2t\pmod{\mathfrak p}$ and $\bigl(\tfrac27\bigr)=1$, this is $\tfrac i7\Phi_7(t)$, that is,

$$
F\Phi_7=i\,D_7\Phi_7 .
$$

  The charged state is a Fourier eigenvector up to the squeeze by $7$, which generates $\mathfrak f\mathfrak d=\mathfrak p^2$, and the eigenphase is $i$.
- B3 verifies this identity on all 49 classes of $\mathfrak p^{-3}/\mathfrak p^{-1}$ by direct summation, to $6\times10^{-17}$, with the support on the shell $v=-2$ as stated.
- B4 sums the two zeta integrals shell by shell. It finds $Z(F\Phi_7,\chi^{-1},1-s)/Z(\Phi_7,\chi,s)=i\cdot49^{1/2-s}$ at $s=\tfrac12$, $0.3+0.7i$ and $1.7-0.4i$, to $10^{-15}$. So

$$
\varepsilon_7=i,\qquad N_7=49 .
$$

- In Tate's form: with $c=\pi^2=-7$ the Gauss phase is $-i$ and $\chi_7(\pi^2)=-1$; with $c=7$ the Gauss phase is $+i$ and $\chi_7(7)=+1$. The product is $i$ either way.

**2.3 The complex place (proved here; checked B5, B6).** The local state is $\Phi_\infty(z)=z\,e^{-2\pi|z|^2}$, the angular-momentum-1 Gaussian of `cm-lift.md` §2.2 at the self-dual width. Differentiate the self-duality $F[e^{-2\pi|z|^2}]=e^{-2\pi|w|^2}$ in $w$, treating $w$ and $\bar w$ as independent (Wirtinger derivative). The kernel is $e^{-2\pi i(zw+\bar z\bar w)}$, which gives

$$
F[z\,e^{-2\pi|z|^2}](w)=-i\,\bar w\,e^{-2\pi|w|^2}.
$$

- The trace pairing $\mathrm{Tr}(zw)$ sends angular momentum $\ell=1$ to $\ell=-1$, which is the $\chi^{-1}$ sector, as the local functional equation requires.
- In the Euclidean picture of two real modes (kernel $e^{-2\pi i(xu+yv)}$), the same state goes to itself: $F[z e^{-\pi|z|^2}]=-i\,z\,e^{-\pi|z|^2}$. This is the Hermite phase $(-i)^n$ with $n=1$, and the trace pairing $2(xu-yv)$ differs from it by the parity $y\mapsto-y$ of the second mode and a rescaling by 2.
- Check B5 confirms both by 2D quadrature to $7\times10^{-15}$.
- Check B6 computes the zeta integrals with $\chi_\infty=|z|/z$ and $L_\infty(s)=\Gamma_{\mathbb C}(s+\tfrac12)$ at two values of $s$ (to $10^{-26}$). It finds

$$
\varepsilon_\infty=-i,
$$

  and zero overlap with the wrong sector. That is Tate's $(\pm i)^{|\ell|}$ for $\ell=1$; the sign is set by $\psi_\infty=e^{-2\pi ix}$ (*standard* in form, value computed).

**2.4 The place 3 (proved here; checked C2–C4).**

- **49a1.** The state is the qunaught $1_{\mathcal O_3}$. With $\mathfrak d_3=1$ it satisfies $F1_{\mathcal O_3}=1_{\mathcal O_3}$ (C3), so $\varepsilon_3=1$. The half turn $\psi_3(3)=-1$ enters the Euler factor instead: $(1+3\cdot9^{-s})^{-1}$ motivically, $a_9=-3$ (A3).
- **441d1.** The state is $\Phi_3=\eta\,1_{\mathcal O_3^\times}$. The same computation as at 7, with $\mathbb F_9$ in place of $\mathbb F_7$, gives

$$
F\Phi_3(t/3)=\tfrac19\,\eta(t)\,g_9,\qquad g_9=\sum_{u\in\mathbb F_9^\times}\eta(u)e^{2\pi i\,\mathrm{Tr}(u)/3}=3,\qquad\text{so}\qquad F\Phi_3=+D_3\Phi_3 .
$$

  - The bare eigenphase is $+1$. By Hasse–Davenport $g_9=-g_3^2$, where $g_3=i\sqrt3$ is the quadratic Gauss sum of $\mathbb F_3$ (C2).
  - The zeta integrals then give the ratio $-9^{1/2-s}$ (C4). The sign is $\psi'_3(3)=-1$, the inert half turn evaluated on the squeeze. The control in C4 sets $\psi'_3(3)=+1$ and gets $+1$. So

$$
\varepsilon_3(\psi')=-1,\qquad N_3=9 .
$$

**2.5 Products (checked B7, C5, C7).**

$$
W(49\text{a}1)=\varepsilon_\infty\varepsilon_7=(-i)(i)=+1,\qquad W(441\text{d}1)=\varepsilon_\infty\varepsilon_7\varepsilon_3=(-i)(i)(-1)=-1,
$$

with conductors $\prod_vN_v=49$ and $49\cdot9=441$. These agree with `ellrootno` and `lfunrootres` exactly; the local values are exact algebraic numbers, computed to between 15 and 50 digits.

- An $L$-function assembled from the $a_n$ with these $N$ and $W$ passes `lfuncheckfeq` at $2^{-139}$ and $2^{-135}$; with $-W$ it fails ($2^{1}$, $2^{0}$).
- Independently of PARI's functional equation, lane C's overlap $f(iy)=\sum a_ne^{-2\pi ny}$ (3000 terms) satisfies $f(i/(Ny))=W\,N\,y^2f(iy)$ to 31.1 and 29.6 digits at $y=0.8/\sqrt N$ and $1.25/\sqrt N$. With $-W$ the relative error is 3.1.

**2.6 Over $\mathbb Q$ (standard bookkeeping; checked A2, C6).** PARI's local root numbers are those of the 2-dimensional representation $\mathrm{Ind}_K^{\mathbb Q}\psi$. They differ from the $K$-values by Langlands' $\lambda$-factors, $w_p=\lambda_p(K/\mathbb Q)\,\varepsilon_{\mathfrak p}(\psi)$:

| place | $\lambda_p$ | $\varepsilon$ over $K$ | $w_p$ over $\mathbb Q$ (PARI) |
|---|---|---|---|
| $\infty$ | $\varepsilon(\mathrm{sign})=-i$ | $-i$ | $-1$ |
| 7 | normalised Gauss sum of $\chi_{-7}$: $g_7/\sqrt7=i$ | $i$ | $-1$ |
| 3 (49a1) | 1 (unramified) | 1 | $+1$ |
| 3 (441d1) | 1 | $-1$ | $-1$ |

- $\prod\lambda_p=1$ is the root number of $\chi_{-7}$.
- Over $\mathbb Q$ the 3-adic sign of 441d1 has a second factorisation: $w_3=\varepsilon(\chi_{-3,3})^2\cdot\det\rho_3(\mathrm{Frob})=(i)^2\cdot1$. Here $\rho_3$ is 49a1's unramified 3-adic representation, with normalised Frobenius the quarter turn ($x^2+1$) and determinant 1. The local mode at 3 is 2-dimensional over $\mathbb Q_3$, so the $\mathbb F_3$ Gauss phase $i$ enters once per eigenline. Over $K$ the same $-1$ is (normalised $\mathbb F_9$ Gauss sum $+1$) $\times$ (half turn $-1$). Hasse–Davenport's sign is what converts one bookkeeping into the other.

## 3. The GKP reading

**3.1 Table (local identities proved here and checked; reading mine).**

| place $v$ of $K$ | local state $\Phi_v$ (49a1) | Fourier gate $F_v\Phi_v$ | $\varepsilon_v(\tfrac12)$ | change for 441d1 |
|---|---|---|---|---|
| split or inert $v\nmid 3\cdot7$ | qunaught $1_{\mathcal O_v}$ | $1_{\mathcal O_v}$ | $1$ | none (the step changes by $\chi_{-3}(p)$, the phase does not) |
| $3$ (inert) | qunaught $1_{\mathcal O_3}$ | $1_{\mathcal O_3}$ | $1$ | $\eta\,1_{\mathcal O_3^\times}\mapsto+D_3(\eta\,1_{\mathcal O_3^\times})$; $\varepsilon_3=\psi'_3(3)\cdot1=-1$ |
| $7$ (ramified) | charged $\varepsilon\,1_{\mathcal O_7^\times}$ | $i\,D_7(\varepsilon\,1_{\mathcal O_7^\times})$ | $i$ | none |
| $\infty$ (complex) | $z\,e^{-2\pi\lvert z\rvert^2}$, $\ell=1$ | $-i\,\bar z\,e^{-2\pi\lvert z\rvert^2}$ ($\ell=-1$) | $-i$ | none |
| product | | | $+1$ | $-1$ |

**3.2 The global statement (standard, Tate; the GKP phrasing proved here given the local identities).** The product state $\Phi=\bigotimes_v\Phi_v$ and the global gate $F=\bigotimes_vF_v$ give

$$
F\Phi=\Bigl(\prod_v\lambda_v\Bigr)\,D_c\,\Phi^\vee,\qquad c=(c_v)_v\ \text{(the finite idele }(7,3,1,1,\dots)\text{ for 441d1)},
$$

where $\lambda_v$ is the bare eigenphase and $\Phi^\vee$ is the same product with the archimedean factor conjugated ($\ell\to-\ell$).

- Poisson summation, $\langle\Theta_K,F\cdot\rangle=\langle\Theta_K,\cdot\rangle$, together with $FD_aF^{-1}=D_{a^{-1}}$ (`functional-equation-gate.md` §3), gives $Z(\Phi,\chi,s)=Z(F\Phi,\chi^{-1},1-s)$ globally, with no pole terms because $\chi\ne1$.
- The local identities then give $\Lambda(\psi_u,s)=\varepsilon(s)\Lambda(\bar\psi_u,1-s)$ with $\varepsilon(s)=W\,N^{1/2-s}$ and $W=\prod_v\lambda_v\chi_v(c_v)=\prod_v\varepsilon_v(\tfrac12)$. The squeeze $c$ accounts for $N$, and the phases for $W$.
- $L(\bar\psi_u,s)=L(\psi_u,s)$ because the $a_n$ are real, so $W=\pm1$ here. For a Dirichlet character of order 4 it is a genuine phase (D3).

**Status of the reorganisation.**

- Each local identity in the table is *proved here*, by finite Gauss sums or the Wirtinger computation, and *checked*.
- The global assembly is Tate's thesis (*standard*, from memory).
- The reading of $\varepsilon_v$ as "the phase the local Hadamard applies to the local charged state" is exact only modulo the squeeze $D_{c_v}$ and the sector flip at $\infty$. The uniformiser-independent object is $\lambda_v\chi_v(c_v)$, not $\lambda_v$ alone.

**3.3 Which states carry phases (proved here, elementary, from §2).**

- A qunaught $1_{\mathcal O_v}$ at a place where $\psi_v$ is unramified is exactly Fourier-invariant, so it contributes phase 1.
- At a place where only the additive character is ramified (the different, as at 7 for $\zeta_K$, or at 2 for $\mathbb Q(\sqrt2)$ in `adelic-gkp.md` §14.3), it contributes a squeeze and phase 1, because $\chi(c)=1$ for unramified $\chi$.
- A non-trivial phase needs a charged state (a ramified $\chi_v$) or a non-Gaussian archimedean state ($\ell\neq0$).

## 4. The twist, precisely

**4.1 What changes at 3 (proved here; checked A3, C3, C4).** For 49a1 the local mode at 3 carries the vacuum $1_{\mathcal O_3}$, which has phase 1. The half turn $\psi_3(3)=-1$ acts as a step on it and appears in the Euler factor. For 441d1 the twist multiplies $\psi_3$ by the even charge $\eta$, which is trivial on rational elements: $\chi_{-3,3}(N(\pm3))=1$. Three things follow.

- **The vacuum has no overlap any more.** $\int_{\mathcal O_3^\times}\eta=0$, so the local state must be the charged state $\eta\,1_{\mathcal O_3^\times}$. The Euler factor becomes 1 ($a_{3^k}=0$, A3) and the conductor picks up $N_3=9$.
- **The step at 3 is no longer an invariant.** On rational uniformisers, $\psi'_3(\pm3)=\psi_3(\pm3)=-1$, unchanged. But a general uniformiser $3u$ gives $\psi'_3(3u)=-\eta(u)$, so the "step" is $-3$ or $+3$ depending on the choice. Over $\mathbb Q$ the same is true of the Frobenius lift: for the uniformiser $3$ it is 49a1's quarter turn $F$ ($F^2=-3$), and for $-3$ it is $-F$, since $\chi_{-3,3}(-1)=-1$. **"$-3\to\pm3$" and "the quarter turn becomes its negative" are both uniformiser artefacts.** The inertia group now acts by $-1$, so no Frobenius-invariant line exists to step on.
- **The half turn has moved into the gate phase.** The invariant combination is $\varepsilon_3=\psi'_3(c)\times(\text{normalised Gauss sum at }c)=(-1)(+1)$ for $c=3$, or $(+1)(-1)$ for a $c=3u$ with $\eta(u)=-1$. **The half turn that 49a1 spends in its Euler factor, 441d1 spends in its gate phase.**

**4.2 Conclusion (proved here for this pair; the general form is *standard*).** 49a1 and 441d1 have the same lattice $\mathcal O_K$ and the same vacuum $J_K$. Up to the sign $\chi_{-3}(p)$ they have the same steps at every split $p$, and they have the same states and phases at 7 and $\infty$. They differ in one local state, at 3: a qunaught for one and a charged state for the other. Its gate phase, $-1$, is the whole difference between their root numbers. That datum is a vector in the Hilbert space $L^2(K_3)$ of the local mode, together with its Fourier eigenphase. It is not a property of $\mathcal O_K$ or $J_K$.

So `cm-lift.md`'s "local data up to sign" was too coarse. The negative finding of `cm-lift.md` §3.4 stands as stated, since it concerned lattice and vacuum. But the local data in the full sense (the local states with their charges) do contain the sign of the functional equation (*proved here*).

**4.3 What the gate phases do not see (negative finding, elementary).**

- $\varepsilon_v=1$ at every place where $\psi_v$ is unramified, so the twist's signs $\chi_{-3}(p)$ at the split primes do not enter $W$.
- Those signs do enter the zeros. The full sets of local components $\{\psi_v\}$ and $\{\psi'_v\}$ determine $L$, but only through the Euler product, not through any finite local datum.
- $W$ fixes the parity of $\mathrm{ord}_{s=1/2}$, which is why 441d1 is forced to have a central zero. It says nothing about the remaining zeros.

## 5. For the data ladder

1. *Checked (D4); standard.* For a curve of genus $g$ over $\mathbb F_q$, $Z(1/(qu))=q^{1-g}u^{2-2g}Z(u)$. Equivalently, $\xi(s)=q^{(g-1)s}Z(q^{-s})$ satisfies $\xi(s)=\xi(1-s)$: the root number is $+1$. In Tate's form $\varepsilon(s)=q^{(2g-2)(1/2-s)}=\prod_vq_v^{d_v(1/2-s)}$, a product of local squeezes by the canonical divisor, with every local phase equal to 1. Checked on the E mode over $\mathbb F_2$ and on lane E's genus-2 curve over $\mathbb F_5$.
2. *Checked (D5); standard (Ihara–Bass, Terras).* For a $(q+1)$-regular graph, $\Xi(s)=q^{n(s-1/2)}\det(1-Aq^{-s}+q^{1-2s})$ is exactly even about $\tfrac12$: sign $+1$. Terras's completion $\Lambda(u)=(1-u^2)^{m-n+n/2}(1-q^2u^2)^{n/2}\zeta(u)$ has sign $(-1)^n$, with principal branches. That is $+1$ for $K_4$ and $-1$ for $K_5$. The sign comes from the trivial factor and is a convention, not a product of local phases. The places of a graph (prime cycles) carry no Fourier gate.
3. *Checked (D1); standard.* For $\zeta$ every local state is Fourier-invariant: the Gaussian at $\infty$ and the qunaughts $1_{\mathbb Z_p}$. Every phase is 1 and $W=1$, so $\zeta$ has no non-trivial gate phase at all.
4. *Checked (D2, D3); standard.* For Dirichlet $L$-functions the phases sit at the conductor (normalised Gauss sums) and at $\infty$ ($-i$ for odd $\chi$, the Hermite phase of $x e^{-\pi x^2}$). For $\chi_{-3}$ they cancel ($i\cdot(-i)=1$). For the quartic character mod 5 their product is $0.8507+0.5257i$, PARI's root number.
5. *Proved here; checked.* For the CM rung the phases sit at the ramified prime 7 ($i$), at $\infty$ ($-i$) and at any twisting prime ($-1$ at 3 for 441d1).
6. *Heuristic.* On the ladder as recorded in `data-ladder.md` §0, the root number is the first global invariant assembled from local data that is not a lattice or vacuum datum: it is a product of Fourier eigenphases of local states.
7. *Heuristic.* So `data-ladder.md` should list "the local charged states and their gate phases" as an item of its own, next to lattice, step and vacuum. It is trivial on the finite rungs and for $\zeta$, and non-trivial from Dirichlet $L$-functions on.
8. *Negative finding.* The item determines only the sign of the functional equation. It does not determine the zeros (§4.3), so it does not touch what `data-ladder.md` §4 lists as absent for $\zeta$.

## 6. Remarks on existing pages

- `cm-lift.md` §2.4 says the S-gate "maps the angular-momentum-1 Gaussian to itself up to a phase". With the self-dual trace pairing on $K_\infty=\mathbb C$ it maps $\ell=1$ to $\ell=-1$ (§2.3). "To itself" holds in the Euclidean two-mode picture, which differs by the parity of the second mode. Imprecise rather than wrong; the phase is $-i$ in both pictures.
- `cm-lift.md` §2.4 and §1.5 say the charged state at 7 goes to "a Gauss-sum multiple of a squeezed copy of itself". This is confirmed, $F\Phi_7=i\,D_7\Phi_7$, and the squeeze accounts for $N=49$.
- The lane I brief speaks of "local steps that agree up to a sign at the primes dividing 3". `cm-lift.md` §3.4 correctly says "at every prime $p\neq3$". At 3, 441d1 has no invariant step (§4.1).
- The brief's ladder item for $\zeta$ ("one non-trivial phase only, at infinity") is not right as phrased. The phase at infinity is 1, so $\zeta$ has none.

## 7. Status and checks

| statement | status | check |
|---|---|---|
| root numbers $+1$, $-1$; local $w_p$ over $\mathbb Q$; Euler factor at 3 | checked (PARI) | A1–A3 |
| local components: $\psi_\infty=\lvert z\rvert/z$, $\psi_7\vert_{\mathcal O^\times}=\varepsilon$, $\psi_7(\sqrt{-7})=i$ | derived here; checked (301 elements) | B1 |
| $g_7=i\sqrt7$; $F\Phi_7=i\,D_7\Phi_7$; $\varepsilon_7=i$, $N_7=49$ | proved here; checked | B2–B4 |
| $F[z e^{-2\pi\lvert z\rvert^2}]=-i\,\bar z e^{-2\pi\lvert z\rvert^2}$; Euclidean Hermite phase $-i$; $\varepsilon_\infty=-i$ | proved here; checked | B5, B6 |
| $\eta$ quadratic on $\mathbb F_9^\times$; $g_9=3=-g_3^2$; $F\Phi_3=D_3\Phi_3$; $\varepsilon_3(\psi')=-1$, $N_3=9$; vacuum at 3 for 49a1 | proved here; checked | C1–C4 |
| $\prod_v\varepsilon_v=+1,-1$ equals `ellrootno` | checked (exact) | B7, C5 |
| $\lambda$-factors; $w_3=\varepsilon(\chi_{-3,3})^2\det F$ | standard; checked against PARI | C6 |
| functional equation with $W=\prod\varepsilon_v$, $N=\prod N_v$; fails with $-W$ | checked ($2^{-139}$, $2^{-135}$; theta form 31.1 / 29.6 digits) | C7 |
| global FE as Poisson summation times local phases | standard (Tate, from memory); GKP phrasing proved here given B–C | – |
| the twist moves the half turn from the Euler factor into the gate phase; the step at 3 is uniformiser-dependent | proved here | A3, C4 |
| the distinguishing datum lives in $L^2(K_3)$, not on $\mathcal O_K$ or $J_K$ | proved here (for this pair) | – |
| gate phases do not see the split-prime signs; $W$ fixes only the central parity | negative finding (elementary) | – |
| curves over $\mathbb F_q$: root number $+1$, squeezes only | standard; checked | D4 |
| graphs: $\Xi$ even; Terras's sign $(-1)^n$ ($K_4$: $+1$, $K_5$: $-1$) a convention | standard; checked | D5 |
| $\zeta$: all phases 1; Dirichlet: Gauss and Hermite phases | standard; checked | D1–D3 |
| the root number as a separate rung item of the data ladder | heuristic | – |

Checks: `checks/check_gate_phases.py`, 32 of 32 pass. Exact rational arithmetic in $K$ for the finite Fourier transforms; mpmath at 50 digits for the Gauss sums and at 25–30 digits for the archimedean zeta integrals and the theta functional equation; float64 for the 2D Fourier quadrature, the curves and the graphs; PARI at 38 digits.

## 8. Next

- Extend lane C's twist family: for each quadratic twist $\chi_d$ of 49a1, list the charged places and their phases. Check that $W$ is the product, and record which twists are forced to have a central zero by phases alone.
- Compute the phases for Hecke characters of $K$ with infinity type $\ell=2,3$. The Hermite phase should be $(-i)^{\ell}$, and the charge at 7 is forced only for odd $\ell$ (the parity argument of `cm-lift.md` §1.5).
- A finite shadow: a function-field $L$-function with a ramified twist (for example a quadratic twist of a curve over $\mathbb F_q$), where the root number is a product of local Gauss sums over finite fields. That would put the new ladder item on a finite rung.
- Fold the item "local charged states and their gate phases" into `data-ladder.md` §0 when the synthesis is next revised (not done here; existing pages untouched).
