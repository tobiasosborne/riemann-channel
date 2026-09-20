# A physicist's picture: resonances, cusps, and Lindblad dynamics

Author: `claude:opus`. Date 2026-09-20. Exposition lane, no new claims.

TJO asked for a BSc-level, physicist-friendly visualisation of the cusp-graph language
(resonances, cusps, bound states, zeros, poles), as close as possible to the situation at hand,
with the physics connecting resonances and Lindblad dynamics.

Nothing here is new. Textbook facts are labelled **standard (textbook)**; notebook facts carry
claim ids and `report/sections/<file>`; worked examples come from the graph-scattering preprint
`refs/src/2603.26443/final_draft.tex`, cited by line; corrections found in this lane's numerics
are cited as `notes/cusp-graph/numerics.md` ledger rows (D1, D4, ...).

---

## 0. The one-paragraph version

A finite graph with an infinite ray attached is a **cavity coupled to a single-mode waveguide**:
the ray is the guide (the "cusp"), the finite graph the cavity, and `R` is what comes back out.
Poles of `R` inside the unit disc are **bound states** (trapped); zeros inside are **resonances**
(leaky, Gamow states); cavity eigenstates with a node at the junction never couple to the guide —
the **cusp forms**, i.e. **dark states**. The guide carries one propagating mode, so the cavity
has a **one-dimensional exit**: that is all "the exit is the cusp" means
(`lem:exit-one-dimensional`). Project onto the cavity and the guide becomes a complex self-energy,
the Hamiltonian becomes non-Hermitian, its complex eigenvalues are the resonances. Put the leaked
quantum back as a **reset** and you have a Lindbladian: no-jump contraction plus reinsertion. RH
says **every resonance of one particular cavity has the same linewidth**.

---

## 1. The textbook problem

### 1.1 Setup

Take the classic: a particle on the half-line `x >= 0` with a potential well near the wall.
Standard (textbook): outside the well `psi(x) = e^{-ikx} + R(k) e^{+ikx}`, `E = hbar^2k^2/2m`, and
the **reflection coefficient** `R(k)` is everything the well does to the wave — one complex number
per momentum.

The discrete version is the one we want. Put the particle on a chain, hopping `1`, and let the
well be a finite weighted graph `X` (the "core") glued at one site `v_0` to a semi-infinite chain
`r_1, r_2, ...` with coupling `c`:

```
   (finite core X)       c          1        1        1
   o--o--o--o--[v_0]---------[r_1]----[r_2]----[r_3]---- ... --> infinity
      cavity                  the ray = the cusp = the waveguide
```

The Hamiltonian is the adjacency operator `T = T_X (+) T_ray + c(|v_0><r_1| + |r_1><v_0|)`, with
`(T g)(r_k) = g(k+1)+g(k-1)` for `k >= 2` and `(T g)(r_1) = g(r_2) + c g(v_0)`.

Standard (textbook). On the free chain `z^{-k}` solves `T g = lambda g` when

    lambda = z + 1/z ,     z = e^{i theta} on the unit circle,     lambda = 2 cos theta .

So `z` is the discrete `e^{ik}` and `lambda` the discrete energy. The **band** `[-2,2]` is the
continuum — the energies at which a wave can actually travel up the ray. Outside the band `z` is
real with `|z| < 1` and `z^k` decays: **bound states**.

### 1.2 The reflection coefficient and unitarity

Make the ansatz `g(r_k) = z^{-k} + R(z) z^{k}` (incoming plus reflected), match at the junction
and eliminate the core. With `G(lambda) = <v_0|(lambda - T_X)^{-1}|v_0>` ("how much the cavity
responds at the port"),

    R(z) = (1 - c^2 G(lambda)/z) / (c^2 G(lambda) z - 1) ,

or in determinant form (`numerics.md` D1: the brief's determinant form was off by a sign; the
power of `z` is zero):

    R(z) = - p(z)/ptilde(z) ,
    p(z)      = det( (1+z^2) I - z T_X - c^2 P_0 ) ,
    ptilde(z) = det( (1+z^2) I - z T_X - c^2 z^2 P_0 ) = z^{2n} p(1/z) ,    P_0 = |v_0><v_0| .

Three facts, standard (textbook) in the continuum and proved for the graph in this lane:

1. **Unitarity.** `|R(z)| = 1` on `|z| = 1`: nothing is absorbed, whatever goes in comes out. `R`
   is a pure phase, `R = e^{2 i delta(theta)}`, `delta` the **scattering phase shift**.
2. **The functional equation.** `R(z) R(1/z) = 1`, i.e. `R(-k) = 1/R(k)`; with reality
   `R(zbar) = conj R(z)` this is the usual `R(k)^* = R(-k^*)`. Reversing the incoming wave undoes
   the reflection. *This is the same statement as `xi(s) = xi(1-s)` on the zeta side.*
3. **Reality.** `R` has real coefficients: poles and zeros are real or in conjugate pairs.

### 1.3 Bound states are poles, resonances are zeros

Standard (textbook). Continue `R` off the real-momentum axis. Two kinds of singularity appear.

**Bound states.** Poles on the positive imaginary `k` axis, `k = i kappa`: there
`e^{ikx} = e^{-kappa x}` decays, so "reflected wave with no incoming wave" is a normalisable
state. In the disc variable, `z` real with `|z| < 1`, ray wavefunction `z^k`: exactly the `l^2`
eigenvalues of `T` outside the band (C2(i); `numerics.md` D4 sharpens it to *those whose
eigenfunction does not vanish at `v_0`*, the rest being dark — below).

**Resonances.** Poles on the *second sheet*: complex `k` with `Im k < 0`, complex energy
`E_0 - i Gamma/2`. The wavefunction is the **Gamow state**: purely outgoing,

    psi(x) ~ e^{ikx}, k = k_0 - i gamma  =>  |psi(x)| ~ e^{+gamma x} (grows in space),
    psi(t) ~ e^{-i E_0 t/hbar - Gamma t/2hbar}                        (decays in time).

The growth in space is not pathological: it is the record of a particle that left long ago, when
the state was more populated. In the disc variable the resonance branch continues the *outgoing*
solution `z^{-k}`, which for `|z| < 1` grows up the ray — the Gamow behaviour — and the resonances
are the zeros of `R` inside `|z| < 1` (C2(iv)). So:

```
     .-----------.     rim |z| = 1 : the band, real momenta, |R| = 1, pure phase
   /   x  x   x    \    x = resonance   (zero of R)   -> leaky, decays as |z|^m
  |  o      x   o   |   o = bound state (pole of R)   -> trapped, no decay
   \    x   x     /     distance in from the rim = the width
     `-----------'
```

### 1.4 Breit-Wigner, time delay, Levinson

Standard (textbook). Near an isolated resonance at `E_0` of width `Gamma`,
`R(E) ~ (background)*(E-E_0-i Gamma/2)/(E-E_0+i Gamma/2)`, unimodular, with the phase sweeping
`2 pi` as `E` crosses `E_0`: the **Breit-Wigner** line shape. The **Wigner time delay** is

    tau(E) = hbar d(2 delta)/dE = -i hbar d log R/dE = hbar Gamma/((E-E_0)^2 + Gamma^2/4) ,

a Lorentzian of height `4 hbar/Gamma`: a narrow resonance holds the particle a long time.
**Levinson**: the total phase winding counts bound states,
`delta(0) - delta(infinity) = n_bound * pi`. All three survive the translation, prettily:

* The Breit-Wigner factor is a **Blaschke factor**: `R(z) = - prod_i (z-z_i)/(1-z_i z)` over the
  roots of `p` (`numerics.md` D13). A factor with `|z_i| < 1` is unimodular on the rim and winds
  once — one resonance, one bump; one with `|z_i| > 1` is an *inverse* Blaschke factor, a pole
  inside, a bound state. (So `R` is **not** inner; `R` times the Blaschke product over the bound
  states is, and that is the characteristic function of the Lax-Phillips contraction `Z`.)
  Hence **Levinson in graph clothing**: winding = zeros minus poles inside, so the winding of `R`
  on `|z| = 1` is (number of resonances) - (number of bound states).
* The **time delay is the trace formula's cusp term**: `-z d/dz log R(z)` is what T2(b) calls
  the cusp contribution, where a comb over primes (monic irreducibles, in the function-field
  round) has to live. *The primes sit in the Wigner time delay.*

### 1.5 The dictionary

| textbook scattering | graph / cusp language | what it is physically |
|---|---|---|
| `e^{ik}` | `z` | one step of propagation along the guide |
| `E = hbar^2k^2/2m` | `lambda = z + 1/z = 2 cos theta` | energy; band `[-2,2]` is the continuum |
| half-line tail `x > a` | the ray `r_1, r_2, ...` = the cusp | the single-mode waveguide |
| potential well | the finite core `T_X` | the cavity |
| coupling to the tail | `c`, with `c^2 = q+1` for a tree quotient | port transmission; see 1.6 |
| threshold `k = 0` | `z = +1`, `lambda = +2` | bottom of the band: wave stops propagating |
| threshold `k = pi` (lattice) | `z = -1`, `lambda = -2` | top of the band = the **bipartite twin** |
| `|R| = 1` on real `k` | `|R| = 1` on `|z| = 1` | unitarity, no absorption |
| `R(-k) = 1/R(k)` | `R(z) R(1/z) = 1` | the functional equation |
| bound state, pole at `k = i kappa` | pole of `R` in `|z| < 1` | trapped, normalisable, no decay |
| resonance, second-sheet pole | zero of `R` in `|z| < 1` | Gamow state: leaks at rate `-log|z|` |
| Breit-Wigner factor | Blaschke factor `(z - z_i)/(1 - z_i z)` | one bump, one `2 pi` of phase |
| Wigner time delay | `-z d/dz log R` | the cusp term of the trace formula |
| Levinson winding | winding of `R` on `|z| = 1` | counts resonances minus bound states |
| embedded eigenvalue | **cusp form**: eigenvector of `T_X` with a node at `v_0` | dark state, invisible to `R` |
| scattering matrix `S(s)` of the modular surface | `phi = 1/R` (`numerics.md` D7) | `xi(2s-1)/xi(2s)` |

### 1.6 What the weight `c^2 = q+1` is doing

A hyperbolic cusp is a funnel whose cross-section **shrinks geometrically** as you go up it; the
discrete model (Serre) is the ray on which every `Lambda_n`, `n >= 1`, sends `q` edges *down* and
one *up*, the invariant measure falling like `q^{-n}`. Two consequences:

* **Only one transverse mode propagates.** A wave going up a shrinking guide falls below cutoff
  in every transverse channel except the constant (angle-independent) one — which is why the
  **exit is one-dimensional** (`lem:exit-one-dimensional`): one function of one variable leaves
  through a cusp (T1(a)).
* **The geometric measure becomes a coupling.** After the unitary `g = m^{1/2} f` flattening the
  measure, the shrinking guide becomes an ordinary uniform chain and the whole effect of the
  shrinking is absorbed into the junction weight `c^2 = q+1` (C1; `numerics.md` D2, which also
  corrects the junction measure to `m_0 : m_1 = q : (q+1)`).

So: **cusp = single-mode guide, `c^2 = q+1` = impedance of the port.** `h` cusps give an `h x h`
scattering matrix (T8). *The exit counts cusps, never resonances.*

---

## 2. From scattering to Lindblad

### 2.1 Feshbach: integrate out the waveguide, get a non-Hermitian cavity

Standard (textbook). Split with projectors `P` (cavity) and `Q = 1-P` (waveguide); write
`H|psi> = E|psi>` in blocks and eliminate the `Q` part:

    H_eff(E) = P H P + P H Q (E - Q H Q)^{-1} Q H P  =  T_X + Sigma(E) P_0 ,

with `Sigma(E) = c^2 g(E)`, `g(E)` the Green's function of the *isolated* ray at its end site.
Five lines for `g`:

    1.  g = <r_1|(lambda - T_ray)^{-1}|r_1> .
    2.  Deleting site r_1 from the ray leaves the same semi-infinite ray. (self-similarity)
    3.  Dyson:  g = 1/(lambda - 1*g*1)  =>  g^2 - lambda g + 1 = 0 .
    4.  With lambda = z + 1/z the two roots are  g = z  and  g = 1/z .
    5.  On the band, z = e^{i theta}: Im(1/z) = -sin theta < 0, so the RETARDED (outgoing) root is
        g = 1/z, and the other root g = z is the decaying/bound branch.

Hence `Sigma_res = c^2/z` (outgoing/retarded: the resonances) and `Sigma_bound = c^2 z`
(decaying: the `l^2` bound states), which is exactly C2(iv) of the brief with a physical reading —
the two branches of a square root, i.e. the two sheets. The effective Hamiltonian

    H_eff = T_X + (c^2/z) P_0 ,      resonances: det(lambda - H_eff(lambda)) = 0 ,

is **non-Hermitian**, because `Im Sigma < 0` on the band: the port leaks, and its complex
eigenvalues are the resonances. Sanity check on the pure cusp (`T_X = [0]`, `c^2 = q+1`): the
bound branch gives `z+1/z = (q+1)z`, `z = +-q^{-1/2}` — the Perron eigenvalue `(q+1)/sqrt q` and
its bipartite twin; the outgoing branch gives `z = +-q^{1/2}`, outside: **no resonances** (C3).

**Wide-band limit.** Near the band centre `theta ~ pi/2`, `Sigma ~ -i c^2` is energy independent,
so `H_eff = T_X - i c^2 P_0 = H - (i/2) L^dagger L` with `L = sqrt(2) c |out><v_0|`: with no extra
assumption we have landed on the **Lindblad no-jump generator**.

### 2.2 Quantum jumps: a Lindbladian is a contraction plus a reset

Standard (textbook: Monte-Carlo wavefunction / quantum trajectories). Unravel
`d rho/dt = -i[H,rho] + L rho L^dagger - (1/2){L^dagger L, rho}` as follows:

    |psi> --no-jump exp(-i H_eff t), norm decreases--> ...jump!... --reset to Omega--> |psi>

* **No-jump evolution** is `exp(-i H_eff t)`, `H_eff = H - (i/2)L^dagger L`: a contraction, not
  unitary, whose eigenvalues are the resonances.
* **The norm is the survival probability**: `||psi(t)||^2` = nothing detected yet.
* **The waiting-time density between jumps** is the rate at which that leaks,
  `w(t) = -d/dt ||exp(-i H_eff t)psi||^2` — the **exit flux**; in the notebook the holding-time
  law `m_Omega(t) = -d/dt Tr(C_t Omega C_t^*)` (`def:rebound-renewal-generator`).
* **The jump is the detection of the leaked quantum**; what puts the state back is
  `L rho L^dagger` with `L = |omega><j|`, i.e. `<j|rho|j> * Omega = (flux) * Omega`.

So a Lindbladian **is** a no-event semigroup plus a rebound:

    L_Omega(rho) = B^* rho + rho B + fl(rho) Omega ,    fl(rho) = <j|rho|j> ,
    discrete:      E_Omega(rho) = C rho C^* + <j|rho|j> Omega ,

exactly the Siemon-Holevo-Werner structure of `def:rebound-renewal-generator` and
`thm:rebound-renewal` (`04h_rebound_state.tex`), and the renewal channel of T3. The
one-dimensional exit `1 - C^*C = |j><j|` says there is one jump operator, i.e. **one detector**,
because there is one cusp.

### 2.3 The concrete cavity

A single cavity mode `a` at frequency `omega_0` leaking into a waveguide at rate `kappa`, with a
repump that reinjects a photon in a chosen state.

```
    repump (reset to Omega) --> [ cavity omega_0 ] --kappa--> waveguide (one mode)
```

* `H_eff = (omega_0 - i kappa/2)a^dagger a`: in the one-excitation sector the **resonance** is
  `omega_0 - i kappa/2` — oscillation `omega_0`, amplitude decay `kappa/2`, intensity `kappa`.
* **No-jump**: the norm decays, waiting-time density `w(t) = kappa e^{-kappa t}`. **Jump**: a
  photon is counted and the repump resets the mode to `Omega`.
* **Stationary state**: the balance of decay and reset,
  `rho_inf = (1/mu) int_0^infty C_t Omega C_t^* dt`, `mu` the **mean holding time**
  (`thm:rebound-renewal`(ii)). Nothing is stationary unless the mean waiting time is finite.

Discrete time is identical with `C` for `e^{-iH_eff t}` and
`mu_Omega = sum_m Tr(C^m Omega C^{*m})` (T3(b)).

### 2.4 The absorption spectrum, and RH as equal linewidths

The resonances are the eigenvalues of the no-jump generator: the complex frequencies at which the
cavity rings. Connes's phrase for the zeros — **absorption** spectrum rather than emission — is
recorded verbatim in `cit:connes-absorption` (`report/sections/04b_phantasm_forced.tex`), and this
is its cavity meaning: not lines the cavity emits, but **dips in the reflected light**,
frequencies at which the wave is absorbed, held for `~1/Gamma`, and re-emitted with a `2 pi` phase
slip — exactly a Breit-Wigner dip in `R`.

For the Riemann channel (`04_riemann_channel.tex`, `prop:functional-model-modes`, sign corrected
in `obs:model-modes-sign`): one mode per nontrivial zero `rho = sigma + i gamma`, frequency
`gamma/2`, amplitude decay rate `(1-sigma)/2`, and

    RH  <=>  every mode decays at the single rate 1/4 .

**RH = every resonance of this cavity has the same linewidth**: a "critically damped" cavity, or
in the notebook's language a Riemann quantum expander (side B of `README.md`: one modulus for all
zeros = the transfer matrix is a scalar times a unitary).

A caution on the folklore phrasing: equal *linewidth* is **not** equal *Q*. With
`Q_n = omega_n/Gamma = (gamma_n/2)/(1/2) = gamma_n`, uniform width means `Q` grows linearly with
frequency — the high modes are relatively sharper and sharper. What is uniform is the **lifetime**:
every mode rings for the same time, mean holding time `2` (`prop:mode-diagonal-rebound-rh`(ii));
in discrete time with common modulus `r`, `1/(1-r^2)` (T4).

### 2.5 Why uniform width is special

Three cavities.

1. **A generic (chaotic) cavity.** Standard (textbook): the widths *scatter* — in the weak
   coupling limit the partial widths of a chaotic cavity are Porter-Thomas distributed, broad,
   with plenty of very narrow modes. A histogram of widths is a smooth distribution, not a spike.
2. **A cavity with a symmetry that pins the widths.** The `N`-cycle with funnels below: rotation
   symmetry makes the resonance matrix circulant, the resonances are one number times the `N`th
   roots of unity, widths equal *by symmetry*, for free.
3. **Our cavity.** The only symmetry available is the functional equation, and on its own a
   functional equation buys a **pairing**:

```
   FE pairs rho <-> 1-rho, i.e. widths (1-sigma)/2 <-> sigma/2, SUM always 1/2:
   an unconditional width sum rule.
        width axis:   0 ----- x --------|-------- x ----- 1/2
                              G        1/4      1/2-G
   RH: the two are never split; every pair sits on the middle mark.
```

So the physics of RH here is sharp and modest: *the functional equation already guarantees that
each resonance has a mirror partner whose width completes it to a fixed total.* RH says the
pairing is implemented by **a reflection through one line rather than a genuine exchange of two
distinct widths** — no pair split, every pair degenerate. In disc language the resonance multiset
is invariant under inversion in the circle `|z| = r` (`z -> r^2/zbar`), whose fixed set is exactly
that circle. A sum rule on widths is cheap; degeneracy of every pair under it is the hard part.

---

## 3. The graded (fermionic) twist, briefly and honestly

In the notebook the zeros enter the trace with a **minus sign** (supertrace of a graded bond;
`cit:fmps-supertrace`, `obs:zero-coherences-populations`, `04c_phantasm_channels.tex`), so the
modes carrying them are **odd**. An odd operator is not a population:

    even:  |vac><vac| ,  |1><1|        (populations, diagonal in excitation number)
    odd:   |1><vac| ,  |vac><1|        (a COHERENCE between vacuum and one excitation)

An odd operator is a **dipole**: an off-diagonal element oscillating at the resonance frequency
and decaying at the resonance width. It is what a classical field couples to, and it is *not* a
probability. Hence a triviality in quantum optics that is a theorem in the notebook: the exit flux
`fl(rho) = <j|rho|j>` reads a population, so it **vanishes identically on odd operators**; the
reset cannot feed them, and the odd modes evolve autonomously whatever the repump is. That is
`prop:odd-modes-protected` (`04h_rebound_state.tex`): for every rebound density, `|k_w><vac|` is
an eigen-operator with eigenvalue set by the zero. **The zeros are protected because they are
coherences.**

The two-level atom makes the factor of two explicit. Standard (textbook), spontaneous emission at
rate `gamma`:

    population  rho_ee(t) = e^{-gamma t} rho_ee(0)                   (rate gamma)
    coherence   rho_eg(t) = e^{-i omega_0 t - gamma t/2} rho_eg(0)   (rate gamma/2)

Exactly this factor of two appears in the notebook: under RH every odd (coherence) mode decays at
`1/4` and every even (population/pair) eigenvalue has real part `-1/2`
(`prop:mode-diagonal-rebound-rh`(ii)). **The zeros are the coherences; the pair sums are the
populations** — which is why the even sector carries no zeros (`obs:zero-coherences-populations`):
populations know only rates, coherences know frequencies.

---

## 4. A ladder of examples

Six cavities. One line of physics, one of graph language, each.

**(i) The bare half-line.** `T_X = [0]`, `c = 1`.
*Physics:* an open waveguide with a hard wall — no cavity, reflection is a pure phase.
*Graph:* `p = z^2`, `ptilde = 1`, `R = -z^2` (`numerics.md` D3): a double "resonance" at `z = 0`,
the degenerate case where a jump can only happen at even times (`numerics.md` D14).

**(ii) One vertex with a loop.** `T_X = [a]`, coupling `c`.
*Physics:* a single-site cavity with return amplitude `a`, coupled to the guide.
*Graph:* `p(z) = z^2 - a z + (1-c^2)`. At `c = 1` the roots are `z = 0` and `z = a`: one resonance
at the return amplitude, as intuition says. A **complex** pair needs `a^2 < 4(1-c^2)`, hence
`c^2 < 1`, and then `|z| = sqrt(1-c^2)` automatically — equal moduli for free (`numerics.md` D18).
With `c^2 = q+1 > 1` a one-vertex core has only real resonances.

**(iii) The pure cusp.** `n = 1`, `T_X = [0]`, `c^2 = q+1`.
*Physics:* an all-mirror cavity — the constant mode is bound, nothing rings, the reflected wave
has no structure.
*Graph:* `R(z) = (z^2-q)/(q z^2-1)`, poles `+-q^{-1/2}` (the constant function and its bipartite
twin), zeros `+-q^{1/2}` outside the disc, **no resonances** (C3, `numerics.md` D7); and
`1/R(z) = q zeta_K(2s-1)/zeta_K(2s)` with `z = q^{s-1/2}`, the function-field twin of
`phi(s) = xi(2s-1)/xi(2s)`, a pole at `s = 1`, a zero at `s = 0`, nothing else. Same graph in the
preprint as the "modular curve", one vertex attached `q+1` times to a cusp, with resonance matrix
`H(mu) = ((q+1) sqrt q/mu)/(2 sqrt q) - (mu+mu^{-1})/2`, zeros at `mu = +-sqrt q`, resonant states
the constant and the alternating function (`refs/src/2603.26443/final_draft.tex:1974-1979`).

**(iv) The `N`-cycle with funnels (hyperbolic cylinder).**
*Physics:* a **ring resonator** — one closed orbit of length `N`, a comb of equally spaced modes
(a free spectral range), all of the same linewidth because rotation makes them images of one
another.
*Graph:* the resonance matrix is circulant and the resonances are `mu = q^{-1/2} e^{2 pi i j/N}`,
`j = 0..N-1`, equidistributing on the circle of radius `q^{-1/2}` as `N -> infinity`
(`refs/src/2603.26443/final_draft.tex:1940-1954`). Equal widths for free — the cheap way to meet
an RH-like condition, and why it proves nothing by itself.

**(v) The elliptic-curve quotients.**
*Physics:* a cavity whose resonance list is a Weil zero list — and Weil's theorem *is* the
statement that all its widths are equal.
*Graph:* for `y^2+y = x^3+x+1` over `F_2` the resonance determinant is
`(mu^2+1)^2 (mu^2-2)(2 mu^4 - 2 mu^2 + 1)`, the last factor being `P(mu^2)` with `P` the numerator
of `Z_X(T) = (2T^2-2T+1)/((1-T)(1-2T))`, so those resonances lie on the circle of radius
`2^{-1/4}`; for `y^2 = x^3+x+1` over `F_3`, `(mu^2+1)^2 (mu-1)^2 (mu+1)^2 (mu^2-3)(3 mu^4+1)`,
same at radius `3^{-1/4}`, plus "topological" resonances at `mu = +-1` that are *not* `l^2`
(`refs/src/2603.26443/final_draft.tex:1981-2070`). In both the trivial pair `+-sqrt q` — Perron
mode and bipartite twin — sits far from the Weil circle.
*(Convention warning: that preprint's `mu` and the brief's `z` are the two roots of the same
quadratic `mu + mu^{-1} = lambda`, and the two write-ups do not always pick the same root; what
transfers is the invariant statement, one common modulus for the nontrivial family, not the
numerical value of the modulus.)*

**(vi) The modular surface.**
*Physics:* the cavity whose resonances are the Riemann zeros; equal widths iff RH.
*Graph:* one cusp, one-dimensional exit, scattering matrix `phi(s) = xi(2s-1)/xi(2s)`, poles with
`Re s < 1/2` at `rho/2` — the eigenvalues of the compressed Lax-Phillips semigroup, one per zero
(`04_riemann_channel.tex`, `prop:scattering-inner`, `prop:functional-model-modes`).

**Bonus: a dark state you can draw.** The same preprint exhibits a 3-regular graph with a funnel
carrying an honest `l^2` eigenfunction at eigenvalue `-2`, inside the continuum
(`refs/src/2603.26443/final_draft.tex:1956-1971`): an **embedded eigenvalue**, a state in the
middle of the band that cannot escape because it has a node exactly where the guide attaches —
the cusp form, and the cavity physicist's dark state.

---

## 5. What to keep in mind

1. **The exit counts cusps, not resonances.** One cusp = one propagating mode = one jump operator
   = one detector, however many resonances there are (`lem:exit-one-dimensional`); `h` cusps give
   an `h x h` scattering matrix (T8). Hence the rank-one defect and the single reset map.
2. **Bound states use the incoming self-energy, resonances the outgoing one.** Same square root,
   two branches: `Sigma = c^2 z` gives the `l^2` eigenvalues (wave `z^k`, decaying up the ray),
   `Sigma = c^2/z` the resonances (wave `z^{-k}`, growing up the ray = Gamow). The wrong branch
   gives growth in time instead of decay — the sign error corrected in `obs:model-modes-sign`.
3. **Cusp forms are dark states.** An eigenvector of the core with a node at the junction never
   couples to the guide and cancels between numerator and denominator of `R` (C2(iii); by
   `numerics.md` D4/D5 the band-edge roots at `z = +-1` cancel too, with no cusp form present).
   They are `l^2` eigenvalues scattering cannot see — including *inside* the continuum.
4. **The rebound is the repump.** The rebound density `Omega` is just "what state the cavity is
   put back into when a photon is counted". The stationary state is the time-average of the
   decaying orbit started from `Omega` (`thm:rebound-renewal`); conversely, for a target
   stationary `rho` the repump is forced, `Omega = Q_rho/Tr Q_rho`, `Q_rho = rho - C rho C^*`
   the loss (`thm:rebound-admissibility`).
5. **Uniform width gives a uniform holding time.** In discrete time with common modulus `r` the
   mean holding time is `1/(1-r^2)` whatever mixture you rebound into (T4); in the continuous
   Riemann normalisation (rate `1/4` in amplitude, `1/2` in probability) exactly `2`
   (`prop:mode-diagonal-rebound-rh`(ii)). Conversely, "stationary state = repump for every modal
   mixture" **is** the equal-width condition.
6. **Do not oversell the criterion.** `thm:flag-spectrum-attainable` holds for *any* one-exit
   no-event semigroup: nothing about zeta is used, the resonance list is put in by hand. Equal
   widths is a *reformulation* of RH in cavity language, not a mechanism
   (`obs:rebound-both-halves-scope`); and (iv) gets it free from a rotation symmetry.
7. **The open question, in physics terms.** All of the above is generic cavity QED; the one thing
   the arithmetic has not yet supplied is the repump:

   > **What physical reset does the arithmetic choose?** Which rebound density `Omega` — which
   > state the cavity is put back into after each detected quantum — is the one selected by the
   > primes, rather than chosen by hand from a flag?

   Equivalently: a distinguished isometry `U` carrying the Bost-Connes observables and the prime
   action, so that `Omega` is not free (`prop:gibbs-flag-isometry`, "Open: a distinguished `U`").
   In the graph round the question is finite: attach the ray to a congruence quotient of
   `GL_2(F_q[T])` and see whether the arithmetic hands you the exit, the resonances *and* the
   rebound together (T8, hypothesis H-ARITH).
