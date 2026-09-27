# Lane AS: Artin–Schreier transfer-matrix station (`demos-as.js`)

## Built

`WT.demos.artinSchreier` (mount `demo-artinSchreier`, 171 lines). The numerics are exposed as
`WT.demos.artinSchreier.num` (`transfer, perturb, vMinus, hPer, eigQR, analyse, PINNED`) so node can run them.

- Controls (all ids prefixed `demo-artinSchreier-`): `q` ∈ {3,5,7}, `J` ∈ {1,2}, `a0..aJ` selects (the `a_J` select offers
  only 1..q−1, so a_J ≠ 0 always holds), `eps` slider in [0, 0.5] (perturbation), `K` slider 2..14 (the window shown in the heat map).
- (a) `-phase`: E as a phase map. Each cell is filled with the categorical colour `WT.CYC[k]` of the root of unity ψ(k) it holds,
  plus a unit-circle arrow in `var(--ink)` when dim ≤ 25; colour only for dim 49. Rows and columns are labelled by bond states,
  and the perturbed cell is outlined in `--spec`.
- (b) `-spec`: the spectrum of E (marked *comparison*) with the circle √q; for ε > 0 the true spectrum is drawn as hollow `--ink2` markers.
- (c) `-count`: Re/Im bars of Tr Eⁿ/q^{n/2}, n = 1..8, and a table with n, Tr Eⁿ, Sₙ, the transfer-matrix Nₙ (integrality checked to
  1e-6; shown with ✗ when it fails), the pinned brute-force count (precomputed) with ✓/✗, and |Nₙ − qⁿ| ≤ q^J(q−1)q^{n/2}.
- (d) `-weil`: heat map of Re T for the window K; `-mins`: λ_min against K = 1..14 on an asinh scale, blue if ≥ −1e-9 and orange if negative.
- (e) `-readout`: g, dim E, the chirp-Fourier remark (J = 1), the unitarity residual, the functional-equation residual ‖E − qE^{−†}‖_F/q,
  eigenvalue moduli with the maximum deviation from √q, the sign law with v₋ and h, and then either the unitary verdict with the "why" line
  and the "no pole" line, or the broken-unitarity verdict. All colours go through `var(--token)` strings, so a theme switch needs no redraw.

**Spectra: what I did about q = 7, J = 2.** I tested `WT.cmat.eigvals` (charpoly + Durand–Kerner) at dim 25 on E/√q.
For q = 5, a = (0,0,1) the moduli come out wrong by 2.7e-5, because the unitary spectrum has repeated eigenvalues.
So the demo uses its own ~25-line complex Hessenberg + Wilkinson-shifted QR (`eigQR`), which is backward stable.
Against numpy it matches to 1.1e-14 at dim 25 and 1.9e-14 at dim 49. The spectrum is therefore shown at every size, including dim 49.
It stays a comparison panel: the verdict's Weil form is built only from Tr Eᵏ.

## Mathematics used

| statement | label | where the demo computes it |
|---|---|---|
| E_{(s₁..s_J)→(s₂..s_J,x)} = ψ(a₀x² + Σ a_j s_{J+1−j} x), rows = output state, states lexicographic (s₁ most significant), as in `scripts/artin_schreier_mps.py` | eq:as-transfer-entries, prop:as-transfer-matrix | `transfer` |
| EE† = qI if a_J ≠ 0 (oldest spin linear: Σ_{s₁} ψ(a_J s₁(x'−x'')) = qδ) | prop:as-unitarity | residual line and "why" line |
| functional equation E ↦ qE^{−†} | sec:artin-schreier (note §5) | ‖E − qE^{−†}‖_F/q |
| exact sign law Sₙ = (−1)^{n−1}δₙ Tr Eⁿ = (1 − 2·[2h ∣ n]) Tr Eⁿ; h = least power of q > v₋, v₋ = ord_{z=−1} z^J P_g(z), P_g = Σ(a_j/2)(z^j+z^{−j}) | thm:as-sign-law, cor:as-periodic-sign, def:as-ring-forms | `vMinus`, `hPer`, Sₙ column |
| Nₙ = qⁿ + Σ_{a≠0} Sₙ(ag) (affine; the projective curve adds 1) | eq:as-hilbert90, thm:as-super-transfer | Nₙ column; E_{ag} built for each a |
| t_{k−j} = Tr((E^j)^† E^k)/q^{(j+k)/2}: the Toeplitz form is the Gram matrix of the open strips when E/√q is unitary | prop:ccm-tn-operator-gram | panel (d), unitary verdict |
| positivity ⇔ \|μ\| ≤ r (one-sided) | thm:weil-positivity-finite (T1) | perturbed verdict |

## Independent check (`python3 notes/weil-tn-tutorial/lanes/check_as.py`, from the repo root)

The check reuses `irreducible, polymulmod, polypow, S_bruteforce, transfer` from `scripts/artin_schreier_mps.py`.
Point counts come from a separate direct enumeration of (x, y) with y^q − y = g(x). It then runs the JS numerics in node
(window/document stub, core.js, demos-as.js) and compares the two. The worst Python/JS discrepancy over all compared numbers
(Tr Eⁿ for n ≤ 8, Nₙ, λ_min for K = 1..14 at ε = 0 and at ε = 0.3, spectra) is **1.2e-13: PASS**.

| (q, a) | ‖EE†−qI‖_F/q py / JS | max\|\|λ\|−√q\| | v₋, h | λ_min K=4, 8, 12 (ε=0) | ε=0.3: residual; λ_min K=4, 8, 12, 14 (py = JS to 6 d.p.) |
|---|---|---|---|---|---|
| 3, (0,1) | 3.9e-16 / 3.0e-16 | 4.4e-16 | 0, 1 | −1.8e-15, −3.6e-15, −7.8e-15 | 0.199251; 0.019950, 0.011740, 0.010743, 0.010546 |
| 3, (1,1) | 5.4e-16 / 5.2e-16 | 4.4e-16 | 2, 3 | −1.6e-15, −3.4e-15, −1.0e-14 | 0.199251; 0.057726, −0.280980, −0.699677, −1.045066 |
| 5, (0,1) | 2.4e-16 / 1.8e-16 | 1.8e-15 | 0, 1 | 4.0, −9.2e-16, −2.2e-15 | 0.169070; 3.880449, 0.014344, 0.009576, 0.008849 |
| 3, (0,1,1) | 6.5e-16 / 5.1e-16 | 2.7e-15 | 4, 9 | 6.0, 1.51, −1.2e-14 | 0.199251; 5.941450, 1.545866, −0.077605, −0.151923 |
| 3, (1,0,1) | 9.4e-16 / 8.9e-16 | 2.2e-15 | 0, 1 | 8.0, 4.0, −8.8e-15 | 0.199251; 7.899999, 3.704832, −0.067678, −0.457054 |

All ε = 0 minima are ≥ −1e-12, as required. They are exactly 0 up to rounding once K exceeds the number of distinct eigenvalues,
since the Gram matrix of the strips has that rank.

Sign law against brute-force Sₙ (n ≤ 5 for dim 3, n ≤ 3 for dim 9): the exact law holds in every case.
The brief's law −(−1)ⁿ Tr Eⁿ fails at n = 2 and 4 for (3,(1,1)) and at n = 2 for (3,(0,1,1)).

Nₙ from the transfer matrices (exact law) = brute force (these are the pinned numbers hard-coded in the demo):

| q, a | n = 1 | 2 | 3 | 4 | band q^J(q−1)q^{n/2}, n = 1..4 |
|---|---|---|---|---|---|
| 3, (0,1) | 3 | 3 | 27 | 27 | 10.39, 18, 31.18, 54 (saturated at n = 4) |
| 3, (1,1) | 3 | 9 | 27 | 81 | same |
| 3, (0,1,1) | 3 | 9 | 27 | – | 31.18, 54, 93.53 |
| 3, (1,0,1) | 3 | 15 | 27 | – | same |

Transfer-matrix Nₙ for n = 1..8 (py = JS, printed identically in the demo):

- (3,(0,1)): 3, 3, 27, 27, 243, 675, 2187, 6075
- (3,(1,1)): 3, 9, 27, 81, 243, 891, 2187, 6561
- (5,(0,1)): 5, 5, 125, 125, 3125, 15125, 78125, 378125

The imaginary parts are below 1e-10.

## Findings against the brief

1. **Sign law.** The brief's Sₙ = −(−1)ⁿ Tr Eⁿ is the founding note's claim, and 06b (thm:as-sign-law, cor:as-periodic-sign)
   corrected it. It holds for all n iff P_g(−1) ≠ 0 (v₋ = 0), which is the case for q = 3, a = (0,1) (the check the brief asked for),
   but it fails e.g. for (3,(1,1)), where S₂ = +Tr E². The demo implements the exact law, Sₙ = (1 − 2[2h∣n]) Tr Eⁿ, and prints v₋ and h.
   The brief's law gives the same Nₙ in the q = 3 cases checked: the flipped Sₙ(g) are purely imaginary and cancel against Sₙ(2g) = conj Sₙ(g).
   This is not true in general.
2. **E[0][1] is structurally zero for J = 2**, because state (0,1) cannot shift to (0,0). The perturbation therefore multiplies
   E[0][c] by e^{iε}, with c the first column ≥ 1 where row 0 is nonzero: c = 1 for J = 1 (as briefed) and c = q for J = 2.
3. **"With ε > 0 the form goes negative once K is large enough" is false for (3,(0,1)) and (5,(0,1)).** There the perturbed
   eigenvalues never leave the closed disc: one stays on the circle and the rest move inside, with max|λ|/√q = 1.0000 for all
   ε ∈ [0.05, 0.5]. By T1 the form stays positive (λ_min ≈ 0.0105 at K = 14 for q = 3, ε = 0.3). The demo says so explicitly
   (T1 is one-sided and the Weil form cannot see a contraction; the counting side can, because Nₙ stops being an integer).
   The form does turn negative in the other cases:
   - (3,(1,1)): at K = 5 from ε = 0.05
   - (3,(0,1,1)): at K = 11
   - (3,(1,0,1)): at K = 12

   For larger dims (e.g. q = 5, J = 2, a = (2,1,3); q = 7, J = 2) some eigenvalue leaves the disc, but λ_min stays positive
   for K ≤ 14. The readout then says that a larger window will turn it negative.
4. **Nₙ is the affine count**, as briefed. The projective count (thm:as-super-transfer) adds 1, and the demo's footnote says so.
5. **Spectra use a local QR, not `WT.cmat.eigvals`** (see *Built*). As a result q = 7, J = 2 is fully supported, spectrum included.

## Visual check

Playwright (global `playwright@1.56.1`, chromium-1194) rendered a scratch page with theme.css, core.js and demos-as.js in five states:

- light at 1000px (default)
- dark at 1000px (q = 5, J = 2, a₀ = 2, ε = 0.3)
- light at 400px (q = 3, J = 2)
- dark at 1000px (q = 7, J = 2, ε = 0.5)
- light at 1000px (q = 3, a = (1,1), ε = 0.3, K = 12)

There were no page errors and no horizontal page scroll at 400px; the counts table scrolls inside its own box. The fix pass
addressed a grid-column overflow (min-width: 0), the table width, clipped titles, legend/tick overlap, and the bar scale at dim 25.

## Open

- Why one eigenvalue stays exactly on the circle for J = 1, a₀ = 0 under the E[0][1] phase perturbation was not analysed (observed numerically only).
- The Weil form uses E itself (every eigenvalue a zero). When v₋ > 0, the Frobenius block F of thm:as-frobenius-block differs from −E,
  but its eigenvalues also have modulus √q; the demo does not build F.
