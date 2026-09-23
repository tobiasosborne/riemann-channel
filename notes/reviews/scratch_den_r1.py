"""REFUTE lane for notes/deninger-cmps/reformulation.md, Proposition R1 and D2/D3.
Independent: imports nothing from scripts/.  Run from the repository root.

Checks
 A. Deninger's explicit formula on R^{>0} in Deninger time t_D  [D05:874-880], [D07:432-436]:
      Phi(0) + Phi(1) - sum_rho Phi(rho) = sum_{p^k} log p phi(k log p) + int phi(t)/(1-e^{-2t}) dt
    with Gaussian test functions (closed-form Phi), 3000 zeros; plus five wrong variants that must fail.
 B. R1(b) in notebook time t = 2 t_D:  1 + e^{-t/2} - Tr_d Z(t) = 2 P_+(t) + sum_{k>=0} e^{-(k+1/2)t},
    Tr_d Z(t) = sum_rho e^{-conj(rho) t/2} (def:distributional-trace), and prop:ringnorm-trace;
    plus the factor-2 and support variants that must fail.
 C. Pointwise identities of the proof of R1(b).
 D. Divisor bookkeeping of R1(d) with mpmath: zeta-hat, Gamma_R, Gamma_C = Gamma_R(s)Gamma_R(s+1).
 E. Deninger's Proposition 2.1 [D05:204-215, 286-296]: the archimedean Euler factor is a zeta-regularised
    determinant on R[e^{-2y}] (real) / R[e^{-y}] (complex): the bosonic ladder is Deninger's own, byte-citable.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 30
ok = 0
fail = 0


def check(name, cond, info=''):
    global ok, fail
    if cond:
        ok += 1
        print(f'  PASS {name} {info}')
    else:
        fail += 1
        print(f'  FAIL {name} {info}')


gam = np.load('data/zeros3000.npy')          # imaginary parts, gamma > 0
# primes up to e^{8}
def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0]
P = primes_upto(20000)


def gauss(t, t0, s):
    return np.exp(-(t - t0) ** 2 / (2 * s * s))


def Phi_gauss(rho, t0, s):
    """int exp(-(t-t0)^2/2s^2) e^{t rho} dt  (closed form, complex rho)."""
    return s * np.sqrt(2 * np.pi) * np.exp(t0 * rho + s * s * rho * rho / 2)


def zero_sum(t0, s, scale=1.0, conj_half=False):
    """sum over rho = 1/2 +- i gamma of int phi(t) e^{t * f(rho)} dt."""
    rho = 0.5 + 1j * gam
    if conj_half:          # notebook: e^{-conj(rho) t/2}
        a1, a2 = -np.conj(rho) / 2, -rho / 2      # rho and its conjugate
    else:
        a1, a2 = rho, np.conj(rho)
    return np.sum(Phi_gauss(a1, t0, s) + Phi_gauss(a2, t0, s))


def prime_sum(t0, s, stretch=1.0, weight='deninger'):
    tot = 0.0
    for p in P:
        lp = np.log(p)
        k = 1
        while k * lp * stretch < t0 + 40 * s:
            t = k * lp * stretch
            if weight == 'deninger':
                w = lp
            elif weight == 'notebook':          # 2 Lambda(n)/n at t = 2 log n
                w = 2 * lp / p ** k
            elif weight == 'notebook_no2':
                w = lp / p ** k
            tot += w * gauss(t, t0, s)
            k += 1
    return tot


def quad(f, a, b, n=200001):
    t = np.linspace(a, b, n)
    y = f(t)
    return np.trapezoid(y, t)


print('A. Deninger explicit formula on R^{>0}, Deninger time')
for (t0, s) in [(1.2, 0.05), (2.0, 0.03), (2.9, 0.02), (0.8, 0.06)]:
    lhs = Phi_gauss(0.0, t0, s) + Phi_gauss(1.0, t0, s) - zero_sum(t0, s)
    lo, hi = max(t0 - 14 * s, 1e-3), t0 + 14 * s
    arch = quad(lambda t: gauss(t, t0, s) / (1 - np.exp(-2 * t)), lo, hi)
    rhs = prime_sum(t0, s) + arch
    err = abs(lhs - rhs)
    check(f'A t0={t0} s={s}', abs(lhs.imag) < 1e-9 and err < 1e-7 * max(1, abs(rhs)),
          f'lhs={lhs.real:.10f} rhs={rhs:.10f} |diff|={err:.2e}')
    # wrong variants
    arch_c = quad(lambda t: gauss(t, t0, s) / (1 - np.exp(-t)), lo, hi)     # kappa = -1
    check(f'A-wrong kappa=-1 fails t0={t0}', abs(lhs - (prime_sum(t0, s) + arch_c)) > 1e-4)
    check(f'A-wrong no H^0 term fails t0={t0}', abs(lhs - Phi_gauss(0.0, t0, s) - rhs) > 1e-4)

print('B. R1(b) in notebook time t = 2 t_D, and prop:ringnorm-trace')
for (t0, s) in [(2.4, 0.06), (4.0, 0.04), (5.5, 0.03)]:
    lo, hi = max(t0 - 14 * s, 1e-3), t0 + 14 * s
    one = s * np.sqrt(2 * np.pi)
    lhs = one + Phi_gauss(-0.5, t0, s) - zero_sum(t0, s, conj_half=True)
    arch = quad(lambda t: gauss(t, t0, s) / (2 * np.sinh(t / 2)), lo, hi)
    rhs = prime_sum(t0, s, stretch=2.0, weight='notebook') + arch
    check(f'B R1(b) t0={t0} s={s}', abs(lhs - rhs) < 1e-7 * max(1, abs(rhs)),
          f'lhs={lhs.real:.10f} rhs={rhs:.10f}')
    # prop:ringnorm-trace: Tr_d Z = 1 - 2P_+ - e^{-t/2}/(e^t - 1)
    trz = zero_sum(t0, s, conj_half=True)
    pred = one - prime_sum(t0, s, stretch=2.0, weight='notebook') - quad(
        lambda t: gauss(t, t0, s) * np.exp(-t / 2) / (np.exp(t) - 1), lo, hi)
    check(f'B prop:ringnorm-trace t0={t0}', abs(trz - pred) < 1e-7 * max(1, abs(pred)),
          f'Tr_d Z={trz.real:.10f} pred={pred:.10f}')
    wrong = prime_sum(t0, s, stretch=2.0, weight='notebook_no2') + arch
    check(f'B-wrong weight Lambda(n)/n (no 2) fails t0={t0}', abs(lhs - wrong) > 1e-4)
    wrong2 = prime_sum(t0, s, stretch=1.0, weight='notebook') + arch
    check(f'B-wrong support t=log n fails t0={t0}', abs(lhs - wrong2) > 1e-4)

print('C. pointwise identities')
for t in [0.3, 1.0, 2.7, 6.1]:
    tD = t / 2
    a = np.exp(-tD) / (1 - np.exp(-2 * tD))
    check(f'C e^-tD/(1-e^-2tD)=1/(2sinh(t/2)) t={t}', abs(a - 1 / (2 * np.sinh(t / 2))) < 1e-13)
    s1 = sum(np.exp(-(k + 0.5) * t) for k in range(1, 400))
    check(f'C sum_{{k>=1}} e^-(k+1/2)t = e^-t/2/(e^t-1) t={t}', abs(s1 - np.exp(-t / 2) / (np.exp(t) - 1)) < 1e-13)
    jets = sum(np.exp(-2 * k * tD) for k in range(0, 800))
    check(f'C jet trace sum e^-2k tD = W_inf t={t}', abs(jets - 1 / (1 - np.exp(-2 * tD))) < 1e-12)
    # complex place: one kappa=-1 ladder = two kappa=-2 ladders shifted by one
    lhs = 1 / (1 - np.exp(-tD))
    rhs = 1 / (1 - np.exp(-2 * tD)) + np.exp(-tD) / (1 - np.exp(-2 * tD))
    check(f'C complex W = two real ladders t={t}', abs(lhs - rhs) < 1e-12)

print('D. divisor bookkeeping (mpmath)')
GR = lambda s: mp.pi ** (-s / 2) * mp.gamma(s / 2)
GC = lambda s: 2 * (2 * mp.pi) ** (-s) * mp.gamma(s)
zhat = lambda s: GR(s) * mp.zeta(s)
eps = mp.mpf('1e-12')
check('D res zeta-hat at s=1 is +1', abs(zhat(1 + eps) * eps - 1) < 1e-9)
check('D res zeta-hat at s=0 is -1 (pole of Gamma_R times zeta(0) = -1/2)', abs(zhat(eps) * eps + 1) < 1e-9)
for k in (1, 2, 3):
    v = zhat(-2 * k + eps)
    check(f'D zeta-hat finite and nonzero at s=-{2*k} (trivial zero cancels Gamma_R pole)',
          abs(v) > 1e-6 and abs(v) < 1e6, f'value {mp.nstr(v, 8)}')
    check(f'D zeta(-{2*k}) = 0', abs(mp.zeta(-2 * k)) < 1e-25)
    r = GR(-2 * k + eps) * eps
    check(f'D Gamma_R simple pole at -{2*k}', abs(r) > 1e-6 and abs(GR(-2 * k + eps) * eps * eps) < 1e-9)
for s in (mp.mpf('0.3'), mp.mpf('2.7'), mp.mpc('0.5', '3.1')):
    check(f'D Gamma_C(s) = Gamma_R(s) Gamma_R(s+1) at s={s}', abs(GC(s) - GR(s) * GR(s + 1)) < 1e-25)
for k in range(0, 5):
    r = GC(-k + eps) * eps
    check(f'D Gamma_C has a SIMPLE pole at -{k} (one pole per integer)', abs(r) > 1e-6 and abs(r * eps) < 1e-9,
          f'residue {mp.nstr(r, 8)}')

print('E. Deninger Prop 2.1: archimedean factor as regularised determinant [D05:204-215, 286-296]')
for s in (mp.mpf('0.7'), mp.mpf('3.2'), mp.mpc('1.5', '2.0')):
    # real place: spectrum of d/dy on R[e^{-2y}] is 0,-2,-4,...; det_inf((s-Theta)/2pi) = prod (s+2nu)/(2pi)
    # zeta-regularised: sum ((s/2+nu)/pi)^{-z} = pi^z zeta_H(z, s/2);  -d/dz at 0
    d = -(mp.log(mp.pi) * mp.zeta(0, s / 2) + mp.zeta(0, s / 2, derivative=1))
    det_real = mp.e ** d
    check(f'E real place det = sqrt2 pi^(s/2)/Gamma(s/2) at s={s}',
          abs(det_real - mp.sqrt(2) * mp.pi ** (s / 2) / mp.gamma(s / 2)) < 1e-20)
    dc = -(mp.log(2 * mp.pi) * mp.zeta(0, s) * (-1) + mp.zeta(0, s, derivative=1))
    # sum ((s+nu)/2pi)^{-z} = (2pi)^z zeta_H(z,s); -d/dz at 0 = -(log(2pi) zeta_H(0,s) + zeta_H'(0,s))
    dc = -(mp.log(2 * mp.pi) * mp.zeta(0, s) + mp.zeta(0, s, derivative=1))
    check(f'E complex place det = (2pi)^s/Gamma(s) at s={s}',
          abs(mp.e ** dc - (2 * mp.pi) ** s / mp.gamma(s)) < 1e-20)

print(f'\nscratch_den_r1: {ok} pass, {fail} fail')
