#!/usr/bin/env python3
"""Independent checks of astra-proofs T1.1-T1.3, T2.1-T2.3.
Reviewer claude:opus, 2026-09-12.  Written from the statements only,
not from scripts/weil_positivity.py."""
import numpy as np
rng = np.random.default_rng(20260912)

def nu(Z, L):
    """nu_l for l=-L..L from a multiset Z of z=mu/r (list, multiplicity by repetition)."""
    out = {}
    for l in range(0, L + 1):
        out[l] = sum(z ** l if l > 0 else 1.0 + 0j for z in Z)
    for l in range(1, L + 1):
        out[-l] = np.conj(out[l])
    return out

def toeplitz(nud, L):
    idx = np.arange(L + 1)
    K = idx[:, None] - idx[None, :]
    v = np.array([nud[k] for k in range(-L, L + 1)], dtype=complex)
    return v[K + L]

def mineig(Z, L):
    M = toeplitz(nu(Z, L), L)
    return np.linalg.eigvalsh((M + M.conj().T) / 2).min()

print("=" * 78)
print("T1.1  Poisson kernel: (1/2pi) int e^{ik th} P_z(th) dth  ==  z^{[k]}")
print("=" * 78)
th = np.linspace(0, 2 * np.pi, 20001)[:-1]; dth = th[1] - th[0]
worst = 0.0
for z in [0.0, 0.7, -0.3 + 0.5j, 0.95j, 0.2 - 0.8j]:
    P = (1 - abs(z) ** 2) / np.abs(1 - z * np.exp(-1j * th)) ** 2
    mass = (P.sum() * dth) / (2 * np.pi)
    for k in range(-4, 5):
        num = (np.exp(1j * k * th) * P).sum() * dth / (2 * np.pi)
        exact = z ** k if k >= 0 else np.conj(z) ** (-k)
        worst = max(worst, abs(num - exact))
    print(f"  z={z!s:>12}  mass/2pi={mass:.10f}  min P={P.min():.6f}")
print(f"  max |numeric coeff - z^[k]| over k=-4..4 : {worst:.2e}   (T1.1 orientation OK)")

print()
print("=" * 78)
print("T1.1  single mode identity: sum_{l,m} c_l bar c_m z^{[l-m]} == Poisson integral / |f(z)|^2")
print("=" * 78)
c = rng.normal(size=6) + 1j * rng.normal(size=6)
for z in [0.0, 0.6 - 0.2j, np.exp(0.9j), 0.999 * np.exp(2.1j)]:
    lhs = sum(c[l] * np.conj(c[m]) * (z ** (l - m) if l >= m else np.conj(z) ** (m - l))
              for l in range(6) for m in range(6))
    f = sum(c[l] * np.exp(1j * l * th) for l in range(6))
    if abs(z) < 1:
        rhs = (np.abs(f) ** 2 * (1 - abs(z) ** 2) / np.abs(1 - z * np.exp(-1j * th)) ** 2).sum() * dth / (2 * np.pi)
    else:
        rhs = abs(sum(c[l] * z ** l for l in range(6))) ** 2
    print(f"  z={z!s:>22}  lhs={lhs.real:+.10f}{lhs.imag:+.2e}i   rhs={rhs.real:+.10f}   diff={abs(lhs-rhs):.2e}")

print()
print("=" * 78)
print("T1.3  positive definite  <=>  |mu| <= r  (random multisets, incl. zeros and Jordan)")
print("=" * 78)
bad = 0
for trial in range(200):
    d = rng.integers(1, 6)
    Z = []
    for _ in range(d):
        mode = rng.integers(0, 4)
        if mode == 0: Z.append(0.0 + 0j)
        elif mode == 1: Z.append(rng.uniform(0, 1) * np.exp(2j * np.pi * rng.uniform()))
        elif mode == 2: Z.append(np.exp(2j * np.pi * rng.uniform()))
        else: Z.append(rng.uniform(1.06, 1.6) * np.exp(2j * np.pi * rng.uniform()))
    R = max(abs(z) for z in Z)
    inside = R <= 1 + 1e-12
    # escalate L until the verdict is clear
    verdict = None
    for L in (10, 40, 160, 400):
        me = mineig(Z, L)
        scale = max(1.0, max(abs(nu(Z, L)[l]) for l in range(L + 1)))
        if me < -1e-9 * scale:
            verdict = False; break
    if verdict is None: verdict = True
    if verdict != inside:
        bad += 1
        print(f"  MISMATCH R={R:.4f} inside={inside} PSD={verdict}  Z={Z}")
print(f"  200 random multisets: mismatches between 'PSD for all tested L' and '|mu|<=r' : {bad}")
print("  (a mode just outside the circle needs large L: finite-L masking, as reported by the other agent)")
for eps in (0.2, 0.05, 0.02, 0.01):
    Z = [(1 + eps) * np.exp(0.7j), (1 + eps) * np.exp(-0.7j), 0.5, 0.3j]
    firstL = None
    for L in (5, 10, 20, 40, 80, 160, 320, 640, 1280):
        if mineig(Z, L) < -1e-9:
            firstL = L; break
    print(f"    R = 1+{eps:<6}  first L with a negative Toeplitz eigenvalue: {firstL}")

print()
print("=" * 78)
print("T1.2  two-point bound |nu_l| <= nu_0 on positive definite sequences")
print("=" * 78)
viol = 0
for trial in range(300):
    Z = [np.exp(2j * np.pi * rng.uniform()) * rng.uniform(0, 1) for _ in range(rng.integers(1, 6))]
    nud = nu(Z, 30)
    if max(abs(nud[l]) for l in range(1, 31)) > nud[0].real + 1e-9: viol += 1
print(f"  violations of |nu_l| <= nu_0 among 300 in-disk multisets: {viol}")

print()
print("=" * 78)
print("T2.1 / T2.2 / T2.3")
print("=" * 78)
# T2.1: W = M on J-invariant multisets (J(mu) = r^2/conj(mu), r = 1 here)
def Wform(Z, c):
    L = len(c) - 1; nud = nu(Z, L)
    return sum(c[l] * np.conj(c[m]) * nud[l - m] for l in range(L + 1) for m in range(L + 1))
def Mform(Z, c):
    f = lambda w: sum(c[l] * w ** l for l in range(len(c)))
    return sum(f(z) * np.conj(f(1 / np.conj(z))) for z in Z)
worst = 0.0
for trial in range(200):
    Z = []
    for _ in range(rng.integers(1, 4)):
        z = rng.uniform(0.2, 2.5) * np.exp(2j * np.pi * rng.uniform())
        Z += [z, 1 / np.conj(z)]          # J-orbit
    for _ in range(rng.integers(0, 3)):
        Z.append(np.exp(2j * np.pi * rng.uniform()))   # J-fixed
    c = rng.normal(size=5) + 1j * rng.normal(size=5)
    worst = max(worst, abs(Wform(Z, c) - Mform(Z, c)))
print(f"  T2.1(a)  max |W(c) - M(c)| over 200 J-invariant multisets : {worst:.2e}")

# T2.2: Lagrange interpolation makes the whole form negative on one off-circle orbit
print("  T2.2  interpolation construction (f=1 at z, -1 at j(z), 0 elsewhere):")
for trial in range(5):
    z0 = rng.uniform(1.2, 2.0) * np.exp(2j * np.pi * rng.uniform())
    Z = [z0, 1 / np.conj(z0), np.exp(1.1j), np.exp(-1.1j)]
    Z = Z + [z0, 1 / np.conj(z0)]           # multiplicity 2 on the chosen orbit
    pts = []
    for z in Z:
        if not any(abs(z - p) < 1e-12 for p in pts): pts.append(z)
    vals = [1.0 if abs(p - z0) < 1e-12 else (-1.0 if abs(p - 1 / np.conj(z0)) < 1e-12 else 0.0) for p in pts]
    # Lagrange coefficients in the monomial basis
    coef = np.zeros(len(pts), dtype=complex)
    for i, p in enumerate(pts):
        num = np.array([1.0 + 0j])
        den = 1.0 + 0j
        for h, ph in enumerate(pts):
            if h == i: continue
            num = np.convolve(num, np.array([-ph, 1.0 + 0j]))
            den *= (p - ph)
        coef += vals[i] * num / den
    print(f"    orbit modulus {abs(z0):.4f}:  W(c) = {Wform(Z, coef).real:+.6f} (predicted -2*mult = -4)"
          f"   imag {Wform(Z, coef).imag:+.1e}")

# T2.3: reciprocal-only example A = {2i, -i/2}, r = 1
Z = [2j, -0.5j]; c = np.array([1.0 + 0j, 1.0 + 0j])
nud = nu(Z, 1)
print(f"  T2.3  A={{2i,-i/2}}: nu_1 = {nud[1]}, nu_-1 = {nud[-1]}, sum z^-1 = {sum(1/z for z in Z)}")
print(f"        W(1+z) = {Wform(Z, c)}   M(1+z) = {Mform(Z, c)}   (astra: W=4, M=4+3i)")
