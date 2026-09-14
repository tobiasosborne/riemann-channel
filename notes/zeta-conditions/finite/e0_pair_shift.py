from common import *

def run():
    c=Checks('e0_pair_shift'); P=s.diag(1,-1)
    letters=[s.diag(1,int(a==b)) for a,b in itertools.product(range(2),repeat=2)]
    E,N=verify_tensor(c,letters,P,[4**n-2**n for n in range(1,7)])
    Z=ring_zeta(E,s.kronecker_product(P,P))
    c.equal(Z,(1-2*u)/(1-4*u),'net cancellation gives E0')
    for n,a in enumerate(primes(N),1): c.check(a.is_Integer and a>=0,f'bosonic primes degree {n}')
    # Positive integral norms need not be a genuine gas.
    bad=[s.diag(1,-1)]; badN=norm_counts(bad,P)
    c.equal(primes(badN)[1],-2,'positive integral norm has a_2=-2')
    inv=[s.diag(1,2),s.diag(1,s.Rational(1,2))]
    Einv=transfer(inv)
    c.check(inv[0]*inv[1]==s.eye(2),'counterexample letters are inverse paired')
    # Pair of even eigenvalues fixes q=17/2; odd 5/2 is not self reciprocal.
    c.check(s.Rational(5,2)**2 != s.Rational(17,2),'inverse pairing does not give raw-transfer FE')
    fake=[s.Rational(4**n-2**n,2) for n in range(1,7)]
    c.equal(primes(fake)[1],s.Rational(5,2),'fake swap L has nonintegral degree-two exponent')
    weighted=[s.diag(s.Rational(1,2),s.Rational(1,2)),s.diag(s.Rational(1,2),0)]
    WN=norm_counts(weighted,P)
    c.equal(primes(WN)[1],-s.Rational(1,32),'equal weighted sub-sums do not ensure a genuine gas')
    return c.finish({**{f'A_{a}{b}':letters[2*a+b] for a,b in itertools.product(range(2),repeat=2)},
                     'Pi':P,'E_d':E,'counterexample_C2_A':bad[0],
                     'inverse_B':inv[0],'inverse_Binv':inv[1],'inverse_E_d':Einv,
                     'weighted_subset_A_0':weighted[0],'weighted_subset_A_1':weighted[1]},
                    {'N_1..6':N,'a_1..6':primes(N),'C2_counterexample_N':badN,'C2_counterexample_a':primes(badN),
                     'fake_swap_N':fake,'fake_swap_a':primes(fake),'weighted_subset_N':WN,'weighted_subset_a':primes(WN),
                     'inverse_counterexample_N':norm_counts(inv,P),'inverse_counterexample_a':primes(norm_counts(inv,P))},
                    {'Z':Z,'C2_counterexample_Z':ring_zeta(transfer(bad),s.kronecker_product(P,P)),
                     'weighted_subset_Z':ring_zeta(transfer(weighted),s.kronecker_product(P,P)),
                     'inverse_counterexample_Z':ring_zeta(Einv,s.kronecker_product(P,P))})
if __name__=='__main__': run()
