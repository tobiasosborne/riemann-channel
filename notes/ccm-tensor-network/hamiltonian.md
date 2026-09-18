# The nullvector and Hamiltonians

Author: codex:gpt-6 (root). Initial status SKETCH, pending adversarial review.
User steering: "perhaps the nullvector is related to a hamiltonian".

The word Hamiltonian has at least three concrete meanings here. They act on
different spaces and have different zero vectors.

## prop:ccm-tn-clock-hamiltonian

ASSUME E acts on a nonzero space of dimension d>=1 and is unitary for a positive retained-space metric G; let F map a
length coefficient vector c to sum c_j E^j, with the G-HS operator inner
product, and W=F^*F. Let v_j=vec(G^(1/2) E^j G^(-1/2)). Put

    Omega = sum_{j=0}^{K-1} |j> tensor conjugate(v_j).

PROVE: (a) W is a positive clock Hamiltonian; its zero-energy states are
exactly the polynomial relations in the selected window. (b) Its kernel
projector P is a parent constraint for Omega: (P tensor I)Omega=0.
The normalised clock density is W/(K d), so P is supported on its zero
eigenspace, whereas W itself generally does NOT annihilate Omega.

<1>1. For any c, <c,Wc>=||Fc||^2. Thus W>=0 and Wc=0 iff Fc=0. This is
the Gram identity, not an inference from individual positive ring norms.

<1>2. The (j,k) matrix entry of Tr_feature |Omega><Omega| is
<conjugate(v_k),conjugate(v_j)>=<v_j,v_k>=W_jk. Also ||Omega||^2=K d,
since E is G-unitary and ||E^j||^2_HS,G=d for every j. This proves the
density formula and fixes the complex-conjugation convention.

<1>3. The squared norm of (P tensor I)Omega is Tr(PW)=0. Hence it
vanishes. Conversely any positive clock h obeys (h tensor I)Omega=0
iff h annihilates the range of W: taking a square root of h or a Schmidt
decomposition proves both directions. For a one-dimensional radical,
P=|xi><xi|/<xi,xi>. This is a parent constraint on a length register,
not a local parent Hamiltonian on the physical sites of the original MPS.

<1>4. At a full-rank window W has no zero-energy state and P=0. Subtracting
epsilon=lambda_min(W) gives a different positive clock Hamiltonian
T=W-epsilon I with a ground vector. It does not turn that vector into an
exact polynomial relation of the original E: if ||xi||=1 then
||Fxi||^2=epsilon. One can purify T as a new feature state, but its features
need not be the original powers of E. In the Loewner setting replace W
by Q_N; the same finite linear algebra applies without claiming a power
feature representation for the unshifted Q_N.

## prop:ccm-tn-history-hamiltonian

ASSUME the setting above with K>=2. On the conjugate HS feature space,
let V be the conjugate of left multiplication by the unitary
G^(1/2) E G^(-1/2); thus V conjugate(v_j)=conjugate(v_{j+1}).
Let L_j=(<j+1| tensor I)-(<j| tensor V) for j=0,...,K-2, and define

    H_prop = sum_j L_j^* L_j.

PROVE: H_prop>=0 and Omega is a zero-energy history state. The zero
space consists exactly of sum_j |j> tensor V^j w for arbitrary w.
It has dimension d^2, and the first positive eigenvalue is
2-2 cos(pi/K). Pinning the initial feature to conjugate(vec(I))/sqrt(d)
by a positive boundary projector makes this ground state unique.

<1>1. A term has the explicit tensor form

    (|j><j|+|j+1><j+1|) tensor I
    - |j+1><j| tensor V - |j><j+1| tensor V^*.

Expansion of L_j^*L_j uses V^*V=I and proves the displayed formula.
Each term is positive and acts between adjacent clock values.

<1>2. For psi=sum |j> tensor w_j, L_j psi=w_{j+1}-Vw_j. Since the
terms are positive, H_prop psi=0 iff all these expressions vanish.
Recursion gives w_j=V^j w_0. Taking w_0=conjugate(vec(I)) yields Omega.

<1>3. The controlled unitary B=sum |j><j| tensor V^j conjugates
H_prop to the path-graph Laplacian on K vertices tensor I. Directly,
the diagonal terms are fixed and B^*(|j+1><j| tensor V)B is
|j+1><j| tensor I. The path Laplacian has eigenvalues
2-2 cos(ell pi/K), ell=0,...,K-1, as verified by the cosine vectors
w_j=cos((j+1/2)ell pi/K) and the endpoint equations. This establishes
the stated dimension and gap.

<1>4. Add |0><0| tensor (I-|w_*><w_*|), w_*=conjugate(vec(I))/sqrt(d).
It is positive. A vector has zero energy for the sum iff it obeys all
propagation equations and w_0 belongs to C w_*. This leaves precisely
one ground-state line, spanned by Omega. No gap for the pinned sum is
asserted here.

<1>5. This is nearest-neighbour locality in the length clock. V can be
a dense operator on the retained feature space. Neither a local physical
MPS Hamiltonian nor physical-site locality follows. This construction
requires E and its unitarising metric, or a supplied canonical moment
realisation; it does not construct the missing arithmetic bond from
positivity alone.

## Distinguishing the reconstructed Hamiltonian

Under CCM's even-simple hypotheses, T=Q_N-epsilon I is a positive
Hamiltonian on the Fourier coefficient space and Txi=0. The operator D''
is another Hamiltonian (self-adjoint frequency operator) on the T-metric
quotient. D'xi=0 makes the quotient possible; the xi direction is removed
there. Thus xi is not a physical zero-frequency mode of D''. In particular,
this does not solve the central-zero problem of the elliptic-curve tests.

If an exact kernel polynomial p satisfies p(E)=0, taking p(E)^*p(E)
produces the identically zero operator, not a recovered nontrivial Hamiltonian.
The useful Hamiltonians act on length coefficients or on a clock with its
feature space, not by calling an annihilating polynomial of E its generator.
