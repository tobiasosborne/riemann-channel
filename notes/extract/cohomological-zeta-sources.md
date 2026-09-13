# Sources for the cohomological / graded ("fermionic") reading of zeta zeros and poles

Written 2026-09-13 by the source-acquisition worker, in the style of
`notes/extract/selberg-sources.md`. Every quote below was copied out of the
arXiv **TeX source** in `refs/src/<id>/` and is cited as
`<id>:<file>:<line-range>`; each quote is whole and contiguous in the lines
stated, so it can be re-checked with `sed -n '<a>,<b>p'`. Preference throughout:
TeX source, never PDF text. **All 87 quotes in this file were machine-verified
byte-for-byte against the source files after writing** (a small script that
re-reads every `<id>:<file>:<a>,<b>` block and diffs it against
`sed -n '<a>,<b>p'`; 0 mismatches). Sources that are not on arXiv are recorded as
bibliographic data only, wherever possible **byte-cited out of the bibliography
of an arXiv paper that is in the tree**, so that even the bibliographic claim is
re-checkable.

Question being grounded (HANDOFF "CENTRAL PRIORITY", forced consequence): the
notebook's picture is that the zeta zeros are an ODD (fermionic) sector, the
pole an EVEN sector, and the zeta a supertrace; for graphs the Ihara zeta is
`1/[(1-u^2)^{-chi} det(1 - Au + qu^2)]` with `chi = V - E`. We want (i) the
literature on the alternating/graded structure over degree, (ii) the
order-of-vanishing and torsion statements, (iii) graph analogues, (iv)
fermionic/Grassmann proofs of the determinant identities, (v) the quantum side.

## New arXiv ids fetched for this note

`2104.00215 1709.06052 0706.1509 2307.03321`

(SHA-256 of the main TeX file, for the manifest:
`2104.00215/Ihara_zeta_function_and_twisted_Alexander_invariants.tex`
`1d869a7d0f4917ae344e6860fb207db87dd56640e568679f792d50aa87f31674`;
`1709.06052/2018_KW_JSP__Nov1.tex`
`2353e04b76b68ae066b5346f6786db6f1381be6da1b1d45365071d385f132491`;
`0706.1509/hyper_v4b.tex`
`e2f91916a0e706d2fc3479ced1b57664f39ce3de4717928161ce7737f96413fa`;
`2307.03321/main.tex`
`717b1c979e134d085ddb5431f8537759e29f7b4afb4953a65b52f326d109a227`.)

**Already in `refs/src` and reused, not re-fetched:** `dg-ga/9511006`,
`1606.04560`, `1807.01189`, `2009.08558`, `1602.00664`, `2303.11226`,
`2607.21262`, `0809.1401`, `0809.1401v1`, `0809.3479`, `0809.3481`,
`2501.08803`, `math/9806037`, `math/0306396`, `cond-mat/0403271`,
`2201.09412`, `2310.15619`, `2503.19641`, `2405.04361`, `1706.00851`,
`1103.0605`, `1507.01194`, `1701.00154`, `1605.02664`, `1712.02526`,
`1702.05452`, `1804.08028`, `2602.15180`, `2204.06424`, `math/0505354`,
`math/9811068`.

**Re-fetch confirmations requested by the orchestrator:** `2602.15180/main.tex`
is now 1862 lines (was empty) — read and extracted in §F1;
`2204.06424/main.tex` is now 2342 lines (was empty) — it is the Matsuura–Ohta
Kazakov–Migdal/Ihara paper already recorded as prior art in
`notes/prior-art-quantum-ihara.md`, not re-extracted here.

---

# A. The alternating product over form degree (continuous side)

## A1. `dg-ga/9511006` — Deitmar, *Geometric zeta-functions of locally symmetric spaces*

Title and author:

- `dg-ga/9511006:main.tex:98` — `\Title{Geometric zeta-functions of locally symmetric spaces}`
- `dg-ga/9511006:main.tex:101` — `\Author{Anton Deitmar} `

**The explicit statement that the intended output is a Deligne-type alternating
product** (this is the single most quotable line for the notebook's analogy):

- `dg-ga/9511006:main.tex:269`
```
We express the vanishing order of the zeta function in terms of nilpotent Lie algebra cohomology, thereby proving the generalized Riemann hypothesis for the zeta function and a determinant formula similar to the determinant formula of Deligne expressing the Hasse-Weil zeta function as an alternating product of determinants of the Frobenius-action on \'etale cohomology. 
```

**The determinant formula itself — a regularised determinant of `H + s` on the
virtual (super) space `\bigoplus_p (-1)^p V_p`, raised to `(-1)^{dim N}`:**

- `dg-ga/9511006:main.tex:864,871`
```
\begin{proposition} \label{detformel}
Assume $\tau$ is invariant under $w$, then
the zeta function satisfies a determinant formula, i.e.:
$$
Z_{P,\tau ,\ph}(s) \= e^{Q(s)} \det 
\left( H+s\left|\bigoplus_p (-1)^pV_p\right.\right)^{(-1)^{\dim (N)}} ,
$$
where $Q$ is a polynomial of degree $\leq \dim G +\dim N$.
```

**The Ruelle zeta as an alternating product of Selberg-type zetas indexed by
exterior power `\wedge^l n` (i.e. by form degree):**

- `dg-ga/9511006:main.tex:1153,1168`
```
\begin{theorem}
Let $\Ga$ be neat and choose a parabolic $P$ of splitrank one. For $\Re(s)>>0$ define the zeta function
$$
Z_{P,\ph}^R(s) \= \prod_{[\ga]\in {\cal E}_H^p(\Ga)} \det\left(\begin{array}{c}1-e^{-sl_\ga}\ph(\ga)\end{array}\right)^{\chi_{_1}(X_\ga)},
$$
then $Z_{P,\ph}^R(s)$ extends to a meromorphic function on $\C$. In the case that there is only one positive root $\alpha$ in the root system of $(\a ,\g)$ we have 
$$
Z_{P,\ph}^R(s) \= \prod_{l=0}^{\dim N} Z_{P,\sigma_l,\ph}(s+l|\alpha |)^{(-1)^l},
$$
where $\sigma_l$ is the representation of $K_M$ on $\wedge^l \n$.
If we have two positive roots, say $\alpha$ and $2{\alpha}$, then we have ${\n} = {\n}_r \oplus {\n}_I$ where ${\n}_r$ has dimension one and $a$ acts on ${\n}_r$ by $a^{2\alpha}$ and on ${\n}_I$ by $a^{2{\alpha}}$.
Then it follows
$$
Z_{P,\ph}^R(s) \= \prod_{l=0}^{\dim N-1} \left( \frac{Z_{P,\wedge^l{\n}_I,\ph}(s+l|\alpha |)}{Z_{P,\wedge^l{\n}_I\otimes {\n}_r,\ph}(s+(l+2)|\alpha |)}\right)^{(-1)^l}. 
$$
\end{theorem}
```

**The vanishing-order theorem — the order of the zeta at a point is a weighted
Euler characteristic `chi_1` of group cohomology, i.e. an alternating sum:**

- `dg-ga/9511006:main.tex:1194,1212`
```
The cohomology $H^p(\Ga ,H_{\sigma ,\nu}^{max} \otimes V_\ph)$ is finite dimensional for all $p\geq 0$ and the vanishing order of the zeta function
$Z_{P,\sigma ,\ph}$ is
\begin{eqnarray*}
\ord_{s=\nu(H_1)}Z_{P,\sigma ,\ph}(s+|\rho_0|)
&\=& \chi_{_1}(\Ga ,H_{\sigma ,{-\nu}}^{max} \otimes V_\ph)\\ 
&\=& - \sum_{p=0}^\infty p(-1)^p
\dim\ H^p(\Ga ,H_{\sigma ,{-\nu}}^{max} \otimes V_\ph)
\end{eqnarray*}
if $\nu \neq 0$ and
\begin{eqnarray*}
\ord_{s=0}Z_{P,\sigma ,\ph}(s+|\rho_0|) 
&\=& \chi_{_1}(\Ga ,\hat{H}_{\sigma,0}^{max}\otimes V_\ph)\\
&\=& -\sum_{p=0}^\infty p(-1)^p \dim\
H^p(\Ga ,\hat{H}_{\sigma ,0}^{max}\otimes V_\ph),
\end{eqnarray*}
where $\hat{H}_{\sigma ,0}^{max}$ is a certain nontrivial extension of $H_{\sigma ,0}^{max}$ with itself.

Further $\chi (\Ga ,H_{\sigma ,\nu}^{max}\otimes V_\ph)=\sum_p(-1)^p\dim\ H^p(\Ga ,H_{\sigma ,\nu}^{max} \otimes V_\ph)$ always vanishes.
\end{theorem}
```
(The definition of the *higher* Euler number `chi_r` is at
`dg-ga/9511006:main.tex:506,509`
```
Let $h^j(X_\ga)$ denote the j-th Betti number of $X_\ga$ then for $r\ge 0$ we define the higher Euler number of $X_\ga$ as
$$
\chi_{_r}(X_\ga) := \sum_{j=0}^{\dim X_\ga} (-1)^{j+r} \binom{j}{r} h^j(X_\ga),
$$
```
.) Note the last sentence: the *ordinary* Euler characteristic vanishes
identically, so the zeta's divisor is governed by the **weighted** (degree-`p`)
alternating sum, not the plain supertrace.

Deitmar also records, byte-citably, that the higher-rank continuation was first
obtained by **supersymmetry** arguments (Moscovici–Stanton):

- `dg-ga/9511006:main.tex:254,259`
```
The case of higher rank seemed impenetrable until H. Moscovici and R. Stanton 
\cite{MS-tors} used supersymmetry arguments to compute traces of certain 
linear combinations of heat operators. 
This made it possible for them to 
get the continuation of the Ruelle zeta function in the cases $SL_3(\R)$ and $SO(p,q)$ with $pq$ odd. The Ruelle zeta function is a rational 
function in some Selberg zeta functions. Their method was generalized in 
```

*Plain summary.* Deitmar builds geometric (Selberg-type) zeta functions for
locally symmetric spaces of arbitrary rank, and the answer is a **virtual/graded
object**: the divisor of the zeta is read off nilpotent Lie-algebra cohomology,
the determinant formula is a determinant over the virtual space
`\bigoplus_p (-1)^p V_p` to the power `(-1)^{dim N}`, and the Ruelle zeta is
literally an alternating product `\prod_l Z_{\wedge^l n}(s + l|alpha|)^{(-1)^l}`
over exterior degree. He himself names the analogy: this is "a determinant
formula similar to the determinant formula of Deligne expressing the Hasse–Weil
zeta function as an alternating product of determinants of the Frobenius-action
on étale cohomology". This is the continuous prototype of the notebook's
supertrace picture, and it is stated as such in the source.

## A2. `1606.04560` — Dyatlov–Zworski, *Ruelle zeta function at zero for surfaces*

(The task named `1606.04569`; the correct id, and the one in the tree, is
`1606.04560`.)

Title and authors:

- `1606.04560:zazi.tex:14,21`
```
\title[Ruelle zeta function]%
{Ruelle zeta function at zero for surfaces}
\author{Semyon Dyatlov}
\email{dyatlov@math.mit.edu}
\address{Department of Mathematics, Massachusetts Institute of Technology,
 Cambridge, MA 02139}
\author{Maciej Zworski}
\email{zworski@math.berkeley.edu}
```

**Order of vanishing = `-chi(Sigma)`, for any negatively curved oriented
surface:**

- `1606.04560:zazi.tex:59,62`
```
Thanks to the Selberg trace formula the order of vanishing of $ \zeta_R ( s ) $
at $ 0$ has been known for a long time 
in the case of {\em constant curvature} and it is given by $ - \chi ( \Sigma ) $ where $ \chi ( \Sigma ) $ is the Euler characteristic. We show that the 
same result remains true for {\em any} negatively curved oriented surface:
```

- `1606.04560:zazi.tex:68,77`
```
{\bf Theorem.} \emph{ Let $ \zeta_R ( s ) $ be the Ruelle zeta
function for an oriented negatively curved $C^\infty$ Riemannian surface
$ ( \Sigma, g ) $ and 
let $ \chi ( \Sigma ) $ be its
Euler characteristic.
Then $s^{\chi(\Sigma)}\zeta_R(s)$ is holomorphic at $s=0$ and
\begin{equation}
\label{eq:t1}
s^{\chi(\Sigma)}\zeta_R(s)|_{s=0}\neq 0.
\end{equation}
```

**The grading by form degree — the mechanism. `zeta_1` (ODD, 1-forms) is the
NUMERATOR; `zeta_0`, `zeta_2` (EVEN) the DENOMINATOR:**

- `1606.04560:zazi.tex:843,855`
```
for the meromorphic continuation of $\zeta_R$:
$$
\zeta_R(s)={\zeta_1(s )\over \zeta_0( s )\zeta_2(s  )},\quad
s\in\mathbb C.
$$
(It is here that we the assumption that the stable and unstable bundle are orientable.)
Here each $\zeta_k(s )$ is an entire function having a zero of multiplicity
$m_k( i s )$ at each $ s \in\mathbb C$. Therefore, $\zeta_R(s )$ has a zero at
$s =0$ of multiplicity
\begin{equation}
  \label{e:mul-ultimate}
m_R(0):=m_1(0)-m_0(0)-m_2(0).
\end{equation}
```

The `zeta_k` are built from the Lie derivative on `iota_X`-horizontal `k`-forms:

- `1606.04560:zazi.tex:823,828`
```
For $k=0,1,2$, let $\Omega^k_0\subset\Omega^k$ be the bundle of exterior $k$-forms $\mathbf u$
on $M$ such that $\iota_X \mathbf u=0$.
Consider the following operator satisfying~\eqref{e:principal-part}:
$$
\mathbf P_k:=-i\mathcal L_X:\mathcal D'(M;\Omega^k_0)\to\mathcal D'(M;\Omega^k_0).
$$
```

**The degree-by-degree count (`1` in degrees 0 and 2, `b_1` in degree 1):**

- `1606.04560:zazi.tex:877,885`
```
\begin{prop}
\label{l:main}
In the notation of \eqref{eq:Resk} we have
\begin{enumerate}
\item $\dim\Res_0(0)=\dim\Res_2(0)=1$;
\item $\dim\Res_1(0)$ is equal to the Betti number $\mathbf b_1(M)$ defined in~\eqref{e:Betti};
\item the condition~\eqref{e:algsim} holds for $k=0,1,2$.
\end{enumerate}
\end{prop}
```

**Fried's constant-curvature result being generalised:**

- `1606.04560:zazi.tex:121,126`
```
see for instance \cite[Theorem~5]{Mark} for a self-contained presentation. 
In this case the behaviour at $ s = 0 $ was analysed by Fried \cite[Corollary 2]{Fr1}
who showed that 
\begin{equation}
\label{eq:fried}    \zeta_R ( s ) = \pm ( 2 \pi s )^{ |\chi ( \Sigma )| } ( 1 + \mathcal O ( s ) ), \end{equation}
where $ \chi ( \Sigma ) $ is the Euler characteristic of $ \Sigma $. A far reaching
```

*Plain summary.* This is the cleanest instance of exactly the notebook's picture
in the continuous world. The Ruelle zeta of a surface's geodesic flow is a
**quotient**: the odd sector (1-forms) upstairs, the even sectors (0- and
2-forms) downstairs, so the order of vanishing is the supertrace-like alternating
count `m_1 - m_0 - m_2`. The even sectors contribute `1` each (a "pole"/vacuum
sector of dimension one), the odd sector contributes `b_1(M)`. The answer,
`-chi(Sigma)`, is purely topological. If one transcribes to the notebook's
language: the pole/fixed point is even and one-dimensional, the interesting
modes are odd and counted by `H^1`.

## A3. `1807.01189` — Dang–Guillarmou–Rivière–Shen, *The Fried conjecture in small dimensions*

Title and authors:

- `1807.01189:main.tex:140,157`
```
\title[The Fried conjecture in small dimensions]{The Fried conjecture in small dimensions}

\author[N.V.~Dang]{Nguyen Viet Dang}


\address{Institut Camille Jordan (U.M.R. CNRS 5208), Universit\'e Claude Bernard Lyon 1, B\^atiment Braconnier, 43, boulevard du 11 novembre 1918, 
69622 Villeurbanne Cedex }

\email{dang@math.univ-lyon1.fr}


\author[C.~Guillarmou]{Colin Guillarmou}

\address{CNRS, Universit\'e Paris-Sud, D\'epartement de Math\'ematiques, 91400
Orsay, France}
\email{cguillar@math.cnrs.fr}

\author[G.~Rivi\`ere]{Gabriel Rivi\`ere}
```
(The fourth author, Shen, is declared further down the same author block.)

**Fried's theorem: `|zeta(0)^{(-1)^{n_0}}| = tau_rho`, the Ray–Singer /
Reidemeister torsion, and Fried's own reading of it as a Lefschetz formula:**

- `1807.01189:main.tex:229,236`
```
Fried showed that $\zeta_{X,\rho}(\la)$ extends meromorphically to $\la\in \cc$ using Selberg trace formula~\cite{FriedAnnENS} and the work or Ruelle~\cite{Rue}. 
Then he proved~\cite{FrInv} the remarkable formula (with $\dim(\ml{M})=2n_0+1$)~:
\begin{equation}\label{friedhyp}
|\zeta_{X,\rho}(0)^{(-1)^{n_0}}|=\tau_\rho(\ml{M}),
\end{equation}
where $\rho$ is the lift to $\pi_1(\ml{M})$ of an acyclic and unitary representation $\rho_0:\pi_1(M)\rightarrow U(\cc^r)$. Fried 
interpreted this formula as an analogue of the Lefschetz fixed point formula answering his own question in the case of geodesic flows~\cite[p.~441]{Fr0}~: 
\emph{is there a general connection between the analytic torsion of Ray and Singer and closed orbits of some flow (e.g. geodesic flow) ?}
```

**The main theorem in dimension 3:**

- `1807.01189:main.tex:271,278`
```
\begin{theo}\label{t:maintheo2} 
Suppose that $\operatorname{dim}(\ml{M})=3$ and let $E$ be a smooth Hermitian vector bundle with a flat connection $\nabla$ inducing a unitary and acyclic 
representation $\rho:\pi_1(\mc{M})\to U(\cc^r)$.
Let $X_0$ be a smooth Anosov vector field preserving a smooth volume form.
Then, there is a nonempty neighborhood $\mc{U}(X_0)\subset C^\infty(\mc{M};T\mc{M})$ of $X_0$ so that 
\[ \forall X\in \mc{U}(X_0), \quad \zeta_{X,\rho}(0)=\zeta_{X_0,\rho}(0)\neq 0.\]
In addition, if $b_1(\ml{M})\not=0$ or if there exists a closed orbit $\gamma$ of $X_0$ such that, for each 
$j\in\{0,1\}$, $\ker( \rho([\gamma])-\varepsilon_{\gamma}^j{\rm Id})=0$, then $\vert\zeta_{X,\rho}(0)\vert^{-1}=\tau_\rho(\mc{M})$ is the Reidemeister torsion for each $X\in \mc{U}(X_0)$.
```

**The degree-graded dynamical zetas and the alternating weight `(-1)^k`:**

- `1807.01189:main.tex:1627,1632`
```
We define the \emph{dynamical zeta function} of $X$ acting on $\Omega_0^k(SM;\til{E})$ by 
\begin{equation}\label{Zj}
Z_{{\bf X}^{(k)}}(\la)=\exp\Big(-\sum_{\gamma\in \mc{P}}\sum_{j=1}^\infty 
\frac{1}{j}\frac{e^{-\la j \ell(\gamma)}{\rm Tr}(\til{\rho}(\gamma)^j){\rm Tr}(\wedge^k P(\gamma)^j)}{|\det(1-P(\gamma)^j)|}\Big)
\end{equation}
where $\mc{P}$ denotes the set primitive closed geodesics and $P(\gamma)$ is the linearized Poincar\'e map of the geodesic flow along this geodesic. Note that $\mc{P}$ is parametrized by the conjugacy classes of primitive elements in the group $\Gamma$. 
```

- `1807.01189:main.tex:809,817`
```
\begin{corr}\label{corrolairevar}
With the conventions of Lemma~\ref{l:regularity-physical-region}, one has, for every $\tau\in(-\tau_0,\tau_0)$ and for $\lambda \in \Omega_0$ 
\[
\frac{\zeta_{\tau,\rho}(\lambda)}{\zeta_{0,\rho}(\lambda)}=\exp\left(-\lambda\int_0^{\tau}\sum_{k=0}^n(-1)^{k}\sum_{\gamma_{\tau'}}\frac{\ell^\sharp(\gamma_{\tau'})}{\ell(\gamma_{\tau'})}
 \frac{\left(\int_{\gamma_{\tau'}}{\rm Tr}\left(A_{\tau'}^{(k)}\left(\wedge^k 
 d\varphi^{\tau'}_{\ell(\gamma_{\tau'})}\right)\right)\right)}{|\det({\rm 
 Id}-P(\gamma_{\tau'}))|e^{\lambda \ell(\gamma_{\tau'})}} 
 {\rm Tr}(\rho([\gamma_{\tau'}]))d\tau'\right).\] 
\end{corr}
```

**Explicit degree-by-degree multiplicities for hyperbolic 3-manifolds:**

- `1807.01189:main.tex:1719,1727`
```
\begin{prop}\label{dim3}
Let $M=\Gamma\backslash \hh^{3}$ be a smooth compact oriented hyperbolic manifold and let 
$\rho$ be a unitary representation of $\pi_1(M)$. The multiplicity 
$m_k(0):=\dim C_0^k$ of $0$ as a Ruelle resonance for ${\bf X}^{(k)}$ are given by 
\[\begin{gathered} 
m_0(0)=\dim H^0(M;\rho), \quad  m_1(0)=2\dim H^1(M,\rho), \\ 
m_2(0)=2(\dim H^1(M,\rho)+\dim H^0(M;\rho)), \quad m_{4-k}(0)=m_k(0)
\end{gathered}\]   
where $H^k(M;\rho)$ is the twisted de Rham cohomology of degree $k$ associated to $\rho$.
```

*Plain summary.* This is the modern theorem-level version of "the value of the
dynamical zeta at zero is a torsion". The zeta is assembled degree by degree
with the sign `(-1)^k`; the full alternating product is the Ruelle zeta, whose
value at 0 (up to the global sign `(-1)^{n_0}`) is the Reidemeister torsion when
the representation is acyclic. The authors prove local constancy of
`zeta_{X,rho}(0)` in the vector field, hence the Fried conjecture in dimension 3
and for perturbations of hyperbolic geodesic flows in dimension 5. For the
notebook: the torsion is exactly "the supertrace of the graded complex", and the
minus sign in the explicit formula is the same `(-1)^k`.

## A4. `2009.08558` — Cekić–Delarue–Dyatlov–Paternain, *The Ruelle zeta function at zero for nearly hyperbolic 3-manifolds*

(The task named "Cekić–Dyatlov–Küster–Paternain"; the author list in the source
is Cekić, **Delarue** — `formerly known as Benjamin Küster` — Dyatlov, Paternain.)

Title and authors:

- `2009.08558:contact5d.tex:9,25`
```
\title[The Ruelle zeta function at zero for nearly hyperbolic 3-manifolds]%
{The Ruelle zeta function at zero\\ for nearly hyperbolic 3-manifolds}
\author{Mihajlo Ceki\'c}
\email{mihajlo.cekic@math.uzh.ch}
\curraddr{Institut f\"ur Mathematik, Universit\"at Z\"urich, Winterthurerstrasse 190, CH-8057 Z\"urich, Switzerland}
\address{Laboratoire de Math\'ematiques d'Orsay, Universit\'e Paris-Saclay, CNRS, 91405 Orsay, France}
\author{Benjamin Delarue}
\email{bdelarue@math.upb.de}
\address{Institut f\"ur Mathematik, Universit\"at Paderborn, Paderborn, Germany; formerly known as Benjamin Küster}
\author{Semyon Dyatlov}
\email{dyatlov@math.mit.edu}
\address{Department of Mathematics, Massachusetts Institute of Technology, Cambridge, MA 02139}
\author{Gabriel P. Paternain}
\email{g.p.paternain@dpmms.cam.ac.uk}
\address{Department of Pure Mathematics and Mathematical Statistics,
University of Cambridge,
Cambridge CB3 0WB, UK}
```

**The sensitivity result — the order of vanishing is NOT a topological invariant
in dimension 3 (5-dimensional sphere bundle):**

- `2009.08558:contact5d.tex:63,75`
```
\begin{theo}
\label{thm:main}
Let $(\Sigma,g_H)$ be a compact connected oriented hyperbolic 3-manifold and $b_1(\Sigma)$
be the first Betti number of~$\Sigma$. Then:

1. For $(\Sigma,g_H)$ we have $m_{\mathrm R}(0)=4-2b_1(\Sigma)$.

2. There exists an open and dense set $\mathscr O\subset C^\infty(\Sigma;\mathbb R)$
such that for any $\mathbf b\in\mathscr O$, there exists $\varepsilon>0$
such that for any $\tau\in (-\varepsilon,\varepsilon)\setminus \{0\}$
and $g_\tau:=e^{-2\tau\mathbf b}g_H$,
the manifold $(\Sigma,g_\tau)$ has $m_{\mathrm R}(0)=4-b_1(\Sigma)$.
\end{theo}
```

**The alternating factorisation in the 5-dimensional case — note that here the
EVEN degrees are the numerator and the ODD degrees the denominator, the opposite
placement from the surface case:**

- `2009.08558:contact5d.tex:1157,1168`
```
By Ruelle's identity (see e.g.~\cite[(2.5)]{dyatlov-zworski-16}) the Ruelle zeta function defined in~\eqref{e:ruelle-zeta}
factorizes as follows:
$$
\zeta_{\mathrm R}(\lambda)={\zeta_0(\lambda)\zeta_2(\lambda)\zeta_4(\lambda)\over \zeta_1(\lambda)\zeta_3(\lambda)}.
$$
Using~\eqref{e:isom-2} we see that the order of vanishing of the function $\zeta_{\mathrm R}$ at $\lambda_0$ is equal to
\begin{equation}
  \label{e:alternator}
m_{\mathrm R}(\lambda_0)=
\sum_{k=0}^4 (-1)^k m_{k,0}(\lambda_0)=2m_{0,0}(\lambda_0)-2m_{1,0}(\lambda_0)+m_{2,0}(\lambda_0).
\end{equation}
```

- `2009.08558:contact5d.tex:120,124`
```
The order of vanishing of the Ruelle zeta function at~0 can be expressed as the alternating sum of the dimensions of the spaces of generalized resonant $k$-forms, see~\eqref{e:alternator}:
$$
m_{\mathrm R}(0)=\sum_{k=0}^4 (-1)^k\dim \Res^{k,\infty}_0.
$$
Thus the problem reduces to understanding the spaces $\Res^{k,\infty}_0$ for $k=0,1,2,3,4$.
```

**Contrast with the 2-dimensional case, stated by the authors:**

- `2009.08558:contact5d.tex:78,84`
```
using the Selberg trace formula. The novelty is part~2, which says that
\emph{for generic conformal perturbations of the hyperbolic metric the order
of vanishing of $\zeta_{\mathrm R}$ equals $4-b_1(\Sigma)$.}
In particular, when $b_1(\Sigma)>0$ (fulfilled in many cases, in particular for mapping tori over pseudo-Anosov maps \cite[Theorem 13.4]{Farb-Margalit-12}), $m_{\mathrm R}(0)$ is not topologically invariant.
Theorem~\ref{thm:main} is the first result on instability of the order of vanishing of $\zeta_{\mathrm R}$ at~0 for Riemannian metrics. It is in contrast to the 2-dimensional case, where Dyatlov--Zworski~\cite{dyatlov-zworski-17} showed that $m_{\mathrm R}(0)=b_1(\Sigma)-2$
for \emph{any} compact connected oriented negatively curved surface $(\Sigma,g)$,
and is complementary to a recent breakthrough on the (acyclic) \emph{Fried conjecture} by Dang--Guillarmou--Rivi\`ere--Shen~\cite{dang-guillarmou-riviere-shen-20}, see~\S\ref{s:history} below.
```
(Note `m_R(0) = b_1(Sigma) - 2 = -chi(Sigma)` in the surface case, matching §A2.)

*Plain summary.* The cohomological reading is real but **fragile**. In dimension
2 the alternating count is exactly topological (`-chi`). In dimension 3 (i.e. on
the 5-dimensional sphere bundle) the individual degree multiplicities `m_k(0)`
are only topological at the hyperbolic point; a generic conformal perturbation
halves the degree-1 contribution (`2b_1 -> b_1`) and the alternating sum jumps
from `4-2b_1` to `4-b_1`. For the notebook this is the warning: "the zeros are
the odd cohomology" is a statement that can hold at a symmetric point and fail
under perturbation, so any graded/supertrace realisation must be pinned by more
than the alternating count.

---

# B. Analytic / Reidemeister torsion and zeta — and the graph analogue

## B1. Fried's papers (not on arXiv; bibliographic data byte-cited from arXiv sources in the tree)

- `1606.04560:zazi.tex:1177,1180`
```
\bibitem[Fr1]{Fr1} David Fried,
	\emph{Fuchsian groups and Reidemeister torsion,\/}
	in \emph{The Selberg trace formula and related topics (Brunswick, Maine, 1984),\/} 
	Contemp. Math. \textbf{53}, 141--163, Amer. Math. Soc., Providence, RI, 1986. 
```

- `1807.01189:main.tex:2036,2044`
```
\bibitem[Fr1]{Fr0} D. Fried, \emph{Homological identities for closed orbits}, Inventiones Math. \textbf{71} (1983), 419--442.

\bibitem[Fr2]{FrInv} D. Fried, \emph{Analytic torsion and closed geodesics on hyperbolic manifolds}, Inventiones Math. \textbf{84} (1986), 523--540.

\bibitem[Fr3]{FriedAnnENS} D. Fried, \emph{The zeta functions of Ruelle and Selberg. I.} Annales de l'ENS \textbf{19} (1986) no 4, 491--517

\bibitem[Fr4]{F87} D.~Fried \emph{Lefschetz formulas for flows}, Contemporary Mathematics Vol. 58, Part III (1987), 19--69 

\bibitem[Fr5]{Friedanalytic} D. Fried, \emph{Meromorphic zeta functions for analytic flows.} Communications in mathematical physics \textbf{174} (1995): 161-190.
```

Deitmar's independent record of the same *Analytic torsion* paper:

- `dg-ga/9511006:main.tex:1573,1576`
```
\name{Fried, D.:}
\it Analytic torsion and closed geodesics on hyperbolic manifolds.
\rm Invent. math. 84, 523-540 (1986).

```

The *Fuchsian groups and Reidemeister torsion* reference appears identically in
a second arXiv source in the tree (a cross-check, not the same bibliography):

- `2303.11226:zeta_triangulations9.tex:1939`
```
% \textsc{Fried, D.}, \emph{Fuchsian groups and Reidemeister torsion}, in "The Selberg trace formula and related topics" (Brunswick, Maine, 1984), Contemp. Math. 53, 141-163, Amer. Math. Soc., Providence, RI, 1986.
```
(Commented out in that source, but the bytes are the bibliographic record.)

**Content, as byte-cited from the arXiv papers that use it** (no TeX of Fried's
own papers exists): the "Fuchsian groups" paper supplies
`zeta_R(s) = ±(2 pi s)^{|chi(Sigma)|}(1 + O(s))` — `1606.04560:zazi.tex:122,126`
quoted in §A2 above, labelled there as Fried, Corollary 2. The
*Analytic torsion and closed geodesics* paper supplies
`|zeta_{X,rho}(0)^{(-1)^{n_0}}| = tau_rho(M)` — `1807.01189:main.tex:230,233`
quoted in §A3, labelled there as `\cite{FrInv}`.

## B2. Juhl (book; not on arXiv)

- `1807.01189:main.tex:2081`
```
\bibitem[Ju]{Ju} A. Juhl, \emph{Cohomological Theory of Dynamical Zeta Functions}, Progress in Mathematics Vol 194.
```
(Birkhäuser, 2001. The earlier Habilitationsschrift is recorded in Deitmar's
bibliography: `dg-ga/9511006:main.tex:1624,1627` —
```
\name{Juhl, A.:}
\it Zeta-Funktionen, Index-Theorie und hyperbolische Dynamik.
\rm Habilitationsschrift. Humboldt-Universit\"{a}t zu Berlin 1993.

```
.) Deitmar credits Juhl's rank-one method as the engine of his own higher-rank
argument: `dg-ga/9511006:main.tex:264,265`
```
The central idea is to use the rank one approach of A. Juhl to shift
down to a Levi component of splitrank one.
```

## B3. `2310.15619` — the Ihara determinant formula with `(1-u^2)^{-chi}`, and Hashimoto's `h'(1) = -2 chi kappa`

(Already in the tree; author/title line
`2310.15619:main.tex:253` —
`\title[Spanning trees in $\mathbb{Z}$-covers of a finite graph and Mahler measures]{Spanning trees in $\mathbb{Z}$-covers of a finite graph and Mahler measures}`.)

**The graph zeta in exactly the notebook's normalisation, with
`chi(X) = |V| - |E|`:**

- `2310.15619:main.tex:941,948`
```
    Z_{X}(u) = \frac{1}{(1-u^{2})^{-\chi(X)} \cdot {\rm det}(\mathrm{Id}_g - A_X u + (D_X - \mathrm{Id}_g)u^{2})},
\end{equation}
where $\mathrm{Id}_g$ denotes the $g \times g$ identity matrix, and $\chi(X) := \lvert V_X \rvert - \lvert \mathbf{E}_X \rvert/2$ is the Euler characteristic of $X$.
In particular, we have that $Z_X(u)^{-1} = (1-u^2)^{-\chi(X)} \cdot h_X(u)$, where
\[
h_{X}(u) := {\rm det}(\mathrm{Id}_g - A_X u + (D_X - \mathrm{Id}_g)u^{2}) \in \mathbb{Z}[u]
\]
is a polynomial.
```
(`\mathbf{E}_X` counts *directed* edges here, hence the `/2`.)

**Hashimoto's formula — the graph "value at the special point = torsion-like
invariant" statement:**

- `2310.15619:main.tex:950,955`
```
\subsubsection*{Hashimoto's formula}
This explicit formula can be used to relate the Ihara zeta function to the number of spanning trees of $X$. More precisely, given a finite connected graph $X$, one has
\begin{equation} \label{eq:Hashimoto}
    h_{X}'(1) = -2 \chi(X) \kappa(X),
\end{equation}
as was proven by Hashimoto in \cite[Theorem~B]{Hashimoto:1990} (see also \cite[Part~II, Sections~5~and~6]{Bass:1992}).
```

The same statement, attributed to Northshield, in a second arXiv source:

- `2405.04361:v3.tex:432,441`
```
\begin{theorem}\label{class number formula thm}
    For a graph $X$ satisfying Assumption \ref{no vertices with val 1}, one has that 
    \[h_X'(1)=-2\chi(X) \kappa_X.\]
\end{theorem}
\begin{proof}
    For a proof of the result, we refer to \cite{Northshield} or \cite[Theorem 2.11]{HammerMattmanSandsVallieres}.
\end{proof}

For abelian covers, the Artin-Ihara L-functions described satisfy a relation as a consequence of the Artin formalism, as the following result shows.
```

A third, completely explicit modern restatement (Mizuno), which also makes
plain that the tree number is carried by the **Hecke/Laplacian factor `h_X`**,
not by the `(1-u^2)^chi` factor:

- `2503.19641:Spanning_trees_and_their_relations_in_Galois_covers.tex:313,318`
```
The Ihara zeta function is a rational function associated with a finite connected graph $X$, denoted by $\zeta_{X}(u)$. One notable property of the Ihara zeta function is that it can be explicitly computed using the three-term determinant formula, which expresses $\zeta_{X}(u)$ in terms of the adjacency matrix $A_X$ and degree matrix $D_X$ (see Theorem 2.5. \cite{Terras}): 
$$\zeta_{X}(u)=\frac{(1-u^{2})^{\chi(X)}}{\det(I-A_{X}u+(D_{X}-I)u^{2}).}$$  

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hashimoto establishes a connection between the Ihara zeta function and the number of spanning trees of the graph. By defining $h_X(u)\coloneq \det(I - A_{X}u + (D_{X}-I)u^2)$, we obtain the following result (see \cite{Hashimoto}):
$$h'_X(1)=-2\chi(X)\kappa(X), $$ where $\kappa(X)$ denotes the number of spanning trees of $X$. 
```

**Which factor carries the tree number — the precise answer.** `h_X(u) =
det(I - A_X u + (D_X - I)u^2)` is the *denominator* of the Ihara zeta (the
Laplacian/Hecke factor), and `h_X(1) = 0` for a connected graph with
`chi != 0`; the complexity `kappa(X)` appears in its **first derivative** at
`u = 1`, `h'_X(1) = -2 chi(X) kappa(X)`. The prefactor `(1-u^2)^{chi(X)}` also
vanishes (or blows up) at `u = 1`, and its role is to cancel that zero: from
`Z_X(u)^{-1} = (1-u^2)^{-chi(X)} h_X(u)` (`2310.15619:main.tex:944`), the two
factors together give a finite nonzero limit whose value is set by
`-2 chi kappa`. So: **`(1-u^2)^chi` is the torsion-like/Euler-characteristic
bookkeeping factor; `kappa` sits in the Laplacian determinant, exactly as in
Kirchhoff's theorem.** Compare §C1: it is `(1-u^n)^chi` that is the determinant
of a cochain automorphism on cohomology, and §B7: it is the *super* determinant
of the Hodge/Dirac complex that equals the even/odd tree ratio.

**Bibliographic data for the non-arXiv originals, byte-cited:**

- `2310.15619:references.bib:953,961` (Bass 1992)
```
@article {Bass:1992,
    AUTHOR = {Bass, Hyman},
     TITLE = {The {I}hara-{S}elberg zeta function of a tree lattice},
   JOURNAL = {Internat. J. Math.},
  FJOURNAL = {International Journal of Mathematics},
    VOLUME = {3},
      YEAR = {1992},
    NUMBER = {6},
     PAGES = {717--797},
```

- `2310.15619:references.bib:420,428` (Hashimoto 1990)
```
@article {Hashimoto:1990,
    AUTHOR = {Hashimoto, Ki{-}ichiro},
     TITLE = {On zeta and {$L$}-functions of finite graphs},
   JOURNAL = {Internat. J. Math.},
  FJOURNAL = {International Journal of Mathematics},
    VOLUME = {1},
      YEAR = {1990},
    NUMBER = {4},
     PAGES = {381--396},
```

- `2405.04361:references.bib:412,421` (Northshield 1998)
```
@article {Northshield,
    AUTHOR = {Northshield, Sam},
     TITLE = {A note on the zeta function of a graph},
   JOURNAL = {J. Combin. Theory Ser. B},
  FJOURNAL = {Journal of Combinatorial Theory. Series B},
    VOLUME = {74},
      YEAR = {1998},
    NUMBER = {2},
     PAGES = {408--410},
}
```

- `2208.14032:refs.bib:1106,1113` (Northshield, *Two proofs of Ihara's theorem*)
```
@incollection{northshield1999two,
  title={Two proofs of Ihara’s theorem},
  author={Northshield, Sam},
  booktitle={Emerging applications of number theory},
  pages={469--478},
  year={1999},
  publisher={Springer}
}
```

## B4. Hoffman — Bass's proof of Ihara's identity *is* a torsion-of-complexes computation (not on arXiv)

**Bibliographic data:**

- `2607.21262:main.tex:3421,3430`
```
\bib{Hof}{article}{
   author={Hoffman, J. William},
   title={Remarks on the zeta function of a graph},
   journal={Discrete Contin. Dyn. Syst.},
   date={2003},
   pages={413--422},
   note={Supplement; Dynamical systems and differential equations
   (Wilmington, NC, 2002)},
   doi={10.3934/proc.2003.2003.413},
}
```

**The content, byte-cited from the paper that builds on it:**

- `2607.21262:main.tex:351,366`
```
The \(\mathrm{PGL}_3\) identity just mentioned has two published proofs: the
combinatorial proof of~\cite{KL} and the representation-theoretic proof
of~\cite{KLW}.  Our proof is different from both and, upon specialization,
gives another proof of that identity.  It is inspired instead by Hoffman's
reformulation of Bass's proof of the Ihara identity in terms of torsion of
complexes~\cite{Hof}.

The higher-rank argument is necessarily more elaborate.  The Euler products
are first expressed as determinants of successor operators on pointed
\(k\)-facets.  These spaces, for all \(k\), are assembled into a cochain
complex.  A family of Laplacian-type endomorphisms then compares the
alternating product of successor determinants with the spherical Hecke
determinant for the unramified \(L\)-function.  The principal technical step
is a M\"obius-inversion calculation of these endomorphisms.  This strategy
retains the cohomological idea behind Hoffman's proof while accommodating all
facet dimensions and all possible algebraic lengths.
```

*This is the direct, byte-verified answer to the question "is `(1-u^2)^{chi}`
the torsion-like factor?" — see §C1 for the identity where it falls out as
exactly the determinant of a cochain automorphism on cohomology.*

## B5. `2104.00215` — Zhuang, *Ihara zeta function and twisted Alexander invariants* (NEW)

- `2104.00215:Ihara_zeta_function_and_twisted_Alexander_invariants.tex:4,5`
```
\title{Ihara zeta function and twisted Alexander invariants}
\author{Zipei Zhuang}
```

- `2104.00215:Ihara_zeta_function_and_twisted_Alexander_invariants.tex:31,33`
```
	\begin{abstract}
		In \cite{Lin98randomwalk}, Lin and Wang defined a model of random walks on knot diagrams and interprete the Alexnader polynomials and the colored Jones polynomials as Ihara zeta functions, i.e. zeta functions defined by counting cycles on the knot diagram. Using this explanation, they gave a more conceptual proof for the Melvin-Morton conjecture. In this paper, we give an analogous zeta function expression for the twisted Alexander invariants. 
	\end{abstract}
```

The `L^2`-torsion obstruction, stated by the author:

- `2104.00215:Ihara_zeta_function_and_twisted_Alexander_invariants.tex:721`
```
We cannot get a zeta function formula like the twisted Alexander case since, unlike the determinant, there is no direct relationship between the $L^2$- torsion of a matrix and its entries.
```

*Plain summary.* The twisted Alexander polynomial is a Reidemeister torsion of
the knot exterior, and this paper writes it as an Ihara-type zeta counting cycles
on a knot diagram (a graph). So there **is** a direct graph-zeta = torsion
statement in the literature, but it is for the twisted Alexander/Reidemeister
torsion of a 3-manifold via a diagram graph, not for `(1-u^2)^chi` per se.
Fuglede–Kadison (`L^2`) torsion resists the same treatment.

## B6. `2303.11226` — Benard–Chaubet–Dang–Schick, *Combinatorial zeta functions counting triangles*

This is the closest thing in the literature to "Dyatlov–Zworski for a
triangulation", and it is already in the tree.

- `2303.11226:zeta_triangulations9.tex:89,105`
```
\title[Triangulations and combinatorial zeta functions]{Combinatorial zeta functions counting triangles}
%\date{\today}
\author{Leo Benard}
\address{Mathematisches Institut, Georg--August Universit\"at G\"ottingen $\&$
Institut de Mathématiques de Marseille, Aix--Marseille University}
\email{leo.benard@univ-amu.fr}
\author{Yann Chaubet}
\address{Department of Pure Mathematics and Mathematical Statistics, University of
Cambridge, Cambridge}
\email{y.chaubet@dpmms.cam.ac.uk}
\author{Nguyen Viet Dang}
\address{Sorbonne Université and Université Paris Cité, CNRS, IMJ-PRG, F-75005 Paris, France.\\
Institut Universitaire de France, Paris, France.}
\email{dang@imj-prg.fr }
\author{Thomas Schick}
\address{Mathematisches Institut, Georg--August Universit\"at  G\"ottingen}
\email{thomas.schick@math.uni-goettingen.de}
```

**The combinatorial "Fried theorem": a signed zeta over combinatorial geodesics
in the `(n-1)`-skeleton whose order of vanishing at a special point is `b_1(M)`:**

- `2303.11226:zeta_triangulations9.tex:192,205`
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

Note the `varepsilon_gamma in {-1,1}` "reversing index" — a **sign weight on
each cycle**, i.e. a `Z_2`-grading carried by the orbit, not by the coefficient
space:

- `2303.11226:zeta_triangulations9.tex:179,183`
```
  geodesic is called primitive if it 
  is not a power of a shorter one. The length of a combinatorial closed geodesic
  $\gamma = [(\sigma_1, \dots, \sigma_q)]$ is denoted by $|\gamma| = q$ while
  $\varepsilon_\gamma \in \{-1, 1\}$ denotes its \textit{reversing index},
  which is the parity of how often orientations are flipped traversing the
```

**The torsion remark — the alternating combination over all degrees is the
topological invariant, a single degree is not:**

- `2303.11226:zeta_triangulations9.tex:1481,1483`
```
  Note, however, that a combination of the Fuglede--Kadison determinants of
  all the combinatorial $L^2$-Laplacians gives the $L^2$-torsion of $M$, a
  very interesting topological invariant, compare \cite[Chapter 3]{Lueck}. This is similar to the compact Riemannian case, it is well--known that the Ray--Singer zeta determinant of the Laplacian acting on functions is not a topological invariant. However, a combination of the zeta determinants for the Laplacian acting on forms of all degrees gives the analytic torsion which happens to be a topological invariant.   
```

Their own comparison with Bass:

- `2303.11226:zeta_triangulations9.tex:1906,1916`
```
In the case of graphs and more specifically trees with a cocompact action
of a group $\pi$, there are also approaches to define and study zeta functions
and relate them to the combinatorial Laplacian. A specific example here is the
Ihara zeta function as introduced and studied by Bass in \cite{Bass92}. On a
formal level, many fundamental properties are similar to ours, compare
e.g.~\cite[Theorem 3.9]{Bass92}. On the other hand, there are also many
fundamental differences: Bass uses non-commutative determinants in the style
of Hattori--Stallings. They are finer, but much more intricate than our
Fuglede--Kadison invariant, whereas the latter can be defined and manipulated
in more general situations. Bass deals with proper actions which are not
necessarily free (free actions on trees occur only by free groups).
```

*Plain summary.* A purely combinatorial zeta counting non-backtracking paths in
the `(n-1)`-skeleton of a triangulation, with a sign per orbit, reproduces the
Fried/Dyatlov–Zworski phenomenon: the special value at `z = (n+2)^{-1}` has
vanishing order `b_1(M)`. The "torsion is the alternating combination over all
degrees; a single degree is not topological" statement is made explicitly. For
the notebook this is the strongest evidence that the graded picture survives
discretisation.

## B7. `2201.09412` — Knill, *Analytic torsion for graphs* — **the graph supertrace statement**

This is the single most on-target source for the notebook's "zeta = supertrace"
picture on the discrete side. Already in the tree.

- `2201.09412:reidemeister.tex:13,19`
```
\title{Analytic torsion for graphs}
\fancyhead{}
\fancyhead[LO]{\fontsize{9}{9} \selectfont OLIVER KNILL}
\fancyhead[LE]{\fontsize{9}{9} \selectfont TORSION}
\renewcommand{\headrulewidth}{0pt}
\author{Oliver Knill}
\date{January 23, 2022 }
```

**Torsion = super pseudo-determinant of the Dirac operator; the generalised
matrix-tree theorem as an even/odd ratio:**

- `2201.09412:reidemeister.tex:42,52`
```
For any finite simple graph $(V,E)$, the squared analytic torsion is the
positive rational number $A(G) = \prod_k {\rm Det}(L_k)^{k (-1)^{k+1}}$,
where $L_k$ are the blocks of the Hodge Laplacian $L=D^2=(d+d^*)^2$ of the Whitney
complex and ${\rm Det}$ is the pseudo determinant. Torsion $A(G)$ agrees with the super pseudo determinant 
${\rm SDet}(D) = \prod_k {\rm Det}(D_k)^{(-1)^k}$ of the Dirac blocks
$D_k=d_k^* d_k$ of the Dirac operator $D=d+d^*$ and is related to the pseudo determinant 
${\rm Det}(D)=\pm \prod_k{\rm Det}(D_k)$ of $D$. 
This gives a generalized matrix tree theorem: $A(G)$ is the ratio of rooted spanning trees 
on even-dimensional simplices divided by the number of rooted spanning trees in odd simplices. 
In particular, the classical matrix tree theorem rephrases that for graphs without triangles, 
$A(G)$ is the number of rooted spanning trees in $G$. For $2$-spheres with $|F|$ triangles, 
```

**The bosonic/fermionic language, in the author's own words:**

- `2201.09412:reidemeister.tex:545,556`
```
can be identified with the {\bf super pseudo determinant of the Dirac operator}
$$ A(G) = \prod_{k} {\rm Det}(D_k)^{(-1)^k} \; . $$
It is a {\bf ``Fermionic" version} of the pseudo determinant of the Dirac operator
$$ {\rm Det}(D) = \pm \prod_{k} {\rm Det}(D_k) \;  $$
which as an orientation oblivious determinant and so has a more {\bf ``Bosonic"} nature.

\paragraph{}
While the pseudo determinant counts types of trees in a graph defined by the simplicial complex,
the super pseudo determinant and so the analytic torsion is the ratio of the number of even trees 
over the number of odd trees. For the 4-sphere, the {\bf cross polytope} with $f$-vector 
$f=(10, 40, 80, 80, 32)$ for example, we have a Dirac determinant ${\rm Det}(D)=2^{220} 3^{40} 5^{15}$, a number 
with $95$ digits while torsion $A(G) = 10/32=0.3125$ is small. For the first few cross polytopes $S^k$
```

*Plain summary.* On a finite simple graph with its Whitney complex, the analytic
(Ray–Singer) torsion is literally `SDet(D) = prod_k Det(D_k)^{(-1)^k}`, the
**super** pseudo-determinant of the Dirac operator `D = d + d*`, and Knill spells
out that this is the "fermionic" version of the ordinary (orientation-oblivious,
"bosonic") determinant. The combinatorial content is a generalised matrix-tree
theorem: torsion is the number of rooted spanning trees on **even**-dimensional
simplices divided by the number on **odd** simplices. For a triangle-free graph
the odd part is trivial and one recovers Kirchhoff. This is precisely the
notebook's even-sector/odd-sector split, realised on a graph, with the
"supertrace" being the alternating product over simplex dimension. It is not a
statement about the Ihara zeta, but it is the torsion that the Ihara zeta's
special value at `u = 1` (§B3) is the graph shadow of.

## B8. `1602.00664` — Shen, *Analytic torsion, dynamical zeta functions, and the Fried conjecture*

- `1602.00664:main.tex:172,174`
```
\title{Analytic torsion, dynamical zeta functions, and  the Fried 
conjecture}
\author{Shu Shen}
```
*(Caution: this file is latin1-encoded and GNU `grep` treats it as binary; use
`grep -a` or `sed -n`.)*

**Milnor's original observation — torsion vs the Weil zeta:**

- `1602.00664:main.tex:241,243`
```
From the dynamical side, in \cite[Section 3]{MilnorZcover}, Milnor  pointed out a remarkable similarity between the Reidemeister torsion and
the Weil zeta function.
A quantitative description of their relation was formulated by Fried \cite{FriedRealtorsion} when $Z$ is a closed oriented hyperbolic manifold. Namely, he showed that the value at zero of the Ruelle dynamical zeta function, constructed using the closed geodesics in $Z$ and the holonomy of $F$, is equal to  $T(F)^2$. In \cite[p. 66, Conjecture]{Friedconj}, Fried conjectured that a similar result holds true for general closed locally homogeneous manifolds.
```

**The analytic torsion defined as a SUPERTRACE with the form-degree number
operator — the exact shape of the notebook's `str`:**

- `1602.00664:main.tex:365,378`
```
Let $N^{\Lambda^\cdot(T^*Z)}$ \index{N@$N^{\Lambda^\cdot(T^*Z)}$} be the number operator of $\Lambda^\cdot(T^*Z)$, i.e., multiplication by $i$ on $\Omega^i (Z, F )$.
 Let $\Trs$ denote  the supertrace.
For $s\in\bC$, $\Re(s)>\frac{1}{2}\dim Z$, set
\begin{align}
  \theta(s)=-\Trs\[N^{\Lambda^\cdot(T^*Z)}\(\Box^{Z}\)^{-s}\].\index{T@$\theta(s)$}
\end{align}
By \cite{Seeley66},  $\theta(s)$ has a meromorphic extension to $\bC$, which is holomorphic at $s=0$. The analytic torsion is a positive real number given by
\begin{align}
T(F)=\exp(\theta'(0)/2).\index{T@$T(F)$}
\end{align}
Equivalently, $T(F)$ is given by the following weighted product of the zeta regularized determinants
\begin{align}\label{eq:inn}
T(F)=\prod_{i=1}^{\dim Z}\det\(\Box^Z|_{\Omega^i(Z,F)}\)^{(-1)^ii/2}.
\end{align}
```

**The main theorem (Fried conjecture for odd-dimensional closed locally
symmetric reductive manifolds):**

- `1602.00664:main.tex:740,755`
```
\begin{thm}\label{thm:01}
Assume $\dim Z$ is odd. The dynamical zeta function  $R_\rho(\sigma)$ 
is  holomorphic for $\Re(\sigma)\gg1$ and extends meromorphically to 
$\sigma\in \bC$. Moreover, there exist explicit constants $C_\rho\in \bR^{*}$ and $r_\rho\in \mathbf{Z}$ (c.f. \eqref{eq:Cr}) such that, when  $\sigma\to 0$,
\begin{align}\label{eq:t01}
  R_\rho(\sigma)=C_\rho T(F)^2\sigma^{r_\rho}+\cO\(\sigma^{r_\rho+1}\).
\end{align}
If $H^\cdot(Z,F)=0$, then
\begin{align}\label{eq:t02}
  &C_\rho=1,&r_\rho=0,
\end{align}
so that
\begin{align}
R_\rho(0)=T(F)^2.
\end{align}
\end{thm}
```

*Plain summary.* Shen completes Moscovici–Stanton and proves Fried's conjecture
for all odd-dimensional closed locally symmetric reductive manifolds:
`R_rho(0) = T(F)^2` in the acyclic case. The `str` shape the notebook wants is
literally the definition of `T(F)`: a supertrace of the **number operator**
(form degree) against the heat/zeta kernel of the Hodge Laplacian, equivalently
`prod_i det(Box|_{Omega^i})^{(-1)^i i/2}` — the same `(-1)^i i` weight that
appears in Deitmar's `chi_1` (§A1) and in Knill's `A(G) = prod_k Det(L_k)^{k(-1)^{k+1}}`
(§B7). All three are the same weighted supertrace.

---

# C. The alternating product for graphs and complexes: where `(1-u^2)^chi` comes from

## C1. `2607.21262` — Kang–Yu, *Zeta functions of PGL_n over non-Archimedean local fields*

- `2607.21262:main.tex:150,155`
```
\title[zeta functions]{Zeta functions of PGL$_n$ over non-Archimedean local fields}
\author{Ming-Hsuan Kang}
\address{National Yang Ming Chiao Tung University, Department of Mathematics,
Hsinchu, Taiwan 300} 
\email{mhkang@math.nctu.edu.tw}
\author{Jiu-Kang Yu}
```

**Ihara's identity in the notebook's exact form, `(1-u^2)^{chi}` over the
Hecke/adjacency determinant:**

- `2607.21262:main.tex:210,219`
```
Bruhat--Tits tree is \((q+1)\)-regular, and Ihara's identity may be written
\begin{equation}\label{eq:Ihara}
 Z(X_\Gamma,u)
 =\frac{(1-u^2)^{\chi(X_\Gamma)}}{\det(I-Au+qu^2I)}
 =(1-u^2)^{\chi(X_\Gamma)}L(\Gamma,q^{1/2}u).
\end{equation}
Here \(A\) is both the graph adjacency operator and the spherical Hecke
operator, while \(L(\Gamma,u)\) is the unramified \(L\)-function attached to
the unramified spectrum of \(L^2(\Gamma\backslash\mathrm{PGL}_2(F))\); see
also~\cite{Ha}.  Thus~\eqref{eq:Ihara} connects a zeta function defined by
```

**The main theorem: the general Ihara identity IS an alternating product over
facet dimension, with the `(1-u^n)^chi` factor:**

- `2607.21262:main.tex:172,188`
```
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
extend the construction and the identity to \(\mathrm{PGL}_n(D)\), where
\(D\) is a central division algebra over \(F\); in that setting the residue
parameter is \(Q=|\ringO_D/\mathfrak p_D|\).
\end{abstract}
\maketitle
\def \X {\scrB_\Gamma}
\def \oo {\mathrm{O}}
```

**The `epsilon` sign — an explicit `(-1)^{(k+1) l_G}` parity weight on each
closed geodesic (the discrete analogue of the orientation index):**

- `2607.21262:main.tex:289,299`
```
Here \(l_A\) is the algebraic length; the geometric length \(l_G\) records
the number of facets.  The sign
\(
 \epsilon(\scrC)=(-1)^{(k+1)l_G(\scrC)}
\)
gives the twisted zeta function
\[
 Z_k^\epsilon(\scrB_\Gamma,u)
 =\prod_{[\scrC]}
  (1-\epsilon(\scrC)u^{l_A(\scrC)})^{-1}.
\]
```

**The conceptual proof: the `(1-u^n)^chi` factor IS a determinant on cohomology
— a torsion — via the Euler–Poincaré identity:**

- `2607.21262:main.tex:2463,2487`
```
\begin{align*}
\prod_{i=0}^{n-1}\det(\Phi_i\mid C_i(\X))^{(-1)^i}
&=
\prod_{i=0}^{n-1}\det(\Phi_i\mid H^i(\X,\C(u)))^{(-1)^i} \\
&=
\prod_{i=0}^{n-1}\det(1-u^n\mid H^i(\X,\C(u)))^{(-1)^i} \\
&=
(1-u^n)^{\sum_{i=0}^{n-1}(-1)^i(i+1)V_i}.
\end{align*}

Comparing the two expressions and using
\[
\chi(\X)=\sum_{i=0}^{n-1}(-1)^i V_i,
\]
we obtain
\[
\prod_{i=0}^{n-1} Z_i^\epsilon(\X,u)^{(-1)^{i+1}}
=
(1-u^n)^{\chi(\X)},
\]
or equivalently, since $Z_0^\epsilon(\X,u)=L(\Gamma,q^{(n-1)/2}u)$,
\[
(1-u^n)^{\chi(\X)}L(\Gamma,q^{(n-1)/2}u)
=
\prod_{k=1}^{n-1}Z_k^\epsilon(\X,u)^{(-1)^{k+1}}.
```

*Plain summary.* This settles the question "is `(1-u^2)^chi` the torsion-like
factor?" **Yes, and provably so.** In the uniform `PGL_n` identity, the zeta
functions of the `k`-geodesics for all facet dimensions `k = 0,...,n-1` are the
determinants of a family of "successor" cochain automorphisms `Phi_i` on
`C_i(X)`; the alternating product of their determinants is a *torsion* and by
standard homological algebra equals the same alternating product taken on
cohomology, where `Phi_i` acts by `1 - u^n`. The result is `(1-u^n)^{chi}`. For
`n = 2` this reduces exactly to Ihara: the numerator `(1-u^2)^{chi(X)}` of the
graph zeta is the determinant of a cochain automorphism over the whole
(vertex, edge) complex, i.e. exactly the object the notebook wants to call a
torsion / supertrace factor.

## C2. `0809.1401` and `0809.1401v1` — Kang–Li (and Kang–Li–Wang), zeta functions of `PGL(3)` complexes

- `0809.1401:main.tex:58,59`
```
\title[Zeta Functions of Complexes Arising from $\PGL(3)$]{Zeta Functions of Complexes Arising from $\PGL(3)$}
\author{Ming-Hsuan Kang and Wen-Ching Winnie Li}
```
- `0809.1401v1:main.tex:144,150`
```
\title[The Zeta Functions of Complexes from $\PGL(3)$: a Representation-theoretic Approach]
{The Zeta Functions of Complexes from $\PGL(3)$: a
Representation-theoretic Approach}



\author{Ming-Hsuan Kang, Wen-Ching Winnie Li and Chian-Jen Wang}
```
(Two distinct papers share the id in the tree: `0809.1401v1` is the
representation-theoretic Kang–Li–Wang version, `0809.1401` the later combinatorial
Kang–Li one.)

**Ihara's theorem for `(q+1)`-regular graphs:**

- `0809.1401:main.tex:103,110`
```
\begin{theorem}[Ihara \cite{Ih}]\label{Ihara}
Let $X$ be a
$(q+1)$-regular graph. Then its zeta function
 is a rational function of the form
$$ Z(X,u) = \frac{(1 - u^2)^{\chi(X)}}{\det(I - Au + qu^2I)},$$
where $\chi(X)$ is the Euler characteristic of $X$
and $A$ is the adjacency matrix of $X$.
\end{theorem}
```

**Theorem C, the 2-dimensional analogue — and the authors' own remark that this
is the "surface vs curve" contrast:**

- `0809.1401:main.tex:260,289`
```
{\bf Theorem C.} {\it
 The zeta function of the finite
complex $X_\G = \Gamma \backslash \B$ can be expressed as
\begin{eqnarray}\label{zeta}
Z(X_\G, u) %&=& \frac{1}{\det(1 - L_E u) \det(1- (L_E)^t u^2)} \\
=  \frac{(1-u^3)^{\chi(X_\G)}}{\det(I-A_1u+qA_2u^2-q^3
u^3I)\det(I + L_Bu)},
\end{eqnarray}
in which $\chi(X_\G)$ is the Euler characteristic of $X_\G$, $A_1$ and $A_2$ are operators on vertices, %$L_E$ (resp. $(L_E)^t$) is the operator on type $1$ (resp. $2$) edges,
and $L_B$ is the operator on pointed chambers in $X_\G$ introduced above.}

Combining Theorems A and B, and noting that the transpose $(L_E)^t$ of $L_E$ is the edge adjacency operator of type 2 edges in $X_\G$, we rephrase the identity (\ref{zeta}) in terms of the
operators on $X_\G$ as
\begin{eqnarray}\label{zetaidentity}
\frac{(1-u^3)^{\chi(X_\G)}}{\det(I-A_1u+qA_2u^2-q^3 u^3I)} =
\frac{\det(I + L_Bu)}{\det(I - L_E u) \det(I - (L_E)^t u^2)}.
\end{eqnarray}
Compared to the parallel identity of operators on a $(q+1)$-regular graph
$X$:
$$\frac{(1 - u^2)^{\chi(X)}}{\det(I - Au + qu^2I)} = \frac{1}{\det(I
- A_eu)},$$ the similarity is reminiscent of the zeta functions
attached to a surface and a curve over a finite field. It is likely that the identity
(\ref{zetaidentity}) expressed in terms of the operators on the
finite complex is a prototype of complex zeta
functions in general. Indeed, the identity on zeta functions in \cite{FLW} for the
$GSp_4(F)$ case is formulated after this. Theorem C was proved in
\cite{KLW} from representation-theoretical viewpoint
by comparing the eigenvalues of the operators in (\ref{zetaidentity}), while
the proof  in this paper explores the combinatorial and group-theoretic viewpoints of the identity.
```

**"Riemann hypothesis" for a complex = Ramanujan:**

- `0809.1401:main.tex:75,80`
```
\begin{abstract} In this paper we obtain a closed form expression of
the zeta function $Z(X_\G, u)$ of a finite quotient {$X_\G$ of the Bruhat-Tits building of
$\PGL_3$ over a nonarchimedean local field $F$ by a discrete cocompact torsion-free subgroup $\Gamma$ of $\PGL_3$}. Analogous to a graph
zeta function, $Z(X_\G, u)$ is a rational function with two different expressions and it satisfies
the Riemann hypothesis if and only if $X_\G$ is a Ramanujan complex.
\end{abstract}
```

- `0809.1401v1:main.tex:1344,1346`
```
Recall also that $X_\Gamma$ is a Ramanujan complex if and only if
the nontrivial zeros of $\det(I - A_1u + qA_2u^2 - q^3u^3I)$ have
absolute value $q^{-1}$ (cf. \cite{Li}, \cite{LSV}).  It is natural
```


*Plain summary.* The `PGL(3)` complex zeta has, next to the vertex
(Hecke) factor, a chamber factor `det(I + L_B u)` appearing with the **opposite**
placement to the edge factors `det(I - L_E u) det(I - (L_E)^t u^2)`, and the
whole is balanced by `(1-u^3)^{chi}`. The authors themselves call the resulting
structure "reminiscent of the zeta functions attached to a surface and a curve
over a finite field" — which is exactly the notebook's "surface-like" reading:
higher facet dimension supplies the extra cohomological degrees, placed in the
numerator or the denominator according to parity.

---

# D. Fermionic / Grassmann proofs of the determinant identities

## D1. `2501.08803` — Matsuura–Ohta, *Fermions and Zeta Function on the Graph* — **the fermionic proof of Bass's identity**

(Same authors as the quantum-Ihara prior art `2204.06424`; already in the tree.)

- `2501.08803:main.tex:114,116`
```
\title{Fermions and Zeta Function on the Graph}
\author[1]{So Matsuura\thanks{s.matsu@keio.jp}}
\author[2]{Kazutoshi Ohta\thanks{kazutoshi.ohta@mi.meijigakuin.ac.jp}}
```

- `2501.08803:main.tex:133,140`
```
We propose a novel fermionic model on the graphs. %way to construct fermions on graphs.
%We introduce a Dirac operator defined by a deformed incidence matrix on the graph, and 
%we show that the partition function of the fermion model is expressed in terms of the inverse of the graph zeta function.
The Dirac operator of the model consists of deformed incidence matrices on the graph %and mass terms 
and the partition function is given by the inverse of the graph zeta function.
We find that the coefficients of the inverse of the graph zeta function, 
which is a polynomial of finite degree in the coupling constant, 
%and we give an interpretation on the meaning of the polynomial from the viewpoint of fermionic cycles.
```

**The Grassmann partition function evaluates to the Ihara-side expression, with
the `(1-t^2)^{n_E-n_V} = (1-t^2)^{-chi}` prefactor coming out as a Schur
complement of the Dirac operator:**

- `2501.08803:main.tex:750,755`
```
Then, the determinant of the Dirac operator can be evaluated as 
\be
\det \left(\slashed{D}+{\cal M}\right)
=(1-t^2)^{n_E-n_V}\det \Delta_{q,u}=\zeta_\Gamma(q,u)^{-1}
\, ,
\ee
```

**The same fermion determinant evaluated the other way gives the Hashimoto
(non-backtracking) expression — hence a fermionic proof of Bass's identity:**

- `2501.08803:main.tex:811,826`
```
which yields the determinant of the Dirac operator 
associated with the Hashimoto expression \cite{Hashimoto1990ONZA}, 
\be
\det \left(\slashed{D}+{\cal M}\right) =
\det\left(I_{2n_E}-qB_u\right)\, ,
\ee
since $\det(I_{n_E}-t J)=(1-t^2)^{n_E}$.
This equivalence of the two representations of the fermion determinant also shows that the equivalence of the Ihara and Hashimoto expressions
\cite{bass1992ihara}
\be
\begin{split}
\zeta_\Gamma(q,u)^{-1}&=
(1-t^2)^{n_E-n_V}\det \Delta_{q,u}\\
&=\det\left(I_{2n_E}-qB_u\right)\, .
\end{split}
\ee
```

**The Dirac operator is off-diagonal between the VERTEX block and the (two-component)
EDGE block — a chiral / bipartite `Z_2` structure, which is the parity carrier:**

- `2501.08803:main.tex:630,648`
```
Combining the deformed incidence matrices, we define a Dirac operator as 
\be
\slashed{D} = \alpha\begin{pmatrix}
0 & \Lt_{q,u}^T & L_{q,u}^T\\
L_{q,u} & 0 & 0 \\
\Lt_{q,u} & 0 & 0
\end{pmatrix}\ ,
\ee
where $\alpha=\sqrt{\frac{q}{1-t^2}}$ is a normalization constant introduced for later convenience.
%The Dirac operator is acting on three component fermion
Corresponding to the structure of this operator, we introduce fermions
\be
\Psi=(\xi, \psi,\psit)^T,\qquad
\bar{\Psi} = (\bar{\xi},\bar{\psi},\bar{\psit}),
\label{eq:fermions on the graph}
\ee
where
$\xi^v$ and $(\psi^e,\psit^e)$ are Grassmann variables defined on $V$ and $E$, respectively, 
and $\bar\xi^v$ and $(\bar\psi^e,\bar\psit^e)$ are their complex conjugate.
```

- `2501.08803:main.tex:192`
```
In addition, the Dirac operator possesses the so-called $\gamma_5$-hermiticity, which allows us to construct the overlap fermion on the graph.
```

**Answer to "do vertex and edge fermions enter with opposite Grassmann parity or
sign?"** — Not by an explicit sign in the measure. All of `xi, psi, psit` are
ordinary Grassmann variables (`2501.08803:main.tex:647`), entering the same
Berezin integral `D Psi D bar Psi` with the same parity. The `Z_2` structure is
**structural, not a sign**: `Dslash` is block *off-diagonal* between the
`n_V`-dimensional vertex block and the `2 n_E`-dimensional edge block (zeros on
both diagonal blocks), i.e. a chiral/bipartite Dirac operator with a
`gamma_5`-hermiticity. The mass operator `M` is block diagonal, `I_{n_V}` on
vertices and the `2n_E x 2n_E` block `[[I, -tI],[-tI, I]]` on edges
(`2501.08803:main.tex:700,707`), so the edge-reversal involution `J` lives
entirely inside the edge block. When the determinant is Schur-complemented, the
vertex block yields `det Delta_{q,u}` and the edge block yields
`det(I_{n_E} - tJ) = (1 - t^2)^{n_E}`; the exponent in
`(1-t^2)^{n_E - n_V} = (1-t^2)^{-chi}` is exactly the **difference of the
dimensions of the two blocks**. So in this model the Euler characteristic in the
Ihara zeta is the *index-like* difference `dim(edge sector) - dim(vertex sector)`
of a chiral Dirac operator — the closest thing in the literature to the
notebook's "the `chi` exponent is a supertrace".

**The signs in the cycle expansion are called a Witten index by the authors:**

- `2501.08803:main.tex:1114`
```
The cycle M\"obius function does not allow the overlapping of directed edges due to the exclusion principle, and its signature makes it an alternating sum according to the number of the fermionic cycles, like the Witten index.
```

The same Berezin integral is used again to derive the zeta directly from the
non-backtracking matrix `B_u`:

- `2501.08803:main.tex:1028,1030`
```
where $\boldsymbol{\eta}=(\eta_{e_1}, \cdots,\eta_{e_{n_E}},\eta_{\bar{e}_1},\cdots, \eta_{\bar{e}_{n_E}})^T$ and $\bar{\boldsymbol{\eta}}=(\bar{\eta}_{e_1}, \cdots,\bar{\eta}_{e_{n_E}},\bar{\eta}_{\bar{e}_1},\cdots, \bar{\eta}_{\bar{e}_{n_E}})$ are independent $2n_E$-dimensional Grassmann valued vectors,
and we have used the nature of the Grassmann integral that the integrand must contain $2n_E$ Grassmann variables in the third line. 
Note that we have to normalize the measure of the Grassmann integral as 
```

*Plain summary.* **This is the fermionic proof of Bass's identity the question
asked for, and it exists.** Put a Grassmann field on vertices and two on each
oriented edge, take the Dirac operator built from deformed incidence matrices
plus a mass term; the Berezin integral gives `det(D + M)`. Block-decomposing that
determinant one way gives `(1-t^2)^{n_E-n_V} det Delta_{q,u}` (the Ihara/Bass
side, with the Euler-characteristic prefactor); decomposing it the other way
gives `det(I - q B_u)` (the Hashimoto/non-backtracking side). The equality of the
two decompositions *is* Bass's identity (in Bartholdi-deformed form, `u` the bump
parameter). Crucially, `(1-t^2)^{-chi}` arises as a *fermionic determinant of the
edge-reversal involution `J`*: `det(I_{n_E} - tJ) = (1-t^2)^{n_E}`. That is the
`Z_2`/parity object the notebook is looking for.

## D2. `math/9806037` — Foata–Zeilberger, *A Combinatorial Proof of Bass's Evaluations of the Ihara-Selberg Zeta Function for Graphs*

- `math/9806037:main.tex:564,570`
```
A Combinatorial Proof of Bass's Evaluations\\
of the Ihara-Selberg Zeta
Function for Graphs
\endtitle

\author 
Dominique Foata and Doron Zeilberger
```

**The two Bass evaluations, with the `(1-u^2)^{c_1-c_0}` factor:**

- `math/9806037:main.tex:686,692`
```
\eta(u)&=\det (I-u\,T),&(1.2)\cr
\noalign{\hbox{second, as a product}}
\eta(u)&=(1-u^2) ^{c_1-c_0}\det \Delta(u),&(1.3)\cr}
$$
where $\Delta(u)$ is a matrix of order~$c_0$ that depends on
the {\it connectedness} of the {\it vertices}. The definitions of
$T$ and $\Delta(u)$ will be given in full details later on.
```
(`c_0 = #vertices`, `2c_1 = #oriented edges`, so `c_1 - c_0 = -chi`.)

**The mechanism is a sign-reversing involution — the combinatorial shadow of a
fermionic cancellation:**

- `math/9806037:main.tex:1127,1130`
```
The proof of Theorem 4.1 is based on an {\it involution}
$\pi\mapsto \pi'$ of ${\Cal D}\setminus {\Cal G}$ 
such that $\deg \pi+\deg \pi'=0$ mod~2 that is defined as
follows. 
```

**The endgame, where the `(1-u^2)` factor is a determinant of the edge-reversal
matrix `J` — the same object as Matsuura–Ohta's:**

- `math/9806037:main.tex:1953,1960`
```
we have ${\text {Com}}=TJ$.
Accordingly, if we let $v(i)=u^2$ for all $i$ and replace all
the $u(i,j)$ by $-u$ in the definition of~$A$, we get
$A=I-u(T+J)+u^2TJ=(I-uT)(I-uJ)$. But
$\det(I-uJ )$ is clearly equal to $(1-u^2)^{c_1}$. Hence
$\det \Delta \prod\limits_{i=1}^n (1-u^2)^{Q(i)}=\det\Delta
(1-u^2)^{2c_1-c_0}=\det (1-uT)\det(I-uJ)$, so that
$\det(I-uT)=\det\Delta(1-u^2)^{c_1-c_0}$, which is Bass's
```

*Plain summary.* Foata–Zeilberger's proof is combinatorial, not Grassmann: the
key device is a **sign-reversing involution with `deg pi + deg pi' = 0 mod 2`**,
i.e. pairing terms of opposite parity so they cancel. That is the same cancellation
that a Berezin integral performs automatically. And the `(1-u^2)^{c_1-c_0}` factor
comes out here, as in Matsuura–Ohta, from `det(I - uJ) = (1-u^2)^{c_1}` where `J`
is the edge-reversal involution. The parity structure of the graph zeta is
carried by the involution `J : e -> bar e`.

## D3. `0706.1509` — Caracciolo–Sokal–Sportiello, *Grassmann Integral Representation for Spanning Hyperforests* (NEW)

- `0706.1509:hyper_v4b.tex:253,257`
```
Grassmann Integral Representation \\ for Spanning Hyperforests}

\author{Sergio Caracciolo$^{1}$, Alan D. Sokal$^{2,3}$,
        Andrea Sportiello$^{1}$  \\[4mm]
\hspace*{-1cm}
```

- `0706.1509:hyper_v4b.tex:284,294`
```
\begin{abstract}
Given a hypergraph $G$, we introduce a Grassmann algebra over the
vertex set, and show that a class of Grassmann integrals permits
an expansion in terms of spanning hyperforests.
Special cases provide the generating functions for rooted and unrooted
spanning (hyper)forests and spanning (hyper)trees.
All these results are generalizations of Kirchhoff's matrix-tree theorem.
Furthermore, we show that the class of integrals describing
unrooted spanning (hyper)forests is induced by a theory with an
underlying $\OSP(1|2)$ supersymmetry.
\end{abstract}
```

- `0706.1509:hyper_v4b.tex:320,325`
```
Like all determinants, those arising in Kirchhoff's theorem
can be rewritten as Gaussian integrals
over fermionic (Grassmann) variables.
Indeed, the use of Grassmann--Berezin calculus~\cite{Berezin}
has provided an interesting short-cut toward the classical matrix-tree result
as well as generalizations thereof~\cite{abdes,us_prl}.
```

*Plain summary.* The other half of the graph story: the **spanning-tree**
invariant `kappa(X)`, which by Hashimoto's formula (§B3) is the special value of
the Ihara zeta at `u=1`, has a Grassmann/Berezin representation, and the
unrooted-forest version is governed by an honest `OSP(1|2)` **supersymmetry**.
So both sides of "the Ihara zeta at `u=1` is `-2 chi kappa`" have fermionic
proofs in the literature: the determinant identity (Matsuura–Ohta, §D1) and the
spanning-tree count (Caracciolo–Sokal–Sportiello). Not found: a paper joining the
two into a single supersymmetric statement about `(1-u^2)^chi`.

## D3b. `cond-mat/0403271` — Caracciolo–Jacobsen–Saleur–Sokal–Sportiello, *Fermionic field theory for trees and forests*

The PRL companion of §D3 (already in the tree).

- `cond-mat/0403271:main.tex:141,141`
```
\title{Fermionic field theory for trees and forests}
```
(authors on `:143`, `:147`, `:151`, `:157` and the `\author{Andrea Sportiello}`
line in the affiliation block).

- `cond-mat/0403271:main.tex:168,182`
```
\begin{abstract}
We prove a generalization of Kirchhoff's matrix-tree theorem
in which a large class of combinatorial objects are represented
by non-Gaussian Grassmann integrals.
As a special case, we show that unrooted spanning forests,
which arise as a $q \to 0$ limit of the Potts model,
can be represented by a Grassmann theory involving a Gaussian term
and a particular bilocal four-fermion term.
We show that this latter model can be mapped,
to all orders in perturbation theory,
onto the $N$-vector model at $N=-1$ or, equivalently,
onto the $\sigma$-model taking values in the unit supersphere in $\R^{1|2}$.
It follows that, in two dimensions,
this fermionic model is perturbatively asymptotically free.
\end{abstract}
```

## D3c. `math/0306396` — Abdesselam, *Grassmann-Berezin Calculus and Theorems of the Matrix-Tree Type*

- `math/0306396:Matrixtreecor.tex:163,172`
```
\title{Grassmann-Berezin Calculus and Theorems of the 
Matrix-Tree Type }

\author{Abdelmalek Abdesselam \\
\\
{\small LAGA, Institut Galil\'ee, CNRS UMR 7539}\\
{\small  Universit{\'e} Paris XIII}\\
{\small Avenue J.B. Cl{\'e}ment, F93430 Villetaneuse, France}\\
{\small email: abdessel@math.univ-paris13.fr}
}
```

- `math/0306396:Matrixtreecor.tex:181,193`
```
We prove two generalizations of the matrix-tree theorem.
The first one, a result essentially due to Moon for which we provide
a new proof, extends the ``all minors'' matrix-tree theorem
to the ``massive'' case where no condition on row or column sums  
is imposed. The second generalization,
which is new, extends the recently discovered
Pfaffian-tree theorem of Masbaum and Vaintrob into
a ``Hyperpfaffian-cactus'' theorem.
Our methods are noninductive, explicit and make critical use
of Grassmann-Berezin calculus that was developed for the needs of
modern theoretical physics.
}
}
```

*Plain summary of D3/D3b/D3c together.* The matrix-tree side of the Ihara zeta —
the spanning-tree number `kappa(X)` that Hashimoto's formula pins to `h'_X(1)`
(§B3) — has a complete Grassmann–Berezin theory: all-minors and Pfaffian/
hyperpfaffian generalisations (Abdesselam), unrooted forests as a non-Gaussian
Grassmann theory with `OSP(1|2)` supersymmetry (Caracciolo et al.). Knill (§B7)
supplies the even/odd (supertrace) refinement of the same object.

## D4. `1709.06052` — Aizenman–Warzel, *Kac-Ward formula and its extension to order-disorder correlators through a graph zeta function* (NEW)

- `1709.06052:2018_KW_JSP__Nov1.tex:142,149`
```
\title{\Large \bf 
%Planar Ising model's free energy and order-disorder correlators through a graph zeta function \\[3ex] 
Kac-Ward formula and its extension to  order-disorder correlators through a graph zeta function
}


\author{\normalsize Michael Aizenman\footnote{Departments of Physics and Mathematics,  Princeton University,  Princeton NJ 08544, USA. }
\and  \normalsize
```

**The Bowen–Lanford/Ihara-type zeta for an arbitrary non-backtracking flow
matrix:**

- `1709.06052:2018_KW_JSP__Nov1.tex:305,312`
```
\begin{theorem} \label{thm:Ihara} Let  $\mathcal{M}$ be a non-backtracking  $\widehat{\mathcal E}\times \widehat{\mathcal E} $ flow  matrix over a finite graph. 
Then  for all  $u \in \C$ such that 
$  \label{eq:norm_M}
|u|^{-1}  >  \| \mathcal{M} \|_{\infty} \ := \  \max_{e\in \widehat{\mathcal{E}}}   \sum_{e'\in\widehat{\mathcal{E}}} |\mathcal{M}_{e,e'}| \,      
$:
\be  \label{eq:zetaM}
  \det (1 - u\mathcal{M}) \ =\  \prod_{p} \left[ 1 - u^{|p|}\chi_{\mathcal{M}}(p) \right] \quad  \left[=: \, \zeta_M(u)^{-1}\right]
\ee 
```

**The explicit "the cancellations are fermionic" statement:**

- `1709.06052:2018_KW_JSP__Nov1.tex:346`
```
In view of the simplicity of the argument, it may be worth stressing that the  limitations placed on the loops in \eqref{eq:zetaM}  leave the possibility of self intersection, multiple crossing of  edges, and arbitrary repetitions of  sub-loops.  The product in \eqref{eq:zetaM}  is over an infinite collection of factors, whose series expansions  yield terms with arbitrary powers of $u$.   However on the left side is a polynomial in  $u$.  Thus contained in  this zeta function relation is an infinite collection of combinatorial cancellations reflecting the fact that the loop ensemble has a fermionic nature. \\
```

Relation to the Ihara zeta, made explicit:

- `1709.06052:2018_KW_JSP__Nov1.tex:342`
```
The meromorphic function $\zeta_M$ defined in \eqref{eq:zetaM}  is related to Ihara's graph zeta function, whose usual definition is in terms of site-indexed paths and $\mathcal{V}\times \mathcal{V}$ matrices.  In that case the customary non-backtracking restriction on $p$  needs to be added explicitly.   Also the statement and proof of the corresponding result are a bit more involved.  Further background on this topic, other extensions, and graph theoretic applications, can be found in, e.g., \cite{ST96,Smi09}.   
```

*Plain summary.* Aizenman–Warzel use a graph zeta function (Bowen–Lanford form
`det(1-uM) = prod_p (1 - u^{|p|} chi(p))`, for arbitrary non-backtracking flow
matrices `M`) as the engine of a short Kac–Ward derivation of the planar Ising
free energy. They say in so many words that the reason the infinite Euler product
collapses to a polynomial is that **"the loop ensemble has a fermionic nature"**.
This is the physics literature's own statement of the notebook's thesis, for the
graph zeta.

## D5. `0809.3479` / `0809.3481` — Chernyak–Chertkov, *Fermions and Loops on Graphs I, II* (already in the tree)

- `0809.3479:LCD7.tex:11,13`
```
\title{Fermions and Loops on Graphs. I. Loop Calculus for Determinant}
\author {Vladimir Y. \surname{Chernyak}$^{a,b}$}
\author{Michael \surname{Chertkov}$^{b}$}
```

From the abstract:

- `0809.3479:LCD7.tex:23,30`
```
This paper is the first in the series devoted to evaluation of the partition function in
statistical models on graphs with loops in terms of the Berezin/fermion integrals. The paper
focuses on a representation of the determinant of a square matrix
% we do not even need to require that the matrix is positive
in terms of a finite series, where each term corresponds to a loop on the graph. The representation
is based on a fermion version of the Loop Calculus, previously introduced by the authors for
graphical models with finite alphabets. Our construction contains two levels. First, we represent
the determinant in terms of an integral over anti-commuting Grassman variables, with some
```

*Plain summary.* A Berezin/Grassmann loop expansion for `det` of an arbitrary
matrix on a graph, with a BP gauge fixing that turns the expansion into a sum over
(generalised) loops. Same technology as D1/D4 but organised as a loop calculus;
relevant machinery if the notebook wants a fermionic derivation of the Kraus
Ihara–Bass formula (`notes/quantum-ihara-general.md`) rather than the linear-algebra one.
Part II is `0809.3481:MDM8.tex:16` —
`\title{Fermions and Loops on Graphs. II. Monomer-Dimer Model as Series of Determinants.}`.

## D6. What was NOT found on the fermionic side

No source was found in which the Ihara/Hashimoto determinant identity itself is
proved by an explicit **supertrace** argument (a `Z_2`-graded trace with a parity
operator `(-1)^F`). The two closest are:

- Matsuura–Ohta (§D1): the parity is structural — a chiral, block-off-diagonal
  Dirac operator whose two blocks are the vertices and the edges, with the
  `(1-t^2)^{n_E-n_V}` exponent equal to the *difference of the two block
  dimensions*. They call the sign pattern of the cycle expansion a "Witten
  index" (`2501.08803:main.tex:1114`) but never write a supertrace of the
  transfer operator.
- Knill (§B7): an honest **super** pseudo-determinant statement,
  `A(G) = SDet(D) = prod_k Det(D_k)^{(-1)^k}`, explicitly labelled "fermionic"
  versus "bosonic" — but for the analytic *torsion* of the Whitney complex, not
  for the Ihara zeta.

Searched: `"supertrace" graded proof Hashimoto determinant identity
non-backtracking graph zeta Z2-graded`; `supersymmetric OR supersymmetry OR
Grassmann proof "Ihara zeta" OR "Bass formula" graph determinant` — returned only
combinatorial (Lyndon-word, involution, linear-algebra) proofs. **The gap: nobody
has joined Knill's `SDet` statement to the Ihara/Bass determinant identity.** That
join is exactly what the notebook's "zeta is a supertrace" would be, on a graph.

---

# E. Deninger and Connes — cross-reference only

Item 4 of the task (Deninger's `H^0` = pole / `H^1` = zeros, the Lefschetz trace
formula reading; Connes's absorption spectrum and the minus sign) **is already
byte-cited in `notes/extract/riemann-cmps-sources.md`**, sections A and B. The
relevant anchors, not repeated here:

- `math/0505354:main.tex:308-312` — the conjectural `zeta_K(s) = prod_{i=0}^2
  det_infty(...)^{(-1)^{i+1}}`, quoted at `riemann-cmps-sources.md` §A1.
- `math/0505354:main.tex:316-326` — `H^0 = R` with `Theta = 0`, `H^1` infinite
  dimensional carrying the nontrivial zeros, `H^2 = R` with `Theta = id`; §A1.
- `math/0505354:main.tex:874-880` — the Lefschetz/explicit formula
  `sum_i (-1)^i Tr(phi^*|H^i) = 1 - sum_rho e^{t rho} + e^t`, i.e. the
  supertrace with the zeros entering with a minus sign; §A1.
- `1807.06400`, `0709.2801` — Deninger's later constructions; §§A2–A3.
- `math/9811068:main.tex:194-209`, `:469-476`, `:556-581` — Connes's absorption
  spectrum, the "overall minus sign" mismatch with Selberg, and its resolution by
  `H^1_et`; `riemann-cmps-sources.md` §B1.

The only thing worth adding here is the observation that Deninger's
`prod_{i=0}^2 (...)^{(-1)^{i+1}}` and Deitmar's
`prod_{l=0}^{dim N} Z_{sigma_l}(s + l|alpha|)^{(-1)^l}` (§A1) and Kang–Yu's
`prod_{k=1}^{n-1} Z_k^epsilon(X,u)^{(-1)^{k+1}}` (§C1) and Dyatlov–Zworski's
`zeta_R = zeta_1/(zeta_0 zeta_2)` (§A2) are four instances of one and the same
shape, in four different categories (arithmetic schemes, locally symmetric
spaces, Bruhat–Tits buildings, Anosov flows).

---

# F. The quantum side

## F1. What exists

**`1507.01194` — Matsue–Ogurisu–Segawa, *Quantum walks on simplicial complexes*.**

- `1507.01194:QW-simplicial.tex:56,59`
```
\title{Quantum walks on simplicial complexes}

\author{Kaname Matsue\thanks{The Institute of Statistical Mathematics, Tachikawa, Tokyo, 190-8562, Japan} $^{,}$\footnote{(Corresponding author) \tt kmatsue@ism.ac.jp} ,\ Osamu Ogurisu\thanks{Division of Mathematical and Physical Sciences,
  Kanazawa University, Kanazawa, Ishikawa 920-1192, Japan} $^{,}$\footnote{\tt ogurisu@staff.kanazawa-u.ac.jp}$\ $ and Etsuo Segawa\thanks{Graduate school of Information Sciences, Tohoku University, Aoba, Sendai, 980-8579, Japan}  $^{,}$\footnote{\tt e-segawa@m.tohoku.ac.jp}}
```

- `1507.01194:QW-simplicial.tex:62,68`
```
\begin{abstract}
We construct a new type of quantum walks on simplicial complexes as a natural extension of the well-known Szegedy walk on graphs.
One can numerically observe that our proposing quantum walks possess linear spreading and localization
as in the case of the Grover walk on lattices.
Moreover, our numerical simulation suggests that localization of our quantum walks reflect not only topological but also geometric structures.
On the other hand, our proposing quantum walk contains an intrinsic problem concerning exhibition of nontrivial behavior, which is not seen in typical quantum walks such as Grover walks on graphs.
\end{abstract}
```

**Verified negative:** the string `zeta` does not occur anywhere in
`1507.01194:QW-simplicial.tex` (checked with
`grep -c -i zeta refs/src/1507.01194/QW-simplicial.tex` → 0; likewise `Ihara`,
`backtrack`). So this paper defines a quantum walk on a complex but **attaches
no zeta function to it**.

**`2307.03321` — Bradshaw–LaBorde et al., *Quantum Entanglement & Purity Testing:
A Graph Zeta Function Perspective* (NEW).**

- `2307.03321:main.tex:53,53`
```
\title{Quantum Entanglement \& Purity Testing: A Graph Zeta Function Perspective}
```

- `2307.03321:main.tex:68,70`
```
\begin{abstract}
    We assign an arbitrary density matrix to a weighted graph and associate to it a graph zeta function that is both a generalization of the Ihara zeta function and a special case of the edge zeta function. We show that a recently developed bipartite pure state separability algorithm based on the symmetric group is equivalent to the condition that the coefficients in the exponential expansion of this zeta function are unity. Moreover, there is a one-to-one correspondence between the nonzero eigenvalues of a density matrix and the singularities of its zeta function. Several examples are given to illustrate these findings.
\end{abstract}
```

*Plain summary.* The only "quantum zeta" found: a **density matrix** is turned
into edge weights on a complete graph and its edge zeta is formed. The
singularities correspond to the nonzero eigenvalues of `rho`; the authors call
this "a variant of the Hilbert-Pólya conjecture associated to this zeta
function". It is **not** a zeta of a quantum channel, not Kraus-weighted, and not
on a complex — it is an ordinary edge zeta with `rho`-derived scalar weights.

**`2602.15180` — Iyer–Jain–Jordan–Somma, explicit Ramanujan quantum expanders.**
(Re-fetched by the other worker; `main.tex` is now populated, 1862 lines.)

- `2602.15180:main.tex:222,226`
```
\title{Efficient quantum circuits for high-dimensional representations of $SU(n)$ and Ramanujan quantum expanders}

\author[1]{Vishnu~Iyer}
\author[1,2]{Siddhartha~Jain}
\author[2]{Stephen~Jordan}
```

What "Ramanujan quantum expander" means there — a *spectral gap* statement about
a channel's second eigenvalue, with no zeta and no complex anywhere:

- `2602.15180:main.tex:598,604`
```
\begin{corollary}[Explicit Ramanujan quantum expanders]
\label{cor:expanders}
    For any $D = p+1$ where p is a prime congruent to 1 modulo 4, there exists explicit
    quantum circuits that implement a Ramanujan quantum expander
    of degree $D$ and dimension $N$, within error $\epsilon >0$, in time polynomial in $\log(N)$ and $\log(1/\epsilon)$. For this quantum expander,
    the second eigenvalue can get arbitrarily close to the optimal bound $\lambda \le 2 \sqrt{D-1}/D$.
\end{corollary}
```

**Verified negative (byte-level).** In `2602.15180:main.tex`:
`grep -c -i zeta` → `0`; `grep -c -i ihara` → `0`; `grep -c -i simplicial` → `0`.
So the strongest "Ramanujan quantum expander" paper in the literature contains no
zeta function at all: the Ramanujan property there is the Hastings/Alon–Boppana
bound `lambda <= 2 sqrt(D-1)/D` on the channel's second eigenvalue, exactly as the
notebook already uses it, and never a Riemann-hypothesis-for-a-zeta statement.

**Other Ramanujan-complex material already in the tree:** `1605.02664` (First,
the Ramanujan property for simplicial complexes), `1701.00154` (Kamber,
`L^p`-expander complexes), `1712.02526` (Lubotzky, high-dimensional expanders),
`1702.05452` (Lubetzky–Lubotzky–Parzanchevski, random walks on Ramanujan
complexes and digraphs — this is where the higher-dimensional "geodesic flow"
non-backtracking operator lives), `1804.08028` (Ramanujan graphs and digraphs).
None of these carries a *quantum-channel* zeta.

## F2. What was NOT found (quantum)

Searches run, all negative for the target object:

1. `"quantum expander" "Ramanujan complex" high-dimensional expander quantum
   channel arXiv` — returns quantum expanders (channels, no complexes) and
   Ramanujan complexes (complexes, no channels), never both.
2. `quantum channel zeta function simplicial complex "Ramanujan complex" quantum
   expander Kraus non-backtracking superoperator` — no hit.
3. `"quantum Ihara zeta" OR "zeta function of a quantum channel" OR "Kraus" zeta
   function graph` — hits are the Konno–Sato "quantum walk / zeta correspondence"
   family (`1103.0079`, already in the tree, and its successors: Grover/Zeta,
   Walk/Zeta, absolute zeta) and `2307.03321`. All of these are **scalar** zetas
   whose transfer matrix happens to be unitary; none is a zeta of a CPTP map.
4. `"zeta function" "quantum walk" hypergraph OR "simplicial complex" Ihara
   Konno Segawa` — the quantum-walk/zeta correspondence exists only for graphs;
   `1507.01194` (walks on complexes) has no zeta.
5. `arXiv "quantum walks on simplicial complexes" Matsue Ogurisu Segawa` — only
   `1507.01194` and its search sequel (`1707.00156`, *Quantum Search on Simplicial
   Complexes*), neither with a zeta.

**Conclusion for the quantum side.** No quantum (channel / Kraus /
unitary-weighted) zeta function *of a complex or hypergraph* exists in the
literature as far as these searches reach. The two known quantum-flavoured zetas
are (i) the Ad(U)-weighted Ihara zeta of a **graph** (Matsuura–Ohta `2204.06424`,
already recorded as prior art) and (ii) the density-matrix edge zeta of a
**complete graph** (`2307.03321`). The combination "quantum zeta of a complex"
— which is what a graded/supertrace quantum Ihara–Bass on a 2-complex would be —
appears to be open.

---

# G. Not found

Searches that returned nothing relevant:

- **A supertrace / `Z_2`-graded proof of Hashimoto's or Bass's determinant
  identity.** (§D6.) Only Berezin-integral (Matsuura–Ohta), sign-reversing
  involution (Foata–Zeilberger), Lyndon-word, and linear-algebra proofs.
- **A Grassmann/Berezin proof of Bass's identity predating Matsuura–Ohta 2025.**
  The Kac–Ward literature (Lis `1502.04322`, Cimasoni, Aizenman–Warzel
  `1709.06052`) uses graph zetas and calls the cancellations fermionic, but does
  not present itself as a proof of Bass. The Grassmann matrix-tree literature
  (Abdesselam `math/0306396`, Caracciolo et al. `cond-mat/0403271`, `0706.1509`)
  treats the *tree* side, never the non-backtracking determinant.
- **A supertrace statement joining Knill's `SDet(D)` (`2201.09412`) to the Ihara
  zeta.** Knill's paper does not mention the Ihara zeta; the Ihara literature does
  not mention `SDet`. (Verified: `grep -c -i ihara refs/src/2201.09412/reidemeister.tex`.)
- **Any zeta function in `2602.15180`, `1507.01194`, or `1605.02664`.** Verified
  by `grep -c -i zeta`: `refs/src/2602.15180/main.tex` → 0;
  `refs/src/1507.01194/QW-simplicial.tex` → 0;
  `refs/src/1605.02664/ram_complexes_v32.tex` → 8, but all eight are the Greek
  letter `\zeta` used as a variable (an ordering map at `:3767,3768`, a root of
  unity at `:4916,4933`), not a zeta function. So First's Ramanujan-property
  paper defines Ramanujan-ness purely spectrally, with no zeta at all.
- **Any statement in the graph literature that `(1-u^2)^{chi}` "is a Reidemeister
  torsion".** The nearest byte-verified statements are (i) Hoffman's
  torsion-of-complexes reformulation of Bass's proof, cited from
  `2607.21262:main.tex:352,356`, and (ii) Kang–Yu's own derivation of
  `(1-u^n)^{chi}` as `prod_i det(Phi_i | H^i)^{(-1)^i}`
  (`2607.21262:main.tex:2459,2474`). Hoffman's own text is not on arXiv.
- **Fried's papers on arXiv.** None of D. Fried's papers is on arXiv (checked the
  arXiv listing; bibliographic data recorded in §B1 instead).
- **Juhl's book on arXiv.** Not on arXiv (§B2).
- **Northshield 1998 / Hashimoto 1990 / Bass 1992 on arXiv.** None on arXiv;
  bibliographic data byte-cited from arXiv bibliographies in §B3.
- **A quantum-channel zeta of a simplicial complex or hypergraph** (§F2).
- **"Ihara zeta and Reidemeister torsion" as a titled paper.** Does not exist; the
  closest are `2104.00215` (twisted Alexander = torsion, as an Ihara zeta of a
  knot diagram) and `2303.11226` (combinatorial zeta, `L^2`-torsion remark).

---

# H. Line-range re-check commands

```sh
cd refs/src
sed -n '269p'          dg-ga/9511006/main.tex
sed -n '1153,1168p'    dg-ga/9511006/main.tex
sed -n '843,855p'      1606.04560/zazi.tex
sed -n '877,885p'      1606.04560/zazi.tex
sed -n '229,236p'      1807.01189/main.tex
sed -n '1157,1168p'    2009.08558/contact5d.tex
sed -n '78,84p'        2009.08558/contact5d.tex
sed -n '170,186p'      2607.21262/main.tex
sed -n '2459,2487p'    2607.21262/main.tex
sed -n '260,289p'      0809.1401/main.tex
sed -n '75,80p'        0809.1401/main.tex
sed -n '1344,1346p'    0809.1401v1/main.tex
sed -n '750,755p'      2501.08803/main.tex
sed -n '811,826p'      2501.08803/main.tex
sed -n '686,692p'      math/9806037/main.tex
sed -n '1953,1960p'    math/9806037/main.tex
sed -n '284,294p'      0706.1509/hyper_v4b.tex
sed -n '305,312p'      1709.06052/2018_KW_JSP__Nov1.tex
sed -n '346p'          1709.06052/2018_KW_JSP__Nov1.tex
sed -n '191,204p'      2303.11226/zeta_triangulations9.tex
sed -n '941,955p'      2310.15619/main.tex
sed -n '68,70p'        2307.03321/main.tex
sed -n '53p'           2307.03321/main.tex
sed -n '62,68p'        1507.01194/QW-simplicial.tex
sed -n '809,817p'      1807.01189/main.tex
sed -n '11,13p'        0809.3479/LCD7.tex
sed -n '1193,1212p'    dg-ga/9511006/main.tex
sed -n '313,318p'      2503.19641/Spanning_trees_and_their_relations_in_Galois_covers.tex
sed -n '42,52p'        2201.09412/reidemeister.tex
sed -n '545,556p'      2201.09412/reidemeister.tex
sed -n '365,378p'      1602.00664/main.tex            # latin1: use sed, not grep
sed -n '740,755p'      1602.00664/main.tex
sed -n '630,648p'      2501.08803/main.tex
sed -n '1114p'         2501.08803/main.tex
sed -n '168,182p'      cond-mat/0403271/main.tex
sed -n '181,193p'      math/0306396/Matrixtreecor.tex
sed -n '598,604p'      2602.15180/main.tex
grep -c -i zeta        1507.01194/QW-simplicial.tex   # expect 0
grep -c -i zeta        2602.15180/main.tex            # expect 0
grep -c -i ihara       2201.09412/reidemeister.tex    # expect 0
```
