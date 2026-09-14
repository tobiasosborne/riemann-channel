from common import *

def count(n):
    F=Field(2,2*n)
    return 1+sum(2 if F.trace(F.power(x,3))==0 else 0 for x in range(F.order))

def run():
    c=Checks('curve_supersingular'); a=5-count(1)
    letters,P,pi=elliptic_tensor(4,a)
    Ntarget=[1+4**n-v for n,v in enumerate(powers(a,4),1)]
    E,N=verify_tensor(c,letters,P,Ntarget,channel_q=4)
    original=[s.diag(1,pi)]
    verify_tensor(c,original,P,Ntarget)
    for n in range(1,7): c.equal(N[n-1],count(n),f'y^2+y=x^3 over F_2^{2*n}')
    Z=ring_zeta(E,s.kronecker_product(P,P))
    c.equal(Z.subs(u,1/(4*u)),Z,'functional equation')
    c.equal(pi,-2,'double real root derived from finite field count')
    return c.finish({**{f'A_{j}':v for j,v in enumerate(letters)},'Pi':P,'E_d':E,'product_A':original[0]},
                    {'N_1..6':N,'a_1..6':primes(N)}, {'Z':Z,'pi from N1':pi})
if __name__=='__main__': run()
