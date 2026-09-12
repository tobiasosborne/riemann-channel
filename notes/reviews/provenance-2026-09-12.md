# Adversarial provenance review — `notes/quantum-ihara-general.md` §5 and `notes/prior-art-quantum-ihara.md`

Reviewer: Claude Opus 5 (1M), REFUTE stance, 2026-09-12. No memory of the author's session; no web
access; everything checked against `refs/src/` only. `sha256sum -c refs/manifest.sha256` returns OK
for all 41 recorded `.tex` files, so the line numbers below are against exactly the bytes the author
cited. Numerics for §B/§C are in `notes/reviews/scratch_wf_mo_conventions.py`.

Summary up front: **no quoted string is misquoted or fabricated** — every quoted fragment appears
verbatim, contiguous, at or within two lines of its stated position. What fails is (a) the *addresses*:
11 citations name a file that does not exist under `refs/src/`, 2 point past the end of the file they
name, 2 line ranges do not contain the quote they label; and (b) one convention claim: a bouquet is
**not** a graph in Watanabe–Fukumizu's sense, so Theorem 1 is not literally the one-vertex case of
their corollary, even though the two formulas agree exactly (verified symbolically and numerically).

---

## A. Byte-check of every `<id>:<file>:<line>` citation

Legend: **OK** = quoted text present, whole and contiguous, at the cited line(s) (whitespace
normalised). **LINE** = text genuine but the cited range does not contain it. **FILE** = the cited
file does not exist in `refs/src/<id>/`; text and line number are correct in the file that is there.
**NOT FOUND** = nothing at that address.

### `notes/quantum-ihara-general.md` §5

| # | citation | fragment | status |
|---|---|---|---|
| G1 | `1103.0605:section3.tex:330-341` | `Z_{G}(\bs{u})^{-1}= \det ( I + \hat{\mathcal{D}}(\bsu) - \hat{\mathcal{A}}(\bsu) ) \prod_{[e] \in {E}} \det(I - u_e u_{\bar{e}})` | **OK** (lines 333–335; source continues `, \label{eq:IBfornonhyper}`) |
| G2 | `1103.0605:section3.tex:330-341` | `(\hat{\mathcal{D}}(\bsu)g)(i):= \Big( \sum_{e: t(e)=i}(I_{r_i}-u_eu_{\bar{e}})^{-1}u_eu_{\bar{e}} \Big)g(i)` | **OK** (line 339, after a leading `&`) |
| G3 | `1103.0605:section3.tex:330-341` | `(\hat{\mathcal{A}}(\bsu)g)(i):= \sum_{e: t(e)=i}(I_{r_i}-u_eu_{\bar{e}})^{-1}u_e g(o(e))` | **OK** (line 340, after a leading `&`) |
| G4 | `1103.0605:section3.tex:373` | "Corollary \ref{cor:IBfornonhyper} gives the extension of the result to graphs with arbitrary weights." | **OK** (line 373, exact, whole line) |
| G5 | `2204.06424:main.tex:476` | "Suppose $X_{e}$ $(e\in E)$ are invertible matrices of size $K$ living on each edge." | **OK** (line 476, exact, whole line) |
| G6 | `2204.06424:main.tex:516-519` | pointer to eq. (2.11), no quoted text | **OK** — the `align` runs 515–520, the formula body is 516–518, and it really is equation **(2.11)** (I recounted the numbered equations of their §2: 2.1@330, 2.2@358, 2.3@379, 2.4@394, 2.5@425, 2.6@438, 2.7@461, 2.8@478, 2.9@487, 2.10@502, 2.11@515, 2.12@522) |
| G7 | `HANDOFF.md` item 1 | "the formula of `HANDOFF.md` item 1" | **OK** (`HANDOFF.md:15-17`, identical formula) |

Nit: §5 writes "Corollary `IBfornonhyper`"; the LaTeX label is `cor:IBfornonhyper` (the prior-art note
gets this right).

### `notes/prior-art-quantum-ihara.md` §2

| # | citation | status | detail |
|---|---|---|---|
| P1 | `2204.06424:main.tex:476` | **OK** | exact whole line |
| P2 | `2204.06424:main.tex:480-485` (eq. 2.8) | **LINE** | text is genuine but sits at **479–482**; line 479 is `\zeta_G(q;X) \equiv`, which is *outside* the cited range. Cited range 480–485 holds only `\det\Bigl(...\Bigr)^{-1}`, the label and `\end{align}` |
| P3 | `2204.06424:main.tex:489-494` (eq. 2.9) | **OK** | both `X_{e} & {\rm if}...` (489) and `X_{e}^{-1} & {\rm if}...` (490) inside the range; source has a double space in `E, \  t(e)`, immaterial after whitespace normalisation |
| P4 | `2204.06424:main.tex:505-510` (eq. 2.10) | **LINE** | text is genuine but sits at **503–505**. The cited range starts at the quote's *last* line (`    }\,,`); the head `\zeta_G(q;X) = \exp\lrpar{` (503) and the sum (504) are outside it |
| P5 | `2204.06424:main.tex:516-519` (eq. 2.11) | **OK** | body at 516–518, inside the range |
| P6 | `2204.06424:main.tex:533-534` | **OK** | exact, spans both lines |
| P7 | `2204.06424:main.tex:696` | **OK** | exact |
| P8 | `2208.14032:main.tex:137` | **OK** | exact whole line |
| P9 | `2607.27935:main.tex:381` | **OK** | line 381, after a leading `&`, before `\,,` |
| P10 | `2607.27935:main.tex:401-404` | **OK** | first fragment 401, second 403–404 |
| P11 | `2607.27935:main.tex:508-510` | **OK** | prose at 508, `\rho_{\rm adj}(U_e) = U_e\otimes U_e^\dag` at 510 |
| P12 | `1103.0605:section3.tex:307-318` | **OK** | "matrix weights..." at 309–310, `Z_{G}(\boldsymbol{u}):=...` at 312–318 |
| P13 | `1103.0605:section3.tex:330-341` | **OK** | as G1–G3 |
| P14 | `1103.0605:section3.tex:373` | **OK** | exact |
| P15 | `1801.00876:main.tex:158` | **FILE** | no `main.tex`; the source is `tenseur9.tex`, where line **158** is the quote, exact |
| P16 | `1801.00876:main.tex:165` | **FILE** | `tenseur9.tex:165`, exact |
| P17 | `1801.00876:main.tex:779-786` | **FILE** | `tenseur9.tex`: prose at 779–781, `B = \sum_{j \ne i^*} a_j \otimes S_i \otimes E_{ij}` at 784 — both inside 779–786 |
| P18 | `1801.00876:main.tex:608-610` | **FILE** | `tenseur9.tex`: quote spans 608–610, exact |
| P19 | `2304.05714:main.tex:2568` | **FILE** | no `main.tex`; source is `PT-RC_reloaded.tex`, line **2568**, both sentences exact |
| P20 | `2304.05714:main.tex:399` | **FILE** | `PT-RC_reloaded.tex:399`; elision replaces "to study operators of the form \eqref{eq:defA}." — faithful |
| P21 | `0706.0556:main.tex:118-122` | **FILE** | no `main.tex`; source is `sd10.tex`: prose 118–120, `\lambda_{H}=\frac{2\sqrt{D-1}}{D}.` at 122 |
| P22 | `0709.1142:expand.tex:72-73` | **FILE** | no `expand.tex`; the arXiv source was a bare gzipped `.tex`, unpacked by `fetch_sources.sh` as `main.tex`, where **72–73** is the quote, exact |
| P23 | `0709.1142:expand.tex:213-217` | **FILE** | `main.tex`: `\lambda_2(\cE) \leq \lambda_2(W_\Gamma)` at 213, the gloss at 214–217 |
| P24 | `2602.15180:main.tex:241` | **OK** | exact |
| P25 | `2602.15180:main.tex:362` | **OK** | exact |
| P26 | `2602.15180:main.tex:1508` | **OK** | exact |
| P27 | `2209.07024:abstract.tex:8` | **OK** | exact |
| P28 | `2209.07024:quan_exp.tex:37` | **OK** | exact |
| P29 | `2105.02677:main.tex:87-89` | **OK** | spans 87–89 |
| P30 | `2309.15873:main.tex:131` | **FILE** | no `main.tex`; source is `AiM_Final.tex`, line **131**, exact |
| P31 | `2405.04361:main.tex:427` | **FILE** | no `main.tex`; source is `v3.tex`, line **427**, exact |
| P32 | `2204.06424:main.tex:3068` (Sunada, "ref [6]") | **NOT FOUND** | `main.tex` is 2342 lines. Sunada is `main.bbl:30` (`\bibitem{sunada1986functions}`) / `refs.bib:1067`; cited in the body at `main.tex:191,329`. The "**ref [6]**" part *is* right — it is the 6th `\bibitem` |
| P33 | `2204.06424:main.tex:3095-3096` (Hashimoto) | **NOT FOUND** | out of range. Actual: `main.bbl:94` and `main.bbl:100` (`hashimoto1989zeta`, `hashimoto1990zeta`) / `refs.bib:1076,1085`; cited in the body at `main.tex:393,424` |

Tally: 39 rows across the two tables (33 prior-art + 6 in §5, excluding the `HANDOFF.md` pointer) —
**24 OK, 2 LINE, 11 FILE, 2 NOT FOUND**. Zero misquotes: every quoted string, in all 39, is verbatim
and contiguous in the file that actually holds it.

---

## B. Convention check: is Theorem 1 the one-vertex case of Watanabe–Fukumizu `cor:IBfornonhyper`?

Sources read: `refs/src/1103.0605/section2.tex:11-42` (hypergraph/graph definitions),
`section3.tex:1-200` (zeta, `thm:det1`, the §3.2 weight assumption), `section3.tex:200-290`
(`thm:Ihara`), `section3.tex:291-400` (graph specialisation, `cor:IBfornonhyper`, scalar reduction).
Macros from `main.tex:57-134`: `\etea` = `e' \rightharpoonup e`, `\edai` = `\alpha \rightarrow i`,
`\mat{a}{b}` = `M(a,b)`.

### (i) Order of composition in π(p)

WF's graph-case definition (`section3.tex:312-318`) is
`\pi(\mathfrak{p}):=u_{e_1} \cdots u_{e_k}` for `\mathfrak{p}=(e_1,\ldots,e_k)` — **first step
leftmost**. The note's Corollary 2 Euler product and trace formula compose **last step leftmost**
(`E_{i_\ell}\cdots E_{i_1}`). These are opposite, and reversing a product of ≥3 matrices is *not* a
cyclic permutation, so the two conventions give **different individual Euler factors**.

They nonetheless give the same zeta and the same `det(1-uT)`, for two independent reasons:

* on a one-vertex graph the map `(i_1,…,i_ℓ) ↦ (i_ℓ,…,i_1)` is a bijection of the set of cyclically
  non-backtracking index sequences — the constraint `i_{k+1} ≠ σ(i_k)` is symmetric because σ is an
  involution and every pair of edges is composable — so the *products over all prime classes* (and the
  traces `Tr T^ℓ`) agree even though term-by-term they do not;
* more directly, WF's edge operator is `M(u)_{e,e'} = u_e` for `e' ⇀ e` (`section3.tex:162-169`), i.e.
  weight of the **target** edge, whereas the note's `T_{j,i} = E_i` weights the **source** edge. With
  `d = diag(uE_e)` and `B_{e,e'} = [e' ≠ ē]` one has `M = dB` and `T = Bd` (note `B = Bᵀ` here), so
  `det(1-M) = det(1-uT)` by Sylvester. Verified numerically to 4e-16 (`scratch_wf_mo_conventions.py`,
  column `detWFedge`).

So: **order does not matter for the final determinant, but the note's §5 asserts the identification
without either step.** Add one sentence. (For the record, WF are internally inconsistent here: their
hypergraph definition `section3.tex:93-95` gives `\pi(\mathfrak{p}) = u_{e_k⇀e_1}\ldots u_{e_1⇀e_2}`,
the *reverse* of their graph definition at line 315, the two being reconciled only by the same
reversal bijection.)

### (ii) Do D̂ and Â specialise as the note says?

Yes — exactly, and the note's stated route is correct. On a one-vertex graph every directed edge has
`t(e) = o(e) = *`, so with `r_* = N` and `u_e = u·E_e`:

* `Â = Σ_{e:t(e)=*} (I - u_e u_ē)^{-1} u_e g(o(e)) = u Σ_{e=1}^{D} (1 - u²E_eE_ē)^{-1} E_e`,
* `D̂ = Σ_{e:t(e)=*} (I - u_e u_ē)^{-1} u_e u_ē = u² Σ_{e=1}^{D} (1 - u²E_eE_ē)^{-1} E_eE_ē`,
* the prefactor `∏_{[e]∈E} det(I - u_e u_ē)` becomes the note's `∏_{\{i,ī\}} det(1 - u²E_īE_i)`
  (m factors, well defined by Sylvester).

Turning these into the note's `A(u) = u Σ_i E_i(1-u²E_īE_i)^{-1}` and
`D(u) = u² Σ_i E_īE_i(1-u²E_īE_i)^{-1}`:

* **A**: pure push-through, `(1-u²E_eE_ē)^{-1}E_e = E_e(1-u²E_ēE_e)^{-1}` (i.e. `(1-XY)^{-1}X =
  X(1-YX)^{-1}` with `X = E_e`, `Y = u²E_ē`). No relabelling needed. ✔
* **D**: `(1-u²E_eE_ē)^{-1}E_eE_ē = E_eE_ē(1-u²E_eE_ē)^{-1}` (commuting factors); substituting `e = ī`
  turns the `e`-th WF term into the `i`-th note term, and `e ↦ ē` is a bijection of the directed edge
  set, so the two sums are equal term-for-term after relabelling. ✔

Both claims confirmed to machine precision (`Ahat-vs-A ≤ 1.2e-16`, `Dhat-vs-D ≤ 1.4e-17` for random
non-normal complex `E_i`, N=3, D=6), and the whole corollary RHS equals `det(1-uT)` to 4.5e-16.
**The note's one-line "push-through + relabelling in D" is exactly right.**

### (iii) Do Watanabe–Fukumizu allow loops? **No — and this is the defect.**

`section2.tex:17-25`: "A **hypergraph** $H=(V,F)$ consists of a set of *vertices* $V$ and a set of
*hyperedges* $F$. A hyperedge is a non-empty subset of $V$. … $d_{\alpha}:=|N_{\alpha}|=|\alpha|$ …
If all the degrees of hyperedges are two, then the hypergraph is naturally identified with an ordinary
graph." And `section3.tex:282-283`: "A hypergraph $H=(V,F)$, which has only hyperedges of degrees two,
is naturally identified with an (undirected) graph $G_{H}=(V,E)$", with `section3.tex:66`: "a factor
$\alpha=\{i,j\}$ is identified with an undirected edge $ij$".

So an edge of a WF graph **is a two-element subset of V**: no loops (a loop would be the subset `{i}`,
of degree 1, hence not a graph edge at all) and no multiple edges (subsets cannot repeat in `F`). A
bouquet with D/2 loops is outside their class on both counts. Three further confirmations that this is
substantive and not pedantry:

1. `cor:IBfornonhyper` is proved by "Plugging these equations into Theorem \ref{thm:Ihara}"
   (`section3.tex:365`), and `thm:Ihara` is stated over hypergraphs with blocks `U_α` indexed by
   `α = {i_1,…,i_{d_α}}` (`section3.tex:218-228, 249-267`) — there is no `U_α` for a loop.
2. `thm:Ihara`'s degree operator is `(\mathcal{D}g)(i):= d_i g(i)` with `d_i = |N_i|` = *number of
   hyperedges containing i*. On a bouquet that is D/2, whereas the correct degree is D. Their framework
   simply has no way to count a loop twice.
3. Their own scalar reduction (`section3.tex:377-397`) — `Z_G(u)^{-1} = (1-u^2)^{|E|-|V|}\det(I - u\mathcal{A}
   + u^2(\mathcal{D}-I))` with `\mathcal{A}_{i,j} = 1` iff `\{i,j\}\in E` — evaluates on a bouquet to
   `(1-u²)^{D/2-1}(1 - u + (D/2-1)u²)`, which is **wrong**; the truth is
   `(1-u²)^{D/2-1}(1 - Du + (D-1)u²)`. Their formulas are only correct on loopless simple graphs.

What *is* true is that the corollary's own displayed expressions, read literally as sums over directed
edges, remain valid on a bouquet — that is the content of (ii) and of the note's Theorem 1. But that is
an **extension of their formula past its stated domain, not an instance of their corollary**.

Caveat in the author's favour, which I cannot settle locally: `section3.tex:374-375` says "A direct
proof of Corollary \ref{cor:IBfornonhyper}, without discussing hypergraphs, is found in the
supplementary material of \citet{WFzeta}" (the NIPS 2009 paper). That supplement is **not in
`refs/src/`**, so I cannot check whether the direct proof covers loops. The claim cannot be repaired by
appeal to a document nobody in this repo has read.

### (iv) Do they require anything of the weights that the note drops?

No — this direction is clean.

* Weight sizes: `u_e ∈ \mat{r_{t(e)}}{r_{o(e)}}` (`section3.tex:309-310`); on one vertex all
  `r_i = N`, so all `u_e ∈ M_N`. The note's `E_i ∈ End(V)` matches.
* Invertibility of the weights themselves: **not assumed** by WF (contrast Matsuura–Ohta, who do
  assume it). The note likewise assumes none. ✔
* Invertibility of `I - u_e u_ē`: WF never state it as a hypothesis, but it is forced — the corollary
  writes `(I_{r_i}-u_eu_{\bar e})^{-1}` and its proof sets `W_{[e]} = U_{[e]}^{-1}` with
  `\det U_{[e]}= \det(I_{r_i}-u_eu_{\bar{e}})` (`section3.tex:344-364`). This is *exactly* the note's
  stated hypothesis, so the note is strictly more careful than the source, not less.
* Structural assumption `r_e := r_{t(e)}` and `u_{e'⇀e} := u^{s(e)}_{t(e')→t(e)}` (`section3.tex:185-193`),
  i.e. the transition weight depends only on the edge entered, not on the edge left — satisfied by the
  note's `T`. ✔

### Conclusion for B

**Holds with the following correction.** The algebraic identification is correct in every detail
(push-through for A, `i ↔ ī` relabelling for D, the pair prefactor, no dropped weight hypothesis), and
I verified the full corollary RHS against `det(1-uT)` numerically on a bouquet. What does **not** hold
is the provenance sentence: a bouquet is not a graph in Watanabe–Fukumizu's sense — their edges are
2-element subsets, their `d_i` counts hyperedges, and their own scalar Ihara–Bass specialisation is
false on a bouquet — so Theorem 1 is *not* the one-vertex case of `cor:IBfornonhyper`; it is the
loop-admitting extension of their formula, which their corollary does not cover. Suggested wording:

> Theorem 1 is the bouquet analogue of Watanabe–Fukumizu's arbitrary-weight corollary
> (`1103.0605:section3.tex:330-341`): their `D̂`, `Â` and edge-pair prefactor specialise, on a
> one-vertex graph and after the push-through identity … and the relabelling `i ↔ ī` in `D`, to
> `D(u)`, `A(u)` and `∏_{\{i,ī\}}det(1-u²E_īE_i)`. Their graphs are hypergraphs all of whose
> hyperedges are 2-element subsets (`section2.tex:17-25`), so loops and multiple edges — i.e. the
> bouquet — are outside the scope of their corollary; the theorem below supplies that case, with a
> direct proof. Their zeta is an Euler product composed in the opposite order (`section3.tex:315`) and
> their edge operator weights the target rather than the source edge; both differences wash out of
> `det(1-u·)` (reversal is a bijection of cyclic non-backtracking words because σ is an involution;
> `det(1-dB) = det(1-Bd)` by Sylvester).

---

## C. Matsuura–Ohta bouquet specialisation — **confirmed**

Read `refs/src/2204.06424/main.tex:271-332` (graph, paths, backtracking, reduced/primitive cycles),
`437-465` (A, deg, D, Ihara), `474-534` (X-weights, `W_X`, eq. 2.10, eq. 2.11, `A_X`), `536-621`
(the Bass-style proof).

* **Loops and multiple edges are allowed.** Their graph is defined purely combinatorially
  (`main.tex:271-292`): edges are elements of a set `E` with `s(e)`, `t(e)`, and
  `E_D = \{e_1,…,e_{n_E},e_1^{-1},…,e_{n_E}^{-1}\}` is a *labelled* 2n_E-element set, so a loop
  `e = \langle v,v\rangle` has an `e^{-1}` distinct from it as an element of `E_D`. Backtracking
  (`main.tex:303`) and tailless/reduced (`309-311`) are defined by edge labels, never by vertices.
  No simplicity or loop-freeness is assumed anywhere. Grep for "loop" in `main.tex` returns only
  *Wilson* loops. This is the decisive difference from Watanabe–Fukumizu.
* **`A_X` for a loop is `X_e + X_e^{-1}`.** Eq. (2.12) `main.tex:523-527`:
  `(A_X)_{vv'} = \sum_{e\in E}(X_e\,\delta_{\langle v,v'\rangle,e} + X_e^{-1}\,\delta_{\langle v',v\rangle,e})`.
  For a loop at `v`, both deltas fire at `v'=v`, giving `X_e + X_e^{-1}`. This is consistent with the
  identity their proof actually uses, `S^T T_X + T^T S_X = A_X` (`main.tex:553`), which on a bouquet
  reads `Σ_e X_e + Σ_e X_e^{-1}`. ✔
* **Degree.** Eq. (2.6) `main.tex:439-440` gives `A_{vv} = 2` per loop, so `deg v = D` for D/2 loops,
  and `(D - \bs{1}_{n_V}) \to (D-1)`; consistent with `S^TS + T^TT = D\otimes\bs{1}_K`
  (`main.tex:554`), which also counts a loop twice. ✔
* **Their Bass proof survives loops.** I checked the four blocks of `ML` (`main.tex:594-609`) entry by
  entry with `s(e)=t(e)` allowed: e.g. the `(E^{-1},E)` block needs
  `-q(J_X+W_X) = -qX_e^{-1}\delta_{s(e),s(e')}` and `q^2 J_XW_X = q^2\delta_{t(e),s(e')}`, both of
  which hold with the labelled-edge conditions `\bse'^{-1}\ne e` of eq. (2.9). Nothing in `L`, `M`,
  `J_X`, or `\det(1-qJ_X) = (1-q^2)^{Kn_E}` uses simplicity.
* **Arithmetic.** `n_V = 1`, `n_E = D/2`, `K = n²`, `deg = D`, `X_i = U_i\otimes U_i^\dagger` invertible
  (required by `main.tex:476` ✔ for unitaries), `A_X = Σ_{i=1}^{D/2}(X_i + X_i^{-1}) = Σ_{i=1}^{D}
  \mathrm{Ad}(U_i) = D\Phi`. Exponent `(n_V-n_E)K = (1-D/2)n^2 = -n^2(D-2)/2` ✔. Inverting eq. (2.11)
  (`\zeta_G = \det(1-qW_X)^{-1}`, eq. 2.8) gives
  `\det(1-qW_X) = (1-q^2)^{n^2(D-2)/2}\det(1 - qD\Phi + (D-1)q^2)` ✔ — exactly claim 1 / `HANDOFF.md`
  item 1 / Corollary 3 of the theorem note.
* Numerically verified end to end for a bouquet with D=6 Haar unitaries, n=3: rel. err ≤ 1.3e-15.

Two small notational snags, neither affecting the verdict: (1) prior-art writes
`A_X = \sum_i U_i\otimes\bar U_i`, which conflicts with the theorem note's own stated convention
`\mathrm{Ad}(A) = \bar A\otimes A` (`quantum-ihara-general.md:19`) and with MO's own
`\rho_{\rm adj}(U_e) = U_e\otimes U_e^\dag`; pick one vectorisation convention repo-wide. (2) The
phrase "exponent `(n_V − n_E)K = −n²(D−2)/2` … This is claim 1 verbatim" elides the inversion
`\zeta^{-1} = \det(1-qW_X)`, which flips the sign of the exponent; "verbatim" is doing work it has not
earned, but the identification is correct.

**mo-specialisation: confirmed.**

---

## D. Stark–Terras: "the representation is of the finite Galois group"

Local bytes only (`2309.15873/AiM_Final.tex`, `2405.04361/v3.tex`; Stark–Terras itself is not in
`refs/src/`).

* "**of the Galois group of a covering**" — **supported**. `AiM_Final.tex:131` (the quoted line):
  "in \cite{stark2000zeta}, Stark and Terras further introduced notions of *Galois coverings* and
  *Artin-Ihara L-functions* for graphs … for a Galois covering $\pi:Y \to X$ of graphs with the Galois
  group $G$, the Ihara zeta function … is obtained by evaluating the Artin-Ihara L-function of the
  covering $\pi$ at the trivial representation (resp. the right regular representation)". Their own
  definition, attributed to Stark–Terras at `AiM_Final.tex:298-300`, is `AiM_Final.tex:291`: "Let $G$
  be the Galois group of $\pi$ and let $\rho$ be a representation of $G$". `v3.tex:396` likewise:
  "Let $Y/X$ be a Galois cover with abelian Galois group $G:=\op{Gal}(Y/X)$ … Given a character
  $\psi\in\widehat G$".
* "**finite**" — **not stated anywhere in the local bytes**; it is an inference, though a safe one.
  `AiM_Final.tex:203` ("all graphs are assumed to be undirected and finite") plus a *free* `G`-action
  on a finite graph forces `|G| < ∞`; `v3.tex:470` says "Let $\cG$ be a finite group, a *voltage*
  assignment …", and `v3.tex:315-317` fixes `X` a finite multigraph. But neither source writes "finite
  Galois group", and the definitions at `AiM_Final.tex:291` and `:1090` say only "Let $G$ be a group".
  The right-regular-representation statement at `:131` and the `\widehat G` factorisation at `:1291`
  presuppose finiteness without asserting it.

Verdict: the sentence is **defensible but over-attributed to the local bytes**. Either drop "finite"
or attach the inference explicitly ("the covering group of a finite graph is finite,
`2309.15873:AiM_Final.tex:203`, `2405.04361:v3.tex:470`"). The downstream conclusion — that
`Ad(U_i)` for generic unitaries generates an infinite group so the notebook's object is not literally
a Stark–Terras L-function — stands, and is reinforced by `v3.tex:262,295` (Cayley graphs *are* Galois
covers of bouquets, for finite groups), and by Matsuura–Ohta 2026 `main.tex:470`, "While the above
discussion assumes $G$ to be a finite group, the same procedure can be extended to the case where $G$
is the compact Lie group $U(N_c)$" — which, incidentally, refutes the prior-art gloss at line 50 that
2607.27935 gives the L-function "for a representation $R$ of **any** group".

---

## E. `scripts/qihara_general.py` vs `outputs/qihara_general.txt` vs Theorem 1

* **Output reproduces exactly.** `python3 scripts/qihara_general.py` re-run today: byte-identical to
  `outputs/qihara_general.txt` (`diff` empty, exit 0). The RNG is seeded (`default_rng(7)`), so this is
  deterministic.
* **§5's summary of the numbers is accurate.** "relative errors ≤ 3·10⁻¹⁵": worst printed float error
  is 2.8e-15 ✔. "trace formula of Corollary 2 for ℓ≤4 to 6·10⁻¹²": printed 5.5e-12 ✔. "exact
  rational-arithmetic verification … for (N,D) = (1,4), (2,4), (2,6)": three `True`s ✔. Case labels
  (b), (b′), (d), (a) match the code ✔.
* **What the script actually tests is Theorem 1 in the `⟨1⟩6` form, not the displayed form.** `rhs()`
  computes `∏ det(1-u²E_īE_i) · det(1 - u·M(u))` with
  `M(u) = Σ_i (E_i - uE_īE_i)(1-u²E_īE_i)^{-1}`, i.e. step ⟨1⟩6; the statement of Theorem 1 is in terms
  of `1 + D(u) - A(u)`. The two are identical by ⟨1⟩7 (one line of linearity), so this is not an error,
  but strictly the *displayed* identity is never evaluated. A two-line addition evaluating
  `det(1 + D(u) - A(u))` directly would close the gap.
* **Corollary 2's trace formula is tested in the `Tr_V(E_{i_ℓ}…E_{i_1})` form**, not the
  `|Tr(A_{i_ℓ}…A_{i_1})|²` form; the product order in `trace_formula` (`P = Es[i] @ P`) is
  `E_{i_m}···E_{i_1}` ✔ matching the note, and the cyclic non-backtracking mask is correct ✔. The
  positivity claim of Corollary 2 is not exercised numerically.
* **Docstring/labelling drift.** The docstring says "(c) trace formula Tr T^m = …" but the code's `(c)`
  is "D=2 single Kraus pair" and the trace formula is printed under `(b)`; case `(d)` is in the code
  and not in the docstring. Also §5 says "Theorem 1 at three complex $u$" — `us=(0.13, 0.21+0.09j,
  -0.17)` is two real and one genuinely complex; and §5 omits case (c) (D=2) entirely, although it is
  run and passes. (The earlier review `theorem1-algebra-2026-09-12.md` recommended adding a D=2 line;
  it is now there.)
* Cosmetic: `w5` is assigned twice (lines 72, 74) — harmless, it takes a max; `pref` multiplies over a
  `set`, so iteration order is nondeterministic but the product is commutative.

---

## Issues and fixes

| # | sev | where | issue | fix |
|---|---|---|---|---|
| 1 | **MAJOR** | `quantum-ihara-general.md:5` (status banner), `:109`; `prior-art:20, 26, 64` | "Theorem 1 is the one-vertex (bouquet) case of Watanabe–Fukumizu's corollary" / "SPECIAL CASE of this corollary". False under their conventions: WF edges are 2-element subsets of V (`1103.0605:section2.tex:17-25`), `d_i` counts hyperedges, and their own scalar Ihara–Bass (`section3.tex:377-397`) is wrong on a bouquet. A bouquet is not a WF graph | Reword to "the bouquet analogue / the loop-admitting extension of their arbitrary-weight formula, which they state only for graphs without loops or multiple edges". Draft wording in §B above. Do **not** let this stand as a priority concession: for arbitrary (non-invertible) weights *on a bouquet*, no local source covers the case |
| 2 | **MAJOR** | `prior-art:124, 125` | `2204.06424:main.tex:3068` and `:3095-3096` point past EOF (file is 2342 lines) | `main.bbl:30` / `refs.bib:1067` (Sunada), `main.bbl:94,100` / `refs.bib:1076,1085` (Hashimoto); body citations at `main.tex:191,329` and `:393,424`. "ref [6]" is correct |
| 3 | **MAJOR** | `prior-art:70-73, 75, 79, 85-86, 117, 118` (11 citations, 6 papers) | Cited file does not exist under `refs/src/`: `1801.00876` → `tenseur9.tex`, `2304.05714` → `PT-RC_reloaded.tex`, `0706.0556` → `sd10.tex`, `0709.1142` → `main.tex` (not `expand.tex`), `2309.15873` → `AiM_Final.tex`, `2405.04361` → `v3.tex`. Line numbers and text are all correct | Rewrite the filenames. `refs/README.md` promises re-checkability against these paths; as written, 11 citations do not resolve |
| 4 | MINOR | `prior-art:35` | eq. 2.8 quote is at `main.tex:479-482`, cited `480-485` (range excludes `\zeta_G(q;X) \equiv`) | cite `479-482` |
| 5 | MINOR | `prior-art:37` | eq. 2.10 quote is at `main.tex:503-505`, cited `505-510` | cite `503-505` |
| 6 | MINOR | `quantum-ihara-general.md:109` | The identification silently uses two further steps: WF compose prime cycles in the opposite order (`section3.tex:315`), and their edge operator weights the target edge while `T` weights the source | Add the reversal-bijection / Sylvester sentence (§B(i)) |
| 7 | MINOR | `prior-art:50` | "(Artin–Ihara $L$-function for a representation $R$ of **any** group …)" — `2607.27935:main.tex:470`: "the above discussion assumes $G$ to be a finite group, the same procedure can be extended to … $U(N_c)$" | "for a finite group, extended to $U(N_c)$" — which is *better* for claim 3, since `ρ_adj` of `U(N_c)` is precisely the notebook's object |
| 8 | MINOR | `prior-art:120` | "In Stark–Terras the representation is of the **finite** Galois group" — "finite" appears nowhere in the local secondary sources; it follows only from graph finiteness | Attach the inference, citing `2309.15873:AiM_Final.tex:203` and `2405.04361:v3.tex:470` |
| 9 | MINOR | `prior-art:42` | `A_X = \sum_i U_i\otimes\bar U_i` contradicts the theorem note's own `Ad(A) = \bar A\otimes A` and MO's `U_e\otimes U_e^\dag` | Fix the vectorisation convention repo-wide |
| 10 | MINOR | `prior-art:42` | "This is claim 1 **verbatim**" skips the inversion `\zeta_G^{-1} = \det(1-qW_X)` that flips the exponent's sign | say "after inverting eq. (2.8)" |
| 11 | MINOR | `scripts/qihara_general.py:1-16` vs code | Docstring labels `(c)` = trace formula; code `(c)` = the D=2 pair; case `(d)` undocumented. Displayed form `1+D(u)-A(u)` never evaluated (only the equivalent `1-uM(u)`) | Sync labels; add a direct `det(1+D-A)` evaluation |
| 12 | MINOR | `quantum-ihara-general.md:111` | "at three complex $u$" (two are real); case (c), D=2, is run and passes but is not mentioned | reword; mention (c) |
| 13 | MINOR | `quantum-ihara-general.md:109` | "Corollary `IBfornonhyper`" — the label is `cor:IBfornonhyper` | add the prefix |

Not an issue, recorded for the author: `1103.0605:section3.tex:374-375` points to a direct,
hypergraph-free proof of the corollary in the NIPS 2009 supplementary material. That file is **not in
`refs/src/`**, so it cannot be used to rescue issue 1 without fetching it; it is the one document that
could plausibly extend their corollary to loops.

---

VERDICT provenance-quotes: INVALID

*(No quoted string is misquoted, distorted or fabricated — all 39 rows are verbatim. But 15 of 39
citation addresses do not resolve as written: 11 name a nonexistent file, 2 point past EOF, 2 ranges
exclude the quote they label. Under `<id>:<file>:<line>` the address is part of the claim.)*

VERDICT wf-equivalence: INVALID

*(Holds with the correction in §B: the algebra matches exactly — push-through for A, `i↔ī` relabelling
for D, prefactor, weight hypotheses — and I verified the full corollary RHS numerically on a bouquet.
But a bouquet is not a graph in Watanabe–Fukumizu's sense, so Theorem 1 is the loop-admitting extension
of their formula, not the one-vertex case of their corollary.)*

VERDICT mo-specialisation: VALID

RESULT: INVALID — the mathematics and every quoted string check out, but the Watanabe–Fukumizu
priority claim overreaches their loop-free conventions and 15 citation addresses do not resolve.

Files written: `notes/reviews/provenance-2026-09-12.md`, `notes/reviews/scratch_wf_mo_conventions.py`
