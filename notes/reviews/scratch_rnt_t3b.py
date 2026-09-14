# Reviewer claude:opus-5. Clean re-run of the random test in C3 (tolerance-robust).
import numpy as np
rng = np.random.default_rng(11)
def blocks(as_,Bs):
    m=as_[0].shape[0]; k=Bs[0].shape[0]
    Sp=sum(np.kron(a,a.conj()) for a in as_); Sm=sum(np.kron(B,B.conj()) for B in Bs)
    M=sum(np.kron(a,B.conj()) for a,B in zip(as_,Bs))
    As=[np.block([[a,np.zeros((m,k))],[np.zeros((k,m)),B]]) for a,B in zip(as_,Bs)]
    E=sum(np.kron(A,A.conj()) for A in As)
    P=np.array([1.]*m+[-1.]*k); G=np.kron(P,P)
    return Sp,Sm,M,E,G
w31=w32=w34=wodd=0; m31=m32=m34=modd=0.0
for t in range(400):
    m=int(rng.integers(1,4)); k=int(rng.integers(1,4)); S=int(rng.integers(1,5))
    as_=[rng.normal(size=(m,m))+1j*rng.normal(size=(m,m)) for _ in range(S)]
    Bs =[rng.normal(size=(k,k))+1j*rng.normal(size=(k,k)) for _ in range(S)]
    Sp,Sm,M,E,G=blocks(as_,Bs); od=np.where(G==-1)[0]
    mu=np.linalg.eigvals(E[np.ix_(od,od)])
    tp=sum(np.linalg.norm(a,'fro')**2 for a in as_); tm=sum(np.linalg.norm(B,'fro')**2 for B in Bs)
    s=float(np.sum(np.abs(mu)**2)); h=2*np.linalg.norm(M,'fro')**2
    r=lambda x: x/max(1.0,abs(x))
    m31=max(m31,(s-h)/max(1,abs(h)));  w31+= (s>h*(1+1e-9))
    m32=max(m32,(h/2-np.linalg.norm(Sp,'fro')*np.linalg.norm(Sm,'fro'))/max(1,h))
    w32+= (h/2>np.linalg.norm(Sp,'fro')*np.linalg.norm(Sm,'fro')*(1+1e-9))
    mhs=max(0.0,(h-2*tp*tm)/max(1,h)); w34+=(h>2*tp*tm*(1+1e-9))
    for n in range(1,7):
        lhs=abs(np.trace(np.linalg.matrix_power(M,n)))**2
        rhs=np.trace(np.linalg.matrix_power(Sp,n)).real*np.trace(np.linalg.matrix_power(Sm,n)).real
        if lhs>rhs*(1+1e-7)+1e-7: m34=max(m34,(lhs-rhs)/max(1,abs(rhs)))
    # odd block similar to M (+) conj M : compare char polys
    pa=np.poly(E[np.ix_(od,od)]); pb=np.poly(np.block([[M,np.zeros_like(M)],[np.zeros_like(M),M.conj()]]))
    d=np.max(np.abs(pa-pb))/max(1,np.max(np.abs(pa))); modd=max(modd,d); wodd+=(d>1e-6)
print("violations: (3.1) eig<=2||M||^2:",w31," 2||M||^2<=2 tau+tau-:",w34," (3.2):",w32," (3.4) worst rel excess:",m34)
print("odd block char-poly mismatch max rel:",modd," count>1e-6:",wodd)
