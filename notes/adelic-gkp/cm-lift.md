# The CM lift: one lattice for every Euler factor, and the global zeros

Author: `claude:opus-5.5`, 2026-10-06, lane C of an orchestrated session.

Status: **a record, not a round; nothing registered in `db/claims.tsv`; no REFUTE review; no shard.** Each statement carries one of the labels *standard* (classical; quoted from memory, since `refs/src/` is absent in this container), *proved here*, *checked* (numerically, `checks/check_cm_lift.py`), *sketched*, *heuristic*, *open* or *negative finding*. Checks: `checks/check_cm_lift.py`, output `checks/output_cm_lift.txt` (50 of 50 pass; needs PARI/GP with elldata, about 15 s).

Conventions as in `adelic-gkp.md` and `lattice-tower.md`. $K=\mathbb Q(\sqrt{-7})$, $\mathcal O_K=\mathbb Z[w]$ with $w=\tfrac{1+\sqrt{-7}}2$ and $w^2=w-2$, $h_K=1$, $\mathcal O_K^\times=\{\pm1\}$, $d_K=-7$. The E mode is the step $M=\begin{pmatrix}0&-1\\2&-1\end{pmatrix}$ of `lattice-tower.md`, with characteristic polynomial $x^2+x+2$ and eigenvalues $\mu,\bar\mu$, $\mu=\tfrac{-1+\sqrt{-7}}2$. $L(E,s)$ is in PARI's (motivic) normalisation, with centre $s=1$; $s'=s-\tfrac12$ is the analytic variable, with centre $\tfrac12$; a zero is written $s=1+i\gamma$, i.e. $s'=\tfrac12+i\gamma$.

**Verdict.**

- **Which curve (checked).** 49a1 has $a_2=+1$. Its reduction mod 2 is the quadratic twist over $\mathbb F_2$ of the E mode, so its step at 2 is $-M$, the E mode composed with the half turn. The E mode itself is the reduction of **441d1**, the twist of 49a1 by $-3$: conductor $441=3^2\cdot7^2$, root number $-1$, analytic rank 1. I use 49a1 as the main example, because its only bad prime is the ramified prime 7, and I carry 441d1 through all the numerics.
- **One lattice, one vacuum (standard; checked).** Every split prime gives a step $\psi(\mathfrak p)\in\mathcal O_K$ of norm $p$ on the same lattice $\mathcal O_K$. These steps commute, and all of them preserve the same vacuum, the complex structure $J_K$ of $K\otimes\mathbb R=\mathbb C$. Over $K$ an inert prime gives the step $-p$, a half turn times a dilation. Over $\mathbb Q$, though, the inert Frobenius is a quarter turn that does not live on $\mathcal O_K$ (proved here).
- **The ramified prime carries a charge, and the charge is forced (proved here, elementary).** The archimedean test state has angular momentum 1, so it is odd under the global unit $-1$. Its overlap with the code therefore vanishes unless some finite place is odd too. For 49a1 that place is 7, where the vacuum is replaced by the Legendre-symbol state. This accounts for the second factor of 7 in the conductor $49=|d_K|\cdot7$.
- **Numerics (checked).** I computed the first 20 zeros of both curves and verified the functional equation to $2^{-135}$. The explicit formula in echo form has **no zero-mode term**. With prime kicks from the Hecke character alone (split primes up to $2\cdot10^6$), it reproduces the zero sums for five Gaussian packets to 15.1–15.7 digits, which is the float64 limit. The windowed Weil (Gram) form computed from the prime side is positive definite. With one made-up off-line pair it gets a negative eigenvalue ($-6.19$).
- **Negative finding (proved here; checked).** 49a1 and 441d1 share the lattice $\mathcal O_K$ and the vacuum $J_K$. At every split prime their steps agree up to the half turn $\chi_{-3}(p)=\pm1$. Their global zeros are different, and 441d1 has a zero at the centre. So the datum that makes local RH hold at every prime does not determine the global zeros. They depend on sign data that the vacuum cannot see.

---------------------------------------------------------------------------------------------------------------------

## 1. The curve and the character

**1.1 Which curve (checked A1–A4).**

| curve | Weierstrass $[a_1,a_2,a_3,a_4,a_6]$ | $j$ | conductor | root number | rank | $a_2$ | reduction mod 2 |
|---|---|---|---|---|---|---|---|
| E mode (over $\mathbb F_2$) | $[1,0,0,0,1]$ | 1 | – | – | – | $-1$ | itself: 4 points, $x^2+x+2$ |
| 49a1 | $[1,-1,0,-2,-1]$ | $-3375$ | 49 | $+1$ | 0, $L(1)=0.966656$ | $+1$ | $y^2+xy=x^3+x^2+1$, polynomial $x^2-x+2$ |
| 441d1 = 49a1 twisted by $-3$ | $[1,-1,1,-20,46]$ | $-3375$ | 441 | $-1$ | 1, $L'(1)=1.294559$ | $-1$ | the E mode ($j=1$, 4 points) |

- Over $\mathbb F_2$ the ordinary curves are $y^2+xy=x^3+ax^2+1$ with $a\in\{0,1\}$. They are the two quadratic twists with $j=1$, with traces $-1$ and $+1$ (*standard*). The E mode is $a=0$, and 49a1 reduces to $a=1$.
- Twisting by a quadratic character $\chi_d$ with $d$ odd multiplies $a_2$ by $\chi_d(2)$. That is $-1$ for $d\equiv5\pmod8$. The smallest conductor among these twists is $441$ ($d=-3$, or $d=21$ within the same isogeny class); $d=5$ gives 1225 (checked A4).
- Twisting by the CM discriminant $-7$ leaves every $a_p$ unchanged; the result is 49a3, in the same isogeny class (checked A4). That every elliptic curve over $\mathbb Q$ with CM by $\mathcal O_K$ is a quadratic twist of 49a1 or of its isogenous 49a2 is *standard* (from memory).
- **In the lattice:** $M$ and $-M$ differ by the half turn $-1\in\mathcal O_K^\times$, which commutes with everything here. Locally the choice costs nothing. Globally the sign at 2 costs an extra bad place (3, inert in $K$), a root number of $-1$ and a central zero.

**1.2 The character (standard; checked A5–A7).** $L(E/\mathbb Q,s)=L(\psi,s)$ with

$$
\psi((\alpha))=\varepsilon(\alpha)\,\alpha,\qquad \varepsilon(\alpha)=\Bigl(\frac{\alpha\bmod\sqrt{-7}}{7}\Bigr)\in\{0,\pm1\},
$$

defined on ideals prime to $\mathfrak f=(\sqrt{-7})$. The definition is consistent on ideals because $\varepsilon(-1)=\bigl(\tfrac{-1}7\bigr)=-1$, so $\varepsilon(-\alpha)(-\alpha)=\varepsilon(\alpha)\alpha$. **The sign of $\pi_p$ is therefore fixed by the character:** $\psi(\mathfrak p)$ is the one generator of $\mathfrak p$ that is a square modulo $\sqrt{-7}$. Concretely, write $4p=x^2+7y^2$ with $x,y>0$ (this representation is unique for split $p$; checked D0 for $p<2\cdot10^6$). Then

$$
a_p(49\text{a}1)=\Bigl(\frac x7\Bigr)x,\qquad a_p(441\text{d}1)=\Bigl(\frac p3\Bigr)\Bigl(\frac x7\Bigr)x ,
$$

with $a_p=0$ for inert $p$, for $p=7$, and for $p=3$ on 441d1. Both formulas agree with `ellap` for all 1229 primes below $10^4$ (A5). The Hecke theta series $\tfrac12\sum_{\alpha\in\mathcal O_K}\varepsilon(\alpha)\,\alpha\,q^{N\alpha}$ equals the $q$-expansion of 49a1 up to $n=3000$ (A7).

Split primes $p\le60$ (A6). The table lists one prime $\mathfrak p$ above each $p$; the other prime gets the complex conjugate. "arg" is $\theta_{\mathfrak p}/\pi$ with $\psi(\mathfrak p)=\sqrt p\,e^{i\theta_{\mathfrak p}}$, the local oscillator angle.

| $p$ | $\psi(\mathfrak p)$ | in the basis $1,w$ | $a_p$ (49a1) | $a_p$ (441d1) | arg |
|---|---|---|---|---|---|
| 2 | $\tfrac{1+\sqrt{-7}}2$ | $w$ | $+1$ | $-1$ | $+0.3850$ |
| 11 | $2+\sqrt{-7}$ | $1+2w$ | $+4$ | $-4$ | $+0.2940$ |
| 23 | $4+\sqrt{-7}$ | $3+2w$ | $+8$ | $-8$ | $+0.1860$ |
| 29 | $1+2\sqrt{-7}$ | $-1+4w$ | $+2$ | $-2$ | $+0.4405$ |
| 37 | $-3-2\sqrt{-7}$ | $-1-4w$ | $-6$ | $-6$ | $-0.6642$ |
| 43 | $-6-\sqrt{-7}$ | $-5-2w$ | $-12$ | $-12$ | $-0.8678$ |
| 53 | $-5-2\sqrt{-7}$ | $-3-4w$ | $-10$ | $+10$ | $-0.7410$ |

For 441d1 the character is $\psi'=\psi\cdot(\chi_{-3}\circ N)$, so $\psi'(\mathfrak p)=\bigl(\tfrac p3\bigr)\psi(\mathfrak p)$. At $p=2$ this gives $\psi'(\mathfrak p_2)=-w=\bar\mu$, the E mode exactly (B3).

**1.3 The E mode is multiplication by $\mu$ on $\mathcal O_K$ (checked B3).** On the basis $\{1,w\}$, multiplication by $a+bw$ is the integer matrix $\begin{pmatrix}a&-2b\\b&a+b\end{pmatrix}$. Multiplication by $\mu=w-1$ is conjugate to $M$ by $P=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$. This is the statement of `lattice-tower.md` §5 that the E-mode lattice in vacuum coordinates is $\mathbb Z[w]$, now with the arithmetic origin attached.

**1.4 Inert primes: a quarter turn over $\mathbb Q$, a half turn over $K$ (proved here; checked B4).** The inert primes are those with $\bigl(\tfrac p7\bigr)=-1$; below 60 they are $3,5,13,17,19,31,41,47,59$. For them $a_p=0$ and the Euler factor of $L(E,s)$ is $(1+p^{1-2s})^{-1}$.

- *Over $K$.* $(p)$ is a prime of norm $p^2$, and $\psi((p))=\bigl(\tfrac p7\bigr)p=-p$. The step is multiplication by $-p$ on $\mathcal O_K$. Normalised, it is the half turn $-1$: a lattice symmetry that commutes with $J_K$.
- *Over $\mathbb Q$.* Frobenius has polynomial $x^2+p$. Normalised, it is a quarter turn with eigenvalues $\pm i$, and it is a square root of the $K$-step, since $F_p^2=-p$. **It is not a step on $\mathcal O_K$ compatible with $K$.** A $K$-linear integral step is multiplication by some $\alpha\in\mathcal O_K$, and $x^2+p$ would need $\mathrm{tr}\,\alpha=0$ and $N\alpha=p$, i.e. $p=7b^2$ (proved; B4). A $K$-antilinear step $z\mapsto c\bar z$ has polynomial $x^2-|c|^2$, with real eigenvalues. As a step on some lattice $\mathbb Z^2$, for example $\begin{pmatrix}0&-1\\p&0\end{pmatrix}$, it has $S^2=-1$, so its only invariant vacuum is $S$ itself: the complex structure of $\mathbb Z[\sqrt{-p}]$, not $J_K$.
- These are the supersingular primes, the mode with $\lambda=0$. As `lattice-tower.md` §6 notes, the non-ordinary case falls outside Deligne's theorem.
- *Relation to `locks.md`* (*heuristic*). The quarter-turn lock there relates two different ordinary modes in $\mathbb Q(i)$, and that is not what happens here. Here a single mode with $\lambda=0$ is the fixed point of the half-turn lock $\lambda\leftrightarrow-\lambda$. The closer parallel is `locks.md` §4. There, on a bipartite graph, the step is a square root of Frobenius over $\mathbb F_{q^2}$, and the half-turn lock dissolves on passing to two steps. Here the inert step is a square root of the $K$-step $-p$, and passing to $K$ dissolves the quarter turn into a half turn.

**1.5 The ramified prime: a squeezed vacuum with a charge (standard / sketched; checked B5, A7).** $\mathfrak p_7=(\sqrt{-7})$, and $\sqrt{-7}=2w-1$ is an integral step of norm 7 that commutes with $J_K$: a quarter turn times $\sqrt7$. But $\varepsilon(\sqrt{-7})=0$, so $\psi$ is ramified at $\mathfrak p_7$, the Euler factor is 1 and $a_7=0$. The conductor is $49=|d_K|\cdot N\mathfrak f=7\cdot7$, and the two factors of 7 have different origins:

- **The different $\mathfrak d=(\sqrt{-7})$** is the squeezed vacuum of note §14.3. $1_{\mathcal O_7}$ is the qunaught of the asymmetric lattice $\mathcal O_7\times\mathfrak d_7^{-1}$, and since the exponent 1 is odd, no Fourier-symmetric $1_{\mathfrak a}$ exists (*standard*; the same argument as §14.3, where the exponent was 3).
- **The conductor $\mathfrak f$ of $\psi$** reflects a change of local state. The local test vector is no longer the vacuum. It is the charged state $\varepsilon_7(x)\,1_{\mathcal O_7^\times}(x)$, with the Legendre symbol acting through $\mathcal O_7^\times\to\mathbb F_7^\times$. Its Tate integral is independent of $s$, which gives the Euler factor 1. Its Fourier transform is a Gauss-sum multiple of a squeezed copy of itself, which gives the local root number (*standard*, Tate's local functional equation, from memory; not checked separately here).

**Why there must be a charge (proved here).** The global unit $-1\in K^\times$ fixes $\Theta_K$ and acts diagonally on every place. The archimedean state of angular momentum 1 (§2.2) is odd under $z\mapsto-z$. So the overlap of $\Theta_K$ with a product state vanishes identically, along the whole squeeze orbit, unless the finite part is odd under $-1$ as well. Check A7 shows the simplest instance: $\sum_{\alpha\in\mathcal O_K}\alpha\,q^{N\alpha}=0$.

*Sketched:* for a curve over $\mathbb Q$ the charge must sit at the ramified prime. Since $\psi$ takes values in $K$, $\varepsilon$ is quadratic. A quadratic character of $\mathbb F_{p^2}^\times$ is even on $-1$. A conjugation-stable charge at a split $p$ has the form $\varepsilon_1\times\varepsilon_1\circ\sigma$, which is even on $-1$. So the only place where an odd charge can sit is the ramified prime. The conclusion, that every curve over $\mathbb Q$ with CM by $\mathcal O_K$ has bad reduction at 7, is *standard*. For 441d1 the twist adds an even charge, $\chi_{-3}\circ N$, at the inert prime 3, and the Euler factor at 3 becomes 1.

## 2. The adelic GKP reading

**2.1 The code (standard; note §14.1).** $K\subset\mathbb A_K$ is discrete, cocompact and self-dual for $\psi_{\mathbb Q}\circ\mathrm{Tr}$. In the $\mathbb Q$-basis $\{1,w\}$ this makes $\Theta_K=\Theta\otimes\Theta$, the same two-mode adelic qunaught as for $\mathbb Q(\sqrt2)$. Projecting the finite places to their local states (vacua $1_{\mathcal O_p}$ for $p\ne7$, the charged state at 7) leaves the real two-mode qunaught on the lattice $\mathcal O_K\subset\mathbb C$, with dual lattice $\mathfrak d^{-1}=\tfrac1{\sqrt{-7}}\mathcal O_K$.

**2.2 One complex place (standard; phrasing mine).** $K_\infty=\mathbb C$. The positions $z=x+iy$ of the two real modes form one complex coordinate, and the idelic squeezes at infinity are $\mathbb C^\times=\mathbb R_{>0}\times U(1)$.

- **The radial squeeze** $z\mapsto rz$ is the norm direction, $|z|_{\mathbb C}=|z|^2$. RH is about this direction, as in note §14.2.
- **The rotation** $z\mapsto e^{i\phi}z$ is the "unit direction". For $\mathbb Q(\sqrt2)$ that direction was non-compact, and the unit $1+\sqrt2$ (a cat map) compactified it to a circle of length $R_K$. Here it is already a circle. The global units $\{\pm1\}$ act on it only by the half turn: **no cat map and no regulator**.
- **Hecke characters are the Fourier modes on that circle**, labelled by an angular momentum $\ell$; $\zeta_K$ is the sector $\ell=0$. The infinity type $(1,0)$ of $\psi$ is $\ell=1$; whether it reads $z$ or $\bar z$ is a sign convention.
- The archimedean test state is the angular-momentum-1 Gaussian $z\,e^{-2\pi y|z|^2}$, the first circular excitation of the two-dimensional isotropic oscillator, squeezed by $y$.

**2.3 $L(\psi,s)$ is the Mellin transform of the overlap (standard, Hecke/Tate from memory; checked A7, C3).** The overlap of the code with the product of these local states, along the radial squeeze, is the theta series

$$
f(iy)=\tfrac12\sum_{\alpha\in\mathcal O_K}\varepsilon(\alpha)\,\alpha\,e^{-2\pi y\,N\alpha}=\sum_{n\ge1}a_n e^{-2\pi ny},
$$

and

$$
\Lambda(s)=N^{s/2}\,\Gamma_{\mathbb C}(s)\,L(E,s)=2N^{s/2}\int_0^\infty f(iy)\,y^{s}\,\frac{dy}y,\qquad \Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s).
$$

Checked against PARI's `lfun` at $s=1$ and $s=1.3+2i$ to 13 digits (C3). The factor $\tfrac12$ comes from the half turn: $\alpha$ and $-\alpha$ give the same ideal. The rotation part of the squeeze is integrated out by the angular-momentum projection.

**The Gamma factor (standard).** In the analytic variable the Gamma factor is $\Gamma_{\mathbb C}(s'+\tfrac12)$. Compare $\zeta_K=\zeta\cdot L(\chi_{-7})$, whose factor is $\Gamma_{\mathbb R}(s)\Gamma_{\mathbb R}(s+1)=\Gamma_{\mathbb C}(s)$. **The angular momentum $\ell$ shifts the archimedean factor by $|\ell|/2$.**

**2.4 Functional equation (standard; checked C1, C2).** $\Lambda(s)=\varepsilon\,\Lambda(2-s)$, with $\varepsilon=+1$ for 49a1 and $\varepsilon=-1$ for 441d1. In $s'$ this is $s'\leftrightarrow1-s'$. On the overlap it reads

$$
f\bigl(i/(Ny)\bigr)=\varepsilon\,N\,y^2\,f(iy),
$$

checked for 49a1 at $y=0.08,\,0.12$ to $2\times10^{-21}$ (C2). PARI's `lfuncheckfeq` gives $2^{-139}$ (49a1) and $2^{-135}$ (441d1). In the code (*sketched*): the S-gate (Fourier) fixes $\Theta_K$. It maps the angular-momentum-1 Gaussian to itself up to a phase, since Hermite functions are Fourier eigenfunctions. It maps the charged state at 7 to a Gauss-sum multiple of a squeezed copy of itself. The squeeze accounts for $N$, and the product of the local phases is $\varepsilon$. I have not computed the local phases separately.

**2.5 Dictionary.**

| finite picture (`lattice-tower.md`) | CM example: one Euler factor | CM example: the global $L(\psi,s)$ |
|---|---|---|
| lattice $L=\mathbb Z^2$ | $\mathcal O_K$, the same for every $p$ (*standard*) | $\mathcal O_K$ appears only through the overlap $f(iy)$ |
| integral step $M$, $M^T\Omega M=q\Omega$ | $\psi(\mathfrak p)$ acting on $\mathcal O_K$ (split $p$); $-p$ (inert, over $K$); none at 7 (*checked B2, B4, B5*) | no single step; the $\psi(\mathfrak p)$ commute but, with $-1$, generate an infinitely generated group (one free generator per split prime) |
| invariant vacuum $J$ | $J_K$, the same for every split $p$ (*checked B2*) | the same $J_K$, which does not determine the zeros (§3.4) |
| zeros on $\lvert\mu\rvert=\sqrt q$ (local RH) | $\lvert\psi(\mathfrak p)\rvert=\sqrt p$, angle $\theta_{\mathfrak p}$ = oscillator frequency | GRH: zeros at $s'=\tfrac12+i\gamma$, $\gamma$ real (*open*) |
| counts $h_k=\det(1-M^k)$ | $\#E(\mathbb F_{p^k})=N(1-\psi(\mathfrak p)^k)=[\mathcal O_K:(1-\psi(\mathfrak p)^k)\mathcal O_K]$ (*standard*) | none; the counts belong to one prime at a time |
| tower $(1-M^k)L$, self-similar | one self-similar tower per split prime, all inside $\mathcal O_K$ | none |
| zeros = oscillator frequencies of $S=M/\sqrt q$ | frequencies $\theta_{\mathfrak p}$ | squeeze frequencies $\gamma$ at which the Mellin transform of every overlap profile in the $\ell=1$ sector vanishes; the $\theta_{\mathfrak p}$ enter only as phases of the prime kicks (§3.2) |
| Weil form $\tfrac12\Omega(M-V)$, positive | positive at every split $p$ for the same $J_K$ | Weil's functional of §3.3; positivity is GRH (*open*) |

**What has no global analogue** (*negative finding*, within this picture): a lattice whose step has the global zeros as eigenvalue phases; a periodic-point count whose zeta function is $L(\psi,s)$; and a vacuum whose existence implies the zeros. The global object in this picture is a Mellin transform along the radial squeeze. The lattice, the steps and the vacuum enter it only through the Euler product.

## 3. Numerics

**3.1 Zeros (checked C4).** Values of $\gamma$, i.e. $s=1+i\gamma$ (motivic) or $s'=\tfrac12+i\gamma$ (analytic). Each was verified by $|L(1+i\gamma)|<10^{-25}$ (the largest value was $3\times10^{-37}$). The zero counts below $T=70$ (75 for 49a1, 100 for 441d1 including $\gamma=0$) agree with $N(T)\approx\tfrac T\pi\log\tfrac{\sqrt N\,T}{2\pi e}$ to within 2.

| | first 20 zeros $\gamma>0$ |
|---|---|
| 49a1 | 3.457740, 5.086735, 6.478037, 8.498120, 9.489525, 11.308503, 12.279433, 13.558291, 14.367890, 15.256497, 16.914148, 17.589538, 18.933308, 19.892611, 21.085745, 22.036876, 22.847443, 23.469161, 24.705418, 25.492086 |
| 441d1 | $\gamma=0$ (simple), then 1.990687, 3.694984, 4.879149, 5.859345, 7.315046, 8.063481, 8.772289, 10.002161, 10.225577, 11.415262, 12.407372, 13.415103, 13.815652, 14.951187, 15.858625, 16.507437, 17.434017, 18.097020, 18.544250, 19.432609 |

**3.2 The explicit formula in echo form (standard, Weil/Guinand form for self-dual $L$-functions, from memory; checked D1).** Conventions as in `weil-positivity-spectroscopy.md` §§2–3: a packet $h$, its transform $H(E)$, $G(E)=H(E)\overline{H(\bar E)}$, $g(u)=\frac1{2\pi}\int G(E)e^{-iEu}dE$, and the echo $C_h(t)=\sum_\rho G(\gamma_\rho)e^{i\gamma_\rho t}$, summed over all zeros, both signs of $\gamma$, with multiplicity. Then

$$
C_h(t)=-\sum_{n}\frac{\Lambda_E(n)}{\sqrt n}\bigl[g(\log n-t)+g(-\log n-t)\bigr]
+\frac1{2\pi}\int G(E)\,e^{iEt}\bigl[\log N-2\log2\pi+2\,\mathrm{Re}\,\psi_\Gamma(1+iE)\bigr]dE ,
$$

with $\Lambda_E(p^k)=c(p^k)\log p$, where:

- split $p$: $c(p^k)=2\cos k\theta_p$, the oscillator angle of the step, times $\bigl(\tfrac p3\bigr)^k$ for 441d1;
- inert $p$: $c(p^k)=i^k+(-i)^k$, the quarter turn, i.e. kicks only at even $k$ with sign $(-1)^{k/2}$;
- bad $p$ (7, and 3 for 441d1): $c=0$.

$\psi_\Gamma$ is the digamma function.

- **There is no zero-mode term.** $L(\psi,s)$ is entire because $\psi$ is not trivial (*standard*). The pair $2\cosh(t/2)$ of the zeta case is absent. This is the first difference from $\zeta$.
- *In the language of $K$-places (sketched).* The kick at log-squeeze $m\log N\mathfrak P$ carries the phase $\bigl(\psi(\mathfrak P)/\sqrt{N\mathfrak P}\bigr)^m=e^{im\theta_{\mathfrak P}}$. This is the character, on the angular-momentum-1 sector, of the rotation that accompanies the squeeze. So each prime term is a local squeeze trace (Lefschetz at the origin, note §10) weighted by a rotation phase. For an inert $\mathfrak P=(p)$ the phase is $(-1)^m$, the half turn.

Results: zero list up to $T=70$ from PARI; prime side from the Hecke character alone (§1.2), with $n\le2\cdot10^6$ (74434 split primes).

| curve | packet $(E_0,\tau)$ | values of $t$ | $C_h(0)$ | of which primes | of which real place | max $\lvert$difference$\rvert$ | digits |
|---|---|---|---|---|---|---|---|
| 49a1 | (12, 0.25) | 6 | 2.29132074 | $+0.019980$ | $+2.271341$ | $1.8\times10^{-15}$ | 15.1 |
| 49a1 | (20, 1) | 2 | 10.27829387 | $-0.722790$ | $+11.001083$ | $5.8\times10^{-15}$ | 15.2 |
| 49a1 | (2, 0.6) | 2 | 1.12751934 | $-0.414269$ | $+1.541789$ | $2.2\times10^{-16}$ | 15.7 |
| 441d1 | (10, 0.25) | 4 | 3.10545345 | $+0.035886$ | $+3.069567$ | $9.5\times10^{-16}$ | 15.5 |
| 441d1 | (1, 0.6) | 2 | 3.43404428 | $+0.453047$ | $+2.980998$ | $1.3\times10^{-15}$ | 15.4 |

The agreement is at the float64 limit. The packet at $E_0=2$ is where, for $\zeta$, the zero-mode term was needed ($+0.88$ against a total of about 0; `weil-positivity-spectroscopy.md` §3). Here no such term enters and the sum closes. For 49a1 the real-place density $\frac1{2\pi}[\log49-2\log2\pi+2\,\mathrm{Re}\,\psi_\Gamma(1+iE)]$ is negative for $|E|<0.757$, and the primes pay for that. For 441d1 the density is positive everywhere ($+1.26/2\pi$ at $E=0$).

**3.3 The windowed Weil form (checked E1, E2).** For an $L$-function without poles, Weil's criterion reads: GRH for $L(\psi,s)$ $\iff$ $\sum_\rho G(\gamma_\rho)\ge0$ for every $G=H\overline{H(\bar\cdot)}$ (*standard*, from memory). There is no exceptional pair to remove. In the language of note §10, the squeeze correlation functional of the $\ell=1$ sector, with nothing removed, would be a state.

- **Gram form from the prime side** (as check V3). The Toeplitz matrix $[C_h(t_j-t_k)]$ with $t_j=0.35j$, $j<14$, and the packet $(E_0,\tau)=(20,0.25)$ was computed from the place side only. It is Hermitian and positive definite, with eigenvalues in $[0.101,\,7.216]$. The echo stays below its initial value on $[0,6]$; for $t\ge0.5$ the ratio is at most 0.540. For 441d1 with $E_0=10$ the eigenvalues lie in $[0.106,\,11.229]$.
- **One off-line pair** (as check V4). Replace $\gamma=19.8926,\ 21.0857$ (and their negatives) by $20.4892\pm0.5i$ (and their negatives).
  - In the Weil (evaluation) form the smallest eigenvalue becomes $-6.19$, and the echo grows to 2.70 times its initial value.
  - In the Lorentzian form of width 0.5 the Gram matrix stays positive (smallest eigenvalue $+0.102$).
  - The pair contributes $2\,\mathrm{Re}\,z\bar w$, a block of signature $(1,1)$ (note §10, C6).

**3.4 Same vacuum, different zeros (proved here; checked A5, B2, C4).** At every prime $p\ne3$, 441d1 has the same step as 49a1 up to the half turn $\bigl(\tfrac p3\bigr)$: $\psi'(\mathfrak p)=\pm\psi(\mathfrak p)$. Both curves therefore act on the same lattice $\mathcal O_K$ and preserve the same $J_K$, and their local Weil forms are positive for the same reason. Their zero lists nonetheless differ (§3.1), and only one of them vanishes at the centre. **The global zeros depend on the pattern of signs $p\mapsto\pm1$, a character of the primes, which the vacuum cannot see, since $-1$ commutes with everything.**

## 4. What this example says about the data for $\zeta$

In the finite case the datum that carries RH is a vacuum invariant under the integral step on a lattice (`lattice-tower.md` §5). In the CM case the same lattice $\mathcal O_K$ and the same vacuum $J_K$ handle every Euler factor at once, so local RH comes free at every prime (*standard*). The global zeros are a different kind of object. They are frequencies of the Mellin transform of the overlap along the radial squeeze, and in this picture there is no lattice behind them. §3.4 shows that the local data, taken up to half turns, do not determine them (*negative finding*).

This sits awkwardly with `lattice-tower.md` §7.3, which proposes to read zeros as oscillator frequencies and to assign the squeeze to the poles. In the CM case the oscillator frequencies are the local angles $\theta_{\mathfrak p}$. The global zeros are squeeze frequencies, and there are no poles. So the two readings describe different levels, and the closest understood intermediate case gives no support for transferring the §7.3 reading to the global object (*heuristic*).

*Open*, in six sentences:

1. Is there a lattice with an integral step, or a commuting family of steps, whose periodic-point counts have $L(\psi,s)$, or its completed form, as their zeta function, so that the global zeros become oscillator frequencies of one step?
2. If so, its invariant vacuum would have to see the sign character of §3.4, which no vacuum of $\mathcal O_K$ does.
3. Is there an integral structure (a lattice) on Connes's cokernel for the $\ell=1$ sector of $\mathcal O_K$, on which the radial squeeze acts as a similitude?
4. Do the $\ell$-towers of Hecke characters of one $K$ (note §14 Reading) carry a positivity statement uniform in $\ell$?
5. Does 441d1's forced central zero (root number $-1$) have a GKP meaning as a parity of the code with the charged local states?
6. Which of these questions has a finite-field shadow that can be checked first?

## 5. Status and checks

| statement | status | check |
|---|---|---|
| E mode: $a_2=-1$, polynomial $x^2+x+2$; 49a1 has $a_2=+1$ and reduces to the twist ($-M$) | standard; checked | A2, A3 |
| 441d1 = 49a1 twisted by $-3$ lifts the E mode; conductor 441, $\varepsilon=-1$, rank 1; twist by 5 gives 1225 | checked (PARI) | A4 |
| all CM-by-$\mathcal O_K$ curves over $\mathbb Q$ are twists of 49a1/49a2 | standard (from memory) | – |
| $\psi((\alpha))=\varepsilon(\alpha)\alpha$, $\varepsilon$ the Legendre symbol mod $\sqrt{-7}$; $a_p=(x\vert7)x$; theta series | standard; checked for $p<10^4$, $n\le3000$ | A5–A7 |
| the sign of $\pi_p$ is fixed by $\varepsilon(-1)=-1$ | standard; checked | A6 |
| one lattice and one vacuum $J_K$ for all split steps; steps commute | standard; checked | B1, B2 |
| E mode $\cong$ multiplication by $\mu$ on $\mathcal O_K$ | checked (explicit $P$) | B3 |
| inert Frobenius: quarter turn, not $K$-compatible on $\mathcal O_K$; over $K$ the half turn $-p$ | proved here; checked $p\le60$ | B4 |
| parallel with `locks.md` §4 (square root of Frobenius) | heuristic | – |
| ramified 7: different (squeeze) plus charge; Euler factor 1 | standard / sketched | B5 |
| the charge is forced by the parity of the $\ell=1$ state | proved here (elementary); instance checked | A7 |
| the charge must sit at the ramified prime (for curves over $\mathbb Q$) | sketched | – |
| $L(\psi,s)$ as Mellin transform of the $\ell=1$ overlap; $\Gamma_{\mathbb C}$ | standard (Hecke, Tate; from memory); checked | C3 |
| functional equation; theta-overlap form | standard; checked | C1, C2 |
| local phases of the S-gate (Hermite phase, Gauss sum) give $\varepsilon$ | sketched; not computed | – |
| first 20 zeros of 49a1 and 441d1; zero counts | checked (PARI) | C4 |
| explicit formula without zero-mode term; Hecke-character prime side | standard; checked, 15.1–15.7 digits | D0, D1 |
| Weil's criterion for entire self-dual $L$ | standard (from memory) | – |
| windowed Gram form PSD; off-line pair gives $-6.19$; Lorentzian stays PSD | checked | E1, E2 |
| same lattice and vacuum, different global zeros (49a1 vs 441d1) | proved here / checked | A5, B2, C4 |
| §4 reading against `lattice-tower.md` §7.3 | heuristic | – |
| §4 questions | open | – |

Checks: `checks/check_cm_lift.py`, 50 of 50 pass. Exact integer arithmetic for the lattice checks; PARI at 38 digits for the curves, zeros and $L$-values; mpmath at 20 digits for the theta overlap; float64 for the explicit formula and the Gram matrices.

## 6. Next

- Compute the local S-gate phases (the Hermite phase at $\infty$, the Gauss sums at 7 and, for 441d1, at 3) and confirm that their product is the root number.
- Repeat §3.4 across the whole family of quadratic twists of 49a1. Record which sign characters give a central zero, and whether anything in the code distinguishes them.
- Run the explicit formula and the Gram form for $\ell=2,3$ (Hecke characters of higher infinity type of the same $K$). This is the uniform-in-$\ell$ question of §4.
- A finite analogue of §3.4: two Frobenius families on one lattice that agree up to signs, compared through their global zeta functions over a function field. That would be the place to test question 1 of §4.
