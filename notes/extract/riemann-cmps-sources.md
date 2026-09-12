# Sources for "The Riemann cMPS: what is forced and what is free"

Written 2026-09-12 by the source-acquisition worker. Every quote below was copied
out of the arXiv **TeX source** in `refs/src/<id>/` (fetched by
`refs/fetch_sources.sh`, hashes in `refs/manifest.sha256`) and is cited as
`<id>:<file>:<line-range>`; each quote is whole and contiguous in the lines
stated, so it can be re-checked with `sed -n '<a>,<b>p'` or `grep -n -a -F`.
Preference throughout: TeX source, never PDF text.

**Warning on `grep`.** Two of these files (`math/0505354/main.tex`,
`math/9811068/main.tex`) contain bytes that make GNU grep treat them as binary
and print nothing. Always pass `-a` (or `LC_ALL=C`) when re-checking quotes here.

The note is organised by the target list A–I. Each section states the arXiv id
(or "not on arXiv" plus the standard bibliographic reference), the TeX file, the
byte-verified quotes, and a one-line relevance note.

## Ids fetched for this note

`sha256` is of the raw arXiv e-print tarball `refs/src/<id>/src.tar`.

| id | file(s) quoted | sha256 of `src.tar` |
|---|---|---|
| `1807.06400` | `main.tex` | `c079d2e9ea5ae0bea796f1cb0e2b88773f14ee6699a4238a8711075e67a579d5` |
| `math/0505354` | `main.tex` | `d9095720b0adf3fada01363f32c4a809dc0c360c1abd6090d0fe35f826dd7267` |
| `0709.2801` | `main.tex` | `5a2370643da86a7f1df5d1f16ac77baa2e791edeacc719410344136fdf43727b` |
| `1307.3851` | `main.tex` | `154637f612803fc287766aae3b7021da85f08169ccd9d2686418960d5be947e7` |
| `math/9811068` | `main.tex` | `0e1a9d4acac8fd9eff70f24aed3a895c5d3af4352d0b54ca2a0629d82dd2e931` (already in tree) |
| `2006.13771` | `weil-compo.tex` | `771a004b70fb0c36cae11351bd29cec50b3da13896bb1ef5015bbdd68beadb6d` (already in tree) |
| `1610.07849` | `FermionicMPS.tex` | `cf8bc998cef5c3c3c459a7546bb38e9100b53b5e15d32601a99375cc19b6bd22` |
| `1002.1824` | `mpsQFT4.tex` | `96807fc397f2dbf105c540604944323dce3fe25406b84d15cadefb60eefa3718` |
| `1211.3935` | `calculus.tex` | `d9234001ae6a28709219a5891003dac71e1469a935616f5ebc46e4d7f5553fa6` |
| `math/0610644` | `ArxivThomasWeil3.tex` | `ff2194128ac1afdaa89d0f188cf61cf741b997ff415d692d05032275d5887017` |
| `math/0610818` | `main.tex` | `3079b372e57392c818cf3710a8ccff8226d3d43d527cbdb6ef46f7d0b5a9b65c` |
| `quant-ph/0602001` | `poswig.tex` | `1c5371144c5b8b58fb6a8272546fdee54de0045e7dad3c9135a507d987ca9dfe` |
| `quant-ph/0412001` | `main.tex` | `7bc380f788eeec36d6ea8fe08c3c9aaaf62691b45aca550b3ab43ec8ed8f8b2f` |
| `2208.06138` | `main.tex` | `2ae35f68244ea9d374343804516f3c5bf18a580abb623e7338e815e318d4f865` |
| `1007.4899` | `selfdualnb_elsart6.tex` | `e562e7fa6dd3f5c95bead0947eef8f9375e06f60622ac69fba573a2f7186bfab` |
| `1105.2914` | `main.tex` | `0e6fc201bcebed63b3ed8c7dc852d9fc0ecae122e989a2efcfe4b1c6a6eaf34a` |
| `1303.4792` | `main.tex` | `6541b79254ab18da8c3e6e7725517a3fc8f4dd1ccbb06274760eb0655ccac8e7` |
| `1009.0228` | `main.tex` | `975c9000055a0c3c9b0284c6ed2214ab1e2e922ef9fa6b52e9b39bf00c11c9c7` |
| `math/0404128` | `houcheschapter1final7.tex` | `94dc934d5f7b11932f5d3486be2f11481f8f13d7e93df37eaeb9d2541db16a9b` |

**Not on arXiv** (no quote recorded; standard reference given in place):

- C. Deninger, *Some analogies between number theory and dynamical systems on
  foliated spaces*, Doc. Math. J. DMV, Extra Volume ICM I (1998), 163–186.
  (Checked the arXiv author listing for `Deninger_C`: not present.)
- C. Deninger, *Lefschetz trace formulas and explicit formulas in analytic number
  theory*, J. Reine Angew. Math. **441** (1993), 1–15. (Cited as `[D5]` inside
  `math/0505354:main.tex:1580`, itself not on arXiv.)
- E. Leichtnam, *An invitation to Deninger's work on arithmetic zeta functions*,
  in: Geometry, Spectral Theory, Groups and Dynamics, Contemp. Math. **387**,
  AMS (2005), 201–236. (Not on arXiv; **1307.3851** below is the closest
  arXiv-hosted Leichtnam survey of the same formalism and is quoted instead.)
- R. Howe, *On the character of Weil's representation*, Trans. Amer. Math. Soc.
  **177** (1973), 287–298. (Cited as `[Howe]` in `math/0610644`; not on arXiv.
  Thomas's `math/0610644` is quoted in its place.)
- J.-B. Bost, A. Connes, *Hecke algebras, type III factors and phase transitions
  with spontaneous symmetry breaking in number theory*, Selecta Math. (N.S.)
  **1** (1995), 411–457. (Not on arXiv; the theorem is quoted from
  Connes–Marcolli `math/0404128` below.)
- A. Lempel, M. J. Weinberger, *Self-complementary normal bases in finite
  fields*, SIAM J. Discrete Math. **1** (1988), 193–198. (Not on arXiv; the
  existence criterion is quoted from `1007.4899` below.)
- B. Simon, *Trace Ideals and Their Applications*, 2nd ed., AMS Math. Surveys
  and Monographs **120** (2005), Ch. 3 (Lidskii). D. V. Widder, *The Laplace
  Transform*, Princeton (1941), Ch. II §5 (Landau/Pringsheim). Surrogate arXiv
  statements quoted in section G.
- R. Lidl, H. Niederreiter, *Finite Fields*, 2nd ed., CUP (1997), Theorems
  6.26–6.27 (Gauss sums of quadratic forms). Surrogate arXiv statement quoted in
  section H.

---

## A. Deninger's programme: graded cohomology, Frobenius flow, Lefschetz = explicit formula

### A1. `math/0505354` — Deninger, *Arithmetic Geometry and Analysis on Foliated Spaces*

Title and author:
- `math/0505354:main.tex:113-114`
```
\title{Arithmetic Geometry and Analysis on Foliated Spaces}
\author{Christopher Deninger}
```

This is the Arizona lecture-series version of the ICM 1998 programme and the
single most quotable source for the graded picture. **The conjectural formula
for the completed Dedekind zeta as an alternating product of regularised
determinants:**
- `math/0505354:main.tex:308-312`
```
Here, $\Fr_p$ is the absolute Frobenius morphism and $\oeX = \eX \otimes_{\F_p} \OF_p$. This formula together with the proposition suggests by analogy that a formula of the following type might hold:
\begin{equation}
  \label{eq:2}
  \hat{\zeta}_K (s) = \prod^2_{i=0} \ddet_{\infty} \textstyle \left( \frac{1}{2 \pi} (s -\Theta) \tei H^i_{\dyn} ( \overline{\spec \eo}  , \Rh) \right)^{(-1)^{i+1}} \; .
\end{equation}
```

**The forced grading `H^0, H^1, H^2`** — the pole at `s=1` in `H^2` (and `s=0`
in `H^0`), the zeros in `H^1`:
- `math/0505354:main.tex:316-326`
```
As recalled earlier $\hat{\zeta}_K (s)$ has poles only at $s = 0,1$ and these are of first order. Moreover the zeroes of $\hat{\zeta}_K (s)$ are just the
non-trivial zeroes of $\zeta_K (s)$. If we assume that the eigenvalues
of $\Theta$ on $H^i_{\dyn} ( \overline{\spec \eo}  , \Rh)$ are distinct
for $i = 0 , 1 , 2$ it follows therefore that
%%\\[-1cm]
\begin{itemize}
\item $H^0_{\dyn} ( \overline{\spec \eo}  , \Rh) = \R$ with trivial action of $\Theta$, i.e. $\Theta = 0$,
\item $H^1_{\dyn} ( \overline{\spec \eo}  , \Rh)$ is infinite dimensional, the spectrum of $\Theta$ consisting of the non-trivial zeroes $\rho$ of $\zeta_K (s)$ with their multiplicities,
\item $H^2_{\dyn} ( \overline{\spec \eo}  , \Rh) \cong \R$ but with $\Theta = \id$.
\item For $i > 2$ the cohomologies $H^i_{\dyn} ( \overline{\spec \eo}  , \Rh)$ should vanish.
\end{itemize}
```

**The Lefschetz/explicit formula with the minus sign on `H^1`** — this is the
supertrace statement the notebook needs. Restricted to `R^{>0}`:
- `math/0505354:main.tex:874-880`
```
Consider a number field $K / \Q$. 
Formula (\ref{eq:20}) restricted to $\R^{> 0}$ implies the following equality of distributions on $\R^{> 0}$:
\begin{eqnarray}
  \label{eq:26}
  \lefteqn{\sum^2_{i=0} (-1)^i \Tr (\phi^* \tei H^i_{\dyn} (\overline{\spec \eo} , \Rh)) = 1 - \sum_{\hat{\zeta}_K (\rho) = 0} e^{t\rho} + e^t } \\
 & = & \sum_{\ep \nmid \infty} \log N\ep \sum^{\infty}_{k=1} \delta_{k \log N \ep} + \sum_{\ep \tei \infty} (1 - e^{\kappa_{\ep} t})^{-1} \; . \nonumber
\end{eqnarray}
```

The general dynamical Lefschetz trace formula it specialises (Deninger's
conjecture, the alternating sum over leafwise cohomology):
- `math/0505354:main.tex:744-752`
```
\begin{conj}
  \label{t5}
For $X , \Fh$ and $\phi$ as above there exists a natural definition of a $\Dh' (\R^{>0})$-valued trace of $\phi^*$ on the reduced leafwise cohomology $\oH^{\hullet} (X,\Rh)$ such that in $\Dh' (\R^{>0})$ we have:
\begin{equation}
  \label{eq:20}
%  \scriptstyle 
\sum\limits^{\dim \Fh}_{n=0} (-1)^n \Tr (\phi^* \tei \oH^n (X,\Rh)) = \sum\limits_{\gamma} l (\gamma) \sum\limits^{\infty}_{k=1} \varepsilon_{\gamma} (k) \delta_{kl (\gamma)} + \sum\limits_x \varepsilon_x |1 - e^{\kappa_x t}|^{-1} \; .
\end{equation}
\end{conj}
```

and the same thing written for an arithmetic scheme with compact supports:
- `math/0505354:main.tex:452-459`
```
In terms of cohomology, the explicit formulas would take the form
\begin{eqnarray}
  \label{eq:9}
  \lefteqn{\sum_i (-1)^i \Tr (\phi^{\ast} \tei H^i_{\dyn, c} ( \eX  , \Rh))_{\diss} } \\ 
  & = & - (\log A_{\eX}) \delta_0 + \sum_{x \in |\eX|} \log N (x) \sum_{k\ge 1} \delta_{k \log N (x)} \nonumber \\
 & & + \sum_{x \in |\eX|} \log N (x) \sum_{k \le -1} N (x)^k \delta_{k \log N (x)} \nonumber  \; .
\end{eqnarray}
Here $A_{\eX}$ is the conductor of $\eX$.
```

**Closed orbits = primes, length `log N p`** (the dictionary table):
- `math/0505354:main.tex:883-889`
```
  \begin{tabular}{llp{8cm}}
$\spec \eo_K \cup \{ \ep \tei \infty \}$ & \quad $\ent$ \quad & $3$-dimensional dynamical system $(X , \phi^t)$ with a one-codimensional foliation $\Fh$ satisfying the conditions of conjecture \ref{t5} \\
finite place $\ep$ & \quad $\ent$ \quad & closed orbit $\gamma = \gamma_{\ep}$ not contained in a leaf and hence transversal to $\Fh$ such that $l (\gamma_{\ep}) = \log N \ep$ and $\varepsilon_{\gamma_{\ep}} (k) = 1$ for all $k \ge 1$.\\
infinite place $\ep$ & \quad $\ent$ \quad & fixed point $x_{\ep}$ such that $\kappa_{x_{\ep}} = \kappa_{\ep}$ and \nolinebreak $\varepsilon_{x_{\ep}} = 1$. \\
$H^i_{\dyn} (\overline{\spec \eo} , \Rh)$ & \quad $\ent$ \quad & $\oH^i (X , \Rh)$
  \end{tabular}
\end{center}
```

The bibliography line that fixes the not-on-arXiv Crelle 1993 reference
(commented out in the source, but verbatim):
- `math/0505354:main.tex:1580`
```
%\bibitem{D5} C. Deninger, Lefschetz trace formulas and explicit formulas in analytic number theory. J. Reine Angew. Math. {\bf 441} (1993), 1--15
```

*Relevance.* A1 is the citation for "the explicit formula is the Lefschetz trace
formula of a graded cohomology with the zeros odd", i.e. for the claim that the
`Z_2`-grading of the notebook's operator is exactly Deninger's `(-1)^i`.

### A2. `1807.06400` — Deninger, *Dynamical systems for arithmetic schemes*

Title/author:
- `1807.06400:main.tex:477-479`
```
\title{Dynamical systems for arithmetic schemes\\
{\large \it  Dedicated to the memory of Jacob Murre}}
\author{Christopher Deninger\footnote{Funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under Germany's Excellence Strategy EXC 2044--390685587, Mathematics M\"unster: Dynamics--Geometry--Structure, the CRC 878 Groups, Geometry \& Actions and the CRC 1442 Geometry: Deformations and Rigidity} }
```

**Closed orbits correspond to primes, of length `log p`:**
- `1807.06400:main.tex:501`
```
A much more basic property would be a correspondence between the periodic orbits $\gamma$ of $(X_0 , \phi^t)$ and the closed points $\ex_0$ of $\eX_0$. Here the length of $\gamma$ should be the logarithm of the norm $N (\ex_0)$ of $\ex_0$. Thus the Hasse--Weil zeta function of $\eX_0$ would be the Ruelle zeta function of $(X_0 , \phi^t)$. In particular, for $\eX_0 = \spec \Z$ the periodic orbits $\gamma$ of $X_0$ should correspond to the prime numbers $p$, the length being $l (\gamma) = \log p$. The conditions on the $\Q^{> 0}$-action on a space $\ceX_0 [\C]$ for this to happen were written down a long time ago in \cite[3.1 and 4.9]{D1}, but for too many years I had no idea how to construct natural $\Q^{> 0}$-spaces realizing these conditions.  
```

*Relevance.* The 2018 paper is where Deninger actually constructs spaces whose
periodic-orbit packets biject with closed points; cite it for "this is still a
live programme, not only a 1998 analogy".

### A3. `0709.2801` — Deninger, *Analogies between analysis on foliated spaces and arithmetic geometry*

The infinitesimal generator `theta` of the flow playing the role of Frobenius:
- `0709.2801:main.tex:445`
```
The groups $\oH^{\hullet}_{\Fh} (X)$ have a smooth linear $\R$-action $\phi^*$ induced by the flow $\phi^t$. The infinitesimal generator $\theta = \lim_{t \to 0} \frac{1}{t} (\phi^{t*} - \id)$ exists on $\oH^{\hullet}_{\Fh} (X)$. It plays a similar role as the Frobenius morphism on \'etale or crystalline cohomology.
```

The Ruelle zeta as an alternating product of regularised determinants over the
leafwise cohomology:
- `0709.2801:main.tex:552-557`
```
  \begin{array}{rcl}
    \zeta_R (s) & := & \dis \prod_{\gamma} (1 - e^{-sl (\gamma)})^{-\varepsilon_{\gamma}} \\
 & = & \dis \prod_i \ddet_{\infty} (s \cdot \id - \theta \tei \oH^i_{\Fh} (X))^{(-1)^{i+1}} \; .
  \end{array}
\end{equation}
Here $\gamma$ runs over the closed orbits, $\varepsilon_{\gamma} = \sgn \det (1 - T_x \phi^{l (\gamma)} \tei T_x \Fh)$ for any $x \in \gamma$, the Euler product converges in some right half plane and $\det_{\infty}$ is the zeta-regularized determinant. The functions $\ddet_{\infty} (s \cdot \id - \theta \tei \oH^i_{\Fh} (X))$ should be entire.
```

The explicit-formula/index-theorem line of the dictionary:
- `0709.2801:main.tex:425`
```
Explicit formulas of analytic number theory & transversal index theorem for $\R$-action on $X$ and Laplacian along the leaves of $\Fh$, c.f. \cite{D3}  \\ \hline
```

### A4. `1307.3851` — Leichtnam, *On the analogy between L-functions and Atiyah–Bott–Lefschetz trace formulas for foliated spaces*

Used in place of the (non-arXiv) "An invitation to Deninger's work". The cleanest
short statement of the whole graded formalism, with `Theta_0 = 0` on `H^0`,
`Theta_2 = Id` on `H^2`, and the **minus sign in front of the `H^1` term**:
- `1307.3851:main.tex:344-361`
```
Deninger's philosophy is motivated by the fact that
the left hand side of \eqref{eq:EF}
$$ \Phi(0)   - \sum_{\rho \in \widehat{\zeta}^{-1}\{0\},\, \Re \rho \geq 0} \Phi(\rho) +
\Phi(1)
$$ is reminiscent of a Lefschetz trace formula of the form
$$
{\rm TR}\, \int_\R \alpha(t) e^{t\, \Theta_0}\,d t - {\rm TR}\, \int_\R \alpha(t) e^{t\, \Theta_1}\, d t  + {\rm TR}\, \int_\R \alpha(t) e^{t\, \Theta_2}\, d t,
$$ where the following  two assumptions should be satisfied.

$\bullet$ 
$\Theta_0=0$ acts on $H^0=\R$, $\Theta_2={\rm Id}$ acts on $H^2=\R$.


$\bullet$$\bullet$ The closed unbounded operator,
$\Theta_1$ acts on an infinite dimensional real vector (pre-Hilbert) space $H^1$ and has discrete spectrum. 
For any  $ \alpha \in C^\infty_{compact} (\R , \R)$ the operator $ \int_\R \alpha(t) e^{t\, \Theta_1}\, d t $  is trace class. The 
eigenvalues of $\Theta_1 \otimes Id_\C$  acting on $H^1\otimes_\R \C$ coincide with the non trivial zeroes of  $\widehat{\zeta}$.

```

and the regularised-determinant formula for the completed `L`-function:
- `1307.3851:main.tex:385-390`
```
the following identity (which Deninger assumes to hold true):
$$
\Lambda (\chi, s) = C \, \frac{ det_\infty ( \frac{ s - \theta_{1, \chi}}{2 \pi}\,: H^1_\chi )}{ det_\infty ( \frac{ s - \theta_{1, \chi}}{2 \pi}\,: H^0_\chi )\, \, 
det_\infty ( \frac{ s - \theta_{1, \chi}}{2 \pi}\,: H^2_\chi ) }\; ,$$
where $C$ is a constant depending on a choice of conventions. (Actually in this particular case, the denominator is identically equal to $1$).

```

*Relevance.* If only one quote is used for "the zeros live in odd degree and
enter the trace with a minus sign", use either `math/0505354:main.tex:874-880`
or `1307.3851:main.tex:344-361`.

---

## B. Connes: zeros as an absorption spectrum, and the minus sign

### B1. `math/9811068` — Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*

Already in the tree (fetched for `notes/extract/weil-positivity-sources.md`; the
trace formula and the Weil-positivity statements are quoted there and are not
repeated here). What follows is the **sign/absorption** material.

The announcement, in the introduction:
- `math/9811068:main.tex:194-209`
```
Frobenius and the Lefchetz formula. The spectral interpretation of the 
zeros of zeta will be as an absorption spectrum, i.e. as missing 
spectral lines. All zeros will play a role in the spectral side of the 
trace formula, but while the critical zeros will appear per-se, the non 
critical ones will appear as resonances and 
enter in the trace formula through their harmonic potential with respect 
to the critical line. Thus the spectral side is entirely canonical, and 
by proving positivity of the Weil distribution, we shall show that its 
equality with the geometric side, i.e. the global trace formula, is 
equivalent to the Riemann Hypothesis for all $L$-functions with 
Gr\"ossencharakter. We shall model our discussion on the Selberg trace 
formula, but it differs from the latter in several important respects. 
We shall first explain in particular why a crucial negative sign in the 
analysis of the statistical fluctuations of the zeros of zeta indicates 
that the spectral interpretation should be as an absorption spectrum, or 
equivalently should be of a cohomological nature. As it turns out, the 
```

The "two mismatches" with the Selberg trace formula, the first being the overall
minus sign:
- `math/9811068:main.tex:469-476`
```
\noindent However there are two important mismatches  (cf.
[B]) between the two formulas (6) and (7). The first one is
the overall {\it minus sign} in front of formula (7), the
second one is that though $2 {\rm sh} \, \left( {m \lb_p
\over 2} \right) \sim p^{m/2}$ when $m \ra \ify$, we do not
have an equality for finite values of $m$.

\smallskip
```

**The resolution of the minus sign by `H^1_et` and the Lefschetz formula, and
the conclusion that the Polya–Hilbert space appears as its negative:**
- `math/9811068:main.tex:556-581`
```
of the Riemann flow and it only aquires an interesting
structure from algebraic geometry. The minus sign which was
problematic in the above discussion admits here a beautiful
resolution since the analogue of the Polya-Hilbert space is
given, if one replaces $\Cb$ by $\Qb_{\ell}$ the field of
$\ell$-adic numbers $\ell \not= p$, by the cohomology group
$$
H_{\rm et}^1 (\bar{\Si} ,\Qb_{\ell}) \leqno (2)
$$
which appears with an overall minus sign in the Lefchetz
formula 
$$
\sum (-1)^j \, \hbox{Trace} \, \varphi^* / H^j = \sum_{\varphi (x) = x} 
\, 1. \leqno (3)
$$
\smallskip

\noindent For the general case this suggests

\medskip\item{(C)} The Polya-Hilbert space $\Hc$ should appear from
its negative  $\ominus \Hc$.

\medskip
\noindent In other words, the spectral interpretation of the zeros 
of the Riemann zeta function should be as an absorption spectrum rather 
than as an emission spectrum, to borrow the language of spectroscopy.
```

And the remark, late in the paper, that Berry–Keating's count is off precisely
because the interpretation is absorption and not emission:
- `math/9811068:main.tex:3037-3040`
```
 which changes appropriately the sign of the term in $E$. What [BK] had 
not 
taken into account is that the spectral interpretation of [Co] is as an 
{ \it absorption spectrum } rather than an emission spectrum.
```

*Relevance.* B1 is the citation for "the zeros are odd/`ominus`, i.e. an
absorption spectrum; the minus sign is cohomological in origin". Note that
Connes credits the resolution to `H^1_et` appearing with `(-1)^j` in the
Grothendieck–Lefschetz formula — the same mechanism as Deninger's `(-1)^i`.

### B2. `2006.13771` — Connes–Consani, *Weil positivity and trace formula, the archimedean place*

Sign of the zero contribution: in the Riemann–Weil explicit formula as they
write it, the sum over the nontrivial zeros enters with a **minus** sign against
the two `+` polar terms `tilde f(0)`, `tilde f(1)`:
- `2006.13771:weil-compo.tex:99-103`
```
It was shown  by A. Weil  \cite{Weil}  that the Riemann Hypothesis (RH) is equivalent to the negativity of the right-hand  side of the Riemann-Weil explicit formula \cite{EB} (Appendix~\ref{appendix2}: \eqref{bombieriexplicit}) 
\begin{equation}\label{explicit form}
\tilde f(0)-\sum_{\rho\in Z}\tilde f(\rho)+\tilde f(1)=\sum_v {\mathcal W}_v(f), \qquad  \tilde f(s):=\int_0^\infty f(x)x^{s-1}dx
\end{equation}
 where $Z$ is the multi-set of non-trivial zeros of the Riemann zeta function and for a precise class of complex-valued test functions on the positive half-line, of the form 
```

The same paper states the absorption/emission relation explicitly:
- `2006.13771:weil-compo.tex:113`
```
 In \cite{scalingH} we explained  the relation between the simplest instance of the semi-local operator theoretic framework-- the case of the single archimedean place-- and the so-called Berry-Keating Hamiltonian. We showed that if one removes from the ``white light" the absorption spectrum (as in \cite{Co-zeta}) one obtains  the emission spectrum (as suggested  in \cite{BKe0,BKe}), thus proving that there is no mismatch in the semiclassical approximations.  We also noticed (see \cite{scalingH} Figures 5 and 6) that there is a single ``quantum cell" arising from the absorption spectrum that was not accounted for by the cutoff suggested in  \cite{BKe0,BKe}. The  basic problem posed by the choice of the cutoff of \cite{BKe0,BKe} is its lack of invariance under the scaling action  $\rep$ introduced in \cite{Co-zeta},  as the one-parameter group generated by the scaling Hamiltonian giving the spectral realization of the zeros of the Riemann zeta function. This issue  makes problematic restricting the Hamiltonian. On the other hand, there is straightforward interpretation of this cutoff in terms of   the orthogonal projection $\bf S$ of the Hilbert space $L^2(\R)_{\rm ev}$ of square integrable even functions on the subspace of functions, which, together with their Fourier transform, vanish identically in the interval $[-1,1]$. This subspace is the well-known infinite dimensional Sonin's space  whose discovery  goes back to the work of N. Y. Sonin in the XIX-th century \cite{Sonin}. Even though the scaling action $\rep$ does not restrict to this subspace, one can associate to a test function $f\in C_c^\infty(\R_+^*)$ the trace $\Tr(\rep(f)\, {\bf S})$, and one sees that this functional is positive definite by construction, since when evaluated on $f=g*g^*$ it is the trace $\Tr(\rep(g)\, {\bf S}\,\rep(g)^*)$  of a positive operator. 
```

*Relevance.* B2 gives, in one displayed equation, the sign pattern the notebook
reads as a supertrace: `(+1)` on the two one-dimensional pieces, `(-1)` on the
zeros.

---

## C. Fermionic matrix product states: graded bonds, supertrace, parity insertion

### C1. `1610.07849` — Bultinck, Williamson, Haegeman, Verstraete, *Fermionic Matrix Product States and One-Dimensional Topological Phases*

**Definition of the super vector space and the graded tensor product** (the
Koszul sign `(-1)^{|i||j|}`):
- `1610.07849:FermionicMPS.tex:104-118`
```
To construct fermionic matrix product states we will make use of super vector spaces. In this section we introduce the relevant concepts and present the notation to be used in following sections. A super vector space $V$ has a natural direct sum decomposition
\begin{equation}
V = V^0\oplus V^1\, ,
\end{equation}
where we refer to vectors in $V^0 (V^1)$ as even (odd) parity vectors. Vectors that have a definite parity are called homogeneous. We denote the parity of a homogeneous basis state $|i\rangle$ by $|i|\in \{0,1\}$. The tensor product of two homogeneous vectors $|i\rangle$ and $|j\rangle$ is again a homogeneous vector, and its parity is given by $|i|+|j|$ mod 2. In other words, $V$ and the associated operation of taking tensor products is $\mathbb{Z}_2$ graded. We will denote the graded tensor product as
\begin{equation}
|i\rangle \otimesg|j\rangle \in V\otimesg V\, .
\end{equation}
The key relation between super vector spaces and fermionic degrees of freedom is the following canonical graded tensor product isomorphism
\begin{align}\label{reordering}
\mathcal{F}:& V\otimesg W \rightarrow W\otimesg V \nonumber \\
 & |i\rangle\otimesg|j\rangle \rightarrow (-1)^{|i||j|}|j\rangle\otimesg|i\rangle
\end{align}
The canonical isomorphism $\mathcal{F}$ is the crucial ingredient of super vector spaces and it shows why even (odd) parity vectors can be interpreted as having even (odd) fermion number. 

```

**The supertrace, and the fact that the ordinary trace is recovered only by
inserting the fermion parity operator** — this is the exact statement the
notebook needs:
- `1610.07849:FermionicMPS.tex:128-138`
```
\mathcal{C}:V^*\otimesg V \rightarrow \mathbb{C}: \langle \psi |\otimes_{\mathfrak{g}} |\phi\rangle \rightarrow \langle \psi|\phi\rangle\, ,
\end{equation}
and in particular $\mathcal{C}(\bra{j} \otimesg \ket{i}) = \delta_{i,j}$. Applying the contraction of $V^*$ and $V$ in a more general tensor product involving several super vector spaces requires that we first apply $\mathcal{F}$ so as to isolate $V^*\otimesg V$. Still denoting this combined reordering and contraction as $\mathcal{C}$, we obtain for example the famous supertrace
\begin{equation}
\mathcal{C}(\ket{i} \otimesg \bra{j}) = (-1)^{|i||j|} \mathcal{C}(\bra{j} \otimesg \ket{i}) = (-1)^{|i|} \delta_{i,j}.	
\end{equation}
To obtain the normal trace, we need to include the fermion parity operator $\sum_{k} (-1)^{|k|} \ket{k} \otimesg \bra{k}$ so that we indeed obtain
\begin{equation}
\mathcal{C}(\sum_{k} (-1)^{|k|} \ket{k} \otimesg \bra{k} \otimesg\ket{i} \otimesg \bra{j}) = (-1)^{|i|} \mathcal{C}(\ket{i} \otimesg \bra{j}) = \delta_{i,j}.	
\end{equation}
The contraction map also defines the canonical isomorphism $(V\otimesg W)^* \simeq W^* \otimesg V^*$, as indeed we have $\mathcal{C}(\bra{j'}\otimesg \bra{i'} \otimesg \ket{i} \otimesg \ket{j} = \delta_{i',i} \delta_{j',j}$.
```

**Even-parity fMPS on a ring: the coefficients are `tr(P A^{i_1} ... A^{i_N})`
with `P` the parity matrix** (i.e. the periodic-boundary contraction of even
graded tensors is a supertrace of the bond matrices):
- `1610.07849:FermionicMPS.tex:217-232`
```
where we can apply the contraction trivially in order to obtain
\begin{equation}
|\psi\rangle_{e} = \sum_{\{i\}} \text{tr}\left(\mathcal{P} A^{i_1}A^{i_2}\dots A^{i_N} \right) |i_1\rangle |i_2\rangle \dots |i_N\rangle\,.
\end{equation}
Here, we introduced the parity matrix $\mathcal{P}$
\begin{equation}\label{eq:parity}
\mathcal{P} = \left( \begin{matrix} \mathds{1} & 0 \\ 0 &  -\mathds{1}  \end{matrix}\right)\,
\end{equation}
which has the defining property
\begin{equation}\label{eq:parityproperty}
\mathcal{P}A^{i} = \left( -1\right)^{|i|}A^{i}\mathcal{P}\, ,
\end{equation}
because we started from even tensors $\mathsf{A}$. The resulting fMPS $|\psi\rangle_e$, being the contraction of these even tensors, has even fermion parity, as indicated by the subscript. One sees that the coefficients of the fMPS satisfy
\begin{displaymath}
\text{tr}\left(\mathcal{P} A_e^{i_1}A_e^{i_2}\dots A_e^{i_N}\right) = \left(-1 \right)^{|i_1|}\text{tr}\left(\mathcal{P} A_e^{i_2}A_e^{i_3}\dots A_e^{i_1}\right)\, ,
\end{displaymath}
```

**Odd-parity (Kitaev/Majorana) fMPS on a ring: an extra odd tensor `Y` in the
trace**:
- `1610.07849:FermionicMPS.tex:236-244`
```
Because the fMPS tensors $\mathsf{A}$ are even, a fMPS with odd fermion parity is obtained by adding one additional tensor with odd parity and no physical component to the tensor network. We choose $\mathsf{Y} = \sum_{\alpha,\beta} Y_{\alpha,\beta} |\alpha)_N \otimesg (\beta|_1$ with $Y_{\alpha,\beta}=0$ if $|\alpha|+|\beta|\mod 2 = 0 $.
Evaluating $\ket{\psi}_o = \mathcal{C}_v\left(\mathsf{Y} \otimesg \mathsf{A}[1] \otimesg \mathsf{A}[2]\otimesg \cdots \otimesg \mathsf{A}[N]\right)$ using the same steps as in the previous subsection results in
\begin{equation}\label{oddfMPS}
|\psi\rangle_{o} = \sum_{\{i\}} \text{tr}\left(Y A^{i_1}A^{i_2}\dots A^{i_N} \right) |i_1\rangle |i_2\rangle \dots |i_N\rangle\,.
\end{equation}
If we require this state to be invariant under translations then, as shown in appendix \ref{app:translation}, it should hold that
\begin{displaymath}
\text{tr}\left(Y A^{i_1}A^{i_2}\dots A^{i_N} \right) =  \text{tr}\left(Y A^{i_2}A^{i_3}\dots A^{i_1} \right)\, ,
\end{displaymath}
```

with `Y` the odd matrix commuting with all `A^i`:
- `1610.07849:FermionicMPS.tex:258-267`
```
\begin{equation}
Y = \left(\begin{matrix} 0 & \mathds{1} \\ -\mathds{1} & 0 \end{matrix} \right) = y\otimes \mathds{1}\, .
\end{equation}
\end{subequations}
We will comment on the generality of this choice in the next section.

Let us now look at what happens when we define the fMPS with odd fermion parity on a chain with open boundary conditions. We will do this by looking at a particular example, namely the Kitaev chain for spinless fermions, which is described by the Hamiltonian \cite{Kitaev1}
\begin{equation} \label{KitaevChain}
H_{\text{Kitaev}} = -i\sum_{j = 1}^N\gamma_{2j}\gamma_{2j+1}\, ,
\end{equation}
```

and the Kitaev-chain example, whose `A^1` *is* `Y = y`:
- `1610.07849:FermionicMPS.tex:276-282`
```
\end{equation}
to an arbitrary state with odd fermion parity (acting with these projectors on an even parity state gives zero). The matrices of the fMPS ground state are:
\begin{eqnarray}\label{Kitaevchain}
A^0 & = & \left(\begin{matrix}1 & 0 \\ 0 & 1 \end{matrix}\right) \\
A^1  & = & Y = y =  \left(\begin{matrix}0 & 1 \\ -1 & 0 \end{matrix}\right) \, ,
\end{eqnarray}
which is indeed a special case of the general structure given in equations \eqref{oddalgebra}. Starting from the expression
```

The classification statement tying the two cases to the two simple `Z_2`-graded
algebras:
- `1610.07849:FermionicMPS.tex:352`
```
The two types of simple $\mathbb{Z}_2$ graded algebras, which are called even and odd type, correspond to fMPS with even or odd fermion parity respectively under periodic boundary conditions. For this reason we henceforth refer to these two types of irreducible fMPS as even algebra and odd algebra fMPS respectively. As explained in the previous section, odd algebra fMPS have the physical property of Majorana edge modes on a chain with open boundary conditions. 
```

*Relevance.* C1 supplies (i) graded bonds, (ii) `sTr` vs `Tr` differing by the
parity insertion `P`, (iii) the two sectors — even algebra (bond `P`) and odd
algebra (bond `Y`) — which is the fMPS shadow of the notebook's even/odd split.
The footnote making the point again for reduced density matrices:
- `1610.07849:FermionicMPS.tex:543`
```
The reduced density matrix of subsystem $A$ is then defined as \footnote{$\rho_A$ is a positive matrix obtained from tracing out the degrees of freedom in region $B$, starting from $|\psi\rangle\langle\psi|$. Note that in this fermionic setting, tracing is not obtained by simply contracting using $\mathcal{C}$, as the latter gives rise to the supertrace as discussed in Section~\ref{sec:super}. Instead, we first have to apply the corresponding parity operator.}
```

---

## D. Continuous matrix product states

### D1. `1002.1824` — Verstraete, Cirac, *Continuous Matrix Product States for Quantum Fields*

**The norm and expectation values, and the transfer operator
`T = Q (x) 1 + 1 (x) conj(Q) + R (x) conj(R)`:**
- `1002.1824:mpsQFT4.tex:62-69`
```
With the help of this definition, it is straightforward to express the norm and expectation value of operators in terms of the matrices $R$ and $Q$.
For the sake of simplicity, we will consider a bosonic system and assume translational invariance. Note that for inhomogeneous systems one can proceed in a very similar way. Using the commutation relations of the field operators one readily finds $\langle\chi|\chi\rangle = {\rm Tr} \left(e^{T L}\right)$ and
 \begin{eqnarray}
 \langle\hat{\psi}(x)^\dagger \hat{\psi}(x) \rangle &=& {\rm Tr} \left[e^{T L} (R\otimes \bar R)\right],\nonumber \\
 \langle \hat{\psi}(x)^\dagger \hat{\psi}(0)^\dagger\hat{\psi}(0) \hat{\psi}(x) \rangle &=& {\rm Tr} \left[e^{T (L-x)} (R\otimes \bar R)e^{Tx} (R\otimes \bar R) \right],\nonumber \\
 \langle\hat{\psi}(x)^\dagger\left[-\frac{d^2}{dx^2}\right] \hat{\psi}(x) \rangle &=& {\rm Tr} \left[e^{T L} ([Q,R]\otimes [\bar Q,\bar R])\right],\nonumber
 \end{eqnarray}
where $T=Q\otimes\openone + \openone\otimes \bar Q + R\otimes \bar R$ (the bar indicates complex conjugation).  The state $|\chi\rangle$ is invariant under the ''gauge'' transformation $Q\to XQX^{-1}$, $R\to XRX^{-1}$ for arbitrary invertible $X$. This allows us to fix a gauge by imposing $Q+Q^\dagger + R^\dagger R =0$, so that we can write
```

**`T` as a Lindbladian:** after the gauge fixing `Q = -R^dag R/2 - iH`, the
superoperator form of `T` generates a Lindblad master equation, and its spectrum
has non-positive real part:
- `1002.1824:mpsQFT4.tex:69-73`
```
where $T=Q\otimes\openone + \openone\otimes \bar Q + R\otimes \bar R$ (the bar indicates complex conjugation).  The state $|\chi\rangle$ is invariant under the ''gauge'' transformation $Q\to XQX^{-1}$, $R\to XRX^{-1}$ for arbitrary invertible $X$. This allows us to fix a gauge by imposing $Q+Q^\dagger + R^\dagger R =0$, so that we can write
\[ Q=-\frac{1}{2} R^\dagger R - i H \]
where $H=H^\dagger$ and $R^\dagger R$ is diagonal. Making the transformation $X\otimes \bar Y |a,b\rangle \to X|a\rangle\langle \bar b|Y^\dagger$, $T$ is transformed into a superoperator $\tilde T$ (mapping matrices into matrices), and we obtain that $\rho(x):=e^{\tilde Tx} \rho$ satisfies a master equation in the Lindblad form
 \[ \frac{d}{dx}\rho(x) =  -i [\tilde H,\rho(x)] + R\rho(x)R^\dagger - \frac{1}{2}\left[R^\dagger R ,\rho(x)\right]_+.\]
As a consequence,  all eigenvalues of ${\tilde T}$ have a non-positive real part, which implies that all the above quantities are well behaved in the thermodynamical limit $L\to\infty$. In a generic case, the master equation will have a unique steady state $\rho_{ss}\geq 0$, which can be chosen with unit trace. In such a case, the above expressions considerable simplify in the thermodynamic limit, since $\langle\chi|\chi\rangle={\rm Tr}(\rho_{ss})=1$,
```

**The fixed point is the half-line reduced density matrix / entanglement
spectrum:**
- `1002.1824:mpsQFT4.tex:81`
```
In the case of a system with open boundary conditions, the eigenvalues of the matrix $\rho(x)$ would exactly correspond to the squares of the Schmidt coefficients when considering a bipartition at site $x$. This can in its turn be used to calculate the entanglement entropy of the reduced density matrices defined on given intervals.
```

### D2. `1211.3935` — Haegeman, Cirac, Osborne, Verstraete, *Calculus of continuous matrix product states*

**The local transfer operator, in the general (multi-species) form:**
- `1211.3935:calculus.tex:376-379`
```
From the expression above, we can deduce that in the computation of expectation values ($Q'=Q$, $R_\alpha'=R_\alpha$) a central role is played by the local transfer matrix $\voperator{T}(x)$ defined as 
\begin{equation}
\voperator{T}(x)=Q(x)\otimes \one_{D}+\one_{D}\otimes \overline{Q(x)} + \sum_{\alpha=1}^{N} R_{\alpha}(x)\otimes \overline{R_{\alpha}(x)}.\label{eq:transferoperator}
\end{equation}
```

**Lindblad form of the transfer operator** (and the remark that it is trace
preserving, i.e. `T~(1) = 0`):
- `1211.3935:calculus.tex:419-425`
```
\end{align}
From the correspondence with completely positive maps, it can be shown that the solution $l(x)$ and $r(x)$ of Eq.~\eqref{eq:virtualdensitymatrix} starting from positive definite initial conditions $l(-L/2)$ and $r(+L/2)$ are positive for any $x\in\mathcal{R}$ (see Theorem~3 in Ref.~\onlinecite{1976CMaPh..48..119L}). The norm is thus guaranteed to be positive. Note that, for the special parameterization of $Q(x)$ in the continuous measurement interpretation [Eq.~\eqref{eq:qunitary}], we can write the determining differential equation for $r(x)$ as
\begin{multline}
\frac{\d\ }{\d x}r(x)=-\mathscr{T}^{(x)}\big(r(x)\big)=\\
-\ic [K(x), r(x)] -\frac{1}{2}\sum_{\alpha=1}^{N} \{R_{\alpha}(x)^{\dagger}R_{\alpha}(x),r(x)\} +\sum_{\alpha=1}^{N}R_{\alpha}(x) r(x) R_{\alpha}(x)^{\dagger}.
\end{multline}
This is a master equation in Lindblad form \cite{1976CMaPh..48..119L} describing the non-equilibrium Markov dynamics of the ancilla (\textit{i.e.} the cavity). Starting from a pure state $r(L/2)=\bm{v}_{\mathrm{R}}\bm{v}_{\mathrm{R}}^{\dagger}$ at $t=-x=-L/2$, it evolves through interaction with the physical system (via the interaction operators $R_{\alpha}$). At a general time $t=-x$, the density matrix $r(x)$ is no longer pure: non-equilibrium evolution is a dissipative process. Note that the evolution is trace preserving, since tracing the equation above results in $\d \tr[r(x)] /\d x=0$. In addition, the corresponding map $\widetilde{\mathscr{T}}^{(x)}$ satisfies $\widetilde{\mathscr{T}}^{(x)}(\one_{D})=0$.
```

**Fermionic cMPS.** This paper *does* have the fermionic case. The `Z_2` parity
operator on the physical side, and the requirement that it be implemented by a
virtual `P` on the bond:
- `1211.3935:calculus.tex:315-319`
```
We conclude this subsection by investigating what else can be learned from the physical considerations concerning particle statistics. The regularity conditions [Eq.~\eqref{eq:regcondition}] already require that the matrices $R_{\alpha}$ behave as the corresponding operators $\hpsi_{\alpha}$ in terms of commutation and anticommutation relations. In a physical system, we should not have fermionic condensates, \textit{i.e.} $\braket{\Psi|\hpsi_{\alpha}(x)|\Psi}=0$ if particle species $\alpha$ is fermionic. This is a consequence of the invariance of an physical Hamiltonian $\ham$ under the action of the parity operator $\operator{P}$, which flips the sign of any fermionic operator ($\operator{P}\hpsi_{\alpha}(x)\operator{P}=\eta_{\alpha,\alpha}\hpsi_{\alpha}(x)$) and is thus idempotent ($\operator{P}=\operator{P}^{-1}=\operator{P}^{\dagger}$). We can construct $\operator{P}$ as
\begin{equation}
\operator{P}=\exp\left[\ic \pi \sum_{\alpha\ \text{fermionic}} \operator{N}_{\alpha}\right]=\exp\left[\ic \pi \sum_{\alpha\ \text{fermionic}} \int_{\mset{R}} \d x\, \hpsid_{\alpha}(x)\hpsi_{\alpha}(x)\right].
\end{equation}
Physical states satisfy $\operator{P}\ket{\Psi}=\ec^{\ic \phi} \ket{\Psi}$, where the idempotence of $\operator{P}$ requires $\phi=0$ or $\phi=\pi$. Physical states thus consist completely of a superposition of states, all of which have either an even or an odd number of fermions. Imposing this same property for cMPS requires one to explicitly incorporate the $\mathbb{Z}_{2}$ symmetry (with group elements $\{\operator{\one},\operator{P}\}$) in the matrix structure of $R_{\alpha}$ and $Q$. Since $\operator{P}\ket{\Psi[Q,\{R_{\alpha}\}]}=\ket{\Psi[Q,\{\eta_{\alpha,\alpha} R_{\alpha}\}]}$, we should also be able to define a virtual operator $P\in\End(\mathbb{C}^{D})$ such that $P Q P^{-1}=Q$ and $P R_{\alpha} P^{-1} =\eta_{\alpha,\alpha} R_{\alpha}$. This operator can in principle be $x$-dependent, but we should then be able to apply a local gauge transformation (see Section~\ref{s:gauge}) in order to make $P$ space-independent. In addition, it is clear from the definition that $P$ is idempotent ($P=P^{-1}$). If we can assume that $P$ is diagonalizable, then $P$ divides the ancilla space $\mathbb{C}^{D}$ into a sector with positive parity (eigenspace of eigenvalue $+1$) and a sector with negative parity (eigenspace of $-1$). A global gauge transformation brings $P$ into the diagonal form
```

the resulting block structure of `Q` and `R_alpha` (block diagonal for bosons,
**block off-diagonal for fermions**) and the parity-graded boundary matrix `B`:
- `1211.3935:calculus.tex:320-336`
```
\begin{equation}
P=\begin{bmatrix} \one_{D^{(+)}} & 0_{D^{(+)}\times D^{(-)}} \\ 0_{D^{(-)}\times D^{(+)}} & -\one_{D^{(-)}}\end{bmatrix}
\end{equation}
with $D^{(+)}+D^{(-)}=D$. The required transformation behavior of $Q$ and $R_{\alpha}$ then imposes the following decomposition
\begin{align}
Q&=\begin{bmatrix} Q^{(+)} & 0_{D^{(+)}\times D^{(-)}} \\ 0_{D^{(-)}\times D^{(+)}} & Q^{(-)}\end{bmatrix},\\
R_{\alpha}&=\begin{bmatrix} R_{\alpha}^{(+)} & 0_{D^{(+)}\times D^{(-)}} \\ 0_{D^{(-)}\times D^{(-)}} & R_{\alpha}^{(-)} \end{bmatrix}\qquad \text{(particle species $\alpha$ is bosonic)},\\
R_{\alpha}&=\begin{bmatrix} 0_{D^{(+)}\times D^{(+)}} & R_{\alpha}^{(+-)} \\ R_{\alpha}^{(-+)} & 0_{D^{(-)}\times D^{(-)}}\end{bmatrix}\qquad \text{(particle species $\alpha$ is fermionic)}.
\end{align}
In the cMPS $\ket{\Psi[Q,\{R_{\alpha}\}]}$, all contributions with either an even or an odd number of fermions in Eq.~\eqref{eq:cmpsfockembedding} drop out, depending on the boundary matrices $B$. If only states with an even number of fermions are allowed, $B$ should have a decomposition as
\begin{align}
B&=\begin{bmatrix} B^{(+)} & 0_{D^{(+)}\times D^{(-)}} \\ 0_{D^{(-)}\times D^{(+)}} & B^{(-)}\end{bmatrix},
\end{align}
whereas a decomposition of the form
\begin{align}
B&=\begin{bmatrix} 0_{D^{(+)}\times D^{(+)}} & B_{\alpha}^{(+-)} \\ B_{\alpha}^{(-+)} & 0_{D^{(-)}\times D^{(-)}}\end{bmatrix}\end{align}
is required to select only states with an odd number of fermions.
```

the parity superoperator commuting with the transfer operator:
- `1211.3935:calculus.tex:591`
```
By imposing the physical requirements discussed at the end of Section~\ref{s:regularity}, we can define the parity superoperator $\voperator{P}$ as in Section~\ref{s:expectval}. Since $\voperator{P}\voperator{T}\voperator{P}=\voperator{T}$, we can expect that the left and right eigenvectors $\rket{l}$ and $\rket{r}$ corresponding to the zero eigenvalue satisfy $\rbra{l}\voperator{P}=\rbra{l}$ and $\voperator{P}\rket{r}=\rket{r}$, or thus $P^{\dagger} l P = l$ and $P r P^{\dagger}=r$. Note that we can always choose the gauge such that $P$ is Hermitian. In addition, it is easy to prove that $\voperator{T}_{\alpha}$ also has an eigenvalue zero even if $\alpha$ refers to a fermionic particle species so that $\voperator{T}_{\alpha}\neq \voperator{T}$. The corresponding left and right eigenvectors are in that case given by $l_{\alpha}=l P=P^{\dagger} l$ and $r_{\alpha} =P r=r P^{\dagger}$, whereas they equal $l$ and $r$ if $\alpha$ is a bosonic particle.
```

and the uniform/translation-invariant transfer operator with its fixed point,
including the periodic-boundary case `B = 1_D`:
- `1211.3935:calculus.tex:577`
```
When using cMPS to approximate ground states of translation invariant Hamiltonians, we can restrict to the subclass of uniform cMPS $\ket{\Psi(Q,\{R_{\alpha}\})}$, which are obtained from taking $Q(x)=Q$ and $R_{\alpha}(x)=R_{\alpha}$ constant $x$-independent $D\times D$ matrices in $\ket{\Psi[Q,\{R_{\alpha}\}]}$. This approach is valid both for a finite system with periodic boundary conditions ($B=\one_{D}$) or for a system in the thermodynamic limit ($\lvert\mset{R}\rvert=L\to \infty$ or thus $\mset{R}\to \mathbb{R}$), where the precise value of the boundary matrix $B$ should be irrelevant and should not appear in any normalised expectation value. We henceforth restrict to the latter case. The transfer operator $\voperator{T}=Q\otimes 1_{D}+1_{D}\otimes\overline{Q}+\sum_{\alpha=1}^{q} R_{\alpha}\otimes\overline{R}_{\alpha}$ also becomes translation invariant and $\Pexp[\int_{y}^{z}\d x\, \voperator{T}]=\exp[\voperator{T}(z-y)]$. The normalization of the state $\ket{\Psi(Q,R)}$ is given by $\lim_{L\to\infty}\tr\big[(B\otimes\overline{B})\exp(\voperator{T} L)\big]$. If $\mu=\max_{\lambda\in\sigma(\voperator{T})}\{\Re(\lambda)\}$, where $\sigma(\voperator{T})$ denotes the spectrum of $\voperator{T}$ and $\Re$ the real part, then $\braket{\Psi(\overline{Q},\{\overline{R}_{\alpha}\})|\Psi(Q,\{R_{\alpha}\})}\sim \lim_{L\to\infty} \exp(\mu L)$. Normalizing this state by multiplying it with $\exp(-\mu L)$ results in $Q\leftarrow Q-\mu/2 \one_{D}$ and $\voperator{T}\leftarrow \voperator{T}-\mu \voperator{\one}$, so that the new transfer operator $\voperator{T}$ has at least one eigenvalue for which the real part is zero and no eigenvalue has a positive real part. Let us assume that the eigenvalue $\lambda$ with $\Re \lambda=0$ is unique. If $\rket{r}$ is the corresponding right eigenvector, then we can write the eigenvalue equation as $\mathscr{T}(r)=\lambda r$ with $r$ the associated virtual density matrix. Hermitian conjugation learns that $\mathscr{T}(r^{\dagger})=\overline{\lambda} r^{\dagger}$, so that the uniqueness of the eigenvalue with $\Re \lambda=0$ implies that $\lambda=\overline{\lambda}=0$ and $r^{\dagger}=\ec^{\ic \phi} r$, where we can choose the phase of the eigenvector so that $r$ is Hermitian. Similarly, the virtual density matrix $l$ associated to the left eigenvector $\rket{l}$ can also be chosen Hermitian. 
```

*Relevance.* D1 + D2 give exactly the cMPS ingredients the section needs: `Q, R`;
`T` as a Lindbladian; the fixed point of `T` = the half-chain reduced density
matrix (entanglement spectrum); and, crucially, the fact that the **fermionic**
cMPS is already in the literature with the same `Z_2`-graded bond structure
(even = block-diagonal `B`, odd = block-off-diagonal `B`) as the fMPS `P` / `Y`
of section C. The notebook's "graded bond with a supertrace in PBC" is therefore
*not* new as a tensor-network construction; what is proposed as new is the
arithmetic reading of it.

---

## E. The Weil representation over finite fields

### E1. `math/0610818` — Gurevich, Hadani, *The Geometric Weil Representation*

**(i) The characterisation by the intertwining (Egorov) relation with the
Heisenberg/Weyl operators, and the fact that it determines `rho(g)` up to a
scalar:**
- `math/0610818:main.tex:414-429`
```
irreducible one. Let $\pi $ be the Heisenberg representation associated with
a central character $\psi $. Invoking Theorem \ref{SVN}, we conclude that
for every element $g\in G$ we have%
\begin{equation*}
\pi ^{g}\simeq \pi .
\end{equation*}%
Denote by $\rho (g):\mathcal{H\longrightarrow H}$ an intertwiner which
realizes this isomorphism$.$ Equivalently, this means that $\rho (g)$
satisfies and in fact is determined up to scalar by the following equation

\begin{equation}
\rho (g)\pi (h)\rho (g)^{-1}=\pi (g\cdot h),  \label{Egorov2}
\end{equation}%
for every $g\in G.$

The above equation are sometimes referred to in the literature as the Egorov
```

Their character formula for the Weil representation on the subset `U` (elements
with `g+I` invertible):
- `math/0610818:main.tex:604-616`
```
\begin{theorem}[Character formulas]
\label{CF}The character $ch_{\tau \text{ }}$of the Heisenberg-Weil
representation $\tau $ when restricted to the subset $U\times H$ is given by 
\begin{equation*}
ch_{\tau }(g,v,z)=\tfrac{\mathfrak{e}^{2N}}{q^{N}}\sigma (\det (\kappa
(g)+I))\psi (\tfrac{1}{4}\omega (\kappa (g)v,v)+z),
\end{equation*}%
and the character $ch_{\rho \text{ }}$of the Weil representation $\rho $
when restricted to the subset $U$ is given by 
\begin{equation*}
ch_{\rho }(g)=\tfrac{\mathfrak{e}^{2N}}{q^{N}}\sigma (\det (\kappa (g)+I)).
\end{equation*}
\end{theorem}
```

### E2. `math/0610644` — T. Thomas, *The Character of the Weil Representation*

**(ii) The character formula over a finite field.** With `gamma` the (unit
modulus) normalised Gauss sum, this gives `|Tr rho(g)|^2 = |F|^{dim ker(g-1)}`:
- `math/0610644:ArxivThomasWeil3.tex:187-198`
```
Given $g\in\Sp(V)$, the endomorphism $(g-1)\in\End(V)$ plays a key role in the formula for $\Tr\rho(g)$ (cf. \cite{GH} \S2.1 and \cite{Howe} p. 294). Let us denote by $\sigma_g$ the induced isomorphism
\begin{equation*}\sigma_g\colon V/\ker(g-1)\overset\sim\too (g-1)V.\end{equation*}
It is easy to check that $v\otimes w\mapsto\<\sigma_g v,w\>$ defines a nondegenerate bilinear form on $V/\ker(g-1)$. 
Let $\det\sigma_g\in F^\times/(F^\times)^2$ be its discriminant (see \S\ref{orient}); if $(g-1)$ is invertible then $\det\sigma_g$ is just the usual determinant $\det(g-1)$ mod $(F^\times)^2$.

The second ingredient we need is the `Weil index,' a character $\gamma$ of the Witt group $W(F)$ of quadratic forms over $F$ (see \S\ref{WittWeil} and \cite{We},  \cite{Pe}).  If $a\in F^\times$ then denote by $\gamma(a)$ the value of $\gamma$ on the one-dimensional quadratic form $x\mapsto ax^2$.  In this finite field case,
\begin{equation*}\gamma(a)=|F|^{-1/2}\sum_{x\in F}\psi(\tfrac12ax^2).\end{equation*}
It depends only on $a\bmod(F^\times)^2.$
\begin{theorem1a*}\label{THM1A} If $F$ is a finite field,  then
\begin{equation*}\Tr\rho(g)=|F|^{\tfrac12\dim\ker(g-1)}\gamma(1)^{\dim V-\dim\ker(g-1)-1}\gamma(\det\sigma_g).\end{equation*}
\end{theorem1a*}

```

The remark that the absolute value alone follows from `rho (x) rho^*` being the
permutation action on `L^2(V)` — i.e. the `|Tr W(g)|^2 = q^{dim ker(g-1)}`
statement in its Howe form:
- `math/0610644:ArxivThomasWeil3.tex:202-203`
```
\begin{remnum} \label{remHowe} R. Howe \cite{Howe} understood many aspects of Theorem 1A without, apparently, finding a closed formula. For example, one can determine the absolute value of $\Tr\rho(g)$ from the fact that $\rho\otimes\rho^*$ is the natural action of $\Sp(V)$ on $L^2(V)$.
\end{remnum}
```

### E3. `quant-ph/0602001` — D. Gross, *Hudson's Theorem for finite-dimensional quantum systems*

**(iii) The Clifford/Weil correspondence in quantum-information language**: the
metaplectic operator is characterised by conjugating Weyl operators according to
the symplectic matrix.
- `quant-ph/0602001:poswig.tex:504-545`
```
\begin{theorem} \emph{(Structure of the Clifford group)}
	\label{thCliffordStructure}
	\begin{enumerate}
		\item
		For any symplectic $S$, there is a unitary operator
		$\mu(S)$ such that
		\begin{equation*}
			\mu(S)\,w(v)\,\mu(S)^\dagger = w(S\,v).
		\end{equation*}

		\item
		$\mu$ is a \emph{projective representation} of the symplectic
		group, that is
		\begin{equation*}
			\mu(S)\mu(T)=e^{i \phi} \mu(ST)
		\end{equation*}
		for some phase factor $e^{i\phi}$.

		%\item
		%The effect of conjugating a Weyl operator $w(p,q)$ by another
		%one $w(p',q')$ is given by
		%\begin{equation*}
			%w(p',q')\,w(p,q)\,w(p',q')^\dagger = w(p,q,2^{-1}\Symp p,q,p',q'.).
		%\end{equation*}

		\item
		\label{cliffordDecomposition}
		Up to a phase, any Clifford operation is of the form
		\begin{equation*}
			U=w(a)\mu(S)
		\end{equation*}
		for a suitable $a\in V$ and symplectic $S$.
	\end{enumerate}
\end{theorem}

The representation $\mu$ is called the \emph{Weil} or
\emph{metaplectic} representation \cite{weil,folland}.  Theorem
\ref{thCliffordStructure} is could be called a discrete version of the
celebrated \emph{Stone-von Neumann Theorem} \cite{folland}. Its proof
is not essential for understanding the further argument and has
therefore been moved to Appendix \ref{scCliffordProof}.

```

### E4. `quant-ph/0412001` — D. M. Appleby, *SIC-POVMs and the Extended Clifford Group*

The same correspondence with the explicit `SL(2, Z_d)` labelling used for odd
`d`:
- `quant-ph/0412001:main.tex:396-409`
```
We then have
\begin{lemma}
\label{lem:CliffordStructure1}
For each unitary operator $\hat{U}\in\C(d)$ there exists a  matrix $F\in
\SL(2,\mathbb{Z}_{\overline{d}})$  and  a vector
$\boldsymbol{\chi}\in (\mathbb{Z}_d)^2$ such that
\begin{equation}
 \hat{U} \hat{D}_{\mathbf{p}} \hat{U}^{\dagger}
= \omega^{\langle \boldsymbol{\chi}, F\mathbf{p}\rangle} \hat{D}_{F\mathbf{p}}
\end{equation}
for all $\mathbf{p}\in\mathbb{Z}^2$ (where $\omega = \tau^2=e^{2 \pi i/d}$, as
before).
\label{lem:FChiToAisSurjective}
\end{lemma}
```

*Relevance.* E1–E4 justify "the Artin–Schreier transfer matrix is a Clifford /
Weil-representation operator": E1 gives the defining intertwining relation,
E2 the character (hence `|Tr|^2 = q^{dim ker(g-1)}`, which is the point count),
E3/E4 the dictionary to the stabiliser/Clifford group over odd prime dimension.

---

## F. Stickelberger's discriminant theorem and self-dual normal bases

### F1. `2208.06138` — Auel, Biesel, Voight, *Stickelberger's discriminant theorem for algebras*

**Honest caveat.** This arXiv paper is about the *other* statement that goes by
"Stickelberger's discriminant theorem", namely `disc Z_K = 0, 1 (mod 4)`:
- `2208.06138:main.tex:219-225`
```
\begin{theorem}[Stickelberger]
We have $\disc \Z_K \equiv 0,1 \pmod{4}$.
\end{theorem}

This theorem is called \emph{Stickelberger's discriminant theorem}, among other names.  While never stated explicitly in
Stickelberger's work \cite{stickelberger:discriminant}, this statement can be deduced from the main
results.  The modern simple proof given by Schur \cite{schur:stickelberger} is typically provided as an exercise in an algebraic number theory class (see e.g.\ Marcus \cite[Chapter 2, Exercise 22]{Marcus:nf} or Neukirch \cite[Section I.2, Exercise~7]{neukirch}).  For further discussion, see Remark \ref{rmk:PNPN}; and for more on this history, see Cox \cite{cox:stickelberger}.  (There is a different, much deeper, theorem of Stickelberger in algebraic number theory that describes the Galois module structure of class groups of cyclotomic fields.  For more on this theorem, see Washington \cite[Chapter 6]{Washington}.)  Various generalizations of this congruence have also been made \cite{martinet:discriminant,berlekamp:discriminant,baeza:discriminant,harrer,biesel_gioia:discriminant}.
```

What is directly useful is the standard proof it recalls, which is exactly the
even/odd permutation split of the square root of the discriminant — i.e. the
`A_n` mechanism in matrix form:
- `2208.06138:main.tex:867-890`
```
\begin{rmk} \label{rmk:PNPN}
  Let $K$ be a number field with ring of integers $\Z_K$ and integral
  basis $\alpha_1,\dots,\alpha_n$.  Letting
  $\sigma_1,\dots,\sigma_n \colon K \hookrightarrow \C$ be the
  distinct embeddings of $K$ into $\C$, we consider the $n \times n$
  matrix of complex numbers $E \colonequals (\sigma_i(\alpha_j))_{i,j}$.  Then
  $B = E^\matT E$ (see Marcus \cite[Theorem 6]{Marcus:nf}) and so $\disc \Z_K = \det(B) = \det(E)^2$.  
  (The definition in \eqref{eqn:BTralp} has the virtue that it expresses the discriminant as the determinant of a matrix of integers.)
   
  Letting $P$ and $N$ be the sum
  of terms in the expansion of $\det(E)$ involving even and odd
  permutations, respectively, the standard proof of Stickelberger's
  discriminant theorem is to write
  \begin{equation}
   \disc \Z_K = \det(\sigma_i(\alpha_j))_{i,j}^2 = (P-N)^2 =
    (P+N)^2-4PN; 
    \end{equation}
    by construction, the elements $P+N,PN$ are algebraic integers, and
    by Galois theory they belong to $\Q$, hence $P+N,PN \in \Z$
    and the result follows.  With this in mind, a natural square
  root of the discriminant modulo 4 is $P+N$, which is equal to the
  \emph{permanent} of the matrix $E$.    
  This permanent agrees with the 
  discriminant pfaffian modulo $2$ by Theorem \ref{thm-dpf}.
```

**The statement the notebook actually wants** — *`disc` of a degree-`n`
separable extension is a square in the base field iff the Galois group is
contained in `A_n`; hence for `F_{q^n}/F_q` with `q` odd, `disc` is a square iff
`n` is odd* (because `Gal` is cyclic generated by the `n`-cycle Frobenius, whose
sign is `(-1)^{n-1}`) — was **not found stated verbatim in any arXiv TeX
source**. Record as textbook:

- K. Conrad, *Galois groups of cubics and quartics (not in characteristic 2)*,
  expository notes, Proposition 1 (disc is a square iff `Gal ⊆ A_n`).
- N. Jacobson, *Basic Algebra I*, 2nd ed., §4.15; or D. Dummit, R. Foote,
  *Abstract Algebra*, 3rd ed., §14.6.
- For the finite-field specialisation, the sign of the Frobenius `n`-cycle acting
  on the `n` conjugates is `sgn = (-1)^{n-1}`, so the discriminant of
  `F_{q^n}/F_q` (`q` odd) is a square iff `n` is odd.

### F2. `1007.4899` — Arnault, Pickett, Vinatier, *Construction of self-dual normal bases and their complexity*

**The Lempel–Weinberger existence criterion, verbatim:**
- `1007.4899:selfdualnb_elsart6.tex:258-271`
```
We now describe our work more precisely. First we recall the 
necessary and sufficient conditions for the existence of self-dual normal bases
\cite{LempelWeinberger}:  
\begin{ithm}[Lempel-Weinberger]
\label{SDNBexistence}
The extension of finite fields $\F_{q^n}/\F_q$ has a self-dual normal
basis if and only if 
either the degree~$n$ is odd or $n\equiv2$ modulo~4 and $q$ is even.
%one of the following conditions holds:
%\begin{enumerate}[(i)]
%\item the degree~$n$ is odd;
%\item $n\equiv2$ modulo~4 and $q$ is even.
%\end{enumerate}
\end{ithm}
```

*Relevance.* F2 is the independent confirmation of the parity pattern: a
self-dual normal basis of `F_{q^n}/F_q` exists iff `n` is odd (for odd `q`), the
same `n`-odd condition as square discriminant. This is the "even-`n` sign" the
Artin–Schreier section attributes to Stickelberger.

---

## G. Lidskii's trace theorem, and Landau's theorem

### G1. `1105.2914` — Reinov, Latif, *Grothendieck–Lidskii theorem for subspaces and factor spaces of `L_p`-spaces*

**Lidskii's theorem stated verbatim in the introduction:**
- `1105.2914:main.tex:115-122`
```
 In 1955, A. Grothendieck [1] has shown that if the linear operator $T$
in a Banach space  is $2/3$-nuclear then
the trace of $T$ is well defined and is equal to the sum of all  eigenvalues $\{\mu_k(T)\}$
of $T.$  \,
V.B. Lidski\v{\i} [2], in 1959, proved his famous theorem on the coincidence of the trace of the $S_1$-operator
in an (infinite dimensional) Hilbert space
 with its spectral trace $\sum_{k=1}^\infty \mu_k(T).$
  Any Banach space is a subspace of an $L_\infty(\nu)$-space, as well as any Hilbert space
```

Their own theorem, whose `p = 2, s = 1` case *is* Lidskii, and which spells out
"eigenvalues written according to their algebraic multiplicities":
- `1105.2914:main.tex:225-240`
```
  {\bf Theorem.}\
Let $Y$ be a subspace or a factor space of  an $L_p$-space,
$1\le p\le \infty.$ If $T\in N_s(Y,Y),$\,
$1/s=1+|1/2-1/p|,$   \,
then

1.\, the (nuclear) trace  of $T$ is well defined,

2.\, $\sum_{n=1}^\infty |\la_n(T)|<\infty,$ where
$\{\la_n(T)\}$ is the system of all eigenvalues of the operator $T$
(written in according to their algebraic multiplicities)

and
$$
 \tr T= \sum_{n=1}^\infty \la_n(T).
$$
```

### G2. `1303.4792` — Delgado, Ruzhansky, *`L^p`-Nuclearity, traces, and Grothendieck–Lidskii formula on compact Lie groups*

A second verbatim statement:
- `1303.4792:main.tex:283-288`
```
In the setting of Hilbert spaces the class of $r$-nuclear operators agrees with the Schatten-von 
Neumann ideal of order $r$, a result due to R. Oloff (cf. \cite{Oloff:pnorm}). 
When $r=\frac23$, Grothendieck proved (cf. {\cite{gro:me}) that the trace in Banach spaces
agrees with the sum of all the 
eigenvalues with multiplicities counted. In Hilbert spaces this holds for nuclear (i.e. trace class) operators, 
the result which is known as the Lidskii formula (cf. {\cite{li:formula}). 
```

Textbook reference for the same: B. Simon, *Trace Ideals and Their Applications*,
2nd ed., AMS (2005), Theorem 3.7.

*Relevance.* G1/G2 supply the "no ungraded trace-class operator" step: if `X` is
trace class then `Tr X^l = sum_j mu_j^l` with algebraic multiplicities, so the
trace sequence of a genus `>= 1` curve — which has `#X(F_{q^l}) = q^l + 1 -
sum alpha_i^l` with `2g` terms of modulus `q^{1/2}` entering *negatively* —
cannot be realised without a grading.

### G3. `1009.0228` — Maurizi, *Extending Landau's Theorem on Dirichlet Series with Non-Negative Coefficients*

**Landau's theorem stated verbatim:**
- `1009.0228:main.tex:173-179`
```
Specifically, we are interested in extending the following theorem of Landau (we will find it convenient to translate and assume $\sigma_a = 0$ for all functions we consider):

\begin{theorem}[E. Landau \cite{Landau_Handbuch}]\label{thm_Landau}

Suppose that $f(s)= \sum a_n n^{-s}$ has abscissa of absolute convergence equal to $0$.  If $a_n \in \mathbb{R}, a_n \ge 0$ for all $n$ then $f$ does not extend holomorphically to a neighborhood of $s = 0$.

\end{theorem}
```

Textbook reference for the Laplace-transform form (singularity at the abscissa of
convergence for a positive measure): D. V. Widder, *The Laplace Transform*,
Princeton Univ. Press (1941), Ch. II, Theorem 5b.

---

## H. Gauss sums of quadratic forms over `F_q`

No arXiv source was found that states the Lidl–Niederreiter form
`sum_x psi(Q(x)) = q^{n-r} eta(det Q_nd) g(psi)^r` literally. The equivalent
statement, in normalised (Weil-index) form, **is** in `math/0610644`:
- `math/0610644:ArxivThomasWeil3.tex:375-382`
```
\subsection{Integral Formulas.}

First suppose $F$ is finite. We allow here the case when $q$ may be degenerate on $A$. Then to define $\gamma(q)$ one should consider $q$ as a nondegenerate form on $A/\ker q$.
\begin{prop} \label{pg1}  Let $q$ be a possibly degenerate quadratic form on $A$. Then 
\begin{equation*}\gamma(q)=|F|^{-\tfrac12(\dim A/\ker q)-\dim\ker q}\sum_{x\in A} \psi(\tfrac12q(x,x)).\end{equation*}
\end{prop}
\begin{proof} If $\ker q=0$ then the right side is just $(f_q\,dq)^\wedge$, evaluated at $0$. In general, use that $f_q$ is constant along the cosets of $\ker q$ in $A$.
\end{proof}
```

together with the evaluation of `gamma` on a one-dimensional form (the classical
quadratic Gauss sum, normalised by `q^{-1/2}`):
- `math/0610644:ArxivThomasWeil3.tex:192-195`
```
The second ingredient we need is the `Weil index,' a character $\gamma$ of the Witt group $W(F)$ of quadratic forms over $F$ (see \S\ref{WittWeil} and \cite{We},  \cite{Pe}).  If $a\in F^\times$ then denote by $\gamma(a)$ the value of $\gamma$ on the one-dimensional quadratic form $x\mapsto ax^2$.  In this finite field case,
\begin{equation*}\gamma(a)=|F|^{-1/2}\sum_{x\in F}\psi(\tfrac12ax^2).\end{equation*}
It depends only on $a\bmod(F^\times)^2.$
\begin{theorem1a*}\label{THM1A} If $F$ is a finite field,  then
```

and the multiplicativity / discriminant reduction that turns a general form into
`gamma(1)^{dim-1} gamma(det q)`:
- `math/0610644:ArxivThomasWeil3.tex:359-372`
```
\begin{prop}\label{pd}There exists a number $\gamma(q)$ such that
\begin{equation}\label{eqg}
(f_{q}\,dq)^\wedge=\gamma(q)\cdot f_{-q^*}\end{equation}
  as generalized functions on $A^*$. Moreover, $(A,q)\mapsto\gamma(q)$ is a (unitary) character $W(F)\to\CCC^\times$. 
If $a\in F^\times$ then denote by $\gamma(a)$ the value of $\gamma$ on the one-dimensional quadratic form $x\mapsto ax^2$. Then:
\begin{enumerate}
\item[(i)] For $a\in F^\times$, $\gamma(a)$ depends only on $a\bmod(F^\times)^2$.
\item[(ii)] $\gamma(a)\gamma(b)=\pm\gamma(1) \gamma(ab)$ for all $a,b\in F^\times$, with a plus if $F$ is finite or complex.
\item[(iii)] For a quadratic space $(A,q)$, $\gamma(q)=\pm\gamma(1)^{\dim A-1}\gamma(\det q)$, with a plus when $F$ is finite or complex; here $\det q$ is the discriminant of $q$.
\end{enumerate}
\end{prop}

To be precise, in (ii) the sign is the Hilbert symbol $(a,b)$: $(a,b)=1$ if $a$ is a norm from $F[\sqrt b]$, and $(a,b)=-1$ otherwise.  In (iii) the sign is the Hasse invariant of $q$. 

```

*Relevance.* Reading Proposition `pg1` backwards gives exactly the target
identity: for a possibly degenerate `q` on `A` with `r = dim A/ker q`,
`sum_{x in A} psi(q(x,x)/2) = |F|^{r/2 + dim ker q} gamma(q)` and
`gamma(q) = gamma(1)^{r-1} gamma(det q)` with
`gamma(a) = |F|^{-1/2} sum_x psi(a x^2 /2)` the normalised Gauss sum; so
`gamma(1)^2 = eta(-1)` and the `q^{n-r}` prefactor is `|F|^{dim ker q}`.
Textbook alternative: R. Lidl, H. Niederreiter, *Finite Fields*, 2nd ed., CUP
(1997), Theorems 6.26 and 6.27.

---

## I. Bost–Connes: the KMS classification

Bost–Connes 1995 (Selecta Math. 1(3), 411–457) is **not on arXiv**. Nothing in
`refs/src` quoted it before this note. The theorem is stated in full in
Connes–Marcolli, *From Physics to Number Theory via Noncommutative Geometry,
Part I*, **arXiv:math/0404128**:
- `math/0404128:houcheschapter1final7.tex:1815-1849`
```
\n We can now state the basic result that gives content to the
relation between phase transition and arithmetic (BC \cite{BC}):

\begin{thm}\label{BCthm}
\begin{enumerate}
\item  For $0 < \beta \leqq 1$ there exists a unique ${\rm KMS}_{\beta}$
state $\varphi_{\beta}$ for the above system. Its restriction to
$R_\Q=\Q[{\mathbb Q} / {\mathbb Z}] \subset {\mathcal A}$ is given by
\begin{equation}\label{BC-KMS01}
\varphi_{\beta} \left( e(a/b) \right) = b^{-\beta}
\prod_{p \, {\rm prime,} \, p \mid b} \left( \frac{1 - p^{\beta -
1}}{1 - p^{-1}}
\right) \, .
\end{equation}
\item  For $\beta > 1$ the extreme ${\rm KMS}_{\beta}$ states are
parameterized by embeddings $\rho \,:{\mathbb Q}^{ab} \to {\mathbb C}$ and
\begin{equation}\label{BC-KMS1}
\varphi_{\beta , \rho} \left( e(a/b) \right) = Z (\beta)^{-1}
\sum_{n=1}^{\infty} n^{-\beta} \rho \left( \zeta^n_{a/b} \right)
\, ,
\end{equation}
where the partition function $Z(\beta)=\zeta(\beta)$ is the
Riemann zeta function.
\item  For $\beta = \infty$, the Galois group ${\rm Gal}
(\overline{\mathbb Q} / {\mathbb Q})$ acts by  composition on
${\mathcal E}_{\infty}$. The action factors through the abelianization
${\rm Gal}({\mathbb Q}^{ab} / {\mathbb Q})$, and the class field theory
isomorphism $\theta\,: G\to  {\rm Gal}({\mathbb Q}^{ab} / {\mathbb Q})$
intertwines the actions,
$$
\alpha \circ \varphi = \varphi \circ \theta^{-1}(\alpha)\,, \qquad \alpha
\in {\rm Gal} ({\mathbb Q}^{ab} / {\mathbb Q}) \, .
$$
\end{enumerate}
\end{thm}
```

The dictionary table in the same paper, which pairs the critical temperature with
the **absorption spectrum** reading of the zeros and labels the BC system
type `III_1`:
- `math/0404128:houcheschapter1final7.tex:688-695`
```
\GL_n(\A)$ \\[2mm]
\hline & \\
System at critical temperature & Spectral realization \\
 (Riemann's $\zeta$ as partition function) & (Zeros
of $\zeta$ as absorption spectrum)
\\[2mm] \hline & \\
Type III$_1$ & Type II$_\infty$ \\[2mm]
\hline
```

and the bibliographic entry fixing the not-on-arXiv original:
- `math/0404128:houcheschapter1final7.tex:850-853`
```
\bibitem[Bost--C]{0BC} J.B.~Bost, A.~Connes, {\em Hecke algebras, Type III
factors and phase transitions with spontaneous symmetry breaking
in number theory}, Selecta Math. (New Series) Vol.1 (1995) N.3,
411--457.
```

*Relevance.* I is the citation for "unique KMS state for `0 < beta <= 1`,
Gibbs/extremal states parameterised by `Q^ab -> C` with partition function
`zeta(beta)` for `beta > 1`". **Caveat to record honestly:** `math/0404128`
states the uniqueness and the `beta > 1` classification, and it labels the system
`Type III_1` in the dictionary table at line 694, but it does **not** in these
passages prove or restate the type-`III_1` factor claim; for that, cite the
Bost–Connes original (whose very title asserts it).

---

## Summary of the three load-bearing quotes

1. **Deninger, graded/Lefschetz** — `math/0505354:main.tex:874-880`; the
   displayed equation itself is lines 878–879:
   `\sum^2_{i=0} (-1)^i \Tr (\phi^* \tei H^i_{\dyn} (\overline{\spec \eo} , \Rh)) = 1 - \sum_{\hat{\zeta}_K (\rho) = 0} e^{t\rho} + e^t`.
2. **Connes, absorption sign** — `math/9811068:main.tex:556-581`; the core is
   lines 575–581 (`the Polya-Hilbert space $\Hc$ should appear from its negative
   $\ominus \Hc$` ... `should be as an absorption spectrum rather than as an
   emission spectrum`).
3. **fMPS supertrace** — `1610.07849:FermionicMPS.tex:128-138`; the supertrace
   equation is line 132 and the parity-insertion equation is line 136.
