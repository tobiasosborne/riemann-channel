# Which overlaps of the code determine the lattice?

Author: `claude:opus-5.5`, 2026-10-06, lane F of an orchestrated session.

Status: **a record, not a round; nothing registered in db/claims.tsv; no REFUTE review; no shard.** Each statement is labelled *standard*,
*proved here*, *checked*, *sketched*, *heuristic*, *open* or *negative finding*. Theorems quoted without a line reference are from memory;
`refs/src/` was not on disk in this session. Checks: `checks/check_overlap_data.py`, output `checks/output_overlap_data.txt` (40 of 40 pass;
PARI/GP 2.15.4 through the `gp` binary, sympy; about 40 s).

The question comes from `curve-bridge.md` §6, step 3. There, for an ordinary elliptic curve $E/\mathbb F_q$, the counts fix the Frobenius polynomial but not
the lattice $L=H_1$ of the canonical lift. At $q=7$, $a=2$ the curves $j=4$ and $j=5$ have the same counts and the same groups $E(\mathbb F_{7^k})$, yet their
Deligne modules are not isomorphic. That page left open whether the divisor-resolved overlaps $\langle\Theta_K,1_D\rangle=q^{h^0(D)}$ determine $L$.

**Findings.**

- **The product-stabiliser overlaps of the code determine exactly the order $\mathrm{End}(E)$, and not the ideal class of $L$** (proved here, from standard
  inputs; checked). The overlap function on divisors at all levels $\mathbb F_{q^k}$, up to one relabelling compatible with Frobenius, is the same datum as
  the $\mathbb Z[\pi]$-module $E(\overline{\mathbb F}_q)=\bigoplus_\ell E[\ell^\infty]$. Each summand depends only on the completion $\mathrm{End}(E)\otimes\mathbb Z_\ell$, and an ideal class is
  trivial at every completion. For $j=4,5$ over $\mathbb F_7$ an explicit Frobenius-equivariant isomorphism $E_4(\overline{\mathbb F}_7)\to E_5(\overline{\mathbb F}_7)$ is glued from the
  2-isogeny on the odd part and the 3-isogeny on the 2-part. It was checked over $\mathbb F_{7^m}$ for $m=1..12$ and $m=18$.
- **"Code data see the order, not the class" holds on both pairs** (checked). For the Pauli-six pair over $\mathbb F_5$ the orders differ ($\mathbb Z[i]$ against
  $\mathbb Z[2i]$). The degree-0 overlaps at level $\mathbb F_5$ already separate them.
- **"The lattice class is invisible to all local data" is false as stated** (negative finding; proved here for this pair, checked). It holds for
  *unpolarised* local data, and those are what the overlaps are. Add the Weil pairing and it fails. No Frobenius-equivariant isomorphism
  $E_4[8]\to E_5[8]$ respects $e_8$, even up to inversion. Every equivariant isomorphism $E_4[3]\to E_5[3]$ inverts $e_3$. The polarised local data see the
  *genus* of the form. For discriminant $-24$ each genus holds one class, so here they see the class.
- **Which curve has the principal lattice depends on Deligne's embedding $\varepsilon$** (proved here, from standard inputs; checked). Only the difference
  is intrinsic: the two classes differ by $[\mathfrak p_2]$. With $\varepsilon(\sqrt2)=+\sqrt2$ for the 7-adic $\sqrt2\equiv3\bmod7$, the principal curve is $j=5$. With the other choice it
  is $j=4$.

---------------------------------------------------------------------------------------------------------------------

## 1. The two curves and their lattices (task item 1)

$q=7$, $a=2$, $\pi^2-2\pi+7=0$, $\pi=1+\sqrt{-6}$. $\mathbb Z[\pi]=\mathbb Z[\sqrt{-6}]=\mathcal O_K$ is maximal (disc $-24$ is fundamental), and $h=2$ (C2). The curves with
trace 2 over $\mathbb F_7$ have $j\in\{4,5\}$, three models each, all with $E(\mathbb F_7)\cong\mathbb Z_6$ (C1). We fix
$$E_4:\ y^2=x^3+3x+3,\qquad E_5:\ y^2=x^3+x+3 .$$
Since $\mathbb Z[\pi]$ is maximal, $\mathrm{End}(E_4)=\mathrm{End}(E_5)=\mathcal O_K$. The curves over $\overline{\mathbb F}_7$ with this endomorphism ring form a torsor under $\mathrm{Cl}(\mathcal O_K)\cong\mathbb Z_2$
(*standard*: Deuring; Waterhouse, *Abelian varieties over finite fields*, 1969; from memory). The lattice classes are $(1,0,6)$ for $\mathcal O_K$ and
$(2,0,3)$ for $\mathfrak p_2=(2,\sqrt{-6})$, with $[\mathfrak p_2]=[\mathfrak p_3]$ the non-trivial class.

**Criterion 1: the isogenies of degree 2 and 3** (proved here, from standard inputs; checked C3–C5, C9). $\mathfrak p_2=(2,\pi-1)$, so
$E[\mathfrak p_2]=E[2]\cap\ker(\pi-1)=E(\mathbb F_7)[2]$. Similarly $E[\mathfrak p_3]=E(\mathbb F_7)[3]$. Each curve has exactly one $\mathbb F_7$-rational subgroup of order 2 and one of order 3
(C3), because $2$ and $3$ ramify and $\mathcal O_K/2$, $\mathcal O_K/3$ have exactly one ideal of index 2, resp. 3. The quotient $E\to E/E[\mathfrak p]$ moves the class of the
Deligne module by $[\mathfrak p]^{\pm1}$ (*standard*, kernel ideals, Waterhouse 1969, from memory). PARI's Vélu isogenies send $E_4$ to $j=5$ and $E_5$ to $j=4$, in both
degrees (C4, C5). On the lattice side, the $(1,0,6)$ lattice has exactly one $M$-stable sublattice of index 2 and one of index 3, and both are of class
$(2,0,3)$; the converse also holds (C9). So **the two curves carry different classes, and this is intrinsic.**

**Criterion 2: which one is principal** (proved here, from standard inputs; checked C6–C8). The inputs, all *standard* and from memory, are these.
Deligne's module is $T_\varepsilon(E)=H_1(E^{\rm can}\otimes_\varepsilon\mathbb C,\mathbb Z)$ (Deligne, *Variétés abéliennes ordinaires sur un corps fini*, 1969). The canonical lift has
$\mathrm{End}(E^{\rm can})=\mathrm{End}(E)$ (Serre–Tate; Deuring lifting). A complex curve with CM by $\mathcal O_K$ is $\mathbb C/\Lambda$ with $\Lambda$ an $\mathcal O_K$-ideal, and $j(\mathbb C/\Lambda)$ depends only on
the class of $\Lambda$. The two class invariants are
$$j(\mathcal O_K)=j(\sqrt{-6})=2417472+1707264\sqrt2\approx4831908,\qquad j(\mathfrak p_2)=j(\sqrt{-6}/2)=2417472-1707264\sqrt2\approx3036 ,$$
the roots of $H_{-24}=x^2-4834944x+14670139392$ (C6, C7). Mod 7 the roots are 4 and 5, both simple. So $j(E^{\rm can})\in\mathbb Z_7$ is the Hensel lift, equal to
$2417472+1707264\,s$ for a 7-adic $s$ with $s^2=2$. Since $j(\mathcal O_K)\equiv1-\sqrt2$, the curve $E_5$ needs $s\equiv3$ and $E_4$ needs $s\equiv4\pmod 7$ (C8).
$T_\varepsilon(E)\cong\mathcal O_K$ iff $\varepsilon(j(E^{\rm can}))=j(\mathcal O_K)$, that is, iff $\varepsilon(s)=+\sqrt2$. The two embeddings that differ on $\sqrt2$ swap the answer. (Complex conjugation
does not matter here, because the non-trivial class is its own inverse.) **"Which curve is principal" is a property of the pair $(E,\varepsilon)$, not of $E$.**
This settles the item that `curve-bridge.md` §2 left *open*: the assignment is $\varepsilon$-dependent, and only the torsor structure is canonical.

## 2. The overlap data are the Frobenius module of points (task item 2)

**Lemma 1 (proved here; the first two inputs are standard).** Let $E/\mathbb F_q$ be an elliptic curve, and let $D$ be a divisor on $E_{\mathbb F_{q^k}}$.

- $\langle\Theta_{K_k},1_D\rangle=q^{k\,h^0(D)}$, with $h^0(D)=\deg D$ for $\deg D\ge1$, $h^0(D)=0$ for $\deg D<0$, and, for $\deg D=0$, $h^0(D)=1$ iff the geometric points of $D$ sum to $O$
  (Riemann–Roch and Abel–Jacobi, *standard*).
- The places of $E_{\mathbb F_{q^k}}$ are the $\pi^k$-orbits on $E(\overline{\mathbb F}_q)$. A relabelling of places that is compatible with base change is a $\pi$-equivariant
  bijection $\psi$ of $E(\overline{\mathbb F}_q)$.
- $\psi$ preserves $h^0$ at every level iff $\psi=\tau\circ\Psi$, where $\Psi$ is a $\pi$-equivariant group isomorphism and $\tau$ is translation by a rational point. *Proof.*
  Preserving principality of all $P+Q-R-S$ makes $\psi-\psi(O)$ additive. $\psi(O)$ is $\pi$-fixed because $\psi$ commutes with $\pi$. ∎

So **the full overlap function of the code with product stabiliser states, at all levels, is equivalent to the $\mathbb Z[\pi]$-module $E(\overline{\mathbb F}_q)$.** Brute force
confirms the first bullet on both curves. $h^0(nO-E)$, computed by linear algebra on $L(nO)$, agrees with Riemann–Roch plus Abel–Jacobi on 3816
divisors each, of which 1272 have degree 0 and 210 are principal (R1, R2; places of degree $\le3$, the same method as `curve-bridge.md` §3).

**Theorem 2 (proved here, from standard inputs).** Let $E,E'$ be ordinary and isogenous over $\mathbb F_q$. Then $E(\overline{\mathbb F}_q)\cong E'(\overline{\mathbb F}_q)$ as $\mathbb Z[\pi]$-modules iff
$\mathrm{End}(E)=\mathrm{End}(E')$ inside $K=\mathbb Q(\pi)$.

*Proof.* Write $E(\overline{\mathbb F}_q)=\bigoplus_{\ell\ne p}E[\ell^\infty]\oplus E[p^\infty](\overline{\mathbb F}_q)$.

- ($\Leftarrow$) Put $\mathcal O=\mathrm{End}(E)$. For $\ell\ne p$, $T_\ell E$ is a proper, hence invertible, $\mathcal O_\ell$-lattice (Tate's theorem; quadratic orders are
  Gorenstein; *standard*, from memory). $\mathcal O_\ell$ is semilocal, so $T_\ell E\cong\mathcal O_\ell$, and $E[\ell^\infty]\cong K_\ell/\mathcal O_\ell$ with $\pi$ acting by multiplication. The same holds for
  $E'$. At $p$, $E[p^\infty](\overline{\mathbb F}_q)\cong\mathbb Q_p/\mathbb Z_p$ with $\pi$ acting by the unit root of $x^2-ax+q$ in $\mathbb Z_p$. This depends only on $(a,q)$. Glue over $\ell$.
- ($\Rightarrow$) $T_\ell E=\mathrm{Hom}(\mathbb Q_\ell/\mathbb Z_\ell,E[\ell^\infty])$ is recovered from the module, and $\mathcal O\otimes\mathbb Z_\ell=\mathrm{End}_{\mathbb Z_\ell[\pi]}(T_\ell E)$ by Tate's theorem. At $p$ every order
  containing $\mathbb Z[\pi]$ is maximal, since $p\nmid a^2-4q$. An order is the intersection of its completions. ∎

*The key sentence, in the precise form it survives* (proved here). **The overlaps of $\Theta_K$ with product stabiliser states are local data, one $\ell$ at a
time. Through Theorem 2 they determine the order $\mathrm{End}(E)$, which is the multiplier ring of $L$. The class of $L$ among invertible ideals of that order is a
global invariant, trivial at every completion, and these data do not see it.** Within an ordinary isogeny class the overlaps determine $L$ exactly
when $h(\mathrm{End}\,E)=1$.

**The class-number-two pair, explicitly** (checked).

- *Gluing map* (O2, O3). The rational 2-isogeny $\varphi_2$ is an isomorphism on $E[\ell^\infty]$ for $\ell\ne2$, and the rational 3-isogeny $\varphi_3$ is one for
  $\ell\ne3$. So $\Phi=\varphi_2\circ e_{\rm odd}+u\circ\varphi_3\circ e_2$ is a $\pi$-equivariant isomorphism $E_4(\overline{\mathbb F}_7)\to E_5(\overline{\mathbb F}_7)$. Here $e_{\rm odd},e_2$ are the primary
  idempotents and $u:(x,y)\mapsto(4x,y)$. The check is pointwise on all 2400 points over $\mathbb F_{7^4}$ (O2). Over $\mathbb F_{7^m}$, $m=1..12,18$, it checks injectivity
  on every line of every $E_4(\mathbb F_{7^m})[\ell]$, and additivity and Frobenius-equivariance on random points (O3).
- *Overlap statistics without $\Phi$* (O1). Over $\mathbb F_7,\mathbb F_{49},\mathbb F_{343}$ and for places of degree $\le3$ (all pairs except (3,3)), the two curves have the same number
  of places. They also have the same multiset of fibre sizes of the class map onto $\mathrm{Pic}^d$, and hence the same number of pairs with $h^0(P-Q)=1$; for
  example 22860 ordered pairs of degree-2 places over $\mathbb F_{49}$.
- *Lattice side* (T1). $\mathbb Z^2/N$ for $(1,0,6)$ and for $(2,0,3)$ are isomorphic $\mathbb Z[M]$-modules for every $N$ tested, 12 values up to 27.

## 3. What does distinguish them (task item 3)

1. *Standard.* The period lattice of the canonical lift is the class itself: $\varepsilon(j(E^{\rm can}))$ is $j(\mathcal O_K)$ or $j(\mathfrak p_2)$ (§1), a characteristic-0, global datum.
2. *Standard, from memory (Katz, "Serre–Tate local moduli", 1981).* Serre–Tate coordinates do not separate the curves, since both canonical lifts sit at
   the origin of isomorphic deformation spaces; what differs is the global number $j(E^{\rm can})\in\mathbb Z_7\cap\overline{\mathbb Q}$.
3. *Proved here, checked (§4).* Adding the Weil pairing to the local data separates them already at $\ell=2$ (on $E[8]$), and at $\ell=3$ up to the sign of $e_3$.
4. *Sketched (Gauss genus theory, from memory).* In general polarised local data see only the genus of the Latimer–MacDuffee form, i.e. the class
   modulo $\mathrm{Cl}^2$; here $(1,0,6)$ and $(2,0,3)$ lie in different genera (T4) because $\mathrm{Cl}=\mathbb Z_2$ has $\mathrm{Cl}^2=1$, while for $D=-23$ ($\mathrm{Cl}=\mathbb Z_3$, one genus) they would see nothing.
5. *Proved here.* Twisting the product states by characters of $\mathrm{Pic}^0$ adds nothing, because those overlaps are Fourier transforms of the
   divisor-resolved data of §2.
6. *Standard, from memory (Mumford, "On the equations defining abelian varieties I", 1966).* $e_n$ is the commutator form of the theta group of
   $\mathcal O(nO)$ acting on $L(nO)$, the space whose size is the overlap $\langle\Theta_K,1_{nO}\rangle$.
7. *Heuristic.* The first candidate datum beyond the order is therefore operator-valued (the projective action of translations on the overlap space;
   its lattice-side analogue is $\Omega\bmod N$ on $L/NL$ with $M$ acting, tested in T2), not a number $\langle\Theta_K,\cdot\rangle$.
8. *Open.* Whether any overlap of $\Theta_K$ with a non-stabiliser state sees the ideal class beyond its genus.

## 4. The polarised refinement (proved here for the E3 pair; checked)

**Proposition 3.** No $\pi$-equivariant isomorphism $E_4[8]\to E_5[8]$ satisfies $e_8(\Phi x,\Phi y)=e_8(x,y)^{\pm1}$. Every $\pi$-equivariant isomorphism $E_4[3]\to E_5[3]$
satisfies $e_3(\Phi x,\Phi y)=e_3(x,y)^{-1}$. For $\ell\nmid 6p$, Weil-pairing-preserving equivariant isomorphisms $E_4[\ell^\infty]\to E_5[\ell^\infty]$ exist.

*Proof.*

- *At 2.* $\pi$ acts on $E[8]\cong\mathcal O_K/8$ as a regular element, so its commutant in $\mathrm{End}(E[8])$ is $\mathcal O_K/8$. Hence every equivariant isomorphism is
  $\varphi_3\circ u$ with $u\in(\mathcal O_K/8)^\times$.
- *The scale.* $e(\varphi x,\varphi y)=e(x,y)^{\deg\varphi}$ (*standard*), and $u$ scales $e$ by $N(u)$. With $u=x+y\sqrt{-6}$, $x$ odd, we get $N(u)=x^2+6y^2\equiv1$ or $7\pmod8$. So the scale is
  $3N(u)\equiv3,5\pmod 8$, never $\pm1$.
- *At 3.* The same argument with $\varphi_2$ gives the scale $2N(u)$, where $N(u)\equiv x^2\equiv1\pmod3$. So the scale is $\equiv2\equiv-1$.
- *At $\ell\nmid6p$.* $\ell$ is unramified in $K$, so $N(\mathcal O_{K,\ell}^\times)=\mathbb Z_\ell^\times$, and $\varphi_2\circ u$ can be made to have scale 1. ∎

*Checks.* PARI finds the Frobenius matrices and Weil pairings on $E[n]$ for $n=2,3,4,5,8,9,16$ (W1). The scale sets are $\{2\}$ for $n=3$, $\{3,5\}$ for $n=8$,
$\{2,5,8\}$ for $n=9$, $\{3,5,11,13\}$ for $n=16$, and all units for $n=2,4,5$. They are computed from all 6, 32, 54 and 128 equivariant isomorphisms respectively. Each scale set
equals the set of $\det g$ over lattice-side intertwiners $gM_{(1,0,6)}=M_{(2,0,3)}g$ mod $n$ (T2, T3). This also checks, in this instance, the dictionary between the
Weil pairing and $\Omega$. Finally $e(\varphi x,\varphi y)=e(x,y)^{\deg\varphi}$ holds for the explicit $\varphi_2,\varphi_3$ (W3).

So the sentence "the lattice class is invisible to all local data" needs the word *unpolarised*. The overlaps of §2 are unpolarised; the Weil pairing is
not among them (§3, items 6–7).

## 5. The Pauli-six pair: different orders (task item 4)

$q=5$, $a=-2$, $\mathbb Z[\pi]=\mathbb Z[2i]$ (conductor 2). $y^2=x^3+4x$ has $j=1728\equiv3$, $\mathrm{End}=\mathbb Z[i]$ and $E(\mathbb F_5)=\mathbb Z_2\times\mathbb Z_4$. $y^2=x^3+4x+1$ has $j\equiv1$, $\mathrm{End}=\mathbb Z[2i]$ and $E(\mathbb F_5)=\mathbb Z_8$ (P1).
Both orders have class number 1, so each curve is alone with its order. Theorem 2 predicts that the overlaps separate them, through the order. They do.

- *Checked (P2).* $E[2]\subset E(\mathbb F_5)$ only for $b=0$, i.e. $(\pi-1)/2\in\mathrm{End}$ only for $\mathrm{End}=\mathbb Z[i]$.
- *Checked (P3; brute-force $L(D)$ over $\mathbb F_5$).* Count the pairs $\{P,Q\}$ of distinct affine rational points with $\langle\Theta_K,1_{2O-P-Q}\rangle=5$. There are 2 for $b=0$
  and 3 for $b=1$, so the degree-0 overlaps at level 1 separate the pair.
- *Checked (P4, P5).* On the lattice side $(M-1)/2$ is integral on $(2,0,2)$ and not on $(1,0,4)$. The $\mathbb Z[M]$-modules differ mod 2 and mod 4 and agree mod
  3, 5, 7, 9. The difference is local and sits at the conductor.

**Principle** (proved here, Theorem 2; checked on both pairs). *Code data see the order, not the class.* In E2 the two lattices have different multiplier
rings, and that is a local invariant at $\ell=2$. In E3 they have the same multiplier ring and differ by an ideal class, which no unpolarised completion
sees.

## 6. Remarks on the existing pages

- `curve-bridge.md` §6, step 3 ("whether [the $D$-resolved overlaps] determine $L$ in general: *open*") is answered: no. They determine $\mathrm{End}(E)$ and
  nothing more about $L$ (Theorem 2). Its §2 *open* item (which E3 curve has which class) is answered in §1: it depends on $\varepsilon$.
- No error was found in `curve-bridge.md`. Its E3 statements (identical groups to $k=24$ on the lattice side, the reason $\mathfrak a/x\mathfrak a\cong\mathcal O/x\mathcal O$) agree with T1 and O3.
- The lane brief's sentence "the lattice class is invisible to all local data" needs the word *unpolarised*. With the Weil pairing, $\ell=2$ alone separates the
  E3 pair (§4).

## 7. Status and checks

*Review corrections 2026-10-06 (`notes/reviews/adelic-gkp-lattice-2026-10-06.md`):* Lemma 1, bullet 2: base-change compatibility alone does not make a relabelling $\pi$-equivariant (it allows permutations inside a Frobenius orbit); the hypothesis is Frobenius compatibility. At $n=4$ the Weil pairing does not separate the two $q=7$ curves; the detecting level is 8.


| statement | status | checks |
|---|---|---|
| E3: trace-2 curves are $j=4,5$; $\mathbb Z[\pi]=\mathcal O_K$, $h=2$, forms $(1,0,6),(2,0,3)$ | checked | C1, C2 |
| the rational 2- and 3-isogenies swap $j=4,5$; lattice side: unique stable index-2/3 sublattice, of the other class | proved here (kernel ideals standard); checked | C3–C5, C9 |
| which curve is principal depends on $\varepsilon(\sqrt2)$; $\varepsilon(s)=+\sqrt2$ with $s\equiv3$ makes $j=5$ principal | proved here from standard inputs; checked | C6–C8 |
| overlaps $=q^{h^0(D)}$ equal Riemann–Roch + Abel–Jacobi (3816 divisors per curve) | checked (brute force) | R1, R2 |
| Lemma 1: overlap function at all levels $\equiv$ the $\mathbb Z[\pi]$-module $E(\overline{\mathbb F}_q)$ | proved here | none needed |
| Theorem 2: module $\cong$ iff same $\mathrm{End}$; overlaps determine the order, not the class | proved here (Tate's theorem, local freeness standard) | O1–O3, T1, P1–P5 |
| E3: explicit $\pi$-equivariant $\Phi:E_4(\overline{\mathbb F}_7)\to E_5(\overline{\mathbb F}_7)$; trace-fibre statistics agree | checked ($m\le12$, $18$; pointwise at $m=4$) | O1–O3 |
| "class invisible to all local data" | negative finding as stated; true for unpolarised data | T2, W1, W2 |
| polarised local data separate E3 at $\ell=2$ (and at $\ell=3$ up to the sign of $e$) | proved here; checked on curves and lattices | T2, T3, W1–W3 |
| polarised local data see exactly the genus; genus = class when $\mathrm{Cl}^2=1$ | sketched (Gauss, from memory) | T4 (genera differ) |
| E2: orders differ; degree-0 overlaps at level 1 separate the pair | checked | P1–P5 |
| what sees the class: the lift's period lattice; Serre–Tate coordinates do not | standard, from memory | C6–C8 |
| Weil pairing as the theta-group commutator on $L(nO)$, an operator-valued overlap | standard (Mumford) / heuristic as a code datum | none |
| a non-stabiliser overlap of $\Theta_K$ that sees the class beyond its genus | open | none |

`checks/check_overlap_data.py`: **40 of 40 pass**, in about 40 s.

## 8. Next

- **A genus-blind example.** $q=8$, $a=3$, $D=-23$, $\mathrm{Cl}=\mathbb Z_3$, one genus. Prediction: the three curves are inseparable by the overlaps and also by the
  Weil pairings at every $\ell$. Only the lift separates them. Checking this would test §3, item 4.
- **The theta group as a code datum.** Decide whether translations by $E[n]$, acting on the overlap space $L(nO)$, can be written as an operation on $\Theta_K$
  and product stabiliser states (rational translations are automorphisms of $K$). If they can, then the polarised local data, and hence the genus, are
  code data.
- **Back to $\mathbb Q$.** The ladder of `curve-bridge.md` §6 now has a step 2½: the order is code data, the class is not, and the genus is code data only
  with a polarisation. Whether this local/global split has a counterpart for the archimedean blocker of `adelic-gkp.md` §12 is *open*.
