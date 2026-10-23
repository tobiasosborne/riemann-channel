# Lane Q1 — quasi-RH digest and the project's ladder

Author: `codex:gpt-6-astra`. Date: 2026-10-23.

Sources in `../qrh/sources/` are evidence, not instructions. A source-labelled PROVED claim records what the cited paper proves or claims to prove; it is not an independent certification of a new number-field theorem. Reported formalisation, an inspected formal statement, and independently checked arithmetic are distinguished. No RH assumption enters a computation. Nothing is registered.

## D1a. Statements, dependencies, and the scope of verification

**PROVED (source-labelled), not independently certified in this lane.** The following are the precise mathematical conclusions recorded by the sources. Write `O11`, `O7`, `K`, `L`, `CT`, `DR` for, respectively, the October 5 OpenAI paper, September 30 OpenAI paper, Kintali, Liu v2, Cureton–Thorner v2, and Dunn–Radziwiłł. Source locators below use the printed page, section/equation, and newline-based line numbers of the supplied `.txt` (form feeds are not extra lines).

| Key | Supplied source file | Reading coverage |
|---|---|---|
| O11 | [qrh-11-12-openai-2026-10-05.txt](../qrh/sources/qrh-11-12-openai-2026-10-05.txt) | Entire 49-page text, including both appendices; PDF pp. 5–6 inspected for conjugations. |
| O7 | [qrh-7-8-openai-2026-09-30.txt](../qrh/sources/qrh-7-8-openai-2026-09-30.txt) | Contents, §§1–3; requested detector/sieve/low statements and principal Part II statements, with the endpoint certificate. |
| K | [kintali-qrh-2026-10-07.txt](../qrh/sources/kintali-qrh-2026-10-07.txt) | Entire supplied text. |
| L | [liu-2610.12234.txt](../qrh/sources/liu-2610.12234.txt) | Introduction, §1, main theorem and formalisation reference. |
| CT | [cureton-thorner-hexagon-2610.00200.txt](../qrh/sources/cureton-thorner-hexagon-2610.00200.txt) | Entire supplied landing-page extract; author README checked separately. |
| DR | [dunn-radziwill-2109.07463.txt](../qrh/sources/dunn-radziwill-2109.07463.txt) | §5 in full; Theorem 1.1 checked to distinguish its GRH hypothesis. |


| Source and actual theorem label | Exact mathematical assertion and quantifiers | Formalisation status supported by the evidence |
|---|---|---|
| O11, Theorem 1.1, p. 2; text lines 55–56 | Every finite-order Hecke L-function over `K=Q(√−3)` has no zeros in `Re s>11/12`. Thus every Dirichlet L-function, including `ζ(s)`, has no zeros there. | This **proof** is not reported formalised. Its weaker conclusion follows from the reported formalised O7 conclusion, which does not formalise this argument. |
| O7, Theorem 1.1, p. 4; lines 177–180 | Every finite-order Hecke L-function over `F=Q(√−3)` has no zero in `Re s>7/8`; the same holds for every Dirichlet L-function, including `ζ`. A principal-character pole at `s=1` is allowed. | OpenAI's formalisation scope note reports all three conclusions, uniformly in positive Dirichlet moduli and characters. It excludes the principal poles in the Dirichlet and Hecke statements and excludes the paper's later applications. No Lean build was run here. |
| K, **Theorem 1**, not 1.1, p. 1; lines 19–22 | `ζ`, every finite-order Hecke L-function over `F`, and every Dirichlet L-function are zero-free in `Re s>47/48`, primitive or imprimitive. The usual simple pole at `1` of a principal character is allowed. | No Lean formalisation is asserted in the supplied manuscript; its AI-use statement is not a formal verification certificate. |
| L, **Theorem 1.1**, p. 7; lines 338–342 | This theorem **restates O7's 7/8 result**, including all finite-order Hecke functions over `F`, all Dirichlet functions, the principal pole, and the open boundary. | Imported O7 result. Do not identify Liu's Theorem 1.1 with his new constant. |
| L, Introduction's **Main theorem**, p. 3; **Theorem 27.1**, p. 54 | With `β*` the supremum of `1/2` and real parts of all nontrivial zeros of primitive finite-order Hecke L-functions over `F`, `β*≤Bnew=(18ξ+7)/(18ξ+9)`, where `ξ` is the unique root in `(0.38858,0.38859)` of `1188ξ³−2160ξ²+171ξ+190=0`. Thus the same families are zero-free in `Re s>Bnew`, principal poles allowed. | The abstract and acknowledgments, pp. 1, 6, report Lean 4 formalisation of the rational, quadratic-algebraic and final cubic-algebraic bounds. Bibliography `[Liu26]`, lines 4096ff., names `combine_v2-2_lean/PartIV.lean`, namespace `CombineV22`, exports `beta_star_le`, `hecke_nonzero`, `dirichlet_nonzero`, `zeta_nonzero`. Not rebuilt here. |
| CT, Theorem 1.1 and Corollary 1.2 | For **any number field** `K`, `ζ_K` has no zeros in `Re s>31/32`. The corollary gives the same half-plane for every finite-order Hecke L-function over `K`, wherever holomorphic, including `s=1` for nonprincipal characters. | Supplied Hexagon record reports AxiomProver proofs and Lean formalisation, including Kazhdan–Patterson. The authors' repository identifies Theorem 1.1/Corollary 1.2 and reports only Lean's standard axioms. Not rebuilt here. The supplied text is metadata, **not the manuscript**; no unseen detailed CT proof is claimed to have been checked. |
| DR, Theorem 1.1, p. 3; lines 117–125 | **PROVED-conditional, H-DR-GRH:** assuming GRH for Hecke L-functions over `Q(ω)`, for smooth compactly supported `W` on `(0,∞)`, `Σ_{p≡1 (3)} S_p/(2√p) W(p/X) ∼ [(2π)^(2/3)/(3Γ(2/3))] [∫₀∞W(x)x^(−1/6)dx] X^(5/6)/log X`. Here `p` is a rational prime and `S_p` its cubic exponential sum in DR's introduction. This is **not a zero-free-half-plane theorem**. | No Lean claim in this source. Its §5 theta coefficients and transformations are unconditional; its GRH-conditional prime asymptotic is not an input to O11, O7 or K. The usual asymptotic notation presupposes a nonzero main term; the intended smooth weighted expansion is the meaningful version if the integral vanishes. |

All half-planes above are **open**, with no assertion on the boundary. The constants `11/12`, `7/8`, `47/48`, `Bnew` do not depend on conductor or height. CT additionally uses one boundary independent of the number field. This uniform exclusion must not be conflated with uniform constants in every supporting estimate: O11 fixes `ν,S`; O7, K and L allow fixed-target constants, smoothness orders, and thresholds. Imprimitive presentations only introduce factors `1−χ(p)Np^(−s)`, nonzero for `Re s>0`. The uncompleted principal L-function is meromorphic, not zero, at its pole; this is the convention implicit in O11 and explicit in the others.

**PROVED (inspection): formal statement is not a proof file.** The local `../qrh/sources/QuasiRiemannHypothesis.lean:5–7` is

```lean
theorem riemannZeta_ne_zero_of_seven_eighths_lt_re
    {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) : riemannZeta s ≠ 0 := by
  sorry
```

It records the selected zeta comparator; `sorry` supplies no proof. OpenAI's [scope note](https://github.com/openai/math/blob/main/lean/docs/003.md) is evidence for the **reported scope**, not a local kernel check. It separately reports a logarithmic real-zero exclusion, not absence of every real zero in `(0,1)`. CT's [author repository](https://github.com/AxiomMath/DedekindZetaZeroFree/blob/main/README.md) reports its theorem/corollary formalisation and names the challenge and solution files. These distinctions belong in every candidate citation row.

**Dependency graph (source-labelled).**

- O11: Hecke continuation + Landau's prime ideal theorem + Proposition 3.1 ⇒ Theorem 1.1 by amplification and Mellin continuation. Proposition 3.1 ← §4 Poisson comparison ← Proposition 5.1. Proposition 5.1 ← cube inversion (Lemma 5.3), completed estimate (Proposition 5.2), two-Poisson transfer (Proposition 5.4), and finite induction. Proposition 5.2 ← Kubota–Patterson coefficients/automorphy, DR §5 and Appendix A, the extended theta calculation in O11 Appendix A.2, and Goldmakher–Louvel's **number-field quadratic large sieve**. Heath-Brown's quadratic sieve is the predecessor/method; Goldmakher–Louvel is the actual quoted field-specific bound. Appendix A.1 supplies the Gauss–Jacobi/reciprocity identities. **No Hecke zero-density estimate or GRH enters O11.**
- O7 Part I: completed cubic reflection and quadratic sieve + planar additive sieve ⇒ balanced low estimate; truncated-inverse zero detector + sextic sieve ⇒ row count ⇒ balanced high estimate; common-signal continuation ⇒ `11/12`. Part II additionally needs marked reflected energy, compensated low bound, dynamic local Euler identities, marked inverse moments and fourth moments, prime counting in a fixed ray class, and an endpoint certificate ⇒ `7/8`. Its fourth-moment lemma with `κ<1` assumes `β*≤(1+κ)/2`; the application sets `κ=2β*−1` under the contradiction. This is a controlled internal hypothesis, **not assumed GRH**.
- K: unconditional DR cusp formulas + Goldmakher–Louvel + the general Hecke zero-density theorem of Khale–O'Kuhn–Panidapu–Sun–Zhang, Lemma 3.3 ⇒ balanced probe and comparison ⇒ `47/48`. Conductor/multiplicity and CRT calculations replace special row detection/counting. It does not import O7's final theorem as a premise.
- L: O7's analytic estimates and `7/8` conclusion ⇒ changed length bounds; extension of the fourth moment to `13/18≤κ≤1`, with its named zero-free hypothesis, and iteration ⇒ `Bnew`. Optimality is only for the explicitly defined comparison system, not for all cubic-theta arguments.
- CT: the **record** identifies the strategy of the Artin-primitive-root manuscript, general number-field metaplectic theory of Kazhdan–Patterson (and its corrections), and finite-order Hecke conclusions. Its references list the quadratic sieve and other analytic tools, but a reference list alone does not establish a detailed dependency graph. This lane certifies only the stated scope and the reported metaplectic input, pending inspection of the full manuscript.
- DR: §5 coefficients, automorphy and level-aspect Voronoi are unconditional; later prime cancellation/dispersion theorems are separately GRH-conditional. Quasi-RH alone does not discharge those GRH assumptions.

**READING (press, not a mathematical premise).** In Konstantin Kakaes's [Quanta report, 19 October 2026](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/), Sarnak withholds final theorem-level acceptance pending human checking and understanding of all details. Radziwiłł's phrase, “the vast majority of consequences of RH already follow from quasi-RH,” concerns the breadth of consequences, not a quantified percentage. Dunn's “a surprising synthesis of well-known ideas” concerns the use of established techniques, not a claim that every technical adaptation was previously proved. These are compatible positions. None implies RH, certifies a particular Lean build, or licenses dropping a GRH hypothesis from an unrelated theorem.

## D1b. The mechanism, with the exponents exposed

### 1. Möbius cancellation is reciprocal continuation

**PROVED (O11 §3, pp. 11–12; deduction reproduced).** Fix a finite-order character `ν` over `K=Q(ω)`, a finite excluded set `S` containing the primes above `6` and its conductor, and `W∈C_c^∞((0,∞))`. Put

\[
 A_1(D)=\sum_{(\mathfrak n,S)=1}\mu(\mathfrak n)\nu(\mathfrak n)W(N\mathfrak n/D).
\]

Suppose, **for every such test** and every `ε>0`, `A_1(D)≪_{ν,S,W,ε}D^{1−δ+ε}`. Then

\[
 M_W(s)=\int_0^\infty A_1(D)D^{-s}\,\frac{dD}{D}
       =\frac{\widehat W(s)}{L_K^S(s,\nu)}\quad(\Re s>1)
\]

continues holomorphically to `Re s>1−δ`: for a compact set there choose `ε` smaller than its distance from that boundary. Small `D` contributes nothing by compact support. If `ρ` were a zero in this half-plane, choose `W(y)=y^{−ρ}φ(y)` with nonzero nonnegative `φ∈C_c^∞((1,2))`. Then `Ŵ(ρ)=∫φ(y)dy/y>0`, contradicting the continued meromorphic identity `L_K^S M_W=Ŵ`. The principal pole causes no difficulty; a zero under consideration is a holomorphic point. The deleted factors are nonzero in this region. Thus

\[
 \boxed{\text{power saving }\delta\quad\Longrightarrow\quad\Re s>1-\delta\text{ is zero-free}.}
\]

This is the smoothed Littlewood implication needed here, not an assertion that a bound for one fixed test detects every zero.

### 2. The family, its mean square, and the sparse amplifier

**PROVED (O11 §2.2, §3; pp. 4–5, 11).** Primary generators identify ideals prime to `3` with Eisenstein integers `n≡1 mod 3`. Define

\[
 \chi_n(u)=(u/n)_6,\qquad
 A_u(D)=\sum_{(n,S)=1}\mu(n)\nu(n)\chi_n(u)W(Nn/D).
\]

The symbol is zero when `(u,n)≠1`; a zeroth or sixth power of a zero-extended character retains that zero. Proposition 3.1 states, for fixed `0<ϑ≤1/10`,

\[
 \sum_{0<Nu\le H}|A_u(D)|^2
 \ll_{\nu,S,I,\vartheta,\varepsilon}
 \left(\max_{0\le j\le k}\|W^{(j)}\|_\infty\right)^2D^{1+\varepsilon}H,
 \qquad H=D^{1+\vartheta},
\]

where `k=k(ϑ,ε)` and `supp W⊂I⊂(0,∞)` is fixed. This is square-root cancellation **on average in rows**, for this particular Möbius coefficient vector; it is not a pointwise bound in `u`.

For a primary prime `p∉S`, `Y/2<Np≤Y`,

\[
 \chi_n(p^6)=1_{p\nmid n},\qquad
 A_{p^6}(D)-A_1(D)=-\sum_{p\mid n}\mu(n)\nu(n)W(Nn/D)=O_W(D/Y).
\]

Landau supplies `J≍Y/log Y` distinct primes. Set `Y=H^{1/6}`, so their sixth powers lie in the row ball. Cauchy/positivity yields

\[
 |A_1(D)|^2\ll \frac1J\sum_p|A_{p^6}(D)|^2+\frac{D^2}{Y^2}
 \ll D^{1+\varepsilon}H^{5/6}+D^2H^{-1/3}. \tag{Q1.1 = O11 (2.5)}
\]

Consequently

\[
 |A_1(D)|^2\ll D^{11/6+5\vartheta/6+\varepsilon}
                         +D^{5/3-\vartheta/3},
 \qquad
 |A_1(D)|\ll D^{11/12+5\vartheta/12+\varepsilon}.
\]

For each requested positive loss choose a **fixed** sufficiently small `ϑ>0`, then the sieve losses; do not set `ϑ=0` inside the induction. This gives `δ=1/12`, hence `11/12=1−1/12`. At the limiting scale `H=D`, the dominant square exponent is `1+5/6=11/6`; the error square exponent is `5/3`. Their equality would require `H^{7/6}=D`, i.e. `H=D^{6/7}` and a bound of exponent `6/7`. That scale is not available. In particular, this balance does **not** derive `7/8`.

### 3. Row Poisson summation turns Möbius coefficients into theta coefficients

**PROVED (O11 §4, Appendix A.1; pp. 12–18, 35–37).** Normalize

\[
 e(z)=\exp(4\pi i\operatorname{Im}z/\sqrt3),\quad
 d\mu(z)=2\,dx\,dy/\sqrt3,\quad
 \gamma_j(n)=(Nn)^{-1/2}\sum_{x\bmod n}\chi_n(x)^je(x/n),\quad
 \alpha(n)=n/|n|.
\]

The pairing `e(zy)` makes `O` self-dual and its covolume one. Expand the square, first extract `(n₁,n₂)`, then Poisson-sum the row `u` with its coprimality mask retained. Primitive multiplicative Fourier transforms contribute Gauss sums. The exact conversion, visually verified on O11 PDF p. 5, is

\[
 \boxed{\mu(n)\gamma_{-1}(n)
  =\chi_n(-1)G(n)^{-1}\overline{\alpha(n)}\gamma_2(n),\qquad
  G(n)=\overline{\chi_n(4)}\gamma_3(n).} \tag{Q1.2}
\]

The brief and the plain-text extraction lose both conjugation bars. The intermediate identities are `γ₂(n)³=μ(n)α(n)`, `γ₁(n)γ₂(n)=μ(n)α(n)G(n)` and `γ₁(n)γ₋₁(n)=χ_n(−1)`; division and `α⁻¹=\bar α` give (Q1.2). Appendix A.1 proves the prime identity by Gauss–Jacobi identities and `J(χ_p²,χ_p²)=−p`; CRT gives one minus sign per prime factor, hence `μ(n)`. The quadratic Gauss factor and reciprocity sign depend only on a fixed ray class and can be expanded into finitely many fixed characters. **It is `μ(n)` multiplied by the Fourier Gauss factor that becomes a cubic coefficient; `μ` itself is not a theta coefficient.** This is the exact arithmetic bridge, not a geometric counting interpretation.

With `a_ξ(n)=\overline{α(n)}γ₂(n)ξ(n)`, the schematic dual sum and comparison are

\[
 B_h(X)=\sum_{n\ {
m sf}}a_\xi(n)\chi_n(h)U(Nn/X),\qquad
 \mathcal H\asymp D^2/H,
\]
\[
 \sum_{Nu\le H}|A_u(D)|^2\preccurlyeq DH+
       \frac{H}{D}\sum_{0<Nh\ll\mathcal H}|B_h(D)|^2.
\]

Thus a dual bound `Σ_h|B_h(D)|²≼D²` suffices. The rigorous version is `E(H,X,F)` in (4.9), with an auxiliary squarefree index `f` and twist `χ_n(f)^4`; exclusions are removed by `(X,F)→(X/Nd,FNd)`, preserving `XF`. Suppressing this auxiliary index is an outline, not the full proof.

### 4. Cube completion, automorphy, and the quadratic sieve

**PROVED (O11 §6 and Appendix A.2; DR §5, especially (5.4)–(5.8), Lemma 5.2, Corollary 5.1).** Kubota's theta is a residue of a cubic metaplectic Eisenstein series on `H³=C×R_{>0}`. In the cited normalization,

\[
 \theta(z,v)=\frac{3^{5/2}}2v^{2/3}
  +\sum_{0\ne\ell\in\lambda^{-3}O}\tau(\ell)vK_{1/3}(4\pi|\ell|v)
          e^{2\pi i(\ell z+\overline{\ell z})},\quad\lambda=1+2\omega.
\]

O11's `c_θ(nb³)` is the coefficient of **`\bar θ`** at `λ^{−3}nb³`, not of `θ` without conjugation. For primary squarefree `n` and arbitrary primary `b`, away from `6`, Patterson's formula is

\[
 \boxed{c_\theta(nb^3)=3^{5/2}|b|\,\overline{\chi_n(\lambda)^2}\,\gamma_2(n).} \tag{Q1.3}
\]

Here `n,b` may share primes. Complete the squarefree column sum by inserting all such cube indices:

\[
 T_h(X)=\frac{1}{3^{5/2}\sqrt X}\sum_{n\ {
m sf},b}
 c_\theta(nb^3)\overline{\alpha(nb^3)}\chi_{nb^3}(\lambda)^2
 \xi(nb^3)\chi_{nb^3}(h)U(N(nb^3)/X).
\]

Its `b=1` part is `P_h(X)=X^{−1/2}B_h(X)`. The transformation is applied to the **completed** sum, not to the isolated squarefree coefficients. Precisely, DR has scalar automorphy on `Γ₂=⟨SL₂(Z),Γ₁(3)⟩`, with cubic multiplier `κ(γ)=(c/a)₃` on `Γ₁(3)`; full `SL₂(O)` permutes the cusp components. Calling this scalar invariance under all `SL₂(O)` is too strong.

For a squarefree moving row `h`, automorphy at rational cusps transforms the columns to length `Nh²/X`, with schematic summands

\[
 \sum_{m\ne0}\frac{d_\theta(m)\overline{\alpha(m)}}{\sqrt{Nm}}
       \chi_h(m)^3V_*^\sharp(NmX/Nh^2).
\]

The cusp sequences and additive phases are independent of `h` within fixed ray classes (O11 Lemma 6.3). Locally the finite Fourier exponent `−1` combines with the conjugate cubic multiplier `−2` to give `−3≡3 mod 6`: the new twist is **quadratic**. O11 Proposition 6.2 also handles nonprimitive local masks (`j=0,4`) explicitly. The horizontal derivative kills cusp constants, giving an entire Mellin object and the gamma quotient with `7/6±t,5/6±t`; it is not legitimate simply to drop a constant-term residue without this derivative.

Goldmakher–Louvel gives, for squarefree quadratic row and column ranges `M,L`,

\[
 \sum_{k\ {
m sf},Nk\le M}\left|\sum_{n\ {
m sf},Nn\asymp L}
       b_n\chi_k(n)^3\right|^2
 \ll_\varepsilon(ML)^\varepsilon(M+L)\sum_n|b_n|^2.
\]

The general higher-order sieve has an **additional** `(ML)^{2/3}` term; the comparison is not literally `(M+L)` versus a lone `(ML)^{2/3}`. Cube-variable Cauchy, smooth separation, cusp coefficient bounds, and summation over repeated row factors give

\[
 \sum_{0<Nh\ll\mathcal H}|T_h(X)|^2\preccurlyeq
       \mathcal H+\mathcal H^2/X. \tag{Q1.4}
\]

The full Proposition 5.2 has `H+H²Nf/X`. Writing `k=u₀sv²` and absorbing `v²` into `f` costs `Σ_v(Nv)^{−2}<∞`; thus arbitrary rows are included.

### 5. Undo the cubes without throwing away cancellations

**PROVED (O11 §5–§7; schematic formulas are §2.5).** Complete multiplicativity gives

\[
 T_h(X)=\sum_b\frac{w_h(b)}{Nb}P_h(X/(Nb)^3),\qquad
 w_h(b)=\overline{\alpha(b)}^{,3}\xi(b)^3\chi_b(h)^3,
\]
\[
 P_h(X)=\sum_d\frac{\mu(d)w_h(d)}{Nd}T_h(X/(Nd)^3).
\]

The coefficient at total cube index `b` is `w_h(b)Σ_{d|b}μ(d)=1_{b=1}`. It would be false to bound the `b=1` piece by the completed sum by positivity: different cube contributions can cancel. Truncate the inverse sum at

\[
 H_c^3=\min\{X,X^2/\mathcal H^2\}.
\]

Its short part has mean square `≼\mathcal H+\mathcal H²H_c³/X≼X` when `\mathcal H≤X`. The long part recombines to shorter columns `L_b=X/(Nb)³`, with divisor-bounded coefficients, leaving a supremum of energies `E(\mathcal H,L_b)`.

Two Poisson transformations close the recursion. The first turns cubic coefficients back into Möbius coefficients; enlarge its nonnegative row range from `L_b²/\mathcal H` to `Y=XL_b/\mathcal H`; the second turns them back into cubic coefficients at

\[
 (\mathcal H',X')=(\mathcal H L_b/X,L_b),\qquad
 \mathcal H'/X'=\mathcal H/X,
\]
\[
 \frac{E(\mathcal H,X)}X\preccurlyeq1+
       \sup_{Nb>H_c}\frac{E(\mathcal H',X')}{X'}.
\]

At `X≈D`, `\mathcal H≈D^{1−ϑ}`, one has `H_c≈D^{2ϑ/3}` and `\mathcal H'<D^{−2ϑ}\mathcal H`. After finitely many steps, depending on `ϑ`, counting handles row ranges at most one. In the full statement, `Σ=XF`, `H≤ΣD^{−κ}`, and the transfer preserves `H'/Σ'≤H/Σ`, with `H'≤HL/(ΣF)`, `Σ'≤L` (Propositions 5.1, 5.4). Derivative orders increase finitely (`4m+12`) and losses are allocated before the large scale is taken.

The diagonal/zero frequency supplies `DH` in the original mean square, or `O(H)` in normalized dual energy. In §7.3 the preimage signs are summed **before** absolute values: the local cancellation leaves `1_{p|k'}` and hence `f'|k'`, essential to the admissible new scales. These details explain why the transfer is more than formal double Fourier inversion. Section 7 proves this transfer proposition; **it is not the Dirichlet-L transfer**, which occurs already in §3.

### The 7/8 refinement (source-level synopsis of the statements)

**PROVED (O7, claimed theorem; analytic statements inspected, Part II proofs not independently audited).** Part I's probe `Iη(X,Y,Z)` uses completed cubic coefficients, not just the sum `A₁`. At `X=Y=Z^{1/2}`, the squared theta row norm is `≪Z^{1+ε}`, the squared additive norm is `≪Z^{1/2}`, and the outside normalization is `Z^{−1/2}`. Cauchy gives `J_I,η≪Z^{1/4+ε}` (Proposition 6.3, p. 47). Its principal signal has exponent `C_I(s)=s−2/3`. Thus the low boundary is `1/4+2/3=11/12`.

On the high side, Poisson frequencies are `ua⁶` with `u` sixth-power-free. The Euler quotient contains a numerator Hecke L-function and the reciprocal of a twist of the target. Bins locate zeros only to choose buffered contours, not as computational input. Proposition 8.3 (pp. 58–59) gives **two saturated witnesses** for one row character at one height: with `δ=2a−1`, `t∈[1,3/2]`, lengths `D=U^r,N=U^m`,

\[
 t-1/2-O(\varepsilon)\le r\le t+o(1),\quad
 0\le m\le1/2+O(\varepsilon),\quad r+m\ge t-o(1),
 \quad |M_r|^2\gg U^{\delta r-\varepsilon},\quad |S_m|^2\gg U^{\delta m-\varepsilon}.
\]

Part I uses only the inverse witness. The sextic sieve and powerful-part counting give Proposition 9.2's row exponent `R(δ)=min{1,max{1−δ/2,4/3−δ}}`, with a fixed polynomial height cost; the floor bin uses volume only. These detector and sieve statements are in **Part I**, although Part II reuses them.

Part II applies a finite prime compensation to the physical probe, one factor at a time:
`η(p)Iη;p(X,Y,Z Np)−(Np)^{−3/2}Iη(X/Np,Y/Np,Z)`. All prime windows stay fixed, disjoint, and in the identity ray class. It cancels an unwanted scalar Euler contribution without dividing by a possibly zero raw local factor. The geometry is

\[
 b=1/8,\quad\ell=1/6,\quad l_x=17/48,\quad l_y=23/48,\quad
 h=13/16,\quad l_x+l_y+\ell=1.
\]

The refined additive Gram bound and marked reflected energy give Proposition 15.3 (p. 107):

\[
 |J_{II,\eta}(Z)|\ll Z^{l_x/2+b/12+\varepsilon}
  =Z^{17/96+1/96+\varepsilon}=Z^{3/16+\varepsilon}.
\]

The signal is now `C_II(s)=s−11/16`, so

\[
 \boxed{C_{II}(7/8)=7/8-11/16=3/16.} \tag{Q1.5}
\]

The high comparison requires two new moment recursions: Lemma 17.1 for `M_u Q_u` when `r+2z<m`, `2r+8z<3m` by fixed margins; Lemma 18.1 for products of two plain polynomials and short prime factors, with `n₁+n₂+6κz≤M`, the designated nonprincipal row family, and `β*≤(1+κ)/2` when `κ<1`. The application uses the dynamic `κ=2β*−1`. The unmarked amplified inverse exponent is `e(r)=max{1,(1+5r)/6}` (Lemma 17.6).

Proposition 19.2 combines the two witnesses using `α=5/6`, `x∈[0,1/2]`, `D_x=3−17x/9`, `P_x=2−(8x/9)(1−x)`. It balances

\[
 R_{\rm short}(t)=1-\delta+\frac{\delta P_x}{D_x}(3/2-t),\qquad
 L(t)=1-\delta+(\alpha-\delta)(t-1)
\]

at `t=1+δP_x/(2J)`, `J=(α−δ)D_x+δP_x`. The row exponent costs at most the balanced value plus `Δ/4+ε`, where `Δ=β*−7/8`. The main endpoint relative exponent is

\[
 E_*=-1/48+2\delta/3+x\delta/6-(13/16)(1-R_*).
\]

Lemma 20.2 proves `−E_*≥49/440640>1/10000` by an exact completed-square certificate. It is a high-side margin, not the derivation of the low boundary. The late height/mesh choices in Proposition 20.3 give a target-independent positive saving against `C_II(β*)`; the common-signal Proposition 2.1 then contradicts the supremum. No zero attaining that supremum is assumed.

### Kintali's shortcut

**PROVED (K, source-labelled).** Retain the balanced probe and `C(s)=s−2/3`. Cubic reflection plus the quadratic sieve and a planar additive Gram estimate give `Jη(Z)≪Z^{1/4+ε}`. The principal row is identified by CRT and inertia: for rows of norm `U` the primitive conductor is `Oη(U)`, and a fixed primitive character occurs in at most twelve physical sixth-power-free rows (Lemma 2). Two residues give

\[
 f_\eta(Z)=\frac1{2\pi i}\int_{(2)}Z^{s-2/3}e^{(s-5/6)^2}
                   \frac{H_\eta(s)}{L_F^S(s,\eta)}\,ds,\qquad |H_\eta-1|\le1/2
 \quad(\Re s>11/12).
\]

Replace O7's saturated detector, sextic row sieve, and marked inverse/fourth-moment machinery by the general Hecke zero-density theorem. It gives `#B_a≪U^{min(1,5(1−a))+ε}(1+T)^A`. At the central row scale `d=1/2`, the exponent relative to `C(β*)` is

\[
 E(1/2,a)=a-\beta_*+\tfrac12\min\{1,5(1-a)\}-1/3
 \le29/30-\beta_*.
\]

Under `β*>47/48`, this is `<−1/80`; extending to `d≤501/1000` costs at most `1/1000`. Principal/outer rows, contours, and late height choices leave `Jη−fη≪Z^{β*−2/3−1/4800}`. The low bound and rapid decay of the signal at zero continue its Mellin transform across `β*` by that uniform amount, a contradiction. The method deliberately spends margin and does not optimise `47/48`. It avoids **O7 estimates with internal hypotheses**, not unproved external GRH assumptions in O7: O7 claims an unconditional theorem already. DR's conditional prime asymptotic and dispersion are avoided by all three arguments.

### Liu's optimisation

**PROVED (L, source-labelled); arithmetic checked below.** For balanced lengths `l_x=(1−b−ℓ)/2`, `l_y=(1+b−ℓ)/2`, the equality between the low exponent and `C_b(s)=s−(4+b)/6` gives `B=11/12−ℓ/4`, independent of `b`. Increasing `ℓ` is constrained by the high comparison. At the critical amplitude `x=1/2`, the class with row exponent `2/3` eliminates the freedom in `b`; tangency fixes it. Extending the plain fourth moment from `κ≥3/4` to `κ≥13/18`, and iterating the previously proved bound to license the next `κ`, gives the cubic and `Bnew` in D1a. Theorem 34.4 is optimality **of the supplied upper-bound comparison system**, including allowed cutoffs and contours. It explicitly does not rule out stronger analytic estimates.

### Cureton–Thorner

**PROVED (reported source conclusion); proof-detail audit OPEN.** The supplied Hexagon record and author repository state `ζ_K(s)≠0` for `Re s>31/32` for every number field, and the finite-order Hecke corollary. The record identifies the hard generalisation as formalising Kazhdan–Patterson's metaplectic forms, instead of relying only on the explicit Eisenstein-integer cubic-theta setting. This extends the **field scope**, not the strength of the boundary for Dirichlet L-functions. Passing from Dedekind zetas of abelian extensions to their finite-order Hecke factors is the relevant Artin/class-field factorisation; nonprincipal nonvanishing at `1` needs the usual separate pole bookkeeping. Neither the record nor the inspected README supplies enough argument to reconstruct its `31/32` exponent, and no such reconstruction is invented here.

## D1c. Why it stops

**READING, with the algebraic obstructions PROVED.** The O11 output pays for extracting one coefficient vector from an average over `≍H` arithmetic rows. Its prime-sixth-power rows number `J≍H^{1/6}/log H`; their fraction is `H^{−5/6}/log H`. The mean square allows a selected row to be larger than the root-mean-square by `√(H/J)≈H^{5/12}`. At `H≈D`, this converts `D^{1/2}` into `D^{11/12}`. Using all sixth powers would at most remove the prime logarithm; it would not change the exponent `1/6`.

The loss ledger is:

| Place | Quantitative cost | What is, and is not, a potential improvement |
|---|---|---|
| Sixth-power selection | `H/J≈H^{5/6}` in the square | A power loss. A denser **effective** amplifier or coefficient-specific evaluation bound would matter most once the family estimate is optimal. |
| Deleted prime in `A_{p⁶}` | `D/Y`, squared `D²H^{−1/3}` | Another power-scale obstacle to an RH-strength use of this exact inequality. It is subdominant at the proved scales; removing it alone leaves `11/12`. |
| Quadratic large sieve | `(ML)^ε(M+L)` | Order-optimal for general coefficient vectors: one column forces a row-size term, and coefficients aligned with one row force a column-size term. Positivity alone only gives a much worse bound. The sieve is deep quantitative near-orthogonality, not a lossless identity, and special coefficients might admit extra cancellation. |
| Cube completion/inversion | Short inverse piece `H+H²H_c³/X`; long cube divisors | The genuine bookkeeping difficulty. The iteration handles it without a further **fixed** exponent loss in the final range `H_original>D^{1+ϑ}`. It does impose a strict scale gap and finite-depth smoothness costs. It is not an extra independent `1/12` loss. |
| `D^ε`, logarithms, divisor counts | Arbitrarily small powers, fixed after margins | They affect constants/endpoints and cannot account for the fixed distance to `1/2`. Letting `ϑ→0+` means a separate estimate for each loss, not uniform constants at `ϑ=0`. |

Even granting the same mean square for every `H`, minimising **the unaltered** (Q1.1) gives exponent `6/7`, not `1/2`. Thus extending the range alone cannot make that displayed amplifier RH-strength. There is an exact way to remove its crude deletion error:

\[
 A_1(D)=A_{p^6}(D)-\nu(p)A_{p^6}(D/Np),
\]

with the same smooth `W`; split squarefree ideals by whether they contain `p`. Exploiting this requires estimates at the shorter column scale with a common outer row range, and still does not fix the sparse-row loss. It is a useful finite check, not a new proof of an improved half-plane.

For a nonnegative amplifier supported on `J` nearly identical rows, an RH-scale deduction from `Σ|A_u|²≪DH` would need `H/J=D^{o(1)}` **and** approximation error `D^{1/2+o(1)}`. More generally one needs an evaluation inequality on the *arithmetic coefficient subspace*,

\[
 |A_1(D)|^2\le D^{o(1)}\frac1H\sum_{Nu\le H}|A_u(D)|^2
                  +D^{1+o(1)}. \tag{H-EVAL}
\]

This can come from coherent reconstruction, not necessarily many identical rows. It is the missing input for that route, not a consequence of the average.

Liu proves that changing the admitted parameters **within his fixed exponent-comparison system** cannot beat `Bnew`; he already improves `7/8` slightly. He does not prove that no single analytic improvement can help. Nor does his optimisation identify a universally best estimate to improve. For the elementary O11 extraction, the amplifier is the visible dominant cost; for O7/L, the critical row class and moment capacities constrain one another. The assertion “none can help” is correct only for parameter variation with all those bounds unchanged.

Calling the mean square “RH on average” is useful shorthand for a square-root-size norm bound. Calling a lossless evaluation estimate the ladder's “finite rank” is **not justified**: rank and bounded evaluation are different data, and positive spectral control is additional to both (D2 below).

## D2. Mapping onto the ladder

The project pages are Markdown, so section numbers and file/line locators replace printed page numbers. Each verdict states the strength of the identification, not a judgement of usefulness.

### D2.1. Sextic twists, fluxes, and the two meanings of average

**ANALOGY; the coefficient ring and character laws are EXACT.** O11 §2.2, p. 4 matches `zn-flux.md` §§1–2, 4–5 and `graph-super.md` §§3, 6. Algebraically `Z[ω]=Z[ζ₆]`, and the phase values lie in `μ₆`. At fixed nonzero `u`, `n↦(u/n)₆` is a Kummer Hecke character away from its ramification; O7 Lemma 4.1 identifies it with Frobenius on `K(u^{1/6})`. That is a legitimate arithmetic counterpart of holonomy around cycles. But `u` in a norm ball is **not itself a finite flux group**: the balls grow, conductors vary, and nonunit zeros matter. The underlying Kummer classes live in `K×/(K×)^6`; this is not the fixed graph group `H¹(Y,Z/6)` or the project lattice `O^{2n}`. The column `n` is a squarefree ideal/product of prime ideals, not a single prime cycle.

Here is the precise graph object for Q2. Let `𝒫_Y` consist of oriented primitive closed nonbacktracking cycles modulo cyclic shift, with reversal a different prime. Its effective divisors form the **free commutative monoid**

\[
 \mathcal M_Y=\{n=\prod_P P^{e_P}\},\quad
 \deg n=\sum_Pe_P\ell(P),\quad
 \mu_Y(n)=\begin{cases}(-1)^{\#\{P:e_P=1\}},&e_P\in\{0,1\},\\0,&\text{otherwise}.\end{cases}
\]

For `s∈H¹(Y,Z/N)` set `χ_n(s)=ζ_N^{⟨s,[n]⟩}` and, with fixed multiplicative unit-modulus `ν`,

\[
 A^Y_s(d)=\sum_{\deg n=d}\mu_Y(n)\nu(n)\chi_n(s).
\]

For each `c∈H₁(Y,Z/N)` put `b_c(d)=Σ_{deg n=d,[n]=c}μ_Y(n)ν(n)`. Character orthogonality gives the **EXACT** identity

\[
 \frac1{N^g}\sum_s|A^Y_s(d)|^2=\sum_c|b_c(d)|^2
 =\sum_{\substack{\deg n=\deg n'=d\\ \mathrm{cl}_N(n)=\mathrm{cl}_N(n')}}
       \mu_Y(n)\mu_Y(n')\nu(n)\overline{\nu(n')}.
 \tag{Q1.6}
\]

A possible analogue to test is `Σ_c|b_c(d)|²≪C(Y,ν,ε)q^{(1+ε)d}`, with any meaningful **uniformity in varying graphs** stated explicitly. Orthogonality proves the identity, not this bound; the off-diagonal terms have signs, so the diagonal is not a lower bound for the whole energy.

There is a decisive caveat for `ν` a graph flux (including `ν=1`):

\[
 \sum_{d\ge0}A^Y_s(d)z^d=\prod_P(1-\chi_P(s)z^{\ell(P)})
                         =\det(I-zB_s).
\]

Thus `A^Y_s(d)=0` for `d>2|E|`. A fixed-graph exponential upper bound is then vacuous and gives **no** restriction on the zeros of that determinant, which are the **poles** of Ihara zeta. The ordinary graph zeta has no finite zeros. Q2's proposed graph Littlewood equivalence must therefore be refuted, not proved. The appropriate spectrum-sensitive objects are traces `Tr B_s^k`, a reciprocal determinant's coefficients, or the correctly separated super/fermionic numerator. A polynomial may have zeros anywhere while all its sufficiently high Taylor coefficients vanish.

Finally, `N^{−g}Σ_s det(x−A_s)=μ(Y,x)` is a **linear average of polynomials** with a real-rooted result (Heilmann–Lieb); (Q1.6) is a **quadratic average of coefficient sums**. Neither is the other's assertion. The graph already supplies the exact warning against identifying them.

### D2.2. The amplifier and torsion

**ANALOGY in the annihilator mechanism; NONE as an existing graph or level-tower amplifier.** O11 §2.2, p. 5 compares with `zn-flux.md` §4 and `lattice-tower.md` §§2–4. In each multiplicative unit quotient, a sixth power annihilates every sextic character. Its arithmetic representatives `p⁶` are many distinct norm-bounded rows, and only divisibility by `p` distinguishes them from the trivial row. In additive graph notation, `Ns=0` for every `Z/N` flux; `N` times an integral lift gives the **same** zero flux. Counting its different lifts as independent rows repeats the same datum and repeats the mean-square budget. There are no prime-divisibility deletions on which the graph holonomy vanishes.

The `N`-torsion average is the *dual* orthogonality operation selecting classes in `NH₁`; it is not selection of many distinct representatives of a trivial Kummer class. Nor is `H¹(Y,Z/N)` identical to all `N`-torsion of the syndrome torus `R^{2n}/L`: the former has cycle rank `g`, the latter has phase-space rank `2n`. The point tower also depends on an integral step. These similarities explain the torsion vocabulary but supply no density gain. `lattice-tower.md` §4 already proves that a tower can coexist with a hyperbolic, non-RH step.

### D2.3. Poisson and the Fourier gate

**EXACT for Fourier/Poisson duality; ANALOGY for the full arithmetic transformation.** O11 Lemma 4.2, pp. 13–14, is an instance of the Fourier gate in `functional-equation-gate.md` §3(a,b) and `gate-phases.md` §3.2. The field changes from `Q` to `K`, and the different is absorbed into the additive character `e(z)=exp(2πi Tr(z/λ))`. Consequently `O` is self-dual for this particular planar pairing. Finite components give character Gauss sums, exactly as charged local states do in lane I.

What is exact is the operator identity and Poisson summation with specified measures, not an identification of the row average with the project Weil functional. The multiplicative Gauss–Jacobi identity (Q1.2), and particularly the fixed ray-class correction, are extra arithmetic. **NONE** of the existing lattice/GKP statements alone asserts that Möbius is absorbed into a cubic theta coefficient.

### D2.4. D-Θ: cubic theta versus the qunaught

**ANALOGY; the literal “a Z₃ displacement of the qunaught” claim is REFUTED.** Compare O11 §2.4, p. 6, §6, Appendix A.2 and DR §5.1–§5.3 with `curve-bridge.md` §3, `graph-super.md` §3, `zn-flux.md` §2, and `functional-equation-gate.md` §§1–3.

\[
 \Theta_{K_0}=\sum_{x\in K_0}\delta_x,\qquad
 \langle\Theta_{K_0},1_D\rangle=\#L(D)=q^{h^0(D)}
 \quad(K_0=\mathbb F_q(C)),
\]
\[
 \Theta_s^{\rm graph}=\sum_{x\in H_1(Y,\mathbb Z)}\zeta_3^{\langle s,x\rangle}\delta_x,
 \qquad
 \theta(z,v)=\tfrac{3^{5/2}}2v^{2/3}+\sum_\ell\tau(\ell)vK_{1/3}(4\pi|\ell|v)\check e(\ell z).
\]

| Structure | Project comb/qunaught | Cubic theta | Verdict |
|---|---|---|---|
| Discrete arithmetic support | Additive lattice or global field; additive character displacements | Fourier indices in fractional Eisenstein lattices; away from `λ`, valuations only `0,1 mod 3` after squarefree-cube decomposition | Lattice indexing is shared; coefficient support is different. |
| Coefficients | Unit amplitudes/characters for a comb; positive integral counts against `1_D` | Cubic Gauss sums and absolute-value weights, complex phases and zero coefficients | No count identification. |
| Symmetry | Heisenberg stabilisers and ordinary Fourier/Weil action (quadratic metaplectic setting) | Cubic multiplier on `Γ₂`; vector of cusp components under `SL₂(O)`; genuine cubic metaplectic origin | A cubic cover is not merely the usual Fourier gate's sign ambiguity. |
| Ambient object | Distributional state in a representation of the additive Heisenberg group; code Hilbert space after a choice of model | Automorphic function on hyperbolic three-space, obtained as an Eisenstein residue | No supplied isometry, intertwiner, or stabiliser code. |
| Reflection | Fourier exchanges dual additive lattices and inverts squeeze | Rational-cusp transformation plus cubic character multiplier and a Bessel/Mellin kernel | Related transformations, not the same asserted state. |
| Positivity | Counts or Hilbert norms; neither alone proves RH | Norm estimates for transformed character rows | No finite-field polarisation is constructed. |

A precise **literal** D-Θ would demand that the local cubic-character state be a Weyl displacement of a self-dual comb, with the theta reflection realised by the ordinary Clifford Fourier gate. It fails already on the smallest prime residue field admitting a nontrivial cubic character: `F₇`. The vector `v(x)=χ₃(x)` extended by zero has six nonzero coordinates; a one-qudit pure stabiliser state in prime dimension seven has support one or seven in the computational basis (eigenvectors of `Z` or `XZ^a`). So it is not such a displaced stabiliser state. This is a finite obstruction to the literal local-state identification, **not** a proof that no more elaborate representation-theoretic bridge can exist.

A defensible repaired D-Θ asks for a **charged, generally non-stabiliser, metaplectic state construction** with the correct cubic cocycle, all cusp components, zero masks and coefficient formula. Its reflection must produce `j↦−j−2 mod 6`, including the exceptional local factors for `j=0,4`. “Theta” alone does not supply that construction. Notice also that `Z[ζ₃]=Z[ζ₆]`: the common ring does not identify the order-three multiplier with the order-six twisting family. Lane D's trace-form lattice over this ring carries qutrit discriminant data; it is not automatically a qunaught.

### D2.5. Quadratic large sieve and positivity

**ANALOGY to Hilbert/Gram positivity; NONE to Weil positivity or the window criterion.** O11 Lemma 6.5, p. 25, is an operator-norm bound for a character matrix `T`; its square is the positive Gram matrix `T*T`. It belongs with finite Fourier/Plancherel and Bessel inequalities. Positivity makes enlargement of a row sum legal, but the bound `M+L` requires arithmetic quasi-orthogonality, not just `T*T≥0`.

The distinction already appears in `data-ladder.md` §4b: positivity for the Plancherel trace is unconditional, whereas positivity of the **specific** Lefschetz/Weil functional is RH. It is not the disputed overlap positivity. It is also not Carathéodory–Toeplitz positivity of `window-similitude.md` §3: that theorem concerns the moment matrix of the spectral/Weil distribution. No identity identifies the sieve Gram matrix with that moment matrix. Cubic automorphy gives access to a useful positive norm; it does not make the target Weil form positive on all tests.

### D2.6. Quadratic base change, CM lattices, and gate phases

**EXACT as an L-function factorisation; ANALOGY to lane C's lattice; NONE as a global CM-RH deduction.** O11 §3, p. 12; O7 Proposition 11.3, p. 84; K §5.2 give, after common deletion of finitely many bad factors,

\[
 L_{\mathbb Q(\sqrt{-3})}(s,\chi\circ N)
       =L(s,\chi)L(s,\chi\chi_{-3}).
\]

At split primes there are two equal linear factors; at inert primes their product is `1/(1−χ(p)²p^{−2s})`. Pole-zero cancellation at `1` is separately excluded (`L(1,χ_{−3})>0`). This is induction/base change for a quadratic extension, not the Fourier gate itself. In the notebook it is closest to `zn-flux.md` §5.2's Artin factorisation, alongside `cm-lift.md` §§1.2, 2.5 and `gate-phases.md` §§1.2, 4.

The same named quadratic character `χ_{−3}` twists 49a1 to 441d1, but there the base field is **`Q(√−7)`** and the elliptic Hecke character has nonzero infinity type, even after unitary normalization. O11/O7/L cover finite-order characters over `Q(√−3)`; CT covers finite-order characters over any field. **Neither scope includes those elliptic Hecke characters.** A common local lattice and vacuum are not the base-change theorem. The finite-order Dirichlet twisting character is covered; the resulting weight-two elliptic L-function is not thereby covered. Lane C's local/global negative finding survives.

### D2.7. Geometry, D-G, and the meaning of finite rank

**ANALOGY as an alternative global method; the proposed exact D-G is REFUTED.** The decisive automorphic object is global cubic theta, so the proof certainly does not use only a collection of unrelated local bounds. In the explicit Eisenstein setting its geometry is arithmetic hyperbolic/metaplectic geometry, not a finite-field curve with an ample polarisation. It also uses reciprocity, quadratic sieves, counting and analytic continuation; saying theta is the *only* geometric ingredient is an interpretive classification, not a dependency theorem.

D-G's first repair is to replace “a finite family” by a **scale-growing family**, of `≍H` rows and varying conductor. Its second is to distinguish the two spaces whose ranks are discussed: the twist matrix's row/column space and the hypothetical spectral `H¹` on which global zeros are eigenmodes. They have not been identified. Its third is to replace “the gap is exactly average versus pointwise” by the quantitative evaluation problem (H-EVAL). O7 already yields a pointwise zero-free statement for every target; its distance to `1/2` reflects the estimates used to get it, not simply a missing logical quantifier.

Finite rank alone cannot make one member suffice. The exact rank-two integral similitude

\[
 M=\begin{pmatrix}5&-5\\1&0\end{pmatrix},\qquad
 M^T\Omega M=5\Omega,\qquad
 \operatorname{spec}M=\{(5+\sqrt5)/2,(5-\sqrt5)/2\}
\]

fails the Weil modulus condition. It has the finite lattice and step, but no invariant positive vacuum. Likewise a rank-one function supported only at the trivial flux has target/mean-square ratio equal to the number of fluxes: **small rank can coexist with maximally bad evaluation**. A lossless amplifier would need uniform coherence or a reproducing-kernel bound placing the target row at typical norm on the relevant arithmetic subspace, plus control of deletions. That is extra to rank, torsion and a shared coefficient ring.

`family-vacuum.md` Proposition 1 concerns **commuting similitudes on one symplectic space**. The twist family has not supplied such operators or a common symplectic form, so it cannot invoke that theorem. `window-similitude.md` R1–R3 concerns translation invariance and spectral rank; the curve rank is the number of **distinct** spectral atoms (at most `2g`, equal for distinct phases), with multiplicities recorded as weights, not additional independent atoms. Its zeta full-rank discussion is explicitly in the critical-zero model. Quasi-RH supplies neither that model's positivity nor a finite-rank quotient.

**READING for the notebook.** The ladder's claim that finite-field geometry supplies the known finite-rung polarisation remains a useful description; any claim that such geometry is *necessary for every fixed zero-free strip* must be weakened. Cubic-theta automorphy and Hilbert-space estimates supply a different route to a global strip. They supply no global integral `H¹` for zeta, and no proof of positivity of its Weil functional. “Finite rank is needed” is a research programme for the proposed cohomological realisation, not a theorem about all possible RH proofs.

### D2.8. Cube inversion and the scale iteration

**NONE as an existing ladder operation; ANALOGY to a family closed under Fourier transfer.** O11 §§5, 7, pp. 18–22, 29–34 need Möbius convolution over cube divisors, common-factor masks, and a contraction of row/column scales. The lattice point tower in `lattice-tower.md` changes finite syndrome groups under powers of an **integral step**. The analytic recursion has no such fixed step or finite-rank state space. The exact common theme is retaining enough auxiliary data to close a transformation; it does not identify the two constructions. This is the unmatched fifth step of the five-step mechanism.

## D3. Consequences for the record

**PROVED (text audit); source-dependent consequences are labelled.** The scan covers `db/claims.tsv`, every `report/sections/*.tex`, and every `notes/**/*.md`, excluding this output directory to avoid self-matches. It includes the requested broad `conditional` scan in the database and spelling variants of zero-free/zero-density. The reproducible inventory is `checks/record_scan.py`; `checks/output_record_scan.txt` retains exact matches, and `checks/output_record_classification.tsv` gives each occurrence an ID, location and disposition. Draft briefs and the concurrent Q2 work are distinguished from the pre-existing record. No registered row or other page was edited.

The audit finds **no pre-existing claim with “no Siegel zeros” or a fixed quasi-RH strip as its sole unproved hypothesis**, and no explicit “GRH-up-to-ε” assumption that O7 alone discharges. Most `Siegel` hits concern theta, Siegel space, Siegel sets or the graph Brauer–Siegel paper. “Zero-free construction” often means *a construction not using a zero list*, not a nonvanishing region. Counting zeros by `N(T)≈T log T` is also different from bounding zeros to the right of a vertical line.

The table lists each distinct relevant mathematical assertion, grouping duplicate mentions under its registered ID or stable file/section ID. “Partially” means a weaker replacement or stronger auxiliary input is available, **not** that the original claim has become proved.

| ID / location (duplicate occurrences retained in the scan) | Original dependence | Does O7 make it unconditional? |
|---|---|---|
| `asm:zeta-standard`, `09b_selberg_dictionary.tex:69–77`; `notes/selberg/astra-proofs.md` T5.1; review | Meromorphic continuation, FE, zero-free line and `ζ'/ζ(1+ε+it)≪log²(3+abs(t))` | **Partially supplies a stronger location input; no new theorem status.** These were already classical unconditional facts, stored as external assumptions for provenance. O7 does not itself supply every fact in the package. Keep the classical references and add the stronger strip separately. |
| `prop:finite-euler-spectrum`, database line 70; `notes/selberg/astra-proofs.md` T1.3; ledger `G4-T15-4`, `L14-009` | Disjointness from continued zeta zeros uses H-ZETA/H-GAMMA | **Already unconditional given cited classical inputs.** O7 is stronger than needed; it does not create zeros in finite Euler products or recover them from prime circles. |
| `notes/what-rh-has-become.md:146`, §5 hierarchy; `report/sections/03_what_rh_has_become.tex:158`; ledger `G1-T2-3` and copies | Classical shrinking zero-free region gives PNT error | **Partially: strengthen the middle rung.** A fixed strip gives a fixed power saving, e.g. `ψ(x)=x+O_ε(x^{7/8+ε})` by the usual explicit-formula argument. It does not give square-root error. The matrix analogy should not confuse a shrinking classical strip with a fixed spectral gap. |
| `notes/metric-tomography/metric-as-state.md` §4.4, lines 136–143 | Describes then-strongest unconditional density and zero-free information | **Outdated survey, not a conditional theorem.** Add the fixed strip and the metaplectic method; retain critical-line proportions as separate results. The old phrase that the remaining strip “narrows with height” was already misleading for classical regions approaching `Re s=1`. |
| `thm:symbol-edge-quotient`, `notes/h-theta/astra-proofs.md:250`; corresponding review | Hermite–Biehler for every positive translate of the central entire function ⇔ RH | **Partially, only a fixed translation range.** O7 and FE put critical coordinates in `abs(Im z)≤3/8`; translates with `h>3/8` have the usual Hermite–Biehler property. “Every h>0” remains RH. No simplicity conclusion. |
| `thm:model-space-jets`, `thm:twisted-theta-edges`, `thm:level-model-decomposition`; `04v:150`; `deninger-cusp/astra-proofs.md:515` | Common damping `y^{−1/4}` iff represented zeros are critical | **Partially: a uniform range of individual decay rates.** With `w_ρ=γ/2+i(1−β)/2`, O7+FE gives `1/16≤Im w_ρ≤7/16`. It does not give the common value `1/4`, or an operator-norm decay bound for a nonnormal completion. |
| `prop:level-positivity-criterion`, database line 603; `04v:157–168`; `deninger-cusp/astra-proofs.md` D5 and brief | Positive centred spectral metric ⇔ GRH plus no Jordan chains | **Not at all for the asserted positivity.** `1/8≤β≤7/8` permits off-line quartets and multiple zeros. Review status and domain problems are untouched. |
| `prop:kernels-not-riesz`, `thm:ks-not-deninger-h1`, `thm:rescaled-semigroup-unbounded`; `deninger-bond/astra-proofs.md:281,397`; historical close-gap proposals | Some branches discuss RH; zero-count growth supplies close pairs and obstructs bounded equivalent metrics | **Not at all; the registered obstructions are already unconditional in their stated forms.** A fixed strip does not make a non-Riesz eigenfamily Riesz or remove Jordan growth. `T log T` counting is already unconditional, not a conjectural zero-density estimate discharged here. |
| `notes/adelic-gkp/adelic-gkp.md` §14.5, line 441 | `ζ_{Q(√2)}=ζ L(χ₈)`; RH requires both factors critical | **Partially: its finite-order factors now have the O7 strip.** Full RH/Weil positivity remains open. This is an abelian Dirichlet factorisation covered even without CT. |
| Same page, line 449; `gauge-groups.md:21` | Positivity for a full Grössencharacter/angular-frequency family | **Not at all.** Finite-order characters have trivial connected archimedean type; the proposed nonzero angular modes are outside the supplied quasi-RH theorems. |
| `notes/adelic-gkp/cm-lift.md` §§2.5, 3.3; citation ledger item 19; arithmetic/zeta reviews | Global GRH/Weil positivity for 49a1 and 441d1 | **Not at all.** Their Hecke characters over `Q(√−7)` have infinity type `(1,0)`, not finite order. CT does not change that limitation. Local Hasse bounds, shared vacua, FE and numerical comparisons were already independent of global GRH. |
| `notes/zeta-spectral-triples/ellcurve/plan.md:136`, Q4; `astra-review.md:336–337,574` | GRH for `L(E,s)` gives positivity of the entire test form; strict positivity also needs nonvanishing on spectral support | **Not at all.** General elliptic L-functions are outside the scope, and a fixed strip would not imply Weil positivity even if available. Finite certified positive matrices remain finite certificates. |
| `notes/adeles/software-and-algorithmic-scope.md:72,99` | GRH-conditional fast class-group/unit certification | **Not as stated.** O7 covers neither general number fields nor the required algorithmic quantitative thresholds. CT supplies a fixed strip for finite-order Hecke functions, but this does not automatically preserve GRH's polylogarithmic factor-base bounds or Buchmann's stated complexity/certification. A revised algorithmic theorem needs its own proof. |
| Historical Artin survey: `digests/G1-founding-worklogs-shards-a.md:262`, `lanes/L01-founding-handoff.md:180` | Historical sentence that Artin's primitive-root conjecture is known under GRH | **Not from O7.** Hooley's use involves a varying family of Kummer-extension Dedekind zetas and quantitative summation. A fixed strip does not automatically replace it. CT metadata refers to a separate Artin manuscript; that separate claim is outside this digest's audited proof inputs. Flag the historical survey for a separate source review. |
| `notes/metric-tomography/finite-prime-language.md:182`, §5 | A hypothetical truth of GRH trivialises a family decision problem | **Not at all.** Excluding zeros only in a fixed half-plane does not decide the full critical-line predicate. The computability discussion is not a quasi-RH corollary. |
| `notes/weil-bond-analytic/analytic.md` L7 / Theorem 8, §7 | Function-field edge criterion under the cited cokernel description, simple spectrum (multiplicities sketched) | **Not applicable.** This is a function-field theorem/criterion; Weil already supplies its arithmetic RH input. Its “zero-free” adjective means zero-independent construction of the projector. |
| `obs:three-metrics-dictionary`; `prop:weil-form-not-metric`; `connes-weighted-metric/astra-proofs.md` W5; `deninger-bond` | An intrinsic positive metric/domain construction without spectral zero data is missing | **Not at all.** “Zero-free” here is methodological. A zero-free strip supplies no metric, cup product or operator domain. |

For completeness, the remaining broad database hits are not undisclosed analytic assumptions: `asm:gamma-standard`, `prop:siegel-constant-term`, `num:h-theta`, `prop:burnol-even-sector-dictionary`, `obs:two-ends-fold`, and the Siegel-space clause of `thm:deninger-invariant-polarisation` are unrelated uses; `prop:bc-symplectic-odd-counterexample`, `num:bc-symmetry-generators`, `obs:zeta-condition-ledger` use conditional *Choi positivity*; `prop:phase-identity` uses conditional convergence with classical PNT; `thm:no-ungraded-trace`, `prop:absorbing-vacuum-channel`, `obs:complementary-halves`, `thm:as-symplectic-map`, `thm:selberg-two-term-ring-zeta`, `thm:cusp-renewal-discrete`, `cit:bombieri-negative-eigenvalues`, `thm:h-theta-1-refuted`, `thm:sonine-one-exit-norm-classification` have their own stated hypotheses or unconditional conclusions. None is promoted by this scan. The outgoing incomplete-theta zero-free result (`h-theta` T3(c)) is about a different function and was already proved. The RTP Dirichlet/elliptic numerics explicitly do not assume GRH; prefix certificates are finite computations, not full half-plane claims.

**PROVED (source-labelled consequences, O11 p. 2; not included in O7's reported formalisation scope).**

| Consequence listed by O11 | What a fixed strip supplies | Contact with this notebook |
|---|---|---|
| Vinogradov's least quadratic nonresidue conjecture | Via the cited Rodosskiĭ/short-Euler-product method, `n(p)≪(log p)^A` for an absolute fixed `A`, hence `≪_εp^ε`; O7 Cor. 1.2 gives a nonoptimised exponent `A=32`. | Helps deterministic finite-field arithmetic; it does not prove a particular graph flux Ramanujan. |
| Deterministic square roots mod an odd prime | Deterministically search for a nonresidue, then Tonelli–Shanks; polynomial in `log p`. | Potential implementation benefit for finite-field/CM computations, not a change to their exact results. |
| Miller's test | O11 reports deterministic polynomial-time Miller under the fixed strip. AKS was already unconditional. | No corresponding registered algorithmic claim found. |
| Imaginary quadratic class numbers | O11 reports an effective absolute `h(D)≫sqrt(abs(D))/log log(abs(D))` for negative fundamental `D`, using Littlewood and the class-number formula. | Relevant to possible CM lattice classes and discriminants in families; does not change the already known class number of `Q(√−7)`, nor select a lattice or global vacuum. |
| Euler's idoneal numbers | O11 combines absence of near-one exceptional zeros with the cited class-group computations and reduction to fundamental discriminants to confirm the 65-number list. | Relates to class-group exponent two, not to RH for 49a1/441d1 or to positivity on a `Z[ζ_N]` flux lattice. |

A precise near-one implication is: O7 excludes `β>7/8` for every real Dirichlet zero. It excludes a uniform logarithmic exceptional region, for example with `c=(log 3)/8` for primitive conductor `q≥3`, since `1−c/log q≥7/8`. It **does not exclude all real zeros in `(0,1)`**. Thus “no Siegel zeros” must refer to a specified near-one region, not to every real zero. For the cyclotomic fields underlying `Z_N` flux coefficients, the Dedekind zeta factors into finite-order Dirichlet L-functions and inherits the O7 strip. This is a theorem about those number fields' zeta functions; the integral flux lattice's Weil form remains a separate spectral question.

## D4. Four sharp proposals and the handoff to Q2

Three are OPEN conjectures; the fourth is a proposed statement already settled by finite Fourier support. They are not registered. Q2's brief was read: its function-field family calculations and graph monoid enumeration are its work. The tests below specify additional diagnostics or reuse its arrays; this lane does not duplicate those censuses.

### Q1-THETA: a charged cubic state, not a displaced stabiliser comb

**OPEN (repaired D-Θ); the literal stabiliser version is REFUTED in D2.4.** Over `F_q(t)`, `q≡1 mod 6`, conjecture that the completed cubic-Gauss coefficient family has a state construction compatible under CRT and changes of cutoff, using additive Fourier gates, inversion on units, cubic character multiplication and explicit nonunit projectors. Require the following falsifiable properties: coefficients at `nb³` equal the normalized cubic Gauss coefficient at squarefree `n` times the prescribed cube weight; reflection uses a fixed finite set of cusp/charge sectors independent of the varying squarefree row; within each sector the row dependence after reflection is quadratic. The operators may contain non-Clifford charges and projectors. No positive-count interpretation is stipulated.

**Finite test `Q2-THETA-SECTORS`.** Reuse Q2b's finite-ring arithmetic at `q=7,13`; for moduli of degree one and squarefree degree two compare the full finite Fourier/inversion kernel with `j↦−j−2 mod 6` for every `j=0,…,5`, including the Ramanujan-sum branch `j=4`, the nonunit-mask branch `j=0`, and coprime CRT products in both orders. A phase depending on the moving row outside the declared fixed sector, or a missing nonunit value, refutes the proposed realization. Local agreement only tests necessary conditions; the globally compatible completed-state construction remains the conjecture.

### Q1-EVAL: geometry should remove target concentration in a small-conductor function-field regime

**OPEN (repaired D-G as a quantitative statement).** Fix `q≡1 mod 6` and `ϑ>0`. Let primitive nonprincipal `ν_d` have conductor degree `m_d=o(d)`. Form the degree-`d` Möbius sums of Q2a and average over all nonzero polynomial rows of degree at most `h=⌈(1+ϑ)d⌉`, with normalization by their actual count. Conjecture

\[
 |A_1(d;\nu_d)|^2\le q^{o(d)}\,
 \mathbb E_{\deg u\le h}|A_u(d;\nu_d)|^2. \tag{Q1-EVAL}
\]

Equivalently, for every fixed `ε>0` the factor may be `q^{εd}` eventually along each such sequence. This is an assertion about evaluation on the arithmetic family, not rank alone. A sufficient, separately testable statement is the lower energy bound `E|A_u|²≥q^{d−o(d)}`: **using Weil's function-field RH as a labelled theorem**, the reciprocal of a degree-`O(m_d)` L-polynomial has coefficients bounded by `q^{d/2} binom(d+O(m_d),O(m_d))=q^{d/2+o(d)}`. Even-character trivial factors have root of inverse modulus one and obey the same upper bound. Thus the conjecture tests whether the short family retains its expected energy, once geometric pointwise control is known; it does not prove Weil from the family estimate.

**Finite test `Q2-EVAL-RATIO`.** Add the ratio `|A_1|²/E|A_u|²` to Q2b's existing tables at `q=7,13`; vary nontrivial primitive conductors and compare `h≈(1+ϑ)d` with the complete-residue regime `h≥2d−1`. Record zero numerator/zero denominator cases separately. Use polynomial coefficients only, with no L-zero input. A growing exponential ratio in a genuine small-conductor sequence would refute the claim; degrees at most five are exploratory, not an asymptotic certificate. Also check the exact deletion repair `A_1(d)=A_{p⁶}(d)−ν(p)A_{p⁶}(d−deg p)` rather than only its triangle-inequality error.

### Q1-TRACE: the graph Haar trace mean square is exponentially larger than RH scale

**OPEN (sharp asymptotic conjecture, with a specific mechanism).** For a fixed connected non-bipartite simple `(q+1)`-regular graph, `q>1`, cycle rank `g`, conjecture that normalized Haar measure on its full flux torus satisfies

\[
 \int_{H^1(Y,\mathbb R/\mathbb Z)}|\operatorname{Tr}B_s^k|^2\,ds
       \sim C_Y q^{2k}k^{-g/2},\qquad C_Y>0.
\]

The proposed mechanism is a nondegenerate quadratic maximum of the leading nonbacktracking eigenvalue near the trivial flux (and the parity flux). Laplace's method would give the power `k^{−g/2}`. A proof must identify all maximal points and handle possible periodicity; the stated non-bipartite hypothesis avoids the immediate zero trace on odd lengths. This is consistent with the matching-polynomial theorem and contradicts any attempt to read that theorem as an RH-scale trace mean square `O(q^k)`.

**Finite test `Q2-TRACE-LAPLACE`.** On `K₄` and Petersen, use twisted adjacency/Bass recurrences, not prime-cycle enumeration, to compute Haar quadratures for increasing `k` and the Hessian at zero flux. Test convergence of `q^{−2k}k^{g/2}` times the mean square. Refine the torsion/quadrature mesh relative to `√k`; a fixed finite flux group has an atom at zero and tests a different limit. The cube is a periodic control: use even lengths and state the changed constant. All inputs are graph matrices.

### Q1-SAMPLE: the graph coefficient L² average stabilises already at N=3

**SHARPENED → PROVED (elementary finite Fourier argument).** For a simple graph and any fixed finite linear combination `F(s)` of coefficients of `det(I−zB_s)`,

\[
 \frac1{N^g}\sum_{s\in H^1(Y,\mathbb Z/N)}|F(s)|^2
       =\int_{H^1(Y,\mathbb R/\mathbb Z)}|F(s)|^2ds\quad(N\ge3).
\]

Indeed Bass and the elementary-subgraph expansion put each cotree exponent of `F` in `{−1,0,1}`. Those of `|F|²` lie in `{−2,−1,0,1,2}`. For `N≥3`, only exponent zero is divisible by `N`, so torsion and Haar averages agree. At `N=2`, exponents `±2` can survive; `F(z)=z+z^{−1}` already has Haar energy `2` and two-torsion energy `4`. This is finite quadrature, not a large sieve and not RH for any chosen flux.

**Finite test `Q2-SAMPLE-L2`.** Reuse Q2's coefficient arrays for `K₄` at `N=2,3,6`, and compare degree-by-degree against the squared Laurent coefficient mass. No second cycle enumeration is needed. This supplies an exact control for Q2's numerical averaging, and a clean separation between finite Fourier sampling and the number-field family's growing-conductor analysis.

## Correction ledger (completed)

1. **Amplifier balance:** `H=D` gives unequal square exponents `11/6` and `5/3`; the formal balance is `H=D^{6/7}`, outside the proved range. `7/8` comes from a different compensated probe.
2. **Conjugations lost by extraction:** (Q1.2) needs `\bar α(n)` and `G=\overline{χ_n(4)}γ₃(n)`; (Q1.3) uses the coefficient of `\bar θ` and `\overline{χ_n(λ)^2}`. The source PDF confirms these; the unbarred brief identity fails the norm-seven finite check.
3. **Theorem labels:** Kintali has Theorem 1; Liu's Theorem 1.1 restates `7/8`, while his improvement is the Main theorem/Theorem 27.1; DR's Theorem 1.1 is a GRH-conditional prime asymptotic, not a quasi-RH theorem.
4. **Source availability:** CT's supplied `.txt` is a Hexagon landing-page extract, not `pdftotext` of its proof. The author repository confirms theorem/corollary scope; unseen proof details remain unaudited.
5. **Formalisation evidence:** the supplied Lean comparator ends in `sorry`. Reported full formalisation is a separate provenance claim. O11's weaker theorem follows from the reported O7 theorem but its proof is not thereby formalised. O7's applications are outside the reported scope.
6. **Conditional inputs:** O7 is presented as unconditional. Some estimates have explicit internal zero-supremum hypotheses; K avoids their machinery. The DR GRH-conditional prime theorem is not used in the quasi-RH proofs.
7. **Section 7:** in O11 it is the transfer of **dual mean squares**, not transfer to Dirichlet L-functions; the latter is in §3.
8. **Theta automorphy:** scalar automorphy is on `Γ₂` with cubic multiplier; full `SL₂(O)` acts through cusp components. A cubic cover is not the ordinary Fourier metaplectic sign ambiguity.
9. **Sieve:** the higher-order bound has `M+L+(ML)^{2/3}`. The quadratic `M+L` bound is generally sharp but not an automatic consequence of positivity or necessarily sharp on this special coefficient sequence.
10. **Family average:** matching-polynomial real-rootedness and Möbius L² cancellation are different assertions. Norm-bounded Kummer representatives are not a fixed finite flux group, and ideals are products of prime cycles, not single cycles.
11. **Graph Littlewood obstruction (also in Q2's brief):** reciprocal Ihara zeta is a polynomial. Eventual zero Möbius coefficients cannot constrain its zeros; graph RH concerns zeta poles. Off-diagonal signed terms cannot be discarded as a positive lower bound either. The zero-free function-field region `|u|<q^{−θ}` is a disk; zero moduli are bounded **below**, not above.
12. **D-Θ/D-G:** a cubic charged state is not a displaced stabiliser comb; finite rank alone is not positivity or bounded evaluation. The family is scale-growing. The `7/8→1/2` gap has no established equality with a rank gap.
13. **Liu's scope:** his optimisation permits a small improvement and proves a barrier for unchanged comparison bounds; stronger analytic inputs are not ruled out.
14. **CM scope:** finite-order Hecke conclusions, including CT's, do not cover the nonzero infinity-type characters of 49a1/441d1. A twist by a covered Dirichlet character does not change this.
15. **“No Siegel zeros”:** excludes a specified near-one region, not every real zero in the critical interval.
16. **Window rank precision:** finitely many spectral atoms give rank equal to their distinct support size, at most `2g`; repeated eigenvalues do not increase that rank. The zeta rank discussion in lane R is model-labelled and not made unconditional by quasi-RH.

## Numerical checks for the blind lane

Run from this lane directory:

```bash
python3 checks/exponents.py
python3 checks/structural_checks.py
python3 checks/record_scan.py
```

The first script uses exact rational/symbolic arithmetic. Liu's root is isolated by sign changes and a strictly negative derivative on the stated interval, then 280 exact rational bisections; the induced boundary interval has width below `10^(−85)`. Rounded displays are not used to decide inequalities. The second uses exact integer/polynomial arithmetic and an explicitly **NUMERICAL**, non-interval, 80-decimal Gauss-sum check. No L-function zero is an input.

Six values/certificates to recompute:

| Check | Result |
|---|---|
| O11 square exponents at `H=D` | `11/6`, `5/3`; half the dominant exponent is **`11/12`**. |
| Formal, unavailable balance | `H=D^{6/7}` and `A₁≪D^{6/7+ε}` from that inequality alone. |
| O7 low/signal match | `17/96+1/96=3/16=7/8−11/16`. |
| O7 high certificate | Exact symbolic residual of (20.9) is `0`; `49/440640≈0.000111201888162672>1/10000`. |
| Liu cubic | `ξ≈0.3885833542660346667974279910648928174`; **`Bnew≈0.8749570194200989461286038505614529823`**, with exact interval width about `7.24×10^(−91)`. |
| Missing bars, finite norm-seven check | Correct identity residual `<10^(−75)` at 80 digits; unbarred brief residual `≈1.3093073414159542876`. |

Additional exact structural controls printed by the second script: a rank-two integral `5`-similitude with eigenvalue `(5+√5)/2>√5`; all-negative `K₄` has a degree-12 reciprocal Ihara polynomial vanishing at `−1/2` while its degree-13 coefficient is zero; the cubic-charge support over `F₇` is six, incompatible with a prime-qudit stabiliser support of one or seven. These are counterexamples/finite identities, not zero calculations for zeta.

## What this changes in the notebook

**READING / proposed edits only.** Quasi-RH adds a global analytic strip to the ladder by using an auxiliary arithmetic family and cubic automorphy. It does not supply the positive invariant form, integral spectral lattice, common critical decay rate, or simplicity sought by the notebook. No existing claim is promoted by this lane.

| Page / section needing a paragraph | Proposed content |
|---|---|
| `data-ladder.md` §§2, 4, 4b | Add the metaplectic family route to a fixed strip; distinguish coefficient L² positivity from Weil positivity. Treat finite rank as a proposed cohomological structure, not a necessary condition for every proof of a strip. |
| `zn-flux.md` §§4–5; `graph-super.md` §6 | Distinguish the matching-polynomial average, coefficient L² average, and trace L² average. Add the reciprocal-Ihara-polynomial obstruction and the `N≥3` exact L² sampling identity. |
| `functional-equation-gate.md` §3; `gate-phases.md` §3 | Row Poisson is an exact Fourier-gate instance. Cubic metaplectic reflection requires an additional charged state/cocycle and cusp sectors; it is not a displaced ordinary comb. |
| `family-vacuum.md` §3 / `cm-lift.md` §§2.5, 4 | An auxiliary twisting family is not a commuting family of similitude operators. The finite-order theorem does not apply to the elliptic infinity-type characters; the local/global distinction survives. |
| `window-similitude.md` §3 | No quasi-RH positivity upgrade. Rank counts distinct spectral atoms; finite rank alone does not force RH. |
| `notes/what-rh-has-become.md` §5; `report/sections/03_what_rh_has_become.tex` hierarchy | Add the fixed-strip power saving between classical PNT and square-root error. |
| `notes/metric-tomography/metric-as-state.md` §4.4 | Update the survey of unconditional analytic information; add the metaplectic route and its formalisation/provenance limits. |
| `04v_deninger_cusp.tex` / `notes/deninger-cusp/astra-proofs.md` D5 | Add the strip-derived range `[1/16,7/16]` for individual arithmetic mode depths. Do not infer full semigroup norm decay or a GRH metric. |
| `notes/adeles/software-and-algorithmic-scope.md` | Separate the fixed-strip arithmetic consequences from GRH-dependent complexity guarantees; review those algorithmic thresholds separately. |

**Candidate citation rows, not inserted.** In this repository `cit:` is an **ID prefix**; the existing schema's kind is `citedfact`, status `cited`. Use those fields for the following proposals, with `author=codex:gpt-6-astra`, `review=-`, and an as-yet-unassigned shard. The `proof` field should point to the corresponding source/provenance entry, with this digest as the scope audit; no invented provenance key is supplied.

| Candidate ID | Statement / dependency | Mandatory status note |
|---|---|---|
| `cit:openai-qrh-seven-eighths` | O7 Theorem 1.1: all finite-order Hecke L-functions over `Q(√−3)` and all Dirichlet L-functions are zero-free in `Re s>7/8`, principal poles allowed. | Preprint; formalisation of these conclusions reported by publisher scope note; local supplied file is a comparator with `sorry`; not rebuilt here; applications excluded. |
| `cit:openai-qrh-eleven-twelfths` | O11 Theorem 1.1, same families, `Re s>11/12`; independent mean-square/amplifier proof. | Preprint; this proof not reported formalised; human proof audit not performed by this lane. |
| `cit:kintali-qrh-47-48` | K Theorem 1: same families, primitive or imprimitive, `Re s>47/48`, principal pole allowed. | Preprint; no Lean claim in supplied source; uses unconditional theta, quadratic sieve and general Hecke density. |
| `cit:liu-qrh-cubic-bound` | L Main theorem / Theorem 27.1: boundary `Bnew=(18ξ+7)/(18ξ+9)` with the stated cubic; depends on O7's intermediate estimates and its starting bound. | Lean formalisation of the zero-free conclusions reported by author, not rebuilt; optimum only within the specified comparison system (Theorem 34.4). Exact scalar checks reproduced here. |
| `cit:cureton-thorner-qrh-31-32` | CT Theorem 1.1 / Corollary 1.2: all number-field Dedekind zetas and finite-order Hecke functions, `Re s>31/32`, wherever holomorphic. | Hexagon preprint; AxiomProver/Lean reported by authors; supplied text is metadata, proof not inspected; not rebuilt. Does not cover arbitrary infinity type. |
| `cit:dunn-radziwill-cubic-theta` | DR §5: explicit cubic theta cusp coefficients and level-aspect transformation used by the quasi-RH argument. | Published input; unconditional §5 formulas, not DR's GRH-conditional prime theorem. No Lean assertion made here. |
| `cit:dunn-radziwill-prime-bias-conditional` | DR Theorem 1.1 cubic prime-sum asymptotic under Hecke GRH. | **PROVED-conditional, H-DR-GRH**; not discharged by quasi-RH and not a dependency of the quasi-RH proof. Include only if the record needs to distinguish the two DR results. |

The next concrete step is **Q2-THETA-SECTORS**, paired with **Q2-EVAL-RATIO**: check the six local character branches and CRT phases exactly, then measure target concentration using Q2's existing function-field coefficient data. On the graph side, keep **Q2-SAMPLE-L2** as the exact averaging control and **Q2-TRACE-LAPLACE** as the spectrum-sensitive replacement for the invalid Möbius-coefficient/Ramanujan equivalence. A later independent REFUTE review should check the proposed new graph sampling statement and the scope/phase corrections before registration. The unavailable CT proof and all full Lean builds remain explicitly outside this lane's verification claim.
