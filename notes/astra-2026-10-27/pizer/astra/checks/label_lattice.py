"""Integral augmentation labels, symplectic reduction, and elliptic groups."""
import os,sys
sys.dont_write_bytecode=True
P='/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra/bin/python'
try: import cypari2
except ImportError: os.execv(P,[P,'-u',__file__,*sys.argv[1:]])
from pizer_graph import pari, brandt, supersingular, x, u
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

def smith(A):
    D=smith_normal_form(A,domain=s.ZZ)
    return [abs(int(D[i,i])) for i in range(D.rows) if abs(D[i,i])!=1]

def labels(B,ell):
    n=B.rows; g=n-1
    K=s.Matrix.vstack(s.eye(g),-s.ones(1,g))
    C=K.T*K
    A=(B*K)[:g,:]
    assert B*K==K*A
    M=s.BlockMatrix([[A,-ell*s.eye(g)],[s.eye(g),s.zeros(g)]]).as_explicit()
    Om=s.BlockMatrix([[s.zeros(g),C],[-C,s.zeros(g)]]).as_explicit()
    assert M.T*Om*M==ell*Om
    assert all(v.q==1 for v in ell*M.inv())
    Q=Om*(M-ell*M.inv())/2
    assert Q==Q.T
    assert all(Q[:i,:i].det()>0 for i in range(1,2*g+1))
    full=s.BlockMatrix([[B,-ell*s.eye(n)],[s.eye(n),s.zeros(n)]]).as_explicit()
    # e=(1,1) primitive invariant line. Standard symplectic basis of e^perp/Ze:
    # v_i=(e_i,e_n), w_i=(0,e_i-e_n), i<n.
    V=s.zeros(2*n,2*g)
    for i in range(g):
        V[i,i]=1; V[2*n-1,i]=1
        V[n+i,g+i]=1; V[2*n-1,g+i]=-1
    def reduce(v):
        assert sum(v[:n])==sum(v[n:])
        return s.Matrix([v[i]-v[n-1] for i in range(g)]+[v[n+i]-v[n-1] for i in range(g)])
    R=s.Matrix.hstack(*[reduce(full*V[:,i]) for i in range(2*g)])
    Ostd=s.BlockMatrix([[s.zeros(g),s.eye(g)],[-s.eye(g),s.zeros(g)]]).as_explicit()
    assert R.T*Ostd*R==ell*Ostd
    embedding=s.Matrix.hstack(*[reduce(s.BlockDiagMatrix(K,K).as_explicit()[:,i]) for i in range(2*g)])
    assert abs(embedding.det())==n
    assert R*embedding==embedding*M
    assert embedding.T*Ostd*embedding==Om
    return A,M,Om,Q,R,embedding

def main():
    Eeqs=[[0,0,1,-1,0],[0,1,1,-23,-50]]
    Es=[pari.ellinit(a) for a in Eeqs]
    for label,E,eq in zip(['37a1','37b1'],Es,Eeqs):
        print('ELLIPTIC',label,'equation=',eq,'discriminant=',E.disc(),'conductor=',pari.ellglobalred(E)[0], 'a_ell=',[int(pari.ellap(E,l)) for l in [2,3,5,7]])
        try:
            Ec=pari('ellinit("'+label+'")')
            print('Cremona data available; model first five=',list(Ec[:5]))
        except Exception as exc: print('Cremona table absent; equation verified directly:',str(exc).splitlines()[0])
    for p in [37,73,109]:
        _,js,_=supersingular(p)
        for ell in [2,3,5,7]:
            B=brandt(p,ell,js)
            A,M,Om,Q,R,embedding=labels(B,ell)
            cp=M.charpoly(x).as_expr()
            print('\np=',p,'ell=',ell,'A_augmentation=',A.tolist())
            print('F characteristic polynomial=',s.factor(cp),'Omega determinant=',Om.det(),'Omega SNF=',smith(Om),'trivial-plus-cusp index=',B.rows**2)
            print('symplectic reduction index=',abs(embedding.det()),'charpoly match=',R.charpoly(x).as_expr()==cp)
            if p==37:
                print('M_augmentation=',M.tolist(),'M_reduction=',R.tolist(),'embedding=',embedding.tolist())
            for k in [1,2,3]:
                S0=smith(s.eye(M.rows)-M**k)
                Sr=smith(s.eye(R.rows)-R**k)
                count=(s.eye(M.rows)-M**k).det()
                resultant=s.resultant(cp,1-x**k,x)
                assert count==resultant==s.prod(S0)==s.prod(Sr)
                print('k=',k,'augmentation SNF=',S0,'reduction SNF=',Sr,'#J via P=',count)
                if p==37:
                    t=pari.ffgen(ell**k,'t')
                    groups=[]
                    for eq in Eeqs:
                        E=pari.ellinit([a*t**0 for a in eq])
                        groups.append([int(a) for a in pari.ellgroup(E)])
                    factors=[a for G in groups for a in G]
                    combined=smith(s.diag(*factors))
                    assert s.prod(combined)==count
                    print('elliptic groups=',groups,'product invariant factors=',combined,'augmentation equal=',combined==S0,'reduction equal=',combined==Sr)
    print('\nALL LABEL / SMITH / POINT-ORDER CHECKS PASS')

if __name__=='__main__': main()
