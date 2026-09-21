# Brief for the prover: the Riemann channel with a rebound state inside the model space

You are the prover in a mathematical research notebook (git repo, current directory). Author line
for everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/rebound-state/astra-proofs.md`
(create it; overwrite if present). Do not edit anything else. Do not run git. You may run python3
(numpy, mpmath, sympy, scipy are installed) for checks, and you may read any file in the repo,
especially `refs/src/1707.02266/TORUN.tex` (Siemon, Holevo, Werner, "Unbounded generators of
dynamical semigroups", the SHW paper), `notes/extract/shw-unbounded-generators-sources.md` (byte-cited
quotes from it), `report/sections/02b_definitions_arithmetic.tex` (definitions of the model space and
the Riemann channel), `report/sections/02c_definitions_phantasm.tex` (the vacuum-decay Lindbladian),
`report/sections/04_riemann_channel.tex` and `report/sections/04c_phantasm_channels.tex` (what is
already registered), and `notes/rh-strategy-2026-09-19/cusp-bridge.md` (a finite Gram model).

## Why this problem

The notebook's central conjecture (`conj:phantasm-both-halves`, `report/sections/10_open_problems_dead_routes.tex:63-73`)
asks for one Z_2-graded Lindbladian whose stationary state is mixed with a prescribed entanglement
spectrum and whose odd relaxation modes are the nontrivial zeros of zeta. What exists so far is the
vacuum-decay Lindbladian (`def:vacuum-decay`, `thm:vacuum-decay-finite`, `prop:absorbing-vacuum-channel`):
zeros as odd coherences, but the only stationary state is the pure vacuum, and the vacuum is absorbing
(`prop:vacuum-renewal-trivial-entanglement`: the renewal integral with the vacuum as rebound state
diverges). The SHW picture says a standard generator with a given no-event semigroup is fixed by a
rebound state Omega. Nobody has written down what happens when Omega lives INSIDE the model space.
Your job: do that, with proofs, and say exactly what it buys and what it does not.

## Conventions (Section 0 of your file must restate these and PROVE items C1 to C4)

Work in the upper half plane picture, which is the standard Sz.-Nagy--Foias / Lax--Phillips one.

- `H^2 = H^2(C_+)`, the Hardy space of the upper half plane, with the Fourier (Paley--Wiener)
  unitary `F: H^2 -> L^2(0, infinity)`, under which multiplication by `e^{i t tau}` (t >= 0) becomes
  translation to the right by t, and its adjoint becomes the backward translation `(g)(x) -> g(x+t)`.
- `Theta` is an inner function in `C_+` (bounded analytic, unimodular boundary values). The
  notebook's scattering symbol is `S(tau) = xi(1 - 2 i tau)/xi(1 + 2 i tau)` with `xi` the completed
  zeta; its zeros are `tau = -gamma/2 - i(1 - sigma)/2` for each nontrivial zero `rho = sigma + i gamma`
  and its poles are the reflections. So `S` is inner in the LOWER half plane, and `Theta(tau) := S(-tau)
  = xi(1 + 2 i tau)/xi(1 - 2 i tau)` is inner in `C_+` with zeros `w_rho = gamma/2 + i(1 - sigma)/2`
  (both signs of gamma occur), all on the line `Im w = 1/4` iff RH. Nothing below depends on which
  half plane one prefers, but the sign of the eigenvalue does, and the notebook's shard
  `report/sections/04_riemann_channel.tex:69-76` currently prints `Z_t^* k_lambda = e^{-i t conj(lambda)} k_lambda`
  with `lambda` in the lower half plane, which is growth, not decay. Record the corrected statement in
  your correction ledger (item "C-SIGN") and use the corrected one throughout.
- `K = K_Theta = H^2 ominus Theta H^2` (the model space), `P_K` the orthogonal projection.
- The compressed semigroup `Z_t = P_K e^{i t tau}|_K`, `t >= 0`, and the NO-EVENT semigroup of this
  brief is its adjoint `C_t := Z_t^*`. Write `C_t = e^{t K_gen}` with generator `K_gen` (unbounded,
  dissipative). In the notebook's language the Riemann channel is `rho -> Z_t^* rho Z_t = C_t rho C_t^*`
  (`def:riemann-channel`), a no-event semigroup in the SHW sense (`1707.02266:TORUN.tex:172-173`).
- For `w in C_+` with `Theta(w) = 0` let `k_w(tau) = 1/(tau - conj(w))` (reproducing kernel of `H^2` at w,
  up to the constant `2 pi i` which you should fix once and keep).

Prove:
- **C1.** `k_w in K` iff `Theta(w) = 0`, and `C_t k_w = e^{-i t conj(w)} k_w`, so the mode decays at
  rate `Im w = (1 - sigma)/2`, which is `1/4` for every mode iff RH. (This is the corrected form of
  `prop:functional-model-modes`.) Give the time-domain form: `F k_w` is a multiple of `x -> e^{i w x}`
  on `(0, infinity)`, and `C_t` is the backward translation restricted to `F K`, which is invariant.
- **C2.** (Exit space.) In the SHW sense (`1707.02266:TORUN.tex:205-206`), the exit space of `C_t` on `K`
  is one-dimensional, `E = C`, with `j g = g(0)` in the time-domain picture (up to a constant you
  fix), i.e. `<j psi, j phi> = -(<K_gen psi, phi> + <psi, K_gen phi>)` on the domain. State the domain
  precisely. So the "cusp" of this channel is one-dimensional and `-(K_gen + K_gen^*) = |j><j|` as
  forms. (Compare SHW's half-sided shift example, `TORUN.tex:442-450`, where `j psi = psi(0)`; here the
  same shift is restricted to the backward-shift-invariant subspace `F K`.)
- **C3.** `C_t -> 0` strongly on `K` (so `J psi(t) = j C_t psi` is an isometry `K -> L^2(R_+)`, SHW's
  `TORUN.tex:213-215`; this is the outgoing translation representation), and `j k_w = k_w(0-value) != 0`
  for EVERY zero mode: no mode is decoupled from the exit.
- **C4.** The norm statement: `||C_t|| = 1` for all `t` is claimed elsewhere in the notebook
  (unreviewed). Do not prove or use it; but state explicitly which of your results need only strong
  stability and which would need uniform exponential stability.

## The objects to define (Section 1)

- **The renewal generator with rebound state Omega inside K.** For a density `Omega` (positive,
  trace class, `Tr Omega = 1`) on `K`, define on trace-class operators of `K`
  `L_Omega(rho) = K_gen rho + rho K_gen^* + <rho>_j Omega`, where `<rho>_j` is the exit functional
  `rho -> Tr(|j><j| rho)` (formally; give it a precise meaning via SHW's reinsertion map
  `TORUN.tex:246, 253-254` with `M = Omega^{1/2}`-type Kraus operators, jump operators `L_alpha = M_alpha j`).
  Its minimal semigroup in SHW's sense is the object. Call the holding-time law
  `m_Omega(t) := -d/dt Tr(C_t Omega C_t^*)` and its Laplace transform `mhat_Omega(z) = int_0^infty e^{-z t} m_Omega(t) dt`.
- **The graded version.** On `C vac (+) K`, with `vac` even and `K` odd (as in `def:vacuum-decay`),
  the same generator with the exit from `K` reinserted into a density `Omega` on `C vac (+) K`.
  The vacuum-decay Lindbladian is the case `Omega = |vac><vac|`.

## Statements to prove or correct (Sections 2 to 6)

Each statement below is my draft. Prove it, or correct it and prove the corrected version, or mark it
OPEN with the precise missing step. Declare every hypothesis you need as `H-<NAME>` in a list at the
top of your file (for instance H-SIMPLE: all zeros simple; H-FINITE: Omega supported on the span of
finitely many modes; H-SHW: the minimal-semigroup construction of SHW applies to this generator; and
so on). Everything about the actual zeta zeros beyond "Theta is inner with the stated zero set" must
be a declared hypothesis.

- **T1 (conservativity).** For every density Omega on K the minimal semigroup of `L_Omega` is trace
  preserving (conservative): the renewal process "exit at the cusp, rebound to Omega" has holding
  times that are i.i.d. with law `m_Omega`, `m_Omega` is a probability density on `(0, infinity)`
  (because `C_t -> 0` strongly and `C_0 = 1`), and a renewal process with a proper holding-time law does
  not explode. Relate this to SHW's conservativity discussion (their `TORUN.tex:646-650` remark on
  first-order versus finite-time trace preservation) and say whether any additional SHW condition is
  needed here.
- **T2 (stationary state; the renewal theorem).** The mean holding time is
  `mu_Omega = int_0^infty Tr(C_t Omega C_t^*) dt`. If `mu_Omega < infinity`, the minimal semigroup has
  the unique stationary density `rho_inf = mu_Omega^{-1} int_0^infty C_t Omega C_t^* dt` and every
  initial state converges to it (state the mode of convergence you can prove; the renewal theorem
  needs non-lattice holding times, check whether that can fail here). If `mu_Omega = infinity` there is
  no stationary density. Show that `mu_Omega < infinity` whenever Omega is supported on the span of
  finitely many modes `k_w`, with `mu = sum` of the explicit contributions, and give an example of a
  density Omega on K with `mu_Omega = infinity` (or prove none exists), so that the vacuum result
  `prop:vacuum-renewal-trivial-entanglement` is seen as the boundary case of a general criterion.
- **T3 (the zeros survive in the odd sector, for every rebound state).** In the graded version on
  `C vac (+) K`, for ANY density Omega on `C vac (+) K` (even or not), each odd coherence
  `|vac><k_w|` and `|k_w><vac|` is an eigen-operator of `L_Omega` with eigenvalue `-i conj(w)`
  respectively `i w` (decay rate `Im w`, so `1/4` under RH), exactly as in `thm:vacuum-decay-finite`;
  the reason is that the exit functional vanishes on odd operators (`Tr(|j><j| |vac><k_w|) = 0`
  because `j` lives on `K`). So the "zeros as odd relaxation modes" half is preserved by every
  rebound state, and the whole freedom of Omega acts on the even sector.
- **T4 (spectrum of the even sector: persistence criterion and secular equation).**
  `L_Omega = L_0 + |Omega><<j j|` is a rank-one perturbation of `L_0(rho) = K_gen rho + rho K_gen^*`
  on the even sector. Prove: (a) an eigenvalue `z` of `L_0` with (generalised) eigen-operator `X` persists
  as an eigenvalue of `L_Omega` iff `Tr(|j><j| X) = 0` OR Omega has no component along `X` (state this
  precisely with the biorthogonal system of `L_0`, at least under H-FINITE and H-SIMPLE, where the
  even eigen-operators are `|k_w><k_w'|` with eigenvalues `i w - i conj(w')`, i.e. decay rate
  `Im w + Im w'` and frequency `(Re w - Re w')`); (b) every other eigenvalue of `L_Omega` is a root
  of the secular equation `1 = mhat_Omega(z)`; (c) under H-FINITE, `mhat_Omega` is the explicit
  rational function you obtain from the Gram matrix of the modes, `<k_w, k_w'> = c/(w - conj(w'))`
  (fix c), and write it out. Note the shape: `1 = sum_{n,m} (coefficient)/(z - i w_n + i conj(w_m))`,
  a secular equation of Connes--Consani--Moscovici type; say whether that is more than a coincidence.
- **T5 (mode-diagonal rebound states; a reformulation of RH).** Let Omega be diagonal in the modes,
  `Omega = sum_n p_n |khat_n><khat_n|` with `khat_n = k_{w_n}/||k_{w_n}||`, `p_n >= 0`, `sum p_n = 1`,
  finitely many n. Then `rho_inf = mu^{-1} sum_n p_n (2 Im w_n)^{-1} |khat_n><khat_n|` with
  `mu = sum_n p_n (2 Im w_n)^{-1}`. Consequently: (a) `rho_inf = Omega` for every such Omega iff all
  the `Im w_n` are equal, i.e. iff every zero involved has `sigma = 1/2`. So "the stationary state of
  the renewal channel equals its rebound state, for every mode-diagonal rebound state" is equivalent
  to RH for the zeros involved (make the quantifiers exact; with all zeros allowed this is a new
  formulation of RH on the channel side, and say what it adds beyond `prop:functional-model-modes`,
  which already says RH iff all rates equal). (b) The entanglement spectrum (`def:bond-entanglement`)
  of `rho_inf` is `{p_n (2 Im w_n)^{-1}/mu}`, so under RH it is `{p_n}`: the rebound state's own
  spectrum. (c) The full spectrum of `L_Omega` in this case, from T4: which even eigenvalues persist,
  what the secular root is; under RH the secular function is `mhat(z) = (1/2)/(z + 1/2)` and the
  only new eigenvalue is `0`.
- **T6 (the inverse problem; the cone of admissible stationary states).** A density `sigma` on K is the
  stationary state of `L_Omega` for some density Omega iff `-(K_gen sigma + sigma K_gen^*) >= 0` (as a
  positive trace-class operator, on the appropriate domain), and then Omega is unique:
  `Omega = -(K_gen sigma + sigma K_gen^*)/Tr(|j><j| sigma)`. Equivalently `sigma` lies in the cone
  generated by the orbit states `Phi(psi) = int_0^infty |C_t psi><C_t psi| dt` (normalised). Under
  H-FINITE with `sigma = sum_{n,m} sigma_{nm} |khat_n><khat_m|`, the condition is the entrywise
  (Schur) product condition `(sigma_{nm} (a_n + conj(a_m)))_{nm} >= 0` with `a_n = -i w_n` up to your
  normalisations; note `(a_n + conj(a_m))` is a rank-two indefinite matrix, so this is a genuine
  restriction. Then answer, with proof or counterexample: (a) is every finite spectrum
  `{p_1, ..., p_N}` the entanglement spectrum of some admissible sigma (yes trivially by T5 under RH
  if mode-diagonal states are admissible: check they are); (b) which sigma with prescribed
  eigenvectors are admissible, i.e. what T6 says about the notebook's obstacle "identify K with the
  Bost--Connes bond": if `U: l^2(N) -> K` is an isometry and `sigma = U diag(n^{-beta}/zeta(beta)) U^*`,
  the condition on U is `-(K_gen U D U^* + U D U^* K_gen^*) >= 0`. Give at least one necessary condition
  on U in terms of the modes, and say whether the vacuum-decay obstruction (`prop:normal-kms-gibbs`,
  no normal KMS state at beta = 1) reappears here as `mu_Omega = infinity` or as failure of positivity.
- **T7 (what this buys for `conj:phantasm-both-halves`, honestly).** State in one paragraph what the
  graded renewal generator with a mixed Omega achieves (mixed stationary state with a prescribed
  entanglement spectrum AND the zeros as odd modes, once each plus conjugates) and what it does NOT
  (no arithmetic reason for Omega; the entanglement spectrum is put in by hand; no identification of
  K with the Bost--Connes bond; the even sector's non-stationary spectrum is pair differences with
  new secular roots). Also state whether T3+T5 make `obs:complementary-halves` ("no construction in
  this book has both") false as literally stated, and in what sense.

## Output format

`notes/rebound-state/astra-proofs.md`, in Markdown with `$...$` math (or plain ASCII math), with:
0. Author line, list of hypotheses `H-*`, and Section 0 (conventions, C1 to C4 with proofs).
1. Sections 1 to 7 for the definitions and T1 to T7, each statement labelled `T<n>` (and `T<n>(a)`
   etc.), each with STATUS one of PROVED / PROVED-CONDITIONAL (on which H-*) / CORRECTED (state the
   corrected version, then prove it) / OPEN (say exactly what is missing).
2. A **correction ledger**: a numbered table of every place where my draft was wrong, too strong, or
   needed a hypothesis, with the fix. Include C-SIGN.
3. Numerical checks: any python you ran, with the numbers; keep it short.
4. A closing list "What a refuter should attack first", 3 to 5 lines.

Standard facts (Sz.-Nagy--Foias model theory, Paley--Wiener, the renewal theorem, GKLS) may be cited
as "standard (no local source)" per the notebook's convention; anything from SHW cite as
`1707.02266:TORUN.tex:<line>`. Be elementary and explicit; the reader will run numerics against
every formula. Do not pad.
