# Level-local cavity: proofs and corrections

Author: `codex:gpt-6-astra`

| Claim | Verdict | Result |
|---|---|---|
| L1 | REFUTED / SHARPENED | No exact fixed-cut realization of M; inverse realized by a weighted edge up to phases; cusp and funnel geometries differ. |
| L2 | SHARPENED | Orthogonal cascade proved; disk degree two becomes an infinite-dimensional delay/comb space; coupling reverses under adjoint. |
| L3 | SHARPENED | Tensor scattering and Boolean Fourier channels proved; product-graph inference refuted; prime-power matrix open here. |
| L4 | REFUTED / OPEN | Spectral zero comb differs from the trace-side prime comb; no level-tower spacing law follows. |
| L5 | SHARPENED | Registers a scattering-symbol cascade and its limits; no geometric H-LP, general H-CLASS, or function-field H-ARITH closure. |

## Corrections to the brief

| ID | Correction | Established in |
|---|---|---|
| C1 | In the 04k orientation M has a pole at zero; finite-core scattering is regular there. | L1.2 |
| C2 | The inverse factors have a two-ray weighted-edge realization, but its geometric ends are funnels, not finite-volume cusps. | L1.3–5 |
| C3 | A genuine two-cusp regular-tree toy has the reciprocal edge weight and different bound/resonance data. | L1.4 |
| C4 | The constant pole of the modular surface belongs to the global coefficient; M is regular at s=1. | L1.6 |
| C5 | Disk degree two is not half-plane dimension two: its two-dimensional disk fiber is tensored with L² of a delay cell. | L2.2 |
| C6 | Remove the single minus-comb point at i/2; the reduced factor is no longer periodic. | L2.1–2 |
| C7 | Forward compression feeds arithmetic into the local factor; the adjoint convention reverses the triangular coupling. | L2.3 |
| C8 | The continuous instantaneous exit is an unbounded trace; a finite-time loss operator need not have finite rank. | L2.4 |
| C9 | Squarefree level has 2^omega(N) cusps, one per divisor; the Boolean label group is not a Picard group. | L3.3 |
| C10 | Tensor coefficient matrices yield scalar cascade state spaces, not a four-ray scattering theorem for a product building. | L3.1–3 |
| C11 | Composite-level minus channels may retain zeros at i/2 after the one residual-factor cancellation. | L3.1 |
| C12 | A spectral zero comb and a trace-side prime-power measure are different objects, related through phase derivatives and Fourier transformation. | L4 |
| C13 | The Selberg shift tower in 09c is not a congruence-level tower. | L4 |
| C14 | The result concerns a specified reduced Eisenstein model, not the whole modular surface, and does not close geometric H-LP. | L5 |


## Conventions and source contract

Author: `codex:gpt-6-astra`

Abbreviated source citations `04i`, `04j`, `04k`, `04l`, `04r`, and `09c` refer, respectively, to `report/sections/04i_cusp_graph_scattering.tex`, `04j_cusp_graph_renewal.tex`, `04k_elliptic_cavity_scattering.tex`, `04l_elliptic_cavity_channel.tex`, `04r_h_theta_channels.tex`, and `09c_selberg_tower_cusp.tex`, all under `report/sections/`; numbers following the colon are source line numbers.

All formulas use width-one cusps ordered `(infinity,0)` as in `notes/deninger-cusp/astra-proofs.md:202–218`. Write
\[
 \ell=\log q,\quad a=q^{-1/2},\quad z=q^{s-1/2},\quad
 s=\tfrac12+i\tau,\quad z=e^{i\ell\tau},\quad
 F=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad D=\operatorname{diag}(1,-1),\quad
 H=2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\tag{0.1}
\]
This is the **04k disk variable**, not `q^{-s}`; upper-half-plane `tau` maps to the disk. The map is a covering, not a conformal equivalence of Hardy spaces. The disk origin has no finite preimage.

The graph definition is quoted exactly from `report/sections/04k_elliptic_cavity_scattering.tex:49–53`: “defined by the generalised eigenfunctions” with `g_a(k)=u_a z^{-k}+(S(z)u)_a z^k`, and “A delay mode is a root of p at z=0.” In this convention `Q=I-z W^*(z+z^{-1}-T_X)^{-1}W`, `S=-Q(z)^{-1}Q(1/z)` (`:91–107`). The modular coefficient has the inverse orientation; `04i_cusp_graph_scattering.tex:103–112` explicitly says “phi = 1/R”. The global factor below is the **meromorphic completed-zeta ratio** `phi=Lambda_0(2s-1)/Lambda_0(2s)`, not a purely archimedean Gamma factor and not the entire-xi ratio. See `04r_h_theta_channels.tex:22–31` for its theta constant-term derivation and `:44–52` for the radiation-space qualification. Uetake's actual reduced factor is `xi(2p)/xi(-2p)` in his wave variable `p`, with the elementary factors displayed in `refs/src/uetake-2007/paper.txt:615–629,634–657,676–680`.

## L1. What finite object the local matrix represents

Author: `codex:gpt-6-astra`

### L1.1. Exact algebra — PROVED

From the binding oldform computation `notes/deninger-cusp/astra-proofs.md:265–282`,
\[
 M(z)=\frac1{qz^2-1}
 \begin{pmatrix}q-1&\sqrt q(z-z^{-1})\\\sqrt q(z-z^{-1})&q-1\end{pmatrix},
 \qquad H^TMH=\operatorname{diag}(m_+,m_-),
\tag{1.1}
\]
\[
 m_+=\frac{z+\sqrt q}{z(1+\sqrt q z)}=\frac1{z b_{-a}(z)},\qquad
 m_-=\frac{z-\sqrt q}{z(1-\sqrt q z)}=\frac1{z b_a(z)},\qquad
 b_c(z)=\frac{z-c}{1-cz}.
\tag{1.2}
\]
Thus, with `mathcal L=M^{-1}`,
\[
 \mathcal L=H\operatorname{diag}(z b_{-a},z b_a)H^T,
 \quad \det M=\frac{z^2-q}{z^2(1-qz^2)}
 =\frac{1-q^{2-2s}}{1-q^{2s}},\quad
 \det\mathcal L=\frac{z^2(z^2-a^2)}{1-a^2z^2}.
\tag{1.3}
\]
These follow by addition/subtraction of rows and multiplication of the eigenvalues, including removable values by continuation.

### L1.2. No core gives M at the specified cut — REFUTED

For **every** finite real symmetric core and finite `W`, as `z→0`,
\[
 \mathsf G(z)=zW^*W+O(z^2),\quad
 Q(z)=I+O(z^2),\quad Q(1/z)=I-W^*W+O(z),\quad
 S(0)=W^*W-I.
\tag{1.4}
\]
Indeed `(z+z^{-1}-T_X)^{-1}=z(I-zT_X+z^2I)^{-1}` and the resolvent is unchanged by `z↔1/z`. Therefore `S` is regular at zero. But `M_{12}=sqrt(q)/z+O(z)` and `det M` has a double pole at zero. This rules out **any** such core, not merely the proposed two-vertex core. Constant basis changes and cusp-width scalings cannot remove this pole. Consequently there are no `p,ptilde` of the theorem giving this `M` as its fixed-cut scattering matrix: `ptilde(0)=1` already contradicts the requested determinant identity.

### L1.3. The inverse has an explicit weighted-edge realization — PROVED

For a real `t>0` take **two vertices, one edge of normalized weight t, one standard ray at each vertex**, namely
\[
 T_t=tF,\qquad W=I_2,\qquad c_1=c_2=1,\qquad C=I_2,
 \qquad\lambda=z+z^{-1}.
\tag{1.5}
\]
Then
\[
 \mathsf G_t=(\lambda I-tF)^{-1},\quad
 Q_t(z)=(z^{-1}I-tF)(\lambda I-tF)^{-1},\quad
 Q_t(1/z)=(zI-tF)(\lambda I-tF)^{-1},
\tag{1.6}
\]
\[
 S_t=-z(I-tzF)^{-1}(zI-tF),\qquad
 p_t=z^2(z^2-t^2),\qquad \widetilde p_t=1-t^2z^2,\qquad
 \det S_t=p_t/\widetilde p_t.
\tag{1.7}
\]
Proof: multiply the commuting matrices in (1.6); then evaluate the two determinants in the definition of `p`. No transfer theorem beyond 04k is needed.

For `t=a`, the eigenvalues of `S_a` are `-z b_a` in the symmetric channel and `-z b_{-a}` in the antisymmetric channel. Since `DFD=-F`,
\[
 \boxed{\ \mathcal L=-D S_aD,\qquad M=-D S_a^{-1}D.\ }
\tag{1.8}
\]
The left/right phase choices here are explicit; the leading minus is not an equality of scattering matrices with incoming and outgoing bases both fixed. They do give unitarily equivalent Hardy models: `mathcal L H^2=D S_a H^2`.

For this core `W` is surjective, so no invisible core eigenvectors exist. There are no threshold roots, no disk poles, and hence **no bound states**. The resonances are the simple nonzero zeros `z=±a` and two delay zeros at `z=0`. The model has disk dimension four, one nonzero resonance and one delay in each eigenchannel. Equations (1.6–8), rather than the false `M=S_a`, are the comparisons the blind lane must test.

### L1.4. The genuine two-cusp tree toy has a different edge — PROVED

At a cusp the normalized coupling satisfies `c_v^2=S(v)/S(e)` (`04k:72–81`). If each of the two core vertices has one cusp with `c=1`, the directed core-edge index must be `q`, because the total degree is `q+1`. Its normalized symmetric weight is therefore `sqrt(q*q)/sqrt q=√q`, **not a**. Explicit stabilizer data are
\[
 S(v_1)=S(v_2)=q,\quad S(v_1v_2)=1,\quad
 S(v_jr_{j,1})=q,\quad S(r_{j,k})=q^{k+1},\quad
 S(r_{j,k}r_{j,k+1})=q^{k+1}.
\tag{1.9}
\]
At a core vertex the indices are `q,1`; at every ray vertex they are `q,1`. Thus this is a regular-tree diagram in the notebook's stabilizer sense. If actual groups are desired, cyclic vertex groups of the displayed orders, trivial central edge group, and the evident nested cyclic inclusions on the rays realize these indices; their universal covering tree is `(q+1)`-regular. **External theorem, not byte-cited (Bass–Serre covering theorem, the part used):** a connected graph of groups with injective edge homomorphisms has a tree on which its fundamental group acts with that quotient, with the valence above a vertex equal to the sum of the incident edge-group indices in the vertex group. Here every such sum is `q+1`.

The core is `T_{sqrt q}` from (1.5), and exact substitution gives
\[
 \boxed{\ S_{\sqrt q}=-z^2DMD,\qquad
 p_{\sqrt q}=z^2(z^2-q),\qquad\widetilde p_{\sqrt q}=1-qz^2.\ }
\tag{1.10}
\]
It has two delay zeros and **no nonzero disk resonances**. Its two simple disk poles are `±a`, bound eigenvalues `±(√q+1/√q)`: the weighted constant and its bipartite twin. For instance the positive state has equal core coordinates and ray coordinates proportional to `a^k`, so is square summable. Removing the two directional bound poles leaves one disk delay state per channel. There are no invisible modes or thresholds because `W=I` and `q>1`.

Thus an additional ray-origin shift (`S→z^{-2}S`) and the displayed phases relate a genuine cusp toy to `M`. This does not satisfy the proposed fixed-cut equality. Moving an integer cut multiplies determinants by even powers of `z`, exactly as `04k:123–132` warns. The requested nonzero resonance comb belongs to the **inverse/funnel** realization, whereas the genuine cusp toy has those same disk points as **bound poles**. These two claims cannot be combined into one model.

### L1.5. Why this is not Gamma_0(q)'s finite-volume tree quotient — REFUTED / SHARPENED

Every matrix of `Gamma_0(q)` lies in `SL_2(Z_q)` and fixes the lattice vertex `[Z_q^2]` of the Bruhat–Tits tree. It also fixes the adjacent vertex associated with the preserved line modulo `q`. Distances from a fixed vertex are invariant and unbounded, so the quotient is not a single edge. This elementary obstruction requires no arithmetic quotient theorem.

More precisely, its closure is the determinant-one Iwahori subgroup: reduction `SL_2(Z)→SL_2(Z/q^m)` is onto (elementary matrices over the local ring generate, by row reduction), and imposing `c≡0 mod q` gives exactly this inverse limit. Finite vertex orbits of a compact open group are also orbits of its dense subgroup. For an explicit orbit proof, take the fixed edge between `[Z_q e_1+Z_q e_2]` and `[Z_q e_1+q Z_q e_2]`. At depth `n≥1` on the first side the lattices are `[Z_q(e_2+t e_1)+q^n Z_q e_1]`, `t mod q^n`; upper unipotents act transitively. At depth `n≥1` beyond the second endpoint they are `[Z_q(e_1+t e_2)+q^{n+1}Z_q e_2]`, `t∈q Z_q/q^{n+1}Z_q`; lower unipotents with lower entry in `q Z_q` act transitively. Each orbit has size `q^n`. Consequently its orbital quotient is a central edge with two infinite rays, with directed indices **q away from the edge and 1 toward it**. Its counting masses grow as `q^k`. Normalized radial adjacency is precisely `T_a` with two standard rays and unit junctions. This is the radial two-funnel object of L1.3, not the finite-volume cusp object of L1.4, whose masses decay as `q^{-k}`. The arithmetic subgroup is not a discrete lattice in this local compact group, and its stabilizers here are infinite; (1.9) is a different graph-of-groups construction.

The correct finite datum behind the automorphic formula is the two-dimensional oldform coefficient matrix
\[
 B_q(s)=\begin{pmatrix}1&q^s\\q^s&1\end{pmatrix},\qquad
 M_q(s)=B_q(1-s)B_q(s)^{-1}.
\tag{1.11}
\]
This is already proved by the two old Eisenstein series in the binding source `notes/deninger-cusp/astra-proofs.md:275`. It is also compatible with the local two-state intertwining picture; no identification of global modular cusps with finite-volume ends of the q-adic orbital quotient is needed or asserted. The obstruction is orientation, cut, and geometry, not just the widths `1,q`.

### L1.6. Comb and constant — PROVED

The nonzero zeros of the inverse eigenfactors pull back to
\[
 L_-: \quad\tau=\frac{2\pi k}{\ell}+\frac i2,\qquad
 L_+: \quad\tau=\frac{(2k+1)\pi}{\ell}+\frac i2,\qquad k\in\mathbb Z.
\tag{1.12}
\]
Their images in the s-plane have `Re s=0`; in the raw local `M` they are poles. The modular constant pole is at **s=1**, where
\[
 M_q(1)=\frac1{q+1}\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
 \operatorname*{Res}_{s=1}(\phi M_q)=\frac3{\pi(q+1)}\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\tag{1.13}
\]
Thus it is not a pole of `M_q`. In the upper-half-plane inverse symbol the residual pole is at `tau=i/2` in the plus channel; the minus local zero cancels it. The specified reduction is therefore `I_+=Theta_1 L_+`, `I_-=Theta_1 L_-/r`, exactly `notes/deninger-cusp/astra-proofs.md:438–456`. One must remove the **single** zero `k=0` in the minus comb; it is not a surviving local resonance of that reduced channel.


## L2. Model spaces, the delay, dynamics, and exits

Author: `codex:gpt-6-astra`

### L2.1. Orthogonal factorization and the residual reduction — PROVED

For scalar inner `A,B` on the disk or upper half-plane, multiplication by `A` is an isometry, and
\[
 H^2=K_A\oplus A H^2=K_A\oplus A K_B\oplus AB H^2,
 \qquad K_{AB}=K_A\oplus A K_B.
\tag{2.1}
\]
This proves the assertion, including its orthogonality. With
\[
 A=\Theta_1,\qquad B_+=L_+,\qquad B_-=L_-/r,\qquad
 U_A(f,g)=f+Ag,
\tag{2.2}
\]
`U_A` is unitary `K_A⊕K_{B_±}→K_{I_±}`. **The reduced minus channel uses `K_{L_-/r}`, not `K_{L_-}`.** The latter describes the unreduced extra divisor. The prime-level trivial-nebentypus space has **two copies** of `K_Theta_1`, one in each channel. This is a scattering model, not the whole modular surface Hilbert space (invisible Maass cusp forms and the removed residual state are not in it).

The arithmetic factor is pure Blaschke with zeros `w_rho=gamma/2+i(1-sigma)/2`, multiplicity `m_rho`, proved in `notes/h-theta/astra-proofs.md:191–278`. Its kernel jets are complete and minimal (`:698–743`; `04r:77–105`). In the physical `X=log y` coordinate they span the functions
\[
 X^j e^{-(1-\sigma)X/2-i\gamma X/2},\quad X>0,\quad
 \xi(\sigma+i\gamma)=0,\quad 0\le j<m_\rho.
\tag{2.3}
\]
They are eigenvectors/generalized eigenvectors of the **adjoint** compression `C_t` below. No RH is used. Under RH their damping rate is `1/4`.

### L2.2. What “finite per period” can mean — SHARPENED

**External theorem, not byte-cited (Paley–Wiener for the upper half-plane).** With boundary norm `∫|F(tau)|² d tau/(2 pi)`,
\[
 (\mathcal F f)(\tau)=\int_0^\infty f(X)e^{i\tau X}\,dX
\tag{2.4}
\]
is unitary from `L²(0,infinity)` onto `H²(C_+)`, interpreted in the `L²` boundary sense. Multiplication by `e^{it tau}` is the right shift by `t`, extended by zero. In particular
\[
 \mathcal F^{-1}K_{e^{i\ell\tau}}=L^2(0,\ell).
\tag{2.5}
\]
This is **infinite dimensional**, even for one period. The interval may be interpreted as a delay line of length `log q`; the symbol by itself does not identify it with a geodesic edge of the modular surface.

There is a precise finite-fiber statement. Decompose the half-line into cells and use the unitary
\[
 f\longmapsto (f_n)_{n\ge0},\qquad f_n(x)=f(n\ell+x),\quad 0<x<\ell,
 \qquad L^2(0,\infty)\simeq L^2((0,\ell);\ell^2(\mathbb N_0)).
\tag{2.6}
\]
The delay becomes the unilateral shift on the sequence index. Hence for `c=±a`, writing `B_c(tau)=b_c(e^{i ell tau})`,
\[
 \mathcal F^{-1}K_{B_c}
 =\{f(n\ell+x)=\sqrt{1-c^2}\,c^n h(x):h\in L^2(0,\ell)\}.
\tag{2.7}
\]
The normalization follows from `(1-c²)sum c^{2n}=1`; the description follows either by applying the one-dimensional disk kernel space `K_{b_c}=span{sqrt(1-c²)/(1-cz)}` fiberwise or by its geometric-series coefficients. Consequently
\[
 K_{z b_c(z)}^{\rm disk}\simeq\mathbb C^2,\qquad
 K_{e^{i\ell\tau} B_c(\tau)}^{\rm half-plane}
 \simeq L^2(0,\ell)\otimes\mathbb C^2.
\tag{2.8}
\]
Explicitly its physical functions satisfy `f_0=h_0` and `f_n=sqrt(1-c²)c^{n-1}h_1` for `n≥1`, with arbitrary `h_0,h_1∈L²(0,ell)`. This is the orthogonal split `K_u⊕u K_{B_c}`. It is a rational disk system of degree two suspended with a delay, not a two-dimensional half-plane space.

The nonzero disk zero `c` lifts to one simple zero per real period `2 pi/ell`, the comb (1.12). The comb kernels have physical representatives `e^{-X/2}e^{-i omega_k X}`. Their restrictions to the first cell are a bounded invertible exponential weight times a Fourier basis; the recurrence in (2.7) then proves they span `K_{B_c}`. Thus there is **one zero per period**, not one Hilbert-space dimension for a period interval. The disk zero at zero lifts to the zero-free singular inner delay `u`; it yields (2.5), not an additional finite-height comb.

For the reduced minus factor put `widehat B_-=B_a/r`. It is inner with the `k=0` Blaschke divisor removed, and
\[
 K_{B_a}=K_r\oplus rK_{\widehat B_-},\qquad
 K_{L_-/r}=K_u\oplus uK_{\widehat B_-}.
\tag{2.9}
\]
It retains the delay and all minus comb points except `i/2`. Removing one lift breaks periodicity, so this reduced factor is **not** a rational function of `z=e^{i ell tau}`. The exact finite-fiber formula (2.8) applies before this one-state reduction.

For comparison with `thm:h-exit-model`, in the orthonormal disk basis
\[
 e_0=1,\qquad e_1=\frac{z\sqrt{1-c^2}}{1-cz},\qquad
 Z_c=\begin{pmatrix}0&0\\\sqrt{1-c^2}&c\end{pmatrix},\qquad
 J_c=\begin{pmatrix}-c&\sqrt{1-c^2}\end{pmatrix},
 \qquad I-Z_c^*Z_c=J_c^*J_c.
\tag{2.10}
\]
The eigenvalue zero is the delay mode, and `c` is the nonzero resonance. The orthogonal first summand `span{e_0}` in (2.1) is not the zero eigenspace of `Z_c`; factor decompositions are not spectral decompositions. In (2.8), time-`ell` compression is this same matrix with identity on `L²(0,ell)`; its defect has infinite rank. One disk step and one continuous-time sample are different notions of exit multiplicity.

### L2.3. Exact semigroup block, with both time orientations — PROVED

Let `V_t=M_{e^{it tau}}` on `H²(C_+)` and define
\[
 Z_I(t)=P_{K_I}V_t|_{K_I},\qquad C_I(t)=Z_I(t)^*=V_t^*|_{K_I},\quad t\ge0.
\tag{2.11}
\]
`I H²` is `V_t`-invariant, so these are contraction semigroups. Define the output profile
\[
 E_t^A f=M_A^*(I-P_{K_A})V_t f\in H^2,
 \qquad V_t f=Z_A(t)f+A E_t^A f.
\tag{2.12}
\]
Here `M_A^*` is the Hardy adjoint, not unrestricted boundary multiplication. Orthogonality to `e^{it tau}H²` shows `E_t^A f∈K_{e^{it tau}}`. Projecting (2.12) into (2.1) gives
\[
 \boxed{\ U_A^*Z_{AB}(t)U_A=
 \begin{pmatrix}Z_A(t)&0\\P_{K_B}E_t^A&Z_B(t)\end{pmatrix},\qquad
 U_A^*C_{AB}(t)U_A=
 \begin{pmatrix}C_A(t)&(P_{K_B}E_t^A)^*\\0&C_B(t)\end{pmatrix}.\ }
\tag{2.13}
\]
Thus **for the forward compressed shift `Z`, arithmetic feeds the local factor; for the left-shift/kernel convention `C`, the local factor feeds arithmetic**. The arithmetic kernel modes (2.3) are invariant for `C`, not generally for `Z`. Calling both operators `Z_t` while preserving both directions would be an error. Factor order is also a choice: scalar `AB=BA` permits a different orthogonal factor decomposition with the order reversed.

The exact forward output, still in `K_{e^{it tau}}≅L²(0,t)`, is
\[
 E_t^{AB}U_A(f,g)=M_B^*(I-P_{K_B})E_t^A f+E_t^B g,
 \quad \|h\|^2-\|Z_{AB}(t)h\|^2=\|E_t^{AB}h\|^2.
\tag{2.14}
\]
This is a concrete cascade: the first output profile is split into retained local state and final output. Moreover each `B_±` contains the delay `u`, so for arithmetic initial data `(f,0)` the final output in (2.14) vanishes for `0≤t≤ell`: `E_t^A f` is supported in `(0,t)` and is orthogonal to `B_± H²`, whose physical support starts at `ell`. Thus the forward output really traverses a local delay. This proves an operator-model statement; it supplies no geometric gluing theorem for the modular surface.

### L2.4. Exit functionals and their domains — PROVED

For a single **disk compressed shift**, put `k_0^B=1-overline{B(0)}B`. The defining identity `wf=Z_A f+A J_A f` gives
\[
 U_A^*Z_{AB}U_A=
 \begin{pmatrix}Z_A&0\\k_0^B J_A&Z_B\end{pmatrix},\qquad
 J_{AB}U_A(f,g)=\overline{B(0)}J_A f+J_B g,
\tag{2.15}
\]
\[
 J_I^*1=\frac{I(w)-I(0)}w,\qquad I-Z_I^*Z_I=J_I^*J_I,\qquad
 \|J_I\|^2=1-|I(0)|^2.
\tag{2.16}
\]
Indeed the projection of the constant `1` onto `BH²` is `overline{B(0)}B`, proving (2.15); (2.16) follows by taking the norm of the part of `wf` outside the model space. These are `04l:22–28,38–57` and the rank refinement `notes/deninger-cusp/astra-proofs.md:482–494`. To apply them to `Theta_1` and `B_±` simultaneously, use a **Cayley** coordinate `w=(tau-i eta)/(tau+i eta)`, `eta>0`, and the associated weighted Hardy unitary. Do not use the non-injective periodic coordinate `z` as if it were this Cayley coordinate. Each reduced scalar channel is nonconstant, so the Cayley disk model has rank-one exit; their direct sum has rank two.

In continuous time, in the physical realization of `K_I`, `C_I(t)f(X)=f(X+t)`. Its generator has domain `K_I∩H¹(0,infinity)` and is `f'`; the boundary trace
\[
 j_C f=f(0),\qquad
 -2\operatorname{Re}\langle f,f'\rangle=|f(0)|^2,\qquad
 \|f\|^2-\|C_I(t)f\|^2=\int_0^t|f(x)|^2\,dx
\tag{2.17}
\]
is the scalar instantaneous exit. In decomposition (2.2), it is explicitly the boundary value of `mathcal F^{-1}(f+A g)`, on the domain where that total function is `H¹`; the componentwise boundary traces need not exist separately. For the full level models here this functional is unbounded: since the total inner symbol contains a positive delay, its model contains `L²(0,ell)`, and smooth boundary spikes there have unbounded trace at fixed L² norm. For the forward orientation, the standard model conjugation `mathfrak C_I F=I overline F` on the real boundary is an antiunitary involution of `K_I` and intertwines `Z_I(t)` with `C_I(t)` (verify by the Hardy projection and boundary multiplication). Thus
\[
 j_Z F=\overline{\big(\mathcal F^{-1}\mathfrak C_I F\big)(0)},\qquad
 D(j_Z)=\{F:\mathcal F^{-1}\mathfrak C_I F\in H^1\}
\tag{2.18}
\]
is the corresponding linear exit on the generator domain. Its time-integrated flux equals the loss in (2.14). A scalar generator flux does not make `I-Z_I(t)^*Z_I(t)` rank one at fixed `t>0`; the delay already disproves that claim. This is the discrete/continuous distinction explicitly required by `notes/deninger-cusp/astra-proofs.md:496–500`.


## L3. Squarefree level: tensor coefficients, cascade state spaces

Author: `codex:gpt-6-astra`

### L3.1. Squarefree theorem — PROVED

Let `N=product_{j=1}^k q_j` be squarefree, `k≥1`, and `h=2^k`. In width-one cusp coordinates indexed by divisors of `N`, up to a fixed permutation,
\[
 \Phi_{0,N}(s)=\phi(s)\mathcal M_N(s),\qquad
 \mathcal M_N(s)=\bigotimes_{j=1}^k M_{q_j}(s),\qquad
 \det\Phi_{0,N}=\phi(s)^h\prod_{q\mid N}
 \left(\frac{1-q^{2-2s}}{1-q^{2s}}\right)^{h/2}.
\tag{3.1}
\]
This is the binding theorem `notes/deninger-cusp/astra-proofs.md:284–295`. Its proof is especially concrete: the incoming oldform coefficient matrix is `B_N(s)=tensor_j B_{q_j}(s)`; the outgoing one is `phi(s)B_N(1-s)`. Thus `Phi=phi B_N(1-s)B_N(s)^{-1}`. Determinants use `det(A⊗B)=det(A)^{dim B}det(B)^{dim A}`. Notice there is **one scalar phi before taking the determinant**, not one phi per prime factor.

The Walsh transform `H_N=H^{⊗k}` diagonalizes these matrices. For `epsilon=(epsilon_q)∈{+,-}^k`,
\[
 \phi_\epsilon(s)=\phi(s)\prod_{q\mid N}m_{q,\epsilon_q}(s),\qquad
 \phi_\epsilon(\tfrac12+i\tau)^{-1}
 =r(\tau)^{-1}\Theta_1(\tau)\prod_{q\mid N}L_{q,\epsilon_q}(\tau).
\tag{3.2}
\]
Let `m(epsilon)` be the number of minus signs. Each minus factor has one simple zero at `tau=i/2`, and no plus factor does. The sole residual pole is in the all-plus channel. The minimal pole-removed symbols in this convention are
\[
 I_\epsilon=\Theta_1 B_\epsilon,\qquad
 B_\epsilon=
 \begin{cases}
 \prod_{q\mid N}L_{q,+},&m(\epsilon)=0,\\
 r^{-1}\prod_{q\mid N}L_{q,\epsilon_q},&m(\epsilon)\ge1.
 \end{cases}
\tag{3.3}
\]
All are inner: in the second line divide by a Blaschke divisor already present. A channel with `m≥1` retains order `m-1` at `i/2`. This common collision must be counted at composite level. For `N=35`, the `--` channel retains one such zero, while `+-` and `-+` retain none. The all-plus channel gets its residual pole removed, as at prime level.

Consequently the prescribed trivial-character scattering model has
\[
 K_N^{\rm scat}\simeq\bigoplus_{\epsilon\in\{+,-\}^k}
 \left(K_{\Theta_1}\oplus\Theta_1 K_{B_\epsilon}\right).
\tag{3.4}
\]
There are **h arithmetic copies** and exactly `h` Cayley disk exit coordinates, since each scalar symbol is nonconstant inner. Its continuous-time generator has `h` scalar boundary traces, not one per arithmetic zero. No additional Dirichlet-L zero set occurs at squarefree trivial level.

### L3.2. A product of transfer factors is not a tensor of state spaces — SHARPENED

For a fixed channel, write `u_q=e^{i tau log q}`. Before the possible division by `r`, repeated use of (2.1) gives
\[
 K_{\prod_{j=1}^k L_j}=
 \bigoplus_{j=1}^k\left(\prod_{i<j}L_i\right)K_{L_j},\qquad
 \prod_{q\mid N}L_{q,\epsilon_q}
 =e^{i\tau\log N}\prod_{q\mid N}b_{c_q}(u_q),
 \quad c_q=\begin{cases}-q^{-1/2},&\epsilon_q=+,\\q^{-1/2},&\epsilon_q=-.\end{cases}
\tag{3.5}
\]
Thus one may combine the delays into `L²(0,log N)` and then cascade the Blaschke spaces; the minus reduction deletes one of the common factors `r`. State dimensions add in finite rational cascades, whereas a tensor of states multiplies them. These are distinct constructions.

For different primes the periods `2 pi/log q_j` are incommensurate: a rational relation between two logarithms would imply equality of positive powers of distinct primes. Consequently even the unreduced `N=35` factor has no single fundamental real period. The multivariable rational matrix `tensor M_{q_j}(z_j)` is restricted to `z_j=e^{i tau log q_j}`. It is not a rational matrix in one common equal-edge disk variable.

### L3.3. Cusps, the Boolean group, and the failed product-graph inference

**PROVED (the finite labeling/Fourier statement).** The cusp classification used in the binding source `notes/deninger-cusp/astra-proofs.md:191–196` gives
\[
 h_0(N)=\sum_{d\mid N}\varphi(\gcd(d,N/d))=2^k
 \quad\text{for squarefree }N.
\tag{3.6}
\]
There is one cusp `1/d` per divisor, with `1` equivalent to `0` and `1/N` equivalent to `infinity`. Thus `N=q_1 q_2` has the stated four cusps. Identify divisors with subsets of the prime factors, with symmetric difference as addition. Every `M_q` is `alpha_q I+beta_q F`; its tensor product is therefore a convolution matrix on this Boolean labeling group `(Z/2)^k`. The Walsh transform is exactly its character Fourier transform. This elementary group-matrix assertion is proved by the matrix entries and does not require an arithmetic class group. The same group can be realized by the squarefree Atkin–Lehner involutions on the cusp labels.

**REFUTED (literal class group/product cavity).** This is not `prop:cusps-are-class-group-bond`: `report/sections/04p_gl1_bond.tex:67–81` assumes `R=O(C\P_0)` over a finite field and identifies cusps with `Pic(R)`. The rational field's ideal class group is trivial; a Boolean divisor labeling is not that theorem. Nor does it prove H-CLASS for general function-field quotients, stated in `04k:290–304`.

The tensor in (3.1) is not the scattering theorem for a square core with four standard rays. Tensoring one-particle scattering systems introduces separate energy variables; the adjacency of a Cartesian product is a Kronecker **sum**, and its resolvent is not the tensor product of resolvents at the same spectral parameter. Product ends also have transverse continua, not just the four prescribed standard rays. A direct geometric obstruction is the same as in L1.5: `Gamma_0(N)` fixes a vertex in **each** local tree, so the vector of distances is invariant and unbounded. Its quotient cannot be just a square. A square may label a product of fixed edges or local oldform choices; it is not the whole quotient with four finite-volume cusp ends. The distinction between a building quotient and an arbitrary product of transfer symbols is consistent with `02d_definitions_complexes.tex:35–53,80–92`, whose Hecke conditions concern joint geometric data.

An abstract multichannel delay network can realize (3.2) by independent scalar cascades and the Walsh change of basis. A geometric modular-surface/product-building realization of those cascades, including compatible radiation spaces and exit maps, is **OPEN** here, not a consequence of tensor algebra. “A prime contributes one binary local factor, doubling the number of squarefree cusps” is the valid replacement for “one cusp per prime”.

### L3.4. Prime powers — OPEN for the full matrix; elementary obstruction PROVED

Already
\[
 h_0(q^2)=1+(q-1)+1=q+1,
 \qquad h_0(q^n)=\sum_{j=0}^n\varphi(q^{\min(j,n-j)}).
\tag{3.7}
\]
So the `q²` matrix is not the `4×4` tensor of two prime-level matrices (for `q≥5`, even the sizes disagree). The cusps of denominator `q` carry numerator classes, not merely a new Boolean bit. Oldforms no longer exhaust the Eisenstein space in general, and inducing-pair sectors may enter. An explicit full `Gamma_0(q²)` width-one matrix, its completions, and the corresponding minimal inner reductions are **OPEN in this note**; no `q→q²` substitution is licensed.


## L4. The two combs and the meaning of “tower”

Author: `codex:gpt-6-astra`

**REFUTED as an identity of objects; SHARPENED by a Fourier relation.** The comb (1.12) is a **complex spectral zero divisor** at height `1/2`, with real spacing `2 pi/log q` in each scalar channel. The comb in `report/sections/09c_selberg_tower_cusp.tex:78–100` is a **real-time distribution**: its formula is `C_cusp=-P+A_arch`, with `P(t)=sum_{n≥2} Lambda(n)/n [delta(t-2 log n)+delta(t+2 log n)]`. Its q-part lies at `t=±2m log q`, has weights `(log q)q^{-m}`, and has no spectral “height”. These cannot literally be the same comb. There is a useful precise relation: for real `tau`, `c=±a`, the phase derivative of the unreduced local channel is `(1/i)partial_tau log[u b_c(u)]=ell[2+2 sum_{n≥1}c^n cos(n ell tau)]`, by the Poisson-kernel expansion. Summing the two channels cancels the odd harmonics. With Fourier transform `hat f(t)=(2 pi)^{-1}int f(tau)e^{-i tau t}d tau`, the result is `4 ell delta_0+2 ell sum_{m≥1}q^{-m}[delta(t-2m ell)+delta(t+2m ell)]`. Thus the pair's **phase derivative**, after its zero-time term and normalization are accounted for, has the q-prime-power support and weights. It is still not an identification of zero divisors with trace atoms. Division by the single `r` adds a nonperiodic elementary phase term; it cannot be silently omitted. This agrees with the distinction in `04i:241–246` and the warning in `09c:125–138` that equality of prime measures is not equality of full traces or operators.

**REFUTED as a reading of 09c; OPEN as a separate level-tower proposal.** The “Selberg tower” there is `D_tow(v)=product_{j≥1}Z_Sel(v+j)` (`09c:27–42`), arising from the transverse Poincare Jacobian and integer spectral shifts. It is not the congruence tower `q,q²,...`; its bands are described at `:44–62`. Nothing there predicts spacing `2 pi/(n log q)` at level `q^n`. Replacing the local delay by `e^{i n ell tau}` and its disk zero by `q^{-n/2}` would manufacture exactly that spacing and height `1/2`, but identifying that manufactured factor with prime-power scattering is **speculation**, not a theorem. The cusp-count obstruction (3.7) already rules out simply replacing the full prime-level block by its `q→q^n` version. The actual prime-power divisor/spacing question requires the uncomputed matrices of L3.4 and remains **OPEN here**.


## L5. The arithmetic-cavity statement that survives

Author: `codex:gpt-6-astra`

**SHARPENED.** The trivial-character prime-level **reduced Eisenstein scattering model** is two Riemann arithmetic channels, each cascaded with an explicit local delay/comb factor, with the single minus residual cancellation prescribed in (2.2). Its matrix symbol comes from global `phi` times the two-dimensional local oldform datum. The full modular surface is not thereby a finite graph, and `phi` is not merely an archimedean boundary reflection coefficient. The Gaussian/theta derivation identifies constant-term Mellin symbols (`04r:19–31`); it does not identify all geometric wave spaces. Uetake's distinction between radiation-space choices (`paper.txt:615–657`) remains binding.

**PROVED (the exit through the local factor).** In the forward orientation the lower-triangular block (2.13) and output formula (2.14) make the cascade concrete. Arithmetic initial data produces no final output before the local delay `log q`. In a Cayley disk convention the coupling is `k_0^B J_A`, and the final exit is `overline{B(0)}J_A+J_B`, so a direct term can appear in that different clock. In the kernel/left-shift convention the block direction reverses. This is an exact model of a sink repaired by an output space. Selecting a rebound density or a geometric/Hecke reset remains extra data.

**PROVED (scope of 04i–04l).** The Schur-resolvent scattering theorem and `p/ptilde` identity of `04k:88–135` apply verbatim to the two explicit weighted-edge toys, with their different parameters and spectra. The disk inner model, delay count, defect identity, and finite-dimensional Gram/renewal results of `04l:38–90` apply verbatim to `S_a`, a four-state model with two exits, and its scalar eigenchannels. They also apply to the pole-removed genuine cusp toy, whose remaining states are delays. The finite stable one-exit statements of `04j:12–47` apply separately to each scalar finite disk model. Claims about arbitrary resets requiring finite dimension, uniform finite holding means, or finite rational determinants do **not** transfer verbatim to the infinite half-plane arithmetic-plus-delay space. Equations (2.13–18) supply the needed continuous-time version of the no-event dynamics and flux, not a proof of every renewal conclusion.

**OPEN (geometry).** The wave-compression identification H-LP is expressly unproved in `04l:13–18,57` and already qualified in `04i:197–218`; this computation does not close it. It also does not construct a positive arithmetic pairing, identify resonance states with `L²` modular eigenstates, or resolve the missing noncompact flow bridge in `03f_selberg_letters_finite.tex:29–49`. The local rational part is finite before suspension; the global arithmetic zeros are supplied by `Theta_1`, not manufactured by the edge.

**PROVED / OPEN (the named next-round items).** For `obs:h-theta-next(iv)` (`04r:171–172`), the prime and squarefree trivial-character matrices of edge quotients are explicit and proved, using the morning lane; the present note adds the local realization, obstruction, and cascade. The general-level/geometric reading remains open. None of `obs:h-theta-next(i–iii)` (`:167–170`, Sonine Gram test and Burnol channels) is closed by this argument. None of `obs:graded-toys-next(i–iv)` (`04o_graded_toys_exits.tex:217–224`) is closed: they ask for function-field cubic conductor, fermionic MPS closure, an expander realization, and a non-self-adjoint arithmetic-metric core. In particular the number-field Boolean Fourier calculation is not the general Picard-group H-CLASS theorem or the function-field H-ARITH calculation.

## Numerical checks for the blind lane

Author: `codex:gpt-6-astra`

The independently executable scratch file is `notes/level-local-cavity/checks/verify.py`; run `python3 notes/level-local-cavity/checks/verify.py`. It uses 60-digit mpmath arithmetic plus exact SymPy and a small NumPy Gram check. It writes no artifacts. All assertions passed on this run. These are checks of the formulas, not proofs of the Hardy or geometric claims.

1. **Requested matrix test.** At `s=0.7+0.3i`, use `z=q^{s-1/2}` (outside the disk at these test points; the identities are rational). Compute `G_t=(lambda I-tF)^{-1}`, `Q_t=I-zG_t`, and `S_t=-Q_t(z)^{-1}Q_t(1/z)` directly. Test the **corrected** equalities `M^{-1}=-D S_a D` and `S_{sqrt q}=-z² D M D`. The raw requested equality `M=S_a` must fail.

| q | M diagonal | M off-diagonal | det M | max-entry error in false M=S_a |
|---|---|---|---|---|
| 5 | `0.218634648327814 - 0.387681428625362i` | `0.282655097128056 - 0.006293311464958i` | `-0.182350078814851 - 0.165963512494691i` | `1.50604826933` |
| 7 | `0.134991110996399 - 0.379918588305854i` | `0.238480995379373 - 0.040919736670041i` | `-0.181314294000262 - 0.083054105583715i` | `1.66362344181` |

The corrected matrix residuals are below `4.1e-61`. Check `det M=(1-q^{2-2s})/(1-q^{2s})` and `det S_a=z²(z²-a²)/(1-a²z²)` separately; residuals are below `2e-60`. SymPy also verifies (1.6–7) with symbolic `t,z`. Test the genuine cusp bound equation at `theta=±a` on core vectors `(1,±1)`; both residuals are below `1e-55`.

2. **Comb and canceled point.** For `k=-4,...,4`, evaluate `L_-` at `2 pi k/log q+i/2` and `L_+` at `(2k+1)pi/log q+i/2`. All heights are exactly `1/2`; residuals are below `6e-61`. The respective periods are `3.90396253166234` for `q=5` and `3.22891851416156` for `q=7`. The removed minus point must **not** remain a zero: l'Hopital gives
\[
 (L_-/r)(i/2)=-\frac{\log q}{q-1},
\tag{N.1}
\]
namely `-0.402359478108525` and `-0.324318358175886`. This follows from `L_-'(i/2)=i log q/(q-1)` and `r'(i/2)=-i`.

3. **Delay dimension and finite fiber.** Verify the disk matrix/exit identity (2.10), eigenvalues `0,c`, and the geometric norm sum in (2.7). In the half-plane delay space the functions `ell^{-1/2}exp(2 pi i j X/ell)1_(0,ell)`, for **arbitrarily many distinct integers j**, have identity Gram matrix. The script checks eight; the exact identity `ell^{-1}int_0^ell exp(2 pi i (j-k)X/ell)dX=delta_{jk}` proves the unrestricted statement. The answer to “delay dimension per period” is therefore: disk delay degree **one per channel**, half-plane delay Hilbert dimension **infinite**, fiber dimension **one** in (2.6). The full unreduced local fiber dimension is two. Numerical quadrature verifies the eight-function Gram to better than `1e-14`.

4. **N=35 tensor.** Independently form the `4×4` incoming matrix `B_35(s)=B_5(s)⊗B_7(s)` and its outgoing counterpart `B_35(1-s)`. Verify `B_35(1-s)B_35(s)^{-1}=M_5(s)⊗M_7(s)`, then diagonalize with `H⊗H` and compare the four products `m_{5,epsilon_5}m_{7,epsilon_7}`. The oldform residual is below `1.4e-62`, off-diagonal Walsh residual zero at working precision, and the determinant comparison `(det M_5)^2(det M_7)^2` has error below `5e-64`. No zeta evaluation is needed: the common factor is `phi`, with determinant power four. Check the residual-order prediction at `i/2`: orders `0,0,0,1` for the local reduced factors in channels `++,+-,-+,--`.

5. **Comb/trace normalization.** The script checks the real phase derivative of the unreduced product `L_+L_-` against `4 ell[1+sum_{m≥1}q^{-m}cos(2m ell tau)]`, using 99 terms at `tau=0.23`; the truncation and arithmetic errors are below `1e-55`. Transforming cosine terms gives precisely the local distribution stated in L4, including the factor two and the zero-time atom.

## What this changes in the notebook

Author: `codex:gpt-6-astra`

| Claim | Status to register | One-sentence statement |
|---|---|---|
| L1 | REFUTED as stated; corrected realization PROVED | At the fixed 04k cut M is impossible, while its inverse is phase-equivalent to a two-funnel weighted-edge model; the genuine cusp edge instead satisfies S=-z²DMD. |
| L2 | SHARPENED / PROVED | The reduced level model is an orthogonal arithmetic/local cascade with explicit triangular dynamics and exit, finite only in the local disk realization before suspension. |
| L3 | SHARPENED / PROVED; geometric extension OPEN | Squarefree scattering tensors and Walsh-diagonalizes, giving 2^omega(N) arithmetic copies and divisor cusps, without a product-building scattering theorem. |
| L4 | REFUTED as identification; phase/Fourier relation PROVED | Local spectral combs yield prime-power-supported phase transforms, but neither equal the 09c trace comb as objects nor imply a congruence-tower spacing law. |
| L5 | SHARPENED | The programme gains an explicit symbol-level cascade and its local toy, while H-LP, general H-CLASS, function-field H-ARITH, and geometric modular gluing remain open. |
