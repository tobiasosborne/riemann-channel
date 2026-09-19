# Notebook extract for the Ihara-zeta CCM-MVP plan

Extraction lane for `notes/zeta-spectral-triples/plan.md` (sections 5, 6.4). Every statement below
is copied verbatim (LaTeX as written) from `report/sections/*.tex`, with `file:line`. Status is the
**base** status stored in `db/claims.tsv` column 3. Where the shard's own `\claimstatus{id}{...}`
tag differs from the db by a `-conditional` suffix, that is *not* an inconsistency: per
`scripts/labbook_check.py` (rk-light rule, lines 120-155), the renderer appends `-conditional`
automatically whenever the claim's dependency closure includes an `assumed`-status row; the db
stores only the base status. This is noted inline wherever it occurs. Definitions live in
`db/definitions.tsv` (status `stipulated`), not `db/claims.tsv`; their status column is called out
separately.

---

## (a) Ihara zeta, Hashimoto operator, Ihara-Bass, trivial divisor, Ramanujan graphs

All core definitions are in `report/sections/02_definitions.tex` (§"Graphs"), status `stipulated`
in `db/definitions.tsv`.

**def:ihara-zeta** (`report/sections/02_definitions.tex:72-77`), stipulated
> For a finite graph $X$ with $\Ncount{\wl}$ closed non-backtracking walks of
> length $\wl$, $\zetaX(\uz) = \exp\big(\sum_{\wl}\Ncount{\wl}\uz^{\wl}/\wl\big)
> = \prod_{\pcycle}(1-\uz^{\wl(\pcycle)})^{-1}$.

**def:hashimoto-operator** (`report/sections/02_definitions.tex:79-85`), stipulated
> The \emph{Hashimoto} (non-backtracking edge) operator of a graph is the
> matrix $\Hash$ on directed edges with $\Hash_{ef} = 1$ when $f$ can follow $e$
> without backtracking; then $\Ncount{\wl} = \Tr\Hash^{\wl}$ and
> $\zetaX(\uz) = \det(1-\uz\Hash)^{-1}$.

**def:ihara-bass** (`report/sections/02_definitions.tex:87-94`), stipulated
> For a $(\qs+1)$-regular graph with adjacency matrix $\Aadj$ on $|V|$
> vertices and $|E|$ undirected edges, $\det(1-\uz\Hash) =
> (1-\uz^2)^{|E|-|V|}\det(1-\uz\Aadj+\qs\uz^2)$. Each adjacency eigenvalue
> $\lambda$ produces two eigenvalues $\edgeev,\edgeev'$ of $\Hash$ with $\edgeev\edgeev' = \qs$,
> $\edgeev+\edgeev' = \lambda$; the eigenvalue $\qs+1$ gives $\edgeev\in\{\qs,1\}$.

**def:ramanujan-graph** (`report/sections/02_definitions.tex:96-102`), stipulated
> A $(\qs+1)$-regular graph is \emph{Ramanujan} when every adjacency eigenvalue
> other than $\pm(\qs+1)$ satisfies $|\lambda|\le2\sqrt{\qs}$, the spectral
> radius of the universal covering tree. Equivalently all nontrivial $\edgeev$
> satisfy $|\edgeev| = \sqrt{\qs}$, which is the RH analogue for $\zetaX$.

**def:artin-ihara** (`report/sections/02_definitions.tex:104-111`), stipulated
> For a graph with a representation $\hol$ of its fundamental group assigned
> to closed walks (a holonomy), $\Lcurve(\uz,\hol) =
> \prod_{\pcycle}\det\big(1-\hol(\pcycle)\uz^{\wl(\pcycle)}\big)^{-1}$ ...

**def:quantum-hashimoto** (`report/sections/02_definitions.tex:170-180`), stipulated
> For superoperators $\Eop{1},\dots,\Eop{\Dk}$ on $\Vsp$ and a fixed-point-free
> reversal $\rev$ on $[\Dk]$, the \emph{quantum Hashimoto operator} is
> $\Hash$ on $\Wsp = \Vsp\otimes\mathbb C^{\Dk}$ ... It is the Artin--Ihara $L$-function
> of the bouquet twisted by $\hol = \Ad\circ\Un{}$.

**def:ramanujan-channel** (`report/sections/02_definitions.tex:162-168`), quoted (prov:hastings07-bound)
> A quantum expander is \emph{Ramanujan} when $\lamtwo\le\lamH$ ... $\lambda_H = 2\sqrt{D-1}/D$;
> in adjacency units, $\Dk\lamtwo\le2\sqrt{\Dk-1}$.

**Trivial divisor of a regular graph** — no separate labelled definition; stated in running prose,
`report/sections/08_quantum_ihara_general.tex:27-31` (shard RC-08, `sec:quantum-ihara`):
> Call $\pm1$ and the pair $\edgeev\in\{\qs,1\}$ from the adjacency eigenvalue $\lambda = \qs+1$ the
> \emph{trivial} eigenvalues of $\Hash$, everything else nontrivial. Then
> $\Ncount{\wl} = \qs^{\wl} + 1 + \sum_{\edgeev\ \mathrm{nontrivial}} \edgeev^{\wl} + (|E|-|V|)(1+(-1)^{\wl})$ ...

and again in `report/sections/07_deligne_via_graphs.tex:27-38`, same wording, plus:
> Since $\edgeev\edgeev' = \qs$, a pair either has both members of modulus $\sqrt{\qs}$ (when
> $|\lambda|\le2\sqrt{\qs}$ ...) or is real with one member larger. So all nontrivial $|\edgeev| =
> \sqrt{\qs}$ iff all nontrivial $|\lambda| \le 2\sqrt{\qs}$ iff the error in $\Ncount{\wl}$ is
> $O(\qs^{\wl/2})$: the Ramanujan property ... and the RH analogue ... are the same statement.

The general (Kraus-family) Ihara-Bass theorem and its corollaries, `report/sections/08_quantum_ihara_general.tex`, all status **proved**:

**thm:qihara-general** (`:65-79`)
> Let $\uz\in\mathbb C$ be such that $1-\uz^2\Eop{\bari{i}}\Eop{i}$ is invertible for every
> $i\in[\Dk]$. Then $\det_{\Wsp}(1-\uz\Hash) = \prod_{\{i,\bari{i}\}}\det_{\Vsp}(1-\uz^2\Eop{\bari{i}}\Eop{i})
> \cdot \det_{\Vsp}(1+\Dop-\Aop)$ ...

**cor:qihara-kraus** (`:81-98`)
> For arbitrary $\Kr{1},\dots,\Kr{\mpairs}\in\Mn$ ..., $\det_{\Wsp}(1-\uz\Hash) =
> \prod_k\det(1-\uz^2\Ad(\Kr{k}^\dagger\Kr{k}))\cdot\det(1+\Dop-\Aop)$ ...
> $\Tr_{\Wsp}\Hash^{\wl} = \sum |\Tr(\Kr{i_\wl}\cdots\Kr{i_1})|^2 \ge 0$ ...

**cor:qihara-unitary** (`:100-111`)
> If $\Eop{\bari{i}} = \Eop{i}^{-1}$ for all $i$ ..., then, with $\Sig = \sum_i\Eop{i}$,
> $\det_{\Wsp}(1-\uz\Hash) = (1-\uz^2)^{N(\Dk-2)/2}\det_{\Vsp}(1-\uz\Sig+(\Dk-1)\uz^2)$.

**cor:qihara-poles** (`:113-124`) — which factor carries the spectrum, poles bookkeeping.

**obs:rh-iff-ramanujan-channel** (`:288-299`), status **sketched**
> ... every nontrivial pole of $\zetaq$ lies on the circle $|\uz| = \qs^{-1/2}$ if and only if
> $\Dk\lamtwo\le 2\sqrt{\Dk-1}$, which is Hastings' bound $\lamH$ ...: the Riemann hypothesis for
> this zeta is exactly the statement that $\chan$ is a Ramanujan quantum expander.

**obs:rh-graph-ramanujan** (`report/sections/03_what_rh_has_become.tex:90-91` label; statement per `db/claims.tsv`), status **sketched**
> For a $(q+1)$-regular graph, Ihara's formula pairs each adjacency eigenvalue $\lambda$ with
> $\mu\mu' = q$, and RH for the Ihara zeta holds iff $|\lambda| \le 2\sqrt q$ for all nontrivial
> $\lambda$ (Ramanujan).

**obs:deligne-ingredients** (`report/sections/08_quantum_ihara_general.tex` — actually `07_deligne_via_graphs.tex:269-277`), status **sketched**
> Deligne's proof uses three ingredients that a Hilbert-Polya approach would have to replace:
> products, ...; slicing over a curve, ...; and the sign, .... It exhibits no Hermitian form and no
> operator.

**obs:abelian-obstruction** (`report/sections/07_deligne_via_graphs.tex:174-183`), status **sketched**
> Commuting holonomies produce uncontrolled invariants in tensor powers, exactly as commuting Kraus
> unitaries never give an expander ...

*Why it matters for a graph window construction*: (def:ihara-zeta/def:hashimoto-operator) give the
exact side-A/side-B pair `libzst`'s §6.4 atoms are built from (`Tr E^l`); (def:ihara-bass, the
trivial-eigenvalue passage in 07/08) gives the exact trivial divisor `{q,1}` (and `{-q,-1}` if
bipartite, plus $(|E|-|V|)$ copies of $\pm1$) that the plan's "trivial divisor as pole terms" must
reproduce; (thm:qihara-general, cor:qihara-unitary, obs:rh-iff-ramanujan-channel) are the
already-proved statements that let the plan claim the discrete Caratheodory-Fejer anchor is exact
rather than merely analogous.

---

## (b) Finite Weil form / Weil positivity for transfer operators (08b, 08c)

The underlying objects — trivial set, rescaled trace sequence, Weil form, reflection, mode-pairing
form, and the two Kraus pairings — are *defined* in `report/sections/02b_definitions_arithmetic.tex`
(status `stipulated` in `db/definitions.tsv`), not in 08b itself:

**def:rescaled-trace-sequence** (`02b_definitions_arithmetic.tex:233-246`)
> A \emph{trivial set} $\trivS$ is a sub-multiset of $\operatorname{spec}(X)$; the \emph{retained
> multiset} is $\retA = \operatorname{spec}(X)\setminus\trivS$ ... the \emph{rescaled trace sequence}
> is $\nuseq{\wl} = \critr^{-\wl}(\Tr X^{\wl} - \sum_{\edgeev\in\trivS}\edgeev^{\wl}) =
> \sum_{\edgeev\in\retA}(\edgeev/\critr)^{\wl}$ ...

**def:weil-form** (`02b_definitions_arithmetic.tex:248-258`)
> ... the \emph{Weil form} of $X$ is the Toeplitz form $\Wform(c) = \sum_{\wl,k}c_\wl\bar c_k
> \nuseq{\wl-k}$ ... The \emph{reflection in the critical circle} is $\reflJ(\edgeev) =
> \critr^2/\bar\edgeev$ ... the \emph{mode-pairing form} is $\Mform(c) = \sum_{\edgeev\in\retA}
> \fcpoly{c}(\edgeev/\critr)\overline{\fcpoly{c}(\reflJ(\edgeev)/\critr)}$.

**def:kraus-pairings** (`02b_definitions_arithmetic.tex:260-267`)
> A family $\Eop{i} = \Ad(B_i)$ ... is \emph{adjoint-paired} if $B_{\bari{i}} = B_i^\dagger$ and
> \emph{inverse-paired} if every $B_i$ is invertible and $B_{\bari{i}} = B_i^{-1}$ ...

**def:continuous-rescaled-trace** (`02b_definitions_arithmetic.tex:269-279`) — continuous analogue,
$\Fresc(\tsg)$, reflection in the line $\Rrefl{\alev}$.

Theorems, `report/sections/08b_weil_positivity.tex`, all status **proved**:

**thm:weil-positivity-finite** (`:50-56`)
> For any $X$, any $\trivS$ and any $\critr>0$, the sequence $\nuseq{\wl}$ is positive definite
> if and only if $|\edgeev|\le\critr$ for every $\edgeev\in\retA$, algebraic multiplicities
> included and zero eigenvalues allowed.

**thm:weil-duality-pairing** (the inflow identity) (`:72-79`)
> If $\retA$ is invariant under $\reflJ$ ..., then $\Wform(c) = \Mform(c)$ for every finitely
> supported $c$, and the following are equivalent: $\Wform\ge0$; $|\edgeev| = \critr$ for every
> $\edgeev\in\retA$; $\reflJ(\edgeev) = \edgeev$ for every $\edgeev\in\retA$.

**prop:weil-orbit-negative** (`:89-96`)
> ... a $\reflJ$-fixed mode $z$ of multiplicity $m$ contributes $m|\fcpoly{c}(z)|^2$ to $\Wform(c)$
> and a two-element orbit $\{z,\reflJ z\}$ contributes $2m\,\re(\fcpoly{c}(z)\overline{\fcpoly{c}(\reflJ z)})$;
> if any two-element orbit exists there is a $c$ with $\Wform(c)<0$.

**prop:weil-reciprocal-only** (`:102-110`) — reciprocal-only symmetry (no conjugation) is enough for
the circle equivalence, but not for $\Wform = \Mform$ without conjugation symmetry too.

**prop:kraus-conjugation-symmetry** (`:114-125`)
> For any family $\Eop{i} = \Ad(B_i)$ ... the antiunitary involution $x\mapsto x^\dagger$ ...
> commute[s] with $\Sig$ and with $\Hash$. Hence $\operatorname{spec}(\Sig)$ and
> $\operatorname{spec}(\Hash)$ are closed under complex conjugation with multiplicities.

**thm:kraus-inverse-pairing-duality** (`:133-144`) — inverse pairing gives functional equation:
> Let $\Eop{\bari{i}} = \Eop{i}^{-1}$ ..., $\Dk = 2\mpairs\ge4$, $\qs = \Dk-1$ ... The retained
> multiset after removing $\{+1^{[k]},-1^{[k]}\}$ has $2N$ elements, no zero, and is invariant under
> $\edgeev\mapsto\qs/\edgeev$ ...

**prop:kraus-both-pairings-unitary** (`:150-157`)
> $\Ad(B^\dagger) = \Ad(B)^{-1}$ iff $B^\dagger B = 1$ iff $B$ is unitary; a family is simultaneously
> adjoint-paired and inverse-paired iff every $B_i$ is unitary.

**thm:kraus-weil-criterion** (`:159-171`) — the Weil criterion for Kraus families:
> (i) For an adjoint-paired Kraus family ..., Weil positivity ... is exactly the one-sided bound
> $|\edgeev|\le\critr$ off $\trivS$ ... (ii) For unitary, adjoint-paired $B_i$ with $\Dk\ge4$,
> $\critr = \sqrt{\Dk-1}$ ...: Weil positivity holds iff every other eigenvalue $\lambda$ of $\chan$
> satisfies $|\lambda|\le2\sqrt{\Dk-1}/\Dk$ iff every retained mode is $\reflJ$-fixed.
> (Part (ii) is Hastings' bound recovered as Weil positivity.)

**prop:kraus-no-duality-example** (`:177-183`) — explicit adjoint-paired family with no duality
(retained spectrum invariant under $\edgeev\mapsto c/\edgeev$ for no nonzero $c$).

Continuous-time and Hilbert-Polya statements, `report/sections/08c_weil_positivity_continuous.tex`,
all status **proved** unless noted:

**thm:weil-positivity-continuous** (`:17-28`) — half-plane bound analogue of thm:weil-positivity-finite.

**thm:weil-line-duality** (`:30-40`) — continuous inflow identity, line version of thm:weil-duality-pairing.

**thm:cmps-ring-norms** (`:46-59`) — Dyson-expansion ring norms as continuous side A, nonnegative.

**prop:hp-inner-product-discrete** (`:72-79`)
> Let $\trivS$ be a union of full eigenvalue classes, $V'$ the sum of the generalised eigenspaces
> of the retained classes, $X' = X|_{V'}$. Then $X'$ is diagonalisable with all eigenvalues of
> modulus $\critr$ iff there is an inner product on $V'$ in which $X'/\critr$ is unitary.

**prop:hp-inner-product-continuous** (`:81-87`) — skew-adjoint realisation, continuous analogue.

**prop:weil-blind-jordan** (`:89-98`)
> For the Jordan block $X = \critr\begin{pmatrix}1&1\\0&1\end{pmatrix}$ with $\trivS=\varnothing$,
> $\nuseq{\wl}=2$ for all $\wl$ and the sequence is positive definite, although $X/\critr$ is not
> unitarisable ... Weil positivity holds with multiplicities and is blind to Jordan structure; a
> Hilbert-Polya inner product needs semisimplicity in addition.

**obs:huang-boundedness** (`:221-232`), status **proved**
> ... for a conjugation-closed retained multiset, the following are equivalent: positive
> definiteness of $\nuseq{\wl}$; boundedness; $|\nuseq{\wl}|\le\nuseq{0}$ for all $\wl$; and the
> termwise criterion ... For a connected non-bipartite $(\qs+1)$-regular graph with $\critr=\sqrt\qs$
> and $\trivS = \{+1^{[m-n]},-1^{[m-n]},\qs,1\}$ ..., Huang's sequence is exactly $h_k =
> \nuseq{0}-\nuseq{k}$ ..., so Huang's criterion is the boundedness form of Weil positivity.

**obs:kraus-dichotomy** (`:234-251`), status **proved** — the Kraus dichotomy:
> (a) For any $\Ad$-type family the rings are positive and $\operatorname{spec}(\Sig)$ and
> $\operatorname{spec}(\Hash)$ are conjugation-closed. (b) Inverse pairing buys the functional
> equation ... (c) Adjoint pairing buys Hilbert-Schmidt self-adjointness of $\Sig$, so
> $\operatorname{spec}(\Sig)$ is real for free; $\operatorname{spec}(\Hash)$ need not be real, and
> in general there is no functional equation ... (d) A family with both pairings is unitary ...
> Reality of $\operatorname{spec}(\Sig)$ is the Hilbert-Polya half; the functional equation is the
> other half; a Kraus family gets the two from two different pairings, and gets both only by being
> unitary.

**cit:herglotz-bochner** (`:175-187`), status **cited**
> A sequence is positive definite iff its Toeplitz matrices are positive semidefinite iff it is the
> Fourier coefficient sequence of a positive measure on the circle ...; a continuous positive
> definite function on $\mathbb R$ is the Fourier transform of a finite positive measure.

**cit:weil-criterion, cit:li-criterion, cit:huang-graph-criterion, cit:hastings-bound,
cit:suzuki-kernel, cit:pt-real-spectrum** (`:128-211`), all status **cited** — prior-art positivity
criteria; Huang's is explicitly the graph case (`report/sections/08c_weil_positivity_continuous.tex:152-157`).

*Why it matters for a graph window construction*: this is the notebook's own, already-proved,
finite-dimensional Caratheodory-Fejer/Toeplitz machinery — exactly what CCM's window construction
specialises to (plan.md §5 item 1, §6.4). `def:rescaled-trace-sequence`/`def:weil-form` are literally
CCM's `tau` restricted to a finite spectrum; `thm:weil-positivity-finite` is the discrete structure
theorem (positivity = one-sided spectral bound); `thm:weil-duality-pairing`/`obs:kraus-dichotomy`
tell the plan exactly which pairing (inverse vs adjoint) buys the functional equation versus reality
of the transfer spectrum, which is the graph-case fork the MVP needs to choose a convention for;
`prop:hp-inner-product-discrete`/`prop:weil-blind-jordan` are the exact finite analogue of CCM's
"the Connes-van Suijlekom theorem turns positivity into reality," including its failure mode
(Jordan blocks) that the graph case can exhibit on demand.

---

## (c) The graded divisor: definitions and propositions (02h, 03c)

Definitions, `report/sections/02h_definitions_graded_ramanujan.tex`, status **stipulated**:

**def:graded-transfer-channel** (`:19-47`)
> A \emph{graded transfer channel} is a graded lattice tensor $(\Kr{s})_s$ on $V=V_+\oplus V_-$
> with parity $P$ ... The \emph{graded divisor} is $\nu(\lambda) = m_0(\lambda)-m_1(\lambda)$, the
> difference of the algebraic multiplicities of $\lambda$ in the two sectors: $\nu>0$ are the poles
> and $\nu<0$ the zeros of the ring zeta $1/\sdet(1-\uz\Edb)$, and $\nu=0$ is invisible. The
> \emph{growth} is $\qs = \specrad(\Edb) = \specrad(\Esec{0})$ ... The \emph{trivial divisor}
> $\nu_{\mathrm{triv}}$ is a signed divisor, with multiplicities and parities, designated for
> structural reasons: $\qs$ (even, simple), its images $\zeta\qs$ under the period of $\Edb$ ...,
> the value $1$ as the designated $H^0$ partner of $\qs$ ..., the functional-equation partners of
> these ..., and, in the arithmetic cases, the archimedean or topological ladder. The \emph{retained
> divisor} is $\nu_{\mathrm{ret}} = \nu-\nu_{\mathrm{triv}}$ ...

**def:graded-rh-fe-ramanujan** (`:60-95`) — graded RH, functional equation, Ramanujan (two-sided),
manifest/Hilbert-Polya form, all stated on the divisor:
> (RH) \emph{One-sided (square-root cancellation):} every point of $\operatorname{supp}\nu_{\mathrm{ret}}$
> has $|\lambda|\le\sqrt\qs$ ... (FE) \emph{Functional equation:} the divisor form is
> $\nu_{\mathrm{ret}}(\qs/\lambda) = \nu_{\mathrm{ret}}(\lambda)$ ...; the stronger operator form is
> an even similarity $J$ ... with $J\Edb J^{-1} = \qs\Edb^{-1}$ ... (Ram) \emph{Ramanujan
> (two-sided):} every retained divisor point, even (pole) or odd (zero), lies on the critical circle.
> ... (HP) \emph{Manifest, or Hilbert-Polya, form:} on specified retained invariant sector subspaces
> there is a $\Gdb$-even positive definite form $G$ with $\Edb^\dagger G\Edb = \qs G$ ...

**def:graded-hashimoto** (`:114-124`)
> For unitary homogeneous letters $U_i$ ... the \emph{graded Hashimoto operator} is the operator
> $\Hash$ of \cref{def:quantum-hashimoto} on $B(V)\otimes\mathbb C^\Dk$ with $\Eop{i}=\Ad(U_i)$ ...
> The \emph{graded quantum Ihara zeta} is $1/\sdet(1-\uz\Hash) = \det(1-\uz\Hash_1)/\det(1-\uz\Hash_0)$
> ... The grading is \emph{balanced} when $D_+=D_-$.

Propositions, `report/sections/03c_graded_ramanujan.tex`, all status **sketched** (this whole section
is explicitly flagged "nothing here has had an independent (second-family) review", `:28`):

**prop:p-mode** (`:49-62`)
> $\Edb(P) = P\sum_s\epsilon_s\Kr{s}\Kr{s}^\dagger$. Under parity-twisted unitality ... $P$ is an
> even eigenvector with eigenvalue $\pmode$ ...The $P$-mode is structural but not trivial: for the
> elliptic tensor ... $\pmode=1$ (projective) or $0$ (affine) ...; for the Pauli letters below
> $\pmode=-2$ lies inside the Hastings band ...; for all letters odd $\pmode=-\qs-1$ is the period
> image of the fixed point (bipartite case). For unitary letters the Ramanujan property therefore
> imposes the \emph{balance condition} $|w_{\mathrm{even}}-w_{\mathrm{odd}}|\le\lamH$ unless
> $\pmode\in\trivS$.

**prop:no-ungraded-zeros** (`:72-83`)
> (i) For $P=1$ the two closures coincide and the ring zeta $1/\det(1-\uz\Edb)$ has no zeros; a
> quantum expander in the sense of def:quantum-expander (Hastings, Harrow, the Weil-LPS channels,
> the complexes) is such a channel. (ii) If every letter is even, the bond splits ... and both
> $1_+$ and $1_-$ are fixed: no unique fixed point. Zeros with a unique fixed point require odd
> letters, i.e. letters that anticommute with $P$. (iii) No nonzero positive operator is odd; odd
> fixed operators can nevertheless exist when the stationary state is not unique ...

**thm:graded-qihara-bass** (`:91-102`)
> For the graded Hashimoto operator ... with $\Sig_k = \Dk\chan|_k$, $n_0=D_+^2+D_-^2$ and
> $n_1=2D_+D_-$, $\det(1-\uz\Hash_k) = (1-\uz^2)^{n_k(\Dk-2)/2}\det(1-\uz\Sig_k+(\Dk-1)\uz^2)$,
> $k=0,1$, so the graded quantum Ihara zeta is $(1-\uz^2)^{-(\Dk-2)(D_+-D_-)^2/2}
> \prod_{\lambda\ \mathrm{odd}}(1-\lambda\uz+\qs\uz^2)/\prod_{\lambda\ \mathrm{even}}(1-\lambda\uz+\qs\uz^2)$,
> $\qs=\Dk-1$, and for a balanced grading the $(1-\uz^2)$ factors cancel exactly.

**cor:graded-band-circle** (`:110-125`)
> For a Hermitian graded channel ... each adjacency eigenvalue $\lambda$ of a sector gives two edge
> eigenvalues with $\edgeev_+\edgeev_-=\qs$, both of modulus $\sqrt\qs$ iff $|\lambda|\le2\sqrt\qs$.
> Hence: every point of the \emph{retained net} divisor of the graded quantum Ihara zeta lies on
> $|\uz|=\qs^{-1/2}$ iff $|\lambda|\le2\sqrt\qs$ for every $\lambda\notin\{\pm(\qs+1)\}$ with
> nonzero net multiplicity $m_0(\lambda)-m_1(\lambda)$. A bound on both entire sectors implies the
> divisor statement; the converse is false without a no-cancellation hypothesis (primitive
> degree-14 counterexample even $\{14,10\}$, odd $\{10,6\}$) ...

**obs:odd-gap-no-alon-boppana** (`:132-145`) — this is the "prop:graded-alon-boppana" named in the
task; its actual id in the shard is `obs:odd-gap-no-alon-boppana`:
> The drafted odd-sector analogue of Hastings' lower bound, $\specrad(\chan|_1)\ge\lamH-o(1)$, is
> false (prover, D5, refuted): the degree-four channel $\tfrac14(2\Ad1+2\Ad P)$ on $\mathbb C^{m|m}$
> has $\chan|_1=0$ for every $m$, and there are primitive degree-sixteen families with
> $\specrad(\chan|_1)=0$ and unbounded $m$. ... the odd gap has no universal lower bound, and
> "Ramanujan" for the odd sector is an upper bound (the band), not an optimality statement.

**prop:qubit-graded-zeta** (`:220-243`)
> For $\Dk$ unitary homogeneous letters closed under adjoint on $\mathbb C^{1|1}$, $\qs=\Dk-1$ ...
> $\operatorname{spec}\Sig_0=\{\Dk,\pmode\}$, $\Sig_1 = \binom{x\ y}{\bar y\ x}$ with eigenvalues
> $\lambda_\pm=x\pm|y|$, and $\dfrac{(1-\lambda_+\uz+\qs\uz^2)(1-\lambda_-\uz+\qs\uz^2)}
> {(1-\uz)(1-\qs\uz)(1-\pmode\uz+\qs\uz^2)}$ is the graded quantum Ihara zeta ... For the Pauli
> letters $\pmode=\lambda_\pm=-2$ ..., and the result is the zeta function of the elliptic curves
> $y^2=x^3+4x+b$, $b\in\{0,1,4\}$, over $\mathbb F_5$ (8 points, $a_5=-2$) ... The numerator is in
> general not integral ..., need not be a Weil polynomial, and an integral Weil numerator need not
> be a curve numerator.

*Why it matters for a graph window construction*: `def:graded-transfer-channel` is the notebook's
own general apparatus for "atoms plus a designated trivial divisor" that plan.md §6.4(c) explicitly
proposes reusing for graded/quantum graph windows; `def:graded-rh-fe-ramanujan`'s (HP) clause is
named directly in plan.md §5 item 3 as the object to compare against CCM's `xi`/`D'` construction;
`thm:graded-qihara-bass`/`cor:graded-band-circle` give the exact sector-by-sector Ihara-Bass and
band-vs-circle equivalence a graded graph window would need; `prop:no-ungraded-zeros` is a load-bearing
warning that *every* ordinary (ungraded) Ramanujan graph/expander in this notebook has a zeta with
*no zeros at all* — only poles — so a CCM-style zero-finding MVP on a plain Ramanujan graph is
vacuous unless a grading is added.

---

## (d) The finite letter-derived metric (03f) and its endpoint counterexamples

`report/sections/03f_selberg_letters_finite.tex`:

**thm:hashimoto-lift-metric** (`:54-82`), status **proved**
> Let $\mathcal V$ be a finite Hilbert space, $\Wsp$ its edge space, and $T=SR-J_0$ with $J_0^2=1$,
> $RS=\Sig=\Sig^\dagger$, $RJ_0S=\Dk\,1$, $\Dk=\qs+1>2$ ... Then $T$ is invertible, $\Sig R =
> R(T+\qs T^{-1})$, and for $\edgeev\ne\pm1$, $R\colon\ker(T-\edgeev)\xrightarrow{\sim}
> \ker(\Sig-(\edgeev+\qs/\edgeev))$ ... are inverse maps ($\pm\sqrt\qs$ is \emph{not} an exception).
> On the retained band $\Wsp_{\mathrm{band}} = \{Sf+J_0Sg\}$ over $\mathcal V_{\mathrm{ret}}$ (the
> $\pm\Dk$ modes removed), $L(f,g)=Sf+J_0Sg$ is an isomorphism with $L^{-1}TL = C =
> \binom{\Sig\ \qs}{-1\ \ 0}$, and the letter-derived metric $G_C = \binom{1\ \ \Sig/2}{\Sig/2\ \ \qs}$
> satisfies $C^\dagger G_C C = \qs G_C$; $G_C$ is positive definite iff the \emph{strict} band
> $|a|<2\sqrt\qs$ holds for every retained eigenvalue of $\Sig$, and then $T/\sqrt\qs$ is
> $G_C$-unitary on the whole algebraic band, with the operator functional equation $F_C =
> \binom{0\ \ \sqrt\qs}{\qs^{-1/2}\ \ 0}$, $F_C^2=1$, $F_CCF_C=\qs C^{-1}$, $F_C^\dagger G_CF_C=G_C$.
> At an endpoint $a=\pm2\sqrt\qs$ the companion matrix has a size-two Jordan block, so no positive
> form unitarises the full band ...

**thm:letters-derived-finite** (`:132-142`), status **proved**
> With [LETTERS] (incidence and reversal, or homogeneous adjoint-paired unitaries with the
> Hilbert-Schmidt form), [LIFT] (the non-backtracking exclusion and source-letter convention) and
> the finite spectral theorem: the identities of thm:hashimoto-lift-metric, Hermiticity of $\Sig$,
> the pushforward, the companion model, the metric $G_C$ and the operator FE follow; the optional
> sector bound [BOUND] puts the roots on the critical circle, and its strict version makes $G_C$
> positive on the entire retained algebraic band. This is the finite counterpart of
> thm:letters-derived-selberg, with no resonance or Poisson theorem needed.

**Endpoint counterexamples**, `num:selberg-letters` (`:147-165`), status **numerical**:
> $K_3\square Q_3$ is $5$-regular and Ramanujan with $-4$ of multiplicity two, and its Hashimoto
> matrix has $\dim\ker(T+2)=2$, $\dim\ker(T+2)^2=4$; the ten-letter Pauli channel
> ($I^{\times4},X^{\times4},Z^{\times2}$, $P=Z$, $\Dk=10$, $\qs=9$, even adjacency $\{10,2\}$, odd
> $\{6,-2\}$) is sector-Ramanujan with an odd Hashimoto eigenvalue $3$ of nullities $1,2$.

Also relevant, `thm:letters-derived-selberg` (`:112-126`), status **proved** (base; displayed
**proved-conditional** because its dependency closure includes assumed rows
`asm:dfg-resonance-theory`, `asm:selberg-zeta-entire`, `asm:selberg-coercivity` — see the note at the
top of this file) — the compact-Selberg analogue that thm:letters-derived-finite specialises from.

*Why it matters for a graph window construction*: this is exactly the graph-case Hilbert-Polya
metric plan.md §5 item 3 asks about ("how that form relates to the letter-derived metrics ... is a
question the finite cases can settle"); the endpoint counterexamples (Jordan blocks at
$a=\pm2\sqrt\qs$, i.e. at the Ramanujan boundary) are the finite, exactly-computable analogue of
what CCM's construction must avoid or handle at a multiple/boundary zero, and give the MVP concrete,
already-checked test graphs (`K_3 \square Q_3`, the ten-letter Pauli channel) with known Jordan
structure.

---

## (e) The zeta-conditions ledger C1-C10 and the four-letter elliptic tensors (06h)

`report/sections/06h_zeta_conditions.tex`. Whole section status **sketched**/**numerical**, explicitly
"unreviewed by a second family" (`:19`).

**obs:zeta-condition-ledger** (`:27-63`), status **sketched** — ten conditions C1-C10 stated as exact
algebraic statements on a graded lattice tensor / cMPS pair:
> (C1) $N_n = \sum_w|\Tr(\Pi\Kr{w})|^2\ge0$ is automatic; integrality is a separate arithmetic
> constraint ... (C3) Rationality is automatic; poles are net even, zeros net odd multiplicities ...
> (C4) FE: parity-preserving invariance of the reduced spectrum under $\lambda\mapsto q/\lambda$,
> giving $Z(1/(qu))=\pm q^{\chi/2}u^\chi Z(u)$ ...; for cMPS the symmetry is additive,
> $\lambda\mapsto\kappa-\lambda$. Correction to the reading of 08b: inverse-closed letters do
> \emph{not} give the FE for the raw doubled transfer ... (C5) RH: $|\lambda|^2=q$ on the retained
> odd spectrum; a sufficient mechanism is a positive metric $M$ with $\Edb|_-^\dagger M\,\Edb|_-=qM$
> ...; Weil positivity of the rescaled trace sequence gives $|\lambda|\le\sqrt q$ and reciprocity the
> equality ... (C6) Three separate requirements: a simple uncancelled Perron root $q$; a strictly
> positive even $h$ with $\mathcal E^\dagger(h)=qh$ ...; a one-dimensional fixed space ... (mixing;
> uniqueness alone allows periodic modes). (C7) A unitary $G$-action ... splits $\Edb =
> \oplus_\chi 1\otimes E_\chi$ ..., $Z=\prod L(u,\chi)^{\dim\chi}$ ... (C10) Exact embedding of a
> lattice channel in a cMPS needs $\Edb=e^{h\Tcm}$ with Choi conditional positivity ...

**prop:e0-pair-shift** (`:67-81`), status **sketched**
> Letters $\Kr{(a,b)}=\operatorname{diag}(1,[a=b])$ on $\mathbb C^{1|1}$ ... $N_n = m^{2n}-m^n$,
> $Z=(1-mu)/(1-m^2u)$: one pole at $1/m^2$, one zero at $1/m=q^{-1/2}$ (RH by half entropy), a
> genuine gas ..., no FE, no whole-bond channel gauge.

**prop:four-letter-elliptic** (`:83-100`), status **sketched-conditional** in text (`db/claims.tsv`
base is **sketched**):
> Let $E/\mathbb F_q$ have trace $a$ and Frobenius $\pi$, $\pi\bar\pi=q$; put $r\in\{0,1\}$ (affine,
> projective), $t=(q+r)/2$, $h=(q-r)/2$, and $\Kr{0}=\operatorname{diag}(\sqrt t,\pi/\sqrt t)$,
> $\Kr{1}=\operatorname{diag}(0,\sqrt{t-q/t})$, $\Kr{2}=\sqrt h|0\rangle\langle1|$,
> $\Kr{3}=\sqrt h|1\rangle\langle0|$. Then $\sum\Kr{s}^\dagger\Kr{s}=q\,1$ ..., the even spectrum is
> $\{q,r\}$, the odd spectrum $\{\pi,\bar\pi\}$, and the Ramond norm is $r+q^n-\pi^n-\bar\pi^n$: the
> point count of the affine ($r=0$) or projective ($r=1$) curve. For $r=1$: FE by the duality
> $J=\operatorname{diag}(1,-1)_{\text{even}}\oplus\text{swap}_{\text{odd}}$ with
> $J\Edb J^{-1}=q\Edb^{-1}$; RH because $\Edb|_-^\dagger\Edb|_-=q$; the normalised channel is mixing
> with the maximally mixed state as its unique fixed point ...

*Why it matters for a graph window construction*: C1/C3/C4/C5 are precisely the "atoms, kernel,
trivial-divisor, functional-equation, RH" checklist plan.md §6.4 wants applied factor-by-factor to
graph transfer operators, already worked out and numerically checked here for four concrete tensor
families (pair-shift, elliptic, Pauli — see (c)); the explicit warning under C4 ("inverse-closed
letters do not give the FE for the raw doubled transfer... the reciprocal quadratics arise in the
non-backtracking construction after the Bass factors are removed") is a correction the plan should
inherit verbatim, since it is exactly the subtlety a naive graph-window FE implementation would trip
over.

---

## (f) Caratheodory-Fejer, Toeplitz, Pisarenko, "window" in connection with finite transfer operators

Grep of `report/sections/*.tex` and `notes/**/*.md` (excluding `notes/zeta-spectral-triples/*`, which
is the plan's own working notes) for `Caratheodory|Carathéodory|Fejer|Fejér|Pisarenko|window`:

- **Caratheodory-Fejer / Fejer**: **no occurrence anywhere in `report/sections/*.tex` or in any
  established note** (`notes/extract`, `notes/reviews`, `notes/resonances`). The only occurrences in
  the whole repository are in `notes/zeta-spectral-triples/plan.md` itself and its sibling working
  files (`benchmark.md`, `report-2026-09-18.md`) and `docs/worklog/2026-09-17.md`. I.e. the
  Caratheodory-Fejer identification of finite Weil positivity with a discrete Toeplitz
  moment problem is **new to this sidequest**, not something the earlier notebook (08b/08c, before
  2026-09-17) already names, even though it proves exactly the underlying fact
  (`thm:weil-positivity-finite`, "positive definite iff... Toeplitz matrices positive semidefinite",
  `cit:herglotz-bochner`). `docs/worklog/2026-09-17.md:41-46` records this identification explicitly:
  > Structural reading for the programme: the construction is a machine from window explicit-formula
  > data (atoms, kernels, trivial divisor) to a self-adjoint operator with provably real spectrum; on
  > finite transfer operators it degenerates to Caratheodory-Fejer on Toeplitz matrices (exact once
  > the window exceeds the divisor size), and on the modular surface it would take prime geodesics
  > plus the cusp comb ... Recorded in `plan.md` Sections 5-6.

- **Pisarenko**: **no occurrence anywhere in the repository**, including plan.md. Not used by name
  anywhere; the notebook's closest object is the Weil form / Toeplitz-form machinery of 08b, which is
  the same underlying (finite atomic-measure-from-moments) mathematics as Pisarenko's harmonic
  decomposition but the notebook never names it.

- **"window"**: outside the plan's own files, "window" is used only for (i) the archimedean test
  function/window in the explicit formula (`01_conventions_notation.tex:112,121`;
  `02b_definitions_arithmetic.tex:42`; `04_riemann_channel.tex:168,208-212`, the `num:ringnorm-3000`
  Gaussian-window zero-sum check) and (ii) a Gaussian window on the Selberg/cusp side
  (`09c_selberg_tower_cusp.tex:114`). None of these is a *finite-transfer-operator* window in the
  Caratheodory-Fejer sense; they are all continuous test-function windows for the archimedean/prime
  sums of the ordinary or Selberg explicit formula. So there is **no prior "window" object for finite
  transfer operators** in the notebook before this sidequest — plan.md §6.4's `{-M..M}` window is a
  genuinely new construction for the graph/curve case, even though its positivity content
  (`thm:weil-positivity-finite`) is old.

*Why it matters*: confirms the plan is not duplicating an existing notebook construction when it
proposes `zst_weil_discrete` for graphs — the underlying positivity theorem is already proved
(item (b) above) but the finite-window-as-Caratheodory-Fejer framing, and any Pisarenko-style
reading, are net new and should be flagged as such rather than cited to a shard.

---

## (g) Artin-Schreier sign law and super-transfer matrix (06b)

`report/sections/06b_artin_schreier_super.tex`. All theorems here carry `\claimstatus{...}{proved-conditional}`
in the shard text; the `db/claims.tsv` base status is **proved** for all of them (deps include
`asm:normal-basis`, `asm:as-lpolynomial`, `asm:frobenius-semisimple`, `asm:weil-implementer-exact` —
this is the same base-vs-rendered-suffix situation noted at the top of this file, not an
inconsistency).

**thm:as-sign-law** (`:41-51`)
> For every $n\ge1$, including $\qs\mid n$, $\expsum{n}(g) = (-1)^{n-1}\,\dsign{n}\,\Tr\Tmat_g^{\,n}$,
> $\dsign{n} = \det(\cshift|_{\radn{n}})\in\{\pm1\}$, equivalently
> $\expsum{n}(g) = (-1)^{n-1}\dsign{n}\eta(-1)^{n-\dfix{n}}\Tr\Tmat_{-g}^{\,n}$.

**cor:as-periodic-sign** (`:71-83`)
> With $f(z)=z^\asrange\Ppoly{g}(z)$, $v_-$ its order of vanishing at $-1$ (always even) and $\hper$
> the period parameter: $\dsign{n}=1$ for $n$ odd and $(-1)^{\min(v_-,\,\qs^{v_\qs(n)})}$ for $n$
> even, so $\expsum{n}(g) = (1-2\cdot\mathbf1_{2\hper\mid n})\Tr\Tmat_g^{\,n}$. The claim
> $\alphaw{i}=-\lambda_i(\Tmat_g)$ ... holds for all $n$ iff $\Ppoly{g}(-1)\ne0$; the conjugated law
> $\expsum{n}=-(-\eta(-1))^n\overline{\Tr\Tmat_g^n}$ holds for all $n$ iff $\Ppoly{g}(-\eta(-1))\ne0$.

**prop:as-sign-counterexamples** (`:85-92`) — both drafted universal sign laws fail on explicit
$(\qs,g,n)$ examples (both endpoint criteria proved by these counterexamples).

**thm:as-frobenius-block** (`:112-123`)
> $\Lcurve(g,\uz)^\hper = \prod_{\omega^{2\hper}=1}\Dg{g}(\omega\uz)/\Dg{g}(\uz)^\hper$; ... the
> diagonal $\qs^\asrange\times\qs^\asrange$ matrix $\Fodd{g}$ with these multiplicities satisfies
> $\Fodd{g}\Fodd{g}^\dagger=\qs$, $\Lcurve(g,\uz)=\det(1-\uz\Fodd{g})$ and
> $\expsum{n}(g)=-\Tr\Fodd{g}^{\,n}$ for all $n$.

**thm:as-super-transfer** (`:133-144`) — the ring-norm-as-supertrace statement with the
$1+q^n-\sum\alpha^n$-type form:
> The projective curve $y^\qs-y=g(x)$ has one point at infinity; $\Ncount{n} = 1 + \qs^n +
> \sum_{a\ne0}\expsum{n}(ag)$ (additive Hilbert 90); $\Tr E_0^n = \qs^n$; and the super-transfer
> matrix $\Etr$ ... satisfies $\Ncount{n} = \str\Etr^{n}$ for all $n\ge1$. Its odd block $F$ has
> $FF^\dagger=\qs$, and its multiset is the $2g=(\qs-1)\qs^\asrange$ Frobenius eigenvalues with no
> even-odd cancellation ...

**thm:as-symplectic-map** (`:179-191`) and **cor:as-weil-bound-fixed-space** (`:193-202`) — the
transfer unitary is a Weil-representation operator implementing an explicit symplectic map; the Weil
bound is saturated iff that map has finite order dividing $n$.

*Why it matters for a graph window construction*: this is the notebook's other fully-worked finite
side-A/side-B pair with an exact sign law and an exact ring-norm-as-supertrace identity
($N_n=1+q^n-\sum\alpha^n$-shaped); it is the curve-side companion to the graph case in (a)/(e), and a
useful cross-check for the plan's §6.4(b) ("Artin-Schreier and elliptic curves") extension target,
since the sign/positivity bookkeeping here (odd block, $FF^\dagger=\qs$) is structurally the same
kind of object the graded-divisor apparatus of (c) formalises.

---

## Notation macros used above (from `db/notation.tsv`)

| macro | latex | meaning |
|---|---|---|
| `Hash` | $T$ | non-backtracking (Hashimoto) edge operator, classical or quantum |
| `zetaX` | $\zeta_X$ | Ihara zeta of a graph $X$ |
| `zetaT` | $\zeta_T$ | zeta function $\det(1-uT)^{-1}$ of a non-backtracking operator |
| `zetaq` | $\zeta_\Phi$ | quantum Ihara zeta of a unital channel with unitary Kraus operators |
| `Aadj` | $A$ | adjacency matrix of a graph |
| `qs` | $q$ | size parameter: field size, LPS prime, or $D-1$ for graphs/channels |
| `edgeev` | $\mu$ | eigenvalue of the edge operator $T$; pairs $\mu\mu'=q$ with adjacency eigenvalue $\lambda$ |
| `wl` | $\ell$ | length of a walk, word or prime cycle |
| `Ncount` | $N_{\#1}$ | closed non-backtracking walk count, or point count over $\mathbb F_{q^\ell}$ |
| `pcycle` | $P$ | prime cycle of a graph |
| `Dk` | $D$ | number of Kraus operators / bouquet degree, $D=2m$ |
| `Vsp`, `Wsp` | $\mathcal V$, $\mathcal W$ | vertex space, edge space $\mathcal V\otimes\mathbb C^D$ |
| `Eop` | $\mathcal E_{\#1}$ | $i$-th superoperator of a family |
| `Kr` | $A_{\#1}$ | $i$-th Kraus operator |
| `Sig` | $\Sigma$ | unnormalised transfer matrix $\sum_i E_i$ |
| `chan` | $\Phi$ | unital channel |
| `Ad` | $\operatorname{Ad}$ | adjoint action, $\operatorname{Ad}(A): X\mapsto AXA^\dagger$ |
| `rev`, `bari` | $\iota$, $\bar{\#1}$ | fixed-point-free reversal involution, reversed index |
| `lamtwo`, `lamH` | $\lambda_2$, $\lambda_H$ | second-largest eigenvalue; Hastings bound $2\sqrt{D-1}/D$ |
| `hol` | $\varrho$ | representation twisting a zeta (holonomy / Artin-Ihara twist) |
| `Lcurve` | $L$ | $L$-function (curve with coefficients, or Artin-Ihara) |
| `trivS` | $S_{\mathrm{triv}}$ | trivial sub-multiset of the spectrum |
| `critr` | $r$ | critical radius, $\sqrt{D-1}$ in the unitary Kraus case |
| `retA` | $\mathcal A_{\mathrm{ret}}$ | retained multiset $\operatorname{spec}(X)\setminus S_{\mathrm{triv}}$ |
| `nuseq` | $\mathsf n_{\#1}$ | rescaled trace sequence |
| `Wform` | $\mathrm W$ | Weil (Toeplitz) form |
| `Mform` | $\mathrm M$ | mode-pairing form |
| `reflJ` | $\mathrm J$ | reflection in the critical circle, $J(\mu)=r^2/\bar\mu$ |
| `Lgen` | $\mathcal L$ | Lindblad-type generator |
| `Fresc` | $\mathrm F$ | rescaled continuous trace |
| `Rrefl` | $\mathrm R_{\#1}$ | reflection in the line $\re\rho=a$ |
| `fcpoly` | $f_{\#1}$ | polynomial $\sum_\ell c_\ell z^\ell$ of a finitely supported coefficient vector |
| `Gdb` | $\Gamma_{\mathrm b}$ | doubled-bond parity $P\otimes\bar P$ |
| `Edb` | $\mathcal E_{\mathrm d}$ | doubled transfer matrix $\sum_s A_s\otimes\bar A_s$ of a graded lattice tensor |
| `pmode` | $r_P$ | $P$-mode eigenvalue under parity-twisted unitality |
| `specrad` | $\operatorname{rad}$ | spectral radius of an operator |
| `expsum` | $\mathcal S_{\#1}$ | exponential sum $S_n(g)=\sum_x e_q(\Tr g(x))$ |
| `alphaw` | $\alpha_{\#1}$ | Frobenius eigenvalues, $|\alpha|=\sqrt q$ |
| `dweight` | $c$ | pointwise weight scalar of a twisted coefficient system |
| `Tmat` | $E$ | transfer matrix of an MPS (Artin-Schreier transfer matrix is one instance) |
| `Frob` | $\mathrm{Fr}$ | Frobenius |
| `asrange` | $J$ | range of the quadratic Artin-Schreier polynomial |
| `dsign` | $\delta_{\#1}$ | radical sign $\det(\mathbb S|_{R_n})\in\{\pm1\}$ |
| `dfix` | $d_{\#1}$ | rank deficiency of the ring form |
| `Msymp` | $M_{\#1}$ | symplectic matrix implemented by the transfer unitary |
| `Weyl`, `Weil`, `Ugu` | $\mathrm X_{\#1}$, $W$, $\mathcal U_{\#1}$ | centred Weyl operator, Weil representation, transfer unitary $E_g/\sqrt q$ |
| `cshift`, `radn` | $\mathbb S$, $\mathcal R_{\#1}$ | cyclic shift / Frobenius in normal-basis coords; radical of the ring form |
| `ringnorm` | $\langle\Psi_{\#1}|\Psi_{\#1}\rangle$ | ring norm of the periodic $n$-site state, $=\Tr E^n$ |

---

## Grep of transcript and worklogs: "Ihara" and "Caratheodory"

`grep -n "Ihara" transcript/transcript.md docs/worklog/*.md` and
`grep -n "Caratheodory" docs/worklog/*.md` (only `2026-09-17.md` hits; no hits in `transcript.md`).

### 10-line summary of what TJO has said about the graph case as a test bed

1. The graph case entered as TJO's own steering move in the founding session: "the compression from
   big matrix to small matrix happens in one line" for Ihara's zeta, offered as the discrete sibling
   of Selberg's zeta with a genuine, checkable RH (`transcript/transcript.md:492`).
2. TJO had two small cubic graphs checked immediately for the Ramanujan property and Ihara zero radii,
   and asked for a non-Ramanujan cubic graph with explicit off-line Ihara zeros as a counterexample
   probe (`transcript/transcript.md:484-488`).
3. TJO pushed the graph case to the quantum setting the same session ("Verify a quantum Ihara-Bass
   determinant formula for a channel with unitary Kraus operators"), establishing RH ⇔
   Hastings-Ramanujan for channels as a direct graph-case generalisation
   (`transcript/transcript.md:586-600`; `docs/worklog/2026-09-11.md:35-37`).
4. TJO steered toward reading the Ihara-Bass compression as an MPS ring-norm identity ("the
   constrained ring norms are determined by the spectrum of the unconstrained transfer matrix... up
   to the trivial factor $(1-u^2)^{n^2(D-2)/2}$") and had it checked on AKLT/$K_4$
   (`transcript/transcript.md:650-652`).
5. TJO asked whether the quantum Ihara construction was new in the literature, prompting the prior-art
   review that produced `report/sections/09_prior_art.tex` (`docs/worklog/2026-09-12.md:55-74`).
6. TJO's sidequest of 2026-09-13 asked for an Ihara-type zeta for simplicial complexes, generalising
   the graph case one dimension up (`docs/worklog/2026-09-13.md:3-48`), which became shards 08d-08f.
7. TJO asked (2026-09-14/15) for a rigorous, continuum-stable Ramanujan definition "starting from the
   MPS picture" with "Harrow expanders as a test case," explicitly suspecting every known expander is
   ungraded — the question that produced `def:graded-rh-fe-ramanujan` and
   `prop:no-ungraded-zeros` (`report/sections/03c_graded_ramanujan.tex:12-17`).
8. Worklogs for 2026-09-15/16 record the graded quantum Ihara-Bass identity being proved sector by
   sector and checked on Pauli/PGL_2(F_p) Cayley-graph examples
   (`docs/worklog/2026-09-15.md:44-60`; `docs/worklog/2026-09-16.md:28-41`).
9. On 2026-09-17 (the CCM sidequest that produced `plan.md`), the graph/finite-transfer-operator case
   was explicitly named the "exact sanity anchor" for the Caratheodory-Fejer degeneration of the CCM
   window construction, with the identification "on finite transfer operators it degenerates to
   Caratheodory-Fejer on Toeplitz matrices (exact once the window exceeds the divisor size)"
   (`docs/worklog/2026-09-17.md:41-46`).
10. Across the whole run the graph case functions consistently as TJO's preferred *test bed*: the one
    setting where RH can fail or hold for computationally cheap, exactly-known reasons (a $4\times4$
    prism graph, a degree-14 Cayley graph, $K_3\square Q_3$), used repeatedly to falsify drafted
    universal claims (the Alon-Boppana analogue, the Artin-Schreier sign law, the Hashimoto-lift
    metric's endpoint) before they were allowed into the book as theorems.

---

## Cross-check note: base status vs. rendered `-conditional` suffix

Several shards display `\claimstatus{id}{X-conditional}` in the LaTeX while `db/claims.tsv` stores
only `X` in column 3 (e.g. all of 06b's `thm:as-*`/`cor:as-*` rows show `proved-conditional` in text
but `proved` in the db; `thm:letters-derived-selberg` shows `proved-conditional` in text, `proved` in
the db; `obs:modular-scattering-sector` shows `sketched-conditional` in text, `sketched` in the db).
This is **not** a data inconsistency: `scripts/labbook_check.py` computes the rendered status from
the base status plus a `-conditional` suffix appended whenever the claim's dependency closure (column
4, `deps`) includes a row of status `assumed` (rk-light rule, `scripts/labbook_check.py:120-155`).
The db intentionally stores only the base status; the plan should cite the `db/claims.tsv` base status
given above and, where relevant, note the assumed dependency by name (e.g. thm:as-sign-law depends on
`asm:normal-basis`; thm:as-super-transfer and friends depend on `asm:frobenius-semisimple`,
`asm:weil-implementer-exact`).
