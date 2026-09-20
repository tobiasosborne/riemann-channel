# The Childs lead: scattering theory of quantum walks on graphs with tails

Author: `claude:opus`. Date: 2026-09-20. Lane: LITERATURE.
Target: `notes/cusp-graph/astra-brief.md` (finite core + one infinite ray, reflection coefficient
`R(z)`, resonances = zeros of `R` in `|z| < 1`, bound states = poles, discrete Lax–Phillips
contraction `Z`). TJO's recollection that Andrew Childs did something extremely similar is
**correct and stronger than expected**: Childs–Strouse `1103.5077` contains the brief's `R(z)`
*verbatim, sign and all*, together with C2(i), C2(ii), C2(iii) and a count that subsumes C2(iv).

Quotes below are byte-verified: each is preceded by the `grep -n -F` command and its output.
All line numbers are against the arXiv TeX sources fetched into `refs/src/` (see §1).

---

## 1. Papers found and fetched

All fetched with `curl -sSL -o refs/src/<id>/src.tar https://arxiv.org/e-print/<id>` and extracted
as `refs/fetch_sources.sh` does. Ids appended to the `IDS` list in `refs/fetch_sources.sh`;
sha256 lines appended to `refs/manifest.sha256`.

| id | paper | file | sha256 |
|---|---|---|---|
| `1103.5077` | Childs, Strouse, *Levinson's theorem for graphs*, JMP 52, 082102 (2011) | `src/1103.5077/main.tex` | `24caf434f70bc56e2b7f5c6cb68d6261b1504cf5c08f4036007375a56b82c768` |
| `1203.6557` | Childs, Gosset, *Levinson's theorem for graphs II*, JMP 53, 102207 (2012) | `src/1203.6557/levinson2.tex` | `3238842df5a11c7c71043da5b613b9c2fd76f2bd3f6f558a400504d48ef60514` |
| | | `src/1203.6557/levinson2.bbl` | `56c15cfa75d3a81506ab85df079f3d09d2f73f18d048e7f10eb4707cde797735` |
| `0806.1972` | Childs, *Universal computation by quantum walk*, PRL 102, 180501 (2009) | `src/0806.1972/uwalk.tex` | `bf95591472af4db3a293d212db8ef1e330a86c9a0a0969afe30a0793905a2fdf` |
| `1205.3782` | Childs, Gosset, Webb, *Universal computation by multi-particle quantum walk*, Science 339, 791 (2013) | `src/1205.3782/MPQW.tex` | `99e1d0c4562b10522189fd7a003ffbda11e3dd814e08c19badeb897c1c569ab3` |
| | | `src/1205.3782/MPQW.bbl` | `8b7122761bf5766ce52f7fe318b24257536c72f1fe8dd3a18aebdf271f10f663` |
| `1406.4510` | Childs, Gosset, Nagaj, Raha, Webb, *Momentum switches* (QIC 15, 601 (2015)) | `src/1406.4510/momentumswitch.tex` | `8fad232f6dceb3898a0dcc5ecaaf28d811a35968e2cd2f22025422c7215639bf` |
| | | `src/1406.4510/momentumswitch.bbl` | `58670b81f6089dbdecc35e82b07547bb4f2b3f98fdf626a32c2c891e037db782` |
| `quant-ph/9706062` | Farhi, Gutmann, *Quantum computation and decision trees* | `src/quant-ph/9706062/FarhiGutmann2651WEB.tex` | `679e9cf2bdd0b29da31565afddb9909b2d60aa7d7e21b55db4a41ff187796368` |
| `quant-ph/0209131` | Childs, Cleve, Deotto, Farhi, Gutmann, Spielman, *Exponential algorithmic speedup by quantum walk* (glued trees) | `src/quant-ph/0209131/walk.tex` | `a506cd07afec15d463a92c2e16d5eb75c6a6353c9bc6ce2a776ca3ae8f7f84c5` |
| `0810.0312` | Childs, *On the relationship between continuous- and discrete-time quantum walk* | `src/0810.0312/main.tex` | `59cab0a2ed8a49c900c42cc6964e6ef653583cdb8bc6ce2118da0788fb9b9e71` |

**Corrections to the brief's own bibliography guesses.** (b) is *not* Childs–Gosset: the `n = 1`
paper `1103.5077` is **Childs and Strouse** (2011); `1203.6557` is the **sequel, "II"**, by
Childs and Gosset, for `n` tails. Both exist and both matter. (d) `1406.4510` **exists** (five
authors as the brief guessed).

**Adjacent hits, not by Childs, fetched anyway** because they answer brief items (f) and (g)
that Childs's own corpus does not:

| id | paper | file | sha256 |
|---|---|---|---|
| `2602.03192` | Higuchi, Ishikawa, Morioka, Segawa, Yoshimura, *Resonant scattering for tunable quantum walks on graphs with tails* (2026) | `src/2602.03192/qw_resonance_ver2_arxiv.tex` | `bf7adca486a29a42d0990329365135114f0c2f4993163c5b6de12b3918ee16f6` |
| `2605.14640` | Gerrard, Asaka, Sakai, *Perfect transmission and parallel composition for quantum walks on graphs with two leads* (2026) | `src/2605.14640/charpoly_paper.tex` | `08892ded415be9a778ba7a465664d640410ba1b9f60dd0be4b89aa783d759b7e` |

`2602.03192` is the **discrete-time / coined** analogue with resonances defined properly (complex
translation / distortion); `2605.14640` gives the **two-terminal S-matrix as a ratio of
characteristic polynomials** of vertex-deleted subgraphs — the closest published thing to the
brief's determinant form for `R`.

**Not fetched / not found.**
- No Childs paper on *resonances*: `grep -c -i resonan` over all eight sources above returns `0`
  for every file (§2.6). There is no Childs paper on poles of the S-matrix off the real momentum
  axis, and none on a coined/discrete-time tail-scattering analogue.
- No Childs paper using Lax–Phillips: `grep -c -i -E "lax.phillips|ihara|zeta function"` returns
  `0` everywhere except one bibliography line in `0810.0312` (a citation to Kedlaya, *Quantum
  computation of zeta functions of curves*, `src/0810.0312/main.tex:904`) — unrelated to tails.
- `0810.0312` (CTQW vs DTQW) has **zero** occurrences of `semi-infinite|scattering|S-matrix`; it
  is not a tail-scattering paper and is recorded only to close the sweep of Childs's listing.
- Childs's arXiv author listing (`https://arxiv.org/a/childs_a_1`, fetched 2026-09-20) lists no
  further tail-scattering papers beyond those above.

---

## 2. Byte-verified quotes

### 2.1 How the tail is attached, and the scattering ansatz

    $ grep -n -F 'Now let $G$ be an $(m+1)$-vertex graph, and create an infinite graph by attaching a semi-infinite path' src/1103.5077/main.tex
    110:Now let $G$ be an $(m+1)$-vertex graph, and create an infinite graph by attaching a semi-infinite path to the first vertex of $G$.  We refer to the remaining $m$ vertices of $G$ as \emph{internal vertices}.  Label the basis states for vertices on the semi-infinite path as $|x\>$, where $x=1$ for the vertex in the original graph and $x=2,3,\ldots$ moving out along the path.

    $ grep -n -F '\<x \scattering{k} &= e^{-\ii k x} + R(e^{\ii k}) \, e^{\ii k x}' src/1103.5077/main.tex
    159:  \<x \scattering{k} &= e^{-\ii k x} + R(e^{\ii k}) \, e^{\ii k x}

`1203.6557`, `n` tails, energy written as `z + 1/z` exactly as the brief's `lambda`:

    $ grep -n -F 'on the semi-infinite lines, where $z=e^{ik}$. Such a state has energy' src/1203.6557/levinson2.tex
    331:on the semi-infinite lines, where $z=e^{ik}$. Such a state has energy $z+\frac{1}{z}=2\cos k.$ (Here $z$ is on the unit circle; later we discuss the analytic continuation of the S-matrix to other values of $z$.) The label $j$ indicates the semi-infinite line on which the state is incoming and $x=1,2,3,\ldots$ indexes the distance along this line (with $|1,j\rangle$ corresponding to the vertex where the $j$th line connects to the $(m+n)$-vertex graph).

Farhi–Gutmann's original ansatz (Laplacian convention, `E = 4 sin^2(theta/2)`, "runway" indexed by
`j = 0, -1, -2, ...`), i.e. the tail-scattering setup predates Childs:

    $ grep -n -F '\langle j|\theta\rangle=\frac{1}{(2\pi)^{1/2}}\left[e^{ij\theta}+R(\theta)' src/quant-ph/9706062/FarhiGutmann2651WEB.tex
    619:\langle j|\theta\rangle=\frac{1}{(2\pi)^{1/2}}\left[e^{ij\theta}+R(\theta)

### 2.2 Closed-form reflection coefficient (the brief's `R(z)`)

    $ grep -n -F 'R(e^{\ii k}) = -\frac{Q(e^{-\ii k})}{Q(e^{\ii k})}' src/1103.5077/main.tex
    181:  R(e^{\ii k}) = -\frac{Q(e^{-\ii k})}{Q(e^{\ii k})}

    $ grep -n -F 'Q(e^{\ii k}) &\defeq 1 - e^{\ii k}(a+C(e^{\ii k}))' src/1103.5077/main.tex
    185:  Q(e^{\ii k}) &\defeq 1 - e^{\ii k}(a+C(e^{\ii k})) \label{eq:qmatrix} \\

    $ grep -n -F 'C(e^{\ii k}) &\defeq b^\dag (2\cos k - D)^{-1} b.' src/1103.5077/main.tex
    186:  C(e^{\ii k}) &\defeq b^\dag (2\cos k - D)^{-1} b. \label{eq:c}

The `n`-tail matrix version (already stated as future work in `1103.5077`, then proved in II):

    $ grep -n -F 'One could also consider generalizing \thm{levinson} to the case where $n > 1$ semi-infinite paths are attached' src/1103.5077/main.tex
    454:One could also consider generalizing \thm{levinson} to the case where $n > 1$ semi-infinite paths are attached to $n$ vertices of an $(n+m)$-vertex graph.  In general, the scattering is described by an $n \times n$ matrix, the $S$-matrix, instead of a single reflection coefficient (see Ref.~\cite{Chi09} for details).  Similar calculations to those in \sec{scattering} can be used to determine the $S$-matrix in this more general case: for a weighted adjacency matrix of the form $\left(\begin{smallmatrix}A & B^\dag \\ B & D\end{smallmatrix}\right)$, where $A \in \C^{n \times n}$, $B \in \C^{m \times n}$, and $D \in \C^{m \times m}$, the $S$-matrix at momentum $k$ is $S(e^{\ii k})$, where $S(z) = -Q(z^{-1})/Q(z)$ with $Q(z) = I - z(A + B^\dag[(z + z^{-1}) I - D]^{-1}B)$.  Furthermore, similar conditions to those described in \sec{bound} can be used to characterize the bound states.  We expect the number of bound states in such a scattering problem to be related to the winding number of $\det S(z)$, but we leave the details as a topic for future work.

    $ grep -n -F 'S(z) & =-Q(z)^{-1}Q(z^{-1})\label{eq:S_matrix}' src/1203.6557/levinson2.tex
    365:S(z) & =-Q(z)^{-1}Q(z^{-1})\label{eq:S_matrix}

### 2.3 Levinson's theorem for graphs (both versions)

    $ grep -n -F '  w_\Gamma(R) = 2 (m - n_b - n_c - \smfrac{1}{2}n_h).' src/1103.5077/main.tex
    277:  w_\Gamma(R) = 2 (m - n_b - n_c - \smfrac{1}{2}n_h).

(`m` = number of internal vertices, `n_b` = evanescent bound states, `n_c` = confined bound
states, `n_h` = half-bound states; hypothesis `a != 0` or `||b|| != 1`.)

    $ grep -n -F 'w_{\Gamma}(\det(S))=2\left(m-n_{b}-n_{c}-\frac{1}{2}n_{h}\right).' src/1203.6557/levinson2.tex
    511:w_{\Gamma}(\det(S))=2\left(m-n_{b}-n_{c}-\frac{1}{2}n_{h}\right).

Degree of the numerator (the brief's C1 "state the degree of `R`"):

    $ grep -n -F 'If $a = 0$ and $\norm{b} \ne 1$, then $Q(z)$ is a rational function of $z$ whose numerator has degree $2m - 2n_c$.' src/1103.5077/main.tex
    365:If $a = 0$ and $\norm{b} \ne 1$, then $Q(z)$ is a rational function of $z$ whose numerator has degree $2m - 2n_c$.

### 2.4 Bound, half-bound, confined states; reality inside the disc

    $ grep -n -F '  Let $|z| \le 1$ and $Q(z)=0$.  Then $\Im(z)=0$.' src/1103.5077/main.tex
    303:  Let $|z| \le 1$ and $Q(z)=0$.  Then $\Im(z)=0$.

(= the brief's C2(ii): no non-real pole of `R` in the disc.)

    $ grep -n -F 'we refer to such states as \emph{half-bound states}' src/1103.5077/main.tex
    232:The states $\bound{\pm}{\kappa}$ with $\kappa>0$ have amplitudes that decay exponentially along the semi-infinite path, so we refer to them collectively as \emph{evanescent bound states}.  However, in the preceding discussion, we have allowed the possibility that $\kappa=0$.  States of the form $\bound{\pm}{0}$ may or may not exist depending on whether $Q(\pm 1) = 1 \mp (a + C(\pm 1)) = 0$.  Using the terminology of Ref.~\cite{HKS91}, we refer to such states as \emph{half-bound states}.  This reflects that they are, in a sense, halfway between scattering and bound states: when they exist, we have $\bound{+}{0} = \scattering{0}$ and $\bound{-}{0} = \scattering{\pi}$.

    $ grep -n -F 'Half-bound states\cite{hinton:754} are unnormalizable states' src/1203.6557/levinson2.tex
    321:Half-bound states\cite{hinton:754} are unnormalizable states that are ``almost'' bound states. They are eigenstates of the Hamiltonian taking the form \eqref{eq:bound_states} on the semi-infinite lines with $z\in\{-1,1\}$ (where $\vec{\alpha}\neq\vec{0})$. 

    $ grep -n -F 'Thus, confined bound states correspond to eigenvectors $\psi$ of $D$ that also satisfy the further condition of orthogonality to $b$.' src/1103.5077/main.tex
    242:The lower block says that $\psi$ is an eigenvector of $D$ with eigenvalue $\lambda$, and the upper block says that $b^\dag \psi=0$.  Thus, confined bound states correspond to eigenvectors $\psi$ of $D$ that also satisfy the further condition of orthogonality to $b$.  Note that if $\lambda$ is a degenerate eigenvalue of $D$, then there may be multiple confined bound states corresponding to $\lambda$.  In general, the number of confined bound states corresponding to $\lambda$ is the dimension of the subspace $\{\psi\colon D\psi = \lambda\psi,\, b^\dag \psi = 0\}$.  If $b$ is orthogonal to the $\lambda$-eigenspace of $D$, this dimension is simply the multiplicity of $\lambda$; otherwise it is the multiplicity of $\lambda$ minus $1$.

(= the brief's C2(iii) "cusp forms", exactly.)

### 2.5 Which direction is incoming, and the phase convention

    $ grep -n -F 'there is an incoming scattering state of momentum $k$, denoted $|\tilde k, \incoming_j\>$, of the form' src/0806.1972/uwalk.tex
    138:Now consider an arbitrary finite graph $G$, and create an infinite graph with adjacency matrix $H$ by attaching a semi-infinite line to each of $N$ of its vertices.  Label the basis states for vertices on the $j$th semi-infinite line as $|x,j\>$, with $x=0$ at the vertex in the original graph and $x=1,2,\ldots$ moving out along the line.  On each semi-infinite line, an eigenstate of the adjacency matrix must be a linear combination of states of the form \eq{kstate} with momenta $\pm k$, corresponding to an eigenvalue $2 \cos k$; or possibly of the same form but with $k=\ii\kappa$ or $k=\ii\kappa + \pi$ for some $\kappa > 0$, corresponding to an eigenvalue $2 \cosh \kappa$ or $-2\cosh\kappa$, respectively.  For each $j \in \{1,\ldots,N\}$ and each $k \in [-\pi,0]$,\footnote{Since the off-diagonal elements of the adjacency matrix are positive, whereas in a discrete approximation to the kinetic term $-{\d^2}/{\d{x}^2}$ they are negative, we use the convention that incoming states have \emph{negative} momentum.} there is an incoming scattering state of momentum $k$, denoted $|\tilde k, \incoming_j\>$, of the form

    $ grep -n -F '\<x,j |\tilde k, \incoming_j\> &= e^{-\ii k x} + R_j(k) \, e^{\ii k x} \\' src/0806.1972/uwalk.tex
    140:  \<x,j |\tilde k, \incoming_j\> &= e^{-\ii k x} + R_j(k) \, e^{\ii k x} \\

    $ grep -n -F 'The incoming states are related to the outgoing states by a transformation known as the scattering matrix' src/0806.1972/uwalk.tex
    185:on the semi-infinite lines.  The incoming states are related to the outgoing states by a transformation known as the scattering matrix, or $S$-matrix, with $|\tilde k,\incoming_j\> = \sum_{j'} S_{j,j'}(k) |\tilde k,\outgoing_{j'}\>$.  It can be shown that the $S$-matrix is unitary, and has the form $S_{j,j}(k)=R_j(k)$ and $S_{j,j'}(k)=T_{j,j'}(k)$ for $j \ne j'$.  In particular, the orthogonality of columns $j$ and $j'$ of $S$ implies that $T_{j,j'} R_j^* + R_{j'} R_{j',j}^* + \sum_{\jbar \notin \{j,j'\}} T_{\jbar,j'} T_{\jbar,j}^* = 0$, giving the cancellation in \eq{evolution}.

The phase convention is *not* canonical, and Childs says so (this matters for the brief's C3
"which of `R`, `1/R` plays the role of `phi`"):

    $ grep -n -F 'Note that the expression \eq{rcoeff} depends on the choice \eq{scattering} for the form of the scattering states.' src/1103.5077/main.tex
    179:Applying this identity to the upper block of \eq{eigeqn} and solving for $R(e^{\ii k})$, we find\footnote{Note that the expression \eq{rcoeff} depends on the choice \eq{scattering} for the form of the scattering states.  In particular, it assumes a particular convention for the overall phases of these states.  While the stated form will turn out to be convenient for our purposes, other natural choices can be obtained by taking states of the same form, but numbering vertices on the semi-infinite path starting from an integer other than $1$.  Such a choice modifies the reflection coefficient by factors of $e^{\ii k}$, which ultimately modifies the statement of Levinson's theorem.}

Note `0806.1972` starts the tail at `x = 0` while `1103.5077` and `1203.6557` start at `x = 1`;
the brief starts at `k = 1`, so the brief agrees with `1103.5077`/`1203.6557`, not with `0806.1972`.

### 2.6 Negative results (nothing on resonances, nothing on Lax–Phillips)

    $ grep -c -i resonan src/0806.1972/uwalk.tex src/1103.5077/main.tex src/1203.6557/levinson2.tex src/1205.3782/MPQW.tex src/1406.4510/momentumswitch.tex src/quant-ph/9706062/FarhiGutmann2651WEB.tex src/quant-ph/0209131/walk.tex src/0810.0312/main.tex
    src/1103.5077/main.tex:0
    src/0806.1972/uwalk.tex:0
    src/1203.6557/levinson2.tex:0
    src/1406.4510/momentumswitch.tex:0
    src/0810.0312/main.tex:0
    src/quant-ph/9706062/FarhiGutmann2651WEB.tex:0
    src/quant-ph/0209131/walk.tex:0
    src/1205.3782/MPQW.tex:0

Same command with `-i -E "lax.phillips|ihara|zeta function"` returns `0` for all files except
`src/0810.0312/main.tex:1`, which is the Kedlaya bibliography line noted in §1.

---

## 3. DICTIONARY: Childs's conventions vs the brief's

The identification is **exact**, not analogical. Take Childs's `1103.5077` block matrix
`(a b^dag ; b D)` and set

> `a = 0`,  `b = c |v_0>` (a vector in `C^m` supported on the brief's junction vertex),  `D = T_X`.

Childs's "first vertex of `G`", labelled `x = 1`, is then the brief's ray site `r_1`; his `m`
internal vertices are the brief's core `V_X` (so `m = n` in the brief's notation, and Childs's
total graph has `n + 1` vertices).

| brief (`astra-brief.md`) | Childs (`1103.5077`, `1203.6557`, `0806.1972`) | notes |
|---|---|---|
| `lambda = z + 1/z` | energy `2 cos k`, `z = e^{ik}`; `1203.6557:331` writes it as `z + 1/z` | identical; `|z| = 1` ↔ `k` real |
| `z = q^{s-1/2}`, `|z|=1` ↔ `Re s = 1/2` | no arithmetic parametrisation | brief's addition |
| ray `r_1, r_2, ...`, ansatz `z^{-k} + R z^k`, `k >= 1` | `<x|sc(k)> = e^{-ikx} + R e^{ikx}`, `x >= 1` (`1103.5077:159`) | **same offset**, same sign |
| incoming = down the cusp toward the core | incoming = `k in (-pi,0)`, i.e. `z` on the lower half circle (`0806.1972:138` footnote) | `z^{-x} = e^{-ikx}` is the incoming piece in both |
| `G(lambda) = <v_0|(lambda - T_X)^{-1}|v_0>` | `C(z) = b^dag((z+1/z) - D)^{-1} b` (`1103.5077:186`) | `C(z) = c^2 G(lambda)` |
| `R(z) = (1 - c^2 G z^{-1})/(c^2 G z - 1)` | `R(z) = -Q(1/z)/Q(z)`, `Q(z) = 1 - z(a + C(z))` (`1103.5077:181,185`) | **algebraically identical** with `a=0`, `b = c|v_0>`; verified numerically below |
| coupling `c > 0`, cusp weight `c^2 = q+1` | `||b||`, an arbitrary weight | `c` is **not** a new ingredient: Childs allows arbitrary complex weighted `b`. What is new is only the *interpretation* `c^2 = q+1` from Serre's tree quotient |
| C2(i) poles of `R` in `|z|<1` = `l^2` eigenvalues outside `[-2,2]` | bound states at `z = ±e^{-kappa}`, energy `±2 cosh kappa`, roots of `Q` (`1103.5077:232` and around) | same |
| C2(ii) no non-real pole in the disc | Lemma `1103.5077:303` | **proved there** |
| C2(iii) cusp forms = core eigenvectors vanishing at `v_0`, invisible to `R` | *confined bound states* = eigenvectors of `D` with `b^dag psi = 0` (`1103.5077:242`) | same; Childs also computes the common-factor count `2(n_c + mbar - m)` |
| C2(iv) resonances = zeros of `R` in `|z|<1` | **unnamed**; they appear only as `Z_int(Q(1/z))` inside the Levinson proof | Childs never says "resonance" (§2.6) |
| — (missing from the brief) | **half-bound states** at `z = ±1` (`1103.5077:232`, `1203.6557:321`) | the threshold `lambda = ±2`; under `z = q^{s-1/2}` these are `s = 1/2` and `s = 1/2 + i pi/log q` |
| `h`-cusp scattering matrix | `n x n` S-matrix `S(z) = -Q(z)^{-1} Q(1/z)` (`1203.6557:365`), `Q(z) = 1 - z(A + B^dag((1/z)+z-D)^{-1} B)` | exactly the matrix generalisation T8 needs |
| determinant form of `R` | `det S(z) = (-1)^n z^{2m} W(1/z)/W(z)`, `W(z) = det gamma(z)`, `gamma(z) = (zA-1, zB^dag ; zB, zD - z^2 - 1)` (`1203.6557`, proof of the theorem at `:511`) | Childs's is the *polynomial* version; see the sign correction below |

**Degrees and counts.** With `a = 0` and `c != 1` (so `||b|| != 1`), `1103.5077:365` gives
`deg(numerator of Q) = 2n - 2n_c`. Splitting those roots: `n_b` inside the circle (the brief's
"trivial" poles of `R`), `n_h` on the circle at `z = ±1` (half-bound), and the rest outside,
whose reciprocals are the zeros of `R` inside. Hence

> **#resonances = `2n - 2n_c - n_b - n_h`**, and Levinson (`1103.5077:277`) is equivalent to
> **`w_Gamma(R) = #resonances - n_b`**, i.e. the argument principle for `R` on `|z| = 1`.

This is precisely the count the brief's C2(iv) asks for — with an extra term, `n_h`, that the
brief does not have.

**Coupling `c = 1` is the excluded case.** Childs I needs `a != 0` or `||b|| != 1`, i.e. in the
brief's variables `c != 1` (with no loop at the junction). The arithmetic case `c^2 = q + 1 >= 3`
is safely inside the hypothesis, but any toy core in T7 with `c = 1` is **not**; there `R` acquires
a zero/pole at `z = 0` and the count shifts. Childs–Gosset `1203.6557` removes the hypothesis
entirely, so the notebook should quote **II**, not I, for the general statement.

**Sign correction to the brief's C1.** `det(lambda - T_X - a P_0) = det(lambda - T_X)(1 - a G)`
gives
`det(lambda - T_X - c^2 z^{-1} P_0)/det(lambda - T_X - c^2 z P_0) = (1 - c^2 G z^{-1})/(1 - c^2 G z) = -R(z)`.
So the brief's determinant form in C1 is off by a sign relative to its own `R`; the correct
statement is `R(z) = -det(lambda - T_X - c^2 z^{-1} P_0)/det(lambda - T_X - c^2 z P_0)`, which is
Childs's `-Q(1/z)/Q(z)` written out. Numerically confirmed (random real symmetric `4 x 4` `T_X`,
`c = 1.7`, three values of `z`): `R_brief = R_Childs = -R_det` to 8 decimals.

**Pure cusp (brief C3) inside Childs's framework.** `m = 1`, `D = [0]`, `b = sqrt(q+1)`, `a = 0`:
`C(z) = (q+1)/(z + 1/z)`, `Q(z) = (1 - q z^2)/(1 + z^2)`, so `R(z) = -Q(1/z)/Q(z) = (z^2 - q)/(q z^2 - 1)`
— the brief's C3 value, confirmed numerically at `q = 5`. Childs's bookkeeping then reads
`n_b = 2` (`z = ±q^{-1/2}`), `n_c = n_h = 0`, degree `2m - 2n_c = 2`, `#resonances = 0`, and
`w_Gamma(R) = 2(1 - 2 - 0 - 0) = -2`. All four agree with the brief.

**`R` vs `1/R`.** Since `R(z) R(1/z) = 1`, the brief's `phi`-analogue `1/R` is Childs's reflection
coefficient evaluated at `1/z` — equivalently the reflection coefficient of the *outgoing*
scattering states (`0806.1972:180`, `<x,j|sc^<-_j> = e^{ikx} + R_j(k)^* e^{-ikx}`). So the brief's
`1/R = q zeta_K(2s-1)/zeta_K(2s)` is the outgoing-convention object; Childs's `R` as literally
defined is its inverse. Stating this once fixes the brief's C3 question.

---

## 4. Assessment

**Exactly the brief's setup — must be cited as prior art.**
1. The object: a finite weighted graph with one (or `n`) semi-infinite unit-weight paths attached,
   adjacency operator, energy `2 cos k = z + 1/z`.
2. The reflection coefficient `R(z) = -Q(1/z)/Q(z)` with `Q(z) = 1 - z(a + b^dag((z+1/z)-D)^{-1}b)`
   — *identical* to the brief's `R`, including sign, once `a = 0`, `b = c|v_0>`.
3. Rationality of `R`, `|R| = 1` on the circle, `R(z)R(1/z) = 1`, analytic continuation off the
   circle, and the classification of the poles in the disc as real and simple — C1, C2(i), C2(ii)
   are all theorems in `1103.5077`.
4. C2(iii) is Childs's "confined bound states", with the common-factor count.
5. The `h`-cusp S-matrix and its determinant `det S(z) = (-1)^n z^{2m} W(1/z)/W(z)` with
   `W = det gamma` — `1203.6557`. This is the matrix statement the brief's T8 says the arithmetic
   round needs, and it already exists.
6. Completeness of scattering + bound + confined states as a basis (`1203.6557` Thm, Goldstone for
   `n = 1`) — the brief's T1(b) `H_LP` decomposition rests on exactly this.

**Different — genuinely new in the brief.**
- *Time.* Childs is continuous time (`e^{-iHt}`); the brief's T1 is the discrete wave equation
  `u_{m+1} = T u_m - u_{m-1}` and a Lax–Phillips contraction `Z` with rank-one defect. Childs has
  **no** wave group, **no** `D_±`, **no** `Z`, **no** characteristic function / Sz.-Nagy–Foias.
  Confirmed: zero hits for `lax.phillips` (§2.6).
- *Resonances.* Childs never names, studies, or interprets the zeros of `R` in the disc; they are
  a bookkeeping term in the Levinson proof. The brief makes them the object (spectrum of `Z`),
  which is new relative to Childs. (Arends–Peterson–Weich `2603.26443`, already in
  `notes/cusp-graph/sources.md`, is the paper that *does* define them; `2602.03192` does the
  discrete-time version.)
- *Arithmetic.* No tree quotients, no Serre, no `c^2 = q+1`, no zeta or `L`-functions, no
  "all resonances on `|z| = q^{-1/4}`". Childs's weights are free parameters chosen to build gates.
- *RH / Ramanujan.* Nothing.
- *Cusp weight.* Formally covered (Childs allows any weighted `b`), so `c^2 = q + 1` is **not** a
  new ingredient at the level of the formula — only at the level of interpretation. The brief
  should not claim novelty for it.

**Usable directly.**
- **Levinson's theorem** (`1103.5077:277`, `1203.6557:511`) is exactly a count of the brief's
  C2(iv) in the form `w_Gamma(R) = #resonances - #bound states`, with the half-bound correction.
  Take the `1203.6557` version: no hypothesis on the core, and it covers `h` cusps at once.
- **The degree lemma** (`1103.5077:365`) answers C1's "state the degree of `R`": `2n - 2n_c`
  when `a = 0`, `c != 1` (and `2n - 2n_c + 1` when there is a loop at the junction).
- **Lemma at `:303`** proves C2(ii) outright; the companion "no repeated roots" lemma proves that
  the poles of `R` in the disc are simple, which the brief needs for H-SIMPLE on the trivial side.
- **Completeness** (`1203.6557`) is the prerequisite for T1(b).
- **`gamma(z)` and `W(z) = det gamma(z)`** give the polynomial `p`/`ptilde` of the brief's C1 in
  ready-made `h`-cusp form: `W(z)` is the brief's `ptilde`-analogue up to normalisation, and
  `det S(z) = (-1)^n z^{2m} W(1/z)/W(z)` is the brief's `R = p/ptilde` up to the power of `z` the
  brief asks to determine — Childs determines it: `z^{2m-k}` where `k = deg W`.

**Gap the lead exposes in the brief.** The brief's C2 has no `z = ±1` (threshold / half-bound)
case. Childs shows these occur exactly when `Q(±1) = 0` and that they must be counted as half a
bound state or the winding count is wrong. Under `z = q^{s-1/2}` they sit at `s = 1/2` and
`s = 1/2 + i pi / log q` — i.e. *on the critical line* — so for the arithmetic round they are not
a curiosity: they are the discrete analogue of a pole of the scattering matrix at the centre of
the critical line. C2 and T1(c) (`dim K`) should be restated with an `n_h` term.

---

## 5. Manifest check

    $ cd refs && sha256sum -c --quiet manifest.sha256 && echo MANIFEST OK
    MANIFEST OK
