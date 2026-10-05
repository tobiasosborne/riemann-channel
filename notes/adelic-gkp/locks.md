# Locks between modes: where they come from, and which fluxes have none

Author: `claude:fable-5.1`, 2026-10-05, at TJO's request ("Ok investigate this": the two questions left open by `sign-vector.md`, whether a symmetry stands behind locks other than $\pm\lambda$, and which signed graphs have no locks). Status: **a record, not a round.** Nothing is registered in `db/claims.tsv`; no REFUTE review has run; no shard. Checks: `checks/check_locks.py`, output `checks/output_locks.txt` (7/7; needs PARI through `cypari2`, and `networkx`).

**Verdict.**

- **A lock between two modes is a rotation of finite order.** When the real field of the eigenvalues has one prime above $p$ (always the case for integer eigenvalues), two modes are locked exactly when their Frobenius eigenvalues differ by a root of unity, $\mu'=\zeta\mu$ or $\mu'=\zeta\bar\mu$. The lock sign is $+1$ for a rotation and $-1$ for a rotation composed with a reflection.
- **For integer eigenvalues there are only three kinds.** The half turn ($\zeta=-1$, the pair $\pm\lambda$), the quarter turn (Gaussian integers: $\lambda^2+(\lambda')^2=4q$) and the sixth turn (Eisenstein integers). The quarter turn is the Hadamard gate of the square GKP lattice; the sixth turn is the corresponding symmetry of the hexagonal one.
- **Only the half turn comes from a symmetry of the graph.** For a bipartite graph it is the sign change on one side, and it always exists. I found no graph symmetry behind the quarter and sixth turns; they are coincidences of the eigenvalues.
- **For bipartite graphs the lock dissolves.** The step is then a square root. The arithmetic lattice is one Lagrangian half, functions on one side plus functions on the other; its symplectic form is the signed biadjacency matrix; and Frobenius is two steps of the walk. On that half every ordinary Ramanujan flux of the cube is polarised, 15 of the 31 principally.
- **Fluxes without locks exist on small graphs**, the smallest found being a cubic graph on 8 vertices with one negative edge. In a scan of 21069 ordinary Ramanujan flux classes, $\Omega$ is a polarisation for 4534 of the 13329 that could be decided (§5).

## 1. A pairwise lock is a root-of-unity relation

**Proposition.** Suppose the real field $N^+$ of the eigenvalues has exactly one prime above $p$. Two ordinary modes $\lambda\ne\lambda'$ are locked if and only if $\mu'_+=\zeta\mu_+$ or $\mu'_+=\zeta\mu_-$ for a root of unity $\zeta$. The lock sign is $+1$ in the first case and $-1$ in the second.

*Proof.* If the modes are locked they have the same field $K_1=N^+(\delta)$, and the one prime $\mathfrak{p}^+$ splits in it as $\mathfrak{P}\bar{\mathfrak{P}}$. Each of $\mu_+,\mu'_+$ generates a power of $\mathfrak{P}$ or of $\bar{\mathfrak{P}}$, so $\mu'_+$ generates the same ideal as $\mu_+$ or as $\mu_-$. The quotient is a unit of absolute value 1 in every complex embedding, hence a root of unity (Kronecker). The sign is $+1$ exactly when $\mu_+$ and $\mu'_+$ lie in the same prime. Conversely, if $\mu'=\zeta\mu$ with different fields, applying the automorphism that fixes $\delta$ and flips $\delta'$ gives $\mu^2/q$ a root of unity, which is impossible for an ordinary mode. ∎

Checked on eight pairs (L1); the order of $\zeta$ and the sign agree with the residue rule of `sign-vector.md`.

| $q$ | eigenvalues | order of $\zeta$ | relation | lock |
|---|---|---|---|---|
| any | $\lambda,\ -\lambda$ | 2 | $\mu'_+=-\mu_-$ | $-1$ |
| 5 | $2,\ 4$ | 4 | $\mu'_+=\zeta\mu_-$ | $-1$ |
| 5 | $-2,\ 4$ | 4 | $\mu'_+=\zeta\mu_+$ | $+1$ |
| 7 | $1,\ 5$ | 6 | $\mu'_+=\zeta\mu_+$ | $+1$ |
| 7 | $1,\ 4$ | 3 | $\mu'_+=\zeta\mu_-$ | $-1$ |
| 7 | $4,\ 5$ | 6 | $\mu'_+=\zeta\mu_-$ | $-1$ |
| 5 | $1\pm2\sqrt3$ | 3 | $\mu'_+=\zeta\mu_+$ | $+1$ |

**In the lattice.** A locked partner is the same step followed by a rotation of finite order of the mode's plane, or by such a rotation and a reflection. The rotation is a symmetry of the field, and of the maximal lattice in it; the two modes' own lattices can differ by a sublattice (for $q=5$ the mode $\lambda=4$ has the square lattice $\mathbb Z[i]$ and the mode $\lambda=2$ the 1 by 2 rectangle).

## 2. Integer eigenvalues: three kinds of lock, and no others

Write $4q-\lambda^2=d\,m^2$ with $d$ squarefree. The mode's field is $\mathbb Q(\sqrt{-d})$, and its only roots of unity are $\pm1$ unless $d=1$ or $d=3$. So (L2, checked for all primes $q<400$):

| kind | field | condition | partners of $\lambda$ |
|---|---|---|---|
| half turn | any | none | $-\lambda$ |
| quarter turn | $\mathbb Q(i)$, $d=1$ | $4q-\lambda^2=m^2$ | $\pm m$ |
| sixth turn | $\mathbb Q(\sqrt{-3})$, $d=3$ | $4q-\lambda^2=3m^2$ | $\pm\tfrac12(\lambda+3m),\ \pm\tfrac12(\lambda-3m)$ |

Examples: $q=5$: $\{2,4\}$; $q=13$: $\{4,6\}$ and $\{2,5,7\}$; $q=7$: $\{1,4,5\}$; $q=19$: $\{1,7,8\}$.

The quarter turn is the rotation by which the square GKP lattice is self-dual, its Hadamard gate. So two modes locked by a quarter turn are the same step up to a Hadamard gate on that mode, and two locked by a sixth turn are the same step up to the order-six symmetry of the hexagonal lattice.

## 3. A lock that depends on the prime

When $N^+$ has several primes above $p$, a relation can have different signs at different primes, and then it is not a root-of-unity relation and does not obstruct. Example (L3): $q=11$, eigenvalues $\tfrac12(-1\pm\sqrt5)$. The Frobenius eigenvalues lie in the cyclic quartic field $\mathbb Q(\zeta_5)$. There is one relation, with sign $-1$ at one prime of $\mathbb Q(\sqrt5)$ above 11 and $+1$ at the other, so all four sign vectors occur and $\Omega$ is a polarisation for a suitable choice.

## 4. The half turn as a symmetry, and how bipartite graphs dissolve it

**Bipartite graphs.** Let $D=\pm1$ according to the side of the bipartition. Then $DA_sD=-A_s$ for every flux, so the fermionic spectrum is symmetric and $\Omega$ is never a polarisation. But $D$ is an involution, and that changes the picture (L4):

- $\Gamma=\mathrm{diag}(D,-D)$ anticommutes with the step, reverses $\Omega$, and $\Gamma^2=1$.
- Its fixed lattice $T_+$ is a Lagrangian half of rank $n$: **functions on one side of the graph as positions, functions on the other side as momenta.**
- The step maps $T_+$ to the other half, so $F^2$ acts on $T_+$: **the step is a square root of Frobenius**, which now lives over $\mathbb F_{q^2}$. The notebook has this for graded channels with all letters odd (`thm:odd-letters-chiral`).
- The form $\omega_+(x,y)=\Omega(x,(F+V)y)$ restricted to $T_+$ is the **signed biadjacency matrix** $B_s$: $\omega_+=\begin{pmatrix}0&B_s\\-B_s^T&0\end{pmatrix}$. It is compatible with $F^2$ and positive for the upper half-plane type of $F^2$. Its determinant is $\det(B_s)^2$, so the half lattice is a GKP code of dimension $\lvert\det B_s\rvert$, a qunaught when $B_s$ is unimodular.

The modes $\lambda$ and $-\lambda$ of the step are one mode of $F^2$, so the half-turn lock is gone. What remains is the question for the two-step eigenvalues $\lambda^2-2q$. For the cube:

| flux classes | $\lvert\det B_s\rvert$ | two-step eigenvalues | relations | polarised by $\omega_+$ |
|---|---|---|---|---|
| 12 | 1 | four distinct | none | yes, principally |
| 12 | 3 | $-3.83,\ -1,\ 1.83$ | none | yes |
| 3 | 5 | $-3,\ 1$ | none | yes |
| 3 | 1 | $-3.83,\ 1.83$ | none | yes, principally |
| 1 | 9 | $-1$ | none | yes |

So every ordinary Ramanujan flux of the cube gives a polarised abelian fourfold over $\mathbb F_4$ on the half lattice, and 15 of the 31 give a principally polarised one. (For the first row the splitting field is too large for the direct check; the rule alone was used.)

**$K_4$, which is not bipartite.** There the signed permutations with $DA_sD^{-1}=-A_s$ have order four, some with $D^2=-1$, so there is no real half (`howe-positivity.md` §3). The half turn is still a symmetry, but it does not split the lattice over the integers.

**The other turns.** A quarter or sixth turn would need a map on the graph sending the eigenvalue $\lambda$ to $\pm\sqrt{4q-\lambda^2}$, or to $\tfrac12(\lambda\pm3m)$. I know of no graph operation that does this, and the examples do not suggest one.

## 5. Which fluxes have no locks

Two necessary conditions come first.

- **Not on a bipartite graph**, by §4 (though there the half lattice takes over).
- **Integer spectra:** no locks exactly when the squarefree parts of $4q-\lambda_j^2$ are pairwise distinct, by §2.

Beyond that the condition is that the Weil-form determinants are independent modulo squares, and I have no description of it in terms of the graph. A scan of small regular graphs (L6) shows what happens in practice. Only fluxes that are Ramanujan and ordinary are counted.

| family | graphs | flux classes | with a $\pm\lambda$ pair | no locks | other locks, all $+1$ | other locks, some $-1$ | undecided |
|---|---|---|---|---|---|---|---|
| cubic, 4 vertices ($K_4$) | 1 | 6 | 6 | 0 | 0 | 0 | 0 |
| cubic, 6 vertices | 2 | 0 | | | | | |
| cubic, 8 vertices | 5 | 121 | 87 | 2 | 0 | 2 | 30 |
| 4-regular, 5 vertices ($K_5$) | 1 | 20 | 20 | 0 | 0 | 0 | 0 |
| 4-regular, 6 vertices (octahedron) | 1 | 66 | 58 | 8 | 0 | 0 | 0 |
| 4-regular, 7 vertices | 2 | 186 | 12 | 24 | 0 | 0 | 150 |
| 6-regular, 7 vertices ($K_7$) | 1 | 20670 | 8190 | 3240 | 1260 | 420 | 7560 |

$\Omega$ is a polarisation in the columns "no locks" and "all $+1$": 4534 of the 13329 classes that could be decided. "Undecided" means the real field of the eigenvalues was too large for the time limit of 25 seconds per spectrum.

What the scan shows:

- **Lock-free fluxes exist on small graphs.** The smallest found: a cubic graph on 8 vertices with one negative edge (fermionic characteristic polynomial $(x+1)^2(x^3-x^2-5x+1)^2$), and the octahedron with three negative edges ($(x+2)^2(x^2-2x-2)^2$, $q=3$). For these the lattice with its standard form is a principally polarised abelian variety.
- **The pair $\pm\lambda$ is the common obstruction, but its share falls** as the graphs get larger and less symmetric: all classes for $K_4$ and $K_5$, 12 of 186 for the 4-regular graphs on 7 vertices.
- **Locks by a third turn occur on real graphs, with both signs.** In $K_7$, 1260 classes contain the pair $1\pm2\sqrt3$, locked with sign $+1$, and $\Omega$ is still a polarisation. Another 420 contain $-1$ together with $\tfrac12(1\pm\sqrt{57})$ (or the analogous triple with $\sqrt{33}$); these three modes share the field $\mathbb Q(\sqrt{-3},\sqrt{-19})$, one of the locks has sign $-1$, and $\Omega$ fails without any $\pm\lambda$ pair.


## 6. Reading

- **Locks are the finite-order symmetries that two modes share.** The step on a locked partner is the same step up to a half turn, a Hadamard, or a sixth turn. These are the rotations that are Clifford gates of a GKP lattice.
- **The half turn is special because the graph has it.** On a bipartite graph it is literal: reverse the sign on one side. There the right phase space is not two quadratures per vertex but one quadrature per vertex, positions on one side and momenta on the other, with the graph's own biadjacency matrix as the symplectic form.
- **For the direction TJO set.** In the understood case a mismatch between the vacuum and the arithmetic structure was traced to a hidden symmetry, and taking the symmetry into account (passing to the half lattice and to two steps) removed it. That is a pattern to look for, not a claim about $\zeta$.

## 7. Status and checks

| statement | status |
|---|---|
| the proposition of §1 | proved above; checked on eight pairs (L1) |
| the classification of §2 | follows from the roots of unity of imaginary quadratic fields; checked for primes $q<400$ (L2) |
| the prime-dependent lock | computed (L3), both by the rule and from the full splitting field |
| bipartite graphs: $\Gamma$, the half lattice, the biadjacency form, $F^2$ | elementary; checked exactly on $K_{3,3}$ and the cube for every flux (L4) |
| polarisation on the half lattice for the cube | by the locking rule; confirmed from the splitting field for four of the five spectra |
| "no graph symmetry behind the quarter and sixth turns" | not found; not a theorem |
| the scan | computed (L6); spectra whose real field is too large are reported as undecided |

## 8. Next

- **The half lattice for bipartite graphs is the better object.** Redo the tower and the vacuum on it: one quadrature per vertex, form $B_s$, Frobenius two steps.
- **Unimodular biadjacency.** Characterise the fluxes with $\det B_s=\pm1$; these give principally polarised varieties directly.
- **Non-bipartite graphs with a symmetric spectrum**, like $K_4$: the order-four symmetry suggests a structure over $\mathbb Z[i]$ in place of a real half.
