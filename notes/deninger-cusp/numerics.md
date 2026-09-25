# Numerics lane: deninger-cusp (2026-09-22)

Author: `claude:fable-5.1` (numerics lane, independent of `notes/deninger-cusp/checks/`, which was not read).
Script `scripts/deninger_cusp.py` (mpmath at 25 digits for all L-function quantities; numpy double precision
for the two-dimensional Gaussian lattice sums); output `outputs/deninger_cusp.txt`. === 163/163 checks pass; runtime 115.0 s ===

Tested: the displayed formulas of `astra-proofs.md` D3 ((D3.5)–(D3.13), (D3.16)), D4 ((D4.1)–(D4.12)),
D5 ((D4.11), (D5.11), (D5.13), (N.3), (N.4)) and N5 ((N.5), (N.6)), plus the items requested by the brief:
`Phi(s)Phi(1-s) = I` at `s = 0.7+0.3i` for `N = 5` (quadratic), `7` and `13` (even characters of order 3 and 6)
and for the full four-cusp `Gamma_1(5)` matrix; the determinant against the product of `Lambda`-ratios; the
residue at `s = 1` and its rank; the twisted Siegel-theta constant terms at `y = 1.3`, `t = 0.7` by direct
lattice summation (`|m| <= 14..16`, `|n| <= 260..400`, 96-point midpoint rule in `x`, error `< 4e-16`) at both
cusps; `|Theta_chi| = 1` on the real line and `< 1` on a 24-point grid in the upper half-plane; the first two
zeros of `L(s, (./5))` as modes.

## Findings

- **F1 (all reproduced).** Every displayed number of N1–N5 reproduces to the printed precision (12 decimals
  for the tables, 21 for the zero ordinates); every identity holds to `1e-20` or better in mpmath, `4e-16`
  for the double-precision lattice sums.
- **F2 (astra's (D3.5) two forms).** The first form `q^(1/2-s) Lambda_psi(2s-1)/Lambda_psi(2s)` and the second
  form with `sqrt(pi) Gamma(s-1/2)/Gamma(s)` coincide for even `psi` (checked at all six table points). For the
  odd diagnostic (N.1) only the first form is meaningful (the second uses the even Gamma factor); with the
  first form the (N.1) entries and `B(s)B(1-s) = I` reproduce exactly, as astra states.
- **F3 (numerical pitfall, not a discrepancy).** `mp.quad` on `[0, inf]` for the mode transform
  `int_0^inf e^{(-1/4 - i gamma/2 + i tau) X} dX` is inaccurate (errors `5e-7`, `2e-4`) because of the slow
  oscillatory decay; a subdivided integral over `[0, 300]` reproduces `i/(tau - conj w_j)` to `1e-26`.
- **F4 (odd character).** The unsigned twisted lattice sum for `chi_{5,1}` vanishes identically in double
  precision (`< 1e-14`), confirming D4.2; the GL_1 replacement `theta_{chi,1}` satisfies (D4.8) with the odd
  completion to `1e-15` at `u = 0.7 + 0.3i`, and (N2)'s value `1.390329535856 + 0.747945730562i` reproduces.
- **F5 (Eisenstein spectra).** The eigenvalue multiset `{p+1} u {chi_1(p) + p chi_2(p)}` over the pairs
  `(1, chi)`, `(chi, 1)`, `chi` even nontrivial mod 11 (derived independently, four characters of order 5),
  equals the roots of astra's closed form (N.6) for `p = 2, 3` to `5e-22`, with trace `4(p+1)`, so
  `T_p != (p+1) I` on `Eis`.
- **F6 (asymptotic (D4.12)).** `Theta_chi(iv)/(eps sqrt(pi/(f v))) = 1.0031298` at `v = 40` for all three
  characters (the `O(1/v)` Stirling correction, identical across `f` as it should be).

Nothing in the proofs file failed to reproduce.

## Ledger (163 checks, 163 pass)

| id | verdict | check |
|---|---|---|
| D01 | PASS | chi_{5,2} is the Legendre symbol mod 5 |
| D02 | PASS | chi_{7,2} even of order 3 |
| D03 | PASS | chi_{13,2} even of order 6 |
| D04 | PASS | chi_{5,1} odd, chi(2) = i |
| D05 | PASS | Dirichlet FE Lambda_chi(s) = eps Lambda_barchi(1-s), chi_{5,2} 8.23e-26 |
| D06 | PASS | Dirichlet FE Lambda_chi(s) = eps Lambda_barchi(1-s), chi_{7,2} 1.73e-25 |
| D07 | PASS | Dirichlet FE Lambda_chi(s) = eps Lambda_barchi(1-s), chi_{13,2} 6.52e-25 |
| D08 | PASS | Dirichlet FE Lambda_chi(s) = eps Lambda_barchi(1-s), chi_{5,1} 1.83e-25 |
| D09 | PASS | root numbers eps: chi5 = 1 (1.0 + 9.82617042149e-26j) |
| D10 | PASS | root number chi7 = 0.895953219663-0.444148430342i (0.8959532196631 - 0.4441484303421j) |
| D11 | PASS | root number chi13 = 0.859542535099+0.511064213535i (0.8595425350988 + 0.5110642135348j) |
| D12 | PASS | (D3.6) table entry a, chi5, s=0.7+0.3i (0.5703962414778 - 0.3709877479189j) |
| D13 | PASS | (D3.6) table entry b, chi5, s=0.7+0.3i (0.5703962414778 - 0.3709877479189j) |
| D14 | PASS | (D3.7) Gauss-sum form = (D3.5), chi5, s=0.7+0.3i 7.75e-26 |
| D15 | PASS | (D3.5) both forms of A_psi agree for even psi, chi5, s=0.7+0.3i |
| D16 | PASS | (D3.9) Phi_psi(s)Phi_psi(1-s) = I, chi5, s=0.7+0.3i 9.07e-26 |
| D17 | PASS | (D3.6) det Phi_psi = -q^(1-2s) R_psi R_barpsi, chi5, s=0.7+0.3i |
| D18 | PASS | (D3.6) table entry a, chi5, s=1.2+0.4i (0.1881743972667 - 0.1800158890342j) |
| D19 | PASS | (D3.6) table entry b, chi5, s=1.2+0.4i (0.1881743972667 - 0.1800158890342j) |
| D20 | PASS | (D3.7) Gauss-sum form = (D3.5), chi5, s=1.2+0.4i 5.22e-26 |
| D21 | PASS | (D3.5) both forms of A_psi agree for even psi, chi5, s=1.2+0.4i |
| D22 | PASS | (D3.9) Phi_psi(s)Phi_psi(1-s) = I, chi5, s=1.2+0.4i 7.22e-26 |
| D23 | PASS | (D3.6) det Phi_psi = -q^(1-2s) R_psi R_barpsi, chi5, s=1.2+0.4i |
| D24 | PASS | (D3.6) table entry a, chi7, s=0.7+0.3i (0.4354386602347 - 0.4384824645853j) |
| D25 | PASS | (D3.6) table entry b, chi7, s=0.7+0.3i (0.499568861119 - 0.3712942965542j) |
| D26 | PASS | (D3.7) Gauss-sum form = (D3.5), chi7, s=0.7+0.3i 3.77e-26 |
| D27 | PASS | (D3.5) both forms of A_psi agree for even psi, chi7, s=0.7+0.3i |
| D28 | PASS | (D3.9) Phi_psi(s)Phi_psi(1-s) = I, chi7, s=0.7+0.3i 2.43e-25 |
| D29 | PASS | (D3.6) det Phi_psi = -q^(1-2s) R_psi R_barpsi, chi7, s=0.7+0.3i |
| D30 | PASS | (D3.6) table entry a, chi7, s=1.2+0.4i (0.100947189666 - 0.1569108099978j) |
| D31 | PASS | (D3.6) table entry b, chi7, s=1.2+0.4i (0.1230840436388 - 0.1470157868313j) |
| D32 | PASS | (D3.7) Gauss-sum form = (D3.5), chi7, s=1.2+0.4i 2.33e-26 |
| D33 | PASS | (D3.5) both forms of A_psi agree for even psi, chi7, s=1.2+0.4i |
| D34 | PASS | (D3.9) Phi_psi(s)Phi_psi(1-s) = I, chi7, s=1.2+0.4i 1.6e-25 |
| D35 | PASS | (D3.6) det Phi_psi = -q^(1-2s) R_psi R_barpsi, chi7, s=1.2+0.4i |
| D36 | PASS | (D3.6) table entry a, chi13, s=0.7+0.3i (0.3360619442777 - 0.4028335970273j) |
| D37 | PASS | (D3.6) table entry b, chi13, s=0.7+0.3i (0.2518449784188 - 0.4535219263969j) |
| D38 | PASS | (D3.7) Gauss-sum form = (D3.5), chi13, s=0.7+0.3i 7.81e-26 |
| D39 | PASS | (D3.5) both forms of A_psi agree for even psi, chi13, s=0.7+0.3i |
| D40 | PASS | (D3.9) Phi_psi(s)Phi_psi(1-s) = I, chi13, s=0.7+0.3i 1.44e-25 |
| D41 | PASS | (D3.6) det Phi_psi = -q^(1-2s) R_psi R_barpsi, chi13, s=0.7+0.3i |
| D42 | PASS | (D3.6) table entry a, chi13, s=1.2+0.4i (0.04052123577272 - 0.09844023004843j) |
| D43 | PASS | (D3.6) table entry b, chi13, s=1.2+0.4i (0.0243399464159 - 0.09939643285893j) |
| D44 | PASS | (D3.7) Gauss-sum form = (D3.5), chi13, s=1.2+0.4i 9.69e-27 |
| D45 | PASS | (D3.5) both forms of A_psi agree for even psi, chi13, s=1.2+0.4i |
| D46 | PASS | (D3.9) Phi_psi(s)Phi_psi(1-s) = I, chi13, s=1.2+0.4i 8.0e-26 |
| D47 | PASS | (D3.6) det Phi_psi = -q^(1-2s) R_psi R_barpsi, chi13, s=1.2+0.4i |
| D48 | PASS | Phi_psi unitary on Re s = 1/2 (tau = 1.7), chi5 5.48e-26 |
| D49 | PASS | Phi_psi unitary on Re s = 1/2 (tau = 1.7), chi7 3.88e-26 |
| D50 | PASS | Phi_psi unitary on Re s = 1/2 (tau = 1.7), chi13 4.67e-25 |
| D51 | PASS | (D3.10) A_psi(1) = pi/q L(1,psi)/L(2,psi), regular at s=1, chi5 (0.382936203162541 - 2.21333120443895e-26j) |
| D52 | PASS | (D3.10) A_psi(1) = pi/q L(1,psi)/L(2,psi), regular at s=1, chi7 (0.304559716356551 - 0.0203183974069055j) |
| D53 | PASS | (D3.10) A_psi(1) = pi/q L(1,psi)/L(2,psi), regular at s=1, chi13 (0.199607864326399 + 0.0163494338400264j) |
| D54 | PASS | (D3.11) trivial block d, q=5, s=0.7+0.3i (-0.7799566752048 - 0.08241680628375j) |
| D55 | PASS | (D3.11) trivial block o, q=5, s=0.7+0.3i (-0.2079022048511 - 0.4527500313743j) |
| D56 | PASS | (D3.11) Phi_1(s)Phi_1(1-s) = I, q=5, s=0.7+0.3i 3.69e-26 |
| D57 | PASS | (D3.12) det Phi_1, q=5, s=0.7+0.3i |
| D58 | PASS | (D3.12) phi_pm eigenvalues on (1,+-1), q=5, s=0.7+0.3i |
| D59 | PASS | (D3.11) trivial block d, q=5, s=1.2+0.4i (-0.1188714453389 - 0.1899878273538j) |
| D60 | PASS | (D3.11) trivial block o, q=5, s=1.2+0.4i (0.0705839927903 - 0.370524601121j) |
| D61 | PASS | (D3.11) Phi_1(s)Phi_1(1-s) = I, q=5, s=1.2+0.4i 2.71e-26 |
| D62 | PASS | (D3.12) det Phi_1, q=5, s=1.2+0.4i |
| D63 | PASS | (D3.12) phi_pm eigenvalues on (1,+-1), q=5, s=1.2+0.4i |
| D64 | PASS | (D3.13) Res_(s=1) Phi_1 = 3/(pi(q+1)) all-ones, q=5 0.159154943092 |
| D65 | PASS | (D3.13) Res_(s=1) Phi_1 = 3/(pi(q+1)) all-ones, q=7 0.119366207319 |
| D66 | PASS | (N3) q=5 trivial residue entry = 1/(2 pi) |
| D67 | PASS | Res_(s=1) phi = 3/pi |
| D68 | PASS | Gamma_1(5) 4x4 cusp-basis matrix: Phi(s)Phi(1-s) = I 1.04e-25 |
| D69 | PASS | (N3) Gamma_1(5) residue entries all 1/(4 pi) (0.0795774715458 + 0.0j) |
| D70 | PASS | (N3) Gamma_1(5) residue has rank one ['0.3183', '3.842e-13', '3.829e-13', '3.829e-13'] |
| D71 | PASS | (D3.16) det Phi_Gamma_1(5) formula (m = 2) 2.2e-26 |
| D72 | PASS | (N.1) formal odd-completion matrix B(0.7+0.3i) entries (0.5840130078601 - 0.3287653684253j) |
| D73 | PASS | (N.1) formal B(s)B(1-s) = I (algebraic only; not weight-zero scattering) |
| D74 | PASS | (N.1) odd eps = 0.850650808352+0.525731112119i (0.850650808352 + 0.5257311121191j) |
| D75 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi5, v=0.3 1.04e-25 |
| D76 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi5, v=0.5385 1.08e-25 |
| D77 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi5, v=2.5 2.4e-26 |
| D78 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi7, v=0.3 9.61e-26 |
| D79 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi7, v=0.5385 1.25e-25 |
| D80 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi7, v=2.5 9.32e-26 |
| D81 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi13, v=0.3 1.56e-25 |
| D82 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi13, v=0.5385 1.74e-25 |
| D83 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi13, v=2.5 9.69e-27 |
| D84 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi5odd, v=0.3 1.7e-25 |
| D85 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi5odd, v=0.5385 2.21e-25 |
| D86 | PASS | (D4.6)/(D4.8) Poisson theta_chi,a(v) = eps v^(-a-1/2) theta_barchi,a(1/v), chi5odd, v=2.5 5.18e-26 |
| D87 | PASS | odd chi: unsigned theta_chi(v) = 0 exactly |
| D88 | PASS | (N2) odd GL1 theta_{chi_{5,1},1}(0.7/1.3) = 1.390329535856+0.747945730562i (1.390329535856 + 0.7479457305616j) |
| D89 | PASS | (D4.8) (1/2) int theta_{chi,1}(v) v^((u+1)/2) dv/v = Lambda_chi(u), odd chi mod 5, u=0.7+0.3i 4.66e-26 |
| D90 | PASS | (N2) A_chi = theta_chi(t/y), chi5 (0.8228802941695 - 1.18526698208e-26j) |
| D91 | PASS | (N2) C_chi = sqrt(y/t) theta_chi(f t y), chi5 (0.1562385891669 + 2.936950558017e-27j) |
| D92 | PASS | (N2) B_chi = sqrt(y/t) theta_chi(t y), chi5 (1.246242825365 + 1.036717979696e-26j) |
| D93 | PASS | (D4.6) W A_chi = eps_chi B_barchi at (t,y), chi5 1.21e-25 |
| D94 | PASS | (N2) A_chi = theta_chi(t/y), chi7 (1.053699131048 - 0.4298802154008j) |
| D95 | PASS | (N2) C_chi = sqrt(y/t) theta_chi(f t y), chi7 (0.156253315445 - 2.550663024227e-5j) |
| D96 | PASS | (N2) B_chi = sqrt(y/t) theta_chi(t y), chi7 (1.509098455595 - 0.3976586101199j) |
| D97 | PASS | (D4.6) W A_chi = eps_chi B_barchi at (t,y), chi7 1.78e-25 |
| D98 | PASS | (N2) A_chi = theta_chi(t/y), chi13 (1.848617210324 + 0.6893062270462j) |
| D99 | PASS | (N2) C_chi = sqrt(y/t) theta_chi(f t y), chi13 (0.1562827679829 + 2.550663024227e-5j) |
| D100 | PASS | (N2) B_chi = sqrt(y/t) theta_chi(t y), chi13 (2.513603987405 + 0.7222937897604j) |
| D101 | PASS | (D4.6) W A_chi = eps_chi B_barchi at (t,y), chi13 6.46e-26 |
| D102 | PASS | (D4.3) int_0^1 T_chi(x+iy,t) dx = theta_chi(t/y), direct lattice sum, chi5 1.11e-16 |
| D103 | PASS | (D4.3) int_0^1 T_chi(W_f(x+iy),t) dx = sqrt(y/t) theta_chi(f t y), direct lattice sum, chi5 2.78e-17 |
| D104 | PASS | (D4.1) T_chi periodic in x with period one, chi5 0.0e+00 |
| D105 | PASS | (D4.3) int_0^1 T_chi(x+iy,t) dx = theta_chi(t/y), direct lattice sum, chi7 2.78e-16 |
| D106 | PASS | (D4.3) int_0^1 T_chi(W_f(x+iy),t) dx = sqrt(y/t) theta_chi(f t y), direct lattice sum, chi7 1.69e-20 |
| D107 | PASS | (D4.1) T_chi periodic in x with period one, chi7 0.0e+00 |
| D108 | PASS | (D4.3) int_0^1 T_chi(x+iy,t) dx = theta_chi(t/y), direct lattice sum, chi13 3.14e-16 |
| D109 | PASS | (D4.3) int_0^1 T_chi(W_f(x+iy),t) dx = sqrt(y/t) theta_chi(f t y), direct lattice sum, chi13 2.78e-17 |
| D110 | PASS | (D4.1) T_chi periodic in x with period one, chi13 0.0e+00 |
| D111 | PASS | (D4.2) odd chi: T_chi(z,t) = 0 identically (unsigned lattice sum) |
| D112 | PASS | (D4.7) (1/2) int A_chi(t;y) t^s dt/t = Lambda_chi(2s) y^s, chi5 8.03e-26 |
| D113 | PASS | (D4.7) (1/2) int B_chi(t;y) t^s dt/t = Lambda_chi(2s-1) y^(1-s), chi5 |
| D114 | PASS | (D4.4) physical edge (1/2) int C_chi t^s dt/t = f^(1/2-s) Lambda_chi(2s-1) y^(1-s), chi5 |
| D115 | PASS | (D4.4) edge quotient (physical/incoming) y^(2s-1) = A_chi(s) of (D3.5), chi5 |
| D116 | PASS | (D4.7) Lambda_chi(2s-1) = eps_chi Lambda_barchi(2-2s), chi5 |
| D117 | PASS | (D4.7) (1/2) int A_chi(t;y) t^s dt/t = Lambda_chi(2s) y^s, chi7 3.89e-26 |
| D118 | PASS | (D4.7) (1/2) int B_chi(t;y) t^s dt/t = Lambda_chi(2s-1) y^(1-s), chi7 |
| D119 | PASS | (D4.4) physical edge (1/2) int C_chi t^s dt/t = f^(1/2-s) Lambda_chi(2s-1) y^(1-s), chi7 |
| D120 | PASS | (D4.4) edge quotient (physical/incoming) y^(2s-1) = A_chi(s) of (D3.5), chi7 |
| D121 | PASS | (D4.7) Lambda_chi(2s-1) = eps_chi Lambda_barchi(2-2s), chi7 |
| D122 | PASS | (D4.9) \|Theta_chi\| = 1 on the real line (13 points), chi5 1.29e-25 |
| D123 | PASS | (D4.9) \|Theta_chi\| < 1 in the upper half-plane (24 grid points), chi5 0.96547 |
| D124 | PASS | (D4.10) Theta_chi = eps Lambda_chi(1+2i tau)/Lambda_chi(2i tau), chi5 |
| D125 | PASS | (D4.10) A_chi(1/2+i tau) = f^(-i tau) eps Theta_chi^(-1), chi5 1.23e-25 |
| D126 | PASS | (D4.12) Theta_chi(iv)/(eps sqrt(pi/(f v))) -> 1 (v=40, within 2%), chi5 (1.0031298 - 4.7289831e-26j) |
| D127 | PASS | (D4.9) \|Theta_chi\| = 1 on the real line (13 points), chi7 1.16e-25 |
| D128 | PASS | (D4.9) \|Theta_chi\| < 1 in the upper half-plane (24 grid points), chi7 0.954831 |
| D129 | PASS | (D4.10) Theta_chi = eps Lambda_chi(1+2i tau)/Lambda_chi(2i tau), chi7 |
| D130 | PASS | (D4.10) A_chi(1/2+i tau) = f^(-i tau) eps Theta_chi^(-1), chi7 7.31e-26 |
| D131 | PASS | (D4.12) Theta_chi(iv)/(eps sqrt(pi/(f v))) -> 1 (v=40, within 2%), chi7 (1.0031298 + 2.824869e-25j) |
| D132 | PASS | (D4.9) \|Theta_chi\| = 1 on the real line (13 points), chi13 7.75e-26 |
| D133 | PASS | (D4.9) \|Theta_chi\| < 1 in the upper half-plane (24 grid points), chi13 0.919758 |
| D134 | PASS | (D4.10) Theta_chi = eps Lambda_chi(1+2i tau)/Lambda_chi(2i tau), chi13 |
| D135 | PASS | (D4.10) A_chi(1/2+i tau) = f^(-i tau) eps Theta_chi^(-1), chi13 7.54e-26 |
| D136 | PASS | (D4.12) Theta_chi(iv)/(eps sqrt(pi/(f v))) -> 1 (v=40, within 2%), chi13 (1.0031298 - 3.6396439e-25j) |
| D137 | PASS | (D4.3) Lambda_chi(1+2i tau)/Lambda_chi(1-2i tau) is NOT unimodular for chi7 (astra's warning) 0.6777 |
| D138 | PASS | Theta_1 = xi(1+2i tau)/xi(1-2i tau) unimodular on R |
| D139 | PASS | Lambda_(./5)(1/2+it) is real (eps = 1) 3.34e-26 |
| D140 | PASS | first two zero ordinates of L(s,(./5)) (scan to 12) ['6.648453344727714716123', '9.831444432886669616348', '11.95884562608351453027'] |
| D141 | PASS | (N.3) gamma_1 = 6.648453344727714716123 6.648453344727714716123 |
| D142 | PASS | (N.3) gamma_2 = 9.831444432886669616348 9.831444432886669616348 |
| D143 | PASS | L(rho_j,(./5)) residuals |
| D144 | PASS | (D4.11) Theta_(./5)(w_1) = 0 at w = gamma/2 + i/4 2.6e-26 |
| D145 | PASS | (N.4) m_1(1.3) = y^(-1/4 - i gamma/2) (0.6023426169872 - 0.7171062620477j) |
| D146 | PASS | (D5.11) C_t m_1 = exp(-t/4 - i t gamma/2) m_1 |
| D147 | PASS | (N.4) kernel: hat m_1(tau) = i/(tau - conj w_1) 8.08e-28 |
| D148 | PASS | (D4.11) Theta_(./5)(w_2) = 0 at w = gamma/2 + i/4 5.58e-26 |
| D149 | PASS | (N.4) m_2(1.3) = y^(-1/4 - i gamma/2) (0.2597885941672 - 0.8997599155595j) |
| D150 | PASS | (D5.11) C_t m_2 = exp(-t/4 - i t gamma/2) m_2 |
| D151 | PASS | (N.4) kernel: hat m_2(tau) = i/(tau - conj w_2) 6.51e-27 |
| D152 | PASS | (D5.13) \|<k~, k~'>\| = 2b/sqrt((a-a')^2 + 4 b^2) for the two modes 0.2997260401 |
| D153 | PASS | p = 2: p = 2^1 mod 11 |
| D154 | PASS | (N.6) every eigenvalue of (N.5) is a root of the closed-form polynomial, p=2 4.99e-22 |
| D155 | PASS | (N.5) trace = 4(p+1) = 12, not 9(p+1), p=2 (12.0 - 1.9387046e-25j) |
| D156 | PASS | (N.5) dim Eis = 9 = h - 1 with h = 10 cusps of Gamma_1(11), p=2 |
| D157 | PASS | (N.5) the four listed conjugate pairs of T_2 eigenvalues |
| D158 | PASS | T_p on Eis is not (p+1) I, p=2 |
| D159 | PASS | p = 3: p = 2^8 mod 11 |
| D160 | PASS | (N.6) every eigenvalue of (N.5) is a root of the closed-form polynomial, p=3 3.68e-19 |
| D161 | PASS | (N.5) trace = 4(p+1) = 16, not 9(p+1), p=3 (16.0 - 1.7189847e-24j) |
| D162 | PASS | (N.5) dim Eis = 9 = h - 1 with h = 10 cusps of Gamma_1(11), p=3 |
| D163 | PASS | T_p on Eis is not (p+1) I, p=3 |
