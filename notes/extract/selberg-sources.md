# Sources for the continuous (Selberg) analogue of the quantum Ihara zeta

Written 2026-09-12 by the source-acquisition worker. Every quote below was copied
out of the arXiv **TeX source** in `refs/src/<id>/` (fetched by
`refs/fetch_sources.sh`, hashes in `refs/manifest.sha256`) and is cited as
`<id>:<file>:<line-range>`; each quote is whole and contiguous in the lines
stated, so it can be re-checked with `sed -n '<a>,<b>p'`. Preference throughout:
TeX source, never PDF text.

New ids appended to `refs/fetch_sources.sh` for this note:
`1306.4203 1403.0256 math/0407288 math/0402356 1511.04265 1606.04560 1607.08053 1108.5659 1710.00603`.

---

## F1. Guillemin (flat) trace formula for an Anosov flow

**arXiv:1306.4203** — `1306.4203:zeta.tex:85-87` `\title[Dynamical zeta functions via microlocal analysis]%` /
`{Dynamical zeta functions for Anosov flows\\` / `via microlocal analysis}`;
authors `1306.4203:zeta.tex:88` `\author{Semyon Dyatlov}` and
`1306.4203:zeta.tex:92` `\author{Maciej Zworski}`.

Guillemin's formula, scalar version (eq. `eq:ABG`):

- `1306.4203:zeta.tex:260-264`
```
\label{eq:ABG}  \tr^\flat e^{-it P }  = 
\sum_{
    \gamma} 
\frac{ T_\gamma^\#     \delta (
  t - T_\gamma ) } { | \det ( I - \mathcal P_\gamma ) |} , \ \ t > 0
```

Form-valued version, attributed to Guillemin, with the conventions spelled out (eq. `eq:guill`):

- `1306.4203:zeta.tex:500-505`
```
\label{eq:guill}   \tr^\flat e^{-i t\mathbf P } |_{ C^\infty ( X ;
\mathcal E^k_0 )} 
 =   \sum_{ \gamma }
\frac{ T_\gamma^\#   \tr ( \wedge^k \mathcal P_\gamma ) \,  \delta (
  t - T_\gamma ) } { | \det ( I - \mathcal P_\gamma ) 
  |} , \ \  t > 0 , \end{equation}
```

- `1306.4203:zeta.tex:506-508` — `where $\gamma $'s  are periodic orbits,  $ \mathcal P_\gamma:=d\varphi_{-T_\gamma}|_{E_s\oplus E_u} $ is the` / `linearized  Poincar\'e map, $ T_\gamma $ is the period of $ \gamma $, and $` / `T_\gamma^\# $ is the primitive period. See~\S\ref{tft} for definition and properties`

- `1306.4203:zeta.tex:496-498` — `We recall the trace formula of Guillemin \cite[Theorem 8,` / `(II.22)]{Gu} which is valid for any flow with nondegenerate periodic trajectories~-- see Appendix~\ref{s:guillemin}` / `for a self-contained proof in the Anosov case. In our notation it says that `

**Conventions fixed by the source.**
- Propagator is `e^{-itP}` with `P = -iV` (`V` the generator of the flow), i.e. `e^{-itP} = \varphi_{-t}^*`; the vector-bundle version uses `\mathbf P = (1/i)\mathcal L_V` (`1306.4203:zeta.tex:490-491`). So this is Tr♭ of the *pull-back by the backward flow*, the analytic continuation being to `\Im\lambda \gg 1`; to get the task's `Tr♭ e^{-tX}` set `t \mapsto` real time and `X = V`.
- The sum `\sum_\gamma` runs over **all** periodic orbits (repetitions included), not primitive ones: `T_\gamma` is the period of `\gamma`, `T_\gamma^\#` the primitive period. So the task's `\sum_\gamma\sum_k \ell_\gamma^\# \delta(t-k\ell_\gamma)` is the same sum written with the repetition index made explicit.
- `\mathcal P_\gamma := d\varphi_{-T_\gamma}|_{E_s\oplus E_u}` — **negative** time in the linearised Poincaré map; consequently `|\mu|<1` on `E_u` (`1306.4203:zeta.tex:510-511`).
- The flat trace `\tr^\flat B := \int_X (\iota^* K_B)(x)\,dx` is defined at `1306.4203:zeta.tex:811-816`; its existence rests on the wave-front condition `1306.4203:zeta.tex:270-274`.
- Ruelle zeta, for comparison: `1306.4203:zeta.tex:140-141` — `\[  \zeta_{\rm{R}} ( \lambda ) = \prod_{\gamma^\sharp } ( 1 - e^{ i \lambda T_\gamma^\sharp` / `} ) , \]` — product over **primitive** orbits, variable `e^{i\lambda T}` (not `e^{-sT}`).

---

## F2. Ruelle resonances of the geodesic flow from the Laplace spectrum; Ruelle zeta = Z(s)/Z(s+1)

### F2a. Band structure (Dyatlov–Faure–Guillarmou)

**arXiv:1403.0256** — `1403.0256:RuelleResonForHn.tex:118-119`
`\title[Power spectrum of hyperbolic manifolds]` / `{Power spectrum of the geodesic flow\\ on hyperbolic manifolds}`;
authors `1403.0256:RuelleResonForHn.tex:120` `\author{Semyon Dyatlov}`,
`:124` `\author{Fr\'ed\'eric Faure}`, `:128` `\author{Colin Guillarmou}`.

- `1403.0256:RuelleResonForHn.tex:181-191` (Theorem 1, the surface case)
```
Assume that $M$ is a compact hyperbolic surface ($n=1$) and the spectrum of the positive Laplacian on $M$ is
(see Figure~\ref{f:dim2})
$$
\Spec(\Delta)=\{s_j(1-s_j)\},\quad
s_j\in [0,1]\cup \Big({1\over 2}+i\mathbb R\Big).
$$
Then Pollicott--Ruelle resonances for the geodesic
flow on $SM$ in $\mathbb C\setminus (-1-{1\over 2}\mathbb N_0)$ are
\begin{equation}
  \label{e:dim2}
\lambda_{j,m}=-m-1+s_j,\quad m\in\mathbb N_0.
```

**Conventions fixed by the source.**
- `\Delta` is the **positive** Laplacian, spectrum written as `s_j(1-s_j)` — note this is the *opposite* sign convention to FGKP's `\Delta f_s = s(s-1) f_s` in F4.
- Resonances are poles of the **Laplace** transform of the correlation `\rho_{f,g}(t)=\int_{SM}(f\circ\varphi_{-t})\bar g\,d\mu` (`1403.0256:RuelleResonForHn.tex:157-160`), not the Fourier transform; the paper says explicitly (`:209-211`) `We use the Laplace transform (which has poles in the left half-plane) rather than the Fourier transform` / `as in~\cite{ruelle,FaSj}` / `to simplify the relation to the parameter $s$ used for Laplacians on hyperbolic manifolds.` So `\lambda` here is `-` (the DZ `-i\lambda`): the first band is `\lambda_{j,0}=s_j-1`, the shifted bands are `\lambda_{j,m}=s_j-1-m`.
- The theorem excludes the exceptional set `\mathbb C\setminus(-1-\tfrac12\mathbb N_0)`.
- The paper contains **no** occurrence of "Selberg" or "Ruelle zeta" — use 1606.04560 for the zeta relation.

### F2b. Ruelle zeta = Selberg zeta ratio, and the Selberg zeta product

**arXiv:1606.04560** — `1606.04560:zazi.tex:14-15` `\title[Ruelle zeta function]%` / `{Ruelle zeta function at zero for surfaces}`;
authors `1606.04560:zazi.tex:16` `\author{Semyon Dyatlov}` and `:20` `\author{Maciej Zworski}`.

- `1606.04560:zazi.tex:117-119`
```
\zeta_S ( s ) := \prod_{ \gamma \in \mathcal G } \prod_{ m=0}^\infty
( 1 - e^{- ( m + s ) \ell_\gamma } ) , \quad
\zeta_R ( s ) = \frac{ \zeta_S ( s  ) }{ \zeta_S ( s + 1  ) } ,
```

- `1606.04560:zazi.tex:54` — `\zeta_R ( s ) := \prod_{ \gamma \in \mathcal G } ( 1 - e^{ -s  \ell_\gamma } ) .`

**Conventions fixed by the source.** `\mathcal G` is "the set of **primitive** closed geodesics on `\Sigma` (counted with multiplicity)" and `\ell_\gamma` its length (`1606.04560:zazi.tex:45-47`); so both products are over primitive lengths, `m` is the band index. Here the Ruelle zeta is in the `e^{-s\ell}` normalisation (contrast `e^{i\lambda T}` in 1306.4203). Line `:121` attributes the ratio identity to `\cite[Theorem~5]{Mark}` = Marklof, math/0407288 (our F3 source).

---

## F3. Selberg trace formula (hyperbolic term) and the wave-trace/Poisson relation

### F3a. Selberg trace formula, compact hyperbolic surface (Marklof)

**arXiv:math/0407288** — `math/0407288:selberg07.tex:120` `\title*{Selberg's trace formula: an introduction}`;
author `math/0407288:selberg07.tex:122` `\author{Jens Marklof}`.

- `math/0407288:selberg07.tex:1766-1770` (Theorem, eq. `traceEQ`)
```
\sum_{j=0}^\infty  h(\rho_j)
= \frac{\Area(\scrM)}{4\pi} 
\int_{-\infty}^\infty h(\rho) \tanh(\pi\rho)\,\rho\, d\rho
+ \sum_{\gamma\in H_*}  \sum_{n=1}^\infty
\frac{\ell_{\gamma}\,g(n\ell_{\gamma})}{2\sinh(n\ell_{\gamma}/2)} ,
```

- Selberg zeta product, `math/0407288:selberg07.tex:2245-2246`
```
Z(s) = \prod_{\gamma\in H_*} \prod_{m=0}^\infty 
\left( 1-\e^{-\ell_\gamma(s+m)} \right),
```

**Conventions fixed by the source.**
- `H_*` is the set of **primitive** hyperbolic conjugacy classes: `math/0407288:selberg07.tex:1626-1627` — `If we denote by $H_*\subset H$ the subset of primitive elements, \eqref{kk}` / `equals`. So `\ell_\gamma` in the numerator is the **primitive** length and `n\ell_\gamma` the repeated one — exactly the task's `\ell_\gamma \hat g(k\ell_\gamma)/(2\sinh(k\ell_\gamma/2))`.
- `g` is the Fourier transform of `h`, `math/0407288:selberg07.tex:896` — `g(t)=\frac{1}{2\pi} \int_\RR h(\rho)\, \e^{-\i\rho t} d\rho .`
- Spectral parameter: `math/0407288:selberg07.tex:1674` — `\rho_j=\sqrt{\lambda_j-\tfrac14}, \qquad -\pi/2 \leq \arg\rho_j < \pi/2.` with `(\Delta+\lambda_j)\varphi_j=0` (`:1667`), i.e. `\Delta` is the **negative** (geometer's) Laplacian and `\lambda_j \ge 0` are the eigenvalues of `-\Delta`. In the `s(1-s)` parametrisation `s=\tfrac12+i\rho_j`.
- `\Area(\scrM)=4\pi(g-1)` (`:2277`).
- Marklof's notes contain **no** mention of the wave trace, `\cos(t\sqrt{\Delta-1/4})`, Duistermaat–Guillemin, or the Casimir operator — those are covered by math/0402356 and 1511.04265 below.

### F3b. Wave trace / Duistermaat–Guillemin (Poisson relation)

**arXiv:math/0402356** — `math/0402356:main.tex:77` `\title{The inverse spectral problem  }`;
author `math/0402356:main.tex:65` `\author{Steve Zelditch}`. (The arXiv listing title is
"Survey of the inverse spectral problem"; the TeX `\title` reads as quoted. The gzip member is
named `SurveyJDGAMSFV.tex` and is stored here as `main.tex` by `fetch_sources.sh`'s gunzip branch.)

- `math/0402356:main.tex:1459-1465`
```
The first result on the wave trace is the Poisson relation on a
manifold without boundary,
\begin{equation}\label{SS} \mbox{Sing Supp} Tr U(t) \subset \;\;
Lsp(M,g),
\end{equation}
proved by Y. Colin de Verdi\`ere \cite{CdV2, CdV3}, Chazarain
\cite{Ch2}, and Duistermaat-Guillemin \cite{DG} (following
```

- The even part, `math/0402356:main.tex:1471-1472` — `there are at least two closed geodesics of that length, namely` / `$\gamma$ and $\gamma^{-1}$ (its time reversal). The singularities` ; and `:1473-1475` — `due to these lengths are identical so one often considers the even` / `part of $Tr U(t)$ i.e. $Tr E(t)$ where $E(t)= \cos (t` / `\sqrt{\Delta}).$`

**Conventions fixed by the source.**
- The wave group is `U(t)=e^{it\sqrt{\Delta}}` and the trace `Tr U(t)=\sum_{\lambda_j\in Sp(\sqrt\Delta)} e^{it\lambda_j}` (`math/0402356:main.tex:1451-1454`), so `\Delta` is the **positive** Laplacian here.
- The statement is an **inclusion** `\subset`, not an equality: `math/0402356:main.tex:1480-1482` — `We emphasize that  (\ref{SS}) is only known to be a containment` / `relation. As will be seen below, cancellations could take place if` / `a length $L \in Lsp(M, g)$ is multiple, so that $Tr U(t)$ might be`. For a compact **hyperbolic** surface the Selberg trace formula (F3a) upgrades this to an equality, with `\sqrt{\Delta}` replaced by `\sqrt{\Delta-1/4}` (the `\rho_j` of Marklof); the `-1/4` shift is **not** present in this general-manifold source.

---

## F4. Casimir of sl(2,R) = hyperbolic Laplacian on right-K-invariant functions

**arXiv:1511.04265** — title `1511.04265:AutomorphicBook.tex:5`
`\newcommand{\titleString}{Eisenstein series and automorphic representations}` (the document has no
`\title` macro; the string is set here and used by `\fancyhead`/`pdftitle`);
authors `1511.04265:AutomorphicBook.tex:266`
`Philipp Fleig${}^{1}$, Henrik P. A. Gustafsson${}^2$, Axel Kleinschmidt${}^{3,4}$, Daniel Persson${}^{2}$`
(also `:77` `pdfauthor={ Philipp Fleig, Henrik P. A. Gustafsson, Axel Kleinschmidt, Daniel Persson },`).

Chevalley basis:

- `1511.04265:AutomorphicBook.tex:2835-2837`
```
e = \begin{pmatrix}0&1\\0&0\end{pmatrix}\,,\quad
h = \begin{pmatrix}1&0\\0&-1\end{pmatrix}\,,\quad
f = \begin{pmatrix}0&0\\1&0\end{pmatrix}
```
- commutators `1511.04265:AutomorphicBook.tex:2842-2844` — `\lb h,e\rb =2e\,,\quad` / `\lb h,f\rb = -2f\,,\quad` / `\lb e,f\rb =h\,.`

Casimir:

- `1511.04265:AutomorphicBook.tex:2851` — `\Omega = \frac14 h^2 + \frac12 ef + \frac12 fe = \frac14 h^2-\frac12 h +ef.`
- normalisation caveat, `:2853` — `This definition is unique up to normalisation. The Casimir operator commutes with all Lie algebra elements.`

As a differential operator on `SL(2,R)` in Iwasawa coordinates `(x,y,\theta)`:

- `1511.04265:AutomorphicBook.tex:3107-3110`
```
The Casimir operator~\eqref{eq:SL2cas} then becomes a second order differential operator, namely the Laplacian
\begin{align}
\label{eq:SL2Lapapp}
\Delta_{SL(2,\mathbb{R})} = y^2 \left( \partial_x^2 + \partial_y^2 \right) - y \partial_x \partial_\theta.
```

And on the upper half plane (weight zero / right-`SO(2)`-invariant):

- `1511.04265:AutomorphicBook.tex:409-411`
```
\Delta = y^2 \left( \partial_x^2 + \partial_y^2\right)
\end{align}
and corresponds to the Laplace--Beltrami operator on the upper half plane $\UHP$. In group theoretical terms it is the quadratic Casimir operator. Acting with it on the function (\ref{Eisenintro}) one finds 
```

Compact basis, for the `(H, E, F)` presentation the task asks about:

- `1511.04265:AutomorphicBook.tex:3115-3117`
```
H=-i(e-f),\quad
E= \frac12\left( h +i (e+f) \right),\quad
F= \frac12\left( h -i (e+f) \right),
```
- `1511.04265:AutomorphicBook.tex:3146` — `H &= -i\partial_\theta,\\`
- `1511.04265:AutomorphicBook.tex:3156` — `Because the compact basis is unitarily equivalent, the Casimir operator does not change.`

**Conventions fixed by the source.**
- Basis is the **Chevalley** `(e,h,f)` with `[h,e]=2e`, `[h,f]=-2f`, `[e,f]=h`; the compact subgroup is generated by `e-f` (`:2846`), and the compact basis is `H=-i(e-f)`, `E=\tfrac12(h+i(e+f))`, `F=\tfrac12(h-i(e+f))`.
- Casimir normalisation `\Omega = \tfrac14 h^2 + \tfrac12(ef+fe)` — i.e. `\tfrac12` the Killing-form-normalised `h^2/2+ef+fe`; the source flags this as a choice.
- Iwasawa gauge `g = \exp(xe)\exp(\tfrac12\log y\,h)\exp(\theta(e-f))` (`:2859`), `\partial_\theta = e-f` (`:3103`). Hence on right-`K`-invariant (`\partial_\theta = 0`, weight `w=0`) functions `\Delta_{SL(2,\reals)}` of `:3110` reduces to `y^2(\partial_x^2+\partial_y^2)` of `:409`. The book does **not** write that one-line reduction out explicitly; it states both operators and identifies the second as "the quadratic Casimir operator" on `\UHP` (`:411`), and defines `K`-finiteness / the weight-`w` phase `\varphi_f(gk)=e^{iw\vartheta}\varphi_f(g)` at `:3064` with `H` eigenvalue `w` at `:3167`.
- **Sign convention is the analyst-unfriendly one**: `\Delta f_s(z)=s(s-1) f_s(z)` (`1511.04265:AutomorphicBook.tex:414`), i.e. `\Delta` is the *negative* Laplacian and the eigenvalue is `s(s-1) = -s(1-s)`. Opposite in sign to DFG's `\Spec(\Delta)=\{s_j(1-s_j)\}` (F2a) and to Marklof's `\lambda_j = \rho_j^2+\tfrac14 \ge 0` (F3a).

---

## F5. Scattering determinant of PSL(2,Z) and the continuous-spectrum term

### F5a. `\phi(s)` for the modular group

**arXiv:1607.08053** — `1607.08053:main.tex:158`
`\title{An evaluation of the central value of the automorphic scattering determinant}`;
authors `1607.08053:main.tex:159-161` `\author{Joshua S. Friedman\footnote{...}}, Jay Jorgenson\footnote{...} and Lejla Smajlovi\'{c}}`
(the `\author` argument is split over lines 159–161 by two footnotes; the names are
`Joshua S. Friedman` at `:159`, `Jay Jorgenson` at `:160`, `Lejla Smajlovi\'{c}` at `:161`).

- `1607.08053:main.tex:592-594`
```
In the case when $\Gamma$ is the modular group $\mathrm{PSL}(2,\mathbb{Z})$, the scattering determinant is given by
$$
\phi(s)=\sqrt{\pi}\frac{\Gamma(s-1/2)}{\Gamma(s)} \frac{\zeta(2s-1)}{\zeta(2s)},
```

**Conventions fixed by the source.** `\phi(s)` is the determinant of the scattering matrix for a
finite-volume non-compact hyperbolic Riemann surface, normalised by the functional equation
`\phi(s)\phi(1-s)=1` (`1607.08053:main.tex:167-168`). At the central point the example continues
`\phi(1/2)=\dots=-1` (`:598`).

The same constant appears as the Eisenstein constant term:

- `1511.04265:AutomorphicBook.tex:6196` — `W_1^\circ(s,g)= |v|^{2s}+\sqrt{\pi}\frac{\Gamma(s-1/2)}{\Gamma(s)}\frac{\zeta(2s-1)}{\zeta(2s)}|v|^{-2s+2}.`
- completed form, `1511.04265:AutomorphicBook.tex:554` — `\frac{\xi(2s-1)}{\xi(2s)} = \pi^{1/2}\frac{\Gamma(s-1/2)}{\Gamma(s)} \prod_{p<\infty} \frac{1-p^{-2s}}{1-p^{1-2s}}`
- and in the Fourier expansion, `1511.04265:AutomorphicBook.tex:584` — `E(\chi_s,g)= y^{s}+\frac{\xi(2s-1)}{\xi(2s)}y^{1-s}`

so that `\phi(s)` **is** the `y^{1-s}` coefficient of the constant term, with `\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)` (`:6206`). For `g\in SL(2,\reals)` one sets `v=y^{1/2}` (`:6198`).

### F5b. Selberg trace formula for a finite-area surface, continuous term

**arXiv:1108.5659** — `1108.5659:main.tex:21`
`\title{\textbf{Zeta functions and regularized determinants related to the Selberg trace formula}}`;
authors `1108.5659:main.tex:22` `\author{\begin{Large}Arash Momeni$^1$ and Alexei Venkov$^2$\end{Large}\\ \begin{small}`.

- `1108.5659:main.tex:2125-2129`
```
\sum_{k=0}^{\infty}h(\lambda_k)+C=I+H+E+P
\end{equation}
where $\left\lbrace \lambda_n \ \vert\ 0=\lambda_0<\lambda_1\leq \lambda_2\leq \ldots\right\rbrace$ are the discrete eigenvalues of $A(\Gamma;\chi)$. Here $C$ corresponds to the continuous part of the spectrum given by
\begin{equation}
C=C(\overset{\sim}{h}(r);\Gamma;\chi)=-\frac{1}{4\pi}\int_{-\infty}^{\infty}\dfrac{\varphi'}{\varphi}(\frac{1}{2}+ir;\Gamma;\chi)h(r^2+\frac{1}{4})dr+\dfrac{K_0}{4} h(\dfrac{1}{4})
```

- hyperbolic term for comparison, `1108.5659:main.tex:2137`
```
H=H(\overset{\sim}{h}(r);\Gamma;\chi)=\sum_{\left\lbrace P\right\rbrace _\Gamma}\sum_{m=1}^\infty \dfrac{\text{tr}_V\chi^m(P)logN(P)}{N(P)^{\frac{m}{2}}-N(P)^{-\frac{m}{2}}}g(m \ logN(P))
```

**Conventions fixed by the source.**
- `C` sits on the **spectral** side (`\sum_k h(\lambda_k) + C = I+H+E+P`), with the sign `-\tfrac1{4\pi}\int_{\mathbb R}` — exactly the task's `-(1/4\pi)\int h(r)(\varphi'/\varphi)(\tfrac12+ir)\,dr`, plus the central correction `\tfrac{K_0}{4}h(\tfrac14)` with `K_0=\mathrm{tr}\,\Phi(\tfrac12)` (`:2131`).
- Test function: `\overset{\sim}{h}(r) := h(r^2+\tfrac14)`, holomorphic in `|\Im r|<\tfrac12+\varepsilon` (`:2116-2119`); `g(u)=\tfrac1{2\pi}\int_{\mathbb R} e^{-iru} h(r^2+\tfrac14)\,dr` (`:2141`).
- `\{P\}_\Gamma` are the **primitive** hyperbolic conjugacy classes and `N(P)>1` the norm, so `\log N(P) = \ell_P` is the primitive length and `N(P)^{m/2}-N(P)^{-m/2} = 2\sinh(m\ell_P/2)`; with `\chi` trivial and `\ell_\gamma=\log N(P)` this is literally Marklof's `\ell_\gamma g(n\ell_\gamma)/(2\sinh(n\ell_\gamma/2))` of F3a.
- Cocompact case: `\varphi(s;\Gamma;\chi)\equiv 1` (`1108.5659:main.tex:208`), i.e. `C` disappears (`:2156-2158`).
- This theorem is stated for a general Fuchsian group of the first kind with a unitary representation `\chi`, **not** specialised to `PSL(2,\Z)`; combine with F5a for the modular case.

### F5c. Trace formula written out for PSL(2,Z) (secondary)

**arXiv:1710.00603** — `1710.00603:turing6.tex:41` `\title{Turing's method for the Selberg zeta-function}`;
authors `:42` `\author{Andrew R. Booker}`, `:45` `\author{David J. Platt}`.

- `1710.00603:turing6.tex:350-351` — `\begin{proposition}[The Selberg trace formula for Maass forms on` / `$\PSL(2,\Z)\backslash\H$]\label{prop:trace}`

This gives every term (identity `I`, elliptic `E`, parabolic `P`, discrete `D`, continuous `C`) explicitly
for `\Gamma=\PSL(2,\Z)`, but in the Booker–Strömbergsson arithmetic normalisation: the continuous
contribution appears as `C(\hat h)=\int_\R\hat{h}(t)(\cosh \pi t-1)\dif t` (`:388`) — the
`\varphi'/\varphi` integral has already been evaluated using `\phi(s)` of F5a and folded into the
`\Lambda(n)/n` sum in `D` (`:384`). Use this only if a fully explicit modular-group formula is wanted;
for the `\varphi'/\varphi` shape quote F5b.

---

## Nothing marked [NOT FOUND]

All five facts are available in local TeX. Two caveats worth recording:

1. F2's "band structure" and F2's "Ruelle zeta = `Z(s)/Z(s+1)`" come from **different** papers
   (1403.0256 and 1606.04560); 1403.0256 never mentions Selberg or Ruelle zeta.
2. F4's "on right-`K`-invariant functions the Casimir equals `y^2(\partial_x^2+\partial_y^2)`" is
   assembled from two equations in 1511.04265 (`:3110` and `:409`) plus its `\partial_\theta=e-f`
   (`:3103`); the book does not state the one-line reduction as a displayed sentence. If a single
   displayed statement is needed, the standard book reference is D. Bump, *Automorphic Forms and
   Representations*, CUP 1997, §2.2 (not on arXiv, not quoted here).

Also not on arXiv and therefore only named, not quoted: D. A. Hejhal, *The Selberg Trace Formula for
PSL(2,R)*, Vols. I–II, Springer LNM 548 (1976) / 1001 (1983); H. Iwaniec, *Spectral Methods of
Automorphic Forms*, AMS GSM 53, 2nd ed. 2002 (Ch. 10 for the trace formula with the `\varphi'/\varphi`
term, Ch. 3 for `\phi(s)` of the modular group); V. Guillemin, *Lectures on spectral theory of
elliptic operators*, Duke Math. J. 44 (1977) 485–517 (the original of F1, cited by 1306.4203 as `\cite{Gu}`).

---

## Proposed rows for `db/provenance.tsv`

(Not written to `db/`; paste as-is. Columns: `id | key | file | lines | quote | used_by`.)

```tsv
prov:dz13-guillemin	1306.4203	zeta.tex	260-264	\label{eq:ABG}  \tr^\flat e^{-it P }  = \sum_{ \gamma} \frac{ T_\gamma^\#     \delta ( t - T_\gamma ) } { | \det ( I - \mathcal P_\gamma ) |} , \ \ t > 0	F1
prov:dz13-guillemin-forms	1306.4203	zeta.tex	500-505	\label{eq:guill}   \tr^\flat e^{-i t\mathbf P } |_{ C^\infty ( X ; \mathcal E^k_0 )} =   \sum_{ \gamma } \frac{ T_\gamma^\#   \tr ( \wedge^k \mathcal P_\gamma ) \,  \delta ( t - T_\gamma ) } { | \det ( I - \mathcal P_\gamma ) |} , \ \  t > 0 , \end{equation}	F1
prov:dz13-conventions	1306.4203	zeta.tex	506-508	where $\gamma $'s  are periodic orbits,  $ \mathcal P_\gamma:=d\varphi_{-T_\gamma}|_{E_s\oplus E_u} $ is the linearized  Poincar\'e map, $ T_\gamma $ is the period of $ \gamma $, and $ T_\gamma^\# $ is the primitive period. See~\S\ref{tft} for definition and properties	F1
prov:dz13-ruelle-def	1306.4203	zeta.tex	140-141	\[  \zeta_{\rm{R}} ( \lambda ) = \prod_{\gamma^\sharp } ( 1 - e^{ i \lambda T_\gamma^\sharp } ) , \]	F1,F2
prov:dfg14-band	1403.0256	RuelleResonForHn.tex	181-191	Assume that $M$ is a compact hyperbolic surface ($n=1$) and the spectrum of the positive Laplacian on $M$ is (see Figure~\ref{f:dim2}) $$ \Spec(\Delta)=\{s_j(1-s_j)\},\quad s_j\in [0,1]\cup \Big({1\over 2}+i\mathbb R\Big). $$ Then Pollicott--Ruelle resonances for the geodesic flow on $SM$ in $\mathbb C\setminus (-1-{1\over 2}\mathbb N_0)$ are \begin{equation}   \label{e:dim2} \lambda_{j,m}=-m-1+s_j,\quad m\in\mathbb N_0.	F2
prov:dfg14-laplace-transform	1403.0256	RuelleResonForHn.tex	209-211	We use the Laplace transform (which has poles in the left half-plane) rather than the Fourier transform as in~\cite{ruelle,FaSj} to simplify the relation to the parameter $s$ used for Laplacians on hyperbolic manifolds.	F2
prov:dz16-ruelle-selberg	1606.04560	zazi.tex	117-119	\zeta_S ( s ) := \prod_{ \gamma \in \mathcal G } \prod_{ m=0}^\infty ( 1 - e^{- ( m + s ) \ell_\gamma } ) , \quad \zeta_R ( s ) = \frac{ \zeta_S ( s  ) }{ \zeta_S ( s + 1  ) } ,	F2
prov:dz16-ruelle-def	1606.04560	zazi.tex	54	\zeta_R ( s ) := \prod_{ \gamma \in \mathcal G } ( 1 - e^{ -s  \ell_\gamma } ) .	F2
prov:marklof04-hyperbolic	math/0407288	selberg07.tex	1766-1770	\sum_{j=0}^\infty  h(\rho_j) = \frac{\Area(\scrM)}{4\pi}  \int_{-\infty}^\infty h(\rho) \tanh(\pi\rho)\,\rho\, d\rho + \sum_{\gamma\in H_*}  \sum_{n=1}^\infty \frac{\ell_{\gamma}\,g(n\ell_{\gamma})}{2\sinh(n\ell_{\gamma}/2)} ,	F3
prov:marklof04-selbergzeta	math/0407288	selberg07.tex	2245-2246	Z(s) = \prod_{\gamma\in H_*} \prod_{m=0}^\infty \left( 1-\e^{-\ell_\gamma(s+m)} \right),	F2,F3
prov:marklof04-primitive	math/0407288	selberg07.tex	1626-1627	If we denote by $H_*\subset H$ the subset of primitive elements, \eqref{kk} equals	F3
prov:marklof04-gtransform	math/0407288	selberg07.tex	896	g(t)=\frac{1}{2\pi} \int_\RR h(\rho)\, \e^{-\i\rho t} d\rho .	F3
prov:marklof04-rho	math/0407288	selberg07.tex	1674	\rho_j=\sqrt{\lambda_j-\tfrac14}, \qquad -\pi/2 \leq \arg\rho_j < \pi/2.	F3
prov:zelditch04-poisson	math/0402356	main.tex	1459-1465	The first result on the wave trace is the Poisson relation on a manifold without boundary, \begin{equation}\label{SS} \mbox{Sing Supp} Tr U(t) \subset \;\; Lsp(M,g), \end{equation} proved by Y. Colin de Verdi\`ere \cite{CdV2, CdV3}, Chazarain \cite{Ch2}, and Duistermaat-Guillemin \cite{DG} (following	F3
prov:zelditch04-wavegroup	math/0402356	main.tex	1451-1454	wave group $U(t) = e^{i t \sqrt{\Delta}}$ of $(M, g)$. One forms the (distribution) trace \begin{equation} Tr U(t) = \sum_{ \lambda_j \in Sp(\sqrt{\Delta})} e^{i t \lambda_j}. \end{equation} It is a tempered distribution on	F3
prov:zelditch04-costerm	math/0402356	main.tex	1473-1475	due to these lengths are identical so one often considers the even part of $Tr U(t)$ i.e. $Tr E(t)$ where $E(t)= \cos (t \sqrt{\Delta}).$	F3
prov:fgkp16-chevalley	1511.04265	AutomorphicBook.tex	2835-2837	e = \begin{pmatrix}0&1\\0&0\end{pmatrix}\,,\quad h = \begin{pmatrix}1&0\\0&-1\end{pmatrix}\,,\quad f = \begin{pmatrix}0&0\\1&0\end{pmatrix}	F4
prov:fgkp16-casimir	1511.04265	AutomorphicBook.tex	2851	\Omega = \frac14 h^2 + \frac12 ef + \frac12 fe = \frac14 h^2-\frac12 h +ef.	F4
prov:fgkp16-casimir-laplacian	1511.04265	AutomorphicBook.tex	3107-3110	The Casimir operator~\eqref{eq:SL2cas} then becomes a second order differential operator, namely the Laplacian \begin{align} \label{eq:SL2Lapapp} \Delta_{SL(2,\mathbb{R})} = y^2 \left( \partial_x^2 + \partial_y^2 \right) - y \partial_x \partial_\theta.	F4
prov:fgkp16-uhp-laplacian	1511.04265	AutomorphicBook.tex	409-411	\Delta = y^2 \left( \partial_x^2 + \partial_y^2\right) \end{align} and corresponds to the Laplace--Beltrami operator on the upper half plane $\UHP$. In group theoretical terms it is the quadratic Casimir operator. Acting with it on the function (\ref{Eisenintro}) one finds	F4
prov:fgkp16-compact-basis	1511.04265	AutomorphicBook.tex	3115-3117	H=-i(e-f),\quad E= \frac12\left( h +i (e+f) \right),\quad F= \frac12\left( h -i (e+f) \right),	F4
prov:fgkp16-eigenvalue-sign	1511.04265	AutomorphicBook.tex	414	\Delta f_s(z) = s(s-1) f_s(z)	F4
prov:fgkp16-constant-term	1511.04265	AutomorphicBook.tex	6196	W_1^\circ(s,g)= |v|^{2s}+\sqrt{\pi}\frac{\Gamma(s-1/2)}{\Gamma(s)}\frac{\zeta(2s-1)}{\zeta(2s)}|v|^{-2s+2}.	F5
prov:fgkp16-xi-ratio	1511.04265	AutomorphicBook.tex	554	\frac{\xi(2s-1)}{\xi(2s)} = \pi^{1/2}\frac{\Gamma(s-1/2)}{\Gamma(s)} \prod_{p<\infty} \frac{1-p^{-2s}}{1-p^{1-2s}}	F5
prov:fjs16-scattering-det	1607.08053	main.tex	592-594	In the case when $\Gamma$ is the modular group $\mathrm{PSL}(2,\mathbb{Z})$, the scattering determinant is given by $$ \phi(s)=\sqrt{\pi}\frac{\Gamma(s-1/2)}{\Gamma(s)} \frac{\zeta(2s-1)}{\zeta(2s)},	F5
prov:mv11-continuous-term	1108.5659	main.tex	2128-2129	\begin{equation} C=C(\overset{\sim}{h}(r);\Gamma;\chi)=-\frac{1}{4\pi}\int_{-\infty}^{\infty}\dfrac{\varphi'}{\varphi}(\frac{1}{2}+ir;\Gamma;\chi)h(r^2+\frac{1}{4})dr+\dfrac{K_0}{4} h(\dfrac{1}{4})	F5
prov:mv11-traceformula	1108.5659	main.tex	2125	\sum_{k=0}^{\infty}h(\lambda_k)+C=I+H+E+P	F5
prov:mv11-hyperbolic-term	1108.5659	main.tex	2137	H=H(\overset{\sim}{h}(r);\Gamma;\chi)=\sum_{\left\lbrace P\right\rbrace _\Gamma}\sum_{m=1}^\infty \dfrac{\text{tr}_V\chi^m(P)logN(P)}{N(P)^{\frac{m}{2}}-N(P)^{-\frac{m}{2}}}g(m \ logN(P))	F3,F5
prov:bp17-psl2z-trace	1710.00603	turing6.tex	350-351	\begin{proposition}[The Selberg trace formula for Maass forms on $\PSL(2,\Z)\backslash\H$]\label{prop:trace}	F5
```
