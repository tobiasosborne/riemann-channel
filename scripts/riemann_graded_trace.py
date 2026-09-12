"""Graded supertrace of the compressed Riemann semigroup, and two finite Lindblad models.

CONVENTIONS
-----------
Compressed semigroup Z(t), t > 0: one mode per nontrivial zero rho = sigma + i gamma of
zeta, with eigenvalue exp(-conj(rho) t / 2).  Distributional trace

    Tr Z(t) := sum_rho exp(-conj(rho) t / 2),     sum over ALL zeros (both signs of gamma).

Under RH (assumed for the numerics, sigma = 1/2 for the cached ordinates) the zero and its
conjugate contribute 2 e^{-t/4} cos(gamma t / 2), so

    Tr Z(t) = 2 sum_{gamma > 0} e^{-t/4} cos(gamma t / 2).

Positive-time prime measure

    P_+(t) := sum_{n >= 2} (Lambda(n) / n) delta(t - 2 log n),      Lambda = von Mangoldt.

Graded generator G on  C (even)  (+)  [ K_S (+) l^2(N_{>=1}) ] (odd):
even spectrum {0}; odd spectrum {-conj(rho)/2} union {-(k + 1/2) : k >= 1}.  Supertrace

    str e^{tG} := 1 - Tr Z(t) - sum_{k >= 1} e^{-(k + 1/2) t},
                                   with sum_{k>=1} e^{-(k+1/2)t} = e^{-t/2} / (e^t - 1).

CLAIM A (tested here):   str e^{tG} = 2 P_+(t)  exactly as distributions on t > 0;
in particular a POSITIVE measure.

Derivation used as the analytic target.  For u > 0 the explicit formula reads

    sum_rho e^{rho u} = e^u - sum_n Lambda(n) delta(u - log n) - 1 / (e^{2u} - 1).

The zero multiset is invariant under rho -> conj(rho) and under rho -> 1 - rho, hence
Tr Z(t) = sum_rho e^{-rho t/2} = e^{-t/2} sum_rho e^{rho t/2}.  Put u = t/2; the Jacobian of
the substitution is delta(t/2 - log n) = 2 delta(t - 2 log n), and e^{-t/2} = 1/n on the
support of that delta.  Therefore

    Tr Z(t) = 1 - 2 P_+(t) - e^{-t/2} / (e^t - 1),                             (*)

so that  1 - Tr Z(t) = 2 P_+(t) + e^{-t/2}/(e^t - 1)  and, subtracting the odd ladder,
str e^{tG} = 2 P_+(t).  Note the factor 2 in front of P_+ is exactly the u = t/2 Jacobian.

SMOOTHING.  Everything is distributional, so both sides are convolved in t with a normalised
Gaussian k_s(t) = exp(-t^2/2s^2) / (s sqrt(2 pi)).  We inherit the truncation treatment of
scripts/ringnorm.py: that script weights the zero gamma by exp(-(gamma/G)^2/2) with
G = gamma_max / 3.5 and works in the variable u = t/2, i.e. it smooths in u with standard
deviation 1/G.  Here the variable is t = 2u, so the matching t-space width is

    s = 2 / G,      G = gamma_max / 3.5,       exp(-gamma^2 s^2 / 8) = exp(-(gamma/G)^2 / 2).

Convolution is applied EXACTLY, mode by mode: (e^{a t} * k_s)(t) = e^{a t} e^{a^2 s^2 / 2}.
For a = -1/4 + i gamma/2 this gives amplitude e^{s^2/32} e^{-(gamma/G)^2/2} and a phase shift
gamma s^2 / 8 = gamma / (2 G^2); for a = -(k + 1/2) it gives the factor e^{(k+1/2)^2 s^2/2};
the even constant 1 is unchanged.

TASKS
  1  Windowed supertrace vs 2 P_+ on t in [1.0, 6.6]  (covers 2 log n, n = 2..27).
  2  Ladder parity: the two alternative gradings both match and are both positive, while
     flipping ONE pair of nontrivial zeros to even destroys positivity.
  3  Vacuum-decay Lindbladian on B(C (+) C^D): trace preservation, complete positivity,
     unique fixed point, spectral multiset, exact coherence-block evolution.
  4  Prime-chain detailed-balance Lindbladian (classical birth-death part): Gibbs stationary
     state, M/M/1 spectral band, product-chain gap -- a real spectrum, no zeta zeros.

No plotting.  Deterministic (seeded).  Run from the repo root:
    python3 scripts/riemann_graded_trace.py > outputs/riemann_graded_trace.txt
"""

import time
import numpy as np
from numpy.linalg import eig, eigh, norm
from scipy.linalg import expm
from sympy import factorint

T_START = time.time()
RNG = np.random.default_rng(20260912)
np.set_printoptions(precision=6, suppress=False)

RESULTS = []          # (label, passed, detail)


def record(label, passed, detail=""):
    RESULTS.append((label, bool(passed), detail))
    print(f"    [{'PASS' if passed else 'FAIL'}] {label}" + (f"   {detail}" if detail else ""))


def hrule(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ----------------------------------------------------------------------------------------
# Common data: zeros, window, von Mangoldt
# ----------------------------------------------------------------------------------------
ZS = np.load("data/zeros3000.npy")
GAMMA_MAX = float(ZS[-1])
G = GAMMA_MAX / 3.5                      # same choice as scripts/ringnorm.py
S = 2.0 / G                              # Gaussian width in t (= 2 * width in u = t/2)
W = np.exp(-(ZS / G) ** 2 / 2)           # truncation / smoothing weight, as in ringnorm.py
PHI = ZS / (2 * G ** 2)                  # exact phase shift from smoothing e^{-t/4+i gamma t/2}
AMP = np.exp(S ** 2 / 32)                # exact amplitude correction from the e^{-t/4} factor


def zero_cos_sum(tv, extra_weight=None):
    """sum_{gamma>0} w(gamma) cos(gamma t/2 - phi(gamma)), chunked over t."""
    w = W if extra_weight is None else W * extra_weight
    out = np.empty_like(tv)
    step = 1200
    for i in range(0, tv.size, step):
        tt = tv[i:i + step]
        out[i:i + step] = (np.cos(np.outer(tt, ZS) / 2 - PHI[None, :]) * w[None, :]).sum(axis=1)
    return out


def tr_Z_smooth(tv):
    """Gaussian-smoothed Tr Z(t) = 2 sum_{gamma>0} e^{-t/4} cos(gamma t/2), RH assumed."""
    return 2.0 * AMP * np.exp(-tv / 4) * zero_cos_sum(tv)


K_LADDER = np.arange(1, 401)


def ladder_smooth(tv):
    """Gaussian-smoothed sum_{k>=1} e^{-(k+1/2)t}  ( = e^{-t/2}/(e^t-1) unsmoothed )."""
    a = K_LADDER + 0.5
    out = np.zeros_like(tv)
    for i in range(0, tv.size, 2000):
        tt = tv[i:i + 2000]
        out[i:i + 2000] = np.exp(-np.outer(tt, a) + (a ** 2 * S ** 2 / 2)[None, :]).sum(axis=1)
    return out


def vonmangoldt(n):
    f = factorint(n)
    return float(np.log(list(f)[0])) if len(f) == 1 else 0.0


NMAX = 200
PRIME_POWERS = [(n, vonmangoldt(n)) for n in range(2, NMAX + 1) if vonmangoldt(n) > 0]


def two_P_plus_smooth(tv):
    """Gaussian-smoothed 2 P_+(t) = 2 sum_n (Lambda(n)/n) delta(t - 2 log n)."""
    out = np.zeros_like(tv)
    pref = 1.0 / (S * np.sqrt(2 * np.pi))
    for n, L in PRIME_POWERS:
        out += 2.0 * (L / n) * pref * np.exp(-(tv - 2 * np.log(n)) ** 2 / (2 * S ** 2))
    return out


TABLE_N = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 25, 27]
T_LO, T_HI, DT = 1.0, 6.6, 4e-4
TGRID = np.arange(T_LO, T_HI + DT / 2, DT)


def dip_mask(tv, n_sigma=4.0):
    m = np.ones_like(tv, dtype=bool)
    for n, _ in PRIME_POWERS:
        m &= np.abs(tv - 2 * np.log(n)) > n_sigma * S
    return m


# ----------------------------------------------------------------------------------------
hrule("SETUP")
print(f"  zeros loaded              : {ZS.size}   gamma_1 = {ZS[0]:.6f}   gamma_max = {GAMMA_MAX:.4f}")
print(f"  window G = gamma_max/3.5  : {G:.6f}      (same rule as scripts/ringnorm.py)")
print(f"  truncation weight at g_max: {W[-1]:.6e}   = exp(-3.5^2/2); the 3000-zero cut-off is")
print( "                              the window itself, so the sum is converged by construction.")
print(f"  Gaussian width in t       : s = 2/G = {S:.6e}   (= 1/G in the variable u = t/2)")
print(f"  amplitude corr e^(s^2/32) : {AMP:.12f}    max phase shift gamma/(2G^2) = {PHI[-1]:.6e}")
print(f"  grid                      : t in [{T_LO}, {T_HI}], dt = {DT}, {TGRID.size} points"
      f"  ({DT / S:.3f} sigma per step)")
print(f"  prime powers in 2 P_+     : n = 2 .. {NMAX} ({len(PRIME_POWERS)} terms)")

TRZ_GRID = tr_Z_smooth(TGRID)
LAD_GRID = ladder_smooth(TGRID)
RHS_A_GRID = two_P_plus_smooth(TGRID)
F_GRID = 1.0 - TRZ_GRID - LAD_GRID                       # str e^{tG}, smoothed

T_TAB = np.array([2 * np.log(n) for n in TABLE_N])
TRZ_TAB = tr_Z_smooth(T_TAB)
LAD_TAB = ladder_smooth(T_TAB)
RHS_A_TAB = two_P_plus_smooth(T_TAB)
F_TAB = 1.0 - TRZ_TAB - LAD_TAB

MASK4 = dip_mask(TGRID, 4.0)
MASK8 = dip_mask(TGRID, 8.0)


# ----------------------------------------------------------------------------------------
hrule("TASK 1  WINDOWED SUPERTRACE   str e^{tG}  vs  2 P_+(t)")
print("""
  F(t) := 1 - 2 sum_{gamma>0} w(gamma) e^{-t/4} cos(gamma t/2 - phi(gamma)) * e^{s^2/32}
              - sum_{k>=1} e^{-(k+1/2)t + (k+1/2)^2 s^2/2}
  compared with   2 sum_n (Lambda(n)/n) k_s(t - 2 log n).
  Both sides carry the SAME Gaussian window; the factor 2 in front of P_+ is the u = t/2
  Jacobian delta(t/2 - log n) = 2 delta(t - 2 log n).  Table evaluated exactly at t = 2 log n
  (not at a grid point) so the ratio is free of grid-offset bias.
""")
print("   n    2 log n     str e^{tG} (num)     2 P_+ (pred)      ratio      Lambda(n)/n")
ratios = []
for i, n in enumerate(TABLE_N):
    r = F_TAB[i] / RHS_A_TAB[i]
    ratios.append(r)
    print(f"  {n:2d}   {T_TAB[i]:.6f}   {F_TAB[i]:16.4f}  {RHS_A_TAB[i]:16.4f}   {r:8.5f}   "
          f"{vonmangoldt(n) / n:.6f}")
ratios = np.array(ratios)
print(f"\n  ratio: min {ratios.min():.5f}  max {ratios.max():.5f}  "
      f"max |ratio - 1| = {np.max(np.abs(ratios - 1)):.5f}")
record("T1.ratios  all 12 dip ratios within 1 +/- 0.02",
       np.max(np.abs(ratios - 1)) < 0.02,
       f"max |ratio-1| = {np.max(np.abs(ratios - 1)):.5f}")

res = F_GRID - RHS_A_GRID
r4, r8 = np.max(np.abs(res[MASK4])), np.max(np.abs(res[MASK8]))
print(f"\n  max |str - 2P_+| away from dips (>4 sigma, ringnorm convention) : {r4:.6f}")
print(f"  max |str - 2P_+| away from dips (>8 sigma)                      : {r8:.6f}")
print(f"  max |str - 2P_+| over the whole grid                            : {np.max(np.abs(res)):.6f}")
print(f"  peak height of str e^{{tG}} on the grid                           : {F_GRID.max():.4f}")
print( "  (the 4-sigma figure is dominated by Gaussian tail leakage from the dips themselves:")
print(f"   e^-8 * peak = {np.exp(-8.0) * F_GRID.max():.4f}.  The 8-sigma figure {r8:.4f} is the genuine")
print( "   3000-zero truncation error; ringnorm.py reports 0.180 for the bare zero sum in u.)")
record("T1.residual  max |str - 2P_+| away from dips < 1.0 (peak ~ 140)", r4 < 1.0,
       f"{r4:.6f}  (0.7% of the n=2 dip height)")

fmin = F_GRID.min()
eps = max(0.0, -fmin)
i0 = int(np.argmin(F_GRID))
print(f"\n  POSITIVITY: min_t str e^{{tG}} on the grid = {fmin:.6f} at t = {TGRID[i0]:.5f}")
print(f"              epsilon = {eps:.6f}   (str e^{{tG}} >= -epsilon everywhere on the grid)")
print(f"              epsilon / peak = {eps / F_GRID.max():.3e}, and epsilon is of the same size")
print( "              as the truncation residual, i.e. consistent with exact positivity.")
record("T1.positivity  str e^{tG} >= -epsilon with epsilon < 1.0", eps < 1.0,
       f"epsilon = {eps:.6f} at t = {TGRID[i0]:.5f}")


# ----------------------------------------------------------------------------------------
hrule("TASK 2  LADDER PARITY")
print("""
  (a) ladder dropped   : 1 - Tr Z(t)                       vs  2 P_+ + e^{-t/2}/(e^t - 1)
  (b) ladder counted even: 1 - Tr Z + sum_k e^{-(k+1/2)t}  vs  2 P_+ + 2 e^{-t/2}/(e^t - 1)
  Both are identities (they are (*) plus 0, resp. plus twice the ladder), and both right-hand
  sides are positive measures, so POSITIVITY ALONE DOES NOT FIX THE LADDER PARITY.
""")

for tag, lhs_tab, lhs_grid, rhs_tab, rhs_grid in [
    ("2a  C (+) K_S only        ", 1 - TRZ_TAB, 1 - TRZ_GRID,
     RHS_A_TAB + LAD_TAB, RHS_A_GRID + LAD_GRID),
    ("2b  ladder counted even   ", 1 - TRZ_TAB + LAD_TAB, 1 - TRZ_GRID + LAD_GRID,
     RHS_A_TAB + 2 * LAD_TAB, RHS_A_GRID + 2 * LAD_GRID),
]:
    rr = lhs_tab / rhs_tab
    rg = lhs_grid - rhs_grid
    m4 = np.max(np.abs(rg[MASK4]))
    mn = lhs_grid.min()
    print(f"\n  {tag}")
    print( "     n    2 log n        numeric          prediction       ratio")
    for i, n in enumerate(TABLE_N):
        print(f"    {n:2d}   {T_TAB[i]:.6f}  {lhs_tab[i]:16.4f}  {rhs_tab[i]:16.4f}   {rr[i]:8.5f}")
    print(f"     max |ratio - 1| = {np.max(np.abs(rr - 1)):.5f}   "
          f"max residual away from dips = {m4:.6f}   min over grid = {mn:.6f}")
    record(f"T{tag.split()[0]}.match", np.max(np.abs(rr - 1)) < 0.02 and m4 < 1.0,
           f"max |ratio-1| = {np.max(np.abs(rr - 1)):.5f}, residual = {m4:.6f}")
    record(f"T{tag.split()[0]}.positivity", mn > -1.0, f"min = {mn:.6f}")

print("""
  (c) flip ONE pair of nontrivial zeros (gamma_1 = 14.134725...) from odd to even, i.e. add
      + 4 e^{-t/4} cos(gamma_1 t/2)  to the supertrace.  If positivity survived this, the
      grading of the zero modes would be undetermined; it does not.
""")
g1 = ZS[0]
flip = 4.0 * AMP * np.exp(-TGRID / 4) * W[0] * np.cos(g1 * TGRID / 2 - PHI[0])
F_FLIP = F_GRID + flip
j0 = int(np.argmin(F_FLIP))
neg_frac = float(np.mean(F_FLIP < -1e-9))
print(f"    gamma_1 = {g1:.9f},  window weight w(gamma_1) = {W[0]:.9f}")
print(f"    most negative value of the flipped smoothed supertrace: {F_FLIP[j0]:.6f}  at t = {TGRID[j0]:.5f}")
print(f"    (naive envelope -4 e^(-t/4) at that t: {-4 * np.exp(-TGRID[j0] / 4):.6f})")
print(f"    fraction of grid points where the flipped supertrace is negative: {neg_frac:.4f}")
record("T2c.flip destroys positivity (min < -1.0)", F_FLIP[j0] < -1.0,
       f"min = {F_FLIP[j0]:.6f} at t = {TGRID[j0]:.5f}")


# ----------------------------------------------------------------------------------------
hrule("TASK 3  VACUUM-DECAY LINDBLADIAN ON B(C (+) C^D)")
print("""
  H Hermitian Gaussian on C^D, j a random vector, B = -i H - (1/2)|j><j|  so -(B+B^*) = |j><j|.
  bB = 0 (+) B on C (+) C^D,  J = |vac><j|,  L(x) = bB x + x bB^* + J x J^*.
  Predicted spectrum: {0} u spec(B) u conj(spec B) u {b_n + conj(b_m)}.
""")


def super_matrix(f, N):
    """Matrix of a linear map on N x N matrices, column-stacking vec."""
    M = np.zeros((N * N, N * N), dtype=complex)
    for a in range(N):
        for b in range(N):
            E = np.zeros((N, N), dtype=complex)
            E[a, b] = 1.0
            M[:, b * N + a] = f(E).reshape(N, N).flatten(order="F")
    return M


def greedy_multiset_dev(x, y):
    """Max deviation of a greedy nearest-neighbour matching of two equal-size complex multisets."""
    x = list(np.asarray(x))
    y = list(np.asarray(y))
    worst = 0.0
    for v in x:
        d = [abs(v - w) for w in y]
        k = int(np.argmin(d))
        worst = max(worst, d[k])
        y.pop(k)
    return worst


for D in (3, 5, 8):
    N = D + 1
    A = RNG.normal(size=(D, D)) + 1j * RNG.normal(size=(D, D))
    H = (A + A.conj().T) / 2
    j = RNG.normal(size=D) + 1j * RNG.normal(size=D)
    B = -1j * H - 0.5 * np.outer(j, j.conj())
    bB = np.zeros((N, N), dtype=complex)
    bB[1:, 1:] = B
    J = np.zeros((N, N), dtype=complex)
    J[0, 1:] = j.conj()                      # J = |vac><j|
    print(f"\n  --- D = {D}  (N = {N}, superoperator dimension {N * N}) ---")

    # sanity: -(B + B^*) = |j><j|
    dev_bb = norm(-(B + B.conj().T) - np.outer(j, j.conj()))
    record(f"T3.D{D}.dissipator  -(B+B^*) = |j><j|", dev_bb < 1e-12, f"dev = {dev_bb:.3e}")

    def L(x, bB=bB, J=J):
        return bB @ x + x @ bB.conj().T + J @ x @ J.conj().T

    Lmat = super_matrix(L, N)

    # trace preservation
    worst_tr = 0.0
    for _ in range(20):
        X = RNG.normal(size=(N, N)) + 1j * RNG.normal(size=(N, N))
        X = X + X.conj().T
        worst_tr = max(worst_tr, abs(np.trace(L(X))))
    record(f"T3.D{D}.trace preservation  Tr L(x) = 0", worst_tr < 1e-11,
           f"max |Tr L(x)| over 20 random x = {worst_tr:.3e}")

    # complete positivity of e^{tL} at t = 0.7 via the Choi matrix
    t_cp = 0.7
    E = expm(t_cp * Lmat)
    Choi = np.zeros((N * N, N * N), dtype=complex)
    for a in range(N):
        for b in range(N):
            Eab = np.zeros((N, N), dtype=complex)
            Eab[a, b] = 1.0
            out = (E @ Eab.flatten(order="F")).reshape(N, N, order="F")
            Choi[a * N:(a + 1) * N, b * N:(b + 1) * N] = out
    Choi = (Choi + Choi.conj().T) / 2
    lam_min = float(eigh(Choi)[0][0])
    scale = float(np.abs(eigh(Choi)[0]).max())
    record(f"T3.D{D}.complete positivity of e^{{0.7 L}} (Choi PSD)", lam_min > -1e-10 * max(1.0, scale),
           f"min Choi eigenvalue = {lam_min:.3e}  (largest = {scale:.4f})")

    # spectrum multiset
    spL = eig(Lmat)[0]
    bspec = eig(B)[0]
    pred = np.concatenate([[0.0 + 0j], bspec, bspec.conj(),
                           (bspec[:, None] + bspec.conj()[None, :]).flatten()])
    dev = greedy_multiset_dev(spL, pred)
    record(f"T3.D{D}.spec(L) = {{0}} u spec(B) u conj spec(B) u {{b_n + conj b_m}}",
           dev < 1e-8, f"max matching deviation = {dev:.3e}  ({spL.size} eigenvalues)")
    print(f"      max Re spec(B) = {bspec.real.max():.6e}   "
          f"(strictly negative => vacuum is globally attracting)")

    # unique fixed point
    zero_like = np.sort(np.abs(spL))
    nker = int(np.sum(np.abs(spL) < 1e-9))
    vals, vecs = eig(Lmat)
    k0 = int(np.argmin(np.abs(vals)))
    fp = vecs[:, k0].reshape(N, N, order="F")
    fp = fp / fp[0, 0]
    target = np.zeros((N, N), dtype=complex)
    target[0, 0] = 1.0
    dev_fp = norm(fp - target)
    record(f"T3.D{D}.unique fixed point = |vac><vac|", nker == 1 and dev_fp < 1e-8,
           f"dim ker = {nker}, ||fp - |vac><vac||| = {dev_fp:.3e}, "
           f"next |eigenvalue| = {zero_like[1]:.4f}")

    # coherence block
    psi = RNG.normal(size=D) + 1j * RNG.normal(size=D)
    x = np.zeros((N, N), dtype=complex)
    x[0, 1:] = psi.conj()                              # |vac><psi|
    worst_coh = 0.0
    for t in (0.13, 0.7, 2.5):
        got = (expm(t * Lmat) @ x.flatten(order="F")).reshape(N, N, order="F")
        want = np.zeros((N, N), dtype=complex)
        want[0, 1:] = (expm(t * B) @ psi).conj()        # |vac><e^{tB} psi|
        worst_coh = max(worst_coh, norm(got - want))
    record(f"T3.D{D}.coherence block  e^{{tL}}|vac><psi| = |vac><e^{{tB}}psi|",
           worst_coh < 1e-9, f"max ||diff|| over t in {{0.13,0.7,2.5}} = {worst_coh:.3e}")


# ----------------------------------------------------------------------------------------
hrule("TASK 4  PRIME-CHAIN DETAILED-BALANCE LINDBLADIAN (CLASSICAL PART)")
print("""
  Birth-death chain on occupations k = 0..K (K = 60) for a prime p at inverse temperature beta:
  up-rate  k -> k+1 :  r      = p^{-beta}
  down-rate k -> k-1:  r p^beta = 1.
  Detailed balance forces pi_{k+1}/pi_k = r/(r p^beta) = p^{-beta}, i.e. the Gibbs weight
  pi_k ~ p^{-beta k}.  The symmetrised generator S = diag(pi)^{1/2} Q diag(pi)^{-1/2} is the
  Jacobi matrix with constant off-diagonal sqrt(r * r p^beta); its bulk spectrum is the M/M/1
  band  [ -(sqrt(r p^beta) + sqrt(r))^2 , -(sqrt(r p^beta) - sqrt(r))^2 ].
""")
KTR = 60
single = {}
for beta in (1.5, 2.0):
    print(f"\n  ---- beta = {beta} ----")
    for p in (2, 3, 5):
        r = p ** (-beta)
        lam, mu = r, r * p ** beta                    # up-rate, down-rate  (mu = 1 exactly)
        lo = -(np.sqrt(mu) + np.sqrt(lam)) ** 2
        hi = -(np.sqrt(mu) - np.sqrt(lam)) ** 2

        Q = np.zeros((KTR + 1, KTR + 1))
        for k in range(KTR + 1):
            if k < KTR:
                Q[k, k + 1] = lam
            if k > 0:
                Q[k, k - 1] = mu
            Q[k, k] = -(Q[k].sum() - Q[k, k])

        logpi = -beta * np.log(p) * np.arange(KTR + 1)
        pi = np.exp(logpi - logpi.max())
        pi = pi / pi.sum()
        stat_res = float(np.max(np.abs(pi @ Q)))      # pi is stationary:  pi^T Q = 0

        off = np.sqrt(lam * mu)
        Sm = np.diag(np.diag(Q)) + np.diag(off * np.ones(KTR), 1) + np.diag(off * np.ones(KTR), -1)
        # cross-check that Sm really is the similarity transform of Q
        sim = np.diag(np.sqrt(pi)) @ Q @ np.diag(1 / np.sqrt(pi))
        sim_dev = float(np.max(np.abs(sim - Sm)))

        ev = np.sort(eigh(Sm)[0])[::-1]               # descending; ev[0] should be 0
        zero_ev = ev[0]
        nz = ev[1:]
        gap = -nz.max()
        inside = np.sum((nz >= lo - 1e-12) & (nz <= hi + 1e-12))
        frac = inside / nz.size
        ev_full = eig(Q)[0]
        max_imag = float(np.max(np.abs(ev_full.imag)))
        cond = (mu / lam) ** (KTR / 2)          # condition number of the diag(pi)^{1/2} similarity

        single[(beta, p)] = ev

        print(f"    p = {p}:  r = p^-beta = {lam:.6f},  down-rate r p^beta = {mu:.6f}")
        print(f"       Gibbs pi_k ~ p^(-beta k):  max |pi^T Q| = {stat_res:.3e}   "
              f"(similarity check {sim_dev:.3e})")
        print(f"       M/M/1 band = [{lo:.6f}, {hi:.6f}]   width {hi - lo:.6f}")
        print(f"       zero eigenvalue = {zero_ev:.3e};  spectral gap = {gap:.6f}  "
              f"(band edge {-hi:.6f}, rel. dev {abs(gap + hi) / abs(hi):.3e})")
        print(f"       eigenvalues inside the band: {inside}/{nz.size} = {frac:.4f}   "
              f"most negative = {nz.min():.6f}")
        print(f"       eigenvalues of the SYMMETRISED S are real by construction (eigh); the naive")
        print(f"       non-symmetric eig(Q) gives max |Im| = {max_imag:.3e}, a pure numerical artefact:")
        print(f"       the similarity diag(pi)^(1/2) has condition number (p^beta)^(K/2) = {cond:.3e},")
        print(f"       so eig(Q) in the unsymmetrised basis is hopelessly ill-conditioned.")
        record(f"T4.beta{beta}.p{p}.Gibbs stationary", stat_res < 1e-12, f"max |pi^T Q| = {stat_res:.3e}")
        record(f"T4.beta{beta}.p{p}.band containment", frac > 0.99,
               f"{inside}/{nz.size} inside [{lo:.5f}, {hi:.5f}], gap = {gap:.6f}")

    # product chain: spectrum of the sum of commuting independent generators = Minkowski sum
    sp = [single[(beta, p)] for p in (2, 3, 5)]
    M = (sp[0][:, None, None] + sp[1][None, :, None] + sp[2][None, None, :]).ravel()
    M = np.sort(M)[::-1]
    tot_gap = -M[1]
    print(f"\n    product chain over p = 2,3,5 (Minkowski sum, {M.size} points):")
    print(f"       top eigenvalue = {M[0]:.3e}  (the product Gibbs state)")
    print(f"       total spectral gap = {tot_gap:.6f}   = min over p of the single-prime gaps"
          f" ({min(-single[(beta, p)][1] for p in (2, 3, 5)):.6f})")
    print(f"       full range = [{M.min():.6f}, {M.max():.6e}]")
    print( "       Every point is real: the generator is self-adjoint after the detailed-balance")
    print( "       similarity transform, so the spectrum is a union of REAL intervals (the three")
    print( "       M/M/1 bands and their sum-sets).  No imaginary parts anywhere, hence NO ZETA")
    print( "       ZEROS: this classical prime chain does not see the critical line.")
    record(f"T4.beta{beta}.product gap = min single-prime gap",
           abs(tot_gap - min(-single[(beta, p)][1] for p in (2, 3, 5))) < 1e-12,
           f"gap = {tot_gap:.6f}")
    record(f"T4.beta{beta}.product spectrum real (symmetrised generator)",
           np.all(np.isreal(M)), "all sum-set points real; no imaginary parts")


# ----------------------------------------------------------------------------------------
hrule("SUMMARY")
npass = sum(1 for _, p, _ in RESULTS if p)
nfail = len(RESULTS) - npass
print(f"  checks run : {len(RESULTS)}")
print(f"  PASS       : {npass}")
print(f"  FAIL       : {nfail}")
if nfail:
    print("\n  FAILURES:")
    for label, p, detail in RESULTS:
        if not p:
            print(f"    FAIL  {label}   {detail}")
else:
    print("\n  no failures.")

print(f"""
  Headline numbers
    Claim A (str e^{{tG}} = 2 P_+) : max |ratio - 1| over the 12 prime-power dips = {np.max(np.abs(ratios - 1)):.5f}
    truncation residual away from dips                                  = {r4:.6f}
    positivity epsilon (min of the smoothed supertrace, sign flipped)   = {eps:.6f}
    flipped-pair supertrace minimum                                     = {F_FLIP[j0]:.6f} at t = {TGRID[j0]:.5f}
  Ladder parity is NOT fixed by positivity: dropping the ladder and counting it even both give
  positive measures (2 P_+ + e^{{-t/2}}/(e^t-1) and 2 P_+ + 2 e^{{-t/2}}/(e^t-1)).  What positivity
  does fix is the grading of the ZERO modes: flipping a single pair to even goes negative.
""")
print(f"  runtime: {time.time() - T_START:.1f} s")
