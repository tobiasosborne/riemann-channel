"""REFUTE scratch (family-vacuum.md sections 1 and 3, M1, M2, M4).
(1) symbolic one-mode identities; (2) Proposition 1 (iii)=>(i) constructed numerically on random commuting
families of my own (block-diagonal rotations conjugated by a random symplectic matrix), including a step with a
Krein-indefinite eigenspace; (3) counter-checks of the hypotheses; (4) zeta: 50 zero pairs, p = 2,3,5."""
import sympy as sp, numpy as np, mpmath as mp, math
from scipy.linalg import expm, sqrtm, inv
q, qq, l, ll = sp.symbols('q qp lam lamp', real=True)
Mq = sp.Matrix([[0, -1], [q, l]]); Mp = sp.Matrix([[0, -1], [qq, ll]])
Vq = sp.simplify(q*Mq.inv()); Vp = sp.simplify(qq*Mp.inv())
Om = sp.Matrix([[0, 1], [-1, 0]])
print('(1a) V_q =', Vq.tolist(), ' M^T Om M = q Om:', sp.simplify(Mq.T*Om*Mq-q*Om) == sp.zeros(2))
J = (Mq-Vq)/sp.sqrt(4*q-l**2)
print('     J_q =', sp.simplify(J*sp.sqrt(4*q-l**2)).tolist(), '/sqrt(4q-l^2); J^2 = -1:', sp.simplify(J*J+sp.eye(2)) == sp.zeros(2), '; Om J =', sp.simplify(Om*J*sp.sqrt(4*q-l**2)).tolist())
print('(1b) [M_q,M_q\'] =', sp.expand(Mq*Mp-Mp*Mq).tolist(), ';  M_q V_q\' =', sp.expand(Mq*Vp).tolist())
# (2) Proposition 1, (iii) => (i) by averaging, on my own example
rng = np.random.default_rng(7)
def R(t): return np.array([[math.cos(t), -math.sin(t)], [math.sin(t), math.cos(t)]])
def blockdiag(bs):
    k = sum(b.shape[0] for b in bs); out = np.zeros((k, k)); i = 0
    for b in bs: out[i:i+b.shape[0], i:i+b.shape[0]] = b; i += b.shape[0]
    return out
nm = 4; n2 = 2*nm
Om0 = blockdiag([np.array([[0, 1.], [-1, 0]])]*nm)
# random symplectic P = expm(Om0^{-1} Sym)
Sx = rng.normal(size=(n2, n2)); Sx = Sx+Sx.T
Psym = expm(np.linalg.inv(Om0)@Sx*0.3)
print('P symplectic:', np.allclose(Psym.T@Om0@Psym, Om0))
qs = [2., 3., 5.]
# step 1 has a repeated eigenvalue on modes 0,1 with OPPOSITE orientation (Krein-indefinite), others generic
thetas = {2.: [0.7, -0.7, 1.9, 2.5], 3.: [0.4, 1.1, -2.2, 0.3], 5.: [1.3, 0.2, 0.9, -1.0]}
steps = {p: Psym@blockdiag([math.sqrt(p)*R(t) for t in thetas[p]])@np.linalg.inv(Psym) for p in qs}
print('steps commute:', all(np.allclose(steps[a]@steps[b], steps[b]@steps[a]) for a in qs for b in qs), ' similitudes:', all(np.allclose(steps[p].T@Om0@steps[p], p*Om0) for p in qs))
# averaging over the compact closure: the closure is a torus; average over a long word sample (Weyl equidistribution)
S = {p: steps[p]/math.sqrt(p) for p in qs}
G0 = np.eye(n2); G = np.zeros((n2, n2)); K = 0
for a in range(-12, 13):
    for b in range(-12, 13):
        for c in range(-12, 13):
            g = np.linalg.matrix_power(S[2.], a % 1000) if a >= 0 else np.linalg.matrix_power(np.linalg.inv(S[2.]), -a)
            g = g@(np.linalg.matrix_power(S[3.], b) if b >= 0 else np.linalg.matrix_power(np.linalg.inv(S[3.]), -b))
            g = g@(np.linalg.matrix_power(S[5.], c) if c >= 0 else np.linalg.matrix_power(np.linalg.inv(S[5.]), -c))
            G += g.T@G0@g; K += 1
G /= K
# NB a finite average is not exactly invariant; build the exactly invariant form instead from the torus structure:
# exact Haar average over the torus closure = projection onto the commutant; do it by averaging over the full torus in the diagonal frame
Pi = np.linalg.inv(Psym); Gd = Psym.T@G0@Psym  # form in diagonal frame
acc = np.zeros((n2, n2)); T = 64
for ks in np.ndindex(*([T]*nm)) if nm <= 3 else []:
    pass
# exact: in the frame where all S are block rotations, the closure contains the full torus T^nm iff angles are rationally independent;
# averaging over T^nm of g^T Gd g kills off-diagonal blocks and replaces each 2x2 diagonal block by its scalar part
Gavg_d = np.zeros((n2, n2))
for i in range(nm):
    blk = Gd[2*i:2*i+2, 2*i:2*i+2]; Gavg_d[2*i:2*i+2, 2*i:2*i+2] = 0.5*np.trace(blk)*np.eye(2)
Gex = Pi.T@Gavg_d@Pi
inv_ok = all(np.allclose(S[p].T@Gex@S[p], Gex) for p in qs)
A = np.linalg.solve(Gex, Om0)
Jm = -A@np.real(inv(sqrtm(-A@A)))
print('averaged G invariant under all S:', inv_ok, '; positive:', np.linalg.eigvalsh(Gex).min() > 0)
print('J = -A(-A^2)^{-1/2}: J^2=-1', np.allclose(Jm@Jm, -np.eye(n2)), '; commutes with steps', all(np.allclose(Jm@steps[p], steps[p]@Jm) for p in qs),
      '; Om J symmetric', np.allclose(Om0@Jm, (Om0@Jm).T), '; Om J > 0:', np.linalg.eigvalsh(0.5*(Om0@Jm+(Om0@Jm).T)).min() > 0)
# the finite-word average: how close to invariant
print('finite-word average (25^3 words) invariance defect:', max(np.abs(S[p].T@G@S[p]-G).max() for p in qs))
# Uniqueness: step 2 has a Krein-indefinite eigenspace (angles 0.7 and -0.7 on two modes, same eigenvalue pair)
# -> its vacua form a positive-dimensional family; exhibit a second vacuum of M_2 alone that is not the family's.
# In the diagonal frame, mixing modes 0,1 by a hyperbolic boost preserving Om and commuting with diag(R(0.7),R(-0.7)).
Jd = blockdiag([R(math.pi/2)]*nm)
Bst = np.eye(n2); s = 0.8
# boost on modes 0,1: commutes with R(t)+R(-t) structure: use the U(1,1) element acting on C^2 (mode0 as z, mode1 as conj z)
E = np.zeros((n2, n2)); E[0:2, 2:4] = np.eye(2)*0; 
# generic construction: search symplectic X in commutant of D2=diag(R(.7),R(-.7)) with X J X^-1 != J via exp of commutant Lie algebra elements
D2 = blockdiag([R(t) for t in thetas[2.]])
basis = []
for i in range(n2):
    for j in range(n2):
        Y = np.zeros((n2, n2)); Y[i, j] = 1; basis.append(Y)
# Lie algebra sp: Om0 Y symmetric; commute with D2: solve linear system
rows = []
for Y in basis:
    rows.append(np.concatenate([(D2@Y-Y@D2).ravel(), (Om0@Y+(Om0@Y).T).ravel()]))
Mx = np.array(rows).T
u, sv, vt = np.linalg.svd(Mx); null = vt[np.sum(sv > 1e-9):]
found = None
for v in null:
    Y = sum(c*b for c, b in zip(v, basis)); X = expm(Y)
    J2 = X@Jd@np.linalg.inv(X)
    if not np.allclose(J2, Jd, atol=1e-6): found = (Y, J2); break
if found:
    Y, J2 = found
    print('Krein-indefinite step: second vacuum of M_2 exists:', np.allclose(J2@J2, -np.eye(n2)), np.allclose(J2@D2, D2@J2),
          np.linalg.eigvalsh(0.5*(Om0@J2+(Om0@J2).T)).min() > 0, '; commutes with the other steps?',
          all(np.allclose(J2@blockdiag([R(t) for t in thetas[p]]), blockdiag([R(t) for t in thetas[p]])@J2) for p in [3., 5.]))
print('dim of sp-commutant of step 2 (Lie algebra):', len(null), '(= 1 per simple mode pair + dim u(1,1)=4 for the indefinite pair -> 2+4 = 6 expected)')
# (4) zeta
mp.mp.dps = 20
gam = [float(mp.im(mp.zetazero(k))) for k in range(1, 51)]
Omf = np.array([[0, 1.], [-1, 0]]); Jz = R(math.pi/2)
for p in [2, 3, 5]:
    neg = 0; ok = True
    for g in gam:
        Mp_ = math.sqrt(p)*R(g*math.log(p)); Vp_ = p*np.linalg.inv(Mp_)
        Wf = 0.5*Omf@(Mp_-Vp_); ev = np.linalg.eigvalsh(0.5*(Wf+Wf.T)); neg += np.sum(ev < 0)
        ok &= np.allclose(Mp_.T@Omf@Mp_, p*Omf) and np.allclose(Jz@Mp_, Mp_@Jz) and np.allclose(np.abs(np.linalg.eigvals(Mp_)), math.sqrt(p))
        ok &= np.allclose(np.sort(ev), np.sort([math.sqrt(p)*math.sin(g*math.log(p))]*2))
    print(f'zeta p={p}: similitude/commute-with-J/modulus/Weil-eigs ok {ok}; Om J = I: {np.allclose(Omf@Jz, np.eye(2))}; negative Weil eigenvalues {neg} of 100')
for p, pp in [(2, 3), (2, 5), (3, 5)]:
    hyp = 0; hypinv = 0; comm = 0
    for g in gam:
        Bp = np.array([[0, -1], [p, 2*math.sqrt(p)*math.cos(g*math.log(p))]]); Bq = np.array([[0, -1], [pp, 2*math.sqrt(pp)*math.cos(g*math.log(pp))]])
        hyp += abs(np.trace(Bp@Bq))/math.sqrt(p*pp) > 2+1e-12
        hypinv += abs(np.trace(Bp@np.linalg.inv(Bq)))*math.sqrt(pp/p) > 2+1e-12
        comm += np.allclose(Bp@Bq, Bq@Bp)
    print(f'Bass-doubled ({p},{pp}): B_pB_q hyperbolic on {hyp}/50, B_pB_q^-1 hyperbolic on {hypinv}/50, commuting on {comm}/50')
