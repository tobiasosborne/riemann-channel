# Brief for the prover: a graded quantum channel for the LPS square complex. Realise the signed non-backtracking transport of the (13, 17; 5) worked example as a graded transfer channel with a C^{1|1} letter register (the sign as the parity), compute its sector restrictions and graded divisor, and determine exactly how the net divisor [1] + [17] - spec F_1 is or is not reproduced

You are the prover in a mathematical research notebook (git repo, current directory). Author line for
everything you write: `codex:gpt-6-astra`. Write ONLY the file `notes/lps-graded-cp/astra-proofs.md` (create it;
overwrite if present) and, if you want scratch computations, python files under `notes/lps-graded-cp/checks/`.
Do not edit anything else. Do not run git. python3 with numpy, scipy, sympy is installed; the complex can be
rebuilt from `scripts/lps_square_complex.py` (read it; you may import or copy its construction into your checks).
Read first:

1. `notes/deninger-lps/astra-proofs.md` B6 (binding): for a graded transfer channel `Str E^n = sum_w |Tr(P A_w)|^2 >= 0`,
   `Tr E^n = sum_w |Tr A_w|^2 >= 0`, `dim End(V)_even - dim End(V)_odd = (dim V_+ - dim V_-)^2 >= 0`; the direct sector
   prescription `E_even = 1 (+) 17`, `E_odd = F_1` is impossible (`Tr E^2 = -10940`); equality of supertraces fixes only the
   net divisor `[1] + [17] - sum_{lambda in spec F_1} [lambda]` with `nu(0) = (dim V_+ - dim V_-)^2 + 1440`; `N_n >= 0` for all
   `n`; **"scalar orientation signs cancel under Ad (Ad(-U) = Ad(U)); one can put a sign into relative phases between
   auxiliary bond components, but then coherences and population spectra must also be computed"**; the letter-register
   CP transfer `A_(j,i) = U_i (x) |j><i|`, `j != rev(i)`, realising a unitary Hashimoto block map with zero register
   coherences; "OPEN: no homogeneous Kraus family realising this exact net divisor, and no obstruction excluding all such
   families with cancelling modes, is established". Also `notes/reviews/deninger-lps-2026-09-22.md` B6.
2. `notes/deninger-lps/src/lps-deninger-worked-example.md` Sections 7–8: `F_1 = [[T, -17],[1, 0]]` on `K (+) K`; the signed
   graph `G_e` (vertices = the 840 unoriented horizontal edges, edges = the 7560 squares joining opposite horizontal
   edges, sign +1/-1 by orientation transport), its signed adjacency `T_1`, the signed non-backtracking operator `B_e`
   (with `epsilon(c)` the product of edge signs along a walk), the vertical graph `G_v` (18-regular on 120 vertices) with
   `B_v`; `Z_v^{-1} = (1-u^2)^{960} det Q_u(T_0)`, `Z_e^{-1} = (1-u^2)^{6720} det Q_u(T_1)`, `Z(u) = (1-u^2)^{-5760} Z_v/Z_e`,
   `N_n = 1 + 17^n - Tr F_1^n = Tr B_v^n - Tr B_e^n + 5760(1 + (-1)^n)`, the table `N_1..N_6 = 0, 11520, 10080, 126720,
   1209600, 23886720`.
3. The notebook's graded machinery: `report/sections/02h_definitions_graded_ramanujan.tex` (`def:graded-transfer-channel`,
   `def:parity-twisted-tp`, `def:graded-rh-fe-ramanujan`, `def:graded-quantum-expander`, `def:graded-hashimoto`,
   `def:index-two-grading`), `report/sections/03c_graded_ramanujan.tex` (`thm:graded-harrow`, `thm:graded-qihara-bass`,
   `cor:graded-band-circle`, the graded Ihara--Bass with `(1-u^2)^{n_k(D-2)/2}` cancelling for balanced gradings),
   `report/sections/03b_graded_permutation.tex` (the graded permutation: how a sign becomes a parity),
   `report/sections/04n_graded_toys_network.tex` (`thm:diagram-linearisation`, `thm:scattering-superdeterminant`,
   `def:graded-renewal-network`, `thm:renewal-graded-mps`: a companion matrix `[[T_X, -(I-C)],[I, 0]]` realised as a
   graded network), `report/sections/08_quantum_ihara_general.tex` (Ihara--Bass for an arbitrary Kraus family),
   `notes/ramanujan-graded/astra-proofs.md` (ledger L28, L31, L36, L41 conventions), `scripts/graded_ramanujan.py`,
   `scripts/graded_toys.py`.

Be explicit and finite: every operator below is a finite matrix that the numerics lane will build. Label PROVED,
REFUTED, SHARPENED or OPEN. Keep a correction ledger. Do not pad.

## 0. Why this round

The worked example's positivity package is a *spectral* graded transfer (a signed linear operator whose determinant
is the numerator), and B6 showed that the naive quantum reading fails because scalar signs are invisible to `Ad`.
The notebook's own device for exactly this situation is the graded permutation of shard 03b: a sign becomes a
parity when the bond is `C^{1|1}` and the negative letters act by the odd/even structure. The author of this brief
(`claude:fable-5.1`) proposes the following construction and asks you to compute it exactly and settle what it
realises.

**Construction (to be made precise).** Bond `V = C^{1|1} = C_+ (+) C_-` with parity `P = diag(1, -1)`. Letter register
`C^{E}` indexed by the directed squares-as-edges of `G_e` (or the directed edges of the relevant non-backtracking
graph; choose the smallest register that works and say why). Kraus operators `A_{(j,i)} = U_i (x) |j><i|` for
`j != rev(i)`, with `U_i = 1` for positive edges and `U_i = P` (= sigma_z, which is EVEN: Ad(P) is the grading itself) or
`U_i = X` (= sigma_x, ODD: an odd letter) for negative edges: decide which choice makes the sector restrictions
`E_0 = E|_even`, `E_1 = E|_odd` of the doubled transfer reproduce `Tr B_e^n` with the signs, i.e. such that the
supertrace `Str E^n = Tr E_0^n - Tr E_1^n` (or the parity-twisted trace of `def:parity-twisted-tp`) equals
`sum_{closed walks} epsilon(c)`-type sums. The hoped-for statement: on the invariant diagonal-register algebra the
channel acts as `(E X)_j = sum_{i != rev j} U_i X_i U_i^*`, and on `End(C^{1|1}) = M_2` the even part `{1, P}` and the odd
part `{X, Y}` are each two-dimensional; with `U_i in {1, P}` the map on the odd sector picks up the sign `epsilon_i`
from `P X P = -X`, so `E_1` restricted to the register-diagonal odd sector is exactly `B_e` (signed) tensored with a
two-dimensional multiplicity, while `E_0` is the unsigned `|B_e|` tensored with two: then
`Str E^n|_{diag} = 2 Tr|B_e|^n - 2 Tr B_e^n`, which is NOT `Tr B_v^n - Tr B_e^n` — so the vertical walk `B_v` must be
supplied by a second register or by the even sector of a different letter set. Work this out: what is the smallest
graded Kraus family (letters, bond, register) whose graded divisor (`def:graded-transfer-channel`: `nu = m_0 - m_1`)
has retained part exactly `-sum_{lambda in spec F_1}[lambda]` plus poles `[1] + [17]` (with `[1]` the designated `H^0`
partner), possibly up to a designated trivial divisor of the `(1-u^2)`-type that the notebook's graded Ihara--Bass
already handles (`thm:graded-qihara-bass`'s `(1-u^2)^{n_k(D-2)/2}` factor), and up to cancelling modes appearing in
both sectors with equal multiplicity (invisible to the supertrace). Determine:

**G1.** The exact sector restrictions of the letter-register channel with `U_i in {1, P}` on the negative edges of
`G_e`: prove `E_1|_{diag} = B_e (x) 1_2`-type and `E_0|_{diag} = |B_e| (x) 1_2`-type (or whatever is true), including the
off-diagonal register coherences (which the predecessor said are annihilated: prove or refute for this letter set,
noting `P` is not a generic unitary), and compute `Tr E^n`, `Str E^n` for `n = 1..6` exactly (the numerics lane will do
it numerically; you give the formula and the values for `n <= 3` at least).

**G2.** The correct graded family. Either (a) exhibit a homogeneous Kraus family on a graded bond and register whose
sector traces satisfy `Tr E_0^n - Tr E_1^n = N_n + (trivial/cancelling terms you name exactly)` for all `n`, with the
retained graded divisor equal to `[1] + [17] - spec F_1` (i.e. the completed `Z(u)` is the ring zeta `1/sdet(1 - u E)` up
to the named trivial factor), and prove it; or (b) prove an obstruction that no such family exists with the
constraint that letters are homogeneous and the bond parity is `C^{a|b}` for some `a, b` (use the necessary conditions
of B6: `Str E^n = sum_w |Tr(P A_w)|^2`, the `n = 2` trace, the even-minus-odd dimension count), quantifying which
cancelling modes would be needed. The author's guess for (a): two registers (the 17-direction for `B_v` and the
squares for `B_e`) on a bond `C^{1|1} (x) C^{1|1}`-type, with the vertical walk contributing to the EVEN sector (poles
`1, 17` and the `(1-u^2)^{960}` trivial factor) and the signed square walk to the ODD sector (zeros, and the
`(1-u^2)^{6720}` factor), so that the graded Ihara--Bass of `thm:graded-qihara-bass` gives
`sdet(1 - uE) = (1-u^2)^{6720 - 960} det Q_u(T_1)/det Q_u(T_0) = (1-u^2)^{5760}/Z(u)`-type: exactly the worked example's
correction `(1-u^2)^{5760}` as the graded trivial divisor. Prove or refute this identification, with the exact
exponents and the exact designated trivial set `S_triv` in the sense of `def:graded-transfer-channel`.

**G3.** If (a): is the resulting channel parity-twisted unital (`def:parity-twisted-tp`), what is its `P`-mode, is it a
graded quantum expander in the sense of `def:graded-quantum-expander` (the retained modes on the circle
`|u| = 17^{-1/2}` is the worked example's certified `||T|| < 2 sqrt 17`), and how does this relate to the notebook's
graded Weil--LPS Hashimoto (`thm:graded-qihara-bass`) whose odd Weil constituent is NOT Steinberg (B5)? If (b): what is
the minimal obstruction and does it survive allowing non-homogeneous but parity-covariant letters?

**G4.** The positive certificate as a channel statement: the worked example's `G = [[I, -T/2],[-T/2, 17 I]]` is a metric
on the doubled space; in the channel picture the natural positive object is the Hilbert--Schmidt metric on
`End(V (x) register)`. Prove or refute: the channel of (a) is Hilbert--Schmidt self-adjoint (inverse-paired letters,
`obs:kraus-dichotomy`), so its odd-sector operator is diagonalisable with real spectrum, and the Bass/companion
structure (the pairs `alpha, 17/alpha`) arises from the non-backtracking structure exactly as in the graded Ihara--Bass;
then "positivity = strict Ramanujan" (Proposition 9.3 of the finite note) is the statement that the odd non-backtracking
spectrum lies on the circle, which is `cor:graded-band-circle`'s band-iff-circle. Say exactly how the finite note's
positivity certificate and the notebook's graded band-circle theorem are the same or different statements.

**G5.** What this changes (one page): B6 closed or not; the worked example as a graded quantum channel or as a
spectral transfer only; the dictionary between the finite Deninger package and `def:graded-rh-fe-ramanujan`.

## Output format

`notes/lps-graded-cp/astra-proofs.md`: ledger (G1–G5, verdicts); full proofs with hierarchical steps; repo sources by
file and line; a section "Numerical checks for the blind lane" (explicit: the Kraus family as matrices to build, the
register size, `Tr E^n` and `Str E^n` for `n = 1..6`, the sector dimensions, the graded divisor's retained part
against `spec F_1` with multiplicities, the trivial exponents); a section "Corrections to the brief"; and a closing
"What this changes in the notebook" with statuses and one-sentence statements.

## Durability (the network is unreliable today; this is mandatory)

Write your output file **incrementally**: create `astra-proofs.md` with the ledger table (all verdicts `PENDING`)
before you start, and after finishing each claim rewrite the file with that claim's section and its updated ledger
row. If you are resumed after an interruption, read your own `astra-proofs.md` first, keep everything already
written, and continue from the first `PENDING` row. Keep a one-line `notes/lps-graded-cp/progress.txt` with the
claim you are working on.
