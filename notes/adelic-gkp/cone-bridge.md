# The bridge in genus two: a cone, not a line

Author: `claude:opus-5.5`, 2026-10-06, lane E of an orchestrated session.

Status: **a record, not a round; nothing registered in db/claims.tsv; no REFUTE review; no shard.** Each statement is labelled *standard*,
*proved here*, *checked*, *sketched*, *heuristic*, *open* or *negative finding*. Theorems quoted without a line reference are from memory;
`refs/src/` was not on disk in this session. Checks: `checks/check_cone_bridge.py`, output `checks/output_cone_bridge.txt` (42 of 42 pass;
PARI/GP 2.15.4 through the `gp` binary, sympy, numpy, mpmath; about 3 s).

`curve-bridge.md` §5 showed that in genus one the vacuum form of the GKP lattice is the Rosati form scaled by $1/\sqrt{4q-a^2}$, and remarked that for
several modes the invariant forms make up a cone. This page works out that cone on the genus-two curve of shard 04w and on $K_4$ with one negative edge.
It then asks which point of the cone carries RH and which point the arithmetic picks.

**Findings.**

- **Coordinates on the cone** (proved here, checked). Fix a compatible symplectic form $\Omega$. Every invariant positive form is then
  $\sum_j t_j\,G_\Omega|_j$, with one weight $t_j>0$ per mode, where $G_\Omega$ is the vacuum form of $\Omega$. The Weil form of $\Omega$ has the
  universal weights $t_j=\varepsilon_j\tfrac12\sqrt{4q-\lambda_j^2}=\varepsilon_j\,\mathrm{Im}\,\alpha_j$, where $\varepsilon_j=\pm1$ is the Krein sign of mode $j$ for $\Omega$.
  These are also the Williamson frequencies of the Weil form.
- **The genus-$g$ bridge** (proved here; checked exactly in genus two). Take $L=\mathbb Z[F,V]$ with the cyclic vector $e=1$. The form
  $\Omega_+(x,y)=\mathrm{Tr}\bigl(x\bar y/(V-F)\bigr)$ has Weil form exactly $\tfrac12\mathcal T$ (the Rosati form). Its vacuum is therefore $\mathcal T$ with weight
  $1/\sqrt{4q-\lambda_j^2}$ on mode $j$. That is the expected per-mode version of lane A's scalar. But $\Omega_+$ is principal only in genus one: its determinant is $\mathrm{disc}(h)^2$,
  which is 441 for the curve. The principal form is $\Omega_{\rm can}=\mathrm{Tr}(x\bar y/\mathfrak d)$ with $\mathfrak d=(F-V)h'(F+V)$, and its vacuum carries the extra weight
  $1/|h'(\lambda_j)|$. For the curve, $\mathcal T$ and the vacuum of $\Omega_{\rm can}$ are **not proportional**. The weights are $10.870$ and $20.171$, and their ratio is 04w's $R_0=1.8557$.
- **The Rosati form is not a point of the cone on $L$** (proved here, checked). Transport by a cyclic vector $e$ moves $\mathcal T$ through the whole open cone as $e$
  varies over $\mathbb R$. Even among integral generators of $L$ it moves along an orbit of the real unit group. For the curve that orbit is infinite: $e\mapsto\varepsilon e$
  with $\varepsilon=(5+\sqrt{21})/2$. In genus one this freedom is invisible.
- **Which point the arithmetic picks depends on the 5-adic choice** (checked with PARI). Of the eight primes above 5 in the Galois closure, four give
  the archimedean CM type $\Phi_+$ and four give the mixed type of $\Omega_{\rm can}$. For a mixed choice, the Weil form of the principal polarisation is indefinite,
  of signature $(2,2)$. For $K_4$ with one negative edge it is indefinite, of signature $(4,4)$, for every choice. There the Riemann form of Howe's principal polarisation is
  the vacuum with weights $(\varphi^3,1,1,\varphi^{-3})$. These weights are not the function of $\lambda_j$ found in example 1 (negative finding).
- **RH is that the cone is non-empty** (standard). This condition does not involve $\Omega$. Its witness is the Weil form of a type-$\Phi_+$ form, for example $\Omega_+$ or the
  graph form, which exists before RH is known. The polarisation is a further point. It decides integrality, not RH. It also shows that
  `lattice-tower.md` §5's "(i)$\Rightarrow$(ii)" needs an orientation hypothesis (§5 below).

---------------------------------------------------------------------------------------------------------------------

## 1. Setting

The conventions are those of `lattice-tower.md` §1 and `curve-bridge.md` §1. $L=\mathbb Z^{2g}$ carries the standard $\Omega$, and the step $M$ satisfies $M^T\Omega M=q\Omega$. Its adjoint is $V=qM^{-1}$.
Let $\chi$ be the characteristic polynomial of $M$, and write $\chi(x)=x^gh(x+q/x)$, where $h$ is the real Weil polynomial with roots $\lambda_j$ (the traces of the Frobenius
pairs). Throughout, $\chi$ is squarefree and $|\lambda_j|<2\sqrt q$. The **modes** are $V_j=\ker(M^2-\lambda_jM+q)$, with projectors
$\pi_j=\prod_{k\ne j}(M+V-\lambda_k)/(\lambda_j-\lambda_k)$. The eigenvalues of $M$ on $V_j$ are $\alpha_j,\bar\alpha_j$, with $\mathrm{Im}\,\alpha_j=\tfrac12\sqrt{4q-\lambda_j^2}$.

- **Similitude forms**: symmetric $B$ with $M^TBM=qB$. The **cone** $\mathcal C(M)$ is the set of positive definite ones.
- **Compatible forms**: alternating $\Omega'$ with $M^T\Omega' M=q\Omega'$. Each has a CM type $\Phi_{\Omega'}$ (`howe-positivity.md` §1). On mode $j$ its **Krein sign**
  $\varepsilon_j(\Omega')$ is the sign of $\Omega'(x,(M-V)x)$ for $x\in V_j$. $\Phi_+$ is the type with $\mathrm{Im}\,\varphi(F)>0$. It is the type of $\Omega'$ exactly when all $\varepsilon_j=+1$.
- **Vacuum of $\Omega'$**: the complex structure $J_{\Omega'}$ that commutes with $M$ and has $G_{\Omega'}=\Omega'(\cdot,J_{\Omega'}\cdot)>0$.
- **Weil form of $\Omega'$**: $W_{\Omega'}=\tfrac12\Omega'(\cdot,(M-V)\cdot)$.
- **Rosati form** (analytic §14, Proposition 15): $\mathcal T(\varphi,\psi)=\mathrm{Tr}_{H^1}(\varphi(F)\psi(V))$ on $\mathbb R[F]$, with Gram matrix $\mathcal T_{ik}=\mathrm{Tr}(F^iV^k)$ in the basis $1,F,\dots,F^{2g-1}$.
  It is transported to $L$ by a cyclic vector $e$: $\psi_e(\varphi)=\varphi(M)e$, and $\mathcal T_L=\Psi^{-T}\mathcal T\Psi^{-1}$ with $\Psi=[e,Me,\dots]$.

## 2. The cone and its distinguished points (general $g$)

**Proposition 1** (*standard*; the abstract form is the notebook's `thm:deninger-invariant-polarisation`, and 04w's `prop:genus-two-metric-cone` for $g=2$).
(a) $\mathcal C(M)\neq\emptyset$ if and only if $M$ is semisimple with all eigenvalues of modulus $\sqrt q$. This involves no $\Omega$.
(b) Under the standing hypotheses, the similitude forms make up a $g$-dimensional space. They are block-diagonal over the modes, with one real parameter per mode,
and $\mathcal C(M)$ is the open positive orthant in these parameters.

*Proof.*
(a) If $B>0$ is a similitude form, then $M/\sqrt q$ is $B$-orthogonal. Conversely, average any positive form over the compact closure of the group generated by $M/\sqrt q$.
(b) Over $\mathbb C$, $B$ pairs the eigenvalue $\mu$ only with the eigenvalue $q/\mu=\bar\mu$. Since $\alpha_j\ne\bar\alpha_j$ when $\lambda_j^2<4q$, we have $\alpha_j^2\ne q$, and $B$ vanishes on each eigenline. Distinct $\lambda_j$ make it block-diagonal, so it is fixed on $V_j$ by the single number $B(v,\bar v)$. ∎
Checked: Q1 and G2 (the dimension is 2 for the curve and 4 for $K_4$), X2 (for the hyperbolic step the only similitude forms are indefinite).

**Proposition 2** (*proved here*). Let $\Omega'$ be a compatible form. On $V_j$, $(M-V)^2=-(4q-\lambda_j^2)$, so $J_{\Omega'}=\sum_j\varepsilon_j(M-V)\pi_j/\sqrt{4q-\lambda_j^2}$ and
$$
W_{\Omega'}=\sum_j\varepsilon_j\,\tfrac12\sqrt{4q-\lambda_j^2}\;G_{\Omega'}|_{V_j}.
$$
*Proof.* On $V_j$, $V=\lambda_j-M$, so $M-V=2M-\lambda_j$ and $(2M-\lambda_j)^2=4(\lambda_jM-q)-4\lambda_jM+\lambda_j^2$. The operator $(M-V)\pi_j/\sqrt{4q-\lambda_j^2}$ is a complex structure on $V_j$ that commutes with $M$.
The commutant of an elliptic $2\times2$ block is $\mathbb C$, so it equals $\pm J_{\Omega'}|_{V_j}$, and the sign is the Krein sign. ∎
So the Weil form is positive if and only if every $\varepsilon_j=+1$. Its Williamson frequencies (the symplectic eigenvalues of $|W|$) are $\mathrm{Im}\,\alpha_j$, and those of $G$ are all 1. Checked: Q3–Q6, G3.

**Proposition 3** (*proved here*). The map $\Omega'\mapsto W_{\Omega'}$ is a linear isomorphism from the $g$-dimensional space of compatible alternating forms onto the space of
similitude forms. $W_{\Omega'}$ lies in the cone if and only if $\Phi_{\Omega'}=\Phi_+$.

*Proof.* $M^T\Omega'=\Omega'V$ gives symmetry and $M^TW_{\Omega'}M=qW_{\Omega'}$. Compatible forms are $\Omega'(\cdot,p(F+V)\cdot)$ with $p$ real, and the weights of $W$ become $p(\lambda_j)\varepsilon_j\mathrm{Im}\,\alpha_j$.
The rest follows from Proposition 2. ∎ Checked: X1, on both examples.
**Every point of the cone is therefore the Weil form of exactly one compatible form of type $\Phi_+$.**

**Proposition 4** (*proved here*; the Rosati form transported by a cyclic vector). Write $K=\mathbb Q[F]$. Fix a cyclic $e$ and write $\Omega'(ae,be)=\mathrm{Tr}_{K\otimes\mathbb R}(\zeta_e\,\bar ab)$, with
$\bar\zeta_e=-\zeta_e$. Then
$$
\mathcal T_L=\sum_j\frac{1}{|\varphi_j(\zeta_e)|}\,G_{\Omega'}|_{V_j}=\sum_j\frac{2}{G_{\Omega'}(\pi_je)}\,G_{\Omega'}|_{V_j},\qquad \zeta_{ue}=u\bar u\,\zeta_e .
$$
*Proof.* In the coordinates $x_j=\varphi_j(a)$, $\varphi_j\in\Phi_+$, we have $\mathcal T=\sum_j2|x_j|^2$ and $\Omega'(x,Jx)=\sum_j2|\varphi_j(\zeta_e)||x_j|^2$. ∎
As $u$ runs over $(K\otimes\mathbb R)^\times\cong(\mathbb C^\times)^g$, the factors $|u(\alpha_j)|^2$ cover the whole orthant. **So "the Rosati form on $L$" is the whole open cone until a
cyclic vector is chosen.** If $L$ is a free $\mathbb Z[F,V]$-module, its integral generators differ by units, and the real units $\eta$ move the point by $\eta(\lambda_j)^2$. That is an
infinite orbit when $g\ge2$, since the unit rank of the real order is $g-1$. Checked: U1–U2 (the curve) and G10 (the $e$-dependence for $K_4$).

**Theorem 5** (*proved here*; the genus-$g$ bridge). Let $L=\mathbb Z[F,V]$ and $e=1$, and put $\mathfrak d=(F-V)\,h'(F+V)$.
1. $\Omega_{\rm can}(x,y)=\mathrm{Tr}(x\bar y/\mathfrak d)$ is integral, alternating, unimodular and compatible. The ring $\mathbb Z[F,V]=\mathbb Z[F+V][F]$ is a tower of monogenic extensions, so Euler's lemma
   applied twice makes $\mathfrak d^{-1}\mathbb Z[F,V]$ the trace dual (*standard*, from memory). Its Krein signs are $\varepsilon_j=-\mathrm{sgn}\,h'(\lambda_j)$. They alternate along the ordered
   $\lambda_j$, so for $g\ge2$ the type of $\Omega_{\rm can}$ is never $\Phi_+$.
2. $\Omega_+(x,y)=\mathrm{Tr}(x\bar y/(V-F))=-\Omega_{\rm can}(x,h'(F+V)y)$ is integral, of type $\Phi_+$, and of determinant $N_{K/\mathbb Q}(h'(F+V))=\mathrm{disc}(h)^2$. **Its Weil form is exactly half
   the transported Rosati form:** $\tfrac12\Omega_+(x,(M-V)x)=\tfrac12\mathrm{Tr}(x\bar x)=\tfrac12\mathcal T_L(x,x)$.
3. Hence
$$
\mathcal T_L=\sum_j\sqrt{4q-\lambda_j^2}\;G_{\Omega_+}|_{V_j}=\sum_j|h'(\lambda_j)|\sqrt{4q-\lambda_j^2}\;G_{\Omega_{\rm can}}|_{V_j}.
$$
   In genus one, $h'=1$ and $\Omega_+=\Omega_{\rm can}$, and this is lane A's identity, including the scalar $\sqrt{4q-a^2}$ (R9 rechecks E1–E3). In genus two,
   $|h'(\lambda_1)|=|h'(\lambda_2)|=\sqrt{\mathrm{disc}\,h}$, so $G_{\Omega_+}=\sqrt{\mathrm{disc}\,h}\;G_{\Omega_{\rm can}}$ (R8). For $g\ge3$ the two vacua are no longer proportional.

*Proof of 2.* $\overline{(F-V)x}=(V-F)\bar x$, so $\Omega_+(x,(F-V)x)=\mathrm{Tr}\bigl(\tfrac{1}{V-F}(V-F)x\bar x\bigr)$. The type follows from $\varphi(V-F)=-2i\,\mathrm{Im}\,\varphi(F)$. Part 3 is Propositions 2 and 4 with
$\zeta=1/(V-F)$ and $\zeta=1/\mathfrak d$. ∎ Checked: K3–K4, R6–R9, with exact arithmetic in $\mathbb Q(\sqrt{21})$.

So the brief's expected statement, "the Rosati form is the vacuum form with weight $\sqrt{4q-\lambda_j^2}$ on mode $j$", holds for $\Omega_+$ with $e=1$. For the
principal form it needs the extra factor $|h'(\lambda_j)|$. For any other marking it needs the factors $|u(\alpha_j)|^{-2}$.

## 3. Example 1: $y^2=x^5+x^3+x^2-2$ over $\mathbb F_5$

**Data** (checked, C1–C5). PARI's `hyperellcharpoly` gives $\chi=x^4-3x^3+7x^2-15x+25$, and brute force gives $N_1=3$, $N_2=31$, so
$P(T)=1-3T+7T^2-15T^3+25T^4$ as in 04w. The curve is ordinary (the middle coefficient 7 is prime to 5). The real Weil polynomial is $h=y^2-3y-3$, with
$\lambda_{1,2}=(3\pm\sqrt{21})/2=3.7913,\,-0.7913$. The mode angles are $\theta_j/\pi=0.17795$ and $0.55662$. Further, $\mathrm{disc}\,O_K=48069=21^2\cdot109$ and $h_K=4$.

**Two small negative findings** (checked).
- The graph convention $M=\bigl(\begin{smallmatrix}0&-I\\qI&A\end{smallmatrix}\bigr)$ with $A$ symmetric and integral cannot host this isogeny class. It would need $(a-c)^2+4b^2=21$ (C5).
- The companion lattice $\mathbb Z[F]$ is not a Deligne module here. It has index 5 in $O_K=\mathbb Z[\pi,5/\pi]$ and is not $V$-stable (K2). In genus one $\mathbb Z[F]=\mathbb Z[F,V]$ always holds, which is
  why lane A could use the companion matrix.

**The module** (checked, K1–K5). $L=O_K$ has basis $(1,\beta,\pi,\beta\pi)$ and the principal form $\Omega_{\rm can}$. This form is 04w's reference form $E_0$, with $\xi_0=1/(\sqrt{21}\delta)$. In a symplectic
$\mathbb Z$-basis of $\Omega_{\rm can}$,
$$
M=\begin{pmatrix}-2&17&101&32\\-1&4&29&5\\0&1&7&3\\0&-2&-19&-6\end{pmatrix},\qquad M^T\Omega M=5\Omega .
$$

**The cone and its points** (checked, Q1–Q6, R1–R8, U1–U2). The table gives the weights relative to $G_{\rm can}$, the vacuum of $\Omega_{\rm can}$ (the GKP vacuum of this lattice).

| form on $L$ | mode $\lambda_1=3.791$ | mode $\lambda_2=-0.791$ | status |
|---|---|---|---|
| vacuum $G_{\rm can}$ | 1 | 1 | positive; Williamson spectrum $(1,1)$ |
| Weil form $W_{\rm can}=\tfrac12\Omega_{\rm can}(M-V)$ | $-1.1860=-\mathrm{Im}\,\alpha_1$ | $+2.2008=\mathrm{Im}\,\alpha_2$ | **indefinite**, signature $(2,2)$; Krein signs $(-,+)$ |
| Rosati $\mathcal T_L$, $e=1$ | $10.870=\sqrt{21}\,d_1$ | $20.171=\sqrt{21}\,d_2$ | not proportional; ratio $R_0=1.8557$ (04w) |
| Rosati, $e=\varepsilon=(5+\sqrt{21})/2$ | $0.4735$ | $463.04$ | the same lattice, another point |
| vacuum of $\Omega_+$ ($=\sqrt{21}\,G_{\rm can}$) | $\sqrt{21}$ | $\sqrt{21}$ | its Weil form is exactly $\tfrac12\mathcal T_L$ |

Here $d_j=\sqrt{4q-\lambda_j^2}=2.3719,\ 4.4016$. The reciprocals $1/(\sqrt{21}d_j)=0.0919994,\ 0.0495772$ are 04w's weights $c^0_j$, so this page and the shard agree.
The transported Rosati form is integral, $\mathcal T_L=B^T\bigl(\mathrm{Tr}(x\bar y)\bigr)B$, the trace form of $O_K$ (R2–R3).

**Which type the arithmetic picks** (checked, H1–H2; the reading uses Deligne's and Howe's theorems as quoted in `howe-positivity.md`).

- Fix one complex embedding of the Galois closure (degree 8, group $D_4$). The eight primes above 5 give the sets $S_{\mathfrak P}$. Four of them are $\Phi_+$ or $\overline{\Phi_+}$. The other four are the type of
  $\Omega_{\rm can}$ or its conjugate, which is 04w's $\Phi_0=\{\alpha_{1,-},\alpha_{2,+}\}$.
- The principal forms on $O_K$ are exactly $\pm\varepsilon^k\Omega_{\rm can}$ (*proved here*). From $\xi O_K=\mathfrak d^{-1}O_K$ we get $\xi=u/\mathfrak d$ with $u$ a unit, and $\bar\xi=-\xi$ forces $u\in O_{K^+}^\times=\pm\varepsilon^{\mathbb Z}$
  (fundamental unit from memory; 04w states it). These forms all have the mixed type, and their Riemann forms are $G_{\rm can}$ with weights $\varepsilon_j^k$, again an orbit.
- So for a mixed choice of $\varepsilon$, $(O_K,\pi,\pm\Omega_{\rm can})$ is a principally polarised ordinary abelian surface in the isogeny class of $\mathrm{Jac}(C)$. Its arithmetic Riemann form is the GKP
  vacuum $G_{\rm can}$, and the Weil form of its polarisation is indefinite.
- For a $\Phi_+$ choice, $O_K$ carries no principal polarisation of the right type, so the Jacobian's module is one of the other three ideal classes.
- Which class, and which principal form is $\Theta$'s: *open*. This is the finite task of 04w's `obs:bond-h1-comparison-open`.

## 4. Example 2: $K_4$ with one negative edge ($q=2$, rank 8)

(Checked, G1–G10.) $M=\bigl(\begin{smallmatrix}0&-I\\2I&A_s\end{smallmatrix}\bigr)$ and $F+V=A_s\oplus A_s$, with $\lambda\in\{-\sqrt5,-1,1,\sqrt5\}$. The similitude forms make up a 4-dimensional space.
The standard $\Omega$ has all Krein signs $+$ (type $\Phi_+$), and its Weil form $\bigl(\begin{smallmatrix}qI&A_s/2\\A_s/2&I\end{smallmatrix}\bigr)$ is positive, equal to $\sum_j\tfrac12\sqrt{8-\lambda_j^2}\,G_J|_j$.
Howe's unit $P$ takes the values $p(\lambda)=(-\varphi^3,-1,1,\varphi^{-3})$ on the modes $\lambda=(-\sqrt5,-1,1,\sqrt5)$. The principal polarisation $\Omega_P=\Omega(\cdot,(P\oplus P)\cdot)$ then gives:

| form | $\lambda=-\sqrt5$ | $-1$ | $1$ | $\sqrt5$ |
|---|---|---|---|---|
| vacuum $G_J$ of $\Omega$ | 1 | 1 | 1 | 1 |
| Weil form of $\Omega$ | $\sqrt3/2$ | $\sqrt7/2$ | $\sqrt7/2$ | $\sqrt3/2$ |
| Riemann form $\Omega_P(\cdot,J_P\cdot)$, $J_P=\sigma J$, $\sigma=(-,-,+,+)$ | $\varphi^3$ | 1 | 1 | $\varphi^{-3}$ |
| Weil form of $\Omega_P$ | $-\varphi^3\sqrt3/2$ | $-\sqrt7/2$ | $\sqrt7/2$ | $\varphi^{-3}\sqrt3/2$ (signature $(4,4)$) |

- **Not the function of example 1** (*negative finding*, G8). In example 1 the principal form differs from the $\Phi_+$ form by $1/|h'(\lambda_j)|$. Here $|p(\lambda_j)|\,|h'(\lambda_j)|=(75.8,8,8,4.22)$, which is not constant.
  The only weight that is a universal function of $\lambda_j$ in both examples is the Weil-to-vacuum weight $\varepsilon_j\tfrac12\sqrt{4q-\lambda_j^2}$.
- **Why** (*proved here*, G9). $P=\tfrac12(1+2A_s-A_s^2)\notin\mathbb Z[A_s]$, so $\mathbb Z^8$ has endomorphisms outside $\mathbb Z[F,V]$ and is not a free $\mathbb Z[F,V]$-module. Theorem 5 has no integral cyclic vector to work with.
  With a rational cyclic $e$, the Rosati weights are $2/G_J(\pi_je)$, which depend on $e$ (G10).

## 5. Which point carries RH

1. **RH $\Leftrightarrow$ $\mathcal C(M)\ne\emptyset$** (*standard*, Proposition 1). The condition needs no symplectic form, no CM type and no integral structure.
2. **The Weil form is a point of the cone** (*proved here*, Proposition 3; checked Q4, G3, X1). $\tfrac12\Omega'(\cdot,(M-V)\cdot)$ is symmetric and $M$-invariant for every compatible $\Omega'$.
   It is positive if and only if RH holds and $\Phi_{\Omega'}=\Phi_+$. For the graph steps with the standard $\Omega$, and for $\Omega_+=\mathrm{Tr}(x\bar y/(V-F))$ on $\mathbb Z[F,V]$, the type is
   $\Phi_+$ by construction. There the Weil form, $\bigl(\begin{smallmatrix}qI&A/2\\A/2&I\end{smallmatrix}\bigr)$ or $\tfrac12\mathcal T$, can be written down before RH is known, and its positivity is RH.
   It is one point, polynomial in the step. The vacuum, by contrast, needs $\sqrt{4q-\lambda_j^2}$, so it exists only after RH.
3. **Precision on `lattice-tower.md` §5** (*negative finding*, X3). That page states (i)$\Leftrightarrow$(ii)$\Leftrightarrow$(iii). The step from (i) to (ii) fails for compatible forms of another type. For example, $M'=\bigl(\begin{smallmatrix}0&1\\-5&-2\end{smallmatrix}\bigr)$ satisfies
   RH, yet its Weil form is negative definite. The polarisations of §§3–4 are further cases. The statement is correct for the graph steps it was written for. The general form is "(i) $\Leftrightarrow$ (iii) $\Leftrightarrow$ the
   Weil form of some compatible form is positive". Not edited here.
4. **The polarisation is a further point and does not carry RH** (*checked* on both examples). The principal polarisation picks the point $\Omega_{\rm pol}(\cdot,J_\varepsilon\cdot)$ (on a fixed lattice,
   up to units). It decides integrality: $\det\Omega_{\rm pol}=1$, a qunaught. Its own Weil form is indefinite whenever $\Phi_\varepsilon\ne\Phi_+$: for $K_4$ always, and for the curve at half
   the primes above 5.

**What this means for "what data for $\zeta$"** (*heuristic*, all six sentences).
(i) What carries RH is that the cone is non-empty. The witness that exists before RH is known is one point, the Weil form, which on the algebra with its unit as cyclic vector is $\tfrac12\mathcal T$.
(ii) Weil's quadratic form for $\zeta$ is the analogue of this point; analytic §14 already matches it with $\mathcal T$. Here it needs no polarisation, because the test-function algebra acts on itself and the unit is a canonical cyclic vector.
(iii) The notebook's Deninger metric cone (04u: dimension $\sum_am_a^2=16539$ for the LPS complex, Hermitian blocks because of multiplicities) is the analogue of $\mathcal C(M)$.
(iv) A point of that cone other than the Weil form needs extra data: a marking modulo units, or a polarisation.
(v) In the curve case the arithmetic supplies the polarisation ($\Theta$). It decides integrality and not RH.
(vi) For $\zeta$ nothing in the notebook supplies a polarisation (`adelic-gkp.md` §12.2), and on the evidence of the curve examples RH should not need one.

## 6. Status and checks

| statement | status | checks |
|---|---|---|
| L-polynomial, counts, ordinariness, $\mathrm{disc}\,O_K$, $h_K=4$ | checked (PARI, brute force) | C1–C4 |
| graph convention impossible for this class; $\mathbb Z[F]$ not $V$-stable | negative finding; checked | C5, K2 |
| $(O_K,\pi,\Omega_{\rm can})$ in a symplectic $\mathbb Z$-basis | checked exactly | K1, K3, K5 |
| cone = positive orthant of mode weights; RH $\Leftrightarrow$ non-empty (Prop. 1) | standard; checked | Q1, G2, X2 |
| Weil form $=\sum\varepsilon_j\,\mathrm{Im}\,\alpha_j\,G|_j$; Williamson frequencies $\mathrm{Im}\,\alpha_j$ (Prop. 2) | proved here; checked | Q3–Q6, G3 |
| $\Omega'\mapsto W_{\Omega'}$ is an isomorphism onto the similitude forms (Prop. 3) | proved here; checked | X1 |
| Rosati transport is $e$-dependent; it sweeps the cone; unit orbits (Prop. 4) | proved here; checked | U1–U2, G10 |
| genus-$g$ bridge: $W_{\Omega_+}=\tfrac12\mathcal T_L$; weights $\sqrt{4q-\lambda_j^2}$, resp. $|h'(\lambda_j)|\sqrt{4q-\lambda_j^2}$ (Thm. 5) | proved here (Euler's lemma from memory); checked exactly in genus 2, and in genus 1 against lane A | K3–K4, R1–R9 |
| $\mathcal T_L$ not proportional to the vacuum; agreement with 04w's $c^0_j$, $R_0$, $\varepsilon_1^4$ | checked | R4–R5, U2 |
| 5-adic types: 4 primes $\Phi_+$, 4 mixed; principal forms on $O_K$ are $\pm\varepsilon^k\Omega_{\rm can}$ | checked (PARI); proved here (unit argument) | H1–H2 |
| which ideal class and which principal form is $\mathrm{Jac}(C)$'s | open | none |
| $K_4$: Howe's Riemann form has weights $(\varphi^3,1,1,\varphi^{-3})$; its Weil form has signature $(4,4)$; not the example-1 function; $\mathbb Z^8$ not free | checked; negative finding; proved here | G1–G10 |
| precision on `lattice-tower.md` §5, (i)$\Rightarrow$(ii) | negative finding; checked | X3 |
| the reading for $\zeta$ (§5, six sentences) | heuristic | none |

`checks/check_cone_bridge.py`: **42 of 42 pass**, in about 3 s. Arithmetic is exact (sympy, $\mathbb Q(\sqrt{21})$, $\mathbb Q(\sqrt5)$) except for the vacua, which use mpmath at 40 digits,
and the Williamson spectra and signatures, which use float64.

## 7. Next

- **The Jacobian's own point.** For each kind of 5-adic choice, find which of the four ideal classes of $O_K$ is $H_1$ of the canonical lift of $\mathrm{Jac}(C)$, and which
  principal form is $\Theta$'s. One route is the group structures $J(\mathbb F_{5^k})\cong T/(1-F^k)T$, as lane A did for E2. This settles where in the cone the arithmetic point of the actual
  curve sits.
- **The $K_6$ flux** (`howe-positivity.md` §2). There the standard $\Omega$ is principal and of type $\Phi_+$ for some choice, so the Weil form, the vacuum and the arithmetic Riemann form are all
  given by the universal weights of Proposition 2. It is the several-mode case in which nothing is twisted, and a control for this page.
- **Genus $\ge3$.** Theorem 5 predicts that the vacua of $\Omega_+$ and $\Omega_{\rm can}$ stop being proportional. Check it on one genus-three curve.
