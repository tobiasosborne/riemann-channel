#!/usr/bin/env python3
"""Independent checks: raw determinant integration on S^3, direct Q8 sums,
Petersen constant by an edge-subset census, random-cover matching enumeration.
No imports from either reviewed lane. All polynomial arithmetic is exact.
"""
import itertools as it
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
import networkx as nx
import sympy as s
import flint

x=s.Symbol('x')

def sphere_moment(p):
    if any(a%2 for a in p): return F(0)
    num=den=1
    for a in p:
        for j in range(1,a,2): num*=j
    for j in range(sum(p)//2): den*=4+2*j
    return F(num,den)

# Each entry is a real-coordinate linear polynomial on the unit quaternion S^3.
# U=[[q0+i*q1,q2+i*q3],[-q2+i*q3,q0-i*q1]].
entry={0:[(0,1),(1,s.I)],1:[(2,1),(3,s.I)],
       2:[(2,-1),(3,s.I)],3:[(0,1),(1,-s.I)]}
reverse={0:3,1:1,2:2,3:0}

@lru_cache(None)
def edge_integral(codes):
    poly={(0,0,0,0):s.Integer(1)}
    for code in codes:
        inv,j=divmod(code,4)
        terms=entry[reverse[j] if inv else j]
        sign=-1 if inv and j in (1,2) else 1
        new=defaultdict(lambda:s.Integer(0))
        for p,v in poly.items():
            for k,c in terms:
                pp=list(p);pp[k]+=1;new[tuple(pp)]+=v*c*sign
        poly=dict(new)
    return s.expand(sum(v*s.Rational(sphere_moment(p).numerator,sphere_moment(p).denominator)
                        for p,v in poly.items()))

def integrate_leibniz(G):
    """Integrate every Leibniz term with ALL edge labels independent Haar.
    In particular no Pfaffian, matching polynomial, finite design, or cotree
    integration is used in this route.
    """
    N=2*len(G);coef=[s.Integer(0)]*(N+1);terms=0
    for perm in it.permutations(range(N)):
        factors=defaultdict(list);fixed=0;ok=True
        for a,b in enumerate(perm):
            if a==b: fixed+=1;continue
            u,i=divmod(a,2);v,j=divmod(b,2)
            if not G.has_edge(u,v): ok=False;break
            if u<v: factors[u,v].append(2*i+j)
            else: factors[v,u].append(4+2*i+j)
        if not ok:continue
        inversions=sum(perm[i]>perm[j] for i in range(N) for j in range(i+1,N))
        value=s.Integer((-1)**(inversions+N-fixed))
        for codes in factors.values():
            value*=edge_integral(tuple(sorted(codes)))
            if value==0:break
        coef[fixed]+=value;terms+=1
    p=s.Poly(sum(c*x**k for k,c in enumerate(coef)),x)
    print('S^3 raw Leibniz Haar',len(G),'vertices:',p.as_expr(),'valid terms',terms,flush=True)
    return p

def q8_average(G):
    I=s.eye(2);qi=s.diag(s.I,-s.I);qj=s.Matrix([[0,1],[-1,0]])
    group=[sgn*M for M in (I,qi,qj,qi*qj) for sgn in (1,-1)]
    # Deliberately a path-first DFS tree, unlike the lane's BFS/star tree.
    tree={tuple(sorted(e)) for e in nx.dfs_edges(G,0)}
    chords=sorted(set(tuple(sorted(e)) for e in G.edges())-tree)
    total=s.Poly(0,x)
    for gs in it.product(group,repeat=len(chords)):
        A=s.zeros(2*len(G));labels=dict(zip(chords,gs))
        for u,v in G.edges():
            U=labels.get((u,v),I)
            A[2*u:2*u+2,2*v:2*v+2]=U
            A[2*v:2*v+2,2*u:2*u+2]=U.conjugate().T
        # Direct complex charpoly, no realification or square-root extraction.
        total+=s.Poly(A.charpoly(x).as_expr(),x)
    p=total.set_domain(s.QQ).mul_ground(s.Rational(1,8**len(chords)))
    print('Q8 direct complex charpoly',len(G),'vertices:',p.as_expr(),flush=True)
    return p

def petersen_constant():
    """Enumerate 2-regular subsets via edge
    subsets, then count complementary perfect matchings by brute force.
    """
    G=nx.petersen_graph();E=list(G.edges());counts=defaultdict(int)
    @lru_cache(None)
    def pm(mask):
        if not mask:return 1
        v=(mask&-mask).bit_length()-1;rest=mask^(1<<v)
        return sum(pm(rest^(1<<u)) for u in G[v] if rest>>u&1)
    total=0;nonzero=[]
    for mask in range(1<<len(E)):
        deg=[0]*10;edges=[]
        for j,(u,v) in enumerate(E):
            if mask>>j&1:deg[u]+=1;deg[v]+=1;edges.append((u,v))
        if any(d not in (0,2) for d in deg):continue
        used=sum(1<<v for v,d in enumerate(deg) if d)
        count=pm(((1<<10)-1)^used);weight=count*count
        total+=weight;counts[sum(deg)//2]+=weight
        if weight:nonzero.append((len(edges),count))
    print('Petersen SU2 constant via 2-regular edge subsets and perfect matchings:',total)
    print('Petersen constant contributions grouped by cycle edges:',dict(sorted(counts.items())))
    assert total==57

def cover_matching_average(G,d):
    """Enumerate d-sheet covers, then their ordinary matchings by vertex deletion.
    Used only for U2 K4; independent of edge multiplicity formula (8).
    """
    tree={tuple(sorted(e)) for e in nx.dfs_edges(G,0)}
    chords=sorted(set(tuple(sorted(e)) for e in G.edges())-tree)
    perms=list(it.permutations(range(d)));sums=defaultdict(int)
    for ps in it.product(perms,repeat=len(chords)):
        labels=dict(zip(chords,ps));N=len(G)*d;nb=[0]*N
        for u,v in G.edges():
            perm=labels.get((u,v),tuple(range(d)))
            for a,b in enumerate(perm):nb[u*d+a]|=1<<(v*d+b);nb[v*d+b]|=1<<(u*d+a)
        @lru_cache(None)
        def rec(mask):
            if not mask:return (1,)
            a=(mask&-mask).bit_length()-1;rest=mask^(1<<a)
            out=[0]+list(rec(rest));options=nb[a]&rest
            while options:
                b=options&-options;options-=b
                for k,c in enumerate(rec(rest^b)):out[k]-=c
            return tuple(out)
        for k,c in enumerate(rec((1<<N)-1)):sums[k]+=c
    p=s.Poly(sum(s.Rational(c,len(perms)**len(chords))*x**k for k,c in sums.items()),x)
    print('K4 U2 from mean ordinary matching polynomial of all 2-covers:',p.as_expr())
    assert p.TC()==6
    return p

def a4_direct():
    """All 1728 A4 K4 fields, generated by group closure; no conjugacy orbits."""
    generators=[s.Matrix([[0,1,0],[0,0,1],[1,0,0]]),s.diag(-1,-1,1)]
    group={tuple(s.eye(3)):s.eye(3)};queue=[s.eye(3)]
    while queue:
        a=queue.pop()
        for b in generators:
            c=a*b;k=tuple(c)
            if k not in group:group[k]=c;queue.append(c)
    assert len(group)==12
    G=nx.complete_graph(4);tree={(0,1),(1,2),(2,3)};chords=sorted(set(G.edges())-tree)
    coeff=[0]*13
    for gs in it.product(group.values(),repeat=3):
        labels=dict(zip(chords,gs));A=s.zeros(12)
        for u,v in G.edges():
            U=labels.get((u,v),s.eye(3));A[3*u:3*u+3,3*v:3*v+3]=U;A[3*v:3*v+3,3*u:3*u+3]=U.T
        p=flint.fmpz_mat([[int(z) for z in row] for row in A.tolist()]).charpoly()
        for k,c in enumerate(p.coeffs()):coeff[k]+=int(c)
    p=s.Poly(sum(s.Rational(c,1728)*x**k for k,c in enumerate(coeff)),x)
    print('K4 A4/SO3/A5 triple by direct full enumeration:',p.as_expr())
    assert p.nth(3)==-16 and p.TC()==-s.Rational(11,9)

def design_degrees():
    axes=[]
    for j in range(4):
        for sign in [-1,1]:
            v=[F(0)]*4;v[j]=F(sign);axes.append(tuple(v))
    tetra=axes+list(it.product([F(-1,2),F(1,2)],repeat=4))
    for name,points,degree in [('Q8',axes,3),('2T',tetra,5)]:
        for powers in it.product(range(degree+1),repeat=4):
            if sum(powers)>degree:continue
            avg=sum((s.prod(q**k for q,k in zip(p,powers)) for p in points),F(0))/len(points)
            assert avg==sphere_moment(powers)
        print(name,'all quaternion-coordinate monomials of total degree <=',degree,'match Haar EXACT')

def main():
    print('Exact normalized S^3 moment: E product q_i^(2a_i) = product(2a_i-1)!!/[4*6*...*(2sum(a)+2)]')
    for G in (nx.cycle_graph(3),nx.complete_graph(4)):
        a=integrate_leibniz(G);b=q8_average(G);assert (a-b).is_zero
    print('Q8 not a fourth-degree design: E q0^4 = 1/4; Haar =',sphere_moment((4,0,0,0)))
    print('2T degree-six failure: E q0^6 =',(F(2)+16*F(1,2)**6)/24,'; Haar =',sphere_moment((6,0,0,0)))
    design_degrees()
    petersen_constant();cover_matching_average(nx.complete_graph(4),2);a4_direct()
    print('PASS independent Haar and finite-group computations')

if __name__=='__main__':main()
