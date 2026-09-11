import numpy as np
rng=np.random.default_rng(1)
def haar(n):
    z=(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/np.sqrt(2); q,r=np.linalg.qr(z); return q*(np.diag(r)/abs(np.diag(r)))
def sup(U):            # superoperator rho -> U rho U^dag, column-stacking
    return np.kron(U.conj(),U)
def run(n,k,label):
    Us=[haar(n) for _ in range(k)]; Us=Us+[u.conj().T for u in Us]   # closed under inverse
    D=len(Us); inv=lambda i:(i+k)%D
    Phi=sum(sup(u) for u in Us)/D                      # unital channel, D Kraus unitaries
    # Hashimoto superoperator on M_n (x) C^D
    N=n*n; T=np.zeros((N*D,N*D),complex)
    for i in range(D):
        for j in range(D):
            if j!=inv(i): T[j*N:(j+1)*N, i*N:(i+1)*N]=sup(Us[i])
    q=D-1; I=np.eye(N)
    for u in (0.13,0.29+0.11j,-0.4):
        lhs=np.linalg.det(np.eye(N*D)-u*T)
        rhs=(1-u*u)**(N*(D-2)/2)*np.linalg.det(I-u*D*Phi+q*u*u*I)
        print(label,'u=',u,' |lhs/rhs-1| =',abs(lhs/rhs-1))
    ev=np.sort(np.linalg.eigvalsh((D*Phi+ (D*Phi).conj().T)/2))  # Phi HS-self-adjoint for symmetric set
    print(label,'eigs of D*Phi (top 4):',np.round(ev[-4:],3),' Ramanujan bound 2sqrt(q)=',round(2*np.sqrt(q),3))
run(3,2,'n=3,D=4')
run(4,3,'n=4,D=6')
