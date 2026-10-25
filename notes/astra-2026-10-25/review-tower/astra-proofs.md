# Lane RT: adversarial review of lane T

Author: `codex:gpt-6-astra` (reviewer), 2026-10-25. This is a **same-family** REFUTE review; the notebook gate still requires a second-family review of lane T. No record page or registry is edited. No RH assumption or number-field zero is used.

Scope: the five requested items, including all five candidate rows and the additional proved/refuted claims omitted from the candidate table. Exact scripts and logs are in `checks/`. Verdicts will be written incrementally after derivation and independent recomputation.

## 1. RT1 — `thm:ordinary-torsion-similitude-order`

**VALID (PROVED from the stated standard classification and Tate theorem; independently recomputed).** Over a *fixed* finite field, the isomorphism class of the full Frobenius torsion group, equipped with its compatible Weil and reduced Frey–Rück pairings modulo one compatible cyclotomic automorphism, is exactly the pair (isogeny class, endomorphism order). It contains no further relative ideal-class invariant.

**T0 definitions: VALID.** Perfect rank-two Weil pairings are restricted to N prime to p. For an ordinary curve the geometric p^a-torsion is cyclic of order p^a and mu_{p^a}(Fbar_q) is trivial; it is retained separately with its unit-root Frobenius action. Thus geometric points are not identified with the full rank-two p-primary torsion of a complex torus. Lane T states this distinction, and its direct-sum construction includes the actual etale p-primary group.

### Compatibility and the ideal action

Waterhouse's ordinary classification says that the curves **in the fixed ordinary F_q-isogeny class with endomorphism order O** form a torsor under Pic(O), using proper invertible ideals. This is not a claim about arbitrary noninvertible ideals, or about all twists over the algebraic closure. In particular the action is transitive even when O is nonmaximal. The notebook's `cit:latimer-macduffee` records the torsor input; the actual arithmetic input here is Waterhouse/Deligne, not just rational similarity of matrices.

Here is an explicit proof of the prime-to-N representative assertion for a nonmaximal order. Given an invertible fractional ideal J and finitely many rational primes S, write J_l=b_l O_l. The inverse fractional ideal J^{-1} is a rank-two Z-lattice, with completion b_l^{-1}O_l. CRT in this lattice chooses a nonzero alpha in J^{-1} with alpha b_l in 1+l O_l for all l in S. Then A=alpha J is integral and invertible, has class [J], and A_l=O_l for l in S. Thus its index is prime to every prime in S. Include the characteristic and conductor primes in S when needed. No Dedekind factorisation at conductor primes was assumed.

An ideal chosen prime to N' does identify every level dividing N', but arbitrary choices for different N' are not a pro-system isomorphism. **Lane T explicitly repairs this**: for each rational prime l choose one ideal isogeny phi_l of degree d_l prime to pl, and use it on the *whole* l-primary group. Their direct sum Phi is a Frobenius-equivariant isomorphism E(Fbar_q) -> E'(Fbar_q). Hence the square with vertical multiplication [N'/N] commutes for every N|N', as does the square with inclusions. On inverse limits this is an isomorphism of Tate modules, and on the discrete direct limit it is the single Phi. It also commutes with field inclusions, Frobenius traces, and every multiplication map. The multipliers (d_l)_{l != p} form one element of the product of Z_l^units; CRT gives a_N, with a_N' reducing to a_N. There is no requirement that these profinite units come from one ordinary integer degree. The explicit 2/3-isogeny maps in the numerical audits are instances of this construction.

### Which Tate pairing, on which sides, with which exponent

Put Q=q^k and N|Q-1. The pairing used is the **reduced Frey–Rück pairing**

    t_N : E(F_Q)[N] × E(F_Q)/N E(F_Q) -> mu_N,
    t_N(P,[R]) = f_P(D_R)^((Q-1)/N),  div(f_P)=N D_P,

with disjoint degree-zero divisor representatives. It is often called the Tate or Tate–Lichtenbaum pairing; this is not an invocation of Lichtenbaum's original local-field pairing. It is not restricted to E[N] in both variables. Nor does N|Q-1 imply that E[N] is rational. [Bruin, §1 and §3–4](https://www.numdam.org/item/10.5802/jtnb.764.pdf) verifies these domains and the Kummer description.

Independently deriving naturality: choose NS=R. The Kummer value is (pi^k-1)S, and t_N is its evaluation against P under the Weil pairing (with one globally fixed sign convention). For phi:E->E' defined over F_q, use

    e'_N(phi P,T') = e_N(P,hat(phi) T'),
    (pi^k-1)phi S = phi((pi^k-1)S).

Consequently

    t'_N(phi P,[R']) = t_N(P,[hat(phi) R']),
    t'_N(phi P,[phi R]) = t_N(P,[R])^(deg phi).

The first identity acts by phi on the torsion argument and by the **dual** isogeny on the other argument. The second acts by phi on **both** arguments, and its exponent is d, not d², d^{-1}, or 1. Applying a map to only one side without the dual is not the identity used. The same exponent d scales e_N. Reversing the Weil/Kummer convention inverts both Tate pairings and changes neither identity. Unreduced Miller outputs are representatives modulo Nth powers; equality of arbitrary representatives is not asserted. The exact PARI/FLINT comparisons in §3 check the reduced convention directly.

### Why the tower sees the conductor

It recovers the pi-action on T_l E for every l != p, and hence the **integral** centraliser

    C_l = End_{Z_l[pi]}(T_l E) = End(E) tensor Z_l.

The rational centraliser is K tensor Q_l. Its identification is fixed by pi, so the index of C_l in the integral closure gives v_l(f_End), not merely the conductor of Z[pi]. This is the exact step at which the conductor is detected. Ordinariness gives p not dividing the trace or trace²-4q; therefore every possible order is maximal and split at p. Intersecting the completions recovers O. Finally #ker(pi-1)=#E(F_q) recovers the trace, and the fixed-q isogeny class follows. This direction does not mistake a finite sample of abstract point groups for the full Frobenius module.

[Lenstra, Theorem 1(a)](https://pub.math.leidenuniv.nl/~lenstrahw/PUBLICATIONS/1996c/art.pdf) gives E(F_{q^k}) ≅ O/(pi^k-1)O for every k. For an invertible ideal lattice I, I/(pi^k-1)I is free rank one over that finite semilocal ring, explaining the independence of the ideal class. Individual isomorphisms need not be chosen compatibly; Phi already supplies the compatible ones.

**The requested “separating k for lane T's F_41 example” does not exist.** Its trace is 12 and disc Z[pi]=12²-4·41=-20, fundamental. Both curves have the same maximal order, so their abstract groups agree for *every* k. They separate by strict pairings, not by an extension's group. This mistaken premise belongs to the RT brief, not to lane T. The independent census gives the following groups; [a,b] denotes Z/a × Z/b.

| pair | endomorphism conductors | groups at k=1 | groups at k=2 | smallest separating k |
|---|---|---|---|---|
| F_41, trace 12: (A,B)=(1,17),(3,11) | 1,1 in D_K=-20 | [30], [30] | [270,6], [270,6] | none, for all k |
| **new** F_41, trace 6: (6,20),(1,13), j=5,22 | 1,2 in D_K=-8 | [18,2], [18,2] | [72,24], [144,12] | **2** |
| **new** F_7, trace 1: (0,5),(3,5), j=0,3 | 1,3 in D_K=-3 | [7], [7] | [21,3], [63] | **2** |

These orders are certified, rather than guessed from j. For trace 6 over F_41, write w²=-2 and pi=3+4w. The only possible conductors are 1,2,4, and on O_f the matrix is [[3,-8f],[4/f,3]]. The index-one and index-two Smith invariants above distinguish all three possibilities: f=4 has [36] already at k=1. Also pi²-1=24(w-1); full rational 24-torsion at k=2 implies (pi²-1)/24=w-1 is an endomorphism and forces f=1. Rational 12-torsion but not full 24-torsion forces f=2. For the trace-1 pair, take w²-w+1=0, pi=-1+3w, so pi²-1=3(w-3). Full rational 3-torsion at k=2 is equivalent to containing w and forces the maximal order; otherwise f=3. Base groups coincide, proving the stated k are minimal. The script also checks the respective class polynomials, all allowed conductors, all curves in these isogeny classes, and six extension groups by PARI.

Recompute: `python3 notes/astra-2026-10-25/review-tower/checks/independent_arithmetic.py`; certificate: `checks/output_independent_arithmetic.txt`. The separate PARI audit of the lane's supplied curves is `checks/output_pari_audit.txt`.

## 2. RT2 — `thm:ordinary-strict-tower-genus`

**VALID (PROVED, including nonmaximal orders).** Within the fixed ordinary isogeny class and order, the strict tower is the Pic(O)/Pic(O)² torsor. Its compatible multipliers at N are exactly

    S_N(c) = Norm(A_0) H_N,    H_N = Norm((O/NO)^units),

where A_0 is any integral invertible representative of c prime to N. “Genus” means proper ideal classes modulo squares, not ideal classes themselves. The theorem is not an assertion that one fixed level separates every distinct genus.

### Independent check of the norm reduction and principal genus argument

For A=alpha A_0 in the same class, with both ideals prime to N, alpha is a unit of O_l at every l|N; hence Norm(A)/Norm(A_0) belongs to H_N. Conversely choose alpha in A_0^{-1} with any prescribed unit residue modulo N at these primes, by CRT. Then alpha A_0 is integral, invertible, prime to N, and realises the specified norm residue. This proves both inclusions, for nonmaximal orders too. Global units are insufficient: one needs units of the finite local rings. Multiplication by u on the rank-two lattice has determinant Norm(u). The centraliser of the *whole* local pi-module is O_l, so its invertible automorphisms give exactly these factors. Reduction O_l^units -> (O/l^a O)^units is surjective. The other primes can be chosen independently. This proves that S_N is precisely the reduction of the compatible multiplier coset.

Let A represent the relative class and let d=Norm(A)>0. Give O and A the same complex orientation. Their unimodular alternating forms differ by the covolume factor d. An intertwiner O_l -> A_l is multiplication by x_l, and the strict condition is

    A_l=x_l O_l,    Norm(x_l)=d.                 (*)

There are no additional pi-centralising rational maps: pi generates the quadratic algebra. At p the algebra is split, the order is maximal, and its unit norm map is surjective. Thus omitting the connected p-primary geometric points loses no obstruction to (*). The real-place norm condition is automatic because d>0.

If A=alpha B², and B_l=b_l O_l, the generator

    x_l = alpha b_l² · Norm(B)/Norm(b_l)

has norm d. The final scalar is a Z_l-unit because the two norms have the same l-adic valuation. Thus every square class is strictly locally isometric. Conversely assume (*). Replace A by a representative prime to its order's conductor. Hasse–Minkowski for the quadratic norm conic gives alpha in K with Norm(alpha)=d. Once it has a rational point this conic is rational, so weak approximation lets alpha agree sufficiently closely with x_l at the finitely many conductor primes. Consequently B=A/(alpha) has norm one and B_l=O_l at those primes. Now factor **only away from the conductor**, where O is Dedekind. Inert or ramified prime exponents vanish; at each split rational prime the two exponents are opposite. Hence B=C/conjugate(C) for an invertible fractional ideal C prime to the conductor. Since [conjugate(C)]=[C]^{-1}, [A]=[C]². No illegal factorisation of noninvertible conductor ideals occurs.

Finally, congruence solutions at every l-power give nested nonempty closed subsets of the compact group O_l^units; their intersection gives (*). Thus the infinite tower is compatible even if reductions between particular finite sets of intertwiners are not surjective. The Kummer derivation in §1 makes the reduced Tate pairings redundant once Frobenius, all division maps and the Weil pairings are present.

The class-field terminology survives for a nonmaximal order provided it refers to the **ring class field H_O**, not automatically to the Hilbert class field of K. Under Artin reciprocity Gal(H_O/K)=Pic(O), and the relevant genus field is H_O^{Pic(O)²}. Complex conjugation acts by inversion, so this is the largest subfield of H_O abelian over Q. It may ramify at conductor primes. Replacing the local groups Norm(O_l^units) by Norm(O_{K,l}^units) erases precisely some conductor information and would give the wrong genus. The proof above establishes the norm-residue formulation without needing a precomputed genus-field formula.

### The isolated-level caveat is real, but does not invalidate the tower iff

Lane T's example is correct: O has discriminant -7, pi=3+7w, w²-w+2=0, q=128 and trace 13. The pi-matrix [[3,-14],[7,10]] becomes scalar modulo 7. Consequently its isolated E[7] centraliser has all six possible nonzero determinants, while the extendable norm subgroup is {1,2,4}. The other three determinants cannot extend to the full 7-adic tower.

A stronger **new actual-curve example** shows that even an isolated strict isomorphism between *different genera* can be misleading. Over F_41, trace 6, the curves

    y²=x³+x+13 (j=22),     y²=x³+2x+12 (j=29)

both have End of discriminant -32 and conductor 2, whose Picard group has order two. Here [O:Z[pi]]=2. Direct division-polynomial enumeration of all torsion points and all intertwiners gives:

| N | compatible ideal-norm set S_N(nontrivial) | all isolated E[N] Weil multipliers |
|---|---|---|
| 4 | {3} | **{1,3}** |
| 8 | {3} | {3,7} |
| 16 | {3,11} | {3,11} |

Thus an E[4] isometry exists although the strict towers are nonisomorphic; that isometry cannot extend to E[8]. This does not break the all-level iff. For O=Z[pi], as in the -24, -20 and -84 tests below, the regular-module centraliser already has the expected size at every level, so the finite-level exception does not arise. These results also delimit the caveat: “isolated” here means just E[N] with Frobenius and Weil pairing, not the already compatible full group tower with its division points.

### Independent brute force over actual ideals

`independent_arithmetic.py` enumerates all integral HNF lattices of index at most 1024 stable under the order, keeps the invertible ones, and reduces their norm forms to determine their proper classes. Specifically, with w²-s w+n=0 they have bases c(A,B+w), where A divides B²+sB+n. Invertibility is tested by primitivity of (A,2B+s,(B²+sB+n)/A). Thus this is an actual ideal search, independent of lane T's residue-vector enumeration. For every displayed set it prints a smallest-norm HNF witness for **every** residue. Comparing with the finite norm-form values gives an upper bound matching the search, certifying exhaustion of the residue sets rather than relying on an unproved norm cutoff.

For D=-24, columns are the classes (1,0,6), (2,0,3):

| N | principal | nontrivial |
|---|---|---|
| 2 | {1} | {1} |
| 3 | {1} | {2} |
| 4 | {1,3} | {1,3} |
| 8 | {1,7} | {3,5} |
| 9 | {1,4,7} | {2,5,8} |
| 16 | {1,7,9,15} | {3,5,11,13} |

For D=-20, columns are (1,0,5), (2,2,3):

| N | principal | nontrivial |
|---|---|---|
| 2 | {1} | {1} |
| 3 | {1,2} | {1,2} |
| 4 | {1} | {3} |
| 5 | {1,4} | {2,3} |
| 8 | {1,5} | {3,7} |
| 9 | {1,2,4,5,7,8} | {1,2,4,5,7,8} |
| 16 | {1,5,9,13} | {3,7,11,15} |

For **D=-84**, all four reduced classes square to the principal class (also checked by PARI `qfbpow`), so Pic ≅ (Z/2)². The four columns are respectively (1,0,21), (2,2,11), (3,0,7), (5,4,5):

| N | c0 | c1 | c2 | c3 |
|---|---|---|---|---|
| 2 | {1} | {1} | {1} | {1} |
| 3 | {1} | {2} | {1} | {2} |
| 4 | {1} | {3} | {3} | {1} |
| 7 | {1,2,4} | {1,2,4} | {3,5,6} | {3,5,6} |
| 8 | {1,5} | {3,7} | {3,7} | {1,5} |
| 12 | {1} | {11} | {7} | {5} |

The N=12 row alone distinguishes all four classes; equivalently N=3 and N=4 together do. Representative small norms for the nontrivial columns are 2,3,5; representatives prime to 12 of norms 11,7,5 witness that row.

**Actual curves, not just forms.** Take p=37=4²+21, pi=4+sqrt(-21), trace 8. Its Frobenius discriminant -84 is fundamental, so every curve in the class has End=O_K. Exhaustive model counting finds exactly four F_37-isomorphism classes, represented by (A,B)=(2,2),(2,11),(3,14),(5,17), with j=7,3,2,28. All have [30] at k=1 and [690,2] at k=2; PARI also agrees with Lenstra's groups through k=6. Division-polynomial roots provide E[3] over F_{37³} and E[4] over F_{37⁴}; no lane-T sampling or lattice-identification routines are imported. The pairing multiplier sets for all six pairs are:

| j pair | N=3 | N=4 |
|---|---|---|
| 3,7 | {1} | {3} |
| 2,7 | {2} | {3} |
| 7,28 | {2} | {1} |
| 2,3 | {2} | {1} |
| 3,28 | {2} | {3} |
| 2,28 | {1} | {3} |

Every pair is strictly separated. Taking j=7 as a relative base identifies j=2,3,28 with c1,c2,c3 respectively; this is a relative torsor labelling, not a claim that j=7 is the epsilon-normalised principal curve. Independent pairing recomputation also reproduces {2} at N=3 and {3,5} at N=8 for D=-24, and {3} at N=4 and {3,7} at N=8 for D=-20. Additional actual-ideal tests for nonmaximal D=-32,-36 reproduce their norm cosets. D=-23 has three proper classes with squares permuting all three; the square subgroup is all of Pic, so the theorem correctly predicts a single strict genus.

Commands: `python3 notes/astra-2026-10-25/review-tower/checks/independent_arithmetic.py` and `python3 notes/astra-2026-10-25/review-tower/checks/independent_pairings.py`. Certificates: `checks/output_independent_arithmetic.txt`, `checks/output_independent_pairings.txt`, with machine-readable curve and pairing tables alongside them.

## 3. RT3 — the two numerical candidate rows and the pending PARI rerun

**`num:q7-strict-tower-audit`: VALID (NUMERICAL). `num:q41-same-order-tower`: VALID (NUMERICAL).** The common orders, scale sets, six-extension group tables, explicit isogenies and the pairing identities reproduce. The previously pending PARI arithmetic is now executed, with the one explicitly documented database substitution below. There is no arithmetic discrepancy.

### Unchanged-script reruns versus lane T's saved outputs

| script | result | comparison with saved output |
|---|---|---|
| `tower_audit.py` | all assertions pass | all 108 lines identical in the FLINT-only run |
| `tower_strict.py` | all assertions pass | all 71 lines identical |
| `replay_tower_flint.py` | 22/22; all 42 cases; additional common-multiplier check passes | 108 lines identical except elapsed seconds |
| `replay_cm_flint.py` | 27/27; conjugation check passes | 36 lines identical except elapsed seconds |
| `audit_overlap_refinement.py` | all W1–W3 checks pass | 19 lines; the only differences are the appended printed coordinate scalars (1,1) and (4,1) on the two isogeny lines |

The last difference is a stale-output formatting difference, not changed arithmetic: the current shared helper prints those two extra values. `checks/diff_overlap_refinement.txt` records the exact diff. `rerun_flint.py` prints source hashes and checks all five return codes. Nothing in the old lane was edited; bytecode writes were disabled.

The main audit was then run with its previously unexecuted cypari2 branch. PARI is **2.17.2**. Keeping the original FLINT 0.8 finite-field contexts preserves every point coordinate and random-generator certificate in the saved output: the 106 non-PARI output lines are identical. In those exact same fields and on those exact same points:

- **16/16 Weil values and 64/64 reduced Tate entries agree literally**, not just up to a sign, a basis change or a root automorphism: **80/80**.
- **42/42 `pari_validate` calls** agree on both cardinality and group invariants: 24 six-extension cases, 16 pairing-field cases and the two F_5 curves, hence 84 cardinality/group equalities. Some pairing-field groups repeat earlier cases; these are invocation counts, not 42 distinct extensions.
- PARI's four `ellisogeny` outputs have quotient coefficients (1,3), (4,3) over F_7 and (30,3), (38,24) over F_41, exactly the independently calculated Vélu coefficients. The target coordinate scalings are u=1,2 and u=8,14 respectively. The isogeny tests on torsion check Frobenius-equivariance and the degree exponent on both pairings.

Here are the shared extension groups for each pair, each checked for **both** curves:

| k | #E/F_{7^k} | group | #E/F_{41^k} | group |
|---|---|---|---|---|
| 1 | 6 | [6] | 30 | [30] |
| 2 | 60 | [30,2] | 1620 | [270,6] |
| 3 | 378 | [126,3] | 68670 | [68670] |
| 4 | 2400 | [120,20] | 2825280 | [117720,24] |
| 5 | 16566 | [16566] | 115860750 | [23172150,5] |
| 6 | 117180 | [19530,6] | 4750178580 | [37699830,126] |

At F_41 level 8 the source and target values are exactly 14 and 38; 14³=38 mod 41. The degree-3 kernel is {O,(34,6),(34,35)}, the quotient has coefficients (38,24), and u=14 gives (u²,u³)=(32,38). The degree-2 kernel is {O,(35,0)}, quotient (30,3), and u=8 gives (23,20). These prime-to-primary-degree maps define the compatible tower isomorphism, not merely unrelated level maps. The pointwise mixed-primary tests again have 2400 distinct images over F_{7⁴} and 1620 over F_{41²}.

### Original F/U/CM scripts under PARI

`run_pari.py legacy` loads the **original** `rerun_legacy.py`, changing only its output-directory global to this review's checks directory. Its original cypari2 GP-boundary adapter evaluates the unchanged legacy F and U GP payloads. Results:

| legacy check | fresh PARI result | number-by-number comparison |
|---|---|---|
| F `check_overlap_data.py` | **40/40** | all 40 assertion lines, including every printed number, identical to its original saved PARI output |
| U `check_tower_pairing.py` | **22/22**, **42/42 comparison cases** | 42 primary-group tuples, 42 isomorphism counts, 25 Weil scale sets and 42 Tate scale sets all match the saved independent FLINT replay: **151/151 invariant records** |
| CM `check_cm_tower.py`, literally unchanged | stops at `ellinit("441d1")` | missing `/usr/share/pari/elldata/ell0`; preserved failure log, not counted as a successful unchanged execution |
| CM, same arithmetic with explicit recorded curve coefficients | **27/27** | all 27 assertion lines and every printed number identical to the FLINT replay and historical CM output |

The CM workaround is concrete and narrow: `pari_cm_explicit.py` replaces the one `ellinit("441d1")` lookup by `ellinit([1,-1,1,-20,46])`, the coefficients printed in `cm-lift.md` and the historical output. PARI independently checks conductor 441 and j=-3375. All other GP instructions and all original Python assertions are unchanged. The script saves all **15** evaluated GP payloads and their output, and asserts that precisely **one** database lookup was expanded. Thus the arithmetic rerun is complete; this environment still cannot execute the label lookup itself without elldata. No package or database was installed.

The 42 U cases use sampled bases. Raw Frobenius coordinate matrices agree in 13 cases and differ in 29; this is expected, not a mathematical discrepancy. `compare_results.py` finds and prints an explicit invertible change of invariant-factor basis intertwining the two Frobenius actions in **every** case. `checks/output_comparison.txt` reports the group, isomorphism count, Weil set, Tate set and that witness **case by case**; `comparison_certificates.json` preserves them in machine-readable form. The 22 printed assertion lines also agree exactly. The shared sign is addressed below, rather than silently choosing one per case.

For F's decisive seven W1 checks, the independent FLINT and fresh PARI sets agree number by number:

| N | number of equivariant isomorphisms | Weil multipliers |
|---|---|---|
| 2 | 2 | {1} |
| 3 | 6 | {2} |
| 4 | 8 | {1,3} |
| 5 | 16 | {1,2,3,4} |
| 8 | 32 | {3,5} |
| 9 | 54 | {2,5,8} |
| 16 | 128 | {3,5,11,13} |

W3's four degree multipliers are [2,3,2,3] in both backends. F's Riemann–Roch checks now genuinely rerun under PARI: 3816 tested divisors per curve, 1272 degree-zero cases and 210 principal cases; the degree-2-place statistic over F_49 is 22860. These are rerun confirmations, not a claim that the earlier FLINT replacement recomputed the Riemann–Roch block.

The CM five base-prime traces are -1,-4,-8,-2,-6 at p=2,11,23,29,37. Its nine groups and five Tate comparisons are:

| p | k | cardinality | group, ascending invariant factors | N / Tate scales / number of maps |
|---|---|---|---|---|
| 2 | 1 | 4 | [4] | — |
| 2 | 2 | 8 | [8] | — |
| 2 | 3 | 4 | [4] | — |
| 2 | 4 | 16 | [16] | — |
| 11 | 1 | 16 | [2,8] | 2 / {1} / 16 |
| 11 | 2 | 128 | [8,16] | 8 / {1,3,5,7} / 128 |
| 23 | 1 | 32 | [2,16] | 2 / {1} / 32 |
| 29 | 1 | 32 | [4,8] | 4 / {1,3} / 128 |
| 37 | 1 | 44 | [2,22] | 4 / {1,3} / 6 |

### Orders, signs and the additional corrections

Both q=7 curves have six F_7-points, hence trace 2 and disc Z[pi]=**-24**. This is fundamental, forcing End=Z[sqrt(-6)] and conductor **1** on both curves. This settles the requested order computation without a volcano algorithm. It is a same-order genus separation, not different orders or a non-equivariant-identification bug. The original F/U pages already identified this field correctly; the Q(sqrt(-7)) wording was in lane T's brief. Q(sqrt(-7)) belongs to the q=2 E mode and the CM example. PARI `ellisomat` is not being used as a finite-field endomorphism-order oracle; `ellisogeny` with an explicit kernel is the relevant computation here.

There is no accidental matrix-convention switch. For q=7, the record's companion [[2,-7],[1,0]] and the principal ideal matrix [[1,-6],[1,1]] are conjugate by U=[[1,-1],[0,1]], determinant 1. For q=41 replace the -1 in U by -6; for p=37 replace it by -4. The E-mode convention [[0,-1],[2,-1]] is similarly related to [[-1,-2],[1,0]] by [[0,-1],[1,0]]. `independent_linear.py` verifies these identities exactly. Nonprincipal matrices are not being identified integrally with the principal one.

**Tate sign correction: VALID.** The legacy helper evaluates Omega(P,(1-M^k)Q), whereas the page's final formula evaluates Omega(P,(M^k-1)Q). These differ by one global inversion. At N=3 the matched Weil set is {1} and the old-helper Tate set {2}; inversion reconciles them. No curve-dependent adjustment is allowed. Lane T's additional FLINT check of all 25 cases having both pairings passes. A fresh PARI run also checks a common multiplier for all **1688** individual maps in these **25/25** cases after this same single sign correction (`output_pari_u_simultaneous.txt`).

**Well-definedness correction: VALID.** For the formal lattice Tate expression, changing Q's lift by l changes the exponent modulo Z by (q^k-1)Omega(P,l). Unimodularity makes this vanish for all P in G_k[N] exactly when **exp(G_k[N]) divides q^k-1**. N itself is necessary only if G_k has a point of exact order N. The q=2,k=1,N=3 example has G_k=Z/4 and G_k[3]=0, so the zero pairing is well defined although 3 does not divide 1. This was independently enumerated in `independent_linear.py`. The defined Frey–Rück pairing remains under the sufficient hypothesis N|q^k-1; none of the audited separation cases changes.

**CM “not its conjugate” correction: VALID.** In the basis (1,w), w²-w+2=0, conjugation C=[[1,1],[0,-1]] has determinant -1 and satisfies C M_{u+vw}=M_{u+v conjugate(w)} C. The identity is checked for every listed reduction prime. Thus a match for one step gives a match for its conjugate under root inversion; the legacy first-match loop never excludes the second. This does not settle a prescribed common epsilon-normalisation across primes, which remains open. It does refute the unqualified exclusion as an inference from that script.

Reproduce in order from the repository root:

```sh
python3 notes/astra-2026-10-25/review-tower/checks/rerun_flint.py
python3 notes/astra-2026-10-25/review-tower/checks/run_pari.py audit
python3 notes/astra-2026-10-25/review-tower/checks/run_pari.py legacy
python3 notes/astra-2026-10-25/review-tower/checks/pari_cm_explicit.py
python3 notes/astra-2026-10-25/review-tower/checks/run_pari.py u_simultaneous
python3 notes/astra-2026-10-25/review-tower/checks/compare_results.py
python3 notes/astra-2026-10-25/review-tower/checks/independent_linear.py
```

The `legacy` command deliberately preserves the absent-database failure, returning nonzero for that lookup; the following explicit-model command completes its arithmetic. Saved logs distinguish the two. Main scripts' stdout should be redirected to the corresponding `checks/output_*.txt` to refresh comparison inputs.

## 4. RT4 — `prop:torsion-topology-retains-integral-class`

**VALID (PROVED; elementary, not a new arithmetic rigidity theorem).** The homology argument is correct. It is nearly tautological once a topological torus has been supplied with its integral step: that datum already retains the lattice which the profinite comparison forgot. A useful precise proposition to register, if not simply cited as a consequence of `prop:integral-marking-gauge`, is:

> Let L,L' be free Z-modules of finite rank, M in End_Z(L), M' in End_Z(L'), and let T_L=(L tensor R)/L and T_L'=(L' tensor R)/L'. There is a continuous group isomorphism f:T_L -> T_L' satisfying f M=M' f if and only if there is an integral module isomorphism U:L -> L' satisfying UM=M'U. For rank two with common irreducible quadratic characteristic polynomial and proper invertible ideal lattices in the fixed quadratic algebra, this is equivalent to equality of their ideal classes with the specified Frobenius marking.

Proof: the universal cover identifies H_1(T_L,Z) canonically with L, and M_* with M. Thus f_* is the required U. Conversely U tensor R descends to the required continuous group isomorphism. No RH, Weil pairing, norm residue or limiting argument enters this equivalence. Even an arbitrary homeomorphism conjugating the steps would induce such an integral intertwiner on H_1; the stated group-isomorphism formulation is already sufficient.

The first clause of the candidate, that abstract compatible torsion may fail to recover the class, also has a concrete proof. For D=-23, q=8, trace 3, take the principal and nonprincipal matrices

    M0=[[1,-6],[1,2]],    M1=[[1,-3],[2,2]].

Solving UM0=M1U over Z gives U=[[a,-3c],[c,2a+c]], with

    det(U)=2a²+ac+3c²,
    8 det(U)=(4a+c)²+23c².

For c=0 the determinant is 2a²; for |c|>=1 it exceeds 1. Thus it cannot be ±1. The topological tori with these steps are not isomorphic. On the other hand Pic(O_{-23}) has order three, its square subgroup is the whole group, and §2 supplies strict isomorphisms on the compatible torsion towers. `independent_linear.py` solves the intertwining equations independently and prints determinant-one congruence witnesses at N=2,3,4,8,16,23. The all-level assertion follows from the proved square criterion, not from those finitely many witnesses.

The prime-to-p torsion is dense in the real torus, but its **abstract** isomorphism need not be continuous in the induced topology, hence need not extend to the torus. In this example such an extension would contradict the determinant calculation. Remembering topology, or an embedding of all quotients in a common integral lattice, is therefore a genuine strengthening of the input. The proposition should not be advertised as recovering a global lattice from finite quotients alone.

## 5. RT5 — T4 and the proposed record corrections

**T4 verdict: AGREE; lane T's refutation is VALID.** The statement “every local or torsion datum, including fixed pairings, sees at most the order” is false. The q=7 same-order pair already disproves it. The exact replacement is: *the compatible similitude tower sees isogeny class and order; the compatible strict tower additionally sees the relative genus; integral topology with the step sees the full integral class.* These are different equivalence relations on different data.

**Minimality claim omitted from the candidate table: VALID (NUMERICAL plus derivation).** The q=4 pair y²+xy=x³+t and y²+xy=x³+t+1, t²+t+1=0, has four rational points each and j=t+1,t. Independent direct point enumeration and PARI agree. The trace is 1, Frobenius discriminant -15, and the order is maximal. The two classes (1,1,4),(2,1,2) give crossed determinant set {2} modulo 3, independently recomputed. Using **Hasse's theorem for elliptic curves** (not an RH assumption) to bound the ordinary traces, for q=2 they are ±1 and the discriminant is -7; for q=3 they are ±1,±2 and discriminants -11,-8. Each has class number one, as a direct reduced-ideal enumeration confirms. Hence q=4 is the smallest field for a same-isogeny-class, same-order strict-genus counterexample. This is not a minimality claim about arbitrary different-order curves.

**No-go qualification omitted from the candidate table: VALID.** T1/T2 show nonuniqueness of a global integral class from a specified abstract local input. They do not show that no choice of a suitable integral lattice can be constructed, do not supply or rule out a zeta H¹, and do not classify higher-dimensional polarised modules. Also, existence of a formal tower is weaker than the spectral RH condition, while complete count data determine the Frobenius polynomial and hence decide that condition. For example M=[[0,-1],[5,5]] has M^T Omega M=5 Omega and integral V, but trace²=25>4·5=20; all periodic-point quotients still exist. The first five determinants det(1-M^k) are 1,11,76,451,2501, independently recomputed. These are logical scope distinctions, not numerical claims about number-field zeros.

The requested record decisions and concrete replacement wording are as follows. These are recommendations only; no record file was changed.

| record / proposed correction | decision | wording to use |
|---|---|---|
| `HANDOFF.md`, 2026-10-06 Findings (F) | **AGREE** | “Product-stabiliser overlaps determine the ordinary isogeny class and endomorphism order, with no further ideal-class information. With the roots of unity fixed, the Frobenius pairing tower determines the genus; it separates the two D=-24 classes.” |
| `HANDOFF.md`, Findings (U) and Next (iii) | **AGREE-WITH-CHANGE** | “The commutator together with the step recovers the Weil/reduced-Tate data with a fixed sign convention; at N=8 it separates the D=-24 pair even up to inversion. Formal tower existence does not force RH. The 42 comparisons now have both an independent FLINT replay and a fresh PARI audit; the CM arithmetic passes after expanding the unavailable 441d1 database lookup. A common epsilon-normalisation across primes and the second-family review of lane T remain outstanding.” Do **not** retain lane T's now-obsolete statement that the PARI arithmetic is pending. |
| `overlap-data.md`, Findings, §3 items 3–4, §4 closing | **AGREE** | “The full unpolarised Frobenius module determines the order within the isogeny class. The compatible strict polarised tower determines Pic(O)/Pic(O)²; for D=-24 each genus has one class. Allowing one arbitrary compatible cyclotomic automorphism removes this genus distinction.” Its original Findings and §3 already mention genus, so this is an exactness/scope annotation, not a retraction of its q=7 proof. Keep N=3 strict separation and N=8 separation even up to inversion; do not replace them by an order difference. |
| `tower-pairing.md`, Findings, §4 “How far”, Conclusions 4/7 and §7 | **AGREE-WITH-CHANGE** | “For ordinary elliptic curves with fixed order, the compatible fixed-centre Frobenius pairing tower distinguishes exactly the genus. The D=-24 separation remains valid. Arbitrary-unit consistency and equality/inversion code comparisons are distinct equivalences. Use the full rational torsion × rational quotient Tate domain, the single M^k-1 convention, and the exp(G_k[N]) well-definedness condition. The geometric-point/Deligne torsion identification excludes the connected p-primary half. The CM test establishes consistency for psi; its conjugate also works when root inversion is allowed. Uniform epsilon-normalisation across primes is not checked.” This includes the p-primary correction explicitly and records the completed PARI arithmetic with the lookup caveat. |
| `data-ladder.md`, answer paragraph, ordinary-elliptic lattice cell, §1 items 2–3, §2 first two bullets | **AGREE-WITH-CHANGE** | “The global lattice is H_1 of the canonical lift. Counts determine its isogeny class; the abstract Frobenius torsion tower determines its endomorphism order; strict compatible pairings determine its genus. The remaining ideal-class ambiguity is a Pic(O)² torsor. A topological torus with its step retains the full integral lattice. Formal tower existence does not force RH, although its full counts decide the spectral test.” Replace universal “excluded as sources” rhetoric by the model-specific nonuniqueness statement; no zeta construction no-go follows. |
| `lattice-tower.md`, §8 addendum (and the meaning of “blind” in §4/§7) | **AGREE** | “For abstract finite quotients with fixed scalar commutators and a common Frobenius step, the ordinary elliptic invariant is genus, which equals class for the D=-24 pair. The topological syndrome torus with its step retains the integral class through H_1. ‘Blind to RH’ concerns existence of the formal tower, not the information in its count sequence.” |
| `shard-draft/claims-rows.tsv`, `prop:gkp-overlaps-see-order` | **AGREE** | Keep the order theorem, the Frobenius-compatibility hypothesis, the explicit E[8]/E[3] statements, the failure at n=4, and epsilon-dependence. Replace “the Weil pairing sees the class” by “the strict Frobenius pairing tower sees genus; here genus equals class since Pic(O)²=1”. Make the same title/summary correction in `04za_adelic_gkp_ladder.tex`. |
| `obs:gkp-missing-datum` | **AGREE-WITH-CHANGE** | “These elliptic examples show that the indicated abstract local data need not select a unique global integral class or provide a positivity reason; they do not exclude all constructions of a global H¹ from those inputs.” The row remains an observation/reading, not a no-go theorem. |
| `num:gkp-counts-not-lattice` and the registered Lenstra/Latimer–MacDuffee citations | **AGREE: retain** | No refutation or reclassification follows from this review. Do not turn the correctly distinct count, order and integral-class assertions into one invariant. |

For the order/overlap clause of the existing `prop:gkp-overlaps-see-order`, the independent derivation is short: Riemann–Roch fixes h⁰ away from degree zero, while degree-zero h⁰ tests whether the Abel–Jacobi sum vanishes. Preserving all divisors P+Q-R-S forces psi(P)-psi(O) to be a group isomorphism; Frobenius compatibility makes psi(O) rational and that isomorphism pi-equivariant. Conversely a pi-equivariant group isomorphism followed by rational translation preserves all these tests. The conductor argument of §1 then identifies the order. Thus the proposed correction preserves the actual theorem, rather than relying on a numerical sample of overlaps. The epsilon-dependent principal assignment remains consistent with the two simple roots of H_{-24} modulo 7 and the two embeddings of sqrt(2); the separation itself is intrinsic.

## Correction ledger

| attribution | what is wrong, incomplete, or requires qualification | disposition |
|---|---|---|
| Lane T's theorem proofs | No false theorem found within their stated ordinary-elliptic, compatible-tower scope | T1, T2 and the topology proposition are VALID; the independent nonmaximal and four-class tests support their exact boundaries |
| Lane T's saved `output_overlap_refinement.txt` | It predates two additional printed coordinate-scalar fields in the helper | Cosmetic stale-output difference only; actual values and all assertions agree |
| Lane T's execution status | PARI was explicitly left unexecuted; the saved failure logs do not constitute independent PARI evidence | Now completed for F/U and the main audit, and for CM arithmetic with the documented one-lookup substitution; retain the literal missing-elldata failure separately |
| Lane T's exposition of the isolated-level caveat | Correct, but its scalar example does not illustrate an actual false finite-level genus identification between two curves | New D=-32 curves supply that sharper witness: strict E[4] identification exists, strict E[8] identification does not |
| Lane T's proposed HANDOFF “PARI pending” annotation | Historically accurate on 2026-10-23, obsolete after this review | Replace by the precise completed-audit statement, retaining the cross-prime epsilon question |
| Lane T's original brief: “I prime to N' works for all divisors” | Does not itself choose one compatible infinite system | Lane T repaired it correctly with one isogeny on each whole primary tower |
| Lane T's original brief: unqualified Tate pairings “on E[N]” | Wrong/incomplete domain for the perfect reduced Frey–Rück pairing | Use rational N-torsion × rational points modulo N; same degree exponent when phi acts on both arguments |
| Lane T's original brief: Q(sqrt(-7))-type q=7 example | Wrong field | The actual trace-2 pair has D=-24 and K=Q(sqrt(-6)); the original F/U pages already said this |
| Lane T's original brief: T4 says every local/torsion datum sees at most O | False for fixed pairing targets, and conflates a topological torus with abstract torsion | Strict towers see genus; topology plus M sees the integral lattice |
| Lane T's original brief: finite-field `ellisomat` as suggested order tool | Inappropriate API shortcut | The fundamental discriminant proves the q=7/q=41 orders; known-kernel `ellisogeny` validates the explicit maps |
| RT brief item 1(c): smallest separating k for lane T's F_41 pair | No such k exists: same maximal order | Corrected explicitly; a *different trace-6* F_41 conductor-2 pair first separates at k=2, as does the new F_7 conductor-3 pair |
| Older unqualified “pairing sees class” summaries | True for D=-24, false as a general class-reconstruction theorem | Say strict genus, with full class recovery only when Pic(O)²=1 |
| Older U Tate “iff N divides q^k-1” | Necessity omitted the existence of exact-order-N rational torsion | Replace N by exp(G_k[N]) for the formal well-definedness claim |
| Older U CM “psi, not its conjugate” | Unsupported by its first-match loop, and false under arbitrary cyclotomic automorphisms | Conjugation supplies an integral determinant-minus-one intertwiner |
| Zeta extrapolation | Nonuniqueness in the elliptic model is not nonexistence of a global H¹ or a universal obstruction to choosing a lattice | Retain a scoped limitation and the open positivity/construction problem |


## Verdict lines

The five candidate IDs are retained verbatim. T0 and T4 are lane T's item labels; the remaining T-prefixed aliases identify its unnumbered subsidiary assertions so that no proved/refuted claim is omitted from adjudication. “VALID” on a refutation means that lane T's refutation is valid, not that the refuted sentence is true.

VERDICT thm:ordinary-torsion-similitude-order: VALID — primary-tower maps are compatible and integral Frobenius centralisers recover the full order.
VERDICT thm:ordinary-strict-tower-genus: VALID — compatible strict isomorphism is exactly the square-class condition, including nonmaximal orders.
VERDICT num:q7-strict-tower-audit: VALID — D=-24 and multipliers {3,5} modulo 8 reproduce with PARI and independent FLINT arithmetic.
VERDICT num:q41-same-order-tower: VALID — common D=-20, six-extension groups and both isogeny pairing functorialities reproduce exactly.
VERDICT prop:torsion-topology-retains-integral-class: VALID — a continuous step-intertwining torus isomorphism is equivalent to an integral intertwiner on H_1.
VERDICT T0: VALID — the geometric p-primary summand and full reduced-Tate domain are correctly distinguished.
VERDICT T2-isolated-level: VALID — isolated Frobenius centralisers can admit extra multipliers which do not extend to the compatible tower.
VERDICT T3-Tate-sign: VALID — one global inversion of the legacy helper reconciles Weil and Tate multipliers for every checked map.
VERDICT T3-Tate-well-definedness: VALID — the formal necessity condition uses exp(G_k[N]), with N sufficient under the stated Tate hypotheses.
VERDICT T3-CM-conjugation: VALID — determinant-minus-one conjugation refutes the unqualified exclusion of the conjugate step.
VERDICT T4: VALID — fixed pairing targets retain genus, refuting the blanket local-torsion blindness assertion.
VERDICT T4-minimal-counterexample: VALID — the ordinary F_4 discriminant-minus-15 pair is the smallest same-order strict-genus counterexample.
VERDICT T4-zeta-scope: VALID — elliptic local nonuniqueness gives neither a zeta H_1 nonexistence theorem nor a positivity obstruction by itself.

## Numerical checks for the blind lane

These are exact certificates, with no number-field zero input. Run the scripts from the repository root; they write only inside this review directory. The PARI subprocess interpreter is fixed in each driver to the environment specified by the round brief.

1. **Order versus small-extension groups.** `python3 notes/astra-2026-10-25/review-tower/checks/independent_arithmetic.py`: the original F_41 trace-12 pair has **no separating k**. For the new F_41 trace-6 pair (6,20),(1,13), conductors 1,2, the smallest k is **2**: [18,2] agrees at k=1, while [72,24] differs from [144,12] at k=2. For the F_7 trace-1 pair (0,5),(3,5), conductors 1,3, the smallest k is also **2**: [7] agrees, then [21,3] differs from [63].
2. **D=-24 ideal norms.** The same script gives S_3=( {1}, {2} ), S_8=( {1,7}, {3,5} ) and S_16=( {1,7,9,15}, {3,5,11,13} ), in principal/nonprincipal order, by actual invertible ideals of norm at most 1024 with printed HNF witnesses.
3. **D=-20 ideal norms.** It gives S_4=( {1}, {3} ), S_8=( {1,5}, {3,7} ) and S_16=( {1,5,9,13}, {3,7,11,15} ). `independent_pairings.py` reproduces the crossed sets {3} and {3,7} on actual E[4] and E[8].
4. **D=-84, four different genera.** In form order (1,0,21),(2,2,11),(3,0,7),(5,4,5), S_12 is **({1},{11},{7},{5})**. At p=37, trace 8, the four j-invariants are **7,3,2,28**. `python3 notes/astra-2026-10-25/review-tower/checks/independent_pairings.py` checks all **six** pairs: each fails a strict identification at N=3 or N=4, despite identical groups through all six tested extensions.
5. **Nonmaximal isolated-level trap.** The same pairing script gives D=-32, j=22,29 over F_41: the compatible S_4 is **{3}**, but the isolated E[4] scale set is **{1,3}**; at E[8] the actual scale set is **{3,7}** and strict extension fails. The ideal script independently supplies S_8={3}.
6. **PARI versus FLINT.** `python3 notes/astra-2026-10-25/review-tower/checks/compare_results.py` checks **42/42** lane-U cases, **151/151** invariant records and explicit Frobenius basis changes; the main audit has **16/16** literal Weil agreements plus **64/64** literal reduced-Tate agreements, total **80/80**. F passes **40/40**, U **22/22**, CM **27/27** after the one recorded elldata substitution. `run_pari.py u_simultaneous` additionally checks the common multiplier on **1688** maps in **25/25** cases. The original missing-elldata exception is retained and is not counted as a successful lookup.

## What this changes in the notebook

The five lane-T rows can go forward as **`codex:gpt-6-astra`-reviewed, VALID**, with this review and its exact certificates attached. This is a **same-family review of lane T**, so it does **not** by itself satisfy the independent second-family promotion gate.

| candidate | reviewed status / gate disposition | remaining requirement |
|---|---|---|
| `thm:ordinary-torsion-similitude-order` | VALID; suitable for the review queue in its precise compatible-tower formulation | second-family proof review and the ordinary classification/Tate citation dependencies |
| `thm:ordinary-strict-tower-genus` | VALID; suitable for the review queue with the extendability caveat explicitly attached | second-family review of the nonmaximal principal-genus argument; no additional numerical obstruction found |
| `num:q7-strict-tower-audit` | VALID numerical evidence, now backed by fresh PARI as well as FLINT | second-family adjudication for lane-T promotion; keep strict versus inversion-only comparisons distinct |
| `num:q41-same-order-tower` | VALID numerical evidence; PARI validation is complete | second-family adjudication; do not request an impossible separating extension for its same-order pair |
| `prop:torsion-topology-retains-integral-class` | VALID in the precise §4 formulation; may be recorded as an elementary corollary of the existing integral-marking proposition | second-family review if introduced as a new row; avoid claiming new arithmetic reconstruction from torsion alone |

For the older Opus-authored `prop:gkp-overlaps-see-order`, this review supplies **different-family support** for the order dictionary and the two explicit q=7 separations, with the corrected parenthetical in §5. Its existing dependencies and normal gate checks still apply. The unqualified “Weil pairing sees the class” title should change even though the two arithmetic examples stand. No blanket promotion of every claim on the original F/U/CM pages is implied by their pass counts.

Endorse the concrete record corrections in §5: strict genus in HANDOFF and the ladder; exact compatible scope in F/U; the Tate domain, sign and well-definedness correction; deletion of the CM “not its conjugate” exclusion; and the distinction between an abstract torsion tower and a topological torus. Update the execution note to reflect the completed PARI arithmetic and the explicit missing-database workaround. Keep the common epsilon comparison across reduction primes **OPEN**. The additional D=-84 and D=-32 tests are review evidence, not registered claims.

This review changed no notebook page, draft shard, registry, Git state or file outside `notes/astra-2026-10-25/review-tower/`. The next mathematical gate is a second-family review of T1/T2, especially the conductor-prime approximation step and the distinction between compatible and isolated-level maps; the next record action is applying the endorsed wording, separately from promotion.
