"""check_kraus.py -- independent numpy check of the Kraus station (demos-kraus.js, WT.demos.kraus).

Run from anywhere:  python3 notes/weil-tn-tutorial/lanes/check_kraus.py
It (1) runs the demo's own numerics headless in node (window/document stubs, core.js + demos-kraus.js) for one
fixed state per regime and exports the raw Kraus matrices B_1..B_4 and every number the readout prints;
(2) recomputes everything from those identical matrices with numpy, conventions as scripts/weil_positivity.py
(Ad(A) = conj(A) (x) A, T[j-block, i-block] = E_i for j != inv[i], inv = [2,3,0,1]);
(3) prints both side by side in the demo's number format and counts mismatches.
Also: Tr T^l = sum_w |Tr B_w|^2 for l <= 5; Ihara-Bass det(1-uT) = (1-u^2)^4 det(1 - u Sigma + 3u^2) at three u
in the inverse-paired cases; the Weil minima at K = 4, 8, 12; the Hastings search behind the presets.
"""
import itertools
import json
import os
import subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D, Q, INV, KMAX, HB = 4, 3, [2, 3, 0, 1], 14, 2 * np.sqrt(3) / 4
RQ = np.sqrt(3)

NODE = r"""
global.window = {matchMedia: () => ({matches: false})}; global.document = {getElementById: () => null};
require(process.argv[1] + '/core.js'); require(process.argv[1] + '/demos-kraus.js');
const K = window.WT.demos.kraus.model, d = K.defaultState();
const cases = [Object.assign({}, d), {regime: 'unitary', seed: 1, eps: 0, preset: 'sqrt'}, {regime: 'unitary', seed: 1, eps: 0, preset: 'pauli'},
  {regime: 'unitary', seed: d.seed, eps: 0.3, preset: null}, {regime: 'inverse', seed: K.inverseSeed(1), eps: 0, preset: null},
  {regime: 'adjoint', seed: 1, eps: 0, preset: null}, {regime: 'nodual', seed: 1, eps: 0, preset: null}];
const out = cases.map(st => { const M = K.model(st); const el = {innerHTML: ''}; K.readout(el, M, 12);
  const mat = B => ({re: B.re, im: B.im});
  return {st, kind: M.kind, raw: M.raw.map(mat), scale: M.scale, sig: M.sig, phi: M.hast.phi, hastMax: M.hast.max, holds: M.hast.holds,
    S: M.S, r: M.r, tr: M.tr, words: M.words, specQ: M.specQ, ret: M.ret, Jinv: M.Jinv, circle: M.circle, maxRet: M.maxRet,
    mins: M.mins, mins3: M.mins3, disc: M.disc, pe: M.pe, readout: el.innerHTML.replace(/<[^>]+>/g, '')}; });
console.log(JSON.stringify(out));
"""


def fmtF(x, d=4):
    v = 0.0 if abs(x) < 0.5 * 10 ** (-d) else x
    return f'{v:.{d}f}'


def fmtW(x, sc, p=5):
    """the demo's lambda_min format: 0 below 1e-9 * max(1, max|nu|), else JS toPrecision(5) with WT.fmt's exponent"""
    if abs(x) < 1e-9 * sc:
        return '0'
    e = int(np.floor(np.log10(abs(float(f'{x:.{p - 1}e}')))))
    if e < -6 or e >= p:
        m, ex = f'{x:.{p - 1}e}'.split('e')
        return f'{m}e{int(ex)}'
    return f'{x:.{p - 1 - e}f}'


def ad(A):
    return np.kron(A.conj(), A)


def build_T(Bs):
    T = np.zeros((16, 16), complex)
    for i in range(D):
        for j in range(D):
            if j != INV[i]:
                T[4 * j:4 * j + 4, 4 * i:4 * i + 4] = ad(Bs[i])
    return T


def remove_nearest(ev, S):
    ev = list(np.asarray(ev, complex))
    for s in S:
        i = int(np.argmin([abs(e - s) for e in ev]))
        ev.pop(i)
    return np.array(ev)


def hausdorff(A, B):
    A, B = np.asarray(A, complex), np.asarray(B, complex)
    d = np.abs(A[:, None] - B[None, :])
    return max(d.min(axis=1).max(), d.min(axis=0).max())


def word_sum(Bs, l):
    tot, cnt = 0.0, 0
    for w in itertools.product(range(D), repeat=l):
        if all(w[(k + 1) % l] != INV[w[k]] for k in range(l)):
            P = np.eye(2, dtype=complex)
            for i in w:
                P = Bs[i] @ P
            tot += abs(np.trace(P)) ** 2
            cnt += 1
    return tot, cnt


def newton_roots(tr):
    n = len(tr) - 1
    e = [1.0 + 0j]
    for k in range(1, n + 1):
        e.append(sum((-1) ** (i - 1) * e[k - i] * tr[i] for i in range(1, k + 1)) / k)
    return np.roots([(-1) ** k * e[k] for k in range(n + 1)])


def quad(a):
    s = np.sqrt(complex(a * a - 4 * Q))
    return [(a + s) / 2, (a - s) / 2]


def analyse(case):
    st, regime = case['st'], case['st']['regime']
    raw = [np.array(B['re']) + 1j * np.array(B['im']) for B in case['raw']]
    inv_err = max(np.linalg.norm(raw[INV[i]] @ raw[i] - np.eye(2)) for i in range(D))
    adj_err = max(np.linalg.norm(raw[INV[i]] - raw[i].conj().T) for i in range(D))
    invP, adjP = inv_err < 1e-9, adj_err < 1e-9
    kind = 'nodual' if regime == 'nodual' else 'unitary' if invP and adjP else 'inverse' if invP else 'adjoint'
    scale = 1.0
    if kind == 'adjoint':
        scale = np.sqrt(Q / np.max(np.abs(np.linalg.eigvals(build_T(raw)))))
    Bs = [scale * B for B in raw]
    T = build_T(Bs)
    Sig = sum(ad(B) for B in Bs)
    sig = np.linalg.eigvalsh(Sig).astype(complex) if adjP else np.linalg.eigvals(Sig)
    phi = sig / D
    nt = [z for z in phi if abs(z - 1) >= 1e-8 and abs(z + 1) >= 1e-8]
    hmax = max([abs(z) for z in nt], default=0.0)
    pm1 = [1.0] * 4 + [-1.0] * 4
    ref, r = None, RQ
    if invP:
        ref = pm1 + [m for a in sig for m in quad(a)]
    if kind == 'unitary':
        S = list(pm1)
        for z in phi:
            if abs(z - 1) < 1e-8:
                S += [Q, 1.0]
            elif abs(z + 1) < 1e-8:
                S += [-Q, -1.0]
    elif kind == 'inverse':
        a0 = sig[np.argmax(np.abs(sig))]
        S = pm1 + quad(a0)
    elif kind == 'adjoint':
        S = [float(Q)]
    else:
        ref = []
        for a in (1, 2, 2, 4):
            dd = np.sqrt((a + 1) ** 2 + 12 * a)
            ref += [a, 1, (a + 1 + dd) / 2, (a + 1 - dd) / 2]
        S = [1, 1, 1, 1, 1, 2, 2, 4, 3, -1]
        r = (5 + np.sqrt(73)) / 2
    ev = np.linalg.eigvals(T)
    base = np.array(ref, complex) if ref is not None else ev
    ret = remove_nearest(base, S)
    J = r * r / np.conj(ret)
    Jinv = all(np.min(np.abs(ret - j)) < 1e-6 for j in J)
    circle = float(np.max(np.abs(np.abs(ret) - r)))
    maxret = float(np.max(np.abs(ret)))
    tr = [np.trace(np.linalg.matrix_power(T, l)) for l in range(17)]
    words = [word_sum(Bs, l) for l in range(1, 6)]
    word_err = max(abs(w[0] - tr[l + 1]) / max(1, abs(tr[l + 1])) for l, w in enumerate(words))

    def mins_at(rr):
        nu = np.array([(tr[l].real - sum((complex(s) ** l).real for s in S)) / rr ** l for l in range(KMAX)])
        return [np.linalg.eigvalsh(np.array([[nu[abs(j - k)] for k in range(K)] for j in range(K)]))[0] for K in range(1, KMAX + 1)]
    mins = mins_at(r)
    nusc = max(1.0, max(abs((tr[l].real - sum((complex(s) ** l).real for s in S)) / r ** l) for l in range(KMAX)))
    ib = None
    if invP:
        ib = 0.0
        for u in (0.13, 0.21 + 0.09j, -0.17):
            lhs = np.linalg.det(np.eye(16) - u * T)
            rhs = (1 - u * u) ** 4 * np.linalg.det(np.eye(4) - u * Sig + Q * u * u * np.eye(4))
            ib = max(ib, abs(lhs / rhs - 1))
    return dict(kind=kind, inv_err=inv_err, adj_err=adj_err, scale=scale, sig=sig, phi=phi, hmax=hmax, holds=hmax <= HB * (1 + 1e-9),
                S=S, r=r, ev=ev, ref=ref, ret=ret, Jinv=Jinv, circle=circle, maxret=maxret, tr=tr, words=words, word_err=word_err,
                mins=mins, mins3=mins_at(RQ) if kind == 'nodual' else None, ib=ib, nusc=nusc,
                eig_vs_ref=hausdorff(ev, ref) if ref is not None else None, newton=hausdorff(newton_roots(tr), ref if ref is not None else ev))


def cfmt(z, d=4):
    z = complex(z)
    return fmtF(z.real, d) if abs(z.imag) < 0.5 * 10 ** (-d) else f'{fmtF(z.real, d)}{"-" if z.imag < 0 else "+"}{fmtF(abs(z.imag), d)}i'


def srt(zs):
    return sorted((complex(z[0], z[1]) if isinstance(z, list) else complex(z) for z in zs), key=lambda z: (round(z.real, 6), round(z.imag, 6)))


def main():
    js = subprocess.run(['node', '-e', NODE, ROOT], capture_output=True, text=True, check=True)
    cases = json.loads(js.stdout)
    bad = 0
    for c in cases:
        P = analyse(c)
        st = c['st']
        print('=' * 110)
        print(f"case {st}  ->  kind: python {P['kind']}, demo {c['kind']}")
        print('-- demo readout (K = 12) --')
        print(c['readout'])
        print('-- python vs demo --')
        rows = [
            ('pairing ||B_ibar B_i - 1||, ||B_ibar - B_i^+|| < 1e-9', f"{P['inv_err'] < 1e-9}, {P['adj_err'] < 1e-9}", f"{c['pe']['inv'] < 1e-9}, {c['pe']['adj'] < 1e-9}"),
            ('rescale s (adjoint-only: Perron root of T -> 3)', fmtF(P['scale'], 6), fmtF(c['scale'], 6)),
            ('spec Sigma', ' '.join(cfmt(z) for z in srt(P['sig'])), ' '.join(cfmt(z) for z in srt(c['sig']))),
            ('Hastings max |lambda(Phi)| off +-1', fmtF(P['hmax']), fmtF(c['hastMax'])),
            ('Hastings bound holds', str(P['holds']), str(c['holds'])),
            ('trivial S', ' '.join(cfmt(z) for z in srt(P['S'])), ' '.join(cfmt(z) for z in srt(c['S']))),
            ('r', fmtF(P['r']), fmtF(c['r'])),
            ('Tr T^l, l = 1..4', ' '.join(fmtF(P['tr'][l].real) for l in range(1, 5)), ' '.join(fmtF(c['tr'][l][0]) for l in range(1, 5))),
            ('#words l = 1..4', ' '.join(str(w[1]) for w in P['words'][:4]), ' '.join(str(w['count']) for w in c['words'])),
            ('retained multiset', ' '.join(cfmt(z) for z in srt(P['ret'])), ' '.join(cfmt(z) for z in srt(c['ret']))),
            ('J-invariant', str(P['Jinv']), str(c['Jinv'])),
            ('max ||mu| - r|', fmtF(P['circle']), fmtF(c['circle'])),
            ('max |mu| retained', fmtF(P['maxret']), fmtF(c['maxRet'])),
            ('spec T (numpy eig vs demo QR), sorted', ' '.join(cfmt(z) for z in srt(P['ev'])), ' '.join(cfmt(z) for z in srt(c['specQ']))),
            ('Weil lambda_min K = 4, 8, 12', ', '.join(fmtW(P['mins'][k - 1], P['nusc']) for k in (4, 8, 12)), ', '.join(fmtW(c['mins'][k - 1], P['nusc']) for k in (4, 8, 12))),
            ('Weil lambda_min K = 1..14', ' '.join(fmtW(x, P['nusc']) for x in P['mins']), ' '.join(fmtW(x, P['nusc']) for x in c['mins'])),
        ]
        if P['mins3'] is not None:
            rows.append(('no-duality: lambda_min(12) at r = sqrt3', fmtW(P['mins3'][11], P['nusc']), fmtW(c['mins3'][11], P['nusc'])))
        for name, a, b in rows:
            ok = a == b
            bad += not ok
            print(f"  [{'ok ' if ok else 'BAD'}] {name}\n        python: {a}\n        demo:   {b}")
        print(f"  Tr T^l = sum_w |Tr B_w|^2, l <= 5: max rel diff {P['word_err']:.1e}; words per l: {[w[1] for w in P['words']]}")
        print(f"  Tr T^l >= 0 for l <= 16: {all(t.real >= -1e-9 * max(1, abs(t)) for t in P['tr'][1:])}; "
              f"max |Im|/|.| = {max(abs(t.imag) / max(1, abs(t)) for t in P['tr'][1:]):.1e}")
        if P['ib'] is not None:
            print(f"  Ihara-Bass det(1-uT) = (1-u^2)^4 det(1-u Sigma+3u^2) at u = 0.13, 0.21+0.09i, -0.17: max rel err {P['ib']:.1e}")
            print(f"  numpy eig vs Ihara-Bass/closed form: {P['eig_vs_ref']:.1e}  (demo QR vs the same: {c['disc']['qr']:.1e})")
        print(f"  Newton-identity roots (np.roots) off by {P['newton']:.0e};  demo (Durand-Kerner) off by {c['disc']['newton']:.0e}  [diagnostic: order of magnitude only]")
    # the Hastings search behind the presets
    print('=' * 110)
    print('Unitary pairs (U1, U2, U1^+, U2^+), n = 2: nontrivial spec Phi and Hastings 2 sqrt3/4 = 0.8660')
    X = np.array([[0, 1], [1, 0]], complex)
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.diag([1, -1]).astype(complex)
    Hd = (X + Z) / np.sqrt(2)
    rot = lambda P, t: np.cos(t / 2) * np.eye(2) - 1j * np.sin(t / 2) * P
    th = np.arccos(-1 / 3)
    cands = {'X, Z (Pauli)': (X, Z), 'X, H (Hadamard)': (X, Hd), 'sqrt X, sqrt Z = (1-iX)/sqrt2, (1-iZ)/sqrt2': (rot(X, np.pi / 2), rot(Z, np.pi / 2)),
             'X, exp(i pi/8 Y)': (X, rot(Y, -np.pi / 4)), 'rotations by arccos(-1/3) about x and z': (rot(X, th), rot(Z, th))}
    for name, (U1, U2) in cands.items():
        fam = [U1, U2, U1.conj().T, U2.conj().T]
        lam = np.sort(np.linalg.eigvalsh(sum(ad(U) for U in fam) / 4))
        nt = [l for l in lam if abs(abs(l) - 1) >= 1e-8]
        print(f'  {name:48s} spec Phi = {np.round(lam, 4)}  max nontrivial |lambda| = {max(map(abs, nt), default=0):.4f}  '
              f'self-inverse: {np.allclose(U1 @ U1, np.eye(2))}')
    rng = np.random.default_rng(0)
    passes = 0
    for _ in range(2000):
        U = []
        for _k in range(2):
            z = (rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))) / np.sqrt(2)
            q, rr = np.linalg.qr(z)
            U.append(q * (np.diag(rr) / abs(np.diag(rr))))
        lam = np.linalg.eigvalsh(sum(ad(u) for u in U + [u.conj().T for u in U]) / 4)
        passes += max(abs(l) for l in lam if abs(abs(l) - 1) >= 1e-8) <= HB
    print(f'  Haar pairs meeting the bound (numpy, 2000 draws): {passes / 2000:.3f}')
    # inverse-paired families: how often is spec Sigma non-real, with and without |det B| = 1
    for norm in ('raw', 'det1'):
        nr = 0
        for s in range(400):
            rng = np.random.default_rng(s)
            B = [rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)) for _ in range(2)]
            if norm == 'det1':
                B = [b / np.sqrt(abs(np.linalg.det(b))) for b in B]
            ev = np.linalg.eigvals(sum(ad(b) for b in B + [np.linalg.inv(b) for b in B]))
            nr += np.max(np.abs(ev.imag)) > 1e-8
        print(f'  inverse-paired, normalisation {norm:4s}: spec Sigma non-real in {nr / 400:.2f} of 400 draws')
    print('=' * 110)
    print(f'mismatches between python and demo (printed digits): {bad}')


if __name__ == '__main__':
    main()
