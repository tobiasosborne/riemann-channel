from common import *

def run():
    c=Checks('curve_projective'); a=6-elliptic5(1)
    letters,P,pi=elliptic_tensor(5,a)
    target=[1+5**n-v for n,v in enumerate(powers(a,5),1)]
    E,N=verify_tensor(c,letters,P,target,channel_q=5)
    original=[s.diag(1,pi)/s.sqrt(2)]*2
    Eold,Nold=verify_tensor(c,original,P,target)
    for n in range(1,4): c.equal(N[n-1],elliptic5(n),f'independent point enumeration n={n}')
    Z=ring_zeta(E,s.kronecker_product(P,P))
    c.equal(Z.subs(u,1/(5*u)),Z,'genus-one functional equation')
    # Hodge duality in the original doubled basis: exchange degree 0/2 and the two degree-1 lines.
    J=s.Matrix([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
    c.check(s.simplify(J*Eold*J-5*Eold.inv())==s.zeros(4),'visible Hodge duality')
    # Perron left eigenvector of the product tensor is singular, hence no faithful TP gauge.
    c.check((Eold.T-5*s.eye(4)).nullspace()==[s.Matrix([0,0,0,1])], 'product tensor has singular left Perron matrix')
    damping=[s.diag(pi,1),s.Matrix([[0,2],[0,0]])]
    verify_tensor(c,damping,P,target,channel_q=5)
    return c.finish({**{f'A_{j}':v for j,v in enumerate(letters)},'Pi':P,'E_d':E,
                     'product_A_0':original[0],'product_A_1':original[1],'product_E_d':Eold,'Hodge_J':J,
                     'damping_A_0':damping[0],'damping_A_1':damping[1]},
                    {'N_1..6':N,'a_1..6':primes(N)}, {'Z':Z,'pi from N1':pi})
if __name__=='__main__': run()
