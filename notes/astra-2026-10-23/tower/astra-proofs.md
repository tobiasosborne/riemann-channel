# Lane T: torsion similitudes, strict genera, and the global lattice

Author: `codex:gpt-6-astra`, 2026-10-23. Record only; nothing registered. All new files are in this lane. No RH assumption or number-field zero is used.

**SHARPENED.** The arbitrary-multiplier torsion tower determines the ordinary isogeny class and its endomorphism order, and no further ideal-class information. The **strict** tower determines the genus, namely the ideal-class torsor modulo squares. Thus the proposed blindness theorem and lane U's discriminant −24 separation are consistent: they use different equivalence relations. The blanket T4 sentence is false. In particular, the actual q=7 example is Q(√−6), discriminant −24, not Q(√−7).

## 0. T0 — definitions and scope (PROVED / conventions)

Fix q=p^r and an ordinary elliptic curve. Identify its rational endomorphism algebra with K=Q(π), fixing π. Its geometric and F_q endomorphism rings agree. Put D_E=E(F̄_q). This is a discrete torsion group, with its Frobenius action. Each finite subgroup of elements killed by N is denoted D_E[N]. For p∤N it is (Z/N)^2, with the canonical principal-polarisation Weil pairing into the **common** group μ_N(F̄_q).

The qualification p∤N is essential for perfect rank-two Weil pairings. The question defined geometric points, not finite flat group schemes: D_E[p^a] has rank one, and μ_{p^a}(F̄_q) is trivial. We retain this étale p-primary summand, with its Frobenius, but do not pretend it is rank two. A full ordinary p-divisible group can also be included; it adds no obstruction here, since O_p is split maximal. The literal identification D_E=(L⊗Q)/L in lane U must exclude p or select the periodic p-primary summand.

For N|(q^k−1), the reduced Tate pairing has domain

    t_{N,k}: E(F_{q^k})[N] × E(F_{q^k})/N E(F_{q^k}) → μ_N.

Merely putting both arguments in E[N] is not its full definition; such a restriction can be degenerate. Nor does N|(q^k−1) imply all E[N] is rational. We use the full displayed domain, so the theorem also implies blindness of every restriction requested in the question.

An isomorphism of the **similitude tower** is one π-equivariant group isomorphism Φ:D_E→D_E′ and one compatible automorphism a of μ_{p′∞}. Write its restriction as ζ↦ζ^{a_N}, with a_N∈(Z/N)^× and a_{N′}≡a_N mod N for N|N′, p∤N′. We require

    e′_N(ΦP,ΦQ)=e_N(P,Q)^{a_N},
    t′_{N,k}(ΦP,Φ[Q])=t_{N,k}(P,[Q])^{a_N}.

The second multiplier is the **same** as the first and is independent of k. Equivalently, the maps Φ_N commute with inclusions D[N]⊂D[N′] and with multiplication maps [N′/N]:D[N′]→D[N]. They induce the maps on ker(π^k−1) and their N-quotients. These commute with field-extension inclusions and Frobenius traces. The root maps commute with inclusions and powers. This specifies compatibility; separate choices for every N without it are insufficient.

The **strict tower** fixes the identity on the common μ_N, so a_N=1 for every N. Identifying these groups with complex roots through a fixed Deligne embedding ε is a way of displaying that choice, not an extra property of the curves. Allowing inversion at an isolated level is a weaker comparison at that level; requiring one global inversion along the tower differs from allowing independent signs at every prime. None of these conventions should be substituted for arbitrary compatible automorphisms of μ_N. Lane U uses arbitrary units for its consistency checks, and fixed roots with equality or inversion for its separation/Clifford obstruction. It does **not** define one global arbitrary-multiplier isomorphism and then claim that it is impossible.

## 1. T1 — the compatible blindness theorem (PROVED)

**Theorem.** For ordinary E,E′/F_q in the same isogeny class, their similitude towers are isomorphic if and only if End(E)=End(E′) inside K. Their strict towers need not be isomorphic.

### 1.1 Ideal action and compatible maps

Use the ordinary ideal-action classification (Waterhouse 1969; Deligne 1969): curves with multiplier order O in the fixed ordinary isogeny class form a torsor under Pic(O), the group of invertible proper ideals. Choose c carrying E to E′. Every such class has an integral representative prime to any prescribed finite set of primes. One proof is approximation in an invertible ideal: choose a generator at each of the finitely many completions, impose the resulting congruences by CRT, and multiply by a suitable principal fractional ideal. This also avoids p and the conductor if desired.

For **each rational prime ℓ**, fix once and for all a representative A_ℓ of c with degree d_ℓ=Norm(A_ℓ) prime to pℓ. Compose the ideal isogeny E→A_ℓ*E with an F_q-isomorphism to E′, and call it φ_ℓ. It has degree d_ℓ. Since its degree is prime to ℓ, it is an isomorphism of the entire ℓ-divisible geometric-point group. Define

    Φ = ⊕_ℓ φ_ℓ | D_E[ℓ^∞].

Every point has finitely many primary components. Hence this is a genuine group isomorphism, not a limit of incompatible choices. It commutes with π, with every multiplication map and with all field-extension maps. Put a_ℓ=d_ℓ∈Z_ℓ^× for ℓ≠p, and a=(a_ℓ)∈∏_{ℓ≠p}Z_ℓ^×. CRT supplies a_N at every prime-to-p level. At mixed levels the primary pairings have zero cross terms, so this same a works for the whole tower.

This repairs the gap in the proposed proof: choosing an ideal prime to N′ shows compatibility for its divisors, but does not by itself supply an infinite compatible family. Fixing one isogeny on **each whole primary tower** does. Alternatively, finite nonempty sets of compatible maps on cofinal levels admit an infinite path by compactness; surjectivity of every transition map is unnecessary.

### 1.2 Weil and Tate functoriality

For an isogeny φ:E→E′ defined over F_q, with dual φ̂, the principal polarisations give

    e′_N(φP,Q′)=e_N(P,φ̂Q′),
    e′_N(φP,φQ)=e_N(P,Q)^{deg φ}.

This is the dual-isogeny identity of Silverman, *The Arithmetic of Elliptic Curves*, III.8 (bibliographic citation from memory). It is valid without coprimality of the degree and N; coprimality makes φ an isomorphism on N-torsion and its exponent a unit.

Here is the corresponding Tate statement, including the domains. For P∈E(F_Q)[N], Q′∈E′(F_Q), Q=q^k and N|Q−1,

    t′_{N,k}(φP,[Q′]) = t_{N,k}(P,[φ̂Q′]),
    t′_{N,k}(φP,[φQ_0]) = t_{N,k}(P,[Q_0])^{deg φ}.       (1)

**Proof.** For NR=Q_0, the Kummer cocycle is δ_N(Q_0)(σ)=σR−R, where σ=π^k. The reduced Tate pairing is evaluation of this cocycle against P by the Weil pairing, with one fixed argument/sign convention. For example, choose t(P,[Q_0])=e_N(P,σR−R). Naturality δ_N(φQ_0)=φδ_N(Q_0) and the dual-isogeny identity give (1) immediately. Using the opposite convention inverts both Tate pairings and leaves (1) unchanged. Independence of R follows because P is σ-fixed and μ_N is σ-fixed. The quotient by N E(F_Q) is precisely the Kummer quotient. ∎

For a source with all composite N and this full domain, see Peter Bruin, [*The Tate pairing for Abelian varieties over finite fields*](https://www.numdam.org/item/10.5802/jtnb.764.pdf), J. Théor. Nombres Bordeaux **23** (2011), 323–328, §3 equation (3.2) and §4 Theorem 4.1. It identifies Kummer evaluation with the reduced Frey–Rück pairing; (1) is the naturality deduction just proved. Bruin writes his Weil arguments in the opposite order to the displayed convention. Frey–Rück (1994), Lichtenbaum (1969), and Schaefer (2005) are the historical references. Exact **unreduced** values from Miller functions are only representatives in F_Q^×/(F_Q^×)^N; (1) is an equality in that quotient or for the reduced pairing, not for arbitrary representatives.

Apply (1) to φ_ℓ on the ℓ-primary groups, including division points R in D_E[ℓ^∞]. The single Φ of §1.1 therefore preserves every reduced Tate pairing with exactly the same compatible multipliers as every Weil pairing. The Tate data add no obstruction to a compatible Frobenius/Weil-tower isomorphism.

### 1.3 Groups and recovery of the order

Lenstra, [*Complex multiplication structure of elliptic curves*](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1996c/art.pdf), J. Number Theory **56** (1996), 227–241, Theorem 1(a), gives

    E(F_{q^k}) ≅ O/(π^k−1)O ≅ E′(F_{q^k})

as O-modules. The notebook already records this as `cit:lenstra-structure`. These individual isomorphisms need not be chosen canonically or compatibly; Φ above supplies compatible group identifications directly. In ideal language, invertible I gives I/(π^k−1)I, and a rank-one invertible module over the finite semilocal ring O/(π^k−1) is free.

Conversely, the tower recovers T_ℓE for each ℓ≠p and its π-action. Tate's finite-field endomorphism theorem gives

    End_{Z_ℓ[π]}(T_ℓE)=O⊗Z_ℓ.

Ordinariness implies p∤(a²−4q), so O is already maximal at p. The completions determine O. Counts recover a=q+1−#E(F_q) and hence the isogeny class over the fixed field. Thus the invariant is exactly (isogeny class,O), with no additional distinction among Pic(O)-translates. When h(O)=1 the class is of course unique; “never the class” means no **additional** information within a fixed order, not that uniqueness cannot occur.

The torsor and Deligne inputs above are standard cited theorems, not new claims about the existence of CM lifts. Waterhouse, *Abelian varieties over finite fields*, Ann. Sci. ÉNS **2** (1969), 521–560; Deligne, *Variétés abéliennes ordinaires sur un corps fini*, Invent. Math. **8** (1969), 238–243. The existing `cit:latimer-macduffee` is consistent with this: fixing the multiplier ring selects invertible classes of that order, rather than only the principal Z[π]-lattice.

## 2. T2 — precisely the genus, with a finite-level qualification (PROVED / SHARPENED)

**Theorem.** Fix the ordinary isogeny class and O. Two strict towers are isomorphic if and only if their relative class c lies in Pic(O)². Thus the strict tower distinguishes the torsor Pic(O)/Pic(O)², not a preferred principal class. For h=2 it distinguishes both classes; for h=3 it distinguishes none. The proposed norm-residue intuition is correct for the compatible tower, provided “principal norms” means local units, not merely the global units O^×.

### 2.1 The exact sets at a modulus

For every N define

    H_N = {Norm(u) mod N : u∈(O/NO)^×},
    S_N(c) = {Norm(A) mod N : A integral invertible, [A]=c, gcd(Norm(A),N)=1}.

Choose any representative A_0 of c prime to N and put d=Norm(A_0). Then

    S_N(c)=d H_N.                                             (2)

In particular c↦S_N(c) is a homomorphism Pic(O)→(Z/N)^×/H_N. The quotient has exponent at most two: the norm of a scalar u is u². This explains why replacing a class by its inverse cannot change these sets.

**Proof of (2).** Another representative is A=αA_0. At ℓ|N, both ideals are O_ℓ, so α∈O_ℓ^×. Hence its norm residue is in H_N. Conversely, prescribe any element of (O/NO)^× as the residue of α. The fractional lattice A_0^{-1} has completion O_ℓ at every ℓ|N, so CRT in that lattice gives α∈A_0^{-1} with the prescribed residues. Then αA_0 is integral, invertible, in c and prime to N. Its norm is d Norm(α), proving surjectivity. Additional conditions at the conductor or p can be imposed at the same time. ∎

One can compute S_N(c) by taking all unit values mod N of the primitive positive binary norm form in c (or c^{-1}, which has the same represented integers). This is a finite exhaustive computation, not a bounded search for ideal representatives. `checks/tower_strict.py` implements exactly that computation.

The image of the **compatible** multiplier coset at N is S_N(c). To see this, start with a prime-to-N ideal isogeny of degree d. Every automorphism of the entire local Tate module commuting with π is multiplication by a unit of O_ℓ, whose determinant is its norm. Reduction gives dH_N. Such local units lift all units of O/NO. Fixed-level π-centralisers can be larger if ℓ divides [O:Z[π]]; their extra elements need not extend to the tower.

**Explicit caveat (NUMERICAL, proved by the displayed matrices).** For O=Z[ω], ω²−ω+2=0, π=3+7ω, q=128 and a=13, the matrix of π on O is [[3,−14],[7,10]]. Modulo 7 it is scalar, so its centraliser is all GL₂(F_7), with determinant set {1,2,3,4,5,6}. But Norm((O/7)^×)={1,2,4}. The extra determinants {3,5,6} do not extend to π-equivariant automorphisms of the full 7-adic module. Therefore (2) is not automatically the set of **all isolated-level** intertwiners for an arbitrary order. The discriminant −24 examples have O=Z[π], so there is no such caveat there.

### 2.2 Why all these local obstructions equal the genus obstruction

Here is a proof, including nonmaximal quadratic orders. In a fixed complex embedding, realise a proper invertible ideal A as an oriented lattice. Its canonical principal alternating form is Ω_A=Ω_O/Norm(A), restricted to A; for fractional ideals use the positive rational norm. Locally A_ℓ=a_ℓO_ℓ. A π-equivariant map O_ℓ→A_ℓ is multiplication by x_ℓ∈K_ℓ, since π generates K over Q. It is an isomorphism exactly when x_ℓ generates A_ℓ, and is strict exactly when

    Norm(x_ℓ)=Norm(A).                                       (3)

For two arbitrary ideal lattices the same argument uses their quotient class. At p the order is split maximal, so there is always a solution of (3); the geometric p-torsion omitted half introduces no condition. Positivity supplies the real-place condition automatically.

If [A]=[B]², write A=αB². Let b_ℓ generate B_ℓ. Put

    x_ℓ = α b_ℓ² · Norm(B)/Norm(b_ℓ).

The final scalar is an ℓ-adic unit, so x_ℓ generates A_ℓ; its norm is Norm(α)Norm(B)²=Norm(A). Thus squares admit compatible strict identifications.

Conversely suppose (3) is solvable at every ℓ. Choose A prime to the conductor. The equation Norm(x)=Norm(A) has solutions at every finite place and at infinity. The Hasse principle for a quadratic norm equation (equivalently Hasse–Minkowski for its ternary conic) supplies α∈K^× with Norm(α)=Norm(A). Weak approximation on this rational conic lets α approximate x_ℓ at each conductor prime closely enough that α∈A_ℓ O_ℓ^× there. Now B=A/(α) is an invertible fractional ideal, prime to the conductor, of norm one. Away from the conductor its ideal factorisation is unique. At an inert or ramified prime its exponent must be zero; at a split prime the two exponents must be opposites. Consequently B=C/\bar C for an invertible fractional ideal C prime to the conductor. Since [\bar C]=[C]^{-1}, [A]=[B]=[C]². This proves necessity and the theorem. ∎

This is the ideal-theoretic principal genus theorem. Equivalently, the norm forms Norm(x)/Norm(A) are locally integrally isometric at every place exactly when their proper classes differ by a square. The proof used the standard Hasse principle and weak approximation for conics, not an assumption that a genus contains one class. Compactness of O_ℓ^× shows that satisfying the strict condition at every power ℓ^a gives a single solution of (3); arbitrary separate congruence solutions are enough because their closed solution sets are nested in a compact set.

Once the strict Weil identification is made, all Tate pairings agree by Kummer naturality (§1.2). They do not refine this genus quotient. Genus is therefore both an upper bound **and** the exact invariant for the strict tower defined here.

### 2.3 The actual lane-U examples

For q=7, a=2, π=1+√−6 and O=Z[√−6], the primitive forms are f_0=x²+6y² and f_1=2x²+3y². Let c be the nontrivial class. The exact norm sets are:

| N | H_N=S_N(1) | S_N(c) |
|---|---|---|
| 2 | {1} | {1} |
| 3 | {1} | {2} |
| 4 | {1,3} | {1,3} |
| 8 | {1,7} | {3,5} |
| 9 | {1,4,7} | {2,5,8} |
| 16 | {1,7,9,15} | {3,5,11,13} |

These are printed in `checks/output_strict.txt`; intertwiners are enumerated independently and have exactly these crossed determinant sets. At N=8 the rational 3-isogeny gives multiplier 3 and local unit norms give {1,7}; at N=3 the rational 2-isogeny gives multiplier 2 and local unit norms give {1}. Thus strict separation already occurs at 3; separation **even allowing inversion** occurs at 8. Every level still admits an arbitrary-unit similitude, as T1 requires.

The Q(√−7) example is instead the q=2 E mode and the CM curve 441d1 in `check_cm_tower.py`. Its maximal order has class number one. Its sets are just the principal-form values x²+xy+2y²: all units for N=2,3,4,8, and {1,2,4} for N=7. A restricted norm image at a ramified prime does not imply multiple ideal classes. The CM check across different rational primes also requires a single ε to compare curve-to-code assignments; this one-fixed-F_q theorem does not complete that separate cross-prime normalisation problem.

For D=−23 the forms (1,1,6), (2,−1,3), (2,1,3) have identical S_N for every N by the theorem (Pic has order three). The script prints determinant-one intertwiner witnesses for all three at N=2,3,4,8,16,23. These finite tests illustrate, and do not replace, the all-level theorem.

## 3. T3 — audit verdict (PROVED for the distinction; NUMERICAL for finite comparisons)

### 3.1 Orders, without a guessed CM field

All rows below are printed by `checks/tower_audit.py`.

| field, trace | curve | disc Z[π] | End(E) | conductor in O_K | verdict |
|---|---|---|---|---|---|
| F_7, 2 | E_4: y²=x³+3x+3, j=4 | −24 | Z[√−6] | 1 | same order, different strict genus |
| F_7, 2 | E_5: y²=x³+x+3, j=5 | −24 | Z[√−6] | 1 | same order, different strict genus |
| F_5, −2 | y²=x³+4x, j=3 | −16 | Z[i] (disc −4) | 1 | different order from next row |
| F_5, −2 | y²=x³+4x+1, j=1 | −16 | Z[2i] (disc −16) | 2 | different order from previous row |
| F_41, 12 | y²=x³+x+17, j=40 | −20 | Z[√−5] | 1 | second same-order pair |
| F_41, 12 | y²=x³+3x+11, j=12 | −20 | Z[√−5] | 1 | second same-order pair |

For −24 and −20, the discriminant of Z[π] is already fundamental, so the inclusions Z[π]⊂End(E)⊂O_K **force** conductor one. A volcano traversal cannot improve this certificate. For the F_5 pair, the only possible conductors are one and two. Full rational 2-torsion is equivalent to factoring π−1 through [2], hence to (π−1)/2∈End(E); that element generates Z[i]. The two rational 2-torsion sizes are four and two, respectively. This is the elementary divisibility criterion underlying the order/volcano computation (Kohel, *Endomorphism rings of elliptic curves over finite fields*, Berkeley thesis, 1996, bibliographic citation from memory; [thesis record](https://math.berkeley.edu/publications/endomorphism-rings-elliptic-curves-over-finite-fields)). It proves the orders, not merely a possible list of orders.

The brief's proposed `ellisomat` shortcut needs correction: [PARI documents `ellisomat` for number fields](https://pari.math.u-bordeaux.fr/dochtml/ref/Elliptic_curves.html#ellisomat), not as a finite-field volcano routine. `ellisogeny`, with a known kernel, is applicable here. The provided cypari2 branch uses it and does not rely on `ellisomat`.

### 3.2 Lane F: classification (b) for q=7, (a) for q=5

The exact statement is `overlap-data.md` §4 Proposition 3: there is no π-equivariant E_4[8]→E_5[8] preserving e_8 even up to inversion; every such map at N=3 inverts e_3. The preceding Findings and §3 item 4 **already say genus**. The proof there computes Norm(x+y√−6)=x²+6y² and multiplies it by the degree of a horizontal isogeny. It is correct. This is case **(b)**, not case (a), and not a non-equivariance artefact (c).

The explicit isogenies from E_4 are the Vélu quotient by {(1,0),O}, of degree two with target E_5, and the quotient by {±(3,2),O}, of degree three with target y²=x³+4x+3, followed by (x,y)↦(4x,y). Fix the latter on the entire 2-primary tower and the former on every odd-primary tower. This gives the compatible Φ of T1. Its cyclotomic multiplier is 3 in Z_2^× and 2 in Z_ℓ^× at every odd ℓ≠7. Both curve maps and their Frobenius equivariance are tested, rather than inferred from an arbitrary basis matching.

`checks/audit_overlap_refinement.py` independently recomputes all seven W1 levels N=2,3,4,5,8,9,16 with exact finite fields and Miller pairings. Its scale sets are {1}, {2}, {1,3}, {1,2,3,4}, {3,5}, {2,5,8}, {3,5,11,13}. It verifies the degree-two/degree-three pairing identities as well. These agree with the norm sets and with enumerated π-intertwiners. The F_5 overlap/group separation is case **(a)** and remains valid.

The correction needed is therefore to the **unqualified summaries** “the Weil pairing sees the class”: replace them by “the strict Frobenius/Weil tower sees the genus; here each genus consists of one class.” Do not replace the q=7 verdict by “different orders.”

### 3.3 Lane U: classification (b); all 42 comparisons independently reproduced

The original file has two distinct comparisons. C1 allows every unit multiplier and establishes consistency; C3/K1 disallow all multipliers except ±1 and establish strict separation even allowing complex conjugation. T1 proves the former is inevitable at the compatible-tower level; it does not refute the latter. Physical unitary conjugation fixes scalar commutators, and antiunitary conjugation inverts them. An arbitrary automorphism ζ↦ζ³ of μ_8 is not implemented by such a scalar-preserving unitary comparison. Changing the equivalence relation changes what the code is allowed to forget.

The exact independent replay retains the original source's lattice routines, case list and assertions and replaces only its GP boundary by a separate finite-field/group-law/Miller implementation. **22/22 assertions pass, including all 42 comparisons.** An additional check requires a common Weil/Tate multiplier for **each** equivariant map in all 25 cases where both pairings are present. This passes after using one consistent Tate sign. Thus we also check the stronger simultaneous condition which the original C1, with separate sets, did not explicitly assert.

Under lane U's normalisation w_8+w_8^{-1}=3, the reproduced N=8 table is:

| curve versus lattice | Weil at k=8 | Tate at k=8 | Tate at k=4 |
|---|---|---|---|
| E_4 versus (1,0,6) | {3,5} | {3,5} | {3,5} |
| E_4 versus (2,0,3) | {1,7} | {1,7} | {1,7} |
| E_5 versus (1,0,6) | {1,7} | {1,7} | {1,7} |
| E_5 versus (2,0,3) | {3,5} | {3,5} | {3,5} |

At k=4 the 2-primary rational group is Z/8×Z/4: the Tate pairing uses its rational torsion and quotient; it does **not** assert that full E[8] is rational. Full E[8] appears at k=8. The shifted-root normalisation swaps curve-to-lattice assignments exactly as in the original table. The separation is case **(b)**. There is no evidence for case (c).

The sign needs to remain explicit: the old Python `tate_exp` uses **1−M^k**, while the page's final Tate formula uses **M^k−1**. At N=3 its matched Weil scale is +1 and its matched Tate scale against the old helper is −1. Inverting the helper's Tate form reconciles them. This is a uniform convention difference, already recognised by C10, not a class-dependent discrepancy and not an extra Tate invariant.

Two scope corrections emerged from reading the proofs and CM script:

* The page's unconditional “well defined iff N|q^k−1” needs the presence of a rational point of **exact** order N. Generally the condition is exp(G_k[N])|(q^k−1). For q=2, k=1, E1 has G=Z/4; at N=3 the first argument is zero, so the formula is trivially well defined although 3∤1. This does not affect the defined Tate domain N|q^k−1 or any of the separation tests.
* `check_cm_tower.py` stops at the first matching choice among ψ and ψ̄. It does not prove the page's parenthetical “not its conjugate.” In the basis (1,ω), ω²−ω+2=0, C=[[1,1],[0,−1]] conjugates multiplication by u+vω to multiplication by u+v\barω, with determinant −1. Hence both choices match under arbitrary root automorphisms. The independent CM replay passes **27/27** original assertions and verifies C for every checked prime. The common ε across different reduction primes remains a separate normalisation task, not settled by these consistency checks or by T1.

### 3.4 What was actually run; PARI limitation

The requested original scripts were invoked. Here neither `gp` nor `cypari2` is installed. The shared brief's named environment did not exist; creating its venv succeeded, but installing cypari2 failed because shell network/DNS access is unavailable. The original F, U and CM runs therefore stop at their first `gp` subprocess. The full exceptions and source hashes are in `output_legacy_*.txt`. **Their historical PARI pass counts are not reported as newly rerun PARI results.**

Completed fresh checks are `tower_strict.py`, `tower_audit.py`, `audit_overlap_refinement.py`, `replay_tower_flint.py` and `replay_cm_flint.py`. Their `output_*.txt` files label the backend. The independent curve arithmetic is exact `python-flint` (version printed separately), with deterministic Python sampling followed by algebraic certificates: generator orders and a primitive Weil value prove the group structure once its cardinality is known. Base counts are enumerated; extension counts use the Frobenius recurrence, with no hypothesis about its eigenvalue sizes. For k≤2 they are also enumerated. Every finite field's defining polynomial, torsion basis, Frobenius matrix, root and pairing exponents used in the main audit is printed.

`tower_audit.py` includes a cypari2 validation branch using `ellcard`, `ellgroup`, `ellweilpairing`, `elltatepairing` (reduced by (p^k−1)/N), and `ellisogeny`, with explicit finite-field conversions. `rerun_legacy.py` evaluates the original unchanged GP programs through cypari2 when available. Those branches are **prepared but unexecuted here**. Therefore the requested PARI-specific NUM item remains PARTIAL even though the mathematical audit and independent curve computations are complete. The original overlap script's separate Riemann–Roch incidence statistics were not reimplemented or promoted by this audit.

## 4. T4 — the ladder, corrected (REFUTED as worded; SHARPENED)

**REFUTED.** “Every local or torsion datum, including pairings, determines at most the order” is false with fixed pairing targets. The same q=7 curves in the question are its counterexample: both have O=Z[√−6], yet the strict towers differ already at N=3, and differ even up to inversion at N=8. Likewise, a syndrome **torus with its topology and step** is not just an abstract torsion tower.

The smallest field counterexample is already q=4. Write F_4=F_2[t]/(t²+t+1). The curves y²+xy=x³+t and y²+xy=x³+t+1 both have four rational points, trace one and maximal order of discriminant −15, with distinct j-invariants t+1 and t. Its two forms (1,1,4),(2,1,2) have crossed determinant set {2} mod 3, so their strict towers differ. `tower_strict.py` prints both point sets and this determinant calculation. For the smaller fields q=2,3 the ordinary Frobenius discriminants are −7,−8,−11, all of class number one. Thus this is minimal in field size (and N=3 is the first possible strict separating level in characteristic two).

For ordinary elliptic curves over a fixed finite field the sharp hierarchy is:

| datum and equivalence | exactly what survives, within this setting |
|---|---|
| counts / Frobenius polynomial | isogeny class |
| full abstract Frobenius torsion module | isogeny class and O |
| compatible Weil and Tate pairings allowing one compatible arbitrary cyclotomic multiplier | the same pair (isogeny class,O) |
| compatible strict Weil and Tate pairings | additionally the genus torsor Pic(O)/Pic(O)² |
| integral (L,M), or a topological syndrome torus with M | the actual ideal class / Deligne module |

The last row follows because H_1((L⊗R)/L,Z)=L, and the induced map on H_1 is M. An isomorphism of topological group tori intertwining the steps induces an integral intertwiner, not merely a profinite one. Conversely an integral intertwiner induces a torus isomorphism. The density of torsion does not repair the lost information if the torsion data are given only as an abstract discrete group: a compatible profinite map need not extend to a continuous map of the real tori. Remembering the actual nested sublattices inside a common integral lattice likewise retains that global lattice; forgetting to finite quotients is a different operation.

For the **finite quotients** built from (1−M^k)L and the dual stabiliser lattices (1−V^k)L, and for their abstract Heisenberg commutators, the same local distinction applies: arbitrary compatible central automorphisms erase the genus; fixed scalar commutators can retain it. No assertion about a full Hilbert-space realisation, a common embedded real lattice, a quadratic refinement or extra theta data follows merely from T1. The unadorned level-N Bell pairs on the zeta side have no specified common integral Frobenius step, so they do not by themselves provide the Deligne module sought by the ladder. Adding a topology or a global integral marking changes the supplied datum.

Replace the ordinary-elliptic row's lattice entry by:

> H_1 of the canonical lift, an invertible ideal class of its endomorphism order; counts determine its isogeny class, the abstract torsion module determines its order, and the strict polarised torsion tower determines its genus. The remaining ambiguity is a torsor under Pic(O)².

Replace the one-paragraph “the lattice's class is seen by the pairing” by:

> The strict pairing tower can distinguish genera, and distinguishes the two discriminant −24 classes; arbitrary compatible root-of-unity automorphisms erase this distinction. In general it cannot recover the class within a genus.

“The tower is blind to RH” also needs its intended meaning: **the existence of the formal tower does not force RH**. Its full count sequence is not informationally blind: it determines the characteristic polynomial and therefore decides the RH spectral test. The ladder already makes the latter point. An ideal class is unnecessary for deciding that spectral test; every member of a fixed isogeny class has the same zeros.

For zeta this is a precise local/global limitation in the understood finite-field model, largely a restatement of the genus/local-triviality issue already sketched in F and U. The new content here is the compatible-tower formulation, the exact genus theorem and the verified audit. It is **not** a theorem forbidding a future construction of a global H^1 over Q from arithmetic input. Nonuniqueness of an integral lattice is not nonexistence, and supplying one suitable lattice does not require reconstructing a predetermined ideal class. Nor does an elliptic genus theorem automatically classify higher-dimensional polarised modules. The missing “finite-rank integral structure on global H^1 plus a positivity reason” remains a construction problem; neither T1 nor T2 settles it.

## Correction ledger

| item | status and correction |
|---|---|
| Title interpreted as blindness even with strict pairings | **REFUTED**: blindness holds for the similitude tower; the strict tower sees genus. |
| T1's choices of ideal prime to each N | **SHARPENED**: do not assert compatibility from unrelated choices; choose one isogeny per whole primary tower (§1.1). |
| T1's Tate functoriality | **PROVED** with the full rational torsion × rational quotient domain, dual isogeny, one fixed sign, and reduced values (§1.2). |
| T2's “norms of principal ideals” | **SHARPENED** to H_N=Norm((O/NO)^×), the residue norms of locally invertible principal generators. Global units alone give the wrong subgroup. |
| q=7 described as “Q(√−7)-type” | **REFUTED**: D=−24, K=Q(√−6). The q=2 E mode / 441d1 has D=−7. |
| Suggestion that q=7 separation might reflect different orders | **REFUTED**: fundamental discriminant forces the same maximal order. It is a strict genus distinction, case (b). |
| “The Weil pairing sees the class” without a genus qualification | **SHARPENED**: true for the class-number-two examples, false as a general class reconstruction statement. |
| Every fixed-level intertwiner multiplier equals an ideal norm residue | **REFUTED** without extendability; q=128, N=7 is an explicit counterexample. The compatible tower has precisely the norm coset (§2.1). |
| Lane U's Tate sign | **SHARPENED**, not a class bug: its helper uses 1−M^k, the final formula M^k−1. With one global sign correction simultaneous Weil/Tate scales agree. |
| Lane U's Tate well-definedness “iff” | **SHARPENED**: necessity requires rational exact order N; in general use exp(G[N]). The theorem only uses N|q^k−1. |
| CM check “ψ, not its conjugate” | **REFUTED** as an inference from that script. Conjugation is an integral determinant-minus-one intertwiner, and the script stops at its first match. |
| T4 includes syndrome tori under “local or torsion” | **REFUTED** if topology and step are retained: their H_1 recovers the global lattice. Abstract finite quotients are a weaker datum. |
| “Tower is blind to RH” as an information statement | **SHARPENED**: existence of the formal tower does not force RH; its count sequence still determines the spectral test. |
| T1 yields a new no-go theorem for zeta H^1 | **REFUTED** as a deduction: it is nonuniqueness in an elliptic model, not nonexistence or a general classification for zeta. |
| PARI tools/environment in the brief | **PARTIAL execution**: cypari2/gp absent and installation unavailable here; finite-field `ellisomat` was also the wrong suggested API. Exact independent checks are clearly labelled. |

## Numerical checks for the blind lane

**NUMERICAL, exact finite-field arithmetic.** The second example is the complete ordinary trace-12 isogeny class over F_41 with O=Z[√−5]. Since disc Z[π]=−20 is fundamental, all its curves have that order. Exhausting every nonsingular short Weierstrass model produces exactly two F_41-isomorphism classes, as h(O)=2 predicts. Their values on the printed E[8] bases over F_{41^4} are:

| curve | E(F_41) | one Weil value e_8(P,Q) |
|---|---|---|
| y²=x³+x+17, j=40 | Z/30 | 14 |
| y²=x³+3x+11, j=12 | Z/30 | 38 |

Here μ_8 lies in F_41, and the printed root is w=3. The values are w^7 and w^5. The degree-three isogeny has kernel {O,(34,6),(34,35)} on the first curve. Its Vélu quotient is y²=x³+38x+24; the isomorphism to the second curve is (x,y)↦(32x,38y), equivalently u=14. On the image of the source basis its Weil value is **14³ mod 41 = 38**, as checked in the output. The independently printed target basis has the same value. The ideal is (3,π−1)=(3,√−5−1), with π=6+√−5; it is nonprincipal, since x²+5y² cannot equal 3.

For the odd-primary part use instead the degree-two isogeny with kernel {O,(35,0)} and target change u=8. Its ideal is (2,π−1). These two maps give the all-level compatible identification; they are not one degree-one algebraic map. The script prints their target coefficients, point images through basis matrices, and all four reduced Tate entries before and after transport at N=2,3,4,8. It also prints and certifies E(F_{41^k}) for k≤6, identically for both curves. Thus the second pair is blind in the T1 sense but strictly separable: S_4(c)={3}, and S_8(c)={3,7}, whereas H_4={1} and H_8={1,5}.

Reproduce from the repository root (with the supplied `python-flint` and `sympy`):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 notes/astra-2026-10-23/tower/checks/tower_strict.py
PYTHONDONTWRITEBYTECODE=1 python3 notes/astra-2026-10-23/tower/checks/tower_audit.py
PYTHONDONTWRITEBYTECODE=1 python3 notes/astra-2026-10-23/tower/checks/audit_overlap_refinement.py
PYTHONDONTWRITEBYTECODE=1 python3 notes/astra-2026-10-23/tower/checks/replay_tower_flint.py
PYTHONDONTWRITEBYTECODE=1 python3 notes/astra-2026-10-23/tower/checks/replay_cm_flint.py
```

The saved outputs are respectively `output_strict.txt`, `output_audit.txt`, `output_overlap_refinement.txt`, `output_tower_flint.txt`, `output_cm_flint.txt` in `checks/`. The main audit proves the mixed-primary map is a bijection and commutes with Frobenius **pointwise** on all 2400 points over F_{7^4} and all 1620 points over F_{41^2}. Additivity follows from the isogeny construction and is also checked on a deterministic sample. Actual coordinates and field moduli make every pairing value reproducible; random basis changes do not enter any classification verdict. No numerical root of a number-field L-function was used.

For the outstanding requested PARI run, activate an environment containing cypari2 and run the same `tower_audit.py`, then `checks/rerun_legacy.py`. The latter has no replacement mathematical assertions: it runs the original F/U/CM Python files and evaluates their unchanged GP payloads through cypari2. Full F Riemann–Roch statistics and the PARI-specific backend remain unverified in this session; see §3.4 and `progress.txt`.

## What this changes in the notebook

**No notebook file outside this lane was edited and no claim was registered.** The proposed annotations are concrete:

* `overlap-data.md`, Findings, §3 items 3–4, §4 closing paragraph: retain the proved q=7 result; state “strict polarised torsion sees genus, with equality to class for D=−24.” The unrestricted pairing-tower variant forgets that genus. Its unpolarised order theorem stands.
* `tower-pairing.md`, Findings, §4 “How far this reaches”, Conclusion 4 and 7: replace the genus sketch/open question by the theorem of §2, and explicitly distinguish arbitrary-unit consistency from fixed-centre / inversion-only code equivalence. The N=8 separation stands. State the Tate sign convention once, qualify the well-definedness converse, and remove “not its conjugate” from §7's CM-check report.
* `data-ladder.md`, answer paragraph, §0 ordinary-elliptic lattice cell, §1 items 2–3 and §2's first two bullets: use the replacement sentences in §4 here. Counts still determine the isogeny class and decide the spectral test. Strict local data can see a genus; the full global lattice is finer in general. Do not call a topological torus with its step merely torsion data.
* `HANDOFF.md`, session 2026-10-06 Findings (F): change “the Weil pairing sees the class” to “the strict pairing tower sees genus; it separates the D=−24 pair.” In Next (iii), record that the 42 comparisons and separation now have an independent exact FLINT replay and proofs with explicit scope, while the specified PARI rerun and cross-prime ε normalisation remain outstanding. This is an authored audit, not a substitute for the notebook's separate REFUTE promotion process.
* `lattice-tower.md`, §8's lane-U addendum: qualify class by genus for finite quotients with fixed commutators. Its actual topological syndrome torus still recovers L through H_1. In §4/§7 “blind” means that formal tower existence does not enforce RH.

**Draft shards are affected by wording, not by a refutation of their q=7 arithmetic.** In `notes/adelic-gkp/shard-draft/claims-rows.tsv`, `prop:gkp-overlaps-see-order` retains both its order theorem and its two specific separation assertions; change its general parenthetical to “strict genus; class here because h=2.” In `04za_adelic_gkp_ladder.tex`, make the same change in the SHARD-SUMMARY and the proposition title around line 125. `obs:gkp-missing-datum` needs the scope qualification: the formal tower alone does not force positivity, and nonuniqueness of an integral class is not a universal impossibility of constructing a global H^1. `num:gkp-counts-not-lattice` remains valid. There is no lane-U theorem row in that draft to delete. The registered `cit:latimer-macduffee`, `cit:lenstra-structure` and their count/module consequences remain intact.

Candidate rows, for later independent REFUTE review, not immediate registration (the `sketched` proposals below refer to the registry gate; the local proof statuses are PROVED):

| candidate id | kind / proposed registry status | precise statement | evidence |
|---|---|---|---|
| `thm:ordinary-torsion-similitude-order` | theorem / sketched | For ordinary curves over a fixed F_q, the compatible Frobenius/Weil/reduced-Tate tower modulo one compatible cyclotomic automorphism determines exactly the isogeny class and End(E). | §1; dependencies `cit:latimer-macduffee`, `cit:lenstra-structure`, Tate endomorphism theorem and Kummer naturality |
| `thm:ordinary-strict-tower-genus` | theorem / sketched | Within one ordinary isogeny class and order O, strict tower isomorphism holds exactly when the relative invertible ideal class lies in Pic(O)²; S_N(c)=Norm(A)Norm((O/NO)^×). | §2, including the nonmaximal-order proof and the isolated-level caveat |
| `num:q7-strict-tower-audit` | numerical / numerical | The common maximal order is D=−24; equivariant E_4[8]→E_5[8] pairing multipliers are {3,5}; U's 42 comparisons and 22 assertions reproduce with exact independent finite-field arithmetic. | `output_overlap_refinement.txt`, `output_tower_flint.txt`; backend FLINT |
| `num:q41-same-order-tower` | numerical / numerical | The two trace-12 curves with j=40,12 over F_41 have common maximal order D=−20, identical certified groups through k=6, and compatible primary tower maps from the explicit 2/3-isogenies, obeying both pairing functorialities. | `output_audit.txt`; backend FLINT, PARI validation pending |
| `prop:torsion-topology-retains-integral-class` | proposition / sketched | Abstract compatible torsion data need not recover the integral ideal class; a topological group-torus isomorphism intertwining M does recover it through H_1. | §4; elementary homology argument |

**Next:** rerun the supplied PARI branches in an environment with cypari2, then seek the independent REFUTE review of the proof (especially the genus reduction and the distinction among the three equivalence relations). The ε-uniform CM comparison across different reduction primes remains open here. The theorem/audit should not be used to promote either a blanket “pairings never see classes” claim or a new zeta no-go claim.
