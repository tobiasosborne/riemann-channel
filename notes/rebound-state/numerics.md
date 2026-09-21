# Numerics lane: the rebound state inside the model space (T1–T7)

Author line: `claude:opus-5`. Date 2026-09-19. Independent numerical lane for the brief
`notes/rebound-state/astra-brief.md`. Written without reading the prover's file.

Evidence script: `scripts/rebound_state.py` (deterministic, seed 20260919, numpy + scipy,
runtime ≈ 10 s). Captured output: `outputs/rebound_state.txt`. **150 assertions, all passing**;
every assertion prints the formula it verified and the deviation. Three findings are printed
loudly as `!!` lines; one of them is an outright numerical **contradiction of T5(b)**.

## The finite model

Modes `w_1..w_N` in `C_+`, `k_w(tau) = 1/(tau - conj w)`, `N = 5`:

* **on-line** (RH true) `w_n = gamma_n/2 + i/4` for the first five zeta ordinates;
* **off-line** (RH false) `w_n = gamma_n/2 + i(1-sigma_n)/2`, `sigma = (.50,.62,.38,.55,.50)`,
  so `Im w = (.25,.19,.31,.225,.25)`;
* **both-signs** `w = ±gamma_1/2, ±gamma_2/2` at `i/4` (the FE-symmetric set, `N = 4`);
* plus `N = 1`, `N = 2`, `N = 3` and one set with `Im w_5 = 0.002`.

Gram condition numbers are tame (2.75 on-line, 2.89 off-line), so every number below is at
machine precision, not at the edge of a conditioning cliff.

## Constants fixed (derived in the script header, not assumed)

**Gram constant.** With `<f|g> = (1/2pi) int_R conj(f) g dx` (conjugate-linear in the first
slot) and the Paley–Wiener convention `f(tau) = int_0^inf fhat(x) e^{i tau x} dx`:

```
F k_w (x) = -i e^{-i conj(w) x}            on (0, infinity)
G_nm = <k_n|k_m> = int_0^inf e^{i(w_n - conj w_m)x} dx = i/(w_n - conj w_m),   G_nn = 1/(2 Im w_n)
```

so the brief's constant is **`c = i`** for the measure `dx/2pi` (equivalently `c = 2 pi i` for
plain Lebesgue `dx`: `int_R conj(k_n)k_m dx = 2 pi i/(w_n - conj w_m)`). Verified by direct
quadrature of `(1/2pi) int conj(k_n)k_m dx` on `[-4e4, 4e4]`, max deviation `8e-6` (checks 1–3).
This is the same matrix as `K_ij` of `cusp-bridge.md` checkpoint 3.

**Exit vector normalisation.** Integration by parts in the time domain gives, with no constant
left free, `-(<K psi|phi> + <psi|K phi>) = conj(psihat(0)) phihat(0)`, i.e.

```
j psi = psihat(0) = -i sum_n c_n           (psi = sum c_n k_n)   --> j = -i 1^T in the mode basis
```

Equivalently, entrywise, `-(D^* G + G D) = 1 1^T` with `D = diag(-i conj w_n)`: verified exactly
(checks 6, 9, 12), because `(i w_n - i conj w_m) · i/(w_n - conj w_m) = -1`.
In the orthonormalised picture `R = G^{1/2}`, `K = R diag(-i conj w) R^{-1}`:

```
|j> = i R^{-1} 1,   -(K + K^dag) = |j><j|   (numerical rank 1, sv2/sv1 ~ 1e-15),
<j|k_n> = -i  != 0  for every n             (C3),   ||j||^2 = 1^T G^{-1} 1 = 2.5 (on-line, N=5)
```

**C1/C4 remarks.** `C_t k_n = e^{-i conj(w_n) t} k_n` verified at `t = 0.3, 1.7, 5.0`; the sign is
the *corrected* one (decay, not growth) — the repo's `C-SIGN` item. `spec(K) = {-i conj w_n}`,
decay rates `Im w_n`. On C4: in the finite model `||C_t||_2` is `1, 1.0000, 0.9552, 0.1018,
5.9e-5` at `t = 0, .5, 2, 10, 40`, i.e. **strictly `< 1` for every `t > 0`**. So `||C_t|| = 1` is
*false* in every finite Gram model; any result that needs it needs genuinely infinitely many
modes. Nothing in T1–T6 below uses more than strong stability `C_t -> 0`.

## T1 conservativity — **SUPPORTS**

`Tr L_Omega(rho) = 0` identically for all four rebound states (mode-diagonal, pure on one mode,
generic full-rank, rank-one random) in both the on-line and off-line models: `vec(1)` is an exact
left null vector of the `N^2 x N^2` superoperator, to `1e-12` (checks 34–41). `e^{t L_Omega}` is
CPTP (Choi `>= -1e-10`, partial trace `= 1`) at `t = 0.1, 1, 6` (check 42) — the GKLS form is
`K = -i H - (1/2)|j><j|`, `H = (i/2)(K - K^dag)`, jumps `L_a = sqrt(omega_a)|phi_a><j|` with
`Omega = sum omega_a |phi_a><phi_a|`, and `sum L_a^dag L_a = |j><j|` because `Tr Omega = 1`.
The holding-time law `m_Omega(t) = -d/dt Tr(C_t Omega C_t^dag) = <j|C_t Omega C_t^dag|j>` is
non-negative pointwise and integrates to `1.000000` in all eight cases (checks 43–50): a proper
probability density, as T1 asserts. No extra SHW condition was needed in the finite model (where
of course conservativity is automatic); the finite model cannot test the explosion question.

## T2 stationary state — **SUPPORTS**

For each of the eight (model, Omega) pairs, `rho_inf` was computed by **four independent routes**
and they agree to `< 1e-14` (checks 51–66), better than the `1e-10` the brief asked for:

1. the closed mode-basis renewal integral `rho_inf = mu^{-1} R (Omega_k * conj(G)) R`, where
   `Omega_k = R^{-1} Omega R^{-1}` and `conj(G)_{nm} = i/(w_m - conj w_n)` is the entrywise factor
   `int_0^inf e^{(-i conj w_n + i w_m)t} dt` — this is the "entrywise `i/(w - conj w')`" formula of
   the brief, with the index order made explicit;
2. the Lyapunov solve `K X + X K^dag = -Omega`;
3. an eigenbasis-of-`K` integral (uses no mode structure at all);
4. the null vector of the `N^2 x N^2` superoperator `L_Omega`.

Also verified: `Tr(|j><j| rho_inf) = 1/mu` exactly; `ker L_Omega` is one-dimensional; the spectral
gap is `0.4358` (on-line, generic Omega) and `e^{60 L} rho_0 = rho_inf` to `8e-13` from a random
initial density — unique and globally attracting (checks 67–68). `mu = sum_n p_n/(2 Im w_n)` for
mode-diagonal Omega (checks 69–70).

Two by-products the brief did not ask for:

* **Under RH every mode-diagonal Omega has `mu = 2` exactly**, independent of `p` (check 71); so
  *no* mode-diagonal rebound state on the critical line can have `mu = infinity`. Off the
  mode-diagonal `mu` does vary: over 300 random full-rank Omega, `mu in [1.861, 2.582]` (check 72).
* `mu = infinity` cannot be produced in a finite model. Its finite shadow is a mode approaching
  the real axis: `Im w_5 = 0.002` gives `mu = 51.6 ~ p_5/(2 Im w_5)` (check 73). The genuine
  boundary case is the vacuum: `Tr(C_t Omega_vac C_t^dag) = 1` for all `t`, so `m_vac = 0` and
  `mu_vac = infinity` — `prop:vacuum-renewal-trivial-entanglement` is exactly the `Im w = 0` end of
  T2's criterion (check 126).

## T3 the graded sector — **SUPPORTS** (with two corrections)

On `C vac (+) K` with `Kbar = 0 (+) K` and `j` supported on `K`, the one-exit identity survives
(check 111). For **all four** rebound states tested (even/mode-diagonal on `K`; with vacuum-mode
coherences; `Omega = |vac><vac|`; generic full-rank on the whole space) the odd coherences are
**exact** eigen-operators with the zero eigenvalues, deviation `1.4e-14` (checks 112–115), because
the exit functional annihilates them. Confirmed: `spec L_Omega` always contains the `2N+1`
protected values `{0} u {-i conj w_n} u {+i w_n}`, and `det(z - L_Omega) = det(z - L_0)(1 -
mhat_K(z))` where `mhat_K` is built **from the K-block of Omega alone** (rel. dev `< 3e-14`,
checks 121–124). For `Omega = |vac><vac|` the spectrum reproduces `thm:vacuum-decay-finite`,
`{0} u spec B u conj spec B u {b_i + conj b_j}`, to `2.1e-14` (check 125).

Two corrections:

1. **Labelling (minor).** With `<·|·>` conjugate-linear in the first slot it is `|k_w><vac|` that
   carries `-i conj(w)` and `|vac><k_w|` that carries `+i w`. The brief's T3 states the transpose.
2. **The vacuum is stationary for EVERY Omega** (check 116): `Kbar|vac> = 0` and the exit
   functional kills `|vac><vac|`, so `L_Omega(|vac><vac|) = 0` identically. Hence in the graded
   model the stationary state is **not unique** when `Tr(Omega|_K) = 1` (`dim ker L_Omega = 2`,
   check 117: the stationary manifold is `{q|vac><vac| + (1-q) rho_inf}`), and when
   `Tr(Omega|_K) < 1` the *only* stationary state is the vacuum again (`dim ker = 1`, checks
   118–120): all population drains into `vac`. So the graded renewal generator buys a mixed
   stationary state only in the degenerate sense that the vacuum sector is invariant and
   decoupled. **This should be flagged in T7.**

## T4 persistence and the secular equation — **SUPPORTS**

`mhat_Omega(z) = Tr(|j><j|(z - L_0)^{-1} Omega)` agrees with the rational form

```
mhat_Omega(z) = sum_{n,m} Omega_k[n,m] / (z + i conj(w_n) - i w_m),     z_nm = -i conj w_n + i w_m
```

to `< 1.4e-14`, and with a numerical Laplace transform of `m_Omega(t)` to `~3e-6` (quadrature
limited), for all eight cases (checks 74–81). This is T4(c): the coefficients are exactly the
mode-basis matrix elements `Omega_k = R^{-1} Omega R^{-1} = G^{-1/2} Omega G^{-1/2}`.

T4(b) is verified in the strongest available form, the **rank-one determinant identity**

```
det(z - L_Omega) = det(z - L_0) (1 - mhat_Omega(z))
```

at three off-spectrum points `z` for every case, max relative deviation `5e-14` (checks 82–89).
For `N = 3` the spectrum of `L_Omega` was matched root-by-root against
`prod(z - z_nm) - sum_nm Omega_k[n,m] prod_{others}` to `< 1e-7` (checks 95–96).

T4(a): **the first disjunct never fires in the ungraded model.** `Tr(|j><j| X_nm) = 1` for *all*
`N^2` eigen-operators `X_nm = |k_n><k_m|` (checks 90–91) — the operator-level form of C3. So an
eigenvalue of `L_0` persists **iff** `Omega_k[n,m] = 0`, i.e. only via the second disjunct. For
mode-diagonal Omega all `N^2 - N = 20` off-diagonal `z_nm` persist (check 92); the `N`-fold
degenerate diagonal eigenvalue `-1/2` (on-line) keeps multiplicity `N - 1 = 4` — a rank-one
perturbation can only move one copy — and the single new eigenvalue is `z = 0` to `1e-15`
(checks 93–94). In the graded model the first disjunct *does* fire, for every vacuum-touching
eigen-operator; that is exactly T3.

On the Connes–Consani–Moscovici shape: the numerics confirm the shape
`1 = sum_{n,m} c_{nm}/(z - i w_m + i conj w_n)` with `c_{nm} = (G^{-1/2} Omega G^{-1/2})_{nm}` and
`sum_{n,m} c_{nm} G_{nm}... ` — but note `mhat(0) = Tr Omega = 1` always, which is just trace
preservation. Nothing in the numerics distinguishes this from a generic rank-one secular equation;
the coefficients are put in by hand with Omega. (Numerics cannot settle "more than a coincidence".)

## T5 mode-diagonal rebound states — **(a) SUPPORTS, (c) SUPPORTS, (b) CONTRADICTS**

**T5 main formula and (a): supported, exactly.** `rho_inf = mu^{-1} sum_n p_n (2 Im w_n)^{-1}
|khat_n><khat_n|` with `mu = sum_n p_n (2 Im w_n)^{-1}`, verified to `9e-16` in all three mode sets
(checks 97–99). In the mode basis `rho_inf,k = mu^{-1} diag(p_n)` while `Omega_k = diag(2 Im w_n
p_n)`, so `rho_inf = Omega` iff `2 Im w_n = 1/mu` for every `n` with `p_n > 0`:

* on-line and both-signs (RH true): `rho_inf = Omega` for 6 random `p`, max dev `8e-16`
  (checks 100–101);
* off-line (RH false): `rho_inf != Omega` for all 6 random `p`, trace distance
  `||rho_inf - Omega||_1 in [0.111, 0.154]`, max-entry gap `in [0.054, 0.077]` (check 102) — a
  large, unambiguous discrepancy;
* **exact quantifier** (check 103): in the off-line model, a `p` supported on the two modes that
  happen to have `Im w = 1/4` restores `rho_inf = Omega` to `4e-16`. So the correct statement is
  "all `Im w_n` **with `p_n > 0`** are equal", and the RH reformulation needs the quantifier
  "for **every** mode-diagonal Omega", including the ones supported on two modes at a time. With
  that quantifier it is exactly "all `Im w_n` equal"; it is *not* "all on the critical line" until
  one adds the FE (which pins the common value at `1/4`).

**T5(c): supported.** On-line, `mhat_Omega(z) = (1/2)/(z + 1/2)` for **every** mode-diagonal
Omega, independent of `p`, to `3e-16` (check 108); the unique root is `z = 0`. Moreover every
nonzero eigenvalue of `L_Omega` then has `Re = -1/2` exactly (check 110): the even-sector
relaxation rate is twice the common zero-decay rate, frequencies `(gamma_m - gamma_n)/2`.
Off-line the `N` diagonal `L_0` eigenvalues `-2 Im w_n` are replaced by the `N` roots of
`1 = sum_n p_n 2 Im w_n/(z + 2 Im w_n)`, e.g. `(-0.5568, -0.5000, -0.4880, -0.4163, 0)`; `z = 0`
is always a root (check 109).

### !! T5(b) FAILS NUMERICALLY

The drafted claim is that the entanglement spectrum (`def:bond-entanglement`: the spectrum of the
bond density) of `rho_inf` is `{p_n (2 Im w_n)^{-1}/mu}`, hence `{p_n}` under RH. **This is false,
and by a large margin.** On-line, `N = 5`, `p = (0.40, 0.30, 0.15, 0.10, 0.05)`:

```
claimed spectrum   0.400000  0.300000  0.150000  0.100000  0.050000
actual spec(rho_inf) 0.425600  0.295654  0.144090  0.097305  0.037351
max discrepancy 0.0256 (6.4% relative);  entropy 1.352492 vs 1.392321 nats
```

(the loud line before check 104, and checks 104–107).

**Reason.** `G_nm = i/(w_n - conj w_m)` is *never* zero, so distinct kernel modes are never
orthogonal: on-line the normalised overlap is `|<khat_n|khat_m>| = 1/sqrt((gamma_n-gamma_m)^2 + 1)`,
which is `0.1437` for the first two zeros and lies in `[0.053, 0.370]` over the on-line `N=5`
set (checks 5, 8, 11). Hence `sum_n lambda_n |khat_n><khat_n|` is a sum of **non-orthogonal** rank ones, not a
spectral decomposition, and its eigenvalues are not the `lambda_n`.

**Corrected statement, verified to `1.4e-15`** (check 105):

```
spec(rho_inf) = spec( diag( p_n (2 Im w_n)^{-1} / (mu G_nn) ) · G )
              = spec( G^{1/2} diag(...) G^{1/2} ),     G_nm = i/(w_n - conj w_m)
```

and for `N = 2` the closed form is exactly (check 150, dev `5e-16`)

```
spec(rho_inf) = { (1 ± sqrt( (p_1-p_2)^2 + 4 p_1 p_2 |o|^2 )) / 2 },   o = <khat_1|khat_2>.
```

What *does* survive of T5(b): under RH `spec(rho_inf) = spec(Omega)` exactly (check 106) — a
corollary of T5(a) — so "the entanglement spectrum is the rebound state's own spectrum" is true;
it just is not `{p_n}`. The boundary case `N = 1` (`p = delta_1`) does give `{1, 0, ..., 0}`
(check 107): the failure is strictly a multi-mode non-orthogonality effect.

**Consequence for the programme.** One cannot read off a prescribed entanglement spectrum from
the weights `p_n` of a mode-diagonal rebound state. Prescribing `{p_n}` as the entanglement
spectrum means *inverting* the map `p -> spec(G^{1/2} diag(p/(mu G_nn) · ...) G^{1/2})`, whose
input data include the zero ordinates through `G`. That is a genuine (and interesting) extra
constraint, not a free choice — and it is exactly what T6 then has to face.

## T6 the admissibility cone — **SUPPORTS**, with a new necessary condition

The candidate `Omega_cand = -(K sigma + sigma K^dag)/Tr(|j><j| sigma)` always has
`Tr Omega_cand = 1` automatically (a consequence of the one-exit identity), so admissibility is
purely a positivity question. Verified:

* **(a) mode-diagonal sigma is always admissible** (checks 127–128), on-line and off-line, 6
  random `p` each, worst `lambda_min(Omega_cand) = 3.1e-3 > 0`. So under RH every finite spectrum
  *of the mode-diagonal family* is realised — but see the T5(b) correction: the realised
  entanglement spectrum is `spec(G^{1/2} diag(p) G^{1/2})`, not `p`.
* **Schur form** (checks 129–131): `Omega_cand,k[n,m] = sigma_k[n,m] (conj(a_n) + a_m)` with
  `a_n = -i w_n`, verified to `1e-10`; `M_nm = conj(a_n) + a_m` has rank exactly 2 and signature
  `(1,1)` (eigenvalues `-15.60, +18.10` for the on-line `N=5` set), since
  `x^dag M x = 2 Re(conj(v) u)` with `u = sum x_n`, `v = sum a_n x_n`. Under RH the explicit form
  is `M_nm = 1/2 + i(gamma_n - gamma_m)/2`: constant real part `2 Im w`, imaginary part the
  ordinate differences. Admissibility is therefore the Schur-positivity condition
  `(sigma_k ∘ M) >= 0` against an indefinite rank-two matrix — a genuine restriction, as drafted.
* **(b) random eigenvectors, Gibbs-like spectrum `n^{-beta}/Z`.** Over 400 Haar-random unitaries
  per case, positivity failed **400/400 times**, for `beta = 1.5` and `beta = 2`, in both the
  on-line and off-line models (checks 132–135). Most negative eigenvalue of `Omega_cand`:
  `-8.30` (`beta=1.5`), `-19.14` (`beta=2`) on-line; `-8.76`, `-19.74` off-line. **Prescribing an
  entanglement spectrum with an eigenbasis chosen independently of the modes essentially never
  gives an admissible state.**
* **A necessary condition on the eigenbasis (new).** Writing `K = -i H - (1/2)|j><j|`,
  admissibility is `i[H, sigma] + (1/2){|j><j|, sigma} >= 0`. In an eigenbasis
  `sigma = sum_a lambda_a |phi_a><phi_a|`, with `j_a = <phi_a|j>` and `H_ab = <phi_a|H|phi_b>`, the
  `2x2` minors give

  ```
  |H_ab|  >=  (1/2) |j_a| |j_b| · |sqrt(lambda_a) - sqrt(lambda_b)| / (sqrt(lambda_a) + sqrt(lambda_b))
  ```

  for every `a != b`. Verified to hold on 50 admissible (mode-diagonal) sigma with worst margin
  `+0.0121` (check 136), and it is necessary-not-sufficient: it certifies 5/200 of the
  inadmissible Gibbs samples outright, worst violation `0.163` (check 137).
  **Sharp corollary, verified:** if `sigma` commutes with `H` and has non-degenerate spectrum
  (and no `j_a = 0`, which C3 guarantees) it can *never* be admissible; a Gibbs state in the
  eigenbasis of `H` gives `lambda_min(Omega_cand) = -0.2926` (check 138).

  **Bost–Connes reading.** The obstruction reappears as **failure of positivity**, not as
  `mu = infinity`. `mu` stays finite for every finite-rank sigma. With
  `sigma = U diag(n^{-beta}/zeta(beta)) U^*`, the condition on the isometry `U` is
  `|<U n|H|U m>| >= (1/2)|<U n|j>| |<U m|j>| |n^{-beta/2} - m^{-beta/2}|/(n^{-beta/2} + m^{-beta/2})`:
  the Bost–Connes basis must be *strongly non-commuting with the mode Hamiltonian*, with a
  quantitative lower bound that grows as the Gibbs weights spread (i.e. as `beta` grows). An
  "arithmetic" eigenbasis chosen without reference to the modes is excluded outright.
* **(c) the cone of orbit states**: `-(K Phi(psi) + Phi(psi) K^dag) = |psi><psi|`, so every orbit
  state is admissible (check 139); an admissible sigma is reconstructed as the positive
  combination `sigma = Tr(|j><j|sigma) sum_a omega_a Phi(phi_a)` over the eigenvectors of
  `Omega_cand` to `7e-15` (check 140); positive combinations of random orbit states are admissible
  (check 141); and a nonnegative least-squares fit against a dictionary of 600 random orbit states
  reproduces an admissible sigma to residual `0.0` and an inadmissible one only to `0.253`
  (check 142). `Omega_cand(rho_inf(Omega)) = Omega` exactly (check 143): the map is a bijection
  between rebound states and admissible stationary states.

## Sanity

`N = 1` (checks 144–145): `G = 1/(2 Im w) = 2`, `|j|^2 = 2 Im w = 1/2`, `L_Omega = 0` identically,
`mhat(z) = (1/2)/(z+1/2)`. `N = 2` by hand (checks 146–150): `||j||^2 = (G_11+G_22-2 Re G_12)/det G
= 1`; solving `(z+b_1)(z+b_2) = p_1 b_1 (z+b_2) + p_2 b_2 (z+b_1)`, `b_n = 2 Im w_n`, gives
`spec L_Omega = {0, -(b_1 p_2 + b_2 p_1), z_12, z_21}`, matched to `1e-10`; and the corrected
entanglement-spectrum closed form above to `5e-16`.

## Verdicts

| statement | verdict |
|---|---|
| T1 conservativity | **supports** (trace preservation exact, CPTP, `m_Omega` a proper density) |
| T2 stationary state | **supports** (four independent routes agree to `1e-14`; unique, globally attracting; `mu` formula exact). `mu = infinity` not testable in a finite model |
| T3 zeros survive for every Omega | **supports**; two corrections: the coherence labels are transposed, and `|vac><vac|` is stationary for **every** Omega, so uniqueness fails in the graded model |
| T4 persistence + secular equation | **supports**; note the first disjunct of T4(a) never fires in the ungraded model (`Tr(|j><j| X_nm) = 1` always) |
| T5(a) RH reformulation | **supports**, with the quantifier sharpened to "all `Im w_n` with `p_n > 0`" |
| T5(b) entanglement spectrum `{p_n}` | **CONTRADICTS** — 6.4% discrepancy at `N=5`; corrected form `spec(G^{1/2} diag(...) G^{1/2})` verified |
| T5(c) `mhat = (1/2)/(z+1/2)`, new eigenvalue 0 | **supports** exactly |
| T6 admissibility cone | **supports** (cone = orbit cone, Schur form rank-two indefinite, mode-diagonal admissible); random Gibbs eigenbases fail 400/400; new necessary condition on the eigenbasis derived and verified |
| T7 | not a numerical statement; but T3's non-uniqueness and T5(b)'s failure both weaken it, see below |

## What a refuter should attack next (from this lane)

1. **T5(b) is the load-bearing failure.** The programme wants a *prescribed* entanglement
   spectrum; the mode-diagonal family does not deliver `{p_n}` but `spec(G^{1/2} diag(·) G^{1/2})`,
   whose dependence on the zero ordinates is the whole question. Ask the prover to invert this map.
2. **The graded model's stationary state is not unique.** Any `Omega` with vacuum weight makes
   the vacuum the *only* stationary state; any `Omega` inside `K` leaves a two-dimensional
   stationary manifold. So "both halves at once" holds only after restricting to the
   vacuum-free sector, which should be stated explicitly in T7 and in any claim about
   `obs:complementary-halves`.
3. **`||C_t|| = 1` is false in every finite model.** Any argument that needs it needs the infinite
   Blaschke product, and the finite Gram evidence cannot support it.
4. **The T6 necessary condition kills the naive Bost–Connes identification**: a prescribed
   eigenbasis commuting with `H` is never admissible, and a Gibbs-spectrum state in a random
   basis fails positivity essentially always. The obstruction is positivity, not `mu = infinity`.
5. The Connes–Consani–Moscovici shape of the secular equation is, in the finite model, exactly a
   generic rank-one secular equation whose residues are the free parameters of `Omega`. Numerics
   give no reason to call it more than a coincidence.
