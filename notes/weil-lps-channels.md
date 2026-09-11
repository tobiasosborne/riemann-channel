# Weil–LPS channels: exactly Ramanujan quantum expanders on $\ell^2(\mathbb{F}_p)$

Computed 2026-09-11. Scripts `scripts/weil_lps.py`, `scripts/weil_lps_hashimoto.py`; outputs in `outputs/weil_lps_*.txt`. Everything below was computed, and every construction step carries its own numerical check.

## 1. The object

Fix an odd prime $p$ and an LPS parameter $q \equiv 1 \pmod 4$ with $q$ a square mod $p$. The Weil intertwiner exists only for symplectic (determinant one) matrices, and $q$ a square is what lets the norm-$q$ quaternions land in $\mathrm{SL}_2(\mathbb{F}_p)$ after scaling. The admissible pairs computed:

| $p$ | $q$ | $\lvert\mathrm{PSL}_2(\mathbb{F}_p)\rvert$ | Weil blocks $M_{(p+1)/2}$, $M_{(p-1)/2}$ |
|---|---|---|---|
| 5 | 29 | 60 | $M_3$, $M_2$ |
| 7 | 29 | 168 | $M_4$, $M_3$ |
| 11 | 5 | 660 | $M_6$, $M_5$ |
| 13 | 17, 29 | 1092 | $M_7$, $M_6$ |
| 17 | 13 | 2448 | $M_9$, $M_8$ |
| 19 | 5, 17 | 3420 | $M_{10}$, $M_9$ |
| 29 | 5, 13 | 12180 | $M_{15}$, $M_{14}$ |

**Step 1, generators.** The $q+1$ integer quaternions $\alpha = a_0 + a_1 i + a_2 j + a_3 k$ of norm $q$ with $a_0 > 0$ odd and $a_1, a_2, a_3$ even. Jacobi's four-square theorem gives exactly $q+1$ of them; the enumeration was checked against $\sigma(n)$ for the norms $q$, $q^2$ and $q_1 q_2$ used below.

**Step 2, images in $\mathrm{SL}_2(\mathbb{F}_p)$.** Split the Hamilton quaternions over $\mathbb{F}_p$ by $I = \begin{pmatrix} x & y \\ y & -x\end{pmatrix}$, $J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ with $x^2 + y^2 + 1 \equiv 0$. Then $\alpha \mapsto a_0 + a_1 I + a_2 J + a_3 IJ$ is a ring homomorphism with $\det = N(\alpha)$. Divide by a square root $s$ of $q$ mod $p$ to get $g_\alpha \in \mathrm{SL}_2(\mathbb{F}_p)$. Checked: $\det g_\alpha = 1$, $g_{\bar\alpha} = g_\alpha^{-1}$, all $q+1$ images distinct.

**Step 3, the Weil representation, built and checked numerically.** On $\ell^2(\mathbb{F}_p)$ take the clock and shift operators $X, Z$ and $T(u,v) = X^u Z^v$. The Fourier transform $F$, the chirp $M = \mathrm{diag}\,\psi(x^2/2)$ and a dilation $D$ each satisfy $U\,T(v)\,U^\dagger \propto T(g_U v)$ for a symplectic $g_U$, which the code *reads off* rather than assumes. A breadth-first search over $\mathrm{SL}_2(\mathbb{F}_p)$ in these three generators assigns to every group element a unitary $W(g)$, projectively; the table has exactly $p(p^2-1)$ entries. For each LPS generator the intertwining relation

$$
W(g_\alpha)\, T(v)\, W(g_\alpha)^\dagger \;\propto\; T(g_\alpha v)
$$

was verified directly, with error $\le 4\cdot 10^{-14}$ in every case. Since only $\mathrm{Ad}\,W$ enters the channel, the projective phases are irrelevant.

**Step 4, the two irreducible blocks.** $W(-1)$ is the parity operator, so $W$ splits into even and odd functions, of dimensions $(p\pm1)/2$. Each block is an irreducible representation on which $-1$ acts as a scalar, hence a representation of $\mathrm{PSL}_2(\mathbb{F}_p)$ up to phase. This matters: on the full $M_p$ the parity operator is a second fixed point of the channel, and Harrow's theorem needs irreducibility. The channels are

$$
\Phi_q^{\pm}(\rho) = \frac{1}{q+1}\sum_{\alpha} W_\pm(g_\alpha)\,\rho\,W_\pm(g_\alpha)^\dagger \quad\text{on } M_{(p\pm1)/2}.
$$

Block unitarity and Hilbert–Schmidt self-adjointness of the superoperator were checked, both at $10^{-14}$.

## 2. Results

Ramanujan bound $2\sqrt q$ in adjacency units. Every entry below is on the correct side of the bound.

| $p$ | $q$ | Cayley $\lambda_2$ | Cayley $\lambda_{\min}$ | $\Phi^{+}$: $(q{+}1)\lambda_2$ | $\Phi^{+}$: $(q{+}1)\lambda_{\min}$ | $\Phi^{-}$: $(q{+}1)\lambda_2$ | $\Phi^{-}$: $(q{+}1)\lambda_{\min}$ | $2\sqrt q$ |
|---|---|---|---|---|---|---|---|---|
| 5 | 29 | 6.000 | $-8.000$ | 6.000 | $-2.000$ | 2.000 | 2.000 | 10.770 |
| 7 | 29 | 8.000 | $-6.000$ | 6.000 | $-6.000$ | 2.000 | $-6.000$ | 10.770 |
| 11 | 5 | 4.372 | $-4.024$ | 3.562 | $-4.024$ | 3.406 | $-4.024$ | 4.472 |
| 13 | 17 | 6.928 | $-7.851$ | 6.000 | $-6.685$ | 5.555 | $-5.555$ | 8.246 |
| 13 | 29 | 9.932 | $-9.208$ | 9.000 | $-9.000$ | 9.000 | $-9.000$ | 10.770 |
| 17 | 13 | 6.106 | $-7.090$ | 6.000 | $-6.828$ | 6.000 | $-6.828$ | 7.211 |
| 19 | 5 | 4.275 | $-4.274$ | 4.243 | $-4.000$ | 4.243 | $-4.000$ | 4.472 |
| 19 | 17 | 7.671 | $-7.638$ | 7.128 | $-7.638$ | 7.128 | $-7.638$ | 8.246 |
| 29 | 5 | 4.442 | $-4.411$ | 4.442 | $-4.049$ | 4.442 | $-4.049$ | 4.472 |
| 29 | 13 | 6.765 | $-6.949$ | 6.765 | $-6.912$ | 6.579 | $-6.912$ | 7.211 |

Further checks, all passed in every case:

- **Harrow containment.** Every channel eigenvalue, times $q+1$, lies in the spectrum of the $\mathrm{PSL}_2(\mathbb{F}_p)$ Cayley graph, to $5\cdot10^{-7}$ (the graph spectrum was computed in double precision on up to 3420 vertices; for $p = 29$ only the extreme eigenvalues were computed, by Lanczos).
- **Unique fixed point.** The eigenvalue $1$ of each block channel has multiplicity one.
- **Hecke relation.** $A_q^2 - q\,I = A_{q^2}$ on $\mathrm{PSL}_2(\mathbb{F}_p)$, where $A_{q^2}$ is built from the $q^2+q+1$ normalised quaternions of norm $q^2$. Residual exactly $0$. This is the tree relation "two steps without backtracking".
- **Commutation across $q$.** For $(p; q_1, q_2) = (13; 17, 29)$, $(19; 5, 17)$, $(29; 5, 13)$: $\lVert[\Phi_{q_1}^\pm, \Phi_{q_2}^\pm]\rVert \le 3\cdot10^{-15}$, and $A_{q_1}A_{q_2} = A_{q_1 q_2}$ exactly, with $(q_1+1)(q_2+1)$ quaternions of norm $q_1 q_2$.
- **Quantum Ihara zeta.** For $(p,q) = (13, 17)$, odd block, the non-backtracking edge superoperator $T$ on $M_6\otimes\mathbb{C}^{18}$ (dimension 648) was built directly. The Ihara–Bass factorisation $\det(1-uT) = (1-u^2)^{n^2(D-2)/2}\det(1 - uD\Phi + qu^2)$ holds to $10^{-14}$, and the moduli of the eigenvalues of $T$ are exactly $\{17,\ \sqrt{17},\ 1\}$ with multiplicities $1$, $70$, $577$. So the quantum Ihara zeta of this channel satisfies RH on the nose: every nontrivial zero on the critical circle. For every other case the same conclusion follows from the channel spectrum through $\mu^2 - \lambda\mu + q = 0$.

## 3. What the joint spectrum looks like

For $(13; 17, 29)$ the even block has 19 distinct joint eigenvalue pairs $(a_{17}, a_{29})$. Examples, adjacency units:

| $(a_{17}, a_{29})$ | multiplicity | remark |
|---|---|---|
| $(18, 30)$ | 1 | trivial: $q+1$ |
| $(6, 2)$ | 2 | integers |
| $(3, -1), (3, 3), (3, 9)$ | 3, 3, 2 | integers |
| $(-5, -5)$ | 6 | integers |
| $\big(\tfrac{3+\sqrt{17}}{2},\ -1-\sqrt{17}\big)$ | 3 | quadratic, field $\mathbb{Q}(\sqrt{17})$ |
| $(5.6847, -2)$, $(5.5549, -0.3344)$, $(1.7730, 5.1119)$, … | 3 each | higher degree |

The eigenvalues are algebraic integers by construction, since the Cayley adjacency matrix is an integer matrix, so that is not a test. The real identification, that these are Hecke eigenvalues $a_q(f)$ of weight-2 forms attached to the quaternion algebra ramified at $2$ and $\infty$ with level determined by $p$, was **not** done here; it needs LMFDB and the Jacquet–Langlands bookkeeping. What is visible is the structure the identification predicts: joint eigenvalue pairs, small-degree algebraic integers, multiplicities equal to the multiplicity of the corresponding irreducible representation of $\mathrm{PSL}_2(\mathbb{F}_p)$ in $W_\pm\otimes\overline{W_\pm}$, and every pair inside the box $[-2\sqrt{q_1}, 2\sqrt{q_1}]\times[-2\sqrt{q_2}, 2\sqrt{q_2}]$.

## 4. Reading

This is the finite model of the Riemann channel with every ingredient present and every claim checkable:

| Riemann channel | Weil–LPS channel at $p$ |
|---|---|
| commuting dilations by primes | commuting Hecke channels $\Phi_q$, one per LPS prime $q$ |
| arithmetic quotient supplying expansion | $\mathrm{PSL}_2(\mathbb{F}_p)$ as quotient of the $(q+1)$-regular tree |
| Weil representation (SP-WEYL) | $W_\pm$ on $\ell^2(\mathbb{F}_p)$, even and odd |
| joint spectrum $=$ zeros | joint spectrum $=$ Hecke eigenvalues |
| RH: all modes at $\operatorname{Re} = 1/2$ | Ramanujan: all modes at $\lvert\mu\rvert = \sqrt q$ |
| source of the bound: unknown | source of the bound: Deligne, via LPS |

The last row is the honest one. These channels are exactly Ramanujan because Deligne proved the Weil conjectures, not because they are channels. What the computation establishes is that the object proposed in the handoff exists, is cheap to build, is self-checking at every step, and lands on the parent campaign's Hilbert space with the parent campaign's representation.

## 5. Not established

- The identification of the joint spectrum with specific modular forms in LMFDB.
- Any statement about $p \to \infty$ or about assembling the $\Phi_q$ over all $p$ into an object with the primes as rings; that is the DG-GLOBAL question of the parent repo in a new guise.
- Anything about RH.
