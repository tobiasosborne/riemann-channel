<!-- ROLE: live state. UPDATE POLICY: every session end. -->

# HANDOFF — riemann-channel

## Current state (2026-09-17: sidequest, Connes-Consani-Moscovici zeta spectral triples read, prototyped and planned as a standalone arb/FLINT library, `notes/zeta-spectral-triples/plan.md`; 2026-09-16: the Selberg zeta as a graded transfer whose odd-block form is derived from the letters (shards 03e/03f), Opus-reviewed; 2026-09-15, morning: the Ramanujan property for graded transfer channels defined (shards 02h/03c/03d), graded Harrow expanders with zeros, Pauli qubit = elliptic curve over F_5; 2026-09-14, night: zeta conditions catalogue (shard 06h); the yolo Lindbladian audited (negative, shard 04g); back to basics, the graded permutation and the physical letters; afternoon: the ring-norm-tensor campaign; morning: cMPS parity/supertrace theorem, two Lindblad papers, Weil numerator as ring norm)

Repo created from a single conversation in `../arithmetic-quantum-mechanics`
(session 2026-09-10/11, TJO with Claude Fable 5.1). Everything in this repo
is exploratory. The lab book, claim databases, and parity/CI gate described
below are in force. The founding conversation is in `transcript/transcript.md` (rendered from
the raw session log, which is kept out of the repository).

### CENTRAL PRIORITY (set by TJO, 2026-09-12 evening): the Bost–Connes reframe

Bost–Connes as used so far is side A only: a product state over primes,
ζ(β) a partition function, the dilation flow's spectrum the ring lengths
log n. The reframe (transcript and worklog, evening): **dilation time is the
one-dimensional space of a cMPS; the bond carries the Riemann Lindbladian;
its unique fixed point is the pole at s = 1, i.e. the critical KMS₁ state;
the zeros are its relaxation modes; the physical cMPS is pure and the KMS
state is its entanglement spectrum.** The Gibbs states at β > 1 are the
symmetry-broken steady-state manifold labelled by the Galois group, and the
BC phase transition is ergodicity breaking of the Lindbladian. RH is the
Ramanujan statement that all relaxation modes share one rate after the
e^{-t/4} rescaling (uniform gap = extremal object, "Riemann quantum
expander").

**Forced consequence (the fermionic zeros).** A cMPS ring norm is a positive
sum of squares (thm:cmps-ring-norms), while the zeros enter the explicit
formula with a minus sign (Deligne's third ingredient in shard 07; the
dips −2Λ(n)n^{-1/2} confirmed by review item X3). So the bond must be
Z₂-graded: the pole is the bosonic sector and carries the fixed point, the
zeros are fermionic modes, and the ring norm is a supertrace, which is the
ordinary norm of a fermionic ring with its parity insertion. This is the
curve picture (H¹ odd, counts 1 + qⁿ − Σαⁿ) and the Artin–Schreier lane
already carries the sign (S_n = −Σαⁿ). TJO: the Weil conjectures should
have the same fermionic interpretation; pursue the analogies concretely and
rigorously.

**Programme status after the night campaign (2026-09-12, "riemann-cmps").**
Items 0a–0c are done in the lab book (shards 02c, 04b, 04c, 06b; worklog
"Night: the Phantasm campaign"). What is now established, with proofs by the
codex prover and an Opus REFUTE review (0 INVALID, 5 MINOR, all applied): (i) rigidity, the supertrace of a
graded generator determines its net graded spectrum, and the explicit formula
forces the pole even and the zeros odd (finite parity flips excluded by
positivity; infinite flips open); (ii) the no-go, no finite or trace-class
operator has a genus ≥ 1 point count as trace sequence, so no bosonic MPS ring
norm can, and a zeta numerator is exactly an odd sector; (iii) the realisation,
on C_+ ⊕ (K_S ⊕ ladder)_- the generator 0 ⊕ B ⊕ diag(−(k+½)) has supertrace
exactly 2P_+, with Tr_dist Z(t) = 1 − 2P_+ − e^{−t/2}/(e^t − 1) (item 1c done);
(iv) the vacuum-decay Lindbladian on B(C ⊕ K_S): a genuine CPTP semigroup, zeros
as odd coherences, pair sums as even populations, PURE stationary vacuum, the
vacuum absorbing (renewal integral diverges) — so the SHW rebound state cannot
be the vacuum; (v) the prime-chain detailed-balance Lindbladian: Gibbs fixed
point, real spectrum (Minkowski sums of M/M/1 bands), no zeros; normal KMS
states only for β > 1; (vi) Artin–Schreier: the exact sign law
S_n = (−1)^{n−1} det(S|ker P_g(S)) Tr E^n (the founding α = −λ(E) claim was
FALSE in general; so was the orchestrator's conjugated replacement), the
corrected Frobenius block, N_n = str of the super-transfer matrix with even =
trivial character and odd = nontrivial characters, and E_g/√q = a
Weil-representation operator of an explicit symplectic M_g with
|S_n|² = q^{n + dim ker(M_g^n − 1)}. The two Lindbladians are complementary
halves (obs:complementary-halves); the Phantasm needs both
(conj:phantasm-both-halves, which replaces 0b).

TJO's steering in the campaign: the bond fixed point IS the entanglement
spectrum (so the Gibbs entropy and its cutoff laws are entanglement data;
`scripts/bc_entropy.py`; Hagedorn level density, no CFT reading); and the
Phantasm must carry Ẑ^× = Gal(Q^ab/Q), which gives the trivial-vs-nontrivial
character reading of the grading and conj:galois-graded-bond.

**Programme, next, in order.**
0a'. **Γ_0(N) model space** (conj:galois-graded-bond): compute the scattering
    determinant of Γ_0(N) (Dirichlet L-functions by character), the exit space
    C^h, and check that the Shor map acts on the bond as the level-N Galois
    symmetry with the L(s,χ) zeros in the χ-sectors. Numerics first (small N),
    then prover.
0b'. **Both halves** (conj:phantasm-both-halves): the SHW renewal equation with
    a MIXED rebound state Ω on K_S; the obstacle is the missing identification of
    K_S with the Bost–Connes bond (shard 04). Try the character decomposition of
    0a' as the identification.
0c'. **Infinite parity rigidity** (obs:parity-infinite-open): the prover
    isolated the missing step (negative mass at prime-power atoms of μ − comb);
    a positivity-alone argument or a counterexample-shaped obstruction.
0d. **Mayer cusp tail** (`notes/resonances/astra-freeassoc.md` §3): unchanged.
0e. **Suzuki's prime-defined screw kernel** (§16.3): unchanged.
0f. **Literature:** Bonthonneau–Weich; Lewis–Zagier, Chang–Mayer: unchanged.

### Sidequest 2026-09-17: zeta spectral triples (Connes-Consani-Moscovici, arXiv:2511.22755)

TJO asked for a careful reading and a concrete plan for a highly optimised, extensible arb/FLINT C
implementation of the paper's algorithm, as a possible standalone repository. Delivered in
`notes/zeta-spectral-triples/` (`plan.md`, `ccm_proto.py`, two runs, `flint_smoke.c`); worklog 2026-09-17.

- The algorithm: window `[lambda^-1, lambda]`, `2N+1` Fourier modes, Weil form matrix of Loewner form
  `(b_n - b_m)/(n - m)` (pole term rank two, primes `<= lambda^2` as atoms, archimedean part by
  digamma/trigamma plus `e^{-2L}`-series), even-block minimal eigenvector `xi`, rank-one perturbation
  of the scaling operator, spectrum = real zeros of `sum_j xi_j/(j - s)` scaled by `2 pi/L`. The mpmath
  prototype reproduces the paper's `lambda = sqrt 13, N = 120` column for all 50 zeros to every
  printed digit (first zero to `2.4e-55` from primes `<= 13`).
- Found: a typo in the paper's displayed constant `c(L)` (identity shift only; `eps_N` moves, the
  spectrum does not); the secular function has several roots per pole interval (root isolation must
  use the `2N` count); the accuracy law `|z_1 - gamma_1| ~ 5e4 (1 - chi_4(lambda))`, about `5.5`
  digits per unit `lambda^2`.
- Plan: `libzst` on FLINT 3 (all needed calls verified on 3.0.1 here), input = abstract
  explicit-formula distribution (atoms, exponential-series kernels, trivial-divisor poles, identity
  shift) so Dirichlet/Hecke/GL(2), graph and curve transfer operators (Caratheodory-Fejer anchor),
  Selberg compact and modular (H-CUSP-BRIDGE test), and the notebook's graded divisor formulation
  run through one pipeline; certified eigenpair (inverse iteration + Rump + LDL inertia for
  even-simplicity), certified roots, adaptive precision; milestones M0 (done) to M5.
- Not started: the repository itself. **Next, if TJO approves:** create `zst`, execute M1 (zeta
  pipeline, approximate) and M2 (certification), then the `(lambda, N)` accuracy map and the
  `x = 100` run.

### An infinite object whose odd-block form is derived from the letters (2026-09-16; shards 03e, 03f)

TJO asked for the most consequential step toward a proof; recommendation and execution: exhibit an
infinite-object zeta as a graded transfer whose odd-block unitarity is DERIVED from the letters,
Selberg first. Orchestrator draft D1-D8 (`notes/selberg-letters/draft.md`), one codex gpt-6-astra
xhigh lane (`astra-proofs.md`, 7 corrected / 1 open, 40-row ledger of which 34 are genuine
corrections, `scripts/selberg_letters.py` 131 checks in CI), Opus REFUTE review
`notes/reviews/selberg-letters-2026-09-16.md` (4 independent scripts, 153 checks, 31 citations
byte-checked; no BLOCKER/MAJOR; round 1: 7 VALID, 4 MINOR, applied; round 2: all VALID; verdicts
in the claims rows). Worklog
2026-09-16.

- **Z_S is the ring zeta of the stable two-term transverse complex** (even -X, odd -X+1;
  def:stable-transverse-complex; thm:selberg-two-term-ring-zeta): Z_S(s) = D_tow(s-1)/D_tow(s),
  retained divisor all odd, FE unconditional, RH/Ram iff Selberg's 1/4 (asm:selberg-coercivity).
  The Ruelle zeta (full transverse forms) FAILS FE/Ram: its even band is shifted by one. Closed
  geodesics are fermionic because dim E_s = 1.
- **First band, derived from the letters** (thm:selberg-first-band-form): Omega = lambda(1+lambda)
  on Res^0 (algebra), pushforward onto Laplace eigenspaces (DFG, cited by line), reality from Haar;
  the positive form is the ORTHOGONAL sum of branchwise pullbacks (the total pullback is degenerate);
  operator FE J X J^{-1} = 1 - X; Jordan block at a Laplace eigenvalue exactly 1/4, so full operator
  HP needs the strict bound. What is extra: the 1/4 coercivity, the Poisson bridge, strictness
  (thm:letters-derived-selberg).
- **Finite theorem** (thm:hashimoto-lift-metric, thm:letters-derived-finite): for graphs and graded
  quantum Hashimoto lifts, inverse pushforward F_mu, companion model, letter-derived metric
  G_C = [[1, S/2],[S/2, q]] with C* G C = q G, positive iff STRICT band; exact endpoint
  counterexamples (K_3 x Q_3; a ten-letter Pauli channel). Settles the "Hermitian channel plus
  lift => odd block unitary" open item (inverse-paired setting).
- **Negatives:** no doubled-bond CP realisation (flat supertraces are negative distributions,
  prop:selberg-no-cp-realisation); K-type parity is not a flow grading and does not supercancel
  (prop:ktype-not-flow-grading; obs:selberg-grading-choice corrected); the first-band operator form
  of the continuous Ihara-Bass is proved, the full-tower compression is not (prop:selberg-ladder-ihara).
- **Where it stops, the Riemann side** (obs:modular-scattering-sector, OPEN): on PSL_2(Z) the Riemann
  zeros rho/2 are Selberg zeros (FJS divisor theorem, byte-checked); their first-band states push to
  Eisenstein Laurent coefficients outside L^2, so the Haar form is unavailable; the orchestrator's
  e^{t/2} rescaling was the WRONG rate (that sector's centre is -3/4 under RH; the Riemann model's
  -1/4 belongs to -conj(rho)/2; not identified); truncated Maass-Selberg norms are positive
  throughout the strip; Selberg's 1/4 for PSL_2(Z) is KNOWN (Booker-Lee-Strombergsson, reported,
  not byte-checked). The missing object is H-CUSP-BRIDGE: a non-compact flow realisation with
  finite-rank resonant data at rho/2 - 1 and a positive modal pairing at the correct centre.
- **Next, if pursued:** (1) the bridge: DFG-type resonance theory for the modular flow (Dyatlov-
  Guillarmou cusp resonances) and the Eisenstein Laurent data as first-band states, with the
  correct centre; (2) identify or refute the affine relation between the scattering sector
  (-3/4) and the Riemann graded generator (-1/4) of 04b; (3) a positive form on regular data for
  the Eisenstein sector (Lax-Phillips, weighted), the exact shape RH must take here.

### The Ramanujan property for graded transfer channels (2026-09-15, morning; shards 02h, 03c, 03d)

TJO's quest item: a rigorous definition of the Ramanujan property from the graded MPS picture that
survives the continuum limit, with Harrow expanders as the test; and whether "we only have quantum
expanders for ungraded bond space / antiperiodic BCs". Orchestrator alone, then one codex
gpt-6-astra xhigh prover lane (`notes/ramanujan-graded/`). All rows sketched, author
claude:fable-5.1, unreviewed. Worklog 2026-09-15.

- **Answer: yes.** Every quantum expander in the literature and the book is ungraded; its ring zeta
  has only poles; the two closures coincide (prop:no-ungraded-zeros). Zeros are the odd-sector
  (parity-coherence) eigenvalues under the periodic closure.
- **Definition (def:graded-rh-fe-ramanujan):** on the divisor nu = m_even - m_odd of 1/sdet(1 - uE);
  growth q = Perron root; trivial set {q, period images, 1, FE partners}; RH = one-sided
  |lambda| <= sqrt q; FE = even similarity J E J^-1 = q E^-1; Ramanujan = both; manifest = E/sqrt q
  unitary for a Gamma_b-even positive form. Exactly eps-independent for e^{eps T}; in a Chernoff
  limit the grading survives only in the jumps (odd letters are never close to 1:
  prop:graded-chernoff). For infinite bonds: divisor of correlation functions of regular data, not
  the L2 spectrum (obs:divisor-regular-data).
- **The P-mode is structural, not trivial** (prop:p-mode; my own mid-session correction):
  sum_s eps_s A_s A_s^+ = r_P 1 gives E(P) = r_P P; r_P = 1 for the 06h tensor (H^0), -2 for the
  Pauli letters (inside the band, a pole pair on the circle), -(q+1) for all letters odd.
- **Graded quantum expanders exist** (thm:graded-harrow, thm:graded-qihara-bass,
  cor:graded-band-circle, prop:graded-alon-boppana): index-two (Clifford) gradings of Harrow
  channels; Ad P intertwines; trivial and sign reps both even; Harrow's bound sector by sector;
  graded Ihara-Bass with (1-u^2)^{n_k(D-2)/2} cancelling for balanced gradings; odd edge
  eigenvalues on |mu| = sqrt q are zeros. Verified: PGL2(F_5) and PGL2(F_13) principal series
  (chi of order 4) with bipartite LPS generators (5;13), (13;5); Pauli X,X,Y,Y,Z,Z on C^{1|1}
  gives (1+2u+5u^2)/((1-u)(1-5u)), the zeta of y^2 = x^3+4x+b over F_5 (prop:qubit-graded-zeta).
  `scripts/graded_ramanujan.py`, 79 checks, in CI.
- **Harrow's continuum limit is clean:** the representation Lindbladian; Ramanujan = temperedness
  of pi (x) conj pi (gap 1/2), no discrete divisor; graded PGL2(R) version = discrete series pairs,
  odd sector = archimedean ladder, closed geodesics EVEN (obs:graded-continuous-harrow). The grading
  that makes Selberg zeros odd is Dyatlov-Zworski's form degree (obs:selberg-grading-choice).
- **Prover lane (codex gpt-6-astra, `notes/ramanujan-graded/astra-proofs.md`): 4 proved, 9
  corrected, 1 refuted, 41 ledger rows, applied.** Biggest corrections: the LPS "genus 18/98" was the
  raw odd count; only the NET divisor survives ((5;13): numerator degree 4, no nontrivial poles;
  (13;5): 144/144 with 140 nontrivial poles); NO odd-sector Alon-Boppana (the letter P kills the odd
  sector; obs:odd-gap-no-alon-boppana); band iff circle only for the net divisor; trivial data must
  be a signed divisor with parities; the continuum needs two reference rates; "graded CP transfer" vs
  "graded spectral transfer" (Artin-Schreier / Riemann / Selberg have no supplied Kraus
  realisation); the PSL2(R) type-zero bound >= 1/2 is EQUIVALENT to temperedness; PGL2(R) pairs need
  even k >= 2; shard 05's "nontrivial zero" should have read "pole" (fixed).
- **Open:** a circle-type graded expander from a representation (odd block sqrt q-unitary by a
  mechanism; Artin-Schreier is the prototype); a Kraus realisation of the Artin-Schreier / Riemann /
  Selberg graded spectral transfers; the relation between "Hermitian + lift" and "odd block
  unitary"; the Repka 3/4 threshold vs Selberg 3/16 (unverified, do not cite); which Selberg grading
  is the Phantasm's. **Next, if pursued:** Opus REFUTE review of 02h/03c/03d against
  astra-proofs.md; then the K-type-0-vs-2 grading of a PSL2(R) representation channel as the
  candidate form-degree grading.

### Back to basics: the graded permutation and the physical letters (2026-09-14, night; shard 03b)

TJO restarted from the permutation (1 2)(3 4 5): one-matrix MPS, ring norms, the gas of rings
as l^2(N) with zeta a pure vector of square-root thermal weights, and the two oscillators with
energies 2 and 3. Recorded in shard 03b with `scripts/graded_permutation.py` (46 checks, in CI);
all rows sketched/numerical, author claude:fable-5.1, unreviewed. Worklog "Night".

- **Gas = oscillators is unique factorisation.** Point-letter ring norm = periodic points =
  Lambda_sigma(n); the gas is (x)_c l^2(N_0), H = sum l_c N_c, zeta = Tr e^{-beta H}; also
  zeta = Tr u^N Gamma(P) on the bond Fock space (sigma-fixed monomials = gas configurations);
  the thermal vector is a product state, Gibbs only on the diagonal algebra.
- **Grading a cycle odd induces zeros, with two more knobs.** Ramond closure: 1/sdet, zeros
  at the odd cycle's eigenvalues; holonomy places them; untwisted closure has none; the pole at
  1 is eaten unless a holonomy is used (rigidity/net multiplicity in miniature). A fermionic
  prime contributes 1 - u^l for every l; all primes fermionic gives 1/zeta (Moebius as fermion
  parity, zeros on Re s = 0, NOT the critical line).
- **Physical dimension principle (obs:physical-dimension-principle).** Ring norms see the
  letters only through the transfer channel: lower bound = Kraus rank (canonical up to a
  unitary), one letter = the channel itself. The sign lives only in even-odd coherences of the
  doubled bond: letters that record the bond parity kill the zeros (ladder at n = 6: one
  letter 1, one per cycle 13, one per point 5); partial recording at rate gamma shifts every
  odd eigenvalue by -2 gamma and no even one (prop:parity-jump-uniform-shift): the
  letter-level form of the uniform-rate statement, 2 gamma = 1/4 is the e^{-t/4}.
- **Jump operators of the Riemann cMPS (obs:jump-operator-guidance, TJO's question).**
  Prime jumps vs Galois jumps generate different dissipators, so it is a question about the
  Lindbladian. Galois jumps (character-diagonal unitaries) give character dephasing: they set
  the uniform rate and cannot produce frequencies; as a full per-step average they are a
  character measurement and remove the zeros. Prime jumps act on all character sectors and
  carry the lengths: the record; alone, real spectrum, no zeros. The grading must be
  transverse to the primes. The frequencies gamma_n need an even-odd Hamiltonian (or
  non-normal coupling) that neither family supplies. Ansatz shape: prime jumps + Galois
  dephasing at 2 gamma = 1/4 + even-odd Hamiltonian; RH = the dissipation on the even-odd
  coherences is pure dephasing. **Next:** test (e) in the finite covariant cones of shard 04d
  (does Galois covariance + a character-dephasing Kossakowski block + BC stationarity leave
  exactly an even-odd Hamiltonian free?); review shard 03b.

### The zeta conditions factor by factor (2026-09-14, night; shard 06h) — catalogue

TJO's complementary strategy after the negative: impose the zeta conditions one at a time on
graded ring norms, with tiny L-functions and completely concrete tensors. One astra lane
(`notes/zeta-conditions/`, 461 checks re-run; `scripts/zeta_conditions.py` 26 checks in CI).
- **Smallest example:** pair shift on m^2 letters with the diagonal odd, diag(1,[a=b]) on
  C^{1|1}: Z = (1 - m u)/(1 - m^2 u), one zero at q^-1/2 by half entropy, genuine gas, no FE.
- **Ledger C1-C10** as exact algebra; automatic: positivity, rationality, sign structure;
  constraints: integrality, genuine gas, FE, RH, unique fixed point (= simple Perron root +
  whole-bond TP gauge + mixing), Galois/Artin, realisability, continuum embedding.
- **Catalogue:** four-letter TP elliptic tensors on C^{1|1} (FE by a visible duality J, RH by a
  unitary odd block, unique maximally mixed mixing fixed point; affine, projective, supersingular
  with a real double zero); Pauli family proving FE/RH/mixing independent; Horner MPS for
  Dirichlet L over F_2[x] and F_3[x]; Gauss, Kloosterman (affine count of y^2+xy=x^3+1), a graph
  cover with reciprocal Bass quadratics; cMPS half entropy and amplitude damping with the additive
  FE Z(2-z) = Z(z).
- **Orchestrator corrected:** inverse-closed letters alone give no FE (diag(1,2)); the swap
  L-function is not an Artin factor; unique fixed point is three conditions; my duality matrix
  for the elliptic tensor was wrong twice before Z-conjugation on the even block.
- **Limits:** finite bond => rational Z, no atomic prime comb, periodic copies of finitely many
  divisor points under u = q^-s. Factor by factor tests local data; it does not build the infinite
  object. **Next, if pursued:** Opus REFUTE review of 06h (and 04g); a bond-cutoff family of
  four-letter-type tensors whose divisor points accumulate (the only route to non-rational
  behaviour), or the Selberg/Lax-Phillips side where the infinite object exists.

### The yolo Lindbladian and its audit (2026-09-14, night; shard 04g) — NEGATIVE

TJO asked for a bold guess of the Riemann Lindbladian from the circumstantial evidence, then had
two codex gpt-6-astra xhigh lanes investigate it (`notes/yolo-lindblad/`). The guess: bond
L2(Zhat) (x) L2(R_+^*), grading by the profinite Fourier mode, one prime jump V_p per prime at
rate 1/p (a Galois unit away from p, the shift at p), Galois dephasing at 1/4, archimedean
ladder + dilation Hamiltonian; the Ramanujan-sum sector as the K_S identification (0b').

- **Holds (exact):** the V_p isometries and their Galois covariance; the Ramanujan-shell
  formulas (the vacuum leaks into shell p); <c_b>_beta -> 0 iff b > 1; the inverse multiset sum
  prod_p (1 - p^-w V_p) has vacuum element 1/zeta(w+1/2); uniform Galois dephasing.
- **Fails (exact counterexamples):** the grading is not invariant; vacuum-character coherences
  are not modes; the vacuum generating functions are 1/(1 - S_P(s+beta+1)) and zeta_P(s+beta+1),
  shifted, with no singularity in the strip at any cutoff; shell Gibbs weights are not
  stationary; rates 1/p define no normal semigroup; the parity ring trace is not a trace at a
  prime cutoff; parity closure is not the Q^x quotient.
- **Orchestrator corrected:** inversion-asymmetric Galois rates DO produce frequencies (shard 03b
  obs:jump-operator-guidance (b) amended); "fermionic primes: zeros on Re s = 0" is per finite
  factor only (cor:moebius-fermion-parity amended).
- **Bearing:** phase-side prime jumps are side A (Euler product) with the Fourier side included;
  0b' unchanged; the Ramanujan-sum sector + prime jumps alone is ruled out. Unreviewed by a
  second family (both lanes codex). **Next, if pursued:** Opus REFUTE review of 04g; a
  summable-rate or radial local model with a genuine bond cutoff (lane A §8.4–8.6) before any
  metric question.

### The ring-norm-tensor campaign (2026-09-14, afternoon; shards 02g, 06c--06f)

TJO asked for an educated guess for the MPS tensor of the absolute simplest variety
without an obvious Polya--Hilbert Hamiltonian, with the wish list (1) natural tensor
from the variety, (2) graded decomposition and why, (3) ring norms = counts as a
theorem, (4) the PH operator, (5) Ramanujan, modulo gauge. Reading: in this notebook
the obvious PH Hamiltonian is the quadratic Artin--Schreier unitary E_g; that family
is supersingular (proved, every characteristic), so Tier A is the ordinary elliptic
curve and Tier B is ordinary genus two, where fermionic letters are forced. Lanes:
codex gpt-6-astra prover (`notes/ring-norm-tensor/astra-proofs.md`), Opus numerics
(`scripts/ring_norm_tensor.py`), Opus sources (`notes/ring-norm-tensor/sources.md`,
nine new TeX e-prints), Opus REFUTE review (`notes/reviews/ring-norm-tensor-2026-09-14.md`).
Full account: `docs/worklog/2026-09-14.md`.

- **Tier A answers all five items** (conditional on Deuring lifting, degree = norm,
  toral Lefschetz, all byte-cited or assumed): the natural tensor is the lifted
  Frobenius as a toral endomorphism M of C/Lambda; N_n = det(1 - M^n) = |1 - pi^n|^2 =
  |O/(pi^n - 1)| is literally a ring norm and a Lefschetz number; ket bond
  Lambda^*(H^{1,0}) = C^{1|1}, double = H^*(T^2), grading = form degree, ket/bra =
  Hodge decomposition, (-,-) = H^2 with eigenvalue q = the degree; PH unitary =
  q^{-1/2} M^* on harmonic one-forms, unitary because the lift is a conformal
  similarity of degree q (positivity = the degree form, Hasse's bound follows); gauge
  = lattice basis, classes = ideal classes (Latimer--MacDuffee, Waterhouse), unitary
  gauge = Hodge basis. The physical state is a product state; the Fourier pullback is
  an injection whose only finite orbit is the zero mode.
- **Correction of the orchestrator.** The morning's drafted bound
  sum_odd |mu|^2 <= 2 Tr(E_++) Tr(E_--) is false (Tr(A (x) conj A) = |Tr A|^2); both
  the prover and the numerics lane caught it. The genus bound g <= 1 for bosonic
  letters without cancellation is proved instead by |Tr M^n|^2 <= Tr S_+^n Tr S_-^n
  for all n plus a Cesaro argument. Infinite-bond version: fermionic jumps are forced
  under explicit Hilbert--Schmidt hypotheses (`asm:kraus-hs-setting`).
- **Tier B.** The literal geometric placement and the drafted vacuum ansatz are
  impossible; an explicit nine-letter tensor exists for q + 1 >= 4 sqrt q
  (depolarising even block, diagonal odd block, normal transfer); a two-even, one-odd
  tensor for y^2 = x^5 + x^3 + x^2 - 2 over F_5 is certified by an exact rational
  contraction argument (`scripts/ring_norm_certificate.py`); the Jacobian is the
  bosonic product of two genus-one rings with the curve a rank-six non-product
  boundary inside it; Rosati positivity forces conjugation at every CM place and is
  the PH metric; CM type is a marking, not a gauge. Numerics: the CM-diagonal ansatz
  with two odd letters solves genus two; no closed form is pinned by the counts.
- **Open:** universal three-letter tensor and its natural selection
  (`conj:three-letter-universal`); bosonic cancellation on larger bonds; whether the
  certified tensor's unitary similarity is an even gauge carrying the Hodge metric;
  the amplitude-locality conjecture (`conj:amplitude-locality`).
- **Explicit examples (evening, shard 06g, `scripts/ring_norm_examples.py`):** one MPS
  per genus 0-3 written out (genus 3 over F_37 from three brute-force counts); every
  odd mode has correlation length 2/log q (that is RH); block Schmidt spectra from the
  doubled bond, entropy <= 2 log D, closed forms give flat spectra (log 8, log 12);
  parent Hamiltonians with the periodic fermion ring selected by a parity-twisted
  boundary term. Unreviewed.
- **Next rung, if TJO meant a Deligne-type variety:** the simplest is a curve with
  coefficients (an elliptic surface over F_q(t) with degree-2 L-function, a K3 with
  Picard number 20). Note: a surface's middle cohomology is EVEN, so its interesting
  eigenvalues are bosonic and the Ramanujan shape is the graph one (trivial q^2,
  nontrivial |beta| = q); the fermion enters as odd(base) (x) odd(fibre) = even.

### Finite BC symmetry calculation (2026-09-13, Codex)

TJO clarified the inverse problem: the BC state is the stationary state of an
unknown Lindbladian, constrained by Galois symmetry and adelic symplectic
structure. The no-event generator and the jumps are BOTH unknown. The
fixed-B scalar-reset positivity test is one ansatz, not the whole problem.

First finite constraint calculation completed: `notes/bc-symmetry-generators.md`
(full arguments B0–B6), shards 02e/04d, `scripts/bc_symmetry_generators.py`,
captured output, four source quotes reused from local TeX. New arguments
are **unreviewed**, hence `sketched` in the database; no independent review
was performed or implied. Nine new claim rows, four definitions.

- The critical BC restriction to finite phases is uniform. Extending those
  probabilities to M_p adds state data. No finite-dimensional unital
  representation of the full BC algebra retains its nontrivial phase
  observables: finite isometries are unitary, forcing e(r)=I.
- At odd prime p and the critical tracial extension I/p, the exact real
  span dimensions of GKLS cones are (p−1)(p+1)^2 for Galois covariance,
  2p−2 for full linear Weil covariance, p+1 for Weyl+Galois covariance,
  and 1 for Weyl+Weil covariance. The cone is linear constraints plus
  conditional Choi positivity; positivity has an interior point.
- Full Weyl-translation covariance is an EXTRA assumption, not synonymous
  with carrying the symplectic structure. With Galois it makes the spectrum
  real; with full Weil it leaves only depolarization.
- Full linear Weil covariance alone permits unequal odd decay rates:
  an explicit p=7 conditional-Choi-positive perturbation has odd
  eigenvalues −1−epsilon and −1+epsilon/2 ± i sqrt(3)epsilon/2,
  epsilon=1/196, each eight times. No zero positions were fitted.
- Two-prime covariant CP couplings can vary while both one-prime dynamics
  remain fixed. CRT marginal compatibility does not select the coupling.
- 427 numerical checks at p=3,5,7, including independent orbit/Burnside
  counts, actual finite-time Choi positivity, state extensions, odd spectra,
  and two-prime restrictions. The script is included in local CI.

**Next:** an arithmetic representation or CP comparison map connecting the
finite phase/Weil data and the full BC prime isometries to the scattering
bond. This should specify which symmetries commute with the dynamics and
which act covariantly on the construction, and constrain the Kossakowski
blocks and inter-prime couplings. The Gamma_0(N) scattering/character
calculation above remains OPEN; this finite matrix calculation does not
complete it. Prime powers, the real place, metaplectic compatibility,
the critical operator-algebra limit, and the physical cMPS remain open.
The new statements should receive independent review before promotion.

### Two Lindblad papers read (2026-09-14, two Opus readers) and the mixing-time question

TJO's hypothesis: Ramanujan properties are tightly related to MIXING TIMES of
Lindbladians. Two new papers were read from TeX (sources in refs/src, notes
`notes/extract/2609.13121-reading.md`, `notes/extract/2609.12284-reading.md`,
quotes line-checked by the readers; no lab-book rows yet).

- **2609.13121, Becker–Zworski, "Optimal relaxation for Witten Lindbladians
  (in 1D)".** One jump a = h d_x + V', pure fixed point |nu><nu|. Trace-norm
  decay at exactly the gap lambda_1(h)/(2h) for a REGULAR class of inputs,
  sharp; no uniform exponential decay on all trace class (1/t example, in
  the untypeset tail of the latexdiff source). SUSY intertwining (d_y moves
  to the partner aa* with no zero mode) + maximum principle. Relevance:
  suggestive, one-sided (slowest rate only); same pattern as our vacuum-decay
  Lindbladian with a Gibbs diffusion on the diagonal ("both halves" under
  one jump) but self-adjoint H, so real rates, no zeros. Nothing on cMPS,
  grading, expanders, cutoff.
- **2609.12284, Shang, "A Simple Quantum Linear-System Solver via
  Dissipation".** Purely dissipative reset Lindbladian with pure fixed point
  encoding A^{-1}b, A non-normal allowed; worst-case mixing O(kappa^2 log 1/eps),
  dimension independent, matching lower bound for the family; proof via a
  Poisson-equation / absorption-time argument, no spectrum. Reader-derived
  (not in paper, numerically checked): spectrum real, gap in
  [sigma_min^2/2, sigma_min^2], Jordan blocks at tuned parameters invisible to
  mixing. Relevance: weak; in the notebook's "no-event generator + scalar
  reset" class.
- **Convergent negative (UNREVIEWED, both readers independently):** for the
  Riemann semigroup, ||Z(t)|| = 1 for all t, with or without RH. Argument:
  reproducing-kernel bound ||Z_t|| >= e^{-eps t} - |S(x - i eps)| and
  |S(x - i eps)| -> 0 as x -> infinity (mpmath at eps=0.2: 0.72, 0.60, 0.095,
  0.027 at x = 10, 100, 1000, 5000; heuristic Gamma decay t^{-2 eps} against
  convexity t^{eps}). Consistent with the recorded Riesz-basis dead route.
  Consequence: RH cannot be a WORST-CASE mixing-time statement for these
  channels (no bounded G with B^dag G + G B = -G/2 on all of K_S); a mixing
  form must restrict to regular data or a weighted norm — exactly the shape
  of Becker–Zworski's theorem.
- Pointer (from memory, NOT yet checked against a source): Lubetzky–Peres,
  "Cutoff on all Ramanujan graphs" (GAFA 2016) — the natural Ramanujan ↔
  mixing link; quantum analogue for Weil–LPS channels is an open question.

**Next, proposed (not started):** (1) review the ||Z_t|| = 1 argument and
record it as a negative; (2) truncated-zero numerics: sup_t e^{t/4}||Z_t^(N)||,
Gram condition number, integrated Gramian versus N; (3) fetch Lubetzky–Peres,
ask for cutoff of Ramanujan quantum expanders (Weil–LPS); (4) the regular
data class on which "all rates 1/4" ⇔ uniform e^{-t/4} decay.

### Discussion 2026-09-14: Weil numerator as a boson–fermion ring norm

TJO: for elliptic curves the zeta has numerator and denominator; natural to
realise via ring norms of an MPS with fermions and bosons. Answer (discussion,
not registered): by the twisted-ring theorem the P-closed ring norm is
str E^n on the doubled bond; the untwisted closure is excluded by
thm:no-ungraded-trace. Minimal bond C^{1|1} has even and odd doubled
sectors of dimension 2 each, exactly {1,q} and {alpha, conj alpha}. Even a
BOSONIC tensor A_s = diag(a_s, c a_s), sum |a_s|^2 = 1, |c|^2 = q gives
||Psi_P||^2 = ||Psi_+ - Psi_-||^2 = |1 - conj(c)^n|^2 = 1 + q^n - alpha^n -
conj(alpha)^n: Hasse's N_n = deg(1 - phi^n) in MPS clothing. Cauchy–Schwarz
on the cross transfer gives the one-sided bound |alpha| <= sqrt(1*q) for
free (decoupled blocks); the functional equation is the equality case.
Caveats: alpha is put in by hand (circular); the real question is a tensor
from the curve (test: can the Artin–Schreier super-transfer be written as a
P(x)conj P graded E = sum A (x) conj A?); genus >= 2 needs cancellations in
the (-,-) block and presumably fermionic couplings, where C–S is no longer
free. Wording note: cor:curve-counts-graded is correct as stated (it names
Tr(sum A (x) conj A)^n, periodic closure) but a bosonic MPS with boundary P
does realise genus-1 counts; add "with periodic closure" when next touched.

### The fermion parity of a cMPS ring (2026-09-13, Opus, alone)

TJO was cautious about "the ring norm is a supertrace" and asked whether it
had been proved (it had NOT: only the lattice fMPS contraction was cited,
cit:fmps-supertrace) and for a direct rigorous calculation of <(-1)^F> in a
general boson–fermion cMPS ending in str and sdet. Done without subagents
at TJO's instruction: shards 02f, 04e, 04f (Lamport proofs), script
`scripts/cmps_parity_supertrace.py` (89 checks against explicit
Jordan–Wigner Fock vectors; in local CI). All new rows `sketched`
(unreviewed, author claude:opus-5).

- General data (no grading): <Psi_B'|(-1)^F|Psi_B> = Tr[(B⊗B̄') e^{L T_eta}],
  T_eta = Q⊗1 + 1⊗Q̄' + Σ eta_a R_a⊗R̄'_a; a signed sum of squares. The
  absence of any sign in the plain norm is a proved step (ordered creation
  vectors contract without sign), not a convention.
- With a bond grading P: (-1)^F Psi_B = Psi_{PBP}, so <(-1)^F> = ±1 for
  B = 1, P, Pi_±. The physical parity carries NO spectral information.
- The supertrace lives on the doubled bond, Gamma = P⊗P̄ (odd = block
  off-diagonal coherences): ||Psi_P||² = str e^{LT}, ||Psi_1||² = Tr e^{LT};
  odd trace = 2 Re<Psi_{Pi-}|Psi_{Pi+}> (interference); Psi_P is the
  periodic (Ramond) fermion ring, Psi_1 the antiperiodic one.
- Ring-length transforms: ∫e^{-zL}||Psi_P||² dL = str(z−T)^{-1} =
  d/dz log sdet(z−T); Frullani gives sdet(z−T)/sdet(z0−T); ring zeta
  1/sdet(z−T), poles net even, zeros net odd.
- Bearing: the HANDOFF sentence is a theorem for finite bonds, sharpened
  (obs:cmps-supertrace-reading). Open: infinite bonds; review.

### Latest discussion: Ramanujan conditions in Q and R (2026-09-13)

TJO asked for the shape of the Ramanujan property directly in the matrices
of a boson–fermion cMPS. The response is preserved in
`outputs/ramanujan-boson-fermion-cmps.md`; the human-readable deliverable is
`outputs/ramanujan-boson-fermion-cmps-fmd.pdf`, with its self-contained HTML
at the same stem. This is an unreviewed discussion export, not a new set of
registered/proved lab-book claims.

**Refinement of the preceding calculation:** the finite covariant-GKLS
cone did NOT impose regular mixed-cMPS relations. For the standard
finite-kinetic-energy regularity condition, Q is even, R_b even, R_f odd,
and R_alpha R_beta = (−1)^(p_alpha p_beta) R_beta R_alpha; in particular
R_f^2=0. Canonical normalisation is Q = −iH − (1/2) sum R_alpha^dag R_alpha.
Thus parity covariance alone does not make a generator a regular cMPS of
the specified species. Source: the existing local cMPS calculus paper,
1211.3935, `calculus.tex`, regularity and transfer sections.

The observable-convention fermionic correlation transfer is
K_f(X) = Q^dag X + XQ + sum_b R_b^dag X R_b − sum_f R_f^dag X R_f.
The ordinary norm-transfer generator has PLUS signs for every species and
generates a CP semigroup; multiplication X -> PX intertwines it with K_f.
The candidate arithmetic sector E must be identified separately from the
entire odd operator space. For A = K_f restricted to E, the one-sided
bound is Re spec A <= −Delta; an additional reflection
lambda -> −2Delta − conjugate(lambda) makes this a line condition.
In the Riemann convention Delta=1/4. For a finite block, the concrete test
A^dag G + G A = −2Delta G with G>0 is equivalent to the line spectrum AND
diagonalizability. The metric G is additional structure; it is not
automatically the inner product from the BC stationary state.

A regular two-fermion example was checked in-session, numerically and by
an exact SymPy characteristic polynomial: R_j=sqrt(kappa)c_j,
H=g(c_1^dag c_2^dag+c_2c_1), Q=−iH−(kappa/2)(n_1+n_2).
The elementary odd span of c_j,c_j^dag has rates −kappa/2 ± ig;
the full odd space also has −3kappa/2 ± ig. The exact full odd polynomial
is [((z+kappa/2)^2+g^2)((z+3kappa/2)^2+g^2)]^2.
These scratch checks are described in the export, not yet a registered
evidence script or independently reviewed theorem.

The stationary-state Dirichlet identity for K_f uses commutators with R_b
and anticommutators with R_f. Regularity makes it vanish at X=R_f, so a
strict instantaneous coercivity bound in that metric cannot hold on a
sector containing an R_f with nonzero stationary-state norm (in particular
for a nonzero R_f and faithful stationary density). A spectral gap or a
different positive metric can still exist.

**Next mathematical work, when requested:** impose the regular graded
Q,R algebra together with BC stationarity and the arithmetic covariance;
identify the sector E from the explicit formula/scattering comparison;
seek the positive metric or the one-sided bound plus arithmetic duality.
The full adelic representation, domains and metric completion remain open.
The finite-GKLS counterexample above must not be presented as a
counterexample within the narrower regular mixed-cMPS class.

**Export tooling:** at TJO's request a Luna subagent installed the official
checksum-verified `fmd` 0.4.2 at `/home/tobiasosborne/.local/bin/fmd`.
This version takes `$...$` / `$$...$$` math delimiters. Its HTML renders
MathML, but native PDF leaves LaTeX as text, so the delivered PDF was made
by rendering HTML with fmd and printing it with headless Chromium. The
unsupported decorative `\\boxed` wrapper was removed without changing its
equation. A wording correction distinguishes the CP semigroup from its
generator. All 37 expressions were rendered and the two-page PDF inspected.

TJO's closing instruction is to update this handoff, commit and push the
session changes, then stop work. Do not autonomously resume the research.

### Sidequest 2026-09-13: Ihara zeta functions of simplicial complexes (done)

TJO's question: the fermion–zeros connection for graphs looks central and the
zeros seem to carry "surface-like" qualities, so is there a natural Ihara-type
result for simplicial complexes, and what is its quantum generalisation?
Answered in one day (four Opus lanes, one codex `gpt-6-astra` prover, Opus
REFUTE review: round 1 0 INVALID / 3 MINOR / 44 VALID, MINOR items applied, round 2 47/47 VALID). Lab book: shards 02d,
08d, 08e, 08f; note `notes/complex-zeta.md`; sources
`notes/extract/complex-zeta-sources.md`, `notes/extract/cohomological-zeta-sources.md`;
proofs `notes/complex-zeta/astra-proofs.md`; numerics `scripts/a2_complex_zeta.py`.

- **Literature.** The result exists for building quotients only: Kang–Li
  (PGL_3), Fang–Li–Wang (Sp_4), Kang–Yu (PGL_n, July 2026): an alternating
  product over cell dimension of geodesic-flow determinants equals
  (1−u^n)^χ times the vertex Hecke L-function, χ-factor a cochain torsion,
  RH ⇔ Ramanujan with each factor's zeros on prescribed circles. LLP: the
  higher Hashimoto operator is the geodesic flow; higher-rank RH is the
  one-sided band Re s ≤ 1/2 with interior poles present (Kamber: L_p-expander
  ⇔ one-sided bound). No Ihara zeta for a general complex exists and four
  papers say so. Storm's hypergraph zeta is a graph zeta. Cohomological side:
  Deitmar (degree-weighted supertrace), Dyatlov–Zworski, Knill's graph
  torsion (never joined to Ihara), Matsuura–Ohta's Berezin proof of Bass
  (chirality vertex/edge, not Grassmann parity). Quantum side: empty.
- **Prover (astra), all reviewed VALID.** The object that "wants to exist" is
  the graded geodesic determinant with SPECIFIED data (states, successors,
  algebraic lengths, transports; parity k+1). Corrections to the drafted
  statements: the rule "add a vertex not closing a cell" gives outdegree
  2q²+q on the Ã_2 building, Kang–Li's L_E needs link OPPOSITION (q²), a
  building notion; the graded total is the completed vertex L-function
  D_B/D_E = (1−u³)^χ/det P_3, not Kang–Li's 1/D_E; a universal Bass–Schur
  identity holds for every complex and arbitrary weights (rational
  compression by one dimension) but the vertex-level polynomial identity is a
  building phenomenon (∂Δ³: 𝒵 = (1−u⁴)⁶, no matrix polynomial works); on the
  building vertex side every chamber root cancels, the reduced vertex
  L-function is a reciprocal polynomial with NO finite zeros, so "fermionic
  zeros" is net odd multiplicity in a graded presentation, to be checked after
  cancellation; the k-cells ↔ H^{k−1} dictionary is parity only (one tempered
  constituent feeds two circles); Tr Ad(B_w) = |Tr B_w|² needs no pairing; the
  no-go's operative hypothesis is "honest trace", not positivity; chronological
  weights π(s) are not flat, the covariant twist on the full Cayley complex is
  pure gauge, the genuine Artin block is the voltage quotient with
  det(1−uT) = ∏_ρ det(1−uT_ρ)^{dim ρ}; Harrow transfer gives Ramanujan quantum
  expanders of type Ã_{d−1} for every representation, with an exceptional
  space and an exact converse criterion.
- **Numerics (PGL_3(F_3), 5616 vertices, LSV generators).** Link = PG(2,3),
  χ = 29952, NOT 3-colourable (Kang–Li's type hypothesis fails) yet the
  corrected identity holds exactly to u^18 on the base and on the 16848-vertex
  type-preserving cover; all 5615 nontrivial vertex eigenvalues tempered;
  block radii {3, √3} for L_E and {1, 3^{1/4}, √3} for L_B; the 12-dim twist is
  a Ramanujan quantum expander of type Ã_2 (|13μ| ≤ 6.4817 < 2√12, all 143
  joint eigenvalues in the deltoid); Euler-factor bookkeeping per block.
- **Bearing on the programme.** None of this touches the Riemann side. It
  sharpens the graph/complex half of the fermionic analogy: the odd sector of
  a complex is real as a graded presentation and cancels on the vertex side;
  the surviving "surface-like" fact is the alternating structure over cell
  dimension with its χ-torsion. Open (conj:vertex-collapse-characterisation):
  which complexes beyond buildings admit a vertex-level collapse. Possible
  follow-ups, not scheduled: the Knill-SDet ↔ Ihara join; a voltage-quotient
  channel zeta for the Weil–LPS channels (shard 05) to compare with the Ã_2
  case; Ã_3 numerics (PGL_4(F_2), LSV e > 1 needed for q = 2).

Dead routes recorded today: SPT protection (signs, not moduli);
PSL(2,Z)-generator channels (expanders, not Ramanujan); "GUE positions with
equal widths is the fingerprint of scalar loss" (false: one-port inverse
design realises any equal-width poles; the information is in the couplings,
`astra-freeassoc.md` §1); a bounded renorming of K_S (Riesz-basis
obstruction: Gram condition number 10 → 700 across the 3000 zeros).

### What was established (standard theory, numerically confirmed)

1. **Quantum Ihara–Bass.** For a unital channel with D unitary Kraus
   operators closed under adjoint, the non-backtracking edge superoperator T
   on M_n ⊗ C^D satisfies det(1 − uT) = (1 − u²)^{n²(D−2)/2} det(1 − uDΦ + (D−1)u²).
   Verified to 10⁻¹⁵ (`scripts/qihara.py`). RH for this zeta ⇔ Φ is a
   Ramanujan quantum expander (Hastings' bound). AKLT gives the K₄ Ihara zeta.
2. **Bost–Connes as MPO over the prime chain.** ℓ²(ℕ) = ⊗_p (oscillator at p);
   Gibbs state is a product state; μ_n local; e(a/b) is an MPO with bond
   space ℤ/b whose local transfer map is r ↦ p^k r (Shor's map). Transfer
   eigenvalues in the character basis are L(β, χ̄)/ζ(β). Extremal KMS states
   differ by the boundary residue; β → 1⁺ kills every nontrivial sector.
   Verified against Hurwitz-zeta sums and mpmath L-functions (`scripts/bcmpo.py`).
3. **The Riemann channel.** S(τ) = ξ(1−2iτ)/ξ(1+2iτ) is unimodular on ℝ,
   inner in Im τ < 0, zeros at γ_n/2 − iβ_n/2; its phase equals the imaginary
   part of the β = 1 BC Lévy exponent (prime sum, PNT tail; residual 10⁻³).
   The functional-model semigroup has one mode per zero, decay β_n/2,
   frequency γ_n/2; RH ⇔ uniform rate 1/4 (`scripts/scat.py`).
4. **Ring norms = primes.** Windowed zero sum over 3000 zeros matches the
   full Weil explicit formula to 0.2 on a scale of 147; dips at u = log n of
   depth ∝ Λ(n)/√n including prime powers (`scripts/ringnorm.py`).

5. **Weil–LPS channels built and verified** (2026-09-11, `scripts/weil_lps.py`,
   `notes/weil-lps-channels.md`). For (p; q) in {(5;29), (7;29), (11;5),
   (13;17,29), (17;13), (19;5,17), (29;5,13)}: the q+1 norm-q quaternions map
   into SL₂(F_p); the Weil representation is built numerically with the
   intertwining relation checked to 10⁻¹⁴; the channels on the even and odd
   Weil blocks are Ramanujan quantum expanders in every case (Hastings bound),
   with a unique fixed point; Harrow containment in the PSL₂ Cayley spectrum;
   Hecke relation A_q² − qI = A_{q²} and multiplicativity A_{q1}A_{q2} = A_{q1q2}
   exact; channels for different q commute to 10⁻¹⁵; the direct edge
   superoperator for (13,17) has |μ| ∈ {17, √17, 1}, so its quantum Ihara zeta
   satisfies RH exactly. Not done: LMFDB identification of the joint spectrum.

6. **MPS formulation of the Weil conjectures for quadratic Artin–Schreier
   curves** (2026-09-11, `scripts/artin_schreier_mps.py`,
   `notes/artin-schreier-mps.md`). In a normal basis Frobenius is the cyclic
   shift; for g(x) = Σ a_j x^{1+q^j} the exponential sum S_n is Tr(Eⁿ) for a
   q^J × q^J transfer matrix (odd n exactly; even n with the sign that makes
   S_n = −Σ α_iⁿ). E E† = q I whenever a_J ≠ 0, so RH is manifest: the
   transfer matrix is √q times a unitary. Beyond quadratic g the trace form
   is non-local and n-dependent in the shift basis; the uniform formulation
   is Dwork's p-adic transfer operator, which gives rationality and the
   functional equation but not RH.

### What is NOT established

- RH. Everything above is equivalent to, not a proof of, the uniform-rate
  statement.
- A Stinespring form of the compressed semigroup Z(t) with the prime
  dilations as jump (Kraus) operators. This is the open question isolated by
  `notes/riemann-channel-note.md` §7.
- Any identification with the Phantasm constructions in the parent repo
  (SP-PRIME, SP-BC-CONTROL are β > 1 objects).

### Ideas raised but not pursued

- Selberg as the continuum limit: MPS matrices ↔ flat U(χ) connection on a
  hyperbolic surface, rings ↔ closed geodesics, twisted Selberg zeta =
  one-loop determinant (D'Hoker–Phong, Sarnak). TJO flagged the functional
  integral framing as going too far; the "length quantisation is a flatness
  condition" reading was later matched by the product formula ∏_v |p|_v = 1.
- Shor's unitary U_a : x ↦ ax mod N is the level-N Galois symmetry of BC and
  a single-time snapshot of the dilation flow; its periods are governed by
  Dirichlet L-function zeros, not ζ's.
- Holevo's Lévy–Khinchin classification of dilation-covariant CP semigroups
  gives the *form* of any quantum lift of BC: prime jumps + Gaussian
  (archimedean) part + Hamiltonian part. Dilation theorems supply existence
  only; positivity (Weil's criterion) is where RH lives.

7. **Deligne's proof via graphs** (2026-09-12, `notes/deligne-via-graphs.md`,
   expository). The three ingredients a Hilbert–Pólya approach would have to
   replace: products (eigenvalues multiply, trivial loss fixed), slicing over
   a curve (the core theorem is about a curve with matrix coefficients, i.e.
   a twisted Ihara zeta), and the sign (interesting eigenvalues are zeros,
   not poles). Deligne exhibits no Hermitian form; Weil and Artin–Schreier do.

8. **Prior art and the general Kraus Ihara–Bass formula** (2026-09-12,
   `notes/prior-art-quantum-ihara.md`, `notes/quantum-ihara-general.md`,
   `refs/`). Literature check with byte-verified TeX quotes: the
   Ad(U)-weighted Ihara zeta and its Bass formula are Matsuura–Ohta 2022
   (arXiv:2204.06424); arbitrary-weight Bass for loopless graphs is
   Watanabe–Fukumizu 2011; twisted zetas go back to Sunada 1986. NOT found:
   any zeta of a quantum channel, "RH ⇔ Ramanujan quantum expander", the
   MPS/ring-norm reading. Exactly-Ramanujan channels from LPS via Harrow are
   in Iyer–Jain–Jordan–Somma arXiv:2602.15180 (SU(2) irreps); the Weil
   instance is ours. Then proved: Ihara–Bass for the non-backtracking
   superoperator of an ARBITRARY Kraus family (Theorem 1, Lamport proof,
   Corollaries 2–4: adjoint pairing + positive trace formula; unitary case;
   pole bookkeeping). Numerics float 1e-15 and exact sympy. Adversarial
   review by Opus (author Fable): round 1 algebra VALID, provenance fixes
   applied; round 2 receipt in `notes/reviews/round2-2026-09-12.md`.
   Convention: status `proved` requires a reviewer ≠ author; both are Claude
   models (single family declared), no codex lane used.

9. **The continuous (Selberg) dictionary** (2026-09-12 night,
   `notes/selberg-dictionary.md`, `notes/selberg/astra-proofs.md`, lab-book
   shards 09b/09c, `scripts/selberg_lindblad.py`). Proved by the codex prover
   (`gpt-6-astra`), reviewed by Opus: circle comb and its blindness to zeros
   (orbital trace only); Lindbladian of the sl2 vector fields = 2Ω = −2Δ on
   the K-invariant sector (Casimir has the compact direction with a minus
   sign); Poincaré Jacobian 4 sinh²(kℓ/2); flat trace ↔ tower
   D(ς)=∏_{j≥1}Z(ς+j) with Λ_fl = +D'/D; tower zeros in bands −½−k±ir_j,
   nonconstant first band on Re ς = −½ iff no eigenvalue in (0,¼); Ruelle =
   Z(s)/Z(s+1); modular cusp term = prime comb with dips Λ(n)/n at 2 log n
   plus an exact +½ from the pole of ζ; e^{−t/4}·(channel prime measure) =
   cusp prime measure. Six standard inputs are `assumed` rows (dependants
   print -conditional). Open: conj:quantum-lindblad-gap (the continuous
   Harrow construction, gap of 2Ω_{π⊗π̄} + ½B_W²), and an operator-level
   continuous Ihara–Bass (the tower as a Laplacian determinant). Opus REFUTE
   review: 13/13 VALID (`notes/reviews/selberg-2026-09-12.md`). Two action
   items from the review: (a) H-SZ (Selberg zeta entire with full divisor)
   and H-LAP have no byte-cited quote; fetch a source and convert the
   `assumed` rows to `cited`, which lifts the -conditional suffix; (b) the
   reviewer confirms that `notes/riemann-channel-note.md` §5's prime weight
   +Λ(n)n^{-1/2} is off by a factor −2 against the note's own explicit
   formula and double-counts the e^{-t/4} damping: correct §5 of that note
   (shard 04 already carries the corrected statement via prop:damping-identity).

10. **Weil positivity for an arbitrary transfer operator** (2026-09-12
   afternoon, lab-book shards 08b/08c, `notes/weil-positivity.md`,
   `notes/weil-positivity/astra-proofs.md`, `scripts/weil_positivity.py`).
   TJO's question: what does "the reflection pairs the mode at ρ with the
   mode at 1−ρ̄, RH says every mode is its own partner" mean for an arbitrary
   Kraus family? Proved by the codex prover (gpt-6-astra), Opus refute
   review: (i) for any finite-dimensional X, trivial set and radius r,
   positive definiteness of the rescaled trace sequence
   r^{-l}(Tr X^l − trivial) is exactly the one-sided bound |μ| ≤ r
   (Poisson kernel + growth lemma), modes inside the disc pass; (ii) if the
   retained spectrum is invariant under J(μ) = r²/μ̄ the Weil form equals
   the mode-pairing form (the finite inflow identity) and positivity ⇔ every
   mode J-fixed ⇔ all on the circle; (iii) Kraus dichotomy: ANY Ad-family
   has nonnegative ring traces and conjugation-closed spectrum (the adjoint
   pairing was never needed for either; two drafted claims corrected by
   prover and numerics independently); inverse pairing B_ī = B_i^{-1} gives
   the functional equation μ ↦ (D−1)/μ, so its RH reads "every nontrivial
   eigenvalue of Σ is real with |α| ≤ 2√(D−1)"; adjoint pairing gives
   HS-self-adjointness of Σ, i.e. reality for free (the Hilbert–Pólya half);
   both iff unitary, where the criterion is Hastings' bound alone;
   (iv) Bochner version for Lindblad-type generators, Dyson-expansion ring
   norms with the free propagators between jumps; (v) a Hilbert–Pólya inner
   product exists iff semisimple on the circle; Weil positivity is blind to
   Jordan blocks. Prior art found: Huang 2019 (Ramanujan ⇔ h_k ≥ 0 termwise,
   the boundedness form), Suzuki 2022 (kernel form), Weil/Li (Connes–Consani,
   Lagarias). Not found: the arbitrary-operator statement, the separation
   of bound from duality, the Kraus dichotomy. SPT side quest recorded as a
   dead route (obs:spt-protection-is-sign-data); PSL(2,Z)-generator channels
   parked (expanders, not Ramanujan for p ≥ 11).

### Discussion 2026-09-12: circle flows

Direct sum over $p$ of rotations on circles of circumference $\log p$ has
trace $\sum_n \Lambda(n)\delta(s - \log n)$ (Poisson), dynamical zeta =
Euler product; it is side A. For finite sets of primes its spectrum is the
poles of the partial Euler product; zeros exist only in the infinite
product. Prime-by-prime ansätze (direct sums, commuting dilations) cannot
see zeros. See `docs/worklog/2026-09-12.md`.

## Steering 2026-09-11 (TJO)

TJO's deepest learning from the founding session: **RH is a Ramanujan
property**, and this gives cautious optimism because the quantum-expander
literature supplies a wealth of constructions to tinker with. Claude's
assessment, recorded for the next session:

- The equivalence chain is theorem-level at every link (Ihara/Sunada;
  quantum Ihara–Bass, to be written as a lemma; Faddeev–Pavlov for ζ).
- Ramanujan-ness has exactly three known sources: arithmetic (LPS via
  Deligne), probabilistic-asymptotic (Friedman, Hastings; "nearly", ε → 0),
  and interlacing families (Marcus–Spielman–Srivastava; real-rootedness of
  expected characteristic polynomials, no arithmetic). MSS is the one whose
  shape matches "the Hilbert–Pólya operator H is Hermitian"; Montgomery–
  Odlyzko is the hint that ξ could be an expected characteristic polynomial.
- Obstruction: the prime dilations commute, and abelian Cayley graphs are
  never expanders. LPS resolves the analogous problem: Hecke operators T_q
  also commute, and expansion comes from the arithmetic quotient. The joint
  spectrum of the commuting family is the content (Hecke eigenvalues there,
  zeros here).

**Proposed first tinkering object (Weil–LPS channels).** Harrow's
construction with G = SL₂(F_p), S = LPS generators for a prime q, π = the
Weil representation on ℓ²(F_p): Φ_q(ρ) = (1/|S|) Σ_{s∈S} π(s) ρ π(s)†.
Exactly Ramanujan (LPS + Deligne), commuting for different q, jointly
diagonal with spectrum given by Hecke eigenvalues of weight-2 forms of
level p (Eichler–Shimura). Its quantum Ihara zeta is an Artin–Ihara
L-function twisted by Ad(Weil) and satisfies RH. Compute for p = 5, 7, 11,
13 and q = 2, 5; verify the Hastings bound numerically; compare the joint
spectrum with LMFDB Hecke eigenvalues. This lands on the parent campaign's
SP-WEYL Hilbert space and is the concrete link between the two repos.

## Next useful steps, in order

0. **The Bost–Connes reframe, items 0a–0f above. Central priority.**

1. **Weil–LPS channels, part 2.** Built and verified (item 5 above). Remaining:
   identify the joint spectra (13;17,29), (19;5,17), (29;5,13) with Hecke
   eigenvalues of weight-2 forms for the quaternion algebra ramified at {2,∞}
   via LMFDB; decide what "assemble over p" should mean (the DG-GLOBAL
   question in this guise). The Ihara–Bass lemma is done (item 8), in the
   general Kraus form; cite Matsuura–Ohta for the unitary case.
1b. **Continuous Harrow channel (was conj:quantum-lindblad-gap).** Assessment
   2026-09-12 night: not hard, theorem-shaped. On each constituent σ of π⊗π̄
   and diagonal K-type m, −𝓛 = 2λ_σ + m²/2 with λ_σ = s_σ(1−s_σ), so
   gap = min(½, 2·s(1−s) over complementary-series constituents); for
   tempered π the spherical part of π⊗π̄ is tempered (Cowling–Haagerup–Howe:
   L^{2+ε} coefficients) and the gap is exactly ½ = 2·¼, the continuous
   Ramanujan value; e^{t𝓛} is a mixed-unitary channel averaged over the
   hypoelliptic heat kernel of ½(H²+E²) (Nelson, Hörmander). Complementary
   π_s: Repka 1978 decides when π_s⊗π_s contains π_{2s−1} (threshold s>¾ from
   memory, must be byte-checked). The SL(2,F_p) half of the conjecture is
   void (no vector fields; that case is Harrow + LPS, item 5). To do: fetch
   Nelson/CHH/Repka TeX, restate as a theorem with the gap formula, run the
   codex prover, Opus refute. The real difficulty is the lattice version
   (gap of −2Δ on Γ\H = 2λ₁, Ramanujan ⇔ Selberg ¼), already the first-band
   criterion of shard 09c; a quantum (operator-level) lattice version is not
   yet formulated.
1a. **General Kraus zeta, part 2 (sharpened 2026-09-12 by item 10).** For
   adjoint-paired non-unitary families "Ramanujan" can only be the one-sided
   bound |μ| ≤ r (Weil positivity), there being no duality
   (prop:kraus-no-duality-example). The new class to study is the
   INVERSE-paired non-unitary families B_ī = B_i^{-1}: positive rings,
   functional equation, RH ⇔ Σ has real spectrum in [−2√(D−1), 2√(D−1)],
   a PT-symmetric-type reality statement. Cheap experiments: B_i = G U_i G^{-1}
   (Σ similar to Hermitian, reality free); random invertible B_i (does
   reality fail generically? does the bound?); whether canonical form or the
   Bartholdi deformation (Matsuura–Ohta arXiv:2208.14032) singles out a
   duality for adjoint-paired families.
1c. **Restate prop:ringnorm-trace.** DONE 2026-09-12 night in shard 04
   (Tr_dist Z(t) = 1 − 2P_+ − e^{−t/2}/(e^t − 1), proved-conditional). §5 of
   notes/riemann-channel-note.md still carries the old weight; notes are
   free-form and the shard is authoritative.
2. **The Stinespring question.** Write the compressed semigroup Z(t) on K_S
   explicitly (functional model, Cauchy kernels) and test whether a generator
   of Holevo jump form with jumps at k log p reproduces it on K_S. A negative
   answer with a reason is a result. Suggested: codex lane, gpt-5.6-sol xhigh,
   blind, with the note as the only input.
3. **Tighten §4 of the note.** The "bridge" statement (LP = BC at β=1 +
   Sz.-Nagy–Foias) is stated at the level of the boundary phase. Write the
   innerness argument in full (Phragmén–Lindelöf in Im τ < 0) rather than
   citing Lax–Phillips.
4. **Repo rules: decided 2026-09-12 evening.** The lab book `report.tex`
   with shards under `report/sections/`, the four databases under `db/`
   (notation, definitions, claims, provenance), the gate
   `scripts/labbook_check.py` and the local CI `scripts/ci_local.sh`
   (pre-commit via `make hooks`) are the discipline from now on. A statement
   is a claim only when it has a row in `db/claims.tsv`; `proved` needs a
   reviewer file; every quote needs a provenance row. Notes under `notes/`
   stay free-form but every note must be distilled by a shard (the gate
   checks both directions).
5. **Remote.** Public at github.com/tobiasosborne/riemann-channel (AGPL-3.0), created 2026-09-12.

## Environment

python3 with numpy, mpmath, sympy. `fmd-report` renders `notes/*.md` to HTML
with MathML verification. Zeros: `mpmath.zetazero(n)`, ~0.5 s each near
n = 3000; `data/zeros3000.npy` caches the first 3000.
