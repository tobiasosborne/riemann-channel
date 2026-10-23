# Lane C — trace moments, Schur recursion, and the Casoratian

Author: `codex:gpt-6-astra`, 2026-10-23. Research record; no claims registered.

The brief is false as written in C1(iii) and requires qualifications in C2. The correct length of a finite Schur sequence is the number of **distinct spectral points**, not the degree with multiplicity. All graph computations below remove both roots of every trivial adjacency mode. No RH assumption supplies numerical input. Function-field RH is invoked only as the labelled theorem of Weil. The zeta computation is an independent Python implementation of lane R's prime/pole/archimedean formula, not a call to its zero-based model or to `zst`'s zero routines.

## 1. C1 — graph rung

### C1(i): PROVED — traces and the exact Ihara correction

Assume a connected undirected `(q+1)`-regular graph, `q>=1`, with `n` vertices and `m` edges. Write the two roots of each quadratic as `mu_+,mu_-`; they are complex conjugates only in the band. With

\[
 M=\begin{pmatrix}A&-qI\\I&0\end{pmatrix},\quad S=M/\sqrt q,
 \qquad c_k=q^{-k/2}\operatorname{Tr}M^k=\operatorname{Tr}S^k,
\]

Ihara–Bass, followed by `-u d/du log`, gives for **every k>=1**

\[
 c_k=q^{-k/2}\{\operatorname{Tr} B^k-(m-n)(1+(-1)^k)\}.
\]

At `k=0` the same identity follows by dimensions: `2m-2(m-n)=2n`. For retained moments subtract `q^{k/2}+q^{-k/2}` for `lambda=q+1`, and also `(-1)^k(q^{k/2}+q^{-k/2})` for `lambda=-(q+1)` in the bipartite case. At `k=0` subtract two per removed mode. These are exactly the cycle/trivial/tree terms of `graph-ihara.md` §5, including their signs.

The label-space convention here is symplectically conjugate to that page's `M_0=[[0,-I],[qI,A]]` by `C=[[0,-I],[I,0]]`: `CM C^{-1}=M_0`. Thus its lattice energy `[[qI,A/2],[A/2,I]]` pulls back to

\[
 Q=\tfrac12\Omega(M-qM^{-1})=
 \begin{pmatrix}I&-A/2\\-A/2&qI\end{pmatrix},\qquad
 \Omega=\begin{pmatrix}0&I\\-I&0\end{pmatrix}.
\]

The label-to-edge map has rank `2n-1` (`2n-2` bipartite); the nondegenerate alternating form is on labels and does not descend through this kernel. The two conventions must not be mixed.

### C1(ii): PROVED — Toeplitz positivity and the lattice form

For any retained finite reciprocal multiset `w=mu/sqrt(q)`, define `c_{-k}=conj(c_k)`. All `T_N=(c_{j-k})` are positive semidefinite iff every retained `|w|=1`. Sufficiency is
\[
 \sum_{j,k}b_j\bar b_k c_{j-k}=\sum_w\left|\sum_j b_j w^j\right|^2\ge0.
\]
For necessity, positivity gives `|c_k|<=c_0` from two-by-two principal minors. If the maximal root modulus is `R>1`, divide `c_k` by `R^k`. The maximal-modulus terms form a finite trigonometric sum whose Cesàro mean square tends to the sum of squared grouped multiplicities, which is positive; the other terms decay. Hence `c_k` is unbounded on a subsequence. Reciprocity excludes a root strictly inside without one outside. This also proves the statement without semisimplicity: traces do not see Jordan blocks.

This is precisely registered `thm:weil-positivity-finite` in `report/sections/08b_weil_positivity.tex`: “the sequence … is positive definite if and only if [the retained eigenvalues have modulus at most the critical radius]”; its registered `thm:weil-duality-pairing` adds reflection duality and turns the disk into the circle. Here the radius is `sqrt(q)` and the retained roots have the required reflection symmetry. Consequently
\[
 \text{Ramanujan}\iff T_N\succeq0\ (\forall N)\iff Q\succeq0
 \text{ on the nontrivial label modes}.
\]

For one mode put `a=lambda/sqrt(q)`. Then `Q_lambda=[[1,-lambda/2],[-lambda/2,q]]` is semidefinite iff `a^2<=4`. The trace Gram on `1,w` is `[[2,a],[a,2]]`; exactly
\[
 T_1=2D^TQ_\lambda D,\qquad D=\operatorname{diag}(1,-1/\sqrt q).
\]
Reduce any polynomial modulo `w^2-aw+1` and sum this identity over modes with their multiplicities. This identifies positivity on all test polynomials, without asserting that a single cyclic polynomial sees separate copies of an identical mode.

The handoff's stronger identity is specifically for the **trace-oriented** compatible form: in the squarefree trace algebra, `sigma(F)=V=q/F`,
\[
 \Omega_+(x,y)=\operatorname{Tr}\frac{x\sigma(y)}{V-F},\quad
 2Q_{\Omega_+}(x,y)=\operatorname{Tr}(x\sigma(y)),\quad
 \operatorname{Tr}((F/\sqrt q)^j\sigma((F/\sqrt q)^k))=c_{j-k}.
\]
Thus 08b's window form is twice that lattice form, as recorded in `registered-record.md` §2.3. This formula needs invertibility of `V-F`; real endpoints require the elementary limiting/block formula above. Repeated roots require a reduced spectral algebra with multiplicity weights, or a separate geometric semisimple realization. It is not an unconditional equality of matrices on the original `2n` labels.

**Endpoint correction (PROVED).** Strict inequality `|a|<2` means the Chebyshev transfer `[[a,-1],[1,0]]` is conjugate to a rotation and the energy is positive definite. At `|a|=2` it is a nontrivial parabolic Jordan block and the energy is only semidefinite. Thus “semidefinite iff rotation” in the prompt is false. Rescaling recurrence states by `diag(sqrt(q),1)` conjugates `M_lambda/sqrt(q)` to this Chebyshev matrix. The alternating Casoratian scales by `q` before removing damping and is constant afterwards. With states ordered as `(y_{k+1},y_k)`, our displayed `Omega` evaluates to minus the prompt's `C_k`; reversing the order gives `C_k`. This is an orientation convention, not a change in Abel's identity.

### C1(iii): REFUTED as stated; PROVED with distinct support in place of degree

The smallest requested counterexample is `K4`: even after removing the trivial pair, `p_nt(z)=(1+z/sqrt(2)+z^2)^3`, whereas its measure has two atoms of mass three. Its coefficients are `alpha_0=-sqrt(2)/4, alpha_1=-1`, and there are no further coefficients. The full `p` also includes off-circle trivial roots: keeping them gives `alpha=[0,-1/4,4sqrt(2)/5]` through the first failed pivot, also printed by the script. A POPUC with interior preceding parameters has simple circle zeros; it cannot equal either polynomial claimed in the brief.

Here is the corrected theorem. Let `r` be the number of distinct retained circle points, counted without multiplicity, and weight each point by its spectral multiplicity. Then

\[
 |\alpha_j|<1\quad(0\le j<r-1),\qquad |\alpha_{r-1}|=1.
\]

The rank is `min(N+1,r)` and the terminal monic polynomial is

\[
 R(z)=\prod_{w\in\operatorname{supp}\nu}(z-w)
     =z\Phi_{r-1}(z)-\bar\beta\Phi_{r-1}^*(z),\qquad
 \beta=\alpha_{r-1}=-\overline{R(0)}.
\]

For an interior real graph spectrum the distinct roots occur in conjugate pairs, so `R(0)=1` and `beta=-1`. At an endpoint use the displayed general formula. Multiplicities affect the earlier parameters, but not the terminal polynomial. The reduced retained Ihara polynomial is this POPUC up to its leading coefficient; the original polynomial with multiplicities generally is not.

**Constructive proof and convention.** Use the inner product linear in its first argument, `c_k=int w^k dnu(w)`, `Phi_0=1`, and `h_0=c_0`. If `Phi_n(z)=sum_j b_j z^j`, set

\[
 \alpha_n=\frac{\overline{\sum_{j=0}^n b_jc_{j+1}}}{h_n},\quad
 \Phi_{n+1}=z\Phi_n-\bar\alpha_n\Phi_n^*,\quad
 h_{n+1}=h_n(1-|\alpha_n|^2),\quad
 \Phi_n^*=z^n\overline{\Phi_n(1/\bar z)}.
\]

Orthogonality of the new polynomial against `z,...,z^n` follows from the two old orthogonality relations; the displayed choice enforces orthogonality against `1`. Taking norms gives the pivot identity. A nonzero polynomial of degree below `r` cannot vanish at every support point, so these norms are positive up to degree `r-1`; the monic degree-`r` vanishing polynomial has norm zero. Vandermonde evaluation gives the rank and proves all assertions.

This is Levinson recursion on the Toeplitz matrix. In determinant form, with `D_N=det T_N`, `D_-1=1`,

\[
 h_n=D_n/D_{n-1},\quad
 1-|\alpha_n|^2=D_{n+1}D_{n-1}/D_n^2,\quad
 D_N=c_0^{N+1}\prod_{j=0}^{N-1}(1-|\alpha_j|^2)^{N-j}.
\]

Normalizing the measure by `c_0` does not change alpha. Equivalently the Carathéodory function is `F(z)=1+2 sum_{k>=1} conj(c_k)z^k/c_0`, its Schur function is `(F-1)/(z(F+1))`, and the iterates are `f_{n+1}=(f_n-alpha_n)/(z(1-conj(alpha_n)f_n))`. Equality with the polynomial coefficients is Geronimus's theorem. These are moment coordinates, not the Schur–Cohn reflection coefficients obtained by applying polynomial stability recursion directly to `p`. For instance the latter encounters a unit-modulus constant term immediately for any self-reciprocal `p`, even an off-circle one. Schur–Cohn/Jury is an open-disk stability test; our finite circle measures lie on its terminal boundary.

All entries in the following table are exact and printed by `python3 checks/check_graph.py` (`checks/output_graph.txt`). The final entry in each row is the terminal parameter, not a violation.

| graph | retained degree | distinct points | alpha, starting at index 0 |
|---|---:|---:|---|
| K4, q=2 | 6 | 2 | `-sqrt(2)/4, -1` |
| Petersen, q=2 | 18 | 4 | `-sqrt(2)/12, -31/71, -9sqrt(2)/34, -1` |
| K5, q=3 | 8 | 2 | `-sqrt(3)/6, -1` |
| cube, q=2 | 12 | 4 | `0, -3/4, 0, -1` |
| triangular prism, q=2 | 10 | 6 | `-3sqrt(2)/20, -119/191, -97sqrt(2)/372, -251/313, 3sqrt(2)/47, -1` |

For `K_n`, `4<=n<=9`, the answer is `[-1/(2sqrt(n-2)),-1]`; the script prints each separately. Möbius–Kantor is Ramanujan: `alpha=[0,-13/28,0,-173/205,0,-67/108,0,-1]`. Its eigenvalues and numerical coefficients are printed independently.

For the record's prism `C_21 x K_2`, the parameters through the first failure are

```
-0.0258697602873127143, -0.287446982662400476,
-0.0608510450260311539,  0.269128549447475171,
-0.0879024920375665844,  0.432267067410905968,
-0.226630190203709668,   0.782165486842001300,
-2.02694065057576385732.
```

Thus `T_8` (size nine) is positive definite, and the first negative pivot occurs in `T_9` (size ten). The survey covers every prism with `3<=m<=32` at 100 decimal digits. Selected results:

| m | out-of-band adjacency modes, with multiplicity | first bad alpha index | value |
|---:|---:|---:|---:|
| 9 | 2 | 8 | -1.874002062070699 |
| 16 | 4 | 13 | 10.931938452149598 |
| 17 | 4 | 8 | -1.866996318231494 |
| 18 | 4 | 11 | 2.871057611438183 |
| 21 | 4 | 8 | -2.026940650575764 |
| 22 | 4 | 9 | 1.187755102040816 |
| 31 | 8 | 8 | -2.704805804451441 |
| 32 | 8 | 9 | 2.306252570958453 |

**PROVED: the first failure index is not a function of the number of out-of-band modes.** The two prisms at `m=16,17` each have exactly four such modes (use `lambda=2cos(2pi j/m)+/-1`). Exact integer adjacency-power calculations and exact symbolic Levinson pivots give respectively `alpha_13=43707967/3998190>1` and `alpha_8=-413023893 sqrt(2)/312857602<-1`, all earlier pivot factors positive. This is an exact counterexample, not an inference from the table. In general an indefinite sequence can also encounter a zero pivot followed by inconsistent later moments; a boundary coefficient alone is not an automatic positivity certificate. Continue with rank-consistency tests rather than division by zero.

### The transfer matrices: PROVED identity, REFUTED literal identification

For the monic Szegő recursion,

\[
 A_n(z)=\begin{pmatrix}z&-\bar\alpha_n\\-\alpha_nz&1\end{pmatrix},\quad
 \det A_n(z)=z(1-|\alpha_n|^2),\quad
 A_n(z)^TJ_0A_n(z)=z(1-|\alpha_n|^2)J_0,
\]

where `J_0=[[0,1],[-1,0]]`. On `|z|=1`, with `J=diag(1,-1)`, also

\[
 A_n(z)^*JA_n(z)=(1-|\alpha_n|^2)J.
\]

Both follow by multiplication. Dividing by `sqrt(z)` removes the spectral phase in the determinant, and dividing by `sqrt(1-|alpha_n|^2)` removes its positive damping. A fixed Cayley change of basis takes the resulting `SU(1,1)` matrix to a real `SL(2,R)` matrix. This is the precise Abel/Casoratian analogy. The raw alternating multiplier is **z times** `1-|alpha|^2`, not just `1-|alpha|^2`. At the terminal coefficient the matrix degenerates.

The notebook's `Omega` is the same universal two-dimensional alternating form on each recurrence mode, not a special `k=0` value of a spectral Gram–Schmidt algorithm. Its time index and the Szegő degree index are different, and alpha changes when the spectral weights change even though the graph mode recurrence does not. In particular neither the Casoratian nor the matrix `S_lambda` literally equals the Szegő transfer matrix. The de Branges/canonical-system discussion in `analytic.md` §10 supplies a continuous analogue of positive transfer systems; it does not identify these independent evolution variables. The genus-one degree form in §13 is the symmetric energy built from the alternating Casoratian.

References: B. Simon, *Orthogonal Polynomials on the Unit Circle*, Part 1 (2005), §§1.3, 1.5, 2.1–2.3 (standard results cited from memory, with the elementary finite proof above); the [author's contents](https://math.caltech.edu/opuc/opuctoc.html) locate these sections. The POPUC convention is also fixed explicitly in [Simon, “Rank One Perturbations and the Zeros of Paraorthogonal Polynomials on the Unit Circle”](https://web.ma.utexas.edu/mp_arc/c/06/06-173.pdf), (1.1)–(1.3). Schur–Cohn/Jury and de Branges, *Hilbert Spaces of Entire Functions* (1968), are cited bibliographically; no new identification with their systems is claimed.

## 2. C2 — function-field rung

### C2: REFUTED at the stated degree; PROVED with completion and distinct support

Already at `q=5, f=t^4+1=(t^2+2)(t^2+3)` there is an even primitive quartic character with

\[
 \Lambda(u)=L(u)/(1-u)=1+(2-4i)u+(-3-4i)u^2
             =(1+(1-2i)u)^2.
\]

It has completed degree two but **one** support point, and its only coefficient is `alpha_0=(-1-2i)/sqrt(5)`, of modulus one. This refutes the requested strict inequality at index zero. Character specification: on the two residue fields, choose generators `1+t mod(t^2+2)` and `1+2t mod(t^2+3)` (both of order 24), and give each generator value `exp(2pi i*6/24)=i`. The script `checks/check_ff_examples.py` recomputes every coefficient by character sums in `Q[Z]/Phi_24(Z)` and prints zero discriminant exactly. This example also locates the failure in the squarefree-modulus setting of lane J, without wild ramification.

Let `m=deg f`, let `epsilon=1` for an even character and zero otherwise, and let `chi` be primitive and nontrivial. Define

\[
 \Lambda_\chi(u)=L(u,\chi)/(1-u)^\epsilon
   =\sum_{j=0}^{d}A_ju^j=\prod_{i=1}^{d}(1-F_i u),\qquad d=m-1-\epsilon.
\]

The **completed finite polynomial**, rather than the raw even `L`, satisfies Weil's RH. The degree-zero cases have the zero trace measure and no Schur coefficients; they are recorded as empty lists. The trivial character of conductor one is excluded: its L-function is rational and is not an instance of this polynomial assertion.

The correct moments are

\[
 c_0=d,\qquad
 c_k=q^{-k/2}\sum_iF_i^k
 =-q^{-k/2}\left(\sum_{\substack{P\text{ monic irreducible}\\\deg P\mid k}}
             \deg P\,\chi(P)^{k/\deg P}+\epsilon\right),\qquad
 c_{-k}=\overline{c_k}.
\]

Here `chi(P)=0` at ramified primes. **Proof:** `u L'/L` is the Euler sum in parentheses without epsilon; removing `1-u` adds `epsilon*u/(1-u)` to the logarithmic derivative, while `u Lambda'/Lambda=-sum_k Tr(F^k)u^k`. Thus the minus sign and the even-character correction are essential. Equivalently Newton identities give, for example,

\[
 c_1=-A_1/\sqrt q,\quad c_2=(A_1^2-2A_2)/q,\quad
 c_3=(-A_1^3+3A_1A_2-3A_3)/q^{3/2}.
\]

The finite functional equation is

\[
 p_\chi(z):=\Lambda_\chi(z/\sqrt q)=W p_\chi^*(z),\quad
 W=A_d/q^{d/2},\quad |W|=1.
\]

If `W=e^{i omega}`, multiplying by `e^{-i omega/2}` makes `p` conjugate-reciprocal (`p_tilde=p_tilde^*`). It does **not** in general make it a real reciprocal/palindromic polynomial. A scalar phase cannot alter its zeros. The functional equation sends the normalized Frobenius multiset to `w -> 1/conj(w)`.

**PROVED finite criterion.** With `r` distinct normalized Frobenius values and their multiplicity weights,

\[
 \bigl(|F_i|=\sqrt q\ \forall i\bigr)
 \iff (T_N\succeq0\ \forall N)
 \iff \text{the moment Schur recursion terminates consistently at }r,
\]

where consistent termination means `|alpha_j|<1` for `j<r-1`, `|alpha_{r-1}|=1`, and all subsequent moments satisfy the annihilating polynomial of the terminal measure. The proof is C1(ii)'s bounded-trace argument with reflection symmetry, followed by the finite Vandermonde/orthogonalization proof of C1(iii). Weil's theorem supplies the left-hand statement for these characters; it is not used to generate the numbers. For squarefree `Lambda`, `r=d` and the brief's parameter inequalities are correct. In that case evaluation of polynomials of degree below `d` at the `d` distinct spectral points is invertible. The reflection-pairing expression from 08b has a negative direction for each off-circle pair, so `T_{d-1}>0` already forces every root onto the circle; the terminal boundary relation then follows. One must not identify a general weighted moment sum with an unweighted Newton sum merely because the first few values agree.

There is a reversal convention to retain: for moments of `F_i/sqrt(q)`, the terminal monic polynomial is the squarefree part of

\[
 \Psi_\chi(z)=z^d\Lambda_\chi(1/(\sqrt q z)),
\]

not `p_chi(z)`. When squarefree its terminal parameter is `-conj(W)`. The measure of **reciprocal** normalized roots has conjugate moments and conjugate Schur parameters; its monic POPUC is `p_chi/W`, with terminal parameter `-W`. For repeated roots use the reduced polynomial and its own constant term; the original root number includes multiplicities. This is why “up to normalization” alone is insufficient for a complex character.

### Exhaustive computation: NUMERICAL, with exact checks

`python3 checks/check_ff_all.py` builds the unit group of **every monic modulus** of degrees one through four over `F_3,F_5`, including reducible moduli and prime powers. It chooses direct cyclic generators of the residue-field units and principal units, lists all characters, and retains those nontrivial on the last conductor kernel at every local factor. It sums `chi(D)` over all monic `D` of degrees below the modulus degree from scratch. It uses neither lane J's L-polynomial table nor roots as input. Integer character exponents are exact; their complex evaluations use IEEE double precision, with 75-decimal recomputation of all early terminations and selected checks. Newton and Levinson give the printed coefficients.

Every character, its modulus, its local generator convention, completed polynomial, and **all** its alpha values is printed in [`checks/output_ff_all.txt`](checks/output_ff_all.txt) (263,694 rows; about 49 MiB). This is the complete requested table, not a sampling of power-residue characters. The short report is [`checks/output_ff_summary.txt`](checks/output_ff_summary.txt). Counts by conductor degree are:

| q | degree 1 | degree 2 | degree 3 | degree 4 |
|---:|---:|---:|---:|---:|
| 3 | 3 | 36 | 324 | 2,916 |
| 5 | 15 | 400 | 10,000 | 250,000 |

As an independent census check, the generating series for primitive-character counts is `(1-qu)^2/(1-q^2u)` (divide the series for all unit-group characters by the monic-divisor series). Thus the degree-one count is `q^2-2q`, and for degree `m>=2` it is `(q-1)^2 q^(2m-2)`, exactly the enumerated counts.

Support-rank counts for the largest degree:

| q | completed degree | rank | characters |
|---:|---:|---:|---:|
| 3 | 2 | 2 | 1,458 |
| 3 | 3 | 3 | 1,458 |
| 5 | 2 | 1 | 30 |
| 5 | 2 | 2 | 62,470 |
| 5 | 3 | 2 | 80 |
| 5 | 3 | 3 | 187,420 |

The smaller-degree cases have full distinct support (or degree zero), as printed in the summary. All computed nonterminal coefficients lie inside the disk and every terminal one lies on its boundary. Maximum functional-equation/terminal numerical defect is `6.93e-15`; the independently computed prime-power logarithmic-derivative identity has defect below `1.56e-13`. The 110 early terminations were all recomputed at 75 digits; these census classifications are numerical, not interval-certified algebraic discriminants. The displayed counterexample above is exact. The two methods agree; neither imports RH or an L-zero list into the computation.

A small exact table, recomputed in `check_ff_examples.py`, illustrates the conventions:

| character | completed polynomial | alpha |
|---|---|---|
| lane J X1: q=5, quartic symbol mod `t^3+t+1` | `1+(-2+i)u+(3-4i)u^2` | `(2+i)/(2sqrt(5)), -(3+4i)/5` |
| repeated example mod `t^4+1` specified above | `(1+(1-2i)u)^2` | `(-1-2i)/sqrt(5)` |

In particular the first X1 parameter has squared modulus `1/4`; the terminal one has modulus one. More examples, including wild conductor `t^3` at `q=3` and `t^4` at `q=5`, are printed in the exhaustive summary and full table.

### C2′: SHARPENED and decided — individual prime data suffice; aggregate prime/squarefree sums do not

**PROVED positive formulation.** Given `q,d,epsilon`, `alpha_k` depends only on `c_1,...,c_{k+1}` and their conjugates. The displayed logarithmic derivative expresses these in the individual values `chi(P)` for `deg P<=k+1`, including powers `chi(P)^r` for `r deg P<=k+1`. Hence it is a rational, triangular transformation of finite prime data. No additional root-number phase is required. The same statement holds for the individual squarefree values, since they include the primes. The coefficients of the **Möbius-weighted** squarefree series also suffice: `sum mu(D)chi(D)u^deg D=1/L(u,chi)` can be inverted to the required degree.

**REFUTED aggregate formulation, even with the same root number.** Unweighted degree sums over primes do not determine the contributions of prime powers. Already

\[
 A_2=\sum_{\deg P=2}\chi(P)
       +\tfrac12\left(\left(\sum_{\deg P=1}\chi(P)\right)^2
                       +\sum_{\deg P=1}\chi(P)^2\right).
\]

The last sum is extra information. Similarly `sum_{D squarefree} chi(D)u^deg D=L(u,chi)/L(u^2,chi^2)` loses the square contributions if the `chi^2` data are omitted.

Exact counterexamples use primitive quadratic characters modulo the following squarefree degree-five polynomials over `F_3`. All have completed degree four and **root number +1**, so a phase cannot repair the discrepancy. The examples were extended to degree five specifically because the degree-two/three functional equations constrain the short census too strongly; no aggregate collision with fixed phase occurred in the degree-at-most-four census.

| information held equal | first modulus f | second modulus f | common sums | alpha_1, first / second |
|---|---|---|---|---|
| prime sums through degree 2 | `t^5+t^4+2t^3+t^2+2t` | `t^5+2t^4+1` | prime degree 1 = -1, prime degree 2 = 1 | `-13/47` / `-21/47` |
| unweighted squarefree sums through degree 2 | `t^5+2t` | `t^5+2t^4+t^3+t^2+2t` | degree 1 = 0, squarefree degree 2 = -2 | `1/3` / `0` |

For the prime pair, the missing linear-prime-square sums are 1 and 3; `alpha_0=sqrt(3)/12` in both. For the squarefree pair those missing sums are 0 and 2; `alpha_0=0`. `python3 checks/check_ff_examples.py` prints the character sums and rational alpha values exactly. Thus Schur coefficients are **not** primitive-cycle counts or a linear prime-degree trace. They are nonlinear functions of the full prime-power moments with multiplicity and parity data.

## 3. C3 — zeta rung: prime-only NUMERICAL tests and conditional theorems

### C3(i): PROVED-conditional (H-RH) positivity; PROVED exact Toeplitz structure without RH

Let `g` be a nonzero compactly supported smooth function of log-coordinate `u`, and put `h=g*g^*`, with `g^*(u)=conj(g(-u))`. Let `U_tg(u)=g(u-t)`, `a=log p`, and

\[
 c_j(p;g)=W(U_{ja}g,g),\qquad T_N=(c_{j-k})_{0\le j,k\le N}.
\]

The convolution of `U_tg` with `(U_tk)^*` equals `g*k^*`. Thus `W(U_tg,U_tk)=W(g,k)` before RH, and this is **exactly Toeplitz**, even at finite support length. There is no Toeplitz-defect limit to repair. If `g` occupies length `L`, the entire family through `N` occupies length `L+N log p`. Clipping all the translates back to a common window destroys this identity; that compressed problem is not used here. The unnormalized prime step is `sqrt(p) U_log(p)` and has multiplier `p`.

The explicit formula implemented here, with `H_t(x)=h(x-t)`, `U=L+|t|`, is

\[
\begin{split}
 c(t)={}&\int_{-U}^{U}2\cosh(x/2)H_t(x)\,dx
 -\sum_{n\le e^U}\frac{\Lambda(n)}{\sqrt n}\{H_t(\log n)+H_t(-\log n)\}\\
 &-(\log(4\pi)+\gamma)H_t(0)
 -\int_0^U\frac{H_t(x)+H_t(-x)-2e^{-x/2}H_t(0)}{e^{x/2}-e^{-3x/2}}\,dx
 +H_t(0)\log\coth(U/2).
\end{split}
\]

Only primes and their powers, the pole, and the archimedean factor enter. This is lane R's formula, independently implemented in `checks/check_zeta.py`; it is also the distribution underlying `zst` and the formula sheet `notes/zeta-spectral-triples/plan.md` §1. We **do not import** `check_window_similitude.py`, since its top level reads a zero file. No zero, zero table, or RH-assuming routine enters either zeta script here.

For computably specified `g`, each finite matrix requires finitely many primes plus ordinary quadrature of smooth integrals with the removable singularity handled as displayed. This means a finite prime computation to any target numerical accuracy; it does not mean that exact semidefiniteness at a zero eigenvalue is decided by finite-precision arithmetic.

**H-RH:** all nontrivial zeta zeros lie on the critical line. Under H-RH the explicit formula identifies the positive finite measure

\[
 \nu_{p,g}=\sum_{\rho=1/2+i\gamma}m_\rho|\widehat g(\gamma)|^2
                \delta_{\exp(i\gamma\log p)},\qquad
 c_j=\int w^j\,d\nu_{p,g}(w).
\]

Multiplicity is counted once via `m_rho`; the sum is over distinct zeros in this notation. Hence `T_N>=0` for all `N,g`. Conversely requiring this for every `g`, already at `N=0` and over all support lengths, is Weil's positivity criterion, not an independently easier RH proof.

**SHARPENED rank statement under H-RH.** Every nonzero compactly supported smooth `g` gives infinitely many distinct atoms, and hence `T_N>0` for every finite `N`. No assumption of pairwise nonresonance of ordinates modulo `2pi/log p` is needed. Indeed a nonzero compact-support Fourier transform is an entire function of exponential type and has `O(T)` zeros in a disk of radius `T` (Jensen's inequality, after choosing a nonzero center). There are `>>T log T` distinct simple critical zeros, by the known positive-simple-proportion theorem. Removing the `O(T)` zeros of `g_hat` still leaves that many ordinates. A fixed finite collection of residue classes modulo `2pi/log p` contains only `O(T)` distinct ordinates. This contradiction excludes finite support. Pairwise collisions can occur without affecting this argument. The simple-proportion input is classical; see [Conrey, *More than two fifths of the zeros of the Riemann zeta function are on the critical line* (1989), Introduction](https://aimath.org/~kaur/publications/24.pdf). For a curve the corresponding rank is the number of distinct weighted Frobenius points, **at most** `2g`, with equality only under the relevant distinctness hypothesis. This sharpens the rank wording in the requested Carathéodory–Toeplitz adjudication.

Without positivity we have the exact sequence of finite Toeplitz forms, but not automatically a positive circle symbol or even a distributional symbol for all shifts: exponentially growing moments need not be Fourier coefficients of a distribution. The positive symbol above is explicitly conditional on H-RH.

### C3(ii): NUMERICAL convergence for a specified probe; REFUTED universal probe independence

A growing window does not specify a sequence of test functions. To make the question determinate, the main experiment uses

\[
 g_{L,\tau}(u)=e^{-u^2/(2\tau^2)}\eta(2u/L),
\]

where `eta(x)=1` for `|x|<=1/2`, zero for `|x|>=1`, and for `s=2|x|-1` between zero and one,

\[
 \eta(x)=\frac{e^{-1/(1-s)}}{e^{-1/(1-s)}+e^{-1/s}}.
\]

These are actual `C^infinity` compact windows. A second shape is `b_L(u)=exp(1-1/(1-(2u/L)^2))` inside the support, zero outside. All tables are normalized by `c_0` when computing alpha, so changing the overall amplitude cannot explain the differences.

Here are all eight parameters at `L=0.4, tau=0.1` for the compact Gaussian cutoff. Every row is prime-only, with `N=8`:

| p | alpha_0 | alpha_1 | alpha_2 | alpha_3 | alpha_4 | alpha_5 | alpha_6 | alpha_7 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | -.821215964 | -.529390257 | -.211390092 | -.316740817 | .004893159 | -.718724096 | .285682627 | -.441783561 |
| 3 | -.876784648 | -.415021641 | -.523178088 | -.054511958 | -.174464927 | -.658786009 | -.030364242 | -.750598495 |
| 5 | -.722198240 | -.938906454 | .203496957 | -.577340533 | -.280267872 | .359425540 | -.095231104 | -.425480897 |
| 7 | -.728208573 | -.850077487 | -.114877765 | -.246411988 | -.718386185 | .270987796 | -.536843548 | -.131367450 |

At fixed `g`, `alpha_k` uses only moments through `k+1`; increasing `N` beyond that point does not change it at all. Thus there is no nontrivial convergence in `N` for a fixed index. The changing objects are the new tail coefficients and prediction-error products. Dependence on support length for the specified cutoff sequence (`tau=0.1`) is:

| L | alpha_0(2) | alpha_0(3) | alpha_0(5) | alpha_0(7) |
|---:|---:|---:|---:|---:|
| .4 | -.821215964 | -.876784648 | -.722198240 | -.728208573 |
| .8 | -.880395130 | -.939313731 | -.728452750 | -.730909900 |
| 1.2 | -.877321484 | -.936834978 | -.728940736 | -.731882889 |
| 1.6 | -.877354040 | -.936855544 | -.728935609 | -.731883261 |
| 2.4 | -.877354040 | -.936855596 | -.728935624 | -.731883191 |

The Gaussian limit is checked independently at 60 decimal digits by `check_zeta_gaussian.py`. It uses the analytic autocorrelation `h(x)=tau sqrt(pi) exp(-x^2/(4tau^2))`, the exact pole integral, a finite prime sum, and an explicit bound on the omitted Gaussian prime/archimedean tails. The first six limiting parameters at `tau=0.1` are:

| p | alpha_0 | alpha_1 | alpha_2 | alpha_3 | alpha_4 | alpha_5 |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | -.877354040133 | -.733458502258 | -.469501256004 | -.826508508579 | -.182908217450 | -.993611943143 |
| 3 | -.936855595506 | -.638699808629 | -.821302118023 | -.966190590119 | -.427973751449 | -.664259686923 |
| 5 | -.728935623578 | -.996514722742 | .026527175587 | -.592720888745 | -.717839832798 | -.987643008421 |
| 7 | -.731883191482 | -.946566743302 | -.511288058000 | -.374297144487 | -.982101601618 | -.256177923024 |

The limit depends strongly on the probe. At `p=2`, Gaussian widths `tau=.04,.07,.10` have respectively

\[
 \alpha_0=-.499631848644198,\quad -.731119471406270,\quad -.877354040133073.
\]

All three are independent prime-side computations. Even at the same finite support length `.4`, replacing the cutoff Gaussian by the compact bump changes `alpha_0(2)` from `-.821215963568` to `-.838807825762`. The full bump tables for all four primes and both lengths `.4,.8`, and all Gaussian tables, are in `checks/output_zeta.txt` and `checks/output_zeta_table.txt`.

**PROVED-conditional fixed-probe limit.** If `g_L` converges to a fixed Gaussian as above, its transforms converge with uniform rapid-decay bounds in the critical strip. The zero-sum formula (without putting any zero values into computation) therefore gives convergence of each moment. Alternatively use continuity of the explicit-formula distribution on this test-function class. Every finite nonsingular Toeplitz block has Schur parameters rationally continuous in these moments. Thus its coefficients converge; under H-RH all fixed Gaussian blocks are strictly positive. This is convergence to the chosen **global** weighted zeta spectrum, not to a local factor. The numerical results above test precisely this assertion.

**REFUTED uniformity over probes/windows.** Under H-RH, take a compact smooth window expanded and modulated so its Fourier transform concentrates at one fixed zero ordinate. After normalizing `c_0`, its measures approach the single circle atom at that ordinate modulo `2pi/log p`; then `|alpha_0|` approaches one. This is a theoretical counterexample, not a computation using a zero. Therefore no bound `|alpha_k(p;g)|<=1-delta`, with a positive delta independent of `g` and window size, can hold. Allowing arbitrary expanding probes can also destroy convergence by alternating two different cutoff families. Whether a particular fixed infinite sequence has `sup_k|alpha_k|<1` is a separate question; these experiments do not decide it.

The “local factor only” proposal has no surviving probe-independent meaning. In the prime expression, each moment receives **all** prime powers with `|log n-j log p|<L`, along with pole and archimedean terms. A narrow window can make the contribution at `n=p^j` dominant, but dominance is not equality and is not preserved by increasing `L` or `j`. The corrected limit is the pushforward of the global spectral measure displayed above. Its detailed `p` dependence is global sampling at step `log p`, not a demonstrated Euler-factor law.

### Numerical precision and Toeplitz defect

The compact computation convolves sampled smooth windows by FFT and evaluates the resulting autocorrelation spline with composite Gauss–Legendre quadrature. It compares 4,096 versus 8,192 subdivisions and 32 versus 48 quadrature nodes per panel. These are convergence checks, **not certified enclosures**. No prime-tail approximation is made for the compact functions. Across the 36 tested `(shape,L,tau,p)` cases, the largest observed moment change is `1.82e-11`, and all size-nine matrices have positive numerical minimum eigenvalues; the smallest is `1.65e-9`. In the `L=.4` primary table, the largest alpha change is below `2.8e-11`. Ill-conditioned late coefficients of the wider `tau=.1` probes amplify small errors: the worst observed alpha change is `2.01e-4`. Those late compact-window digits are diagnostic output, not claimed accurate to all printed digits. The main late-coefficient table above instead uses the high-precision Gaussian calculation.

The matrices built as `T[j,k]=c[j-k]` have zero Toeplitz-part residual exactly by construction and by the proved identity. Independent reevaluation using literal differences `j log p-k log p` gives sampled entry discrepancies below `6.3e-15`; this is roundoff, not a window defect. We do not reinterpret that sampled maximum as a measured norm of an independently computed entire matrix.

For the supplementary Gaussian computation, `U=j log p+20 tau`. The prime tail is bounded using `Lambda(n)<=log n` and the decreasing-tail integral of

\[
 f(x)=\log x\,x^{-1/2}\tau\sqrt\pi\exp[-(\log x-t)^2/(4\tau^2)].
\]

The sum past `X=floor(exp U)` is at most `f(X)+int_X^infinity f(x)dx`, with an analogous `-t` term; completing the square gives the `erfc` formula implemented in the script. The archimedean Gaussian tail has the corresponding exponential bound. The printed maximum analytic tail bound at `tau=.1` is `2.16e-42`; the narrower `.04` case has bound `1.76e-34`. The integrals use 60-digit mpmath quadrature, so these bounds enclose truncation, not quadrature error. Extra precision/reintegration checks are recorded in the validation output. This Gaussian is a limit/comparison probe; it is not represented as a finitely supported function.

### C3(iii): PROVED-conditional (H-RH) — the Szegő product is zero

Normalize `nu_{p,g}` to mass one. Szegő's theorem states

\[
 \prod_{k=0}^{\infty}(1-|\alpha_k|^2)
   =\exp\int_0^{2\pi}\log w(\theta)\,\frac{d\theta}{2\pi},
 \qquad d\nu=w\,\frac{d\theta}{2\pi}+d\nu_s.
\]

The theorem includes the value zero when the log integral is minus infinity; see [Simon–Zlatoš, *Higher-Order Szegő Theorems*, (1.5)](https://mathweb.ucsd.edu/~zlatos/Papers/sz_2004.pdf). Under H-RH the measure here is **pure point**, even if its atoms are dense and even if some phases collide. Thus `w=0` almost everywhere and the product is **zero for every p and every nonzero admissible probe**. If the support were finite, the terminal factor already makes it zero. This rejects the proposed nonzero local factor and supplies a theorem stronger than a numerical guess. The product always has a nonnegative limit whenever all its factors are in `[0,1]`; its zero value expresses singularity of the symbol and is not special to zeta or an additional arithmetic invariant.

The prime-only Gaussian experiment (`tau=.1`) records `P_N=prod_{k=0}^{N-1}(1-|alpha_k|^2)=h_N/c_0`:

| N | p=2 | p=3 | p=5 | p=7 |
|---:|---:|---:|---:|---:|
| 2 | .106384341886 | .072410193666 | .003261077486 | .048297381155 |
| 4 | .026280396486 | .001566622323 | .002113913507 | .030674152023 |
| 6 | .000323491746 | .000715031340 | .000025166147 | .001016793753 |
| 8 | .000265877672 | .000084426006 | — | — |
| 10 | .000001155808 | — | — | — |
| 12 | .000000189300 | — | — | — |
| 14 | .000000151085 | — | — | — |
| 16 | .000000000314 | — | — | — |

The compact tables also print products through `N=8` for every `p`, with the error qualifications above. The finite data support decreasing prediction error; they do not prove an unconditional infinite product statement. **Corrected conjecture (OPEN without RH):** for each specified nonzero compact smooth probe, all prime-side Toeplitz blocks are positive and their normalized prediction errors tend to zero. Under H-RH both assertions are proved above. There is no surviving nonzero Euler-factor conjecture, and no canonical limit sequence without fixing the probe.

## Correction ledger

| item in brief / record wording | correction and status |
|---|---|
| the two graph roots are `mu,bar(mu)` | **PROVED correction:** outside the band they are two distinct real reciprocal roots; conjugation is the wrong notation there |
| `M=[[A,-q],[1,0]]` and the record's label map | **PROVED correction:** the original edge-label convention has `M_0=[[0,-1],[q,A]]`; use the stated symplectic conjugacy and keep the sign/orientation of the Casoratian explicit |
| the edge-label span has dimension `2n` | **PROVED correction already in tutorial:** its rank is `2n-1` or `2n-2`; Omega lives on labels |
| semidefinite energy iff rotation | **REFUTED:** endpoints give parabolic Jordan blocks and a degenerate energy; only the open band gives a rotation |
| full graph polynomial is a POPUC with `2n-1` interior parameters | **REFUTED by K4:** trivial roots must be removed, then repeated points still force earlier termination |
| curve/character Toeplitz rank equals degree | **REFUTED by t^4+1 at q=5:** rank counts distinct weighted points; multiplicities are weights |
| 08b's form is twice any lattice Weil form | **SHARPENED:** twice the trace-oriented `Omega_+` form under the cyclic map, with its invertibility/reduced-algebra qualifications |
| Szegő Casoratian is exactly `1-|alpha|^2`; Omega is its `k=0` instance | **SHARPENED:** the alternating multiplier is `z(1-|alpha|^2)`; the Hermitian multiplier on the circle omits `z`; the two evolution indices are different |
| Schur–Cohn coefficients of the characteristic polynomial equal moment Verblunsky coefficients | **REFUTED:** different algorithms and inputs; self-reciprocal polynomials are already on the polynomial test's boundary |
| even primitive L has no trivial root | **REFUTED:** divide raw L by `1-u`; the completed log trace contains the extra `+epsilon` before the minus sign |
| phase normalization makes complex-character p real reciprocal | **REFUTED:** it makes p conjugate-reciprocal; the moment POPUC uses the reversed polynomial or conjugate moments |
| alpha is a sum of prime/squarefree degree counts | **REFUTED in that aggregate sense:** prime-power values or Möbius-weighted data are needed; the precise individual-prime formulation is proved |
| a translate Gram matrix is only approximately Toeplitz | **REFUTED for uncut translates:** exact before RH; edge compression is a separate operation |
| zeta full rank needs all aliased phases pairwise distinct | **SHARPENED under H-RH:** infinitely many distinct surviving phases suffice, and follow for compact smooth probes from exponential type and the positive simple-zero proportion |
| growing L defines a unique Schur limit, uniform over probes | **REFUTED:** a probe family must be specified; normalized coefficients retain probe dependence and can approach the disk boundary |
| the infinite Szegő product might be `1-1/p` | **REFUTED under H-RH:** the positive symbol is pure point, so its product is zero |

## Numerical checks for the blind lane

Run commands from `notes/astra-2026-10-23/canonical/` (the scripts also work with absolute paths from any directory). Every quoted numerical result comes from these scripts; none requires a zero file.

1. `python3 checks/check_graph.py`: retained `K4` gives `alpha_0=-sqrt(2)/4`, `alpha_1=-1`. Keeping its trivial pair instead gives `[0,-1/4,4sqrt(2)/5]` through failure.
2. `python3 checks/check_graph.py`: the same four out-of-band modes in prisms `m=16,17` first fail at indices `13,8`, with exact values `43707967/3998190` and `-413023893 sqrt(2)/312857602`.
3. `python3 checks/check_ff_examples.py`: for `q=5`, quartic symbol modulo `t^3+t+1`, `Lambda=1+(-2+i)u+(3-4i)u^2` and `alpha_0=(2+i)/(2sqrt(5))`, with squared modulus `1/4`. It also prints the exact repeated-root discriminant and the C2′ counterexamples.
4. `python3 checks/check_zeta.py`: for `p=2`, the specified compact cutoff window `L=.4, tau=.1`, `c_0=.0343767341909677`, `c_1=-.0282307228929465`, hence `alpha_0=-.821215963567708`. The translated span through `N=8` occupies total log-length `.4+8 log 2`.
5. `python3 checks/check_zeta_gaussian.py`: for the Gaussian limit `tau=.1,p=2`, `c_0=.0188116068964750446097537528963`, `alpha_0=-.8773540401330732165071981`, and `P_16=3.138642811395271634818009e-10`. The first five moments at all four primes agree after 60-to-80-digit reintegration to within `1.865e-60`.
6. `python3 checks/check_ff_all.py`: exactly `263694` primitive characters; all coefficient rows are written to `checks/output_ff_all.txt`. Degree-four rank drops at `q=5`: 30 degree-two polynomials and 80 degree-three polynomials. No other rank drops occur in this census.

The saved outputs are `output_graph.txt`, `output_ff_summary.txt`, `output_ff_all.txt`, `output_ff_examples.txt`, `output_zeta.txt`, `output_zeta_table.txt`, and `output_zeta_gaussian.txt`. The graph identities and displayed function-field counterexamples are exact; the full character census and compact zeta tables are numerical with the precision checks stated above. The high-precision Gaussian prime tails have explicit analytic bounds; its quadrature checks are not a full ball-arithmetic certificate.

## What this changes in the notebook

No registered row, existing record page, or global worklog was edited. Proposed rows for a later independent REFUTE review:

| candidate id | proposed statement | lane status |
|---|---|---|
| `prop:graph-trace-schur-support` | retained Ihara trace positivity is Ramanujan; Schur length is distinct spectral support, with multiplicity weights | **PROVED**; packages 08b with standard OPUC, not a new RH mechanism |
| `prop:casoratian-szego-conformal` | graph Abel and Szegő determinant identities share a two-dimensional conformal alternating form; the raw Szegő multiplier includes z | **PROVED**; explicit distinction of evolution variables |
| `obs:schur-failure-not-mode-count` | first failed moment coefficient is not determined by the number of out-of-band graph modes | **PROVED** by two exact prisms |
| `prop:ff-schur-logtrace` | completed character logarithmic traces give Toeplitz/Schur RH criterion; termination uses distinct roots and the complex reversal convention | **PROVED**, with Weil RH cited as an existing theorem |
| `prop:ff-prime-aggregate-insufficient` | individual prime values determine early Schur coefficients; unweighted aggregate prime/squarefree sums do not, even with fixed root number | **PROVED** with exact quadratic counterexamples |
| `num:ff-all-small-conductors-schur` | all primitive characters over F_3,F_5 through conductor degree four, including wild characters | **NUMERICAL**, 263694 printed rows |
| `prop:zeta-schur-purepoint-product` | for each nonzero compact smooth probe, under H-RH the translate measure has infinite support and its Szegő product is zero | **PROVED-conditional (H-RH)**; uses standard OPUC and the established simple-zero proportion |
| `num:zeta-prime-schur-probes` | exact Toeplitz translate structure; prime-only coefficients vary with the probe and converge for the specified cutoff family | exact identity **PROVED**; tables **NUMERICAL**; positive limiting symbol **PROVED-conditional (H-RH)** |

The one-line annotation requested for `graph-ihara.md` §8 item 2 and §9 is:

> **Omega is the Casoratian, Q = ½Omega(M − qM^{-1}).** The latter is the symmetric recurrence energy; use the page's label convention and distinguish strict rotation from parabolic endpoints.

Additional short annotations would be useful in lane J (remove the even factor; Schur rank counts distinct points), lane R and its adjudication (exact translates are Toeplitz; full rank requires infinite support, not pairwise nonresonance), and the data ladder (the moment quotient is the reduced cyclic spectral algebra, not the full geometric H¹ when eigenvalues repeat).

**Are Schur coordinates the missing “finite rank per mode” datum? No.** Together with `c_0` they are invertible coordinates on a positive moment functional. Finite support gives terminal degeneration and a finite cyclic quotient; multiplicities survive as masses but Jordan structure and integral lattice classes do not. Different spectral probe weights change the parameters. On the zeta rung, under H-RH the compact-window sequence is infinite and never terminates, while its product tends to zero. A two-by-two transfer presentation at every recursion degree does not make the spectral space two-dimensional, nor supply an integral lattice, a polarization, or a geometric proof of positivity. These coordinates are constructive diagnostics for the counts and conditioning, not the missing arithmetic structure.

The next mathematical step is a prime-side description of quantitative lower bounds for finite prediction pivots for a **specified** probe family, or of their decay rates. The universal positive limit/Euler-factor proposal has been eliminated. Any such bounds must retain the global prime-power and archimedean data; a future arithmetic explanation would need extra structure beyond the Schur reparameterization itself.
