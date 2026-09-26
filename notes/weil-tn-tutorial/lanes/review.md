# REFUTE review of "Weil Positivity, Contracted" (index.html), 2026-09-26

Reviewer: claude:opus-5.5 (adversarial). Scope: every mathematical statement in the prose of steps 0 to 7, the
`.cap` captions, the `.dict` rows, the `.claim` boxes, the TERMS modal texts, and the footer. Checked against
the shards named in CONTRACT.md, `db/claims.tsv`, notes X1/X2, and the lane reports. The parent artifact
*The Weil Functional* was read for its conventions: Toeplitz form `sum g_k conj(g_m) T_{k-m}`,
`ghat(gamma) = int g e^{i gamma x} dx`, `G_ij = W(g_i * g~_j)`, and `W = pole - primes - [g(0) log pi + int ...]`.
Python (numpy) scratch scripts were run in the session scratchpad; the constructions are given inline so that
they can be reproduced.

Replacements quote the current text verbatim, in the file's own syntax: single backslashes in the HTML body,
doubled backslashes inside the TERMS template strings.

## (a) Statements checked

### Step 0

1. **VALID.** `\|\psi_L\|^2 = \sum_w|\operatorname{Tr}(A_{w_L}\cdots A_{w_1})|^2 = \operatorname{Tr}E^L`, with
   `E = \sum_s A_s\otimes\overline{A_s}`. This is the 03g first display and def:transfer-matrix/def:ring-norm
   (`E = \sum\operatorname{Ad}(A_i)`, the same map vectorised). Python on (1 2)(3 4 5) with point letters at L = 4:
   the word sum, `Tr E^4` and `Tr P^4` all equal 2.
2. **VALID.** `\exp\sum_L t_L u^L/L = 1/\det(1-uE)`, called "the one identity" of the parent page (parent step 0).
3. **VALID.** The step 0 dictionary rows.
4. **MINOR.** Hero lede: "The Weil form of a zeta function is an overlap of two open pieces of a tensor network."
   The form is an overlap only when a unitarising metric exists (prop:ccm-tn-operator-gram). For the prism
   C16×K2 the form is negative (graphs lane, λ_min(K = 16) = −29.17), so it is not an overlap of anything, and
   for ζ the existence is exactly the open question of step 7.
   Replace `The Weil form of a zeta function is an overlap of two open pieces of a tensor network.` →
   `The Weil form of a zeta function is the Toeplitz matrix of the ring norms of a tensor network, and it is an overlap of two open pieces of that network exactly when a metric exists that makes the transfer operator unitary.`

### Step 1

5. **MINOR.** `the Toeplitz form \(\sum_{j,k}c_j\overline{c_k}\,t_{k-j}\)`. The parent page uses
   `\sum_{k,m}g_k\overline{g_m}T_{k-m}`, and def:weil-form uses `\sum c_\ell\bar c_k\nu_{\ell-k}`, as does this page's
   own footer. With `t_{k-j}` the expression equals W at the conjugate vector, not W(c). It agrees with the rest of
   step 1 only as `c^*Tc = \sum\overline{c_j}c_k t_{k-j}`.
   Replace `\(\sum_{j,k}c_j\overline{c_k}\,t_{k-j}\)` → `\(\sum_{j,k}c_j\overline{c_k}\,t_{j-k}\)`.
6. **VALID.** For unitary E: `\operatorname{Tr}((E^j)^*E^k) = t_{k-j} = \langle E^j,E^k\rangle_{\mathrm{HS}}`, and a
   Gram matrix is PSD. See 03g ⟨1⟩1. The HS product is conjugate-linear in the first slot (02i).
7. **MINOR.** "In every interesting example \(E\) is not unitary in the metric the bond came with."
   This contradicts step 6 ("Here the metric of step 1 is the native one", prop:as-unitarity) and step 2 (P unitary, G = 1).
   Replace `In every interesting example \(E\) is not unitary in the metric the bond came with.` →
   `In most examples below (shifts, graphs, general Kraus families) \(E\) is not unitary in the metric the bond came with.`
8. **MINOR.** Claim box prop:ccm-tn-operator-gram, forward part. The formula matches the claims.tsv statement
   exactly: `T_jk = Tr((E^j)^♯E^k)`, `c^*Tc = ‖p_c(E)‖²_{HS,G}`, `A^♯ = G^{-1}A^*G` (def:ccm-tn-feature), and
   `T_jk = t_{k-j}`, `t_{-k} = conj t_k` (def:ccm-tn-moments). However, E in the label is the **rescaled retained
   operator** (def:ccm-tn-spaces), whereas on this page E was introduced in step 0 as the MPS transfer matrix. That
   matrix is never G-unitary when it has trivial modes; the permutation's E has n²−n zero eigenvalues. The TN lane
   flagged this, and movieGram's first caption fixes it, but the prose does not.
   Replace `The Toeplitz form is the Gram matrix of the strips in the \(G\)-twisted Hilbert–Schmidt product, hence positive semidefinite.` →
   `Here \(E\) is the rescaled retained operator (trivial modes removed, divided by \(r\)), so that \(t_k = \operatorname{Tr}E^k = \nu_k\). The Toeplitz form is the Gram matrix of the strips in the \(G\)-twisted Hilbert–Schmidt product, hence positive semidefinite.`
9. **MINOR.** Same box, converse: "Conversely, Gram equality for all windows forces \(E\) to be unitary in some metric."
   The label says something narrower: *native* Gram equality for *all* nonnegative powers forces *native*
   unitarity, and equality on one fixed finite window does not (03g ⟨1⟩4 gives a 2×2 counterexample). "Unitary in
   some metric" reads as "positivity gives a metric", which is false (item 13).
   Replace `Conversely, Gram equality for all windows forces \(E\) to be unitary in some metric.` →
   `Conversely, if the native Hilbert–Schmidt Gram matrix of the strips equals the Toeplitz matrix for all windows, \(E\) is unitary in the native metric; equality on one fixed window does not suffice.`
10. **VALID.** `\tilde E = G^{1/2}EG^{-1/2}`, and `E^*GE = G` iff `\tilde E^*\tilde E = 1`. Algebra:
    `\tilde E^*\tilde E = G^{-1/2}E^*GEG^{-1/2}`. This is def:ccm-tn-feature.
11. **MINOR.** Claim box prop:hp-inner-product-discrete.
    - The label's hypothesis "S_triv a union of full eigenvalue classes; V′ = sum of the generalised eigenspaces of
      the retained classes" is missing. Without it the "retained space" is not defined (def:ccm-tn-spaces).
    - "\(-i\log E\) is self-adjoint" is not in the label. It is a true consequence, once a branch of log is chosen
      on the G-orthogonal spectral decomposition, but it sits inside a box tagged with the label.
    Replace `(on the retained space, with critical radius \(1\)) exists iff \(E\) is diagonalisable with every eigenvalue of modulus one. It is a Hilbert–Pólya inner product: in it \(E\) is unitary and \(-i\log E\) is self-adjoint.` →
    `(on the retained space, the sum of the generalised eigenspaces of the retained eigenvalues, the trivial set being a union of full eigenvalue classes; critical radius \(1\)) exists iff \(E\) is diagonalisable there with every eigenvalue of modulus one. It is a Hilbert–Pólya inner product: in it \(E\) is unitary, so (for any choice of branch) \(-i\log E\) is self-adjoint.`
12. **MINOR.** "The finite Weil theorem of the parent page links them, and adds the one thing positivity cannot see".
    Positivity is linked to "on the circle" only under J-invariance (thm:weil-duality-pairing). Without it,
    positivity is just the disc bound, as in the golden mean. The Jordan-block remark is a caveat, not something the
    theorem "adds".
    Replace `The finite Weil theorem of the parent page links them, and adds the one thing positivity cannot see:` →
    `When the retained set is reflection-invariant the finite Weil theorem links them (positivity ⇔ circle), and one thing remains that positivity cannot see:`
13. **VALID.** "a Jordan block on the circle has positive counts but no metric". This is prop:weil-blind-jordan
    (proved). Python: for `X = [[1,1],[0,1]]`, ν_ℓ = 2 for all ℓ and λ_min(T_10) = −5e−16 (PSD of rank 1).
14. **VALID.** Demo A caption: `G = (V^{-1})^*V^{-1}` with `E = VΛV^{-1}` and Λ unitary gives
    `E^*GE = (V^{-1})^*Λ^*ΛV^{-1} = G`. Core lane: max|metric Gram − T| = 1.4e−15 against naive 7.99.
15. **VALID.** Claim box thm:weil-positivity-finite matches claims.tsv (status proved), including zero modes.
16. **VALID.** Claim box thm:weil-duality-pairing matches claims.tsv (proved). J-invariance excludes 0 automatically.
17. **VALID.** "Positivity alone is the spectral-gap half of RH, Re ρ ≤ 1/2". See 08b lines 58–60 and 78–79.
18. **MINOR.** Step 1 dictionary, Weil form row. The Toeplitz matrix is the Gram matrix of the strips only when
    `E^*GE = G`.
    Replace `<td>the Gram matrix of the strips, \(T_{jk} = \operatorname{Tr}((E^j)^\sharp E^k) = t_{k-j}\)</td>` →
    `<td>the Toeplitz matrix \(T_{jk} = t_{k-j}\) of the counts; when \(E^*GE = G\), the Gram matrix of the strips, \(T_{jk} = \operatorname{Tr}((E^j)^\sharp E^k)\)</td>`
19. **VALID.** Step 1 dictionary: the metric row ("exists iff semisimple on the circle"), the positivity row, and
    the functional equation row.

### Step 2

20. **VALID.** `A_x = |\sigma x\rangle\langle x|`, `\sum A_x = P`, and `\operatorname{Tr}(A_{x_L}\cdots A_{x_1}) = 1`
    iff `x_{k+1} = \sigma x_k` cyclically (prop:permutation-rings); ring norm = #Fix(σ^L).
21. **VALID.** "\(E\) acts as \(P\) on the diagonal vectors and kills every off-diagonal one: spectrum of \(P\)
    with \(n^2-n\) zeros". Python checked `E|yz⟩ = δ_yz |σy σy⟩` on all basis vectors, so E is block diagonal
    [[P,0],[0,0]]. For (1 2)(3 4 5), E has nonzero spectrum {1, 1, −1, ω, ω̄} = spec P, and 20 zeros = n² − n.
22. **VALID.** Zeros trivial, r = 1, G = 1, Toeplitz of fixed-point counts = Gram matrix of P^0, …, P^{K−1}
    (on ℂ^n, the retained block).
23. **INVALID.** "The notebook's shard also grades a cycle odd and closes the ring with the parity operator inserted, \(t_k = \operatorname{Tr}(\Pi P^k)\). … the supertrace sequence is not positive definite. That is the sign convention of the curve …, seen at the level of letters".
    - Shard 03b says the opposite about this network. With point letters, which are sector-separating, the twisted
      ring norm is `‖Ψ_Π‖² = Tr[(Π⊗Π̄)E^n] = Tr P^n`, with no sign (lem:sector-separating-letters,
      prop:letters-word-formula: "point letters give ‖Ψ_Π‖² = Tr P^n"). A sign survives in a ring norm only for
      letters coarser than the grading (one letter: `|str P^n|²`).
    - `Tr(ΠP^k) = str P^k` is the single-layer bond supertrace of thm:permutation-induced-zeros (status
      *sketched*). It is not the ring norm of the doubled network.
    - "Not positive definite" is false in general. If an odd and an even cycle have the same length, `str P^k ≡ 0`.
      Python: (1 2 3)(4 5 6) with one cycle odd gives t = 0, 0, 0, … and λ_min = 0. For (1 2)(3 4 5) with either
      cycle odd, λ_min(T_8) = −8.64 or −7.64, so there it does fail.

    Replace the whole passage from `The notebook's shard also grades a cycle odd and closes the ring with the parity operator inserted, \(t_k = \operatorname{Tr}(\Pi P^k)\).` through `seen at the level of letters: a positive form for zeros counts them with the sign reversed.` →
    `The notebook's shard also grades a cycle odd and inserts the parity \(\Pi\) into the bond trace, \(t_k = \operatorname{str}P^k = \operatorname{Tr}(\Pi P^k)\). The odd cycle's eigenvalues then appear in the <em>numerator</em> of the graded zeta function: they are zeros, not poles, and unless an even cycle of the same length cancels them the supertrace sequence is not positive definite. This supertrace is not a ring norm of the point-letter network: with point letters the twisted ring norm \(\|\Psi_\Pi\|^2\) is still \(\operatorname{Tr}P^k\), because letters that separate the parity sectors kill the sign, and a sign survives in a ring norm only for letters coarser than the grading (one letter gives \(|\operatorname{str}P^k|^2\)). It is the sign convention of the curve on the parent page, \(T_k = q^{k/2}+q^{-k/2}-N_kq^{-k/2}\): a positive form for zeros counts them with the sign reversed.`
24. **MINOR.** Demo B caption: "Grade a cycle odd (click its label) to see the twisted closure produce an
    indefinite form." The demo's default permutation is (1 2 3)(4 5 6) (`demos-core.js`, `sig: [1,2,0,4,5,3]`).
    Grading one cycle odd there gives t ≡ 0 and λ_min = 0, which is not indefinite.
    Replace `Grade a cycle odd (click its label) to see the twisted closure produce an indefinite form.` →
    `Grade a cycle odd (click its label) to see the parity-twisted supertrace produce an indefinite form (use the preset \((1\,2)(3\,4\,5)\): with two cycles of equal length one odd cycle cancels the other and the form is zero).`
25. **MINOR.** Step 2 dictionary: "an odd cycle under the twisted closure enters with a minus sign: a zero". Same
    issue as item 23.
    Replace `an odd cycle under the twisted closure enters with a minus sign: a zero` →
    `an odd cycle enters the parity supertrace \(\operatorname{Tr}(\Pi P^k)\) with a minus sign: a zero`

### Step 3

26. **MINOR (cosmetic).** "\(E\) acts as \(M\) on the diagonal". With `A_{a→b} = |b⟩⟨a|` and `M_{ab} = 1` for an
    allowed a→b, the sum `Σ A` equals `M^T`, and E acts as `M^T` on the diagonal. Traces and spectra are the same.
    Replace `and \(E\) acts as \(M\) on the diagonal` → `and \(E\) acts as \(M^{\mathsf T}\) (same traces as \(M\)) on the diagonal`.
27. **MINOR.** "the Perron eigenvalue, which is the fixed point of the channel". An eigenvalue is not a fixed point.
    The Perron *eigenvector*, a positive diagonal vector of the doubled bond, is the fixed point of the normalised
    map `E/λ_max`. The same looseness appears in the step 3 dictionary and in TERMS `transfer` (item 88).
    - Replace `the Perron eigenvalue, which is the fixed point of the channel and carries` →
      `the Perron eigenvalue, whose eigenvector is the fixed point of the normalised channel \(E/\lambda_{\max}\), and which carries`.
    - Dictionary: replace `the channel's fixed point, the growth of the counts` →
      `the growth rate of the counts; its eigenvector is the fixed point of \(E/\lambda_{\max}\)`.
28. **MINOR.** `\nu_\ell = \lambda_{\max}^{-\ell/2}(t_\ell - \lambda_{\max}^\ell)` omits the zero eigenvalues of M.
    With the lab's convention 0⁰ = 1 (def:rescaled-trace-sequence) they contribute to ν₀. For I + C₄ the sentence
    "the retained set is invariant under μ ↦ 2/μ̄" is true only if 0 is trivial: thm:weil-duality-pairing needs
    0 ∉ retained, and J(0) is undefined. The demo and check_core.py do put the zeros in the trivial set
    (ν₀ = n − 1 − #zeros). The prose should say so.
    Replace `gives the retained sequence \(\nu_\ell = \lambda_{\max}^{-\ell/2}(t_\ell - \lambda_{\max}^\ell)\)` →
    `gives the retained sequence \(\nu_\ell = \lambda_{\max}^{-\ell/2}(t_\ell - \lambda_{\max}^\ell)\) (the zero eigenvalues of \(M\), which contribute only to \(t_0\), go in the trivial set too, so \(\nu_0\) drops by their number)`.
29. **VALID.** Golden mean: eigenvalues 1.6180 and −0.6180; |−1/φ| = 0.618 < √φ = 1.2720 (Python), so the form is
    positive (T1) and RH fails. Core lane: λ_min(K = 10) = 0.3531.
30. **VALID (given item 28).** For I + C₄, Python gives eigenvalues 2, 1 ± i, 0 and |1 ± i| = 1.4142 = √2 = √λ_max.
    J(1 ± i) = 2/(1 ∓ i) = 1 ± i, so the retained set is J-fixed and the form is positive.
31. **VALID.** "What the golden mean lacks is exactly the reflection symmetry": J(−1/φ) = φ/(−1/φ) = −φ² = −2.618,
    which is not in the retained set.
32. **MINOR (game rule).** Demo C caption: "the verdicts: positive? on the circle? reflection-invariant?". The last
    two verdicts are computed from eigenvalues (`eigvals(cm.fromReal(M))` in `demos-core.js`). The eigenvalue
    panel is marked comparison, but the verdicts are not.
    Replace `and the verdicts: positive? on the circle? reflection-invariant?` →
    `and the verdicts: positive? (from the counts) and, <span class="pill spec">comparison</span>, on the circle? reflection-invariant?`

### Step 4

33. **VALID.** A (q+1)-regular graph as the shift on directed edges with the non-backtracking rule; B is the
    Hashimoto matrix; `Tr B^L` counts closed non-backtracking walks; the Ihara zeta is `1/det(1−uB)`
    (def:hashimoto-operator, def:ihara-zeta).
34. **MINOR.** "that single extra structure produces the functional equation". Edge reversal alone does not do it:
    an irregular graph has reversal but no μ ↦ q/μ symmetry (its Bass factor is `det(1 − uA + u²(Deg − 1))`).
    Regularity is the second input.
    Replace `and that single extra structure produces the functional equation:` →
    `and that extra structure, together with regularity, produces the functional equation:`
35. **VALID.** Ihara–Bass `det(1−uB) = (1−u²)^{|E|−|V|} det(1 − uA + qu²)` (def:ihara-bass). The spectrum
    description is right: 2|E| = 2(|E|−|V|) + 2|V|.
36. **VALID.** The roots multiply to q; with real a this is J-invariance for r = √q.
37. **VALID (for connected graphs).** Trivial set {q, 1}, {−q, −1} if bipartite, and ±1 × (|E|−|V|). This is the
    trivial set of the graphs lane (its finding 1).
38. **VALID.** Weil positivity ⇔ every retained |μ| = √q ⇔ |a| ≤ 2√q (T1 + T2, def:ramanujan-graph).
39. **MINOR.** "Huang's criterion \(h_k = \nu_0 - \nu_k\ge0\) is the same statement in the form of the \(2\times2\) minors (the notebook's observation X1)."
    X1 is titled "Huang's criterion is the *boundedness* form". h_k ≥ 0 is X1(iii), Re ν_k ≤ ν₀. That is weaker than
    the 2×2 minor condition |ν_k| ≤ ν₀ (X1(iv)), and it is equivalent to positivity only through boundedness.
    Huang's own formula (cit:huang-graph-criterion) needs `N_k = Tr B^k − (|E|−|V|)(1+(−1)^k)`, and as written it is
    for non-bipartite graphs (graphs lane, finding 3).
    Replace `Huang's criterion \(h_k = \nu_0 - \nu_k\ge0\) is the same statement in the form of the \(2\times2\) minors (the notebook's observation X1).` →
    `Huang's criterion \(h_k = \nu_0 - \nu_k\ge0\) for all \(k\) is the same statement in a weaker, termwise form: it is one side of the \(2\times2\) minor bound \(|\nu_k|\le\nu_0\), and it is equivalent to positivity because both force the sequence to be bounded (the notebook's observation X1; Huang's closed formula uses \(N_k = \operatorname{Tr}B^k-(|E|-|V|)(1+(-1)^k)\) and is stated for non-bipartite graphs).`
40. **INVALID** (the last sentence of the metric paragraph). The first half is **VALID**: "a Hilbert–Pólya inner
    product on the retained space exists iff the graph is Ramanujan and \(B\) is semisimple there"
    (prop:hp-inner-product-discrete). The last sentence, "The Ramanujan property of the graph is the existence of
    that metric.", is false.
    - Counterexample (Python): G = C₃ × C₆ × K₂, 5-regular, q = 4, |V| = 36, |E| = 90, non-bipartite. Its
      adjacency spectrum has max nontrivial |a| = 4 = 2√q, so G is Ramanujan. The value a = +4 (multiplicity 2)
      is 2 + 1 + 1 from the three factors, and a = −4 is −1 − 2 − 1.
    - B on 180 darts has dim ker(B − 2) = 2 but dim ker(B − 2)² = 4, and likewise at −2. These are two 2×2 Jordan
      blocks at μ = √q and two at −√q. They lie in the retained space, so by prop:hp-inner-product-discrete no
      Hilbert–Pólya inner product exists.
    - The Weil form is nevertheless positive: from Tr B^ℓ with the trivial set removed, ν₀ = 70 and
      λ_min(T_16) = +0.3135.
    - In general, a = ±2√q gives a double root of μ² − aμ + q, and B restricted there is a companion block.
    Replace `The Ramanujan property of the graph is the existence of that metric.` →
    `The Ramanujan property is Weil positivity; the metric needs in addition that no adjacency eigenvalue equals \(\pm2\sqrt q\) exactly, since there \(B\) has a \(2\times2\) Jordan block at \(\pm\sqrt q\), which positivity cannot see.`
41. **INVALID.** Step 4 dictionary: `⇔ Ramanujan ⇔ \(h_k\ge0\) ⇔ a Hilbert–Pólya metric on the retained edge space`.
    Same counterexample as item 40.
    Replace `<td>⇔ Ramanujan ⇔ \(h_k\ge0\) ⇔ a Hilbert–Pólya metric on the retained edge space</td>` →
    `<td>⇔ Ramanujan ⇔ \(h_k\ge0\); a Hilbert–Pólya metric on the retained edge space iff, in addition, \(B\) is semisimple there (no \(a = \pm2\sqrt q\))</td>`
42. **VALID.** Demo E caption: "The prism \(C_{16}\times K_2\) is cubic and not Ramanujan." a = 1 + 2cos(π/8) =
    2.8478 > 2√2 = 2.8284. The page nowhere claims the form goes negative at K = 12. The graphs lane has it first
    negative at K = 14.

### Step 5

43. **MINOR.** In `\operatorname{Tr}T^\ell = \sum_{w\in[D]^\ell,\ w_{k+1}\ne\bar w_k}\dots`, the constraint must be
    cyclic (k ∈ ℤ/ℓ, including w₁ ≠ w̄_ℓ), as in Corollary 2 of notes/quantum-ihara-general.md. The TERMS `edgelift`
    text says "cyclically".
    Replace `w_{k+1}\ne\bar w_k}}` → `w_{k+1}\ne\bar w_k\ (k\in\mathbb Z/\ell)}}`.
44. **VALID.** "nonnegative for every family whatever: it uses only \(\operatorname{Ad}(A)\operatorname{Ad}(B) = \operatorname{Ad}(AB)\) and \(\operatorname{Tr}\operatorname{Ad}(A) = |\operatorname{Tr}A|^2\)".
    cor:qihara-kraus itself is stated for adjoint-paired families. The any-family statement is
    prop:kraus-conjugation-symmetry (proved), which quotes exactly this proof.
45. **VALID.** "The spectrum of \(T\) is also always closed under conjugation" (prop:kraus-conjugation-symmetry).
46. **MINOR.** Claim box thm:kraus-inverse-pairing-duality. The formula, `N = n²` (N = dim End(V)) and
    μ ↦ q/μ-invariance all match (Corollary 3 of the note; claims.tsv). The label's hypothesis `D = 2m ≥ 4`
    and the trivial set it refers to, `{+1^{[k]},-1^{[k]}}` with `k = N(D−2)/2`, are omitted.
    Replace `The retained set is invariant under \(\mu\mapsto q/\mu\), \(q = D-1\): the functional equation.` →
    `For \(D\ge4\), the retained set (after removing \(\pm1\), each \(k = N(D-2)/2\) times) is invariant under \(\mu\mapsto q/\mu\), \(q = D-1\): the functional equation.`
47. **MINOR.** Claim box thm:kraus-weil-criterion.
    - "but there is no duality": in general there is none. That is prop:kraus-no-duality-example, one family,
      not a theorem that adjoint pairing precludes duality; unitary families are adjoint-paired *and* dual.
    - "Both pairings hold iff every \(B_i\) is unitary" is prop:kraus-both-pairings-unitary, not this label.
    - Part (ii) needs D ≥ 4 and the stated trivial set.
    Replace `so its spectrum is real, but there is no duality, and Weil positivity is exactly the one-sided bound \(|\mu|\le r\). Both pairings hold iff every \(B_i\) is unitary, and then Weil positivity` →
    `so its spectrum is real, but in general there is no duality (prop:kraus-no-duality-example), and Weil positivity is exactly the one-sided bound \(|\mu|\le r\). Both pairings hold iff every \(B_i\) is unitary (prop:kraus-both-pairings-unitary), and then, for \(D\ge4\) and the trivial set \(\{\pm1^{[k]}\}\) plus \(\{q,1\}\) (\(\{-q,-1\}\)) once per eigenvalue \(+1\) (\(-1\)) of \(\Phi\), Weil positivity`
48. **MINOR.** "A quantum channel that is a Ramanujan quantum expander is therefore a Kraus family whose non-backtracking ring norms form a positive definite sequence, in the same sense, with the same trivial set …".
    thm:kraus-weil-criterion(ii) covers only mixed-unitary channels whose Kraus unitaries are closed under
    adjoint, with D ≥ 4. The trivial set is the analogue of the graph's, not the same set (its ±1 multiplicity is
    k = N(D−2)/2, plus pairs per eigenvalue ±1 of Φ).
    Replace `A quantum channel that is a Ramanujan quantum expander is therefore a Kraus family` →
    `A mixed-unitary channel \(\Phi = \frac1D\sum_i\operatorname{Ad}(U_i)\) with the \(U_i\) closed under adjoint (\(D\ge4\)) that is a Ramanujan quantum expander is therefore a Kraus family`
    and replace `with the same trivial set and the same radius` → `with the analogous trivial set and the same radius`.
49. **INVALID.** "The classical graph is the case where the \(B_i\) are the permutation matrices of the generators".
    - With the page's `\mathcal E_i = \operatorname{Ad}(B_i)`, permutation matrices give the permutation action on
      ordered **pairs** of vertices. T is then the Hashimoto matrix of the Schreier graph on X × X, and
      `Tr T^ℓ = Σ_w (#Fix P_w)²`, not the graph's `Σ_w #Fix P_w`.
    - Python, Z₅ with generators ±1, ±2 (Cayley graph = K₅), ℓ = 3, 4, 5, 6: Tr T[Ad(P_i)]^ℓ = 300, 600, 600,
      3900, while Tr B_{K₅}^ℓ = 60, 120, 120, 780. The classical graph is Theorem 1 of the note with
      `\mathcal E_i = P_i` themselves, which reproduces 60, 120, 120, 780.
    - A fixed-point-free reversal needs D even, so odd-degree graphs such as the cubic Petersen graph and the prism
      are not of this form at all. Step 4 treats them directly.
    Replace `The classical graph is the case where the \(B_i\) are the permutation matrices of the generators;` →
    `A \(2m\)-regular Schreier graph is the case of the same construction with \(\mathcal E_i = P_i\) themselves, the permutation matrices of the generators and their inverses acting on the vertices (with \(\operatorname{Ad}(P_i)\) instead one gets the graph on ordered pairs of vertices, whose ring norms are \(\sum_w(\#\operatorname{Fix}P_w)^2\)); odd-degree graphs are treated directly as in step 4;`
    and replace `Replace the permutation matrices behind a graph by arbitrary matrices.` →
    `Replace the permutation matrices behind a Schreier graph by the conjugation maps of arbitrary matrices.`
50. **MINOR.** "the Weil–LPS channels of the notebook are exact examples with \(V = \ell^2(\mathbb F_p)\)".
    def:weil-lps-channel acts on `M_{(p±1)/2}`, the even or odd Weil block, not on ℓ²(𝔽_p). On all of ℓ²(𝔽_p)
    the reducible representation has a fixed-point space of dimension ≥ 2, so the channel is not an expander
    there. Exactness is prop:weil-lps-exactly-ramanujan, status **sketched** (the LPS theorem has no local
    source), checked numerically (num:weil-lps-ramanujan).
    Replace `the Weil–LPS channels of the notebook are exact examples with \(V = \ell^2(\mathbb F_p)\).` →
    `the Weil–LPS channels of the notebook are examples with \(V\) the even or odd Weil block of \(\ell^2(\mathbb F_p)\), of dimension \((p\pm1)/2\) (exactly Ramanujan by Harrow's transfer inequality and Lubotzky–Phillips–Sarnak: sketched in the notebook, checked numerically).`
51. **MINOR.** Step 5 dictionary: "Weil positivity = Hastings' bound = Ramanujan quantum expander".
    thm:kraus-weil-criterion(ii) removes every ±1 eigenvalue of Φ. A Ramanujan quantum expander additionally has a
    unique fixed point and no eigenvalue −1 (def:quantum-expander), so the second "=" holds in one direction only.
    Replace `Weil positivity = Hastings' bound = Ramanujan quantum expander` →
    `Weil positivity = Hastings' bound on the eigenvalues of \(\Phi\) other than \(\pm1\) (with a unique fixed point and no \(-1\): a Ramanujan quantum expander)`
52. **VALID.** Demo F caption: "sixteen-dimensional lifted transfer operator". With D = 4 and dim End(ℂ²) = 4,
    it is 4 · 4 = 16. The adjoint/inverse/unitary/no-duality options match the 08b labels. The demos-kraus.js
    readout strings cite prop:kraus-no-duality-example and thm:kraus-weil-criterion (i) correctly. There is no
    `lanes/kraus.md`.
53. **VALID.** Step 5 dictionary: "reality (Hilbert–Pólya half) | adjoint pairing". This is the reality of
    spec(Σ), not of spec(T) (X2). The functional equation row, inverse pairing, is also right.

### Step 6

54. **MINOR.** "An element of \(\mathbb F_{q^m}\) in a self-dual normal basis is a ring of \(m\) sites". For odd q a
    self-dual normal basis exists only for odd m (06 shard; asm:normal-basis). Even m uses a general normal basis
    with trace form `C·P_g(S)`, which is exactly where the sign ε_m comes from (06b). The shard also assumes q an
    odd prime.
    Replace `An element of \(\mathbb F_{q^m}\) in a self-dual normal basis` →
    `For \(q\) an odd prime, an element of \(\mathbb F_{q^m}\) in a normal basis (self-dual when \(m\) is odd; for even \(m\) the basis Gram matrix is what produces the sign \(\epsilon_m\) below)`
55. **VALID.** The transfer-matrix entry formula is eq:as-transfer-entries verbatim (rows = output state).
    `S_m = ε_m Tr E^m` is thm:as-sign-law. `N_m = q^m + Σ_{a≠0} S_m(ag)` is the affine count of eq:as-hilbert90;
    the projective count adds 1 (thm:as-super-transfer).
56. **VALID.** "\(\epsilon_m = -(-1)^m\) when \(P_g(-1)\ne0\), as for \(g = x^{1+q}\), and periodic with a longer period otherwise".
    - cor:as-periodic-sign gives `S_n = (1 − 2[2h | n]) Tr E^n`, with h the least power of q exceeding v₋.
    - P_g(−1) ≠ 0 means v₋ = 0 and h = 1, so ε = −(−1)^m.
    - For a = (0,1): P_g(z) = a₀ + ½(z + z⁻¹), so P_g(−1) = −1 ≠ 0 (06b table: q = 3, (0,1), v₋ = 0, h = 1).
    - Otherwise h ≥ q, so the period is 2h ≥ 2q > 2.
    - Status caveat: claims.tsv lists thm:as-sign-law as `proved`, but the shard's `\claimstatus` is
      `proved-conditional` (it rests on asm:normal-basis).
57. **INVALID.** "The transfer matrix is, up to that sign, the Frobenius matrix of the exponential sum, uniformly in \(m\)."
    - This is the founding-session claim that 06 and 06b explicitly correct.
    - thm:as-frobenius-block: the Frobenius block F (with `S_n = −Tr F^n`) may be taken as −E only when
      P_g(−1) ≠ 0. Otherwise F is a different √q-unitary, diagonal matrix whose multiplicities come from the
      m_E formula.
    - cor:as-periodic-sign: "α_i = −λ_i(E_g) holds for all n iff P_g(−1) ≠ 0".
    - An m-dependent sign ε_m makes the sentence tautological at best.
    Replace `The transfer matrix is, up to that sign, the Frobenius matrix of the exponential sum, uniformly in \(m\).` →
    `When \(P_g(-1)\ne0\), \(-E\) is the Frobenius matrix of the exponential sum, uniformly in \(m\); otherwise the Frobenius block is a different \(\sqrt q\)-unitary matrix built from the spectrum of \(E\) (thm:as-frobenius-block), and the traces of \(E\) give the sums only up to the periodic sign.`
58. **VALID.** `EE^† = q·1` by the oldest-spin argument when a_J ≠ 0 (prop:as-unitarity, proved). The AS lane
    measured residuals of 3e−16 to 9e−16.
59. **VALID.** Toeplitz form of `Tr(E/√q)^k` = Gram matrix of the strips with G = 1 (no trivial set;
    prop:ccm-tn-operator-gram in the native metric).
60. **VALID.** "RH manifest … Parseval for additive characters, the same mechanism as the permutation"
    (06: obs:rh-finite-permutation mechanism; the character sum `Σ_s ψ(a s(x′−x″)) = qδ`).
61. **VALID.** Functional equation `E ↦ qE^{−†}` (trivial for a scaled unitary); "rationality is finiteness of
    the bond" (06, "RH is unitarity" subsection).
62. **MINOR.** "there is no fixed local tensor, and the Weil bound is Deligne's theorem". The shard says there is
    no fixed local tensor *in the shift basis* ("Whether a different basis … makes cubic traces local was neither
    settled nor searched"). For these one-variable sums on curves the bound is Weil's theorem; the shard's table
    says "Weil / Deligne".
    - Replace `there is no fixed local tensor, and the Weil bound is Deligne's theorem` →
      `there is no fixed local tensor in that basis (none is known in any basis), and the Weil bound is Weil's theorem (Deligne's in general)`.
    - Dictionary: replace `non-quadratic \(g\): no local tensor;` → `non-quadratic \(g\): no local tensor in the shift basis;`.
63. **VALID.** Demo G caption. The perturbation leaves the circle, and whether the form goes negative depends on
    the disc. This matches the AS lane (finding 3): for (3,(0,1)) and (5,(0,1)) the form stays positive. N_m stops
    being an integer at some m.
64. **MINOR.** Step 6 dictionary "ring norms | \(\operatorname{Tr}E^m\)", the complete-dictionary "ring norms
    (side A)" row, and TERMS `ringnorm` ("a nonnegative count …; for a curve the number of points"). For
    Artin–Schreier, `Tr E^m` is a complex exponential sum: a ring *contraction*, not a norm, not nonnegative, and
    not the number of points (`N_m = q^m + Σ_a S_m(ag)`). The same holds for ζ, whose distribution has negative
    parts.
    - Step 6 dictionary: replace `<td>ring norms</td><td>\(\operatorname{Tr}E^m\), the exponential sum \(S_m\) up to sign</td>` →
      `<td>ring contractions</td><td>\(\operatorname{Tr}E^m\) (complex, not a norm), the exponential sum \(S_m\) up to sign</td>`.
    - TERMS `ringnorm`: replace `It is the notebook's name for side A: a nonnegative count of closed configurations` →
      `It is the notebook's name for side A: for an MPS a nonnegative count of closed configurations`.
    - TERMS `ringnorm`: replace `for a curve the number of points,` →
      `for an Artin–Schreier curve the exponential sum \\(S_m\\) up to sign (a complex ring contraction, from which the point count follows),`.
65. **VALID.** Step 6 dictionary rows for the pole ("q^m in N_m; absent from the exponential sum … polynomial";
    asm:as-lpolynomial), the metric row, and the Dwork row (obs:as-nonquadratic: rationality and functional
    equation, p-adic sizes only).

### Step 7

66. **MINOR.** "Tr E^x" = `2\cosh(x/2) - \sum_n\frac{\Lambda(n)}{\sqrt n}(\delta_{\log n}+\delta_{-\log n}) - (\text{archimedean kernel})`.
    This is **VALID** in the parent's normalisation: `W(g) = ∫g·2cosh(x/2) − Σ Λ(n)n^{−1/2}(g(log n) + g(−log n)) − arch`.
    But "its Fourier transform is \(\sum_\rho \delta_{\gamma_\rho}\)" is off by 2π. The distribution is
    `Σ_ρ e^{iγ_ρ x}` (since `⟨D,g⟩ = Σ ĝ(γ_ρ)`), and with `ĝ(γ) = ∫g e^{iγx}dx` its transform is
    `2π Σ_ρ δ_{γ_ρ}`, counted with multiplicity and using γ ↔ −γ symmetry.
    Replace `and that its Fourier transform is \(\sum_\rho \delta_{\gamma_\rho}\), the spectral side.` →
    `and that it equals \(\sum_\rho e^{i\gamma_\rho x}\) (zeros with multiplicity), so that \(\langle\text{“}\operatorname{Tr}E^x\text{”},g\rangle = \sum_\rho\hat g(\gamma_\rho)\): the spectral side.`
67. **MINOR (convention).** `G_{ij} = \langle E^{g_i},E^{g_j}\rangle = W(g_i*\tilde g_j)`. The lab convention (02i)
    makes the inner product conjugate-linear in the first slot. Then
    `⟨E^{g_i},E^{g_j}⟩ = ∬ conj g_i(x) g_j(y) "Tr E^{y−x}" = W(g̃_i * g_j) = W(g_j * g̃_i)`. That is the parent's
    G_ji = conj(G_ij), not G_ij. On the zero side (under RH) `⟨E^{g_i},E^{g_j}⟩ = Σ conj ĝ_i ĝ_j`, while the
    parent's `G_ij = Σ ĝ_i conj ĝ_j`. The two agree for real g, as in Demo H.
    Replace `G_{ij} = \big\langle E^{g_i},E^{g_j}\big\rangle = W(g_i*\tilde g_j)` →
    `G_{ij} = \big\langle E^{g_j},E^{g_i}\big\rangle = W(g_i*\tilde g_j)`.
68. **VALID.** "Every entry is a finite computation from the primes, the pole and the archimedean term" (compact
    support; parent step 6).
69. **VALID.** "Under RH this is the Gram matrix of the functions \(\hat g_i\) restricted to the zeros in
    \(\ell^2(\text{zeros})\) … the metric … exists, and in it the dilation semigroup … is unitary". The GNS
    construction of a PSD translation-invariant form gives it, with multiplicities as weights, so no Jordan issue
    arises. It is explicitly conditional.
70. **VALID.** "whether the sequence of overlaps is a Gram sequence at all. That is Weil's criterion"
    (cit:weil-criterion, status *cited*, not proved).
71. **VALID.** Tomography sentence (metric-as-state.md §3: "every expectation value W(f*f~) is measurable from
    arithmetic").
72. **MINOR.** Demo H caption: "Switch off the primes to see that the pole and the archimedean place alone give no
    positive form." This holds for the default strips but not in general. Python, s = 0.08, pole − arch only:
    - n ∈ {1,2,3,4,6}: eigenvalues −0.0998, −0.0363, −0.00024, 0.0468, 0.2341 (indefinite, as claimed);
    - {1}: 0.0289 (positive);
    - {2,3}: 0.0109, 0.0469 (positive; Yoshida-type small support).
    Replace `Switch off the primes to see that the pole and the archimedean place alone give no positive form.` →
    `Switch off the primes to see that, for the default strips, the pole and the archimedean place alone give an indefinite form.`
73. **VALID.** "in step 2 the strips \(P^0,\dots,P^{K-1}\) become linearly dependent once \(K\) exceeds the number
    of distinct eigenvalues, and the kernel polynomial's roots are the spectrum". This is num:weil-window-extension
    for (1 2)(3 4 5): four distinct atoms, W_K singular from K = 4 (lab indexing, K+1 lags), kernel roots = the
    four distinct eigenvalues.
74. **MINOR.** "For zeta the spectrum is infinite, so the Gram matrix has no kernel". That no window Gram matrix
    has a kernel is not a theorem (without RH, positivity itself is unknown). It is a certified fact at x = 13:
    even-block λ_min = 1.566e−39 > 0, odd minimum 2.1e−36.
    Replace `For zeta the spectrum is infinite, so the Gram matrix has no kernel, but` →
    `For zeta the spectrum is infinite and the window Gram matrix at \(x = 13\) is certified positive definite (no kernel), but`
75. **VALID.** "the CCM correction turns that direction into an operator whose spectrum reproduces the low zeros to
    dozens of digits". thm:ccm-tn-loewner-quotient (proved): D′ = D − |Dξ⟩⟨η| descends to a self-adjoint D″.
    From data-riemann.js, |z_k − γ_k| = 2.27e−35, 1.15e−31, 2.44e−29, 9.53e−26, 4.45e−24, 5.09e−21, 3.32e−18,
    2.29e−16 for k = 1..8, then 1.3e−11, 3.4e−9, 2.2e−5 and 0.36 at k = 12. "The low zeros" is accurate.
76. **VALID.** Demo I readout: "the primes below x = 13 pinning γ₁ to 35 digits".
    - The error is 2.27e−35 absolute, and log₁₀(14.1347/2.27e−35) = 35.8, so about 35 significant digits
      (34 decimal places).
    - The prime powers entering are ≤ 13. n = 13 sits at the support endpoint y = L of the correlation, where
      u*∗u vanishes, so it contributes 0.
    - "Primes below x" is the lab's own phrasing (metric-as-state §4.1).
    - Optional precision edit: `pinning γ₁ to 35 digits` → `pinning γ₁ to within 2.3·10⁻³⁵ (about 35 significant digits)`.
77. **VALID.** Demo I readout: "D′ = D − |Dξ⟩⟨η| has real spectrum". D′ξ = 0, and the rest is the self-adjoint D″
    in metric T (thm:ccm-tn-loewner-quotient, under even-simple).

### Complete dictionary

78. **VALID.** Letters row.
79. **VALID.** Bond row.
80. **MINOR.** Ring norms (side A) row: `Tr E^m` is a complex contraction (item 64).
    Replace `→ \(\operatorname{Tr}E^m\) → the explicit-formula distribution` →
    `→ \(\operatorname{Tr}E^m\) (a complex ring contraction) → the explicit-formula distribution`.
81. **MINOR.** Trivial set row: "→ the same →" for Kraus families. The trivial set there is ±1 × k with
    k = N(D−2)/2, plus {q,1} ({−q,−1}) per eigenvalue +1 (−1) of Φ (thm:kraus-weil-criterion). That is analogous,
    not the same.
    Replace `→ the same → \(q^m\) in \(N_m\)` →
    `→ \(\{\pm1\}\) and \(\{q,1\}\) (\(\{-q,-1\}\)) per eigenvalue \(\pm1\) of \(\Phi\) → \(q^m\) in \(N_m\)`.
82. **VALID.** Critical radius row.
83. **VALID.** Functional equation row.
84. **INVALID.** Weil form row: "in every case the Gram matrix of open strips, \(T_{jk} = \operatorname{Tr}((E^j)^\sharp E^k)\), built from counts".
    Where no unitarising metric exists, the Toeplitz matrix of counts is not a Gram matrix of the strips. For the
    prism C16×K2 and for C21×K2 it is not PSD at all (λ_min(K = 16) = −29.17 and −689.4; graphs lane), so it is not
    a Gram matrix of any vectors.
    Replace `<td>in every case the Gram matrix of open strips, \(T_{jk} = \operatorname{Tr}((E^j)^\sharp E^k)\), built from counts</td>` →
    `<td>in every case the Toeplitz matrix of the counts, \(T_{jk} = t_{k-j}\); it is the Gram matrix of the open strips, \(\operatorname{Tr}((E^j)^\sharp E^k)\), exactly when a unitarising metric \(G\) exists</td>`
85. **INVALID.** Metric row: "Hilbert–Pólya on the edge space iff Ramanujan → iff Hastings".
    - Graph counterexample: item 40.
    - Kraus counterexample (Python): Z₂₄ with unitary permutation letters P(±1), P(±11), D = 4, q = 3,
      E_i = Ad(P_i), adjoint-paired, so unitary and both pairings hold. The nontrivial adjacency eigenvalues
      satisfy max |a| = 2√3 exactly (twice), so Hastings' bound holds with equality.
    - T on 2304 dimensions has dim ker(T − √3) = 48 and dim ker(T − √3)² = 96: Jordan blocks at √q, hence no
      Hilbert–Pólya metric.
    Replace `<td>\(1\) → none in general → Hilbert–Pólya on the edge space iff Ramanujan → iff Hastings → native, \(EE^\dagger = q\) → the unknown</td>` →
    `<td>\(1\) → none in general → Hilbert–Pólya on the edge space iff Ramanujan and semisimple (no \(a = \pm2\sqrt q\)) → iff Hastings and semisimple → native, \(EE^\dagger = q\) → the unknown</td>`
86. **VALID.** Riemann hypothesis row.

### TERMS

87. **VALID.** `mps`.
88. **MINOR.** `transfer`: "Its leading eigenvalue is the fixed point of the channel (the pole)". This is the same
    looseness as item 27. The "single modulus" RH sentence is fine.
    Replace `Its leading eigenvalue is the fixed point of the channel (the pole);` →
    `Its leading eigenvalue is the pole, and the corresponding eigenvector is the fixed point of the normalised channel;`
89. **MINOR.** `ringnorm`: see item 64.
90. **VALID.** `strip` ("states of different lengths … zero overlap"; 03g).
91. **VALID.** `gram`.
92. **VALID.** `metric`. The formulas match def:ccm-tn-feature. The "Level 2 / Level 3" wording could not be
    matched to a shard; see (c).
93. **VALID.** `trivial`.
94. **VALID.** `radius`.
95. **MINOR.** `reflection`: "An off-circle pair \\(\\{\\mu,J\\mu\\}\\) contributes \\(2\\operatorname{Re}[p_c(\\mu)\\overline{p_c(J\\mu)}]\\)".
    prop:weil-orbit-negative has `2m·Re(f_c(z) conj f_c(Jz))` with z = μ/r.
    Replace `contributes \\(2\\operatorname{Re}[p_c(\\mu)\\overline{p_c(J\\mu)}]\\)` →
    `contributes \\(2m\\operatorname{Re}[p_c(\\mu/r)\\overline{p_c(J\\mu/r)}]\\) (multiplicity \\(m\\))`.
96. **VALID.** `hashimoto`.
97. **VALID.** `ihara`. The Petersen vis spectrum {3, 1⁵, (−2)⁴} is inside ±2√2.
98. **INVALID** (one clause). `ramanujan`: "equivalent, by the notebook's theorems, to Weil positivity … and to the
    existence of a Hilbert–Pólya metric on the retained edge space". The second equivalence fails (item 40).
    "Spectral radius of the infinite (q+1)-regular tree" is VALID (def:ramanujan-graph). The prism vis value
    a = 2.848 > 2√2 is VALID.
    Replace `to Weil positivity of the rescaled non-backtracking ring norms and to the existence of a Hilbert–Pólya metric on the retained edge space.` →
    `to Weil positivity of the rescaled non-backtracking ring norms; a Hilbert–Pólya metric on the retained edge space exists iff in addition no adjacency eigenvalue equals \\(\\pm2\\sqrt q\\) (where the Hashimoto matrix has a Jordan block).`
99. **INVALID.** `edgelift`: "For permutation matrices this is the Hashimoto matrix of the Cayley graph." See
    item 49: with Ad(P_i) it is the Schreier graph on ordered pairs, and with P_i themselves the Schreier graph on
    the vertices. It is a Cayley graph only for the regular action.
    Replace `For permutation matrices this is the Hashimoto matrix of the Cayley graph.` →
    `With \\(\\operatorname{Ad}(B_i)\\) replaced by permutation matrices \\(P_i\\) themselves this is the Hashimoto matrix of the Schreier graph of the generators (the Cayley graph for the regular action); with \\(\\operatorname{Ad}(P_i)\\) it is that of the graph on ordered pairs of vertices.`

### Footer

100. **VALID.** Conventions line: `E`, `t_L`, `ν_ℓ`, the Weil form `Σ c_j c̄_k ν_{j−k}` (= def:weil-form), and J.
101. **MINOR.** "every one quoted is proved there (author and reviewer from different model families where stated)".
     Every boxed label is `proved` in claims.tsv: prop:ccm-tn-operator-gram, prop:hp-inner-product-discrete,
     thm:weil-positivity-finite, thm:weil-duality-pairing, thm:kraus-inverse-pairing-duality and
     thm:kraus-weil-criterion. However:
     - thm:as-sign-law (cited in step 6) is `proved` in claims.tsv but `proved-conditional` in shard 06b;
     - prop:ccm-tn-operator-gram's review is "independent same-family" (codex author, codex reviewer);
     - cit:weil-criterion is only `cited`, and prop:weil-lps-exactly-ramanujan (implicit in step 5) is `sketched`.
     Replace `every one quoted is <code>proved</code> there (author and reviewer from different model families where stated).` →
     `every one in a margin tag is <code>proved</code> there (thm:as-sign-law is <code>proved-conditional</code> in its shard; Weil's criterion is cited, the Weil–LPS exactness sketched).`
102. **VALID.** "Nothing on this page assumes the Riemann hypothesis except where a comparison is labelled". Step 7's
     "Under RH …" is explicitly conditional. Zeros appear only in comparison panels (Demo E, G, H, I, A) and in the
     comparison-labelled |z_k − γ_k| readout. The one exception is the Demo C verdicts (item 32).

### Claim-label existence audit (task list)

All exist in `db/claims.tsv`:

| label | status | cited on page? |
|---|---|---|
| prop:ccm-tn-operator-gram | proved | margin tag |
| prop:hp-inner-product-discrete | proved | margin tag |
| thm:weil-positivity-finite | proved | margin tag |
| thm:weil-duality-pairing | proved | margin tag (twice) |
| thm:kraus-inverse-pairing-duality | proved | margin tag |
| thm:kraus-weil-criterion | proved | margin tag |
| thm:as-sign-law | proved (shard: proved-conditional) | in text |
| prop:weil-orbit-negative | proved | not cited (content used in TERMS `reflection`) |
| prop:kraus-both-pairings-unitary | proved | not cited (content in the kraus-weil-criterion box; see item 47) |
| cor:qihara-kraus | proved | not cited |
| cit:weil-criterion | cited | not cited |

Paraphrase mismatches: items 9, 11, 46 and 47.

## (b) Summary count

102 statements checked. **VALID 58 · MINOR 35 · INVALID 9.**

The INVALID items are 23, 40, 41, 49, 57, 84, 85, 98 and 99. They reduce to four errors:

1. **The "Ramanujan ⇔ metric" (and "Hastings ⇔ metric") equivalence fails at the edge a = ±2√q.** The Hashimoto
   matrix, or T for Kraus families, has Jordan blocks there. Explicit counterexamples: C₃×C₆×K₂ for graphs, and the
   Z₂₄ unitary family for Kraus. This affects items 40, 41, 85 and 98.
2. **Permutation matrices under Ad do not give the classical graph.** They give the graph on ordered pairs
   (Tr T³ = 300 against 60 for K₅). Odd degree is excluded by a fixed-point-free reversal. This affects items 49
   and 99.
3. **The graded-permutation paragraph attributes a sign to the point-letter ring that shard 03b proves absent.**
   `Tr(ΠP^k)` is a bond supertrace, not a ring norm. This is item 23.
4. **"E is, up to sign, the Frobenius matrix uniformly in m" is the corrected founding claim.** It holds only when
   P_g(−1) ≠ 0 (thm:as-frobenius-block). This is item 57. In the same family of errors, the Weil form is "in every
   case a Gram matrix" (item 84), false wherever it is indefinite.

## (c) Could not verify from the notebook

- **TERMS `metric`: "Level 2 of the metric problem is the existence of such a G …; Level 3 is a construction."**
  metric-as-state §3 mentions "Level 3" (a construction making positivity manifest) but does not define "Level 2";
  the numbering is presumably in HANDOFF or another note that I did not read.
- **Whether a = ±2√q always gives a Jordan block in the Kraus T.** For graphs this is the companion-block
  structure. For the Kraus family I verified it only in the one Z₂₄ example. The notebook has no label stating
  semisimplicity (or not) of T at α = ±2√q; 08b records only the algebraic multiplicity 2a_α. The replacement
  texts therefore say "and semisimple" rather than asserting a Jordan block for Kraus.
- **The demo readouts for the Kraus station** (no `lanes/kraus.md`). I checked only that the readout strings cite
  the right labels. I did not rerun `check_kraus.py` or compare its numbers with the page.
- **The exact archimedean-kernel form in step 7.** I took it from the parent artifact
  (`g(0) log π + ∫₀^∞ …`), which states it was checked against 3000 zeros. I did not re-derive it.
