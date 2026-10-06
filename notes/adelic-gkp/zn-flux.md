# A $\mathbb Z_N$ flux on a graph: the finite shadow of a Dirichlet family

Author: `claude:opus-5.5`, 2026-10-06, lane D of an orchestrated session

Status: **a record, not a round; nothing registered in db/claims.tsv; no REFUTE review; no shard.** Each statement carries one label:
*standard*, *proved here*, *checked*, *sketched*, *heuristic*, *open* or *negative finding*. `refs/src/` is absent in this container, so
Godsil–Gutman, Heilmann–Lieb, Deligne, Stark–Terras and Davenport–Heilbronn are quoted from memory. Checks: `checks/check_zn_flux.py`,
output `checks/output_zn_flux.txt`, 87 of 87 pass (about 75 s).

Continues `graph-super.md` §§3, 6 and the U(1) section of `gauge-groups.md`, and fills the `data-ladder.md` §6 "Next" item on $\mathbb Z_N$ fluxes.

**A correction to the brief.** The brief gave $q=3,3,2$ for $K_4$, the cube and Petersen. All three are 3-regular, so $q=2$ for each, as
`graph-super.md` uses ($2\sqrt q=2.828$). Everything below uses $q=2$.

**Verdict.**

- **There is a lattice state, over $\mathbb Z[\zeta_N]$.** The step $M_\rho=\bigl(\begin{smallmatrix}0&-1\\q&A_\rho\end{smallmatrix}\bigr)$ satisfies
  $M_\rho^\dagger\Omega M_\rho=q\Omega$. Restricting scalars gives an integral lattice $L\cong\mathbb Z^{2n\varphi(N)}$, an integral step of norm $q$, and the
  alternating integral form $\Omega_{\mathbb Z}(x,y)=\mathrm{Tr}_{\mathbb Q(\zeta_N)/\mathbb Q}(x^\dagger\Omega y)$ (*proved here*, *checked*).
- **RH is again an invariant vacuum, but for the whole Galois orbit.** The Weil form on $L$ is positive definite exactly when every Galois-conjugate
  flux $\rho^\sigma$ is Ramanujan. The vacuum is explicit, $J=(M-V)(4q-A^2)^{-1/2}$, and it commutes with $\zeta_N$ (*proved here*, *checked*).
- **No lock of order $N$.** The $\mathbb Z_N$ structure supplies an automorphism of order $N$ that commutes with $M$, which is complex
  multiplication, not a relation between eigenvalues. The one forced relation is that every eigenvalue appears twice, because $\rho$ and $\bar\rho$
  have the same spectrum (*proved here*; *negative finding* against "a lock of order $N$ by construction").
- **RH on average over the $N$-torsion holds for every $N\ge2$, and the average is the matching polynomial.** It is the same polynomial as for
  $N=2$ and for the full U(1) torus, with no new combinatorics (*proved here*, *checked*). The selection "homology class in $N\cdot H_1$" that the
  brief expected is real, but it acts on the walk counts $\mathrm{Tr}\,B_\chi^k$, not on the determinant (*checked*).

## 1. Setting

$Y$ is connected and $(q+1)$-regular, with $n$ vertices and $g=|E|-|V|+1$. A $\mathbb Z_N$ flux is a 1-cochain $\varphi$ on directed edges with
$\varphi(\bar e)=-\varphi(e)\in\mathbb Z/N$, taken modulo coboundaries. The classes form $H^1(Y,\mathbb Z/N)=\mathrm{Hom}(H_1(Y,\mathbb Z),\mathbb Z/N)\cong(\mathbb Z/N)^g$, the
$N$-torsion of the Brillouin torus (*standard*). The check fixes a spanning tree, puts $\varphi=0$ on it and lets $\varphi$ run over all values on the $g$
cotree edges. The twisted adjacency is $A_\rho[u,v]=\sum_{e:u\to v}\zeta_N^{\varphi(e)}$, which is Hermitian.

- **Ihara–Bass** (*standard*, Stark–Terras, from memory; elementary per `gauge-groups.md`):
  $\det(1-uB_\rho)=(1-u^2)^{|E|-|V|}\det(1-A_\rho u+qu^2)$, with $B_\rho$ the twisted Hashimoto operator on the $2|E|$ directed edges. Check I1 tests it
  on 3 random fluxes for each $(Y,N)$ with $N\in\{3,4,5,6\}$, at 3 complex values of $u$. The largest relative error is $2\times10^{-15}$.
- **$L(u,\bar\rho)=L(u,\rho)$** (*proved here*, elementary). Since $A_{\bar\rho}=\overline{A_\rho}=A_\rho^T$, the two have the same characteristic polynomial.
  In Euler-product terms, reversing orientation maps each prime cycle $P$ to a prime $P^{-1}$ of the same length, and
  $\chi(P^{-1})=\overline{\chi(P)}$. A graph character and its conjugate therefore give the **same** spectrum and the same zeros, not
  conjugate ones. The coefficients of $\det(1-A_\rho u+qu^2)$ lie in $\mathbb Q(\zeta_N)\cap\mathbb R$.

## 2. The lattice state over $\mathbb Z[\zeta_N]$

**Proposition 2.1** (*proved here*). Let $K=\mathbb Q(\zeta_N)$, $\mathcal O=\mathbb Z[\zeta_N]$ and $d=\varphi(N)$. Let $\Omega=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$ be in $n\times n$
blocks, and set $V_\rho=qM_\rho^{-1}=\bigl(\begin{smallmatrix}A_\rho&1\\-q&0\end{smallmatrix}\bigr)$.

1. $M_\rho^\dagger\Omega M_\rho=q\Omega$, where $\dagger$ is the conjugate transpose with complex conjugation of $\mathcal O$. The plain transpose works only when
   $A_\rho$ is symmetric. Both $M_\rho$ and $V_\rho$ have entries in $\mathcal O$.
2. On $L=\mathcal O^{2n}\cong\mathbb Z^{2nd}$, define $\Omega_{\mathbb Z}(x,y)=\mathrm{Tr}_{K/\mathbb Q}(x^\dagger\Omega y)$. It is integral and alternating, and
   $M^T\Omega_{\mathbb Z}M=q\Omega_{\mathbb Z}$ in any $\mathbb Z$-basis. A twist $\mathrm{Tr}(\delta\,x^\dagger\Omega y)$ is alternating if and only if $\delta$ is real.
3. $\mathrm{charpoly}_{\mathbb Z}(M)=\prod_{a\in(\mathbb Z/N)^\times}\det(x^2-A_{a\varphi}x+q)=P(x)^2$ with $P\in\mathbb Z[x]$.
4. The Weil form $\tfrac12\Omega_{\mathbb Z}(M-V)$ is $\mathrm{Tr}(x^\dagger W_\rho y)$ with $W_\rho=\bigl(\begin{smallmatrix}q&A_\rho/2\\A_\rho/2&1\end{smallmatrix}\bigr)$. It is positive definite
   if and only if every $A_{a\varphi}$, $a\in(\mathbb Z/N)^\times$, has spectrum in the **open** band $(-2\sqrt q,2\sqrt q)$. Call such a flux *Galois-Ramanujan*.
   For the trivial character the uniform mode ($\lambda=q+1$) lies in $L$, so the form is positive only after that mode is removed; no other
   class contains it.
5. For a Galois-Ramanujan flux, $J=(M-V)\bigl((4q-A^2)^{-1/2}\oplus(4q-A^2)^{-1/2}\bigr)$ is an invariant vacuum: $J^2=-1$, $JM=MJ$, $\Omega_{\mathbb Z}(\cdot,J\cdot)>0$.
   $J$ also commutes with multiplication by $\zeta_N$.

*Proof.* Item 1: a block computation gives $M^\dagger\Omega M=\bigl(\begin{smallmatrix}0&q\\-q&A^\dagger-A\end{smallmatrix}\bigr)$, and $MV=q$.

Item 2: complex conjugation is a field automorphism, so $\mathrm{Tr}(\bar z)=\mathrm{Tr}(z)$. The form $h(x,y)=x^\dagger\Omega y$ is skew-Hermitian, so
$\mathrm{Tr}(\delta h(y,x))=-\mathrm{Tr}(\bar\delta h(x,y))$. This is alternating exactly when $\bar\delta=\delta$, and $h(x,x)$ is purely imaginary, so its trace
vanishes. The similitude identity is $\mathrm{Tr}$ applied to item 1.

Item 3: for a $K$-linear map restricted to $\mathbb Q$, the characteristic polynomial is the norm of the $K$-characteristic polynomial, which is the
product over embeddings $\zeta\mapsto\zeta^a$; these send $\varphi$ to $a\varphi$. The blocks of $M$ commute, so $\det(x-M_\rho)=\det(x^2-A_\rho x+q)$. The
factors for $a$ and $-a$ coincide by §1, so the product is a square. $P$ is the norm from $K^+$ of a polynomial with coefficients in
$\mathcal O\cap\mathbb R$, so $P\in\mathbb Z[x]$.

Item 4: $K\otimes\mathbb R\cong\mathbb C^{d/2}$, one factor for each pair $\{\sigma,\bar\sigma\}$, and
$\mathrm{Tr}(x^\dagger Wx)=2\sum_{\sigma\in\Phi}\sigma(x)^\dagger W_{\sigma\rho}\,\sigma(x)$. This is positive definite if and only if each $W_{a\varphi}$ is. The Schur complement of
$W_{a\varphi}$ is $1-A_{a\varphi}^2/(4q)$.

Item 5: $M+V=A\oplus A$ and $MV=q$, so $(M-V)^2=(A^2-4q)\oplus(A^2-4q)$, which gives $J^2=-1$. $J$ is built from $M$, $V$ and functions of $A$,
all of which commute with $M$ and with $\zeta$. Finally $\Omega_{\mathbb Z}J=2W\cdot(4q-A^2)^{-1/2}$ is a product of commuting positive operators. ∎

This is the $\mathbb Z_2$ argument of `graph-super.md` §4 and `lattice-tower.md` §5, run over $\mathcal O$ and then restricted. RH for the twisted zeta
is again an invariant vacuum, with three differences. The vacuum is Hermitian ($\mathcal O\otimes\mathbb R$-linear). It exists only if the whole Galois
orbit $\{\rho^\sigma\}$ is Ramanujan. Each mode occurs twice in $L$, once for $\rho$ and once for $\bar\rho$.

**Checks.** L1–L4 run on 14 examples: a Galois-Ramanujan flux for each of $K_4$ with $N=3,4,5,6$, the cube with $N=3,4,6$ and Petersen with $N=3$,
plus one non-Ramanujan flux where one exists among 400 sampled classes. They confirm:

- exact integrality and $M_{\mathbb Z}^T\Omega_{\mathbb Z}M_{\mathbb Z}=q\Omega_{\mathbb Z}$;
- the characteristic polynomial from `python-flint` against the 60-digit Galois product (residue below $10^{-50}$), and that it is a square;
- the Weil form, positive or not as predicted;
- $J$ (float, $10^{-8}$).

L5 tests the equivalence in item 4 on **every** class of $K_4$ ($N=3,4,5,6$; 432 classes) and of the cube ($N=3$; 243 classes).

**The Galois condition is real only for $\varphi(N)>2$.** For $N=3,4,6$ the orbit is $\{\rho,\bar\rho\}$, which is isospectral, so Galois-Ramanujan is the same
as Ramanujan (D2). For $K_4$ with $N=5$, 118 of the 125 classes are Ramanujan, but only 112 are Galois-Ramanujan (*checked*).

**The symplectic lattice as a GKP code** (*checked*, L0; the reading is mine). $\Omega_{\mathbb Z}=\Omega\otimes T$, where $T_{ij}=\mathrm{Tr}(\zeta^{j-i})$ is the trace
form of $\mathcal O$, and $\det T=|\mathrm{disc}\,K|$. So $L\subset L^\perp$ with $L^\perp/L\cong(\mathcal O/\mathfrak D)^{2n}$, where $\mathfrak D$ is the different. The code
encodes $|\mathrm{disc}\,K|^{n}$ logical states, that is, $|\mathrm{disc}\,K|$ per vertex.

| $N$ | $T$ | Smith invariants of $T$ | $L^\perp/L$ | logical dimension per vertex |
|---|---|---|---|---|
| 2 | $(1)$ | 1 | 0 | 1 (the qunaught lattice of `graph-super.md` §4) |
| 3, 6 | $\bigl(\begin{smallmatrix}2&\mp1\\\mp1&2\end{smallmatrix}\bigr)$ ($A_2$) | 1, 3 | $(\mathbb Z/3)^{2n}$ | 3, a qutrit |
| 4 | $2I$ | 2, 2 | $(\mathbb Z/2)^{4n}$; unimodular after $\delta=\tfrac12$ ($\mathrm{Re}\,x^\dagger\Omega y$) | 4; 1 after the twist |
| 5 | $5I_4-J_4$ | 1, 5, 5, 5 | $(\mathbb Z/5)^{6n}$ | 125 |

For $N=3,6$ no admissible scalar twist does better: $\delta$ must be real, and $K^+=\mathbb Q$ forces $\delta\in\mathbb Z$ for integrality (*proved here*). Whether
a non-scalar similitude form of $M$ is unimodular on $L$ is *open*.

**Locks** (`locks.md` §§1–2).

- (a) Multiplication by $\zeta_N$ is a symplectic automorphism of $(L,\Omega_{\mathbb Z})$ of order $N$ that commutes with $M$ (*proved here*,
  $\mathrm{Tr}(\overline{\zeta}\zeta\,\cdot)=\mathrm{Tr}(\cdot)$). It is complex multiplication by $\mathcal O$. It does **not** rotate eigenvalues: on the $\sigma$-isotypic part it
  is the scalar $\sigma(\zeta)$.
- (b) The one forced eigenvalue relation is equality: each $\mu$ appears twice (item 3). That is $\zeta=1$, between a mode and its own copy, not a
  lock between distinct modes in the sense of `locks.md`.
- (c) A half-turn lock $\lambda\leftrightarrow-\lambda$ appears whenever $-A_\rho$ is gauge-equivalent to $A_\rho$. On the bipartite cube this holds for every
  class (K2).
- (d) Every other root-of-unity relation between distinct modes is a coincidence of the eigenvalues, as for the quarter and sixth turns of
  `locks.md`. Check K1 searches all Galois-Ramanujan classes for relations $\mu'_+=\zeta\mu_\pm$ with $\zeta$ of order up to 120.

| graph, $N$ | Galois-Ramanujan classes | with a lock of order $N$ | lock orders found (number of classes) |
|---|---|---|---|
| $K_4$, 3 | 26 | 6 | 3, 4, 8, 12, 24 (6 each) |
| $K_4$, 4 | 62 | 0 | 2 (38) |
| $K_4$, 5 | 112 | 16 | 5 (16), 30 (16) |
| $K_4$, 6 | 190 | 60 | 2 (90), 3 (12), 4 (24), 6 (60), 8 (36), 12 (12), 24 (24) |
| cube, 3 | 242 | 42 | 2 (all), 3, 4, 6, 8, 12, 24 |
| cube, 4 | 993 | 80 | 2 (all), 4 (80) |
| cube, 6 | 7571 | 200 | 2 (all), 3, 4, 5, 6, 8, 10, 12, 24 |

So a $\mathbb Z_N$ flux is not a lock of order $N$ by construction (*negative finding*, *checked*). Locks of order $N$ occur in some classes only, and
locks of other orders occur as often.

## 3. Deligne modules

For $q=p$ prime, $(L,M)$ is a Deligne module exactly when three conditions hold: $M$ is semisimple with Weil $q$-number eigenvalues
(Galois-Ramanujan, by item 4 and `lattice-tower.md` §5); it is ordinary (the middle coefficient of $\mathrm{charpoly}_{\mathbb Z}M$ is prime to $p$); and
$V$ is integral, which always holds. It then gives an ordinary abelian variety over $\mathbb F_q$ of dimension $n\varphi(N)$ with
$\mathcal O\subset\mathrm{End}$ (Deligne, *standard*, from memory).

- **Ordinariness rule** (*proved here*, D1). Reduce modulo $p$: each factor $x^2-\lambda x+q$ becomes $x(x-\lambda)$. So the middle coefficient is
  $\equiv(-1)^{nd}N_{K/\mathbb Q}(\det A_\rho)\pmod p$, and the flux is ordinary if and only if $\det A_\rho$ is a unit at every prime of $\mathcal O$ above $p$.
- **For $N$ a power of $p$, ordinariness does not depend on the flux** (*proved here*, D4). $\zeta\equiv1$ modulo the unique prime above $p$, so
  $\det A_\rho\equiv\det A$. Here $\det A$ is $-3$ for $K_4$, $9$ for the cube and $48$ for Petersen. So for $N=4$ every Galois-Ramanujan class is ordinary
  on $K_4$ and on the cube, and none is on Petersen. This matches `no-lift.md` at $N=2$: $K_4$ ordinary, Petersen not.
- **Isogeny type** (*sketched*). The characteristic polynomial is $P^2$. By Tate's isogeny theorem, $A\sim B^2$, where $B$ has characteristic polynomial
  $P$ and dimension $n\varphi(N)/2$. $\mathcal O$ embeds into $M_2(\mathrm{End}^0B)$. Howe's polarisation test was not run.

The table counts flux classes for $q=2$ (*checked*, census over all classes):

| graph, $N$ | classes $N^g$ | Ramanujan | Galois-Ramanujan | of these ordinary (Deligne modules) | $\dim$ |
|---|---|---|---|---|---|
| $K_4$, 3 | 27 | 26 | 26 | 12 | 8 |
| $K_4$, 4 | 64 | 62 | 62 | 62 | 8 |
| $K_4$, 5 | 125 | 118 | 112 | 88 | 16 |
| $K_4$, 6 | 216 | 190 | 190 | 78 | 8 |
| cube, 3 | 243 | 242 | 242 | 162 | 16 |
| cube, 4 | 1024 | 993 | 993 | 993 | 16 |
| cube, 6 | 7776 | 7571 | 7571 | 5065 | 16 |
| Petersen, 3 | 729 | 678 | 678 | 474 | 20 |
| Petersen, 4 | 4096 | 3914 | 3914 | 0 | 20 |
| Petersen, 6 | 46656 | 44286 | 44286 | 28656 | 20 |

- No class has an eigenvalue exactly on $\pm2\sqrt q$ (D3), so the difference between the open and the closed band never matters here.
- The classes that fail Ramanujan sit next to the zero flux. For even $N$ they also sit next to the all-negative class: for $K_4$ with $N=6$, the
  failures are the classes with entries in $\{0,\pm1\}$ or $\{3,3\pm1\}$, with $\lambda_{\max}=2.866$. This is the continuity remark of
  `gauge-groups.md` seen on the torsion points (*checked* in a scratch computation; the script records only the counts).
- On $K_4$ at $N=3$ the 27 classes give four spectra:
  - $(x-3)(x+1)^3$: 1 class, the trivial one;
  - $(x+1)(x^3-x^2-5x+3)$: 12 classes, ordinary;
  - $(x-2)(x+1)(x^2+x-3)$: 8 classes, not ordinary;
  - $x(x-2)(x^2+2x-2)$: 6 classes, not ordinary.

## 4. RH on average over the $N$-torsion

**Theorem 4.1** (*proved here*). For every $N\ge2$,
$$
\frac1{N^g}\sum_{\varphi\in H^1(Y,\mathbb Z/N)}\det(x-A_\varphi)\;=\;\int_{H^1(Y,\mathbb R/\mathbb Z)}\det(x-A_\varphi)\,d\varphi\;=\;\mu(Y,x),
$$
the matching polynomial. Its roots are real and lie in $(-2\sqrt q,2\sqrt q)$ (Heilmann–Lieb, *standard*, from memory).

*Proof.* Expand the determinant over spanning elementary subgraphs $H$, which are vertex-disjoint unions of edges and cycles of length at least 3:
$$
\det(x-A_\varphi)=\sum_Hx^{\,n-|V(H)|}(-1)^{c(H)}\prod_{C\subset H}\bigl(\chi_\varphi(C)+\chi_\varphi(C)^{-1}\bigr)\quad\text{(Sachs; Godsil–Gutman, standard)}.
$$
In cotree coordinates $z_e=\zeta^{\varphi(e)}$, the class of a simple cycle has entries in $\{0,\pm1\}$ and is nonzero. Vertex-disjoint cycles are
edge-disjoint. So every term is a monomial with exponents in $\{-1,0,1\}^g$, and it is non-constant exactly when $H$ has a cycle. A Laurent monomial
with exponents in $\{-1,0,1\}^g$ averages over $\mu_N^g$, $N\ge2$, and over the torus, to its constant term. The constant term is the sum over
matchings, which is $\mu(Y,x)$. ∎

**Checks.**

- R1: exact equality over all classes for $K_4$ and the cube with $N=3,4,6$ (27 to 7776 classes). Each class's $\det(x-A_\varphi)\in\mathbb Z[x]$ is certified
  by $\det^2=\mathrm{charpoly}(A_{\mathbb Z})$.
- R2: $K_4$ with $N=5$, in floating point.
- R3: the $N=2$ case for comparison.
- R4: the Laurent structure, symbolically, for $K_4$: 17 monomials, all exponents in $\{-1,0,1\}$, constant term $x^4-6x^2+3$.
- R5: the U(1) Haar average by Gauss–Legendre quadrature, which is not a torsion grid, for $K_4$ and the cube. Errors are $10^{-14}$ and $4\times10^{-12}$.
- R6: largest roots 2.334 ($K_4$), 2.578 (cube) and 2.631 (Petersen), all below $2\sqrt2=2.828$.

`gauge-groups.md`'s claim that the U(1) average is the matching polynomial is **verified** (*checked*, R5, and proved by 4.1).

**What the brief expected, and where it lives.**

- The brief expected the $N$-average to be a generating polynomial of subgraphs whose cycles have homology in $N\cdot H_1$, with lengths
  $\equiv0\bmod N$. For the determinant this is a *negative finding*. An elementary subgraph uses each of its cycles once, with coefficient $\pm1$, and
  never lands in $N\cdot H_1\setminus0$. So the $N$-average is the same polynomial for every $N\ge2$, and RH on average over the $N$-torsion follows from
  Heilmann–Lieb for every $N$. No new computation decides it.
- The selection by $N\cdot H_1$ does act on the **counts**:
  $$N^{-g}\sum_\chi\mathrm{Tr}\,B_\chi^k=\#\{\text{closed non-backtracking walks of length }k\text{ with class in }N\cdot H_1\}.$$
  For $K_4$ with $N=3$ the counts are 0 for $k\le8$ and 24 of 528 at $k=9$ (*checked*, C1, brute force).
- Equivalently, $\prod_\chi L(u,\chi)$ is the Ihara zeta of the $H_1/NH_1$-cover. For $K_4$ with $N=3$ its 108-vertex spectrum is the union of the 27
  twisted spectra (*standard*, Artin factorisation; *checked*, C2).
- A consequence of 4.1 at the level of Euler products (*proved here*; *checked*, C3). $\det(1-uB_\chi)=\prod_P(1-\chi(P)u^{\ell(P)})$, so its average
  over the $N$-torsion is $\sum_S(-1)^{|S|}u^{\ell(S)}$ over finite sets $S$ of prime cycles with $\sum_{P\in S}[P]\in N\cdot H_1$. By 4.1 this does not depend on
  $N\ge2$. So the sets with total class in $N\cdot H_1\setminus0$ cancel exactly, for every $N$.

## 5. The Dirichlet rung of the ladder

1. (*standard*) A Dirichlet character mod $N$ is a finite-order character of the idele class group of $\mathbb Q$, unramified outside $N$. The graph
   analogue is a character of $H_1(Y,\mathbb Z)$ of order dividing $N$. Both take values in $\mu_N\subset\mathbb Z[\zeta_N]$, and both families are acted on by
   $\mathrm{Gal}(\mathbb Q(\zeta_N)/\mathbb Q)$.
2. (*standard*, from memory; *checked* on the graph, C1–C2) Orthogonality at the level of counts is shared. $\varphi(N)^{-1}\sum_\chi\chi(n)$ selects
   $n\equiv1\bmod N$, the primes that split completely in $\mathbb Q(\zeta_N)$, and $\prod_\chi L(s,\chi)$ is $\zeta_{\mathbb Q(\zeta_N)}$ up to the factors at $p\mid N$. On the graph,
   $N^{-g}\sum_\chi\chi$ selects walks with class in $N\cdot H_1$, the cycles that close up in the $H_1/N$-cover, and $\prod_\chi L(u,\chi)$ is that cover's Ihara
   zeta.
3. (*proved here* / *standard*) The Galois-orbit product is the characteristic polynomial of one integral step on $\mathbb Z[\zeta_N]^{2n}$ on the graph. On
   the Dirichlet side it is an $L$-function with rational coefficients for which no lattice and no step are known. This is the same gap as for
   $\zeta$ (`data-ladder.md` §4, item 1).
4. (*proved here* on the graph; *standard* for Dirichlet) On a graph $L(u,\bar\chi)=L(u,\chi)$, because orientation reversal pairs every prime cycle with
   one of conjugate character value. For a complex Dirichlet character, $L(s,\bar\chi)\ne L(s,\chi)$ and the zeros are reflected. So the finite rung has
   no non-self-dual character, and this item has no finite analogue.
5. (*proved here*) For each Galois-Ramanujan flux the graph supplies a lattice, an integral step of norm $q$, a symplectic form with
   $L^\perp/L\cong(\mathcal O/\mathfrak D)^{2n}$, and an explicit Hermitian vacuum $J$. For $L(s,\chi)$ none of these four is known, exactly as for $\zeta$.
6. (*standard*) At the local level, the Dirichlet factor at $p\nmid N$ is $(1-\chi(p)p^{-s})^{-1}$: the character enters as a phase on a pole, and there
   are no local zeros, as for $\zeta$ (`data-ladder.md` §3). The graph analogue of a local factor is the factor of a prime cycle, $1-\chi(P)u^{\ell(P)}$.
7. (*proved here* on the graph; *standard*, from memory, for Dirichlet) On average over the family, the graph's $\det$, which is $1/L$ up to the
   $\chi$-independent factor $(1-u^2)^{|E|-|V|}$, averages to the matching polynomial for every $N$, with roots in the band. On the Dirichlet side:
   - $\varphi(N)^{-1}\sum_\chi1/L(s,\chi)=\sum_{n\equiv1(N)}\mu(n)n^{-s}$, which depends on $N$ and for which I know no RH-type statement;
   - $\varphi(N)^{-1}\sum_\chi L(s,\chi)=N^{-s}\zeta(s,1/N)$, which for $N\ge3$ has zeros in $\mathrm{Re}\,s>1$ (Davenport–Heilbronn).
8. (*proved here*) The mechanism of Theorem 4.1 uses two facts: $\det(x-A_\varphi)$ is a polynomial of degree at most 1 in each coordinate of a
   finite-dimensional character torus, and the cycles of an elementary subgraph are primitive in $H_1$. The Dirichlet family has neither a
   finite-rank $H_1$ nor a bounded-degree expression in $\chi$, so the mechanism has no counterpart there.
9. (*standard*) Ordinariness and the Deligne module (§3) need a finite base field and have no Dirichlet analogue.
10. Summary. The items of the finite rung with a Dirichlet analogue are the character values in $\mathbb Z[\zeta_N]$, the Galois orbits, and
    orthogonality at the level of counts, whose product over the family is the zeta of the cover or of the cyclotomic field. The items without one
    are the lattice, the step, the vacuum, the Deligne module, the self-duality $L(\bar\chi)=L(\chi)$, and the RH-on-average theorem for the
    determinant.

A row for `data-ladder.md` §0 (proposed, not inserted):

| rung | lattice $L$ | step | vacuum $J$ (= RH) | zeros |
|---|---|---|---|---|
| $\mathbb Z_N$ flux on a graph | $\mathbb Z[\zeta_N]^{2n}$ restricted to $\mathbb Z$; $\Omega_{\mathbb Z}=\mathrm{Tr}\,x^\dagger\Omega y$, $L^\perp/L=(\mathcal O/\mathfrak D)^{2n}$ | $M_\rho$, CM by $\mathbb Z[\zeta_N]$ | yes iff every $\rho^\sigma$ is Ramanujan; $J=(M-V)(4q-A^2)^{-1/2}$ | $2n\varphi(N)$, each twice |

## 6. Status and checks

*Review correction 2026-10-06 (`notes/reviews/adelic-gkp-arithmetic-2026-10-06.md`, 37 VALID / 3 MINOR / 1 INVALID, none INVALID on this page):* Proposition 2.1(3), "the characteristic polynomial over $\mathbb Z$ is $P(x)^2$, each mode twice", holds for $N\ge3$; at $N=2$ ($K_4$ with one negative edge) the polynomial is squarefree.


| statement | status | check |
|---|---|---|
| $q=2$ for $K_4$, cube, Petersen (brief said 3, 3, 2) | correction | — |
| Ihara–Bass for $\mathbb Z_N$ fluxes | standard; checked | I1 |
| $L(u,\bar\rho)=L(u,\rho)$ | proved here | L2 (square) |
| Prop. 2.1 (similitude, $\Omega_{\mathbb Z}$, char. poly $=P^2$, Weil form $\Leftrightarrow$ Galois-Ramanujan, vacuum $J$) | proved here; checked | L1–L5 |
| $L^\perp/L\cong(\mathcal O/\mathfrak D)^{2n}$; $N=4$ unimodular after $\delta=\tfrac12$; no scalar repair for $N=3,6$ | proved here; checked | L0, L0' |
| unimodular non-scalar similitude form for $N=3,6$ | open | — |
| no forced lock of order $N$; only forced relation is the doubling; half turn on bipartite graphs | negative finding; checked | K1, K2 |
| ordinariness $\Leftrightarrow N(\det A_\rho)$ prime to $p$; flux-independent for $N=p^k$ | proved here; checked | D1, D4 |
| census and Deligne-module counts (§3 table) | checked | census, D2, D3 |
| $A\sim B^2$ with $\mathcal O\subset\mathrm{End}$ | sketched | — |
| Theorem 4.1: $N$-torsion average $=$ Haar average $=$ matching polynomial for every $N\ge2$ | proved here; checked | R1–R5 |
| roots of the average in the band | standard (Heilmann–Lieb, from memory); checked | R6 |
| "average = subgraphs with cycles in $N\cdot H_1$" | negative finding (at det level) | R1 |
| count-level selection of $N\cdot H_1$; Artin factorisation over the $H_1/N$-cover | standard; checked | C1, C2 |
| Euler-product cancellation of sets with class in $N\cdot H_1\setminus0$ | proved here; checked | C3 |
| Dirichlet comparisons (§5) | standard, from memory, where so labelled | — |

`checks/check_zn_flux.py`: 87 of 87 pass. Nothing is registered and no REFUTE review has run.

## 7. Next

- Average $L(u,\chi)$ itself, not $\det$, over the $N$-torsion, and locate its poles. This is the graph counterpart of the Hurwitz average in §5.7, where
  the Dirichlet side has zeros off the line.
- Run Howe's test on $(L,M,\Omega_{\mathbb Z})$ for the ordinary classes, with the CM type now also carrying the $\mathcal O$-action
  (`howe-positivity.md`). Decide whether a unimodular similitude form exists for $N=3$.
- Average over primitive characters only (exact order $N$), the analogue of primitive Dirichlet characters. Theorem 4.1 does not cover this subfamily.
