import numpy as np, itertools
rng=np.random.default_rng(11)
N,D=3,6; inv=[1,0,3,2,5,4]
E=[rng.normal(size=(N,N))/3+1j*rng.normal(size=(N,N))/3 for _ in range(D)]
def T_note(u):
    T=np.zeros((N*D,N*D),complex)
    for i in range(D):
        for j in range(D):
            if j!=inv[i]: T[j*N:(j+1)*N,i*N:(i+1)*N]=E[i]
    return np.eye(N*D)-u*T
# WF edge matrix: M_{e,e'} = u_e if e'->e allowed, i.e. e' != ebar (bouquet)
def M_wf(u):
    M=np.zeros((N*D,N*D),complex)
    for e in range(D):
        for ep in range(D):
            if ep!=inv[e]: M[e*N:(e+1)*N,ep*N:(ep+1)*N]=u*E[e]
    return np.eye(N*D)-M
for u in (0.11,0.2+0.07j):
    I=np.eye(N)
    Ahat=sum(np.linalg.inv(I-u*u*E[e]@E[inv[e]])@(u*E[e]) for e in range(D))
    Dhat=sum(np.linalg.inv(I-u*u*E[e]@E[inv[e]])@(u*u*E[e]@E[inv[e]]) for e in range(D))
    pairs={tuple(sorted((i,inv[i]))) for i in range(D)}
    prod=np.prod([np.linalg.det(I-u*u*E[a]@E[b]) for a,b in pairs])
    wf=np.linalg.det(I+Dhat-Ahat)*prod
    # note's A,D
    An=u*sum(E[i]@np.linalg.inv(I-u*u*E[inv[i]]@E[i]) for i in range(D))
    Dn=u*u*sum(E[inv[i]]@E[i]@np.linalg.inv(I-u*u*E[inv[i]]@E[i]) for i in range(D))
    note=np.linalg.det(I+Dn-An)*prod
    lhs=np.linalg.det(T_note(u)); wfdet=np.linalg.det(M_wf(u))
    print(f"u={u}: det(1-uT)={lhs:.6g}  detWFedge={wfdet:.6g}  WFcor={wf:.6g}  note={note:.6g}")
    print("   rel: WFedge",abs(wfdet/lhs-1)," WFcor",abs(wf/lhs-1)," note",abs(note/lhs-1),
          " Ahat-vs-A",np.abs(Ahat-An).max()," Dhat-vs-D",np.abs(Dhat-Dn).max())
# MO bouquet specialisation with unitaries
n=3; Dg=6
Us=[ (lambda z:(lambda qr:qr[0]*(np.diag(qr[1])/abs(np.diag(qr[1]))))(np.linalg.qr(z)))((rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/np.sqrt(2)) for _ in range(Dg//2)]
X=[np.kron(U.conj(),U) for U in Us]           # Ad(U) column stacking
Xall=X+[np.linalg.inv(x) for x in X]
Eu=Xall; invu=[(i+Dg//2)%Dg for i in range(Dg)]
def Tg(u):
    T=np.zeros((n*n*Dg,)*2,complex)
    for i in range(Dg):
        for j in range(Dg):
            if j!=invu[i]: T[j*n*n:(j+1)*n*n,i*n*n:(i+1)*n*n]=Eu[i]
    return np.eye(n*n*Dg)-u*T
for q in (0.13,0.21+0.09j):
    A_X=sum(Xall)          # = sum_e (X_e + X_e^{-1}) for the D/2 loops
    mo=(1-q*q)**(n*n*(Dg-2)/2)*np.linalg.det(np.eye(n*n)-q*A_X+(Dg-1)*q*q*np.eye(n*n))
    print(f"MO bouquet q={q}: rel err {abs(np.linalg.det(Tg(q))/mo-1):.2e}")
