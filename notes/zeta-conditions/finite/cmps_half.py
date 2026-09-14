from common import *
from scipy.linalg import expm

def generator(Q,Rs):
    return s.kronecker_product(Q,s.eye(Q.rows))+s.kronecker_product(s.eye(Q.rows),Q.conjugate())+sum(
        (s.kronecker_product(R,R.conjugate()) for R in Rs),s.zeros(Q.rows**2))

def run():
    c=Checks('cmps_half'); P=s.diag(1,-1); G=s.kronecker_product(P,P)
    Q=s.eye(2)/2; R=s.diag(1,0); T=generator(Q,[R])
    c.check(T==s.diag(2,1,1,1),'regular bosonic half-entropy transfer')
    values=[]
    for L in range(1,7):
        val=np.trace(np.array(G,float)@expm(np.array(T,float)*L)); values.append(val)
        c.close(val,np.exp(2*L)-np.exp(L),f'half-entropy norm L={L}')
    c.equal((z-1)**2/((z-2)*(z-1)),(z-1)/(z-2),'zero-mode cancellation')
    # A finite-norm CPTP alternative. It fails the mixed-species kinetic regularity relation.
    Rf=s.Matrix([[0,1],[0,0]]); Rb=P/2
    Qn=-s.Rational(1,2)*(Rf.conjugate().T*Rf+Rb.conjugate().T*Rb)
    Tn=generator(Qn,[Rf,Rb]); H=s.zeros(2)
    c.check(Qn+Qn.conjugate().T+Rf.conjugate().T*Rf+Rb.conjugate().T*Rb==s.zeros(2),'alternative is Lindblad normalized')
    c.check(Rf*Rf==s.zeros(2),'fermionic jump nilpotent')
    c.check(Rb*Rf!=Rf*Rb,'alternative fails mixed-species finite-kinetic-energy regularity')
    for L in range(1,7):
        c.close(np.trace(np.array(G,float)@expm(np.array(Tn,float)*L)),1-np.exp(-L),f'CPTP alternative norm L={L}')
    c.check(len(Tn.nullspace())==1,'CPTP alternative has unique stationary vacuum')
    return c.finish({'Pi':P,'Q_regular':Q,'R_regular':R,'T_regular':T,
                     'Q_Lindblad':Qn,'R_fermion':Rf,'R_boson':Rb,'T_Lindblad':Tn,'H_Lindblad':H},
                    {'N_L=1..6':values,'N_exact_L=1..6':[s.exp(2*n)-s.exp(n) for n in range(1,7)]},
                    {'N_regular':'exp(2L)-exp(L)','Z_regular':(z-1)/(z-2),
                     'N_Lindblad':'1-exp(-L)','Z_Lindblad':(z+1)/z,
                     'shift_to_positive_exponents':'Q_Lindblad + I gives T_Lindblad + 2I'},
                    ['No intrinsic integer-degree prime counts in continuous length.',
                     'Regular bosonic tensor is not TP gaugeable on the whole bond; its Perron left eigenmatrix has rank one.'])
if __name__=='__main__': run()
