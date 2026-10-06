#!/usr/bin/env python3
"""Checks for 'The lattice without a lift' (notes/adelic-gkp/no-lift.md).

Setting (graph-super.md, lattice-tower.md). A Z_2 flux on a (q+1)-regular graph gives the signed adjacency A_s and the
fermionic step M = [[0, -1], [q, A_s]] on L = Z^{2n}, with M^T Omega M = q Omega, Omega = [[0, I], [-I, 0]],
Omega(x, y) = x^T Omega y, V = q M^{-1} = [[A_s, 1], [-q, 0]], Weil form (1/2) Omega (M - V) = [[q, A_s/2], [A_s/2, 1]].
Examples: K4 with one negative edge (q = 2), Petersen with the dodecahedral flux (q = 2), K5 with the pentagon
negative (q = 3: K5 is 4-regular). The fluxes are rebuilt exactly as in check_super_gkp.py.

PARI/GP is driven by subprocess (`gp -q -f`); cypari2 is not used.
Run:  python3 check_no_lift.py > output_no_lift.txt
"""
import itertools
import subprocess
import numpy as np
import sympy as sp

npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


def gp(script, timeout=300):
    r = subprocess.run(["gp", "-q", "-f"], input=script, capture_output=True, text=True, timeout=timeout)
    if "***" in r.stdout or "***" in r.stderr:
        raise RuntimeError("gp error:\n" + r.stdout + r.stderr)
    return r.stdout.strip()


# ------------------------------------------------------------------------------------------ graphs and fluxes (as in check_super_gkp.py)
def from_edges(n, edges):
    A = np.zeros((n, n), dtype=np.int64)
    for a, b in edges:
        A[a, b] = A[b, a] = 1
    return A

def K(n):
    return from_edges(n, [(a, b) for a in range(n) for b in range(a + 1, n)])

def petersen():
    e = [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] + [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return from_edges(10, e)

def edges_of(A):
    n = len(A)
    return [(a, b) for a in range(n) for b in range(a + 1, n) if A[a, b]]

def signed(A, neg):
    As = A.copy()
    for a, b in neg:
        assert A[a, b]
        As[a, b] = As[b, a] = -1
    return As

def spanning_tree(A):
    n, seen, tree, stack = len(A), {0}, [], [0]
    while stack:
        v = stack.pop()
        for w in range(n):
            if A[v, w] and w not in seen:
                seen.add(w)
                tree.append((min(v, w), max(v, w)))
                stack.append(w)
    return tree

def flux_classes(A):
    tree = set(spanning_tree(A))
    cot = [e for e in edges_of(A) if e not in tree]
    for bits in itertools.product((0, 1), repeat=len(cot)):
        neg = [e for e, b in zip(cot, bits) if b]
        yield neg, signed(A, neg)


x, y = sp.symbols("x y")
A4, AP, A5 = K(4), petersen(), K(5)
target = np.sort(np.array([-np.sqrt(5)] * 3 + [0.0] * 4 + [np.sqrt(5)] * 3))
dod = [(neg, As) for neg, As in flux_classes(AP)
       if np.allclose(np.sort(np.linalg.eigvalsh(As.astype(float))), target, atol=1e-9)]
EX = {
    "K4, one negative edge": (signed(A4, [(0, 1)]), 2, 2, 1),
    "Petersen, dodecahedral flux": (dod[0][1], 2, 2, 1),
    "K5, pentagon negative": (signed(A5, [(i, (i + 1) % 5) for i in range(5)]), 3, 3, 1),
}   # name: (A_s, q, p, r) with q = p^r


def step(As, q):
    n = len(As)
    return sp.Matrix(sp.BlockMatrix([[sp.zeros(n), -sp.eye(n)], [q * sp.eye(n), sp.Matrix(As.tolist())]]).as_explicit())

def omega(n):
    return sp.Matrix(sp.BlockMatrix([[sp.zeros(n), sp.eye(n)], [-sp.eye(n), sp.zeros(n)]]).as_explicit())

def gpmat(A):
    return "[" + ";".join(",".join(str(int(v)) for v in row) for row in np.array(A).tolist()) + "]"

def pd_exact(Q):
    """exact positive definiteness by Gaussian elimination over Q (all pivots > 0)"""
    Q = sp.Matrix(Q)
    n = Q.shape[0]
    for k in range(n):
        if Q[k, k] <= 0:
            return False
        for i in range(k + 1, n):
            f = Q[i, k] / Q[k, k]
            Q[i, :] = Q[i, :] - f * Q[k, :]
    return True


print("== N1  the examples: fluxes, spectra, the step")
check("Petersen: the dodecahedral spectrum (+-sqrt5 three times, 0 four times) occurs for 2 of 64 flux classes; the first is used",
      len(dod) == 2, f"negative non-tree edges of the class used: {dod[0][0]}")
EXPECT_A = {"K4, one negative edge": (x - 1) * (x + 1) * (x**2 - 5),
            "Petersen, dodecahedral flux": x**4 * (x**2 - 5)**3,
            "K5, pentagon negative": x * (x**2 - 5)**2}
DATA = {}
for name, (As, q, p, r) in EX.items():
    n = len(As)
    A = sp.Matrix(As.tolist())
    M = step(As, q)
    Om = omega(n)
    V = q * M.inv()
    ok_reg = all(sum(abs(int(v)) for v in row) == q + 1 for row in As.tolist())
    ok_sym = (M.T * Om * M - q * Om).is_zero_matrix
    ok_V = all(v.is_integer for v in V) and V == sp.Matrix(sp.BlockMatrix([[A, sp.eye(n)], [-q * sp.eye(n), sp.zeros(n)]]).as_explicit())
    ok_A = sp.expand(A.charpoly(x).as_expr() - EXPECT_A[name]) == 0
    check(f"{name}: (q+1)-regular with q = {q}; charpoly of A_s = {sp.factor(EXPECT_A[name])}; M^T Omega M = q Omega; V = qM^-1 = [[A_s, 1], [-q, 0]] integral",
          ok_reg and ok_sym and ok_V and ok_A)
    DATA[name] = dict(A=A, M=M, V=V, Om=Om, n=n, q=q, p=p, r=r, As=As)

print("== N2  characteristic polynomial of M, factored over Z")
EXPECT_P = {"K4, one negative edge": [(x**2 - x + 2, 1), (x**2 + x + 2, 1), (x**4 - x**2 + 4, 1)],
            "Petersen, dodecahedral flux": [(x**2 + 2, 4), (x**4 - x**2 + 4, 3)],
            "K5, pentagon negative": [(x**2 + 3, 1), (x**4 + x**2 + 9, 2)]}
for name, d in DATA.items():
    cp = d["M"].charpoly(x).as_expr()
    c, fl = sp.factor_list(cp)
    got = sorted((str(sp.expand(f)), e) for f, e in fl)
    exp = sorted((str(sp.expand(f)), e) for f, e in EXPECT_P[name])
    d["P"] = sp.expand(cp)
    d["factors"] = EXPECT_P[name]
    check(f"{name}: det(x - M) = " + " * ".join(f"({sp.expand(f)})^{e}" if e > 1 else f"({sp.expand(f)})" for f, e in EXPECT_P[name]),
          c == 1 and got == exp)

print("== N3  RH and semisimplicity: Weil form positive definite (exact), radical of the charpoly kills M")
for name, d in DATA.items():
    n, q, A = d["n"], d["q"], d["A"]
    W = (d["Om"] * (d["M"] - d["V"])) / 2
    W_exp = sp.Matrix(sp.BlockMatrix([[q * sp.eye(n), A / 2], [A / 2, sp.eye(n)]]).as_explicit())
    rad = sp.prod([f for f, e in d["factors"]])
    hM = sp.zeros(2 * n)
    coeffs = sp.Poly(rad, x).all_coeffs()
    for cf in coeffs:
        hM = hM * d["M"] + cf * sp.eye(2 * n)
    lam_min = min(np.linalg.eigvalsh(np.array(W, dtype=float)))
    check(f"{name}: (1/2) Omega (M - V) = [[q, A_s/2], [A_s/2, 1]] is positive definite, so RH holds; the radical {sp.factor(rad)} annihilates M (semisimple)",
          W == W_exp and pd_exact(W) and hM.is_zero_matrix, f"smallest eigenvalue {lam_min:.4f}")

print("== N4  Centeleghe-Stix hypotheses over F_p (q prime): no eigenvalue +-sqrt(p); FV = VF = p with V integral")
for name, d in DATA.items():
    q, p, r = d["q"], d["p"], d["r"]
    g = sp.gcd(d["P"], x**2 - q)
    ok = (r == 1) and sp.degree(g, x) == 0 and (d["M"] * d["V"] - q * sp.eye(2 * d["n"])).is_zero_matrix
    check(f"{name}: q = {q} is prime, gcd(det(x - M), x^2 - {q}) = 1, MV = VM = {q}", ok)

print("== N5  Honda-Tate data for each irreducible factor (PARI): local invariants at the primes above p, e, Newton slopes")
HT = r"""
ht(f,p,r)={my(nf=nfinit(f),P=idealprimedec(nf,p),inv=vector(#P),e=1);
 for(i=1,#P, my(pr=P[i], v=nfeltval(nf,variable(f),pr), vq=r*pr.e); inv[i]=frac(v/vq*pr.e*pr.f); e=lcm(e,denominator(inv[i])));
 if(polsturm(f)>0, e=lcm(e,2));
 [inv, e, newtonpoly(f,p)/r]};
"""
FACT_INFO = {}
for name, d in DATA.items():
    p, r, q = d["p"], d["r"], d["q"]
    for f, e in d["factors"]:
        key = (str(sp.expand(f)), q)
        if key in FACT_INFO:
            continue
        out = gp(HT + f"my(t=ht({key[0].replace('**', '^')},{p},{r})); print(t[2]); print(t[3]); print(t[1]);")
        lines = out.splitlines()
        e_inv = int(lines[0])
        slopes = [sp.Rational(s) for s in lines[1].strip("[]").split(",")]
        FACT_INFO[key] = (e_inv, slopes)
        deg = sp.degree(f, x)
        prank = sum(1 for s in slopes if s == 0)
        kind = "ordinary" if prank == deg // 2 else ("supersingular" if all(s == sp.Rational(1, 2) for s in slopes) else "mixed")
        npts = int(sp.Poly(f, x).eval(1))
        check(f"over F_{q}: {key[0]}: all local invariants 0 (e = {e_inv}), so a simple isogeny class of dimension {deg // 2} with exactly this Weil polynomial; "
              f"slopes {[str(s) for s in slopes]}: {kind}; #A(F_{q}) = {npts}",
              e_inv == 1 and (kind != "mixed"), f"invariants {lines[2]}")
for name, d in DATA.items():
    q = d["q"]
    prank = sum(e * sum(1 for s in FACT_INFO[(str(sp.expand(f)), q)][1] if s == 0) for f, e in d["factors"])
    dim = d["n"]
    npts = int(sp.Poly(d["P"], x).eval(1))
    lap = int((sp.Matrix(sp.eye(dim)) * (q + 1) - d["A"]).det())
    check(f"{name}: dimension {dim}, p-rank {prank}; #A(F_{q}) = det(1 - M) = det((q+1) - A_s) = {npts}",
          npts == lap, "almost ordinary (p-rank g - 1)" if prank == dim - 1 else ("ordinary" if prank == dim else "neither ordinary nor almost ordinary"))

print("== N6  the half turn: det(x - M) = Q(x^2), so up to isogeny a Weil restriction from F_{q^2} when Q is a Weil polynomial there")
for name, d in DATA.items():
    q, p, r = d["q"], d["p"], d["r"]
    P = sp.Poly(d["P"], x)
    even = all(m[0] % 2 == 0 for m in P.monoms())
    Q = sp.expand(d["P"].subs(x, sp.sqrt(y)))
    degQ = sp.degree(Q, y)
    cQ, fQ = sp.factor_list(Q)
    ok = even and sp.expand(Q.subs(y, x**2) - d["P"]) == 0
    det = f"Q(y) = {sp.factor(Q)}, degree {degQ}"
    if degQ % 2 == 1:
        check(f"{name}: spectrum of A_s symmetric, det(x - M) = Q(x^2); Q has odd degree, so it is not the Weil polynomial of any abelian variety over F_{q*q}",
              ok and degQ % 2 == 1, det)
    else:
        # each factor of Q over F_{q^2}: Honda-Tate e, and the multiplicity must be a multiple of e times (deg factor) ... check Q = prod m_i^{e_i k_i}
        okf = True
        info = []
        for f, m in fQ:
            out = gp(HT + f"my(t=ht({str(sp.expand(f.subs(y, x))).replace('**', '^')},{p},{2 * r})); print(t[2]);")
            ee = int(out)
            okf &= (m % ee == 0)
            info.append(f"{sp.expand(f)}: e={ee}, mult {m}")
        check(f"{name}: det(x - M) = Q(x^2) and every factor of Q over F_{q*q} occurs to a multiple of its Honda-Tate e, so Q is a Weil polynomial over F_{q*q}",
              ok and okf, det + "; " + "; ".join(info))

print("== N7  genus-2 Jacobians (PARI hyperellcharpoly over all models y^2 + h y = f, deg h <= 3, deg f <= 6)")
G2_F2 = r"""
T=Map(); cnt=0;
{for(a=1,2^4-1, for(b=0,2^7-1,
  my(h=Pol(binary(a+16))-x^4, f=Pol(binary(b+128))-x^7, cp);
  if(max(2*poldegree(h),poldegree(f))<5, next);
  cp=iferr(hyperellcharpoly(Mod(1,2)*[f,h]),E,0);
  if(cp==0,next); cnt++;
  if(mapisdefined(T,cp), mapput(T,cp,mapget(T,cp)+1), mapput(T,cp,1))))};
g(P)=if(mapisdefined(T,P),mapget(T,P),0);
print(cnt); print(g(x^4-x^2+4)); print(g(x^4+3*x^2+4)); print(hyperellcharpoly(Mod(1,2)*[x^5+1,x^2+x]));
cntpts(f,h,p,k)={my(g0=ffgen(p^k,'t),g=ffprimroot(g0),N=0,els=concat([0*g],vector(p^k-1,i,g^i)),H=polcoef(h,3),F6=polcoef(f,6));
 for(i=1,#els, my(X=els[i], hx=subst(h,x,X)*g^0, fx=subst(f,x,X)*g^0);
   for(j=1,#els, my(Y=els[j]); if(Y^2+hx*Y-fx==0, N++)));
 for(j=1,#els, my(Y=els[j]); if(Y^2+H*g^0*Y-F6*g^0==0, N++));
 N};
print(vector(4,k,cntpts(x^5+1,x^2+x,2,k)));
"""
out = gp(G2_F2).splitlines()
nsmooth, nS, nprod, cpC, cnts = int(out[0]), int(out[1]), int(out[2]), out[3], eval(out[4])
def pred_counts(Pexpr, q, kmax):
    rts = np.roots([float(c) for c in sp.Poly(Pexpr, x).all_coeffs()])
    return [int(round((q**k + 1 - np.sum(rts**k)).real)) for k in range(1, kmax + 1)]
predS = pred_counts(x**4 - x**2 + 4, 2, 4)
check("over F_2: 768 smooth genus-2 models; 16 have Weil polynomial x^4 - x^2 + 4, so the simple surface of K4 and Petersen is a Jacobian",
      nsmooth == 768 and nS == 16, f"smooth {nsmooth}, matching {nS}")
check("C: y^2 + (x^2 + x) y = x^5 + 1 over F_2 has charpoly x^4 - x^2 + 4; brute-force counts over F_2, F_4, F_8, F_16 agree",
      cpC == "x^4 - x^2 + 4" and cnts == predS, f"counts {cnts}, predicted {predS}")
check("over F_2: no smooth genus-2 model has Weil polynomial x^4 + 3x^2 + 4 = (x^2 - x + 2)(x^2 + x + 2) (the product E_2pts x E_4pts of K4)",
      nprod == 0)
G2_F3 = r"""
n=0; hit=List();
{forvec(v=vector(7,i,[0,2]), my(f=Pol(Vecrev(v))); if(poldegree(f)<5,next); if(poldisc(Mod(1,3)*f)==0,next); n++;
  my(cp=hyperellcharpoly(Mod(1,3)*f)); if(cp==x^4+x^2+9, listput(hit,f)))};
print(n); print(#hit); print(hit[1]);
cntpts(f,h,p,k)={my(g0=ffgen(p^k,'t),g=ffprimroot(g0),N=0,els=concat([0*g],vector(p^k-1,i,g^i)),H=polcoef(h,3),F6=polcoef(f,6));
 for(i=1,#els, my(X=els[i], hx=subst(h,x,X)*g^0, fx=subst(f,x,X)*g^0);
   for(j=1,#els, my(Y=els[j]); if(Y^2+hx*Y-fx==0, N++)));
 for(j=1,#els, my(Y=els[j]); if(Y^2+H*g^0*Y-F6*g^0==0, N++));
 N};
print(vector(3,k,cntpts(hit[1],0,3,k)));
"""
out = gp(G2_F3).splitlines()
n3, h3, f3, c3 = int(out[0]), int(out[1]), out[2], eval(out[3])
pred3 = pred_counts(x**4 + x**2 + 9, 3, 3)
check(f"over F_3: {n3} squarefree models y^2 = f, deg f in (5, 6); {h3} have Weil polynomial x^4 + x^2 + 9 (the ordinary surface of K5); "
      f"y^2 = {f3} has brute-force counts {c3} over F_3, F_9, F_27", h3 > 0 and c3 == pred3, f"predicted {pred3}")

print("== N8  the invariant vacuum J = (M - V)(D + D), D = (4q - A_s^2)^(-1/2); compared with the spectral construction")
for name, d in DATA.items():
    n, q = d["n"], d["q"]
    M = np.array(d["M"], dtype=float)
    V = q * np.linalg.inv(M)
    Om = np.array(d["Om"], dtype=float)
    A = np.array(d["A"], dtype=float)
    w, U = np.linalg.eigh(4 * q * np.eye(n) - A @ A)
    D = U @ np.diag(w ** -0.5) @ U.T
    J = (M - V) @ np.block([[D, np.zeros((n, n))], [np.zeros((n, n)), D]])
    mu, W = np.linalg.eig(M)
    Jspec = (W @ np.diag(1j * np.sign(mu.imag)) @ np.linalg.inv(W)).real
    G = Om @ J
    ok = (np.allclose(J @ J, -np.eye(2 * n)) and np.allclose(J @ M, M @ J) and np.allclose(J.T @ Om @ J, Om)
          and np.allclose(G, G.T) and np.min(np.linalg.eigvalsh((G + G.T) / 2)) > 0 and np.allclose(J, Jspec, atol=1e-8))
    lam = np.linalg.eigvalsh(A)
    th = sorted(set(float(t) for t in np.round(np.arccos(lam / (2 * np.sqrt(q))) / np.pi, 4)))
    d["J"] = J
    check(f"{name}: J^2 = -1, JM = MJ, J symplectic, Omega(x, Jx) > 0, and J equals U diag(i sign Im mu) U^-1",
          ok, f"mode frequencies theta/pi = {th}; min eigenvalue of Omega J = {np.min(np.linalg.eigvalsh((G + G.T) / 2)):.4f}")

print("== N9  the supersingular block: the vacuum is the normalised step; the p-adic valuation does not choose a CM type")
for name, d in DATA.items():
    if "K4" in name:
        continue
    n, q, p = d["n"], d["q"], d["p"]
    Mx = d["M"]
    K = (Mx * Mx + q * sp.eye(2 * n)).nullspace()
    B = np.array(sp.Matrix.hstack(*K), dtype=float)
    J = d["J"]
    ok = np.allclose(np.sqrt(q) * J @ B, np.array(Mx, dtype=float) @ B)
    out = gp(f"nf=nfinit(x^2+{q}); P=idealprimedec(nf,{p}); print(#P); print(P[1].e); print(nfeltval(nf,x,P[1])); print(nfeltval(nf,-x,P[1])); print(idealval(nf,{q},P[1]));").splitlines()
    ok2 = out[0] == "1" and out[1] == "2" and out[2] == out[3] == "1" and out[4] == "2"
    check(f"{name}: on ker(M^2 + {q}) (rank {B.shape[1]}) the vacuum is J = M/sqrt({q}), a quarter turn",
          ok and B.shape[1] == 2 * (4 if "Petersen" in name else 1))
    check(f"{name}: {p} is ramified in Q(sqrt(-{q})); mu = i sqrt({q}) and its conjugate -mu have the same valuation (slope 1/2), "
          f"so Deligne's rule val_p(phi(F)) > 0 selects neither embedding", ok2)

print("== N10  the ordinary block: every prime above p sees mu and -mu alike (Howe's half-turn obstruction)")
for f, q, p in ((x**4 - x**2 + 4, 2, 2), (x**4 + x**2 + 9, 3, 3)):
    fs = str(f).replace("**", "^")
    out = gp(f"""f={fs}; nf=nfinit(subst(f,x,y)); r=nfroots(nf,f); P=idealprimedec(nf,{p});
print(#P); {{for(i=1,#P, my(S=vector(4,j,nfeltval(nf,r[j],P[i])>0), ok=1);
  for(j=1,4, for(k=1,4, if(r[k]==-r[j] && S[j]!=S[k], ok=0))); print(ok))}}""").splitlines()
    nP = int(out[0])
    check(f"{f} over F_{q}: Galois quartic, roots +-mu, +-conj(mu); at each of the {nP} primes above {p} the set of non-units is closed under mu -> -mu",
          all(o == "1" for o in out[1:]) and nP == 2)

print("== N11  the lattice does not split: [L : L_ss + L_ord] and the forms on the pieces")
SPLIT = r"""
stepM(A,q)={my(n=#A); matconcat([0*A,-matid(n);q*matid(n),A])};
Om(n)=matconcat([0*matid(n),matid(n);-matid(n),0*matid(n)]);
doit(A,q,hss,hord)={my(n=#A,M=stepM(A,q),Bss,Bord,O=Om(n));
  Bss=matkerint(subst(hss,x,M)); Bord=matkerint(subst(hord,x,M));
  print(abs(matdet(matconcat([Bss,Bord])))); print(matdet(Bss~*O*Bss)); print(matdet(Bord~*O*Bord))};
"""
for name, hss, hord, exp in (("Petersen, dodecahedral flux", "x^2+2", "x^4-x^2+4", (5**6, 5**6, 5**6)),
                             ("K5, pentagon negative", "x^2+3", "x^4+x^2+9", (25, 25, 25))):
    d = DATA[name]
    out = gp(SPLIT + f"doit({gpmat(d['As'])},{d['q']},{hss},{hord});").splitlines()
    got = tuple(int(v) for v in out)
    check(f"{name}: L_ss = L cap ker({hss})(M), L_ord = L cap ker({hord})(M): index [L : L_ss + L_ord] = {got[0]}; det Omega on L_ss, L_ord = {got[1]}, {got[2]}",
          got == exp)

for f, e, q in ((x**4 - x**2 + 4, 3, 2), (x**4 + x**2 + 9, 2, 3)):
    Pord = sp.Poly(sp.expand(f**e), x)
    g = sp.degree(Pord) // 2
    mid = Pord.coeff_monomial(x**g)
    check(f"(L_ord, M): characteristic polynomial ({f})^{e}, middle coefficient {mid} prime to {q}: a Deligne module of rank {2 * g} over F_{q}",
          mid % q != 0)

print("== N12  twisted forms Omega(x, (C + C) y), C symmetric integral commuting with A_s")
UNITS = r"""
Rbasis(A)={my(n=#A,B=Mat([concat(Vec(matid(n))), concat(Vec(A)), concat(Vec(A^2))]), S=matrixqz(B,-2)); matsolve(B~*B, B~*S)};
search(A,N)={my(T=Rbasis(A),c0=0,cnt=0);
  forvec(v=vector(3,i,[-N,N]), my(c=T*v~, a=c[1], nm=(c[1]+5*c[3])^2-5*c[2]^2);
     if(abs(a)==1 && abs(nm)==1, cnt++; if(nm==-1, c0++)));
  print(T); print(cnt); print(c0)};
"""
for name in ("Petersen, dodecahedral flux", "K5, pentagon negative"):
    d = DATA[name]
    out = gp(UNITS + f"search({gpmat(d['As'])},30);").splitlines()
    check(f"{name}: R = Q[A_s] cap M_n(Z) has basis {out[0]} in (1, A_s, A_s^2); among the {out[1]} units with coordinates in [-30, 30], "
          f"none has opposite signs at +-sqrt5", int(out[2]) == 0 and int(out[1]) > 0)
# an explicit unimodular C for K5 outside Q[A_s], positive on E(sqrt5), negative on E(-sqrt5)
d = DATA["K5, pentagon negative"]
C = sp.Matrix([[2, -2, 3, 1, -5], [-2, 1, -3, -1, 4], [3, -3, -3, 0, 2], [1, -1, 0, 0, -1], [-5, 4, 2, -1, -1]])
A = d["A"]
Ep = (A - sp.sqrt(5) * sp.eye(5)).nullspace()
Em = (A + sp.sqrt(5) * sp.eye(5)).nullspace()
E0 = A.nullspace()
def restr(Cm, basis):
    Bm = sp.Matrix.hstack(*basis)
    return np.linalg.eigvalsh(np.array((Bm.T * Cm * Bm).evalf(), dtype=float))
sp_, sm_, s0_ = restr(C, Ep), restr(C, Em), restr(C, E0)
inQA = sp.Matrix.hstack(sp.eye(5).reshape(25, 1), A.reshape(25, 1), (A * A).reshape(25, 1)).rank() == \
       sp.Matrix.hstack(sp.eye(5).reshape(25, 1), A.reshape(25, 1), (A * A).reshape(25, 1), C.reshape(25, 1)).rank()
check("K5: an integral symmetric C with CA_s = A_sC, det C = -1, positive definite on E(sqrt5), negative definite on E(-sqrt5); C is not in Q[A_s]",
      C == C.T and (C * A - A * C).is_zero_matrix and C.det() == -1 and min(sp_) > 0 and max(sm_) < 0 and not inQA,
      f"restricted eigenvalues: E(+) {np.round(sp_, 3)}, E(-) {np.round(sm_, 3)}, E(0) {np.round(s0_, 3)}")
Jn = d["J"]
P = np.block([[np.array(C, dtype=float), np.zeros((5, 5))], [np.zeros((5, 5)), np.array(C, dtype=float)]])
Mn = np.array(d["M"], dtype=float)
Omn = np.array(d["Om"], dtype=float)
G = Omn @ P @ Jn
check("K5: Omega_C(x, y) = Omega(x, (C + C) y) is unimodular, satisfies Omega_C(Mx, y) = Omega_C(x, Vy), and is NOT positive for the vacuum J (indefinite)",
      abs(round(np.linalg.det(Omn @ P))) == 1 and np.allclose(Mn.T @ Omn @ P, Omn @ P @ (3 * np.linalg.inv(Mn)))
      and np.allclose(G, G.T) and np.min(np.linalg.eigvalsh(G)) < 0 < np.max(np.linalg.eigvalsh(G)))
d = DATA["Petersen, dodecahedral flux"]
PET = r"""
symcomm(A)={my(n=#A,E=List());
  for(i=1,n,for(j=i,n, my(S=matrix(n,n)); S[i,j]=1; S[j,i]=1; listput(E,S)));
  my(L=matrix(n*n,#E,r,c, my(X=E[c]*A-A*E[c]); X[(r-1)\n+1,(r-1)%n+1]), K=matkerint(L));
  vector(#K,k, sum(c=1,#E,K[c,k]*E[c]))};
A=AMAT; B=symcomm(A); n=#A;
Bv=matrix(n*n,#B,r,c,B[c][(r-1)\n+1,(r-1)%n+1]); U=qflll(Bv); B2=vector(#B,k,matrix(n,n,i,j,(Bv*U[,k])[(i-1)*n+j]));
D=mateigen(A*1.,1); V=D[2]; vals=D[1];
ip=[i|i<-[1..n],abs(vals[i]-sqrt(5))<1e-8]; im=[i|i<-[1..n],abs(vals[i]+sqrt(5))<1e-8];
Pp=vecextract(V,ip); Pm=vecextract(V,im); nu=0; hit=0; pats=Map();
setrand(3); {for(t=1,200000, my(S=vector(4,i,random(#B2)+1), c=vector(4,i,random(7)-3), C=sum(k=1,4,c[k]*B2[S[k]]), d=matdet(C)); if(abs(d)==1, nu++;
  my(s1=qfsign(Pp~*C*Pp), s2=qfsign(Pm~*C*Pm)); if((s1==[3,0]&&s2==[0,3])||(s1==[0,3]&&s2==[3,0]), hit++);
  mapput(pats,[s1[1],s2[1]],1)))};
print(#B); print(#ip); print(#im); print(nu); print(hit); print(#Mat(pats)~);
""".replace("AMAT", gpmat(d["As"]))
out = gp(PET, timeout=600).splitlines()
check("Petersen: symmetric commutant of A_s has rank 22; in a sparse search on its LLL basis (2e5 samples, 4 terms, coefficients in [-3, 3]) "
      "no unimodular C is definite of opposite signs on E(sqrt5), E(-sqrt5)",
      out[0] == "22" and out[1] == out[2] == "3" and int(out[3]) > 1000 and out[4] == "0",
      f"unimodular samples {out[3]}, sign-changing {out[4]}; (positive-count on E+, on E-) patterns realised: {out[5]} of 16 (a search, not a proof)")

def rosati_dims(As, q):
    """exact ranks with python-flint: unknowns X (2n x 2n) with XM = MX and X^T Omega = Omega X; C (n x n) with CA = AC, C = C^T"""
    import flint
    n = len(As)
    M = np.array(step(As, q), dtype=np.int64)
    Om = np.array(omega(n), dtype=np.int64)
    A = np.array(As, dtype=np.int64)
    def kernel_dim(m, f):
        E = np.eye(m * m, dtype=np.int64)
        cols = [f(E[k].reshape(m, m)).ravel() for k in range(m * m)]
        Mat = np.array(cols).T
        return m * m - flint.fmpz_mat([[int(v) for v in row] for row in Mat.tolist()]).rank()
    full = kernel_dim(2 * n, lambda X: np.concatenate([(X @ M - M @ X).ravel(), (X.T @ Om - Om @ X).ravel()]))
    sub = kernel_dim(n, lambda C: np.concatenate([(C @ A - A @ C).ravel(), (C - C.T).ravel()]))
    return full, sub
for name, exp in (("K4, one negative edge", (4, 4)), ("K5, pentagon negative", (9, 7)), ("Petersen, dodecahedral flux", (34, 22))):
    got = rosati_dims(DATA[name]["As"], DATA[name]["q"])
    check(f"{name}: Rosati-fixed commutant of M (all compatible forms Omega(x, Py)) has rank {got[0]}; the subfamily P = C + C has rank {got[1]}",
          got == exp)

print()
print(f"{npass} of {npass + nfail} pass" + ("" if nfail == 0 else f"  ({nfail} FAIL)"))
