from common import *

def run():
    c=Checks('gauss'); G=sum((1 if x==1 else -1)*s.exp(2*s.pi*s.I*x/3) for x in [1,2])
    G=s.expand_complex(G); alpha=-G
    N=[]
    for n in range(1,7):
        F=Field(3,n); value=0j
        for x in range(1,F.order):
            eta=1 if F.power(x,(F.order-1)//2)==1 else -1
            value+=eta*np.exp(2j*np.pi*F.trace(x)/3)
        exact=-alpha**n; N.append(s.expand(exact))
        c.close(value,complex(exact),'Hasse-Davenport sign from direct extension sum n='+str(n))
        additive=sum(np.exp(2j*np.pi*F.trace(F.power(x,2))/3) for x in range(F.order))
        c.close(additive,value,'affine-line quadratic additive Gauss sum n='+str(n))
    c.equal(s.expand_complex(G*s.conjugate(G)),3,'Gauss norm squared')
    # Open-chain MPS over the affine line: the three physical letters are x=0,1,2.
    A0=s.Matrix([[1]]); A1=s.Matrix([[(-1+s.I*s.sqrt(3))/2]]); A2=A1
    c.equal((A0+A1+A2)[0],G,'three explicit affine letters sum to the base Gauss sum')
    return c.finish({'open_A_0':A0,'open_A_1':A1,'open_A_2':A2,'open_boundary':s.Matrix([[1]]),
                     'amplitude_F':s.Matrix([[alpha]]),'Pi_amplitude':s.Matrix([[-1]])},
                    {'log_N_1..6':N,'formal_a_1..6':primes(N)},
                    {'G_standard_sum':G,'L_standard':1+G*u,'L_if_G_means_Frobenius_alpha':1-alpha*u,
                     'physical_open_norm_degree_n':'3**n'})
if __name__=='__main__': run()
