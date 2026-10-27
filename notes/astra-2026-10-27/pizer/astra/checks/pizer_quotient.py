"""Actual isogeny duality, then independent quaternion ideal computation.

Run with python3. All arithmetic is exact; displayed field embeddings may vary.
"""
import os, sys
sys.dont_write_bytecode=True
PARI_PY='/tmp/claude-1000/-home-tobias-Projects-riemann-channel/dcae8e10-414e-4cb4-8b95-d35e159cfb50/scratchpad/venv-astra/bin/python'
try:
    import cypari2
except ImportError:
    os.execv(PARI_PY,[PARI_PY,'-u',__file__,*sys.argv[1:]])
from pizer_graph import pari, supersingular, brandt, bass_check
import sympy as s
import itertools, math
from sympy.matrices.normalforms import hermite_normal_form

def sm(A):
    return s.Matrix([[s.Rational(str(A[i,j])) for j in range(A.ncols())] for i in range(A.nrows())])

def pm(A):
    return pari.matrix(A.rows,A.cols,[pari(str(a)) for a in A])

def exact_vectors(G,bound):
    """One representative per +/- pair with norm exactly bound, exhaustive.

    LLL only changes an integral basis; exact inverse-Gram coordinate bounds
    and an integer box search certify completeness independently of qfminim.
    """
    den=s.ilcm(*[a.q for a in G])
    U=sm(pari.qflllgram(pm(G*den)))
    assert abs(U.det())==1
    R=U.T*G*U
    den=s.ilcm(*[a.q for a in R],s.Rational(bound).q)
    Q=[[int(a*den) for a in R.row(i)] for i in range(4)]
    target=int(bound*den)
    inv=R.inv()
    bounds=[math.isqrt(int(s.floor(bound*inv[i,i]))) for i in range(4)]
    vs=[]
    for v in itertools.product(*[range(-b,b+1) for b in bounds]):
        if not any(v) or next(a for a in v if a)!=abs(next(a for a in v if a)): continue
        val=sum(Q[i][i]*v[i]**2 for i in range(4))+2*sum(Q[i][j]*v[i]*v[j] for i in range(4) for j in range(i+1,4))
        if val==target: vs.append(U*s.Matrix(v))
    return vs

def quaternion_main():
    al=pari.alginit(pari.nfinit('y'),[-2,-37])
    base=sm(pari.algbasis(al))
    G0=base.T*s.diag(1,2,37,74)*base
    mult=[sm(M) for M in pari.algmultable(al)]
    bi=base.inv()
    qi,qj,qk=[bi[:,a] for a in [1,2,3]]
    product=sum((qi[a]*mult[a] for a in range(4)),s.zeros(4))*qj
    assert product==-qk  # PARI's natural cyclic basis is (1,i,j,ji).
    assert sum((qi[a]*mult[a] for a in range(4)),s.zeros(4))*qi==-2*bi[:,0]
    assert sum((qj[a]*mult[a] for a in range(4)),s.zeros(4))*qj==-37*bi[:,0]
    for a in range(4):
        for b in range(4):
            v=s.eye(4)[:,a]+s.eye(4)[:,b]
            assert pari.algnorm(al,pari.Col([int(c) for c in v]))==(v.T*G0*v)[0]
    print('\nQUATERNION B=(-2,-37); maximal-order basis in PARI (1,i,j,ji)=',base.tolist())
    print('norm Gram=',G0.tolist(),'reduced trace discriminant=',-(2*G0).det())
    print('finite Hasse data=',pari.alghassef(al),'infinite=',pari.alghassei(al))
    assert -(2*G0).det()==-37**2
    assert G0.det()>0
    right=[s.Matrix.hstack(*[M[:,j] for M in mult]) for j in range(4)]
    def lat(I): return pari.alglathnf(al,pm(I))
    def transporter(J,I):
        L=pari.alglatlefttransporter(al,lat(J),lat(I))
        return sm(L[0])*s.Rational(str(L[1]))
    def normI(I):
        a=s.sqrt(abs(I.det())); assert a.is_Rational
        return a
    def hom_vectors(J,I,degree):
        L=transporter(J,I)
        vs=exact_vectors(L.T*G0*L,degree*normI(I)/normI(J))
        return [L*v for v in vs]
    def neighbours2(I):
        actions=[I.inv()*R*I for R in right]
        assert all(a.q==1 for R in actions for a in R)
        spaces=set()
        for a,b in itertools.combinations(range(1,16),2):
            U=frozenset([0,a,b,a^b])
            spaces.add(U)
        answer=[]
        for U in sorted(spaces,key=lambda z:sorted(z)):
            def vec(a): return s.Matrix([(a>>i)&1 for i in range(4)])
            good=True
            for a in U:
                for R in actions:
                    v=R*vec(a)
                    aa=sum((int(v[i])%2)<<i for i in range(4))
                    if aa not in U: good=False; break
                if not good: break
            if good:
                cols=[vec(a) for a in sorted(U) if a]
                K=hermite_normal_form(s.Matrix.hstack(2*s.eye(4),*cols))
                assert K.det()==4
                answer.append(I*K)
        assert len(answer)==3
        return answer
    ideals=[s.eye(4)]
    for J in neighbours2(ideals[0]):
        if not any(hom_vectors(K,J,1) for K in ideals): ideals.append(J)
    assert len(ideals)==3
    for i,I in enumerate(ideals):
        print('ideal',i,'basis=',I.tolist(),'norm=',normI(I))
        OL=transporter(I,I)
        print('left order',i,'basis=',OL.tolist(),'norm Gram=',(OL.T*G0*OL).tolist())
        assert len(exact_vectors(OL.T*G0*OL,1))==1
    B2=s.zeros(3)
    for i,I in enumerate(ideals):
        for J in neighbours2(I):
            matches=[j for j,K in enumerate(ideals) if hom_vectors(K,J,1)]
            assert len(matches)==1
            B2[i,matches[0]]+=1
    print('direct ideal 2-neighbour matrix=',B2.tolist())
    _,js,_=supersingular(37)
    modB=brandt(37,2,js)
    perms=[perm for perm in itertools.permutations(range(3)) if B2==modB.extract(perm,perm)]
    assert perms
    perm=perms[0]
    print('ideal classes -> modular-polynomial j indices=',perm,'j=',[str(js[i]) for i in perm])
    for ell in [2,3,5,7]:
        B=s.Matrix(3,3,lambda i,j:len(hom_vectors(ideals[j],ideals[i],ell)))
        assert B==brandt(37,ell,js).extract(perm,perm)
        print('THETA BRANDT ell=',ell,'B=',B.tolist(),'MODULAR POLYNOMIAL MATCH PASS')
        half=[]
        for I in ideals:
            vs=hom_vectors(I,I,ell)
            half.append(sum(pari.algtrace(al,pari.Col([pari(str(a)) for a in v]))==0 for v in vs))
        _,natural=natural_halfloops(37,ell)
        assert half==[natural[i] for i in perm]
        print('trace-zero norm ell elements modulo +/- =',half,'VELU DUALITY MATCH PASS')
    print('ALL QUATERNION IDEAL / EXACT NORM-ENUMERATION CHECKS PASS')

def natural_halfloops(p,ell,verbose=False):
    t,js,w=supersingular(p)
    assert all(a==1 for a in w)
    result=[]; rows=[]
    for i,j in enumerate(js):
        c=j/(1728-j)
        E0=pari.ellinit([3*c,2*c])
        trace=p*p+1-int(pari.ellcard(E0))
        assert abs(trace)==2*p
        scalar=trace//2
        k=1
        while pow(scalar,k,ell)!=1: k+=1
        z=pari.ffgen(p**(2*k),'z')
        emb=pari.ffembed(t,z)
        jj=[pari.ffmap(emb,a) for a in js]
        a=pari.ffmap(emb,3*c); b=pari.ffmap(emb,2*c)
        E=pari.ellinit([a,b])
        xs=list(pari.polrootsmod(pari.elldivpol(E,ell)))
        assert len(xs)==(3 if ell==2 else (ell*ell-1)//2)
        pts=[]
        for xx in xs:
            yy=pari.polrootsmod(pari('y')**2-(xx**3+a*xx+b))[0]
            P=pari([xx,yy]); assert len(pari.ellmul(E,P,ell))==1
            pts.append(P)
        subgroups={}
        for P in pts:
            xxset=frozenset(str(pari.ellmul(E,P,m)[0]) for m in range(1,ell))
            if xxset not in subgroups: subgroups[xxset]=P
        assert len(subgroups)==ell+1
        row=[0]*len(js); half=0; loopdata=[]
        for kernel,P in subgroups.items():
            image,iso=pari.ellisogeny(E,P)
            Ep=pari.ellinit(image)
            jp=Ep.j()
            target=next(ii for ii,j0 in enumerate(jj) if jp==j0)
            row[target]+=1
            if target!=i: continue
            # x-coordinate multiplier of an isomorphism E -> E/kernel.
            d=(image[4]/b)/(image[3]/a)
            assert image[3]==a*d*d and image[4]==b*d*d*d
            Q=next(Q for Q in pts if str(Q[0]) not in kernel)
            R=pari.ellisogenyapply(iso,Q)
            assert len(R)==2
            dual=frozenset(str(pari.ellmul(Ep,R,m)[0]/d) for m in range(1,ell))
            fixed=(dual==kernel)
            half+=fixed
            loopdata.append(fixed)
        result.append(half); rows.append(row)
        if verbose: print('duality p ell vertex=',p,ell,i,'j=',j,'extension degree=',2*k,'loop fixed flags=',loopdata)
    B=brandt(p,ell,js)
    assert B==s.Matrix(rows)
    return B,result

def duality_main():
    for p in [13,37,73,109]:
        for ell in [2,3,5,7]:
            B,half=natural_halfloops(p,ell,True)
            m,h,detH=bass_check(B,ell,half)
            print('ACTUAL DUALITY p=',p,'ell=',ell,'B=',B.tolist(),'halfloops=',half,'paired edges=',m,'fixed darts=',h)
            print('ACTUAL DUALITY BASS PASS; det(I-uH)=',detH)
            if p==37:
                Z=s.zeros(B.rows)
                doubled=s.BlockMatrix([[Z,B],[B,Z]]).as_explicit()
                mp,hp,dp=bass_check(doubled,ell,[0]*doubled.rows)
                assert hp==0 and mp==B.rows*(ell+1)
                print('BIPARTITE DOUBLE ordinary Bass: vertices=',doubled.rows,'edges=',mp,'PASS; determinant=',dp)
    print('ALL NATURAL DUALITY / MODULAR POLYNOMIAL / BASS CHECKS PASS')

if __name__=='__main__':
    if '--quaternion-only' not in sys.argv: duality_main()
    quaternion_main()
