"""REFUTE-stance independent re-derivation of T5.1 constants (reviewer: claude:opus).
No file in the repo is imported; everything is recomputed from phi(s) directly."""
import mpmath as mp
mp.mp.dps = 40
g_E = mp.euler; lpi = mp.log(mp.pi)

def phi(s):
    return mp.sqrt(mp.pi)*mp.gamma(s-mp.mpf(1)/2)*mp.zeta(2*s-1)/(mp.gamma(s)*mp.zeta(2*s))
def dlogphi(s):   # phi'/phi by direct numerical derivative of log phi
    return mp.diff(lambda z: mp.log(phi(z)), s)
def q(z): return mp.zeta(z, derivative=1)/mp.zeta(z)
def m_auth(r):    # author's multiplier  -1/2 phi'/phi(1/2+ir), via the CLOSED FORM of <1>1
    s = mp.mpf(1)/2 + 1j*mp.mpf(r)
    v = mp.digamma(s-mp.mpf(1)/2) - mp.digamma(s) + 2*q(2*s-1) - 2*q(2*s)
    return -v/2
def m_ab(r):      # author's <1>2 form  a(r)+b(r)
    r = mp.mpf(r)
    a = -lpi + (mp.digamma(mp.mpf(1)/2+1j*r)+mp.digamma(mp.mpf(1)/2-1j*r))/2
    b = q(1+2j*r)+q(1-2j*r)
    return a, b, a+b
def m_script(r):  # script's multiplier  -Re phi'/phi(1/2+ir)
    s = mp.mpf(1)/2 + 1j*mp.mpf(r)
    v = (mp.digamma(s-mp.mpf(1)/2) - mp.digamma(s)
         + 2*(mp.zeta(2*s-1,derivative=1)/mp.zeta(2*s-1)
              - mp.zeta(2*s,derivative=1)/mp.zeta(2*s)))
    return -mp.re(v)
def m_arch_script(r):
    r = mp.mpf(r)
    return -mp.re(mp.digamma(1j*r) - mp.digamma(mp.mpf(1)/2+1j*r)
                  + 2*(mp.log(2*mp.pi) - mp.digamma(1-2j*r)))

print("== 1. phi'/phi chain rule (T5.1 <1>1): closed form vs numerical d/ds log phi ==")
for r in ('0.31','0.9','2.7','11.3'):
    s = mp.mpf(1)/2+1j*mp.mpf(r)
    cf = mp.digamma(s-mp.mpf(1)/2)-mp.digamma(s)+2*q(2*s-1)-2*q(2*s)
    print(f"   r={r:>6}  |closed - numeric| = {mp.nstr(abs(cf-dlogphi(s)),5)}")

print("== 2. m is REAL (so script's -Re phi'/phi = 2 * author's -1/2 phi'/phi) ==")
for r in ('0.31','0.9','2.7','11.3'):
    v = m_auth(r)
    print(f"   r={r:>6}  m_auth={mp.nstr(v,12)}   |Im|={mp.nstr(abs(mp.im(v)),5)}"
          f"   m_script/2 - m_auth = {mp.nstr(abs(m_script(r)/2-mp.re(v)),5)}")

print("== 3. functional-equation step (T5.1 <1>2): m = a + b, psi(ir) cancels ==")
for r in ('0.31','0.9','2.7','11.3'):
    a,b,tot = m_ab(r)
    print(f"   r={r:>6}  a={mp.nstr(mp.re(a),12)}  b={mp.nstr(mp.re(b),12)}"
          f"  |a+b-m_auth|={mp.nstr(abs(tot-m_auth(r)),5)}"
          f"  |a - m_arch_script/2|={mp.nstr(abs(mp.re(a)-m_arch_script(r)/2),5)}")

print("== 4. phi(1/2) = -1  and  m(0) = gamma_E - log pi - 2 log 2 ==")
print("   phi(1/2+1e-12) =", mp.nstr(phi(mp.mpf(1)/2+mp.mpf('1e-12')), 12))
m0pred = g_E - lpi - 2*mp.log(2)
for r in ('1e-6','1e-4','1e-2'):
    print(f"   r={r:>6}  m_auth(r)={mp.nstr(mp.re(m_auth(r)),12)}   predicted m(0)={mp.nstr(m0pred,12)}")

print("== 5. pairing check with h(t)=exp(-t^2/2):  <C,h> =? -<P,h> + <A,h> ==")
# <C,h> = int m(r) * (F^{-1}h)(r) dr,  F^{-1}h(r) = e^{-r^2/2}/sqrt(2pi)
f = lambda r: mp.re(m_auth(r))*mp.e**(-mp.mpf(r)**2/2)/mp.sqrt(2*mp.pi)
Cq = 2*mp.quad(f, [mp.mpf('1e-9'), 0.5, 2, 6, 14, 30])
print("   <C,h> by quadrature of m            =", mp.nstr(Cq, 18))
# <P,h>
def Lam(n):
    k=2; mm=n; ps=[]
    while k*k<=mm:
        if mm%k==0:
            ps.append(k)
            while mm%k==0: mm//=k
        k+=1
    if mm>1: ps.append(mm)
    return mp.log(ps[0]) if len(ps)==1 else mp.mpf(0)
P = mp.mpf(0)
for n in range(2, 4000):
    L = Lam(n)
    if L: P += 2*(L/n)*mp.e**(-2*mp.log(n)**2)
print("   <P,h> =", mp.nstr(P, 18))
# <A,h>
Aval = (mp.sqrt(2*mp.pi)/2 - (g_E+lpi)
        + mp.quad(lambda u: (mp.e**(-u) - mp.e**(-u/2)*mp.e**(-u**2/2))/(1-mp.e**(-u)),
                  [mp.mpf('1e-30'), 1e-6, 1e-3, 0.1, 1, 5, 30, 80]))
print("   <A,h> =", mp.nstr(Aval, 18))
print("   -<P,h> + <A,h> =", mp.nstr(Aval-P, 18))
print("   residual  <C,h> - (-<P,h>+<A,h>) =", mp.nstr(abs(Cq-(Aval-P)), 5))
print("   author's stated numbers: <A,h>=-0.487137717291990449  <P,h>=0.342066654304729763"
      "  <C,h>=-0.829204371596720212")
