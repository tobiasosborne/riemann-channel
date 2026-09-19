#!/usr/bin/env python3
"""The windowed Weil form as a compression, the extension disc for the next trace, and what
the counts add (nonnegativity, the Newton congruence), on the permutation (1 2)(3 4 5) and on the
Petersen graph.

Evidence for report/sections/08g_weil_window_extension.tex (lab-book shard RC-08G).
Deterministic; every check is an assertion, the tally is printed at the end.
Sections: 1 the permutation: windows, the disc (Schur complement = Levinson predictor and the
determinant ratio), truth inside, boundary = singular with kernel roots on the circle, the Pisarenko
extension, the Newton congruence, what pins the next trace; 2 the singular windows and the kernel
recurrence; 3 the Petersen graph: the disc in rescaled units and in count units.
"""
import numpy as np

CHECKS = 0
def check(cond, msg):
    global CHECKS
    CHECKS += 1
    assert cond, msg
    print(f"  ok {CHECKS:2d}  {msg}")

def toeplitz(t, K):                       # window matrix, entries t_{|j-k|}, j,k = 0..K (real data)
    return np.array([[t[abs(j - k)] for k in range(K + 1)] for j in range(K + 1)], float)

def disc(t, K):
    """Admissible next trace x = t_{K+1}: T_{K+1}(x) >= 0 iff |x - c| <= r (Schur complement)."""
    T = toeplitz(t, K); Ti = np.linalg.inv(T)
    w = np.array([t[K + 1 - j] for j in range(1, K + 1)])            # column above the diagonal, minus x
    c = -(Ti[0, 1:] @ w) / Ti[0, 0]
    r2 = (t[0] - w @ Ti[1:, 1:] @ w) / Ti[0, 0] + c ** 2
    return c, float(np.sqrt(max(r2, 0.0)))

def levinson_centre(t, K):
    """One-step linear predictor: T_{K-1} a = -(t_1..t_K), c = -sum_j a_j t_{K+1-j}."""
    a = np.linalg.solve(toeplitz(t, K - 1), -np.array([t[j] for j in range(1, K + 1)]))
    return -sum(a[j - 1] * t[K + 1 - j] for j in range(1, K + 1))

def pisarenko_next(t, K):
    """Subtract eps = min eig, kernel polynomial roots = atoms, weights by least squares; extrapolate."""
    T = toeplitz(t, K); ev, V = np.linalg.eigh(T); eps = ev[0]; ker = V[:, 0]
    roots = np.roots(ker[::-1])                                       # roots of sum_j ker_j w^j
    Vand = np.array([roots ** k for k in range(K + 1)])
    rhs = np.array([t[k] for k in range(K + 1)], complex); rhs[0] -= eps
    wts = np.linalg.lstsq(Vand, rhs, rcond=None)[0]
    return float((wts @ roots ** (K + 1)).real), float(eps), roots

def newton_residue(N, K):
    """Integer matrix: (K+1) c_{K+1} = -sum_{i=0}^{K} c_i N_{K+1-i} with c_i integers, so
    N_{K+1} = -sum_{i=1}^{K} c_i N_{K+1-i}  mod (K+1). Returns (residue, the c_i)."""
    c = [1]
    for j in range(1, K + 1):
        s = N[j] + sum(c[i] * N[j - i] for i in range(1, j))
        assert s % j == 0, "Newton identity must give an integer coefficient"
        c.append(-(s // j))
    return (-sum(c[i] * N[K + 1 - i] for i in range(1, K + 1))) % (K + 1), c

# ------------------------------------------------------------------ 1. the permutation (1 2)(3 4 5)
print("1. the permutation (1 2)(3 4 5): windows, the disc, what pins the next trace")
z = np.array([-1, 1, 1, np.exp(2j * np.pi / 3), np.exp(-2j * np.pi / 3)])
t = [int(round(np.sum(z ** k).real)) for k in range(12)]              # Tr P^k = #Fix(sigma^k)
check(t[:12] == [5, 0, 2, 3, 2, 0, 5, 0, 2, 3, 2, 0], f"Tr P^k = #Fix(sigma^k) = {t[:12]}")
posdef = [np.linalg.eigvalsh(toeplitz(t, K))[0] > 1e-9 for K in range(0, 7)]
check(posdef == [True, True, True, True, False, False, False],
      "window matrix T_K positive definite for K <= 3, singular from K = 4 (four distinct atoms)")

pinned = {}
for K in range(1, 4):
    c, r = disc(t, K)
    check(abs(c - levinson_centre(t, K)) < 1e-12, f"K={K}: disc centre = Levinson one-step predictor = {c:.4f}")
    dr = np.linalg.det(toeplitz(t, K)) / np.linalg.det(toeplitz(t, K - 1))
    check(abs(r - dr) < 1e-9, f"K={K}: disc radius = det T_K / det T_(K-1) = {r:.4f}")
    xs = np.linspace(c - 1.5 * r, c + 1.5 * r, 61)
    ok = all((np.linalg.eigvalsh(toeplitz(t[:K + 1] + [x], K + 1))[0] >= -1e-9) == (abs(x - c) <= r + 1e-9) for x in xs)
    check(ok, f"K={K}: T_(K+1)(x) >= 0 exactly for |x - c| <= r (61 sample points)")
    check(abs(t[K + 1] - c) <= r + 1e-9, f"K={K}: true t_(K+1) = {t[K+1]} lies in [{c-r:.3f}, {c+r:.3f}]")
    for x in (c - r, c + r):
        Tb = toeplitz(t[:K + 1] + [x], K + 1); ev, V = np.linalg.eigh(Tb)
        rts = np.roots(V[:, 0][::-1])
        check(abs(ev[0]) < 1e-8 and np.all(abs(abs(rts) - 1) < 1e-6),
              f"K={K}: boundary point x = {x:.4f} gives a singular window; kernel roots on the unit circle (K+1 = {K+1} atoms)")
    pis, eps, _ = pisarenko_next(t, K)
    check(abs(pis - c) <= r + 1e-9, f"K={K}: Pisarenko extension {pis:.4f} (eps = {eps:.3f}) lies inside the disc")
    res, coef = newton_residue(t, K)
    check(t[K + 1] % (K + 1) == res, f"K={K}: Newton congruence t_(K+1) = {res} mod {K+1} holds (true {t[K+1]})")
    cands = [x for x in range(0, 6) if abs(x - c) <= r + 1e-9 and x % (K + 1) == res]
    pinned[K] = cands
    print(f"       K={K}: disc [{c-r:.3f}, {c+r:.3f}], Pisarenko {pis:.3f}, residue {res} mod {K+1}, integers >= 0 in disc with that residue: {cands}")
check(pinned[1] == [0, 2, 4] and pinned[2] == [0, 3] and pinned[3] == [2],
      "disc + nonnegativity + Newton congruence: 3 candidates at K=1, 2 at K=2, pinned to the truth (2) at K=3")
pis3, eps3, _ = pisarenko_next(t, 3)
check(abs(pis3 + 0.5) < 1e-9 and t[4] == 2, "K=3: Pisarenko alone predicts -0.5 (repeated atom at 1), truth is 2")

# ------------------------------------------------------------------ 2. singular windows
print("2. singular windows: the kernel recurrence determines every later trace")
for K in (4, 5):
    T = toeplitz(t, K); ev, V = np.linalg.eigh(T); k = V[:, 0]
    check(abs(ev[0]) < 1e-9, f"K={K}: window singular, min eigenvalue {ev[0]:.1e}")
    w = np.array([t[K + 1 - j] for j in range(1, K + 1)])
    pred = -(k[1:] @ w) / k[0]
    check(abs(pred - t[K + 1]) < 1e-9, f"K={K}: kernel recurrence gives t_(K+1) = {pred:.6f} = truth {t[K+1]}")
    if K == 4:
        rts = sorted(np.roots(k[::-1]), key=lambda x: np.angle(x))
        target = sorted(np.array([-1, 1, np.exp(2j*np.pi/3), np.exp(-2j*np.pi/3)]), key=lambda x: np.angle(x))
        check(np.allclose(rts, target, atol=1e-8), "K=4: kernel polynomial roots = the four distinct eigenvalues of P")

# ------------------------------------------------------------------ 3. the Petersen graph
print("3. the Petersen graph (q = 2): the disc in rescaled units and in count units")
q, V_, E_ = 2, 10, 15
th1 = np.arccos(1 / (2 * np.sqrt(2)))                                 # lambda = 1: mu = (1 +- i sqrt 7)/2
th2 = 3 * np.pi / 4                                                   # lambda = -2: mu = -1 +- i
tp = [10 * np.cos(k * th1) + 8 * np.cos(k * th2) for k in range(12)]  # rescaled retained traces, 18 atoms
Np = [int(round(q ** (k / 2) * tp[k] + q ** k + 1 + (E_ - V_) * (1 + (-1) ** k))) for k in range(12)]
check(Np[:8] == [30, 0, 0, 0, 0, 120, 120, 0], f"Tr B^k = {Np[:8]} (Petersen: girth 5, 12 pentagons, 10 hexagons)")
check(all(abs(q ** (k / 2) * tp[k] + q ** k + 1 + (E_ - V_) * (1 + (-1) ** k) - Np[k]) < 1e-9 for k in range(12)),
      "rescaled traces reproduce integer counts exactly for k <= 11")
posdef = [np.linalg.eigvalsh(toeplitz(tp, K))[0] > 1e-9 for K in range(0, 6)]
check(posdef == [True, True, True, True, False, False], "window positive definite for K <= 3, singular from K = 4 (four distinct atoms)")
for K in range(1, 4):
    c, r = disc(tp, K)
    check(abs(tp[K + 1] - c) <= r + 1e-9, f"K={K}: true rescaled t_(K+1) = {tp[K+1]:.4f} in [{c-r:.3f}, {c+r:.3f}]")
    rN = q ** ((K + 1) / 2) * r
    cN = q ** ((K + 1) / 2) * c + q ** (K + 1) + 1 + (E_ - V_) * (1 + (-1) ** (K + 1))
    res, _ = newton_residue(Np, K)
    check(Np[K + 1] % (K + 1) == res, f"K={K}: Newton congruence N_(K+1) = {res} mod {K+1} holds (true {Np[K+1]})")
    cands = [x for x in range(0, int(cN + rN) + 2) if abs(x - cN) <= rN + 1e-9 and x % (K + 1) == res]
    check(rN > 1 and len(cands) > 1, f"K={K}: disc radius {r:.3f} rescaled, {rN:.2f} in counts; {len(cands)} admissible integers, not pinned")
    print(f"       K={K}: counts disc [{cN-rN:.2f}, {cN+rN:.2f}], truth N_{K+1} = {Np[K+1]}, candidates {cands}")

print(f"\nall {CHECKS} checks passed")
