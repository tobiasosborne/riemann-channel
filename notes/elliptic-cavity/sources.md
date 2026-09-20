# Sources for the elliptic-cavity round (two arithmetic cavities with cusps, `GL_2(R)` for `R` the coordinate ring of an affine elliptic curve)

Author: claude:opus. Date: 2026-09-20.

Purpose: byte-verified sources for the round described in `notes/elliptic-cavity/astra-brief.md`
(the quotient graphs of groups of the two elliptic curves over `F_2` and `F_3` of
Arends--Peterson--Weich, arXiv `2603.26443`, read as arithmetic cavities whose resonances are the
square roots of the Hasse--Weil zeros; the `h x h` scattering matrix; the class-group /
Eisenstein-series structure; the funnel as an exit for the constant mode; function-field
Bost--Connes). Format and conventions follow `notes/cusp-graph/sources.md` and `refs/README.md`:
arXiv TeX source is fetched into `refs/src/<id>/`, quotes are cited as `<id>:<file>:<line>` and every
line number is verified by `grep -n -F` against the file on disk (the command and its output are
given under each quote); PDF text extraction is used only where no TeX exists, and such items get
their own sha256 recorded here (precedent: `refs/src/efrat-1991/`).

Convention: a quote is **exact** when it states the fact the brief needs essentially verbatim,
**variant** when it is a related but differently packaged statement (the difference is spelled out),
and a target is **NOT FOUND** when no freely accessible source stating it could be located
(bibliographic data is still given). Anything read off a *figure* rather than out of text is marked
**figure-read, not byte-verified**.

---

## 0. What was fetched

| id / slug | Title | Author(s) | File(s) | In `refs/manifest.sha256`? |
|---|---|---|---|---|
| `1012.4825` | Automorphic forms for elliptic function fields | O. Lorscheid | `refs/src/1012.4825/elliptic.tex` (+ figures) | yes |
| `1012.3513` | Graphs of Hecke operators | O. Lorscheid | `refs/src/1012.3513/hecke.tex` | yes |
| `1012.3223` | Toroidal automorphic forms for function fields | O. Lorscheid | `refs/src/1012.3223/main.tex` | yes |
| `sorensen-2001` | Fourier expansion of Eisenstein series on the Hilbert modular group and Hilbert class fields (Aarhus Preprint Series No. 6, Aug. 2001) | C. M. Sørensen | `refs/src/sorensen-2001/{paper.pdf,paper.txt}` | no (non-arXiv PDF; own sha256 below) |
| `math/0602554` | Bost--Connes type systems for function fields | B. Jacob | `refs/src/math/0602554/BC-for-function-fields.{tex,bbl}` | yes |
| `math/0607363` | Quantum statistical mechanics over function fields | C. Consani, M. Marcolli | `refs/src/math/0607363/main.tex` | yes |
| `1112.5826` | Bost--Connes systems associated with function fields | S. Neshveyev, S. Rustad | `refs/src/1112.5826/main.tex` | yes |
| `2603.16518` | Quantum ergodicity of Eisenstein series for Bianchi groups | (2026) | `refs/src/2603.16518/qe_eisseries.tex` | yes |
| `2603.26443` | Resonances on geometrically finite graphs | C. Arends, C. Peterson, T. Weich | `refs/src/2603.26443/final_draft.tex` | yes (earlier round) |
| `1203.6557` | Levinson's theorem for graphs II | A. M. Childs, D. Gosset | `refs/src/1203.6557/levinson2.tex` | yes (earlier round) |

sha256 of the non-arXiv item (not written into `refs/manifest.sha256`, which by the convention in
`refs/fetch_sources.sh` records only `.tex`/`.bbl`/`lambda2.txt`):

```
$ cd refs && sha256sum src/sorensen-2001/paper.pdf src/sorensen-2001/paper.txt
36ac826bfff651e430240b715e0ac3ecad46a426aa4d9e7c1c04982b046573a2  src/sorensen-2001/paper.pdf
0b8a2a8559ce65e71b596eb4dcdcf560a51b2f14fd677a0fc8738ea38f574c3b  src/sorensen-2001/paper.txt
```

Sørensen's preprint is freely hosted by Aarhus University at
`https://data.math.au.dk/publications/pp/2001/imf-pp-2001-6.pdf`; the text was extracted with
`pdftotext -layout` (the PDF's Type-1 fonts lose most Greek letters and `zeta`/`xi`, so the quotes
below have gaps -- each gap is reconstructed in the surrounding prose and flagged).

sha256 of the two Lorscheid figure files used in the D2 diagram check of Target 1 (figures are not
text, so they are recorded here explicitly and marked figure-read):

```
$ cd refs && sha256sum "src/1012.4825/ell_h=1_graph.pdf" "src/1012.4825/ell_h=4_graphA.pdf"
8c1967e29148ecc960554c84d1442b67e95b6fafef7663ebeb2a9b89d765b983  src/1012.4825/ell_h=1_graph.pdf
79d67646a65e8a7575a35bcd05022d6f81479b096151cfa54e6b9dfd1d90aec0  src/1012.4825/ell_h=4_graphA.pdf
```

### Exact fetch commands

The seven new arXiv ids were appended to the `IDS=` list in `refs/fetch_sources.sh` and fetched with
the script's own method:

```
$ cd refs
$ for id in 1012.3223 1012.3513 1012.4825 2603.16518 math/0602554 math/0607363 1112.5826; do
    d=src/$id; mkdir -p "$d"
    [ -f "$d/src.tar" ] || timeout 120 curl -sSL -o "$d/src.tar" "https://arxiv.org/e-print/$id"
    ( cd "$d" && ( tar xf src.tar 2>/dev/null || gunzip -c src.tar > main.tex ) )
  done
$ mkdir -p src/sorensen-2001
$ curl -sSL -A "Mozilla/5.0 (X11; Linux x86_64)" -o src/sorensen-2001/paper.pdf \
    "https://data.math.au.dk/publications/pp/2001/imf-pp-2001-6.pdf"
$ pdftotext -layout src/sorensen-2001/paper.pdf src/sorensen-2001/paper.txt
```

Manifest append (same rule as `fetch_sources.sh`: `.tex`/`.bbl`/`lambda2.txt`, `LC_ALL=C sort` per id):

```
$ cd refs
$ for id in 1012.3223 1012.3513 1012.4825 2603.16518 math/0602554 math/0607363 1112.5826; do
    find "src/$id" -type f \( -name '*.tex' -o -name '*.bbl' -o -name 'lambda2.txt' \) \
      | LC_ALL=C sort | while read -r f; do sha256sum "$f"; done
  done >> manifest.sha256
$ sha256sum -c --quiet manifest.sha256 && echo MANIFEST OK
MANIFEST OK
```

The eight lines appended (manifest went from 250 to 258 lines):

```
c2fd00e0eaa7ee7ab1ba98abfd5a77e83f2788e77d84f99fa52d6456a139f66e  src/1012.3223/main.tex
66babf6a6cef0a673e98986c1d3feb620015dc5778055d3e98116908fdfa0a75  src/1012.3513/hecke.tex
bff45689b903161eed388c922401bd4315febc39ab43d211a7c7250220177640  src/1012.4825/elliptic.tex
82b49c7ab942670d27350e648244269e42609fa4a9f1036ed207c029abb88ecc  src/2603.16518/qe_eisseries.tex
6088957de6dc6b8b696988ff85dd7284edf0799cdaac66c86e281e47accc3e78  src/math/0602554/BC-for-function-fields.bbl
63d63e09a799e0de36bcc4a353a3336fb2ddbfaea745d3c3739da1ba4ff9e735  src/math/0602554/BC-for-function-fields.tex
55ce5b3341bf361acd471ce79693bda4890668094691782b9b2e05245c5ffa57  src/math/0607363/main.tex
3aa990c62e03b7e82295e307e85ecace8f23d33691887df1601ec9590b3071b2  src/1112.5826/main.tex
```

---

## Target 1 -- Takahashi, *The fundamental domain of the tree of GL(2) over the function field of an elliptic curve*, Duke Math. J. **72** (1993) 85--97

**NOT FOUND as a free download.** The article is on Project Euclid
(`https://projecteuclid.org/journals/duke-mathematical-journal/volume-72/issue-1/The-fundamental-domain-of-the-tree-of-GL2-over-the/10.1215/S0012-7094-93-07204-3.short`,
DOI `10.1215/S0012-7094-93-07204-3`); Duke back issues of 1993 are subscription-only and the landing
page returns no downloadable PDF to an unauthenticated client. No arXiv version exists (pre-arXiv
era), and no author's-page or repository copy was located. So **Theorem 5 and Figure 5, the actual
source of H-DIAG-2 and H-DIAG-3, remain unverified at the primary source.**

Bibliographic record, independently confirmed twice. `1012.4825:elliptic.tex:1144-1148`
(Lorscheid's bibliography):

```
\bibitem{Takahashi}
Shuzo Takahashi.
\newblock The fundamental domain of the tree of {${\rm GL}(2)$} over the
  function field of an elliptic curve.
\newblock {\em Duke Math. J.}, 72(1):85--97, 1993.
```

    $ grep -n -F "The fundamental domain of the tree of {\${\rm GL}(2)\$} over the" refs/src/1012.4825/elliptic.tex
    1146:\newblock The fundamental domain of the tree of {${\rm GL}(2)$} over the

and APW's own citation of the theorem, `2603.26443:final_draft.tex:1983`:

```
Takahashi \cite{takahashi} (specifically Theorem 5 therein) describes explicitly how to compute the arithmetic graph of groups described in Section \ref{sec_arithmetic_lattice} corresponding to an elliptic curve over a finite field. We discuss two examples.
```

    $ grep -n -F "(specifically Theorem 5 therein) describes explicitly how to compute the arithmetic graph of groups" refs/src/2603.26443/final_draft.tex
    1983:Takahashi \cite{takahashi} (specifically Theorem 5 therein) describes explicitly how to compute the arithmetic graph of groups described in Section \ref{sec_arithmetic_lattice} corresponding to an elliptic curve over a finite field. We discuss two examples.

### 1a. The best available substitute: Lorscheid, `1012.4825`

Lorscheid's paper is the closest thing to Takahashi's theorem that is freely available, and it treats
*the same two curves*. He uses Takahashi's computation explicitly.

`1012.4825:elliptic.tex:212`:

```
Thus we can regard $f$ as a function on the quotient $\lquot{\Gamma}{\Vertex\cT_x}$. Shuzo Takahashi calculates this quotient for places $x$ of degree $1$ in \cite{Takahashi}. This means that he describes representatives in $\PGL_2(F_x)$ for the double quotient $\lrquot{\Gamma}{\PGL_2(F_x)}{\PGL_2(\cO_x)}$. The full subgraph of the classes of these representatives in $\Vertex\cT_x$ is a tree, and this tree is isomorphic to the quotient graph $\lquot{\Gamma}{\cT_x}$.
```

    $ grep -n -F "Shuzo Takahashi calculates this quotient for places \$x\$ of degree \$1\$ in \cite{Takahashi}." refs/src/1012.4825/elliptic.tex
    212:Thus we can regard $f$ as a function on the quotient ... (line as quoted)

`1012.4825:elliptic.tex:224` (Takahashi also gives the stabilisers -- i.e. exactly APW's `S`):

```
This quotient graph, in turn, is isomorphic to the graph of $\Phi_x$ (when weights are suppressed), which is illustrated in Figure \ref{ell_h_odd_graph} (see section \ref{section_examples}). Takahashi further determines the stabilizers of $\Gamma$ acting $\Vertex\cT_x$, which allows to compute the action of $T_x$ on a function on $\lquot{\Gamma}{\Vertex\cT_x}\simeq\cX$ by the formula
```

    $ grep -n -F "Takahashi further determines the stabilizers of \$\Gamma\$ acting \$\Vertex\cT_x\$" refs/src/1012.4825/elliptic.tex
    224:This quotient graph, in turn, is isomorphic to the graph of $\Phi_x$ (when weights are suppressed), ...

**Crucial restriction** -- the isomorphism "quotient graph of the tree = graph of the Hecke operator"
is asserted for odd class number only, and Lorscheid says it *fails* for even class number,
`1012.4825:elliptic.tex:227`:

```
If the class number is odd, but not $1$, then the eigenvalue with respect to $T_x$ does not suffice to determine an automorphic form, but we need to consider the action of other Hecke operators as well. ... Even worse, if the class number is even, the correspondence between the local and the global situation breaks down and we are not able to draw any of the above conclusions.
```

    $ grep -n -F "Even worse, if the class number is even, the correspondence between the local and the global situation breaks down" refs/src/1012.4825/elliptic.tex
    227:An automorphic form that is an simultaneous eigenfunction for all Hecke operators ... (line as quoted)

This is why the substitute confirms D2 (`h = 1`) but **not** D3 (`h = 4`); see 1b, 1c.

The three class-number-one elliptic function fields, `1012.4825:elliptic.tex:609` -- the first of them
is exactly APW's first example and the brief's D2:

```
 The easiest examples are given by elliptic curves with only one rational point $x$. These examples can be found in the literature, cf.\ \cite{Cornelissen-Lorscheid}, \cite[2.4.4 and Ex. 3 of 2.4]{Serre} or \cite{Takahashi}. There are up to isomorphism three such elliptic curves: $X_2$ over $\FF_2$ defined by the Weierstrass equation $\underline Y^2+\underline Y=\underline X^3+\underline X+1$, $X_3$ over $\FF_3$ ... Since the class number is $1$, $\PBundec X_q = \{c_{nx}\}_{n\geq0}$ and $\PBungi X_q=\{s_0,s_x\}$ for $q\in\{2,3,4\}$.
```

    $ grep -n -F "There are up to isomorphism three such elliptic curves: \$X_2\$ over \$\FF_2\$ defined by the Weierstrass equation \$\underline Y^2+\underline Y=\underline X^3+\underline X+1\$" refs/src/1012.4825/elliptic.tex
    609: The easiest examples are given by elliptic curves with only one rational point $x$. ... (line as quoted)

Note that Lorscheid's genus-one bibliography cites `Serre, Trees, 2.4.4` for the same example, which
is APW's own stated source for D2 (`2603.26443:final_draft.tex:1985`, "The first example is taken
from 2.4.4 of \cite{serre_trees}").

### 1b. Independent check of H-DIAG-2 (figure-read, not byte-verified)

`refs/src/1012.4825/ell_h=1_graph.pdf` is Lorscheid's Figure for the class-number-one curves (caption,
`1012.4825:elliptic.tex:615`: `$\cG_x$ for the unique degree one place $x$ of the elliptic curves
$X_q$ for $q=2,3,4$`). Rendered (`pdftoppm -r 200 -png`) it shows a weighted graph with vertices
`t_1, ..., t_q`, `s_1`, `s_0`, `c_0`, `c_1`, `c_2`, ... and the weight written next to a vertex on an
edge is the number of edges seen from that vertex; the weights around every vertex sum to `q+1`.
Lorscheid's weights `m_x(v,w)` and APW's adjacency coefficients `S(v)/S(e)` are the same number
(both give `A f(v) = sum_w m(v,w) f(w)` with row sum `q+1`), so the two data sets can be compared
entry by entry. For `q = 2` the comparison against the brief's H-DIAG-2 is:

| APW / brief (D2) | `S(v)/S(e)` | Lorscheid vertex | Lorscheid weight |
|---|---|---|---|
| `A -> B` | `6/2 = 3` | `c_0 -> c_1` | `q+1 = 3` |
| `B -> A` | `2/2 = 1` | `c_1 -> c_0` | `1` |
| `B -> C` | `2/2 = 1` | `c_1 -> s_0` | `q-1 = 1` |
| `C -> B` | `2/2 = 1` | `s_0 -> c_1` | `1` |
| `C -> D` | `2/1 = 2` | `s_0 -> s_1` | `q = 2` |
| `D -> C` | `1/1 = 1` | `s_1 -> s_0` | `1` |
| `D -> E`, `D -> F` | `1/1 = 1` | `s_1 -> t_1`, `s_1 -> t_2` | `1` |
| `E -> D`, `F -> D` | `3/1 = 3` | `t_1 -> s_1`, `t_2 -> s_1` | `q+1 = 3` |
| `B -> c_1` (cusp edge) | `2/2 = 1` | `c_1 -> c_2` | `1` |
| `c_1 -> B` | `4/2 = 2` | `c_2 -> c_1` | `q = 2` |
| `c_k -> c_{k+1}` | `2^{k+1}/2^{k+1} = 1` | `c_{k+1} -> c_{k+2}` | `1` |
| `c_{k+1} -> c_k` | `2^{k+2}/2^{k+1} = 2` | `c_{k+2} -> c_{k+1}` | `q = 2` |

Every entry matches under the relabelling `A,B,C,D,E,F <-> c_0, c_1, s_0, s_1, t_1, t_2` and
`c_k^{APW} <-> c_{k+1}^{Lorscheid}`. So **H-DIAG-2 is independently confirmed as a weighted graph**
(hence the adjacency operator `A`, hence `T_X` and `c^2 = 1` at the junction `B`) by a second,
freely available source that does not go through APW.

Caveat, stated plainly: the weights live in a *figure*, read by rendering the PDF, not in the TeX
source. The file's sha256 is recorded in section 0 so the read is reproducible, but this is
**figure-read, not byte-verified**. The one thing it does *not* confirm is the individual stabiliser
sizes `S(v)` (only the ratios `S(v)/S(e)`), which is all the spectral theory uses
(`2603.26443:final_draft.tex:429`: "The specific structure of the vertex and edge groups is not
relevant for the spectral theory; we only need the data of their sizes.").

### 1c. H-DIAG-3 is **not** confirmed, and the obvious substitute is a *different graph*

Lorscheid's two class-number-four examples are over `F_3`, `1012.4825:elliptic.tex:634`:

```
 We give two examples for elliptic curves with even class number.
 Both examples are elliptic curves over $\FF_3$ with class number $4$, but with respective class group $\ZZ/4\ZZ$ and $(\ZZ/2\ZZ)\times(\ZZ/2\ZZ)$.
```

    $ grep -n -F "Both examples are elliptic curves over \$\FF_3\$ with class number \$4\$, but with respective class group \$\ZZ/4\ZZ\$ and \$(\ZZ/2\ZZ)\times(\ZZ/2\ZZ)\$." refs/src/1012.4825/elliptic.tex
    634: We give two examples for elliptic curves with even class number. ... (line as quoted)

and the `Z/4` one is `1012.4825:elliptic.tex:637`:

```
 The first example is the elliptic curve $X_5$ over $\FF_3$ defined by the Weierstrass equation $\underline Y^2=\underline X^3+\underline X+2$, which has class group $\Cl^0 X_5\simeq\ZZ/4\ZZ$. Let $X(\FF_3)=\{x,y,z,z'\}$ such that $x-y$ is the element of order $2$. The number of components is $h_2=2$, ...
```

    $ grep -n -F "The first example is the elliptic curve \$X_5\$ over \$\FF_3\$ defined by the Weierstrass equation \$\underline Y^2=\underline X^3+\underline X+2\$, which has class group \$\Cl^0 X_5\simeq\ZZ/4\ZZ\$." refs/src/1012.4825/elliptic.tex
    637: The first example is the elliptic curve $X_5$ over $\FF_3$ ... (line as quoted)

`X_5: y^2 = x^3 + x + 2` over `F_3` is **the same curve** as the brief's D3, `y^2 = x^3 + x + 1`: the
substitution `x -> x + 2` gives `(x+2)^3 + (x+2) + 1 = x^3 + 2^3 + x + 3 = x^3 + x + 2` in
characteristic 3. (Arithmetic check, not a quoted source.) But Lorscheid's Figure
`ell_h=4_graphA.pdf` is **disconnected into two components**, because, `1012.4825:elliptic.tex:309`:

```
 The connected components of $\cG_x$ stay in bijection with the $2$-torsion elements of $\Pic X$. In particular, $\cG_x$ is connected if and only if the class number of $F$ is odd.
```

    $ grep -n -F "The connected components of \$\cG_x\$ stay in bijection with the \$2\$-torsion elements of \$\Pic X\$." refs/src/1012.4825/elliptic.tex
    309: The connected components of $\cG_x$ stay in bijection with the $2$-torsion elements of $\Pic X$. ...

Read off the rendered figure (**figure-read**): two components, nucleus vertices
`t_D, s_x, s_0, c_{y-x}` and `t_{D'}, s_z, c_{z-x}` (7 in all), and four cusp rays beginning at
`c_x, c_y, c_z, c_{z'}`. APW's D3 has **one** component, **nine** core vertices and four cusps. So the
two graphs are different objects -- which is exactly what line 227 above predicts for even class
number: `G_x` (the global graph of the Hecke operator on `P^1`-bundles) is not `Gamma \ T_x` when
`h` is even. **Conclusion: H-DIAG-3 is neither confirmed nor contradicted by any source found; the
only free source with a `h = 4` picture of this curve is drawing a different graph.** The `h = 4`
cusp count does agree (four cusps), and that part is independently supported (Target 7).

Assessment: Takahashi himself **NOT FOUND**; H-DIAG-2 **confirmed** (figure-read) by `1012.4825`;
H-DIAG-3 **left open**, with a documented reason why the natural substitute does not settle it.

---

## Target 2 -- Li 1979, the constant term of the Eisenstein series on `GL_2(R) \ T`; the genus-dependent prefactor; class-group characters; Gekeler, Gekeler--Nonnengardt, Weil LNM 189

### 2a. The primary items

**W.-C. W. Li, "Eisenstein series and decomposition theory over function fields", Math. Ann. 240
(1979), 115--139: NOT FOUND as a free download.** DOI `10.1007/BF01364628`; Springer serves only a
bot-challenge page to an unauthenticated client (verified: `curl` on
`https://link.springer.com/content/pdf/10.1007/BF01364628.pdf` returns a 3 kB HTML challenge document,
not a PDF). This was already recorded as NOT FOUND in the previous round
(`notes/cusp-graph/sources.md`, Target 3), where second-hand descriptions from `2108.02919:290`
(Ali--Carbone--Garrett: "She studied the intertwining operators arising from constant Fourier
coefficients, proved that they are rational and showed that they satisfy a functional equation")
and `2303.09327:108` are recorded and byte-verified; they are not repeated here.

**E.-U. Gekeler, "Improper Eisenstein series on Bruhat--Tits trees", Manuscripta Math. 86 (1995)
367--391: NOT FOUND as a free download** (DOI `10.1007/BF02568000`; Springer paywall, no arXiv
version, no author's-page copy located).

**E.-U. Gekeler and U. Nonnengardt, "Fundamental domains of some arithmetic groups over function
fields", Internat. J. Math. 6 (1995), no. 5, 689--708: NOT FOUND as a free download** (already
recorded as NOT FOUND in `notes/cusp-graph/sources.md`, Target 6). Cited by Lorscheid at
`1012.3513:hecke.tex:156` as `\cite{Gekeler-Nonnengardt}` for the rational-function-field case.

**A. Weil, "Dirichlet series and automorphic forms" (LNM 189, 1971): NOT FOUND**; no freely
accessible copy of the function-field chapter was located (Springer LNM, paywalled). No verified
statement from it is used anywhere below.

**Later arXiv work stating the scattering matrix / constant term for `GL_2` over the function field
of a curve of genus `g` with class number `h`: NOT FOUND in the form the brief asks for.** arXiv
searches over Drinfeld modular curves, harmonic cochains and "Eisenstein series on the Bruhat--Tits
tree" turned up the Eisenstein-ideal literature (`1410.8277`, `1306.3632`, `0902.4776`) but nothing
that writes an `h x h` matrix of `zeta`/`L`-ratios for a general curve. The best available is the
adelic statement of Lorscheid below, which is Li's theory restated with an explicit genus-dependent
factor, plus the level-`A` rational-function-field case already in the repo from the previous round
(`2303.09327:main.tex:390`, `q^{a(1-2s)}/(1-q^{-2as}) * zeta(2s-1)/zeta(2s)`).

### 2b. What *is* available: Lorscheid `1012.3223` (adelic constant term, citing Li)

`1012.3223:main.tex:563-568` -- the constant term and the intertwining operator, with Li as the
reference (this is the object the brief calls the scattering matrix):

```
 We state the functional equation for Eisenstein series. For reference, see \cite{Li}. Let $B$ be the standard Borel subgroup and $N$ its unipotent radical. The constant term of $E(g,\varphi,\chi,s)$ is given by
 $$ E_N(g,\varphi,\chi,s) \ = \ f_{\varphi,\chi}(s)(g) \ + \ M_\chi(s)\,f_{\varphi,\chi}(s)(g) $$
 with
 $$ M_\chi(s)f_{\varphi,\chi}(g) \ = \ \int\limits_{N_\AA}f_{\varphi,\chi}(\tinymat {} 1 1 b g)\;db \;. $$
```

    $ grep -n -F "We state the functional equation for Eisenstein series. For reference, see \cite{Li}." refs/src/1012.3223/main.tex
    563: We state the functional equation for Eisenstein series. For reference, see \cite{Li}. Let $B$ be the standard Borel subgroup ...

`1012.3223:main.tex:573` -- **the genus-dependent factor**, which is what the brief's H-EIS is
guessing at:

```
 for all $\chi\in\Xi$ and $s\in\CC$ unless $\chi^2\norm \ ^{2s}=1$.  If $\chi\in\Xi_0$, then $c(\chi,s)=\chi^2(\fc) \norm \fc^{2s}$.
```

    $ grep -n -F "If \$\chi\in\Xi_0\$, then \$c(\chi,s)=\chi^2(\fc) \norm \fc^{2s}\$." refs/src/1012.3223/main.tex
    573: for all $\chi\in\Xi$ and $s\in\CC$ unless $\chi^2\norm \ ^{2s}=1$.  If $\chi\in\Xi_0$, then $c(\chi,s)=\chi^2(\fc) \norm \fc^{2s}$.

and the genus enters through the differental idele `fc`, `1012.3223:main.tex:187`:

```
Let $\fc$ be a differental idele, i.e.\ a representative of the canonical divisor in the divisor class group $\AA^\times/F^\times\cO_\AA^\times$, which is of degree $2g-2$.
```

    $ grep -n -F "which is of degree \$2g-2\$" refs/src/1012.3223/main.tex
    187: Let $\AA$ be the adele ring of $F$ ... which is of degree $2g-2$. ...

together with the matching `L`-series functional equation, `1012.3223:main.tex:583`:

```
 of $L$-series where $\epsilon(\chi,s)=\chi(\fc)\norm{\fc}^s$ if $\chi$ is unramified.
```

    $ grep -n -F "of \$L\$-series where \$\epsilon(\chi,s)=\chi(\fc)\norm{\fc}^s\$ if \$\chi\$ is unramified." refs/src/1012.3223/main.tex
    583: of $L$-series where $\epsilon(\chi,s)=\chi(\fc)\norm{\fc}^s$ if $\chi$ is unramified.

Reading (arithmetic, not quoted): `deg fc = 2g-2` gives `|fc| = q^{-(2g-2)} = q^{2-2g}`, so the
factor relating `E(.,chi,s)` to `E(.,chi^{-1},-s)` is `chi^2(fc) q^{(2-2g)2s}` in the adelic
normalisation. **This is genus-dependent and it is a pure monomial in `q^{-s}`** -- the shape the
brief's H-EIS posits. But the exponent is `(2-2g)2s`, which at `g=0` gives `q^{4s}` and at `g=1`
gives `1`, whereas the brief's two data points, in the *ray* normalisation of the graph, are `q`
(`g=0`) and `q^{1-2s}` (`g=1`). The two normalisations differ (Lorscheid's `E` is not the normalised
Eisenstein series, and the graph normalisation divides by `sqrt q` and rescales by `sqrt S`), and
**no fetched source performs the translation**. So this quote *constrains* H-EIS (the prefactor is a
monomial whose exponent is affine in `g`) but does **not** establish the brief's `q^{1-2gs}`.

`1012.3223:main.tex:104` gives the one clean genus-and-class-number count in the function field case:

```
The dimension of the space of derivatives of unramified Eisenstein series equals $h(g-1)+1$ if the characterisitc is not $2$; in characteristic $2$, the dimension is bounded from below by this number. Here $g$ is the genus and $h$ is the class number of $F$.
```

    $ grep -n -F "The dimension of the space of derivatives of unramified Eisenstein series equals \$h(g-1)+1\$" refs/src/1012.3223/main.tex
    104: In this paper, we concentrate on the function field case. ... (line as quoted)

### 2c. The genus-one zeta function with the class number in it

`1012.4825:elliptic.tex:927` -- exactly the object the brief calls `zeta_K`, with `h` visible in the
numerator (so `P(T) = qT^2 + (h - (q+1))T + 1`; for D2, `q=2, h=1`: `2T^2 - 2T + 1`; for D3,
`q=3, h=4`: `3T^2 + 1` -- both agree with APW):

```
 Before we proceed to determine the rest of $\cA_\tor(F')$, we need some facts on the zeros of the zeta function $\zeta_{F'}$ of $F'$. The zeta function
 $$ \zeta_F(s)=\frac{qT^2\,+\,\bigl(h\,-\,(q+1)\bigr)T\,+\,1}{(1\,-\,T)\,(1\,-\,qT)} $$
 of $F$ satisfies the functional equation $\zeta_F(1-s)=\zeta_F(s)$. Here $h$ is the class number and $T=q^{-s}$.
```

    $ grep -n -F "\$\$ \zeta_F(s)=\frac{qT^2\,+\,\bigl(h\,-\,(q+1)\bigr)T\,+\,1}{(1\,-\,T)\,(1\,-\,qT)} \$\$" refs/src/1012.4825/elliptic.tex
    927: Before we proceed to determine the rest of $\cA_\tor(F')$ ... (line as quoted)

and the notebook-relevant remark that temperedness of a space of automorphic forms *is* the Riemann
hypothesis for the curve, `1012.4825:elliptic.tex:993`:

```
The interesting aspect of the calculations with the eigenvalue equations is that one obtains the equality $\lambda_x^2=(q+1-h)^2$ for the $\Phi_x$-eigenvalues $\lambda_x$ of the Eisenstein series $E(\blanc,\chi)$ in $\cA_\tor(F')$ if $x$ is of degree $1$. The estimation $0<h<2q+2$ coming from the embedding of $X$ into $\PP^2$ yields that $\cA_\tor(F')$ is unitarizable. To prove that $\cA_\tor(F')$ is a tempered representation, which would imply the Riemann hypothesis for $X$ (cf.\ \cite[Thm.\ 9.4]{Lorscheid1}), one needs the estimate $q+1-2q^{1/2}\leq h\leq q+1+2q^{1/2}$.
```

    $ grep -n -F "To prove that \$\cA_\tor(F')\$ is a tempered representation, which would imply the Riemann hypothesis for \$X\$" refs/src/1012.4825/elliptic.tex
    993: An alternative proof of the above theorem ... (line as quoted)

Assessment: Li, Gekeler, Gekeler--Nonnengardt, Weil LNM 189 all **NOT FOUND**; H-EIS is
**constrained but not settled** by `1012.3223`; the genus-one `zeta_K` with `h` is **exact**.

---

## Target 3 -- the class-group-character diagonalisation of the scattering matrix (Efrat 1987 / Efrat--Sarnak 1985 / Hejhal)

**Efrat, "The Selberg trace formula for `PSL_2(R)^n`", Mem. Amer. Math. Soc. 65 (1987), no. 359, and
Hejhal, LNM 1001: NOT FOUND as free downloads.** Efrat--Sarnak, "The determinant of the Eisenstein
matrix and Hilbert class fields", Trans. Amer. Math. Soc. **290** (1985), no. 2, 815--824, is also
not freely retrievable (`ams.org` returns HTTP 403 to an unauthenticated client; verified by `curl`
on the issue table of contents).

**A free, complete, primary substitute was found: C. M. Sørensen, Aarhus Preprint Series No. 6
(Aug. 2001)**, which proves exactly the statement the brief wants, *for a general number field*
(no class-number-one assumption), and cites Efrat 1987 as `[1]` and Efrat--Sarnak 1985 as `[2]`.
Quotes below are from `pdftotext -layout` output; the PDF's fonts drop `zeta`, `xi`, `chi`, `psi` and
`Phi`, so each missing symbol is reconstructed in square brackets in the prose (never inside the
quote).

Abstract, `sorensen-2001:paper.txt:33-37`:

```
     Eisenstein vector. That is, we identify the scattering matrix. When we compute
     the determinant of the scattering matrix in the principal case, the Dedekind  -
     function of the Hilbert class  eld shows up. A proof in the imaginary quadratic
     case was given in [2], and for totally real  elds with class number one a proof was
     given in [1].
```

    $ LC_ALL=C grep -n -F "Eisenstein vector. That is, we identify the scattering matrix. When we compute" refs/src/sorensen-2001/paper.txt
    34:     Eisenstein vector. That is, we identify the scattering matrix. When we compute

(the gap after "Dedekind" is `zeta`; `[1]` = Efrat 1987, `[2]` = Efrat--Sarnak 1985, per the
bibliography quoted below.)

Cusps = ideal classes, `sorensen-2001:paper.txt:493-494`:

```
this number is equal to the ideal class number h.
Proposition 2.2. The number of inequivalent cusps for              is equal to h.
```

    $ LC_ALL=C grep -n -F "Proposition 2.2. The number of inequivalent cusps for" refs/src/sorensen-2001/paper.txt
    494:Proposition 2.2. The number of inequivalent cusps for              is equal to h.

The scattering matrix itself, `sorensen-2001:paper.txt:1413-1417` (Theorem 7.2) -- the matrix is
indexed by ideal classes, built from the matrix of completed partial Hecke `L`-series at `2s` and
`2s-1`, times the permutation matrix `P` of inversion on the class group:

```
Theorem 7.2. The scattering matrix for the Hilbert modular group is

                                          ^ s; ) 1(2
                             (s; m; ) = (2      ^ s                 1; )P;

with notation as above.
```

    $ LC_ALL=C grep -n -F "Theorem 7.2. The scattering matrix for the Hilbert modular group is" refs/src/sorensen-2001/paper.txt
    1413:Theorem 7.2. The scattering matrix for the Hilbert modular group is

(reconstructed: `Phi(s,m,chi) = xihat(2s,chi)^{-1} xihat(2s-1,chi) P`; the same formula appears at
`:1216` as the constant-term matrix, and Lemma 5.1 at `:1202-1214` shows it is the `h x h` matrix of
constant terms in the two cusp exponentials -- i.e. literally the brief's `S(z)` with
`z^{-k} delta_{ab} + S_{ab} z^k`.)

The **diagonalisation over class-group characters** is the Dedekind determinant relation,
`sorensen-2001:paper.txt:1429-1433` (Proposition 8.1) applied to the class group:

```
Proposition 8.1. Let G be a  nite abelian group, and f any function. Then
                                                  YX
                            det f (a 1 b) =                    (a)f (a);
                               a;b
                                                     2G a2G
where G = f g is the group of characters.
```

    $ LC_ALL=C grep -n -F "Proposition 8.1. Let G be a" refs/src/sorensen-2001/paper.txt
    1429:Proposition 8.1. Let G be a  nite abelian group, and f any function. Then

(the proof, `:1434-1460`, is exactly "the characters are a basis of eigenvectors"; the missing symbol
before `(a)f(a)` is `psi`, the character, and `G` with a hat is the character group.)

The resulting determinant, `sorensen-2001:paper.txt:1475-1481` (Corollary 8.2) -- **the ratio of
Hecke `L`-functions at `2s-1` and `2s`, one factor per class-group character**:

```
Corollary 8.2. The scattering determinant for the Hilbert modular group is
                                                   Y (2s 1; )
                      det (s; m; ) = sign(Cl)                ;
                                                          (2s; )

where     varies over all Grossencharacters modulo m = O extending m .
```

    $ LC_ALL=C grep -n -F "Corollary 8.2. The scattering determinant for the Hilbert modular group is" refs/src/sorensen-2001/paper.txt
    1475:Corollary 8.2. The scattering determinant for the Hilbert modular group is

(reconstructed: `det Phi(s,m,chi) = sign(Cl) prod_psi xi(2s-1, psi) / xi(2s, psi)`.)

and the unramified case, `sorensen-2001:paper.txt:1536-1541` (Corollary 8.3) -- the Dedekind zeta of
the **Hilbert class field** `H`:

```
Corollary 8.3. For m = 0 the scattering determinant is given by
                                                (2s 1)
                             (s; 0) = sign(Cl) H        ;
                                                 H (2s)
with notation as above.
```

    $ LC_ALL=C grep -n -F "Corollary 8.3. For m = 0 the scattering determinant is given by" refs/src/sorensen-2001/paper.txt
    1536:Corollary 8.3. For m = 0 the scattering determinant is given by

(reconstructed: `phi(s,0) = sign(Cl) zeta_H(2s-1)/zeta_H(2s)`, since
`zeta_H(s) = prod_psi L(s,psi)` over the class-group characters.)

Bibliography confirming the two items the brief names,
`sorensen-2001:paper.txt:1637-1640`:

```
[1] Efrat, Isaac Y, The Selberg trace formula for PSL2 (R)n , Mem. Amer. Math. Soc. 65 (1987),
 no. 359, iv+111 pp.
[2] Efrat, I. ; Sarnak, P, The determinant of the Eisenstein matrix and Hilbert class  elds, Trans.
 Amer. Math. Soc. 290 (1985), no. 2, 815{824.
```

    $ LC_ALL=C grep -n -F "[1] Efrat, Isaac Y, The Selberg trace formula for PSL2 (R)n , Mem. Amer. Math. Soc. 65 (1987)," refs/src/sorensen-2001/paper.txt
    1637:[1] Efrat, Isaac Y, The Selberg trace formula for PSL2 (R)n , Mem. Amer. Math. Soc. 65 (1987),

**One warning the brief should register** (this is the part T2(d) is confronting). Sørensen's
scattering matrix is `xihat(2s)^{-1} xihat(2s-1) P`, a matrix of *partial* `L`-series indexed by
class pairs, *times a permutation matrix* `P` (inversion on `Cl`). It is diagonalised by the
class-group characters because the `xihat` matrices are group matrices, i.e. their entries depend
only on `C_1^{-1} C_2`. **That is a genuinely arithmetic hypothesis about the cusps, not a symmetry
of the graph:** the class group acts *simply transitively* on the cusps by construction. The brief's
D3 diagram has automorphism group only the Klein four-group and `S(L1) = 12 != S(Q) = 4`, so the
`h x h` matrix of a graph of groups is *not* forced to be a group matrix. Nothing found asserts that
the tree-quotient scattering matrix of `GL_2(R)` for an elliptic `R` is a `Pic(R)`-group matrix.
This is precisely the gap the brief marks H-CLASS, and it remains open.

Independent confirmation of the cusps/class-group bijection in the Bianchi setting,
`2603.16518:qe_eisseries.tex:188`:

```
Let $h=h_F$ be the class number of $F$. Throughout this paper, we assume $h>1$. Then it is well known that the number of $\Gamma$-inequivalent cusps is $h$, because there is a bijection between the class group $\Cl_F$ and the set of $\Gamma$-equivalence classes of the cusps of $\Gamma$.
```

    $ grep -n -F "the number of \$\Gamma\$-inequivalent cusps is \$h\$, because there is a bijection between the class group" refs/src/2603.16518/qe_eisseries.tex
    188:Let $h=h_F$ be the class number of $F$. Throughout this paper, we assume $h>1$. ... (line as quoted)

Assessment: **exact** -- the brief's "one clean quote" exists and is better than asked for (a full
free proof for a general number field, with Efrat and Efrat--Sarnak as the cited antecedents).

---

## Target 4 -- function-field Bost--Connes systems

### 4a. Jacob, `math/0602554`

Abstract, `math/0602554:BC-for-function-fields.tex:148` -- the KMS classification, and **the
partition function is the Dedekind zeta function of the function field with the place at infinity
removed**:

```
We describe a construction which associates to any function field $k$ and any place $\infty$ of $k$ a $C^*$-dynamical system $(C_{k,\infty},\sigma_t)$ that is analogous to the Bost-Connes system associated to $\QQ$ and its archimedian place. ... We classify the extremal KMS$_\beta$ states of $(C_{k,\infty},\sigma_t)$ at any temperature $0<1/\beta<\infty$ and show that a phase transition with spontaneous symmetry breaking occurs at temperature $1/\beta=1$. At high temperature $1/\beta\geqslant 1$, there is a unique KMS$_\beta$ state. At low temperature $1/\beta<1$, the space of extremal KMS$_\beta$ states is principal homogeneous under $\Gal(K/k)$. Each such state is of type $\I_\infty$ and the partition function is the Dedekind zeta function $\zeta_{k,\infty}$.
```

    $ grep -n -F "Each such state is of type \$\I_\infty\$ and the partition function is the Dedekind zeta function \$\zeta_{k,\infty}\$." refs/src/math/0602554/BC-for-function-fields.tex
    148:We describe a construction which associates to any function field $k$ ... (line as quoted)

The place at infinity is explicitly removed, `math/0602554:BC-for-function-fields.tex:169`:

```
The partition function of the BC system is the Riemann zeta function without the $\Gamma$-factor at infinity. Similarly, we will check (Lemma \ref{xr36}) that the partition function of our system is the zeta function of the field $k$ without the factor corresponding to the place $\infty$ of $k$.
```

    $ grep -n -F "the partition function of our system is the zeta function of the field \$k\$ without the factor corresponding to the place \$\infty\$ of \$k\$" refs/src/math/0602554/BC-for-function-fields.tex
    169:Our system aims to be an analog of the Bost-Connes (BC for short) system ... (line as quoted)

This is directly relevant to the notebook: the "zeta of the curve minus the point at infinity", i.e.
`zeta` of the Dedekind domain `R`, is the same object whose class group indexes the cusps of the
cavity (Target 7). Jacob's own erratum at `:150` records that the high-temperature type is
`III_{q^{-beta d_infty}}` (Neshveyev--Rustad), not `III_{q^{-beta}}`.

### 4b. Consani--Marcolli, `math/0607363`

`math/0607363:main.tex:265-268` -- the partition function is the zeta function of the ring `A`
(again the affine curve), but the system is built over `C_infty`, i.e. quantum statistical mechanics
in positive characteristic:

```
The partition function of such a time evolution is the zeta
function $\zeta_{\bA}(s)=\sum_{I\subset \bA} I^{-s}$, defined in a
``half plane'' of $S_\infty=\bC_\infty^*\times \Z_p$ and
with values in $\bC_\infty$. We prove in Theorem \ref{KMSinvL} that
the points of the moduli space $\cM^1$ of Drinfeld modules define
KMS functionals for this time evolution, and that the induced action
of symmetries of the quantum statistical mechanical system on KMS
states recovers the class field theory action of $\A_{\K,f}^*/\K^*$
on $\cM^1$.
```

    $ grep -n -F "The partition function of such a time evolution is the zeta" refs/src/math/0607363/main.tex
    265:The partition function of such a time evolution is the zeta

Note the honest caveat for the notebook: these are KMS **functionals** with values in a field of
positive characteristic, not states on a `C*`-algebra, so this system is *not* a channel/Lindbladian
object in the notebook's sense.

### 4c. Neshveyev--Rustad, `1112.5826`

Abstract, `1112.5826:main.tex:163` -- the unifying construction, the phase transition, and the type:

```
With a global function field $K$ with constant field $\F_q$, a finite set $S$ of primes in $K$ and an abelian extension $L$ of $K$, finite or infinite, we associate a C$^*$-dynamical system. The systems, or at least their underlying groupoids, defined earlier by Jacob using the ideal action on Drinfeld modules and by Consani-Marcolli using commensurability of $K$-lattices are isomorphic to particular cases of our construction. We prove a phase transition theorem for our systems and show that the unique KMS$_\beta$-state for every $0<\beta\le1$ gives rise to an ITPFI-factor of type III$_{q^{-\beta n}}$, where $n$ is the degree of the algebraic closure of $\F_q$ in $L$. Therefore for $n=+\infty$ we get a factor of type III$_0$. Its flow of weights is a scaled suspension flow of the translation by the Frobenius element on $\Gal(\bar \F_q/\F_q)$.
```

    $ grep -n -F "We prove a phase transition theorem for our systems and show that the unique KMS" refs/src/1112.5826/main.tex
    163:With a global function field $K$ with constant field $\F_q$ ... (line as quoted)

The KMS classification with the partition function named,
`1112.5826:main.tex:241-253` (Theorem, "tphase"):

```
For the system $(A_{L,S},\sigma)$ we have:
\enu{i} for $\beta<0$ there are no KMS$_\beta$-states;
\enu{ii} for every $0< \beta \leq 1$ there is a
unique KMS$_\beta$-state; \enu{ii} for every  $1< \beta<\infty$ the
extremal KMS$_\beta$-states are indexed by the points of the subset $$Y^0_{L,S}=  \Gal(L/
K)\times_{\oas^*}\oas^* \cong \Gal(L / K)$$ of $Y_{L,S}$, ...
where $\zeta_{K,S}(\beta)=\sum_{D\in\D^+_S} N(D)^{-\beta}$; furthermore, every extremal KMS$_\beta$-state $\varphi_{\beta,w}$ is of type I$_\infty$ and its partition function is $\zeta_{K,S}(\beta)$;
```

    $ grep -n -F "furthermore, every extremal KMS\$_\beta\$-state \$\varphi_{\beta,w}\$ is of type I\$_\infty\$ and its partition function is \$\zeta_{K,S}(\beta)\$" refs/src/1112.5826/main.tex
    253:where $\zeta_{K,S}(\beta)=\sum_{D\in\D^+_S} N(D)^{-\beta}$; ... (line as quoted)

So in all three treatments the partition function is the zeta function of the curve **with the
chosen place(s) removed** -- the same `zeta_R` the cavity's cusps see. The interesting negative for
the notebook: the type-III factor at high temperature is `III_{q^{-beta d_infty}}`, and the flow of
weights is the Frobenius translation; nothing in these papers is a Lax--Phillips/resonance statement
and nothing connects the KMS structure to a scattering matrix. **No source relates function-field BC
to the resonances of the cavity.**

Assessment: **exact** for what the brief asks (KMS classification + partition function + the role of
the place at infinity); **NOT FOUND**: any link between a BC system and the cavity's scattering.

---

## Target 5 -- APW, byte-verified line addresses for the seven items the brief names

All in `refs/src/2603.26443/final_draft.tex`.

**(i) The adjacency operator (eq. `average`), line 442**, with the stabiliser-function setup at 427--434:

```
 Af(v) = \sum_{\overrightarrow{e} \in \vec{\mathcal{E}} : t(\overrightarrow{e}) = v} \frac{\mathcal{S}(v)}{\mathcal{S}(e)}f(o(\overrightarrow{e})).
```

    $ grep -n -F "Af(v) = \sum_{\overrightarrow{e} \in \vec{\mathcal{E}} : t(\overrightarrow{e}) = v}" refs/src/2603.26443/final_draft.tex
    442: Af(v) = \sum_{\overrightarrow{e} \in \vec{\mathcal{E}} : t(\overrightarrow{e}) = v} \frac{\mathcal{S}(v)}{\mathcal{S}(e)}f(o(\overrightarrow{e})).

**(ii) The resonance matrix and `c_v` (and `f_v`), lines 1899, 1901, 1907.** Line 1899 is the
sentence defining `B(mu)`, and it contains **the funnel self-energy the brief asks for in T5**:

```
We now discuss how we may use the results of the previous section to explicitly compute the resonances and generalized resonant states. Let $A_{\mathcal{L}}$ be the adjacency matrix of the induced subgraph corresponding to the compact core $\mathcal{L}$. Let $B(\mu)$ be the diagonal matrix with entry $(v, v)$ equal to $c_v \frac{\sqrt{q}}{\mu} + f_v \frac{1}{\sqrt{q} \mu}$ where
```

    $ grep -n -F "Let \$B(\mu)\$ be the diagonal matrix with entry \$(v, v)\$ equal to \$c_v \frac{\sqrt{q}}{\mu} + f_v \frac{1}{\sqrt{q} \mu}\$ where" refs/src/2603.26443/final_draft.tex
    1899:We now discuss how we may use the results of the previous section ... (line as quoted)

line 1901 (the definitions):

```
    c_v = \sum_{\substack{\textnormal{edge $e$ containing $v$,} \\
    \textnormal{$e$ attached to a cusp}}} \frac{\mathcal{S}(v)}{\mathcal{S}(e)}, \hspace{10mm} f_v = \sum_{\substack{\textnormal{edge $e$ containing $v$,} \\
    \textnormal{$e$ attached to a funnel}}} \frac{\mathcal{S}(v)}{\mathcal{S}(e)}.
```

    $ grep -n -F "c_v = \sum_{\substack{\textnormal{edge \$e\$ containing \$v\$,}" refs/src/2603.26443/final_draft.tex
    1901:    c_v = \sum_{\substack{\textnormal{edge $e$ containing $v$,} \\

line 1907 (the resonance matrix):

```
  H(\mu) \coloneqq  \frac{1}{2 \sqrt{q}}(A_{\mathcal{L}} + B(\mu)) - z(\mu) I.
```

    $ grep -n -F "H(\mu) \coloneqq  \frac{1}{2 \sqrt{q}}(A_{\mathcal{L}} + B(\mu)) - z(\mu) I." refs/src/2603.26443/final_draft.tex
    1907:  H(\mu) \coloneqq  \frac{1}{2 \sqrt{q}}(A_{\mathcal{L}} + B(\mu)) - z(\mu) I.

The proof that follows states the outgoing conditions used by the brief's C1 explicitly
(`f(w) = sqrt(q)/mu_0 f(v)` on a cusp, `f(u) = 1/(sqrt q mu_0) f(v)` on a funnel), same proof, line 1915.

**(iii) The D2 determinant, line 2008, and the sentence identifying `P(mu^2)`, line 2030:**

```
        (\mu^2 + 1)^2 (\mu^2 - 2) (2 \mu^4 - 2 \mu^2 + 1).
```

    $ grep -n -F "(\mu^2 + 1)^2 (\mu^2 - 2) (2 \mu^4 - 2 \mu^2 + 1)." refs/src/2603.26443/final_draft.tex
    2008:        (\mu^2 + 1)^2 (\mu^2 - 2) (2 \mu^4 - 2 \mu^2 + 1).

```
    Letting $P(T)$ denote the numerator, we find that $P(\mu^2)$ is exactly equal to the unaccounted for polynomial in the determinant of the resonance matrix. The Riemann hypothesis (Weil's theorem) implies that all the associated resonances lie on the circle of radius $\frac{1}{2^{\frac{1}{4}}}$.
```

    $ grep -n -F "Letting \$P(T)\$ denote the numerator, we find that \$P(\mu^2)\$ is exactly equal" refs/src/2603.26443/final_draft.tex
    2030:    Letting $P(T)$ denote the numerator, we find that $P(\mu^2)$ is exactly equal to the unaccounted for polynomial in the determinant of the resonance matrix. ...

(The `l^2` statement the brief's T1(c) needs -- "both $\mu = i$ and $\mu = -i$ have two associated
$\ell^2$-eigenfunctions" -- is at line 2014.)

**(iv) The D3 determinant, line 2056, and the "topological" `±1` sentence, line 2058:**

```
        (\mu^2 + 1)^2 (\mu - 1)^2 (\mu + 1)^2 (\mu^2 - 3) (3 \mu^4 + 1).
```

    $ grep -n -F "(\mu^2 + 1)^2 (\mu - 1)^2 (\mu + 1)^2 (\mu^2 - 3) (3 \mu^4 + 1)." refs/src/2603.26443/final_draft.tex
    2056:        (\mu^2 + 1)^2 (\mu - 1)^2 (\mu + 1)^2 (\mu^2 - 3) (3 \mu^4 + 1).

```
    We again get the ``trivial'' resonances at $\mu = \pm \sqrt{3}$. We also compute that we get $\ell^2$-eigenvalues at $\mu = \pm i$ (each of multiplicity 2). We also have resonances at $\mu = \pm 1$ (each of multiplicity 2). However, we compute that they are in fact not $\ell^2$-eigenfunctions.
```

    $ grep -n -F "We also have resonances at \$\mu = \pm 1\$ (each of multiplicity 2). However, we compute that they are in fact not" refs/src/2603.26443/final_draft.tex
    2058:    We again get the ``trivial'' resonances at $\mu = \pm \sqrt{3}$. ... (line as quoted)

The word "topological" for these is in the *figure caption*, line 2049
(`we have additional ``topological'' resonances at $\mu = \pm 1$ (in green)`), and in the
introduction at line 136.

**(v) The four-type expectation list, lines 2088--2095**, and the follow-up sentence:

```
Thus in analogy with the number field setting, we should expect the resonances to be of the following form:
```
(line 2088, end of paragraph), then the four items at 2089--2093:
```
    \item Trivial resonances at $\pm \sqrt{q}$ corresponding to trivial $\ell^2$-eigenfunctions.
    \item Resonances corresponding to the other $\ell^2$-eigenvalues which all lie on the unit circle (the analogue of the Selberg conjecture) as a consequence of Drinfeld's proof of the Langlands correspondence for $\textnormal{GL}(2, \mathbb{F}_q(C))$ \cite{drinfeld2, drinfeld1}.
    \item Resonances on the circle of radius $\frac{1}{q^{\frac{1}{4}}}$ corresponding to square roots of zeros of the Hasse-Weil zeta function of $C$. ...
    \item Resonances at $\mu = \pm 1$ whose multiplicity is related to the number of cusps and the functional equation of the zeta function/trace of the scattering matrix.
```

    $ grep -n -F "Thus in analogy with the number field setting, we should expect the resonances to be of the following form:" refs/src/2603.26443/final_draft.tex
    2088:We now wish to describe how we are observing the same phenomenon ... (line as quoted)
    $ grep -n -F "Resonances corresponding to the other \$\ell^2\$-eigenvalues which all lie on the unit circle" refs/src/2603.26443/final_draft.tex
    2091:    \item Resonances corresponding to the other $\ell^2$-eigenvalues which all lie on the unit circle ...
    $ grep -n -F "Resonances at \$\mu = \pm 1\$ whose multiplicity is related to the number of cusps" refs/src/2603.26443/final_draft.tex
    2093:    \item Resonances at $\mu = \pm 1$ whose multiplicity is related to the number of cusps and the functional equation of the zeta function/trace of the scattering matrix.

and line 2095:

```
We plan to make this correspondence precise in follow-up work connecting resonances with the Lax-Phillips scattering theory in this setting.
```

    $ grep -n -F "We plan to make this correspondence precise in follow-up work" refs/src/2603.26443/final_draft.tex
    2095:We plan to make this correspondence precise in follow-up work connecting resonances with the Lax-Phillips scattering theory in this setting.

Note for T2(c): item 4 says the `±1` multiplicity is tied to **the number of cusps and the trace of
the scattering matrix** -- which is exactly Sørensen's Corollary 9.2
(`sorensen-2001:paper.txt:1616-1620` (`tr Phi(1/2,0,chi) = h[2] - 2`), the 2-torsion of the class group).
That is an independent, checkable prediction for D3: `Pic = Z/4`, so `h[2] = 2` and `h[2] - 2 = 0`,
while the `±1` resonances have multiplicity 2 each. The brief should treat the agreement or
disagreement as a test, not an assumption.

**(vi) The funnel self-energy `f_v / (sqrt q mu)` versus the cusp's `c_v sqrt q / mu`:** line 1899
(quoted in (ii) above). The brief's T5 asks for it "at line 1900"; the actual address is **1899**
for the sentence and **1901** for the two sums.

**(vii) The "cusp forms on the unit circle by Drinfeld" sentence:** line 2091 (quoted above), and the
introduction's version, line 136:

```
In particular, we observe that the resonances correspond to the ``trivial'' $\ell^2$-eigenvalues ($\pm \sqrt{q}$), the remaining $\ell^2$-eigenvalues (which are known to all lie on the unit circle as a result of Drinfeld's proof of the Langlands correspondence and Petersson conjecture for $\textnormal{GL}(2)$ over function fields \cite{drinfeld2, drinfeld1}), the square roots of the zeros of the Hasse-Weil zeta function (which are known to all lie on the circle of radius $\frac{1}{\sqrt{q}}$ as a result of Weil's proof of the Riemann hypothesis in this setting \cite{weil}), and additional ``topological'' resonances at the special values $\pm 1$.
```

    $ grep -n -F "the remaining \$\ell^2\$-eigenvalues (which are known to all lie on the unit circle as a result of Drinfeld's proof" refs/src/2603.26443/final_draft.tex
    136:It is a consequence of our results that resonances can be computed explicitly ... (line as quoted)

(Careful: APW write "circle of radius `1/sqrt q`" at line 136 for the Hasse--Weil zeros of `P(T)` in
the variable `T`; in the resonance variable `mu` with `T = mu^2` this is radius `q^{-1/4}`, as they
write at line 2092 and at line 2030. Both are correct in their own variable; the brief's `q^{-1/4}`
is the `mu` statement.)

---

## Target 6 -- Childs--Gosset, `1203.6557`

The `h`-tail S-matrix, `1203.6557:levinson2.tex:365`:

```
S(z) & =-Q(z)^{-1}Q(z^{-1})\label{eq:S_matrix}
```

    $ grep -n -F "S(z) & =-Q(z)^{-1}Q(z^{-1})\label{eq:S_matrix}" refs/src/1203.6557/levinson2.tex
    365:S(z) & =-Q(z)^{-1}Q(z^{-1})\label{eq:S_matrix}

with `Q` defined immediately below (line 369,
`Q(z) := 1 - z(A + B^dagger (1/z + z - D)^{-1} B)`) and unitarity on the circle proved at 373--380.

The Levinson count, `1203.6557:levinson2.tex:508-512`:

```
The winding number of the determinant of the S-matrix around
the unit circle $\Gamma$ is
\[
w_{\Gamma}(\det(S))=2\left(m-n_{b}-n_{c}-\frac{1}{2}n_{h}\right).
\]
```

    $ grep -n -F "The winding number of the determinant of the S-matrix around" refs/src/1203.6557/levinson2.tex
    508:The winding number of the determinant of the S-matrix around
    $ grep -n -F "w_{\Gamma}(\det(S))=2\left(m-n_{b}-n_{c}-\frac{1}{2}n_{h}\right)." refs/src/1203.6557/levinson2.tex
    511:w_{\Gamma}(\det(S))=2\left(m-n_{b}-n_{c}-\frac{1}{2}n_{h}\right).

The half-bound-state count `n_h` (the quantity the brief's C3 wants to read the threshold
multiplicity off) is defined at `1203.6557:levinson2.tex:463`:

```
n_{h} & \defeq \sum_{x=\pm1}\dim\left(\spn\left\{ |\psi\rangle \colon |\psi\rangle\in \Conf_{=}^{\perp} \text{ and }\gamma(x)|\widehat{\psi}\rangle=0\right\} \right).
```

    $ grep -n -F "n_{h} & \defeq \sum_{x=\pm1}\dim" refs/src/1203.6557/levinson2.tex
    463:n_{h} & \defeq \sum_{x=\pm1}\dim\left(\spn\left\{ |\psi\rangle \colon |\psi\rangle\in \Conf_{=}^{\perp} \text{ and }\gamma(x)|\widehat{\psi}\rangle=0\right\} \right).

Assessment: **exact**, both addresses confirmed as the brief gives them.

---

## Target 7 -- number of cusps `= |Pic(R)|`, and the volume of `GL_2(R) \ T`

### 7a. APW's own statement (Serre, Trees, II.2, restated)

`2603.26443:final_draft.tex:892` -- **cusps `<->` `Pic(R)`, stated as a theorem-like assertion**:

```
The structure of the cusps carries geometric information in the language of vector bundles. Let $\textnormal{Pic}(R)$ denote the Picard group of $R$, i.e.\@ the group of isomorphism classes of line bundles on $C^{\textnormal{aff}}$, with group operation given by tensor product (or equivalently the class group of the Dedekind domain $R$). In the case at hand, it turns out that $\textnormal{Pic}(R)$ is finite. Let $c \in \textnormal{Pic}(R)$. We can then form an associated line bundle $L_c$ on $C$. Let $L_P$ be the line bundle corresponding to the divisor $[P]$. Let $L_P^n$ be the $n$th tensor power of $L_P$. Any rank-2 vector bundle of the form $L_c \oplus (L_P^n \otimes L_c^{-1})$ is trivial on $C^{\textnormal{aff}}$. Furthermore, such vector bundles all define distinct elements in \eqref{eqn_function_field_quotient} for $n \geq 1$. Additionally, the corresponding subgraph of groups for $n \geq m_c$ sufficiently large defines a cusp. As we vary over $c \in \textnormal{Pic}(R)$, we obtain distinct cusps, and all cusps arise in this way.
```

    $ grep -n -F "As we vary over \$c \in \textnormal{Pic}(R)\$, we obtain distinct cusps, and all cusps arise in this way." refs/src/2603.26443/final_draft.tex
    892:The structure of the cusps carries geometric information in the language of vector bundles. ... (line as quoted)

with the setup (`R` a Dedekind domain, `Gamma = PGL(2,R)` a lattice in `G = PGL(2,K_P)`, the quotient
`eqn_function_field_quotient`) at lines 862--888, and the general finiteness statement at line 854:

```
On the other hand, if one restricts to the setting of lattices in $\textnormal{PGL}(2, F)$ ... then any lattice $\Gamma$ in such a setting is necessarily geometrically finite, and the quotient has finitely many cusps (possibly none) and no funnels. See Theorem 6.1 of Lubotzky \cite{Lubotzky}. ... Cusps are genuinely a positive characteristic phenomenon
```

    $ grep -n -F "and the quotient has finitely many cusps (possibly none) and no funnels. See Theorem 6.1 of Lubotzky" refs/src/2603.26443/final_draft.tex
    854:On the other hand, if one restricts to the setting of lattices in $\textnormal{PGL}(2, F)$ ... (line as quoted)

This is also the source for the brief's T5 remark that **arithmetic quotients of this kind have no
funnels**: a funnel-plus-cusp diagram is *not* an arithmetic quotient of the tree by a lattice in
`PGL(2,F)`. The brief should record that as a constraint on the "smallest candidate" it proposes.

### 7b. Lorscheid's counting formula (independent, with the `deg x` factor)

`1012.3513:hecke.tex:992` -- the number of cusps counted exactly:

```
 The number of cusps is $\#\Cl\cO_X^x \,=\,\#(\rquot{\Cl X}{\langle x\rangle}) \,=\, \#\Cl^0X\cdot\#(\ZZ/d_x\ZZ)\,=\,h_Xd_x$.
```

    $ grep -n -F "The number of cusps is \$\#\Cl\cO_X^x \,=\,\#(\rquot{\Cl X}{\langle x\rangle}) \,=\, \#\Cl^0X\cdot\#(\ZZ/d_x\ZZ)\,=\,h_Xd_x\$." refs/src/1012.3513/hecke.tex
    992: The number of cusps is $\#\Cl\cO_X^x \,=\,\#(\rquot{\Cl X}{\langle x\rangle}) \,=\, \#\Cl^0X\cdot\#(\ZZ/d_x\ZZ)\,=\,h_Xd_x$. ...

and `1012.4825:elliptic.tex:305` (same statement, genus-one paper, with the cusp shape):

```
consequently there are $h\deg x$ cusps where $h=\#\Cl^0 X$ is the class number of $F$.
```

    $ grep -n -F "consequently there are \$h\deg x\$ cusps where \$h=\#\Cl^0 X\$ is the class number of \$F\$." refs/src/1012.4825/elliptic.tex
    305: We recall the definitions of the nucleus and the cusps of $\cG_x$. ... (line as quoted)

and the Serre statement itself in Lorscheid's words, `1012.3513:hecke.tex:146`:

```
Let $\cO^x_F\subset F$ be the Dedekind ring of all elements $a\in F$ with $\norm a_y\leq 1$ for all places $y\neq x$. Put $\Gamma=\PGL_2(\cO^x_F)$. Serre investigates in \cite{Serre} the quotient graph $\lquot{\Gamma}{\cT_x}$. It is the union of a finite connected graph with a finite number of cusps.
```

    $ grep -n -F "It is the union of a finite connected graph with a finite number of cusps." refs/src/1012.3513/hecke.tex
    146:Every subgroup of $\PGL_2(F_x)$ acts on $\cT_x$ by multiplication from the left. ... (line as quoted)

**Important refinement of the brief:** for a place `x` of degree `d_x > 1` the number of cusps is
`h * d_x`, not `h`. Both D2 and D3 use a rational point (`d_x = 1`), so `h = |Pic(R)|` there; the
brief's T6 generalisation to other curves must carry the `deg x` factor.

**Volume of `GL_2(R) \ T`: NOT FOUND** as a closed formula in any fetched source. APW give only the
qualitative statement (finite volume `<=>` lattice, line 852: "a discrete subgroup
`Gamma < Aut(T)` is a lattice if and only if `Gamma \\ T` has finite volume"). The brief's T5 only
needs `sum_v 1/S(v) < infinity`, which is that statement, so no numerical volume is required.

Assessment: **exact** for cusps `= |Pic(R)|` (two independent sources, one of them APW's own text);
**NOT FOUND** for a closed-form volume, and not needed.

---

## Closing table: which hypothesis does each source support, contradict, or leave open?

`S` = supports, `C` = contradicts, `O` = leaves open / no bearing, `~` = partial (see the note).
"Funnel" = the brief's T5 funnel self-energy `f_v/(sqrt q mu)`; "BC" = function-field Bost--Connes.

| source | H-DIAG-2 | H-DIAG-3 | H-EIS | H-CLASS | H-HECKE | Funnel | BC |
|---|---|---|---|---|---|---|---|
| `2603.26443` (APW) | S (the data's origin, via Takahashi) | S (same) | ~ S (asserts the Eisenstein mechanism, proves nothing; `±1` tied to #cusps + `tr S`) | ~ S (cusps = `Pic(R)`, line 892; no matrix) | O | **S** (`f_v/(sqrt q mu)` at 1899/1901; funnels are *excluded* for arithmetic lattices, line 854) | O |
| `1012.4825` (Lorscheid, elliptic) | **S** (full weight-by-weight match, figure-read) | **O**, and warns the natural substitute is a different graph (`:227`, `:309`) | ~ S (`zeta_F` with `h`, `:927`; temperedness `<=>` RH, `:993`) | O | O | O | O |
| `1012.3513` (Lorscheid, Hecke graphs) | ~ S (same graphs, weights) | O | O | ~ S (cusps `= h d_x`, `:992`) | ~ S (defines the Hecke operator on the quotient graph -- the double-coset data H-HECKE says is missing) | O | O |
| `1012.3223` (Lorscheid, toroidal) | O | O | **S, partially** (constant term + `M_chi(s)`, `:563`; genus factor `chi^2(fc)|fc|^{2s}`, `deg fc = 2g-2`, `:573`/`:187`) -- does **not** give the brief's `q^{1-2gs}` in the ray normalisation | ~ S (Eisenstein series indexed by unramified Hecke characters = characters of `Cl`) | O | O | O |
| `sorensen-2001` | O | O | ~ S (the number-field analogue of the `2s-1 / 2s` ratio) | **S, exactly** (`Phi = xihat(2s)^{-1} xihat(2s-1) P`, Thm 7.2; Dedekind-determinant diagonalisation, Prop. 8.1; `det Phi = sign(Cl) prod_psi xi(2s-1,psi)/xi(2s,psi)`, Cor. 8.2; `zeta_H` at Cor. 8.3) -- **but only because the class group acts simply transitively on the cusps, which is unproved for the graph-of-groups cavity** | O | O | O |
| `2603.16518` (Bianchi QE) | O | O | O | ~ S (cusps `<->` `Cl_F`, `:188`) | O | O | O |
| `1203.6557` (Childs--Gosset) | O | O | O | O | O | O | O |
| `math/0602554` (Jacob) | O | O | O | O | O | O | **S** (KMS classified; partition function `= zeta_{k,infty}`, the curve minus the place at infinity) |
| `math/0607363` (Consani--Marcolli) | O | O | O | O | O | O | **S** with caveat (KMS *functionals* valued in `C_infty`, `zeta_A(s) = sum_{I subset A} |I|^{-s}`) |
| `1112.5826` (Neshveyev--Rustad) | O | O | O | O | O | O | **S** (unifies Jacob and Consani--Marcolli; phase transition; partition function `zeta_{K,S}`; type `III_{q^{-beta n}}`; flow of weights = Frobenius) |
| Takahashi 1993 | (would settle) | (would settle) | O | O | O | O | O |
| Li 1979, Gekeler 1995, Gekeler--Nonnengardt 1995, Weil LNM 189, Efrat 1987, Efrat--Sarnak 1985, Hejhal LNM 1001 | -- all **NOT FOUND**; recorded bibliographically only -- | | | | | | |

### Things the round should not assume

1. **H-DIAG-3 has no independent confirmation.** The only free `h = 4` picture of the same curve
   (Lorscheid's `G_x`) is a *disconnected, 7-vertex-nucleus* graph, which by his own line 227 is a
   different object from `Gamma \ T` when the class number is even. The four-cusp count is confirmed;
   the core is not.
2. **H-CLASS is a theorem in the number-field case (Sørensen) only because the class group acts
   simply transitively on the cusps.** No source asserts the analogous group-matrix structure for the
   `h x h` scattering matrix of a graph of groups, and the D3 diagram's automorphism group (Klein
   four) is not `Pic(R) = Z/4`. The brief's own numerics (T2(d)) already point the same way.
3. **H-EIS's `q^{1 - 2gs}`** is not established. What is established is that the adelic functional
   equation carries a monomial `chi^2(fc) |fc|^{2s}` with `deg fc = 2g - 2`; the translation to the
   ray normalisation is nowhere in the literature found.
4. **Arithmetic quotients of the tree by a lattice in `PGL(2,F)` have no funnels** (APW line 854,
   citing Lubotzky Thm 6.1). The brief's T5 "one cusp and one funnel" candidate is therefore *not*
   an arithmetic quotient of this type; it would have to be built by hand.
5. **No source connects a function-field Bost--Connes system to a scattering matrix or to
   resonances.** The only shared object is `zeta_R`, the zeta function of the curve with the place at
   infinity removed, which is both the BC partition function and the ratio in the cavity's reflection
   coefficient.
