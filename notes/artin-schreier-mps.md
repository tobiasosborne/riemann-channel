# A matrix-product formulation of the Weil conjectures: what works and where it stops

Computed 2026-09-11. Script `scripts/artin_schreier_mps.py`, output `outputs/artin_schreier_mps.txt`.

## 1. The question

The Weil conjectures for a curve $C$ over $\mathbb{F}_q$ say: the zeta function $Z(C,T) = \exp\sum_n N_n T^n/n$ is rational (Dwork), satisfies a functional equation (Grothendieck), and its numerator's roots $\alpha_i$ have $|\alpha_i| = \sqrt q$ (Weil for curves, Deligne in general). In the language of this repo: $N_n = \#C(\mathbb{F}_{q^n})$ is a ring norm, the $\alpha_i$ are the transfer spectrum, and RH is Ramanujan. Is there an honest matrix product state behind this, meaning a fixed local tensor whose $n$-site ring contraction is $N_n$?

## 2. The shift picture

$\mathbb{F}_{q^n}$ has a normal basis $\{\theta, \theta^q, \dots, \theta^{q^{n-1}}\}$, in which Frobenius $x \mapsto x^q$ is the cyclic shift of coordinates. So an element of $\mathbb{F}_{q^n}$ is a ring of $n$ sites with alphabet $\mathbb{F}_q$, and Frobenius is translation by one site. Points over $\mathbb{F}_{q^n}$ are ring configurations. This is the MPS setting, and the only question is whether the defining equation of the curve is a *local* constraint on the ring.

Take Artin–Schreier curves $y^q - y = g(x)$. By Hilbert 90 the affine point count is

$$
N_n = q^n + \sum_{a \in \mathbb{F}_q^\times} S_n(a g), \qquad S_n(g) = \sum_{x \in \mathbb{F}_{q^n}} \psi\big(\operatorname{Tr}\, g(x)\big),
$$

so everything reduces to the exponential sums $S_n$. Now write the exponent $m$ of a monomial $x^m$ in base $q$, $m = \sum_j m_j q^j$. Then $x^m = \prod_j (x^{q^j})^{m_j}$ is a product of *shifted copies* of $x$, of range equal to the number of base-$q$ digits. In a self-dual normal basis, which exists for $n$ odd, the trace form is the dot product, $\operatorname{Tr}(ab) = \sum_i a_i b_i$. Hence for the **quadratic** family

$$
g(x) = \sum_{j=0}^{J} a_j\, x^{1+q^j}, \qquad \operatorname{Tr}\, g(x) = \sum_{j=0}^{J} a_j \sum_{i} x_i\, x_{i+j},
$$

a translation-invariant quadratic spin model of range $J$ on the ring. Its partition function is $\operatorname{Tr} E^n$ for a transfer matrix $E$ of size $q^J$, with entries

$$
E_{(s_1,\dots,s_J)\to(s_2,\dots,s_J,x)} = \psi\Big(a_0 x^2 + \sum_{j=1}^{J} a_j\, s_{J+1-j}\, x\Big).
$$

This is an MPS with bond dimension $q^J$ and physical index $\mathbb{F}_q$.

## 3. Results

Brute-force $S_n$ in $\mathbb{F}_{q^n}$ (polynomial basis, sympy-verified irreducible) against $\operatorname{Tr}E^n$:

| $q$ | $a = (a_0,\dots,a_J)$ | $\dim E$ | $n$ tested | $S_n$ vs $\operatorname{Tr} E^n$ |
|---|---|---|---|---|
| 3 | (0, 1) | 3 | 2–7 | equal for odd $n$; $S_n = -\operatorname{Tr}E^n$ for even $n$ |
| 3 | (1, 1) | 3 | 3, 5, 7 | equal |
| 5 | (0, 1) | 5 | 2–5 | equal for odd, sign flip for even |
| 3 | (0, 1, 1) | 9 | 3, 5, 7 | equal |
| 3 | (0, 0, 1) | 9 | 3, 5, 7 | equal |

The even-$n$ sign is not a failure but the standard normalisation: with $\alpha_i = -\lambda_i(E)$,

$$
S_n = -\sum_i \alpha_i^{\,n} \quad\text{for all } n,
$$

which is exactly the shape $L(g,T) = \prod_i (1 - \alpha_i T)$ of the $L$-function of an exponential sum. So the transfer matrix is minus the Frobenius matrix, uniformly in $n$, and the self-dual basis was only needed to *see* the locality, not for the identity.

**RH is unitarity.** In every case tested, all eigenvalues of $E$ have modulus exactly $\sqrt q$, and

$$
E\,E^\dagger = q\,I \qquad(\text{checked to } 10^{-15} \text{ for eight } (q,a) \text{ up to } \dim E = 49).
$$

The reason is one line. In $(EE^\dagger)_{s' s''}$ the oldest spin $s_1$, which is summed over, appears only in the linear term $a_J s_1 (x' - x'')$, so the sum over $s_1$ is $q\,\delta_{x' x''}$ whenever $a_J \ne 0$. Therefore $E/\sqrt q$ is unitary and the Weil bound $|\alpha_i| = \sqrt q$ holds for the whole quadratic Artin–Schreier family, by the same mechanism as for a finite permutation in section 1 of `what-rh-has-become.md`: **the transfer matrix is a scaled unitary**. The degree of $L$ is $q^J = \deg g - 1$, matching Weil, and the $n = 4$ values saturate the bound $|S_n| \le (\deg g - 1)\, q^{n/2}$, the maximal-curve phenomenon.

## 4. Where it stops, and why that is the right place

Take a non-quadratic exponent, say $g(x) = x^3$ over $\mathbb{F}_q$ with $q \ge 5$. The base-$q$ expansion of $3$ has one digit, so $x^3$ is an on-site cubic. But $\operatorname{Tr}(x^3)$ in normal-basis coordinates is $\sum_{ijk} c_{ijk} x_i x_j x_k$ with the multiplication structure constants $c_{ijk}$ of the basis, which are non-local and depend on $n$. The self-dual normal basis makes the *bilinear* trace form local, not the *trilinear* one. So for cubic and higher $g$ there is no fixed local tensor in the shift basis, the ring model is not an MPS, and Weil's bound for these sums, cubic Gauss sums, Kloosterman-type sums, is exactly the case that needed algebraic geometry.

The dividing line is therefore sharp:

| $g$ | locality in the shift basis | transfer matrix | RH |
|---|---|---|---|
| quadratic, $\sum a_j x^{1+q^j}$ | local, range $J$ | $q^J \times q^J$, $= \sqrt q\,\cdot$ unitary | manifest |
| degree $\ge 3$ in any digit | non-local, $n$-dependent | none of fixed size in this basis | Weil / Deligne |

**The general transfer operator exists, but it is $p$-adic.** Dwork's 1960 proof of rationality is precisely a transfer-operator formulation for arbitrary $g$: the operator $\alpha = \psi_q \circ M_F$ on $p$-adic power series, where $M_F$ multiplies by a local weight (the splitting function $\prod_j \theta(a_j x^j)$) and $\psi_q$ decimates, $x^m \mapsto x^{m/q}$. Then $S_n^{\times} = (q^n - 1)\operatorname{Tr}(\alpha^n)$ and $L$ is a Fredholm determinant. This has the exact form of a coarse-graining tensor-network step, "local weight then decimate by $q$", with infinite but nuclear bond dimension. It delivers rationality and, through Dwork's duality, the functional equation. It cannot deliver RH: it sees the $p$-adic sizes of the eigenvalues (Newton polygon), and RH is about their complex absolute values. Deligne's proof lives in $\ell$-adic cohomology for that reason.

## 5. Answer

Yes, with a precise boundary. For the quadratic Artin–Schreier family, the Weil conjectures are literally statements about a finite MPS transfer matrix: rationality because it is finite, the functional equation because $E \mapsto q\,E^{-\dagger}$, and RH because $E/\sqrt q$ is unitary, which follows from the oldest spin coupling linearly to the newest. Beyond quadratic, the shift basis loses locality, the uniform formulation becomes Dwork's $p$-adic transfer operator, and RH is no longer a property of the transfer structure. That boundary is the same one seen for graphs and for the Riemann channel: the Ramanujan bound is either manifest because the transfer matrix is a scaled unitary, or it comes from arithmetic input outside the transfer structure.

## 6. Not established

- Any MPS with a fixed local tensor for a non-quadratic Artin–Schreier curve, or for any curve of genus $\ge 1$ that is not of this maximal type.
- Whether a *different* basis of $\mathbb{F}_{q^n}$, uniform in $n$, makes cubic traces local. No candidate was found or searched for.
- A rigorous write-up of the unitarity argument as a lemma with the exact hypothesis $a_J \ne 0$ and the even-$n$ sign convention.
