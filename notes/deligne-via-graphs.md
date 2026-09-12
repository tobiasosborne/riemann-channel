# Deligne's proof, told through regular graphs

*Expository. Nothing here is new; the point is to isolate what is actually hard in the proof of the Riemann hypothesis over finite fields, using the Ihara zeta of a regular graph as the running model. Written 2026-09-11 for the riemann-channel notebook.*

## 1. One graph, two sides

Take a finite connected graph in which every vertex has exactly $q+1$ neighbours. A walk is *non-backtracking* if it never immediately retraces an edge. Count closed non-backtracking walks of length $m$ (closed in the strong sense: the last step must not be the reverse of the first), and call that number $N_m$. It is a count, so $N_m \ge 0$.

**Side A: orbits.** Package the counts as a generating function

$$
\zeta_X(u) = \exp\Bigl(\sum_{m\ge1} \frac{N_m}{m} u^m\Bigr) = \prod_{P} \bigl(1 - u^{\ell(P)}\bigr)^{-1},
$$

where the product runs over *prime cycles* $P$: closed non-backtracking walks that are not a repetition of a shorter one, taken up to choice of starting point. The product form is the Euler product; the prime cycles are the primes of the graph and $\ell(P)$ is the length. This is the Ihara zeta.

**Side B: a small matrix.** Let $T$ be the matrix indexed by directed edges, with $T_{ef} = 1$ when $f$ can follow $e$ without backtracking. Then $N_m = \operatorname{Tr} T^m$, so

$$
\zeta_X(u) = \frac{1}{\det(1 - uT)}.
$$

The counts on side A are the power sums of the eigenvalues of $T$. Nothing has been proved yet: this is bookkeeping. $T$ has $2|E|$ rows, which is as large as the data.

**The compression.** Bass's theorem compresses $T$ to the ordinary adjacency matrix $A$ on vertices:

$$
\det(1 - uT) = (1-u^2)^{|E|-|V|}\det\bigl(1 - uA + q u^2\bigr).
$$

So the eigenvalues of $T$ are: $\pm 1$ with multiplicity $|E|-|V|$ each, and for every eigenvalue $\lambda$ of $A$ the two roots $\mu, \mu'$ of

$$
\mu^2 - \lambda \mu + q = 0, \qquad \mu\mu' = q, \quad \mu+\mu' = \lambda .
$$

The eigenvalue $\lambda = q+1$ (the constant vector) gives $\mu = q$ and $\mu = 1$. Call these, and the $\pm1$, the *trivial* eigenvalues. Everything else is *nontrivial*.

**Reading the walk count.** Putting it together,

$$
N_m = q^m + 1 + \sum_{\mu\ \text{nontrivial}} \mu^m + (|E|-|V|)\bigl(1 + (-1)^m\bigr)
$$

(plus terms from $\lambda = -(q+1)$ if the graph is bipartite). The leading term $q^m$ says closed walks multiply by $q$ per step, the growth rate of the tree. The nontrivial eigenvalues are the *error term* in the walk count.

**Riemann hypothesis for the graph.** Since $\mu\mu' = q$, the pair $\mu, \mu'$ either both have modulus $\sqrt q$ (when $|\lambda| \le 2\sqrt q$, they are complex conjugates) or are both real with one of them larger than $\sqrt q$ (when $|\lambda| > 2\sqrt q$). So

$$
\text{all nontrivial } |\mu| = \sqrt q
\quad\Longleftrightarrow\quad
\text{all nontrivial } |\lambda| \le 2\sqrt q
\quad\Longleftrightarrow\quad
\text{the error term in } N_m \text{ is } O(q^{m/2}).
$$

The middle statement is the definition of a Ramanujan graph. The right-hand statement is what the Riemann hypothesis *means*: closed walks are as evenly spread as they could possibly be, with square-root cancellation in the error.

**Two examples from the founding session.** $K_4$ has $q=2$, adjacency eigenvalues $3, -1, -1, -1$, hence $\mu = (-1 \pm i\sqrt7)/2$ with $|\mu|^2 = 2$: Ramanujan, and $N_3 = 8 + 1 + 6\cdot\tfrac52 = 24$, the twenty-four oriented, pointed triangles. The prism $C_{16}\times K_2$ has an eigenvalue $2\cos(\pi/8)+1 \approx 2.848 > 2\sqrt2 \approx 2.828$: a real pole slightly inside the circle, and the walk count has an error term growing faster than $2^{m/2}$. A long thin graph always fails: a bottleneck gives an eigenvalue $\lambda$ close to $q+1$, hence a real $\mu$ close to $q$, and walks pile up on one side of the bottleneck instead of spreading.

## 2. The same statement for a curve, with one sign changed

Now the object Deligne is concerned with. A curve $C$ over the field with $q$ elements has $N_m$ points over the field with $q^m$ elements. Again a count, again $N_m \ge 0$, and again a generating function with an Euler product,

$$
Z_C(t) = \exp\Bigl(\sum_{m \ge 1} \frac{N_m}{m} t^m\Bigr) = \prod_{x} \bigl(1 - t^{\deg x}\bigr)^{-1},
$$

the product over closed points $x$ (orbits of Frobenius on the points over the algebraic closure). The closed points are the prime cycles; $\deg x$ is the orbit length. Side A is identical in form.

Side B for the curve says: there is a $2g\times 2g$ matrix $F$ ($g$ the genus) with

$$
N_m = q^m + 1 - \operatorname{Tr} F^m = q^m + 1 - \sum_{i=1}^{2g} \alpha_i^m ,
\qquad
Z_C(t) = \frac{\det(1 - tF)}{(1-t)(1-qt)} .
$$

Line this up with the graph:

| | graph | curve |
|---|---|---|
| count | closed non-backtracking walks | points over $\mathbb F_{q^m}$ |
| leading term | $q^m + 1$ | $q^m + 1$ |
| error term | $+\sum \mu^m$ | $-\sum \alpha^m$ |
| pairing | $\mu \leftrightarrow q/\mu$ | $\alpha \leftrightarrow q/\alpha$ |
| where the interesting eigenvalues sit | poles of $\zeta_X$ | zeros of $Z_C$ |
| RH | $\lvert\mu\rvert = \sqrt q$ | $\lvert\alpha\rvert = \sqrt q$ |

Everything matches except the sign of the error term, and hence whether the interesting eigenvalues are poles or zeros. For the graph, $\zeta_X$ is the reciprocal of a polynomial and every eigenvalue is a pole. For the curve, the trivial eigenvalues $1$ and $q$ are poles and the interesting ones are zeros. This is the sign you met last session in the Artin–Schreier computation, $S_n = -\sum \alpha_i^n$, and in the explicit formula for $\zeta$, where the zeros are subtracted from the prime count. Keep it in view; it will turn out to be one of the three things the proof runs on.

For a variety of dimension $n$ the pattern repeats with more terms: $N_m$ is an alternating sum of traces over $n+1$ blocks, block $i$ having eigenvalues of modulus $q^{i/2}$, the top and bottom blocks being the single eigenvalues $q^n$ and $1$. RH is "block $i$ has modulus exactly $q^{i/2}$", and the one that matters is the middle block, $i = n$.

## 3. What is cheap and what is not

**Cheap: side B exists.** For graphs it is bookkeeping ($T$) plus Bass's identity. For varieties it is Grothendieck's trace formula, which is heavy technology but conceptually the same move: the count is the trace of a power of a finite matrix. Rationality of the zeta function is this statement and nothing more.

**Cheap: the pairing.** For graphs, $\mu\mu' = q$ falls out of Bass. For varieties it is Poincaré duality. Either way, once one proves $|\mu| \le \sqrt q$ for every nontrivial $\mu$, the pairing gives $|\mu| \ge \sqrt q$ as well and RH follows. So the whole problem is a one-sided bound.

**Cheap: the trivial bound.** Since counts are nonnegative and cannot exceed the number of walks (or points) available, the Euler product converges for $|u| < 1/q$. For the graph this says every $|\mu| \le q$, the Perron bound, which is exactly what one gets by noting that $T$ has nonnegative entries and row sums $q$. For a curve it gives $|\alpha| \le q$ by a similar argument. The gap between $q$ and $\sqrt q$ is the entire content.

**Not cheap, and for graphs not true.** There is no theorem that a $(q+1)$-regular graph is Ramanujan; most are not. The prism above is a counterexample and long thin graphs fail badly. Ramanujan is a special property that particular constructions have, and each construction comes with its own proof: arithmetic (Lubotzky–Phillips–Sarnak, via the Riemann hypothesis for a modular curve), probabilistic (Friedman: random regular graphs are nearly Ramanujan), or interlacing (Marcus–Spielman–Srivastava: bipartite Ramanujan graphs of every degree exist).

So the right question about Deligne's theorem is not "how does one prove the bound" but

> *what do varieties have, that graphs lack, which makes every one of them Ramanujan?*

The answer has three parts, and the rest of this note is those three parts. Varieties can be **multiplied** (the product $X \times X$ is again a variety, and the eigenvalues multiply). Varieties can be **sliced over a curve** (a one-parameter family of hyperplane sections, so the object becomes "a curve with matrix-valued coefficients"). And the interesting eigenvalues enter the count **with a minus sign**. A graph has none of these: there is no product of graphs under which walk-count eigenvalues multiply while staying in the same class, a graph is already one-dimensional so it cannot be sliced into something smaller, and its interesting eigenvalues are poles.

## 4. The engine: power up, dominate, take roots

Before the proof, the one elementary trick it is built on, in its purest graph form: *why the Ramanujan bound is $2\sqrt q$ at all.*

Take the infinite $(q+1)$-regular tree, pick a root, and let $c_{2k}$ be the number of closed walks of length $2k$ from the root (ordinary walks now, backtracking allowed). The spectral radius of the tree's adjacency operator is $\lim_k c_{2k}^{1/2k}$. Count: a closed walk on a tree is determined by the pattern of steps away from and back toward the root, which is a Dyck path (about $4^k$ of them, up to a polynomial factor), together with the choice of fresh neighbour at each of the $k$ outward steps ($q$ choices, or $q+1$ at the root). So

$$
c_{2k} = 4^k q^k \times (\text{bounded factor}) \times (\text{polynomial in } k),
$$

and $c_{2k}^{1/2k} \to 2\sqrt q$. Three moves were made:

1. **A nonnegative count dominates a power of an eigenvalue.** $c_{2k} = \langle \delta_{\text{root}}, A^{2k}\delta_{\text{root}}\rangle$, and its growth rate is the spectral radius.
2. **The count is known up to a fixed loss.** The bounded factor and the polynomial are losses, but they do not grow exponentially in $k$.
3. **Take the $2k$-th root and let $k\to\infty$.** Every fixed loss disappears and the exponential rate is exact.

Ramanujan means: the finite graph's nontrivial eigenvalues are no larger than the tree's spectral radius. The tree side of that comparison is exactly this computation. Deligne's proof makes the same three moves, twice, with different things in the roles of "count" and "eigenvalue". The nontrivial content is entirely in move 2: knowing the growth of the count with only a fixed loss.

## 5. The pointwise theorem, in graph language

Deligne's core theorem is not about a variety. It is about a curve carrying **matrix-valued coefficients**. Here is that setup for a graph; you have already computed with it.

A *twist* on a base graph $B$ assigns to each directed edge $e$ an invertible $d\times d$ matrix $\rho(e)$, with $\rho(\bar e) = \rho(e)^{-1}$ for the reversed edge. A closed walk $w$ then has a *holonomy* $\rho(w)$, the ordered product along the walk. The twisted zeta is

$$
L(B,\rho,u) = \prod_P \det\bigl(1 - u^{\ell(P)}\rho(P)\bigr)^{-1}
= \exp\Bigl(\sum_{w} \frac{\operatorname{Tr}\rho(w)}{|w|}\, u^{|w|}\Bigr),
$$

and it equals $1/\det(1 - uT_\rho)$ for the twisted edge matrix. The quantum Ihara zeta of the founding session is exactly this, with $B$ a bouquet of $D$ loops and $\rho = \operatorname{Ad}(U_i)$ on the $i$-th loop; a quantum expander is a Ramanujan twist of a bouquet.

Two kinds of eigenvalue now live on side B:

- **global**: the eigenvalues of $T_\rho$ (poles of $L$), the analogue of the $\mu$'s;
- **pointwise**: for each prime cycle $P$, the eigenvalues of the holonomy $\rho(P)$.

Say the twist is *pure with constant $c$* if every eigenvalue of every $\rho(P)$ has modulus exactly $c^{\ell(P)}$. A unitary twist is pure with $c=1$. Deligne's coefficient systems are pure with $c = q^{\beta/2}$ for an integer $\beta$ called the weight.

**Deligne's pointwise theorem** (his Theorem 3.2, in this language). Let $\rho$ be a twist on a curve such that

- (a) all traces $\operatorname{Tr}\rho(w)$ are real (in fact rational);
- (b) $\rho$ preserves an alternating pairing up to the scalar $c^{2\ell(w)}$, so eigenvalues of $\rho(P)$ come in pairs $\alpha, c^{2\ell(P)}/\alpha$;
- (c) the holonomies generate a group as large as (b) permits.

Then $\rho$ is pure with constant $c$.

**The argument, four steps.** Fix a prime cycle $P_0$ and an eigenvalue $\alpha$ of $\rho(P_0)$. The goal is $|\alpha| \le c^{\ell(P_0)}$; the pairing (b) then gives equality.

*Step 1, power up.* Replace $\rho$ by its $2k$-fold tensor power $\rho^{\otimes 2k}$, dimension $d^{2k}$. Holonomies become $\rho(w)^{\otimes 2k}$, traces become $(\operatorname{Tr}\rho(w))^{2k}$, and $\alpha^{2k}$ is an eigenvalue of $\rho^{\otimes 2k}(P_0)$.

*Step 2, dominate.* By (a), $(\operatorname{Tr}\rho(w))^{2k} \ge 0$. So every Euler factor of $L_{2k} := L(B,\rho^{\otimes 2k},u)$ is a power series with nonnegative coefficients and constant term $1$, and the coefficients of the full product dominate those of any single factor. The factor at $P_0$ has a pole at $|u| = |\alpha|^{-2k/\ell(P_0)}$. A dominated series cannot converge farther than the dominating one, so $L_{2k}$ has a singularity at or inside that radius.

*Step 3, the known pole.* Suppose one knew that the only poles of $L_{2k}$ are the *trivial* ones, at $|u| = 1/(q c^{2k})$: the pole of an untwisted zeta, rescaled by the constant. Then

$$
|\alpha|^{-2k/\ell(P_0)} \;\ge\; \frac{1}{q\,c^{2k}}
\qquad\Longleftrightarrow\qquad
|\alpha| \;\le\; c^{\ell(P_0)}\, q^{\ell(P_0)/2k}.
$$

*Step 4, take roots.* Let $k \to \infty$. The loss $q^{\ell(P_0)/2k}$ vanishes and $|\alpha| \le c^{\ell(P_0)}$.

Compare with §4: the count is the coefficient sequence of $L_{2k}$, the eigenvalue is $\alpha^{2k}$, the fixed loss is the single factor $q$ in the trivial pole, and it is paid once by the base curve no matter how large $k$ is.

**Where a graph breaks it.** Step 3 is false for graphs, and it has to be, because the theorem is false for graphs. Take $B$ a bouquet of two loops and $\rho(a) = \begin{pmatrix}2&1\\1&1\end{pmatrix}$, $\rho(b) = \begin{pmatrix}1&1\\1&2\end{pmatrix}$. Traces are integers (a), determinants are $1$ so the pairing holds with $c=1$ (b), and the two matrices generate a group dense in $SL_2$ in every sense that matters (c). Yet $\rho(a)$ has eigenvalue $(3+\sqrt5)/2 > 1$: not pure. What happens in the argument is that $L_{2k} = 1/\det(1-uT_{\rho^{\otimes 2k}})$ has a pole at $|u| = ((3+\sqrt5)/2)^{-2k}$, far inside $1/q$, coming from a *nontrivial* eigenvalue of the twisted edge matrix. For a graph, every eigenvalue of side B is a pole, so nothing forces the poles to sit at the trivial place. The next two sections are what makes Step 3 true for a curve: one hypothesis (big monodromy) and one structural fact (the sign).

## 6. Big monodromy: why the trivial poles are computable

Where do the trivial poles of $L_{2k}$ come from? From **invariant vectors**: a vector $v$ in the $d^{2k}$-dimensional coefficient space fixed by every holonomy $\rho(w)^{\otimes 2k}$. On such a vector the twist acts like no twist at all, and the twisted zeta acquires a copy of the untwisted zeta, with its pole at $1/q$, rescaled by whatever scalar the twist puts on $v$. If that scalar is known, the pole is at a known place.

The pairing (b) supplies invariants for free: contract the $2k$ tensor slots in pairs using the alternating form. Each such contraction is fixed by the holonomies up to the scalar $c^{2k\ell}$, so it contributes a trivial pole at exactly $1/(qc^{2k})$. Hypothesis (c), *big monodromy*, is the statement that **these are the only invariants**: if the holonomies fill out the whole group preserving the pairing, then invariant theory says every invariant of $\rho^{\otimes 2k}$ is a combination of pairwise contractions. Nothing else is fixed, so no other trivial pole appears.

What goes wrong without it is best seen at the opposite extreme. Suppose all holonomies commute. Then they have common eigenvectors, and the tensor powers have far more invariants than the contractions: a common eigenvector with eigenvalue $\chi(w)$ becomes invariant in $\rho^{\otimes N}$ as soon as $\chi^N = 1$, and the scalar it carries is $\chi$-dependent, i.e. unknown. The trivial poles then sit at places the argument does not control, and Step 3 gives nothing. In Deligne's setting this is a coefficient system with abelian monodromy, which can indeed have arbitrary pointwise weights; his hypothesis excludes it. In your setting it is the observation from the founding session that commuting Kraus unitaries never give an expander: the adjoint action of an abelian group has as many invariants as it has joint eigenprojectors. The same obstruction, on both sides of the dictionary.

How is big monodromy verified in the geometric case? Deligne needs it for the coefficients that arise from slicing a variety over a curve (§8). There, the holonomy around each bad slice is a *shear*, the identity plus a rank-one nilpotent along one specific vector, and the vectors for the different bad slices are all carried to one another by the holonomy group. A theorem of Kazhdan and Margulis says a group generated by a single conjugacy class of shears, acting without invariant subspaces, is automatically as large as the pairing allows. So big monodromy is not a miracle; it is the statement that the bad slices are all alike, which is true because they are generic.

## 7. The sign: why the interesting eigenvalues cannot make poles

Now the structural fact. For a graph, side B is one matrix $T_\rho$ and $L = 1/\det(1-uT_\rho)$: every eigenvalue is a pole. For a curve with coefficients, the trace formula has two blocks with opposite signs. Written for the twisted count,

$$
\sum_{w:\,|w|=m} \operatorname{Tr}\rho(w) \;=\; \operatorname{Tr}\bigl(F^m \,\big|\, \text{invariant block}\bigr) \;-\; \operatorname{Tr}\bigl(F^m \,\big|\, \text{interesting block}\bigr),
$$

so that

$$
L(\text{curve},\rho,u) = \frac{\det(1 - uF \mid \text{interesting block})}{\det(1 - uF \mid \text{invariant block})}.
$$

The invariant block is the one §6 computes: it is spanned by the invariant vectors, its Frobenius eigenvalues are the trivial ones, and it produces poles. The interesting block, everything else, produces **zeros**. The power series of a rational function converges up to its nearest *pole*; zeros do not obstruct convergence. So the radius of convergence of $L_{2k}$ is set by the invariant block alone, which big monodromy has made computable. That is Step 3.

This is the same minus sign as in §2. For a graph the walk count is $q^m + 1 + \sum\mu^m$; for a curve the point count is $q^m + 1 - \sum \alpha^m$. Positivity of counts is available on both sides. What differs is what positivity *constrains*: on the graph side it constrains the sum of everything, which is the Perron bound and no more; on the curve side the interesting eigenvalues are subtracted, so positivity of the count bounds them from above by the trivial ones, and the tensor-power trick then squeezes that bound to equality. The $2\times 2$ integer example of §5 is not a curve because there is no way to write its walk counts with the interesting part subtracted.

So the honest summary of the pointwise theorem is: **an Euler product with nonnegative coefficients, whose only poles are at a known place, forces every local eigenvalue to lie inside that place, and even tensor powers make the bound exact.** Positivity from (a), known poles from (b) together with (c) together with the sign, exactness from the roots.

## 8. From pointwise to global: slice, bound, multiply

The pointwise theorem is about the holonomies. RH for a variety $X$ of dimension $n$ is about the *global* eigenvalues of its middle block. Three moves connect them.

**Slice.** Choose a one-parameter family of hyperplane sections of $X$; the parameter runs over a curve, and all but finitely many slices are smooth of dimension $n-1$. Then the middle block of $X$ is, up to pieces already understood, the interesting block of the *base curve with coefficients*, the coefficients at a parameter value being the middle block of the slice there. In graph terms: a graph covering $X \to B$ writes the eigenvalues of $X$ as the eigenvalues of $B$ twisted by the permutation holonomy of the fibres, and the Artin–Ihara factorisation you used for the quantum Ihara zeta is this statement. Slicing does the same with the fibre replaced by a variety of one dimension less. The coefficients satisfy (a), (b), (c) of §5: the pairing is Poincaré duality on the slice; big monodromy is §6; and the traces are rational because the zeta function of a slice is a rational function with rational coefficients, from which the blocks already known by induction on dimension are peeled off (bookkeeping, omitted here). So the pointwise theorem applies and the coefficients are pure with $c = q^{(n-1)/2}$.

**Bound.** With pure coefficients the Euler product over the base curve converges absolutely for $|u| < 1/(qc)$: there are about $q^\ell/\ell$ prime cycles of length $\ell$ and each holonomy has norm $c^\ell$. So the interesting block has no eigenvalue larger than $qc = q^{(n+1)/2}$. RH wants $q^{n/2}$. The loss is a single factor $\sqrt q$, paid by the base being a curve, and independent of $n$.

**Multiply.** The product $X^k$ has dimension $nk$, and its middle block contains the $k$-fold tensor products of the middle block of $X$, so the products $\alpha_1\cdots\alpha_k$ are among its eigenvalues. Apply the bound to $X^k$: the loss is still one factor $\sqrt q$, because the base of a slicing is always a curve. Hence

$$
|\alpha|^k \le q^{(nk+1)/2}
\qquad\Longrightarrow\qquad
|\alpha| \le q^{n/2}\, q^{1/2k} \xrightarrow{\,k\to\infty\,} q^{n/2},
$$

and Poincaré duality gives the reverse inequality. This is §4 a second time: count, fixed loss, roots.

The pointwise theorem is what makes the last move legitimate. The slices of $X^k$ have dimension $nk-1$, far above anything the induction on dimension knows, so their purity cannot be assumed; §5 delivers it from rationality and big monodromy alone. That is why the core theorem is stated for coefficients on a curve rather than for varieties: it certifies coefficients in any dimension at the price of one curve. Even for a curve $C$, Deligne's argument passes through $C^k$ for all $k$; the surface $C\times C$ is where Weil's proof lived, and the products are not a convenience but the mechanism.

The remaining blocks $i \neq n$ come from the middle blocks of hyperplane sections of lower dimension, by induction, and from duality.

## 9. What the proof does not do

It never exhibits a Hermitian structure. Compare Weil's proof for curves: the intersection form on $C\times C$ is definite on the relevant part (the Hodge index theorem), and this makes $F/\sqrt q$ unitary for an explicit positive inner product on the middle block. That proof produces the Hilbert–Pólya operator. In graph terms it is the statement that on the nontrivial part $T$ is $\sqrt q$ times a unitary in some inner product, which for each $2\times 2$ block $\begin{pmatrix}\lambda & -q\\ 1 & 0\end{pmatrix}$ is true exactly when $|\lambda| < 2\sqrt q$. Grothendieck's plan was to prove a definite form in all dimensions (the standard conjectures) and deduce RH as Weil had. That plan is still open. Deligne bypassed it: no form, no operator, only positivity of coefficients and a limit. So RH over finite fields is a theorem, but the inner product that would make Frobenius normal is, in dimension above one, not known to exist.

Your Artin–Schreier computation sits on the Weil side of this divide: $EE^\dagger = qI$ was manifest from Parseval for the additive characters, an explicit inner product. Deligne's proof is what one has when no such structure is in sight.

Two further honesty notes. The Ramanujan property of the LPS graphs you built needs only the curve case (Eichler–Shimura transports Hecke eigenvalues to Frobenius eigenvalues of a modular curve), so Weil's theorem suffices there; Deligne's method is what extends it to higher weight, and to $\tau(p)$. And the technology hidden in the phrase "side B exists", the trace formula for a curve with coefficients, is the largest single piece of the proof by page count, though not by idea.

## 10. What this says for the project

- **Which ingredients $\zeta$ has.** The zeros are subtracted from the prime count, so $\zeta$ is on the curve side of the table in §2, not the graph side, and the positivity $\Lambda(n) \ge 0$ is the right kind. The sign and the positivity are present. What is absent is the product: there is no $X\times X$ with $\zeta$ as its slice, so the multiply step of §8 has nothing to act on. This is the standard diagnosis, stated in the terms of this note.
- **The number-field shadow of the pointwise theorem exists and is called Rankin–Selberg.** For a modular form, the Euler product of $L(f\times\bar f)$ has nonnegative coefficients and a known pole, and dominating one local factor gives $|a_p| \le p^{(k-1)/2}\cdot p^{1/2}$, the fixed loss of §8. Each symmetric-power $L$-function whose poles are known shaves the loss (Kim–Sarnak's $7/64$ is the current state). Knowing the poles of *all* the tensor-power $L$-functions is the analogue of big monodromy, and over number fields it is Langlands functoriality, unproved.
- **The abelian obstruction is inside Deligne's proof.** Commuting holonomies produce uncontrolled invariants (§6) exactly as commuting prime dilations produce a non-expanding channel. Any lift of the prime dilations that hopes to be Ramanujan must break the commutativity by a quotient, as LPS does with the arithmetic lattice and as Deligne does with the shears of a generic slicing.
- **Ramanujan without Hermiticity is possible.** Deligne's route and the interlacing route both reach the spectral bound without a Hilbert–Pólya operator. For the steering question of where Hermiticity enters, this is the cleanest evidence that it need not enter at all; what must enter is a positivity plus an operation under which eigenvalues multiply while the loss stays fixed.
