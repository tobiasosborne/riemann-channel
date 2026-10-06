# Adversarial review: the ζ lane of the adelic-GKP session (`zeta-ingredients.md`) and the synthesis's own §§3–4b (`data-ladder.md`)

- **Date:** 2026-10-06
- **Reviewer:** claude:opus-5.5 (REFUTE lane)
- **Authors under review:** claude:opus-5.5, lane G (`zeta-ingredients.md`, with `checks/check_zeta_ingredients.py`); claude:fable-5.1, orchestrator (`data-ladder.md` §3 "Two levels", §4 "The data for ζ, item by item", §4b "One step against a family", with `checks/check_family_weil.py`).
- **Version reviewed:** HEAD `bd0697a`. This includes lane M's fold-in to §4b (the CM sentence now restricted to "families of complex multiplications", plus the paragraph "Which families share a vacuum") and lane N's $L^2_\delta$ annotation on `zeta-ingredients.md` §6.
- **Statements adjudicated:** G0–G6 (every *proved here* / *checked* statement of lane G), S1 (§3), S2a–S2b (§4), S3a–S3c (§4b).
- **Context read but not reviewed:** `cone-bridge.md` §§2, 5; `cm-lift.md` §§2–4; `adelic-gkp.md` §§0, 1, 7–12; `lattice-tower.md` §7; `notes/weil-bond-analytic/analytic.md` conventions and §14; `report/sections/04t_deninger_bond.tex` (`thm:fe-pairing-jets`, `thm:bond-positive-metric-criterion`, `prop:weil-form-not-metric`).
- **Independent numerics.** Four scratch scripts, `notes/reviews/scratch_gkp_zeta_*.py`, written from the *statements* only. No code from `notes/adelic-gkp/checks/` or from the reviewer helper `scratch_rtp2_grid_common.py` was read or reused.
  - `scratch_gkp_zeta_eftest.py`. My own explicit-formula convention: pole terms, von Mangoldt sum, and Weil's archimedean term in the $u$-form $-(\gamma_E+\log\pi)g(0)+\int_0^\infty[2e^{-2u}g(0)-e^{-u/2}(g(u)+g(-u))]/(1-e^{-2u})\,du$. Validated on three Gaussians against the 3000-zero sum to 14–15 digits.
  - `scratch_gkp_zeta_window.py`. The window form $Z_N$ on $[0,\log x]$ in a closed form of my own: off the diagonal, $Z_{mn}=(R_n-R_m)/(\pi(m-n))$, so the form is real symmetric and needs only $O(N)$ quadratures. Run at 50 digits with mpmath; checks Π₁, the Loewner identity and the synthetic quartets.
  - `scratch_gkp_zeta_dilation.py`. A float64 rebuild of the same form for $N\le160$. The compressed dilation by 2, its residuals, singular values, the low-mode cut limit, and smooth bumps away from the edge, at $x=13$ and $x=100$.
  - `scratch_gkp_zeta_algebra.py` (48/48). Covers G1 (step and involution computed by quadrature from the functions, with an off-line quartet in ω), Proposition 1 (real and Hermitian, definite and indefinite), the spectral-model numbers, $\Omega_D$, the genus-two curve (PARI `hyperellcharpoly`), the one-mode identity, and the CM family on $\mathcal O_{\mathbb Q(\sqrt{-7})}$ for ten split primes.

**Headline. 6 VALID / 5 MINOR / 2 INVALID.**

Every number on lane G's page that I recomputed agrees with the page.
- Window inertias: $\lambda_{\min}(Z_5)=7.13\cdot10^{-17}$; $\lambda_-(Z_N-P_N)=-5.8417,-5.8459,-5.8488$ and $\lambda_-(Z_N+P_N)=-0.64788,-0.69405,-0.7042$ for $N=5,10,15$; quartet indices 2 and 3.
- Dilation residuals: all twelve whole-window values agree to two digits. The cut limits are 0.379 at $c=0.372$ and 0.395 at $c=0.393$. The singular-value counts are 87 and 48.
- Spectral model: the fractions 0.5017, 0.4973 and 0.4980; the weight 4393.1; the five ratios.

Lane G's mathematics stands. Its faults are one convention line (G0) and one normalisation sentence (G3).

The two INVALIDs are in the orchestrator's synthesis, in the *readings* drawn from lane G:
- §4 item 2 says that what ζ lacks is "one Ω for the whole commuting family of prime steps" (S2b). ζ has such forms: $\Omega_{\rm FE}$ on zero spans, and $\Omega_D$ on the test algebra unconditionally. And what the sentence really demands, one Ω for which a fixed form is every step's Weil form, exists in no understood family.
- §4b says each prime step's Weil form is "indefinite for every $p$, exactly as for the Hecke family" (S3b). In the Hecke family each step's Weil form is *definite*, and the sign differs only between conjugate primes. Choosing one prime above each $p$ removes it, which makes the CM half of the sentence false even after lane M's restriction. For ζ no compatible Ω makes even the steps 2 and 3 both positive: their signs disagree on 50.1% of the first 3000 zeros.

The MINORs:
- the convention line of lane G §1 (G0);
- the normalisation dependence of "$B$ is the vacuum point" (G3);
- the local/global split of §3, which omits the function-field case the ladder itself now contains (S1);
- four precision faults in the §4 inventory (S2a);
- "positivity of the involution" where Weil's criterion is positivity of the functional ω (S3c). This also covers the CM Rosati form, which is a local trace.

---

## Lane G: `zeta-ingredients.md`

### G0: the convention line of §1

**Claim (one line).** "$F_h(s)=\int h(u)e^{(s-1/2)u}du$ (this is $\hat h(s)$), $\tilde h(x)=x^{-1}\overline{h(1/x)}$, … $\hat g(s)=\hat h(s)\overline{\hat h(1-\bar s)}$."

**VERDICT G0: MINOR**

Attacks tried and what happened.
- `analytic.md` defines $\hat h(s)=\int h(x)x^s\,d^\times x=\int h(e^u)e^{su}du$. With that transform, the stated $\tilde h$ and $\hat g$ formula are right. I checked by quadrature that $\widehat{\tilde h}(s)=\overline{\hat h(1-\bar s)}$.
- For the *same* function $h$, $F_h(s)=\hat h(s-\tfrac12)$, not $\hat h(s)$. With $F_h$ and the stated $\tilde h$ one gets $F_g(s)=F_h(s)\overline{F_h(2-\bar s)}$.
- The page uses both conventions. §1.1 has the multiplier $a^s$ (the $\hat h$ convention). The window of §3.2 uses the normalised, unitary translation (the $F_h$ convention, applied to the half-density $e^{u/2}h(e^u)$).
- No result is affected. Every statement downstream is made in one convention or the other.

**Sentence at fault** (§1, first line): "$F_h(s)=\int h(u)e^{(s-1/2)u}du$ (this is $\hat h(s)$)".

**Corrected statement.** "$\hat h(s)=\int h(x)x^s\,d^\times x$ as in `analytic.md`. In the normalised variable $h^\natural(u)=e^{u/2}h(e^u)$ one has $\hat h(s)=\int h^\natural(u)e^{(s-1/2)u}du$, and there $\tilde h$ becomes $\overline{h^\natural(-u)}$ and the step becomes the unitary translation. §1.1 uses $\hat h$; §3.2 uses $h^\natural$."

### G1: step, adjoint, similitude and adjunction before RH

**Claim.** With $M_a=\delta_a*$ and $\tilde h(x)=x^{-1}\overline{h(1/x)}$, one has $\tilde\delta_a=a\delta_{1/a}$ and $V_a=aM_a^{-1}$. Then $B(h,k)=\omega(h*\tilde k)$ satisfies $B(M_ah,M_ak)=aB(h,k)$ and $B(M_ah,k)=B(h,V_ak)$ for every $a>0$, before RH.

**VERDICT G1: VALID**

- *By hand.*
  - $(\delta_a*h)^\sim=\tilde h*\tilde\delta_a=a\,\tilde h*\delta_{1/a}$, so $(\delta_a*h)*(\delta_a*k)^\sim=a\,h*\tilde k$.
  - $(a\delta_{1/a}*k)^\sim=\tilde k*\delta_a$, which gives the adjunction.
  - Both use only commutativity and the linearity of ω, and no property of the zeros.
- *Numerically, with RH deliberately false.* I took ω to be the sum over 12 critical zeros plus the off-line quartet $0.8\pm9i,\ 0.2\pm9i$. Steps, involution and transforms were all computed by quadrature from the functions themselves. For $a=2$ and $3.7$:
  - the similitude ratio is $a$ to $10^{-12}$;
  - the adjunction holds to $10^{-12}$.

### G2: Proposition 1, $\Omega=2G(M-V)^{-1}$

**Claim.** For a non-degenerate symmetric $G$ with $M^TGM=qG$, $V=qM^{-1}$ and $M-V$ invertible, $\Omega=2G(M-V)^{-1}$ is alternating and compatible, and $\tfrac12\Omega(M-V)=G$. Conversely, a compatible Ω gives a similitude $\tfrac12\Omega(M-V)$.

**VERDICT G2: VALID**

- *The relation that the alternating claim needs.*
  - $M^TGM=qG$ gives $M^TG=GV$ by right multiplication with $M^{-1}$, and $V^TG=GM$ by left multiplication with $M^{-T}$. That is, $V$ is the $G$-adjoint of $M$. This step does not even need $G^{-1}$.
  - Then $A=G(M-V)$ is antisymmetric, and $G(M-V)^{-1}=GA^{-1}G$ is antisymmetric.
  - Compatibility uses $[M,V]=0$. Ω is non-degenerate iff $G$ is.
- *The converse.* $M^T\Omega=\Omega V$ and $V^T\Omega=\Omega M$ make $\Omega(M-V)$ symmetric and a $q$-similitude.
- *Numerically.*
  - Real and Hermitian $G$ of signatures (4,0), (2,2) and (3,1), with $M=\sqrt q\exp(G^{-1}A)$: all three identities hold to $10^{-11}$.
  - A random $M$ that is not a similitude gives an Ω with $\max|\Omega+\Omega^T|=47$. So the hypothesis is used, and the proof uses it correctly.
  - Hermitian case: $q$ must be real, which it is.
- *Spectral model.* With $B=I$, $M_p=\mathrm{diag}(p^\rho)$ and $V_p=\mathrm{diag}(p^{1-\rho})$, $\Omega_p$ is anti-Hermitian with weights $-i/(\sqrt p\sin(\gamma\log p))$ exactly, checked on 200 zeros for $p=2,3$.

### G3: one $\Omega_p$ per prime; indefinite against $\Omega_{\rm FE}$; $B$ the vacuum point; $D$ with Williamson weights $|\gamma|$

**Claim.**
- $\Omega_p$ has weights $1/(\sqrt p\sin(\gamma\log p))$, which give 4393 for $p=2$, and no compatible Ω serves two primes.
- For $\Omega_{\rm FE}$ the prime-step Weil forms have weights $\sqrt p\sin(\gamma\log p)$ and are indefinite (fractions 0.502, 0.497, 0.498), and $B$ is the vacuum point.
- $B=\Omega_D(\cdot,D\cdot)$ with Williamson weights $|\gamma|$.
- "The statements below compare weights within one normalisation and are unaffected by it."

**VERDICT G3: MINOR**

The mathematics.
- *Recomputed.*
  - Fractions 0.5017, 0.4973, 0.4980.
  - $\min|\sin(\gamma\log2)|=1.6096\cdot10^{-4}$, giving weight 4393.1.
  - Ratios $-1.666,-0.830,-1.140,0.708,0.608$.
- *Compatible forms are diagonal.* $\overline{a^\rho}a^\sigma=a$ for two multiplicatively independent $a$ forces $\sigma=1-\bar\rho$.
- *Generator.*
  - $\Omega_{\rm FE}(\cdot,D\cdot)$ has weights $\mathrm{sgn}(\gamma)\gamma=|\gamma|$.
  - $\Omega_D$ has weights $1/\overline{i\gamma}$, so $B=\Omega_D(\cdot,D\cdot)$ and the symplectic eigenvalues are $|\gamma|$.
  - $\Omega_D$ is anti-Hermitian with an off-line quartet present. I checked this, and it is the claim "whether or not RH holds".
- *A stronger form of "no Ω serves two primes".* No compatible Ω makes the Weil forms of 2 and 3 even *both positive*. That needs $\mathrm{sgn}\sin(\gamma\log2)=\mathrm{sgn}\sin(\gamma\log3)$ for every γ, and the signs disagree on 50.1% of the 3000 zeros. This matters for S3b.

**The fault.** The normalisation sentence is false for the vacuum-point claim.
- 04t `prop:weil-form-not-metric`(b) says unit weights are tied to a chosen evaluation normalisation. 04t `thm:bond-positive-metric-criterion`(d) says the diagonal commutant acts transitively on certificates.
- Concretely: every positive step-invariant diagonal form $c_\gamma$ is the vacuum form of the compatible Ω with weights $-i\,\mathrm{sgn}(\gamma)c_\gamma$. I checked this for random $c$.
- So "$B=G_J$ for 04t's $J$" holds only when the jet basis $e_\rho$ of $\Omega_{\rm FE}$ is identified with the evaluation coordinates $\hat h(\rho)$ at unit scale.
- What is normalisation-free:
  - the indefiniteness (it depends only on the Krein signs $\mathrm{sgn}\,\gamma$);
  - the non-existence of a common $\Omega_p$ (it depends on ratios across primes at fixed γ);
  - the statement that $B$ is invariant under every step, which is what "vacuum point" amounts to.

**Sentence at fault** (§3.1, model paragraph): "The statements below compare weights within one normalisation and are unaffected by it."

**Corrected statement.** "Indefiniteness, the singular weights of $\Omega_p$, and the absence of a common $\Omega_p$ are independent of the normalisation. They involve only Krein signs and ratios across primes at a fixed ordinate. '$B=G_J$' holds in the evaluation normalisation. In any other diagonal normalisation, $B$ is the vacuum form of the correspondingly rescaled compatible Ω, because every positive form invariant under all steps is the vacuum form of some compatible Ω (04t `thm:bond-positive-metric-criterion`(d)). So 'vacuum point' says that $B$ is invariant under the whole family, and nothing more."

*Remark, not a fault.* The inventory's "$\Omega_p$ … singular" means unbounded weights (small divisors), not degenerate. "Unbounded" would be clearer.

### G4: the window: the Loewner identity, the prime-2 dilation, and the singular values

**Claim.**
- $G_N(\cdot,D^{-1}\cdot)$ is anti-Hermitian on mean-zero window functions.
- The compressed dilation by 2 is a similitude only on functions supported in $[0,L-\log2]$.
- The whole-window residual stays near 0.4 for $N\le160$ and does not shrink from $x=13$ to 100.
- The low-mode block converges to a non-zero cut limit.
- Each step loses $n\log p/L$ singular values.

**VERDICT G4: VALID**

- *Loewner.*
  - On the window, $D^{-1}e_n=(e_n-e_0)/(i\beta_n)$ is the true antiderivative, vanishing at both ends. So it stays in the window.
  - $Z_5(\cdot,D^{-1}\cdot)$ is anti-Hermitian to $4\cdot10^{-53}$ at 50 digits.
  - The identity holds for *any* Hermitian translation-invariant kernel; I checked the pole pair separately by hand. The page is right that it encodes squeeze invariance only.
- *Residual.* Measured as best-$c$ $\|M^\dagger ZM-cZ\|_F/\|Z\|_F$, I get:

  | | $N=5$ | 10 | 20 | 40 | 80 | 160 |
  |---|---|---|---|---|---|---|
  | $x=13$ | 0.401 | 0.455 | 0.472 | 0.477 | 0.470 | 0.464 |
  | $x=100$ | 0.367 | 0.400 | 0.451 | 0.439 | 0.441 | 0.433 |

  These are the page's numbers to two digits.
  - The cut limit has residual 0.379 at $c=0.372$ ($x=13$) and 0.395 at $c=0.393$ ($x=100$).
  - The low-mode distance to the cut limit falls from $5.4\cdot10^{-2}$ to $1.1\cdot10^{-2}$ ($x=13$, $N=20\to160$, Frobenius). The page's $2.6\cdot10^{-2}\to1.8\cdot10^{-3}$ presumably uses another norm or another range of $N$. The convergence itself is confirmed.
  - A reason the effect is $O(1)$: on slowly varying functions the zero-sum form is dominated by the endpoint jumps, through $\sum_\gamma1/\gamma^2$ and $\sum_\gamma\cos(\gamma\ell)/\gamma^2$. The second term changes by $O(1)$ when $\ell$ drops from $L$ to $L-\log2$, whatever $L$ is.
  - This is consistent with "edge effect of size $O(1)$". That reading is still tested only at two values of $x$.
- *Away from the edge.* For a smooth bump supported in $[0.1,L-\log2-0.1]$, $|Z(Mh,Mh)/Z(h,h)-1|$ goes $8.8\cdot10^{-5}\to3.3\cdot10^{-12}$ ($x=13$) and $1.6\cdot10^{-2}\to5.6\cdot10^{-7}$ ($x=100$), for $N=20\to160$.
- *Singular values.* Below ½: 87 against 86.7 ($x=13$) and 48 against 48.3 ($x=100$).
- *Precision remarks, not faults.*
  - $M_N=P_N1_{[a,L]}P_N\cdot\mathrm{diag}(e^{-i\beta_na})$ is a positive Toeplitz matrix times a diagonal unitary. So it is *invertible* for every $N$: $\sigma_{\min}=9.6\cdot10^{-4}$ at $N=5$ and $2.3\cdot10^{-18}$ at $N=160$.
  - "Partial isometry" is true of the cut limit $\chi U_a$, not of $M_N$. The inventory's "in truncation a partial isometry" should say "in the limit $N\to\infty$".
  - Findings bullet 1, "no finite window carries one of them as an invertible map", is true in the sense of invariance. No non-zero finite-dimensional space of compactly supported functions is invariant under one translation, because the supports of $U_a^kh$ eventually separate. That sense should be stated.
- *Precision of Z.* In float64, $\lambda_{\min}(Z_5)=-2.8\cdot10^{-15}$ (true value $7.1\cdot10^{-17}$). This confirms the page's precision note that float data cannot certify positivity.

### G5: Π₁ on the window

**Claim.**
- $Z_N>0$.
- $Z_N\mp P_N$ have inertia $(n-1,1,0)$ at $N=5,10,15$.
- A synthetic off-line quartet gives negative index 2 for $Z+Q$ and 3 for $Z+Q-P$.
- Each off-line pair adds one negative direction.

**VERDICT G5: VALID**

- *Independent 50-digit rebuild.*

  | $N$ | $\lambda_{\min}(Z_N)$ | $\lambda_-(Z_N-P_N)$ | $\lambda_-(Z_N+P_N)$ |
  |---|---|---|---|
  | 5 | $7.13\cdot10^{-17}$ | $-5.8417$ | $-0.64788$ |
  | 10 | $2.83\cdot10^{-26}$ | $-5.8459$ | $-0.69405$ |
  | 15 | $1.21\cdot10^{-33}$ | $-5.8488$ | $-0.7042$ |

  - $P_N$ has inertia $(1,1,n-2)$.
  - Quartets at $0.75+5i$ and $0.6+14.13i$ ($N=10$): $Q$ has inertia (2,2,17), $Z+Q$ has (19,2,0), and $Z+Q-P$ has (18,3,0).
  - These are identical to the page.
- *Structure.* Most of these counts are forced, and the page should say how much.
  - $Z>0$ plus a rank-2 term of signature (1,1) has at most one negative eigenvalue and at least $n-1$ positive ones.
  - So "exactly one" is the single condition $\det(Z\pm P)<0$.
  - Likewise a quartet ($Q$ of signature (2,2)) can add at most two.
  - "Each off-line pair adds one" is therefore an upper bound by rank, attained in the two tested cases. It is not a theorem about every placement.
  - The statement is labelled *checked*, which is accurate.
- *Zero-side cross-check* (B3).
  - The explicit-formula diagonal exceeds the 3000-zero sum by $5.65\cdot10^{-4}$ ($m=0$). That is 11% *more* than the mean-square Riemann–von Mangoldt tail ($5.09\cdot10^{-4}$, with $\sin^2$ averaged to ½).
  - The excess is Landau's bias. $x=13$ is prime, so $\sum_{\gamma\le T}\cos(\gamma\log13)\approx-(T/2\pi)\log13/\sqrt{13}$ inflates $\langle\sin^2(\gamma L/2)\rangle$ by about $0.71/\log(T/2\pi e)\approx13\%$.
  - Against the sup bound of the tail the page's "less than the tail estimate" holds. This is a remark on B3, not a fault.

### G6: the one-line *proved here* items

**Claim.**
- Compatible forms are diagonal.
- The curve's $\tfrac12\Omega_+(F^2-V^2)=\tfrac12\mathcal T(\cdot,(F+V)\cdot)$ has weights $\lambda_j=3.79,-0.79$ for the genus-two curve.
- The nilpotent Toeplitz shift admits no non-degenerate similitude.
- §1.2: $W(Mx,y)=W(x,Vy)$.
- The inventory's CM column: Weil form $\varepsilon\,\mathrm{Im}\,\psi(\mathfrak p)\,G_{J_K}$.

**VERDICT G6: VALID**

- PARI gives $P(x)=x^4-3x^3+7x^2-15x+25$, hence $\lambda^2-3\lambda-3=0$ and $\lambda=(3\pm\sqrt{21})/2=3.791,-0.791$.
- I built the Frobenius matrix, a positive similitude $G$, and $\Omega_+=2G(F-V)^{-1}$. The Weil form of $F^2$ then has inertia (2,2).
- Nilpotent case: $\det M=0$ forces $c^n\det G=0$.
- §1.2 is $M^T\Omega=\Omega V$ plus $[M,V]=0$.
- CM column: see S3a.

---

## Synthesis: `data-ladder.md` §§3–4b

### S1 (§3): two levels, local and global

**Claim.**
- The finite cases model the local level of ζ-like $L$-functions.
- The zeros of ζ are entirely global, and the local factor at $p$ has no zeros.
- "The exception that keeps the programme alive is the graph itself read as a global field."
- `lattice-tower.md` §7.3 is "a reading of the local level only" (also listed in §5).

**VERDICT S1: MINOR**

What holds.
- The local factors $(1-p^{-s})^{-1}$ and $\pi^{-s/2}\Gamma(s/2)$ have no zeros.
- The explicit formula is consistent with the split. Global zeros equal the pole plane minus the sum of local terms, and each local term is a spectral sum over a local factor's poles (Poisson in $k\log p$).
- Lane C's CM example is described correctly. In the `cm-lift.md` §2.5 table, local RH is free on $\mathcal O_K$ and the global zeros are squeeze frequencies with GRH open.

Attacks that succeed.
1. *The split is not "finite cases = local".*
   - A curve over $\mathbb F_q$ has two readings. As the reduction of a lift it is a local factor of $L(E,s)$, and its zeros are that factor's *poles*. As the function field $\mathbb F_q(C)$ it is a **global field**: its places are closed points, and its zeros are global and are eigenvalues of Frobenius on the finite-rank $H^1$.
   - The second reading is the classical analogue of $\mathbb Q$ (Weil). It is the one `analytic.md` §14 makes exact ($\mathbb R[F]\leftrightarrow$ test algebra), and the one lane J (`ff-dirichlet.md`) now puts on the ladder.
   - The page's own first paragraph treats graphs *and* curves as finite global objects. Yet the third paragraph names only the graph as "the exception". The graph is the combinatorial instance of the function-field case, not an exception to it.
2. *§7.3 is not local-only.*
   - "Zeros are oscillator frequencies; the squeeze is the trivial pair" is exactly right for the global zeta of a function field. The global zeros are the rotation angles of $F/\sqrt q$ on $H^1$, and the poles are the hyperbolic pair on $H^0\oplus H^2$.
   - What separates the CM case from that picture is not local against global. It is the step group: discrete ($\mathbb Z$, generated by Frobenius) against continuous ($\mathbb R_+^\times$).
3. *"For ζ the local level is empty of zeros"* is literally true, but it is not a contrast with the finite cases. No local factor of any $L$-function has zeros. The curve's zeros reappear as poles of $L_p(E,s)$, and ζ's local factor carries the weight-0 piece (the $H^0$ pole series on $\mathrm{Re}\,s=0$).

**Sentences at fault.**
- §3: "So the understood finite cases model the **local** level of $\zeta$-like $L$-functions, … and the reading of `lattice-tower.md` §7.3 … is a reading of that level."
- §3: "The exception that keeps the programme alive is the graph itself read as a global field".
- §5: "`lattice-tower.md` §7.3 is a reading of the local level only".

**Corrected statement.** "Each finite case has two readings. As a reduction it models the local level of an $L$-function over $\mathbb Q$: its zeros are the poles of an Euler factor, and RH there is Hasse–Deligne. As a global field (the function field $\mathbb F_q(C)$, the graph with its prime cycles, the Dirichlet characters of $\mathbb F_q(t)$ of lane J) its zeros are global and are eigenvalues of an integral step on a finite-rank $H^1$. `lattice-tower.md` §7.3 holds wherever the step group is discrete: the local level over $\mathbb Q$, and the global level of function fields and graphs. It has no established counterpart at the global level over $\mathbb Q$, where the step group is $\mathbb R_+^\times$ and the zeros appear as squeeze frequencies (lane C). The question 'what data for ζ' is what plays $H^1$ of the function field for the global zeros."

### S2a (§4): the in-hand and absent lists

**Claim.**
- The itemised lists.
- "The code's own lattice $\mathbb Q^2$ cannot serve … the squeezes $D_a$ act on it as automorphisms with $(1-D_a)\mathbb Q^2=\mathbb Q^2$, so there is no logical space and no counts."
- "the missing datum … is extra structure on the cokernel, of the kind the symplectic pairing supplies in the finite case".

**VERDICT S2a: MINOR**

The conclusion ($\mathbb Q^2$ cannot be the lattice) stands. There are four precision faults.

1. *Which squeezes act on $\mathbb Q^2$.*
   - `adelic-gkp.md` G2 says $D_a$ preserves $\mathbb Q^2$ only for $a\in\mathbb Q^\times$. For those $a$, $1-D_a=\mathrm{diag}(1-a^{-1},1-a)$ is indeed invertible on $\mathbb Q^2$.
   - But those $a$ act trivially on the code ($D_a\Theta=\Theta$) and are the identity of $C_{\mathbb Q}=\mathbb A^\times/\mathbb Q^\times$.
   - The steps that carry ζ's zeros are non-principal idele classes, e.g. $p\in\mathbb R_+^\times\subset C_{\mathbb Q}$ ($\delta_p$). They do not preserve $\mathbb Q^2$ at all. For example, the idele $(2,1,1,\dots)$ moves the diagonal $(1,1,\dots)$ off $\mathbb Q$.
   - So the stated reason is about the trivial steps. For the real ones, the reason is that they have no invariant lattice to act on.
2. *"Connes's cokernel, an infinite-dimensional space with a unitary squeeze flow".* Lane N's citation correction, annotated on `zeta-ingredients.md` §6, places Connes's realisation in $L^2_\delta$ with $\delta>1$, where the action is **not unitary**; 04t `prop:weil-form-not-metric`(c) says the same. §4 still says "unitary".
3. *"The pole plane as the one negative direction of the windowed form with poles kept".* Lane G is explicit that Weil's form with the poles kept, $Z_N$, is positive definite. The one negative direction belongs to $Z_N\mp P_N$. The parenthesis gets this right but the sentence reinstates the ambiguity lane G warned about.
4. *"Extra structure on the cokernel, of the kind the symplectic pairing supplies".* In the finite case the Weil pairing detects the *class* of a lattice that is already given (lane F). It does not supply the lattice. The missing datum for ζ is item 1 itself, a lattice with an integral step. The pairing-type data (an alternating form compatible with every step) ζ already has (S2b).

**Sentences at fault, with corrections.**
- (1) "the squeezes $D_a$ act on it as automorphisms with $(1-D_a)\mathbb Q^2=\mathbb Q^2$" → "the principal squeezes $D_a$, $a\in\mathbb Q^\times$, preserve $\mathbb Q^2$ with $(1-D_a)\mathbb Q^2=\mathbb Q^2$, but they act trivially on Θ and are the identity of $C_{\mathbb Q}$. The idele-class steps that carry the zeros do not preserve $\mathbb Q^2$."
- (2) "with a unitary squeeze flow" → "with a squeeze flow, non-unitary on Connes's weighted space $L^2_\delta$".
- (3) "the one negative direction of the windowed form with poles kept" → "the one negative direction of $Z_N\mp P_N$ (Weil's windowed form $Z_N$ itself is positive)".
- (4) "it is extra structure on the cokernel, of the kind the symplectic pairing supplies in the finite case" → "it is an integral structure on the cokernel on which the steps act. In the finite case the Weil pairing detects the class of such a structure; it does not create it."

### S2b (§4 item 2, last sentence): "what ζ lacks is … one Ω for the whole commuting family of prime steps"

**Claim.** "So what $\zeta$ lacks is not a symplectic partner for one step but one $\Omega$ for the whole commuting family of prime steps".

**VERDICT S2b: INVALID**

- *Reading 1: one compatible Ω for every step.* ζ has two.
  - $\Omega_{\rm FE}$ is compatible with the whole flow on finite zero spans (04t `thm:fe-pairing-jets`; lane G §1.3).
  - $\Omega_D=B(\cdot,D^{-1}\cdot)$ is defined on the test algebra (on $\hat k(\tfrac12)=0$) before RH. It is compatible with every $M_a$ at once, because $D^{-1}$ commutes with $M_a$.
  - I checked $\Omega_D(M_ax,M_ay)=a\,\Omega_D(x,y)$ for $a=2,3,5$ simultaneously, with an off-line quartet present.
  - Lane M (now folded into §4b) adds that ζ's prime steps share one $J$.
- *Reading 2: one Ω for which $B$ is every prime step's Weil form.* That is what lane G's "no single compatible Ω serves two primes" refers to. No understood family has such an Ω either:
  - for the curve, $\mathcal T$ is the $\Omega_+$-Weil form of $F$ but not of $F^2$ (lane G §3.1; inertia (2,2), G6);
  - in the CM family the Weil forms $\mathrm{Im}\,\psi(\mathfrak p)\,G_{J_K}$ differ in size and sign from prime to prime (S3a).
  - So its absence cannot be what separates ζ from the understood cases.
- On either reading the sentence names as missing something that is either present or absent everywhere. §4b's own conclusion, "not an Ω for one step … but a reason for the family's involution to be positive", contradicts it.

**Corrected statement.** "So what $\zeta$ lacks is neither a symplectic partner for one step ($\Omega_p$) nor a form compatible with the whole family. $\Omega_{\rm FE}$ on zero spans and $\Omega_D=B(\cdot,D^{-1}\cdot)$ on the test algebra are compatible with every step. No understood family has one Ω for which a fixed form is every step's Weil form. What is missing is a reason for the family-invariant point $B$ to be positive."

### S3a (§4b): the identities

**Claim.**
- On one mode, the Weil form is $\sqrt q\sin\theta\,G_J$ and its sign depends on orientation.
- CM family: the Weil forms are $\mathrm{Im}\,\psi(\mathfrak p)\,G_{J_K}$, with opposite signs on conjugate primes and one vacuum $J_K$, and the trace form is a positive multiple of $G_{J_K}$.
- ζ: the step on a zero mode rotates by $\gamma\log p$, so its $\Omega_{\rm FE}$-Weil form is $\sqrt p\sin(\gamma\log p)$ times the vacuum form.

**VERDICT S3a: VALID**

- One mode: $M-V=2\sqrt q\sin\theta\,J$, exact for $\theta=0.4,2.0,4.0$, and $-\Omega$ flips the sign.
- CM:
  - $\mathcal O_K=\mathbb Z[w]$, $w^2=w-2$, $\Omega=\det$, $J_K$ multiplication by $\sqrt{-7}/\sqrt7$.
  - For the ten split primes $2,11,\dots,79$ the Weil form equals $\mathrm{Im}\,\psi(\mathfrak p)\,G_{J_K}$ exactly, and the conjugate prime gives the negative.
  - $\mathrm{Tr}(x\bar y)=\bigl(\begin{smallmatrix}2&1\\1&4\end{smallmatrix}\bigr)=\sqrt7\,G_{J_K}$ for this orientation.
- ζ: $p^{\rho}=\sqrt p\,e^{i\gamma\log p}$.
- One notational slip. §4b writes "on the pair $\{\rho,1-\bar\rho\}$", but for a critical zero $1-\bar\rho=\rho$. The rotation plane is $\{\rho,\bar\rho\}=\{\rho,1-\rho\}$, the real span of one mode for real test functions. The pair $\{\rho,1-\bar\rho\}$ is the *hyperbolic* pair of an off-line zero (`adelic-gkp.md` §10).

### S3b (§4b): "indefinite for every $p$, exactly as for the Hecke family"; "for a family of complex multiplications no orientation makes every Weil form positive"

**Claim.** In the CM family no orientation makes every Weil form positive. ζ's prime-step Weil forms for $\Omega_{\rm FE}$ are "indefinite for every $p$, exactly as for the Hecke family", so lane G's finding is "the family version of lanes A and E".

**VERDICT S3b: INVALID**

- *The CM sentence is false even after lane M's restriction.*
  - Take one step per split rational prime, $\psi(\mathfrak p_p)$ with the prime $\mathfrak p_p\mid p$ chosen so that $\mathrm{Im}\,\psi(\mathfrak p_p)>0$.
  - This is a commuting family of complex multiplications on $\mathcal O_K$, all with the vacuum $J_K$. It is the family §3 itself describes: "one one-mode step $\psi(\mathfrak p)$ on $\mathcal O_K$ per split prime".
  - Every Weil form in it is *positive* for one fixed Ω. I checked this for $p=2,\dots,79$.
  - `cm-lift.md` §2.5 records the same: "positive at every split $p$ for the same $J_K$".
  - The obstruction exists only for a family that contains a conjugate pair $\psi(\mathfrak p),\psi(\bar{\mathfrak p})$.
- *"Exactly as" is false.* The two mechanisms differ.
  - **Hecke.** One mode per step. Each step's Weil form is *definite* ($\det>0$ for all ten primes). The sign is one number per step, and choosing the generator removes it.
  - **ζ.** Each single step's Weil form is *indefinite* already, with about half the modes negative. No compatible Ω can repair even two steps: a common positive orientation for $\delta_2$ and $\delta_3$ needs $\mathrm{sgn}\sin(\gamma\log2)=\mathrm{sgn}\sin(\gamma\log3)$ for every γ, and that fails on 50.1% of the first 3000 zeros.
- *The faithful analogue is the one lane G draws* (§3.1, "The curve has the same feature"). With $\Omega_{\rm FE}$ the *generator* $D$ has a positive Weil form, with weights $|\gamma|$. The steps $\delta_p=e^{(\log p)D}$ are large powers of it, rotating mode γ by $\gamma\log p$, far past π. That is the curve's $\Omega_+$ with $F$ positive and $F^2$ indefinite. §4b's ζ bullet does not mention $D$, and it replaces this analogue with the Hecke one, which is a different phenomenon: the labelling of conjugate primes.

**Sentences at fault.**
- §4b, second bullet: "for a family of complex multiplications no orientation makes every Weil form positive, and this has nothing to do with RH."
- §4b, third bullet: "so its Weil form for $\Omega_{\rm FE}$ is $\sqrt p\,\sin(\gamma\log p)$ times the vacuum form, indefinite for every $p$, exactly as for the Hecke family".

**Corrected statement.** "For a family of complex multiplications that contains a conjugate pair $\psi(\mathfrak p),\psi(\bar{\mathfrak p})$, no orientation makes every Weil form positive. With one step per split rational prime, chosen with $\mathrm{Im}\,\psi>0$, one orientation makes them all positive. Either way each step's Weil form is definite, and this has nothing to do with RH. ζ is different. On the mode $\{\rho,\bar\rho\}$ the step $M_p$ rotates by $\gamma\log p$, so its $\Omega_{\rm FE}$-Weil form is $\sqrt p\sin(\gamma\log p)$ times the vacuum form. That is indefinite for *each single* $p$, and no compatible Ω makes even two prime steps positive. The understood analogue is the curve's step group, not the Hecke family: the generator $D$ has a positive $\Omega_{\rm FE}$-Weil form (weights $|\gamma|$), as $F$ has for $\Omega_+$, and the prime steps are large powers of it, as $F^2$ is of $F$."

### S3c (§4b): "$B$ is the Rosati form of the family's algebra"; "the positivity of the involution $h\mapsto\tilde h$ … is Weil's criterion itself"; the reason "in every understood case"

**Claim.**
- $B=\omega(h*\tilde h)$ is the Rosati form of the family's algebra (the test-function algebra with $\tilde{\ }$), i.e. the vacuum point.
- "for $\zeta$ the positivity of the involution $h\mapsto\tilde h$ on the squeeze algebra is Weil's criterion itself".
- The missing datum is "a reason for the family's involution to be positive". In every understood case that reason is "geometric and global (ampleness on a Jacobian, the CM field of the lift)" and is carried by the lattice.

**VERDICT S3c: MINOR**

- *The Rosati identification is sound, in the sense of `analytic.md` §14.* Under the dictionary $\mathbb R[F]\leftrightarrow$ test algebra, Rosati $\leftrightarrow\tilde{\ }$, $\mathcal T\leftrightarrow Z$:
  - $B=\omega(x\,x^\dagger)$ is the trace form of the involutive algebra for the trace ω;
  - ω is the Lefschetz trace on $H^1$, defined through the explicit formula $\omega=P-\mathrm{Loc}$;
  - the CM Rosati form $\mathrm{Tr}_{K/\mathbb Q}(x\bar y)=\sum_\sigma\sigma(x)\overline{\sigma(y)}$ has the same structure, a sum over the characters of the algebra.
  - Under RH, $B$ is invariant under every step and positive, hence the vacuum point (with the normalisation caveat of G3).
- *Positivity of the involution is not positivity of ω.*
  - After the twist $h\mapsto x^{1/2}h$, the involution $\tilde{\ }$ is the $*$-operation of the group algebra of $\mathbb R_+^\times$. It is positive for the Plancherel trace $\tau_0(g)=\int\hat g(\tfrac12+it)\,dt/2\pi$, because $\tau_0(h*\tilde h)=\int|\hat h(\tfrac12+it)|^2dt/2\pi\ge0$, unconditionally.
  - The window computation shows the difference concretely. With the same involution, the $L^2$ Gram of the basis is the identity, while ω with a synthetic quartet has two negative directions.
  - Weil's criterion is that the *functional* ω is a state on the $*$-algebra. That is how `adelic-gkp.md` §10 states it, and `analytic.md` §14 states its target as "an involutive algebra whose *trace* is positive for a structural reason". For the finite-dimensional algebra $K$ the trace is canonical, so "positive involution" is unambiguous there. For the squeeze algebra it is not.
- *Level.*
  - In the CM case, $\mathrm{Tr}_{K/\mathbb Q}$ sums over the two embeddings, which are the local Frobenius angles. Its positivity is **local** RH, free (lane C).
  - The global counterpart, Weil's functional of $L(\psi,s)$, has positivity equal to GRH, which is open (`cm-lift.md` §2.5, last row).
  - So "the CM field of the lift" gives a structural reason only at the local level. The understood case where the reason is global and carried by the lattice is the function field: ampleness of Θ on the Jacobian (`analytic.md` §14, `adelic-gkp.md` §11).
  - This is the two-level point of §3, which §4b's comparison of ζ's global $B$ with the CM's local $G_{J_K}$ crosses without saying so. Lane G lists the global CM version as open (§7, third item).

**Sentences at fault.**
- "**for $\zeta$ the positivity of the involution $h\mapsto\tilde h$ on the squeeze algebra is Weil's criterion itself.**"
- "in every understood case that reason is geometric and global (ampleness on a Jacobian, the CM field of the lift)".

**Corrected statement.** "In the finite cases the positivity of the Rosati trace form comes from a polarisation (an ample divisor). For ζ the involution $h\mapsto\tilde h$ is positive for the Plancherel trace unconditionally. What Weil's criterion asks is that the functional ω, the Lefschetz trace on $H^1$, be a state on the squeeze $*$-algebra (`adelic-gkp.md` §10). The datum ζ lacks is a reason for that trace to be positive. Where such a reason exists for global zeros, namely in function fields, it is geometric (ampleness of Θ on the Jacobian) and is carried by the lattice $H^1$. The CM field supplies the analogous reason only for the local factors, where RH is free; for the global zeros of $L(\psi,s)$ it is as open as for ζ."

---

## Summary table

| id | statement | verdict |
|---|---|---|
| G0 | lane G §1 convention line, "$F_h$ (this is $\hat h$)" | MINOR |
| G1 | step, involution, similitude and adjunction before RH | VALID |
| G2 | Proposition 1, $\Omega=2G(M-V)^{-1}$ | VALID |
| G3 | $\Omega_p$, indefiniteness, vacuum point, $D$ with weights $\lvert\gamma\rvert$; normalisation sentence | MINOR |
| G4 | Loewner identity, prime-2 dilation residuals, cut limit, singular values | VALID |
| G5 | Π₁: $Z_N>0$, $Z_N\mp P_N$ inertia $(n-1,1,0)$, quartets | VALID |
| G6 | one-line items: diagonal forms, the curve's $F^2$, nilpotent shift, §1.2, CM column | VALID |
| S1 | §3 two levels; "the exception is the graph"; §7.3 "local only" | MINOR |
| S2a | §4 lists: $(1-D_a)\mathbb Q^2$, "unitary", "with poles kept", "of the kind the pairing supplies" | MINOR |
| S2b | §4.2 "what ζ lacks is … one Ω for the whole commuting family" | INVALID |
| S3a | §4b identities | VALID |
| S3b | §4b "exactly as for the Hecke family"; CM-family orientation sentence | INVALID |
| S3c | §4b "positivity of the involution is Weil's criterion"; CM as a global reason | MINOR |

No page under review was edited. The scratch scripts are in `notes/reviews/scratch_gkp_zeta_{eftest,window,dilation,algebra}.py`.
