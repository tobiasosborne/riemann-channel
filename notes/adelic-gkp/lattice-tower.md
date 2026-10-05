# The tower of lattices

Author: `claude:fable-5.1`, 2026-10-05, at TJO's request ("please then investigate the tower of lattices"), under the steer given the same day: "Let us find the natural QI interpreations on the cases we understand *then* try to match to corresponding analogous setting for standard RH. Not the other way around." Status: **a record, not a round.** Nothing is registered in `db/claims.tsv`; no REFUTE review has run; no shard. Continues `graph-super.md`. Checks: `checks/check_lattice_tower.py`, output `checks/output_lattice_tower.txt` (45/45).

**Verdict.**

- **The tower has a clean reading.** Level $k$ is a GKP code whose basis is the qunaught displaced by the syndromes of period $k$. Its dimension is the number of points over $\mathbb F_{q^k}$, its logical Paulis are the Heisenberg group of the group of points, and the step acts on it as a logical Clifford of order $k$. The places are the orbits of that Clifford.
- **The tower is blind to RH.** A step that violates RH has every piece of it. This is a negative finding: the tower is not where positivity lives.
- **RH is one extra datum: a vacuum invariant under the normalised step.** With it the step is a rotation and dilation of the lattice, the lattice has complex multiplication, the zeros are the frequencies of harmonic oscillators, and every level of the tower is a scaled copy of the lattice.
- **In the ordinary case this is a theorem, not an analogy.** The lattice with its step is a Deligne module, and Deligne's theorem says these are exactly the ordinary abelian varieties over $\mathbb F_q$. The one-mode case is the notebook's Deninger elliptic solenoid.
- **What to carry to the standard case** is therefore the vacuum, not the tower (§7).

## 1. Setting

$L=\mathbb Z^{2n}$ with the standard symplectic form $\Omega$ is the stabiliser lattice of $n$ GKP qunaught modes, and $\mathbb R^{2n}/L$ is their torus of displacement syndromes. A **step** is an integer matrix $M$ with $M^T\Omega M=q\,\Omega$. Its adjoint for $\Omega$ is $V=qM^{-1}$, also an integer matrix, and $MV=VM=q$. For a graph with a flux, $M=\begin{pmatrix}0&-1\\q&A_s\end{pmatrix}$ (`graph-super.md`).

| example | $n$ | $q$ | eigenvalues of $M$ | where it comes from |
|---|---|---|---|---|
| E mode | 1 | 2 | $\mu=\tfrac{-1\pm\sqrt{-7}}2$ | the fermionic mode of $K_4$ with Pauli letters |
| Pauli six | 1 | 5 | $\mu=-1\pm2i$ | the notebook's Pauli-qubit elliptic curve (shard 03c) |
| $K_4$, one negative edge | 4 | 2 | four pairs on $\lvert\mu\rvert=\sqrt2$ | `graph-super.md` |
| hyperbolic step | 1 | 5 | $\mu=\tfrac{5\pm\sqrt5}2$, real | a contrast that violates RH; not from a graph |

## 2. The point tower

**The codes.** Put $L_k=(1-V^k)L$. It is a sublattice of $L$, so it is the stabiliser lattice of a GKP code $\mathcal C_k$. A displaced qunaught $W(e)\vert L\rangle$ lies in $\mathcal C_k$ exactly when

$$
\Omega\bigl((1-V^k)y,\,e\bigr)=\Omega\bigl(y,\,(1-M^k)e\bigr)\in\mathbb Z\ \ \text{for all}\ y\in L,\qquad\text{that is,}\qquad M^ke\equiv e\ \ (\mathrm{mod}\ L).
$$

So:

- **Basis.** $\mathcal C_k$ is spanned by the qunaught displaced by the syndromes of period $k$. Distinct syndromes give orthogonal states.
- **Dimension.** $\dim\mathcal C_k=h_k=\det(1-M^k)$, the number of points over $\mathbb F_{q^k}$.
- **Nesting.** $\mathcal C_d\subset\mathcal C_k$ when $d$ divides $k$. A field extension is a code extension.
- **Logical Paulis.** Displacements by periodic syndromes are the logical shifts; the stabilisers of $L$, taken modulo $L_k$, are the logical phases. Together they are the Heisenberg group of the finite group of points $G_k=L/(1-M^k)L$, acting irreducibly (W5). This is the finite Heisenberg group that analytic §13 said the bond lacked.
- **The step is a logical Clifford.** $\Phi:W(e)\vert L\rangle\mapsto W(Me)\vert L\rangle$ permutes the basis, sends the shift by $e$ to the shift by $Me$ and the phase $Z_\lambda$ to $Z_{V^{-1}\lambda}$, and preserves their commutation pairing. On $\mathcal C_k$ it has order dividing $k$: it is the Galois group of $\mathbb F_{q^k}$ over $\mathbb F_q$, acting by Cliffords.
- **Places.** The orbits of $\Phi$ on the basis are the closed points. An orbit of size $d$ is a place of degree $d$.

| $k$ | $h_k$ for the E mode | group of points | orbits of the step (size: number) |
|---|---|---|---|
| 1 | 4 | $\mathbb Z_4$ | 1: 4 |
| 2 | 8 | $\mathbb Z_8$ | 1: 4, 2: 2 |
| 3 | 4 | $\mathbb Z_4$ | 1: 4 |
| 4 | 16 | $\mathbb Z_{16}$ | 1: 4, 2: 2, 4: 2 |
| 5 | 44 | $\mathbb Z_{44}$ | 1: 4, 5: 8 |
| 6 | 56 | $\mathbb Z_{56}$ | 1: 4, 2: 2, 6: 8 |
| 7 | 116 | $\mathbb Z_{116}$ | 1: 4, 7: 16 |
| 8 | 288 | $\mathbb Z_3\times\mathbb Z_{96}$ | 1: 4, 2: 2, 4: 2, 8: 34 |

For $K_4$ with one negative edge the first three levels have dimensions $32$, $1024$, $4256$.

**The zeta function from the tower.** Two traces of the same step give the count:

$$
\underbrace{\mathrm{Tr}\bigl(\Phi^j\,\big\vert\,\mathcal C_k\bigr)}_{\text{a unitary on a code}}=h_{\gcd(j,k)},\qquad h_k=\underbrace{\sum_i(-1)^i\,\mathrm{Tr}\,\Lambda^iM^k}_{\text{supertrace on the fermionic Fock space}} .
$$

- The left side is the Euler product: on the union of all levels, $1/\det(1-u\Phi)=\prod_{\text{orbits}}(1-u^{d})^{-1}$. **The Euler product is the cycle decomposition of a logical Clifford.** Because $\Phi$ is unitary, this side is positive for free and says nothing about RH.
- The right side is the cohomological side, where the zeros are the one-fermion states (`graph-super.md` §4).
- The Lefschetz formula is their equality: **the trace of the logical Clifford on the code equals the supertrace of the step on the Fock space of phase space.**

This is the zeta-level statement I was looking for on the previous page. It needs no comb and no overlap.

## 3. The kernel tower

The lattices $M^kL$ form a second tower, of index $q^{nk}$: codes of $n$ registers with $q^k$ levels each ($L/M^3L$ is $\mathbb Z_8$ for the E mode and $\mathbb Z_8^4$ for $K_4$ with one negative edge). On it the step is a lowering operator: it kills every syndrome after finitely many steps and contributes nothing to any trace.

The two towers are the two halves of one decomposition. Every torsion syndrome is uniquely a periodic one plus one that the step kills (W9: among the 24-torsion syndromes of the E mode, $72$ periodic times $8$ killed is $576$). The point tower is the recurrent part of the dynamics and the kernel tower is the transient part.

## 4. The tower is blind to RH

The hyperbolic step has real eigenvalues $3.618$ and $1.382$, so it violates RH. It still has all of §2 and §3: codes of dimensions $1,11,76,451,2501$, a Heisenberg group of logical Paulis at each level, the step as a logical Clifford, places, both towers (W2, W6).

What differs is only how the two towers compare in size:

| $k$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $h_k/q^{k}$, E mode ($q=2$) | 2.0 | 2.0 | 0.5 | 1.0 | 1.375 | 0.875 |
| window allowed by RH for $q=2$: $1\pm$ | 1.91 | 1.25 | 0.83 | 0.56 | 0.39 | 0.27 |
| $h_k/q^{k}$, hyperbolic step ($q=5$) | 0.2 | 0.44 | 0.61 | 0.72 | 0.80 | 0.86 |
| window allowed by RH for $q=5$: $1\pm$ | 1.09 | 0.44 | 0.19 | 0.08 | 0.04 | 0.02 |

RH says $\lvert h_k/q^{nk}-1\rvert\le(1+q^{-k/2})^{2n}-1$: the code of period-$k$ syndromes and the code of $k$ registers have the same dimension up to square-root error. The E mode stays inside its window (at $k=5$ only just). The hyperbolic step approaches 1 at the slower rate $1.382^{-k}$ and is outside its window from $k=2$ on.

So the tower is kinematics, in the notebook's sense. Any integer step with $M^T\Omega M=q\Omega$ has it.

## 5. Where RH lives: an invariant vacuum

Normalise the step: $S=M/\sqrt q$ is symplectic, so it is a Gaussian unitary on the $n$ modes.

**Statement (standard; the notebook has the abstract form as `thm:deninger-invariant-polarisation`).** The following are equivalent: (i) all eigenvalues of $M$ have modulus $\sqrt q$ and $M$ is semisimple; (ii) the Weil form $\tfrac12\Omega(M-V)$ is positive definite; (iii) there is a pure Gaussian state, a vacuum, that $S$ leaves invariant. A vacuum is a complex structure $J$ on phase space with $\Omega(\cdot,J\cdot)>0$, and invariance is $JS=SJ$. A polarisation, in the sense of the Deninger shards, is an invariant vacuum.

With the vacuum in hand (W7):

- **The zeros are oscillator frequencies.** In the normal modes of the vacuum, $S$ is a rotation by $\theta_j$ in the $j$-th mode, so its Gaussian unitary is one period of $n$ harmonic oscillators, $\exp\bigl(-i\sum_j\theta_j(\hat n_j+\tfrac12)\bigr)$. The Hilbert–Pólya operator is this oscillator Hamiltonian and its positivity is Weil positivity. For $K_4$ with one negative edge the frequencies are $\theta/\pi=0.210,\ 0.385,\ 0.615,\ 0.790$.
- **The trivial pair is an inverted oscillator.** On the uniform bosonic mode $S$ is a pure squeeze by $\sqrt q$, generated by $\tfrac12(xp+px)$. A step that violates RH has further inverted oscillators.
- **The counts are distances.** $h_k=\prod_j\lvert1-q^{k/2}e^{ik\theta_j}\rvert^2$.
- **The lattice has a shape, and complex multiplication.** For one mode, the coordinate $z=\bar\mu x_1+x_2$ turns the step into multiplication by the complex number $\mu$. The lattice with the invariant metric is the binary quadratic form $qx^2+\lambda xy+y^2$, of discriminant $\lambda^2-4q$.

| example | quadratic form | discriminant | the lattice in vacuum coordinates |
|---|---|---|---|
| E mode | $2x^2-xy+y^2$ | $-7$ | $\mathbb Z\bigl[\tfrac{1+\sqrt{-7}}2\bigr]$ |
| Pauli six | $5x^2-2xy+y^2$ | $-16$ | $\mathbb Z+2i\,\mathbb Z$, a 1 by 2 rectangle |
| hyperbolic step | $5x^2+5xy+y^2$ | $+5$ | none: the form is indefinite |

RH for one mode is the statement that the discriminant is negative, so that the lattice is a lattice in the complex plane. The square and hexagonal GKP lattices have a rotation symmetry; these have instead a rotation and dilation of norm $q$ that maps the lattice into itself. A violating step is a real quadratic lattice, like the unit of $\mathbb Q(\sqrt2)$ in note §14 but of norm $q$.

![Two panels showing the lattice of the E mode in vacuum coordinates. Left: the lattice with its sublattices M L of index 2 and M squared L of index 4. Right: the lattice with its sublattices (1 minus M) L of index 4 and (1 minus M squared) L of index 8. Every sublattice is a rotated and scaled copy of the lattice.](fig_tower_lattice.png)

*Figure. The E mode in vacuum coordinates; the dashed circle is the vacuum's uncertainty disc. Every lattice of either tower is a rotated and scaled copy of $L$: the tower is self-similar. Without a vacuum there is no such picture.*

## 6. In the ordinary case this is an abelian variety

Goresky and Tai, recalling Deligne (`refs/src/1701.07742/main.tex:561-571`): a **Deligne module** of rank $2n$ over $\mathbb F_q$ is a pair $(T,F)$, $T$ a free $\mathbb Z$-module of rank $2n$ and $F$ an endomorphism, such that (1) $F$ is semisimple with all eigenvalues of modulus $\sqrt q$; (2) half its eigenvalues are $p$-adic units and half are divisible by $q$; (3) the middle coefficient of its characteristic polynomial is prime to $p$; (4) there is $V$ with $FV=VF=q$. **Deligne's theorem** (`:586-591`): the category of $n$-dimensional ordinary abelian varieties over $\mathbb F_q$ is equivalent to the category of Deligne modules of rank $2n$, with $T=H_1$ of the canonical lift (`:580-584`).

Our $(L,M)$ always satisfies (4). Condition (1) is RH with semisimplicity. Condition (3) is ordinariness, and it gives (2) here because $q$ is prime.

| example | characteristic polynomial of $M$ | (1) | (3) | Deligne module |
|---|---|---|---|---|
| E mode | $x^2+x+2$ | yes | yes | yes, over $\mathbb F_2$ |
| Pauli six | $x^2+2x+5$ | yes | yes | yes, over $\mathbb F_5$ |
| $K_4$, one negative edge | $x^8+2x^6+5x^4+8x^2+16$ | yes | yes | yes, rank 8 over $\mathbb F_2$ |
| hyperbolic step | $x^2-5x+5$ | no | no | no |

So for these three the fermionic sector **is** an ordinary abelian variety over $\mathbb F_q$, of dimension 1, 1 and 4, and:

- the GKP lattice is $H_1$ of its canonical lift, and the syndrome torus is the lift's complex points;
- the level-$k$ code is $\ell^2$ of its $\mathbb F_{q^k}$-points;
- the vacuum is the complex structure of the lift **only when a sign condition holds** (one mode: yes; $K_4$ with one negative edge: no). Corrected in `howe-positivity.md`, which carries out the check below;
- the one-mode case is the leaf space of Deninger's elliptic solenoid, which the notebook already matched to its doubled Hodge bond (`prop:deninger-elliptic-hodge-ket`).

Three limits of this identification:

- Petersen with the dodecahedral flux and $K_5$ with the pentagon flux have the eigenvalue $0$, a supersingular factor, so they are not ordinary and Deligne's theorem does not cover them.
- $\Omega$ satisfies Howe's adjunction condition $\omega(Fx,y)=\omega(x,Vy)$ (`:602`), but a polarisation also needs positivity for the CM type fixed by Deligne's embedding (`:604-607`). **Checked afterwards in `howe-positivity.md`:** it holds (up to the sign of $\Omega$) for the two one-mode examples and fails for $K_4$ with one negative edge, where a twisted form $\Omega(x,Py)$ is the principal polarisation.
- That the group of points is $L/(1-M^k)L$ as a group, and not only in order, is quoted from memory.

Deninger's warning applies with a difference (`cit:deninger-lift-misleading`): a curve almost never lifts together with its Frobenius, but an ordinary abelian variety does, and it is the abelian variety that the lattice sees.

## 7. What to carry to the standard case

Following the steer, these are the readings that are natural in the understood case, stated as things to look for and not as claims about $\zeta$.

1. **Do not look for RH in the tower.** Levels, codes, logical Paulis and the Galois Clifford exist with or without RH. The level-$N$ Bell pairs of note §4 are the same kind of structure and should be expected to be equally blind.
2. **The datum that carries RH is a vacuum invariant under the normalised step.** It is a structure on phase space, that is on $H_1$, and not on the space the points live in. This fits Deninger's remark that a conformal metric will not exist for number fields and that the identities are needed on cohomology (`cit:deninger-conformal-metric`).
3. **Zeros are oscillator frequencies; the squeeze is the trivial pair.** In the understood case the normalised step rotates the fermionic modes and squeezes only the uniform bosonic mode. This differs from the reading on `weil-positivity-spectroscopy.md`, where the zeros were squeeze frequencies. The understood case says the generator whose spectrum is the zeros is a positive oscillator Hamiltonian, and $\tfrac12(xp+px)$ belongs to the poles.
4. **Lefschetz is "code trace equals Fock supertrace".** The Euler product is the cycle decomposition of a unitary and is positive for free; the content is on the supertrace side.

## 8. Status and checks

| statement | status |
|---|---|
| the point tower: codes, bases, dimensions, nesting, logical Heisenberg group, the step as a logical Clifford, places as orbits | elementary; checked exactly (W2, W5); the usual sign convention for the stabilisers of $L$ is assumed |
| kernel tower; periodic plus killed decomposition | elementary (Fitting); checked (W6, W9) |
| blindness of the tower | checked on the hyperbolic step (W2, W6, W7) |
| invariant vacuum, normal modes, invariant Gaussian state, counts as distances | standard (Williamson; `thm:deninger-invariant-polarisation`); checked classically (W7). The oscillator form of the Gaussian unitary is standard and not checked here |
| lattice shape and complex multiplication for one mode | elementary; checked (W7) |
| Deligne modules and Deligne's theorem | cited by line from Goresky–Tai on disk; conditions checked for the examples (W8) |
| polarisation positivity; group structure of the points | not checked; the second is from memory |
| §7 | readings to test, not results |

Checks: `checks/check_lattice_tower.py`, 45 of 45 pass, exact arithmetic except the vacuum (float64).

## 9. Next

- **Howe's positivity:** done, see `howe-positivity.md`.
- **Which abelian variety.** For $K_4$ with one negative edge, the characteristic polynomial factors as $(x^4+3x^2+4)(x^4-x^2+4)$; identify the isogeny factors (two elliptic curves with traces $\pm1$ and an abelian surface) and whether the whole is a Jacobian or a Prym.
- **The non-ordinary examples.** Petersen and $K_5$ need the description of abelian varieties over a prime field that allows supersingular factors.
- **The matching question of §7.2,** in the notebook's own terms: an invariant vacuum on the odd bond of shard 04t.
