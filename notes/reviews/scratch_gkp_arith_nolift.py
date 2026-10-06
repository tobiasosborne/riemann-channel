"""REFUTE scratch (no-lift.md), written from the statements only.
Graphs, fluxes, Frobenius polynomials, Honda-Tate data via PARI, Weil restriction,
genus-2 Jacobians by brute force, gluing index, the order R = Q[A_s] cap M_n(Z), the K5 twist C."""
import itertools, subprocess, sympy as sp, numpy as np, networkx as nx
from sympy import Matrix, symbols, factor_list, Poly, ZZ
x, y = symbols('x y')

def gp(cmd):
    return subprocess.run(['gp', '-q', '-f'], input=cmd, capture_output=True, text=True).stdout.strip()

def flux_classes(G):
    T = nx.minimum_spanning_tree(G)
    cot = [e for e in G.edges() if not T.has_edge(*e)]
    return cot

def signed_adj(G, neg):
    n = G.number_of_nodes(); A = sp.zeros(n, n)
    for (u, v) in G.edges():
        s = -1 if (u, v) in neg or (v, u) in neg else 1
        A[u, v] = s; A[v, u] = s
    return A

def step(A, q):
    n = A.shape[0]
    return sp.BlockMatrix([[sp.zeros(n), -sp.eye(n)], [q*sp.eye(n), A]]).as_explicit()

def prank(P, p):
    c = Poly(P, x).all_coeffs()  # leading first: a_0=1, a_1,...
    r = 0
    for i, a in enumerate(c):
        if a % p != 0: r = i
        if i > len(c)//2: break
    return r

out = {}
# ---- K4 one negative edge, q = 2
K4 = nx.complete_graph(4)
A4 = signed_adj(K4, {(0, 1)})
# ---- Petersen: search all 2^6 classes for spectrum x^4 (x^2-5)^3
P10 = nx.petersen_graph()
cot = flux_classes(P10)
target = sp.expand(x**4*(x**2-5)**3)
hits = []
for bits in itertools.product([0, 1], repeat=len(cot)):
    neg = {e for e, b in zip(cot, bits) if b}
    A = signed_adj(P10, neg)
    if sp.expand(A.charpoly(x).as_expr() - target) == 0:
        hits.append((bits, A))
print('Petersen: classes with dodecahedral spectrum:', len(hits), 'of', 2**len(cot))
AP = hits[0][1]
# ---- K5 pentagon negative, q = 3
K5 = nx.complete_graph(5)
A5 = signed_adj(K5, {(i, (i+1) % 5) for i in range(5)})
cases = [('K4', A4, 2), ('Petersen', AP, 2), ('K5', A5, 3)]
for name, A, q in cases:
    M = step(A, q)
    cpA = sp.factor(A.charpoly(x).as_expr())
    cpM = M.charpoly(x).as_expr()
    fl = factor_list(cpM)
    Q = sp.expand(cpM.subs(x, sp.sqrt(y)))
    n = A.shape[0]
    W = sp.BlockMatrix([[q*sp.eye(n), A/2], [A/2, sp.eye(n)]]).as_explicit()
    ev = min(np.linalg.eigvalsh(np.array(W.evalf(), dtype=float)))
    sq = sp.prod([f for f, m in fl[1]])
    annih = (sp.Poly(sq, x).as_expr())
    # evaluate squarefree part at M
    coeffs = Poly(sq, x).all_coeffs(); Z = sp.zeros(2*n)
    for c in coeffs: Z = Z*M + c*sp.eye(2*n)
    print(f'\n{name}: q={q}, charpoly(A_s) = {cpA}')
    print('  det(x-M) =', sp.factor(cpM), ' p-rank =', prank(sp.expand(cpM), q), ' #A(F_q)=det(1-M) =', cpM.subs(x, 1))
    print('  min eig Weil form =', round(ev, 4), ' squarefree part annihilates M:', Z.is_zero_matrix)
    print('  Q(y) with det(x-M)=Q(x^2):', sp.factor(Q) if Q.is_polynomial(y) else 'not a polynomial in x^2')
    out[name] = (A, M, q, fl)

# ---- Honda-Tate invariants for each irreducible factor with PARI
print('\nHonda-Tate (PARI): for each factor f over F_q, root pi, list inv_v at v|p, real places, e, slopes')
fac = [('x^2-x+2', 2), ('x^2+x+2', 2), ('x^4-x^2+4', 2), ('x^2+2', 2), ('x^4+x^2+9', 3), ('x^2+3', 3),
       ('y^2+3*y+4', 4), ('y^2-y+4', 4), ('y+2', 4), ('y+3', 9), ('y^2+y+9', 9)]
for f, q in fac:
    v = 'x' if 'x' in f else 'y'
    cmd = f"""f={f}; q={q}; p=factor(q)[1,1]; K=nfinit(subst(f,{v},x)); pid=idealprimedec(K,p);
    inv=vector(#pid,j,(nfeltval(K,x,pid[j])/(valuation(q,p)*1.))*pid[j].e*pid[j].f/1.);
    sl=vector(#pid,j,nfeltval(K,x,pid[j])/(valuation(q,p)*pid[j].e));
    print([f, q, K.r1, inv, sl, K.disc, poldegree(f)]);"""
    print(' ', gp(cmd))

# ---- Weil restriction facts over F_4
print('\nTraces over F_4 of base changes of F_2 curves (a^2-4):', sorted({a*a-4 for a in range(-2, 3)}))

# ---- genus-2 Jacobians by brute force over F_{2^k}
def gf2_mul(a, b, mod, k):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
        if a >> k & 1: a ^= mod
    return r
IRR = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}
def count_F2k(h, f, k):
    mod = IRR[k]; q = 2**k
    def ev(poly, t):  # poly coeffs low->high in F_2
        r = 0; pw = 1
        for c in poly:
            if c: r ^= pw
            pw = gf2_mul(pw, t, mod, k)
        return r
    N = 0
    for t in range(q):
        ht, ft = ev(h, t), ev(f, t)
        for s in range(q):
            if gf2_mul(s, s, mod, k) ^ gf2_mul(ht, s, mod, k) ^ ft == 0: N += 1
    # points at infinity: Y^2 + h3 Y = f6
    h3 = h[3] if len(h) > 3 else 0; f6 = f[6] if len(f) > 6 else 0
    for s in range(q):
        if gf2_mul(s, s, mod, k) ^ (s if h3 else 0) ^ (1 if f6 else 0) == 0: N += 1
    return N
h = [0, 1, 1]; f = [1, 0, 0, 0, 0, 1]   # y^2 + (x^2+x) y = x^5 + 1
cnt = [count_F2k(h, f, k) for k in range(1, 5)]
print('\nC: y^2+(x^2+x)y=x^5+1 over F_2^k, k=1..4: brute-force counts', cnt)
# Weil polynomial x^4 - x^2 + 4 prediction
r = sp.Poly(x**4 - x**2 + 4, x).nroots()
print('  predicted from x^4-x^2+4:', [round(float(sp.re(2**k + 1 - sum(z**k for z in r)))) for k in range(1, 5)])
# exhaustive over F_2 and F_3 models with PARI (smoothness via hyperelldisc / poldisc)
cmd = r"""
c=0; cs=0; ce=0;
for(hb=0,15, for(fb=0,127, H=sum(i=0,3,bittest(hb,i)*x^i); F=sum(i=0,6,bittest(fb,i)*x^i); \
  if(poldegree(4*F+H^2)<5, next); D=hyperelldisc([F,H]); if(D%2==0, next); c++; \
  cp=hyperellcharpoly(Mod(1,2)*[F,H]); if(cp==x^4-x^2+4, cs++); if(cp==x^4+3*x^2+4, ce++)));
print("F2 models: smooth=",c," with x^4-x^2+4: ",cs,"  with x^4+3x^2+4: ",ce);
c=0; cs=0; for(fb=0,3^7-1, v=digits(fb+3^7,3); F=sum(i=0,6,v[8-i]*x^i); if(poldegree(F)<5, next); \
  if(poldisc(F)%3==0, next); c++; if(hyperellcharpoly(Mod(1,3)*F)==x^4+x^2+9, cs++));
print("F3 models y^2=f: squarefree deg 5/6 = ",c,"  with x^4+x^2+9: ",cs);
F=2*x^6+2*x^5+x^3+x+1; print1("F3 example brute counts k=1..3: "); for(k=1,3, g=ffgen(3^k,'a); q=3^k; r=ffprimroot(g); N=0; \
  for(i=0,q-1, t=if(i==0,0*g,r^i); v=subst(F,x,t); if(v==0,N+=1, if(issquare(v),N+=2))); \
  N+= if(issquare(2*g^0),2,0); print1(N," ")); print("");
"""
print(gp(cmd))

# ---- K4: is the graph lattice the Deligne module of a PRODUCT (E2 x E4-part) x (S-part)?  gluing index
cmd = r"""A=[0,-1,1,1;-1,0,1,1;1,1,0,1;1,1,1,0]; M=matconcat([matrix(4,4),-matid(4);2*matid(4),A]);
K12=matkerint(subst((x^2-x+2)*(x^2+x+2),x,M)); K3=matkerint(subst(x^4-x^2+4,x,M));
K1=matkerint(subst(x^2-x+2,x,M)); K2=matkerint(subst(x^2+x+2,x,M));
print("K4: [L : L(E2xE4) + L(S)] = ", factor(abs(matdet(concat(K12,K3)))), ";  [L : L1+L2+L3] = ", factor(abs(matdet(concat([K1,K2,K3])))));"""
print(gp(cmd))

# ---- gluing and det Omega
def gp_mat(Mz):
    return '[' + ';'.join(','.join(str(int(Mz[i, j])) for j in range(Mz.shape[1])) for i in range(Mz.shape[0])) + ']'
for name in ['Petersen', 'K5']:
    A, M, q, fl = out[name]
    n = A.shape[0]
    Mss = M*M + q*sp.eye(2*n)
    hord = [f for f, m in fl[1] if sp.degree(f, x) == 4][0]
    Hc = Poly(hord, x).all_coeffs(); Hm = sp.zeros(2*n)
    for c in Hc: Hm = Hm*M + c*sp.eye(2*n)
    Om = sp.BlockMatrix([[sp.zeros(n), sp.eye(n)], [-sp.eye(n), sp.zeros(n)]]).as_explicit()
    cmd = f"""M={gp_mat(M)}; Kss=matkerint({gp_mat(Mss)}); Kord=matkerint({gp_mat(Hm)}); Om={gp_mat(Om)};
    print([#Kss, #Kord, factor(abs(matdet(concat(Kss,Kord)))), factor(matdet(Kss~*Om*Kss)), factor(matdet(Kord~*Om*Kord))]);
    Mord=matsolve(Kord, M*Kord); print(factor(charpoly(Mord)), " middle coeff ", polcoeff(charpoly(Mord), poldegree(charpoly(Mord))/2));"""
    print(f'\n{name}: [rank ss, rank ord, index, det Omega|ss, det Omega|ord]:', gp(cmd))
    # order R = Q[A] cap M_n(Z): saturate span{I,A,A^2}
    basis = [sp.eye(n), A, A*A]
    Bm = Matrix([[b[i, j] for b in basis] for i in range(n) for j in range(n)])
    cmd = f"""B={gp_mat(Bm)}; S=matsnf(B); v=select(t->t!=0,S); print("elementary divisors of Z[A] in M_n(Z): ", v, "  => [R : Z[A]] = ", vecprod(v));"""
    print('  ', gp(cmd))
    # test (A+A^2)/2 integrality and any other candidates p(A)/m for small m
    found = []
    for m in [2, 3, 5]:
        for a, b, c in itertools.product(range(m), repeat=3):
            if (a, b, c) == (0, 0, 0): continue
            X = (a*sp.eye(n) + b*A + c*A*A)
            if all(v % m == 0 for v in X): found.append(((a, b, c), m))
    print('  extra integral elements (a+bA+cA^2)/m found:', found)

# ---- K5 twist C
C = Matrix([[2, -2, 3, 1, -5], [-2, 1, -3, -1, 4], [3, -3, -3, 0, 2], [1, -1, 0, 0, -1], [-5, 4, 2, -1, -1]])
print('\nK5 C: symmetric', C == C.T, ' det', C.det(), ' commutes with my A_s (pentagon 0-1-2-3-4)', (C*A5 - A5*C).is_zero_matrix)
# search over relabelings for one with which C commutes
ok = []
for perm in itertools.permutations(range(5)):
    neg = {(perm[i], perm[(i+1) % 5]) for i in range(5)}
    A = signed_adj(K5, neg)
    for g in itertools.product([1, -1], repeat=5):
        D = sp.diag(*g); Ag = D*A*D
        if (C*Ag - Ag*C).is_zero_matrix: ok.append((perm, g, Ag))
print('  relabelings/gauges of the pentagon flux with [C,A_s]=0:', len(ok))
if ok:
    Ag = ok[0][2]
    An = np.array(Ag, dtype=float); Cn = np.array(C, dtype=float)
    w, U = np.linalg.eigh(An)
    for lam in [np.sqrt(5), -np.sqrt(5), 0.0]:
        Ub = U[:, np.abs(w - lam) < 1e-8]
        print(f'  C on E({lam:+.3f}): eigenvalues', np.round(np.linalg.eigvalsh(Ub.T @ Cn @ Ub), 4))

# ---- vacuum: closed form J = (M-V)(D+D), D=(4q-A^2)^{-1/2}; on ker(M^2+q) it equals M/sqrt q
for name in ['Petersen', 'K5']:
    A, M, q, fl = out[name]; n = A.shape[0]
    An = np.array(A, dtype=float); Mn = np.array(M, dtype=float); Vn = q*np.linalg.inv(Mn)
    w, U = np.linalg.eigh(4*q*np.eye(n) - An@An); D = U@np.diag(w**-0.5)@U.T
    J = (Mn - Vn)@np.block([[D, 0*D], [0*D, D]])
    Om = np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])
    ker = sp.Matrix(M*M + q*sp.eye(2*n)).nullspace(); Kn = np.array(sp.Matrix.hstack(*ker), dtype=float)
    print(f'{name}: |J^2+1|={np.abs(J@J+np.eye(2*n)).max():.1e} |JM-MJ|={np.abs(J@Mn-Mn@J).max():.1e} '
          f'min eig sym(Om J)={np.linalg.eigvalsh((Om@J+(Om@J).T)/2).min():.3f} |(J - M/sqrt q) on ker(M^2+q)|={np.abs((J-Mn/np.sqrt(q))@Kn).max():.1e}')
