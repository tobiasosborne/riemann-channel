from common import *

def run():
    c=Checks('z2_shift_cover'); X=s.Matrix([[0,1],[1,0]])
    C=s.eye(2)+2*X; letters=[]
    for g in range(2):
        for voltage in [0,1,1]:
            A=s.zeros(2); A[g^voltage,g]=1; letters.append(A)
    target=[3**n+(-1)**n for n in range(1,7)]
    E,N=verify_tensor(c,letters,s.eye(2),target,channel_q=3)
    c.check(len((E-3*s.eye(4)).nullspace())==1,'unique stationary cover channel')
    twisted=[s.trace(X*C**n) for n in range(1,7)]
    for n in range(1,7):
        c.equal((N[n-1]+twisted[n-1])/2,3**n,f'trivial Artin trace n={n}')
        c.equal((N[n-1]-twisted[n-1])/2,(-1)**n,f'sign Artin trace n={n}')
    c.check(X*C==C*X,'deck transformation commutes with path transfer')
    return c.finish({**{f'A_{j}':v for j,v in enumerate(letters)},'Pi':s.eye(2),'deck_X':X,'path_C':C,
                     'Artin_trivial_amplitude_letter':s.Matrix([[3]]),'Artin_sign_amplitude_letter':s.Matrix([[-1]])},
                    {'N_1..6':N,'a_1..6':primes(N),'deck_twisted_traces':twisted,
                     'N_sign_1..6':[(-1)**n for n in range(1,7)],'a_sign_1..6':primes([(-1)**n for n in range(1,7)])},
                    {'Z_cover':1/((1-3*u)*(1+u)),'L_trivial':1/(1-3*u),'L_sign':1/(1+u)})
if __name__=='__main__': run()
