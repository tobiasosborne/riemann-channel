# Numerics lane for the ring-norm tensor campaign

Author: `claude:opus-5`.  Date: 2026-09-14.
Independent numerical check of the statements drafted in `notes/ring-norm-tensor/astra-brief.md`
(the prover lane is `codex:gpt-6-astra`).

## How to reproduce

```
cd /home/tobiasosborne/Projects/riemann-channel
python3 scripts/ring_norm_tensor.py > outputs/ring_norm_tensor.txt
echo $?          # 0 iff every check passed
```

One deterministic script, one captured output.  Every line of the output is labelled
`PASS`/`FAIL`; lines indented with six spaces are data, not checks.  The script exits nonzero
on any `FAIL` and ends with a check count.

Last run: **193 checks, 0 failures, 561.7 s wall time** (single core; the least-squares searches
of N3(b) are ~70 % of it).

Conventions are the brief's: graded bond $\mathbf{C}^{m|k}$, $P=\mathrm{diag}(1_m,-1_k)$, even
tensors block diagonal and odd tensors block off diagonal, $E=\sum_s A_s\otimes\bar A_s$,
$\Gamma=P\otimes\bar P$, $P$-closed ring norm $=\operatorname{str}_\Gamma E^n=\operatorname{Tr}(\Gamma E^n)$.
Helper code (`irreducible`, `polymulmod`, `polypow`, `transfer`) is imported from
`scripts/artin_schreier_mps.py`; the explicit Jordan–Wigner lattice model
(`creation_ops`, `mps_state`, `translation_op`) from `scripts/cmps_parity_supertrace.py`;
the case list of N4(a) is read out of `scripts/artin_schreier_super.py` by regex (that file
runs its whole campaign on import, so it must not be imported).

Finite fields are rebuilt from scratch here with log/antilog tables (elements are integers,
base-$p$ digits low first), which is what makes the brute-force counts and the $q=3,\,n=7$
cut-rank computation cheap.

---

## N1 Frobenius as a toral endomorphism (Tier A)

Five curves $y^2=x^3+Ax+B$, all ordinary; $M=\begin{pmatrix}0&-q\\1&a\end{pmatrix}$ is
multiplication by $\pi$ in the $\mathbf{Z}$-basis $\{1,\pi\}$.

| curve | $a$ | $N_n$ (brute force) | $\operatorname{disc}=a^2-4q$ | $\pi$ | $\operatorname{cond}(V)$ |
|---|---|---|---|---|---|
| $y^2=x^3+x+1/\mathbf{F}_5$ | $-3$ | 9, 27, 108, 675, 3069 | $-11$ | $-1.5+1.65831240i$ | 3.316625 |
| $y^2=x^3+2x+1/\mathbf{F}_5$ | $-1$ | 7, 35, 112, 595, 3227 | $-19$ | $-0.5+2.17944947i$ | 2.322400 |
| $y^2=x^3+x+1/\mathbf{F}_7$ | $3$ | 5, 55, 380, 2475 | $-19$ | $1.5+2.17944947i$ | 3.374293 |
| $y^2=x^3+2x+3/\mathbf{F}_7$ | $2$ | 6, 60, 378, 2400 | $-24$ | $1+2.44948974i$ | 2.923988 |
| $y^2=x^3+x+1/\mathbf{F}_{11}$ | $-2$ | 14, 140, 1274, 14560 | $-40$ | $-1+3.16227766i$ | 3.509818 |

Checked for every curve:

* $N_n=|\det(M^n-1)|$ and $N_n=1-\operatorname{Tr}M^n+\det M^n$ (Lefschetz) for all brute-forced $n$;
* $\det(M^n-1)\neq0$ for $n\le 12$, and **directly** that the permutation $k\mapsto M^{\mathsf T}k$
  of the box $[-50,50]^2\subset\mathbf{Z}^2$ has no periodic point except $0$ for periods $\le12$
  (0 found in every case) — this is T1(d)'s "exactly one finite orbit";
* the torus fixed points, enumerated as the finite group $\mathbf{Z}^2/(M^n-1)\mathbf{Z}^2$ via a
  $2\times2$ column Hermite form and exact `Fraction` arithmetic, number exactly $|\det(M^n-1)|$,
  each representative really satisfying $(M^n-1)x\in\mathbf{Z}^2$; and $\det(1-M^n)>0$ throughout,
  so every fixed point has index $+1$.  Enumerated up to $n=6$ for $q=5$ (15552 fixed points at
  $n=6$) and $n=4$ for $q=7,11$; the cut-off is $|\det|\le 20000$.
* $\exp\big(\sum_n N_nu^n/n\big)=(1-au+qu^2)/\big((1-u)(1-qu)\big)$ as exact rational power series
  to order $u^8$;
* $|\pi|^2=q$; the eigenvectors of $M$ for $\pi,\bar\pi$ diagonalise $M$; $M/\sqrt q$ is unitary in
  that (Hodge) basis; equivalently $M^\dagger G M=qG$ for $G=(VV^\dagger)^{-1}$.

The "gauge needed" is the condition number of $V=[v_\pi,v_{\bar\pi}]$, tabulated above: it is
$O(1)$ but never $1$ — the integral basis is never the Hodge-orthonormal one, which is exactly
T1(f)'s point that the unitary gauge is a complex, not an integral, change of basis.

**Verdict: T1(a), (b), (d), (e), (f) all consistent.**

## N2 Lenstra's structure theorem

For all five curves $\operatorname{disc}(\mathbf{Z}[\pi])$ is already a fundamental discriminant
(conductor $f=1$), so $\mathbf{Z}[\pi]=O_K=\operatorname{End}(E)$ and
$O/(\pi^n-1)\cong\mathbf{Z}^2/(M^n-1)\mathbf{Z}^2$.  The first three curves were done in full:
points enumerated by brute force in $\mathbf{F}_{q^n}$, the group law implemented in the extension
field, the exponent taken as the lcm of the orders of **all** points, and $(d_1,d_2)=(N/e,e)$
compared with the Smith normal form of $M^n-1$.

| curve | $n=1$ | $n=2$ | $n=3$ |
|---|---|---|---|
| $x^3+x+1/\mathbf{F}_5$ | $\mathbf{Z}/9$ | $\mathbf{Z}/3\times\mathbf{Z}/9$ | $\mathbf{Z}/2\times\mathbf{Z}/54$ |
| $x^3+2x+1/\mathbf{F}_5$ | $\mathbf{Z}/7$ | $\mathbf{Z}/35$ | $\mathbf{Z}/4\times\mathbf{Z}/28$ |
| $x^3+x+1/\mathbf{F}_7$ | $\mathbf{Z}/5$ | $\mathbf{Z}/55$ | $\mathbf{Z}/2\times\mathbf{Z}/190$ |

Every $(curve,n)$ agrees, and the same invariant factors come out of the matrix of $\pi$ in the
$\omega=(d_K+\sqrt{d_K})/2$ basis of $O_K$ (a cross-check that catches sign errors: the correct
relation is $\omega^2=d_K\omega-\tfrac{d_K(d_K-1)}4$, so the matrix is
$\begin{pmatrix}u&-d_K(d_K-1)/4\\1&u+d_K\end{pmatrix}$ with $u=(a-d_K)/2$; its trace is $a$ and its
determinant $q$).

**Verdict: H-LENSTRA consistent.**

## N3 Genus 2 on $\mathbf{C}^{1|2}$

Curve $y^2=x^5+x^3+x^2-2$ over $\mathbf{F}_5$.  Brute force reproduces $N_n=3,31,117,619$,
$L(u)=1-3u+7u^2-15u^3+25u^4$, $\alpha=1.89564392\pm1.18597391i$, $-0.39564392\pm2.20078756i$,
$|\alpha_j|^2=5$.

### (a) Existence and the Jordan–Wigner norm

A free search on $\mathbf{C}^{1|2}$ with two even and one odd species reaches
$\operatorname{str}E^n=N_n$ at cost $1.07\cdot10^{-26}$ (first restart, 5 s), and
$\operatorname{str}E^n=N_n$ holds through $n=20$ with $\max|{\rm dev}|/q^{n/2}=6.4\cdot10^{-9}$.
Even spectrum $\{1,5,0,0,0\}$, odd spectrum exactly the four $\alpha_j$ (deviation $2\cdot10^{-14}$):
no even/odd cancellation.  The explicit Jordan–Wigner Fock vector gives
$\|\Psi_P\|^2=31,117,619,3318$ for $n=2,3,4,5$ and is invariant under the **periodic** translation
($\|T\Psi-\Psi\|\sim10^{-15}$).

Numerical note worth recording: the three nilpotent even modes show up as eigenvalues of modulus
$\sim6\cdot10^{-5}$, the **cube root** of the least-squares residual — the signature of a genuine
$3\times3$ nilpotent Jordan block, not of sloppy convergence.  A naive $10^{-5}$ threshold
misreads this as five nonzero eigenvalues.

### (c) Block formulas of T4(a): confirmed, with index order fixed

With the bond-pair orders
`even = [(0,0),(1,1),(1,2),(2,1),(2,2)]`, `odd = [(0,1),(0,2),(1,0),(2,0)]`, we verified to
$4\cdot10^{-16}$ that

$$E_{\rm even}=\begin{pmatrix}t&u\\v&W\end{pmatrix},\qquad
E_{\rm odd}=\begin{pmatrix}M&N\\\bar N&\bar M\end{pmatrix},$$

$t=\sum_s|a_s|^2$, $u=\sum_f c_f\otimes\bar c_f$, $v=\sum_f d_f\otimes\bar d_f$,
$W=\sum_s B_s\otimes\bar B_s$, $M=\sum_s a_s\bar B_s$, and — a detail the brief leaves implicit —
$N_{ji}=\sum_f \overline{(d_f)_j}\,(c_f)_i$, so **$\operatorname{rank}N\le$ number of odd species**.
Equivalently, in map language $E$ acts on $X=\mathrm{diag}(x,Y)$ by
$x\mapsto tx+cYc^\dagger$, $Y\mapsto x\,dd^\dagger+\sum_sB_sYB_s^\dagger$: the $u,v$ blocks come
from the **odd** species only, and the $M$ block from the **even** ones only.

Two identities are forced and hold to $10^{-10}$ on every solution found:

* $t+\operatorname{Tr}W=1+q$ (here $6$), where $\operatorname{Tr}W=\sum_s|\operatorname{Tr}B_s|^2$;
* $2\,\mathrm{Re}\operatorname{Tr}M=e_1=3$.

Everything else moves.  Three independent restarts converging to cost $<10^{-25}$ give
$t=3.5380,\,3.3681,\,4.0115$ with completely different $\operatorname{spec}M$ and
$c\!\cdot\!d$.  **The solution set is a positive-dimensional family that is not a single gauge
orbit**, so no individual entry — and in particular no "$|c_j||d_j|$ tied to $q$" pattern — can be
read off.  We also checked that $B_1,B_2$ are linearly independent in the solutions found, so no
unitary mixing of the two even species produces a vacuum species: the generic solution has none.

### (b) Structured ansaetze — the main result of this lane

Gauge $G=1\oplus g$, $g\in GL(2,\mathbf{C})$, acts by $B_s\mapsto gB_sg^{-1}$, $c\mapsto cg^{-1}$,
$d\mapsto gd$, plus a unitary mixing of the physical index.  So "$B_1=0$" (a vacuum species) and
"all $B_s$ diagonal" are genuine restrictions, not gauge choices.  Each ansatz was fitted to
$\operatorname{str}E^n=N_n$, $n\le10$, with 5–10 random restarts and `least_squares` bounds
$\pm4$.  "Solved" means cost $<10^{-20}$.

| ansatz | params (real) | best cost | verdict |
|---|---|---|---|
| S1 vacuum, $a_2=0$, $B_2$ free (**the brief's suggestion**) | 16 | $7.2\cdot10^{0}$ | fails |
| S2 vacuum, 2 even + 1 odd, all free | 18 | $5.6\cdot10^{-1}$ | fails |
| S3 vacuum, 2 even + 1 odd, $B_2$ diagonal | 14 | $1.7\cdot10^{-1}$ | fails |
| S4 vacuum, $B_2=z\,\mathrm{diag}(\pi_1,\pi_2)/\sqrt q$ | 12 | $5.7\cdot10^{-1}$ | fails |
| S5 vacuum, $B_2=z\,\mathrm{diag}(\bar\pi_1,\bar\pi_2)/\sqrt q$ | 12 | $5.7\cdot10^{-1}$ | fails |
| S6 vacuum, $M=\mathrm{diag}(\bar\pi_1,\bar\pi_2)$ exactly | 10 | $6.0\cdot10^{-1}$ | fails |
| S7 vacuum, 3 even + 1 odd | 28 | $2.1\cdot10^{-2}$ | fails |
| S8 vacuum, 2 even + 2 odd | 26 | $6.3\cdot10^{-2}$ | fails |
| **S9 vacuum, 3 even + 2 odd** | 36 | $1.8\cdot10^{-25}$ | **SOLVED** |
| D21 CM-diagonal, 2 even + 1 odd | 20 | $4.2\cdot10^{-2}$ | fails |
| D31 CM-diagonal, 3 even + 1 odd | 26 | $4.2\cdot10^{-2}$ | fails |
| **D22 CM-diagonal, 2 even + 2 odd** | 28 | $5.1\cdot10^{-26}$ | **SOLVED** |
| B3 purely bosonic, 3 even species | 30 | $4.1\cdot10^{-2}$ | fails |
| B4 purely bosonic, 4 even species | 40 | $4.1\cdot10^{-2}$ | fails |

**S1 is refuted, with a proof, not just a failed search.**  $a_1=1,B_1=0,a_2=0$ force
$M=\sum_sa_s\bar B_s=0$ identically; with $M=0$ the odd block is
$\begin{pmatrix}0&N\\\bar N&0\end{pmatrix}$, whose spectrum is symmetric under
$\lambda\mapsto-\lambda$ (verified to $10^{-14}$).  The Frobenius multiset of this curve is not:
$\min_{j,k}|\alpha_j+\alpha_k|=0.791288>0$.  So **no** tensor of that shape can work, for any
curve whose $\{\alpha_j\}$ is not closed under negation — i.e. for every ordinary curve with
$e_1\neq0$.  This is an unconditional refutation of the ansatz suggested in T4(a), not a numerical
near-miss.

**The vacuum species itself is the obstruction with one fermion.**  Every ansatz with
$a_1=1,B_1=0$ and a *single* odd species fails, with 2 or 3 even species and for each structured
$B_2$ tried.  They all stall in the same place: $t=\sum_s|a_s|^2\to q=5$ and
$\operatorname{spec}M\to\{\bar\pi_1,\bar\pi_2\}$, i.e. the optimiser is dragged to the
Hodge-natural $M$ and then cannot repair the even sector, because $t+\operatorname{Tr}W$ must be
$1+q=6$ while $t$ alone has already reached $5$.  A vacuum species becomes possible once there are
**two** odd species (S9, 3 even + 2 odd, solved).

**New positive result: the CM-diagonal ansatz.**  Take every even tensor simultaneously diagonal,
$A_s=\mathrm{diag}(a_s,b_{s,1},b_{s,2})$ — the direct generalisation of the genus-1 tensor
$A_s=\mathrm{diag}(a_s,\alpha a_s)$ — with the odd species unrestricted.  With one odd species this
fails (D21, D31, again stalling at $t\to5$); with **two** odd species it solves exactly (D22,
cost $5\cdot10^{-26}$, even spectrum $\{1,5,0,0,0\}$, odd spectrum exactly the four $\alpha_j$).
In that ansatz the whole even sector is encoded in the $3\times3$ Gram matrix of $(a,b_1,b_2)$ in
the species index, and $M=\mathrm{diag}(\langle b_1,a\rangle,\langle b_2,a\rangle)$ is diagonal.
The solution printed in `outputs/ring_norm_tensor.txt` has

```
Gram(a,b_1,b_2) = [[2.175182,          1.008989+0.101111i, 0.491011+1.066166i],
                   [1.008989-0.101111i, 1.802520,          0.626051+0.226228i],
                   [0.491011-1.066166i, 0.626051-0.226228i, 0.770196]]
m_1 = 1.00898868 - 0.10111084i,  m_2 = 0.49101132 - 1.06616619i,
|m_1|^2 = 1.028282,  |m_2|^2 = 1.377802      (q = 5)
```

so $M$ is **not** $\mathrm{diag}(\bar\pi_1,\bar\pi_2)$ and $|m_i|^2\neq q$: the four Frobenius
eigenvalues are produced by the interplay of $M$ (rank 2) and $N$ (rank 2), not by $M$ alone.
$t+\operatorname{Tr}W=6.00000000$ and $2\mathrm{Re}\operatorname{Tr}M=3.000000$ exactly, as forced.
Attempts to recognise the entries (moduli, phases relative to $\pi_j$, ratios to $\sqrt q$, the
diagonal-torus invariants $u_{ii}v_{ii}=\sum_f|c_i|^2\sum_f|d_i|^2$, $|N_{ii}|$, $N_{12}N_{21}$)
produced **no** stable pattern tied to $q$: the values differ between the two solved ansaetze
($u_{11}v_{11}=10.14$, $u_{22}v_{22}=5.98$ for D22; $4.89$ and $6.01$ for S9), and $t$ itself
differs between independent restarts of the same free ansatz ($3.538,\,3.368,\,4.012$).

**Honest summary of (b): the campaign's hoped-for closed form is not there.**  There is a
positive-dimensional real-algebraic variety of solutions; the only functions of the tensor that
the counting equations pin down are the two trace identities above and the two spectra.  Any
closed-form tensor will have to be singled out by an extra principle (Hodge metric / Rosati
positivity / a normalisation of the physical index), not by the counts alone.

### (b') T3(a) as drafted is FALSE

The drafted chain is
$\sum_{\rm odd}|\mu|^2\le 2\|M\|_{\rm HS}^2\le 2(\sum_s\|a_s\|_{\rm HS}\|B_s\|_{\rm HS})^2\le
2\operatorname{Tr}(E_{++})\operatorname{Tr}(E_{--})$.
The last step is wrong for $k>1$, because $\operatorname{Tr}(E_{--})=\sum_s|\operatorname{Tr}B_s|^2$
is the **superoperator** trace, while what the Cauchy–Schwarz step produces is
$\sum_s\|B_s\|_{\rm HS}^2$, and $\|B\|_{\rm HS}^2\ge|\operatorname{Tr}B|^2/k$ points the wrong way.

Explicit counterexample on $\mathbf{C}^{1|2}$: one even species with $a=1$, $B=\mathrm{diag}(1,-1)$.
Then $\operatorname{Tr}B=0$ so the drafted right-hand side is $0$, while
$\sum_{\rm odd}|\mu|^2=4$.  On 400 random purely bosonic $\mathbf{C}^{1|2}$ instances the drafted
bound fails **173 times**.  The repaired bound

$$\sum_{\rm odd}|\mu|^2\;\le\;2\Big(\sum_s\|a_s\|_{\rm HS}^2\Big)\Big(\sum_s\|B_s\|_{\rm HS}^2\Big)$$

held on all 400.  Note that the repaired right-hand side is $2\operatorname{Tr}\Phi_{++}(1)\cdot
\operatorname{Tr}\Phi_{--}(1)$, not a superoperator trace, so **T3(b)'s corollary does not follow
from it in the stated way** for $k>1$; for $\mathbf{C}^{1|1}$ the two coincide and the corollary is
safe.  The conclusion of T3(b) (no purely bosonic genus-2 realisation) is still supported
numerically — B3 and B4 both fail, with 3 and 4 even species on $\mathbf{C}^{1|2}$ — but the proof
needs a different argument.

### (d) Jacobian versus curve

With $\mathrm{Frob}=\mathrm{diag}(\pi_1,\bar\pi_1,\pi_2,\bar\pi_2)$ on $\mathbf{C}^4$:
$\operatorname{str}\Lambda^\ast(\mathrm{Frob}^n)=\prod_j|1-\pi_j^n|^2$ for $n\le6$
(15, 765, 14715, 386325, 10381200, 249904845 — these are $\#\mathrm{Jac}(\mathbf{F}_{5^n})$), and
the supertrace restricted to $\mathrm{span}\{1\}\oplus\Lambda^1\oplus\mathbf{C}\omega$ with
$\omega=e_1\wedge e_1'+e_2\wedge e_2'$ (each $\pi_j$ paired with its conjugate, so
$\mathrm{Frob}\,\omega=q\omega$, verified: $\pi_j\bar\pi_j=q$) equals
$N_n(C)=3,31,117,619,3318,15991$.  **T4(b) consistent.**

## N4 The dichotomy

### (a) Supersingularity of the quadratic Artin–Schreier family

All 11 cases of `scripts/artin_schreier_super.py` ($q\in\{3,5,7\}$, $J\le2$).  In every case
$E_gE_g^\dagger=q$, and every eigenvalue of $E_g/\sqrt q$ is a root of unity of order $\le36$:

| $q$ | $a$ | orders of $\lambda/\sqrt q$ | lcm |
|---|---|---|---|
| 3 | $[0,1]$ | 1, 2, 4 | 4 |
| 3 | $[1,1]$ | 4, 12 | 12 |
| 3 | $[0,1,1]$ | 4, 12, 36 | 36 |
| 3 | $[0,0,1]$ | 1, 2, 4, 8 | 8 |
| 3 | $[1,0,1]$ | 3, 4, 6, 12 | 12 |
| 3 | $[2,1]$ | 4, 12 | 12 |
| 5 | $[0,1]$ | 1, 2, 4 | 4 |
| 5 | $[1,2]$ | 1, 3 | 3 |
| 5 | $[0,1,1]$ | 2, 3, 5, 6, 10, 15, 30 | 30 |
| 7 | $[0,1]$ | 1, 2, 4 | 4 |
| 7 | $[1,1]$ | 4, 28 | 28 |

**T0(a) consistent.**

### (b) Cut rank: the statement is true but basis dependent

For a quadratic form $Q$ over $\mathbf{F}_2$ the amplitude $(-1)^{Q(x)}$ has cut rank
$2^{\operatorname{rank}_{\mathbf{F}_2}C_{AB}}$ across a bipartition, $C_{AB}$ the off-diagonal
block of the Gram matrix.  In a **self-dual** normal basis (which exists for
$\mathbf{F}_{2^n}/\mathbf{F}_2$ iff $n$ is odd) $\operatorname{tr}(x^{1+2})=\sum_ix_ix_{i+1}$ is
nearest-neighbour, so $C_{AB}$ has two nonzero entries on a ring cut into two arcs and the cut rank
is $\le4$.  Self-duality does **not** make the cubic $\operatorname{tr}(x^{1+2+4})$ local.

Cut rank across the first $\lfloor n/2\rfloor$ coordinates:

| $n$ | quad. (plain NB) | cubic (plain NB) | quad. (self-dual NB) | cubic (self-dual NB) |
|---|---|---|---|---|
| 2 | 1 | 1 | — | — |
| 3 | 2 | 2 | 2 | 2 |
| 4 | 4 | 3 | — | — |
| 5 | 2 | 4 | 4 | 4 |
| 6 | 4 | 8 | — | — |
| 7 | 8 | 8 | 4 | 8 |
| 8 | 4 | 15 | — | — |
| 9 | 8 | 16 | 4 | 16 |
| 10 | 16 | 32 | — | — |

$q=3$, $\psi=e^{2\pi ic/3}$, quadratic $\operatorname{tr}(x^{1+3})$ vs cubic
$\operatorname{tr}(x^{1+3+9})$:

| $n$ | quad. (plain) | cubic (plain) | quad. (self-dual) | cubic (self-dual) |
|---|---|---|---|---|
| 2 | 1 | 3 | — | — |
| 3 | 3 | 1 | 3 | 1 |
| 4 | 9 | 7 | — | — |
| 5 | 1 | 9 | 9 | 9 |
| 6 | 9 | 27 | — | — |
| 7 | 27 | 27 | 9 | 27 |

**Plain statement.** In the self-dual normal basis the quadratic (Artin–Schreier, supersingular)
amplitude has **bounded** cut rank — $\le4$ for $q=2$, $\le9$ for $q=3$, i.e. $\le q^{2J}$ as the
transfer-matrix picture predicts — while the cubic amplitude's cut rank **grows**, roughly
doubling (tripling for $q=3$) with each two extra sites: $2,4,8,16$ for $q=2$ at $n=3,5,7,9$ and
$1,9,27$ for $q=3$ at $n=3,5,7$.  So no fixed finite lattice tensor reproduces the cubic amplitude.

**Caveat that should go into T0(b).** In a *plain* (non-self-dual) normal basis even the quadratic
amplitude has growing cut rank (16 at $n=10$ for $q=2$, 27 at $n=7$ for $q=3$), because
$\operatorname{tr}(x\,x^{q^j})=\sum_{i,k}x_ix_k\,t_{k-i+j}$ is a circulant, and only self-duality
makes $t$ supported at one offset.  The bounded-bond-dimension claim is therefore a statement about
the *self-dual normal basis*, which is exactly the basis in which the transfer matrix of
`artin_schreier_mps.transfer` is derived, and it must be stated with that hypothesis (and with the
hypothesis $n$ odd, since self-dual normal bases of $\mathbf{F}_{q^n}/\mathbf{F}_q$ exist only for
$n$ odd, or $n\equiv2\bmod4$ with $q$ even).

---

## Verdict table (N5)

| drafted statement | verdict |
|---|---|
| T1(a) $M$, $N_n=|\det(M^n-1)|=1-\operatorname{Tr}M^n+\det M^n$, fixed points nondegenerate of index $+1$, $\#\mathrm{Fix}=|\mathbf{Z}^2/(M^n-1)\mathbf{Z}^2|$ | consistent |
| T1(a) $N_n=N_{K/\mathbf{Q}}(1-\pi^n)=|O/(\pi^n-1)|$ | consistent |
| T1(b) dynamical zeta $=Z(E,u)$ to order $u^8$ | consistent |
| T1(d) $k\mapsto M^{\mathsf T}k$ has exactly one finite orbit | consistent (box $[-50,50]^2$, periods $\le12$) |
| T1(e) $|\pi|^2=q$, $M/\sqrt q$ unitary in the Hodge basis, $M^\dagger GM=qG$ | consistent |
| T1(f) gauge $=$ change of $\mathbf{Z}$-basis; $\operatorname{cond}(V)$ reported | consistent |
| H-LENSTRA $E(\mathbf{F}_{q^n})\cong O/(\pi^n-1)$, $n=1,2,3$ | consistent |
| T3(a) $\sum_{\rm odd}|\mu|^2\le2\operatorname{Tr}(E_{++})\operatorname{Tr}(E_{--})$ | **REFUTED** |
| T3(a) repaired with $\sum_s\|a_s\|_{\rm HS}^2,\ \sum_s\|B_s\|_{\rm HS}^2$ | consistent |
| T3(b) purely bosonic cannot reach genus 2 | consistent (numerically); the drafted proof needs repair |
| T3(c) minimal bond $\mathbf{C}^{1|g}$, even spectrum $\{1,q\}$ + $g^2-1$ nilpotents | consistent |
| T4(a) block formulas $E_{\rm even}$, $E_{\rm odd}$ | consistent ($\operatorname{rank}N\le\#$odd species) |
| T4(a) existence, 2 even + 1 odd, JW Fock norm | consistent |
| T4(a) suggested ansatz $a_1=1,B_1=0,a_2=0$ | **REFUTED** (it forces $M=0$; unconditional) |
| T4(a) vacuum species with ONE odd species | **REFUTED** (numerically, 2 and 3 even species) |
| T4(a) vacuum species with TWO odd species (3 even + 2 odd) | consistent (SOLVED) |
| T4(a) NEW: CM-diagonal $A_s=\mathrm{diag}(a_s,b_{s,1},b_{s,2})$, 2 even + 2 odd | consistent (SOLVED) |
| T4(a) CM-diagonal with one odd species | **REFUTED** (numerically) |
| T4(a) entries recognisable in terms of $\pi_j,q$ | **not supported**: positive-dimensional family; only $t+\operatorname{Tr}W=1+q$ and $2\mathrm{Re}\operatorname{Tr}M=e_1$ are pinned |
| T4(b) $\operatorname{str}\Lambda^\ast(\mathrm{Frob}^n)=\#\mathrm{Jac}$; curve subspace gives $N_n(C)$ | consistent |
| T0(a) $E_g/\sqrt q$ has finite order; supersingularity | consistent (11/11 cases) |
| T0(b) bounded cut rank for quadratic, growing for cubic | consistent **only in a self-dual normal basis** |
| T2 finite-state ring model | not tested |
| T5 Phantasm assessment | not tested |

## Surprises, for the prover lane

1. **T3(a) is false as drafted** and the counterexample is one line: $a=1$, $B=\mathrm{diag}(1,-1)$.
   The genus-$\le1$ corollary T3(b) survives numerically but needs a different proof for $k>1$.
2. **The suggested genus-2 ansatz is dead on arrival**, because $a_2=0$ makes $M=0$ and forces the
   odd spectrum to be $\pm$-symmetric.  More: a vacuum species with a *single* fermionic species is
   impossible for this curve no matter how many bosonic species are added.
3. **One fermionic species is enough only if there is no vacuum species.**  The two structured
   families that do work both need two fermionic species: 3 even + 2 odd with a vacuum, or 2 even +
   2 odd with all even tensors diagonal.  The species count is not a free parameter of the
   construction — it interacts with the structure imposed.
4. **The CM-diagonal ansatz works** and is the natural lift of the genus-1 tensor
   $\mathrm{diag}(a_s,\alpha a_s)$: all bosonic data reduce to the $3\times3$ Gram matrix of
   $(a,b_1,b_2)$ in the physical index, and $M$ is diagonal.  This is the most promising shape for a
   closed form.
5. **But $M$ is not the Hodge Frobenius in any solution found.**  $\mathrm{spec}\,M$ moves from
   restart to restart and $|m_i|^2\neq q$; the four $\alpha_j$ come out of $M$ and $N$ together.
   The "$M=\mathrm{diag}(\bar\pi_1,\bar\pi_2)$, $N=0$" picture from the cohomology is a saddle that
   every failing search is attracted to ($t\to q$, $\operatorname{spec}M\to\{\bar\pi_j\}$) and no
   solution reaches.  Whatever makes RH manifest for this tensor, it is not the odd block being
   $\sqrt q$ times a unitary by construction.
6. **The cut-rank dichotomy is basis dependent** and the self-dual normal basis hypothesis is not
   optional.
