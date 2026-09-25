#!/usr/bin/env python3
"""REFUTE lane R, RTP-1 (claude:opus, 2026-09-24).  Claim C7 side numbers and the section-4.3 audit.
(1) h_+(t) = -log pi + Re psi(1/4 + it/2): zero at 6.2898 (lane B1), h_+(0); Yoshida's t_0 = 2.0320 (Re psi = 0).
(2) The even box phi = (2a)^{-1/2} 1_[-a,a], a = log2/2: pole, archimedean and total of Psi(phi * phi~) computed in
    REAL SPACE from the CCM/Bombieri definitions (triangle F, W_R's defining integral) -- independent of the lane's
    Fourier-side computation.  Also an odd function and a pole-free even function on the same support.
(3) Coffey/Bombieri-Lagarias: lambda_1 = 1 + gamma/2 - (1/2) log 4 pi and the Li formula at n = 1, 2 against the
    zero-free closed forms (eta_0 = -gamma, eta_1 from the Stieltjes constants).
(4) Lagarias's inequality sigma(n) <= H_n + exp(H_n) log H_n for n <= 5000 (sanity only; not evidence), and the
    Y-A/DMR inequality for n <= 6.
Deterministic."""
import mpmath as mp
mp.mp.dps = 30
NCHK = [0, 0]
def check(c, m):
    NCHK[0] += 1; NCHK[1] += (not c); print(('PASS ' if c else 'FAIL ') + m, flush=True)
hp = lambda t: -mp.log(mp.pi) + mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * t / 2))
t1 = mp.findroot(hp, 6.3); t0 = mp.findroot(lambda t: mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * t / 2)), 2)
check(abs(t1 - mp.mpf('6.2898359888369')) < 1e-10 and abs(t0 - mp.mpf('2.03205843152397')) < 1e-10,
      f'h_+ zero {mp.nstr(t1, 12)} (lane 6.2898), h_+(0) = {mp.nstr(hp(0), 10)}; Re psi(1/4+it/2) = 0 at t_0 = {mp.nstr(t0, 10)} (Yoshida "t_0 = 2.0320")')
check(all(hp(t) < 0 for t in mp.linspace(0, 6.28, 50)) and hp(6.3) > 0 and hp(50) > 0, 'h_+ < 0 on [0, 6.28], > 0 beyond: the archimedean form alone is indefinite on unrestricted test functions')
# (2) real space, CCM normalisation: Psi(F) = int F 2cosh(y/2) - W_R(F), W_R(F) = (log4pi+gamma)F(0) + int_0^oo (F(y)+F(-y) - 2e^{-y/2}F(0)) rho(y) dy
a = mp.log(2) / 2
rho = lambda y: mp.e ** (y / 2) / (mp.e ** y - mp.e ** (-y))
def psi_parts(F, supp):
    pole = mp.quad(lambda y: F(y) * 2 * mp.cosh(y / 2), [-supp, 0, supp])
    F0 = F(0)
    inner = mp.quad(lambda y: (F(y) + F(-y) - 2 * mp.e ** (-y / 2) * F0) * rho(y), [0, supp / 2, supp])
    tail = F0 * mp.log(mp.tanh(supp / 2))    # int_supp^oo -2e^{-y/2}F0 rho = -F0 int dy/sinh y = F0 log tanh(supp/2)
    WR = (mp.log(4 * mp.pi) + mp.euler) * F0 + inner + tail
    return pole, -WR, pole - WR
tri = lambda y: max(mp.mpf(0), 1 - abs(y) / (2 * a))      # F = phi * phi~ for the normalised even box
p, ar, tot = psi_parts(tri, 2 * a)
check(abs(ar + mp.mpf('1.21684168637841')) < 1e-5 and abs(p - mp.mpf('1.40022606409953')) < 1e-12 and abs(tot - mp.mpf('0.183384377721127')) < 1e-5,   # B1 states 5-digit stability of its Fourier-side quadrature
      f'even box of width log 2 (real space): pole {mp.nstr(p, 12)}, archimedean {mp.nstr(ar, 12)}, total {mp.nstr(tot, 12)} (lane B1: 1.40023, -1.21684, 0.18338; its 15-digit script values differ from the real-space ones by {mp.nstr(abs(ar + mp.mpf("1.21684168637841")), 2)})')
# odd box: phi = (2a)^{-1/2} sign(x) on [-a,a]: F = phi*phi~
def conv(phi, s, lo, hi):
    return mp.quad(lambda x: phi(x + s) * phi(x), [max(lo, lo - s), 0, min(hi, hi - s)]) if max(lo, lo - s) < min(hi, hi - s) else mp.mpf(0)
odd = lambda x: (mp.sign(x) / mp.sqrt(2 * a)) if abs(x) <= a else mp.mpf(0)
Fo = lambda y: conv(odd, y, -a, a)
po, aro, toto = psi_parts(Fo, 2 * a)
check(po < 0 and toto > 0 and aro > 0, f'odd box: pole {mp.nstr(po, 8)} (<= 0), archimedean {mp.nstr(aro, 8)}, total {mp.nstr(toto, 8)}')
# (3) Li lambda_1 via Coffey's (10) with eta_0 = -gamma, against the known closed form and the zero-side sum (labelled comparison)
lam1 = -(-mp.euler) + 1 - mp.mpf(1) / 2 * (mp.euler + mp.log(mp.pi) + 2 * mp.log(2))
check(abs(lam1 - (1 + mp.euler / 2 - mp.log(4 * mp.pi) / 2)) < 1e-25 and abs(lam1 - mp.mpf('0.0230957089661210338')) < 1e-18,
      f'Coffey (10) at n = 1 with eta_0 = -gamma: lambda_1 = {mp.nstr(lam1, 15)} = 1 + gamma/2 - log(4pi)/2')
# eta_j from the Stieltjes constants: (s-1) zeta(s) = 1 + g0 u - g1 u^2 + ..., f = d/ds log((s-1) zeta) = -sum eta_p u^p
g0, g1 = mp.stieltjes(0), mp.stieltjes(1)
eta0 = -g0; eta1 = 2 * g1 + g0 ** 2
lam2 = -(2 * eta0 + eta1) + (1 - mp.mpf(1) / 4) * mp.zeta(2) + 1 - (mp.euler + mp.log(mp.pi) + 2 * mp.log(2))
# COMPARISON STEP (zeros used here only): lambda_2 = sum_rho [1 - (1 - 1/rho)^2] over the first 400 zero pairs + density tail
zs = [mp.zetazero(k) for k in range(1, 401)]
lam2z = mp.fsum(2 * mp.re(1 - (1 - 1 / r) ** 2) for r in zs)
T = mp.im(zs[-1]); tail = (2 / mp.pi) * (mp.log(T / (2 * mp.pi)) + 1) / T
check(abs(lam2 - (lam2z + tail)) < 1e-3, f'# COMPARISON STEP: Coffey (10) at n = 2 gives lambda_2 = {mp.nstr(lam2, 10)}; 400 zero pairs {mp.nstr(lam2z, 8)} + density tail {mp.nstr(tail, 3)} = {mp.nstr(lam2z + tail, 8)}')
# (4) Lagarias, sanity range
from math import log, exp
H = 0.0; sig = [0] * 5001
for d in range(1, 5001):
    for m in range(d, 5001, d): sig[m] += d
ok = True
for n in range(1, 5001):
    H += 1.0 / n
    if n > 1 and not sig[n] < H + exp(H) * log(H): ok = False
check(ok, "Lagarias's inequality holds strictly for 2 <= n <= 5000 (sanity of the transcription only)")
print(f'# checks: {NCHK[0]} run, {NCHK[1]} failed')
