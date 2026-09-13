# Ramanujan conditions for boson–fermion cMPS

*13 September 2026*

There is a precise condition in $Q,R_\alpha$. But we need to specify
**the transfer sector that carries the zeros**, and the decay scale.
Fermionic statistics alone do not determine either.

There is also an important refinement to the previous work: an arbitrary
parity-covariant Lindbladian need not satisfy the additional algebraic
conditions of a regular boson–fermion cMPS.

For a translation-invariant cMPS, write $p_\alpha=0,1$ for bosonic and
fermionic species. With bond parity $P$, the usual conditions are

$$
PQP=Q,\qquad PR_\alpha P=(-1)^{p_\alpha}R_\alpha,
$$

and, for the standard finite-kinetic-energy regularity condition,

$$
R_\alpha R_\beta
=(-1)^{p_\alpha p_\beta}R_\beta R_\alpha.
$$

In particular, $R_f^2=0$. In left canonical form,

$$
Q=-iH-\frac12\sum_\alpha R_\alpha^\dagger R_\alpha,
\qquad H=H^\dagger.
$$

These are the mixed-species cMPS conditions from the
[cMPS calculus paper](https://arxiv.org/html/1211.3935).

The stationary bond density $\sigma$, when a density-matrix description
applies, additionally satisfies

$$
Q\sigma+\sigma Q^\dagger
+\sum_\alpha R_\alpha\sigma R_\alpha^\dagger=0.
$$

For the Phantasm, this is where the BC state enters.

The operator whose spectrum matters is built directly from these matrices.
In the observable convention, fermionic correlations propagate with the
parity-twisted transfer generator

$$
\mathcal K_f(X)=Q^\dagger X+XQ
+\sum_b R_b^\dagger X R_b
-\sum_f R_f^\dagger X R_f.
$$

The ordinary norm-transfer generator has **plus signs for every species**
and generates a completely positive semigroup. The minus signs above belong to the fermionic
correlation transfer. With the bond parity present, multiplication
$X\mapsto PX$ intertwines the two generators, preserving the odd operator
sector. [Transfer formulas](https://arxiv.org/html/1211.3935#S5)

Now let $\mathcal E$ be an invariant sector of this transfer operator—the
sector intended to represent the arithmetic zeros—and set
$A=\mathcal K_f|_{\mathcal E}$.

The natural one-sided Ramanujan condition is

$$
\operatorname{Re}\lambda\le-\Delta
\qquad(\lambda\in\operatorname{spec}A).
$$

If the arithmetic functional equation supplies the reflection
$\lambda\mapsto-2\Delta-\overline\lambda$, this becomes

$$
\operatorname{Re}\lambda=-\Delta.
$$

The grading itself does not supply that reflection. In our Riemann
normalization, $\Delta=\tfrac14$.

A particularly useful condition directly on the
$Q,R_\alpha$-constructed matrix $A$ is

$$
A^\dagger G+GA=-2\Delta G,\qquad G>0.
$$

It says that the transfer on $\mathcal E$ is **uniform damping plus unitary
evolution in the metric $G$**:

$$
e^{tA}=e^{-\Delta t}U_t,\qquad U_t^\dagger G U_t=G.
$$


For a finite-dimensional block, existence of such a $G$ is equivalent to
the critical-line spectrum **and diagonalizability**. Thus this is a
concrete matrix criterion, stronger than the bare spectral statement only
through its exclusion of Jordan blocks. Choosing $G$ from the BC and
symplectic structure would give it arithmetic content; the stationary
density does not automatically provide the required metric.

Why specify $\mathcal E$, rather than demand one rate throughout the odd
sector? A small regular example makes the distinction clear. Take two
fermionic bond modes:

$$
R_1=\sqrt\kappa\,c_1,\qquad R_2=\sqrt\kappa\,c_2,
$$


$$
H=g(c_1^\dagger c_2^\dagger+c_2c_1),\qquad
Q=-iH-\frac{\kappa}{2}(n_1+n_2).
$$

On the elementary odd sector

$$
\mathcal E=\operatorname{span}\{c_1,c_2,c_1^\dagger,c_2^\dagger\},
$$

the fermionic transfer eigenvalues are

$$
-\frac{\kappa}{2}\pm ig.
$$

But the full odd operator sector also contains

$$
-\frac{3\kappa}{2}\pm ig.
$$

I checked this characteristic polynomial exactly. The elementary modes
have one decay rate; higher operator sectors carry additional rates.

There is a further reason not to insist prematurely on the BC-state metric.
Writing $\|X\|_\sigma^2=\operatorname{Tr}(\sigma X^\dagger X)$, stationarity
gives the exact identity

$$
-2\operatorname{Re}\langle X,\mathcal K_fX\rangle_\sigma
=
\sum_b\|[R_b,X]\|_\sigma^2+
\sum_f\|\{R_f,X\}\|_\sigma^2.
$$

Regularity makes the right side vanish for $X=R_f$. Consequently, a
strictly positive instantaneous dissipation bound in this metric cannot
hold on a sector containing a nonzero $R_f$, even though its spectral
decay rates can all be positive.

So the promising formulation is: **find regular graded $Q,R_\alpha$, the
BC stationary state, and an arithmetically identified transfer sector
$\mathcal E$ on which the shifted transfer is skew-adjoint in a specified
positive metric.** The finite-dimensional equation above expresses that
target explicitly; extending it to the infinite Phantasm bond requires
control of the metric and operator domains.
