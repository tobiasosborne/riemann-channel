# Topic T, Fable lane: the tree of local GKP codes and the Ihara zeta as the zeta of the squeezes

> **Status (tidy 2026-10-28):** cross-family REFUTE-reviewed by codex:gpt-6-astra (`../review-astra-of-fable/astra-proofs.md`): 12 VALID / 7 MINOR / 6 INVALID. MINOR corrections applied below as marked annotations; INVALID items flagged in place. Not registered in db/. Not yet turned into a record page.

Author: `claude:fable-5.1`, 2026-10-27, blind of `tree-codes/astra/`. Brief: `notes/astra-2026-10-27/tree-codes/lane-brief.md` (binding,
with `notes/astra-2026-10-27/brief.md`). Steer respected: every statement below is a map or an identity between a lattice, a symplectic
form and a zeta function; no overlap is used. Checks: `checks/tree_codes.py` (T1, T3; output `checks/output_tree_codes.txt`),
`checks/mub.py` (T2; `checks/output_mub.txt`), `checks/ihara_lefschetz.py` (T4; `checks/output_ihara_lefschetz.txt`, and with `--big`
`checks/output_ihara_lefschetz_big.txt`). All exact arithmetic except the adjacency spectra (LAPACK, residuals printed).

Conventions of the brief §0 throughout: $V=\mathbb Q_p^2$, $\omega(x,y)=x_1y_2-x_2y_1$, $\psi_p(x)=e^{2\pi i\{x\}_p}$ (trivial exactly on
$\mathbb Z_p$), $W(u,v)f(x)=\psi_p(vx)f(x+u)$, $D_af(x)=|a|_p^{1/2}f(ax)$, $p$ odd. One convention of the brief is corrected at once
(ledger C1): the symmetric Weyl operator that is a representation on isotropic lattices is $\widetilde W(u,v)=\psi_p(+uv/2)\,W(u,v)$, not
$\psi_p(-uv/2)W(u,v)$. Summary of statuses: T1 PROVED (with one correction to the brief's wording), T2 PROVED, T3 PROVED, T4(a) PROVED
(Ihara, from memory, re-proved in the tree language), T4(b) PROVED as an exact trace identity with a corrected attribution of the operator,
T4(c) NUMERICAL on honest arithmetic quotients $\Gamma\backslash T_5$ (LPS graphs, 660, 2184 and 12180 vertices), T5 SKETCHED (one part PROVED).

---

## §1. T1 — colours are code dimensions. PROVED; the brief's "independent of the representative up to $D_c$" is false as worded (ledger C2)

**Lemma 1.1 (products of Weyl operators).** $W(u,v)W(u',v')=\psi_p(uv')\,W(u+u',v+v')$, hence
$W(\lambda)W(\lambda')=\psi_p(\omega(\lambda,\lambda'))\,W(\lambda')W(\lambda)$.
*Proof.* $W(u,v)W(u',v')f(x)=\psi_p(vx)\psi_p(v'(x+u))f(x+u+u')=\psi_p(uv')\psi_p((v+v')x)f(x+u+u')$. ∎

**Lemma 1.2 (phase convention, C1).** Put $\widetilde W_s(u,v)=\psi_p(s\,uv)W(u,v)$. Then
$\widetilde W_s(\lambda)\widetilde W_s(\lambda')=\psi_p\big(uv'-s(uv'+u'v)\big)\widetilde W_s(\lambda+\lambda')$, which equals
$\psi_p(\omega(\lambda,\lambda')/2)\widetilde W_s(\lambda+\lambda')$ iff $s=+\tfrac12$. With $s=+\tfrac12$, $\lambda\mapsto\widetilde W(\lambda)$ is a
genuine representation of every isotropic lattice $L$ ($\omega(L,L)\subset\mathbb Z_p$, $2\in\mathbb Z_p^\times$, so $\psi_p(\omega/2)=1$), and a
projective representation of $V$ with cocycle $\psi_p(\omega/2)$. With the brief's $s=-\tfrac12$ the phase is $\psi_p((3uv'+u'v)/2)$, not a
cocycle on $L$: e.g. $\widetilde W_{-1/2}(1,c/p)^2\neq\widetilde W_{-1/2}(2,2c/p)$. *Proof.* Lemma 1.1 and $\psi_p((u+u')(v+v')s)$. ∎
Checked: `output_tree_codes.txt` block T1' ($p=3,5$: True for $s=+1/2$, False for $s=-1/2$). The sign is invisible on $\mathbb Z_p^2$ (all
$uv\in\mathbb Z_p$) and matters exactly for the quadratic-phase bases of T2 (`output_mub.txt`, last line of each block: with the brief's sign the
$+1$ eigenvector of $\widetilde W(1,1/p)$ is $\psi_p(-(x-1)^2/2p)$, a translate, not $\psi_p(-x^2/2p)$). The brief's sign is the right one for the
other ordering $W'(u,v)f(x)=\psi_p(v(x+u))f(x+u)$.

**Proposition 1.3 (the dual lattice).** For $L=g\mathbb Z_p^2$, $g\in GL_2(\mathbb Q_p)$: $L^\perp=(\det g)^{-1}L$ and $[L^\perp:L]=p^{2v_p(\det g)}$
(a negative exponent meaning $[L:L^\perp]$).
*Proof.* $\omega(x,gy)=x^TJgy=(g^TJ^Tx)^Ty$ with $J=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$, so $x\in L^\perp$ iff
$g^TJ^Tx\in\mathbb Z_p^2$. For $2\times2$ matrices $g^TJg=(\det g)J$, so $g^TJ^T=-(\det g)Jg^{-1}$ and the condition reads
$g^{-1}x\in(\det g)^{-1}J^{-1}\mathbb Z_p^2=(\det g)^{-1}\mathbb Z_p^2$, i.e. $x\in(\det g)^{-1}L$. The index of $L$ in $c^{-1}L$ is $|c|_p^{-2}$. ∎
Checked on 18 random $g$ with entries in $p^{\pm2}\mathbb Z$ (`output_tree_codes.txt`, block T1: the two bases differ by a matrix in $GL_2(\mathbb Z_p)$).

**Proposition 1.4 (colours).** Write $k(L)=v_p(\det g)$ for $L=g\mathbb Z_p^2$. (i) $k(cL)=k(L)+2v_p(c)$, so the parity $k\bmod2$ is a function
of the vertex $[L]$; (ii) adjacent vertices have opposite parity; (iii) each vertex has a **unique** representative with $k\in\{0,1\}$, and it is
the unique isotropic representative of minimal index $[L^\perp:L]=p^{2k}$: $k=0$ self-dual (qunaught, code dimension $1$), $k=1$
($[L^\perp:L]=p^2$, one $p$-dimensional qudit). (iv) the representatives with $k<0$ are coisotropic ($L\supset L^\perp$) and have **no** code
(the $W(\lambda)$, $\lambda\in L$, do not commute).
*Proof.* (i) $\det(cg)=c^2\det g$. (ii) $pL\subset L'\subset L$ with $[L:L']=p$ gives $\det g'=p\cdot u\det g$, $u$ a unit. (iii) by (i) the
class contains exactly one $L$ with $k\in\{0,1\}$; $L\subset L^\perp$ iff $k\ge0$ by 1.3. (iv) Lemma 1.1. ∎ Checked (`T1` block: all $p+1$
neighbours of the $k=0$ and $k=1$ vertices have the other parity, $p=3,5,7$).

**Proposition 1.5 (the code of a split lattice; dimension).** For $L_{a,b}=p^a\mathbb Z_pe_1\oplus p^b\mathbb Z_pe_2$ in a symplectic basis
($\omega(e_1,e_2)=1$) with $a+b\ge0$, the code $\mathcal C_L=\{f:\widetilde W(\lambda)f=f\ \forall\lambda\in L\}$ is the space of functions supported
on $p^{-b}\mathbb Z_p$ and $p^a\mathbb Z_p$-periodic, of dimension $p^{a+b}=[L^\perp:L]^{1/2}$ (`adelic-gkp.md` Prop. 5, re-proved).
*Proof.* $\widetilde W(p^am,0)f(x)=f(x+p^am)$ and $\widetilde W(0,p^bn)f(x)=\psi_p(p^bnx)f(x)$; a general $\lambda=(p^am,p^bn)$ has
$\widetilde W(\lambda)=\psi_p(p^{a+b}mn/2)W(0,p^bn)W(p^am,0)=W(0,p^bn)W(p^am,0)$ since $p^{a+b}mn/2\in\mathbb Z_p$. So $f\in\mathcal C_L$ iff $f$ is
$p^a\mathbb Z_p$-periodic and supported where $\psi_p(p^bnx)=1$ for all $n$, i.e. on $p^{-b}\mathbb Z_p$. ∎ Every isotropic lattice is split in some
symplectic basis: $g=k\,\mathrm{diag}(p^a,p^b)$ with $k\in SL_2(\mathbb Z_p)$ after absorbing a unit into the first column (Smith form), so
$e_i=ke_i^0$. The code of a general isotropic $L$ is $\rho(k)\mathcal C_{L_{a,b}}$ for the Weil representation $\rho$ of $SL_2(\mathbb Q_p)$
(Weil 1964, from memory; for $p$ odd it is implemented on $L^2(\mathbb Q_p)$ by $D_a$, the shears $f\mapsto\psi_p(tx^2/2)f$ and the Fourier
transform), hence of the same dimension. Only split lattices are used numerically below.

**What the brief gets wrong (C2) and the corrected statement.** The brief asks "why the code is independent of the representative (up to a
canonical isomorphism / scaling by $D_c$)". It is **not** independent: $D_c$ implements $\mathrm{diag}(c^{-1},c)$ (brief §0), not the homothety
$\mathrm{diag}(c,c)$, and no unitary normalising the Weyl operators implements a homothety, because conjugation preserves the commutator
$\psi_p(\omega(\lambda,\lambda'))$ and so induces an element of $Sp(V)=SL_2(\mathbb Q_p)$, while $\mathrm{diag}(c,c)$ has multiplier $c^2\ne1$.
Concretely $\mathcal C_{pL}\supsetneq\mathcal C_L$ (fewer stabilisers: $\widetilde W(p\lambda)=\widetilde W(\lambda)^p$ on $L$) with
$\dim\mathcal C_{p^mL_0}=p^{k+2m}$. **Corrected statement (PROVED):** a vertex $[L]$ carries the nested tower of codes
$\mathcal C_{L_0}\subset\mathcal C_{pL_0}\subset\mathcal C_{p^2L_0}\subset\cdots$ of dimensions $p^k,p^{k+2},p^{k+4},\dots$, $L_0$ the unique
representative of Prop. 1.4(iii); "the code of the vertex" means $\mathcal C_{L_0}$. Two lattices $L,L'$ have unitarily equivalent codes through a
Clifford iff $L'=\sigma L$ with $\sigma\in SL_2(\mathbb Q_p)$, iff $k(L)=k(L')$ (the $SL_2(\mathbb Q_p)$-orbits of lattices are the level sets of
$k$, by the Smith form above). So all qunaught vertices have equivalent codes, all qudit vertices have equivalent codes, and the two colours are
not equivalent (dimensions $1$ and $p$). The tower $\mathcal C_{p^n\mathbb Z_p^2}$ of the base vertex is exactly the cutoff used in §4 (T4b).

*Review correction 2026-10-28 (astra review, VERDICT prop:tree-colours-code-dimension: MINOR; also VERDICT C2: MINOR):* scope. The nested tower, the strict inclusions and the homothety obstruction are proved; but "equivalent codes iff same colour" holds only for the minimal representatives $L_0$ (the $k\in\{0,1\}$ lattices) or for towers compared level by level. For arbitrary isotropic lattices the codes are Clifford-equivalent iff the determinant valuations $k(L)$ are equal (not merely congruent mod 2); counterexample: at $p=3$ levels 0 and 1 of the same even vertex have dimensions 1 and 9. The homotheties $c=\pm1$ are harmless exceptions to "no unitary normalising the Weyl operators implements a homothety" (a homothety with $c^2\ne1$ cannot preserve all commutators).

## §2. T2 — neighbours are MUB axes. PROVED

Fix the qudit vertex $M=p\mathbb Z_p\oplus\mathbb Z_p$ ($a=1,b=0$; this is the representative for which $\mathcal C_M$ is "functions on
$\mathbb Z_p/p\mathbb Z_p$", Prop. 1.5), $M^\perp=\mathbb Z_p\oplus p^{-1}\mathbb Z_p=p^{-1}M$ (Prop. 1.3 with $\det=p$).

**Proposition 2.1.** (i) The lattices $L$ with $M\subset L\subset M^\perp$ and $[L:M]=p$ are exactly the self-dual lattices between $M$ and
$M^\perp$, they are the $p+1$ lines of the symplectic $\mathbb F_p$-plane $M^\perp/M$ (every line of a symplectic plane is Lagrangian), and
$[L]$ runs over the $p+1$ neighbours of $[M]$. (ii) Dually the neighbours of a qunaught $[L]$ are the index-$p$ sublattices $M\subset L$, the lines of
$L/pL$, and $\mathcal C_L\subset\mathcal C_M$ for each, so $1_L\in\mathcal C_M$.
*Proof.* (i) $[L^\perp:L]=[M^\perp:M]/[L:M]^2=p^2/p^2=1$ (duality reverses inclusions and preserves indices). Since $M^\perp=p^{-1}M$,
scaling by $p$ turns $M\subset L\subset p^{-1}M$, $[L:M]=p$, into $pM\subset pL\subset M$, $[M:pL]=p$, the definition of adjacency. (ii)
$M\subset L$ means more stabilisers, so $\mathcal C_L\subset\mathcal C_M$. ∎

**Proposition 2.2 (the operators on $\mathcal C_M$).** For $u\in\mathbb Z_p$, $j\in\mathbb Z$, on $\mathcal C_M=\mathbb C^{\mathbb Z/p}$:
$\widetilde W(u,j/p)=\omega^{2^{-1}uj}Z^jX^u$ with $\omega=e^{2\pi i/p}$, $Xf(x)=f(x+1)$, $Zf(x)=\omega^xf(x)$, $2^{-1}$ the inverse of $2$ mod
$p$. *Proof.* $\psi_p(uj/2p)=\omega^{2^{-1}uj}$ and $\psi_p(jx/p)=\omega^{jx}$ on $\mathbb Z_p$. ∎ These are the standard symmetric
displacement operators of a qudit; $\widetilde W(M)$ acts as $1$ on $\mathcal C_M$ and $\widetilde W(M^\perp/M)$ is the Weyl–Heisenberg group of
$\mathbb F_p^2$ with the symplectic cocycle $\omega^{2^{-1}(uj'-u'j)}$ (checked on all $p^4$ pairs, `output_mub.txt`).

**Theorem 2.3 (MUBs).** Let $L_\infty=M+\mathbb Z_p(0,1/p)=p\mathbb Z_p\oplus p^{-1}\mathbb Z_p$ and $L_c=M+\mathbb Z_p(1,c/p)$, $c\in\mathbb F_p$.
(i) $\mathcal C_{L}\subset\mathcal C_M$ is one-dimensional, spanned by $b_{L_\infty}=\delta_0$ ($=1_{p\mathbb Z_p}$) and
$b_{L_c}(x)=p^{-1/2}\psi_p(-cx^2/2p)=p^{-1/2}\omega^{-2^{-1}cx^2}$ ($=\psi_p(-cx^2/2p)1_{\mathbb Z_p}$, the quadratic-phase vector; $c=0$ gives
$1_{\mathbb Z_p}$). (ii) The $p$ vectors $\widetilde W(\lambda)b_L$, $\lambda\in M^\perp/L\cong\mathbb F_p$, form an orthonormal basis $B_L$ of
$\mathcal C_M$: $B_{L_\infty}$ is the computational basis $\{\delta_x\}$ (eigenbasis of $Z$) and $B_{L_c}=\{Z^jb_{L_c}\}$ is the eigenbasis of
$Z^cX$. (iii) The $p+1$ bases are mutually unbiased: $|\langle b,b'\rangle|^2=1/p$ for $b\in B_L$, $b'\in B_{L'}$, $L\ne L'$. They are the standard
MUBs of the Weyl–Heisenberg group over $\mathbb F_p$ (Wootters–Fields 1989; Bandyopadhyay–Boykin–Roychowdhury–Vatan 2002, from memory).
*Proof.* (i) $\widetilde W(1,c/p)f(x)=\psi_p(c/2p)\psi_p(cx/p)f(x+1)$ and $\psi_p(c/2p+cx/p-c(x+1)^2/2p)=\psi_p(-cx^2/2p)$, so $b_{L_c}$ is fixed;
$\widetilde W(0,1/p)=Z$ fixes $\delta_0$; uniqueness because $\widetilde W(L)$ generates, with $\widetilde W(M)$, a maximal abelian subgroup whose
$+1$ eigenspace in the irreducible $p$-dimensional Weyl–Heisenberg representation is one-dimensional (or directly: the fixed space of $Z^cX$
is one-dimensional since $Z^cX$ has $p$ distinct eigenvalues). (ii) $\widetilde W(\lambda)$, $\lambda\in M^\perp$, commutes with $\widetilde W(L)$
up to $\psi_p(\omega)$ with $\omega(\lambda,L)\subset p^{-1}\mathbb Z_p$, and the $p$ characters $\psi_p(\omega(\lambda,\cdot))$ of $L/M$ are
distinct for distinct $\lambda\in M^\perp/L$, so the $\widetilde W(\lambda)b_L$ are eigenvectors of $\widetilde W(L)$ for distinct characters,
hence orthogonal. (iii) $|\langle Z^jb_{L_c},Z^{j'}b_{L_{c'}}\rangle|^2=p^{-2}|\sum_x\omega^{(j'-j)x-2^{-1}(c'-c)x^2}|^2=p^{-2}\cdot p=1/p$ for
$c\ne c'$ (a Gauss sum with invertible quadratic coefficient has modulus $\sqrt p$), and $|\langle\delta_x,Z^jb_{L_c}\rangle|^2=1/p$. ∎

**Numerical check** (`output_mub.txt`, $p=3,5,7$): all within-basis Gram matrices are the identity; over all pairs of distinct bases the
cross overlaps $|\langle b,b'\rangle|^2$ have min $=$ max $=1/p$ ($0.333333333333$, $0.200000000000$, $0.142857142857$); basis $\infty$ is the
computational basis up to order and basis $c$ is the quadratic phase $\psi_p(-cx^2/2p)$ shifted by $Z^j$, diagonalising $Z^cX$; $1_{\mathbb Z_p}$
lies in $\mathcal C_M$ and is fixed by $X=\widetilde W(1,0)$ (the dual statement). The stabiliser generators are printed, e.g. for $p=5$,
$\widetilde W(1,1/p)=\omega^{3}ZX$ ($2^{-1}=3$ mod 5).

**Reading.** A qudit vertex is a $p$-dimensional GKP code; its $p+1$ neighbours are the $p+1$ Lagrangian lines of the syndrome plane $M^\perp/M$,
i.e. its $p+1$ stabiliser axes, and walking along an edge is choosing one MUB. This is the exact form of `graph-ihara.md` §2(b) and of check H10
there (which only verified unbiasedness of the eigenbases of $XZ^t$; here the bases are derived from the lattices).

## §3. T3 — geodesics are pairs of transverse Lagrangians; translation is the squeeze. PROVED

**Proposition 3.1 (ends).** Rays from $[\mathbb Z_p^2]$ are in bijection with lines $\ell\in\mathbb P^1(\mathbb Q_p)$ (= Lagrangian subspaces of
$V$, every line being Lagrangian in dimension two) by $\ell\mapsto\big([L_n(\ell)]\big)_{n\ge0}$, $L_n(\ell)=(\ell\cap\mathbb Z_p^2)+p^n\mathbb Z_p^2$.
Hence the space of ends of $T_p$ is $\mathbb P^1(\mathbb Q_p)$ (Serre, *Trees*, II.1.1, from memory; $PGL_2(\mathbb Q_p)$-equivariantly).
*Proof.* Write $\ell\cap\mathbb Z_p^2=\mathbb Z_pe_1$ with $e_1$ primitive and complete to a basis $(e_1,e_2)$ of $\mathbb Z_p^2$. Then
$L_n=\mathbb Z_pe_1\oplus p^n\mathbb Z_pe_2$, $[L_n:L_{n+1}]=p$, and $L_{n+1}\not\supset pL_{n-1}\ni p^ne_2$: a ray. Conversely let
$\mathbb Z_p^2=L_0\supset L_1\supset\cdots$ be a ray. Inductively $\mathbb Z_p^2/L_n$ is cyclic of order $p^n$, $L_n=\mathbb Z_pe_1^{(n)}\oplus
p^n\mathbb Z_pe_2$: the $p+1$ index-$p$ sublattices of $L_n$ containing $pL_n$ are $pL_{n-1}$ (excluded: backtracking) and the $p$ lattices
$\mathbb Z_p(e_1^{(n)}+tp^ne_2)\oplus p^{n+1}\mathbb Z_pe_2$, $t\in\mathbb F_p$, each again with cyclic quotient. The $e_1^{(n)}$ converge
$p$-adically to a primitive $e_1$ and $L_n=L_n(\mathbb Q_pe_1)$. Distinct lines give distinct rays since $\ell\cap\mathbb Z_p^2$ mod $p^n$ is
recovered from $L_n$. Two rays from the same vertex are equivalent iff equal; by transitivity of $GL_2(\mathbb Q_p)$ on vertices every end is
represented by a ray from the base vertex. ∎

**Proposition 3.2 (geodesics are split lattices).** For $\ell_1\ne\ell_2$ choose $e_1\in\ell_1,e_2\in\ell_2$ with $\omega(e_1,e_2)=1$ (possible:
$\omega(e_1,e_2)\ne0$ since the lines are distinct). The vertices of the bi-infinite geodesic with ends $\ell_1,\ell_2$ are exactly the classes of
the lattices split by the pair, $L=(L\cap\ell_1)\oplus(L\cap\ell_2)=p^a\mathbb Z_pe_1\oplus p^b\mathbb Z_pe_2=L_{a,b}$, and $[L_{a,b}]$ depends on
$b-a$ only.
*Proof.* $[L_{a,b}]=[L_{0,b-a}]$ (homothety by $p^{-a}$). The classes $[L_{0,n}]$, $n\in\mathbb Z$, form a bi-infinite path without backtracking
(as in 3.1) whose two rays are $L_n(\ell_1)$ ($n\to+\infty$) and, after scaling, $L_n(\ell_2)$ ($n\to-\infty$); in a tree the geodesic between
two ends is unique, so its vertex set is $\{[L_{0,n}]\}$. A lattice is split by $(\ell_1,\ell_2)$ iff it has a basis $p^ae_1,p^be_2$ since
$L\cap\ell_i$ is a rank-one $\mathbb Z_p$-module. ∎

**Proposition 3.3 (the squeeze is the translation).** In the basis $(e_1,e_2)$, $\mathrm{diag}(a^{-1},a)$ with $v_p(a)=m$ maps $[L_{0,n}]$ to
$[L_{-m,n+m}]=[L_{0,n+2m}]$: translation by $2m$ along the geodesic, colour preserved, and no vertex fixed if $m\neq0$. $\mathrm{diag}(1,p)$ maps
$[L_{0,n}]$ to $[L_{0,n+1}]$: one step, colours exchanged. *Proof.* Direct; "no fixed vertex" is the tree fact that an automorphism with a
translation axis of length $\ell>0$ displaces every vertex $x$ by $\ell+2d(x,\text{axis})$ (Serre, *Trees*, I.6.4, Prop. 25, from memory). ∎
Checked: `output_tree_codes.txt` block T3' ($d([\mathbb Z_p^2],\mathrm{diag}(p^{-m},p^m)[\mathbb Z_p^2])=2m$ for $m=1,2,3$; one step and colour
change for $\mathrm{diag}(1,p)$; $p=3,5$).

**Theorem 3.4 (hyperbolic elements).** Let $\gamma\in GL_2(\mathbb Q_p)$ with $t=\operatorname{tr}\gamma$, $d=\det\gamma$ (its class in $PGL_2$ is what
acts). (i) The eigenvalues have distinct valuations iff $2v_p(t)<v_p(d)$; then both lie in $\mathbb Q_p$ with $v_p(\lambda_1)=v_p(t)$,
$v_p(\lambda_2)=v_p(d)-v_p(t)$, and $\gamma$ is conjugate in $PGL_2(\mathbb Q_p)$ (by an element of $SL_2(\mathbb Q_p)$) to $\mathrm{diag}(1,\lambda)$,
$\lambda=\lambda_2/\lambda_1$, with translation length $\ell(\gamma)=v_p(\lambda)=v_p(d)-2v_p(t)\ge1$ along the geodesic $(\ell_1,\ell_2)$ of its
two eigenlines (two transverse Lagrangians). (ii) Otherwise ($2v_p(t)\ge v_p(d)$) both eigenvalues have valuation $v_p(d)/2$ and $\gamma$ is
elliptic: it fixes a vertex if $v_p(d)$ is even and inverts an edge if $v_p(d)$ is odd. So for all $\gamma$,
$\ell(\gamma)=\max\big(v_p(\det\gamma)-2v_p(\operatorname{tr}\gamma),0\big)$, a function on $PGL_2$.
*Proof.* (i) Newton polygon of $x^2-tx+d$ with vertices $(0,v(d)),(1,v(t)),(2,0)$: $(1,v(t))$ lies strictly below the segment iff
$2v(t)<v(d)$, and then the polygon has two segments of length one with slopes $-v(t)$ and $-(v(d)-v(t))$; each segment of length one gives a
root in $\mathbb Q_p$ (Hensel: with $\lambda=p^{v(t)}\mu$, $\mu$ solves $\mu^2-(t/p^{v(t)})\mu+d/p^{2v(t)}=0$ whose reduction $\mu(\mu-\bar t')$ has
two simple roots; `hensel_root` in the script does exactly this lift). Distinct eigenvalues give a basis of eigenvectors $e_1\in\ell_1$, $e_2\in\ell_2$,
rescaled to $\omega(e_1,e_2)=1$, so the conjugating matrix is in $SL_2$ and $\gamma=\lambda_1\mathrm{diag}(1,\lambda)$ in that basis. By Prop. 3.3
with $\lambda=p^{\ell}u$: $[L_{0,n}]\mapsto[L_{0,n+\ell}]$, translation by $\ell$ on the geodesic of the eigenlines; this is the axis and $\ell$ the
translation length (Serre I.6.4). (ii) If $2v(t)\ge v(d)$ the polygon is one segment of slope $-v(d)/2$. Scale $\gamma$ so that $v(d)\in\{0,1\}$ and
$v(t)\ge0$: then $\gamma$ is integral over $\mathbb Z_p$ and $\Lambda=\mathbb Z_p[\gamma]\mathbb Z_p^2$ is a lattice with $\gamma\Lambda\subset\Lambda$;
if $v(d)=0$, $\gamma^{-1}=(t-\gamma)/d\in\mathbb Z_p[\gamma]$ so $\gamma\Lambda=\Lambda$: a fixed vertex. If $v(d)=1$, $\gamma$ changes colour, so it
fixes no vertex, and $\gamma^2/p$ has unit determinant and integral trace $(t^2-2d)/p$ (as $2v(t)\ge1$), hence fixes a vertex $x$; $\gamma$
then permutes the two vertices $x,\gamma x$ which are at distance $d(x,\gamma x)\equiv1$ mod 2 and, since $\gamma^2x=x$, at distance one: an
inversion. The formula for $\ell$ follows. ∎

*Review correction 2026-10-28 (astra review, VERDICT T3: MINOR):* proof of (ii), odd $v(d)$. The inference "$x,\gamma x$ at odd distance and $\gamma^2x=x$, hence at distance one" is false (old: distance one; new: $\gamma$ exchanges the endpoints of the odd-length segment $[x,\gamma x]$, so it inverts the central edge of that segment). Counterexample to the old step (recomputed 2026-10-28): $p=3,5$, $\gamma=\bigl(\begin{smallmatrix}0&1\\p&0\end{smallmatrix}\bigr)$, $\gamma^2=pI$, and $L=\mathrm{diag}(1,p^2)\mathbb Z_p^2$ has $d(L,\gamma L)=3$. The classification (fixed vertex iff $v(d)$ even, edge inversion iff odd) survives. The displayed $\ell(\gamma)=\max(v(\det)-2v(\operatorname{tr}),0)$ is the geometric (stable) translation length, allowing an edge midpoint; for an inversion the minimum vertex displacement is 1; the two notions coincide in the torsion-free, inversion-free $\Gamma$.
In the brief's $\Gamma$ (torsion-free, no inversions, free action) every nontrivial element is hyperbolic.

*Review correction 2026-10-28 (astra review, VERDICT C5: MINOR):* exclude the identity (an elliptic exception). In $\Gamma$ discreteness is essential: a nonidentity elliptic lies in a compact vertex stabiliser, whose intersection with the discrete $\Gamma$ is finite, so torsion-freeness removes it; inversions are excluded by hypothesis; the inversion step uses the central-edge argument of the annotation above.

**"Every hyperbolic element is a squeeze along its axis composed with a unit" — the precise form (ledger C4).** In the symplectic eigenbasis,
$\gamma\equiv\mathrm{diag}(1,p^\ell u)=\mathrm{diag}(1,p)^{\ell}\,\mathrm{diag}(1,u)$ in $PGL_2$, $u\in\mathbb Z_p^\times$. The unit factor
$\mathrm{diag}(1,u)$ fixes the axis pointwise. If $\ell=2m$ is even, $\mathrm{diag}(1,p)^{2m}\equiv\mathrm{diag}(p^{-m},p^m)$ is the symplectic
squeeze implemented by $D_{p^m}$ (translation $2m$). If $\ell$ is odd, $\mathrm{diag}(1,p)^\ell$ is **not** in the image of $SL_2(\mathbb Q_p)$ (a
similitude of multiplier $p$, exchanging colours): it is $D_{p^{(\ell-1)/2}}$ composed with the half-step $\mathrm{diag}(1,p)$, which no unitary
normalising the Weyl operators implements. So the brief's sentence is true verbatim for even $\ell$ and true for odd $\ell$ only with
"squeeze" read as $\mathrm{diag}(1,p)^\ell$ in $PGL_2$. (The unit $u$ is a square iff $\gamma$ lies in the image of $SL_2\cdot$scalars when
$\ell$ is even; this does not affect the tree.)

*Review 2026-10-28 (astra review, VERDICT prop:geodesic-squeeze: INVALID):* even translation length does not make $\gamma$ a symplectic squeeze over $\mathbb Q_p$: the $PGL_2$ class lifts to $SL_2(\mathbb Q_p)$ iff its determinant square class is trivial, equivalently iff the eigenvalue ratio $\lambda$ is a square. Example: $p=3$, $\gamma=\mathrm{diag}(1,18)$ has $\ell=2$ but unit part $2$, a nonsquare mod 3, so $\sqrt\lambda\notin\mathbb Q_3$. The candidate-row clause "a symplectic squeeze iff $\ell$ even" (and "true verbatim for even $\ell$" above) is therefore false as stated; the body notices the unit obstruction only in the parenthetical. Survives: ends $=\mathbb P^1(\mathbb Q_p)$, apartments, $\ell(\gamma)=\max(v(\det)-2v(\operatorname{tr}),0)$, and the decomposition above (replace the last clause by that decomposition; an $SL_2$ lift needs square determinant).

*Review correction 2026-10-28 (astra review, VERDICT T3: MINOR), second part:* distinguish the even translation factor from the determinant-square obstruction. For $\lambda=p^\ell u$: if $\ell=2m$ the translation factor alone is projectively $\mathrm{diag}(p^{-m},p^m)$ and $\gamma$ is this squeeze times the axis-fixing projective unit $\mathrm{diag}(1,u)$; if $\ell=2m+1$ it is that squeeze times $\mathrm{diag}(1,p)$ times the unit. These are identities of projective phase-space maps, not a product of two operators on one Hilbert space, and $\mathrm{diag}(1,p)$ is a similitude, so an odd step is not a Clifford. That $\gamma$ itself is a $\mathbb Q_p$ symplectic squeeze additionally needs the determinant square class trivial (above).

**Numerical check** (`output_tree_codes.txt`, block T3; $p=3,5$, ten random integer matrices each, entries in $[-12,12]$). For every matrix:
$v(\operatorname{tr})$, $v(\det)$, $\ell=\max(v(\det)-2v(\operatorname{tr}),0)$, and the tree distances $d(v,\gamma^kv)$, $k=1..5$, from the base vertex,
computed exactly from the elementary divisors of $\gamma^k$ (distance $=v(\det)-2\min v(\text{entries})$). Hyperbolic cases: $p=3$:
$\gamma=(8,5;9,0)$, $\ell=2$, distances $[2,4,6,8,10]$; $(-1,12;10,-6)$ and $(6,-11;12,4)$, $\ell=1$, distances $[1,2,3,4,5]$; $p=5$:
$(-2,-8;4,-4)$, $\ell=1$. In every hyperbolic case the increments equal $\ell$, the Hensel-lifted eigenvalues have $v(\lambda_2)-v(\lambda_1)=\ell$,
and among the $53$ ($p=3$) resp. $187$ ($p=5$) vertices within distance $3$ of the base, the $7$ with displacement $\ell$ (the axis through the base)
are exactly the $7$ lattices split by the eigenlines (split test: $L=(L\cap\ell_1)\oplus(L\cap\ell_2)$ iff the index of $p^a\mathbb Z_pe_1\oplus
p^b\mathbb Z_pe_2$ in $L$ is a unit, with $a,b$ read off from $B^{-1}e_i$). Elliptic cases have bounded orbits (distances $0$ or $[2,0,2,0,2]$).

## §4. T4 — the Ihara zeta of $\Gamma\backslash T_p$ is the zeta of the squeezes in $\Gamma$; orbit terms are local Lefschetz traces

Setting: $\Gamma\subset PGL_2(\mathbb Q_p)$ discrete, cocompact, torsion-free, without inversions; $Y=\Gamma\backslash T_p$ finite $(p+1)$-regular
($q=p$ below). The action is free (no fixed vertex: torsion-free + Thm 3.4(ii); no inversion), so $\Gamma\cong\pi_1(Y)$ and every $\gamma\ne1$ is
hyperbolic. $B$ the Hashimoto operator, $N_k=\operatorname{Tr}B^k$ = closed non-backtracking walks of length $k$ that are also non-backtracking at the
closing step (tailless), with a base point; $\zeta_Y(u)=\det(1-uB)^{-1}$.

### 4(a). Ihara's theorem in the tree language. PROVED (Ihara 1966, Serre *Trees* II.1.5; from memory, re-proved)

**Theorem 4.1.** (i) Closed tailless non-backtracking walks of length $k$ in $Y$ based at $y$ correspond bijectively to pairs $(\gamma,\tilde y)$ with
$\gamma\in\Gamma$ hyperbolic, $\ell(\gamma)=k$, $\tilde y$ a lift of $y$ lying on the axis of $\gamma$, modulo the diagonal $\Gamma$-action
$(\gamma,\tilde y)\mapsto(\delta\gamma\delta^{-1},\delta\tilde y)$. (ii) The centraliser $\Gamma_\gamma$ of a hyperbolic $\gamma$ is infinite cyclic,
generated by the primitive root $\gamma_0$ ($\gamma=\gamma_0^m$), and $\Gamma_\gamma\backslash\mathrm{Axis}(\gamma)$ has $\ell(\gamma_0)$ vertices. (iii)
Hence $N_k=\sum_{[\gamma]:\ \ell(\gamma)=k}\ell(\gamma_0)$, the sum over $\Gamma$-conjugacy classes of hyperbolic elements of translation length $k$,
each weighted by the length of its primitive root, and
$$\zeta_Y(u)=\prod_{[\gamma_0]\ \text{primitive hyperbolic}}\big(1-u^{\ell(\gamma_0)}\big)^{-1},$$
the Euler product over the primitive squeezes of $\Gamma$ (each oriented prime cycle once; $[\gamma_0]$ and $[\gamma_0^{-1}]$ are the two orientations).
*Proof.* (i) Lift the walk to a path in $T$ from $\tilde y$; it is non-backtracking, hence a geodesic segment of length $k$, ending at
$\gamma\tilde y$ for a unique $\gamma\in\Gamma$ (free action). The closing step being non-backtracking means the concatenation of the segment with
its $\gamma$-translate is again a geodesic, so the bi-infinite union $\bigcup_j\gamma^j(\text{segment})$ is a geodesic line translated by $\gamma$ by
$k$ steps: it is the axis and $\ell(\gamma)=k$ (an automorphism translating a line by $k>0$ has that line as its axis; Serre I.6.4). Conversely a
hyperbolic $\gamma$ and a vertex $\tilde y$ on its axis give the segment $[\tilde y,\gamma\tilde y]$, whose image is a closed tailless NB walk. Two
data give the same walk iff they differ by $\delta\in\Gamma$. (ii) The stabiliser of the axis in $\Gamma$ acts on it by translations (an element
reversing it would fix a vertex or an edge midpoint, excluded) and freely (an element fixing the axis pointwise is elliptic, hence trivial), so it is
infinite cyclic, generated by the element $\gamma_0$ of least translation length; it contains and centralises $\gamma$, and $\Gamma_\gamma$ preserves
the axis (the axis of $\delta\gamma\delta^{-1}=\gamma$ is $\delta\cdot\mathrm{Axis}(\gamma)$). The quotient of the axis by $\langle\gamma_0\rangle$ is a
cycle of $\ell(\gamma_0)$ vertices. (iii) Count the pairs of (i) modulo $\Gamma$: for each class $[\gamma]$ with $\ell(\gamma)=k$ there are
$\ell(\gamma_0)$ choices of $\tilde y$ modulo $\Gamma_\gamma$. Then $\log\zeta_Y(u)=\sum_kN_ku^k/k=\sum_{[\gamma_0]}\sum_{m\ge1}\ell_0u^{m\ell_0}/(m\ell_0)
=-\sum_{[\gamma_0]}\log(1-u^{\ell_0})$. ∎
By Theorem 3.4 each class $[\gamma_0]$ is a squeeze: in its symplectic eigenbasis $\gamma_0\equiv\mathrm{diag}(1,\lambda(\gamma_0))$ with
$v_p(\lambda(\gamma_0))=\ell_0$, so **the Ihara zeta is the Euler product over the primitive squeezes of $\Gamma$, with $u^{\ell_0}=u^{v_p(\lambda(\gamma_0))}$**:
the exponent is the valuation of the eigenvalue ratio, i.e. the $p$-adic size of the relative squeeze between the two Lagrangians of the axis.

### 4(b). The orbit term is a $p$-adic Lefschetz trace. PROVED, with the operator attribution corrected (ledger C3)

*Review 2026-10-28 (astra review, VERDICT T4b: INVALID):* bundled item. The finite compression theorem (Theorem 4.2) survives (VALID, `thm:code-trace-of-squeeze`); the bundled bipartite, phase-space and Connes identity-point claims do not (in-place lines below: after Theorem 4.2, after the consequence of Theorem 4.3, after "Which operator (C3)"). The status "PROVED" in this heading applies to Theorem 4.2 only.

**Theorem 4.2 (the distributional trace of the squeeze, exactly).** Let $\mathcal C_n=\mathcal C_{p^n\mathbb Z_p^2}$ be the GKP code of the lattice
$p^n\mathbb Z_p^2$ (functions supported on $p^{-n}\mathbb Z_p$ and $p^n\mathbb Z_p$-periodic; dimension $p^{2n}$; the $n$-th level of the tower of
§1 at the base vertex) and $P_n$ the orthogonal projector onto it. For $a\in\mathbb Q_p^\times$ and $n\ge0$,
$$\operatorname{Tr}(P_nD_aP_n)=|a|_p^{1/2}\,p^{\min(v_p(1-a),\,2n)}\qquad(\text{with }p^{\min(\infty,2n)}=p^{2n}\text{ at }a=1).$$
In particular for $a\ne1$ and $2n\ge v_p(1-a)$: $\operatorname{Tr}(P_nD_aP_n)=|a|_p^{1/2}/|1-a|_p$, the Lefschetz number of $x\mapsto ax$ at its
fixed point $0$ (the formal $\int|a|^{1/2}\delta((a-1)x)\,dx$ of the brief), independent of $n$; and at $a=1$ the trace is the volume $p^{2n}$
(Connes's $2h(1)\log\Lambda$ with $\Lambda=p^n$, `adelic-gkp.md` §10). So the "distributional trace" is literally the trace on the code tower.
*Proof.* Orthonormal basis $e_c=p^{n/2}1_{c+p^n\mathbb Z_p}$, $c\in p^{-n}\mathbb Z_p/p^n\mathbb Z_p$. Then
$\langle e_c,D_ae_c\rangle=p^n|a|^{1/2}\operatorname{vol}\big((c+p^n\mathbb Z_p)\cap a^{-1}(c+p^n\mathbb Z_p)\big)$. Case $|a|\le1$: $a^{-1}(c+p^n\mathbb Z_p)
=a^{-1}c+a^{-1}p^n\mathbb Z_p$ is a ball of radius $\ge$ that of $c+p^n\mathbb Z_p$, so the intersection is empty or the whole small ball (volume
$p^{-n}$), and it is nonempty iff $c-a^{-1}c\in a^{-1}p^n\mathbb Z_p$ iff $(a-1)c\in p^n\mathbb Z_p$ iff $c\in p^{\,n-r}\mathbb Z_p$, $r=v_p(1-a)$.
The number of such $c$ in $p^{-n}\mathbb Z_p/p^n\mathbb Z_p$ is $p^{\min(r,2n)}$, each contributing $p^n|a|^{1/2}p^{-n}=|a|^{1/2}$. Case $|a|>1$:
$D_a^*=D_{a^{-1}}$ and $P_n$ is self-adjoint, so $\operatorname{Tr}(P_nD_aP_n)=\overline{\operatorname{Tr}(P_nD_{a^{-1}}P_n)}=|a|^{-1/2}p^{\min(v(1-a^{-1}),2n)}$,
and $v(1-a^{-1})=v(a-1)-v(a)$, $|a|^{-1/2}p^{-v(a)}=|a|^{1/2}$. ∎
Checked exactly (`output_ihara_lefschetz.txt`, block T4(b), $p=5$, $n=0..3$): e.g. $a=5,25,125$: $0.44721,0.20000,0.08944=5^{-1/2},5^{-1},5^{-3/2}$ at
every $n$; $a=1/5$: $0.44721$; $a=126$ ($v(1-a)=3$): $1,25,125,125$ for $n=0,1,2,3$ (stabilising once $2n\ge3$); $a=-4$: $5$; $a=1$: $1,25,625,15625$.

*Review correction 2026-10-28 (astra review, VERDICT C7: MINOR):* Theorem 4.2 is an identity of traces of the compression $C_n(a)=P_nD_aP_n|_{\mathcal C_n}$, not of a restriction of $D_a$ ($\mathcal C_n$ is not $D_a$-invariant for nonunit $a$). The flat trace $|a|^{1/2}/|1-a|$ at $a\ne1$ is well defined, distinct from an ordinary operator trace; the non-Hilbert–Schmidt statement of ledger C7 excludes the zero average of $h$.

*Review 2026-10-28 (astra review, VERDICT T4b: INVALID, identity-point part):* the claim "at $a=1$ the trace is the volume $p^{2n}$ (Connes's $2h(1)\log\Lambda$ with $\Lambda=p^n$)" fails: $\operatorname{Tr}C_n(1)=p^{2n}$ is a rank, not $2h(1)\log\Lambda$ (at $p=5,n=1$: $25$ versus $2\log5=3.2189$, recomputed); a point value of a singular trace kernel is not the divergence of its integral. Survives (review's repair): with $\operatorname{vol}(\mathbb Z_p^\times)=1$, $\int_{\mathbb Z_p^\times}\operatorname{Tr}C_n(a)\,d^\times a=2n+1$ (the annulus $v(1-a)=r\ge1$ has measure $p^{-r}$ and trace $p^{\min(r,2n)}$; re-summed for $p=3,5$, $n=0..3$: $1,3,5,7$; equivalently a Burnside count of valuation orbits on $\mathbb Z/p^{2n}$); with $\operatorname{vol}(\mathbb Z_p^\times)=\log p$ it is $(2n+1)\log p$. The logarithm comes from integrating the cutoff kernel near the identity; this is a local computation, not a proof of Connes's global trace formula.

**Theorem 4.3 (the orbit identity).** For hyperbolic $\gamma\in PGL_2(\mathbb Q_p)$ let $\lambda(\gamma)=\lambda_2/\lambda_1$ be its eigenvalue ratio
(well defined up to inversion, $v_p(\lambda)=\ell(\gamma)$ by Thm 3.4) and $g_\gamma=\gamma/\sqrt{\det\gamma}$ its $SL_2$-normalisation (in
$SL_2(\mathbb Q_p(\sqrt{\det\gamma}))$; unique up to sign). Then
$$p^{-\ell(\gamma)/2}\;=\;\frac{|\lambda(\gamma)|_p^{1/2}}{|1-\lambda(\gamma)|_p}\;=\;\operatorname{Tr}\big(P_nD_{\lambda(\gamma)^{\pm1}}P_n\big)\ (\forall n\ge0)
\;=\;\frac{1}{|\det(1-g_\gamma)|_p}\;=\;\frac{|\det\gamma|_p^{1/2}}{|\operatorname{tr}\gamma|_p}.$$
*Proof.* $v(\lambda)=\ell\ge1$ gives $|1-\lambda|=1$ and $|\lambda|^{1/2}=p^{-\ell/2}$; Thm 4.2 with $v(1-\lambda)=0$ (and $v(1-\lambda^{-1})=-\ell$, both
below $2n$ for every $n\ge0$). $\det(1-g_\gamma)=2-\operatorname{tr}\gamma/\sqrt{\det\gamma}$, and $|\operatorname{tr}\gamma/\sqrt{\det\gamma}|=p^{\ell/2}>1\ge|2|$,
so $|\det(1-g_\gamma)|=|\operatorname{tr}\gamma|/|\det\gamma|^{1/2}=p^{-v(\operatorname{tr})+v(\det)/2}=p^{\ell/2}$. ∎
Consequently, with Theorem 4.1 and the explicit formula of `graph-ihara.md` §5 (re-derived below in 4(c) from Ihara–Bass for arbitrary
regular graphs, bipartite included):
$$\sum_{\text{non-trivial lines}}w^k\;=\;\sum_{[\gamma_0]}\sum_{m\ge1:\ m\ell(\gamma_0)=k}\ell(\gamma_0)\cdot\operatorname{Tr}_{\mathcal C_n}\!\big(D_{\lambda(\gamma_0)^m}\big)
\;-\;n(q-1)q^{-k/2}[k\text{ even}]\;-\;(q^{k/2}+q^{-k/2}),$$
**the orbit side is the sum over primitive hyperbolic classes of (length of the primitive element) × ($p$-adic Lefschetz trace of the squeeze by
the eigenvalue ratio of $\gamma_0^m$)**, where $\ell(\gamma_0)=\#\big(\Gamma_\gamma\backslash\mathrm{Axis}\big)$ is the volume of the centraliser
quotient (Thm 4.1(ii)), and $\lambda(\gamma_0^m)=\lambda(\gamma_0)^m$. Each term is a trace on a fixed finite-dimensional GKP code $\mathcal C_n$
(any $n\ge0$); nothing distributional remains.

*Review 2026-10-28 (astra review, VERDICT thm:ihara-zeta-squeeze-lefschetz: INVALID):* the displayed identity omits the bipartite alternating pair although it is stated for bipartite graphs too, and $\operatorname{Tr}_{\mathcal C_n}D_a$ must read $\operatorname{Tr}C_n(a)$, a compression trace, not an action on $\mathcal C_n$ ($D_a$ does not preserve $\mathcal C_n$: $D_p1_{\mathbb Z_p}=p^{-1/2}1_{p^{-1}\mathbb Z_p}\notin\mathcal C_0$; $C_0(p)C_0(p^{-1})=p^{-1}I\ne I=C_0(1)$). "Nothing distributional remains" holds only in this compression sense; no determinant formula $\zeta_Y=\det(1-uC_n)^{-1}$ and no common representation of $\Gamma$ follows. Corrected identity (review §5.4, from Ihara–Bass, no Ramanujan assumption; $N=|V(Y)|$, $\epsilon=1$ if $Y$ is bipartite and $0$ otherwise, both trivial adjacency eigenvalues $\pm(q+1)$ removed): $\sum_{\text{nontrivial}}w^k=\sum_{[\gamma_0],m:\ m\ell_0=k}\ell_0\operatorname{Tr}C_n(\lambda(\gamma_0)^m)-N(q-1)q^{-k/2}[k\ \text{even}]-(1+\epsilon(-1)^k)(q^{k/2}+q^{-k/2})$. For $X^{5,13}$ the printed display fails at $k=1$ (right side $-(\sqrt5+1/\sqrt5)=-2.683281573$, left side $0$ by symmetry of the spectrum) and at $k=8$ (error $625.0016=5^4+5^{-4}$); §4(c) and the scripts already use the corrected form. Survives: Theorem 4.1, the orbit term itself, and Theorem 4.2. Also, the two code colours descend to $\Gamma\backslash T$ only when $\Gamma$ preserves colour (bipartite quotient): the length-7 elements of $X^{5,11}$ exchange colours (minimal dimensions $1$ and $p$), so the local code dictionary does not define a Clifford action of $\Gamma$ on one family of minimal codes over a non-bipartite quotient.

**Which operator (C3).** The brief says "the squeeze part of $\gamma\sim\mathrm{diag}(1,\lambda)$ is $D_{\lambda^{\pm1}}$". The number is right, the
operator is not: $D_\lambda$ implements $\mathrm{diag}(\lambda^{-1},\lambda)\equiv\mathrm{diag}(1,\lambda^2)$, which translates the axis by
$2\ell(\gamma)$, i.e. $D_{\lambda(\gamma)}$ is the Weil-representation image of $\gamma^2/\det\gamma\in SL_2(\mathbb Q_p)$ (exactly:
$\mathrm{diag}(\lambda_1,\lambda_2)^2/\lambda_1\lambda_2=\mathrm{diag}(\lambda^{-1},\lambda)$), not of $\gamma$. The squeeze that implements $\gamma$
itself on the tree (even $\ell$) is $D_{\sqrt\lambda}$, whose trace is $p^{-\ell/4}$, the wrong weight. Two equivalent correct readings of
Theorem 4.3: (1) on $L^2(\mathbb Q_p)$ the weight is the trace of the squeeze by the **eigenvalue ratio**, the relative squeeze of the two
Lagrangians of the axis ($\lambda=d\gamma$ at the fixed point $\ell_1\in\mathbb P^1(\mathbb Q_p)$, since $T_{\ell_1}\mathbb P^1=\operatorname{Hom}(\ell_1,V/\ell_1)
=\ell_1^*\otimes\ell_2$); (2) on functions on the **phase space** $V$ the weight is the Lefschetz number $1/|\det(1-g_\gamma)|_p$ of the symplectic
map $g_\gamma$ at its unique fixed point $0$, and for even $\ell$ this is proved by the same cutoff argument as Thm 4.2 applied in the eigenbasis
(product of the two one-dimensional traces $1/|1-\mu^{\mp1}|$ with $\mu^2=\lambda$: $|\mu|\cdot1=p^{-\ell/2}$). Reading (2) is the one with
"$\gamma$ is a squeeze of $(V,\omega)$" verbatim; reading (1) matches Connes's local term. For the boundary: the unitary principal series at
$s=\tfrac12$, $\pi(\gamma)f(z)=|d(\gamma^{-1}z)/dz|^{1/2}f(\gamma^{-1}z)$ on $L^2(\mathbb P^1(\mathbb Q_p))$, has flat trace
$\sum_{\text{fixed }z}|\gamma'(z)|^{1/2}/|1-\gamma'(z)|=|\lambda|^{1/2}/|1-\lambda|+|\lambda|^{-1/2}/|1-\lambda^{-1}|=2p^{-\ell/2}$: each of the two
transverse Lagrangians of the axis contributes one orbit weight (PROVED as a computation; used in §5).

*Review 2026-10-28 (astra review, VERDICT C3: INVALID):* correct: $\gamma^2/\det\gamma=\mathrm{diag}(\lambda^{-1},\lambda)$ in an eigenbasis (with $D_\lambda$ the chosen intertwiner; for general $\gamma$ a metaplectic lift/phase convention is needed, "the Weil image" is too strong) and the numerical identity of Theorem 4.3. Fails: (a) a fixed finite cutoff is not conjugacy invariant: conjugating by the shear $Q_tf=\psi_p(tx^2/2)f$, $t=1/p$, keeps $\lambda=p$ but $\operatorname{Tr}(P_0Q_tD_pQ_t^{-1}P_0)=p^{-1/2}\int_{\mathbb Z_p}\psi_p((1-p^2)x^2/2p)\,dx$, which is $-1/5$ at $p=5$ (recomputed from the Gauss sum) versus $\operatorname{Tr}(P_0D_5P_0)=1/\sqrt5$; the all-$n$ formula holds for the standardised ratio dilation or a cutoff transported with the eigenbasis. (b) Reading (2), the $\mathbb Q_p$ phase-space Lefschetz number, needs $\det\gamma$ a $\mathbb Q_p$-square; "even $\ell$" does not suffice ($\mathrm{diag}(1,18)$, $p=3$) and for odd $\ell$ $g_\gamma$ is not $\mathbb Q_p$-linear; over $K=\mathbb Q_p(\sqrt p)$ the Haar Jacobian is $|N_{K/\mathbb Q_p}\det(1-g_\gamma)|_p$ and the $K$-phase-space fixed-point trace is $p^{-\ell}$, not $p^{-\ell/2}$ (the equality $1/|\det(1-g_\gamma)|=p^{-\ell/2}$ stays a valid numerical equality over the extension). (c) $\gamma\mapsto\gamma^2/\det\gamma$ is not a homomorphism, and an "Euler product of the $D_\lambda$ with their own tree lengths" would give $\zeta_Y(u^2)$; the correct factor stays $(1-u^{\ell})^{-1}$, indexed by the original primitive $\gamma$.

**Normalisation against Connes's local term (brief's question).** For $\zeta$ the prime side of Weil's explicit formula carries, at $t=\pm k\log p$,
the weight $\log p\cdot p^{-k/2}$ (record convention, `adelic-gkp.md` §10: $\operatorname{Loc}=\sum_vW_v$, $W_p(h)=\sum_{k\ne0}\log p\,p^{-|k|/2}h(p^k)$ in the
unitary normalisation $\mathrm{Re}\,s=\tfrac12$). The dictionary that makes the two formulas one formula is:

| | $\zeta$ at $p$ (Connes) | graph $Y=\Gamma\backslash T_p$ |
|---|---|---|
| primitive orbit, its length | the closed orbit of the squeeze flow at $p$, period $\log p$ | the primitive class $[\gamma_0]$, $\ell(\gamma_0)$ (volume of $\Gamma_\gamma\backslash\langle\gamma\rangle$) |
| its $m$-th iterate | $a=p^{m}$ (or $p^{-m}$: both orientations) | $\gamma_0^{m}$, eigenvalue ratio $\lambda(\gamma_0)^m$ ($\gamma_0^{-m}$: the other orientation) |
| time of the kick | $t=m\log p$, unit $\log p$ | $k=m\ell(\gamma_0)$, unit $1=\log q$ in the record's $t=k\log q$ |
| weight | $\log p\cdot\operatorname{Tr}_{\mathcal C_n}D_{p^m}=\log p\cdot p^{-m/2}$ | $\ell(\gamma_0)\cdot\operatorname{Tr}_{\mathcal C_n}D_{\lambda(\gamma_0)^m}=\ell(\gamma_0)\,p^{-m\ell(\gamma_0)/2}$ |
| sign | $-$ (dark: $\sum_\rho\hat h(\rho)=\hat h(0)+\hat h(1)-\operatorname{Loc}$) | $+$ (bright: $\sum w^k=q^{-k/2}N_k-\ldots$) |

With the unit of time chosen as the length of one tree step ($\log q$) the two weights are the same function of (length of the primitive orbit,
Lefschetz trace of the iterate): the only normalisation choices are (i) the measure on the squeeze group, $d^\times a$ with the primitive orbit of
measure $\log p$ for $\zeta$ and $\ell(\gamma_0)$ vertices for the graph, and (ii) the unitary normalisation $|a|^{1/2}$ of $D_a$ (the
$\mathrm{Re}\,s=\tfrac12$ axis), which is what makes the trace $p^{-m/2}$ rather than $1/|1-a|$. **Where the sign enters.** $N_k=\operatorname{Tr}B^k$ is an
honest trace on $\ell^2(\text{oriented edges})$, so the lines $w$ (eigenvalues of $S=M/\sqrt q$, the step on the label phase space) are emitted
and the orbit sum carries $+$; the trivial pair $q^{\pm k/2}$ is then subtracted. For $\zeta$ the orbit terms are the trace of the squeeze on the
code complement (Connes), and the zeros appear with the opposite sign relative to the pole pair ($\hat h(0)+\hat h(1)$): a supertrace, the
record's "dark lines" (`graph-ihara.md` §5, `cor:curve-counts-graded`). The relative sign between the orbit sum and the trivial/pole pair is the
same ($-$) in both columns; the overall sign flips. This lane adds no new mechanism for the flip; it fixes the normalisation so that the flip is the
only difference.

### 4(c). Honest arithmetic quotients $\Gamma\backslash T_5$: the LPS graphs. NUMERICAL (identity verified to $10^{-11}$)

Construction (`checks/ihara_lefschetz.py`; Lubotzky–Phillips–Sarnak, *Ramanujan graphs*, Combinatorica 1988, from memory): the six integer
quaternions $1\pm2i,1\pm2j,1\pm2k$ of norm $5$ generate the free group $\Lambda(2)$ of quaternions $\equiv1$ mod 2 of norm $5^k$ modulo $\pm5^k$,
which embeds in $PGL_2(\mathbb Q_5)$ as a cocompact torsion-free lattice acting simply transitively on the vertices of $T_5$; the Cayley graph
$X^{5,q}$ of its image in $PGL_2(\mathbb F_q)$ (through a splitting $i\mapsto\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$,
$j\mapsto\bigl(\begin{smallmatrix}x&y\\y&-x\end{smallmatrix}\bigr)$, $x^2+y^2\equiv-1$) is $\Gamma\backslash T_5$ for the congruence subgroup
$\Gamma=\Lambda(2q)$; it is the Cayley graph of $PSL_2(\mathbb F_q)$ (non-bipartite) when $(5/q)=1$ and of $PGL_2(\mathbb F_q)$ (bipartite) when
$(5/q)=-1$. Note (ledger C6): the brief's suggested $q=13$ gives $(5/13)=-1$, **bipartite**, so the brief's non-bipartite formula needs the
alternating pair $w=-q^{\pm1/2}$ added; $q=11$ and $q=29$ are the non-bipartite cases. The scripts verify: 6-regular simple graphs, vertex
counts $660=|PSL_2(\mathbb F_{11})|$, $2184=|PGL_2(\mathbb F_{13})|$, $12180=|PSL_2(\mathbb F_{29})|$, Ramanujan (largest non-trivial $|\lambda|$:
$4.372281$, $4.249721$ against $2\sqrt5=4.472136$).

(i) $N_k$ for $k\le8$ by enumeration of cyclically reduced words $s_1\cdots s_k$ in the six generators with product $1$ (left multiplication is simply
transitive on vertices, so $N_k=|G|\times$ the number of such words at the identity); for $q=11$ independently by dense powers of the $3960\times3960$
Hashimoto matrix: differences $[0,0,0,0,0,0,0,0]$.
(ii) $N_k$ from Ihara–Bass through the adjacency spectrum, $N_k=n(q-1)[k\text{ even}]+\sum_\lambda(\mu_\lambda^k+\bar\mu_\lambda^k)$ ($\mu+\bar\mu=\lambda$,
$\mu\bar\mu=q$; from $\det(1-uB)=(1-u^2)^{n(q-1)/2}\prod_\lambda(1-\lambda u+qu^2)$), and the primitive classes $\pi(\ell)=\frac1\ell\sum_{d|\ell}\mu(\ell/d)N_d$:

| graph | girth | $N_6$ | $N_7$ | $N_8$ | $\pi(6)$ | $\pi(7)$ | $\pi(8)$ | max $|N_k^{\rm words}-N_k^{\rm IB}|$ |
|---|---|---|---|---|---|---|---|---|
| $X^{5,11}$, $n=660$ | 6 | 3960 | 110880 | 475200 | 660 | 15840 | 59400 | $7.5\cdot10^{-9}$ |
| $X^{5,13}$, $n=2184$ | 8 | 0 | 0 | 1048320 | 0 | 0 | 131040 | $2.9\cdot10^{-8}$ |
| $X^{5,29}$, $n=12180$ | $>8$ | 0 | 0 | 0 | 0 | 0 | 0 | $7.2\cdot10^{-8}$ |

(iii) The explicit formula with the orbit weights of Theorem 4.3, $\sum_{\text{non-trivial}}w^k=q^{-k/2}\sum_{\ell|k}\ell\,\pi(\ell)-n(q-1)q^{-k/2}[k\text{ even}]
-(q^{k/2}+q^{-k/2})-[\text{bip}](-1)^k(q^{k/2}+q^{-k/2})$, against the LAPACK spectrum: max residual over $k\le8$ is $3.41\cdot10^{-12}$ ($q=11$) and
$1.00\cdot10^{-11}$ ($q=13$), and $2.67\cdot10^{-10}$ for $X^{5,29}$ ($12180$ vertices, non-bipartite, largest non-trivial $|\lambda|=4.442016$;
its girth exceeds 8, consistent with the LPS bound $\ge2\log_5n\approx11.7$, so at $k\le8$ the identity there tests the spectrum against the
tree term and the trivial pair only; `output_ihara_lefschetz_big.txt`, 964 s).

*Review correction 2026-10-28 (astra review, VERDICT T4c: MINOR):* the incidental girth bound for $X^{5,29}$ is false. Old: "its girth exceeds 8, consistent with the LPS bound $\ge2\log_5n\approx11.7$"; new: $\operatorname{girth}(X^{5,29})=9$ ($N_9=2630880$, $\pi(9)=292320$; 216 tailless identity words of length 9 at a fixed vertex, e.g. the quaternion $(549,-58,-406,1218)$ of norm $5^9$). Delete the claimed lower bound; "girth $>8$" and all printed tables stand. (Recomputed 2026-10-28: $12180\cdot216=2630880$, $2630880/9=292320$, $549^2+58^2+406^2+1218^2=5^9$; the existence of the words and vanishing of $N_k$, $k\le8$, are the review's computation, not re-run here.)
(a)/(b) on the lattice itself ($q=11$): for every closed tailless word the quaternion product $\alpha$ (norm $5^k$) is an element of $\Gamma$, and as a
$5$-adic matrix $\bigl(\begin{smallmatrix}a+bi&c+di\\-c+di&a-bi\end{smallmatrix}\bigr)$ ($i=\sqrt{-1}\in\mathbb Z_5$) its translation length
$\ell(\gamma)=v_5(\det)-2v_5(\operatorname{tr})=k-2v_5(2a)$ equals $k$ for **all** 6, 168, 720 tailless closed words of length 6, 7, 8 (so
$v_5(\lambda(\gamma))=k$ and the weight is $5^{-k/2}$: $0.008000$, $0.003578$, $0.001600$), while the 24 closed reduced words of length 8 **with** a
tail all have $\ell(\gamma)=6$ (their element is conjugate to a length-6 cycle: Theorem 4.1(i) in action). Example: the word $(5,5,5,5,5,5)$
(the generator $1-2k$ six times) gives $\alpha=117-44k$, $\operatorname{tr}=234$, $\det=5^6$, $\ell=6$: the cycle of length 6 is the squeeze with
eigenvalue ratio of valuation 6.

## §5. T5 — $\Omega$ on the $\lambda$-eigenplane as a boundary pairing. SKETCHED (two parts PROVED, the intertwiner identification OPEN)

**5.1 (PROVED, elementary).** For the record's step $M=\bigl(\begin{smallmatrix}0&-1\\q&\lambda\end{smallmatrix}\bigr)$ on one mode (`graph-ihara.md`
§4; the 2026-10-23 convention $\bigl(\begin{smallmatrix}A&-q\\1&0\end{smallmatrix}\bigr)$ is its transpose-conjugate and gives the same numbers), the
eigenvectors are $v_\mu=(1,-\mu)$ with $\mu^2-\lambda\mu+q=0$, and $\Omega(v_\mu,v_{q/\mu})=\mu-q/\mu=\sqrt q\,(w-w^{-1})$, $w=\mu/\sqrt q$. This is
the Casoratian $(f_{k+1}g_k-f_kg_{k+1})/q^k$ of the two solutions $f_k=\mu^k$, $g_k=(q/\mu)^k$ of $f_{k+2}=\lambda f_{k+1}-qf_k$, constant in $k$ by Abel's
formula ($M^T\Omega M=q\Omega$), and $\Omega(v_\mu,v_{q/\mu})^2=\lambda^2-4q=-4\det\mathcal Q|_{\text{plane}}$: the Casoratian of the two Satake modes is
the square root of minus the discriminant of the Weil form $\mathcal Q=\tfrac12\Omega(M-V)=\bigl(\begin{smallmatrix}q&\lambda/2\\\lambda/2&1\end{smallmatrix}\bigr)$
on that plane; it is purely imaginary exactly in the Ramanujan band, where $\mathcal Q>0$ (tutorial §6, `graph-ihara.md` §6: unchanged).

*Review correction 2026-10-28 (astra review, VERDICT T5: INVALID; this part survives with two endpoint corrections):* $\mathcal Q$ is positive definite only in the open band $|\lambda|<2\sqrt q$ (at the endpoints it has rank one, the two eigenvectors coincide and the pairing vanishes); the square root is of the discriminant $\lambda^2-4q$, not of its negative (review §7.1; the identity $\Omega(v_\mu,v_{q/\mu})^2=\lambda^2-4q=-4\det\mathcal Q$ itself is verified).

**5.2 (PROVED, a computation; from 4(b)).** On the boundary $\mathbb P^1(\mathbb Q_p)=$ the Lagrangian Grassmannian of $(V,\omega)$, the unitary
principal series $\pi_s(\gamma)f(z)=|(\gamma^{-1})'(z)|^{s}f(\gamma^{-1}z)$ has, for hyperbolic $\gamma$ with eigenvalue ratio $\lambda$ ($v_p(\lambda)=\ell$),
flat trace $|\lambda|^{s}/|1-\lambda|+|\lambda|^{-s}/|1-\lambda^{-1}|=p^{-\ell s}+p^{-\ell(1-s)}$; with the normalisation
$\mu=p^{1-s}$ (so $|\mu|=\sqrt p$ iff $\mathrm{Re}\,s=\tfrac12$), $p^{-\ell(1-s)}=p^{-\ell}\mu^{\ell}$ and $p^{-\ell s}=p^{-\ell}(p/\mu)^{\ell}$, the two fixed Lagrangians of the axis
contribute the two Satake parameters $\mu^{\ell},(p/\mu)^{\ell}$ (times $p^{-\ell}$). So the pair $\{\mu,p/\mu\}$ of the label phase space is, on the
boundary, the pair of fixed points of the squeeze, and the symmetric point $s=\tfrac12$ ($|\mu|=\sqrt p$) is where both contribute equally, $2p^{-\ell/2}$.
This fixes the normalisation the brief left open: $\mu=p^{1-s}$, $\lambda=\mu+p/\mu=p^{1-s}+p^{s}$ is the eigenvalue of the adjacency operator
on the Poisson transform $P_s\phi(x)=\int_{\mathbb P^1}P(x,z)^{s}\phi(z)\,dz$ of a boundary function (standard: Cartier 1972, Figà-Talamanca–Nebbia 1991,
from memory; the radial Poisson kernel $P(x,z)=p^{-h(x,z)}$ with $h$ the horocycle index).

*Review correction 2026-10-28 (astra review, VERDICT obs:boundary-lefschetz-two-lagrangians: MINOR):* (i) specify the density model: $\pi_s$ acts on $s$-densities in compatible local Haar coordinates (or via the Radon–Nikodym derivative of a fixed quasi-invariant measure); no PGL-invariant finite measure exists; $\mathrm{Re}\,s=\tfrac12$ is the unitary half-density model, a general $s$ is not unitary in the displayed $L^2$ norm. (ii) The two power assignments are swapped. Old: $p^{-\ell(1-s)}=p^{-\ell}\mu^{\ell}$ and $p^{-\ell s}=p^{-\ell}(p/\mu)^{\ell}$; new: $p^{-\ell s}=p^{-\ell}\mu^{\ell}$ and $p^{-\ell(1-s)}=p^{-\ell}(p/\mu)^{\ell}$ ($\mu=p^{1-s}$). The unordered sum and the Satake pair $\{\mu,p/\mu\}$ are unaffected. Recomputed at $p=5$, $s=3/4$, $\ell=1$: $p^{-\ell(1-s)}=0.66874\ne p^{-1}\mu=0.29907=p^{-\ell s}$. (iii) $|\mu|=\sqrt p$ holds on the whole line $\mathrm{Re}\,s=\tfrac12$, not only at $s=\tfrac12$; for $s=\tfrac12+it$ the trace is $2p^{-\ell/2}\cos(t\ell\log p)$, so equal positive contributions are special to $s=\tfrac12$. The complex Satake numbers are inducing-character contributions at the two fixed points, not literally the two boundary points.

**5.3 (SKETCHED; the claim of T5).** The Poisson transforms $P_s\phi$ and $P_{1-s}\psi$ both satisfy the radial recurrence with the same $\lambda$;
the standard intertwining operator $I_s:\pi_s\to\pi_{1-s}$, $I_s\phi(z)=\int|z-z'|^{-2(1-s)}\phi(z')dz'$ (normalised so that $P_{1-s}I_s=c(s)P_s$ with
Harish-Chandra's $c(s)=(1-p^{-2s}\ldots)$, from memory), gives the invariant pairing $\langle\phi,\psi\rangle_s=\int\phi\,\overline{I_s\psi}$ on $\pi_s$.
Restricting the label phase space to the $\lambda$-eigenplane and writing a label $(f,g)=(P_s\phi$ at a vertex, at its neighbour$)$, the Casoratian
$\Omega$ of 5.1 is the antisymmetric form $(\mu-p/\mu)\,(a\bar b'-a'\bar b)$ on the coefficients of the two Satake modes, and I expect
$\Omega((f,g),(f',g'))=(\mu-p/\mu)\cdot\langle\phi,\psi'\rangle_s$-type with the pairing of the $\mu$-component of one label against the $p/\mu$-component
of the other, the constant being the Casoratian $\mu-p/\mu=\sqrt{\lambda^2-4p}$, which is $1/c$-function-like (it vanishes exactly at the
degenerate points $\lambda=\pm2\sqrt p$ where $\pi_s$ is reducible/$I_s$ singular). I did not have time to fix the measure normalisation of $I_s$ on
$\mathbb P^1(\mathbb Q_p)$ and verify the constant; this is the OPEN part. If it holds, the Weil form $\mathcal Q=\tfrac12\Omega(M-V)$ becomes, on the
boundary, $\tfrac12(\mu-p/\mu)\cdot(\mu-p/\mu)\cdot(\ldots)$, i.e. $\mathcal Q|_{\text{plane}}=\tfrac{4p-\lambda^2}4\times$(a positive Hermitian pairing of
boundary functions), which would state Weil positivity as: **the intertwining pairing of $\pi_s$ with itself through $I_s$ is positive definite iff
$s=\tfrac12+i\theta$ (unitary principal series), i.e. iff the Satake parameter is in the band** — the known unitarity criterion for the principal
series of $PGL_2(\mathbb Q_p)$ (complementary series $s\in(0,1)$ real have a positive but different pairing). What would be needed: the explicit $I_s$
normalisation, a two-line check on the spherical vector, and the identification of the label space coefficients with boundary functions on a finite
quotient (through $\Gamma$-invariant boundary distributions, not functions, which is the real obstacle for a finite $Y$).

*Review 2026-10-28 (astra review, VERDICT T5 and VERDICT conj:casoratian-is-intertwining-pairing: INVALID):* the exact Casoratian (5.1) and the flat trace (5.2) survive; the sketch 5.3 contains false assertions. (a) The map from label space to boundary (Poisson) data is unconstructed (UNVERIFIED); a radial adjacency eigenfunction satisfies $pf_{r+1}=\lambda f_r-f_{r-1}$ and one needs $F_r=p^rf_r$ to get $F_{r+2}=\lambda F_{r+1}-pF_r$; a Poisson kernel at $s=\tfrac12$ along a ray moving away from its boundary point (ratio $p^{-1/2}$) has defect $(p-1)^2/p$ in the unrescaled transfer recurrence; nonradial restrictions need satisfy neither. (b) The complex-linear $\Omega$ is bilinear, coefficient form $(\mu-\nu)(ab'-ba')$; the displayed conjugated form is not the same symplectic form without a specified real structure. (c) The positivity equivalence is false: for real $\tfrac12<s<1$ the form $\int\bar f\,I_sf$ is strictly positive (Fourier multiplier $\Gamma_p(\alpha)|\xi|^{-\alpha}$, $\alpha=2s-1$, $\Gamma_p(\alpha)=(1-p^{\alpha-1})/(1-p^{-\alpha})>0$), yet $\lambda=p^s+p^{1-s}>2\sqrt p$ and $\mathcal Q$ is indefinite (e.g. $p=5$, $s=3/4$: $\lambda=4.8390503$, $\det\mathcal Q=-0.8541020$, recomputed); a factor $(4p-\lambda^2)/4$ times a positive pairing would be negative definite there. (d) Coalescence $\mu=\pm\sqrt p$ is not reducibility of the normalised unramified principal series (reducible at $\lambda=\pm(p+1)$); the normalised Riesz intertwiner has multiplier $|\xi|^{1-2s}$ and is the identity at $s=\tfrac12$; a pole of an unnormalised $c$-function is not a singular normalised intertwiner; $c(s)$ was left unspecified. Survives only as an OPEN question: a specified map from automorphic boundary data and a specified pairing recovering the graph form without inserting the finite-quotient pairing. Next-step item (iii) below is likewise unverified (a complex Satake pair is not a pair of $\mathbb Q_p$ Lagrangian points).

## Correction ledger (what the brief got wrong, with the fix)

| id | brief says | correction | where shown |
|---|---|---|---|
| C1 | $\widetilde W(u,v)=\psi_p(-uv/2)W(u,v)$ is a representation on isotropic lattices | the sign must be $+$ for $W(u,v)f=\psi_p(vx)f(x+u)$; with $-$ the phase is $\psi_p((3uv'+u'v)/2)$ and $\widetilde W(1,c/p)^2\ne\widetilde W(2,2c/p)$ | Lemma 1.2; `output_tree_codes.txt` T1'; `output_mub.txt` last lines |
| C2 | the code of a vertex is independent of the representative up to $D_c$ | false: $D_c$ is $\mathrm{diag}(c^{-1},c)$, no Clifford implements a homothety; $\mathcal C_{pL}\supsetneq\mathcal C_L$, a nested tower of dimensions $p^{k+2m}$; the vertex's code is that of the unique rep. with $k\in\{0,1\}$; codes equivalent iff same colour ($SL_2$-orbit) | §1 after Prop. 1.5 |
| C3 | "the squeeze part of $\gamma\sim\mathrm{diag}(1,\lambda)$ is $D_{\lambda^{\pm1}}$" | $D_\lambda$ is the Weil image of $\gamma^2/\det\gamma$ (translation $2\ell$); the weight $p^{-\ell/2}$ is $\operatorname{Tr}D_{\lambda(\gamma)}$ with $\lambda$ the eigenvalue ratio, equivalently the phase-space Lefschetz number $1/|\det(1-g_\gamma)|$ of the $SL_2$-normalisation of $\gamma$ | Thm 4.3 and the paragraph after it |
| C4 | every hyperbolic element is a squeeze composed with a unit | true for even $\ell$; for odd $\ell$ the element is $D_{p^{(\ell-1)/2}}\cdot\mathrm{diag}(1,p)\cdot$unit, and $\mathrm{diag}(1,p)$ is a similitude of multiplier $p$, not in $Sp(V)$ | §3 after Thm 3.4 |
| C5 | elliptic elements "fix a vertex or an edge" | correct as a statement about $PGL_2$ (edge = inversion, odd $v(\det)$); in $\Gamma$ (no inversions, torsion-free) there are none at all | Thm 3.4(ii) |
| C6 | $X^{5,13}$ (2184 vertices) suggested for the non-bipartite explicit formula | $(5/13)=-1$: $X^{5,13}$ is the Cayley graph of $PGL_2(\mathbb F_{13})$ and bipartite; the formula needs the alternating pair; $X^{5,11}$, $X^{5,29}$ are the non-bipartite ones | §4(c) |
| C7 | "Tr $D_a=|a|^{1/2}/|1-a|$" as a distributional trace on $L^2(\mathbb Q_p)$ | $D_a$ is not trace class and $\int h(a)D_ad^\times a$ is not Hilbert–Schmidt (scale invariance); the correct exact statement is Thm 4.2: the trace on the code $\mathcal C_n$ equals $|a|^{1/2}p^{\min(v(1-a),2n)}$, stabilising to the Lefschetz number once $2n\ge v(1-a)$, and diverging as $p^{2n}$ at $a=1$ | Thm 4.2; `output_ihara_lefschetz.txt` T4(b) |

*Review correction 2026-10-28 (astra review, VERDICT C2: MINOR):* row C2, "codes equivalent iff same colour", holds for the minimal representatives $L_0$ (or equal tower levels); arbitrary isotropic lattices have Clifford-equivalent codes iff $k(L)$ is equal. Homotheties $\pm I$ are harmless exceptions to "no Clifford implements a homothety".

*Review 2026-10-28 (astra review, VERDICT C3: INVALID):* row C3 as a bundled universal statement; see the in-place line after "Which operator (C3)" (§4(b)). The eigenbasis identity $\gamma^2/\det\gamma=\mathrm{diag}(\lambda^{-1},\lambda)$ survives.

*Review correction 2026-10-28 (astra review, VERDICT C5: MINOR):* row C5: exclude the identity; discreteness of $\Gamma$ plus torsion-freeness removes nonidentity elliptics; the inversion step uses the central edge of $[x,\gamma x]$ (annotations after Theorem 3.4).

*Review correction 2026-10-28 (astra review, VERDICT C7: MINOR):* row C7: the exact statement concerns compressions $P_nD_aP_n$; the flat trace at $a\ne1$ is well defined; the non-Hilbert–Schmidt assertion excludes the zero average; the rank $p^{2n}$ at $a=1$ is not Connes's logarithmic cutoff term (annotation after Theorem 4.2).

## Numerical checks for the blind lane

All from `cd notes/astra-2026-10-27/tree-codes/fable && python3 checks/<name>.py` (system python3; no PARI needed).

1. `checks/mub.py`: for $p=7$, over the $8$ bases, min and max of $|\langle b,b'\rangle|^2$ across bases are both $0.142857142857=1/7$; for $p=5$ the
   stabiliser generator of basis $c=1$ prints as $\omega^{3}Z^1X^1$ ($2^{-1}\equiv3$ mod 5).
2. `checks/tree_codes.py`: $p=3$, $\gamma=(8,5;9,0)$: $v(\operatorname{tr})=0$, $v(\det)=2$, $\ell=2$, $d(v,\gamma^kv)=[2,4,6,8,10]$; among the 53 vertices
   within distance 3 of the base, exactly 7 have displacement 2 and exactly those 7 are split by the eigenlines. For $s=-1/2$ the representation check
   prints False, for $s=+1/2$ True.
3. `checks/ihara_lefschetz.py` (about 6 min, dominated by the dense Hashimoto route): $X^{5,11}$ has $660$ vertices, girth 6, $N_6=3960$, $N_7=110880$,
   $N_8=475200$, $\pi(6)=660$, $\pi(7)=15840$, $\pi(8)=59400$, largest non-trivial $|\lambda|=4.372281$; explicit-formula residual $3.41\cdot10^{-12}$;
   $24$ tailed closed reduced words of length 8, all with $\ell(\gamma)=6$.
4. same script: $X^{5,13}$ has $2184$ vertices, bipartite, girth 8, $N_8=1048320$, $\pi(8)=131040$, largest non-trivial $|\lambda|=4.249721$, residual
   $1.00\cdot10^{-11}$ (with the alternating pair included).
5. same script, block T4(b): $\operatorname{Tr}(P_nD_{126}P_n)=1,25,125,125$ for $n=0,1,2,3$ at $p=5$ ($v_5(1-126)=3$); $\operatorname{Tr}(P_nD_{1/25}P_n)=0.2$
   for all $n$; $\operatorname{Tr}(P_nD_1P_n)=1,25,625,15625$.
6. `python3 checks/ihara_lefschetz.py --big` (about 16 min) adds $X^{5,29}$: $12180$ vertices, non-bipartite, largest non-trivial $|\lambda|=4.442016$,
   $N_k=0$ for all $k\le8$ (girth $>8$), explicit-formula residual $2.67\cdot10^{-10}$.

## What this changes in the notebook

Candidate rows (none registered; cross-family REFUTE review pending per the round design):

| id | statement | status |
|---|---|---|
| `prop:tree-dual-lattice` | $L^\perp=(\det g)^{-1}L$, $[L^\perp:L]=p^{2v(\det g)}$; colour $=v(\det g)$ mod 2; unique isotropic representative with $k\in\{0,1\}$; qunaught/qudit vertices | PROVED (§1) |
| `prop:tree-colours-code-dimension` | the vertex carries the nested code tower $\mathcal C_{p^mL_0}$, $\dim p^{k+2m}$; codes Clifford-equivalent iff same colour; the brief's "independent up to $D_c$" is false | PROVED, corrects the brief (§1, C2) |
| `lem:symmetric-weyl-sign` | $\widetilde W=\psi_p(+uv/2)W$ is a representation on isotropic lattices; $\psi_p(-uv/2)W$ is not | PROVED (C1) |
| `prop:tree-neighbours-mub` | neighbours of a qudit vertex = lines of $M^\perp/M$ = the $p+1$ standard WH MUBs (computational + quadratic phases $\psi_p(-cx^2/2p)$); dual statement for qunaughts | PROVED, checked $p=3,5,7$ (§2) |
| `prop:geodesic-squeeze` | ends $=\mathbb P^1(\mathbb Q_p)$; geodesic $=$ split lattices of a transverse Lagrangian pair; $\ell(\gamma)=\max(v(\det)-2v(\operatorname{tr}),0)=v(\lambda_2/\lambda_1)$; hyperbolic $\equiv\mathrm{diag}(1,p)^\ell\cdot$unit, a symplectic squeeze iff $\ell$ even | PROVED (§3) |
| `thm:ihara-zeta-squeeze-euler` | $\zeta_Y(u)=\prod_{[\gamma_0]}(1-u^{v_p(\lambda(\gamma_0))})^{-1}$ with multiplicity $\ell(\gamma_0)=\#\Gamma_\gamma\backslash\mathrm{Axis}$ | PROVED (from memory + re-proof, §4a) |
| `thm:code-trace-of-squeeze` | $\operatorname{Tr}(P_nD_aP_n)=|a|_p^{1/2}p^{\min(v(1-a),2n)}$ on the code of $p^n\mathbb Z_p^2$; $=|a|^{1/2}/|1-a|$ once $2n\ge v(1-a)$; $p^{2n}$ at $a=1$ | PROVED, checked exactly (§4b) |
| `thm:ihara-zeta-squeeze-lefschetz` | orbit side of the graph's explicit formula $=\sum_{[\gamma_0]}\sum_m\ell(\gamma_0)\operatorname{Tr}_{\mathcal C_n}D_{\lambda(\gamma_0)^m}$, $=\ell(\gamma_0)/|\det(1-g_{\gamma_0^m})|_p$; the operator is the squeeze by the eigenvalue ratio ($=\gamma^2/\det\gamma$), not $\gamma$ | PROVED (§4b, C3); NUMERICAL on $X^{5,11},X^{5,13}$ to $10^{-11}$ |
| `obs:lps-words-translation-length` | in $\Lambda(2q)\subset PGL_2(\mathbb Q_5)$, $\ell(\gamma)=k-2v_5(2a)$ equals the word length for every tailless closed word ($k\le8$, $q=11$) and is smaller for tailed ones | NUMERICAL (§4c) |
| `obs:boundary-lefschetz-two-lagrangians` | flat trace of $\pi_{1/2}(\gamma)$ on $L^2(\mathbb P^1(\mathbb Q_p))$ is $2p^{-\ell/2}$, one orbit weight per fixed Lagrangian; $\mu=p^{1-s}$ fixes T5's normalisation | PROVED as a computation (§4b, §5.2) |
| `conj:casoratian-is-intertwining-pairing` | $\Omega|_{\lambda\text{-plane}}=(\mu-p/\mu)\times$ the $I_s$-pairing of Poisson data; Weil positivity $=$ unitarity of $\pi_s$ | SKETCHED/OPEN (§5.3) |

*Review 2026-10-28 (astra review): dispositions of the candidate rows above.* VALID: `prop:tree-dual-lattice`, `lem:symmetric-weyl-sign`, `prop:tree-neighbours-mub`, `thm:ihara-zeta-squeeze-euler`, `thm:code-trace-of-squeeze`, `obs:lps-words-translation-length`. MINOR: `prop:tree-colours-code-dimension` (annotation after §1 C2 paragraph), `obs:boundary-lefschetz-two-lagrangians` (annotation after §5.2). INVALID as stated: `prop:geodesic-squeeze` (§3, after the C4 paragraph), `thm:ihara-zeta-squeeze-lefschetz` (§4(b), after Theorem 4.3), `conj:casoratian-is-intertwining-pairing` (§5, end). The "PROVED" words in the Status column are superseded by these annotations.

One-line annotations for record pages: `graph-ihara.md` §2(b): "the $p+1$ stabiliser axes are the lines of $M^\perp/M$ and are the standard WH
MUBs (2026-10-27, T2); the vertex's code is the code of its unique representative with $k\in\{0,1\}$, the class carries a nested tower"; also
replace "two qunaughts $2k$ steps apart have overlap $p^{-k/2}$" by "the squeeze $D_{p^k}$ of translation $2k$ has trace $p^{-k/2}$ on every code
$\mathcal C_n$ of the base vertex (Thm 4.2)", which is the steer-compliant form. `graph-ihara.md` §5: "the orbit term $+\ell q^{-m\ell/2}$ is
$\ell(\gamma_0)\operatorname{Tr}_{\mathcal C_n}D_{\lambda(\gamma_0)^m}$, the $p$-adic Lefschetz trace of the squeeze by the eigenvalue ratio of the
hyperbolic class (not of $\gamma$ itself: that squeeze is $\gamma^2/\det\gamma$); the bipartite case adds $-(-1)^k(q^{k/2}+q^{-k/2})$".
`adelic-gkp.md` §10: "the distributional trace $|\lambda|^{1/2}/|1-\lambda|$ is the trace of $D_\lambda$ on the GKP code of $p^n\mathbb Z_p^2$ for
$2n\ge v_p(1-\lambda)$ (exact, Thm 4.2 of the 2026-10-27 T lane), and the $2h(1)\log\Lambda$ term is its value $p^{2n}$ at $\lambda=1$". `adelic-gkp.md`
§5 / Prop. 5: "the symmetric phase convention for $p$ odd is $\psi_p(+uv/2)W(u,v)$ (C1)".

*Review 2026-10-28 (astra review, §9 adjudication of the annotations proposed above):* `graph-ihara.md` §2(b) MUB/tower annotation: AGREE (add: the minimal code uses the unique representative of determinant valuation 0 or 1; do not infer that both colours descend to a non-bipartite quotient). The two-qunaught replacement: AGREE-WITH-CHANGE, use "for $k\ge1$, $D_{p^k}$ implements a symplectic translation of length $2k$ on the standard apartment, and $\operatorname{Tr}(P_nD_{p^k}P_n)=p^{-k/2}$ for every $n\ge0$" (the word compression and $k\ge1$ are necessary; at $k=0$ the trace is $p^{2n}$). `graph-ihara.md` §5: AGREE-WITH-CHANGE, say $\ell_0\operatorname{Tr}(P_nD_{\lambda^m}P_n)=\ell_0p^{-k/2}$, that $D_\lambda$ intertwines the Weyl action of $\gamma^2/\det\gamma$ of tree length $2\ell_0$ while the orbit exponent stays $\ell_0$, and subtract $(-1)^k(q^{k/2}+q^{-k/2})$ in the bipartite case; not a representation of $\Gamma$ on $\mathcal C_n$, not an unrestricted $\mathbb Q_p$ phase-space trace. `adelic-gkp.md` §10: DISAGREE as written (its last clause equates $p^{2n}$ with $2h(1)\log\Lambda$); the review's replacement: "for $a\ne1$ the flat trace $|a|^{1/2}/|1-a|$ equals $\operatorname{Tr}(P_nD_aP_n)$ whenever $2n\ge v_p(1-a)$; at $a=1$ this compression has rank $p^{2n}$; integrating the cutoff traces over units with multiplicative unit volume $\log p$ gives $(2n+1)\log p$, exhibiting local logarithmic growth near the identity without identifying a pointwise rank with Connes's global cutoff term". `adelic-gkp.md` §5/Prop. 5 sign: AGREE.

Next step: (i) the cross-family REFUTE review of this lane (the round design), with special attention to Thm 4.2's case $|a|>1$ and to C3; (ii)
close T5: normalise $I_s$ on $\mathbb P^1(\mathbb Q_p)$ and test the Casoratian identity on the spherical vector numerically on a finite ball of the
tree; (iii) the pizer lane's phase space $(\mathbb Z^{2n},\Omega,M)$ versus the local statement here: the global $H^1$ of $X_0(p)$ should decompose the
label space into the $\lambda$-eigenplanes of §5.1, each a pair of Satake parameters, i.e. a pair of fixed Lagrangians of some hyperbolic class.
