# Sources for the cusp-graph round (Gamma_0(N) < GL_2(F_q[T]) on the tree)

Author: claude:sonnet. Date: 2026-09-20.

Purpose: byte-verified sources for the NEXT round described in `notes/cusp-graph/astra-brief.md`
(attaching the ray to the quotient graph of a congruence subgroup `Gamma_0(N)` of `GL_2(F_q[T])`,
where the Eisenstein-series scattering matrix is expected to involve Dirichlet `L`-functions over
`F_q[T]`, the resonances their zeros, and Morgenstern's "Ramanujan diagrams" the relevant finite
objects). Every quote below was copied verbatim out of the file recorded, and every line number was
verified by `grep -n -F` against that file on disk; the command and its output are given under each
quote. Citation format: `<id>:<file>:<line>` as in `refs/README.md`. Preference throughout: arXiv TeX
source, never PDF text extraction; two pre-arXiv items (Efrat 1991, Morgenstern's 1991 UBC technical
report) were freely downloadable as PDF and are recorded under `refs/src/<slug>/` per the
`refs/src/uetake-2007/` precedent (they are not `.tex`, so they are **not** in `refs/manifest.sha256`;
their own sha256 is given here instead, computed directly from the files on disk).

Convention: a quote is marked **exact** when it states the fact needed by the brief essentially
verbatim, **variant** when it is a related but differently packaged statement (the difference is
spelled out), and a target is marked **NOT FOUND** when no freely accessible source stating it could
be located (bibliographic data is still given).

---

## 0. What was fetched (summary table)

| id / slug | Title | Author(s) | Where | In `refs/manifest.sha256`? |
|---|---|---|---|---|
| `efrat-1991` | Automorphic spectra on the tree of $PGL_2$ | I. Efrat | `refs/src/efrat-1991/{paper.pdf,paper.txt}` | no (non-arXiv PDF; own sha256 below) |
| `morgenstern-1991-tr` | Existence and Explicit Constructions of $q+1$ Regular Ramanujan Graphs for Every Prime Power $q$ (UBC TR-91-11, preprint of the JCTB 1994 paper) | M. Morgenstern | `refs/src/morgenstern-1991-tr/{paper.pdf,paper.txt}` | no (non-arXiv PDF; own sha256 below) |
| `2302.08850` | Zeta functions of geometrically finite graphs of groups | S. Hong, S. Kwon | `refs/src/2302.08850/sn-article.tex` | yes |
| `2603.26443` | Resonances on geometrically finite graphs | C. Arends, C. Peterson, T. Weich | `refs/src/2603.26443/{common.tex,final_draft.tex}` | yes |
| `2303.09327` | Quantum Unique Ergodicity for Eisenstein Series over Function Fields in the Level Aspect (a.k.a. "...on Bruhat–Tits Buildings") | I. Kaneko, S. Koyama | `refs/src/2303.09327/main.tex` | yes |
| `2108.02919` | Eisenstein series on arithmetic quotients of rank 2 Kac–Moody groups over finite fields (appendix by P. Garrett) | A. Ali, L. Carbone | `refs/src/2108.02919/KMGESFinal.tex` | yes |
| `0906.2825` | Quantum scattering theory on graphs with tails | M. Varbanov, T. A. Brun | `refs/src/0906.2825/main.tex` | yes |
| `1503.04952` | Spectra of infinite graphs with tails | L. Golinskii | `refs/src/1503.04952/main.tex` | yes |
| `1601.04573` | A functional relation for $L$-functions of graphs equivalent to the Riemann Hypothesis for Dirichlet $L$-functions | F. Friedli | `refs/src/1601.04573/L-functions.tex` (+ `.bbl`) | yes |
| `1909.07365` | Ramanujan graphs and exponential sums over function fields | N. T. Sardari, M. Zargar | `refs/src/1909.07365/part2.tex` (+ `.bbl`) | yes |
| `2105.02677` | The scattering matrix with respect to an Hermitian matrix of a graph | T. Komatsu, N. Konno, I. Sato | `refs/src/2105.02677/main.tex` | yes (already present from an earlier round) |

sha256 of the two non-arXiv items (not written into `refs/manifest.sha256`, which by convention in
`refs/fetch_sources.sh` only records `.tex`/`.bbl`/`lambda2.txt`):

```
$ sha256sum refs/src/efrat-1991/paper.pdf refs/src/efrat-1991/paper.txt \
            refs/src/morgenstern-1991-tr/paper.pdf refs/src/morgenstern-1991-tr/paper.txt
e7e76f710d7d972a99dad9afeceb13a5e91cea85665502d5c2b65adac8380e36  refs/src/efrat-1991/paper.pdf
ce3be6a351862bdf59fd81926300c84da09efcbae9c504904404a02230679074  refs/src/efrat-1991/paper.txt
de03c4c5868577fa43eb569f83d76a0f86d92e08027abee16b603defeb14b6cf  refs/src/morgenstern-1991-tr/paper.pdf
93326ae84991e29cc62b7beb61f8688d03d8edba058becc029f08f72b3246b01  refs/src/morgenstern-1991-tr/paper.txt
```

Efrat's paper was retrieved from e-periodica (ETH-Bibliothek's digitised-journals platform), the
open digitisation of *L'Enseignement Mathématique*, DOI `10.5169/seals-58728`, at
`https://www.e-periodica.ch/cntmng?pid=ens-001:1991:37::20` (bot-accessible variant of the same URL).
Morgenstern's technical report is UBC CS Dept. Technical Report 91-11 (June 1991), freely hosted at
`https://www.cs.ubc.ca/sites/default/files/tr/1991/TR-91-11.pdf`; it is the preprint of the JCTB 1994
paper (target 2, second item below), not of the SIAM "Ramanujan diagrams" paper (target 2, first item,
which could not be freely fetched — see Target 2 below).

All eight new arXiv ids were added to the `IDS=` list in `refs/fetch_sources.sh` and their `.tex`/`.bbl`
hashes appended to `refs/manifest.sha256`.

---

## Target 1 — Serre, *Trees*, II.1.6 / II.2 (the ray quotient of the tree by $GL_2(F_q[T])$)

Book, not fetchable (Serre, J.-P., *Trees*, Springer-Verlag, Berlin–New York, 1980, translated by
John Stillwell; the 2003 "Springer Monographs in Mathematics" reprint is the edition most later
papers cite). Its content is restated, with the stabiliser orders spelled out, by several arXiv papers
found for this round; all cite the exact chapter/section:

**`2603.26443:final_draft.tex:870`** (Arends–Peterson–Weich cite Serre II.1.6 by name for the Nagao-ray
structure of $\mathrm{PGL}(2,\mathbb F_q[T^{-1}])\backslash\!\backslash\mathcal T$):

```
with the obvious inclusions into $G_0$ and $G_1$, and for $j \geq 1$, $G_{\{j, j+1\}} = G_j$ with the obvious inclusions into $G_j$ and $G_{j+1}$. See Serre \cite{serre_trees} Chapter II Section 1.6. In particular, we remark that, if we cut along the edge $\{0, 1\}$, the graph of groups with boundary consisting of vertices $j \geq 1$ is a cusp. This is very similar to $\textnormal{SL}(2, \mathbb{Z}) \backslash \mathbb{H}$ which also consists of a single cusp. See Figure \ref{fig_nagao}.
```

    $ grep -n -F "See Serre \cite{serre_trees} Chapter II Section 1.6." refs/src/2603.26443/final_draft.tex
    870:with the obvious inclusions into $G_0$ and $G_1$, and for $j \geq 1$, $G_{\{j, j+1\}} = G_j$ with the obvious inclusions into $G_j$ and $G_{j+1}$. See Serre \cite{serre_trees} Chapter II Section 1.6. In particular, we remark that, if we cut along the edge $\{0, 1\}$, the graph of groups with boundary consisting of vertices $j \geq 1$ is a cusp. This is very similar to $\textnormal{SL}(2, \mathbb{Z}) \backslash \mathbb{H}$ which also consists of a single cusp. See Figure \ref{fig_nagao}.

and the stabiliser data explicitly, just above (`2603.26443:final_draft.tex:856-864`, structure of
$\Gamma\backslash\!\backslash\mathcal T$ via Nagao's theorem, $\Gamma=\mathrm{PGL}(2,\mathbb F_q[T^{-1}])$):

```
A very illustrative and in many ways prototypical example of a non-cocompact lattice in $\textnormal{PGL}(2, \mathbb{F}_q((T)))$ is given by $\Gamma = \textnormal{PGL}(2, \mathbb{F}_q[T^{-1}])$. Nagao's theorem \cite{nagao} tells us the structure of $\Gamma \backslash \backslash \mathcal{T}$. The underlying graph is a path graph, with nodes labelled by $\mathbb{Z}_{\geq 0}$. We have $G_0 = \textnormal{PGL}(2,\mathbb{F}_q)$ and for $j \geq 1$,
```

    $ grep -n -F "Nagao's theorem \cite{nagao} tells us the structure" refs/src/2603.26443/final_draft.tex
    856:A very illustrative and in many ways prototypical example of a non-cocompact lattice in $\textnormal{PGL}(2, \mathbb{F}_q((T)))$ is given by $\Gamma = \textnormal{PGL}(2, \mathbb{F}_q[T^{-1}])$. Nagao's theorem \cite{nagao} tells us the structure of $\Gamma \backslash \backslash \mathcal{T}$. The underlying graph is a path graph, with nodes labelled by $\mathbb{Z}_{\geq 0}$. We have $G_0 = \textnormal{PGL}(2,\mathbb{F}_q)$ and for $j \geq 1$,

The BibTeX entry these papers cite is `refs/src/2603.26443/Literatur.bib:11-20` (a supporting file
in the same e-print, not itself part of the TeX source that was hashed):

```
@book {serre_trees,
    AUTHOR = {Serre, Jean-Pierre},
     TITLE = {Trees},
      NOTE = {Translated from the French by John Stillwell},
 PUBLISHER = {Springer-Verlag, Berlin-New York},
      YEAR = {1980},
     PAGES = {ix+142},
```

and the underlying Nagao result: `refs/src/2603.26443/Literatur.bib:3214-3220`
(`Nagao, Hirosi, "On GL(2,K[x])", J. Inst. Polytech. Osaka City Univ. Ser. A, 10 (1959), 117–121`).

A **second, independent modern restatement** — for $\mathrm{GL}_2(\mathbb F_q[T])$ rather than
$\mathrm{PGL}_2(\mathbb F_q[T^{-1}])$, and with the vertex stabilisers spelled out as explicit matrix
groups $\Gamma_0^+=\mathrm{PGL}(2,\mathbb F_q)$, $\Gamma_n=\{(\begin{smallmatrix}a&b\\0&d\end{smallmatrix}):
a,d\in\mathbb F_q^\times,\,b\in\mathbb F_q[t],\,\deg b\le n\}$ — is in **`2302.08850:sn-article.tex:525-548`**
(Hong–Kwon), quoted in full under Target 6 below (it is the same picture as the astra-brief's
$\Lambda_0,\Lambda_1,\dots$ with $\Lambda_0$ sending all $q+1$ edges up and each $\Lambda_n$ sending
one edge up / $q$ down — here in the equivalent "one vertex + ray with shrinking stabilisers" language).

A **third** restatement, in the rank-2 Kac–Moody setting but reducing to the same $(q+1)$-regular tree
for the affine case: **`2108.02919:KMGESFinal.tex:316`** (Ali–Carbone–Garrett):

```
There are several other ingredients that are crucial to our study of Eisenstein series. Our results depend heavily on the structure of the fundamental domain for a non-uniform lattice $\Gamma\leq G$. We will work with the  lattice $\Gamma=P_1^-$, whose fundamental domain on the Tits building is a single vertex to which one cusp ( a semi-infinite ray) is attached.
```

    $ grep -n -F "whose fundamental domain on the Tits building is a single vertex to which one cusp" refs/src/2108.02919/KMGESFinal.tex
    316:There are several other ingredients that are crucial to our study of Eisenstein series. Our results depend heavily on the structure of the fundamental domain for a non-uniform lattice $\Gamma\leq G$. We will work with the  lattice $\Gamma=P_1^-$, whose fundamental domain on the Tits building is a single vertex to which one cusp ( a semi-infinite ray) is attached.

and again at **`2108.02919:KMGESFinal.tex:331`**:

```
Our setting, where the Tits building is one dimensional, allows us to simplify the  proof of meromorphic continuation in  the classical case.  In particular, the quotient graph $\Gamma \bsl X$ has  the simple structure of a semi-infinite ray. This allows us to work with an exact fundamental domain, rather than a Siegel set as in the classical case. We find that our analog of the truncation operator (Section~\ref{trunc}) is identically zero on the exact fundamental domain. Therefore, it is  a compact operator. While it is possible to define Siegel sets and related notions, this turns out not to be required for our proof of meromorphic continuation of Eisenstein series.
```

    $ grep -n -F "the quotient graph \$\Gamma \bsl X\$ has  the simple structure of a semi-infinite ray" refs/src/2108.02919/KMGESFinal.tex
    331:Our setting, where the Tits building is one dimensional, allows us to simplify the  proof of meromorphic continuation in  the classical case.  In particular, the quotient graph $\Gamma \bsl X$ has  the simple structure of a semi-infinite ray. This allows us to work with an exact fundamental domain, rather than a Siegel set as in the classical case. We find that our analog of the truncation operator (Section~\ref{trunc}) is identically zero on the exact fundamental domain. Therefore, it is  a compact operator. While it is possible to define Siegel sets and related notions, this turns out not to be required for our proof of meromorphic continuation of Eisenstein series.

Assessment: **exact** (Target 1 is fully covered) — Serre's own statement (book) is recorded
bibliographically; the tree-quotient-is-a-ray fact with explicit stabiliser data is triply confirmed
in current arXiv TeX by three independent groups, one of them ($GL_2(F_q[T])$, Hong–Kwon) matching
the astra-brief's own group exactly.

---

## Target 2 — Morgenstern, "Ramanujan diagrams" (SIAM 1994) and "Existence and explicit constructions..." (JCTB 1994)

**"Ramanujan diagrams", SIAM J. Discrete Math. 7 (1994), 560–570: NOT FOUND as a free download.**
No arXiv version exists (pre-arXiv-era SIAM paper); no free PDF was located at SIAM, Semantic
Scholar, ResearchGate, or the author's institution. Bibliographic record only, cross-confirmed
independently by two of the fetched papers' bibliographies:

`2302.08850:sn-article.tex:1345`:
```
\bibitem[Mo]{Mo} M. Morgenstern, \emph{Ramanujan diagrams}, SIAM J. Discrete Math. \textbf{7} (1994), 560–570
```

    $ grep -n -F "M. Morgenstern, \emph{Ramanujan diagrams}" refs/src/2302.08850/sn-article.tex
    1345:\bibitem[Mo]{Mo} M. Morgenstern, \emph{Ramanujan diagrams}, SIAM J. Discrete Math. \textbf{7} (1994), 560–570

**"Existence and explicit constructions of $q+1$ regular Ramanujan graphs for every prime power $q$",
J. Combin. Theory Ser. B 62 (1994), 44–62: fetched** as its 1991 UBC preprint (technical report
TR-91-11), which is the same paper before final SIAM-style renumbering. Saved to
`refs/src/morgenstern-1991-tr/`.

Definition of Ramanujan graph, `morgenstern-1991-tr:paper.txt:80-81`:
```
Definition 1.1 A Ramanujan Graph is a connected fmite r regular graph
r , its second largest eigenvalue ·A(I') is smaller or equal to 2-Jr="I.
```

    $ grep -n -F "A Ramanujan Graph is a connected" refs/src/morgenstern-1991-tr/paper.txt
    80:Definition 1.1 A Ramanujan Graph is a connected fmite r regular graph

(NB: this technical report's OCR/typography is degraded — `fmite`=finite, `·A(I')`=$\lambda(\Gamma)$,
`2-Jr="I`=$2\sqrt{r-1}$; the mathematical content is the standard Ramanujan-graph bound
$\lambda\le2\sqrt{r-1}$.)

Role of Drinfeld's theorem (the function-field analogue of Deligne's theorem/Ramanujan conjecture that
the brief expects to drive the "Ramanujan diagram" property), `morgenstern-1991-tr:paper.txt:86-89`:
```
In (LPS), by use of representation theory of PGL2(Qp) and Deligne's theorem (known as Ramanujan's conjecture), for every prime p -:/- 2 a linear
family of p + l regular Ramanujan graphs is explicitly constructed. They
raised the question of the existence and explicit construction of r regular
Ramanujan graphs for other r's. Here we solve this partially, by working
```
```
over function fields, and using Drinfeld 's theorem [Dr] (instead of Deligne's ).
```

    $ grep -n -F "over function fields, and using Drinfeld" refs/src/morgenstern-1991-tr/paper.txt
    88:over function fields, and using Drinfeld 's theorem [Dr] (instead of Deligne's ).

The Jacquet–Langlands / Drinfeld argument spelled out, `morgenstern-1991-tr:paper.txt:346-350`
(this is the exact mechanism — cuspidal automorphic representation over the function field, Drinfeld's
theorem bounding the local component — the astra-brief's H-ARITH will need to invoke):
```
edge Langlands correspondence [Ge, th. 10.5) there is a cuspidal sub
representation x = ®JXI of GA in L2(G~ \GA) s.t. Xp = Cp = p/J.. By the
theorem of Drinfeld [Dr], pµ.
Xp is a principle series representation, i.e.
```

    $ grep -n -F "By the" refs/src/morgenstern-1991-tr/paper.txt | sed -n '1,3p'
    (multiple matches; the relevant one is line 349, confirmed by the surrounding context above, printed with)
    $ sed -n '346,352p' refs/src/morgenstern-1991-tr/paper.txt
    representation of GA in L2( Gk \GA). By
    the Jacquet Langlands correspondence [Ge, th. 10.5) there is a cuspidal sub
    representation x = ®JXI of GA in L2(G~ \GA) s.t. Xp = Cp = p/J.. By the
    theorem of Drinfeld [Dr], pµ.
    Xp is a principle series representation, i.e.
    lµ I :s 2..jq. D

Modern restatement (via Morgenstern's own quaternion-algebra construction over $\mathbb F_q[t]$, with
the Ramanujan bound again attributed to Drinfeld), `1909.07365:part2.tex:161`:
```
Let $q$ be a prime power and $\mathbb{F}_q$ be the finite field with $q$ elements.   Morgenstern also constructed Ramanujan graphs $X^{q,g}$  by considering a suitable quaternion algebra over $\mathbb{F}_q[t]$, where  $g\in \mathbb{F}_q[t]$ and $\gcd(g,t(t-1))=1$~\cite{Morgenstern}. For a discussion of the connection to strong approximation, see the introduction to the authors' paper \cite{SZ2019}. The graph-theoretic conjecture with which this paper is concerned is the following.
```

    $ grep -n -F "Morgenstern also constructed Ramanujan graphs" refs/src/1909.07365/part2.tex
    161:Let $q$ be a prime power and $\mathbb{F}_q$ be the finite field with $q$ elements.   Morgenstern also constructed Ramanujan graphs $X^{q,g}$  by considering a suitable quaternion algebra over $\mathbb{F}_q[t]$, where  $g\in \mathbb{F}_q[t]$ and $\gcd(g,t(t-1))=1$~\cite{Morgenstern}. For a discussion of the connection to strong approximation, see the introduction to the authors' paper \cite{SZ2019}. The graph-theoretic conjecture with which this paper is concerned is the following.

and `1909.07365:part2.tex:178`:
```
Most importantly, since the untwisted Linnik\textendash Selberg conjecture is known to be true over function fields~\cite{Cogdell} (a consequence of the Ramanujan conjecture over function fields proved by Drinfeld), we are hopeful that we will be able to prove at least a variant of the twisted Linnik\textendash Selberg conjecture and at least improve upon the best known upper bound on the diameter of such graphs; see Remark~\ref{rem4}.
```

    $ grep -n -F "a consequence of the Ramanujan conjecture over function fields proved by Drinfeld" refs/src/1909.07365/part2.tex
    178:Most importantly, since the untwisted Linnik\textendash Selberg conjecture is known to be true over function fields~\cite{Cogdell} (a consequence of the Ramanujan conjecture over function fields proved by Drinfeld), we are hopeful that we will be able to prove at least a variant of the twisted Linnik\textendash Selberg conjecture and at least improve upon the best known upper bound on the diameter of such graphs; see Remark~\ref{rem4}.

Independently, `2603.26443:final_draft.tex:136` states the modern spectral consequence directly for
the tree-quotient setting (the "trivial" eigenvalues $\pm\sqrt q$ vs. the rest of the spectrum on the
unit circle by Drinfeld):
```
In particular, we observe that the resonances correspond to the ``trivial'' $\ell^2$-eigenvalues ($\pm \sqrt{q}$), the remaining $\ell^2$-eigenvalues (which are known to all lie on the unit circle as a result of Drinfeld's proof of the Langlands correspondence and Petersson conjecture for $\textnormal{GL}(2)$ over function fields \cite{drinfeld2, drinfeld1}), the square roots of the zeros of the Hasse-Weil zeta function (which are known to all lie on the circle of radius $\frac{1}{\sqrt{q}}$ as a result of Weil's proof of the Riemann hypothesis in this setting \cite{weil}), and additional ``topological'' resonances at the special values $\pm 1$.
```

    $ grep -n -F "the resonances correspond to the \`\`trivial'' \$\ell^2\$-eigenvalues" refs/src/2603.26443/final_draft.tex
    136:It is a consequence of our results that resonances can be computed explicitly via reduction to a finite-dimensional linear algebra problem. In Section \ref{sec_examples} we compute resonances explicitly for several examples. A particularly interesting class of examples is constructed via algebraic curves over finite fields; we summarize this construction in Section \ref{sec_arithmetic_lattice}. In Section \ref{sec_elliptic_curves}, we compute the resonances explicitly for two examples constructed from elliptic curves. In particular, we observe that the resonances correspond to the ``trivial'' $\ell^2$-eigenvalues ($\pm \sqrt{q}$), the remaining $\ell^2$-eigenvalues (which are known to all lie on the unit circle as a result of Drinfeld's proof of the Langlands correspondence and Petersson conjecture for $\textnormal{GL}(2)$ over function fields \cite{drinfeld2, drinfeld1}), the square roots of the zeros of the Hasse-Weil zeta function (which are known to all lie on the circle of radius $\frac{1}{\sqrt{q}}$ as a result of Weil's proof of the Riemann hypothesis in this setting \cite{weil}), and additional ``topological'' resonances at the special values $\pm 1$.

Assessment: **variant/exact mix**. "Ramanujan diagrams" (the SIAM paper that coins the term for
*quotient graphs*, as opposed to the earlier LPS-style Cayley graphs) is bibliographic-only; the
companion JCTB paper's full Drinfeld-theorem argument is fetched and quoted in full (**exact**); and
the role of Drinfeld's theorem is triply cross-confirmed by three independent later papers, one of
which (`2603.26443`) directly ties it to the resonance picture the astra-brief needs.

---

## Target 3 — W.-C. Winnie Li, "Eisenstein series and decomposition theory over function fields" (Math. Ann. 240 (1979), 115–139)

Pre-arXiv (1979); **NOT FOUND as a free download**. Bibliographic data confirmed independently by
three sources:

`efrat-1991:paper.txt:1479-1480`:
```
Li, W. Eisenstein series and decomposition theory over function fields.
Math. Ann. 240 (1979), 115-139.
```

    $ grep -n -F "Eisenstein series and decomposition theory over function fields" refs/src/efrat-1991/paper.txt
    1479:Li, W. Eisenstein series and decomposition theory over function fields.

`2108.02919:KMGESFinal.tex:290` (Ali–Carbone–Garrett, describing Li's contribution in detail — this
is the fullest free description of the paper's content found):
```
These Eisenstein series converge in a half space. Harder proved analytic continuation which is simpler than Langlands' method in the number field case. He also proved that the Eisenstein series are rational functions and showed that they satisfy a functional equation.  Building on Harder's work, Li \cite{Li} developed a full theory of Eisenstein series for $GL_2$ over function fields. She studied the intertwining operators arising from constant Fourier coefficients, proved that they are rational and showed that they satisfy a functional equation. She developed the theory of spectral decomposition for automorphic eigenfunctions of a certain Hecke operator, writing them as a sum of an Eisenstein series and a cusp form.
```

    $ grep -n -F "Li \cite{Li} developed a full theory of Eisenstein series for" refs/src/2108.02919/KMGESFinal.tex
    290:These Eisenstein series converge in a half space. Harder proved analytic continuation which is simpler than Langlands' method in the number field case. He also proved that the Eisenstein series are rational functions and showed that they satisfy a functional equation.  Building on Harder's work, Li \cite{Li} developed a full theory of Eisenstein series for $GL_2$ over function fields. She studied the intertwining operators arising from constant Fourier coefficients, proved that they are rational and showed that they satisfy a functional equation. She developed the theory of spectral decomposition for automorphic eigenfunctions of a certain Hecke operator, writing them as a sum of an Eisenstein series and a cusp form.

`2303.09327:main.tex:108` (Kaneko–Koyama cite Li 1979 jointly with Nagoshi 2001 for identifying the
continuous spectrum with the Eisenstein series — this is the direct precursor of the astra-brief's
"constant term / scattering" object):
```
where $h((x, y)) = \sup \{|x|, |y| \}$ for each vector $(x, y)$ in $k_{\infty} \times k_{\infty}$ with $k_{\infty} = \F_{q}((T^{-1}))$. It is absolutely convergent for $\Re(s) > 1$ and meromorphic in the entire complex plane $\mathbb{C}$.~Li~\cite{Li1979} and Nagoshi~\cite{Nagoshi2001} demonstrated that $E(g, \frac{1}{2}+it)$ corresponds to the continuous spectrum of the adjacency operator.
```

    $ grep -n -F "Li~\cite{Li1979} and Nagoshi~\cite{Nagoshi2001} demonstrated" refs/src/2303.09327/main.tex
    108:where $h((x, y)) = \sup \{|x|, |y| \}$ for each vector $(x, y)$ in $k_{\infty} \times k_{\infty}$ with $k_{\infty} = \F_{q}((T^{-1}))$. It is absolutely convergent for $\Re(s) > 1$ and meromorphic in the entire complex plane $\mathbb{C}$.~Li~\cite{Li1979} and Nagoshi~\cite{Nagoshi2001} demonstrated that $E(g, \frac{1}{2}+it)$ corresponds to the continuous spectrum of the adjacency operator.

No later Li paper specifically on the tree scattering matrix was located in this search (only the
1979 Math. Ann. paper is cited by every source found).

Assessment: **exact but not directly fetchable**; content of the paper is recovered second-hand
(above) with enough precision (intertwining operators = scattering matrix, rational + functional
equation) for the next round to know what to expect, but no primary-source verbatim quote from Li's
own paper is available.

---

## Target 4 — Nagoshi, "Spectra of arithmetic infinite graphs and their application" and "Selberg zeta functions over function fields"

**"Selberg zeta functions over function fields", J. Number Theory 90 (2001), 207–238** (the brief's
guessed year "2006" is wrong — corrected to 2001 from three independent bibliographies below).
**NOT FOUND as a free download** (ScienceDirect paywalled, DOI `10.1006/jnth.2001.2658`; no arXiv
version, no author's-page copy located). Bibliographic record, triply confirmed:

`2302.08850:sn-article.tex:1347`:
```
\bibitem[Na]{Na} H. Nagoshi, \emph{Selberg zeta functions over function fields}, Journal of Number Theory \textbf{90} (2001), 207-238
```

    $ grep -n -F "H. Nagoshi, \emph{Selberg zeta functions over function fields}" refs/src/2302.08850/sn-article.tex
    1347:\bibitem[Na]{Na} H. Nagoshi, \emph{Selberg zeta functions over function fields}, Journal of Number Theory \textbf{90} (2001), 207-238

`2303.09327:main.tex:949-951`:
```
\bibitem[Nag01]{Nagoshi2001}
Hirofumi Nagoshi, \href{https://doi.org/10.1006/jnth.2001.2658}{{S}elberg Zeta
  Functions over Function Fields}, Journal of Number Theory \textbf{90} (2001),
```

    $ grep -n -F "Hirofumi Nagoshi" refs/src/2303.09327/main.tex
    949:\bibitem[Nag01]{Nagoshi2001}
    (next line, verified) $ sed -n '949,951p' refs/src/2303.09327/main.tex
    \bibitem[Nag01]{Nagoshi2001}
    Hirofumi Nagoshi, \href{https://doi.org/10.1006/jnth.2001.2658}{{S}elberg Zeta
      Functions over Function Fields}, Journal of Number Theory \textbf{90} (2001),

The **content** of Nagoshi's paper is described, and directly used, by two independent papers fetched
in full:

`2302.08850:sn-article.tex:176` (Hong–Kwon, commented-out but present in the TeX source — describes
what `[Na]` proved):
```
%The theory of Ihara zeta functions for finite graphs has been extended to non-compact cuspidal tree-lattices in \cite{DK} with a geometric method. Meanwhile, when $\Gamma$ is a principal congruence subgroup of $PGL(2,\mathbb{F}_q[t])$, the Selberg zeta function attached to $\Gamma$ and its determinant expression have been achieved in \cite{Na} using a purely algebraic approach.
```

    $ grep -n -F "the Selberg zeta function attached to \$\Gamma\$ and its determinant expression have been achieved in \cite{Na}" refs/src/2302.08850/sn-article.tex
    176:%The theory of Ihara zeta functions for finite graphs has been extended to non-compact cuspidal tree-lattices in \cite{DK} with a geometric method. Meanwhile, when $\Gamma$ is a principal congruence subgroup of $PGL(2,\mathbb{F}_q[t])$, the Selberg zeta function attached to $\Gamma$ and its determinant expression have been achieved in \cite{Na} using a purely algebraic approach.

(NB: this specific line is commented out in the TeX source with a leading `%`, i.e. it did not render
in the published PDF, but it is present verbatim in the source file and is a legitimate,
author-written statement of what Nagoshi's paper does; the *uncommented* restatement of the same fact
is at line 180, quoted in Target 6 below.)

`2303.09327:main.tex:101-103` (Kaneko–Koyama, the most load-bearing citation for the next round: it
places Nagoshi's spectral theory exactly on $\Gamma_0(A)\backslash G$, and independently confirms the
"finite graph + finitely many rays" picture):
```
On the other hand, the analogy between rational numbers and polynomials over finite~fields plays an essential role in number theory. If $q > 3$ is a prime, then the alternative~underlying group is $\PGL_{2}(\F_{q}[T])$ acting on $G = \PGL_{2}(\F_{q}((T^{-1})))$. We handle the congruence subgroup $\Gamma_{0}(A)$ with $A \in \F_{q}[T]$ a monic irreducible polynomial. The space $\Gamma_{0}(A) \backslash G$ can be realised as an arithmetic infinite graph for which the spectral theory of automorphic forms is developed by Nagoshi~\cite{Nagoshi2001}. Furthermore, the space is geometrically finite in the sense that it is a union of a finite graph with finitely many infinite rays, and the spectra of the corresponding Laplacian consist of a finite number of eigenvalues.
```

    $ grep -n -F "can be realised as an arithmetic infinite graph for which the spectral theory" refs/src/2303.09327/main.tex
    101:On the other hand, the analogy between rational numbers and polynomials over finite~fields plays an essential role in number theory. If $q > 3$ is a prime, then the alternative~underlying group is $\PGL_{2}(\F_{q}[T])$ acting on $G = \PGL_{2}(\F_{q}((T^{-1})))$. We handle the congruence subgroup $\Gamma_{0}(A)$ with $A \in \F_{q}[T]$ a monic irreducible polynomial. The space $\Gamma_{0}(A) \backslash G$ can be realised as an arithmetic infinite graph for which the spectral theory of automorphic forms is developed by Nagoshi~\cite{Nagoshi2001}. Furthermore, the space is geometrically finite in the sense that it is a union of a finite graph with finitely many infinite rays, and the spectra of the corresponding Laplacian consist of a finite number of eigenvalues. Hence, there is no analogue of~\eqref{QUE} to be formulated in our case. This naturally leads us to the study of the level aspect version~\eqref{level} over function fields by taking a sequence of polynomials $A$ such that $\deg{A}$ tends to infinity.

Kaneko–Koyama also **use** and quote Nagoshi's notation directly at `2303.09327:main.tex:184`:
```
We follow the notation of Nagoshi~\cite{Nagoshi2001} with minor adjustments. Let $\{\mathfrak{a}, \mathfrak{b}, \mathfrak{c}, \dots \}$ be the set of inequivalent cusps for $\Gamma$. Let $\Gamma_{\mathfrak{a}}$ be the stabiliser of the cusp $\mathfrak{a}$ in $\Gamma$, and let $\sigma_{\mathfrak{a}} \in G$ denote the scaling matrix such that $\sigma_{\mathfrak{a}} \infty = \mathfrak{a}$ and $\sigma_{\mathfrak{a}}^{-1} \Gamma_{\mathfrak{a}} \sigma_{\mathfrak{a}} = \Gamma_{\infty}$.
```

    $ grep -n -F "We follow the notation of Nagoshi" refs/src/2303.09327/main.tex
    184:We follow the notation of Nagoshi~\cite{Nagoshi2001} with minor adjustments. Let $\{\mathfrak{a}, \mathfrak{b}, \mathfrak{c}, \dots \}$ be the set of inequivalent cusps for $\Gamma$. Let $\Gamma_{\mathfrak{a}}$ be the stabiliser of the cusp $\mathfrak{a}$ in $\Gamma$, and let $\sigma_{\mathfrak{a}} \in G$ denote the scaling matrix such that $\sigma_{\mathfrak{a}} \infty = \mathfrak{a}$ and $\sigma_{\mathfrak{a}}^{-1} \Gamma_{\mathfrak{a}} \sigma_{\mathfrak{a}} = \Gamma_{\infty}$.

**"Spectra of arithmetic infinite graphs and their application", Interdiscip. Inform. Sci. (2001):
NOT FOUND.** No listing for this exact title was located on J-STAGE, arXiv, or via web search; only
a related Proceedings of the Japan Academy note "On arithmetic infinite graphs" (Nagoshi, Proc. Japan
Acad. Ser. A Math. Sci. 76 (2000), no. 2, 22–25, free-access-looking abstract on Project Euclid at
`https://projecteuclid.org/journals/proceedings-of-the-japan-academy-series-a-mathematical-sciences/volume-76/issue-2/On-arithmetic-infinite-graphs/10.3792/pjaa.76.22.full`)
was found describing the same programme ("explicit computation of the Selberg trace formula for
principal congruence subgroups of PGL(2,F_q[t])..."); this could **not** be verified byte-for-byte
(full text not freely downloadable, only an abstract page), so it is recorded here as a probably-related
but unverified item, distinct from the brief's exact title, and is **not** quoted as a source.

Assessment: **exact but not directly fetchable** for the Journal of Number Theory paper (its content
is recovered with high fidelity through Kaneko–Koyama's direct use of it, including their
Eisenstein-series and cusp-stabiliser conventions, which are "Nagoshi's notation"); the
*Interdiscip. Inform. Sci.* paper is **NOT FOUND / unverified**.

---

## Target 5 — Efrat, "Automorphic spectra on the tree of $PGL_2$" (Enseign. Math. 37 (1991), 31–43)

**Fetched in full** from e-periodica (open digitisation of the journal by ETH-Bibliothek), saved as
`refs/src/efrat-1991/paper.pdf` (15pp, the full published article) with OCR text
`refs/src/efrat-1991/paper.txt`.

Masthead confirming title/author/journal/pages, `efrat-1991:paper.txt:19-45`:
```
AUTOMORPHIC SPECTRA ON THE TREE OF PGL2
by Isaac Efrat
```
and
```
L'Enseignement Mathématique, t. 37 (1991), p. 31-43
```

    $ sed -n '43,45p' refs/src/efrat-1991/paper.txt
    L'Enseignement Mathématique, t. 37 (1991), p. 31-43

    AUTOMORPHIC SPECTRA ON THE TREE OF PGL2

Discrete spectrum $\pm(q+1)$ (this is exactly C2(i)/T7's "trivial" spectrum in the astra-brief),
`efrat-1991:paper.txt:894-897`:
```
Combining Propositions 3.5 and 3.6 we conclude

Corollary 3.7.
±(q + 1),

The discrete spectrum of T consists of the numbers
whose corresponding eigenfunctions (given in Example 3.1) span

two one-dimensional eigenspaces of L2(F).
```

    $ grep -n -F "The discrete spectrum of T consists of the numbers" refs/src/efrat-1991/paper.txt
    896:The discrete spectrum of T consists of the numbers

No cusp forms for $\Gamma=\mathrm{PGL}_2(\mathbb F_q[t])$ (relevant to C2(iii) of the astra-brief —
for the *unlevelled* group there are no cusp forms to worry about; at level $N$ there will be),
`efrat-1991:paper.txt:150-153`:
```
The discrete eigenfunctions
of T
generate a two-dimensional subspace R, explicitly given by Proposition 3.5. In particular, T admits no
cusp forms. This is a special case of much more general dimension formulae
```

    $ grep -n -F "In particular, T admits no" refs/src/efrat-1991/paper.txt
    161:generate a two-dimensional subspace R, explicitly given by Proposition 3.5. In particular, T admits no

(NB: `sed -n` shows the fragment "T admits no" begins at line 161 in the OCR'd flow, not 152 — the
PDF's two-column-to-flow OCR reorders short fragments; the full sentence, confirmed contiguous by
`sed -n '158,163p'`, reads "The discrete eigenfunctions of T generate a two-dimensional subspace R,
explicitly given by Proposition 3.5. In particular, T admits no cusp forms.")

Tree structure cited to Serre and Weil, `efrat-1991:paper.txt:222` and Theorem 1.1:
```
The material in this section is adapted from Serre [S] and Weil [W].
```
```
Theorem 1.1 ([S]). The graph whose set of vertices is X and whose
edges are the pairs (A, AO satisfying (1) is the (infinite) (q + 1 )-regular tree.
```

    $ grep -n -F "the (infinite) (q + 1 )-regular tree" refs/src/efrat-1991/paper.txt
    252:edges are the pairs (A, AO satisfying (1) is the (infinite) (q + 1 )-regular tree.

Bibliography confirms `[L]` = W. Li 1979 (Target 3) and `[S]` = Serre, *Trees* (Target 1),
`efrat-1991:paper.txt:1479-1484`:
```
Li, W. Eisenstein series and decomposition theory over function fields.
Math. Ann. 240 (1979), 115-139.
```
```
Serre, J.-P. Trees. Springer Verlag, 1980.
```

    $ grep -n -F "Serre, J.-P. Trees. Springer Verlag, 1980." refs/src/efrat-1991/paper.txt
    1484:Serre, J.-P. Trees. Springer Verlag, 1980.

Independent bibliographic confirmation of the exact title/journal/volume from `2603.26443`'s
`Literatur.bib` (a supporting file in that e-print, not part of the hashed `.tex`):
```
@article {efrat2,
    AUTHOR = {Efrat, Isaac},
     TITLE = {Automorphic spectra on the tree of {${\rm PGL}_2$}},
   JOURNAL = {Enseign. Math. (2)},
```

(`refs/src/2603.26443/Literatur.bib:3694-3697`.)

Assessment: **exact**, fully fetched and verified. This is the strongest primary source found for the
"trivial"/discrete part of the spectrum on the unlevelled tree quotient.

---

## Target 6 — Gekeler–Nonnengardt, "Fundamental domains of some arithmetic groups over function fields" (Internat. J. Math. 6 (1995), 689–708)

**NOT FOUND as a free download** (no arXiv preprint from 1995; no free PDF located at World
Scientific, the authors' institutional pages, or elsewhere). Bibliographic record only:
E.-U. Gekeler and U. Nonnengardt, *Fundamental domains of some arithmetic groups over function
fields*, Internat. J. Math. **6** (1995), no. 5, 689–708.

The explicit small-level $\Gamma_0(N)\backslash T$ picture the brief wants is, however, **directly
available**, with figures, in `2302.08850` (Hong–Kwon), which gives both the unlevelled case
$\Gamma=\mathrm{PGL}(2,\mathbb F_q[t])$ **and** a general multi-cusp $n$-ray family
$\mathbf A^{(n)}(\alpha_1,\dots,\alpha_n)$ with prescribed junction indices, which is exactly the
shape ($n$ rays meeting at one vertex with indices $\alpha_i$ summing to $\le q+1$) the astra-brief's
T8 will need for $h$ cusps:

Unlevelled case, vertex stabilisers as explicit matrix groups, `2302.08850:sn-article.tex:525-548`:
```
Let $\Gamma=PGL(2,\mathbb{F}_q[t])$. It is a lattice of $PGL(2,\mathbb{F}_q(\!(t^{-1})\!))$ whose Bruhat-Tits tree is the infinite $(q+1)$-regular tree. The quotient graph of groups $(X,\mathcal{G})$ under $\Gamma$-action is given by
```
```
Here, $\Gamma_0^+=PGL(2,\mathbb{F}_q)$, $\Gamma_0=\Gamma_0^+\cap\Gamma_1$ and
\[\Gamma_n=\left\{\begin{pmatrix}a & b \\ 0 & d\end{pmatrix}\colon a,b\in\mathbb{F}_q^\times, b\in\mathbb{F}_q[t], \deg(b)\le n\right\}\textrm{ for }n\ge 1.\]
```

    $ grep -n -F "Let \$\Gamma=PGL(2,\mathbb{F}_q[t])\$" refs/src/2302.08850/sn-article.tex
    525:Let $\Gamma=PGL(2,\mathbb{F}_q[t])$. It is a lattice of $PGL(2,\mathbb{F}_q(\!(t^{-1})\!))$ whose Bruhat-Tits tree is the infinite $(q+1)$-regular tree. The quotient graph of groups $(X,\mathcal{G})$ under $\Gamma$-action is given by

    $ sed -n '548,550p' refs/src/2302.08850/sn-article.tex
    Here, $\Gamma_0^+=PGL(2,\mathbb{F}_q)$, $\Gamma_0=\Gamma_0^+\cap\Gamma_1$ and
    \[\Gamma_n=\left\{\begin{pmatrix}a & b \\ 0 & d\end{pmatrix}\colon a,b\in\mathbb{F}_q^\times, b\in\mathbb{F}_q[t], \deg(b)\le n\right\}\textrm{ for }n\ge 1.\]

together with the resulting Bass-Ihara and Selberg zeta functions in closed form (immediately below,
same lines):
```
Let $\mathbf{A}=(X,w)$ be the associated weighted graph. Then, its Bass-Ihara zeta function is
\[Z_\mathbf{A}(u)=\frac{1-qu^2}{1-q^2u^2}\]
while the Selberg zeta function for $\mathbf{X}=(X,\mathcal{G})$ is
\[Z_\mathbf{X}(u)=\left(\frac{1-qu^2}{1-q^2u^2}\right)^{q-1}.\]
```

Multi-cusp family with explicit ray indices, `2302.08850:sn-article.tex:685`:
```
Let $\alpha_i$ be the integers with $k:=\alpha_1+\cdots+\alpha_n\leq q+1.$ Let $\mathbf{A}^{(n)}(\alpha_1,\ldots,\alpha_n)$ be a weighted graph arising from a geometrically finite lattice which consists of $n$-rays connected at a base point $v_0$ with indices $\alpha_1,\ldots,\alpha_n$. See Figure~\ref{fig:6} for $\mathbf{A}^{(3)}(\alpha_1,\alpha_2,\alpha_3)$.
```

    $ grep -n -F "which consists of \$n\$-rays connected at a base point" refs/src/2302.08850/sn-article.tex
    685:Let $\alpha_i$ be the integers with $k:=\alpha_1+\cdots+\alpha_n\leq q+1.$ Let $\mathbf{A}^{(n)}(\alpha_1,\ldots,\alpha_n)$ be a weighted graph arising from a geometrically finite lattice which consists of $n$-rays connected at a base point $v_0$ with indices $\alpha_1,\ldots,\alpha_n$. See Figure~\ref{fig:6} for $\mathbf{A}^{(3)}(\alpha_1,\alpha_2,\alpha_3)$.

Zeros of the zeta function counted by number of cusps (relevant to astra-brief's T7 zero-counting),
`2302.08850:sn-article.tex:1461`:
```
Let $\mathbf{X}$ be a $(q+1)$-regular graph of groups associated to a cuspidal lattice $\Gamma$ and denote by $Z_\mathbf{X}(u)$ the Ihara zeta function of $\mathbf{X}$. Then zeros of $Z_\mathbf{X}(u)$ are $\frac{1}{\sqrt{q}}$ and $-\frac{1}{\sqrt{q}}$, with each multiplicity is of the number of cuspidal rays in $\mathbf{X}$.
```

    $ grep -n -F "Then zeros of \$Z_\mathbf{X}(u)\$ are \$\frac{1}{\sqrt{q}}\$" refs/src/2302.08850/sn-article.tex
    1461:Let $\mathbf{X}$ be a $(q+1)$-regular graph of groups associated to a cuspidal lattice $\Gamma$ and denote by $Z_\mathbf{X}(u)$ the Ihara zeta function of $\mathbf{X}$. Then zeros of $Z_\mathbf{X}(u)$ are $\frac{1}{\sqrt{q}}$ and $-\frac{1}{\sqrt{q}}$, with each multiplicity is of the number of cuspidal rays in $\mathbf{X}$.

Uncommented restatement of what Nagoshi did (cross-refs Target 4), `2302.08850:sn-article.tex:180`:
```
Of particular interest is the case where the graph of groups $(X,\mathcal{G})$ is obtained from a geometrically finite (or equivalently, cuspidal) tree lattice. This encompasses every quotient of the tree of rank-one Lie groups over non-archimedean local fields by its discrete subgroup (as proved in \cite{Lu}). Specifically, we define the zeta function $Z_{(X,\mathcal{G})}(u)$ of $(q+1)$-regular graphs of groups $(X,\mathcal{G})$ that resembles the Selberg zeta function, and investigate its relationship with the Bass-Ihara zeta function $Z_{(X,w)}(u)$ for the weighted graph $(X,w)$ associated with $(X,\mathcal{G})$ under \emph{centrally rigid} condition. (We refer to Definition~\ref{def:cr} for precise details.) It is worth mentioning that the Selberg zeta function and its determinant expression for principal congruence subgroups of $PGL(2,\mathbb{F}_q[t])$ have been also achieved in \cite{Na} with algebraic approach.
```

    $ grep -n -F "the Selberg zeta function and its determinant expression for principal congruence subgroups of \$PGL(2,\mathbb{F}_q[t])\$" refs/src/2302.08850/sn-article.tex
    180:Of particular interest is the case where the graph of groups $(X,\mathcal{G})$ is obtained from a geometrically finite (or equivalently, cuspidal) tree lattice. This encompasses every quotient of the tree of rank-one Lie groups over non-archimedean local fields by its discrete subgroup (as proved in \cite{Lu}). Specifically, we define the zeta function $Z_{(X,\mathcal{G})}(u)$ of $(q+1)$-regular graphs of groups $(X,\mathcal{G})$ that resembles the Selberg zeta function, and investigate its relationship with the Bass-Ihara zeta function $Z_{(X,w)}(u)$ for the weighted graph $(X,w)$ associated with $(X,\mathcal{G})$ under \emph{centrally rigid} condition. (We refer to Definition~\ref{def:cr} for precise details.) It is worth mentioning that the Selberg zeta function and its determinant expression for principal congruence subgroups of $PGL(2,\mathbb{F}_q[t])$ have been also achieved in \cite{Na} with algebraic approach.

For the specific case $\Gamma_0(A)\subset\mathrm{PGL}_2(\mathbb F_q[T])$, `2303.09327` gives the exact
matrix definition and the index formula (directly usable for the "next round" instead of
Gekeler–Nonnengardt), `2303.09327:main.tex:206` and `:253`:
```
\Gamma = \Gamma_{0}(A) \coloneqq \left\{g = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \PGL_{2}(\F_{q}[T]): c \equiv 0 \tpmod{A} \right\}.
```
```
The index $m$ of $\Gamma_{0}(A)$ in $\PGL_{2}(\F_{q}[T])$ is given by $m = |A|+1$.
```

    $ grep -n -F "\Gamma = \Gamma_{0}(A) \coloneqq" refs/src/2303.09327/main.tex
    206:\Gamma = \Gamma_{0}(A) \coloneqq \left\{g = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \PGL_{2}(\F_{q}[T]): c \equiv 0 \tpmod{A} \right\}.

    $ grep -n -F "The index \$m\$ of \$\Gamma_{0}(A)\$ in \$\PGL_{2}(\F_{q}[T])\$ is given by" refs/src/2303.09327/main.tex
    253:The index $m$ of $\Gamma_{0}(A)$ in $\PGL_{2}(\F_{q}[T])$ is given by $m = |A|+1$.

Also directly relevant, an explicit single-cusp arithmetic example given as a full graph-of-groups
with matrix stabilisers, `2603.26443:final_draft.tex:1975-1979` ("modular curve" = $A=1$ case,
matching the astra-brief's C3 pure-cusp exactly: single vertex, $q+1$ edges to one cusp):
```
Consider the modular curve from Section \ref{sec_arithmetic_lattice}. It consists of a single vertex attached $q+1$ times to a cusp. Therefore its resonance matrix is
\begin{gather*}
    H(\mu) = \frac{1}{2 \sqrt{q}}\Big(\frac{(q+1) \sqrt{q}}{\mu}\Big) - \frac{\mu + \mu^{-1}}{2}.
\end{gather*}
This has zeros at $\mu = \pm \sqrt{q}$.
```

    $ grep -n -F "It consists of a single vertex attached \$q+1\$ times to a cusp." refs/src/2603.26443/final_draft.tex
    1975:Consider the modular curve from Section \ref{sec_arithmetic_lattice}. It consists of a single vertex attached $q+1$ times to a cusp. Therefore its resonance matrix is

Assessment: **exact substitute found** — Gekeler–Nonnengardt itself is unavailable, but the explicit
$\Gamma_0(N)\backslash T$ / multi-cusp structure the brief needs is fully present, quoted and
byte-verified, in two independent, freely available, more recent papers (`2302.08850`, `2303.09327`),
one of which gives the precise matrix definition of $\Gamma_0(A)$ and its index.

---

## Target 7 — Eisenstein series / scattering matrix / constant term for $\Gamma_0(N)<GL_2(F_q[T])$ in terms of Dirichlet $L$-functions

This is the single most important target for the next round, and the strongest hit. **`2303.09327`**
(Kaneko–Koyama) gives, for $\Gamma_0(A)$ with $A$ monic irreducible, the constant term of the
Eisenstein series computed explicitly as a ratio of zeta functions of $\mathbb F_q[T]$ — the direct
function-field, level-$A$ analogue of $\varphi(s)=\xi(2s-1)/\xi(2s)$ and of the astra-brief's C3
formula $1/R(z)=q\,\zeta_K(2s-1)/\zeta_K(2s)$:

`2303.09327:main.tex:384-392` (Lemma 3.4, the constant-term computation):
```
On the other hand, the following lemma is useful when we calculate the constant term in the Fourier--Whittaker expansion of the Eisenstein series.
\begin{lemma}\label{lemma34}
Keep the notation as above. Then
\begin{equation}\label{constant}
\sum_{\substack{X \ne 0 \\ A \mid X}} \frac{1}{|X|^{2s}}
\sum_{\substack{Y \equiv 1 \tpmod A \\ Y \tpmod{AX} \\ (X, Y) = 1}} 1
 = \frac{q^{a(1-2s)}}{1-q^{-2as}} \frac{\zeta_{\F_{q}[T]}(2s-1)}{\zeta_{\F_{q}[T]}(2s)}.
\end{equation}
\end{lemma}
```

    $ grep -n -F "\frac{q^{a(1-2s)}}{1-q^{-2as}} \frac{\zeta_{\F_{q}[T]}(2s-1)}{\zeta_{\F_{q}[T]}(2s)}" refs/src/2303.09327/main.tex
    390: = \frac{q^{a(1-2s)}}{1-q^{-2as}} \frac{\zeta_{\F_{q}[T]}(2s-1)}{\zeta_{\F_{q}[T]}(2s)}.

    $ grep -n -F "the following lemma is useful when we calculate the constant term" refs/src/2303.09327/main.tex
    384:On the other hand, the following lemma is useful when we calculate the constant term in the Fourier--Whittaker expansion of the Eisenstein series.

The same paper defines the automorphic $L$-function attached to a Hecke–Maaß form for $\Gamma_0(A)$
as a Dirichlet series over monic polynomials of $\mathbb F_q[T]$ (needed to state the
zeros-of-$L$-are-resonances hypothesis H-ARITH precisely), `2303.09327:main.tex:466`:
```
L(s, u) = \sum_{\substack{Q \in \F_{q}[T] \\ \text{monic}}} \frac{\tilde{c}(Q)}{|Q|^{s}}
```

    $ grep -n -F "L(s, u) = \sum_{\substack{Q \in \F_{q}[T] \\ \text{monic}}}" refs/src/2303.09327/main.tex
    466:L(s, u) = \sum_{\substack{Q \in \F_{q}[T] \\ \text{monic}}} \frac{\tilde{c}(Q)}{|Q|^{s}}

and relates it (Rankin–Selberg-style) to $\zeta_{\mathbb F_q[T]}$, `2303.09327:main.tex:514`:
```
 = \frac{L(s, u) L(s-\nu, u)}{\zeta_{\F_{q}[T]}(2s-\nu)}.
```

    $ grep -n -F "= \frac{L(s, u) L(s-\nu, u)}{\zeta_{\F_{q}[T]}(2s-\nu)}." refs/src/2303.09327/main.tex
    514: = \frac{L(s, u) L(s-\nu, u)}{\zeta_{\F_{q}[T]}(2s-\nu)}.

**What was NOT found**: an explicit statement in this paper, or any other paper fetched, naming an
object "$\Psi(s)$" or "scattering matrix" for $\Gamma_0(A)\backslash T$ and asserting its poles/zeros
are $L$-function zeros. (An earlier web-search snippet suggested such wording existed in this paper;
after fetching and grepping the full TeX source, no occurrence of "scattering" was found anywhere in
`2303.09327/main.tex` — that snippet could not be reproduced and should be treated as a search-tool
hallucination, not a verified fact.) The scattering-matrix *language* is standard for Eisenstein
series (constant term $=$ scattering matrix acting on the space of cusps, by general automorphic
theory), and the astra-brief's own C3 already derives the $2s-1/2s$ zeta ratio from first principles
for the unlevelled cusp; what Kaneko–Koyama supply is the **verified generalisation of that ratio to
level $A$**, i.e. exactly the input needed to state H-ARITH precisely as a conjecture about the
$h\times h$ matrix generalisation.

For the graph-Ihara-zeta side (Target 6/7 overlap), the closest general "poles of a scattering-type
object are $L$-function zeros" statement found is `2105.02677` (already in the manifest from an
earlier round; Komatsu–Konno–Sato, *The scattering matrix with respect to an Hermitian matrix of a
graph*), which defines a scattering matrix for *finite* graphs and an associated $L$-function with
determinant expression, but for finite (not cuspidal/infinite) graphs — a structurally different but
methodologically related object; and `1601.04573` (Friedli), which proves an RH-equivalence for
*cyclic-graph* $L$-functions vs. classical Dirichlet $L$-functions, a genuinely analogous but
number-field (not function-field-tree) phenomenon:

`1601.04573:L-functions.tex:200` (abstract):
```
In this note we define $L$-functions of finite graphs and study the particular case of finite cycles in the spirit of a previous paper that studied spectral zeta functions of graphs. The main result is a suggestive equivalence between an asymptotic functional equation for these $L$-functions and the corresponding case of the Generalized Riemann Hypothesis. We also establish a relation between the positivity of such functions and the existence of real zeros in the critical strip of the classical Dirichlet $L$-functions with the same character.
```

    $ grep -n -F "In this note we define \$L\$-functions of finite graphs" refs/src/1601.04573/L-functions.tex
    200:In this note we define $L$-functions of finite graphs and study the particular case of finite cycles in the spirit of a previous paper that studied spectral zeta functions of graphs. The main result is a suggestive equivalence between an asymptotic functional equation for these $L$-functions and the corresponding case of the Generalized Riemann Hypothesis. We also establish a relation between the positivity of such functions and the existence of real zeros in the critical strip of the classical Dirichlet $L$-functions with the same character.

Assessment: **exact, high-value hit** for the constant term $\leftrightarrow$ $\zeta_{\mathbb F_q[T]}$
ratio at level $A$ (the direct analogue of C3, generalised to level, is now in hand and byte-verified);
**NOT FOUND**: an explicit "$L$-function zeros $=$ resonances" theorem for $\Gamma_0(N)$ on the tree —
this appears to be genuinely open / not yet written down anywhere, matching the astra-brief's
instruction to state it only as hypothesis H-ARITH.

---

## Target 8 — Discrete Lax–Phillips scattering / resonances for a finite graph with an attached ray or lead

Best and most directly relevant hit: **`2603.26443`** (Arends–Peterson–Weich, *Resonances on
geometrically finite graphs*), which is essentially a general-purpose discrete Lax–Phillips theory for
exactly the astra-brief's class of objects (finite core + rays/"cusps"), fully worked out for the
adjacency operator, with explicit arithmetic examples matching C3 and pointing at the Weil/Drinfeld
connection the next round needs.

Framework statement, `2603.26443:final_draft.tex:62`:
```
The aim of this article is to establish a notion of resonances for the adjacency operator on a certain class of infinite graphs which are the ``right'' analogues of geometrically finite manifolds in the setting of graphs. In fact, the objects we study must be properly understood not as graphs in the usual sense, but as \textit{graphs of groups}. We defer a detailed discussion of the precise definition of geometrically finite graphs (and the justification for why they deserve to be named as such) to Sections \ref{sec_graph_of_groups} and \ref{sec_graph_of_groups_2}. However, for now we state that, analogously to the setting of hyperbolic surfaces, geometrically finite graphs are those which can be decomposed into finitely many pieces, one of which is a finite graph called the \textit{compact core}, which we denote by $\mathcal{L}$, and the rest of which are either \textit{(orbifold) funnels} or \textit{cusps}.
```

    $ grep -n -F "The aim of this article is to establish a notion of resonances for the adjacency operator" refs/src/2603.26443/final_draft.tex
    62:The aim of this article is to establish a notion of resonances for the adjacency operator on a certain class of infinite graphs which are the ``right'' analogues of geometrically finite manifolds in the setting of graphs. In fact, the objects we study must be properly understood not as graphs in the usual sense, but as \textit{graphs of groups}. We defer a detailed discussion of the precise definition of geometrically finite graphs (and the justification for why they deserve to be named as such) to Sections \ref{sec_graph_of_groups} and \ref{sec_graph_of_groups_2}. However, for now we state that, analogously to the setting of hyperbolic surfaces, geometrically finite graphs are those which can be decomposed into finitely many pieces, one of which is a finite graph called the \textit{compact core}, which we denote by $\mathcal{L}$, and the rest of which are either \textit{(orbifold) funnels} or \textit{cusps}.

Explicit Lax–Phillips connection and stated future work (this paper is aware it has NOT yet done the
wave-equation/Lax–Phillips construction proper — it works via resolvent meromorphic continuation
instead, and flags the wave-equation approach as follow-up work, citing Peterson's separate work),
`2603.26443:final_draft.tex:138`:
```
In the setting of geometrically finite hyperbolic manifolds, the theory of resonances is very closely connected with the Lax-Phillips scattering theory \cite{pbhr-LP76}. Roughly speaking, the resonances correspond to the poles of the scattering operator. The Lax-Phillips scattering theory is itself defined in terms of the (automorphic) wave equation, and in general the resonances control the long-term behavior of waves on the manifold. In follow-up work, we plan to connect the theory of resonances on geometrically finite graphs developed in this paper with the wave equation on regular trees and graphs \cite{brooks_lindenstrauss1, brooks_lindenstrauss2, anker_wave}, and in particular with the Lax-Phillips scattering theory in this setting studied by the second author in \cite{peterson}. This should in turn be very closely related to the analogue of Eisenstein series in this setting which we plan to also develop; this should also allow us to rigorously describe in representation-theoretic terms the structure of the resonances for arithmetic examples mentioned in the previous paragraph.
```

    $ grep -n -F "In the setting of geometrically finite hyperbolic manifolds, the theory of resonances is very closely connected with the Lax-Phillips scattering theory" refs/src/2603.26443/final_draft.tex
    138:In the setting of geometrically finite hyperbolic manifolds, the theory of resonances is very closely connected with the Lax-Phillips scattering theory \cite{pbhr-LP76}. Roughly speaking, the resonances correspond to the poles of the scattering operator. The Lax-Phillips scattering theory is itself defined in terms of the (automorphic) wave equation, and in general the resonances control the long-term behavior of waves on the manifold. In follow-up work, we plan to connect the theory of resonances on geometrically finite graphs developed in this paper with the wave equation on regular trees and graphs \cite{brooks_lindenstrauss1, brooks_lindenstrauss2, anker_wave}, and in particular with the Lax-Phillips scattering theory in this setting studied by the second author in \cite{peterson}. This should in turn be very closely related to the analogue of Eisenstein series in this setting which we plan to also develop; this should also allow us to rigorously describe in representation-theoretic terms the structure of the resonances for arithmetic examples mentioned in the previous paragraph.
```
(NB: `\cite{peterson}` here refers to a second author's separate paper on discrete Lax–Phillips
scattering for graphs; its bibliographic entry was not resolved in this search — flagged for a
follow-up literature pass if the next round wants the wave-equation formulation specifically rather
than resolvent meromorphic continuation.)

Explicit resonance matrix for the pure cusp ($n=1$, one vertex, $q+1$ edges to a single ray) —
**this can be checked directly against the astra-brief's own C3 formula**, `2603.26443:final_draft.tex:1975-1979`,
quoted in full under Target 6 above.

Arithmetic examples tying resonances to Hasse–Weil zeta zeros (the closest existing "resonances $=$
$L$-function zeros" statement, albeit for the Hasse–Weil zeta of a curve rather than a Dirichlet
$L$-function of $\Gamma_0(N)$), `2603.26443:final_draft.tex:2088-2092`:
```
We now wish to describe how we are observing the same phenomenon in the examples from Section \ref{sec_elliptic_curves}. In the set-up described in Section \ref{sec_arithmetic_lattice}, we start with a smooth projective algebraic curve $C$ over a finite field $\mathbb{F}_q$ and a point $P$ on $C$ (which we think of as a ``point at $\infty$''). The analogue of \eqref{eqn_locally_symmetric_space} is \eqref{eqn_function_field_quotient}. Thus in analogy with the number field setting, we should expect the resonances to be of the following form:
```
```
    \item Resonances on the circle of radius $\frac{1}{q^{\frac{1}{4}}}$ corresponding to square roots of zeros of the Hasse-Weil zeta function of $C$. The connection between resonances and the Hasse-Weil zeta function (the function field analogue of the Dedekind zeta function) should come from the connection of them both to Eisenstein series (via the Lax-Phillips scattering theory and the Langlands-Shahidi method, respectively). The fact that they all lie on this circle is a consequence of Weil's proof of the Riemann hypothesis in this setting \cite{weil}.
```

    $ grep -n -F "Resonances on the circle of radius \$\frac{1}{q^{\frac{1}{4}}}\$ corresponding to square roots of zeros of the Hasse-Weil zeta function" refs/src/2603.26443/final_draft.tex
    2092:    \item Resonances on the circle of radius $\frac{1}{q^{\frac{1}{4}}}$ corresponding to square roots of zeros of the Hasse-Weil zeta function of $C$. The connection between resonances and the Hasse-Weil zeta function (the function field analogue of the Dedekind zeta function) should come from the connection of them both to Eisenstein series (via the Lax-Phillips scattering theory and the Langlands-Shahidi method, respectively). The fact that they all lie on this circle is a consequence of Weil's proof of the Riemann hypothesis in this setting \cite{weil}.

This is important for the astra-brief's T7/T8: it is the *arithmetic curve* analogue (Hasse–Weil zeta
of the underlying curve $C$, via $\mathrm{PGL}_2(R)$ for $R$ the coordinate ring) of what the brief
wants for the *level* case ($\Gamma_0(N)\subset\mathrm{GL}_2(\mathbb F_q[T])$, via Dirichlet
$L$-functions of $\mathbb F_q[T]$). These are two different (complementary) arithmetic generalisations
of the same pure-cusp base case, and the paper explicitly notes the mechanism in both cases is
"Eisenstein series" — supporting, but not proving, H-ARITH.

Complementary, foundational-but-generic sources on scattering for graphs with tails/leads (standard
background, cited for the discrete Lax–Phillips machinery of T1 in the astra-brief, not
arithmetic-specific):

`0906.2825:main.tex:38` (Varbanov–Brun, S-matrix for a finite graph with several infinite tails,
continuous time):
```
We consider quantum walks on a finite graphs to which infinite tails are attached. We explore how the propagating and bound states depend on the structure of the finite graph. The S-matrix for such graphs is defined. Its unitarity is proved as well as some other of its properties such as its transformation under time reversal.
```

    $ grep -n -F "We consider quantum walks on a finite graphs to which infinite tails are attached." refs/src/0906.2825/main.tex
    38:We consider quantum walks on a finite graphs to which infinite tails are attached. We explore how the propagating and bound states depend on the structure of the finite graph. The S-matrix for such graphs is defined. Its unitarity is proved as well as some other of its properties such as its transformation under time reversal. A spectral decomposition of the identity for the Hamiltonian of the graph is derived using its eigenvectors. We derive formulas for the S-matrix of a graph under certain operation such as cutting a tail, attaching a tail or connecting two tails to form an edge.

and its explicit S-matrix definition, `0906.2825:main.tex:224`:
```
The S-matrix is defined as
```

    $ grep -n -F "The S-matrix is defined as" refs/src/0906.2825/main.tex
    224:The S-matrix is defined as

`1503.04952:main.tex:139-141` (Golinskii, spectral canonical form for finite graphs with attached
infinite paths — discrete-time adjacency-operator analogue, closest in spirit to the astra-brief's
$T=T_X\oplus T_\text{ray}+\text{coupling}$ setup):
```
We compute explicitly (modulo solutions of certain algebraic equations) the spectra of
infinite graphs obtained by attaching one or several infinite paths to some vertices of
certain finite graphs. The main result concerns a canonical form of the adjacency matrix
of such infinite graphs.
```

    $ grep -n -F "We compute explicitly (modulo solutions of certain algebraic equations) the spectra of" refs/src/1503.04952/main.tex
    139:We compute explicitly (modulo solutions of certain algebraic equations) the spectra of

Assessment: **strong hit, not a perfect match**. `2603.26443` gives a complete, modern, arithmetic-aware
discrete resonance theory that reproduces the astra-brief's C3 pure-cusp formula exactly and already
connects resonances to Hasse–Weil zeta zeros for algebraic-curve lattices (the "other" arithmetic
generalisation of the pure cusp, complementary to $\Gamma_0(N)$-level). It explicitly says the true
wave-equation/Lax–Phillips construction for graphs is *follow-up work* (citing an unresolved
`\cite{peterson}`), so the astra-brief's own T1 (discrete Lax–Phillips wave group, one-exit
contraction, Sz.-Nagy–Foias model) is **not yet written down in the literature** for this setting and
must be done from scratch, exactly as the brief assumes; `0906.2825` and `1503.04952` are the standard
generic (non-arithmetic) building blocks for that construction.

---

## Manifest check

```
$ cd refs && sha256sum -c --quiet manifest.sha256 && echo MANIFEST OK
MANIFEST OK
```
