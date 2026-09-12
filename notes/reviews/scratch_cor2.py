import numpy as np, itertools
rng=np.random.default_rng(2)
def ad(A): return np.kron(A.conj(),A)
def hashi(Es,bar):
    N=Es[0].shape[0]; D=len(Es); T=np.zeros((N*D,N*D),complex)
    for i in range(D):
        for j in range(D):
            if j!=bar[i]: T[j*N:(j+1)*N,i*N:(i+1)*N]=Es[i]
    return T
n,m=3,2
As=[rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)) for _ in range(m)]
As=As+[A.conj().T for A in As]; D=2*m; bar=[(i+m)%D for i in range(D)]
As=[A/3 for A in As]
Es=[ad(A) for A in As]; T=hashi(Es,bar)
print('--- Cor 2 trace formula, exactly as stated ---')
for L in range(1,6):
    lhs=np.trace(np.linalg.matrix_power(T,L))
    # stated: sum over (i_1..i_L), i_{k+1} != bar(i_k) cyclically, of |Tr(A_{i_L}...A_{i_1})|^2
    tot=0.0
    for w in itertools.product(range(D),repeat=L):
        if all(w[(k+1)%L]!=bar[w[k]] for k in range(L)):
            P=np.eye(n)
            for i in w: P=As[i]@P          # A_{i_L} ... A_{i_1}
            tot+=abs(np.trace(P))**2
    # reversed product order, same condition (to see whether the condition/order pairing matters)
    tot_rev=0.0
    for w in itertools.product(range(D),repeat=L):
        if all(w[(k+1)%L]!=bar[w[k]] for k in range(L)):
            P=np.eye(n)
            for i in w: P=P@As[i]          # A_{i_1} ... A_{i_L}
            tot_rev+=abs(np.trace(P))**2
    print(f' L={L}: Tr T^L={lhs.real:.10f} (imag {lhs.imag:.1e})  stated={tot:.10f} err={abs(lhs-tot):.1e}   revprod={tot_rev:.10f}')
print()
print('--- nonnegativity of Tr T^L and of zeta Taylor coefficients ---')
print(' Tr T^L for L=1..8:', [round(np.trace(np.linalg.matrix_power(T,L)).real,6) for L in range(1,9)])
print()
print('--- Euler product vs zeta, |u| small ---')
u=0.05
zeta=1/np.linalg.det(np.eye(T.shape[0])-u*T)
# primitive cyclic non-backtracking classes up to length Lmax
Lmax=6; prod=1.0
seen=set()
for L in range(1,Lmax+1):
    for w in itertools.product(range(D),repeat=L):
        if not all(w[(k+1)%L]!=bar[w[k]] for k in range(L)): continue
        rots={tuple(w[k:]+w[:k]) for k in range(L)}
        if len(rots)<L: continue           # not primitive
        key=min(rots)
        if key in seen: continue
        seen.add(key)
        P=np.eye(n)
        for i in w: P=As[i]@P
        prod*= 1/np.linalg.det(np.eye(n*n)-u**L*ad(P))
print(f' zeta={zeta.real:.12f}  Euler(trunc L<={Lmax})={prod.real:.12f}  ratio={ (prod/zeta).real:.10f}')
print()
print('--- norm claim ||Ad(A^dag A)|| = ||A||^4 ---')
for A in As[:2]:
    print(f'  ||Ad(A^dag A)||={np.linalg.norm(ad(A.conj().T@A),2):.10f}   ||A||^4={np.linalg.norm(A,2)**4:.10f}')
    print(f'  eigs Ad(A^dag A) real&>=0: {np.allclose(np.linalg.eigvals(ad(A.conj().T@A)).imag,0)}, min={np.linalg.eigvals(ad(A.conj().T@A)).real.min():.2e}')
