"""REFUTE scratch (family-vacuum.md section 2, M3): my own LPS pair. PGL_2(F_5) as 2x2 matrices mod scalars;
S_p = {a0^2+a1^2+a2^2+a3^2 = p, a0 > 0 odd, a1,a2,a3 even}; phi(a) = [[a0 + i a1, a2 + i a3], [-a2 + i a3, a0 - i a1]] with i = 3
(3^2 = -1 mod 5; the other square root, unlike the construction in scripts/), Cayley graphs by LEFT multiplication.
Then: commutation, joint spectrum, steps M_q, Omega, Weil forms, commutant (direct linear solve on sub-blocks
and the block argument), M13 V17, hyperbolicity counts, per-plane commutator norms."""
import numpy as np, itertools, math
from collections import Counter
P = 5; I5 = 3
def norm_m(m):
    m = [x % P for x in m]
    for x in m:
        if x:
            inv = pow(x, P-2, P); return tuple(y*inv % P for y in m)
def mm(a, b): return norm_m([a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3], a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]])
G = sorted({norm_m(m) for m in itertools.product(range(P), repeat=4) if (m[0]*m[3]-m[1]*m[2]) % P})
idx = {g: i for i, g in enumerate(G)}; n = len(G)
def gens(p):
    r = int(math.isqrt(p)); out = []
    for a in itertools.product(range(-r, r+1), repeat=4):
        if a[0] > 0 and a[0] % 2 == 1 and all(x % 2 == 0 for x in a[1:]) and sum(x*x for x in a) == p: out.append(a)
    return out
def phi(a): return norm_m([a[0]+I5*a[1], a[2]+I5*a[3], -a[2]+I5*a[3], a[0]-I5*a[1]])
def adj(p):
    S = [phi(a) for a in gens(p)]; A = np.zeros((n, n), int)
    for g in G:
        for s in S: A[idx[mm(s, g)], idx[g]] += 1
    return A, len(S)
A13, k13 = adj(13); A17, k17 = adj(17)
print('|PGL2(F5)| =', n, ' degrees', k13, k17, ' symmetric', (A13 == A13.T).all(), (A17 == A17.T).all(), ' simple', A13.max(), A17.max())
print('A13 A17 == A17 A13:', (A13@A17 == A17@A13).all())
# joint spectrum
H = A13 + math.sqrt(2)*A17
w, U = np.linalg.eigh(H)
l13 = np.round(np.einsum('ij,ik,kj->j', U, A13, U), 8); l17 = np.round(np.einsum('ij,ik,kj->j', U, A17, U), 8)
js = Counter(zip(l13, l17))
print('joint spectrum (lambda13, lambda17): mult ->', sorted(js.items(), key=lambda t: -t[0][0]))
nontriv = {k: v for k, v in js.items() if abs(abs(k[0])-14) > 1e-6}
print('number of nontrivial joint eigenspaces', len(nontriv), ' dim W =', sum(nontriv.values()),
      ' all integer', all(abs(a-round(a)) < 1e-6 and abs(b-round(b)) < 1e-6 for a, b in nontriv), ' strictly Ramanujan', all(a*a < 52 and b*b < 68 for a, b in nontriv))
print('sum m^2 =', sum(v*v for v in nontriv.values()), ';  commutant of M13 alone on W predicted 2*sum over A13-eigenspaces m^2 =',
      2*sum(v*v for v in Counter([round(k[0]) for k, m in nontriv.items() for _ in range(m)]).values()))
Z = np.zeros((n, n)); I = np.eye(n)
def M(q, A): return np.block([[Z, -I], [q*I, A]])
def Vq(q, A): return np.block([[A, I], [-q*I, Z]])
Om = np.block([[Z, I], [-I, Z]])
M13, M17 = M(13, A13), M(17, A17); V13, V17 = Vq(13, A13), Vq(17, A17)
print('similitudes:', np.allclose(M13.T@Om@M13, 13*Om), np.allclose(M17.T@Om@M17, 17*Om), ' V = q M^-1:', np.allclose(V13, 13*np.linalg.inv(M13)), np.allclose(V17, 17*np.linalg.inv(M17)))
Cm = M13@M17-M17@M13
print('[M13,M17] = [[-4I, A13-A17],[17A13-13A17, 4I]]:', np.allclose(Cm, np.block([[-4*I, A13-A17], [17*A13-13*A17, 4*I]])))
X = M13@V17
print('M13 V17 integral:', np.allclose(X, np.round(X)), ' = [[17I,0],[13A17-17A13,13I]]:', np.allclose(X, np.block([[17*I, Z], [13*A17-17*A13, 13*I]])))
ev = np.linalg.eigvals(M13@M17); off = np.sum(np.abs(np.abs(ev)-math.sqrt(221)) > 1e-6)
print('M13 M17: eigenvalues off |mu| = sqrt(221):', off, 'of', len(ev))
# W projector and Weil forms on W (x) R^2
Uw = U[:, [j for j in range(n) if abs(abs(l13[j])-14) > 1e-6]]
Pw = np.block([[Uw, np.zeros_like(Uw)], [np.zeros_like(Uw), Uw]])
for q, Mq, V in [(13, M13, V13), (17, M17, V17)]:
    Wf = 0.5*Om@(Mq-V); Wf = 0.5*(Wf+Wf.T)
    print(f'Weil form q={q}: equals 1/2[[2q,A],[A,2]]:', np.allclose(0.5*Om@(Mq-V), 0.5*np.block([[2*q*I, (A13 if q == 13 else A17)], [(A13 if q == 13 else A17), 2*I]])),
          ' min eig on W:', round(np.linalg.eigvalsh(Pw.T@Wf@Pw).min(), 4), ' min eig on all:', round(np.linalg.eigvalsh(Wf).min(), 4))
# per-plane facts
planes = sorted(nontriv)
hyp = 0; norms = []; gen_full = True
for (a, b) in planes:
    m13 = np.array([[0, -1], [13, a]]); m17 = np.array([[0, -1], [17, b]])
    s = m13@m17/math.sqrt(221); hyp += abs(np.trace(s)) > 2
    c = (m13/math.sqrt(13))@(m17/math.sqrt(17))-(m17/math.sqrt(17))@(m13/math.sqrt(13)); norms.append(np.linalg.norm(c))
    alg = np.array([np.eye(2).ravel(), m13.ravel(), m17.ravel(), (m13@m17).ravel()]); gen_full &= np.linalg.matrix_rank(alg) == 4
print('S13 S17 hyperbolic on', hyp, 'of', len(planes), 'joint eigenspaces; those with l13*l17<=0:', sum(1 for a, b in planes if a*b <= 0),
      '; min ||[S13,S17]||_F per plane:', round(min(norms), 4), '; pair generates M2(R) on every plane:', gen_full)
# direct commutant on a sub-block: the two joint eigenspaces (4,5) and (4,3) [dims 12, 4], and on (-2,2)+(2,-2)
def commutant_dim(keys):
    cols = [j for j in range(n) if (l13[j], l17[j]) in keys]
    Ub = U[:, cols]; Pb = np.block([[Ub, np.zeros_like(Ub)], [np.zeros_like(Ub), Ub]])
    a = Pb.T@M13@Pb; b = Pb.T@M17@Pb; k = a.shape[0]; Ik = np.eye(k)
    L = np.vstack([np.kron(Ik, a)-np.kron(a.T, Ik), np.kron(Ik, b)-np.kron(b.T, Ik)])
    s = np.linalg.svd(L, compute_uv=False); return int(np.sum(s < 1e-8*s.max())), [js[x] for x in keys]
import sys
for keys in ([[(4.0, 5.0), (4.0, 3.0)], [(-2.0, 2.0), (2.0, -2.0)], [(4.0, 0.0), (-4.0, 0.0)]] if 'full' in sys.argv else [[(4.0, 5.0), (4.0, 3.0)]]):
    keys = [k for k in planes if any(abs(k[0]-x[0]) < 1e-6 and abs(k[1]-x[1]) < 1e-6 for x in keys)]
    d, ms = commutant_dim(keys); print('direct commutant of {M13,M17} on joint eigenspaces', keys, 'mults', ms, ': dim', d, 'vs sum m^2', sum(m*m for m in ms))
# vacua J_q = (M_q - V_q)(4q - A_q^2)^{-1/2} on W (x) R^2 (in the W-basis)
from scipy.linalg import sqrtm
Aw13 = Uw.T@A13@Uw; Aw17 = Uw.T@A17@Uw; k = Aw13.shape[0]; Zk = np.zeros((k, k)); Ik = np.eye(k)
def Mw(q, A): return np.block([[Zk, -Ik], [q*Ik, A]])
def Vw(q, A): return np.block([[A, Ik], [-q*Ik, Zk]])
Omw = np.block([[Zk, Ik], [-Ik, Zk]])
Js = {}
for q, A in [(13, Aw13), (17, Aw17)]:
    Dm = np.real(np.linalg.inv(sqrtm(4*q*Ik-A@A))); Dd = np.block([[Dm, Zk], [Zk, Dm]])
    J = (Mw(q, A)-Vw(q, A))@Dd; Js[q] = J
    print(f'J_{q}: J^2=-1 {np.allclose(J@J, -np.eye(2*k))}, commutes with M_{q} {np.allclose(J@Mw(q, A), Mw(q, A)@J)}, Om J sym>0 {np.allclose(Omw@J, (Omw@J).T) and np.linalg.eigvalsh(0.5*(Omw@J+(Omw@J).T)).min() > 0}')
print('max |J13 - J17| (entries, W-basis):', round(np.abs(Js[13]-Js[17]).max(), 4), '; J13 commutes with M17:', np.allclose(Js[13]@Mw(17, Aw17), Mw(17, Aw17)@Js[13]), '; J17 with M13:', np.allclose(Js[17]@Mw(13, Aw13), Mw(13, Aw13)@Js[17]))
# per-plane |J13-J17| in the (function, shifted) coordinates
print('per-plane max entry |J13-J17|:', round(max(np.abs(np.array([[-a, -2], [26, a]])/math.sqrt(52-a*a) - np.array([[-b, -2], [34, b]])/math.sqrt(68-b*b)).max() for a, b in planes), 4))
# full-W commutant via randomised rank on W (x) R^2 is too big for a dense Kronecker solve; the block argument + sub-block solves stand in.
# rotation family remark
