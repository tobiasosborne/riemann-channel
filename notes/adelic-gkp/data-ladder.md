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
for a step without real eigenvalues and an $\Omega$ of CM type $\Phi_+$ equivalently the positivity of the Weil form $\tfrac12\Omega(M-V)$ (`lattice-tower.md` §5 with the
precisions of lane E and of the review: $M'=\bigl(\begin{smallmatrix}0&1\\-5&-2\end{smallmatrix}\bigr)$ has a vacuum and a negative Weil form; $B\oplus2B^{-T}$, $B=\bigl(\begin{smallmatrix}0&2\\1&0\end{smallmatrix}\bigr)$,
has eigenvalues $\pm\sqrt2$, a vacuum, and every compatible Weil form zero). The table says where each item comes from on each rung.

| rung | lattice $L$ | step | vacuum $J$ (= RH) | arithmetic $J$ (polarisation) | zeros | page |
|---|---|---|---|---|---|---|
| one mode $M=\bigl(\begin{smallmatrix}0&-1\\q&\lambda\end{smallmatrix}\bigr)$ | $\mathbb Z^2$, the form $qx^2+\lambda xy+y^2$ | $M$ | exists iff $\lambda^2<4q$ | Deligne/Howe, $=\pm J$; the sign cancels in the metric | two, $\mu^\pm$ | `lattice-tower.md`, `curve-bridge.md` |
| ordinary elliptic curve $E/\mathbb F_q$ | $H_1$ of the canonical lift; **not determined by the counts** (class number) | lifted Frobenius | yes (Hasse) | Rosati form $=$ vacuum form $\times\sqrt{4q-a^2}$ on the companion lattice $\mathbb Z[F]$ (proved); on a non-principal lattice the pull-back is doubled | two | `curve-bridge.md` |
| $\mathbb Z_2$ flux on a graph, ordinary ($K_4$, one negative edge) | $\mathbb Z^{2n}$ from the graph $=H_1$ of the lift of an abelian fourfold isogenous to $E_2\times E_4\times\mathrm{Jac}(y^2+(x^2+x)y=x^5+1)$, glued at 2 (index $2^4$ over the product; review INVALID corrected) | $M_s$ | yes iff the flux is Ramanujan | exists; differs from the vacuum by a sign per mode; $\Omega$ itself fails Howe, a unit twist repairs it | $2n$ | `howe-positivity.md`, `no-lift.md` |
| $\mathbb Z_2$ flux, non-ordinary (Petersen, $K_5$) | $\mathbb Z^{2n}$ from the graph; arithmetically from the Centeleghe–Stix category, **no canonical lift**; glued, not a product | $M_s$ | yes; on the supersingular block $J=M/\sqrt q$ (quarter turn) | ordinary block: as above; supersingular block: **none selected** | $2n$ | `no-lift.md` |
| genus two over $\mathbb F_q$ ($y^2=x^5+x^3+x^2-2$, $\mathbb F_5$) | $\mathbb Z^4$ | Frobenius | yes; the positive similitude forms are a cone $\sum_jt_j\,(\text{vacuum form on mode }j)$ and **RH is the cone being non-empty** | a further point of the cone; Rosati transported is not proportional to the vacuum form (weights 10.870, 20.171); it settles integrality, not RH | four | `cone-bridge.md` |
| $\mathbb Z_N$ flux on a graph ($N=3,4,5,6$) | $\mathbb Z[\zeta_N]^{2n}$ by restriction of scalars; $\zeta_N$ is complex multiplication, not a lock | $M_\rho$, $M_\rho^\dagger\Omega M_\rho=q\Omega$ | yes iff every Galois-conjugate flux is in the band ($\rho$ and $\bar\rho$ have the same spectrum) | not run | $2n\varphi(N)$, each mode twice | `zn-flux.md` |
| Dirichlet character $\chi$ of $\mathbb F_q(t)$ mod $f$ (order $N$) | $\mathbb Z[\zeta_N][F,V]$, the $\chi$-part of $\mathrm{Jac}(y^N=cf)$ up to isogeny | $F$ | yes (Weil) when $P_\chi$ is squarefree; Weil form $\tfrac12\mathrm{Tr}(x\sigma y)$ positive then, degenerate for a repeated root ($t^4+1$ at $q=5$) | $\Omega_+$ from the functional equation alone; not principal | $\deg f-1$ or $\deg f-2$; **gate phases present and non-trivial**, product $=W$ | `ff-dirichlet.md` |
| CM Hecke $L(\psi,s)$, $K=\mathbb Q(\sqrt{-7})$ (441d1, 49a1) | one lattice $\mathcal O_K$ for every split prime | one step $\psi(\mathfrak p)$ per prime, all commuting | one $J_K$ for all primes: **local RH free** | the complex structure of $K\otimes\mathbb R$ | infinitely many, **not determined by the local data** | `cm-lift.md` |
| LPS Hecke pair $A_{13},A_{17}$ on one $H_1$ | $\mathbb Z^{2n}$ | $M_{13}$, $M_{17}$: commuting Hecke operators, non-commuting steps | one per step; **none shared** ($M_{13}V_{17}$ has real eigenvalues) | both Weil forms positive for the shared $\Omega$ | Ramanujan | `family-vacuum.md` |
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
   Riemann–Roch cokernel state $(Y_j,Y_{j-1})$ of `analytic.md` §13 to the companion lattice $\mathbb Z[F]$ (the Deligne module when the lattice is
   principal; otherwise the smallest integral intertwiner has determinant 2 and the vacuum form pulls back doubled, review MINOR), the window shift to $M$, the discrete Wronskian to $\Omega$, and
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
- **Local lattices and vacua do not determine global zeros** (lane C): 49a1 and 441d1 share $\mathcal O_K$, $J_K$ and every local step up to sign at every $p\ne3$ (at 3, 441d1 has a
  charged local state and no step), and have different zeros; only 441d1 has a central zero (root number $-1$). Lane I (`gate-phases.md`, *proved/checked*) locates the difference: the
  root number is the product of the local Fourier-gate phases ($-i$ at $\infty$ from the Hermite function, $i$ at 7 the normalised Gauss sum $g_7/\sqrt7$, the squeeze
  $D_7$ supplying only the conductor 49, $\pm1$ at 3, $1$ at every unramified place, where the local state is a Fourier-invariant qunaught); the half turn that 49a1 spends in its Euler factor at 3
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

Each finite case has two readings (review S1). As a reduction it models the **local** level of an $L$-function over $\mathbb Q$: its zeros
are the poles of an Euler factor and RH there is Hasse–Deligne. As a global field (the function field of a curve, the graph with its prime
cycles, lane J's Dirichlet characters of $\mathbb F_q(t)$) its zeros are global and are eigenvalues of an integral step on a finite-rank $H^1$.
`lattice-tower.md` §7.3 (zeros as oscillator frequencies, the squeeze as the trivial pair) holds wherever the step group is discrete: the local level
over $\mathbb Q$ and the global level of function fields and graphs. It has no established counterpart at the global level over $\mathbb Q$, where
the step group is $\mathbb R_+^\times$ and the zeros appear as squeeze frequencies (lane C: in the CM case the oscillator frequencies are the local
angles $\theta_{\mathfrak p}$, the global zeros are squeeze frequencies, and there are no poles; *heuristic*). The question "what data for $\zeta$" is
what plays $H^1$ of the function field, with its integral step, for the global zeros, which is Deninger's demand that the identities be realised on
cohomology (`cit:deninger-conformal-metric`), now with the integrality made explicit.

## 4. The data for $\zeta$, item by item

In hand (*standard*, note §§1–10; inventory in `zeta-ingredients.md` §2): the qunaught $\Theta$ on the lattice $\mathbb Q^2\subset\mathbb A^2$; the product vacuum
$f_0$ (Gaussian at $\infty$, qunaughts at $p$); the squeeze group $C_{\mathbb Q}$ with its Mellin transform, each prime step with its exact adjoint; the
Fourier gate; Weil's functional $\omega$ with its explicit decomposition into two zero modes and local Lefschetz traces, a similitude form for every
step before RH; the functional-equation pairing of shard 04t on finite spans of zeros; the pole plane as the one negative direction of $Z_N\mp P_N$, Weil's windowed form $Z_N$ itself being positive (lane G, *checked* at 40–60
digits: inertia $(n-1,1,0)$, each off-line pair adds one); Connes's cokernel, an infinite-dimensional space with a squeeze flow, non-unitary on Connes's weighted space $L^2_\delta$, that sees only the
critical zeros.

Absent, by the ladder:

1. **A lattice with an integral step** whose Weil form is $\omega$. The code's own lattice $\mathbb Q^2$ cannot serve: it is rigid and divisible (G3); the principal squeezes $D_a$,
   $a\in\mathbb Q^\times$, preserve it with $(1-D_a)\mathbb Q^2=\mathbb Q^2$ but act trivially on $\Theta$ and are the identity of $C_{\mathbb Q}$, and the
   idele-class steps that carry the zeros do not preserve it at all (review S2a); so there is no logical space and no counts. In the curve case the
   lattice is not the code's lattice either: it is $H_1$ of a lift, or a Centeleghe–Stix object, and the code's trivial-character data do not even
   fix its class (lane A), nor do any of its product-stabiliser overlaps (lane F); the class is seen only by the Weil pairing, the commutator form
   of the theta group (an operator datum of the code, not an overlap). So the missing datum is not something the overlaps can be expected to
   contain; it is an integral structure on the cokernel on which the steps act. In the finite case the Weil pairing detects the class of such a
   structure; it does not create it.
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
   for the generator $F$ only). In a window the prime steps survive exactly as the Toeplitz shift (lane R, `window-similitude.md`, *checked*, 25/25): Weil's form is invariant
   under every translation $u\mapsto u+\log p$ before RH, so the Gram matrix of the translates $h(\cdot-j\log p)$ is Toeplitz (its entries are the echo
   $C_h(d\log p)$, the notebook's windowed Weil form; zero side against prime side to 13 digits for a Gaussian window), and the compressed step is an
   exact similitude on all but a fraction $O(\log p/L)$ of any window basis (exactly $1-\log2/L$ for a frame of translates). Lane G's residual near
   $0.4$ is that edge share in the Frobenius norm and decays roughly like $(\log p/L)^{1/2}$; the negative finding is withdrawn. What the prime steps
   lack is not similitude but a finite-rank integral structure: $\zeta$'s Toeplitz form has full rank on every window, one atom $\gamma\log p$ mod
   $2\pi$ per zero (Carathéodory–Toeplitz, from memory), where a curve's has rank $2g$, so there is no lattice for the shift to act on. So what $\zeta$ lacks is neither a symplectic partner for one step ($\Omega_p$) nor a form compatible with the whole family: $\Omega_{\rm FE}$ on zero
   spans and $\Omega_D=B(\cdot,D^{-1}\cdot)$ on the test algebra are compatible with every step (review S2b, checked for $a=2,3,5$ with an off-line
   quartet), and no understood family has one $\Omega$ for which a fixed form is every step's Weil form. What is missing is a reason for the
   family-invariant point $B$ to be positive; the Deninger metric cone of shard 04u remains the analogue of the cone, and that reason, ampleness
   through Rosati in the curve case, is for $\zeta$ the open statement itself.
3. **The local charged states and their gate phases** (lane I): a separate item of the ladder, present for Hecke and Dirichlet $L$-functions
   (Gauss sums at the conductor, the Hermite phase at $\infty$), trivial for a curve's zeta as a whole (root number $+1$, squeezes only), for graphs
   (the completed zeta is even) and for $\zeta$ (every phase is 1). Lane J (`ff-dirichlet.md`, *proved/checked* on six characters and a census of 532)
   supplies the finite case that has this item together with everything else: a Dirichlet character $\chi$ of $\mathbb F_q(t)$ modulo $f$ has a lattice
   $\mathbb Z[\zeta_N][F,V]$ with a similitude form from the functional equation alone, a positive Weil form, a vacuum, counts (the $\chi$-part of the
   Jacobian of $y^N=cf$), charged local states at the places dividing $f$ (and at $\infty$ for odd $\chi$), and gate phases $\chi_P(P)G_P/\sqrt Q$ whose
   product is the root number $W=(-1)^n\det F/q^{n/2}$; the phases of the $\chi^j$-parts of a cover multiply to 1, which is why a curve's own zeta shows
   none. So the gate phases coexist with the lattice and do not enter the positivity: the item is the first global invariant assembled from local
   data that is not a lattice or vacuum datum, and it does not carry RH. For Dirichlet $L$ over $\mathbb Q$ the only item missing is then the same one
   as for $\zeta$, the global lattice, with the charged local states present on both sides.
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
- One lattice, a family of steps (lane C). On $\mathcal O_K$ the Hecke steps $\psi(\mathfrak p)$ all commute with the one vacuum $J_K$, and their Weil
  forms for a fixed $\Omega$ are $\mathrm{Im}\,\psi(\mathfrak p)$ times the vacuum form: for a family containing a conjugate pair $\psi(\mathfrak p),\psi(\bar{\mathfrak p})$
  no orientation makes every Weil form positive, while with one step per split rational prime chosen with $\mathrm{Im}\,\psi>0$ one orientation makes
  them all positive (review S3b, checked for ten primes); either way each step's Weil form is definite, and none of this is RH. The family-invariant
  datum is the vacuum, or equivalently the Rosati form $\mathrm{Tr}_{K/\mathbb Q}(x\bar y)$ of the family's algebra, positive because $K$ is a CM field,
  which is RH for every local factor at once and says nothing about the global zeros.
- $\zeta$ (lane G). On the mode $\{\rho,\bar\rho\}$ (for a critical zero; $\{\rho,1-\bar\rho\}$ in general) the step $M_p$ rotates by $\gamma\log p$, so its $\Omega_{\rm FE}$-Weil form is $\sqrt p\sin(\gamma\log p)$
  times the vacuum form: indefinite for *each single* $p$, and no compatible $\Omega$ makes even the steps at 2 and 3 both positive (their signs
  disagree on 50.1% of the first 3000 zeros; review S3b). This is unlike the Hecke family (each step definite, lane M) and unlike the CM family. The
  understood analogue is the curve's step group: the generator $D$ has a positive $\Omega_{\rm FE}$-Weil form (weights $|\gamma|$), as $F$ has for
  $\Omega_+$, and the prime steps are large powers of it, as $F^2$ is of $F$ (lane E: $\tfrac12\Omega_+(F^2-V^2)$ is indefinite). Weil's form
  $B=\omega(h*\tilde h)$ is the family-invariant point ("vacuum point" means invariant under the whole family, in the evaluation normalisation;
  review G3), which is already registered as 04t `prop:weil-form-not-metric`(a, c) with `obs:deninger-same-gap` (lane O). So lane G's finding is the family version of lanes A and E, and it sharpens note §12.2 as
  follows (review S3c): the involution $h\mapsto\tilde h$ is positive for the Plancherel trace unconditionally; what Weil's criterion asks is that the
  functional $\omega$, the Lefschetz trace on "$H^1$", be a state on the squeeze $*$-algebra (`adelic-gkp.md` §10). **In the finite cases the positivity
  of the Rosati trace form comes from a polarisation (an ample divisor) and is carried by the lattice $H^1$; the CM field supplies that reason only
  for the local factors; for the global zeros of $L(\psi,s)$ it is as open as for $\zeta$.** The datum $\zeta$ lacks is a reason for that trace to be
  positive, and in every understood case with global zeros that reason is geometric and carried by the lattice, the item the ladder says $\zeta$ does
  not have. Checked: `checks/check_step_powers.py` (38 of 38 pass): $W_k=\tfrac12\Omega(F^k-V^k)$ is $q^{k/2}\sin(k\theta)\,G_J$ per mode, positive for $k=1$ and indefinite already at $k=2$ on the genus-two curve and on $K_4$ (for later $k$ it is definite or indefinite according to the signs of $\sin k\theta_j$); for $\zeta$ the normalised Weil form of $e^{tD}$ tends to $\oplus\gamma_n I_2$ as $t\to0$ and is indefinite for every $t>\pi/\gamma_{200}\approx0.008$ tested (grid to $t=10$), so for every prime step $\log p$ with $p<10^5$.

Checked: `checks/check_family_weil.py` (51 of 51 pass): the one-mode identity Weil form $=\sqrt q\sin\theta\,G_J$, its orientation dependence, the CM family's opposite signs on conjugate primes with one vacuum $J_K$ and the trace form a positive multiple of $G_{J_K}$, and the sign statistics of $\sin(\gamma\log p)$ over 200 zeros for $p=2,3,5$.

**Which families share a vacuum** (lane M, `family-vacuum.md`, *proved/checked*). Commuting similitudes of one $\Omega$ share a vacuum iff each is
semisimple with all eigenvalues of modulus $\sqrt q$, i.e. iff RH holds for each step (average over the compact closure; $J=-A(-A^2)^{-1/2}$); so for
a commuting family the shared vacuum is not extra data beyond one step's. Steps of different norms in the non-backtracking form $M_q=\bigl(\begin{smallmatrix}0&-1\\q&T_q\end{smallmatrix}\bigr)$
never commute ($[M_q,M_{q'}]$ has diagonal $q-q'$), and $M_{13}V_{17}$ for the LPS pair has real eigenvalues 13 and 17, so no $\Omega$ gives the
Hecke family of shard 04u a common vacuum, although each Hecke step has one. $\zeta$'s prime steps on the zero pairs commute, share $J$, and have
modulus $\sqrt p$ (*checked*, 50 pairs, $p=2,3,5$). So the finite shadow of $\zeta$'s family is the CM family and the function-field characters (lanes
C, J), families of complex multiplications in one structure, not the Hecke family on a graph, where each operator brings its own tree (*heuristic*).

**Semisimplicity and repeated roots** (lane S, `repeated-root.md`, *checked/proved*). Where the Frobenius polynomial has a repeated root (the Fermat
quartic $y^4=t^4+1$ over $\mathbb F_5$: $L_C=(1+2u+5u^2)^2(1-2u+5u^2)$, $J\sim E\times E'^2$ by Kani–Rosen) the Jacobian's lattice is semisimple ($F=\alpha I$ on
$\mathbb Z[i]^2$, principal form, Weil form $2I_4$, vacuum $-i$) while the companion construction of lanes A and J gives an order with $F-\alpha$ nilpotent,
a degenerate trace form and no definite Weil form for any compatible form. So the companion and cokernel constructions produce the geometric
lattice only for squarefree $P$; "RH with semisimplicity" is one condition on the geometric lattice; a repeated Frobenius eigenvalue costs nothing
geometrically and is seen by the group structures of the points, not by their counts. For $\zeta$ Weil's form weights a multiple zero by its
multiplicity and stays positive, a unitary realisation is automatically semisimple, and Connes's cokernel realises a multiple zero as a Jordan block
(`math/9811068:main.tex:949-952`), which makes it a construction of the companion type (*heuristic* as a reading).

## 4c. REFUTE reviews

- `notes/reviews/adelic-gkp-zeta-2026-10-06.md` (lane G and this page's §§3–4b): 6 VALID / 5 MINOR / 2 INVALID. Lane G's mathematics reproduces;
  both INVALIDs were this page's readings and are corrected above: "$\zeta$ lacks one $\Omega$ for the family" (false: $\Omega_{\rm FE}$ and $\Omega_D$ are
  compatible with every step) and "indefinite for every $p$, exactly as for the Hecke family" (false: Hecke steps are definite, a CM family can be
  oriented, $\zeta$'s cannot even for two primes). MINORs applied: the two readings of a finite case (§3); the principal squeezes versus the idele-class
  steps, $L^2_\delta$, $Z_N\mp P_N$, and "detects, does not create" (§4); the Plancherel versus Weil positivity (§4b); lane G's $\hat h$ normalisation and
  "vacuum point" meaning (annotated on `zeta-ingredients.md`).

- `notes/reviews/adelic-gkp-lattice-2026-10-06.md` (lanes A, E, F): 22 VALID / 6 MINOR / 0 INVALID; the three headline claims of §1 stand; the six
  precision faults are corrected above and annotated on the pages (the bridge lands on $\mathbb Z[F]$; the cone page's prime count; the general form of
  the vacuum/Weil-form equivalence needs "no real eigenvalue"; Frobenius compatibility in lane F's lemma; this page's §0).

- `notes/reviews/adelic-gkp-arithmetic-2026-10-06.md` (lanes B, C, D, I): 37 VALID / 3 MINOR / 1 INVALID; the four lane pages hold; the INVALID was
  this page's table row writing an isomorphism where `no-lift.md` says isogeny (corrected above: the $K_4$ fourfold is glued at 2, index $2^4$ over the
  product, which partly answers `no-lift.md` §2's open question); the MINORs: `zn-flux.md` Prop. 2.1(3) "charpoly $=P^2$" needs $N\ge3$ (squarefree at
  $N=2$); this page's "up to sign" is "at every $p\ne3$"; the phase at 7 is the normalised Gauss sum, the squeeze supplies the conductor. The reviewer
  recalls every "from memory" theorem the same way; the Centeleghe–Stix functor is contravariant.

- `citations-2026-10-06.md` (lane N): of 43 theorems quoted from memory on the ten pages, 28 are now byte-cited (`id:file:line`, verified byte-exact)
  against TeX sources on disk (six to the paper named, 22 to an arXiv paper restating a result whose own source is not on arXiv), 15 are cited
  bibliographically; new sources are listed in `refs/manifest-2026-10-06-pending.txt` for merging into `refs/fetch_sources.sh` and the manifest.
  Three discrepancies, annotated on the pages: 49a2 is not a twist of 49a1 (`cm-lift.md`); Connes's realisation lives in $L^2_\delta$, $\delta>1$, not
  $L^2$ (`zeta-ingredients.md`); Chai–Conrad–Oort: CM lifts need no field extension (`no-lift.md`). Settled: the Centeleghe–Stix functor is
  contravariant with a covariant version; Oswal–Shankar need odd $p$ and a simple variety, Bergström–Karemaker–Marseglia a squarefree Weil
  polynomial, so neither covers $K_5$.

- `notes/reviews/adelic-gkp-ff-family-2026-10-06.md` (lanes J, M): 14 VALID / 3 MINOR / 0 INVALID; lane M entirely VALID; lane J's "positivity is RH"
  needs $P_\chi$ squarefree (the Fermat quartic $t^4+1$ at $q=5$, $N=4$ has a repeated root, a degenerate $\Omega_+$ and no vacuum although RH holds);
  its minor table is of the trace form on the companion lattice; X6's phases are trivial and the $N=2$ lattice is $H_1$ up to isogeny. Annotated on the pages.

## 4d. Against the registered record (lane O, `registered-record.md`)

No registered claim is refuted or weakened (14 candidates tested, among them `thm:toral-frobenius-count`, `thm:lps-bass-frobenius`(c),
`thm:weil-positivity-finite`, `thm:kraus-weil-criterion`, `prop:weil-form-not-metric`(b)). Already registered: RH $\Leftrightarrow$ invariant vacuum (04q,
04t `thm:bond-positive-metric-criterion`, 04u, 04w/08c); the one-mode identity of §4b (04u's certificate $G=\tfrac12\Omega_B(F_1-V_1)$); "$B$ is the
vacuum point" (04t `prop:weil-form-not-metric`(a, c), `obs:deninger-same-gap`); lane E's genus-two numbers (04w); the gate-phase verdict
(`obs:spt-protection-is-sign-data`); "counts do not fix the lattice" (`cit:latimer-macduffee`, `cit:lenstra-structure`); 08b's trace Weil form on a
window of length $2g$ is twice the lattice Weil form of $\Omega_+$ (checked to $10^{-15}$). Out of date, not wrong: `obs:deninger-same-gap`'s "a canonical
$B$ only on the genus-one Hodge ket" (genus two now has principal forms, canonical only up to an infinite unit orbit). New relative to the record:
integrality as its own item, the orientation condition $\Phi_+$, the genus-$g$ bridge, "overlaps see the order, not the class", the CM
local-versus-global finding with the gate phases, shared vacua for families, lane G's prime-step analysis with $\Omega_D$. The page proposes 15 claim
rows and one definition and recommends one new shard (`04za_adelic_gkp_ladder.tex`) rather than extending 04t or 08b, since "Weil form" names the
trace form in 08b and $\tfrac12\Omega(M-V)$ here. Lanes B and D were not cross-checked; lanes J and M need their review before rows are written.

## 5. Corrections to earlier pages (recorded here; the pages carry a one-line annotation)

- `lattice-tower.md` §1 table and §6, `adelic-gkp.md` G12(ii): the Pauli-six lattice ($x^2+2x+5$, groups $\mathbb Z/8$) belongs to $y^2=x^3+4x\pm1$ over
  $\mathbb F_5$ ($j=1$), not to $y^2=x^3+4x$ ($j=1728$, End $=\mathbb Z[i]$, groups $\mathbb Z/2\times\mathbb Z/4$); shard 03c lists all three equations (lane A).
- The E mode lifts to 441d1; 49a1 reduces mod 2 to the $\mathbb F_2$-twist, step $-M$ (lane C). `cm-lift.md` §2.4: under the self-dual trace pairing the
  Fourier gate maps the $\ell=1$ Gaussian to $\ell=-1$, not to itself (lane I).
- `lattice-tower.md` §6, §9: "no lift" for the non-ordinary examples is "no canonical lift"; supersingular factors lift with Frobenius, not canonically (lane B).
- `lattice-tower.md` §7.3 is a reading of the local level only (lane C, §3 above).
- `zn-flux.md` §5 item 4 ("the finite rung has no non-self-dual character") holds for graphs, not for function-field characters: lane J's $N=3,4$
  examples have $L(\chi)\ne L(\bar\chi)$.
- `lattice-tower.md` §5: (i)$\Rightarrow$(ii) needs the CM type $\Phi_+$ for $\Omega$; it holds for the graph steps the page was written for and fails for
  $M'=\bigl(\begin{smallmatrix}0&1\\-5&-2\end{smallmatrix}\bigr)$ (RH, Weil form negative definite). General form: (i) $\Leftrightarrow$ (iii) $\Leftrightarrow$ the Weil form
  of some compatible form is positive (lane E).
- The lane B brief had $K_5$ at $q=4$ and the lane D brief had $K_4$ and the cube at $q=3$; all are 3-regular except $K_5$ (4-regular), so $q=2$ and $q=3$
  respectively, as the existing pages use.

## 6. Next

- Lane R settles lane G's two next items: $\Omega_D(h,g)=B(h,H*g)$ with $H*g$ the antiderivative, kernel $K=\sum_\gamma2\sin(\gamma x)/\gamma$ with $K'=$ Weil's
  distribution (prime part the weighted Chebyshev staircase), natural but no new datum; the smooth-window test is above. Remaining: the CM version of the
  vacuum-point reading. The REFUTE reviews of the arithmetic quartet and of the $\zeta$ pages (`notes/reviews/adelic-gkp-*-2026-10-06.md`) are to be folded in when they
  land. Lane J's open items: which lattice in the isogeny class is $H_1$ of the $\chi$-part and its polarisation ($\Omega_+$ is not principal); a twisted curve.
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
