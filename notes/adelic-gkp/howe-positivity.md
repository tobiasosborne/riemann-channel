# Is the natural symplectic form a polarisation?

Author: `claude:fable-5.1`, 2026-10-05, at TJO's request ("Take this natural next step": Howe's positivity on the three ordinary examples of `lattice-tower.md`). Status: **a record, not a round.** Nothing is registered in `db/claims.tsv`; no REFUTE review has run; no shard. Checks: `checks/check_howe_positivity.py`, output `checks/output_howe_positivity.txt` (14/14; needs PARI through `cypari2`, see the script header).

**Verdict.**

- **For one mode, yes.** For the E mode and for the Pauli-qubit curve, $\Omega$ or $-\Omega$ is a polarisation in Howe's sense, depending on a choice that Deligne's construction leaves open. The lattice with its standard form is a principally polarised elliptic curve.
- **For $K_4$ with one negative edge, no, for every choice.** The standard form $\Omega$ is not a polarisation of the abelian variety that Deligne's theorem attaches to the lattice. The reason is structural: both $\lambda$ and $-\lambda$ occur in the fermionic spectrum.
- **It can be repaired, and the repair is explicit.** Every compatible form is $\Omega(x,Py)$ with $P$ a function of the signed adjacency matrix. A unimodular $P$ with the right signs exists, so the variety is principally polarisable, only not by $\Omega$.
- **It is not always broken for several modes.** A flux on $K_6$ ($q=5$, six modes) has no $\pm\lambda$ pair, and there $\Omega$ itself is a principal polarisation.
- **This corrects one sentence of `lattice-tower.md`.** The vacuum and the complex structure of Deligne's lift are two different invariant complex structures in general. They differ by a sign on each mode.

## 1. What is tested

Definitions from Goresky and Tai (`refs/src/1701.07742/main.tex:3474-3497`, `:3556-3563`). For a Deligne module $(T,F)$ with $V=qF^{-1}$, the algebra $K=\mathbb Q[F]$ is a product of CM fields and its conjugation swaps $F$ and $V$. A **CM type** $\Phi$ chooses one embedding $K\to\mathbb C$ from each conjugate pair. A symplectic form $\omega$ on $T$ with $\omega(Fx,y)=\omega(x,Vy)$ is **$\Phi$-positive** when $\omega(x,\iota y)$ is symmetric and positive definite for a purely imaginary $\iota\in K$ whose images under all $\varphi\in\Phi$ are positive imaginary.

Deligne's construction fixes an embedding $\varepsilon$, which gives a $p$-adic valuation on the algebraic numbers inside $\mathbb C$, and with it the CM type

$$
\Phi_\varepsilon=\{\varphi:\ \mathrm{val}_p\,\varphi(F)>0\}:
$$

of each pair of conjugate Frobenius eigenvalues, the one that is not a $p$-adic unit. **Howe's theorem** (`:3568-3590`): $\omega$ is a polarisation of the abelian variety exactly when it is $\Phi_\varepsilon$-positive.

Here $T=\mathbb Z^{2n}$, $F=M$, $\omega=\Omega$. Take $\iota=F-V$. Then $\Omega(x,\iota y)$ is twice the Weil form, which is positive definite (P1). So

$$
\Omega\ \text{is positive for}\quad\Phi_+=\{\varphi:\ \mathrm{Im}\,\varphi(F)>0\},
$$

the eigenvalues in the upper half-plane. **The question is whether the eigenvalues in the upper half-plane are exactly the $p$-adic non-units, for some $\varepsilon$.** All choices of $\varepsilon$ are covered by fixing one complex embedding of the splitting field and running over its primes $\mathfrak{P}$ above $p$; write $S_{\mathfrak{P}}$ for the set of eigenvalues with positive valuation at $\mathfrak{P}$.

## 2. Results

| example | modes | primes above $p$ | $S_{\mathfrak{P}}=\Phi_+$ | $S_{\mathfrak{P}}=\overline{\Phi_+}$ | conclusion |
|---|---|---|---|---|---|
| E mode ($q=2$) | 1 | 2 | 1 | 1 | $\Omega$ for one choice, $-\Omega$ for the other |
| Pauli six ($q=5$) | 1 | 2 | 1 | 1 | the same |
| $K_4$, one negative edge ($q=2$) | 4 | 4 | 0 | 0 | neither, for every choice |
| $K_6$, a flux without $\pm\lambda$ pairs ($q=5$) | 6 | 16 | 1 | 1 | $\Omega$ for one choice, $-\Omega$ for another |

The $K_6$ flux has fermionic eigenvalues $-2.759,\ -1,\ -1,\ -1,\ 1.695,\ 4.064$, all inside $2\sqrt5=4.472$. For it the sixteen primes realise all sixteen sign patterns on the four distinct eigenvalue pairs, and one of them is $\Phi_+$. So for a suitable $\varepsilon$ its fermionic sector, **with the standard form**, is a principally polarised ordinary abelian variety of dimension 6 over $\mathbb F_5$.

## 3. Why $K_4$ with one negative edge fails

**Proposition.** If $\lambda$ and $-\lambda$ are both fermionic eigenvalues ($\lambda\ne0$), then neither $\Omega$ nor $-\Omega$ is $\Phi_\varepsilon$-positive, for any $\varepsilon$.

*Proof.* The Frobenius eigenvalues for $-\lambda$ are the negatives of those for $\lambda$. A valuation does not see a sign, so every $S_{\mathfrak{P}}$ contains $\mu$ together with $-\mu$. These two have imaginary parts of opposite sign, so $S_{\mathfrak{P}}$ is neither $\Phi_+$ nor its conjugate. ∎

$K_4$ with one negative edge has eigenvalues $\pm1,\pm\sqrt5$. The four primes above 2 give exactly the four sign patterns that are odd in $\lambda$ (P2, P4).

**The symmetry behind it.** There is a signed permutation $D$ of the vertices with $DA_sD^{-1}=-A_s$, and every such $D$ has order four; some have $D^2=-1$. For those, $\Gamma=\mathrm{diag}(D,-D)$ anticommutes with the step, reverses $\Omega$, and squares to $-1$ (P6). It exchanges the mode $\lambda$ with the mode $-\lambda$ and reverses its orientation. It is an anti-symplectic symmetry of the kind a time reversal with $T^2=-1$ would be.

## 4. The repair

The spectrum of $A_s$ is simple, so the forms compatible with the step are exactly

$$
\omega_P(x,y)=\Omega\bigl(x,\ (P\oplus P)\,y\bigr),\qquad P=p(A_s)\ \text{a rational polynomial in}\ A_s,
$$

and $\omega_P$ is positive for the CM type $\{\varphi:\ \mathrm{Im}\,\varphi(F)\cdot p(\lambda_\varphi)>0\}$. To be a polarisation, $p$ must take opposite signs at $\lambda$ and $-\lambda$.

- **$P=A_s$**, that is $\omega(x,y)=\Omega(x,(F+V)y)$: a polarisation for one of the four primes, of degree $\det(A_s)^2=25$ (P4).
- **A principal one.** The order $R=\mathbb Q[A_s]\cap M_4(\mathbb Z)$ contains $\mathbb Z[A_s]$ with index 8, and it contains the unit

$$
P=\begin{pmatrix}-1&-2&1&1\\-2&-1&1&1\\1&1&-1&0\\1&1&0&-1\end{pmatrix},\qquad\text{eigenvalues}\ \ 1,\ -1,\ \varphi^{-3},\ -\varphi^{3}\quad(\varphi=\tfrac{1+\sqrt5}2),
$$

of determinant 1 and with opposite signs at $\pm1$ and at $\pm\sqrt5$. So $\Omega(x,Py)$ is unimodular and is a polarisation for one of the four primes (P5).

So the abelian variety of $K_4$ with one negative edge is principally polarisable, by $\Omega$ twisted with a unit of the real algebra $\mathbb Q[A_s]$. This is the same kind of object as the unit squeezes of note §14.

**In GKP terms.** A lattice with a symplectic form of determinant $d^2$ is the stabiliser lattice of a GKP code of dimension $d$; a principal polarisation is a qunaught. With $\Omega$ the lattice is a qunaught for the vacuum. With $\Omega(x,A_sy)$ it is a code of dimension 5 for the arithmetic structure. With $\Omega(x,Py)$ it is again a qunaught, for the arithmetic structure.

## 5. What it means: two invariant complex structures

When all eigenvalues are on the circle there are two complex structures on phase space that commute with the step.

| | the vacuum $J_+$ | the arithmetic structure $J_\varepsilon$ |
|---|---|---|
| defined by | the step rotates every mode forwards | the step acts on the holomorphic directions by its $p$-adic non-units |
| CM type | $\Phi_+$ | $\Phi_\varepsilon$ |
| $\Omega(x,Jx)$ | positive: a Gaussian state | positive only if $\Phi_+=\Phi_\varepsilon$ |
| complex torus | a principally polarised complex abelian variety with the step as an endomorphism | the complex points of Deligne's canonical lift |

They are related by a sign on each mode, $J_\varepsilon=\sigma J_+$ with $\sigma_j=+1$ when the forward-rotating eigenvalue of mode $j$ is the $p$-adic non-unit. The arithmetic polarisation is $\Omega$ with the orientation of the modes with $\sigma_j=-1$ reversed (and rescaled by a unit): a particle–hole exchange on those modes.

Consequences:

- **Correction to `lattice-tower.md` §6.** "The vacuum is the complex structure of the lift" holds when $\sigma$ is constant: for one mode, and for the $K_6$ flux. For $K_4$ with one negative edge it is false for every $\varepsilon$. The lattice and the syndrome torus, as a real torus with the step, are those of the lift in all cases.
- **Positivity is unaffected.** For the arithmetic polarisation the positive form of Howe's condition is $2\mathcal Q(x,\lvert P\rvert y)$: the Weil form composed with a positive operator that commutes with the step. The Rosati involution is the same for every $\omega_P$, namely $F\leftrightarrow V$. So Weil positivity and the positivity of the arithmetic polarisation are the same statement.
- **A new invariant.** The sign vector $\sigma$, up to the choice of prime, compares an archimedean ordering (which eigenvalue is in the upper half-plane) with a $p$-adic one (which is the non-unit). It is forced to be odd under $\lambda\to-\lambda$; the complete list of constraints is the locking rule of `sign-vector.md`.

## 6. Which abelian variety

For $K_4$ with one negative edge the Weil polynomial is $(x^2-x+2)(x^2+x+2)(x^4-x^2+4)$ (P6). Up to isogeny over $\mathbb F_2$ the variety is the product of an elliptic curve with 2 points, an elliptic curve with 4 points (the curve $E$ of the earlier pages), and a simple abelian surface. Over $\mathbb F_4$ the Weil polynomial is $\bigl((y^2+3y+4)(y^2-y+4)\bigr)^2$: the variety becomes isogenous to $E_1^2\times E_2^2$ with $E_1,E_2$ elliptic curves with 8 and 4 points over $\mathbb F_4$, with complex multiplication by $\mathbb Q(\sqrt{-7})$ and $\mathbb Q(\sqrt{-15})$.

## 7. Status and checks

| statement | status |
|---|---|
| definitions; Deligne's CM type; Howe's theorem | cited by line from Goresky–Tai on disk |
| $\Omega$ is $\Phi_+$-positive | elementary; checked exactly (P1) |
| the table of §2 | computed with PARI: splitting field, its primes above $p$, valuations of the eigenvalues (P2, P7) |
| the proposition of §3 | proved above; checked (P3) |
| the forms $\omega_P$, the degree-25 polarisation, the unit $P$ | elementary; checked exactly (P4, P5) |
| the symmetry $\Gamma$ | checked (P6); the time-reversal reading is an analogy |
| the two complex structures and $\sigma$ | follows from the definitions; not separately checked |
| isogeny factors | from the factorisation (P6); "simple" from irreducibility of $x^4-x^2+4$ |

Not done: the non-ordinary examples; whether the principal polarisation of §4 makes the variety a Jacobian or a Prym.

## 8. Next

- **The sign vector $\sigma$ on the graph side:** done, see `sign-vector.md` (a single mode's sign is free; locked sets of modes and their signs are decided by a residue rule).
- **Jacobian or Prym.** With the principal polarisation of §4, decide whether the abelian fourfold of $K_4$ with one negative edge is the Jacobian of a genus-4 curve over $\mathbb F_2$ or the Prym of a double cover.
- **The $K_6$ example.** It is the first several-mode case where the lattice with its standard form is a principally polarised abelian variety; it is the natural place to compare the vacuum picture with the arithmetic one mode by mode.
