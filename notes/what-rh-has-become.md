# What the Riemann hypothesis has become

Written 2026-09-11 for TJO, after the founding conversation. Everything here uses only the ingredients built up there: the one determinant identity, permutations and their cycles, the small matrix, graphs, MPS transfer matrices, and the explicit formula. Nothing in this document is new mathematics; it is a translation.

## 0. The one identity, and the two readings of it

For any matrix $M$ with eigenvalues $\lambda_1,\dots,\lambda_N$,

$$
\frac{1}{\det(1-uM)} \;=\; \prod_{i}\frac{1}{1-\lambda_i u} \;=\; \exp\Big(\sum_{n\ge1}\frac{\operatorname{Tr}(M^n)}{n}\,u^n\Big).
$$

The middle expression is a bosonic partition function, one mode per eigenvector, Boltzmann factor $\lambda_i u$. The right expression is a sum over closed walks of length $n$, with the $1/n$ of a ring's rotation symmetry. So one object has two descriptions: a **gas of modes** labelled by eigenvalues, and a **gas of rings** labelled by closed walks. Call them side B and side A. The whole subject is the tension between them.

When $M$ is a permutation matrix, the ring side is very concrete: $\operatorname{Tr}(M^n)$ counts fixed points of $\sigma^n$, the closed walks are the cycles and their repeats, and

$$
\frac{1}{\det(1-uM)} = \prod_{\text{cycles } c}\frac{1}{1-u^{|c|}},
$$

a Bose gas with one mode per cycle and energy = cycle length. That is the Euler product, and the primes will be the cycles.

## 1. RH for a finite permutation: automatic

A permutation matrix permutes an orthonormal basis, so it is unitary, so every eigenvalue satisfies $|\lambda| = 1$. That is the RH analogue at this level, and it is free.

## 2. RH for an infinite permutation: a statement about a *different* matrix

For infinitely many cycles, the permutation matrix is still unitary and still useless: roots of unity with infinite multiplicity. The fixed-point counts $\operatorname{fix}(\sigma^n) = \sum_{d\mid n} d\,c_d$ still make sense. The interesting question is whether there is a **small matrix** $M_{\text{small}}$, not a piece of the permutation matrix, with

$$
\operatorname{Tr}\big(M_{\text{small}}^n\big) = \operatorname{fix}(\sigma^n)\quad\text{for all } n .
$$

It exists exactly when the zeta function is rational, and then its eigenvalues $\lambda_i$ are new numbers, not on the unit circle. The largest one, $\lambda_{\max}$, is the growth rate of the counts. The RH analogue is:

> every other nonzero eigenvalue has $|\lambda_i| = \sqrt{\lambda_{\max}}$.

Two shift examples from the conversation: the 4-symbol cyclic rule has eigenvalues $2,\ 1\pm i,\ 0$ and satisfies it; the golden-mean shift has $\varphi,\ -1/\varphi$ and does not. Both are perfectly good infinite permutations. So at this level RH is a *property some systems have*, and it is about the sizes of the subleading eigenvalues relative to the leading one.

**What it says on the counting side.** Write the fixed-point counts as leading term plus fluctuation:

$$
\operatorname{fix}(\sigma^n) = \lambda_{\max}^n + \sum_{i\ge2}\lambda_i^n .
$$

RH says the fluctuation has size $(\sqrt{\lambda_{\max}})^n = \sqrt{\lambda_{\max}^n}$: the square root of the leading term. That is the size of the fluctuation of a sum of $\lambda_{\max}^n$ independent coin tosses. So RH, in counting language, says **the cycle counts fluctuate no more than a random sequence would**. This is the single most useful sentence in the document; every later version of RH is this sentence in a different costume.

## 3. RH for a graph: Ramanujan

For a $(q+1)$-regular graph, the permutation is the shift on non-backtracking closed walks, the small matrix is the vertex adjacency matrix $A$, and Ihara's formula compresses one to the other. Each eigenvalue $\lambda$ of $A$ produces a pair $\mu,\mu'$ of eigenvalues of the walk-counting matrix through

$$
\mu^2 - \lambda\mu + q = 0, \qquad\text{so}\qquad \mu\mu' = q .
$$

The leading eigenvalue $\lambda = q+1$ gives $\mu = q$ and $\mu' = 1$. For the others, the constraint $\mu\mu' = q$ leaves two possibilities:

- $\lambda^2 < 4q$: the pair is complex conjugate, $|\mu| = |\mu'| = \sqrt q$. On the critical circle.
- $\lambda^2 > 4q$: the pair is real, one bigger than $\sqrt q$ and one smaller. Off it.

So RH for the graph $\iff$ $|\lambda| \le 2\sqrt q$ for all nontrivial $\lambda$ $\iff$ the graph is Ramanujan. Three remarks that carry over to the primes:

1. **The pairing comes from a symmetry, RH from a bound.** $\mu\mu' = q$ is a functional equation; it pairs eigenvalues symmetrically about $\sqrt q$ on a logarithmic scale. RH is the extra statement that each pair is *degenerate in modulus*, which happens iff it is a conjugate pair.
2. **Self-adjointness is not enough.** $A$ is symmetric, so $\lambda$ is real always. That guarantees the pairing, not the bound. The prism graph $C_{16}\times K_2$ is symmetric and fails RH.
3. **Geometric meaning of the bound.** $[-2\sqrt q, 2\sqrt q]$ is the spectrum of the infinite tree covering the graph. RH says the finite graph has no eigenvalue outside the spectrum of its universal cover. "Tempered" is the word for this.

Counting version: the number of closed non-backtracking walks of length $n$ is $q^n + O(q^{n/2})$, square-root fluctuation, exactly section 2.

## 4. RH for an MPS: one correlation length

Now the channel $\Phi(\rho) = \sum_i A_i\rho A_i^\dagger$ is the transfer matrix $E$ of a matrix product state, $\operatorname{Tr}E^n = \langle\psi_n|\psi_n\rangle$ is the norm of the periodic state on $n$ sites, and the zeta function is the generating function of ring norms. In canonical form $E$ has leading eigenvalue $1$ and the rest inside the unit disc,

$$
\lambda_k = e^{-1/\xi_k + i\theta_k},
$$

with $\xi_k$ the correlation lengths. Then

$$
\langle\psi_n|\psi_n\rangle = 1 + \sum_k e^{-n/\xi_k}\,e^{in\theta_k}.
$$

Translate the graph statement, where leading growth is $q$ per step and subleading modulus $\sqrt q$. In normalised units the subleading modulus is $q^{-1/2}$, so $e^{-1/\xi} = q^{-1/2}$, so

$$
\xi = \frac{2}{\log q} = \frac{2}{\text{entropy per site}} .
$$

So RH for an MPS reads:

> all correlation lengths are equal, and equal to twice the inverse entropy rate.

The frequencies $\theta_k$ are unconstrained, and there may be infinitely many of them; only the moduli are pinned. There is a two-level hierarchy that will reappear for the primes:

| statement about $E$ | name | counting meaning |
|---|---|---|
| a unique eigenvalue on the unit circle | primitivity (Perron–Frobenius) | ring norms $\sim$ leading term |
| all others inside a smaller circle | spectral gap | fluctuation exponentially smaller than leading |
| all others on **one** circle of radius $e^{-1/\xi}$, $\xi = 2/h$ | Ramanujan / RH | fluctuation is square-root of leading |

## 5. The primes: continuous time, and the sign

For the primes the cycle lengths are $\log p$, rationally independent, so the "matrix" becomes a semigroup $e^{LT}$ in a continuous length $L$, and ring norms become a measure in $L$. Here is the whole content of the explicit formula in that language. Start from the Riemann–von Mangoldt formula for the prime-power counting function $\psi(x) = \sum_{n\le x}\Lambda(n)$, valid for $x$ not a prime power:

$$
\psi(x) = x - \sum_{\rho}\frac{x^{\rho}}{\rho} - \log 2\pi - \tfrac12\log\!\big(1-x^{-2}\big).
$$

Put $x = e^{L}$ and differentiate in $L$. The left side becomes a sum of delta functions, one per prime power, of weight $\log p$. The right side becomes a sum of exponentials:

$$
\sum_{n}\Lambda(n)\,\delta(L-\log n) \;=\; e^{L} \;-\; \sum_{\rho} e^{\rho L} \;-\; \big(e^{-2L} + e^{-4L} + \cdots\big).
$$

Read it as $\operatorname{Tr} e^{LT}$ for a generator $T$ whose eigenvalues are: $1$ (the pole of $\zeta$, the leading term, entropy $1$), every zero $\rho$, and the trivial zeros $-2,-4,\dots$. This is the trace identity of section 0 with $M^n$ replaced by $e^{LT}$: **ring side = prime powers at lengths $\log n$, mode side = zeros.** The 3000-zero computation in `ringnorm.py` is this identity checked numerically.

Two features are visible immediately.

**The sign.** The zeros enter with a minus sign relative to the leading term. In the elliptic-curve case the same minus sign marks the $H^1$ block, the fermionic one; in Connes's language it is the absorption spectrum. In MPS language the total measure is still positive, because $\Lambda(n)\ge0$, but the subleading sector of the bond space contributes negatively, so whatever the state is, its bond space is graded, not plainly bosonic.

**The pairing.** The functional equation $\xi(s)=\xi(1-s)$ says $\rho$ and $1-\rho$ are both zeros. In normalised rates, dividing by the leading $e^{L}$, the mode $\rho$ decays like $e^{-(1-\beta)L}$ and its partner $1-\rho$ like $e^{-\beta L}$, where $\rho = \beta + i\gamma$. So

$$
\text{decay rates come in pairs } (1-\beta,\ \beta) \text{ summing to } 1,
$$

exactly as $\mu\mu' = q$ paired the graph eigenvalues around $\sqrt q$. This is the symmetry, and it is a theorem. RH is the extra statement:

> every pair is degenerate, $\beta = 1-\beta = \tfrac12$.

So, in the four languages of sections 2 to 4:

| language | the Riemann hypothesis says |
|---|---|
| counting | $\psi(x) = x + O(x^{1/2+\epsilon})$: the prime powers fluctuate like coin tosses |
| small matrix | every subleading mode has modulus $\sqrt{\text{leading}}$ |
| MPS | the state whose rings are the primes has **one** correlation length, $\xi = 2$ (entropy is $1$), and an infinite tower of frequencies $\gamma_n$ |
| channel | the transfer semigroup has a single uniform decay rate $\tfrac12$ |

And the hierarchy of section 4 becomes classical number theory:

| statement about $T$ | number theory |
|---|---|
| unique eigenvalue with $\operatorname{Re}=1$ | $\zeta(1+it)\ne0$, the prime number theorem |
| all zeros in $\operatorname{Re}\,s < 1-\delta(t)$ | the zero-free region, $\psi(x) = x + O(x e^{-c\sqrt{\log x}})$ |
| all zeros on $\operatorname{Re}\,s = \tfrac12$ | RH |

## 6. The Hilbert space where this is literally true

There is a concrete Hilbert space on which the channel version is a theorem, not an analogy. Take the scattering symbol of the modular surface, in the Mellin variable $\tau$ of the dilation group,

$$
S(\tau) = \frac{\xi(1-2i\tau)}{\xi(1+2i\tau)} .
$$

It is unimodular on the real line and analytic and contractive in the lower half plane, with zeros exactly at $\tau_n = \gamma_n/2 - i\beta_n/2$. Being inner, it defines a model space $K_S = H^2\ominus S H^2$, and the dilation group compressed to $K_S$ is a contraction semigroup $Z(t)$ with one mode per zero:

$$
Z(t)^*\,k_n = \exp\!\Big(-\tfrac{\beta_n}{2}\,t - i\,\tfrac{\gamma_n}{2}\,t\Big)\,k_n .
$$

The factor $\tfrac12$ everywhere is the doubling in the variable $2i\tau$; in the undoubled variable of section 5 the rates are $\beta_n$ and the frequencies $\gamma_n$. This is Lax–Phillips, and the statement "RH $\iff$ every mode of $Z(t)$ decays at the same rate" is Faddeev–Pavlov (1972). So the MPS/channel version of RH is not a metaphor: there is a bond space and a transfer semigroup, and RH is its Ramanujan property.

What the conversation added is where $S$ comes from. Its phase is

$$
\arg S(\tau) = 2\sum_{p}\sum_{k\ge1}\frac{p^{-k}}{k}\sin(2k\tau\log p) + (\text{Gamma phase}),
$$

which is the imaginary part of the Bost–Connes Lévy exponent at the critical temperature $\beta = 1$: the BC gas at its phase transition, with the divergent real part thrown away and only the phase kept. So the ring gas (Bost–Connes, side A) and the transfer semigroup (Lax–Phillips, side B) are one object seen from its two ends, and the bridge is the critical phase.

## 7. Why it is still hard, in this language

The graph example is the honest guide. There, side B exists for every graph, the trace identity holds for every graph, the small matrix is symmetric for every graph, and most graphs fail RH. Ramanujan-ness is never a consequence of the structure; it is an extra fact, and in every known case it comes from arithmetic input of Deligne's type. For Selberg's surfaces the same statement, no Laplace eigenvalue below $\tfrac14$, is open. So:

- **What the new language settles.** RH is a statement about the *sizes* of the subleading modes of a transfer semigroup, not about the existence of the semigroup. The semigroup exists (section 6). The zeros are its modes. The primes are its rings. The functional equation is the pairing of rates. None of this is in doubt.
- **What it does not settle.** A mechanism forcing the pairs to be degenerate. In positivity form (Weil, Connes): RH $\iff$ the zero-side function $F(u) = \sum_\rho e^{(\rho-1/2)u}$ is positive-definite on the dilation group $\iff$ its spectral measure $\sum_\rho\delta_{t_\rho}$ is a positive measure on the real line, which by Bochner is the same as all $t_\rho$ real. In MPS words: **RH says the entanglement Hamiltonian of the state whose rings are the primes is Hermitian.** Proving it means exhibiting that state, or a Stinespring form of $Z(t)$ with the prime dilations as Kraus operators, in a way that makes the positivity manifest. That is the open question the repo isolates, and the graph lesson says the Kraus structure alone will not do it; some arithmetic rigidity has to enter, playing the role weights play for curves.

## 8. One-paragraph summary

A zeta function is one partition function with two Fock-space descriptions: a gas of rings (cycles, closed walks, prime powers) and a gas of modes (eigenvalues of a small transfer matrix). The trace identity links them. For the primes the rings have lengths $\log n$ and weights $\Lambda(n)$, the modes are the zeros of $\zeta$ plus the pole, and the functional equation pairs the modes' decay rates as $(\beta, 1-\beta)$. The Riemann hypothesis says every pair is degenerate at $\tfrac12$: the transfer semigroup has one correlation length, $\xi = 2$, so the ring counts fluctuate by no more than the square root of their size, so the primes are as regular as coin tosses. That semigroup exists explicitly (Lax–Phillips), its scattering symbol is the phase of the Bost–Connes system at its critical temperature, and RH is the statement that this channel is Ramanujan.
