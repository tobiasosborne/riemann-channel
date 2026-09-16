# Selberg letters: prover report on D1–D8

## Main conclusions

- **Selberg has a concrete graded spectral transfer:** even $A=-X$, odd $A+1$, with ring zeta $D_{\rm tow}(s-1)/D_{\rm tow}(s)=Z_S(s)$. Full transverse forms instead give Ruelle and two different retained bands.
- **The positive first-band form is derived using Haar, the Lie algebra, and DFG analysis.** It requires orthogonal, branchwise pullbacks; the draft's total pullback is degenerate. The operator FE is $JXJ^{-1}=1-X$.
- **Divisor Ramanujan iff $1/4$ coercivity; full operator HP additionally excludes the threshold.** At a Laplace eigenvalue $1/4$, algebraic resonance multiplicity is twice geometric multiplicity, obstructing positive unitarization.
- **D7's finite mechanism is proved constructively**, including a strict-band metric and operator FE. Exact graph and quantum endpoint counterexamples explain the same qualification. All 131 checks pass.
- **D5 supplies no doubled-bond CP realization.** Its single-copy negative flat supertraces cannot be honest squared ring norms.
- **D6 remains open at the noncompact operator bridge.** The $\rho/2$ divisor is verified, but Eisenstein Laurent coefficients are not $L^2$ and truncated positivity does not imply RH. The draft's rate and its “open for the full modular group” claim are corrected.
- **K-type parity is not Hodge degree:** it makes $X$ odd, and its diffusion supertrace need not cancel. The transverse two-term complex is the Selberg construction established here.

This report changes no notebook shard. “PROVED” below means proved under the enumerated standard analytic inputs, not independently reviewed. Every use of a deep analytic result is separated from the algebra proved here.

## Conventions and hypothesis register

Use $M=\Gamma\backslash\mathbb H$, $SM=\Gamma\backslash G$, $G=\mathrm{PSL}_2(\mathbb R)$, and the matrices and left-invariant differential fields in the brief. Write
\[
 A=-X,\qquad \Omega=X^2+\tfrac12(U_+U_-+U_-U_+),\qquad
 \Delta=-\Omega\quad\hbox{on right-}K\hbox{-invariants}.
\]
Thus a DFG resonance $\lambda$ is an eigenvalue of **$A=-X$**, not of $X$; $e^{-tX}u=e^{t\lambda}u$. The Laplace variable $\varsigma$ for the function flat trace equals this $\lambda$. For the Selberg first band set $s=1+\lambda$. Use $\sigma$ for a Laplace eigenvalue, $s_\pm(\sigma)=1/2\pm\sqrt{1/4-\sigma}$, and $\lambda_\pm=s_\pm-1$. Both roots occur with multiplicity $d_\sigma=\dim\ker(\Delta-\sigma)$; a repeated root counts twice in a divisor.

Normalize the fibre Haar measure to mass one and choose the quotient measure consistently, so $\pi^*:L^2(M)\to L^2(SM)$ is isometric. DFG's unnormalized $dS$ only rescales $\pi_*$ by a fixed positive constant. Primitive orbits are oriented as in the notebook, consistently in every product. Put $c=2g-2=-\chi(M)>0$. Write $\operatorname{ord}F$ for zeros minus poles, but **$\nu=-\operatorname{ord}Z_{\rm ring}$** for the notebook's even-minus-odd divisor. These signs must not be conflated.

The following are labelled inputs, not conclusions silently attributed to the letters. Source names below are paths relative to the repository root; line numbers refer to the files read in this run.

| Hypothesis | Content and provenance |
|---|---|
| **H-GEO** | $\Gamma$ is discrete, torsion-free, cocompact; the quotient is connected. This is the specified compact-surface setting, not an assertion about the modular orbifold. `report/sections/02b_definitions_arithmetic.tex:173–182`; DFG `refs/src/1403.0256/RuelleResonForHn.tex:521–539`. |
| **H-HAAR** | The right flows preserve the descended Haar measure. Unimodularity follows from the displayed Lie brackets, as proved in D1; the quotient measure is stipulated. Previous proof: `notes/selberg/astra-proofs.md:199–207`. |
| **H-SL2** | The differential representation respects the specified matrix brackets. Directly verified in D1 and the finite script; conventions agree with DFG `RuelleResonForHn.tex:531–544`. |
| **H-AN** | Complete smooth volume-preserving flows have skew-adjoint generators with smooth core; the compact positive Laplacian has its self-adjoint elliptic realization. Standard operator/elliptic theory, *not proved from formal skew-symmetry*. The earlier report explicitly isolates it at `notes/selberg/astra-proofs.md:148`. DFG recalls the $X$ realization at `RuelleResonForHn.tex:2162–2168`; Marklof recalls the Laplace spectral theorem at `refs/src/math/0407288/selberg07.tex:1657–1682` (his Laplacian has the opposite sign). The general smooth-core theorem is not proved in these supplied sources. |
| **H-LAP** | Smooth finite-dimensional Laplace eigenspaces, complete orthonormal eigenbasis, $0$ simple and spectrum tending to infinity. Standard compact elliptic spectral theory, recalled in Marklof `selberg07.tex:1657–1682`; nonnegativity is proved here from the letters. |
| **H-SZ** | Selberg product, entire continuation and full compact divisor. Proved via the trace formula in Marklof `selberg07.tex:2243–2249,2279–2351`; threshold double multiplicity is at `2286–2298`. Trace formula: `1763–1772`. |
| **H-DZ-FLAT** | Flat trace on transverse forms, with the backward Poincaré map. Standard Guillemin formula with a proof in DZ: `refs/src/1306.4203/zeta.tex:489–509`; orientation sign and Lefschetz identity: `510–526`. This is not an $L^2$ trace. |
| **H-DZ-MULT** | The logarithmic derivative of each flat dynamical determinant has residue equal to the rank of the anisotropic Riesz projection. Proved in DZ `zeta.tex:1522–1539,1567–1620`, especially `1585–1619`. Thus it measures *algebraic* multiplicity. |
| **H-DFG-REG** | Use the closed $X$ realizations on the anisotropic spaces $\mathcal H^r$, with smooth tests and distributional outputs, compatible in overlapping half-planes. Standard resonance construction recalled as a theorem in DFG `RuelleResonForHn.tex:2075–2113`; no right-half-plane resonances: `2162–2168`. |
| **H-DFG-POIS** | $\pi_*:\operatorname{Res}^0_X(\lambda)\simeq\ker(\Delta+\lambda(1+\lambda))$ for the scalar Poisson nonexceptional parameters. DFG gives the pushforward at `599–607`, boundary representation at **`612–624`**, Poisson integral at **`626–636`**, and scalar exception discussion at `2456–2461`. We use it on $\lambda\notin-1-\mathbb N_0$, a safe explicit exclusion; in particular throughout $-1<\Re\lambda<0$, including $-1/2$, and at $0$. This is substantial cited analysis, not a consequence of centrality alone. |
| **H-DFG-LAD** | Eigenspace decomposition outside $-1-\tfrac12\mathbb N_0$. DFG `RuelleResonForHn.tex:546–591`; the ladder algebra is rederived in D4. |
| **H-DFG-SS** | Algebraic equals geometric multiplicity outside $-\tfrac12-\tfrac12\mathbb N_0$ in dimension two. DFG Theorem `t:noalg`, `RuelleResonForHn.tex:357–375`. **Its exceptional set is larger than the ladder theorem's.** |
| **H-COERC** | $\|Hf\|^2+\|Ef\|^2\geq\|f\|^2$ for smooth $K$-invariant $f\perp1$. An *additional surface-dependent property*, equivalent to $\Delta\vert_{1^\perp}\geq1/4$, proved equivalent in D3. No source here proves it for arbitrary compact surfaces. |
| **H-NOEDGE** | $1/4\notin\operatorname{spec}\Delta$. An optional extra hypothesis for identifying the full algebraic first band with its eigenstates; not needed for divisor RH/FE/Ram. No general surface theorem is assumed. |
| **H-GRAPH** | Finite connected simple undirected $D=q+1\geq3$ regular graph, counting inner products and the edge convention in D7. Specified finite data; all algebra is proved here. |
| **H-UNIT** | Finite Hilbert bond, orthogonal parity $P$, $D\geq4$ labelled homogeneous unitary letters with fixed-point-free reversal and $U_{\bar i}=U_i^*$. Specified finite data (`02h_definitions_graded_ramanujan.tex:114–123`); inverse pairing, not CP alone, supplies the quadratic. |
| **H-BAND** | On explicitly retained vertex/channel spaces, $\operatorname{spec}\Sigma\subseteq[-2\sqrt q,2\sqrt q]$. Extra Ramanujan bound; strict version excludes the endpoints. It is checked in the examples, never deduced merely from Hermiticity. Harrow's sufficient representation transfer is proved in `refs/src/0709.1142/main.tex:230–304`; Hastings' benchmark is in `refs/src/0706.0556/sd10.tex:284–287`. |

Additional inputs specific to D6 and D8 are stated in their own hypothesis blocks. References to notebook definitions fix vocabulary rather than supplying a new analytic theorem.

## D1 — Letters, the positive Laplacian, and the direction of the spectral map

### Statement (as proved)

The stated fields have skew-adjoint closures under H-AN; $\Omega$ is central and preserves $K$-invariants. On those invariants,
\[
 \langle f,\Delta f\rangle=\tfrac14(\|Hf\|^2+\|Ef\|^2),\qquad
 \operatorname{spec}\Delta\subset[0,\infty).
\]
It is the **inverse image** of $[0,\infty)$ under $s\mapsto s(1-s)$ that is

\[
 [0,1]\ \cup\ (\tfrac12+i\mathbb R).
\]

### Hypotheses H-*

H-GEO, H-HAAR, H-SL2, H-AN, H-LAP, as registered above.

### Proof

1. **Haar adjoints.** The matrix brackets are $[H,E]=2W$, $[H,W]=2E$, $[E,W]=-2H$. Each adjoint matrix has trace zero; connectedness implies unimodularity. Right translation and its quotient preserve Haar. Integrating $B(\bar f h)$ gives $\langle Bf,h\rangle=-\langle f,Bh\rangle$. Completeness and H-AN identify the closures with the unitary-group generators.
2. **Casimir.** For example, $[H,E^2]=2(WE+EW)=[H,W^2]$; the corresponding $E,W$ identities give $[B,\Omega]=0$ for each basis field. In particular $\Omega$ commutes with right $K$.
3. **Laplacian normalization.** At $g_{x,y}\cdot i=x+iy$, differentiating the actual curves $g_{x,y}e^{uH}\cdot i=x+iye^{2u}$ and $g_{x,y}e^{uE}\cdot i=x+y\tanh(2u)+iy\operatorname{sech}(2u)$ gives $H^2f=4y^2F_{yy}+4yF_y$, $E^2f=4y^2F_{xx}-4yF_y$. With $Wf=0$, $\Omega f=y^2(F_{xx}+F_{yy})=-\Delta F$. Centrality extends the section computation to all frames.
4. **Positivity and roots.** Integration by parts gives the asserted quadratic form. H-AN/H-LAP give the nonnegative self-adjoint operator. If $s=a+ib$, reality of $s(1-s)$ says $b(1-2a)=0$. On the real branch nonnegativity is $0\leq a\leq1$; on the other branch $a=1/2$. This proves the stated preimage, including multiplicities through H-LAP.

**Status: CORRECTED (L01).**

## D2 — Exact ring zetas, signs, and trivial divisors

### Statement (as proved)

Define distributions on $t>0$
\[
 C(t)=\sum_{\gamma\ {\rm primitive}}\sum_{k\geq1}\ell_\gamma\,
       \delta(t-k\ell_\gamma),\qquad
 F(t)=\frac{C(t)}{4\sinh^2(t/2)}.
\]
The division is multiplication by a smooth function on $(0,\infty)$. Flat ring zetas are normalized by their convergent orbital exponential, tending to $1$ as the real Laplace parameter tends to $+\infty$. The absence of arbitrarily short closed orbits makes these integrals unambiguous at $t=0$. This fixes any zero-free factor; no unspecified regularized determinant is substituted for this normalization.

| Transfer (single-copy spectral category) | Flat supertrace | Ring zeta $\exp\int_0^\infty e^{-st}\operatorname{str}(t)dt/t$ |
|---|---|---|
| Function flow $A=-X$, even | $F(t)$ | $D_{\rm tow}(s)^{-1}$ |
| Same flow, parity reversed (all odd) | $-F(t)$ | $D_{\rm tow}(s)$ |
| Full transverse forms, usual degree parity | $(2-e^t-e^{-t})F(t)=-C(t)$ | $\zeta_R(s)=Z_S(s)/Z_S(s+1)$ |
| **Two-term stable transverse complex:** even $A$, odd $A+1$ | $(1-e^t)F(t)=-C(t)/(1-e^{-t})$ | **$Z_S(s)=D_{\rm tow}(s-1)/D_{\rm tow}(s)$** |

The last line is the Selberg ring zeta used in the rest of this report. “Stable” here labels the covector dual to $U_+$: $\eta_+(U_+)=1$, $\eta_+(X)=\eta_+(U_-)=0$, so $\mathcal L_X\eta_+=-\eta_+$. It is an actual globally trivialized transverse line on this constant-curvature quotient. The even and odd spaces are $\mathcal D'(SM)$ and $\mathcal D'(SM)\eta_+$, realized by the compatible anisotropic spaces of D5. This is not yet a CP norm transfer.

For exact bookkeeping, let
\[
 \mathcal S=\sum_{\sigma>0}d_\sigma(\delta_{s_+(\sigma)}+\delta_{s_-(\sigma)}),\qquad
 \mathcal Q=\delta_1+\delta_0+c\sum_{n\geq0}(2n+1)\delta_{-n}.
\]
Thus $\operatorname{ord}Z_S=\mathcal S+\mathcal Q$; $\operatorname{ord}_0 Z_S=c+1=2g-1$, and $\operatorname{ord}_{1/2}Z_S=2d_{1/4}$. A root collision is counted, not removed.

For $Z_S$, designate
\[
 \nu_{\rm triv}^{S}=-\delta_1-\delta_0-c\sum_{n\geq0}(2n+1)\delta_{-n},\qquad
 \nu_{\rm ret}^{S}=-\mathcal S.
\]
All these net divisor points are odd. The constant roots $1,0$ are both **zeros**, not a Perron pole and its pole partner. The reference pair $(1,0)$ and its shifted version $(0,-1)$ are supplied geometric rates in the *spectral* category; they are not claimed to satisfy the CP definition's even Perron requirement.

For $\zeta_R$, writing $\tau_{-1}\delta_z=\delta_{z-1}$,
\[
 \nu_{\rm ret}^{R}=-\mathcal S+\tau_{-1}\mathcal S,
\qquad
 \nu_{\rm triv}^{R}=-\delta_1+\delta_{-1}-c\delta_0-2c\sum_{n\geq1}\delta_{-n}.
\]
The integer **net zero orders** are therefore

| Point | $1$ | $0$ | $-1$ | $-n, n\geq2$ |
|---|---:|---:|---:|---:|
| $\operatorname{ord}\zeta_R$ | $1$ | $c$ | $2c-1$ | $2c$ |

There is **no net pole at $0$**. Before cancellation, the constant pair contributes $\delta_1-\delta_{-1}$ to zero-minus-pole order, while the topological quotient contributes $c\delta_0+2c\sum_{n\geq1}\delta_{-n}$. This records the hidden even contribution at $-1$ without declaring the final zero to be a pole.

For $D_{\rm tow}$, the nonconstant zero divisor is
\[
 \sum_{\sigma>0}\sum_{k\geq0}d_\sigma
 (\delta_{-1/2-k+ir_\sigma}+\delta_{-1/2-k-ir_\sigma}).
\]
It has one zero at $0$ and zeros at $-N$, $N\geq1$, of order $cN^2+2$. For the all-odd convention, $\nu$ is the negative of these zero orders. For the even function-flow convention, it is positive. The $k\geq1$ nonconstant descendants are *spectral* ladders depending on the surface, not the universal topological ladder.

The precise retained-divisor verdicts are:

| Object and reference midpoint | (RH): all retained real parts at most midpoint | (FE): reflection preserving signed multiplicity | (Ram): all retained real parts equal midpoint |
|---|---|---|---|
| $Z_S$, midpoint $1/2$ | iff H-COERC | always, $s\mapsto1-s$ | iff H-COERC |
| $\zeta_R$, both nonconstant bands retained, midpoint $1/2$ | iff H-COERC | **fails** | **fails**, even under H-COERC |
| All-odd $D_{\rm tow}$, all nonconstant bands retained, midpoint $-1/2$ | iff H-COERC | **fails** | **fails**, even under H-COERC |
| $D_{\rm tow}$ restricted to its nonconstant first-band divisor, midpoint $-1/2$ | iff H-COERC | always | iff H-COERC |

One may explicitly remove the entire even shifted spectral band of $\zeta_R$ as additional supplied structural data. Then its remaining odd divisor has the $Z_S$ verdict. This is a *change of retained data*, not a consequence of calling a Jacobian shift a “period image.” The natural two-term complex above gives $Z_S$ directly and avoids this discretionary removal.

The full retained Ruelle divisor instead has $\nu^R_{\rm ret}(-s)=-\nu^R_{\rm ret}(s)$: its reflection about zero exchanges the two parities. This inverse-zeta symmetry is not the notebook's parity-preserving (FE).

### Hypotheses H-*

H-GEO, H-DZ-FLAT, H-SZ. H-DFG-REG and H-DZ-MULT identify these divisors with relative resonance multiplicities. H-COERC is used only in the equivalences explicitly bearing its name. H-LAP supplies the spectral indexing.

### Proof

1. **Jacobian and parity.** The transverse backward return multipliers are $e^t,e^{-t}$. Thus $\det(1-P)=2-e^t-e^{-t}<0$ and $|\det(1-P)|=4\sinh^2(t/2)$. H-DZ-FLAT and the elementary exterior identity give $N_0=N_2=F$, $N_1=(e^t+e^{-t})F$. Consequently the full supertrace is $-C$. “Fermionic closed geodesics” means precisely this orientation sign; it does not assert a CP realization or a physical state norm.
2. **Integrate the comb.** At a repeated period $t=k\ell$, the factor $\ell/t$ is $1/k$. Hence $\int e^{-st}(-C)dt/t=-\sum_{\gamma,k}e^{-sk\ell_\gamma}/k=\log\zeta_R(s)$ for $\Re s>1$. No extra $t$ or orientation factor appears.
3. **Function determinant and Selberg reduction.** Since $F=C\sum_{j\geq1}j e^{-jt}$, the same calculation gives $\exp(-\int e^{-st}Fdt/t)=\prod_{j\geq1}Z_S(s+j)=D_{\rm tow}(s)$, initially $\Re s>0$. Multiplication by $1-e^t$ cancels one transverse denominator and gives $\log Z_S(s)$. Equivalently the ratio of the two dynamical determinants is $D_{\rm tow}(s-1)/D_{\rm tow}(s)$. Full transverse forms give $D(s-1)D(s+1)/D(s)^2=Z_S(s)/Z_S(s+1)$. The products converge normally after finitely many factors are separated, so H-SZ gives their stated continuations.
4. **It is a complex built from a letter.** $d f=(U_+f)\eta_+$ intertwines the even generator $A$ and odd generator $A+1$, since $[A,U_+]=-U_+$. There is no degree-two term. On nonexceptional ladder modules, $d$ pairs even level $m$ with odd level $m+1$; the odd level zero survives. This is the first-band mechanism behind the determinant quotient. We assert this algebra on resonant modules, not an unproved closed-range theorem for a global leafwise cohomology.
5. **Divisors.** H-SZ gives $\mathcal S+\mathcal Q$. Subtracting its unit shift proves the Ruelle formulas and the displayed integer table. Summing the shifts for the tower gives $c\sum_{n=0}^{N-1}(2n+1)+2=cN^2+2$, with the two constants coming from $Z_S(1)$ and the extra order at $Z_S(0)$; at zero only $Z_S(1)$ contributes. These multiplicities are also checked symbolically in the script.
6. **RH/FE/Ram.** Each nonconstant spectral pair has sum $1$. D1 puts it on the line or on the real interval. The rightmost member is at most $1/2$ iff $\sigma\geq1/4$. Reflection interchanges equal odd multiplicities. The Ruelle even spectral band is one unit left, so reflection about $1/2$ sends it to a nonexistent even band to the right; it is never on the same critical line. The same obstruction applies to tower descendants. These are signed-divisor statements, not assertions about uncancelled operator subspaces or Jordan data.

**Status: CORRECTED (L02–L09).**

## D3 — The first band: Casimir, positive form, FE, and the threshold

### Statement (as proved)

For $u\in\operatorname{Res}^0_X(\lambda)=\{(X+\lambda)u=0, U_-u=0\}\subset\mathcal D'(SM)$,
\[
 \Omega u=\lambda(1+\lambda)u,\qquad
 \Delta\pi_*u=-\lambda(1+\lambda)\pi_*u.
\]
The wavefront requirement follows already from the two equations (or H-DFG-POIS); its omission does not mean an arbitrary distributional flow eigenstate is resonant. Under H-DFG-POIS the nonzero first-band states with $-1<\Re\lambda<0$ have nonzero smooth pushforward, and
\[
 \lambda\in[-1,0]\cup(-\tfrac12+i\mathbb R).
\]
The first-band nonconstant divisor lies on $-1/2+i\mathbb R$ iff H-COERC holds.

Let $\mathcal F_{\rm eig}=\bigoplus_{\lambda\ {\rm nonconstant}}\operatorname{Res}^0_X(\lambda)$ be the algebraic direct sum of **distinct eigenvalue spaces**, and define
\[
 G_\oplus(u,v)=\sum_\lambda
 \langle\pi_*u_\lambda,\pi_*v_\lambda\rangle_{L^2(M)}.
 \tag{D3-G}
\]
Then $G_\oplus$ is positive definite; $A=-X$ is normal in its modal completion. The rescaled flow $e^{t/2}e^{-tX}$ is $G_\oplus$-unitary iff H-COERC holds. At $\lambda=-1/2$, this eigenstate space has only $d_{1/4}$ dimensions, whereas the zeta divisor requires $2d_{1/4}$.

Under **H-NOEDGE**, this construction covers the full algebraic nonconstant first band. It gives the manifest form for the retained odd block of the Selberg two-term transfer, shifted by $+1$. Its domain and completion are the transported modal ones specified below, not the original Haar $L^2(SM)$ and not an asserted equivalent norm on a DFG anisotropic space.

On each paired pair of nonthreshold branches define $J$ by retaining the pushforward and swapping branches:
\[
 J|_{\mathcal F_\lambda}=(\pi_*|_{\mathcal F_{-1-\lambda}})^{-1}\pi_*|_{\mathcal F_\lambda}.
\]
Then
\[
 J^2=1,\quad G_\oplus(Ju,Jv)=G_\oplus(u,v),\quad
 JAJ^{-1}=-1-A,\quad JXJ^{-1}=1-X.
 \tag{D3-FE}
\]
On the shifted odd Selberg generator $S=A+1$, $JSJ^{-1}=1-S$. The map is even because it acts within the retained odd sector. For the eigenstate space at $-1/2$ one may take $J=1$; this does not extend the positive unitary-flow claim to its generalized eigenspace.

### Hypotheses H-*

H-GEO, H-HAAR, H-SL2, H-AN, H-LAP, H-DFG-REG, H-DFG-POIS; H-COERC precisely for the line/unitarity conclusion. H-DFG-SS and H-NOEDGE identify the eigenspace construction with the entire algebraic band. H-SZ and H-DZ-MULT are used to audit the threshold multiplicity.

### Proof

1. **Casimir algebra, including the sign.** From $[U_+,U_-]=2X$,
   \[
   U_-U_+=U_+U_--2X,\qquad
   \Omega=X^2+U_+U_--X.
   \]
   On $U_-u=0$ this is $X^2-X$. Substituting $Xu=-\lambda u$ gives $\lambda^2+\lambda$. The draft's intermediate $+X$ in this ordering is wrong. Alternatively $\Omega=X^2+U_-U_++X$, with the *other* ordering.
2. **Pushforward intertwining.** Let $\Pi_K=\pi^*\pi_*$ be fibre averaging. Centrality implies $\Pi_K\Omega=\Omega\Pi_K$, first on smooth functions and then by duality on distributions. D1 therefore gives $\pi_*\Omega=-\Delta\pi_*$. Elliptic regularity makes a distributional Laplace eigenfunction smooth. This proves where the pushforward lands; it does **not** prove that it is nonzero or onto.
3. **The analytic bridge.** H-DFG-POIS proves exactly that missing injectivity and surjectivity. In DFG's formulas a boundary distribution $w$ represents $u=P(y,B_-)^\lambda w(B_-)$, and fibre integration becomes $\int P(y,\nu)^{1+\lambda}w(\nu)dS(\nu)$. The latter Poisson transform is the cited analytic isomorphism. Its equivariance, distributional boundary regularity and invertibility are not consequences of finite Lie algebra manipulations. The wavefront condition can also be seen locally from elliptic regularity for the equations $X+\lambda$ and $U_-$: their characteristic intersection is the annihilator of $X,U_-$, namely DFG's $E_u^*$.
4. **Reality.** For nonzero $u$, put $f=\pi_*u\ne0$. Then
   \[
   -\lambda(1+\lambda)=\frac{\langle f,\Delta f\rangle}{\|f\|^2}
   =\frac{\|H\pi^*f\|^2+\|E\pi^*f\|^2}{4\|f\|^2}\geq0.
   \]
   Writing $\lambda=a+ib$ yields $b(2a+1)=0$. If $b=0$, nonnegativity is $-1\leq a\leq0$; otherwise $a=-1/2$. The claimed reality is derived from Haar plus the analytic bridge, not from CP and not from the original $L^2$ spectrum of the flow.
5. **Coercivity equivalence.** The Rayleigh inequality in H-COERC is exactly $\langle f,\Delta f\rangle\geq\|f\|^2/4$ on $1^\perp$. H-LAP makes it equivalent to $\sigma\geq1/4$ for all nonconstant eigenvalues. The quadratic then puts both roots on the line, and a $0<\sigma<1/4$ produces two real off-line roots. This is the sole new spectral bound needed for *divisor* Ramanujan. It is additional geometry/arithmetic, not a formal property of the letters.
6. **Why the draft's form fails.** For $\sigma\ne1/4$, choose $0\ne f\in E_\sigma$ and its two inverse images $u_+,u_-$. They are linearly independent (distinct flow eigenvalues), but $\pi_*(u_+-u_-)=0$. Thus $\langle\pi_*u,\pi_*v\rangle$, with a single total pushforward, is degenerate on the sum. Its Gram matrix on this pair is $\|f\|^2\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)$. Declaring branches orthogonal as in (D3-G) repairs the failure. This is an explicit modal choice, natural once the two branches are labelled; it is not forced by an untagged averaging map.
7. **Positive form, domains, and FE.** Each branch is isomorphic to its Laplace eigenspace, so (D3-G) is positive. Complete to $\bigoplus_\lambda^{\ell^2}E_{-\lambda(1+\lambda)}$, with
   \[
   D(A)=\{(f_\lambda):\sum_\lambda |\lambda|^2\|f_\lambda\|^2<\infty\}.
   \]
   Here $A(f_\lambda)=(\lambda f_\lambda)$ is closed and normal. The adjoint identity $A^{*G}+A=-1$ holds exactly when every retained real part is $-1/2$. In that case $A=-1/2+iH_G$ with a self-adjoint diagonal $H_G$; exponentiation gives the claimed unitary group. Branch exchange preserves the norm and domain, squares to one, and changes $\lambda$ into $-1-\lambda$. This proves (D3-FE), and also explains the sign change when switching from $A$ back to $X$. Equal branch weights are part of this $J$-unitary choice.
8. **The threshold is a real obstruction, not an omitted technicality.** At $\lambda=-1/2$, DFG's first-band isomorphism gives geometric multiplicity $d=d_{1/4}$. No higher band contributes there: its shifted first-band argument would have positive real part. H-SZ says $\operatorname{ord}_{-1/2}D_{\rm tow}=2d$, and H-DZ-MULT identifies this with the algebraic resonance multiplicity. Thus if $d>0$ the flow block is not semisimple. A finite-dimensional generator satisfying $A^*G+GA=-G$ with $G>0$ is similar to a skew-Hermitian operator minus $1/2$, hence semisimple. Such $G$ is impossible on this full block. Replacing it by two diagonal copies of $E_{1/4}$ preserves the divisor and allows a positive form, but changes the operator to a semisimplification. We make no such replacement silently.
9. **Other exceptional parameters and the constant.** The ladder excludes $-1,-3/2,-2,\ldots$; scalar Poisson invertibility excludes negative integers (our safe set is $-1-\mathbb N_0$); semisimplicity additionally excludes $-1/2$. None of the negative parameters at or below $-1$ belongs to the nonconstant first band in the open strip. At $\lambda=0$, $u=1$ is the constant first-band state and $\pi_*1=1$. At $\lambda=-1$, if $u$ is first-band then $\pi_*u$ is constant by Step 2, but $\langle u,1\rangle=0$ from $Xu=u$; hence $\pi_*u=0$. There is no inverse-pushforward partner for the constant at $-1$. Its topological resonance data must be treated by the divisor, not by the displayed $J$. At other excluded negative half-integers no extension of the cited ladder/semisimplicity theorem is claimed.

Consequently the draft's “everything else is derived from the letters” must include the labelled analytic inputs and the branch orthogonalization, and must distinguish eigenstates from algebraic resonance spaces. The theorem with exactly those inputs is restated after the ledger.

**Status: CORRECTED (L10–L16).**


## D4 — What the operator-level continuous Ihara statement actually says

### Statement (as proved)

The first-band polynomial intertwining is
\[
 \pi_*(A^2+A)=-\Delta\pi_*\quad\text{on }\ker U_-,\qquad A=-X.
 \tag{D4-I}
\]
On the nonexceptional resonance eigenspaces,
\[
 \operatorname{Res}_X(\lambda)=\bigoplus_{m\geq0}U_+^m
       \operatorname{Res}^0_X(\lambda+m),\qquad
 U_-^mU_+^m=m!\prod_{j=1}^m(2\lambda+m+j).
 \tag{D4-L}
\]
The sum is finite for each fixed $\lambda$. Its stated range is $\lambda\notin-1-\tfrac12\mathbb N_0$; it is an eigenspace statement, with generalized multiplicities handled separately.

The two-jump multiplication-observable generator is
\[
 L_{\rm adj}=\tfrac12(H^2+E^2)=2\Omega+\tfrac12W^2,
 \qquad L_{\rm adj}|_K=-2\Delta.
\]
Thus the comparison with Ihara–Bass is a **quadratic intertwining on first-band resonant data plus an explicit ladder**, not a compression of the whole flow by an orthogonal projection onto $K$-invariants. The corresponding notebook open item is proved for this first-band polynomial relation; a literal full-tower compression to a single Laplacian determinant is still not supplied.

If one samples time $\tau>0$, the two first-band eigenvalues become
\[
 \mu_\pm=e^{\tau\lambda_\pm},\qquad q_\tau=e^{-\tau},\qquad
 \mu_+\mu_-=q_\tau,\qquad
 a_\tau(\sigma)=2e^{-\tau/2}\cos\bigl(\tau\sqrt{\sigma-1/4}\bigr).
\]
They obey $\mu^2-a_\tau(\sigma)\mu+q_\tau=0$. This adjacency is a functional calculus of $\Delta$, **not** $-2\Delta$, and time sampling loses spectral information through aliasing.

### Hypotheses H-*

H-GEO, H-SL2, H-DFG-REG, H-DFG-LAD for the ladder; H-DFG-POIS for its Laplace identification. H-AN for closed heat realizations. The sum-of-squares identity itself is algebra on a common smooth domain, proved in `notes/selberg/astra-proofs.md:105–209` and `report/sections/09b_selberg_dictionary.tex:190–229`.

### Proof

1. **Intertwining.** On $\ker U_-$, D3's computation is the operator identity $\Omega=A^2+A$. Fibre averaging gives (D4-I). It is quadratic because the single eigenvalue $\sigma$ has two flow roots; one cannot intertwine $A$ itself with the single operator $\Delta$ on one copy of $E_\sigma$.
2. **Ladder coefficient.** If $U_-v=0$ and $Xv=-zv$, then the commutators give
   \[
   U_-U_+^m v=m(2z-m+1)U_+^{m-1}v.
   \]
   Indeed expand $[U_-,U_+^m]=-2\sum_{k=0}^{m-1}U_+^kXU_+^{m-1-k}$ and use $XU_+^rv=(-z+r)U_+^rv$. Iteration yields $m!\prod_{k=1}^m(2z-k+1)$. With $z=\lambda+m$ this is (D4-L)'s coefficient.
3. **Splitting.** $U_-$ takes a resonance at $\lambda$ to one at $\lambda+1$, and preserves its allowed wavefront set. H-DFG-REG says the target is zero after sufficiently many steps. The nonzero ladder coefficient then splits each level of the nilpotence filtration, precisely the induction in DFG `581–591`. This proves the direct-sum algebra using the cited exhaustion/no-right-resonance input. At exceptional values the coefficient may vanish, so this proof cannot be extended by substitution.
4. **Adjacency from letters.** For a skew-adjoint derivation $B$, jumps $R=\sqrt\kappa B$ give
   \[
   R M_fR^* -\tfrac12\{R^*R,M_f\}
      =\tfrac\kappa2[B,[B,M_f]]=M_{\kappa B^2f/2}.
   \]
   Taking $B=H,E$ and $\kappa=1$ gives the asserted generator, and $Wf=0$ reduces it to $-2\Delta$. The phase choice $-iB$ for the jump gives the same dissipator. Its real spectrum is a consequence of D1 and H-AN, independently of the drift resonance spectrum.
5. **Comparison with finite Bass.** The finite relation is $R(T+qT^{-1})=\Sigma R$, proved in D7 from inverse-paired letters. The continuous polynomial is $\pi_*(A^2+A)=-\Delta\pi_*$. Exponentiating the two continuous roots gives the displayed cosine expression by elementary algebra. It does not identify the two polynomial pencils or preserve a global spectral label after sampling. The tower's infinitely many shifted first bands and topological multiplicities are still present. Fibre averaging is not injective on their total sum, and $X$ does not preserve $K$-invariants. Hence no full-space determinant compression follows.

This closes the *first-band* operator interpretation behind `09c_selberg_tower_cusp.tex:176–179`. H-DFG-REG already supplies the anisotropic resonance realization mentioned there as not established. An equality of suitably regularized scalar determinants could be deduced with separately fixed normalization factors from Selberg theory; it would not by itself be the literal operator compression requested in that item.

**Status: CORRECTED (L17–L19).**

## D5 — Spectral transfer, multiplication observables, and CP

### Statement (as proved)

The full transverse generator is the even **single-copy** operator
\[
 T_{\perp}=A\otimes1+1\otimes B_{\perp},\qquad
 B_{\perp}=\operatorname{diag}(0,0;1,-1),
\]
on even degrees $0,2$ and odd degree $1$. The two-term Selberg generator is $T_S=A\oplus(A+1)$ on $1|1$ coefficient spaces. Both have the flat supertraces and zetas in D2. They are graded spectral transfers, not the doubled transfer generators of `def:cmps-transfer-generators`.

For the function flow alone, conjugation is a genuine CP automorphism and
\[
 \operatorname{Ad}(e^{-tX})(M_f)=M_{e^{-tX}f}.
\]
Thus the scalar flow is realized on multiplication observables. Tensoring its observable vector space with an exterior algebra does not convert the resulting single-copy parity into a doubled-bond parity. A distributional $M_f$ is a map on test data, not generally a bounded observable or a Hilbert–Schmidt vector.

On smooth multiplication observables, adding the two dissipative jumps with coefficient $\kappa\geq0$ gives exactly
\[
 \mathcal L_\kappa(M_f)=M_{L_\kappa f},\qquad
 L_\kappa=-X+\tfrac\kappa2(H^2+E^2)
          =-X+2\kappa\Omega+\tfrac\kappa2W^2.
 \tag{D5-L}
\]
The jumps alone preserve $K$-invariants and equal $-2\kappa\Delta$ there. With the drift included, that subspace is no longer invariant. Nor is the horocyclic first band invariant under the added diffusion in general. The Selberg zeta established here is the $\kappa=0$ drift transfer; retaining a drift while adding arbitrary diffusion does not preserve its divisor.

### Hypotheses H-*

H-GEO, H-AN, H-DFG-REG, H-DZ-FLAT and H-DZ-MULT. **H-CORE:** multiplication by smooth functions and finite differential words are evaluated on the common smooth domain $C^\infty(SM)$; specified algebraic domain, exactly the qualification of `09b_selberg_dictionary.tex:190–210`. **H-CP-NORM:** when comparing with a genuine doubled-bond cMPS, its ring supertrace is the nonnegative squared norm proved in `04f_cmps_twisted_supertrace.tex:50–59`; this hypothesis is *not* assumed for flat traces.

### Proof

1. **Actual transverse dynamics.** The coframe dual to $(X,U_+,U_-)$ is global. Lie differentiation gives weights $0,-1,+1$ for the covectors, and hence weights $0,+1,-1,0$ for the backward flow on transverse exterior degrees. This gives $B_\perp$ and the single-copy semigroup. Its even drift and the stable-line restriction yield D2 exactly.
2. **Regular data and multiplicity.** Take test sections $\mathcal D=C^\infty(SM)\otimes\Lambda^*\langle\eta_+,\eta_-\rangle$ paired with distributions. For each desired left half-plane use the finite direct sum of DFG $\mathcal H^r$ spaces, shifting the scalar generator by $0,1,-1,0$; choose $r$ large enough to cover all these shifts. Use the closed differential domain of $A$ in each summand. Their meromorphic resolvents agree on overlapping regions by H-DFG-REG. Define $m_k(z)$ as the rank of the sector Riesz projection and $\nu=m_0-m_1$. Smooth test pairings separate distributions; H-DZ-MULT proves the determinant-residue identification. This supplies exactly the relative resonance data requested in `notes/ramanujan-graded/astra-proofs.md:704–790`. One fixed $L^2$ spectrum is not used as the divisor, nor is the order of a scalar correlation pole called a multiplicity.
3. **Single Kraus does not mean single-copy transfer.** For $K_t=e^{tT_\perp}$ the map $Y\mapsto K_tYK_t^*$ on $B(L^2(SM)\otimes\mathbb C^{2|2})$ is CP. Its doubled generator is $T_\perp\otimes1+1\otimes\overline{T_\perp}$ and its grading is the product grading. It is a different operator. On a finite bond its graded trace is $|\operatorname{Tr}(P K_t)|^2$, not $\operatorname{Tr}(P K_t)$. The doubled coefficient growth at time one would be $e^2$, not the proposed single-copy $e$. No honest trace is asserted for the infinite bond.
4. **Why the proposed multiplication-sector formula does not fix this.** The displayed covariance for $M_f$ follows by applying the operators to a test function. But an exterior vector $\omega$ is not automatically an operator on that coefficient bond; if it is embedded in an endomorphism space, conjugation acts on both its indices and must be computed. For real growth weights this gives sums of weights, not an arbitrary prescribed single-copy action. Moreover multiplication by nonzero $f$ on this non-atomic $L^2$ space is not Hilbert–Schmidt: on a set where $|f|>\epsilon$, an infinite orthonormal sequence has images of norm at least $\epsilon$. So these observables are not a doubled Hilbert-bond subspace whose own trace proves the asserted zeta.
5. **A direct norm-sign obstruction.** The finite exterior factor has $\operatorname{str}e^{tB_\perp}=2-e^t-e^{-t}<0$ for $t>0$. Both D2 orbital ring distributions are negative nonzero measures. Any actual cMPS ring norm is nonnegative by H-CP-NORM, and any distributional limit of nonnegative norm distributions stays nonnegative on nonnegative tests. Consequently these particular flat ring distributions cannot be identified with such norms. This does not prohibit an embedding with a different regularization or a restricted correlation functional; it does prohibit the identification asserted in the draft without additional construction.
6. **Chernoff is consistent but inapplicable as a construction.** `03d_graded_ramanujan_continuum.tex:39–61` addresses finite CPTP maps on a *doubled* bond. It permits an even drift and does not require an odd jump in every graded spectral model. The transverse parity here is a coefficient grading, not a parity-changing physical Kraus process. Therefore the absence of odd jumps is no contradiction, but also gives no CP realization or fixed-point statement.
7. **Drift plus jumps.** The drift generator of $Y\mapsto e^{-tX}Ye^{tX}$ is $-[X,Y]$, giving $-Xf$ on multiplication observables. D4 Step 4 gives the diffusion terms, proving (D5-L). On the $K$ sector the diffusion reduces to $-2\kappa\Delta$, but $[W,-X]=E\ne0$, so the drift does not preserve it. The diffusion also fails to commute with $X$ and fails to preserve $\ker U_-$: using $E=U_++U_-$ and $[U_-,E]=-2X$, one obtains
   \[
   [U_-,\tfrac12(H^2+E^2)]u=(2\lambda-1)U_+u
   \quad\text{when }(X+\lambda)u=U_-u=0.
   \]
   This is generally nonzero. Therefore the first-band proof is not stable under this added noise. Without drift, the $K$ eigenvalues $-2\kappa\sigma$ are real and unbounded to the left, so are not a nontrivial single vertical-line divisor. With drift there is a new differential operator whose divisor requires new analysis; neither preservation nor a universal destruction theorem is asserted without it.

**Status: CORRECTED (L20–L25).**

## D6 — Modular surface: established divisor facts and the missing bridge

### Statement (as proved)

For $\Gamma=\mathrm{PSL}_2(\mathbb Z)$ and a nontrivial Riemann zero $\rho$ of order $m$, the scattering determinant has a pole of order $m$ at $s_0=\rho/2$, and $Z_S$ has a zero there of order $m$. Thus RH is equivalent to **these** zeros lying on $\Re s=1/4$. It is not equivalent to a $1/4$ line for the full Selberg divisor, which also has the discrete Laplace spectrum on the $1/2$ line.

At a scattering pole one must use the **leading Laurent coefficient** of the Eisenstein series, not the undefined value $E(z,s_0)$. That coefficient has a nonzero $y^{1-s_0}$ constant term and is not in $L^2$. The compact argument using a Haar norm therefore fails at the pushforward-to-$L^2$ step. The algebraic Casimir identity remains valid wherever a corresponding distributional first-band state is available.

For a putative flow first-band state with $\lambda=s_0-1$, the proposed rescaling $e^{t/2}$ can never make its flow unitary in a positive norm: $\Re(\lambda+1/2)=\Re s_0-1/2<0$. This impossibility holds for *any* positive finite norm on that eigenvector, independently of RH and independently of how the form was built. The correct proposed flow centre for the scattering-zero subset would be $-3/4$, whereas the Riemann functional-model centre is $-1/4$.

### Hypotheses H-*

- **H-MOD:** the standard complete finite-area modular orbifold with its self-adjoint Laplacian and one cusp. Its torsion means that H-GEO's compact surface divisor cannot be reused; elliptic and parabolic factors must be included.
- **H-PHI:** the given scattering formula and functional equation $\phi(s)\phi(1-s)=1$. Standard, verified in `refs/src/1607.08053/main.tex:592–601` and `refs/src/1108.5659/main.tex:2071–2079`.
- **H-ZETA:** the Riemann functional equation, Euler-product nonvanishing for $\Re z>1$, and the nontrivial zero region $0<\Re\rho<1$, $\Im\rho\ne0$. Standard classical facts; the last region is explicitly assumed in `04b_phantasm_forced.tex:96–101`. Their full proofs are not in the supplied source excerpts. No RH or simplicity hypothesis is made.
- **H-CUSP-DIV:** the finite-area Selberg divisor theorem, verified as stated in FJS `refs/src/1607.08053/main.tex:370–401`. FJS attributes it at line `371` to Venkov, *Spectral Theory of Automorphic Functions*, p. 49, and Hejhal, *The Selberg Trace Formula for PSL(2,R)*, vol. II, p. 499. **Those original book pages have not been checked here**; the FJS statement has. There is no invented “H-Iwaniec” citation.
- **H-EIS:** Eisenstein eigenfunction equation, constant term, meromorphic continuation and functional equation. Standard and explicitly recalled in `refs/src/1108.5659/main.tex:2037–2049,2067–2079`. For the truncation calculation, use the usual cusp Fourier expansion with exponentially decreasing nonconstant terms, locally meromorphic in $s$; that last decay statement is a standard Fourier–Bessel fact, not proved in that excerpt. The boundary calculation below derives the Maass–Selberg identity from these inputs.
- **H-MOD-GAP:** the $1/4$ property for the full modular group is a known theorem. A verified primary source is Booker–Lee–Strömbergsson, [*Twist-minimal trace formulas and the Selberg eigenvalue conjecture*](https://arxiv.org/pdf/1803.06016), Theorem 1.1, p. 1 (web text lines 16–17), covering $\Gamma(N)$ for $N\leq226$, hence $N=1$. This extra source is used only to correct the draft's “open” claim for this particular group, not as an input about Riemann zeros.

The *unavailable* hypothesis needed to promote this to a D3 theorem is **H-CUSP-BRIDGE**: a specified noncompact flow resolvent realization, with finite-rank resonant data at $s_0-1$, a multiplicity-preserving first-band pushforward to Eisenstein Laurent data, and a compatible positive modal pairing. No such theorem is proved by the compact DFG lines cited in the brief. It is explicitly **not assumed** in the conclusions above.

### Proof and boundary of the conclusion

1. **Scattering poles.** At $s_0=\rho/2$ all gamma factors in H-PHI are finite and nonzero. The numerator $\zeta(\rho-1)$ is nonzero: its functional equation relates it to $\zeta(2-\rho)$ in $\Re(2-\rho)>1$, with nonzero elementary factors because $\rho$ is nonreal. Thus the denominator's order $m$ survives. H-PHI reflects this pole to a zero of $\phi$ at $1-s_0$ with the same multiplicity; H-CUSP-DIV puts a Selberg zero at $s_0$. It has no collision with a discrete Laplace zero, since $0<\Re s_0<1/2$ and $\Im s_0\ne0$.
2. **Precisely which finite-area divisor theorem is used.** For a one-cusp group, H-CUSP-DIV lists: discrete eigenvalue zeros on the $1/2$ line and in $(1/2,1]$ with multiplicity $m(\sigma)$; lower real partners with multiplicity $m(\sigma)-q(1-s)$, where $q$ is the residual scattering-pole multiplicity; at $1/2$, signed order $2d_{1/4}-(1-\phi(1/2))/2$; parabolic poles at $-n-1/2$, $n\geq0$, of order one; zeros reflected from scattering zeros in $\Re s>1/2$; and the integer topological/elliptic divisor with the multiplicities in FJS `389–401`. In the latter formula for negative integers $-n$, $n\geq1$,
   \[
   m_n=(2n+1)(2g-1)+2n e-2\sum_{R}\lfloor n/d_R\rfloor,
   \]
   where $e$ counts elliptic conjugacy classes and $d_R$ are their orders. For the modular group $g=0$, $e=2$, $d_R=2,3$, this is $2n-1-2\lfloor n/2\rfloor-2\lfloor n/3\rfloor$. At zero the modular zeta has signed order $-1$: in FJS's completion $Z_+=Z/[G_1(s)\Gamma(s-1/2)]$ (`404–423`), the residual multiplicity is $m(0)-q(1)=1-1=0$, while $G_1$ from `282–287` has a simple pole at zero (the exponent $2g-2+1$ is $-1$ and all Barnes factors there are nonzero). Also $\phi(1/2)=-1$ by FJS `598`, so the modular signed order at $1/2$ is $2d_{1/4}-1$. These signed endpoint orders are separate from the nonreal scattering subset proved in Step 1; no compact genus multiplicities have been reused for the orbifold.
3. **Why the Haar norm fails.** From $E(z,s)=\phi(s)E(z,1-s)$ and the nonzero constant term, the pole order of $E$ at $s_0$ is $m$. Write $E(z,s)=(s-s_0)^{-m}e_{-m}(z)+\cdots$ and $\phi(s)=(s-s_0)^{-m}c_{-m}+\cdots$, with $c_{-m}\ne0$. Then $e_{-m}$ solves $\Delta e_{-m}=s_0(1-s_0)e_{-m}$ and has cusp constant term $c_{-m}y^{1-s_0}$. Its squared cusp norm contains
   \[
   |c_{-m}|^2\int_Y^\infty y^{-2\Re s_0}\,dy=\infty.
   \]
   Formal symmetry of $\Delta$ on its $L^2$ domain says nothing about this non-domain eigenfunction. Indeed $s_0(1-s_0)$ is nonreal, since $\Im s_0\ne0$ and $\Re s_0\ne1/2$. The algebra was not lost; the Hilbert-space step was.
4. **What is still covered by self-adjointness.** It applies to $L^2$ cusp forms and residual eigenfunctions, including the constant; for the modular group the residual space is only the constant (FJS `601`). More generally there can be further residual modes. The continuous spectrum also has a positive direct-integral spectral theory on its physical line, so “precisely cusp forms and constant” is too restrictive as a statement about all of Laplace spectral theory. None of this supplies positive norms for the *off-physical-sheet scattering poles*. A first-band realization on the noncompact flow still needs H-CUSP-BRIDGE, rather than a blanket application of compact DFG.
5. **Rates and FE differ.** On a genuine flow eigenvector the rescaled norm is multiplied by $e^{t(\Re s_0-1/2)}$, strictly less than one for $t>0$. This proves the corrected no-go in the statement. Under RH the flow rate would be $-3/4$; the subset's Riemann reflection is $s\mapsto1/2-s$, or $\lambda\mapsto-3/2-\lambda$. The compact reflection $s\mapsto1-s$ instead exchanges scattering poles with zeros of the scattering determinant; it does not preserve this odd zero subset. The Riemann model in `04b_phantasm_forced.tex:246–265` uses $B$ eigenvalues $-\bar\rho/2=-\bar s_0=-1-\bar\lambda$, with centre $-1/4$. Its identification with a flow compression is not proved by these affine relations or by the prime-measure identity in `09c_selberg_tower_cusp.tex:122–138`.
6. **Maass–Selberg, with its normalization fixed.** Use a width-one cusp and $Y$ above the compact core. Let $\Lambda^Y E(s)$ subtract the constant term $y^s+\phi(s)y^{1-s}$ for $y>Y$ and leave $E(s)$ unchanged below $Y$. For regular parameters, and by meromorphic continuation with limits at removable denominators,
   \[
   \begin{aligned}
   \langle\Lambda^YE(s),\Lambda^YE(w)\rangle
   ={}&\frac{Y^{s+\bar w-1}-\phi(s)\overline{\phi(w)}Y^{1-s-\bar w}}
              {s+\bar w-1}\\
      &+\frac{\overline{\phi(w)}Y^{s-\bar w}-\phi(s)Y^{\bar w-s}}{s-\bar w}.
   \end{aligned}
   \tag{D6-MS}
   \]
   Here the displayed pairing uses the convention linear in the first entry. To verify the formula, apply Green's identity to the two eigenfunction equations on the truncated domain, cancel paired sides of a fundamental domain, and add the integrals of nonconstant Fourier terms above $Y$. Their boundary Wronskians cancel by decay. With the boundary orientation chosen accordingly, each constant-term monomial pair $y^a,y^b$ gives $(a-\bar b)Y^{a+\bar b-1}$ divided by $\bar b(1-\bar b)-a(1-a)=(a-\bar b)(a+\bar b-1)$, hence $Y^{a+\bar b-1}/(a+\bar b-1)$. Substituting the four exponent pairs $a=s,1-s$, $b=w,1-w$ gives exactly the two terms in (D6-MS), with the negative signs shown. This also derives the identity without inventing an unchecked page citation for it.
7. **Positivity at a scattering pole does not imply RH.** Take the leading bivariate Laurent coefficient of (D6-MS) at $s=w=s_0$. Only the $\phi(s)\overline{\phi(w)}$ term contributes at order $(-m,-m)$, so
   \[
   \|\Lambda^Y e_{-m}\|^2
     =\frac{|c_{-m}|^2Y^{1-2\Re s_0}}{1-2\Re s_0}>0.
   \]
   This holds throughout $0<\Re s_0<1/2$, not only at $1/4$. Its growth with $Y$ is exactly the missing Haar integrability. Positivity of these truncated norms is therefore not the desired RH coercivity. A finite word in the letters applied to a vector in the common $L^2$ domain of all those derivatives still produces an $L^2$ vector and cannot produce $e_{-m}$. But unrestricted $C^\infty$ functions on a noncompact surface need not lie in $L^2$; the draft's proposed class “finite words applied to $L^2$ or $C^\infty$” does not define a general no-go for every weighted form. At the corrected centre, existence of an invariant positive form would need a new construction, with RH and Jordan data accounted for.

**Status: OPEN (exploratory), with proved corrections L26–L31.** What is missing is H-CUSP-BRIDGE and a positive form at the *correct* rate on its specified regular data. The divisor inclusion, failure of the Haar argument, wrong-rate obstruction, and truncated-norm computation above are established; no RH statement or general impossibility theorem for all weighted constructions is claimed.

## D7 — A constructive common theorem for graph and quantum Hashimoto lifts

### Statement (as proved)

The following finite-dimensional theorem covers both cases. Let $\mathcal V$ be a finite Hilbert space, $\mathcal W$ its edge space, and let
\[
 T=SR-J_0,\quad J_0^2=1,\quad RS=\Sigma=\Sigma^*,\quad RJ_0S=D\,1,
 \quad D=q+1>2.
 \tag{D7-data}
\]
In the concrete cases below also $S^*S=D1$, $J_0^*=J_0$, and $S^*J_0S=\Sigma$. All maps preserve the specified parity.

For **$\mu\ne\pm1$**,
\[
 R:\ker(T-\mu)\overset{\sim}{\longrightarrow}
     \ker(\Sigma-(\mu+q/\mu)),\qquad
 F_\mu f=\frac{\mu S-J_0S}{\mu^2-1}f
 \tag{D7-push}
\]
are inverse maps whenever the spaces are nonzero. Here $T$ is invertible, so $\mu=0$ is not an eigenvalue. **$\mu=\pm\sqrt q$ is not an exception to this eigenspace isomorphism.** It is an exception to semisimplicity of the full band.

Let $\mathcal V_{\rm ret}$ be the orthogonal sum of the $\Sigma$ eigenspaces with the entire structural $\pm D$ spaces removed. The cycle/reversal modes at $\mu=\pm1$ are excluded from the edge band. On
\[
 \mathcal W_{\rm band}=\{Sf+J_0Sg:f,g\in\mathcal V_{\rm ret}\},
\]
the map $L(f,g)=Sf+J_0Sg$ is an isomorphism, and
\[
 L^{-1}TL=C=\begin{pmatrix}\Sigma&qI\\-I&0\end{pmatrix},\qquad
 G_C=\begin{pmatrix}I&\Sigma/2\\\Sigma/2&qI\end{pmatrix},\qquad
 C^*G_CC=qG_C.
 \tag{D7-G}
\]
The metric $G_C$ is positive definite iff **the strict sector band** $|a|<2\sqrt q$ holds for every retained adjacency eigenvalue. It transports by $L^{-1}$ to an explicit metric on the edge band. In that case $T/\sqrt q$ is unitary in this metric. Moreover
\[
 F_C=\begin{pmatrix}0&\sqrt q I\\q^{-1/2}I&0\end{pmatrix},\qquad
 F_C^2=1,\quad F_CC F_C=qC^{-1},\quad F_C^*G_CF_C=G_C.
 \tag{D7-FE}
\]
Thus the operator FE is also constructed, without selecting arbitrary eigenvectors.

The **closed** bound $|a|\leq2\sqrt q$ is equivalent to the circle statement for the full band eigenvalue multiset. But if an endpoint occurs, $C$ has a nontrivial size-two Jordan block for each corresponding vertex eigenvector. Therefore a positive form making the *full algebraic band* unitary exists iff the bound is **strict**. On the direct sum of eigenstates alone, one can use branchwise pullbacks under $R$ and obtain unitarity for the closed bound, at the cost of losing half the endpoint algebraic multiplicity. This is exactly D3's distinction.

For a graded zeta, the reduced divisor sees only $m_0(a)-m_1(a)$. Full sector Ramanujan implies divisor Ramanujan, while cancellations can hide out-of-band eigenvalues. Positive forms for the actual retained sectors cannot be inferred just from the reduced divisor.

**Graph convention.** For an oriented edge $(v,w)$, use
\[
 (Tu)(v,w)=\sum_{x\sim v,\ x\ne w}u(x,v),\quad
 (Ru)(v)=\sum_{x\sim v}u(x,v),\quad
 (Sf)(v,w)=f(v),\quad (J_0u)(v,w)=u(w,v).
\]
Then $\Sigma$ is the usual symmetric adjacency, and
\[
 (F_\mu f)(v,w)=\frac{\mu f(v)-f(w)}{\mu^2-1}.
\]
The generic exact exception is $\mu=\pm1$; the extra cycle eigenvectors there prevent a uniform eigenspace isomorphism. On a connected nonbipartite graph only $D$ is a vertex period mode; on a connected bipartite graph $-D$ is also removed. Their quadratic partners are $1,q$ and, when present, $-1,-q$.

**Quantum convention.** Put $\mathcal V=\operatorname{End}(V)$, $E_i=\operatorname{Ad}(U_i)$, $\Sigma=\sum_iE_i=D\Phi$, and use exactly the notebook's source-letter convention
\[
 (Tx)_j=\sum_{i\ne\bar j}E_i x_i,\qquad
 Rx=\sum_i E_i x_i,\quad (Sf)_j=f,\quad (J_0x)_j=E_{\bar j}x_{\bar j}.
\]
Thus the correct pushforward uses **$\operatorname{Ad}(U_i)$**, not $\operatorname{Ad}(U_i^*)$, in this convention. Its inverse is
\[
 (F_\mu f)_j=\frac{\mu f-E_{\bar j}f}{\mu^2-1}.
\]
The theorem applies separately on the even and odd Hilbert–Schmidt sectors, with $\Gamma=\operatorname{Ad}P$. Homogeneous letters are sufficient; a group representation is not required for this algebra. A representation and Harrow's theorem are one way to obtain the additional band bound.

### Hypotheses H-*

H-GRAPH or H-UNIT, as applicable; H-BAND only for the circle conclusion and its strict version for the positive algebraic-band metric. Finite spectral theorem and ordinary matrix algebra are used. The notebook's convention and determinant identity are `08_quantum_ihara_general.tex:24–61,100–110`; graded restrictions and cancellation qualifications are `03c_graded_ramanujan.tex:91–129`. Those references are consistent with the theorem, but the intertwining, metric and endpoint analysis are proved here.

### Proof

1. **The common letter identities.** For a graph, $RSf(v)=\sum_{x\sim v}f(x)$ and $RJ_0Sf(v)=Df(v)$. Edge reversal is a unitary involution, $S^*S=D1$, and $S^*J_0S=\Sigma$. Symmetry is from undirected reversal; arbitrary regular graphs need not possess a preassigned decomposition into globally inverse-labelled neighbour permutations. For a Cayley graph those permutations give the same symmetry directly. In the quantum case $E_i^*=E_i^{-1}=E_{\bar i}$ in the Hilbert–Schmidt form. Thus $\Sigma^*=\Sigma$, $J_0^*=J_0$, $J_0^2=1$, and $RJ_0S=\sum_iE_iE_{\bar i}=D1$. The remaining identities follow by summing components. All maps commute with grading because $\operatorname{Ad}(U_i)$ does, even when $U_i$ is odd.
2. **Elimination and invertibility.** $TJ_0=SRJ_0-1$, while $(SRJ_0)^2=D(SRJ_0)$. Its eigenvalues are among $0,D$, so $SRJ_0-1$ is invertible for $D>1$; hence $T$ is invertible. Also
   \[
   RT=\Sigma R-RJ_0,\qquad RJ_0T=qR,
   \qquad \Sigma R=R(T+qT^{-1}).
   \]
   The second identity follows by $RJ_0(SR-J_0)=(D-1)R$. On a $\mu$-eigenvector the last identity gives the quadratic $\mu^2-a\mu+q=0$ for its image under $R$.
3. **The inverse pushforward.** If $Tu=\mu u$, then $(\mu+J_0)u=SRu$. For $\mu^2\ne1$, $(\mu+J_0)^{-1}=(\mu-J_0)/(\mu^2-1)$, yielding (D7-push) and injectivity. Conversely for $\Sigma f=(\mu+q/\mu)f$,
   \[
   RF_\mu f=\frac{\mu\Sigma-D}{\mu^2-1}f=f,
   \]
   and $(\mu+J_0)F_\mu f=Sf$ gives $TF_\mu f=\mu F_\mu f$. This proves surjectivity, even at the double roots $\mu=\pm\sqrt q$ when $q>1$. At $\pm1$ the inverse fails exactly where the reversal/cycle subspace can contribute. At $q=1$ these exceptions coincide with the endpoints; the degree-two cycle case is outside H-GRAPH/H-UNIT's present theorem and has a directly unitary permutation flow.
4. **Two-copy companion space.** From (D7-data), $TS=S\Sigma-J_0S$ and $TJ_0S=qS$, proving $TL=LC$. Furthermore
   \[
   L^*L=\begin{pmatrix}DI&\Sigma\\\Sigma&DI\end{pmatrix}.
   \]
   A symmetric graph adjacency or a sum of $D$ unitaries has spectrum in $[-D,D]$. Once all $\pm D$ spaces are removed this Gram matrix is positive, so $L$ is injective and hence isomorphic to its displayed image. This includes the algebraic endpoint blocks and specifies the actual invariant subspace, rather than cancelling multiplicities to manufacture a new operator.
5. **Positive metric and FE by multiplication.** Multiply the two-by-two operator matrices in (D7-G): the upper-left entry is $\Sigma^2-\Sigma^2+qI=qI$, the off-diagonal entries are $q\Sigma/2$, and the lower-right entry is $q^2I$. Thus $C^*G_CC=qG_C$. The Schur complement is $qI-\Sigma^2/4$, so positivity is exactly the strict band. The three identities (D7-FE) follow by the same multiplication. These formulas use only $\Sigma$, its Hermitian form, and $q$, all derived from the labelled letters; no CP principle is being substituted for the bound.
6. **Circle, endpoint, and necessity.** For real $a$, the roots of $\mu^2-a\mu+q$ both have modulus $\sqrt q$ iff $|a|\leq2\sqrt q$. At $a=2\epsilon\sqrt q$, $C_a-\epsilon\sqrt q I$ is a nonzero square-zero matrix, hence a size-two Jordan block. A positive-metric unitary is diagonalizable, so the endpoint is impossible on the entire block. Outside the closed band an eigenvalue has wrong modulus, also impossible. This proves the sharp iff for positive algebraic-band unitarity. For distinct roots, the alternative metric $\sum_\mu\langle Ru_\mu,Rv_\mu\rangle$ works by branchwise orthogonalization; the untagged metric $\langle Ru,Rv\rangle$ has a kernel formed by differences of partner lifts, exactly as in D3.
7. **Divisor versus sectors.** Applying the determinant Bass identity on each parity sector gives factors $(1-au+qu^2)$ with signed multiplicities $m_1(a)-m_0(a)$ in the ring zeta. Equal factors cancel. This proves both the sufficient sector bound and the failure of its converse after cancellation. The geometric $\pm1$ factors are supplied as structural modes with their own signed multiplicities; balanced grading cancels them in the net divisor but does not remove their actual vectors from the operator unless the retained subspace is specified.
8. **Verified examples and counterexamples.** The finite script checks every retained adjacency eigenvector and both lifts, the metric identity, its positivity test, operator FE, and the two graded Bass determinants. It tests Petersen, $K_4$, the degree-$14$ LPS Cayley graph on PGL$_2(\mathbb F_5)$ (120 vertices), its six-dimensional principal-series bond with $3|3$ grading, and the six Pauli letters. For Pauli, the even spectrum is $\{6,-2\}$, the odd spectrum is $\{-2,-2\}$, and
   \[
   Z(u)=\frac{1+2u+5u^2}{(1-u)(1-5u)},\quad
   N_P(1),\ldots,N_P(6)=8,32,104,640,3208,15392.
   \]
   The quantum operator is not being replaced by its reduced zeta: one odd quadratic cancels the even $P$-mode quadratic only at divisor level.
9. **Exact endpoint counterexamples.** The graph $K_3\square Q_3$ is connected and $5$-regular, with spectrum obtained by adding $\{2,-1,-1\}$ to $\{3,1,1,1,-1,-1,-1,-3\}$. Every nontrivial value lies in $[-4,4]$, so it is Ramanujan, and $-4$ has multiplicity two. Its Hashimoto matrix satisfies $\dim\ker(T+2)=2$, $\dim\ker(T+2)^2=4$, verified by exact rational linear algebra. For the quantum example, take $I$ four times, $X$ four times and $Z$ twice, paired within equal letters, with $P=Z$. Then $D=10$, $q=9$, even adjacency $\{10,2\}$ and odd adjacency $\{6,-2\}$. It is sector-Ramanujan, but the odd Hashimoto eigenvalue $3$ has kernel dimension one and squared-kernel dimension two. Its endpoint odd quadratic survives in the net zeta. Both are finite counterexamples to the draft's unqualified “unitary iff Ramanujan” assertion.

**Status: CORRECTED (L32–L36), with exact finite counterexamples to the omitted endpoint qualification.** The notebook's open “Hermitian channel plus lift” principle is settled in this inverse-paired setting, with strictness/Jordan and net-divisor qualifications. It is not a theorem for arbitrary Hermitian CP channels without an inverse-paired lift.

## D8 — K-type parity is not the transverse or Hodge grading

### Statement (as proved)

For the right $K$ representation on $L^2(SM)$, let $Wf=imf$, $m\in2\mathbb Z$, and set $P_Kf=(-1)^{m/2}f$. Then
\[
 P_KHP_K=-H,\quad P_KEP_K=-E,\quad P_KWP_K=W.
\]
The diffusion $L_{\rm adj}=\tfrac12(H^2+E^2)$ is even, but **the geodesic generator $X=H/2$ is odd**. Thus $P_K$ is not a commuting grading for $e^{-tX}$.

Full K-type parity is not the Hodge parity on $M$. The latter uses two copies of weight zero for degrees zero and two, and the associated weight $\pm2$ bundles for degree one, with the actual Hodge Laplacian. On that genuine complex,
\[
 \operatorname{str}e^{-t\Delta_{\rm Hodge}}=\chi(M).
\]
This identity cannot be transferred to all K-types or to the two-jump diffusion merely by renaming weights. For example on a spherical principal-series constituent with Casimir $-\sigma$,
\[
 \operatorname{Tr}\bigl(P_K e^{tL_{\rm adj}}\bigr)
   =e^{-2\sigma t}\sum_{n\in\mathbb Z}(-1)^n e^{-2n^2t}\ne0
   \quad(t>0).
 \tag{D8-counter}
\]
The transverse grading does give D2's ring functions, but the full exterior algebra gives Ruelle, and the two-term stable transverse complex gives Selberg. A K-type grading remains a possible grading for the *diffusion representation channel*, subject to its own doubled parity and spectral analysis; it does not identify that channel with this Selberg flow transfer.

### Hypotheses H-*

H-GEO, H-SL2, H-AN. **H-KTYPE:** in a spherical principal-series constituent of the right regular representation of PSL$_2(\mathbb R)$, every weight $2n$ occurs once and the Casimir is scalar $-\sigma$. Standard representation theory; the rate formula is recalled in `03d_graded_ramanujan_continuum.tex:105–120` and the prior proof `notes/ramanujan-graded/astra-proofs.md` D11; no detailed representation-theoretic proof is present in the listed source excerpts. It can alternatively be obtained by the usual nonvanishing K-raising/lowering relations on a spherical eigenfunction with $\sigma>1/4$. **H-HODGE:** the standard de Rham/Hodge identification on the closed oriented surface, with harmonic dimensions $1,2g,1$. DFG `RuelleResonForHn.tex:4949–4975` recalls the Hodge operators and proves the relevant positive coexact correspondence; the general harmonic-dimension theorem is not proved there. The positive-eigenvalue cancellation is proved below. Neither input is needed for the elementary obstruction $P_KX=-XP_K$.

### Proof

1. **K weights.** From $[W,H]=-2E$, $[W,E]=2H$, the complex combinations $H\pm iE$ change weight by $\pm2$ (with the sign determined by the chosen combination). Both flip $(-1)^{m/2}$; $W$ preserves it. This proves the parity claims and also proves that the proposed geodesic grading fails before any trace is taken. On a doubled bond the drift generated by $X$ likewise changes sign under $\operatorname{Ad}P_K$; it is not an even cMPS drift.
2. **What Hodge cancellation actually proves.** For a positive scalar Laplace eigenvalue $\sigma$, the maps $f\mapsto df$ and $f\mapsto *df$ give two independent one-form eigenspaces, matching the function and volume-form eigenspaces. Conversely the exact/coexact decomposition of a positive-eigenvalue one-form follows by applying $\sigma^{-1}(dd^*+d^*d)$. All positive eigenvalues therefore cancel by degree. The harmonic contribution is $1-2g+1=\chi(M)$ by H-HODGE. This is a proof on $\Omega^0(M)\oplus\Omega^1(M)\oplus\Omega^2(M)$, not on $\bigoplus_{m\in2\mathbb Z}L^2(SM)_m$.
3. **The operators are also different.** On a weight $m$, $L_{\rm adj}=2\Omega-m^2/2$. Thus weights $0$ and $\pm2$ carry an extra relative diffusion shift $-2$. Even on the selected Hodge bundles, with the standard Casimir realization of their Hodge Laplacians, the diffusion heat supertrace would be
   \[
   2\operatorname{Tr}e^{-2t\Delta_0}-e^{-2t}\operatorname{Tr}e^{-2t\Delta_1}
   =2(1-e^{-2t})\operatorname{Tr}e^{-2t\Delta_0}+e^{-2t}\chi(M),
   \]
   not the constant Hodge supertrace. More fundamentally, the full K-type space has one weight-zero copy and infinitely many further weights, so it is not this three-term complex at all.
4. **Explicit noncancellation.** Under H-KTYPE, $m=2n$ has diffusion eigenvalue $-2\sigma-2n^2$. Summing its absolutely convergent heat trace gives (D8-counter). Poisson summation of a Gaussian gives
   \[
   \sum_{n\in\mathbb Z}(-1)^n e^{-2tn^2}
    =\sqrt{\frac\pi{2t}}\sum_{k\in\mathbb Z}
        e^{-\pi^2(k+1/2)^2/(2t)}>0.
   \]
   Hence a positive Laplace eigenvalue need not supercancel under K parity. The finite script evaluates both convergent expressions at $t=1$, obtaining $0.730000328323$ for the theta factor. This numeric check illustrates the counterexample; the strictly positive Gaussian sum proves it.
5. **Precise replacement for the notebook observation.** In `03d_graded_ramanujan_continuum.tex:156–171`, retain the transverse Lefschetz explanation, but replace “Selberg is the odd-degree factor” by D2's determinant ratio/two-term complex. Remove the inference that identifying weight zero with functions and weights $\pm2$ with one-forms constructs the Selberg grading on a doubled representation bond. Those associated-bundle identifications are useful, and K parity genuinely grades the diffusion letters, but the omitted second scalar copy, further K-types, drift parity, diffusion shift and doubled-bond geometry all require separate treatment. They do not prove “no net-odd divisor” for that representation channel either.

**Status: CORRECTED (L37–L40), with the explicit noncancellation counterexample (D8-counter).**

## Correction ledger

Each row is one change of mathematical assertion; purely typographical source-line updates are included where they could otherwise misidentify a theorem.

| Row | Claimed in the draft | True statement | Why |
|---|---|---|---|
| L01 | $s\mapsto s(1-s)$ sends the divisor into the line/interval union. | Its **preimage** of the nonnegative Laplace spectrum lies in that union. | D1, quadratic roots; the displayed map points the other way. |
| L02 | The Ruelle constant zero at $1$ is partnered by a pole at $0$. | The net order at $0$ is the **zero** order $c=2g-2$; constant factors cancel there. | D2's exact quotient divisor. |
| L03 | Unspecified topological zeros and poles at nonpositive integers. | Net Ruelle orders are $c$ at $0$, $2c-1$ at $-1$, $2c$ thereafter; record the hidden even constant contribution separately. | Subtract the two full Selberg divisors. |
| L04 | Full Ruelle retained divisor has a Selberg-centred Ramanujan/FE statement. | Its odd and even spectral bands have different centres; full retained FE and Ram fail. | Even band is translated by $-1$ and reflection does not preserve parity multiplicity. |
| L05 | Shifted spectral poles can be called trivial period images without changing the statement. | Removing them is extra retained-divisor data; they depend on the nonconstant Laplace spectrum. | A transverse Jacobian shift is not a period mode of the Perron root. |
| L06 | Function flow's ring zeta is its tower determinant. | Even function flow gives $1/D_{\rm tow}$; all-odd flow gives $D_{\rm tow}$. | The ring exponential has the plus sign, the flat determinant the minus sign. |
| L07 | Selberg, full transverse Ruelle, and the all-band tower may be used interchangeably. | Selberg is the ring zeta of even $A$ / odd $A+1$; full transverse forms give Ruelle. | Exact orbital calculation and $D(s-1)/D(s)=Z_S(s)$. |
| L08 | Reference pair $(1,0)$ behaves as CP Perron and partner data. | Both Selberg constant roots are net odd; the pair is spectral reference data only. | Selberg is entire, with zeros at both constants; no CP Perron pole is supplied. |
| L09 | Threshold and tower trivial multiplicities need no special counting. | Selberg threshold order is $2d_{1/4}$; tower has order one at zero and $cN^2+2$ at $-N$. | H-SZ and exact shift sum. |
| L10 | $\Omega=X^2+U_+U_-+X$ in the stated ordering. | $\Omega=X^2+U_+U_--X$. | $[U_+,U_-]=2X$. |
| L11 | Centrality and letter algebra establish the first-band identification. | They establish the target eigenspace; injectivity/surjectivity and resonance regularity are DFG/Poisson analysis. | A zero pushforward cannot yield a Rayleigh quotient. |
| L12 | One total Haar pullback is positive on all first-band branches. | It has partner-difference kernel; the **orthogonal sum** of branchwise pullbacks is positive. | Both branches push to the same $E_\sigma$. |
| L13 | Closed $1/4$ coercivity gives HP on the complete algebraic band. | It gives divisor Ram and eigenstate HP; full algebraic-band HP also needs no threshold. | At $1/4$, algebraic multiplicity $2d$ exceeds geometric $d$. |
| L14 | $JXJ^{-1}=-1-X$. | $JAJ^{-1}=-1-A$ for $A=-X$; $JXJ^{-1}=1-X$. | Resonance parameter is the eigenvalue of $-X$. |
| L15 | Constant and exceptional parameters are covered by the same inverse pushforward/FE. | Constant at $0$ is excluded structurally; first-band pushforward at $-1$ is zero. Threshold and ladder exceptions are different. | D3 Step 9 and DFG's different exception sets. |
| L16 | DFG boundary formula at lines 619–621, Poisson at 631–633, suffices for all algebraic conclusions. | Formula at 612–615 and its interpretation at 619–624; analytic isomorphism at 626–636, with semisimplicity separately at 357–375. | Precise byte-read provenance; eigenstate isomorphism is not algebraic-multiplicity equality. |
| L17 | Unqualified ladder formula on all resonances. | Eigenspace splitting holds outside $-1-\tfrac12\mathbb N_0$; singular coefficients cannot be inverted. | D4 ladder proof. |
| L18 | Exponentiation turns the flow/Laplacian relation into the Ihara quadratic with the same adjacency. | The sampled adjacency is the cosine functional calculus $a_\tau(\Delta)$, not $-2\Delta$. | Sum of the two exponentiated roots; sampling aliases frequencies. |
| L19 | First-band intertwining resolves the full-tower compression. | It proves the first-band polynomial relation and ladder; literal global compression remains unsupplied. | Two branches, descendants, exceptional states and normalization cannot be collapsed by $\pi_*$. |
| L20 | The single-copy exterior drift itself is a graded CP/cMPS transfer. | Its conjugation is CP on a larger doubled space, with another generator and another trace. | A Kraus operator is not its own doubled transfer. |
| L21 | $M_f\otimes\omega$ automatically identifies the doubled graded sector. | One needs an actual operator embedding and induced parity/action; multiplication observables are not HS vectors. | D5 Step 4. |
| L22 | Growth $q=e$ for the claimed CP transfer. | This is a single-copy coefficient growth; its conjugation has doubled coefficient growth $e^2$. Neither is a Selberg CP Perron statement. | The two exponents add in the doubled transfer. |
| L23 | The negative exterior flat supertrace is a physical ring norm. | These negative distributions cannot be honest squared norms or positive distributional limits of them. | cMPS supertrace positivity versus $-C$ and $-C/(1-e^{-t})$. |
| L24 | Missing odd jumps follows from, or conflicts with, the Chernoff proposition. | The proposition permits even drift; it neither requires odd jumps nor constructs this spectral grading as CP. | Its hypotheses concern finite CPTP doubled bonds. |
| L25 | Adjacency jumps can be added while keeping the Selberg divisor by retaining drift. | Generator is (D5-L); its first-band and $K$ subspaces are generally not invariant. | Explicit commutators; new spectral analysis is needed. |
| L26 | Cusp divisor needs an invented/unverified Venkov assertion. | The required scattering subset is verified in FJS 370–401; original Venkov/Hejhal pages remain unchecked. | Supplied primary text already states the finite-area divisor theorem. |
| L27 | First-band cusp states push to the value $E(z,\rho/2)$. | At a pole use leading Laurent coefficients (and generalized data for higher orders). | The value is undefined; its nonzero constant term proves nonintegrability. |
| L28 | Selberg's $1/4$ property is open for PSL$_2(\mathbb Z)$. | It is known for that group; the general congruence-level conjecture is different. | Verified Booker–Lee–Strömbergsson Theorem 1.1 includes level one. |
| L29 | The compact mechanism covers precisely cusp forms and the constant on every one-cusp surface. | It applies to the $L^2$ discrete/residual modes; physical continuous spectral theory also remains positive. Noncompact flow correspondence is additional. | General residual modes exist; compact DFG is not a cusp theorem. |
| L30 | $e^{t/2}$ is the candidate unitarizing factor for $\lambda=\rho/2-1$. | It is impossible for that subset under any positive eigenvector norm; RH would give factor $e^{3t/4}$. | Exact real parts; Riemann-model factor $e^{t/4}$ belongs to $-\bar\rho/2$. |
| L31 | Truncated norm positivity might force $\Re s_0=1/4$; all forms from smooth words are ruled out. | Leading norm is $|c|^2Y^{1-2\Re s_0}/(1-2\Re s_0)>0$ throughout the strip; only the common $L^2$ word domain has the elementary obstruction. | Maass–Selberg coefficient and the distinction between smooth and $L^2$ data at a cusp. |
| L32 | Graph pushforward is exceptional also at $\pm\sqrt q$. | Eigenspace isomorphism fails generically only at $\pm1$; endpoints obstruct semisimplicity, not that isomorphism. | Explicit inverse $F_\mu$. |
| L33 | A single total graph/quantum pushforward gives a positive form on both branches. | Total pullback is degenerate; branchwise pullback or the companion metric is needed. | Partner lifts have the same vertex image. |
| L34 | Full Hashimoto HP iff closed sector Ramanujan. | Full algebraic-band HP iff strict sector band; closed band gives a divisor statement and may have Jordan blocks. | Exact graph and quantum endpoint counterexamples. |
| L35 | Quantum pushforward uses $\sum_i\operatorname{Ad}(U_i^*)x_i$. | In the notebook's source-letter convention use $\sum_i\operatorname{Ad}(U_i)x_i$. | $T=SR-J_0$ with the actual block convention. |
| L36 | Hermiticity alone, or reduced net Ramanujan, yields the claimed operator mechanism. | Need inverse-paired lift, actual sector bound and explicit retained spaces; generic graph symmetry is edge reversal, not a supplied permutation labelling. | D7 common identities, cancellations, and metric positivity. |
| L37 | K-type parity is a grading for the geodesic flow. | It makes $X$ odd, hence does not commute with the flow. | $H,E$ change K weight by two. |
| L38 | Full K-type parity equals Hodge form degree. | Hodge uses two weight-zero copies and weights $\pm2$; full K parity has all even weights and only one scalar copy. | Different vector spaces and multiplicities. |
| L39 | Two-jump K-type supertrace cancels every positive Laplace eigenvalue. | It has a nonzero theta factor on a spherical constituent; even selected Hodge bundles acquire a relative diffusion shift. | Formula (D8-counter) and $L_{\rm adj}=2\Omega+W^2/2$. |
| L40 | The doubled K-type candidate is therefore proved to have no Selberg net-odd divisor, while full transverse degree gives $Z_S$. | No such doubled-bond conclusion follows. K parity survives as a diffusion grading; full transverse degree gives Ruelle and the two-term complex gives Selberg. | D2, D5 and D8 distinguish the three constructions. |

## What is derived from the letters

### Labelled-input theorem: compact Selberg

**Theorem.** Give the compact quotient H-GEO and the following labelled inputs:

1. **[HAAR]** invariant Haar inner product and the closed-generator/Laplace realization H-AN/H-LAP;
2. **[SL2]** the three matrix letters and their brackets H-SL2;
3. **[ANALYSIS]** DFG's regular resonance spaces (`2075–2113`), first-band pushforward/Poisson isomorphism (`599–636,2456–2461`), ladder (`546–591`), and semisimplicity away from the specified exceptions (`357–375`);
4. **[TRACE]** the DZ flat trace and multiplicity theorem (`zeta.tex:489–526,1522–1620`) and Marklof's compact Selberg divisor (`selberg07.tex:2279–2351`);
5. **[BOUND, optional]** H-COERC, the $1/4$ coercivity;
6. **[ENDPOINT, for full operator HP]** H-NOEDGE.

Then [HAAR]+[SL2] give $\Delta\geq0$ as a sum of letter squares. Adding [ANALYSIS] gives the nonconstant first-band quadratic, reality, branchwise Haar form (D3-G), and the paired operator FE (D3-FE) off the threshold. Adding [TRACE] identifies the two-term transverse complex's ring zeta with $Z_S$, makes its surviving spectral divisor odd, and fixes all trivial multiplicities. [BOUND] is equivalent to (RH) and to (Ram) on the retained Selberg divisor; retained divisor (FE) already holds without it. With [ENDPOINT], [BOUND] additionally gives a positive manifest form on the complete algebraic retained odd first-band operator in its explicitly defined modal completion. Without [ENDPOINT], the divisor conclusion remains valid, but the full flow block at a threshold is not positively unitarizable.

**Proof.** D1 proves the letter sum of squares; D3 Steps 1–4 prove the quadratic and invoke exactly the Poisson bridge to make its Haar argument nonzero; D3 Steps 6–9 construct and qualify the form/FE; D2 proves the ring identity and divisor; D3 Step 5 proves the coercivity equivalence. None of [ANALYSIS], [TRACE], [BOUND], or [ENDPOINT] is asserted to follow from a list of abstract $\mathfrak{sl}_2$ matrices. The branch-orthogonal direct sum is part of the stated form construction. This is the precise meaning of “derived from the letters” supported by these proofs.

The retained odd sector is thus derived at the level of a **graded spectral transfer with regular resonance data**, with a constructive positive form under the sharp qualifications. A tensor-network Kraus realization and norm equivalence to the original anisotropic space are separate, unproved claims.

### Labelled-input theorem: finite graphs and quantum channels

**Theorem.** Give:

1. **[LETTERS]** graph incidence/reversal or homogeneous adjoint-paired unitary channel letters, with the counting/HS inner product;
2. **[LIFT]** the non-backtracking exclusion and source-letter convention defining $S,R,J_0,T$;
3. **[FINITE ANALYSIS]** the finite Hermitian spectral theorem (no resonance or Poisson theorem is needed);
4. **[BOUND, optional]** the sector Ramanujan bound, obtained separately by graph theory, Harrow containment, or a direct computation.

Then [LETTERS]+[LIFT] prove the identities (D7-data), Hermiticity of $\Sigma$, the pushforward (D7-push), the companion model and operator FE. They also give the explicit candidate metric (D7-G). [BOUND] puts all roots on the critical circle. Its strict version makes that metric positive on the entire retained algebraic band; endpoint Jordan blocks are the exact obstruction to replacing “strict” by “closed.” The construction is parity-even sector by sector; the odd surviving quadratics are zeros of the graded ring zeta. Cancellation is performed only for divisor assertions, never in the operator-form claim.

**Proof.** D7 Steps 1–7. The graph/quantum theorem is completely algebraic once the independently supplied bound is known. This is the finite counterpart of the compact theorem's separation between Haar reality, an analytic identification, and the extra $1/4$ inequality.

## Numerical checks

Only one script was written: [`finite/check_letters.py`](finite/check_letters.py). It is deterministic, runs from any directory, does not modify imported scripts, and disables bytecode writes. Existing PGL/principal-series and LPS helper functions are loaded by AST without executing their top-level experiments. Its full printed output is [`finite/check_letters.out`](finite/check_letters.out).

Command:

```bash
OPENBLAS_NUM_THREADS=1 python3 notes/selberg-letters/finite/check_letters.py
```

The checks comprise exact $\mathfrak{sl}_2$ brackets and ladder coefficients through level six; Casimir and FE sign checks; the singular naive first-band Gram matrix; compact integer divisor arithmetic for genera $2,3,5$; full/half transverse orbit weights; the negative CP-norm obstruction; the K-type theta counterexample; all retained root lifts and explicit metric/FE identities for the requested graph and quantum examples; graded Bass determinants; the Pauli reduced zeta and its six ring counts; and exact rational endpoint kernel computations.

| Example | Retained adjacency maximum | Bound | Largest tested lift residual / exact result |
|---|---:|---:|---|
| Petersen, degree 3 | $2$ | $2\sqrt2$ | $3.8\times10^{-15}$ |
| $K_4$, degree 3 | $1$ | $2\sqrt2$ | $1.9\times10^{-15}$ |
| $K_3\square Q_3$, degree 5 | $4$ | $4$ | exact Hashimoto nullities $2,4$ at $-2$ |
| Pauli, degree 6 | $2$ in both sectors | $2\sqrt5$ | counts $8,32,104,640,3208,15392$ |
| Ten-letter Pauli endpoint | even $2$, odd $6$ | $6$ | exact odd Hashimoto nullities $1,2$ at $3$ |
| PGL$_2(\mathbb F_5)$, LPS degree 14 graph | $4$ | $2\sqrt{13}$ | $3.0\times10^{-14}$ |
| PGL$_2(\mathbb F_5)$ principal series, even/odd dimensions $18,18$ | $4$ in both sectors | $2\sqrt{13}$ | $4.5\times10^{-14}$ |

The script prints:

```text
FINAL TALLY: 131 PASS / 0 FAIL
```

These are finite verification and counterexamples, not numerical evidence for a general Selberg gap or RH. All infinite-dimensional conclusions above use the declared analytic inputs.

**Final D-item tally: PROVED 0 / CORRECTED 7 (D1, D2, D3, D4, D5, D7, D8) / REFUTED 0 / OPEN 1 (D6).** The corrected items contain explicit refutations of their stronger subclaims; each D-item is counted once, according to its proved replacement or remaining essential open part.

## Post-review corrections (orchestrator, 2026-09-16, after the Opus REFUTE review)

The review `notes/reviews/selberg-letters-2026-09-16.md` (claude:opus-5) found no BLOCKER and no
MAJOR issue; round 1: seven items VALID, four MINOR (D3, D5, D6, LEDGER); round 2, after the fixes below: all VALID. The MINOR items are applied here without altering the
proofs above; the lab-book shards 03e/03f carry the corrected wording.

1. **D3 (MINOR 1).** The display $\lambda\in[-1,0]\cup(-\tfrac12+i\mathbb R)$ holds for
   $\lambda\notin-1-\mathbb N_0$, the range of H-DFG-POIS (Step 9 already shows $\pi_*u=0$ at
   $\lambda=-1$); the restriction is recorded here and stated with the display in shard 03e, thm:selberg-first-band-form (i); the display above is unchanged.
2. **D6 (MINOR 2).** "$Z_S$ has a zero of order $m$ at $\rho/2$": FJS item 6 gives the location;
   the order $m$ is inferred from the residues of $Z_S'/Z_S$ and $\phi'/\phi$ and is marked as an
   inference. The RH equivalence uses only the location.
3. **D5 (MINOR 3).** H-CP-NORM cites `04f_cmps_twisted_supertrace.tex:50-59`, whose lab-book status
   is `sketched-conditional`; only the sign of the cMPS ring norm is used.
4. **Ledger (MINOR 4).** Rows L04, L05, L06, L20, L23, L26 answer questions or instructions the
   draft had posed rather than correcting claims; their "true statement" columns stand. The
   remaining 34 rows are genuine corrections of the draft.
5. **D2 (MINOR 5).** The covector $\eta_+$ dual to $U_+$ annihilates $E_0\oplus E_u$ and lies in
   DFG's $E_u^*$; "stable" refers to DFG's naming of $U_+$.
6. **D3 headline (MINOR 6).** What the letters supply is the branch norms and the reality/line;
   given the line and semisimplicity, the existence of some positive form is the notebook's (HP)
   equivalence; the new content is the transported Haar form and the threshold obstruction.

H-MOD-GAP is now byte-checked: `refs/src/1803.06016/main.tex:121-122` (fetched by the reviewer;
registered as `cit:bls-selberg-level-one`).
