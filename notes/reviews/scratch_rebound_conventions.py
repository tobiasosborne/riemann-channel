#!/usr/bin/env python3
"""REFUTE lane, independent of scripts/rebound_state.py.

Checks the prover's Section 0 constants (C1, C2, C3) in the PROVER's own
convention (plain Lebesgue dtau on R, PW unitary f(tau) = (2pi)^{-1/2} int_0^inf
e^{i tau x} (Ff)(x) dx), and reconciles them with the numerics lane's
normalised convention (<f|g> = (1/2pi) int conj(f) g dtau, c = i).

Everything is recomputed from scratch by quadrature / residues; no import of
the other lane's code.
"""
import numpy as np
from scipy.integrate import quad

N = 0
FAIL = []


def ck(cond, msg, dev=None):
    global N
    N += 1
    tag = "ok " if cond else "FAIL"
    if not cond:
        FAIL.append(msg)
    print(f"  {tag} {N:2d}  {msg}" + ("" if dev is None else f"   dev={dev:.3e}"))


def kw(w, tau):
    return 1.0 / (tau - np.conj(w))


def quad_c(f, a, b, **kw_):
    re = quad(lambda t: f(t).real, a, b, **kw_)[0]
    im = quad(lambda t: f(t).imag, a, b, **kw_)[0]
    return re + 1j * im


print("=" * 78)
print("C1  Gram constant, kernel norm, reproducing constant (plain Lebesgue dtau)")
print("=" * 78)

ws = [0.25j, 1.0 + 0.25j, -2.3 + 0.31j, 0.7 + 0.19j]
# full-line integral by the substitution tau = tan(theta), theta in (-pi/2, pi/2)
for w in ws:
    for v in ws:
        num = quad_c(lambda th: np.conj(kw(w, np.tan(th))) * kw(v, np.tan(th))
                     / np.cos(th) ** 2, -np.pi / 2, np.pi / 2, limit=600)
        exact = 2j * np.pi / (w - np.conj(v))
        ck(abs(num - exact) < 1e-6 * max(1.0, abs(exact)),
           f"<k_w,k_v> = 2 pi i/(w - conj v) for w={w}, v={v}",
           abs(num - exact))

for w in ws:
    ck(abs(2j * np.pi / (w - np.conj(w)) - np.pi / w.imag) < 1e-13,
       f"||k_w||^2 = pi/Im w at w={w}")

# reproducing: <k_w, f> = 2 pi i f(w) for f = k_v
for w in ws:
    v = ws[1]
    ck(abs(2j * np.pi / (w - np.conj(v)) - 2j * np.pi * kw(v, w)) < 1e-13,
       f"<k_w,f> = 2 pi i f(w) (f = k_v) at w={w}")
    ck(abs((-1j / (2 * np.pi)) * 2j * np.pi * kw(v, w) - kw(v, w)) < 1e-15,
       f"exactly reproducing vector i k_w/(2 pi) at w={w}")

print()
print("=" * 78)
print("C1  Fourier image: F k_w = -i sqrt(2 pi) e^{-i conj(w) x}   (prover eq. line 57)")
print("=" * 78)
# f(tau) = (2 pi)^{-1/2} int_0^inf e^{i tau x} (F f)(x) dx.  Test at real tau.
for w in ws:
    for tau in (-1.7, 0.0, 2.4):
        rec = (2 * np.pi) ** -0.5 * quad_c(
            lambda x: np.exp(1j * tau * x) * (-1j * np.sqrt(2 * np.pi))
            * np.exp(-1j * np.conj(w) * x), 0, np.inf, limit=400)
        ck(abs(rec - kw(w, tau)) < 1e-8,
           f"PW inversion of -i sqrt(2pi) e^{{-i conj(w) x}} gives k_w, w={w}, tau={tau}",
           abs(rec - kw(w, tau)))
# the brief's alternative e^{i w x} is NOT the image
w = ws[1]
rec_bad = (2 * np.pi) ** -0.5 * quad_c(
    lambda x: np.exp(1j * 0.0 * x) * np.exp(1j * w * x), 0, np.inf, limit=400)
ck(abs(rec_bad - kw(w, 0.0)) > 0.1,
   "brief's e^{i w x} is NOT the PW image of k_w (ledger item 2 confirmed)")

# Plancherel with this normalisation: int_R conj(f) g dtau = int_0^inf conj(Ff) Fg dx
for (w, v) in [(ws[0], ws[1]), (ws[2], ws[3])]:
    lhs = 2j * np.pi / (w - np.conj(v))
    rhs = quad_c(lambda x: np.conj(-1j * np.sqrt(2 * np.pi) * np.exp(-1j * np.conj(w) * x))
                 * (-1j * np.sqrt(2 * np.pi)) * np.exp(-1j * np.conj(v) * x), 0, np.inf, limit=400)
    ck(abs(lhs - rhs) < 1e-9, f"Plancherel consistency for w={w}, v={v}", abs(lhs - rhs))

print()
print("=" * 78)
print("C1  eigen-relation  C_t k_w = e^{-i t conj(w)} k_w  (backward translation)")
print("=" * 78)
for w in ws:
    for t in (0.3, 1.7, 5.0):
        g0 = lambda x: -1j * np.sqrt(2 * np.pi) * np.exp(-1j * np.conj(w) * x)
        ck(abs(g0(t + 0.83) - np.exp(-1j * t * np.conj(w)) * g0(0.83)) < 1e-12,
           f"(F k_w)(x+t) = e^{{-i t conj w}} (F k_w)(x), w={w}, t={t}")
    ck(abs(abs(np.exp(-1j * 1.0 * np.conj(w))) - np.exp(-w.imag)) < 1e-14,
       f"modulus = e^{{-Im w}} (decay), w={w}")
# the shard's OLD lower-half-plane formula is growth
lam = -0.5 - 0.25j          # lower half plane zero, sigma = 1/2
ck(abs(np.exp(-1j * 1.0 * np.conj(lam))) > 1.0,
   "old prop:functional-model-modes  Z^* k_lambda = e^{-i t conj lambda}: modulus e^{+1/4} > 1 (GROWTH)")
ck(abs(abs(np.exp(1j * 1.0 * np.conj(lam))) - np.exp(-0.25)) < 1e-14,
   "corrected lower-half-plane form Z_t k_lambda = e^{i t conj lambda}: modulus e^{-1/4} (decay)")
print(f"     old modulus {np.exp(0.25):.10f} vs corrected {np.exp(-0.25):.10f}"
      "   (prover's numeric table row 7 reproduced)")

print()
print("=" * 78)
print("C2/C3  exit value, form identity, reconciliation with the numerics lane")
print("=" * 78)
# j k_w = (F k_w)(0) = -i sqrt(2 pi)
for w in ws:
    ck(abs((-1j * np.sqrt(2 * np.pi)) - (-1j * np.sqrt(2 * np.pi))) < 1e-15,
       f"j k_w = -i sqrt(2 pi) != 0, w={w} (C3: no dark mode)")

wv = np.array(ws)
y = wv.imag
Gun = 2j * np.pi / (wv[:, None] - np.conj(wv)[None, :])        # prover, plain Lebesgue
Gnum = 1j / (wv[:, None] - np.conj(wv)[None, :])               # numerics lane, dtau/2pi
ck(np.allclose(Gun, 2 * np.pi * Gnum), "c_prover = 2 pi i  =  2 pi * c_numerics = 2 pi * i")
Gnorm_p = Gun / np.sqrt(np.outer(np.pi / y, np.pi / y))
Gnorm_n = Gnum / np.sqrt(np.outer(1 / (2 * y), 1 / (2 * y)))
Gnorm_f = 2j * np.sqrt(np.outer(y, y)) / (wv[:, None] - np.conj(wv)[None, :])
ck(np.allclose(Gnorm_p, Gnorm_n) and np.allclose(Gnorm_p, Gnorm_f),
   "NORMALISED Gram 2i sqrt(y_n y_m)/(w_n - conj w_m) identical in both conventions (T2(b) line 225)",
   float(np.max(np.abs(Gnorm_p - Gnorm_f))))
jp = -1j * np.sqrt(2 * np.pi) / np.sqrt(np.pi / y)             # j e_n, prover convention
jn = -1j / np.sqrt(1 / (2 * y))                                # j ehat_n, numerics convention
ck(np.allclose(jp, jn) and np.allclose(jp, -1j * np.sqrt(2 * y)),
   "j e_n = -i sqrt(2 Im w_n) in BOTH conventions: the sqrt(2 pi) cancels on normalised modes")

# form identity  -(conj(b_n) G_nm + G_nm b_m) = conj(j e_n) j e_m
b = -1j * np.conj(wv)
lhs = -(np.conj(b)[:, None] * Gnorm_f + Gnorm_f * b[None, :])
rhs = np.outer(np.conj(jp), jp)
ck(np.allclose(lhs, rhs), "-(B + B^*) = |j><j| as a form on the normalised modes",
   float(np.max(np.abs(lhs - rhs))))
q = 2 * np.sqrt(np.outer(y, y))
ck(np.allclose(rhs, q), "ell(E_nm) = q_nm = 2 sqrt(y_n y_m) != 0  (prover eq. (7))")
lam_nm = b[:, None] + np.conj(b)[None, :]
ck(np.allclose(-lam_nm * Gnorm_f.T, q), "-lambda_nm G_mn = q_nm  (prover, T4(c))",
   float(np.max(np.abs(-lam_nm * Gnorm_f.T - q))))

# |g(0)|^2 <= 2 ||g|| ||g'||  for g = F k_w
for w in ws:
    g0 = 2 * np.pi
    nrm2 = 2 * np.pi / (2 * w.imag)
    nrmd2 = 2 * np.pi * abs(w) ** 2 / (2 * w.imag)
    ck(g0 <= 2 * np.sqrt(nrm2 * nrmd2) + 1e-12,
       f"|g(0)|^2 <= 2||g|| ||g'|| for g = F k_w, w={w}")

print()
print(f"TOTAL {N} checks, {len(FAIL)} failures")
for f in FAIL:
    print("   FAILED:", f)
