from common import *

def run():
    c=Checks('graph_artin'); inv=[1,0,3,2]; volts=[0,0,1,1]
    H=s.Matrix(4,4,lambda i,j:int(i!=inv[j])); Hsign=s.diag(1,1,-1,-1)*H
    cover=s.zeros(8); deck=s.zeros(8)
    for g in range(2):
        for e in range(4):
            deck[(1-g)*4+e,g*4+e]=1
            for f in range(4):
                if f!=inv[e]: cover[(g^volts[f])*4+f,g*4+e]=1
    letters=[]
    for j in range(8):
        A=s.zeros(8); A[j,:]=cover[j,:]; letters.append(A)
    N=[s.trace(cover**n) for n in range(1,7)]
    E,actual=verify_tensor(c,letters,s.eye(8),N,word_n=2)
    c.check(sum((A*A.T for A in letters),s.zeros(8))==3*s.eye(8),'transposed row letters have TP normalization')
    c.check(len((E.T-3*s.eye(64)).nullspace())==1,'unique stationary graph-cover channel')
    c.check(all(abs(complex(v))<3-1e-10 for v in cover.eigenvals() if v!=3),'other graph eigenvalues strictly subleading')
    L0=1/s.factor((s.eye(4)-u*H).det()); L1=1/s.factor((s.eye(4)-u*Hsign).det())
    c.equal(1/(s.eye(8)-u*cover).det(),L0*L1,'Artin determinant factorisation')
    for n in range(1,7):
        c.equal(s.trace(Hsign**n),(N[n-1]-s.trace(deck*cover**n))/2,f'character projector n={n}')
    c.check(deck*cover==cover*deck,'free deck action commutes with transfer')
    Bp=s.Matrix([[0,-3],[1,4]]); Bm=s.Matrix([[0,-3],[1,0]])
    c.equal((s.eye(4)-u*H).det(),(1-u*u)*(s.eye(2)-u*Bp).det(),'Bass trivial factor')
    c.equal((s.eye(4)-u*Hsign).det(),(1-u*u)*(s.eye(2)-u*Bm).det(),'Bass sign factor')
    # Feed the reduced trace a=0 (sum of character voltages) into a physical genus-one tensor.
    curve,P,pi=elliptic_tensor(3,0)
    Ec,Nc=verify_tensor(c,curve,P,[1+3**n-v for n,v in enumerate(powers(0,3),1)],channel_q=3)
    Zc=ring_zeta(Ec,s.kronecker_product(P,P))
    c.equal(Zc.subs(u,1/(3*u)),Zc,'physical tensor from reduced inverse-pairing quadratic has FE')
    return c.finish({**{f'cover_A_{j}':v for j,v in enumerate(letters)},'Pi_cover':s.eye(8),
                     **{f'cover_TP_A_{j}':v.T/s.sqrt(3) for j,v in enumerate(letters)},
                     'H_base':H,'H_sign':Hsign,'H_cover':cover,'deck':deck,
                     'Bass_even':Bp,'Bass_odd':Bm,
                     **{f'curve_A_{j}':v for j,v in enumerate(curve)},'Pi_curve':P},
                    {'N_cover_1..6':N,'a_cover_1..6':primes(N),
                     'N_sign_1..6':[s.trace(Hsign**n) for n in range(1,7)],
                     'a_sign_1..6':primes([s.trace(Hsign**n) for n in range(1,7)]),
                     'N_curve_1..6':Nc,'a_curve_1..6':primes(Nc)},
                    {'Z_cover':s.factor(L0*L1),'L_trivial':L0,'L_sign':L1,'Z_curve':Zc})
if __name__=='__main__': run()
