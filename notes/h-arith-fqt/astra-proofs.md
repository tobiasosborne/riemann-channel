# H-ARITH over F_q[T]: proof and correction ledger

Author: `codex:gpt-6-astra`

| Claim | Verdict | Finding |
|---|---|---|
| H1 | PROVED / SHARPENED | Specified GL₂ subgroup; two diamond torsors; exact cores and stabilizers |
| H2 | PROVED / SHARPENED | Completed polynomial ratio with coefficient q u^d; odd scalar channels excluded |
| H3 | PROVED / REFUTED | Exact prime-level blocks and residue; literal diagonal H-ARITH-1 refuted |
| H4 | PROVED / SHARPENED | Exact finite cores after inversion/height correction; model dimensions 0,14,84 and 0,18,156 |
| H5 | SHARPENED / OPEN | Corrected prime-level assumption settled; general H-CLASS and BC/Shor comparisons retained open |

H1–H5 are complete as proof/refutation tasks. Explicit OPEN items state the limits of the theorem; no ledger row is pending. The file was saved incrementally after each claim.

## H1. The group, cusp set, and exact finite core — PROVED with specified conventions

Author: `codex:gpt-6-astra`

### H1.1. Group and cusps

Write `A=F_q[T]`, `K=F_q(T)`, `pi=T^{-1}`, and `G=GL_2(A)`. Every determinant in `G` belongs to `F_q^*`. Define

\[
\Gamma_0(N)=\{\gamma\in G:c\equiv0\pmod N\},\qquad
\Gamma_1(N)=\{\gamma\in G:c\equiv0, d\equiv1\pmod N\}.
\tag{1.1}
\]

In particular **we do not additionally impose `a=1` or `det=1`**. The kernel of the action of `G` on the tree is `Z=F_q^*I`. The image of `Gamma_1` is the image of `Z Gamma_1`; all stabilizer orders below are in this effective image. For `Gamma_0`, divide its matrix stabilizer orders by `q-1`; the action of `Gamma_1` itself is faithful. The images of `Gamma_1` and `Z Gamma_1` coincide, so adjoining this center changes neither the graph nor its scattering. Do not enlarge to all matrices with arbitrary rational determinant, or to `GL_2(A/N)` before imposing determinant in `F_q^*`.

For an arbitrary monic nonconstant `N`, put `U(D)=(A/D)^*`, with `U(1)` the one-element set. The exact analogues of the rational cusp parametrizations are

\[
 C_1(N)=\coprod_{D\mid N}(U(D)/F_q^*)\times(U(N/D)/F_q^*),
\qquad
 C_0(N)=\coprod_{D\mid N}U(\gcd(D,N/D))/F_q^*.
\tag{1.2}
\]

Actions on `U(1)` are understood as trivial. These are sets, not canonically groups. A primitive column `(a,c)` gives `D=gcd(c,N)` (monic), `a mod D`, and `c/D mod N/D`. For `Gamma_1`, upper triangular reduction sends `(a,c)` to `(delta a+bc,c)`, `delta in F_q^*`; projective rescaling of the primitive column is independently in `F_q^*`. This gives the two independent constant quotients in (1.2). For `Gamma_0`, diagonal entries are `t,delta/t`; the invariant is `a(c/D) mod gcd(D,N/D)` modulo constants. Conversely the Chinese remainder theorem solves for `t` precisely when these products agree modulo that gcd up to a constant. Elementary matrices over the Euclidean ring lift the required reductions. To check no extra lift invariant occurs, complete a primitive column to an `SL_2(A)` matrix and choose its second column with the prescribed reduction; the ratio of two such completions lies in the principal congruence subgroup. This proves (1.2).

For a prime `P` of degree `d`, put `Q=q^d`, `B=(A/P)^*/F_q^*`, `r=|B|=(Q-1)/(q-1)`. There are two `B`-torsors, denoted `infinity` and `0`, and

\[
 h_0(P)=2,\qquad h_1(P)=2r=2,\ 2(q+1),\ 2(q^2+q+1)\quad(d=1,2,3).
\tag{1.3}
\]

`Gamma_0/(Z Gamma_1)=B`, via the lower right entry. Both cusp permutation representations are regular representations of `B`. Thus the cusp space is `C[B] ⊕ C[B]`, with **two** coordinates per even character, including the trivial character. The formula is `2r`, not `2r+2`.

### H1.2. A finite exact specification of every vertex and edge

**External theorem (Serre, Trees, English edition 1980, II.1–2; Gekeler–Nonnengardt 1995, not byte-cited):** the vertices `v_n=[diag(T^n,1)O_infinity^2]`, `n>=0`, form a fundamental ray for `G` on the `(q+1)`-regular tree. Its vertex stabilizers are `G_0=GL_2(F_q)` and, for `n>=1`, upper triangular matrices with constant nonzero diagonal and upper right polynomial of degree at most `n`. The edge `v_0v_1` has stabilizer `B_0=B(F_q)`; the edge `v_nv_{n+1}`, `n>=1`, has stabilizer `G_n`. The quotient of a finite-index subgroup is consequently obtained by the corresponding double cosets. A primary implementation reference, **not byte-cited**, is [Carbone–Cobbs–Murray, 2009, revised 2012](https://arxiv.org/abs/0909.0062). The elementary ray reduction is also available in the repository: `refs/src/1012.3513/hecke.tex:1364–1366` says “Executing these steps ... will finally lead to a matrix” `p_n`, `n>=0`; the actual steps are `:1339–1361`. This is Lorscheid's GL₂ quotient, not an unweighted graph.

Here is a complete finite recipe, including incidence and stabilizers, avoiding a large unlabelled picture. In `k=A/P`, use

\[
 \Omega_0=\mathbb P^1(k),\qquad
 \Omega_1=(k^2\setminus0)/F_q^*.
\tag{1.4}
\]

These are left coset sets of the effective congruence groups in `G`: a matrix is represented by its bottom row, modulo `k^*` or `F_q^*` respectively. The right action is ordinary row multiplication. At level zero take the `GL_2(F_q)` orbits; at level `n>=1` take the orbits of

\[
 B_n=\left\{\begin{pmatrix}a&b\\0&e\end{pmatrix}:a,e\in F_q^*,\ b\in A,\ \deg b\le n\right\}
\tag{1.5}
\]

on `Omega_i`, reducing the entries modulo `P`. Edges between levels `n,n+1` are the `B_n` orbits, including `n=0`. An edge orbit maps to the two containing vertex orbits. If an orbit has size `o`, its effective stabilizer order is `q(q^2-1)/o` at level zero and `(q-1)q^{n+1}/o` at level `n>=1` or at an edge of level `n`. These orders include the reduction kernel when `n>=d`.

For `n>=max(1,d-1)`, the `B_n` orbits are exactly `(0,b)`, `b in B`, and `(a,*)`, `a in B`, for `Omega_1` (one of each for `Omega_0`). Every edge thereafter joins the corresponding orbit to itself at the next level, and its stabilizer multiplies by `q` per step. This proves finite core plus exactly `h_i` disjoint rays, not a finite graph without infinite ends. For arbitrary `N`, the same argument over `A/N`, together with finite index, gives finitely many rays labelled by (1.2).

Our **fixed core cut** consists of levels `0,...,d-1`. All edges to level `d` are the exits; for `d=1` both rays attach to the single level-zero vertex. Parallel edges are retained. This cut is part of every dimension assertion below.

### H1.3. Counts and stabilizers (exact)

In the following table, `s^m` in a stabilizer column means **m vertices with stabilizer order s**, not exponentiation. Lists are by level. Core edges exclude the exits.

| q | d | group | core vertices by level | core edges by level | exits | stabilizer multisets by level |
|---|---|---|---|---|---|---|
| 2 | 1 | both | 1 | 0 | 2 | `2^1` |
| 3 | 1 | both | 1 | 0 | 2 | `6^1` |
| 2 | 2 | Gamma_0 | 2,2 | 3 | 2 | `2^1,3^1`; `4^1,1^1` |
| 3 | 2 | Gamma_0 | 2,2 | 3 | 2 | `6^1,4^1`; `18^1,2^1` |
| 2 | 3 | Gamma_0 | 2,3,2 | 5,3 | 2 | `2^1,1^1`; `4^1,1^2`; `8^1,1^1` |
| 3 | 3 | Gamma_0 | 2,3,2 | 6,3 | 2 | `6^1,1^1`; `18^1,2^1,1^1`; `54^1,2^1` |
| 2 | 2 | Gamma_1 | 4,6 | 9 | 6 | `2^3,1^1`; `4^3,1^3` |
| 3 | 2 | Gamma_1 | 5,8 | 12 | 8 | `6^4,1^1`; `18^4,2^4` |
| 2 | 3 | Gamma_1 | 14,21,14 | 35,21 | 14 | `2^7,1^7`; `4^7,1^14`; `8^7,1^7` |
| 3 | 3 | Gamma_1 | 26,39,26 | 78,39 | 26 | `6^13,1^13`; `18^13,2^13,1^13`; `54^13,2^13` |

These are orbit counts, hence exact proofs by finite enumeration with (1.4)–(1.5), reproduced by `checks/finite_graph.py`. They can also be counted symbolically: for `Gamma_1`, quadratic level has `(r+1,2r)` vertices and `3r` edges; cubic level has `(2r,3r,2r)` vertices and `((q+3)r,3r)` edges. At level zero rank-one `F_q` spans of the two coordinates give `r` orbits with stabilizer `q(q-1)`; the rank-two spans give one orbit at degree two and `r` at degree three, all with trivial stabilizer. Upper triangular orbits give the remaining entries directly by translation by the span of `1,T,...,T^n` and multiplication by `F_q^*`. This also proves the counts do not depend on which irreducible polynomial of the indicated degree is chosen.

For `Gamma_0`, the quadratic level-zero stabilizers are `q(q-1),q+1` and the cubic ones `q(q-1),1`; its cubic intermediate level has orders `(q-1)q^2,q-1,1`. Level-one prime has the familiar two-cusp line, with the central vertex order `q(q-1)` and the two exit-edge orders `q(q-1),q-1`. Stabilizer order greater than one in the table identifies precisely every nontrivial core vertex stabilizer. No stabilizer has been silently discarded as if this were an unweighted covering graph.

## H2. Completion, infinity representation, and every constant term — PROVED / SHARPENED

Author: `codex:gpt-6-astra`

### H2.1. Three parameters and the exact GL₁ completion

Use `u=q^{-s}` for the Eisenstein parameter, `t` for a GL₁ polynomial argument, and `z=q^{s-1/2}=1/(sqrt(q)u)` for 04k scattering. In particular the two GL₁ arguments are **`qu^2` and `u^2`**, with no additional unspecified shift. Character values are roots of unity; “rational” means rational functions with coefficients in their cyclotomic field (and fixed positive square roots of `q` when using symmetric graph coordinates).

For a primitive nonprincipal `chi` of conductor `P` of degree `d`, extend `chi` by zero on nonunits and put

\[
 L(t,\chi)=\sum_{f\text{ monic}}\chi(f)t^{\deg f},\quad
 e_\chi=\begin{cases}1&\chi|_{F_q^*}=1,\\0&\text{otherwise},\end{cases}\quad
 \Lambda_\chi(t)=\frac{L(t,\chi)}{(1-t)^{e_\chi}},\quad m_\chi=d-1-e_\chi.
\tag{2.1}
\]

**External theorem (Rosen 2002, Chapter 9, Dirichlet functional equation; Weil 1948, Riemann hypothesis for curves, not byte-cited):** `L` has degree exactly `d-1`; the quotient (2.1) is a polynomial of degree `m_chi`, constant term one, with every zero of modulus `q^{-1/2}`. It satisfies

\[
 \Lambda_\chi(t)=\epsilon_\chi(\sqrt q\,t)^{m_\chi}
                  \Lambda_{\bar\chi}(1/(qt)),\qquad
 |\epsilon_\chi|=1,\quad\epsilon_\chi\epsilon_{\bar\chi}=1.
\tag{2.2}
\]

Here is an explicit Gauss convention fixing every phase. For `q=p^a`, let `e_q(x)=exp(2 pi i Tr_{F_q/F_p}(x)/p)`, and let `ell_P(b)` be the coefficient of `T^{-1}` in `b/P`, with `deg b<d`. For monic `P`, this is the top coefficient `b_{d-1}`. Set

\[
 \tau_P(\chi)=\sum_{b\in A/P}\chi(b)e_q(\ell_P(b)),\quad
 \tau_\infty(\chi)=\sum_{a\in F_q^*}\chi(a)e_q(a).
\]
\[
 \epsilon_\chi=
 \begin{cases}
 q^{-d/2}\tau_P(\chi),&\chi\text{ even},\\
 \tau_P(\chi)/(q^{(d-1)/2}\tau_\infty(\chi)),&\chi\text{ odd}.
 \end{cases}
\tag{2.3}
\]

“Odd” means nontrivial restriction to `F_q^*`, not necessarily a sign character. A change of the additive character changes the displayed Gauss sums in the prescribed way; (2.3) uses the fixed one above. There is no additional root number multiplying the same-character scattering ratio below.

For completeness, the finite Fourier proof fixes the normalizations without appealing to a guessed analogy. Orthogonality gives `sum_b chi(b)e_q(ell_P(ab))=bar chi(a) tau_P(chi)`. Orthogonal complements of the degree-`<j` subspaces under this pairing are the degree-`<d-j` subspaces. Applying this identity to each monic degree stratum gives the coefficient reversal (2.2). If `B_j=sum_{f monic,deg f=j}chi(f)`, summing over scalar multiples first gives `tau_P=-q B_{d-1}` for even `chi`, and `tau_P=tau_infinity B_{d-1}` for odd `chi`. In the even case the top coefficient of `Lambda` is `-B_{d-1}`. Thus (2.3) is exactly `epsilon=q^{-m/2}[t^m]Lambda`. The elementary identity `|tau_P|^2=q^d` (and `|tau_infinity|^2=q` in the odd case) proves its modulus. The degree and zero-location input in the external theorem is retained explicitly; finite Fourier symmetry alone does not prove the Weil bound.

For the **primitive trivial** character use

\[
 Z(t)=\zeta_K(t)=\frac1{(1-t)(1-qt)},\qquad
 \zeta_A(t)=\frac1{1-qt},\qquad
 \frac{Z(qu^2)}{Z(u^2)}=\frac{1-u^2}{1-q^2u^2}.
\tag{2.4}
\]

`Z` is meromorphic, not a polynomial and not an entire xi-function. The principal character modulo `P` instead has finite series `(1-t^d)/(1-qt)`; that missing Euler factor belongs in the level matrix, not in the primitive trivial `Z`. The infinity Euler factor is `(1-t)^{-1}` for an even character, removing the finite polynomial's factor `1-t`; it is `1` for an odd character, whose infinity character is ramified. This is the Rosen convention required by `notes/deninger-cusp/astra-proofs.md:686` and `report/sections/04o_graded_toys_exits.tex:183–196`.

### H2.2. Infinity spherical vector, cusp heights, and Eisenstein columns

Represent a tree vertex by `g in GL_2(K_infinity)/(K_infinity^* GL_2(O_infinity))`. For a nonzero row `v`, define

\[
 H_v(g)=\frac{|\det g|}{\|vg\|_\infty^2},\qquad
 \|(x,y)\|_\infty=\max(|x|,|y|),\qquad |T|=q.
\tag{2.5}
\]

This is the weight-zero, maximal-compact-invariant infinity vector. It is invariant under central rescaling of `g`. With `g_n=diag(T^n,1)`, `H_{(0,1)}(g_n)=q^n`; its adjacency eigenvalue is `q^s+q^{1-s}`. The repository gives precisely this vector and eigenvalue in `refs/src/2303.09327/main.tex:184–195`, including “the Eisenstein series attached to the cusp” at `:184–187`.

For an even character `psi mod P`, set, initially `Re s>1`,

\[
 E_\infty^\psi(g,s)=\frac1{q-1}
 \sum_{\substack{(c,d)=1\\P\mid c}}\bar\psi(d)H_{(c,d)}(g)^s,
 \quad W_P=\begin{pmatrix}0&-1\\P&0\end{pmatrix},\quad
 E_0^\psi(g,s)=E_\infty^{\bar\psi}(W_Pg,s).
\tag{2.6}
\]

The gcd is monic; the factor `1/(q-1)` quotients primitive rows by units. Both columns transform by `psi(d_gamma)` under `Gamma_0(P)`. Indeed reindex the first sum under `gamma`; conjugation by `W_P` changes the lower right diagonal entry to the upper left one, and `psi(det gamma)=1`. Since `W_P^2=-P I`, it is a projective involution. These observations also fix the inducing-character bookkeeping: the two local sections have ramification in opposite inducing positions; their intertwining characters are `psi` and `bar psi`, but their **diamond nebentypus is the same psi**.

Use scaling matrices `I,W_P` at the two representative cusps; no square root of `P` is required in the local field. At each cusp write `g= sigma_a n(x)g_h`, `h in Z`, and average over the transported unipotent lattice with quotient volume one. The two terms are

\[
 (E_b^\psi|\sigma_a)_0(h,s)=\delta_{ab}u^{-h}
                      +\Phi_\psi(u)_{ab}(qu)^h.
\tag{2.7}
\]

Rows are observing cusps, columns source cusps. This is a height convention, not a literal Euclidean cusp width. In the raw `G`-ray description of H1, the infinity height is `h=n`, the zero-cusp height is `h=n-d`. Indeed `W_Pg_h` is `G`-equivalent to `g_{h+d}`; the unit `P/T^d` is absorbed by the maximal compact. At the fixed cut of H1 the height origins are therefore

\[
 c_\infty=d-1,\qquad c_0=-1.
\tag{2.8}
\]

At either normalized cusp the eventual effective stabilizer is `(q-1)q^{h+1}`. All its diamond translates have the same data. Each even `psi` is singular at both representative cusps: their diagonal stabilizer characters restrict to constants and hence are trivial. Fourier transforming the two torsors, with entries `r^{-1/2}psi(b)`, supplies all `2r` independent incoming coordinates. Concretely the columns (2.6) divided by `sqrt(r)` have these unit incoming Fourier vectors. Inverse Fourier transformation of (2.7) is the constant-term formula at **every actual cusp**; no unsupplied cusp constants remain.

### H2.3. Direct unfolding, including the factor q

Normalize additive Haar measure by `vol(K_infinity/A)=1`, so `vol(O_infinity)=q`. The spherical integral is exactly

\[
 I_\infty(s)=\int_{K_\infty}\max(1,|x|)^{-2s}\,dx
 =q+(q-1)\sum_{j\ge1}q^{j(1-2s)}
 =q\frac{1-u^2}{1-qu^2}.
\tag{2.9}
\]

1. Passing from primitive rows in (2.6) to all nonzero rows multiplies by `L(u^2,bar psi)`. For fixed nonzero `c` divisible by `P`, the average over the residue classes of `d mod P` is zero if `psi!=1`. Thus the diagonal outgoing term at infinity vanishes. Fricke conjugation proves the same at zero.
2. Substitute `W_P` and write `c=Pm`. Homogeneity of the sup norm and `|det W_P|=Q` give exactly

\[
 E_0^\psi(g,s)=\frac{Q^{-s}}{q-1}
       \sum_{(m,n)=1}\psi(m)H_{(m,n)}(g)^s.
\tag{2.10}
\]

3. In the all-row sum, unfold `n in A` and the unipotent average into `K_infinity`. For monic nonzero `m` the integral is `|m|^{1-2s}q^{(1-s)h} I_infinity(s)`. The units cancel `q-1`. Summing over `m` gives `L(qu^2,psi)` and dividing out the primitive-row factor gives

\[
 \boxed{A_\psi(u)=q\,u^d\frac{\Lambda_\psi(qu^2)}{\Lambda_\psi(u^2)}}.
\tag{2.11}
\]

The opposite coefficient has `bar psi`. Absolute convergence in `Re s>1` justifies these operations. The displayed rational functions then give meromorphic continuation; the finite core linear system gives the same continuation of the Eisenstein columns away from its exceptional parameters. This proves the requested all-cusp formula, rather than importing an untranscribed adelic normalization. Lorscheid supplies the general intertwining framework: `refs/src/1012.3223/main.tex:565–568` displays `E_N=f+M f` and the Weyl integral, and says the operator maps the inducing representation to the inverse one. Its `chi^2` convention for a central-trivial inducing pair is **not** permission to replace our explicit `psi` by `psi^2`.

### H2.4. Odd characters — REFUTED for scalar vertices and scalar edges

If `psi` is nontrivial on constants, a scalar `aI` fixes every vertex while its diamond action would multiply a function by `psi(a)`. Such a function is zero. The same scalar fixes oriented and unoriented edges, so replacing vertices by edges does **not** repair this obstruction. The bipartition sign depends on the valuation of the determinant modulo two; it is trivial on `F_q^*` and also does not repair it. The nonzero odd GL₁ polynomial and Gauss formula are (2.1)–(2.3). To realize them automorphically one must specify a nontrivial infinity unit type/coefficient system with the compensating central character; that is a different representation, not weight-zero tree scattering. **OPEN in this note:** scattering for those nonspherical coefficient systems. There is no scalar odd analogue to compute under the stated hypotheses.

## H3. Complete prime-level matrix for degrees one, two, and three — PROVED / SHARPENED

Author: `codex:gpt-6-astra`

### H3.1. Blocks, determinant, and root numbers

Put `R_psi(u)=Lambda_psi(qu^2)/Lambda_psi(u^2)` and

\[
 \phi(u)=q\frac{1-u^2}{1-q^2u^2}.
\tag{3.1}
\]

In the orthonormal diamond basis specified in H2, the answer is the direct sum over the `r` even characters of the following **two-dimensional** blocks:

\[
 \boxed{\Phi_1(u)=\frac{\phi(u)}{1-u^{2d}}
 \begin{pmatrix}
 (Q-1)u^{2d}&u^d(1-Qu^{2d})\\
 u^d(1-Qu^{2d})&(Q-1)u^{2d}
 \end{pmatrix}},
\tag{3.2}
\]
\[
 \boxed{\Phi_\psi(u)=\begin{pmatrix}0&q u^dR_\psi(u)\\
                                q u^dR_{\bar\psi}(u)&0\end{pmatrix}}
 \quad(\psi\ne1,\ \psi\text{ even}).
\tag{3.3}
\]

These are full matrices, not determinants offered in place of matrices. The original cusp matrix is `U (direct sum Phi_psi) U^*`, where `U_{(a,b),(psi,a')}=delta_{a,a'}psi(b)/sqrt(r)` on the two torsors of H1. This also specifies every entry as a finite character sum.

Proof of the remaining trivial block: the level-one constant term is `q^{sh}+phi(u)q^{(1-s)h}`. It follows either from (2.9) and `zeta_A(qu^2)/zeta_A(u^2)`, or directly from the central Nagao equation `(q^s+q^{1-s})f_0=(q+1)f_1`. The two old sections `E(g,s),E(diag(P,1)g,s)` have incoming matrix

\[
 H(u)=\begin{pmatrix}1&u^{-d}\\u^{-d}&1\end{pmatrix}
\]

and outgoing matrix `phi(u)H(1/(qu))`. Multiplication by `H(u)^{-1}` gives (3.2). This proof fixes the infinity factor and the local missing Euler factor independently. The source at `refs/src/2303.09327/main.tex:388–390` computes a **Dirichlet sum**, namely `Q^{1-2s}/(1-Q^{-2s})` times the finite zeta ratio; it is not by itself a normalized all-cusp matrix. Its residue condition `Y=1 mod P` explains why its local numerator is `Q`, whereas summing all admissible primitive residues for the diagonal coefficient gives `Q-1`. Thus the byte-cited result in `report/sections/04i_cusp_graph_scattering.tex:188–192` cannot be substituted for (3.2) without its other normalizations.

For the Gauss form of a nontrivial block, put `m=d-2`. Equation (2.2) gives exactly

\[
 A_\psi(u)=q^{1+3m/2}u^{d+2m}\epsilon_\psi
       \frac{\Lambda_{\bar\psi}(1/(q^2u^2))}{\Lambda_\psi(u^2)},
 \qquad \epsilon_\psi=q^{-d/2}\tau_P(\psi).
\tag{3.4}
\]

This is an alternative expression for (2.11), not an extra multiplicative constant. The determinants, including signs and multiplicities, are

\[
 \det\Phi_1=-\phi(u)^2 u^{2d}
                  \frac{1-Q^2u^{2d}}{1-u^{2d}},\qquad
 \det\Phi_\psi=-q^2u^{2d}R_\psi R_{\bar\psi},
\tag{3.5}
\]
\[
 \boxed{\det\Phi_P=
 -\phi(u)^2u^{2d}\frac{1-Q^2u^{2d}}{1-u^{2d}}
 (-q^2u^{2d})^{r-1}
 \prod_{\substack{\psi\in\widehat B\\\psi\ne1}}R_\psi(u)^2.}
\tag{3.6}
\]

### H3.2. Functional equation and residue, exactly

Set `u'=1/(qu)`. From (2.2), `R_psi(u)R_barpsi(u')=q^{d-2}`, and hence

\[
 A_\psi(u)A_{\bar\psi}(u')=q^2q^{-d}q^{d-2}=1.
\]

The trivial identity follows from `phi(u)phi(u')=1` and the commuting oldform matrices `H(u),H(u')`. Consequently

\[
 \boxed{\Phi_P(u)\Phi_P(1/(qu))=I_{2r}.}
\tag{3.7}
\]

On `|u|=q^{-1/2}`, conjugation and this identity give unitarity. All identities are meromorphic identities, including removable exceptional points; they are not statements that every individual uncancelled denominator is a pole.

At `u_0=q^{-1}`, no nonprincipal block has a pole: its numerator and denominator arguments are `q^{-1},q^{-2}`, both strictly inside the GL₁ zero circle. The residue in the trivial block and the original cusp basis is

\[
 \mathop{\rm Res}_{u=q^{-1}}\Phi_1(u)
 =-\frac{q^2-1}{2q^2(Q+1)}\begin{pmatrix}1&1\\1&1\end{pmatrix},
\tag{3.8}
\]
\[
 \boxed{\mathop{\rm Res}_{u=q^{-1}}\Phi_P(u)
       =-\frac{q^2-1}{2q^2r(Q+1)}\,\boldsymbol1\boldsymbol1^t.}
\tag{3.9}
\]

It has rank one and represents the constant function. Multiplying the `u`-residue by `-q/log q` converts to the `s=1` residue. The tree also has the bipartite constant twin: there is a rank-one pole at `u=-q^{-1}`, with its type signs. Ignoring it gives the wrong bound-state removal in H4. In particular “the residue” is rank one at the stated point, not a claim that the graph has only one residual state.

### H3.3. Degree-by-degree finite formulas

| d | Q | r | even nontrivial characters | completed degree | nontrivial entry A_psi |
|---|---|---|---|---|---|
| 1 | q | 1 | 0 | not applicable | none |
| 2 | q^2 | q+1 | q | 0 | `q u^2` |
| 3 | q^3 | q^2+q+1 | q^2+q | 1 | `q u^3(1+q c_psi u^2)/(1+c_psi u^2)` |

Here for any cubic prime, exactly

\[
 \Lambda_\psi(t)=1+c_\psi t,\qquad
 c_\psi=1+\sum_{a\in F_q}\psi(T+a),\quad |c_\psi|=\sqrt q,
 \quad \epsilon_\psi=c_\psi/\sqrt q.
\tag{3.10}
\]

These character sums are an exact finite specification of every coefficient for **any** prime of degree three, also for `q=5`. At degree two `epsilon_psi=1` and `tau_P(psi)=q`; an even nontrivial character of degree one does not exist. For the blind lane's canonical cubics, these specialize particularly simply:

\[
 \begin{array}{ll}
 q=2,\ P=T^3+T+1:& c_k=1+\zeta_7^k+\zeta_7^{3k},\quad1\le k\le6,\\
 q=3,\ P=T^3-T-1:& c_k=1+\zeta_{13}^k+\zeta_{13}^{3k}+\zeta_{13}^{9k},\quad1\le k\le12.
 \end{array}
\tag{3.11}
\]

In both lines `psi_k([T])=zeta_r^k`; `[T]` generates `B`. For other primes use (3.10), or, in all degrees, the finite sum over monics of degree `<d` in (2.1). Formula (3.2) with `d=1,2,3` supplies the entire trivial block with no extra data. Thus (3.2), the table, and (3.10) are the complete requested theorem, not just a template depending on unspecified local constants.

### H3.4. The exact correction to H-ARITH-1

**REFUTED:** the assumption at `report/sections/04o_graded_toys_exits.tex:174–177` as written. Only even characters occur; each has multiplicity two; the trivial block has a nonmonomial rational level factor. The diamond acts as `psi(b) I_2` on the whole `psi` block. The two GL₁ labels `psi,bar psi` in its off-diagonal entries are not two different diamond eigenvalues within that block. For complex characters a constant simultaneous diagonalization need not exist; at quadratic level the identical degree-zero ratios do allow a constant diagonalization, but still give **two** channels per character. For real characters the sum/difference basis also gives two scalar channels. Thus “never diagonalizable” would be an overcorrection.

**PROVED replacement:** at the prime levels considered, spherical `Gamma_1(P)` scattering is Fourier block-diagonal with (3.2)–(3.3), and its nonprincipal entries are exactly the monomial `q u^d` times the **completed** Dirichlet ratio. This matches the structure, though not the archimedean constants, of `notes/deninger-cusp/astra-proofs.md:224–255,265–306`.

## H4. The exact finite cavity and the model space — SHARPENED

Author: `codex:gpt-6-astra`

### H4.1. Orientation and cut are essential

**REFUTED literally:** `Phi_1` itself is not the 04k scattering matrix at the stated cut. The notebook defines incoming `z^{-k}` and outgoing `z^k` (`report/sections/04k_elliptic_cavity_scattering.tex:49–53`), whereas (2.7) has incoming `z^h` after symmetrization. With `D(z)=diag(z^{d-1},z^{-1})`, the graph matrices are exactly

\[
 \boxed{S_\psi(z)=D(z)\Phi_\psi(1/(\sqrt qz))^{-1}D(z).}
\tag{4.1}
\]

The same diagonal is repeated on every character block. To prove this, use `g=f/sqrt(S(v))`, so, up to the same constant on all normalized cusps, `g_h=z^h a+z^{-h}Phi a`. Substitute `h=c_a+k` from (2.8) and solve for outgoing in terms of incoming. This gives the congruence, not a similarity. The normalization `T=q^{-1/2}A` after conjugating by the square root of the stabilizer measure is exactly `report/sections/04k_elliptic_cavity_scattering.tex:72–79`.

Every finite 04k core satisfies `S(0)=W^*W-I`, by expanding `(z+z^{-1}-T_X)^{-1}=zI+O(z^2)`. But the off-diagonal entries of `Phi_1(1/(sqrt(q)z))` have a pole of order `d` at zero. Therefore no finite fixed-cut core realizes that **Eisenstein-oriented** matrix as `S`. This is the same obstruction proved for the rational-side local factor in `notes/level-local-cavity/astra-proofs.md:77–86`; its inverse weighted-edge realization at `:88–95` is not a substitute for the arithmetic cusp normalization here.

### H4.2. Explicit two-exit core for the entire trivial block

The trivial diamond sector is the `Gamma_0(P)` weighted quotient. The following symmetric cores, with unlisted entries zero and listed edges counted symmetrically, realize exactly (4.1). Normalized parallel edges are summed.

| d | n | nonzero edges of T_X | W (exit columns infinity,0) |
|---|---|---|---|
| 1 | 1 | `T_X=[0]` | row `(1,sqrt(q))` |
| 2 | 4 | `AC=1, AD=1, BD=sqrt((q^2-1)/q)` | `(e_C,e_D)` |
| 3 | 7 | `AC=1, AD=1, BD=sqrt((q-1)/q), BE=sqrt(q), CF=1, DG=1/sqrt(q), EG=sqrt((q-1)/q)` | `(e_F,e_G)` |

At degree two `A,B` are level zero and `C,D` level one. At degree three `A,B` are level zero, `C,D,E` level one, `F,G` level two. These weights follow from each H1 edge by `sqrt(S(v)S(w))/(sqrt(q)S(e))`. In the cubic case there are `q` parallel edges `BE`, each of weight `1/sqrt(q)`, giving the stated total. All standard rays beyond these exits have unit normalized edges. Thus the finite arithmetic core, including couplings and the cut, is fully specified.

Put `C=WW^*`, `G_X=(z+z^{-1}-T_X)^{-1}`, `Q_X(z)=I_2-zW^*G_XW`. The finite-core elimination theorem, byte-cited as the formula `S=-Q(z)^{-1}Q(1/z)` in `report/sections/04k_elliptic_cavity_scattering.tex:91–102`, gives

\[
 S_1(z)=-Q_X(z)^{-1}Q_X(1/z),\qquad
 p_1(z)=\det((1+z^2)I-zT_X-C),\quad
 \widetilde p_1(z)=z^{2n}p_1(1/z),\quad \det S_1=p_1/\widetilde p_1.
\tag{4.2}
\]

Define the explicitly monic polynomial

\[
 C_d(z)=\frac{z^{2d}-q^{-d}}{z^2-q^{-1}}
       =\sum_{j=0}^{d-1}q^{-j}z^{2(d-1-j)},\qquad
 C_d^*(z)=z^{2d-2}C_d(1/z).
\tag{4.3}
\]

For all three rows, direct determinant expansion yields

\[
 \boxed{p_1=z^{4d-4}(z^2-q)C_d(z),\qquad
 \widetilde p_1=(1-qz^2)C_d^*(z).}
\tag{4.4}
\]

The degrees are `2n=2,8,14`. This is also an algebraic check of the oldform answer: the determinant of (4.1), using (3.5), simplifies to (4.4). `checks/exact_cavity.py` verifies (4.4) by independent symbolic determinants of the displayed quotient cores for `q=2,3`; the same finite expansion proves the formula for symbolic `q`.

The exact spectral classification is:

* Two simple visible bound states, at `z=+q^{-1/2}` and `z=-q^{-1/2}`, with eigenvalues `±(q+1)/sqrt(q)`. They are the normalized constant function and its bipartite twin. Their reciprocal roots `±sqrt(q)` occur in `p_1`.
* `2d-2` nonzero local resonances, all simple: `z=q^{-1/2}exp(pi i k/d)`, `0<=k<2d`, excluding `k=0,d`. Equivalently they are the roots of `C_d`. There are none at linear level, the pair `±i/sqrt(q)` at quadratic level, and the four remaining sixth-root directions at cubic level.
* `4d-4` delay modes at zero, counted algebraically. There are no invisible core eigenvectors and no threshold factors in this trivial sector: (4.4) and its reversal have no common root. In particular no root at `±1` is being discarded by hand.

Only the **completed trivial block together with its local level factor** is being realized here. A separate scattering realization of the oldform factor in its own variable need not have the arithmetic tree's cusps or cut. Nor can “local modes” exclude delays when quoting a Hardy model dimension.

### H4.3. Arithmetic blocks are already rational inner after the inversion

For even nonprincipal `psi`, put `m=d-2`. Applying (2.2) to (4.1) gives

\[
 S_\psi(z)=\begin{pmatrix}0&f_\psi(z)\\f_{\bar\psi}(z)&0\end{pmatrix},\qquad
 \boxed{f_\psi(z)=q^{-m/2}z^{2d-2}
             \frac{\Lambda_\psi(z^2)}{\Lambda_\psi(z^2/q)}}.
\tag{4.5}
\]

Each `f_psi` is a scalar rational inner function. Its denominator zeros have modulus `q^{1/4}>1`; its numerator zeros have modulus `q^{-1/4}<1`, besides its specified power of zero. On `|z|=1`, (2.2) proves that the modulus of the polynomial ratio is `q^{m/2}`, exactly cancelled by its prefactor. This is where Weil's theorem enters the finite dissipative model. There is no Gauss phase missing: it has cancelled between the numerator and denominator when (2.2) is used twice.

A fixed **right** swap changes (4.5) to `diag(f_psi,f_barpsi)` and leaves its Hardy range unchanged. This is an exact model-space decomposition, even when no fixed similarity diagonalizes the scattering family. Each scalar function has degree `2d-2+2m=4d-6`; hence each nontrivial character block contributes

\[
 \underbrace{4(d-2)}_{\text{arithmetic square-root modes}}
 +\underbrace{4d-4}_{\text{delay modes}}=8d-12.
\tag{4.6}
\]

There are no nonzero local resonances in these primitive nontrivial blocks. At quadratic level the block is simply `z^2` times the swap. At cubic level it is a pair of degree-six inner functions, each with a delay of order four and two arithmetic zeros.

The full core determinants can also be specified exactly. A nonprincipal block has core dimension `3` at degree two and `7` at degree three (Fourier transform the layer counts of H1). Its monic determinant is

\[
 p_\psi(z)=q^{-m}z^{4d-4}(z^2-1)
                 \Lambda_\psi(z^2)\Lambda_{\bar\psi}(z^2).
\tag{4.7}
\]

Indeed (4.5) supplies the entire nonthreshold divisor. At each threshold `z=±1`, the off-diagonal matrix has eigenvalues `+1,-1`, supplying one bounded non-square-summable solution and one threshold factor at each sign. The product in (4.7) has precisely the core degree `6` or `14`, so there is no room for an additional reciprocal cusp-form factor. Equivalently one may Fourier transform the finite matrix of (1.4) and take its determinant. Thus

\[
 p_{\Gamma_1}=p_1\prod_{\psi\ne1}p_\psi,
\tag{4.8}
\]

with reversal at the full core degree. Only the `r-1` copies of `z^2-1` cancel at thresholds. This is a matrix-level statement: no cancellation of a scalar determinant is being used to erase a pole in another channel. In the trivial block each bound pole has rank one; its second direction is finite and nonzero there. The other blocks are holomorphic and invertible at those two points. Hence their removal cannot conceal a cross-channel zero/pole collision.

### H4.4. Exact finite model degrees and exits

Use the **defined** model from `report/sections/04l_elliptic_cavity_channel.tex:24–29`: `Theta=eta S B_bd`, with the ordered right Blaschke–Potapov product removing bound poles. The cited theorem at `:41–48` states “dim K = deg det Theta” and “rank J <= h”; its identification with the geometric wave compression is separately conditional at `:57`. Here the rational-inner model is proved, while that general wave-space identification is not newly asserted.

Only the trivial block needs pole removal. Its two rank-one factors have determinant `b_a(z)b_{-a}(z)`, `a=q^{-1/2}`, and

\[
 \det\Theta_1(z)=z^{4d-4}\frac{C_d(z)}{C_d^*(z)}
\tag{4.9}
\]

up to the immaterial constant `det eta`. Multiplying (4.4) by `b_a b_-a` proves (4.9). Its model degree is `6d-6`. Together with (4.6),

\[
 \boxed{\dim K_{\Gamma_1(P)}=(6d-6)+(r-1)(8d-12)}\quad(d=2,3),
 \qquad \dim K_{\Gamma_1(P)}=0\quad(d=1).
\tag{4.10}
\]

The complete split at the fixed core cut is

| q | d | completed GL₁ roots, once per even nontrivial character | arithmetic model modes | nonzero local modes | delays | dim K | cusp exits h |
|---|---|---|---|---|---|---|---|
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| 3 | 1 | 0 | 0 | 0 | 0 | 0 | 2 |
| 2 | 2 | 0 | 0 | 2 | 12 | 14 | 6 |
| 3 | 2 | 0 | 0 | 2 | 16 | 18 | 8 |
| 2 | 3 | 6 | 24 | 4 | 56 | 84 | 14 |
| 3 | 3 | 12 | 48 | 4 | 104 | 156 | 26 |

For comparison `Gamma_0(P)` has two exits and dimensions `0,6,12` for `d=1,2,3`. In general the columns in the table are `(d-2)(r-1)`, `4(d-2)(r-1)`, `2d-2`, and `4(d-1)r`, with the first two zero at linear level. The factor four between the first two columns comes from **two L-occurrences across the full character matrix and two square roots in the tree variable**. Counting just `(d-2)` per character gives neither the scattering determinant multiplicity nor the 04l Hardy model dimension.

There are `h=2r` geometric ray coordinates. The defined model has zero defect at linear level because its space is zero; the phrase “one exit per cusp” must not assert a nonzero model exit in that case. In all cases the theorem gives `rank J<=h`; it is this bound, not a count of one independent exit for each arithmetic zero, that is used for the renewal construction. Moving any cusp cut outward by `k` adds `2k` to `deg det Theta` and changes the delay sector. The nonzero divisor and its arithmetic/local radii are unchanged. The numerical dimensions above are consequently **cut-specific**, not invariants of the abstract congruence subgroup without a normalization.

### H4.5. H-CLASS and the precise comparison with Q

The Fourier transform is exactly the transform on the ray-class group `B=k^*/F_q^*`, but the cusp set consists of **two torsors** for it. `Pic(F_q[T])` itself is trivial. In `report/sections/04p_gl1_bond.tex:67–79`, the level-one curve quotient has **one** `Pic(R)`-torsor; its proposed group matrix times inversion pairs inverse characters. Our scattering instead commutes with diamonds and has a two-dimensional multiplicity block for each individual `psi`. These are different representations of the cusp symmetries. Calling them identical inverse-character blocks would repeat the correction already made in `notes/deninger-cusp/astra-proofs.md:198`.

What agrees with the rational-side D3 is the two-torsor decomposition, evenness from the scalar center, opposite inducing positions with the same nebentypus, and the two old sections for the trivial block. What changes is `|P|=q^d`, the local infinity integral (2.9) in place of the Gaussian/gamma integral, the factor `q u^d` in place of the rational conductor/gamma normalization, and a rational function in a single disk variable in place of an infinite zero/delay space on a logarithmic continuous clock. This is precisely the limitation required by D6 at `notes/deninger-cusp/astra-proofs.md:684–686`.

## Numerical checks for the blind lane

Author: `codex:gpt-6-astra`

The proofs above are exact. The following checks have also been **run**, with integer finite-field arithmetic, SymPy for core determinants, and double precision only for character values and resolvent comparisons. They do not replace the proofs or claim rigorous floating-point error intervals.

### N1. Quotient graphs, with all stabilizers retained

Run `python3 notes/h-arith-fqt/checks/finite_graph.py`. It constructs both `Gamma_0` and `Gamma_1` from the finite coset sets, without using any scattering formula. The requested `q=2` primes are `T`, `T^2+T+1`, `T^3+T+1`; the `q=3` primes are `T`, `T^2+1`, `T^3-T-1`. Polynomials are encoded low coefficient first. Representatives are lexicographically minimal row pairs after scalar quotient; orbit and edge lists are printed in this deterministic order. Each edge is printed as `(source orbit index,target orbit index,stabilizer order)`, separately for each pair of consecutive levels, including exits. This reproduces H1's vertex counts, edge counts, all nontrivial stabilizers, and cusps. The script checks the exact weighted valence `sum_e S(v)/S(e)=q+1` at every core vertex, and `q` on the incoming edge at every first tail vertex (the next tail edge contributes one). Thus it checks the graph-of-groups weights, not just the topological shape.

For example the `q=2` quadratic `Gamma_0` core has vertex orders `(2,3;4,1)` and three edge triples `(0,0,2),(0,1,1),(1,1,1)` between its two levels. Its two exits have orders `4,1`. The cubic `Gamma_0` core has orders `(2,1;4,1,1;8,1)`, first-level edge triples `(0,0,2),(0,1,1),(1,1,1),(1,2,1),(1,2,1)`, and second-level triples `(0,0,4),(1,1,1),(2,1,1)`. Its exits have orders `8,1`. The larger `Gamma_1` graphs are specified by exactly the same finite orbit recipe, with respectively `1,10,49` core vertices and `2,6,14` exits; their edge lists are determined without a choice of unknown geometric data.

### N2. Direct primitive-row summation and its explicit truncation bound

Run `python3 notes/h-arith-fqt/checks/direct_sums.py`. For every monic `m` of degree at most `M=5`, it enumerates **all** residues `n mod m` with `(m,n)=1`, using polynomial Euclid. These are primitive-row orbits under unipotent translation. It sums their character weights and truncates the infinity integral to the shells `|x|<=q^J`, `J=6`. Thus it directly checks the constant-term unfolding rather than reconstructing an L-ratio from its own coefficients. The off-diagonal finite sum is

\[
 u^d I_J(u)\sum_{\deg m\le M}\psi(m)\varphi(m)u^{2\deg m},\qquad
 I_J=q+(q-1)\sum_{j=1}^J(qu^2)^j.
\tag{N.1}
\]

The principal diagonal sum restricts to `P|m` and omits `u^d`. For a nonprincipal diagonal it sums `bar psi(n)` over the primitive residues, obtaining zero for each admissible `m`. At linear level the off-diagonal test uses the principal character modulo `P`, with its missing Euler factor, and compares to (3.2).

For real `0<u<1/q`, let `rho=q^2u^2`. The omitted off-diagonal sum is bounded in absolute value by

\[
 u^d\left[I_\infty(u)\frac{\rho^{M+1}}{1-\rho}
 +\frac{(q-1)(qu^2)^{J+1}}{(1-qu^2)(1-\rho)}\right].
\tag{N.2}
\]

Use the same bound without `u^d` for the principal diagonal. This follows simply from `varphi(m)<=q^{deg m}` and the `q^n` monics of degree `n`; no cancellation is assumed in the error estimate. At `u=.17,.23` every direct sum passed this bound for all six cases. The program enumerates 683 primitive residue rows for `q=2` and 44,287 for `q=3` per modulus. For the cubic nonprincipal off-diagonal entries, errors were at most `5.17e-9` (`q=2`) and `1.12e-7` (`q=3`). Principal sums converge more slowly; e.g. the cubic `q=3,u=.23` diagonal error was `0.00179`, below the conservative bound `0.0751`. This is an honest bounded truncation, not a claim of machine precision for an infinite series.

### N3. Two exact evaluation points, matrix functional equations, and determinants

For a compact exact test, write the trivial block as `[[a,b],[b,a]]`. Its entries at two rational values are:

| q | d | (a,b) at u=1/5 | (a,b) at u=1/4 |
|---|---|---|---|
| 2 | 1 | `(2/21,46/105)` | `(1/6,7/12)` |
| 2 | 2 | `(1/91,207/2275)` | `(1/34,21/136)` |
| 2 | 3 | `(2/1953,4462/244125)` | `(1/234,73/1872)` |
| 3 | 1 | `(3/8,33/40)` | `(6/7,39/28)` |
| 3 | 2 | `(3/52,231/1300)` | `(24/119,741/1904)` |
| 3 | 3 | `(13/1736,7799/217000)` | `(2/49,313/3136)` |

Every nontrivial quadratic block has off-diagonal entries `q/25` and `q/16` respectively, with zero diagonal. For each cubic character of (3.10)–(3.11), its upper-right entries at these two points are exactly

\[
 \frac q{125}\frac{25+qc_\psi}{25+c_\psi},\qquad
 \frac q{64}\frac{16+qc_\psi}{16+c_\psi},
\tag{N.3}
\]

and its lower-left entries use `bar c_psi`. These are finite cyclotomic numbers, not decimals with unknown phases.

Run `python3 notes/h-arith-fqt/checks/verify_scattering.py`. At `u=.17` and `u=.29+.03i`, it computes the entire graph scattering from `T_X,W`, Fourier transforms the actual tail labels, and compares each block with `D Phi^{-1} D`. Largest absolute entry error among the six cases was `8.18e-11`; the matrix functional-equation error was at most `8.90e-15`. It also checks (2.2) and (2.3) for **every primitive nonprincipal character**, including the odd characters solely as GL₁ tests; maximal errors were `1.62e-14` and `1.29e-14` respectively. These tests would detect replacing `psi` by `psi^2`, changing the `q u^d` coefficient, omitting infinity, or using a wrong tail-height shift.

A separate full determinant comparison at `z=.71+.16i,.57+.23i` uses the determinant of the untransformed finite graph matrix and (3.6), with the factor `z^{2(d-2)r}` from the height congruence. Relative errors were at most `7.67e-14` for `q=2,3`. The same determinant and Weil-circle tests also passed at `q=5`, `P=T^2+2,T^3+T+1`, with maximal relative error `2.75e-13` and predicted model dimensions `26,372`. No floating-point determinant was treated as a proof of absence of matrix pole/zero cancellations; that issue is settled blockwise in H4.

### N4. Core polynomials and model dimension

Run `python3 notes/h-arith-fqt/checks/exact_cavity.py`. For each of the six `Gamma_0` cores, it forms the adjacency from the integer stabilizer data, takes the **exact symbolic determinant**, and verifies (4.4) identically. It then counts the roots of `C_d`, the specified zero multiplicities, and the arithmetic polynomial roots used by the character checker. The reported full `Gamma_1` degrees are `0,14,84` and `0,18,156`, with the split in H4.4. For a direct blind check of (4.7)–(4.8), Fourier transform the full core rather than just the tail matrix: quadratic blocks have dimensions `4` (trivial), `3` (each other character); cubic blocks all have dimension `7`. The only removable factors are `z^2-1` in the nontrivial blocks. Remove the two rank-one bound poles of the trivial block, **not a scalar pole factor from all h channels**, before computing `deg det Theta`.

## Corrections to the brief

Author: `codex:gpt-6-astra`

| ID | Verdict | Correction |
|---|---|---|
| C1 | SHARPENED | `Gamma_1` means `c=0,d=1 mod N` inside `GL_2(A)`, with determinant any constant unit; imposing `a=1` or determinant one is a different problem. |
| C2 | REFUTED | The tree quotient is finite core plus infinite rays, not literally a finite graph; stabilizer weights are necessary. |
| C3 | SHARPENED | Prime-level cusp count is `2r`, with the trivial character already among the r even characters. |
| C4 | REFUTED | One scalar channel per arbitrary Dirichlet character: only even characters occur, each with two cusp coordinates. |
| C5 | SHARPENED | `u=q^{-s}`, GL₁ argument `t`, and tree variable `z=1/(sqrt(q)u)` must not be identified. |
| C6 | PROVED correction | The nonprincipal coefficient is exactly `q u^d Lambda_psi(qu^2)/Lambda_psi(u^2)` in the declared height convention. |
| C7 | REFUTED | The principal completion is not a polynomial; the infinity-completed rational zeta ratio needs the factor q from Haar normalization. |
| C8 | REFUTED | Scalar edge functions and the bipartition sign do not realize odd diamond characters; a nontrivial infinity type is required. |
| C9 | REFUTED | The two GL₁ labels inside a psi block are not its two diamond eigenvalues; the diamond is `psi I_2`. |
| C10 | REFUTED | Eisenstein Phi is not the 04k finite-core S; invert it and perform the explicit height congruence (4.1). |
| C11 | SHARPENED | Both residual tree modes, constant and bipartite, must be removed; each pole separately has rank one. |
| C12 | REFUTED | `d-2` roots per even character is not the model dimension: each contributes four arithmetic modes in the full tree model, plus local modes and delays. |
| C13 | SHARPENED | Model degrees and zero delays depend on the core/cusp cut; the table uses exactly levels 0 through d-1. |
| C14 | REFUTED | The two ray-class torsors here are not the single Pic-group torsor in H-CLASS; the two block mechanisms must be distinguished. |
| C15 | SHARPENED | The relevant graph author in the repository is **Nonnengardt**, not Nonnenmacher: `refs/src/1012.3513/hecke.tex:1575–1578`. The level paper is **Kaneko–Koyama**, not Kondo: `refs/src/2303.09327/main.tex:50,55`. |
| C16 | OPEN | General composite-level local matrices, nonspherical odd scattering, and a BC/Shor comparison are not consequences of this prime-level theorem. |

Source scope: Gekeler's *Improper Eisenstein series on Bruhat–Tits trees* (1995) is listed at `refs/src/1012.3513/hecke.tex:1565–1568`, but that bibliography entry is **not** a byte citation of its theorem. Serre (1980), Gekeler–Nonnengardt (1995), Rosen (2002), and Weil (1948) are used only in the precise external-theorem forms stated in H1.2 and H2.1, all marked **not byte-cited**. No unavailable Weil book passage has been represented as read. The local/adelic quotient distinction must also be retained: Lorscheid explicitly warns that for even class number “the correspondence between the local and the global situation breaks down” (`refs/src/1012.4825/elliptic.tex:227`), and introduces the adelic Hecke graph to address it (`:229`). The tree type convention is consistent with `report/sections/02d_definitions_complexes.tex:80–92`; the finite Hashimoto metric theorem at `report/sections/03f_selberg_letters_finite.tex:54–81` concerns a separate retained band and is not a proof of our arithmetic resonance metric or of a graded cancellation.

## H5. What this changes in the notebook

Author: `codex:gpt-6-astra`

**PROVED / SHARPENED:** replace `asm:h-arith-gamma1` (`report/sections/04o_graded_toys_exits.tex:171–177`) at prime degrees one through three by (3.2)–(3.3), for the explicitly defined GL₂ group, even characters, two cusp coordinates, and the infinity-completed L-polynomials; retain the rational trivial block and the graph orientation/cut correction. The quotient now supplies a fully specified finite example of arithmetic resonances plus a local cavity and cusp exits, with the exact model counts in H4; linear level has zero model space, and cubic level is the first of these levels with nonzero arithmetic modes. **SHARPENED:** `prop:character-channel-graded-bond` (`report/sections/04o_graded_toys_exits.tex:180–196`) remains valid for each primitive completed GL₁ ratio as an odd arithmetic factor, but the full level determinant has two L-occurrences per character and its tree model has square-root multiplicity; its psi multiplicity block carries the arithmetic pair `(F_psi,F_barpsi)` with diamond action `psi I`, together with the separately specified local/delay divisor, rather than one Frobenius list per character and one vacuum by decree. The actual model inherits the finite diamond representation because the scattering and the trivial-sector pole removal commute with it. **OPEN:** the stronger `conj:galois-graded-bond` (`report/sections/10_open_problems_dead_routes.tex:81–93`) still needs the BC/Shor comparison map and a justified grading/renewal realization; the incorrect squarefree `Gamma_0` premise must be replaced by `Gamma_1`, and proving the diamond decomposition does not supply that comparison. The conditional geometric wave-compression clause of 04l also remains conditional; the rational-inner model and its finite defect algebra are proved here.

**SHARPENED, with the proposed extension marked SPECULATION:** for an affine elliptic curve with a rational point removed, the standard cusp theorem labels the level-one GL₂ cusps by `Pic(R)=Pic^0`, and the nontrivial unramified GL₁ L-polynomials have degree `2g-2=0`; these are the existing statements of `report/sections/04p_gl1_bond.tex:67–81`, not new prime-level consequences. It is reasonable to seek one common adelic constant-term theorem whose level-one genus-one case yields the equal-depth H-CLASS matrix and whose genus-zero prime-ray-level case yields this note. It is **not** the same theorem obtained by merely replacing `B` with `Pic^0`: the number of torsors, Weyl/character bookkeeping, determinant components, heights, and infinity representation must all be reconciled, especially for even class number as Lorscheid warns. **OPEN as a new derivation here:** a fully normalized proof for arbitrary affine elliptic curves, including the precise passage to the notebook's D2/D3 cores and the inverse-pair Pic blocks; the already recorded example calculations remain their existing results. The next target is that comparison, not an assertion that H-CLASS has automatically become the level-one specialization of (3.3).
