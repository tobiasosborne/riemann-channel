# The Riemann channel: Bost–Connes at $\beta = 1$, compressed

Scratch note, 2026-09-11. Exploratory; not part of the Phantasm SOP, nothing here is registered. Scripts in the session scratchpad: `scat.py`, `ringnorm.py`, `bcmpo.py`, `qihara.py`.

## 1. Setting

Mellin variable $\tau$ on the dilation group $\mathbb{R}_+^\times$; dilation by $e^{t}$ acts on $L^2(\mathbb{R}_+^\times)$ as the multiplier $e^{it\tau}$. Completed zeta

$$
\xi(s) = \tfrac12\, s(s-1)\, \pi^{-s/2}\, \Gamma(s/2)\, \zeta(s).
$$

Lax–Phillips scattering symbol for the modular surface, in this variable:

$$
S(\tau) = \frac{\xi(1-2i\tau)}{\xi(1+2i\tau)}.
$$

## 2. Facts established (analytic; checked numerically in `scat.py`)

**(a) Unimodular on the line.** $|S(\tau)| = 1$ for real $\tau$, since $\xi$ is real on the real axis. Checked at four points to machine precision.

**(b) Inner in the lower half plane.** For $\operatorname{Im}\tau < 0$ the denominator's argument $1+2i\tau$ has real part $> 1$, inside the Euler product, so $S$ is analytic there. Contractive: $|S| = 0.93,\ 0.54,\ 0.83,\ 0.27$ at four interior points.

**(c) Zeros.** The zeros of $S$ in $\operatorname{Im}\tau<0$ are at

$$
\tau_n = \frac{\gamma_n}{2} - i\,\frac{\beta_n}{2}, \qquad \rho_n = \beta_n + i\gamma_n \text{ a zeta zero}.
$$

Found by root search for $n = 1,\dots,6$ at $\gamma_n/2 - 0.25\,i$ with $|S(\tau_n)| < 10^{-19}$.

**(d) Phase identity.** For real $\tau$, $S(\tau) = \exp(-2i \arg \xi(1+2i\tau))$, and

$$
-\arg\zeta(1+2i\tau) = \sum_{p}\sum_{k\ge1} \frac{p^{-k}}{k}\,\sin(2k\tau\log p).
$$

The right side is the imaginary part of the Bost–Connes Lévy exponent $\psi_\sigma(\tau') = \log\zeta(\sigma - i\tau') - \log\zeta(\sigma)$ at the critical temperature $\sigma = 1$, $\tau' = 2\tau$. The real part of $\psi_1$ diverges ($\sum_p p^{-1} = \infty$, the BC phase transition); the imaginary part converges conditionally, at prime-number-theorem strength ($\zeta(1+it)\neq0$). Checked with primes below $3\cdot10^6$ plus the PNT tail $\pi/2 - \operatorname{Si}(2\tau\log X)$:

| $\tau$ | exact | prime sum + tail | residual |
|---|---|---|---|
| 0.7 | $+0.80572$ | $+0.80469$ | $-1.0\cdot10^{-3}$ |
| 1.9 | $-0.03879$ | $-0.03854$ | $+2.5\cdot10^{-4}$ |
| 4.2 | $-0.17233$ | $-0.17306$ | $-7.3\cdot10^{-4}$ |
| 9.0 | $+0.06468$ | $+0.06594$ | $+1.3\cdot10^{-3}$ |
| 15.5 | $-0.06432$ | $-0.06409$ | $+2.3\cdot10^{-4}$ |

## 3. The compressed semigroup (Sz.-Nagy–Foias functional model)

Since $S$ is inner in the lower half plane, the model space $K_S = H^2 \ominus S\,H^2$ carries the compressed dilation semigroup

$$
Z(t) = P_{K_S}\, e^{it\tau}\big|_{K_S}, \qquad t>0 .
$$

By Adamyan–Arov this is unitarily the Lax–Phillips semigroup of the modular surface with the cusp forms removed.

**Eigenvectors.** For each zero $\lambda$ of $S$, the reproducing kernel $k_\lambda(\tau) = (\tau - \bar\lambda)^{-1}$ lies in $K_S$ (it is orthogonal to $S H^2$ because $S(\lambda)=0$), and

$$
Z(t)^*\, k_\lambda = e^{-it\bar\lambda}\, k_\lambda, \qquad \lambda = \frac{\gamma_n}{2} - i\frac{\beta_n}{2}
\;\Longrightarrow\;
\text{eigenvalue } \exp\!\Big(-\frac{\beta_n}{2}\,t - i\,\frac{\gamma_n}{2}\,t\Big).
$$

Decay rate $\beta_n/2$, frequency $\gamma_n/2$, one mode per zero. Hence

> **RH $\iff$ every mode of $Z(t)$ decays at the single rate $1/4$** (Faddeev–Pavlov 1972, Lax–Phillips 1976).

This is the "one correlation length / Ramanujan" criterion of the MPS discussion, on an explicit Hilbert space.

**CP lift.** $\Phi_t(X) = Z(t)^* X Z(t)$ on $B(K_S)$, a single Kraus operator, sub-unital. Its Stinespring/unitary dilation is the automorphic wave group; the environment is the pair of incoming/outgoing subspaces, i.e. the cusp.

## 4. Where the primes are

Two placements, and they are different objects.

**Holevo-form covariant semigroup** on $L^2(\mathbb{R}_+^\times)$ with von Mangoldt jump measure $\nu_\sigma = \sum_{p,k} \frac{p^{-k\sigma}}{k}\,\delta_{k\log p}$: its symbol is

$$
\Big(\frac{\zeta(\sigma - i\tau)}{\zeta(\sigma)}\Big)^{t} = \exp\Big( t \sum_{p,k}\frac{p^{-k\sigma}}{k}\big(e^{ik\tau\log p} - 1\big)\Big),
$$

a genuine Markov semigroup for $\sigma>1$ (Khinchin: the zeta distribution is compound Poisson). It has no zeros for $\sigma>1$, and at $\sigma = 1/2$ it is not a semigroup at all (the symbol is unbounded). The BC phase transition $\sigma = 1$ is the finite-/infinite-activity threshold of $\nu_\sigma$.

**Compressed semigroup** $Z(t)$ on $K_S$: zeros as resonances, no jump structure; the primes enter only through $S$, and by (d) $S$ is the *phase* of the critical BC Lévy exponent.

**Bridge.** Take the BC process at $\beta = 1$, discard the divergent real part of its Lévy exponent, keep the phase, use that unimodular function as the characteristic function of a contraction semigroup. The functional model of that phase has the zeta zeros as its spectrum:

$$
\text{Lax–Phillips} \;=\; (\text{Bost–Connes at } \beta=1) \;+\; (\text{Sz.-Nagy–Foias}).
$$

## 5. Ring norms: the trace of the semigroup is the prime measure

Distributionally, $\operatorname{Tr} Z(t) = \sum_n e^{-t\beta_n/2 + it\gamma_n/2}$; under RH this is $e^{-t/4}\sum_n e^{it\gamma_n/2}$, and the explicit formula turns the zero sum into a prime sum. In the variable $u = t/2$, with a window $\hat g$ and its transform $g$,

$$
\sum_{\gamma} \hat g(\gamma) = \hat g(\tfrac i2) + \hat g(-\tfrac i2) - g(0)\log\pi + \frac{1}{2\pi}\int \hat g(r)\, \operatorname{Re}\psi\!\big(\tfrac14 + \tfrac{ir}{2}\big)\,dr - 2\sum_{n} \frac{\Lambda(n)}{\sqrt n}\, g(\log n).
$$

So $\operatorname{Tr}Z(t)$ is supported at ring lengths $t = 2\log n$ with weight $\Lambda(n)\,n^{-1/2}$; after the $e^{-t/4} = n^{-1/2}$ decay of the modes this is the $\sigma=1$ Lévy measure $\nu_1$ weighted by jump length, $\Lambda(n)/n$.

## 6. Numerical ring-norm test (`ringnorm.py`)

First 3000 zeros ($\gamma_{\max} = 3533.3$), window $\hat g(r) = \cos(ru)\,e^{-r^2/2G^2}$ with $G = 1009.5$ (truncation weight at $\gamma_{\max}$ is $2\cdot10^{-3}$). Numeric side: $F(u) = \sum_{\gamma>0} e^{-\gamma^2/2G^2}\cos(\gamma u)$ on $u\in[0.3,\,3.3]$. Prediction: every term of the explicit formula above, including the archimedean digamma integral. The prime terms are Gaussian dips of depth $\frac{G}{2\sqrt{2\pi}}\,\Lambda(n)\,n^{-1/2}$ at $u = \log n$.

| $n$ | $\log n$ | $F(u_n)$ | prediction | ratio | $\Lambda(n)/\sqrt n$ |
|---|---|---|---|---|---|
| 2 | 0.6931 | $-97.95$ | $-98.13$ | 0.998 | 0.490 |
| 3 | 1.0986 | $-126.83$ | $-127.02$ | 0.999 | 0.634 |
| 4 | 1.3863 | $-68.77$ | $-68.94$ | 0.998 | 0.347 |
| 5 | 1.6094 | $-143.66$ | $-143.86$ | 0.999 | 0.720 |
| 7 | 1.9459 | $-146.71$ | $-146.92$ | 0.999 | 0.736 |
| 8 | 2.0794 | $-47.87$ | $-48.03$ | 0.997 | 0.245 |
| 9 | 2.1972 | $-72.19$ | $-72.36$ | 0.998 | 0.366 |
| 11 | 2.3979 | $-143.86$ | $-144.07$ | 0.999 | 0.723 |
| 13 | 2.5649 | $-141.21$ | $-141.41$ | 0.999 | 0.711 |
| 16 | 2.7726 | $-32.88$ | $-33.03$ | 0.995 | 0.173 |
| 27 | 3.2958 | $-39.93$ | $-40.09$ | 0.996 | 0.211 |

Maximum $|F - \text{prediction}|$ over the whole interval: $0.20$, against dip depths up to $147$; the residual is flat ($0.18$ away from the dips) and is the truncation of the zero sum. Depths scale as $\Lambda(n)/\sqrt n$, prime powers included.

**Reading.** The primes are the ring spectrum of the Riemann channel, the zeros are its transfer spectrum, and one identity, the explicit formula, links them. In the MPS dictionary: rings of length $\log n$ with weight $\Lambda(n)$, transfer generator with eigenvalues $-\tfrac12 \pm i t_\rho$ (in the undoubled variable), single correlation length iff RH.

## 7. What is and is not established

**Established** (theorem-level, standard, numerically confirmed here):

- $S$ is inner in the lower half plane with zeros at $\gamma_n/2 - i\beta_n/2$.
- The functional-model semigroup $Z(t)$ has modes decaying at rate $\beta_n/2$ with frequency $\gamma_n/2$; RH $\iff$ single rate $1/4$.
- $S(\tau) = \exp\big(2i\sum_{p,k} p^{-k}\sin(2k\tau\log p)/k\big)\cdot(\text{Gamma phase})$: the scattering symbol is the phase of the critical BC Lévy exponent.
- The distributional trace of $Z(t)$ is the prime measure with weights $\Lambda(n)\,n^{-1/2}$.

**Not established, and not claimed:**

- RH itself. Everything here is equivalent to, not a proof of, the uniform-rate statement.
- A Stinespring form of $Z(t)$ with the prime dilations as Kraus/jump operators. The single-Kraus lift exists trivially. A Holevo-form covariant Lindbladian with the von Mangoldt jump measure lives on the full regular representation, has symbol $\zeta^t$, and is not the compressed object. Whether a jump-type generator on $K_S$ reproduces $Z(t)$ is the open question this note isolates; its physical index would be the Stinespring environment.
- Any identification with the Phantasm constructions SP-PRIME and SP-BC-CONTROL. Those are $\beta>1$ objects; the channel here is a $\beta=1$ phase compressed to a co-invariant subspace. The prime-chain MPO computation (`bcmpo.py`) showed the bond space of the BC phase operators $e(a/b)$ is $\mathbb{Z}/b$ with Dirichlet-character transfer eigenvalues $L(\beta,\bar\chi)/\zeta(\beta)$; the analogous bond space for the compressed semigroup is $K_S$.
