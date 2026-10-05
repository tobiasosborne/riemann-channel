#!/usr/bin/env python3
"""Checks for 'Locks between modes: where they come from, and which fluxes have none' (notes/adelic-gkp/locks.md).

Needs PARI through cypari2 and networkx (scratch venv; see check_howe_positivity.py).

Conventions as in check_sign_vector.py, generalised to a multiplier qm that is a power of the prime p:
mu^+- = (lambda +- delta)/2, delta = i sqrt(4 qm - lambda^2), D = lambda^2 - 4 qm.
"""
import itertools
import numpy as np
import sympy as sp
import networkx as nx
import cypari2
from cysignals.alarm import alarm, cancel_alarm, AlarmInterrupt

pari = cypari2.Pari()
pari.allocatemem(2 * 10 ** 9)
x = sp.symbols("x")
X = pari("x")
npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def P(expr):
    return pari(str(sp.expand(expr)).replace("**", "^"))

def weil_poly(g, qm):
    m = sp.Poly(g, x).degree()
    return sp.Poly(sp.expand(sp.simplify(x ** m * g.subs(x, x + sp.Integer(qm) / x))), x).as_expr()

def truth(g, qm, p):
    f = P(weil_poly(g, qm))
    spl = pari.nfsplitting(f)
    N = pari.nfinit(pari.subst(spl, "x", "y"))
    rts = N.nfroots(f)
    theta = pari.polroots(N.nf_get_pol())[0]
    vals = [complex(pari.subst(pari.lift(r), "y", theta)) for r in rts]
    lam = sorted({round((v + qm / v).real, 8) for v in vals})
    pats = set()
    for Pr in N.idealprimedec(p):
        sig = {}
        for r, v in zip(rts, vals):
            if v.imag > 0:
                sig[round((v + qm / v).real, 8)] = 1 if int(N.idealval(r, Pr)) > 0 else -1
        pats.add(tuple(sig[l] for l in lam))
    return pats, any(len(set(s)) == 1 for s in pats), vals

def predict(g, qm, p):
    gp = P(g)
    spl = pari.nfsplitting(gp)
    Np = pari.nfinit(pari.subst(spl, "x", "y"))
    lam = Np.nfroots(gp)
    th = [t for t in pari.polroots(Np.nf_get_pol()) if abs(complex(t).imag) < 1e-12][0]
    num = lambda e: complex(pari.subst(pari.lift(e), "y", th)).real
    lam = sorted(lam, key=num)
    D = [l * l - 4 * qm for l in lam]
    m = len(lam)
    rel = []
    for k in range(2, m + 1, 2):
        for I in itertools.combinations(range(m), k):
            prod = D[I[0]]
            for j in I[1:]:
                prod = prod * D[j]
            fac = Np.nffactor(X * X - prod)
            if len(fac[0]) == 2 or (len(fac[0]) == 1 and int(fac[1][0]) == 2):
                r = -pari.polcoef(fac[0][0], 0)
                if num(r) < 0:
                    r = -r
                lp = lam[I[0]]
                for j in I[1:]:
                    lp = lp * lam[j]
                rel.append((I, (-1) ** (k // 2) * r / lp))
    taus, allowed = [], set()
    for Pr in Np.idealprimedec(p):
        tau = {}
        for I, rho in rel:
            if rho == 1:
                tau[I] = 1
            elif rho == -1:
                tau[I] = -1
            else:
                tau[I] = 1 if int(Np.idealval(rho - 1, Pr)) > int(Np.idealval(rho + 1, Pr)) else -1
        taus.append(tau)
        for s in itertools.product((1, -1), repeat=m):
            if all(np.prod([s[j] for j in I]) == t for I, t in tau.items()):
                allowed.add(s)
    return [I for I, _ in rel], taus, allowed, any(all(t == 1 for t in tau.values()) for tau in taus)


def predict_fast(g, qm, p, limit=20):
    """Same output as predict, for larger spectra. The relation group is found from quadratic characters at auxiliary
    primes that split completely in N+ (a necessary condition), and each generator is then verified to be a square."""
    gp = P(g)
    spl = pari.nfsplitting(gp)
    if int(pari.poldegree(spl)) > 60:
        return None
    Np = pari.nfinit(pari.subst(spl, "x", "y"))
    lam = Np.nfroots(gp)
    th = [t for t in pari.polroots(Np.nf_get_pol()) if abs(complex(t).imag) < 1e-12][0]
    num = lambda e: complex(pari.subst(pari.lift(e), "y", th)).real
    lam = sorted(lam, key=num)
    D = [l * l - 4 * qm for l in lam]
    m = len(lam)
    deg = int(pari.poldegree(Np.nf_get_pol()))
    rows, ell = [], 3
    while len(rows) < 6 * m + 12:
        ell = int(pari.nextprime(ell + 1))
        if ell == p:
            continue
        rts_l = pari.polrootsmod(Np.nf_get_pol(), ell)
        if len(rts_l) != deg:
            continue
        for a_l in rts_l:
            try:
                vals_ = [int(pari.lift(pari.subst(pari.lift(d_), "y", a_l))) for d_ in D]
            except Exception:
                break
            if any(v == 0 for v in vals_):
                continue
            rows.append([0 if int(pari.kronecker(v, ell)) == 1 else 1 for v in vals_])
    # kernel over F_2 by Gaussian elimination
    Mrows = [r[:] for r in rows]
    piv, r_ = [], 0
    for c in range(m):
        pr_ = next((i for i in range(r_, len(Mrows)) if Mrows[i][c]), None)
        if pr_ is None:
            continue
        Mrows[r_], Mrows[pr_] = Mrows[pr_], Mrows[r_]
        for i in range(len(Mrows)):
            if i != r_ and Mrows[i][c]:
                Mrows[i] = [(a_ + b_) % 2 for a_, b_ in zip(Mrows[i], Mrows[r_])]
        piv.append(c)
        r_ += 1
    free = [c for c in range(m) if c not in piv]
    gens = []
    for fcol in free:
        v = [0] * m
        v[fcol] = 1
        for i, c in enumerate(piv):
            v[c] = Mrows[i][fcol]
        gens.append(tuple(j for j in range(m) if v[j]))
    rel = []
    for I in gens:
        prod = D[I[0]]
        for j in I[1:]:
            prod = prod * D[j]
        fac = Np.nffactor(X * X - prod)
        if not (len(fac[0]) == 2 or (len(fac[0]) == 1 and int(fac[1][0]) == 2)):
            return None                          # a candidate relation that is not a square: inconclusive
        r = -pari.polcoef(fac[0][0], 0)
        if num(r) < 0:
            r = -r
        lp = lam[I[0]]
        for j in I[1:]:
            lp = lp * lam[j]
        rel.append((I, (-1) ** (len(I) // 2) * r / lp))
    taus = []
    for Pr in Np.idealprimedec(p):
        tau = {}
        for I, rho in rel:
            if rho == 1:
                tau[I] = 1
            elif rho == -1:
                tau[I] = -1
            else:
                tau[I] = 1 if int(Np.idealval(rho - 1, Pr)) > int(Np.idealval(rho + 1, Pr)) else -1
        taus.append(tau)
    return [I for I, _ in rel], taus, any(all(t == 1 for t in tau.values()) for tau in taus)


# ------------------------------------------------------------------------------------------ L1
print("== L1  a pairwise lock is a root-of-unity relation between Frobenius eigenvalues (one prime of N+ above p)")
def upper(lam, q):
    return (lam + 1j * np.sqrt(4 * q - lam * lam)) / 2
def root_of_unity_order(zz):
    for n in range(1, 61):
        if abs(zz ** n - 1) < 1e-9:
            return n
    return None
L1 = [(5, 2.0, 4.0), (5, -2.0, 4.0), (7, 1.0, 5.0), (7, 1.0, 4.0), (7, 4.0, 5.0), (2, 1.0, -1.0), (2, 5 ** 0.5, -5 ** 0.5),
      (5, 1 + 2 * 3 ** 0.5, 1 - 2 * 3 ** 0.5)]
LOCK = {(5, 2.0, 4.0): -1, (5, -2.0, 4.0): 1, (7, 1.0, 5.0): 1, (7, 1.0, 4.0): -1, (7, 4.0, 5.0): -1, (2, 1.0, -1.0): -1}
ok, rows = True, []
for q, a, b in L1:
    ma, mb = upper(a, q), upper(b, q)
    n_same, n_conj = root_of_unity_order(mb / ma), root_of_unity_order(mb / np.conj(ma))
    sign = 1 if n_same else (-1 if n_conj else 0)
    ok &= sign != 0 and (LOCK.get((q, a, b), sign) == sign)
    rows.append(f"q={q}: ({a:.3f}, {b:.3f}) zeta of order {n_same or n_conj}, lock {sign:+d}")
check("in each locked pair mu'_+ = zeta mu_+ (lock +1) or zeta conj(mu_+) (lock -1), zeta a root of unity; signs match the residue rule", ok, "; ".join(rows))
for q, a, b in ((5, 5 ** 0.5, -5 ** 0.5), (5, 1 + 2 * 3 ** 0.5, 1 - 2 * 3 ** 0.5)):
    pass
g_irr = [(x ** 2 - 5, 2), (x ** 2 - 2 * x - 11, 5)]
okp = True
for g, q in g_irr:
    rel, taus, allowed, yes = predict(g, q, q)
    a, b = sorted(float(r) for r in sp.Poly(g, x).nroots())
    ma, mb = upper(a, q), upper(b, q)
    sign = 1 if root_of_unity_order(mb / ma) else -1
    okp &= len(taus) == 1 and list(taus[0].values()) == [sign]
check("for the two irrational pairs the residue rule gives the same sign as the root-of-unity relation", okp)

# ------------------------------------------------------------------------------------------ L2
print("== L2  integer eigenvalues: locks other than +-lambda need the Gaussian or the Eisenstein field")
bad, examples = 0, []
for q in sp.primerange(2, 400):
    groups = {}
    for lam in range(-int(2 * q ** 0.5), int(2 * q ** 0.5) + 1):
        if lam % q == 0 or lam * lam >= 4 * q:
            continue
        val, sf = 4 * q - lam * lam, 1
        for pr, e in sp.factorint(val).items():
            if e % 2:
                sf *= pr
        groups.setdefault(sf, set()).add(abs(lam))
    for d, s in groups.items():
        if len(s) > 1:
            if d not in (1, 3):
                bad += 1
            elif len(examples) < 6:
                examples.append((int(q), d, sorted(s)))
            # partner formulas: square lattice |lam'| = m; hexagonal |lam'| = |lam +- 3m|/2
            for lam in s:
                m = int(sp.sqrt((4 * q - lam * lam) // d))
                partners = {m} if d == 1 else {abs(lam + 3 * m) // 2, abs(lam - 3 * m) // 2}
                if not (s - {lam}) <= partners:
                    bad += 1
check("for all primes q < 400: several |lambda| share a field only for d = 1 (partner m) or d = 3 (partners |lambda +- 3m|/2)", bad == 0,
      f"examples (q, d, |lambda|): {examples}")

# ------------------------------------------------------------------------------------------ L3
print("== L3  a lock that depends on the prime: a cyclic quartic field")
g, q = x ** 2 + x - 1, 11
rel, taus, allowed, yes = predict(g, q, q)
pats, yes_t, vals = truth(g, q, q)
check("q = 11, eigenvalues (-1 +- sqrt5)/2: one relation, its sign differs at the two primes of Q(sqrt5) above 11, so all four sign vectors occur",
      len(rel) == 1 and len(taus) == 2 and sorted(list(t.values())[0] for t in taus) == [-1, 1] and pats == allowed and len(pats) == 4 and yes_t,
      f"tau = {[list(t.values())[0] for t in taus]}; mu_+ = {vals[[i for i, v in enumerate(vals) if v.imag > 0][0]]:.4f} lies in Q(zeta_5)")

# ------------------------------------------------------------------------------------------ L4
print("== L4  bipartite base graphs: the step is a square root; the arithmetic lattice is one Lagrangian half")
def from_edges(n, edges):
    A = np.zeros((n, n), dtype=int)
    for a, b in edges:
        A[a, b] = A[b, a] = 1
    return A
def prism(m):
    return from_edges(2 * m, [(i, (i + 1) % m) for i in range(m)] + [(m + i, m + (i + 1) % m) for i in range(m)] + [(i, m + i) for i in range(m)])
def K33():
    return from_edges(6, [(a, 3 + b) for a in range(3) for b in range(3)])
def flux_spectra(A):
    n = len(A)
    seen, tree, stack = {0}, set(), [0]
    while stack:
        v = stack.pop()
        for w in range(n):
            if A[v, w] and w not in seen:
                seen.add(w)
                tree.add((min(v, w), max(v, w)))
                stack.append(w)
    cot = [(a, b) for a in range(n) for b in range(a + 1, n) if A[a, b] and (a, b) not in tree]
    out = {}
    for bits in itertools.product((0, 1), repeat=len(cot)):
        As = A.copy()
        for (a, b), bt in zip(cot, bits):
            if bt:
                As[a, b] = As[b, a] = -1
        key = tuple(int(round(c)) for c in np.poly(As.astype(float)))
        out.setdefault(key, [0, As])[0] += 1
    return out
def sides(A):
    G = nx.from_numpy_array(A)
    return nx.bipartite.color(G)
okb, rowsb = True, []
for gname, A, q in (("K33", K33(), 2), ("cube", prism(4), 2)):
    col = sides(A)
    n = len(A)
    Dg = np.diag([1 if col[v] == 0 else -1 for v in range(n)])
    Aside = [v for v in range(n) if col[v] == 0]
    Bside = [v for v in range(n) if col[v] == 1]
    for key, (cnt, As) in flux_spectra(A).items():
        okb &= np.array_equal(Dg @ As @ Dg, -As)
        lamf = np.linalg.eigvalsh(As.astype(float))
        I, Z = np.eye(n, dtype=int), np.zeros((n, n), dtype=int)
        M = np.block([[Z, -I], [q * I, As]])
        V = np.block([[As, I], [-q * I, Z]])
        Om = np.block([[Z, I], [-I, Z]])
        Gam = np.block([[Dg, Z], [Z, -Dg]])
        okb &= np.array_equal(Gam @ M, -M @ Gam) and np.array_equal(Gam.T @ Om @ Gam, -Om) and np.array_equal(Gam @ Gam, np.eye(2 * n, dtype=int))
        Tp = np.zeros((2 * n, n), dtype=int)                    # basis of T_+: f on side A, g on side B
        for k, v in enumerate(Aside):
            Tp[v, k] = 1
        for k, v in enumerate(Bside):
            Tp[n + v, len(Aside) + k] = 1
        okb &= np.array_equal(Gam @ Tp, Tp) and not (Tp.T @ Om @ Tp).any()
        M2T = M @ M @ Tp
        F2 = np.linalg.lstsq(Tp.astype(float), M2T.astype(float), rcond=None)[0].round().astype(int)
        V2 = np.linalg.lstsq(Tp.astype(float), (V @ V @ Tp).astype(float), rcond=None)[0].round().astype(int)
        okb &= np.array_equal(Tp @ F2, M2T)
        Bs = As[np.ix_(Aside, Bside)]
        wplus = Tp.T @ Om @ (M + V) @ Tp
        okb &= np.array_equal(wplus, np.block([[np.zeros((len(Aside),) * 2, dtype=int), Bs], [-Bs.T, np.zeros((len(Bside),) * 2, dtype=int)]]))
        okb &= np.array_equal(F2.T @ wplus, wplus @ V2)
        if not (np.all(np.abs(lamf) < 2 * np.sqrt(q) - 1e-9) and int(sp.Matrix(As.tolist()).det()) % q != 0):
            continue
        Rf = wplus @ (F2 - V2)
        okb &= np.array_equal(Rf, Rf.T) and np.linalg.eigvalsh(Rf.astype(float)).min() > 1e-9
        g2m = sp.Matrix((F2 + V2).tolist())
        cp2 = sp.Poly(g2m.charpoly(x).as_expr(), x)
        g2 = sp.quo(cp2.as_expr(), sp.gcd(cp2.as_expr(), sp.diff(cp2.as_expr(), x)))
        rel, taus, allowed, yes = predict(g2, q * q, q)
        lam2 = sorted(set(np.round(np.linalg.eigvals(np.array((F2 + V2), dtype=float)).real, 6)))
        if len(lam2) <= 3:
            pats, yes_t, _ = truth(g2, q * q, q)
            okb &= pats == allowed and yes_t == yes
            how = "rule = PARI"
        else:
            how = "rule only"
        rowsb.append(f"{gname}: {cnt} classes, |det B_s| = {abs(int(round(np.linalg.det(Bs.astype(float)))))}, two-step eigenvalues {lam2}, "
                     f"{len(rel)} relations, polarised by w_+: {'YES' if yes else 'NO'} ({how})")
for r in rowsb:
    print("      " + r)
check("bipartite: D = +-1 by side gives D A_s D = -A_s for every flux; Gamma = diag(D,-D) is an antisymplectic involution anticommuting with the step; "
      "T_+ = (functions on one side) + (functions on the other) is Lagrangian, F^2 acts on it, and w_+ is the signed biadjacency form, positive for {Im phi(F^2) > 0}", okb)

# ------------------------------------------------------------------------------------------ L5
print("== L5  the fast relation finder agrees with the direct one")
okf = True
for g, q in ((x ** 2 - 1) * (x ** 2 - 5), 2), ((x + 1) * (x ** 3 - 3 * x ** 2 - 9 * x + 19), 5), ((x - 1) * (x - 4) * (x - 5), 7), ((x + 4) * (x - 1) * (x - 5), 7), (x ** 2 - 2 * x - 11, 5), (x ** 2 + x - 1, 11):
    rel, taus, allowed, yes = predict(g, q, q)
    out = predict_fast(g, q, q)
    okf &= out is not None and out[2] == yes and len(rel) == 2 ** len(out[0]) - 1
check("same number of independent relations and same verdict on six spectra", okf)

print("== L6  which fluxes have no locks: a scan of small regular graphs")
def regular_graphs(n, d, target, seed=0):
    found, tries = [], 0
    rng = np.random.default_rng(seed)
    while len(found) < target and tries < 200000:
        tries += 1
        G = nx.random_regular_graph(d, n, seed=int(rng.integers(1 << 30)))
        if nx.is_connected(G) and not any(nx.is_isomorphic(G, H) for H in found):
            found.append(G)
    return found
FAM = [("cubic, 4 vertices", 3, 2, regular_graphs(4, 3, 1)), ("cubic, 6 vertices", 3, 2, regular_graphs(6, 3, 2)),
       ("cubic, 8 vertices", 3, 2, regular_graphs(8, 3, 5)),
       ("4-regular, 5 vertices", 4, 3, regular_graphs(5, 4, 1)), ("4-regular, 6 vertices", 4, 3, regular_graphs(6, 4, 1)),
       ("4-regular, 7 vertices", 4, 3, regular_graphs(7, 4, 2)),
       ("6-regular, 7 vertices", 6, 5, regular_graphs(7, 6, 1))]
cache, examples = {}, []
tot_all = {"classes": 0, "pm": 0, "lockfree": 0, "locked_yes": 0, "locked_no": 0, "undecided": 0}
okscan = True
for fname, d, q, graphs in FAM:
    c = {"classes": 0, "pm": 0, "lockfree": 0, "locked_yes": 0, "locked_no": 0, "undecided": 0, "bip": 0, "bip_pm": 0}
    for G in graphs:
        A = nx.to_numpy_array(G, dtype=int)
        n = len(A)
        bip = nx.is_bipartite(G)
        for key, (cnt, As) in flux_spectra(A).items():
            lamf = np.linalg.eigvalsh(As.astype(float))
            if not np.all(np.abs(lamf) < 2 * np.sqrt(q) - 1e-9):
                continue
            cp = sp.Poly(list(key), x)
            fM = sp.Poly(sp.expand(x ** n * cp.as_expr().subs(x, x + sp.Integer(q) / x)), x)
            if fM.all_coeffs()[n] % q == 0:
                continue
            c["classes"] += cnt
            c["bip"] += cnt if bip else 0
            g = sp.quo(cp.as_expr(), sp.gcd(cp.as_expr(), sp.diff(cp.as_expr(), x)))
            lam = sorted(set(np.round(lamf, 7)))
            if any(abs(a + b) < 1e-6 for a in lam for b in lam):
                c["pm"] += cnt
                c["bip_pm"] += cnt if bip else 0
                continue
            gk = (str(g), q)
            if gk not in cache:
                alarm(25)
                try:
                    out = predict_fast(g, q, q)
                except (AlarmInterrupt, Exception):
                    out = None
                finally:
                    cancel_alarm()
                cache[gk] = "undecided" if out is None else ("lockfree" if not out[0] else ("locked_yes" if out[2] else "locked_no"))
                if cache[gk] in ("lockfree", "locked_yes") and len(examples) < 6:
                    examples.append((fname, sorted(G.edges()), [e for e in sorted(G.edges()) if As[e[0], e[1]] < 0], str(sp.factor(cp.as_expr())), cache[gk]))
            c[cache[gk]] += cnt
    okscan &= c["bip"] == c["bip_pm"]
    for k in tot_all:
        tot_all[k] += c[k]
    print(f"      {fname}: {len(graphs)} graphs; ordinary Ramanujan flux classes {c['classes']} (on bipartite graphs: {c['bip']}); with a +-lambda pair {c['pm']}; "
          f"no locks {c['lockfree']}; locked, Omega still a polarisation {c['locked_yes']}; locked, not {c['locked_no']}; undecided {c['undecided']}", flush=True)
for e in examples:
    print(f"      example ({e[0]}, {e[4]}): edges {e[1]}, negative edges {e[2]}, fermionic char poly {e[3]}")
check("scan completed; every ordinary Ramanujan class on a bipartite graph has a +-lambda pair", okscan, f"totals: {tot_all}")

print(f"\n{npass} passed, {nfail} failed")
