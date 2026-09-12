# The Ihara–Bass formula for the non-backtracking superoperator of an arbitrary Kraus family

Written 2026-09-12. Author of the proof: Claude Fable 5.1 (orchestrator). Style: Lamport structured proof; status tags follow rk-light (`sketched` = written by the author and not yet attacked; `proved` only after a reviewer other than the author returns VALID; `numerical` = checked in `scripts/qihara_general.py`, output in `outputs/qihara_general.txt`). Provenance quotes are cited as `<arxiv-id>:<file>:<line>` against `refs/src/`.

**Status banner.** Theorem 1: `proved` + `numerical`. Corollaries 2–4: `proved`, each depending on Theorem 1. Reviewer ≠ author: two Opus round-1 reports (`notes/reviews/theorem1-algebra-2026-09-12.md`: VALID with four cosmetic fixes, applied; `notes/reviews/provenance-2026-09-12.md`: citation addresses and the Watanabe–Fukumizu framing corrected) and a round-2 re-verification (`notes/reviews/round2-2026-09-12.md`: all verdicts VALID, 48/48 citations byte-checked). Single family declared (author Claude Fable 5.1, reviewers Claude Opus); no codex lane. Edits after the round-2 receipt: only the cosmetic items that receipt itself lists (norm convention, the word "cofinite" justified, wording of "every such $u$"). Prior art: Theorem 1 is the bouquet (one vertex, all edges loops) analogue of Watanabe–Fukumizu's arbitrary-weight corollary, which is stated for loopless graphs (`cited`, §5); no local source covers arbitrary weights on a bouquet, and the proof here is self-contained.

## 1. Setting and conventions

- $V$ is a finite-dimensional complex vector space, $N = \dim V$. In the application $V = M_n(\mathbb C)$ with the Hilbert–Schmidt inner product, $N = n^2$.
- $D = 2m$ is even; $\sigma$ is a fixed-point-free involution on $[D] = \{1,\dots,D\}$ (the *reversal*). Write $\bar i = \sigma(i)$.
- $\mathcal E_1,\dots,\mathcal E_D \in \operatorname{End}(V)$ are arbitrary linear maps. No invertibility, positivity or unitarity is assumed.
- Edge space $W = V\otimes\mathbb C^D$, with $\mathbb C^D$ spanned by $|1\rangle,\dots,|D\rangle$. Elements are written $x = \sum_i x_i\otimes|i\rangle$, $x_i\in V$ the *component* of $x$ at $i$.
- **Non-backtracking operator.** $T\in\operatorname{End}(W)$,
$$
T\,(v\otimes|i\rangle) \;=\; \sum_{j\ne \bar i} \mathcal E_i v\otimes|j\rangle .
$$
- **Zeta function.** $\zeta(u) = \det_W(1-uT)^{-1}$, a rational function of $u\in\mathbb C$.
- $\|\cdot\|$ is the operator norm (any submultiplicative norm on $\operatorname{End}(V)$ would do).
- Determinants: $\det_V$, $\det_W$ over the named space. Sylvester's identity $\det(1-XY) = \det(1-YX)$ for $X: V\to W$, $Y: W\to V$ is used without further comment. For a $2\times2$ block operator with identity diagonal blocks, $\det\begin{pmatrix}1 & B\\ C & 1\end{pmatrix} = \det(1-CB) = \det(1-BC)$ (Schur complement, then Sylvester).
- **Kraus case** (Corollary 2). $V = M_n$, $A_1,\dots,A_m\in M_n$ arbitrary, $A_{m+k} = A_k^\dagger$, $\sigma(k) = m+k$, and $\mathcal E_i = \operatorname{Ad}(A_i): \rho\mapsto A_i\rho A_i^\dagger$. With column stacking, $\operatorname{Ad}(A) = \bar A\otimes A$ as an $n^2\times n^2$ matrix, so $\operatorname{Tr}_V\operatorname{Ad}(A) = |\operatorname{Tr}A|^2$ and $\operatorname{Ad}(A)\operatorname{Ad}(B) = \operatorname{Ad}(AB)$.
- Unfixed choices (none needed below): normalisation of the channel ($\sum_i\mathcal E_i$ versus $\frac1D\sum_i\mathcal E_i$); the notebook elsewhere uses $D\Phi = \sum_i \mathcal E_i$.

## 2. Statement

**Theorem 1** (`proved`, `numerical`). Let $u\in\mathbb C$ be such that $1 - u^2\,\mathcal E_{\bar i}\mathcal E_i$ is invertible for every $i\in[D]$. Then
$$
\det_W(1-uT) \;=\; \prod_{\{i,\bar i\}} \det_V\!\big(1 - u^2\,\mathcal E_{\bar i}\mathcal E_i\big)\;\cdot\;\det_V\!\big(1 + \mathcal D(u) - \mathcal A(u)\big),
$$
where the product is over the $m$ unordered pairs $\{i,\bar i\}$ (well defined since $\det(1-u^2\mathcal E_{\bar i}\mathcal E_i) = \det(1-u^2\mathcal E_i\mathcal E_{\bar i})$), and
$$
\mathcal A(u) \;=\; u\sum_{i=1}^{D} \mathcal E_i\,\big(1-u^2\mathcal E_{\bar i}\mathcal E_i\big)^{-1},
\qquad
\mathcal D(u) \;=\; u^2\sum_{i=1}^{D} \mathcal E_{\bar i}\mathcal E_i\,\big(1-u^2\mathcal E_{\bar i}\mathcal E_i\big)^{-1}.
$$
The hypothesis holds for all $|u| < \big(\max_i \|\mathcal E_{\bar i}\mathcal E_i\|\big)^{-1/2}$ (all $u$ if every $\mathcal E_{\bar i}\mathcal E_i = 0$), and the identity holds pointwise at every $u$ satisfying the hypothesis; since the left side is a polynomial of degree $\le ND$ and the right side is rational, the two sides are equal as rational functions.

**Corollary 2** (Kraus families, `proved`; deps: Theorem 1). For arbitrary $A_1,\dots,A_m\in M_n$ with the adjoint pairing of §1,
$$
\det_W(1-uT) \;=\; \prod_{k=1}^{m}\det\!\big(1-u^2\operatorname{Ad}(A_k^\dagger A_k)\big)\cdot \det\!\big(1+\mathcal D(u)-\mathcal A(u)\big),
$$
valid for $|u| < \min_k\|A_k\|^{-2}$; here $\mathcal E_{\bar i}\mathcal E_i = \operatorname{Ad}(A_k^\dagger A_k)$ for $i = k\le m$ and $\operatorname{Ad}(A_kA_k^\dagger)$ for $i = m+k$, both positive semidefinite superoperators. Moreover, for every $\ell\ge1$,
$$
\operatorname{Tr}_W T^{\ell} \;=\; \sum_{\substack{(i_1,\dots,i_\ell)\in[D]^\ell\\ i_{k+1}\ne\bar i_k\ (k\in\mathbb Z/\ell)}} \big|\operatorname{Tr}\big(A_{i_\ell}\cdots A_{i_1}\big)\big|^2 \;\ge 0,
$$
so $\zeta(u) = \exp\sum_\ell \frac{u^\ell}{\ell}\operatorname{Tr}T^\ell$ has nonnegative Taylor coefficients, and $\zeta(u) = \prod_{[w]}\det_V\big(1 - u^{|w|}\operatorname{Ad}(A_w)\big)^{-1}$ over primitive cyclically non-backtracking classes $[w]$.

**Corollary 3** (inverse pairing, `proved`; deps: Theorem 1). If $\mathcal E_{\bar i} = \mathcal E_i^{-1}$ for all $i$ (in particular for unitary Kraus operators $A_{\bar i} = A_i^\dagger = A_i^{-1}$), then with $\Sigma = \sum_i\mathcal E_i$,
$$
\det_W(1-uT) \;=\; (1-u^2)^{N(D-2)/2}\,\det_V\!\big(1 - u\,\Sigma + (D-1)u^2\big).
$$
For $V = M_n$ and $\Sigma = D\Phi$ this is the formula of `HANDOFF.md` item 1 and of Matsuura–Ohta eq. (2.11) on the bouquet.

**Corollary 4** (which factor carries the spectrum, `proved`; deps: Theorem 1). The poles of $\zeta$ are among the roots of $\det_V(1+\mathcal D(u)-\mathcal A(u)) = 0$ together with the points $u^2 = 1/\lambda$, $\lambda\in\operatorname{spec}(\mathcal E_{\bar i}\mathcal E_i)\setminus\{0\}$; the latter may cancel against poles of the second factor, as they do in Corollary 3 (exponent $ND/2$ against $-N$; for $D = 2$ the exponent there is $0$ and the cancellation is total). For $D = 2$ in general, $T = \mathcal E_1\oplus\mathcal E_2$ on $W = V\oplus V$ because the only non-backtracking successor of $i$ is $i$ itself, so $\det_W(1-uT) = \det_V(1-u\mathcal E_1)\det_V(1-u\mathcal E_2)$; Theorem 1 then expresses this product through the single pair factor $\det_V(1-u^2\mathcal E_2\mathcal E_1)$. Conversely a pole of the second factor, which can only sit at a point where some $1-u^2\mathcal E_{\bar i}\mathcal E_i$ is singular, cannot be a pole of $\zeta$ unless it survives multiplication by the first factor.

## 3. Proof of Theorem 1 (Lamport structure)

ASSUME: $u\in\mathbb C$ with $1-u^2\mathcal E_{\bar i}\mathcal E_i$ invertible for all $i\in[D]$.
PROVE: the displayed identity.

⟨1⟩1. **Three auxiliary maps and the decomposition $T = SR - J$.** Define
$R: W\to V$, $R(v\otimes|i\rangle) = \mathcal E_i v$;
$S: V\to W$, $Sv = \sum_{j=1}^{D} v\otimes|j\rangle$;
$J: W\to W$, $J(v\otimes|i\rangle) = \mathcal E_i v\otimes|\bar i\rangle$.
Then $T = SR - J$.
PROOF: On $v\otimes|i\rangle$: $SR(v\otimes|i\rangle) = \sum_j \mathcal E_i v\otimes|j\rangle$ and $J(v\otimes|i\rangle) = \mathcal E_i v\otimes|\bar i\rangle$, so $(SR-J)(v\otimes|i\rangle) = \sum_{j\ne\bar i}\mathcal E_iv\otimes|j\rangle = T(v\otimes|i\rangle)$. Both sides are linear and these vectors span $W$. $\square$

⟨1⟩2. **Block structure of $J$.** For each pair $p = \{i,\bar i\}$ let $W_p = V\otimes\operatorname{span}\{|i\rangle,|\bar i\rangle\}$. Then $W = \bigoplus_p W_p$, $J W_p\subseteq W_p$, and in the ordered decomposition $W_p = V\oplus V$ (component at $i$, component at $\bar i$)
$$
J|_{W_p} = \begin{pmatrix} 0 & \mathcal E_{\bar i}\\ \mathcal E_i & 0\end{pmatrix}.
$$
PROOF: $J$ sends component $i$ to component $\bar i$ through $\mathcal E_i$ and component $\bar i$ to component $i$ through $\mathcal E_{\bar i}$ (apply the definition to $v\otimes|i\rangle$ and to $v\otimes|\bar i\rangle$, using $\bar{\bar i} = i$). The direct-sum decomposition is the partition of $[D]$ into $\sigma$-orbits, which have size two because $\sigma$ is fixed-point-free. $\square$

⟨1⟩3. **$1+uJ$ is invertible, with $\det_W(1+uJ) = \prod_p\det_V(1-u^2\mathcal E_{\bar i}\mathcal E_i)$.**
PROOF: By ⟨1⟩2, $\det_W(1+uJ) = \prod_p\det\begin{pmatrix}1 & u\mathcal E_{\bar i}\\ u\mathcal E_i & 1\end{pmatrix} = \prod_p\det_V(1-u^2\mathcal E_i\mathcal E_{\bar i}) = \prod_p\det_V(1-u^2\mathcal E_{\bar i}\mathcal E_i)$ (block determinant with identity diagonal, then Sylvester). Each factor is nonzero by ASSUME, so $1+uJ$ is invertible. $\square$

⟨1⟩4. **Explicit inverse on a pair.** Write $B = u\mathcal E_{\bar i}$, $C = u\mathcal E_i$, $P = (1-BC)^{-1} = (1-u^2\mathcal E_{\bar i}\mathcal E_i)^{-1}$, $Q = (1-CB)^{-1} = (1-u^2\mathcal E_i\mathcal E_{\bar i})^{-1}$; both exist by ASSUME (the second is the hypothesis at the index $\bar i$). Then
$$
(1+uJ)^{-1}\big|_{W_p} = \begin{pmatrix} P & -BQ\\ -CP & Q\end{pmatrix}.
$$
PROOF: Multiply: $\begin{pmatrix}1&B\\C&1\end{pmatrix}\begin{pmatrix}P&-BQ\\-CP&Q\end{pmatrix} = \begin{pmatrix}(1-BC)P & -BQ+BQ\\ CP-CP & (1-CB)Q\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix}$. A right inverse of a square operator on a finite-dimensional space is the inverse. $\square$

⟨1⟩5. **Sylvester step.** $\det_W(1-uT) = \det_W(1+uJ)\cdot\det_V\!\big(1 - u\,R(1+uJ)^{-1}S\big)$.
PROOF: By ⟨1⟩1, $1-uT = 1+uJ-uSR = (1+uJ)\big(1 - u(1+uJ)^{-1}SR\big)$, using ⟨1⟩3 for the inverse. Take determinants; apply Sylvester with $X = u(1+uJ)^{-1}S: V\to W$ and $Y = R: W\to V$. $\square$

⟨1⟩6. **Computation of $M(u) := R(1+uJ)^{-1}S$.** $M(u) = \sum_{i=1}^{D}\big(\mathcal E_i - u\,\mathcal E_{\bar i}\mathcal E_i\big)\big(1-u^2\mathcal E_{\bar i}\mathcal E_i\big)^{-1}$.
PROOF: For $v\in V$, $Sv$ has component $v$ at every index. By ⟨1⟩4, on the pair $p=\{i,\bar i\}$ the vector $(1+uJ)^{-1}Sv$ has component $(P - BQ)v$ at $i$ and $(-CP + Q)v$ at $\bar i$. Applying $R$ (which applies $\mathcal E_i$ to the component at $i$, $\mathcal E_{\bar i}$ to the component at $\bar i$, and sums over all indices) and substituting $B, C, P, Q$:
$$
\text{pair }p\text{ contributes}\quad \mathcal E_iP - u\,\mathcal E_i\mathcal E_{\bar i}Q \;+\; \mathcal E_{\bar i}Q - u\,\mathcal E_{\bar i}\mathcal E_iP
\;=\; (\mathcal E_i - u\mathcal E_{\bar i}\mathcal E_i)P \;+\; (\mathcal E_{\bar i} - u\mathcal E_i\mathcal E_{\bar i})Q .
$$
The first summand is the $i$-th term of the claimed sum and the second is the $\bar i$-th term (since $Q = (1-u^2\mathcal E_{\bar{\bar i}}\mathcal E_{\bar i})^{-1}$). Summing over the $m$ pairs gives the sum over all $D$ indices. $\square$

⟨1⟩7. **$1 - uM(u) = 1 + \mathcal D(u) - \mathcal A(u)$.**
PROOF: Expand ⟨1⟩6 linearly: $uM(u) = u\sum_i\mathcal E_i(1-u^2\mathcal E_{\bar i}\mathcal E_i)^{-1} - u^2\sum_i\mathcal E_{\bar i}\mathcal E_i(1-u^2\mathcal E_{\bar i}\mathcal E_i)^{-1} = \mathcal A(u) - \mathcal D(u)$. $\square$

⟨1⟩8. **QED.** Combine ⟨1⟩5, ⟨1⟩3 and ⟨1⟩7; steps ⟨1⟩1–⟨1⟩7 hold pointwise at every $u$ satisfying ASSUME, with no analyticity used. The bound $|u| < (\max_i\|\mathcal E_{\bar i}\mathcal E_i\|)^{-1/2}$ makes $\|u^2\mathcal E_{\bar i}\mathcal E_i\| < 1$, so the Neumann series gives the inverses and ASSUME holds there; the set of admissible $u$ is cofinite (its complement is the zero set of the polynomial $\prod_i\det_V(1-u^2\mathcal E_{\bar i}\mathcal E_i)$, which equals $1$ at $u=0$ and so is not identically zero), and two rational functions agreeing on a cofinite set are equal. $\square$

## 4. Proofs of the corollaries

**Corollary 2.** ⟨1⟩1. $\mathcal E_{\bar i}\mathcal E_i = \operatorname{Ad}(A_{\bar i})\operatorname{Ad}(A_i) = \operatorname{Ad}(A_{\bar i}A_i)$, which is $\operatorname{Ad}(A_k^\dagger A_k)$ or $\operatorname{Ad}(A_kA_k^\dagger)$; $\operatorname{Ad}(P) = \bar P\otimes P$ has spectrum $\{\bar p_a p_b\}\subseteq[0,\infty)$ for $P\ge0$ with eigenvalues $p_a$, and $\|\operatorname{Ad}(A_k^\dagger A_k)\| = \|A_k\|^4$, so the hypothesis of Theorem 1 holds for $|u|<\min_k\|A_k\|^{-2}$; the pair factors are $\det(1-u^2\operatorname{Ad}(A_k^\dagger A_k))$, one per $k$ (the two orderings have equal determinant by Sylvester).
⟨1⟩2. Trace formula: by induction on $\ell$, $T^\ell(v\otimes|i_1\rangle) = \sum \mathcal E_{i_\ell}\cdots\mathcal E_{i_1}v\otimes|i_{\ell+1}\rangle$, the sum over $(i_2,\dots,i_{\ell+1})$ with $i_{k+1}\ne\bar i_k$ for $k=1,\dots,\ell$. Taking the trace over $W = V\otimes\mathbb C^D$ sets $i_{\ell+1} = i_1$, which adds the cyclic condition $i_1\ne\bar i_\ell$, and leaves $\operatorname{Tr}_V(\mathcal E_{i_\ell}\cdots\mathcal E_{i_1}) = \operatorname{Tr}_V\operatorname{Ad}(A_{i_\ell}\cdots A_{i_1}) = |\operatorname{Tr}(A_{i_\ell}\cdots A_{i_1})|^2$.
⟨1⟩3. Nonnegativity of the coefficients of $\log\zeta = \sum_\ell u^\ell\operatorname{Tr}T^\ell/\ell$ implies nonnegativity for $\zeta = \exp(\cdot)$. The Euler product is the standard regrouping of cyclic words into powers of primitive classes, $\sum_{k\ge1}\frac{u^{k|w|}}{k}\operatorname{Tr}\operatorname{Ad}(A_w)^k = -\log\det(1-u^{|w|}\operatorname{Ad}(A_w))$, valid for $|u|$ small. $\square$

**Corollary 3.** With $\mathcal E_{\bar i}\mathcal E_i = 1$: each pair factor is $\det_V(1-u^2) = (1-u^2)^N$, so the product is $(1-u^2)^{ND/2}$; $\mathcal A(u) = \frac{u}{1-u^2}\Sigma$, $\mathcal D(u) = \frac{Du^2}{1-u^2}$; hence $1+\mathcal D-\mathcal A = \frac{1}{1-u^2}\big(1 - u\Sigma + (D-1)u^2\big)$ and its determinant is $(1-u^2)^{-N}\det_V(1-u\Sigma+(D-1)u^2)$. Total exponent $ND/2 - N = N(D-2)/2$. The computation divides by $1-u^2$, so it is carried out for $u^2\ne1$; both sides are polynomials in $u$, so the identity extends to $u^2 = 1$. $\square$

**Corollary 4.** Immediate from the factorisation: a zero of the polynomial $\det_W(1-uT)$ is a zero of the product, each factor is analytic away from the points named, and the polynomial has no poles, so every pole of the second factor is cancelled by a zero of the first. $\square$

## 5. Provenance and relation to the literature

- Watanabe & Fukumizu, arXiv:1103.0605, `section3.tex:330-341`, Corollary `cor:IBfornonhyper`: `Z_{G}(\bs{u})^{-1}= \det ( I + \hat{\mathcal{D}}(\bsu) - \hat{\mathcal{A}}(\bsu) ) \prod_{[e] \in {E}} \det(I - u_e u_{\bar{e}})` with `(\hat{\mathcal{D}}(\bsu)g)(i):= \Big( \sum_{e: t(e)=i}(I_{r_i}-u_eu_{\bar{e}})^{-1}u_eu_{\bar{e}} \Big)g(i)` and `(\hat{\mathcal{A}}(\bsu)g)(i):= \sum_{e: t(e)=i}(I_{r_i}-u_eu_{\bar{e}})^{-1}u_e g(o(e))`; and `section3.tex:373`: "Corollary \ref{cor:IBfornonhyper} gives the extension of the result to graphs with arbitrary weights." Formally, on a one-vertex graph whose $2m$ directed edges are $[D]$ with reversal $\sigma$, and with $u_e = u\mathcal E_e$, their right-hand side becomes the right-hand side of Theorem 1 after the push-through identity $\mathcal E_i(1-u^2\mathcal E_{\bar i}\mathcal E_i)^{-1} = (1-u^2\mathcal E_i\mathcal E_{\bar i})^{-1}\mathcal E_i$ and the relabelling $i\leftrightarrow\bar i$ in $\mathcal D$; two further conventions differ and wash out of $\det(1-u\,\cdot)$: they compose a prime cycle as $u_{e_1}\cdots u_{e_k}$ (`section3.tex:315`), the reverse of our $\mathcal E_{i_\ell}\cdots\mathcal E_{i_1}$, and their edge operator weights the target edge where $T$ weights the source (reversal of words is a bijection of cyclically non-backtracking words because $\sigma$ is an involution, and $\det(1-XY) = \det(1-YX)$). But their graphs are hypergraphs with two-element hyperedges (`section2.tex:17-25`), so a bouquet is not one of their graphs and their corollary does not apply to it; Theorem 1 is the loop-admitting extension, not an instance. Their proof goes through a hypergraph theorem; ours is direct. Status of the shape-matching: `numerical` (reviewer's script `notes/reviews/scratch_wf_mo_conventions.py`).
- Matsuura & Ohta, arXiv:2204.06424, `main.tex:476` ("Suppose $X_{e}$ $(e\in E)$ are invertible matrices of size $K$ living on each edge.") and `main.tex:516-519` (eq. 2.11): the invertible-weight case, i.e. Corollary 3 for a general graph. Bouquet with $X_e = U_e\otimes U_e^\dagger$: the formula of `HANDOFF.md` item 1.
- Numerical check (`scripts/qihara_general.py`, `outputs/qihara_general.txt`): Theorem 1 at three values of $u$ (one complex) for (b) Gaussian Kraus operators with adjoint pairing, (b') canonical-form MPS tensors, (d) generic real superoperators with a generic involution, (c) $D = 2$ with the direct-sum check, (a) unitary case against Corollary 3, in both the $1-uM(u)$ and the displayed $1+\mathcal D-\mathcal A$ form; relative errors $\le 3\cdot10^{-15}$; the trace formula of Corollary 2 for $\ell\le4$ to $6\cdot10^{-12}$; and exact rational-arithmetic verification of Theorem 1 with sympy for $(N,D) = (1,4), (2,4), (2,6)$.

## 6. What this does and does not give

- It gives the transfer-matrix compression for **every** MPS transfer matrix $\Sigma = \sum_i\operatorname{Ad}(A_i)$, with the physical index doubled by the adjoints. The price of dropping unitarity is that the "degree" $(D-1)u^2$ becomes the operator $\mathcal D(u)$ and the adjacency $u\Sigma$ becomes the deformed channel $\mathcal A(u)$; both depend on $u$ through $(1-u^2\operatorname{Ad}(A_k^\dagger A_k))^{-1}$.
- It does not give a Ramanujan-type reading by itself: without $\mathcal E_{\bar i}\mathcal E_i = 1$ there is no quadratic relation $\mu\mu' = D-1$ pairing the eigenvalues of $T$ with those of $\Sigma$. What replaces it, and whether canonical form ($\sum_k A_k^\dagger A_k = 1$) buys anything, is open.
- Side A is unconditionally positive: $\operatorname{Tr}T^\ell = \sum_w|\operatorname{Tr}A_w|^2\ge0$ for any Kraus family. The primes are the primitive cyclically non-backtracking words in the $A_k$ and $A_k^\dagger$, with real nonnegative multiplicities $|\operatorname{Tr}A_w|^2$.
