"""Exact graph combinatorics and numerical helpers for Lane H. No external writes."""
from functools import lru_cache
from fractions import Fraction
from math import factorial
import itertools
import numpy as np
import networkx as nx
import sympy as sp

x = sp.Symbol('x')

def graph(name):
    return {'C3': nx.cycle_graph(3), 'K4': nx.complete_graph(4),
            'K33': nx.complete_bipartite_graph(3, 3), 'cube': nx.cubical_graph(),
            'Petersen': nx.petersen_graph()}[name]

def tree_edges(G):
    tree = {tuple(sorted(e)) for e in nx.bfs_edges(G, 0)}
    edges = sorted(tuple(sorted(e)) for e in G.edges())
    return sorted(tree), [e for e in edges if e not in tree]

def matching(G):
    """Return exact matching polynomial as an ascending integer coefficient tuple."""
    neighbors = {v: set(G.neighbors(v)) for v in G}
    @lru_cache(None)
    def rec(vs):
        if not vs:
            return (1,)
        v = min(vs); rest = vs - {v}
        out = [0] + list(rec(rest))
        for u in neighbors[v] & rest:
            for i, c in enumerate(rec(rest - {u})):
                out[i] -= c
        return tuple(out)
    return sp.Poly.from_list(list(rec(frozenset(G)))[::-1], x)

def cycles(G):
    """Every unoriented simple cycle once, represented by its vertex tuple."""
    out = []
    for start in sorted(G):
        def dfs(path):
            v = path[-1]
            for w in sorted(G[v]):
                if w == start and len(path) >= 3 and path[1] < path[-1]:
                    out.append(tuple(path))
                elif w > start and w not in path:
                    dfs(path + [w])
        dfs([start])
    return out

def su2_average(G):
    """Sum over vertex-disjoint cycle collections of mu(complement)^2."""
    cs = cycles(G)
    masks = [sum(1 << v for v in c) for c in cs]
    mu_cache = {}
    total = sp.Poly(0, x)
    collections = 0
    constant_covers = 0
    def rec(start, used):
        nonlocal total, collections, constant_covers
        if used not in mu_cache:
            mu_cache[used] = matching(G.subgraph([v for v in G if not used >> v & 1]))
        total += mu_cache[used] ** 2
        collections += 1
        constant_covers += used == (1 << len(G)) - 1
        for j in range(start, len(cs)):
            if not used & masks[j]:
                rec(j + 1, used | masks[j])
    rec(0, 0)
    return total, {'simple_cycles': len(cs), 'cycle_collections': collections,
                   'spanning_cycle_collections': constant_covers}

def matching_d(G, d):
    """HPS d-matching polynomial by edge multiplicities, rational arithmetic."""
    E = sorted(G.edges()); n = len(G)
    falling = [factorial(d) // factorial(d-k) for k in range(d+1)]
    degrees = [0] * n
    sums = [Fraction(0)] * (n*d//2+1)
    def rec(j, k, denom):
        if j == len(E):
            weight = 1
            for s in degrees:
                weight *= falling[s]
            sums[k] += Fraction(weight, denom)
            return
        u, v = E[j]
        for r in range(min(d-degrees[u], d-degrees[v])+1):
            degrees[u] += r; degrees[v] += r
            rec(j+1, k+r, denom * factorial(r) * falling[r])
            degrees[u] -= r; degrees[v] -= r
    rec(0, 0, 1)
    return sp.Poly(sum((-1)**k * sp.Rational(c.numerator, c.denominator) * x**(n*d-2*k)
                       for k, c in enumerate(sums)), x)

def root_report(p, q, label):
    p = sp.Poly(p, x)
    print(label, '=', p.as_expr())
    intervals = sp.polys.polytools.intervals(p, eps=sp.Rational(1, 10**20))
    nr = sum(mult for _, mult in intervals)
    inband = 0
    for (a, b), mult in intervals:
        if max(a*a, b*b) <= 4*q:
            inband += mult
    roots = sorted([complex(r) for r in sp.nroots(p, n=30, maxsteps=2000)],
                   key=lambda z: (z.real, z.imag))
    print('roots (decimal approximations):', ' '.join(f'{r.real:.12f}{r.imag:+.12f}i' for r in roots))
    print(f'exact real-root isolation: {nr}/{p.degree()} real, {inband}/{p.degree()} certified in band; band={2*np.sqrt(q):.12f}')
    print('real-rooted:', nr == p.degree(), 'all roots in band:', inband == p.degree())
    return roots

def quaternion_matrices(a):
    """a[...,4] real unit quaternions -> a[...,2,2] complex SU(2)."""
    w, xx, yy, zz = np.moveaxis(a, -1, 0)
    out = np.empty(a.shape[:-1] + (2, 2), complex)
    out[...,0,0] = w+1j*xx; out[...,0,1] = yy+1j*zz
    out[...,1,0] = -yy+1j*zz; out[...,1,1] = w-1j*xx
    return out

def spin_one(a):
    """The real SO(3) representation, quaternion axes in a conventional order."""
    w, xx, yy, zz = np.moveaxis(a, -1, 0)
    out = np.empty(a.shape[:-1] + (3,3))
    out[...,0,0]=1-2*(yy*yy+zz*zz); out[...,0,1]=2*(xx*yy-w*zz); out[...,0,2]=2*(xx*zz+w*yy)
    out[...,1,0]=2*(xx*yy+w*zz); out[...,1,1]=1-2*(xx*xx+zz*zz); out[...,1,2]=2*(yy*zz-w*xx)
    out[...,2,0]=2*(xx*zz-w*yy); out[...,2,1]=2*(yy*zz+w*xx); out[...,2,2]=1-2*(xx*xx+yy*yy)
    return out

def batch_adjacency(G, blocks):
    tree, cot = tree_edges(G)
    batch, g, d, _ = blocks.shape
    assert g == len(cot)
    A = np.zeros((batch, len(G)*d, len(G)*d), dtype=blocks.dtype)
    for u,v in tree:
        A[:,u*d:(u+1)*d,v*d:(v+1)*d]=np.eye(d)
        A[:,v*d:(v+1)*d,u*d:(u+1)*d]=np.eye(d)
    for j,(u,v) in enumerate(cot):
        A[:,u*d:(u+1)*d,v*d:(v+1)*d]=blocks[:,j]
        A[:,v*d:(v+1)*d,u*d:(u+1)*d]=blocks[:,j].conj().transpose(0,2,1)
    return A

def eigen_polynomials(ev):
    """Batched characteristic coefficients, descending powers, using long double."""
    b, n = ev.shape
    c = np.zeros((b,n+1), dtype=np.longdouble); c[:,0]=1
    for j in range(n):
        c[:,1:j+2] -= ev[:,j,None].astype(np.longdouble)*c[:,:j+1].copy()
    return c
