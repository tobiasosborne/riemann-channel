# Lane L07: Selberg dictionary, resonances, Weil positivity

Compiled 2026-09-19 from the 2026-09-12 Selberg-dictionary campaign, the
"resonances" free-association lane, and the Weil-positivity campaign. This is a
ledger of *ideas and leads*, not a summary of the established mathematics. Line
numbers are the ones I read.

## Coverage

| file | lines | read fully? | ideas found |
|---|---:|---|---:|
| `notes/selberg-dictionary.md` | 34 | yes | 4 (all also appear below with deeper sources) |
| `notes/selberg/astra-brief.md` | 21 | yes | 9 (drafted statements, several later corrected) |
| `notes/selberg/astra-proofs.md` | 805 | yes | 18 |
| `notes/reviews/selberg-2026-09-12.md` | 408 | yes | 9 |
| `notes/resonances/astra-brief.md` | 19 | yes | 9 (TJO framing + seeds S1–S8) |
| `notes/resonances/astra-freeassoc.md` | 646 | yes | 34 |
| `notes/weil-positivity.md` | 112 | yes | 5 |
| `notes/weil-positivity/astra-brief.md` | 25 | yes | 7 (drafted statements, several later corrected) |
| `notes/weil-positivity/astra-proofs.md` | 986 | yes | 14 |
| `notes/reviews/weil-positivity-2026-09-12.md` | 436 | yes | 10 |

Total entries below: 81 (ideas that recur across files are merged into one entry
carrying all their source lines).

---

## Ideas and leads

### L07-001 Prime circles: a direct sum that has the prime comb but no zeros
- Source: `notes/selberg-dictionary.md`:32; `notes/selberg/astra-brief.md`:9 (task T1); `notes/selberg/astra-proofs.md`:47-101 (T1.2, T1.3)
- Raised by: TJO / orchestrator (Claude), from the "circle flows" paragraph of `docs/worklog/2026-09-12.md`
- Status at last mention: pursued, negative (registered; lab-book shard `report/sections/09b_selberg_dictionary.tex`)
- Content: Take one circle of circumference $\log p$ per prime and let the flow be rotation. Each circle's smeared trace is $\log p \sum_k \delta(t-k\log p)$ (Poisson), so the direct sum has positive-time orbital trace $\sum_{n\ge2}\Lambda(n)\delta(t-\log n)$ — exactly the prime comb. But the generator's spectrum is $\bigcup_{p\in S}(2\pi i/\log p)\mathbb Z$, which is precisely the *pole* set of the finite Euler product $\prod_{p\in S}(1-p^{-s})^{-1}$, and that product "has no zeros anywhere in $\mathbb C$".
- Lead: none stated beyond the negative conclusion — the moral drawn is that side A alone (a ring/orbit count) never produces side B; the zeros are a product of analytic *continuation*, an operation the finite construction does not perform. If one ever wanted this route back, the missing step is a non-commuting coupling between the circles.
- Related: L07-002, L07-003, L07-052, L07-054

### L07-002 The undamped prime comb is not tempered, and the infinite direct sum is not trace class
- Source: `notes/selberg/astra-proofs.md`:57, 63-73, 759, 783
- Raised by: codex prover (correction to the orchestrator's draft)
- Status at last mention: pursued, negative (a correction, registered in the T6.1 ledger item 2)
- Content: The smeared direct-sum operator has the constant mode on every circle with the same eigenvalue $\int h>0$, so it has a nonzero eigenvalue of infinite multiplicity: not compact, hence not trace class. And the comb extended by zero to negative times is *not tempered*, because $\sum_p \log p/(1+\log p)^N = \infty$ for every $N$ (the summands exceed $1/p$). At $t=0$ the orbital coefficient $\sum_p\log p$ diverges outright.
- Lead: the correct setting is local distributions on $(0,\infty)$, or a damped comb. This is the structural reason the Riemann channel's weights carry $n^{-1/2}$ and why the rate-$1/4$ damping of L07-015 is not cosmetic.
- Related: L07-001, L07-015

### L07-003 Zeros live only past the continuation; a finite prime construction is blind to them
- Source: `notes/selberg/astra-proofs.md`:97-99; `notes/resonances/astra-freeassoc.md`:473
- Raised by: codex prover
- Status at last mention: registered as a standing warning
- Content: "Passing to the infinite Euler product and analytically continuing is a different operation; the finite-prime calculation does not recover its zeros." The free-association note repeats it in the scattering language: the completed $S$ "is not a straightforward convergent product of the local inner $b_p$", and "a partial Euler product cannot be treated as a normal family converging to the continued inner function throughout that strip".
- Lead: any candidate mechanism must say where continuation happens. This is the criterion the free-association note uses to reject several candidates.
- Related: L07-001, L07-054

### L07-004 Lindbladian from the two non-compact $\mathfrak{sl}_2$ jumps is $-2\Delta$ on the $K$-invariant sector
- Source: `notes/selberg/astra-brief.md`:11 (T2); `notes/selberg/astra-proofs.md`:105-257 (T2.1-T2.3); `notes/selberg-dictionary.md`:18-27
- Raised by: TJO ("Lindblad from the vector fields on PSL, small operator = Laplacian")
- Status at last mention: registered, proved-here and reviewed VALID (shard 09b; independent sympy check in `scripts/selberg_lindblad.py`)
- Content: With $L_j=-iX_j$ the Heisenberg Lindbladian on multiplication observables is $-\frac12\sum_j[L_j,[L_j,\cdot]] = \frac12\sum_j X_j^2$. For $H=\mathrm{diag}(1,-1)$, $E=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$ the constant is exactly $c=1$: $\Omega f = y^2(F_{xx}+F_{yy})$ and $\frac12(H^2+E^2)f=2\Omega f=-2\Delta F$. The first-derivative terms $\pm4yF_y$ cancel between the two jumps.
- Lead: the continuous side B generator is a genuine dissipative sum of squares on the $K$-invariant sector, which is where the Selberg spectrum lives. What was never done: turn this into an actual completely positive semigroup with domains, or extract a gap from it (see L07-006).
- Related: L07-005, L07-006

### L07-005 The Casimir is *not* a Lindbladian off the $K$-invariant sector
- Source: `notes/selberg/astra-proofs.md`:201-207, 226-232, 785-786
- Raised by: codex prover (correction)
- Status at last mention: pursued, negative (correction registered, ledger item 4 and 5)
- Content: On all of $M=\Gamma\backslash G$ the identity is $\frac12(H^2+E^2)=2\Omega+\frac12 W^2$, not $2\Omega$. The compact direction enters $\Omega=\frac14(H^2+E^2-W^2)$ with a *minus* sign, so the quadratic symbol of $\Omega$ is indefinite and cannot be a scalar diffusion generator. In the representation version the two-jump generator is $2\Omega_{\pi\otimes\bar\pi}+\frac12 B_W^2$.
- Lead: none stated; the restriction to $Wf=0$ is mandatory. Anyone tempted to say "the Riemann Lindbladian is the Casimir" must carry the $B_W^2/2$ term.
- Related: L07-004, L07-006

### L07-006 Spectral gap from the decomposition of $\pi\otimes\bar\pi$ into irreducibles
- Source: `notes/selberg/astra-brief.md`:11 (T2c, "record as a remark (not a theorem)"); `notes/selberg/astra-proofs.md`:255 (Remark after T2.3)
- Raised by: orchestrator (Claude); hedged by the codex prover
- Status at last mention: raised, not pursued
- Content: The "quantum Lindbladian" of a unitary representation $\pi$ is the sum-of-squares operator of $\pi\otimes\bar\pi$ on Hilbert–Schmidt operators, so its spectral gap is governed by how $\pi\otimes\bar\pi$ decomposes. The prover's remark is deliberately deflationary: "The decomposition can involve parameters accumulating at zero; no positive gap follows just from writing a tensor-product Casimir", and the extra $B_W^2/2$ means the $K$-types and invariant vectors matter.
- Lead: supply the direct-integral and domain theory and ask what the $K$-types of $\pi\otimes\bar\pi$ actually do; if a gap in this decomposition could be tied to the $1/4$ property, that would be a representation-theoretic route to the continuous Ramanujan statement. Nobody tried.
- Related: L07-004, L07-005, L07-008, L07-044

### L07-007 The Selberg tower $D(\sigma)=\prod_{j\ge1}Z_{\rm Sel}(\sigma+j)$, and $\Lambda_{\rm fl}=+D'/D$
- Source: `notes/selberg/astra-proofs.md`:299-398 (T4.1); `notes/reviews/selberg-2026-09-12.md`:206-215 (C7); `notes/resonances/astra-freeassoc.md`:111-119
- Raised by: orchestrator (Claude) as task T4; sign corrected by the codex prover
- Status at last mention: registered, `conditional-on H-GEO, H-GUI` (shard 09c), reviewed VALID
- Content: Laplace-transforming the Guillemin flat trace and expanding $1/(4\sinh^2(x/2))=\sum_{m\ge0}(m+1)e^{-(m+1)x}$ gives the tower. Equivalently $D(\sigma)=\exp\left(-\int_0^\infty \frac{e^{-\sigma t}}{t}\mathrm{Tr}^{\rm flat}e^{-tX}dt\right)$, a flat dynamical determinant normalised to $1$ at $+\infty$. The orchestrator's drafted $-\partial_\sigma\log D$ was wrong by a sign (the minus belongs to $D^{-1}$).
- Lead: the tower is the continuous replacement for $\det(1-uT)$; the transverse Jacobian is what creates it and what the graph case lacks.
- Related: L07-008, L07-010, L07-013, L07-058

### L07-008 First band on $\mathrm{Re}\,\sigma=-1/2$ iff no Laplace eigenvalue in $(0,1/4)$ — the continuous Ramanujan statement
- Source: `notes/selberg/astra-proofs.md`:400-463 (T4.2), esp. 424-434; `notes/selberg-dictionary.md`:29-31
- Raised by: orchestrator (Claude), task T4(iv)
- Status at last mention: registered, `conditional-on H-GEO, H-GUI, H-LAP, H-SZ`, reviewed VALID (shard 09c)
- Content: $\mathcal B_0=\{-\frac12\pm ir_j : j\ge1\}$ is exactly the pole multiset of $\Lambda_{\rm fl}$ in the open strip $-1<\mathrm{Re}\,\sigma<0$, and it lies on the midpoint line exactly when there are no exceptional eigenvalues. This is the honest continuous counterpart of "Ramanujan iff RH for the Ihara zeta".
- Lead: the statement is an equivalence, not a proof that a given surface has the $1/4$ property — and, crucially, it is about the *discrete* Laplace spectrum, which for $\mathrm{PSL}(2,\mathbb Z)$ is Selberg's known $1/4$ and contains no RH. The Riemann zeros are on a different family (L07-029). This gap is the central obstacle the resonances lane was launched to attack.
- Related: L07-009, L07-029, L07-032, L07-044

### L07-009 The constant mode must be excised: $r_0=i/2$, the analogue of removing the trivial adjacency eigenvalue
- Source: `notes/selberg/astra-proofs.md`:434, 461, 789; `notes/reviews/selberg-2026-09-12.md`:77-80, 384-387
- Raised by: codex prover (correction to the brief)
- Status at last mention: registered (correction, ledger item 8)
- Content: "The assertion 'every $r_j$ is real' including $j=0$ is false on every compact connected surface." With $j=0$ the band contains $0$ and $-1$. The corrected property is the absence of *nonconstant* complementary-series parameters. The brief's exceptional range $ir_j\in(0,1/2]$ was also tightened to the open interval, since $\nu=1/2$ is the constant mode.
- Lead: the "trivial set" bookkeeping in the continuous case is the exact counterpart of the trivial set $S$ in the Weil-positivity theorems (L07-066, L07-068). Getting it wrong is the commonest failure mode in both lanes.
- Related: L07-008, L07-066, L07-068, L07-079

### L07-010 No continuous Ihara–Bass: there is no vertex-space determinant or quadratic operator relation for the flow
- Source: `notes/selberg/astra-proofs.md`:524 (T4.3 <1>4), 799; `notes/selberg/astra-brief.md`:15 (task T4(v))
- Raised by: orchestrator (Claude) asked for the comparison; codex prover recorded the negative
- Status at last mention: raised, not pursued (an explicit open item)
- Content: "Nothing in T4.1 alone constructs an analogous finite vertex-space determinant or proves a quadratic operator relation." On a $(q+1)$-regular graph, Ihara–Bass factors $\det(1-uT)$ through $1-uA+qu^2$ plus a topological factor; the continuous concrete identities obtained are only the tower, its shifted divisor, and $D(\sigma)/D(\sigma+1)=Z_{\rm Sel}(\sigma+1)$.
- Lead: find a continuous analogue of the vertex-space compression $1-uA+qu^2$. If it existed it would give the continuous "adjacency operator" whose Ramanujan bound is the target. Nobody attempted it.
- Related: L07-007, L07-011, L07-058

### L07-011 $D$ is a flat dynamical determinant, not a Fredholm determinant; the anisotropic resolvent was never constructed
- Source: `notes/selberg/astra-proofs.md`:388-396 (T4.1 <1>5), 413, 799
- Raised by: codex prover (scope discipline)
- Status at last mention: raised, not pursued
- Content: "It does not identify $D$ with an ordinary Fredholm determinant on $L^2(M)$ or construct an anisotropic-space resolvent. Those are additional assertions with additional analytic hypotheses." The closing audit lists as unestablished: "A literal operator-theoretic continuous Ihara–Bass compression, actual anisotropic resonant spaces, a full channel/scattering trace identity, and a proof of any Ramanujan/$1/4$/RH property".
- Lead: build the anisotropic space (Faure–Tsujii / Dyatlov–Zworski style) so that "resonance" means an eigenvalue of an actual operator. That is the step that would make side B an operator spectrum rather than a divisor.
- Related: L07-012, L07-028, L07-032

### L07-012 "Trace resonances" are deliberately not identified with Pollicott–Ruelle resonances
- Source: `notes/selberg/astra-proofs.md`:413; `notes/reviews/selberg-2026-09-12.md`:266-272 (C15)
- Raised by: codex prover; endorsed by the Opus reviewer
- Status at last mention: registered as a scope restriction
- Content: The prover defines "trace resonances" as poles of the continued $\Lambda_{\rm fl}$ and makes "no separate assertion about a chosen operator realization". The reviewer checked against Dyatlov–Faure–Guillarmou `1403.0256:181-191`: $\lambda_{j,m}=-m-1+s_j$ matches $\sigma=-1/2-k\pm ir_j$ identically, but DFG's theorem excludes $\mathbb C\setminus(-1-\frac12\mathbb N_0)$, so it says nothing about the integer points; "the author correctly declines to identify his trace resonances with Pollicott–Ruelle resonances".
- Lead: check the DFG hypotheses at the integer points; that is precisely where the constant mode and the topological zeros sit (L07-009).
- Related: L07-009, L07-011, L07-028

### L07-013 The Ruelle quotient $\zeta_R(s)=Z_{\rm Sel}(s)/Z_{\rm Sel}(s+1)$
- Source: `notes/selberg/astra-proofs.md`:483-491, 512-520 (T4.3); `notes/resonances/astra-freeassoc.md`:542-546
- Raised by: orchestrator (Claude), task T4
- Status at last mention: registered, proved-here (telescoping), reviewed VALID against byte-cited `1606.04560`
- Content: Telescoping the Selberg product over the shift gives $\zeta_R(s)=\prod_\gamma(1-e^{-s\ell_\gamma})$. The reviewer used this, plus $\mathrm{ord}_{s=0}Z=2g-1$, to confirm the whole trivial-zero normalisation $(2g-2)(2n+1)$ *and* the orientation convention.
- Lead: §14 of the free-association note wants to read this quotient as a *graded* cancellation (bosonic/fermionic determinants), which would make the tower collapse operator-theoretic.
- Related: L07-007, L07-021, L07-058

### L07-014 The cusp scattering term IS the prime comb — with dips $-\Lambda(n)/n$ and a $+1/2$ boundary constant from the pole of $\zeta$ at $1$
- Source: `notes/selberg/astra-proofs.md`:534-700 (T5.1), esp. 568-589, 660-677; `notes/reviews/selberg-2026-09-12.md`:190-204 (C5, C6)
- Raised by: TJO / orchestrator (task T5); constants and signs corrected by the codex prover
- Status at last mention: registered, `conditional-on H-PHI, H-ZETA, H-GAMMA`, reviewed VALID (shard 09c)
- Content: With $m(r)=-\frac12(\phi'/\phi)(\frac12+ir)$ one gets exactly $C=-P+A$, where the prime atoms are *dips* of weight $-\Lambda(n)/n$ at $t=\pm2\log n$ and $A(t)=\frac12-\frac1{4\sinh(|t|/2)}$ away from $0$. The $+1/2$ comes from $\mathcal F^{-1}(\pi\delta_0)$: the ordinary boundary value of $q(1+2ir)+q(1-2ir)$ differs from its Abel boundary distribution by $+\pi\delta_0$. "Treating both boundary Dirichlet series as ordinary convergent series and simply cancelling their poles would lose it."
- Lead: this is where — and *only* where — the primes of $\zeta$ enter the modular geometry. Every candidate mechanism in the resonances lane is measured against whether it uses this cusp term.
- Related: L07-015, L07-019, L07-020, L07-032, L07-042

### L07-015 The rate-$1/4$ damping identity, and exactly what it does not prove
- Source: `notes/selberg/astra-proofs.md`:702-746 (T5.2); `notes/selberg-dictionary.md`:31-32
- Raised by: orchestrator (task T5 corollary); scope corrected by the codex prover
- Status at last mention: registered; the damping of the *defined prime measures* is proved-here, the full-trace reading is corrected away
- Content: $e^{-t/4}P_{\rm ch,prime}(t)=P_+(t)=-(C-A)|_{(0,\infty)}$: multiplying the channel weights $\Lambda(n)n^{-1/2}$ at $2\log n$ by $e^{-t/4}=n^{-1/2}$ gives $\Lambda(n)/n$. But "the unqualified sentence 'the cusp term is the trace of the Riemann channel damped at rate $1/4$' requires both a subtraction/sign convention and a separately justified channel trace formula."
- Lead: to promote this to a real identity one needs a trace theorem for $Z_{\rm ch}(t)$ — which the Weil lane's T6 also flags as missing (L07-073, L07-074).
- Related: L07-014, L07-016, L07-073, L07-074

### L07-016 The notebook's §5 is out by a factor $-2$ and double-counts the damping
- Source: `notes/selberg/astra-proofs.md`:728-744 (T5.2 <1>3); `notes/reviews/selberg-2026-09-12.md`:291-300 (C18); `notes/reviews/weil-positivity-2026-09-12.md`:283-314 (X3), 344
- Raised by: codex prover (Selberg lane), independently confirmed by the Opus reviewer in both lanes
- Status at last mention: registered as a required correction to `report/sections/04_riemann_channel.tex` l.169-173
- Content: The prime part of $\mathrm{Tr}\,Z(t)$ is $-2\sum_n(\Lambda(n)/n)\delta(t-2\log n)$ on $t>0$; equivalently the centred trace has $-2\Lambda(n)n^{-1/2}$ at each $t=\pm2\log n$. The shard asserted $+\Lambda(n)n^{-1/2}$ and then applied the damping a second time. The reviewer confirmed numerically to six digits with 70 zeros. "The magnitude of the factor $2$ is variable-dependent — it is the Jacobian $dt=2du$ — so the shard must name its variable when it quotes the number. The sign is not convention-dependent: it is negative in every convention."
- Lead: fix the shard; more importantly, the negative sign kills the hope that the trace of $Z$ is literally a nonnegative Kraus ring count (side A) — endpoint, contact and archimedean terms are present too.
- Related: L07-015, L07-073

### L07-017 H-SZ's zero divisor and H-LAP have no byte-cited source
- Source: `notes/reviews/selberg-2026-09-12.md`:26-47 (M1), 69-80 (M3), 320, 403
- Raised by: Opus reviewer
- Status at last mention: raised, action item outstanding (blocks promoting T4.2 past `conditional-on`)
- Content: The extract has the Selberg *Euler product* verbatim but "no quote at all" for entireness on $\mathbb C$, the spectral divisor, the trivial divisor $(2g-2)\sum_n(2n+1)[-n]$, order $2g-1$ at $s=0$ and simplicity at $s=1$. Fix: cite Hejhal LNM 548 vol. I or Iwaniec GSM 53 Ch. 10 as named-not-quoted, or mark `[NOT FOUND]`.
- Lead: fetch or name-cite; the reviewer's mitigating consistency check (via $\mathrm{ord}_0\zeta_R=|\chi|=2g-2$) shows H-SZ is right, merely unsourced.
- Related: L07-021

### L07-018 H-GUI needs explicit Anosov/nondegeneracy and a measure-valued reading
- Source: `notes/reviews/selberg-2026-09-12.md`:49-67 (M2), 122-133 (M7), 354
- Raised by: Opus reviewer
- Status at last mention: raised, MINOR fix not yet applied
- Content: (a) Guillemin's theorem needs nondegenerate periodic trajectories and a wave-front condition for $\mathrm{tr}^{\rm flat}$ to exist; H-GUI as phrased "swallows both rather than stating them". (b) $e^{-\sigma t}$ is not compactly supported, so the Laplace pairing needs H-GUI read as an identity of locally finite *positive measures* on $(0,\infty)$, not merely in $\mathcal D'$.
- Lead: add the clauses; the author's own absolute-convergence bound already legitimises the strengthening.
- Related: L07-007

### L07-019 The continuous term of the modular trace formula carries an extra $(K_0/4)h(1/4)$ with $K_0=\phi(1/2)=-1$
- Source: `notes/reviews/selberg-2026-09-12.md`:102-120 (M6), 327
- Raised by: Opus reviewer, cross-checking `1108.5659:main.tex:2128-2129`
- Status at last mention: raised, not pursued (flagged as terminology, but the extra term is real)
- Content: $C=\mathcal F^{-1}m$ is only the *scattering-determinant* part of the continuous term. The quoted Momeni–Venkov form is $-\frac1{4\pi}\int(\varphi'/\varphi)(\frac12+ir)h(r^2+\frac14)dr + \frac{K_0}{4}h(1/4)$, and "the modular parabolic contribution carries further terms besides". Calling $C$ "the full cusp distribution" is loose.
- Lead: write down *all* the parabolic terms for $\mathrm{PSL}(2,\mathbb Z)$ before comparing the cusp distribution with any channel trace. The $h(1/4)$ contact term sits exactly at the rate the RH condition names, which nobody followed up.
- Related: L07-014, L07-015

### L07-020 An unclaimed confirmation: the $-1/2$ in $m$ *is* the trace-formula normalisation
- Source: `notes/reviews/selberg-2026-09-12.md`:114-120 (M6 "favourable check the author did not make"), 322
- Raised by: Opus reviewer
- Status at last mention: raised, recorded but not used
- Content: $-\frac1{4\pi}(\phi'/\phi)=\frac1{2\pi}m$, so $C_{MV}=\frac1{2\pi}\int m(r)\tilde h(r)dr=\langle\mathcal F^{-1}m,g\rangle$ with $g$ the Marklof/Momeni–Venkov transform. "So the author's $C$ is precisely the kernel of the continuous term against $g$ — an independent confirmation of the $-1/2$ that the file does not claim."
- Lead: this identification means the stipulated multiplier was not an arbitrary normalisation choice; it is the one the trace formula forces. Worth stating in the shard.
- Related: L07-014, L07-019

### L07-021 The orientation factor-2 trap, forced by $\mathrm{ord}_0\zeta_R=2g-2$
- Source: `notes/reviews/selberg-2026-09-12.md`:284-289 (C17), 40-47, 317
- Raised by: Opus reviewer
- Status at last mention: registered (a consistency check that pinned a convention)
- Content: The convention "opposite directions are not identified" is *forced*: with unoriented geodesics the trivial-zero multiplicity would be $(g-1)(2n+1)$ and $\mathrm{ord}_0\zeta_R$ would be $g-1$, contradicting the quoted $|\chi|=2g-2$.
- Lead: none stated; recorded so nobody "simplifies" the orbit index later.
- Related: L07-013, L07-017

### L07-022 The Selberg trace formula is deliberately *not* used as an input
- Source: `notes/selberg/astra-proofs.md`:776
- Raised by: codex prover (methodological)
- Status at last mention: registered
- Content: "The Selberg trace formula itself is not invoked as a separate input. H-SZ is a substantial standard theorem which is commonly proved using that trace formula; taking its conclusion as an explicit hypothesis does not reproduce its proof."
- Lead: the honest accounting means the continuous dictionary rests on the *divisor* of $Z$, not on the trace formula. If one ever wants a self-contained derivation, the trace formula is the shortcut that was deliberately declined.
- Related: L07-017

### L07-023 Numerical sanity checks are not reproducible from the repo
- Source: `notes/reviews/selberg-2026-09-12.md`:153-159 (M10); `notes/reviews/weil-positivity-2026-09-12.md`:138 (T3.5 process note)
- Raised by: Opus reviewer (both lanes)
- Status at last mention: raised, process issue outstanding
- Content: Both briefs asked for scratch scripts under `notes/<lane>/scratch/`; both prover files used "inline, non-writing Python", leaving those directories empty. The reviewer re-derived every quoted number independently and they are exact, so this is a process defect only.
- Lead: require scratch files, or the numbers cannot be re-run.
- Related: —

### L07-024 TJO's framing: RH as an extremal "Riemann quantum expander", and the refusal of general constructions
- Source: `notes/resonances/astra-brief.md`:5-7
- Raised by: TJO (quoted in the brief)
- Status at last mention: the governing frame for the whole resonances lane
- Content: "RH is a Ramanujan property, i.e. the existence of an EXTREMAL object, a 'Riemann quantum expander': a mixing transfer operator whose ring norms are exactly the prime measure, which has a duality (functional equation), and which is manifestly self-adjoint on some bond space; then Weil positivity puts all modes on the circle." The obstruction named: the zeros are *resonances* of the modular surface, not eigenvalues; the Riemann channel turns them into eigenvalues of $B=iA_0-\frac12|j\rangle\langle j|$ "at the price of Hermiticity". TJO: "now we are doing physics"; "we must be clear that no general construction will work, we must use the data we have" (the data: primes, the one cusp, the scattering phase, Hecke operators, Weil–LPS channels, Bost–Connes, the Gauss map / Mayer operator, the explicit formula).
- Lead: the operative test applied to every candidate below — *which of our data does it use?* — comes from this sentence.
- Related: every entry L07-025 to L07-065

### L07-025 One exit, correlated couplings: the Hermite–Biehler inverse construction and the exit Gram matrix
- Source: `notes/resonances/astra-freeassoc.md`:45-103 (§1), ranked 2nd at :28
- Raised by: orchestrator seed S2 (`astra-brief.md`:11), developed by the codex prover
- Status at last mention: partially explored (concrete numerics run in memory; proposed as script 16.2)
- Content: With $H_{\rm eff}=H-\frac i2 vv^*$ the secular equation is $1+\frac i2\sum_k|v_k|^2/(z-E_k)=0$; eigenvalues are *not* obtained by subtracting $i|v_k|^2/2$ once resonances overlap. Conversely, given any finite set of equal-width poles, write $P(z)=\prod(z-z_n)=U+iV$; Hermite–Biehler interlacing gives real roots $E_k$ of $U$ and positive residues $|v_k|^2=2V(E_k)/U'(E_k)$, and the matrix determinant lemma recovers $P$ as the characteristic polynomial of $H-ivv^*/2$. The mode geometry is a Cauchy Gram matrix $\langle u_n,u_m\rangle=2\sqrt{w_nw_m}/(w_n+w_m-i(a_m-a_n))$.
- Lead: "The new content would be an arithmetic formula for the spectral weights $|v_k|^2$ that forces the secular roots to have the same imaginary part." That is the concrete missing identity. Perturb the residues at fixed energies and watch the widths split — done in memory for 4 poles; never done with arithmetic residues.
- Related: L07-026, L07-027, L07-053, L07-062

### L07-026 Obstruction: no *bounded* change of metric on $K_S$ can exist (Riesz-basis / interpolating-sequence test)
- Source: `notes/resonances/astra-freeassoc.md`:103; numerics at :99; repeated at :137, :450, :602
- Raised by: codex prover
- Status at last mention: pursued, negative for the specific target (bounded renorming of $K_S$), open for a different completion
- Content: Under RH, fixed depth $w_0=1/4$ and increasing zero density force pairs of frequencies with arbitrarily small separation, so normalised kernel overlaps approach one; they "cannot be images of mutually orthogonal eigenvectors under one bounded, boundedly invertible similarity". Numerically the exit Gram condition number rose from $\approx9.88$ (first 24 ordinates) to $\approx701$ (last 24 of 3000), largest neighbouring overlap $0.570\to0.939$.
- Lead: the relevant standard check is the Riesz-basis/interpolating-sequence theorem for model-space kernels. "A new Hilbert–Pólya space could still exist, but an equivalent renorming of the entire physical model space is too strong a target." Also: $j$ is a boundary *form*, not necessarily a bounded vector, so $\sum w_n=\|v\|^2/2$ must not be passed to infinity without domain analysis.
- Related: L07-025, L07-053, L07-071

### L07-027 Correction: "GUE positions plus equal widths" is *not* uniquely the fingerprint of scalar loss
- Source: `notes/resonances/astra-freeassoc.md`:43, 77, 101
- Raised by: codex prover, correcting orchestrator seed S2 (`astra-brief.md`:11)
- Status at last mention: pursued, negative (the seed's inference is withdrawn)
- Content: The inverse construction of L07-025 realises *any* finite collection of equal-width, non-lattice poles with a one-port system. So equal widths with irregular positions do not force scalar loss. Also: scalar loss $B=-w_0I+iH$ means $B+B^*=-2w_0I$, which cannot be rank one in dimension $>1$ — "eigenvalue equality is much weaker than this operator identity".
- Lead: the special information therefore lies in the *couplings*, not in the width pattern. Redirects the question from "what makes widths equal" to "what arithmetic law fixes the residues".
- Related: L07-025, L07-046

### L07-028 Ruelle–Pollicott bands and a cohomological attenuation identity ($V=c+Xf$, Livšic)
- Source: `notes/resonances/astra-freeassoc.md`:105-137 (§2), esp. 123; ranked 6th at :30; seed S1 at `astra-brief.md`:10
- Raised by: orchestrator seed S1; the coboundary idea is the codex prover's
- Status at last mention: partially explored (a genuine mechanism for lines; the cusp extension is the missing step)
- Content: "If a weighted flow has potential $V=c+Xf$, multiplication by $e^f$ removes its nonconstant part. The attenuation accumulated on any periodic orbit is then exactly $c$ times its period." Livšic theory gives the standard test in compact hyperbolic settings. That would be an actual width mechanism — every mode loses the same amount per unit time — *if* it could be derived from the cusp return dynamics and supplied a usable Hilbert metric.
- Lead: test it on periodic continued-fraction words (L07-031). "One mismatch disproves that proposed periodic-orbit identity." What kills it: an unbounded coboundary destroys bounded similarity (L07-026).
- Related: L07-030, L07-031, L07-052

### L07-029 The modular scattering band would sit at $\mathrm{Re}\,\sigma=1/4-j$ — a different family from the compact Laplace band
- Source: `notes/resonances/astra-freeassoc.md`:119
- Raised by: codex prover (a sharp warning)
- Status at last mention: registered as an obstruction
- Content: For a scattering zero $s_*=\rho/2$ the tower bookkeeping puts $\sigma=s_*-j$, hence $\mathrm{Re}\,\sigma=1/4-j$ under RH. "This is a different family from the compact Laplace first band. It is not legitimate to replace one by the other."
- Lead: any use of the compact $1/4$-property theorems for the Riemann family is an error. The first literature question is whether $\rho/2$ are actual resonances of the scalar flow generator or "only appear in a related dynamical determinant after auxiliary factors and shifts" (:127).
- Related: L07-008, L07-012, L07-032, L07-041

### L07-030 Cusp return times are not constant: the unbounded roof is where the missing information lives
- Source: `notes/resonances/astra-freeassoc.md`:125
- Raised by: codex prover
- Status at last mention: raised, not pursued
- Content: "Constant curvature makes expansion uniform per unit geodesic time. It does not make cusp return times constant. Inducing the flow introduces an unbounded roof and boundary conditions, precisely where the missing information can reside."
- Lead: study the roof function of the cusp-return (Gauss map) suspension directly. This is the single sentence that connects §2 (uniform expansion) to §3 (Mayer) and explains why the naive band argument fails.
- Related: L07-028, L07-032, L07-033

### L07-031 A falsifiable test: integrated loss on periodic continued-fraction words
- Source: `notes/resonances/astra-freeassoc.md`:129-135
- Raised by: codex prover
- Status at last mention: raised, not run
- Content: Fixed-digit words have geodesic lengths $\ell_n=2\log\frac{n+\sqrt{n^2+4}}2$. Compare total attenuation divided by $\ell$ for words of lengths one, two, three. "One mismatch disproves that proposed periodic-orbit identity. Constant per-branch loss will fail because the roofs differ."
- Lead: cheap and decisive for any proposed coboundary; nobody ran it.
- Related: L07-028, L07-030

### L07-032 Mayer's transfer operator as the induced cusp-return operator — the top-ranked mechanism
- Source: `notes/resonances/astra-freeassoc.md`:139-189 (§3), ranked 1st at :25 and :41; seed S1 at `astra-brief.md`:10
- Raised by: TJO (the Gauss map / Mayer operator is in TJO's data list), developed by the codex prover
- Status at last mention: partially explored; explicitly the one the prover would pursue first
- Content: $(\mathcal L_s f)(z)=\sum_{n\ge1}(n+z)^{-2s}f(1/(n+z))$, with $Z_{\rm Sel}(s)=\det(1-\mathcal L_s)\det(1+\mathcal L_s)=\det(1-\mathcal L_s^2)$. The countable alphabet *is* the family of cusp excursions; the branch index $n$ is an integer, not a prime, and the primes enter only through the scattering determinant inside the global Selberg object. "The task would be to isolate the Eisenstein/cusp part of Mayer's determinant with its exact Hurwitz-zeta tail, then identify the boundary pairing induced on that part. This uses $ST^n$, the one cusp, and the actual scattering function together."
- Lead: see L07-034 for the programme and L07-035 for the implementable matrix. If it works it "would turn an abstract positive kernel into a boundary-energy identity".
- Related: L07-033, L07-034, L07-035, L07-036, L07-037, L07-061

### L07-033 The Mayer cusp tail: an exact Hurwitz-zeta expansion whose leading singular term at $s=1/2$ is rank one
- Source: `notes/resonances/astra-freeassoc.md`:164-174
- Raised by: codex prover
- Status at last mention: raised, not pursued (this is the sharpest concrete object in the whole lane)
- Content: For analytic $f$, $\sum_{n>M}(n+z)^{-2s}f((n+z)^{-1})=\sum_{\ell\ge0}\frac{f^{(\ell)}(0)}{\ell!}\zeta(2s+\ell,M+1+z)$. "The leading singular term at $s=1/2$ factors through $f(0)$, so its residue is rank one. The entire tail is not rank one. This distinction could connect one geometric exit with an infinite-dimensional return operator without inventing independent prime jump channels."
- Lead: this is the candidate identification of the Riemann channel's *rank-one* dissipation $|j\rangle\langle j|$ with an object that is arithmetically defined rather than postulated. Continue the tail exactly and read off the exit map.
- Related: L07-032, L07-034, L07-048

### L07-034 The programme: continue the tail, find the cusp boundary coordinate, Schur-complement it out, look for a positive centred pairing
- Source: `notes/resonances/astra-freeassoc.md`:162, 174, 588
- Raised by: codex prover
- Status at last mention: raised, not pursued — explicitly labelled "a plausible but unproved program"
- Content: "Continue the tail exactly, identify the cusp boundary coordinate, and ask whether the remaining Schur complement admits a positive centered pairing that can be computed from its coefficients. If this works, it would turn an abstract positive kernel into a boundary-energy identity. That is the prospective mechanism; the determinant identity itself is only a bridge." The place to look for the adjoint structure is "an adjoint identity involving orientation reversal, an Eisenstein pairing, and the cusp boundary form".
- Lead: the single highest-leverage unattempted item in this lane. Discipline attached: "Do not call a fitted positive matrix a natural pairing until its entries have a formula independent of the zero locations."
- Related: L07-032, L07-033, L07-035, L07-038, L07-053

### L07-035 Explicit Taylor-basis matrix entries for the Mayer operator
- Source: `notes/resonances/astra-freeassoc.md`:176-185
- Raised by: codex prover
- Status at last mention: derived, not implemented
- Content: In the basis $(z-1)^k$, $(L_s)_{mk}=\frac{(-1)^m}{m!}\sum_{\ell=0}^k(-1)^{k-\ell}\binom{k}{\ell}(2s+\ell)_m\,\zeta(2s+\ell+m,2)$, with $(a)_m$ the rising factorial. Directly implementable in mpmath; high precision needed for cancellations.
- Lead: compare Taylor sizes 12, 20, 32 near the first few $s=\rho/2$; track the $+1$ and $-1$ sectors and their near-null vectors; extract cusp evaluations and compare the local determinant divisor with $\phi(s)$.
- Related: L07-032, L07-061

### L07-036 Lewis–Zagier / Chang–Mayer period functions — the Eisenstein/resonance part is recorded as *memory*, unverified
- Source: `notes/resonances/astra-freeassoc.md`:187
- Raised by: codex prover, flagging a provenance hole
- Status at last mention: raised, literature check outstanding
- Content: "The named literature checks are Mayer's nuclear determinant theorem and the Lewis–Zagier/Chang–Mayer period-function correspondence, specifically its Eisenstein/resonance part and exceptional parameters. The worklog labels that latter identification as memory, so it remains to be checked."
- Lead: fetch and byte-check. The Eisenstein/resonance part of the period-function correspondence is exactly the sector that would carry the Riemann zeros; if the notebook's belief about it is wrong, the §3 programme changes shape.
- Related: L07-032

### L07-037 Warning: $\lambda_j(s)=\pm1$ is a spectral-parameter-dependent pencil, not the spectrum of one operator
- Source: `notes/resonances/astra-freeassoc.md`:160
- Raised by: codex prover
- Status at last mention: registered as a structural caveat
- Content: A zero of $\det(1-\mathcal L_s^2)$ solves $\lambda_j(s)=\pm1$, a nonlinear eigenvalue problem. "Passing to a suspension generator, or explicitly linearizing a return-time problem, is part of the resonance-to-transfer bridge."
- Lead: linearise the pencil (suspension generator) before claiming the Mayer operator's spectrum *is* side B.
- Related: L07-032, L07-030

### L07-038 Canonical systems, Krein strings and Suzuki's prime-defined screw kernel
- Source: `notes/resonances/astra-freeassoc.md`:191-240 (§4), ranked 3rd at :27; seed S4 at `astra-brief.md`:13
- Raised by: orchestrator seed S4 (TJO's "positive-mass prime string"), developed by the codex prover against the local TeX `refs/src/2206.03682/screwz_15.tex`
- Status at last mention: partially explored; the target of the §3 programme
- Content: $JY'(x,z)=z\mathsf H(x)Y(x,z)$ with $\mathsf H\ge0$ gives a self-adjoint boundary-value problem and a Herglotz Weyl function. Suzuki's intermediate object is concrete: with $g=-\Psi$, the kernel is $G_g(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u)$, $\Psi$ even with $\Psi(0)=0$, and global nonnegative definiteness is *equivalent* to RH. Under RH it is the Gram kernel of vectors with components $(e^{i\gamma t}-1)/\gamma$.
- Lead: "The physical opportunity is a local assembly law for this energy: a factorization, an increasing family of positive boundary energies, or a canonical-system reconstruction whose positive coefficients follow from arithmetic." Warning: off RH the "$\gamma$" in Suzuki's source can be complex — replacing them by imaginary parts of zeros silently assumes the conclusion.
- Related: L07-039, L07-040, L07-041, L07-063

### L07-039 Correction (seed S4 was false): positive local energy does *not* make the monodromy elliptic
- Source: `notes/resonances/astra-freeassoc.md`:43, 226-234
- Raised by: codex prover, correcting orchestrator seed S4
- Status at last mention: pursued, negative (explicit counterexample)
- Content: The seed hoped "positivity of the Hamiltonian is what makes a J-unitary monodromy similar to a unitary". False: take $\mathsf H_1=\mathrm{diag}(4,1/4)$, $\mathsf H_2=\mathrm{diag}(1/4,4)$, each of length $\pi/2$ at $z=1$; the transfer is $-J\mathsf H_j$ and the product is $\mathrm{diag}(-16,-1/16)$, off the unit circle. Periodic positive media still have forbidden bands. "The relevant positivity must belong to the spectral operator or its boundary response, not to an arbitrary spatial monodromy."
- Lead: the inverse-pairing/adjoint-pairing analogy of the Weil lane survives only with that distinction.
- Related: L07-038, L07-068

### L07-040 Two different inverse problems: passive realization of $S$ (free) vs positive realization of the centred $Q_\xi$ (RH)
- Source: `notes/resonances/astra-freeassoc.md`:206-212, 638
- Raised by: codex prover
- Status at last mention: registered; the second is classified a *rewriting*, not a mechanism
- Content: "A Cayley transform of the already-inner $S$ ... produces passive Herglotz data unconditionally. That construction cannot prove RH." Whereas $Q_\xi(z)=i\frac{\xi'}{\xi}(\frac12-iz)$ is Herglotz exactly under RH (Lagarias's criterion, via Suzuki's local source). "A positive canonical realization of this centered response is a much stronger statement than a passive realization of $S$."
- Lead: the distinction is the standing test for every "inverse scattering gives RH" proposal.
- Related: L07-038, L07-042, L07-064

### L07-041 Look for an arithmetic recurrence in the factors of the screw kernel as the interval crosses $\log p^k$
- Source: `notes/resonances/astra-freeassoc.md`:236, 629
- Raised by: codex prover
- Status at last mention: raised, not pursued
- Content: "Attempt a high-precision factorization and inspect how its coefficients change when the interval grows past $\log p^k$. The first useful discovery would be an arithmetic recurrence for the factors, not another numerical positive matrix." Expanded in §16.3: "study Schur complements as new prime-power breakpoints enter".
- Lead: this is the one proposed numerical experiment that could *discover* structure rather than confirm it — a Cholesky/Schur factorisation of the prime-defined kernel whose increments are indexed by prime powers.
- Related: L07-038, L07-063

### L07-042 Wigner time delay, the completion, and removal of the common width $1/4$
- Source: `notes/resonances/astra-freeassoc.md`:242-295 (§5), ranked 4th at :28; seed S7 at `astra-brief.md`:16
- Raised by: orchestrator seed S7, corrected and developed by the codex prover
- Status at last mention: partially explored; classified as a rewriting unless the removal's positivity has a prime-side cause
- Content: $q_S(x)=-\frac{d}{dx}\arg S(x)=4\mathrm{Re}\frac{\xi'}{\xi}(1+2ix)$, with each pole $a-iw$ contributing $2w/((x-a)^2+w^2)$. The completion matters: $S(x)=\frac{x+i/2}{x-i/2}\phi(\frac12+ix)$, so $q_S(x)=q_\phi(x)+\frac1{x^2+1/4}$ — "positivity of the completed model delay is not an unconditional positivity assertion for every convention of physical cusp delay". Under RH, $q_S=2\pi P_{1/4}*\mu$ and $\mu$ would be the density of states of a Hermitian system. Removing width $1/4$ is multiplication by $e^{|t|/4}$ in Fourier variables — "exponentially ill-conditioned", and at the singular origin it needs a specified regularisation.
- Lead: "Is there a physical quantity that is sensitive to the equality of widths and computable from the primes?" (TJO's seed question, still unanswered.) Concrete test: perturb an equal-width pole pair to $1/4\pm\epsilon$ keeping the functional-equation pairing, and search for a negative direction only after common-width removal.
- Related: L07-043, L07-063, L07-064

### L07-043 Suzuki's integrated kernel is the clean way to implement width removal on compact supports
- Source: `notes/resonances/astra-freeassoc.md`:282
- Raised by: codex prover
- Status at last mention: raised, not pursued
- Content: "Integrating twice and using Suzuki's kernel is a cleaner way to implement the same question on compact test supports" — i.e. instead of deconvolving $e^{|t|/4}$ against a distribution, work with $G_g(t,u)=\Psi(t)+\Psi(u)-\Psi(t-u)$ where the double integration has already regularised the origin.
- Lead: connects §5 (an observable) to §4/§16.3 (a computable prime-defined matrix). One sentence, never followed.
- Related: L07-038, L07-042, L07-063

### L07-044 Hecke: $t_p(\rho/2)$ is complex even under RH, so the continued cusp state cannot inherit self-adjoint Hecke action
- Source: `notes/resonances/astra-freeassoc.md`:297-327 (§6), esp. 303-317; ranked 5th at :29; seeds S6, S8 at `astra-brief.md`:15,17
- Raised by: orchestrator seeds S6/S8; the computation is the codex prover's
- Status at last mention: pursued, negative for the naive continuation — "the strongest available arithmetic rigidity, but currently acting on the wrong spectral sector"
- Content: On Eisenstein series $t_p(s)=p^{s-1/2}+p^{1/2-s}$, which on $s=\frac12+ir$ is $2\cos(r\log p)$. At $s=\rho/2$, even under RH, it is $p^{-1/4+i\gamma/2}+p^{1/4-i\gamma/2}$ — generically complex. "Thus the continued cusp state cannot simply inherit the original self-adjoint Hecke action in a positive Hilbert space."
- Lead: "A new boundary representation might have centered local parameters $p^{\rho-1/2}$ and their inverses. Under RH these are unimodular. To make this a mechanism one must construct that representation and its positive form from the cusp data, rather than assign the desired parameters to its spectrum." Cheap first check: evaluate $t_p(\rho/2)$ at the first few verified zeros for two primes. Literature: the Maass–Selberg relation and the normalised intertwining operator on principal series — "including what becomes of its positive form off the unitary axis".
- Related: L07-006, L07-045, L07-047

### L07-045 "Ramanujan for a lead": temperedness of the continuous spectrum is not a bound on continued-response poles
- Source: `notes/resonances/astra-freeassoc.md`:317-319; seed S8 at `astra-brief.md`:17
- Raised by: TJO/orchestrator (seed S8: "is there a notion of Ramanujan for the continuous spectrum / for a lead?"), sharpened by the codex prover
- Status at last mention: raised, definition still missing
- Content: Two questions must be distinguished. "Temperedness of the physical continuous spectrum is already a unitary representation statement. A resonance Ramanujan property would be a bound on poles of its continued boundary response, after a specified centering and subtraction of trivial factors. The first does not imply the second. A complete graph-with-leads definition would have to specify the coupling, scattering variable, trivial poles, and reciprocal pairing before stating a bound."
- Lead: write that definition. It is the missing vocabulary item that would let the Weil-positivity theorems (which need a declared trivial set $S$ and radius $r$) apply to an open system. Directly parallel to the $S$-bookkeeping problems of L07-009 and L07-079.
- Related: L07-009, L07-044, L07-047, L07-068, L07-079

### L07-046 Restraint on random-matrix language: Poisson vs GUE, and no prohibition of superradiance
- Source: `notes/resonances/astra-freeassoc.md`:101, 321; seed S6 at `astra-brief.md`:15
- Raised by: orchestrator seed S6; corrected by the codex prover
- Status at last mention: pursued, negative (the seed's "what forbids superradiance here?" has no answer in this framing)
- Content: "Poisson-like statistics of arithmetic Laplace spectra and GUE-like statistics of zeta ordinates are different conjectural statistical statements; Hecke commutativity alone does not prove the former. Nor does GUE-like zero spacing establish that a physical cusp cavity literally belongs to a time-reversal-broken ensemble. In particular it supplies no prohibition of superradiance." Also: calling every weak-coupling width law "Porter–Thomas" hides the symmetry distinction (complex Gaussian vs real-symmetric).
- Lead: none; recorded so the statistics are not used as evidence.
- Related: L07-027, L07-047

### L07-047 Attach a lead to a Weil–LPS Ramanujan graph and watch the widths
- Source: `notes/resonances/astra-freeassoc.md`:323, 327, 596-602
- Raised by: codex prover (concrete test for §6)
- Status at last mention: raised, not run
- Content: Take the Hermitian adjacency operator of a small Weil–LPS example, attach one vector $v$, form $H-i\eta vv^*/2$ as $\eta$ varies, and compare a basis-vector attachment, a symmetry-adapted attachment and a generic attachment. "The closed Ramanujan bound should survive as a statement about $H$, while the resonance widths generically vary and may segregate at strong opening." Related warning: "the notebook's $S,T,T^{-1}$ channels already warn that even the choice of modular generators does not automatically give the required Ramanujan bound."
- Lead: this is the cheapest experiment that would show *whether* opening a Ramanujan object preserves anything — i.e. whether "Ramanujan for a lead" can exist at all.
- Related: L07-044, L07-045, L07-062, L07-068

### L07-048 SHW renewal: exit at the cusp and reinsertion with an undetermined rebound state $\Omega$
- Source: `notes/resonances/astra-freeassoc.md`:329-367 (§7), ranked 7th at :31
- Raised by: orchestrator (from the Siemon–Holevo–Werner extract), developed by the codex prover
- Status at last mention: partially explored — "a genuine new transfer process, but its reinsertion state is undetermined"
- Content: $\mathcal L_\Omega(\rho)=B\rho+\rho B^*+\mathrm{tr}(j\rho j^*)\Omega$ with $\Omega\ge0$, $\mathrm{tr}\,\Omega=1$. The arrival density is $m_\Omega(t)=\mathrm{tr}(jZ(t)\Omega Z(t)^*j^*)$ and the feedback denominator is $1-\hat m_\Omega(\lambda)$. "The scalar exit does not determine $\Omega$." A resolvent calculation must track cancellations and modes not coupled to the reinsertion functional.
- Lead: "A distinguished arithmetic rebound state might make the renewal kernel satisfy a detailed-balance or reflection identity. ... Its missing input is precisely the rebound state and the reason for choosing it." Concrete test: build $\mathcal L_\Omega$ on the finite one-port model with three candidate $\Omega$ (maximally mixed, closed-energy eigenstate, coherent) and compare eigenvalues with the unchanged no-event poles.
- Related: L07-033, L07-049, L07-050, L07-056

### L07-049 The Bost–Connes critical measure diverges at *large* jumps — a new state space is needed, not small-jump compensation
- Source: `notes/resonances/astra-freeassoc.md`:355-361
- Raised by: codex prover
- Status at last mention: raised, not pursued (a sharp negative about the BC critical limit)
- Content: $\nu_\sigma=\sum_{p,k}\frac{p^{-k\sigma}}{k}\delta_{k\log p}$ has finite mass for $\sigma>1$; at $\sigma=1$ "its divergence is at arbitrarily large jump lengths; the lengths are bounded below by $\log 2$. This is not ordinary infinite activity from small jumps satisfying the usual Lévy integrability condition." Moreover $\zeta(\sigma-it)/\zeta(\sigma)\to0$ for fixed $t\ne0$ and $\to1$ at $t=0$: "no continuous probability characteristic function on the same real dilation group results. A critical completion therefore needs a new state space or compactification."
- Lead: this is a concrete structural fact about the BC threshold that the notebook's critical-KMS programme (the "BC reframe") has to face. Test escape of mass and tightness *before* any spectral conjecture.
- Related: L07-048, L07-056

### L07-050 Jump-gauge freedom; a formal trace-preserving reinsertion rule is not a conservative semigroup
- Source: `notes/resonances/astra-freeassoc.md`:353
- Raised by: codex prover (two caveats to "today's informal discussion")
- Status at last mention: registered as a caveat
- Content: "Jump representations have gauge freedoms, including dynamically trivial scalar jumps; the useful negative statement is that adding genuine reinsertion changes the no-event map, not that every displayed nonzero Kraus term must visibly mix every state." And: "in an unbounded problem, a trace-preserving formal reinsertion rule is not by itself a proof that the minimal semigroup is conservative for all times. Explosion and domains are exactly SHW's point."
- Lead: none stated; guards against over-reading the jump structure of the Riemann channel.
- Related: L07-048

### L07-051 Feshbach reduction and complex scaling — and the misleading Mellin association in seed S3
- Source: `notes/resonances/astra-freeassoc.md`:369-390 (§8), esp. 384; ranked 12th at :36; seed S3 at `astra-brief.md`:12
- Raised by: orchestrator seed S3; corrected by the codex prover
- Status at last mention: pursued, negative as a width mechanism — "excellent bookkeeping for resonances; does not align widths"
- Content: $H_{\rm eff}(z)=PHP+PHQ(z-QHQ)^{-1}QHP$. The correction: in the cusp coordinate $r=\log y$, the map $y\mapsto e^{i\theta}y$ is $r\mapsto r+i\theta$, a complex *translation*, "not automatically the exterior rotation $r\mapsto e^{i\theta}r$ that rotates the kinetic continuous spectrum. Analytic dilation of an operator family, continuation in a spectral Mellin variable, and continuation in BC inverse temperature are three different operations."
- Lead: if wanted, derive the outgoing boundary form for the zero Fourier mode in $r$ and check the Laplace-to-wave-to-$\tau$ parameter changes; the named theorem is Aguilar–Balslev–Combes or an exterior-complex-scaling theorem *for cusp ends* — "the Euclidean theorem cannot simply be quoted with no cusp hypotheses". What kills it: "Complex scaling exposes existing poles and does not move them onto a new line."
- Related: L07-049, L07-064

### L07-052 Isochronous loops: $T=rU$ gives equal widths for *any* unitary $U$ — one exit is not itself an obstruction
- Source: `notes/resonances/astra-freeassoc.md`:392-415 (§9), ranked 8th at :32
- Raised by: codex prover
- Status at last mention: partially explored — "exact physical examples; their required equalities are absent from the prime circles"
- Content: A circle of length $L$ with return factor $r$ has $\lambda_n=(\log r+2\pi in)/L$, so $\mathrm{Re}\,\lambda_n=\log|r|/L$ for every mode, whatever the eigenphases. "This is a genuine one-port equal-width mechanism... The circle example proves that one exit is not itself an obstruction." For a network the requirement is that every periodic trajectory have the same integrated loss divided by travel time — the elementary counterpart of the §2 coboundary.
- Lead: "The useful possibility is that the arithmetic return dynamics admit exactly such a cohomological attenuation identity, even though it is hidden in physical coordinates." Test: an equilateral quantum graph with $\det(1-re^{ikL}U)=0$, then perturb; for prime circles impose $|r_p|=e^{-w_0L_p}$. "Then compare the resulting determinant's divisor with $\xi$. This last check matters more than the easy width check."
- Related: L07-001, L07-028, L07-031

### L07-053 PT symmetry / Krein signature: look for $K^*G=GK$ with $G>0$
- Source: `notes/resonances/astra-freeassoc.md`:417-450 (§10), ranked 9th at :33
- Raised by: codex prover (connecting to the Weil lane's T5)
- Status at last mention: partially explored — "identifies the symmetry-breaking question; no arithmetic inequality supplied"
- Content: Centre $C=B+w_0I$, $K=-iC$. If $K^*G=GK$ with $G>0$ then $K$ is self-adjoint in that metric; an indefinite $G$ only gives a Krein space where complex eigenvalues are allowed. The elementary model is $K=\begin{psmallmatrix}ig&t\\t&-ig\end{psmallmatrix}$ with $\mathrm{spec}=\{\pm\sqrt{t^2-g^2}\}$: symmetric for all $g$, real only for $|g|\le|t|$, and at the threshold there is a Jordan block — "precisely why semisimplicity matters in the notebook's theorem".
- Lead: "The missing physics would be an arithmetic bound that prevents the relevant signatures from colliding, or directly makes the boundary form definite." Test: solve $K^*G=GK$ on finite sections of a candidate centred cusp operator, ask whether the solution cone contains a positive matrix, and track the best achievable condition number against cutoff. Discipline: "A numerical positive solution obtained only after fitting known critical zeros has no evidentiary value; the relevant input is a prime- or branch-defined operator."
- Related: L07-026, L07-069, L07-071

### L07-054 Correction: the local Euler factor $R_p$ is *not* inner — it has poles on $\mathrm{Im}\,\tau=-1/2$
- Source: `notes/resonances/astra-freeassoc.md`:452-495 (§11), esp. 456-473, 485-493; ranked 10th at :34; seed S5 at `astra-brief.md`:14
- Raised by: orchestrator seed S5; refuted by the codex prover with numerics
- Status at last mention: pursued, negative (the seed's "local inner factors" picture is withdrawn)
- Content: With $u_p=e^{-2i\tau\log p}$, $a_p=p^{-1}$, the actual local factor in the zeta-phase ratio is $R_p(\tau)=\frac{1-a_pu_p}{1-a_p/u_p}=u_p/b_p(\tau)$ with $b_p=\frac{u_p-a_p}{1-a_pu_p}$ inner. "$R_p$ is not inner and instead has poles there." Direct check at $p=2$, $\tau=-iy$: $|R_2|=2.207,\,54.22,\,53.97$ at $y=0.25,0.49,0.51$ while $|b_2|=0.320,\,0.0093,\,0.0091$.
- Lead: "A genuine noncommuting transfer chain might replace the scalar factors by matrices whose boundary determinant has the required phase" — but the order and reflection amplitudes would have to be specified arithmetically, and "arbitrary noncommuting factors add information not supplied by the primes".
- Related: L07-003, L07-055

### L07-055 Thouless formula as "Hadamard = Euler" — appealing, but needs an actual self-adjoint chain
- Source: `notes/resonances/astra-freeassoc.md`:475-483, 643; seed S5 at `astra-brief.md`:14
- Raised by: orchestrator seed S5; deflated by the codex prover
- Status at last mention: raised, classified a rewriting
- Content: The ergodic-Jacobi Thouless formula $L(E)=\int\log|E-x|dN(x)-\mathbb E\log|a|$ has the shape "one side assembled locally, the other reads a spectral logarithmic potential" — formally the Hadamard-equals-Euler identity. "But the theorem assumes an actual self-adjoint chain, an integrated density of states, and a controlled limiting process. Those objects do not come from relabeling the Euler product. If the measure in the logarithmic potential is already declared to live on real centered zero frequencies, RH has been assumed." Also: factorised integrable (Yang–Baxter) S-matrices constrain poles and residues but "do not generally put all resonances at one distance from the physical axis"; scalar arithmetic phases satisfy no useful version.
- Lead: build the self-adjoint chain first, or drop the analogy. A Furstenberg Lyapunov exponent measures growth, not unit-circle eigenvalues, and randomness gives localisation rather than a Ramanujan property.
- Related: L07-054, L07-064

### L07-056 Detailed balance and scalar-loss Lindbladians: equal rates are easy, but on the wrong spectrum
- Source: `notes/resonances/astra-freeassoc.md`:497-516 (§12), ranked 14th at :38
- Raised by: codex prover
- Status at last mention: pursued, negative as an identification — "the easy mechanism exists, but identifying it with the Riemann channel is the entire problem"
- Content: $\mathcal L(\rho)=-i[H,\rho]+\kappa(\mathrm{tr}(\rho)I/N-\rho)$ gives coherences $-\kappa-i(E_m-E_n)$ and traceless diagonals $-\kappa$: "a real structural source of equal decay rates". But there is a spectrum confusion to avoid: the amplitude generator $B$ has one mode per zero; its density-operator no-event lift has $\lambda_m+\overline{\lambda_n}$, whose real parts under RH are $-1/2$, not $-1/4$, and whose frequencies are *differences*. "A depolarizing model naturally constructs this much larger kind of spectrum."
- Lead: any BC detailed-balance construction should be compared on all four counts — full Liouville spectrum, no-event part in a specified jump gauge, one-port rank-one loss, and exit multiplicity — with the equilibrium state written explicitly.
- Related: L07-048, L07-049

### L07-057 Thermal and conformal quasinormal-mode ladders
- Source: `notes/resonances/astra-freeassoc.md`:518-536 (§13), ranked 15th at :39
- Raised by: codex prover
- Status at last mention: raised, ranked last — "presently only an analogy for the archimedean part"
- Content: Conformal/thermal correlators built from ratios of gamma functions have pole families $\omega=\omega_{\rm spatial}-i\,2\pi T(n+h)$, with a genuine representation-theoretic explanation for the ladder. Suggestive for the archimedean towers and the half-divergence shifts of §2, but "it does not explain why the irregular arithmetic resonance set occupies one particular row".
- Lead: one specific divisor comparison — BTZ scalar quasinormal modes or a 2d CFT retarded two-point function against the gamma and rational factors of $\phi$ and $S$; divide those out and ask whether anything survives in the zeta part. "This is a specific divisor comparison, not a proposed identification of physical spacetimes."
- Related: L07-014, L07-042

### L07-058 Graded transfer and a relative/boundary complex for the cusp
- Source: `notes/resonances/astra-freeassoc.md`:538-556 (§14), ranked 11th at :35
- Raised by: codex prover
- Status at last mention: partially explored — "explains the sign and cancellations; no modulus bound by itself"
- Content: Bosonic/fermionic determinants with opposite signs pair and cancel modes, explaining why an orbit-counting partition function is governed by a *reduced* determinant. "A complex of transfer operators on differential forms can make the tower cancellations operator-theoretic. A relative or boundary complex for the cusp might isolate the scattering sector that a naive $L^2$ Laplacian misses. If it also carried a positive pairing compatible with a centered evolution, that would be an actual candidate bond space."
- Lead: compute the alternating exterior-power transverse traces from the flat-trace weights and check exactly which factors of $D$ cancel, tracking the modular cusp divisor separately from the compact Laplace divisor. Literature: the dynamical determinant / resonant-state complex for geodesic flow, then a cusp version with explicit boundary conditions. Obstruction recorded: "an outgoing resonant state has boundary flux. The positive $L^2$ Hodge inner product and a residue pairing on boundary distributions are not interchangeable."
- Related: L07-007, L07-010, L07-013, L07-059

### L07-059 Grading explains the sign, not the modulus; the finite-field lesson
- Source: `notes/resonances/astra-freeassoc.md`:552, 556
- Raised by: codex prover
- Status at last mention: registered as a standing warning
- Content: "The finite-field lesson is precisely that rationality, duality, and the sign are cheaper than the weight bound." And: "Cancellation can remove or retain poles but cannot move a surviving off-line pole onto a line. Grading explains the minus sign, not the modulus. A cohomological description that silently discards the cusp resonance sector proves a statement about the wrong object."
- Lead: none; a criterion. Explicitly notes that "SPT protection of signs and phases, already rejected in the worklog as a route to moduli, is not revived by changing its vocabulary to supersymmetry."
- Related: L07-058

### L07-060 Real-rootedness, MSS interlacing, and the de Bruijn–Newman threshold
- Source: `notes/resonances/astra-freeassoc.md`:558-578 (§15), ranked 13th at :37
- Raised by: HANDOFF ("an expected characteristic polynomial might provide the missing Hermitian structure"), assessed by the codex prover
- Status at last mention: raised, classified a target not a mechanism — "a known extremality technology with no identified prime ensemble"
- Content: A mixed characteristic polynomial from independent positive rank-one data has special real-rootedness properties; if a regularised limit of such were the centred $\xi$ preserving its divisor, the Hermitian structure would be explicit. But "it is emphatically not enough that every matrix in an ensemble be Hermitian": the ensemble $H=\pm I_2$ has average characteristic polynomial $x^2+1$, with no real zeros. The de Bruijn–Newman framing (Gaussian heat factor on the Fourier kernel of $\xi$) is the same target — "Naming the threshold does not explain its value."
- Lead: reproduce the $\pm I_2$ counterexample and a genuine small MSS example, then ask whether any *finite prime construction* gives the MSS algebraic form with the right trace coefficients and a controlled limit. Literature: de Bruijn, Newman, Rodgers–Tao, "not ingredients imported without inspection".
- Related: L07-064

### L07-061 Proposed script `mayer_cusp_tail.py`
- Source: `notes/resonances/astra-freeassoc.md`:584-592 (§16.1)
- Raised by: codex prover
- Status at last mention: proposed, not written
- Content: Implement L07-035's Taylor entries in mpmath at dimensions 12/20/32 and precisions 50/80; compute $\det(I\mp\mathcal L_s)$ near the first three $s=\rho/2$ tracking null vectors; compare the exact Hurwitz tail with finite-branch approximations *in the convergence region first*, then demonstrate why they cannot be extrapolated to $\mathrm{Re}\,s=1/4$. Deliverable: a divisor and boundary-coordinate comparison with $\phi(s)$ — which parity sector sees the pole, exceptional factors, whether cusp evaluation captures the residue. Then attempt the Schur complement.
- Lead: this is the concrete first step of the top-ranked programme. Failure mode named: "cutoff-sensitive roots, a missing divisor, or wrong residues first falsify the truncation or the claimed cusp identification. A numerical pole off the line is not a counterexample unless analytic continuation, residual/error bounds, and identification with an actual zero of $\xi$ are independently certified."
- Related: L07-032, L07-034, L07-035

### L07-062 Proposed script `one_port_width_metric.py`
- Source: `notes/resonances/astra-freeassoc.md`:594-602 (§16.2)
- Raised by: codex prover
- Status at last mention: proposed, not written (partial calibration run in memory)
- Content: Build the inverse one-port model from prescribed poles and perturb the coupling residues; sweep opening strength in a closed Hermitian model to observe width splitting and superradiant segregation; form exit Gram matrices for windows of cached ordinates at increasing height; also synthetic $1/4\pm\epsilon$ pairs. Controls: scalar loss $-w_0I+iH$, equal-width inverse design, generic one-port opening. "Equal pole widths and a common survival law must be measured separately."
- Lead: "Deteriorating conditioning rules against a bounded metric change on $K_S$, while leaving open a different Hilbert completion or a different bond space. A physical scalar-loss claim is falsified as soon as nontrivial interference survives in the supposed universal norm-decay law."
- Related: L07-025, L07-026, L07-047

### L07-063 Proposed script `prime_screw_kernel.py` — a positivity test that does not input critical zeros
- Source: `notes/resonances/astra-freeassoc.md`:604-633 (§16.3)
- Raised by: codex prover, from Suzuki's local TeX
- Status at last mention: proposed, not written (a small in-memory calibration exists)
- Content: For $t\ge0$, $\Psi(t)=4(e^{t/2}+e^{-t/2}-2)-\sum_{n\le e^t}\frac{\Lambda(n)}{\sqrt n}(t-\log n)+\frac t2[\psi(1/4)-\log\pi]+\frac14[C-e^{-t/2}\Phi(e^{-2t},2,1/4)]$ with $C=\pi^2+8G_{\rm Catalan}$, even extension, $\Psi(0)=0$; form $K_{ij}=\Psi(t_i)+\Psi(t_j)-\Psi(t_i-t_j)$. Calibration at 40 digits, $t_j=j/8$, $j=1..16$: prime-defined matrix eigenvalues $\approx0.0223365$ to $0.817350$; the matrix from 3000 ordinates gave $\approx0.0216643$ to $0.806458$, largest entrywise discrepancy $0.00132330$ (the omitted zero tail). $\Psi(1)\approx0.04400730524$, $\Psi(2)\approx0.05334112417$.
- Lead: enlarge the interval, inspect the lowest eigenvectors, and study Schur complements as new prime-power breakpoints enter (L07-041). Discipline: compute the prime sum exactly to cutoff $e^{2A}$; refine precision independently of the grid; an $N\times N$ matrix with entrywise error $\epsilon$ has operator-norm error $\le N\epsilon$; "a negative direction should be converted into a smooth compactly supported test function and checked against the explicit formula before it is taken seriously". This is the only proposed test whose input is purely arithmetic.
- Related: L07-038, L07-041, L07-043

### L07-064 The eight "rewritings, not mechanisms"
- Source: `notes/resonances/astra-freeassoc.md`:635-644 (§17)
- Raised by: codex prover (self-assessment)
- Status at last mention: registered as rewritings — each restates RH without causing it
- Content: (1) "There is a centered Hermitian zero operator" — assumes reality; a positive metric additionally assumes semisimplicity, and boundedness on the cusp model is a further requirement. (2) "There is a positive centered canonical system or prime string" — with the response fixed to $Q_\xi$, positivity is presently equivalent to RH. (3) "The common-width-removed delay is a positive density of states" — the Weil criterion in experimental dress. (4) "The centered dynamics have unbroken PT symmetry" — names the desired reality. (5) "The cusp Ruelle band is an exact line" — if the roots are already $\rho/2$, this *is* RH. (6) "Inverse scattering reconstructs equal-width poles" — succeeds because equal widths were prescribed; its useful output is the residue constraint. (7) "The continued Euler product is a Hermitian density-of-states determinant" — needs an independently constructed self-adjoint chain. (8) "$\xi$ is a real-rooted expected characteristic polynomial" / "the heat threshold has the RH value" — targets until the prime ensemble or threshold-fixing identity is exhibited.
- Lead: each item names exactly what extra ingredient would promote it from rewriting to mechanism. Item (6)'s "useful output is the constraint on residues, which would still have to be derived arithmetically" is the same missing identity as L07-025.
- Related: L07-025, L07-038, L07-042, L07-053, L07-055, L07-060

### L07-065 The five genuine mechanisms in the notebook, none yet attached to the Riemann cusp sector
- Source: `notes/resonances/astra-freeassoc.md`:646
- Raised by: codex prover (closing assessment)
- Status at last mention: registered as the lane's summary verdict
- Content: "There are genuine mechanisms in this notebook: uniform attenuation per travel time, an attenuation coboundary, arithmetic tempering in a constructed representation, a positive canonical energy obtained from local data, and the special interlacing structure of certain matrix ensembles. None is yet identified with the Riemann cusp sector."
- Lead: "The next useful result would be an explicit arithmetic identity for the cusp transfer or its boundary pairing — even an obstruction showing that a proposed pairing cannot work — rather than one more general dilation of a function we already know."
- Related: L07-028, L07-038, L07-044, L07-052, L07-060

### L07-066 Weil positivity for an arbitrary transfer operator: one-sided bound, made two-sided by a duality
- Source: `notes/weil-positivity.md`:11-39; `notes/weil-positivity/astra-proofs.md`:90-115 (T1.3), 119-201 (T2.1-T2.3)
- Raised by: orchestrator (Claude), the whole brief `notes/weil-positivity/astra-brief.md`:5
- Status at last mention: registered, proved (two families), reviewed VALID; shard `report/sections/08b_weil_positivity.tex`
- Content: $\nu_\ell=r^{-\ell}(\mathrm{Tr}X^\ell-\sum_S\mu^\ell)$ is positive definite iff $|\mu|\le r$ off $S$. If the retained multiset is invariant under $J(\mu)=r^2/\bar\mu$ then the Weil form equals the mode-pairing form $W(c)=M(c)=\sum_\mu f_c(\mu/r)\overline{f_c(J\mu/r)}$ — the finite "inflow identity" — and positivity is equivalent to every mode being its own partner. An off-circle pair makes the whole form negative by Lagrange interpolation.
- Lead: "Positivity is the spectral-gap half of RH, nothing more." Every candidate transfer operator in the notebook must therefore come with a *declared* trivial set and radius plus a duality, or Weil positivity says only "no mode outside the disc".
- Related: L07-009, L07-045, L07-067, L07-068, L07-071

### L07-067 X1: Huang's criterion is the boundedness form, and $h_k=\nu_0-\nu_k$ exactly
- Source: `notes/weil-positivity.md`:41-70; `notes/reviews/weil-positivity-2026-09-12.md`:237-264, 342
- Raised by: orchestrator (Claude); the key step supplied by the Opus reviewer
- Status at last mention: registered, proved (VERDICT X1: VALID)
- Content: For a finite exponential sum, positive definite $\iff$ bounded $\iff$ $\mathrm{Re}\,\nu_\ell\le\nu_0$ for all $\ell\ge1$. The (iii)$\Rightarrow$(ii) step needs a torus-recurrence/Kronecker argument (the orchestrator's draft tried to arrange $\cos(\ell\theta)\le0$ for most $\ell$, "which cannot happen"). And Huang's $h_k=2(n-1)+q^{k/2}+q^{-k/2}-q^{-k/2}N_k$ is *literally* $\nu_0-\nu_k$, with the same $r=\sqrt q$ and the same trivial set — verified to $10^{-13}$ on $K_4$, Petersen, $K_5$, $2\times(K_4-e)$ and the non-Ramanujan ladder $CL_{21}$.
- Lead: the reviewer: "That identity is worth putting in the write-up verbatim — it reconciles the two results rather than merely relating them, and it is the cleanest available answer to the prior-art question raised in `notes/extract/weil-positivity-sources.md` W6." Two cautions to keep: the equivalence uses the *finite exponential sum* structure (the sequence $(1,0.9,-1)$ satisfies $|\nu_\ell|\le\nu_0$ but has Toeplitz eigenvalue $-0.8675$); and in the distributional case $\nu_0=\infty$, so only the positive-type form survives.
- Related: L07-066, L07-081

### L07-068 X2, the Kraus dichotomy: adjoint pairing buys reality of $\mathrm{spec}(\Sigma)$, inverse pairing buys the functional equation, unitary buys both
- Source: `notes/weil-positivity.md`:72-105; `notes/weil-positivity/astra-proofs.md`:226-441 (T3.1-T3.5); `notes/reviews/weil-positivity-2026-09-12.md`:266-281, 399-421
- Raised by: orchestrator (Claude); corrected twice by the Opus reviewer
- Status at last mention: registered, proved after the Round-2 wording fixes; shard `report/sections/08c_weil_positivity_continuous.tex` l.234-247
- Content: Every $\mathrm{Ad}$-family has nonnegative ring traces and a conjugation-closed spectrum with *no pairing hypothesis at all*. Inverse pairing gives $\mu\mapsto(D-1)/\mu$; adjoint pairing gives Hilbert–Schmidt self-adjointness of $\Sigma$; both simultaneously force every $B_i$ unitary, and then Weil positivity is exactly Hastings' bound $|\lambda|\le2\sqrt{D-1}/D$. Reviewer's slogan: "the adjoint pairing buys a Hermitian channel (hence a real $\Sigma$-spectrum, the Hilbert–Pólya half); the inverse pairing buys the functional equation; every $\mathrm{Ad}$ family gives conjugation closure and nonnegative ring counts for free."
- Lead: this is the notebook's cleanest statement of *what structure RH needs* — and it says a Riemann transfer operator would have to be simultaneously adjoint- and inverse-paired, i.e. unitary-like, which is exactly what the cusp dissipation prevents. The escape hatch is L07-069.
- Related: L07-039, L07-045, L07-066, L07-069, L07-077, L07-079

### L07-069 $B_i=GU_iG^{-1}$: inverse-paired, far from unitary, yet real $\Sigma$-spectrum — the sharpened `conj:kraus-ramanujan`
- Source: `notes/weil-positivity.md`:96-101; `notes/reviews/weil-positivity-2026-09-12.md`:277, 278, 421
- Raised by: orchestrator (Claude) guessed it; the Opus reviewer confirmed it numerically
- Status at last mention: registered as a conjecture (`conj:kraus-ramanujan`, sharpened form); confirmed 6/6 numerically but not proved to be the only such class
- Content: With $U_{\bar i}=U_i^\dagger$ unitary and one common invertible $G$, the family is inverse-paired and in general far from adjoint-paired ($|B^\dagger B-1|$ up to $24.3$), yet $\Sigma=\mathrm{Ad}(G)\Sigma_U\mathrm{Ad}(G)^{-1}$ is similar to the self-adjoint $\Sigma_U$ (via $S(x)=G^{-1}xG^{-\dagger}$), so $\mathrm{spec}(\Sigma)$ is real and the band holds iff it holds for the unitary family. Random inverse-paired families instead give non-real $\Sigma$-spectra (e.g. $0.628\pm3.294i$) in 3/5 runs.
- Lead: the reviewer: "Calling their non-Hermitian-$\Sigma$-with-real-spectrum an unbroken-PT situation is a fair analogy provided it stays an analogy: the similarity $S$ here is explicit and finite-dimensional." The open question is whether *every* inverse-paired family with real $\Sigma$-spectrum is of this similarity form — that would be the finite-dimensional model of the Hilbert–Pólya metric problem of L07-053.
- Related: L07-053, L07-068, L07-071

### L07-070 T3.5: an adjoint-paired family with no reciprocal duality at all
- Source: `notes/weil-positivity/astra-proofs.md`:395-441; `notes/reviews/weil-positivity-2026-09-12.md`:128-138, 409
- Raised by: orchestrator asked for it (brief T3(e)); constructed by the codex prover
- Status at last mention: registered, proved-here and reviewed VALID
- Content: $n=2$, $D=4$, $B_1=B_3=\mathrm{diag}(1,2)$, $B_2=B_4=I$. The retained multiset $\{p_2^{[2]},n_2^{[2]},p_4,n_4\}$ (roots of $x^2-(a+1)x-3a$) is invariant under $\mu\mapsto c/\mu$ for *no* $c$, because the multiplicity-2 pair forces $c=-6$ and the multiplicity-1 pair forces $c=-12$. Yet the Weil form is well defined and positive exactly for $r\ge p_4$.
- Lead: the reviewer used this family to refute a universal clause in the shard: this family has *all sixteen* eigenvalues of $T$ real while admitting no reciprocal symmetry, so "spec(T) is not real" must be "need not be real" (L07-079). Also: the brief's phrase "has no partner to refer to" was corrected — the reflection still exists on the punctured plane, it just need not land on a retained mode.
- Related: L07-066, L07-068, L07-079

### L07-071 Weil positivity is blind to Jordan blocks; Hilbert–Pólya needs semisimplicity
- Source: `notes/weil-positivity/astra-proofs.md`:676-741 (T5.1-T5.3); `notes/weil-positivity.md`:38-39; `notes/reviews/weil-positivity-2026-09-12.md`:202-209
- Raised by: orchestrator (brief T5); proved by the codex prover
- Status at last mention: registered, proved
- Content: For $X=r\begin{psmallmatrix}1&1\\0&1\end{psmallmatrix}$, $\nu_\ell=2$ for every $\ell$, so the Weil form is positive definite — but $\|(X/r)^ke_2\|\to\infty$, so no inner product unitarises $X/r$. Continuous version identical with $F(t)=2$. Hence "RH $\iff$ Weil positivity" holds with multiplicities, but "RH $\iff$ a Hilbert–Pólya inner product exists" needs semisimplicity in addition.
- Lead: this is why §10 of the resonances note insists semisimplicity matters at the PT threshold (L07-053), and why the notebook must not equate "all modes on the line" with "there is a self-adjoint operator". Repeated zeros of $\zeta$ would be exactly this issue.
- Related: L07-026, L07-053, L07-066, L07-069

### L07-072 Continuous ring norms from the Dyson expansion (the cMPS/Lindblad side A)
- Source: `notes/weil-positivity/astra-proofs.md`:601-666 (T4.4); `notes/reviews/weil-positivity-2026-09-12.md`:169-179
- Raised by: orchestrator (brief T4c); the product corrected by the codex prover
- Status at last mention: registered, proved-here, reviewed VALID
- Content: For $\mathcal L(x)=Kx+xK^\dagger+\sum_jR_jxR_j^\dagger$ (no trace preservation), $\mathrm{Tr}_{M_n}e^{t\mathcal L}=\sum_k\sum_{\mathbf j}\int_{\rm simplex}|\mathrm{Tr}\,A_{\mathbf j,\mathbf t}|^2\ge0$ with the *free propagators retained between jumps*. The brief's propagator-free product is false for non-commuting $K,R_j$ — and the reviewer added the precise reason it is not visible at first order: at $k=1$ cyclicity recombines them, so the error first bites at $k=2$ ($0.19440805$ vs the true $0.19452865$).
- Lead: this is the continuous analogue of "ring norms are nonnegative", i.e. side A for a cMPS. It gives no line reflection and no positive definiteness of shifted subtracted traces — those need side B structure.
- Related: L07-066, L07-068, L07-073

### L07-073 T6: the conditional zeta dictionary ($a=-1/4$, $\eta(\rho)=-\bar\rho/2$, $S=\varnothing$, the autocorrelation identity)
- Source: `notes/weil-positivity/astra-proofs.md`:743-938 (T6.1-T6.4); `notes/reviews/weil-positivity-2026-09-12.md`:211-227
- Raised by: orchestrator (brief T6); corrected and made precise by the codex prover
- Status at last mention: registered as `sketched`/`conditional-on H-ZD, H-ZM, H-ZEF, H-ZW`; reviewed VALID as a dictionary
- Content: Centre at $a=-1/4$; the reflection $\rho\mapsto1-\bar\rho$ becomes $\eta\mapsto-1/2-\bar\eta$, fixed line $\mathrm{Re}\,\eta=-1/4$. The one-sided condition of T4.2 reads $\sigma\ge1/2$ — "the direction of this one-sided inequality is important", and the functional equation supplies the other half. The exact identity is $\sum_\rho\hat g_\zeta(\rho)\overline{\hat g_\zeta(1-\bar\rho)}=\langle\mathcal K,\varphi_g\rangle=\iint g(t)\overline{g(s)}e^{(t-s)/4}\mathrm{Tr}_{\rm dist}Z(t-s)\,dt\,ds$ with $\hat g_\zeta(s)=\int g(t)e^{(s-1/2)t/2}dt$ (the exponent is $/2$, forced because $Z$ runs at frequency $\gamma/2$). Correction: $\xi$ is entire, so $S=\varnothing$; $\{0,-1/2\}$ is available only after an artificial augmentation. Negative-time extension: $\tau(-u)=e^{u/2}\overline{\tau(u)}$, *not* $\overline{\tau(u)}$.
- Lead: the four named inputs are the exact list of what would have to be verified to make the dictionary a theorem. The reviewer confirmed H-ZEF numerically to six digits with 70 zeros.
- Related: L07-015, L07-016, L07-074, L07-075, L07-076

### L07-074 The modes of $Z$ cannot be a trace-class eigenvalue list
- Source: `notes/weil-positivity/astra-proofs.md`:938
- Raised by: codex prover
- Status at last mention: registered as a structural obstruction
- Content: "For the asserted infinitely many semigroup eigenmodes, the moduli at a fixed $t>0$ satisfy $|e^{t\eta(\rho)}|=e^{-t\mathrm{Re}\,\rho/2}\ge e^{-t/2}$; they cannot be an absolutely summable trace-class eigenvalue list. Distributional testing is essential, and no bounded negative-time operator has been assumed."
- Lead: any attempt to write $\mathrm{Tr}\,Z(t)$ as an honest operator trace is doomed; the same obstruction as L07-002 for the prime circles, on the other side of the dictionary. A regularised (zeta-regularised, or flat) trace is the only option.
- Related: L07-002, L07-015, L07-073

### L07-075 H-ZW: the infinite-dimensional Weil converse is an input, and the finite interpolation does NOT supply it
- Source: `notes/weil-positivity/astra-proofs.md`:914-920, 934; `notes/weil-positivity.md`:111-112; `notes/reviews/weil-positivity-2026-09-12.md`:225
- Raised by: codex prover; singled out by the Opus reviewer
- Status at last mention: registered as an unproved input
- Content: The converse ("positivity of the pairing for all $g\in C_c^\infty$ implies every zero on the line") "is not established by the finite interpolation in T2.2 and is not a consequence claimed here from Bochner–Schwartz alone". Nor can the finite boundedness proof be used, since $F(0)=\#\mathcal Z=\infty$, nor "interpolate away infinitely many unwanted modes by a finite polynomial".
- Lead: the reviewer: "Given the rest of the notebook, that refusal is the most valuable sentence in T6." If one wanted to *prove* the converse in the notebook's own language, one would need an infinite-dimensional version of the Lagrange-interpolation separation of T2.2 — that is a genuine open problem stated here.
- Related: L07-066, L07-073, L07-076

### L07-076 What a rigorous realization would need
- Source: `notes/weil-positivity/astra-proofs.md`:936-938 (T6.4 <1>2)
- Raised by: codex prover (scope audit)
- Status at last mention: raised, open
- Content: "H-ZD supplies a test space and convergence; H-ZEF supplies the arithmetic evaluation; H-ZM supplies the asserted link to the particular compressed semigroup; and H-ZW supplies the infinite-dimensional converse. Verifying those inputs would make the corresponding distributional identities and equivalence rigorous. A further Hilbert–Pólya conclusion would require a suitable spectral realization by a self-adjoint operator, with its domain and multiplicities specified; a mode list alone is insufficient."
- Lead: a four-item checklist for turning the Riemann-channel dictionary into mathematics. H-ZM (the identification of $Z$'s regularised trace with the spectral distribution) is the one nobody has attempted.
- Related: L07-073, L07-074, L07-075

### L07-077 Correction: "both pairings iff a nonzero scalar multiple of a unitary" is false — it is $B^\dagger B=I$
- Source: `notes/weil-positivity/astra-proofs.md`:318-343 (T3.3), 954; `notes/reviews/weil-positivity-2026-09-12.md`:107-114
- Raised by: orchestrator (drafted wrong); corrected by the codex prover, confirmed by the reviewer
- Status at last mention: pursued, negative (drafted statement withdrawn)
- Content: $\mathrm{Ad}$ is *quadratic* in $B$: for $B=tU$, $\mathrm{Ad}(B^\dagger)=t^2\mathrm{Ad}(U^\dagger)$ while $\mathrm{Ad}(B)^{-1}=t^{-2}\mathrm{Ad}(U^\dagger)$, so $t^4=1$. $B=2I$ is the direct disproof: $\mathrm{Ad}(B^\dagger)=16\,\mathrm{Ad}(B)^{-1}$. The projective variant is $\mathrm{Ad}(B^\dagger)=\kappa\mathrm{Ad}(B)^{-1}\iff B^\dagger B=\sqrt\kappa I$.
- Lead: none; a trap recorded. It matters because the "unitary-up-to-scalar" reading would have made the Ramanujan criterion look more available than it is.
- Related: L07-068

### L07-078 Correction: the requested Kraus counterexample to conjugation closure does not exist
- Source: `notes/weil-positivity/astra-proofs.md`:270, 301-316, 952; `notes/reviews/weil-positivity-2026-09-12.md`:104
- Raised by: orchestrator asked for one (brief T3b); codex prover showed none exists
- Status at last mention: pursued, negative (a strengthening, not a gap)
- Content: For arbitrary inverse-paired *superoperators* the criterion "$A_0$ conjugation-invariant $\iff$ $\mathrm{spec}(\Sigma)$ conjugation-invariant" can fail ($N=1$, $D=4$, scalar weights $2i,1,-i/2,1$, $\Sigma=2+3i/2$). But "for inverse-paired Kraus matrices both sides always hold. There is no Kraus counterexample." The reviewer: $M_1$ Kraus maps are multiplication by $|b|^2\ge0$, so no $n=1$ counterexample can exist.
- Lead: conjugation symmetry of the transfer spectrum is free for Kraus families — one of the two symmetries RH needs comes at no cost. Only the reciprocal one is expensive.
- Related: L07-068, L07-070

### L07-079 Round-2 mandatory edits to `obs:kraus-dichotomy`
- Source: `notes/reviews/weil-positivity-2026-09-12.md`:399-427, 434
- Raised by: Opus reviewer (Round 2)
- Status at last mention: raised; verdict conditional — "if the (d) qualifier is declined, my verdict on X2 reverts to INVALID for that clause alone"
- Content: (1) Clause (d) must carry the *enlarged* trivial set. With $S_{\rm triv}=S_0$ alone the clause is false for *every* unitary family, because $\Phi(I)=I$ always makes $\alpha=D$ an eigenvalue and $D>2\sqrt{D-1}$ for every $D\ge4$; measured distance from the retained mode $\mu=q$ to the circle: $1.2679,\,2.7639,\,1.2679$. The fix is $S=S_0\uplus\{q^{[d_+]},1^{[d_+]}\}\uplus\{(-q)^{[d_-]},(-1)^{[d_-]}\}$. (2) Clause (c) needs "need not"/"in general": T3.5's $\mathrm{diag}(1,2)$ family has a real $\mathrm{spec}(T)$.
- Lead: the general moral — the *trivial set is not optional bookkeeping*; a wrong $S$ flips the criterion. Exactly the lesson of L07-009 in the Selberg lane and of L07-045 for a lead.
- Related: L07-009, L07-045, L07-068, L07-070

### L07-080 The one-sided theorems need no positive ring-count premise
- Source: `notes/weil-positivity/astra-proofs.md`:441, 969
- Raised by: codex prover
- Status at last mention: registered
- Content: "For completely arbitrary superoperators even the nonnegative ring-count premise is absent: a scalar superoperator with weight $i$ and $D=2$ can already give $\mathrm{Tr}\,T=2i$. T1 and T2 still apply to that transfer operator with their stated hypotheses." Nonnegative ring traces hold for $\mathrm{Ad}$ families, are distinct from Weil positive definiteness even when available, and are not needed by the one-sided theorems.
- Lead: side A positivity and Weil positivity are logically independent. Any claim that "the ring count being positive gives Weil positivity" is wrong.
- Related: L07-066, L07-068, L07-072

### L07-081 Finite-$L$ masking in the Toeplitz test
- Source: `notes/reviews/weil-positivity-2026-09-12.md`:44, 158, 356
- Raised by: Opus reviewer (practical)
- Status at last mention: registered as a numerics caveat
- Content: A pair at radius $1+\epsilon$ first produces a negative Toeplitz eigenvalue only at $L=5,20,20,40$ for $\epsilon=0.2,0.05,0.02,0.01$; continuously, the threshold at offset $\pm0.02$ needs window $T=40$ (at $T=10$ the Gram matrix is still $+1.4$). "This is a property of truncation, not a defect of the theorem."
- Lead: any numerical Weil-positivity test on a candidate operator must escalate $L$ (or the window) with the expected off-line distance, or it will report a false positive. Directly relevant to L07-061/062/063.
- Related: L07-061, L07-062, L07-063, L07-067

---

## Small but possibly consequential

1. **L07-019** — the modular continuous term has an extra $(K_0/4)h(1/4)$ contact term with $K_0=\phi(1/2)=-1$, sitting exactly at the spectral parameter $1/4$ that the RH condition names; nobody wrote out the remaining parabolic terms.
2. **L07-033** — the Mayer cusp tail's leading singular term at $s=1/2$ has **rank-one** residue: the only place in the notebook where the Riemann channel's postulated rank-one dissipation could be *derived* from arithmetic rather than assumed.
3. **L07-030** — "inducing the flow introduces an unbounded roof and boundary conditions, precisely where the missing information can reside": one sentence that locates the gap between uniform hyperbolic expansion and the cusp.
4. **L07-006** — the spectral gap of the two-jump Lindbladian is governed by the decomposition of $\pi\otimes\bar\pi$; written as a deliberate non-theorem and never revisited, yet it is the representation-theoretic route to a continuous Ramanujan bound.
5. **L07-041 / L07-063** — look for an *arithmetic recurrence* in the Cholesky/Schur factors of Suzuki's prime kernel as the interval crosses $\log p^k$; the only proposed experiment that could discover structure instead of confirming RH numerically.
6. **L07-043** — "integrating twice and using Suzuki's kernel is a cleaner way to implement the same question on compact test supports": a one-line bridge from the ill-conditioned $e^{|t|/4}$ deconvolution to a computable matrix.
7. **L07-052** — a loop with scalar attenuation gives equal widths for an arbitrary unitary $U$, proving that a single exit is not itself an obstruction to uniform widths; this quietly removes the strongest "physical" objection to the whole programme.
8. **L07-020** — the $-1/2$ in the scattering multiplier is exactly the trace-formula normalisation, an independent confirmation the prover's file does not claim; worth stating because it shows the convention was forced, not chosen.

---

## Dead routes recorded

Do not re-try these blindly; each was explicitly declared negative or corrected.

- **Prime circles as side B.** The direct sum over primes of rotations has the prime comb as its orbital trace but its spectrum is exactly the *poles* of the finite Euler product, which has no zeros at all — `notes/selberg/astra-proofs.md`:77-101, `notes/selberg-dictionary.md`:32.
- **Smearing the infinite direct sum to get a trace.** Not trace class: the constant modes give one eigenvalue of infinite multiplicity — `notes/selberg/astra-proofs.md`:63-65, 783.
- **Treating the undamped positive prime comb as a tempered distribution.** It is not: $\sum_p\log p/(1+\log p)^N=\infty$ for every $N$; and its coefficient at $t=0$ diverges — `notes/selberg/astra-proofs.md`:67-73.
- **Calling a circle-translation generator a dissipative Lindbladian.** It is anti-self-adjoint and first order — `notes/selberg/astra-proofs.md`:784.
- **The Casimir as a global Lindbladian on $\Gamma\backslash G$.** The compact direction enters with a minus sign; the symbol is indefinite. Valid only on $Wf=0$ — `notes/selberg/astra-proofs.md`:201-207, 785.
- **$\Lambda_{\rm fl}=-\partial_\sigma\log D$.** Wrong sign; it is $+D'/D$ (confirmed to $10^{-31}$) — `notes/selberg/astra-proofs.md`:332, 787; review `notes/reviews/selberg-2026-09-12.md`:206-215.
- **"The graph analogue of $D$ is $1/\det(1-uT)$."** It is $\det(1-uT)$ — `notes/selberg/astra-proofs.md`:481, 790; review `notes/reviews/selberg-2026-09-12.md`:274-282.
- **A positive prime comb in the cusp transform.** For $m=-\frac12\phi'/\phi$ the prime atoms are *dips*, $-\Lambda(n)/n$; reversing the Fourier exponential cannot fix it since $m$ is even — `notes/selberg/astra-proofs.md`:589, 791.
- **"The cusp term is the trace of the Riemann channel damped at rate $1/4$" (unqualified).** Needs a subtraction/sign convention and a separately justified channel trace formula; $A$ does not vanish on $t>0$ — `notes/selberg/astra-proofs.md`:718, 726, 744.
- **The notebook §5 prime weights $+\Lambda(n)n^{-1/2}$, and applying the damping twice.** Out by $-2$ and double-counted — `notes/selberg/astra-proofs.md`:728-744; `notes/reviews/selberg-2026-09-12.md`:291-300; `notes/reviews/weil-positivity-2026-09-12.md`:283-314.
- **Identifying "trace resonances" with Pollicott–Ruelle resonances.** Declined deliberately; the DFG theorem excludes exactly the integer points at issue — `notes/selberg/astra-proofs.md`:413; `notes/reviews/selberg-2026-09-12.md`:266-272.
- **"Uniform curvature therefore RH."** "Skips the entire scattering problem"; a spectral gap does not put every resonance on its boundary — `notes/resonances/astra-freeassoc.md`:137.
- **Replacing the modular scattering band by the compact Laplace first band.** Different families ($\mathrm{Re}\,\sigma=1/4-j$ vs $-1/2-k$) — `notes/resonances/astra-freeassoc.md`:119.
- **"GUE positions plus equal widths is the fingerprint of scalar loss."** Any finite equal-width non-lattice pole set has a one-port realisation — `notes/resonances/astra-freeassoc.md`:43, 77, 101.
- **Positive canonical-system energy makes the monodromy elliptic.** False; explicit two-slab counterexample with transfer $\mathrm{diag}(-16,-1/16)$ — `notes/resonances/astra-freeassoc.md`:226-234.
- **Local Euler factors as inner functions with zeros on $\mathrm{Im}\,\tau=-1/2$.** $R_p$ has *poles* there; only $b_p$ is inner. Numerically $|R_2|=54.2$ at $y=0.49$ — `notes/resonances/astra-freeassoc.md`:462-473, 485-493.
- **A bounded renorming of the model space $K_S$ making the generator normal.** Ruled out by the increasing density of zeros: overlaps $\to1$ — `notes/resonances/astra-freeassoc.md`:103; conditioning $9.88\to701$ at :99.
- **Reading $y\mapsto e^{i\theta}y$ in the cusp as exterior complex scaling.** It is a complex *translation* in $r=\log y$, not a rotation; three different continuations are being conflated — `notes/resonances/astra-freeassoc.md`:384.
- **Complex scaling as a width mechanism.** "Complex scaling exposes existing poles and does not move them onto a new line" — `notes/resonances/astra-freeassoc.md`:390.
- **Choosing $\Omega$ to tune the renewal spectrum.** "That would explain a designed process, not RH" — `notes/resonances/astra-freeassoc.md`:367.
- **A Lévy-style small-jump completion of the Bost–Connes measure at $\sigma=1$.** The divergence is at *large* jumps; no continuous characteristic function on the dilation group results — `notes/resonances/astra-freeassoc.md`:355-361.
- **Picking $r_p$ to give the desired decay on independent prime circles.** Builds the answer in; their direct sum is still side A — `notes/resonances/astra-freeassoc.md`:415.
- **Deriving equal widths from Hecke self-adjointness continued to $\rho/2$.** $t_p(\rho/2)$ is complex even under RH — `notes/resonances/astra-freeassoc.md`:309-315.
- **Substituting Selberg's $1/4$ for RH, or importing Deligne's bound without identifying the cusp sector** — `notes/resonances/astra-freeassoc.md`:327.
- **Thouless/Furstenberg reading of the Euler product.** Measures exponential growth, not unit-circle eigenvalues; needs an independently constructed self-adjoint chain — `notes/resonances/astra-freeassoc.md`:495, 643.
- **Detailed balance / KMS as a source of scalar damping.** "A KMS state or a symmetric dissipator does not impose scalar damping"; and the density-operator lift has the wrong real parts ($-1/2$) and difference frequencies — `notes/resonances/astra-freeassoc.md`:512, 516.
- **SPT protection of signs and phases as a route to moduli** — already rejected in the worklog, and "not revived by changing its vocabulary to supersymmetry" — `notes/resonances/astra-freeassoc.md`:556.
- **"Every matrix Hermitian therefore real-rooted average characteristic polynomial."** $H=\pm I_2$ gives $x^2+1$ — `notes/resonances/astra-freeassoc.md`:566-572.
- **Treating $q_S\ge0$ as Weil positivity.** It holds for all passive inner models — `notes/resonances/astra-freeassoc.md`:295.
- **The eight rewritings of §17** (centred Hermitian zero operator; positive prime string; width-removed delay; unbroken PT; the cusp Ruelle band being a line; inverse-scattering reconstruction; Euler product as a density-of-states determinant; real-rooted $\xi$ / heat threshold) — `notes/resonances/astra-freeassoc.md`:635-644.
- **"Both pairings iff a nonzero scalar multiple of a unitary."** False; $B^\dagger B=I$. $B=2I$ disproves it — `notes/weil-positivity/astra-proofs.md`:328, 343, 954.
- **A Kraus counterexample to conjugation closure under inverse pairing.** None exists — `notes/weil-positivity/astra-proofs.md`:270, 952.
- **The Dyson product without the free propagators between jumps.** False for non-commuting $K,R_j$; invisible at $k=1$ by cyclicity, wrong from $k=2$ — `notes/weil-positivity/astra-proofs.md`:959; `notes/reviews/weil-positivity-2026-09-12.md`:179.
- **Two trivial modes of $Z$ from "the poles of $\xi$ at $0,1$."** $\xi$ is entire; the poles belong to $\Lambda_\zeta$. The honest answer is $S=\varnothing$ — `notes/weil-positivity/astra-proofs.md`:790-794, 963.
- **Taking the superoperator trace over $M_n\otimes M_n^*$.** Dimension $n^4$; the right trace is over $M_n$ — `notes/weil-positivity/astra-proofs.md`:666, 960.
- **The naive negative-time extension $\tau(-u)=\overline{\tau(u)}$.** It is $e^{u/2}\overline{\tau(u)}$ — `notes/weil-positivity/astra-proofs.md`:842-844, 966.
- **Arranging $\cos(\ell\theta)\le0$ for most $\ell$ (the orchestrator's first X1 draft).** "The rotation always returns near the identity" — `notes/weil-positivity.md`:60-61; `notes/reviews/weil-positivity-2026-09-12.md`:250.
- **Hastings' bound with the *unenlarged* trivial set $S_0$ for a unitary family.** False for every unitary family, since $\alpha=D$ is always an eigenvalue and always out of band — `notes/reviews/weil-positivity-2026-09-12.md`:411, 424.
- **Deducing the infinite Weil converse from the finite interpolation or from Bochner–Schwartz.** Explicitly not available; $F(0)=\infty$ — `notes/weil-positivity/astra-proofs.md`:920, 934.
