# RTP-1, lane A2: the prime-content channel (Step 2)

Author: `claude:opus`, 2026-09-24. Brief: `notes/rtp-round-1/brief.md` (lane A2). Background read:
`notes/metric-tomography/metric-as-state.md` sections 3 (with the Correction), 4.2, 6. Lane A1 was not read.

Files:

- script `scripts/rtp1_prime_content.py` (deterministic, seed 20260924, single `check(cond, msg)` helper as in
  `scripts/gl1_bond.py`, no timestamps, runtime about 1 min 40 s);
- output `outputs/rtp1_prime_content.txt` (produced from the repository root by
  `python3 scripts/rtp1_prime_content.py > outputs/rtp1_prime_content.txt 2>&1`; run twice plus one earlier run,
  byte-identical under `cmp`; sha256 `6361ccd076b36f5b46187062fe73504251da874270d6672f9fd70876a39afb65`);
  **192 checks passed, 0 failed**.

Zeros of zeta are used only in the labelled comparison step (Section 7 of the output, section 6 here). No
form, entry or eigenvalue below uses a zero. RH is not assumed anywhere.

## 0. Results in one paragraph

The Weil form on the brief's lattice of bumps is certified positive in all 42 cases measured, and its structure is
**exactly separable up to O(delta)**. With the mixed entries (lattice points differing in two or more coordinates)
set to zero, the form is *exactly* the Kronecker sum of the one-prime forms (a lemma, section 4.1). Its minimal
eigenvector is then a tensor product, and adding a prime does not move it at all on the old sublattice. The true
form differs from that Kronecker sum only through the mixed entries. Those carry no prime term (verified) and are
of size O(delta) relative to the diagonal. They move lambda_min by O(delta) (the ratio gap/delta converges) and the
eigenvector by O(delta^2) (fitted slopes 2.000 to 2.06). But admissibility forces delta to shrink roughly like the
reciprocal of the largest lattice ratio: delta_max = 1.2e-6 already for `S = {2,3,5}, A = 4`. So the inter-place
correlation this channel can see is small: Schmidt defect 3e-3 down to 6e-9. **The correlation is carried mainly by
the pole term W_{0,2}, not by the archimedean kernel.** To first order along the minimal eigenvector, the pole part
of the mixed entries is 2.4 to 21 times the archimedean part, with the opposite sign. The note's Correction said the
archimedean kernel carries this correlation, and that is wrong in this respect. The explicit formula checks against
2000 certified zeros to a relative 1e-15 to 1e-18 (delta = 0.1) and 1e-11 to 1e-13 (delta = 0.05). The truncation
error decays like exp(-2.2 sqrt(delta gamma_M)).

## 1. Definitions

### 1.1 The form (brief, Conventions)

Log coordinate `y = log u`, Lebesgue measure `dy = d*u`. `QW(f, g) = Psi(f^* * g)`, where
`(f^* * g)(y) = int conj f(x - y) g(x) dx` and `Psi = W_{0,2} - W_R - sum_p W_p`
(`refs/src/2511.22755/mc2arXiv.tex` eq. `bombtest`, l.385-388). In the `F`-normalisation of l.366-383:

    W_{0,2}(F) = Fhat(i/2) + Fhat(-i/2) = int F(y) 2 cosh(y/2) dy,      Fhat(t) = int F(y) e^{-ity} dy,
    W_p(F)     = log p sum_{m>=1} p^{-m/2} (F(m log p) + F(-m log p)),
    W_R(F)     = (log 4 pi + gamma) F(0) + int_0^oo (F(y) + F(-y) - 2 e^{-y/2} F(0)) rho(y) dy,
    rho(y)     = e^{y/2}/(e^y - e^{-y}).

`Psi` sees only `q(y) = F(y) + F(-y)` on `y >= 0` (the paper's `q(f, g)`). The general implementation
`psi_general(q, Y)` evaluates these three definitions literally, by `mpmath.quad` at 60 digits, for any `q`
supported in `[0, Y]`. The prime sum runs over every prime power `k <= e^Y`. The arch tail beyond `Y` is added
in closed form: `-(q(0)/2) int_Y^oo dy/sinh y = (q(0)/2) log tanh(Y/2)`. This one implementation is used for the
zst check (section 2) and as an independent check of the bump formulas (section 3).

### 1.2 Test class (brief A2.1)

`phi_delta(x) = exp(-1/(1 - (x/delta)^2))` on `|x| < delta`, and `phi_1` is the `delta = 1` bump. For
`S = {p_1 < ... < p_r}` and `Lambda_S(A) = {0..A}^r`:
`phi_alpha(x) = phi_delta(x - t_alpha)`, `t_alpha = sum a_p log p`, `n_alpha = prod p^{a_p}`. Then
`phi_alpha^* * phi_beta = R_delta(. - D')`, where `D' = log(n_beta/n_alpha)` and
`R_delta(s) = int phi_delta(x - s) phi_delta(x) dx = delta R_1(s/delta)`, supported in `|s| < 2 delta`.
(The brief writes the centre as `log(n_alpha/n_beta)`. `q` is even, so only `D = |D'|` matters.)

Closed forms per entry, all derived from the definitions in 1.1:

    pole  = 2 cosh(D/2) c_delta^2,         c_delta = int phi_delta e^{x/2} dx = delta int phi_1(t) e^{delta t/2} dt
    prime = sum over all prime powers k of Lambda(k) k^{-1/2} [R_delta(log k - D) + R_delta(log k + D)]
    arch, D > 2 delta:  int int phi_delta(x) phi_delta(w) rho(D + x - w) dx dw
                      = sum_{j even} rho_j(D) delta^{j+2} Mt_j,
                        rho_j = rho^{(j)}(D)/j!,  Mt_j = int int phi_1 phi_1 (x-w)^j = sum_{i even} C(j,i) mu_i mu_{j-i}
    arch, D = 0:        delta [ (log 4 pi + gamma - log 2) R_1(0) + T_1 + R_1(0) log delta + sum_j r_j delta^{j+1} At_j ]
    G_{alpha beta} = pole - arch - prime

Here `mu_i = int phi_1 t^i`, `T_1 = int_0^2 (R_1(s) - R_1(0))/s ds + R_1(0) log 2`, `At_j = int R_1(u) |u|^j du`,
and `r_j` are the Taylor coefficients at 0 of `rho_reg(y) = rho(y) - 1/(2y)`, which is analytic for `|y| < pi`
(`rho_reg = 1/4 - y/48 - y^2/32 + ...`).

*Derivation of the D = 0 formula.* `F = R` is even, so
`W_R(R) = (log 4pi + gamma) R(0) + int_0^oo [2R(y) rho(y) - R(0)/sinh y] dy`. Split at `Y = 2 delta`, write
`2 rho = 1/y + 2 rho_reg`, and use `int_Y^oo dy/sinh y = -log tanh(Y/2)` and
`int_0^Y (1/y - 1/sinh y) dy = log Y - log tanh(Y/2) - log 2`. The `log tanh` terms cancel, and
`W_R(R) = (log 4pi + gamma - log 2) R(0) + [int_0^Y (R(y) - R(0))/y dy + R(0) log Y] + int R(u) rho_reg(|u|) du`.
The bracket scales as `delta (T_1 + R_1(0) log delta)`. The last integral is `sum_j r_j delta^{j+2} At_j`.

Consequence: the normalised diagonal is `d = G_{alpha alpha}/||phi||^2 = -log delta - log 2 pi - gamma - T_1/R_1(0) + O(delta)`,
that is `d = -log delta - 1.9555 + O(delta)`. The output agrees: `d + log delta = -1.951` at `delta = 0.001587`.
This logarithmic self-energy is what positivity runs on in this test class (section 7).

Constants (certified, arb): `mu_0 = 0.44399381616807943782...`, `R_1(0) = int phi_1^2 = 0.13308612084499427155...`.
Constant (not certified, see 6): `T_1 = -0.06117053533400677206...`.

All Gram matrices are reported normalised by `||phi_delta||^2 = delta R_1(0)`. The translates are pairwise
disjointly supported (checked), so `G/||phi||^2` is `QW` on an orthonormal family.

### 1.3 Admissible delta (brief A2.1)

`delta_max(S, A) = (1/2) min |log k - log r|`. The minimum is over lattice ratios `r = n_beta/n_alpha >= 1` and
prime powers `k != r`. The case `r = 1` is included and gives `log 2`. For `delta < delta_max`, an entry has a
prime term iff `r` is a prime power, and that term is then exactly `log p p^{-j/2} ||phi||^2`. Each `delta_max`
is **sharp**: at `delta_max (1 + 1e-12)` the binding ratio picks up its foreign neighbour (checked, all 14 rows).
Also `2 delta_max < min_{r>1} log r` and `2 delta_max <= log 2` in every row, so entries have either `D = 0` or
`D > 2 delta`.

| S | A | dim | #ratios | delta_max | binding pair | min log r (r>1) |
|---|---|---|---|---|---|---|
| {2} | 1 | 2 | 2 | 0.2027325541 | 2 vs 3 | 0.6931 |
| {2} | 2 | 3 | 3 | 0.1115717757 | 4 vs 5 | 0.6931 |
| {2} | 3 | 4 | 4 | 0.05889151783 | 8 vs 9 | 0.6931 |
| {2} | 4 | 5 | 5 | 0.03031231091 | 16 vs 17 | 0.6931 |
| {2} | 5 | 6 | 6 | 0.01587434916 | 32 vs 31 | 0.6931 |
| {2} | 6 | 7 | 7 | 0.01587434916 | 32 vs 31 | 0.6931 |
| {2,3} | 1 | 4 | 5 | 0.07707533991 | 6 vs 7 | 0.4055 |
| {2,3} | 2 | 9 | 13 | 0.01369948709 | 36 vs 37 | 0.2877 |
| {2,3} | 3 | 16 | 25 | 0.004608327552 | 108 vs 109 | 0.1178 |
| {2,3} | 4 | 25 | 41 | 0.0003856537021 | 1296 vs 1297 | 0.1178 |
| {2,3,5} | 1 | 8 | 14 | 0.01639491141 | 30 vs 31 | 0.1823 |
| {2,3,5} | 2 | 27 | 63 | 0.001112347511 | 450 vs 449 | 0.1054 |
| {2,3,5} | 3 | 64 | 172 | 3.703840885e-5 | 13500 vs 13499 | 0.04082 |
| {2,3,5} | 4 | 125 | 365 | 1.234566377e-6 | 405000 vs 405001 | 0.01242 |

(Balls of radius below 1e-59. The pair names the ratio `r` and the foreign prime power `k` at minimal distance.)

The delta grid is `0.9, 0.3, 0.1 x delta_max(S, A)`, each rounded down to 4 significant digits (the values are in the
summary table of section 4.2).

## 2. Consistency check against zst (brief, Conventions; A2.2(iii)): PASSED

`zst`'s driver does not print `(a_n, b_n)`. The script therefore compiles, in a temporary directory, a 20-line
printer that calls `zst_riemann_ab` from `zst/build/libzst.a` at 300 bits and prints 60 digits. zst itself is not
modified. The general `Psi` of 1.1 is applied to `q(U_n, U_m)`. The generic convolution quadrature reproduces the
paper's closed form (Lemma `polarize0`) to 1.1e-61 at 9 samples. The values `a_n = Psi(q(U_n, U_n))` and
`b_n = n Psi(q(U_n, U_0))` then give:

| window | modes | max \|a_n - a_n^zst\|, \|b_n - b_n^zst\| | Loewner off-column `(b_n - b_m)/(n-m)` | vs 50-digit reference (`test_ab`) |
|---|---|---|---|---|
| x = 13 (paper) | n = 0..10 | **2.2e-60** | 3.5e-61 | n/a |
| x = 9 | n = 0..8 | **4.0e-60** | 1.9e-61 | 3.1e-50 (the reference's own 50 digits) |

(quad error estimates <= 1e-63). Example at x = 13: `a_1 = 0.0465118895436779793116060710601`,
`b_1 = 0.0457203442394000540357853654912`. This implementation of `W` is independent of zst's digamma/Lerch closed
forms and of the Loewner structure.

## 3. Structure of the entries (A2.2(i), (ii)) and cross-check of the bump formulas

- (i) In every one of the 42 Gram matrices, **every mixed entry has no prime contribution**: 27,918 mixed pairs
  in total. The prime-power membership test is decided in ball arithmetic over all prime powers with
  `|log k - D| < 2 delta`.
- (ii) Every axis-type entry (differing in one coordinate `p` by `j`) carries exactly the comb term
  `-log p p^{-j/2} ||phi||^2` of its own ratio and nothing else. The diagonal carries none.
- The bump closed forms of 1.2 were checked against `psi_general` applied to `q(y) = R_delta(y - D) + R_delta(y + D)`,
  with `R_1` evaluated by certified arb integrals at the quadrature nodes. Cases: `r = 1, 2, 3/2` at `delta = 0.05`,
  and the deliberately non-admissible `r = 8` at `delta = 0.1`, where the neighbours 7 and 9 also enter through
  `R_1` at non-zero arguments. Agreement is to 2.7e-60 or better, part by part (pole, arch, prime).

This cross-check caught a real bug during development: python-flint's default power-series cap (10) truncated the
`rho_reg` series and produced a 5.8e-19 diagonal discrepancy. It was fixed by `ctx.cap = 1000`.

## 4. Measurements (A2.3)

### 4.1 An exact lemma that organises everything

**Lemma (Kronecker structure).** Let `G_nomix` be `G` with the mixed entries set to 0. An axis-type entry depends
only on the ratio `p^j`, the diagonal is the constant `d`, and the one-prime form `G_(p)` on `{0..A}` has the same
diagonal. Hence

    G_nomix = d I + sum_{p in S} I x ... x (G_(p) - d I) x ... x I,

that is, the Kronecker sum of the one-prime forms. So `lambda_min(G_nomix) = d + sum_p (lambda_min(G_(p)) - d)`,
and its minimal eigenvector is `(x)_p v_(p)`, a product state.

*Proof.* Entrywise comparison: the right-hand side has entry `G_(p)[a_p, b_p]` exactly when alpha and beta differ
only in coordinate `p`, `d` on the diagonal, and 0 otherwise. Checked numerically in all 24 multi-prime cases: the
eigenvalue identity holds to 1e-40, and the eigenvector's Schmidt defect is below 1e-40.

So brief decomposition 2 (mixed entries replaced by 0) is exactly "the places decoupled". All inter-place
correlation of the form, and of its minimal eigenvector, sits in the mixed entries. By 3(i) these are
**pole + archimedean only**.

### 4.2 Summary table (normalised; lambda = certified simple minimal eigenvalue)

Legend: `G_X` = principal submatrix on the single-prime points (origin plus axes). `G_bd` = direct sum of the
one-prime forms, the brief's "block-diagonal restriction to the axis subspaces" (see Findings 2). `nomix` = mixed
entries zeroed. `noP` = prime terms removed. `gap_mix = lambda(nomix) - lambda(G)`. `offaxis` = weight of `v_min`
off `X`. `schmidt` = max over cuts `{p} | S - {p}` of `1 - sigma_1^2`.

```
      S  A      delta          d       lam(G)     lam(G_X)    lam(G_bd)   lam(nomix)   lam(noP)    gap_mix   offaxis   schmidt
    {2}  1     0.1824   0.220168  0.044731016  0.044731016  0.044731016  0.044731016 -0.0945246   0.00e+00  0.00e+00       0.0
    {2}  1    0.06081    1.00225   0.61814403   0.61814403   0.61814403   0.61814403   0.896226   0.00e+00  0.00e+00       0.0
    {2}  1    0.02027    1.99570    1.5409518    1.5409518    1.5409518    1.5409518    1.96032   0.00e+00  0.00e+00       0.0
    {2}  2     0.1004   0.603658   0.12970056   0.12970056   0.12970056   0.12970056   0.311124   0.00e+00  0.00e+00       0.0
    {2}  2    0.03347    1.52842   0.78076753   0.78076753   0.78076753   0.78076753    1.43092   0.00e+00  0.00e+00       0.0
    {2}  2    0.01115    2.56976    1.7288143    1.7288143    1.7288143    1.7288143    2.53728   0.00e+00  0.00e+00       0.0
    {2}  3    0.05300    1.11944   0.29004107   0.29004107   0.29004107   0.29004107   0.872899   0.00e+00  0.00e+00       0.0
    {2}  3    0.01766    2.12677    1.0434503    1.0434503    1.0434503    1.0434503    2.04464   0.00e+00  0.00e+00       0.0
    {2}  3   0.005889    3.19447    2.0247323    2.0247323    2.0247323    2.0247323    3.16709   0.00e+00  0.00e+00       0.0
    {2}  4    0.02728    1.71687   0.54118249   0.54118249   0.54118249   0.54118249    1.51821   0.00e+00  0.00e+00       0.0
    {2}  4   0.009093    2.76836    1.3899227    1.3899227    1.3899227    1.3899227    2.70215   0.00e+00  0.00e+00       0.0
    {2}  4   0.003031    3.85126    2.4039248    2.4039248    2.4039248    2.4039248    3.82919   0.00e+00  0.00e+00       0.0
    {2}  5    0.01428    2.33045   0.85705063   0.85705063   0.85705063   0.85705063    2.16970   0.00e+00  0.00e+00       0.0
    {2}  5   0.004762    3.40397    1.7766527    1.7766527    1.7766527    1.7766527    3.35037   0.00e+00  0.00e+00       0.0
    {2}  5   0.001587    4.49456    2.8150095    2.8150095    2.8150095    2.8150095    4.47670   0.00e+00  0.00e+00       0.0
    {2}  6    0.01428    2.33045   0.75466824   0.75466824   0.75466824   0.75466824    2.08496   0.00e+00  0.00e+00       0.0
    {2}  6   0.004762    3.40397    1.6188491    1.6188491    1.6188491    1.6188491    3.32211   0.00e+00  0.00e+00       0.0
    {2}  6   0.001587    4.49456    2.6372872    2.6372872    2.6372872    2.6372872    4.46728   0.00e+00  0.00e+00       0.0
 {2, 3}  1    0.06936   0.892886   0.20834288   0.32731261   0.42912272  0.059879534   0.630368  -1.48e-01  2.21e-01   0.00332
 {2, 3}  1    0.02312    1.87154   0.89532959    1.1489862    1.2940949   0.84431801    1.78405  -5.10e-02  2.42e-01  0.000242
 {2, 3}  1   0.007707    2.93014    1.8552569    2.1549250    2.3148081    1.8381324    2.90098  -1.71e-02  2.48e-01   2.38e-5
 {2, 3}  2    0.01232    2.47301   0.76014856    1.3117999    1.4489781   0.61293939    2.30378  -1.47e-01  4.94e-01  0.000972
 {2, 3}  2   0.004109    3.54977    1.6558568    2.3183476    2.4760715    1.6055744    3.49332  -5.03e-02  4.86e-01   9.18e-5
 {2, 3}  2   0.001369    4.64176    2.6863122    3.3867841    3.5514562    2.6694452    4.62296  -1.69e-02  4.84e-01   9.66e-6
 {2, 3}  3   0.004147    3.54066    1.1104032    2.0127485    2.1418723   0.95928478    3.35881  -1.51e-01  6.49e-01     0.001
 {2, 3}  3   0.001382    4.63234    2.0512994    3.0611220    3.2024825    1.9994764    4.57174  -5.18e-02  6.36e-01    0.0001
 {2, 3}  3  0.0004608    5.72828    3.0956490    4.1425602    4.2880368    3.0782205    5.70807  -1.74e-02  6.32e-01   1.08e-5
 {2, 3}  4  0.0003470    6.01162    2.8628708    4.1855621    4.3085152    2.8305058    5.96759  -3.24e-02  7.30e-01   4.36e-5
 {2, 3}  4  0.0001156    7.11021    3.9329518    5.2778124    5.4027548    3.9220961    7.09554  -1.09e-02  7.28e-01   4.78e-6
 {2, 3}  4 0.00003856    8.20793    5.0211150    6.3734208    6.4990268    5.0174858    8.20304  -3.63e-03  7.27e-01   5.29e-7
{2,3,5}  1    0.01475    2.29929   0.74604970    1.3075384    1.6279728   0.56557107    2.12670  -1.80e-01  5.00e-01   0.00151
{2,3,5}  1   0.004918    3.37214    1.6258251    2.3234179    2.6685311    1.5647946    3.31460  -6.10e-02  5.00e-01  0.000139
{2,3,5}  1   0.001639    4.46246    2.6509770    3.3946783    3.7480768    2.6305545    4.44328  -2.04e-02  5.00e-01   1.45e-5
{2,3,5}  2   0.001001    4.95389    1.8960090    3.4055069    3.7712759    1.7951798    4.84379  -1.01e-01  7.95e-01  0.000366
{2,3,5}  2  0.0003337    6.05067    2.9132753    4.4921544    4.8621439    2.8791934    6.01397  -3.41e-02  7.88e-01   3.89e-5
{2,3,5}  2  0.0001112    7.14901    3.9846773    5.5871057    5.9585062    3.9732698    7.13678  -1.14e-02  7.85e-01   4.25e-6
{2,3,5}  3 0.00003333    8.35368    4.1996387    6.4963935    6.8417298    4.1836880    8.32807  -1.60e-02  8.99e-01   1.49e-5
{2,3,5}  3 0.00001111    9.45223    5.2867550    7.5942768    7.9398744    5.2814175    9.44370  -5.34e-03  8.98e-01   1.65e-6
{2,3,5}  3 0.000003703    10.5509    6.3816068    8.6927360    9.0384208    6.3798256    10.5481  -1.78e-03  8.98e-01   1.84e-7
{2,3,5}  4 0.000001111    11.7548    6.8263518    9.6982760    10.015896    6.8243149    11.7496  -2.04e-03  9.47e-01    4.6e-7
{2,3,5}  4 0.0000003703    12.8535    7.9236463    10.796933    11.114570    7.9229668    12.8518  -6.80e-04  9.47e-01   5.11e-8
{2,3,5}  4 0.0000001234    13.9524    9.0220589    11.895801    12.213443    9.0218324    13.9518  -2.27e-04  9.47e-01   5.68e-9
```

Certification: every `lambda(G)` is a ball of radius about 2e-54, set by the non-certified diagonal constant (see
6). Each is simple: `LDL^T` of `G - s I` has exactly one negative pivot, with a certified gap from 0.18 to 0.74.
The eigenvector angle bound is `sin <= 1e-53`. The same certificate covers every other lambda in the table.

Examples of Gram matrices (normalised):

```
{2}, A = 2, delta = 0.1004:           {2,3}, A = 1, delta = 0.06936, order (0,0),(0,1),(1,0),(1,1):
  0.603658  -0.315455  -0.054040        0.892886  -0.463764  -0.369243   0.250499
 -0.315455   0.603658  -0.315455       -0.463764   0.892886   0.057563  -0.369243
 -0.054040  -0.315455   0.603658       -0.369243   0.057563   0.892886  -0.463764
                                        0.250499  -0.369243  -0.463764   0.892886
```

In the `{2,3}` example, the entries `0.2505` ((0,0)-(1,1), ratio 6) and `0.0576` ((0,1)-(1,0), ratio 3/2) are the
mixed entries: pole plus archimedean only. The `{2}` entry `-0.054` at ratio 4 is comb `-log2/2 = -0.3466` plus
pole-minus-arch `+0.2925`. Minimal eigenvectors for small cases, all components positive and reflection-symmetric
(`alpha -> A - alpha`):

- `{2}, A=3, delta=0.053`: (0.418, 0.571, 0.571, 0.418).
- `{2,3}, A=1, delta=0.069`: (0.470, 0.528, 0.528, 0.470).
- `{2,3}, A=4, delta=3.47e-4`: 8 largest components 0.258 at (2,2), then 0.244 at (1,2),(3,2), and so on.

### 4.3 The three decompositions

**(a) G vs the block-diagonal restriction to the axis subspaces (inter-place gap).**
`lambda(G_bd) - lambda(G)` is 0.22 to 1.48 for `{2,3}` and 0.88 to 3.19 for `{2,3,5}`. By the lemma this gap is
**almost all Kronecker addition**: `lambda(nomix) - d = sum_p (lambda(G_(p)) - d)`. The comb depths of the
individual primes add. It is not correlation, and the mixed correction is only the column `gap_mix`. The principal
submatrix on the axes (`G_X`) lies in between.

**(b) G vs G with mixed entries zeroed (brief: "archimedean kernel at S-smooth rationals").**
`gap_mix` is negative in every case: the mixed entries *raise* `lambda_min`. It is exactly linear in delta.
`gap_mix/delta` converges as delta decreases through the grid:

| S | A=1 | A=2 | A=3 | A=4 |
|---|---|---|---|---|
| {2,3} | -2.22 | -12.3 | -37.8 | -94.1 |
| {2,3,5} | -12.5 | -102.6 | -481.0 | -1835.6 |

Split of the mixed entries into their two parts. Both the eigenvalue gaps and the first-order values
`v^T (G - G_x) v` are shown; they agree, which confirms the perturbative regime.

| case (0.9 delta_max) | first-order pole part | first-order arch part | pole/arch | lam(G) with mixed pole removed | with mixed arch removed |
|---|---|---|---|---|---|
| {2,3} A=1 | +0.247 | -0.104 | 2.4 | **-0.0396** (indefinite) | 0.3105 |
| {2,3} A=2 | +0.204 | -0.061 | 3.4 | | |
| {2,3} A=3 | +0.188 | -0.042 | 4.5 | | |
| {2,3} A=4 | +0.0375 | -0.0054 | 6.9 | | |
| {2,3,5} A=1 | +0.250 | -0.074 | 3.4 | | |
| {2,3,5} A=2 | +0.120 | -0.021 | 5.7 | | |
| {2,3,5} A=3 | +0.0175 | -0.0017 | 10.6 | | |
| {2,3,5} A=4 | +0.00214 | -0.00010 | 21.0 | | |

The pole part of a mixed entry is `2 cosh(D/2) c_delta^2/||phi||^2 ~ 2.96 delta cosh(D/2)`. The archimedean part is
`~1.48 delta rho(D)`, with `rho(D) ~ e^{-D/2}`. So the pole wins by a factor of `2 cosh(D/2)/rho(D) ~ e^{D}` at large `D`, and
large lattice ratios make it dominant. The pole is also what keeps the smallest two-prime case positive: removing
only the pole part of the two mixed entries in `{2,3}, A = 1, delta = 0.069` makes the form indefinite
(`-0.0396`).

**(c) G vs G without prime terms (combs).** `lambda(noP) - lambda(G)` ranges from -0.139 to +4.93. The first-order
comb contribution `v^T(G - G_noP)v` is `-1.12` (`{2,3}` A=1) up to `-4.93` (`{2,3,5}` A=4). This is the dominant
off-diagonal structure. At `{2}, A = 1, delta = 0.1824` the pole-plus-arch form alone is **indefinite**
(`lambda(noP) = -0.0945`), and the 2-comb restores positivity (`lambda(G) = +0.0447`). The pole term's positive
off-diagonal would otherwise win against the diagonal.

Positivity: all 42 Gram matrices are certified positive definite. This is a necessary condition of RH on these
finite families, so it is consistent with RH and proves nothing beyond them. Mechanism: `lambda(G) = d +
sum_p (comb depth of p) + O(delta)`. The one-prime Toeplitz symbol gives a comb depth of at most
`2 log p/(sqrt p - 1)` as `A -> oo` (3.35, 3.00, 2.61 for p = 2, 3, 5; symbol minimum, not certified). Against it
stands the log self-energy `d = -log delta - 1.9555`. Admissibility makes delta tiny, so `d` wins comfortably.
The Correction's statement "positivity is about correlations between places" is not tested by this regime: the
margin is set by the self-energy.

### 4.4 Eigenvector movement when a prime is added

Common delta, admissible for the largest S, at `delta_c = 0.9 delta_max({2,3,5}, A)`, `delta_c/10` and
`delta_c/100`. `1 - overlap` compares the restriction of the new minimal eigenvector to the old sublattice with the
old minimal eigenvector. "weight" is the norm squared of that restriction, and "Kron." is the Kronecker-sum
prediction `v_new[0]^2`.

| A | step | 1-overlap at delta_c, /10, /100 | weight (Kron.) at delta_c | log-log slope |
|---|---|---|---|---|
| 1 | {2}->{2,3} | 4.6e-5, 4.2e-7, 4.1e-9 | 0.5000 (0.5000) | 2.02 |
| 1 | {2,3}->{2,3,5} | 7.6e-4, 5.8e-6, 5.7e-8 | 0.5000 (0.5000) | 2.06 |
| 2 | {2}->{2,3} | 4.8e-6, 4.7e-8, 4.7e-10 | 0.29865 (0.29960) | 2.01 |
| 2 | {2,3}->{2,3,5} | 4.1e-4, 3.7e-6, 3.7e-8 | 0.28044 (0.28834) | 2.02 |
| 3 | {2}->{2,3} | 7.2e-8, 7.2e-10, 7.2e-12 | 0.19817 (0.19828) | 2.00 |
| 3 | {2,3}->{2,3,5} | 2.4e-5, 2.3e-7, 2.3e-9 | 0.18167 (0.18333) | 2.00 |
| 4 | {2}->{2,3} | 7.6e-10, 7.6e-12, 7.6e-14 | 0.13929 (0.13930) | 2.00 |
| 4 | {2,3}->{2,3,5} | 9.7e-7, 9.7e-9, 9.7e-11 | 0.12371 (0.12396) | 2.00 |

The eigenvector on the old places does not learn from the new prime, except at O(delta^2). Its weight on the old
sublattice is the product-state value `v_new[0]^2` up to O(delta). The eigenvalue moves by the new prime's comb
depth. Example at A = 1, delta = 0.01475: `lambda` goes 1.835 -> 1.270 -> 0.746 as {2} -> {2,3} -> {2,3,5}.

## 5. What the round asked (this lane's part)

- **Q2 (how much of the two-prime eigenvector lives off the axes, and who carries it).** Off-axis weight: 22-25%
  (`{2,3}` A=1), 48-49% (A=2), 63-65% (A=3), 73% (A=4); `{2,3,5}`: 50%, 79%, 90%, 95%. That weight is almost all
  **product-state weight**. It is `1 - (weight of a tensor product on the axes)`, and it comes from the combs
  acting along lattice lines through off-axis points. The genuine inter-place part is the Schmidt defect: 3e-3
  down to 6e-9, scaling as `delta^2`. It is carried by the mixed entries, and within them **mostly by the pole
  term** (70% to 95% of the first-order effect), with the archimedean kernel second and of opposite sign. The
  combs carry none of it (exact, lemma 4.1).
- **Q1 (learning rate along the prime-content axis at matched information).** At matched prime-power count `m`
  ({2}: m = A; {2,3}: m = 2A; {2,3,5}: m = 3A), the eigenvector restricted to already-seen places changes by
  `1 - overlap = O(delta^2)`. The numbers are in 4.4, and `delta` itself is forced down to `~1/(max ratio)`, so for
  m = 12 ({2,3,5}, A = 4) the change is 1e-6 to 1e-10. Nothing in this channel contracts like `e^{-4 pi x}`. There
  is no zero-location signal to contract: the lattice-bump forms are a Kronecker sum plus O(delta), and their
  minimal eigenvalue is a self-energy minus comb depths. The dilation-channel comparison is left to the synthesis
  (lane A1's numbers were not read).

## 6. Comparison step: zeros used here only (A2.4; labelled; output Section 7)

The explicit formula in this normalisation is `Psi(F) = sum_rho Fhat(i(rho - 1/2))`. For
`F = phi_alpha^* * phi_beta`, `Fhat(t) = conj(phihat_alpha(tbar)) phihat_beta(t)`. This is the brief's
`sum_rho phihat_alpha(rho) conj phihat_beta(1 - rhobar)` up to which slot carries the conjugate, and the two agree
here since everything is real. With the zeros used as returned (`rho = 1/2 + i gamma`):
`Z_M(D) = sum_{k<=M} 2 cos(gamma_k D) phihat_delta(gamma_k)^2`. The zeros come from `acb.zeta_zeros`: 2000 certified
zeros, `gamma_2000 = 2515.2865`. `phihat_1` is a certified arb integral.

| delta | r (D) | prime powers in the entry | \|Psi - Z_M\| for M = 10, 100, 1000, 2000 |
|---|---|---|---|
| 0.1 | 1 (0) | none | 3.3e-4, 7.7e-7, 1.4e-13, 3.4e-17 |
| 0.1 | 2 | 2 | 6.7e-5, 1.1e-7, 9.7e-15, 2.7e-18 |
| 0.1 | 3 | 3 | 9.0e-5, 1.2e-7, 1.9e-14, 3.5e-18 |
| 0.1 | 3/2 | none | 1.8e-6, 4.0e-9, 4.8e-15, 4.8e-20 |
| 0.1 | 6 | 5, 7 (non-admissible delta) | 2.7e-7, 5.7e-8, 4.2e-15, 8.0e-19 |
| 0.1 | 8 | 7, 8, 9 (non-admissible delta) | 6.5e-6, 3.1e-8, 5.6e-15, 1.0e-18 |
| 0.05 | 1 (0) | none | 1.8e-3, 9.7e-6, 1.5e-10, 3.4e-13 |
| 0.05 | 2 | 2 | 1.7e-4, 1.3e-6, 1.3e-11, 2.6e-14 |
| 0.05 | 3/2 | none | 2.2e-4, 4.1e-7, 8.2e-14, 6.2e-15 |
| 0.05 | 6 | none | 4.1e-4, 1.8e-7, 3.6e-13, 3.6e-15 |

At M = 2000 the relative error `|Psi - Z_2000|/(|Psi| + ||phi||^2)` is 3e-18 to 2e-15 for delta = 0.1 and 5e-13 to 2e-11 for delta = 0.05. The entries
are of size 1e-3.

**Truncation law.** The tail is `sum_{gamma > gamma_M} 2 cos(gamma D) phihat_delta(gamma)^2`. The Fourier transform
of this bump satisfies `|phihat_1(tau)| ~ C tau^{-3/4} e^{-sqrt tau}` (saddle point at the edge), so the error
envelope is `~ exp(-2 sqrt(delta gamma_M))` times a power. A fitted slope of `log max_r |Psi - Z_M|` against
`sqrt(delta gamma_M)` for M = 30..1000 gives -2.23 (delta = 0.1) and -2.27 (delta = 0.05). The excess over -2 is the
power-law prefactor together with the growth of the zero density. For D = 0 the error equals the absolute tail, since
all terms are positive. For D != 0 the oscillating `cos(gamma D)` makes it up to about 10^3 times smaller than the absolute
tail. Consequence for the channel: resolving the admissible `delta` of `{2,3,5}, A = 3` (3.7e-5) on the zero side
would need `2 sqrt(delta gamma_M) >~ 23` for 1e-10, i.e. `gamma_M >~ 130/delta ~ 3.5e6`: out of reach of a
zero list and far beyond the prime side's cost. The zero side of these forms is the explicit formula's
high-frequency sum.

## 7. Precision statement (A2.5)

python-flint 0.9.0 installed from PyPI; arb balls at 200 bits.

- **Certified (arb):**
  - `mu_i` (up to i = 400 as needed), `R_1(0)`, `R_1(s)`, `c_delta`: `acb.integral` on `[-1 + eps, 1 - eps]`, plus
    the rigorous bound `eps phi_1(1 - eps) <= eps 2^-220` for each omitted end;
  - pole and prime terms;
  - the off-diagonal archimedean term: Taylor series of `rho` at D via `arb_series`, plus a Cauchy tail bound on
    `|y - D| = (D + 2 delta)/2` using `|rho(y)| <= e^{Re y/2}/(2 sinh Re y)` and `|Mt_j| <= 2^j mu_0^2`;
  - the `rho_reg` Taylor coefficients, with a Cauchy bound on `|y| = 3` (720 covering balls, max 6.69);
  - the eigenvalue enclosures relative to the entry balls: residual bound on a refined vector, plus the inertia of
    a ball `LDL^T` of `G - s I` (exactly one negative pivot), plus a Davis-Kahan angle bound;
  - the zeros in section 6 (`acb.zeta_zeros`).
- **Not certified:** `T_1` and the odd `At_j`, which enter only the diagonal `d`. They are tanh-sinh sums on `[0, 2]`
  (1177 nodes, |u| <= 4.6) over **certified** ball values of `R_1` at the nodes. Level doubling (h = 1/64 to 1/128)
  moves `T_1` by 2.6e-56 and the `At_j` by up to 2.3e-45 relative at j = 100. The balls carry 10x these differences.
  The effect on the normalised diagonal is <= 2.2e-56 from the `At_j` and 2.7e-55 from `T_1`. The even `At_j` from
  the same nodes agree with the certified moment formula to 6.3e-56 relative (a validation of the node table), and
  `At_0 = mu_0^2` holds to 1.6e-58. Since `d` is one number shared by all entries at fixed delta, its uncertainty is
  a multiple of the identity: it moves no eigenvector and no gap between two forms at the same delta.
- **Consistency check (section 2):** `mpmath.quad` at 60 digits with its error estimates (<= 1e-63). The
  bump-formula cross-check (section 3) uses the same quadrature over certified `R_1`.
- numpy is used only for starting vectors (single-threaded BLAS). Every printed number comes from arb.

Disclosure of check changes made during development (no tolerance was loosened to make a claim pass):

- the expected `rho_reg'(0) = -1/12` was my arithmetic slip. Re-derived by hand, the value is `-1/48`, which the
  series gives.
- the a-priori check "every At_j moves by < 1e-45 relative under level doubling" failed (2.3e-45 at j = 100). It
  was replaced by the check that matters: the propagated effect on the diagonal is <= 2.2e-56. The 2.3e-45 figure
  is printed.

## 8. Findings against the brief

1. **The Correction's claim is partly wrong** (metric-as-state section 3(a), repeated in brief A2.3 decomposition 2).
   The claim: "the cross-place information of the two-prime channel is carried entirely by the archimedean kernel
   sampled at logarithms of S-smooth rationals". In fact, the mixed entries are **pole plus archimedean**:
   `W_{0,2}` gives `2 cosh(D/2) c_delta^2`, which is non-zero at every `D`. The pole part dominates, with 2.4 to 21
   times the archimedean first-order effect and the opposite sign, growing with the lattice (about `e^{D}` per entry). It
   is also what keeps the smallest two-prime form positive (4.3(b)). What I did: split decomposition 2 into
   "mixed pole removed" and "mixed arch removed", and report both.
2. **Decomposition 1 is ill-defined as written.** The "block-diagonal restriction to the axis subspaces" has two
   problems: the axis subspaces share the origin, and the off-axis test functions belong to no axis subspace. What
   I did: report `G_X` (the principal submatrix on the union of the axes) and `G_bd` (the direct sum of the
   one-prime forms, each with its own origin), both against `G`. The better-posed "decoupled places" comparison is
   decomposition 2, which by lemma 4.1 is *exactly* the Kronecker sum of the one-prime forms. The brief does not
   note this identity. It turns the three decompositions into one statement:
   `lambda(G) = d + sum_p (comb depth) + O(delta)`.
3. **Admissibility forces a perturbative, short-support regime.** `delta_max` falls like the reciprocal of the
   largest lattice ratio: 1.2e-6 at `{2,3,5}, A = 4`, and the binding pairs are ratios next to primes (13500/13499,
   405000/405001). All inter-place effects are then O(delta) in eigenvalues and O(delta^2) in eigenvectors. The
   expectation in metric-as-state section 6, that "the two-prime forms will show the first nontrivial eigenvector",
   is not borne out: the minimal eigenvector is a product state up to a Schmidt defect of 3e-3 to 6e-9. "A = 1, 2,
   3, ... as affordable" is limited by delta, not by cost: A = 4 with 125 test functions runs in seconds. To see
   inter-place structure at O(1), the channel would need test functions whose supports overlap prime powers other
   than the ratio, that is, a non-admissible delta with the full prime sum. The implementation handles that
   (sections 3 and 6 exercise it), but it is not the brief's protocol.
4. **A2.5 underestimates the archimedean term.** The brief calls it "one integral against a smooth compactly
   supported function, so control is straightforward". For this test class `F = phi^* * phi` has no closed form.
   The diagonal needs a finite-part (log-singular) integral of it. Arb cannot integrate across the bump's essential
   singularity at the support edge without an explicit truncation bound. What I did: certify everything except two
   diagonal constants (`T_1`, the odd `At_j`), and state that their error is a scalar multiple of the identity
   (section 7).
5. **Consistency-check logistics.** zst's driver and `test_ab` print no `(a_n, b_n)`: `test_ab` compares internally
   and prints PASS/FAIL. What I did: a 20-line C printer linked against `zst/build/libzst.a` is compiled at run
   time in a temporary directory. zst is not modified.
6. **Conventions, minor.**
   - The brief says the window `[lambda^-1, lambda]` is `[0, L]` in `x = log u`. It is `[-L/2, L/2]`; `[0, L]` is
     the paper's `x = log(lambda u)`. This is harmless by translation invariance (Lemma `qtrans`).
   - "The Problem" writes `G_ij = W(f_i * f~_j)` with `f~(u) = u^{-1} f(1/u)`, a Mellin-side convention. The
     Conventions section fixes `QW(f, g) = Psi(f^* * g)`, and I followed that.
   - A2.1 centres `phi_alpha^* * phi_beta` at `log(n_alpha/n_beta)`. With this convolution it is
     `log(n_beta/n_alpha)`. Only `|D|` enters.
   - A2.4's zero sum is in the Mellin normalisation. The unitary form used here is stated in section 6.
7. **Round question 1 cannot be answered from this lane alone in the form asked.** The prime-content channel has no
   zero-location signal that contracts. Its only "learning" is the O(delta^2) movement in 4.4, at a delta that
   admissibility ties to the lattice. A comparison with the `e^{-4 pi x}` law of the dilation channel at matched
   prime-power count is therefore a comparison with something structurally different. I give the numbers (4.4,
   section 5) and leave the synthesis to the orchestrator.
