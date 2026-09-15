# The Ramanujan property for graded transfer channels: a definition that survives the continuum limit

Session 2026-09-15, TJO's quest item: "I want to understand what the correct definition is for the
Ramanujan property. Working from the MPS picture, provide a rigorous definition that makes sense in
the continuous limit. Harrow expanders ought to have a clean continuous limit. The starting point
is MPS with graded bonds: even here I am not sure in the graded case if we really understand the
Ramanujan property yet. My feeling is we only have quantum expanders for ungraded bond space /
antiperiodic BCs. Can that be."

Orchestrator draft, written alone; statements D1-D14 are drafted deliberately a little too strong
and go to one codex gpt-6-astra lane for proofs and corrections (`astra-brief.md`). Numerics:
`scripts/graded_ramanujan.py` (79 checks, `outputs/graded_ramanujan.txt`). Nothing here is
reviewed.

## 0. Answer in one paragraph

TJO's feeling is correct as a statement about the literature and about this notebook up to
yesterday: every quantum expander we have (Hastings, Harrow, the Weil-LPS channels, the A2
complexes) is a channel on an ungraded bond whose ring zeta 1/det(1 - uE) has only poles, and on
an ungraded bond the periodic and antiperiodic closures coincide. Zeros need a bond grading P and
the periodic (Ramond) closure, whose ring norm is the supertrace str E^n (shards 04e/04f, 03b), and
the zeros are then the eigenvalues of E on the odd sector of the doubled bond, the coherences
between the two parity blocks. The correct definition of the Ramanujan property is a statement
about the *divisor of the parity-closed ring zeta* (poles = net-even modes, zeros = net-odd modes):
every divisor point outside a trivial set lies on the critical circle |mu| = sqrt q (lattice) or
the critical line Re z = omega/2 (continuum), q = e^omega being the growth of the ring norm. Stated
on the ring norms it passes to the continuum verbatim, because e^{eps T} has the same ring norms
as the cMPS for every eps, and in a genuine continuum limit the grading survives if and only if
the even letters are drift plus jumps and the odd letters are jumps of finite rate (an odd letter
cannot be close to 1). Graded quantum expanders do exist and are abundant: a channel built from
an irreducible representation induced from an index-2 subgroup (Clifford theory) is graded by the
coset parity, both parity sectors of its doubled bond obey Harrow's bound sector by sector, and the
odd sector of its non-backtracking lift carries zeros on the critical circle. The smallest one is
the six-letter Pauli channel on a qubit, whose parity-closed non-backtracking ring norms are the
point counts 8, 32, 104, 640, ... of an elliptic curve over F_5. What is *not* yet understood is
a graded expander of *circle type* with a group-theoretic mechanism: in the Harrow-type examples
the odd sector is Hermitian and lands in a band, and the circle only appears after the
non-backtracking lift; in the curve-type examples (Artin-Schreier, 06h) the odd block is sqrt q
times a unitary directly, with no lift and no Hermitian channel. Those are two different
mechanisms for the same divisor statement, and the Riemann case needs the second kind in the
continuum, on regular data (the ||Z(t)|| = 1 negative of 2026-09-14).

## 1. The graded transfer channel and its two ring norms (recalled, shards 02f, 03b, 04f)

Bond H = H_+ (+) H_-, parity P = 1 (+) (-1), D_+ + D_- = D. Letters A_s in B(H) homogeneous:
P A_s P = eps_s A_s, eps_s = +-1. Doubled transfer E = sum_s A_s (x) conj(A_s) on H (x) conj H, or
in the channel picture E(X) = sum_s A_s X A_s^+ on B(H). Doubled-bond parity Gamma = P (x) conj P
= Ad(P); E commutes with Gamma. Sectors:

- even, B(H)_0 = B(H_+) (+) B(H_-), block-diagonal operators, dimension D_+^2 + D_-^2, an
  algebra containing every positive operator, hence the fixed point;
- odd, B(H)_1 = B(H_-, H_+) (+) B(H_+, H_-), block-off-diagonal operators (parity coherences),
  dimension 2 D_+ D_-, contains no nonzero positive operator, hence no fixed point.

E_0 = E|even, E_1 = E|odd. Even letters preserve each off-diagonal block, odd letters swap them.
Ring norms of the length-n ring closed with B: ||Psi_B||^2 = Tr[(B (x) conj B) E^n]. The two
natural closures: B = 1 (antiperiodic / NS), N_1(n) = Tr E^n = Tr E_0^n + Tr E_1^n; B = P
(periodic / Ramond), N_P(n) = str E^n = Tr E_0^n - Tr E_1^n. Both are sums of squares of word
amplitudes, N_P(n) = sum_w |Tr(P A_w)|^2 >= 0, N_1(n) = sum_w |Tr A_w|^2 >= 0.

Graded ring zeta: Z_P(u) = exp(sum_n N_P(n) u^n / n) = 1/sdet(1 - uE) =
det(1 - uE_1)/det(1 - uE_0). Divisor nu(lambda) = m_0(lambda) - m_1(lambda) (algebraic
multiplicities in the two sectors): poles at nu > 0, zeros at nu < 0, and lambda with nu = 0 is
invisible (the "eaten pole" of shard 03b). cMPS: same with E = e^{L T}, N_P(L) = str e^{LT},
Z_P(z) = 1/sdet(z - T) (thm:cmps-sdet).

**D1 (graded Weil-Hodge inequality).** For every graded transfer channel and every n >= 1,
|Tr E_1^n| <= Tr E_0^n; in particular rho(E_1) <= rho(E_0) = q. Equality of spectral radii forces
a net cancellation (an odd eigenvalue of modulus q cancels or dominates an even one in N_P).
*Proof sketch:* N_1(n) >= 0 and N_P(n) >= 0 give Tr E_0^n >= +-Tr E_1^n. This is the graded
form of Weil positivity (shard 08b) and the finite-dimensional shadow of the Hodge index
inequality |Tr M^n|^2 <= Tr S_+^n Tr S_-^n of shard 06e. (Checked numerically on all examples.)

## 2. Growth, trivial set, critical circle; RH, FE, Ramanujan

*Growth.* q := rho(E) = rho(E_0), the Perron root of the completely positive map E on B(H)
(the Perron eigenvector can be taken even; positive operators need not be even, e.g. 1 + X, but no nonzero positive operator is odd). *Counting normalisation:* the ring norms are counts
N_P(n) = sum_lambda nu(lambda) lambda^n with leading term q^n. *Channel normalisation:* divide
the letters by sqrt q; then the fixed point is 1 and everything below is divided by q.

*Trivial set.* The following even modes are present for structural reasons and are excluded from
the Ramanujan statement:
(a) the fixed point q, with nu(q) = 1 ("graded primitivity": no odd eigenvalue at q, so the
    pole at u = 1/q is not eaten);
(b) its images under the period: if E is irreducible with period k on the positive cone, the
    eigenvalues of modulus q are exactly zeta q, zeta^k = 1 (Perron-Frobenius; bipartite graphs:
    -q);
(c) NOT the P-mode in general. If the channel is *parity-twisted trace preserving*,
    sum_s eps_s A_s A_s^+ = r 1 (equivalently E(P) = r P), then P is an even eigenvector with
    eigenvalue r, structurally present. For a unital channel with unitary letters r = w_even -
    w_odd, the signed weight of the letters; for the 06h elliptic tensor r = 1 (projective) or 0
    (affine), the H^0 pole at s = 0, the functional-equation partner of the fixed point, which IS
    trivial by (d). But for the Pauli channel r = -2 lies inside the band and its Ihara-Bass
    quadratic contributes a pole pair ON the critical circle (cancelled there by an odd quadratic);
    in the bipartite Harrow case r = -(q+1) is the period image of q, trivial by (b). So the P-mode
    is structural, not trivial: Ramanujan constrains it like every other mode, which for unitary
    letters is the *balance condition* |w_even - w_odd| <= lambda_H (or r in {1, 0, q, period
    images}).
(d) the value 1 (the pole at s = 0 in the counting normalisation) and the functional-equation partners of (a)-(b) when an FE is present (below).

**D2 (P-mode).** For a graded channel with homogeneous letters, E(P) = P sum_s eps_s A_s A_s^+;
if sum_s eps_s A_s A_s^+ = r 1 then P is an even eigenvector with eigenvalue r, and for a unital
channel with unitary homogeneous letters of weights w_s, r = sum_s eps_s w_s. For a
representation channel (section 4) r = eps(W_S), the value of the sign character on the walk
element. (Elementary; checked on all examples.)

*Critical circle / line.* In the counting normalisation the critical circle is |mu| = sqrt q,
the geometric mean of the fixed point q and the value 1 (the pole at s = 0 in the curve and
Riemann cases; the trivial edge eigenvalue 1 produced by the Ihara-Bass quadratic in the graph
case). In the channel normalisation it is |mu| = q^{-1/2}; for a generator T (cMPS) it is the line
Re z = omega/2 where omega = log q is the leading rate (counting) or Re z = -omega/2 (channel
normalisation, fixed point at 0). In every case: *the fluctuation of the ring norm is the square
root of its leading term* (def:rh-analogue), i.e. all correlation lengths equal 2/omega
(obs:rh-mps-correlation-length).

**Definition (graded RH, FE, Ramanujan).** Let (H, P, E) be a graded transfer channel with
divisor nu and trivial set Triv.
- *RH (one-sided, square-root cancellation):* every lambda with nu(lambda) != 0, lambda not in
  Triv, satisfies |lambda| <= sqrt q. Equivalently N_P(n) - N_P^{triv}(n) = O(n^c q^{n/2}).
- *FE:* there is an even similarity J of the doubled bond (J commutes with Gamma) with
  J E J^{-1} = q E^{-1} on the support of nu; then nu(q/lambda) = nu(lambda) parity by parity.
  (Shard 06h: J = diag(1,-1)_even (+) swap_odd for the elliptic tensor. Shard 08b: inverse-paired
  letters give the FE for the non-backtracking lift.)
- *Ramanujan (two-sided):* RH and FE; equivalently every nontrivial divisor point lies on the
  critical circle, even (poles) and odd (zeros) alike.
- *Manifest (Hilbert-Polya) form:* there is a Hermitian form G on the doubled bond, Gamma-even,
  positive definite on the odd sector and on the nontrivial even sector, with E^+ G E = q G there,
  i.e. E_1/sqrt q and E_0^{nontriv}/sqrt q are G-unitary. Manifest implies Ramanujan (with
  diagonalisability); the converse is prop:hp-inner-product-discrete sector by sector.
For a cMPS generator T: replace |lambda| <= sqrt q by Re lambda <= omega/2, J E J^{-1} = q E^{-1}
by J T J^{-1} = omega - T, and the manifest form by T_1 = omega/2 + i H_1 with H_1 G-self-adjoint
(the "e^{-t/4} rescaling" of the Riemann normalisation, where omega = 1/2).

*Remark (band versus circle).* For a Hermitian channel (unitary letters closed under adjoint, equal
weights) every eigenvalue is real, so "on the circle" would force lambda in {+-sqrt q} and the
definition is degenerate. The Ramanujan statement for such channels is the band |lambda| <=
2 sqrt(q) with q = D - 1 (Hastings), and the circle statement holds for the *non-backtracking
lift* T whose divisor is the divisor of the quantum Ihara zeta (section 3). The definition above
is applied to whichever operator generates the ring norms in question; the band is what it becomes
under Ihara-Bass. This is obs:rh-iff-ramanujan-channel, now sector by sector.

## 3. Graded quantum Ihara-Bass, graded quantum expanders, graded Alon-Boppana

Letters A_i = U_i unitary, homogeneous, with a fixed-point-free reversal i -> ibar, U_ibar =
U_i^+ (so U_i and U_ibar have the same parity). Hashimoto operator on B(H) (x) C^D:
T(X (x) e_i) = sum_{j != ibar} Ad(U_i)X (x) e_j. It commutes with Gamma (x) 1; sectors T_0, T_1.

**D3 (graded quantum Ihara-Bass).** With Sigma_k = D E_k (unnormalised channel on sector k),
n_0 = D_+^2 + D_-^2, n_1 = 2 D_+ D_-:
  det(1 - u T_k) = (1 - u^2)^{n_k (D-2)/2} det(1 - u Sigma_k + (D-1) u^2), k = 0, 1.
Hence the graded quantum Ihara zeta 1/sdet(1 - uT) equals
  (1 - u^2)^{(D-2)(n_1 - n_0)/2} prod_{lambda odd} (1 - lambda u + q u^2) / prod_{lambda even}
  (1 - lambda u + q u^2),
and (D-2)(n_1 - n_0)/2 = -(D-2)(D_+ - D_-)^2/2: for a balanced grading D_+ = D_- the trivial
(1 - u^2) factors cancel exactly. *Proof:* thm:qihara-general's proof on each Gamma-invariant
subspace; Gamma (x) 1 commutes with every ingredient. (Checked: Pauli, (5;13), (13;5).)

**D4 (graded Ramanujan = both sectors in the band).** For a Hermitian graded channel, every
nontrivial divisor point of the graded quantum Ihara zeta lies on |u| = q^{-1/2} iff every
eigenvalue of Sigma_0 outside {+-(q+1)} (as applicable) and every eigenvalue of Sigma_1 satisfies
|lambda| <= 2 sqrt q. Zeros are the odd-sector quadratics, poles the even ones. The trivial set of
the zeta is {1, q} from lambda = q+1, {-1, -q} from the P-mode lambda = -(q+1) when all letters are
odd (bipartite case), and +-1 from the (1 - u^2) factor.

**Definition (graded quantum expander).** A trace-preserving graded channel Phi (channel
normalisation) on B(H_+ (+) H_-) with a unique fixed point (necessarily even) is an
(D_+|D_-, D, lambda_0, lambda_1) graded quantum expander if |lambda| <= lambda_0 < 1 for every even
eigenvalue outside the trivial set and rho(Phi_1) <= lambda_1 < 1. It is *Ramanujan* if
lambda_0 = lambda_1 = lambda_H = 2 sqrt(D-1)/D (Hermitian case) or if its divisor is Ramanujan in
the sense of section 2 (general case). The odd gap -log lambda_1 is the decoherence rate of the
parity coherences; RH says all parity coherences decay at exactly the critical rate.

**D5 (graded Alon-Boppana).** For a graded channel with D unitary letters closed under adjoint
(equal weights), rho(Phi_1) >= lambda_H - c log log(D_+D_-)/log(D_+D_-): the odd sector cannot beat
the Hastings value either. *Proof:* Hastings' trace argument (0706.0556, sd10.tex, the section
"Lower bounds", the quantum Alon-Boppana bound) restricted to the odd sector: Tr Phi_1^{2k} >=
sum over words freely reducing to the identity of Tr Ad(1)|odd / D^{2k} = 2 D_+ D_- N(0,2k)/D^{2k}
with N(0,m) >= c (2 sqrt(D-1))^m/(m+1)^{3/2}; compare with 2 D_+ D_- rho(Phi_1)^{2k}. (Not checked
numerically beyond the examples; the prover should confirm the words that reduce to 1 act as 1 on
the odd sector, which is immediate, and that no other words are needed.)

## 4. Graded Harrow expanders: Clifford theory supplies the grading

Let G be a finite group with an index-2 subgroup G_0 and sign character eps: G -> {+-1},
ker eps = G_0. Let pi be an irreducible unitary representation of G whose restriction to G_0 is
reducible; by Clifford theory it splits as pi|G_0 = pi_+ (+) pi_-, two conjugate irreducibles
swapped by the odd coset, and pi = Ind_{G_0}^G pi_+. Let P = +1 on H_+ = pi_+, -1 on H_- = pi_-.
Then P pi(g) P = eps(g) pi(g): elements of G_0 are even letters, elements of the odd coset are odd
letters. For a symmetric generating set S of G, the Harrow channel Phi = (1/|S|) sum_{s in S}
Ad pi(s) is a graded channel.

**D6 (graded Harrow).** (i) Gamma = Ad(P) is a G-intertwiner of pi (x) conj pi = End(H), so the
even and odd sectors are G-subrepresentations: even = pi_+ (x) conj pi_+ (+) pi_- (x) conj pi_-
(as G_0-modules), odd = pi_+ (x) conj pi_- (+) pi_- (x) conj pi_+. (ii) The trivial representation
occurs once, in the even sector (the scalars); the sign representation eps occurs once, in the even
sector, spanned by P, with Phi(P) = eps(W_S) P, eps(W_S) = (#even - #odd letters)/|S|. (iii) Every
other constituent sigma of either sector satisfies |sigma(W_S)| <= lambda_2(Cay(G,S)) (Harrow's
transfer, 0709.1142:main.tex:213), so if Cay(G,S) is Ramanujan then Phi is a graded Ramanujan
quantum expander (band form) and, by D3-D4, the odd sector of its non-backtracking lift carries
zeros on |u| = q^{-1/2}, q = |S| - 1. (iv) The ring norms are character sums over the Cayley graph:
Tr Phi^n = |S|^{-n} sum_{|w| = n} |chi_pi(w)|^2 and str Phi^n = |S|^{-n} sum_{|w| = n}
|chi_+(w) - chi_-(w)|^2 where chi_pi = chi_+ + chi_- on G_0 and chi_pi = 0 off G_0 (induced
character), so only words with product in G_0 contribute to either norm; the odd sector's trace
is the cross term 2 Re sum_w chi_+(w) conj(chi_-(w)) / |S|^n. (v) Artin factorisation: the graded
quantum Ihara zeta is prod over constituents sigma of the odd sector of det(1 - u T_sigma) over the
same product for the even sector, T_sigma the Hashimoto operator of sigma(W_S) (dimension
dim sigma times multiplicity): the L-functions of the graded expander are the sigma-factors, with
zeros for odd-sector constituents and poles for even-sector ones.

**Example (LPS, bipartite case).** G = PGL_2(F_p), G_0 = PSL_2(F_p), eps = Legendre symbol of the
determinant. pi = principal series I(chi, chi^{-1}) with chi a character of F_p^* of order 4
(p = 1 mod 4), dimension p + 1, splitting on PSL_2 into two halves of dimension (p+1)/2. S = the
q + 1 LPS quaternions of norm q with (q/p) = -1, which lie in the odd coset: all letters odd,
Cay(G,S) bipartite, Ramanujan by LPS. Numerics (`scripts/graded_ramanujan.py`): (p;q) = (5;13)
and (13;5). Both sectors in the band (max odd |lambda| = 4.00 and 4.25 against 2 sqrt q = 7.21 and
4.47), P-mode -(q+1), Harrow containment of both sectors in the Cayley spectrum, str Phi^n >= 0 with
the word formula (iv) verified on words of length <= 3, graded Ihara-Bass on both sectors, odd
edge eigenvalues on |mu| = sqrt q (36 and 196 of them), even edge eigenvalues on the circle plus
{+-q, +-1}. The graded quantum Ihara zeta is P(u)/[(1-u)(1-qu)(1+u)(1+qu)] with P of degree
2 g, g = 18 and 98, all zeros on the critical circle, and the (1-u^2) factors cancel (balanced
grading). In the (13;5) case the extremal Hecke eigenvalue 4.2497 lives in the *odd* sector.

**Example (the smallest one).** G = Pauli group mod centre = Z_2 x Z_2, G_0 = <Z>, pi = the qubit,
P = Z; letters X, X, Y, Y, Z, Z (each self-adjoint letter listed twice so the reversal is
fixed-point-free), D = 6, q = 5. Even spectrum {6, -2}, odd {-2, -2}; graded quantum Ihara zeta
(1 + 2u + 5u^2)/((1-u)(1-5u)); str T^n = 8, 32, 104, 640, 3208, 15392 = 1 + 5^n - (mu^n + conj
mu^n), mu = -1 + 2i. These are the point counts of the elliptic curves y^2 = x^3 + 4x + b, b in
{0, 1, 4}, over F_5 (8 points, a_5 = -2). Word reading: str T^n = 4 x #{cyclically
non-backtracking Pauli words of length n with product proportional to Z}.

## 5. The continuum limit

**D7 (exactness).** For a graded cMPS (Q even, R_a homogeneous) the lattice channel E_eps =
e^{eps T} has ring norms N_P^{(eps)}(n) = str e^{n eps T} = N_P(n eps) for every eps, so the divisor
of the lattice zeta is {e^{eps lambda}} and the critical circle |e^{eps lambda}| = e^{eps omega/2}
is the critical line Re lambda = omega/2: RH, FE and Ramanujan are eps-independent.

**D8 (graded Chernoff; the grading lives in the jumps).** Let Phi_eps be graded channels with
Phi_eps = 1 + eps T + o(eps) in norm. Then Phi_eps^{floor(L/eps)} -> e^{LT}, both ring norms
converge, T commutes with Gamma, and T is a graded cMPS generator: Q even and the jump operators
homogeneous. Conversely any Gamma-commuting T of Lindblad form (Q = -iH - (1/2) sum R^+ R) has Q
even (H even) and R_a homogeneous up to an even unitary re-mixing of the jumps. Odd letters cannot
be O(1)-close to the identity (P A P = -A and A = 1 + O(sqrt eps) is impossible), so an odd letter
enters the continuum limit as sqrt(eps) R with R an odd jump of finite rate, never as a drift.
*Consequence:* in the continuum, parity-changing dynamics is dissipative; "fermionic zeros" are
relaxation modes and there is no Hamiltonian odd letter. (This is why obs:jump-operator-guidance
needed an even-odd *Hamiltonian* on the doubled bond, i.e. on the coherences, rather than an odd
letter.)

**D9 (jump Lindbladians: the band is affine).** For T = sum_s g_s (Ad U_s - 1), homogeneous
unitaries closed under adjoint, e^{tT} = e^{-Gt} e^{G t Phi} with G = sum g_s and Phi the weighted
channel; spectrum of T = G (spec Phi - 1); the graded Ramanujan band for the equal-rate case is
[-G(1 + lambda_H), -G(1 - lambda_H)] on both sectors, and the non-backtracking lift exists
(words are discrete). Checked on the Pauli jump Lindbladian: even {0, -2(g_X + g_Y)}, odd
{-2(g_Z + g_Y), -2(g_Z + g_X)}; the P-mode rate is twice the total odd-letter rate.

**D10 (what the divisor is when there is no trace).** For an infinite-dimensional graded bond the
ring norms are defined as distributions (def:distributional-trace) or through correlation
functions of regular data: for X, Y in a dense subspace of regular vectors, F_{X,Y}(L) =
<X, e^{LT} Y> has a Laplace transform meromorphic beyond Re z = omega/2 (an assumption of the same
kind as asm:explicit-formula-trace), and the divisor is the union of its poles, signed by Gamma.
When the transform has continuous spectrum, nu is a signed measure and RH reads supp(nu) \ Triv
subset {Re z <= omega/2}. The definition is deliberately *not* the L^2 spectrum of T: for the
compressed Riemann semigroup ||Z(t)|| = 1 for all t (the two Opus readers, 2026-09-14,
unreviewed), so no statement on the Hilbert space K_S can see the rate 1/4; the divisor of the
correlation functions of regular data can. The manifest form must then be stated on a weighted or
anisotropic space of regular data, exactly as resonances are for Anosov flows.

## 6. Harrow's continuum limit, ungraded and graded

*Ungraded.* Replace the finite group by a Lie group G with Lie algebra generators X_1..X_d and the
letters by exp(+-sqrt(eps) X_j): Phi_eps = 1 + (eps/2d) sum_j B_j^2 + O(eps^2) with B_j = [dpi(X_j), .]
on Hilbert-Schmidt operators, so T = (1/2d) sum_j B_j^2 = (1/d)(2 Cas_{pi (x) conj pi} + (1/2) B_W^2)
for sl_2 with the two non-compact generators (prop:quantum-lindblad-tensor). Harrow's transfer
"gap of Phi >= gap of the Cayley graph" becomes:

**D11 (continuous Harrow).** For pi tempered, pi (x) conj pi is weakly contained in the regular
representation (Fell absorption: pi < lambda implies pi (x) sigma < lambda (x) sigma = (dim sigma)
lambda), so spec(-T) on the K-invariant sector of HS(pi) is contained in {2 s(1-s): s = 1/2 + ir}
= [1/2, oo) (Casimir normalisation of shard 09b): the gap 1/2 is the tempered threshold, the
continuous Ramanujan value, attained by every tempered pi. For infinite-dimensional pi there is no
normalisable fixed point (1 is not Hilbert-Schmidt) and no discrete divisor: the spectrum is
purely continuous. The edge-level (circle) statement is about the matrix coefficients of the flow
Ad pi(a_t) on the constituents sigma_s of pi (x) conj pi: they decay as e^{-st} and e^{-(1-s)t}
(spherical function asymptotics), so the correlation "divisor" is supported on the lines
Re z = -s, -(1-s), on the critical line Re z = -1/2 iff sigma_s is tempered. Harrow's continuum
limit is therefore clean and is exactly: *Ramanujan = temperedness of pi (x) conj pi*, with the
flow entropy omega = 1 and the critical rate 1/2; the discrete zeros appear only after passing to
a lattice quotient, where the constituents become Maass forms (Selberg's 1/4 = Ramanujan, shard
09c). Question for the prover: for the complementary series pi_s of SL_2(R), pi_s (x) pi_s contains
a complementary series iff s > 3/4 (Repka 1978, from memory, must be checked), so the quantum
Lindbladian of pi_s is Ramanujan for 1/2 < s <= 3/4 although pi_s is not tempered; the threshold
s = 3/4 is Selberg's 3/16 = (3/4)(1/4). Is that a coincidence?

*Graded.* Take G = PGL_2(R), G_0 = PSL_2(R), eps = sign of the determinant. The irreducible unitary
representations of PGL_2(R) induced from G_0 are exactly the discrete series pairs pi = D_k^+ (+)
D_k^- (holomorphic and antiholomorphic weight k), swapped by the reflection r = diag(-1, 1);
principal and complementary series restrict irreducibly and do not grade. Even letters: the sl_2
generators (drift/diffusion); odd letter: the reflection, which cannot be small and enters as a
jump at rate gamma.

**D12 (graded continuous Harrow).** T = (1/2d) sum_j B_j^2 + gamma (Ad pi(r) - 1) on HS(D_k^+ (+)
D_k^-) commutes with Gamma = Ad(P), P = 1 (+) (-1). (i) Even sector: D_k^+ (x) conj D_k^+ (+)
D_k^- (x) conj D_k^-, each = D_k^+ (x) D_k^-, which contains the principal series continuously:
spectrum of the diffusion part [1/2, oo) on K-invariants (Ramanujan), and the jump splits it into
r-symmetric (shift 0) and r-antisymmetric (shift -2 gamma) halves; the P-mode 1_+ - 1_- is
antisymmetric, at -2 gamma (its FE partner would be at -2 gamma: critical line Re = -gamma for the
jump part). (ii) Odd sector: D_k^+ (x) conj D_k^- (+) c.c. = D_k^+ (x) D_k^+ (+) D_k^- (x) D_k^-
= (+)_{m >= 0} D_{2k+2m}^{+-}, purely discrete series, no principal, no complementary, no trivial
constituent: the odd-sector diffusion spectrum on the lowest K-types is the *ladder* n/2... (to be
computed exactly by the prover: -T on D_n at K-type m is n(2-n)/2 + m^2/2 in the shard-09b
normalisation, minimal at |m| = n, value n), and the matrix-coefficient exponents along a_t are
-n/2, n = 2k + 2m, an arithmetic ladder starting at -k, i.e. at or beyond the FE partner: the
continuous odd sector is the analogue of the Gamma-factor ladder diag(-(k + 1/2)) of the Riemann
graded generator (prop:riemann-graded-generator), and it carries no critical-line modes. (iii)
Character reading: str e^{tT} = integral over G of the heat kernel against |chi_+ - chi_-|^2, and
chi_{D_k^+} = chi_{D_k^-} on hyperbolic elements, so the supertrace sees only elliptic classes:
in the PGL_2(R) grading the closed geodesics live in the even sector and the odd sector is
compact. (iv) For k = 1 (limit of discrete series), D_1 (x) D_1 = (+) D_{2+2m} gives exponents
-(1 + m), the Gamma_C ladder (poles of Gamma(s) at 0, -1, -2, ...), and its symmetric and
antisymmetric parts Sym^2 D_1 = (+)_{m even}, Lambda^2 D_1 = (+)_{m odd} give the Gamma_R ladder
(poles of Gamma(s/2): every other rung) and its complement. Prover: confirm or correct the
decompositions and the exponents.

The bearing of D12 on the Phantasm: the reflection grading of PGL_2(R) puts the critical continuum
(and, on a lattice quotient, the Maass zeros) in the *even* sector and the archimedean ladder in
the *odd* sector, the opposite of the Riemann assignment (zeros odd). The grading that makes the
Selberg zeros odd is the transverse form-degree grading of the geodesic flow: Dyatlov-Zworski
write the Ruelle zeta as the alternating product over k of the flat-trace zeta on k-forms
(1306.4203:zeta.tex, eq:Rue, with det(I - P) = sum_k (-1)^k tr wedge^k P at line 526), and the
Selberg zeta Z(s) = det(1 - L_s) is the fermionic (odd-degree) factor. The two gradings are
different: PGL_2 grading = holomorphic/antiholomorphic, form-degree grading = stable/unstable
transverse degree. The form-degree grading is the one found in the ring-norm-tensor campaign
(grading = form degree on the torus, Tier A). Statement to test next: on the doubled bond of a
representation channel of PSL_2(R), the form-degree grading is the K-type grading m = 0 (functions)
versus m = +-2 (1-forms), and the uniform shift m^2/2 = 2 of the K-type-2 sector against the
K-type-0 sector is the continuous analogue of the -2 gamma parity-jump shift of
prop:parity-jump-uniform-shift. Not drafted as a claim.

## 7. Where this leaves the graded Ramanujan property

Understood (definitions, elementary theorems, examples):
1. The definition: divisor of the parity-closed ring zeta, trivial set, critical circle/line,
   RH / FE / Ramanujan / manifest, and its exact stability under the continuum limit (D7-D8).
2. Graded quantum expanders exist with a mechanism: Clifford-theory gradings of Harrow channels
   (D6), band form, zeros on the circle after the non-backtracking lift (D3-D4), optimal by the
   graded Alon-Boppana (D5); Weil-LPS with odd generators gives Hecke-eigenvalue zeros; the qubit
   Pauli channel gives an elliptic curve over F_5.
3. Curve-type graded channels (Artin-Schreier 06b, elliptic 06h) are Ramanujan by a different
   mechanism: no lift, no Hermitian channel, the odd block is sqrt q times a unitary, the P-mode is
   the H^0 pole by parity-twisted trace preservation (D2).
4. Harrow's continuum limit is clean and is temperedness (D11); its graded version (D12) is the
   archimedean ladder.

Not understood (the honest list):
5. A graded channel of *circle type* with a group-theoretic (Harrow-like) mechanism: a
   non-Hermitian graded channel whose odd block is sqrt q-unitary because of a representation, not
   because it was written down that way. Artin-Schreier is the prototype (Parseval); a general
   principle relating "Hermitian channel + non-backtracking lift" to "odd block unitary" is
   missing. The Ihara-Bass quadratic is such a principle for graphs (it manufactures the FE
   partner and the circle from a real band); the analogue for curves is the Hodge index.
6. The continuum circle statement for a non-normal generator on regular data (the Riemann case):
   D10 defines it; no example with an infinite discrete divisor on the critical line other than
   Riemann itself and the Selberg lattice case is in the notebook.
7. Which grading of the Selberg side is the Phantasm's: PGL_2 (zeros even) or form degree (zeros
   odd). Section 6 argues form degree.

## Drafted statements for the prover (prove, correct, or refute; declare hypotheses H-*)

D1 graded Weil-Hodge inequality. D2 P-mode / parity-twisted trace preservation. D3 graded quantum
Ihara-Bass with the (1-u^2) exponents n_k(D-2)/2 and their cancellation for balanced gradings.
D4 graded Ramanujan equivalence (band iff circle, sector by sector, trivial set as stated).
D5 graded Alon-Boppana for the odd sector. D6 graded Harrow (i)-(v), including the character
formula for str and the Artin factorisation. D7 exactness. D8 graded Chernoff and "odd letters are
jumps". D9 jump Lindbladians. D10 the divisor via correlation functions (state precisely what is
assumed). D11 continuous Harrow: tempered implies gap 1/2 via Fell absorption + Cowling-Haagerup-
Howe or a direct SL_2(R) argument; the Repka threshold. D12 graded continuous Harrow for PGL_2(R):
Clifford theory for PGL_2(R) versus PSL_2(R), the sector decompositions, the ladder exponents, the
elliptic-support of the supertrace, the Sym^2 / Lambda^2 ladders.

D13 (the general C^{1|1} graded channel with unitary letters): for D unitary homogeneous letters
closed under adjoint on C^{1|1}, q = D - 1, even spectrum {D, r} with r = #even - #odd (the P-mode),
odd spectrum {lambda_1, lambda_2} real, and the graded quantum Ihara zeta is
  (1 - lambda_1 u + q u^2)(1 - lambda_2 u + q u^2) / [(1 - u)(1 - q u)(1 - r u + q u^2)],
the (1 - u^2) factors cancelling since D_+ = D_-. It is Ramanujan iff |lambda_1|, |lambda_2|,
|r| <= 2 sqrt q (or r = -(q+1), bipartite, all letters odd, in which case lambda_i = ... state it).
For the Pauli letters {X,X,Y,Y,Z,Z}: r = lambda_1 = lambda_2 = -2 and one odd quadratic cancels
the P-mode pole pair, leaving the genus-1 numerator 1 + 2u + 5u^2. Prover: derive the general
formula, the cancellation condition, and whether the numerator is always a Weil q-polynomial
(integrality of the ring norms holds since they are counts of words; is the numerator always the
L-polynomial of a curve over F_q, or only a Weil polynomial?).

D14 (no ungraded expander has zeros; no graded expander with only even letters has a unique fixed
point): the two elementary facts behind TJO's question, stated as a proposition with proof.


## Corrections received from the prover lane (2026-09-15, `astra-proofs.md`)

PROVED D2, D3, D9, D14. CORRECTED D1 (equal radii need not share an eigenvalue; positive operators
need not be even), D4 (net divisor only; converse needs no hidden modes), D6 (bipartite = period
two; Pauli group, not its quotient; Artin factors with net exponents and T_sigma from letters; the
LPS numerator degrees 36/196 were the raw odd counts, reduced 4/4 and 144/144), D7 (aliasing), D8
(fixed bond; odd Kraus letters collectively O(sqrt h)), D10 (relative resonance divisor via Riesz
projections), D11 (threshold 1/(2d) for the walk vs 1/2 for T_*; type-zero bound >= 1/2 iff
tempered for PSL2(R); discrete series tempered with faster exponents), D12 (k >= 2 even; exact rates
kappa(n+2nj+2j^2); P not HS; hyperbolic contributions cancel; Gamma-ladder positional only), D13
(exact qubit formula; non-integral / non-curve numerators). REFUTED D5 (no odd Alon-Boppana).
Definitions: signed trivial divisor with parities; two reference rates in the continuum; graded CP
transfer vs graded spectral transfer; signed unitality, not TP. The shards carry the corrected
statements; this note keeps the original draft for the record.
