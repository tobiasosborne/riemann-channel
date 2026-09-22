# The class-group bond at genus two

Author: `codex:gpt-6-astra`

| Claim | Verdict | Statement |
|---|---|---|
| E1 | PROVED | Counts (3,31,117,619), Pic⁰=Z/15, all special classes and P(T). |
| E2 | SHARPENED | All 14 L-factors and the genus-16 cover; Fourier labels, not an isomorphism of Hilbert spaces. |
| E3 | SHARPENED | Direct-Frobenius channel exists; two real weights on H¹(C), with convention and multiplicity corrections. |
| E4 | OPEN | The bond-to-H¹ normalization is absent; explicit CM reference weights and a rational-marking obstruction are PROVED. |
| E5 | REFUTED | Literal cut is infinite or nilpotent; the scalar-inner replacement has a non-Frobenius-normal Gram. |
| E6 | SHARPENED | The constant-term identity is proved; a geometric fold and genus-two H-CLASS remain OPEN. |

## Progress

E1–E6 completed. E4 and the geometric part of E6 retain the explicitly stated OPEN identifications.

## E1 — PROVED: the finite class-group bond

### E1.1. Curve, points and numerator

Put `P_0 = infinity`, `P_+ = (1,1)`, `P_- = (1,4)`. All polynomial entries below in Mumford coordinates are in `F_5`. The polynomial `f=x^5+x^3+x^2-2` is squarefree (`gcd(f,f')=1`). Its odd degree gives one ramified, rational point over infinity on the smooth hyperelliptic model, genus two, and `div(dx/y)=2P_0`. Thus `K_C~2P_0`.

The standalone check `checks/finite_data.py` enumerates squares in the following fields; the coefficient lists are low to high:

| k | irreducible modulus | affine points | N_k including infinity |
|---|---|---:|---:|
| 1 | t | 2 | 3 |
| 2 | t²+t+1 | 30 | 31 |
| 3 | t³+t²+1 | 116 | 117 |
| 4 | t⁴+t³+t²+1 | 618 | 619 |

**PROVED.** Newton's identities applied to `s_k=5^k+1-N_k=(3,-5,9,7)` give

`P(T)=1-3T+7T²-15T³+25T⁴`,

`f_F(z)=z⁴-3z³+7z²-15z+25`, `h=P(1)=15`.

This confirms `report/sections/06f_ring_norm_genus_two.tex:124–128`, which quotes “counts `3,31,117,619`”. Define

`b_1=(3+sqrt(21))/2`, `b_2=(3-sqrt(21))/2`,

`d_j=sqrt(20-b_j²)>0`, `alpha_{j,±}=(b_j±i d_j)/2`.

Then `f_F(z)=(z²-b_1 z+5)(z²-b_2 z+5)`. Both `b_j²<20`, so all four roots are distinct and have modulus exactly `sqrt(5)`. Their positive-imaginary representatives are

`alpha_{1,+}=1.895643923739+1.185973909659i`,

`alpha_{2,+}=-0.395643923739+2.200787560308i`.

This is an exact algebraic verification of the circle, stronger than a numerical check and independent of `asm:weil-curves`. The zeros of `P` are `alpha_{j,±}^{-1}`; zeros and reciprocal roots must not be interchanged.

### E1.2. All fifteen classes and their special degrees

**PROVED.** `G=[P_+-P_0]` generates `A=Pic^0(C)(F_5)=Z/15Z`. Equivalently `A=Z/3Z × Z/5Z`; those are not different candidates. Identify `Pic^n(F_5)` with `A` by `D↦[D-nP_0]`. In the table, `(u,v)` represents the reduced class of the zeros of `(u,y-v)` minus `deg(u)P_0`. The three `h^0` columns refer to the classes `kG+nP_0`.

| k | u | v | h⁰, n=0 | h⁰, n=1 | h⁰, n=2 |
|---:|---|---|---:|---:|---:|
| 0 | 1 | 0 | 1 | 1 | 2 |
| 1 | x−1 | 1 | 0 | 1 | 1 |
| 2 | x²−2x+1 | 1 | 0 | 0 | 1 |
| 3 | x²−x+1 | 2x−1 | 0 | 0 | 1 |
| 4 | x²+2x−2 | 1−2x | 0 | 0 | 1 |
| 5 | x²+2 | 2−2x | 0 | 0 | 1 |
| 6 | x²+2x−1 | x+2 | 0 | 0 | 1 |
| 7 | x²−2x−1 | −2x−2 | 0 | 0 | 1 |
| 8 | x²−2x−1 | 2x+2 | 0 | 0 | 1 |
| 9 | x²+2x−1 | −x−2 | 0 | 0 | 1 |
| 10 | x²+2 | 2x−2 | 0 | 0 | 1 |
| 11 | x²+2x−2 | 2x−1 | 0 | 0 | 1 |
| 12 | x²−x+1 | 1−2x | 0 | 0 | 1 |
| 13 | x²−2x+1 | −1 | 0 | 0 | 1 |
| 14 | x−1 | −1 | 0 | 1 | 1 |

1. The script enumerates **every** monic `u` of degree at most two and every `v` of smaller degree satisfying `u | f-v²`. There are exactly the fifteen rows. The reduced-divisor theorem for an odd hyperelliptic model identifies these with the rational Jacobian classes.
2. Addition can be audited without a black-box Jacobian package: choose `a u_1+b u_2=d_1`, then `c d_1+d(v_1+v_2)=e`, using monic gcds. Set `u=u_1u_2/e²` and `v=(ca u_1v_2+cb u_2v_1+d(v_1v_2+f))/e mod u`. Repeatedly replace `(u,v)` by `(monic((f-v²)/u),-v mod u_new)` until `deg u≤2`. These are cancellation of hyperelliptic pairs and the principal divisor of `y-v`. The script checks all 225 additions against addition modulo 15; in particular `15G=0`, and no earlier positive multiple is zero.
3. In degree zero, only the trivial class is effective. A degree-one class is effective exactly when represented by a rational point, hence the theta set is `{0,1,14}` and each has `h^0=1` (a moving degree-one system would make the curve rational). Riemann–Roch in degree two says `h^0(D)=1+h^0(K_C-D)`: the canonical class `0` has dimension two and each other class dimension one. All fifteen classes are effective. Representatives in degree two are the displayed degree-two reduced divisors, `P_++P_0`, `P_-+P_0`, and `2P_0`.

The principal degree-two class has six effective representatives: `2P_0` and the five fibres of `x` over `F_5`. There are six unordered pairs of rational points and `(N_2-N_1)/2=14` closed degree-two points, hence twenty effective degree-two divisors in total, independently checking the class sum.

### E1.3. The sequence

**PROVED.** The per-class formula gives `a_0=1`, `a_1=3`, `a_2=6+14=20`; for `n≥3`, every class has `h^0=n−1` and

`a_n=15(5^{n−1}−1)/4`.

Consequently `a_n=(1,3,20,90,465,2340,11715,58590,…)`. Multiplication of this series by `1−6T+5T²` gives precisely `P(T)` (coefficients in degrees three and four are `−15,25`, then zero). This supplies the exact instance of `prop:class-group-bond`, `report/sections/04p_gl1_bond.tex:36–47`; its formula is “`a_n = sum_{[D]} (q^{h^0(D)}−1)/(q−1)`”. The predecessor gives its elementary counting proof at `notes/gl1-bond/proofs.md:18–30`. The finite-field and divisor-enumeration approach was read in `scripts/gl1_bond.py:26–71,128–225,718–745`; this round's script is independent and uses genus-two reduced divisors.

## E2 — SHARPENED: all characters and the class-field cohomology

### E2.1. The fourteen polynomials, including their zeros

**PROVED.** Set `ζ=exp(2πi/15)`, and display the entire character group as

`A^ = {χ_k : χ_k(jG)=ζ^{kj}, 0≤k≤14}`,

with `χ_k(P_0)=1`; `χ_0=1`, `bar χ_k=χ_{15−k}`. Let `A_k=1+ζ^k+ζ^{−k}`. The complete answer is `L_k(T)=1+A_k T+5T²` for each nonzero k. The table spells out every character and polynomial. Its two numerical zeros are rounded, while the formula

`ρ_{k,±}=(-A_k ± i sqrt(20−A_k²))/10`

specifies both zeros exactly in every row.

| k | order χ_k | L(T,χ_k) | zeros ρ_{k,+}, ρ_{k,−} |
|---:|---:|---|---|
| 1 | 15 | 1+(1+ζ+ζ¹⁴)T+5T² | −0.282709092 ± 0.34651922i |
| 2 | 15 | 1+(1+ζ²+ζ¹³)T+5T² | −0.233826121 ± 0.38121561i |
| 3 | 5 | 1+((1+√5)/2)T+5T² | −0.161803399 ± 0.41691685i |
| 4 | 15 | 1+(1+ζ⁴+ζ¹¹)T+5T² | −0.079094307 ± 0.44016371i |
| 5 | 3 | 1+5T² | 0 ± 0.447213595i |
| 6 | 5 | 1+((1−√5)/2)T+5T² | 0.061803399 ± 0.44292250i |
| 7 | 15 | 1+(1+ζ⁷+ζ⁸)T+5T² | 0.095629520 ± 0.43686954i |
| 8 | 15 | 1+(1+ζ⁸+ζ⁷)T+5T² | 0.095629520 ± 0.43686954i |
| 9 | 5 | 1+((1−√5)/2)T+5T² | 0.061803399 ± 0.44292250i |
| 10 | 3 | 1+5T² | 0 ± 0.447213595i |
| 11 | 15 | 1+(1+ζ¹¹+ζ⁴)T+5T² | −0.079094307 ± 0.44016371i |
| 12 | 5 | 1+((1+√5)/2)T+5T² | −0.161803399 ± 0.41691685i |
| 13 | 15 | 1+(1+ζ¹³+ζ²)T+5T² | −0.233826121 ± 0.38121561i |
| 14 | 15 | 1+(1+ζ¹⁴+ζ)T+5T² | −0.282709092 ± 0.34651922i |

**Proof.** E1 gives degree-zero coefficient 1, degree-one coefficient `χ_k(0)+χ_k(G)+χ_k(−G)=A_k`, and degree-two coefficient `6χ_k(0)+Σ_{j≠0}χ_k(jG)=5`. All later coefficients vanish because Riemann–Roch makes their class weights constant and `Σ_jχ_k(jG)=0`. Since `−1≤A_k≤3`, we have `A_k²≤9<20`, proving distinct zeros and `|ρ_{k,±}|=1/√5` exactly, without invoking a general RH assumption. The reciprocal Frobenius values are `λ_{k,±}=(-A_k±i sqrt(20−A_k²))/2`; reciprocal inverts the sign label. Every pair `{χ_k,χ_{15−k}}` has the same polynomial, which happens here because the theta set is inversion invariant.

### E2.2. The precise theorem, functional equation and signs

**PROVED (with the standard external inputs explicitly recorded below).** Let `X/F_q` be smooth, projective and geometrically connected, with rational point `O` and genus `g≥1`. Let `A=Pic^0(X)(F_q)`, `h=|A|`, and extend each finite character of A by `χ(O)=1`. The maximal abelian extension of `F_q(X)` unramified at every place and in which O splits completely is a finite **geometric** extension, the function field of a connected finite étale cover `p:Y→X`, with deck group A and degree h. Its genus is `1+h(g−1)`. For a nontrivial χ,

`L_X(T,χ)=Σ_{n≥0}Σ_{c∈Pic^n(F_q)} χ(c−nO)(q^{h^0(c)}−1)/(q−1) T^n`

is of degree `2g−2`, constant coefficient 1, and leading coefficient `q^{g−1}χ(κ)`, where `κ=[K_X−(2g−2)O]`. Its functional equation in these conventions is

`L_X(T,χ)=χ(κ) q^{g−1} T^{2g−2} L_X(1/(qT),χ^{-1})`.

Thus the “χ-dependent constant” is exactly `χ(κ)`, with **no extra minus sign**. Here `κ=0`, so all fourteen equations are `L_k(T)=5T²L_{15−k}(1/(5T))`.

1. **Reciprocity and constants.** The relevant idele quotient is `Pic(X)/Z[O]≅A`: local units impose unramifiedness and the degree-one Frobenius imposes complete splitting at O. A nontrivial constant-field extension cannot split a degree-one point; hence Y is geometric. Riemann–Hurwitz has no different term for this étale cover, giving `2g_Y−2=h(2g−2)`.
2. **Polynomial and functional equation, directly.** For χ nontrivial the class sum of constants is zero. Riemann–Roch and `D↦K_X−D` give, writing B_n for the coefficient, `B_n(χ)=q^{n+1−g}χ(κ) B_{2g−2−n}(χ^{-1})`. Coefficients of negative degrees vanish; those of degree greater than `2g−2` vanish by the same constant-class argument. `B_0=1` proves the leading coefficient and functional equation.
3. **Cohomology.** Choose `ℓ≠char F_q` and a coefficient field containing all values of the characters. Write `ℒ_χ` for the rank-one summand of `p_* Q̄_ℓ` whose **geometric** Frobenius at a closed point Q has eigenvalue `χ([Q−deg(Q)O])`. This fixes the character labelling independently of whether reciprocity is written with arithmetic or geometric Frobenius; switching that convention interchanges χ and χ⁻¹. Then

   `H¹(Y,Q̄_ℓ)=⊕_{χ∈A^} V_χ`, `V_χ=H¹(X,Q̄_ℓ,ℒ_χ)`,

   `V_1≅H¹(X,Q̄_ℓ)`, `dim V_1=2g`, `dim V_χ=2g−2 (χ≠1)`,

   `det(1−T F|V_χ)=L_X(T,χ) (χ≠1)`.

   Indeed nontrivial geometric rank-one summands have zero H⁰ and H²; the étale Euler characteristic is `2−2g`. The trace formula gives the stated Euler factors. The invariant summand is pullback from X (averaging by 1/h is valid also when ℓ divides h). This is an algebraic decomposition over a characteristic-zero coefficient field, not a canonical analytic complexification of `Q_ℓ`.
4. **Factorisation.** At each place, the character product of local factors is the zeta factor of its full inverse image; hence

   `P_Y(T)=P_X(T) ∏_{χ≠1}L_X(T,χ)`.

For this curve `g_Y=16`, with 4 trivial-character modes and 28 nontrivial modes. An explicit integer polynomial display, in factored form, is

`P_Y(T)=(1−3T+7T²−15T³+25T⁴) (1+5T²)²`

`× (1+T+9T²+5T³+25T⁴)²`

`× (1+5T+25T²+70T³+195T⁴+350T⁵+625T⁶+625T⁷+625T⁸)²`.

The three squared factors are the products over character orders 3, 5 and 15 respectively. This is degree 32 with leading coefficient `5^16`; its first coefficients are `1+9T+95T²+575T³+3585T⁴+…`. In particular `N_1(Y)=15`: infinity splits into 15 rational points and `P_±`, whose classes are generators, do not split. This also checks the sign of the linear coefficient.

### E2.3. What “the bond's H¹” actually says

**SHARPENED.** Fourier transformation of `ℓ²(A)` supplies the **labels** χ; Fourier transformation of its divisor-count sequences supplies the L-functions. The resulting cohomological realization is `H¹(Y)`, with the displayed multiplicities. It is **not** an isomorphism `ℓ²(A)≅H¹(Y)`, nor an identification of the degree shift with F. Their dimensions are 15 and 32, and the full degree bond is infinite dimensional. In particular no cohomological eigenvectors, map of inner-product spaces or Hodge normalization follow from the factorisation alone.

A correction to the predecessor is needed: `notes/gl1-bond/proofs.md:99–101` says a single L-function is “the numerator ... divided by that of C”. For a cyclic cover the quotient is the **product over all its nontrivial characters**, not generally a single L-factor. The proof here uses the individual rank-one summands.

### E2.4. External inputs and byte sources

**PROVED — source audit.** Sources are present, contrary to the brief's possible fallback:

- Oliver Lorscheid, *Toroidal automorphic forms for function fields* (2010 preprint), `refs/src/1012.3223/main.tex:318–332` states reciprocity and the product of L-series; lines `1235–1244` state “a finite abelian unramified extension ... of order h”, its zeta factorisation and `g_{F'}=(g−1)h+1`.
- Sergey Neshveyev and Simen Rustad, *Bost–Connes systems associated with function fields* (2011 preprint), `refs/src/1112.5826/main.tex:534`: “The Galois group of H/K is Pic(O)”; the same line specifies the maximal abelian extension unramified at finite primes and split at infinity.
- Artin reciprocity in the pointed, everywhere-unramified form used in step 1 (Emil Artin, 1927; function-field exposition Michael Rosen, 2002) is stated precisely there but its original proof is **not byte-cited**. No class-field construction by explicit equations is claimed.
- Riemann–Roch (Bernhard Riemann, 1857; Gustav Roch, 1865), **not byte-cited**: `h⁰(D)−h⁰(K−D)=deg D+1−g`, `deg K=2g−2`. Riemann–Hurwitz (Adolf Hurwitz, 1891), **not byte-cited**: an étale degree-h map satisfies `2g_Y−2=h(2g_X−2)`.
- The rank-one étale Euler characteristic and trace formula (Alexander Grothendieck, 1965), **not byte-cited**: for a finite-monodromy rank-one lisse sheaf on a projective smooth curve, unramified everywhere, `χ_et=2−2g`, and its Euler product equals the alternating cohomological determinants. These give step 3, not a metric comparison.
- Weil's curve theorem (André Weil, 1948), **not byte-cited** in its original source: every reciprocal root of the numerator of a smooth projective geometrically connected curve over `F_q` has complex absolute value `√q`; therefore so do the reciprocal roots of these factors for its geometric unramified abelian covers. This theorem explains the general statement; E1–E2 verify every modulus in this example algebraically and do not assume it.
- The unique reduced-divisor description used in E1 is the odd hyperelliptic case of David Mumford, *Tata Lectures on Theta II* (1984), and its arithmetic is David Cantor (1987), **not byte-cited**. Its precise form here is the bijection between degree-zero classes and reduced `(u,v)` with `u` monic, `deg v<deg u≤2`, `u|f−v²`; the cancellation algorithm and exhaustive table are supplied above.

## E3 — SHARPENED: the block channel and its metric cone

### E3.1. Two channel conventions

**PROVED.** Choose a complex realization of the Frobenius module of E2 (or work first over algebraic numbers with a chosen embedding into C). On its 32-dimensional space set

`U=F/√5 = diag((alpha_{j,±}/√5)_{j=1,2}, (λ_{k,±}/√5)_{k=1,…,14})`,

`r=5^(−1/4)`, `Z'=rU`, `J'=sqrt(1−1/√5) I_32`.

These display every block: one 4×4 block and fourteen 2×2 blocks; the eigenvalues are exactly those in E1 and E2. In a chosen invariant positive metric U is unitary. For any density Ω the renewal channel is

`E(X)=5^(−1/2) U X U* +(1−5^(−1/2)) Tr(X) Ω`.

On traceless matrices it is `5^(−1/2) Ad(U)`, so all relaxation eigenvalues have modulus `5^(−1/2)`. Each modal characteristic factor is `(z−rμ)/(1−r bar μ z)`, `μ` an eigenvalue of U. These are immediate applications of the general theorem in `report/sections/04o_graded_toys_exits.tex:127–134`, which starts “Let U be unitary ... Z'=rU”.

**SHARPENED.** That construction is a valid **new direct-Frobenius model**. It is not the cited D2 cavity normalization: line 133 instead says `U²≃(F/√q)⊗1_2`. To reproduce that convention here one needs 64 modes with `μ=±sqrt(α/√5)` for every one of the 32 reciprocal roots α; it gives eight trivial-character modes and four per nontrivial character. This agrees with the prediction at `report/sections/04l_elliptic_cavity_channel.tex:233–238`. The eigenvalues of the direct model are `r α/√5`; neither α nor a zero of P itself is a contraction eigenvalue in that convention.

A finite-dimensional operator is unitary in some positive metric **iff it is semisimple and all eigenvalues have modulus one**. Necessity follows by similarity to a unitary, sufficiency by transporting the standard metric from an eigenbasis. A Jordan block is a counterexample to dropping semisimplicity. Here each character block has distinct roots, so the stated modulus test suffices block by block; the direct sum is semisimple despite repeated roots in inverse-character blocks.

### E3.2. The trivial character: the non-vacuous cone

**PROVED.** Fix eigenvectors `(e_{1,+},e_{1,−},e_{2,+},e_{2,−})` and an antilinear involution `c` with `c e_{j,+}=e_{j,−}`. If `D=diag(alpha_{j,±}/√5)`, then

`(D* H D−H)_{ab}=(bar μ_a μ_b−1) H_ab`.

Distinctness and unit modulus make the multiplier zero precisely on the diagonal. Thus all invariant positive metrics are

`H=diag(h_{1,+},h_{1,−},h_{2,+},h_{2,−})`, `h>0`.

The reality requirement is the **additional** condition `H(cx,cy)=overline(H(x,y))`, not a consequence of merely being Hermitian. It forces

`H=diag(h_1,h_1,h_2,h_2)`, `h_1,h_2>0`.

There are two positive parameters and one ratio modulo scale. Equivalently `Z'^* H Z'=r²H`. This extends the calculation, but not the transitive parity symmetry, of `thm:arithmetic-metric`, `report/sections/04l_elliptic_cavity_channel.tex:160–175`: the D2 “single ray” is explicitly on its normalized cavity vectors e_i at line 164. There is no genus-two symmetry there that exchanges j=1 and j=2.

**SHARPENED (meaning of real).** A `Q_ℓ`-vector space has no distinguished complex conjugation and no natural tensor product with C over `Q_ℓ` without an embedding choice. “F is real on H¹(C,Q_ℓ)” is therefore not the reason for the condition above. On the polarized characteristic-zero lift, `H¹(J~,R)⊗C` has its usual coefficient conjugation and the lifted endomorphism commutes with it. Alternatively define a real spectral module with the displayed conjugate pairs. This supplies the involution c; it is not an antiholomorphic involution of the complex variety, and no real model of that variety is assumed.

### E3.3. Nontrivial characters and repeated eigenvalues

**PROVED.** Complex conjugation on a real realization of the **joint** deck/Frobenius representation sends

`c: V_{χ_k,λ_{k,+}} → V_{χ_{15−k},λ_{k,−}}`,

and interchanges the other two lines. Normalize those vectors by c. The seven inverse pairs are exactly

`(1,14), (2,13), (3,12), (4,11), (5,10), (6,9), (7,8)`.

For metrics that are also **deck-group invariant**, distinct characters are orthogonal by averaging. On each four-dimensional pair, in the order `(k,+),(k,−),(15−k,+),(15−k,−)`, the real metric is

`diag(a_k,b_k,b_k,a_k)`, `a_k,b_k>0`.

There is no intrinsic real structure on an individual nonreal character block inherited from this joint representation; its two weights need not agree merely because its polynomial happens to have real coefficients. Reality relates different character blocks.

**SHARPENED.** F-invariance alone on the full cover does **not** force character blocks to be orthogonal: `L_k=L_{15−k}`, so each common λ-eigenspace can carry any positive 2×2 Hermitian Gram matrix across the two characters. One must require A-invariance, or choose such an invariant metric by averaging, to obtain the diagonal block description. On the direct sum of the seven inverse pairs the real structure conjugates the Gram at λ to the Gram at bar λ. No multiplicity exception affects the four-dimensional trivial block, whose four roots are simple and disjoint from the other factors (Euclidean gcd of P with the three displayed factors is 1).

## E4 — OPEN for the proposed comparison; PROVED obstructions and explicit CM calculations

### E4.1. The field and its order are computable

**PROVED.** Write π for the class of z in `K=Q[z]/(f_F)`, and put

`β=π+5/π`, `δ=π−5/π`.

Then

`β²−3β−3=0`, `F=K^+=Q(√21)`, `√21=2β−3`,

`δ²=3β−17=(-25+3√21)/2`, `K=F(δ)`, `π=(β+δ)/2`.

The two conjugates of δ² are negative, so this is a quartic CM field. The quartic is irreducible modulo 2 (`z⁴+z³+z²+z+1`), hence irreducible over Q. The Jacobian is simple, and it is ordinary since its middle coefficient 7 is prime to 5 (the ordinary criterion is byte-stated at `refs/src/1701.07742/main.tex:551–555`). Under the two lift assumptions named in the brief, its rational endomorphism field is K.

There is no unresolved maximal-order question here:

`O_F=Z[β]`, `O_K=Z[β,π]=Z[π,5/π]`,

with integral basis `B=(1,β,π,βπ)`, `disc K=21²·109=48069`,

`disc Z[π]=1201725=25 disc K`, `[O_K:Z[π]]=5`.

To prove maximality, the relative discriminant of `O_F[π]` is `(β²−20)=(3β−17)`, an ideal of norm 109, hence squarefree; a larger order's index ideal would have its square dividing this ideal, which is impossible. The base order is maximal because its discriminant is 21. Independently, the exact trace matrix on B is

```
[ 4   6   3  15 ]
[ 6  30  15  54 ]
[ 3  15  -5  24 ]
[15  54  24  57 ]
```

and its determinant is 48069. As both Frobenius and Verschiebung are integral endomorphisms, the endomorphism order already contains `O_K`, so equals it in the assumed commutative endomorphism field. Maximality matters for the ideal description, not for the eigenvalue or metric-cone proofs.

K has **no imaginary quadratic subfield**. If it contained `Q(√−d)`, then `K=F(√−d)` and `δ²=−d a²` for `a∈F`; its norm to Q would be a rational square, whereas `N_{F/Q}(δ²)=109`. In particular K is not biquadratic. It is not normal either: the conjugate δ would require the real element `√109` in K, hence in F, which it is not.

### E4.2. What the polarization formula actually determines

**PROVED, conditional on `asm:cm-hodge-type` and `asm:cm-polarised-lift`.** After a **chosen rational K-module marking**, the homology lattice of the lift is a fractional `O_K` ideal I. Its principal Riemann form has the form

`E(x,y)=Tr_{K/Q}(ξ x bar y)`, `bar ξ=−ξ`,

`ξ I bar I = D_K^(−1)`.

The ideal equation is exactly unimodularity: the E-dual lattice is `ξ^(−1) bar I^t`, where `I^t=D_K^(−1) I^(−1)`. Choose the CM type Φ so `Im φ_j(ξ)>0`; then on `K⊗R≅C²` the positive real metric `E(x,Jy)` is

`2 Σ_{j=1}² Im φ_j(ξ) Re(x_j bar y_j)`.

Thus the complexified **homology** metric, or a cohomology basis transported isometrically by the principal polarization and relabelled on conjugates, has diagonal weights

`(c_1,c_2,c_1,c_2)`, `c_j=|φ_j(ξ)|`,

up to a common factor. In this paragraph the order is `(φ_1,φ_2,bar φ_1,bar φ_2)`, unlike E3's adjacent-pair order. Orthogonality also follows directly from E3. Rosati is complex conjugation, and `π bar π=5` gives unitarity in this metric.

**SHARPENED: dual-basis warning.** If instead `H^{1,0}` is written in the period coordinate forms `dz_j` dual to the uniformizing lattice coordinates, its Hodge weights are proportional to `1/|φ_j(ξ)|`. These are dual norms. The brief's formula for **H¹** is correct only after specifying the polarization-transported basis, not for every meaning of “eigenvectors normalized by the lattice”. A lattice supplies a rational structure and an integral lattice, not a preferred generator of every complex eigenline.

The trace description of Riemann forms is the standard CM theorem (Shimura–Taniyama, 1961; J. S. Milne, 2020, Proposition 2.9), **not byte-cited from an original source in this repository**: forms compatible with CM conjugation are `Tr(ξ x bar y)` with ξ purely imaginary, and positivity is the indicated sign condition. The displayed metric follows by expanding the trace at the two places. See [Milne, Complex Multiplication, Proposition 2.9](https://www.jmilne.org/math/CourseNotes/CM.pdf). The notebook already explicitly limits its equivalence to “up to positive weights and the CM type”, `report/sections/06f_ring_norm_genus_two.tex:227–239`; the predecessor is equally explicit about a “module generator and positive metric weights” at `notes/ring-norm-tensor/astra-proofs.md:1011–1039`. Neither asserts an equality of normalized metrics.

### E4.3. A complete algebraic reference normalization and two exact ratios

**PROVED (reference model; not identified with the curve's marked lift).** The polynomial itself canonically defines the Frobenius algebra `K=Q[z]/(f_F)` with distinguished cyclic vector 1. Its complex eigenbasis is the spectral-idempotent basis

`e_α = f_F(z)/((z−α)f_F'(α)) ∈ K⊗C`, `α∈{alpha_{1,±},alpha_{2,±}}`.

Evaluation at the four roots identifies e_α with the four coordinate vectors. This is a useful algebraic normalization **constructed from** the polynomial extracted from the bond; it is not a map from a theta vector to geometric H¹. In the power basis `(1,π,π²,π³)`, multiplication by π is explicitly

```
F = [0 0 0 -25]
    [1 0 0  15]
    [0 1 0  -7]
    [0 0 1   3].
```

A fully specified principally polarized CM reference lattice is

`I_0=O_K`, `ξ_0=1/((2β−3)(2π−β))=1/(√21 δ)`.

The different is generated by `√21 δ`, so its inverse generates the codifferent. An independent exact check gives, in basis B,

```
E_0 = [0 0  0 -1]
      [0 0 -1 -3]
      [0 1  0  0]
      [1 3  0  0],       det E_0=1.
```

Choose `Φ_0={alpha_{1,−},alpha_{2,+}}` so both imaginary parts of ξ_0 are positive. The transported metric weights in the idempotent coordinates are

`c_1^0=1/(√21 d_1)=0.091999448073339…`,

`c_2^0=1/(√21 d_2)=0.049577227300714…`.

Its ratio is

`R_0 = d_2/d_1 = (25+3√21)/(2√109) = 1.85567957472308…`,

`R_0²=(407+75√21)/218`.

In the dual period-form normalization the weights are `√21 d_1, √21 d_2` up to scale and their ratio is

`R_0^(−1)=(25−3√21)/(2√109)=0.538886138329796…`.

These two explicit answers are **different coordinate conventions for the reference model**, not two asserted candidates for the canonical lift of J. The weights measure the Riemann form relative to the algebra's chosen generator. The ratio need not belong to K: here it lies in the real biquadratic field `Q(√21,√109)`, whereas its square lies in `K^+=Q(√21)`. Requiring the unsquared ratio to lie in K or K⁺ is another incorrect premise in the brief. The script `checks/cm_metric.py` verifies the field identities, trace discriminant, alternating integral unimodular E_0 and numerical weights exactly or to the printed precision.

**PROVED (stronger obstruction in this normalization).** For **any** nonzero purely imaginary ξ in K, write `ξ=aδ`, `a∈F^×`. Its transported ratio is exactly `R(ξ)=|σ_1(a)/σ_2(a)| d_1/d_2`, with σ_j the two real embeddings; its square belongs to F. Equality `|φ_1ξ|=|φ_2ξ|` would say that the two real conjugates of ξ² agree. Then `ξ²∈Q_<0`, producing an imaginary quadratic subfield, which E4.1 excludes. Thus in a rational K-module idempotent normalization the Hodge weights can **never** both be equal for this K, irrespective of the unknown ideal class or CM type. This is a negative test for that expressly declared algebraic normalization, not a comparison with D2's unrelated cavity vectors.

### E4.4. The canonical theta normalization can be computed, but does not normalize H¹

**PROVED.** On the class basis `|j,n>` put

`v_{k,n}=15^(−1/2) Σ_{j=0}^{14} ζ^{−kj}|j,n>`.

This is a canonical unitary Fourier normalization up to character phase. With `θ_n(j)=5^{h⁰(jG+nP_0)}`, its special-degree Fourier components are exactly

| k | coefficient at n=0 | at n=1 | at n=2 |
|---|---|---|---|
| 0 | 19/√15 | 27/√15 | 95/√15 |
| 1,…,14 | 4/√15 | 4A_k/√15 | 20/√15 |

Their squared norms across degrees 0,1,2 are `2023/3` for k=0 and `16(26+A_k²)/15` for k≠0; the total is 1101. For the effective-divisor state `(θ−1)/4`, the corresponding degree polynomials are `15^(−1/2)(1+3T+20T²)` and `15^(−1/2)L_k(T)`. These are computed from E1, not assumed theta-period identities.

This computes the requested **canonical normalization on the bond itself**. It gives one vector of length three per character. It gives no components along the four α-eigenvectors in geometric H¹, because there is no specified linear map between these spaces, and the degree shift is not Frobenius (E5 proves the obstruction). The whole `Ω_θ` is not an ℓ² vector: it is constant nonzero towards negative degrees and grows exponentially towards positive degrees. Only an expressly truncated or regularized state can be normalized there.

The proposed L-value alternative has the same problem. Here the complete list is `L_k(1)=6+A_k`, `L_k(5^(−1/2))=2+A_k/√5` for k=1,…,14, with every A_k listed in E2. These nonzero scalars can normalize **whole character blocks** but cannot set a relative norm of eigenlines within a block; in particular the four-dimensional trivial block has no subdivision by class characters. Evaluating its numerator at 1 gives only P(1)=15. Selecting residues or cyclic vectors would be additional constructions requiring a stated comparison to geometric H¹.

### E4.5. Why the requested two-candidate resolution is not well posed

**REFUTED.** An ideal class does not eliminate the normalization ambiguity. Even fixing a fractional ideal I and the actual geometric polarization, replace a rational module generator e by `εe`, where

`ε=(5+√21)/2∈O_F^×`, `ε bar ε=ε²`, `N_{F/Q}(ε)=1`.

Both real embeddings of ε are positive and `εI=I`, so the lattice **as a set** is unchanged. The eigenvectors have been multiplied by `φ_j(ε)`, and the transported metric ratio changes by

`R ↦ (φ_1(ε)/φ_2(ε))² R = ε_1⁴ R = ((527+115√21)/2) R`.

Every integral power gives another allowed lattice marking. This is a coordinate change of the same polarized object (the matrix of E changes with the basis), not an automorphism claimed to preserve its polarization matrix. Hence there are infinitely many presentations even before allowing arbitrary real rescaling. There are not intrinsically “two candidate answers” to select by an ideal-class computation. In a Hodge orthonormal eigenbasis the answer 1 can always be imposed, which would be tautological.

**OPEN — precisely what remains.** To compare to a specific independent symmetric ray one must first supply a map, or a normalization rule on geometric H¹, that is invariantly determined by the bond and compatible with F. Neither the theta coefficients nor the proposed L-values supply that map. Consequently “the symmetric ray of `thm:arithmetic-metric` equals the Hodge metric for this curve” has no specified pair of metrics on one marked space in the brief. It is neither proved nor disproved by R_0. The rational-idempotent version just stated is well defined once a K-module marking is chosen and is refuted for every such marking.

If a marked lift is desired for its own sake, the finite arithmetic task is explicit: enumerate ideal classes of `O_K` (Minkowski bound `(4!/4⁴)(4/π)²√48069 < 34`), and for each I solve `ξ I bar I=D_K^(−1)`, `bar ξ=−ξ`, with the Φ-sign condition, modulo `(I,ξ)~(aI,ξ/(a bar a))`. Unit computations reduce the principal-polarization possibilities modulo norms; ordinary CM type is selected by a fixed 5-adic embedding. To identify the particular J, compare the resulting **polarized** reductions to the Jacobian of the given curve, e.g. through genus-two invariants and twist/isomorphism tests, not just their common f_F. Finally specify the module generator or period marking. The isogeny polynomial determines an isogeny class, not that last marking. This is the Deligne (1969) ordinary-lattice equivalence with polarization (Howe, 1995), **not byte-cited in the originals**; the lattice equivalence and positivity conditions are byte-stated in `refs/src/1701.07742/main.tex:560–618`. None of this finite enumeration cures the missing bond-to-H¹ comparison. No value for the actual marked ξ of J is asserted here.

## E5 — REFUTED: the degree cut does not realize H¹

### E5.1. The two literal cuts

**PROVED.** The degree shift in the brief is precisely the bilateral unitary

`S|j,n>=|j,n+1>` on `ℓ²(A)⊗ℓ²(Z)`.

Its definition does not involve h⁰, P or θ. The special-degree **deviation** must also specify how negative degrees are treated: “n≤2” is not a finite interval.

1. Keep literally every degree `n≤2`. Orthogonal compression gives `T_-|j,n>=|j,n+1>` for `n<2` and zero for `n=2`. This is a multiplicity-15 backward unilateral shift after writing `m=2−n`. It is an **infinite-dimensional contraction**, a coisometry, with `I−T_-*T_-=I_15⊗|2><2|` of rank 15. Its opposite defect `I−T_-T_-*=0`. There is no finite characteristic determinant; its characteristic function has zero-dimensional target defect space. The cut is not noncontractive: its defect is the failure of the proposed finite-dimensional interpretation.
2. Keep just the meaningful nonnegative special degrees `0,1,2`. Then

   `T_sp=I_15⊗N_3`, `N_3=[[0,0,0],[1,0,0],[0,1,0]]`, `N_3³=0`.

   This is a 45-dimensional contraction, with defect rank 15 at degree two and opposite defect rank 15 at degree zero. In the canonical degree/class basis its Gram matrix is `I_45`. In the canonical Fourier basis it is fifteen copies of `N_3`, again Gram `I_3` per character. All eigenvalues are zero. Its matrix characteristic function is `Θ_sp(z)=z³ I_15`, hence `det Θ_sp(z)=z^45`, while `det(1−T T_sp)=1`. Neither determinant has P as numerator or reciprocal numerator. The trivial character cut is only dimension three and cannot be H¹(C), of dimension four.

The characteristic function assertion can be checked from `Θ_N(z)=−N+z D_{N*}(I−zN*)^(−1)D_N`, restricted between its defect spaces: only the `z³` term carries the degree-two defect vector to degree zero. Calling the exiting degree a “single direction” does not make the exit scalar: there are fifteen independent class amplitudes at that degree.

**REFUTED.** No nonzero nilpotent restriction or quotient of this finite cut can have the nonzero Frobenius spectrum. Nor can a positive Gram matrix make it a positive radius times a unitary: iterating `N* H N=r²H` three times would give `0=r⁶H`. Reweighting a Hilbert norm cannot fix that spectral obstruction.

### E5.2. The theta-cyclic cut, with its exact Gram

**PROVED.** Take the actual special-degree theta vector `θ=Σ_{j,n=0}²θ_n(j)|j,n>`. In the cyclic basis `(θ,T_sp θ,T_sp² θ)`, the operator is N_3 and the inherited Gram matrix is

```
G_theta = [1101 282 195]
          [ 282 126  47]
          [ 195  47  39],       det G_theta=254679.
```

Its exit defect in that basis is

```
G_theta − N_3^t G_theta N_3
       = [975 235 195]
         [235  87  47]
         [195  47  39],        rank=2.
```

Indeed the three outgoing class amplitudes are `(θ_2,θ_1,θ_0)`, with `θ_2=5θ_0` and θ_1 independent of θ_0. Thus even the single vector's cyclic restriction has **two** exit coordinates, not one. These are Jordan-chain Grams; there is no basis of four Frobenius modes on which to form the requested “modal Gram of the bond cut”. If class translations are added before taking the cyclic span, every character has a nonzero degree-zero coefficient, so the generated space is the full 45-dimensional cut. If only χ_0 is retained, its cyclic cut is the whole scalar three-step nilpotent chain, with a scalar exit but the same wrong zero spectrum.

The Perron tail is a statement about the scalar divisor-count generating function, not a subspace whose elimination turns S into F. A scalar rational realization of `Z(T)` has nonzero poles at 1 and 1/5, i.e. nonzero transfer eigenvalues 1 and 5 (finite polynomial terms may require nilpotent delay modes); P is its transmission numerator. It is not a characteristic polynomial of that shift. Without rescaling, the Perron realization containing eigenvalue 5 is not a contraction. The correct literal object is the shift plus the h⁰-dependent observation/state, not a Frobenius dynamics hidden in the orthogonal degree cut.

### E5.3. A correct scalar-exit model built from P, and its non-normal Gram

**PROVED.** There is a useful **different** model built after extracting the polynomial. Let

`B(w)=P(w)/f_F(w)`.

Since `P(w)=w⁴ f_F(1/w)` and its roots lie inside the disk, B is a scalar finite Blaschke product of degree four. Its zeros, ordered for the following matrix, are

`ρ=(alpha_{1,+}/5,alpha_{1,−}/5,alpha_{2,+}/5,alpha_{2,−}/5)`

`=(0.379128785±0.237194782i, −0.079128785±0.440157512i)`.

On `K_B=H²⊖BH²`, let `T_B=P_{K_B} M_w|K_B`. It is a four-dimensional contraction with one exit and characteristic function B up to constant unitaries. The eigenvectors `k_a(w)=B(w)/(w−ρ_a)` can be normalized to exit amplitude 1; then

`G_ab=<k_a,k_b>=1/(1−bar ρ_a ρ_b)`.

This follows either from the Hardy kernel calculation or the defect identity `G−D*GD=11*`, `D=diag(ρ_a)`. It is exactly the identity at `report/sections/04l_elliptic_cavity_channel.tex:48–53`: “`(1−bar z_n z_m)<k_n,k_m>=a_n* a_m`”. The normalized vectors `sqrt(4/5) k_a` have Gram

```
[1                 .843907307−.166330902i  .830882677+.166648649i  .693397159−.090529801i]
[.843907307+.166330902i  1                 .693397159+.090529801i  .830882677−.166648649i]
[.830882677−.166648649i  .693397159−.090529801i  1                 .671386810+.039384026i]
[.693397159+.090529801i  .830882677+.166648649i  .671386810−.039384026i  1                ].
```

All off-diagonal entries are nonzero. Thus this metric lies **outside** the invariant cone of E3. With `F=5T_B` in this spectral realization, the maximum absolute entry of `(F/√5)* G_norm (F/√5)−G_norm` is `1.3238593874…`, not a rounding residual. The exact nonzero off-diagonal formula is the proof.

For the cavity square-root convention one may instead form `B_cav(z)=P(z²)/f_F(z²)`; its degree is eight, its zeros satisfy `z²=ρ_a`, and its normalized modal Gram is `(1−1/√5)/(1−bar z_a z_b)`. The same off-diagonal obstruction remains. For the direct four-mode channel of E3, a scalar Blaschke product at its four chosen eigenvalues likewise has the Cauchy Gram, not a diagonal metric. These constructions use the finite scalar-inner/model-space theorem (Béla Sz.-Nagy and Ciprian Foiaş, 1970), **not byte-cited in the original**, in the precise finite form: a scalar Blaschke product of degree d gives a d-dimensional compressed shift with one-dimensional defects, spectrum its zeros and characteristic function that product. The notebook's `thm:h-exit-model` supplies the specific identity just used.

**PROVED — structural obstruction.** On any d-dimensional invariant-metric channel `Z'=rU`, `0<r<1`, the defect is `(1−r²)I_d`, rank d. A conservative completion with a scalar exit has defect rank at most one. Thus for d=4 these demands are incompatible in **any** scalar-exit realization, not just the degree cut; for the square-root model d=8. This is the same obstruction proved for D2 at `report/sections/04l_elliptic_cavity_channel.tex:171–175`. Consequently the canonical class metric induces no point of E3 by the proposed cut, and the legitimate scalar-inner replacement has an explicit Gram outside that cone. Neither is the unknown comparison metric of E4.

## E6 — SHARPENED: two ends, one cusp, and inverse-character blocks (ideation)

**PROVED — the existing theorem.** The exact notebook claim is `prop:siegel-constant-term`, `report/sections/04r_h_theta_channels.tex:19–31`:

`∫_0^1 Θ_z(t) dx = θ(t/y)+sqrt(y/t)(θ(ty)−1)`.

Poisson exchanges the two complete theta terms by `F(t)↦t^(−1)F(1/t)` **at fixed y**, and the subtracted `sqrt(y/t)` is fixed. Their Mellin transforms are the two coefficients of the constant term at the modular surface's single cusp. This is a theorem about theta channels and a constant term. It does not identify a topological quotient of the GL₁ bond with the GL₂ surface or its exit model.

**SHARPENED.** `R_+^×≅R` has two topological ends, 0 and infinity. Calling those “two GL₁ cusps” is metaphorical: they are not two rational parabolic cusp classes of GL₁. The earlier shard itself says “one cusp” at `report/sections/04p_gl1_bond.tex:88–90`. The geometric slogan “the automorphism folds the two GL₁ cusps into the one GL₂ cusp” is therefore an **OPEN identification / speculation**, beyond the proved constant-term identity. The proposed theta-cyclic cut is already marked refuted at `04p_gl1_bond.tex:103–109`; it cannot provide the missing exit identification.

**PROVED — the finite analogue on this bond.** Since `K_C~2P_0`, the Riemann–Roch involution is `(j,n)↦(−j,2−n)`, and `θ_n(j)=5^{n−1}θ_{2−n}(−j)`. It sends Fourier label k to 15−k. There are fifteen cusp classes for `GL₂(O(C\P_0))`: the count and class parametrization are byte-supported by Oliver Lorscheid (2010), `refs/src/1012.3513/hecke.tex:992`, and Arends–Peterson–Weich (2026), `refs/src/2603.26443/final_draft.tex:884–892`. The seven inverse pairs listed in E3 and the trivial character form Fourier blocks; they do **not** turn fifteen geometric cusps into eight.

**OPEN — conditional H-CLASS fold.** If the genus-two scattering matrix has the form `S=M P_inv`, `M_ab=f(b−a)`, postulated at `report/sections/04k_elliptic_cavity_scattering.tex:290–304`, its Fourier transform is one scalar block and seven blocks

`[[0,m_k],[m_{15−k},0]]`, `m_k=Σ_{j=0}^{14}f(j)ζ^{−kj}`,

with eigenvalues `±sqrt(m_k m_{15−k})`. H-CLASS predicts L-ratios (with the induced-character and height conventions still to be checked for this quotient); this curve supplies all fourteen nonconstant quadratic L-factors, where genus one supplied constants. This is the precise algebraic content available for the proposed fold. Proving that this actual genus-two quotient has that scattering matrix, and transporting its metric to cohomology, remains **OPEN**, not a consequence of class-field reciprocity.

## Numerical checks for the blind lane

**PROVED — reproducible specification.** Run the three standalone scripts with `python3`; they write no auxiliary output files and require only SymPy and NumPy. The finite-data script recomputes from the curve equation, checks all 225 group additions, enumerates every reduced divisor class, and multiplies the L-factors exactly modulo `Φ_15(ζ)=0`. Exact arithmetic is used for identities and integer counts; floating point is used only for printed roots, ratios and the displayed numerical scalar Gram. All three scripts completed with `ALL ASSERTIONS PASSED` in this lane.

| Item | Exact expected output |
|---|---|
| Point counts | `(N_1,N_2,N_3,N_4)=(3,31,117,619)`, including one infinity each time |
| Power sums / P | `(3,−5,9,7)` / `1−3T+7T²−15T³+25T⁴` |
| Class group | `Z/15`, generator `[(1,1)−∞]`, inverse `[(1,4)−∞]`; all 15 Mumford pairs in E1 |
| Special effective sets | degree 0: `{0}`; degree 1: `{0,1,14}`; degree 2: every class, with h⁰=2 only at 0 |
| Effective-divisor counts | `a_0,…,a_7=(1,3,20,90,465,2340,11715,58590)` |
| Fourteen L-polynomials | `L_k=1+A_k T+5T²`, with the full ordered coefficient tuple below |
| Cover numerator | the explicit four-factor product in E2; degree 32; genus 16; `N_1(C')=15` |
| π eigenbasis | `e_α=f_F(z)/((z−α)f_F'(α))`, α given in E1; multiplication matrix in E4.3 |
| Actual lift weights | `c_j=|φ_jξ|` in the polarization-transported marking, `ξ I bar I=D_K^(−1)`; **not numerically identified with the bond** |
| Completely specified reference weights | `I_0=O_K`, `ξ_0=1/(√21 δ)`, `(c_1^0,c_2^0)=(0.091999448073339…,0.049577227300714…)`, ratio `(25+3√21)/(2√109)`; dual ratio its reciprocal |
| Bond Fourier θ weights | `(19,27,95)/√15` at k=0, `(4,4A_k,20)/√15` for k≠0; total squared norm 1101 |
| Literal cut Gram / spectrum | `I_45`, spectrum `{0}` with fifteen Jordan blocks of size 3; scalar θ-cyclic Gram `G_theta` in E5.2, determinant 254679, exit rank 2 |
| Scalar-inner modal Gram | `(4/5)/(1−bar ρ_aρ_b)` in E5.3, positive definite, off-diagonal nonzero, Frobenius-normality defect max `1.3238593874…` |

For a compact independent checksum of **all fourteen** coefficient triples, put `s_j=1+ζ^j+ζ^(−j)` and `u_±=(1±√5)/2`. Ordered by k=1,…,14 they are

`(1,s_1,5), (1,s_2,5), (1,u_+,5), (1,s_4,5), (1,0,5), (1,u_−,5), (1,s_7,5),`

`(1,s_7,5), (1,u_−,5), (1,0,5), (1,s_4,5), (1,u_+,5), (1,s_2,5), (1,s_1,5)`.

The ordered A_k decimals are

`(2.827090915285, 2.338261212718, 1.618033988750, 0.790943073465, 0, −0.618033988750, −0.956295201468,`

`−0.956295201468, −0.618033988750, 0, 0.790943073465, 1.618033988750, 2.338261212718, 2.827090915285)`.

No numerical test should silently substitute the reference lattice's weights for J's marked lift, or the Hardy Gram for the bond's degree-cut Gram. They are three different, explicitly named objects. The blind lane can refute or confirm every finite entry without making that substitution.

## Corrections to the brief

| # | Verdict | Correction |
|---:|---|---|
| 1 | SHARPENED | `Z/15` and `Z/3×Z/5` are the same group; the explicit generator is `[(1,1)−∞]`. |
| 2 | SHARPENED | Zeros of P and L have modulus `1/√5`; their reciprocals are Frobenius eigenvalues of modulus `√5`. Both are displayed separately. |
| 3 | SHARPENED | The class-group Fourier transform labels the cohomology summands and computes their L-factors; it is not a Hilbert-space identification of the bond with H¹(C'). |
| 4 | SHARPENED | The unramified functional-equation constant is `χ([K_C−(2g−2)P_0])`; here it is 1 for every character. |
| 5 | REFUTED | A single nontrivial L-factor is generally not the quotient of a cyclic cover's numerator by P; that quotient is a product over its nontrivial characters (also a correction to the predecessor). |
| 6 | SHARPENED | The direct channel uses U=F/√5 on 32 modes; the cited cavity convention uses U²≃(F/√5)⊗1₂ on 64 modes. |
| 7 | SHARPENED | Circle spectrum implies a positive invariant metric only with semisimplicity; distinct roots provide it here blockwise. |
| 8 | REFUTED | `Q_ℓ`-cohomology does not itself supply complex conjugation; use coefficient reality on Betti cohomology of a lift or an expressly defined real spectral module. |
| 9 | SHARPENED | Real structure interchanges χ and bar χ; it need not equalize the two weights within a nonreal χ block. Repeated inverse-character eigenvalues allow off-block metrics unless deck invariance is imposed. |
| 10 | SHARPENED | The trace Riemann form gives weights `|φξ|` on homology or polarization-transported eigenvectors; dual period forms in H¹ have reciprocal weights. |
| 11 | REFUTED | “Normalized by the lattice” is not a unique normalization: multiplication by the explicit real unit ε preserves the lattice and changes the weight ratio. |
| 12 | REFUTED | The full theta state is not in the stated ℓ² bond. Its finite special-degree truncation is well defined and computed. |
| 13 | OPEN | No map from theta Fourier components or L-values to the trivial block's four geometric eigenvectors is specified; the desired independent symmetric-ray comparison remains undefined. |
| 14 | REFUTED | The unsquared ratio need not be in K or K⁺: the explicit reference ratio requires √109, although its square is in K⁺. |
| 15 | REFUTED | There are not intrinsically two possible marked ratios awaiting an ideal-class test; even one fixed lattice has infinitely many generator-dependent ratios. The two displayed reciprocal ratios distinguish a primal from a dual coordinate convention. |
| 16 | SHARPENED | The endomorphism order is already maximal: `Z[π,5/π]=O_K`, with discriminant 48069. Unknown marked CM data cannot be blamed on an unspecified overorder. |
| 17 | REFUTED | Keeping all n≤2 leaves an infinite-dimensional contraction; keeping 0≤n≤2 gives a nilpotent 45-dimensional contraction with determinant z⁴⁵. |
| 18 | REFUTED | One boundary degree does not mean one scalar exit: the full cut has rank 15, and the special theta-cyclic cut has rank 2. |
| 19 | REFUTED | A scalar-exit contraction of dimension greater than one and common spectral modulus r<1 cannot have a Frobenius-normal metric with defect `(1−r²)I`. |
| 20 | SHARPENED | A characteristic determinant of a finite conservative model is rational inner; the replacement with P as numerator is `P(w)/f_F(w)`, not P alone. |
| 21 | SHARPENED | The GL₁ “two cusps” are two topological ends; the proved GL₂ theorem is the theta constant-term identity, with weighted involution in t at fixed y. |
| 22 | OPEN | Inverse-character Fourier blocks do not identify pairs of geometric cusps. General genus-two H-CLASS and a geometric fold remain to be established. |
| 23 | SHARPENED | The allowed-output instruction and the mandatory durability instruction conflict literally over `progress.txt`; this file was maintained solely as the explicitly requested one-line durability marker. No other project files were edited, and no git command was used. |

**PROVED — dependency boundary.** The finite circle checks in E1–E2 are exact inequalities, not an appeal to numerical accuracy or `asm:weil-curves`. The identification with étale H¹ uses the named standard trace/Euler-characteristic facts; the Hodge interpretation uses exactly the two CM lift assumptions of shard 06f plus the explicitly stated Riemann-form description. The optional finite ideal enumeration uses Minkowski's ideal-class bound (Hermann Minkowski, *Geometrie der Zahlen*, 1896), **not byte-cited**: every ideal class of a degree-n field of signature `(r_1,r_2)` has an integral ideal of norm at most `(n!/n^n)(4/π)^{r_2} sqrt(|disc K|)`. It is a specified follow-up computation for a marked lift, not evidence that the proposed comparison is already defined.

## What this changes in the notebook

| Claim to register | Status | One-sentence statement |
|---|---|---|
| E1 / genus-two class-bond data | PROVED | The curve has counts `(3,31,117,619)`, group `Z/15` generated by `[(1,1)−∞]`, theta classes `{0,±1}`, and special counts `(1,3,20)`. |
| E2 / pointed class-field cohomology | PROVED, with stated standard inputs | The pointed Hilbert class cover has genus 16 and its Frobenius numerator is P times the fourteen explicitly computed quadratic character factors. |
| E2 / literal bond=H¹ | SHARPENED | The correspondence is a character-labelled cohomological realization of L-functions, not an identification of the class/degree Hilbert space or its metric with H¹. |
| E3 / genus-two metric cone | PROVED | The trivial Frobenius block has a two-parameter real positive invariant cone, one ratio modulo scale, with character-pair and multiplicity qualifications on the full cover. |
| E3 / channel convention | SHARPENED | A direct-Frobenius channel has 32 modes and a square-root cavity channel has 64, both giving relaxation modulus `1/√5` after choosing an invariant metric. |
| E4 / CM field and reference metric | PROVED, Hodge reading conditional on the named lift assumptions | The field is `Q(√21, sqrt((-25+3√21)/2))`, its order is maximal, and the explicit principal reference lattice has transported ratio `(25+3√21)/(2√109)`. |
| E4 / rational-idempotent symmetric metric | REFUTED | No rational K-module marking can give equal polarization weights at the two CM places, since that would force an imaginary quadratic subfield of K. |
| E4 / actual bond-versus-Hodge comparison | OPEN | A canonical comparison map and eigenvector normalization must be supplied before the bond's symmetric-ray claim has a numerical meaning for the marked lift. |
| E5 / special-degree exit model | REFUTED | The literal cut is infinite or nilpotent and does not carry P, while the scalar Blaschke replacement has the explicitly non-Frobenius-normal Cauchy Gram. |
| E6 / two-end fold | SHARPENED / OPEN | The Siegel theta constant-term identity is proved; interpreting it as a geometric fold of ends or as a genus-two scattering/metric identification remains open. |
