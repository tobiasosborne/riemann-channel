# Sources for the hypotheses of the ring-norm-tensor campaign

Author: claude:opus-5. Date: 2026-09-14.

Purpose: for each hypothesis label H-* of `notes/ring-norm-tensor/astra-brief.md`, one
arXiv source whose **TeX** contains a quotable precise statement, plus the non-arXiv
primary reference where the canonical source is not on arXiv. Every quote below was
copied verbatim out of the file under `refs/src/<id>/` and its line number verified by
printing that line with `sed -n`; the printed output is pasted under each quote. Citation
format is `<arxiv-id>:<file>:<line>`, as in `refs/README.md`. All nine new e-prints were
downloaded with `curl https://arxiv.org/e-print/<id>`, all are gzipped **TeX** (none
PDF-only), and all are listed in `refs/fetch_sources.sh` and hashed in
`refs/manifest.sha256`.

Convention used below: a quote is marked **exact** when the quoted sentence states the
hypothesis as drafted in the brief, **variant** when it states a more general, a more
special, or a differently-packaged form (the difference is then spelled out), and
**assumed** when no arXiv TeX statement was found and only the primary (non-arXiv)
reference is recorded.

---

## H-WEIL — Riemann hypothesis for curves and abelian varieties over F_q

* arXiv **1509.00797**, J. S. Milne, *The Riemann Hypothesis over Finite Fields: From Weil
  to the Present Day*, 2015.

Quote 1 (the point-count formula), `1509.00797:pRH.tex:176`:

```
N_{n}=1+q^{n}-(a_{1}^{n}+\cdots+a_{2g}^{n}).
```

    $ sed -n '176p' refs/src/1509.00797/pRH.tex
    N_{n}=1+q^{n}-(a_{1}^{n}+\cdots+a_{2g}^{n}).

Quote 2 (the Weil bound on the eigenvalues), `1509.00797:pRH.tex:1675-1677`:

```
integer coefficients, and its roots $a_{1},\ldots,a_{2g}$ have absolute value
$q^{1/2}$. For all $\ell\neq p$,%
```

    $ sed -n '1673,1677p' refs/src/1509.00797/pRH.tex
    \label{r33}Let $A$ be an abelian variety of dimension $g$ over $k=\mathbb{F}%
    {}_{q}$, and let $P(T)$ be the characteristic polynomial of the Frobenius
    endomorphism $\pi$. Then $P(T)$ is a monic polynomial of degree $2g$ with
    integer coefficients, and its roots $a_{1},\ldots,a_{2g}$ have absolute value
    $q^{1/2}$. For all $\ell\neq p$,%

Assessment: **exact**. Quote 1 is the curve count `N_n = 1 + q^n - sum_j alpha_j^n` of the
brief's CONVENTIONS paragraph; quote 2 (Milne's summary \ref{r33}) is `|alpha_j| = sqrt q`
for abelian varieties, which for `A = Jac C` is the curve case. The two together are
H-WEIL verbatim. A second, independent statement of `|rho(pi)| = q^{1/2}` is at
`1509.00797:pRH.tex:1640-1641` (Theorem \ref{r14}, quoted under H-ROSATI below).

## H-HASSE — Hasse bound and the Frobenius quadratic

* arXiv **1509.00797** (Milne, as above) for the bound;
* arXiv **1208.5370**, A. V. Sutherland, *Isogeny volcanoes*, 2012 (ANTS X), for the
  characteristic equation and the trace.

Quote 1, `1509.00797:pRH.tex:256`:

```
\left\vert |E(k)|-q-1\right\vert =|c|\leq2\,q^{1/2}\text{, }%
```

    $ sed -n '256p' refs/src/1509.00797/pRH.tex
    \left\vert |E(k)|-q-1\right\vert =|c|\leq2\,q^{1/2}\text{, }%

Quote 2, `1208.5370:IsogenyVolcanoes.tex:347-351`:

```
t = \tr \pi_E = q+1 - \#E(\Fq),
\]
and $\pi_E$ satisfies the characteristic equation $\pi_E^2-t\pi_E+q=0$.
```

    $ sed -n '347,351p' refs/src/1208.5370/IsogenyVolcanoes.tex
    The \emph{trace of Frobenius} is given by
    \[
    t = \tr \pi_E = q+1 - \#E(\Fq),
    \]
    and $\pi_E$ satisfies the characteristic equation $\pi_E^2-t\pi_E+q=0$.

Assessment: **exact** for all three clauses of H-HASSE (`#E(F_q) = q + 1 - a`,
`|a| <= 2 sqrt q`, `pi^2 - a pi + q = 0`), but split across two sources: Milne's `c` is
minus the brief's `a` (he writes `|E(k)| = 1 + c + q`, so `c = -t`), Sutherland's `t` is
the brief's `a`. Sutherland's sentence is for ordinary curves only; Milne's bound is for
every elliptic curve over a finite field.

## H-DEURING — Deuring's lifting theorem (ordinary curve, endomorphisms lift, pi lifts to a complex number)

* arXiv **1701.07742**, M. Goresky and Y.-S. Tai, *Real structures on ordinary Abelian
  varieties*, 2017 — states the Serre–Tate canonical lift plus Deligne's equivalence,
  which is the g-dimensional form of H-DEURING (g = 1 gives the brief's statement).
* Primary (non-arXiv, **assumed**): M. Deuring, *Die Typen der Multiplikatorenringe
  elliptischer Funktionenkörper*, Abh. Math. Sem. Hansischen Univ. **14** (1941), 197–272.
  This bibliographic datum is itself byte-verifiable at `1509.00797:pRH.tex:4609-4610`:

```
Deuring, M. 1941. Die Typen der Multiplikatorenringe elliptischer
Funktionenk\"orper. Abh. Math. Sem. Hansischen Univ. 14, (1941). 197--272.
```

    $ sed -n '4609,4610p' refs/src/1509.00797/pRH.tex
    Deuring, M. 1941. Die Typen der Multiplikatorenringe elliptischer
    Funktionenk\"orper. Abh. Math. Sem. Hansischen Univ. 14, (1941). 197--272.

Quote (the lift and the lifted Frobenius on the lattice), `1701.07742:main.tex:580-584`:

```
By a theorem of Serre and Tate,  \cite{Drinfeld, Katz, Messing, Srinivas} the ordinary Abelian
variety $A$ has a canonical lift $\bar A$ over $W(k)$ which, using (\ref{eqn-epsilon}) 
gives rise to a complex variety $A_{\CC}$ over $\CC.$  Let $F \in \Gal(\bar k/k)$ denote the Frobenius.
The geometric action of $F$ on $A$ lifts to an automorphism $F_A$ on
\[ T = T_A = H_1(A_{\CC},\ZZ).\]
```

    $ sed -n '580,584p' refs/src/1701.07742/main.tex
    By a theorem of Serre and Tate,  \cite{Drinfeld, Katz, Messing, Srinivas} the ordinary Abelian
    variety $A$ has a canonical lift $\bar A$ over $W(k)$ which, using (\ref{eqn-epsilon}) 
    gives rise to a complex variety $A_{\CC}$ over $\CC.$  Let $F \in \Gal(\bar k/k)$ denote the Frobenius.
    The geometric action of $F$ on $A$ lifts to an automorphism $F_A$ on
    \[ T = T_A = H_1(A_{\CC},\ZZ).\]

Quote (Deligne's equivalence, which supplies "the reduction map End -> End is an
isomorphism"), `1701.07742:main.tex:586-592`:

```
\begin{thm} \cite{Deligne} \label{thm-Deligne}
This association $A \to (T_A,F_A)$, determined by the embedding (\ref{eqn-epsilon}), 
induces an equivalence of categories between
the category of $n$-dimensional ordinary Abelian varieties over $k=\FF_q$ and the
category of Deligne modules of rank $2n$.
\end{thm}
```

    $ sed -n '586,591p' refs/src/1701.07742/main.tex
    \begin{thm} \cite{Deligne} \label{thm-Deligne}
    This association $A \to (T_A,F_A)$, determined by the embedding (\ref{eqn-epsilon}), 
    induces an equivalence of categories between
    the category of $n$-dimensional ordinary Abelian varieties over $k=\FF_q$ and the
    category of Deligne modules of rank $2n$.
    \end{thm}

Assessment: **variant**, in the direction the campaign needs. It is not Deuring's 1941
statement about elliptic curves over a number field and reduction at a prime above p; it
is the Serre–Tate canonical lift to `W(k)`, embedded in `C`, together with Deligne's
categorical equivalence `A |-> (T = H_1(A_C, Z), F)`. For `n = 1` this gives precisely the
data the prover uses in T1: a rank-2 lattice `T = Lambda` and an endomorphism `F` of it
which is the lift of Frobenius (and, over `C`, multiplication by the complex number pi —
see H-CM below for `F` acting by `phi(pi)` on each `C_phi`). The clause "whose
endomorphism ring is O and whose reduction map is an isomorphism taking pi~ to pi" is the
fully-faithfulness half of Theorem thm-Deligne, not stated separately. No arXiv source was
found (searches: "Deuring", "Deuring correspondence", "Deuring lifting theorem",
"Deuring for the people") that states the ordinary lifting theorem in Deuring's own form;
for that, cite Deuring 1941 directly, or Lang, *Elliptic Functions*, Ch. 13 §5
(Deuring's lifting theorem), as an assumed fact.

## H-DEG — degree of the isogeny = lattice index = norm; degree is a positive quadratic form

* arXiv **1208.5370** (Sutherland) for `deg = ideal norm = index`;
* arXiv **1509.00797** (Milne) for `deg alpha = det(alpha | T_l E)` and its positivity.

Quote 1, `1208.5370:IsogenyVolcanoes.tex:273`:

```
Provided that $\fa$ has norm not divisible by the characteristic of $k$, we have $\deg \varphi_\fa = N(\fa)=[\O:\fa]$.
```

    $ sed -n '273p' refs/src/1208.5370/IsogenyVolcanoes.tex
    Provided that $\fa$ has norm not divisible by the characteristic of $k$, we have $\deg \varphi_\fa = N(\fa)=[\O:\fa]$.

Quote 2 (positivity of the degree form, which is Hasse's discriminant argument),
`1509.00797:pRH.tex:241-242`:

```
The right hand side is the degree of the map $m-n\alpha$, which is always
nonnegative, and so the discriminant $c^{2}-4d\leq0$, i.e., $c^{2}\leq4d$.
```

    $ sed -n '241,242p' refs/src/1509.00797/pRH.tex
    The right hand side is the degree of the map $m-n\alpha$, which is always
    nonnegative, and so the discriminant $c^{2}-4d\leq0$, i.e., $c^{2}\leq4d$.

and, six lines above quote 2, `1509.00797:pRH.tex:248-249` gives `d = deg(pi) = q`:

    $ sed -n '248,249p' refs/src/1509.00797/pRH.tex
    $f=T^{2}+cT+d$ be the characteristic polynomial of $\pi$. Then $d=\deg(\pi
    )=q$, and $c^{2}\leq4d=4q$. From%

Assessment: **variant**. Sutherland's sentence is `deg phi_a = N(a) = [O : a]` for the
isogeny attached to an invertible O-ideal a, not literally `[Lambda : pi Lambda] =
N_{K/Q}(pi)` for the principal ideal `(pi)` on `C/Lambda`; the principal case is the
special case `a = (pi)` (and then `[O : (pi)] = |pi|^2`). Milne supplies the two remaining
halves of H-DEG: that the degree of `m - n alpha` is a nonnegative (indeed positive
definite) integral quadratic form in `(m,n)`, and that `deg(pi) = q`. Together they are
H-DEG; no single quote states it.

## H-LEF — Lefschetz fixed points of a toral endomorphism, and the dynamical zeta function

* arXiv **0810.1855**, M. Baake, E. Lau, V. Paskunas, *A note on the dynamical zeta
  function of general toral endomorphisms*, 2008 (Monatsh. Math. **161** (2010) 33–42).

Quote 1 (fixed point count), `0810.1855:main.tex:94-98`:

```
For $M\in \Mat (d,\ZZ)$ and $m\geq 1$, let $a_m$ be the number of
\emph{isolated} fixed points in $\TT^d$ of the $m$-th iterate $M^m$.
The starting point of our considerations is the identity
\begin{equation} \label{fixcount}
     a^{}_{m} = \lvert \ts \det(\one - M^m) \rvert \ts .
```

    $ sed -n '94,98p' refs/src/0810.1855/main.tex
    For $M\in \Mat (d,\ZZ)$ and $m\geq 1$, let $a_m$ be the number of
    \emph{isolated} fixed points in $\TT^d$ of the $m$-th iterate $M^m$.
    The starting point of our considerations is the identity
    \begin{equation} \label{fixcount}
         a^{}_{m} = \lvert \ts \det(\one - M^m) \rvert \ts .

Quote 2 (the signed = Lefschetz zeta function as an alternating product over exterior
powers, i.e. Lefschetz on `H^*(T^d) = Lambda^*(H^1)`), `0810.1855:main.tex:196-201`:

```
\begin{prop}
\label{pr-zeta-torus}
   For $M\in \Mat (d,\ZZ)$, we have 
   $\; \widetilde{\zeta}^{}_{M} (z) = \prod_{k=0}^{d}
    \det \bigl( \one - z \ep^k (M) \bigr)^{(-1)^{k+1}}$.
\end{prop}
```

    $ sed -n '196,201p' refs/src/0810.1855/main.tex
    \begin{prop}
    \label{pr-zeta-torus}
       For $M\in \Mat (d,\ZZ)$, we have 
       $\; \widetilde{\zeta}^{}_{M} (z) = \prod_{k=0}^{d}
        \det \bigl( \one - z \ep^k (M) \bigr)^{(-1)^{k+1}}$.
    \end{prop}

with `\widetilde a_m = det(1 - M^m)` defined at `0810.1855:main.tex:179` and the name
"Lefschetz zeta function" attached to `\widetilde\zeta_M` at `0810.1855:main.tex:186-187`:

    $ sed -n '179p;186,187p' refs/src/0810.1855/main.tex
    Let us start with the numbers $\widetilde{a}_{m} := \det(\one - M^m)$,
    In Section~\ref{sec:lef}, we will see that this is actually a
    Lefschetz zeta function, see Eq.~\eqref{rel-equals-lef} below.

Assessment: **variant, and stronger than needed**. The brief's H-LEF is the general
Lefschetz fixed point theorem for a self-map with nondegenerate fixed points; this source
states its toral specialisation — exactly the case T1(a),(b) uses — with the unsigned
count `|det(1 - M^m)|` and the signed (Lefschetz) zeta as the alternating product over
`Lambda^k(M)`. For T1 the sign issue is void: `det(1 - M^n) = |1 - pi^n|^2 > 0`, so the
two counts agree and `a_m = det(1 - M^m) = N_m`. The general manifold-level H-LEF is not
stated here; if the prover wants the general theorem it should be cited to a topology text
(e.g. Dold, *Lectures on Algebraic Topology*, VII.6) as assumed.

## H-LENSTRA — CM structure of E(F_{q^n})

* arXiv **2006.00637**, C. Springer, *The Structure of the Group of Rational Points of an
  Abelian Variety over a Finite Field*, 2020 (states Lenstra's Theorem 1 verbatim).
* Primary (non-arXiv, **assumed**): H. W. Lenstra, Jr., *Complex multiplication structure
  of elliptic curves*, J. Number Theory **56** (1996), 227–241; bibliographic datum
  byte-verifiable at `2006.00637:main.tex:625-628`.

Quote, `2006.00637:main.tex:97-104`:

```
\begin{theorem}[{\cite{lenstra}, Theorem 1}]
\label{len-thm}
	Let $E$ be an elliptic curve over $\FF_q$. Write $R = \End_{\FF_q}(E)$ and let $\pi \in R$ be the Frobenius endomorphism of $E$.  
	\begin{enumerate}[(a)]
	\item  Suppose that $\pi \notin\ZZ$.  Then $R$ has rank $2$ over $\ZZ$ and there is an isomorphism of $R$-modules
	$$
		E(\FF_{q^n}) \cong R/(\pi^n - 1)R.
	$$
```

    $ sed -n '97,104p' refs/src/2006.00637/main.tex
    \begin{theorem}[{\cite{lenstra}, Theorem 1}]
    \label{len-thm}
    	Let $E$ be an elliptic curve over $\FF_q$. Write $R = \End_{\FF_q}(E)$ and let $\pi \in R$ be the Frobenius endomorphism of $E$.  
    	\begin{enumerate}[(a)]
    	\item  Suppose that $\pi \notin\ZZ$.  Then $R$ has rank $2$ over $\ZZ$ and there is an isomorphism of $R$-modules
    	$$
    		E(\FF_{q^n}) \cong R/(\pi^n - 1)R.
    	$$

    $ sed -n '625,628p' refs/src/2006.00637/main.tex
    \bibitem{lenstra}
    {\sc Lenstra, Jr., H.~W.}
    \newblock Complex multiplication structure of elliptic curves.
    \newblock {\em J. Number Theory 56}, 2 (1996), 227--241.

Assessment: **exact**. `pi not in Z` is exactly "E ordinary or non-supersingular with
CM by an imaginary quadratic order" (for ordinary E it always holds), `R = End_{F_q}(E) =
O`, and `E(F_{q^n}) ≅ O/(pi^n - 1)O` as O-modules is H-LENSTRA as drafted. Note the source
states it for `R = End_{F_q}(E)`, the ring of F_q-rational endomorphisms; for ordinary E
this is all of End(E).

## H-LM — Latimer–MacDuffee

* arXiv **2205.02094**, L. Knight and A. Stasinski, *Representatives of similarity classes
  of matrices over PIDs corresponding to ideal classes*, 2022.
* Primary (non-arXiv, **assumed**): C. G. Latimer and C. C. MacDuffee, *A correspondence
  between classes of ideals and classes of matrices*, Ann. of Math. (2) **34** (1933),
  313–316; bibliographic datum byte-verifiable at `2205.02094:main.bbl:19-22`.

Quote, `2205.02094:main.tex:93-97`:

```
Latimer and MacDuffee \cite{Latimer-MacDuffee} showed that there
is a bijection between the similarity classes of matrices with integer
entries (i.e., the orbits under the action of $\GL_{n}(\Z)$ on $\M_{n}(\Z)$
by conjugation) with irreducible characteristic polynomial $f(x)\in\Z[x]$
and the ideal classes of the order $\Z[x]/(f(x))$. Another proof
```

    $ sed -n '93,97p' refs/src/2205.02094/main.tex
    Latimer and MacDuffee \cite{Latimer-MacDuffee} showed that there
    is a bijection between the similarity classes of matrices with integer
    entries (i.e., the orbits under the action of $\GL_{n}(\Z)$ on $\M_{n}(\Z)$
    by conjugation) with irreducible characteristic polynomial $f(x)\in\Z[x]$
    and the ideal classes of the order $\Z[x]/(f(x))$. Another proof

    $ sed -n '19,22p' refs/src/2205.02094/main.bbl
    \bibitem{Latimer-MacDuffee}
    C.~G. Latimer and C.~C. MacDuffee, \emph{A correspondence between classes of
      ideals and classes of matrices}, Ann. of Math. (2) \textbf{34} (1933), no.~2,
      313--316.

The canonicity of the bijection (the direction the brief needs: an ideal `I` maps to the
matrix of multiplication by `x` on a Z-basis of `I`) is at `2205.02094:main.tex:538-542`
plus the sentence following it:

    $ sed -n '538,545p' refs/src/2205.02094/main.tex
    \begin{thm}
    There is a canonical bijection between the similarity classes of matrices
    in $\M_{n}(A)$ with characteristic polynomial $f(x)$ and ideal classes
    in $A[\theta]$.
    \end{thm}
    
    The bijection is canonical in the following sense. Let $\alpha\in\M_{n}(A)$
    have characteristic polynomial $f(x)$. Then $\theta$ is an eigenvalue of $\alpha$

Assessment: **exact** for the bijection as drafted (with `Z[x]/(f)` the order and `f`
monic irreducible of degree n = d); the brief's parenthetical description of the map
("an ideal I mapping to the matrix of multiplication by x on a Z-basis of I") is the
content of the "canonical" clause and of the surrounding paragraph, which is a longer
paraphrase rather than a single quotable sentence.

## H-WAT — Waterhouse: isomorphism classes in an ordinary isogeny class vs. ideal classes of orders

* arXiv **1208.5370** (Sutherland) for the torsor statement;
* arXiv **2006.00637** (Springer) for the citation of Waterhouse Thm 7.4 (which orders occur);
* arXiv **2605.07626** (M. el Baraka, S. Ezzouak, *Weighted Distributions of Complex
  Multiplication Orders in Ordinary Isogeny Classes*, 2026) for the joint attribution to
  Deuring 1941 + Waterhouse 1969. **Caveat**: this is a very recent, unrefereed preprint
  whose front matter contains typographic errors; use it only for attribution, never as
  the authority for a proof.
* Primary (non-arXiv, **assumed**): W. C. Waterhouse, *Abelian varieties over finite
  fields*, Ann. Sci. École Norm. Sup. (4) **2** (1969), 521–560; bibliographic datum
  byte-verifiable at `2006.00637:main.tex:670-673`.

Quote 1 (the class-group torsor), `1208.5370:IsogenyVolcanoes.tex:278-284`:

```
When $\fa$ is a principal ideal, we have $E\simeq E'$, thus there is an induced action of the ideal class group $\cl(\O)$ on the set
\[
\Ell_\O(k) = \{j(E): E/k \text{ with } \End(E)\simeq \O\}.
\]
This action is faithful (only principal ideals act trivially), and transitive (see \cite[Prop.~II.1.2]{Silverman:EllipticCurves2} for a proof in the case that $k=\C$ and $\O=\O_K$, which may be generalized via \cite[Ch.~10,13]{Lang:EllipticFunctions}).
Provided it is non-empty, the set $\Ell_\O(k)$ is thus a principal homogeneous space, a \emph{torsor}, for the group $\cl(\O)$.
```

    $ sed -n '278,283p' refs/src/1208.5370/IsogenyVolcanoes.tex
    When $\fa$ is a principal ideal, we have $E\simeq E'$, thus there is an induced action of the ideal class group $\cl(\O)$ on the set
    \[
    \Ell_\O(k) = \{j(E): E/k \text{ with } \End(E)\simeq \O\}.
    \]
    This action is faithful (only principal ideals act trivially), and transitive (see \cite[Prop.~II.1.2]{Silverman:EllipticCurves2} for a proof in the case that $k=\C$ and $\O=\O_K$, which may be generalized via \cite[Ch.~10,13]{Lang:EllipticFunctions}).
    Provided it is non-empty, the set $\Ell_\O(k)$ is thus a principal homogeneous space, a \emph{torsor}, for the group $\cl(\O)$.

Quote 2 (the decomposition of the isogeny class over the orders `Z[pi] <= O <= O_K`),
`1208.5370:IsogenyVolcanoes.tex:368-372`, printed here from line 368:

    $ sed -n '368p' refs/src/1208.5370/IsogenyVolcanoes.tex
    By a theorem of Tate \cite{Tate:IsogenyTheorem}, $\Ell_t(\Fq)$ corresponds to an isogeny class, but note that $\Ell_t(\Fq)=\Ell_{-t}(\Fq)$.  For any ordinary elliptic curve $E/\Fq$ with Frobenius trace $t=\tr \pi_E$, we may write $\Ell_t(\Fq)$ as the disjoint union

Quote 3 (Waterhouse 7.4, which orders occur), `2006.00637:main.tex:134` (long line; the
relevant clause):

```
In fact, if $\pi$ is an ordinary Weil $q$-integer, then the rings which arise as the endomorphism rings of abelian varieties in the corresponding isogeny class over $\FF_q$ are precisely the orders of $\QQ(\pi)$ which contain the minimal order $\ZZ[\pi, \overline\pi]$ \cite[Theorem 7.4]{waterhouse}.
```

    $ sed -n '134p' refs/src/2006.00637/main.tex | cut -c 508-807
    In fact, if $\pi$ is an ordinary Weil $q$-integer, then the rings which arise as the endomorphism rings of abelian varieties in the corresponding isogeny class over $\FF_q$ are precisely the orders of $\QQ(\pi)$ which contain the minimal order $\ZZ[\pi, \overline\pi]$ \cite[Theorem 7.4]{waterhouse}.

    $ sed -n '670,673p' refs/src/2006.00637/main.tex
    \bibitem{waterhouse}
    {\sc Waterhouse, W.~C.}
    \newblock Abelian varieties over finite fields.
    \newblock {\em Ann. Sci. \'{E}cole Norm. Sup. (4) 2\/} (1969), 521--560.

Quote 4 (attribution of the order stratification to Deuring and Waterhouse),
`2605.07626:Weighted_Distributions_of_Complex_Multiplication.tex:444-449`:

    $ sed -n '444,449p' refs/src/2605.07626/Weighted_Distributions_of_Complex_Multiplication.tex
    For every $E\in\mathcal{I}(t,p)$ one has
    \[
    \Z[\pi_E]\subseteq \End(E)\subseteq \mathcal{O}_K,
    \]
    and $\End(E)\simeq \mathcal{O}_f$ for a unique divisor $f\mid v$
    (Deuring \cite{Deuring1941}, Waterhouse \cite{Waterhouse1969}).

Assessment: **variant**. Sutherland states that `Ell_O(k)` (F_q-curves with End ≅ O, up to
isomorphism, indexed by j-invariant) is a `cl(O)`-torsor — which is H-WAT's bijection once
a base point is chosen, but the bijection is not canonical (a torsor, not a canonical
bijection with `cl(O)`), and the set is indexed by j-invariants rather than by
F_q-isomorphism classes (these differ by quadratic twists, an issue the brief's H-WAT
glosses). Quote 3 states the other half of H-WAT (which orders `Z[pi] <= O <= O_K` occur)
with explicit attribution to Waterhouse Thm 7.4, but for `Z[pi, pi-bar]`, which for
ordinary elliptic curves equals `Z[pi]`. No arXiv source states H-WAT as a single
proposition; cite Waterhouse 1969 §7 directly for the sharp form.

## H-CM — CM field, CM type, canonical lift, Frobenius acting by phi(pi) on C_phi

* arXiv **1701.07742** (Goresky–Tai) for the canonical lift, the lattice `T = H_1(A_C,Z)`,
  the eigenvalue normalisation, and the CM type with its positivity condition;
* arXiv **2003.05380**, T. Dupuy, K. Kedlaya, D. Roe, C. Vincent, *Isogeny Classes of
  Abelian Varieties over Finite Fields in the LMFDB*, 2020, for `Q(pi)` being CM.

Quote 1 (`|eigenvalues| = sqrt q` and the ordinarity condition — Deligne module axioms),
`1701.07742:main.tex:565-566`:

```
\item The mapping $F$ is semisimple and all of its eigenvalues in $\CC$ have magnitude
$\sqrt{q}.$
```

    $ sed -n '565,566p' refs/src/1701.07742/main.tex
    \item The mapping $F$ is semisimple and all of its eigenvalues in $\CC$ have magnitude
    $\sqrt{q}.$

Quote 2 (`Q(pi)` is a CM field), `2003.05380:weil.tex:332`:

```
\item $\QQ(\pi)$ is a CM-field with maximal totally real subfield $\QQ(\beta)$, and $\pi$ has no real embeddings;
```

    $ sed -n '332p' refs/src/2003.05380/weil.tex
    \item $\QQ(\pi)$ is a CM-field with maximal totally real subfield $\QQ(\beta)$, and $\pi$ has no real embeddings;

    $ sed -n '343p' refs/src/2003.05380/weil.tex
    \item The fact that $\QQ(\pi)$ is CM is \cite{Honda1967}*{Proposition 4}, and the second part follows.

Quote 3 (CM type and its positivity — the polarisation side of H-CM),
`1701.07742:main.tex:604-609`:

```
and where $\Phi$ is a CM type on $\QQ[F]$ such that the following {\em positivity
condition} holds:
\begin{enumerate} 
\item[(3)] the form $R(x,y) = \omega(x,\iota y)$ is symmetric and positive definite,
where $\iota$ is some (and hence, any) totally $\Phi$-positive imaginary element of $\QQ[F]$ 
```

    $ sed -n '604,608p' refs/src/1701.07742/main.tex
    and where $\Phi$ is a CM type on $\QQ[F]$ such that the following {\em positivity
    condition} holds:
    \begin{enumerate} 
    \item[(3)] the form $R(x,y) = \omega(x,\iota y)$ is symmetric and positive definite,
    where $\iota$ is some (and hence, any) totally $\Phi$-positive imaginary element of $\QQ[F]$ 

Assessment: **variant**, and incomplete in one place. The source gives: the canonical
(Serre–Tate) lift (quote under H-DEURING), `T = H_1(A_C, Z)` with the lifted Frobenius,
`|eigenvalue| = sqrt q`, the CM type `Phi` on `Q[F]` and the positivity condition defining
a `Phi`-positive polarisation. It does **not** state the Hodge decomposition in the shape
the brief writes it, `H^1(A~(C), C) = (+)_phi C_phi` with `H^{1,0} = (+)_{phi in Phi}
C_phi` and `pi~` acting on `C_phi` by `phi(pi)`; that eigenspace decomposition must be
derived (it is the standard CM-type description of the tangent space, Shimura–Taniyama)
or cited to Milne, *Abelian Varieties* (course notes, not on arXiv) or Lang,
*Complex Multiplication*, Ch. 1 — record as **assumed**. That `End^0(A) = K` when
`[Q(pi):Q] = 2g` is stated at `2006.00637:main.tex:134` (first clause of the long line).

## H-ROSATI — positivity of the Rosati involution; pi pi^dagger = q

* arXiv **1509.00797** (Milne).

Quote 1, `1509.00797:pRH.tex:1557-1565`:

```
\begin{theorem}
\label{r12}The Rosati involution on $E\overset{\textup{{\tiny def}}}%
{=}\End^{0}(A)$ is positive, i.e., the pairing%
\[
\alpha,\beta\mapsto\Tr_{E/\mathbb{Q}{}}(\alpha\circ\beta^{\dagger})\colon
E\times E\rightarrow\mathbb{Q}{}%
\]
is positive definite.
\end{theorem}
```

    $ sed -n '1557,1565p' refs/src/1509.00797/pRH.tex
    \begin{theorem}
    \label{r12}The Rosati involution on $E\overset{\textup{{\tiny def}}}%
    {=}\End^{0}(A)$ is positive, i.e., the pairing%
    \[
    \alpha,\beta\mapsto\Tr_{E/\mathbb{Q}{}}(\alpha\circ\beta^{\dagger})\colon
    E\times E\rightarrow\mathbb{Q}{}%
    \]
    is positive definite.
    \end{theorem}

Quote 2 (`pi pi^dagger = q` and `|rho(pi)| = q^{1/2}`), `1509.00797:pRH.tex:1634-1643`:

```
\begin{theorem}
\label{r14}Let $A$ be an abelian variety over $k=\mathbb{F}{}_{q}$, and let
$\pi\in\End(A)$ be the Frobenius endomorphism. Let $^{\dagger}$ be a Rosati
involution on $\End^{0}(A)$. For every homomorphism $\rho\colon\mathbb{Q}%
[\pi]\rightarrow\mathbb{C}$,
\[
\rho(\alpha^{\dagger})=\overline{\rho(\pi)}\text{ and }\left\vert \rho
\pi\right\vert =q^{1/2}.
\]
```

    $ sed -n '1634,1643p' refs/src/1509.00797/pRH.tex
    \begin{theorem}
    \label{r14}Let $A$ be an abelian variety over $k=\mathbb{F}{}_{q}$, and let
    $\pi\in\End(A)$ be the Frobenius endomorphism. Let $^{\dagger}$ be a Rosati
    involution on $\End^{0}(A)$. For every homomorphism $\rho\colon\mathbb{Q}%
    [\pi]\rightarrow\mathbb{C}$,
    \[
    \rho(\alpha^{\dagger})=\overline{\rho(\pi)}\text{ and }\left\vert \rho
    \pi\right\vert =q^{1/2}.
    \]

and the identity `pi pi^dagger = q_A` is proved two lines into that proof,
`1509.00797:pRH.tex:1647-1648`:

    $ sed -n '1647,1648p' refs/src/1509.00797/pRH.tex
    This will follow from (\ref{r39}) once we show that $\pi\circ\pi^{\dagger
    }=q_{A}$. This can be proved by a direct calculation, but it is more

Assessment: **exact** for the positivity clause, with the caveat that the brief writes it
as `Tr(x x^dagger) > 0` on `End(A) (x) R` while Milne states positive definiteness of the
rational trace form on `End^0(A) = End(A) (x) Q` (the two are equivalent by continuity /
density). `pi pi^dagger = q` is stated inside the proof of Theorem r14, not as a numbered
statement, so quote lines 1647-1648 for it.

## H-SCHUR — sum |mu_i|^2 <= ||M||_HS^2, equality iff M normal

**assumed — no arXiv TeX source found.** Searched arXiv (all fields) for "Schur
inequality", "Schur's inequality eigenvalues matrix", "Schur triangularization",
"departure from normality eigenvalues", "normality Frobenius norm eigenvalues bound
matrix", "Schur upper bound eigenvalues normal matrices"; also grepped the whole existing
`refs/src` corpus for "Schur's inequality" / "Schur inequality" — no hits. This is a
textbook fact with no modern arXiv restatement in quotable form. Record as assumed with:

* I. Schur, *Über die charakteristischen Wurzeln einer linearen Substitution mit einer
  Anwendung auf die Theorie der Integralgleichungen*, Math. Ann. **66** (1909), 488–510
  (the inequality and the equality case).
* R. A. Horn and C. R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge UP, 2013,
  Theorem 2.3.1 (Schur triangularization) and the ensuing (2.3.2a): for
  `A in M_n(C)` with eigenvalues `lambda_1, ..., lambda_n`,
  `sum_i |lambda_i|^2 <= tr(A^* A) = ||A||_F^2`, with equality if and only if `A` is
  normal.

The prover can also prove it in one line from Schur triangularisation (`A = U(T)U^*`,
`||A||_F^2 = sum_i |lambda_i|^2 + sum_{i<j} |t_{ij}|^2`), which is the recommended route
given that no byte-verifiable external statement exists.

## Extra 1 — Lefschetz / dynamical zeta for a toral endomorphism

Covered by **0810.1855** above (both the fixed-point count `|det(1 - M^m)|` and the
Lefschetz zeta as an alternating product over `Lambda^k H^1`). This is the single source
that delivers the whole of T1(a),(b).

## Extra 2 — Hodge inner product on 1-forms is positive definite

* arXiv **0903.2156**, A. Lesfari, *Surfaces de Riemann compactes, courbes algébriques
  complexes et leurs Jacobiennes*, 2009 (in French).

Quote (the second Riemann bilinear relation = positivity of the Hodge form),
`0903.2156:main.tex:1189-1199`:

```
\begin{thm}
Soient $\omega $\ et $\omega ^{\prime }$\ et deux
diff\'{e}rentielles holomorphes sur $X$. Alors,
$$\sum_{k=1}^{g}\left( \int_{a_{k}}\omega \int_{b_{k}}\omega ^{\prime }
-\int_{b_{k}}\omega \int_{a_{k}}\omega ^{\prime }\right) =0.$$ Si
en outre $\omega $\ est non nulle, alors
$$i\sum_{k=1}^{g}\left( \int_{a_{k}}\omega
\int_{b_{k}}\overline{\omega }-\int_{b_{k}}\omega \int_{a_{k}}
\overline{\omega }\right) \text{ }>  0.$$ (Ces deux expressions
s'appellent relations bilin\'{e}aires de Riemann).
\end{thm}
```

    $ sed -n '1189,1199p' refs/src/0903.2156/main.tex
    \begin{thm}
    Soient $\omega $\ et $\omega ^{\prime }$\ et deux
    diff\'{e}rentielles holomorphes sur $X$. Alors,
    $$\sum_{k=1}^{g}\left( \int_{a_{k}}\omega \int_{b_{k}}\omega ^{\prime }
    -\int_{b_{k}}\omega \int_{a_{k}}\omega ^{\prime }\right) =0.$$ Si
    en outre $\omega $\ est non nulle, alors
    $$i\sum_{k=1}^{g}\left( \int_{a_{k}}\omega
    \int_{b_{k}}\overline{\omega }-\int_{b_{k}}\omega \int_{a_{k}}
    \overline{\omega }\right) \text{ }>  0.$$ (Ces deux expressions
    s'appellent relations bilin\'{e}aires de Riemann).
    \end{thm}

and the intrinsic form of the same positivity, in the proof,
`0903.2156:main.tex:1254` and `0903.2156:main.tex:1262`:

    $ sed -n '1254p;1262p' refs/src/0903.2156/main.tex
    $$\omega\wedge \overline{\omega}=-2i|f|^2dx\wedge dy.$$
    &=&\int_X|f|^2dx\wedge dy > 0, \quad \omega\neq 0,\nonumber

Assessment: **variant**, and it is the right variant for T1(e)/T4(c). The theorem is the
pair of Riemann bilinear relations for a compact Riemann surface `X` of genus `g`; the
second one is exactly the statement that the Hermitian form
`(omega, omega') |-> i int_X omega ^ conj(omega')` on `H^{1,0}(X)` is positive definite
(`i int_X omega ^ conj omega = int_X |f|^2 dx ^ dy > 0` for `omega = f dz != 0`). For the
flat torus (`g = 1`, `X = C/Lambda`, `omega = dz`) this is the Hodge inner product of
T1(e), and `M^*` scaling it by `|pi|^2` then follows from `M^* dz = pi dz`. The source
does not state the flat-torus case separately, nor the general Hodge-star `L^2` inner
product `(alpha, beta) = int alpha ^ *conj(beta)` on `k`-forms of a Riemannian manifold;
if the prover needs the latter in general, record as assumed (Griffiths–Harris,
*Principles of Algebraic Geometry*, Ch. 0 §6, or Warner, *Foundations of Differentiable
Manifolds*, Ch. 6).

---

## Summary table

| hypothesis | best source | quote location | exactness |
|---|---|---|---|
| H-WEIL | Milne, *RH over finite fields*, arXiv 1509.00797 (2015) | `1509.00797:pRH.tex:176` (N_n) and `:1675-1677` (\|alpha_j\|=q^{1/2}) | exact (two quotes) |
| H-HASSE | Milne 1509.00797; Sutherland, *Isogeny volcanoes*, arXiv 1208.5370 (2012) | `1509.00797:pRH.tex:256` (bound); `1208.5370:IsogenyVolcanoes.tex:347-351` (trace, char. eq.) | exact (split across two sources; sign convention c = -a) |
| H-DEURING | Goresky–Tai, arXiv 1701.07742 (2017) | `1701.07742:main.tex:580-584` (canonical lift, T=H_1) and `:586-591` (Deligne equivalence) | variant (Serre–Tate lift + Deligne equivalence, not Deuring's own form); primary assumed: Deuring 1941, bib at `1509.00797:pRH.tex:4609-4610` |
| H-DEG | Sutherland 1208.5370; Milne 1509.00797 | `1208.5370:IsogenyVolcanoes.tex:273` (deg = N(a) = [O:a]); `1509.00797:pRH.tex:241-242` (degree form nonnegative), `:248-249` (deg pi = q) | variant (principal-ideal case not stated separately; three quotes needed) |
| H-LEF | Baake–Lau–Paskunas, arXiv 0810.1855 (2008) | `0810.1855:main.tex:94-98` (a_m = \|det(1-M^m)\|); `:196-201` (Lefschetz zeta = alternating product over Lambda^k M) | variant: toral specialisation, which is what T1 uses; general manifold Lefschetz theorem not stated |
| H-LENSTRA | Springer, arXiv 2006.00637 (2020) | `2006.00637:main.tex:97-104` | exact (Lenstra Thm 1(a), quoted with attribution); primary assumed: Lenstra 1996, bib at `:625-628` |
| H-LM | Knight–Stasinski, arXiv 2205.02094 (2022) | `2205.02094:main.tex:93-97`; canonicity at `:538-545` | exact; primary assumed: Latimer–MacDuffee 1933, bib at `2205.02094:main.bbl:19-22` |
| H-WAT | Sutherland 1208.5370; Springer 2006.00637 | `1208.5370:IsogenyVolcanoes.tex:278-283` (cl(O)-torsor), `:368` (union over orders); `2006.00637:main.tex:134` (Waterhouse Thm 7.4) | variant (torsor, not canonical bijection; indexed by j-invariants); primary assumed: Waterhouse 1969, bib at `2006.00637:main.tex:670-673` |
| H-CM | Goresky–Tai 1701.07742; Dupuy–Kedlaya–Roe–Vincent, arXiv 2003.05380 (2020) | `1701.07742:main.tex:565-566` (\|eig\|=sqrt q), `:580-591` (lift), `:604-608` (CM type + positivity); `2003.05380:weil.tex:332`, `:343` (Q(pi) is CM) | variant; the H^{1,0} = (+)_{phi in Phi} C_phi eigenspace statement is NOT quotable from arXiv — assumed (Shimura–Taniyama; Lang, *Complex Multiplication*, Ch. 1) |
| H-ROSATI | Milne 1509.00797 | `1509.00797:pRH.tex:1557-1565` (positivity); `:1634-1643` (\|rho pi\|=q^{1/2}); `:1647-1648` (pi pi^dagger = q_A) | exact (positivity over Q rather than R; pi pi^dagger = q sits inside a proof) |
| H-SCHUR | none found on arXiv | — | assumed: Schur 1909, Math. Ann. 66, 488–510; Horn–Johnson, *Matrix Analysis* 2nd ed., Thm 2.3.1 and (2.3.2a). Recommend proving from Schur triangularisation |
| extra: Lefschetz/dynamical zeta of a toral endomorphism | Baake–Lau–Paskunas 0810.1855 | `0810.1855:main.tex:94-98`, `:179`, `:186-187`, `:196-201` | variant (toral case; exactly T1(a),(b)) |
| extra: Hodge inner product on 1-forms positive definite | Lesfari, arXiv 0903.2156 (2009, French) | `0903.2156:main.tex:1189-1199`; intrinsic form at `:1254`, `:1262` | variant: second Riemann bilinear relation, i.e. positive definiteness of i∫ω∧conj(ω) on H^{1,0}; flat-torus and general Hodge-star cases assumed |

### Fetch status

All nine new e-prints are TeX (gzipped tar or gzipped single .tex); none was PDF-only.
They are appended to `refs/fetch_sources.sh` (IDS list, sorted) and their hashes are in
`refs/manifest.sha256`, regenerated by running that script; the regeneration added lines
only (verified by diff against the previous manifest). New ids: 0810.1855, 0903.2156,
1208.5370, 1509.00797, 1701.07742, 2003.05380, 2006.00637, 2205.02094, 2605.07626.
