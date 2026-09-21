# Numerics ledger: square roots of Ihara--Bass (shard 08h)

Script `scripts/ihara_dirac.py`, output `outputs/ihara_dirac.txt`, 158 checks, all passing (137 in the version written before the proofs; 21 added after the prover's corrections: the T2 real-square and twist checks and, under `T3'`, the all-X cancellation, the band-edge Jordan block, the X,X,Y,Y zeta and single-layer polynomial, the second chiral involution for mixed parities and the continuum reflection about -c).
Author `claude:fable-5.1`, written from `astra-brief.md` before the prover's text was read; the
brief's statements were sanity-checked once on a scratch example before the brief was sent
(chirality anticommutation, the square-root formula, the Berezinian mismatch), so this lane is
self-blind rather than blind: the same author drafted the statements and the checks. No Opus
lane ran in this round (TJO's instruction, 2026-09-21).

| block | what is checked | examples |
|---|---|---|
| T1(a) | `det N(u)` against `det(1 - uH)`, against `det(1 + uJ) det(1 - uR(1+uJ)^{-1}S)` and against the shard-08 form `prod det(1 - u^2 E_ibar E_i) det(1 + D - A)` | random non-unitary Kraus (n = 2, m = 2), random unitary (n = 2, m = 3), classical bouquets D = 4, 6 |
| T1(b) | nonzero spectra of `XY` and `YX` coincide; `YX = u(H + J)(1 + uJ)^{-1}`; `str K^k = 0`, k = 1..5; `sdet(1 - K) = 1` | same four families |
| T1(c) | `Ber diag(1 + uJ, (1 - u^2)1_V) = (1 - u^2)^{N(D-2)/2}` and `cor:qihara-unitary` on the same letters | random unitary, N = 4, D = 6 |
| T1(d) | the two would-be Berezinians of the coupled pencil: one is `det(1 - uH)`, the other `det(1 + uJ)^2/det(1 - uH)`; they differ; bouquet D = 4 polynomials `(1-u)^2(1+u)(1-3u)` and `(1 - u^2)^2` at three points | all four families; bouquet |
| T2(a) | no self-reverse class among all primitive cyclically non-backtracking classes; reversal permutes the classes | D = 4 (length <= 7, 1218 classes), D = 6 (length <= 5) |
| T2(b) | `det(1 - u^l E_wbar) = conj det(1 - conj(u)^l E_w)` at complex u | non-unitary and unitary Kraus |
| T2(c) | `det(1 - uH) = |F(u)|^2` at `u = 0.35/rad(H)` with prime classes of length <= 8, to 2e-3; the truncated full product is real and equals `|F|^2` exactly; positivity on the real axis | both |
| T2(d) | `sdet(1 - uH) = |F_gr(u)|^2` to 5e-3 with classes of length <= 6 | C^{2|2}, two odd and one even unitary letter |
| T2(c'), added after the proofs | Kraus letters: `det(1 - uH) = F(u)^2` at complex u to 5e-3; real coefficients of `det(1 - z E_w)`; the non-Kraus pair `E_1 = i, E_2 = -i` has `1 + u^2 = |1 - iu|^2` but not `(1 - iu)^2` | non-unitary Kraus; scalar |
| T2(e) | simple roots -1, 1/3 of the bouquet polynomial; in the transition convention the Ad path traces of a path and its twist are neither equal nor opposite (random Kraus; the prover's `U_e = U_f = diag(1, i)` with traces 0 and 4); classical weights twist symmetric; loopwise time reversal; Kraus loop traces real and nonnegative | non-unitary Kraus, unitary, classical |
| T3(a) | `Gamma_c^2 = 1`, `[Gamma_c, Gamma_b] = 0`, `Gamma_c H Gamma_c = H^eps` (and J, Sigma), sector determinants invariant under the sign twist | C^{2|2} three odd; C^{1|1} two odd; C^{2|2} two odd + one even |
| T3(b) | anticommutation with H, J, Sigma; symmetric sector spectra; `det(1 - uH_k)` even and equal to `det_+(1 - u^2 H_k^2|_+)` at real and complex u; `Sigma_k = [[0, a],[a^*, 0]]`; `det(1 - u Sigma_k + q u^2) = det_+((1 + q u^2)^2 - u^2 a a^*)`; `spec(Sigma_k)^2 = spec(a a^*)` doubled; band equivalence; balanced grading | the two all-odd families |
| T3(c) | `Gamma_c = +1` part of the odd sector is `Hom(V_-, V_+) (x) C^D`; `spec(H_1^2|_+)` = squares of the odd edge eigenvalues, each once | the two all-odd families |
| T3(d) | `Sigma 1 = D 1`, `Sigma P = -D P`, `Gamma_c 1 = P`; trivial even edge eigenvalues q, 1, -q, -1 present | the two all-odd families |
| T3(e) | even-sector spectrum not symmetric with one even letter (random mixed family; Pauli X,X,Y,Y,Z,Z with even spectrum {6, -2}) | |
| T3 (D_5) | five reflections of D_5, each twice (D = 10, q = 9), P the rotation grading: anticommutation; `Sigma_1 = 0`; `det(1 - uH_1) = (1 - u^2)^8 (1 + 9u^2)^2`; the four nontrivial odd edge eigenvalues on `|mu| = 3` | |
| T4 | `h` odd; `det(1 - uh) = det_+(1 - u^2 h^2|_+)`; `str h^k = 0` for k <= 6; word sums of `Tr(P U_w)` vanish at lengths 2 and 4; `str H^2 = sum_w |Tr(P U_w)|^2 = 24.26 > 0` | C^{2|2} three odd |

Findings for the reviewer: the brief's T2(e) claim that Ad-weights are twist symmetric was tested in the first version with the terminal letter included in the path weight, which is the wrong convention (the prover's <1>4 identity); in the transition convention the traces are neither equal nor opposite, as the prover found, and the checks now say so. The Kraus real-square strengthening of T2(c) (the prover's <1>4) is confirmed. The one check that failed on the
first run was the D_5 modulus test, which counted the `|mu| = 1` eigenvalues of the
`(1 - u^2)^{n_1(D-2)/2}` factor as nontrivial; the corrected check excludes them (they are the
trivial `+-1` of `prop:odd-sector-two-step`(b)).
