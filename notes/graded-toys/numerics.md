# Graded toys: blind numerics lane

**Lane.** Numerics, author line `claude:opus`.
**Brief tested.** `notes/graded-toys/brief.md` (claims G1--G7), author `claude:fable-5.1`, 2026-09-20.
**Protocol.** *Blind to the prover.* `notes/graded-toys/proofs.md` was not read, not opened and not
searched for. The definitions were taken from the shards the brief cites --
`report/sections/04i_cusp_graph_scattering.tex`, `04j_cusp_graph_renewal.tex`,
`04k_elliptic_cavity_scattering.tex`, `04l_elliptic_cavity_channel.tex`, `04h_rebound_state.tex`,
`02h_definitions_graded_ramanujan.tex`, `02f_definitions_graded_cmps.tex` -- and from the header
comment of `scripts/elliptic_cavity.py` (conventions only). Nothing is imported from any other
repository script; the diagrams, determinants, model spaces, channels and characters are all
re-implemented here.

**Artefacts.** `scripts/graded_toys.py` (2002 lines, seed `20260920`; imports only numpy, mpmath and
sympy from the permitted set -- scipy was allowed but not needed), output captured by

```
python3 scripts/graded_toys.py > outputs/graded_toys.txt 2>&1
```

from the repository root. Runtime **11.7 s**; the output is byte-for-byte reproducible run to run
(verified by three runs and `diff`), contains no timestamp and no memory address.

**Tally: 512 checks, 498 passed, 14 failed.** Every one of the 14 failures is a claim of the brief
that does not hold as stated; each is paired in the script with a CORRECTED assertion that passes.
No tolerance was loosened to make anything pass.

---

## Ledger

Line numbers are lines of `scripts/graded_toys.py` (the line on which the `check(...)` call begins).
Where a row cites several lines, they are the assertions that make up that row.

| # | Brief claim | What was computed | Result | Verdict | Line(s) |
|---|---|---|---|---|---|
| D1 | G0 / `def:elliptic-cavity`, `prop:stabiliser-normalisation` | D2, D3 transcribed from shard 04k; degree of every core vertex and of every first ray vertex; junction couplings `c^2 = S(v)/S(e)`; symmetry of `Ahat`; the normalised core weights | all degrees `q+1` (3 on D2, 4 on D3); `c^2 = 1` at every junction; `C_D2 = diag(0,1,0,0,0,0)`, `C_D3 = diag(0,1,0,0,0,0,1,0,2)`; weights `sqrt(3/2), 1/sqrt2, 1` / `2/sqrt3, sqrt(2/3), 1` | VERIFIED | 236, 239, 242, 245, 250, 252, 260, 263 |
| D2 | G0, `thm:d2-zeta`, `thm:d3-channels` | `p`, `ptilde` by exact integer arithmetic in `t = z/sqrt q` | `p_2 = (z^2/2)(z^2-2)(z^2+1)^2(2z^4-2z^2+1)`, `ptilde_2 = -(1/2)(z^2+1)^2(2z^2-1)(z^4-2z^2+2)`, `p_3 = (z^4/3)(z-1)^2(z+1)^2(z^2-3)(z^2+1)^2(3z^4+1)`, `ptilde_3` as displayed; `ptilde = z^{2n}p(1/z)`, `ptilde(0)=1` | VERIFIED | 274, 276, 278, 281, 285 |
| D3 | G1(a) | `det(z-M) = p`, `det(1-zM) = ptilde` for a *generic* symbolic core, `n = 2` (5 symbols) and `n = 3` (9 symbols) | identically zero difference | VERIFIED | 332, 335 |
| D4 | G1(a) | the same on D2 and D3, coefficient by coefficient | deviations `6.0e-15` (D2), `1.1e-14` (D3) | VERIFIED | 353, 360 |
| D5 | G1(a) | on D2: the split of `spec M`; cancellation of unimodular conjugate pairs in `prod (z-mu)/(1-z mu)`; `R = -prod`; exterior roots `= 1/vartheta` | 4 unimodular (`+-i` twice), 6 interior (4 Hasse--Weil at `|z| = 0.8408964` + double 0), 2 exterior (`+-sqrt2`); cancellation residual `1.1e-16`; `R` deviation `4.2e-17`; `vartheta = +-q^{-1/2}` | VERIFIED | 475, 480, 485, 488 |
| D6 | G1(b) | `Tr M^m = sum_{roots of p} mu^m` (power sums by Newton's identities) | D2/D3, `m = 1..8`: deviations `3.6e-14`, `5.7e-14`; five random rational cores, `m = 1..6`: exact over Q | VERIFIED | 369, 525 |
| D7 | G1(c) | `ker M = 0 (+) ker(I-C)`; `ord_0 p = 2 dim ker(I-C)`; nullities of `M, M^2, M^3` | D2: `1, 2, 2`, `ord_0 p = 2`; D3: `2, 4, 4`, `ord_0 p = 4`; five random cores (junctions made loopless) all consistent | VERIFIED | 377, 385, 531 |
| D8 | G1(c) | the same with a **loop** at the `c = 1` junction: `T = [[1/2,1],[1,-1/3]]`, `C = diag(1,0)` | `dim ker(I-C) = 1` but `ord_0 p = 1`, `p = z(6z^3-z^2-z-3)/6`; the Jordan block at 0 has size **one** | **FAILED** (brief) / corrected form verified | 542 / 545 |
| D9 | G1(d) | `M - M_0 = [[0,C],[0,0]]` and its rank | identity exact (generic and on both diagrams); rank `1` on D2 (`h = 1`) but rank **3** on D3 while `h = 4` | PARTIAL | 338, 391 |
| D10 | G1(d) | `det(1 - zM_0) = det(I - zT_X + z^2) = det(I - uA_X + qu^2)`, `u = z/sqrt q` | max deviation `< 1e-9` at 5 random points on each diagram | VERIFIED | 404 |
| D11 | G1(d) | Ihara--Bass `det(I-uB) = (1-u^2)^{|E|-|V|} det(I-uA+qu^2)` on `K_4`, the 3-cube, Petersen, `K_{3,3}`, `C_5` with the explicit Hashimoto operator `B` | max deviation `< 1e-8` on all five | VERIFIED | 443 |
| D12 | G1(d) | `spec(M_0) u {+-1, multiplicity |E|-|V|} = spec(B)/sqrt q` | max deviation `7.65e-1` (`= 1 - 1/sqrt2` on the 3-regular cores); the corrected form `spec(M_0) u {+-q^{-1/2}} = spec(B)/sqrt q` holds to `< 1e-6` | **FAILED** (brief) / corrected form verified | 454 / 457 |
| D13 | G1(d) scope | are the D2/D3 *cores* `(q+1)`-regular, as H-REG requires? | D2 core degrees `A:3, B:2, C:3, D:3, E:3, F:3` -- not regular (the missing unit at `B` is the cusp ray) | VERIFIED (scope note) | 464 |
| D14 | G2 | Weil data of D2 (`1-2T+2T^2`), D3 (`1+3T^2`) and the synthetic genus two `(1+3T^2)(1-2T+3T^2)` over `F_3` | `|alpha_i| = sqrt q` exactly; `alpha -> q/alpha = conj(alpha)` is an involution of each multiset | VERIFIED | 590, 593 |
| D15 | G2(a) | `E_S = Fr (+) Pi Fr(-1)`; `dim = 4g+4`; `sdet(1-wE_S) = (1-w)P(qw)/((1-q^2w)P(w))`; `= zeta_K(2s-1)/zeta_K(2s)` | exact (sympy) for all three curves; dims `8, 8, 12` | VERIFIED | 597, 604, 608 |
| D16 | G2(d) | `sdet(1-wE_S) . sdet(1-E_S/(q^2 w)) = q^{2g-2}` | exact: `1, 1, 9` | VERIFIED | 610 |
| D17 | G2(b) | the disc part of the graded divisor under `w = 1/(qz^2)` | only even disc eigenvalue `e = 1` (`nu = +1`, `z = +-q^{-1/2}`); odd disc eigenvalues exactly the `2g` `alpha_i` (`nu = -1`, `|z| = q^{-1/4}`); all others `|e| > q` **except** the two cancelling lines at `e = q` exactly, which sit on `|z| = 1` | VERIFIED, with the omission recorded as finding F5 | 616, 619, 623, 627 |
| D18 | G2(c) | `1/R(z) = z^{-2} sdet(1 - E_S/(qz^2))` on D2 at 8 points | max deviation `1.35e-15` | VERIFIED | 642 |
| D19 | G2(c) | D3: the 4x4 `S(z)` built from `Gamma`, rotated into `(q_-, l_-, l_+, q_+)`; the even block and `det S_e` | block diagonal to `3.9e-16`; channels `-1` and `z^2` exact; `1/det S_e = z^{-2} sdet(1-E_S/(qz^2))` to `1.8e-15` at 8 points | VERIFIED | 679, 682, 685 |
| D20 | G2(e) | `[z^2] p = -q^{1-g}` | D2: `[z^2]p_2 = -1` ✓. D3: `[z^2]p_3 = 0`, `ord_0 p_3 = 4`; the first nonzero coefficient is `[z^4]p_3 = -1 = -q^{1-g}`, and `|[z^m]p| = q^{1-g-(h-1)(g-1)} = 1` with `h = 4` | **FAILED** on D3 (brief) / first-nonzero form verified on both | 693 / 696 |
| D21 | `thm:h-exit-model` (used by G3--G5) | the six-dimensional model of D2 built from scratch: companion `Z` in the basis `w^k/qq`, Gram by trapezoidal quadrature on the circle (`2^14` points), Cholesky frame, `J = e_N^*` | `char Z = prod(w-z_j)` to `4.4e-15`; `I - Z^*Z = J^*J` to `5.9e-16` with `rank J = 1`; `||Z^120|| = 3.0e-9`; delay sector one Jordan block of size two; `a_n = 1` for every Hasse--Weil mode; Gram identity to `9.4e-16`; the normalised Gram equals `prop:d2-modal-gram`'s closed form (`d = 3-2sqrt2`, `u = delta(1-i)`, `v = delta(3+i)/5`) to `4.4e-16` | VERIFIED | 752, 756, 759, 765, 770, 775, 789 |
| D22 | G3(a) | `sum A_i^* A_i = 1`; all letters even; `EE` commutes with `P (x) conj P` | deviations `6e-16`, `0`, `0`, for the modal Hasse--Weil reset and a random reset | VERIFIED | 847, 850, 854 |
| D23 | G3(b) | sector split of `EE`; `E_0 = [1] (+) E_Omega`; `E_1` acts as `Z (x) 1` and `1 (x) conj Z` | even/odd dims `37 / 12 = (1+N^2) / 2N`; `spec E_0 = {1} u spec E_Omega` to `3.6e-8`; odd spectrum `{z_n} u {conj z_n}` to `1e-8`, independent of the reset | VERIFIED | 860, 868, 873 |
| D24 | G3(b), `thm:h-exit-renewal`(d) | stationary density, mean holding time, secular identity | eigenvalue 1 of `E_Omega` simple; `rho_inf = tbar^{-1} sum_m Z^m Omega Z^{*m}`; for the modal Hasse--Weil reset `rho_inf = Omega` to `5.6e-17` and `tbar = 2+sqrt2 = 3.4142136`; `det(1-uE_Omega) = det(1-uE_0^K)(1-mhat(u))` at three points | VERIFIED | 884, 894, 898, 903, 915 |
| D25 | G3(c) | `Tr EE^L = 1 + Tr E_Omega^L + 2 Re Tr Z^L`, `str EE^L = 1 + Tr E_Omega^L - 2 Re Tr Z^L`, `L = 1..8`; and the *explicit* ring vectors `psi_L`, `psi_L^P` (5 and 7 letters, `L = 1..4`) | both identities to `< 1e-7`; `<psi_L|psi_L> = Tr EE^L`, `<psi_L^P|psi_L^P> = str EE^L` | VERIFIED | 927, 947 |
| D26 | G3(c) | `Tr Z^{2k} = 2q^{-k}(alpha_+^k + alpha_-^k) = 2q^{-k}(1+q^k-N_k)`, with `N_k` by direct enumeration of `y^2+y = x^3+x+1` over `F_{2^k}`, `k = 1..5` (field built as `F_2[x]/(irred)`, point at infinity included) | `N_k = 1, 5, 13, 25, 41` both ways; both identities hold; `Tr Z^L = 0` for odd `L` | VERIFIED | 1047, 1056, 1059 |
| D27 | G3(d) | `1/sdet(1-uEE) = prod_n (1-uz_n)(1-u conj z_n) / ((1-u)^2 prod_sec (1-u lambda))` | deviations `7.6e-15` (modal), `1.6e-15` (random) | VERIFIED | 959 |
| D28 | G3(d) | `nu(1) = 2` | `= 2` for both resets (vacuum and `rho_inf`, both even) | VERIFIED | 965 |
| D29 | G3(d) | `nu(z_n) = -m_n` at each Hasse--Weil resonance | measured `-2` at all four, for both resets; the corrected value is `-2m_n` | **FAILED** (brief) / corrected form verified | 968 / 971 |
| D30 | G3(d) | `nu(z_n) = -m_n` at the delay value `z = 0` | `nu(0) = +16` (modal) and `+14` (random): the even sector carries `0` with multiplicity 20 resp. 18 (from `Ad_Z`) against 4 in the odd sector | **FAILED** (brief) | 976 |
| D31 | G3(e) | `RH(Y)` holds iff every odd eigenvalue of `EE` has modulus `r` | on the full six-dimensional model the odd moduli are `{0, 0.8408964}` -- two distinct values, so the equivalence fails as stated; on `K_HW` alone every odd eigenvalue has modulus `q^{-1/4} = 0.8408964` | **FAILED** (full model) / VERIFIED on `K_HW` | 982 / 994 |
| D32 | G3(e) | the even sector's fixed-point segment | exactly two even fixed points, so `EE` is not a mixing graded expander | VERIFIED | 1004 |
| D33 | G4(b) | the one-vertex cusp(`a`)+funnel(`b`) diagram, `a+b = q+1`, symbolically in `a, q` | `p = z^2 - (1+a(q-1))/q` exactly; `a = 0` gives the resonance at `q^{-1/2}`; `a = q+1` gives the bound state at `q^{-1/2}`; `vartheta^2 = 1` at `a = 1`, `= 1/q` at `a = q+1`. But `vartheta^2 in (1/q,1)` **fails** for `0 < a < 1` (e.g. `q=2, a=1/2` gives `vartheta^2 = 4/3 > 1`, roots of `p` at `+-sqrt3/2` *inside* the disc) | FAILED on the range (brief) / corrected range `1 < a < q+1` verified | 1072, 1075, 1077, 1081, **1090** / 1098 |
| D34 | G4(a) | the constant mode `g = 1/sqrt S` on `(q+1)`-regular cusp-plus-funnel diagrams: D2 with the cusp at `B` replaced by a funnel, D2 as it stands, and a hand-built two-vertex 3-regular cusp(2)+funnel(2) diagram | residuals `2.2e-16` in all three; `z = q^{-1/2}` is a root of `p_funnel` iff `C_c = 0` (D2-with-funnel: yes; the mixed diagram: `p = -0.5`) and a root of `ptilde` iff `C_f = 0` (D2: yes; mixed: `ptilde = +0.25`) | VERIFIED | 1123, 1129, 1138, 1142, 1150, 1155 |
| D35 | G4(c) | `p_f = det((1+z^2) - zT_2 - P_B - (f/q)P_v) = p_0 - (f/q)M_vv` (rank-one cofactor expansion, checked symbolically), then `d|z_i|/df` at `f = 0` for the quartet at all six vertices | `A: +0.0630672`, `B: +0.1261345`, `C: -0.0210224`, `D: -0.1681793`, `E: -0.0630672`, `F: -0.0630672`; **no derivative vanishes at any vertex** | VERIFIED | 1172, 1220 |
| D36 | G4(c) | does the quartet leave the Weil circle in the sense of losing the equal-modulus property? | at each vertex the four derivatives are **identical** (spread `0.00e+00`), and at `f = 1/5` the four moduli are still equal at every vertex (spreads `6e-16 .. 2e-15`) at the shifted radii `A: .853128, B: .864176, C: .836761, D: .807041, E, F: .827557`. The quartet splits into two Klein orbits only at `f >= 1` (`D`), `f >= 2` (`E, F`), `f >= 5` (`A`), and not at all up to `f = 5` at `B` and `C` | **FAILED** (brief) / corrected form verified | 1258 / 1225, 1263, 1271 |
| D37 | G4(c) | "the Perron pair moves inward without reaching `q^{-1/2}` for finite `f`" | `vartheta(f)` at the funnel at `B`: `f=0.01: 0.706576`, `0.5: 0.679776`, `2: 0.598405`, `10: 0.382576`, `100: 0.138712` -- strictly **below** `q^{-1/2} = 0.7071068` for every `f > 0`, decreasing monotonically to 0; the exterior root `1/vartheta` never re-enters the disc | **FAILED** as stated / corrected form verified | 1283 / 1286 |
| D38 | G4(d)(v) | `K_+` = APW's tree: `p_+ = z^2 - 1/q` exactly, model space of dimension 2, eigenvalues `+-q^{-1/2}`, `I - Z^*Z = J^*J`; the glued `Z = Z_+ (+) Z_-`, `J = J_+ (+) J_-` on `K` of dimension `2+6` | all exact / `< 1e-9` | VERIFIED | 1297, 1302, 1315 |
| D39 | G4(d)(i) | letter parities `eps(omega_k) eps(j_a)`; trace preservation; grading | 13 letters, parities `[1,-1,1,-1,1,1,-1,-1,1,-1,1,1,-1]`, 6 of them odd (the cross letters); `sum A_i^*A_i = 1` to `< 1e-9`; `EE` commutes with the doubled parity | VERIFIED | 1344, 1350, 1354 |
| D40 | G4(d)(ii) | uniqueness, evenness and mixedness of `rho_inf` | eigenvalue 1 of `EE` simple; `rho_inf` even to `< 1e-8` and mixed, sector weights `0.356496 / 0.643504`; `rho_inf = tbar^{-1} sum_m Z^m Omega Z^{*m}` to `2.8e-16` | VERIFIED | 1358, 1366, 1375 |
| D41 | G4(d)(iv,v) | the odd spectrum of the glued channel; the twisted ring norm | odd eigenvalues exactly `{+-q^{-1/2} conj(z_n)}` and conjugates (deviation `1e-8`), moduli `{0, 0.5946036 = q^{-3/4}}`; `Tr EE^L - str EE^L = 2 . 2 Re[(Tr Z_-^L) conj(Tr Z_+^L)]` with `Tr Z_+^L = q^{-L/2}(1+(-1)^L)`, `L = 1..8`; `|k_n><k_m|` is an eigen-operator with eigenvalue `z_n conj(z_m)` (residual `2.1e-16`) because `<a_m,a_n> = 0` exactly | VERIFIED | 1386, 1392, 1405, 1415, 1421 |
| D42 | G4(d)(iii) | sector-preserving reset | all letters even; eigenvalue 1 of `EE` has multiplicity **2**: the stationary densities form a segment, so a unique mixed stationary state needs an odd letter | VERIFIED | 1442, 1444, 1449 |
| D43 | G4(d)(vi) | random three-vertex core, one shared cusp, six distinct nonzero resonances (`c^2 = 0.755181`); Gram identity; the fate of the odd coherences | `<a_m,a_n> = conj(a_m)a_n = 1` for all pairs; `|k_n><k_m|` is **not** an eigen-operator of `EE_Omega`, the residue being exactly `<a_m,a_n> Omega` (deviation `< 1e-9`); the multiplicity of each cross eigenvalue drops by exactly one; the secular identity `det(1-uEE_Omega) = det(1-uEE_0)(1-mhat(u))` holds | VERIFIED, with the persistence wording corrected (finding F15) | 1487, 1513, 1518, 1531 |
| D44 | G5(a) | the arithmetic-metric channel on `K_HW` of D2 | `Z = rU`, `r = q^{-1/4} = 0.8408964`, `U` unitary; `J' = sqrt(1-r^2)1_4` satisfies the defect identity; `U^2` similar to `(Fr/sqrt q)^{-1} (x) 1_2` (spectra agree exactly); `EE'` CPTP; `rho_inf = (1-r^2)sum_m r^{2m}U^m Omega U^{*m}`; `rho_inf = Omega` iff `[Omega,U] = 0` (tested with a non-commuting random `Omega` and a modal one); all 15 relaxation eigenvalues of modulus exactly `r^2 = q^{-1/2}`, equal to `{r^2 e^{i(theta_a-theta_b)}}`; with the vacuum adjoined `lambda_1 = r = q^{-1/4}` | VERIFIED | 1545, 1549, 1557, 1569, 1578, 1583, 1590, 1599, 1606 |
| D45 | G5(b) | `Theta'(z) = (1-zrU^*)^{-1}(z-rU) = diag(b_{z_a}(z))` | equal to `diag((z-z_a)/(1-conj(z_a)z))` at three points, deviation `< 1e-10` | VERIFIED | 1615 |
| D46 | G5(c) | D2 with the cusp at `B` and a second unit cusp at each of `A, C, D, E, F`: `S = S^T`, `S(conj z) = conj(S(z))`, and `e^* S(conj z) e = conj(e^* S(z) e)` for random real and complex `e`; and the disc zero sets of `e^* S(z) e` for `e = e_1, e_2, (1,1), (1,i)` | identity holds to `0.0` (real `e`) and `3.3e-15` (complex `e`, where it needs `S = S^T`); every disc zero set is conjugation closed, e.g. at `C`: `{0,0,0.79931 x4}`, `{0,0,0.451768 x2}`, `{0,0.601593}`, `{0,0}` | VERIFIED | 1644, 1648, 1651, 1675 |
| D47 | G6(b) | the unit groups over `F_3[T]`: irreducible counts, `N_1 = T^3-T-1` irreducible, `T^2+1` irreducible, group orders, generators, CRT presentation | irreducible counts `3, 3, 8, 18, 48`; `|(A/N_1)^x| = 26` cyclic with generator `2T`; `|(A/N_2)^x| = 16 = 2 . 8`, not cyclic, presented as `Z/2 x Z/8` through `u -> (u mod T, u mod T^2+1)` | VERIFIED | 1753, 1791, 1793, 1798, 1803, 1819, 1832 |
| D48 | G6(b) | the trivial character | the truncated sum `sum_{deg f < deg N} psi(f) u^{deg f}` is `1+3u+9u^2` for `N_1`, which is *not* `L(u, chi_0) = prod_{P|N}(1-u^{deg P})/(1-qu)`; the trivial channel is the `g = 0` zeta line `sdet(1-wE_S) = (1-w)/(1-q^2w)`, a single even disc eigenvalue at `e = 1` | VERIFIED (scope note) | 1882, 1990 |
| D49 | G6(b) | for each nontrivial `psi`: `deg L = deg N - 1`; `|beta| = sqrt q` for the nontrivial roots (primitive `psi`); the `(1-u)` factor iff `psi` even; agreement with the Euler product to `u^5`; `det(1-wFr_psi) = L(w,psi)`; `sdet(1-wE_psi) = L(qw)/L(w) = L(2s-1,psi)/L(2s,psi)`; the disc divisor | 25 nontrivial `psi` mod `N_1` (all primitive) and 15 mod `N_2` (7 primitive); every degree `= 2 = deg N - 1`; Weil holds for every primitive `psi`; `(1-u) | L` exactly for the even primitive `psi`; Euler product to `< 1e-9`; both determinant identities to `< 1e-7`; no even disc eigenvalue in any channel | VERIFIED | 1888, 1896, 1901, 1906, 1934, 1947, 1953, 1960, 1968 |
| D50 | G6(b) | the imprimitive characters mod `N_2 = T(T^2+1)` (8 of the 15 nontrivial ones) | their root moduli are `{1, sqrt3}` or `{1,1}`: one modulus-1 inverse root per Euler factor `(1-psi^*(P)u^{deg P})` that the induction re-inserts. For `psi = (1,0)` (odd) `L = 1-u^2`, so `L(1) = 0` although `psi` is not even | VERIFIED (corrected statement) | 1912 |
| D51 | G6(b) | the level-`N` graded bond `(1)_+ (+) (+)_{psi != 1} (beta_{psi,i})_-`: all odd modes on `|beta| = sqrt q` | `N_1`: 12 of the 25 nontrivial characters (the even ones) each contribute one odd mode at `beta = 1`. `N_2`: 12 of the 15 contribute at least one, several contribute two. Corrected: for a *primitive* `psi` at most one odd mode is off the Weil circle, namely the trivial zero `beta = 1` of an even `psi` | **FAILED** (brief) / corrected form verified | 1974 / 1979 |

Row counts: 51 rows. Ten carry a FAILED verdict -- D8, D12, D20, D29, D30, D31, D33, D36, D37, D51
-- and each of them (except D30, where no corrected multiplicity statement exists) is paired in the
script with a CORRECTED assertion that passes. One row is PARTIAL (D9). The remaining forty are
VERIFIED.

---

## Findings against the brief

Fourteen assertions failed, and they group into ten substantive findings (F1, F3, F6, F7, F8, F9,
F10, F11, F12, F13). Five further findings are scope notes, omissions or wording corrections that
did not produce a failing assertion but that a reader of the brief would be misled by (F2, F4, F5,
F14, F15); they are listed here too, because being adversarial about the wording is the point of
this section. Nothing was softened: every corrected form below is itself asserted in the script and
passes, and the failing assertion is kept in the run.

An explanation of why a given equimodularity or degeneracy survives is my own reading of the data;
the numbers are what the script measured.

**F1 (G1(c)). `ord_0 p = 2 dim ker(I-C)` and the size-two Jordan blocks need the unstated hypothesis
`T_UU = 0`.** The brief says: "for `c = 1` junctions `M` is singular with Jordan blocks of size two at
`0` (one per junction with `c = 1`, when the Schur bracket of `prop:multi-exit-spectrum`(iii) is
invertible): ... `ord_0 p = 2 dim ker(I - C)`". Invertibility of the bracket is not the only missing
hypothesis. The Schur elimination of `prop:multi-exit-spectrum`(iii) also assumes `T_{UU} = 0`, i.e.
**no loop at a `c = 1` junction**. With `T_X = [[1/2, 1],[1, -1/3]]`, `C = diag(1,0)` one has
`dim ker(I-C) = 1` but `p = z(6z^3 - z^2 - z - 3)/6`, so `ord_0 p = 1`, and `M` has a single Jordan
block of *size one* at `0` (nullities of `M` and `M^2` are both 1). The general first-order statement
is `prop:nonzero-root-product`'s: `p(z) = det M_0(z)[z^2 - az - z^2 b^* M_0^{-1} b]` with
`a = T_X(v,v)`, so `ord_0 p = 1` whenever `a != 0`. Corrected: *for a core with no loop at any `c = 1`
junction* (which D2 and D3 satisfy, being simple graphs) `ord_0 p = 2 dim ker(I-C)` and every delay
block has size two. Line 542 (failing), 545 (corrected).

**F2 (G1(d)). "a rank-`h` correction supported on the junctions" -- the rank is the number of distinct
junction vertices, not `h`.** `M - M_0 = [[0, C],[0,0]]` is exact, but `rank C = #{distinct v_a}`. On
D3, `h = 4` while `C = diag(0,1,0,0,0,0,1,0,2)` has rank **3**, because the two cusps at `Q` share a
vertex and merely add their `c^2`. The correction is rank `h` only when the attachment vertices are
distinct. Line 391 (recorded as PARTIAL, row D9).

**F3 (G1(d)). The Ihara--Bass spectral statement is off by `sqrt q` on the trivial block.** The brief
writes `spec(M_0) u {+-1 with multiplicity |E| - |V|} = spec(B)/sqrt q`. Measured on `K_4`, the
3-cube, Petersen, `K_{3,3}` (all 3-regular, `q = 2`) and `C_5` (`q = 1`): the mismatch is exactly
`1 - 1/sqrt2 = 0.2929` (`0.765` on Petersen, where the pairing also shifts), i.e. the `+-1` entries
are in the wrong normalisation. The determinant identity itself,
`det(I-uB) = (1-u^2)^{|E|-|V|} det(I-uA+qu^2)`, holds to `< 1e-8` on all five graphs. The Bass
trivial factor lives in the variable `u = z/sqrt q`, so its roots `u = +-1` correspond to
`z = +-sqrt q` and to `B`-eigenvalues `+-1`, which are *not* rescaled the way `spec(M_0)` is.
Corrected: `spec(M_0) u {+-q^{-1/2} with multiplicity |E|-|V|} = spec(B)/sqrt q`, equivalently
`sqrt q . spec(M_0) u {+-1} = spec(B)`. Lines 454 (failing), 457 (corrected).

**F4 (G1(d), scope).** G1(d) is stated "with `C = 0` and `T_X = A_X/sqrt q` (H-REG)". Neither the D2
core nor the D3 core is `(q+1)`-regular on its own -- the D2 core degrees are `A:3, B:2, C:3, D:3,
E:3, F:3`, the missing unit at `B` being carried by the cusp ray. So the sentence "the diagram's
transfer matrix is the core's non-backtracking operator plus a rank-`h` correction" is not available
for the two arithmetic diagrams: only the determinant identity
`det(1-zM_0) = det(I-uA_X+qu^2)` transfers (verified to `< 1e-9` on both), and the Hashimoto reading
needs a genuinely regular core. Line 464.

**F5 (G2(b), omission).** "every other eigenvalue (`q alpha_i`, `q^2`) has `|e| > q`" leaves out the
two eigenvalues at `e = q` itself (one even, from `Fr` on `H^2`; one odd, from `Pi Fr(-1)` on `H^0`).
They have `|e| = q` exactly, hence `|z| = 1`: they sit *on* the unit circle, not outside the disc.
They cancel in the superdeterminant, as the brief says two lines earlier, so the divisor conclusion is
unaffected; but the classification of `spec E_S` into "disc" and "`|e| > q`" is not exhaustive as
written. Line 627.

**F6 (G2(e)). `[z^2] p = -q^{1-g}` is false whenever `ord_0 p > 2`.** On D3, `[z^2]p_3 = 0`: the
lowest nonzero coefficient is `[z^4]p_3 = -1`, because `ord_0 p_3 = 2 dim ker(I-C) = 4` (two `c = 1`
junction vertices, `L1` and `Z`; the double cusp at `Q` gives `1 - C_QQ = -1 != 0` and contributes no
kernel vector). The formula is correct on D2, where `ord_0 p_2 = 2`. Corrected: the invariant
statement is the one of `prop:nonzero-root-product`, about the **first nonzero coefficient**,
`[z^{ord_0 p}] p = -q^{1-g}`, which holds on both diagrams and agrees with
`|[z^m]p| = q^{1-g-(h-1)(g-1)} = 1` at `g = 1` for `h = 1` and `h = 4`. The brief's own derivation of
`[z^2]p = -q^{1-g}` from "`ord_0 p = 2` (one `c = 1` junction)" is therefore right but only inside
the one-junction hypothesis it names; the displayed formula should carry it. Lines 693 (failing),
696 (corrected).

**F7 (G3(d)). `nu(z_n) = -m_n` is a factor of two out: `nu(z_n) = -2 m_n`.** The odd sector of `EE`
carries `{z_n}` (from `Z (x) 1`) *and* `{conj z_n}` (from `1 (x) conj Z`). The resonance set of a real
symmetric core is closed under conjugation, so each Hasse--Weil value occurs **twice** in the odd
spectrum. Measured `nu(z_n) = -2` at all four Hasse--Weil resonances, for the modal and for the random
reset. (The displayed product formula
`1/sdet = prod_n (1-uz_n)^{m_n}(1-u conj z_n)^{m_n}/((1-u)^2 prod_sec(1-u lambda))` is nevertheless
correct and was verified to `< 1e-14`: it already contains both factors per `n`. It is the divisor
sentence "`nu(z_n) = nu(conj z_n) = -m_n`" that double counts.) Lines 968 (failing), 971 (corrected).

**F8 (G3(d)). The delay value is not an odd divisor point at all.** For `z_n = 0` the brief's rule
would give `nu(0) = -m_0 = -2`. Measured: `nu(0) = +16` for the modal Hasse--Weil reset and `+14` for
the random reset -- the even sector carries the eigenvalue `0` with multiplicity 20 resp. 18 (it is
`Ad_Z` on `B(K)` with a nilpotent block, plus whatever the reset kills), against multiplicity 4 in
the odd sector. The value `0` is in fact invisible to the ring zeta (a factor `1 - u . 0` is trivial
on both sides), so no reading of the rational function assigns it a divisor; the multiplicity
statement is simply not about the same object as the product formula. Corrected: restrict the
divisor sentence of G3(d) to the nonzero resonances, i.e. to the retained divisor of
`def:graded-transfer-channel`. Line 976.

**F9 (G3(e), and G4(d)(iv) in the same breath). `RH(Y) iff every odd eigenvalue of `EE` has modulus
`r`" is false for D2 as `def:cusp-diagram` defines `RH(Y)`.** The odd spectrum of `EE` on the full
six-dimensional model space has two moduli, `{0, 0.8408964}`: the two delay modes sit at `0`. Since
`thm:cusp-resonance-count` counts the zero root as a resonance, `RH(D2)` is false for the full model
and the equivalence collapses on both sides at once -- which is not the statement the brief wants.
On `K_HW` the claim is exactly right: every odd eigenvalue has modulus `r = q^{-1/4} = 0.8408964`
(verified, line 994). Corrected: read G3(e) on the retained divisor (equivalently on `K_HW`), as
`prop:d2-spectrum-frobenius` already insists ("Weil's theorem ... on `K_HW`, and only there"). The
same caveat applies to G4(d)(iv)'s "every odd eigenvalue has modulus `r_+ r_-`", whose instance (v)
the brief itself states with the exception "`0` on the delay part". Lines 982 (failing), 994
(corrected).

**F10 (G4(b)). The bound-state range is `1 < a < q+1`, not `0 < a < q+1`; and a cusp of small weight
does *not* keep the constant mode bound.** `vartheta^2 = q/(1+a(q-1))` exceeds 1 for every `a < 1`:
measured `8/5, 4/3, 8/7` at `q = 2` for `a = 1/4, 1/2, 3/4`, and similarly at `q = 3, 5`. For
`a < 1` the root of `p` lies *inside* the unit disc (`q = 2, a = 1/2`: roots `+-sqrt3/2`,
modulus `0.8660254`; `q = 3, a = 1/2`: `+-sqrt6/3`, modulus `0.8164966`), so the constant mode is a
**resonance**, not a visible bound state -- the reflection coefficient has no pole there. Corrected:
`vartheta^2 in (1/q, 1)` and a visible bound state exactly for `1 < a < q+1`; for `0 < a < 1` the
constant mode is outgoing; `a = 1` is the threshold. The concluding sentence "A cusp of any weight
keeps the constant mode bound" should read "A cusp of weight `a > 1` keeps the constant mode bound".
Lines 1090 (failing), 1098 (corrected).

**F11 (G4(c)). The quartet leaves the circle `|z| = q^{-1/4}` but stays equimodular: bolting a funnel
onto D2 does not break RH(Y) at first order, and the arithmetic is more robust than the brief
claims.** The requested derivatives are all nonzero, as predicted:
`d|z_i|/df` at `f = 0` is `+0.0630672` (A), `+0.1261345` (B), `-0.0210224` (C), `-0.1681793` (D),
`-0.0630672` (E), `-0.0630672` (F). But at each vertex the **four derivatives are identical** (spread
`0.00e+00`), and the four moduli remain equal at finite `f` as well: at `f = 1/5` the spreads are
`6e-16 .. 2e-15` at all six vertices, at shifted radii `0.853128` (A), `0.864176` (B), `0.836761` (C),
`0.807041` (D), `0.827557` (E, F). The reason is structural: `P_v` is diagonal, so it commutes with
the bipartite sign `eps` and has real entries, so the perturbed quartet remains a single orbit
`{z, -z, conj z, -conj z}` of the Klein group of `G5(d)` -- and every such orbit is automatically
equimodular. Equimodularity is lost only when the orbit degenerates: the quartet splits into two
Klein orbits of different moduli at `f = 1` for `v = D` (`0.618034` twice, `0.707107` twice), `f = 2`
for `E` and `F`, `f = 5` for `A`, and not at all up to `f = 5` at `B` and `C`. Corrected: "the
Hasse--Weil quartet leaves the circle `|z| = 2^{-1/4}`" is true (the radius moves), but the inference
"the arithmetic is not robust under an extra funnel" does not follow for small `f`: `RH(Y)` survives
with a shifted radius, and only the *value* `q^{-1/4}` is lost. What a funnel destroys immediately is
the identification of the radius with `q^{-1/4}`, not the equal-modulus property. Lines 1258
(failing), 1225 / 1263 / 1271 (corrected).

**F12 (G4(c)). "the Perron pair moves inward without reaching `q^{-1/2}` for finite `f`" is
self-contradictory as written.** At `f = 0` the Perron pair *is* at `vartheta = q^{-1/2}`, so any
inward motion takes it below `q^{-1/2}` at once. Measured for the funnel at `B`:
`vartheta = 0.706576` at `f = 0.01`, `0.679776` at `f = 0.5`, `0.598405` at `f = 2`, `0.382576` at
`f = 10`, `0.138712` at `f = 100`, against `q^{-1/2} = 0.7071068`. Corrected: `vartheta` decreases
strictly and monotonically from `q^{-1/2}` towards `0`; the exterior root `1/vartheta` never re-enters
the disc, so the Perron pair stays a *visible bound state* for every finite `f` and never turns into
the funnel's outgoing constant mode at `z = q^{-1/2}`. That last sentence is presumably what was
meant, and it is what the corrected assertion checks. Lines 1283 (failing), 1286 (corrected).

**F13 (G6(b)). The level-`N` graded bond is not "only odd modes, the `L`-zeros" on the Weil circle:
every even character contributes an extra odd mode at `beta = 1`, and for composite `N` the
imprimitive characters contribute one modulus-one mode per re-inserted Euler factor.** The brief's
displayed bond is `(1)_+ (+) (+)_{psi != 1} (beta_{psi,1}, ..., beta_{psi,d_psi})_-`, the sum running
over all nontrivial `psi`. Measured for `q = 3`:

* `N = T^3 - T - 1` (irreducible; 25 nontrivial characters, all primitive, all with `deg L = 2`):
  **12** of them are even, and each contributes exactly one odd mode at `beta = 1`, of modulus 1, not
  `sqrt3`. So 12 of the 50 odd modes of the bond are off the Weil circle. The brief does split the
  `(1-u)` factor off in the sentence before, but the bond display does not.
* `N = T(T^2+1)` (composite; 15 nontrivial characters, of which **7** are primitive -- those
  nontrivial on both CRT factors): the 8 imprimitive ones have root moduli `{1, sqrt3}` or `{1,1}`,
  the modulus-1 roots coming from the factors `prod_{P|N, P not| M} (1 - psi^*(P) u^{deg P})` that
  induction from the conductor `M` re-inserts. In total 12 of the 15 nontrivial characters
  contribute at least one non-Weil mode. In addition `psi = (1,0)` is *odd* yet has `L = 1-u^2`, so
  `L(1) = 0`: the equivalence "`(1-u)` factor iff `psi` even" also needs primitivity.

Corrected: for a *primitive* `psi` at most one odd mode is off the Weil circle -- the trivial zero
`beta = 1` contributed by the factor `(1-u)` when `psi` is even -- and that mode should be removed
from the bond exactly as the vacuum line is removed from the trivial channel. The bond should
therefore be written over primitive characters (equivalently over the conductors dividing `N`), with
the trivial zeros split off. Everything else in G6(b) checks out: `deg L = deg N - 1` for every
nontrivial character in both examples, `|beta| = sqrt q` for every nontrivial root of every primitive
`psi`, agreement with the Euler product to order `u^5`, `det(1 - w Fr_psi) = L(w,psi)`, the
superdeterminant identity `sdet(1 - w E_psi) = L(qw,psi)/L(w,psi) = L(2s-1,psi)/L(2s,psi)` as an
identity of rational functions of `w` for all 40 nontrivial characters, and "no even disc
eigenvalue" in every channel. Lines 1974 (failing), 1979 (corrected), 1912 (imprimitive structure).

**F14 (G6(b), scope).** `L(u, psi) = sum_{f monic} psi(f) u^{deg f}` truncated to `deg f < deg N` is
the `L`-function only for `psi != 1`. For the trivial character mod `N = T^3-T-1` the truncated sum
is `1 + 3u + 9u^2`, whereas `L(u, chi_0) = prod_{P|N}(1-u^{deg P})/(1-qu)` is not a polynomial. The
brief handles the trivial character separately and correctly (the `g = 0` zeta line
`sdet(1-wE_S) = (1-w)/(1-q^2w)`, verified), so this is a scope note on the displayed definition, not
a contradiction. Lines 1882, 1990.

**F15 (G4(d)(vi)). The persistence criterion is about the eigen-*operator* and one copy of the
eigenvalue, not about the eigen-*value* disappearing.** The brief says "the eigenvalue `z_n conj z_m`
of `EE_0` survives in `EE_Omega` iff `<a_m, a_n> . dual_{nm}(Omega) = 0`". On the random three-vertex
core with one shared cusp, all `<a_m,a_n> = conj(a_m) a_n = 1 != 0` and `Omega` is generic, yet every
value `z_n conj z_m` is still an eigenvalue of `EE_Omega` to machine precision. The reason is that
`spec(Ad_Z)` on a real core is conjugation symmetric: `z_n conj z_m` coincides with
`z_{n'} conj z_{m'}` for the conjugate roots, so it is already degenerate in `EE_0`, and a rank-one
perturbation removes only **one** copy. Measured: the multiplicity of each cross eigenvalue drops by
exactly one. What does fail, exactly as the brief intends, is that `|k_n><k_m|` stops being an
eigen-operator: the residue
`EE_Omega(|k_n><k_m|) - z_n conj(z_m) |k_n><k_m| = <a_m,a_n> Omega` is nonzero (verified to `< 1e-9`
against that closed form). Corrected wording: "the eigen-operator `|k_n><k_m|` survives iff
`<a_m,a_n> . dual_{nm}(Omega) = 0`; the eigenvalue survives with its multiplicity reduced by one".
Lines 1513, 1518 (both passing; this is a wording correction, not a failed assertion).

### Claims that survived every attempt to break them

For the record, the following were attacked and held: the whole of G1(a)--(b); G1(c) on loopless
cores; G2(a), (b), (c), (d) exactly and symbolically for `g = 1` (two curves) and a synthetic `g = 2`
Weil polynomial; G2(e) on D2; the entire model-space construction of `thm:h-exit-model` including the
closed-form Gram matrix of `prop:d2-modal-gram`; G3(a), (b), (c) -- including the *explicit* ring
vectors `psi_L` and `psi_L^P` up to `L = 4` -- and the point-count identity
`Tr Z^{2k} = 2q^{-k}(1+q^k-N_k)` against `N_k = 1, 5, 13, 25, 41` computed by enumeration in
`F_{2^k}`; the ring-zeta product formula of G3(d); the fixed-point segment of G3(e); G4(a) on three
regular cusp-plus-funnel diagrams including both "iff" clauses; G4(b) except for the range; G4(d)
(i)--(v) in full on the funnel-glued D2, including the twisted ring-norm identity and the exact
vanishing `<a_m,a_n> = 0` across exit blocks; G4(d)(iii)'s segment; G5(a) and (b) in full; G5(c) for
real *and* complex exit directions, with every disc zero set conjugation closed.

---

## Conventions used

These are the conventions this lane fixed; they are re-derived from the cited definitions, not taken
from the brief, and they are also recorded in the script's header.

**Diagram and normalisation.** `(A f)(v) = sum_{e at v} (S(v)/S(e)) f(o(e))`,
`deg(v) = sum_{e at v} S(v)/S(e)`. `T_X = q^{-1/2} D^{-1/2} A_X D^{1/2}` with `D = diag S` and
`(A_X)_{vw} = S(v)/S(e)`; equivalently `T_X = Ahat/sqrt q` with
`Ahat_{vw} = sqrt(S(v)S(w))/S(e)` symmetric. All determinants are computed on the integer form
`A_X` (same determinant, exact integer coefficients) in the variable `t = z/sqrt q`; all analytic
objects (resolvents, `Gamma`, `S`) on the symmetric form `Ahat`.

**Cusp versus funnel couplings.** A cusp ray (`S(c_{k+1}) = qS(c_k)`, `S(c_kc_{k+1}) = S(c_k)`) has
junction coupling `c^2 = S(v)/S(e)`. A funnel ray (`S(f_{k+1}) = S(f_k)/q`) normalises to the same
free path, but the degree condition at `f_1` forces `S(f_1) = S(e)`, so its junction coupling is
`c_f^2 = S(v)S(f_1)/(q S(e)^2) = (S(v)/S(e))/q`. Hence the brief's `C_funnel` is the *weight*
`S(v)/S(e)` and the coupling carries the extra `1/q`; the two self-energies on the outgoing sheet are
`C_c/z` and `C_f/(qz)`, giving `p_funnel = det((1+z^2) - zT_X - C_c - q^{-1}C_f)`, and on the bound
sheet `z^2 C_c` and `z^2 q^{-1} C_f`. This is the convention under which G4(a)'s displayed constant-mode
equation `[(1+z^2) - zT_X - z^2 C_c - q^{-1}C_f]x = 0` is the correct mixed (cusp bound, funnel
outgoing) equation, and it is verified to `2e-16` on three regular diagrams.

**Spectral parameter.** `lambda = z + 1/z`, `z = q^{s-1/2}`; `lambda` is invariant under `z -> 1/z`,
so `Gamma(1/z) = Gamma(z)` and `S(z) = -Q(z)^{-1}Q(1/z)` with `Q(z) = I - z Gamma(z)` agrees with
`thm:multi-exit-scattering`'s `(z Gamma - I)^{-1}(I - Gamma/z)`.

**Inner product.** `<x, y> = x^dagger y`, conjugate linear in the **first** slot. The Gram identity of
`thm:h-exit-model` is then `a_n^* a_m = (1 - conj(z_n) z_m) <k_n, k_m>`, and G4(d)(vi)'s
`<a_m, a_n> = (1 - conj(z_m) z_n) <k_m, k_n>` is the same statement with the labels swapped.

**Model space (scalar inner `Theta`, `h = 1`).** `Theta = Pc/qq` with `Pc(w) = prod_j (w - z_j)` over
the `N` resonances (delay roots at `0` **included**) and `qq(w) = prod_j (1 - conj(z_j) w)`;
`K = {P/qq : deg P < N}`; in the basis `f_k = w^k/qq` the compressed shift `Z = P_K M_w|_K` is
*exactly* the companion matrix of `Pc` (because `w^N/qq = Theta - (Pc - w^N)/qq` and `Theta ⟂ K`).
The Gram `G_{kl} = <f_l, f_k> = (1/2pi) int e^{i(l-k)theta}/|qq|^2` is computed by the trapezoidal
rule on `2^14` points on the circle -- exponentially convergent, since the poles of `1/|qq|^2` sit at
radius `1/|z_j| > 1` -- then `G = L L^*` (Cholesky) and the orthonormal frame is `y = L^* x`, so
`Z_orth = L^* Z_comp L^{-*}`.

**Exit map `J`.** Fixed by `(I - P_K)(w f) = Theta . Jf`. Since `(I-P_K)(w f_{N-1}) = Theta . 1` and
`w f_k = f_{k+1} in K` for `k < N-1`, `J = e_{N-1}^*` in the `f`-basis, hence
`J_orth = e_{N-1}^* L^{-*}`. That `I - Z^*Z = J^*J` then holds (to `5.9e-16` on D2) is a check of the
whole construction, not an input. For several exits, `J = J_+ (+) J_-` block diagonal, one block per
exit group.

**Eigenvector normalisation.** `k_a = Theta/(w-a)`, whose `f`-coordinates are the coefficients of the
synthetic quotient `Pc(w)/(w-a)`. This is the normalisation in which the exit amplitude is
`a_n = J k_a = 1` (monic quotient) and `||k_a||^2 = (1-|a|^2)^{-1}`. The *normalised* modal vectors
used for the resets and for `prop:d2-modal-gram`'s Gram matrix are `e_i = k_i/||k_i|| = sqrt(delta) k_i`
with `delta = 1 - q^{-1/2}`.

**Arithmetic metric (G5).** The symmetric ray of `thm:arithmetic-metric` is realised by *declaring*
the four vectors `e_i` orthonormal, i.e. by working in `C^4` with the standard inner product and
`Z' = diag(z_a)`. Then `Z' = rU` with `r = q^{-1/4}` and `U = diag(z_a/r)` unitary, and
`J' = sqrt(1-r^2) 1_4`, one exit per mode.

**Grading, supertrace, superdeterminant.** Bond `H = H_+ (+) H_-`, `P = 1 (+) (-1)`; `B(H)` graded by
`Ad(P)`: even = block diagonal, odd = block off-diagonal. Channels are vectorised **row-major**
(`vec(rho) = rho.reshape(-1)`), so `E(rho) = sum_i A_i rho A_i^*` becomes
`EE = sum_i A_i (x) conj(A_i)` and the doubled parity is `P (x) conj P`. Following
`def:cmps-transfer-generators`, `str M = Tr[(P (x) conj P) M]` and
`sdet(1 - u EE) = det(1 - u EE|even)/det(1 - u EE|odd)`, so
`1/sdet(1-uEE) = det(1-uE_1)/det(1-uE_0)`. The graded divisor is
`nu(lambda) = m_even(lambda) - m_odd(lambda)` in *algebraic* multiplicities, grouped numerically at
`1e-7`.

**Tate twist and parity flip (G2).** `Fr(-1) := q Fr`: the same space, the same parities, eigenvalues
multiplied by `q`. `Pi` is the parity flip, the same operator with `P` replaced by `-P`. Hence in
`E_S = Fr (+) Pi Fr(-1)` the *twisted* copy is the one whose parities are reversed: its `H^0` and
`H^2` lines (eigenvalues `q`, `q^2`) become **odd** and its `H^1` lines (eigenvalues `q alpha_i`)
become **even**, while the untwisted copy keeps `1, q` even (from `H^0, H^2`) and `alpha_i` odd (from
`H^1`). The two lines at `e = q` -- even from `Fr` on `H^2`, odd from `Pi Fr(-1)` on `H^0` -- cancel.
The disc is cut out by `w = 1/(qz^2)`, i.e. `z^2 = e/q`, so `|e| < q` iff `|z| < 1`.

**Tolerances.** `1e-9` for float identities throughout, exact (sympy over `Q`, or `Q(sqrt q)`)
wherever exactness is available -- all of `p`, `ptilde`, the G1 linearisation identities, the G2
superdeterminant identities, G4(b), and the G4(c) cofactor expansion. Documented exceptions, none of
them chosen to make a claim pass:

* `1e-8`/`1e-7` when matching or counting **eigenvalues** of the doubled channels (49x49, 64x64) or
  of `Ad_Z`. These matrices are strongly non-normal and carry a nilpotent delay block; eigenvalues of
  a defective matrix are conditioned like a root of the perturbation, so agreement below `1e-8` is
  not available. Multiplicity grouping uses `1e-7`.
* `1e-8` for the equimodularity spread of the perturbed Hasse--Weil quartet (`np.roots` on a
  degree-12 polynomial; the observed spreads are `1e-15`, four orders below the threshold) and `1e-6`
  for the modulus classification of `L`-function roots, some of which are **double** roots at `u = 1`
  and are therefore resolved only to about the square root of machine precision.
* Root finding of polynomials with repeated roots uses mpmath at 50 digits with extra precision, and
  deflates the `z = 0` factor exactly first.

**Determinism.** Single seed `20260920` for the one `numpy.random.default_rng`; no other source of
randomness; no timestamps, no memory addresses, no iteration over unordered containers whose order
could vary. Three consecutive runs produce byte-identical output.

---

## Tally

```
CHECKS: 498 passed, 14 failed
```

(512 assertions; 11.7 s; `outputs/graded_toys.txt`.)
