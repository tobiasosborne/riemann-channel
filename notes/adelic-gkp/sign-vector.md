# The per-mode sign: what the graph decides and what it does not

Author: `claude:fable-5.1`, 2026-10-05, at TJO's request ("Please study it": what on the signed graph decides the per-mode sign of `howe-positivity.md`). Status: **a record, not a round.** Nothing is registered in `db/claims.tsv`; no REFUTE review has run; no shard. Checks: `checks/check_sign_vector.py`, output `checks/output_sign_vector.txt` (19/19; needs PARI through `cypari2`).

**Verdict.**

- **For a single mode, nothing decides it.** The sign compares two ways of telling a mode's two Frobenius eigenvalues apart: by direction of rotation at the real place, and by attraction at $p$. For one mode both matchings occur. That is the freedom Deligne's construction leaves open.
- **What the graph decides is which modes are locked together, and with which sign.** Modes are grouped by the square class of the determinant of their Weil form, $q-\lambda^2/4$. Inside a group the relative signs are fixed by an explicit residue. Between groups they are free. This is proved below and agrees with PARI on 13 spectra and on all 527 ordinary Ramanujan flux classes of $K_4$, $K_5$, the cube and $K_6$.
- **So $\Omega$ is a polarisation exactly when every lock has sign $+1$.** A pair $\pm\lambda$ is always locked with sign $-1$, but it is not the only lock: for $q=5$ the eigenvalues 2 and 4 are locked with sign $-1$, and $-2$ and 4 with sign $+1$.
- **The $K_6$ flux has no locks at all**, which is why it works. Of the 527 flux classes, only the 120 with its spectrum or the mirror spectrum make $\Omega$ a polarisation.

## 1. One mode: two ways to tell the eigenvalues apart

A mode with eigenvalue $\lambda$ has Frobenius eigenvalues $\mu^\pm=\tfrac12(\lambda\pm\delta)$, with $\delta=i\sqrt{4q-\lambda^2}$. Both are fixed points of the same recursion,

$$
u\ \longmapsto\ \lambda-\frac qu ,
$$

which is how the step acts on the lines of the mode's phase plane.

| | at the real place | at $p$ |
|---|---|---|
| the recursion is | a rotation (when $\lvert\lambda\rvert<2\sqrt q$): it never settles | a contraction: it converges to the unit root |
| the two roots are told apart by | direction of rotation; adding $+i0$ to $\lambda$ selects $\mu^+$ | attraction: the unit root attracts, the non-unit repels |
| the invariant structure is | a point: the vacuum | two lines: $\mathbb Z_p^2$ splits into a unit-root line and a non-unit line |
| on the space of GKP lattices | the normalised step rotates about the vacuum | the step moves one edge along a line of the tree of $p$-adic lattices |

So **a Ramanujan ordinary mode is a rotation at the real place and a translation at $p$** (S1 checks the recursion at both places and the splitting; the tree statement is the standard description of a matrix whose eigenvalues have valuations 0 and 1). The kernel tower $M^kL$ of `lattice-tower.md` is the walk along that line.

The sign of the mode is $\sigma=+1$ when the root that rotates forwards, $\mu^+$, is the $p$-adic non-unit. Nothing on the mode fixes this: it is the choice of which $p$-adic square root of $\lambda^2-4q$ is called $\delta$. Changing it is the same as reversing the orientation of the mode's phase plane.

## 2. Several modes: the locking rule

Let $\lambda_1,\dots,\lambda_m$ be the distinct fermionic eigenvalues, $D_j=\lambda_j^2-4q<0$, and $N^+$ the totally real field they generate with its conjugates. Fix a prime $\mathfrak{p}^+$ of $N^+$ above $p$.

**Theorem.** Let $\mathrm{Rel}$ be the set of subsets $I$ for which $\prod_{j\in I}D_j$ is a square in $N^+$; such $I$ have even size. For $I\in\mathrm{Rel}$ put

$$
\rho_I=(-1)^{\lvert I\rvert/2}\,\frac{\sqrt{\prod_{j\in I}D_j}}{\prod_{j\in I}\lambda_j}\ \in N^+\quad(\text{positive square root}),\qquad \tau_I=\begin{cases}+1&\mathrm{val}_{\mathfrak{p}^+}(\rho_I-1)>\mathrm{val}_{\mathfrak{p}^+}(\rho_I+1)\\-1&\text{otherwise.}\end{cases}
$$

Then the sign vectors realised by the primes above $\mathfrak{p}^+$ are exactly the solutions of

$$
\prod_{j\in I}\sigma_j=\tau_I\qquad\text{for all}\ I\in\mathrm{Rel}.
$$

*Proof.*
1. Each $\mathfrak{p}^+$ splits in $N^+(\delta_j)$: otherwise $\mu_j^+$ and $\mu_j^-$ would be conjugate over the completion and have the same valuation, but one is a unit and the other is not.
2. So $\mathfrak{p}^+$ splits completely in $N=N^+(\delta_1,\dots,\delta_m)$, and $\mathrm{Gal}(N/N^+)$ permutes the primes above it simply transitively.
3. An element $g$ of that group sends $\delta_j$ to $\chi_j(g)\delta_j$ with $\chi_j(g)=\pm1$, hence $\mu_j^+$ to $\mu_j^{\chi_j(g)}$, hence $\sigma_j(g\mathfrak{P})=\chi_j(g)\sigma_j(\mathfrak{P})$. By Kummer theory the vectors $(\chi_j(g))_j$ are exactly those with $\prod_I\chi_j=1$ for all $I\in\mathrm{Rel}$. So the realised sign vectors form one coset of that group.
4. The coset is fixed by the products over $I\in\mathrm{Rel}$. Since $\mu_j^+=\tfrac12(\lambda_j+\delta_j)$ is a non-unit exactly when $-\delta_j/\lambda_j$ is congruent to $+1$, the product $\prod_I\sigma_j$ is the residue of $\prod_I(-\delta_j/\lambda_j)=\rho_I$. ∎

**In terms of the modes.** $-D_j/4=q-\lambda_j^2/4$ is the determinant of the Weil form on mode $j$. Two modes are locked when these determinants agree up to a square, which is when their lattices in vacuum coordinates have complex multiplication by the same field. A larger set is locked when the product of its determinants is a square.

**Corollary.** $\Omega$ or $-\Omega$ is a polarisation, for some choice of Deligne's embedding, exactly when there is a $\mathfrak{p}^+$ with $\tau_I=+1$ for every $I\in\mathrm{Rel}$. If the determinants are independent modulo squares, it always is.

## 3. Rational eigenvalues: a one-line rule

For integer eigenvalues write $4q-\lambda^2=d\,m^2$ with $d$ squarefree and $m>0$. Two eigenvalues are locked when they have the same $d$, and then for odd $p$

$$
\sigma_{\lambda}\sigma_{\lambda'}=+1\iff\frac{\lambda}{m}\equiv\frac{\lambda'}{m'}\pmod p
$$

(both sides are square roots of $-d$ modulo $p$). Checked against PARI on every such pair for $q=7$, $5$ and $2$ (S3).

| $q$ | eigenvalues | field | $\lambda/m$ mod $p$ | lock |
|---|---|---|---|---|
| 7 | 1 and 5 | $\mathbb Q(\sqrt{-3})$ | 5 and 5 | $+1$ |
| 7 | 1 and 4 | $\mathbb Q(\sqrt{-3})$ | 5 and 2 | $-1$ |
| 7 | 4 and 5 | $\mathbb Q(\sqrt{-3})$ | 2 and 5 | $-1$ |
| 7 | $-4$ and 1 | $\mathbb Q(\sqrt{-3})$ | 5 and 5 | $+1$ |
| 5 | 2 and 4 | $\mathbb Q(i)$ | 3 and 2 | $-1$ |
| 5 | $-2$ and 4 | $\mathbb Q(i)$ | 2 and 2 | $+1$ |
| any | $\lambda$ and $-\lambda$ | the same | opposite | $-1$ |

## 4. Tests

For each spectrum the realised sign vectors were computed in two ways: from the valuations of the Frobenius eigenvalues at every prime of the full splitting field (PARI), and from the theorem using the real field only. They agree in all cases (S2).

| $q$ | fermionic eigenvalues | relations | sign vectors realised | $\Omega$ a polarisation |
|---|---|---|---|---|
| 2 | $\pm1,\ \pm\sqrt5$ ($K_4$, one negative edge) | 2 independent | 4 of 16 | no |
| 5 | $-1$, roots of $x^3-3x^2-9x+19$ (the $K_6$ flux) | none | 16 of 16 | yes |
| 5 | $2,\ 4$ | 1 | 2 of 4 | no |
| 5 | $-2,\ 4$ | 1 | 2 of 4 | yes |
| 5 | $1,\ 2,\ 4$ | 1 | 4 of 8 | no |
| 7 | $1,\ 5$ | 1 | 2 of 4 | yes |
| 7 | $1,\ 4$ | 1 | 2 of 4 | no |
| 7 | $4,\ 5$ | 1 | 2 of 4 | no |
| 7 | $-4,\ 1,\ 5$ | 2 independent | 2 of 8 | yes |
| 7 | $1,\ 4,\ 5$ | 2 independent | 2 of 8 | no |
| 5 | $1\pm2\sqrt3$ | 1 | 2 of 4 | yes |
| 3 | $\tfrac{1\pm\sqrt5}2$ | none | 4 of 4 | yes |
| 2 | $\tfrac{1\pm\sqrt5}2$ | none | 4 of 4 | yes |

The pair $1\pm2\sqrt3$ is a lock between two conjugate irrational modes: both determinants are $-1$ times a square in $\mathbb Q(\sqrt3)$.

## 5. The graphs

All flux classes of $K_4$ ($q=2$), $K_5$ ($q=3$), the cube ($q=2$) and $K_6$ ($q=5$) that are Ramanujan and ordinary: 18 spectra, 527 classes (S4).

| graph | ordinary Ramanujan flux classes | with a $\pm\lambda$ pair | $\Omega$ a polarisation |
|---|---|---|---|
| $K_4$ | 6 | 6 | 0 |
| $K_5$ | 20 | 20 | 0 |
| cube | 31 | 31 | 0 |
| $K_6$ | 470 | 350 | 120 |

Every failure in this sample comes from a $\pm\lambda$ pair, most often $\pm1$. The 120 successes are the $K_6$ classes with spectrum $-1,-1,-1$ and the roots of $x^3-3x^2-9x+19$, or the mirror spectrum.

**The $K_6$ flux mode by mode.** It has four groups of modes and no locks:

- the eigenvalue $-1$, three times, with determinant $19/4$ and field $\mathbb Q(\sqrt{-19})$;
- three conjugate eigenvalues $-2.759,\ 1.695,\ 4.064$ in a cyclic cubic field, whose three determinants are independent modulo squares.

So all sixteen sign vectors occur, each at exactly one of the sixteen primes above 5, and at one of them the vacuum and the arithmetic structure agree on every mode.

## 6. Reading

- **The sign is an orientation, and only relative orientations are real.** For each mode the vacuum orients the phase plane by the direction of rotation; the prime orients it by which eigen-line attracts. A single mode cannot tell whether the two agree. Two modes whose lattices have the same complex multiplication field can, and the answer is the residue of §2.
- **The standard form $\Omega$ orients every mode by the vacuum.** It is the arithmetic polarisation exactly when the vacuum's orientations are coherent with the prime's on every locked set.
- **For the direction TJO set (understood cases first).** In the understood case the same step is a rotation at the real place and a translation at $p$. Weil positivity, the vacuum, is a statement at the real place alone. Being an abelian variety with $\Omega$ as polarisation is a statement of coherence between the real place and $p$, and it can fail while Weil positivity holds.

## 7. Status and checks

| statement | status |
|---|---|
| the recursion at the two places; splitting of $\mathbb Z_p^2$ | elementary; checked (S1) |
| the step as a one-edge translation on the tree of $p$-adic lattices | standard; not separately checked |
| the theorem and corollary of §2 | proved above; agree with PARI on 13 spectra (S2) and on the flux classes without a $\pm\lambda$ pair (S4) |
| the rule of §3 | consequence of the theorem for odd $p$; checked on all pairs for $q=7,5$ and by the general rule for $q=2$ (S3) |
| the scan of §5 | computed (S4); for classes with a $\pm\lambda$ pair the outcome is the proposition of `howe-positivity.md` and PARI was not run on the full splitting field |
| §6 | reading |

The proof of step 1 uses ordinariness only. For $p=2$ the residue is read through the valuation comparison in the definition of $\tau_I$.

## 8. Next

- **A graph meaning for the lock sign.** The rule is in terms of eigenvalues. For the lock $\pm\lambda$ there is a graph symmetry behind it (the signed permutation of `howe-positivity.md` §3). Is there one behind the lock of 2 and 4 at $q=5$?
- **Which fluxes have no locks.** Characterise the signed graphs whose Weil-form determinants are independent modulo squares; these are the ones where the lattice with its standard form is an abelian variety.
- **The arithmetic orientation as a second form.** When $\Omega$ fails, the twist $P$ of `howe-positivity.md` §4 is a unit with prescribed signs on the locked sets. Decide when such a unit exists in general.
