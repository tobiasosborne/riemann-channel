#!/usr/bin/env python3
"""Audit the net divisor, which the supplied 79 checks do not reduce.

Loads only selected function definitions from the supplied construction;
independently decomposes both sector spectra and subtracts multiplicities.
Eigenvalue matching uses tolerance 1e-7; this is numerical evidence.
"""
import ast
import pathlib
import sys
import itertools
import numpy as np

ROOT=pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'scripts'))
from weil_lps import lps_quaternions, split_matrices, quat_to_gl2
names={'gl2_elements','mul','inv','det','pgl_canon','legendre','principal_series'}
tree=ast.parse((ROOT/'scripts/graded_ramanujan.py').read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names],type_ignores=[]),'<construction functions>','exec'))

checks=0
def check(ok,msg):
    global checks
    assert bool(ok),msg
    checks+=1
    print(f'PASS {checks:02d}: {msg}')

def clusters(se,so):
    groups=[]
    for v,k in sorted([(x,0) for x in se]+[(x,1) for x in so]):
        if not groups or abs(v-groups[-1][0])>1e-7:
            groups.append([float(v),0,0])
        groups[-1][k+1]+=1
    return groups

for p,q in [(5,13),(13,5)]:
    gen=next(g for g in range(2,p) if len({pow(g,k,p) for k in range(1,p)})==p-1)
    chi=np.zeros(p,complex)
    for k in range(p-1): chi[pow(gen,k,p)]=(1j)**k
    rep=principal_series(p,chi)
    group=sorted({pgl_canon(g,p) for g in gl2_elements(p)})
    g0=[g for g in group if legendre(det(g,p),p)==1]
    n=p+1
    # The G0 commutant consists of two scalar blocks. A deterministic generic seed.
    rng=np.random.default_rng(16)
    seed=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));seed=seed+seed.conj().T
    C=sum(rep(g)@seed@rep(g).conj().T for g in g0)/len(g0)
    C=C-np.trace(C)/n*np.eye(n);C=(C+C.conj().T)/2
    eig,V=np.linalg.eigh(C);V=V[:,np.argsort(-eig)]
    P=np.diag(np.r_[np.ones(n//2),-np.ones(n//2)])
    check(np.allclose(np.abs(eig),np.abs(eig[0])),f'p={p}: two equal-dimensional Clifford blocks')
    A,B=split_matrices(p)
    gs=[tuple(map(int,quat_to_gl2(a,p,A,B).ravel())) for a in lps_quaternions(q)]
    us=[V.conj().T@rep(g)@V for g in gs]
    check(all(np.allclose(P@a@P,-a) for a in us),f'p={p}: all LPS letters odd')
    E=sum(np.kron(a,a.conj()) for a in us)
    parity=np.diag(np.kron(P,P))
    even=np.where(parity>0)[0];odd=np.where(parity<0)[0]
    se=np.linalg.eigvalsh(E[np.ix_(even,even)]);so=np.linalg.eigvalsh(E[np.ix_(odd,odd)])
    check(np.max(np.abs(so))<2*np.sqrt(q)+1e-10,f'p={p}: odd band')
    check(np.max(np.abs(se[np.abs(se)<q+.9]))<2*np.sqrt(q)+1e-10,f'p={p}: even band')
    rows=clusters(se,so)
    print(f'\n(p,q)=({p},{q}), adjacency value : even, odd, nu=even-odd')
    for val,a,b in rows: print(f'  {val: .10f} : {a:2d}, {b:2d}, {a-b:+3d}')
    # Counts below are reduced polynomial degrees in u, not raw odd dimensions.
    zero_degree=2*sum(max(b-a,0) for val,a,b in rows)
    pole_degree=2*sum(max(a-b,0) for val,a,b in rows)
    print(f'REDUCED degrees: numerator {zero_degree}, denominator {pole_degree}; nontrivial denominator degree {pole_degree-4}')
    check(pole_degree>=4 and zero_degree==pole_degree,f'p={p}: balanced total degree and four structural poles')
    check(zero_degree != 2*len(odd),f'p={p}: printed raw-odd genus is not the reduced numerator degree')
    # Character sums for arbitrary even/odd group elements (ordinary and twisted).
    for g in [g0[5],next(g for g in group if legendre(det(g,p),p)==-1)]:
        U=V.conj().T@rep(g)@V
        U2=np.kron(U,U.conj())
        check(abs(np.trace(np.kron(P,P)@U2)-abs(np.trace(P@U))**2)<1e-9,
              f'p={p}: twisted character identity, parity {legendre(det(g,p),p)}')
    print()
print(f'{checks}/{checks} checks passed')
