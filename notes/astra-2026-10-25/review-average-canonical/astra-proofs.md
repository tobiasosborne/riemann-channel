# REFUTE review of lanes A and C

Author: `codex:gpt-6-astra` (reviewer), 2026-10-25. This is a same-family review; the record gate also wants a second-family review. No record page is changed.

The audit distinguishes a polynomial average from an average of trace measures, raw from completed character polynomials, and the label Casoratian from its symmetric energy. All requested checks are complete; independent derivations, computations and original-script replays are recorded below.

## A1. Exact squarefree quadratic average — VALID

**PROVED; candidate `prop:sf-quadratic-average-exact`.** The claim is an exact finite-degree identity, including the nonsquares, for the uniform average over **monic squarefree** moduli. It is not the limiting probability that two random polynomials are coprime.

For monic $f=a^2h$, with $h$ squarefree, multiplicativity gives
\[
 (f/D)=1_{(a,D)=1}(h/D)
 =\epsilon^{d\deg h}1_{(a,D)=1}(D/h),\qquad \epsilon=(-1)^{(q-1)/2}.
\]
This also holds when a symbol vanishes. No coprimality of $a,h$ is needed. Taking the coefficient of $t^d$ in the squarefree Euler product gives
\[
 \epsilon^{d\deg h}[t^d]
 \prod_{P\nmid a}(1+\chi_h(P)t^{\deg P}).
\]
The factor is already 1 for $P\mid h$. Using $1+x=(1-x^2)/(1-x)$ gives exactly lane A's (1), including the product only over $P\mid a,P\nmid h$. The sign is correct: it is outside coefficient extraction because the degree of $D$ is fixed. It would instead be implemented by replacing $t$ by $\epsilon^{\deg h}t$ in the whole series.

For $h=1$, the character is the everywhere-one character, its $L$-series and squared-character $L$-series are $1/(1-qt)$ and $1/(1-qt^2)$. Thus (2) is precisely
\[
 [t^d]\frac{1-qt^2}{1-qt}\prod_{P\mid a}(1+t^{\deg P})^{-1}.
\]
In particular $a=h=1$ gives $H_d=q^d-q^{d-1}$ for $d\ge2$; there is no lost factor at conductor one. For (5), the allowed local states of $(D,a)$ are: $P\nmid a$, with $P$ absent or present in $D$; or $P^j\Vert a,j\ge1$, with $P\nmid D$. Their factor is
\[
 1+t^r+\frac{z^r}{1-z^r}
 =\frac{1+t^r}{1-z^r}\left(1-\frac{(tz)^r}{1+t^r}\right),\quad r=\deg P.
\]
Multiplication and the polynomial-ring zeta identities give both sides of (5). The unique square/squarefree decomposition of each monic $f$ then proves (3)–(4). The raw numerator for nonconstant even $h$ retains its $1-t$ factor; replacing it by the completed numerator would invalidate (1).

**Independent enumeration.** `checks/direct_average.py` compiles the accompanying C++ source and enumerates all $q^d$ monic moduli, selecting squarefree ones by Euclidean gcd. Every coefficient $S_n(D)=\sum_{\deg f=n}(f/D)$, $0\le n<d$, is obtained from direct character sums with the affine reuse described below. Polynomial symbols use a separately written Euclidean Jacobi algorithm; multiplicativity caches the value of a composite test polynomial, rather than reconstructing coefficients from an Euler product. For efficiency equivalent sums are reused under the exact affine bijection
\[
 D_{b,c}(x)=b^{-d}D(bx+c),\qquad S_n(D_{b,c})=\eta(b)^{dn}S_n(D).
\]
All moduli are covered, including affine orbits with stabilizers; images are deduplicated. There are 29 orbits covering 162 squarefree degree-five moduli over $\mathbb F_3$, and 16,865 orbits covering 705,894 squarefree degree-seven moduli over $\mathbb F_7$. No functional equation constructs any coefficient; the source's final functional-equation assertion is only an after-the-fact check of already computed individual coefficients.

The **unnormalized** coefficient totals, in ascending degree, are
\[
 (162,0,372,0,1458),
\qquad
 (705894,0,4324110,0,30268770,0,242121642).
\]
Consequently
\[
 \overline L_{3,2}=1+\frac{62}{27}u^2+9u^4,
\quad
 \overline L_{7,3}=1+\frac{102955}{16807}u^2
       +\frac{102955}{2401}u^4+343u^6.
\]
The full coefficients, rather than just those below the midpoint, agree with lane A. The independent local-product audit `checks/check_algebra.py` passes 448 cases of (1)–(2), including 128 nonzero negative-sign cases, and counts 1,086 coprime pairs for (5) at $(q,d,m)=(3,5,2)$, giving density $181/243$; the unchanged original routines are replayed from `checks/replay_average/` so their output paths cannot modify the input lane.

## A2. The half-polynomial lemma — VALID

**PROVED; candidate `lem:reciprocal-half-stability`.** The actual hypothesis concerns $P$, including **half the middle coefficient** at even degree. It does not assert global monotonicity of the reciprocal polynomial $B$.

Write $P=\sum_{j=0}^k p_jw^j$, $p_0=1\ge p_1\ge\cdots\ge p_k>0$, with the stipulated strict first drop if $k>0$. Directly, without citing Eneström–Kakeya,
\[
 (1-w)P(w)=p_0-\sum_{j=1}^k(p_{j-1}-p_j)w^j-p_kw^{k+1}.
\]
If $|w|<1$, the modulus of the sum on the right is strictly smaller than $p_0$. If $|w|=1$ and $P(w)=0$, equality in the triangle inequality and $p_0-p_1>0$ force $w=1$, where $P(1)>0$. Thus $P$ has no zeros in the closed disk.

Now $B=P+w^gP(1/w)$, precisely because the central coefficient was halved. The quotient $R=w^gP(1/w)/P(w)$ is holomorphic near the closed disk; $g-k>0$ gives $R(0)=0$, and reality of the coefficients gives $|R|=1$ on its boundary. The maximum-modulus principle gives $|R|<1$ inside, so $B=P(1+R)$ has no interior zero. Its nonzero constant coefficient and reciprocal symmetry exclude exterior zeros too. Constant $P$ gives $B=1+w^g$ directly. Every step survives scrutiny.

**SHARPENED, not an arithmetic H-half claim.** The strict first drop is sufficient but unnecessary for circle location: increase the constant coefficient of $P$ by $\varepsilon>0$, apply the argument, and pass to the limit in $B+\varepsilon(1+w^g)$. Thus the weak monotone version also has all roots on the circle, although $P$ itself may then have boundary zeros. This does not address whether the hyperelliptic coefficients satisfy either hypothesis in general; that is lane A2's separate task.

The exact degree-4–8 search in `checks/check_algebra.py` tests 842 integer reciprocal coefficient arrays with $b_0=1,\ldots,5$, nonnegative decreasing coefficients of the correctly halved $P$, and also the weak first-drop boundary. It reduces to $w+w^{-1}\in[-2,2]$ and uses rational Sturm counts, rather than numerical radii. No counterexample is possible under the actual hypothesis. If “first half” is weakened to omit the central coefficient altogether, $1+3w^2+w^4$ is a counterexample: its initial $(1,0)$ decreases, but its correct half is $(1,0,3/2)$, which fails H-half. Its reduced polynomial is $y^2+1$, so its roots are off the circle.

A further search, `checks/check_self_inversive.py`, tests 460 self-inversive polynomials of degrees 4–8 with phases $\tau\in\{1,-1,i,-i\}$ and small integer first-half coefficients. It forms $B=P+\tau w^gP(1/w)$ (zero middle coefficient in the even cases) and uses an exact Cayley transform and rational Sturm counts. All transformed roots are real, hence all roots of $B$ lie on the circle; a degree drop records roots at $w=1$. The quotient proof itself extends to any unit-modulus $\tau$, so the search is a control on conventions, not a substitute for the lemma.

## A3. Low genus and the first coefficient — VALID

**PROVED; candidate `thm:hyperelliptic-average-low-genus`.** This candidate includes the odd-degree genera 1–3 and the completed even-degree genera 1–2. The supporting odd-coefficient vanishing, formula (7), and rejection of global monotonicity are also valid.

Scaling $x\mapsto bx$ permutes the monic squarefree degree-$d$ ensemble and multiplies $S_n$ by $\eta(b)^{dn}$. For odd $d$, a nonsquare $b$ kills every odd averaged coefficient. The quadratic functional equation, an algebraic fact independent of a root-location theorem, then makes $B(w)$, $w=qu^2$, reciprocal with $b_0=b_g=1$. The Jacobi convention differs from $y^2=D$ by the constant twist when $q\equiv3\pmod4,d$ is odd; this is $u\mapsto-u$ and leaves the average unchanged.

The degree-two sum splits into $q$ linear squares, $q(q-1)/2$ products of distinct linear factors, and $q(q-1)/2$ irreducible quadratics. Both kinds of squarefree quadratic $h$ have raw $L(t,\chi_h)=1-t$. Their denominators in (1) are respectively $(1-t^2)^2$ and $1-t^4$; the coefficient at $t^{2g+1}$ is respectively $(q-1)g-1$ and $\delta_g\in\{q,-1\}$. Together with the square coprimality count, this rederives
\[
 b_1=\frac q{q+1}+q^{-2g}K_g,
 \quad K_g=\frac1{q+1}+\frac{(q-1)g-1+\delta_g}{2}.
\]
For $g\ge2,q\ge3$, $K_g>0$ and
\[
 (q+1)K_g\le 1+\frac{(q^2-1)(g+1)}2<q^{2g}.
\]
The last inequality's base-case slack is $(q^2-1)(q^2-1/2)>0$. If $F_g=q^{2g}-1-(q^2-1)(g+1)/2$, its induction increment is
\[
 F_{g+1}-q^2F_g=\frac{q^2-1}{2}\bigl((q^2-1)g+q^2\bigr)>0.
\]
This supplies the previously abbreviated induction. Hence $0<b_1<1$ for every $g\ge2$; for $g=1$, (7) gives 1. It also proves that the full reciprocal coefficient sequence cannot be monotone when $g\ge2$.

For $g=2$, $1+b_1w+w^2$ has its roots on the circle. For $g=3$, multiplication verifies exactly
\[
 B=(1+w)(1+(b_1-1)w+w^2),
\]
and $-1<b_1-1<0$ lies strictly inside the interval $[-2,2]$ needed for a real reciprocal quadratic. There is no missing sign or extra inequality.

For even degree, the raw polynomial is divisible by $1-u$; after division the genus-one coefficients are $(1,1-q^{-2},q)$. The discriminant is negative. In genus two the coefficients are $(1,A,B,qA,q^2)$, $A=1-q^{-4}$, $B=q+q^{-1}-q^{-2}-q^{-3}$. Direct extraction in (1) gives the stated raw quadratic split $4-3q,-q$, and hence these coefficients. The reduced polynomial is $y^2+(A/\sqrt q)y+B/q-2$. Since $1<B/q<2$, its value at zero is negative; at either endpoint it is at least $B/q+2-2A/\sqrt q>3-2/\sqrt3>0$. Its two roots therefore lie in $(-2,2)$. This verifies the even-degree part of the candidate as well.

## A4. Which cubic average fails — VALID

**REFUTED dichotomy; candidate `obs:geometric-level-average-dichotomy`.** The counterexample averages a specified **isotypic factor**, not the numerator of the whole cubic cover, and not every cubic character of every degree-three modulus.

Precisely, over $\mathbb F_7$ take the 294 monic **squarefree** polynomials $D$ of degree 3. For each choose the canonical product residue character
\[
 \chi_D(f)=\prod_{P\mid D}(f/P)_3
\]
with one common embedding $\mu_3(\mathbb F_7)\to\mathbb C$. At a reducible $D$ this uses the same exponent at every local factor; independently choosing either local cubic character would be a different ensemble. The conjugate product character gives the conjugate factor. Averaging both of these factors per $D$, rather than one, has the same answer because this ensemble average is real. There are 343 monic degree-three polynomials in all; the 49 nonsquarefree ones are excluded.

`checks/check_algebra.py` enumerates all 294 moduli by gcd, then sums cubic characters through raw degree 2 via resultants, with $3\mapsto\omega$ on constant-field norms. It obtains
\[
 \langle L\rangle=1-u^2,\qquad
 \left\langle L/(1-u)\right\rangle=1+u,\qquad
 \left\langle L^*(\chi_D)L^*(\bar\chi_D)\right\rangle=1+2u+7u^2.
\]
Thus $-1$ is an off-circle root of the completed isotypic average. The whole-curve average does satisfy the circle statement in this example.

The all-$q\equiv1\pmod3$, odd-$q$ proof is sound. Cubic reciprocity has no sign since $6\mid q-1$. A linear test modulus has $L(t,\chi)=L(t,\chi^2)=1$, so its squarefree twist-generating series is 1. The average linear coefficient is zero. At degree 3 every product character is primitive and even; its raw degree-two polynomial vanishes at $u=1$, forcing the averaged $1-u^2$. Degrees 1 and 2 have constant isotypic averages, so degree 3 is the first nonconstant example in this family.

**Additional body assertions adjudicated.** The degree-four exact isotypic averages $1+qu^3$ at $q=7,13$, and the whole-curve finite certificates at degrees 1–4, reproduce in the original-script replay. For the whole numerator, the degree-two and degree-three all-$q$ formulas follow from the vanishing linear character average and the genus-one functional equation; these arguments are valid. The independent `checks/check_cubic_extra.py` verifies the degree-four whole-curve formula by full direct cubic sums. The unrestricted whole-curve assertion remains OPEN; the isotypic counterexample does not refute it.

## A5. Irreducible level and exact order — VALID

**PROVED; candidate `prop:ff-irreducible-level-average`.** Let $Q=q^d$, $f$ irreducible. For monic $A$ of degree $0<n<d$, $A\not\equiv1\pmod f$; summing all nontrivial characters therefore gives $-1$ for each of the $q^n$ such $A$. At degree zero it gives $Q-2$. This proves the polynomial side of (10) directly; multiplying by $1-qu$ gives its rational side. There are no hidden poles left.

The even characters are the characters of $\mathbb F_Q^\times/\mathbb F_q^\times$, whose order is $M=(Q-1)/(q-1)$. Among nontrivial even characters their raw sum is $(M-1)-\sum_{n=1}^{d-1}q^nu^n$; the odd-character sum is the constant $Q-1-M$. Dividing only the even sum by $1-u$ proves (11). The normalized leading-coefficient test correctly proves failure for raw $d\ge2$ and completed $d\ge3$. The completed degree-two average is constant, not a degree-preserving RH example.

For exact order $N\mid Q-1$, the characters are $\gamma\mapsto e^{2\pi ia/N}$, $(a,N)=1$; their sum at $\gamma^k$ is $c_N(k)$. This proves (12). Constants are generated by $\gamma^M$, so all these characters are even exactly when $N\mid M$. Selecting exact order is not a subgroup average.

`checks/check_characters_independent.py` constructs $\mathbb F_{q^2}$ as coefficient pairs with $t^2=-r$, evaluates **each character** in a cyclotomic polynomial quotient, groups by its order, and only afterwards compares to the Ramanujan-sum formula. The full degree-two check is:

| $q,f$ | order $N$ | raw average | completed average |
|---|---|---|---|
| $3,t^2+1$ | 2, 4 | $1-u$ | 1 |
| $3,t^2+1$ | 8 | 1 | 1 |
| $5,t^2+2$ | 2, 3, 6 | $1-u$ | 1 |
| $5,t^2+2$ | 4 | $1+2u$ | $1+2u$ |
| $5,t^2+2$ | 8, 24 | 1 | 1 |
| $5,t^2+2$ | 12 | $1-u$ | $1-u$ |

Their raw sums over all nontrivial characters are $7-3u$ and $23-5u$, and their completed sums are 7 and 23. In particular the order-four $q=5$ failure is genuine, while the order-two family is a singleton satisfying the **existing theorem of Weil** after completion. The other level counterexamples reproduce in the replay.

**PROVED negative finding; candidate `obs:common-vacuum-average-det`.** The steps $I_4,-I_4$ commute and preserve a common compatible complex structure. Direct expansion gives their average determinant $1+6z^2+z^4$, with root moduli $\sqrt2\pm1$. A common vacuum therefore does not imply a circle-rooted average determinant. This also validates lane A's refusal to infer an averaging theorem from lane M.

**OPEN/HEURISTIC body item.** The number-field proposal (13) is correctly left open, and (14) is a different, linear explicit-formula functional. For a finite family, the logarithmic derivative of a product is the sum of logarithmic derivatives; the logarithmic derivative of a sum is not. Primitive nontrivial quadratic completions have root number $+1$; conductor one is excluded, so no principal pole was dropped. No claimed number-field RH theorem needs adjudication here.

## C1. Retained graph moments and Schur length — VALID

**PROVED; candidate `prop:graph-trace-schur-support`.** These are the traces of the **second-order Ihara step**, not ordinary adjacency-power moments. With $n=|V|,m=|E|$, put
\[
 C_k=q^{-k/2}\operatorname{Tr}M^k,
 \quad M=\begin{pmatrix}A&-qI\\I&0\end{pmatrix}.
\]
The logarithmic derivative of Ihara–Bass gives
\[
 C_k=q^{-k/2}\{\operatorname{Tr}B^k-(m-n)(1+(-1)^k)\},\quad k\ge1.
\]
At $k=0$, the same formula is the dimension identity $2m-2(m-n)=2n$. Equivalently, each adjacency mode contributes $2T_k(\lambda/(2\sqrt q))$; it does **not** contribute $(\lambda/\sqrt q)^k$. For example $C_2=q^{-1}\operatorname{Tr}A^2-2n$, already distinguishing them.

Retain the nontrivial adjacency modes by subtracting **both** roots of the uniform quadratic: $q^{k/2}+q^{-k/2}$. In the bipartite case also subtract $(-1)^k(q^{k/2}+q^{-k/2})$. At $k=0$ each removal subtracts 2. Set $c_{-k}=\overline{c_k}$ and $T_N=(c_{j-k})_{0\le j,k\le N}$.

Sufficiency of Ramanujan follows by expressing these moments as a sum of unit-circle point masses, weighted by algebraic multiplicities. For necessity, positive $2\times2$ minors give $|c_k|\le c_0$. If the largest normalized root modulus $R$ exceeds one, its grouped phases have a trigonometric sum with positive Cesàro mean square; thus the power sums are unbounded along a subsequence. The quadratic reciprocal pairing excludes all remaining strictly interior roots. This is exactly the combination of `thm:weil-positivity-finite` and `thm:weil-duality-pairing` in `report/sections/08b_weil_positivity.tex:51` and `:73`. Traces do not detect Jordan blocks.

The label conventions also check. The symplectic matrix $C=\bigl(\begin{smallmatrix}0&-I\\I&0\end{smallmatrix}\bigr)$ satisfies
\[
 CMC^{-1}=\begin{pmatrix}0&-I\\qI&A\end{pmatrix}=M_0,
\quad
 Q=\tfrac12\Omega(M-qM^{-1})=
 \begin{pmatrix}I&-A/2\\-A/2&qI\end{pmatrix}.
\]
It transports $Q$ to the tutorial/page convention $\bigl(\begin{smallmatrix}qI&A/2\\A/2&I\end{smallmatrix}\bigr)$. On one mode, $T_1=\bigl(\begin{smallmatrix}2&\lambda/\sqrt q\\\lambda/\sqrt q&2\end{smallmatrix}\bigr)=2D^TQ_\lambda D$, $D=\operatorname{diag}(1,-1/\sqrt q)$. Reduction modulo $w^2-(\lambda/\sqrt q)w+1$ identifies the trace functional for longer polynomials. This is a cyclic trace quotient, not an isomorphism onto every repeated label block. The lane appropriately restricts its $\Omega_+=\operatorname{Tr}(x\sigma(y)/(V-F))$ formula to the reduced algebra with $V-F$ invertible; endpoints require the elementary block formula.

For $r>0$ distinct circle points with positive weights, Vandermonde evaluation has rank $\min(N+1,r)$. Orthogonal polynomial norms are positive before degree $r$ and zero at degree $r$, so $|\alpha_j|<1$ for $j<r-1$ and $|\alpha_{r-1}|=1$. The terminal polynomial is the monic product over the **distinct** points. Its parameter is $-\overline{R(0)}$, not a parameter inferred from the unreduced degree. The recurrence and determinant/pivot formulas in the lane have the correct conjugations and indices. A terminal boundary value in an arbitrary indefinite sequence must still pass the stated subsequent-moment consistency test.

**Independent exact route.** `checks/check_graph_independent.py` counts closed Hashimoto walks using edge successors and integer dynamic programming; it then forms the corrected moments and applies the **formal Carathéodory/Schur-function algorithm** over $\mathbb Q(\sqrt2)$. This is separate from the lane's adjacency/Chebyshev recurrence and monic-polynomial Levinson routine.

For $K_4$, retained moments begin
\[
 (c_0,c_1,c_2,c_3,c_4)=
 (6,-3/\sqrt2,-9/2,15/(2\sqrt2),3/4),
\quad (\alpha_0,\alpha_1)=(-\sqrt2/4,-1).
\]
Thus the retained degree is six, but the support and Schur length are two.

For $C_{16}\times K_2$, the full sequence through first failure is
\[
 0,-\frac7{20},0,\frac{163}{1053},0,\frac{1525}{6764},0,
 \frac{21349}{123721},0,\frac{396933}{731870},0,
 \frac{11257789}{12223564},0,\frac{43707967}{3998190}.
\]
All earlier moduli are strictly below one. Index 13 is the first failure: $T_{13}$, of size 14, is positive definite; its extension $T_{14}$, of size 15, has a negative prediction pivot. This indexing follows because $\alpha_n$ connects norms $h_n,h_{n+1}$.

**PROVED; candidate `obs:schur-failure-not-mode-count`.** The independent check also obtains the first failure at index 8 for $C_{17}\times K_2$, with value $-413023893\sqrt2/312857602$. Rational isolating intervals for the two adjacency characteristic polynomials certify exactly four out-of-band adjacency modes, with multiplicity, in each graph. Hence the first failure index is not a function of that count. The original five-graph table, complete-graph family, Möbius–Kantor example and prism survey reproduce in the replay; their finite trace/support interpretation is correct.

## C2. Casoratian versus Szegő transfer — VALID as a reformulation

**PROVED identity; candidate `prop:casoratian-szego-conformal`.** The sharp statement is the two-dimensional identity
\[
 T^TJT=(\det T)J,\qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\]
valid for **every** $2\times2$ matrix, including singular ones. Applying it to the recurrence step gives Abel's multiplier $q$; applying it to
\[
 A_\alpha(z)=\begin{pmatrix}z&-\bar\alpha\\-\alpha z&1\end{pmatrix}
\]
gives the alternating multiplier $z(1-|\alpha|^2)$. On $|z|=1$, direct multiplication separately gives
\[
 A_\alpha(z)^*\operatorname{diag}(1,-1)A_\alpha(z)
 =(1-|\alpha|^2)\operatorname{diag}(1,-1).
\]
The missing $z$ in the original brief would have conflated an alternating bilinear identity with a Hermitian identity. For $|\alpha|<1$, phase/determinant normalization and a Cayley change of basis give an $SL(2,\mathbb R)$ realization; at a terminal coefficient the transfer is singular. The independent graph script checks the alternating identity symbolically with independent variables for $\alpha,\bar\alpha$.

This is a useful exact reformulation of Abel's determinant identity, **not** a conjugacy between the graph's time evolution and the moment recursion. The latter advances polynomial degree, depends on spectral weights, and is not the graph mode recurrence. Tutorial Section 6c is consistent with this reading: with labels $(x_k,-x_{k+1})$, its displayed $\Omega$ is **minus** the scalar Casoratian $x_ky_{k+1}-x_{k+1}y_k$. The phrase “$\Omega$ is the Casoratian” must allow this explicitly fixed orientation. The symmetric $Q$ is a different form derived from $\Omega$ and the step.

**Endpoint body correction verified.** At $|\lambda|=2\sqrt q$, the $2\times2$ companion block has a nontrivial Jordan part: $Q\succeq0$, but no conjugacy to a rotation or invariant positive definite metric. Strictly in-band modes do have those properties. The tutorial's subsequent sentence in Section 6d saying graph RH means “the first case” is itself too strict: Ramanujan allows the band-edge case as well. This is a recommended record correction, not a defect in lane C's sharpened theorem.

## C3. Completed character log-traces — VALID

**PROVED; candidate `prop:ff-schur-logtrace`.** For a primitive nontrivial character, let $\varepsilon=1$ if even, (0) otherwise, and $\Lambda=L/(1-u)^\varepsilon=\prod_{i=1}^d(1-F_i u)$. Then
\[
 c_0=d,\qquad c_k=-q^{-k/2}
 \left(\sum_{\deg P\mid k}\deg P\,\chi(P)^{k/\deg P}+\varepsilon\right).
\]
Indeed $uL'/L$ has the positive Euler sum, whereas $u\Lambda'/\Lambda=-\sum_k\operatorname{Tr}(F^k)u^k$; dividing by $1-u$ adds $u/(1-u)$ to this logarithmic derivative. Both the leading minus sign and the even correction check. Degree-zero completions have zero measure and no Schur sequence.

The algebraic functional equation gives $p=Wp^*$, $p(z)=\Lambda(z/\sqrt q)$, $|W|=1$. A scalar phase makes $p$ conjugate-reciprocal; it cannot generally make it real reciprocal. This reflection symmetry plus bounded power sums proves the same Toeplitz criterion as in C1. The finite-rank Schur criterion must include consistent termination at the number of distinct Frobenius values, not at the degree with multiplicity. These are existing finite-dimensional moment facts; **Weil's theorem** supplies RH for the character as a separate known theorem, not as numerical input.

The reversal convention is right. The measure uses $F_i/\sqrt q$, so its monic annihilator is the reduced part of $z^d\Lambda(1/(\sqrt qz))$. In the squarefree case its terminal parameter is $-\bar W$. The reciprocal-root measure has conjugate moments, and its monic polynomial is $p/W$, with terminal parameter $-W$.

**Independent computation.** `checks/check_characters_independent.py` computes each quartic character value as an integral Sylvester resultant reduced modulo 5, then solves the exact Toeplitz orthogonality equations for the monic polynomials. It uses neither a saved coefficient row nor the lane's polynomial-power or Levinson code. For $f=t^3+t+1$, with $2\mapsto i$,
\[
 \Lambda=1+(-2+i)u+(3-4i)u^2,
\quad c_1=(2-i)/\sqrt5,
\quad c_2=(-3+4i)/5,
\]
\[
 \alpha_0=(2+i)/(2\sqrt5),\quad |\alpha_0|^2=1/4,
\quad \alpha_1=-(3+4i)/5.
\]
The conjugation of $c_1$ in $\alpha_0=\bar c_1/c_0$ is essential.

The repeated-root counterexample also reproduces exactly. At $f=t^4+1$, the specified two local generators both have norm 3, so the product character is the conjugate of the constant-field quartic norm symbol. Direct sums give raw $L=1+(1-4i)u-5u^2+(3+4i)u^3$, hence
\[
 \Lambda=1+(2-4i)u+(-3-4i)u^2=(1+(1-2i)u)^2.
\]
Its discriminant is zero; its one Schur parameter is $(-1-2i)/\sqrt5$, of modulus one. This verifies the support-versus-degree correction without relying on approximate root merging.

## C4. Prime and squarefree aggregates — VALID

**PROVED; candidate `prop:ff-prime-aggregate-insufficient`.** Individual prime values through degree $k+1$ do determine $\alpha_k$: they determine every prime-power log-trace through that degree, and Schur/Levinson is a triangular rational transformation of those moments. Individual squarefree values also include the primes; the Möbius-weighted squarefree generating series is $1/L$. None of these assertions is the false claim about *unweighted degree aggregates*.

The missing term is already visible in
\[
 A_2=\sum_{\deg P=2}\chi(P)+\tfrac12\left(
       (\sum_{\deg P=1}\chi(P))^2+\sum_{\deg P=1}\chi(P)^2\right).
\]
The independent script computes all coefficients through degree four by direct quadratic resultant sums for the four listed degree-five moduli over $\mathbb F_3$:

| modulus | full raw/completed $L$ | prime sums in degrees 1,2 | squarefree sum in degree 2 | $\alpha_1$ |
|---|---|---|---:|---:|
| $t^5+t^4+2t^3+t^2+2t$ | $1-u+2u^2-3u^3+9u^4$ | $(-1,1)$ | 1 | $-13/47$ |
| $t^5+2t^4+1$ | $1-u+3u^2-3u^3+9u^4$ | $(-1,1)$ | 0 | $-21/47$ |
| $t^5+2t$ | $1-2u^2+9u^4$ | $(0,-2)$ | $-2$ | $1/3$ |
| $t^5+2t^4+t^3+t^2+2t$ | $1+9u^4$ | $(0,-1)$ | $-2$ | 0 |

All four moduli are squarefree, all four characters are primitive and odd, and all four root numbers are $+1$. The first pair has $\alpha_0=\sqrt3/12$ but missing prime-square sums 1 and 3; the second has $\alpha_0=0$ and missing sums 0 and 2. Thus the counterexamples hold with conductor degree, completed degree, parity and root-number phase fixed. There is no completion or multiplicity escape.

## C5. Zeta support, product and prime-side probes — VALID at the stated statuses

**PROVED-conditional (H-RH); candidate `prop:zeta-schur-purepoint-product`.** H-RH means all nontrivial zeta zeros lie on the critical line. For nonzero $g\in C_c^\infty(\mathbb R)$, the conditional measure is
\[
 \nu_{p,g}=\sum_{\rho=1/2+i\gamma}m_\rho|\widehat g(\gamma)|^2
                      \delta_{e^{i\gamma\log p}},
\]
with multiplicity included once and coincident phases combined. Rapid decay and the zero-counting bound give finite mass. Its support is infinite: a nonzero compact-support Fourier transform has only $O(T)$ zeros in $|z|\le T$, by exponential type and Jensen; there are $\gg T\log T$ distinct simple critical zeros. This last standard input is also stated in the locally supplied source `refs/src/2206.03682/screwz_15.tex:962` (with Conrey/Levinson attribution), so it is not an unverified claim of pairwise nonresonance. A finite union of phase residue classes modulo $2\pi/\log p$ contains only $O(T)$ distinct real ordinates up to height $T$, a contradiction after deleting the transform's zeros. Consequently every finite $T_N$ is strictly positive under H-RH, and no Schur parameter terminates the sequence.

Normalize the mass to one. The Szegő formula quoted by the lane is the correct one, including the value zero when $\int\log w=-\infty$:
\[
 \prod_{j\ge0}(1-|\alpha_j|^2)=
 \exp\int\log w(\theta)\,\frac{d\theta}{2\pi}.
\]
The measure is pure point, regardless of whether its support is dense, so its absolutely continuous density $w$ vanishes a.e. and the product is zero.

There is also a direct prediction-error verification of the zero conclusion. The finite product is the minimum of $\int|p|^2d\nu$ over polynomials of degree at most $n$ with $p(0)=1$, by reversal of the monic minimization and the norm recursion. For any finite set of atoms carrying mass $>1-\delta$, choose tiny arcs covering them and a smooth boundary log-modulus that is $\log\varepsilon$ near those atoms, has mean zero, and is at most $\log2$ everywhere. This is possible by making the arcs sufficiently short. Its outer analytic function has value 1 at zero, modulus at most 2, and modulus $\varepsilon$ at the chosen atoms. Smoothness gives uniform polynomial approximation while preserving the constant coefficient. Thus the limiting prediction error is at most $\varepsilon^2+4\delta$, and tends to zero. This verifies the pure-point step independently of any numerical product extrapolation.

**PROVED exact structure / NUMERICAL probes; candidate `num:zeta-prime-schur-probes`.** Simultaneous translation cancels in $g*k^*$, so $W(U_tg,U_tk)=W(g,k)$ before RH. The uncut translate matrix is exactly Toeplitz. Its span through $N$ uses support length $L+N\log p$; a separately clipped common window is a different construction. The original conditional statements, numerical positivity, and small sampled roundoff residuals must remain distinguished.

The source audit of **both** `check_zeta.py` and `check_zeta_gaussian.py` finds no number-field zero file, `zetazero`/`lfun` call, or imported window routine that reads zeros. The compact script constructs $g$, autocorrelates it, sieves primes and powers, and evaluates pole/archimedean integrals. The Gaussian script uses its analytic autocorrelation, a sieve, and ordinary high-precision quadrature. Their only persistent data output is the compact table; neither reads a saved spectral table. Quadrature nodes and numerical polynomial roots elsewhere in the review are not zeta/L-zero inputs. The expected constants in the independent check appear only in final comparison assertions, not as inputs to a form. This satisfies game rule 3.

**Independent recomputation of $c_0,c_1$.** `checks/check_zeta_independent.py` uses direct Gauss–Legendre integration of $g(v)g(v-x)$, splitting at every cutoff transition. It uses no FFT, spline, or lane import. For the same $L=.4,\tau=.1,p=2$, it uses the equivalent archimedean subtraction
\[
 \mathcal A(H)=(\log\pi+\gamma)H(0)
  +\int_0^U\frac{e^{-x/2}(H(x)+H(-x))-2e^{-2x}H(0)}{1-e^{-2x}}\,dx
  +H(0)\log(1-e^{-2U}).
\]
This follows by moving $2H(0)(e^{-x}-e^{-2x})/(1-e^{-2x})$ between the integral and constant: its integral over $(0,\infty)$ is $2H(0)\log2$. It therefore checks the lane's $\log(4\pi)$ normalization and analytic tail subtraction, not just its numerical integrator.

For $c_0$, $e^L<2$, so the prime sum is empty. For $c_1$, $e^{L+\log2}<3$, so **only $n=2$** occurs; its term is $\log2\,h(0)/\sqrt2$. At quadrature order 108, the separate terms are

| entry | pole | prime | archimedean | result |
|---|---:|---:|---:|---:|
| $c_0$ | .0933240662056472 | 0 | .0589473320146792 | .0343767341909680 |
| $c_1$ | .0989851200928732 | .0824691857004111 | .0447466572854086 | −.0282307228929465 |

Orders 48, 72, 108 and 160 differ by at most $2.6\times10^{-15}$ in these moments. Thus the reproduced values are
\[
 c_0\simeq .03437673419097,\qquad c_1\simeq-.0282307228929465,
 \qquad\alpha_0=c_1/c_0\simeq-.8212159635677.
\]
These are numerical convergence checks, not certified interval enclosures. They agree with the requested saved values. The original compact and Gaussian scripts also reproduce their saved outputs, including the Gaussian $p=2$ product through $N=16$. The analytic Gaussian tail bounds do not bound quadrature error; the lane explicitly says so, and this qualification must accompany those digits.

**Other body assertions adjudicated.** Fixed-index coefficients depend only on finitely many moments, so enlarging $N$ does not change a previously computed coefficient. For the specified expanding Gaussian cutoff, convergence in weighted smooth test-function norms gives moment convergence; rational continuity gives coefficient convergence at nonsingular blocks, which H-RH guarantees. A window length alone does not choose a probe or a limit. Under H-RH, $g_T(u)=\phi(u/T)e^{-i\gamma_0u}$, with $\int\phi\ne0$, concentrates normalized spectral weight at one chosen ordinate; rapid Fourier decay controls the remaining discrete spectrum. Hence $|\alpha_0|\to1$, disproving a gap uniform over all probes/windows. This is a theoretical argument, not a computation fed a zero. The different compact and Gaussian probe values in the replays independently refute probe independence. No nonzero Euler-factor product remains: the conditional product is identically zero for these pure-point measures.

## C6. Meaning for the ladder and proposed record corrections

**AGREE with the headline.** Schur coordinates, together with $c_0$, specify a positive moment functional, rather than supplying an integral lattice or a positivity mechanism. The finite cyclic quotient has one coordinate per distinct supported spectral point. Multiplicity enters the mass; Jordan data do not enter traces. For an elementary independent check, `checks/check_certificates.py` compares $I_2$ with $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$: both have $c_k=2$ for every $k$, and the same terminal $\alpha_0=1$, but one is semisimple and the other is not. No moment-coordinate change can recover the missing distinction. Nor does a two-component recursion at each degree imply a two-dimensional spectral space. Probe dependence and conditional infinite support on the zeta rung reinforce, rather than remove, this limitation.

**AGREE-WITH-CHANGE — `graph-ihara.md` §8 item 2 / §9.** Use this precise annotation:

> On the label space, the alternating form $\Omega$ is the recurrence Casoratian up to the stated ordering/sign convention; with the tutorial's labels $(x_k,-x_{k+1})$, $\Omega=-W_k$. The symmetric recurrence energy is $Q=\tfrac12\Omega(M-qM^{-1})$. In-band endpoints give a degenerate energy and parabolic blocks; strict interior modes give rotations and a positive definite energy.

The correction should also cover the inaccurate strict-rotation sentence in tutorial §6d. The label form does not descend through the kernel of the label-to-edge map. Its matrix must be changed by the displayed symplectic conjugacy if the step convention changes.

**AGREE-WITH-CHANGE — `data-ladder.md`.** Suggested replacement for the finite/infinite rank comparison:

> A trace-moment quotient has rank equal to the number of distinct supported normalized Frobenius points, with multiplicities recorded as weights; it need not have the full dimension of geometric $H^1$. For a fixed nonzero compact smooth probe, under H-RH the zeta translate measure has infinitely many distinct phases even after aliasing, so every finite Toeplitz block is positive definite and the Schur sequence does not terminate. This diagnostic supplies neither an integral lattice nor a proof of positivity.

In particular replace “one atom per zero” by “one atom per distinct surviving phase, with collided weights added”; replace the unconditional zeta rank assertion by its stated H-RH version; and replace a universal curve rank $2g$ by “at most $2g$, equal only for distinct supported Frobenius values.” Retain the distinction between the reduced cyclic algebra and the full geometric module.

**AGREE — lane A's `graph-super.md` §9 annotation**, with “full character average” understood to use nontrivial torsion order $N\ge2$: determinant cancellation is a special mechanism; varying characters or covers alone does not imply RH for the averaged polynomial. **AGREE** that the failed geometric/level dichotomy belongs among the negative findings in `data-ladder.md` §2, with the word **isotypic** retained. **AGREE** with keeping the raw/completed distinction explicit in `ff-dirichlet.md`, the full group including the trivial member explicit in `zn-flux.md`, and a warning against the common-vacuum inference near `family-vacuum.md`. These are proposed annotations only; no record page was edited.

## Additional candidate rows and complete body coverage

**PROVED by exact finite certificates; `obs:hyperelliptic-average-certificates` — MINOR (wording only).** The arithmetic formula and its implementation have been audited above. `checks/check_certificates.py` independently checks every exact polynomial printed in the extended table: 26 odd-degree cells $(3,1{:}12),(5,1{:}8),(7,1{:}6)$, and 14 completed even-degree cells $(3,1{:}6),(5,1{:}4),(7,1{:}4)$. In addition to exact half-coefficient inequalities for the odd cells, it uses a different root certificate. For the reduced real polynomial $R$, form Newton sums $s_k$, the Hermite matrix $H=(s_{i+j})$, and the weighted matrix $K=(R_0^2s_{i+j}-s_{i+j+2})$. All leading principal minors are positive. Positivity of $H$ certifies distinct real roots; after Vandermonde congruence, positivity of $K$ places every root in $(-R_0,R_0)$. For odd averages it first works in $w=qu^2$, removes $1+w$ when necessary, and takes $R_0=2$. For completed even averages it takes $R_0^2=4q$. This is independent of the lane's Sturm isolation and floating-point root refinement. Exact determinants are saved in `checks/output_certificates.txt`.

One wording precision: H-half in the lane's extended section applies to the odd-degree $B(w)$ cells. The even-degree completed polynomials have odd $u$-coefficients and are certified by the separate band test, not by that same $B(w)$ hypothesis. The code and candidate range are correct; the introductory prose should say “H-half for the odd cells, and Sturm certificates for both parities.”

**OPEN; `conj:hyperelliptic-average-all-genus` — UNVERIFIED as a universal assertion.** The reviewed lane explicitly does not claim a proof. Its conditional implication from H-half is valid by A1–A2 of this review, and its finite certificates reproduce. Neither proves the universal arithmetic inequality or universal averaged RH. This review deliberately leaves that new work to the current round's `hhalf/` lane, as instructed; UNVERIFIED here is not a refutation of the conjecture or criticism of its honest OPEN status.

**NUMERICAL; `num:ff-all-small-conductors-schur` — VALID at its numerical status.** The replay independently constructs the characters again and reproduces the full 264,595-line saved output, including all 263,694 character rows. The generation/primitive-conductor tests in `check_ff_all.py` are correct: local characters are retained exactly when nontrivial on the final reduction kernel, and the Teichmüller/principal-unit direct product enumerates the whole local unit group (checked by exact cardinalities).

`checks/audit_outputs.py` parses every row and checks counts independently from
\[
 \sum_{m\ge0}\#\{\text{primitive characters of monic conductor degree }m\}u^m
   =\frac{(1-qu)^2}{1-q^2u}.
\]
Thus the counts by degree 1–4 are $3,36,324,2916$ for $q=3$, and $15,400,10000,250000$ for $q=5$. It also classifies support rank using the quadratic/cubic **discriminants**, without using Schur stopping to infer rank, and then compares the results with the printed sequences. This reproduces 30 degree-two rank-one completions and 80 degree-three rank-two completions at conductor degree four over $\mathbb F_5$, and no other rank drops. Across the rounded printed coefficients, the largest repeated-discriminant residual is $1.79\times10^{-7}$, whereas the smallest nonzero discriminant magnitude is $1.3397\ldots$. This is a well-separated numerical cross-check, not an exact algebraic census certificate. The displayed repeated-root example was verified exactly in C3.

The following body-only adjudications make explicit the claims not individually named in the original closing tables. The `body:` aliases below are assigned **by this review for identification**, not proposed registered claim IDs. The associated statements and proofs were checked in the sections indicated; none is silently omitted.

| review alias | original body assertion | verdict and evidence |
|---|---|---|
| `body:A-odd-vanishing` | Odd coefficients vanish for the odd-degree quadratic ensemble | VALID; affine change of variable, A3, and all-coefficient enumeration A1 |
| `body:A-first-coefficient` | Formula $7$, with $b_1=1$ at $g=1$ and $0<b_1<1$ at $g\ge2$ | VALID; degree-two factor split and explicit induction slack, A3; exact checks in `output_algebra.txt` |
| `body:A-global-monotonicity` | The original global Eneström–Kakeya premise fails for every $g\ge2$ | VALID refutation; equal endpoints plus the strict $b_1<1$ |
| `body:A-cubic-degree-four` | $\langle L\rangle=1+qu^3$ at $q=7,13,d=4$ | VALID; direct sums in `checks/check_cubic_extra.py`, no functional-equation reconstruction |
| `body:A-whole-cubic-certificates` | Whole-curve averages for $q=7,13,d\le4$, and the all-$q$ degree-two/three formulas | VALID; independent complete character sums and exact band certificates in `output_cubic_extra.txt`; all-$q$ derivation in A4 |
| `body:C-ihara-correction` | Hashimoto-to-step trace correction, including $k=0$ | VALID; logarithmic derivative/dimension derivation and independent closed-walk sums, C1 |
| `body:C-endpoint-rotation` | Semidefinite energy does not imply a rotation at a band endpoint | VALID; explicit companion Jordan block, C2 |
| `body:C-full-polynomial-popuc` | The full or multiplicity-bearing graph polynomial is not generally the terminal POPUC | VALID refutation; exact $K_4$ degree-six/support-two check, C1 |
| `body:C-polynomial-versus-moment-schur` | Polynomial Schur–Cohn coefficients are not moment Verblunsky coefficients | VALID; a reciprocal polynomial already has unit-modulus leading/constant ratio, whereas the $K_4$ moment algorithm starts at $-\sqrt2/4$; C1 |
| `body:C-completion-and-phase` | Raw even factors and a scalar phase cannot justify the original degree/real-reciprocity claim | VALID refutation; completion, complex quartic and exact repeated-root examples, C3 |
| `body:C-fixed-probe-convergence` | The specified expanding cutoff has convergent fixed-index coefficients at nonsingular blocks | VALID with the stated conditions; test-function convergence and rational continuity, C5; prime-only replay |
| `body:C-uniform-probe-gap` | No positive disk gap or unique limit is uniform over arbitrary probes/windows | VALID refutation under the explicit H-RH hypothesis; concentration argument and differing prime-only probe outputs, C5 |

The two remaining distinction statements need no new conjecture: finite support records weights but loses Jordan structure (C1, C6); and averaging the number-field Weil functional is not taking the logarithmic derivative of the averaged completed function (A5). The OPEN/HEURISTIC number-field suggestions and the general whole-cover conjecture remain proposals, not promoted theorems.

## Correction ledger

1. No counterexample was found to the **stated** half-polynomial lemma. Dropping the middle-coefficient requirement creates a different false statement; omitting strictness alone does not.
2. The low-genus bracket argument is correct; its omitted induction algebra is supplied in A3. The even-degree genus-two band inequalities also check.
3. The cubic refutation concerns a specific uniformly weighted product-character ensemble over squarefree moduli and its completed isotypic factors. It does not say that every cubic character modulo every cubic polynomial is being averaged, or that whole-curve averages fail.
4. For finite extensions, explicitly separate the odd-cell H-half test from the band test used for completed even cells.
5. The graph moment is a trace of $M/\sqrt q$, equivalently a corrected Hashimoto trace, rather than a trace of $A/\sqrt q$. Both roots of each trivial adjacency mode must be removed.
6. The Casoratian/Szegő statement is a correct determinant identity and reformulation; it is not a new positivity theorem or an identification of evolution variables. Preserve the raw $z$ multiplier and the tutorial's minus sign.
7. Retain endpoint, repeated-support and phase-aliasing qualifications in record annotations. The unconditional sentence in tutorial §6d that excludes endpoints should be corrected.
8. The zeta computations obey the prime-input rule. Their finite numerical positivity and quadrature convergence are not rigorous semidefinite or interval certificates. Infinite support and zero Szegő product remain explicitly conditional on H-RH.

## Recomputations and saved-output comparison

`checks/replay.py` ran all six lane-A commands and all five lane-C commands from byte-identical source copies under this review's directory. All eleven exited zero. `checks/audit_outputs.py` read and compared all thirteen original saved output files, including the entire character census: every line agrees with the replay after dropping only elapsed-time lines. Source SHA-256 hashes, line counts, census/discriminant checks and the zeta input audit are saved in `checks/output_audit_outputs.txt`; run statuses are in `checks/output_replay.txt`. The input lanes were not edited.

Independent work is in `direct_average.py`/`.cpp`, `check_algebra.py`, `check_self_inversive.py`, `check_cubic_extra.py`, `check_graph_independent.py`, `check_characters_independent.py`, `check_zeta_independent.py`, and `check_certificates.py`, with correspondingly named `output_*.txt`. They use direct character sums, a separate Jacobi implementation, cyclotomic character enumeration, a formal Schur-function algorithm, exact Toeplitz solves, Hermite matrices, discriminants, and direct double quadrature as described above. No claim of independent recomputation is based merely on rerunning the original code.

## Verdict lines

VERDICT prop:sf-quadratic-average-exact: VALID — reciprocity, conductor one, local products and both full-degree averages reproduce.
VERDICT lem:reciprocal-half-stability: VALID — the halved central coefficient and maximum-modulus argument give the claimed circle theorem.
VERDICT thm:hyperelliptic-average-low-genus: VALID — the bracket bound, induction, cubic factorization and completed even cases check.
VERDICT obs:hyperelliptic-average-certificates: MINOR — say H-half for odd cells and band certificates for both parities; all stated ranges reproduce.
VERDICT conj:hyperelliptic-average-all-genus: UNVERIFIED — this remains an explicitly OPEN universal assertion assigned to the separate hhalf lane.
VERDICT obs:geometric-level-average-dichotomy: VALID — the specified completed cubic isotypic average is 1+u, while the whole-curve object differs.
VERDICT prop:ff-irreducible-level-average: VALID — raw, completed and exact-order formulas agree with explicit character enumeration.
VERDICT obs:common-vacuum-average-det: VALID — the common-vacuum determinant average has root moduli sqrt(2)−1 and sqrt(2)+1.
VERDICT prop:graph-trace-schur-support: VALID — corrected Ihara-step traces give the stated positivity criterion and distinct-support termination.
VERDICT prop:casoratian-szego-conformal: VALID — the claim is the exact two-dimensional determinant reformulation with raw multiplier z(1−|alpha|²).
VERDICT obs:schur-failure-not-mode-count: VALID — exact prism failures at indices 13 and 8 occur with the same four out-of-band modes.
VERDICT prop:ff-schur-logtrace: VALID — completion, log-trace signs, conjugation, reversal and repeated-support conventions reproduce.
VERDICT prop:ff-prime-aggregate-insufficient: VALID — both exact quadratic counterexample pairs retain equal root number and the stated aggregates.
VERDICT num:ff-all-small-conductors-schur: VALID — the full numerical census reproduces and an independent discriminant audit agrees on support ranks.
VERDICT prop:zeta-schur-purepoint-product: VALID — under H-RH the probe measure has infinite support and zero Szegő product.
VERDICT num:zeta-prime-schur-probes: VALID — the computations use only allowed inputs and independent direct quadrature reproduces c0 and c1.
VERDICT body:A-odd-vanishing: VALID — affine covariance kills odd averaged coefficients.
VERDICT body:A-first-coefficient: VALID — the exact degree-two split proves formula (7) and its strict bounds.
VERDICT body:A-global-monotonicity: VALID — equal reciprocal endpoints and b1<1 refute global monotonicity for g≥2.
VERDICT body:A-cubic-degree-four: VALID — full direct sums reproduce 1+qu³ at q=7 and 13.
VERDICT body:A-whole-cubic-certificates: VALID — the separate whole-curve averages and all claimed finite band certificates reproduce.
VERDICT body:C-ihara-correction: VALID — closed Hashimoto walks reproduce the correction including degree zero.
VERDICT body:C-endpoint-rotation: VALID — a band-edge companion block is parabolic with degenerate energy.
VERDICT body:C-full-polynomial-popuc: VALID — K4 has retained degree six but only two supported points.
VERDICT body:C-polynomial-versus-moment-schur: VALID — the two algorithms have different inputs and boundary behavior.
VERDICT body:C-completion-and-phase: VALID — exact quartic examples verify the raw/completed and conjugate-reciprocal corrections.
VERDICT body:C-fixed-probe-convergence: VALID — the specified cutoff converges and coefficients are continuous at nonsingular blocks.
VERDICT body:C-uniform-probe-gap: VALID — conditional concentration and differing prime-only probes refute uniformity over arbitrary probes.

## Numerical checks for the blind lane

Run from the repository root; every script saves its printed result inside this review's `checks/` directory.

1. `python3 notes/astra-2026-10-25/review-average-canonical/checks/direct_average.py` — full coefficient totals are `[162,0,372,0,1458]` at `(q,d)=(3,5)` and `[705894,0,4324110,0,30268770,0,242121642]` at `(7,7)`. In particular the latter average is $1+(102955/16807)u^2+(102955/2401)u^4+343u^6$.
2. `python3 notes/astra-2026-10-25/review-average-canonical/checks/check_algebra.py` — cubic `(7,3)` gives raw `[1,0,-1]`, completed `[1,1]`, whole-curve `[1,2,7]`; equation (5) at `(q,d,m)=(3,5,2)` gives 1,086 coprime pairs and density `181/243`; all 842 correctly halved reciprocal search cases pass exact root tests.
3. `python3 notes/astra-2026-10-25/review-average-canonical/checks/check_graph_independent.py` — K4 gives `[-sqrt(2)/4,-1]`; prism 16 first fails at index 13 with `43707967/3998190`; prism 17 first fails at index 8 with `-413023893*sqrt(2)/312857602`.
4. `python3 notes/astra-2026-10-25/review-average-canonical/checks/check_characters_independent.py` — X1 gives `[1,-2+i,3-4i]` and `|alpha0|²=1/4`; the aggregate-counterexample pairs give `alpha1=(-13/47,-21/47)` and `(1/3,0)`; level raw sums at `(3,2),(5,2)` are `7−3u,23−5u`.
5. `python3 notes/astra-2026-10-25/review-average-canonical/checks/check_zeta_independent.py` — at `p=2,L=.4,tau=.1`, obtain `c0≈.03437673419097`, `c1≈−.0282307228929465`, `alpha0≈−.8212159635677`, with only prime 2 contributing to the second entry and none to the first.
6. `python3 notes/astra-2026-10-25/review-average-canonical/checks/audit_outputs.py` — all thirteen saved/replayed outputs agree apart from timing; all 263,694 character rows parse; independent discriminants give exactly 30 and 80 rank drops in the two degree-four-conductor categories. `check_certificates.py` additionally verifies all 26 odd and 14 even exact finite certificates by Hermite matrices.

## What this changes in the notebook

For the sixteen original candidate rows: **14 VALID, 1 MINOR, 1 UNVERIFIED**. All twelve additional body-only adjudications are VALID. No INVALID claim was found in the reviewed lanes' corrected statements. The one MINOR changes wording, not the finite certified parameter ranges; the UNVERIFIED row was already explicitly OPEN.

| candidate rows | retained status / action |
|---|---|
| `prop:sf-quadratic-average-exact`, `lem:reciprocal-half-stability`, `thm:hyperelliptic-average-low-genus` | PROVED statements survive; record the exact coefficient, middle-term and completion conventions. |
| `obs:hyperelliptic-average-certificates` | PROVED by finite exact computation; fix the sentence to distinguish odd H-half from the band tests for both parities. |
| `conj:hyperelliptic-average-all-genus` | Keep OPEN pending the separate current-round lane; this review does not extend the arithmetic theorem. |
| `obs:geometric-level-average-dichotomy`, `obs:common-vacuum-average-det` | Retain the negative findings with the isotypic/whole-curve and common-vacuum distinctions. |
| `prop:ff-irreducible-level-average` | Retain raw, completed and exact-order formulas as stated. |
| `prop:graph-trace-schur-support`, `obs:schur-failure-not-mode-count` | Retain the corrected moments, trivial-mode removals, distinct-support rank and exact prism counterexample. |
| `prop:casoratian-szego-conformal` | Retain as an elementary identity/reformulation, with label orientation and endpoint qualifications. |
| `prop:ff-schur-logtrace`, `prop:ff-prime-aggregate-insufficient` | Retain completion, complex reversal and the exact aggregate counterexamples. |
| `num:ff-all-small-conductors-schur` | Retain NUMERICAL status; the census replay and independent rank audit do not turn every row into an exact discriminant certificate. |
| `prop:zeta-schur-purepoint-product` | Retain PROVED-conditional (H-RH); the product is zero, not a nonzero local factor. |
| `num:zeta-prime-schur-probes` | Retain the exact translate identity, NUMERICAL tables and conditional interpretation, with the stated precision limits. |

Apply the precise annotation wording in C6 when the record is next edited: distinguish the alternating Casoratian from the symmetric energy; include parabolic endpoints; count distinct supported points and combine aliased phases; retain H-RH on the zeta rank/product statement. Keep the failed geometric/level dichotomy among the negative findings, explicitly about the isotypic average. Schur coordinates remain diagnostics of a supplied moment functional, not the missing integral structure or a reason for positivity.

Nothing was registered or edited outside `notes/astra-2026-10-25/review-average-canonical/`. This is a **same-family** review; the record's second-family gate is still required. The next review step is a second-family check of these surviving claims and stated wording repairs, with universal H-half work kept in its assigned lane.
