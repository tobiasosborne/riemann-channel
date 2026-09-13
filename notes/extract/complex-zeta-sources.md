# Sources for an Ihara-type zeta of simplicial complexes (Bass/Hashimoto + RH ⇔ Ramanujan)

Written 2026-09-13 by the source-acquisition worker. Same discipline as
`notes/extract/selberg-sources.md`: every quote below was copied out of the arXiv **TeX
source** in `refs/src/<id>/` (fetched by `refs/fetch_sources.sh`, hashes in
`refs/manifest.sha256`) and is cited as `<id>:<file>:<line-range>`; each quote is whole and
contiguous in the lines stated, so it can be re-checked with `sed -n '<a>,<b>p'`.
Preference throughout: TeX source, never PDF.

New ids appended to `refs/fetch_sources.sh` for this note:
`0804.2305 0809.1401 0809.1401v1 1505.00902 math/0407509 1303.6848 1303.6847 1412.3327
1109.3854 math/0608761 1702.05452 1804.08028 math/0406208 math/0406217 1712.02526
1701.00154 1605.02664 2607.21262 2411.15489 2512.23276 2405.14395 1606.07317 2303.11226
2204.13586 2002.12099 2510.27134`
(plus the second worker's list, see the script).

**Short answer to the grounding question.** Yes for **quotients of affine buildings**, and
only there. The Ihara zeta generalises to finite quotients of the Bruhat–Tits building of
PGL₃ (C1), PGSp₄ (C4), and — since 2026 — every PGLₙ (C2), always in the shape
`(1 − u^n)^{χ} / (vertex-Hecke determinant)` = an alternating product of
`det(I ∓ L u^j)` factors over the facet dimensions; and RH for it is literally
"the nontrivial zeros of each determinant factor sit on prescribed circles `|u| = q^{-c}`",
equivalent to the complex being Ramanujan. The higher-dimensional Hashimoto operator
exists and is the **geodesic-flow branching operator** of Lubetzky–Lubotzky–Parzanchevski
(C5), with Ramanujan complex ⇒ Ramanujan digraph ⇒ RH for *every* group `G`; the converse
is Kamber's (C7a). For a **general finite simplicial or cell complex** there is *no*
Ihara-type zeta with a Bass identity and a Ramanujan theorem; what exists instead is
(i) the hypergraph zeta, which provably collapses to the Ihara zeta of the incidence
bipartite graph (C6), and (ii) a combinatorial Ruelle zeta on an arbitrary triangulated
manifold with a Fried-type theorem but no Ramanujan/RH statement (C8).

---

## C1. Kang–Li and Kang–Li–Wang: the PGL(3) complex zeta (the prototype)

### C1a. Kang–Li, "Zeta Functions of Complexes Arising from PGL(3)" (Adv. Math. 2014)

**arXiv:0804.2305** — title `0804.2305:main.tex:53`
`\title[Zeta Functions of Complexes Arising from $\PGL(3)$]{Zeta Functions of Complexes Arising from $\PGL(3)$}`;
authors `0804.2305:main.tex:54` `\author{Ming-Hsuan Kang and Wen-Ching Winnie Li}`.

**Ihara's theorem, as this paper states it** (the baseline for all exponents below):

- `0804.2305:main.tex:97-104`
```
\begin{theorem}[Ihara \cite{Ih}]
Suppose $X = (V, E)$ with vertex set $V$ and edge set $E$ is
$(q+1)$-regular. Then its zeta function
 is a rational function of the form
$$ Z(X,u) = \frac{(1 - u^2)^{\chi(X)}}{\det(I - Au + qu^2I)},$$
where $\chi(X) = \#(V) - \#(E)$ is the Euler characteristic of $X$
and $A$ is the adjacency matrix of $X$.
\end{theorem}
```

**The zeta of the complex, by closed geodesics of one type:**

- `0804.2305:main.tex:215-220`
```
The zeta function of $X_\G$ is defined as
$$ Z(X_\G,u) = \prod_{[C]} (1 - u^{l_A([C])})^{-1},$$
\noindent where $[C]$ runs through the equivalence classes of
 tailless primitive closed geodesics consisting of edges of the same type,
 and $l_A([C])$ is the algebraic
length of any geodesic in $[C]$.
```

**Main Theorem (the determinant identity), with the two hypotheses on Γ:**

- `0804.2305:main.tex:225-243`
```
{\bf Main Theorem.} {\it Let $\Gamma$ be a discrete cocompact
torsion-free
 subgroup of $G$ such that

(I) $\ord_{\pi} \det \G \subseteq 3\mathbb Z$,  and

(II) $\G$ is regular, namely, the {centralizer} of any non-identity
element of $\G$ in $G$ is a torus.

\noindent Then the zeta function of the $(q+1)$-regular finite
complex $X_\G = \Gamma \backslash \B$ is a rational function
\begin{eqnarray}\label{zeta}
Z(X_\G, u) = \frac{(1-u^3)^{\chi(X_\G)}}{\det(I-A_1u+qA_2u^2-q^3
u^3I)\det(I + L_Bu)},
\end{eqnarray}
in which $\chi(X_\G)$ is the Euler characteristic of $X_\G$, and $L_B$ is the Iwahori-Hecke
operator given by the $B$-double coset $Bt_2\sigma^2 B$, where
$t_2= \left( \begin{smallmatrix}  &  & \pi^{-1} \\
 &1 &  \\\pi & & \end{smallmatrix}\right)$.}
```

**Hashimoto (edge) form and the operator identity:**

- `0804.2305:main.tex:245-250`
```
Similar to the graph zeta function, our complex zeta function can be
expressed as
$$ Z(X_\G, u) = \frac{1}{\det(I - L_E u) \det(I - (L_E)^t u^2)} =
\frac{1}{\det(I - L_E u) \det(I - L_E u^2)},$$ where $L_E$ is the
operator given by the double coset $E(t_2 \sigma^2)^2E$, which is also the
adjacency matrix of type $1$ edges in $X_\G$.
```

- `0804.2305:main.tex:257-260`
```
\begin{eqnarray}\label{zetaidentity}
\frac{(1-u^3)^{\chi(X_\G)}}{\det(I-A_1u+qA_2u^2-q^3 u^3I)} =
\frac{\det(I + L_Bu)}{\det(I - L_E u) \det(I - (L_E)^t u^2)},
\end{eqnarray}
```
with the rank-one comparison printed immediately after,
`0804.2305:main.tex:264-265` — `$$\frac{(1 - u^2)^{\chi(X)}}{\det(I - Au + qu^2I)} = \frac{1}{\det(I` / `- A_eu)}.$$`

**Placement, spelled out** (from the displayed equations above):
`(1−u³)^{χ}` is in the **numerator**; the vertex-Hecke determinant
`det(I − A₁u + qA₂u² − q³u³I)` and the directed-chamber determinant `det(I + L_B u)` are
both in the **denominator**; the edge determinants `det(I − L_E u)` and
`det(I − (L_E)ᵗ u²)` are in the denominator of the Hashimoto form. Note the **plus** sign
in `det(I + L_B u)` and the `u²` in the transposed edge factor.

**RH ⇔ Ramanujan, with the exact absolute values:**

- `0804.2305:main.tex:272-279`
```
$Z(X_\G, u)$ clearly has properties (1) and (2). Now we discuss its
connection with the Riemann hypothesis. The trivial zeros of
$\det(I-A_1u+qA_2u^2-q^3 u^3I)$ arise from the trivial eigenvalues
of $A_1$ and $A_2$ on $X_\G$; they are $1, q^{-1}, q^{-2}$ and their
multiples by cubic roots of unity. An equivalent statement for
$X_\G$ being Ramanujan is that the nontrivial zeros of
$\det(I-A_1u+qA_2u^2-q^3 u^3I)$ all have absolute value $q^{-1}$
(cf.\cite{Li}), which is the Riemann hypothesis for $Z(X_\G, u)$.
```

- `0804.2305:main.tex:285-295`
```
\begin{theorem}[\cite{KLW}, Theorem 2] The following four statements on $X_\G$ are equivalent.
\begin{enumerate}
\item[(1)] $X_\G$ is a Ramanujan complex;

\item[(2)] The nontrivial zeros of $\det(I-A_1u+qA_2u^2-q^3 u^3I)$ have absolute value $q^{-1}$;

\item[(3)] The nontrivial zeros of $\det(I + L_Bu)$ have absolute values $1$, $q^{-1/2}$ and $q^{-1/4}$; and

\item[(4)] The nontrivial zeros of $\det(I - L_E u)$ have absolute values $q^{-1}$ and $q^{-1/2}$.
\end{enumerate}
\end{theorem}
```

**Ramanujan complex, definition used** (spectral, vertex operators only):

- `0804.2305:main.tex:155-165`
```
 There are $n-1$
Hecke operators $A_i$, for $1 \le i \le n-1$,
 associated to $\PGL_n(\oo)$-double cosets represented by
$\dig( 1,..., 1,\pi, ..., \pi)$
 with determinant $\pi^i$. A finite
quotient $X_\G = \G \backslash \B_n$ of $\B_n$ by a torsion-free discrete
cocompact  subgroup $\G$ preserving the types of vertices is
again a $(q+1)$-regular finite complex. It is called a {\it
Ramanujan complex} if all the nontrivial eigenvalues of $A_i$ on
$X_\G$ fall within the spectrum of $A_i$ on the universal cover
$\B_n$. See \cite{Li} for more details.
```

**The "prototype" remark** (the authors' own claim that this shape should be general):

- `0804.2305:main.tex:266-269` — `attached to a surface and a curve over a finite field. Since` / `(\ref{zetaidentity}) is expressed in terms of the operators on the` / `finite complex, it is likely to be the prototype of complex zeta` / `functions in general.`

**Euler-product reading of the left-hand side** (an algebraic and a geometric factor):

- `0804.2305:main.tex:3066-3072`
```
\begin{theorem} $Z_-(\G,u)$ and $Z(\G,u)$ are rational functions with the following closed forms:
$$ Z_-(\G,u)=  \frac{\det(1+L_Bu)}{\det(1-L_Eu^2)}\quad \mbox{and} \quad Z(\G,u)= \frac{\det(1+L_Bu)\det(1+L_Bu^{1/2})}{\det(1-L_Eu)\det(1-L_Eu^2)}.$$
\end{theorem}
This gives another interpretation of the zeta identity.
\begin{theorem}[Another zeta identity]\label{newzetaidentity} Let $X_\G = \G \backslash \PGL_3(F)/ \PGL_3(\oo)$. Then
$$\frac{(1-u^3)^{\chi(X_\G)}}{\det(I-A_1u+qA_2u^2-q^3u^3 I)} = Z_1(X_\G,u)Z_-(\G,u).$$
\end{theorem}
```

### C1b. Kang–Li–Wang, "The Zeta Functions of Complexes from PGL(3): a Representation-theoretic Approach" (Israel J. Math. 2010)

**arXiv:0809.1401v1** — title `0809.1401v1:main.tex:144-146`
```
\title[The Zeta Functions of Complexes from $\PGL(3)$: a Representation-theoretic Approach]
{The Zeta Functions of Complexes from $\PGL(3)$: a
Representation-theoretic Approach}
```
authors `0809.1401v1:main.tex:150` `\author{Ming-Hsuan Kang, Wen-Ching Winnie Li and Chian-Jen Wang}`.

> **CAVEAT (must be respected when citing).** The directory `refs/src/0809.1401/` holds the
> *latest*-version tarball of arXiv:0809.1401, and its `main.tex` carries
> `\title[Zeta Functions of Complexes Arising from $\PGL(3)$]{...}` (`:58`) and
> `\author{Ming-Hsuan Kang and Wen-Ching Winnie Li}` (`:59`) — i.e. the **Kang–Li** paper,
> not Kang–Li–Wang, and it is *not* byte-identical to `0804.2305/main.tex` (2944 vs 3180
> lines). The arXiv abs page for 0809.1401 reports the Kang–Li–Wang title for all three
> versions, so the v3 source package is inconsistent with its own metadata. **Quote
> Kang–Li–Wang from `0809.1401v1` only.**

**The operators, defined** (this is the cleanest statement of `A_1, A_2, L_E, L_B`):

- `0809.1401v1:main.tex:342-368`
```
We recall the definition of the operators $L_B$, $L_E$, $A_1$, $A_2$
from \cite{KL}. Following the notation of \cite{KL}, denote by $K$
the maximal compact subgroup of $G$, consisting of elements in $G$
with entries in the ring of integers $\mathcal{O}_F$ of $F$ and
determinant in $\mathcal{O}^\times_F$. Let
$\sigma=\left(\begin{matrix} &1&\\ &&1\\ \pi&&
\end{matrix}\right)$, where $\pi$ is a uniformizer of $F$.
Define the Iwahori subgroup $B=K \cap \sigma K \sigma^{-1} \cap \sigma^{-1}K\sigma$
and the parahoric subgroup $E=K \cap \sigma K \sigma^{-1}$. Note that $B$ is the set of
elements in $K$ congruent to the upper triangular matrices modulo
$\pi$, while  $E$ consists of elements in $K$ whose third
row is congruent to $(0, 0, *)$ mod $\pi$. Clearly,
$B \subset E \subset K$.



Write $t_2=\left(\begin{matrix}&&\pi^{-1}\\ &1&\\ \pi&&\end{matrix}\right)$.
The operator $L_B$ acts on the space $L^2(\Gamma \backslash G/B)$ by sending
a function $f$ in $L^2(\Gamma \backslash G/B)$ to the function $L_B f$, where
$$L_B f(gB)=\sum_{w_iB \in B{t_2\sigma^2}B/B} f(gw_iB).$$ The operator $L_E$
on $L^2(\Gamma \backslash G/E)$ sends a function $f$ in $L^2(\Gamma \backslash G/E)$
to the function $L_E f$ given by $$L_E f(gE)=\sum_{w'_jE \in E(t_2\sigma^2)^2E/E}
f(gw'_jE).$$ The operators $A_1$, $A_2$ on $L^2(\Gamma \backslash G/K)$ are
associated to the double cosets $K\diag(1, 1, \pi)K = \sqcup g_iK$ and
$K\diag(1, \pi, \pi)K = \sqcup g'_jK$ respectively, and they are defined by
$$A_1 f(gK)=\sum_{i} f(gg_iK),$$ $$A_2 f(gK)=\sum_{j} f(gg'_j K),$$ for any $f$
in the space $L^2(\Gamma \backslash G/K)$.
```

**The identity as stated here (no regularity hypothesis on Γ):**

- `0809.1401v1:main.tex:218-221`
```
\begin{eqnarray}\label{zetaoperator}
\frac{(1-u^3)^{\chi(X_\Gamma)}}{\det(I-A_1u+qA_2u^2-q^3 u^3I)} =
\frac{\det(I + L_Bu)}{\det(I - L_E u) \det(I - (L_E)^t u^2)},
\end{eqnarray}
```
- and the removal of the hypothesis, `0809.1401v1:main.tex:244-247` — `this paper we re-establish the zeta identity by computing the` / `spectrum of each operator using representation theory. Our proof not only` / `provides a totally different, new aspect of the identity (1.1), but also removes the regularity` / `assumption on $\Gamma$.`

**Theorem 2 (the RH ⇔ Ramanujan theorem, source of C1a's quoted version):**

- `0809.1401v1:main.tex:1352-1370`
```
\begin{theorem}

The following statements are equivalent.

\begin{itemize}

\item[(1)] $X_{\Gamma}$ is Ramanujan.

\item[(2)] The nontrivial zeros of $\det(I - A_1u + qA_2u^2 -q^3u^3)$
have absolute value $q^{-1}$.

\item[(3)] The nontrivial zeros of $\det(I - L_Eu)$ have absolute
values $q^{-1}$ and $q^{-1/2}$.

\item[(4)] The nontrivial zeros of $\det(I + L_Bu)$ have absolute
values 1, $q^{-1/2}$, and $q^{-1/4}$.

\end{itemize}
\end{theorem}
```

**Theorem 3 (the identity, cleared of denominators):**

- `0809.1401v1:main.tex:1410-1418`
```
\begin{theorem}

There holds the identity

$$(1-u^3)^{\chi(X_\Gamma)} =
\frac{{\det(I-A_1u+qA_2u^2-q^3 u^3I)}{\det(I + L_Bu)}}{\det(I - L_E u) \det(I - (L_E)^t u^2)}.
$$

\end{theorem}
```

The proof is a factor-by-factor bookkeeping over the five types of unitary
Iwahori-spherical representations (a) principal series, (b) 1-dimensional, (c) Steinberg,
(d)/(e) the two non-tempered/tempered subrepresentations of
`Ind(χ|·|^{∓1/2}, χ|·|^{±1/2}, χ^{-2})` — listed at `0809.1401v1:main.tex:391-424`, with the
per-type zeros in Table 1 at `0809.1401v1:main.tex:1132-1154` and the per-type contributions
to the identity at `0809.1401v1:main.tex:1425-1437`. The Steinberg multiplicity is what
produces the Euler-characteristic exponent: `0809.1401v1:main.tex:1183-1186` — `Combined with the total` / `dimension of $V^B$, we get that the total number of Steinberg` / `representations (type (c)), counting multiplicities, is equal to` / `$3\chi(X_\Gamma) - 3$, where $\chi(X_\Gamma)= N_0 - N_1 + N_2$ is`.

**Plain summary (C1).** For a torsion-free cocompact type-preserving Γ ⊂ PGL₃(F), the
2-dimensional complex `X_Γ = Γ\B₃` carries a zeta counting tailless primitive closed
geodesics made of same-type edges. It equals `(1−u³)^{χ}` over the product of the
vertex-Hecke cubic `det(I − A₁u + qA₂u² − q³u³I)` and the directed-chamber factor
`det(I + L_B u)`; equivalently the reciprocal of `det(I − L_E u)det(I − L_Eᵗ u²)`. The
Euler characteristic enters to the **first power** with exponent `χ = N₀ − N₁ + N₂`, and the
base is `(1 − u³)` (rank 3), not `(1 − u²)`. RH is the statement that the nontrivial zeros
of the cubic all have `|u| = q^{-1}`; equivalently the chamber factor's nontrivial zeros lie
on the **three** circles `1, q^{-1/2}, q^{-1/4}` and the edge factor's on the **two** circles
`q^{-1}, q^{-1/2}`. Note that, unlike the graph case, RH here does *not* say a single circle.

---

## C2. General rank: Kang–Yu, PGLₙ, the alternating product over facet dimension

**arXiv:2607.21262** — title `2607.21262:main.tex:150`
`\title[zeta functions]{Zeta functions of PGL$_n$ over non-Archimedean local fields}`;
authors `2607.21262:main.tex:151` `\author{Ming-Hsuan Kang}` and `:155` `\author{Jiu-Kang Yu}`.

**Abstract, the main identity:**

- `2607.21262:main.tex:171-181`
```
the primitive closed \(k\)-geodesics define zeta functions \(Z_k\) and their
\(\epsilon\)-twisted variants \(Z_k^\epsilon\).  Our main result identifies
an alternating product of these zeta functions with the unramified
\(L\)-function of \(L^2(\Gamma\backslash \mathrm{PGL}_n(F))\):
\[
(1-u^n)^{\chi(\Gamma\backslash\scrB)}
L(\Gamma,q^{(n-1)/2}u)
=
\prod_{k=1}^{n-1} Z_k^\epsilon(\Gamma\backslash\scrB,u)^{(-1)^{k+1}}.
\]
This gives a uniform Ihara-type identity for all \(\mathrm{PGL}_n\).  We also
```

**The `k`-geodesic zeta and its ε-twist:**

- `2607.21262:main.tex:1971-1981`
```
For a closed \(k\)-geodesic \(\scrC\), define
\[
\epsilon(\scrC):=(-1)^{(k+1)l_G(\scrC)}.
\]
We also define the \(\epsilon\)-twisted \(k\)-th geodesic zeta function by
\[
Z_k^\epsilon(\X,u)
=
\prod_{[\scrC]}
\left(1-\epsilon(\scrC)u^{l_A(\scrC)}\right)^{-1}.
\]
```
(`l_A` = algebraic length, `l_G` = geometric length = number of facets; both defined at
`2607.21262:main.tex:289-290` — `Here \(l_A\) is the algebraic length; the geometric length \(l_G\) records` / `the number of facets.`)

**Main theorem:**

- `2607.21262:main.tex:2014-2026`
```
\begin{theorem}\label{main}
Let \(\Gamma\) be a discrete torsion-free cocompact subgroup of \(G_\ad\), and
assume that \(\Gamma\) preserves vertex types, equivalently
\(\Gamma\subset\ker(G_\ad\to\Xi_\ad\simeq\mathbb Z/n\mathbb Z)\).  Put
\(\X:=\Gamma\backslash\scrB\). Then
\[
(1-u^n)^{\chi(\X)}\,L(\Gamma,q^{(n-1)/2}u)
=
\prod_{k=1}^{n-1}Z_k^\epsilon(\X,u)^{(-1)^{k+1}},
\]
where \(\chi(\X)\) is the Euler characteristic of the finite \(\Delta\)-complex \(\X\).
Here \(L(\Gamma,u)\) is the unramified standard \(L\)-function defined above.
\end{theorem}
```
with `2607.21262:main.tex:1995-2005` — `\[` / `L(\rho,u)=\det(I-s(\rho)u)^{-1},` / `\]` / `where \(I\) is the identity matrix.` / ... / `L(\Gamma,u)=\prod_\rho L(\rho,u)^{m(\rho)}.` — i.e. the `L`-function is itself a reciprocal
Hecke determinant (the PGL₃ case reduces to `1/det(I − A₁u + qA₂u² − q³u³I)`, C3 below).

**The Hashimoto-type (successor-operator) determinant, for each facet dimension:**

- `2607.21262:main.tex:2304-2312`
```
\begin{theorem}\label{thm:zeta-determinant}
For \(1\le k\le n-1\), with \(T_k=T_k(u)\) acting on \(C_k(\X)\), the zeta
functions are given by the rational functions
\[
Z_k(\X,u)=\det(I-T_k)^{-1},
\qquad
Z_k^\epsilon(\X,u)=\det\!\left(I-(-1)^{k+1}T_k\right)^{-1}.
\]
\end{theorem}
```

**The Laplacian/Hecke bridge (how the Euler-characteristic factor appears):**

- `2607.21262:main.tex:2410-2438`
```
\begin{theorem}\label{thm:Phi-determinants}
The operators \(\Phi_i\) satisfy the following determinant identities:
\begin{itemize}
\item[(1)]
\[
\det(\Phi_0\mid C_0(\X))
=
\det\!\left(
\sum_{i=0}^n (-q^{(i-1)/2}u)^i \hat A_i
\;\middle|\;
C_0(\X)
\right).
\]

\item[(2)]
For $i\ge1$,
\[
\det(\Phi_i\mid C_i(\X))
=
(1-u^n)^{iV_i}\,
\det\!\left(I-(-1)^{i+1}T_i\mid C_i(\X)\right),
\]
where
\[
V_i=\frac{1}{i+1}\dim C_i(\X)
\]
is the number of $i$-facets of $\X$.
\end{itemize}
\end{theorem}
```
with `2607.21262:main.tex:2400-2402` — `\[` / `\Phi_i=\Delta_i+(1-u^n)\,\mathrm{Id}_{C_i(\scrB)}.` / `\]`.

**What the paper says about the state of the art before it:**

- `2607.21262:main.tex:246-250`
```
This paper resolves that problem for the entire family
\(\mathrm{PGL}_n(F)\), \(n\ge2\).  Since its building has dimension \(n-1\),
this is a single theory encompassing geometry of arbitrarily high dimension.
To our knowledge, it is the first Ihara-type identity uniform in \(n\) for
this family.
```
- and the reduction to the known cases, `2607.21262:main.tex:321-324` — `For \(n=2\), the two lengths agree and the theorem is precisely` / `Ihara's identity~\eqref{eq:Ihara}.  For \(n=3\), after matching conventions,` / `it gives the main identity of~\cite{KL}, with the \(k=1\) and \(k=2\) factors` / `corresponding to the edge and chamber contributions.`

**Placement.** Here the `(1 − u^n)^{χ}` factor and the `L`-function sit together on the
**left**; the alternating product `∏_k Z_k^ε(u)^{(−1)^{k+1}}` on the right means the
odd-`k` (edge-like) zetas are in the numerator and the even-`k` (chamber-like) zetas in the
denominator. In terms of determinants (`thm:zeta-determinant`), the right-hand side is
`∏_k det(I − (−1)^{k+1} T_k)^{(−1)^k}` — so the chamber factor `det(I + L_B u)` of C1
reappears as the `k = 2` factor **upstairs**, matching `0809.1401v1:main.tex:1414-1416`.

**Plain summary (C2).** This is the general-rank answer: for every `n`, primitive closed
`k`-geodesics (straight strips paved by `k`-facets, equivalently sequences of pointed
`k`-facets under a local successor relation) define zeta functions `Z_k`, each a reciprocal
determinant of a `k`-dimensional Hashimoto successor operator `T_k`; the alternating product
over `k = 1,…,n−1` equals `(1 − u^n)^{χ}` times the unramified standard `L`-function
evaluated at `q^{(n−1)/2}u`. The proof is cohomological (Hoffman's torsion reformulation of
Bass), with `Δ_i + (1−u^n)Id` on the building's cochain complex as the comparison object.

> **What I could NOT verify from this TeX.** 2607.21262 contains **no** RH or Ramanujan
> theorem: grepping the source for `Ramanujan`/`Riemann hypothesis`/`tempered` returns only
> `2607.21262:main.tex:222-223` (a historical remark) and three bibliography titles
> (`:3474`, `:3489`, `:3614`). The general-rank RH statement is Kang's J. Number Theory
> 2016 paper (not on arXiv — see "Not found"), Kamber's C7a, and LLP's C5.

---

## C3. Kang–Li–Wang, "Zeta and L-functions of finite quotients of apartments and buildings"

**arXiv:1505.00902** — title `1505.00902:Zeta-and-Lfunction-20170426.tex:78`
`\title{Zeta and L-functions of finite quotients of apartments and buildings}`;
authors `:79` `\author{Ming-Hsuan Kang, Wen-Ching Winnie Li, and Chian-Jen Wang}`.

**The dictionary L-function ↔ Hecke determinant, PGL₃:**

- `1505.00902:Zeta-and-Lfunction-20170426.tex:1134`
```
$$L(\Ga \bs G(F), \pi_1, qu) = \frac{1}{\det(I-A_1u+q A_2u^2-q^3u^3I)}.$$
```
- `1505.00902:Zeta-and-Lfunction-20170426.tex:1137-1138`
```
$$Z(\B_\Ga, \pi_1, u) =\frac{1}{ \det(I - L_Eu)} \quad {\rm{and}} \quad Z(\B_\Ga, \pi_2, u) = \frac{1}{\det(I - (L_E)^t u)},$$
where $E$ is a parahoric subgroup of $K$,  $L_E$ is the parahoric operator on $L^2(\Ga \bs G(F)/E)$ associated to the double coset $E\diag(1, 1, \varpi)E$, and $(L_E)^t$ is the transpose of $L_E$.   Likewise, the type 2 chamber zeta fu
```
- `1505.00902:Zeta-and-Lfunction-20170426.tex:1141` — `$$Z_{2,2}(\B_\Ga, u) = Z_2(\B_\Ga, \pi_1, u) = \frac{1}{\det(I - L_Iu)}.$$`
- `1505.00902:Zeta-and-Lfunction-20170426.tex:1149-1152`
```
\begin{equation*}
Z(\B_\Ga, u) %= \frac{1}{\det(I-L_E u)\det(I-(L_E)^t u^2)} \\
= \frac{(1-u^3)^{\chi(\B_\Ga)}}{\det(I-A_1u+q A_2u^2-q^3u^3I) \det(I + L_Iu)},
\end{equation*}
```

**The identity restated with `L`- and zeta-functions only:**

- `1505.00902:Zeta-and-Lfunction-20170426.tex:1155-1161`
```
\begin{theorem}\label{buildingA2}
With $G=$PGL$_3$, the following identity for the finite quotient $\B_\Ga$ holds:
\begin{eqnarray}\label{A2-building}
 (1-u^3)^{\chi(\B_\Ga)}L(\Ga \bs G(F), \pi_1, qu) = \frac{Z(\B_\Ga, \pi_1, u) Z(\B_\Ga, \pi_2, u^2)}{Z_2(\B_\Ga, \pi_1, -u)},
\end{eqnarray}
where $\chi(\B_\Ga)$ denotes the Euler characteristic of $\B_\Ga$.
\end{theorem}
```
This is the `n = 3` case of C2's alternating product, with the gallery (`k = 2`) zeta in the
**denominator** — and note the argument `−u` there.

**The Euler characteristic, explicitly, for a PGL₃ quotient:**

- `1505.00902:Zeta-and-Lfunction-20170426.tex:1163-1166`
```
Let $N_0, N_1$, and $N_2$ denote the number of vertices, edges, and chambers in $\B_\Ga$, respectively. Then $N_1=(q^2+q+1)N_0$ and $N_2=
\frac{1}{3}(q+1)(q^2+q+1)N_0$ so that the Euler characteristic
$$\chi(\B_{\Ga})=N_0-N_1+N_2=\frac{1}{3}(q-1)^2(q+1)N_0.$$
Notice that when $q$ is set to $1$, $\chi(\B_{\Ga})$ vanishes and (\ref{A2-building})  reduces to (5.2) in Theorem \ref{Aidentity}.
```
Useful for the notebook: `χ > 0` here and vanishes at the "field with one element" `q = 1`.

**The PGSp₄ analogues (spin and standard L-functions):**

- `1505.00902:Zeta-and-Lfunction-20170426.tex:1197` — `$$ L(\Ga \bs G(F), \pi_\spin, q^{3/2}u) = \frac{1}{\det(I-A_1 u+qA_2 u^2-q^3 A_1 u^3+q^6I u^4)}.$$`
- `1505.00902:Zeta-and-Lfunction-20170426.tex:1210-1211`
```
$$\frac{(1-u^2)^{\chi(\B_{\Gamma})}(1-q^2 u^2)^{-(q^2-1)N_p}}{\det(I-A_1 u+qA_2 u^2-q^3 A_1 u^3+q^6I u^4)}
= \frac{\det(I-L_I u)}{\det(I-L_{P_1} u)\det(I-L_{P_2}u^2)}.$$
```
- `1505.00902:Zeta-and-Lfunction-20170426.tex:1180-1182` — `The Euler characteristic of $\B_\Ga$ is` / `$$\chi(\B_{\Ga})=N_0-N_1+N_2=(q-1)^2(q^2+q+1)N_p.$$` / `In particular, it vanishes when $q$ is set to $1$.`

**Plain summary (C3).** Kang–Li–Wang's later paper is the Rosetta stone: it identifies every
determinant in the PGL₃ and PGSp₄ identities with a Langlands `L`-function of a
representation `π` of the dual group (minuscule `π₁, π₂` for PGL₃; spin and standard for
PGSp₄) and with a zeta counting `π`-geodesic walks or `π`-geodesic galleries. It also
supplies the degenerate `q = 1` apartment case, where the Euler-characteristic factor
disappears.

---

## C4. Fang–Li–Wang: PGSp₄ / Sp(4) complexes

**arXiv:1109.3854** — title `1109.3854:zetagsp4-final.tex:62`
`\title{The Zeta Functions of Complexes from $\Sp(4)$}`;
authors `:64` `\author{Yang Fang, Wen-Ching Winnie Li and Chian-Jen Wang}`.

**Theorem 1.1 (the identity, two ways):**

- `1109.3854:zetagsp4-final.tex:128-136`
```
\begin{theorem} Assume $\ord_{\pi}  \det (\Gamma) \subset 4 \mathbb Z$. The zeta function $Z(X_\Gamma, u)$ is a rational function expressed in two ways, the first in terms of the two vertex adjacency operators $A_1$ and $A_2$ and the chamber adjacency operator $L_I$, and the 
\begin{equation}\label{GSp4zeta}
\begin{aligned}
Z(X_\Gamma, u) &= \frac{(1-u^2)^{\chi(X_{\Gamma})}(1-q^2 u^2)^{2N_p-N_{ns}}}{\det(I-A_1 u+qA_2 u^2-q^3 A_1 u^3+q^6I u^4)\det(I-L_I u)}\\
&= \frac{1}{\det(I-L_{P_1} u)\det(I-L_{P_2}u^2)},
\end{aligned}
\end{equation}
where $\chi(X_{\Gamma})$ is the Euler characteristic of $X_{\Gamma}$, and $2N_p$ (resp. $N_{ns}$) is the number of special (resp. non-special) vertices in $X_{\Gamma}$.
\end{theorem}
```

**Theorem 1.2 (RH ⇔ Ramanujan, five equivalent statements):**

- `1109.3854:zetagsp4-final.tex:145-157`
```
\begin{theorem} The following statements are equivalent:

$(1)$ $X_{\Gamma}$ is Ramanujan.

$(2)$ All the nontrivial zeros of $\det(I-A_{1}u+qA_{2}u^{2}-q^{3}A_{1}u^{3}+q^{6}Iu^{4})$ have absolute value $q^{-\frac{3}{2}}$.

$(3)$ All the nontrivial zeros of $\det(I - L_{P_{1}} u)$ have absolute values $q^{-\frac{3}{2}}$ or $q^{-1}$.

$(4)$ All the nontrivial zeros of $\det(I - L_{P_{2}} u)$ have absolute values $q^{\alpha}$, where $-2 \le \alpha \le -1$.

$(5)$ All the nontrivial zeros of $\det(I - L_{I} u)$ have absolute values $1$ or $q^{\beta}$, where $-1 \le \beta \le -\frac{1}{2}$.

\end{theorem}
```
(restated verbatim in §7 at `1109.3854:zetagsp4-final.tex:1076-1090`).

**Ramanujan, definition used here** (representation-theoretic, temperedness):

- `1109.3854:zetagsp4-final.tex:1067-1068`
```
We extend the notion of Ramanujan complexes to the symplectic case. Given a discrete torsion-free cocompact-mod-center subgroup $\Gamma$ of $G$ as before, define $X_{\Gamma}$ to be Ramanujan if all the irreducible unramified infinite-dimensional representations that occur in $L^2(\Gamma \bb G/Z)$ are tempered. Since only infinite-dimensional representations are concerned in the definition, the zeros of each determinant listed in Table 3 arising from 1-dimensional representations (type IVd) are called trivial zeros, whereas those arising from infinite-dimensional representations are nontrivial.
```

**Plain summary (C4).** In type `C̃₂` the vertex determinant becomes **quartic**,
`det(I − A₁u + qA₂u² − q³A₁u³ + q⁶Iu⁴)` (the degree-4 spin `L`-function), the base of the
Euler-characteristic factor drops back to `(1 − u²)`, and a **second** topological factor
`(1 − q²u²)^{2N_p − N_ns}` appears with a *positive* exponent in the numerator. RH is now
the statement that the vertex determinant's nontrivial zeros lie on `|u| = q^{-3/2}`; the
edge and chamber factors give only *bands* of moduli (intervals `q^{α}`, `−2 ≤ α ≤ −1`), not
finitely many circles. This is the first sign that "RH ⇔ Ramanujan" in higher rank is not a
single-circle statement.

---

## C5. Lubetzky–Lubotzky–Parzanchevski: the geodesic-flow digraph (the higher-dimensional Hashimoto operator)

**arXiv:1702.05452** — title `1702.05452:rw_ramanujan_complex.tex:176-177`
`\title[Random walks on Ramanujan complexes and digraphs]{Random walks on\\` / `  Ramanujan complexes and digraphs}`;
authors `:154` `\author[E. Lubetzky]{E. Lubetzky}`, `:160` `\author[A. Lubotzky]{A. Lubotzky}`,
`:166` `\author[O. Parzanchevski]{O. Parzanchevski}`.

**The geodesic flow on a building, by dimension `j`:**

- `1702.05452:rw_ramanujan_complex.tex:999-1002`
```
for every $1\leq j\leq m-1$, we define the ``$j$-th-unit bundle''
$UT^{j}\mathcal{B}$ as the set of pairs $\left(v\in \mathcal{B}\left(0\right),\sigma\in\mathcal{B}\left(j\right)\right)$
(where $\cB(j)$ is the set of $j$-dimensional cells) such that $v\in\sigma$, and the vertices in $\sigma$ are of colors
$\col\left(v\right),\col\left(v\right)+1,\ldots,\col\left(v\right)+j$.
```
- `1702.05452:rw_ramanujan_complex.tex:1009-1019`
```
\begin{definition}\label{def:geodesic-flow} The geodesic flow $T$
on $UT^{j}\mathcal{B}$ is defined as follows: $T(\sigma)$ for $\sigma=\left(v_{0},\left\{ v_{0},\ldots,v_{j}\right\} \right)\in UT^{j}\mathcal{B}$,
with $\col\left(v_{i}\right)\equiv\col\left(v_{0}\right)+i$, consists
of all the cells $\sigma'=\left(v_{1},\left\{ v_{1},\ldots,v_{j},w\right\} \right)\in UT^{j}\mathcal{B}$
such that 
\begin{enumerate}
\item $\col\left(w\right)\equiv\col\left(v_{1}\right)+j$ (the ``direction
vector'' is based at $v_{1}$), 
\item $\{v_{0},v_{1},\ldots,v_{j},w\}$ is not a cell (geodicity). 
\end{enumerate}
\end{definition}
```
- and the identification with non-backtracking in dimension one,
`1702.05452:rw_ramanujan_complex.tex:1021-1027` — `For example, in dimension one, the geodesic flow on $UT^{1}X$ coincides` / `with the non-backtracking walk on the graph $X$, since any two neighbors` / `$v,w$ satisfy $\col\left(w\right)\equiv\col\left(v\right)+1$, and` / `there are no triangles, so (2) reduces to $w\neq v_{0}$. When` / `$X$ is of higher dimension, (2) also prevents the flow on $U T^{1}X$` / `from making two steps along the edges of a triangle, as there is a` / ```shorter route''.`

**Ramanujan digraph, definition:**

- `1702.05452:rw_ramanujan_complex.tex:330-336`
```
An important tool in this work is the directed analog of Ramanujan graphs. We define a finite $k$-out-regular digraph $\cY$ to be Ramanujan if the following holds:

\vspace{-0.35cm}
\begin{equation}\begin{tabular}{l}every eigenvalue $\lambda\in\C$ of the adjacency matrix   \\
of $\cY$ satisfies either $\left|\lambda\right|\leq\sqrt{k}$
or $\left|\lambda\right|=k$\end{tabular}\,.\label{eq:ram-digrap-def}
\end{equation}
```

**The digraph zeta, and the `T`-zeta of a complex:**

- `1702.05452:rw_ramanujan_complex.tex:1390-1401`
```
\begin{equation}
Z_{\cY}\left(u\right)=\prod_{\left[\gamma\right]}\frac{1}{1-u^{\ell\left(\gamma\right)}}\,,\label{eq:digraph-zeta}
\end{equation}
where $\left[\gamma\right]$ runs over  the equivalence classes of primitive
(directed) cycles in $\cY$, one has:
\begin{theorem}[\cite{bowen1970zeta,kotani2000zeta}]
\label{thm:digraph-zeta-polynom}If $N_{m}\left(\cY\right)$ is the
number of (directed) cycles of length $m$ in $\cY$, then 
\[
Z_{\cY}\left(u\right)=\exp\biggl(\sum_{m=1}^{\infty}\frac{N_{m}\left(\cY\right)}{m}u^{m}\bigg)=\frac{1}{\det\left(I-uA_{\cY}\right)}\,.
\]
\end{theorem}
```
- `1702.05452:rw_ramanujan_complex.tex:1405-1412`
```
\begin{definition}
For every $G$-equivariant branching operator $T$ on $\fC\subseteq\mathcal{B}=\mathcal{B}(G)$,
the \emph{$T$-zeta function} of a quotient complex
$X=\Gamma\backslash\mathcal{B}$ (as in \S\ref{sec:Ramanujan-complexes})
is defined as 
$\mathfrak{z}_{T}\left(X,u\right)=Z_{\cY_{T,\fX}}(u)$, namely \eqref{eq:digraph-zeta}, with $\gamma$ running over the equivalence classes of primitive
cycles in the digraph defined by $T$ on $\fX$.
\end{definition}
```

**The RH corollary — "Ramanujan complex ⇒ RH", for every `G`:**

- `1702.05452:rw_ramanujan_complex.tex:410-416`
```
\begin{maincoro}
\label{cor:R-H-for-Ramanujan} Let $X$ be a Ramanujan complex as in~\eqref{eq:ram-def}, and let $Z_{\cY_{T,\fX}}(u)$ be
the zeta function associated with a $G$-equivariant, collision-free, $k$-regular branching operator $T$
on $\cB=\mathcal{B}\left(G\right)$. Then $Z_{\cY_{T,\fX}}(u)$ satisfies the Riemann Hypothesis;
that is, if $Z_{\cY_{T,\fX}}\left(u\right)$ has a pole at $k^{-s}$
then $|s|=1$ or $\Re\left(s\right)\leq\frac{1}{2}$.
\end{maincoro}
```
- the mechanism, `1702.05452:rw_ramanujan_complex.tex:1417-1419` — `We have shown in~\S\ref{sec:Ramanujan-complexes} that if $X=\Gamma\backslash\cB$ is a Ramanujan complex` / `and $T$ is a $G$-equivariant, $k$-regular, collision-free branching operator on $\cB$, then $\cY_{T,\fX}$ is Ramanujan. In particular, the $T$-zeta function of $X$ satisfies the R.H.; that is, if ` / `$\mathfrak{z}_{T}\left(X,k^{-s}\right)=\infty$ then either $|s|=1$ or $\Re\left(s\right)\le\frac{1}{2}$, establishing Corollary~\ref{cor:R-H-for-Ramanujan}.`

**Important honesty caveats from the source** (the inequality `Re s ≤ 1/2` is *not* an
equality, unlike the graph case):

- `1702.05452:rw_ramanujan_complex.tex:1420-1424`
```
\begin{remark}
 The bound $\left|\Re (s)\right|\leq\frac{1}{2}$ is the true situation: there are poles 
with $\left|\Re (s)\right|<\frac{1}{2}$. In fact, already in the graph case there are poles with $|\Re (s)|=0$, 
and in higher dimension there are also poles with $0<|\Re( s)|<\frac{1}{2}$ (see, e.g.,~\cite{kang2010zeta}).
\end{remark}
```
- `1702.05452:rw_ramanujan_complex.tex:1425-1438`
```
\begin{remark} 
Zeta functions of this kind have been studied by a 
number of authors~\cite{deitmar2006ihara,kang2010zeta,kang2014zeta,kang2015zeta,fang2013zeta,kang2016riemann}.
The most general results regarding the R.H.\ are due to Kang~\cite{kang2016riemann},
who studied the case of buildings of type $\widetilde{A}_{n}$
and gave more detailed information about the poles of the zeta functions corresponding to geodesic flows,
via case by case analysis of the representations of $\mathrm{GL}_{n}\left(F\right)$. In~\cite{fang2013zeta}, 
the same is done for the building of type $\widetilde{C}_2$ associated with $\mathrm{PSp}(4)$.
Our simple combinatorial treatment gives
the upper bound on $\Re\left(s\right)$ but not the exact possible
values of it. However, our method applies for any building, and not only those of type $\widetilde{A}_{n}$ and $\widetilde{C}_{2}$.
It seems, in any case, that for combinatorial applications
the upper bound on $\Re\left(s\right)$ suffices, as is illustrated in this paper.
\end{remark}
```
- the converse, `1702.05452:rw_ramanujan_complex.tex:1439-1444`
```
\begin{remark}
 For $k$-regular graphs,  it is known that the converse also holds: the R.H.\ for the zeta function of a graph implies
it is Ramanujan. In~\cite{kang2010zeta} it was shown that the R.H.\ for zeta functions of geodesic
flows on the building of type $\widetilde{A}_2$ implies that a quotient complex is Ramanujan. Recently, an analogous result was
established by Kamber for buildings of general type~\cite{Kamber2017LP}.
\end{remark}
```

**Plain summary (C5).** The right higher-dimensional Hashimoto operator is a *branching*
(multi-valued) operator, not a permutation: the `j`-dimensional geodesic flow on the pairs
(basepoint, `j`-cell) of a building, with "geodicity" enforced by the condition that the
next `(j+2)`-set is **not** a cell. Its digraph on a finite quotient has a zeta which is a
plain reciprocal determinant, `det(I − uA_Y)^{-1}`; if the quotient is a Ramanujan complex
then this digraph is a Ramanujan digraph (`|λ| ≤ √k` off the trivial `|λ| = k`) and the zeta
satisfies RH in the weak form `Re s ≤ 1/2`. This covers *every* affine building, not only
`Ã_n` and `C̃₂`.

### C5a. Parzanchevski, "Ramanujan Graphs and Digraphs" (survey)

**arXiv:1804.08028** — title `1804.08028:Ramanujan_digraphs.tex:142`
`\title{Ramanujan Graphs and Digraphs}`; author `:143` `\author{Ori Parzanchevski}`.
(The file is latin9-encoded; `grep` needs `-a`.)

- the theorem, restated, `1804.08028:Ramanujan_digraphs.tex:514-521`
```
\begin{thm}[\cite{Lubetzky2017RandomWalks}]
Let $\mathcal{X}$ be a complex whose universal cover is the affine
Bruhat-Tits building $\mathcal{B}$, and let $W$ be a geometric regular
random walk operator. If $W$ is collision-free on $\mathcal{B}$
(namely, $\mathcal{D}_{W}\left(\mathcal{B}\right)$ is collision-free),
and $\mathcal{X}$ is a Ramanujan complex, then $\mathcal{D}_{W}\left(\mathcal{X}\right)$
is a Ramanujan digraph.
\end{thm}
```
- the "geodesic edge walk" in plain words, `1804.08028:Ramanujan_digraphs.tex:528-533` —
`Let us give one concrete example: the \emph{geodesic edge walk }on` / `a complex goes from a directed edge $\left(v,w\right)$ to the directed` / `edge $\left(w,u\right)$ if $u\neq v$ (no backtracking), and in addition` / `$\left\{ v,w,u\right\} $ is \textbf{not }a triangle in the complex` / `(so the path $v\rightarrow w\rightarrow u$ is not ``homotopic''` / `to the shorter path $v\rightarrow u$). `
- and the sharp normality, `1804.08028:Ramanujan_digraphs.tex:546-551` — `Finally, all geometric walks on quotients of a fixed building $\mathcal{B}$` / `form a family of almost-normal digraphs \cite[Prop.\ 4.5]{Lubetzky2017RandomWalks}.` / `For the geodesic edge walk on $\widetilde{A}_{d}$-Ramanujan complexes,` / `the corresponding Ramanujan digraphs are sharply $\left(d+1\right)$-normal` / `\cite[Prop.\ 5.3, 5.4]{Lubetzky2017RandomWalks}, and they can be` / `made to be $m$-periodic for any $m$ dividing $\left(d+1\right)$.`
- the RH statement in `s`, both directions, `1804.08028:Ramanujan_digraphs.tex:996-1007`
```
For digraphs the story is simpler:
the zeta function $Z_{\mathcal{D}}\left(u\right)$ of a digraph $\mathcal{D}$
(following \cite{bowen1970zeta,hashimoto1989zeta,kotani2000zeta})
is $Z_{\mathcal{D}}\left(u\right)=\prod_{\left[\gamma\right]}\left(1-u^{\ell\left(\gamma\right)}\right)^{-1}$,
where $\gamma$ is a primitive directed cycle of length $\ell\left(\gamma\right)$
in $\mathcal{D}$, and $\left[\gamma\right]$ is the equivalence class
of its cyclic rotations. One then has $Z_{\mathcal{D}}\left(u\right)=\det\left(I-u\cdot A_{\mathcal{D}}\right)^{-1}$,
so that by (\ref{eq:ram-digraph}) a $k$-regular digraph $\mathcal{D}$
is Ramanujan if and only if every pole at $Z_{\mathcal{D}}\left(k^{-s}\right)$
satisfies $\Re s=1$ or $0\leq\Re s\leq\frac{1}{2}$. The fact that
we cannot rule out $s$ with $0<\Re s<\frac{1}{2}$ is demonstrated
by (\ref{eq:PGL3-spec}), for example.
```
So for **digraphs** the RH ⇔ Ramanujan equivalence *is* an iff, but the RH is the band
`0 ≤ Re s ≤ 1/2`, not the line `Re s = 1/2`.

---

## C6. Storm: the zeta of a hypergraph (and why it is not a new object)

**arXiv:math/0608761** — title `math/0608761:Ihara-SelbergofHypergraph.tex:64`
`\title{The Zeta Function of a Hypergraph}`; author `:65` `\author{Christopher K. Storm\\`.

**Definition (hyperedge backtracking, prime cycle, zeta):**

- `math/0608761:Ihara-SelbergofHypergraph.tex:151`
```
To define our zeta function, we need the appropriate concept of a ``prime cycle."  A \emph{closed path} in $\hyperH$ is a sequence $c = (v_1, e_1, v_2, e_2, \cdots, v_k, e_k, v_1)$, of \emph{length} $k = |c|$, such that $v_i \in e_{i - 1}, e_i$ for $i \in \IZ / k\IZ$.  Note that this implies that $v_1 \in e_k$ so that this path really is ``closed."  We say $c$ has  \emph{hyperedge backtracking} if there is a subsequence of $c$ of the form $(e, v, e)$.
```
- `math/0608761:Ihara-SelbergofHypergraph.tex:173-174`
```
For $u \in \IC$ with $|u|$ sufficiently small, we define the \emph{generalized Ihara-Selberg zeta function} of a finite hypergraph $\hyperH$ by
\[\zeta_\hyperH(u) = \prod_{\mathfrak{p} \in P}\left(1 - u^{|\mathfrak{p}|}\right)^{-1},\]
```

**Perron–Frobenius (Hashimoto) form and the bipartite reduction:**

- `math/0608761:Ihara-SelbergofHypergraph.tex:341-342`
```
There is a one-to-one correspondence between prime cycles of length $l$ in $\hyperH$ and admissible prime cycles of length $l$ in $\hyperH_L^o$.  In particular, the zeta function of $\hyperH$ can be written as
\[\zeta_\hyperH(u) = \det(I - uT)^{-1},\]
```
- `math/0608761:Ihara-SelbergofHypergraph.tex:417` — `Let $\hyperH$ be a finite, connected hypergraph with associated bipartite graph $B_\hyperH$.  Then there is a one-to-one correspondence between prime cycles of length $l$ in $\hyperH$ and prime geodesics of length $2l$ in $B_\hyperH$.`
- `math/0608761:Ihara-SelbergofHypergraph.tex:430` — `\[ \zeta_\hyperH(u) = Z_{B_\hyperH}(\sqrt{u}).\]`

**Bass, transported:**

- `math/0608761:Ihara-SelbergofHypergraph.tex:453-458`
```
\begin{Thm}[Bass]
Let $X$ be a finite, connected graph with adjacency operator $A$ and operator $Q$ defined by $D - I$ where $D$ is the diagonal operator with the degree of vertex $v_i$ in the $i$th slot of the diagonal.  Let $I$ be the $|V| \times |V|$ identity operator.  Then,
\[Z_{X}(u) = (1 - u^2)^{\chi(X)} \det(I - uA + u^2Q)^{-1}\]
where $\chi = |V| - |E|$ is the Euler Number of the graph $X$.
\label{Thm:Bass}
\end{Thm}
```
- `math/0608761:Ihara-SelbergofHypergraph.tex:463`
```
\[\zeta_\hyperH(u) = Z_{B_\hyperH}(\sqrt{u}) = (1 - u)^{\chi(B_\hyperH)} \det(I - \sqrt{u}A_{B_\hyperH} + uQ_{B_\hyperH})^{-1},\]
```
- Hashimoto's exact `(d,r)`-regular factorisation,
`math/0608761:Ihara-SelbergofHypergraph.tex:489-498`
```
\begin{Thm}
Suppose that $\hyperH$ is a finite, connected $(d, r)$-regular hypergraph with $d \geq r$.  Let $n_1 = |V(\hyperH)|$, $n_2 = |E(\hyperH)|$, and $q = (d-1)(r-1)$.  Let $A$ be the adjacency operator of $\hyperH$, and let $A^*$ be the adjacency operator of $\hyperH^*$.  Then one has
\begin{align*}
\zeta_\hyperH&(u)^{-1} \\
&= (1-u)^{-\chi(B_\hyperH)}(1+(r-1)u)^{(n_2 - n_1)}\times\det[I_{n_1} - (A - r + 2)u +qu^2] \\
&= (1-u)^{-\chi(B_\hyperH)}(1+(d-1)u)^{(n_1 - n_2)}\times\det[I_{n_2} - (A^* - d +2)u +qu^2],
\end{align*}
where $-\chi(B_\hyperH) = n_1(d-1) - n_2 = n_2(r-1) - n_1$.
\label{Thm:RegularHypergraphGeneralFactor}
\end{Thm}
```

**Ramanujan hypergraph and the modified RH:**

- `math/0608761:Ihara-SelbergofHypergraph.tex:140-147`
```
\begin{Def}[Li and Sol\'e]
Let $\hyperH$ be a finite, connected $(d, r)$-regular hypergraph.  We say $\hyperH$ is a \emph{Ramanujan hypergraph} if
\begin{equation}
|\lambda - r + 2| \leq 2\sqrt{(d-1)(r-1)},
\end{equation}
for all \emph{non-obvious} eigenvalues $\lambda \in \text{Spec}(\hyperH)$ such that $\lambda \neq d(r-1).$
\label{Def:RamHypergraph}
\end{Def}
```
- `math/0608761:Ihara-SelbergofHypergraph.tex:621-630`
```
\begin{Def}
Let $\hyperH$ be a $(d, r)$-regular hypergraph with $d \geq r$ and $q = (d-1)(r-1)$.  We then consider $\zeta_\hyperH(q^{-s})$.  We say that $\zeta_\hyperH(q^{-s})$ satisfies the \emph{modified hypergraph Riemann hypothesis} if and only if for
\[\text{Re }s \in (0, 1), \, \, \, \frac{(1+(r-1)q^{-s})^{(n_2 - n_1)}}{\zeta_\hyperH(q^{-s})} = 0 \Longrightarrow \text{Re } s = \frac{1}{2}.\]
\end{Def}

Then the previous two propositions can be summarized by
\begin{Thm}
For a $(d, r)$-regular hypergraph $\hyperH$, $\zeta_\hyperH(q^{-s})$ satisfies the modified hypergraph Riemann hypothesis if and only if $\hyperH$ is a Ramanujan hypergraph.
 \label{Thm:RamanujanEquivalence}
 \end{Thm}
```

**Plain summary (C6).** Storm's hypergraph zeta is the only "general combinatorial object"
zeta with a genuine Bass identity *and* an if-and-only-if Ramanujan theorem — but the
theorem `ζ_H(u) = Z_{B_H}(√u)` says it is literally the Ihara zeta of the incidence
bipartite graph in the variable `√u`. So any simplicial complex, read as a hypergraph
(all simplices as hyperedges), gets a zeta — but it is a *graph* zeta of a derived graph,
blind to the simplicial structure beyond incidence, and the "modified RH" needs the
auxiliary factor `(1 + (r−1)q^{-s})^{n₂−n₁}` divided out. Note also the exponent placement:
in the Bass form the Euler factor `(1 − u)^{χ(B_H)}` is in the **numerator** of `ζ_H` (so
`(1−u)^{−χ}` in `ζ^{-1}`), `χ(B_H) = |V| − |E|` of the bipartite graph, and the base is
`(1 − u)`, not `(1 − u²)`, because of the `√u` substitution.

### C6a. The hypergraph non-backtracking operator, non-uniform Ihara–Bass

**arXiv:2204.13586** — title `2204.13586:shared.tex:43`
`\title{Nonbacktracking Spectral Clustering of Nonuniform Hypergraphs}`;
authors `2204.13586:shared.tex:45-49` (alphabetical: Philip S. Chodrow, Nicole Eikmeier,
Jamie Haddock).

- `2204.13586:content/ihara-bass.tex:62-72`
```
\begin{theorem}[Ihara-Bass for nonuniform hypergraphs]\label{thm:ib-nonuniform}
    For any hypergraph $\HG$, we have 
    \begin{equation}
        \det(\mI - \mu \bB) = f_\HG(\mu) \det \paren*{\mI_{\kappa n} + \mu ((\mK - 2\mI_{\kappa})\otimes \mI_n - \bA) + \mu^2 \revision{(\bD - \mI_{\kappa n})}((\mK - \mI_{\kappa}) \otimes \mI_n)}\;,  \label{eq:ib-equation}
    \end{equation}
    where 
    \begin{equation*}
        f_\HG(\mu) = \prod_{k\in \Kset} (1 - \mu)^{m_k(k-1) - n}(1 + \mu(k-1))^{m_k - n}\;,
    \end{equation*}
    and $\otimes$ is the Kronecker product.
\end{theorem}
```
This is Storm's `B` operator (`2204.13586:content/discussion.tex:7` — `we have employed the hypergraph nonbacktracking matrix $\bB$ proposed by~\citet{stormZetaFunctionHypergraph2006a}`) with a
size-graded Ihara–Bass reduction; no RH/Ramanujan statement (it is a data-science paper).

### C6b. Cubical complexes as hypergraphs

**arXiv:2002.12099** — title `2002.12099:main.tex:155`
`\title{Zeta functions of periodic cubical lattices and cyclotomic-like polynomials}`;
authors `:156` `\author{Yasuaki Hiraoka}`, `:164` `\author{Hiroyuki Ochiai}`,
`:170` `\author{Tomoyuki Shirai}`.

- `2002.12099:main.tex:1013-1016`
```
(2) A simplicial complex over a set $V$ can be viewed as a hypergraph by regarding 
 all simplices as $E$. \\
(3) For a $q$-dimensional cubical complex, let $V$ be the set of $(d-1)$-cubes and 
 $E$ the set of $d$-cubes. Then $H=(V,E)$ forms a hypergraph.
```
- `2002.12099:main.tex:994-995` — `The zeta functions of cubical complexes can be reformulated as those of` / `hypergraphs (see Definition~\ref{def:zetafn2}).  `
- Storm's theorem restated, `2002.12099:main.tex:1061-1074`
```
\begin{thm}[\cite{storm}]\label{thm:storm}
Let $H = (V,E)$ be a finite, connected hypergraph such that
 $\deg(v) \ge 2$ for all $v \in V$ with adjacency matrix $A$
 and diagonal degree matrix $D$ in $B_H$. 
Then, 
\[
 \zeta_{H}(u)
= (1-u)^{\chi(B_H)} \det(I - \sqrt{u} A + u Q)^{-1}, 
\]
 where $I$ is the $m \times m$ identity matrix with $m = |V|+|E|$,
 $Q = D-I$, 
$B_H$ is the bipartite graph associated with $H$, and 
$\chi(B_H) = |V|-|E|$ is the Euler characteristic of $B_H$. 
\end{thm}
```
This is the explicit statement that a general simplicial or cubical complex *does* get a
zeta — via the hypergraph/bipartite route only.

### C6c. Bartholdi zeta of a hypergraph

**arXiv:2510.27134** — title `2510.27134:honban2.tex:57`
`\title{A decomposition formula for the Bartholdi zeta function of a hypergraph covering}`;
author `:58` `\author{Kosei Watanabe}`. A determinant expression for the Bartholdi zeta of a
hypergraph is quoted there from Sato at `2510.27134:honban2.tex:516-518`. Recorded for
completeness (the task named "Bartholdi zeta hypergraph"); no Ramanujan/RH content.

---

## C7. The converse direction, and the "any complex" zeta of Kamber

### C7a. Kamber, "L_p-Expander Complexes"

**arXiv:1701.00154** — title `1701.00154:L_p_Expander_Complexes.tex:65`
`\title{$L_{p}$-Expander Complexes}`; author `:67` `\author{Amitay Kamber}`.

- abstract, `1701.00154:L_p_Expander_Complexes.tex:78-81`
```
We associate with any complex a natural ``zeta function'', generalizing
the Ihara-Hashimoto zeta function of a finite graph. We generalize
a well known theorem of Hashimoto, showing that a complex is Ramanujan
if and only if the zeta function satisfies the Riemann hypothesis.
```
- the operators, `1701.00154:L_p_Expander_Complexes.tex:334-343`
```
case, we can give a generalization of the non-backtracking operator.
As a preliminary, one can extend the Iwahori-Hecke algebra $H_{\phi}$
to an extended Iwahori-Hecke algebra $\hat{H}_{\phi}$, given by operators
$h_{w},w\in\hat{W}$, the extended Iwahori-Hecke algebra. The operators
of $\hat{H}_{\phi}$ act naturally on function on ``colored'' chambers
of $B$- $\mathbb{C}^{\hat{B}_{\phi}}=\mathbb{C}{}^{B_{\phi}\times\Omega}$.
Within $\hat{H}_{\phi}$ we have $n$ Bernstein-Luzstig operators
$h_{\beta_{1}},...,h_{\beta_{n}}$, corresponding to the simple coweights
$\beta_{1},...,\beta_{n}$ of the root system of $\hat{W}$. The one
dimensional case agrees with Hashimoto's non-backtracking operator.
```
- the zeta, `1701.00154:L_p_Expander_Complexes.tex:352-358`
```
\begin{defn}
Consider the $\hat{H}_{\phi}$-representation $L_{2}\left(\hat{B}_{\phi}\right)$.
Let
\[
\zeta_{\hat{B}_{\phi}}(u)=\frac{1}{\det(1-h_{\beta_{1}}u^{l(\beta_{1})})\cdot...\cdot\det(1-h_{\beta_{n}}u^{l(\beta_{n})})}
\]
\end{defn}
```
- the iff, `1701.00154:L_p_Expander_Complexes.tex:359-363`
```
\begin{cor}
The complex $X$ is an $L_{p}$-expander if and only if every pole
$\lambda$ of $\zeta_{\hat{B}_{\phi}}(u)$ satisfies $\left|\lambda\right|\le q^{(p-1)/p}$
or $\left|\lambda\right|=q$.
\end{cor}
```
- with `Ramanujan := L₂-expander`, `1701.00154:L_p_Expander_Complexes.tex:144`
`Call $X$ \emph{Ramanujan} if it is an $L_{2}$-expander.` and the identification with
Kang's notion, `:163-165` — `The definition is equivalent to` / `\emph{strongly-Ramanujan} in \cite{kang2016riemann} and \emph{flag-Ramanujan}` / `in \cite{first2016ramanujan}.`

> **Scope caveat.** "any complex" in the abstract means *any quotient of a building*: the
> definitions at `1701.00154:L_p_Expander_Complexes.tex:130-145` are for
> `X = Γ\B` with `B` an affine building. This is **not** a zeta for an arbitrary simplicial
> complex.

**Plain summary (C7a).** Kamber's zeta is the cleanest general-rank object: one
Bernstein–Lusztig operator `h_{β_i}` per simple coweight, and `ζ` is the reciprocal of the
product of the `n` determinants `det(1 − h_{β_i} u^{l(β_i)})`. For `n = 1` it is exactly
Hashimoto. And the RH ⇔ Ramanujan statement is an **iff**, supplying the converse that
LLP (C5) could not get, for buildings of general type.

### C7b. First, "The Ramanujan Property for Simplicial Complexes"

**arXiv:1605.02664** — title `1605.02664:ram_complexes_v32.tex:146`
`\title[The Ramanujan Property for Simplicial Complexes]{The Ramanujan Property for Simplicial Complexes}`;
author `:148` `\author{Uriya A.\ First$^*$}`. Cited by Kamber (`:154`, `:164-165`) as the
source of the "flag-Ramanujan" notion and of the fact that the LSV complexes are Ramanujan
in the stronger sense. Not further quoted here.

---

## C8. The only general-complex candidate: a combinatorial Ruelle zeta on a triangulation

**arXiv:2303.11226** — title `2303.11226:zeta_triangulations9.tex:89`
`\title[Triangulations and combinatorial zeta functions]{Combinatorial zeta functions counting triangles}`;
authors `:91` `\author{Leo Benard}`, `:95` `\author{Yann Chaubet}`,
`:99` `\author{Nguyen Viet Dang}`, `:103` `\author{Thomas Schick}`.

**Combinatorial geodesic in an arbitrary triangulation:**

- `2303.11226:zeta_triangulations9.tex:165-185`
```
\begin{definition}\label{def:geodesic}
  A \textit{combinatorial geodesic path} in the $n-1$ skeleton
  $\mathscr T^{(n-1)}$ of the triangulation $ \mathscr T$ is a finite sequence
  $c = (\sigma_1, \dots, \sigma_q)$ of adjacent $(n-1)$-simplices such that no
  pair $(\sigma_k, \sigma_{k+1})$ of consecutive simplices bound the same
  $n$-simplex. A combinatorial geodesic path $c = (\sigma_1, \dots, \sigma_q)$ is
  \textit{closed} if $\sigma_q$ is adjacent to $\sigma_1$ and
  $(\sigma_q, \sigma_1)$ do not bound the same simplex. A
  \textit{combinatorial closed
    geodesic} is an equivalence class of closed geodesic paths,
  % such that every cyclic permutation of $c$ is a geodesic path~; we will
  where we identify two closed geodesic paths if one is a cyclic permutation
  of the other. We denote by $\mathcal P$ the (in general infinite) set of
  primitive combinatorial closed geodesics, where a combinatorial closed
  geodesic is called primitive if it 
  is not a power of a shorter one. The length of a combinatorial closed geodesic
  $\gamma = [(\sigma_1, \dots, \sigma_q)]$ is denoted by $|\gamma| = q$ while
  $\varepsilon_\gamma \in \{-1, 1\}$ denotes its \textit{reversing index},
  which is the parity of how often orientations are flipped traversing the
  combinatorial closed geodesic and which is defined in Definition \ref{def:reversing_ind}.
\end{definition}
```
Note the geodicity condition is exactly LLP's (C5): consecutive `(n−1)`-simplices must not
bound the same `n`-simplex.

**Main theorem (Fried-type, but no Ramanujan):**

- `2303.11226:zeta_triangulations9.tex:192-205`
```
\begin{theorem}\label{theo:mainfried}
Assume that $M$ is a compact oriented manifold of dimension $n\geqslant 2$ with
triangulation $\mathscr T$. The combinatorial zeta function 
$$
\zeta_\mathscr T(z) = \prod_{\gamma\in \mathcal{P}}\left(1-\varepsilon_\gamma z^{|\gamma|}\right),
$$
%where the product 
converges for $|z|$ small enough. It is a polynomial function of degree $|\mathscr T^{(n-1)}|$ in $z$ and vanishes of order $b_1(M)$ at $z=(n+2)^{-1}$.
%The Euler characteristic of a closed surface $\Sigma$ is determined by the
%numbers $n_k$ of {primitive closed geodesics} in any triangulation of
%$\Sigma$.
Here, $|\mathscr T^{(n-1)}|$ denotes the cardinality of the $(n-1)-$skeleton
of the triangulation.
\end{theorem}
```

**The `L²` version, with Fuglede–Kadison determinant:**

- `2303.11226:zeta_triangulations9.tex:277-292`
```
\begin{theorem}
\label{theo:mainL2}
The combinatorial $L^2$-zeta function 
$$\zeta^{(2)}_{\wh{\mathscr{T}}}(z) = \prod_{\gamma\in {\wh{P}}}\left(1-\varepsilon_\gamma z^{|\gamma|}\right)
$$
%where the product 
converges for $|z|$ small enough, and it extends as a real analytic function
on the disk of diameter $(0, \frac{1}{n+2})$. Moreover,
$$
\zeta^{(2)}_{\wh{\mathscr T}}\left(\frac{1}{n+2}-z\right) = z^{b_1^{(2)}(M,\pi)} f(z) 
$$
with a function $f$ which is continuous at $0$.  If $\Delta_{n-1}^{(2)}$ is of
determinant class, then
\begin{equation*}
  f(0) =(n+2)^{2b_1^{(2)}(M,\pi)-|\mathscr T^{(n-1)}|} \cdot \detFK(\Delta_{n-1}^{(2)}).
\end{equation*}
```

**Their own comparison with Bass:**

- `2303.11226:zeta_triangulations9.tex:1909-1919`
```
Ihara zeta function as introduced and studied by Bass in \cite{Bass92}. On a
[...]
e.g.~\cite[Theorem 3.9]{Bass92}. On the other hand, there are also many
fundamental differences: Bass uses non-commutative determinants in the style
[...]
in more general situations. Bass deals with proper actions which are not
[...]
generalizations of Theorem \ref{theo:mainL2} when we have a simplicial action
```

**Plain summary (C8).** This is the closest thing to an Ihara zeta of a *general* finite
complex: on any triangulation of a compact oriented `n`-manifold, count primitive closed
geodesics in the `(n−1)`-skeleton (no two consecutive `(n−1)`-simplices in a common
`n`-simplex), weight each by a `±1` reversing index, and take the **direct** product
`∏(1 − ε_γ z^{|γ|})` (Selberg/Deitmar convention, no reciprocal). The result is a
*polynomial* of degree `|T^{(n−1)}|` whose vanishing order at the distinguished point
`z = (n+2)^{-1}` is `b₁(M)`, with an `L²`-version whose leading coefficient is a
Fuglede–Kadison determinant of the combinatorial Laplacian `Δ_{n−1}`. So: a determinant
identity (of torsion type, à la Fried, not of Bass–Ihara adjacency type), and **no**
Ramanujan notion and **no** RH — the distinguished point `(n+2)^{-1}` is not `q^{-1/2}`
and there is no spectral-gap statement.

---

## C9. Predecessors and variants (recorded, less central)

### C9a. Deitmar–Hoffman, "The Ihara–Selberg zeta function for PGL₃ and Hecke operators"

**arXiv:math/0407509** — title `math/0407509:main.tex:136`
`\title{The Ihara-Selberg zeta function for $\PGL_3$ and Hecke operators}`;
authors `:137` `\author{Anton Deitmar \& J. William Hoffman}`.

- `math/0407509:main.tex:173-188`
```
In \cite{padgeom} the author gave a definition of an Ihara-type zeta function $Z(u)$ for a higher rank group.
There is no Ihara-formula for higher rank up to date.
In this paper we give an approximation to an Ihara formula in the case of the group $\PGL_3$.
For this group the unramified Hecke-algebra has two generators $\pi_1,\pi_2$.
The canonical replacement of the determinant factor in Ihara's formula is
$$
\det(1-u\pi_1 +u^2 q \pi_2 -u^3 q^3).
$$
The main result of the present paper is

\begin{theorem}\label{main}
There are a natural number $n$ and a polynomial $P(u)$ such that
$$
Z(u)\= \frac{\det(1-u\pi_1+ u^2 q \pi_2 -u^3 q^3)^n}{P(u)}.
$$             
\end{theorem}
```
- zeta definition (note: **no reciprocal**, and rank-one geodesics only),
`math/0407509:main.tex:277-281`
```
We define the \emph{zeta function}
$$
Z(u)\=\prod_c\left( 1-u^{l(c)} \right)
$$
as a formal power series at first, where $c$ ranges over the set of all primitive rank-one closed geodesics in $\Ga\bs X$ modulo homotopy and modulo change of orientation.
```
- the two auxiliary zetas, `math/0407509:main.tex:396-399`
```
\begin{proposition}\label{2.3}
For the zeta function $Z$ we have $\ds Z(u)=\frac{Z_1(u)}{Z_2(u)}$. 
Moreover, if $\Ga$ is regular, then $Z_2(u)=1$.
\end{proposition}
```
- Hashimoto form, `math/0407509:main.tex:447-448` — `\begin{theorem}` / `We have $Z_1(u)=\det(1-uT)$. In particular, $Z_1(u)$ is a polynomial of degree equal to the number of edges of $\Ga\bs X$, or, equivalently,`
- the weak identity, `math/0407509:main.tex:654-659`
```
\begin{theorem}\label{3.5}
There is $m\in\N$ and a polynomial $Q(u)$ such that
$$
Z_1(u)\=\frac{\det(1-u\pi_1+u^2 q\pi_2-u^3q^3)^m}{Q(u)}.
$$
\end{theorem}
```
- gallery zeta, `math/0407509:main.tex:729-735`
```
\begin{proposition}\label{gall}
We have
$$
Z_2(u)\= \det(1-u^3 L).
$$
In particular, $Z_2(u)$ is a polynomial of degree at most $3$ times the number of chambers of $\Ga\bs X$.
\end{proposition}
```

**Plain summary (C9a).** This is the historical first step and is explicitly *weak*: the
cubic Hecke determinant is identified as "the canonical replacement", and the theorem only
says `Z` is that determinant to an **unspecified power `n`** over an **unspecified**
polynomial `P(u)`. Kang–Li/Kang–Li–Wang later pinned both down (`n = 1`, `P = det(I+L_Bu)`
up to the `(1−u³)^χ` factor and the correct geodesic types). Note the convention here is
the Selberg one, `∏(1 − u^l)`, so the Hecke determinant sits in the **numerator**.

### C9b. Deitmar–Kang, "Geometric zeta functions for higher rank p-adic groups"

**arXiv:1303.6848** — title `1303.6848:main.tex:124`
`\title{Geometric zeta functions for higher rank $p$-adic groups\\ \ \\ \small`;
authors `:126` `\author{Anton Deitmar \& Ming-Hsuan Kang\thanks{...`.

- the sign convention, argued, `1303.6848:main.tex:793-805`
```
\begin{definition}
Let 
$$
Z_{1,+}(u)=\prod_{c}\(1-u^{l(c)}\),
$$
where the product is extended over all closed integral positive primitive geodesics in $\Ga\bs\CB$.
Here a closed geodesic $c$ is called \e{primitive}, if it is not a power of a shorter one.
Note that $l(c)$ here denotes the length of the closed geodesic $c$.
\end{definition}

The reader may note, that this definition differs from Ihara's and others in that we consider the Euler factors with a positive exponent while other authors would prefer $1/Z_{1,+}(u)$ instead.
```
with the deeper reason given at `1303.6848:main.tex:805` — `There is a deep reason for the sign in Selberg's paper, which is explained in \cite{Geom1}: It emerges that the exponent prescribed by the trace formula is an Euler number, in Selberg's original case the Euler number of a point, but generally the Euler number of a locally sym`
(**directly relevant to the notebook's graded/supertrace reading**: the exponent *is* an
Euler number, which is why it can be negative).

- the Ruelle-type identity, `1303.6848:main.tex:870-876`
```
\begin{theorem}\label{thm4.4}
After replacing the group $\Ga$ with a finite index subgroup, we have the identity of rational functions,
$$
\frac{Z_{2,+}(-u)}{Z_{1,+}(u^2)}=\exp\(- \int_0^u  S_{\Ga,P_1}(z)\,dz\).
$$
Or, otherwise stated, $S_{\Ga,P_1}(u)=\frac{F'}F(u)$, where $F(u)=\frac{Z_{1,+}(u^2)}{Z_{2,+}(u)}$.
\end{theorem}
```
- the RH section, `1303.6848:main.tex:953-962`
```
\section{Riemann Hypothesis}
The complex $\CB_\Gamma = \Gamma \backslash \CB$ is called \emph{Ramanujan} if all irreducible unramified infinite dimensional subrepresentations of $L^2(\Gamma \backslash G)$ are tempered. See \cite{Li} and \cite{LSV} for details. When $G=\PGL_2(F)$, $\CB_\Gamma$ is a finite
It was first pointed out by \cite{Sunada} that the non-trivial poles of Ihara zeta function $Z(\CB_\Gamma,u)$  of $\CB_\Gamma$ have absolute values equal to $q^{-1/2}$ if and only if $\CB_\Gamma$ is a Ramanujan graph. The first condition is called the Riemann hypothesis of $Z
```
- `1303.6848:main.tex:958-962`
```
We shall give an analogue of the above statement for $G=\PGL_3(F)$.
Recall that $Z_{1,+}(u)$ and  $Z_{2,+}(u)$ are polynomials so that $ Z_{1,+}(u)=\det(I-L_E u)$ for some parahoric Hecke operator $L_E$; $ Z_{2,+}(u)=\det(I-L_B u)$ for some Iwahori Hecke operator $L_B$ \cite{KLW}. Given a smooth unramified representation $V$ of $G$, consider 
$$ Q(V,u)=\frac{\det(I+ L_B u)}{\det(I-L_E u^2)}$$
where the determinant is taken over the spaces of parahoric and Iwahori fixed vectors of $V$ respectively. Then we have 
$$ \frac{Z_{2,+}( -u)}{Z_{1,+}(u^2)} = \prod_{V} Q(V,u)^{m_V}$$
```
- the RH theorem and its Ramanujan corollary, `1303.6848:main.tex:982-994`
```
\begin{theorem}
With the above notation we have
$$
\frac{Z_{2,+}( -u)}{Z_{1,+}(u^2)} = \frac{(1-u^3)^{\chi-1}P_1(u)}{(1-q^3u^3)P_2(u)}
$$ 
where $P_1(u)=\prod_\alpha (1-\alpha u)$ and $P_2(u)=\prod_\beta (1-\beta u)$ with $|\alpha|=|\beta|=q^{1/2}$.
\end{theorem}


\begin{corollary}
When $\CB_\Gamma$ is a Ramanujan complex, then 
$$ \frac{Z_{2,+}( -u)}{Z_{1,+}(u^2)}= (1-u^3)^{\chi(X_\Gamma)} \frac{P_1(u)}{(1-u^3)(1-q^3u^3)},$$ where $P_1(u)=\prod_\alpha (1-\alpha u)$ with $|\alpha|=q^{1/2}$ of degree $N_1-3N_0+6$. Here $N_i$ is the number of $i$-simplex in $\CB_\Gamma$. In this case, we say the complex zeta functions of $\CB_\Gamma$ satisfy the Riemann hypothesis.
```
Note the **`χ − 1`** exponent in the theorem (not `χ`), and the degree
`N₁ − 3N₀ + 6` of the "critical-line" polynomial `P₁`.

### C9c. Hong–Kwon: the non-cocompact (non-uniform) case, weighted complexes

**arXiv:2411.15489** — title `2411.15489:main.tex:304`
`\title[Edge zeta function of $\operatorname{PGL}_3$]{Edge zeta function and closed  cycles in the standard non-uniform complex from $\operatorname{PGL}_3$}`;
authors `:305` `\author{Soonki Hong}`, `:308` `\author{Sanghoon Kwon}`.
Companion: **arXiv:2512.23276** — title
`2512.23276:Chamber_Zeta_Submitted_260116.tex:311`
`\title[Chamber zeta function of $\operatorname{PGL}_3$]{Chamber zeta function and closed galleries in the standard non-uniform complex from $\operatorname{P`;
same authors (`:312`, `:315`).

- the state-of-the-art statement, `2411.15489:main.tex:354`
```
In this paper, we investigate a non-compact higher rank case. One problem in higher rank is the lack of a unified zeta function, as in higher dimensional buildings there are several possibilities to generalize Ihara's approach. We take geometric approach and investigate the edge zeta function of a non-cocompact arithmetic lattice of $\operatorname{PGL}_3$.
```
(written before Kang–Yu 2607.21262 supplied the unified version).
- they do extend the definition to **weighted** complexes,
`2411.15489:main.tex:944` — `In this section, we begin by reviewing the definition of zeta functions for simplicial complexes, paying particular attention to the extension of these functions to the weighted complexes. After we introduce the notion of weighted complexes, we define the edge zeta function for those and express it in terms of a determinant, analogous to the Bass-Ihara formula. We also establish the convergence properties of the zeta function for $\operatorname{PGL}(3,\mathbb{F}_q[t])\backslash\mathcal{B}$.`

---

## C10. Lubotzky–Samuels–Vishne: the Ramanujan complexes themselves

### C10a. "Ramanujan Complexes of Type Ã_d" (Israel J. Math. 149 (2005) 267–299)

**arXiv:math/0406208** — title `math/0406208:main.tex:432-434`
```
\title
%
{Ramanujan Complexes of Type $\tilde{A_d}$}
```
authors `:448` `\author{Alexander Lubotzky}`, `:452` `\author{Beth Samuels}`,
`:458` `\author{Uzi Vishne }`.

**The Hecke (coloured adjacency) operators `A_k`:**

- `math/0406208:main.tex:541-549`
```
The vertices $\B^0$ of the building are labelled by a `color'
function $\color \co \B^0 \ra \Z/d\Z$, and we may look at the
$d-1$ colored adjacency operators $A_k$, $k = 1,\dots,d-1$ on
$\L2{\B^0}$, called the Hecke operators. They are defined by
\begin{equation}\label{Akdef}
(A_kf)(x) = \sum{f(y)}
\end{equation}
where the summation is over the neighbors $y$ of $x$ such that
$\color(y)-\color(x) = k$ in $\Z/d\Z$.
```

**Ramanujan complex, definition (joint spectrum):**

- `math/0406208:main.tex:564-572`
```
\begin{defn} [{following \cite{CSZ}}]
A finite quotient $X$ of $\B$ is called a Ramanujan complex if the
eigenvalues of every non-trivial simultanenous eigenvector $v \in
\L2{X}$, $A_k v = \lam_k v$, satisfy $(\lam_1,\dots,\lam_{d-1})
\in \Aspec_d$.
%
%
%
\end{defn}
```
(restated at `math/0406208:main.tex:1391-1396`). The crucial point, stressed at
`:553-558`, is that `Aspec_d ⊂ C^{d-1}` is the **joint** spectrum and is strictly smaller
than the product of the individual spectra.

### C10b. "Explicit constructions of Ramanujan Complexes" (Eur. J. Comb. 26 (2005) 965–993)

**arXiv:math/0406217** — title `math/0406217:main.tex:416-418`
```
\title
[Explicit constructions of Ramanujan Complexes] {Explicit
constructions of Ramanujan Complexes}
```
authors `:432` `\author{Alexander Lubotzky}`, `:436` `\author{Beth Samuels}`,
`:442` `\author{Uzi Vishne }`.

**The Cayley-complex theorem (the generating set):**

- `math/0406217:main.tex:497-515`
```
Let $\binomq{d}{k}{q}$ denote the number of subspaces of dimension $k$
of $\F_q^d$.
\begin{thm}\label{mainIntro}
Let $q$ be a prime power, $d \geq 2$, $e \geq 1$ ($e > 1$ if $q =
2$).

Then, the group $G = \PGL[d](\F_{q^e})$ has an (explicit) set $S$
of $\binomq{d}{1}{q} + \binomq{d}{2}{q} + \cdots +
\binomq{d}{d-1}{q}$ generators, such that the Cayley complex of
$G$ with respect to $S$ is a Ramanujan complex, covered by
$\B_d(F)$, when $F = \F_q\db{y}$.
\end{thm}
The Cayley complex of $G$ with respect to a set of generators $S$
is the simplicial complex whose $1$-skeleton is the Cayley graph
$\Cayley{G}{S}$, where a subset of $i+1$ vertices is an $i$-cell
iff every two vertices comprise an edge.
%
The generators in \Tref{mainIntro} are explicitly given in Section
\ref{sec:explicit}.
```

**The generators of Γ, concretely** (this is what a numerical construction needs):

- `math/0406217:main.tex:1407-1415`
```
By definition, $\Gamma$ is generated by the elements $b_u =
u(1-z^{-1})u^{-1}$ of $G'(R)$, where $u$ ranges over
$\mul{\F_{q^d}}/\mul{\F_{q}}$.

%
Since $b_u = 1 - \frac{u}{\phi(u)}z^{-1}$, for every $u$, there is
a unique $r \in \mul{\F_{q^d}}$ with $\Norm(r)=1$, such that $b_u
= b_{(r)} = 1 - rz^{-1}$, where $\Norm =\Norm_{\F_{q^d}/\F_q}$ is
the norm map.
```
- the relations (a presentation of Γ), `math/0406217:main.tex:1455-1460`
```
\begin{thm}\label{presGamma}
Let $\Gamma'$ be the abstract group generated by $\set{x_u
\suchthat u \in \mul{\F_{q^d}}/\mul{\F_{q}}}$, with the relations
$x_{u'} x_{u} = x_{v'} x_{v}$ whenever $b_{u'} b_{u} = b_{v'}
b_{v}$ in $\Gamma$, and a single relation $x_{u_1} \ldots x_{u_d}
= 1$ for some $u_1,\dots,u_d$ such that
```
with the pairing relation displayed at `math/0406217:main.tex:1416-1422`
```
\begin{rem}\label{uvprime}
For every $u\neq v \in \mul{\F_{q^d}}/\mul{\F_{q}}$ there are unique
$u',v' \in \mul{\F_{q^d}}/\mul{\F_{q}}$ such that
\begin{equation}\label{pairs}
b_{u} b_{u'} = b_{v} b_{v'}.
\end{equation}
\end{rem}
```
and the explicit solution at `math/0406217:main.tex:1431-1438` — `Computationally, assume first $d > 2$. Since` / `$(1-rz^{-1})(1-r'z^{-1}) = 1 - (r+r')z^{-1} +` / `r\phi^{-1}(r')z^{-2}$, $b_{(r)}b_{(r')} = b_{(s)}b_{(s')}$ in` / `$\Gamma$ iff` / `$$r+r' = s+s'\quad\,\mbox{and}\quad\, r\phi^{-1}(r') = s\phi^{-1}(s').$$` / `The unique solution is $r' = \frac{s-r}{\phi s -\phi r} \phi(s)$` / `and $s' = \frac{s-r}{\phi s -\phi r} \phi(r)$, where $r'$ and $s'`.

**The Hecke operators on the quotient, and the clique-complex structure:**

- `math/0406217:main.tex:676-682`
```
The colors provide us with $d$ Hecke operators, defined on
functions of $\B^0$ by summation over the neighbors of fixed
color-shift:
$$A_kf(x) = \sum_{y\sim x,\, \color(y)-\color(x)\equiv k} f(y).$$
These operators generate the Hecke
algebra $\He[\PGL(F)]{\PGL(\O)}$ (see \cite[Sec.~2]{paperI} for
more details).
```
- `math/0406217:main.tex:1673-1686`
```
The generators $\set{b_u}$ correspond to the neighbors of color
$1$ of $[L_0]$. More generally, by \Cref{actk}
the neighbors of color $k$ correspond to the products $b_{u_1}
\ldots b_{u_k}$ which are headers of a product of $d$ generators
which equals $1$. The $1$-skeleton of $\B_I$ is thus the Cayley
graph of $\Gamma/\Gamma(I)$ with respect to these generators (for
$k = 1,\dots,d-1$), and there are `partial Laplacian operators'
$A_k$ of $\Gamma/\Gamma(I)$, induced from the Hecke operators of
$\B$. Frequently, these are the colored Laplacian operators (\ie\
they can be defined for $\Gamma/\Gamma(I)$ directly); we address
this issue towards the end of this section. The higher dimensional
cells of $\Gamma/\Gamma(I)$ are then defined to make it a clique
complex. Thus, $\dc{\Gamma(I)}{G(F)}{K}$ and $\Gamma/\Gamma(I)$
become isomorphic complexes.
```
- the main theorem, `math/0406217:main.tex:1719-1724`
```
\begin{thm}\label{main}
For every $d\geq 2$ and every $0 \neq I \normali R$,
the Cayley complex of $\Gamma / \Gamma(I)$
%
is a Ramanujan complex.
\end{thm}
```

**Plain summary (C10).** The `Ã_{d−1}` Ramanujan complexes are Cayley complexes: take the
Cartwright–Steger lattice `Γ ⊂ PGL_d(F_q((1/y)))` acting simply transitively on the
vertices of the building, generated by `b_u = 1 − r z^{-1}` with `r ∈ F_{q^d}^×` of norm 1
(one generator per `u ∈ F_{q^d}^×/F_q^×`, i.e. `(q^d − 1)/(q − 1) = [d,1]_q` of them);
the quotient by a congruence subgroup is `PGL_d(F_{q^e})` (or a subgroup), the 1-skeleton
is its Cayley graph on the colour-`k` products `b_{u_1}…b_{u_k}` (so `S` has
`Σ_k [d,k]_q` elements), and the complex is the clique complex. The Hecke operators are
the colour-shift adjacency sums `A_k`. **No zeta function is defined in these two papers.**

### C10a′. Lubotzky's ICM survey, on the zeta programme

**arXiv:1712.02526** — title `1712.02526:main.tex:219`
`\title[High Dimensional Expanders]{High Dimensional Expanders}`;
author `:220` `\author[A. Lubotzky]{Alexander Lubotzky}`.

- `1712.02526:main.tex:488`
```
\begin{definition} In the notation above, $\Ga\setminus\calb$ is called a Ramanujan complex if every infinite dimensional irreducible $I$-spherical $G$-subrepresentation  of $L^2(\Ga\setminus G)$ is tempered.
```
- `1712.02526:main.tex:497`
```
Ramanujan graphs can be characterized as those graphs whose associated zeta functions satisfy ``the Riemann Hypothesis (RH)" - see \cite{Lub94},  for an exact formulation and references.  An interesting direction of research is to try to associate to high dimensional complexes suitable ``zeta functions" with the hope that also in this context the Ramanujaness of the complex can be expressed via the RH.  For this direction or research - see \cite{Sto06}, \cite{KaLi14}, \cite{DK14}, \cite{KLW10}, \cite{Kan16}, \cite{Kam17b} and \cite{LLP17}.
```
Read carefully: as of the 2018 ICM this was still phrased as **"an interesting direction of
research ... with the hope that"**, i.e. a programme, not a theorem — and the references
`[Sto06] [KaLi14] [DK14] [KLW10] [Kan16] [Kam17b] [LLP17]` are exactly C6, C1a, C9b, C1b,
the JNT-2016 paper, C7a, C5 above.

---

## Not found

1. **Kang, "Riemann Hypothesis and strongly Ramanujan complexes from GL_n",
   J. Number Theory 161 (2016) 281–297, doi `10.1016/j.jnt.2015.09.002`** — **not on
   arXiv**. Searched: the arXiv API (`au:"Ming-Hsuan Kang"`, `all:"strongly Ramanujan"` —
   both rate-limited/empty), two WebSearch passes, and the author's own publication list at
   `math.nycu.edu.tw` (which lists it as item 10, "forthcoming in Journal of Number
   Theory", with **no arXiv number**, while listing arXiv-posted items alongside).
   Its content is reachable second-hand and byte-cited above: the scope (`Ã_n` buildings,
   pole locations by representation type) at `1702.05452:rw_ramanujan_complex.tex:1428-1432`;
   the equivalence of "strongly Ramanujan" with Kamber's `L₂`-expander at
   `1701.00154:L_p_Expander_Complexes.tex:163-165`; the open converse question it posed at
   `1702.05452:rw_ramanujan_complex.tex:421-425`. **Nothing from it is quoted verbatim in
   this note.**

2. **An Ihara-type zeta for a general finite simplicial or cell complex, with a Bass
   identity and an RH ⇔ Ramanujan theorem — does not exist.** Searches run, all returning
   nothing of the sought kind: *"zeta function of a simplicial complex"*, *"non-backtracking
   operator simplicial complex"*, *"Ihara zeta cell complex"*, *"zeta function higher-
   dimensional Hashimoto"*, *"zeta function of a 2-complex"*, *"Ihara zeta general finite
   CW complex"*. What came back was, in every case, one of: (a) building quotients
   (C1–C5, C7, C9); (b) hypergraph zetas that reduce to a bipartite-graph Ihara zeta (C6,
   C6a, C6b); (c) graph-only refinements (weighted Ihara, edge reconstruction, directed
   non-backtracking); (d) the combinatorial Ruelle/torsion zeta of C8, which has no
   Ramanujan notion. The papers themselves say so: `math/0407509:main.tex:174` — `There is
   no Ihara-formula for higher rank up to date.` (2004); `2411.15489:main.tex:354` — `One
   problem in higher rank is the lack of a unified zeta function, as in higher dimensional
   buildings there are several possibilities to generalize Ihara's approach.` (2024);
   `1712.02526:main.tex:497` — still a "hope" in 2018; and `2607.21262:main.tex:249-250` —
   `To our knowledge, it is the first Ihara-type identity uniform in \(n\) for` / `this
   family.` (2026, and even that is only for PGLₙ buildings).

3. **"Bartholdi zeta simplicial complex"** — nothing. The Bartholdi generalisation exists
   for graphs and for hypergraphs only (C6c, and Sato's determinant expression quoted
   inside it); the only "complex" reachable is via the hypergraph reduction of C6b.

4. **"Ruelle zeta simplicial complex geodesic"** — returns only C8 (2303.11226) and the
   smooth-manifold Ruelle-zeta literature already covered in
   `notes/extract/selberg-sources.md` (1306.4203, 1403.0256, 1606.04560) and by the second
   worker (1807.01189, 2009.08558).

5. **Not on arXiv, therefore only named, not quoted:** K. Hashimoto, *Zeta functions of
   finite graphs and representations of p-adic groups*, Adv. Stud. Pure Math. 15 (1989)
   211–280 (the origin of the non-backtracking operator and of the bipartite factorisation
   used by Storm); H. Bass, *The Ihara–Selberg zeta function of a tree lattice*, Internat.
   J. Math. 3 (1992) 717–797 (cited as `0804.2305:main.tex:3079-3081`); Y. Ihara,
   *On discrete subgroups of the two by two projective linear group over p-adic fields*,
   J. Math. Soc. Japan 18 (1966) 219–235; W.-C. W. Li, *Ramanujan hypergraphs*, GAFA 14
   (2004) 380–399 (cited as `0804.2305:main.tex:3141`); Cartwright–Solé–Żuk, and
   Cartwright–Steger (the lattice `Γ` of C10b).

---

## Proposed rows for `db/provenance.tsv`

(Not written to `db/`; paste as-is. Columns: `id | key | file | lines | quote | used_by`.)

```tsv
prov:kl14-zeta-def	0804.2305	main.tex	215-220	The zeta function of $X_\G$ is defined as $$ Z(X_\G,u) = \prod_{[C]} (1 - u^{l_A([C])})^{-1},$$ \noindent where $[C]$ runs through the equivalence classes of tailless primitive closed geodesics consisting of edges of the same type, and $l_A([C])$ is the algebraic length of any geodesic in $[C]$.	C1
prov:kl14-main	0804.2305	main.tex	236-239	\begin{eqnarray}\label{zeta} Z(X_\G, u) = \frac{(1-u^3)^{\chi(X_\G)}}{\det(I-A_1u+qA_2u^2-q^3 u^3I)\det(I + L_Bu)}, \end{eqnarray}	C1
prov:kl14-hashimoto	0804.2305	main.tex	247-248	$$ Z(X_\G, u) = \frac{1}{\det(I - L_E u) \det(I - (L_E)^t u^2)} = \frac{1}{\det(I - L_E u) \det(I - L_E u^2)},$$	C1
prov:kl14-operator-identity	0804.2305	main.tex	257-260	\begin{eqnarray}\label{zetaidentity} \frac{(1-u^3)^{\chi(X_\G)}}{\det(I-A_1u+qA_2u^2-q^3 u^3I)} = \frac{\det(I + L_Bu)}{\det(I - L_E u) \det(I - (L_E)^t u^2)}, \end{eqnarray}	C1
prov:kl14-rh-ramanujan	0804.2305	main.tex	285-295	\begin{theorem}[\cite{KLW}, Theorem 2] The following four statements on $X_\G$ are equivalent. (1) $X_\G$ is a Ramanujan complex; (2) The nontrivial zeros of $\det(I-A_1u+qA_2u^2-q^3 u^3I)$ have absolute value $q^{-1}$; (3) The nontrivial zeros of $\det(I + L_Bu)$ have absolute values $1$, $q^{-1/2}$ and $q^{-1/4}$; and (4) The nontrivial zeros of $\det(I - L_E u)$ have absolute values $q^{-1}$ and $q^{-1/2}$. \end{theorem}	C1
prov:klw10-operators	0809.1401v1	main.tex	342-368	We recall the definition of the operators $L_B$, $L_E$, $A_1$, $A_2$ from \cite{KL}. ... $$L_B f(gB)=\sum_{w_iB \in B{t_2\sigma^2}B/B} f(gw_iB).$$ ... $$L_E f(gE)=\sum_{w'_jE \in E(t_2\sigma^2)^2E/E} f(gw'_jE).$$ ... $$A_1 f(gK)=\sum_{i} f(gg_iK),$$ $$A_2 f(gK)=\sum_{j} f(gg'_j K),$$	C1
prov:klw10-identity	0809.1401v1	main.tex	1414-1416	$$(1-u^3)^{\chi(X_\Gamma)} = \frac{{\det(I-A_1u+qA_2u^2-q^3 u^3I)}{\det(I + L_Bu)}}{\det(I - L_E u) \det(I - (L_E)^t u^2)}. $$	C1
prov:kangyu26-main	2607.21262	main.tex	2019-2023	\[ (1-u^n)^{\chi(\X)}\,L(\Gamma,q^{(n-1)/2}u) = \prod_{k=1}^{n-1}Z_k^\epsilon(\X,u)^{(-1)^{k+1}}, \]	C2
prov:kangyu26-zetadet	2607.21262	main.tex	2304-2312	\begin{theorem}\label{thm:zeta-determinant} For \(1\le k\le n-1\), with \(T_k=T_k(u)\) acting on \(C_k(\X)\), the zeta functions are given by the rational functions \[ Z_k(\X,u)=\det(I-T_k)^{-1}, \qquad Z_k^\epsilon(\X,u)=\det\!\left(I-(-1)^{k+1}T_k\right)^{-1}. \] \end{theorem}	C2
prov:kangyu26-twist	2607.21262	main.tex	1971-1981	For a closed \(k\)-geodesic \(\scrC\), define \[ \epsilon(\scrC):=(-1)^{(k+1)l_G(\scrC)}. \] We also define the \(\epsilon\)-twisted \(k\)-th geodesic zeta function by \[ Z_k^\epsilon(\X,u) = \prod_{[\scrC]} \left(1-\epsilon(\scrC)u^{l_A(\scrC)}\right)^{-1}. \]	C2
prov:klw18-buildingA2	1505.00902	Zeta-and-Lfunction-20170426.tex	1155-1161	\begin{theorem}\label{buildingA2} With $G=$PGL$_3$, the following identity for the finite quotient $\B_\Ga$ holds: \begin{eqnarray}\label{A2-building} (1-u^3)^{\chi(\B_\Ga)}L(\Ga \bs G(F), \pi_1, qu) = \frac{Z(\B_\Ga, \pi_1, u) Z(\B_\Ga, \pi_2, u^2)}{Z_2(\B_\Ga, \pi_1, -u)}, \end{eqnarray} where $\chi(\B_\Ga)$ denotes the Euler characteristic of $\B_\Ga$. \end{theorem}	C3
prov:klw18-chi	1505.00902	Zeta-and-Lfunction-20170426.tex	1163-1166	Let $N_0, N_1$, and $N_2$ denote the number of vertices, edges, and chambers in $\B_\Ga$, respectively. Then $N_1=(q^2+q+1)N_0$ and $N_2= \frac{1}{3}(q+1)(q^2+q+1)N_0$ so that the Euler characteristic $$\chi(\B_{\Ga})=N_0-N_1+N_2=\frac{1}{3}(q-1)^2(q+1)N_0.$$	C3
prov:flw13-main	1109.3854	zetagsp4-final.tex	129-135	\begin{equation}\label{GSp4zeta} \begin{aligned} Z(X_\Gamma, u) &= \frac{(1-u^2)^{\chi(X_{\Gamma})}(1-q^2 u^2)^{2N_p-N_{ns}}}{\det(I-A_1 u+qA_2 u^2-q^3 A_1 u^3+q^6I u^4)\det(I-L_I u)}\\ &= \frac{1}{\det(I-L_{P_1} u)\det(I-L_{P_2}u^2)}, \end{aligned} \end{equation}	C4
prov:flw13-rh	1109.3854	zetagsp4-final.tex	145-157	\begin{theorem} The following statements are equivalent: $(1)$ $X_{\Gamma}$ is Ramanujan. $(2)$ All the nontrivial zeros of $\det(I-A_{1}u+qA_{2}u^{2}-q^{3}A_{1}u^{3}+q^{6}Iu^{4})$ have absolute value $q^{-\frac{3}{2}}$. $(3)$ All the nontrivial zeros of $\det(I - L_{P_{1}} u)$ have absolute values $q^{-\frac{3}{2}}$ or $q^{-1}$. $(4)$ All the nontrivial zeros of $\det(I - L_{P_{2}} u)$ have absolute values $q^{\alpha}$, where $-2 \le \alpha \le -1$. $(5)$ All the nontrivial zeros of $\det(I - L_{I} u)$ have absolute values $1$ or $q^{\beta}$, where $-1 \le \beta \le -\frac{1}{2}$. \end{theorem}	C4
prov:llp17-geodesic-flow	1702.05452	rw_ramanujan_complex.tex	1009-1019	\begin{definition}\label{def:geodesic-flow} The geodesic flow $T$ on $UT^{j}\mathcal{B}$ is defined as follows: $T(\sigma)$ for $\sigma=\left(v_{0},\left\{ v_{0},\ldots,v_{j}\right\} \right)\in UT^{j}\mathcal{B}$, with $\col\left(v_{i}\right)\equiv\col\left(v_{0}\right)+i$, consists of all the cells $\sigma'=\left(v_{1},\left\{ v_{1},\ldots,v_{j},w\right\} \right)\in UT^{j}\mathcal{B}$ such that \begin{enumerate} \item $\col\left(w\right)\equiv\col\left(v_{1}\right)+j$ (the ``direction vector'' is based at $v_{1}$), \item $\{v_{0},v_{1},\ldots,v_{j},w\}$ is not a cell (geodicity). \end{enumerate} \end{definition}	C5
prov:llp17-ram-digraph-def	1702.05452	rw_ramanujan_complex.tex	333-336	\begin{equation}\begin{tabular}{l}every eigenvalue $\lambda\in\C$ of the adjacency matrix \\ of $\cY$ satisfies either $\left|\lambda\right|\leq\sqrt{k}$ or $\left|\lambda\right|=k$\end{tabular}\,.\label{eq:ram-digrap-def} \end{equation}	C5
prov:llp17-rh	1702.05452	rw_ramanujan_complex.tex	410-416	\begin{maincoro} \label{cor:R-H-for-Ramanujan} Let $X$ be a Ramanujan complex as in~\eqref{eq:ram-def}, and let $Z_{\cY_{T,\fX}}(u)$ be the zeta function associated with a $G$-equivariant, collision-free, $k$-regular branching operator $T$ on $\cB=\mathcal{B}\left(G\right)$. Then $Z_{\cY_{T,\fX}}(u)$ satisfies the Riemann Hypothesis; that is, if $Z_{\cY_{T,\fX}}\left(u\right)$ has a pole at $k^{-s}$ then $|s|=1$ or $\Re\left(s\right)\leq\frac{1}{2}$. \end{maincoro}	C5
prov:storm06-zeta	math/0608761	Ihara-SelbergofHypergraph.tex	173-174	For $u \in \IC$ with $|u|$ sufficiently small, we define the \emph{generalized Ihara-Selberg zeta function} of a finite hypergraph $\hyperH$ by \[\zeta_\hyperH(u) = \prod_{\mathfrak{p} \in P}\left(1 - u^{|\mathfrak{p}|}\right)^{-1},\]	C6
prov:storm06-bipartite	math/0608761	Ihara-SelbergofHypergraph.tex	430	\[ \zeta_\hyperH(u) = Z_{B_\hyperH}(\sqrt{u}).\]	C6
prov:storm06-bass	math/0608761	Ihara-SelbergofHypergraph.tex	463	\[\zeta_\hyperH(u) = Z_{B_\hyperH}(\sqrt{u}) = (1 - u)^{\chi(B_\hyperH)} \det(I - \sqrt{u}A_{B_\hyperH} + uQ_{B_\hyperH})^{-1},\]	C6
prov:storm06-rh	math/0608761	Ihara-SelbergofHypergraph.tex	627-630	\begin{Thm} For a $(d, r)$-regular hypergraph $\hyperH$, $\zeta_\hyperH(q^{-s})$ satisfies the modified hypergraph Riemann hypothesis if and only if $\hyperH$ is a Ramanujan hypergraph. \label{Thm:RamanujanEquivalence} \end{Thm}	C6
prov:kamber17-zeta	1701.00154	L_p_Expander_Complexes.tex	352-358	\begin{defn} Consider the $\hat{H}_{\phi}$-representation $L_{2}\left(\hat{B}_{\phi}\right)$. Let \[ \zeta_{\hat{B}_{\phi}}(u)=\frac{1}{\det(1-h_{\beta_{1}}u^{l(\beta_{1})})\cdot...\cdot\det(1-h_{\beta_{n}}u^{l(\beta_{n})})} \] \end{defn}	C7
prov:kamber17-iff	1701.00154	L_p_Expander_Complexes.tex	359-363	\begin{cor} The complex $X$ is an $L_{p}$-expander if and only if every pole $\lambda$ of $\zeta_{\hat{B}_{\phi}}(u)$ satisfies $\left|\lambda\right|\le q^{(p-1)/p}$ or $\left|\lambda\right|=q$. \end{cor}	C7
prov:bcds23-def	2303.11226	zeta_triangulations9.tex	165-185	\begin{definition}\label{def:geodesic} A \textit{combinatorial geodesic path} in the $n-1$ skeleton $\mathscr T^{(n-1)}$ of the triangulation $ \mathscr T$ is a finite sequence $c = (\sigma_1, \dots, \sigma_q)$ of adjacent $(n-1)$-simplices such that no pair $(\sigma_k, \sigma_{k+1})$ of consecutive simplices bound the same $n$-simplex. ... \end{definition}	C8
prov:bcds23-fried	2303.11226	zeta_triangulations9.tex	192-205	\begin{theorem}\label{theo:mainfried} Assume that $M$ is a compact oriented manifold of dimension $n\geqslant 2$ with triangulation $\mathscr T$. The combinatorial zeta function $$ \zeta_\mathscr T(z) = \prod_{\gamma\in \mathcal{P}}\left(1-\varepsilon_\gamma z^{|\gamma|}\right), $$ converges for $|z|$ small enough. It is a polynomial function of degree $|\mathscr T^{(n-1)}|$ in $z$ and vanishes of order $b_1(M)$ at $z=(n+2)^{-1}$. \end{theorem}	C8
prov:dh06-weak	math/0407509	main.tex	183-188	\begin{theorem}\label{main} There are a natural number $n$ and a polynomial $P(u)$ such that $$ Z(u)\= \frac{\det(1-u\pi_1+ u^2 q \pi_2 -u^3 q^3)^n}{P(u)}. $$ \end{theorem}	C9
prov:dh06-nohigherrank	math/0407509	main.tex	174	There is no Ihara-formula for higher rank up to date.	C9
prov:dk14-sign	1303.6848	main.tex	803	The reader may note, that this definition differs from Ihara's and others in that we consider the Euler factors with a positive exponent while other authors would prefer $1/Z_{1,+}(u)$ instead.	C9
prov:dk14-rh	1303.6848	main.tex	984-987	$$ \frac{Z_{2,+}( -u)}{Z_{1,+}(u^2)} = \frac{(1-u^3)^{\chi-1}P_1(u)}{(1-q^3u^3)P_2(u)} $$ where $P_1(u)=\prod_\alpha (1-\alpha u)$ and $P_2(u)=\prod_\beta (1-\beta u)$ with $|\alpha|=|\beta|=q^{1/2}$.	C9
prov:lsv05-Ak	math/0406208	main.tex	541-549	The vertices $\B^0$ of the building are labelled by a `color' function $\color \co \B^0 \ra \Z/d\Z$, and we may look at the $d-1$ colored adjacency operators $A_k$, $k = 1,\dots,d-1$ on $\L2{\B^0}$, called the Hecke operators. They are defined by \begin{equation}\label{Akdef} (A_kf)(x) = \sum{f(y)} \end{equation} where the summation is over the neighbors $y$ of $x$ such that $\color(y)-\color(x) = k$ in $\Z/d\Z$.	C10
prov:lsv05-ramdef	math/0406208	main.tex	564-568	\begin{defn} [{following \cite{CSZ}}] A finite quotient $X$ of $\B$ is called a Ramanujan complex if the eigenvalues of every non-trivial simultanenous eigenvector $v \in \L2{X}$, $A_k v = \lam_k v$, satisfy $(\lam_1,\dots,\lam_{d-1}) \in \Aspec_d$.	C10
prov:lsv05e-cayley	math/0406217	main.tex	499-508	\begin{thm}\label{mainIntro} Let $q$ be a prime power, $d \geq 2$, $e \geq 1$ ($e > 1$ if $q = 2$). Then, the group $G = \PGL[d](\F_{q^e})$ has an (explicit) set $S$ of $\binomq{d}{1}{q} + \binomq{d}{2}{q} + \cdots + \binomq{d}{d-1}{q}$ generators, such that the Cayley complex of $G$ with respect to $S$ is a Ramanujan complex, covered by $\B_d(F)$, when $F = \F_q\db{y}$. \end{thm}	C10
prov:lsv05e-generators	math/0406217	main.tex	1407-1415	By definition, $\Gamma$ is generated by the elements $b_u = u(1-z^{-1})u^{-1}$ of $G'(R)$, where $u$ ranges over $\mul{\F_{q^d}}/\mul{\F_{q}}$. Since $b_u = 1 - \frac{u}{\phi(u)}z^{-1}$, for every $u$, there is a unique $r \in \mul{\F_{q^d}}$ with $\Norm(r)=1$, such that $b_u = b_{(r)} = 1 - rz^{-1}$, where $\Norm =\Norm_{\F_{q^d}/\F_q}$ is the norm map.	C10
prov:lub18-zeta-programme	1712.02526	main.tex	497	Ramanujan graphs can be characterized as those graphs whose associated zeta functions satisfy ``the Riemann Hypothesis (RH)" ... An interesting direction of research is to try to associate to high dimensional complexes suitable ``zeta functions" with the hope that also in this context the Ramanujaness of the complex can be expressed via the RH.	C10
```
