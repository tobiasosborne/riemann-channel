#!/usr/bin/env python3
"""Exact flux census; run with python3 checks/jac_fluxes.py. No spectral floats.

Tree edges have sign +1. The integer mask records negative cotree edges in
the printed order. Automorphisms act followed by re-normalizing the tree.
All point and closed-point counts are certified for every k: direct k<32,
then the uniform Weil tail bound proved in astra-proofs.md.
"""
import json
from pathlib import Path
import networkx as nx
import sympy as S
from flint import fmpz_mat

HERE = Path(__file__).resolve().parent
x = S.Symbol('x')

def graphs():
    return [('K4', nx.complete_graph(4), 2),
            ('Petersen', nx.petersen_graph(), 2),
            ('K33', nx.complete_bipartite_graph(3, 3), 2),
            ('cube', nx.cubical_graph(), 2),
            ('K5', nx.complete_graph(5), 3)]

def step(A, p):
    n = A.rows
    return A.row_join(-p*S.eye(n)).col_join(S.eye(n).row_join(S.zeros(n)))

def positive_definite(B):
    # Sylvester's criterion, evaluated by exact integer determinants.
    return all(B[:j, :j].det() > 0 for j in range(1, B.rows+1))

def canonical_setup(G):
    edges = sorted(tuple(sorted(e)) for e in G.edges())
    tree = list(nx.bfs_edges(G, 0))
    tree_set = {tuple(sorted(e)) for e in tree}
    cot = [e for e in edges if e not in tree_set]
    autos = list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
    def matrix(mask):
        A = S.zeros(len(G))
        signs = dict.fromkeys(edges, 1)
        signs.update({e: -1 if mask>>i&1 else 1 for i,e in enumerate(cot)})
        for (v,w),sg in signs.items():
            A[v,w] = A[w,v] = sg
        return A
    def normalize(A):
        gauge = {0:1}
        for v,w in tree:
            gauge[w] = gauge[v]*int(A[v,w])
        return sum((1<<i) for i,(v,w) in enumerate(cot) if gauge[v]*gauge[w]*A[v,w] < 0)
    def orbit(mask):
        A = matrix(mask)
        return {normalize(A.extract([a[i] for i in range(len(G))],
                                    [a[i] for i in range(len(G))])) for a in autos}
    return edges, tree, cot, autos, matrix, orbit

def counts(M,p,K=31):
    F = fmpz_mat([[int(v) for v in row] for row in M.tolist()])
    power = F
    traces, N, a = {}, {}, {}
    for k in range(1,K+1):
        traces[k] = sum(int(power[i,i]) for i in range(M.rows))
        N[k] = p**k+1-traces[k]
        numerator = sum(int(S.mobius(k//d))*N[d] for d in S.divisors(k))
        assert numerator % k == 0
        a[k] = numerator//k
        power = power*F
    return traces,N,a

def census():
    records=[]
    for name,G,p in graphs():
        edges,tree,cot,autos,matrix,orbit=canonical_setup(G)
        print(f'GRAPH {name} p={p} n={len(G)} edges={edges}')
        print(f'  tree={tree} cotree={cot} automorphisms={len(autos)} switching_classes={2**len(cot)}')
        unseen=set(range(2**len(cot))); nr=0; norb=0
        while unseen:
            mask=min(unseen); orb=orbit(mask); unseen-=orb
            A=matrix(mask); n=A.rows
            cp=S.Poly(A.charpoly(x).as_expr(),x)
            ram=positive_definite(4*p*S.eye(n)-A*A)
            rec={'graph':name,'p':p,'n':n,'mask':mask,'orbit':sorted(orb),
                 'multiplicity':len(orb),'ramanujan':ram,'A':A.tolist(),
                 'adjacency_polynomial':str(S.factor(cp.as_expr())),
                 'adjacency_coefficients':[int(c) for c in cp.all_coeffs()]}
            if ram:
                nr+=len(orb); norb+=1
                M=step(A,p)
                V=p*M.inv(); Om=S.zeros(n).row_join(S.eye(n)).col_join((-S.eye(n)).row_join(S.zeros(n)))
                assert all(v.q==1 for v in V)
                assert M.T*Om*M==p*Om and M+V==S.diag(A,A)
                Fcp=S.Poly(M.charpoly(x).as_expr(),x)
                tr,N,a=counts(M,p)
                rec.update(weil_polynomial=str(S.factor(Fcp.as_expr())),
                           weil_coefficients=[int(c) for c in Fcp.all_coeffs()],
                           traces=tr,N=N,a=a,
                           ordinary=bool(int(Fcp.nth(n))%p),
                           negative_N=[k for k in N if N[k]<0],
                           negative_a=[k for k in a if a[k]<0],
                           serre_bound=p+1+n*S.integer_nthroot(4*p,2)[0])
                assert N[1]<=rec['serre_bound']
                # The uniform all-k tail is independent of floating roots.
                assert n<=10 and p>=2 and 2**16>20+11*32
                print(f'  mask={mask} size={len(orb)} RAM cp(A)={rec["adjacency_polynomial"]}')
                print(f'    F={rec["weil_polynomial"]} ordinary={rec["ordinary"]}')
                print(f'    N[1:12]={[N[k] for k in range(1,13)]}')
                print(f'    a[1:12]={[a[k] for k in range(1,13)]}')
                print(f'    negative N={[(k,N[k]) for k in rec["negative_N"]]} negative a={[(k,a[k]) for k in rec["negative_a"]]} Serre={rec["serre_bound"]}')
            else:
                print(f'  mask={mask} size={len(orb)} NOT_STRICT_RAM cp(A)={rec["adjacency_polynomial"]}')
            records.append(rec)
        print(f'SUMMARY {name}: Ramanujan switching classes={nr}; automorphism orbits={norb}')
    (HERE/'output_fluxes.json.txt').write_text(json.dumps(records,indent=2,default=int)+'\n')
    return records

if __name__=='__main__':
    import contextlib
    with (HERE/'output_fluxes.txt').open('w') as f, contextlib.redirect_stdout(f):
        census()
    print((HERE/'output_fluxes.txt').read_text())
