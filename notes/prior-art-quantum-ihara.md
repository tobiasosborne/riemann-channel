# Prior art for the "quantum Ihara zeta"

Written 2026-09-12. Three Opus literature agents (angles: graph-zeta / L-functions; quantum expanders and free probability; direct phrase search on arXiv, Scholar, MathOverflow), then every load-bearing claim re-checked by the orchestrator against the arXiv **TeX source** of the paper. Sources live in `refs/src/<arxiv-id>/` (fetched by `refs/fetch_sources.sh`, hashes in `refs/manifest.sha256`); a quote below is cited as `<id>:<file>:<line>` and was copied from those bytes. Anything not local is marked `[UNVERIFIED]`.

## 0. The object under examination

From the founding session (2026-09-11, `transcript/transcript.md` 08:15 UTC; `HANDOFF.md` item 1): for a unital channel $\Phi(\rho) = \frac1D\sum_i U_i\rho U_i^\dagger$ with unitary Kraus operators closed under adjoint, the non-backtracking edge superoperator $T$ on $M_n\otimes\mathbb C^D$, $T(\rho\otimes|i\rangle) = \sum_{j\ne i^{-1}} U_i\rho U_i^\dagger\otimes|j\rangle$, and $\zeta_\Phi(u) = \det(1-uT)^{-1}$. Four claims were made:

1. **Ihara–Bass.** $\det(1-uT) = (1-u^2)^{n^2(D-2)/2}\det(1 - uD\Phi + (D-1)u^2)$.
2. **RH $\iff$ Ramanujan.** All nontrivial poles of $\zeta_\Phi$ on $|u| = (D-1)^{-1/2}$ iff $\Phi$ is a Ramanujan quantum expander in Hastings' sense.
3. **Identification.** $\zeta_\Phi$ is the Artin–Ihara $L$-function of the bouquet with $D/2$ loops twisted by $g_i\mapsto U_i\cdot U_i^\dagger$; $\operatorname{Tr}T^m = \sum_w |\operatorname{Tr}U_w|^2$ over cyclically reduced words.
4. **Weil–LPS instance.** For the Weil representation of $\mathrm{SL}_2(\mathbb F_p)$ with LPS generators, $\zeta_\Phi$ satisfies RH exactly.

Also the MPS reading (channel = transfer matrix, $\zeta$ = generating function of ring norms, RH = one correlation length, AKLT gives $K_4$).

## 1. Verdict

| claim | status | where |
|---|---|---|
| 1 Ihara–Bass with $\mathrm{Ad}(U)$ weights | **known** | Matsuura–Ohta 2022, eqs. (2.8)–(2.11) with $X_e = U_e\otimes U_e^\dagger$ (loops allowed); the arbitrary-matrix-weight formula of Watanabe–Fukumizu 2011, Cor. `cor:IBfornonhyper`, for loopless graphs; representation-twisted zeta goes back to Sunada 1986 / Hashimoto 1989 `[UNVERIFIED, secondary]` |
| 3 trace formula, free-group $L$-function | **known** | Matsuura–Ohta 2022 eq. (2.10); Matsuura–Ohta 2026 (Artin–Ihara $L$ for a representation of a finite group, extended to $U(N_c)$; $\rho_{\rm adj}$ named) |
| 2 RH for $\zeta_\Phi$ $\iff$ Hastings-Ramanujan | **not found** | zero hits for any zeta/Ihara + channel/Kraus/CP-map/expander combination; Matsuura–Ohta contain none of the words Ramanujan, expander, Riemann hypothesis; Bordenave–Collins have the operator but no determinant or zeta |
| 4 exactly Ramanujan channels from LPS | **mechanism known, instance not** | Harrow 2008 $\lambda_2(\mathcal E)\le\lambda_2(W_\Gamma)$ + LPS; Iyer–Jain–Jordan–Somma (Feb 2026) state it with $SU(2)$ irreps and call explicit Ramanujan quantum expanders "a longstanding open problem"; no Weil-representation instance, no zeta |
| MPS / ring-norm reading, AKLT $=K_4$ | **not found** | no hits for Ihara/zeta + matrix product state / transfer matrix / AKLT |

Consequence for this repo: cite Matsuura–Ohta, Watanabe–Fukumizu and Sunada/Hashimoto for the object and the determinant formula; present the RH-for-channels reading, the MPS dictionary, and the Weil–LPS instance as this notebook's contribution. The general Kraus-operator formula in `notes/quantum-ihara-general.md` is the bouquet analogue of Watanabe–Fukumizu's arbitrary-weight corollary, which is stated only for loopless graphs; it is proved there from scratch, and no local source covers arbitrary non-invertible weights on a bouquet.

## 2. Candidates, with byte-checked quotes

### Matsuura & Ohta, "Kazakov-Migdal model on the Graph and Ihara Zeta Function", JHEP 09 (2022) 178, arXiv:2204.06424

Defines the "extended Ihara zeta function" with invertible matrix weights and proves the three-term formula by Bass's argument; applies it with adjoint weights.

- `2204.06424:main.tex:476` — "Suppose $X_{e}$ $(e\in E)$ are invertible matrices of size $K$ living on each edge."
- `2204.06424:main.tex:479-482` (eq. 2.8) — `\zeta_G(q;X) \equiv \det\Bigl( \bs{1}_{2n_E}\otimes\bs{1}_{K} - q W_X \Bigr)^{-1}`
- `2204.06424:main.tex:489-494` (eq. 2.9, edge matrix): `X_{e} & {\rm if}\ \bse=e\in E, \ t(e) = s(\bse'),\ {\rm and}\ \bse'^{-1}\ne e` / `X_{e}^{-1} & {\rm if}\ \bse=e^{-1}\in E^{-1}, ...`
- `2204.06424:main.tex:503-505` (eq. 2.10, trace formula): `\zeta_G(q;X) = \exp\lrpar{ \sum_{k=1}^\infty \frac{1}{k}\sum_{C\in R_k}\Tr P_{C}(X) }`
- `2204.06424:main.tex:516-519` (eq. 2.11, Ihara–Bass): `\zeta_G(q;X) = (1-q^2)^{(n_V-n_E)K}\det\Bigl( \bs{1}_{n_V}\otimes\bs{1}_{K} - qA_X + q^2(D-\bs{1}_{n_V})\otimes\bs{1}_K \Bigr)^{-1}`
- `2204.06424:main.tex:533-534` — "The following proof is parallel to the one given in \cite{bass1992ihara} for the original Ihara zeta function"
- `2204.06424:main.tex:696` — "where $S_U$ and $T_U$ are defined by (\ref{S and T}) with $X_e=U_e\otimes U_e^\dagger$"

Specialise to the bouquet (their construction admits loops and multiple edges; a loop contributes $X_e + X_e^{-1}$ to $A_X$ and $2$ to the degree): $n_V = 1$, $n_E = D/2$, $K = n^2$, $D_{\rm graph} = D$: exponent $(n_V - n_E)K = -n^2(D-2)/2$ and the bracket is $1 - qA_X + (D-1)q^2$ with $A_X = \sum_i \bar U_i\otimes U_i = D\Phi$ (column-stacking convention, as in `notes/quantum-ihara-general.md`). After inverting eq. (2.8), $\zeta_G^{-1} = \det(1-qW_X)$, this is claim 1. Verdict: claims 1 and 3 SAME.

### Matsuura & Ohta, "Graph Zeta Functions and Wilson Loops in Kazakov-Migdal Model", arXiv:2208.14032

- `2208.14032:main.tex:137` — `\title{Graph Zeta Functions\\and\\Wilson Loops in Kazakov-Migdal Model}`. Matrix-weighted Bartholdi zeta with the same adjoint weights; the Ihara case is $u = 0$ of their Bartholdi parameter. Verdict: SAME (via the previous item).

### Matsuura & Ohta, "Generalized Kazakov-Migdal Models on Graphs via Artin-Ihara L-function and Random Partitions", arXiv:2607.27935 (v2, 26 Aug 2026)

- `2607.27935:main.tex:381` — `\equiv\prod_{[C]\in [{\cal P}]}\det\left(I_{d_R}-\rho_R(g_C)q^{\ell(C)}u^{b(C)} \right)^{-1}` (Artin–Ihara $L$-function for a representation $R$ of a finite group, extended to $U(N_c)$ at `2607.27935:main.tex:470`; Bartholdi-deformed)
- `2607.27935:main.tex:401-404` — `\left(1-q^2(1-u)\right)^{(n_E-n_V)d_R}` ... `\det\left(I_{n_V d_R} -q A_{G,R}^\alpha +q^2(1-u)(D-(1-u)I_{n_V d_R})\right)^{-1}`
- `2607.27935:main.tex:508-510` — "the KM model on the arbitrary graph (gKM model) proposed in \cite{Matsuura:2022dzl,Matsuura:2022ner} is the model with the representation $R$ being the adjoint representation of $U(N_c)$," `\rho_{\rm adj}(U_e) = U_e\otimes U_e^\dag`

Verdict: claim 3 SAME (they name the object an Artin–Ihara $L$-function of a bundle with representation $\rho_{\rm adj}$).

### Watanabe & Fukumizu, "Loopy belief propagation, Bethe free energy and graph zeta function", arXiv:1103.0605 (JMLR 2011; extends NeurIPS 2009)

Matrix-weighted edge zeta with **arbitrary** weights (no inverse relation between $u_e$ and $u_{\bar e}$), and an Ihara–Bass formula for it. Their graphs are hypergraphs whose hyperedges are subsets of $V$ of size two (`1103.0605:section2.tex:17-25`): no loops and no multiple edges, so a bouquet is not one of their graphs.

- `1103.0605:section3.tex:307-318` — definition: "matrix weights $\bsu=\{ u_{e} \}_{e \in \vec{E}}$ with $u_e \in \mat{r_{t(e)}}{r_{o(e)}}$," `Z_{G}(\boldsymbol{u}):=\prod_{\mathfrak{p} \in \mathfrak{P}_G } \det(1-\pi(\mathfrak{p}))^{-1}, \quad \pi(\mathfrak{p}):=u_{e_1} \cdots u_{e_k}`
- `1103.0605:section3.tex:330-341` — Corollary `cor:IBfornonhyper`: `Z_{G}(\bs{u})^{-1}= \det ( I + \hat{\mathcal{D}}(\bsu) - \hat{\mathcal{A}}(\bsu) ) \prod_{[e] \in {E}} \det(I - u_e u_{\bar{e}})` with `(\hat{\mathcal{D}}(\bsu)g)(i):= \Big( \sum_{e: t(e)=i}(I_{r_i}-u_eu_{\bar{e}})^{-1}u_eu_{\bar{e}} \Big)g(i)` and `(\hat{\mathcal{A}}(\bsu)g)(i):= \sum_{e: t(e)=i}(I_{r_i}-u_eu_{\bar{e}})^{-1}u_e g(o(e))`
- `1103.0605:section3.tex:373` — "Corollary \ref{cor:IBfornonhyper} gives the extension of the result to graphs with arbitrary weights."

Theorem 1 of `notes/quantum-ihara-general.md` is the loop-admitting (bouquet) analogue of this corollary, with the same shape after $u_e = uE_e$; the corollary itself does not cover the bouquet, and its scalar reduction (`1103.0605:section3.tex:377-397`) does not evaluate correctly there. `1103.0605:section3.tex:374-375` points to a hypergraph-free proof in the NeurIPS 2009 supplement, not fetched. Verdict: RELATED, the closest prior art for arbitrary weights; not a special case. No representation-theoretic or quantum reading is drawn.

### Bordenave & Collins, "Eigenvalues of random lifts and polynomials of random permutation matrices", Ann. Math. 190 (2019), arXiv:1801.00876

Operator-valued non-backtracking operator with matrix coefficients; spectral (resolvent) correspondence; explicitly aimed at quantum expanders; no determinant, no zeta.

- `1801.00876:tenseur9.tex:158` — "Our proof relies on the development of a matrix version of the non-backtracking operator theory and a refined trace method."
- `1801.00876:tenseur9.tex:165` — "Finally, we extend our results to tensor products of random permutation matrices. This extension is especially relevant in the context of quantum expanders."
- `1801.00876:tenseur9.tex:779-786` — "The non-backtracking operator $B$ associated to $A$ is the operator on $\dC^r \otimes \ell^{2} (E) = \dC^r \otimes \ell^2 (X) \otimes \dC^d$ defined by" `B = \sum_{j \ne i^*} a_j \otimes S_i \otimes E_{ij}`
- `1801.00876:tenseur9.tex:608-610` — "the family $S_i\otimes S_i$ viewed as an operator on $V^\perp$ is a nearly optimal quantum expander in the sense of Hastings \cite{MR2486279} and Pisier \cite{MR3226740}."

Follow-ups: arXiv:2012.08759 (Invent. Math. 2024; general unitaries), arXiv:2304.05714, whose §9 is the only place the words appear: `2304.05714:PT-RC_reloaded.tex:2568` — "This formula is closely related to various spectral identities known as Ihara-Bass identities; ... An interesting aspect of the present theorem is that it is in an identity in its strongest form, i.e., between two operators." and `2304.05714:PT-RC_reloaded.tex:399` — "Operator-valued non-backtracking operators were introduced in \cite{MR4024563,BC2} ... These operators have, however, some important drawbacks: they are not self-adjoint, the spectral correspondence is established only for $\cA_1 = M_n(\dC)$". Verdict: RELATED (the operator, resolvent identity); NOT for zeta / RH.

### Hastings, "Random unitaries give quantum expanders", PRA 76, 032315 (2007), arXiv:0706.0556

- `0706.0556:sd10.tex:118-122` — "Let $\lambda_2$ be the eigenvalue with the second largest absolute value of all eigenvalues other than $\lambda_1$. Let" `\lambda_{H}=\frac{2\sqrt{D-1}}{D}.`

Source of the bound in claim 2. No zeta, no non-backtracking. Verdict: NOT (except as the bound).

### Harrow, "Quantum expanders from any classical Cayley graph expander", QIC 8 (2008), arXiv:0709.1142

- `0709.1142:main.tex:72-73` — "degree becomes the number of Kraus operators, the spectral gap becomes the gap of the quantum operation"
- `0709.1142:main.tex:213-217` — `\lambda_2(\cE) \leq \lambda_2(W_\Gamma)` "Here $\lambda_2(\cE)$ is the second largest singular value of $\cE$, when interpreted as a linear map on density matrices, while $\lambda_2(W_\Gamma)$ is the second-largest singular value of the Cayley graph transition matrix"

With $\Gamma$ = LPS generators in $\mathrm{PSL}_2(\mathbb F_p)$ this gives exactly Ramanujan channels for any irrep. The word Ramanujan does not occur in the paper. Verdict: claim 4 mechanism SAME; no zeta.

### Iyer, Jain, Jordan & Somma, "Efficient quantum circuits for high-dimensional representations of SU(n) and Ramanujan quantum expanders", arXiv:2602.15180 (16 Feb 2026)

- `2602.15180:main.tex:241` — "Our quantum circuits can be used to construct explicit Ramanujan quantum expanders, a longstanding open problem."
- `2602.15180:main.tex:362` — "This was also a longstanding problem in quantum information. It is implied by Refs.~\cite{lubotzky1988ramanujan,harrow02expander,harrow2007quantum},"
- `2602.15180:main.tex:1508` — "Furthermore, it is possible to construct {\em exact} Ramanujan quantum expanders from $SU(2)$ unitaries derived from the LPS construction~\cite{lubotzky1988ramanujan,harrow2007quantum}."

Verdict: claim 4 RELATED (same mechanism, $SU(2)$ irreps rather than the Weil representation; no zeta). Note their Appendix C example $p = 5$, $D = 6$ uses the same norm-5 quaternions as `scripts/weil_lps.py`.

### Jeronimo, Mittal, Roy & Wigderson, "Almost Ramanujan expanders from arbitrary expanders via operator amplification", arXiv:2209.07024

- `2209.07024:abstract.tex:8` — "Ramanujan bound, so our construction gives almost Ramanujan expanders"
- `2209.07024:quan_exp.tex:37` — "In~\cite{Hastings07}, Hastings showed that the Ramanujan bound also"

Verdict: NOT (almost-Ramanujan only, no zeta).

### Komatsu, Konno & Sato, "Grover/Zeta Correspondence" and "Walk/Zeta Correspondence", arXiv:2103.12971, arXiv:2104.10287; Konno & Sato, QIP 11 (2012), arXiv:1103.0079; Komatsu–Konno–Sato, "The scattering matrix with respect to an Hermitian matrix of a graph", arXiv:2105.02677

Zeta functions built from the **unitary evolution matrix of a quantum walk on a graph** (Grover walk), not from Kraus operators. arXiv:2104.10287 extends to open quantum random walks on the torus by Fourier analysis; not read in full.

- `2105.02677:main.tex:87-89` — "A zeta function of a regular graph $G$ associated with a unitary representation of the fundamental group of $G$ was developed by Sunada \cite{Sunada1, Sunada2}."

Verdict: NOT for claims 1–4; the Sunada attribution is the pointer to the earliest twisted zeta.

### Eyler & Jun, "Artin-Ihara L-functions for hypergraphs", arXiv:2309.15873; Ghosh & Ray, "On the Iwasawa theory of Cayley graphs", arXiv:2405.04361

(Correction 2026-09-12 evening: an agent had attributed 2309.15873 to "Kudo & Li"; the TeX header `2309.15873:AiM_Final.tex:86,90` reads `\author{Mason Eyler}` and `\author{Jaiung Jun}`.)

Used only as verified secondary sources for the Stark–Terras definition and for Terras's three-term formula.

- `2309.15873:AiM_Final.tex:131` — "In fact, in \cite{stark2000zeta}, Stark and Terras further introduced notions of \emph{Galois coverings} and \emph{Artin-Ihara L-functions} for graphs"
- `2405.04361:v3.tex:427` — "according to the three-term determinant formula from \cite[Theorem 18.15]{Terras:2011} applied to the Artin-Ihara $L$-function"

In Stark–Terras the representation is of the Galois group of a covering of finite graphs (`2309.15873:AiM_Final.tex:131,203`; `2405.04361:v3.tex:396,470`), hence of a finite group; $\mathrm{Ad}(U_i)$ for generic unitaries generates an infinite group, so the notebook's object is not literally a Stark–Terras $L$-function, though the formula is the same. Verdict: RELATED.

### Not fetched (no arXiv source): `[UNVERIFIED]`

- T. Sunada, "L-functions in geometry and some applications", LNM 1201 (1986) 266–284. Cited by Matsuura–Ohta (`2204.06424:main.bbl:30`, ref [6]; body citations `main.tex:191,329`) and by Komatsu–Konno–Sato as the origin of the representation-twisted zeta.
- K. Hashimoto, "Zeta functions of finite graphs and representations of p-adic groups", ASPM 15 (1989) 211–280; "On zeta and L-functions of finite graphs", IJM 1 (1990) 381–396. Cited at `2204.06424:main.bbl:94,100`; body citations `main.tex:393,424`.
- H. Bass, "The Ihara–Selberg zeta function of a tree lattice", IJM 3 (1992) 717–797.
- H. M. Stark & A. A. Terras, "Zeta functions of finite graphs and coverings" I–III, Adv. Math. 121 (1996), 154 (2000), 208 (2007).
- A. Terras, *Zeta Functions of Graphs: A Stroll through the Garden*, CUP 2010 (Thm 18.15 per Ghosh–Ray).
- A. Ben-Aroya, O. Schwartz, A. Ta-Shma, "Quantum expanders: motivation and constructions", Theory of Computing 6 (2010) 47–79 (agent-verified from the publisher PDF: "we believe our first construction has the potential of being improved to a construction of a quantum Ramanujan expander").
- G. Pisier, arXiv:1503.07937, arXiv:1209.2059 (agent-checked: no Ihara/Bass/zeta/non-backtracking).
- D. Gross & J. Eisert arXiv:0710.0651; Hastings & Harrow arXiv:0804.0011; Chen–Garza-Vargas–Tropp–van Handel arXiv:2405.16026; Lancien–Youssef arXiv:2302.07772; Friedman–Kohler arXiv:1403.3462; Guido–Isola–Lapidus math/0608060; Deitmar arXiv:1402.4945; Harrison–Kirsten arXiv:0911.2509 (agent-checked abstracts/text: no zeta of a channel).

## 3. Searches that returned nothing

arXiv metadata queries (all zero hits): `"Ihara zeta" AND "quantum channel"`, `"Ihara zeta" AND "completely positive"`, `"zeta" AND "quantum expander"`, `"zeta" AND "Kraus operators"`, `abs:"zeta function" AND abs:"superoperator"`, `"Ruelle zeta" AND "quantum channel"`, `"Ihara" AND "matrix product state"`, `"AKLT" AND "zeta"`, `"non-backtracking" AND "superoperator"`, `"Ihara" AND ("quantum Ramanujan" OR "Ramanujan quantum")`. Web and Scholar searches for "quantum Ihara zeta", Ihara zeta + noncommutative/quantum graph (Weaver, Duan–Severini–Winter), Ihara zeta + MPS/tensor network, MathOverflow on Ihara zeta for quantum expanders: nothing on point. Limits: arXiv search is metadata-only; a formula inside a paper body would not surface.
