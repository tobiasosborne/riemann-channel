"""REFUTE scratch (ff-dirichlet.md, J1, J2, J4): L-functions, functional equation, root number,
global and local Gauss sums, and Tate local epsilons for an additive character of MY choice
(psi_v = psi0(Tr Res_v(x h dt)) with h != 1, so the local factors differ from the page's),
computed by finite sums from Tate's integral  eps_v = int_{varpi^{-(a+d)} O^x} chi_v^{-1}(x)|x|^{-1/2} psi_v(x) dx.
Written from the statements only; check_ff_dirichlet.py was not opened."""
import sys, random
from scratch_gkp_ffm_core import *
mp.mp.dps = 40
z = lambda N: mp.exp(2j*mp.pi/N)
def C(ch, k): return mp.mpf(0) if k is None else z(ch.N)**k

EX = {  # name: (q, N, [P_i])  as on the page (P_i low degree first)
 'X1': (5, 4, [[1, 1, 0, 1]]),
 'X2': (5, 4, [[0, 1], [2, 0, 1]]),
 'X3': (7, 3, [[1, 0, 0, 1, 1]]),
 'X4': (7, 3, [[1, 1, 0, 1]]),
 'X5': (7, 2, [[1, 1, 0, 1]]),
 'X6': (3, 2, [[1, 0, 1, 1, 1]]),
}
def fmt(c): return '%.5f%+.5fi' % (float(c.real), float(c.imag))

def coef_inf(A, B, p):   # coefficient of t^{-1} in the 1/t-expansion of A/B
    q_, R = pdivmod(A, B, p); m = len(B)-1
    if len(R) < m: return 0
    return R[m-1]*pow(B[-1], p-2, p) % p

def global_W(ch):
    Lam, even, n = Lambda(ch); q = ch.q
    W = Lam[n]/mp.mpf(q)**(mp.mpf(n)/2)
    return Lam, even, n, W

def page_local(ch, use_chiPP=True):
    q, N = ch.q, ch.N; out = []
    for i, P in enumerate(ch.Ps):
        Q = q**(len(P)-1); G = 0
        for a in polys_below(len(P)-1, q):
            k = ch.comp(trim(a), i)
            if k is None: continue
            G += C(ch, k)*psi0(a[-1], q)            # coefficient of t^{deg P - 1}
        chiPP = 0
        for j, Pj in enumerate(ch.Ps):
            if j != i: chiPP += ch.comp(P, j)
        e = G/mp.sqrt(Q)*(C(ch, chiPP % N) if use_chiPP else 1)
        out.append(e)
    even = all(ch.on_const(c) == 0 for c in range(1, q))
    if even: out.append(mp.mpf(1))
    else:
        g = sum(C(ch, ch.on_const(c))*psi0(c, q) for c in range(1, q))
        out.append(mp.conj(g)/mp.sqrt(q))
    return out

def tate_product(ch, h):
    """product of local epsilons for psi = psi0(Tr Res(x h dt)), h a polynomial (h != 0)"""
    q, N = ch.q, ch.N; prod = mp.mpf(1); log = []; condsum = 0
    even = all(ch.on_const(c) == 0 for c in range(1, q))
    # finite ramified places
    for i, P in enumerate(ch.Ps):
        Q = q**(len(P)-1); degP = len(P)-1
        d = 0; hh = h
        while not pmod(hh, P, q): hh = pdivmod(hh, P, q)[0]; d += 1
        chiPP = sum(ch.comp(P, j) for j in range(len(ch.Ps)) if j != i) % N   # chi_P(P) from the product formula
        Pk = [1]
        for _ in range(1+d): Pk = pmul(Pk, P, q)
        s = 0
        for a in polys_below(degP, q):
            k = ch.comp(trim(a), i)
            if k is None: continue
            s += C(ch, k)*psi0(coef_inf(pmul(trim(a), h, q), Pk, q), q)
        e = s/mp.sqrt(Q)*C(ch, (chiPP*(1+d)) % N)
        prod *= e; log.append(('P|f', P, d, fmt(e))); condsum += (1+d)*degP
    # finite unramified places where h vanishes: eps = chi(P)^d
    hh = h
    for k in range(1, len(h)):
        for P in irreducibles(k, q):
            d = 0
            while len(hh) > 1 and not pmod(hh, P, q): hh = pdivmod(hh, P, q)[0]; d += 1
            if d and P not in ch.Ps:
                e = C(ch, (ch(P)*d) % N); prod *= e; log.append(('unram', P, d, fmt(e))); condsum += d*(len(P)-1)
    # infinity
    dinf = -2-(len(h)-1); lead = h[-1]
    if even:
        e = mp.mpf(1); condsum += dinf
    else:
        e = sum(mp.conj(C(ch, ch.on_const(c)))*psi0(-c*lead, q) for c in range(1, q))/mp.sqrt(q); condsum += 1+dinf
    prod *= e; log.append(('inf', dinf, fmt(e)))
    return prod, log, condsum

if __name__ == '__main__':
    worst = 0
    for name, (q, N, Ps) in EX.items():
        ch = Char(q, N, Ps)
        Lam, even, n, W = global_W(ch)
        roots = mp.polyroots(Lam[::-1], maxsteps=200, extraprec=200) if n > 0 else []   # roots of Lambda(u); |alpha| = 1/|u|
        rh = max([abs(1/abs(r) - mp.sqrt(q)) for r in roots] + [0])
        # FE at three points
        fe = 0; fe_neg = 0
        for u in [mp.mpc(0.3, 0.7), mp.mpc(-1.1, 0.2), mp.mpc(0.05, -0.4)]:
            lhs = sum(c*u**k for k, c in enumerate(Lam))
            rhs = W*(mp.sqrt(q)*u)**n*sum(mp.conj(c)*(1/(q*u))**k for k, c in enumerate(Lam))
            fe = max(fe, abs(lhs-rhs)/abs(lhs)); fe_neg = max(fe_neg, abs(lhs+rhs)/abs(lhs))
        # global Gauss sums
        d = ch.d; G = 0
        for a in polys_below(d, q):
            k = ch(trim(a))
            if k is None: continue
            G += C(ch, k)*psi0(a[-1], q)
        g = sum(C(ch, ch.on_const(c))*psi0(c, q) for c in range(1, q))
        Wg = G/mp.mpf(q)**(mp.mpf(d)/2) if even else (G/mp.mpf(q)**(mp.mpf(d)/2))/(g/mp.sqrt(q))
        loc = page_local(ch); pl = mp.fprod(loc)
        locn = page_local(ch, use_chiPP=False); pln = mp.fprod(locn)
        tp = []
        for h in ([2], [1, 1], [0, 1], [3, 0, 1], [1, 2, 0, 1]):
            pr, lg, cs = tate_product(ch, [x % q for x in h])
            tp.append((h, abs(pr-W), cs))
        print(f"{name}: q={q} N={N} f={ch.f} {'even' if even else 'odd'} n={n} deg-check n={'d-2' if even else 'd-1'}:{n == (d-2 if even else d-1)}")
        print('   Lambda =', [fmt(c) for c in Lam], ' W =', fmt(W), ' |W|-1 =', mp.nstr(abs(W)-1, 3))
        print('   RH max||alpha|-sqrt q| =', mp.nstr(rh, 3), ' FE resid', mp.nstr(fe, 3), ' with -W', mp.nstr(fe_neg, 3))
        print('   |G|^2/q^d =', mp.nstr(abs(G)**2/q**d, 12), ' |W_gauss - W| =', mp.nstr(abs(Wg-W), 3))
        print('   page local phases', [fmt(e) for e in loc], ' |prod - W| =', mp.nstr(abs(pl-W), 3), ' without chi_P(P):', mp.nstr(abs(pln-W), 3))
        for h, err, cs in tp:
            print(f'   own psi (h={h}): |prod eps - W| = {mp.nstr(err, 3)}, conductor sum = {cs} (n={n})')
        worst = max(worst, abs(pl-W), abs(Wg-W), max(e for _, e, _ in tp))
    print('worst over X1-X6:', mp.nstr(worst, 3))
    # B7: f = P1 P2 with deg 1 x deg 2 at q=5, N=4
    q, N = 5, 4
    fails = 0; tot = 0; bad_tate = 0; jfails = []
    for P1 in irreducibles(1, q):
        for P2 in irreducibles(2, q):
            ch = Char(q, N, [P1, P2]); _, _, n, W = global_W(ch)
            pl = mp.fprod(page_local(ch)); pln = mp.fprod(page_local(ch, False))
            pr, _, _ = tate_product(ch, [1, 1])
            tot += 1; fails += abs(pln-W) > 1e-20; bad_tate += abs(pr-W) > 1e-20 or abs(pl-W) > 1e-20
            if abs(pl-W) > 1e-20: jfails.append((P1, P2))
    print(f'B7: q=5,N=4, f=P1P2 (1x2): {tot} moduli; page product = W in {tot-len(jfails)}; own-psi Tate product = W fails {bad_tate}; dropping chi_P(P) fails in {fails}')
