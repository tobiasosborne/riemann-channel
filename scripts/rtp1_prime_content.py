#!/usr/bin/env python3
"""rtp1_prime_content.py -- lane A2 of RTP-1 (`notes/rtp-round-1/brief.md`): the prime-content channel.

Author line: claude:opus.  Lane file: `notes/rtp-round-1/lane-A2.md`.  Output:
`outputs/rtp1_prime_content.txt` (run from the repository root:
`python3 scripts/rtp1_prime_content.py > outputs/rtp1_prime_content.txt 2>&1`).
Deterministic (seed 20260924; the seed is set but nothing below is random), no timestamps,
no memory addresses.  Every claim is an assertion through the single helper `check(cond, msg)`,
which counts, prints one line and never aborts.

================================================================================
CONVENTIONS (brief, section "Conventions"; Connes-Consani-Moscovici, refs/src/2511.22755/mc2arXiv.tex)
================================================================================
Log coordinate y = log u on R_+^x, Lebesgue measure dy = d*u.  For test functions f, g
  (f^* * g)(y) = int conj(f(x - y)) g(x) dx,        QW(f, g) = Psi(f^* * g),
  Psi(F) = W_{0,2}(F) - W_R(F) - sum_p W_p(F)                    (eq. `bombtest`, l.385-388)
with, for F on R (F-normalisation of l.366-383, F(u) = u^{1/2} f(u)):
  W_{0,2}(F) = Fhat(i/2) + Fhat(-i/2) = int F(y) 2 cosh(y/2) dy,       Fhat(t) = int F(y) e^{-ity} dy
  W_p(F)     = log p sum_{m>=1} p^{-m/2} (F(m log p) + F(-m log p))
  W_R(F)     = (log 4 pi + gamma) F(0) + int_0^oo (F(y) + F(-y) - 2 e^{-y/2} F(0)) rho(y) dy,
               rho(y) = e^{y/2} / (e^y - e^{-y}).
Psi only sees q(y) = F(y) + F(-y), y >= 0 (the even part; the paper's q(f, g), eq. `qfg`).
The general implementation `psi_general` below evaluates exactly these three definitions by
quadrature for any q given as a callable; it is the implementation that must reproduce zst's
(a_n, b_n) on the Fourier basis V_n (brief A2.2(iii)); Section 1 does that first.

TEST CLASS (brief A2.1).  phi_delta(x) = exp(-1/(1 - (x/delta)^2)) on |x| < delta, phi_1 the
delta = 1 bump; for S = {p_1 < ... < p_r} and the box Lambda_S(A) = {0..A}^r,
  phi_alpha(x) = phi_delta(x - t_alpha),   t_alpha = sum_p a_p log p,   n_alpha = prod p^{a_p}.
Then phi_alpha^* * phi_beta = R_delta(. - D'), D' = t_beta - t_alpha = log(n_beta / n_alpha),
R_delta(s) = int phi_delta(x - s) phi_delta(x) dx = delta R_1(s / delta) (autocorrelation,
supported in |s| < 2 delta).  Everything depends only on D = |D'|:
  pole  = 2 cosh(D/2) c_delta^2,               c_delta = int phi_delta e^{x/2} = delta int phi_1(t) e^{delta t/2} dt
  prime = sum_k Lambda(k) k^{-1/2} [R_delta(log k - D) + R_delta(log k + D)]   (all prime powers k)
  arch  (D > 2 delta) = int int phi_delta(x) phi_delta(w) rho(D + x - w) dx dw
                      = sum_{j even} rho_j(D) delta^{j+2} Mt_j,   rho_j = rho^{(j)}(D)/j!,
                        Mt_j = int int phi_1 phi_1 (x - w)^j = sum_{i even} C(j,i) mu_i mu_{j-i},
                        mu_i = int phi_1 t^i dt;  Cauchy tail bound on |y - D| = (D + 2 delta)/2.
  arch  (D = 0)       = delta [ (log 4 pi + gamma - log 2) R_1(0) + T_1 + R_1(0) log delta
                                + sum_j r_j delta^{j+1} At_j ],
                        T_1 = int_0^2 (R_1(s) - R_1(0))/s ds + R_1(0) log 2,
                        At_j = int R_1(u) |u|^j du,  r_j = Taylor coefficients at 0 of
                        rho_reg(y) = rho(y) - 1/(2y) (analytic for |y| < pi); Cauchy tail on |y| = 3.
  G_{alpha beta} = pole - arch - prime.   (Derivation of the D = 0 formula in the lane file.)
The Gram matrix is reported normalised by ||phi_delta||^2 = R_delta(0) = delta R_1(0) (the
translates are pairwise disjointly supported, so G/||phi||^2 is QW on an orthonormal family).

ADMISSIBILITY.  delta_max(S, A) = (1/2) min over lattice ratios r = n_beta/n_alpha >= 1 and prime
powers k != r of |log k - log r| (r = 1 included, giving log 2).  For delta < delta_max the prime
term of an entry is nonzero iff r is a prime power, and then equals log p p^{-j/2} R_delta(0).

PRECISION (brief A2.5).  python-flint (arb balls) at 200 bits.  CERTIFIED: mu_i, R_1(0), R_1(s),
c_delta (arb integrals on [-1 + eps, 1 - eps] plus the rigorous bound eps * phi_1(1 - eps) for
the omitted ends), pole and prime terms, the off-diagonal archimedean term (Taylor series with a
Cauchy tail bound), the Taylor coefficients of rho, and the eigenvalue enclosures relative to the
entry balls (residual bound + ball LDL^T inertia).  NOT CERTIFIED: the two families of constants
T_1 and At_j (odd j) of the diagonal archimedean term, obtained by tanh-sinh quadrature (levels
h = 1/64 and 1/128) over certified ball values of R_1 at the nodes; their balls carry 10 x the
level-doubling difference.  They enter only the diagonal, which is the same number for every
entry of every Gram matrix at fixed delta: a multiple of the identity, so it moves no
eigenvector and no gap between two forms at the same delta.  The consistency check (Section 1)
uses mpmath quad at 60 digits with its error estimates.

ZEROS.  Zeros of zeta appear only in Section 7, the labelled comparison step (brief A2.4, game
rule 2); acb.zeta_zeros (arb, certified) is called there and nowhere else.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")

import bisect
import inspect
import itertools
import math
import random
import subprocess
import tempfile
from decimal import Decimal
from fractions import Fraction

import numpy as np
import mpmath as mp
from flint import arb, acb, arb_mat, arb_series, ctx

SEED = 20260924
random.seed(SEED)
np.random.seed(SEED)
PREC = 200
ctx.prec = PREC
ctx.cap = 1000                                  # power-series length (arb_series); default 10 would truncate
mp.mp.dps = 60
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# the single assertion helper
# ---------------------------------------------------------------------------
_PASS = 0
_FAIL = 0
_FAILED = []


def check(cond, msg):
    """The single assertion helper: counts, prints one line, never aborts."""
    global _PASS, _FAIL
    line = inspect.currentframe().f_back.f_lineno
    ok = bool(cond)
    if ok:
        _PASS += 1
    else:
        _FAIL += 1
        _FAILED.append((line, msg))
    print(f"  {'ok  ' if ok else 'FAIL'} [L{line:4d}]  {msg}")
    return ok


def head(msg):
    print()
    print("=" * 100)
    print(msg)
    print("=" * 100)


def fm(a, d=12):
    """midpoint of an arb ball, d significant digits"""
    return a.mid().str(d, radius=False)


def fr(a):
    """radius of an arb ball"""
    return "%.1e" % float(a.rad())


def fb(a, d=12):
    return f"{fm(a, d)} (+/- {fr(a)})"


def ff(a):
    return float(a.mid())


def mpf_of(a):
    return mp.mpf(a.mid().str(70, radius=False))


def arb_of_mpf(x):
    return arb(mp.nstr(x, 70))


def sci(x, d=3):
    return ("%." + str(d) + "e") % float(x)


LOG2 = arb(2).log()
PI = arb.pi()
EULER = arb.const_euler()

# ===========================================================================
# prime powers
# ===========================================================================
XMAX = 1_100_000


def _prime_powers(X):
    s = bytearray([1]) * (X + 1)
    s[0] = s[1] = 0
    for i in range(2, int(X ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    base = {}
    for p in range(2, X + 1):
        if s[p]:
            k = p
            while k <= X:
                base[k] = p
                k *= p
    return base


PP_BASE = _prime_powers(XMAX)          # k -> p for every prime power k <= XMAX
PP_SORTED = sorted(PP_BASE)
PP_LOGF = [math.log(k) for k in PP_SORTED]


def log_frac(r):
    return arb(r.numerator).log() - arb(r.denominator).log()


# ===========================================================================
# GENERAL Weil functional Psi(q) by quadrature (mpmath), used for the zst check and cross-checks
# ===========================================================================
def mp_rho(y):
    return mp.exp(y / 2) / (2 * mp.sinh(y))


def psi_general(q, Y, breaks=()):
    """Psi(F) for F with q(y) = F(y) + F(-y) supported in [0, Y]; q a callable on mpf.
    Returns (value, parts, quad_error_estimate).  Direct transcription of the definitions:
      pole  = int_0^Y q(y) 2 cosh(y/2) dy
      arch  = (log 4pi + gamma) q(0)/2 + int_0^Y (q(y) - e^{-y/2} q(0)) rho(y) dy + (q(0)/2) log tanh(Y/2)
              (the last term is int_Y^oo of -e^{-y/2} q(0) rho = -q(0)/(2 sinh y))
      prime = sum over ALL prime powers k <= e^Y of Lambda(k) k^{-1/2} q(log k)."""
    pts = sorted(set([mp.mpf(0)] + [mp.mpf(b) for b in breaks if 0 < b < Y] + [mp.mpf(Y)]))
    pole, e1 = mp.quad(lambda y: q(y) * 2 * mp.cosh(y / 2), pts, error=True)
    q0 = q(mp.mpf(0))

    def ai(y):
        if y == 0:
            return mp.mpf(0)
        return (q(y) - mp.exp(-y / 2) * q0) * mp_rho(y)
    aint, e2 = mp.quad(ai, pts, error=True)
    arch = (mp.log(4 * mp.pi) + mp.euler) * q0 / 2 + aint + q0 / 2 * mp.log(mp.tanh(mp.mpf(Y) / 2))
    kmax = int(mp.floor(mp.exp(Y))) + 1
    prime = mp.mpf(0)
    for k in PP_SORTED:
        if k > kmax:
            break
        lk = mp.log(k)
        if lk <= Y:
            prime += mp.log(PP_BASE[k]) / mp.sqrt(k) * q(lk)
    return pole - arch - prime, dict(pole=pole, arch=arch, prime=prime), e1 + e2


# ===========================================================================
head("0. ENVIRONMENT AND PRECISION")
# ===========================================================================
import flint as _flint  # noqa: E402
print(f"  python-flint {_flint.__version__} (arb balls), working precision {PREC} bits; mpmath {mp.__version__} "
      f"at {mp.mp.dps} digits for the general quadrature path; numpy only for starting vectors")
print(f"  prime powers sieved up to {XMAX}: {len(PP_SORTED)} of them")
check(len(PP_SORTED) > 0 and PP_BASE[2] == 2 and PP_BASE[1024] == 2 and 1000 not in PP_BASE,
      "prime-power sieve sane (2, 1024 are prime powers; 1000 is not)")

# ===========================================================================
head("1. CONSISTENCY CHECK (brief, Conventions; A2.2(iii)): the general Psi reproduces zst's (a_n, b_n)")
# ===========================================================================
ZST_C = r"""
#include <stdio.h>
#include <stdlib.h>
#include "zst.h"
int main(int argc, char **argv)
{
    ulong X = strtoul(argv[1], 0, 10); slong N = atol(argv[2]); slong prec = atol(argv[3]);
    arb_t x; arb_ptr a = _arb_vec_init(N + 1), b = _arb_vec_init(N + 1); slong n;
    arb_init(x); arb_set_ui(x, X);
    zst_riemann_ab(a, b, N, x, X, prec);
    for (n = 0; n <= N; n++) {
        flint_printf("%wd ", n);
        arb_printn(a + n, 60, ARB_STR_NO_RADIUS); flint_printf(" "); mag_printd(arb_radref(a + n), 3); flint_printf(" ");
        arb_printn(b + n, 60, ARB_STR_NO_RADIUS); flint_printf(" "); mag_printd(arb_radref(b + n), 3); flint_printf("\n");
    }
    _arb_vec_clear(a, N + 1); _arb_vec_clear(b, N + 1); arb_clear(x);
    return 0;
}
"""


def zst_ab(X, N, prec=300):
    zdir = os.path.join(REPO, "zst")
    lib = os.path.join(zdir, "build", "libzst.a")
    if not os.path.exists(lib):
        subprocess.run(["make", "-C", zdir], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(td, "p.c")
        exe = os.path.join(td, "p")
        with open(src, "w") as fh:
            fh.write(ZST_C)
        cp = subprocess.run(["cc", "-O2", "-I" + os.path.join(zdir, "include"), src, lib,
                             "-lflint", "-lmpfr", "-lgmp", "-lm", "-o", exe], capture_output=True, text=True)
        if cp.returncode != 0:
            return None
        out = subprocess.run([exe, str(X), str(N), str(prec)], capture_output=True, text=True).stdout
    a, b, ra, rb = [], [], [], []
    for line in out.strip().splitlines():
        t = line.split()
        a.append(mp.mpf(t[1])); ra.append(float(t[2])); b.append(mp.mpf(t[3])); rb.append(float(t[4]))
    return a, b, ra, rb


def qU(n, m, L):
    """q(U_n, U_m)(y) on [0, L] (paper Lemma `polarize0`, l.389-397)"""
    if n == m:
        return lambda y: 2 * (1 - y / L) * mp.cos(2 * mp.pi * n * y / L)
    return lambda y: (mp.sin(2 * mp.pi * m * y / L) - mp.sin(2 * mp.pi * n * y / L)) / (mp.pi * (n - m))


def conv_general(f, g, supp_f, supp_g, y):
    """(f^* * g)(y) = int conj(f(x - y)) g(x) dx by quadrature; f, g callables with compact supports"""
    lo = max(supp_g[0], supp_f[0] + y)
    hi = min(supp_g[1], supp_f[1] + y)
    if hi <= lo:
        return mp.mpf(0)
    return mp.quad(lambda x: mp.conj(f(x - y)) * g(x), [lo, hi])


# (1a) the convolution itself, generic quadrature vs the paper's closed form
L13 = mp.log(13)
maxc = mp.mpf(0)
for (n, m) in ((2, 2), (3, 1), (0, 4)):
    Un = lambda x, n=n: mp.exp(2j * mp.pi * n * x / L13) / mp.sqrt(L13)
    Um = lambda x, m=m: mp.exp(2j * mp.pi * m * x / L13) / mp.sqrt(L13)
    for y in (mp.mpf("0.3"), mp.mpf("1.1"), mp.mpf("2.0")):
        qn = conv_general(Un, Um, (0, L13), (0, L13), y) + conv_general(Un, Um, (0, L13), (0, L13), -y)
        maxc = max(maxc, abs(qn - qU(n, m, L13)(y)))
check(maxc < mp.mpf("1e-50"),
      f"generic (f^* * g)(y) + (f^* * g)(-y) for f, g = U_n, U_m on [0, log 13] equals the paper's q(U_n, U_m) "
      f"(Lemma polarize0) at 9 (n, m, y) samples: max |diff| = {mp.nstr(maxc, 3)}")

# (1b) a_n = Psi(q(U_n, U_n)), b_n = n Psi(q(U_n, U_0)) (tau_{n0} = (b_n - b_0)/n, b_0 = 0) against zst
ZST_OK = True
for (X, N) in ((13, 10), (9, 8)):
    Z = zst_ab(X, N)
    if Z is None:
        check(False, f"zst printer compiled and ran for x = {X}")
        ZST_OK = False
        continue
    za, zb, zra, zrb = Z
    L = mp.log(X)
    print(f"\n  x = lambda^2 = {X}, L = log x = {mp.nstr(L, 15)}, prime powers <= {X}; zst at 300 bits, printed to 60 digits")
    print(f"  {'n':>3} {'a_n (this implementation)':>34} {'|a - a_zst|':>11} {'b_n (this implementation)':>34} "
          f"{'|b - b_zst|':>11} {'quad err':>9}")
    maxdev = mp.mpf(0)
    maxerr = mp.mpf(0)
    for n in range(N + 1):
        a_m, _, ea = psi_general(qU(n, n, L), L)
        if n > 0:
            t_m, _, eb = psi_general(qU(n, 0, L), L)
            b_m = n * t_m
        else:
            b_m, eb = mp.mpf(0), mp.mpf(0)
        da, db = abs(a_m - za[n]), abs(b_m - zb[n])
        maxdev = max(maxdev, da, db)
        maxerr = max(maxerr, ea, eb)
        print(f"  {n:>3} {mp.nstr(a_m, 30):>34} {mp.nstr(da, 2):>11} {mp.nstr(b_m, 30):>34} {mp.nstr(db, 2):>11} "
              f"{mp.nstr(max(ea, eb), 2):>9}")
    ok = check(maxdev < mp.mpf("1e-45"),
               f"x = {X}: all a_n, b_n (n = 0..{N}) of the general Psi agree with zst: max deviation "
               f"{mp.nstr(maxdev, 3)} (zst radii <= {max(zra + zrb):.1e}, quad estimates <= {mp.nstr(maxerr, 2)})")
    ZST_OK = ZST_OK and ok
    # Loewner structure: tau_{nm} = (b_n - b_m)/(n - m) off the (n, 0) column
    maxl = mp.mpf(0)
    for (n, m) in ((1, 2), (2, 5), (3, 7), (8, 6)):
        if max(n, m) <= N:
            t_nm, _, _ = psi_general(qU(n, m, L), L)
            maxl = max(maxl, abs(t_nm - (zb[n] - zb[m]) / (n - m)))
    check(maxl < mp.mpf("1e-45"),
          f"x = {X}: off-column entries Psi(q(U_n, U_m)) = (b_n - b_m)/(n - m) with zst's b for "
          f"(n,m) = (1,2),(2,5),(3,7),(8,6): max deviation {mp.nstr(maxl, 3)}")
    if X == 9:
        ref = os.path.join(REPO, "notes", "zeta-spectral-triples", "reference_ab_lambda3.txt")
        dref = mp.mpf(0)
        with open(ref) as fh:
            for line in fh:
                if line.startswith("#"):
                    continue
                t = line.split()
                n = int(t[0])
                a_m, _, _ = psi_general(qU(n, n, L), L)
                b_m = n * psi_general(qU(n, 0, L), L)[0] if n > 0 else mp.mpf(0)
                dref = max(dref, abs(a_m - mp.mpf(t[1])), abs(b_m - mp.mpf(t[2])))
        check(dref < mp.mpf("1e-45"),
              f"x = 9: also agrees with the 50-digit mpmath reference file used by zst/tests/test_ab.c: "
              f"max deviation {mp.nstr(dref, 3)}")
check(ZST_OK, "CONSISTENCY CHECK PASSED: the implementation of W used below reproduces zst on the Fourier basis")

# ===========================================================================
head("2. TEST CLASS AND THE ADMISSIBLE delta TABLE (brief A2.1)")
# ===========================================================================
PLAN = [((2,), A) for A in range(1, 7)] + [((2, 3), A) for A in range(1, 5)] + [((2, 3, 5), A) for A in range(1, 5)]
FRACTIONS = (Fraction(9, 10), Fraction(3, 10), Fraction(1, 10))


def lattice(S, A):
    return list(itertools.product(range(A + 1), repeat=len(S)))


def ratio_of(S, e):
    r = Fraction(1)
    for p, a in zip(S, e):
        r *= Fraction(p) ** a
    return r


def admissible(S, A):
    """delta_max = (1/2) min_{r, k != r} |log k - log r| over lattice ratios r >= 1 (r = 1 included)."""
    ratios = set()
    for e in itertools.product(range(-A, A + 1), repeat=len(S)):
        r = ratio_of(S, e)
        if r >= 1:
            ratios.add(r)
    cand = []                                  # (float distance, r, k)
    for r in ratios:
        D = math.log(r.numerator) - math.log(r.denominator)
        i = bisect.bisect_left(PP_LOGF, D)
        for j in (i - 2, i - 1, i, i + 1, i + 2):
            if 0 <= j < len(PP_SORTED):
                k = PP_SORTED[j]
                if Fraction(k) == r:
                    continue
                cand.append((abs(PP_LOGF[j] - D), r, k))
    cand.sort(key=lambda t: t[0])
    fmin = cand[0][0]
    best = None
    for dist, r, k in cand:
        if dist > fmin + 1e-9:
            break
        d = abs(arb(k).log() - log_frac(r))
        if best is None or d < best[0]:
            best = (d, r, k)
    minD = min((log_frac(r) for r in ratios if r > 1), key=lambda a: ff(a))
    return dict(dmax=best[0] / 2, r=best[1], k=best[2], minD=minD, nratios=len(ratios))


def round_down_4(x):
    """largest 4-significant-digit decimal below x (x > 0 float); returns the string"""
    e = math.floor(math.log10(x))
    mant = math.floor(x / 10.0 ** (e - 3))
    return format(Decimal(mant).scaleb(e - 3), "f")


ADM = {}
print(f"  {'S':>9} {'A':>2} {'dim':>4} {'#ratios':>7} {'delta_max':>24} {'binding pair (r vs k)':>24} "
      f"{'min log r (r>1)':>16}")
for S, A in PLAN:
    ad = admissible(S, A)
    ADM[(S, A)] = ad
    print(f"  {str(set(S)):>9} {A:>2} {(A + 1) ** len(S):>4} {ad['nratios']:>7} {fb(ad['dmax'], 10):>24} "
          f"{str(ad['r']) + ' vs ' + str(ad['k']):>24} {fm(ad['minD'], 8):>16}")
for S, A in PLAN:
    ad = ADM[(S, A)]
    check(2 * ad["dmax"] < ad["minD"] and 2 * ad["dmax"] <= LOG2,
          f"S = {set(S)}, A = {A}: 2 delta_max < min_(r>1) log r and <= log 2, so for admissible delta the "
          f"translates are disjointly supported and no entry has overlapping bumps (D = 0 or D > 2 delta)")


def delta_grid(S, A):
    ad = ADM[(S, A)]
    out = []
    for f in FRACTIONS:
        s = round_down_4(float(ad["dmax"].mid()) * f.numerator / f.denominator)
        out.append((f, s))
    return out


# ===========================================================================
head("3. BUMP CONSTANTS (delta-independent; certified unless marked)")
# ===========================================================================
EPS = arb(1) / (2 * (PREC + 20) * LOG2)          # phi_1(1 - eps) <= exp(-1/(2 eps)) = 2^-(PREC+20)
TINY = arb(2) ** (-(PREC + 20))
RTOL = arb(2) ** (-(PREC - 8))
ATOL = arb(2) ** (-(PREC + 12))


def phi1(t):
    return (-1 / (1 - t * t)).exp()


def bump_int(g, gsup):
    """int_{-1}^{1} phi_1(t) g(t) dt as a certified ball; |g| <= gsup on [-1, 1]"""
    v = acb.integral(lambda t, _: phi1(t) * g(t), -1 + EPS, 1 - EPS, rel_tol=RTOL, abs_tol=ATOL).real
    return v + arb(0, 2 * EPS * TINY * gsup)


_MU = {}


def mu(j):
    """mu_j = int phi_1 t^j dt (0 for odd j)"""
    if j % 2:
        return arb(0)
    if j not in _MU:
        _MU[j] = bump_int(lambda t, j=j: t ** j, 1)
    return _MU[j]


_MT = {}


def Mt(j):
    """Mt_j = int int phi_1(x) phi_1(w) (x - w)^j dx dw = sum_{i even} C(j, i) mu_i mu_{j-i} (0 for odd j)"""
    if j % 2:
        return arb(0)
    if j not in _MT:
        _MT[j] = sum((math.comb(j, i) * mu(i) * mu(j - i) for i in range(0, j + 1, 2)), arb(0))
    return _MT[j]


R10 = bump_int(lambda t: phi1(t), 1)             # R_1(0) = int phi_1^2


def R1(s):
    """R_1(s) = int phi_1(t) phi_1(t - s) dt, certified ball, any real s"""
    s = abs(s)
    a = s - 1 + EPS
    b = arb(1) - EPS
    if not (a < b):
        return arb(0, 2 * TINY)
    v = acb.integral(lambda t, _: phi1(t) * phi1(t - s), a, b, rel_tol=RTOL, abs_tol=ATOL).real
    return v + arb(0, 2 * EPS * TINY)


print(f"  eps (end truncation) = {fm(EPS, 6)}, phi_1(1 - eps) <= 2^-{PREC + 20}")
print(f"  mu_0 = int phi_1        = {fb(mu(0), 40)}")
print(f"  mu_2 = int phi_1 t^2    = {fb(mu(2), 40)}")
print(f"  R_1(0) = int phi_1^2    = {fb(R10, 40)}")
check(R10.rad() < arb("1e-55") and mu(0).rad() < arb("1e-55"), "mu_0 and R_1(0) certified to better than 1e-55")

# tanh-sinh on [0, 2] over certified R_1 node values: levels h = 1/64 and 1/128, |u| <= 4.6
TS_K = 7
TS_U = 4.6
_nodes = []
for j in range(-int(TS_U * 2 ** TS_K), int(TS_U * 2 ** TS_K) + 1):
    u = arb(j) / 2 ** TS_K
    x = (PI / 2) * u.sinh()
    s = 2 / (1 + (-2 * x).exp())
    w = (PI / 2) * u.cosh() / (x.cosh() * x.cosh()) / 2 ** TS_K
    _nodes.append((j, s.mid(), w))
_R1n = {j: R1(s) for j, s, _ in _nodes}
JD = 100                                          # enough for delta <= 0.21 (diagonal Taylor ratio 2 delta / 3)


def _ts_consts(level_step):
    T = arb(0)
    A = [arb(0)] * (JD + 1)
    A = [arb(0) for _ in range(JD + 1)]
    for j, s, w in _nodes:
        if j % level_step:
            continue
        ww = w * level_step
        r = _R1n[j]
        T += (r - R10) / s * ww
        sp = arb(1)
        for i in range(JD + 1):
            A[i] += 2 * r * sp * ww
            sp = sp * s
    return T + R10 * LOG2, A


T7, A7 = _ts_consts(1)
T6, A6 = _ts_consts(2)
T1 = arb(T7.mid(), float((10 * abs(T7 - T6)).upper()) + float(T7.rad()))
AT = [arb(A7[i].mid(), float((10 * abs(A7[i] - A6[i])).upper()) + float(A7[i].rad())) for i in range(JD + 1)]
print(f"  tanh-sinh nodes on [0, 2]: {len(_nodes)} (level h = 1/128), certified R_1 at each node")
print(f"  T_1  = {fb(T1, 40)}   [NOT certified; level-doubling |T(1/128) - T(1/64)| = {sci(abs(T7 - T6).upper(), 1)}]")
for i in (0, 1, 2, 3, 5, 11, 31):
    print(f"  At_{i:<2} = int R_1 |u|^{i:<2} du = {fb(AT[i], 30)}" + ("   [NOT certified]" if i % 2 else ""))
check(abs(AT[0] - mu(0) * mu(0)) < arb("1e-50"),
      f"quadrature At_0 = int R_1 equals (int phi_1)^2 = mu_0^2 (certified): |diff| = {sci(abs(A7[0] - mu(0) * mu(0)).upper(), 1)}")
dev_even = max(float(abs(A7[i] - Mt(i)).upper()) / float(Mt(i).mid()) for i in range(2, JD + 1, 2))
check(dev_even < 1e-45,
      f"quadrature At_j equals the moment formula Mt_j for all even j <= {JD} (relative dev <= {dev_even:.1e}): "
      f"validates the node table that also gives T_1 and the odd At_j")
_reljmax = max(float(abs(A7[i] - A6[i]).upper()) / float(A7[i].mid()) for i in range(JD + 1))
print(f"  level doubling: |T(1/128) - T(1/64)| = {sci(abs(T7 - T6).upper(), 1)}; max_j |At_j(1/128) - At_j(1/64)|/At_j = "
      f"{_reljmax:.1e} (attained at the largest j; the balls above carry 10x these differences)")
check(float(abs(T7 - T6).upper()) < 1e-50, "level doubling h = 1/64 -> 1/128 moves T_1 by < 1e-50")
# Taylor coefficients of rho_reg(y) = rho(y) - 1/(2y) at 0: rho = e^{-y/2} B(y)/(2y), B = 2y/(1 - e^{-2y})
_t = arb_series([0, 1], prec=JD + 3)
_om = 1 - (-2 * _t).exp()                         # 2y - 2y^2 + ...
_om_over_y = arb_series(_om.coeffs()[1:], prec=JD + 2)
_B = 2 / _om_over_y
_num = (-_t / 2).exp() * _B - 1                   # vanishes at 0
RREG = [c / 2 for c in _num.coeffs()[1:JD + 2]]   # r_j, j = 0..JD
while len(RREG) < JD + 1:
    RREG.append(arb(0))
print(f"  rho_reg(y) = rho(y) - 1/(2y) = {fm(RREG[0], 20)} + ({fm(RREG[1], 20)}) y + ({fm(RREG[2], 20)}) y^2 + ...")
check(abs(RREG[0] - arb(1) / 4) < arb("1e-55") and abs(RREG[1] - arb(-1) / 48) < arb("1e-55"),
      "rho_reg(0) = 1/4 and rho_reg'(0) = -1/48 (hand expansion of e^{y/2}/(2 sinh y) - 1/(2y))")
# Cauchy bound B0 >= max |rho_reg| on |y| = 3 (covering by 720 complex balls)
_B0 = arb(0)
for i in range(720):
    th = 2 * PI * i / 720
    c = acb(3 * th.cos(), 3 * th.sin())
    rad = 3 * 2 * PI / 720
    y = acb(arb(c.real.mid(), float(rad.upper())), arb(c.imag.mid(), float(rad.upper())))
    val = (y / 2).exp() / (y.exp() - (-y).exp()) - 1 / (2 * y)
    _B0 = max(_B0, abs(val).upper(), key=lambda a: float(a.mid()))
B0 = arb(float(_B0.mid()) * 1.01 + 1e-9)
print(f"  Cauchy bound max_(|y| = 3) |rho_reg(y)| <= {fm(B0, 6)}")
check(float(B0.mid()) < 50, "rho_reg is bounded on |y| = 3 (its nearest singularities are +-i pi)")
_prop = sum((abs(RREG[j]) * arb("0.21") ** (j + 1) * AT[j].rad() for j in range(JD + 1)), arb(0))
check(_prop < arb("1e-50"),
      f"the non-certified At_j balls move the normalised diagonal by at most sum_j |r_j| delta^(j+1) rad(At_j) / R_1(0) "
      f"<= {sci(ff(_prop / R10), 1)} for every delta <= 0.21 used (T_1 adds its own radius {fr(T1)})")


# ===========================================================================
# Gram entries
# ===========================================================================
_CD = {}


def c_delta(dl):
    key = dl.mid().str(30)
    if key not in _CD:
        _CD[key] = dl * bump_int(lambda t: (dl * t / 2).exp(), (dl / 2).exp())
    return _CD[key]


def arch_diag(dl):
    """W_R(R_delta), certified except for T_1 and odd At_j (see header)"""
    assert dl < arb("0.21")
    s = (arb(4) * PI).log() + EULER - LOG2
    val = s * R10 + T1 + R10 * dl.log()
    dp = arb(1)
    ratio = 2 * dl / 3
    for j in range(JD + 1):
        val += RREG[j] * dp * dl * AT[j]            # r_j delta^{j+1} At_j
        dp = dp * dl
    tail = B0 * mu(0) * mu(0) * dl * ratio ** (JD + 1) / (1 - ratio)
    return dl * (val + arb(0, float(tail.upper())))


def arch_off(D, dl):
    """int int phi_delta(x) phi_delta(w) rho(D + x - w) dx dw for D > 2 delta: Taylor at D + Cauchy tail"""
    assert D > 2 * dl
    r = (D + 2 * dl) / 2
    q = 2 * dl / r
    B = ((D + r) / 2).exp() / (2 * (D - r).sinh())
    qf, Bf, df = float(q.mid()), float(B.mid()), float(dl.mid())
    target = 2.0 ** (-(PREC + 10)) * df
    J = 2
    while Bf * 0.2 * df * df * qf ** (J + 1) / (1 - qf) > target:
        J += 2
    ser = arb_series([D, 1], prec=J + 1)
    rho_ser = (-ser / 2).exp() / (1 - (-2 * ser).exp())
    co = rho_ser.coeffs()
    val = arb(0)
    dp = dl * dl
    for j in range(0, J + 1, 2):
        val += co[j] * dp * Mt(j)
        dp = dp * dl * dl
    tail = B * mu(0) * mu(0) * dl * dl * q ** (J + 1) / (1 - q)
    return val + arb(0, float(tail.upper())), J


def prime_part(D, dl, D_is_zero=False, r=None):
    """sum over ALL prime powers k with |log k -+ D| < 2 delta of Lambda(k) k^{-1/2} R_delta(log k -+ D).
    Returns (value, list of k that contribute).  Membership decided in ball arithmetic."""
    val = arb(0)
    ks = []
    lo = math.exp(float((D - 2 * dl).mid())) * (1 - 1e-12)
    hi = math.exp(float((D + 2 * dl).mid())) * (1 + 1e-12)
    for k in range(max(2, math.floor(lo)), math.ceil(hi) + 1):
        if k not in PP_BASE:
            continue
        for sgn in ((1,) if not D_is_zero else (1, -1)):
            s = arb(k).log() - sgn * D
            if abs(s) < 2 * dl:
                ks.append(k)
                Rv = R10 if (r is not None and Fraction(k) == r) else R1(s / dl)   # s = 0 exactly when k = r
                val += arb(PP_BASE[k]).log() / arb(k).sqrt() * dl * Rv
            elif not (abs(s) >= 2 * dl):
                raise ValueError("undecided prime-power membership")
    # q(y) = R(y - D) + R(y + D): the second term needs log k + D < 2 delta, impossible for k >= 2 when
    # 2 delta < log 2 and D >= 0 -- asserted, not assumed:
    assert 2 * dl < LOG2
    return val, ks


_ENT = {}


def entry(r, dls):
    """Gram entry for the lattice ratio r = n_beta / n_alpha (Fraction >= 1) at delta = arb(dls)."""
    key = (r, dls)
    if key in _ENT:
        return _ENT[key]
    dl = arb(dls)
    D = log_frac(r)
    c = c_delta(dl)
    if r == 1:
        pole = 2 * c * c
        arch = arch_diag(dl)
        prime, ks = prime_part(arb(0), dl, D_is_zero=True)
        J = JD
    else:
        pole = 2 * (D / 2).cosh() * c * c
        arch, J = arch_off(D, dl)
        prime, ks = prime_part(D, dl, r=r)
    e = dict(pole=pole, arch=arch, prime=prime, total=pole - arch - prime, ks=ks, J=J, D=D)
    _ENT[key] = e
    return e


# ===========================================================================
head("4. STRUCTURE OF THE ENTRIES AND CROSS-CHECK OF THE BUMP FORMULAS AGAINST THE GENERAL Psi")
# ===========================================================================
# (4a) the bump formulas against psi_general applied to q(y) = R_delta(y - D) + R_delta(y + D) (R_1 by arb)
def q_bump(D, dl):
    dlm = mpf_of(dl)
    Dm = mp.mpf(D) if not isinstance(D, arb) else mpf_of(D)

    memo = {}

    def q(y):
        if y in memo:
            return memo[y]
        v = mp.mpf(0)
        for s in (y - Dm, y + Dm):
            if abs(s) < 2 * dlm:
                v += dlm * mpf_of(R1(arb_of_mpf(s / dlm)))
        memo[y] = v
        return v
    return q


for (rs, dls) in (("1", "0.05"), ("2", "0.05"), ("3/2", "0.05"), ("8", "0.1")):
    r = Fraction(rs)
    dl = arb(dls)
    e = entry(r, dls)
    Dm = mpf_of(e["D"])
    dlm = mp.mpf(dls)
    Y = Dm + 2 * dlm
    brk = [Dm - 2 * dlm, Dm, dlm, 2 * dlm] if r != 1 else [dlm, 2 * dlm]
    gv, parts, gerr = psi_general(q_bump(e["D"], dl), Y, brk)
    dev = abs(gv - mpf_of(e["total"]))
    devp = max(abs(parts["pole"] - mpf_of(e["pole"])), abs(parts["arch"] - mpf_of(e["arch"])),
               abs(parts["prime"] - mpf_of(e["prime"])))
    check(dev < mp.mpf("1e-40") and devp < mp.mpf("1e-40"),
          f"entry r = {rs}, delta = {dls}: bump formulas (pole {fm(e['pole'], 8)}, arch {fm(e['arch'], 8)}, prime "
          f"{fm(e['prime'], 8)}, prime powers {e['ks']}) = general Psi by quadrature: |diff| = {mp.nstr(dev, 2)}, "
          f"parts <= {mp.nstr(devp, 2)} (quad est {mp.nstr(gerr, 2)})")
check(entry(Fraction(8), "0.1")["ks"] == [7, 8, 9],
      "at the NON-admissible delta = 0.1 the entry r = 8 picks up the neighbours 7 and 9 as well as 8 "
      "(a generic-R_1 prime contribution; exercised on purpose)")

# (4b) sharpness of delta_max: slightly above it the binding pair acquires a foreign prime power
for S, A in PLAN:
    ad = ADM[(S, A)]
    dl = ad["dmax"] * (1 + arb("1e-12"))
    _, ks = prime_part(log_frac(ad["r"]), dl)
    foreign = [k for k in ks if Fraction(k) != ad["r"]]
    check(ad["k"] in foreign,
          f"S = {set(S)}, A = {A}: at delta = delta_max (1 + 1e-12) the ratio {ad['r']} sees the foreign prime "
          f"power {ad['k']} (delta_max is sharp)")


# ===========================================================================
# linear algebra in balls
# ===========================================================================
def ldl_inertia(G, s):
    """(neg, pos) inertia of G - s I by unpivoted LDL^T in ball arithmetic; None if a pivot ball contains 0."""
    n = len(G)
    Ld = [[None] * n for _ in range(n)]           # Ld[i][k] = L[i][k] d[k]
    Lm = [[None] * n for _ in range(n)]
    d = [None] * n
    for j in range(n):
        acc = G[j][j] - s
        for k in range(j):
            acc -= Lm[j][k] * Ld[j][k]
        if acc.contains(0):
            return None
        d[j] = acc
        for i in range(j + 1, n):
            acc = G[i][j]
            for k in range(j):
                acc -= Lm[i][k] * Ld[j][k]
            Lm[i][j] = acc / d[j]
            Ld[i][j] = acc
    neg = sum(1 for x in d if x < 0)
    pos = sum(1 for x in d if x > 0)
    return neg, pos


def min_eig(G, want_vec=True):
    """Certified simple minimal eigenvalue of the symmetric ball matrix G (list of lists of arb).
    Returns dict(lam = ball, vec = list of arb midpoints (unit), res, gap_lb, sin_bound, certified)."""
    n = len(G)
    if n == 1:
        return dict(lam=G[0][0], vec=[arb(1)], res=arb(0), gap_lb=None, sin_bound=arb(0), certified=True)
    Mf = np.array([[ff(x) for x in row] for row in G])
    w, V = np.linalg.eigh(Mf)
    Mm = arb_mat([[x.mid() for x in row] for row in G])
    # shift slightly below the float eigenvalue so that M - sig I is safely invertible in ball arithmetic;
    # each inverse-iteration step then contracts the error by ~1e-6 / gap
    sig = arb(float(w[0]) - 1e-6 * (abs(float(w[0])) + 1.0))
    Ms = arb_mat([[Mm[i, j] - (sig if i == j else 0) for j in range(n)] for i in range(n)])
    v = arb_mat([[float(V[i, 0])] for i in range(n)])
    for _ in range(12):
        v = Ms.solve(v)
        nv = sum((v[i, 0] * v[i, 0] for i in range(n)), arb(0)).sqrt()
        v = arb_mat([[(v[i, 0] / nv).mid()] for i in range(n)])
    vv = [v[i, 0] for i in range(n)]
    # sign convention: component of largest modulus positive
    imax = max(range(n), key=lambda i: abs(ff(vv[i])))
    if vv[imax] < 0:
        vv = [-x for x in vv]
    Gv = [sum((G[i][j] * vv[j] for j in range(n)), arb(0)) for i in range(n)]
    nrm2 = sum((x * x for x in vv), arb(0))
    ray = sum((vv[i] * Gv[i] for i in range(n)), arb(0)) / nrm2
    lm = ray.mid()
    r2 = sum(((Gv[i] - lm * vv[i]) * (Gv[i] - lm * vv[i]) for i in range(n)), arb(0)) / nrm2
    res = arb(r2.upper()).sqrt()                  # upper bound for ||(G - lm) v|| / ||v||
    resu = float(res.upper())
    s2 = arb((float(lm) + float(w[1])) / 2)
    inert = ldl_inertia(G, s2)
    gap_lb = s2 - lm - resu
    cert = inert is not None and inert[0] == 1 and gap_lb > 0
    lam = arb(lm, resu)
    sinb = arb(resu) / gap_lb if gap_lb > 0 else arb(1)
    return dict(lam=lam, vec=vv, res=res, gap_lb=gap_lb, sin_bound=sinb, certified=cert, second=float(w[1]))


def sub(G, idx):
    return [[G[i][j] for j in idx] for i in idx]


# ===========================================================================
head("5. MEASUREMENTS (brief A2.3): Gram matrices, minimal eigenpairs, the three decompositions")
# ===========================================================================
print("""  Notation (all matrices normalised by ||phi_delta||^2 = delta R_1(0)):
    G        the Gram matrix on Lambda_S(A);  d = its (constant) diagonal
    G_X      principal submatrix on the single-prime points X (origin + the |S| axes)
    G_bd     block-diagonal restriction to the axis subspaces = direct sum of the one-prime forms G_{p}
             (each on its own copy of the origin); lambda(G_bd) = min_p lambda(G_{p})
    G_nomix  mixed entries (alpha, beta differing in >= 2 coordinates) set to 0.  EXACT FACT used below:
             G_nomix = d I + sum_p I x (G_{p} - d I) x I is the Kronecker sum of the one-prime forms
             (axis-type entries depend only on the ratio p^j), so lambda(G_nomix) = d + sum_p (lambda(G_{p}) - d)
             and its minimal eigenvector is the tensor product of the one-prime eigenvectors.
    G_-mixA  only the archimedean part of the mixed entries removed (pole part kept)
    G_-mixP  only the pole part of the mixed entries removed
    G_noP    prime terms removed everywhere (pole + archimedean only)
  Gaps: inter-place = lambda(G_bd) - lambda(G); mixed = lambda(G_nomix) - lambda(G); combs = lambda(G_noP) - lambda(G).
  'offaxis' = weight of the minimal eigenvector outside X; 'schmidt(p)' = 1 - sigma_1^2 for the cut {p} | S - {p}
  (0 iff the eigenvector is a product across that cut).""")

RESULTS = {}


def classify(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def schmidt_defect(vec, S, A, pidx):
    """1 - sigma_1^2 of the unit vector reshaped as (coordinate p) x (other coordinates), in mpmath"""
    pts = lattice(S, A)
    others = sorted(set(tuple(x for i, x in enumerate(pt) if i != pidx) for pt in pts))
    oi = {o: i for i, o in enumerate(others)}
    M = mp.matrix(A + 1, len(others))
    for pt, v in zip(pts, vec):
        o = tuple(x for i, x in enumerate(pt) if i != pidx)
        M[pt[pidx], oi[o]] = mpf_of(v)
    MM = M * M.T
    ev = mp.eigsy(MM, eigvals_only=True)
    ev = sorted([ev[i] for i in range(A + 1)])
    return mp.fsum(ev[:-1])


def build(S, A, dls):
    pts = lattice(S, A)
    n = len(pts)
    nrm = arb(dls) * R10
    parts = {}
    for i in range(n):
        for j in range(i, n):
            e = [b - a for a, b in zip(pts[i], pts[j])]
            r = ratio_of(S, e)
            if r < 1:
                r = 1 / r
            parts[(i, j)] = entry(r, dls)
    mats = {}

    def mk(fn):
        M = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                v = fn(i, j, parts[(i, j)]) / nrm
                M[i][j] = v
                M[j][i] = v
        return M
    cls = {(i, j): classify(pts[i], pts[j]) for i in range(n) for j in range(i, n)}
    mats["G"] = mk(lambda i, j, e: e["total"])
    mats["G_noP"] = mk(lambda i, j, e: e["pole"] - e["arch"])
    mats["G_nomix"] = mk(lambda i, j, e: e["total"] if cls[(i, j)] <= 1 else arb(0))
    mats["G_-mixA"] = mk(lambda i, j, e: e["total"] if cls[(i, j)] <= 1 else e["pole"])
    mats["G_-mixP"] = mk(lambda i, j, e: e["total"] if cls[(i, j)] <= 1 else -e["arch"])
    return pts, parts, cls, mats, nrm


def axis_index(pts, pidx):
    return [i for i, pt in enumerate(pts) if all(x == 0 for k, x in enumerate(pt) if k != pidx)]


def single_prime_index(pts):
    return [i for i, pt in enumerate(pts) if sum(1 for x in pt if x) <= 1]


def run_case(S, A, dls, verbose):
    pts, parts, cls, mats, nrm = build(S, A, dls)
    n = len(pts)
    G = mats["G"]
    d = G[0][0]
    # A2.2 (i), (ii): structure of the entries
    bad_mixed = [(i, j) for (i, j), c in cls.items() if c >= 2 and parts[(i, j)]["ks"]]
    bad_axis = []
    for (i, j), c in cls.items():
        if c == 1:
            e = [b - a for a, b in zip(pts[i], pts[j])]
            r = ratio_of(S, [abs(x) for x in e])
            k = int(r)
            p = PP_BASE.get(k)
            expect = arb(p).log() / arb(k).sqrt() * arb(dls) * R10
            if parts[(i, j)]["ks"] != [k] or not abs(parts[(i, j)]["prime"] - expect) < arb("1e-50"):
                bad_axis.append((i, j))
        if c == 0 and parts[(i, j)]["ks"]:
            bad_axis.append((i, j))
    nmixed = sum(1 for c in cls.values() if c >= 2)
    naxis = sum(1 for c in cls.values() if c == 1)
    check(not bad_mixed and not bad_axis,
          f"S = {set(S)}, A = {A}, delta = {dls}: all {nmixed} mixed entries have NO prime contribution (pole + "
          f"archimedean only; A2.2(i)); all {naxis} axis-type entries carry exactly the comb term "
          f"log p p^(-j/2) ||phi||^2 of their own ratio p^j and nothing else (A2.2(ii)); diagonal: none")
    out = dict(S=S, A=A, dls=dls, n=n, d=d, pts=pts)
    # entry-class sizes
    comb = [parts[k]["prime"] / nrm for k, c in cls.items() if c == 1]
    pa_axis = [(parts[k]["pole"] - parts[k]["arch"]) / nrm for k, c in cls.items() if c == 1]
    mixP = [parts[k]["pole"] / nrm for k, c in cls.items() if c >= 2]
    mixA = [parts[k]["arch"] / nrm for k, c in cls.items() if c >= 2]
    mixT = [parts[k]["total"] / nrm for k, c in cls.items() if c >= 2]
    mx = lambda L: max((abs(ff(x)) for x in L), default=0.0)
    out["mixmax"] = (mx(mixP), mx(mixA), mx(mixT))
    # eigen-analysis
    E = {}
    for name in ("G", "G_nomix", "G_-mixA", "G_-mixP", "G_noP"):
        E[name] = min_eig(mats[name])
    Xi = single_prime_index(pts)
    E["G_X"] = min_eig(sub(G, Xi))
    Ep = {}
    for k, p in enumerate(S):
        Ep[p] = min_eig(sub(G, axis_index(pts, k)))
    lam_bd = min((Ep[p]["lam"] for p in S), key=lambda a: ff(a))
    kron = d + sum((Ep[p]["lam"] - d for p in S), arb(0))
    allcert = all(e["certified"] for e in E.values()) and all(e["certified"] for e in Ep.values())
    check(allcert, f"S = {set(S)}, A = {A}, delta = {dls}: every minimal eigenvalue below is certified simple "
                   f"(residual ball + LDL^T inertia of G - s I with exactly one negative pivot)")
    if len(S) >= 2:
        check(abs(E["G_nomix"]["lam"] - kron) < arb("1e-40"),
              f"S = {set(S)}, A = {A}, delta = {dls}: lambda(G_nomix) = d + sum_p (lambda(G_(p)) - d) (Kronecker sum): "
              f"{fm(E['G_nomix']['lam'], 15)} vs {fm(kron, 15)}")
        sd0 = max(schmidt_defect(E["G_nomix"]["vec"], S, A, k) for k in range(len(S)))
        check(sd0 < mp.mpf("1e-40"),
              f"S = {set(S)}, A = {A}, delta = {dls}: the minimal eigenvector of G_nomix is a product state across every "
              f"cut (max Schmidt defect {mp.nstr(sd0, 2)})")
    v = E["G"]["vec"]
    Xset = set(Xi)
    offaxis = sum((v[i] * v[i] for i in range(n) if i not in Xset), arb(0))
    schm = [schmidt_defect(v, S, A, k) for k in range(len(S))] if len(S) >= 2 else []
    # first-order attributions along v: v^T (G - G_x) v
    def quad_form(M, u):
        return sum((u[i] * sum((M[i][j] * u[j] for j in range(n)), arb(0)) for i in range(n)), arb(0))
    attr = {}
    for name in ("G_nomix", "G_-mixA", "G_-mixP", "G_noP"):
        D_ = [[G[i][j] - mats[name][i][j] for j in range(n)] for i in range(n)]
        attr[name] = quad_form(D_, v)
    out.update(E=E, Ep=Ep, lam_bd=lam_bd, kron=kron, offaxis=offaxis, schm=schm, attr=attr)
    # printing
    print(f"\n  --- S = {set(S)}, A = {A}, dim {n}, delta = {dls}  (delta/delta_max = "
          f"{float(arb(dls).mid()) / float(ADM[(S, A)]['dmax'].mid()):.3f}),  ||phi||^2 = {fm(nrm, 10)}")
    print(f"      diagonal d = {fb(d, 15)}   [d = (2 c^2 - W_R(R_delta))/||phi||^2; its radius is the non-certified T_1/At part]")
    print(f"      axis-type entries: comb part -Lambda(k)k^-1/2 in [{-max(ff(x) for x in comb):.6f}, "
          f"{-min(ff(x) for x in comb):.6f}], pole-arch part in [{min(ff(x) for x in pa_axis):.3e}, "
          f"{max(ff(x) for x in pa_axis):.3e}]")
    if nmixed:
        print(f"      mixed entries ({nmixed}): max |pole| = {out['mixmax'][0]:.3e}, max |arch| = {out['mixmax'][1]:.3e}, "
              f"max |total| = {out['mixmax'][2]:.3e}")
    print(f"      lambda_min:  G {fb(E['G']['lam'], 13)}   (next eigenvalue ~ {E['G']['second']:.6f}, gap >= "
          f"{fm(E['G']['gap_lb'], 4)})")
    print(f"                   G_X {fm(E['G_X']['lam'], 13)}   G_bd {fm(lam_bd, 13)}   one-prime: " +
          "  ".join(f"G_({p}) {fm(Ep[p]['lam'], 10)}" for p in S))
    if len(S) >= 2:
        print(f"                   G_nomix {fm(E['G_nomix']['lam'], 13)}   G_-mixA {fm(E['G_-mixA']['lam'], 13)}   "
              f"G_-mixP {fm(E['G_-mixP']['lam'], 13)}")
    print(f"                   G_noP {fm(E['G_noP']['lam'], 13)}")
    lg = E["G"]["lam"]
    print(f"      gaps: inter-place lambda(G_bd) - lambda(G) = {sci(ff(lam_bd - lg), 4)};  "
          f"mixed lambda(G_nomix) - lambda(G) = {sci(ff(E['G_nomix']['lam'] - lg), 4)};  "
          f"combs lambda(G_noP) - lambda(G) = {sci(ff(E['G_noP']['lam'] - lg), 4)}")
    if len(S) >= 2:
        print(f"            of the mixed gap: archimedean-only removal {sci(ff(E['G_-mixA']['lam'] - lg), 4)}, "
              f"pole-only removal {sci(ff(E['G_-mixP']['lam'] - lg), 4)}")
        print(f"      first order along v: v^T(G - G_nomix)v = {sci(ff(attr['G_nomix']), 4)} (arch part "
              f"{sci(ff(attr['G_-mixA']), 4)}, pole part {sci(ff(attr['G_-mixP']), 4)}); v^T(G - G_noP)v = "
              f"{sci(ff(attr['G_noP']), 4)}")
        print(f"      eigenvector: off-axis weight {sci(ff(offaxis), 4)};  Schmidt defects " +
              ", ".join(f"({p}|rest) {mp.nstr(sd, 4)}" for p, sd in zip(S, schm)) +
              f";  sin(angle to true eigvec) <= {sci(ff(E['G']['sin_bound']), 1)}")
    if verbose:
        if n <= 16:
            print("      minimal eigenvector (lattice point: component):")
            print("        " + "  ".join(f"{pt}: {fm(x, 8)}" for pt, x in zip(pts, v)))
        else:
            top = sorted(range(n), key=lambda i: -abs(ff(v[i])))[:8]
            print("      minimal eigenvector, 8 largest components: " +
                  "  ".join(f"{pts[i]}: {fm(v[i], 7)}" for i in top))
    return out


def print_gram(S, A, dls):
    pts, parts, cls, mats, nrm = build(S, A, dls)
    G = mats["G"]
    print(f"\n  Gram matrix G/||phi||^2 for S = {set(S)}, A = {A}, delta = {dls} (rows/cols: {pts}):")
    for i in range(len(pts)):
        print("      " + " ".join(f"{fm(G[i][j], 9):>14}" for j in range(len(pts))))


print_gram((2,), 2, delta_grid((2,), 2)[0][1])
print_gram((2, 3), 1, delta_grid((2, 3), 1)[0][1])

for S, A in PLAN:
    print(f"\n  ===== S = {set(S)}, A = {A}: delta_max = {fm(ADM[(S, A)]['dmax'], 10)}")
    for f, dls in delta_grid(S, A):
        RESULTS[(S, A, dls)] = run_case(S, A, dls, verbose=(f == FRACTIONS[0]))

# positivity of all forms measured (necessary condition of RH on these families; nothing assumed)
allpos = all(R["E"]["G"]["lam"] > 0 for R in RESULTS.values())
check(allpos, f"every Gram matrix measured ({len(RESULTS)} of them) is positive definite (certified lambda_min > 0)")

head("5b. SUMMARY TABLE (normalised minimal eigenvalues)")
print(f"  {'S':>9} {'A':>2} {'delta':>10} {'d':>10} {'lam(G)':>12} {'lam(G_X)':>12} {'lam(G_bd)':>12} "
      f"{'lam(nomix)':>12} {'lam(noP)':>10} {'gap_mix':>10} {'offaxis':>9} {'schmidt':>9}")
for (S, A, dls), R in RESULTS.items():
    E = R["E"]
    lg = E["G"]["lam"]
    sd = max(R["schm"]) if R["schm"] else mp.mpf(0)
    print(f"  {str(set(S)):>9} {A:>2} {dls:>10} {fm(R['d'], 6):>10} {fm(lg, 8):>12} {fm(E['G_X']['lam'], 8):>12} "
          f"{fm(R['lam_bd'], 8):>12} {fm(E['G_nomix']['lam'], 8):>12} {fm(E['G_noP']['lam'], 6):>10} "
          f"{sci(ff(E['G_nomix']['lam'] - lg), 2):>10} {sci(ff(R['offaxis']), 2):>9} {mp.nstr(sd, 3):>9}")

# scaling of the mixed gap with delta
for S, A in PLAN:
    if len(S) < 2:
        continue
    gs = [(float(arb(dls).mid()), ff(RESULTS[(S, A, dls)]["E"]["G_nomix"]["lam"] - RESULTS[(S, A, dls)]["E"]["G"]["lam"]))
          for _, dls in delta_grid(S, A)]
    ratios = [g / dd for dd, g in gs]
    print(f"  mixed gap / delta for S = {set(S)}, A = {A}: " + ", ".join(f"{x:.4f}" for x in ratios))

# ===========================================================================
head("6. EIGENVECTOR MOVEMENT WHEN A PRIME IS ADDED (brief A2.3, last paragraph)")
# ===========================================================================
print("""  At a common delta (admissible for the largest S), restrict the minimal eigenvector of the larger form to the
  sublattice of the smaller S (new coordinate = 0) and compare with the smaller form's minimal eigenvector.
  overlap = |<v_small, v_big|_sub>| / ||v_big|_sub||;  weight = ||v_big|_sub||^2.  In the Kronecker-sum model (mixed
  entries 0) the restriction is EXACTLY proportional to v_small (overlap 1) with weight = v_new[0]^2, the square of
  the origin component of the new prime's one-prime eigenvector; every deviation is carried by the mixed entries.""")
MOVE = []
for A, chain in ((1, ((2,), (2, 3), (2, 3, 5))), (2, ((2,), (2, 3), (2, 3, 5))), (3, ((2,), (2, 3), (2, 3, 5))),
                 (4, ((2,), (2, 3), (2, 3, 5)))):
    dmx = ADM[(chain[-1], A)]["dmax"]
    for fac in (Fraction(9, 10), Fraction(9, 100), Fraction(9, 1000)):
        dls = round_down_4(float(dmx.mid()) * fac.numerator / fac.denominator)
        vecs = {}
        for S in chain:
            if (S, A, dls) in RESULTS:
                R = RESULTS[(S, A, dls)]
            else:
                pts, parts, cls, mats, nrm = build(S, A, dls)
                E = min_eig(mats["G"])
                Ep = {p: min_eig(sub(mats["G"], axis_index(pts, k))) for k, p in enumerate(S)}
                R = dict(E={"G": E}, Ep=Ep, pts=pts)
            vecs[S] = R
        for small, big in zip(chain[:-1], chain[1:]):
            vs = vecs[small]["E"]["G"]["vec"]
            ps = vecs[small]["pts"]
            vb = vecs[big]["E"]["G"]["vec"]
            pb = vecs[big]["pts"]
            idx = {pt: i for i, pt in enumerate(pb)}
            restr = [vb[idx[pt + (0,)]] for pt in ps]
            w2 = sum((x * x for x in restr), arb(0))
            ov = abs(sum((a * b for a, b in zip(vs, restr)), arb(0))) / w2.sqrt()
            newp = big[-1]
            vnew = vecs[big]["Ep"][newp]["vec"]
            wpred = vnew[0] * vnew[0]
            lam_s = vecs[small]["E"]["G"]["lam"]
            lam_b = vecs[big]["E"]["G"]["lam"]
            MOVE.append((A, dls, small, big, ov, w2, wpred, lam_s, lam_b))
            print(f"  A = {A}, delta = {dls:>9}: {str(set(small)):>7} -> {str(set(big)):>9}: 1 - overlap = "
                  f"{sci(ff(1 - ov), 3):>10}, weight on old sublattice {fm(w2, 8)} (Kronecker prediction {fm(wpred, 8)}), "
                  f"lambda {fm(lam_s, 8)} -> {fm(lam_b, 8)}")
mono = True
for A in (1, 2, 3, 4):
    for small in ((2,), (2, 3)):
        rows = [ff(1 - m[4]) for m in MOVE if m[0] == A and m[2] == small]
        mono = mono and all(x > y for x, y in zip(rows, rows[1:]))
check(mono, "in every chain step the movement 1 - overlap decreases strictly as delta decreases (delta_c, "
            "delta_c/10, delta_c/100): the movement is carried by the O(delta) mixed entries")
# scaling of the movement with delta at fixed (A, chain step)
for A in (1, 2, 3, 4):
    for small in ((2,), (2, 3)):
        rows = [m for m in MOVE if m[0] == A and m[2] == small]
        if len(rows) == 3:
            xs = [math.log(float(arb(m[1]).mid())) for m in rows]
            ys = [math.log(max(ff(1 - m[4]), 1e-300)) for m in rows]
            slope = (ys[0] - ys[-1]) / (xs[0] - xs[-1])
            print(f"  A = {A}, {set(small)} -> +1 prime: log(1 - overlap) vs log delta slope over the three deltas = "
                  f"{slope:.3f}")

# ===========================================================================
head("7. COMPARISON STEP -- ZEROS OF ZETA USED HERE ONLY (brief A2.4, game rule 2; labelled)")
# ===========================================================================
print("""  Explicit formula in this normalisation: Psi(F) = sum_rho Fhat(i(rho - 1/2)), Fhat(t) = int F(y) e^{-ity} dy.
  For F = phi_alpha^* * phi_beta, Fhat(t) = conj(phihat_alpha(tbar)) phihat_beta(t), i.e. the brief's
  sum_rho phihat_alpha(rho) conj phihat_beta(1 - rhobar) up to the order of the two slots (real here).
  With the zeros used as returned (rho = 1/2 + i gamma, gamma > 0, together with conjugates):
      Z_M(D) = sum_{k <= M} 2 cos(gamma_k D) phihat_delta(gamma_k)^2,   phihat_delta(g) = delta int phi_1(t) cos(delta g t) dt.
  The prime side is the certified entry (pole - arch - prime) at the same D; no zero entered it.""")
ZPREC = 128
MMAX = 2000
ctx.prec = ZPREC
ZEROS = [z.imag for z in acb.zeta_zeros(1, MMAX)]    # certified gamma_1..gamma_2000 (arb)
ctx.prec = PREC
print(f"  gamma_1 = {fm(ZEROS[0], 15)}, gamma_{MMAX} = {fm(ZEROS[-1], 15)} (acb.zeta_zeros)")
EPSZ = arb(1) / (2 * (ZPREC + 20) * LOG2)


def phihat1(tau):
    ctx.prec = ZPREC
    v = acb.integral(lambda t, _: phi1(t) * (tau * t).cos(), -1 + EPSZ, 1 - EPSZ,
                     rel_tol=arb(2) ** -(ZPREC - 10), abs_tol=arb(2) ** -(ZPREC + 10)).real
    ctx.prec = PREC
    return v


MLIST = (10, 30, 100, 300, 1000, 2000)
CMP = []
for dls, rlist in (("0.1", ("1", "2", "3", "3/2", "6", "8")), ("0.05", ("1", "2", "3/2", "6"))):
    dl = arb(dls)
    ph = [dl * phihat1(dl * g) for g in ZEROS]
    ph2 = [x * x for x in ph]
    for rs in rlist:
        r = Fraction(rs)
        e = entry(r, dls)
        D = e["D"]
        terms = [2 * (g * D).cos() * p2 for g, p2 in zip(ZEROS, ph2)]
        part = []
        acc = arb(0)
        for k, t in enumerate(terms, 1):
            acc += t
            if k in MLIST:
                part.append(acc)
        errs = [abs(e["total"] - z) for z in part]
        absT = [sum((abs(t) for t in terms[M:]), arb(0)) for M in MLIST[:-1]]
        CMP.append((dls, rs, e, part, errs))
        print(f"  delta = {dls:>5}, r = {rs:>3} (D = {fm(D, 6)}, prime powers {e['ks']}): Psi = {fm(e['total'], 16)}")
        print("      M:            " + "  ".join(f"{M:>9}" for M in MLIST))
        print("      |Psi - Z_M|:  " + "  ".join(f"{sci(ff(x), 2):>9}" for x in errs))
        print("      sum_(M<k<=2000) |term|: " + "  ".join(f"{sci(ff(x), 2):>9}" for x in absT))
for dls, rs, e, part, errs in CMP:
    scale = abs(ff(e["total"])) + ff(arb(dls) * R10)
    check(ff(errs[-1]) / scale < 1e-9,
          f"explicit formula, delta = {dls}, r = {rs}: |Psi - Z_2000| / (|Psi| + ||phi||^2) = "
          f"{sci(ff(errs[-1]) / scale, 2)} (< 1e-9)")
# truncation law: log|Psi - Z_M| against sqrt(delta gamma_M)
for dls in ("0.1", "0.05"):
    rows = [c for c in CMP if c[0] == dls]
    xs, ys = [], []
    for k, M in enumerate(MLIST[1:-1], 1):
        g = ZEROS[M - 1]
        mx = max(ff(c[4][k]) for c in rows)
        xs.append(math.sqrt(float((arb(dls) * g).mid())))
        ys.append(math.log(mx))
    sl = np.polyfit(np.array(xs), np.array(ys), 1)[0]
    print(f"  delta = {dls}: fit of log max_r |Psi - Z_M| against sqrt(delta gamma_M) over M = 30..1000: slope "
          f"{sl:.3f} (the bump's transform decays like exp(-sqrt(tau)), so its square like exp(-2 sqrt(tau)))")

# ===========================================================================
head("TALLY")
# ===========================================================================
if _FAILED:
    print("  failing checks:")
    for line, msg in _FAILED:
        print(f"    L{line:4d}  {msg}")
else:
    print("  no failing checks")
print()
print(f"CHECKS: {_PASS} passed, {_FAIL} failed")
