# Q2: transposing the quasi-RH mechanism

Author: `codex:gpt-6-astra`, 2026-10-23. Research record; no claims registered.
All computations and changes are confined to this lane. No RH is an input to a computation.
The supplied quasi-RH manuscripts are treated as sources to transpose, not independently certified here.

**Verdict.** The sixth-power amplifier gives the conditional exponent 11/12, not Weil's 1/2. Hasse–Davenport simplifies the function-field Gauss coefficients but does not, by itself, prove the required short-row mean square; that estimate remains OPEN here. On graphs the proposed Möbius/Littlewood criterion is false, and the proposed diagonal interpretation fails by exact cancellation. The corrected flux-distribution theorem has a parity exception; a surface intersection pairing supplies no sixth-power amplifier.

## 1. Function fields

### Q2a — PROVED-conditional on H-MS: the sixth-power amplifier gives 11/12

Fix a prime power q ≡ 1 (mod 6), R = F_q[t], and an embedding of its sixth roots of unity in C. Let ν be a fixed finite-order Dirichlet character modulo a monic f, extended by zero at nonunits. For a monic prime P set

\[
(u/P)_6=u^{(q^{\deg P}-1)/6}\bmod P,
\]

with value zero when P divides u, and extend multiplicatively in the denominator. The empty denominator has value one. For monic coprime a,b, power reciprocity is

\[
(a/b)_6=(-1)^{((q-1)/6)\deg a\deg b}(b/a)_6.
\tag{1}
\]

This is Rosen, *Number Theory in Function Fields*, power reciprocity (bibliographic citation; also follows by swapping the two arguments of the resultant). The sign is essential at q=7. Define A_u(D) as in the question, including all monic n of degree D. For D>0 the row u=0 is zero. We use **all** polynomials of degree ≤h as rows; their number is q^{h+1}, so the frequently used q^h normalization differs by a fixed factor q. Constants may depend on q and ν.

For every monic prime p of degree k,

\[
A_{p^6}(D)=A_1(D)-\sum_{\deg n=D,\ p\mid n}\mu(n)\nu(n),
\qquad |A_{p^6}(D)-A_1(D)|\le q^{D-k}
\tag{2}
\]

when k≤D (the error is zero if k>D). Indeed the sextic symbol is exactly 1 off p and 0 on p; there are q^{D-k} multiples. No smoothing or estimate for primes is needed for this identity.

**H-MS.** For every fixed 0<ϑ≤1/10 and every ε>0, at h=⌊(1+ϑ)D⌋,

\[
S(D,h):=\sum_{\deg u\le h}|A_u(D)|^2
\ll_{q,\nu,\vartheta,\epsilon}q^{(1+\epsilon)D+h}.
\tag{3}
\]

Take k=⌊h/6⌋≥1. The exact prime-polynomial formula
\(\pi_q(k)=k^{-1}\sum_{d\mid k}\mu_{\mathbb Z}(d)q^{k/d}\)
gives π_q(k) ≍_q q^k/k as k grows; bounded k and D are absorbed in constants. Distinct monic p give distinct rows p^6. Applying |x+y|²≤2|x|²+2|y|² to (2) and averaging gives the exact analogue of source (2.5):

\[
|A_1(D)|^2\le {2S(D,h)\over\pi_q(k)}+2q^{2D-2k}
\ll Ckq^{(1+\epsilon)D+h-k}+q^{2D-2k}.
\tag{4}
\]

Consequently

\[
|A_1(D)|\ll \sqrt{k}\,q^{(11/12+5\vartheta/12+\epsilon/2)D+O_q(1)}
 +q^{(5/6-\vartheta/6)D+O_q(1)}.
\tag{5}
\]

Choosing ϑ and then ε sufficiently small proves \(|A_1(D)|\ll_{q,\nu,\delta}q^{(11/12+\delta)D}\) for every δ>0. This is a conditional theorem, not a use of Weil.

**PROVED: Littlewood relation with its correct boundary convention.** Formal Euler products give
\(\sum_{D\ge0}A_1(D)z^D=1/L(z,\nu)\).
An O(q^{θD}) bound implies that this series is analytic in |z|<q^{-θ}; multiplying by L and using the identity near zero shows L has no zero there. Conversely, nonvanishing in that open disk gives O_ε(q^{(θ+ε)D}) by Cauchy's estimate on smaller circles. At the exact exponent a multiple boundary zero can introduce a polynomial factor in D. Thus (3) for all ϑ,ε excludes zeros in **the disk** |z|<q^{-11/12}. Equivalently reciprocal roots α satisfy |α|≤q^{11/12}. A bound on the roots themselves has the opposite inequality: |z|≥q^{-11/12}.

**COMPARISON STEP — Weil's theorem, not an input.** For primitive nonprincipal ν, let Λ=L for odd ν and Λ=L/(1-z) for even ν. Every root of Λ has modulus q^{-1/2}. The uncompleted even L has also the trivial root z=1. Imprimitive presentations add omitted Euler factors with roots on |z|=1. The principal L is rational and needs its own pole factors. The brief's statement that every L is of degree deg f−2 when even silently referred to Λ. Under the functional equation, applying the quasi-bound to ν and its conjugate confines nontrivial roots to the annulus q^{-11/12}≤|z|≤q^{-1/12}; it does not put them on the Weil circle.

### Q2b — PROVED for long rows; PROVED Gauss identities; NUMERICAL for short rows; H-MS OPEN in this lane

**1. An unconditional complete-row theorem (no Weil).** For D≥1 and h≥2D−1,

\[
S(D,h)=q^{h+1-D}\sum_{\substack{n\text{ monic squarefree}\deg n=D}}
 |\nu(n)|^2\phi(n)\le q^{h+1+D}.
\tag{6}
\]

Here φ(n)=#(R/n)^×. Expand the square. For distinct squarefree n,m, χ_n\overline{χ_m} is a nonprincipal character modulo lcm(n,m): at a prime in the symmetric difference it has exponent ±1. The degree of that modulus is at most 2D. A ball deg u≤h contains every residue class equally often, so the cross term is zero. For n=m the character is the unit indicator modulo n, giving q^{h+1}φ(n)/q^D. This proves (6), including its precise threshold and constant. It handles arbitrary fixed ν, not just the characters in the checks.

Ordinary function-field large sieves have the scale q^{h+1}+q^{2D}, rather than the desired q^{h+1}+q^D; see [Hsu (1996)](https://doi.org/10.1006/jnth.1996.0077), *A Large Sieve Inequality for Rational Function Fields*, JNT 58, 267–287. Formula (6) is a self-contained proof of the range we actually use. Putting h≈2D in the amplifier only gives a q^{4D/3+o(D)} upper bound, weaker than the trivial q^D. **The proved long-row mean square is not H-MS.**

**2. Finite Poisson, with no omitted analytic step.** For a monic modulus m of degree M, put
\(e_m(x)=\psi_0([t^{-1}]x/m)\), with ψ₀ a nontrivial additive character of F_q. The pairing (x,v)↦e_m(xv) on R/(m) is nondegenerate: the leading nonzero coefficient of x can be paired with a suitable power of t and constant. Write
\(\widehat F(v)=\sum_{x\bmod m}F(x)e_m(vx)\).
If h<M−1 and V_h is the image of the degree ball, additive orthogonality gives

\[
\sum_{u\in V_h}F(u)
 ={q^{h+1}\over q^M}\sum_{v\in V_h^\perp}\widehat F(v),
\qquad |V_h^\perp|=q^{M-h-1}.
\tag{7}
\]

For primitive χ, \(\widehat\chi(v)=\bar\chi(v)G(\chi)\), including its zero extension at nonunits. Both claims follow by the substitution x↦v^{-1}x for units, and character orthogonality for nonunits. Coprimality masks are expanded by inclusion–exclusion; the common factors of n and m cannot be silently omitted. Thus expanding the family square has dual size at most q^{2D-h-1}, exactly the degree version of Poisson's D²/H scale. Formula (7) is an identity, not an estimate for the dual column sums.

**3. Hasse–Davenport really does evaluate these Gauss sums.** Let κ be the chosen order-six character of F_q^×, η=κ³, and

\[
\tau_j=q^{-1/2}\sum_{c\in\mathbb F_q^\times}\kappa(c)^j\psi_0(c),
\quad
\gamma_j(n)=q^{-D/2}\sum_{x\bmod n}(x/n)_6^j e_n(x).
\]

For monic squarefree n of degree D and j∈{1,2,3,4,5}, set R_n=Res(n,n′). Then

\[
\boxed{\gamma_j(n)=\mu(n)(-\tau_j)^D\kappa(R_n)^j.}
\tag{8}
\]

Proof: write n=∏P with residue degree d_P and root a_P. Partial fractions give
\([t^{-1}]x/n=\sum_P\operatorname{Tr}_{q^{d_P}/q}(x(a_P)/n'(a_P))\).
The residue character is κ^j composed with the norm. For a trace additive character the Hasse–Davenport lifting identity gives the normalized local sum (−1)^{d_P−1}τ_j^{d_P}; scaling by n′(a_P)^{-1} multiplies it by κ^j(Norm n′(a_P)). Multiply these local formulas. Their signs are (−1)^{D−#P}=μ(n)(−1)^D, and their norm product is R_n. This proves (8). The only imported input is the classical finite-field lifting identity, not RH. The same formula is recorded, unnormalized, in [Patterson, *Selberg sums — a new perspective*, §2, pp. 4–5](https://arxiv.org/pdf/1411.7600).

For completeness Pellet's formula here follows without a character-sum bound. A Vandermonde square root Δ of disc(n) changes under Frobenius by the sign of its permutation of the D roots, namely (−1)^{D−#P}. Thus η(disc n)=Δ^{q−1}=(−1)^Dμ(n). Since R_n=(−1)^{D(D−1)/2}disc n, (8) gives

\[
\boxed{\mu(n)\gamma_{-1}(n)=c_D\gamma_2(n),\quad
c_D=(-1)^D\eta((-1)^{D(D-1)/2})(\tau_{-1}/\tau_2)^D,\quad |c_D|=1.}
\tag{9}
\]

In particular the Möbius absorption survives, with a factor **depending only on the degree**. Moreover \(\gamma_2(n)^3=\mu(n)(-\tau_2^3)^D\). The number-field proof's step “the cubic Jacobi sum is a unit times the prime generator” does not make literal sense with a polynomial generator and a complex Jacobi sum. Its correct replacement is (8)–(9). A cubic Gauss sum is determined by D, μ(n), and the cubic character of the discriminant; it is not determined by D alone. At fixed D its phase lies in a fixed finite set times τ₂^D, but this does **not** evaluate a sum over discriminants.

**4. What has not collapsed.** After (7)–(9), the hard sums still contain multiplicative characters of Res(n,n′), a nonlinear function of all coefficients of n. These are Selberg-type sums; knowing each summand explicitly does not prove square-root cancellation in their twisted family. A quadratic large sieve alone does not remove this dependence. To avoid an uncertain attribution, name the needed squarefree quadratic inequality **H-LS**:

\[
\sum_{\deg a\le r}^{\rm sf}\left|\sum_{\deg b=d}^{\rm sf}c_b(b/a)_2\right|^2
\ll_{q,\epsilon}q^{\epsilon(r+d)}(q^r+q^d)\sum_b|c_b|^2.
\tag{10}
\]

Even granting H-LS, one must establish a function-field theta transformation that changes the moving sextic row twists to quadratic ones, its uniformity in the row and auxiliary factors, and the cube-completion/inversion/transfer estimates. The needed model is source Propositions 5.2, 5.4 and 6.2, not just a bound for individual cubic Gauss sums. Relevant literature is Hoffstein, *Theta functions on the n-fold metaplectic cover of SL(2) — the function field case*, Invent. Math. 107 (1992), 61–86, and [Patterson, *The Fourier coefficients of metaplectic theta series on GL(2) over rational function fields*](https://arxiv.org/abs/1411.7594). These are references for the framework, not claims that their statements immediately imply (3). **No short-row H-MS proof or theta-uniformity proof is claimed here.**

**5. NUMERICAL: exact entire families, not sampled rows.** `checks/qrh_ff_family.py` uses the quadratic characters of f=t³+t+1 at q=7 and f=t³+t+5 at q=13. Arithmetic for all family values is exact in Z[ζ₆], represented by integer pairs a+bζ₆, with squared norm a²+ab+b². All nonzero leading coefficients are included using |A_{cu}|=|A_u|, proved by χ_n(c)=κ(c)^D. The polynomial μ is computed by Pellet and independently checked against factorization on deterministic samples. The script checks all linear-prime amplifiers at every D≤5 and exact cyclotomic versions of (8)–(9), 30 cases at q=7 and 37 at q=13, through degree three.

The natural normalized ratio is R=S/q^{D+h+1}, since the row count is q^{h+1}. The requested S/q^{D+h} is qR and is also printed. Define β=(log_q S−h−1)/D; a square-root mean square predicts β→1, not a finite-D equality.

| q | D | h | method | exact S | R | β |
|---|---:|---:|---|---:|---|---:|
| 7 | 1 | 1 | complete | 294 | 6/7 | 0.920782221 |
| 7 | 2 | 3 | complete | 86436 | 36/49 | 0.920782221 |
| 7 | 3 | 4 | direct | 4238010 | 86490/117649 | 0.947295132 |
| 7 | 4 | 5 | direct | 211302504 | 4312296/5764801 | 0.962703808 |
| 7 | 5 | 4 | direct | 208944348 | 208944348/282475249 | 0.969009567 |
| 7 | 5 | 9 | complete | 3543059871288 | 4302216/5764801 | 0.969922517 |
| 13 | 1 | 1 | complete | 2028 | 12/13 | 0.968793650 |
| 13 | 2 | 3 | complete | 4112784 | 144/169 | 0.968793650 |
| 13 | 3 | 4 | direct | 701860380 | 4153020/4826809 | 0.980460978 |
| 13 | 4 | 7 | complete | 19950963010992 | 53733744/62748517 | 0.984883351 |
| 13 | 5 | 9 | complete | 43836864950451456 | 698611968/815730721 | 0.987914862 |

“Complete” means exact evaluation of **all** q^{h+1} rows by (6), using
\([z^D]\prod_{P\nmid f}(1+(q^{\deg P}-1)z^{\deg P})\)
for the weighted diagonal. It is not literal enumeration of these sometimes enormous row sets. Direct calculations cover every h from zero through [2,3,4,5,4] for D=1,…,5 at q=7, and [2,3,4,3,2] at q=13; complete calculations cover h=2D−1 and 2D at both q through D=5. **In particular the critical h≈D family at (q,D)=(13,5) has not been enumerated.** This is a limitation of this lane's numerical evidence, not a claimed verification. The complete-range values cannot validate an asymptotic short-range estimate.

**COMPARISON STEP ONLY.** The exact character coefficients give L₇=1+3z+7z² and L₁₃=1−5z+13z². Their inverse coefficients through D=5 agree with the directly computed A₁(D). Only after all these calculations does the script find roots at 80 decimal digits. Their moduli are respectively 0.377964473009227… and 0.277350098112615…; negative discriminants and leading coefficients 7,13 also certify the moduli exactly. The numerical zeros are not inputs to a family sum or an exponent bound.

### Q2c — READING: what exponent was obtained, and what Weil adds

The rigorously transposed amplifier converts **H-MS**, if proved in the required short range, to 11/12. This lane has proved the elementary Fourier/Gauss steps and the long-row mean square, but has not proved H-MS. Thus it has not obtained an unconditional new quasi-Weil theorem by the proposed mechanism. Weil itself supplies the stronger conclusion as a separately labelled theorem.

More generally, if the same mean-square estimate is supplied at h=αD+O(1), the elementary amplifier gives

\[
\theta(\alpha)=\max\{\tfrac12+\tfrac5{12}\alpha,\ 1-\tfrac16\alpha\}.
\tag{11}
\]

At α=1 this is 11/12. Even allowing arbitrary positive α with the same error bound, its minimum is 6/7 at α=6/7. Therefore **these two estimates alone do not deliver 1/2**, even if the mean square is extended to every row length. A sufficient additional hypothesis to obtain 7/8 would be the same mean square at h=3D/4+O(1); (11) then gives 7/8. This is one possible stronger input, not an assertion about the exact refinement in the supplied 7/8 manuscript. Transposing that refinement would require its probe, reflection and uniform comparison estimates separately; a sixth-power amplifier plus (3) does not already give it.

Weil's proof supplies a bound over every constant-field extension with the square-root exponent. In the correspondence formulation the additional input is the intersection inequality on C×C (Castelnuovo/Hodge index), or equivalently positivity associated with a polarisation of the Jacobian and the adjunction of Frobenius and Verschiebung. The Bombieri–Stepanov method uses large spaces of functions and dimension counts from Riemann–Roch to build a nonzero function with many prescribed high-order zeros, then compares its zeros and poles; applying it over extensions and using rationality isolates the square-root spectral bound. This uses geometric H⁰ data and Frobenius even though it does not need an explicit integral H¹ construction. See [Bombieri, *Counting points on curves over finite fields*, Bourbaki 430](https://numdam.org/item/SB_1972-1973__15__234_0/); Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent* (1948).

In the ladder's words the mean square belongs on the **family/orthogonality rung**; its positive quadratic form is a sum of absolute squares. The amplifier transfers part of that bound to one row. Neither operation constructs a finite-rank global H¹, an integral Frobenius, or a positive polarisation-type trace. This supports the limited reading “the transposed estimates have not supplied the missing geometric datum.” It does **not** prove that geometry is logically necessary for every possible proof of RH. In particular, the existence of a lattice that realizes a spectral bound and the method proving that bound are separate claims. The notebook's universal language should be qualified accordingly.

## 2. Graphs

### Q3a — REFUTED as stated; corrected Littlewood relation below

The obstruction already occurs on K_4: the proposed Möbius series is the polynomial det(1−zB_s), of degree 2|E|. Its coefficients vanish thereafter, so for each fixed graph and flux they satisfy O(q^{θD}) for **every** real θ. For the zero flux K_4, B has eigenvalue q=2, and det(1−zB) has a root at z=1/2. The proposed inference even with θ=0 is false. This is the graph/curve sign reversal already recorded in `graph-ihara.md` §5.

**PROVED: formal identities and the corrected criterion.** Throughout this section Y is finite, connected, simple, (q+1)-regular with q>1; write v=|V|, m=|E| and g=m−v+1. Prime cycles are primitive closed non-backtracking, tailless **oriented** cycles modulo rotation. Reversal is a different prime. There are finitely many at any bounded length, so their free commutative monoid has well-defined formal degree series. For s∈H¹(Y;Z/N), put χ_s(n)=exp(2πi⟨s,[n]⟩/N) and

\[
Q_s(z)=\det(1-zB_s),\qquad
Z_s(z)=\prod_P(1-\chi_s(P)z^{\ell(P)})^{-1}.
\]

Counting rooted cycles gives

\[
zZ_s'/Z_s=\sum_{k\ge1}T_s(k)z^k,\quad
T_s(k)=\sum_{\ell(P)\mid k}\ell(P)\chi_s(P)^{k/\ell(P)}
=\operatorname{Tr}B_s^k.
\tag{12}
\]

The determinant logarithm has the same coefficients and constant term, proving Z_s=Q_s^{-1}. Expanding the Euler factors now proves both

\[
Z_s=\sum_n\chi_s(n)z^{\deg n},\qquad
Q_s=\sum_n\mu(n)\chi_s(n)z^{\deg n}.
\tag{13}
\]

The **poles of Z_s**, equivalently the **zeros of Q_s**, are the inverses of the nonzero eigenvalues of B_s. Ihara–Bass gives
\(Q_s=(1-z^2)^{m-v}\det(1-zA_s+qz^2)\).
These identities do not equate the growth of coefficients of Q_s to its zero locations.

Removing trivial factors does not repair that implication: the remaining determinant is still a polynomial. K₄ at θ=0 remains a counterexample after removing the q and ±1 factors, since its remaining B roots have modulus √2>1. K₄ is the smallest connected simple regular graph with q>1.

The correct exact-exponent statement is

\[
|T_s(k)|=O(q^{\theta k})\ (k\ge1)
\quad\Longleftrightarrow\quad \rho(B_s)\le q^\theta.
\tag{14}
\]

One implication follows by summing at most 2m eigenvalue powers; Jordan blocks do not alter traces. For the converse the generating series in (12) converges on |z|<q^{-θ}; its meromorphic continuation is −zQ_s'/Q_s. Every nonzero root of Q_s is a genuine pole of this logarithmic derivative, with nonzero multiplicity. Thus none can lie in that disk. Equivalently one can use the coefficients of Z_s itself, with an arbitrarily small ε loss at multiple boundary poles. This is the appropriate graph Littlewood analogue, with **all ideals or prime-power traces, not Möbius coefficients**.

After subtracting the known trivial eigenvalue powers (q, also −q for the bipartite zero sector, and the ±1 factors), (14) with θ=1/2 is the usual Ramanujan criterion. For a general unitary flux A_s is Hermitian; each eigenvalue λ contributes roots of x²−λx+q, so the critical-circle condition is exactly |λ|≤2√q. Trivial modes must be removed when they occur, including the sign/length-parity sector; no semisimplicity at a band endpoint is being asserted.

### Q3b — PROVED orthogonality; REFUTED diagonal dominance and unconditional equidistribution; SHARPENED amplifier obstruction

For a class a∈H₁(Y;Z/N) define the integers

\[
b_D(a)=\sum_{\substack{n\ \rm squarefree\deg n=D,[n]=a}}\mu(n),
\qquad c_D(a)=\#\{n\ \rm squarefree:\deg n=D,[n]=a\}.
\]

If a_D(s)=[z^D]Q_s, finite Fourier orthogonality proves exactly

\[
\boxed{\sum_s|a_D(s)|^2=N^g\sum_a b_D(a)^2
=N^g\sum_{\substack{\deg n=\deg n'=D\ n,n'\ \rm squarefree\ [n]=[n']\bmod N}}\mu(n)\mu(n').}
\tag{15}
\]

This is a **signed pair sum**, not a count. Its diagonal contribution is N^g C_D, where C_D=∑_a c_D(a), but cross terms can be negative. For D>2m the left side vanishes exactly, hence the off-diagonal is **−N^g C_D**. The same statement holds coefficientwise in the integral homology group ring, since the determinant identity is valid with independent Laurent edge variables. This invalidates “the diagonal gives a square-root-sized mean square” as a deduction.

**Unsigned squarefree count, with the missing periodicity.** Set

\[
C_s(z)=\prod_P(1+\chi_s(P)z^{\ell(P)})
 ={Z_s(z)\over Z_{2s}(z^2)}={Q_{2s}(z^2)\over Q_s(z)}.
\tag{16}
\]

For the zero flux, C₀ has a simple pole at z=1/q with positive leading constant c_Y. If Y is non-bipartite it is the only pole of that modulus, and for some ρ<q,
\(C_D=c_Yq^D+O_Y(\rho^D)\).
If Y is bipartite, C_D=0 for odd D and
\(C_D=2c_Yq^D+O_Y(\rho^D)\) for even D. Thus C_D ≍_Y q^D only on the allowed degree subsequence. In particular the brief's unrestricted count fails for the cube.

To justify these pole assertions without RH, A₀ is real symmetric with spectrum in [−(q+1),q+1]. Connectedness makes q+1 simple; −(q+1) occurs exactly in the bipartite case. The Bass quadratic shows that the only B₀ eigenvalues on |x|=q are consequently q, and possibly −q. At z=±1/q the numerator Q₀(z²) is nonzero since q^{-2}<q^{-1}. Expanding the resulting rational function at its simple poles proves the assertions; polynomial factors from other poles are absorbed by slightly increasing ρ<q. Positivity of c_Y follows by approaching the positive pole from below in (16).

**What homology bounds, and what it does not.** In cotree coordinates |[n]_j|≤D. For N>2D, congruence of two degree-D classes is equivalent to equality in H₁(Y;Z). Thus (15) stabilizes after division by N^g as N→∞ for fixed D. Null-homologous products and differences of homologous products remain; taking N large does not leave just the diagonal. With U_D(N)=∑_a c_D(a)²,

\[
{C_D^2\over\min\{N^g,(2D+1)^g\}}\le U_D(N)\le C_D^2,
\quad
\left|\sum_s|a_D(s)|^2-N^gC_D\right|\le N^g(U_D(N)-C_D).
\tag{17}
\]

The lower bound is Cauchy–Schwarz and the upper bound just counts all ordered pairs. Even integral homology allows exponentially many unsigned collisions, at least q^{2D} times a polynomial loss on admissible degrees, for fixed Y. A cycle and its reversed partner already give a squarefree product of class zero. These balanced products explain why ordinary orthogonality is not a diagonal estimate. Signed cancellations in (15) are much stronger than these unsigned bounds and become exact above 2m.

There is a sharper stabilization for the **signed** mean square: N^{-g}∑_s|a_D(s)|² is independent of N for every N≥3 and equals the U(1)^g Haar mean square. Indeed the Bass determinant expansion uses vertex-disjoint oriented simple cycles and dimers. Each cotree variable consequently has Laurent exponent in {−1,0,1}; a dimer has exponent zero. In |a_D|² the differences have exponents between −2 and 2. No nonzero such exponent is divisible by N≥3, so finite averaging equals taking the constant term. N=2 can identify the exponents +1 and −1, explaining the different N=2 values in the output. This is a statement about finite determinants, not about the unsigned class distribution.

**PROVED: the corrected equidistribution/amplifier theorem.** Let s have exact order r, and let ε be the character sending every cycle to (−1)^{length}; it is nontrivial precisely when Y is non-bipartite. Let
\(F_s(D)=\#\{n\ \rm squarefree:\deg n=D,\chi_s(n)=1\}/C_D\)
whenever C_D>0. For fixed Y and s, as D→∞:

* If Y is non-bipartite and ε∉⟨s⟩, then F_s(D)=1/r+O(c^D) for some c<1.
* If Y is non-bipartite and ε∈⟨s⟩, then r is even and F_s(D)=(1+(−1)^D)/r+O(c^D).
* If Y is bipartite, F_s(D)=1/r+O(c^D) along even D; it is undefined on odd D.

For s=ε the second formula is exact: F_s(D)=1 for even D and zero for odd D. The cube and this K₄ parity example are the requested loopholes. H₁(Y;Z) is free abelian, never a nonzero group of exponent six; only its mod-six quotient has exponent six.

Proof of the theorem: for any unitary flux t, ρ(B_t)≤q. If equality holds, a Bass root μ with |μ|=q gives a real adjacency eigenvalue μ+q/μ. Its imaginary part is (q−1)sin(arg μ), so μ=±q and the adjacency eigenvalue is ±(q+1). Equality in the adjacency triangle inequality forces the connection to be gauge-equivalent to all +1 or all −1. More explicitly, a maximizing eigenvector has constant nonzero modulus by connectedness; along every edge its transported phase is the same or opposite phase. Therefore t is either 0 or ε. All other Q_t have no root on |z|=1/q. Formula (16) then gives [z^D]C_t=O(ρ_t^D), ρ_t<q, whereas C_ε(z)=C₀(−z). Finally apply the exact root-of-unity filter
\(F_s(D)=r^{-1}\sum_{j=0}^{r-1}[z^D]C_{js}/C_D\).
Only j=0 and, if present, j=r/2 contribute main terms. This proves all cases.

Consequently, among distinct **fixed** fluxes at most the trivial and parity flux can be trivial on asymptotically almost every product of an allowed degree. The parity exception gives at most one extra effective row, not an amplifier whose number of distinct rows grows like q^{h/6}. For r>2 even the parity case has limiting fraction at most 1/2 on even degrees. These assertions concern the actual residue-equality condition χ=1. Closeness of a phase to one is a different condition, particularly if N varies with D.

**NUMERICAL.** `checks/qrh_graph_family.py` enumerates all oriented primes through degree 16 on K₄, Petersen and the cube, checks the prime counts independently against Tr B^k, and expands the signed and unsigned Euler products in the finite homology group ring. It evaluates every flux for N=2,3, and also every N=6 flux on K₄. Exact cyclotomic norms independently verify (15). At K₄, N=2, D=12 the mean square is 2048, with diagonal 10944 and off-diagonal −8896. At D=13 there are 3840 squarefree ideals, the diagonal is 30720 and the mean square is zero. At D=16 the nonparity flux (0,0,1) has fraction 845/1701, whereas the parity flux (1,1,1) has fraction one. Coordinates are the printed cotree edges (1,2),(1,3),(2,3). The output prints fractions for **each** flux, including undefined odd-degree cube fractions.

### Q3c — READING, surface obstruction, and an OPEN quantitative conjecture

The graph has exact Fourier orthogonality and the separate matching-polynomial average theorem in `graph-super.md` §6 / `zn-flux.md` §4. It does **not** have the first half of this specific Möbius-sum mechanism as a spectral statement: (15) has finite support in D and gives no bound on the poles of Z_s. The matching-polynomial theorem averages det(x−A_s), kills nonconstant cycle monomials, and then applies Heilmann–Lieb. This is different from taking squared coefficients of Q_s, and neither theorem alone selects an arbitrary flux with the Ramanujan property.

There are geometric and nongeometric ways to prove graph bounds. LPS uses arithmetic and Deligne; the Marcus–Spielman–Srivastava interlacing construction gives bipartite Ramanujan families, and Hall–Puder–Sawin gives **one-sided** Ramanujan covers of a general base graph, two-sided new-spectrum bounds for a bipartite base. These are existence results, not assertions that every lift or every flux is Ramanujan. See [Hall–Puder–Sawin](https://arxiv.org/abs/1506.02335). Friedman and [Bordenave](https://arxiv.org/abs/1502.04482), and [Bordenave–Collins](https://arxiv.org/abs/1801.00876), give near-Ramanujan bounds with high probability for the relevant random graph/lift models. Alon–Boppana supplies the asymptotic lower obstruction at 2√q for growing regular graphs. These results do not follow from (15), and also show why “geometry is necessary for every graph proof” is too strong.

**PROVED: Fourier duality is not the amplifier.** A graph already has a canonical perfect evaluation pairing H¹(Y;Z/N)×H₁(Y;Z/N)→Z/N, without being on a surface. What it lacks is a canonical intersection self-pairing of H₁; graphs are not closed oriented surfaces. The number-field amplifier uses more than having rows and columns in the same ring: multiplicativity in the row gives χ_n(p⁶)=1 outside a prime-dependent divisibility mask, and there are many different primes with small masks. The local conductor/divisibility structure is essential. The graph flux is already a character after gauge quotient, with no such prime-dependent zero mask.

For a cellular ribbon graph on a closed oriented surface Σ of genus a, use the projection j:H₁(Y)→H₁(Σ) and the unimodular intersection form J on H₁(Σ). The most literal surface candidate is

\[
K_N(b,n)=\exp(2\pi i\langle b,Jj[n]\rangle/N),\qquad b\mapsto6b.
\tag{18}
\]

This makes rows into cycles, as requested. But **the conjecture that (18) is a sixth-power amplifier is REFUTED**: a multiplicative sixth power becomes multiplication by six after abelianization. For N coprime to six this is a permutation of the fluxes. For general N its kernel has gcd(N,6)^{2a} elements, all giving the **same** trivial character. At N|6 every resulting row is the trivial character. Counting these copies multiplies the relevant mean-square contribution by exactly the same factor; no amplification gain results. The face-cycle kernel of j only adds further duplicates. This finite algebraic obstruction is tested on a torus for N=2,3,6,7,12 by the script.

One useful surviving **OPEN conjecture C-SURF** concerns the finite test's scale, not an asserted RH proof. For a fixed cellular ribbon graph with surjective j, the unsigned squarefree-product homology j[n], conditioned on degree D, should obey a nondegenerate lattice local central limit theorem on its admissible degree/homology cosets:

\[
\Pr(j[n]=x)\sim {\operatorname{covol}(\Lambda_D)\over
 (2\pi D)^a\sqrt{\det\Sigma_Y}}
 \exp\!\left(-{x^T\Sigma_Y^{-1}x\over2D}\right)
\tag{19}
\]

uniformly for x=O(√D) in those cosets, with the periodicity and covolume stated explicitly in a proof. This predicts a crossover of mod-N homology distribution at N≈√D; it prevents confusing fixed-N equidistribution with the growing-level situation. It is plausible from the dominant eigenvalue of B_s near trivial/parity phases and (16), but a uniform local theorem is not proved here.

The finite test uses a genuine genus-one ribbon structure on K₄ with two faces of lengths 3 and 9 and face homology ±(0,0,1). Thus j sends the printed cotree coordinates to their first two coordinates. It computes exact integral projected homology through D=16, using modulus 33>2D to avoid collisions, and prints D·Pr(j[n]=0) and Cov(j[n])/D at D=8,12,16. This tests stabilization predicted by (19); three small degrees cannot establish it. Even a proof of (19) would describe homology distribution, not restore the Möbius spectral criterion refuted in Q3a.

## Correction ledger (updated as calculations finish)

1. A zero-free |z|<r region is a disk; the lower bound for zero moduli is ≥r, not ≤r. The functional equation can turn the two-sided conclusion into an annulus.
2. Even primitive characters require removing 1−z before saying that all roots have modulus q^{-1/2}.
3. The graph Möbius series is a polynomial. Its coefficient growth is not a spectral criterion; cancellation is exact above degree 2|E|.
4. The graph mean square is a signed homologous-pair sum. Its positive diagonal is not a lower bound, and need not govern its size. The matching-polynomial “RH on average” theorem is a different average.
5. Squarefree graph ideals have growth ≍q^D only on admissible degrees: the cube has none in odd degree. Non-bipartiteness alone does not give every nontrivial flux a 1/r limit; the length-parity flux is the exception.
6. An exact cubic Gauss evaluation exists over F_q[t], but retains a discriminant character. Calling the theta step “collapsed” would confuse evaluation of a summand with an estimate for a family of sums.
7. H₁(Y;Z) has no torsion. Passing to H₁(Y;Z/6) makes 6b=0, producing duplicate trivial characters rather than arithmetic prime masks. Poincaré duality on a surface does not change this.
8. HPS is one-sided for general bases; bipartiteness supplies the two-sided conclusion. Random-lift near-Ramanujan theorems and exact Ramanujan existence are different statements.
9. Neither a conditional 11/12 result nor these counterexamples prove that every possible RH proof must construct integral H¹. The ladder is a structural reading, not a necessity theorem about proof methods.

## Source map and verification scope

The supplied [11/12 manuscript](../qrh/sources/qrh-11-12-openai-2026-10-05.txt) was read in §§1–3 and for the statements in §§4–6, with the arithmetic argument in Appendix A.1 checked against the finite-field derivation. Relevant local line anchors are 214–236 (mean square and amplifier), 651–724 (Littlewood deduction), 761–781 (Gauss identities), 1094–1103 and 1134–1144 (dual and completed bounds), 1276–1289 (transfer), 1519–1563 (theta formula and uniformity), and 2180–2260 (prime Jacobi evaluation). [Kintali §1](../qrh/sources/kintali-qrh-2026-10-07.txt) was used only to distinguish its 47/48 probe/reflection argument from this amplifier; its theorem is not an input here. Project conventions and the graph sign reversal were checked against the requested ladder, Dirichlet, flux, super-Ihara and Ihara pages, plus `gauge-groups.md`.

Both check programs run with plain `python3` from this lane; dependencies are those listed in their headers. All quoted counts and mean squares are integers or rational numbers. Only reported logarithmic exponents use machine floating point. Root approximations use 80-digit arithmetic, print polynomial residuals, and have a separate exact quadratic certificate. No numerical spectral computation is used to establish (6), (9), (14), (15), or the graph equidistribution theorem.

## Numerical checks for the blind lane

Run `python3 checks/qrh_ff_family.py` and `python3 checks/qrh_graph_family.py` from `notes/astra-2026-10-23/qrh-transpose/`. They write `checks/output_ff.txt` and `checks/output_graph.txt`.

1. **F₇[t], D=3,h=4:** ν=(·/(t³+t+1))₂; all 16807 rows give S=4238010. The normalized ratio per row is 86490/117649. This is a direct enumeration, not the complete-range identity.
2. **Amplifier/inverse check:** for that ν, A₁(1),…,A₁(5) are −3,2,15,−59,72. Every linear p passes the exact sixth-power identity at all five degrees. L=1+3z+7z² is computed from characters before the comparison roots.
3. **K₄, N=2,D=12:** mean square 2048 = diagonal 10944 − 8896. At D=13 it is 0 = 30720 − 30720 despite 3840 squarefree products.
4. **Equidistribution/parity:** at K₄,D=16,N=2, s=(0,0,1) has fraction 845/1701; s=(1,1,1) has fraction 1 (and has fraction 0 at D=13).
5. **Surface finite test:** for the printed torus ribbon K₄ at D=16, projected integral class zero occurs 1188 times among 27216 products; D·Pr(0)=44/63. The corresponding values at D=8,12 are 8/11 and 14/19. This is evidence for a proposed local limit, not an amplifier.

## What this changes in the notebook

No existing page or registry was edited. Suggested annotations, after independent review:

* **`data-ladder.md` §2, family rung:** “The quasi-RH family estimate transfers to a single arithmetic row through many distinct sixth-power rows with small divisibility masks. Conditional on its function-field short-row analogue this yields 11/12, not 1/2. Graph flux orthogonality supplies neither the same amplifier nor a Möbius-coefficient spectral criterion: the latter series is a finite determinant, and its signed mean square eventually vanishes.”
* **`data-ladder.md` §4, missing positivity:** “A quantitative family estimate can give partial zero exclusion without constructing the proposed global integral H¹. This does not supply the polarisation-type positivity at the critical exponent. The geometric interpretation is a description of the understood arithmetic structures, not a theorem that every RH proof must explicitly construct H¹; Bombieri–Stepanov uses Riemann–Roch function spaces, and graph existence proofs can use interlacing.”
* **`graph-super.md` §6 / `zn-flux.md` §4:** distinguish the matching-polynomial average from the squared Möbius-coefficient average. The latter is N-independent after normalization for N≥3, but has no large-degree spectral content. **`gauge-groups.md`:** qualify HPS as one-sided for general bases. **`ff-dirichlet.md`:** its distinction between L and Λ is correct and should also be used in future briefs.

Candidate rows (proposals only; none registered, no external review yet):

| candidate | status | precise scope / dependencies |
|---|---|---|
| `prop:ff-sextic-amplifier` | PROVED-conditional | H-MS in (3) ⇒ (4)–(5) ⇒ zero-free disk q^{-11/12}; fixed q,ν |
| `prop:ff-complete-row-ms` | PROVED | exact (6), h≥2D−1; elementary character orthogonality |
| `prop:ff-gauss-discriminant-absorption` | PROVED | (8)–(9); Hasse–Davenport lifting and the proved Pellet identity |
| `obs:graph-mobius-littlewood-fails` | REFUTED proposed equivalence | K₄ counterexample; corrected trace criterion (14) PROVED |
| `prop:graph-flux-signed-ms` | PROVED | (15), vanishing for D>2m, normalized stabilization for N≥3 |
| `prop:graph-squarefree-flux-parity` | PROVED | (16)–(17), fixed-flux distribution with the exact parity exception |
| `prop:surface-sixfold-no-amplifier` | PROVED | perfect intersection pairing gives only duplicate kernel rows in (18) |
| `conj:ff-short-row-ms` | OPEN in this lane | (3); not inferred from the long-row table or from Weil |
| `conj:surface-squarefree-local-limit` | OPEN | (19); finite torus test, no uniform error estimate claimed |

**Next step.** The arithmetic bottleneck is now precise: prove a uniform transformation/transfer bound for the discriminant-character column sums after (7)–(9), keeping common factors, zero masks and the fixed ν. The quadratic large sieve is only useful after this reduction. Numerically, the next expensive cell is the full short family at q=13,D=5,h=5; it is deliberately absent from the claimed verification. A useful acceleration would reconstruct character L-polynomials from finite Gauss sums and the functional equation (which does not assume RH), with an independent direct-row audit before using it. On the graph side, any proposed new mechanism must act on the trace series (12) or on Z_s, and must add structure beyond surface Fourier duality. The local-limit conjecture is a separate, testable description of that family's homology distribution.
