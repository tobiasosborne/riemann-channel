#!/usr/bin/env python3
"""Lane C: exact small-graph moments and 100-digit prism-family Schur checks.
Run from any cwd. No files outside this checks directory are written.
"""
import sympy as s
import mpmath as mp
import networkx as nx
import numpy as np
mp.mp.dps = 100


def schur(c, exact=False, tol=mp.mpf('1e-80')):
    simp = s.simplify if exact else lambda x: x
    conj = s.conjugate if exact else mp.conj
    phi, h, out = [1], c[0], []
    for k in range(len(c)-1):
        a = simp(conj(sum(phi[j]*c[j+1] for j in range(len(phi))))/h)
        out.append(a)
        r = simp(1-a*conj(a))
        if (exact and r == 0) or (not exact and abs(r) < tol):
            return out, 'terminal'
        if (exact and r < 0) or (not exact and r < 0):
            return out, 'bad'
        star = [conj(x) for x in phi[::-1]]
        phi = [simp(x-conj(a)*y) for x,y in zip([0]+phi,star+[0])]
        h = simp(h*r)
    return out, 'unfinished'


def moments(modes, q, K, exact=False):
    sq = s.sqrt(q) if exact else mp.sqrt(q)
    out = [sum(2*m for a,m in modes)] + [0]*K
    for lam,m in modes:
        a = lam/sq
        x,y = 2,a
        for k in range(1,K+1):
            out[k] += m*y
            x,y = y,a*y-x
    return [s.simplify(x) for x in out] if exact else out


def main():
    examples = [
        ('K4',2,[(-1,3)],nx.complete_graph(4)),
        ('Petersen',2,[(1,5),(-2,4)],nx.petersen_graph()),
        ('K5',3,[(-1,4)],nx.complete_graph(5)),
        ('cube',2,[(-1,3),(1,3)],nx.cubical_graph()),
        ('prism3',2,[(1,1),(0,2),(-2,2)],nx.circular_ladder_graph(3)),
    ]
    print('EXACT; alpha convention Phi_next=z Phi-conj(alpha) Phi_star')
    for name,q,modes,G in examples:
        c=moments(modes,q,16,True)
        a,status=schur(c,True)
        print(name,'q=',q,'retained degree=',c[0],'rank=',len(a),status)
        print('c[0:5]=',c[:5]); print('alpha=',a)
        # Explicit edge-space Ihara check, including k=0.
        A=s.Matrix(nx.to_numpy_array(G,dtype=int)); n=len(G); m=G.number_of_edges()
        M=A.row_join(-q*s.eye(n)).col_join(s.eye(n).row_join(s.zeros(n)))
        edges=list(G.edges())+[(v,u) for u,v in G.edges()]
        B=s.Matrix([[int(v==x and y!=u) for x,y in edges] for u,v in edges])
        for k in range(7):
            assert s.trace(B**k)-s.trace(M**k)==(m-n)*(1+(-1)**k)
    print('PASS exact Ihara correction k=0..6, five graphs')
    aa,st=schur(moments([(3,1),(-1,3)],2,8,True),True)
    print('FULL K4 (trivial roots retained) alpha=',aa,st)
    for n in range(4,10):
        a,status=schur(moments([(-1,n-1)],n-2,4,True),True)
        print('complete',n,'alpha=',a,status)
    print('PRISMS: m, retained degree, out-of-band multiplicity, first boundary/bad index, value, status')
    for m in range(3,33):
        modes=[]
        for j in range(m):
            for sign in [-1,1]:
                if (j==0 and sign==1) or (m%2==0 and j==m//2 and sign==-1):
                    continue
                modes.append((2*mp.cos(2*mp.pi*j/m)+sign,1))
        outband=sum(mult for lam,mult in modes if abs(lam)>2*mp.sqrt(2)+mp.mpf('1e-80'))
        aa,status=schur(moments(modes,2,4*m+3))
        print(m,2*len(modes),outband,len(aa)-1,mp.nstr(aa[-1],22),status)
        if m==21:
            print('prism21 alpha=',[mp.nstr(x,18) for x in aa])
    G=nx.moebius_kantor_graph()
    ev=s.Matrix(nx.to_numpy_array(G,dtype=int)).eigenvals()
    modes=[(mp.mpf(str(s.N(a,105))),int(mult)) for a,mult in ev.items() if a not in [3,-3]]
    aa,status=schur(moments(modes,2,40))
    print('Moebius-Kantor eigenvalues=',ev)
    print('Moebius-Kantor alpha=',[mp.nstr(x,22) for x in aa],status)
    aa,status=schur(moments([(1,3),(-1,3),(s.sqrt(3),4),(-s.sqrt(3),4)],2,9,True),True)
    print('EXACT Moebius-Kantor alpha=',aa,status)
    lam,q=s.symbols('lambda q',real=True,nonzero=True)
    M=s.Matrix([[lam,-q],[1,0]]); Omega=s.Matrix([[0,1],[-1,0]])
    Q=Omega*(M-q*M.inv())/2
    assert M.T*Omega*M==q*Omega
    assert s.simplify(M.T*Q*M-q*Q)==s.zeros(2)
    print('EXACT mode Q=',Q,'; Abel and energy similitude PASS')
    z,ar,ai=s.symbols('z ar ai',real=True)
    alpha=ar+s.I*ai; Az=s.Matrix([[z,-s.conjugate(alpha)],[-alpha*z,1]])
    assert s.simplify(Az.T*Omega*Az-z*(1-ar*ar-ai*ai)*Omega)==s.zeros(2)
    print('EXACT Szego alternating multiplier=z*(1-ar^2-ai^2) PASS')
    for m in [16,17]:
        G=nx.circular_ladder_graph(m)
        A=np.array(nx.to_numpy_array(G,dtype=int),dtype=object)
        n=len(G); X=2*np.eye(n,dtype=object); Y=A.copy()
        cc=[2*n-2*(1+int(m%2==0))]
        for k in range(1,15):
            tr=int(np.trace(Y))-(2**k+1)*(1+((-1)**k if m%2==0 else 0))
            cc.append(s.Rational(tr)/s.sqrt(2)**k)
            X,Y=Y,A@Y-2*X
        aa,st=schur(cc,True)
        print('EXACT prism',m,'first index',len(aa)-1,'value',aa[-1],st)
    # Same number of out-of-band modes, different first failure, a two-mode control.
    for a in [mp.mpf('2.01'),mp.mpf('2.1'),mp.mpf(3)]:
        aa,status=schur(moments([(a,1),(mp.mpf(0),10)],1,50))
        print('two-value-control a=',a,'outband=1 first=',len(aa)-1,mp.nstr(aa[-1],22),status)


if __name__=='__main__': main()
