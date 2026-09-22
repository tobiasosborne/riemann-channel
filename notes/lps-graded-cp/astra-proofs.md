# Graded CP transport for the (13, 17; 5) LPS square complex

Author: `codex:gpt-6-astra`

## Claim ledger

| Claim | Verdict | Statement |
|---|---|---|
| G1 | PROVED / SHARPENED | The P letters give two unsigned even blocks and two signed odd blocks; coherences vanish. The exact divisor is 2 nu_* - 2 iota_* nu_*. |
| G2 | REFUTED / OPEN | The two-register and Bass identifications fail. No exact-family construction or unrestricted no-go theorem is established; necessary cancellation bounds are explicit. |
| G3 | PROVED / REFUTED | The actual channel has P-mode 17, two fixed states and odd period modes; it is not a mixing expander. Parity covariance already admits homogeneous Kraus letters. |
| G4 | REFUTED / PROVED | The CP memory transfer is not HS self-adjoint. Its signed blocks contain Bass companions; the strict metric criterion and nonstrict circle criterion differ at Jordan endpoints. |
| G5 | SHARPENED / OPEN | The signed walk is a genuine odd CP subblock with compulsory extra modes; the completed Deninger divisor remains spectral, with its inverse CP problem open. |

## Corrections to the brief

| ID | Correction | Status |
|---|---|---|
| C1 | Arc compatibility must accompany the exclusion of reversal; an 18-letter bouquet is not the square graph. | PROVED, G1.1 |
| C2 | P is an even letter; X is odd but gives identical sector spectra and zero net divisor. | PROVED, G1.2 |
| C3 | The canonical orientation signs are gauge-equivalent to a minus sign on every square edge. | PROVED, G1.3 |
| C4 | The actual P-letter divisor has multiplicity two and loses every sign-symmetric part of the target; it cannot be repaired by a Bass factor. | PROVED, G1.4 |
| C5 | For the spectral pair, sdet is (1-u^2)^(-5760)/Z; its reciprocal is (1-u^2)^5760 Z. | PROVED, G2.1 |
| C6 | Two independently supported registers do not put one population walk in the odd doubled sector. | REFUTED prescription, G2.2 |
| C7 | The graded permutation and renewal-network theorems do not give the requested exact CP divisor. | SHARPENED, G2.3 |
| C8 | Failure of the proposed family does not prove nonexistence among all homogeneous Kraus families. | OPEN, G2.4 |
| C9 | Adjoint-paired adjacency can be HS self-adjoint while its non-backtracking transfer is not. | REFUTED inference, G4.1 |
| C10 | Circle roots require a closed band; a positive metric for this companion requires the strict band. | PROVED, G4.3 |
| C11 | Parity-covariant CP maps already have homogeneous Kraus presentations. | PROVED, G3.2 |
| C12 | A net-divisor Ramanujan property does not imply a unique fixed state or an odd mixing gap. | REFUTED inference, G3.1 |


## G1 — PROVED / SHARPENED: the exact square-walk CP transfer

### G1.1 Finite matrices and the register

Write `q=17`, `d=18`, `r=15120`. Let `A` be the directed arcs of the signed graph `G_e`: two arcs for each of its 7560 squares-as-edges. For an arc `i`, write `t(i),h(i),bar(i),s_i` for tail, head, reversed arc and sign; `s_bar(i)=s_i`. Set

\[
 C_{ji}=\mathbf1_{h(i)=t(j)}\mathbf1_{j\ne\bar i},\qquad
 B=C\operatorname{diag}(s_i),\qquad W_{ab}=\#\{i:t(i)=a,h(i)=b\}.
\]

Thus `C=|B|` entrywise, and `B` is a departure-weight convention for `B_e`. Arrival weighting is similar to it by the diagonal sign matrix, so all determinants and traces agree. Both row and column sums of `C` are 17. The head-tail condition is essential: merely `j != bar(i)` on 15120 letters would give degree 15119 and a different graph.

On `H=C^{1|1} tensor C^r`, parity `P_H=P tensor I_r`, define the **257040** homogeneous, even Kraus matrices

\[
 A_{ji}=U_i\otimes |j\rangle\langle i|,
 \quad C_{ji}=1,\qquad
 U_i=\operatorname{diag}(1,s_i)\in\{I,P\}.
 \tag{1}
\]

Each is a `30240 x 30240` matrix. The counting transfer is `E(Z)=sum A_ji Z A_ji^*`; divide the letters by `sqrt(17)` for the bistochastic channel `E/17`. Indeed both `sum A A^*` and `sum A^* A` equal `17 I_H`.

This uses the smallest register **in this faithful arc-register construction with only the two-dimensional transport bond**: each Pauli component must carry the invertible `r x r` Hashimoto matrix, so a smaller diagonal register cannot have its nonzero spectrum with its multiplicities. This is not a minimum theorem among all possible CP realizations. An 18-direction memory would also need a position space and its permutation transport; 17 counts allowed continuations, not directions. The Kraus rank of (1) is exactly 257040: its nonzero Kraus vectors are pairwise Hilbert--Schmidt orthogonal (distinct register matrix units), hence the Choi matrix has this rank. No shorter Kraus list represents this same full CP map.

### G1.2 The sectors, including all coherences

For an arbitrary register matrix unit,

\[
 E(Z\otimes |k\rangle\langle l|)
 =\delta_{kl}\sum_{j:C_{jk}=1}U_k ZU_k^*\otimes |j\rangle\langle j|.
 \tag{2}
\]

Proof: the left register multiplication requires `i=k` and the right one requires `i=l`. This uses only the separate Kraus labels `(j,i)`, not genericity of `U_i`. Every off-diagonal register coherence is killed in one step; the diagonal-register algebra is invariant, with

\[
 (EZ)_j=\sum_i C_{ji}U_i Z_iU_i^*.
\]

In the Pauli basis, `Ad U_i` is `diag(1,1,s_i,s_i)` on `(I,P,X,Y)`. Therefore, as **full sector matrices**,

\[
 E_0\simeq C\oplus C\oplus0_{2r(r-1)},\qquad
 E_1\simeq B\oplus B\oplus0_{2r(r-1)}. \tag{3}
\]

Each full sector has dimension `2r^2=457228800`; each diagonal sector has dimension `2r=30240`; each killed coherence sector has dimension `2r(r-1)=457198560`. There are no additional zero eigenvalues in the diagonal sectors: Bass's formula, or reversal on the degree-18 arc space, makes `B,C` invertible. In particular `nu(0)=0` for this balanced bond.

For the alternative `U_i=X` at negative arcs, `Ad X` fixes `I,X` and negates `P,Y`. Consequently both sectors are `C op B op 0`, their supertrace is zero for every positive power, and the entire graded divisor is zero. An odd physical letter does not automatically put a signed walk wholly in the odd doubled sector. With P letters, the *relative phase* carries the sign; their letter parity is always even.

### G1.3 In this example the sign is a length parity, up to gauge

Both color graphs have the determinant-character bipartition, because 13 and 17 are nonsquares modulo 5. Orient every horizontal edge from the positive to the negative class. A vertical step reverses this class, so the transport of the chosen horizontal orientation across any square is the negative of the chosen orientation at its opposite edge. Thus in this orientation **every edge of `G_e` has sign -1**.

In the canonical orientation of the script, let `z_a` be the determinant character of the tail of the chosen horizontal edge `a`. Then

\[
 (T_1)_{ab}=-z_a W_{ab}z_b,
 \qquad s_i=-z_{t(i)}z_{h(i)}.
\]

For `D_A=diag(z_{t(i)})`, direct substitution gives `D_A B D_A=-C`. Hence, with `c_n=Tr C^n`, `b_n=Tr B^n`,

\[
 b_n=(-1)^n c_n,\quad
 \operatorname{Tr}E^n=2(c_n+b_n),\quad
 \operatorname{Str}E^n=2(c_n-b_n).
 \tag{4}
\]

There is also an exact graded-unitary normal form: conjugate the bond by `G_H=sum_i diag(1,z_t(i)) tensor |i><i|`. The new transition transport is `diag(1,z_t(j) s_i z_t(i))=P` whenever `C_ji=1`. Thus the map is graded-unitarily equivalent to `Ad(P) tensor Phi_C`, where `Phi_C` is the scalar register channel with Kraus matrices `|j><i|` for the allowed transitions.

Equivalently a closed walk has sign `(-1)^n`. The ordinary trace is four times the even-length walk count, and the supertrace is four times the odd-length walk count. In a closed Kraus word the register trace is one and its transport is `I` or `P`; `|Tr(PU_w)|^2` is respectively zero or four, which proves the ring-norm formula directly. This is a squared amplitude, not the signed trace `b_n` (already `b_3=-10080<0`). The label `def:parity-twisted-tp` defines signed **unitality**, not an alternative trace that could remove this square.

### G1.4 Exact moments and net divisor

For any signed or unsigned degree-18 adjacency `A_v` on `v` vertices and `m` edges, put

\[
 p_0(x)=2,\quad p_1(x)=x,\quad
 p_n(x)=xp_{n-1}(x)-17p_{n-2}(x).
\]

The signed Bass identity gives the finite, integer computation

\[
 \operatorname{Tr} B_{A_v}^{\,n}=\operatorname{Tr}p_n(A_v)
 +(m-v)(1+(-1)^n). \tag{5}
\]

The script in `checks/exact_transport.py` reconstructs the squares and evaluates (5) using integer sparse matrices; it does not approximate the roots. The results are:

| n | Tr B_v^n | Tr B_e^n | Tr C^n | Tr E_0^n | Tr E_1^n | Tr E^n | Str E^n | target N_n |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11520 |
| 3 | 0 | -10080 | 10080 | 20160 | -20160 | 0 | 40320 | 10080 |
| 4 | 176400 | 61200 | 61200 | 122400 | 122400 | 244800 | 0 | 126720 |
| 5 | 0 | -1209600 | 1209600 | 2419200 | -2419200 | 0 | 4838400 | 1209600 |
| 6 | 48077280 | 24202080 | 24202080 | 48404160 | 48404160 | 96808320 | 0 | 23886720 |

Let `Q_u(A)=I-uA+17u^2 I`, let `Z` denote the **completed** worked-example zeta, and set

\[
 \nu_*=[1]+[17]-\sum_{\alpha\in\operatorname{spec}F_1}[\alpha],
 \qquad \iota(\lambda)=-\lambda.
\]

Both sector Bass exponents are `2*6720=13440`. They cancel, giving exactly

\[
 Z_E(u):={1\over\operatorname{sdet}(1-uE)}
 =\left({\det Q_u(T_1)\over\det Q_u(W)}\right)^2
 =\left({Z(u)\over Z(-u)}\right)^2,
 \qquad \boxed{\nu_E=2\nu_*-2\iota_*\nu_*}. \tag{6}
\]

The last equality uses `W ~ -T_1` and the bipartite symmetry `det Q_u(-T_0)=det Q_u(T_0)`. Equivalently `Str E^n=2(1-(-1)^n)N_n` for all `n>=1`. The structural nonzero divisor is

\[
 2[17]+2[1]-2[-17]-2[-1],
\]

and the remaining divisor is `-2 spec(F_1)+2 spec(-F_1)`, with algebraic multiplicities. For a root `alpha` of `x^2-tx+17`, its exact coefficient is

\[
 \nu_E(\alpha)=2m_T(-t)-2m_T(t), \tag{7}
\]

with absent multiplicities zero. For example the roots at `t=+7,-7` disappear entirely (both adjacency multiplicities are 4), whereas the target has coefficient -4 at each. At `t=2` the coefficient is +114, rather than -20; at `t=-2` it is -114, rather than -77. Thus neither a factor supported at `+/-1` nor equal modes added to both sectors can repair (6).

Sources: `notes/deninger-lps/astra-proofs.md:263-319`; `notes/reviews/deninger-lps-2026-09-22.md:105-111`; `notes/deninger-lps/src/lps-deninger-worked-example.md:320-443`; `scripts/lps_square_complex.py:91-206,228-243,327-355`; `report/sections/02h_definitions_graded_ramanujan.tex:19-57`; `report/sections/03b_graded_permutation.tex:155-210`; `report/sections/08_quantum_ihara_general.tex:24-46,100-110`.


## G2 — REFUTED candidates; OPEN exact inverse CP problem

### G2.1 What the spectral two-register construction actually proves

On a **graded vector space**, declare `B_v` even and `B_e` odd. This is a legitimate finite graded spectral transfer `L=B_v op B_e`, with dimensions `(2160,15120)`. Its determinant identities are

\[
 \operatorname{sdet}(1-uL)
 ={\det(1-uB_v)\over\det(1-uB_e)}
 =(1-u^2)^{-5760}{\det Q_u(T_0)\over\det Q_u(T_1)}
 ={(1-u^2)^{-5760}\over Z(u)},
\]
\[
 {1\over\operatorname{sdet}(1-uL)}=(1-u^2)^{5760}Z(u),\qquad
 \nu_L=\nu_*-5760([1]+[-1]). \tag{8}
\]

The ordinary Bass exponents are 960 and 6720, whose difference is **-5760 in the superdeterminant**. The completed zeta is obtained by multiplying the raw ring zeta by `(1-u^2)^(-5760)`, or adding `5760([1]+[-1])` to its divisor. The first proposed expression in G2 interchanges numerator and denominator; the second has the exponent reversed.

Designated trivial divisors, with multiplicities, are:

* completed spectral transfer: `nu_triv,*=[17]+[1]`; its retained divisor is `-spec F_1`;
* raw spectral pair: `nu_triv,L=[17]+[1]-5760([1]+[-1])`; its retained divisor is again `-spec F_1`;
* actual P-letter CP transfer: `nu_triv,E=2[17]+2[1]-2[-17]-2[-1]`; its retained divisor is `-2 spec F_1+2 spec(-F_1)` after net cancellation.

Thus `S_triv` is respectively `{1,17}`, `{-1,1,17}`, and `{-17,-1,1,17}`, but these supports alone omit essential signed multiplicities. In (8), the designated H^0 contribution `+[1]` is recorded separately from the topological contribution `-5760[1]`. These are exact structural designations, not permission to delete other modes. The term “retained part plus poles” in the brief means the completed divisor `nu_*`; literally, under the notebook definition the retained divisor has already removed those designated poles.

The spectral pair is not the two full `End(H)` sectors: their dimension difference would be `-12960`, whereas that difference must be a square. Additional zero modes could fix this dimension mismatch; (8) supplies neither such a CP extension nor a proof that one is impossible.

### G2.2 Why the two registers and the balanced Bass theorem do not supply a channel

**Step 1 (direct sum of bonds).** Put `H=H_v op H_e` with opposite bond parities and use separate Kraus families supported on the two summands. Both population algebras `End(H_v)` and `End(H_e)` are **even**. Cross coherences are odd and are killed by all these separately supported letters. Both population walks contribute positively. Changing the parity of an entire summand does not change the parity of its endomorphisms.

If instead one directly sums the actual signed CP construction (1) with an ungraded vertical walk channel, its nonzero net divisor is `spec B_v+2 spec C-2 spec B_e`; mixed coherences again vanish. This still has the unwanted unsigned population spectrum and wrong multiplicities. If two CP transfers are tensored, their supertraces multiply and their eigenvalues multiply; they do not give a difference of the two walk traces. Merely specifying a `C^{1|1} tensor C^{1|1}` bond is therefore not the asserted construction. This refutes those operations, not every possible coupled Kraus family on a larger bond.

**Step 2 (Bass exponent).** For a genuine unitary, degree-18 graded Hashimoto family on `C^{a|b}`, the notebook's theorem gives superdeterminant exponent

\[
 {18-2\over2}(n_0-n_1)=8(a-b)^2\ge0,
 \quad n_0=a^2+b^2,\ n_1=2ab. \tag{9}
\]

Its ring-zeta exponent is the negative of this, and it vanishes for balanced grading. The proposed raw graph-pair exponent would require `n_0-n_1=120-840=-720`. It cannot be the full-sector exponent in (9). The 5760 is the difference of two *different graph* Euler characteristics, not a balanced doubled-bond dimension. Adjacency quadratics at `+/-18` can also contribute roots at `+/-1`, so (9) alone is not an obstruction after arbitrary additional spectra and cancellations. It does refute the claimed direct application of that theorem.

### G2.3 The cited devices preserve the distinction

The graded-permutation theorem first discusses the *single* permutation's supertrace and its signed determinant. Its subsequent word formula explicitly changes this to a **sum of squared amplitudes** on the doubled bond; one letter yields `|str P^n|^2`, and parity-separating letters kill the odd sector. It is not a theorem that an arbitrary signed linear determinant is a CP ring zeta. Equation (2) is the required calculation in the present case.

The renewal construction is genuine CP, but has even sector `1 op E_reset` and odd sector `Z op bar Z`. Its extra population eigenvalues are part of its theorem, not optional corrections. Substituting a conjugation-closed `F_1` as the odd contraction would give the doubled multiplicity; choosing half its complex spectrum can avoid that particular doubling but does not prescribe the reset spectrum. Also `F_1` in the counting metric is not a contraction; a similarity and scale must be specified before invoking that construction. The companion-matrix determinant theorem and the scattering superdeterminant are spectral identities, and do not solve these population constraints.

### G2.4 Necessary conditions for an exact family, with cancellations quantified

Suppose a finite CP map on `End(C^{a|b})` has precisely `nu_*` as its **nonzero** divisor. For every nonzero eigenvalue its sector multiplicities necessarily have the form

\[
 m_0(\lambda)=m_{[1]+[17]}(\lambda)+c(\lambda),\qquad
 m_1(\lambda)=m_{\operatorname{spec}F_1}(\lambda)+c(\lambda),
 \qquad c(\lambda)\in\mathbb Z_{\ge0}. \tag{10}
\]

There is no overlap of the two displayed base divisors. Define `c_n=sum c(lambda) lambda^n` and `c=sum c(lambda)`. Counting dimensions and using the two ring norms gives

\[
 \nu(0)=(a-b)^2+1440,\quad
 \operatorname{Tr}E^n=1+17^n+\operatorname{Tr}F_1^n+2c_n\ge0.
\]

At `n=2` this reads

\[
 \boxed{c_2\ge5470},\qquad
 \operatorname{Tr}E^2=-10940+2c_2. \tag{11}
\]

If the actual channel growth is 17, as required for the brief's reference pair, `|lambda|<=17` for every common mode. Hence `c_2<=289 c`, and **at least 19 common nonzero modes per sector** are required. In particular `2ab>=1442+19=1461`, so `a+b>=55`. This is a lower bound, not an attained minimum. Without the growth restriction, hidden cancelling eigenvalues can exceed 17, and the bound 19 does not follow; then 17 is not the growth of that full channel.

Also `N_1=0` forces `Tr(P A_s)=0` for every Kraus letter in every presentation, by the sum-of-squares identity. For homogeneous odd letters this is automatic; for even letters it equates the traces of the two parity blocks. The necessary inequalities `N_n>=0` hold for all n: the first five are in the table, and for `n>=6`,

\[
 N_n\ge1+17^n-1442\,17^{n/2}>0.
\]

Thus neither the ordinary second-trace obstruction after (11), nor positivity of the proposed supertrace, nor the dimension-square condition proves nonexistence with common modes.

For clarity, allowing an additional specified Bass divisor `k([1]+[-1])`, integer k, changes the dimension requirement to `nu(0)=(a-b)^2+1440-2k`. The minimal ordinary second power sum of that nonzero divisor is `-10941+|1+k|+|k|`; common modes must make it nonnegative by adding `2c_2`. This accounts explicitly for such a correction instead of silently applying (11) to a different target.

**Verdict on the requested alternatives.** Neither (a), an exact Kraus family with the target nonzero divisor, nor (b), a universal obstruction for all finite `a,b` with arbitrary cancelling modes, is proved here. The proposed families are refuted, and their exact replacement formulas are proved. The unrestricted inverse CP realization and its smallest bond/register/Kraus rank remain **OPEN**. Claiming (b) from the failure of (1), from (9), or from the negative bare second trace would repeat the error expressly excluded by binding B6. No nonexistent numerical construction is asserted.

Sources: `report/sections/02h_definitions_graded_ramanujan.tex:19-46,60-94,114-123`; `report/sections/03c_graded_ramanujan.tex:91-108`; `report/sections/03b_graded_permutation.tex:103-122,176-210`; `report/sections/04n_graded_toys_network.tex:26-48,50-81,111-157`; `scripts/graded_toys.py:794-833`; `notes/ramanujan-graded/astra-proofs.md:1428-1441`; binding `notes/deninger-lps/astra-proofs.md:263-299` and its review at `notes/reviews/deninger-lps-2026-09-22.md:105-111`.


## G3 — PROVED structure; REFUTED expander identification

### G3.1 Parity-twisted unitality of the channel actually constructed

Every letter in (1) is even, so its signed unitality equation is simply

\[
 \sum_{ji}\epsilon_{ji}A_{ji}A_{ji}^*=17I_H,
 \qquad E(P_H)=17P_H.
\]

Thus its counting P-mode is **17**, and its normalized P-mode is **1**, not the desired designated H^0 partner at counting eigenvalue 1. Both `I_H` and `P_H` are independent fixed operators of `E/17`; the normalized projections onto the two bond parity blocks give distinct stationary states. The transfer is not graded primitive (`nu_E(17)=2`) and is not a graded quantum expander with a unique fixed point, even in the definition's period version.

More precisely, `W` has simple adjacency eigenvalue 18, no eigenvalue -18, and a connected nonbipartite graph. This also follows from `W ~ -T_1`: `spec T_1=spec T union (spec T_0 minus {18})`, with the first spectrum strictly inside (-8,8) and `-18` simple in the second. Its non-backtracking matrix `C` has simple peripheral eigenvalue 17; `B ~ -C` has simple peripheral eigenvalue -17. In (3) these occur twice, in the even and odd sectors respectively. The odd eigenoperators at -17 are `X tensor diag(z_t(i))` and `Y tensor diag(z_t(i))`. They do not decay under the normalized channel. Squaring the channel fixes them.

After the signed structural divisor in G2.1 is removed, every point of the actual **net divisor** lies on the circle of radius `sqrt(17)`; both `F_1` and `-F_1` have that radius. It has divisor RH and FE, with the multiplicities of (7), but not the target zeta, not a unique stationary state, and not an odd mixing gap. A divisor bound and the expander definition are different assertions.

For the X-letter alternative in the canonical gauge,

\[
 E(P_H)=P\otimes\operatorname{diag}\left(\sum_i C_{ji}s_i\right)_j.
\]

It is a scalar P-mode only if these signed predecessor sums are constant. In the all-negative orientation they are -17, so the normalized P-mode is -1; in the script's canonical orientation they take the distinct values `-13,-11,-9,-7,-5,-3,-1,1,3,5,7,9`, so there is no scalar P-mode. In all orientations the sector formula `C op B` in each parity and the zero divisor remain valid. Orientation changes in this X prescription can change the full channel; signed-walk similarity still determines its sector spectra.

### G3.2 Nonhomogeneous but parity-covariant presentations add no maps

Let `E` be any finite CP map satisfying `E Ad(P)=Ad(P) E`, with arbitrary Kraus matrices `K_s`. Define

\[
 K_{s,+}=(K_s+PK_sP)/2,\qquad
 K_{s,-}=(K_s-PK_sP)/2.
\]

They are respectively even and odd, and

\[
 \sum_{s,\pm}\operatorname{Ad}(K_{s,\pm})
 ={1\over2}\big(E+\operatorname{Ad}(P)E\operatorname{Ad}(P)\big)=E. \tag{12}
\]

This is an explicit homogeneous Kraus representation of the same map, with at most twice the original number of letters. Hence allowing a nonhomogeneous Kraus list **while retaining parity covariance** does not enlarge the class of channels. All the B6 necessary conditions, and every genuine channel-level obstruction, survive. It does not turn the candidate-specific obstructions into a universal no-go theorem. Without covariance there are no invariant even/odd restrictions of the stipulated kind.

### G3.3 The Weil--LPS comparison remains different

The transport here uses the sign local system of squares at level 5 and the Steinberg-at-13 cycle space `K`. The notebook's odd Weil **bond** at level 13 has dimension 6, with `End(W_-)=1 op 7 op 14 op 14`, not the 13-dimensional finite Steinberg constituent. Further, `End(W_-)` is an even doubled sector, whereas the odd doubled sector for the full `C^7 op C^6` bond is the 84-dimensional pair of cross-coherence spaces. Neither a C^{1|1} phase register nor the Bass lift changes these representation-theoretic facts. The unitary memory construction makes a genuine CP realization of its *own* Weil Hashimoto divisor; it provides no equality with `nu_*`.

The graded Harrow theorem additionally requires the specified index-two representation grading and the associated generating-set hypotheses. A freely chosen sign register is not that theorem's irreducible representation. Here `17` is square modulo 13 in the Weil setup; this is distinct from both the index-two all-odd setup and the nonsquare modulo 5 used in G1.3.

Sources: `report/sections/02h_definitions_graded_ramanujan.tex:49-57,97-139`; `report/sections/03c_graded_ramanujan.tex:49-88,110-160`; `scripts/graded_ramanujan.py:1-31,39-76,138-159`; `notes/deninger-lps/astra-proofs.md:194-261,301-313`; `notes/reviews/deninger-lps-2026-09-22.md:98-111`.


## G4 — REFUTED HS claim; PROVED Bass/metric comparison

### G4.1 Adjacency self-adjointness is not memory-transfer self-adjointness

Adjoint-paired letters make the adjacency superoperator `Sigma=sum Ad(U_i)` Hilbert--Schmidt self-adjoint, since `(Ad U_i)^*=Ad(U_i^*)`. This conclusion is about `Sigma`, not the non-backtracking lift. Our register Kraus matrices are partial isometries, and their adjoints are not their allowable forward transitions. On the scalar Pauli component, the transfer is `C`; for successive arcs `i=(a,b), j=(b,c)` with `c!=a`, `C_ji=1` and `C_ij=0`. Hence `C` and `E` are not self-adjoint.

An independent exact test is particularly short: G1 gives `Tr E^2=0`, while `E!=0`. A nonzero HS-self-adjoint finite matrix has `Tr E^2=||E||_HS^2>0`. Here `||E||_HS^2=4*257040=1028160`. Thus the assertion is refuted for the supplied genuine channel. Any HS-self-adjoint channel would also fail to have the nonreal roots of `F_1` in its retained spectrum, regardless of extra cancelling modes.

The arbitrary-Kraus Ihara--Bass theorem retains deformed adjacency/degree terms involving `(1-u^2 E_bar(i) E_i)^(-1)`. Its constant `17u^2` specialization requires inverse transport. It does not make arbitrary companion operators CP or self-adjoint. This is exactly the distinction in `obs:kraus-dichotomy`: adjoint pairing gives a real adjacency spectrum; inverse pairing gives the Bass reciprocity; the edge spectrum need not be real.

### G4.2 An explicit companion embedding in the actual odd sector

The CP channel does contain the signed companion modes, with its full multiplicities and its additional spectra as in (3). Here is an explicit intertwiner, not just a determinant comparison. Regard `x,y in K` as functions on the 840 vertices of `G_e`, and define

\[
 \mathcal L(x,y)_i=x(t(i))-s_i y(h(i)). \tag{13}
\]

Using `h(i)=t(j)`, the exclusion of `bar j`, and degree 18 gives

\[
 (B\mathcal L(x,y))_j
 =(T_1x)(t(j))-17y(t(j))-s_jx(h(j))
 =\mathcal L(Tx-17y,x)_j.
\]

Therefore `B L=L F_1`. Its pullback of the arc Euclidean inner product is

\[
 \mathcal L^*\mathcal L=
 \begin{pmatrix}18I&-T\\-T&18I\end{pmatrix}>0 \quad\hbox{on }K\oplus K, \tag{14}
\]

because `||T||<8`. In particular `L` is injective. Each of the two odd Pauli components in (3) contains this invariant 1442-dimensional companion subspace. In an orthonormal cycle basis `Q: C^{721}->K`, (13) is the concrete `15120 x 1442` matrix with row blocks `Q[t(i),:]` and `-s_i Q[h(i),:]`; this is directly buildable. The remaining odd nonzero modes are the lifted gradient/vertex modes and the signed Bass `+/-1` modes. They cannot be discarded when claiming a full CP divisor.

Formula (14) is the HS metric induced on this embedded subspace (use Pauli matrices normalized to HS norm one). It is **not** the Bass invariant metric below. Thus even the explicit CP embedding of the companion does not identify the two positive forms.

### G4.3 The positive certificate and its exact boundary

For any real symmetric `T` and `q>0`, define

\[
 F=\begin{pmatrix}T&-qI\\I&0\end{pmatrix},\quad
 G=\begin{pmatrix}I&-T/2\\-T/2&qI\end{pmatrix},\quad
 \Omega=\begin{pmatrix}0&I\\-I&0\end{pmatrix}.
\]

Block multiplication proves `F^*GF=qG` and `F^t Omega F=q Omega`. The Schur complement proves

\[
 G>0\quad\Longleftrightarrow\quad qI-T^2/4>0
 \quad\Longleftrightarrow\quad\|T\|<2\sqrt q. \tag{15}
\]

The certified `||T||<8` in this example gives `17I-T^2/4>I`. The companion is then similar, by `G^(1/2)`, to `sqrt(17)` times a unitary, and is diagonalizable. This metric can be transported to each image of (13) by `L^{-1}` on that image. It is an additional positive invariant metric on specified modes, not the ambient HS identity. Indeed

\[
 F_1^*F_1=
 \begin{pmatrix}T^2+I&-17T\\-17T&289I\end{pmatrix}\ne17I.
\]

On each real adjacency eigenspace of eigenvalue t, the companion roots satisfy

\[
 \alpha_+\alpha_-=q,\quad \alpha_++\alpha_-=t,\quad
 |\alpha_+|=|\alpha_-|=\sqrt q
 \Longleftrightarrow |t|\le2\sqrt q. \tag{16}
\]

At `t=+/-2sqrt(q)` the two roots coincide and the displayed `2 x 2` companion has a nontrivial Jordan block: its lower-left entry is one, so it is not a scalar matrix. Consequently no positive definite invariant similitude metric exists at the endpoint, even though the determinant roots are still on the circle. Outside the closed band the two real roots have unequal moduli, also excluding such a metric. This proves the necessity of strictness in (15) even if one allows a different positive metric.

The finite note's Proposition 9.3 and `cor:graded-band-circle` therefore use the **same quadratic relation**, with different assertions:

* the band-circle corollary concerns the nonstrict spectral/divisor condition (16), after cancellations and designated trivial factors;
* Proposition 9.3 concerns a specified companion operator and a positive invariant polarization, and requires strictness to exclude its Jordan endpoints;
* in this strictly bounded example both conditions hold, but neither positivity of CP maps nor positivity of ring norms proves the strict band.

For an arbitrary net divisor, cancelled out-of-band modes remain invisible, and an on-circle net divisor does not control Jordan blocks. The finite `G` supplies the stronger manifest metric on the explicitly retained spectral companion. In the actual channel its two copies and the extra signed/unsigned modes still have to be accounted for before making a channel-level statement.

Sources: `notes/deninger-lps/src/manuscript.txt:1188-1235` (Proposition 9.3); `notes/deninger-lps/src/lps-deninger-worked-example.md:449-520`; `notes/deninger-lps/astra-proofs.md:315-319`; `report/sections/02h_definitions_graded_ramanujan.tex:60-94`; `report/sections/03c_graded_ramanujan.tex:91-128`; `report/sections/08_quantum_ihara_general.tex:55-110`; `report/sections/08c_weil_positivity_continuous.tex:234-250`.


## G5 — SHARPENED / OPEN: finite Deninger dictionary

The construction closes the **specific relative-phase calculation** left uncomputed in B6: it is possible to place signed transport in an odd CP block, and the coherences, populations, multiplicities, zero modes and ring zeta are now explicit. It does **not** close the exact net-divisor existence question in B6. The worked example's completed transfer `F_0 op F_2 | F_1` remains a graded spectral transfer unless a different homogeneous Kraus family is supplied. The direct full-sector prescription is impossible; a realization with the zero and shared-mode budget of G2.4 has neither been constructed nor excluded.

| Finite Deninger datum | Notebook dictionary and exact scope |
|---|---|
| `F_0=1, F_2=17` | Reference pair `(H^0,growth)=(1,17)` for the spectral divisor; they do not assert the P-mode of an unspecified channel. |
| `K op K`, `F_1` | Specified odd spectral space of dimension 1442; embedded twice in the actual CP odd sector by (13), not that channel's whole odd sector. |
| `Z=det(1-uF_1)/((1-u)(1-17u))` | Completed net divisor `nu_*`; after designated `[1]+[17]`, the retained divisor is `-spec F_1`. |
| Strict certified band `||T||<8<2sqrt(17)` | Proves the spectral (Ram) circle condition and hence (RH); it is additional spectral input, not a consequence of CP. |
| Pairing `alpha <->17/alpha` | Divisor (FE); on the diagonalizable retained companion it also admits the stronger operator similarity exchanging each conjugate pair. |
| `F_1^* G F_1=17G`, `G>0` | Manifest (HP) on this specified spectral operator, and on its embedded copies after metric transport; not automatic ambient HS unitarity. |
| `N_n` and the corrected signed Euler product | Spectral supertraces with nonnegative values; nonnegativity is necessary for CP, not a Kraus realization theorem. |
| The explicit P-letter channel | A genuine balanced graded CP transfer with zeta `(Z(u)/Z(-u))^2`, different divisor and nonmixing peripheral modes. |

The finite example supplies all four spectral notions (RH), (FE), (Ram), and (HP) in `def:graded-rh-fe-ramanujan`, in exactly the definition's allowance for spectral transfers. It supplies no graded quantum-expander assertion. Its inverse-pair functional equation and its positive metric stay valid independently of the unsuccessful CP identification. The level-13 Weil channel remains a different Fourier selection of the Hecke family.

Sources: `report/sections/02h_definitions_graded_ramanujan.tex:60-110`; `notes/deninger-lps/src/lps-deninger-worked-example.md:332-359,449-534`; `notes/deninger-lps/astra-proofs.md:263-319`; `report/sections/04u_deninger_lps.tex:124-149`.

## Numerical checks for the blind lane

### 1. Build the precise finite objects

Use the quaternion generators, PGL_2(F_5) vertices, color-edge conventions, and 252 square reordering rules of `scripts/lps_square_complex.py:36-206`. Each square boundary has two horizontal entries `(a,sa),(b,sb)`; create the undirected signed edge `(a,b,-sa*sb)`. There are 7560 such edges on 840 vertices. Reconstruct the symmetric signed `T_1` and unsigned `W`; the latter is actually simple (no loops, entries at most one) in this example. Order arcs consecutively as the two directions of each edge, so `bar(i)=i xor 1`.

Build sparse `15120 x 15120` matrices `C_ji=[h(i)=t(j), j!=bar(i)]` and `B_ji=C_ji s_i`. Their 257040 transitions specify the **full** Kraus family (1), with bond `H=C^{15120|15120}` and register size 15120. The actual doubled superoperator has dimension `914457600`; do not allocate it densely. Formula (2), plus the four `15120 x 15120` blocks in (3), specifies every entry including the killed coherences. These are exact matrix formulas, not only spectral prescriptions.

### 2. Expected traces and dimensions

In counting units, for `n=1,...,6`:

\[
\begin{aligned}
 \operatorname{Tr}E_0^n&=(0,0,20160,122400,2419200,48404160),\\
 \operatorname{Tr}E_1^n&=(0,0,-20160,122400,-2419200,48404160),\\
 \operatorname{Tr}E^n&=(0,0,0,244800,0,96808320),\\
 \operatorname{Str}E^n&=(0,0,40320,0,4838400,0).
\end{aligned}
\]

Both sectors have dimension **457228800**: 30240 diagonal-register dimensions and 457198560 one-step-zero coherence dimensions. Each sector has exactly that last number of zero eigenvalues, and the net zero multiplicity is zero. For the normalized channel all nth traces are divided by `17^n`. For the X-letter alternative the ordinary traces are the same displayed ordinary traces, and every supertrace is zero.

Use (5) on the small adjacency matrices for all six exact integer checks; compare the full table in G1.4 to the target `N=(0,11520,10080,126720,1209600,23886720)`. Check also `z_a=EPS13[canonical_tail(a)]`, `T_1=-diag(z) W diag(z)`, and `diag(z_t(i)) B diag(z_t(i))=-C`.

### 3. Divisor, multiplicities and trivial exponents

The full nonzero sector spectra are `2 spec C` and `2 spec B_e`. Their structural algebraic multiplicities are:

| eigenvalue | even multiplicity | odd multiplicity | net multiplicity |
|---:|---:|---:|---:|
| 17 | 2 | 0 | 2 |
| -17 | 0 | 2 | -2 |
| 1 | 13442 | 13440 | 2 |
| -1 | 13440 | 13442 | -2 |

Each sector has 3356 additional eigenvalues on the `sqrt(17)` circle. These comprise two copies of the 1442 target companion roots (with sign reversal in the even sector) and two copies of the 236 companion roots from the 118 nontrivial vertical adjacency modes. The vertical modes are sign symmetric and cancel between sectors. The remaining signed multiplicity is **exactly** (7); sign-symmetric target modes cancel further. In particular test the `t=+/-7` disappearance and the `t=+/-2` coefficients +114 and -114. Compare against target coefficients -4 at each `+/-7` root and respectively -20, -77 at the `+/-2` roots.

For a purely polynomial check, let `P_K(u)=det_K Q_u(T)`, obtained from the exact factor table in `notes/deninger-lps/src/lps-deninger-worked-example.md`, Section 13, or `FACTORS` in `scripts/lps_square_complex.py:321-337`. Then test

\[
 Z_E(u)=\left[
 { (1+u)(1+17u)\,P_K(u)\over
   (1-u)(1-17u)\,P_K(-u)}\right]^2.
\]

This fixes every algebraic multiplicity without rounding roots. The raw Bass exponents are 6720 per square walk and **13440 per actual CP sector**, cancelling to zero in `sdet E`. The vertical exponent is 960. For the purely spectral pair, the superdeterminant exponent is **-5760**, and the ring-zeta exponent is **+5760**. Completion removes the latter. The exact `nu_triv` and `S_triv` are in G2.1; do not remove extra eigenvalues just because they share a value with a designated mode.

### 4. Structural and metric checks

Verify `sum A A^*=sum A^* A=17I`, `E(P_H)=17P_H`, the two even fixed modes and two odd -17 modes. Check the failure of self-adjointness using `C!=C^t`, or `Tr E^2=0` versus `||E||_HS^2=1028160`. Build the sparse full-vertex version of (13) and verify `B L=L [[T_1,-17I],[I,0]]` and (14) before restricting to `K`; restriction preserves the identities. On a basis of `K`, verify the two similitudes for `G,Omega` and their strict Schur complement. These are different metrics.

Executed locally: `OPENBLAS_NUM_THREADS=1 python3 notes/lps-graded-cp/checks/exact_transport.py`. This check reconstructs the finite complex prefix, computes the six moments by integer sparse recurrence, verifies the sign gauge on every transition, tests register-coherence annihilation with a P letter, and checks the exact Bass intertwiner and its HS Gram matrix. All assertions pass. No speculative exact-target CP family is supplied for the blind lane to build.

## What this changes in the notebook

* **PROVED — G1:** Relative phases realize `B_e` twice in the odd sector, with two compulsory unsigned even blocks and exactly computed zero coherences.
* **REFUTED — candidate identification:** This channel realizes `(Z(u)/Z(-u))^2`; topological factors and invisible common modes cannot change it into `Z(u)`.
* **OPEN — B6/G2:** Existence of any finite graded CP channel with exactly the completed net divisor, including arbitrary cancelling modes, remains unresolved.
* **SHARPENED — necessary budget:** At growth 17, an exact realization needs at least 19 common nonzero modes per sector, bond dimension at least 55, and net zero multiplicity `(a-b)^2+1440`.
* **PROVED — G3:** Parity covariance already implies a homogeneous Kraus presentation; the explicit P-letter map is bistochastic after scaling but has no unique stationary state.
* **PROVED / REFUTED — G4:** Bass supplies the companion embedding and reciprocal roots, while the claimed HS self-adjointness fails; the positive invariant metric requires the strict band.
* **SHARPENED — G5:** The completed worked example remains a certified spectral RH/FE/Ramanujan/HP package, with a related genuine CP realization of a different divisor.
