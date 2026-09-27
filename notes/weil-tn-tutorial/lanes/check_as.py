"""Independent cross-check for the Artin-Schreier station (demos-as.js) of "Weil Positivity, Contracted".

Conventions (those of scripts/artin_schreier_mps.py, whose brute force and transfer() are reused):
  q odd prime, psi(t) = exp(2 pi i t / q), g(x) = sum_{j=0}^J a_j x^{1+q^j}, a_J != 0.
  E = transfer(q, a): rows = output bond state (s_2..s_J, x), columns = input (s_1..s_J), states in
  lexicographic order (s_1 most significant); E_{s -> s'} = psi(a_0 x^2 + sum_j a_j s_{J+1-j} x).
  Exact sign law (thm:as-sign-law, cor:as-periodic-sign, report/sections/06b):
      S_n(g) = (1 - 2 [2h | n]) Tr E_g^n,  h = smallest power of q > v_-,  v_- = ord_{z=-1} z^J P_g(z),
      P_g(z) = sum_j (a_j/2)(z^j + z^{-j}).  The brief's law S_n = -(-1)^n Tr E^n is the case v_- = 0.
  Affine count N_n = q^n + sum_{a in F_q^x} S_n(a g)  (the projective curve adds 1 point at infinity).
  Weil form: t_k = Tr (E/sqrt q)^k, T[j][k] = t_{k-j}, t_{-k} = conj t_k (prop:ccm-tn-operator-gram).
  Perturbation: E[0][c] *= exp(i eps), c = first column >= 1 with E[0][c] != 0 (c = 1 for J = 1,
  c = q for J = 2, where E[0][1] is structurally zero).
Run from the repository root:  python3 notes/weil-tn-tutorial/lanes/check_as.py
Optionally compares with the demo's JS numerics (node) if available."""
import sys, os, json, subprocess, itertools
from collections import Counter
import numpy as np
sys.path.insert(0, 'scripts')
from artin_schreier_mps import irreducible, polymulmod, polypow, trace, S_bruteforce, transfer

def f_coeffs(q, a):
    J = len(a) - 1; h2 = pow(2, -1, q); c = [0] * (2 * J + 1)
    for j, aj in enumerate(a):
        c[J + j] = (c[J + j] + aj * h2) % q; c[J - j] = (c[J - j] + aj * h2) % q
    return c

def v_minus(q, a):
    c = f_coeffs(q, a); v = 0
    while any(c) and sum(x * (-1) ** k for k, x in enumerate(c)) % q == 0:
        # divide by (z + 1)
        deg = len(c) - 1; out = [0] * deg; carry = 0
        for k in range(deg, 0, -1):
            carry = (c[k] + carry) % q; out[k - 1] = carry; carry = (-carry) % q
        c = out; v += 1
    return v

def h_of(q, v):
    h = 1
    while h <= v: h *= q
    return h

def sign_exact(q, a, n):
    return -1 if n % (2 * h_of(q, v_minus(q, a))) == 0 else 1

def trE(E, n): return np.trace(np.linalg.matrix_power(E, n))

def affine_count_bruteforce(q, n, a):
    """#{(x,y) in F_{q^n}^2 : y^q - y = g(x)} by direct enumeration in F_q[t]/(f)."""
    f = irreducible(q, n); img = Counter()
    for co in itertools.product(range(q), repeat=n):
        y = list(co); yq = polypow(y, q, f, q); img[tuple((u - w) % q for u, w in zip(yq, y))] += 1
    tot = 0
    for co in itertools.product(range(q), repeat=n):
        x = list(co); gv = [0] * n
        for j, aj in enumerate(a):
            if aj:
                term = polymulmod(x, polypow(x, q ** j, f, q), f, q); gv = [(u + aj * v) % q for u, v in zip(gv, term)]
        tot += img[tuple(gv)]
    return tot

def N_transfer(q, a, n, law='exact'):
    tot = q ** n
    for s in range(1, q):
        aa = [(s * c) % q for c in a]
        sg = sign_exact(q, aa, n) if law == 'exact' else -(-1) ** n
        tot += sg * trE(transfer(q, aa), n)
    return tot

def perturb(E, eps):
    E = E.copy(); c = next(k for k in range(1, E.shape[0]) if abs(E[0, k]) > 1e-12)
    E[0, c] *= np.exp(1j * eps); return E, c

def weil_min(E, q, K):
    U = E / np.sqrt(q); t = [np.trace(np.linalg.matrix_power(U, k)) for k in range(K)]
    T = np.array([[t[k - j] if k >= j else np.conj(t[j - k]) for k in range(K)] for j in range(K)])
    return np.linalg.eigvalsh(T)[0]

CASES = [(3, (0, 1)), (3, (1, 1)), (5, (0, 1)), (3, (0, 1, 1)), (3, (1, 0, 1))]
EXTRA = [(5, (2, 1, 3)), (7, (0, 1, 1))]   # spectra only (dim 25, 49): the demo's QR against numpy

def msdist(A, B):
    """max distance of a greedy nearest matching between two multisets of complex numbers"""
    B = list(B); worst = 0
    for z in A:
        k = min(range(len(B)), key=lambda i: abs(B[i] - z)); worst = max(worst, abs(B[k] - z)); B.pop(k)
    return worst
out = {}
print('=== per case: unitarity, moduli, sign law vs brute-force S_n, Weil-form minima ===')
for q, a in CASES:
    a = list(a); E = transfer(q, a); dim = E.shape[0]
    res = np.linalg.norm(E @ E.conj().T - q * np.eye(dim)) / q
    ev = np.linalg.eigvals(E); dev = np.max(np.abs(np.abs(ev) - np.sqrt(q)))
    vm = v_minus(q, a); h = h_of(q, vm)
    print(f'\nq={q} a={a}: dim {dim}, ||EE^+ - qI||_F/q = {res:.1e}, max ||lambda|-sqrt q| = {dev:.1e}, v_- = {vm}, h = {h}')
    nmax = 5 if dim == 3 else 3
    for n in range(1, nmax + 1):
        s = S_bruteforce(q, n, a); t = trE(E, n)
        ex = sign_exact(q, a, n) * t; br = -(-1) ** n * t
        print(f'   n={n}: S_n brute {s.real:+9.4f}{s.imag:+9.4f}i  Tr E^n {t.real:+9.4f}{t.imag:+9.4f}i  '
              f'exact law {"ok" if abs(ex - s) < 1e-8 else "FAIL"}  brief law -(-1)^n {"ok" if abs(br - s) < 1e-8 else "FAIL"}')
    mins = {K: weil_min(E, q, K) for K in (4, 8, 12)}
    Ep, c = perturb(E, 0.3); evp = np.linalg.eigvals(Ep)
    mp = {K: weil_min(Ep, q, K) for K in (4, 8, 12, 14)}
    kneg = next((K for K in range(1, 15) if weil_min(Ep, q, K) < -1e-9), None)
    resp = np.linalg.norm(Ep @ Ep.conj().T - q * np.eye(dim)) / q
    print(f'   Weil-form lambda_min (eps=0): ' + ', '.join(f'K={K}: {v:.3e}' for K, v in mins.items()))
    print(f'   perturbed eps=0.3 at E[0][{c}]: residual {resp:.4f}, |lambda| in [{np.min(abs(evp)):.4f}, {np.max(abs(evp)):.4f}], '
          f'lambda_min ' + ', '.join(f'K={K}: {v:.6f}' for K, v in mp.items()) + f', first negative K = {kneg}')
    out[f'{q}|{a}'] = dict(res=res, dev=dev, ev=ev, evP=evp, trE=[[trE(E, n).real, trE(E, n).imag] for n in range(1, 9)],
        mins=[weil_min(E, q, K) for K in range(1, 15)], minsP=[weil_min(Ep, q, K) for K in range(1, 15)], resP=resp,
        N=[N_transfer(q, a, n).real for n in range(1, 9)])

print('\n=== affine point counts N_n: transfer matrices (exact / brief sign law) vs brute force ===')
PINNED = {}
for q, a in [(3, (0, 1)), (3, (1, 1)), (3, (0, 1, 1)), (3, (1, 0, 1))]:
    nmax = 4 if len(a) == 2 else 3
    row = []
    for n in range(1, nmax + 1):
        bf = affine_count_bruteforce(q, n, list(a)); ne = N_transfer(q, list(a), n); nb = N_transfer(q, list(a), n, 'brief')
        row.append(bf)
        print(f'q={q} a={a} n={n}: brute {bf:6d}  transfer(exact law) {ne.real:10.4f}{ne.imag:+.1e}i  '
              f'transfer(brief law) {nb.real:10.4f}  |N-q^n| = {abs(bf - q**n)}  band {(q-1)*q**(len(a)-1)*q**(n/2):.2f}')
    PINNED[f'{q}|{list(a)}'] = row
print('\npinned brute-force affine counts (hard-coded in demos-as.js):', json.dumps(PINNED))

# ---- compare with the demo's JS numerics
js = r"""
global.window={matchMedia:()=>({matches:false})}; global.document={getElementById:()=>null};
require('./notes/weil-tn-tutorial/core.js'); require('./notes/weil-tn-tutorial/demos-as.js');
const A=window.WT.demos.artinSchreier.num; const res={};
for (const [q,a] of JSON.parse(process.argv[1])) { const r=A.analyse(q,a,0), p=A.analyse(q,a,0.3);
  res[q+'|'+JSON.stringify(a).replace(/,/g,', ')]={res:r.resid, dev:r.dev, trE:r.tr.slice(1,9), N:r.N, mins:r.mins, minsP:p.mins, resP:p.resid, ev:r.ev, evP:p.ev}; }
console.log(JSON.stringify(res));"""
if os.path.exists('notes/weil-tn-tutorial/demos-as.js'):
    r = subprocess.run(['node', '-e', js, json.dumps([[q, list(a)] for q, a in CASES])], capture_output=True, text=True)
    if r.returncode: print('node failed:', r.stderr[:2000]); sys.exit(1)
    J = json.loads(r.stdout); worst = 0
    print('\n=== Python vs JS (demo numerics) ===')
    for key, P in out.items():
        Jk = J[key]
        d_tr = max(abs(complex(*x) - complex(*y)) for x, y in zip(P['trE'], Jk['trE']))
        d_N = max(abs(x - y) for x, y in zip(P['N'], Jk['N']))
        d_m = max(abs(x - y) for x, y in zip(P['mins'], Jk['mins'])); d_mp = max(abs(x - y) for x, y in zip(P['minsP'], Jk['minsP']))
        worst = max(worst, d_tr, d_N, d_m, d_mp)
        print(f'{key:14s} resid py {P["res"]:.1e} js {Jk["res"]:.1e} | resid(eps=.3) py {P["resP"]:.6f} js {Jk["resP"]:.6f} | '
              f'max|dTrE^n| {d_tr:.1e} max|dN_n| {d_N:.1e} max|d lam_min| {d_m:.1e} (eps=.3: {d_mp:.1e})')
        print(f'   N_1..8 py {[int(round(x)) for x in P["N"]]}\n   lam_min(eps=.3) K=4,8,12,14 py {[round(float(P["minsP"][K-1]),6) for K in (4,8,12,14)]} js {[round(Jk["minsP"][K-1],6) for K in (4,8,12,14)]}')
        d_ev = msdist(P['ev'], [complex(*z) for z in Jk['ev']]); d_evp = msdist(P['evP'], [complex(*z) for z in Jk['evP']])
        print(f'   spectrum: JS QR vs numpy eigvals, max matched distance {d_ev:.1e} (eps=.3: {d_evp:.1e})'); worst = max(worst, d_ev, d_evp)
    r = subprocess.run(['node', '-e', js, json.dumps([[q, list(a)] for q, a in EXTRA])], capture_output=True, text=True); J2 = json.loads(r.stdout)
    for q, a in EXTRA:
        E = transfer(q, list(a)); key = f'{q}|{list(a)}'; Ep, _ = perturb(E, 0.3)
        d1 = msdist(np.linalg.eigvals(E), [complex(*z) for z in J2[key]['ev']]); d2 = msdist(np.linalg.eigvals(Ep), [complex(*z) for z in J2[key]['evP']])
        print(f'{key:14s} dim {E.shape[0]}: spectrum JS QR vs numpy {d1:.1e} (eps=.3: {d2:.1e}); JS max||lam|-sqrt q| {J2[key]["dev"]:.1e}'); worst = max(worst, d1, d2)
    print(f'worst Python/JS discrepancy: {worst:.1e}', 'PASS' if worst < 1e-8 else 'FAIL')

print('\n=== eps sweep: does the perturbed Weil form turn negative within K <= 14? (first negative K, max |lambda|/sqrt q) ===')
for q, a in CASES:
    E = transfer(q, list(a)); row = []
    for eps in (0.05, 0.1, 0.2, 0.3, 0.4, 0.5):
        Ep, _ = perturb(E, eps); kn = next((K for K in range(1, 15) if weil_min(Ep, q, K) < -1e-9), None)
        row.append(f'eps={eps}: K={kn}, {np.max(abs(np.linalg.eigvals(Ep)))/np.sqrt(q):.4f}')
    print(f'q={q} a={list(a)}: ' + '; '.join(row))
