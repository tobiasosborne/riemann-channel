#!/usr/bin/env python3
"""Checks for 'The per-mode sign' (notes/adelic-gkp/sign-vector.md).

Needs PARI through cypari2 (see check_howe_positivity.py for the scratch-venv recipe).

Setting. Distinct fermionic eigenvalues lambda_j (real, |lambda_j| < 2 sqrt q, p-adic units; q = p prime).
mu_j^+- = (lambda_j +- delta_j)/2 with delta_j = i sqrt(4q - lambda_j^2) in the upper half-plane, D_j = lambda_j^2 - 4q.
For a prime P above p of the splitting field, sigma_j(P) = +1 iff mu_j^+ lies in P (the forward-rotating root is the
p-adic non-unit). Omega is a Howe polarisation at P iff sigma is constant.

Locking rule tested here. N+ = Galois closure of Q(lambda_1, ..., lambda_m), a totally real field.
Rel = { I : prod_{j in I} D_j is a square in N+ } (then |I| is even).  For I in Rel and a prime p+ of N+ above p,
    prod_{j in I} sigma_j = tau_I(p+) := +1 if val(rho_I - 1) > val(rho_I + 1), else -1,
    rho_I = (-1)^(|I|/2) sqrt(prod D_j) / prod lambda_j   (positive square root in the fixed real embedding),
and the sign vectors realised by the primes above p+ are exactly the solutions of these equations.
"""
import itertools
import numpy as np
import sympy as sp
import cypari2

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

def weil_poly(g, q):
    """f(x) = x^m g(x + q/x): the distinct Frobenius eigenvalues"""
    m = sp.Poly(g, x).degree()
    return sp.Poly(sp.expand(sp.simplify(x ** m * g.subs(x, x + sp.Integer(q) / x))), x).as_expr()

def truth(g, q):
    """PARI ground truth: number of primes P above p with S_P = Phi_+ or its conjugate; and the set of sign vectors
    (indexed by the eigenvalues lambda, in increasing order)"""
    f = P(weil_poly(g, q))
    spl = pari.nfsplitting(f)
    N = pari.nfinit(pari.subst(spl, "x", "y"))
    rts = N.nfroots(f)
    theta = pari.polroots(N.nf_get_pol())[0]
    vals = [complex(pari.subst(pari.lift(r), "y", theta)) for r in rts]
    lam = sorted({round((v + q / v).real, 9) for v in vals})
    primes = N.idealprimedec(q)
    patterns = set()
    for Pr in primes:
        sig = {}
        for r, v in zip(rts, vals):
            if v.imag > 0:
                sig[round((v + q / v).real, 9)] = 1 if int(N.idealval(r, Pr)) > 0 else -1
        patterns.add(tuple(sig[l] for l in lam))
    const = sum(1 for s in patterns if len(set(s)) == 1)
    return int(pari.poldegree(spl)), len(primes), patterns, const > 0, lam

def predict(g, q):
    """the locking rule, computed in the totally real field N+ only"""
    gp = P(g)
    spl = pari.nfsplitting(gp)
    Np = pari.nfinit(pari.subst(spl, "x", "y"))
    lam = Np.nfroots(gp)
    th = [t for t in pari.polroots(Np.nf_get_pol()) if abs(complex(t).imag) < 1e-12][0]
    num = lambda e: complex(pari.subst(pari.lift(e), "y", th)).real
    order = sorted(range(len(lam)), key=lambda j: num(lam[j]))
    lam = [lam[j] for j in order]
    D = [l * l - 4 * q for l in lam]
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
                rho = (-1) ** (k // 2) * r / lp
                rel.append((I, rho))
    primes = Np.idealprimedec(q)
    allowed = set()
    taus = []
    for Pr in primes:
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
    yes = any(all(t == 1 for t in tau.values()) for tau in taus)
    return int(pari.poldegree(spl)), [I for I, _ in rel], allowed, yes, [round(num(l), 9) for l in lam]


# ------------------------------------------------------------------------------------------ S1
print("== S1  one mode: the two roots are told apart by rotation at the real place and by attraction at p")
for lam, q in ((-1, 2), (-2, 5), (1, 7), (4, 7)):
    p, k = q, 12
    mod = p ** k
    u = lam % mod
    for _ in range(60):
        u = (lam - q * pow(u, -1, mod)) % mod               # cavity recursion u -> lambda - q/u, p-adically
    ok = (u * u - lam * u + q) % mod == 0 and (u - lam) % p == 0
    z = lam + 1e-3j
    w = 1.0 + 0.3j
    for _ in range(200000):
        w = z - q / w                                        # the same recursion at the real place, with lambda + i0
    mu_plus = (lam + 1j * np.sqrt(4 * q - lam * lam)) / 2
    ok &= abs(w - mu_plus) < 2e-2 and w.imag > 0
    w0, drift = 1.0 + 0.3j, []
    for _ in range(50):
        w0 = lam - q / w0
        drift.append(abs(w0 - mu_plus))
    ok &= max(drift) - min(drift) > 0.1                      # without i0 it does not converge: an elliptic Moebius map
    # the lattice splits p-adically along the two eigen-lines: (1,-U) and (1,-N) form a basis since U - N is a unit
    n_ = (lam - u) % mod
    ok &= (u - n_) % p != 0 and n_ % p == 0
    check(f"lambda = {lam}, q = {q}: p-adic recursion converges to the unit root; with +i0 the real recursion converges to the upper root; "
          f"without it, it rotates; Z_p^2 splits along the two eigen-lines", ok, f"unit root = {u % p**3} mod {p}^3")

# ------------------------------------------------------------------------------------------ S2
print("== S2  the locking rule against the PARI ground truth, on spectra")
CASES = [
    ("K4, one negative edge", (x - 1) * (x + 1) * (x ** 2 - 5), 2),
    ("K6 flux", (x + 1) * (x ** 3 - 3 * x ** 2 - 9 * x + 19), 5),
    ("{2, 4}", (x - 2) * (x - 4), 5),
    ("{-2, 4}", (x + 2) * (x - 4), 5),
    ("{1, 2, 4}", (x - 1) * (x - 2) * (x - 4), 5),
    ("{1, 5}", (x - 1) * (x - 5), 7),
    ("{1, 4}", (x - 1) * (x - 4), 7),
    ("{4, 5}", (x - 4) * (x - 5), 7),
    ("{-4, 1, 5}", (x + 4) * (x - 1) * (x - 5), 7),
    ("{1, 4, 5}", (x - 1) * (x - 4) * (x - 5), 7),
    ("{1 +- 2 sqrt 3}", x ** 2 - 2 * x - 11, 5),
    ("{golden ratio pair}", x ** 2 - x - 1, 3),
    ("{golden ratio pair}", x ** 2 - x - 1, 2),
]
TAB = []
for name, g, q in CASES:
    dN, nP, pats, yes_t, lam = truth(g, q)
    dNp, rel, allowed, yes_p, lam2 = predict(g, q)
    ok = (pats == allowed) and (yes_t == yes_p) and np.allclose(lam, lam2)
    TAB.append((name, q, lam, rel, len(pats), yes_t))
    check(f"q = {q}, eigenvalues {name}: realised sign vectors = solutions of the locking equations; constant vector realised: {yes_t}", ok,
          f"splitting degree {dN}, real field degree {dNp}, relations {rel}, {len(pats)} sign vectors of {2 ** len(lam)}")

# ------------------------------------------------------------------------------------------ S3
print("== S3  rational eigenvalues: the lock is lambda/m mod p, with 4q - lambda^2 = d m^2")
def cls(lam, q):
    val = 4 * q - lam * lam
    d = sp.core.numbers.Integer(val)
    sf = sp.Integer(1)
    for pr, e in sp.factorint(val).items():
        if e % 2:
            sf *= pr
    m = sp.sqrt(sp.Integer(val) / sf)
    return int(sf), (lam * pow(int(m), -1, q)) % q
ok = True
rows = []
for q, lams in ((7, (1, 4, 5, -4, -1, -5)), (5, (2, 4, -2, -4, 1, -1)), (2, (1, -1))):
    for a, b in itertools.combinations(lams, 2):
        da, ca = cls(a, q)
        db, cb = cls(b, q)
        if da != db:
            continue
        same = ca == cb if q != 2 else None
        if q == 2:
            # p = 2: decide by the general rule
            _, rel, allowed, _, _ = predict((x - a) * (x - b), q)
            same = (1, 1) in allowed
        _, _, pats, _, lam = truth((x - a) * (x - b), q)
        locked_same = (1, 1) in pats
        ok &= same == locked_same
        rows.append((q, a, b, da, "same" if locked_same else "opposite"))
check("for every pair with the same field, 'lambda/m equal mod p' decides whether the two signs agree", ok,
      "; ".join(f"q={r[0]}: ({r[1]},{r[2]}) Q(sqrt-{r[3]}) {r[4]}" for r in rows[:8]) + " ...")

# ------------------------------------------------------------------------------------------ S4
print("== S4  all ordinary Ramanujan flux classes of K4, K5, the cube and K6")
def from_edges(n, edges):
    A = np.zeros((n, n), dtype=int)
    for a, b in edges:
        A[a, b] = A[b, a] = 1
    return A
def Kn(n):
    return from_edges(n, [(a, b) for a in range(n) for b in range(a + 1, n)])
def prism(m):
    return from_edges(2 * m, [(i, (i + 1) % m) for i in range(m)] + [(m + i, m + (i + 1) % m) for i in range(m)] + [(i, m + i) for i in range(m)])
def classes(A):
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
        cp = sp.Poly(sp.Matrix(As.tolist()).charpoly(x).as_expr(), x)
        key = tuple(cp.all_coeffs())
        out.setdefault(key, [0, As])[0] += 1
    return out
summary = []
okall = True
for gname, A, q in (("K4", Kn(4), 2), ("K5", Kn(5), 3), ("cube", prism(4), 2), ("K6", Kn(6), 5)):
    for key, (cnt, As) in classes(A).items():
        lamf = np.linalg.eigvalsh(As.astype(float))
        if not np.all(np.abs(lamf) < 2 * np.sqrt(q) - 1e-9):
            continue
        cp = sp.Poly(list(key), x)
        n = len(As)
        fM = sp.Poly(sp.expand(x ** n * cp.as_expr().subs(x, x + sp.Integer(q) / x)), x)
        if fM.all_coeffs()[n] % q == 0:
            continue
        g = sp.quo(cp.as_expr(), sp.gcd(cp.as_expr(), sp.diff(cp.as_expr(), x)))
        dNp, rel, allowed, yes_p, lam = predict(g, q)
        pm = any(abs(a + b) < 1e-7 for a in lam for b in lam)
        if pm:
            okall &= not yes_p                       # the proposition of howe-positivity.md
            verdict = "NO (has a +-lambda pair)"
        else:
            dN, nP, pats, yes_t, _ = truth(g, q)
            okall &= (pats == allowed) and (yes_t == yes_p)
            verdict = ("YES" if yes_t else "NO") + f" (no +-lambda pair; checked with PARI, splitting degree {dN})"
        summary.append((gname, q, cnt, str(sp.factor(cp.as_expr())), len(rel), verdict))
for s in summary:
    print(f"      {s[0]} (q={s[1]}): {s[2]} classes, spectrum {s[3]}, {s[4]} relations: Omega a polarisation: {s[5]}")
check("the rule agrees with the proposition on every class with a +-lambda pair, and with PARI on every class without", okall,
      f"{len(summary)} spectra, {sum(s[2] for s in summary)} flux classes")

print(f"\n{npass} passed, {nfail} failed")
