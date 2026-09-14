from common import *

def kl(n):
    F=Field(2,2*n)
    return sum((-1)**F.trace(F.add(x,F.power(x,F.order-2))) for x in range(1,F.order))

def run():
    c=Checks('kloosterman'); sums=[kl(n) for n in range(1,7)]; a=-sums[0]
    letters,P,pi=elliptic_tensor(4,a,True)
    E,N=verify_tensor(c,letters,P,[4**n+sums[n-1] for n in range(1,7)],channel_q=4)
    for n,v in enumerate(powers(a,4),1): c.equal(-v,sums[n-1],f'direct extension Kloosterman sum n={n}')
    # Independent equation count of y^2+xy=x^3+1 for small extensions.
    for n in range(1,4):
        F=Field(2,2*n); total=1  # unique solution at x=0
        for x in range(1,F.order):
            rhs=F.mul(F.add(F.power(x,3),1),F.power(F.power(x,2),F.order-2))
            total+=2 if F.trace(rhs)==0 else 0
        c.equal(total,N[n-1],f'affine elliptic count n={n}')
    Z=ring_zeta(E,s.kronecker_product(P,P))
    return c.finish({**{f'A_{j}':v for j,v in enumerate(letters)},'Pi':P,'E_d':E,
                     'amplitude_F':s.Matrix([[0,-4],[1,a]]),'Pi_amplitude':-s.eye(2)},
                    {'raw_Kl_1..6':sums,'N_1..6':N,'a_1..6':primes(N),
                     'L_log_N_1..6':sums,'L_formal_a_1..6':primes(sums)},
                    {'L_Kl':1-a*u+4*u*u,'Z_affine':Z,'pi from Kl1':pi})
if __name__=='__main__': run()
