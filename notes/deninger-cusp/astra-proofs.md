# Ihara quotient, Eisenstein cohomology, and character scattering

Author: `codex:gpt-6-astra`

| Claim | Verdict | Statement to register |
|---|---|---|
| D1 | SHARPENED | Two surface slices and a Hecke correspondence; vertex cohomology splits, but Eisenstein action is character-dependent. |
| D2 | REFUTED | Frobenius is not the double of all H^1; the four sectors differ in pairing, dimension, and parity. |
| D3 | SHARPENED | Exact prime-level matrices and determinant; two cusp coordinates per even nebentypus, with local factors. |
| D4 | SHARPENED | Two cusp edges yield the ratios; correct conjugation gives pure inner arithmetic factors; odd weight-zero request is impossible. |
| D5 | SHARPENED | Prime-level models have multiplicities, local modes and delays; rank h concerns a specified cogenerator, and GRH metrics concern arithmetic modes. |
| D6 | SHARPENED | Register explicit Q scattering, reject literal diagonal H-ARITH, and retain the specified geometric and function-field tasks as open. |

D1–D6 are complete as proof/refutation tasks. Explicitly marked OPEN items are retained limitations, not pending ledger rows.

## Conventions and scope — SHARPENED

Author: `codex:gpt-6-astra`

A verdict applies to the statement immediately following it; a refuted statement is followed by its replacement. All vector spaces are over characteristic zero. For the geometric arguments assume `N >= 5`; at smaller levels use orbifold cohomology with rational coefficients. Put `X=X_1(N)`, `Y=X-C`, and `h=|C|`. Scattering uses weight zero, hence only **even** nebentypus. We distinguish finite-dimensional boundary cohomology, the continuous Eisenstein spectrum, and a Hardy model constructed from a scattering symbol.

Use the standard completion
\[
 \Lambda_\chi(u)
 =(f/\pi)^{(u+a)/2}\Gamma((u+a)/2)L(u,\chi),
 \quad \chi(-1)=(-1)^a,
 \quad \epsilon_\chi=\tau(\chi)/(i^a\sqrt f).
\]
Here `f` is the primitive conductor, characters are zero on nonunits, and `tau(chi)=sum_{r mod f} chi(r) exp(2 pi i r/f)`. For the primitive trivial character, `f=1`, write `Lambda_0(u)=pi^{-u/2}Gamma(u/2)zeta(u)` and `xi(u)=u(u-1)Lambda_0(u)/2`. Thus **xi is entire and has no poles**. The sibling file's theta Mellin function called `Lambda` is `2 Lambda_0`, as follows from `notes/h-theta/astra-proofs.md:594–604`; ratios are unaffected.

**PROVED (classical input, Dirichlet completion; Tate 1950, not byte-cited).** Primitive nonprincipal `Lambda_chi` is entire of order one, has precisely the nontrivial zeros in `0<Re u<1`, and satisfies
\[
 \Lambda_\chi(u)=\epsilon_\chi\Lambda_{\bar\chi}(1-u),
 \qquad \overline{\Lambda_\chi(\bar u)}=\Lambda_{\bar\chi}(u).
\]
The completion for the trivial character has simple poles at `0,1`. We use nonvanishing on `Re u=1` (Hadamard–de la Vallée Poussin 1896 and the Dirichlet-character extension, not byte-cited), and the fixed-conductor zero count, with multiplicities,
\[
 N_\chi(T):=\#\{\rho:|\Im\rho|\le T\}
 =\frac{T}{\pi}\log\frac{fT}{2\pi e}+O_\chi(\log(T+2)).
\]
This last standard argument-principle theorem is cited in the form in Davenport, *Multiplicative Number Theory*, 3rd ed. 2000, not byte-cited; no simplicity or GRH is included.

Repository anchors: the actual finite criterion is `notes/deninger-lps/src/manuscript.txt:540–545`; its Poincaré hypotheses are `:644–659`; its warning that the doubled form is not a face pairing is `:1219–1225,1255–1259`. The LPS file itself puts the even eigenlines in doubled horizontal **degree zero**, `notes/deninger-lps/src/lps-deninger-worked-example.md:319–350,614–640`. The multi-exit theorem only states `rank J <= h`, `report/sections/04l_elliptic_cavity_channel.tex:38–57`. These distinctions are binding here. In particular the manuscript says, “it is not, without an additional construction, the cup pairing of the original faces” (`notes/deninger-lps/src/manuscript.txt:1224–1225`). The cavity shard itself says, “the model below is proved, its identification with the geometric wave compression is not” (`report/sections/04l_elliptic_cavity_channel.tex:16–17`).

## D1. The arithmetic correspondence, not a literal square complex — SHARPENED

Author: `codex:gpt-6-astra`

### D1.1. Structure — PROVED in the following corrected form

**Classical input (Ihara 1966; Serre, *Trees*, 1980, II.1; not byte-cited).** The diagonal `SL_2(Z[1/p])` is a nonuniform lattice of finite covolume in `SL_2(R) x SL_2(Q_p)`. Its action on the Bruhat–Tits tree is without inversion and has quotient one edge, with two vertex types; the vertex stabilizers are conjugates of `SL_2(Z)` and the edge stabilizer is conjugate to `Gamma_0(p)`. These are the precise lattice/tree facts used here. [Ihara's original paper (1966)](https://www.jstage.jst.go.jp/article/jmath1948/18/3/18_3_219/_article/-char/en) is an external reference, **not byte-cited**.

Define the group, rather than unspecified “points” of a discrete group:
\[
 \Gamma_S=\{\gamma\in SL_2(\mathbb Z[1/p]):
 \gamma\bmod N=\begin{pmatrix}1&*\\0&1\end{pmatrix}\}.
\]
Reduction makes sense because `p` is invertible modulo `N`. This is a finite-index subgroup of the stated lattice. Choose `g=diag(1,p)`, acting projectively, and adjacent vertices `v_0=[Z_p^2]`, `v_1=g v_0`. Their stabilizers in `Gamma_S` are `Gamma` and `g Gamma g^{-1}`; the edge stabilizer is
\[
 \Delta=\Gamma_1(N)\cap\Gamma_0(p).
\]
The quotient still has one edge: the reductions of each integral vertex stabilizer, and of the edge stabilizer before imposing level `N`, surject onto `SL_2(Z/N)` by the Chinese remainder theorem (`p` is coprime to `N`). Consequently the finite-index passage creates no extra vertex or edge orbit. Identifying the second vertex surface by `g^{-1}` gives the graph of surfaces
\[
 Y\ \xleftarrow{\ \alpha\ }\ Y_\Delta\ \xrightarrow{\ \beta\ }\ Y,
 \qquad \alpha(z)=z,\quad\beta(z)=pz.
\]
Both maps have degree `p+1`. The quotient of `H x T` is the associated graph of spaces (use mapping cylinders/topological stacks when necessary).

**REFUTED (literal D1(a)).** `H x T` has real dimension **three**, not two. A triangulated surface times an edge has prisms as well as mixed rectangles. Also `SL_2` preserves tree type: there are two vertex slices, not one. The `p+1` branches are the degree of the two degeneracy maps, not `p+1` distinct edges in the quotient graph. A determinant-`p` enlargement can identify types, but is a different group and must retain its diamond action.

### D1.2. Which horizontal cohomology — SHARPENED

A chosen vertex slice has `H^1(Y;R)`. The horizontal de Rham complex on all of `H x T`, with transverse dependence left unrestricted and no transverse differential, does **not** canonically reduce to that single vector space: the two vertex slices and the edge slices have stabilizers `Gamma`, `g Gamma g^{-1}`, and `Delta`. Their cohomologies form a coefficient system over the quotient edge. Total cohomology additionally imposes the graph-of-spaces differential. Hence “leafwise cohomology is H^1(Y)” is **REFUTED** without the convention “cohomology of one specified vertex slice.” This is the same essential distinction as `notes/deninger-lps/src/lps-deninger-worked-example.md:207–228`, where the horizontal complex is explicitly defined and the full face differential omitted.

**Classical inputs — PROVED as cited theorems, not byte-cited.** Eichler–Shimura (Eichler 1957; Shimura 1959) identifies the complexified parabolic cohomology `im(H_c^1(Y)->H^1(Y))=H^1(X)` Hecke-equivariantly with `S_2(Gamma) ⊕ overline{S_2(Gamma)}`. Manin 1972 and Drinfeld 1973 assert that every degree-zero divisor supported at cusps is torsion in `Jac(X)`. The mixed-Hodge exact sequence for a punctured smooth projective curve (Deligne 1971, not byte-cited) is
\[
 0\longrightarrow H^1(X;\mathbb Q)\longrightarrow H^1(Y;\mathbb Q)
 \xrightarrow{\operatorname{res}}\widetilde H^0(C;\mathbb Q)(-1)
 \longrightarrow0.                                      \tag{D1.1}
\]
Here `tilde H^0` means the kernel of summation on functions on `C`. Its dimension is `h-1`, its Hodge type is `(1,1)`, and the subspace on the left is pure weight one. The extension class is the cuspidal Abel–Jacobi class; Manin–Drinfeld kills it over `Q`. A rational mixed-Hodge splitting is unique because there is no morphism from a Tate structure of weight two to the pure weight-one structure. It is therefore Hecke-equivariant. Denote its image by `Eis`. Equivalently one can use logarithmic differentials of modular units, with their rational residue classes. See [Manin 1972](https://www.mathnet.ru/eng/im2290) for the external theorem reference, **not byte-cited**.

Thus `dim_R H^1(Y)=2g+h-1`, `dim_R Eis=h-1`; the displayed holomorphic decomposition means complexification, with the natural conjugation giving its real form. It is not a sum of two additional independent real copies of `S_2`.

**REFUTED (scalar Eisenstein action).** In the holomorphic Hecke normalization a weight-two Eisenstein eigenpacket with primitive inducing characters `(chi_1,chi_2)`, nebentypus `chi_1 chi_2`, and conductors whose product divides `N`, has, for `p∤N`,
\[
 a_p=\chi_1(p)+p\chi_2(p).                              \tag{D1.2}
\]
This follows directly from its coefficients `a_n=sum_{d|n} chi_1(n/d)chi_2(d)d`. Level raising adds multiplicities. For the pair `(1,1)` one takes the holomorphic combinations `E_2(z)-d E_2(dz)` for divisors `d>1`; their eigenvalue is `1+p`. Other packets need not have this eigenvalue. At prime level `ell>=5` there is one trivial packet and **two** packets `(1,chi),(chi,1)` for every nontrivial even `chi mod ell`. Their total dimension is `1+2((ell-1)/2-1)=ell-2=h-1`. This already disproves the scalar assertion at `N=5,p=2` (eigenvalues `3,-1,1`). The numerical section gives `N=11` exactly.

### D1.3. Transport on forms — PROVED, with definition separated from theorem

Define on smooth differential forms
\[
 \mathcal T_p=\alpha_*\beta^* : \Omega^\bullet(Y)\to\Omega^\bullet(Y),
 \qquad (\alpha_*\eta)|_U=\sum_{j=1}^{p+1}\sigma_j^*\eta, \tag{D1.3}
\]
where the `sigma_j` are local inverse sheets of `alpha` over an evenly covered `U`. The sum is independent of labeling, patches globally, and commutes with `d`, since pullback does. It also preserves compact supports under these proper finite coverings. This is a complete cochain definition. Calling its cohomology action `T_p` is the usual geometric definition of the Hecke operator. The theorem identifying it with the holomorphic Hecke operator is the correspondence form of Eichler–Shimura above (the factors in weight two come from pulling back `f(z) dz`). Mixed rectangles merely express the compatibility needed to patch the local sheets. No new square-complex transport theorem, independent of the correspondence, has been established or is needed.

## D2. Frobenius and the three different pairings — REFUTED as a four-fold identity

Author: `codex:gpt-6-astra`

### D2.1. Arithmetic positivity — SHARPENED

**Classical input (Eichler–Shimura congruence relation, Eichler 1954 / Shimura 1958; good reduction by Igusa 1959; not byte-cited).** For a weight-two normalized newform `f` of nebentypus `psi`, at `p∤N` its two-dimensional coefficient-field summand in the étale cohomology of the compact modular curve has characteristic polynomial
\[
 \det(X-F_p\mid V_f)=X^2-a_p(f)X+p\psi(p).              \tag{D2.1}
\]
Oldform copies have the corresponding multiplicity. On full cohomology the relation is `F_p^2-T_p F_p+p< p >=0`, with compatible choices of the diamond convention. We use cohomological Frobenius, whose eigenvalue on `H^2` is `p`; naming the inverse Galois element would invert eigenvalues. The correspondence identity underlying this input is also described in [Darmon's Eichler–Shimura account, §2.5](https://www.math.mcgill.ca/darmon/pub/Articles/Research/36.NSF-CBMS/chapter.pdf), **not byte-cited**.

**Classical input (Weil 1948; Tate 1966 semisimplicity for abelian varieties over finite fields; not byte-cited).** For the smooth projective reduction `X/F_p`, `F_p` on `H^1_et(X_bar,Q_l)`, `l≠p`, is semisimple with every complex eigenvalue of modulus `sqrt p`. Cup product gives a nondegenerate alternating form with values in `H^2`, and
\[
 F_p^t\Omega_XF_p=p\Omega_X.                           \tag{D2.2}
\]
This weight-two Ramanujan theorem uses the curve Riemann hypothesis and the congruence relation, not Deligne's higher-weight theorem. For nebentypus `psi`, `|a_p(f)|<=2sqrt p` follows after dividing the trace by a square root of `psi(p)`; the two roots themselves always have modulus `sqrt p`.

**REFUTED (D2(a)'s Bass identification).** If `dim H^1(X)=2g`, the proposed companion on `H^1(X) ⊕ H^1(X)` has dimension `4g`; étale `H^1(X)` has dimension `2g`. It is not Frobenius. Moreover the proposed determinant `p` omits `psi(p)`. A companion for (D2.1) can represent a cyclic two-dimensional `V_f`; at a repeated root actual semisimple Frobenius is scalar and the companion is not. Doubling a single holomorphic eigenline, before adjoining its antiholomorphic partner, is the appropriate dimension count, not doubling their sum. There is no canonical comparison identifying complex Petersson cohomology with a real Frobenius space and carrying the proposed doubled form to its cup product.

**PROVED (adjoints versus similitudes).** For correspondence-defined `T_p`, Poincaré duality and change of variables give
\[
 \Omega_X(T_px,y)=\Omega_X(x,T_p' y),\qquad
 T_p'=\beta_*\alpha^*=\langle p\rangle^{-1}T_p.        \tag{D2.3}
\]
The Petersson adjoint has the same Hecke adjoint; equivalently the normalized Fricke involution conjugates `T_p` to this adjoint. Use `w T_p w^{-1}`, not an unspecified `w T_p w` unless `w^2=1` in that convention. This is an adjoint identity, not `T_p^t Omega_X T_p=p Omega_X`. On a real two-plane where `T_p=a_p I`, the latter left side is `a_p^2 Omega_X`, which generally differs from `p Omega_X`.

**PROVED (what Bass positivity actually says).** On a real space `K` with positive form `M` and `M`-self-adjoint `T`, put
\[
 F_B=\begin{pmatrix}T&-pI\\I&0\end{pmatrix},\quad
 \Omega_B=\begin{pmatrix}0&M\\-M&0\end{pmatrix},\quad
 G_B=\begin{pmatrix}M&-MT/2\\-MT/2&pM\end{pmatrix}.
                                                               \tag{D2.4}
\]
Block multiplication gives `F_B^t Omega_B F_B=p Omega_B` and `F_B^t G_B F_B=p G_B`. The Schur complement is `M(pI-T^2/4)` in an `M`-orthonormal basis. Consequently a positive invariant metric for **this companion** exists iff every eigenvalue of `T` satisfies the **strict** inequality `|lambda|<2sqrt p`; equality gives a nontrivial Jordan block. This is exactly `notes/deninger-lps/src/manuscript.txt:1188–1259`, including the endpoint obstruction. For trivial nebentypus the Petersson form supplies `M`, but `G_B`, not the undoubled Petersson metric, is the displayed invariant metric. The direct sum Petersson metric is not invariant: for `T=0`, `F_B` sends `(0,y)` to `(-py,0)`, multiplying its squared norm by `p^2` instead of `p`.

On an actual cyclic real Frobenius plane, every alternating form is a scalar multiple of the standard two-dimensional form, so a chosen companion basis makes `Omega_X=c Omega_B` when (D2.1) has determinant `p`. This elementary basis-dependent observation is **PROVED**, but supplies neither the false `4g=2g` identification nor a face construction. With nonreal nebentypus one must retain `p psi(p)` and the conjugate/dual packets; Proposition 9.3 for a real symmetric `T` cannot simply be applied unchanged. Actual compact-curve Frobenius already has its own cup similitude and semisimplicity. After choosing a real symplectic realization of its conjugate-paired spectral data, Theorem 5.2 supplies a positive compatible metric; this is not a statement that Frobenius acts on the given complex curve with its original Petersson metric.

### D2.2. Open-curve pairings — PROVED; the brief's radical identification is REFUTED

For a connected punctured compact curve with `h>0`, `H^2(Y)=0`. Hence the ordinary cohomological cup product
\[
 H^1(Y)\times H^1(Y)\longrightarrow H^2(Y)
\]
is identically zero: its radical is **all** of `H^1(Y)`. The pairing
\[
 H_c^1(Y)\times H^1(Y)\longrightarrow H_c^2(Y)\simeq\mathbb Q
                                                               \tag{D2.5}
\]
is perfect by Poincaré duality for oriented manifolds. It has **no** radical on either side. Neither assertion in the brief about these two pairings is correct.

For clarity write out the compact-support exact sequence:
\[
 0\to H^0(X)\to H^0(C)\to H_c^1(Y)
 \xrightarrow{j}H^1(X)\to0.                            \tag{D2.6}
\]
The skew form on `H_c^1(Y)` obtained by sending its second argument into `H^1(Y)` has radical `ker j=H^0(C)/H^0(X)`, of dimension `h-1`; it is weight **zero**, dual to the weight-two residue quotient in (D1.1) through the Tate-valued pairing. These are compactly supported connecting classes, not the noncompact Eisenstein classes in `H^1(Y)`.

There are two legitimate replacements. On **homology** `H_1(Y)`, intersection has radical the small cusp loops with their one relation, of dimension `h-1`. On cohomology, the split retraction `r:H^1(Y)->H^1(X)` from D1 defines
\[
 \Omega_{\rm split}(x,y)=\Omega_X(rx,ry),\qquad
 \operatorname{rad}\Omega_{\rm split}=\mathrm{Eis}.     \tag{D2.7}
\]
The second statement is immediate from nondegeneracy on `H^1(X)`; it is **PROVED for this defined form**. It is not the ordinary cup product of `Y` and has not been realized as the face pairing of the three-dimensional arithmetic quotient. Borel–Moore homology gives the equivalent duality formulation; it does not turn (D2.5) into a degenerate pairing.

### D2.3. Eisenstein roots, poles, and exits — REFUTED as identities

For the trivial packet the correct quadratic has roots `1,p`. For a general Eisenstein packet (D1.2), the arithmetic quadratic factors as
\[
 X^2-(\chi_1(p)+p\chi_2(p))X+p\chi_1(p)\chi_2(p)
 =(X-\chi_1(p))(X-p\chi_2(p)).                         \tag{D2.8}
\]
Its root moduli are `1,p`, so no positive `p`-similitude metric exists on these root spaces: applying such a metric to an eigenvector would force its eigenvalue modulus to be `sqrt p`. This conclusion is **PROVED**, also for complex packets using Hermitian metrics. It does not say `T_p=p+1` or put Eisenstein classes in even cohomological degree. The untwisted Bass pencil with constant coefficient `p` is not (D2.8) in general.

The proposed identity fails in dimensions and in parity. Boundary cohomology has dimension `h-1`; the continuous spectrum has multiplicity `h`; the residual constant eigenfunction has multiplicity one; `H^0(X)` and `H^2(X)` are two different even-degree lines. Already `Y(1)` has `h=1`, `H^1(Y(1);Q)=0`, but its scalar scattering coefficient `Lambda_0(2s-1)/Lambda_0(2s)` is nonconstant and has a pole at `s=1`. The same zero-cohomology/one-cusp example can be understood using orbifold rational cohomology. Thus neither a scattering exit nor the pole pair can be the degree-one Eisenstein radical.

**SHARPENED (notebook reading).** The continuous Eisenstein *families*, indexed by cusp data at every spectral parameter, carry the scattering coefficients. Their special weight-two cohomology classes record boundary residues, but are a finite-dimensional shadow, not the scattering state space. The gamma factor and `T log T` zero count appear in the completed scattering `L`-ratios; no finite-dimensional cohomology space produces this count. Compare the explicit gamma/logarithmic-derivative separation in `report/sections/09c_selberg_tower_cusp.tex:78–100,122–138` and the finite-model limitation in `notes/deninger-lps/src/lps-deninger-worked-example.md:635–640`.

**REFUTED (the claimed LPS contrast).** That finite example already has even poles `1,17` without a cusp (`:319–350,620`), and its horizontal precursor has odd dimension `721` (`:217–225`), so it cannot have a nondegenerate alternating form. Positivity is on its constructed odd double; it is not “positivity on everything” or proof of a nondegenerate horizontal face pairing. The later manuscript explicitly makes this correction at `:1284–1289`.

## D3. Prime-level scattering, including all constants — SHARPENED

Author: `codex:gpt-6-astra`

### D3.1. Cusps and the correct character decomposition — PROVED

The exact cusp parametrization for `Gamma_1(N)` is
\[
 C_1(N)=\{(c\bmod N,\ a\bmod d):d=(c,N),\ a\in(\mathbb Z/d)^\times\}/\{(c,a)\sim(-c,-a)\}.
                                                               \tag{D3.1}
\]
It sends the primitive column `(a,c)` to the indicated residues. Indeed upper unipotent left multiplication modulo `N` sends `(a,c)` to `(a+bc,c)`, whose first-coordinate orbits are precisely residues modulo `(c,N)`; primitive columns are transitive lifts, and the sign accounts for projective cusps. Equivalently it is the disjoint union, over `d|N`, of `((Z/d)^x x (Z/(N/d))^x)/±` with simultaneous sign (write `c=d v`). This is a parametrized **set**, not a canonical abelian group. For `N>=5` the sign action is free, hence
\[
 h_1(N)=\frac12\sum_{d\mid N}\varphi(d)\varphi(N/d),
 \qquad h_1(\ell)=\ell-1.                              \tag{D3.2}
\]
For `N=5,7,11,13` this gives `4,6,10,12`. The brief's formula using `gcd(d,N/d)` belongs to `Gamma_0(N)`, whose cusp count is `sum_{d|N} phi(gcd(d,N/d))`; it gives two at prime level and cannot parametrize `Gamma_1(ell)`.

For prime `ell`, the diamond group `G=(Z/ell)^x/{±1}` acts freely and transitively on each of two cusp orbits. Thus the cusp representation is `C[G] ⊕ C[G]`. Fourier transform on `G` yields a **two-dimensional multiplicity space for each even nebentypus** `psi`, including real characters. This is not the inverse-character block structure of the Picard-group model in `report/sections/04p_gl1_bond.tex:64–81`: that proposition concerns `GL_2(O(C-P_0))`, not `Gamma_1(N)` over `Q`.

### D3.2. Normalization — PROVED definitions

Write `q=ell` in this section (it is the level prime, not D1's transverse prime). Use width-one scaling matrices
\[
 \sigma_\infty=I,\qquad \sigma_0=W_q=\begin{pmatrix}0&-q^{-1/2}\\q^{1/2}&0\end{pmatrix}.
\]
For even `psi mod q`, set, initially `Re s>1`,
\[
 E_\infty^\psi(z,s)=\frac12
 \sum_{\substack{(c,d)=1\\q\mid c}}\bar\psi(d)\frac{y^s}{|cz+d|^{2s}},
 \qquad E_0^\psi(z,s)=E_\infty^{\bar\psi}(W_q z,s).
                                                               \tag{D3.3}
\]
For the trivial character use the usual principal values on admissible `d`. Both functions transform by `psi(d_gamma)` under `Gamma_0(q)`. Define `Phi_psi(s)_{ab}` with **row = observing cusp** and **column = source cusp**, ordered `(infinity,0)`, by
\[
 (E_b^\psi\mid\sigma_a)_0(y,s)=\delta_{ab}y^s+\Phi_\psi(s)_{ab}y^{1-s}.
                                                               \tag{D3.4}
\]
Another common convention transposes every matrix below. The functional equation is stated in this convention as `Phi_psi(s) Phi_psi(1-s)=I`.

### D3.3. Nontrivial even character — PROVED by direct summation

Every nontrivial `psi mod q` is primitive. Put
\[
 R_\psi(s)=\frac{\Lambda_\psi(2s-1)}{\Lambda_\psi(2s)},\qquad
 A_\psi(s)=q^{1/2-s}R_\psi(s)
 =q^{-s}\sqrt\pi\frac{\Gamma(s-1/2)}{\Gamma(s)}
       \frac{L(2s-1,\psi)}{L(2s,\psi)}.
                                                               \tag{D3.5}
\]
Then the full answer is
\[
 \boxed{\Phi_\psi(s)=\begin{pmatrix}0&A_\psi(s)\\A_{\bar\psi}(s)&0\end{pmatrix}},
 \qquad \det\Phi_\psi=-q^{1-2s}R_\psi R_{\bar\psi}.     \tag{D3.6}
\]
The Gauss-sum form, often hidden by the use of same-character ratios, is
\[
 A_\psi(s)=q^{1/2-s}\frac{\tau(\psi)}{\sqrt q}
                  \frac{\Lambda_{\bar\psi}(2-2s)}{\Lambda_\psi(2s)}.
                                                               \tag{D3.7}
\]
There is no omitted extra Gauss factor in (D3.5).

1. Replacing primitive pairs by all nonzero pairs in `E_infinity^psi` multiplies it by `L(2s,bar psi)`. For fixed nonzero `c=qm`, averaging over `x in [0,1]` sums a nontrivial character over complete residue periods; its average is zero. Thus this Eisenstein series has no `y^{1-s}` term at infinity.
2. Substitution by `W_q` in (D3.3) gives
\[
 E_0^\psi(z,s)=\frac{q^{-s}}2\sum_{(m,n)=1}\psi(m)\frac{y^s}{|mz+n|^{2s}}.
                                                               \tag{D3.8}
\]
Its zero-frequency term comes from unfolding the `n`-sum for `m≠0`. The integral is `sqrt(pi) Gamma(s-1/2)/Gamma(s)`, and summing `psi(m)m^{1-2s}` then dividing by `L(2s,psi)` gives (D3.5). Applying `W_q` a second time gives the other column. All operations converge absolutely for `Re s>1` and then continue meromorphically.
3. The Dirichlet functional equation gives
\[
 R_\psi(s)R_{\bar\psi}(1-s)=1,\qquad
 A_\psi(s)A_{\bar\psi}(1-s)=1.                         \tag{D3.9}
\]
Here `epsilon_psi epsilon_barpsi=1`. Multiplying the two off-diagonal matrices checks the required matrix functional equation exactly. On `Re s=1/2` each `A` has modulus one, so the matrix is unitary.
4. At `s=1`, both numerator and denominator in (D3.5) are regular and nonzero; the matrix residue is **zero**. Its off-diagonal value there is
\[
 A_\psi(1)=\frac{\pi}{q}\frac{L(1,\psi)}{L(2,\psi)}.    \tag{D3.10}
\]

For real `psi`, the fixed vectors `(1,±1)` diagonalize this block, giving **two** scalar channels `±A_psi`. For complex `psi`, this is still a two-cusp block within a **single** nebentypus; generally no fixed similarity diagonalizes it for every `s`. A fixed right swap does convert it into `diag(A_psi,A_barpsi)`, but that changes the incoming basis separately from the outgoing basis. It is useful for Hardy ranges, not a simultaneous eigenspace assertion. Consequently the asserted one-channel-per-character diagonalization is **REFUTED** even at a real quadratic character.

### D3.4. Trivial nebentypus — PROVED

Put `phi(s)=Lambda_0(2s-1)/Lambda_0(2s)`. Then
\[
 \boxed{\Phi_1(s)=\frac{\phi(s)}{q^{2s}-1}
 \begin{pmatrix}q-1&q^s-q^{1-s}\\q^s-q^{1-s}&q-1\end{pmatrix}},
                                                               \tag{D3.11}
\]
\[
 \phi_\pm(s)=\phi(s)\frac{1\pm q^{1-s}}{1\pm q^s},\qquad
 \det\Phi_1(s)=\phi(s)^2\frac{1-q^{2-2s}}{1-q^{2s}}.    \tag{D3.12}
\]
Proof: the oldforms `E(z,s), E(qz,s)` have incoming coefficient matrix `H(s)=[[1,q^s],[q^s,1]]` and outgoing coefficient matrix `phi(s) H(1-s)`. Thus `Phi_1=phi H(1-s)H(s)^{-1}`, giving these formulas. Since `phi(s)phi(1-s)=1` and the `H` matrices commute, this also proves the matrix functional equation. At exceptional parameters use meromorphic continuation.

The pole has rank-one residue
\[
 \operatorname*{Res}_{s=1}\Phi_1(s)
 =\frac{3}{\pi(q+1)}\begin{pmatrix}1&1\\1&1\end{pmatrix}.       \tag{D3.13}
\]
Indeed `Res_{s=1} phi=3/pi`; every finite matrix entry remaining at `s=1` equals `1/(q+1)`. This equals `1/vol(Y_0(q))` per entry, since its area is `(q+1)pi/3`.

**PROVED (squarefree trivial level).** Tensoring the two oldform choices at every `r|N` gives the factors
\[
 \Phi_{0,N}(s)=\phi(s)\bigotimes_{r\mid N}
 \frac1{r^{2s}-1}\begin{pmatrix}r-1&r^s-r^{1-s}\\r^s-r^{1-s}&r-1\end{pmatrix},
                                                               \tag{D3.14}
\]
up to ordering width-one cusps. This follows from the product incoming matrix `bigotimes H_r(s)`. With `h=2^{omega(N)}` its determinant is
\[
 \phi(s)^h\prod_{r\mid N}
 \left(\frac{1-r^{2-2s}}{1-r^{2s}}\right)^{h/2}.        \tag{D3.15}
\]
No nontrivial Dirichlet ratio appears. This proves the scope stated, with “squarefree” retained, in `report/sections/04o_graded_toys_exits.tex:157–168`.

### D3.5. Full prime-level determinant and the general theorem — SHARPENED

For `Gamma_1(q)`, Fourier transform on its two diamond orbits is unitary and gives the blocks (D3.6), (D3.11). Let `m=(q-1)/2`. Its determinant is
\[
 \det\Phi_{\Gamma_1(q)}(s)=
 \phi(s)^2\frac{1-q^{2-2s}}{1-q^{2s}}
 (-1)^{m-1}q^{(1-2s)(m-1)}
 \prod_{\substack{\psi\bmod q\ {
m even}\\\psi\ne1}}R_\psi(s)^2.
                                                               \tag{D3.16}
\]
This is a product with multiplicities, not a single copy of every `L`-function. In the width-one cusp basis the residue is the `h x h` all-ones matrix times
\[
 \frac1{\operatorname{vol}(Y_1(q))}=\frac6{\pi(q^2-1)},\qquad h=q-1. \tag{D3.17}
\]
The Fourier transform gives (D3.13) on the trivial block and zero on the rest, since each orbit has `m` elements.

**PROVED (precise classical structural input; Huxley 1984, “Scattering matrices for congruence subgroups”; Hejhal 1983, *The Selberg Trace Formula for PSL(2,R)* II, Ch. 11 for squarefree level; both not byte-cited).** At level `N`, weight zero and fixed even nebentypus `psi`, the Eisenstein space is spanned by primitive inducing pairs and their level raises. In the holomorphic-pair convention the labels are `(chi_1,chi_2,b)` with `cond(chi_1)cond(chi_2)|N`, `chi_1 chi_2=psi`, and `b|N/(cond(chi_1)cond(chi_2))`. The global intertwining factors have primitive completion ratios for the character inducing `chi_1 bar chi_2`; imprimitive Euler factors, local level matrices, conductor powers and Gauss constants remain. Weyl interchange in this holomorphic-pair convention is `(chi_1,chi_2) -> (chi_2,chi_1)`; it preserves nebentypus and conjugates the intertwining character. Thus block sizes include level multiplicities, and are not determined solely by the order of a character.

We use from Huxley/Hejhal **only this spanning/intertwining structure**, not an untranscribed all-level determinant formula. A primary accessible source with explicit change-of-basis formulas is [Young, *Explicit calculations with Eisenstein series*, 2017/2019, Theorems 6.1 and 7.1](https://arxiv.org/html/1710.03624v2#S6), **not byte-cited**. Its pair convention has nebentypus `eta_1 bar eta_2`; set `eta_1=chi_1`, `eta_2=bar chi_2`. Local factors include rational functions of `r^{-s}` and missing Euler factors `1-kappa(r)r^{-u}` at `r|N`, not just monomials. Taking determinants of the finite local matrices and of the Weyl permutation gives the determinant structure. **OPEN in this note:** the complete general-level local matrices and their determinant exponents have not been transcribed. The fully explicit prime-level statements requested as the minimum, and squarefree trivial-character statements, are proved above without that input. This is not an assertion that general congruence scattering is an unsolved classical problem.

## D4. Twisted theta edges and scalar inner functions — SHARPENED

Author: `codex:gpt-6-astra`

### D4.1. The two edges are not two nonzero terms at one cusp — PROVED

For a primitive nontrivial **even** character `chi` of conductor `f`, define
\[
 \theta_\chi(v)=\sum_{n\in\mathbb Z}\chi(n)e^{-\pi n^2v/f},\qquad
 \mathcal T_\chi(z,t)=\sum_{m,n\in\mathbb Z}\chi(n)
           e^{-\pi t|fmz+n|^2/(fy)}.                  \tag{D4.1}
\]
Unlike the brief's unqualified twist by `chi(n)`, this level-scaled lattice sum is periodic in `x` with period one. Its Mellin transform is
\[
 \frac12\int_0^\infty\mathcal T_\chi(z,t)t^s\frac{dt}{t}
 =\Lambda_\chi(2s)E_\infty^{\bar\chi}(z,s)
 \quad(\Re s>1),                                    \tag{D4.2}
\]
where the series on the right is (D3.3) with `q=f`. Proof: termwise Gaussian Mellin integration, grouping by the positive gcd, gives the factor `L(2s,chi)`; the remaining primitive sum is exactly `E_infinity^bar chi`. Analytic continuation gives the continued identity.

At the two width-one cusp coordinates, direct averaging gives
\[
 \int_0^1\mathcal T_\chi(x+iy,t)\,dx=\theta_\chi(t/y),\qquad
 \int_0^1\mathcal T_\chi(W_f(x+iy),t)\,dx
       =\sqrt{y/t}\,\theta_\chi(fty).                 \tag{D4.3}
\]
For the first formula `m=0` gives the answer and `m≠0` averages a nontrivial character to zero over full periods. For the second, substitution by `W_f` converts the sum to `sum chi(m) exp(-pi t |mz+n|^2/y)`; `m=0` vanishes and the ordinary Gaussian `n`-sum unfolds to `sqrt(y/t)`. Consequently the Mellin edges are
\[
 \Lambda_\chi(2s)y^s,\qquad
 f^{1/2-s}\Lambda_\chi(2s-1)y^{1-s}.                 \tag{D4.4}
\]
Their quotient, including the conductor power, is exactly `A_chi(s)` in D3. This is a direct GL1 theta-edge derivation of the endpoint scattering entry.

**REFUTED (the literal two-term assertion).** For a nonprincipal primitive character, the incoming series has only its incoming term at infinity; its outgoing coefficient there is zero. The other edge is at the other cusp. A universal nonzero sum of incoming and outgoing terms at the *same* cusp is false. At level one the zero character average is replaced by a nonzero average, producing both terms, as proved in `report/sections/04r_h_theta_channels.tex:19–31` and `notes/h-theta/astra-proofs.md:534–627`.

For comparison with the weighted involution, introduce the symmetrically scaled edges
\[
 A_\chi(t;y)=\theta_\chi(t/y),\qquad
 B_\chi(t;y)=\sqrt{y/t}\theta_\chi(ty),\qquad
 (\mathcal WF)(t)=t^{-1}F(1/t).                       \tag{D4.5}
\]
The physical second edge in (D4.3) is `sqrt(f) B_chi(ft;y)`, not `B_chi(t;y)`. If an actual second theta representative is wanted, `f^{-1/2} sum_{m,n} chi(m) exp(-pi t|mz+n|^2/(fy))` has constant term `B_chi(t;y)`. It is a different lattice sum with different normalization.

**PROVED (Poisson, with all constants).** Finite Fourier inversion gives
\[
 \theta_\chi(v)=\epsilon_\chi v^{-1/2}\theta_{\bar\chi}(1/v),
 \quad \mathcal W A_\chi=\epsilon_\chi B_{\bar\chi},
 \quad \mathcal W B_\chi=\epsilon_\chi A_{\bar\chi}.   \tag{D4.6}
\]
To see the constant, apply Poisson to each residue class `n mod f`; its Fourier coefficient is `tau(chi) bar chi(k)`, and the Gaussian transform contributes `1/sqrt(fv)`. These formulas also give `W^2=1` because `epsilon_chi epsilon_bar chi=1`. The symmetrically scaled Mellin edges are
\[
 \frac12\int_0^\infty A_\chi(t;y)t^s\frac{dt}{t}
   =\Lambda_\chi(2s)y^s,\qquad
 \frac12\int_0^\infty B_\chi(t;y)t^s\frac{dt}{t}
   =\Lambda_\chi(2s-1)y^{1-s}.                       \tag{D4.7}
\]
These edge integrals converge for every complex `s`: a nontrivial primitive theta decays exponentially at both endpoints by Poisson. The same-character outgoing transform can be rewritten as `epsilon_chi Lambda_bar chi(2-2s)y^{1-s}`. Replacing it by `epsilon_chi Lambda_bar chi(2s-1)y^{1-s}` would be wrong. Thus the functional equation exchanges the character **and** the Mellin argument.

### D4.2. Odd characters — REFUTED in weight zero; PROVED with the correct GL1 parity

If `chi(-1)=-1`, the unsigned Gaussian sums in (D4.1) cancel term by term under `(m,n)->(-m,-n)`: they are identically zero. A weight-zero automorphic function of odd nebentypus on `Gamma_0(f)` would obey `F(z)=-F(z)` under `-I`, hence vanish. In particular there is **no weight-zero two-by-two scattering matrix for the order-four character modulo 5**. This also excludes odd diamond characters from scalar functions on `Gamma_1(N)\H`, since the effective diamond group quotients by `±1`.

The nonzero GL1 replacement, for parity `a=0,1`, is
\[
 \theta_{\chi,a}(v)=\sum_n n^a\chi(n)e^{-\pi n^2v/f},\qquad
 \theta_{\chi,a}(v)=\epsilon_\chi v^{-a-1/2}\theta_{\bar\chi,a}(1/v),
\]
\[
 \frac12\int_0^\infty\theta_{\chi,a}(v)v^{(u+a)/2}\frac{dv}{v}
       =\Lambda_\chi(u).                              \tag{D4.8}
\]
Differentiate the Gaussian Fourier transform once for `a=1`; its factor `-i` is exactly the `i^{-a}` in `epsilon_chi`. These identities yield all primitive Dirichlet functional equations. Odd characters require an odd automorphic weight (for example weight one), with an additional archimedean intertwining factor. Formulas (D3.5)–(D3.6), if fed the odd completion, still make a formal matrix satisfying a functional equation; this algebraic coincidence does **not** make it weight-zero scattering.

### D4.3. The correct inner quotient for complex characters — PROVED

Define, for any primitive nonprincipal character, including odd ones as an abstract GL1 construction,
\[
 E_\chi(\tau)=\Lambda_{\bar\chi}(1-2i\tau),\qquad
 \Theta_\chi(\tau)=\frac{E_\chi^\#(\tau)}{E_\chi(\tau)}
 =\frac{\Lambda_\chi(1+2i\tau)}{\Lambda_{\bar\chi}(1-2i\tau)},
 \quad E^\#(\tau)=\overline{E(\bar\tau)}.              \tag{D4.9}
\]
Then
\[
 \Theta_\chi(\tau)=\epsilon_\chi
 \frac{\Lambda_\chi(1+2i\tau)}{\Lambda_\chi(2i\tau)},\qquad
 A_\chi(1/2+i\tau)=f^{-i\tau}\epsilon_\chi\Theta_\chi(\tau)^{-1}
                                                               \tag{D4.10}
\]
in the even scattering case. Thus the inverse physical scattering entry has the inner delay factor `exp(i tau log f)` as well as the pure arithmetic factor `Theta_chi`. Removing this delay is a choice of cusp origins, not an identity with the width-one matrix unchanged.

The conjugation placement matters. If one instead defines `E_chi=Lambda_chi(1-2i tau)`, the inner quotient is `E_chi^#/E_chi` with numerator carrying **bar chi**. The brief's suggested `E_bar chi^#/E_chi` then has numerator and denominator both carrying `chi`, and generally is **not unimodular** on the real line for a complex character. Our notation labels `Theta_chi` by the zeros of `L(u,chi)`.

Here is an unconditional proof of innerness and absence of a singular factor.

1. The denominator has no zero in the closed upper half-plane, by `Re(1-2i tau)>=1`. The numerator zeros are
\[
 w_\rho=\frac{\gamma}{2}+\frac{i(1-\sigma)}2,
 \qquad \rho=\sigma+i\gamma,\quad L(\rho,\chi)=0.      \tag{D4.11}
\]
They all lie strictly in the upper half-plane, with multiplicities preserved. The denominator zeros are their conjugates. This uses `rho -> 1-bar rho` within the same character's zero set, obtained by combining functional equation and complex conjugation.
2. Choose a square root of `epsilon_chi` and put `H_chi(z)=epsilon_chi^{-1/2} Lambda_chi(1/2+iz)`. The functional equation makes `H_chi` real entire, of order one; its zeros lie in `|Im z|<1/2`. Its genus-one Hadamard product can be grouped into real zeros and conjugate pairs, with a real linear exponential exponent. In `H_chi(2 tau-i/2)/H_chi(2 tau+i/2)`, each real-zero factor is a Blaschke factor and each conjugate-pair factor is a product of two Blaschke factors: all shifted numerator zeros lie above, and denominator zeros are their reflections below. The exponential corrections in each group and the real linear exponent have modulus one in this quotient. Local convergence of the Hadamard product proves `|Theta_chi(tau)|<=1` for `Im tau>0`. Nonconstancy makes this inequality strict. This proves the Hermite–Biehler property of `E_chi` without GRH.
3. The zero count gives `sum Im(w_rho)/(1+|w_rho|^2)<infinity`. Meromorphic continuation through every finite real point excludes singular measure there. The only possible remaining inner factor is a delay `exp(i a tau)`, `a>=0`. On the positive imaginary axis the functional equation and Stirling give
\[
 \Theta_\chi(iv)=\epsilon_\chi
 \frac{\Lambda_{\bar\chi}(2v)}{\Lambda_{\bar\chi}(1+2v)}
 \sim\epsilon_\chi\sqrt{\frac{\pi}{fv}},\qquad v\to\infty.       \tag{D4.12}
\]
An inner delay with `a>0` would imply `|Theta_chi(iv)|<=exp(-av)`, a contradiction. Therefore `Theta_chi` is pure Blaschke, up to a constant phase.

For the trivial character replace the meromorphic completion by the entire `xi`: `Theta_1(tau)=xi(1+2i tau)/xi(1-2i tau)`. The extra pole-removing factor `r(tau)=(tau-i/2)/(tau+i/2)` is precisely the one in `notes/h-theta/astra-proofs.md:191–278` and `report/sections/04r_h_theta_channels.tex:34–52`. Uetake's actual convention is locally explicit at `refs/src/uetake-2007/paper.txt:615–629,634–680`: his reduced causal factor is `xi(2s)/xi(-2s)`, not an assertion that every choice of radiation spaces yields the same unreduced symbol.

**SHARPENED (binding).** The edge identity is an equality of Mellin/scattering symbols. It does not resurrect the refuted theta cyclic-space construction: `report/sections/04q_h_theta.tex:110–129` and `notes/h-theta/astra-proofs.md:280–372` distinguish the Gaussian orbit from the prescribed Hardy range. Nor does it identify Burnol's bad-zero defect with this all-zero model; see `notes/h-theta/astra-proofs.md:475–509` and the primary local formula `S=V^2B^{-2}` in `refs/src/math/0001013/main.tex:509–514` (adelic version `:694–699`).

## D5. What the level channel actually decomposes into — SHARPENED

Author: `codex:gpt-6-astra`

### D5.1. A concrete prime-level inner model — PROVED

Fix `q=ell>=5`, `s=1/2+i tau`, `Im tau>0`. As in the notebook's level-one convention, use the **inverse** of the Eisenstein coefficient matrix and remove its upper-half-plane bound-state pole. Calling `Phi` itself the upper-half-plane inner symbol reverses the scattering orientation; compare `report/sections/04i_cusp_graph_scattering.tex:100–112` and `04r_h_theta_channels.tex:27–31`.

Put
\[
 u=e^{i\tau\log q},\quad a=q^{-1/2},\quad
 b_c(u)=\frac{u-c}{1-cu},\quad
 L_+(\tau)=u b_{-a}(u),\quad L_-(\tau)=u b_a(u),\quad
 r(\tau)=\frac{\tau-i/2}{\tau+i/2}.                    \tag{D5.1}
\]
Here `L_±` means an elementary local **inner factor**, not a Dirichlet L-function. Formula (D3.12) yields
\[
 \phi_\pm(1/2+i\tau)^{-1}=r(\tau)^{-1}\Theta_1(\tau)L_\pm(\tau).
                                                               \tag{D5.2}
\]
The zero of `L_-` at `tau=i/2` cancels `r^{-1}`; `L_+` has no zero there. Multiply the plus channel by `r` to remove its one bound-state pole. The resulting two inner entries are
\[
 I_+=\Theta_1 L_+,\qquad I_-=\Theta_1 L_-/r.          \tag{D5.3}
\]
`L_-/r` is inner because one simple Blaschke divisor has been removed from an inner function. For every nontrivial even `psi`, (D3.6), (D4.10) give, up to constant phases and a right permutation, the two inner entries
\[
 I_{\psi,1}=e^{i\tau\log q}\Theta_\psi(\tau),\qquad
 I_{\psi,2}=e^{i\tau\log q}\Theta_{\bar\psi}(\tau).    \tag{D5.4}
\]
These formulas explicitly construct a matrix inner model for prime-level inverse scattering after the specified residual reduction. Calling it the model uses the definition `K_I=H^2(C^h) ⊖ I H^2(C^h)`; it is not identified with D1's finite-dimensional cohomology.

Constant left unitary transformations carry model spaces unitarily to one another; constant right unitaries do not change their Hardy ranges. Therefore
\[
 K_q^{\rm scat}\simeq K_{I_+}\oplus K_{I_-}\oplus
 \bigoplus_{\substack{\psi\ {\rm even}\bmod q\\\psi\ne1}}
 (K_{e^{i\tau\log q}\Theta_\psi}\oplus K_{e^{i\tau\log q}\Theta_{\bar\psi}}).
                                                               \tag{D5.5}
\]
This includes local factors and delays. If one **defines a further arithmetic reduction** by deleting those factors, then after relabeling conjugates,
\[
 K_q^{\rm arith}\simeq
 \bigoplus_{\chi\ {\rm even}\bmod q}K_{\Theta_\chi}^{\oplus2}.
                                                               \tag{D5.6}
\]
It is **two copies**, not one, even for trivial and quadratic characters. Equation (D5.6) is not equality with (D5.5). In general `K_AB=K_A ⊕ A K_B`, so discarded factors carry additional states. The delay `exp(i tau log q)` has model space `L^2(0,log q)` in the Fourier picture and has no zeros; its states cannot be listed as L-zero jets. The local factors have additional periodic zeros at height `1/2`; the zero at `i/2` in the minus factor is the canceled one. Thus “the full divisor is only the union of L-zero sets” is **REFUTED**.

At `q=5` there are four cusp coordinates: two zeta channels and two quadratic-character channels, and no odd-character channels. This is a complete small-level counterexample to the requested indexing and multiplicities.

### D5.2. Exit rank, and which clock — PROVED

For any square matrix inner function on the disk, let `Z=P_K M_w|K` and define `J` as in `report/sections/04l_elliptic_cavity_channel.tex:22–28`. Directly,
\[
 I-Z^*Z=J^*J,\qquad J^*e=\frac{\Theta(w)-\Theta(0)}w e,
 \qquad JJ^*=I-\Theta(0)^*\Theta(0).                  \tag{D5.7}
\]
The middle formula follows by taking inner products with `wf`; its numerator divided by `w` belongs to `K`. Its norm is the norm of `Theta e` minus its constant Fourier coefficient, proving the last identity. Consequently
\[
 \operatorname{rank}J=\operatorname{rank}(I-\Theta(0)^*\Theta(0))\le h.
                                                               \tag{D5.8}
\]
Equality requires no constant isometric direction. It does not follow from `h` nominal rays: `Theta=diag(theta,1)` with `theta` nonconstant has rank one and two nominal exits. The notebook itself has a constant Dirichlet channel with zero model space, `report/sections/04l_elliptic_cavity_channel.tex:93–106`.

For the **specific** prime-level symbols (D5.3)–(D5.4), every scalar entry is nonconstant inner, hence has modulus strictly less than one at any interior basepoint. After a Cayley transform to the disk, (D5.8) gives **exactly `rank J=q-1=h`**. The same holds for (D5.6). This is one exit per scalar multiplicity coordinate, not per character or per zero. An arbitrary-level analogue requires its local matrices and the same purity check.

**SHARPENED (continuous time).** The disk shift is a **cogenerator** convention, not a fixed positive-time slice of dilation. In logarithmic coordinates the adjoint semigroup on a scalar model restricts `C_t f(X)=f(X+t)`, and
\[
 \|f\|^2-\|C_tf\|^2=\int_0^t|f(X)|^2dX,\qquad
 -2\Re\langle Af,f\rangle=|f(0)|^2                   \tag{D5.9}
\]
for generator-domain vectors with a trace at zero. The generator boundary form has one exit per scalar coordinate; evaluation is not bounded on all of `L^2(0,infinity)`. With infinitely many distinct exponential modes the finite-time defect has **infinite rank**, since their restrictions to `[0,t]` are linearly independent. Thus the claim `rank(I-C_t^*C_t)=h` for positive times is false. The finite-cavity identity cannot be imported with the clock changed silently.

### D5.3. Modes, diamonds, and the “even sector” — SHARPENED

For a **pure arithmetic factor** `Theta_chi` of D4 the mode and jet theorem is
\[
 \mathcal M^{-1}K_{\Theta_\chi}=
 \overline{\operatorname{span}}\{(\log y)^j y^{-(1-\sigma)/2-i\gamma/2}1_{y>1}:
 L(\sigma+i\gamma,\chi)=0,\quad0\le j<m_\rho\}.       \tag{D5.10}
\]
The Fourier convention is `hat f(tau)=int f(e^X)e^{i tau X}dX`, with boundary measure `d tau/(2 pi)`. Indeed `(tau-bar w)^{-j-1}` transforms back to `(-i)^{j+1}X^j e^{-i bar w X}/j!`; the ordinary mode evolves under the **adjoint** compression by
\[
 C_t m_\rho=e^{-(1-\sigma)t/2-i\gamma t/2}m_\rho.      \tag{D5.11}
\]
Divisibility by the pure Blaschke product proves completeness of all jets: an orthogonal vector vanishes at every zero to full order and lies in both `Theta H^2` and its complement. The functions `Theta/(tau-w)^j` supply a biorthogonal system. This is the proof in `notes/h-theta/astra-proofs.md:675–778`, with D4 supplying the character version of the pure Blaschke result. Uniform damping by `y^{-1/4}` holds **iff GRH for the represented character**, not unconditionally. The full scattering model's delay states are outside this jet list.

For a function transforming by nebentypus `psi`, a diamond `<d>` acts by `psi(d)`. Both coordinates of the `psi` block have this action, although their L-factors have labels `psi` and `bar psi`. More generally the diamond label is `chi_1 chi_2`, whereas the intertwining L-character is `chi_1 bar chi_2`. These labels differ. Thus “L-character = diamond character, one channel each” is **REFUTED**.

Only the principal **primitive completed L-function** has poles; nonprincipal completions are entire. Together with the unique constant residual automorphic eigenfunction, this supports an optional pole-even/zero-odd **virtual grading of L-functions**. It does not turn all Eisenstein cohomology into that even part. The weight-two Eisenstein classes in D2 exist for nontrivial characters and their local roots have moduli `1,p` by (D2.8), although their completed Dirichlet L-functions have no poles. They belong to a different object. At prime level the scattering residue has rank one, while `dim Eis=q-2`; these dimensions cannot be reconciled by identifying the spaces.

### D5.4. What positivity can imply — PROVED with the specified scope

On a finite, functional-equation-stable selection of **arithmetic zero modes**, include complete Jordan chains and conjugate/dual partners. Let `A` be the generator in (D5.11) and put `D=A+1/4`. Its eigenvalues are
\[
 d_\rho=(\sigma-1/2)/2-i\gamma/2.                    \tag{D5.12}
\]
A positive metric making `exp(tD)` unitary for **every real t** exists iff all selected zeros are on the critical line and every Jordan chain has length one. Test an eigenvector for necessity, then observe polynomial growth in a nontrivial Jordan chain. For sufficiency make an eigenbasis orthonormal. Repeating a simple zero in two independent cusp multiplicity coordinates causes no Jordan obstruction; a multiple analytic zero in one scalar factor does.

This is the infinitesimal version of `notes/deninger-lps/src/manuscript.txt:540–545`: for a specified real symplectic `F` with `F^t Omega F=q Omega`, positive compatibility is equivalent to **semisimplicity plus critical-circle spectrum**. It is not “simple spectrum”: repeated semisimple eigenvalues are allowed. A functional-equation pairing would pair `(chi,rho)` with `(bar chi,1-rho)`, for which (D5.12) changes sign. One can define a pairing on formal paired spectral lines and their nondegenerate symplectic finite sums. The scalar functional equation does not produce a geometric Poincaré pairing on the Hardy space. **OPEN:** a natural arithmetic pairing and a specified topology realizing that further identification.

On the algebraic direct sum of arithmetic modes, a positive diagonal spectral completion exists iff all **represented** L-functions satisfy GRH and have simple zeros. Weight-zero `Gamma_1(N)` at prime level does not represent odd characters, so this is not GRH for *all* characters modulo `N`. The criterion also does not apply unchanged to the full space (D5.5), with local modes and delay states. It proves neither GRH nor simplicity.

### D5.5. No boundedly equivalent arithmetic metric — PROVED

Assume GRH and simplicity for one represented primitive character. Its zero kernels have height `b=1/4`. Two normalized kernels satisfy
\[
 |\langle\widetilde k_{a+ib},\widetilde k_{a'+ib}\rangle|
 =\frac{2b}{\sqrt{(a-a')^2+4b^2}}.                    \tag{D5.13}
\]
The `T log T` zero count forces distinct ordinates with gaps tending to zero; a uniform positive gap would give only `O(T)` zeros. Thus this overlap tends to one and there is no uniform Riesz lower bound. Without simplicity, a multiple zero already prevents unitary centered evolution. For the natural jet system, unbounded multiplicities also give consecutive normalized jet overlaps `sqrt((2j+1)/(2j+2))->1`. This proves the character extension of `report/sections/04r_h_theta_channels.tex:94–105`; the full sibling argument is `notes/h-theta/astra-proofs.md:733–780`.

If a bounded and **boundedly invertible** positive metric made centered evolution unitary, its eigenvectors with distinct frequencies would be orthogonal in that equivalent norm. Unit vectors in an equivalent norm cannot have phase-adjusted differences tending to zero while mutually orthogonal. This contradicts (D5.13). A single scalar summand obstructs such a metric on the level model. The correct conclusion is “no uniformly positive bounded metric equivalent to the Hardy norm,” not “no bounded positive operator of any kind.” A bounded operator without a lower bound defines a different topology and is not excluded. **OPEN here:** any stronger assertion allowing those norm comparisons.

A spectral completion making all modes orthonormal also changes the exit: under GRH `C_t=e^{-t/4}U_t` would have generator loss `I/2` and finite-time loss `(1-e^{-t/2})I`, of infinite rank. This is the infinite-dimensional counterpart of the four-mode/one-exit obstruction in `report/sections/04l_elliptic_cavity_channel.tex:157–175`.

## Numerical checks for the blind lane

Author: `codex:gpt-6-astra`

**PROVED (formulas); SHARPENED (numerical evidence, not a zero-location proof).** Reproduce with `python3 notes/deninger-cusp/checks/verify.py` and `python3 notes/deninger-cusp/checks/extended.py`. The first uses 45-digit mpmath arithmetic; the second independently integrates the finite Gaussian lattice sums with NumPy and checks the local-factor identities for `N=5,7,11,13`. Reported decimal values are rounded, not interval certificates. Matrix functional-equation errors in the first run were below `8e-46`; independent theta integration errors were below `4e-16`. These checks do not prove GRH, simplicity, or the ordering of all complex zeros.

### N1. Scattering matrices — PROVED formulas and reproducible values

Let `chi_{q,k}(g)=exp(2 pi i k/(q-1))`, where `(q,g)=(5,2),(7,3),(13,2)`. In the table each pair `(a,b)` specifies the whole matrix `[[0,a],[b,0]]` in (D3.6).

| Character | `s=0.7+0.3i`: `(a,b)` | `s=1.2+0.4i`: `(a,b)` |
|---|---|---|
| `chi_{5,2}=(./5)` | `(0.570396241478-0.370987747919i, same)` | `(0.188174397267-0.180015889034i, same)` |
| `chi_{7,2}`, even order 3 | `(0.435438660235-0.438482464585i, 0.499568861119-0.371294296554i)` | `(0.100947189666-0.156910809998i, 0.123084043639-0.147015786831i)` |
| `chi_{13,2}`, even order 6 | `(0.336061944278-0.402833597027i, 0.251844978419-0.453521926397i)` | `(0.040521235773-0.098440230048i, 0.024339946416-0.099396432859i)` |

For every row test `Phi_chi(s) Phi_chi(1-s)=I`, without conjugating `s` in that expression. Independently test (D3.7) using Gauss sums. Their root numbers are respectively `1`, `0.895953219663-0.444148430342i`, and `0.859542535099+0.511064213535i`.

For trivial character modulo 5, (D3.11) is the symmetric matrix `[[d,o],[o,d]]` with

| `s` | `d` | `o` |
|---|---|---|
| `0.7+0.3i` | `-0.779956675205-0.082416806284i` | `-0.207902204851-0.452750031374i` |
| `1.2+0.4i` | `-0.118871445339-0.189987827354i` | `0.070583992790-0.370524601121i` |

**REFUTED (requested odd-character scattering test).** For `chi_{5,1}(2)=i`, `chi(-1)=-1`; the weight-zero scattering matrix is undefined. For diagnostic purposes only, feeding its **odd completion** into the formal matrix (D3.6) produces
\[
 B(0.7+0.3i)=\begin{pmatrix}
 0&0.584013007860-0.328765368425i\\
 0.509530467411-0.425768800372i&0
 \end{pmatrix},
\]
\[
 B(1.2+0.4i)=\begin{pmatrix}
 0&0.188057057618-0.162578185622i\\
 0.155797669970-0.182752006783i&0
 \end{pmatrix}.                                      \tag{N.1}
\]
This artificial `B` satisfies `B(s)B(1-s)=I` because the primitive functional equation does, with `epsilon=0.850650808352+0.525731112119i`. It is **not** an automorphic weight-zero scattering matrix. A lane that obtains such a matrix from the zero theta sum has detected a normalization/representation error, not verified the brief.

### N2. Twisted theta at `y=1.3,t=0.7` — PROVED formulas and reproducible values

Use exactly (D4.1), including its factor `f` in both the lattice and the Gaussian denominator. The incoming constant is `A_chi=theta_chi(t/y)`; the **physical cusp-zero constant** is `C_chi=sqrt(y/t)theta_chi(f t y)`. The symmetrically scaled edge used for the involution is the distinct quantity `B_chi=sqrt(y/t)theta_chi(t y)`.

| Character | `A_chi` | `C_chi` (physical) | `B_chi` (symmetric scaling) |
|---|---|---|---|
| `chi_{5,2}` | `0.822880294170` | `0.156238589167` | `1.246242825365` |
| `chi_{7,2}` | `1.053699131048-0.429880215401i` | `0.156253315445-0.000025506630i` | `1.509098455595-0.397658610120i` |
| `chi_{13,2}` | `1.848617210324+0.689306227046i` | `0.156282767983+0.000025506630i` | `2.513603987405+0.722293789760i` |
| `chi_{5,1}` (odd, unsigned sum) | `0` exactly | `0` exactly | `0` exactly |

For the odd **GL1 replacement** with an `n` factor, `theta_{chi_{5,1},1}(0.7/1.3)=1.390329535856+0.747945730562i`. Test (D4.8), not the even Poisson formula, for that vector. The physical constants in the table were checked against direct averaging of both lattice sums, independently of Poisson and L-values.

### N3. Residues — PROVED

At `s=1`, the nontrivial blocks have residue zero. The quadratic block has off-diagonal finite value `A_chi(1)=0.382936203162541402645`; the corresponding values for `chi_{7,2}` and `chi_{13,2}` are `0.304559716357-0.020318397407i` and `0.199607864326+0.016349433840i`. For the trivial block of `Gamma_0(5)`, every residue entry is `1/(2 pi)=0.159154943091895335769`. For the full four-cusp `Gamma_1(5)` matrix in its cusp basis, every residue entry is `1/(4 pi)=0.079577471545947667884`; its rank is one, not four or three.

**SHARPENED (mpmath pitfall).** Floating roots of unity can have a tiny nonzero character sum. Evaluating the sum of Hurwitz zeta poles at `s=1` through `mpmath.dirichlet` can then give a grossly incorrect finite value and excessive precision growth. For a nonprincipal character evaluate the canceled formula
\[
 L(1,\chi)=-\frac1f\sum_{r=1}^{f-1}\chi(r)\,\psi_0(r/f),        \tag{N.2}
\]
where `psi_0` is the digamma function. This follows by canceling the common pole in the Hurwitz-zeta expansion. The script uses this formula; the residues themselves are proved analytically above.

### N4. Quadratic conductor-5 modes — PROVED formula; numerical roots

The first two positive-ordinate critical roots found by the Hardy-function scan are
\[
 \rho_1\simeq\tfrac12+6.648453344727714716123i,\qquad
 \rho_2\simeq\tfrac12+9.831444432886669616348i.          \tag{N.3}
\]
The script scans in increments `0.1` and refines sign changes; it is not an argument-principle certification excluding off-line or missed multiple roots. The computed L-residuals were below `1.1e-45`. Their model zeros are `w_1=3.324226672363857358062+i/4`, `w_2=4.915722216443334808174+i/4`. For modes normalized as `m_j(y)=y^{-1/4-i Im(rho_j)/2}1_{y>1}` (the irrelevant common Fourier factor `-i` suppressed),
\[
 m_1(1.3)\simeq0.602342616987-0.717106262048i,\qquad
 m_2(1.3)\simeq0.259788594167-0.899759915560i.          \tag{N.4}
\]
Test `C_t m_j=exp(-t/4-i t Im(rho_j)/2)m_j`, and the kernels `(tau-bar w_j)^{-1}`. These are modes in **both** quadratic multiplicity coordinates of the conductor-5 prime-level reduction, not one independently exiting mode per zero.

### N5. `N=11`, Eisenstein `T_2,T_3` — PROVED exact answers

There are `h=10` cusps and `dim Eis=9`. Let `zeta_5=exp(2 pi i/5)` and choose the even characters `chi_k(2)=zeta_5^k`, `k=1,2,3,4`. Since `3=2^8 mod 11`,
\[
 \operatorname{spec}(T_2|\mathrm{Eis})=
 \{3\}\cup\{1+2\zeta_5^k,\ 2+\zeta_5^k:1\le k\le4\},
\]
\[
 \operatorname{spec}(T_3|\mathrm{Eis})=
 \{4\}\cup\{1+3\zeta_5^{3k},\ 3+\zeta_5^{3k}:1\le k\le4\}.     \tag{N.5}
\]
The exponents `3k` permute the nonzero residues modulo 5, so for either `p=2,3` the characteristic polynomial is the compact exact expression
\[
 \det(x-T_p|\mathrm{Eis})=
 \left(\sum_{j=0}^4(x-p)^j\right)((x-1)^5-p^5).       \tag{N.6}
\]
It has degree nine and trace `4(p+1)`, respectively `12,16`, not `9(p+1)`. For example the nontrivial `T_2` eigenvalues are the four conjugate pairs `1.618033988750±1.902113032590i`, `-0.618033988750±1.175570504585i`, `2.309016994375±0.951056516295i`, and `1.190983005625±0.587785252292i`. The supplied script prints both full multisets and the expanded polynomials. This is a decisive check against `T_p=(p+1)I`.

## Corrections to the brief

Author: `codex:gpt-6-astra`

| Item | Verdict | Correction |
|---|---|---|
| Product geometry | REFUTED | `H x T` is three-dimensional; `SL_2` has two tree vertex types. |
| `p+1` quotient edges | SHARPENED | These are sheets of the edge-to-vertex coverings; the quotient tree has one edge. |
| Leafwise `H^1=H^1(Y)` | SHARPENED | True for a chosen vertex slice; full horizontal cohomology needs its coefficient system and transverse regularity. |
| Eisenstein `T_p=p+1` | REFUTED | Only the trivial inducing pair has that universal value; use `chi_1(p)+p chi_2(p)`. |
| Full Bass double is Frobenius | REFUTED | Dimension doubles incorrectly and the diamond determinant is missing. |
| Weak Ramanujan suffices for a companion metric | REFUTED | Equality creates a Jordan block; the companion requires the strict bound. |
| Poincaré form equals doubled form canonically | REFUTED | A chosen cyclic two-plane admits a proportionality; no identification of the claimed full spaces exists. |
| Petersson is already the doubled invariant metric | REFUTED | It supplies the base metric in the self-adjoint case; the companion metric has cross terms. |
| Ordinary open-curve cup radical is `Eis` | REFUTED | Ordinary cup is zero on all `H^1(Y)`; the mixed compact-support pairing is perfect. |
| Boundary radical | SHARPENED | It is in homological intersection or the degenerate compact-support form; a split cohomological form may be defined. |
| Eisenstein = even poles = exits | REFUTED | Dimensions `h-1`, residual rank one, exit multiplicity `h`, and even cohomological degrees differ. |
| LPS has no poles/radical and positivity everywhere | REFUTED | It already has even poles and an odd-dimensional horizontal precursor; its positive pairing is constructed on the odd double. |
| `Gamma_1` cusp parametrization | REFUTED | The brief uses the `Gamma_0` count; use (D3.1). |
| Cusps form a canonical class group over `Q` | REFUTED | At prime level they are two diamond torsors, not the Picard group in 04p. |
| One scalar channel per character | REFUTED | Prime level has two cusp multiplicity coordinates per even nebentypus. |
| Inverse-character blocks explain every `2x2` block | REFUTED | Prime-level two-cusp blocks exist even for real characters and remain within one nebentypus. |
| Scattering finite factors are monomials | REFUTED | Already the trivial prime block has the rational factors in (D3.12). |
| Same theta has two nonzero constant terms at infinity | REFUTED | Nontrivial primitive twists have a zero character average; the two edges are at different cusps. |
| Mixed-character edge ratio | SHARPENED | Conjugation must accompany `u -> 1-u`; (D3.7), (D4.9) fix both conventions. |
| Order-four character mod 5 in weight zero | REFUTED | It is odd; unsigned Gaussian sums and weight-zero automorphic functions vanish. |
| Raw complex-character quotient is automatically inner | REFUTED | Use the conjugated denominator in (D4.9); the corrected arithmetic symbol is pure inner. |
| Full level model consists only of zero jets | REFUTED | Local factors and delays add states; (D5.6) is a separately defined arithmetic reduction. |
| Exit rank automatically equals number of cusps | SHARPENED | Equality requires purity; proved here for the specified prime-level cogenerator models. |
| Continuous-time rank equals discrete defect rank | REFUTED | The generator has a boundary form; fixed-time defects may have infinite rank. |
| Diamond label equals L-character | REFUTED | They are respectively `chi_1 chi_2` and `chi_1 bar chi_2`. |
| “Only the trivial character has even poles” identifies all Eisenstein classes | REFUTED | It is a statement about primitive completed L-functions, not degree-one boundary cohomology. |
| Positivity iff GRH plus simple spectrum | SHARPENED | For zero jets use GRH plus no nontrivial Jordan chains; independent repeated packets are allowed. |
| No bounded positive metric whatsoever | SHARPENED | The proved obstruction excludes boundedly equivalent/coercive metrics. |
| Poles of `xi` | REFUTED | `xi` is entire; `Lambda_0` has the pole pair. |
| H-ARITH and Galois/Shor bond fully settled | REFUTED | Classical coefficient factorization does not supply the claimed indexing, geometric pairing, or BC/Shor intertwiner. |

## D6. Consequences — SHARPENED

Author: `codex:gpt-6-astra`

**PROVED over Q:** prime-level scattering and its determinant are explicitly (D3.6), (D3.11), (D3.16), with the theta-edge derivation (D4.1)–(D4.7). Squarefree trivial-character `Gamma_0` scattering sees only the completed zeta ratio and local rational factors. **REFUTED as a Q theorem:** the literal analogue of `asm:h-arith-gamma1` in `report/sections/04o_graded_toys_exits.tex:171–177`, asserting one diagonal monomial-times-L channel for every Dirichlet character. It must be replaced by inducing-pair/multiplicity blocks, allowed archimedean parity, and explicit local matrices. The classical structural coefficient part is known; the all-level local transcription is outside the explicit computations of this note. The statement of `conj:galois-graded-bond` at `report/sections/10_open_problems_dead_routes.tex:81–93` still has an incorrect `Gamma_0` premise. Its stronger assertion of a BC/Shor action on the scattering bond remains **OPEN**, not implied by diagonalizing diamonds; the missing comparison map is already identified in `report/sections/04d_bc_symmetry_generators.tex:220–231`.

**SHARPENED over F_q[T]:** the double-coset correspondence, inducing-character bookkeeping, constant-term intertwining, finite Fourier transform, and finite-dimensional defect algebra have analogues. The real Gaussian, gamma factor, logarithmic continuous clock, and `T log T` argument do not transfer verbatim to a tree quotient. A cubic-level calculation must specify the subgroup including determinant and scalar-center conditions, singular cusps, cusp heights, local new/old bases, and the infinity representation. One cannot include all characters in an unramified scalar infinity model without checking their restrictions to `F_q^x`.

**PROVED (precise classical input, Rosen 2002, not byte-cited):** for a primitive nontrivial Dirichlet character of conductor degree `d` over `F_q[T]`, the finite polynomial `L(u,chi)` has degree `d-1`. If `chi` is trivial on `F_q^x` (“even”), it has the trivial factor `1-u`; the infinity Euler factor removes that factor in the completed geometric polynomial, whose degree is `d-2`. For odd `chi`, infinity is ramified and the polynomial has degree `d-1`. Every reciprocal root of the resulting nontrivial polynomial has modulus `sqrt q`. Thus at primitive cubic conductor the respective degrees are one and two. This is exactly the completion issue recorded in `report/sections/04o_graded_toys_exits.tex:180–196`; it does not prove a quotient graph's scattering formula. **OPEN for the requested cubic notebook example:** the actual local scattering matrices and infinity normalization, and their match to its chosen renewal model (`:214–219`). H-CLASS for the Picard-group tree quotient in `04p_gl1_bond.tex:64–81` remains a different assertion from this ray-level problem.

**PROVED comparison with finite cavities:** `h` counts external cusp coordinates; (D5.8), not that count alone, determines the minimal model exit rank. The finite formula `det S=(-1)^h p/ptilde` in `report/sections/04k_elliptic_cavity_scattering.tex:88–107` is rational in the tree variable. Our archimedean matrices have completed L-functions, infinitely many arithmetic modes, and possible delays; no finite polynomial `p` represents them. Their matrix functional equations are analogous, but determinant agreement alone also loses directional cancellations, as `:110–123` explicitly warns.

**SHARPENED observation (two sentences).** The pole pair of the completed zeta function may be read heuristically as constant/boundary data of an arithmetic cusp, but this note disproves its identification with the Eisenstein radical of `H^1` of the proposed Ihara quotient. A Deninger cohomology for `Spec Z` with an archimedean boundary remains a programme: neither the finite LPS Bass model nor the modular-curve correspondence constructs it, and the entire `xi` itself has no poles.

## What this changes in the notebook

Author: `codex:gpt-6-astra`

| Claim | Status to register | One-sentence statement |
|---|---|---|
| D1 | SHARPENED | The S-arithmetic quotient is a graph of modular surfaces with the Hecke correspondence between two vertex types; its specified vertex cohomology has character-dependent Eisenstein eigenvalues. |
| D2 | REFUTED | Frobenius, Bass doubling, open-curve cup radicals, residual poles, and scattering exits are distinct constructions, although each has a precise corrected pairing or spectral statement. |
| D3 | SHARPENED | Prime-level scattering is explicitly a two-cusp block per even nebentypus, with conductor factors and a rank-one trivial residue. |
| D4 | SHARPENED | Properly scaled twisted theta edges yield those ratios, and conjugation-correct arithmetic quotients are unconditionally pure Blaschke; odd characters require a different infinity type. |
| D5 | SHARPENED | The specified prime-level model has exit rank h, character multiplicities, local modes and delays, while its reduced zero-mode spectral metric criterion is GRH plus absence of Jordan chains and is not boundedly equivalent to the Hardy metric. |
| D6 | SHARPENED | Register the proved Q coefficient calculations, reject the literal diagonal H-ARITH formulation, and retain the function-field normalization and geometric/Galois bond identifications as open. |

**OPEN items retained deliberately:** the general-level explicit local matrix transcription; the cubic function-field scattering calculation with infinity factor; the natural arithmetic pairing on the Hardy model; the BC/Shor comparison; and stronger metric claims without norm equivalence. None is needed to establish the counterexamples or the prime-level formulas proved here.
