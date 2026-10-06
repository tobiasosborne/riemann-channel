# What data the zeros of $\zeta$ need, in the terms of the understood cases

Author: `claude:fable-5.1`, 2026-10-06, synthesis of an orchestrated session (lanes A, B, C, E, F run by `claude:opus-5.5`; the lane pages are
`curve-bridge.md`, `no-lift.md`, `cm-lift.md`, `cone-bridge.md`, `overlap-data.md`). TJO's brief: "explore the GKP connection comprehensively and
build on the ideas of the previous sessions ... build up enough examples to understand what data we need for the classic Riemann zeta zeroes in
the terms we discover here, i.e. the qunaught, GKP, Weil positivity". Method as steered on 2026-10-05: interpret the understood cases first, then
match to $\zeta$, not the other way round.

Status: **a record, not a round.** Nothing registered in `db/claims.tsv`; no REFUTE review; no shard. Statuses inside are those of the lane pages
(*standard*, *proved here*, *checked*, *sketched*, *heuristic*, *open*, *negative finding*); a statement here is never stronger than on its lane page.
`refs/src/` was absent in the container, so every theorem quoted in the lane pages is "from memory" and not byte-cited.

## 0. The ladder

Every understood case is a triple $(L,M,\Omega)$: an integral lattice $L$, an integral step $M$ of norm $q$ on it ($M^T\Omega M=q\Omega$, $V=qM^{-1}$ integral), and
a symplectic form $\Omega$; and RH is one further datum, an invariant Gaussian vacuum $J$ (a complex structure with $\Omega(\cdot,J\cdot)>0$ and $JM=MJ$),
equivalently the positivity of the Weil form $\tfrac12\Omega(M-V)$ (`lattice-tower.md` §5). The table says where each item comes from on each rung.

| rung | lattice $L$ | step | vacuum $J$ (= RH) | arithmetic $J$ (polarisation) | zeros | page |
|---|---|---|---|---|---|---|
| one mode $M=\bigl(\begin{smallmatrix}0&-1\\q&\lambda\end{smallmatrix}\bigr)$ | $\mathbb Z^2$, the form $qx^2+\lambda xy+y^2$ | $M$ | exists iff $\lambda^2<4q$ | Deligne/Howe, $=\pm J$; the sign cancels in the metric | two, $\mu^\pm$ | `lattice-tower.md`, `curve-bridge.md` |
| ordinary elliptic curve $E/\mathbb F_q$ | $H_1$ of the canonical lift; **not determined by the counts** (class number) | lifted Frobenius | yes (Hasse) | Rosati form $=$ vacuum form $\times\sqrt{4q-a^2}$ (proved) | two | `curve-bridge.md` |
| $\mathbb Z_2$ flux on a graph, ordinary ($K_4$, one negative edge) | $\mathbb Z^{2n}$ from the graph $=H_1$ of the lift of $E_2\times E_4\times\mathrm{Jac}(y^2+(x^2+x)y=x^5+1)$ | $M_s$ | yes iff the flux is Ramanujan | exists; differs from the vacuum by a sign per mode; $\Omega$ itself fails Howe, a unit twist repairs it | $2n$ | `howe-positivity.md`, `no-lift.md` |
| $\mathbb Z_2$ flux, non-ordinary (Petersen, $K_5$) | $\mathbb Z^{2n}$ from the graph; arithmetically from the Centeleghe–Stix category, **no canonical lift**; glued, not a product | $M_s$ | yes; on the supersingular block $J=M/\sqrt q$ (quarter turn) | ordinary block: as above; supersingular block: **none selected** | $2n$ | `no-lift.md` |
| genus two over $\mathbb F_q$ ($y^2=x^5+x^3+x^2-2$, $\mathbb F_5$) | $\mathbb Z^4$ | Frobenius | yes; the positive similitude forms are a cone $\sum_jt_j\,(\text{vacuum form on mode }j)$ and **RH is the cone being non-empty** | a further point of the cone; Rosati transported is not proportional to the vacuum form (weights 10.870, 20.171); it settles integrality, not RH | four | `cone-bridge.md` |
| $\mathbb Z_N$ flux on a graph ($N=3,4,5,6$) | $\mathbb Z[\zeta_N]^{2n}$ by restriction of scalars; $\zeta_N$ is complex multiplication, not a lock | $M_\rho$, $M_\rho^\dagger\Omega M_\rho=q\Omega$ | yes iff every Galois-conjugate flux is in the band ($\rho$ and $\bar\rho$ have the same spectrum) | not run | $2n\varphi(N)$, each mode twice | `zn-flux.md` |
| CM Hecke $L(\psi,s)$, $K=\mathbb Q(\sqrt{-7})$ (441d1, 49a1) | one lattice $\mathcal O_K$ for every split prime | one step $\psi(\mathfrak p)$ per prime, all commuting | one $J_K$ for all primes: **local RH free** | the complex structure of $K\otimes\mathbb R$ | infinitely many, **not determined by the local data** | `cm-lift.md` |
| $\zeta$ | none known: $\mathbb Q^2$ is rigid and divisible (G3) | a flow (the squeeze group $C_{\mathbb Q}$), not an integral map | open (= RH) | none | infinitely many, all global | `adelic-gkp.md` §12 |

## 1. What determines what

Lane A's order for an ordinary elliptic curve (`curve-bridge.md` §6), extended by lanes B and C. Each arrow is a *standard* or *checked* fact.

1. **Counts.** The degree-resolved overlaps of the adelic qunaught with product stabiliser states, $\langle\Theta_K,1_D\rangle=q^{h^0(D)}$, give $N_k$,
   the Frobenius polynomial $P$, and with it the isogeny class, $\Omega$ up to scale, the Weil form, and $J$ up to scale. So the counts *decide* RH.
2. **The lattice.** $P$ does not determine $L$: at $q=7$, $a=2$ (discriminant $-24$, class number 2) two curves have the same counts, the same groups
   $E(\mathbb F_{7^k})$ for all $k\le24$, and non-isomorphic Deligne modules (*checked*, lane A). The trivial-character cokernel of Riemann–Roch gives only
   the principal class $\mathbb Z[F]$. Lane F (`overlap-data.md`, *proved/checked*) settles what the divisor-resolved overlaps see: the overlap function
   $D\mapsto q^{h^0(D)}$ at all levels, up to Frobenius-compatible relabelling, is the $\mathbb Z[\pi]$-module $E(\bar{\mathbb F}_q)$, and two such modules
   are isomorphic iff $\mathrm{End}(E)=\mathrm{End}(E')$: **the product-stabiliser overlaps of the code see the order, never the ideal class** (the
   class is a global invariant, locally trivial at every $\ell$; the $q=5$ pair differs in the order, $\mathbb Z[i]$ against $\mathbb Z[2i]$, which is why
   its groups differ). What does see the class is the Weil pairing, which is the commutator form of Mumford's theta group acting on $L(nO)$: an
   operator-valued datum, not an overlap. Which of the two curves has the principal lattice depends on Howe's $\varepsilon$.
3. **$\Omega$ on $L$**: the Weil pairing; fixed by $L$ up to Howe's sign $\varepsilon$. The sign flips $\Omega$ and the arithmetic $J_\varepsilon$ together, so
   $\Omega_\varepsilon(\cdot,J_\varepsilon\cdot)=\Omega(\cdot,J\cdot)$: the Riemann form is the vacuum form whichever $\varepsilon$ (*proved*, lane A).
4. **$J$ from the polarisation.** This step carries RH, and it is the one `adelic-gkp.md` §12 says has no analogue for $\mathbb Q$. Lane B adds that a
   canonical lift is not what supplies the lattice (the Centeleghe–Stix category does, from linear-algebra data with $FV=p$), and that on a
   supersingular block the arithmetic supplies no $J$ at all: there the vacuum is the step itself.
5. **The bridge is exact in genus one** (*proved*, lane A): the unimodular map $S=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ carries the
   Riemann–Roch cokernel state $(Y_j,Y_{j-1})$ of `analytic.md` §13 to the Deligne module, the window shift to $M$, the discrete Wronskian to $\Omega$, and
   the Casoratian (the cokernel metric, the Rosati form) to the Weil form: $\Omega(Ss,J\,Ss)=2\mathcal Q(s)/\sqrt{4q-a^2}$. So the two lattice pictures of
   the notebook (the adelic qunaught's cokernel and the GKP syndrome torus) are one object in genus one. In genus $g\ge2$ the similitude forms form a
   cone of dimension $g$ and proportionality is not forced. Lane E (`cone-bridge.md`, *proved/checked*): for a fixed compatible $\Omega$ the positive
   similitude forms are $\sum_jt_j\,G_j$ with $G_j$ the vacuum form on mode $j$; the Weil form $\tfrac12\Omega(M-V)$ is the point with weights
   $\varepsilon_j\tfrac12\sqrt{4q-\lambda_j^2}$, $\varepsilon_j$ the Krein sign of $\Omega$ on mode $j$, so it is positive iff RH holds **and** $\Omega$ has CM type $\Phi_+$;
   the Rosati form transported by a cyclic vector sweeps the cone (an infinite unit orbit in genus two), and the form $\Omega_+=\mathrm{Tr}(x\bar y/(V-F))$ on
   $\mathbb Z[F,V]$ has Weil form exactly $\tfrac12\mathcal T$ with vacuum weights $1/\sqrt{4q-\lambda_j^2}$ per mode, the per-mode version of lane A's scalar,
   but is principal only in genus one. On the curve over $\mathbb F_5$ and on $K_4$ the principal polarisation's own Weil form is indefinite. So in several
   modes the lattice pictures share a cone, not a point: **RH is the non-emptiness of the cone, witnessed by the Weil form, which is polynomial in the
   step and exists before RH is known; the polarisation is a further point that decides integrality (a qunaught, $\det=1$) and not RH.**

## 2. The negative findings that constrain the $\zeta$ side

Each is *checked* on its page; together they say where not to look.

- **The tower is blind** (`lattice-tower.md` §4): levels, codes, logical Cliffords and Lefschetz exist with or without RH.
- **Counts do not determine the lattice** (lane A), and no overlap of the code with product stabiliser states does (lane F): the datum that carries RH
  sits on a lattice whose class is fixed only by the Weil pairing, an operator-valued datum of the code.
- **Local lattices and vacua do not determine global zeros** (lane C): 49a1 and 441d1 share $\mathcal O_K$, $J_K$ and every local step up to sign, and
  have different zeros; only 441d1 has a central zero (root number $-1$). Lane I (`gate-phases.md`, *proved/checked*) locates the difference: the
  root number is the product of the local Fourier-gate phases ($-i$ at $\infty$ from the Hermite function, $i$ at 7 from the conductor squeeze, $\pm1$
  at 3, $1$ at every unramified place, where the local state is a Fourier-invariant qunaught); the half turn that 49a1 spends in its Euler factor at 3
  ($a_9=-3$), 441d1 spends in its gate phase, and at 3 the "step" stops being an invariant (it depends on the uniformiser). So the distinguishing
  datum is a charged local state with its phase, in the Hilbert space of the local mode, not on the lattice or the vacuum; and the gate phases see
  only the parity of the central zero, not the split-prime signs of the twist.
- **No arithmetic $J$ on a supersingular block** (lane B): where $\mu$ and $-\mu$ have equal valuation, Deligne's rule selects no CM type; positivity
  there is $\Omega(x,Mx)>0$, a statement about the step alone.
- **The lattice index is sign-blind** (`graph-ihara.md`): $|\det(m-nM)|$ carries no sign, so the count mechanism of curves does not transfer to a graph
  without flux.

**The family rung** (lane D, `zn-flux.md`, *proved/checked*). Over the $N$-torsion of the Brillouin torus the average of $\det(x-A_\rho)$ equals the
U(1) Haar average, which is the matching polynomial, for every $N$ (the determinant has degree at most one in each cotree variable); so "RH on
average" holds for every finite-order family by Heilmann–Lieb, and it is a statement about the family, not about any one member. The Dirichlet
analogue of the average is a Hurwitz partial zeta, which has zeros off the line (Davenport–Heilbronn, from memory): the family rung transfers the
count-level orthogonality and the Galois orbits, and does not transfer the lattice, the step, the vacuum, or the average theorem.

## 3. Two levels: local and global

Lane C separates two things that the finite cases fuse. For a graph or a curve over $\mathbb F_q$ the global object is finite: its zeros are the
eigenvalues of one integral step on a finite-rank lattice, and its places are the orbits of that step (prime cycles, closed points). For the CM
$L$-function the places carry the finite structure (one one-mode step $\psi(\mathfrak p)$ on $\mathcal O_K$ per split prime, the quarter turn $\pm i\sqrt p$ at
inert primes, a charged local state at the ramified prime 7) and the zeros are not eigenvalues of anything on $\mathcal O_K$: they are the squeeze
frequencies at which the Mellin transform of every overlap profile in the angular-momentum-one sector vanishes. For $\zeta$ the local level is empty
of zeros: the local factor at $p$ is the Mellin profile of the local qunaught $1_{\mathbb Z_p}$ (`adelic-gkp.md` §7), the local squeeze trace is Lefschetz
at the origin (§10), and there are only poles. Everything about the zeros of $\zeta$ is global.

So the understood finite cases model the **local** level of $\zeta$-like $L$-functions, where RH is Hasse and Deligne, and the reading of
`lattice-tower.md` §7.3 (zeros as oscillator frequencies, the squeeze as the trivial pair) is a reading of that level. At the global level the
examples give no lattice. Lane C's phrase: in the CM case the oscillator frequencies are the local angles $\theta_{\mathfrak p}$, the global zeros are
squeeze frequencies, and there are no poles (*heuristic*).

The exception that keeps the programme alive is the graph itself read as a global field: its places are prime cycles and its zeros are global, and
they are eigenvalues of an integral step because the graph's $H_1$ is of finite rank. The question "what data for $\zeta$" is therefore the question
of what plays $H_1$ (with its integral step) for the global zeros of $\zeta$, which is Deninger's demand that the identities be realised on
cohomology (`cit:deninger-conformal-metric`), now with the integrality made explicit.

## 4. The data for $\zeta$, item by item

In hand (*standard*, note §§1–10; inventory in `zeta-ingredients.md` §2): the qunaught $\Theta$ on the lattice $\mathbb Q^2\subset\mathbb A^2$; the product vacuum
$f_0$ (Gaussian at $\infty$, qunaughts at $p$); the squeeze group $C_{\mathbb Q}$ with its Mellin transform, each prime step with its exact adjoint; the
Fourier gate; Weil's functional $\omega$ with its explicit decomposition into two zero modes and local Lefschetz traces, a similitude form for every
step before RH; the functional-equation pairing of shard 04t on finite spans of zeros; the pole plane as the one negative direction of the windowed
form with poles kept (lane G, *checked* at 40–60 digits: $Z_N\mp P_N$ have inertia $(n-1,1,0)$, each off-line pair adds one); Connes's cokernel, an
infinite-dimensional space with a unitary squeeze flow that sees only the critical zeros.

Absent, by the ladder:

1. **A lattice with an integral step** whose Weil form is $\omega$. The code's own lattice $\mathbb Q^2$ cannot serve: it is rigid and divisible (G3),
   the squeezes $D_a$ act on it as automorphisms with $(1-D_a)\mathbb Q^2=\mathbb Q^2$, so there is no logical space and no counts. In the curve case the
   lattice is not the code's lattice either: it is $H_1$ of a lift, or a Centeleghe–Stix object, and the code's trivial-character data do not even
   fix its class (lane A), nor do any of its product-stabiliser overlaps (lane F); the class is seen only by the Weil pairing, the commutator form
   of the theta group (an operator datum of the code, not an overlap). So the missing datum is not something the overlaps can be expected to
   contain; it is extra structure on the cokernel, of the kind the symplectic pairing supplies in the finite case.
2. **A polarisation** on that lattice (note §12.2). In genus one lane A shows it is the vacuum form transported, so "polarisation" and "vacuum" are
   the same datum seen from the two sides; in several modes lane E separates them: the polarisation is one point of the cone and RH is the
   non-emptiness of the cone, witnessed by the Weil form alone. Lane E read Weil's quadratic form for $\zeta$ as the analogue of that witness
   (*heuristic*); lane G (`zeta-ingredients.md`, *proved/checked*) qualifies this. For $\zeta$ the step and its adjoint exist exactly ($M_a=\delta_a*$,
   $V_a=aM_a^{-1}$ by the involution) and Weil's form $B$ is a similitude form with adjunction for every $a$ before RH; by the converse of lane E's
   proposition ($\Omega=2G(M-V)^{-1}$ is alternating and compatible whenever $M$ is a similitude of $G$), $B$ is a Weil-form point for each prime step
   separately, but with a prime-dependent singular $\Omega_p$ (weights $1/(\sqrt p\sin(\gamma\log p))$, small divisors), and **no single compatible
   $\Omega$ serves two primes**. Relative to the one pairing the notebook already has, the functional-equation pairing $\Omega_{\rm FE}$ of shard 04t,
   every prime step's Weil form is indefinite and $B$ is the **vacuum point**, the analogue of lane C's shared $G_{J_K}$; it is a Weil-form point
   only for the infinitesimal generator $D$, with Williamson weights $|\gamma|$, which is tautological (as $\mathcal T$ in analytic §14 is the Weil form
   for the generator $F$ only). In the window the compressed dilation by 2 is a similitude of the Gram form only on functions supported away from
   the edge; on the whole window the residual stays near $0.4$ for $N\le160$ and $x\le100$ (*negative finding*). So what $\zeta$ lacks is not a
   symplectic partner for one step but one $\Omega$ for the whole commuting family of prime steps; the Deninger metric cone of shard 04u remains the
   analogue of the cone, and the reason for positivity, ampleness through Rosati in the curve case, is for $\zeta$ the open statement itself.
3. **The local charged states and their gate phases** (lane I): a separate item of the ladder, present for Hecke and Dirichlet $L$-functions
   (Gauss sums at the conductor, the Hermite phase at $\infty$), trivial for curves over $\mathbb F_q$ (root number $+1$, squeezes only), for graphs
   (the completed zeta is even) and for $\zeta$ (every phase is 1). It is the first global invariant assembled from local data that is not a
   lattice or vacuum datum, and it does not carry RH.
4. **Counts.** At the real place there is nothing to count (note §12.1); lane A shows that even where there are counts they fix only the isogeny
   class.

What the examples say about where the datum would have to sit (*heuristic*): on a global, integral, finite-rank-per-mode structure on Connes's
cokernel on which the squeeze acts as a similitude; not on the tower, not on the local data (lane C), not on the code lattice (G3). Lane C's open
list (`cm-lift.md` §4) states the three concrete versions of this: a lattice-with-step whose periodic-point counts give $L(\psi,s)$; an integral
structure on the $\ell=1$ cokernel of $\mathcal O_K$; a positivity uniform over the $\ell$-tower of Hecke characters.

## 4b. One step against a family: why the Weil form of $\zeta$ is the vacuum point

Lane E's witness is a one-step statement, and lane G's qualification is what it becomes for a commuting family (*checked* for the identities, *heuristic* for the reading).

- One mode, one step. On a mode where $S=M/\sqrt q$ rotates by $\theta$, the Weil form is $\tfrac12\Omega(M-V)=\sqrt q\,\sin\theta\;\Omega(\cdot,J\cdot)$:
  the vacuum form times $\sin\theta$. It is positive iff $\theta\in(0,\pi)$ for the orientation of $\Omega$, which is lane E's CM-type condition $\Phi_+$
  and lane A's Howe sign. For one step the orientation can be chosen, so "Weil form positive" and "a vacuum exists" coincide.
- One lattice, a family of steps (lane C). On $\mathcal O_K$ the Hecke steps $\psi(\mathfrak p)$ all commute with the one vacuum $J_K$, but their Weil forms
  for a fixed $\Omega$ are $\mathrm{Im}\,\psi(\mathfrak p)$ times the vacuum form, and $\psi(\bar{\mathfrak p})=\overline{\psi(\mathfrak p)}$ gives the opposite sign:
  for a family no orientation makes every Weil form positive, and this has nothing to do with RH. The family-invariant datum is the vacuum, or
  equivalently the Rosati form $\mathrm{Tr}_{K/\mathbb Q}(x\bar y)$ of the family's algebra, positive because the Rosati involution is positive, i.e. because
  $K$ is a CM field, i.e. RH for every $\mathfrak p$ at once.
- $\zeta$ (lane G). The prime dilations are a commuting family; on the pair $\{\rho,1-\bar\rho\}$ the step $M_p$ rotates by $\gamma\log p$, so its Weil form
  for $\Omega_{\rm FE}$ is $\sqrt p\,\sin(\gamma\log p)$ times the vacuum form, indefinite for every $p$, exactly as for the Hecke family; and Weil's form
  $B=\omega(h*\tilde h)$ is the Rosati form of the family's algebra (the test-function algebra with the involution $\tilde{\ }$), i.e. the vacuum point.
  So lane G's finding is the family version of lanes A and E, not a discrepancy, and it sharpens note §12.2: **in the finite cases the positivity of
  the Rosati involution comes from a polarisation (an ample divisor); for $\zeta$ the positivity of the involution $h\mapsto\tilde h$ on the squeeze
  algebra is Weil's criterion itself.** The datum $\zeta$ lacks is therefore not an $\Omega$ for one step (each prime has one, lane G) but a reason for
  the family's involution to be positive; in every understood case that reason is geometric and global (ampleness on a Jacobian, the CM field of
  the lift), and it is carried by the lattice, which is the item the ladder says $\zeta$ does not have.

Checked: `checks/check_family_weil.py` (51 of 51 pass): the one-mode identity Weil form $=\sqrt q\sin\theta\,G_J$, its orientation dependence, the CM family's opposite signs on conjugate primes with one vacuum $J_K$ and the trace form a positive multiple of $G_{J_K}$, and the sign statistics of $\sin(\gamma\log p)$ over 200 zeros for $p=2,3,5$.

## 5. Corrections to earlier pages (recorded here; the pages carry a one-line annotation)

- `lattice-tower.md` §1 table and §6, `adelic-gkp.md` G12(ii): the Pauli-six lattice ($x^2+2x+5$, groups $\mathbb Z/8$) belongs to $y^2=x^3+4x\pm1$ over
  $\mathbb F_5$ ($j=1$), not to $y^2=x^3+4x$ ($j=1728$, End $=\mathbb Z[i]$, groups $\mathbb Z/2\times\mathbb Z/4$); shard 03c lists all three equations (lane A).
- The E mode lifts to 441d1; 49a1 reduces mod 2 to the $\mathbb F_2$-twist, step $-M$ (lane C). `cm-lift.md` §2.4: under the self-dual trace pairing the
  Fourier gate maps the $\ell=1$ Gaussian to $\ell=-1$, not to itself (lane I).
- `lattice-tower.md` §6, §9: "no lift" for the non-ordinary examples is "no canonical lift"; supersingular factors lift with Frobenius, not canonically (lane B).
- `lattice-tower.md` §7.3 is a reading of the local level only (lane C, §3 above).
- `lattice-tower.md` §5: (i)$\Rightarrow$(ii) needs the CM type $\Phi_+$ for $\Omega$; it holds for the graph steps the page was written for and fails for
  $M'=\bigl(\begin{smallmatrix}0&1\\-5&-2\end{smallmatrix}\bigr)$ (RH, Weil form negative definite). General form: (i) $\Leftrightarrow$ (iii) $\Leftrightarrow$ the Weil form
  of some compatible form is positive (lane E).
- The lane B brief had $K_5$ at $q=4$ and the lane D brief had $K_4$ and the cube at $q=3$; all are 3-regular except $K_5$ (4-regular), so $q=2$ and $q=3$
  respectively, as the existing pages use.

## 6. Next

- Lane G's next: a description of $\Omega_D$ that does not go through $B$; the prime-step similitude test in a smooth window basis; the CM version of the
  vacuum-point reading. Lane J (`ff-dirichlet.md`, a Dirichlet character of $\mathbb F_q(t)$ with every ladder item) and the two REFUTE reviews
  (`notes/reviews/adelic-gkp-*-2026-10-06.md`) are to be folded in when they land.
- `notes/weil-bond-analytic/checks/metric_blocker_checks.py` imports `scripts/rtp2_blind_recovery.py`, which needs Python 3.12 (`math.sumprod`); it does not run on 3.11.
- Lane I's open items: the full quadratic-twist family; Hecke characters of higher infinity type; a function-field shadow with a ramified twist.
- Lane F's open items: whether the Weil pairing is expressible as a datum of $\Theta_K$ itself; the genus-blind case ($q=8$, $a=3$, discriminant $-23$, three
  curves in one genus), predicted and not checked.
- Which of the four ideal classes of $\mathcal O_K$ and which principal form belong to $\mathrm{Jac}(C)$ itself for the curve over $\mathbb F_5$ (lane E).
- A $\mathbb Z_N$ flux on a graph as the finite shadow of a Dirichlet family: lattice $\mathbb Z[\zeta_N]$, step, Hermitian Weil form, RH on average over the
  Brillouin torus (`gauge-groups.md`), and the data ladder for Dirichlet $L$ against it.
- The Fourier-gate phases (Gauss sums, Hermite phase) whose product is the root number; the GKP meaning of 441d1's forced central zero (lane C).
- A Howe-type positivity criterion for Centeleghe–Stix objects with supersingular factors; the Petersen twist (lane B).
- Before registering anything: the REFUTE review of `graph-ihara.md`, `graph-super.md` and the lane pages (HANDOFF T-b), and byte-citations once
  `refs/src/` is fetched.
