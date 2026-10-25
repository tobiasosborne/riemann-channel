#!/usr/bin/env python3
"""Independent reciprocal-series counts, complete K5 orbits and resultants.
Run from the repository root; imports no lane J code.
"""
import itertools, json, random
from pathlib import Path
import sympy as s
import networkx as nx

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[2]/'astra-2026-10-23'/'jacobian'/'checks'
x,u=s.symbols('x u')

def counts(c,p,K=40):
    # -u P'(u)/P(u) = sum power_sum(k) u^k, via series division.
    inv=[1]
    for k in range(1,K+1):
        inv.append(-sum(c[j]*inv[k-j] for j in range(1,min(k,len(c)-1)+1)))
    N=[0]+[p**k+1+sum(j*c[j]*inv[k-j] for j in range(1,min(k,len(c)-1)+1)) for k in range(1,K+1)]
    a=[0]
    for k in range(1,K+1):
        num=N[k]-sum(d*a[d] for d in range(1,k) if k%d==0)
        assert num%k==0
        a.append(num//k)
        assert a[k]==sum(int(s.mobius(k//d))*N[d] for d in s.divisors(k))//k
    return N,a

def cycles(A,l):
    total=negative=0
    for vs in itertools.combinations(range(A.rows),l):
        for tail in itertools.permutations(vs[1:]):
            q=(vs[0],)+tail
            if q[1]>q[-1]: continue
            sign=s.prod(A[q[j],q[(j+1)%l]] for j in range(l))
            if sign:
                total+=1; negative+=int(bool(sign<0))
    return total,negative,total-2*negative

def main():
    data=json.loads((SOURCE/'output_fluxes.json.txt').read_text())
    result=[]
    for r in data:
        if not r['ramanujan']:continue
        A=s.Matrix(r['A']);p=r['p'];n=A.rows;I=s.eye(n);O=s.zeros(n)
        F=A.row_join(-p*I).col_join(I.row_join(O))
        V=O.row_join(p*I).col_join((-I).row_join(A))
        Om=O.row_join(I).col_join((-I).row_join(O))
        assert F*V==p*s.eye(2*n) and F+V==s.diag(A,A)
        assert F.T*Om*F==p*Om
        # Integral vector-polynomial presentation in coefficient basis (u,v).
        G=O.row_join(-p*I).col_join(I.row_join(A))
        H=I.row_join(A).col_join(O.row_join(I))
        assert H*G==F*H and H.det()==1
        # Weil polynomial from real characteristic polynomial substitution.
        h=A.charpoly(x).as_expr()
        W=s.Poly(s.cancel(x**n*h.subs(x,x+p/x)).expand(),x)
        c=list(map(int,W.all_coeffs()))
        assert c==r['weil_coefficients']
        N,a=counts(c,p)
        assert all(N[k]==r['N'][str(k)] and a[k]==r['a'][str(k)] for k in range(1,32))
        middle=c[n];ordinary=middle%p!=0
        assert ordinary==r['ordinary']
        minor=[int((4*p*I-A*A)[:j,:j].det()) for j in range(1,n+1)]
        assert min(minor)>0
        cy4=cycles(A,4);cy5=cycles(A,5)
        assert a[4]==(p**4-p**2)//4-2*cy4[2]
        if r['graph']=='Petersen':assert a[5]==6-2*cy5[2]
        print(f'{r["graph"]}:{r["mask"]} middle={middle} residue={middle%p} ordinary={ordinary}')
        print(' N1..12='+str(N[1:13]));print(' a1..12='+str(a[1:13]))
        print(' negative_N='+str([(k,N[k]) for k in range(1,41) if N[k]<0])+' negative_a='+str([(k,a[k]) for k in range(1,41) if a[k]<0]))
        print(' cycle4(total,negative,sum)='+str(cy4)+' cycle5='+str(cy5))
        result.append(dict(graph=r['graph'],mask=r['mask'],N=N[1:],a=a[1:],middle=middle,ordinary=ordinary,minors=minor))
    # K5 switching classes independently classified by all triangle signs.
    ed=list(itertools.combinations(range(5),2));cot=[e for e in ed if e[0]!=0]
    triples=list(itertools.combinations(range(5),3))
    perms=list(itertools.permutations(range(5)))
    orbits={}
    for mask in range(64):
        sg={e:(-1 if e in cot and mask>>cot.index(e)&1 else 1) for e in ed}
        def triangle(a,b,c):return sg[tuple(sorted((a,b)))]*sg[tuple(sorted((a,c)))]*sg[tuple(sorted((b,c)))]
        key=min(tuple(triangle(*(q[i] for i in t)) for t in triples) for q in perms)
        orbits.setdefault(key,[]).append(mask)
    strict=[]
    for group in orbits.values():
        m=min(group);A=s.zeros(5)
        for a,b in ed:A[a,b]=A[b,a]=-1 if (a,b) in cot and m>>cot.index((a,b))&1 else 1
        if all((12*s.eye(5)-A*A)[:i,:i].det()>0 for i in range(1,6)):strict.append((m,len(group)))
    strict.sort();assert strict==[(1,10),(3,15),(11,10),(12,15),(13,12)]
    print('K5 independent triangle-sign orbits: '+str(strict)+'; total switching classes=62')
    # Random connected signed graphs, including sparse graphs with repeated factors.
    rng=random.Random(20261025);tally=dict(graphs=0,reducible=0,factorizations=0,pairwise=0,pairwise_one=0,partition_one=0)
    random_rows=[]
    for trial in range(20):
        n=4+trial%9
        G=nx.Graph();G.add_nodes_from(range(n))
        # Random recursive spanning tree, then independent extra edges.
        for i in range(1,n):G.add_edge(i,rng.randrange(i))
        for a,b in itertools.combinations(range(n),2):
            if rng.random()<(0 if trial%4==0 else .14):G.add_edge(a,b)
        A=s.zeros(n)
        for a,b in sorted(G.edges()):A[a,b]=A[b,a]=rng.choice((-1,1))
        h=A.charpoly(x).as_expr();fs=s.factor_list(h)[1]
        prs=[int(s.resultant(f,g,x)) for (f,e),(g,d) in itertools.combinations(fs,2)]
        tally['pairwise']+=len(prs);tally['pairwise_one']+=sum(abs(v)==1 for v in prs)
        partitions=[]
        for exp in itertools.product(*(range(e+1) for f,e in fs)):
            f=s.prod(g**a for (g,e),a in zip(fs,exp));g=s.cancel(h/f)
            if f==1 or g==1:continue
            if s.Poly(f,x).all_coeffs()>s.Poly(g,x).all_coeffs():continue
            val=int(s.resultant(f,g,x));partitions.append((str(f),str(g),val))
            assert abs(val)!=1
        tally['graphs']+=1;tally['reducible']+=int(bool(sum(e for f,e in fs)>1));tally['factorizations']+=len(partitions)
        print(f'RANDOM {trial+1} n={n} edges={len(G.edges())} charpoly={s.factor(h)} pairwise={prs} factorizations={len(partitions)} resultant_one=0')
        random_rows.append(dict(A=A.tolist(),factors=[(str(f),e) for f,e in fs],pairwise=prs,partitions=partitions))
    print('RESULTANT TALLY '+str(tally))
    print('TAIL k=32: 2^16=65536 > 20+11*32=372; ratio increases for k>=32')
    (HERE/'output_independent_arithmetic.json.txt').write_text(json.dumps(dict(orbits=result,K5_orbits=strict,random=random_rows,tally=tally),indent=2,default=int)+'\n')

if __name__=='__main__':main()
