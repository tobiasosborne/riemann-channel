# Sources for the Weil positivity criterion for transfer operators

Written 2026-09-12 by the source-acquisition worker. Every quote below was copied
out of the arXiv **TeX source** in `refs/src/<id>/` (fetched by
`refs/fetch_sources.sh`, hashes in `refs/manifest.sha256`) and is cited as
`<id>:<file>:<line-range>`; each quote is whole and contiguous in the lines
stated, so it can be re-checked with `sed -n '<a>,<b>p'`. Preference throughout:
TeX source, never PDF text.

New ids appended to `refs/fetch_sources.sh` for this note:
`math/9811068 2006.13771 1608.03679 math-ph/0505052 math/0404394 math/0506326 1905.13485 1403.0079 2009.02802 2206.03682`.
One id was **removed** again: `math-ph/0404030` is *not* Voros (arXiv serves a
paper on `k`-decomposability of positive maps at that identifier); the Voros
paper is `math/0506326`. `fetch_sources.sh` now also hashes `lambda2.txt`,
because Coffey's main LaTeX file carries a `.txt` extension.

The target statement of the notebook is: for a finite-dimensional `X`, trivial
eigenvalues removed, `nu_l = r^{-l}(Tr X^l - trivial)` is a positive-definite
sequence (Herglotz/Toeplitz) iff all nontrivial `|mu| <= r`, and with the duality
`mu -> r^2/conj(mu)` iff `|mu| = r`. Sections W1–W3 supply the number-theoretic
instance (Weil), W4–W5 the Li reformulation, W6 the graph instance, W7 the
quantum-expander bound, W8–W9 the two representation theorems, W10 the PT
remark, W11 the closest prior art on the *continuous* side (Suzuki's screw
function: RH as non-negative definiteness of a kernel, i.e. the Kreĭn/Herglotz
mechanism applied to zeta). The two closest prior-art items are **W6** (graphs)
and **W11** (zeta); read those two sections before claiming novelty.

---

## W1. Connes 1998: Weil positivity as positive-type-ness of the Weil distribution

**arXiv:math/9811068** — `math/9811068:main.tex:127-127` `\centerline{\bf Trace formula in noncommutative Geometry and}` / `math/9811068:main.tex:131-131` `\centerline{\bf the zeros of the Riemann zeta function}`; author
`math/9811068:main.tex:135-135` `\centerline{Alain CONNES}`. (Plain TeX; there is no `\title` macro, title and author are set
with `\centerline`.)

Positivity is the hinge between the trace formula and RH:

- `math/9811068:main.tex:2514-2516`
```
 What we shall show however is that the trace formula (16) 
implies the positivity of the Weil distribution, and hence 
the validity of RH for $k$. Remember that we are still in 
```

The equivalence is Theorem 5:

- `math/9811068:main.tex:2523-2540`
```
\noindent {\bf Theorem 5.} {\it Let $k$ be a global field
 of positive characteritic and $Q_{\L}$ be the orthogonal
 projection on the subspace of $L^2(X)$ spanned by the
 $f \in \Sc(A)$ such that $f(x)$ and $\wh f(x)$ vanish
 for $\vert x \vert > \L$ . Let $h \in \Sc (C_k)$ have
 compact support. Then the following conditions are equivalent, 
\smallskip

a) When 
 $\L \ra \ify$, one has
$$
{\rm Trace} \, (Q_{\L} \, U(h)) = 2h (1) \log' \L + \sum_{v } 
\int'_{k^*_v} {h(u^{-1}) 
\over \vert 1-u \vert} \, d^* u + o(1)
$$  }
\smallskip
{\it b) All $L$ functions with Gr\"ossencharakter on $k$ satisfy the 
Riemann Hypothesis.}
```

The positivity itself is stated as *positive type* of a distribution on the idele
class group — this is the `Delta(f * f^*) >= 0` form that the notebook's
`nu_l` positive-definiteness is the finite-dimensional shadow of:

- `math/9811068:main.tex:2591-2601`
```
and for any $ \L$ the following distribution on $C_k$ is of positive 
type,
$$
  \D_{ \L}(f) = \,  {\rm Trace} \, (( S_{ \L}- \, Q'_{ \L,0}) \, V(f))  
, \leqno (24)
$$
i.e. one has,
$$
\D_{ \L}(f * f^*) \geq \, 0 , \leqno (25)
$$
where $ f^*(g)= \, \ov f(g^{-1})$ for all $g \in C_k$.
```

And the explicit formula it rests on (Connes' Theorem 6, the Weil explicit
formula rewritten multiplicatively):

- `math/9811068:main.tex:4793-4798`
```
Let $h \in \Sc (C_k)$ have compact support, then
$$
\wh h (0) + \wh h (1) - \sum_{L(\Xc , \rho) = 0 \atop 0 < {\rm Re} \rho 
< 1} \wh h (\Xc , \rho) = \sum_v \int'_{k_v^*} {h(u^{-1}) \over \vert 
1-u \vert} \, d^* u
$$
```

**Conventions fixed by the source.**
- `f^*(g) = conj f(g^{-1})` (`math/9811068:main.tex:2601`), so `f * f^*` is the
  convolution square and `Delta(f*f^*) >= 0` is exactly "`Delta` is of positive
  type" on the locally compact group `C_k`; via Bochner for `C_k` this is the
  positivity of the Fourier transform of `Delta`, i.e. Weil's criterion.
- The zero sum runs over the zeros of all Hecke `L`-functions with
  Grössencharakter in the **open** critical strip `0 < Re rho < 1`, and
  `hat h(X, z) = int h(u) X(u) |u|^z d^*u`. The trivial contributions are the two
  separate terms `hat h(0) + hat h(1)` — the analogue of the notebook's
  "trivial eigenvalues removed".
- Connes works in **positive characteristic** for the equivalence of Theorem 5
  (where RH is Weil's theorem); the global characteristic-zero case is the
  conjecture.

---

## W2. Connes–Consani 2020: the Weil criterion in its cleanest quotable form

**arXiv:2006.13771** — `2006.13771:weil-compo.tex:69-69` `\title{Weil positivity and Trace formula\\ the archimedean place}`; authors `2006.13771:weil-compo.tex:71-71` `\author{Alain Connes}` and `2006.13771:weil-compo.tex:75-75` `\author{Caterina Consani}`.

The explicit formula and Weil's equivalence, stated in one place:

- `2006.13771:weil-compo.tex:99-103`
```
It was shown  by A. Weil  \cite{Weil}  that the Riemann Hypothesis (RH) is equivalent to the negativity of the right-hand  side of the Riemann-Weil explicit formula \cite{EB} (Appendix~\ref{appendix2}: \eqref{bombieriexplicit}) 
\begin{equation}\label{explicit form}
\tilde f(0)-\sum_{\rho\in Z}\tilde f(\rho)+\tilde f(1)=\sum_v {\mathcal W}_v(f), \qquad  \tilde f(s):=\int_0^\infty f(x)x^{s-1}dx
\end{equation}
 where $Z$ is the multi-set of non-trivial zeros of the Riemann zeta function and for a precise class of complex-valued test functions on the positive half-line, of the form 
```

The criterion itself, with the involution made explicit
(`g^sharp(x) := x^{-1} g(x^{-1})`, `bar g(x) = conj(g(x))`):

- `2006.13771:weil-compo.tex:107-110`
```
In fact, following \cite{yoshida}, it is enough to prove the negativity of the right-hand  side of \eqref{explicit form} for  functions $g$ with compact support in the (locally compact) multiplicative group $\R_+^*=(0,\infty)$.  Furthermore, given any finite set of complex numbers $F\supset \{0,1\}$, $F\cap Z=\emptyset$, using the notation  $g^\sharp(x):=x^{-1}g(x^{-1}), \ \bar g(x)=\overline{g(x)}$, one has (Appendix \ref{apppositivity}, Proposition~\ref{mainprop})  
\begin{equation}\label{weilnegav}
RH \iff \sum_v {\mathcal W}_v(g*\bar g^\sharp)\leq 0, \quad \forall g\in C_c^\infty(\R_+^*)\mid \tilde g(z)=0,\ \forall z\in F.
\end{equation}
```

Restated as a proposition in the appendix:

- `2006.13771:weil-compo.tex:2075-2079`
```
\begin{prop}\label{mainprop} Let $Z\subset \C$ be the set of non-trivial zeros of the Riemann zeta function and $F \subset \C$ a finite set disjoint from $Z$ and containing $\{0,1\}$, then
\begin{equation}\label{appendweilnegav}
RH \iff \sum_v {\mathcal W}_v(g*\bar g^\sharp)\leq 0, \quad \forall g\in C_c^\infty(\R_+^*)\mid \tilde g(z)=0,\ \forall z\in F.
\end{equation} 	
\end{prop}
```

The underlying (Bombieri-normalised) explicit formula:

- `2006.13771:weil-compo.tex:2038-2041`
```
 Then, with $f^\sharp(x):=x^{-1}f(x^{-1})$  the explicit formula takes the form 
 \begin{equation}\label{bombieriexplicit}
 \sum_{\rho}\tilde f(\rho)=\int_0^\infty f(x)dx+\int_0^\infty f^\sharp(x)dx-\sum_v {\mathcal W}_v(f),
 \end{equation}
```

**Conventions fixed by the source.**
- Mellin, not Fourier: `tilde f(s) := int_0^infty f(x) x^{s-1} dx`
  (`2006.13771:weil-compo.tex:2035-2036`), and the spectral side is
  `sum_rho tilde f(rho)` over the multiset `Z` of nontrivial zeros.
- The test function is `f = g * bar g^sharp`; with this involution
  `tilde f(rho) = tilde g(rho) conj(tilde g(1 - conj rho))`, which is the
  notebook's `sum_rho ghat(rho) conj(ghat(1 - conj rho))`. The source does
  **not** display that product identity; it is stated in the Lagarias form of
  W3 below, which is the one to cite for the exact expression.
- **Sign**: Connes–Consani write the criterion as `<= 0` on the *geometric*
  side `sum_v W_v`, because the explicit formula puts the zero sum and the
  place sum on opposite sides. The notebook's `>= 0` is the spectral side.
- `F` is any finite set with `{0,1} subset F`, `F cap Z = empty`, and the test
  functions are required to have `tilde g` vanishing on `F` — the analogue of
  "trivial eigenvalues removed".

---

## W3. Lagarias 2005: the Weil scalar product `sum_rho F(rho) conj(G(1 - conj rho))`, and Li = Weil

**arXiv:math/0404394** — `math/0404394:main.tex:143-143` `{\Large {\bf  Li  Coefficients for Automorphic $L$-Functions}}\\`; author `math/0404394:main.tex:146-146` `{\em Jeffrey C. Lagarias} \\`.

Abstract (Li's criterion, and the announcement that the `lambda_n` are values of
Weil's quadratic functional):

- `math/0404394:main.tex:156-171`
```
\noindent
Xian-Jin Li gave a criterion for the Riemann
hypothesis in terms of the positivity of
the set of coefficients
$\lambda_n = \sum_{\rho} 1 - \left( 1 - \frac{1}{\rho}\right)^n$,
$(n= 1, 2, ...)$,
in which $\rho$ runs over the nontrivial zeros of the
Riemann zeta function. We define  similar 
coefficients $\lambda_n(\pi)$ associated to principal automorphic
$L$-functions $L(s, \pi)$ over $GL(N)$.
 We relate these cofficients
to values of Weil's quadratic functional 
associated to the representation $\pi$ on a suitable
set of test functions. The positivity of the
real parts of these coefficients is a necessary and sufficient 
condition for the Riemann hypothesis for $L(s, \pi)$ to hold.
```

Li's criterion in the general (automorphic) form:

- `math/0404394:main.tex:1098-1102`
```
\begin{theorem}~\label{Nth22}
Let $\pi$ be an irreducible cuspidal
unitary automorphic representation of $GL(n)$. The following
conditions are each equivalent to the 
Riemann hypothesis for $\xi(s, \pi)$.
```

- `math/0404394:main.tex:1108-1111`
```
(1) For all $n \ge 1$, 
\beql{N217a}
\Re \left( \lambda_n(\pi) \right) \ge 0.
\eeq
```

**The definition the notebook needs verbatim** — the Weil scalar product is
exactly the pairing `sum over zeros of F(rho) conj(G(1 - conj rho))`:

- `math/0404394:main.tex:1243-1250`
```
Given $F(s), G(s) \in \sA$ we define the {\em
Weil scalar product}  associated to
the automorphic representation $\pi$ by 
\beql{301}
\langle F, G \rangle_{\sW(\pi)} := \sum_{ \rho \in Z(\pi) }
F(\rho) \overline{G( 1 - \bar{\rho})}.
\eeq
The sum on the right counts zeros with
```

and RH is precisely the statement that this pairing is a positive semidefinite
Hermitian form, because `rho = 1 - conj rho` iff `Re rho = 1/2`:

- `math/0404394:main.tex:1268-1281`
```
The Riemann hypothesis for $\Lambda(s, \pi)$ implies
that the Weil scalar product is positive semidefinite on
the test function vector space $\sA$. To see
this we note that  
$\rho= 1 - \bar{\rho}$ holds if and only if 
$\rho$ lies on the critical line $\Re(s) = \frac{1}{2}.$
The Riemann hypothesis implies that for all $F(s) \in \sA$, 
$$
\langle F, F \rangle_{\sW(\pi)} = \sum_{ \rho \in Z(\pi) } 
F(\rho) \overline{F(1 - \bar{\rho})}
= \sum_{ \rho \in Z(\pi) }
F(\rho) \overline{F(\rho)} = \sum_{ \rho \in Z(\pi) }
|F(\rho)|^2 \ge 0.
$$
```

Li's criterion is then the specialisation of this form to one distinguished
family of test functions `G_n(s) = 1 - (1 - 1/s)^n`:

- `math/0404394:main.tex:1334-1345`
```

\begin{theorem}~\label{th31}
Let $\pi$ be an irreducible cuspidal unitary automorphic representation
of $GL(N)$, with  associated $\xi$-function
$\xi(s, \pi)$
and with Weil scalar product $\langle \cdot, \cdot \rangle_{\sW(\pi)}$.
For the Li test functions  $G_n(s) = 1 - (1 - \frac{1}{s})^n$
there holds 
\beql{304}
\langle G_n, G_m \rangle_{\sW(\pi)} = 
\lambda_n(\pi) + \lambda_{-m}(\pi) - \lambda_{n-m}(\pi).
\eeq
```

stated again in the introduction:

- `math/0404394:main.tex:333-337`
```
The third observation
was that  each positivity condition  $\lambda_n \ge 0$  
encodes ``Weil positivity''
of Weil's quadratic functional 
for a particular test function $g_n(x)$.
```

and the Bombieri–Lagarias reformulation is quoted as:

- `math/0404394:main.tex:400-404`
```
The results of \cite{BL99}  apply to give a
Riemann hypothesis criterion for $L(s, \pi)$ in the
form: The Riemann hypothesis holds for $L(s, \pi)$ 
if and only if the real parts  $\Re(\lambda_n(\pi))$ are nonnegative for all 
 $n \ge 0.$
```

**Conventions fixed by the source.**
- `Z(pi)` is the multiset of zeros counted with multiplicity, invariant under
  `rho -> 1 - conj rho`; this involution is exactly the notebook's duality
  `mu -> r^2 / conj(mu)` after `mu = q^{-rho}`-type substitution (the source
  does not make that substitution).
- The pairing is linear in the first and **conjugate-linear in the second**
  argument, with Hermitian symmetry `<F,G> = conj<G,F>`.
- One direction is elementary (`RH => psd`); the converse needs a test-function
  class rich enough to separate the zeros — the source says so explicitly
  (`math/0404394:main.tex:1282-1293`). This is the same gap the notebook must
  close when it asserts "iff".
- Theorem `th31` gives `<G_n, G_m> = lambda_n(pi) + lambda_{-m}(pi) -
  lambda_{n-m}(pi)`, i.e. the `lambda_n` are **not** the diagonal of the form
  but a linear combination of Gram entries; the criterion `Re lambda_n >= 0`
  follows from semidefiniteness, not conversely term by term.

---

## W4. Voros 2006: Li's criterion, plain statement

**arXiv:math/0506326** — `math/0506326:main.tex:19-20` `\title{Sharpenings of Li's criterion\\` / `for the Riemann Hypothesis}`; author `math/0506326:main.tex:22-22` `\author{{\bf Andr\'e Voros}\footnote{Also at: `.

- `math/0506326:main.tex:46-48`
```
\emph{Li's criterion} for the Riemann Hypothesis (RH) states that the latter 
is true if and only if a specific real sequence $\{ \lambda_n \}_{n=1,2,\ldots}$
has \emph{all its terms positive} \cite{LI1,BL}.
```

- `math/0506326:main.tex:74-78`
```
(in the notations of Li, whose $\lambda_n$ are $n$ times Keiper's)
\begin{equation}
\label{LDef}
\lambda_n = \sum_\rho \, [1-(1-1/\rho)^n] \qquad (n=1,2, \ldots),
\end{equation}
```

Attribution of the reformulation:

- `math/0506326:main.tex:115-118`
```
Our results \cite{V} mainly relate to those of Keiper \cite{K},
of which we only learned later (thanks to K. Ma\'slanka; they were almost never cited),
of Bombieri--Lagarias \cite{BL} on Li's criterion \cite{LI1}, 
and of Ma\'slanka \cite{M1}.
```

**Caveat on the file.** `refs/src/math/0506326/main.tex` is **ISO-8859 (latin-1)
encoded**, and GNU `grep` on this box exits 1 on it without matching. Read it
with `python3 ... errors="replace"` (which is what `scripts/labbook_check.py`
does); every quote above is pure ASCII, so the gate's `errors="replace"`
decoding does not disturb them.

---

## W5. Coffey 2005: Li's criterion, second independent statement

**arXiv:math-ph/0505052** — `math-ph/0505052:lambda2.txt:7-8` `\title{Toward verification of the Riemann hypothesis:  Application of` / `the Li criterion}`; author `math-ph/0505052:lambda2.txt:10-10` `\author{Mark W. Coffey\\`.

- `math-ph/0505052:lambda2.txt:114-118`
```
The sequence $\{\lambda_n\}_{n=1}^\infty$ is defined by
$$\lambda_n = {1 \over {(n-1)!}}{d^n \over {ds^n}}[s^{n-1}\ln \xi(s)]_{s=1}.
\eqno(1)$$
Then Li's criterion for the Riemann hypothesis to hold is that all 
$\{\lambda_n\}_{n=1}^\infty$ are nonnegative \cite{li}.  We note that Li's
```

**Caveat on the file.** The arXiv tarball's main LaTeX file is named
`lambda2.txt`, not `*.tex` (the `*.tex` members are only appendices D–L). Cite
it as `math-ph/0505052:lambda2.txt:<line>`; `refs/fetch_sources.sh` now hashes
it explicitly.

---

## W6. Huang 2019: **the prior art** — Ramanujan iff a cycle-count sequence is nonnegative

**arXiv:1905.13485** — `1905.13485:revision_graph_Licriterion.tex:96-96` `\title[Ihara zeta function, coefficients of Maclaurin series, and Ramanujan graphs]{Ihara zeta function, coefficients of Maclaurin series, and Ramanujan graphs}`; author `1905.13485:revision_graph_Licriterion.tex:99-99` `\author{Hau-Wen Huang}`.

This is the closest published analogue of what the notebook is proving on the
graph side: a Li/Weil-type positivity criterion for the Ramanujan property,
expressed through the non-backtracking ("geodesic") cycle counts.

Li's criterion, as the paper's model:

- `1905.13485:revision_graph_Licriterion.tex:189-189`
```
Li's criterion states that the Riemann hypothesis holds if and only if $\lambda_k\geq 0$ for all $k\geq 1$ \cite{Li:1997}.
```

Cycle counts and the Ihara zeta:

- `1905.13485:revision_graph_Licriterion.tex:205-212`
```
A cycle is said to be {\it geodesic} if all shifted cycles are backtrackless. 
For all $k\geq 1$ let $N_k$ denote the number of geodesic cycles on $X$ of length $k$. 
The {\it Ihara zeta function} $Z(u)$ of $X$ is the analytic continuation of 
\begin{gather}\label{zeta}
\exp
\left(\sum_{k=1}^\infty \frac{N_k}{k} u^k
\right).
\end{gather}
```

Ramanujan = RH for the Ihara zeta, with the trivial eigenvalues/poles named:

- `1905.13485:revision_graph_Licriterion.tex:217-222`
```
For the rest of this paper, we always assume that $X$ is a connected $(q+1)$-regular undirected graph of finite order $n$ with $q\geq 1$ and $n\geq 3$. 
In this case, the eigenvalues of $X$ with absolute value $q+1$ are called {\it trivial} eigenvalues and the poles of $Z(u)$ with values $\pm 1$ and $\pm q^{-1}$ are called {\it trivial} poles. The graph $X$ is said to be {\it Ramanujan} whenever 
$$
|\lambda|\leq 2q^{\frac{1}{2}}
$$
for all nontrivial eigenvalues $\lambda$ of $X$ \cite{Ramanujan1988}. The graph $X$ is Ramanujan if and only if all nontrivial poles of $Z(u)$ have the same absolute value $q^{-\frac{1}{2}}$, which is similar to the Riemann hypothesis by writing $u=q^{-s}$ \cite{Winnie2019,Terras2010}. We define the function $\Xi(u)$ by 
```

The sequence, as Maclaurin coefficients of `d/du log Xi(q^{-1/2} u)`:

- `1905.13485:revision_graph_Licriterion.tex:251-257`
```
\begin{defn}\label{defn:hk}
Let $\{h_k\}_{k=1}^\infty$ denote the number sequence given by
\begin{gather*}
\frac{d}{du}\ln \Xi(q^{-\frac{1}{2}} u)
=\sum_{k=0}^\infty h_{k+1} u^k.
\end{gather*}
\end{defn}
```

**The criterion:**

- `1905.13485:revision_graph_Licriterion.tex:287-296`
```
\begin{thm}\label{thm:Li}
The following are equivalent:
\begin{enumerate}
\item $X$ is Ramanujan.

\item $h_k\geq 0$ for all $k\geq 1$.

\item $h_k\geq 0$ for infinitely many even $k\geq 2$. 
\end{enumerate}
\end{thm}
```

**The explicit formula linking `h_k` to the cycle counts** — this is the graph
analogue of the notebook's `nu_l = r^{-l}(Tr X^l - trivial)`:

- `1905.13485:revision_graph_Licriterion.tex:440-469`
```
\begin{prop}\label{prop:formula1}
\begin{enumerate}
\item If $X$ is nonbipartite then 
\begin{gather*}
h_k
=
\left\{
\begin{array}{ll}
2(n-1)
+
q^{\frac{k}{2}}
+q^{-\frac{k}{2}}
-q^{-\frac{k}{2}} N_k 
\qquad 
&\hbox{for all odd $k$},
\\
2(n-1)
+
q^{\frac{k}{2}}
+q^{-\frac{k}{2}}
-
q^{-\frac{k}{2}}
\left(
N_k-n(q-1)
\right)
\qquad 
&\hbox{for all even $k$}.
\end{array}
\right.
\end{gather*}
```

**Conventions fixed by the source, and how far the overlap goes.**
- `X` is a connected `(q+1)`-regular undirected graph, order `n >= 3`, `q >= 1`;
  `N_k` counts **geodesic** (backtrackless and tailless after shifting) cycles of
  length `k`; `Z(u) = exp(sum_k N_k u^k / k)`.
- Trivial eigenvalues are those of absolute value `q+1`, trivial poles are
  `u = +-1, +-q^{-1}`. `Xi(u)` divides those out and satisfies
  `Xi(q^{-1}u^{-1}) = Xi(u)` — the graph functional equation, i.e. the
  notebook's duality `mu -> r^2/conj(mu)` at `r = q^{1/2}`.
- The critical radius is `q^{1/2}`: `h_k` is built from `Xi(q^{-1/2}u)`, and the
  formula `h_k = 2(n-1) + q^{k/2} + q^{-k/2} - q^{-k/2} N_k` (nonbipartite, odd
  `k`) is precisely "`q^{-k/2} times (cycle count minus trivial part)`", up to
  sign and an additive constant.
- **The overlap is real but not total.** Huang proves
  `Ramanujan <=> h_k >= 0 for all k`, i.e. **termwise nonnegativity** of a single
  sequence. The notebook's claim is **positive-definiteness in the
  Herglotz/Toeplitz sense** of `nu_l` (every Toeplitz minor `>= 0`). These are
  *different* conditions on a sequence — neither implies the other in general
  (positive-definiteness constrains only `nu_0 >= 0` among the entries
  themselves) — so the two results have to be reconciled, not identified.
  Huang's file contains no occurrence of "Herglotz", "Bochner", "Toeplitz",
  "positive definite" or "positive semidefinite" (full-text scan, 0 hits each).
  So: the *shape* of the result (a positivity
  criterion on non-backtracking cycle counts equivalent to Ramanujan) is prior
  art and must be cited; the *mechanism* (Herglotz/Toeplitz, and the reduction
  to an arbitrary transfer operator) appears not to be.
- Huang's `h_k` also carries the `2(n-1)` constant, which the notebook's
  normalisation does not; any comparison has to account for it.

---

## W7. Hastings 2007: the quantum-expander Ramanujan bound

**arXiv:0706.0556** (already fetched) — `0706.0556:sd10.tex:7-8` `\title{Random Unitaries Give Quantum Expanders}` / `\author{M.~B.~Hastings}`.

- `0706.0556:sd10.tex:118-131`
```
Let $\lambda_2$ be the eigenvalue with the second largest absolute value
of all eigenvalues other than $\lambda_1$.
Let
\be
\lambda_{H}=\frac{2\sqrt{D-1}}{D}.
\ee

The main result of this paper is
that, in the Hermitian case, for any $\epsilon>0$ the probability that
$|\lambda_2|$ is within $\epsilon$ of $\lambda_{H}$ approaches
unity as $N\rightarrow \infty$.  Interestingly, this is the same
as the recently proven tight bound\cite{fried} in the classical
case, but the proof in the
quantum case is much simpler.
```

**Conventions fixed by the source.** `D` is the number of Kraus operators
(`D >= 4` in the Hermitian case, `D >= 2` non-Hermitian), `lambda_2` the
second-largest eigenvalue modulus of the channel. The claim is that
`|lambda_2| -> lambda_H = 2 sqrt(D-1)/D` in probability as `N -> infinity` for
random unitaries — i.e. random quantum expanders are *asymptotically* Ramanujan,
matching the classical Friedman bound. The rigorous bound actually proved in the
paper is the weaker `lambda_loose(D) = sqrt(lambda_H)`
(`0706.0556:sd10.tex:803-806`); do not cite `lambda_H` as a proved bound.

---

## W8. Herglotz's theorem (positive definite sequence = Fourier coefficients of a positive measure)

**arXiv:1403.0079** — `1403.0079:main.tex:67-68` `\title[An extension of Herglotz's theorem to the quaternions]` / `{An extension of Herglotz's theorem to the quaternions} \oddsidemargin` (the `\title` line runs into a layout
macro; the title is the braced argument); authors `1403.0079:main.tex:42-42` `\author[D. Alpay]{Daniel Alpay}`, `1403.0079:main.tex:48-48` `\author[F. Colombo]{Fabrizio Colombo}`,
`1403.0079:main.tex:55-55` `\author[D. P. Kimsey]{David P. Kimsey}`, `1403.0079:main.tex:61-61` `\author[I. Sabadini]{Irene Sabadini}`.

Abstract statement:

- `1403.0079:main.tex:103-107`
```
A classical theorem of Herglotz states that a
function $n\mapsto r(n)$ from $\mathbb Z$ into $\mathbb
C^{s\times s}$ is positive definite if and only there exists a
$\mathbb C^{s\times s}$-valued positive measure $\mu$ on $[0,2\pi]$ such
that $r(n)=\int_0^{2\pi}e^{int}d\mu(t)$for $n\in \mathbb Z$.
```

The Toeplitz formulation — this is the version the notebook uses:

- `1403.0079:main.tex:122-138`
```
pertaining to the complex numbers setting. A function $n\mapsto
r(n)$ from $\mathbb Z$ into $\mathbb C^{s\times s}$ is called
positive definite if the associated function (also called kernel)
$K(n-m)$ is positive definite on $\mathbb Z$. This means that for
every choice of $N\in\mathbb N$ and $n_1,\ldots, n_N\in\mathbb
Z$, the $N\times N$ block matrix with $(j,\ell)$ block entry
equal to the matrix $r(n_j-n_\ell)$ is non-negative, that is, all
the block Toeplitz matrices
\begin{equation}
\label{eq:toeplitz}
\mathbb T_N\stackrel{\rm def.}{=}\begin{pmatrix}r(0)&r(1)&\cdots &r(N)\\
                                         r(-1)&r(0)&\cdots &r(N-1)\\
                                               & & &\\
                                               & & &\\
                                         r(-N)&r(1-N)&\cdots& r(0)\end{pmatrix}
\end{equation}
are non-negative. We will use the notation $\mathbb T_N \succeq 0$.
```

The theorem, with uniqueness:

- `1403.0079:main.tex:142-153`
```
A result of Herglotz, also known as Bochner's theorem, asserts
that:


\begin{Tm}	
\label{Tm:Oct27yt1}
The function $n \mapsto r(n)$ from $\mathbb Z$ into $\mathbb C^{s \times s}$ is positive definite if and only if there exists a unique positive $\mathbb C^{s \times s}$-valued measure $\mu$ on $[0, 2\pi ]$ such that
\begin{equation}
\label{eq:Oct27nv1}
r(n) = \int_0^{2\pi} e^{i n t} d\mu(t), \quad n \in \mathbb Z.
\end{equation}
\end{Tm}
```

**Conventions fixed by the source.**
- Stated for `C^{s x s}`-valued sequences; the notebook's scalar case is `s = 1`.
- Positive-definiteness of the sequence `r(n)` **is** nonnegativity of every
  Toeplitz block matrix `T_N` — the source spells this out, so this single quote
  covers both the "positive definite sequence" and the "Toeplitz" language.
- Positivity forces `r(-n) = r(n)^*`; the notebook's `nu_{-l} = conj(nu_l)` is
  not an extra assumption but a consequence.
- The measure lives on `[0, 2pi]` with `r(n) = int_0^{2pi} e^{int} dmu(t)`, and
  the representation `r(n) = C^* U^n C` with `U` unitary
  (`1403.0079:main.tex:157-161`) is the spectral-theorem form — useful because it
  is literally "trace of a power of a unitary", the `|mu| = r` case of the
  notebook's `Tr X^l`.
- This paper is about the **quaternionic/indefinite** extension; only its recall
  of the classical complex case is quoted here, which is what we want.

---

## W9. Bochner's theorem (continuous positive definite function on R = Fourier transform of a finite positive measure)

**arXiv:2009.02802** — `2009.02802:main.tex:37-38` `\title{On  positive definite distributions}` / `\author{{\large Saulius  Norvidas} }`.

- `2009.02802:main.tex:54-61`
```
A function $f:\R\to\Co$ is said to be positive definite if
\begin{equation}\label{1.1}
\sum_{j, k=1}^n f(x_j-x_k)c_j{\overline{c}}_k\ge 0
\end{equation}
holds for all finite sets of complex numbers $c_1,\dots, c_n$ and points $x_1,\dots,x_n\in\R$.  A survey about positive definite functions and its generalizations can be found in \cite{9}.    The Bochner theorem states that a continuous function $f$ on $\R$ is positive definite if and only if it is the Fourier transform of a finite nonnegative measure $\mu$ on $\R$, i.e.
\[
f(x)= \hat{\mu}(x)=\int_{-\infty}^{\infty}e^{-ixt}\,d\mu(t),
\]
```

**Conventions fixed by the source.** The convention is
`f(x) = hat mu(x) = int e^{-ixt} dmu(t)` with the **minus** sign in the forward
transform and `check mu(xi) = (1/2pi) int e^{i xi t} dmu(t)` for the inverse;
`mu` is a finite nonnegative measure on `R`. The distributional version
(Bochner–Schwartz: `F in D'(R)` is positive definite iff `hat F` is a
nonnegative tempered measure) is at `2009.02802:main.tex:135` if the
continuous version is not enough.

---

## W10. Bender–Brody–Müller 2017: the PT remark

**arXiv:1608.03679** — `1608.03679:main.tex:17-18` `\title{Hamiltonian for the zeros of the Riemann zeta function}` / `\author{Carl M. Bender$^{1}$, Dorje C. Brody$^{2,3}$, Markus P. M\"uller$^{4,5}$}`.

Abstract (fragment of the single long line 32):

- `1608.03679:main.tex:32` (fragment)
```
While $\hat H$ is not Hermitian in the conventional sense, $\ri{\hat H}$ is ${\cal PT}$ symmetric with a broken $\cPT$ symmetry, thus allowing for the possibility that all eigenvalues of $\hat H$ are real.
```

The claim in the introduction:

- `1608.03679:main.tex:92-99`
```
(iii) Although $\hat H$ is not Hermitian, $\ri{\hat H}$ is $\cPT$ symmetric; 
that is, $\ri{\hat H}$ is invariant under parity-time reflection (in the sense 
to be defined), which means that the eigenvalues of $\ri{\hat H}$ are 
either real or else occur in complex-conjugate pairs. If $\ri{\hat H}$ has {\it 
maximally broken} $\cPT$ symmetry; that is, if all of its eigenvalues are 
{\it pure-imaginary complex-conjugate pairs}, then the eigenvalues of 
${\hat H}$ are real and the Riemann hypothesis follows. 
(iv) While ${\hat H}$ is not Hermitian (symmetric) 
```

And the mechanism — PT symmetry gives *either* a real spectrum *or*
complex-conjugate pairs, which is the dichotomy the notebook's `|mu| = r`
duality plays the role of:

- `1608.03679:main.tex:255-265`
```
\,\ri\longrightarrow-\ri$, we deduce that $\ri{\hat H}$ is invariant under this
modified $\cPT$ reflection. It follows that the eigenvalues of $\ri{\hat H}$ are
either real (if the $\cPT$ symmetry is \textit{unbroken} in the sense that the 
associated eigenstates are also eigenstates of $\cPT$), or else they form 
complex-conjugate pairs (if the $\cPT$ symmetry is \textit{broken} in the sense that 
the associated eigenstates are not eigenstates of $\cPT$). If the $\cPT$ symmetry 
is maximally
broken for $\ri{\hat H}$, then the eigenvalues of ${\hat H}$ would be real, and
the Riemann hypothesis would hold. In our case, since $\cPT\psi_n(x)=\psi_{-n}(x
)$, the $\cPT$ symmetry is indeed broken for all complex values of $z_n$. 
(For the trivial zeros the $\cPT$ symmetry is unbroken.) 
```

**Conventions fixed by the source.** `PT` is here the *modified* reflection
`(x, p) -> (x, -p)` (roles of position and momentum interchanged relative to the
usual convention), so that `i H` is PT symmetric, not `H`. Real spectrum of `H`
requires **maximally broken** PT symmetry of `i H` (all eigenvalues of `i H`
pure-imaginary conjugate pairs) — the opposite of the usual "unbroken PT =>
real spectrum" slogan, and easy to quote backwards. The paper is a proposal, not
a theorem: it assumes self-adjointness it does not prove.

---

## W11. Suzuki 2022: **prior art on the continuous side** — RH as non-negative definiteness of a kernel (screw functions)

**arXiv:2206.03682** — `2206.03682:screwz_15.tex:42-43` `\title[Aspects of the screw function of $\zeta$]%` / `      {Aspects of the screw function corresponding to \\ the Riemann zeta-function} `; author `2206.03682:screwz_15.tex:44-44` `\author[M. Suzuki]{Masatoshi Suzuki}`.

- `2206.03682:screwz_15.tex:58-63`
```
We introduce a screw function corresponding to the Riemann zeta-function 
and study its properties from various aspects. 
Typical results are several equivalent conditions 
for the Riemann hypothesis in terms of the screw function. 
One of them can be considered an analog of so-called Weil's positivity or Li's criterion.
In addition, we prove a few partial but unconditional results for such equivalents. 
```

The screw-function class is defined by a **non-negative definite kernel**
condition — this is literally the Herglotz/Toeplitz condition in its continuous,
kernel form:

- `2206.03682:screwz_15.tex:174-195`
```
consisting of all continuous functions $g(t)$ on $(-2a,2a)$ such that 
$g(-t) = \overline{g(t)}$ (hermitian) 
and the kernel 
%
\begin{equation} \label{Eq_104}
G_g(t,u):=g(t-u)-g(t)-g(-u)+g(0).  
\end{equation}
% 
is non-negative definite on $(-a,a)$, that is,  
%
\begin{equation} \label{Eq_105}
\sum_{i,j=1}^{n} G_g(t_i,t_j) \,  \xi_i \overline{\xi_j} \,\geq\, 0
\end{equation}
%
for all $n \in \N$, $\xi_i \in \C$, and $|t_i| < a$, $(i = 1, 2, . . . , n)$. 
(In literature, a kernel satisfying \eqref{Eq_105} is often referred 
to as a positive definite kernel or semi-positive definite kernel,
but in this paper, we use the term above.) 
%
The members of $\mathcal{G}_a$ are called {\it screw functions} 
because of their relationship with screw arcs in Hilbert spaces 
(\cite[\S12]{KrLa14}). 
```

and the source itself names the Nevanlinna / Pick / **Herglotz** class as the
associated function class:

- `2206.03682:screwz_15.tex:197-203`
```
Let $\mathcal{N}$ be the Nevanlinna class
that consists of analytic functions in the upper half-plane $\C_+=\{z\,|\, \Im(z)>0\}$ 
mapping $\C_+$ into $\C_+ \cup \R$. 
(Note that $\mathcal{N}$ is also called the class of Pick functions, 
or R functions, 
or Herglotz functions 
depending on the literature.)   
```

Weil's criterion, stated in the convolution-square form
`W(psi * tilde psi) >= 0` with `tilde psi(x) = conj(psi(-x))` — the cleanest
quotable version of "the Weil distribution is of positive type":

- `2206.03682:screwz_15.tex:1035-1055`
```
The linear functional $W:C_c^\infty(\R)\to\C$ 
defined by 
%
\begin{equation} \label{Eq_303}
\psi~\mapsto~W(\phi):=\sum_{\gamma} \widehat{\psi}(\gamma) 
\end{equation}
%
is called the Weil distribution. A. Weil~\cite{We52} (see also \cite{Yo92}) 
showed that the RH is true if and only if 
the distribution $W$ is non-negative definite, that is,  
%
\begin{equation} \label{Eq_304}
W(\psi \ast \widetilde{\psi}) \geq  0 \quad \text{for every}~\psi \in C_c^\infty(\R),
\end{equation}
%
where 
%
\begin{equation} \label{Eq_305}
(\psi_1\ast\psi_2)(x):=\int_{-\infty}^{\infty} \psi_1(y)\psi_2(x-y) \, dy, \qquad 
\widetilde{\psi}(x) := \overline{\psi(-x)}. 
\end{equation}
```

And the main theorem: RH iff the associated Hermitian form is non-negative
definite:

- `2206.03682:screwz_15.tex:322-334`
```
\begin{theorem}  \label{Thm_1_3}
The RH is true if and only if the hermitian form
$\langle \cdot,\cdot \rangle_{G_g,a}$ 
is non-negative definite on $\mathfrak{C}_0(a)$, 
that is, $\langle \phi,\phi \rangle_{G_g,a} \geq  0$ 
for all $\phi \in \mathfrak{C}_0(a)$ for every $0<a<\infty$. 
Moreover, assuming that the RH is true, 
$\langle \cdot,\cdot \rangle_{G_g,a}$ 
is positive definite on $L^2(-a,a)$, 
that is, 
$\langle \phi,\phi \rangle_{G_g,a}>0$ 
for all non-zero $\phi \in L^2(-a,a)$ for every $0<a<\infty$. 
\end{theorem}
```

**Conventions fixed by the source, and how far the overlap goes.**
- `g` is the screw function attached to zeta; the kernel is
  `G_g(t,u) = g(t-u) - g(t) - g(-u) + g(0)`, i.e. the *second difference* of `g`,
  not `g` itself. Suzuki's "non-negative definite" is other authors' "positive
  semidefinite kernel"; he says so explicitly (`2206.03682:screwz_15.tex:189-191`).
- The `\widehat\psi(\gamma)` in the Weil distribution runs over the imaginary
  parts `gamma` of the nontrivial zeros; the reduction to `C_c^\infty` test
  functions is attributed to Yoshida, not to Weil
  (`2206.03682:screwz_15.tex:1057-1061`).
- Li's criterion is derived in this framework as a **special case of Weil
  positivity**, obtained by testing against triangular functions
  (`2206.03682:screwz_15.tex:1114-1125`).
- **What this does and does not pre-empt.** Suzuki has, for zeta: a
  positive-definiteness criterion (kernel form), the Kreĭn–Langer/Herglotz
  representation behind it, and Li's criterion as a specialisation. He does
  **not** state it for an arbitrary finite-dimensional transfer operator, does
  **not** use the Toeplitz-sequence (Herglotz, discrete) form, and does **not**
  mention graphs or the Ramanujan property. The notebook's contribution has to
  be located against this section and against W6.

---

## What was NOT found

1. **No arXiv TeX source states the Herglotz theorem in the exact form
   "a sequence is positive definite iff it is the moment sequence of a positive
   measure on the circle" as a standalone lemma in a lecture-note.** W8 above is
   the best available: a research paper whose introduction recalls the classical
   matrix-valued theorem with proof references (`1403.0079:main.tex:154-155`, to three sources
   whose keys the tarball's bibliography does not resolve). It is quotable and byte-checkable, which is what the
   convention requires, but it is not a textbook.
2. **Bochner likewise.** W9 is a research paper on positive definite
   distributions whose first paragraph states Bochner's theorem. Adequate, not
   canonical. If the lab book prefers, both W8 and W9 can be demoted to
   *assumptions* (`stipulated`) with these quotes as supporting references;
   the canonical citations, neither on arXiv and therefore **not quoted here**,
   are: G. Herglotz, *Über Potenzreihen mit positivem, reellem Teil im
   Einheitskreis*, Ber. Verh. Sächs. Akad. Wiss. Leipzig 63 (1911) 501–511;
   S. Bochner, *Vorlesungen über Fouriersche Integrale*, Akad. Verlagsges. 1932;
   W. Rudin, *Fourier Analysis on Groups*, Interscience 1962, §1.4.3.
3. **Horton–Stark–Terras, "What are zeta functions of graphs and what are they
   good for?" is not on arXiv** (Contemporary Mathematics 415 (2006) 173–190).
   An arXiv API query `au:Terras_A AND cat:math.NT` returns no entries. Same for
   Stark–Terras, "Zeta functions of finite graphs and coverings" (Adv. Math. 121
   (1996) 124–165; 154 (2000) 132–195): journal only. They are therefore named,
   not quoted. A. Terras, *Zeta Functions of Graphs: A Stroll through the
   Garden*, CUP 2010, is the book reference for the graph explicit formula.
4. **No paper was found that states a Herglotz/Toeplitz positive-definiteness
   criterion for the Ramanujan property.** arXiv API full-text queries for
   `all:"Ramanujan graph" AND all:"positive definite"` returned 0 entries, and
   `all:"Ihara zeta" AND all:"positive definite"` returned exactly one, unrelated
   (arXiv:1908.06563, "Energized simplicial complexes"). Huang (W6) is the
   nearest hit and proves the *termwise* version; see the discussion under W6
   for exactly where the overlap stops. On the **continuous/zeta** side the
   corresponding statement *does* exist — Suzuki, W11 — so the honest position
   is: the mechanism is known for zeta, and the graph/transfer-operator
   transcription is what is new.
5. **No paper was found stating the criterion for an arbitrary transfer
   operator / Kraus channel** (the notebook's actual theorem). The closest
   ingredients are W6 (regular graphs) and W7 (quantum expanders, a bound but
   not a criterion).
6. **Bombieri–Lagarias, "Complements to Li's criterion for the Riemann
   hypothesis", J. Number Theory 77 (1999) 274–287, is not on arXiv.** It is
   cited as `\cite{BL}` / `\cite{BL99}` by W3 and W4; the quotes at
   `math/0404394:main.tex:400-404` and `math/0506326:main.tex:115-118` record
   what those papers attribute to it. Voros' earlier note `math/0404213`
   ("A sharpening of Li's criterion...") was **not** fetched; `math/0506326` is
   its uncompressed successor and says so (`math/0506326:main.tex:65-66`).
7. `math-ph/0404030` — the identifier guessed for Voros in the task brief —
   serves an unrelated paper on `k`-decomposability of positive maps. It was
   fetched, identified as wrong, deleted from `refs/src/`, and removed from the
   `IDS` list.

---

## Verification

Every locus above was byte-checked: the file is read with
`open(..., encoding="utf-8", errors="replace")` (the same decoding
`scripts/labbook_check.py` uses), the stated lines are joined with newlines,
both window and quote are whitespace-normalised, and the quote must be a
substring of the window — i.e. whole and contiguous. Output:

```
63 quotes, 63 verified, 0 failed
```

The per-quote log (one line per locus, all `OK`) is reproducible with:

```
python3 - <<'EOF'
import re
ROOT = "."
for tag, i, f, ln, quote in ROWS:          # (id, file, "a-b", quote) as in the TSV below
    a, _, b = ln.partition("-"); a = int(a); b = int(b or a)
    L = open(f"{ROOT}/refs/src/{i}/{f}", encoding="utf-8", errors="replace").read().split("\n")
    win = " ".join("\n".join(L[a-1:b]).split())
    print("OK " if " ".join(quote.split()) in win else "FAIL", i, f, ln)
EOF
```

---

## Proposed rows for `db/provenance.tsv`

(Not written to `db/`; paste as-is. Columns: `id | key | file | lines | quote | used_by`.)

```tsv
prov:connes98-tf-implies-pos	math/9811068	main.tex	2514-2516	What we shall show however is that the trace formula (16) implies the positivity of the Weil distribution, and hence the validity of RH for $k$. Remember that we are still in	W1
prov:connes98-thm5	math/9811068	main.tex	2523-2540	\noindent {\bf Theorem 5.} {\it Let $k$ be a global field of positive characteritic and $Q_{\L}$ be the orthogonal projection on the subspace of $L^2(X)$ spanned by the $f \in \Sc(A)$ such that $f(x)$ and $\wh f(x)$ vanish for $\vert x \vert > \L$ . Let $h \in \Sc (C_k)$ have compact support. Then the following conditions are equivalent, \smallskip a) When $\L \ra \ify$, one has $$ {\rm Trace} \, (Q_{\L} \, U(h)) = 2h (1) \log' \L + \sum_{v } \int'_{k^*_v} {h(u^{-1}) \over \vert 1-u \vert} \, d^* u + o(1) $$ } \smallskip {\it b) All $L$ functions with Gr\"ossencharakter on $k$ satisfy the Riemann Hypothesis.}	W1
prov:connes98-positive-type	math/9811068	main.tex	2591-2601	and for any $ \L$ the following distribution on $C_k$ is of positive type, $$ \D_{ \L}(f) = \, {\rm Trace} \, (( S_{ \L}- \, Q'_{ \L,0}) \, V(f)) , \leqno (24) $$ i.e. one has, $$ \D_{ \L}(f * f^*) \geq \, 0 , \leqno (25) $$ where $ f^*(g)= \, \ov f(g^{-1})$ for all $g \in C_k$.	W1
prov:connes98-explicit	math/9811068	main.tex	4793-4798	Let $h \in \Sc (C_k)$ have compact support, then $$ \wh h (0) + \wh h (1) - \sum_{L(\Xc , \rho) = 0 \atop 0 < {\rm Re} \rho < 1} \wh h (\Xc , \rho) = \sum_v \int'_{k_v^*} {h(u^{-1}) \over \vert 1-u \vert} \, d^* u $$	W1
prov:cc20-explicit	2006.13771	weil-compo.tex	99-103	It was shown by A. Weil \cite{Weil} that the Riemann Hypothesis (RH) is equivalent to the negativity of the right-hand side of the Riemann-Weil explicit formula \cite{EB} (Appendix~\ref{appendix2}: \eqref{bombieriexplicit}) \begin{equation}\label{explicit form} \tilde f(0)-\sum_{\rho\in Z}\tilde f(\rho)+\tilde f(1)=\sum_v {\mathcal W}_v(f), \qquad \tilde f(s):=\int_0^\infty f(x)x^{s-1}dx \end{equation} where $Z$ is the multi-set of non-trivial zeros of the Riemann zeta function and for a precise class of complex-valued test functions on the positive half-line, of the form	W2
prov:cc20-weilcrit	2006.13771	weil-compo.tex	107-110	In fact, following \cite{yoshida}, it is enough to prove the negativity of the right-hand side of \eqref{explicit form} for functions $g$ with compact support in the (locally compact) multiplicative group $\R_+^*=(0,\infty)$. Furthermore, given any finite set of complex numbers $F\supset \{0,1\}$, $F\cap Z=\emptyset$, using the notation $g^\sharp(x):=x^{-1}g(x^{-1}), \ \bar g(x)=\overline{g(x)}$, one has (Appendix \ref{apppositivity}, Proposition~\ref{mainprop}) \begin{equation}\label{weilnegav} RH \iff \sum_v {\mathcal W}_v(g*\bar g^\sharp)\leq 0, \quad \forall g\in C_c^\infty(\R_+^*)\mid \tilde g(z)=0,\ \forall z\in F. \end{equation}	W2
prov:cc20-mainprop	2006.13771	weil-compo.tex	2075-2079	\begin{prop}\label{mainprop} Let $Z\subset \C$ be the set of non-trivial zeros of the Riemann zeta function and $F \subset \C$ a finite set disjoint from $Z$ and containing $\{0,1\}$, then \begin{equation}\label{appendweilnegav} RH \iff \sum_v {\mathcal W}_v(g*\bar g^\sharp)\leq 0, \quad \forall g\in C_c^\infty(\R_+^*)\mid \tilde g(z)=0,\ \forall z\in F. \end{equation} \end{prop}	W2
prov:cc20-bombieri	2006.13771	weil-compo.tex	2038-2041	Then, with $f^\sharp(x):=x^{-1}f(x^{-1})$ the explicit formula takes the form \begin{equation}\label{bombieriexplicit} \sum_{\rho}\tilde f(\rho)=\int_0^\infty f(x)dx+\int_0^\infty f^\sharp(x)dx-\sum_v {\mathcal W}_v(f), \end{equation}	W2
prov:lagarias05-li	math/0404394	main.tex	156-171	\noindent Xian-Jin Li gave a criterion for the Riemann hypothesis in terms of the positivity of the set of coefficients $\lambda_n = \sum_{\rho} 1 - \left( 1 - \frac{1}{\rho}\right)^n$, $(n= 1, 2, ...)$, in which $\rho$ runs over the nontrivial zeros of the Riemann zeta function. We define similar coefficients $\lambda_n(\pi)$ associated to principal automorphic $L$-functions $L(s, \pi)$ over $GL(N)$. We relate these cofficients to values of Weil's quadratic functional associated to the representation $\pi$ on a suitable set of test functions. The positivity of the real parts of these coefficients is a necessary and sufficient condition for the Riemann hypothesis for $L(s, \pi)$ to hold.	W3
prov:lagarias05-licrit-head	math/0404394	main.tex	1098-1102	\begin{theorem}~\label{Nth22} Let $\pi$ be an irreducible cuspidal unitary automorphic representation of $GL(n)$. The following conditions are each equivalent to the Riemann hypothesis for $\xi(s, \pi)$.	W3
prov:lagarias05-licrit-pos	math/0404394	main.tex	1108-1111	(1) For all $n \ge 1$, \beql{N217a} \Re \left( \lambda_n(\pi) \right) \ge 0. \eeq	W3
prov:lagarias05-weil-scalar-product	math/0404394	main.tex	1243-1250	Given $F(s), G(s) \in \sA$ we define the {\em Weil scalar product} associated to the automorphic representation $\pi$ by \beql{301} \langle F, G \rangle_{\sW(\pi)} := \sum_{ \rho \in Z(\pi) } F(\rho) \overline{G( 1 - \bar{\rho})}. \eeq The sum on the right counts zeros with	W3
prov:lagarias05-rh-implies-psd	math/0404394	main.tex	1268-1281	The Riemann hypothesis for $\Lambda(s, \pi)$ implies that the Weil scalar product is positive semidefinite on the test function vector space $\sA$. To see this we note that $\rho= 1 - \bar{\rho}$ holds if and only if $\rho$ lies on the critical line $\Re(s) = \frac{1}{2}.$ The Riemann hypothesis implies that for all $F(s) \in \sA$, $$ \langle F, F \rangle_{\sW(\pi)} = \sum_{ \rho \in Z(\pi) } F(\rho) \overline{F(1 - \bar{\rho})} = \sum_{ \rho \in Z(\pi) } F(\rho) \overline{F(\rho)} = \sum_{ \rho \in Z(\pi) } |F(\rho)|^2 \ge 0. $$	W3
prov:lagarias05-li-is-weil	math/0404394	main.tex	1334-1345	\begin{theorem}~\label{th31} Let $\pi$ be an irreducible cuspidal unitary automorphic representation of $GL(N)$, with associated $\xi$-function $\xi(s, \pi)$ and with Weil scalar product $\langle \cdot, \cdot \rangle_{\sW(\pi)}$. For the Li test functions $G_n(s) = 1 - (1 - \frac{1}{s})^n$ there holds \beql{304} \langle G_n, G_m \rangle_{\sW(\pi)} = \lambda_n(\pi) + \lambda_{-m}(\pi) - \lambda_{n-m}(\pi). \eeq	W3
prov:lagarias05-encodes	math/0404394	main.tex	333-337	The third observation was that each positivity condition $\lambda_n \ge 0$ encodes ``Weil positivity'' of Weil's quadratic functional for a particular test function $g_n(x)$.	W3
prov:voros06-li-criterion	math/0506326	main.tex	46-48	\emph{Li's criterion} for the Riemann Hypothesis (RH) states that the latter is true if and only if a specific real sequence $\{ \lambda_n \}_{n=1,2,\ldots}$ has \emph{all its terms positive} \cite{LI1,BL}.	W4
prov:voros06-lambda-def	math/0506326	main.tex	74-78	(in the notations of Li, whose $\lambda_n$ are $n$ times Keiper's) \begin{equation} \label{LDef} \lambda_n = \sum_\rho \, [1-(1-1/\rho)^n] \qquad (n=1,2, \ldots), \end{equation}	W4
prov:coffey05-li-criterion	math-ph/0505052	lambda2.txt	114-118	The sequence $\{\lambda_n\}_{n=1}^\infty$ is defined by $$\lambda_n = {1 \over {(n-1)!}}{d^n \over {ds^n}}[s^{n-1}\ln \xi(s)]_{s=1}. \eqno(1)$$ Then Li's criterion for the Riemann hypothesis to hold is that all $\{\lambda_n\}_{n=1}^\infty$ are nonnegative \cite{li}. We note that Li's	W5
prov:huang19-li-criterion	1905.13485	revision_graph_Licriterion.tex	189-189	Li's criterion states that the Riemann hypothesis holds if and only if $\lambda_k\geq 0$ for all $k\geq 1$ \cite{Li:1997}.	W6
prov:huang19-geodesic-cycles	1905.13485	revision_graph_Licriterion.tex	205-212	A cycle is said to be {\it geodesic} if all shifted cycles are backtrackless. For all $k\geq 1$ let $N_k$ denote the number of geodesic cycles on $X$ of length $k$. The {\it Ihara zeta function} $Z(u)$ of $X$ is the analytic continuation of \begin{gather}\label{zeta} \exp \left(\sum_{k=1}^\infty \frac{N_k}{k} u^k \right). \end{gather}	W6
prov:huang19-ramanujan-rh	1905.13485	revision_graph_Licriterion.tex	217-222	For the rest of this paper, we always assume that $X$ is a connected $(q+1)$-regular undirected graph of finite order $n$ with $q\geq 1$ and $n\geq 3$. In this case, the eigenvalues of $X$ with absolute value $q+1$ are called {\it trivial} eigenvalues and the poles of $Z(u)$ with values $\pm 1$ and $\pm q^{-1}$ are called {\it trivial} poles. The graph $X$ is said to be {\it Ramanujan} whenever $$ |\lambda|\leq 2q^{\frac{1}{2}} $$ for all nontrivial eigenvalues $\lambda$ of $X$ \cite{Ramanujan1988}. The graph $X$ is Ramanujan if and only if all nontrivial poles of $Z(u)$ have the same absolute value $q^{-\frac{1}{2}}$, which is similar to the Riemann hypothesis by writing $u=q^{-s}$ \cite{Winnie2019,Terras2010}. We define the function $\Xi(u)$ by	W6
prov:huang19-hk-def	1905.13485	revision_graph_Licriterion.tex	251-257	\begin{defn}\label{defn:hk} Let $\{h_k\}_{k=1}^\infty$ denote the number sequence given by \begin{gather*} \frac{d}{du}\ln \Xi(q^{-\frac{1}{2}} u) =\sum_{k=0}^\infty h_{k+1} u^k. \end{gather*} \end{defn}	W6
prov:huang19-ramanujan-iff-positive	1905.13485	revision_graph_Licriterion.tex	287-296	\begin{thm}\label{thm:Li} The following are equivalent: \begin{enumerate} \item $X$ is Ramanujan. \item $h_k\geq 0$ for all $k\geq 1$. \item $h_k\geq 0$ for infinitely many even $k\geq 2$. \end{enumerate} \end{thm}	W6
prov:huang19-hk-cycle-formula	1905.13485	revision_graph_Licriterion.tex	440-469	\begin{prop}\label{prop:formula1} \begin{enumerate} \item If $X$ is nonbipartite then \begin{gather*} h_k = \left\{ \begin{array}{ll} 2(n-1) + q^{\frac{k}{2}} +q^{-\frac{k}{2}} -q^{-\frac{k}{2}} N_k \qquad &\hbox{for all odd $k$}, \\ 2(n-1) + q^{\frac{k}{2}} +q^{-\frac{k}{2}} - q^{-\frac{k}{2}} \left( N_k-n(q-1) \right) \qquad &\hbox{for all even $k$}. \end{array} \right. \end{gather*}	W6
prov:hastings07-lambdaH	0706.0556	sd10.tex	118-131	Let $\lambda_2$ be the eigenvalue with the second largest absolute value of all eigenvalues other than $\lambda_1$. Let \be \lambda_{H}=\frac{2\sqrt{D-1}}{D}. \ee The main result of this paper is that, in the Hermitian case, for any $\epsilon>0$ the probability that $|\lambda_2|$ is within $\epsilon$ of $\lambda_{H}$ approaches unity as $N\rightarrow \infty$. Interestingly, this is the same as the recently proven tight bound\cite{fried} in the classical case, but the proof in the quantum case is much simpler.	W7
prov:acks14-herglotz-abstract	1403.0079	main.tex	103-107	A classical theorem of Herglotz states that a function $n\mapsto r(n)$ from $\mathbb Z$ into $\mathbb C^{s\times s}$ is positive definite if and only there exists a $\mathbb C^{s\times s}$-valued positive measure $\mu$ on $[0,2\pi]$ such that $r(n)=\int_0^{2\pi}e^{int}d\mu(t)$for $n\in \mathbb Z$.	W8
prov:acks14-toeplitz	1403.0079	main.tex	122-138	pertaining to the complex numbers setting. A function $n\mapsto r(n)$ from $\mathbb Z$ into $\mathbb C^{s\times s}$ is called positive definite if the associated function (also called kernel) $K(n-m)$ is positive definite on $\mathbb Z$. This means that for every choice of $N\in\mathbb N$ and $n_1,\ldots, n_N\in\mathbb Z$, the $N\times N$ block matrix with $(j,\ell)$ block entry equal to the matrix $r(n_j-n_\ell)$ is non-negative, that is, all the block Toeplitz matrices \begin{equation} \label{eq:toeplitz} \mathbb T_N\stackrel{\rm def.}{=}\begin{pmatrix}r(0)&r(1)&\cdots &r(N)\\ r(-1)&r(0)&\cdots &r(N-1)\\ & & &\\ & & &\\ r(-N)&r(1-N)&\cdots& r(0)\end{pmatrix} \end{equation} are non-negative. We will use the notation $\mathbb T_N \succeq 0$.	W8
prov:acks14-herglotz	1403.0079	main.tex	142-153	A result of Herglotz, also known as Bochner's theorem, asserts that: \begin{Tm} \label{Tm:Oct27yt1} The function $n \mapsto r(n)$ from $\mathbb Z$ into $\mathbb C^{s \times s}$ is positive definite if and only if there exists a unique positive $\mathbb C^{s \times s}$-valued measure $\mu$ on $[0, 2\pi ]$ such that \begin{equation} \label{eq:Oct27nv1} r(n) = \int_0^{2\pi} e^{i n t} d\mu(t), \quad n \in \mathbb Z. \end{equation} \end{Tm}	W8
prov:norvidas20-bochner	2009.02802	main.tex	54-61	A function $f:\R\to\Co$ is said to be positive definite if \begin{equation}\label{1.1} \sum_{j, k=1}^n f(x_j-x_k)c_j{\overline{c}}_k\ge 0 \end{equation} holds for all finite sets of complex numbers $c_1,\dots, c_n$ and points $x_1,\dots,x_n\in\R$. A survey about positive definite functions and its generalizations can be found in \cite{9}. The Bochner theorem states that a continuous function $f$ on $\R$ is positive definite if and only if it is the Fourier transform of a finite nonnegative measure $\mu$ on $\R$, i.e. \[ f(x)= \hat{\mu}(x)=\int_{-\infty}^{\infty}e^{-ixt}\,d\mu(t), \]	W9
prov:bbm17-pt-abstract	1608.03679	main.tex	32-32	While $\hat H$ is not Hermitian in the conventional sense, $\ri{\hat H}$ is ${\cal PT}$ symmetric with a broken $\cPT$ symmetry, thus allowing for the possibility that all eigenvalues of $\hat H$ are real.	W10
prov:bbm17-pt-real	1608.03679	main.tex	92-99	(iii) Although $\hat H$ is not Hermitian, $\ri{\hat H}$ is $\cPT$ symmetric; that is, $\ri{\hat H}$ is invariant under parity-time reflection (in the sense to be defined), which means that the eigenvalues of $\ri{\hat H}$ are either real or else occur in complex-conjugate pairs. If $\ri{\hat H}$ has {\it maximally broken} $\cPT$ symmetry; that is, if all of its eigenvalues are {\it pure-imaginary complex-conjugate pairs}, then the eigenvalues of ${\hat H}$ are real and the Riemann hypothesis follows. (iv) While ${\hat H}$ is not Hermitian (symmetric)	W10
prov:bbm17-pt-broken	1608.03679	main.tex	255-265	\,\ri\longrightarrow-\ri$, we deduce that $\ri{\hat H}$ is invariant under this modified $\cPT$ reflection. It follows that the eigenvalues of $\ri{\hat H}$ are either real (if the $\cPT$ symmetry is \textit{unbroken} in the sense that the associated eigenstates are also eigenstates of $\cPT$), or else they form complex-conjugate pairs (if the $\cPT$ symmetry is \textit{broken} in the sense that the associated eigenstates are not eigenstates of $\cPT$). If the $\cPT$ symmetry is maximally broken for $\ri{\hat H}$, then the eigenvalues of ${\hat H}$ would be real, and the Riemann hypothesis would hold. In our case, since $\cPT\psi_n(x)=\psi_{-n}(x )$, the $\cPT$ symmetry is indeed broken for all complex values of $z_n$. (For the trivial zeros the $\cPT$ symmetry is unbroken.)	W10
prov:suzuki22-screw-kernel	2206.03682	screwz_15.tex	174-195	consisting of all continuous functions $g(t)$ on $(-2a,2a)$ such that $g(-t) = \overline{g(t)}$ (hermitian) and the kernel % \begin{equation} \label{Eq_104} G_g(t,u):=g(t-u)-g(t)-g(-u)+g(0). \end{equation} % is non-negative definite on $(-a,a)$, that is, % \begin{equation} \label{Eq_105} \sum_{i,j=1}^{n} G_g(t_i,t_j) \, \xi_i \overline{\xi_j} \,\geq\, 0 \end{equation} % for all $n \in \N$, $\xi_i \in \C$, and $|t_i| < a$, $(i = 1, 2, . . . , n)$. (In literature, a kernel satisfying \eqref{Eq_105} is often referred to as a positive definite kernel or semi-positive definite kernel, but in this paper, we use the term above.) % The members of $\mathcal{G}_a$ are called {\it screw functions} because of their relationship with screw arcs in Hilbert spaces (\cite[\S12]{KrLa14}).	W11
prov:suzuki22-herglotz-class	2206.03682	screwz_15.tex	197-203	Let $\mathcal{N}$ be the Nevanlinna class that consists of analytic functions in the upper half-plane $\C_+=\{z\,|\, \Im(z)>0\}$ mapping $\C_+$ into $\C_+ \cup \R$. (Note that $\mathcal{N}$ is also called the class of Pick functions, or R functions, or Herglotz functions depending on the literature.)	W11
prov:suzuki22-weil-positivity	2206.03682	screwz_15.tex	1035-1055	The linear functional $W:C_c^\infty(\R)\to\C$ defined by % \begin{equation} \label{Eq_303} \psi~\mapsto~W(\phi):=\sum_{\gamma} \widehat{\psi}(\gamma) \end{equation} % is called the Weil distribution. A. Weil~\cite{We52} (see also \cite{Yo92}) showed that the RH is true if and only if the distribution $W$ is non-negative definite, that is, % \begin{equation} \label{Eq_304} W(\psi \ast \widetilde{\psi}) \geq 0 \quad \text{for every}~\psi \in C_c^\infty(\R), \end{equation} % where % \begin{equation} \label{Eq_305} (\psi_1\ast\psi_2)(x):=\int_{-\infty}^{\infty} \psi_1(y)\psi_2(x-y) \, dy, \qquad \widetilde{\psi}(x) := \overline{\psi(-x)}. \end{equation}	W11
prov:suzuki22-rh-iff-nnd	2206.03682	screwz_15.tex	322-334	\begin{theorem} \label{Thm_1_3} The RH is true if and only if the hermitian form $\langle \cdot,\cdot \rangle_{G_g,a}$ is non-negative definite on $\mathfrak{C}_0(a)$, that is, $\langle \phi,\phi \rangle_{G_g,a} \geq 0$ for all $\phi \in \mathfrak{C}_0(a)$ for every $0<a<\infty$. Moreover, assuming that the RH is true, $\langle \cdot,\cdot \rangle_{G_g,a}$ is positive definite on $L^2(-a,a)$, that is, $\langle \phi,\phi \rangle_{G_g,a}>0$ for all non-zero $\phi \in L^2(-a,a)$ for every $0<a<\infty$. \end{theorem}	W11
```
