# Numerics lane: Deninger's package on the GL_1 bond (`notes/deninger-bond/astra-proofs.md`)

Lane: `claude:fable-5.1` (numerics fork, 2026-09-22), independent of the author's `checks/` scripts (not read).
Script `scripts/deninger_bond.py`, output `outputs/deninger_bond.txt`. 51 checks, 51 pass, 0 fail; runtime 60.6 s. Zeros from `data/zeros3000.npy`
(float64, 3000 positive ordinates), mpmath at 40 digits for the analytic side, sympy `factorint` for von Mangoldt.

## Ledger

| Item | Result | Check | Value |
|---|---|---|---|
| D01 | PASS | first three ordinates from mpmath.zetazero vs data file ['14.13472514173469379046', '21.02203963877155499263', '25.01085758014568876321'] |  |
| D02 | PASS | data file: 3000 positive ordinates, last one np.float64(3533.3282433958198) |  |
| D03 | PASS | d_n = e^{-1/4 - i gamma_n/2} at t = 1 against the table (8.1) [(0.551367248054149-0.550022560888031j), (-0.362776434403421+0.689147239967029j), (0.777355034172436+0.047432167981283j)] |  |
| D04 | PASS | D^T Omega D = e^{-1/2} Omega on the six modes maxerr=2.60e-17 |  |
| D05 | PASS | D^T G conj(D) = e^{-1/2} G with G = I (first-slot-linear Hermitian convention) |  |
| D06 | PASS | Omega J R_c = I_6 |  |
| D07 | PASS | /d_n/ = e^{-1/4} for all six modes e^-1/4=0.778800783071404878 |  |
| D08 | PASS | energy Gram (8.2) M_ab = 2/(1+i(s_a-s_b)) equals the direct integral of the modes maxerr=1.4e-17 |  |
| D09 | PASS | energy Gram is NOT a q_t-similitude: off-diagonal residual of D^T M conj(D) - e^{-1/2} M max residual=0.4956, diagonal residual=2.3e-16 |  |
| D10 | PASS | jet pairing (2.1) is an e^{-t/2}-similitude for chains of length 1..4 (synthetic partner pair rho, 1-rho) max residual=2.4e-16 |  |
| D11 | PASS | (2.1) applied to both orderings is alternating: Omega(e_nu,k, e_rho,j) = -Omega(e_rho,j, e_nu,k) |  |
| D12 | PASS | reality: coefficient at conj(rho) is the conjugate of the coefficient at rho, m = 1..4 |  |
| D13 | PASS | all-time invariant Hermitian forms on six simple critical modes: real dimension 6 (one weight per mode) dim=6 |  |
| D14 | PASS | off-line quartet {rho,1-rho,conj rho,1-conj rho}, rho=0.7+3.1i: invariant Hermitian forms have zero diagonal (no positive metric), pairing rho with 1-conj(rho) dim=4 (two complex off-diagonal entries) |  |
| D15 | PASS | double critical zero (length-two jet chain): every invariant Hermitian form has G(e_0,e_0) = 0, hence none is positive definite dim=2 (G_11 free, G_01 imaginary, G_00 = 0) |  |
| D16 | PASS | rescaled jet norm e^{t/2}//C_t e_1//^2 grows like t^2 (ratio at t=40 vs t=20 close to 4) ratio=3.9925 |  |
| D17 | PASS | (3.5): Omega(u,v) = -1, Ju = -v, Jv = u, G_J(u,u) = G_J(v,v) = 1, G_J(u,v) = 0 Omega(u,v)=-1.000+0.000j, G_J(u,u)=1.000+0.000j, G_J(v,v)=1.000+0.000j |  |
| D18 | PASS | u, v are real vectors (fixed by the real structure R) |  |
| D19 | PASS | (3.3)-(3.4): J = -L R^{-1} from a weighted certificate G gives J^2 = -I, J^T Omega J = Omega, Omega J = G R > 0 Omega J = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0] ... (compatible metric is I regardless of the weights) |  |
| D20 | PASS | compatible metric Omega J = I_6 for every positive certificate G (weights change R, not Omega J) |  |
| D21 | PASS | closest pair among 3000 zeros: /<u_gamma,u_delta>/ = (1/2)/sqrt((a-a')^2+1/4) equals the Gram modulus gamma=1977.173944, delta=1977.271446, gap=0.097503, r=0.995280 |  |
| D22 | PASS | (4.4): e^{t*/4}//C_{t*} f/////f// = sqrt((1+r)/(1-r)) for f = u - c v at t* = 2 pi//gamma - delta/ value=20.560930, t*=64.441 |  |
| D23 | PASS | cluster overlap bound: /a - a'/ <= 1 gives squared overlap >= 1/5 0.200 |  |
| D24 | PASS | biorthogonal vector norm //b_u// = (1 - r^2)^{-1/2} for a unit pair with overlap r //b_u//=10.3048 |  |
| D25 | PASS | F_f(s) = e^{a(s-1/2)^2/4} is the transform int f(t) e^{(s-1/2)t/2} dt (s = 0.3 + 0.8i) |  |
| D26 | PASS | h = f * f~ equals (8 pi a)^{-1/2} e^{-t^2/(8a)} at t = 0.37 |  |
| D27 | PASS | F_h(s) = F_f(s) conj(F_f(1 - conj s)) equals the transform of h at s = 0.3 + 0.8i |  |
| D28 | PASS | W_3000(f) = 2 sum e^{-a gamma^2/2} over the 3000 positive ordinates (8.3) 0.29939602250755907983 |  |
| D29 | PASS | (5.3) even terms F_h(0)+F_h(1) = 2 e^{a/8} 2.0050062552115901699 |  |
| D30 | PASS | (5.3) -2 log(pi) h(0) -3.2292233878602183844 |  |
| D31 | PASS | (5.3) gamma integral (1.5236299541478742838 + 0.0j) |  |
| D32 | PASS | (5.3) prime powers n <= 1000 -1.67989916869e-5 |  |
| D33 | PASS | explicit formula: analytic side (5.3) minus the zero sum over 3000 zeros total=(0.29939602250755915579 + 0.0j), difference=(7.5956e-17 + 0.0j) |  |
| D34 | PASS | W(f,g) = conj(W(g,f)) on 400 zero pairs for Gaussians a = 1/50, 1/80 |  |
| D35 | PASS | p=5: primary associates pi = 1 mod (1+i)^3 are a conjugate pair; the one with Im > 0 is (-1+2j) [(-1-2j), (-1+2j)] |  |
| D36 | PASS | p=5: #E(F_p) = P(1) = /pi-1/^2 = 8 (trace -2) by exhaustive count N1=8 |  |
| D37 | PASS | p=5: #E(F_p^2) = /pi^2-1/^2 = 1 + p^2 - pi^2 - conj(pi)^2 by exhaustive count over F_(p^2) N2=32, /pi^2-1/^2=32 |  |
| D38 | PASS | p=5: A^T A = p I, A^T Omega_T A = p Omega_T, A J_T = J_T A, G_T = Omega_T J_T = I |  |
| D39 | PASS | p=5: (7.2) exp(sum #Fix(f^n) u^n/n) = (1-pi u)(1-conj(pi) u)/((1-u)(1-pu)) to order 8, #Fix = det(A^n - I) #Fix=[8, 32, 104, 640] |  |
| D40 | PASS | p=13: primary associates pi = 1 mod (1+i)^3 are a conjugate pair; the one with Im > 0 is (3+2j) [(3-2j), (3+2j)] |  |
| D41 | PASS | p=13: #E(F_p) = P(1) = /pi-1/^2 = 8 (trace 6) by exhaustive count N1=8 |  |
| D42 | PASS | p=13: #E(F_p^2) = /pi^2-1/^2 = 1 + p^2 - pi^2 - conj(pi)^2 by exhaustive count over F_(p^2) N2=160, /pi^2-1/^2=160 |  |
| D43 | PASS | p=13: A^T A = p I, A^T Omega_T A = p Omega_T, A J_T = J_T A, G_T = Omega_T J_T = I |  |
| D44 | PASS | p=13: (7.2) exp(sum #Fix(f^n) u^n/n) = (1-pi u)(1-conj(pi) u)/((1-u)(1-pu)) to order 8, #Fix = det(A^n - I) #Fix=[8, 160, 2216, 28800] |  |
| D45 | PASS | p=17: primary associates pi = 1 mod (1+i)^3 are a conjugate pair; the one with Im > 0 is (1+4j) [(1-4j), (1+4j)] |  |
| D46 | PASS | p=17: #E(F_p) = P(1) = /pi-1/^2 = 16 (trace 2) by exhaustive count N1=16 |  |
| D47 | PASS | p=17: #E(F_p^2) = /pi^2-1/^2 = 1 + p^2 - pi^2 - conj(pi)^2 by exhaustive count over F_(p^2) N2=320, /pi^2-1/^2=320 |  |
| D48 | PASS | p=17: A^T A = p I, A^T Omega_T A = p Omega_T, A J_T = J_T A, G_T = Omega_T J_T = I |  |
| D49 | PASS | p=17: (7.2) exp(sum #Fix(f^n) u^n/n) = (1-pi u)(1-conj(pi) u)/((1-u)(1-pu)) to order 8, #Fix = det(A^n - I) #Fix=[16, 320, 5008, 83200] |  |
| D50 | PASS | (7.5): J_T omega_+ = -i omega_+, J_T omega_- = i omega_-, Omega_T(omega_+, omega_-) = -i, G_T(omega_+, omega_+) = G_T(omega_-, omega_-) = 1, cross term 0 |  |
| D51 | PASS | (7.5): pullback A^T (p = 5) has omega_+ , omega_- as eigenvectors with eigenvalues pi, conj(pi) (up to the stated transpose convention) A omega_+ = [(-0.707107-1.414214j), (1.414214-0.707107j)], A^T omega_+ = [(-0.707107+1.414214j |  |

## Findings

- **F1 (all displayed formulas reproduce).** The six-mode matrices (8.1) satisfy `D^T Omega D = e^(-1/2) Omega`,
  `D^T G conj(D) = e^(-1/2) G`, `Omega J R_c = I` to machine precision; the table of `d_n` agrees to 1e-15. The
  energy Gram (8.2) equals the direct mode integral (1.4e-17) and is *not* a similitude (max residual 0.4956 off the
  diagonal, 2e-16 on it), as stated.
- **F2 (jet pairing (2.1)).** For chains of length 1–4 at a synthetic partner pair `rho = 0.7 + 3.1i`, `1 - rho`,
  the anti-diagonal pairing is an exact `e^(-t/2)`-similitude (residual 2e-16 at three times), alternating, and
  real in the stated sense.
- **F3 (positive-metric criterion, C3).** On six critical simple modes the all-time invariant Hermitian forms are
  the six diagonal weights (real dimension 6). On the off-line quartet `{rho, 1-rho, conj rho, 1-conj rho}` the
  invariant forms pair `rho` with `1 - conj(rho)` only and have zero diagonal (dimension 4, none positive). For a
  double critical zero the eigenvector's diagonal entry is forced to zero (the solution space is `G_11` free and
  `G_01` imaginary, dimension 2, none positive definite); the rescaled jet norm grows like `t^2` (ratio 3.99 between
  `t = 20` and `t = 40`). A first version of this check asserted "only `G = 0`", which is stronger than the proofs
  claim and is false (semidefinite forms survive); the proofs' statement "no positive metric" is what holds.
- **F4 (the star and (3.3)).** (3.5) verified; the construction `J = -L R^(-1)` from a weighted certificate
  `G = diag(1, 1, 2.5, 2.5, 0.3, 0.3)` in the real `(u, v)` basis gives `J^2 = -I`, `J^T Omega J = Omega`, and
  `Omega J = G R = I_6` independent of the weights, confirming Section 3.3's distinction between certificates and the
  compatible metric.
- **F5 (C4, (4.4)).** The closest pair among the 3000 zeros is `gamma = 1977.173944`, `delta = 1977.271446` (gap
  0.0975), overlap `r = 0.995280`; at `t* = 2 pi/(delta - gamma) = 64.44` the rescaled two-mode ratio is
  `sqrt((1+r)/(1-r)) = 20.56`, exactly as (4.4). The biorthogonal norm `(1 - r^2)^(-1/2) = 10.30` also reproduces.
- **F6 (Weil form, (5.3)).** With the Gaussian `a = 1/50`: zero side `W_3000 = 0.29939602250755908`; analytic side
  `2.0050062552115901699 - 3.2292233878602183844 + 1.5236299541478742838 - 0.0000167989916869 = 0.29939602250755916`,
  difference `7.6e-17` (float64 zero data), matching the author's `-7.60e-17` in modulus (sign convention of the
  difference). The transform identities `F_f`, `h = f * f~`, `F_h = F_f conj(F_f(1 - conj s))` verified by quadrature
  to 1e-25; `W(f, g) = conj W(g, f)` on 400 zero pairs.
- **F7 (CM torus, C7).** For `y^2 = x^3 - x` at `p = 5, 13, 17` the primary associates `pi = 1 mod (1+i)^3` with
  `Im > 0` are `-1+2i, 3+2i, 1+4i`; exhaustive counts give `#E(F_p) = 8, 8, 16 = |pi - 1|^2` and
  `#E(F_(p^2)) = 32, 160, 320 = |pi^2 - 1|^2`; `A^T A = pI`, `A^T Omega_T A = p Omega_T`, `A J_T = J_T A`,
  `G_T = I`; (7.2) holds to order 8 with `#Fix(f^n) = det(A^n - I)`; (7.5) verified, with `omega_+` an eigenvector
  of the pullback `A^T` (not of `A`) for eigenvalue `pi`, consistent with the transpose remark in 7.1.

No discrepancy with the proofs was found. Runtime 60.6 s.
