# H-THETA: blind numerics ledger

author: `claude:opus` (numerics lane)
date: 2026-09-21
brief: `notes/h-theta/astra-brief.md` (read in full; Section 1 conventions and the shards it names)
script: `scripts/h_theta.py` (mpmath at 25 digits, deterministic, seed 20260921, 69 s wall)
output: `outputs/h_theta.txt`
tally: **98 checks, 98 passed, 0 failed**

This lane is blind: it did not read `notes/h-theta/astra-proofs.md`, `astra-last.md` or
`astra.stdout`. Every claim below was tested against the brief's own displayed formulas.
"Assertion line" is the line of the `check(...)` call in `scripts/h_theta.py`; "check" is the
`ok NN` number in `outputs/h_theta.txt`.

---

## Ledger

| id | claim tested (brief item) | what was computed | result | verdict | check / line |
|----|---------------------------|-------------------|--------|---------|--------------|
| D01 | `theta(y) = sum_n e^{-pi n^2 y}` equals `jtheta(3,0,e^{-pi y})` | direct sum vs `mp.jtheta` at `y = 1, 1.5, 2.7, 5, 11` | agree to `1e-22` | VERIFIED | 01 / L265 |
| D02 | `theta(y)` for `y<1` via the functional equation | `y^{-1/2} jtheta(3,0,e^{-pi/y})` vs the cancellation-free form, `y = 0.05 … 0.95` | agree to `1e-20` rel | VERIFIED | 02 / L270 |
| D03 | Jacobi `theta(1/y) = y^{1/2} theta(y)` (Section 1) | 6 values `y in [0.05, 9]` | agree to `1e-21` rel | VERIFIED | 03 / L276 |
| D04 | Mellin convention `fhat(tau) = int f(y) y^{i tau} d^x y` (Section 1) | quadrature vs closed form for `f = 1_{y>1} y^{-1/2-1.3i}`, at `tau = 2, 2+3i, -1.5+0.4i`; `fhat = 1/(1/2 - i(tau-1.3))` | agree to `1e-16` rel | VERIFIED | 04 / L308 |
| D05 | **the outgoing half is `y > 1` ↔ `H^2(C_+)`** (Section 1, "check this sign convention first") | the only pole of `fhat` for that `f` sits at `tau = 1.3 - i/2 in C_-`; `\|fhat(2+3i)\| = 0.28016591` (bounded in `C_+`), `\|fhat(1.3-0.49i)\| = 100.0` (blows up at the `C_-` pole) | the brief's convention is **correct as printed**; no change needed | VERIFIED | 05, 06 / L309, L314 |
| D06 | `(U_t f)^hat = e^{i t tau} fhat` for `(U_t f)(y) = f(e^{-t}y)` | quadrature at `t = 0.7, -0.4`, `tau = 2` and `1.1+2i` | agree to `1e-15` rel | VERIFIED | 07 / L337 |
| D07 | `U_t`, `t >= 0`, maps `L^2(1,inf)` into itself (forward = outgoing) | `supp U_t f = {y > e^t}` at `t = 0.7` | exact | VERIFIED | 08 / L338 |
| D08 | `(Jf)^hat(tau) = fhat(-tau)` for `(Jf)(y)=f(1/y)` | quadrature at `tau = 2, 0.8-0.3i` | agree to `1e-15` rel | VERIFIED | 09 / L357 |
| D09 | **T1(a)** `phi(1/y) = y^{1/2} phi(y)` exactly | 8 values `y in [0.02, 30]` | max rel err `1.57e-26` | VERIFIED | 10 / L373 |
| D10 | **T1(b)** `phi(y) = -1 + O(y^{-1/2} e^{-pi/y})` as `y -> 0` | ratio `(phi+1)/(2 y^{-1/2}e^{-pi/y})` at `y = 0.2, 0.1, 0.05, 0.02` | `1.0, 1.0, 1.0, 1.0` (to 16 digits) — the constant is exactly `2` | VERIFIED | 11, 12 / L383, L384 |
| D11 | **T1(b)** `phi(y) = -y^{-1/2} + O(e^{-pi y})` as `y -> inf` | ratio `(phi+y^{-1/2})/(2e^{-pi y})` at `y = 2,3,5,9` | `1.0000000065, 1.0000000000005, 1.0, 1.0` — constant exactly `2` | VERIFIED | 13 / L394 |
| D12 | **T1(b)** `J(y^a phi) = y^a phi` iff `a = 1/4` | defect `max_y \|(1/y)^a phi(1/y) - y^a phi(y)\|` for `a = 0, 0.1, 0.2, 0.3, 0.4, 0.5` vs `a = 1/4` | `1.29e-26` at `a = 1/4`; `0.326` at `a = 0.1` and `0.4`; all other `a` `> 1e-3` | VERIFIED | 14, 15 / L406, L413 |
| D13 | **T1(b)** `y^a phi in L^2(d^x y)` for `0 < a < 1/2` | `\|\|y^a phi\|\|^2` at `a = 0.1, 0.25, 0.4` | `6.164658343267941`, `3.914969408269076`, `6.164658343267941` (finite) | VERIFIED | 16 / L443 |
| D14 | (extra, not in the brief) `\|\|y^a phi\|\| = \|\|y^{1/2-a} phi\|\|` | `a = 0.1` vs `0.4`, `a = 0.15` vs `0.35` | equal to `1e-15` | VERIFIED | 17 / L444 |
| D15 | **T1(b)** divergence at `a = 0` and `a = 1/2` | truncated `int_{-X}^{X} e^{2ax} phi(e^x)^2 dx` for `X = 10,20,40,80`: `10.914, 20.914, 40.914, 80.914` in both cases | increments are exactly `10, 20, 40` (linear in `X = log`-range): log-divergent in `y`, i.e. **not** `L^2` | VERIFIED | 18, 19 / L462, L464 |
| D16 | **T1(b)** control at `a = 1/4` | same truncation: `3.888, 3.91479, 3.9149694, 3.914969408` | increment `X=40->80` is `8.2e-9`: convergent. `\|\|g\|\|^2 = 3.91496940826907585` | VERIFIED | 20 / L466 |
| D17 | **T2(a)** `ghat(tau) = int_0^inf y^{1/4} phi(y) y^{i tau} d^x y = Lambda(1/2+2i tau)` | raw `x = log y` quadrature with exact elementary tails, at `tau = 0, 0.7, 2.3, 7.1`, vs `2 pi^{-s/2}Gamma(s/2)zeta(s)`. Values `-7.953932451013`, `-0.85986663760725`, `-0.05646122659521`, `1.7215935066028e-6` | rel err `< 3.1e-26` (`1.2e-23` at `tau=7.1`) | VERIFIED | 21 / L486 |
| D18 | **T2(a)** `= -xi_crit(tau)/(tau^2+1/16) = -xi_crit/((tau-i/4)(tau+i/4))` | same four `tau` | agree to `1e-20` rel | VERIFIED | 22 / L494 |
| D19 | **T2(a)** `ghat(0) = Lambda(1/2) = -16 xi(1/2)` | `ghat(0) = -7.95393245101302576`; `xi(1/2) = 0.49712077818831411` | identical to 18 digits | VERIFIED | 23 / L501 |
| D20 | **T2(a)** `ghat` real on `R`, even | `tau = 0.3, 1.7, 5.5, 12` | `\|Im\| < 1e-20`, `ghat(tau)=ghat(-tau)` | VERIFIED | 24, 25 / L504, L506 |
| D21 | **T2(a)** simple poles at `tau = ±i/4`, residues `±i` — *which is which* | closed form and `eps*ghat(±i/4+eps)`, `eps = 1e-12` | **`Res_{tau=+i/4} ghat = +i`** (that is `s = 0`, where `Lambda` has residue `-2`); **`Res_{tau=-i/4} ghat = -i`** (that is `s = 1`, residue `+2`); `ds/dtau = 2i` | VERIFIED | 26, 27, 28, 29 / L517, L519, L523, L525 |
| D22 | **T2(a)** zeros of `ghat` on `R` at `gamma_n/2` | `\|ghat(gamma_n/2)\|` for `n=1,2,3` | `1.78e-30`, `3.18e-32`, `1.30e-33` | VERIFIED | 30 / L537 |
| D23 | **T2(a)** `\|ghat(u)\| ~ e^{-pi\|u\|/2}` | least squares of `log\|ghat(u)\|` vs `u`, 386 points on `[5,40]` (zeros excluded) | slope `-1.58261886` vs `-pi/2 = -1.57079633`; on `[40,100]` (370 points) slope `-1.57295904` (`2.2e-3` off) | VERIFIED | 31, 33 / L555, L571 |
| D24 | **T2(a)** the exponent `c` in `\|ghat(u)\| ~ C\|u\|^c e^{-pi\|u\|/2}` | (i) naive log-log fit of `log\|ghat\|+(pi/2)u` vs `log u`; (ii) the exact Stirling ratio `\|ghat(u)\| / (2 pi^{-1/4}sqrt(2pi) u^{-1/4} e^{-pi u/2}\|zeta(1/2+2iu)\|)` at `u = 40, 70, 100` | (i) gives `c = -0.2057` on `[5,40]` and `c = -0.1416` on `[40,100]` — contaminated by `log\|zeta\|`; (ii) gives `1.0000048833`, `1.0000015944`, `1.0000007813`. **`c = -1/4`, but only with `\|zeta(1/2+2iu)\|` retained** | VERIFIED (see finding F5) | 32, 34 / L557, L585 |
| D25 | **T2(b)** `Lambda_>(s) = 2/(s-1) + 2 sum_{n>=1}(pi n^2)^{-s/2}Gamma(s/2,pi n^2)` | vs direct quadrature `int_1^inf phi y^{s/2} d^x y` at `s = 0.3, 0.5+3i, 0.8+10i, -0.4+2i` | agree to `1e-17` rel | VERIFIED | 35 / L597 |
| D26 | **T2(b)** `Lambda_<(s) = Lambda_>(1-s)` | direct `int_0^1` quadrature vs `Lambda_>(1-s)` at `s = 0.3, 0.5+3i, 0.8+10i`. Values `-6.64311085701`, `-0.0871708556 + 0.6415164769i`, `-0.0066157031 + 0.1865826382i` | rel err `<= 2.5e-27` | VERIFIED | 36 / L608 |
| D27 | **T2(b)** `Lambda_> + Lambda_< = Lambda` in the strip | same three `s` | agree to `1e-18` rel | VERIFIED | 37 / L615 |
| D28 | **T2(b)** `Lambda_>(s) - 2/(s-1)` smooth across `s=1` | values `0.0243500874778931745` (`s=0.99`), `0.0243782995343042833` (`s=1`), `0.0244065679799713583` (`s=1.01`); 2nd difference `5.64e-8` at `h=0.01` (`h^2 = 1e-4`); the entire part at `s=1` equals `int_1^inf(theta-1)y^{1/2}d^x y = 0.02437829953430428` | smooth, `C^2`-consistent | VERIFIED | 38 / L628 |
| D29 | **T2(b)** `Lambda_<(s) + 2/s` smooth across `s=0` | values `0.0244065679799713583`, `0.0243782995343042833`, `0.0243500874778931745` at `s = -0.01, 0, 0.01`; 2nd difference `5.64e-8` | smooth (it is the mirror of D28, as it must be) | VERIFIED | 39 / L641 |
| D30 | **T2(b)** `\|ghat_>(u)\|` decays like `1/\|u\|`, not exponentially | `\|u\|\|ghat_>(u)\|` at `u = 5,10,20,40`: `0.934736274877`, `0.917693817961`, `0.914552515192`, `0.913809501842`; predicted limit `2 - theta(1) = 0.913565188787`. At `u=40`: `\|ghat_>\| = 0.0228452` vs `\|ghat\| = 1.52e-27` | 1/u confirmed, and the **constant is `2 - theta(1) = 0.9135651888`** | VERIFIED (sharpened, F7) | 40, 45 / L653, L672 |
| D31 | **T2(b)** pole structure of the halves | `Res_{tau=-i/4} ghat_> = -i` (num `2.4e-14 - 1.0i`), `ghat_>(+i/4) = -1.978186882` finite; `Res_{tau=+i/4} ghat_< = +i`, `ghat_<(-i/4) = -1.978186882` finite | `ghat_>` analytic in `Im tau > -1/4` with its only pole at `-i/4` (the `s=1` pole); `ghat_<` carries `+i/4`. Exactly as the brief states | VERIFIED | 41, 42 / L661, L663 |
| D32 | **T2(b)** `ghat = ghat_> + ghat_<`, `ghat_<(tau) = ghat_>(-tau)` | `tau = 0.3, 1.7, 5.5, 13` | agree to `1e-18` | VERIFIED | 43, 44 / L668, L671 |
| D33 | **T3(c)** `Lambda_>(rho_n)` purely imaginary and **non-zero** | `n=1,2,3`: `-1.01e-28 - 0.13055641672683i`, `0 - 0.087268473867639i`, `-2.52e-29 - 0.07326004624429i`; `\|Re\|/\|Im\| < 8e-28` | purely imaginary; moduli `0.1306, 0.0873, 0.0733` — far from zero | VERIFIED | 46, 47 / L688, L689 |
| D34 | **T3(c)** `Lambda_>(1-rho_n) != 0`, and `Lambda(1/2+it) = 2 Re Lambda_<(1/2+it)` | same three zeros | `\|Lambda_>(1-rho_n)\| > 0.01`; the `2 Re` identity holds to `1e-18` | VERIFIED — the zeros of `zeta` are **not** zeros of the half-transform | 48, 49 / L690, L695 |
| D35 | **T2(c)** `Theta(tau) = [Lambda(1+2i tau)/Lambda(2i tau)](tau-i/2)/(tau+i/2)` | `tau = 0.3, 1.9, 5.5, 12`. `Theta(0.3) = 0.9996155238 + 0.02772732578i`, `Theta(12) = 0.2419505219 + 0.9702885885i` | agree to `1e-18` | VERIFIED | 50 / L711 |
| D36 | **T2(c)** `= [ghat(tau-i/4)/ghat(tau+i/4)](tau-i/2)/(tau+i/2)` | same four `tau` | agree to `1e-18` | VERIFIED | 51 / L712 |
| D37 | **T2(c)** `xi(1+2i tau) = xi_crit(tau-i/4)`, `xi(1-2i tau) = xi_crit(tau+i/4)` | `tau = 0.3, 1.9, 5.5, 2+i` | agree to `1e-20` | VERIFIED | 52 / L719 |
| D38 | **T2(c)** the two edge lines are where the Mellin integral of `phi` diverges | truncated `int_1^{e^X} y^{1/2}phi d^x y` and `int_{e^{-X}}^1 phi d^x y` for `X = 10,20,40` | both grow linearly in `X` with slope `∓1`: the `Re s = 1` integral (numerator, `y^{1/2}phi`) diverges **at the outgoing end `y -> inf`**; the `Re s = 0` integral (denominator, `phi`) diverges **at the incoming end `y -> 0`** | VERIFIED (sharpened, F11) | 53, 54, 55 / L735, L736, L739 |
| D39 | **T2(c)** `\|Theta(tau)\| = 1` on `R` | `tau = 0.3, 1.9, 5.5, 12, 30` | `\|\|Theta\|-1\| < 1e-20` | VERIFIED | 56 / L746 |
| D40 | **T2(c)** `\|Theta\| < 1` in `C_+`, `> 1` in `C_-` | 4x5 grid, `Re tau in {0.3, 2, 7, 15}`, `Im tau in {0.05, 0.2, 0.5, 1, 3}`. e.g. `\|Theta(0.3+0.05i)\| = 0.9953836`, `\|Theta(0.3+3i)\| = 0.768456735`; conjugates `1.00463781`, `1.301309435` | all 20 points `< 1` in `C_+` and `> 1` in `C_-` | VERIFIED | 57, 58 / L759, L760 |
| D41 | **T2(c)** zeros of `Theta` in `C_+` at `w_n = gamma_n/2 + i/4` | `\|Theta(w_n)\|` for `n=1,2,3` at `w = 7.06736257087+0.25i`, `10.5110198194+0.25i`, `12.5054287901+0.25i` | `6.2e-26`, `1.9e-25`, `1.5e-25` | VERIFIED | 59 / L769 |
| D42 | **T2(c)** Hermite–Biehler for `E(tau) = xi(1-2i tau)` | `\|E(tau)\| > \|E(conj tau)\|` on the same 20-point `C_+` grid | holds at all 20 points (equivalent to D40 by `\|E(conj tau)\| = \|xi(1+2i tau)\|`) | VERIFIED | 60 / L775 |
| D43 | **T2(c)** `E(tau) = xi(1-2i tau) = xi(2i tau)` | 6 grid points | agree to `1e-20` rel | VERIFIED | 61 / L778 |
| D44 | **T3** `I_full(T) = int_{-T}^{T} log\|ghat(u)\| du/(1+u^2)` grows without bound | `T = 10, 20, 40`: `-3.90630330835`, `-6.01620982282`, `-8.16899533084`; increments `-2.1099065`, `-2.1527855` | increments do **not** decay (ratio `1.0203`) and match `-pi log 2 = -2.1775861`: log-divergent. So `log\|ghat\| not in L^1(du/(1+u^2))` | VERIFIED | 62, 63 / L808, L811 |
| D45 | **T3** `I_half(T) = int log\|ghat_>(u)\| du/(1+u^2)` converges | `T = 10, 20, 40`: `-0.0990607443471`, `-0.367265602075`, `-0.536641849581`; increments `-0.2682049`, `-0.1693762` | increments decay by `1.58x` per doubling (consistent with the `log u / T` tail of a `1/u` decay): `log\|ghat_>\| in L^1(du/(1+u^2))` | VERIFIED | 64 / L826 |
| D46 | **T3** the contrast | ratio of increments at `20->40` | `12.71` | VERIFIED | 65 / L829 |
| D47 | **T4** Nyman step form `rho_alpha(1/t) = alpha floor(t) - floor(alpha t)` | `alpha = 0.5, 0.3, 0.77` x 7 values of `t` | exact to `1e-20` | VERIFIED | 66 / L858 |
| D48 | **T4** `int_0^1 rho_alpha(u)u^{s-1}du = (alpha - alpha^s)zeta(s)/s` | exact Hurwitz-zeta evaluation of the Mellin integral (period-`q` step function) for `alpha = 1/2, 3/10, 2/7` at `s = 2, 3+i, 0.7+5i`. e.g. `alpha=3/10, s=0.7+5i`: `-0.0223731255839 + 0.00898503163964i` | all 9 agree to `<= 2.9e-25` rel | VERIFIED | 67 / L921 |
| D49 | **T4** same, by independent truncated quadrature | exact piecewise integration of `int_1^{4000} R(t)t^{-s-1}dt` + mean tail, `alpha = 0.3`, `s = 2` and `3+i` | rel err `2.3e-11` and `9.6e-15` | VERIFIED | 68 / L931 |
| D50 | **T4** Balazard–Saias–Yor: `(1/2pi) int_{Re s=1/2} log\|zeta(s)\|/\|s\|^2 \|ds\| ~ 0` | `\|Im s\| <= T` for `T = 50, 100, 200`, breakpoints at the first 80 zeros | `-1.16067886e-4` (T=50), `+3.53484565e-6` (T=100), `+4.98326306e-6` (T=200); increments `1.20e-4`, `1.45e-6`; crude tail scale `2/(pi T) = 1.27e-2, 6.4e-3, 3.2e-3` | VERIFIED: consistent with `0` (the empty bad-zero sum), well inside the tail estimate | 69, 70, 71 / L956, L958, L961 |
| D51 | **T4(d)** `C(t) = (1/2pi)int\|ghat\|^2 e^{i t tau}d tau = int g(e^{-t}y)g(y)d^x y` | both integrals at `t = 0,1,2,4` | agree to `4.2e-14` (limited by the spectral quadrature) | VERIFIED | 72 / L1001 |
| D52 | **T4(d)** `C(0) = \|\|g\|\|^2` | `C(0) = 3.914969408269039`; `\|\|g\|\|^2 = 3.914969408269076` (D16) | agree to `3.7e-14` | VERIFIED | 73 / L1002 |
| D53 | **T4(d)** `C` real and even | `\|Im C(t)\| < 2e-33`; `C(-1) = C(1)`, `C(-2) = C(2)` to `1e-16` | VERIFIED. Values: **`C(0) = 3.914969408269`, `C(1) = 3.822181438389`, `C(2) = 3.583151087755`, `C(4) = 2.909049783340`** | VERIFIED | 74, 75 / L1005, L1006 |
| D54 | **T4(d)** the spectral density `\|ghat\|^2/2pi` vanishes at the on-line zeros | `\|ghat(gamma_n/2)\| < 1.8e-30` for `n=1,2,3` (double zeros of `\|ghat\|^2`) | VERIFIED | 76 / L1013 |
| D55 | **T5(a)** `int_0^1 Theta_z(t)dx = theta(t/y) + sqrt(y/t)(theta(ty)-1)` | truncated double sum (rel tol `1e-30`) integrated over `x in [0,1]`, at `(t,y) = (0.8,1.3), (2.0,0.6), (0.5,3.0)`. Values `1.387389062823723`, `1.025311460580111`, `2.493498765016911` | rel err `<= 1.9e-26` | VERIFIED | 77 / L1053 |
| D56 | **T5(a)** the brief's `sqrt(y/t) theta(ty) = y theta(1/(ty))` | at the three `(t,y)`: `sqrt(y/t)theta(ty) = 1.3719242310449, 0.57297737996699, 2.4934987331127`; `t^{-1}theta(1/(ty)) =` the same; `y theta(1/(ty)) = 1.4268012002867, 0.68757285596038, 3.7402480996691` | **FAILED as printed.** Correct identity: `sqrt(y/t) theta(ty) = t^{-1} theta(1/(ty))` (agrees to `1e-20`). The brief's version holds only on `t y = 1` | FAILED (finding F1) | 78, 79, 80 / L1069, L1070, L1071 |
| D57 | **T5(a)** the brief's involution `t -> 1/(y^2 t)` | `G(t) := theta(t/y)-1+sqrt(y/t)(theta(ty)-1)`; `G(1/(y^2 t))` vs `G(t)` at the three `(t,y)`: `0.46566124803458` vs `0.13738906282372`, `0.097320414484476` vs `0.52531146058011`, `3.5808496778019` vs `0.49349876501691` | **FAILED.** `t -> 1/(y^2 t)` is not a symmetry and does not exchange the channel arguments | FAILED (finding F2) | 82 / L1100 |
| D58 | **T5(a)** the correct involution | `t^{-1}G(1/t)` vs `G(t)+1-1/t`: `0.13738906282372`, `0.52531146058011`, `0.49349876501691` — identical to `1e-20` rel | **`t -> 1/t` with weight `t^{-1}` is the involution**; it sends `t/y -> 1/(ty)` (the Poisson partner of `ty`) and `ty -> y/t` (partner of `t/y`), both verified to `1e-20` | VERIFIED (correction) | 81, 83 / L1099, L1106 |
| D59 | **T5(b)** `int_0^inf (theta(t/y)-1)t^s d^x t = y^s Lambda(2s)` | raw quadrature with exact small-`t` tail, `s = 1.2+0.5i`, `y = 1` and `2.5`. Values `0.28321836791481 - 0.37787158227281i`, `1.2645990562514 - 0.64152038406035i` | rel err `<= 2.9e-24` | VERIFIED | 84 / L1146 |
| D60 | **T5(b)** `int_0^inf sqrt(y/t)(theta(ty)-1)t^s d^x t = y^{1-s}Lambda(2s-1)` | same, `s = 1.2+0.5i`. Values `-0.2103278563733 - 1.0475742706893i`, `-0.54279518334497 - 0.70477085872049i` | rel err `<= 5.6e-25` | VERIFIED | 85 / L1156 |
| D61 | **T5(b)** regions of convergence (the brief says "state the regions you found numerically") | truncated `int_{e^{-X}}^{inf}` at `X = 10,20,40,80,160`, `y = 2.5`. Channel 1 at `s=1.2+0.5i`: `1.4173, 1.41801, 1.4180124, 1.4180124, 1.4180124` (converged). Channel 2 at `s=1.2+0.5i`: `1.0749, 0.9201, 0.88895, 0.8895664, 0.8895665` (converged) | **channel 1 converges exactly for `Re s > 1/2`; channel 2 exactly for `Re s > 1`** | VERIFIED | 86, 88 / L1186, L1193 |
| D62 | **T5(b)** the brief's evaluation point `s = 0.3+0.5i` | channel 1 truncations at `s=0.3+0.5i`: `22.29, 162.34, 8750.7, 2.609e7, 2.318e14`; ratio `X=80->160` is `8.886e6 = e^{80*0.2}`. Channel 2: `1258, 1.398e6, 1.681e12, 2.432e24, 5.086e48`; ratio `2.0917e24 = e^{80*0.7}` | **`s = 0.3+0.5i` is outside BOTH regions.** Both integrals diverge there, at exactly the predicted rates `e^{X(1/2-Re s)}` and `e^{X(1-Re s)}`; the identities hold there only by continuation | FAILED (finding F3) | 87, 89 / L1188, L1195 |
| D63 | **T5(b)** the Lax–Phillips coefficient `phi(1/2+i tau) = Lambda(2i tau)/Lambda(1+2i tau) = Theta(tau)^{-1}(tau-i/2)/(tau+i/2)` | `tau = 0.3, 1.9, 5.5` | agree to `1e-18` rel | VERIFIED | 90 / L1211 |
| D64 | **T6(a)** `m_n(y) = y^{-(1-sigma)/2 - i gamma/2}1_{y>1}` has Mellin transform proportional to `k_{w_n}` | raw quadrature with exact tail at `tau = 0.5` and `9.0`, for `n = 1,2,3` (under RH, `sigma = 1/2`). At `n=1, tau=0.5`: `0.00578800825179 - 0.152047795011i` | equals `i/(tau - conj w_n)` to `1e-14` rel. **The constant is exactly `i`** with `k_w(tau)=1/(tau-conj w)` (04h, line 33) | VERIFIED | 91 / L1244 |
| D65 | **T6(a)** `<mhat_n, Theta h> = 0` for `h = 1/(tau+i)^k`, `k=1,2` | composite 24-node Gauss–Legendre, 120 subintervals of `[-60,60]` (2880 nodes). `k=1`: `5.71e-4, 5.77e-4, 5.81e-4` for `n=1,2,3` (tail bound `5.31e-3`); `k=2`: `5.77e-6, 5.85e-6, 5.91e-6` (tail bound `4.42e-5`). On `[-20,20]` the values are `~3e-3` and `~1e-4`, i.e. they shrink like the truncation bound `1/(pi k T^k)` | VERIFIED (quadrature-limited): the truncated values are an order of magnitude below the tail bound and scale as `T^{-k}` | 92 / L1277 |
| D66 | **T6(a)** the exact reason (contour argument) | closing in `C_-`, the only pole is `conj w_n` and the pairing equals `conj[Theta(w_n)h(w_n)]`, i.e. `1/Theta(conj w_n) = xi(1/2 - i gamma_n)/xi(3/2 + i gamma_n)`. Computed: numerators `8.92e-29, 3.52e-30, 2.04e-31`; denominators `1.43e-3, 1.90e-5, 1.37e-6` | the pairing is exactly `0` | VERIFIED | 93 / L1289 |
| D67 | **T6(b)** Gram matrix of normalised Cauchy kernels at `w_n = gamma_n/2 + i/4` | with `<k_w,k_v> = i/(v - conj w)` (fixing the notebook's convention, 04h line 90), `<k_w,k_w> = 1/(2 Im w) = 2`, so `G_{nm} = i/(gamma_m - gamma_n + i)`, `G_{nn}=1` | verified; `G` Hermitian and positive definite for `N = 10,20,30` | VERIFIED | 94, 95, 96 / L1314, L1315, L1323 |
| D68 | **T6(b)** Riesz-basis signal | `N=10`: `lambda_min = 3.99597060e-01`, `lambda_max = 1.86641948`, `cond = 4.670754`. `N=20`: `2.70419603e-01`, `2.27824367`, `8.424847`. `N=30`: `2.01340242e-01`, `2.56015448`, `12.71556`. Smallest three at `N=30`: `0.2013402, 0.2370691, 0.2711725` | `lambda_min` decreases monotonically, `cond` grows; the trend is the numerical signal, **but see finding F10: at `N=30` (`gamma <= 101.3`) the mean gap is `2.50` against a height `1/4`, so this is far from the regime where Carleson can fail** | PARTIAL | 97, 98 / L1325, L1334 |

---

## Findings against the brief

Numbered `F1 …`; each states exactly what the brief says, what is true, and the numbers.

**F1 (Section 4/T5(a), wrong constant — the brief's identity is false).**
The brief writes

> `Note sqrt(y/t) theta(ty) = y theta(1/(ty)) by the theta functional equation`

This is false. By `theta(v) = v^{-1/2} theta(1/v)` with `v = ty`,

  `sqrt(y/t) theta(ty) = sqrt(y/t) (ty)^{-1/2} theta(1/(ty)) = t^{-1} theta(1/(ty)).`

The correct factor is **`1/t`, not `y`**. Numbers (script line L1069, check 78/79):

| `(t,y)` | `sqrt(y/t)theta(ty)` | `t^{-1}theta(1/(ty))` (correct) | `y theta(1/(ty))` (brief) |
|---|---|---|---|
| `(0.8, 1.3)` | `1.3719242310449` | `1.3719242310449` | `1.4268012002867` |
| `(2.0, 0.6)` | `0.57297737996699` | `0.57297737996699` | `0.68757285596038` |
| `(0.5, 3.0)` | `2.4934987331127` | `2.4934987331127` | `3.7402480996691` |

The two agree exactly on the locus `t y = 1` and nowhere else. Consequently the brief's next
sentence, "the constant term is `theta(t/y) + y theta(1/(ty)) - sqrt(y/t)`", must read

  `theta(t/y) + t^{-1} theta(1/(ty)) - sqrt(y/t)`.

(The *first* form of the constant term, `theta(t/y) + sqrt(y/t)(theta(ty)-1)`, is correct — D55.)

**F2 (Section 4/T5(a), wrong involution).**
The brief writes "`the GL_1 theta in two channels exchanged by the automorphism t -> 1/(y^2 t)…
state the exact involution`". `t -> 1/(y^2 t)` sends `t/y -> 1/(y^3 t)` and `ty -> 1/(yt)`; the
Poisson partner of `t/y` is `y/t`, and `1/(y^3 t) = y/t` only on the curve `t^2 y^4 = 1`. It is
not a symmetry of the constant term either. With `G(t) := theta(t/y) - 1 + sqrt(y/t)(theta(ty)-1)`
(script L1099, check 82):

| `(t,y)` | `G(t)` | `G(1/(y^2 t))` |
|---|---|---|
| `(0.8, 1.3)` | `0.13738906282372` | `0.46566124803458` |
| `(2.0, 0.6)` | `0.52531146058011` | `0.097320414484476` |
| `(0.5, 3.0)` | `0.49349876501691` | `3.5808496778019` |

**The exact involution is `t -> 1/t` carrying the weight `t^{-1}`**: numerically (to `1e-20` rel,
check 81)

  `t^{-1} G(1/t) = G(t) + 1 - 1/t`,

which is precisely the statement `Ghat(s) = Ghat(1-s)` for `Ghat(s) = int_0^inf G(t)t^s d^x t =
y^s Lambda(2s) + y^{1-s}Lambda(2s-1)`, the `s <-> 1-s` functional equation of the completed
Eisenstein constant term, the `1 - 1/t` being the two elementary (pole) terms. Under `t -> 1/t`,
`t/y -> 1/(ty)` (the Poisson partner of the second channel) and `ty -> y/t` (the partner of the
first) — verified to `1e-20`, check 83. Note `y` does not appear in the involution at all.

**F3 (Section 4/T5(b), evaluation point outside the region of convergence).**
The brief instructs: "`int_0^infty sqrt(y/t)(theta(ty)-1)t^s d^x t = y^{1-s}Lambda(2s-1) at
s = 0.3 + 0.5i`". The second integral converges only for `Re s > 1` (near `t -> 0` the integrand is
`~ t^{s-2}`), and the first only for `Re s > 1/2` (integrand `~ t^{s-3/2}`). At `s = 0.3+0.5i`
**both** diverge. Truncated `int_{e^{-X}}^{inf}` at `y = 2.5` (script L1188/L1195, checks 87, 89):

| `X` | ch1 at `1.2+0.5i` | ch1 at `0.3+0.5i` | ch2 at `1.2+0.5i` | ch2 at `0.3+0.5i` |
|---|---|---|---|---|
| 10 | `1.417302737` | `22.28648556` | `1.074893313` | `1258.294254` |
| 20 | `1.418013546` | `162.3399298` | `0.9201425199` | `1397863.519` |
| 40 | `1.418012403` | `8750.693493` | `0.8889475923` | `1.68123968e+12` |
| 80 | `1.418012403` | `26090519.18` | `0.8895664461` | `2.431504775e+24` |
| 160 | `1.418012403` | `2.318432341e+14` | `0.8895665092` | `5.085880052e+48` |

The divergence rates are exactly `e^{X(1/2 - Re s)}` (ch1: observed ratio `8.88611e+6` at
`X=80->160`, predicted `e^{16} = 8.88611e+6`) and `e^{X(1 - Re s)}` (ch2: observed
`2.09166e+24`, predicted `e^{56} = 2.09166e+24`). **Regions found numerically: ch1 `Re s > 1/2`,
ch2 `Re s > 1`; the common region (and the region where `E^*(z,s)` converges) is `Re s > 1`.**
Both identities were verified inside the regions at `s = 1.2+0.5i` (D59, D60).

**F4 (Section 2/T2(a), the residues — the determination the brief asked for).**
`ghat` has simple poles at `tau = ±i/4` with residues `±i`:

  `Res_{tau = +i/4} ghat = +i`, `Res_{tau = -i/4} ghat = -i`.

`tau = +i/4` is `s = 0` (where `Lambda` has residue `-2`) and `tau = -i/4` is `s = 1`
(residue `+2`); `ds/dtau = 2i`, so `Res_tau = Res_s/(2i)`. Cross-checked by
`eps * ghat(±i/4 + eps)` at `eps = 1e-12` (checks 26–28). The brief's parenthetical
("`1/2 + 2i tau = 1` iff `tau = -i/4`; `= 0` iff `tau = +i/4`") is correct as written (check 29).
**Which pole belongs to which half:** the `-i/4` pole (`s = 1`, residue `-i`) belongs entirely to
`ghat_>`, the *outgoing* half `y>1`; the `+i/4` pole (`s = 0`, residue `+i`) belongs entirely to
`ghat_<`, the incoming half (D31, checks 41–42). So the brief's T2(b) assignment is right.

**F5 (Section 2/T2(a), the asymptotic `|ghat(u)| ~ C|u|^c e^{-pi|u|/2}` is not literally true).**
`ghat` has *real zeros* (at `gamma_n/2`, D22), so no pointwise asymptotic of the form
`C|u|^c e^{-pi|u|/2}` can hold. What is true, and what determines `c`, is

  `|ghat(u)| = 2 pi^{-1/4} sqrt(2 pi) |u|^{-1/4} e^{-pi|u|/2} |zeta(1/2 + 2iu)| (1 + O(1/u))`,

verified as a ratio at `u = 40, 70, 100`: `1.0000048833`, `1.0000015944`, `1.0000007813`
(check 34, L585). So **`c = -1/4`**, but only after the factor `|zeta(1/2+2iu)|` is retained.
A naive log-log fit of `log|ghat| + (pi/2)u` against `log u` is badly contaminated: it returns
`c = -0.2057` on `u in [5,40]` and `c = -0.1416` on `[40,100]` (checks 32, and the info line
after 33). The exponential rate itself is robust: fitted slope `-1.58261886` on `[5,40]` and
`-1.57295904` on `[40,100]` versus `-pi/2 = -1.57079633`.

**F6 (Section 2/T2(b), the constant in the `1/|u|` decay of `ghat_>` — sharpening).**
The brief says only "`|ghat_>(u)|` decays only like `1/|u|`". Numerically the constant is

  `|u| |ghat_>(u)| -> 2 - theta(1) = 0.9135651888…`

(`theta(1) = 1.086434811213308`). Observed `|u||ghat_>(u)|`: `0.934736` (`u=5`), `0.917694`
(`u=10`), `0.914553` (`u=20`), `0.913810` (`u=40`) — check 40, L653. (The two contributions are the
pole term `2/(s-1) -> -i/u` and the jump of `(theta(y)-1)y^{1/4}` at `y=1`, which gives
`+i(theta(1)-1)/u`.) For contrast, at `u=40`: `|ghat_>| = 0.0228452` against
`|ghat| = 1.52136e-27` (check 45).

**F7 (Section 2/T3, quantitative Szegő divergence — confirmation with numbers).**
`I_full(T) = int_{-T}^{T} log|ghat(u)| du/(1+u^2)`: `-3.90630330835` (`T=10`),
`-6.01620982282` (`T=20`), `-8.16899533084` (`T=40`). The increments `-2.1099` and `-2.1528` do
not decay and approach `-pi log 2 = -2.1775861`, the exact prediction from
`log|ghat| ~ -(pi/2)|u|`. `I_half(T)`: `-0.0990607`, `-0.3672656`, `-0.5366418`, with increments
`-0.2682` and `-0.1694` decaying by a factor `1.58` per doubling. The ratio of increments at
`20->40` is `12.71`. The brief's T2(b)/T3 claim (full: not in `L^1(du/(1+u^2))`; half: in it)
is confirmed numerically.

**F8 (Section 2/T3(c), confirmation with values).**
`Lambda_>(rho_n)` at the first three zeros: `-0.13055641672683 i`, `-0.087268473867639 i`,
`-0.07326004624429 i` (real parts `< 2.6e-29`, i.e. `|Re|/|Im| < 8e-28`). They are purely
imaginary and **nonzero**, `Lambda_>(1-rho_n)` likewise nonzero, and
`Lambda(1/2+it) = 2 Re Lambda_<(1/2+it)` holds to `1e-18`. The brief's T3(c) claim that the
zeros of the *incomplete* Mellin transform are not the zeros of `zeta` is supported. (These are
values, not a proof that `Lambda_>` has no zero at any `rho`.)

**F9 (Section 1, sign convention — no change needed).**
The brief asks "Check this sign convention first; if it is wrong, fix it and say so." It is right.
For `f = 1_{y>1} y^{-1/2-1.3i}`, `fhat(tau) = 1/(1/2 - i(tau - 1.3))` (verified by quadrature at
three `tau`, check 04); its single pole is at `tau = 1.3 - i/2 in C_-`, `|fhat(2+3i)| = 0.2802`
while `|fhat(1.3 - 0.49i)| = 100.0`. So functions supported on `y > 1` have Mellin transforms of
Hardy class in `C_+`: **the outgoing half is `y > 1` and corresponds to `H^2(C_+)`**, as printed.
Also verified: `(U_t f)^hat = e^{i t tau} fhat` for `(U_t f)(y) = f(e^{-t}y)`, `supp U_t f =
{y > e^t}` for `t >= 0`, and `(Jf)^hat(tau) = fhat(-tau)` (checks 06–09). The `k_w` convention of
`04h` (line 33, `k_w(tau)=(tau-\bar w)^{-1}`; line 90, Cauchy matrix `i/(w_n - \bar w_m)`) is
consistent with `<k_w,k_v> = i/(v - conj w)` and with the constant `i` in D64.

**F10 (Section 5/T6(b), the "numerical signal" is not decisive at `N = 30`).**
The brief asserts: "`the zeros w_n = gamma_n/2 + i/4 are not uniformly separated in the hyperbolic
metric (spacing ~ pi/log gamma_n -> 0 at height 1/4), so the Carleson condition fails`". The
spacing formula is right in order of magnitude (the mean gap of `gamma_n` is `2 pi/log(gamma_n/2pi)`,
so the gap of `w_n` is `pi/log(gamma_n/2 pi)`), but the numerics at `N = 30` cannot see it:
near `gamma_30 = 101.3179` the observed mean gap of `gamma_n` is `2.5017` against
`2 pi/log(gamma_30/2pi) = 2.2598`, so the `w_n` gap is `~1.25` against a height of `0.25` — a
separation ratio of about `5`, not `<< 1`. The Carleson ratio `(pi/log(gamma/2pi))/(1/4)` first
drops to `1` only at `gamma ~ 2 pi e^{4 pi} ~ 1.8e6`. The Gram data are monotone but mild:

| `N` | `lambda_min` | `lambda_max` | `cond` |
|---|---|---|---|
| 10 | `3.99597060e-01` | `1.86641948` | `4.670754` |
| 20 | `2.70419603e-01` | `2.27824367` | `8.424847` |
| 30 | `2.01340242e-01` | `2.56015448` | `12.71556` |

`lambda_min` falls by factors `0.677` and `0.745` per doubling — consistent with a logarithmic
(or slow power) decay, hence with a failure of the Riesz property, but also consistent with a
positive limit. **This lane reports the trend as suggestive only; it does not confirm or refute
the Riesz-basis claim.** (The system is minimal at `N <= 30`: `G > 0` strictly, check 96.)

**F11 (Section 2/T2(c), sharpening: which half each edge line diverges in).**
The brief says the two edge lines are "`where the Mellin integral of phi diverges and only the
continuation exists`". More precisely (checks 53, 54, L735/L736): the numerator's line `Re s = 1`
is the Mellin transform of `y^{1/2}phi` and its integral diverges **at the outgoing end**,
`int_1^Y y^{1/2}phi d^x y = -log Y + O(1)`; the denominator's line `Re s = 0` is the Mellin
transform of `phi` and its integral diverges **at the incoming end**,
`int_delta^1 phi d^x y = log delta + O(1)`. Truncated values grow linearly in `X = log`-range with
slopes `-1` and `+1` respectively, verified to `1e-6` over `X = 10, 20, 40`. This matches the
brief's Section 4(c) picture (`y^{1/2}phi` not in `L^2(1,inf)` but in `L^2(0,1)`, and `phi` the
other way round): the `Re s = 1` edge is the one the outgoing half cannot support, and vice versa.

**F12 (Section 5/T6(a), the constant).**
The brief asks to "find the constant" relating `mhat_n` to the Cauchy kernel. With
`k_w(tau) = 1/(tau - conj w)` (04h line 33) the constant is exactly **`i`**:
`int_1^inf y^{-(1-sigma)/2 - i gamma/2} y^{i tau} d^x y = i/(tau - conj w)`,
`w = gamma/2 + i(1-sigma)/2`. Verified at `tau = 0.5` and `9.0` for the first three zeros to
`1e-14` relative (check 91).

**F13 (Section 3/T4, Balazard–Saias–Yor — values and tail).**
`(1/2 pi) int_{Re s=1/2} log|zeta(s)| |ds|/|s|^2` truncated to `|Im s| <= T`:
`-1.16067886e-4` (`T=50`), `+3.53484565e-6` (`T=100`), `+4.98326306e-6` (`T=200`).
The value is consistent with `0`, i.e. with the empty sum over zeros with `Re rho > 1/2`, at the
`5e-6` level. Tail estimate: the truncation error is bounded by
`(1/pi) int_T^inf |log|zeta(1/2+it)|| dt/t^2`, which with the empirical `|log|zeta|| <~ 2` gives the
crude scale `2/(pi T) = 1.27e-2, 6.4e-3, 3.2e-3`; the observed increments (`1.20e-4`, `1.45e-6`)
are far smaller, because `log|zeta|` oscillates about `0`. **This is a consistency check with RH,
not evidence for it.**

**F14 (Section 3/T4, Nyman — confirmation, plus the exact evaluation route).**
`int_0^1 rho_alpha(u) u^{s-1} du = (alpha - alpha^s) zeta(s)/s` holds (to `<= 2.9e-25` relative)
at `s = 2, 3+i, 0.7+5i` for `alpha = 1/2, 3/10, 2/7`. Two independent routes were used: a direct
truncated piecewise integration (`alpha = 0.3`, `T = 4000`, agreement `2.3e-11` at `s=2`) and an
exact Hurwitz-zeta evaluation resting on the step-function identity (verified, check 66)

  `rho_alpha(1/t) = {alpha t} - alpha{t} = alpha floor(t) - floor(alpha t)`,

which is periodic of period `q` for `alpha = p/q`. The region of convergence in `u` is `Re s > 0`.

**F15 (Section 2/T1, extra structure not stated in the brief).**
`||y^a phi|| = ||y^{1/2-a} phi||` for all `a` (verified at `a = 0.1 vs 0.4` and `0.15 vs 0.35` to
`1e-15`, check 17): the weight family is `J`-symmetric about `a = 1/4`, which is why `a = 1/4` is
simultaneously the unique `J`-fixed weight and the centre of the `L^2` window `0 < a < 1/2`.
`||g||^2 = int y^{1/2}phi(y)^2 d^x y = 3.91496940826907585`. Also
`C(t) = <U_t g, g>` at `t = 0, 1, 2, 4`: `3.914969408269`, `3.822181438389`, `3.583151087755`,
`2.909049783340`; real to `2e-33`, even to `1e-16`.

**F16 (nothing to correct).** Every other displayed formula of the brief that a computer can test
was reproduced: T1(a), T1(b), T2(a) (all displays, including `ghat(0) = -16 xi(1/2) =
-7.95393245101302576`), T2(b) (all displays), T2(c) (all displays including Hermite–Biehler),
T3 (both integrability statements), T4 (Nyman, BSY), T4(d) (the spectral-measure statement),
T5(a) first display, T5(b) both identities inside their regions, the scattering coefficient
`phi(1/2+i tau) = Theta(tau)^{-1}(tau-i/2)/(tau+i/2)`, T6(a) and T6(b).

---

## Conventions used

- `theta(y) = sum_{n in Z} e^{-pi n^2 y}`. Implemented as `1 + thetam1(y)` with
  `thetam1(y) = 2 sum_{n>=1} e^{-pi n^2 y}` for `y >= 1` and
  `theta(y) = y^{-1/2}(1 + thetam1(1/y))` for `y < 1`. The brief's recipe
  (`jtheta(3,0,exp(-pi y))` for `y >= 1`, functional equation below) is cross-checked against this
  at 9 values of `y` (checks 01, 02) and used nowhere else, because **`jtheta` loses all precision
  in the combinations that matter**: `phi(y) = theta(y) - 1 - y^{-1/2}` for small `y` is a
  difference of two quantities of size `y^{-1/2}` whose true value is `O(1)`. The
  cancellation-free forms actually used are
  `phi(y) = thetam1(y) - y^{-1/2}` for `y >= 1` and `phi(y) = y^{-1/2} thetam1(1/y) - 1` for
  `y < 1`; for the near-zero asymptotic, `phi(y) + 1 = y^{-1/2} thetam1(1/y)` directly.
- Mellin transform `fhat(tau) = int_0^inf f(y) y^{i tau} d^x y`, `d^x y = dy/y`; dilation
  `(U_t f)(y) = f(e^{-t}y)`; inversion `(Jf)(y)=f(1/y)`. Outgoing half `y > 1` ↔ `H^2(C_+)`
  (confirmed, F9).
- `phi(y) = theta(y) - 1 - y^{-1/2}`, `g(y) = y^{1/4} phi(y)`,
  `ghat(tau) = Lambda(1/2 + 2 i tau)`, `Lambda(s) = 2 pi^{-s/2}Gamma(s/2)zeta(s) = 4 xi(s)/(s(s-1))`,
  `xi(s) = (1/2)s(s-1)pi^{-s/2}Gamma(s/2)zeta(s)` (implemented as
  `(s-1)pi^{-s/2}Gamma(s/2+1)zeta(s)`, with `xi(0)=xi(1)=1/2` hard-set within `1e-20` of those
  points), `xi_crit(tau) = xi(1/2+2i tau)`, `Theta(tau) = xi(1+2i tau)/xi(1-2i tau)`.
- Halves: `Lambda_>(s) = int_1^inf phi y^{s/2}d^x y` evaluated as
  `2/(s-1) + 2 sum_{n>=1}(pi n^2)^{-s/2}Gamma(s/2, pi n^2)` (`mpmath.gammainc`, 5 terms at 25
  digits), cross-checked against direct quadrature at four `s` (check 35);
  `Lambda_<(s) = Lambda_>(1-s)`, cross-checked against direct `int_0^1` quadrature (check 36).
- **Quadrature of Mellin integrals of `phi`.** Everything is done in `x = log y` on `[-25, 25]`,
  with the two elementary tails integrated in closed form:
  `int_{-inf}^{-X}(-1)e^{sx/2}dx = -2e^{-Xs/2}/s` and
  `int_X^inf(-e^{-x/2})e^{sx/2}dx = +2e^{X(s-1)/2}/(s-1)`. Beyond `|x| = 25` the neglected theta
  tail is `O(e^{-pi e^{25}})`, i.e. exactly zero at any working precision, so these are *exact*
  tails and the quadrature carries full accuracy. Subdivision resolves the oscillation
  `e^{i Im(s) x/2}` at half a period.
- Inner product on the Mellin side: `<F,G> = (1/2 pi) int_R F conj(G) du`, so that
  `k_w(tau) = 1/(tau - conj w)` has `<k_w,k_v> = i/(v - conj w)` and `||k_w||^2 = 1/(2 Im w)`.
  This is the convention of `04h` (line 90: the Cauchy matrix `i/(w_n - conj w_m)`).
- Zeta zeros from `mpmath.zetazero` (80 of them, `gamma_80 = 201.264752`).
- Precision `mp.dps = 25` throughout, dropped to `18` for the Szegő integrals and `15` for the
  Balazard–Saias–Yor integral (both are quadratures over `log`-singular integrands where the
  answer is wanted to 4–6 digits only, and `mp.zeta` dominates the cost).
- No randomness is actually used; `numpy.random.seed(20260921)` is set for reproducibility of any
  future sampling. Runtime 69 s (limit 120 s).

---

## Tally

- checks executed: **98**
- passed: **98**
- failed: **0**
- ledger rows: **68** (D01–D68); verdicts: 65 VERIFIED, 1 PARTIAL (D68), 2 FAILED-against-the-brief
  (D56, D57) plus D62 recorded as FAILED for the brief's evaluation point.
- findings against the brief: **16** (F1–F16), of which **three are errors in the brief**
  (F1 wrong constant `y` for `1/t`; F2 wrong involution; F3 evaluation point outside both regions
  of convergence), one is a statement that is false as printed but true in a corrected form
  (F5, the pointwise asymptotic for `|ghat|`), one confirms a convention the brief asked to be
  checked (F9), one downgrades a claimed numerical signal to inconclusive (F10), and the rest are
  sharpenings or confirmations with values.
