# Brief for the prover: the horizontal cohomology of the LPS square complex is the character group of the toric reduction of a Shimura curve (Cerednik–Drinfeld), the transverse transport is Hecke, and the geometric pairing the square complex could not supply is Grothendieck's monodromy pairing

You are the prover in a mathematical research notebook (git repo, current directory). Author line for
everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/cerednik-drinfeld/astra-proofs.md`
(create it; overwrite if present) and, if you want scratch computations, python files under
`notes/cerednik-drinfeld/checks/`. Do not edit anything else. Do not run git. python3 with numpy, mpmath,
sympy, scipy is installed. Read first:

1. `notes/deninger-lps/astra-proofs.md` (your predecessor's audit of the (13, 17; 5) LPS square complex, this
   morning: B1 the complex is the level-5 congruence cover of the primary quaternion product lattice, total
   Betti `(1, 0, 5759)`; B2 `K = H^1` of the 13-graph `X^{13,5}` (721-dimensional), the transverse transport is
   the degree-18 `T_17` correspondence; B3 the spectrum is a weight-two Hecke spectrum with an explicit level
   at 2 (`U_2 = image(1 + 2 O_2)`) and the Steinberg reversal sign, the other directed new half carrying the
   negative spectrum; **B4 OPEN: "canonical cup/Petersson identification is unsupported; the real cone of
   `F_1`-invariant positive metrics has dimension 16539"**; B5–B7), its correction ledger, and
   `notes/deninger-lps/numerics.md` (blind numerics, 50 checks) and `scripts/lps_square_complex.py`.
2. `notes/deninger-lps/src/lps-deninger-worked-example.md` (the finite model: `T`, `K (+) K`, `F_1 = [[T, -17],[1, 0]]`,
   `Omega_B`, `G = [[I, -T/2],[-T/2, 17 I]]`, the cycle basis `Z` and `M = Z^t Z`, `L`) and
   `notes/deninger-lps/src/manuscript.txt` (Theorem 5.2, Definition 6.1, Theorem 6.2, Proposition 9.3: "`Omega_B`
   is the canonical pairing of a doubled space; it is not, without an additional construction, the cup pairing
   of the original faces"; Section 10: "the specific LPS face-to-pairing construction remains open").
3. The notebook: `report/sections/04l_elliptic_cavity_channel.tex` (`thm:arithmetic-metric`),
   `report/sections/04p_gl1_bond.tex`, `report/sections/07_deligne_via_graphs.tex`, `notes/deligne-via-graphs.md`.
   Sources in `refs/src` are arXiv TeX; search for `drinfeld`, `cerednik`, `shimura curve`, `monodromy pairing`,
   `ribet` and quote by file and line what you find; Cerednik (1976), Drinfeld (1976), Boutot–Carayol (1991),
   Grothendieck SGA 7 IX (monodromy pairing), Ribet (1990, "On modular representations of Gal(Qbar/Q) arising from
   modular forms", the character-group/monodromy-pairing formalism and the Ihara-lemma level-raising exact
   sequence), Jordan–Livné, Kurihara (1979, the dual graph of the Shimura curve's special fibre), and Bertolini–
   Darmon are NOT in the repo: state what you use precisely, marked "not byte-cited".

Be explicit. Standard theory (Cerednik–Drinfeld uniformization, semistable reduction and the character group
of the toric part, Grothendieck's monodromy pairing, Jacquet–Langlands, Ribet's exact sequences) may be used
as cited theorems with precise statements. A numerics lane can rebuild the finite complex and test every
finite statement; a hostile reviewer will try to refute every claim. Label PROVED, REFUTED, SHARPENED or
OPEN. Keep a correction ledger for this brief. Do not pad.

## 0. Why this round

This morning's audit identified the 721-dimensional horizontal cohomology `K` of the (13, 17; 5) square
complex as `H^1` of the LPS graph `X^{13,5}` with `T_17` acting, and identified its Frobenius polynomials with
weight-two Hecke data, but left the *geometric* origin of the pairing `Omega_B` and the metric `G` open,
concluding "one obtains a selected modular-Jacobian/Galois summand, not an identified entire curve". The
author of this brief (`claude:fable-5.1`) believes the identification is classical and exact:

**Cerednik–Drinfeld.** Let `B'` be the indefinite quaternion algebra over `Q` ramified at `{2, 13}` and `X = X_{B'}(5)`
the Shimura curve of level 5 (principal congruence at 5, or `Gamma(5)`-type level structure; fix it to match
`K(5)` in the definite algebra). Then `X` has a 13-adic uniformization by the Drinfeld upper half plane
`Omega_13` modulo the unit group (norm a power of 13, level 5) of the *definite* quaternion algebra `B`
ramified at `{2, infinity}` with 13 inverted; the special fibre of `X` at 13 is a Mumford curve (totally
degenerate semistable reduction), and **its dual graph is the LPS graph `X^{13,5} = Gamma(5) \ T_14`**
(Kurihara; Jordan–Livné). Consequently:

- `K = H_1(X^{13,5}; Z) (x) R` is the **character group** `X_13 = Hom(torus of the Néron model of Jac(X) at 13, G_m)`
  (up to the usual identification of the graph's `H_1` with the character group of the toric special fibre);
- the transverse transport `T = T_17` is the Hecke operator `T_17` acting on the character group, compatibly
  with its action on `Jac(X)` and on `H^1_et(X)`;
- **Grothendieck's monodromy pairing** on the character group is the pairing on `H_1` of the dual graph given by
  the edge lengths, all equal to one for the LPS graph (no extra automorphisms at level 5, i.e. the lengths
  `e_i` of Ribet's formalism are all 1: check), hence it IS the worked example's integral cycle Gram `M = Z^t Z`
  (the standard inner product on cycle space restricted to `H_1`); it is positive definite, Hecke-equivariant,
  and `T_17`-symmetric: this is exactly the geometric pairing on `K` that the squares could not supply and that
  the finite note's Proposition 9.3 said requires "an additional construction";
- the Bass doubling `K (+) K` with `F_1 = [[T, -17 I],[I, 0]]` is the 17-Frobenius on the 13-adic (or `l`-adic) Tate
  module of the torus part, i.e. on `H^1_et(X) = ` the 13-new part (the toric part of `Jac(X)` at 13 is
  `Jac(X)` itself for a Mumford curve: totally degenerate), and `Omega_B` and `G` are respectively the Weil
  pairing on `T_l Jac(X)` composed with the monodromy pairing and the monodromy-pairing metric, up to the
  normalisation of the companion basis; the Petersson metric of the JL correspondents differs from the
  monodromy metric by the per-eigenform ratios `<f, f>_Pet / (monodromy norm of the corresponding
  character-group vector)`, which are the **Ribet–Takahashi / "degree of the modular parametrisation"**
  invariants (Ribet–Takahashi 1997, "Parametrizations of elliptic curves by Shimura curves and by classical
  modular curves"; Bertolini–Darmon; the ratio is an arithmetic invariant, not a constant), so the two natural
  points of the metric cone are *different* and their ratio is arithmetic content, not a normalisation.

Prove, refute or sharpen every one of these.

## 1. Claims

**CD1 (the uniformization and the dual graph).** State the Cerednik–Drinfeld theorem precisely for this case
(which Shimura curve; which level structure at 5 and at 2 matches the audit's `U_2 = image(1 + 2 O_2)` and
`K(5)`; which arithmetic group `Gamma^{13}` of `B^x(Q)` acts on `Omega_13`; the role of the two components /
the bipartite structure of `X^{13,5}` — the special fibre of a Mumford curve uniformised by a group with an
index-two subgroup preserving the bipartition has two "sides"; say whether `X` over `Q_13` or over its
unramified quadratic extension is the right object, since 13 is a nonsquare mod 5 and the graph is bipartite)
and prove: the dual graph of the special fibre is `X^{13,5}` (120 vertices = components, 840 edges = ordinary
double points), and `H_1` of it is `K`. If the correct dual graph is a quotient or a double cover of `X^{13,5}`
(e.g. by the bipartition or by extra automorphisms), say exactly which and correct the identification of `K`.

**CD2 (the character group, Hecke, and the monodromy pairing).** Prove: (a) the character group `X_13` of the
toric part of the Néron model of `J = Jac(X)` at 13 is `H_1(dual graph, Z)`, with `T_17` acting as the graph
correspondence `T` of the audit (so `chi_T` is the characteristic polynomial of `T_17` on `X_13 (x) Q`);
(b) Grothendieck's monodromy pairing `X_13 x X_13 -> Z` is the cycle pairing with edge lengths (the lengths are
the thicknesses of the double points; compute them for this level: with level `K(5)` and the primary lattice,
are all stabilisers trivial, so all lengths are 1?), hence `M = Z^t Z` in the worked example's cycle basis;
(c) the monodromy pairing is positive definite and `T_17`-symmetric (`L^t M = M L` in the worked example) —
this is the geometric origin of the symmetry of `T_1` on `K`; (d) the component group of `J` at 13 is
`X_13^vee / X_13` (cokernel of the monodromy pairing) and its order is `det M`; compute `det M` if the numerics
lane's cycle basis is available in `scripts/lps_square_complex.py` (it may not be; if not, give the formula and
what to compute), and compare with the Eisenstein ideal / Ribet's description of the component group when
possible.

**CD3 (the Frobenius on the toric part is the Bass doubling).** Prove: for a totally degenerate `J` (Mumford
curve), `T_l J` sits in `0 -> X_13^vee (x) Z_l(1) -> T_l J -> X_13 (x) Z_l -> 0` (Raynaud / Grothendieck), and
the Frobenius at a prime `p != 13` of good reduction (here `p = 17`) acts on `T_l J` with characteristic
polynomial `prod_f (1 - a_17(f) u + 17 u^2)` over the eigenforms; the Hecke operator `T_17` on `X_13` is the
"trace of Frobenius" and the Bass companion `F_1 = [[T, -17],[1, 0]]` on `K (+) K` realises `Frob_17` on
`X_13 (x) Q_l (+) X_13^vee (x) Q_l(1)` up to the identification `X_13^vee = X_13` by the monodromy pairing.
Identify `Omega_B` with the Weil pairing on `T_l J` composed with the monodromy-pairing identification (state
exactly), and `G` with the monodromy metric doubled (the worked example's `G_M = [[M, -ML/2],[-ML/2, 17 M]]`).

**CD4 (monodromy versus Petersson: the ratio is arithmetic).** With the Jacquet–Langlands correspondence `f`
(weight-two newform on `Gamma_0(2 * 13 * 25)`-type level, discrete series at 2 and special at 13), the
`f`-isotypic line of `X_13 (x) R` carries two natural norms: the monodromy pairing and the Petersson norm of
`f` transported through the Eichler–Shimura / uniformization comparison. Prove or cite precisely (Ribet–
Takahashi 1997; Bertolini–Darmon 1998/2005; Takahashi 2001) that their ratio is the "degree of the
Shimura-curve parametrisation" invariant (for rational `f`: `deg(phi_X: X -> E)` versus `deg(phi: X_0(N) -> E)`,
with the Ribet–Takahashi formula relating them through the Tamagawa/component numbers at the ramified primes
and the level), and therefore: the audit's "metric cone" has (at least) two canonical points, monodromy and
Petersson, differing by arithmetic invariants per eigenform; the worked example's `G` is (up to the companion
normalisation) the monodromy point. If some part of this is only conjectural or only for rational `f`, say
so exactly.

**CD5 (what this changes).** One structured page: (a) the finite note's "face-to-pairing construction" is
supplied by the *arithmetic surface* `X` over `Z_13`, not by the squares: the squares (the 17-direction) are
the Hecke correspondence, the 13-direction (the graph) is the special fibre, and the pairing comes from the
degeneration (monodromy), i.e. Deninger's positivity here is Grothendieck's monodromy pairing positivity on a
totally degenerate Jacobian; (b) for the notebook's programme, the dictionary "horizontal cohomology =
character group of a toric reduction, transverse = Hecke at another prime, positivity = monodromy pairing,
Bass doubling = Frobenius on the Tate module" and what its analogue would have to be for the GL_1 bond of
04p/04q (the theta bond state's "reduction"; mark speculation); (c) which of the audit's OPEN items (B4b, B6)
this closes and which it does not.

## 2. Output format

`notes/cerednik-drinfeld/astra-proofs.md` with: a ledger table (CD1–CD5, verdicts); full proofs with
hierarchical steps where long; every external theorem stated precisely with author and year, marked "not
byte-cited"; a section "Numerical checks for the blind lane" (explicit finite statements: `L^t M = M L`;
positivity of `M`; `det M` and its prime factorisation if computable; the `T_17`-symmetry of the cycle Gram;
the identification of the audit's reversal sign with the two sides of the bipartite graph; the doubled `G_M`
against the worked example); a section "Corrections to the brief"; and a closing "What this changes in the
notebook" with, per claim, the status to register and the one-sentence statement.

## 3. Durability (the network is unreliable today; this is mandatory)

Write your output file **incrementally**: create `astra-proofs.md` with the ledger table (all verdicts
`PENDING`) before you start on the mathematics, and after finishing each claim rewrite the file with that
claim's section and its updated ledger row. Never hold finished work only in memory. If you are resumed after
an interruption (the prompt will say so), read your own `astra-proofs.md` first, keep everything already
written, and continue from the first `PENDING` row. Keep a one-line `notes/cerednik-drinfeld/progress.txt`
with the claim you are working on, updated whenever you move to the next claim.
