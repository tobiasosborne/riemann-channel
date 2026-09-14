from common import *
from cmps_half import generator
from scipy.linalg import expm

def run():
    c=Checks('cmps_fe'); P=s.diag(1,-1); G=s.kronecker_product(P,P)
    H=s.diag(0,1); R=s.Matrix([[0,s.sqrt(2)],[0,0]])
    Qn=-s.I*H-R.conjugate().T*R/2; Q=Qn+s.eye(2); T=generator(Q,[R]); Tn=generator(Qn,[R])
    c.check(Qn+Qn.conjugate().T+R.conjugate().T*R==s.zeros(2),'Lindblad completeness')
    c.check(R*R==s.zeros(2),'single fermion regularity')
    c.check(Tn.nullspace()==[s.Matrix([1,0,0,0])],'unique stationary vacuum')
    c.check(T==Tn+2*s.eye(4),'positive growth obtained by scalar Q shift')
    values=[]
    for L in range(1,7):
        v=np.trace(np.array(G,float)@expm(np.array(T,complex)*L)).real; values.append(v)
        c.close(v,1+np.exp(2*L)-2*np.exp(L)*np.cos(L),f'FE cMPS norm L={L}')
    Z=((z-1)**2+1)/(z*(z-2)); c.equal(Z.subs(z,2-z),Z,'additive functional equation')
    c.equal(abs(1+s.I-1),1,'odd frequencies are Hamiltonian input, no zero table')
    # Exact lattice sampling of amplitude damping; CP semigroup embeddability is exhibited.
    t=s.symbols('t',positive=True)
    K0=s.diag(1,s.exp((-1-s.I)*t)); K1=s.Matrix([[0,s.sqrt(1-s.exp(-2*t))],[0,0]])
    for time in [0.125,0.5,1.,2.,3.,6.]:
        k0=np.array(K0.subs(t,time),complex); k1=np.array(K1.subs(t,time),complex)
        c.close(k0.conj().T@k0+k1.conj().T@k1,np.eye(2),f'sampled CPTP Kraus completeness t={time}')
    return c.finish({'Pi':P,'H':H,'R':R,'Q_normalized':Qn,'Q_growth':Q,'T_normalized':Tn,'T_growth':T},
                    {'N_L=1..6':values,'N_exact_L=1..6':[1+s.exp(2*n)-2*s.exp(n)*s.cos(n) for n in range(1,7)]},
                    {'N':'1+exp(2L)-2exp(L)cos(L)','Z_growth':Z,
                     'Z_normalized':((z+1)**2+1)/(z*(z+2))},
                    ['Odd decay rates are 1, even nonstationary decay rate 2; normalized correlation lengths 1 and 1/2.',
                     'Continuous length has no intrinsic a_d. Sampling at L=n gives formal Mobius exponents, generally nonintegral.'])
if __name__=='__main__': run()
