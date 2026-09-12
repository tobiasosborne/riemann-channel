"""REFUTE-stance independent checks of T1.1, T2.2, T3.1, T4.1, T4.2, T4.3 (reviewer: claude:opus)."""
import mpmath as mp, sympy as sp
mp.mp.dps = 30

print("=== T4.1  sign of  Lambda_fl = d/dsigma log D   (toy 'surface' with a finite length list) ===")
# The identity to test is purely formal in the length list, so any list with ell > 0 tests it.
ells = [mp.mpf('1.3'), mp.mpf('2.1'), mp.mpf('2.1'), mp.mpf('3.7')]   # repeats allowed
def Lambda_fl(sig, K=400):
    return sum(l*mp.e**(-sig*k*l)/(4*mp.sinh(k*l/2)**2) for l in ells for k in range(1,K+1))
def logZ(s, K=400):     # log of the Selberg Euler product
    return sum(mp.log(1-mp.e**(-(s+qq)*l)) for l in ells for qq in range(0,K+1))
def logD(sig, J=400):
    return sum(logZ(sig+j) for j in range(1,J+1))
for sig in ('0.35','0.9','2.0'):
    s = mp.mpf(sig)
    lhs = Lambda_fl(s); rhs = mp.diff(logD, s)
    print(f"   sigma={sig:>5}  Lambda_fl={mp.nstr(lhs,15)}  +D'/D={mp.nstr(rhs,15)}"
          f"  |diff|={mp.nstr(abs(lhs-rhs),4)}   -D'/D={mp.nstr(-rhs,10)}")
# also the tower product form  D = prod_gamma prod_{m>=0} (1-e^{-(sig+m+1)l})^{m+1}
def logD_tower(sig, M=400):
    return sum((m+1)*mp.log(1-mp.e**(-(sig+m+1)*l)) for l in ells for m in range(0,M+1))
print("   tower form agrees with prod_j Z(sig+j):",
      mp.nstr(abs(logD(mp.mpf('0.9'))-logD_tower(mp.mpf('0.9'))),4))
# and D = exp(-int_0^inf e^{-sigma t} Tr^flat / t dt)
def logD_laplace(sig, K=400):
    return -sum((1/mp.mpf(k))*mp.e**(-(sig+1)*k*l)/(1-mp.e**(-k*l))**2 for l in ells for k in range(1,K+1))
print("   Laplace/t form agrees:", mp.nstr(abs(logD(mp.mpf('0.9'))-logD_laplace(mp.mpf('0.9'))),4))
print("   => the brief's  Lambda = -(d/dsigma) log D  is WRONG by a sign; author's +D'/D is right.")

print()
print("=== T4.1  1/(4 sinh^2(x/2)) = e^{-x}/(1-e^{-x})^2 = sum_{m>=0}(m+1)e^{-(m+1)x} ===")
x = mp.mpf('0.83')
print("   ", mp.nstr(1/(4*mp.sinh(x/2)**2),20), mp.nstr(mp.e**(-x)/(1-mp.e**(-x))**2,20),
      mp.nstr(sum((m+1)*mp.e**(-(m+1)*x) for m in range(0,600)),20))

print()
print("=== T3.1  |det(1-P^k)| ===")
l,k = sp.symbols('ell k', positive=True)
det = sp.expand((1-sp.exp(k*l))*(1-sp.exp(-k*l)))
print("   det(1-P^k) =", sp.simplify(det), "  (negative)")
print("   |det| - 4 sinh^2(kl/2) =", sp.simplify(-det - 4*sp.sinh(k*l/2)**2))
print("   |det| - e^{kl}(1-e^{-kl})^2 =", sp.simplify(-det - sp.exp(k*l)*(1-sp.exp(-k*l))**2))
print("   |det| - (e^{kl}-1)(1-e^{-kl}) =", sp.simplify(-det - (sp.exp(k*l)-1)*(1-sp.exp(-k*l))))

print()
print("=== T2.2  author's own section g_{x,y}, recomputed independently (sympy) ===")
u = sp.symbols('u', real=True); xs = sp.Symbol('x', real=True); ys = sp.Symbol('y', positive=True)
g0 = sp.Matrix([[sp.sqrt(ys), xs/sp.sqrt(ys)],[0, 1/sp.sqrt(ys)]])
print("   det g_{x,y} =", sp.simplify(g0.det()), "   g.i =", sp.simplify((g0[0,0]*sp.I+g0[0,1])/(g0[1,0]*sp.I+g0[1,1])))
def mob(M, z): return (M[0,0]*z+M[0,1])/(M[1,0]*z+M[1,1])
expH = sp.Matrix([[sp.exp(u),0],[0,sp.exp(-u)]])
expE = sp.Matrix([[sp.cosh(u),sp.sinh(u)],[sp.sinh(u),sp.cosh(u)]])
expW = sp.Matrix([[sp.cos(u),sp.sin(u)],[-sp.sin(u),sp.cos(u)]])
F = sp.Function('F')
def second(Ex):
    z = sp.simplify(mob(g0*Ex, sp.I))
    X = sp.simplify(sp.re(sp.expand(z))); Y = sp.simplify(sp.im(sp.expand(z)))
    X = sp.simplify(sp.refine(sp.re(z), sp.Q.real(u))); Y = sp.simplify(sp.refine(sp.im(z), sp.Q.real(u)))
    e = F(X, Y)
    return sp.simplify(sp.diff(e, u, 2).subs(u,0)), X, Y
H2, XH, YH = second(expH); E2, XE, YE = second(expE); W2, XW, YW = second(expW)
print("   g exp(uH).i :", sp.simplify(XH), "+ i(", sp.simplify(YH), ")")
print("   g exp(uE).i :", sp.simplify(XE), "+ i(", sp.simplify(YE), ")")
Fxx = sp.Derivative(F(xs,ys),xs,2); Fyy = sp.Derivative(F(xs,ys),ys,2); Fy = sp.Derivative(F(xs,ys),ys)
print("   H^2 f - (4y^2 F_yy + 4y F_y) =", sp.simplify(H2 - (4*ys**2*Fyy + 4*ys*Fy).doit()))
print("   E^2 f - (4y^2 F_xx - 4y F_y) =", sp.simplify(E2 - (4*ys**2*Fxx - 4*ys*Fy).doit()))
print("   W^2 f =", sp.simplify(W2))
Om = sp.simplify((H2+E2-W2)/4)
print("   Omega f =", Om, "   => c = 1  (Omega = +y^2(F_xx+F_yy) = -Delta F)")
print("   (1/2)(H^2+E^2) f - 2*Omega f =", sp.simplify((H2+E2)/2 - 2*Om))
print("   (1/2)(H^2+E^2) f = -2 Delta F ? residual:",
      sp.simplify((H2+E2)/2 - 2*(ys**2*(Fxx+Fyy)).doit()))

print()
print("=== T1.1  Poisson normalisation, h(t)=exp(-t^2/2), L=1.7 ===")
L = mp.mpf('1.7')
hh = lambda t: mp.e**(-mp.mpf(t)**2/2)
hhat = lambda r: mp.sqrt(2*mp.pi)*mp.e**(-mp.mpf(r)**2/2)     # int e^{-irt}h(t)dt
lhs = sum(hhat(-2*mp.pi*n/L) for n in range(-200,201))
rhs = L*sum(hh(k*L) for k in range(-200,201))
print("   sum_n hhat(-2 pi n/L) =", mp.nstr(lhs,20), "   L sum_k h(kL) =", mp.nstr(rhs,20),
      "   diff =", mp.nstr(abs(lhs-rhs),4))

print()
print("=== T4.2  divisor bookkeeping at sigma = -N  (D = prod_{j>=1} Z(sigma+j)) ===")
gg = sp.Symbol('g')
for N in range(1,5):
    topo = sum((2*gg-2)*(2*n+1) for n in range(0,N))          # s_*=-n, j=N-n>=1
    print(f"   N={N}: topological order = {sp.expand(topo)}  == (2g-2)N^2 -> {sp.simplify(topo-(2*gg-2)*N**2)==0}"
          f";  constant-mode (s_*=0,j=N) + (s_*=1,j=N+1) = 2;  total = (2g-2)N^2+2")
print("   at sigma=0: only s_*=1 with j=1 -> order 1 (simple).")
print("   first band strip -1<Re<0 : k=0 nonconstant only; k>=1 gives Re <= -3/2 (real r) or < -1 (exceptional).")
