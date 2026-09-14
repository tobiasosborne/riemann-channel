from common import *

def run():
    c=Checks('independence'); matrices={}; sequences={}; formulas={}
    I=s.eye(2); X=s.Matrix([[0,1],[1,0]]); Y=s.Matrix([[0,-s.I],[s.I,0]]); P=s.diag(1,-1)
    for name,r,x,y,fe,rh in [('TT',1,4,4,True,True),('TF',1,8,2,True,False),
                              ('FT',0,4,4,False,True),('FF',1,3,3,False,False)]:
        letters=[s.sqrt(s.Rational(16+r+x+y,4))*I,s.sqrt(s.Rational(16+r-x-y,4))*P,
                 s.sqrt(s.Rational(16-r+x-y,4))*X,s.sqrt(s.Rational(16-r-x+y,4))*Y]
        for unique in [True,False]:
            tag=name+('T' if unique else 'F')
            # A parity-preserving idle qubit gives four copies of each doubled mode.
            As=letters if unique else [s.kronecker_product(a,I) for a in letters]
            Pi=P if unique else s.kronecker_product(P,I)
            factor=1 if unique else 4
            N=[factor*(16**n+r**n-x**n-y**n) for n in range(1,7)]
            E,actual=verify_tensor(c,As,Pi,N,word_n=1,channel_q=16)
            Z=((1-x*u)*(1-y*u)/((1-16*u)*(1-r*u)))**factor
            c.check((s.cancel(Z.subs(u,1/(16*u))-Z)==0)==fe,tag+' FE classification')
            c.check((x==4 and y==4)==rh,tag+' RH classification')
            nullity=len((E-16*s.eye(E.rows)).nullspace())
            c.check((nullity==1)==unique,tag+' unique stationary state classification')
            matrices.update({f'{tag}_A_{j}':a for j,a in enumerate(As)})
            matrices[tag+'_Pi']=Pi
            sequences[tag+'_N_1..6']=N; sequences[tag+'_a_1..6']=primes(N)
            formulas[tag+'_Z']=s.factor(Z)
    periodic=[s.Matrix([[0,s.sqrt(2)],[0,0]]),s.Matrix([[0,0],[s.sqrt(2),0]])]
    Ep=transfer(periodic)
    c.check(len((Ep-2*s.eye(4)).nullspace())==1,'periodic channel still has one stationary state')
    c.check(-2 in Ep.eigenvals(),'periodic channel has another peripheral eigenvalue')
    matrices.update({'periodic_A_0':periodic[0],'periodic_A_1':periodic[1],'periodic_Pi':P})
    pn=norm_counts(periodic,P)
    sequences.update({'periodic_N_1..6':pn,'periodic_a_1..6':primes(pn)})
    formulas['periodic_Z']=ring_zeta(Ep,s.kronecker_product(P,P))
    W=s.Matrix([[2,s.Rational(5,2)],[s.Rational(5,2),2]]); v=s.Matrix([1,-1])
    c.equal((v.T*W*v)[0],-1,'off-circle reciprocal pair has a negative Weil form')
    matrices.update({'TFT_Weil_minor':W,'TFT_Weil_witness':v})
    return c.finish(matrices,sequences,formulas,
                    ['Tags give (C4, C5, C6 ergodic channel). FT has only the pole at 1/16: the even zero mode is invisible to positive powers.',
                     'Every A/4 family is CPTP; the idle qubit yields a stationary matrix algebra, not just a duplicated trace.'])
if __name__=='__main__': run()
