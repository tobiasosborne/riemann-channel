from common import *

def run():
    c=Checks('curve_affine'); a=6-elliptic5(1)
    letters,P,pi=elliptic_tensor(5,a,True)
    target=[5**n-v for n,v in enumerate(powers(a,5),1)]
    E,N=verify_tensor(c,letters,P,target,channel_q=5)
    for n in range(1,4): c.equal(N[n-1],elliptic5(n)-1,f'independent F_5^{n} point enumeration minus infinity')
    for n,v in enumerate(primes(N),1): c.check(v.is_Integer and v>=0,f'prime count degree {n}')
    Z=ring_zeta(E,s.kronecker_product(P,P))
    c.equal(Z,(1-a*u+5*u*u)/(1-5*u),'affine zeta')
    c.equal(pi*s.conjugate(pi),5,'odd block divided by sqrt(5) unitary')
    return c.finish({**{f'A_{j}':v for j,v in enumerate(letters)},'Pi':P,'E_d':E},
                    {'N_1..6':N,'a_1..6':primes(N)}, {'Z':Z,'pi from N1':pi})
if __name__=='__main__': run()
