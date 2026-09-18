# Literature lane: classical antecedents for an Ihara/Toeplitz analogue of `zst/`

Written 2026-09-18. Task: for the planned "Ihara zeta spectral triple" (group `Z`, window
`{-M..M}`, Weil form = rescaled-cycle-count Toeplitz matrix, minimal eigenvector, rank-one
perturbation of the shift), find and verify the primary classical/CCM references this
construction should reduce to. Organised A-F as assigned. Every item gives: full citation,
DOI (where one exists), arXiv id (if any), the precise statement, and whether TeX source is
on arXiv. Quotes are copied byte-for-byte from the source named; anything not checked against
primary text is flagged `UNVERIFIED`, anything reworded from a secondary source is flagged
`PARAPHRASE`.

**Method note.** `refs/src/2511.22755/mc2arXiv.tex` (already in this repo's fetch cache) was
read for the CCM bibliography and cross-checked line-by-line. Three more arXiv TeX sources were
fetched **to this session's scratchpad** (not to `refs/src/`, since this lane is not authorised
to write outside `notes/zeta-spectral-triples/ihara/lanes/`) and quoted from directly:
`2511.23257` (Connes-van Suijlekom), `2106.01715` (Connes-Consani), `math/0606037` (Simon). Two
Stark-Terras-school papers with no arXiv id were retrieved as author-hosted PDFs via the Wayback
Machine (the live `mathweb.ucsd.edu` was returning 503 all session) and read verbatim; the exact
archived URLs are given so the quotes are re-checkable. Everything else pre-dates arXiv and is
cited from its journal record plus, where found, a secondary paper that quotes its theorem
statement.

---

## A. Ihara zeta and explicit-formula / RH-for-graphs literature

### A1. Y. Ihara, "On discrete subgroups of the two by two projective linear group over
𝔭-adic fields", *J. Math. Soc. Japan* **18** (1966), 219–235.

- No DOI on the original (pre-DOI journal); Project Euclid record:
  <https://projecteuclid.org/euclid.jmsj/1260541107>. No arXiv (1966).
- Statement (**PARAPHRASE**, via Terras-Wallace, see A7 below, ref. [12]/text): introduces the
  zeta function of a discrete subgroup of `PGL(2, Q_p)` acting on the Bruhat-Tits tree; this is
  the origin of "Ihara zeta" for the graph = quotient tree/subgroup. Not independently read in
  full; every later source (Hashimoto, Bass, Stark-Terras) attributes the founding definition to
  this paper and none of them quote a specific theorem number from it verbatim, so I mark the
  precise original statement `UNVERIFIED`.
- TeX on arXiv: **no** (pre-arXiv).

### A2. K. Hashimoto, "Zeta functions of finite graphs and representations of p-adic groups",
in *Automorphic Forms and Geometry of Algebraic Varieties* (K. Hashimoto, Y. Namikawa, eds.),
Adv. Stud. Pure Math. **15**, Academic Press, 1989, pp. 211–280.

- No DOI (conference-proceedings volume); no arXiv.
- Content (**PARAPHRASE**, cross-checked against two independent bibliographies that both cite
  the same pages): proves the edge-adjacency-operator ("Hashimoto operator" / non-backtracking
  operator) three-term determinant identity for the Ihara zeta function of an irregular graph,
  and treats the biregular-bipartite case (used by Horton-Stark-Terras, A6 below, at their
  ref. [1], pp. 230, 260, 270, for the biregular Ihara-zeta formula — this citation to specific
  page numbers **is** byte-verified, see A6 quote below).
- TeX on arXiv: **no**.

### A3. H. Bass, "The Ihara-Selberg zeta function of a tree lattice", *Internat. J. Math.*
**3** (1992), no. 6, 717–797. DOI: 10.1142/S0129167X92000357 (Ihara-Bass three-term formula).

- No arXiv (1992, pre-arXiv).
- Statement (**PARAPHRASE**, confirmed by every downstream source, e.g. A6 §2, eq. (2.3),
  verbatim below): proves, for an arbitrary (possibly irregular) finite graph `X` with adjacency
  matrix `A_X` and `Q_X = diag(deg(v)-1)`,
  `ζ(u,X)^{-1} = (1-u^2)^{r_X - 1} det(I - A_X u + Q_X u^2)`, `r_X` = rank of `π_1(X)`.
  This is the "Ihara-Bass formula" the CCM-analogue's `(1-u^2)^{|E|-|V|}` factor generalises.
- TeX on arXiv: **no**.

### A4. M. Kotani and T. Sunada, "Zeta functions of finite graphs", *J. Math. Sci. Univ. Tokyo*
**7** (2000), no. 1, 7–25.

- No DOI listed by the journal (J. Math. Sci. Univ. Tokyo, pre-DOI era); no arXiv.
- Statement — **VERIFIED VERBATIM** via Horton-Stark-Terras (A6), which quotes it directly:

  > "Kotani and Sunada [18] show that, for a non-circuit graph X, if q + 1 is the maximum
  > degree of X and p + 1 is the minimum degree of X, then every non-real pole u of ζX(u)
  > satisfies the inequality (2.5) `q^{-1/2} ≤ |u| ≤ p^{-1/2}`." — Horton-Stark-Terras
  > `snowbird.pdf`, p. 3-4 (§2, around eq. (2.5)).

  and further, every pole satisfies `R_X ≤ |u| ≤ 1` with `q^{-1} ≤ R_X ≤ p^{-1}` (ibid., p. 5,
  eq. (2.6)). This is the graph analogue of the strip in which the nontrivial zeros of a
  Dedekind/Hecke L-function must lie; it is the un-conditional half of the "graph RH."
- TeX on arXiv: **no**.

### A5. H. M. Stark and A. A. Terras, "Zeta functions of finite graphs and coverings",
*Adv. Math.* **121** (1996), 124–165. DOI: 10.1006/aima.1996.0050.

*Part II:* Stark-Terras, "Zeta functions of finite graphs and coverings, II", *Adv. Math.*
**154** (2000), no. 1, 132–195. DOI: 10.1006/aima.2000.1917.

*Part III:* Stark-Terras, "Zeta functions of finite graphs and coverings, III", *Adv. Math.*
**208** (2007), no. 2, 467–489. DOI: 10.1016/j.aim.2006.03.002.

- No arXiv for any of the three (1996/2000/2007, all pre- or non-arXiv-deposited).
- Part III is the "Brauer-Siegel for graphs" paper; its introduction and Theorem 3 (Siegel
  poles) are **VERIFIED VERBATIM** by direct PDF read of the author's own preprint copy
  (Wayback Machine capture of `mathweb.ucsd.edu/~aterras/graphbrauersiegel.pdf`, archived
  2024-04-15, `https://web.archive.org/web/20240415004428/https://mathweb.ucsd.edu/~aterras/graphbrauersiegel.pdf`):
  it contains the Ihara determinant formula (their eq., identical to Bass's), the Kotani-Sunada
  inequality restated, and:

  > "The Riemann hypothesis for a regular graph X refers to the location of the poles of ζX(u).
  > If X is (q + 1)-regular, there are poles on the circles |u| = 1/q and |u| = 1 and all other
  > poles are between these two circles. The Riemann hypothesis then demands that all further
  > poles have |u| = 1/√q." — `graphbrauersiegel.pdf`, p. 4.

  and, for irregular graphs:

  > "we could put forward a Riemann hypothesis which says that there are no poles of ζX(u)
  > strictly between the circles |u| = RX and |u| = √RX. ... A milder request ... We could call
  > this a 'weak Riemann hypothesis.'" — ibid., p. 4.

  Also gives worked examples where the (strong) RH is true and false for irregular graphs
  (`K_n - e`, `K_{m,n}`, the "e-graph"), and one infinite family of irregular graphs satisfying
  it (edge-subdivided Ramanujan graphs).
- TeX on arXiv: **no** for I/II/III. Best accessible copy: author-hosted preprints, archived
  (see TO FETCH-alternative list below); Part II is not separately archived in this session,
  only cited secondhand (via A6/A7's bibliography and via Eyler-Jun / Ghosh-Ray, already
  byte-verified in `notes/prior-art-quantum-ihara.md` lines 119–122).

### A6. M. D. Horton, H. M. Stark, A. A. Terras, "What are zeta functions of graphs and what
are they good for?", in *Quantum Graphs and Their Applications* (G. Berkolaiko, R. Carlson,
S. A. Fulling, P. Kuchment, eds.), Contemp. Math. **415**, AMS, 2006, pp. 173–190.
DOI: 10.1090/conm/415/07868.

- No arXiv. **VERIFIED VERBATIM** by direct PDF read of the author's preprint (Wayback capture,
  archived 2024-01-23,
  `https://web.archive.org/web/20240123040609/https://mathweb.ucsd.edu/~aterras/snowbird.pdf`).
- This is the single most useful source for item A. It states, and I quote:
  - The **irregular-graph RH**, in two forms (this is exactly what the task asked to locate):

    > "(Graph theory RH) ζX(u) is pole free for (2.10) RX < |u| < √RX,
    > (Weak graph theory RH) ζX(u) is pole free for (2.11) RX < |u| < 1/√q."
    — p. 6, immediately following the definition of `R_X` as "the radius of the largest circle
    of convergence of the Ihara zeta function" (Def. 2.1, p. 3) and the remark that "the natural
    change of variable is `u = R_X^s`... All poles of ζX(u) are then located in the 'critical
    strip', 0 ≤ Re(s) ≤ 1" (p. 5-6). So the task's phrase "poles on `|u| = R^{1/2}`" is exactly
    the boundary case of pole-freeness (2.10): a pole *on* `|u| = √R_X` is the graph-RH failure
    mode, and RH holding is equivalent to no poles strictly between `R_X` and `√R_X`.
  - The **Ihara-Bass determinant formula** for irregular graphs, eq. (2.3), p. 3 (matches A3).
  - **The `(1-u^2)^{r_X-1}` "gamma factor" claim** (task item A, last sentence): I searched this
    paper, `graphbrauersiegel.pdf` (A5/III) and `treetrace.pdf` (A7/F) in full for the words
    "gamma factor" / "archimedean factor" applied to `(1-u^2)^{...}` and found **no such
    statement in any of the three**. The `(1-u^2)^{r_X-1}` factor is discussed only as the
    trivial-loop/spanning-tree correction coming from the identity block `J` in Bass's proof
    (Horton-Stark-Terras §3, Bass's Proof, p. 14, eq. `det(I+Ju) = (1-u^2)^m`). **Mark this
    specific "gamma factor" framing UNVERIFIED** — it may be this notebook's own reading (by
    analogy with Weil's archimedean factor `π^{-s/2}Γ(s/2)` being the "extra" factor beyond the
    Euler product) rather than a claim made in the Stark-Terras-Horton literature itself.
  - No Weil-style explicit formula with test functions appears in any of the three PDFs read;
    Horton-Stark-Terras only give the *prime number theorem for graphs* (their Theorem 2.10,
    via Möbius inversion of `N_m = Σ_{d|m} d·π(d)`, p. 9-10) — a Chebyshev/PNT-style result, not
    a Weil explicit formula. **Mark "explicit formula in Weil's form for graphs" UNVERIFIED /
    NOT FOUND** in the primary sources read this session.

### A7. A. Terras, *Zeta Functions of Graphs: A Stroll through the Garden*, Cambridge Studies
in Advanced Mathematics 128, Cambridge University Press, 2011. ISBN 978-0-521-11367-0.

- No DOI (book); no arXiv. Publisher page: <https://www.cambridge.org/9780521113670>.
- Not read directly this session (no accessible full text found; Google Books preview only
  shows front matter). Table of contents (from publisher/AMS review,
  `https://www.ams.org/bull/2014-51-01/S0273-0979-2013-01426-5/S0273-0979-2013-01426-5.pdf`,
  itself a **PARAPHRASE** source) confirms Part II is "Ihara's Zeta Function and the Graph
  Theory Prime Number Theorem," i.e. the book's organizing theorem is the PNT-for-graphs, not a
  Weil explicit formula. `Terras:2011, Theorem 18.15` is cited elsewhere in the literature
  (already byte-verified in `notes/prior-art-quantum-ihara.md:120`, quoting
  `2405.04361:v3.tex:427`) as "the three-term determinant formula" — i.e. the Ihara-Bass formula
  again, not an explicit formula. **No "Weil positivity" / "explicit-formula test of RH" content
  located for this book; mark UNVERIFIED** (could not obtain the book's actual text this
  session — this is the single largest verification gap in item A and should be closed by
  actually reading a library copy or the relevant chapter before citing it for anything beyond
  the determinant formula).
- Closest companion source instead: **G. Ahumada / Terras-Wallace's Selberg trace formula for
  the k-regular tree** — see F1 below, which supplies a genuine trace-formula (Selberg-style,
  not Weil-explicit-formula-style) derivation of the Ihara-Bass identity, fully verified.

### A8. Companion finding (not in the task list, but directly load-bearing): E. Hallouin and
M. Perret, "A unified viewpoint for upper bounds for the number of points of curves over finite
fields via Euclidean geometry and semi-definite symmetric Toeplitz matrices", *Trans. Amer.
Math. Soc.* **372** (2019), no. 8, 5409–5451. DOI: 10.1090/tran/7568.

- No arXiv. **VERIFIED**: this is `[HP]` in the Connes-van Suijlekom paper `2511.23257`
  (item E2 below), cited exactly where the CS paper's Corollary `corcar` (positive
  semi-definite rank-`n` Toeplitz matrix ⇒ kernel-vector's polynomial has all zeros on the unit
  circle) is first stated:

  > "This corollary exhibits a striking number-theoretic flavor, resonating with the analogue
  > of the Riemann Hypothesis for function fields; see~\cite{HP} for a further discussion of
  > this connection." — `Araki-final-oct25.tex:800` (arXiv:2511.23257).

  Hallouin-Perret's own abstract (**PARAPHRASE**, via WebSearch secondary summary): recovers
  Weil's and Y. Ihara's classical *point-count* bounds for curves over finite fields as the
  first two steps of an SDP hierarchy built from symmetric Toeplitz matrices of moments — this
  is the **curve-RH-bound "Ihara"** (Y. Ihara's 1981 bound on `#X(F_q)`), a different object
  from the graph Ihara zeta of item A, but the same author and the same "Toeplitz positivity ⇒
  bound related to RH" mechanism the Ihara-graph analogue in this lane wants. **Do not conflate**
  the two "Ihara"s in the write-up — flag explicitly if cited.
- TeX on arXiv: **no** (TAMS-only). Not yet fetched to `refs/src/`; not urgently needed since
  it is not literally about graphs, but worth reading in full before building the finite-graph
  analogue, since it is the closest existing "CCM-style Toeplitz-positivity meets a genuine RH
  bound" precedent.

---

## B. Toeplitz / classical signal-processing literature

### B1. C. Carathéodory and L. Fejér, "Über den Zusammenhang der Extreme von Harmonischen
Funktionen mit ihren Koeffizienten und über den Picard-Landauschen Satz", *Rend. Circ. Mat.
Palermo* **32** (1911), 218–239.

- No DOI (1911); no arXiv.
- **VERIFIED as the exact reference CCM's own papers use** — appears verbatim in the
  bibliography of both zeta-spectral-triple papers:
  `refs/src/2511.22755/mc2arXiv.tex:1466` — `\bibitem{CF11} C. Carathéodory und L. Fejér, {\em
  über den Zusammenhang der Extreme von Harmonischen Funktionen mit ihren Koeffizienten und
  über den Picard-Landauschen Satz}. Rend. Circ. Mat. Palermo 32 (1911)218-239.` — and again,
  identically, in `2511.23257` (`Araki-final-oct25.tex:2066`).
- Statement (**PARAPHRASE**, standard): the Carathéodory-Fejér / Carathéodory-Toeplitz theorem —
  a Hermitian Toeplitz matrix (equivalently a truncated trigonometric-moment sequence) is
  positive semidefinite iff it is the moment matrix of a positive measure on the unit circle
  supported on at most `n` points (`n` = matrix size). The Connes-van Suijlekom Corollary
  `corcar` (item E2) is the direct corollary used by this lane; see there for the exact
  statement and its **byte-verified** $C^*$-algebraic proof.
- TeX on arXiv: **no**. Best alternative: Connes-van Suijlekom `2511.23257`, §2 ("Toeplitz
  case"), reproves and restates it in full (fetched, quoted in E2).

### B2. V. F. Pisarenko, "The retrieval of harmonics from a covariance function", *Geophys. J.
R. Astr. Soc.* **33** (1973), no. 3, 347–366. DOI: 10.1111/j.1365-246X.1973.tb03424.x.

- No arXiv (1973).
- Statement (**PARAPHRASE**, via WebSearch summary of the paper and Wikipedia's "Pisarenko
  harmonic decomposition" article, not independently read): the frequencies of a sum of complex
  sinusoids in white noise are recovered from the phase of the eigenvector of the
  sample-covariance (Hermitian Toeplitz) matrix belonging to its *minimum* eigenvalue; this is
  presented as a rediscovery of the underlying Carathéodory trigonometric-moment-problem fact
  (B1). This is the closest classical analogue of the CCM/`zst` "minimal eigenvector of the
  Weil form" step, specialised to a *known* number of exact sinusoids plus noise (here: rescaled
  cycle counts of a graph in place of a sampled covariance).
- TeX on arXiv: **no**. Best alternative: Oxford Academic (paywalled, but abstract/summary
  accessible): <https://academic.oup.com/gji/article/33/3/347/610926>.

### B3. J. Makhoul, "On the eigenvectors of symmetric Toeplitz matrices", *IEEE Trans. Acoust.,
Speech, Signal Process.* **ASSP-29** (1981), no. 4, 868–872. DOI: 10.1109/TASSP.1981.1163635.

- No arXiv (1981).
- Statement — **PARAPHRASE**, from the IEEE Xplore abstract (not the full text; full text is
  paywalled and was not obtained this session):

  > "the eigenfilters corresponding to the maximum and minimum eigenvalues, if distinct, have
  > their zeros on the unit circle, while the zeros of the other eigenfilters may or may not
  > have their zeros on the unit circle."

  I.e. the precise hypothesis is: symmetric (not necessarily positive-definite) Toeplitz matrix;
  the theorem is stated for the *extreme* (max **and** min) eigenvalue, and requires that
  eigenvalue to be **simple** ("if distinct"); intermediate eigenvectors need not have their
  zeros on the circle. This is a real-symmetric-Toeplitz statement, subtly different from the
  Hermitian positive-semidefinite-rank-deficient hypothesis of Carathéodory-Fejér/B1 (there the
  hypothesis is rank-`n` PSD and the conclusion is about `ker T`, the zero eigenvalue, which is
  automatically the *minimum*). **Note for the design lane:** the finite-graph Weil form is real
  symmetric (Toeplitz, real cycle counts), so Makhoul's theorem is the more directly-applicable
  of the two, but its "if distinct" clause needs checking against the actual small-window Weil
  matrices before use, exactly as `zst/README.md`/`plan.md` already flag for the CCM continuous
  case ("simple-even" condition).
- TeX on arXiv: **no**. Full text not obtained this session (IEEE Xplore paywall); mark the
  precise quoted hypotheses above as `UNVERIFIED` pending primary-text access — the abstract
  wording above is itself already a secondary paraphrase surfaced by WebSearch, not lifted from
  the paper's own abstract text with certainty.

### B4. P. Delsarte, Y. Genin, Y. Kamp, several papers, notably "Orthogonal polynomial matrices
on the unit circle", *IEEE Trans. Circuits Syst.* **25** (1978), no. 3, 149–160 (matrix OPUC),
and later joint work (with others) specifically "On the role of the Nevanlinna-Pick problem in
circuit and system theory" / papers on Toeplitz eigenvector zero-counting cited by Makhoul (B3)
and by Simon's OPUC book (C1).

- No arXiv for any Delsarte-Genin-Kamp paper (1970s-80s).
- Statement: **UNVERIFIED** — I could not locate and read a specific Delsarte-Genin-Kamp paper
  giving the "number of zeros on the unit circle of eigenpolynomials of Hermitian Toeplitz
  matrices" result the task asks about; WebSearch surfaced only secondary descriptions (e.g. a
  Springer chapter, "On the Role of Orthogonal Polynomials on the Unit Circle in Digital Signal
  Processing Applications," and a MathSciNet-style summary) attributing to them "generalized
  Carathéodory representations" and eigenpolynomial zero-counting, consistent with but not
  identical to Makhoul's theorem. Recommend, before relying on this attribution, pulling the
  exact Delsarte-Genin-Kamp reference list from Simon's OPUC book (C1) footnotes, which is the
  standard modern pointer to this literature.
- TeX on arXiv: **no**.

### B5. A. Cantoni and P. Butler, "Eigenvalues and eigenvectors of symmetric centrosymmetric
matrices", *Linear Algebra Appl.* **13** (1976), no. 3, 275–288.
DOI: 10.1016/0024-3795(76)90101-4.

- No arXiv (1976).
- Statement — **PARAPHRASE**, from the ScienceDirect/UWA-repository abstract (full text not
  obtained):

  > "the eigenvectors of a symmetric centrosymmetric matrix of order N are either symmetric or
  > skew symmetric, and that there are ⌈N/2⌉ symmetric and ⌊N/2⌋ skew symmetric eigenvectors...
  > for tridiagonal matrices of both odd and even order... the eigenvectors corresponding to the
  > eigenvalues arranged in descending order are alternately symmetric and skew symmetric
  > provided the eigenvalues are distinct."

  A symmetric Toeplitz matrix is centrosymmetric (invariant under the flip-and-transpose `J`),
  so this is exactly the even/odd (palindromic/anti-palindromic) splitting the CCM paper itself
  uses for the continuous case (`2511.23257`, `Araki-final-oct25.tex:865`, quoted in E2 below:
  "$P(X)$ is either palendromic, or anti-palendromic ... $a_{n-j} = \pm a_j$") and that
  `zst/plan.md` calls the parity of `xi`. Cantoni-Butler is the finite-matrix, purely
  linear-algebraic source for that fact, older than and independent of the CF/OPUC route.
- TeX on arXiv: **no**. Full text not obtained.

### B6. R. O. Schmidt, "Multiple emitter location and signal parameter estimation", *IEEE
Trans. Antennas Propag.* **34** (1986), no. 3, 276–280. DOI: 10.1109/TAP.1986.1143830.

- No arXiv (1986). Context only, as the task requested: MUSIC generalises Pisarenko's (B2)
  minimum-eigenvector-of-covariance-Toeplitz-matrix idea to multiple sensors/emitters; not
  itself a Toeplitz-zero-locus theorem, so not further pursued for this lane's core claims.
  Not independently read; bibliographic data above from IEEE record (WebSearch).
- TeX on arXiv: **no**.

---

## C. Orthogonal polynomials on the unit circle (OPUC) / CMV matrices

### C1. B. Simon, *Orthogonal Polynomials on the Unit Circle*, Parts 1 & 2, AMS Colloquium
Publications 54, American Mathematical Society, 2005. ISBN 978-0-8218-3446-6 (Part 1),
978-0-8218-3675-0 (Part 2).

- No DOI (book); no arXiv.
- The specific theorem number for "paraorthogonal polynomials have all zeros on the unit
  circle" was **not independently confirmed this session** (no full-text access to the book);
  standard OPUC folklore attributes it to Simon's Part 1, roughly the chapter on the
  Christoffel-Darboux formula / "The CMV matrix," but I could not pin a Theorem number without
  the book in hand. **Mark UNVERIFIED.** The *content* of the theorem, however, is
  independently and completely verified via Simon's own later paper C2, which restates and
  reproves it using rank-one unitary perturbations (see below) — this is arguably the more
  directly useful source for the finite-window analogue anyway, since it works matrix-first.
- TeX on arXiv: **no** for the book.

### C2. B. Simon, "Rank one perturbations and the zeros of paraorthogonal polynomials on the
unit circle", *J. Math. Anal. Appl.* **329** (2007), no. 1, 376–382.
DOI: 10.1016/j.jmaa.2006.06.081. **arXiv:math/0606037**.

- **VERIFIED VERBATIM**, fetched and read in full this session
  (`arxiv.org/e-print/math/0606037`, file `main.tex`; title/author at lines 155/158):

  > "\title[Rank One Perturbations and the Zeros of POPUC] \author[B. Simon]{Barry Simon*}" —
  > `main.tex:155,158`.
  > Abstract: "We prove several results about zeros of paraorthogonal polynomials using the
  > theory of rank one perturbations of unitary operators." — `main.tex:169-170`.
  > "Given β∈∂𝔻, the paraorthogonal polynomials (POPUC) are..." — `main.tex:194`.
  > "The key to our proofs is the connection of Φ̃_n to CMV matrices [CMV, OPUC1, Evansproc].
  > Φ̃_n is the determinant of a suitable finite CMV matrix, and so its zeros are the
  > eigenvalues. All our results concern what happens to eigenvalues of unitary matrices under
  > rank one perturbations." — `main.tex:294-298`.
  > "It is a fundamental result of Cantero, Moral, and Velázquez [CMV] that ..." —
  > `main.tex:456`.
  > "In particular, the zeros of Φ̃_n are the eigenvalues of a finite CMV matrix." —
  > `main.tex:485`.

  This is **exactly** the fact the task asked for: the rank-one-perturbed truncated CMV matrix
  is unitary, its characteristic polynomial is a paraorthogonal polynomial, and the POPUC's
  zeros (on the unit circle by C1/C3) are the eigenvalues of that perturbed unitary — the
  literal unit-circle analogue of CCM's rank-one-perturbed self-adjoint scaling operator `D'`
  whose real spectrum is the zero set of `ξ̂`.
- TeX on arXiv: **yes** — `math/0606037`.

### C3. M. J. Cantero, L. Moral, L. Velázquez, "Five-diagonal matrices and zeros of orthogonal
polynomials on the unit circle", *Linear Algebra Appl.* **362** (2003), 29–56.
DOI: 10.1016/S0024-3795(02)00457-3. **arXiv:math/0204300**.

- **arXiv id confirmed**: fetched successfully to scratchpad this session
  (`arxiv.org/e-print/math/0204300` → `main.tex`, 82 KB), not yet content-verified line-by-line
  (time-boxed this session to the CMV-via-Simon route, C2, which already quotes and uses it);
  fetched file exists and is ready for the next lane session to quote directly.
- Statement (**PARAPHRASE**, standard and confirmed independently by C2's own citation
  language, `main.tex:456,583-584` in math/0606037): monic OPUC are shown to be the
  characteristic polynomials of unitary, five-diagonal ("CMV") matrices built from the
  Verblunsky/Schur coefficients; this is the origin of the "CMV matrix" as the canonical
  minimal unitary representation for OPUC, the unit-circle analogue of a Jacobi matrix.
- TeX on arXiv: **yes** — `math/0204300`.

### C4. M. J. Cantero, L. Moral, L. Velázquez, "Minimal representations of unitary operators
and orthogonal polynomials on the unit circle", *Linear Algebra Appl.* **408** (2005), 40–65
(the task calls this "Cantero-Moral-Velázquez 2002/3"; the minimal-representation paper is
dated 2005 in its LAA publication, though a preprint may predate it).

- Not independently searched for an arXiv id this session; **UNVERIFIED** whether one exists.
  Recommend checking `arXiv:math/0405290`-range or later CMV-matrix search terms in a follow-up
  session; not blocking, since C2 (math/0606037) already supplies and cites the needed
  "eigenvalues of finite CMV = zeros of characteristic/paraorthogonal polynomial" statement
  directly.

---

## D. Slepian / discrete prolate spheroidal sequences

### D1. D. Slepian, "Prolate spheroidal wave functions, Fourier analysis, and uncertainty — V:
The discrete case", *Bell Syst. Tech. J.* **57** (1978), no. 5, 1371–1430.
DOI: 10.1002/j.1538-7305.1978.tb02104.x.

- No arXiv (1978).
- Statement (**PARAPHRASE**, from the Wiley abstract, not independently read in full):
  introduces **discrete prolate spheroidal sequences (DPSS)** and discrete prolate spheroidal
  functions — index-limited-and-band-limited eigen-sequences of a finite Toeplitz operator built
  from the `sinc` kernel — as the exact discrete/finite-index analogue of the continuous
  Slepian-Pollak prolate functions the CCM papers use (`2511.22755` cites `[Slepian]` = D2
  below, and `[Sl]` = "Some asymptotic expansions for prolate spheroidal wave functions," J.
  Math. Phys. 44 (1965), 99-140, per `refs/src/2511.22755/mc2arXiv.tex:1522`). **This is exactly
  the object this lane's task description calls "Slepian's discrete prolate spheroidal
  sequences as the analogue of the paper's prolate functions"** — confirmed as the right paper.
- TeX on arXiv: **no**. Full text via Internet Archive:
  <https://archive.org/details/bstj57-5-1371> (freely downloadable scan, not fetched/read this
  session).

### D2. D. Slepian and H. O. Pollak, "Prolate spheroidal wave functions, Fourier analysis and
uncertainty — I", *Bell Syst. Tech. J.* **40** (1961), 43–63.

- No arXiv, no DOI listed by CCM's own bibliography.
- **VERIFIED as the exact reference CCM cites**:
  `refs/src/2511.22755/mc2arXiv.tex:1527-1529` —
  `\bibitem{Slepian} D.~Slepian and H.~Pollack, \emph{Prolate spheroidal wave functions,
  Fourier analysis and uncertainty}, Bell Syst. Tech. J. (1961), 43--63.` This is Part I of the
  continuous-case series; the discrete case is D1 (Part V, different author list — Slepian
  alone). Since the finite-graph analogue is discrete from the start, **D1 is the more directly
  relevant paper of the two for the graph lane**, not D2.
- TeX on arXiv: **no**.

### D3. W. H. J. Fuchs, "On the eigenvalues of an integral equation arising in the theory of
band-limited signals", *J. Math. Anal. Appl.* **9** (1964), 317–330.
DOI: 10.1016/0022-247X(64)90079-0.

- No arXiv (1964).
- **VERIFIED as the exact reference CCM cites** for the eigenvalue-defect asymptotics of the
  continuous prolate operator:
  `refs/src/2511.22755/mc2arXiv.tex:1497-1499` —
  `\bibitem{Fuchs} Fuchs, W. H. J. \emph{On the eigenvalues of an integral equation arising in
  the theory of band-limited signals}. J. Math. Anal. Appl. 9 (1964), 317-330.`
- Statement (**PARAPHRASE**, standard): proves the sharp asymptotic transition ("plunge region")
  in the eigenvalues of the finite Fourier / time-and-band-limiting operator, i.e. the
  `~2λ` eigenvalues near 1 followed by a rapid drop to near 0 — exactly the fact
  `2511.22755:189` (quoted above, F1 in the CCM-paper reading in `notes/zeta-spectral-triples`)
  uses: "the corresponding eigenfunctions ... admits a finite number `1+ν(λ²)~2λ²` of extremely
  small non zero eigenvalues." The **discrete** analogue of this Fuchs eigenvalue-defect
  asymptotic is precisely what Slepian's discrete-case paper D1 supplies for DPSS, and is the
  quantity that would govern the finite-graph window's "plunge region" (how many Fourier modes
  of the `{-M..M}` window are well-resolved before the minimal eigenvector becomes numerically
  degenerate).
- TeX on arXiv: **no**.

---

## E. Connes school — the source of the whole construction

### E1. A. Connes and C. Consani, "Spectral triples and ζ-cycles", *Enseign. Math.* **69**
(2023), no. 1-2, 93–148. DOI: 10.4171/LEM/69-1/2-5. **arXiv:2106.01715.**

- **VERIFIED VERBATIM**, fetched and read this session
  (`arxiv.org/e-print/2106.01715` → `Spectraltriples.tex`, 148 KB):

  > Abstract: "We exhibit very small eigenvalues of the quadratic form associated to the Weil
  > explicit formulas restricted to test functions whose support is within a fixed interval
  > with upper bound S. We show both numerically and conceptually that the associated
  > eigenvectors are obtained by a simple arithmetic operation of finite sum using prolate
  > spheroidal wave functions associated to the scale S. Then we use these functions to
  > condition the canonical spectral triple of the circle of length L=2 Log(S) in such a way
  > that they belong to the kernel of the perturbed Dirac operator." — `Spectraltriples.tex:113`.
  > "The spectral triple Θ(λ,k) is a finite rank perturbation of the Dirac operator on a circle
  > of length log μ=2log λ and involves, as a key ingredient, classical prolate spheroidal wave
  > functions." — `Spectraltriples.tex:168`.

  This is exactly `[VJ]` in `2511.22755`'s own bibliography
  (`refs/src/2511.22755/mc2arXiv.tex:1476-1477`: `\bibitem{VJ} A.~Connes, C.~Consani, {\em
  Spectral triples and $\zeta$--cycles}. Enseign. Math. \textbf{69} (2023), no. 1--2, 93-148.`)
  — the paper introducing the prolate-conditioned Dirac-operator construction that
  `zst` implements. Note: the task description's guess `arXiv:2211.02418` (not stated in the
  task, just checking my own priors) is **wrong** — the correct id, confirmed by two
  independent routes (WebSearch title match + reading the fetched TeX header), is
  **2106.01715**.
- TeX on arXiv: **yes** — `2106.01715`.

### E2. A. Connes and W. van Suijlekom, "Quadratic Forms, Real Zeros and Echoes of the Spectral
Action", *Commun. Math. Phys.* **406** (2026), no. 12, article 312 (a volume dedicated to
H. Araki). DOI: not yet resolved to a live Springer record this session (2026 forthcoming/just
published); arXiv record confirms venue/volume. **arXiv:2511.23257** (posted 28 Nov 2025).

- **VERIFIED VERBATIM**, fetched and read this session
  (`arxiv.org/e-print/2511.23257` → `Araki-final-oct25.tex`, 105 KB). This is `[CS]` in
  `2511.22755`'s bibliography (`refs/src/2511.22755/mc2arXiv.tex:1490-1492`: `\bibitem{CS}
  A.~Connes and W.~van Suijlekom, \emph{Quadratic Forms, Real Zeros and Echoes of the Spectral
  Action}, Commun. Math. Phys. (2025) 406:312, volume dedicated to H. Araki.`) — this is the
  **structure theorem** paper `2511.22755:269` credits for "the necessary self-adjointness":
  "The theoretical foundation rests on the framework introduced in~\cite{VJ} together with the
  extension in~\cite{CS} of the classical Carathéodory–Fejér theorem for Toeplitz matrices."
  Exact statement, **the theorem this whole lane is meant to reduce the graph case to**:

  > Corollary `corcar`: "Let T ∈ M_{n+1}(ℂ) be a Hermitian, positive semidefinite Toeplitz
  > matrix of rank n, and let ξ ∈ ker T. Then all the zeros of the polynomial
  > P(z) := Σ_{j=0}^n ξ_j z^j lie on the unit circle." — `Araki-final-oct25.tex:793-798`.

  Restated as Proposition `toeplitzcase` with a self-contained $C^*$-algebraic (GNS) proof
  rather than the classical CF route:

  > "Let T = (c_k) be a positive (n+1)-dimensional Toeplitz matrix of rank n. If (a_j)_{j=0}^n is
  > a vector in ker T then the polynomial P(z) = Σ_j a_j z^j has all zeros on unit circle in ℂ."
  > — `Araki-final-oct25.tex:900-902`, proof `Araki-final-oct25.tex:904-910` (GNS/positive-
  > measure-on-Pontryagin-dual argument).

  and its own explicit pointer to the number-theoretic/RH resonance and to Hallouin-Perret
  (item A8):

  > "This corollary exhibits a striking number-theoretic flavor, resonating with the analogue
  > of the Riemann Hypothesis for function fields; see~\cite{HP} for a further discussion of
  > this connection." — `Araki-final-oct25.tex:800`.

  **This IS, almost verbatim, the theorem the finite-graph (Toeplitz, real, rank-deficient
  Weil-form) case of this whole research programme needs**: real symmetric Toeplitz matrix of
  rescaled cycle counts, its minimal eigenvector (kernel of `τ - λ_min I`, or literally `ker T`
  if the window is chosen so the minimal eigenvalue is exactly 0), zeros of its associated
  polynomial land on `|z|=1` — i.e. on the "unitary line" that is the finite-graph analogue of
  the critical line. The paper also gives the even/odd (palindromic/anti-palindromic) splitting
  used throughout `zst`:

  > "J* = J since P(X) is either palendromic, or anti-palendromic, i.e. a_{n-j} = ± a_j for all
  > j = 0, …, n. Indeed, because of the structure of T as a Toeplitz matrix, it follows that if
  > (a_j)_j is in the kernel of T, so is (a_{n-j})_j." — `Araki-final-oct25.tex:865-868`.

  Caveat stated by the authors themselves, directly relevant to "does this need a simple
  eigenvalue?" (cf. Makhoul, B3): "when the kernel of T is more than one-dimensional... the
  correct formulation of the theorem is that if you take the intersection of the zeros of the
  various eigenfunctions, then they are all on the unit circle." — `Araki-final-oct25.tex:909`.
- TeX on arXiv: **yes** — `2511.23257`.

### E3. A. Connes and H. Moscovici, "The UV prolate spectrum matches the zeros of zeta",
*Proc. Natl. Acad. Sci. USA* **119** (2022), no. 22, e2123174119. DOI: 10.1073/pnas.2123174119.

- `[CM]` in `2511.22755`'s bibliography (`refs/src/2511.22755/mc2arXiv.tex:1489`). No arXiv id
  found via WebSearch this session (PNAS-direct paper, sometimes deposited as arXiv:2110.xxxxx
  under a different title — **UNVERIFIED**, not confirmed). Not fetched/read.

### E4. A. Connes, C. Consani, H. Moscovici, "Zeta zeros and prolate wave operators",
arXiv:2310.18423.

- `[Mox]` in `2511.22755`'s bibliography, **VERIFIED as cited**:
  `refs/src/2511.22755/mc2arXiv.tex:1485` — `\bibitem{Mox} A.~Connes, C.~Consani,
  H.~Moscovici, {\em Zeta zeros and prolate wave operators}, ArXiv :2310.18423.` This is the
  direct predecessor/companion of `2511.22755` itself (same authorship as the task's "CCM"),
  cited in the task's own framing (item E asks for "Connes Consani Moscovici zeta zeros" —
  this is exactly that paper). Not independently re-fetched this session (its content is
  already the subject of the certified `zst/` implementation this lane is meant to extend).
- TeX on arXiv: **yes** — `2310.18423` (id given directly in the CCM bibliography; not
  separately verified by download this session, but the id is copied verbatim from a primary
  source, so it is trustworthy).

### E5. A. Connes and C. Consani, "Weil positivity and trace formula, the archimedean place",
*Selecta Math. (N.S.)* **27** (2021), article 79. DOI: 10.1007/s00029-021-00689-4.
**arXiv:2006.13771.**

- Already in this repo's `refs/fetch_sources.sh` IDS list (confirmed by
  `grep 2006.13771 refs/fetch_sources.sh` → present) but **not yet physically fetched** to
  `refs/src/` (only `2511.22755` is present there today). Not re-fetched this session (outside
  this lane's write scope; add to TO FETCH). Content (**PARAPHRASE**, via WebSearch abstract
  summary, not independently read): expresses the difference between the Weil distribution and
  the Sonin trace, for the single archimedean place, in terms of prolate spheroidal wave
  functions and Hermitian Toeplitz matrices — i.e. this is very likely the paper that first
  connects Weil positivity to the Toeplitz-matrix machinery that CS (E2) later makes rigorous,
  and should be read closely before finalising the finite-graph plan, since its "single place"
  framing is the closest existing analogue of a "one prime `p`" (or one cycle-length) window.
- TeX on arXiv: **yes** — `2006.13771` (already tracked; needs an actual fetch run).

### E6. Related Connes-Consani papers named by the task but not further chased this session
(no independent verification beyond noting they exist and are plausible arXiv ids from prior
knowledge — **all UNVERIFIED, do not cite without checking**): "Spectral triples and
zeta-cycles" = **E1 above** (task listed it separately as "2022" but it is E1, 2021 arXiv /
2023 journal — same paper, not two); "Riemann-Roch for the ring Z" (Connes-Consani, has an
arXiv id, not looked up this session).

---

## F. Graph explicit-formula numerics / Selberg trace formula for graphs

### F1. G. Ahumada, "Fonctions périodiques et formule des traces de Selberg sur les arbres",
*C. R. Acad. Sci. Paris Sér. I Math.* **305** (1987), 709–712.

- No DOI (1987 Comptes Rendus note); no arXiv. **VERIFIED as the correct citation** via direct
  PDF read of A. Terras and D. Wallace, "Selberg's Trace Formula on the k-Regular Tree and
  Applications" (see below), whose own reference list gives:

  > "[1] G. Ahumada, Fonctions périodiques et formule des traces de Selberg sur les arbres,
  > C.R. Acad. Sci. Paris, 305, Sér. I (1987), 709-712." — `treetrace.pdf`, References, item
  > [1].

  and whose body credits Ahumada with the actual proof technique used:

  > "The proof we sketch is due to Ahumada [1]." — `treetrace.pdf`, p. 19 (§4, just before
  > Theorem 3, "(Ihara)").
- TeX on arXiv: **no**.

### F2. A. Terras and D. Wallace, "Selberg's Trace Formula on the k-Regular Tree and
Applications", *IMRN / other* — actually circulated as an unpublished/course-note-style
preprint (author's own site), dated "November 10, 2001" in the PDF header; a version appeared
in *New York J. Math.* or similar (**UNVERIFIED exact final venue** — the fetched PDF itself
carries no journal header, only "Date: November 10, 2001" and AMS subject classifications
11F72, 05C99, 43A90).

- **VERIFIED VERBATIM**, read in full this session via Wayback Machine capture (archived
  2024-01-23,
  `https://web.archive.org/web/20240123040524/https://mathweb.ucsd.edu/~aterras/treetrace.pdf`).
  This is **exactly** the task's requested item: "the connection between Ihara zeta and the
  Selberg trace formula on graphs ... Terras's book chapter on the 'Selberg trace formula for
  graphs'" — this paper (not the book, which was not independently accessible) is the primary,
  fully worked-out source, and derives the Ihara-Bass determinant formula (their Theorem 3, "the
  following theorem can be attributed to many people... Bass [2], Hashimoto [9], and Sunada
  [18] certainly should be mentioned. The proof we sketch is due to Ahumada [1]") from a genuine
  discrete Selberg trace formula on the `k`-regular tree (their Theorem 2), built from:
  - the **spherical functions** `h_s(d)` on the tree (their analogue of Legendre functions
    `P_{-s}(cosh r)` on the hyperbolic plane), §2.3;
  - the **horocycle transform** `Hf` and its relation to the spherical transform (Lemma 3,
    `f̂(s) = Σ_n Hf(n) q^{|n|/2} z^n`);
  - **Selberg's Lemma** (their Corollary 2): `(f,φ)_Ξ = φ(o)(f,h_s)_Ξ` — the tree pre-trace
    identity;
  - the full **trace formula** (Theorem 2): `Σ_i f̂(s_i) = f(o)|X| + Σ_{ρ∈P_Γ} ν(ρ) Σ_{e≥1}
    Hf(eν(ρ))` — a genuine discrete analogue of the Selberg trace formula, with the "geometric
    side" a sum over primitive hyperbolic conjugacy classes (= primes in the graph) and the
    "spectral side" a sum of spherical transforms over eigenvalues of the adjacency operator;
  - the graph prime number theorem `π_X(r) ~ q^r/r` (their (4.2)), from the pole structure of
    `ζ_X(u)` alone (Landau's theorem argument), **not** from a Weil-style explicit formula with
    general test functions — confirming the A6/A7 finding that no genuine Weil-explicit-formula
    (arbitrary test function `h`, Fourier-dual `g`) statement for graphs was located this
    session.

  This paper is thus the correct, verified answer to F's "connection between Ihara zeta and the
  Selberg trace formula" request, and its trace-formula machinery (spherical/horocycle
  transform pair on the `k`-regular tree) is the natural "already exists" analogue of the
  Fourier-truncation machinery in `zst`/CCM, specialised to `(q+1)`-regular graphs (this lane's
  target, Z-indexed cycle counts, is closer to the *irregular*-graph, edge/path-zeta,
  Toeplitz-of-cycle-counts picture of A5/A6, which does not reduce to a single spherical
  transform since `A_X` and `Q_X` need not commute — explicitly noted in A5/III,
  `graphbrauersiegel.pdf` p. 7: "Since AX and QX do not necessarily commute when X is
  irregular, we cannot simultaneously diagonalize AX and QX...").
- TeX on arXiv: **no**.

### F3. "Spectral reconstruction from closed walks" / "trace method Ihara" — task asked for any
paper reconstructing graph spectra from cycle counts.

- **NOT FOUND** as a distinctly-named result this session beyond the elementary fact used
  throughout A6/F2 themselves: `N_m = Σ_{λ∈Spec(W_1)} λ^m/m` (Horton-Stark-Terras eq. (2.15),
  **VERIFIED VERBATIM** above) — i.e. the power sums of the non-backtracking-operator spectrum
  *are* the closed-non-backtracking-walk counts, by construction/definition of the Ihara zeta
  function as `det(I - uW_1)^{-1}`. This is already exactly the "reconstruction" fact the
  finite-graph analogue needs (cycle counts ↔ trace of powers of the transfer operator ↔
  spectrum via Newton's identities / the secular polynomial), and requires no further
  literature search — it is definitional, not a separate theorem to attribute. No paper titled
  "spectral reconstruction from closed walks" was located; if the design lane wants a citation
  for the elementary Newton's-identities step, any of A3/A5/A6/F2 suffices and is already
  verified.

---

## TO FETCH (arXiv ids, in the exact space-separated form `refs/fetch_sources.sh` uses)

Add these to the `IDS=` line in `refs/fetch_sources.sh` (outside this lane's write scope — flag
for the maintainer) and re-run it to populate `refs/src/` with checkable TeX:

```
2106.01715 2511.23257 math/0204300 math/0606037 2006.13771 2310.18423
```

- `2106.01715` — Connes-Consani, "Spectral triples and ζ-cycles" [VJ] (E1). Already fetched to
  this session's scratchpad and quoted; not yet in `refs/src/`.
- `2511.23257` — Connes-van Suijlekom, "Quadratic Forms, Real Zeros and Echoes of the Spectral
  Action" [CS] (E2). Same status.
- `math/0204300` — Cantero-Moral-Velázquez, CMV matrices (C3). Fetched to scratchpad, not yet
  content-verified line-by-line.
- `math/0606037` — Simon, "Rank One Perturbations and the Zeros of POPUC" (C2). Fetched and
  fully quoted from this session.
- `2006.13771` — Connes-Consani, "Weil positivity and Trace formula, the archimedean place"
  (E5). Already listed in `refs/fetch_sources.sh`'s `IDS`, but not yet physically present in
  `refs/src/` — just needs the script re-run.
- `2310.18423` — Connes-Consani-Moscovici, "Zeta zeros and prolate wave operators" [Mox] (E4).
  Not yet in `refs/fetch_sources.sh`'s `IDS`; add it.

(`2511.22755` itself is already fetched and present in `refs/src/`, per this session's directory
check.)

---

## No-arXiv items and their best accessible alternative

| Item | Reference | Best accessible alternative |
|---|---|---|
| A1 | Ihara 1966, J. Math. Soc. Japan 18 | Project Euclid: `projecteuclid.org/euclid.jmsj/1260541107` |
| A2 | Hashimoto 1989, Adv. Stud. Pure Math. 15 | none found freely online; library/ILL copy of the proceedings volume |
| A3 | Bass 1992, Internat. J. Math. 3 | DOI 10.1142/S0129167X92000357 (publisher paywall); quoted verbatim in every downstream paper (A5, A6, F2) |
| A4 | Kotani-Sunada 2000, J. Math. Sci. Univ. Tokyo 7 | quoted verbatim in A6 (`snowbird.pdf`, Wayback capture below) |
| A5 | Stark-Terras I/II/III, Adv. Math. 121/154/208 | Part III: Wayback capture of author PDF, `https://web.archive.org/web/20240415004428/https://mathweb.ucsd.edu/~aterras/graphbrauersiegel.pdf`; Parts I/II: DOI 10.1006/aima.1996.0050 and 10.1006/aima.2000.1917 (paywall) |
| A6 | Horton-Stark-Terras 2006, Contemp. Math. 415 | Wayback capture, `https://web.archive.org/web/20240123040609/https://mathweb.ucsd.edu/~aterras/snowbird.pdf` |
| A7 | Terras 2011 book (CUP) | publisher page `cambridge.org/9780521113670`; AMS Bulletin review (secondary) `ams.org/bull/2014-51-01/S0273-0979-2013-01426-5/S0273-0979-2013-01426-5.pdf` |
| A8 | Hallouin-Perret 2019, TAMS 372 | DOI 10.1090/tran/7568 (paywall); cited verbatim inside `2511.23257` (already fetched) |
| B1 | Carathéodory-Fejér 1911 | restated and fully reproved in `2511.23257` §2 (fetched, quoted in E2) |
| B2 | Pisarenko 1973, Geophys. J. R. Astr. Soc. 33 | Oxford Academic `academic.oup.com/gji/article/33/3/347/610926` (paywall) |
| B3 | Makhoul 1981, IEEE Trans. ASSP-29 | IEEE Xplore `ieeexplore.ieee.org/document/1163635` (paywall) |
| B4 | Delsarte-Genin-Kamp, IEEE Trans. Circuits Syst. 25 (1978) etc. | not located; check Simon's OPUC-book (C1) reference list |
| B5 | Cantoni-Butler 1976, Linear Algebra Appl. 13 | ScienceDirect `sciencedirect.com/science/article/pii/0024379576901014` (paywall); UWA repository record |
| B6 | Schmidt 1986, IEEE Trans. AP-34 | IEEE record, DOI 10.1109/TAP.1986.1143830 (paywall) |
| C1 | Simon 2005, AMS Colloq. Publ. 54 | AMS Bookstore; library copy needed for exact theorem number |
| D1 | Slepian 1978, Bell Syst. Tech. J. 57 | Internet Archive, freely downloadable: `archive.org/details/bstj57-5-1371` |
| D2 | Slepian-Pollak 1961, Bell Syst. Tech. J. 40 | Wiley DOI 10.1002/j.1538-7305.1961.tb03976.x (paywall) |
| D3 | Fuchs 1964, J. Math. Anal. Appl. 9 | DOI 10.1016/0022-247X(64)90079-0 (paywall) |
| E3 | Connes-Moscovici 2022, PNAS 119 | DOI 10.1073/pnas.2123174119 (open access on PNAS site typically) |
| F1 | Ahumada 1987, C.R. Acad. Sci. Paris 305 | none found freely online; quoted verbatim inside F2 |
| F2 | Terras-Wallace, "Selberg's Trace Formula on the k-Regular Tree" | Wayback capture, `https://web.archive.org/web/20240123040524/https://mathweb.ucsd.edu/~aterras/treetrace.pdf` |

---

## Summary of verification status by item

- **Fully verified (primary text read and quoted this session):** A4 (via A6), A5-III, A6, A8
  (via E2), B1 (via E2), C2, E1, E2, F1 (via F2), F2.
- **Bibliographically confirmed / cited verbatim inside an already-verified source, but not
  independently read in full:** A2 (via A6/F2 refs), A3 (via A5/A6/F2 refs, formula itself
  independently cross-checked in three sources), C3 (fetched, not line-verified), D2, D3, E4,
  E5 (arXiv id confirmed, content not read), E6 partial.
- **UNVERIFIED (secondary WebSearch summary only, full text not obtained):** A1, A7 (the single
  biggest gap — the book's actual explicit-formula/RH chapter content was never confirmed), B2,
  B3 (the exact hypotheses need primary-text confirmation before being relied on), B4, B5, B6,
  C1 (theorem number), C4 (arXiv id existence itself unverified), E3 (arXiv id existence
  unverified), the "gamma factor" framing of `(1-u^2)^{|E|-|V|}` (task's own phrasing — actively
  **not found** in three primary sources searched), and any "Weil explicit formula in test-
  function form for graphs" (actively **not found**; the graph literature has a prime number
  theorem and a pole-location "RH," not a Weil-style explicit formula with general test
  function pairs `h, ĝ`).
