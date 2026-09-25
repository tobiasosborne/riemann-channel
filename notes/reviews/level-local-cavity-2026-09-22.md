# REFUTE review: notes/level-local-cavity/astra-proofs.md

- Reviewer: `claude:fable-5.1` (hostile REFUTE protocol). Author: `codex:gpt-6-astra`. Date: 2026-09-22.
- Files reviewed: `notes/level-local-cavity/astra-brief.md`, `notes/level-local-cavity/astra-proofs.md` (L1–L5, corrections C1–C14,
  numerical checklist, closing table); cited shards `04i`, `04j`, `04k`, `04l`, `04r`, `09c`, `03f`, `02d`, `04p`, `04o`;
  `notes/deninger-cusp/astra-proofs.md` D3.2–D3.4, D5.1–D5.2; `refs/src/uetake-2007/paper.txt`.
- Independent checks: 105 numerical assertions in two scratch scripts written before opening the author's `checks/verify.py`
  (mpmath at 40 digits for the rational identities; a finite Blaschke disk model with 400 Fourier coefficients for the cascade
  algebra); 26 byte-cited line ranges read against the local files; the author's `checks/` were not consulted.

## L1 — VALID

- (1.1)–(1.3): `M_q(s)` from D3.11 equals the `z`-form with `z = q^{s-1/2}`; `H^T M H = diag(m_+, m_-)` with
  `m_± = 1/(z b_{∓a}(z))`; `det M = (1-q^{2-2s})/(1-q^{2s})`; `det M^{-1} = z^2(z^2-a^2)/(1-a^2z^2)`. All residuals `< 2e-40` at
  `q = 5, 7`, `s = 0.7+0.3i`.
- L1.2 (impossibility at the fixed cut): for a random symmetric 3-vertex core with two rays, `S(z) → W^*W - I` as `z → 0`
  (residual `1.7e-6` at `z = 1e-6`, `1.7e-9` at `1e-9`), while `M_{12} z → sqrt q` as `z → 0` (residual `1.6e-15` at `z = 1e-8`): `M` has a
  simple pole at `z = 0` and `det M` a double pole, so no fixed-cut `-Q^{-1}Q(1/z)` equals it. The argument is correct as
  stated for the fixed cut. One wording point: "constant basis changes and cusp-width scalings cannot remove this pole" is true
  for constant scalings, but the notebook's *height renormalisation* `D = diag(z^{a_1}, z^{a_2})` of `def:elliptic-cavity`
  (`04k:53`, and `04k:123–132`: moving the cut multiplies by `z^{2k}`) does remove it, which is exactly the author's own (1.10).
  The ledger row ("at the fixed 04k cut") is consistent; the sentence should name the exception.
- L1.3 (weighted-edge realisation): with `T = tF`, `W = I_2`, the direct Schur computation gives (1.6)–(1.7) exactly:
  `S_t = -z(I - tzF)^{-1}(zI - tF)`, `p_t = z^2(z^2-t^2)` from `det((1+z^2)I - zT - C)`, `det S_t = p_t/ptilde_t` (residuals `< 4e-40`);
  eigenchannels `-z b_a` on `(1,1)` and `-z b_{-a}` on `(1,-1)`; and (1.8) `M^{-1} = -D S_a D`, `M = -D S_a^{-1} D` to `7e-41`.
  The raw equality `M = S_a` fails by `1.506` (`q = 5`) and `1.664` (`q = 7`), matching the author's table.
- L1.4 (genuine cusp toy): (1.10) `S_{sqrt q} = -z^2 D M D` to `3e-41`; the bound equations `(λ - T - θC)x = 0` at `θ = ±a` on
  `(1, ±1)` hold exactly; the stabiliser bookkeeping (core edge index `q`, cusp junction `c^2 = S(v)/S(e) = 1`, degree `q+1`) is
  consistent with `04k:72–81`. The distinction "comb points are bound poles in the cusp toy, resonances in the funnel/inverse
  realisation" is a correct reading of the two determinants.
- L1.5: `Γ_0(q) ⊂ SL_2(Z_q)` fixes the standard lattice vertex and the adjacent line-vertex, so the tree quotient is not one edge;
  the orbit sizes `q^n` and the radial two-funnel weights (`a` on the central edge, standard rays) are right. The identification
  of the correct finite datum as the oldform matrix `B_q(1-s)B_q(s)^{-1}` reproduces D3.4 (`M_q = B(1-s)B(s)^{-1}` to `4e-42`).
- L1.6: comb zeros of `L_-` at `2πk/ℓ + i/2` and of `L_+` at `(2k+1)π/ℓ + i/2` (`k = -3..3`, residuals `< 3e-41`); `L_+(i/2) ≠ 0`;
  `(L_-/r)(i/2) = -log q/(q-1)` by a numerical limit (`-0.402359478108525`, `-0.324318358175886`, residual `< 5e-38`);
  `M_q(1) = (q+1)^{-1}` all-ones. Periods `3.90396253166234`, `3.22891851416156`.

## L2 — VALID

- (2.1) `K_{AB} = K_A ⊕ A K_B` with orthogonality: verified in the disk model (`A` degree two, `B` degree one) to `2e-16`.
- (2.10): the compressed shift on `K_{z b_c}` in the orthonormal basis `1, z sqrt(1-c^2)/(1-cz)` is `[[0,0],[sqrt(1-c^2), c]]`,
  `J_c = (-c, sqrt(1-c^2))`, `I - Z^*Z = J^*J`; verified from Fourier coefficients at `c = 0.3, -0.45` (residuals `< 3e-17`, the
  float input precision).
- (2.13) block structure: in the disk model with basis `(K_A, A K_B)`, the forward compression has zero upper-right block and a
  nonzero lower-left block (entries `0.164+0.247i`, `-0.827-0.158i`), i.e. `A K_B` is `Z`-invariant and arithmetic data feed the
  local factor; the adjoint has the transposed pattern. This is exactly the author's orientation statement.
- (2.15)–(2.16): `J^*1 = (I(w) - I(0))/w ∈ K_{AB}`, `||J||^2 = 1 - |I(0)|^2`, `J_{AB} f = conj(B(0)) J_A f` on `K_A`,
  `J_{AB}(Ag) = J_B g`, and the lower-left block equals `k_0^B J_A` with `k_0^B = 1 - conj(B(0))B` (all `< 4e-16`); `I - Z^*Z = J^*J`
  on the three-dimensional model to `7e-16`. (My first pass mis-implemented `J f` as `<wf, J^*1>` instead of `<f, J^*1>`; corrected,
  everything agrees.)
- (2.5), (2.7)–(2.8): Paley–Wiener gives `F^{-1}K_{e^{iℓτ}} = L^2(0,ℓ)`; the cell unitary makes `u` the unilateral shift on the
  sequence index and `b_c(u)` acts fiberwise, so `K_{B_c} = ker b_c(S)^* ⊗ L^2(0,ℓ) = span{(c^n)} ⊗ L^2(0,ℓ)` with normalisation
  `sqrt(1-c^2)`; the "disk degree two, half-plane fiber two, Hilbert dimension infinite" trichotomy is correct and is the
  right correction (C5) to the brief's "finite per period".
- (2.9): dividing by `r` removes one lift and breaks periodicity in `z`; correct.
- L2.4 unboundedness of the continuous trace on a model containing `L^2(0,ℓ)`: correct and elementary.

## L3 — VALID

- (3.1) at `N = 35`: `B_5(1-s)⊗B_7(1-s) · (B_5(s)⊗B_7(s))^{-1} = M_5 ⊗ M_7` to `5e-42`; `H⊗H` diagonalises it exactly; the four
  eigenvalues equal the products `m_{5,±} m_{7,±}` to `3e-41`; `det = (det M_5)^2 (det M_7)^2` to `1e-43`. One scalar `φ` before
  the determinant: agrees with D3.14–D3.15.
- (3.3) residual orders at `i/2`: `|L_5 L_7(i/2)| = 0.0833` (no zero) in `++`, one zero in `+-` and `-+` (cancelled by `r^{-1}`),
  two in `--` (one retained); matches the author's `0,0,0,1`.
- (3.6)–(3.7): `h_0(N) = Σ_{d|N} φ(gcd(d, N/d))` gives `4, 8` at `N = 35, 30` and `6 = q+1` at `25`, `1+4+4+1` pattern at `125`.
- L3.2 incommensurability of `log 5, log 7` and "state dimensions add, tensor states multiply": correct.
- L3.3 refutations: the Kronecker-sum-versus-product point for product adjacencies and the fixed-vertex obstruction are
  correct; the Boolean labelling is not `prop:cusps-are-class-group-bond` (`04p:67–69` is for `GL_2(O(C∖P_0))` over a finite
  field), as stated.

## L4 — VALID

- `(1/i) ∂_τ log(u b_c(u)) = ℓ[2 + 2Σ c^n cos(nℓτ)]` for `c = ±a` and the pair sum `4ℓ[1 + Σ q^{-m} cos(2mℓτ)]` at `τ = 0.23`:
  residuals `< 3e-50`. The 09c comb (`09c:78–100`) is `-P + A_arch` with `P(t) = Σ Λ(n)/n [δ(t - 2 log n) + δ(t + 2 log n)]`, so its
  `q`-part sits at `±2m log q` with weights `(log q) q^{-m}` and enters with a minus sign; the local phase transform has the same
  support with weights `2ℓ q^{-m}` plus a `4ℓ δ_0` atom. "Different objects, related by a phase derivative and Fourier
  transform" is correct; the sentence "has the q-prime-power support and weights" should say "up to the factor two, the sign,
  and the zero-time atom", which the author lists a line later.
- `09c:27–42`: the tower is `Π_j Z_Sel(v + j)` from the transverse Jacobian, not a congruence tower; the refutation of the
  brief's tower reading is correct, and the `q → q^n` substitution is rightly called speculation (and blocked by (3.7)).

## L5 — VALID

- The scope statements against `04l:13–18, 57` (H-LP not re-litigated), `04i:197–218` (thm:cusp-wave-contraction is
  `sketched`, radiation-space repair is a choice), `03f:29–49` (H-CUSP-BRIDGE open), `04r:167–172` and `04o:217–224` (next-round
  items) are accurate quotations of the notebook's own qualifications. The claim that 04k's Schur/`p/ptilde` theorem and 04l's
  disk model apply verbatim to `S_a` and `S_{sqrt q}` is verified by the direct computations above (`det S = p/ptilde` for
  `h = 2`, delays at `z = 0`, one nonzero resonance per channel for `S_a`, none for `S_{sqrt q}`).

## Source quotes

All 26 cited ranges checked and correct: `04k:49–53` (both quoted phrases), `04k:72–81`, `04k:91–107`, `04k:123–132`,
`04k:290–304`, `04i:103–112` (`φ = 1/R`), `04i:197–218`, `04i:241–246`, `04l:13–18`, `04l:22–28`, `04l:38–57`, `04l:57`,
`04j:12–47`, `04r:22–31`, `04r:44–52`, `04r:167–172`, `09c:27–42`, `09c:78–100`, `09c:125–138`, `03f:29–49`, `04o:217–224`,
`04p:67–81`, `02d:35–53`, `deninger-cusp:202–218, 265–282, 284–295, 438–456, 482–494, 496–500`, `h-theta:191–278, 698–743`,
`uetake-2007:615–629, 634–657, 676–680`.

## Verdict lines

VERDICT L1a: VALID
VERDICT L1b: VALID
VERDICT L2: VALID
VERDICT L3a: VALID
VERDICT L3b: VALID
VERDICT L4: VALID
VERDICT L5: VALID

## MINOR fixes (wording only; no MINOR verdict)

1. L1.2: replace "cusp-width scalings cannot remove this pole" by "constant scalings cannot; the height renormalisation
   `D S D` with `D = diag(z, z)` of `def:elliptic-cavity` does, and that is (1.10)".
2. L4: qualify "the q-prime-power support and weights" with "up to the factor two, the sign (dips) and the `4ℓ δ_0` atom".
3. Numerical checklist item 1: state that `z = q^{s-1/2}` at `s = 0.7 + 0.3i` has `|z| > 1`, so the identities are tested as
   rational identities, not as disk-model statements (the author says "outside the disk"; make it explicit that nothing about
   contractivity is tested there).

## Assessment

The corrected statements are sound and fully reproduced. The brief's central proposal (the local matrix `M_q` is the
fixed-cut scattering matrix of a finite two-cusp diagram, with the comb as its resonances and the constant as its bound
state) is correctly refuted: `M_q` has a pole at `z = 0`, which no fixed-cut core scattering has; what is true is that
`M_q^{-1}` is, up to the sign matrix `D`, the scattering of a two-funnel weighted edge of weight `q^{-1/2}` (comb points as
resonances, two delays, no bound states), while the genuine two-cusp tree toy of edge weight `sqrt q` reproduces `M_q` only
after one ray-origin shift and has the comb points as bound poles. The cascade `K_{AB} = K_A ⊕ A K_B` with its triangular
dynamics and exit (2.13)–(2.16) is exact and the orientation ("arithmetic feeds the local factor" for the forward
compression) is right. The squarefree tensor/Walsh structure and the `2^ω(N)` cusp count are correct; the product-building
inference and the identification of the spectral comb with the 09c trace comb are correctly refuted. Nothing in the file
overclaims: H-LP, general H-CLASS, function-field H-ARITH and the prime-power matrices are explicitly left open.
