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
| genus two over $\mathbb F_q$ | $\mathbb Z^4$ | Frobenius | yes | the forms with $M^TBM=qB$ form a cone; see `cone-bridge.md` | four | `cone-bridge.md` |
| CM Hecke $L(\psi,s)$, $K=\mathbb Q(\sqrt{-7})$ (441d1, 49a1) | one lattice $\mathcal O_K$ for every split prime | one step $\psi(\mathfrak p)$ per prime, all commuting | one $J_K$ for all primes: **local RH free** | the complex structure of $K\otimes\mathbb R$ | infinitely many, **not determined by the local data** | `cm-lift.md` |
| $\zeta$ | none known: $\mathbb Q^2$ is rigid and divisible (G3) | a flow (the squeeze group $C_{\mathbb Q}$), not an integral map | open (= RH) | none | infinitely many, all global | `adelic-gkp.md` §12 |

## 1. What determines what

Lane A's order for an ordinary elliptic curve (`curve-bridge.md` §6), extended by lanes B and C. Each arrow is a *standard* or *checked* fact.

1. **Counts.** The degree-resolved overlaps of the adelic qunaught with product stabiliser states, $\langle\Theta_K,1_D\rangle=q^{h^0(D)}$, give $N_k$,
   the Frobenius polynomial $P$, and with it the isogeny class, $\Omega$ up to scale, the Weil form, and $J$ up to scale. So the counts *decide* RH.
2. **The lattice.** $P$ does not determine $L$: at $q=7$, $a=2$ (discriminant $-24$, class number 2) two curves have the same counts, the same groups
   $E(\mathbb F_{7^k})$ for all $k\le24$, and non-isomorphic Deligne modules (*checked*, lane A). The trivial-character cokernel of Riemann–Roch gives only
   the principal class $\mathbb Z[F]$. Whether the divisor-resolved overlaps see the class is lane F's question (`overlap-data.md`).
3. **$\Omega$ on $L$**: the Weil pairing; fixed by $L$ up to Howe's sign $\varepsilon$. The sign flips $\Omega$ and the arithmetic $J_\varepsilon$ together, so
   $\Omega_\varepsilon(\cdot,J_\varepsilon\cdot)=\Omega(\cdot,J\cdot)$: the Riemann form is the vacuum form whichever $\varepsilon$ (*proved*, lane A).
4. **$J$ from the polarisation.** This step carries RH, and it is the one `adelic-gkp.md` §12 says has no analogue for $\mathbb Q$. Lane B adds that a
   canonical lift is not what supplies the lattice (the Centeleghe–Stix category does, from linear-algebra data with $FV=p$), and that on a
   supersingular block the arithmetic supplies no $J$ at all: there the vacuum is the step itself.
5. **The bridge is exact in genus one** (*proved*, lane A): the unimodular map $S=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ carries the
   Riemann–Roch cokernel state $(Y_j,Y_{j-1})$ of `analytic.md` §13 to the Deligne module, the window shift to $M$, the discrete Wronskian to $\Omega$, and
   the Casoratian (the cokernel metric, the Rosati form) to the Weil form: $\Omega(Ss,J\,Ss)=2\mathcal Q(s)/\sqrt{4q-a^2}$. So the two lattice pictures of
   the notebook (the adelic qunaught's cokernel and the GKP syndrome torus) are one object in genus one. In genus $g\ge2$ the similitude forms form a
   cone of dimension $g$ and proportionality is not forced: lane E (`cone-bridge.md`).

## 2. The negative findings that constrain the $\zeta$ side

Each is *checked* on its page; together they say where not to look.

- **The tower is blind** (`lattice-tower.md` §4): levels, codes, logical Cliffords and Lefschetz exist with or without RH.
- **Counts do not determine the lattice** (lane A): the datum that carries RH sits on a lattice that the trivial-character data of the code do not fix.
- **Local lattices and vacua do not determine global zeros** (lane C): 49a1 and 441d1 share $\mathcal O_K$, $J_K$ and every local step up to sign, and
  have different zeros; only 441d1 has a central zero (root number $-1$).
- **No arithmetic $J$ on a supersingular block** (lane B): where $\mu$ and $-\mu$ have equal valuation, Deligne's rule selects no CM type; positivity
  there is $\Omega(x,Mx)>0$, a statement about the step alone.
- **The lattice index is sign-blind** (`graph-ihara.md`): $|\det(m-nM)|$ carries no sign, so the count mechanism of curves does not transfer to a graph
  without flux.

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

In hand (*standard*, note §§1–10): the qunaught $\Theta$ on the lattice $\mathbb Q^2\subset\mathbb A^2$; the product vacuum $f_0$ (Gaussian at $\infty$,
qunaughts at $p$); the squeeze group $C_{\mathbb Q}$ with its Mellin transform; the Fourier gate; Weil's functional $\omega$ with its explicit decomposition
into two zero modes and local Lefschetz traces; Connes's cokernel, an infinite-dimensional space with a unitary squeeze flow that sees only the
critical zeros.

Absent, by the ladder:

1. **A lattice with an integral step** whose Weil form is $\omega$. The code's own lattice $\mathbb Q^2$ cannot serve: it is rigid and divisible (G3),
   the squeezes $D_a$ act on it as automorphisms with $(1-D_a)\mathbb Q^2=\mathbb Q^2$, so there is no logical space and no counts. In the curve case the
   lattice is not the code's lattice either: it is $H_1$ of a lift, or a Centeleghe–Stix object, and the code's trivial-character data do not even
   fix its class (lane A). So the missing datum is not something the code can be expected to contain; it is extra structure on the cokernel.
2. **A polarisation** on that lattice (note §12.2); in the finite cases this is where positivity comes from (ampleness, Rosati), and lane A shows it is
   the vacuum form transported, so "polarisation" and "vacuum" are the same datum seen from the two sides.
3. **Counts.** At the real place there is nothing to count (note §12.1); lane A shows that even where there are counts they fix only the isogeny
   class.

What the examples say about where the datum would have to sit (*heuristic*): on a global, integral, finite-rank-per-mode structure on Connes's
cokernel on which the squeeze acts as a similitude; not on the tower, not on the local data (lane C), not on the code lattice (G3). Lane C's open
list (`cm-lift.md` §4) states the three concrete versions of this: a lattice-with-step whose periodic-point counts give $L(\psi,s)$; an integral
structure on the $\ell=1$ cokernel of $\mathcal O_K$; a positivity uniform over the $\ell$-tower of Hecke characters.

## 5. Corrections to earlier pages (recorded here; the pages carry a one-line annotation)

- `lattice-tower.md` §1 table and §6, `adelic-gkp.md` G12(ii): the Pauli-six lattice ($x^2+2x+5$, groups $\mathbb Z/8$) belongs to $y^2=x^3+4x\pm1$ over
  $\mathbb F_5$ ($j=1$), not to $y^2=x^3+4x$ ($j=1728$, End $=\mathbb Z[i]$, groups $\mathbb Z/2\times\mathbb Z/4$); shard 03c lists all three equations (lane A).
- The E mode lifts to 441d1; 49a1 reduces mod 2 to the $\mathbb F_2$-twist, step $-M$ (lane C).
- `lattice-tower.md` §6, §9: "no lift" for the non-ordinary examples is "no canonical lift"; supersingular factors lift with Frobenius, not canonically (lane B).
- `lattice-tower.md` §7.3 is a reading of the local level only (lane C, §3 above).
- The lane B brief had $K_5$ at $q=4$; it is 4-regular, $q=3$, as the existing pages use.

## 6. Next

- The lane E and lane F results (cone in genus two; whether divisor-resolved overlaps see the lattice class) are to be folded in here when they land.
- A $\mathbb Z_N$ flux on a graph as the finite shadow of a Dirichlet family: lattice $\mathbb Z[\zeta_N]$, step, Hermitian Weil form, RH on average over the
  Brillouin torus (`gauge-groups.md`), and the data ladder for Dirichlet $L$ against it.
- The Fourier-gate phases (Gauss sums, Hermite phase) whose product is the root number; the GKP meaning of 441d1's forced central zero (lane C).
- A Howe-type positivity criterion for Centeleghe–Stix objects with supersingular factors; the Petersen twist (lane B).
- Before registering anything: the REFUTE review of `graph-ihara.md`, `graph-super.md` and the lane pages (HANDOFF T-b), and byte-citations once
  `refs/src/` is fetched.
