#!/usr/bin/env python3
"""Exact Ihara prime-cycle / flux computations; no spectral assumptions.

Run: python3 notes/astra-2026-10-23/qrh-transpose/checks/qrh_graph_family.py
Output is also written to output_graph.txt beside this file.
Oriented prime cycles are identified under rotation, NOT reversal.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, gcd
from pathlib import Path
import sys
import numpy as np
import networkx as nx
import sympy as sp

MAXD = 16


class Tee:
    def __init__(self, file): self.file = file
    def write(self, s): sys.__stdout__.write(s); self.file.write(s)
    def flush(self):
        sys.__stdout__.flush()
        if not self.file.closed: self.file.flush()


def setup(G):
    edges = sorted(tuple(sorted(e)) for e in G.edges())
    tree = set(tuple(sorted(e)) for e in nx.bfs_edges(G, 0))
    chords = [e for e in edges if e not in tree]
    directed = sorted([(a,b) for a,b in edges]+[(b,a) for a,b in edges])
    index = {e:i for i,e in enumerate(directed)}
    nxt = [[index[(b,c)] for c in sorted(G[b]) if c != a] for a,b in directed]
    delta = []
    for a,b in directed:
        x = [0]*len(chords)
        if tuple(sorted((a,b))) in chords:
            x[chords.index(tuple(sorted((a,b))))] = 1 if a < b else -1
        delta.append(tuple(x))
    return edges, chords, directed, nxt, delta


def enumerate_primes(G):
    edges,chords,directed,nxt,delta = setup(G)
    counts = [Counter() for _ in range(MAXD+1)]
    g = len(chords)
    for first,(origin,_) in enumerate(directed):
        path = [first]
        hom = list(delta[first])
        def visit(last):
            d = len(path)
            if d >= 3 and first in nxt[last]:
                # Minimal first oriented edge plus least rotation among its repeats.
                rotations_ok = all(path <= path[j:]+path[:j]
                                   for j in range(1,d) if path[j] == first)
                primitive = all(path != path[:k]*(d//k)
                                for k in range(1,d//2+1) if d % k == 0)
                if rotations_ok and primitive:
                    counts[d][tuple(hom)] += 1
            if d == MAXD: return
            for e in nxt[last]:
                if e < first: continue
                path.append(e)
                for j in range(g): hom[j] += delta[e][j]
                visit(e)
                for j in range(g): hom[j] -= delta[e][j]
                path.pop()
        visit(first)
    # Independent prime-cycle count via powers of the integer Hashimoto matrix.
    B = np.zeros((len(directed),len(directed)), dtype=np.int64)
    for e,ns in enumerate(nxt): B[e,ns] = 1
    power = np.eye(len(directed), dtype=np.int64)
    prime = [sum(c.values()) for c in counts]
    for k in range(1,MAXD+1):
        power = power @ B
        assert int(np.trace(power)) == sum(d*prime[d] for d in range(1,k+1) if k % d == 0)
    return counts, B, chords


def group_ring_products(counts, N, g):
    classes = np.array(list(product(range(N), repeat=g)), dtype=np.int64)
    radix = N**np.arange(g-1,-1,-1,dtype=np.int64)
    M = N**g
    signed = np.zeros((MAXD+1,M), dtype=np.int64)
    unsigned = np.zeros_like(signed)
    signed[0,0] = unsigned[0,0] = 1
    for length in range(1,MAXD+1):
        grouped = Counter()
        for hom,m in counts[length].items(): grouped[tuple(x % N for x in hom)] += m
        for hom,m in grouped.items():
            old_s,old_u = signed.copy(),unsigned.copy()
            for j in range(1,min(m,MAXD//length)+1):
                shift = (classes-j*np.array(hom)) % N @ radix
                weight = comb(m,j)
                signed[j*length:] += ((-1)**j*weight)*old_s[:-j*length,shift]
                unsigned[j*length:] += weight*old_u[:-j*length,shift]
    assert np.all(unsigned >= 0)
    return classes,signed,unsigned


def exact_char_norm(row, classes, s, N):
    sums = [int(row[(classes @ s) % N == k].sum()) for k in range(N)]
    if N == 2: return (sums[0]-sums[1])**2
    if N == 3:
        a,b = sums[0]-sums[2],sums[1]-sums[2]
        return a*a-a*b+b*b
    if N == 6:
        a = sums[0]-sums[2]-sums[3]+sums[5]
        b = sums[1]+sums[2]-sums[4]-sums[5]
        return a*a+a*b+b*b
    raise ValueError(N)


def main():
    print('EXACT: integers / cyclotomic integer pairs; prime cycles through D=16.')
    print('No RH or zeros used. N=2,3: every flux; K4 also N=6.')
    print('Each flux line gives order and fractions at D=12,14,16, plus D=15 if nonempty.')
    z = sp.Symbol('z')
    for name,G in [('K4',nx.complete_graph(4)),('Petersen',nx.petersen_graph()),('cube',nx.cubical_graph())]:
        counts,B,chords = enumerate_primes(G)
        m,n = G.number_of_edges(),G.number_of_nodes()
        g = m-n+1
        print(f'\nGRAPH {name}: vertices={n} edges={m} q=2 g={g} chords={chords}')
        print('prime_counts_D0_to_16=',[sum(c.values()) for c in counts])
        A = sp.Matrix(nx.to_numpy_array(G,dtype=int))
        Q = sp.Poly((1-z*z)**(m-n)*(sp.eye(n)-z*A+2*z*z*sp.eye(n)).det(),z)
        # Unsigned squarefree Euler product equals Q(z^2)/Q(z).
        inv = [int(Q.nth(d)) for d in range(2*m+1)]
        sf = [0]*(MAXD+1)
        sf[0] = 1
        for d in range(1,MAXD+1):
            sf[d] = (inv[d//2] if d%2 == 0 and d//2<len(inv) else 0)-sum(inv[j]*sf[d-j] for j in range(1,min(d,len(inv)-1)+1))
        print('det(1-zB)=',Q.as_expr())
        print('squarefree_counts_D0_to_16=',sf)
        if name == 'K4':
            assert Q.eval(sp.Rational(1,2)) == 0
            assert np.all(B @ np.ones(2*m,dtype=np.int64) == 2)
            print('LITTLEWOOD COUNTEREXAMPLE: K4 theta=0; Q(1/2)=0; B*1=2*1; deg(Q)=',Q.degree(),
                  '; Mobius coefficients vanish for D>12.')
            print('K4 exact determinant factorization=',sp.factor(Q.as_expr()))
        for N in ([2,3,6] if name == 'K4' else [2,3]):
            classes,signed,unsigned = group_ring_products(counts,N,g)
            assert [int(x) for x in unsigned.sum(axis=1)] == sf
            assert [int(x) for x in signed.sum(axis=1)] == [int(Q.nth(d)) for d in range(MAXD+1)]
            if MAXD>2*m: assert not np.any(signed[2*m+1:])
            print(f'FAMILY N={N}, size={N**g}')
            for D in [3,4,6,8,10,12,13,14,15,16]:
                mean = N**g*sum(int(v)**2 for v in signed[D])
                diagonal = N**g*sf[D]
                pair_unsigned = sum(int(v)**2 for v in unsigned[D])
                # Fourier-side evaluation independently uses cyclotomic norms.
                fourier = sum(exact_char_norm(signed[D],classes,s,N) for s in classes)
                assert mean == fourier
                print(f'D={D} S={mean} diagonal={diagonal} offdiag={mean-diagonal} unsigned_homologous_pairs={pair_unsigned}')
            for s in classes:
                order = N//gcd(N,*[int(x) for x in s])
                mask = (classes @ s) % N == 0
                frac = {D:str(Fraction(int(unsigned[D,mask].sum()),sf[D])) if sf[D] else 'undefined(no ideals)'
                        for D in [12,14,15,16]}
                print(f'flux={tuple(int(x) for x in s)} order={order} fractions={frac}')
            if N == 2 and name == 'K4':
                parity = np.array([nx.shortest_path_length(nx.bfs_tree(G,0).to_undirected(),a,b)+1 for a,b in chords]) % 2
                print('PARITY flux=',tuple(int(x) for x in parity),'D13 fraction=',Fraction(int(unsigned[13,(classes@parity)%2==0].sum()),sf[13]),
                      'D14 fraction=',Fraction(int(unsigned[14,(classes@parity)%2==0].sum()),sf[14]))
        if name == 'K4':
            # Find a torus ribbon structure with a triangular face of class e_3.
            _,_,directed,_,delta = setup(G)
            delta_by_edge = dict(zip(directed,delta))
            ribbon = None
            for bits in product([0,1],repeat=4):
                rot = {}
                for v,b in enumerate(bits):
                    a=sorted(G[v]); rot[v]=a if not b else [a[0],a[2],a[1]]
                unused=set(directed); faces=[]
                while unused:
                    e=min(unused); face=[]
                    while e not in face:
                        face.append(e); unused.remove(e)
                        a,b=e; e=(b,rot[b][(rot[b].index(a)+1)%3])
                    faces.append(face)
                homs=[tuple(sum(delta_by_edge[e][j] for e in face) for j in range(3)) for face in faces]
                if len(faces)==2 and sorted(map(len,faces))==[3,9] and any(h in [(0,0,1),(0,0,-1)] for h in homs):
                    ribbon=(rot,faces,homs); break
            assert ribbon is not None
            print('TORUS RIBBON K4 rotation=',ribbon[0],'face_lengths=',list(map(len,ribbon[1])),'face_homology=',ribbon[2])
            projected=[Counter() for _ in counts]
            for d,c in enumerate(counts):
                for v,num in c.items(): projected[d][v[:2]]+=num
            cc,_,uu=group_ring_products(projected,2*MAXD+1,2)
            zz=np.where(cc>MAXD,cc-(2*MAXD+1),cc)
            for D in [8,12,16]:
                zero=int(uu[D,0]); total=sf[D]
                moments=[[Fraction(sum(int(uu[D,k])*int(zz[k,i])*int(zz[k,j]) for k in range(len(cc))),total*D)
                          for j in range(2)] for i in range(2)]
                print(f'SURFACE_CLT D={D} projected_zero={zero} total={total} D*P_zero={Fraction(D*zero,total)} covariance_over_D={moments}')
    # Closed torus H1 with its unimodular intersection form, independent of graph embedding.
    print('\nSURFACE finite test: J=[[0,1],[-1,0]] on H1(torus;Z/N).')
    for N in [2,3,6,7,12]:
        C = list(product(range(N),repeat=2))
        image = {((6*a)%N,(6*b)%N) for a,b in C}
        kernel = [a for a in C if (6*a[0])%N == (6*a[1])%N == 0]
        assert len(kernel) == gcd(6,N)**2
        print(f'N={N} row_count={N*N} distinct_fluxes_after_times6={len(image)} trivial_rows={len(kernel)}')
    print('PASS: Euler products, trace/prime counts, signed orthogonality, exact cyclotomic Fourier norms, surface kernel.')


if __name__ == '__main__':
    with Path(__file__).with_name('output_graph.txt').open('w') as out:
        sys.stdout = Tee(out)
        main()
        sys.stdout = sys.__stdout__
