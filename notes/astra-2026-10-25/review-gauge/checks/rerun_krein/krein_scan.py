#!/usr/bin/env python3
"""Lane K, reproducible exact certificates and seeded SU(1,1) scans.

Run from any directory: python3 /path/to/checks/krein_scan.py
Writes output_krein_scan.txt next to this file. No input zeros, RH assumption,
network, or files outside this lane. Random successes are checked at 80 decimal
digits; the principal counterexamples have separate exact certificates.
"""
from pathlib import Path
from contextlib import redirect_stdout
import argparse
import collections
import math
import sys
import time
import numpy as np
import scipy.linalg as la
import networkx as nx
import mpmath as mp
import sympy as sp

ETA = np.diag([1., -1.])
REAL_TOL = 1e-8
CLUSTER_TOL = 1e-7
INERTIA_TOL = 1e-8
COND_LIMIT = 1e8
MP_DPS = 80


def adjacency(n, edges, gens, chord_indices, kind='np'):
    if kind == 'np':
        A, I = np.zeros((2*n, 2*n), complex), np.eye(2, dtype=complex)
    elif kind == 'mp':
        A, I = mp.zeros(2*n), mp.eye(2)
    else:
        A, I = sp.zeros(2*n), sp.eye(2)
    chord_map = dict(zip(chord_indices, gens))
    for k, (u, v) in enumerate(edges):
        G = chord_map.get(k, I)
        # For det-one 2x2 matrices the inverse is the adjugate.
        values = [[G[1, 1], -G[0, 1]], [-G[1, 0], G[0, 0]]]
        for i in range(2):
            for j in range(2):
                A[2*u+i, 2*v+j] += G[i, j]
                A[2*v+i, 2*u+j] += values[i][j]
    return A


def graph_specs():
    specs = []
    for name, G, q in [('K4', nx.complete_graph(4), 2),
                       ('Petersen', nx.petersen_graph(), 2),
                       ('K5', nx.complete_graph(5), 3),
                       ('cube', nx.cubical_graph(), 2)]:
        edges = sorted((min(u, v), max(u, v)) for u, v in G.edges())
        tree = {tuple(sorted(e)) for e in nx.bfs_edges(G, 0)}
        chords = [i for i, e in enumerate(edges) if e not in tree]
        specs.append((name, len(G), q, edges, chords))
    specs.append(('theta', 2, 2, [(0, 1)]*3, [1, 2]))
    assert [len(s[4]) for s in specs] == [3, 6, 6, 5, 2]
    return specs


def cayley_generators(params, bounded, kind='np'):
    """Parameters are exact decimal rationals, including for mp reconstruction."""
    if kind == 'np':
        num, mat, ii = float, lambda x: np.array(x, complex), 1j
    elif kind == 'mp':
        num, mat, ii = mp.mpf, mp.matrix, mp.j
    else:
        num, mat, ii = sp.Rational, sp.Matrix, sp.I
    one = num('1')
    def R(u):
        u = num(u)
        a = (one + ii*u)/(one - ii*u)
        return mat([[a, 0], [0, 1/a]])
    def B(v):
        v = num(v)
        c, s = (one+v*v)/(one-v*v), 2*v/(one-v*v)
        return mat([[c, s], [s, c]])
    if bounded:
        # Exactly cosh(log 2)=5/4, sinh(log 2)=3/4.
        G = mat([[num('1.25'), num('.75')], [num('.75'), num('1.25')]])
        Gi = mat([[num('1.25'), -num('.75')], [-num('.75'), num('1.25')]])
        return [G @ R(p[0]) @ Gi if kind == 'np' else G*R(p[0])*Gi for p in params]
    return [R(p[0]) @ B(p[1]) @ R(p[2]) if kind == 'np'
            else R(p[0])*B(p[1])*R(p[2]) for p in params]


def sample_params(rng, rank, bounded):
    # Uniform compact angles; radial t uniform on [.05,1], not a normalized
    # Haar measure on the noncompact group. Cayley values rounded to 12 decimals.
    def compact():
        return f'{math.tan(rng.uniform(-math.pi, math.pi)/2):.12f}'
    if bounded:
        return [[compact()] for _ in range(rank)]
    return [[compact(), f'{math.tanh(rng.uniform(.05, 1.)/2):.12f}', compact()]
            for _ in range(rank)]


def inertia(H):
    vals = la.eigvalsh((H+H.conj().T)/2)
    tol = INERTIA_TOL * max(1., np.max(np.abs(vals)))
    return (int(np.sum(vals > tol)), int(np.sum(vals < -tol)),
            int(np.sum(np.abs(vals) <= tol)))


def analyse(A, q):
    d = len(A)
    H = np.diag(np.tile([1., -1.], d//2))
    vals, vec = la.eig(A)
    cond = float(np.linalg.cond(vec))
    residual = la.norm(A @ vec - vec*vals)/(max(1., la.norm(A))*la.norm(vec))
    clusters = []
    for j in sorted(range(d), key=lambda k: (vals[k].real, vals[k].imag)):
        for c in clusters:
            if abs(vals[j] - np.mean(vals[c])) < CLUSTER_TOL:
                c.append(j)
                break
        else:
            clusters.append([j])
    rows, kappa = [], 0
    for c in clusters:
        z = complex(np.mean(vals[c]))
        if abs(z.imag) < REAL_TOL:
            U, singular, _ = la.svd(vec[:, c], full_matrices=False)
            sig = inertia(U.conj().T @ H @ U)
            if abs(z.real) <= 2*math.sqrt(q)+REAL_TOL:
                kappa += sig[1]
            label = str(sig)
        else:
            label = 'nonreal'
        rows.append((z, len(c), label))
    real = bool(np.max(np.abs(vals.imag)) < REAL_TOL)
    inband = real and bool(np.max(np.abs(vals.real)) <= 2*math.sqrt(q)+REAL_TOL)
    diagonal = cond < COND_LIMIT and residual < 1e-10
    Q = np.block([[H, -H@A/2], [-H@A/2, q*H]])
    assert la.norm(Q-Q.conj().T) < 1e-8
    return dict(values=vals, rows=rows, real=real, inband=inband,
                diagonal=diagonal, ram=bool(inband and diagonal),
                cond=cond, residual=residual, kappa=kappa, Q=inertia(Q),
                imag=float(np.max(np.abs(vals.imag))))


def reduced_coefficients(A, n):
    power, sums = mp.eye(2*n), []
    for k in range(1, n+1):
        power = power*A
        sums.append(sum(power[j, j] for j in range(2*n))/2)
    coefficients = [mp.mpf(1)]
    for k in range(1, n+1):
        coefficients.append(-sum(coefficients[k-j]*sums[j-1]
                                 for j in range(1, k+1))/k)
    imag_error = max(abs(mp.im(z)) for z in coefficients)
    assert imag_error < mp.mpf('1e-65'), imag_error
    return [mp.re(z) for z in coefficients], imag_error


def high_precision_check(spec, params, double_result):
    name, n, q, edges, chords = spec
    with mp.workdps(MP_DPS):
        gens = cayley_generators(params, False, 'mp')
        A = adjacency(n, edges, gens, chords, 'mp')
        coeff, imag_error = reduced_coefficients(A, n)
        guesses = sorted(z.real for z, mult, sign in double_result['rows'])
        assert len(guesses) == n and all(mult == 2 for _, mult, _ in double_result['rows'])
        roots = []
        for guess in guesses:
            z = mp.mpf(str(guess))
            root = mp.findroot(lambda r: mp.polyval(coeff, r),
                               (z-mp.mpf('1e-5'), z+mp.mpf('1e-5')),
                               tol=mp.mpf('1e-70'), maxsteps=100)
            assert isinstance(root, mp.mpf)
            roots.append(root)
        roots.sort()
        gap = min(roots[i+1]-roots[i] for i in range(n-1))
        margin = 2*mp.sqrt(q)-max(abs(r) for r in roots)
        residual = max(abs(mp.polyval(coeff, r)) for r in roots)
        assert gap > mp.mpf('1e-30') and margin > mp.mpf('1e-30')
        assert residual < mp.mpf('1e-60')
        # Disjoint tiny real sign brackets. Floating high precision, not interval
        # arithmetic; exact certification is supplied separately for named examples.
        radius = mp.mpf('1e-50')
        brackets = [mp.polyval(coeff, r-radius)*mp.polyval(coeff, r+radius) < 0
                    for r in roots]
        assert all(brackets)
        print('  MP80 verified reduced roots (each full multiplicity 2):')
        for r in roots:
            print('   ', mp.nstr(r, 60))
        print('  MP80 min_gap=', mp.nstr(gap, 25), 'band_margin=', mp.nstr(margin, 25),
              'max_polynomial_residual=', mp.nstr(residual, 8),
              'coefficient_imaginary_error=', mp.nstr(imag_error, 8),
              'all_real_sign_brackets=', all(brackets))


def print_generators(params, gens):
    print('  exact decimal Cayley parameters:', params)
    for k, G in enumerate(gens):
        print(f'  generator {k}:')
        for row in G:
            print('   ['+', '.join(f'{z.real:.15f}{z.imag:+.15f}j' for z in row)+']')


def polyval_matrix(coeff, A):
    I = sp.eye(A.rows)
    out = sp.zeros(A.rows)
    for c in coeff:
        out = out*A + c*I
    return out.applyfunc(sp.simplify)


def exact_checks():
    print('EXACT CERTIFICATES (SymPy over Q(i), or Q(i,sqrt(133)))')
    x = sp.symbols('x')
    I, eta = sp.eye(2), sp.diag(1, -1)
    g = sp.Matrix([[sp.Rational(5,4), sp.Rational(3,4)],
                   [sp.Rational(3,4), sp.Rational(5,4)]])
    h = sp.diag((-3+4*sp.I)/5, (-3-4*sp.I)/5)
    u = sp.Matrix([[1+sp.I, 1], [1, 1-sp.I]])
    for name, G in [('hyperbolic g', g), ('elliptic h', h), ('parabolic u', u)]:
        assert sp.simplify(G.det()) == 1 and (G.conjugate().T*eta*G-eta).applyfunc(sp.simplify) == sp.zeros(2)
        print(name, G, 'trace', sp.trace(G), 'det=1 and eta-unitary EXACT')
    A2 = adjacency(2, [(0,1)]*2, [u], [1], 'sp')
    assert (A2*A2).applyfunc(sp.simplify) == 4*sp.eye(4)
    print('two-edge parabolic charpoly=', sp.factor(A2.charpoly(x).as_expr()), 'A^2=4I EXACT')
    At = adjacency(2, [(0,1)]*3, [g,h], [1,2], 'sp')
    assert (At*At).applyfunc(sp.simplify) == sp.Rational(14,5)*sp.eye(4)
    print('theta nonelementary charpoly=', sp.factor(At.charpoly(x).as_expr()), 'A^2=(14/5)I EXACT')
    print('theta eigenvalues +/-', sp.N(sp.sqrt(sp.Rational(14,5)), 60), 'each twice')
    R = sp.diag((4+3*sp.I)/5, (4-3*sp.I)/5)
    Ab = adjacency(2, [(0,1)]*3, [I,R], [1,2], 'sp')
    assert (Ab*Ab).applyfunc(sp.simplify) == sp.Rational(41,5)*sp.eye(4)
    print('theta bounded outside-band delta=41/5; kappa=0; n=2')
    # Band edges, nilpotent theta, and an accidental degree eigenvalue.
    for label,cval,target in [('theta edge',sp.Rational(31,4),8),
                             ('theta accidental degree',sp.Integer(9),9)]:
        sval=sp.sqrt(cval*cval-1)
        gg=sp.Matrix([[cval,sval],[sval,cval]])
        aa=adjacency(2,[(0,1)]*3,[gg,h],[1,2],'sp')
        assert (aa*aa-target*sp.eye(4)).applyfunc(sp.simplify)==sp.zeros(4)
        rr=analyse(np.array(aa,complex),2)
        print(label,'delta=',target,'kappa=',rr['kappa'],'Q=',rr['Q'],
              'det(g-I)=',sp.factor((gg-I).det()))
        if target==8:
            assert rr['Q']==(2,2,4)
        else:
            assert (gg-I).det()!=0  # no holonomy-fixed vector
    Anil=adjacency(2,[(0,1)]*3,[-g,-g],[1,2],'sp')
    assert Anil*Anil==sp.zeros(4) and Anil.rank()==2
    print('nilpotent unbounded theta: A^2=0, rank(A)=2 EXACT')
    omega=(-1+sp.sqrt(3)*sp.I)/2
    Rom=sp.diag(omega,sp.conjugate(omega))
    Rinv=sp.diag(sp.conjugate(omega),omega)
    Azero=adjacency(2,[(0,1)]*3,[Rom,Rinv],[1,2],'sp').applyfunc(sp.simplify)
    Acomplex=adjacency(2,[(0,1)]*3,[g*Rom,Rinv],[1,2],'sp')
    assert Azero==sp.zeros(4)
    assert (Acomplex*Acomplex).applyfunc(sp.simplify)==-sp.eye(4)/2
    print('interior lower-semicontinuity counterexample: A0=0; at t=log(2), A^2=-I/2 EXACT')
    spec = graph_specs()[0]
    _, n, q, edges, chords = spec
    assert [edges[k] for k in chords] == [(1,2), (1,3), (2,3)]
    A = adjacency(n, edges, [-I,g,h], chords, 'sp')
    p = (x-1)*(x**3+x**2-5*x-sp.Rational(29,5))
    assert sp.expand(A.charpoly(x).as_expr()-p*p) == 0
    assert polyval_matrix(sp.Poly(p,x).all_coeffs(), A) == sp.zeros(8)
    print('K4 nonelementary reduced polynomial=', sp.factor(p), 'char=p^2 and p(A)=0 EXACT')
    for a,b in [(sp.Rational(-21,10),sp.Integer(-2)),
                (sp.Rational(-13,10),sp.Rational(-6,5)),
                (sp.Rational(11,5),sp.Rational(12,5))]:
        cubic = sp.cancel(p/(x-1))
        fa, fb = cubic.subs(x,a), cubic.subs(x,b)
        assert fa*fb < 0 and a*a < 8 and b*b < 8
        print('K4 exact root bracket', (a,b), 'endpoint cubic values', (fa,fb))
    print('K4 MP60 reduced roots:', sp.nroots(p, n=60, maxsteps=200))
    H = sp.diag(*([1,-1]*4))
    J = sp.BlockMatrix([[sp.zeros(8),H],[-H,sp.zeros(8)]]).as_explicit()
    M = sp.BlockMatrix([[A,-q*sp.eye(8)],[sp.eye(8),sp.zeros(8)]]).as_explicit()
    Q = sp.BlockMatrix([[H,-H*A/2],[-H*A/2,q*H]]).as_explicit()
    assert (M.conjugate().T*J*M-q*J).applyfunc(sp.simplify) == sp.zeros(16)
    assert (M.conjugate().T*Q*M-q*Q).applyfunc(sp.simplify) == sp.zeros(16)
    assert (Q-J*(M-q*M.inv())/2).applyfunc(sp.simplify) == sp.zeros(16)
    print('K4 M^dag J M=qJ; Q=J(M-qM^-1)/2; M^dag Q M=qQ EXACT')
    print('K4 numerical inertia Q=', inertia(np.array(Q,complex)))
    c,b = sp.symbols('c b',real=True)
    G = sp.Matrix([[c,b],[b,c]])
    Af = adjacency(n,edges,[-I,G,h],chords,'sp')
    # Derive the reduced polynomial using half-traces, then c^2-b^2=1.
    power, sums, coeff = sp.eye(8), [], [sp.Integer(1)]
    for k in range(1,5):
        power = power*Af
        sums.append(sp.expand(sp.trace(power)/2).subs(b**2,c**2-1).simplify())
        coeff.append(sp.simplify(-sum(coeff[k-j]*sums[j-1] for j in range(1,k+1))/k))
    pf = sp.factor(sum(coeff[k]*x**(4-k) for k in range(5)))
    print('K4 family reduced polynomial=', pf)
    print('K4 family cubic discriminant=', sp.factor(sp.discriminant(sp.cancel(pf/(x-1)),x)))
    assert sp.expand(pf-(x-1)*(x**3+x**2-5*x-(9+16*c)/5)) == 0
    cc = sp.Rational(79,54)
    gc = sp.Matrix([[cc,5*sp.sqrt(133)/54],[5*sp.sqrt(133)/54,cc]])
    Ac = adjacency(n,edges,[-I,gc,h],chords,'sp')
    rank1 = (Ac+sp.Rational(5,3)*sp.eye(8)).rank()
    rank2 = ((Ac+sp.Rational(5,3)*sp.eye(8))**2).applyfunc(sp.simplify).rank()
    assert (rank1,rank2) == (6,4)
    pc = sp.factor(pf.subs(c,cc))
    print('critical reduced polynomial=',pc,'rank(A+5I/3)=',rank1,'rank((A+5I/3)^2)=',rank2)
    print('critical t=',sp.N(sp.acosh(cc),60),'collision lambda=-5/3; other roots=1,7/3')
    print('later real band-edge parameter cosh(t)=', (31+30*sp.sqrt(2))/16,
          't=',sp.N(sp.acosh((31+30*sp.sqrt(2))/16),40))
    # A second exact rational point checks the isospectral hyperbolic family.
    Aiso = adjacency(n,edges,[-I,g,I],chords,'sp')
    piso = (x*x-1)*(x*x-5)
    assert polyval_matrix(sp.Poly(piso,x).all_coeffs(),Aiso)==sp.zeros(8)
    # Symbolic traces establish independence for all c,b with c^2-b^2=1.
    As = adjacency(n,edges,[-I,G,I],chords,'sp')
    ident = polyval_matrix(sp.Poly(piso,x).all_coeffs(),As)
    assert ident.applyfunc(lambda z: sp.rem(sp.Poly(z,b),sp.Poly(b*b-c*c+1,b)).as_expr().expand()) == sp.zeros(8)
    print('K4 isospectral family p=(x^2-1)(x^2-5), p(A)=0 for all c^2-b^2=1 EXACT')
    # Triangle with one leaf: irregular, so no claimed regular q parameter.
    le = [(0,1),(0,2),(0,3),(1,2)]
    L = adjacency(4,le,[u],[3],'sp')
    lp = x**4-4*x*x-2*x+1
    assert sp.expand(L.charpoly(x).as_expr()-lp**2)==0
    assert sp.gcd(lp,sp.diff(lp,x))==1
    assert polyval_matrix(sp.Poly(lp,x).all_coeffs(),L)==sp.zeros(8)
    print('parabolic triangle+leaf p=x^4-4x^2-2x+1, squarefree, p(A)=0 EXACT')
    print('triangle+leaf scalar roots=',sp.nroots(lp,n=30))
    print('unbounded theta band-edge cosh(t)=31/4, t=',sp.N(sp.acosh(sp.Rational(31,4)),40))
    # Ordinary simple cycles: validate the missing n-th root and parabolic blocks.
    for size in [3,4,5]:
        ce = [(i,i+1) for i in range(size-1)]+[(0,size-1)]
        Cg = adjacency(size,ce,[g],[size-1],'sp')
        pp = 2*sp.chebyshevt(size,x/2)-sp.trace(g)
        assert sp.expand(Cg.charpoly(x).as_expr()-pp**2)==0
        Cp = adjacency(size,ce,[u],[size-1],'sp')
        cp = sp.Poly(Cp.charpoly(x).as_expr(),x).sqf_part()
        defective = polyval_matrix(cp.all_coeffs(),Cp)!=sp.zeros(2*size)
        assert defective
        print(f'C{size}: hyperbolic reduced polynomial={pp}; parabolic adjacency defective EXACT')
    print('EXACT CERTIFICATES PASSED\n')


def family_scan():
    print('K4 ONE-PARAMETER FAMILY: chords -I, exp(t sigma_x), diag((-3+4i)/5,conj)')
    _,n,q,edges,chords=graph_specs()[0]
    tc=math.acosh(79/54)
    h=np.diag([(-3+4j)/5,(-3-4j)/5])
    for t in [0.,.25,math.log(2),tc-.01,tc+.01,1.2,2.]:
        g=np.array([[math.cosh(t),math.sinh(t)],[math.sinh(t),math.cosh(t)]])
        r=analyse(adjacency(n,edges,[-np.eye(2),g,h],chords),q)
        print(f't={t:.16g} cosh={math.cosh(t):.16g} real={r["real"]} inband={r["inband"]}'
              f' cond={r["cond"]:.5g} kappa={r["kappa"]} Q={r["Q"]}')
        print(' reduced eigenvalues/signatures:',[(complex(round(z.real,12),round(z.imag,12)),m,s)
                                                   for z,m,s in r['rows']])
    print(f'tcrit={tc:.16g}: EXACT defective double reduced root -5/3; see ranks above')
    print('No band-edge escape before the interior collision; at collision largest root=7/3 < 2sqrt(2).\n')


def random_scans(samples,seed):
    rng=np.random.default_rng(seed)
    print('RANDOM SCAN')
    print('samples per graph per ensemble=',samples,'seed=',seed)
    print('Reality tolerance=',REAL_TOL,'clustering=',CLUSTER_TOL,
          'relative inertia tolerance=',INERTIA_TOL,'eigenvector condition threshold=',COND_LIMIT)
    print('Semisimplicity screening also requires normalized eigenpair residual <1e-10.')
    print('At repeated real eigenvalues, signs are inertia of the whole eigenspace, never arbitrary eig vectors.')
    print('Bounded ensemble: common hyperbolic conjugate of diagonal U(1), not general SU(2).')
    print('Unbounded ensemble: KAK, compact angles uniform, radial t uniform [.05,1]; exact decimal rational Cayley parameters.')
    print('Noncommuting generators certify unboundedness because every compact subgroup of SU(1,1) is abelian.')
    print('MP80 checks use exact parameter reconstruction and n distinct real roots of the reduced polynomial.')
    print('MP80 is numerical verification, not interval arithmetic; named counterexamples above are exact.')
    summaries=[]
    for spec in graph_specs():
        name,n,q,edges,chords=spec
        print(f'GRAPH {name}: n={n}, q={q}, edges={edges}, chords={[edges[k] for k in chords]}')
        for bounded in [True,False]:
            counts=collections.Counter()
            for idx in range(samples):
                params=sample_params(rng,len(chords),bounded)
                gens=cayley_generators(params,bounded)
                if not bounded:
                    # Exact 2x2 rational-complex noncommutation test.
                    exact=cayley_generators(params[:2],False,'sp')
                    comm=(exact[0]*exact[1]-exact[1]*exact[0]).applyfunc(sp.simplify)
                    assert comm!=sp.zeros(2)
                    counts['certified_unbounded']+=1
                A=adjacency(n,edges,gens,chords)
                H=np.diag(np.tile([1.,-1.],n))
                assert la.norm(A.conj().T@H-H@A)<1e-9
                r=analyse(A,q)
                for key in ['real','inband','diagonal','ram']:
                    counts[key]+=int(r[key])
                print(f'{name} {"bounded" if bounded else "unbounded"} {idx:03d}: '
                      f'real={r["real"]} inband={r["inband"]} diag_screen={r["diagonal"]} '
                      f'ram_screen={r["ram"]} max_imag={r["imag"]:.3e} '
                      f'cond={r["cond"]:.6g} residual={r["residual"]:.2e} '
                      f'kappa={r["kappa"]} Q={r["Q"]}')
                print('  spectrum (cluster centre, multiplicity, Krein inertia):',
                      [(complex(round(z.real,11),round(z.imag,11)),m,s) for z,m,s in r['rows']])
                if not bounded and r['ram']:
                    print_generators(params,gens)
                    high_precision_check(spec,params,r)
                    counts['mp80_verified']+=1
                if bounded:
                    assert r['real'] and r['diagonal']
                expected=sum(m for z,m,s in r['rows']
                             if abs(z.imag)<REAL_TOL and abs(z.real)<=2*math.sqrt(q)+REAL_TOL)//2
                assert expected==r['kappa']
                assert r['Q']==(2*n,2*n,0)  # sampled fields avoid the exact band edges
                assert all(s==str((m//2,m//2,0)) for z,m,s in r['rows']
                           if abs(z.imag)<REAL_TOL)
            if not bounded:
                assert counts['ram']==counts['mp80_verified']
            summary=(name,'bounded' if bounded else 'unbounded',dict(counts),counts['ram']/samples)
            summaries.append(summary)
            print('SUMMARY',summary)
    print('\nALL SCAN SUMMARIES')
    for s in summaries:
        print(s)
    print('All unbounded Ramanujan successes listed above passed MP80 verification.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--samples',type=int,default=64)
    parser.add_argument('--seed',type=int,default=20261023)
    parser.add_argument('--exact-only',action='store_true')
    args=parser.parse_args()
    assert args.samples>0
    output=Path(__file__).resolve().with_name('output_krein_scan.txt')
    start=time.monotonic()
    with output.open('w',encoding='utf-8',buffering=1) as f, redirect_stdout(f):
        print('Lane K — author codex:gpt-6-astra; no RH assumption; deterministic seed.')
        print('Python',sys.version.split()[0],'numpy',np.__version__,'sympy',sp.__version__,
              'mpmath',mp.__version__,'networkx',nx.__version__)
        exact_checks()
        family_scan()
        if not args.exact_only:
            random_scans(args.samples,args.seed)
        print('ALL CHECKS PASSED; elapsed_seconds=',round(time.monotonic()-start,3))
    print('Wrote',output)


if __name__=='__main__':
    main()
