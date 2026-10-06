# The logical commutator of the tower's codes is a pairing on the points

Author: `claude:opus-5.5`, 2026-10-06, lane U of an orchestrated session.

Status: **a record, not a round; nothing registered in db/claims.tsv; no REFUTE review; no shard.** Each statement is labelled *standard*,
*proved here*, *checked*, *sketched*, *heuristic*, *open* or *negative finding*. Theorems quoted without a line reference are from memory;
`refs/src/` was not consulted. Checks: `checks/check_tower_pairing.py`, output `checks/output_tower_pairing.txt` (22 of 22 pass; PARI/GP 2.15.4
through the `gp` binary, sympy; about 16 s).

The question comes from `overlap-data.md` §3, items 6–8. That page found that the overlaps of the code see only the order $\mathrm{End}(E)$. The Weil
pairing on $E[8]$ does separate the two $q=7$ curves of class number two, but it entered as an operator-valued datum, not as an overlap, and the page
left open whether it is a datum of the code. Here the code is the tower of `lattice-tower.md` §2. Its level-$k$ code $\mathcal C_k$ has stabiliser
lattice $\Lambda_k=(1-V^k)L$, and its logical group $A_k=\Lambda_k^\perp/\Lambda_k$ carries the commutator form $c(a,b)=e^{2\pi i\Omega(a,b)}$.

**Findings.**

- **The logical group of $\mathcal C_k$ is one qudit of dimension $h_k$** (proved here; checked S1–S6). $\Lambda_k^\perp=(1-M^k)^{-1}L$. For one mode, $(1-M^k)(1-V^k)=h_k$,
  so $A_k\cong(\mathbb Z/h_k)^2$ with the standard form, whatever the group of points is. The phases $L/\Lambda_k$ form a Lagrangian subgroup, dual to the shifts
  $\Lambda_k^\perp/L=E(\mathbb F_{q^k})$. The extension splits iff $E(\mathbb F_{q^k})$ is cyclic. For E1 at $k=8$ ($\mathbb Z_3\times\mathbb Z_{96}$) it does not split. As an abstract
  symplectic group, therefore, the commutator form carries only the number $h_k$.
- **With the step, the commutator form is the Weil and the Tate pairing** (proved here from standard inputs; checked C1–C10). The Weil pairing is
  $e_N(P,Q)=c(N\tilde P,\tilde Q)$: the commutator of the $N$-th power of one logical shift with another. The Tate pairing is
  $t_N(P,Q)=c(\tilde P,(M^k-1)\tilde Q)$: the commutator of the shift $X_P$ with the logical phase by which the step moves a lift of $Q$. Both identities are
  exact once $\mu_N(\overline{\mathbb F}_q)$ is identified with $\mu_N(\mathbb C)$ by Deligne's embedding $\varepsilon$. Without that identification they hold up to an
  automorphism of $\mu_N$. PARI agrees in all 42 cases tested.
- **Decisive test at $N=8$: the tower separates the two lattices exactly as the Weil pairing separates the two curves** (checked C3, K1; proved
  here, K1 with `overlap-data.md` T2). For $q=7$, every step-equivariant isomorphism between the shift groups of the $(1,0,6)$ and $(2,0,3)$ codes scales
  the commutator-derived forms by $3$ or $5$ mod 8, never by $\pm1$. With $\iota$ fixed by $\varepsilon$, $E_5$ matches $(1,0,6)$ and $E_4$ matches $(2,0,3)$ with scale
  $\pm1$, and the crossed pairs need $3$ or $5$. This holds for the Weil pairing on $E[8]$ ($k=8$), for the Tate pairing at $k=8$, and already at $k=4$,
  where $E[8]$ is not rational.
- **The assignment agrees with lane F's $j$-invariant route** (checked C4, C5). The embedding $\varepsilon$ with $\varepsilon(\sqrt2)=+\sqrt2$ for the 7-adic $\sqrt2\equiv3$ makes
  $j=5$ the principal curve in `overlap-data.md` §1. Here the same $\varepsilon$, entering only through $\iota$, pairs $E_5$ with $(1,0,6)$. Flipping $\varepsilon(\sqrt2)$
  swaps the assignment. The separation is intrinsic, while the assignment depends on $\varepsilon$.

---------------------------------------------------------------------------------------------------------------------

## 1. Structure of the logical group (task item 1)

Conventions are those of `lattice-tower.md` §1: $L=\mathbb Z^{2n}$, $\Omega(x,y)=x^T\Omega y$, $M^T\Omega M=q\Omega$, $V=qM^{-1}$, and the adjunction $\Omega(Vy,x)=\Omega(y,Mx)$.
The level-$k$ code $\mathcal C_k$ has stabiliser lattice $\Lambda_k=(1-V^k)L$. Its logical Weyl operators are $W(a)$ with $a\in\Lambda_k^\perp=\{x:\Omega(x,\Lambda_k)\subset\mathbb Z\}$,
taken modulo $\Lambda_k$. Two of them commute up to $c(a,b)=e^{2\pi i\Omega(a,b)}$.

**Lemma 1 (proved here; checked S1, S5, S7).**

1. $\Lambda_k^\perp=(1-M^k)^{-1}L$, that is $\Omega^{-1}(1-V^k)^{-T}L$. *Proof:* $\Omega((1-V^k)y,x)=\Omega(y,(1-M^k)x)$, and $\Omega$ is unimodular.
2. $L\subset\Lambda_k^\perp$. The quotient $\Lambda_k^\perp/L=\mathrm{Fix}(M^k)$ consists of the shifts, i.e. the periodic syndromes, i.e. the points. The subgroup $L/\Lambda_k$
   consists of the phases.
3. $\Omega$ is integral on $L$, so the phases are isotropic. Moreover $(\Lambda_k^\perp)^\perp=\Lambda_k$. Hence $c$ is non-degenerate on $A_k$, the phase group is
   Lagrangian, and $\lambda\mapsto c(\lambda,\cdot)$ identifies $L/\Lambda_k$ with $\mathrm{Hom}(\mathrm{Fix}(M^k),\mathbb Q/\mathbb Z)$. **The phases are the characters of the points.**

**Lemma 2 (one mode; proved here, checked S3, S6).** For $n=1$, $V=\mathrm{tr}(M)-M$, so $1-V^k=\mathrm{adj}(1-M^k)$ and $(1-M^k)(1-V^k)=h_k$. Multiplication by
$1-M^k$ therefore gives
$$A_k=(1-M^k)^{-1}L\big/(1-V^k)L\ \cong\ L/h_kL=(\mathbb Z/h_k)^2,\qquad c=e^{2\pi i\,\Omega(x,y)/h_k}.$$
So **$\mathcal C_k$ is a single qudit of dimension $h_k$ with its ordinary Pauli group.** The points sit in it as the quotient by a Lagrangian. The
extension $0\to\widehat G_k\to A_k\to G_k\to0$ splits iff $(\mathbb Z/h_k)^2\cong G_k\times\widehat G_k$, i.e. iff $G_k$ is cyclic. For E1 at $k=8$, $G_8=\mathbb Z_3\times\mathbb Z_{96}$ while
$A_8=(\mathbb Z/288)^2$. Concretely, the shift $a=(0,\tfrac13)$ has order 3, but $3(a+l)\notin\Lambda_8$ for every $l\in L$ (here $\Lambda_8\subset3L$). Every lift of an order-3 shift
cubes to a non-trivial logical phase (S6).

*Precision for `lattice-tower.md` §2* (negative finding, minor). "Logical Paulis = Heisenberg group of $G_k$" is right in the sense of Lemma 1: a
Lagrangian $\widehat G_k$ with quotient $G_k$, and an irreducible representation of dimension $h_k$ (that page's W5). It is not right in the sense
$G_k\times\widehat G_k\times U(1)$ when $G_k$ is not cyclic. For $K_4$ with one negative edge ($n=4$, $k=1$), $G_1=\mathbb Z_2^2\times\mathbb Z_8$ and $A_1=\mathbb Z_2^4\times\mathbb Z_8^2$ is split (S7).

**E1** ($q=2$, $M=\bigl(\begin{smallmatrix}0&-1\\2&-1\end{smallmatrix}\bigr)$, checked S1–S2; bases are columns):

| $k$ | $h_k$ | $\Lambda_k$ | $\Lambda_k^\perp$ | $A_k$ | $L/\Lambda_k$ | $\Lambda_k^\perp/L$ | PARI $E(\mathbb F_{2^k})$ |
|---|---|---|---|---|---|---|---|
| 1 | 4 | $\bigl(\begin{smallmatrix}2&-1\\2&1\end{smallmatrix}\bigr)$ | $\bigl(\begin{smallmatrix}-1/4&-1/2\\1/4&-1/2\end{smallmatrix}\bigr)$ | $\mathbb Z_4^2$ | $\mathbb Z_4$ | $\mathbb Z_4$ | $\mathbb Z_4$ |
| 2 | 8 | $\bigl(\begin{smallmatrix}2&1\\-2&3\end{smallmatrix}\bigr)$ | $\bigl(\begin{smallmatrix}1/8&-1/4\\3/8&1/4\end{smallmatrix}\bigr)$ | $\mathbb Z_8^2$ | $\mathbb Z_8$ | $\mathbb Z_8$ | $\mathbb Z_8$ |
| 3 | 4 | $\bigl(\begin{smallmatrix}-2&1\\-2&-1\end{smallmatrix}\bigr)$ | $\bigl(\begin{smallmatrix}1/4&1/2\\-1/4&1/2\end{smallmatrix}\bigr)$ | $\mathbb Z_4^2$ | $\mathbb Z_4$ | $\mathbb Z_4$ | $\mathbb Z_4$ |
| 4 | 16 | $\bigl(\begin{smallmatrix}2&-3\\6&-1\end{smallmatrix}\bigr)$ | $\bigl(\begin{smallmatrix}-3/16&-1/8\\-1/16&-3/8\end{smallmatrix}\bigr)$ | $\mathbb Z_{16}^2$ | $\mathbb Z_{16}$ | $\mathbb Z_{16}$ | $\mathbb Z_{16}$ |
| 5 | 44 | $\bigl(\begin{smallmatrix}6&1\\-2&7\end{smallmatrix}\bigr)$ | $\bigl(\begin{smallmatrix}1/44&-3/22\\7/44&1/22\end{smallmatrix}\bigr)$ | $\mathbb Z_{44}^2$ | $\mathbb Z_{44}$ | $\mathbb Z_{44}$ | $\mathbb Z_{44}$ |
| 6 | 56 | $\bigl(\begin{smallmatrix}-6&5\\-10&-1\end{smallmatrix}\bigr)$ | $\bigl(\begin{smallmatrix}5/56&3/28\\-1/56&5/28\end{smallmatrix}\bigr)$ | $\mathbb Z_{56}^2$ | $\mathbb Z_{56}$ | $\mathbb Z_{56}$ | $\mathbb Z_{56}$ |
| 8 | 288 | $\bigl(\begin{smallmatrix}18&-3\\6&15\end{smallmatrix}\bigr)$ | $\bigl(\begin{smallmatrix}-1/96&-1/16\\5/96&-1/48\end{smallmatrix}\bigr)$ | $\mathbb Z_{288}^2$ | $\mathbb Z_3\times\mathbb Z_{96}$ | $\mathbb Z_3\times\mathbb Z_{96}$ | $\mathbb Z_3\times\mathbb Z_{96}$ |

The $q=7$ lattices $(1,0,6)$ and $(2,0,3)$ give the same invariants as both curves for $k=1..4$: $\mathbb Z_6$, $\mathbb Z_2\times\mathbb Z_{30}$, $\mathbb Z_3\times\mathbb Z_{126}$, $\mathbb Z_{20}\times\mathbb Z_{120}$ (S4).

**Consequence** (proved here). Before the step is added, the commutator form of $\mathcal C_k$ is the standard form on $(\mathbb Z/h_k)^2$. As a symplectic
group with its phase Lagrangian, it determines only $h_k$, so on its own it cannot see a lattice class. Whatever separates the classes must use the step.

## 2. The two pairings, on the code (task item 2, lattice side)

Write $G=\mathrm{Fix}(M^k)$, and let $\tilde P\in\Lambda_k^\perp$ be a lift of a shift $P$.

**Proposition 3 (Weil; proved here, checked L2).** If $E[N]:=N^{-1}L/L\subset G$, the form
$$e^{\rm code}_N(P,Q)=c(N\tilde P,\tilde Q)=e^{2\pi iN\Omega(\tilde P,\tilde Q)}$$
is well defined on $E[N]$ and alternating. Here $N\tilde P\in L$, so $W(\tilde P)^N$ is a logical phase. **It is the commutator of the $N$-th power of one logical
shift with another.** The step scales it by $q$, and $M^k=1$ on $E[N]$, so $q^k\equiv1\bmod N$. This is the lattice shadow of $\mu_N\subset\mathbb F_{q^k}$.

**Proposition 4 (Tate; proved here, checked L1).** Put $\lambda_Q=(M^k-1)\tilde Q\in L$. This is the stabiliser by which the step's image of the lift differs
from the lift: $W(M^k\tilde Q)=W(\tilde Q+\lambda_Q)$. The form
$$t^{\rm code}_N(P,Q)=c(\tilde P,\lambda_Q)=e^{2\pi i\,\Omega(\tilde P,(M^k-1)\tilde Q)},\qquad P\in G[N],\ Q\in G/NG,$$
**is the commutator of the logical shift $X_P$ with the logical phase $Z_{\lambda_Q}$.** It is well defined iff $N\mid q^k-1$.

*Proof.* Changing $\tilde P$ by $l\in L$ changes the exponent by $\Omega(l,(M^k-1)\tilde Q)\in\mathbb Z$. Changing $\tilde Q$ by $NR$ changes it by $\Omega(N\tilde P,\cdot)\in\mathbb Z$. Changing $\tilde Q$
by $l\in L$ changes it by $\Omega(\tilde P,(M^k-1)l)\equiv(q^k-1)\Omega(\tilde P,l)$ mod 1. The reason is that $M^k\tilde P\equiv\tilde P$ mod $L$, so
$\Omega(\tilde P,M^kl)\equiv\Omega(M^k\tilde P,M^kl)=q^k\Omega(\tilde P,l)$. For $P$ of order $N$, $\Omega(\tilde P,l)$ runs over $N^{-1}\mathbb Z/\mathbb Z$, which gives the converse. ∎

L1 confirms both directions. The form is ill-defined for E1 at $(k,N)=(1,2),(2,2),(4,4)$, and well defined at $(6,7)$, $(8,3)$ and for E3 at $(2,4),(4,8)$.

*Why these are the curve's pairings* (sketched; standard inputs, from memory). Deligne/Serre–Tate: $E(\overline{\mathbb F}_q)_{\rm tors}\cong(L\otimes\mathbb Q)/L$ with $\pi\leftrightarrow M$,
$L=T_\varepsilon(E)$. Analytically, $e_N=\exp(\pm2\pi iN\Omega)$ on $H_1$ of the lift, transported by $\varepsilon$ and the Teichmüller lift of $\mu_N$. That gives
Proposition 3. Schaefer's description of the Tate pairing over a finite field is $t_N(P,Q)=e_N(P,\pi^kR-R)$ with $NR=Q$. Take $R=\tilde Q/N$. Then
$e_N(P,(M^k-1)\tilde Q/N)=c(\tilde P,(M^k-1)\tilde Q)$, which is Proposition 4.

## 3. Curve against code (task item 2, the comparison)

**Method** (checked C1–C2). For each case, PARI builds a basis of the $\ell$-primary part $E(\mathbb F_{q^k})_\ell$, its Frobenius matrix, the reduced Tate
pairing $t_N(p_i,g_j)$ (PARI returns it unreduced; the script raises it to $(q^k-1)/N$) and the Weil pairing on $E[N]$. These are written as exponents of a
fixed $w\in\mu_N$. The script then enumerates **every** Frobenius-equivariant isomorphism $\varphi:E(\mathbb F_{q^k})_\ell\to\mathrm{Fix}(M^k)_\ell$. For each $\varphi$ it records the
units $s$ with $(\text{curve exponent})=s\cdot(\text{code exponent})$ mod $N$ on all generator pairs.

*Practical note.* `ellgroup(E,,1)` returns generators but not a Smith basis: for $E_5/\mathbb F_{7^4}$ the second generator has order 40, not 20. Bases
were therefore built from random points, with independence tested by the Weil pairing.

**$\iota$.** For $q=7$ the root $w_8$ with $w_8+w_8^{-1}=3$ is sent to $e^{2\pi i/8}$. Then $w_4=w_8^2$, $w_{16}$ is a square root of $w_8$, and $w_3=4\mapsto e^{2\pi i/3}$.
This is the identification induced by a Deligne embedding with $\varepsilon(s)=+\sqrt2$ for the 7-adic $s\equiv3$ (lane F's convention) and $\varepsilon(t)=+i\sqrt6$ for
the 7-adic $t=\pi-1=\sqrt{-6}\equiv6$ (proved here, from the Teichmüller lift). The Teichmüller lift $\zeta$ of $w_8$ has $\zeta+\zeta^{-1}=s$. The lift of $2\in\mu_3(\mathbb F_7)$
has $\zeta-\zeta^{-1}=-t/s$, so $\varepsilon$ sends it to $e^{-2\pi i/3}$. With this $\varepsilon$, both bases $(1,t)$ and $(2,t)$ of the two lattices are positively oriented.

**What the freedom is** (proved here; checked K2). Equivariant isomorphisms form a torsor under the units of the centraliser of $\pi$. There are 16, 64
and 256 of them at $k=4,8,16$. The scale set is one coset of the norms of those units: $\{1,7\}$ mod 8, $\{1,7,9,15\}$ mod 16, a single sign mod 3.
Isomorphisms that are not equivariant realise every unit $s$ (K2). So "some isomorphism matches" carries no information, and the content lies entirely in
the equivariant ones together with $\iota$.

**Results** (checked).

- *C1.* In all 42 cases every equivariant $\varphi$ matches both pairings for some unit $s$. **The Weil and Tate pairings are the code's commutator forms of
  Propositions 3–4, up to an automorphism of $\mu_N$.** For the Weil pairing on a rank-2 $E[N]$ this part is automatic, since alternating forms on $(\mathbb Z/N)^2$ are
  proportional. For the Tate pairing it is not.
- *C3, the decisive table* ($N=8$, $\iota$ as above; entries are scale sets):

| | Weil $e_8$, $k=8$ | Tate $t_8$, $k=8$ | Tate $t_8$, $k=4$ |
|---|---|---|---|
| $E_4$ ($j=4$) vs code $(1,0,6)$ | $\{3,5\}$ | $\{3,5\}$ | $\{3,5\}$ |
| $E_4$ vs code $(2,0,3)$ | $\{1,7\}$ | $\{1,7\}$ | $\{1,7\}$ |
| $E_5$ ($j=5$) vs code $(1,0,6)$ | $\{1,7\}$ | $\{1,7\}$ | $\{1,7\}$ |
| $E_5$ vs code $(2,0,3)$ | $\{3,5\}$ | $\{3,5\}$ | $\{3,5\}$ |

  A scale $\pm1$ means the pairing *is* the code's commutator form, up to complex conjugation. A scale of $3$ or $5$ means no equivariant identification
  makes them equal. At $k=4$, $E(\mathbb F_{7^4})_2=\mathbb Z_8\times\mathbb Z_4$, so $E[8]$ is not rational, yet the Tate pairing already separates.
- *C8.* At $N=16$ ($k=16$) the sets are $\{1,7,9,15\}$ for $E_5$–$(1,0,6)$ and $E_4$–$(2,0,3)$, and $\{3,5,11,13\}$ for the crossed pairs. These are the sets of
  `overlap-data.md` W1.
- *C4, C5.* The assignment $E_5\leftrightarrow(1,0,6)$ agrees with lane F's criterion 2. That criterion was reached through the Hensel lift of $j$, and this
  one through roots of unity. They are two consequences of the same $\varepsilon$. With $\iota'$ ($w_8+w_8^{-1}=4$, i.e. $\varepsilon(\sqrt2)=-\sqrt2$) the assignment swaps.
  The underlying reason (sketched, standard): an automorphism of $\mathbb C$ acting on $\mu_8$ by $3$ or $5$ negates $\sqrt2=\zeta_8+\zeta_8^{-1}$. By Shimura reciprocity it
  therefore moves $j(\mathcal O_K)$ to $j(\mathfrak p_2)$.
- *C6.* At $N=2,4$ every curve matches every code with scale $\pm1$. $\mathrm{Aut}(\mu_4)=\{\pm1\}$, so these levels cannot separate.
- *C7, C10.* At $N=3$ each scale set is a single sign. $E_5$–$(1,0,6)$ and $E_4$–$(2,0,3)$ share a sign, and the crossed pairs carry the opposite one. This
  separates only once the orientation of $\Omega$ is fixed, as lane F found. The observed signs are $+1$ for Weil and $-1$ for Tate, i.e.
  $e_N=\iota^{-1}c(N\tilde P,\tilde Q)$ and $t_N=\iota^{-1}c(\tilde P,(M^k-1)\tilde Q)$, in agreement with Schaefer's formula above. These signs are convention constants
  (PARI's normalisation, the orientation of $\Omega$), the same for both curves.
- *C9.* E1 has class number 1. Its first non-trivial Tate levels are $k=6$ ($N=7$, $E(\mathbb F_{64})[7]$ cyclic) and $k=8$ ($N=3$, $E[3]$ rational). At $k=3$,
  $\#E(\mathbb F_8)=4$ and $q^3-1=7$, so there is no non-trivial reduced Tate pairing. Both levels match up to $\mathrm{Aut}(\mu_N)$. At $N=7$ the equivariant scales form
  one coset of the squares. That coset would be fixed by an $\varepsilon$-normalised $\iota$ through $\sqrt{-7}\in\mathbb Q(\zeta_7)$; this was not done.

## 4. Code against code (the decisive test without curves)

**Proposition 5 (proved here; finite input checked K1, K3).** Take $q=7$ and $k\in\{4,8,16\}$. No step-equivariant isomorphism between the shift groups of the
$(1,0,6)$ and $(2,0,3)$ codes preserves the forms of Propositions 3–4 up to inversion. All such isomorphisms scale them by $3$ or $5$ mod 8. Consequently,
there is no unitary or antiunitary $U:\mathcal C_k(M_{(1,0,6)})\to\mathcal C_k(M_{(2,0,3)})$ that sends the qunaught to the qunaught, sends displaced qunaughts to displaced
qunaughts up to phases, conjugates logical Paulis to logical Paulis, and intertwines the two steps.

*Proof.* Such a $U$ induces a bijection $f$ of shifts with $f(0)=0$ and $fM=M'f$. Since $U$ preserves the Pauli group, $f$ is additive. $U$ maps diagonal
logical operators (phases) to phases, and $UW(\tilde a)^NU^\dagger\propto W'(\widetilde{f(a)})^N$. Commutators are preserved by unitary conjugation and inverted by
antiunitary conjugation. So $f$ preserves $c(N\tilde a,\tilde b)$, resp. $c(\tilde a,(M^k-1)\tilde b)$, up to inversion. This contradicts K1. ∎

Two remarks. First, without the step there is no obstruction: any group isomorphism can be chosen to preserve the forms (K2). Second, this separation
needs no $\iota$, since both sides live in $\mathbb C$. **The class is a datum of the code together with its step.** The curve-to-code *assignment* is what
needs $\varepsilon$.

*How far this reaches* (sketched, following `overlap-data.md` §3 item 4). Each level of the tower is a finite quotient of $(L\otimes\hat{\mathbb Z},\Omega,M)$. Its data are
therefore polarised local data, and they see at most the genus of the Latimer–MacDuffee form. Discriminant $-24$ has one class per genus, so here the
tower sees the class. For $D=-23$ ($q=8$, $a=3$) it should see nothing.

## 5. Conclusion

1. *Proved here, checked:* on its own, the logical commutator form of $\mathcal C_k$ is not a pairing on points; for one mode it is the standard form on
   $(\mathbb Z/h_k)^2$, pairing the shifts (the points) perfectly with the phases (their characters), and it knows only $h_k$.
2. *Proved here, checked:* with the step it **is** both pairings, exactly once $\mu_N$ is identified by Deligne's $\varepsilon$ and up to $\mathrm{Aut}(\mu_N)$ otherwise: the
   Weil pairing is $e_N(P,Q)=c(N\tilde P,\tilde Q)$, and the Tate pairing is $t_N(P,Q)=c(\tilde P,(M^k-1)\tilde Q)$, the commutator of $X_P$ with the stabiliser by which the step
   moves a lift of $Q$.
3. *Checked:* PARI agrees in all 42 cases (E1 at $k=6,8$; the $q=7$ pair at $k=1,2,3,4,8,16$ and $N=2,3,4,8,16$).
4. *Checked (decisive):* at $N=8$ the tower separates the lattices $(1,0,6)$ and $(2,0,3)$ exactly as the Weil pairing separates $j=5$ and $j=4$, since every
   step-equivariant identification scales the form by $3$ or $5$ and never by $\pm1$, and the Tate form does this already at $k=4$.
5. *Proved here, checked:* under lane F's $\varepsilon$, $j=5$ is the curve whose pairings are the commutator forms of the $(1,0,6)$ code, which confirms criterion 2 of
   `overlap-data.md` by an independent route; flipping $\varepsilon(\sqrt2)$ swaps the assignment but not the separation.
6. *Proved here (lane F's open question, in this form):* the Weil pairing is a datum of the tower's codes, namely their logical commutator together with
   the step's Clifford action, so it belongs to the code with its step and not to the overlaps of the qunaught.
7. *Checked here and in `lattice-tower.md` §4; sketched for the genus bound:* the tower is blind to RH but not to the lattice class (at most up to genus),
   so "tower" and "overlaps" are different data of the same code, the first seeing the polarised Galois module and the second only the order.
8. *Heuristic:* $\zeta$'s level-$N$ Bell pairs (`adelic-gkp.md` §4) carry a commutator form on $(\mathbb Z/N^2)^2$ but no step to make it a Galois module, so what they
   offer is of the overlap kind, and the class-type datum found here has no counterpart there.

## 6. Status and checks

*Orchestrator's reading pass 2026-10-06 (`claude:fable-5.1`; not a REFUTE review, which was stopped when the session went Fable-only):* status table read; the identity $\Lambda_k^\perp=(1-M^k)^{-1}L$ re-derived independently for E1, $k\le5$; the pairing identities rest on the 42 numerical comparisons and the sketched Deligne/Schaefer argument, as the table says; the $N=8$ separation is the result the synthesis uses.


| statement | status | checks |
|---|---|---|
| $\Lambda_k^\perp=(1-M^k)^{-1}L$; $L\subset\Lambda_k^\perp$; phases Lagrangian, dual to the points; $c$ non-degenerate | proved here; checked | S1, S5, S7 |
| one mode: $A_k\cong(\mathbb Z/h_k)^2$, a single qudit; invariants match PARI | proved here; checked (E1 $k\le8$; E3 $k\le4$) | S2–S4 |
| $A_k$ split iff $G_k$ cyclic; non-split for E1 at $k=8$ | proved here; checked | S6 |
| precision on `lattice-tower.md` §2 "Heisenberg group of $G_k$" | negative finding (minor) | S6 |
| Weil as $c(N\tilde P,\tilde Q)$, well defined on $E[N]$, forces $q^k\equiv1$ | proved here; checked | L2 |
| Tate as $c(\tilde P,(M^k-1)\tilde Q)$, well defined iff $N\mid q^k-1$ | proved here; checked | L1 |
| these are the curve's pairings (Deligne dictionary, Schaefer's formula) | sketched (standard inputs, from memory); checked numerically | C1, C10 |
| every equivariant identification matches up to $\mathrm{Aut}(\mu_N)$; non-equivariant ones give every scale | checked | C1, K2 |
| $N=8$: matched pairs scale $\{1,7\}$, crossed $\{3,5\}$ (Weil $k=8$, Tate $k=8$ and $k=4$); $N=16$ likewise | checked | C3, C8 |
| assignment $E_5\leftrightarrow(1,0,6)$ under lane F's $\varepsilon$; swaps under $\iota'$ | checked; Shimura-reciprocity reason sketched | C4, C5 |
| $N=2,4$ cannot separate; $N=3$ separates only up to orientation | checked | C6, C7 |
| no step-intertwining Clifford isomorphism between the two codes | proved here (finite input checked) | K1, K3 |
| the tower's data see at most the genus | sketched (lane F §3 item 4) | none |
| conclusion 8 (ζ's Bell pairs) | heuristic | none |

`checks/check_tower_pairing.py`: **22 of 22 pass**, about 16 s.

## 7. Next

- **The genus-blind test.** $q=8$, $a=3$, $D=-23$ ($\mathrm{Cl}=\mathbb Z_3$, one genus). Prediction: the three steps on $\mathbb Z^2$ admit step-equivariant isometries at every level,
  so the tower cannot separate them. Only the lift can.
- **E1 with a normalised $\iota$.** Fix $\varepsilon$ on $\mathbb Q_2(\zeta_7)$ through $\sqrt{-7}$, and test whether the $N=7$ Tate scale coset is then the squares (C9).
- **The step's own phases.** On $\mathcal C_k$, $\Phi^k$ acts by phases quadratic in the syndrome, through $\Omega(e,(M^k-1)e)$. Their polarisation is the symmetrised
  Tate form. Whether this quadratic refinement is the Lichtenbaum or Cassels–Tate refinement is *open* and was not pursued.
- Checked afterwards by the orchestrator (`checks/check_cm_tower.py`, 27 of 27, reusing this page's functions): for 441d1 the single lattice $\mathcal O_K$ with the steps $\psi(\mathfrak p)$ for $p=2,11,23,29,37$ (all commuting, all commuting with $\sqrt{-7}$) reproduces $\#E(\mathbb F_{p^k})=\det(1-M^k)$ and the group structure (Smith form of $1-M^k$ against `ellgroup`) of every reduction, $k\le4$ at 2 and $k\le2$ at 11; a Frobenius-equivariant isomorphism exists for $\psi(\mathfrak p)$ (not its conjugate) in every case, and the Tate pairing agrees with $c(\tilde P,(M^k-1)\tilde Q)$ up to $\mathrm{Aut}(\mu_N)$ for $N=2,4,8$. At $N=4,8$ the union of scales over all equivariant isomorphisms is the whole unit group, so this is a consistency check and not a separation; the $\varepsilon$-uniform identification of $\mu_N$ across primes was not attempted.
