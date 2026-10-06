# The lattice without a lift: non-ordinary fluxes, and which abelian variety

Author: `claude:opus-5.5`, 2026-10-06, lane B of an orchestrated session

Status: a record, not a round; nothing registered in db/claims.tsv; no REFUTE review; no shard. Each statement carries one of
*standard* (quoted from memory, not byte-cited: `refs/src/` is absent in this container), *proved here*, *checked*
(`checks/check_no_lift.py`, output `checks/output_no_lift.txt`, 50 of 50 pass), *sketched*, *heuristic*, *open* or *negative finding*.
Continues `lattice-tower.md` §§6, 9 and `howe-positivity.md`; uses `graph-super.md` §§1, 4, 5 and `locks.md` §§1–3.

**A correction to the brief, first.** $K_5$ is 4-regular, so $q=3$, not $4$. The existing pages and `check_super_gkp.py` use $q=3$
(the band edge $2\sqrt3=3.464$ in `graph-super.md` §6). All three examples below therefore live over a prime field. *Checked (N1).*

**Verdict.**

- **Which abelian variety.** Up to isogeny over $\mathbb F_q$: $K_4$ with one negative edge is $E_{2}\times E_{4}\times S$, Petersen with the
  dodecahedral flux is $S^3\times E_{ss}^4$ over $\mathbb F_2$, and $K_5$ with the pentagon flux is $S'^2\times E'_{ss}$ over $\mathbb F_3$.
  $S$ is the Jacobian of $y^2+(x^2+x)y=x^5+1$, and $S'$ is a Jacobian too. Petersen and $K_4$ share the same simple surface $S$.
  `howe-positivity.md` §6 is confirmed.
- **The half turn makes these varieties Weil restrictions.** All three spectra are symmetric under $\lambda\to-\lambda$. So
  $\det(x-M)=Q(x^2)$, and $K_4$ and Petersen are, up to isogeny, Weil restrictions from $\mathbb F_4$. For $K_5$ the degree of $Q$ is odd,
  so it is not one.
- **The supersingular mode is the fixed point of the half turn.** Eigenvalue $\lambda=0$ gives Frobenius $\pm i\sqrt q$. On that block the
  normalised step is itself a quarter turn and **is** the vacuum: $J=M/\sqrt q$. The $p$-adic valuation cannot choose between $\mu$ and
  $\bar\mu=-\mu$, so Deligne's rule picks no CM type there.
- **The lattice comes from the category, not from a lift.** $q$ is prime, and no eigenvalue is $\pm\sqrt q$. So $(\mathbb Z^{2n},M_s)$ is an object
  of Centeleghe–Stix's category, an abelian variety over $\mathbb F_p$ that is not ordinary. It is not the product of its ordinary and
  supersingular parts: the lattice is glued at 5.
- **Positivity.** RH holds and the vacuum exists and is unique. On the ordinary block, $\Omega$ again fails Howe's test, by the half turn. On
  the supersingular block there is no arithmetic $J$ to compare the vacuum with. A unimodular twisted form with the arithmetic sign pattern
  exists for $K_5$; for Petersen a search of a subfamily found none.

## 1. The examples

The step is $M=\begin{pmatrix}0&-1\\q&A_s\end{pmatrix}$ on $L=\mathbb Z^{2n}$. Its adjoint is $V=qM^{-1}=\begin{pmatrix}A_s&1\\-q&0\end{pmatrix}$, and the
Weil form is $\tfrac12\Omega(M-V)=\begin{pmatrix}q&A_s/2\\A_s/2&1\end{pmatrix}$ with $\Omega=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$. The fluxes are rebuilt
exactly as in `check_super_gkp.py`. For Petersen, the dodecahedral spectrum occurs for 2 of the 64 flux classes, and the first one is used: the
non-tree edges $(1,2),(3,4),(4,9),(7,9)$ are negative.

| example | $q$ | spectrum of $A_s$ | $\det(x-M)$ over $\mathbb Z$ | $n$ | $p$-rank | $\#A(\mathbb F_q)$ |
|---|---|---|---|---|---|---|
| $K_4$, one negative edge | 2 | $\pm1,\ \pm\sqrt5$ | $(x^2-x+2)(x^2+x+2)(x^4-x^2+4)$ | 4 | 4 (ordinary) | 32 |
| Petersen, dodecahedral | 2 | $\pm\sqrt5$ (3 each), $0$ (4) | $(x^2+2)^4\,(x^4-x^2+4)^3$ | 10 | 6 | 5184 |
| $K_5$, pentagon negative | 3 | $\pm\sqrt5$ (2 each), $0$ (1) | $(x^2+3)\,(x^4+x^2+9)^2$ | 5 | 4 (almost ordinary) | 484 |

All three statements below are *checked* (N1–N3):

- the factorisations in the table;
- the Weil form is positive definite in exact arithmetic, so RH holds. Its smallest eigenvalue is $0.275$, $0.275$ and $0.500$;
- the product of the distinct factors annihilates $M$, so $M$ is semisimple.

The counts $\#A(\mathbb F_q)=\det(1-M)$ agree with the signed-Laplacian determinants of `graph-super.md` §1.

## 2. Isogeny factors

**What I use (Honda–Tate, *standard, from memory*).** Tate, "Endomorphisms of abelian varieties over finite fields" (1966): two abelian
varieties over $\mathbb F_q$ are isogenous iff they have the same characteristic polynomial of Frobenius. Honda, "Isogeny classes of abelian
varieties over finite fields" (1968), and Tate, "Classes d'isogénie des variétés abéliennes sur un corps fini" (Sém. Bourbaki 1968/69):
simple isogeny classes correspond bijectively to conjugacy classes of $q$-Weil numbers $\pi$. The algebra $\mathrm{End}^0$ is the division
algebra over $\mathbb Q(\pi)$ with these invariants:

- $\mathrm{inv}_v=\frac{v(\pi)}{v(q)}[\mathbb Q(\pi)_v:\mathbb Q_p]$ at $v\mid p$;
- $\tfrac12$ at a real place;
- $0$ at the other places.

If $e$ is its order, then $P_A=m_\pi^{\,e}$ and $2\dim A=e\,[\mathbb Q(\pi):\mathbb Q]$. An irreducible Weil polynomial with all invariants 0
is therefore exactly the characteristic polynomial of a simple variety. "Ordinary" means that half the roots are $p$-adic units; for a
factor of degree $2g$ this is the condition that the coefficient of $x^g$ is prime to $p$.

| factor | over | invariants, $e$ | slopes | isogeny factor | points |
|---|---|---|---|---|---|
| $x^2-x+2$ | $\mathbb F_2$ | $0,0$; 1 | $0,1$ | ordinary elliptic curve $E_2$ | 2 |
| $x^2+x+2$ | $\mathbb F_2$ | $0,0$; 1 | $0,1$ | ordinary elliptic curve $E_4$ (the curve $E$ of the earlier pages) | 4 |
| $x^4-x^2+4$ | $\mathbb F_2$ | $0,0$; 1 | $0,0,1,1$ | simple ordinary surface $S$, CM field $\mathbb Q(\sqrt{-3},\sqrt5)$ | 4 |
| $x^2+2$ | $\mathbb F_2$ | $0$; 1 | $\tfrac12,\tfrac12$ | supersingular elliptic curve $E_{ss}$, $\pi=\sqrt{-2}$ | 3 |
| $x^4+x^2+9$ | $\mathbb F_3$ | $0,0$; 1 | $0,0,1,1$ | simple ordinary surface $S'$, CM field $\mathbb Q(\sqrt{-7},\sqrt5)$ | 11 |
| $x^2+3$ | $\mathbb F_3$ | $0$; 1 | $\tfrac12,\tfrac12$ | supersingular elliptic curve $E'_{ss}$, $\pi=\sqrt{-3}$ | 4 |

The invariants, $e$ and the slopes were computed with PARI (*checked*, N5). The CM fields were read off from the discriminants 225 and 1225
of the quartic fields, which are Galois with group $V_4$. So, up to isogeny (*checked* with Honda–Tate as stated):

- $K_4$: $E_2\times E_4\times S$, ordinary, of dimension 4;
- Petersen: $S^3\times E_{ss}^4$, of dimension 10 and $p$-rank 6: neither ordinary nor almost ordinary;
- $K_5$: $S'^2\times E'_{ss}$, of dimension 5 and $p$-rank 4: almost ordinary.

**Weil restrictions (*proved here*, from the standard formula).** If $B$ is an abelian variety over $\mathbb F_{q^2}$ with Weil polynomial $Q$, then
$\mathrm{Res}_{\mathbb F_{q^2}/\mathbb F_q}B$ has Weil polynomial $Q(x^2)$. The reason is that Frobenius acts on the induced Tate module as
$\begin{pmatrix}0&\rho(F^2)\\1&0\end{pmatrix}$ (*standard*). A symmetric spectrum gives
$(x^2-\lambda x+q)(x^2+\lambda x+q)=(x^2+q)^2-\lambda^2x^2$, so $\det(x-M)=Q(x^2)$. The three cases (*checked*, N6):

- $K_4$: $Q=(y^2+3y+4)(y^2-y+4)$. So $K_4$ is $\mathrm{Res}(E_1\times E')$, where $E_1$ and $E'$ are elliptic curves over $\mathbb F_4$
  with 8 and 4 points. In particular $S\sim\mathrm{Res}_{\mathbb F_4/\mathbb F_2}E'$, and $E'$ is not isogenous to the base change of any curve
  over $\mathbb F_2$: those have traces $-4,-3,0$ over $\mathbb F_4$, and $E'$ has trace 1. Over $\mathbb F_4$ the fourfold becomes $E_1^2\times E'^2$,
  as `howe-positivity.md` §6 says.
- Petersen: $Q=(y+2)^4(y^2-y+4)^3$. Here $(y+2)^2$ is the supersingular curve over $\mathbb F_4$ with $\pi=-2$ ($e=2$), so Petersen is
  $\mathrm{Res}(E'^3\times E_{-2}^2)$.
- $K_5$: $Q=(y+3)(y^2+y+9)^2$ has odd degree, so it is not the Weil polynomial of anything. The single supersingular mode is "half" of
  $\mathrm{Res}\,E_{-3}$, whose Weil polynomial is $(x^2+3)^2$.

The obstruction is the parity of the multiplicity of $\lambda=0$, which is $n$ mod 2.

**Jacobians (*checked*, N7).** Every genus-2 curve over $\mathbb F_q$ has a model $y^2+h(x)y=f(x)$ with $\deg h\le3$ and $\deg f\le6$.

- Over $\mathbb F_2$ there are 768 smooth such models. 16 of them have Weil polynomial $x^4-x^2+4$, for example
  $C:\ y^2+(x^2+x)y=x^5+1$, whose point counts over $\mathbb F_{2^k}$, $k=1..4$, are $3,3,9,31$ by brute force. So **$S$ is a Jacobian**, and
  the same surface is a factor for Petersen.
- No smooth model has Weil polynomial $x^4+3x^2+4$, the product $E_2\times E_4$.
- Over $\mathbb F_3$, 24 of the 1296 models $y^2=f$ have Weil polynomial $x^4+x^2+9$. One is $y^2=2x^6+2x^5+x^3+x+1$, with counts $4,12,28$.

Whether the fourfold of $K_4$ itself (its isomorphism class, not its isogeny class) is a Jacobian or a Prym remains *open*. That is the
question of `howe-positivity.md` §8, and it is not addressed here.

## 3. The supersingular mode is the fixed point of the half turn

The vacuum has a closed form. Because $M+V=A_s\oplus A_s$ and $(M-V)^2=-(4q-A_s^2)\oplus(4q-A_s^2)$,

$$
J=(M-V)\,\bigl(D\oplus D\bigr),\qquad D=(4q-A_s^2)^{-1/2}.
$$

**It is unique when RH holds strictly (*proved here*).** Let $J$ commute with $S=M/\sqrt q$. Then its $+i$ eigenspace splits along the
eigenspaces $E_{e^{\pm i\theta}}$ of $S$. On $E_{e^{i\theta}}$ the Hermitian form $i\,\Omega(\bar v,v)$ is a positive multiple ($1/(\sqrt q\sin\theta)$) of the Weil form, so it is
definite. A positive Lagrangian must therefore be $\bigoplus_\theta E_{e^{i\theta}}$, with multiplicities allowed. *Checked* (N8): $J^2=-1$,
$JM=MJ$, $J$ is symplectic, $\Omega(x,Jx)>0$, and the closed form agrees with $U\,\mathrm{diag}(i\,\mathrm{sign\,Im}\,\mu)\,U^{-1}$. The frequencies
are $\theta/\pi=0.210,\ 0.5,\ 0.790$ for Petersen and $0.277,\ 0.5,\ 0.723$ for $K_5$.

**On $\ker(M^2+q)$ the vacuum is the step (*proved here*, *checked* N9).** There $V=-M$, so $M-V=2M$ and $D=(4q)^{-1/2}$, which give
$J=M/\sqrt q$. The normalised step squares to $-1$: it is a quarter turn, and it is its own vacuum. The Weil form on this block is
$\Omega(x,Mx)$, so its positivity is the positivity of the step itself.

**In the language of `locks.md` (*proved here*).** The half turn pairs $\lambda$ with $-\lambda$ through $\mu'_+=-\mu_-$. At $\lambda=0$ the mode is
its own partner: $\mu_+=-\mu_-$ is a lock of the mode with itself, of sign $-1$. `locks.md` §1 excludes this for ordinary modes, and here is
why. $\mu$ and $\bar\mu=-\mu$ generate the same ideal, so they have equal valuation $\tfrac12 v(q)$ at every prime above $p$. That is the
supersingular slope, and it means the rule $\Phi_\varepsilon=\{\mathrm{val}_p\varphi(F)>0\}$ selects neither embedding. PARI confirms that $p$ ramifies in
$\mathbb Q(\sqrt{-q})$ and that $\mathrm{val}(\mu)=\mathrm{val}(-\mu)=1=\tfrac12\mathrm{val}(q)$ (*checked*, N9). The quarter turn of `locks.md` §2, a relation
$\lambda^2+\lambda'^2=4q$ between two ordinary modes, is a different thing. For $\lambda=0$ it would pair the mode with $\lambda'=\pm2\sqrt q$, whose
Frobenius eigenvalue is the real Weil number $\pm\sqrt q$: the one case Centeleghe–Stix exclude (§4). *Proved here*; a remark only.

## 4. Where the lattice comes from: the category, not a lift

**Deligne (*standard, from memory*; "Variétés abéliennes ordinaires sur un corps fini", 1969).** Ordinary abelian varieties over
$\mathbb F_q$ are equivalent to Deligne modules $(T,F)$, with $T=H_1$ of the Serre–Tate canonical lift. Petersen and $K_5$ are not ordinary.

**Centeleghe–Stix (*standard, from memory*; "Categories of abelian varieties over finite fields I: Abelian varieties over
$\mathbb F_p$", Algebra & Number Theory, 2015).** Over a prime field, the category of abelian varieties whose Frobenius has no eigenvalue
$\pm\sqrt p$ is equivalent to the category of pairs $(T,F)$, where:

- $T$ is a free $\mathbb Z$-module of finite rank;
- $F$ is an endomorphism that is semisimple over $\mathbb Q$, with all eigenvalues $p$-Weil numbers and none of them real;
- there exists $V$ with $FV=VF=p$, so that $T$ is a $\mathbb Z[F,V]/(FV-p)$-module.

The functor is built from homomorphisms into a fixed pro-system of abelian varieties. I do not trust my memory of its variance, or of its
precise form. It needs no lift. As far as I recall, ordinariness and squarefreeness are not assumed.

**The hypotheses hold (*checked*, N4).** For Petersen ($p=2$), $K_5$ ($p=3$) and $K_4$ ($p=2$):

- $q$ is prime;
- $\gcd(\det(x-M),x^2-q)=1$;
- $MV=VM=q$ with $V$ integral;
- $M$ is semisimple, with all roots non-real (§1).

Granting the theorem as recalled, $(\mathbb Z^{20},M_s)$ for Petersen **is** an abelian variety over $\mathbb F_2$, determined up to isomorphism
(not only isogeny), of dimension 10, isogenous to $S^3\times E_{ss}^4$, and not ordinary. Likewise $(\mathbb Z^{10},M_s)$ for $K_5$ is a fivefold
over $\mathbb F_3$. In both cases the lattice on the arithmetic side is supplied by the category, not by a lift. For $K_4$, Deligne and
Centeleghe–Stix both apply. I do not know whether the two lattices agree (they could differ by a duality).

**"No lift" should read "no canonical lift" (*standard, from memory*).** By the Deuring lifting lemma (Deuring 1941; Lang, *Elliptic Functions*,
ch. 13), a supersingular elliptic curve lifts to characteristic 0 together with any one endomorphism, Frobenius included. The lift is a
CM curve over a ramified extension of $W(\mathbb F_p)$, and there are two Galois-conjugate choices. More generally, every abelian variety over a
finite field becomes isogenous, possibly after extending the field, to one that has a CM lift; when neither the isogeny nor the extension is
needed is the subject of Chai–Conrad–Oort, *Complex Multiplication and Lifting Problems* (2014). The ordinary case is special because the lift is
**canonical**: it is unique over $W(k)$, all endomorphisms lift, and so the lattice is $H_1$ of it.

**$K_5$ over a non-prime field: not needed.** $K_5$ is almost ordinary. From memory, Oswal–Shankar ("Almost ordinary abelian varieties over
finite fields", J. LMS 2020) give a Deligne-type description of almost ordinary varieties, and Bergström–Karemaker–Marseglia ("Polarizations
of abelian varieties over finite fields via canonical liftings", IMRN 2023) treat their polarisations. I do not recall their exact hypotheses:
which $q$, whether $p=2,3$ are allowed, whether the Weil polynomial must be squarefree. $K_5$'s is not squarefree. Since $q=3$ is prime,
Centeleghe–Stix suffice here.

## 5. The variety is glued, not a product

Put $L_{ss}=L\cap\ker(M^2+q)$ and $L_{ord}=L\cap\ker h_{ord}(M)$. *Checked* (N11):

| example | $[L:L_{ss}\oplus L_{ord}]$ | $\det\Omega\vert_{L_{ss}}$ | $\det\Omega\vert_{L_{ord}}$ |
|---|---|---|---|
| Petersen | $5^6$ | $5^6$ | $5^6$ |
| $K_5$ | $5^2$ | $5^2$ | $5^2$ |

So the Centeleghe–Stix variety is not the product of its supersingular and ordinary parts. It is isogenous to that product by an isogeny of
degree $5^6$, respectively $5^2$, prime to $p$; the gluing sits at the resultant of $x$ and $x^2-5$. In GKP terms, the qunaught $L$ is
a glued code: the two blocks alone are codes of dimensions $125$ and $5$ for $\Omega$. *Checked*; the isogeny reading is *sketched* and
assumes the functor is exact on such inclusions.

$(L_{ord},M)$ is itself a Deligne module (*checked*, N11). Its characteristic polynomials are $(x^4-x^2+4)^3$ and $(x^4+x^2+9)^2$, with middle
coefficients $-25$ and $19$, both prime to $p$. **So the ordinary part has a canonical lift, and the supersingular part does not.**

## 6. The sign check: vacuum against arithmetic

**The vacuum.** $\Omega(x,Jx)>0$ for all $x\ne0$, for Petersen and for $K_5$ (*checked*, N8). This holds by construction once RH holds.

**The ordinary block (*sketched*, from Howe as cited in `howe-positivity.md`).** Both quartics have roots $\pm\mu,\pm\bar\mu$. At each of the two
primes above $p$, the set of non-units is closed under $\mu\to-\mu$ (*checked*, N10). By the proposition of `howe-positivity.md` §3, neither
$\Omega$ nor $-\Omega$ is a polarisation of the Deligne module $L_{ord}$, for any $\varepsilon$.

A polarisation of the whole variety pulls back to one on the ordinary part. Hence $\Omega$ is not a polarisation of the Centeleghe–Stix
variety either. This is *sketched*: it uses the pullback of an ample class under a finite map, plus the variance caveat of §4. The
arithmetic complex structure on the ordinary block is $J$ with the orientation reversed on $E(\sqrt5)$ or on $E(-\sqrt5)$, as for $K_4$.

**The supersingular block.** The $p$-adic rule selects no CM type there (§3). For a single supersingular elliptic factor, exactly one of
$\pm\Omega$ is a polarisation: every alternating form on $\mathbb Z^2$ is compatible with $F$, and the commutant $\mathbb Z[F]$ has only positive
determinants $a^2+pb^2$, so no automorphism reverses $\Omega$. This is *proved here* for rank 2. Which sign it is depends on how the category
identifies $T$, and I know no Howe-type criterion that reads it off from $(T,F,\omega)$ alone. **So in the non-ordinary case there is no arithmetic
$J$ on the supersingular block to compare the vacuum with.** Only the archimedean place (the vacuum) chooses there. *Negative finding / open.*

**Twisted forms.** The candidates are $\Omega_C(x,y)=\Omega(x,(C\oplus C)y)$ with $C$ integral, symmetric and commuting with $A_s$. They are a subfamily of the compatible forms. The Rosati-fixed commutant of $M$, which gives all the compatible forms $\Omega(x,Py)$, has rank 34
for Petersen and 9 for $K_5$, against 22 and 7 for this subfamily; for $K_4$ both have rank 4 (*checked*, N12). Such a form is positive for the vacuum iff $C>0$. It can be a polarisation only if
$C$ is definite of opposite signs on $E(\sqrt5)$ and $E(-\sqrt5)$: that is the necessary condition from the ordinary block.

- **Inside $\mathbb Q[A_s]$: impossible (*proved here*, *checked* N12).** The order $R=\mathbb Q[A_s]\cap M_n(\mathbb Z)$ is $\mathbb Z[A_s]$ for Petersen and
  $\mathbb Z[A_s]+\mathbb Z\tfrac{A_s+A_s^2}2$ for $K_5$. In both, $p(\sqrt5)\equiv p(0)\pmod{\sqrt5}$. A unit has $p(0)=\pm1$ and
  $N=p(\sqrt5)p(-\sqrt5)=\pm1$ with $N\equiv p(0)^2=1\pmod 5$, so $N\ne-1$. Hence no unit of $R$ changes sign between $\pm\sqrt5$. This is
  the difference from $K_4$, where the unit $P$ of `howe-positivity.md` §4 exists.
- **$K_5$, outside $\mathbb Q[A_s]$: exists (*checked*, N12).** The matrix
  $C=\begin{pmatrix}2&-2&3&1&-5\\-2&1&-3&-1&4\\3&-3&-3&0&2\\1&-1&0&0&-1\\-5&4&2&-1&-1\end{pmatrix}$ has $\det C=-1$, is positive definite on
  $E(\sqrt5)$ and negative definite on $E(-\sqrt5)$. So $\Omega_C$ is unimodular and compatible, and it is not positive for the vacuum. It
  satisfies the necessary condition; whether it is a principal polarisation also depends on the supersingular block, so that is *open*.
- **Petersen: none found in the subfamily (*negative finding*, a search and not a proof; the 12 further dimensions were not searched).** A sparse search on an LLL basis of the rank-22 symmetric
  commutant produced 1634 unimodular $C$. They realise 14 of the 16 sign patterns on $(E(\sqrt5),E(-\sqrt5))$. The two missing ones are
  exactly the totally sign-changing patterns. A plausible reason is the odd multiplicity 3, compared with 2 for $K_5$, together with the gluing
  at 5. This is *heuristic*.

## 7. What supplies the lattice when there is no lift

1. *Standard.* In the ordinary case ($K_4$, and the ordinary part $L_{ord}$ of Petersen and $K_5$), the lattice with its step is $H_1$ of the
   canonical lift (Deligne), and the step is the lift of Frobenius.
2. *Checked / standard, from memory.* In the non-ordinary examples over $\mathbb F_p$ the integral lattice and the integral step of norm $q$ are
   still supplied by the graph. On the arithmetic side the Centeleghe–Stix category supplies the same pair as an abelian variety over
   $\mathbb F_p$. Its supersingular part has no canonical lift, only non-canonical CM lifts over ramified bases.
3. *Checked.* The invariant vacuum exists in all three examples because RH holds (the Weil form is positive definite), and it is unique.
4. *Proved here.* On the supersingular block the vacuum is the normalised step itself ($J=M/\sqrt q$, a quarter turn). So there the
   positivity is the positivity of $\Omega(x,Mx)$, a statement about the step alone.
5. *Negative finding.* The arithmetic does not choose a complex structure on the supersingular block, because $\mu$ and $-\mu$ have the same
   $p$-adic valuation. So in the non-ordinary case only the archimedean side (the vacuum) supplies $J$ there.
6. *Sketched.* The positivity that the arithmetic does supply, a polarisation, is not $\Omega$ on the ordinary part. It may exist as a
   twisted form ($K_5$: a unimodular candidate exists; Petersen: none found in the subfamily searched).
7. *Heuristic.* For $\zeta$ nothing supplies the first two ingredients. There is no finite-rank $\mathbb Z$-lattice with an integral step whose
   eigenvalues are the zeros; the adelic code's lattice $\mathbb Q^2$ is rigid and divisible (`adelic-gkp.md` G3); and the analogue of
   Frobenius is a flow, not an integral map of norm $q$. The vacuum is exactly RH.
8. *Heuristic.* What the non-ordinary case teaches for $\zeta$ is that a canonical lift is not what supplies the lattice. A category of
   linear-algebra data (Centeleghe–Stix) does, and it needs integrality and $FV=p$, not a characteristic-zero model.

| example | integral lattice | integral step of norm $q$ | invariant vacuum | arithmetic $J$ |
|---|---|---|---|---|
| $K_4$, one negative edge ($\mathbb F_2$) | graph; $H_1$ of the canonical lift | graph; lifted Frobenius | yes (RH), unique | exists (Deligne/Howe), differs from the vacuum by signs |
| Petersen, dodecahedral ($\mathbb F_2$) | graph; Centeleghe–Stix category | graph; Frobenius | yes (RH), unique; $=M/\sqrt2$ on the ss block | ordinary block: differs by signs; ss block: none selected |
| $K_5$, pentagon ($\mathbb F_3$) | graph; Centeleghe–Stix category | graph; Frobenius | yes (RH), unique; $=M/\sqrt3$ on the ss block | as for Petersen |
| $\zeta$ | none known (G3: $\mathbb Q^2$ only) | none (a flow) | open (= RH) | none |

## 8. Status and checks

| statement | status |
|---|---|
| $K_5$ has $q=3$ (the brief said 4) | checked (N1) |
| factorisations, RH, semisimplicity, point counts | checked exactly (N1–N3, N5) |
| Honda–Tate statement; isogeny factors and their types | statement standard, from memory; invariants, slopes and $e$ computed with PARI (N5) |
| Weil restriction formula; $\det(x-M)=Q(x^2)$; Petersen and $K_4$ are Weil restrictions, $K_5$ is not | formula standard; rest proved here, checked (N6) |
| $S$ is the Jacobian of $y^2+(x^2+x)y=x^5+1$; $E_2\times E_4$ is not a Jacobian; $S'$ is a Jacobian | checked by exhaustive search and brute-force counts (N7) |
| closed form and uniqueness of the vacuum | proved here; checked numerically (N8) |
| vacuum $=M/\sqrt q$ on the supersingular block; self-lock and equal valuations | proved here; checked (N9) |
| Centeleghe–Stix hypotheses hold; the variety is a Centeleghe–Stix object | hypotheses checked (N4); theorem standard, from memory, variance not recalled |
| Deuring lifting; CM lifting up to isogeny | standard, from memory |
| Oswal–Shankar, Bergström–Karemaker–Marseglia hypotheses | not known to me |
| gluing index $5^6$, $5^2$; $L_{ord}$ a Deligne module | checked (N11); isogeny reading sketched |
| $\Omega$ not a polarisation (ordinary block) | sketched from Howe via `howe-positivity.md`; valuations checked (N10) |
| no arithmetic $J$ on the supersingular block | negative finding; rank-2 sign uniqueness proved here |
| no sign-changing unit in $R$; a unimodular sign-changing $C$ for $K_5$ | proved here; checked (N12) |
| none for Petersen in the subfamily $C\oplus C$; ranks of the full commutant | negative finding by search, not a proof; ranks checked (N12) |
| §7, items 7–8 | heuristic |

Checks: `checks/check_no_lift.py` (PARI/GP by subprocess, sympy, numpy, python-flint), output `checks/output_no_lift.txt`, **50 of 50 pass**. Runtime is about
10 s. Nothing is registered and no REFUTE review has run.

## 9. Next

- **A Howe-type criterion for Centeleghe–Stix objects.** Find the condition on $(T,F,\omega)$ that decides whether $\omega$ is a polarisation when
  there are supersingular factors, presumably in the literature that builds on Centeleghe–Stix. Then decide whether the $K_5$ form $\Omega_C$
  is a principal polarisation.
- **Petersen.** Search the full Rosati-fixed commutant (rank 34), and prove or refute the absence of a unimodular sign-changing form, for example by a local (5-adic) obstruction for odd
  multiplicity, using the gluing of §5.
- **Read the cited papers.** Byte-cite Centeleghe–Stix, Oswal–Shankar and Bergström–Karemaker–Marseglia when `refs/src/` is available, and fix
  the variance of the Centeleghe–Stix functor.
