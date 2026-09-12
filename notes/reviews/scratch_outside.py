import numpy as np
rng=np.random.default_rng(5)
def hashi(Es,bar):
    N=Es[0].shape[0]; D=len(Es); T=np.zeros((N*D,N*D),complex)
    for i in range(D):
        for j in range(D):
            if j!=bar[i]: T[j*N:(j+1)*N,i*N:(i+1)*N]=Es[i]
    return T
def rhs(Es,bar,u):
    N=Es[0].shape[0]; I=np.eye(N); D=len(Es)
    pref=1.0
    for i in range(D):
        if i<bar[i]: pref*=np.linalg.det(I-u*u*Es[bar[i]]@Es[i])
    A=sum(u*Es[i]@np.linalg.inv(I-u*u*Es[bar[i]]@Es[i]) for i in range(D))
    Dm=sum(u*u*Es[bar[i]]@Es[i]@np.linalg.inv(I-u*u*Es[bar[i]]@Es[i]) for i in range(D))
    return pref*np.linalg.det(I+Dm-A)
N=4; D=4; bar=[1,0,3,2]
Es=[rng.normal(size=(N,N)) for _ in range(D)]
r=min(np.linalg.norm(Es[bar[i]]@Es[i],2)**-0.5 for i in range(D))
print(f'Neumann radius bound r = {r:.4f}')
for u in (0.5*r, 1.0, 3.7, -2.9, 5+4j, 12.0):
    ok=all(abs(np.linalg.det(np.eye(N)-u*u*Es[bar[i]]@Es[i]))>1e-8 for i in range(D))
    L=np.linalg.det(np.eye(N*D)-u*hashi(Es,bar)); R=rhs(Es,bar,u)
    print(f' u={u!s:>8} |u|/r={abs(u)/r:7.2f} hyp_ok={ok}  rel err={abs(L/R-1):.2e}')
print('deg check: det(1-uT) is a polynomial of degree <= N*D =',N*D)
import numpy.polynomial as P
us=np.linspace(-1,1,N*D+3)
vals=[np.linalg.det(np.eye(N*D)-u*hashi(Es,bar)).real for u in us]
c=np.polyfit(us,vals,N*D)
print(' leading coeff (u^{ND}) =',c[0],' = (-1)^{ND} det T =',(-1)**(N*D)*np.linalg.det(hashi(Es,bar)).real)
