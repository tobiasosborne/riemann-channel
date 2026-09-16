# Draft: the Selberg zeta as a graded transfer whose odd-block form is derived from the letters

Orchestrator draft (claude:fable-5.1, 2026-09-16). Statements D1-D8 are deliberately drafted
slightly too strong; the prover lane is to prove, correct or refute each. Nothing here is registered
in the lab book yet.

## Why this object

The notebook's status row (shard 03d, obs:graded-ramanujan-status) lists as not understood: a
Kraus / transfer realisation of the Artin-Schreier, Riemann and Selberg graded spectral transfers;
a principle relating "Hermitian channel plus non-backtracking lift" to "odd block unitary"; and
which Selberg grading is the Phantasm's. In every manifest example in the book the unitarity of
the odd block has a source that is not complete positivity: Parseval (Artin-Schreier), Deligne
(Weil-LPS), or it is put in by hand (06h). The Selberg zeta of a compact hyperbolic surface is the
one infinite object where (i) the trace formula is a theorem, (ii) the divisor is known, and
(iii) the source of reality is known: self-adjointness of the Laplacian. The task is to write it
as a graded transfer in the notebook's language and to exhibit the mechanism as a property of the
letters: the reality of the retained divisor and the functional equation are DERIVED from the
letters (Haar-unitarity of the sl2 flows plus the sl2 relations), and the critical-line placement
is an additional positivity (Selberg's 1/4), exactly as Ramanujan is an additional bound for a
Hermitian graph channel. Then (D6) say precisely where the same mechanism stops on the modular
surface, whose scattering poles are the Riemann zeros.

## Conventions (must match the notebook; see astra-brief.md for the file list)

- G = PSL_2(R), Gamma < G discrete torsion-free cocompact (D1-D5, D7-D8), M = Gamma\H, SM = Gamma\G
  (def:geodesic-flow). Left-invariant fields Bf(g) = d/du f(g exp(uB)) at u = 0, flow = right
  multiplication. Notebook basis H = diag(1,-1), E = ((0,1),(1,0)), W = ((0,1),(-1,0)),
  Casimir Omega = (1/4)(H^2 + E^2 - W^2); geodesic flow generator X = H/2, Koopman
  (e^{-tX} f)(m) = f(phi_{-t} m), phi_t(Gamma g) = Gamma g a_t, a_t = diag(e^{t/2}, e^{-t/2}).
  Dyatlov-Faure-Guillarmou (DFG, 1403.0256, lines 535-544) use the same X and the horocyclic
  fields U_+ = ((0,1),(0,0)) = (E + W)/2, U_- = ((0,0),(1,0)) = (E - W)/2, with [X, U_pm] = pm U_pm,
  [U_+, U_-] = 2X. Then Omega = X^2 + (1/2)(U_+ U_- + U_- U_+).
- Delta = -y^2(d_x^2 + d_y^2) positive on M; on right-K-invariant f = F o pi, Omega f = -Delta F and
  (1/2)(H^2 + E^2) f = 2 Omega f = -2 Delta F (shard 09b, prop:casimir-laplacian), so
  Delta = -(1/4)(H^2 + E^2) on the K-invariant sector. Laplace spectrum lambda_j = s_j(1 - s_j) =
  1/4 + r_j^2, s_j in [0,1] cup (1/2 + iR), r_0 = i/2 for the constant.
- Selberg zeta Z_S(s) = prod_gamma prod_{k>=0} (1 - e^{-(s+k) l_gamma}) over primitive oriented
  closed geodesics; Ruelle zeta zeta_R(s) = prod_gamma (1 - e^{-s l_gamma}) = Z_S(s)/Z_S(s+1)
  (def:selberg-zeta). Guillemin flat trace (cit:dz-guillemin): Tr^flat e^{-tX} =
  sum_gamma T^#_gamma delta(t - T_gamma)/|det(1 - P_gamma)| over all closed orbits with repetition,
  and on transverse k-forms (Dyatlov-Zworski 1306.4203 eq:guill, lines 501-505) the same with the
  factor tr(wedge^k P_gamma) in the numerator; Lefschetz identity det(1 - P_gamma) =
  sum_k (-1)^k tr wedge^k P_gamma (lines 525-526); for a surface dim E_s = 1 so
  |det(1 - P_gamma)| = -det(1 - P_gamma) = 4 sinh^2(k l/2) (prop:poincare-jacobian).
- Notebook graded conventions (shards 02f, 02g, 02h): bond V = V_+ (+) V_-, parity P, homogeneous
  letters; doubled transfer E_d = sum_s A_s (x) conj A_s; Gamma_b = P (x) conj P; periodic ring norm
  str E_d^n; ring zeta 1/sdet(1 - u E_d) = det(1 - u E_1)/det(1 - u E_0) (zeros from the odd sector);
  divisor nu = m_0 - m_1; cMPS generator T = Q (x) 1 + 1 (x) conj Q + sum_a R_a (x) conj R_a with
  Q even, jumps homogeneous, ring norm str e^{L T}, ring zeta 1/sdet(z - T). For infinite bonds the
  divisor is the relative resonance divisor of obs:divisor-regular-data (specified regular spaces,
  meromorphic continuation, Riesz projections), never the L^2 spectrum. The graded RH / FE /
  Ramanujan / manifest (HP) definitions are def:graded-rh-fe-ramanujan; the trivial divisor is a
  signed divisor with parities; for a generator the critical line is the midpoint of the pair of
  reference rates (omega_0, omega_1).
- A "graded spectral transfer" (prover's distinction of 2026-09-15) is a graded operator with a
  divisor and no supplied Kraus realisation; a "graded CP transfer" has one.

## Drafted statements

**D1 (Letters and bond).** On SM with Haar measure, the left-invariant fields H, E, W, X, U_pm are
skew-symmetric on C^infty(SM) (right translation preserves Haar) and generate unitary groups on
L^2(SM) with skew-adjoint closures (H-AN as in notes/selberg/astra-proofs.md). Omega is central,
commutes with right translation by K, and Delta = -Omega on the K-invariant sector is a sum of
squares of letters: <f, Delta f> = (1/4)(||Hf||^2 + ||Ef||^2) for K-invariant f. Consequently
spec(Delta) subset [0, infinity) and the map s -> s(1-s) sends the divisor {s_j} into
(1/2 + iR) cup [0,1]. [Reality of the Laplace divisor is derived from the letters.]

**D2 (The Ruelle zeta is the graded ring zeta of the geodesic flow with the transverse form-degree
grading; closed geodesics are fermionic because dim E_s = 1).** Let the ring norms of the flow on
transverse k-forms be N_k(t) = Tr^flat e^{-tX}|_{k-forms}, k = 0,1,2, and grade by (-1)^k (degree
one odd). Then the periodic (graded) ring norm is
  str(t) := N_0(t) - N_1(t) + N_2(t) = sum_gamma T^#_gamma delta(t - T_gamma) det(1-P_gamma)/|det(1-P_gamma)|
           = - sum_gamma T^#_gamma delta(t - T_gamma),
the unweighted orbit comb with a global fermionic sign, and the graded ring zeta in the
notebook's convention Z_ring(s) = exp( int_0^infty e^{-st} str(t) dt/t ) equals
zeta_R(s) = Z_S(s)/Z_S(s+1) for Re s > 1, continued meromorphically. Its divisor: zeros (odd)
at s_j = 1/2 pm i r_j (j >= 0) and the topological zeros; poles (even) at s_j - 1 = -1/2 pm i r_j
and the topological poles. Trivial divisor: the zero at s = 1 (growth rate, the constant, omega_0 = 1),
its designated partner the pole at s = 0 (omega_1 = 0; critical line Re s = 1/2 = midpoint), and the
topological ladder at s in -N_0 with multiplicities from chi(M) = 2 - 2g (give them exactly). Retained
divisor: zeros {1/2 pm i r_j}_{j>=1} (odd) and poles {-1/2 pm i r_j}_{j>=1} (even). The retained odd
divisor satisfies the divisor functional equation s -> 1 - s; the retained even poles are the
E_s-shifted (m = 1 band) images of the odd zeros and lie on Re s = -1/2: state whether they should be
designated trivial (ladder-type, period images under the transverse Jacobian) or whether Z_S itself is
the better ring zeta (of the tower D_tow = prod_{j>=1} Z_S(s + j), whose zeros are all the resonances
-1/2 - k pm i r_j: the "all odd" graded spectral transfer of the flow on functions, the notebook's
prop:flat-tower). Fix the exact bookkeeping and the exact statement of the notebook's (RH), (FE),
(Ram) for this object: (Ram) for the retained odd divisor iff every nonconstant Laplace eigenvalue is
>= 1/4 (Selberg's 1/4 property).

**D3 (The manifest form on the first band is derived from the letters).** [Core.] For lambda not in
-1 - (1/2)N_0, let Res^0_X(lambda) = {u in D'(SM) : (X + lambda)u = 0, U_- u = 0} (DFG lines 595-596,
the wavefront condition being automatic). Then:
 (a) [algebra, prove in full] for u in Res^0_X(lambda): Omega u = lambda(1 + lambda) u, because
     U_- U_+ = U_+ U_- - 2X and Omega = X^2 + U_+ U_- + X... (do the computation carefully with
     Omega = X^2 + (1/2)(U_+U_- + U_-U_+)), and the fibre pushforward pi_* u(x) = int_{S_x M} u dS
     commutes with Omega (central) and lands in Eig(-lambda(1 + lambda)) subset C^infty(M).
 (b) [DFG, cite as H-DFG with the exact lines: e:pushy 599-603, e:poppy 619-621, e:peasy 631-633,
     Poisson isomorphism] pi_*: Res^0_X(lambda) -> Eig(-lambda(1+lambda)) is an isomorphism for
     lambda not in -1 - N. Do NOT reprove the analytic part; isolate exactly which statements are
     algebraic (proved here) and which are DFG's.
 (c) [derived reality] Since Delta is a sum of squares of skew-adjoint letters (D1),
     -lambda(1+lambda) in [0, infinity), hence the first-band divisor lies in {Re lambda = -1/2}
     cup [-1, 0]. The first band is on the critical line Re lambda = -1/2 except for the constant
     iff Delta >= 1/4 on 1^perp iff the COERCIVITY ||Hf||^2 + ||Ef||^2 >= ||f||^2 for all K-invariant
     f perp 1. This coercivity is the Selberg-side analogue of Hastings' bound / the Ramanujan bound
     and is NOT derived from the letters; everything else is.
 (d) [the (HP) form] G(u, v) := <pi_* u, pi_* v>_{L^2(M)} is a positive definite form on
     (+)_j Res^0_X(lambda_j) (first band, all j), transported from the Haar form by the letters;
     the flow e^{-tX} is G-normal on the first band, and e^{t/2} e^{-tX} is G-unitary on the
     retained first band iff the coercivity of (c) holds. Under coercivity this is exactly the
     manifest form (HP) of def:graded-rh-fe-ramanujan for the odd sector of D2 (or its shift), with
     the pair of reference rates (0, -1) [or (1, 0) in the s variable], and the form is derived from
     the letters (Haar) through the pushforward.
 (e) [operator-form FE] J := (pi_*|_{Res^0(-1-lambda)})^{-1} o pi_*|_{Res^0(lambda)} is an even
     similarity on the first band with J X J^{-1} = -1 - X and J G-unitary: the functional equation
     of def:graded-rh-fe-ramanujan in operator form, derived from the letters. Check the exceptional
     lambda in -1 - (1/2)N_0 and the constant.
State precisely what "derived from the letters" means as a theorem: which inputs are Haar
invariance, which are the sl2 relations, which are DFG analysis, which is the coercivity.

**D4 (Operator-level continuous Ihara-Bass).** Res_X(lambda) = (+)_{m>=0} U_+^m Res^0_X(lambda + m)
(DFG line 591) with U_-^m U_+^m = m! prod_{j=1}^m (2 lambda + m + j) on Res^0_X(lambda + m)
(line 587): the horocyclic operator U_+ is the continuum non-backtracking lift and the bands are its
ladder. The "adjacency" object is the two-jump Lindbladian of shard 09b on the multiplication
sector, T_adj M_f = M_{(2 Omega + (1/2) W^2) f} = -2 Delta on K-invariant f, with real spectrum
{-2 lambda_j} (derived from the letters, prop:lindblad-sum-of-squares, prop:casimir-laplacian). The
"Hashimoto" object is the flow drift X. The relation lambda(1 + lambda) = -sigma between a first-band
resonance lambda and a Laplace eigenvalue sigma, with roots lambda and -1 - lambda, is the continuum
Ihara quadratic mu^2 - a mu + q = 0 (roots mu, q/mu) under mu = e^{lambda}, q = e^{-1}: fixed product,
variable sum. Formulate the operator-level statement (an intertwining of the flow on the first band
with the Laplacian on M through pi_*, plus the ladder) as the continuous analogue of thm:qihara-general
and say exactly what the 09c "not established" item (operator-level compression turning D_tow into a
Laplacian determinant) becomes: proved, proved for the first band only, or still open.

**D5 (What the Kraus / transfer realisation is; regular-data divisor).** Draft: the graded transfer
of D2 is the single-copy (not doubled) graded transfer on the bond L^2(SM) (x) wedge^*(C^2) =
L^2(SM) (x) C^{2|2} (transverse exterior algebra, degrees 0 and 2 even, degree 1 odd; balanced),
with even drift Q = -X (x) 1 + 1 (x) dJ where dJ is the transverse linearised flow
(diag(+1, -1) on degree 1 for E_u^*, E_s^*; 0 on degrees 0, 2) and NO jumps; its regular-data
supertrace on C^infty (x) C^{2|2} against D' is str(t) of D2 (the C^{2|2} factor contributes
2 - 2 cosh t = -4 sinh^2(t/2) = det(1 - P_gamma) per orbit). As a doubled-bond object it is the
MULTIPLICATION SECTOR {M_f (x) omega} of Ad(e^{tQ}) on B(L^2(SM)) (x) wedge^*, invariant since
Ad(e^{-tX}) M_f = M_{e^{-tX} f}; the doubled bond's own trace would square the flow (|Tr|^2) and is
not the object. Say (i) whether this satisfies def:graded-transfer-channel / def:cmps-transfer-generators
as a CP object (single Kraus letter e^{tQ}, CP but not trace preserving; growth q = e^{1} from the
E_u^* weight; the "regular data" are the diagonal operators M_f with f in C^infty or a DFG anisotropic
space), (ii) that the odd letters demanded by prop:graded-chernoff are absent here because the parity
sits in the transverse fermionic factor and the drift is even, consistent with that proposition, and
(iii) that adding the two dissipative jumps R = sqrt(kappa) H, sqrt(kappa) E (shard 09b) produces the
adjacency on the multiplication sector (real spectrum) and destroys the critical-line divisor unless
the drift is kept: the Selberg realisation is "drift = flow (Hamiltonian letter), jumps = adjacency
letters", and the critical-line divisor is a drift phenomenon. Prove or correct (ii)-(iii) on the
multiplication sector; give the exact relation between the multiplication-sector generator with drift
and jumps and the operators X, Omega.

**D6 (Where the mechanism stops: the modular surface, the Riemann zeros).** Gamma = PSL_2(Z), one
cusp, scattering determinant phi(s) = sqrt(pi) Gamma(s - 1/2) zeta(2s - 1)/(Gamma(s) zeta(2s))
(def:scattering-determinant, cit:fjs-scattering-det). Draft: (a) the Selberg zeta of the modular
surface has zeros at s = rho/2 for every nontrivial zero rho of zeta (from the poles of phi; state
the divisor of Z_S for a one-cusp group as H-VENKOV or H-IWANIEC from your knowledge, with the
reference named and marked unverified; do not invent a citation), so in the graded transfer of D2
adapted to the non-compact surface the odd retained divisor contains {rho/2}; RH iff these lie on
Re s = 1/4, the e^{-t/4} of shard 04. (b) The D3 mechanism fails exactly there: the first-band
states at lambda = rho/2 - 1 push forward to the Eisenstein series E(z, rho/2), which is not in
L^2(M) (growth y^s + phi(s) y^{1-s}), so the Haar-transported form G is not available and the
symmetry of Delta implies nothing about rho; the mechanism covers precisely the Maass cusp forms
(discrete spectrum, Selberg's 1/4 there is the Selberg eigenvalue conjecture, open) and the constant.
(c) Draft (to prove or refute): there is no positive form on the Eisenstein first-band states
built from the Haar form and the letters (finite words in X, U_pm applied to L^2 or C^infty data)
for which e^{t/2}e^{-tX} is unitary on the {rho/2} sector; any such form must be a form on regular
or weighted data (obs:divisor-regular-data), e.g. through the Maass-Selberg relation for the
truncated Eisenstein series (write it down; say what it gives at s = rho/2 and whether Re s = 1/4
becomes a positivity statement of the form "a truncated norm is nonnegative"). No theorem is expected
beyond a precise statement of what the Selberg mechanism does and does not deliver for zeta; this
item is exploratory and should be labelled as such.

**D7 (The same mechanism in finite dimensions: graphs and the quantum Hashimoto).** For a finite
(q+1)-regular graph with Hashimoto matrix T on oriented edges and adjacency A: the edge-to-vertex
pushforward pi_*(u)(v) = sum_{e: head(e) = v} u(e) maps the mu-eigenspace of T into the
lambda-eigenspace of A with mu^2 - lambda mu + q = 0, is an isomorphism for mu not in {pm 1, pm sqrt q}
(state the exact exceptional set), and the form G = pullback of l^2(V) makes T/sqrt q G-unitary on
the retained band iff the graph is Ramanujan; A is self-adjoint because the letters (the edge
reversal / the neighbour maps) are permutations: reality from the letters, the bound is extra.
Quantum version (shard 03c): for a graded representation channel with unitary letters U_i and the
graded Hashimoto operator on B(V) (x) C^D, the pushforward sum_i (X (x) e_i) -> sum_i Ad(U_i^dagger) X
(or the correct variant: find it) intertwines the retained band of the Hashimoto operator with the
channel's eigenspaces via the Ihara quadratic, sector by sector, and the HS form pulled back makes
the retained Hashimoto band unitary iff the channel is sector-Ramanujan. Prove both and verify by
script (Petersen graph, K_4, a small LPS or PGL_2(F_5) case; the Pauli C^{1|1} example of
prop:qubit-graded-zeta) in notes/selberg-letters/finite/. This settles the notebook's open item
"a principle relating Hermitian channel plus non-backtracking lift to odd block unitary".

**D8 (K-type grading supercancels; the transverse grading is the one).** With P_K = (-1)^{m/2} on
K-types m in 2Z of L^2(SM): H and E are odd letters, W is even, the two-jump Lindbladian is even. But
on the Laplacian side the K-type grading is the form-degree (Hodge) grading of M, and
str e^{-t Delta_forms} = chi(M) = 2 - 2g (McKean-Singer): every nonzero Laplace eigenvalue cancels
between degrees, so the K-type grading of the bond produces NO net-odd divisor at the Selberg zeros.
The grading that does (D2) is the transverse form-degree grading carried by the flow's Jacobian on
wedge^*(E_s^* (+) E_u^*), and it is a grading of the transverse fermionic factor, not of the bond
L^2(SM). Prove, and correct obs:selberg-grading-choice accordingly (its last sentence proposes the
K-type grading on the doubled bond as the candidate; say precisely why that is wrong or in what
sense it survives).
