# Blind numerics lane: the LPS square complex (13, 17; level 5)

Author: `claude:fable-5.1` (blind numerics fork, 2026-09-22). Protocol: blind to `astra-proofs.md`; inputs were
`astra-brief.md` and `src/lps-deninger-worked-example.md` only. Script `scripts/lps_square_complex.py`
(459 lines, numpy/scipy only, deterministic, no randomness), output `outputs/lps_square_complex.txt`.
Runtime 58 s (the modular rank of the 1920 x 1920 face Gram matrix and the 1680 x 1680 directed-edge
spectra dominate). 50 checks, 48 pass, 2 fail; both failures are claims of the brief, not of the worked
example, and are explained in the findings.

The complex is rebuilt from the quaternion sets: `S_13` (14), `S_17` (18), `PGL_2(F_5)` normalised row-major,
`phi(a) = [[a0+2a1, a2+2a3],[-a2+2a3, a0-2a1]] mod 5`, directed edges `(g, a): g -> g phi(a)`, the 252 rules
`ab = +-b'a'` found by exhaustive matching of normalised products, squares from the four-edge boundary of the
worked example, `D`, `K = ker D^t`, `T_1` by the opposite-edge transport with signs. The characteristic
polynomial of `T` on `K` was NOT computed exactly (721 x 721 sympy charpoly is too slow); eigenvalues are
`numpy.eigvalsh` in an orthonormal basis of `K` (clustered at `1e-6`), and the comparison with the worked
example's factor table is by multisets of roots (max deviation `5e-14`). The rank of `B_2` is certified
exactly: `rank_101(B_2 B_2^t) = 1801 <= rank_101(B_2) <= rank_Q(B_2) <= 1920 - 119` with `B_1 B_2 = 0`.

## Ledger

| id | verdict | check |
|---|---|---|
| D01 | PASS | |S_13| = 14, |S_17| = 18 (got 14, 18) |
| D02 | PASS | |PGL_2(F_5)| = 120 (got 120) |
| D03 | PASS | phi is a projective homomorphism on the generators, images invertible |
| D04 | PASS | 840 horizontal, 1080 vertical undirected edges (got 840, 1080) |
| D05 | PASS | no loops, no repeated edges within a colour, regular of degree 14 / 18, symmetric |
| D06 | PASS | both colour graphs connected and bipartite with the same bipartition |
| D07 | PASS | spec A_13 = +-14 (1), +-4 (34), +-2 (25): [(-14, 1), (-4, 34), (-2, 25), (2, 25), (4, 34), (14, 1)] |
| D08 | PASS | spec A_17 = +-18 (1), +-6 (10), +-5 (12), +-3 (4), +-2 (15), 0 (36): [(-18, 1), (-6, 10), (-5, 12), (-3, 4), (-2, 15), (0, 36), (2, 15), (3, 4), (5, 12), (6, 10), (18, 1)] |
| D09 | PASS | 252 reordering rules a b = +- b' a' exist and are unique; 252 distinct normalised products |
| D10 | PASS | for fixed a, b -> b' is a bijection of S_17 |
| D11 | PASS | 7560 squares, each with exactly 4 corner representatives agreeing up to sign (got 7560) |
| D12 | PASS | B_1 B_2 = 0 exactly |
| D13 | PASS | every face column has exactly four nonzero entries +-1 |
| D14 | PASS | rank B_1 = 119 (mod 101, = rank over Q since rows sum to zero): 119 |
| D15 | PASS | rank B_2 = 1801: rank_101(B_2 B_2^t) = 1801 <= rank_101(B_2) <= rank_Q(B_2) <= 1920 - 119 |
| D16 | PASS | Betti numbers (1, 0, 5759): (1, 0, 5759) |
| D17 | PASS | dim K = dim ker D^t = 721 (got 721) |
| D18 | PASS | T_1 is symmetric |
| D19 | PASS | T_1 D = D T_0 with T_0 = A_17, exactly |
| D20 | PASS | K = ker D^t is T_1-invariant (|D^t T_1 V| < 1e-9) |
| D21 | PASS | all eigenvalues of T lie in (-8, 8): max |lambda| = 7.464102 < 8 < 2 sqrt17 = 8.246211 |
| D22 | PASS | directed T_1 symmetric; reversal is an involution |
| D23 | PASS | directed T_1 commutes with the edge reversal |
| D24 | PASS | old space (tail and head pull-backs of vertex functions) has dimension 238 (got 238); new = 1442 |
| D25 | PASS | new space is 1442-dimensional and T_1-invariant |
| D26 | PASS | reversal splits new = 721 (+1) + 721 (-1) (got 721, 721) |
| D27 | FAIL | T_1 has the same spectrum on the two reversal sectors of new (max dev 1.17e+00) |
| D28 | PASS | the (-1) reversal sector of new has spectrum spec(T on K): dev 3.55e-14 (dev of the (+1) sector 1.17e+00) |
| D29 | PASS | the (+1) sector has the NEGATED spectrum -spec(T on K) (bipartite twist: the transport crosses one 17-edge): dev 2.93e-14 |
| D30 | PASS | 307 = 17^2 + 17 + 1 normalised quaternions of norm 289 (a0 > 0 odd, others even), including 17*1: got 307 |
| D31 | PASS | 17*1 is among them and phi(17) = identity projectively |
| D32 | PASS | Hecke relation T_17^2 - 17 I = T_289 on vertex functions (all 307 elements) |
| D33 | PASS | the 306 reduced words b1 b2 are exactly the primitive norm-289 elements, each once |
| D34 | PASS | edge version: T_1^2 - 17 I = (double transport over reduced words) + I, exactly, on all antisymmetric fields (hence on K) |
| D35 | PASS | Section 13 table: sum of m deg f = 721 (got 721) |
| D36 | PASS | spec(T on K) equals the roots of the Section 13 factor table with multiplicities (max dev 5.06e-14) |
| D37 | PASS | integer eigenvalue multiplicities of T: [(-7, 4), (-6, 17), (-5, 12), (-3, 6), (-2, 77), (-1, 8), (2, 20), (3, 44), (4, 18), (6, 15), (7, 4)] |
| D38 | PASS | chi_T = chi_{T_1} (x - 18) / chi_{A_17} as multisets of eigenvalues (max dev 4.26e-14) |
| D39 | PASS | Tr T = 18, Tr T_1 = 0 |
| D40 | PASS | F_1^t Omega F_1 = 17 Omega |
| D41 | PASS | F_1^t G F_1 = 17 G |
| D42 | PASS | G > 0: smallest eigenvalue 0.172305 (Schur complement 17 - lambda^2/4 >= 3.071797) |
| D43 | PASS | all eigenvalues of F_1 have modulus sqrt(17): max deviation 1.25e-13 |
| D44 | PASS | N_n = 1 + 17^n - Tr F_1^n, n = 1..6: [0, 11520, 10080, 126720, 1209600, 23886720] |
| D45 | PASS | PGL_2(F_5) has 7 conjugacy classes (got 7): sizes [15, 24, 20, 10, 30, 20, 1] |
| D46 | PASS | irreducible dimensions of PGL_2(F_5) = [1, 1, 4, 4, 5, 5, 6] (sum of squares 120): [1, 1, 4, 4, 5, 5, 6] |
| D47 | PASS | computed irreducible characters are orthonormal |
| D48 | PASS | all multiplicities in the decompositions are integers |
| D49 | FAIL | every irreducible appears in every Hecke eigenspace with multiplicity a multiple of its dimension (isotypic blocks) |
| D50 | PASS | K-eigenspace dimensions equal sum of (dim x multiplicity) |

## Findings

**F1 (brief B3, refuted as stated; D27, D28, D29).** The edge-reversal involution commutes with the
directed-edge transport `T_1` (D23) and splits the 1442-dimensional new space into two 721-dimensional
sectors (D26), but `T_1` does NOT have the same spectrum on the two sectors. The `(-1)` sector (antisymmetric
fields) is `K` and carries `spec(T)` (D28, deviation `4e-14`); the `(+1)` sector (symmetric new fields) carries
exactly `-spec(T)` (D29, deviation `3e-14`; traces `+18` and `-18`). Reason: both colour graphs share one
bipartition (D06), the transport of a horizontal edge crosses one 17-edge, so multiplication by the bipartite
sign `eps(tail)` intertwines the symmetric and antisymmetric sectors and conjugates `T_1` to `-T_1`. In
automorphic terms the second copy is the first twisted by the sign character (`sgn o det`), not an identical
copy. The brief's sentence "`T_17` acting the same way on both" must be corrected to "`T_17` on the second copy
is the sign twist, `a_17 -> -a_17`"; the worked example's `K (+) K` Bass doubling is unaffected (it doubles `K`
with itself, not with the symmetric sector).

**F2 (brief B3, the multiplicity prediction, sharpened; D47--D50).** The eigenspaces of `A_17` on vertex
functions and of `T` on `K` were decomposed under the left action of `PGL_2(F_5)` (7 classes of sizes
`15, 24, 20, 10, 30, 20, 1`; irreducible dimensions `1, 1, 4, 4, 5, 5, 6`, sum of squares 120, obtained by
Burnside's class-sum algorithm and checked orthonormal). The brief's guess "dimensions `1,1,4,4,5,5,6,6`" is
wrong (there are seven irreducibles, one of dimension 6). Every multiplicity is an integer (D48) and the
dimensions add up (D50), but the irreducibles do NOT appear with multiplicity a multiple of their dimension
(D49): e.g. on vertex functions `lambda = -6` (mult 10) is `5 (x) 2`, `lambda = 0` (mult 36) is `6 (x) 6`,
`lambda = +-5` (mult 12) is `4 (x) 3`; on `K`, `lambda = -2` (mult 77) is `4 (x) 3 + 4' (x) 5 + 5 (x) 9`,
`lambda = 3` (mult 44) is `1 (x) 4 + 4 (x) 5 + 5 (x) 4`, `lambda = 2` (mult 20) is `5 (x) 4`, `lambda = -6`
(mult 17) is `1 (x) 2 + 5 (x) 1 + 5' (x) 2`. This is what the regular-representation structure predicts if the
Hecke operator acts nontrivially inside each isotypic block `pi (x) pi^*` (on the `pi^*` factor): the
multiplicity of `pi` in a Hecke eigenspace is the dimension of the `T`-eigenspace inside `pi^*`, between 1 and
`dim pi`, not a multiple of `dim pi`. The full per-eigenvalue tables are in the output file.

**F3 (worked example, all confirmed).** Sizes, spectra of `A_13` and `A_17` with multiplicities, 252 unique
rules, 7560 squares with four representatives each, `B_1 B_2 = 0`, ranks 119 and 1801, Betti numbers
`(1, 0, 5759)`, `dim K = 721`, `T_1` symmetric, `T_1 D = D A_17`, `K` invariant, `||T|| = 7.4641 = 4 + 2 sqrt 3
< 8`, the full Section 13 factor table (`x + 5` has eigenvalue `-5`, multiplicity 12), `chi_T = chi_{T_1}(x)(x-18)/chi_{A_17}(x)`
as multisets, `F_1^t Omega F_1 = 17 Omega`, `F_1^t G F_1 = 17 G`, `G > 0` (least eigenvalue `0.1723`), all
eigenvalues of `F_1` of modulus `sqrt 17` (deviation `1e-13`), and `N_1..N_6 = 0, 11520, 10080, 126720, 1209600,
23886720`.

**F4 (brief item 4, Hecke relations; D30--D34).** There are 307 normalised quaternions of norm 289 (`a0 > 0`
odd, others even), including `17 * 1` (which acts as the identity); `T_17^2 - 17 I = T_289` on vertex
functions with all 307 elements. The 306 reduced words `b_1 b_2` (`b_2 != conj b_1`) are exactly the primitive
norm-289 elements, each once. On edges, the double transport over reduced words plus the identity equals
`T_1^2 - 17 I` exactly (on all antisymmetric fields, hence on `K`); a pair `(b, conj b)` transports an edge back
to itself, which is the algebra behind it.

**F5 (small).** `Tr T = 18`, `Tr T_1 = 0` (no square returns a horizontal edge to itself).
