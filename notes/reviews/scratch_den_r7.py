"""REFUTE lane for notes/deninger-cmps/reformulation.md, Proposition R7 (and S3's normalisation).
Independent of notes/deninger-cmps/scratch_riesz.py and of scripts/.  Run from the repository root.

 1. modes w_n = -gamma_n/2 - i/4 (lower half plane, prop:functional-model-modes); pseudo-hyperbolic distance,
    the note's formula rho^2 = (d/2)^2/((d/2)^2+1/4) and rho <= d.
 2. the Gram matrix by quadrature: <k_n,k_m> = i/(conj w_n - w_m) in the LHP convention; the note's
    i/(w_n - conj w_m) (copied from 04h, where w is in the UPPER half plane) has NEGATIVE diagonal here.
 3. 1 - |<khat_a,khat_b>|^2 = rho(a,b)^2, hence sigma_min(G_N) <= 1 - sqrt(1 - rho_min(N)^2): the Riesz failure
    is already a 2x2 statement; monotone decrease of sigma_min in N is Cauchy interlacing, not evidence.
 4. reproduce the author's sigma_min list; Carleson measure test in unit boxes; truncated Carleson products.
 5. S3: the jump at p in notebook time is Z(2 log p), eigenvalue p^{-conj rho}, not p^{-conj rho/2}.
"""
import numpy as np
from scipy.integrate import quad

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


gam = np.load('data/zeros3000.npy')
w = -gam / 2 - 0.25j


def rho(a, b):
    return abs(a - b) / abs(a - np.conj(b))


d = np.diff(gam)
rr = np.array([rho(w[i], w[i + 1]) for i in range(len(w) - 1)])
check('1. formula rho^2 = (d/2)^2/((d/2)^2+1/4) on all 2999 neighbours',
      np.allclose(rr ** 2, (d / 2) ** 2 / ((d / 2) ** 2 + 0.25)))
check('1. rho <= d on all neighbours', np.all(rr <= d + 1e-15))
i0 = int(np.argmin(rr))
check('1. min neighbour rho = 0.097 (author)', abs(rr.min() - 0.097) < 5e-4,
      f'rho_min = {rr.min():.5f} at n = {i0+1}, gamma = {gam[i0]:.4f}, gap {d[i0]:.5f}')

print('2. Gram matrix convention')
k = lambda wv: (lambda x: 1 / (x - np.conj(wv)))


def ip(a, b):
    f = lambda x: k(a)(x) * np.conj(k(b)(x)) / (2 * np.pi)
    re = quad(lambda x: f(x).real, -np.inf, np.inf, limit=400)[0]
    im = quad(lambda x: f(x).imag, -np.inf, np.inf, limit=400)[0]
    return re + 1j * im


for (n, m) in ((0, 0), (0, 1), (3, 7), (10, 10)):
    val = ip(w[n], w[m])
    lhp = 1j / (np.conj(w[n]) - w[m])
    note = 1j / (w[n] - np.conj(w[m]))
    check(f'2. <k_{n},k_{m}> = i/(conj w_n - w_m) (LHP)', abs(val - lhp) < 1e-6, f'{val:.6f}')
    if n == m:
        check(f'2. note\'s i/(w_n - conj w_n) = {note.real:.3f} < 0 in the LHP convention', note.real < 0)
check('2. ||k_n||^2 = 1/(2|Im w|) = 2 under RH', abs(ip(w[5], w[5]) - 2) < 1e-6)

print('3. two-point identity and the 2x2 bound')
cf = lambda a, b: 1j / (np.conj(a) - b)          # closed form, validated by quadrature in 2.
for (n, m) in ((0, 1), (i0, i0 + 1), (100, 101), (5, 40), (2000, 2001)):
    kn = np.sqrt(abs(cf(w[n], w[n]))); km = np.sqrt(abs(cf(w[m], w[m])))
    o = abs(cf(w[n], w[m])) / (kn * km)
    check(f'3. 1 - |<khat,khat>|^2 = rho^2 for ({n},{m})', abs(1 - o * o - rho(w[n], w[m]) ** 2) < 1e-6)


def gram(N):
    ww = w[:N]
    G = 1j / (np.conj(ww)[:, None] - ww[None, :])
    dg = np.sqrt(np.real(np.diag(G)))
    return G / np.outer(dg, dg)


prev = None
author = {10: 0.40, 25: 0.23, 50: 0.13, 100: 0.075, 200: 0.040, 400: 0.016}
for N in (10, 25, 50, 100, 200, 400, 800, 1600):
    G = gram(N)
    check(f'3. G_{N} Hermitian positive definite', np.allclose(G, G.conj().T) and np.linalg.eigvalsh(G).min() > 0)
    s = np.linalg.eigvalsh(G).min()
    rmin = rr[:N - 1].min()
    bound = 1 - np.sqrt(1 - rmin ** 2)
    check(f'3. N={N}: sigma_min <= 1 - sqrt(1-rho_min^2)', s <= bound + 1e-12,
          f'sigma_min={s:.4f} bound={bound:.4f} rho_min={rmin:.4f}')
    if N in author:
        check(f'4. author sigma_min at N={N} = {author[N]}', abs(s - author[N]) < 0.006 * max(1, author[N] / 0.05), f'got {s:.4f}')
    if prev is not None:
        check(f'3. interlacing: sigma_min(G_{N}) <= sigma_min of its leading principal block', s <= prev + 1e-12)
    prev = s

print('4. Carleson measure: sum of |Im w| over unit boxes [x, x+1] x [-1, 0]')
wr = w.real
for x0 in (-10.0, -100.0, -400.0, -1000.0, -1700.0):
    mass = np.sum(np.abs(w.imag)[(wr <= x0) & (wr > x0 - 1)])
    pred = 0.25 * (1 / np.pi) * np.log(2 * abs(x0) / (2 * np.pi))
    check(f'4. box at Re w = {x0}: mass {mass:.3f} ~ (1/4)(1/pi) log(|2x|/2pi) = {pred:.3f}', abs(mass - pred) < 0.35)
print('   (a Carleson measure needs sup_box mass / side < oo; here it grows like log T: fails unconditionally for the')
print('    on-line zeros by a positive proportion, which is a sharper route than the separation argument)')
prevp = 1.0
for N in (100, 1000, 3000):
    ww = w[:N]
    R = np.abs(ww[:, None] - ww[None, :]) / np.abs(ww[:, None] - np.conj(ww)[None, :])
    np.fill_diagonal(R, 1.0)
    prods = np.exp(np.sum(np.log(R), axis=1))
    check(f'4. truncated Carleson products, N={N}: min_n prod_(m != n) rho = {prods.min():.2e} (upper bound for the true inf), decreasing',
          prods.min() < prevp)
    prevp = prods.min()

print('5. S3 normalisation')
# notebook: Z(t) k_n = exp(i t conj(w_n)) k_n with w_n = -gamma/2 - i(1-sigma)/2  (prop:functional-model-modes)
g0 = gam[0]; wn = -g0 / 2 - 0.25j
rho0 = 0.5 + 1j * g0
for p in (2, 3, 5):
    t = 2 * np.log(p)                         # ring length of p in notebook time (prop:ringnorm-trace)
    ev = np.exp(1j * t * np.conj(wn))
    check(f'5. Z(2 log {p}) eigenvalue = p^(conj rho - 1), modulus p^(-1/2)', abs(ev - p ** (np.conj(rho0) - 1)) < 1e-12
          and abs(abs(ev) - p ** -0.5) < 1e-12)
    check(f'5. note\'s J_p eigenvalue p^(-conj rho/2) has modulus p^(-1/4) = modulus of Z(log {p}), half the ring length',
          abs(abs(p ** (-np.conj(rho0) / 2)) - p ** -0.25) < 1e-12 and abs(abs(np.exp(1j * np.log(p) * np.conj(wn))) - p ** -0.25) < 1e-12)

print(f'\nscratch_den_r7: {ok} pass, {fail} fail')
