# REFUTE review: RTP round 2, lane I (impure lattice bumps)

Reviewer: `claude:opus` (adversarial REFUTE protocol).
Date: 2026-09-26. Subject: `notes/rtp-round-2/impure-bumps/astra-proofs.md` (author `codex:gpt-6-astra`, 2026-09-26),
items I1–I6, the threshold table, "Numerical checks for the blind lane" and the ten candidate rows of
"What this changes in the notebook".

Nothing here assumes RH. Zeros are used only in the block labelled COMPARISON STEP
(`scratch_rtp2_impure_compare.py`). No lane file, script, output, shard or `db/` row was edited; git was not run.

## Inputs read

| file | what it is |
|---|---|
| `notes/rtp-round-2/impure-bumps/astra-proofs.md` (in full) | the report under review |
| `notes/rtp-round-2/impure-bumps/astra-brief.md`, `notes/rtp-round-2/brief.md` | lane brief, round rules and conventions |
| `scripts/rtp2_impure_bumps.py` (in full), `outputs/rtp2_impure_bumps.txt` (in full), `checks/results.json`, `checks/progress.txt` | the lane's script, output, machine-readable results |
| `notes/rtp-round-1/lane-A2.md` §§1–4 | definitions 1.1–1.2, admissibility table, Kronecker lemma 4.1 |
| `scripts/rtp1_prime_content.py` (definitions only) | A2's closed forms |
| `notes/reviews/rtp-round-1-2026-09-24.md` (header, verdict table, C4–C5, VERDICT block) and `notes/reviews/scratch_rtp1_lattice.py` | format; previous real-space implementation |
| `report/sections/08i_riemann_tomography.tex` | `lem:mixed-entries-kronecker`, `num:rtp-prime-content`, `obs:rtp-round-1-reading` |
| `notes/metric-tomography/metric-as-state.md` §7.2 | the contradiction pathway the report invokes |
| `refs/src/2511.22755/mc2arXiv.tex` l.420–500 | `W_p`, `W_R` in the `F` normalisation (l.445–451), `bombtest` (l.465–467), `bombtest-0` |

## Scripts written for this review (under `notes/reviews/`; deterministic, no timestamps)

| script | checks | what it does, independently of the lane |
|---|---|---|
| `scratch_rtp2_impure_thresholds.py` | 22 | all twelve E/H onset rows by brute force over every prime power in `[r/2, 2r]` for every lattice ratio (no nearest-neighbour shortcut), exact `Fraction` separations, 40-digit logs; full admissibility = E onset = lane A2's `delta_max`; R-leakage onsets; first-overlap widths; the external-prime lists; enumeration of **all** minimising pairs (ties) |
| `scratch_rtp2_impure_theory.py` | 10 | tensor-shift form of `B_D` and its ranks; the `k = 3` rank-two counterexample; I2b bounds on 2322 random instances; I2c bounds on 4000 instances; the hypothesis `a >= ||T||_2` is load-bearing (131 lower-bound failures without it); `eps < g/4 => a >= ||T||_2`; the quadratic law `defect/s^2 -> ||Nz||^2`; `M_L (x) I` (no lower bound from `eta`); the Fourier identity for `f^* * g` at complex `z`; paired-zero form PSD on the line and indefinite for an off-line quadruple; independence of overlapping translates |
| `scratch_rtp2_impure_gram.py` | 27 | seven Gram matrices at **non-admissible** widths from the definitions in real space, mpmath 30 digits: every archimedean entry a nested 2D tanh–sinh integral of the bump itself (`int int phi phi rho(D+x-w)` for `D > 2 delta`; for overlapping entries `W_R`'s defining finite-part integral written as `int_x phi(x) int_0^Y [phi(x-y+D)+phi(x+y+D)-2e^{-y/2}phi(x+D)] rho(y) dy dx` plus the exact `log tanh` tail), split at every support edge; no Chebyshev `R_1`, no 1D `q`-integral; prime term over all prime powers, subtracted; `mp.eigsy`. Minus-sign decomposition, Kronecker identity against independently assembled one-prime forms, E/H/R split, I2c bounds, four ablations |
| `scratch_rtp2_impure_channel.py` | 4 | per-prime amplitude matrices `B_q` (q = 2, 3 and every external q) on `{2,3}, A = 2` at `delta = 0.2` and `0.0594`; `d lambda/d theta_q` and `d(defect)/d theta_q`; same for the mixed pole and mixed archimedean amplitudes; I5 chain at `A = 1, delta = 0.2` |
| `scratch_rtp2_impure_compare.py` | 3 | COMPARISON STEP: prime side at `delta = 0.1`, ratios 6 and 8 (reviewer's entries); zero side with mpmath Fourier transforms (64 panels) over the 2000 cached ordinates, spot-checked against `mpmath.zetazero` |
| `scratch_rtp2_impure_scan.py` | (locator) | **not independent**: uses the lane's own `FastKernel`/`build` to scan 4001-point grids (10x the lane's) and to minimise the ground gap at every local minimum, looking for an avoided crossing that could spike the defect between grid points |

All scripts pass (66 checks, 0 failed).

---

## Verdict table

| item | verdict | script | decisive check |
|---|---|---|---|
| I1 (corrected Kronecker lemma, E/H/R, minus sign, threshold table) | **MINOR** | `thresholds`, `gram`, `theory` | lemma exact at all seven non-admissible widths (Kronecker difference 0.0); every mixed prime entry `<= 0` in `G`; 12/12 threshold values to 1e-9; but "the binding pair" is not unique in 8 of the 12 H cells |
| I2 (affine response, I2b/I2c bounds, rank-two counterexample) | **VALID** | `theory`, `gram`, `channel` | I2b and I2c hold on 6322 random instances; Schur bounds at `delta = 0.2` reproduced (0.0021476779 <= 0.0031981480 <= 0.0032016245); `d lambda/d theta_q` for q = 5, 7, 37 reproduced |
| I3 (paired-zero identity, RH-conditional positivity, refutation of the "unconditional square") | **VALID** | `theory` | identity `hat(f^* * g)(z) = conj(hat f(conj z)) hat g(z)` to 4e-25 at complex `z`; an off-line quadruple gives a real, indefinite form (eigenvalue `-4.4e-9`) |
| I4 (sweep, 36 positive matrices, no defect > 0.1 on 401 grids) | **VALID** | `gram`, `scan` | 4 sweep rows reproduced to <= 5e-12 in `lambda`, <= 1e-9 in the defect; `lambda(K)` and the first-order/along-`v` pole/arch/prime triples reproduced; 4001-point grids give maxima 0.00838, 0.0382, 0.0321, no ground-state crossing |
| I5 (prime addition, sensitivity, ablations) | **VALID** | `gram`, `channel` | A = 1 chain `lambda` and movement to 1e-10; all four ablations (`-2.9496987345`, `-3.8055745265`, `-0.92987066659`, `-3.0178280392`) and their defects |
| I6 (comparison step) | **MINOR** | `compare` | prime sides 0.0047166817276683 and 0.0010952680781538 reproduced; M = 10..300 errors match; with mpmath transforms the **same float64 ordinates** close to 1.3e-18 and 6.2e-18 at M = 2000, so the report's 1e-15 "ordinate/quadrature floor" is its float64 Fourier quadrature, not the ordinates |
| Numerical checks for the blind lane | (inside I4/I1) | `gram`, `thresholds` | `0.001353720633183835123359`, `0.0001800746266448849465456`, `0.00003821907764671450095731` (differences 3.4e-21, 4.5e-22, 4.3e-23 from the report); defect 0.003198147992; `log(25/24)/2` to 32 digits |

**Tally: 12 VALID, 4 MINOR, 0 INVALID** (statements: I2, I3, I4, I5 VALID; I1, I6 MINOR. Candidate rows: 8 VALID,
2 MINOR).

---

## I1. Corrected Kronecker lemma, E/H/R, the minus sign: MINOR

*The minus sign.* In CCM's `F` normalisation `W_p(F) = log p sum_m p^{-m/2}(F(p^m)+F(p^{-m}))` (l.445–447) is a
nonnegative functional on nonnegative `F`, and `Psi = W_{0,2} - W_R - sum_p W_p` (l.465–467). With
`F = phi_a^* * phi_b = R_delta(. - D')`, `F(log k) + F(-log k) = R_delta(log k - D) + R_delta(log k + D) >= 0`, so every
prime power enters `G` with a minus sign, and the brief's `+ sum_k Lambda(k) k^{-1/2} P_k` has the wrong sign. The
report's `G = K + M_pole + M_arch - sum_k Lambda(k)/sqrt(k) (X o P_k)` is right: `scratch_rtp2_impure_gram.py`
reassembles `G` from `K`, the mixed pole, the mixed archimedean part and the mixed E/H/R prime parts to 1e-25 at all
seven widths, and every mixed prime entry of `G` is `<= 0`. The ledger's wording "Prime terms are negative" is loose:
the `P_k` are entrywise nonnegative; their contribution to `G` is negative.

*The lemma at all widths.* Every entry of `G` is `Psi` of a function of `D = |t_a - t_b|` only (also for overlapping
translates and for `2 delta >= log 2`, where the diagonal and the `log k + D` branch pick up `k = 2`), and unique
factorisation separates axis distances `j log p` from mixed ones. So `K` (mixed entries zeroed) is the Kronecker sum of
the **full** one-prime restrictions at that width. Checked against one-prime forms assembled separately:
difference exactly 0.0 at `{2,3}, A = 2` (`delta` = 0.0594, 0.2, 0.345), `{2,3}, A = 3` (0.0485, 0.2), `{2,3,5}, A = 2`
(0.0254, 0.2). This is `lem:mixed-entries-kronecker` as registered ("any even kernel"); the report adds nothing
false to it. The double-counting charge against the brief is correct on the literal reading (the round-1
`G_nomix` already contains axis impurities); on the charitable reading (`G_nomix` = Kronecker sum of pure combs) the
charge is only about the R leakage, which is real either way.

*E/H/R.* Correct. R leakage into mixed entries is real and is not small: its onset equals the H onset at
`{2,3}, A = 2, 3` (k = 2 at 9/4) and `{2,3,5}, A = 2` (k = 4 at 25/6); at `{2,3,5}, A = 3` it comes later
(0.0142 vs 0.0119). At `delta = 0.2`, `{2,3}, A = 2`, along the ground vector: E `-1.5172965`, H `-0.0420592`,
R `-0.1310258` (reproduced). The brief's (ii) is refuted as the report says.

*Rank.* `B_D = T_e + T_{-e}` with `rank T_e = prod_p (A + 1 - |e_p|)`; the ranks of the touched `B_D` on `{2,3}, A = 2`
are 2, 4, 6, never 1; the `k = 3, delta = 0.21` example is rank two with eigenvalues `+-c`. Refutation of
"rank one per pattern" stands.

*Threshold table.* All twelve E and H values reproduced to 1e-9 by brute force (not the nearest-neighbour search the
lane uses); E = full admissibility = lane A2's `delta_max` in all twelve rows. **Defect:** the text says the
enumeration is "an exhaustive proof of the binding pairs", but the minimiser is not unique in 8 of the 12 H cells:

| S, A | minimising pairs (H column) |
|---|---|
| {2,3}, 1 | 3:4, 6:8 |
| {2,3}, 2 | 9:8, 18:16, 36:32 |
| {2,3}, 3 | 18:16, 36:32, 72:64, 72:81, 216:243 |
| {2,3}, 4 | 36:32, 72:64, 144:128, 216:243, 648:729 |
| {2,3,5}, 1 | 15/2:8, 15:16, 30:32 |
| {2,3,5}, 2 | 25/3:8, 50/3:16, 100/3:32 |
| {2,3,5}, 3 | 125/8:16, 125/4:32, 125/2:64, 125:128, 250:256, 500:512, 1000:1024 |
| {2,3,5}, 4 | 2025/16:128, ..., 32400:32768 (9 pairs) |

The values are unaffected; the prose and the row must say "a binding pair". Script: `scratch_rtp2_impure_thresholds.py`.

## I2. Affine response and Schmidt bounds: VALID

I2a is exact and elementary (group the finite prime sum by base prime; Hellmann–Feynman and first-order vector
formula), and the derivatives reproduce (`-0.441838446`, `-0.3338406`, `-0.0490887763` for q = 5, 7, 37 from the
reviewer's own matrices). I2b: projecting `(K + M)v = lambda v` by `Q` gives `u = -a[B + QMQ - Delta lambda]^{-1} b` with
the bracket's spectrum in `[g - 2 eps, W + 2 eps]`; the two-sided bound on `t` and `defect <= ||u||^2 <= eta^2/((g-2eps)^2+eta^2)`
held in all 2322 random instances with `eps < g/2`. `M_L (x) I` gives `eta = 3.4e-2` and defect 0: the brief's
requested lower bound in terms of `eta` alone does not exist, as the report says. I2c: the factorisation
`L C R = diag(a, T)` and the rank-one-distance argument are correct; 0 violations in 4000 instances; the hypothesis
`a >= ||T||_2` is load-bearing (the lower bound fails in 131 random draws without it) and is implied by `eps < g/4`
(3000 instances near the boundary, 0 violations). The quadratic law: `defect/s^2 = 0.6567, 0.6540, 0.6527 -> ||Nz||^2 = 0.6514`.
Schur bounds at `{2,3}, A = 2, delta = 0.2` reproduced from the reviewer's own matrix.

One limitation the report states but the reader should see in the shard: I2b's hypothesis `||M|| < g/2` holds at
only the **11 narrowest** of the 36 sweep widths, and `K` is indefinite at 26 of them. The perturbation theorem does
not reach the regime the lane was asked about; only the finite I2c bound does (and it does at `delta = 0.2`).
Scripts: `scratch_rtp2_impure_theory.py`, `scratch_rtp2_impure_gram.py`, `scratch_rtp2_impure_channel.py`.

## I3. Paired-zero identity and conditional positivity: VALID

`hat(f^* * g)(z) = conj(hat f(conj z)) hat g(z)` (checked at `z = 3.7 + 0.21 i` to 4e-25), and `Psi(F) = sum_rho hat F(z_rho)`
is symmetric under `z -> -z` because the zero set is, so the sign convention of `z_rho` is immaterial. For
`rho' = 1 - conj(rho)`, `z_{rho'} = conj(z_rho)`: the pair contributes `2 Re(conj(hat f(conj z)) hat f(z))`, which is not a
square. On three translates a fictitious off-line quadruple (`beta = 0.1, gamma = 14`) gives a real form with
eigenvalues `(-4.4e-9, 2.4e-5, 4.2e-3)`; an on-line pair gives a PSD form. So the brief's "unconditional
`sum_rho |...|^2`" is false and the report is right to refute it; squares need H-RH. The negative-certificate
implication (a certified negative eigenvalue refutes RH, by Weil's criterion) is correct and is exactly
`metric-as-state.md` §7.2. Absolute convergence: the bump transform decays like `exp(-c sqrt|t|)`, faster than any
power, on horizontal strips; fine. Linear independence of overlapping translates: the proof is right (exponential
polynomial vanishing on an interval), and five translates at spacing 0.05, `delta = 0.3`, have a nonsingular L2 Gram
matrix (min eigenvalue 5.2e-5). Script: `scratch_rtp2_impure_theory.py`.

## I4. Sweep: VALID

Independent real-space recomputation (`scratch_rtp2_impure_gram.py`), reviewer's value vs report:

| S, A, delta | lambda_min(G) | report | defect | report | lambda(K) | report |
|---|---|---|---|---|---|---|
| {2,3}, 2, 0.0593710412 | 0.066437458388105 | 0.06643745839 | 0.005197069153 | 0.0051970692 | -0.3617846102 | -0.36178461 |
| {2,3}, 3, 0.048514948 | 0.018836768313438 | 0.01883676831 | 0.02109790047 | 0.0210979 | -0.5921371207 | -0.592137121 |
| {2,3,5}, 2, 0.0254263116 | 0.053332773685154 | 0.05333277369 | 0.01701884861 | 0.017018849 | -0.9129823413 | -0.912982341 |
| {2,3}, 2, 0.345 | 0.000088427383332 | 8.842738307e-05 | 0.002673883293 | 0.0026738833 | -0.008477374169 | -0.00847737417 |

The pole/arch/prime triples at `v0` and at `v` in the report's "exact decomposition" table reproduce (e.g. `{2,3}, 2, 0.345`:
`+6.1506, -1.6993, -4.4427` at `v0`, `+4.8999, -1.5900, -3.3030` at `v`). The claim "positive by more than a million
times the estimate" is true (minimum ratio 1.66e6, at `{2,3,5}, 0.345`), but the doubling estimate (6.9e-14 per entry)
is about half the float64-vs-mpmath discrepancy the lane itself measured at `delta = 0.2` (1.5e-13); the margin is
still six orders of magnitude.

*Trying to break "no defect > 0.1".* The ground gap falls to 3e-6, so an avoided crossing inside one reflection
sector could produce a defect spike between grid points. On 4001-point grids (10x the lane's) with bounded
minimisation of the gap at all 27 local minima, the maxima are 0.00838 / 0.0382 / 0.0321 (lane: 0.00835 / 0.0381 /
0.0320); at every gap minimum the two lowest states have **opposite** reflection parity (so they cannot mix), the
ground state stays even throughout, and the defect is flat to 1e-6 across each minimum. No crossing. This locator
uses the lane's kernel; its values at the four widths above agree with the independent implementation to 5e-12,
which is what licenses it. The continuum statement stays OPEN, as the report says.

Bookkeeping the row must carry: the first width of each set is the admissible threshold itself (impurity weight
exactly zero), so **33** of the 36 matrices are impure; 12 of the 36 have overlapping translates (L2 Gram `H != I`),
where eigenvector and defect are coefficient-basis diagnostics (the report says this in ledger item 6).

## I5. Prime addition and sensitivity: VALID

From the reviewer's matrices: A = 1, `delta = 0.2`: `{2,3} -> {2,3,5}`: `lambda` 0.009617377905 -> 0.002228248928,
movement 0.01341788669; `{2,3,5} -> {2,3,5,7}`: -> 0.0002422501425, movement 0.01852628918 (report ...422 in the last
digit of `lambda`; float64). Ablations at `{2,3}, A = 2, delta = 0.2`: all four eigenvalues and defects agree to 1e-10.
The report's caveats (removal of a prime is not a positivity-preserving operation; full removal and the amplitude
derivative are different regimes; prime addition also widens the sampled third primes) are correct.

## I6. Comparison step: MINOR

Prime side from the reviewer's real-space entries: 0.0047166817276683449 (r = 6, prime powers 5, 7) and
0.0010952680781538118 (r = 8; 7, 8, 9), matching the report to 1e-16. The M = 10, 30, 100, 300 errors match the
report's table to 4 digits. With mpmath transforms of the same 2000 float64 ordinates (which agree with
`mpmath.zetazero` at n = 1, 100, 2000 to 8e-14), the M = 2000 differences are **1.3e-18 and 6.2e-18**; at M = 1000,
4.1e-15 and 5.6e-15. The report's floor (1.1e-15, 3.3e-16) is its float64 Gauss–Legendre transform, not the
ordinates. Correct the sentence (below). Script: `scratch_rtp2_impure_compare.py`.

## The channel verdict: partly supported

The report's paragraph says the newly admitted prime data are third-prime masses (plus R leakage), that pole and
archimedean mixed entries are genuine couplings, and that in the measured example the third primes enforce a
cancellation leaving the ground vector near product. The data support that, but the paragraph (and the brief's
slogan "third-prime channel, not a 2–3 correlation") understate the pole. Along the ground vector, mixed parts at
all seven reviewer widths:

| S, A, delta | mixed pole | mixed arch | E | H | R | pole / abs(E) |
|---|---|---|---|---|---|---|
| {2,3}, 2, 0.0594 | +0.8134 | -0.2737 | -0.1507 | 0 | 0 | 5.40 |
| {2,3}, 3, 0.0485 | +1.6697 | -0.5081 | -0.5960 | 0 | 0 | 2.80 |
| {2,3,5}, 2, 0.0254 | +2.6243 | -0.5261 | -1.1836 | -0.0005 | -0.0005 | 2.22 |
| {2,3}, 2, 0.2 | +2.8574 | -1.0254 | -1.5173 | -0.0421 | -0.1310 | 1.88 |
| {2,3}, 3, 0.2 | +6.6716 | -2.0347 | -3.7780 | -0.1046 | -0.6025 | 1.77 |
| {2,3,5}, 2, 0.2 | +19.0100 | -3.4841 | -11.9072 | -0.8336 | -2.4883 | 1.60 |
| {2,3}, 2, 0.345 | +4.8999 | -1.5900 | -2.5605 | -0.1932 | -0.5493 | 1.91 |

The pole is the largest mixed term at every width. For the correlation observable itself
(`scratch_rtp2_impure_channel.py`, `{2,3}, A = 2`): at `delta = 0.2`, `d(defect)/d(amplitude)` is `+3.08` for the mixed
pole, `+0.89` for the mixed arch, negative for **every** external prime (sum of magnitudes 4.09; largest q = 17, 19,
7, 11), and 0.78 in total for 2 and 3 (their mixed leakage alone: `+0.012`, `-0.001`). At `delta = 0.0594`: pole 0.045,
externals 0.038, 2 and 3 0.032 (through their axis entries), arch 0.011. For `lambda_min` the local primes dominate at
0.0594 (1.88 vs 0.15) and are comparable at 0.2 (2.16 vs 1.68). So: the impure **mixed prime remainder** is a
third-prime object (E dominates it at every width with non-zero E), but the inter-place **observable** is a balance
of the pole against the third primes with comparable magnitudes; it is neither "third-prime" nor "2–3" alone. The
E/H/R split in the report rests on one lattice at one width; the table above is the evidence the row needs.

---

## Corrections to apply

1. Ledger item 1. Replace "Prime terms are negative." with: "Prime powers enter `G` with a minus sign
   (`Psi = W_{0,2} - W_R - sum_p W_p`, `mc2arXiv.tex` l.465–467); the matrices `P_k` are entrywise nonnegative."
2. Threshold paragraph. Replace "This gives an exhaustive proof of the binding pairs without relying on near-tied
   floating logarithms." with: "This gives an exhaustive proof of the threshold values without relying on
   near-tied floating logarithms. The displayed pair is one minimiser: in the H column the minimiser is not unique in
   eight cells (e.g. {2,3}, A = 1: 3:4 and 6:8; {2,3,5}, A = 2: 25/3:8, 50/3:16, 100/3:32; list in
   `notes/reviews/rtp-round-2-impure-bumps-2026-09-26.md`)."
3. I4, after "Each set has 12 log-spaced widths from its admissible onset to 0.345.": insert "The first width of each
   set is the admissible threshold itself, where every impurity weight vanishes, so 33 of the 36 matrices are
   impure. The hypothesis H-small of I2b holds only at the 11 narrowest widths; `K` is indefinite at 26 of the 36."
4. I6. Replace "The last errors reach the float64 ordinate/quadrature floor and must not be read as measured
   infinite-tail errors at 1e-18." with: "The last errors are the floor of the float64 Gauss–Legendre transform: with
   mpmath transforms of the same float64 ordinates the M = 2000 differences are 1.3e-18 (r = 6) and 6.2e-18 (r = 8)
   (`notes/reviews/scratch_rtp2_impure_compare.py`); they are not measured infinite-tail errors."
5. Channel verdict. After "It is therefore not a clean correlation between 2 and 3 alone." insert: "Along the ground
   vector the mixed pole is the largest mixed term at every width checked (1.6 to 5.4 times the external part);
   the inter-place Schmidt defect is a balance in which the pole raises and every external prime lowers the defect
   (at {2,3}, A = 2, delta = 0.2: +3.08 for the mixed pole, -4.09 summed over external primes, per unit amplitude),
   while the mixed leakage of 2 and 3 is negligible for it (+0.012, -0.001)."
6. Candidate row `num:impure-thresholds`, content: replace "exact twelve-row E/H onset table" with "exact twelve-row
   E/H onset values with one binding pair each (ties in eight H cells)".
7. Candidate row `num:impure-bump-sweep`, content: replace "36 positive matrices with precision estimates; no 0.1
   defect on the specified 401-point grids" with "36 positive matrices (33 impure; 12 with overlapping translates,
   where eigenvector and defect are coefficient-basis quantities) with precision estimates; no 0.1 defect on the
   specified 401-point grids (none on 4001-point grids either, reviewer)".

## Recommendation for shard 08j

Register, with the corrections above:

- `lem:impure-mixed-kronecker` (lemma, proved), absorbing `prop:impure-pattern-rank` (the tensor-shift form of `B_D`
  and the rank-two example are one remark) and `prop:impure-prime-response` (the affine dependence is a one-line
  regrouping; the eigenpair derivative formulas are textbook). Three rows for one elementary lemma is padding.
- `prop:schmidt-schur-bounds` (proposition, proved), stating in the row that I2b needs `||M|| < g/2`, which fails at
  25 of the 36 sweep widths, and that I2c needs `a >= ||T||_2`.
- `prop:impure-weil-positivity` (proposition, proved-conditional on H-RH for the squares; the paired identity and the
  certificate implication unconditional). It is Weil's criterion restricted to a family; say so and cite
  `cit:weil-criterion`.
- `num:impure-thresholds` and `num:impure-bump-sweep` (numerical) as corrected.
- `num:impure-prime-sensitivity` (numerical), with the pole-versus-third-prime balance of the channel section above
  (it is the finding of the round for this lane: the true form's ground vector stays within defect 0.04 of product on
  every grid, because third primes cancel the pole's inter-place correlation).
- `obs:impure-logdet-gap`: fold into the sweep row as one sentence; it corrects a term the brief used, not a result.
- `question:impure-continuous-crossing` (open).

`obs:rtp-round-1-reading`(i): replace "`O(delta^2)` in eigenvectors" by "`O(delta)` in the eigenvector,
`O(delta^2)` in `1 - overlap` and in the Schmidt defect", and replace "`O(1)` inter-place structure needs
non-admissible bumps" by "non-admissible bumps (checked to `delta = 0.345` on `{2,3}`, A = 2, 3 and `{2,3,5}`, A = 2)
admit `O(1)` prime entries but leave the Schmidt defect below 0.04 on every sampled width". Nothing in this lane
bears on RH.

---

VERDICT I1: MINOR — the lemma, the minus sign and the E/H/R classification are right at every width; the threshold values are right, but "the binding pair" is one of several minimisers in eight H cells, and "prime terms are negative" should read "enter G with a minus sign".

VERDICT I2: VALID

VERDICT I3: VALID

VERDICT I4: VALID

VERDICT I5: VALID

VERDICT I6: MINOR — the 1e-15 floor at M = 2000 is the float64 Fourier quadrature, not the ordinates: mpmath transforms of the same ordinates agree to 1.3e-18 and 6.2e-18.

VERDICT lem:impure-mixed-kronecker: VALID

VERDICT prop:impure-pattern-rank: VALID

VERDICT prop:impure-prime-response: VALID

VERDICT prop:schmidt-schur-bounds: VALID

VERDICT prop:impure-weil-positivity: VALID

VERDICT num:impure-thresholds: MINOR — binding pairs are not unique (ties in eight H cells, e.g. {2,3,5}, A = 2: 25/3:8, 50/3:16, 100/3:32); state "one binding pair".

VERDICT num:impure-bump-sweep: MINOR — the row must say that 3 of the 36 widths are the admissible threshold itself (33 impure) and that 12 have overlapping translates, where eigenvector and defect are coefficient-basis quantities.

VERDICT num:impure-prime-sensitivity: VALID

VERDICT obs:impure-logdet-gap: VALID

VERDICT question:impure-continuous-crossing: VALID
