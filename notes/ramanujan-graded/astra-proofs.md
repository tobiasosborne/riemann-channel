# Audit and proofs of D1–D14

2026-09-15. Input: `definition.md` and the files specified in `astra-brief.md`.
Only this report and files in `finite/` were written. A status applies to the
whole D-item. **CORRECTED** means that a precise replacement is proved below;
it does not endorse the deleted assertions. Standard analytic or representation
theoretic inputs are explicitly named hypotheses, including **H-repka**.

The main conclusions are these:

* The graded Ihara–Bass identity is valid, and Harrow's bound transfers to both
  sectors. A bound on the **net divisor** is weaker than a bound on both sectors.
* The proposed odd-sector Alon–Boppana theorem is false, even for a family of
  primitive channels with fixed degree and arbitrarily large balanced bonds.
* Norm Chernoff convergence and a homogeneous GKSL presentation hold in finite
  dimension. Sampling can cancel a divisor through frequency aliasing.
* Temperedness gives the diffusion threshold, with a necessary time-normalization
  correction. Reflection grading gives a discrete odd ladder, but does not give
  the claimed heat supertrace or a full critical-line divisor.

## Conventions and reusable hypotheses

**H-fin.** The bond is a finite-dimensional complex Hilbert space
\(H=H_+\oplus H_-\), with self-adjoint unitary
\(P=I_{H_+}\oplus(-I_{H_-})\). This is the standard orthogonal grading; it is
stronger than merely specifying an algebraic involution.

**H-hom.** A finite Kraus family satisfies \(PA_iP=\epsilon_iA_i\),
\(\epsilon_i\in\{1,-1\}\). This is a structural restriction, not a property
of arbitrary Kraus lists. A parity-covariant CP map admits such a list.

**H-unit.** There are \(D=2h\) labelled unitary letters, with a fixed-point-free
reversal \(i\mapsto\bar i\) and \(U_{\bar i}=U_i^*\). Repeated letters are
allowed. This is the usual inverse-paired bouquet convention. The degree counts
labels and need not equal the minimal Kraus rank.

Use \(V=\operatorname{End}(H)\), \(\Gamma X=PXP\), and
\(V_k=\ker(\Gamma-(-1)^k)\). In the requested vectorization convention,
\(E=\sum_i A_i\otimes\overline{A_i}\). Write
\[
 n_0=(\dim H_+)^2+(\dim H_-)^2,\qquad n_1=2\dim H_+\dim H_-.
\]
Here \(E\) means a CP **transfer**, without an implicit trace-preservation
assumption. For unitary letters use the unambiguous notation
\[
 \Sigma=\sum_i\operatorname{Ad}(U_i),\qquad \Phi=\Sigma/D,\qquad b=D-1.
\]
Thus \(\rho(\Sigma)=D\), whereas \(\rho(T)=b\) for its Hashimoto lift.
The draft's \(q\) means \(\rho(E)\) for a general transfer and means \(b\) in
D3–D6 and D13. Those are different operators and different numbers.

At a nonzero transfer eigenvalue \(\mu\), put
\(\nu(\mu)=m_0(\mu)-m_1(\mu)\). Then
\[
 N_P(n)=\sum_\mu\nu(\mu)\mu^n,\qquad
 Z_P(u)=\prod_{\mu\ne0}(1-u\mu)^{-\nu(\mu)}.
\]
Positive \(\nu\) means a pole at **\(u=\mu^{-1}\)**. A zero eigenvalue is
invisible to this lattice zeta, even when its net multiplicity is nonzero.
It is not invisible to the continuous determinant \(\operatorname{sdet}(z-T)\).
Algebraic multiplicities, not Jordan-block counts, occur throughout.

**H-count.** When a positive entropy is used, a counting normalization and two
reference values \((q,1)\), \(q>1\), have been specified. This is additional
geometric data, not an invariant of a normalized channel. In channel units the
pair is \((1,1/q)\), with critical radius \(q^{-1/2}\). In continuous time use
two reference rates \((a_+,a_-)\), with centre \(c=(a_++a_-)/2\); counting
units \((\omega,0)\) and channel units \((0,-\omega)\) give the centres in the
brief. Merely knowing the spectral bound of a TP generator, which is zero,
does not determine a nonzero critical decay rate.

## D1 — Graded trace inequality

### Statement (as proved)

For every \(n\ge1\), both sector traces are real and
\[
 |\operatorname{Tr}E_1^n|\le\operatorname{Tr}E_0^n,\qquad
 \rho(E_1)\le\rho(E_0)=\rho(E).
\]
Equality of the two radii does **not** force cancellation at any eigenvalue.

### Hypotheses H-*

H-fin and H-hom. **H-PF:** a finite-dimensional positive map on the matrix
positive cone has a nonzero positive semidefinite eigenmatrix at its spectral
radius. This is the standard cone Perron–Frobenius theorem; it does not require
irreducibility.

### Proof

1. **Both closures are nonnegative.** Expanding powers of the Kraus sum gives
   \(\operatorname{Tr}E^n=\sum_w|\operatorname{Tr}A_w|^2\) and
   \(\operatorname{Tr}(\Gamma E^n)=\sum_w|\operatorname{Tr}(PA_w)|^2\).
2. **Sector traces are real.** The antilinear involution \(X\mapsto X^*\)
   preserves each sector and commutes with \(E\). Each sector spectrum is
   conjugation invariant, including algebraic multiplicity.
3. **The inequality follows.** Writing the two nonnegative quantities as
   \(a_n+b_n\) and \(a_n-b_n\) gives \(a_n\ge|b_n|\).
4. **The Perron value occurs evenly.** If \(ER=qR\) with \(R\ge0\),
   then \(R_0=(R+PRP)/2\ge0\), \(R_0\ne0\) since it has the same positive
   trace, and \(ER_0=qR_0\). Thus \(\rho(E_0)=q\); the odd restriction has
   radius at most that of the full operator.
5. **The final sentence of the draft fails.** On \(\mathbb C^{1|1}\), take
   the single even letter \(A=P=\operatorname{diag}(1,-1)\). The even
   spectrum is \(\{1,1\}\), the odd spectrum \(\{-1,-1\}\), and
   \(N_P(n)=2-2(-1)^n\). Equal radii coexist with disjoint eigenvalue sets;
   there is no cancellation in the divisor. `finite/finite_checks.py` verifies
   these matrices exactly.

The inequality is a consequence of norm positivity. It is not the positive
definiteness of a centred Weil kernel, which is a different condition.

### Status: CORRECTED

Ledger L01–L02.

## D2 — The parity eigenoperator

### Statement (as proved)

\[
 E(P)=P\sum_i\epsilon_i A_iA_i^*.
\]
Consequently \(E(P)=rP\) iff \(\sum_i\epsilon_i A_iA_i^*=rI\).
For \(A_i=\sqrt{w_i}U_i\), this holds with
\(r=\sum_i\epsilon_iw_i\). In a representation channel this is the value
of the sign character on the weighted walk element.

### Hypotheses H-*

H-fin and H-hom. **H-weight:** \(w_i\ge0\), and \(\sum_iw_i=1\) when
channel units are intended; these are the standard probabilities of a
mixed-unitary channel. **H-sign:** for the representation assertion,
\(P\pi(g)P=\epsilon(g)\pi(g)\) for a sign character; this is precisely
the covariance supplied in D6.

### Proof

\(A_iP=\epsilon_iPA_i\), so summing \(A_iPA_i^*\) proves the identity.
Multiplication by \(P\) proves the equivalence. Unitarity reduces
\(A_iA_i^*\) to \(w_iI\). Finally \(P\) is in \(V_0\), irrespective
of the sign of \(r\).

The displayed condition concerns \(A_iA_i^*\): it is signed **unitality**
in this Schrödinger convention. Signed trace preservation instead concerns
\(\sum_i\epsilon_i A_i^*A_i\), or the adjoint map. The algebraic D2 claim
is unchanged by correcting that surrounding terminology.

### Status: PROVED


## D3 — Graded quantum Ihara–Bass

### Statement (as proved)

Let \(T(v\otimes e_i)=\sum_{j\ne\bar i}\operatorname{Ad}(U_i)v\otimes e_j\).
It preserves \(V_k\otimes\mathbb C^D\), and
\[
 \det(I-uT_k)=(1-u^2)^{n_k(D-2)/2}
       \det(I-u\Sigma_k+b u^2I),\quad k=0,1.
\]
Hence, with \(f_\lambda(u)=1-\lambda u+bu^2\),
\[
 Z_{P,T}(u)=(1-u^2)^{-(D-2)(\dim H_+-\dim H_-)^2/2}
       \prod_\lambda f_\lambda(u)^{-\nu_\Sigma(\lambda)}.
\]
The explicit edge factors cancel for a balanced grading. This does not
assert that all the remaining even factors cancel.

### Hypotheses H-*

H-fin, H-hom, H-unit. \(D\ge2\); use \(D\ge4\) for a nondegenerate
expansion/Ramanujan discussion. All are explicit bouquet hypotheses.

### Proof

1. **Restriction is legitimate.** Each \(B_i=\operatorname{Ad}(U_i)\)
   commutes with \(\Gamma\), and \(B_{\bar i}B_i=I\) on either sector.
2. **Factor the edge operator.** On one sector of dimension \(N=n_k\), set
   \(Rv=\sum_iB_iv_i\), \(Sx=(x)_i\), and
   \(J(v\otimes e_i)=B_iv\otimes e_{\bar i}\). Then \(T=SR-J\)
   and \(J^2=I\).
3. **Compute the backtracking determinant.** Each reversed pair gives
   \(\det\left(\begin{smallmatrix}I&uB_{\bar i}\\uB_i&I\end{smallmatrix}\right)
   =(1-u^2)^N\). Thus \(\det(I+uJ)=(1-u^2)^{ND/2}\).
4. **Compress.** For \(u^2\ne1\), Sylvester's determinant identity gives
   \[
   \det(I-uT)=\det(I+uJ)\det(I-uR(I+uJ)^{-1}S).
   \]
   As \((I+uJ)^{-1}=(I-uJ)/(1-u^2)\), \(RS=\Sigma_k\),
   and \(RJS=DI\), the last matrix is
   \((I-u\Sigma_k+(D-1)u^2I)/(1-u^2)\).
5. **Finish.** Multiplying determinants gives the exponent
   \(ND/2-N=N(D-2)/2\). Polynomial identity extends to \(u=\pm1\).
   Dividing the odd determinant by the even one proves the zeta formula;
   \(n_0-n_1=(\dim H_+-\dim H_-)^2\).

This reproduces the source-weight convention in `thm:qihara-general`.
Changing Kronecker ordering is a permutation similarity and changes no
determinants or signs. Exact Pauli sector determinants are checked in
`finite/finite_checks.py`; the supplied 79-check script also passes.

### Status: PROVED

## D4 — What the band/circle equivalence actually says

### Statement (as proved)

For either sector **before cancellation**, an adjacency eigenvalue
\(\lambda\in\mathbb R\) produces two edge eigenvalues \(\mu_\pm\) satisfying
\[
 \mu_++\mu_-=\lambda,\quad \mu_+\mu_-=b,
 \qquad |\mu_+|=|\mu_-|=\sqrt b
       \Longleftrightarrow |\lambda|\le2\sqrt b.
\]
For the **net graded divisor**, the equivalence is instead
\[
 \text{all retained divisor points have }|u|=b^{-1/2}
 \Longleftrightarrow
 |\lambda|\le2\sqrt b\quad
 \text{for every }\lambda\notin\{D,-D\}
 \text{ with }\nu_\Sigma(\lambda)\ne0.
\]
Here remove the structural edge multiplicities and the entire quadratic
of each declared peripheral adjacency mode. A bound on all odd adjacency
modes additionally requires that no odd \(\pm D\) mode was exempted.
Both-sector bounds imply the divisor bound, but the converse is false.

### Hypotheses H-*

H-fin, H-hom, H-unit with \(D\ge4\). **H-triv-Bass:** the removed modes
are specified with parity and multiplicity: the explicit \(\pm1\) edge
factors and the pairs \((b,1)\) or \((-b,-1)\) attached to declared
\(\pm D\) adjacency eigenvectors. This is standard Ihara bookkeeping.
**H-nohidden** (only for the stronger converse): every retained adjacency
class occurs in just one parity sector. This is an additional restriction,
and the examples do not generally satisfy it.

### Proof

1. \(\Sigma_k\) is Hermitian, since the sum pairs each unitary
   superoperator with its Hilbert–Schmidt adjoint. Thus \(\lambda\) is real.
2. The roots of \(\mu^2-\lambda\mu+b\) are a conjugate pair of modulus
   \(\sqrt b\) if \(|\lambda|<2\sqrt b\), the repeated root
   \(\pm\sqrt b\) at equality, and real roots of unequal moduli otherwise.
3. Distinct \(\lambda\)'s have no common quadratic root: from a root
   \(u\ne0\), recover \(\lambda=u^{-1}+bu\). In particular only
   \(\lambda=\pm D\) contributes roots at \(u=\pm1\).
4. D3 therefore leaves precisely exponent \(-\nu_\Sigma(\lambda)\)
   on each nontrivial quadratic. Step 2 proves the corrected equivalence.
   H-nohidden turns it into a statement about both raw sector spectra.
5. **Counterexample, including primitivity.** On \(\mathbb C^{1|1}\)
   take ten copies of \(I\), two of \(X\), and two of \(Z=P\), paired
   in copies. Then \(D=14,b=13\),
   \[
    \operatorname{spec}\Sigma_0=\{14,10\},\qquad
    \operatorname{spec}\Sigma_1=\{10,6\},\qquad
    Z_{P,T}=\frac{1-6u+13u^2}{(1-u)(1-13u)}.
   \]
   The normalized eigenvalues are \(1,10/14,10/14,6/14\), so the channel
   is primitive. The value \(10>2\sqrt{13}\) cancels completely, while
   \(6<2\sqrt{13}\) gives critical-circle zeros. All identities are checked
   exactly by `finite/finite_checks.py`.

The trivial set in edge-eigenvalue coordinates is \(\{1,b,-1,-b\}\)
as applicable; in zeta coordinates it is \(\{1,b^{-1},-1,-b^{-1}\}\).
An odd quadratic produces a **net zero only when its odd multiplicity exceeds
the even multiplicity**. At a band endpoint a Hashimoto block can be Jordan;
the circle assertion alone does not provide a positive invariant metric.

### Status: CORRECTED

Ledger L03–L04.

## D5 — The proposed odd Alon–Boppana bound

### Statement (as proved)

The claimed odd-sector lower bound is false. In every dimension
\(H=\mathbb C^m\oplus\mathbb C^m\), the degree-four channel
\[
 \Phi=\tfrac14(\operatorname{Ad}I+\operatorname{Ad}I+
                   \operatorname{Ad}P+\operatorname{Ad}P)
\]
has \(\Phi_1=0\). There are also primitive degree-sixteen examples with
\(\rho(\Phi_1)=0\) and unbounded \(m\). Consequently no constant \(c\)
independent of bond dimension makes the drafted inequality hold.

### Hypotheses H-*

H-fin, H-hom and H-unit. Repeated letters are allowed by the same convention
used by the draft's Pauli example. **H-AB-full:** for fixed even \(D>2\),
the full-space mixed-unitary Hermitian channel satisfies Hastings' asymptotic
Alon–Boppana bound. This standard theorem is derived in the specified local
source, `refs/src/0706.0556/sd10.tex`, “Lower Bounds,” especially the positivity
step preceding equation `lowB`.

### Proof / explicit refutation

1. On \(V_1\), \(\operatorname{Ad}P=-I\), so the four-letter average
   is zero. On \(V_0\), it is the identity. This holds for every \(m\).
2. At length two, the proposed trace lower bound would already give
   \(0\ge n_1 D/D^2=n_1/4>0\). The positive freely reducing words are
   cancelled by negative contributions of other words.
3. In Hastings' full-space proof a word contributes
   \(|\operatorname{Tr}U_w|^2\ge0\). In the odd restriction an even word
   with blocks \(U_{w,+},U_{w,-}\) contributes
   \(2\operatorname{Re}(\operatorname{Tr}U_{w,+}
                 \overline{\operatorname{Tr}U_{w,-}})\), which may be negative.
   Dropping those words is not a lower bound.
4. **Primitivity does not repair it.** Let \(m\ge3\) be odd, let \(C_m,S_m\)
   be the clock and cyclic shift, and set
   \(\Psi_m=\frac14\sum_{V\in\{C_m,C_m^*,S_m,S_m^*\}}\operatorname{Ad}V\).
   Use the sixteen letters \(\sigma_a\otimes V\),
   \(\sigma_a\in\{I,X,Y,Z\}\), and grade by \(Z\otimes I_m\).
   The channel is \(\operatorname{Depol}_2\otimes\Psi_m\), so its odd block
   is zero. The clock/shift operator basis diagonalizes \(\Psi_m\) with
   eigenvalues
   \[
    \tfrac12\big(\cos(2\pi a/m)+\cos(2\pi b/m)\big),\quad a,b\in\mathbb Z/m.
   \]
   Only \((a,b)=(0,0)\) gives modulus one, because \(m\) is odd. Hence the
   whole channel is primitive. The degree remains sixteen as \(m\to\infty\).
5. **What survives.** With a simple fixed point and no other peripheral
   modes, Hastings' full-space theorem implies
   \[
    \max\{\rho(\Phi_0|_{I^\perp}),\rho(\Phi_1)\}
      \ge\lambda_H-O_D(\log\log\dim H/\log\dim H).
   \]
   It does not place the large eigenvalue in a prescribed sector.

Script: `finite/finite_checks.py`, including exact degree-four matrices and
degree-sixteen numerical checks at \(m=3,5,7\); step 4 proves the family for
all odd \(m\).

### Status: REFUTED

Ledger L05.

## D6 — Graded Harrow, characters, and Artin factors

### Statement (as proved)

Let \(G_0\) have index two in a finite group \(G\), let \(\epsilon\) be
the quotient sign, and let \(\pi\) be irreducible with reducible restriction.
Then the grading and the sector decompositions in D6(i) hold. The trivial
and sign representations occur once each, both evenly, generated by \(I\)
and \(P\). Every constituent transfers its walk matrix from the regular
representation. For a nonbipartite Ramanujan Cayley multigraph this gives a
mixing graded Ramanujan channel. For a bipartite graph the bound excludes its
bipartition character \(\beta\): if \(\beta\) is absent from
\(\pi\otimes\bar\pi\), the channel still mixes; if present, it supplies a
period-two mode whose parity must be identified. For all-odd letters,
\(\beta=\epsilon\), and this is the even mode \(P\).

Put \(W=D^{-1}\sum_{s\in S}s\), \(b=D-1\), and write
\(V_k=\bigoplus_\sigma M_{k,\sigma}\otimes V_\sigma\),
\(a_{k,\sigma}=\dim M_{k,\sigma}\). Then
\[
 Z_{P,T}(u)=\prod_{\sigma\in\widehat G}
       \det(I-uT_\sigma)^{a_{1,\sigma}-a_{0,\sigma}},
\]
where \(T_\sigma\) uses the individual **unnormalized** letters
\(\sigma(s)\), not just the matrix \(\sigma(W)\).

For a word product \(g=w\in G_0\), set
\(a(g)=\chi_+(g)\), \(b(g)=\chi_-(g)\). Both closures vanish on word
products outside \(G_0\), and
\[
\begin{split}
 \operatorname{Tr}\Phi^n&=D^{-n}\sum_{w\in G_0}|a(w)+b(w)|^2,\\
 \operatorname{str}\Phi^n&=D^{-n}\sum_{w\in G_0}|a(w)-b(w)|^2,\\
 \operatorname{Tr}\Phi_1^n&=2D^{-n}\operatorname{Re}
                      \sum_{w\in G_0}a(w)\overline{b(w)}.
\end{split}
\]
Here the sums run over length-\(n\) labelled words whose product lies in
\(G_0\), not over group elements with uniform multiplicity.

### Hypotheses H-*

**H-group:** \(G\) is finite, \(G_0\lhd G\) has index two, and \(\pi\)
is an ordinary irreducible unitary representation with reducible restriction.
These are the exact Clifford-theory hypotheses. **H-Clifford:** the standard
index-two theorem gives \(\pi|_{G_0}=\pi_+\oplus\pi_-\) with inequivalent
conjugate summands, interchanged by the odd coset. H-unit is required for the
Hashimoto assertion, and the symmetric multiset \(S\) generates \(G\).
**H-Cayley-Ram:** all regular-representation walk eigenvalues except the
constant and, when present, the bipartition sign lie in the Hastings band.
This is a substantive input about the Cayley graph, not a consequence of
Clifford theory. For LPS it is the LPS theorem in the stated admissible cases.

### Proof

1. **Grade the bond.** Put \(P=1\) on \(\pi_+\) and \(-1\) on
   \(\pi_-\). Even group elements preserve the summands; odd ones interchange
   them. Thus \(P\pi(g)P=\epsilon(g)\pi(g)\).
2. **Grade the conjugation representation.** Conjugation by \(\pi(g)\)
   commutes with \(\Gamma\), since the two signs cancel. Restricting to
   \(G_0\) gives
   \[
   V_0=(\pi_+\otimes\bar\pi_+)\oplus(\pi_-\otimes\bar\pi_-),\quad
   V_1=(\pi_+\otimes\bar\pi_-)\oplus(\pi_-\otimes\bar\pi_+).
   \]
   These are expressions as \(G_0\)-modules; the paired blocks together,
   rather than either block individually, are \(G\)-modules.
3. **Identify the two structural lines.** Schur's lemma gives
   \(\dim\operatorname{Hom}_G(1,\pi\otimes\bar\pi)=1\).
   Also \(\pi\simeq\epsilon\otimes\pi\) via \(P\), so Schur gives
   \(\dim\operatorname{Hom}_G(\epsilon,\pi\otimes\bar\pi)=1\).
   Their spanning operators are \(I,P\), both even; D2 gives
   \(\Phi(P)=\epsilon(W)P\).
4. **Transfer the bound.** Fourier decomposition of \(\mathbb C[G]\)
   contains every irreducible \(\sigma\), and convolution acts there as
   \(\sigma(W)\otimes I_{\dim\sigma}\). On each channel isotypic component
   it acts as \(I_{M_{k,\sigma}}\otimes\sigma(W)\). Thus spectral
   containment and the operator-norm bound are immediate. This is exactly
   the mechanism in Harrow, `0709.1142/main.tex`, equation `eq:gap-ineq`.
5. **Handle periodicity explicitly.** For a connected symmetric Cayley
   graph, an eigenvalue \(-1\) occurs exactly when it is bipartite; the
   associated one-dimensional sign is unique. If this sign equals
   \(\epsilon\), its channel line is \(P\), hence even. The regular
   second singular value without removing it is **one**, not \(\lambda_H\).
   After removing it, H-Cayley-Ram gives the band on every remaining sector.
   In particular all-odd LPS letters give a unique fixed state but period two,
   not a strictly mixing expander as in `def:quantum-expander`.
6. **Prove the character identities.** On \(G_0\), the two ordinary bond
   traces are \(a+b\) and \(a-b\). Off \(G_0\), both \(\pi(g)\) and
   \(P\pi(g)\) are block off diagonal and have trace zero. Expand word
   powers and use the trace-of-conjugation identity. Alternatively, on
   \(G_0\) the sector characters are \(|a|^2+|b|^2\) and
   \(a\bar b+\bar a b\); off \(G_0\) both sector characters vanish.
7. **Prove Artin factorization.** Every individual \(\operatorname{Ad}\pi(s)\)
   respects the isotypic decomposition. The edge operator is therefore
   \(\bigoplus_\sigma I_{M_{k,\sigma}}\otimes T_\sigma\).
   Taking determinants proves the formula. Equivalently, the Euler product
   for each inverse determinant is
   \(L_\sigma(u)=\prod_{[c]}\det(I-u^{\ell(c)}\sigma(c))^{-1}\),
   over primitive cyclically reduced bouquet words, and
   \(Z_{P,T}=\prod_\sigma L_\sigma^{a_{0,\sigma}-a_{1,\sigma}}\).
8. **Zeros exist, but raw odd multiplicity is not zero multiplicity.**
   Clifford grading is balanced, so \(\dim V_0=\dim V_1\).
   In the nonbipartite case remove the one even constant adjacency mode;
   the retained sum of net multiplicities is \(-1\). In the all-odd
   bipartite case remove the two even structural modes; that sum is \(-2\).
   Some retained net multiplicity is therefore negative. D3–D4 put these
   actual zeros on the circle. Positive retained net multiplicities, and
   therefore nontrivial circle poles, may also remain.

### Examples and the false genus printout

The finite principal series in the brief descends from
\(\operatorname{Ind}_B^{GL_2(\mathbb F_p)}(\chi\otimes\chi^{-1})\)
because its central character is trivial. For an order-four \(\chi\),
\(\chi\ne\chi^{-1}\) gives irreducibility. Twisting by the quadratic
determinant character interchanges the two inducing characters, so the
representation is sign-self-equivalent and Clifford theory applies.
This uses the standard finite \(GL_2\) principal-series criterion
**H-finite-PS**, in addition to H-Cayley-Ram for the LPS examples.

`finite/harrow_audit.py` independently subtracts the sector multiplicities
of the supplied construction. Its numerical results, with matching tolerance
\(10^{-7}\), are:

| \((p;b)\) | Raw odd quadratic degree | Reduced numerator degree | Reduced denominator degree | Nontrivial denominator degree |
|---|---:|---:|---:|---:|
| \((5;13)\) | 36 | 4 | 4 | 0 |
| \((13;5)\) | 196 | 144 | 144 | 140 |

For \((5;13)\), the numerical multiplicities identify the candidate reduced
formula \(f_{4}(u)f_{-4}(u)/(f_{14}(u)f_{-14}(u))\), with \(b=13\).
For \((13;5)\), for example \(\lambda=0\) has net even multiplicity four,
so the nontrivial denominator survives. These are numerical diagnoses,
not exact arithmetic certificates for the large representation matrices.
The universally claimed numerator-only formula is already disproved by
these checks and by the missing multiplicity subtraction in its derivation.
Even the first denominator has four peripheral factors; it is not the
denominator of a connected curve over \(\mathbb F_{13}\).

The Pauli example itself is exact (D13). However, a two-dimensional ordinary
irreducible representation of \(\mathbb Z_2^2\) does not exist. Use the finite
Pauli group, an index-two subgroup such as \(\langle iI,Z\rangle\), and its
genuine qubit representation; or state explicitly that the quotient carries
a projective representation. Conjugation removes the central phases.

### Status: CORRECTED

Ledger L06–L09 and L37.

## D7 — Exact sampling and the aliasing qualification

### Statement (as proved)

For a finite graded cMPS generator \(T\), \(E_h=e^{hT}\) is a graded CP
transfer, and
\[
 N^{(h)}_P(n)=N_P(nh),\qquad
 \nu_h(\mu)=\sum_{\lambda:e^{h\lambda}=\mu}\nu_T(\lambda).
\]
The scalar equality \(|e^{h\lambda}|=e^{hc}\iff\operatorname{Re}\lambda=c\)
always holds. A spectral line/bound on **all retained sector eigenvalues**
is therefore sampling independent, with compatible retained modes.
The **net-divisor** equivalence needs absence of aliasing and accidental
identification with removed trivial modes. Additive operator FE implies
multiplicative operator FE at every mesh. The converse at a single mesh
needs a consistent logarithm.

### Hypotheses H-*

H-fin. **H-cMPS:**
\(T(X)=QX+XQ^*+\sum_aR_aXR_a^*\), with \(Q\) even and \(R_a\)
homogeneous; this is the standard finite cMPS generator, without an implicit
TP constraint. **H-noalias:** the exponential map is injective on the union
of the rates being compared, including trivial rates and their FE images.
This is a sampling restriction; it holds for all sufficiently small \(h>0\)
for a fixed finite set of rates.

### Proof

1. The Dyson expansion has Kraus words formed from \(e^{tQ}\) and the
   \(R_a\), each homogeneous. Its norm-convergent integrals are CP and
   parity covariant. A homogeneous finite Kraus representation can also
   be obtained by diagonalizing the parity-covariant Choi matrix.
2. \((e^{hT})^n=e^{nhT}\), which proves equality of the ring norms.
3. On a Jordan block \(\lambda I+N\), the exponential is
   \(e^{h\lambda}e^{hN}\), with the same algebraic block dimension.
   Equal exponential eigenvalues add their multiplicities. Subtracting
   parity multiplicities gives the displayed push-forward formula.
4. H-noalias makes this subtraction identical to that before sampling.
   The modulus identity then gives the divisor RH/circle equivalence.
5. If \(JTJ^{-1}=2cI-T\), exponentiation gives
   \(JE_hJ^{-1}=e^{2hc}E_h^{-1}\). Taking a logarithm reverses this only
   when the branch is compatible with all paired rates. The same restriction
   appears for a divisor FE, without the Jordan requirements of operator FE.
6. **A CP aliasing counterexample.** Let
   \(Q=\frac12I-i\operatorname{diag}(0,2\pi)\), take no jumps, and grade
   by \(P=Z\). Then \(T\) has even rates \(1,1\) and odd rates
   \(1\pm2\pi i\). Its continuous supertrace is
   \(2e^L(1-\cos2\pi L)\). At \(h=1\), \(E_h=eI_4\) and the whole
   sampled divisor cancels: \(Z_{P,E_h}=1\). With counting reference rates
   \((1,0)\), the nontrivial continuous odd rates violate the critical bound
   \(c=1/2\), while the sampled assertion is vacuous. The identity is
   checked in `finite/finite_checks.py`.

Trace sampling is exact. Exact recovery of a signed divisor from a single
sampling lattice is a different assertion and is false without H-noalias.

### Status: CORRECTED

Ledger L10.

## D8 — Norm Chernoff theorem and homogeneous jumps

### Statement (as proved)

On a **fixed finite bond**, suppose \(\Phi_h\) is CPTP and parity covariant,
and, in an induced matrix norm,
\[
 \|\Phi_h-I-hT\|=h\delta(h),\qquad\delta(h)\longrightarrow0.
\]
Then \(\Phi_h^{\lfloor L/h\rfloor}\to e^{LT}\) in norm, uniformly for
\(0\le L\le L_0\), and both ring traces converge uniformly there.
The limit is a parity-covariant CPTP semigroup and has a GKSL presentation
\[
 T(X)=-i[H,X]+\sum_a\left(R_aXR_a^*
                  -\tfrac12\{R_a^*R_a,X\}\right),
 \quad [H,P]=0,\quad PR_aP=\pm R_a.
\]
Equivalently \(Q=-iH-\frac12\sum_aR_a^*R_a\) is even. Conversely,
such data give a parity-covariant semigroup. A covariant GKSL generator
admits such a presentation; an arbitrary presentation need not already
have homogeneous jumps or an even Hamiltonian.

For **any homogeneous Kraus representation** of \(\Phi_h\),
\[
 \sum_{a\ {m odd}}\|A_a(h)\|_{HS}^2=O(h).
\]
Thus odd Kraus letters are at most of order \(\sqrt h\), collectively,
and cannot be a drift letter close to the identity. Existence of individual
limits \(A_a(h)/\sqrt h\to R_a\) is not required and is not asserted for an
arbitrarily chosen Kraus list.

### Hypotheses H-*

H-fin. **H-Chernoff-norm:** the preceding first-order expansion holds in
operator norm on the fixed matrix space; this is a substantive approximation
hypothesis. **H-CPTP:** every \(\Phi_h\) is CPTP and commutes with
\(\Gamma\); these are the channel and covariance hypotheses.
**H-GKSL:** finite-dimensional norm-continuous CPTP semigroups have the
GKSL form, with a unique canonical Hamiltonian modulo scalars and a positive
Kossakowski matrix in a fixed traceless orthonormal operator basis. This is
the standard finite-dimensional structure theorem. No unbounded-operator
version is being assumed.

### Proof

1. **Control products.** The expansion gives \(\|\Phi_h\|\le1+Ch\)
   for small \(h\). Also
   \(\|\Phi_h-e^{hT}\|\le h\delta(h)+C'h^2\).
   The telescoping identity for powers gives, for \(nh\le L_0\),
   \[
    \|\Phi_h^n-e^{nhT}\|
      \le C_{L_0}nh(\delta(h)+h).
   \]
   The difference between \(nh\) and \(L\) is at most \(h\), and
   \(e^{LT}\) is norm Lipschitz on this compact interval. This proves
   uniform convergence and the bound \(C_{L_0}(\delta(h)+h)\).
2. **Pass structural properties to the limit.** Commutation with \(\Gamma\)
   passes first to \(T\), then to its exponential. CP and TP are closed
   conditions in finite dimension, so all \(e^{LT}\) are CPTP. The trace
   functionals \(M\mapsto\operatorname{Tr}M\) and
   \(M\mapsto\operatorname{Tr}(\Gamma M)\) are bounded; both converge.
3. **Choose a homogeneous GKSL presentation.** Take a traceless
   Hilbert–Schmidt orthonormal basis consisting of even and odd matrices.
   Covariance and canonical GKSL uniqueness imply that the positive
   Kossakowski matrix commutes with this parity and that
   \(PHP-H\) is scalar. Taking trace makes the scalar zero. Diagonalize
   the positive matrix within its even and odd blocks. Its square roots
   give homogeneous \(R_a\), and \(\sum R_a^*R_a\) is even.
4. **The converse is termwise.** Conjugating the Hamiltonian and dissipator
   terms by \(P\) gives the same generator. If one starts with a different
   GKSL list, reaching canonical form can require scalar shifts of even
   jumps as well as an arbitrary change of jump basis. It is not generally
   an “even unitary remix” of that arbitrary original list.
5. **Bound all odd letters.** In the Choi picture,
   \(C_h=|I\rangle\!\rangle\langle\!\langle I|+O(h)\).
   Homogeneous Kraus vectors diagonalize the Choi parity into even and
   odd blocks. The identity vector is even, so the positive odd block
   of \(C_h\) is \(O(h)\) in norm and hence has trace \(O(h)\).
   That trace is exactly \(\sum_{a\ {m odd}}\|A_a(h)\|_{HS}^2\).
6. **No odd drift.** If \(A\) is odd, then
   \((A-I)+P(A-I)P=-2I\). The triangle inequality in the bond operator
   norm gives \(\|A-I\|\ge1\). A homogeneous letter
   \(I+hQ+o(h)\) must be even. A nonvanishing first-order odd noise
   contribution to the limiting generator has the Kraus scale
   \(\sqrt hR_a\), rather than a drift scale.

For CP transfers without TP, the same norm argument gives a CP semigroup
and the cMPS form \(QX+XQ^*+\sum R_aXR_a^*\). One can average that
presentation with its \(P\)-conjugate, replacing \(Q\) by its even part
and each \(R\) by \((R+PRP)/2,(R-PRP)/2\). The TP restriction on \(Q\)
then follows exactly when TP is assumed.

Under parity covariance there is no parity-changing Hamiltonian term on
the bond in this presentation. An **even** Hamiltonian can nevertheless
give arbitrary oscillation frequencies to odd coherences. Parity-changing
population transitions come from noise; zeros of a net zeta need not detect
every one of those relaxation modes. The fixed-bond norm theorem does not
apply to the unbounded Lie-group generators of D11.

### Status: CORRECTED

Ledger L11–L12 and L38.

## D9 — Poissonized unitary jumps

### Statement (as proved)

Let \(G_r=\sum_i g_i>0\),
\(\Phi=G_r^{-1}\sum_i g_i\operatorname{Ad}U_i\), and
\(T=\sum_i g_i(\operatorname{Ad}U_i-I)\). Then
\[
 e^{tT}=e^{-G_rt}e^{G_rt\Phi},\qquad
 \operatorname{spec}T_k=G_r(\operatorname{spec}\Phi_k-1).
\]
With \(D\) equally weighted inverse-paired letters, a sector Hastings band
is equivalent to the retained rates lying in
\[
 [-G_r(1+\lambda_H),-G_r(1-\lambda_H)],
 \qquad\lambda_H=2\sqrt{D-1}/D.
\]
Remove the fixed rate zero and any explicitly allowed periodic rate
\(-2G_r\). This is an interval of diffusion rates, not an assertion that
they all have the same real part.

### Hypotheses H-*

H-fin and H-hom; **H-rates:** \(g_i\ge0\), with positive total rate, the
standard compound-Poisson assumption. H-unit and equal rates are needed for
the equal-degree Hastings band. With unequal rates, Hermiticity additionally
requires \(g_{\bar i}=g_i\); no equal-degree Hastings theorem for arbitrary
weights is asserted. H-triv-Bass supplies the periodic exclusions if used.

### Proof

The generator is \(G_r(\Phi-I)\). Its summands \(\Phi\) and \(I\)
commute, giving the exponential formula and the affine spectral map,
including Jordan multiplicities. The Poisson expansion
\(e^{-G_rt}\sum_{n\ge0}(G_rt)^n\Phi^n/n!\) proves CP and TP directly.
The two endpoint substitutions give the interval. The underlying labelled
words still have the D3 nonbacktracking lift; this is not a new Ihara
identity for the diffusion generator itself.

For the three Pauli jump types, counted once with total type rates
\(g_X,g_Y,g_Z\), the even rates are
\(0,-2(g_X+g_Y)\) and the odd rates are
\(-2(g_Y+g_Z),-2(g_X+g_Z)\). This follows from the two anticommuting
Paulis for each nonidentity Pauli eigenoperator. The parity rate is twice
the total odd-letter rate, as claimed.

### Status: PROVED

## D10 — A divisor from regular correlations, without a trace

### Statement (as proved)

There is a well-defined **relative resonance divisor** under the hypotheses
below. It is not just the union of the poles of unspecified scalar
correlations. It depends on specified regular spaces, the continuation,
and its finite-dimensional spectral multiplicities.

### Hypotheses H-*

* **H-C0:** \(S(t)\) is a strongly continuous semigroup on a Hilbert space
  \(\mathcal H\), \(\|S(t)\|\le Me^{at}\), and it commutes with a bounded
  self-adjoint grading \(\Gamma\). The exponential bound is standard for
  a \(C_0\) semigroup; the grading is extra structure.
* **H-regular:** fix a dense \(\Gamma\)-stable test space
  \(\mathcal D\subset\mathcal H\), and a specified graded Banach
  realization \(\mathcal B\) of distributions containing \(\mathcal D\)
  densely. Pairings with \(\mathcal D\) separate \(\mathcal B\).
  The semigroup/resolvent realization on \(\mathcal B\) agrees with the
  original matrix elements where both initially exist. Such a compatible
  weighted or anisotropic space is a substantive analytic construction.
* **H-Fredholm:** the resolvent \(R_{\mathcal B}(z)=(z-T_{\mathcal B})^{-1}\)
  continues to a specified connected domain \(\Omega\), meromorphically
  with locally finite poles, finite-rank principal parts, and finite-rank
  Riesz projections. It obeys the resolvent identity. This is an analytic
  Fredholm hypothesis, not a consequence of strong continuity or scalar
  meromorphy alone.
* **H-detect:** the chosen regular test pairings detect every nonzero
  Laurent coefficient of that resolvent. This follows, for example, from
  density and the separating pairings just specified; it prevents an
  artificially invisible resonance.

For the additional trace interpretation, assume:

* **H-trace-dist:** the resonances have real parts bounded above and
  \(\sum_\lambda(m_0(\lambda)+m_1(\lambda))(1+|\lambda|)^{-N}<\infty\)
  for some \(N\), and any proposed regularized/flat trace of \(S(t)\)
  agrees with their signed exponential sum on \(t>0\). The growth condition
  is standard for such spectral distributions; the trace equality is a
  separate trace theorem or an explicit assumption.

### Construction / proof of well-definedness

1. For \(X,Y\in\mathcal D\),
   \(F_{X,Y}(t)=\langle X,S(t)Y\rangle\) has the Laplace transform
   \(\langle X,(z-T)^{-1}Y\rangle\) for \(\operatorname{Re}z>a\).
   H-regular and H-Fredholm specify its meromorphic continuation.
2. For a small contour around an isolated pole \(\lambda\), define
   \[
    \Pi_\lambda=\frac1{2\pi i}\oint R_{\mathcal B}(z)\,dz,
    \qquad m_k(\lambda)=\operatorname{rank}(\Pi_\lambda|_{\mathcal B_k}).
   \]
   The resolvent identity gives a finite-rank idempotent, the generalized
   eigenspace projection. Covariance makes it block diagonal. These ranks
   are the algebraic multiplicities, independent of the contour.
3. Define \(\nu_{\mathcal B}(\lambda)=m_0(\lambda)-m_1(\lambda)\).
   H-detect identifies the unsigned pole support from the entire family of
   correlations. It does not turn scalar pole order into multiplicity:
   a size-\(r\) Jordan block can give a pole of order \(r\), while a
   semisimple eigenvalue of arbitrarily large multiplicity gives simple
   scalar poles. Opposite parity ranks can cancel after detection.
4. Analytic continuation is unique on the fixed connected domain. Thus the
   divisor is well defined for these specified data. Its invariance under a
   change of regular realization needs a further compatibility theorem;
   calling both spaces “regular” supplies no such theorem.
5. Under H-trace-dist,
   \(\sum_\lambda\nu_{\mathcal B}(\lambda)e^{\lambda t}\) converges in
   \(\mathcal D'((0,\infty))\): integrate against a compactly supported
   smooth test function and repeatedly integrate by parts to obtain any
   prescribed inverse power of \(|\lambda|\). This defines the signed
   spectral trace distribution. A meromorphic zeta with pole-minus-zero
   divisor \(\nu_{\mathcal B}\) is determined only up to a zero-free
   holomorphic factor; a determinant normalization/short-time subtraction
   must be separately fixed.

**Continuous spectrum.** There is no canonical scalar signed measure for
an arbitrary nonnormal generator. In the normal case the spectral theorem
gives projection-valued measures, and each pair \(X,Y\) gives its own scalar
measure. A global signed density requires **H-spectral-trace**: specified
positive traces/weights \(\tau_k\) on the sector spectral algebras for which
\(\tau_k(P_k(A))\) are locally finite measures with the needed exponential
integrability. Then \(\nu(A)=\tau_0(P_0(A))-\tau_1(P_1(A))\) is defined,
with no \(\infty-\infty\) subtraction. Without this extra input, use the
separate sector spectral supports or the resonance divisor, not an invented
scalar “continuous divisor.” A Cauchy transform of a continuous measure is
also generally not meromorphic across its support.

With a chosen centre \(c\) and trivial divisor, resonance RH means
\(\operatorname{supp}(\nu_{\mathcal B}-\nu_{\rm triv})
 \subset\{\operatorname{Re}z\le c\}\). It is a condition, not a theorem
about a general \(C_0\) semigroup.

**Relation to shard 02c.** `def:distributional-trace` expressly defines
\(\operatorname{Tr}_{\rm dist}Z(t)=\sum_\rho e^{-\bar\rho t/2}\) by
fiat, and not by a trace theorem. It is an instance of specifying the
spectral distribution once its convergence is proved. Identifying it with
the Riesz multiplicities of a regular-data resolvent or an actual flat trace
is additional work. An operator norm equal to one is compatible with much
faster decay of individual regular correlations; it neither establishes nor
rules out that missing identification.

### Status: CORRECTED

Ledger L13–L14. Well defined under the stated H-*; no Riemann resolvent or
trace theorem is claimed here.

## D11 — Continuous Harrow and its normalization

### Statement (as proved)

Let \(\pi\) be an irreducible tempered unitary representation of
\(SL_2(\mathbb R)\), and let \(\rho=\pi\otimes\bar\pi\) act on
\(HS(H_\pi)\). In the shard-09b normalization put
\[
 T_* =\tfrac12(B_H^2+B_E^2)=2\operatorname{Cas}_\rho+\tfrac12B_W^2.
\]
Then \(\rho\) is tempered and
\[
 \operatorname{spec}(-T_*|_{HS^K})\subset[1/2,\infty).
\]
The bound is sharp: for every discrete series \(\pi=D_k^\pm\), the
\(K\)-invariant spectrum is exactly \([1/2,\infty)\), continuously, and
the endpoint is not a normalizable eigenvector. There is no HS fixed vector.

For the precise walk written in the draft,
\[
 \Phi_h=\frac1{2d}\sum_{j=1}^d
       \big(e^{\sqrt hB_j}+e^{-\sqrt hB_j}\big),
 \qquad T_{\rm walk}=\frac1{2d}\sum_jB_j^2,
\]
the two-generator case has \(d=2\) and
\(T_{\rm walk}=T_*/d\). Its threshold is **\(1/(2d)=1/4\)**.
To obtain \(T_*\) from this equally averaged walk, use steps
\(\exp(\pm\sqrt{dh}\,X_j)\), or speed up time by \(d\).

On a constituent with Casimir \(-s(1-s)\) and \(K\)-type \(m\), the
exact rate is
\[
 -T_* = 2s(1-s)+m^2/2.
\]
Tempered principal constituents have \(s=1/2+ir\); tempered discrete
constituents have \(s=n/2\) and \(|m|\ge n\), not a principal parameter.
Temperedness is a sufficient mechanism for the diffusion bound; it does
not mean that all matrix-coefficient exponents lie on one line or that
the full HS generator has purely continuous spectrum.

In fact, for a unitary representation of \(PSL_2(\mathbb R)\), the
type-zero bound \(-T_*\ge1/2\) is equivalent to temperedness (with the
empty type-zero space allowed). This is a precise diffusion meaning of
“continuous Ramanujan”; it is not a full flow-divisor circle/line theorem.

### Hypotheses H-*

**H-Lie:** use
\[
 H=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
 E=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 W=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
 \quad a_t=\exp(tH/2).
\]
Thus \(a_t\) has hyperbolic translation length \(t\),
\(B_W=im\) on type \(m\), and
\(\operatorname{Cas}=(B_H^2+B_E^2-B_W^2)/4\). These are exactly the
shard-09b choices, not a free rescaling of the generators.

**H-dom:** start on smooth finite-rank tensors and take the self-adjoint
nonpositive realization of the sum of squares supplied by the unitary
representation and its heat convolution semigroup. The smooth vectors
are a core. These are standard closed-realization facts for a Lie-group
sub-Laplacian, and essential when jumps are unbounded.

**H-tempered-dual:** tempered means weak containment in the left regular
representation. The spherical tempered dual of \(PSL_2(\mathbb R)\) is
the principal series \(s=1/2+ir\), with Laplace eigenvalue
\(1/4+r^2\); the other tempered irreducibles are discrete series.
This is standard rank-one Plancherel theory. The centre acts trivially
on \(\pi\otimes\bar\pi\), so only even \(K\)-types occur here.
The accompanying unitary-dual classification says that the non-tempered
irreducibles of PSL are the spherical complementary series and the trivial
representation; this standard fact is also included in H-tempered-dual.

**H-weak-tensor:** tensoring a weak containment with a unitary
representation preserves weak containment. This is the standard Fell
property of unitary representations. Absorption itself is proved below.

**H-mixed-series:**
\(D_k^+\widehat\otimes D_k^-\simeq\int_0^\infty{}^\oplus
 I_{1/2+ir,0}\,dr\), multiplicity one and with no discrete summand,
for integers \(k\ge1\) (\(k=1\) is the SL limit). This is the standard
mixed discrete-series tensor theorem. It is the equal-parameter case of
Groenevelt–Koelink–Rosengren, Theorem 4.1, with their parameters
\(k_1=k_2=k/2\); their explicit transform proves that the measure class
is Lebesgue on \(r>0\). See
[the primary paper, §4.1](https://arxiv.org/pdf/math/0302251).

**H-principal-tensor:** a tensor product of two spherical unitary principal
series of \(SL_2(\mathbb R)\) has discrete-series constituents in addition
to its continuous principal part. This is a standard Pukánszky–Repka
tensor-product theorem (the Repka reference is given under H-repka). It is
used only to refute the purely-continuous assertion for irreducible \(\pi\).

**H-coeff:** the rank-one Harish–Chandra expansions hold for \(K\)-finite
matrix coefficients. This is standard; the leading terms are also obtained
from the radial Casimir equation below. General smooth-vector estimates
require appropriate Sobolev bounds, and arbitrary HS vectors need not have
a common exponential rate.

**H-repka:** for the spherical complementary series \(\pi_s\),
\(1/2<s<1\), the tensor product \(\pi_s\widehat\otimes\pi_s\)
contains a complementary constituent iff \(s>3/4\). In that case the
only complementary constituent is \(\pi_{2s-1}\), of multiplicity one;
the rest is tempered. At \(s=3/4\) no complementary constituent occurs.
This is the standard Repka tensor-product input, stated explicitly as
requested, rather than proved here: Joe Repka, *Tensor Products of Unitary
Representations of SL₂(R)*, **American Journal of Mathematics 100** (1978),
747–774, [DOI 10.2307/2373909](https://doi.org/10.2307/2373909).
The earlier announcement is *Bull. Amer. Math. Soc.* **82** (1976), 930–932,
DOI 10.1090/S0002-9904-1976-14223-1. The 1978 article was not available
for direct text inspection in this session; no theorem number is invented.
The existence direction is independently consistent with Zhang's Theorem
4.1, using \(\alpha=\beta=1-s\), \(\rho=1/2\), and
\(\alpha+\beta<\rho\). See
[Zhang's primary paper](https://arxiv.org/pdf/1402.2950).

### Proof

1. **Absorption.** On \(L^2(G,H_\sigma)\), the unitary
   \((Uf)(x)=\sigma(x)^{-1}f(x)\) satisfies
   \[
    U(\lambda(g)\otimes\sigma(g))U^{-1}f(x)=f(g^{-1}x).
   \]
   Thus \(\lambda\otimes\sigma\simeq\lambda\otimes I_{H_\sigma}\).
   H-weak-tensor and \(\pi\prec\lambda\) imply
   \(\pi\otimes\bar\pi\prec\lambda\otimes\bar\pi\simeq
   \lambda\otimes I\). The multiplicity space can be infinite; “dim σ
   copies” should not be read as a finite multiplier.
2. **Pass to \(K\)-invariants.** In the direct-integral decomposition of
   this tempered representation, discrete series have no type zero.
   On each remaining spherical constituent,
   \(-2\operatorname{Cas}=2(1/4+r^2)\ge1/2\). H-dom and the spectral
   theorem give the asserted closed-operator bound. On the other even
   \(K\)-types add \(m^2/2\); on \(D_n\) the minimum is \(n\ge2\).
   Thus a lower bound \(1/2\) holds on the full HS space as well.
   Conversely, every non-tempered PSL constituent has a type-zero vector
   with rate strictly below \(1/2\): it is either trivial or complementary.
   Any positive direct-integral mass of such constituents violates the
   bound. The unitary-dual classification therefore proves the asserted
   equivalence between this diffusion condition and temperedness.
3. **Sharpness and fixed vectors.** H-mixed-series gives nonzero spectral
   measure in every interval \(0<r<\varepsilon\) for \(\pi=D_k^\pm\),
   proving sharpness and showing the endpoint is continuous. An HS fixed
   vector would be killed by both \(B_H,B_E\), by the nonnegative Dirichlet
   form of \(-T_*\). The generators generate \(G\), so it intertwines
   \(\pi\) with itself. By Schur it is scalar, and a nonzero scalar
   identity is not HS in an infinite-dimensional irreducible representation.
   This proves the absence of a fixed vector. Weak containment alone proves
   the bound, not attainment for every representation; the corrected theorem
   states an explicit family where attainment of the infimum is established.
4. **Check the walk limit.** On a smooth vector in the common fourth-power
   domains, the two Taylor expansions cancel odd terms and give
   \[
    \Phi_hv=v+\frac{h}{2d}\sum_jB_j^2v+O_v(h^2).
   \]
   The averaging and Taylor factors account for both denominators. These
   are strong, core estimates, not a bounded-operator norm expansion.
   The contraction Chernoff theorem on this core gives the corresponding
   strong semigroup limit under H-dom. The coefficient \(T_*/d\) in the
   two-generator case is unavoidable.
5. **The geodesic flow is a different operator.** For a spherical
   coefficient with eigenparameter \(s\), the radial equation is
   \(f''+\coth t\,f'+s(1-s)f=0\). At infinity its indicial roots are
   \(-s\) and \(-(1-s)\). For other fixed \(K\)-types the additional
   radial terms decay, giving the same two leading exponents and descending
   corrections. At \(s=1/2\), a \(t e^{-t/2}\) term can occur.
   In the principal series the leading exponents have real part \(-1/2\).
   In \(D_n\), only the decaying discrete-series branch is present:
   a lowest-type coefficient is exactly \(\cosh(t/2)^{-n}\), with leading
   exponent \(-n/2\). It has further exponents \(-n/2-j\), \(j\ge0\).
   Therefore “tempered iff all exponents are on the critical line” is false:
   discrete series are tempered and decay faster. Even principal-series
   correlations have descendant terms, not just two pure exponentials.
6. **No automatic correlation divisor.** The generator of
   \(\rho(a_t)\) on its Hilbert space is skew-adjoint. Its Hilbert-space
   spectrum, the diffusion spectrum of \(T_*\), and continued poles of
   regular correlations are three distinct objects. A continuous direct
   integral can give a cut instead of discrete poles. D10's analytic
   hypotheses are needed to define any continued divisor.
7. **The full diffusion spectrum need not be purely continuous.** Take
   an irreducible spherical principal series \(\pi_s\), \(s=1/2+ir\).
   Its conjugate is an equivalent spherical principal series.
   H-principal-tensor gives discrete-series constituents of
   \(\pi_s\otimes\bar\pi_s\), whose individual \(K\)-types are
   eigenvectors of the diffusion. Also, without invoking that theorem,
   D12's tempered representation \(D_k^+\oplus D_k^-\) has an entire
   discrete HS odd sector by the polynomial proof given there. Infinite
   bond dimension by itself never implies absence of point spectrum.
8. **Apply H-repka.** For \(s\le3/4\), the tensor square is tempered,
   even though \(\pi_s\) is not. For \(s>3/4\), its spherical
   complementary constituent gives the rate
   \[
    2(2s-1)(2-2s)=4(2s-1)(1-s)<1/2.
   \]
   Its slow geodesic exponent is \(-2(1-s)\). The boundary condition
   \(2(1-s)=1/2\) is exactly \(s=3/4\), whose original Laplace value
   is \(s(1-s)=3/16\). This explains the arithmetic coincidence of
   parameters; it is not a proof of Selberg's automorphic \(3/16\) theorem
   or of the \(1/4\) conjecture.

For completeness, the standard almost-\(L^2\) criterion behind these
tempered estimates is Cowling–Haagerup–Howe, *Almost L² matrix coefficients*,
*J. reine angew. Math.* **387** (1988), 97–110,
[publisher record](https://www.degruyterbrill.com/document/doi/10.1515/crll.1988.387.97/html).
The proof of the diffusion bound above uses absorption and the explicit
rank-one dual, and does not require quoting a stronger uniform coefficient
estimate from that paper.

### Status: CORRECTED

Ledger L15–L18. The complementary-series consequence is conditional on
H-repka; it is not a claimed new proof of that tensor-product theorem.

## D12 — Reflection grading of the continuous representation

### Statement (as proved)

For genuine \(G=PGL_2(\mathbb R)\), take **even \(k\ge2\)** and
\[
 \pi=\operatorname{Ind}_{PSL_2(\mathbb R)}^{PGL_2(\mathbb R)}D_k^+,
 \quad\pi|_{G_0}=D_k^+\oplus D_k^-,\quad P=I\oplus(-I).
\]
Let \(r=\operatorname{diag}(-1,1)\) modulo scalars,
\(\mathcal R=\operatorname{Ad}\pi(r)\), and
\[
 T_{\kappa,\gamma}=\kappa T_*+\gamma(\mathcal R-I),\qquad
 \kappa>0,\ \gamma\ge0.
\]
Use \(\kappa=1\) for shard 09b and \(\kappa=1/d\) for the draft's walk.
This operator commutes with \(\Gamma=\operatorname{Ad}P\).

The exact \(G_0\)-module decompositions are
\[
\begin{split}
 HS_0&\simeq(D_k^+\widehat\otimes D_k^-)
           \oplus(D_k^-\widehat\otimes D_k^+)
       \simeq2\int_0^\infty{}^\oplus I_{1/2+ir,0}\,dr,\\
 HS_1&\simeq\bigoplus_{\ell\ge0}
              \left(D_{2k+2\ell}^+\oplus D_{2k+2\ell}^-\right).
\end{split}
\]
The first direct integral is a unitary equivalence, with Lebesgue measure
class, not a statement that a trace equals an integral against unit density.

On the even \(K\)-invariants the rates of \(-T_{\kappa,\gamma}\) are
\(\kappa(1/2+2r^2)\) and \(\kappa(1/2+2r^2)+2\gamma\).
In the odd sector, for \(n=2k+2\ell\), \(j\ge0\), the two reflection
eigencombinations of types \(m=\pm(n+2j)\) have rates
\[
 \boxed{\ \kappa\big(n+2nj+2j^2\big),\qquad
         \kappa\big(n+2nj+2j^2\big)+2\gamma.\ }
\]
The odd minimum is \(2\kappa k\). There are no odd \(K\)-invariant,
principal, complementary, or trivial constituents. Their leading
\(a_t\)-coefficient exponents are \(-n/2=-(k+\ell)\), followed by
descendants, and not critical-line exponents.

The pointwise equality of the two discrete-series characters on regular
hyperbolic elements is valid. It does **not** give the proposed ordinary
heat supertrace. A localized character expression on the regular semisimple
set is well defined and vanishes on its hyperbolic part; that is the precise
elliptic-support assertion proved below.

### Hypotheses H-*

H-Lie and H-dom, H-mixed-series from D11. **H-SL-dual:** the unitary dual
and index-two Clifford theory apply to these type-I groups; outer reflection
interchanges \(D_k^+\) and \(D_k^-\), while irreducible principal and
complementary series of \(PSL_2(\mathbb R)\) are reflection invariant.
These are standard classification facts. An SL discrete series with lowest
type \(k\) descends to PSL iff \(k\) is even.

**H-highest-weight:** the usual unitary holomorphic model of \(D_k^+\)
has types \(k,k+2,\ldots\) with one-dimensional type spaces, polynomial
smooth vectors, and the corresponding highest/lowest-weight classification.
This is standard discrete-series theory; the positive tensor decomposition
is proved from this model below. The SL limit \(k=1\) has the same positive
Hardy-space model.

**H-HC-character:** admissible discrete series have the usual locally
integrable Harish–Chandra characters, analytic on the regular semisimple
set. Their rank-one formulas below are standard; compare the
[SL₂ reference table, character formulas](https://www.math.utah.edu/vigre/minicourses/sl2/sl2table.pdf),
whose discrete-series parameter is \(k-1\) in our lowest-weight convention.
**H-char-test:** a test function used in a product of these character
functions has compact support inside the regular semisimple set. This is
an explicit localization, not an assertion that a product of distributions
at singular conjugacy classes is defined.

### Proof

1. **Clifford theory and the group issue.** An irreducible representation
   of the identity component induces irreducibly to the index-two extension
   iff it is inequivalent to its reflection conjugate. H-SL-dual gives
   exactly the holomorphic/antiholomorphic discrete-series pairs for PSL.
   With the indicated parity, connected elements are even and the other
   component is odd. Principal/complementary representations that extend
   irreducibly restrict irreducibly, so this construction does not grade
   them. The limit \(D_1\) is a representation of SL with central character
   \(-1\); it is absent from the genuine PSL/PGL assertion.
2. **The generator respects both symmetries needed.** Connected infinitesimal
   generators commute with \(P\). Conjugation by \(r\) fixes \(H\) and
   negates \(E,W\), so it preserves \(B_H^2+B_E^2\). Thus
   \([T_*,\mathcal R]=0\). Also \([\Gamma,\mathcal R]=0\): conjugation
   by an odd unitary is an even superoperator. The reflection is a bounded
   unitary involution, so adding its jump is a bounded perturbation of the
   closed diffusion generator. Heat convolution composed with a Poisson
   reflection jump also directly constructs the CP evolution.
3. **Even decomposition.** Complex conjugation changes \(D_k^+\) into
   \(D_k^-\). H-mixed-series, applied to each diagonal HS block, gives
   exactly the two multiplicity-one principal integrals above, with no
   discrete addenda. Their type-zero rate is \(\kappa(1/2+2r^2)\).
   Reflection interchanges the two diagonal blocks, with an intertwining
   of the diffusion; symmetric and antisymmetric combinations acquire
   jump rates zero and \(2\gamma\), respectively.
4. **Positive tensor decomposition.** In the polynomial model write the
   lowering operator as \(K_-=\partial_z\), raising as
   \(K_+=z^2\partial_z+kz\), and type operator as
   \(2K_0=2z\partial_z+k\). In the tensor square the homogeneous polynomial
   \((z-w)^\ell\) is killed by \(\partial_z+\partial_w\) and has lowest
   type \(2k+2\ell\). It generates \(D_{2k+2\ell}^+\).
   These submodules are mutually orthogonal in the unitary decomposition.
   The type \(2k+2N\) of the tensor square has dimension \(N+1\), and
   the constructed summands \(0\le\ell\le N\) contribute exactly \(N+1\)
   dimensions. All polynomial types are exhausted and their union is dense.
   This proves
   \(D_k^+\widehat\otimes D_k^+=\bigoplus_{\ell\ge0}D_{2k+2\ell}^+\).
   Conjugation gives the negative version and hence the odd decomposition.
5. **Compute the exact diffusion rates.** For \(D_n^\pm\),
   \(\operatorname{Cas}=n(n-2)/4\). Therefore
   \[
    -T_*=\frac{n(2-n)}2+\frac{m^2}2,
    \quad m=\pm(n+2j),\qquad
    -T_*=n+2nj+2j^2.
   \]
   The minimum is \(n\), not \(n/2\). The draft's last displayed
   formula for this eigenvalue was correct in shard units; its “ladder
   n/2” and its preceding \(1/d\) coefficient were not compatible with it.
   Reflection interchanges \(D_n^+\) and \(D_n^-\) and sends type \(m\)
   to \(-m\). Each equal-rate pair thus receives both shifts, zero and
   \(2\gamma\). The odd heat semigroup is trace class for \(t>0\), since
   \(\sum_{\ell,j}e^{-t\kappa(n+2nj+2j^2)}<\infty\).
6. **The P-mode belongs to a different space.** The bounded operator
   \(P=I_+-I_-\) obeys \(T(P)=-2\gamma P\) in the conjugation semigroup
   on \(B(H)\). But \(P\notin HS(H)\), as is \(I\notin HS(H)\).
   It is not an HS eigenmode or an HS divisor pole. Pairing the formal
   bounded rates \(0,-2\gamma\) does not produce an FE for the diffusion
   spectrum: the latter is unbounded to the left and has no reflected
   right-half-plane partner. The reflection jump is not the jump \(P\)
   of `prop:parity-jump-uniform-shift`: that **even bond unitary** shifts
   all \(\Gamma\)-odd modes, whereas the odd bond reflection splits
   both \(\Gamma\) sectors by its own involution eigenvalue.
7. **Flow exponents and symmetric powers.** The lowest-type coefficient
   \(\cosh(t/2)^{-n}\) has leading exponent \(-n/2\). Expanding
   \((1+e^{-t})^{-n}\) shows its descendant exponents. Swapping the two
   positive tensor factors acts on \((z-w)^\ell\) as \((-1)^\ell\), so
   \[
    \operatorname{Sym}^2D_k^+=\bigoplus_{j\ge0}D_{2k+4j}^+,\qquad
    \Lambda^2D_k^+=\bigoplus_{j\ge0}D_{2k+2+4j}^+.
   \]
   The leading exponent lists are \(-(k+2j)\) and \(-(k+1+2j)\).
   They hold also for \(k=1\) on SL and its reflection extension. To use
   them on PGL at \(k=1\), explicitly allow a projective bond representation;
   the central scalar disappears in conjugation. This is a change of
   hypothesis, not a limit representation of PSL.
8. **What the Gamma comparison amounts to.** For \(k=1\) the lowest
   exponents are \(-1,-2,\ldots\), with no zero rung. As divisors of
   meromorphic scalar functions, the two lists match the pole locations of
   \(\Gamma((z+1)/2)\) and \(\Gamma((z+2)/2)\); their product has the
   pole list of \(\Gamma(z+1)\), up to the usual nonzero duplication
   prefactor. This is a statement about lists of lowest exponents. The full
   odd heat determinant uses the quadratic rates in step 5, and a flow
   correlation determinant includes descendant exponents and multiplicities.
   Neither determinant is proved to be one of those Gamma functions.
9. **The character statement that is valid.** With \(t>0\), on a regular
   hyperbolic element conjugate to \(a_t\),
   \[
    \Theta_k^+(a_t)=\Theta_k^-(a_t)
        =\frac{e^{-(k-1)t/2}}{2\sinh(t/2)}.
   \]
   On a regular rotation choose the orientation in which the positive
   series has types \(k,k+2,\ldots\). The boundary values of the geometric
   type sums give
   \[
    \Theta_k^+(k_\theta)=\frac{e^{ik\theta}}{1-e^{2i\theta}},\qquad
    \Theta_k^-(k_\theta)=\frac{e^{-ik\theta}}{1-e^{-2i\theta}}.
   \]
   H-HC-character supplies these as ordinary analytic functions away from
   the singular set. For H-char-test define the localized functional
   \[
    \mathcal C_P(f)=\int_{G_0}f(g)
               |\Theta_k^+(g)-\Theta_k^-(g)|^2\,dg.
   \]
   This integral exists, and the hyperbolic contribution vanishes by the
   first equality. Off the identity component the induced twisted
   character is zero. These observations give the regular elliptic-support
   statement, without multiplying character distributions at their
   singularities.
10. **Why the proposed heat trace is not this functional.** Already on
    even type zero the heat operator is a nonzero multiplication operator
    on a nonatomic \(L^2\) spectral space. It is not compact and not trace
    class. The odd heat operator is trace class by step 5, so subtraction
    cannot make an ordinary even-minus-odd trace. A heat kernel on the
    entire group is also not an H-char-test function. Its pairing with the
    product of singular characters needs a separately defined
    regularization and a trace identity; neither is furnished by finite
    Harrow. Moreover, on hyperbolic elements the formal even and odd
    character contributions are both \(2|\Theta_k^+|^2\), and cancel.
    Hyperbolic classes do not “live only in the even sector,” and discrete
    series do not make the odd dynamics compact.

The polynomial and Lie-algebra calculations in steps 4, 5 and 7 are
independently checked in `finite/continuous_checks.py`.

**Form-degree grading.** The local Dyatlov–Zworski source supplies
\(\det(I-\mathcal P)=\sum_{j=0}^{n-1}(-1)^j
\operatorname{Tr}\Lambda^j\mathcal P\), and equation `eq:Rue` uses
exponent \((-1)^{j+\dim E_s}\) after correcting the sign of the
Poincaré determinant. Its Ruelle convention is
\(\prod_{[\gamma]}(1-e^{-s\ell_\gamma})\), the inverse of the positive
ring-count gas convention. This is a genuine alternating form-degree
construction. It is not the holomorphic/antiholomorphic bond grading above,
nor an identification of a single Selberg determinant with the entire odd
factor. On a hyperbolic surface the transverse complex has degrees 0, 1,
and 2; selecting \(K\)-types \(0,\pm2\) alone does not define an
invariant splitting under all of \(G\) or an \(\operatorname{Ad}P\)
grading. The additional suggested identification in the draft therefore
does not follow from D12.

### Status: CORRECTED

Ledger L19–L24.

## D13 — Every homogeneous unitary qubit channel

### Statement (as proved)

On \(\mathbb C^{1|1}\), take \(D\) inverse-paired homogeneous unitary
letters and set \(b=D-1\). Write the even letters as
\(\operatorname{diag}(a_i,d_i)\), and odd letters as
\(\left(\begin{smallmatrix}0&a_i\\d_i&0\end{smallmatrix}\right)\),
where all displayed entries have modulus one. Define
\[
 r=N_{\rm even}-N_{\rm odd},\quad
 \alpha=\sum_{i\ {m even}}a_i\bar d_i\in\mathbb R,\quad
 \beta=\sum_{i\ {m odd}}a_i\bar d_i.
\]
In the bases \((I,P)\) and \((E_{01},E_{10})\),
\[
 \operatorname{spec}\Sigma_0=\{D,r\},\quad
 \Sigma_1=\begin{pmatrix}\alpha&\beta\\\bar\beta&\alpha\end{pmatrix},
 \quad\lambda_\pm=\alpha\pm|\beta|.
\]
Thus
\[
 Z_{P,T}(u)=
 \frac{f_{\lambda_+}(u)f_{\lambda_-}(u)}
 {(1-u)(1-bu)f_r(u)}.
\]
For a primitive channel, the **sector** Ramanujan condition is
\(|r|,|\lambda_+|,|\lambda_-|\le2\sqrt b\).
The **divisor** condition tests only uncancelled quadratics, as in D4.
If every letter is odd, then \(r=-D\), \(\alpha=0\),
\(\lambda_\pm=\pm|\beta|\), and the period-two sector condition is
\(|\beta|\le2\sqrt b\), after removing the even \(\pm D\) modes.

The numerator is generally not integral, need not be a Weil polynomial,
and need not be the L-polynomial of a curve even when it is an integral
Weil polynomial.

### Hypotheses H-*

H-fin with \(\dim H_+=\dim H_-=1\), H-hom and H-unit, \(D\ge4\).
For the primitive assertion **H-primitive** means exactly that the
normalized fixed eigenvalue is simple and every other eigenvalue has
modulus strictly below one. This is the standard finite-dimensional
mixing condition for these unital Hermitian channels. A Weil
\(b\)-polynomial further presupposes **H-arithmetic**: \(b\) is a prime
power and the reciprocal-root characteristic polynomial is monic integral
with every conjugate root of modulus \(\sqrt b\). These extra arithmetic
conditions are not consequences of unitarity.

### Proof

1. An even letter fixes \(I,P\) and acts on \(E_{01}\) by
   \(a_i\bar d_i\). Its adjoint contributes the conjugate phase.
   An odd letter fixes \(I\), negates \(P\), and interchanges the two
   coherence directions. Summation gives exactly the displayed blocks;
   the odd eigenvalues are \(\alpha\pm|\beta|\).
2. D3 with \(n_0=n_1=2\) removes the explicit edge factors.
   \(f_D=(1-u)(1-bu)\) gives the rational formula.
3. By D4, \(f_\lambda\) and \(f_{\lambda'}\) have no common zero when
   \(\lambda\ne\lambda'\). Thus the \(P\)-quadratic cancels iff
   \(r=\lambda_+\) or \(r=\lambda_-\), with exactly the corresponding
   multiplicities. Under primitivity neither odd value equals \(D\),
   so the constant-mode quadratic cannot cancel. Without primitivity it
   can, and if \(r=D\) there is a second even fixed mode to track.
4. In the all-odd case the even spectrum is \(\{D,-D\}\), the odd
   spectrum \(\{|\beta|,-|\beta|\}\). If \(|\beta|=D\), both odd
   peripheral modes cancel the two even modes and \(Z_{P,T}=1\); there
   is an odd fixed operator and no unique fixed state. For \(|\beta|<D\),
   the state is unique and the channel is period two. The sector band
   criterion follows from D4.
5. For \(X,X,Y,Y,Z,Z\), \(r=\lambda_+=\lambda_-=-2\), so
   \[
    Z_{P,T}=\frac{1+2u+5u^2}{(1-u)(1-5u)},\quad
    \mu=-1+2i,\quad
    N_P(n)=1+5^n-(\mu^n+\bar\mu^n).
   \]
   The first six values are \(8,32,104,640,3208,15392\).
   Counting the smooth curves \(y^2=x^3+4x+b\), \(b=0,1,4\), over
   \(\mathbb F_5\) gives eight points, hence trace \(-2\) and this same
   elliptic L-polynomial. The determinant identity, initial counts, and
   cyclic-word identity are all checked exactly in `finite/finite_checks.py`.
   A cyclic word contributes four iff its Pauli product is proportional
   to \(Z\), and zero otherwise, proving the stated word-count reading.
6. **Nonintegral unitary example.** Set
   \(z=(1+2\sqrt2\,i)/3\), \(U=\operatorname{diag}(z,1)\), and use
   \(U,U^*,U,U^*,X,X\). Then \(D=6,b=5\), \(r=2\),
   \(\lambda_+=10/3\), \(\lambda_-=-2/3\). All three values lie in
   the band, but
   \(N_P(1)=6+2-10/3+2/3=16/3\). The numerator coefficient of \(u\)
   is \(-8/3\). It is not an integral Weil polynomial. Ring norms here
   are weighted sums of squared word amplitudes, not counts of words.
7. **Integral Weil does not imply curve.** Take six \(I\)'s, two \(X\)'s
   and two \(Y\)'s. Then \(D=10,b=9\), even spectrum \(10,2\), odd
   spectrum \(6,6\), and the normalized channel is primitive. The numerator
   is \(f_6(u)^2=(1-3u)^4\), an integral Weil-9 numerator, with every
   reciprocal root equal to three. If it were the L-polynomial of a
   smooth projective connected genus-two curve over \(\mathbb F_9\),
   that curve would have \(9+1-4\cdot3=-2\) rational points, impossible.
   Its actual channel denominator contains \(f_2\) as well as \(f_{10}\),
   and its first ring norm is zero. The exact script verifies this example.

“Weil” is an arithmetic condition on all algebraic conjugates, not just a
numerical modulus test on arbitrary complex entries. A general degree
\(D\) also need not have \(D-1\) a prime power. A curve interpretation
requires substantially more than the circle bound.

### Status: CORRECTED

Ledger L25–L27.

## D14 — Two elementary obstructions

### Statement (as proved)

An ungraded finite transfer has ring zeta \(\det(I-uE)^{-1}\), with no
zeros at finite \(u\). A finite-dimensional CPTP channel on
\(H_+\oplus H_-\), with both summands nonzero and all Kraus letters even,
has at least two stationary states and therefore cannot be a unique-state
graded quantum expander. The analogous finite GKSL statement holds when
the Hamiltonian and all jumps preserve both bond blocks.

### Hypotheses H-*

H-fin; for the second assertion, **H-TP-even:** the channel is TP,
\(\dim H_\pm>0\), and every Kraus letter preserves the two blocks.
These are explicit necessary restrictions. For the generator version use
the finite GKSL hypotheses of D8 with all jumps even.

### Proof

1. A reciprocal polynomial has no finite zeros. Zero transfer eigenvalues
   contribute the constant factor one. The rational function may have a
   zero at infinity; that is not a finite zeta zero.
2. Every even Kraus letter is block diagonal. Restricting
   \(\sum_iA_i^*A_i=I\) to either block gives a CPTP channel on that block.
   A continuous map of its compact convex state space has a fixed state;
   alternatively the Cesàro averages of iterates have a stationary limit
   point. Embed the two block states in the full bond. Their disjoint supports
   make them distinct stationary states. The semigroup argument is identical
   with time averages.

No similar stationary-state existence claim is made on an infinite bond,
where the state space in trace norm is not compact. The zeta statement also
does not extend to arbitrary regularized infinite determinants.

### Status: PROVED

## Correction ledger

Each row records a change to the draft or its surrounding definition. Rows
that restrict a theorem's scope state that restriction explicitly; a
numerical check is not substituted for an analytic theorem.

| ID | Draft claim | Correct statement | Reason / evidence |
|---|---|---|---|
| L01 | Equal even/odd spectral radii force net cancellation. | Equal radii need not give a common eigenvalue. | D1: the single letter \(P\) has even \(1\), odd \(-1\). |
| L02 | The even algebra contains every positive operator. | It contains the parity-invariant positive operators; averaging a positive Perron eigenmatrix produces an even one. | \(I+X\ge0\) is not block diagonal for \(P=Z\); D1. |
| L03 | The graded net Ihara divisor is on the circle iff both entire sectors are in the band. | Test classes with nonzero **net** multiplicity; the full-sector converse needs a no-cancellation hypothesis. | Primitive degree-14 exact counterexample in D4. |
| L04 | The same numerical trivial set describes edge eigenvalues and zeta points. | Zeta points are reciprocals of nonzero edge eigenvalues. | A factor is \(1-u\mu\). |
| L05 | Hastings' word argument gives an odd-sector Alon–Boppana bound. | Only the full positive word trace has that bound; the odd radius can be zero in fixed-degree primitive families. | D5, exact dephasing and depolarizing-qubit tensor family. |
| L06 | A bipartite Ramanujan Cayley graph directly yields a mixing quantum expander through the ordinary second singular value. | That singular value is one. For the all-odd grading, remove the even sign mode to obtain a period-two sector theorem. | D6, \(\Phi(P)=-P\). A different bipartition sign needs its own parity bookkeeping. |
| L07 | The two LPS zetas have numerator degrees 36 and 196 over just four trivial factors. | Reduced degrees are numerically 4/4 and 144/144; the second has a nontrivial denominator of degree 140. | `harrow_audit.py`; the old print statements were not assertions in the 79-check suite. |
| L08 | Every odd eigenvalue or odd constituent supplies a zero. | A zero remains only if its odd multiplicity exceeds its even multiplicity at that point. | D3, D4, D6 factorization. |
| L09 | The qubit is an ordinary irrep of the Pauli group modulo its centre. | It is projective on that abelian quotient; use the actual Pauli group for ordinary Clifford theory. | Ordinary irreps of a finite abelian group are one dimensional. |
| L10 | Exact sampling makes net-divisor RH and FE independent of every mesh. | Sampling pushes forward signed multiplicities and can cancel aliases; use sufficiently small nonaliasing meshes and compatible logarithms. | D7 explicit CP example. |
| L11 | A norm Chernoff statement applies without a fixed-space/domain qualification. | D8 is a fixed finite-bond norm theorem; D11 has unbounded generators and a strong core limit. | Product estimates and the Lie walk Taylor expansion. |
| L12 | Each given odd letter necessarily has a fixed \(\sqrt hR\) limit. | The sum of squared odd Kraus norms is \(O(h)\); a limiting individual list requires a choice of Kraus gauge. | D8 Choi odd-block estimate. |
| L13 | A divisor is the union of scalar correlation poles, signed by parity. | Use finite-rank Riesz projections of a specified meromorphic resolvent, then subtract algebraic multiplicities. | D10; scalar pole order does not measure eigenspace multiplicity. |
| L14 | Continuous spectrum automatically gives a scalar signed measure. | Specify a spectral theorem plus traces/weights, or retain vector-dependent spectral measures. | D10; no spectral measure for a general nonnormal generator. |
| L15 | The displayed equally averaged Lie walk has threshold \(1/2\). | It has threshold \(1/(2d)\); \(1/2\) uses \(T_*\), the shard's faster time. | D11 and exact Lie-algebra check. |
| L16 | Tempered iff every geodesic correlation exponent has real part \(-1/2\). | Principal leading exponents have that real part; discrete series are tempered and have faster exponents, and descendants add further lines. | D11 radial equation and \(\cosh(t/2)^{-n}\). |
| L17 | Infinite-dimensional \(\pi\) implies purely continuous diffusion spectrum and no discrete data. | Continuous and discrete constituents can coexist; grading in D12 exhibits a discrete HS sector. | D11 tensor-product theory; D12 exact odd decomposition. |
| L18 | Weak containment proves the threshold is attained by every tempered \(\pi\). | It proves a lower bound. Sharpness is established here for \(\pi=D_k^\pm\) using the explicit full-support mixed tensor decomposition. | D11; the endpoint is an infimum, not an eigenvector. |
| L19 | All weights, including \(k=1\), give these genuine PGL representations. | Genuine PSL/PGL pairs require even \(k\ge2\); \(k=1\) requires SL/a covering extension or an explicitly projective bond. | The central element \(-I\) acts by \((-1)^k\). |
| L20 | The odd diffusion ladder starts at \(n/2\), with the displayed walk coefficient. | Shard rates are \(n+2nj+2j^2\), and the walk divides by \(d\); reflection produces both shifts in the odd sector too. | D12 exact Casimir calculation. |
| L21 | \(P\) supplies an HS eigenmode at \(-2\gamma\). | It is a bounded eigenoperator, not HS. It supplies no HS divisor point. | Both parity blocks have infinite dimension. |
| L22 | \(\operatorname{str}e^{tT}\) is the ordinary integral of the heat kernel times the squared character difference. | The even heat operator is not trace class. A localized regular-character functional exists; a global heat identity needs regularization. | D12 steps 9–10. |
| L23 | Hyperbolic/geodesic contributions occur only evenly and the odd sector is compact. | The regular even and odd character contributions are equal on hyperbolic elements and cancel. Discrete series have nontrivial hyperbolic dynamics. | D12 hyperbolic character formula. |
| L24 | The lowest exponent ladder is literally the Gamma_C/Gamma_R divisor. | Its positions match shifted Gamma pole lists; the zero rung, multiplicities, descendants, and heat/flow distinction must be addressed separately. | D12 symmetric-square calculation. |
| L25 | The general qubit divisor is Ramanujan iff \(r,\lambda_1,\lambda_2\) all obey the band. | That is the sector criterion. The divisor criterion first cancels equal quadratics. | D13 and the D4 primitive counterexample. |
| L26 | Unitary letters make ring norms integral word counts. | They give weighted squared amplitudes. Even Ramanujan unitary letters can yield \(N_P(1)=16/3\). | Exact D13 example. |
| L27 | A circle numerator is automatically a curve L-polynomial, or at least a Weil polynomial. | Integrality and a prime-power parameter are extra; even an integral Weil numerator need not be a curve numerator. | D13, \((1-3u)^4\) over \(\mathbb F_9\) would give \(-2\) points. |
| L28 | \(\sum\epsilon_iA_iA_i^*=rI\) is signed trace preservation. | In the notebook's map convention it is signed unitality; signed TP uses \(A_i^*A_i\). | D2. |
| L29 | No positive odd operator implies no odd fixed operator. | Only the first implication is true. Uniqueness of the fixed state rules out odd fixed operators in the finite CPTP setting. | The identity channel fixes every coherence; D14 checks. |
| L30 | Dividing the letters by \(\sqrt q\) makes the fixed point \(I\) and gives a channel. | It rescales eigenvalues. An identity fixed point or TP gauge requires the appropriate faithful Perron eigenmatrix. | Definitions below. |
| L31 | Every structural period mode is even. | Period modes can be odd; remove designated modes with their actual parities and multiplicities. | \((\operatorname{Ad}Z+\operatorname{Ad}Y)/2\), graded by \(Z\), has odd eigenoperator \(X\) at \(-1\). |
| L32 | A net-divisor FE is equivalent to an even operator similarity. | Operator similarity also fixes Jordan-block data and requires an actual specified retained realization. | Divisor multiplicities forget nilpotents and cancelling pairs. |
| L33 | A circle divisor is equivalent to a manifest metric on the original sectors. | A positive invariant metric requires a specified retained operator, full sector control, and semisimplicity. | `prop:hp-inner-product-discrete`; hidden modes in D4. |
| L34 | One-sided RH says every parity coherence decays at exactly the critical rate. | It bounds only visible modes; a full-sector line theorem and absence of Jordan growth give the stronger conclusion. | D4, D7, and the signed-divisor definition. |
| L35 | All listed graded spectral examples are already graded CP transfers on doubled bonds. | The Artin–Schreier and Riemann constructions are graded spectral realizations; that Kraus/doubled-bond realization is not supplied. | Explicit scope statements in shards 06b and 04b. |
| L36 | The critical decay rate is determined by the spectral bound of a normalized TP generator. | Supply the second reference rate or a geometric normalization; the TP spectral bound alone is zero. | H-count; amplitude damping has centre \(-\gamma/2\) despite spectral bound zero. |
| L37 | \(T_\sigma\) is the Hashimoto operator of the single averaged matrix \(\sigma(W)\). | It is defined from the individual representation letters and reversal; Bass compresses its determinant to the sum. | D6 step 7. |
| L38 | Covariance forces every given GKSL list to become homogeneous by an even unitary remix alone. | A homogeneous canonical presentation exists; reaching it may involve scalar jump shifts and a general change of noise basis. | D8 canonical GKSL argument. |
| L39 | Removing only the stated pole/period set makes the Riemann and full Selberg tower divisors circle/line type. | Remove the archimedean/topological ladder as appropriate, and specify the first band or a completed factor. | Verdict table below. |
| L40 | Reflection grading identifies the form-degree Selberg grading or a single odd Selberg factor. | They are distinct gradings; the alternating flat determinants carry the orientation sign in `eq:Rue`. | D12 and the local Dyatlov–Zworski source. |
| L41 | The value \(1\) can universally be called trivial in any normalization. | It is trivial only as a designated structural mode in the specified units; accidental eigenvalues at the same value need explicit multiplicities. | Normalization changes and the definition of a retained divisor. |

## Definitions: verdict

### 1. A minimal consistent definition

It is useful to distinguish a **graded CP transfer**
\((H,P,E)\) from a **graded spectral transfer** \((V,\Gamma,M)\).
The latter is just a graded operator or a D10 resonance realization. An
arbitrary graded spectral transfer need not arise as
\(\sum A_i\otimes\bar A_i\) with \(\Gamma=\operatorname{Ad}P\), and
need not have positive ring norms. The distinction is essential for the
notebook's Artin–Schreier, Riemann, and flat-trace constructions.

For either finite category, specify:

* the nonzero lattice divisor or the continuous resonance divisor;
* a **signed trivial divisor**, including multiplicities, supplied for
  structural reasons before applying the spectral test;
* the critical reference pair of H-count, or directly its radius/centre.

Write \(\nu_{\rm ret}=\nu-\nu_{\rm triv}\). When actual dynamical sector
bounds are wanted, specify the retained invariant sector spaces as well.
Do not manufacture a subspace of dimension \(|\nu|\) by silently cancelling
generalized eigenspaces. A formal diagonal realization of the net divisor
is always possible in finite dimension, but need not be the original channel.

**H-real** means \(\nu_{\rm ret}(\bar\lambda)=\nu_{\rm ret}(\lambda)\).
This is standard for real/hermiticity-preserving transfers with
conjugation-invariant trivial data, and must be required in the general
graded spectral category if used below. Let the lattice critical radius
be \(R>0\), and the continuous centre \(c\in\mathbb R\).

| Term | Precise finite statement | Verdict on draft |
|---|---|---|
| One-sided divisor RH | \(|\lambda|\le R\), respectively \(\operatorname{Re}\lambda\le c\), for every point of \(\operatorname{supp}\nu_{\rm ret}\). | Well posed after specifying the retained divisor and scale. It is not a statement about cancelled modes. |
| Divisor FE | \(\nu_{\rm ret}(R^2/\lambda)=\nu_{\rm ret}(\lambda)\), with no retained zero; continuously \(\nu_{\rm ret}(2c-\lambda)=\nu_{\rm ret}(\lambda)\). | This is the minimal FE for a divisor. Trivial data must be paired separately for a full/completed FE. |
| Divisor Ramanujan | Every retained point has modulus \(R\), respectively real part \(c\). | With H-real, equivalent to one-sided RH plus divisor FE. Without H-real, a circle need not imply the holomorphic reciprocal FE. |
| Operator FE | An invertible even similarity pairs the specified retained operators under inversion or affine reflection. | Stronger than divisor FE: Jordan types must match, not just algebraic multiplicities. |
| Manifest form | On the specified retained sector spaces, a positive definite even \(G\) satisfies \(M^*GM=R^2G\), or \(T^*G+GT=2cG\). | Equivalent to **those operators** being diagonalizable with their full spectra on the circle/line. The metric is positive on every retained sector, not on excluded modes. |

**Proof of the finite equivalences.**

1. FE pairs a modulus \(r\) with \(R^2/r\), or a real part \(x\)
   with \(2c-x\); applying the one-sided inequality to both forces equality.
2. Conversely, on the circle/line that paired point is the complex conjugate.
   H-real supplies its same net multiplicity. This proves the divisor FE.
3. If \(M=S\operatorname{diag}(\lambda_j)S^{-1}\) with
   \(|\lambda_j|=R\), take \(G=(S^{-1})^*S^{-1}\). Conversely
   \(G^{1/2}MG^{-1/2}/R\) is unitary, hence diagonalizable. The continuous
   proof replaces unitary by skew-adjoint after subtracting \(cI\).
   Apply this construction separately in both sectors to make \(G\) even.
4. For a finite signed divisor,
   \(N_P(n)-N_{\rm triv}(n)=O(R^n)\) is equivalent to the one-sided
   radius bound. The easy direction is the triangle inequality. For the
   other, take all modes of maximal modulus \(r>R\). After division by
   \(r^n\), they form a nonzero finite trigonometric sum; its Cesàro
   mean squared modulus tends to the sum of the squared nonzero net
   multiplicities. It cannot decay exponentially. The same argument
   permits an \(O(n^aR^n)\) bound for any fixed exponent \(a\) and gives
   the continuous finite-exponential analogue. Jordan powers create no
   polynomial trace terms. None of this infers bounds for invisible modes.

The original manifest definition requires positivity even on odd modes
that may be trivial or cancelled. Restricting it to a specified retained
operator is the minimal correction. A positive metric on an infinite
weighted space also requires domain and norm-equivalence qualifications;
the finite matrix argument does not settle it.

### 2. Growth, normalization and the trivial divisor

**Perron root versus ring growth.** D1 proves \(\rho(E)=\rho(E_0)\).
It does not prove \(\nu(q)=1\), nor that \(N_P(n)\sim q^n\).
For instance, equal even and odd copies of the identity have zero
supertrace at every length. Periodic examples have oscillating leading
coefficients and can vanish at every odd length. To get a leading term
\(q^n\), assume **H-leading**: a simple retained even Perron mode with
no odd mode at \(q\), and every other retained eigenvalue of strictly
smaller modulus. This is a standard spectral asymptotic hypothesis,
not automatic graded positivity.

**Channel gauges.** If \(ER=qR\) with \(R>0\), conjugating letters by
\(R^{-1/2}\) and dividing by \(\sqrt q\) yields a unital transfer.
If \(E^*(L)=qL\) with \(L>0\), the letters
\(q^{-1/2}L^{1/2}A_iL^{-1/2}\) are TP. These are the standard Perron
gauge constructions (**H-faithful-gauge**); a singular Perron matrix
does not furnish a whole-bond gauge. The Perron matrices can be chosen
even by averaging, preserving the grading when they are faithful.
Simply scaling the letters does not implement either similarity.

**Periods and parity.** With the standard irreducible CP Perron theorem
(**H-irreducible-PF**), peripheral eigenvalues form a finite cyclic group
times \(q\). They need not all be even. For a concrete example with
\(P=Z\), \(\Phi=(\operatorname{Ad}Z+\operatorname{Ad}Y)/2\) has a unique
fixed state and \(\Phi(X)=-X\), with \(X\) odd. Thus the draft's trivial
set cannot be specified as a collection of even modes for every graded
channel. A scalar-value set also loses accidental multiplicities; a
designated invariant subspace or signed multiset is the accurate object.

**The parity mode.** D2 supplies it under signed unitality. For unitary
letters it is structurally present, but its value is not thereby exempt
from the expander band. In adjacency units the balance condition is
\(|N_{\rm even}-N_{\rm odd}|\le2\sqrt{D-1}\), unless that mode is an
explicit period mode. In channel units it is
\(|w_{\rm even}-w_{\rm odd}|\le\lambda_H\) for the equal-degree family.
A projective curve's mode at \(1\) is trivial because it is the specified
\(H^0\) partner of \(q\); this does not make every eigenvalue whose
numerical value happens to be one universally trivial.

**Critical units.** An adjacency sum has Perron root \(D\); the graph
critical parameter \(D-1\) is the growth of its nonbacktracking lift.
In continuous time the pair of reference rates is as necessary as the
pair of reference eigenvalues in the lattice. For example an amplitude
damping generator has even rates \(0,-\gamma\) and odd rates
\(-\gamma/2\pm i\omega\): its centre is \(-\gamma/2\), despite
spectral bound zero. There is no way to recover \(\gamma\) from
“\(q=\rho\)” after TP normalization alone.

### 3. Graded quantum expander

For a fixed finite CPTP parity-covariant map with a unique stationary state,
the eigenvalue definition is well posed once the permitted peripheral
subspaces are specified. The stationary state is even by covariance and
uniqueness. Uniqueness rules out odd fixed operators: if an odd Hermitian
fixed operator existed, it would be a traceless fixed direction. In finite
dimension a CPTP map's Hermitian fixed space is spanned by stationary states
(equivalently apply the positive ergodic projection to its positive and
negative parts), contradicting uniqueness.

The minimal distinctions are:

* A **mixing spectral graded expander** has a simple stationary eigenvalue,
  every other even eigenvalue bounded in modulus by \(\lambda_0<1\), and
  every odd eigenvalue bounded by \(\lambda_1<1\). For a nonunital TP
  map, use the invariant trace-zero space when removing the stationary line.
* A **periodic version** records and removes its peripheral modes explicitly.
  The all-odd Harrow examples have the even \(-1\) mode and fit this version.
  They are not mixing as single-step channels.
* A **sector Ramanujan** mixed-unitary Hermitian family obeys the Hastings
  upper bound in each retained sector for its specified inverse-paired
  degree. This is stronger than “its graded Ihara divisor is Ramanujan.”
  D5 prevents calling the odd upper bound universally optimal by a separate
  odd Alon–Boppana theorem.
* In a nonnormal channel, an eigenvalue bound controls asymptotic decay,
  potentially with Jordan polynomial factors. It is not a single-step
  singular-value contraction bound. A spectral radius bound on the odd
  sector is not a statement that every coherence has that exact decay rate.

The letter degree is data: redundant copies change the Hastings benchmark
even if normalized copies implement the same channel. There is no unique
degree attached to a channel unless a Kraus/word convention is retained.

### 4. Verdict for the notebook's cases

The table uses the corrected meanings above. “Conditional” identifies a
named mathematical input or an unproved realization, rather than an
unperformed numerical test. This report does not prove RH or Selberg's
\(1/4\) property for an arbitrary surface.

| Case | Graded CP transfer / expander? | Divisor RH, FE and manifest verdict with the stated trivial set | Minimal change |
|---|---|---|---|
| Regular Ramanujan graphs | Adjacency and Hashimoto are classical operators. A graph adjacency matrix is not automatically a doubled Kraus transfer. | The nonbacktracking **ungraded** divisor has circle poles after removing edge \(\pm1\) and constant/bipartition pairs. Bass supplies reciprocal FE. A manifest metric requires semisimplicity, which can fail at band endpoints. | Distinguish adjacency degree \(D\) from edge growth \(D-1\); retain multiplicities and an endpoint Jordan qualification. |
| Weil–LPS block channels of 05 | Each irreducible Weil block is an ungraded mixed-unitary expander under the stated LPS/representation inputs. | The direct channel is of real band type. Its ungraded Ihara zeta has poles on the circle, and **no zeros**. Standard Ihara trivial factors suffice; operator-manifest requires the same Jordan check. | Apply the circle definition to the Hashimoto lift. The last paragraph of 05 calling these “nontrivial zeros” should say poles. |
| Full Weil representation graded by even/odd functions | All letters preserve the two inequivalent Weil blocks, so there are at least two stationary states. It is not a unique-state graded expander. | The block-channel results alone do not prove a bound on the cross-transfer coherences or a single-simple-Perron graded divisor with the draft's trivial prescription. | Work on the irreducible ungraded blocks, or establish a new full-bond sector theorem with its actual trivial multiplicities. |
| D6 induced PGL finite examples | Genuine balanced graded CP channels; all-odd LPS letters give a unique state and period two. | Both nonperipheral adjacency sectors obey the band under LPS. Net Ihara zeros and any remaining nontrivial poles are on the circle. Trivial \(\pm b,\pm1\) suffice for this periodic lift. The printed curve/genus formulas fail. | Use “period-two graded expander,” subtract net multiplicities, and do not assert a curve denominator. |
| Six-letter Pauli example | A strictly mixing graded mixed-unitary channel, with nonstationary eigenvalues \(-1/3\). | Its **Ihara** zeta is exactly the elliptic zeta of D13, with trivial edge values \(1,5\), circle zeros and FE. The direct adjacency transfer has \(Z_P(u)=(1+2u)/(1-6u)\), whose zero is at eigenvalue \(-2\), not on \(|\mu|=\sqrt6\). | Keep direct-transfer and nonbacktracking zetas separate; use the true/projective Pauli group as in D6. |
| 06h projective elliptic tensor | A genuine four-letter graded CP transfer; \(E/q\) is unital, TP, and mixing for the displayed \(q>1\) data. | Even eigenvalues \(q,1\), odd \(\pi,\bar\pi\), with \(|\pi|=\sqrt q\). The stated trivial pair works; visible even duality and unitary odd block prove FE and manifest circle form, including a semisimple real double zero. | No spectral correction for this example. The tensor formula needs nonnegative \(t-q/t\); projective \(t=(q+1)/2\) ensures it. |
| 06h affine elliptic tensor | Genuine for \(t=q/2\) when \(q\ge4\), including the notebook example; mixing after division by \(q\). | Even eigenvalues \(q,0\); zero is invisible in lattice zeta. Odd circle/manifest form holds. The full transfer is singular and has no full inverse FE; the \(H^0\) partner of \(q\) is absent. | Either impose FE only on the retained divisor, or pass to the projective completion/tensor. Do not assert a finite-generator exponential embedding of this singular transfer. |
| Artin–Schreier super-transfer of 06b | A graded **spectral** transfer; the notebook does not construct homogeneous Kraus letters on a bond with this doubled spectrum. It is not yet a graded quantum expander in the CP sense. | After removing \(q,1\) and ignoring nilpotent zero modes of the de Bruijn block, the diagonal Frobenius block is \(\sqrt q\)-unitary. Curve duality/Weil inputs supply FE and RH; the diagonal realization is manifest. | Admit the larger graded spectral category, or supply a separate CP realization. Do not apply D1 or D8 to it merely from the grading. |
| Riemann graded generator of 04b | A graded spectral semigroup \(\mathbb C_+\oplus(K_S\oplus\text{ladder})_-\), with one fixed vector under the shard's assumptions. It is not a constructed doubled-bond cMPS/GKSL transfer. | The regular nontrivial-zero modes have centre \(-1/4\) **iff RH**. The odd ladder \(-(k+1/2)\), \(k\ge1\), lies strictly to the left and is not in the draft's finite trivial set. It prevents a full single-line/FE statement even assuming RH. A compatible regular resolvent and manifest metric are not established. | Specify reference rates \(0,-1/2\), remove the archimedean ladder as structural data, distinguish completion of the pole pair, and supply D10's analytic realization. |
| Selberg flat tower of 09c | A flat-trace/dynamical determinant construction; no graded Kraus realization is supplied. The heat Lindbladian and the geodesic flat determinant are different operators. | The full tower has first band \(-1/2\pm ir_j\), descendants \(-1/2-k\pm ir_j\), and integer topological/constant modes. The draft's pole/period trivial set does not make the entire tower single-line or reflection symmetric. The nonconstant **first band** is on the critical line iff there is no Laplace eigenvalue in \((0,1/4)\). | Select the first band (or the appropriate Selberg factor and its topological completion), rather than declare every descendant trivial without specifying the factor. In the cusp case include the scattering/continuous terms and a regularized trace. |

For the elliptic row, the standard genus-one Frobenius statement used in D13
and 06h is **H-elliptic**: the point counts of a smooth elliptic curve are
\(q^n+1-\pi^n-\bar\pi^n\), with \(\pi\bar\pi=q\) and trace
\(q+1-\#E(\mathbb F_q)\). For the Artin–Schreier row, **H-Weil-curve**
is the corresponding Weil theorem and Frobenius duality for the smooth
projective curve; the local 06b shard explicitly lists its conditional
inputs. These are standard arithmetic theorems, not implications of CP.

The simplest dimension warning about identifying the Artin–Schreier
construction with a doubled graded bond is that every such bond has
\(n_0-n_1=(D_+-D_-)^2\ge0\), while its formal cohomological grading
can have more odd than even dimensions. Ring-norm positivity and a positive
Kraus realization are additional requirements beyond a signed determinant.

## Numerical checks

All new scripts are in `notes/ramanujan-graded/finite/`. They print a tally
and fail with an assertion on a failed check. No tests or code elsewhere
were edited. Floating-point comparisons are diagnostic checks; the report
distinguishes them from exact algebra and infinite-dimensional theorems.

| Script written | Scope | Printed tally | Saved output |
|---|---|---|---|
| `finite/finite_checks.py` | Exact D1/D4/D5 counterexamples, primitive zero-odd family, Pauli Bass and word identities, nonintegral/Weil-but-not-curve examples, sampling and CPTP Chernoff checks | **50/50 checks passed** | `finite/finite_checks.txt` |
| `finite/harrow_audit.py` | Reuses only the finite group representation construction functions, then independently matches sector multiplicities and reduces the two LPS divisors | **16/16 checks passed** | `finite/harrow_audit.txt` |
| `finite/continuous_checks.py` | Exact Lie normalization, lowest-weight vectors, symmetric/exterior parity, rate formulas and elementary exponent checks | **66/66 checks passed** | `finite/continuous_checks.txt` |

The supplied `scripts/graded_ramanujan.py` was rerun unchanged:
**79/79 checks passed**, saved as `finite/baseline_graded.txt`.
The supplied `scripts/zeta_conditions.py` was also rerun unchanged:
**all 26 checks passed**, saved as `finite/baseline_zeta.txt`.
The group audit and the supplied graded script read functions from
`scripts/weil_lps.py`. The 79-check script's unasserted numerator-degree
printout is specifically corrected by the additional audit.

Reproduce the new checks from the repository root, e.g.

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 notes/ramanujan-graded/finite/finite_checks.py
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 notes/ramanujan-graded/finite/harrow_audit.py
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python3 notes/ramanujan-graded/finite/continuous_checks.py
```

The three new scripts pass **132/132** checks; including the two unchanged
baseline runs, **237/237** checks pass. This tally does not assert numerical
verification of H-repka, analytic continuation, an infinite trace identity,
or the RH/automorphic conjectures.

## Final tally

| Status | D-items | Count |
|---|---|---:|
| PROVED | D2, D3, D9, D14 | 4 |
| CORRECTED | D1, D4, D6, D7, D8, D10, D11, D12, D13 | 9 |
| REFUTED | D5 | 1 |
| OPEN | None of the fourteen replacement tasks; the explicitly identified external realization problems remain unproved | 0 |

**PROVED 4 / CORRECTED 9 / REFUTED 1 / OPEN 0**
