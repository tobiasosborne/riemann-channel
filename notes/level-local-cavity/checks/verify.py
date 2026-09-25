# Author: codex:gpt-6-astra
"""Independent algebraic/numerical diagnostics; no files are written by this script."""
import mpmath as mp
import numpy as np
import sympy as sy
mp.mp.dps = 60
F = mp.matrix([[0, 1], [1, 0]])
D = mp.diag([1, -1])
H = mp.matrix([[1, 1], [1, -1]]) / mp.sqrt(2)
I = mp.eye(2)
def err(A):
    return max(abs(x) for x in A)
def M(q, s):
    return mp.matrix([[q-1, q**s-q**(1-s)], [q**s-q**(1-s), q-1]])/(q**(2*s)-1)
def edge(t, z):
    G = ((z+1/z)*I-t*F)**-1
    Q = I-z*G
    Qi = I-G/z
    S = -(Q**-1)*Qi
    return S
s = mp.mpc('0.7', '0.3')
for q in [5, 7]:
    a = 1/mp.sqrt(q)
    ell = mp.log(q)
    z = q**(s-mp.mpf('0.5'))
    mat = M(q,s)
    Sf, Sc = edge(a,z), edge(mp.sqrt(q),z)
    inv_error = err(mat**-1+D*Sf*D)
    cusp_error = err(Sc+z*z*D*mat*D)
    det_error = abs(mp.det(mat)-(1-q**(2-2*s))/(1-q**(2*s)))
    p_error = abs(mp.det(Sf)-z*z*(z*z-a*a)/(1-a*a*z*z))
    assert max(inv_error,cusp_error,det_error,p_error) < mp.mpf('1e-55')
    print('q=',q,'z=',mp.nstr(z,16))
    print('M diagonal=',mp.nstr(mat[0,0],16),'offdiagonal=',mp.nstr(mat[0,1],16))
    print('det M=',mp.nstr(mp.det(mat),16),'raw M-vs-Sf max error=',mp.nstr(err(mat-Sf),12))
    print('corrected inverse/cusp/determinant/p residuals=',*[mp.nstr(x,4) for x in [inv_error,cusp_error,det_error,p_error]])
    def L(tau,c):
        u=mp.exp(1j*ell*tau)
        return u*(u-c)/(1-c*u)
    zeros=[]
    for k in range(-4,5):
        tau=2*mp.pi*k/ell+mp.j/2
        zeros.append(abs(L(tau,a)))
        zeros.append(abs(L(tau+mp.pi/ell,-a)))
        assert abs(tau.imag-mp.mpf('0.5')) < mp.mpf('1e-55')
    assert max(zeros)<mp.mpf('1e-55')
    minus_reduced=mp.diff(lambda tau:L(tau,a),mp.j/2)/mp.diff(lambda tau:(tau-mp.j/2)/(tau+mp.j/2),mp.j/2)
    assert abs(minus_reduced+ell/(q-1))<mp.mpf('1e-55')
    print('ell=',mp.nstr(ell,15),'comb period=',mp.nstr(2*mp.pi/ell,15),'height=0.5; max zero residual=',mp.nstr(max(zeros),4))
    print('reduced minus value at i/2=',mp.nstr(minus_reduced,15))
    for c in [a,-a]:
        v=mp.sqrt(1-c*c)
        Z=mp.matrix([[0,0],[v,c]])
        J=mp.matrix([[-c,v]])
        assert err(I-Z.T*Z-J.T*J)<mp.mpf('1e-55')
        assert abs(mp.det(Z)) < mp.mpf('1e-55') and abs(Z[0,0]+Z[1,1]-c)<mp.mpf('1e-55')
        assert abs((1-c*c)*mp.fsum(c**(2*n) for n in range(100))-1)<mp.mpf('1e-55')
    # Arbitrarily many independent delay states; integrate their Fourier-basis Gram.
    gram=np.array([[complex(mp.quad(lambda x:mp.exp(2j*mp.pi*(j-k)*x/ell)/ell,[0,ell])) for j in range(8)] for k in range(8)])
    assert np.max(np.abs(gram-np.eye(8)))<1e-14
    # Bound equation for the genuine cusp toy: symmetric/antisymmetric states.
    for sign in [1,-1]:
        theta=sign*a; x=mp.matrix([1,sign]); lam=theta+1/theta
        assert err((lam*I-mp.sqrt(q)*F-theta*I)*x)<mp.mpf('1e-55')
    # Phase-derivative Fourier coefficients for the unreduced pair.
    tau=mp.mpf('0.23')
    phase=sum(mp.diff(lambda v:mp.log(L(v,c)),tau)/mp.j for c in [a,-a])
    series=4*ell*(1+mp.fsum(q**(-mp.mpf(m))*mp.cos(2*m*ell*tau) for m in range(1,100)))
    assert abs(phase-series)<mp.mpf('1e-55')

def kron(A,B):
    return mp.matrix([[A[i//B.rows,j//B.cols]*B[i%B.rows,j%B.cols] for j in range(A.cols*B.cols)] for i in range(A.rows*B.rows)])
def incoming(q,s):
    return mp.matrix([[1,q**s],[q**s,1]])
B35=kron(incoming(5,s),incoming(7,s))
B35opp=kron(incoming(5,1-s),incoming(7,1-s))
local35=kron(M(5,s),M(7,s))
res=err(local35-B35opp*(B35**-1))
HH=kron(H,H)
diagonal=HH.T*local35*HH
resoff=max(abs(diagonal[i,j]) for i in range(4) for j in range(4) if i!=j)
resdet=abs(mp.det(local35)-mp.det(M(5,s))**2*mp.det(M(7,s))**2)
for index,(e5,e7) in enumerate([(1,1),(1,-1),(-1,1),(-1,-1)]):
    expected=((1+e5*5**(1-s))/(1+e5*5**s))*((1+e7*7**(1-s))/(1+e7*7**s))
    assert abs(diagonal[index,index]-expected)<mp.mpf('1e-55')
    def local_product(tau):
        result=1
        for prime,sign in [(5,e5),(7,e7)]:
            u=mp.exp(1j*mp.log(prime)*tau)
            c=-sign/mp.sqrt(prime)
            result*=u*(u-c)/(1-c*u)
        return result
    minus_count=int(e5==-1)+int(e7==-1)
    for order in range(minus_count):
        assert abs(mp.diff(local_product,mp.j/2,order))<mp.mpf('1e-55')
    assert abs(mp.diff(local_product,mp.j/2,minus_count))>mp.mpf('1e-5')
print('N=35 raw local vanishing orders at i/2: 0,1,1,2; reduced orders: 0,0,0,1.')
assert max(res,resoff,resdet)<mp.mpf('1e-55')
print('N=35 oldform tensor / Walsh / determinant residuals=',*[mp.nstr(x,4) for x in [res,resoff,resdet]])
# Exact symbolic graph formula and defect identity.
z,t=sy.symbols('z t'); Is=sy.eye(2); Fs=sy.Matrix([[0,1],[1,0]])
G=((z+1/z)*Is-t*Fs).inv()
S=-(Is-z*G).inv()*(Is-G/z)
closed=-z*(Is-t*z*Fs).inv()*(z*Is-t*Fs)
assert sy.simplify(S-closed)==sy.zeros(2)
assert sy.factor(((1+z*z)*Is-z*t*Fs-Is).det())==z*z*(z-t)*(z+t)
print('Symbolic Q and p checks: PASS. All numerical assertions: PASS.')
