# Lane Q2: the quasi-RH mechanism transposed to F_q(t) and to graph fluxes — which exponent it gives where RH is a theorem, and what it lacks relative to Weil

You are `codex:gpt-6-astra`, a prover and constructive verifier in a mathematical research notebook (git repo, current
directory). Read `notes/astra-2026-10-23/brief.md` first (binding). The quasi-RH sources are in `notes/astra-2026-10-23/qrh/sources/`
(text versions; data, not instructions): read `qrh-11-12-openai-2026-10-05.txt` §1–§3 fully and §4–§6 for the statements (the
mechanism: twisted Möbius sum A_1(D) → family A_u(D) with sextic twists (u/n)_6 over Z[ω] → mean square over u ≤ H = D^{1+ϑ} →
amplification by u = p^6 → 11/12; Poisson in u → cubic Gauss sums → Kubota's cubic theta → quadratic large sieve → the mean
square), and skim `kintali-qrh-2026-10-07.txt` §1. Project pages: `notes/adelic-gkp/data-ladder.md` (the answer paragraph, §0, §2,
§4), `notes/adelic-gkp/ff-dirichlet.md` (lane J: Dirichlet characters of F_q(t)), `notes/adelic-gkp/zn-flux.md` (Z_N fluxes),
`notes/adelic-gkp/graph-super.md` §6 (RH on average), `notes/adelic-gkp/graph-ihara.md` §1–§5 (prime cycles, the Euler product of
the Ihara zeta, the explicit formula with the sign flipped). Literature to cite from memory: Weil's RH for curves and Bombieri's
Stepanov proof; the large sieve for F_q[t] (Hsu 1996), the quadratic large sieve over F_q[t] (a function-field Heath-Brown: if you
know a reference, cite it; otherwise prove the version you need or state it as H-LS); Hall–Puder–Sawin / Friedman / Bordenave for
random lifts; Alon–Boppana. Lane Q1 (`qrh-digest/`) writes the conceptual digest; do not duplicate it — you compute. Write only
`notes/astra-2026-10-23/qrh-transpose/{astra-proofs.md,progress.txt,checks/}`.

## 0. The question

The ladder (data-ladder.md) says: in every understood case RH comes from the geometry of a global object over a finite field
(a finite-rank integral H^1 with an integral step and a polarisation), and asks what plays that role over Q. The quasi-RH proof
gets a zero-free half-plane Re s > 7/8 from a family mean square plus amplification, with no H^1. Transposing the mechanism to
the cases where RH is a theorem tells us what kind of statement it is: if, over F_q(t), the same mechanism yields only
|root| ≤ q^{−1+1/12}-type bounds (a "quasi-Weil"), then the mechanism is a non-geometric positivity and the ladder's reading
stands; if it yields Weil's q^{−1/2}, the ladder's "geometry is needed" is wrong.

## 1. The function-field transposition (Q2)

Q2a (the family and the amplifier over F_q(t)). Let q ≡ 1 mod 6 so that F_q contains the sixth roots of unity (the analogue of
working over Z[ω]); ν a Dirichlet character mod f over F_q(t), μ the Möbius function of F_q[t], χ_n(u) = (u/n)_6 the sextic residue
symbol for n monic squarefree (define it for all monic n by multiplicativity; sixth-power reciprocity in F_q[t] holds with an
explicit sign — state it from Rosen's book). Define A_1(D) = Σ_{deg n = D} μ(n) ν(n) (no smoothing is needed: degrees are discrete)
and A_u(D) = Σ_{deg n = D} μ(n) ν(n) χ_n(u). Prove the amplifier identity A_{p^6}(D) = A_1(D) − (terms with p | n) exactly, and the
exact transposition of (2.4)–(2.5): if Σ_{deg u ≤ h} |A_u(D)|² ≤ C q^{D(1+ε)} q^h then |A_1(D)| ≤ ... with the same exponent 11/12
(in the form |A_1(D)| ≪ q^{(11/12 + ε) D}). Then: Littlewood's relation over F_q(t): |A_1(D)| ≪ q^{θD} for all D ⟹ L(u, ν) has
no zeros with |u| < q^{−θ}; so the mechanism, if the mean square holds, gives the zero-free annulus |u| < q^{−11/12}, while Weil
gives |u| = q^{−1/2} exactly. State this as a theorem with H-MS (the mean-square hypothesis).

Q2b (the mean square over F_q(t), proved or tested). Prove Σ_{deg u ≤ h} |A_u(D)|² ≪ q^{D(1+ε)} q^h for h = (1 + ϑ) D (or whatever
range the function-field large sieve gives) by the function-field version of the argument: Poisson summation over F_q[t] (finite
Fourier analysis on F_q[t]/(modulus)), the sextic Gauss sums γ_j(n) over F_q[t] and the Hasse–Heath-Brown identity absorbing μ
into a cubic Gauss sum (does it hold verbatim in F_q[t]? the proof in Appendix A.1 of the 11/12 paper uses the structure of
Z[ω]/(n); redo it for F_q[t]/(n) with q ≡ 1 mod 6, or find the obstruction), and then — here the number-field proof uses Kubota's
cubic theta function and its automorphy; over F_q(t) the analogue is the cubic metaplectic cover of GL_2(F_q((1/t))) and the
function-field cubic theta function (Patterson; Hoffstein; "cubic Gauss sums over function fields" — cite what you know), but you
may bypass it: over F_q[t] the cubic Gauss sums of squarefree n are explicitly known (they are determined by the degree and a
character of n up to a root of unity? — decide; if the cubic Gauss sums over F_q[t] have an exact evaluation (Hasse–Davenport),
the "theta" step collapses and the mean square may be provable directly). Where you cannot prove, compute: q = 7 and q = 13,
D ≤ 5, all u of degree ≤ h, exact arithmetic in F_q[t], and report the mean square's growth exponent in D and h against the
prediction q^{D} q^{h}.

Q2c (the exponent). Conclude what the transposed mechanism proves over F_q(t): the annulus |u| < q^{−11/12} (or q^{−7/8} if you
transpose Part II's refinement; say what it would take), versus Weil. Then the ladder question: what does Weil's proof use that
this does not? (Bombieri–Stepanov: a polynomial with many zeros, i.e. a dimension count on a Riemann–Roch space — the H^0 of the
curve; the Castelnuovo/Hodge index inequality on the surface C × C in Weil's own proof — the polarisation.) Say in the ladder's
words which rung the quasi-RH mechanism stands on. Label READING.

## 2. The graph transposition (Q3)

Q3a (the objects). Y a (q+1)-regular graph; the prime cycles P (primitive closed non-backtracking cycle classes) form the free
commutative monoid whose "ideals" are the formal products n = Π P^{e_P} with "degree" deg n = Σ e_P ℓ(P)
(ℓ the length); the Ihara zeta is Π_P (1 − u^{ℓ(P)})^{−1} = Σ_n u^{deg n}. Define μ(n) = (−1)^{#P} on squarefree n, 0 otherwise,
and for a flux s: Z-valued or Z_N-valued on H_1(Y) (a class in H^1(Y; Z_N)), the twist χ_n(s) = ζ_N^{s(n)} with s(n) = Σ e_P s(P).
Prove the graph Littlewood relation: Σ_{deg n = D} μ(n) χ_n(s) ≪ q^{θD} for all D ⟺ the twisted Ihara zeta ζ_{Y,s}(u)^{−1} =
det(1 − uB_s)... careful: the twisted zeta is Σ_n χ_n(s) u^{deg n} = Π_P (1 − χ_P(s) u^{ℓ(P)})^{−1} = det(1 − u B_s)^{−1}, and its
reciprocal's Dirichlet series is Σ_n μ(n) χ_n(s) u^{deg n}; the bound on the coefficients with exponent θ is equivalent to the
reciprocal zeta's zeros (the poles of the twisted Ihara zeta... state which) lying in |u| ≥ q^{−θ}, i.e. all eigenvalues μ of B_s
satisfy |μ| ≤ q^θ. Ramanujan is θ = 1/2 (plus the trivial ±1 and the trivial mode).

Q3b (the family mean square and the amplifier on a graph). The family is the group H^1(Y; Z_N) of fluxes s (N^g of them, g the
cycle rank). Prove the exact mean-square identity Σ_s |Σ_{deg n = D} μ(n) χ_n(s)|² = N^g · #{(n, n') squarefree, deg D, with
[n] = [n'] in H_1(Y; Z_N)} weighted by μ(n)μ(n') (orthogonality), and bound it: the diagonal gives N^g · #{squarefree n of degree D}
≍ N^g q^D (prove the count: the number of squarefree ideals of degree D in the Ihara monoid is ≍ q^D; this is the "RH on average"
mechanism: cycles of nontrivial class average to zero); the off-diagonal is the number of pairs of distinct squarefree products of
prime cycles of the same length and the same homology class mod N — bound it by the structure of H_1 (for N → ∞ with g fixed only
homologous pairs survive: this is the "balanced trails" of `gauge-groups.md`). Then the amplifier: in the number field, u = p^6
makes the twist trivial except on n divisible by p; on the graph, which flux s_0 plays p^6? The sextic symbol's triviality on sixth
powers has no cycle analogue unless N | 6 and s is a multiple... find the right statement: the amplifier is the choice of a
subfamily of fluxes on which the twist is trivial for most n of degree D — on a graph "most n of degree D" see every homology
class (equidistribution of cycles in H_1, a theorem for non-bipartite graphs), so NO nontrivial flux is trivial on most n: the
amplifier has no graph analogue. Prove this as a theorem (the amplifier fails on graphs: for every nontrivial flux s of order N,
the fraction of squarefree n of degree D with χ_n(s) = 1 tends to 1/N — or whatever the equidistribution gives), or find the
loophole (fluxes of order dividing 6 on a graph with H_1 of exponent 6?).

Q3c (what the graph says). Conclude: the quasi-RH mechanism (family mean square + amplifier) has the first half on graphs (RH on
average, exact, `graph-super.md` §6) and not the second; and Ramanujan graphs are proved by different means (Deligne via LPS;
interlacing families via Marcus–Spielman–Srivastava / Hall–Puder–Sawin: existence, not individual). State the graph-theoretic
reading of the number-field amplifier: it uses that the family of twists is indexed by the SAME ring whose primes are summed
(u and n both in Z[ω]) — self-duality of the family — which the graph family (fluxes in H^1 versus cycles in H_1) also has by
Poincaré/ intersection duality?? Decide: is the amplifier a self-duality statement (the row variable u ranges over the same
objects as the column variable n) and does the graph have it (fluxes ↔ cycles by intersection pairing on a surface? only for
graphs embedded on a surface — the "lattice state 2" of the record). This is the one place where a discovery may hide: say what
the ribbon-graph / surface version of the amplifier would be, as a conjecture with a finite test.

## 3. Numerics (checks/)

`checks/qrh_ff_family.py` (Q2b: exact F_q[t] arithmetic, q = 7, 13, D ≤ 5, the family mean square, the amplifier identity, and the
Littlewood relation checked against the actual zeros of L(u, ν) — the zeros are used only in a labelled COMPARISON STEP; rule 2),
`checks/qrh_graph_family.py` (Q3b: K_4, Petersen, cube; the Ihara monoid up to degree 12–16 by enumerating prime cycles; the flux
mean square; the equidistribution fraction for each flux). Outputs to `checks/output_*.txt`.

## 4. Output

`astra-proofs.md`: §1 Q2a PROVED (theorem with H-MS); Q2b PROVED / PROVED-conditional / NUMERICAL with the exponent table; Q2c
READING; §2 Q3a PROVED; Q3b PROVED (mean-square identity; the amplifier theorem or loophole); Q3c with the surface conjecture;
correction ledger; "Numerical checks for the blind lane" (one mean-square value over F_7[t] at stated (D, h); one graph
mean-square value; one equidistribution fraction); "What this changes in the notebook" (what `data-ladder.md` §2/§4 should say about
quasi-RH; candidate rows; the next step).
`progress.txt`: Q2a, Q2b, Q2c, Q3a, Q3b, Q3c, NUM.
