"""Source-extracted scalar audit; no input from either lane's programs."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, localcontext
import re
import sympy as s

ROOT = Path(__file__).resolve().parents[4]
src = ROOT/'notes/astra-2026-10-23/qrh/sources/liu-2610.12234.txt'
lines = src.read_text().split('\n')
line = next((i,l) for i,l in enumerate(lines,1) if '1188' in l and l.strip().startswith('1188'))
print('Liu source definition:',src.relative_to(ROOT), 'line',line[0],line[1].strip())
# Parse the coefficients from the source's displayed polynomial, not a lane.
nums=list(map(int,re.findall(r'\d+',line[1])))
assert nums[1:2]==[3] and nums[3:4]==[2] and nums[-1]==0
a,_,b,_,c,d,_=nums
x,k=s.symbols('x k')
P=a*x**3-b*x**2+c*x+d
# Independent elimination by polynomial resultant of L lines 245 and 270-272.
Q=(216*k-18)*x**2-(468*k-57)*x+150*k-20
E=(18*x+9)*k-(18*x+5)
elim=s.Poly(s.resultant(Q,E,k),x).primitive()[1].monic()
assert elim==s.Poly(P,x).monic()
print('eliminated primitive cubic:',s.Poly(s.resultant(Q,E,k),x).primitive()[1].as_expr())
intervals=s.polys.polytools.intervals(P,eps=s.Rational(1,10**72))
isolated=[(a,b) for (a,b),m in intervals if a>s.Rational(38858,100000) and b<s.Rational(38859,100000)]
assert len(isolated)==1
lo,hi=isolated[0]
assert P.subs(x,lo)>0>P.subs(x,hi)
Bl=(18*lo+7)/(18*lo+9); Bh=(18*hi+7)/(18*hi+9)
print('root certified interval:',lo,hi)
print('xi midpoint:',s.N((lo+hi)/2,65))
print('B midpoint:',s.N((Bl+Bh)/2,65))
print('B interval width:',s.N(Bh-Bl,8))
print('7/8 - B:',s.N(s.Rational(7,8)-(Bl+Bh)/2,35))
alpha=s.solve(s.Eq(s.Rational(1,2)+5*x/12,1-x/6),x)[0]
print('amplifier at H=D squared exponents:',s.Rational(11,6),s.Rational(5,3))
print('balanced alpha, theta:',alpha,s.Rational(1,2)+5*alpha/12)
print('O7 low exponent:',s.Rational(17,96)+s.Rational(1,96),'boundary:',s.Rational(3,16)+s.Rational(11,16))
print('mode-depth interval:',(F(1)-F(7,8))/2,(F(1)-F(1,8))/2)

# Cubic character of F7 built from the generator; show every entry as a power
# of omega, and independently count nonzero Fourier coefficients in Q(zeta_21).
log={pow(3,j,7):j for j in range(6)}
support=[u for u in range(7) if u in log]
print('F7 cubic charge: x=0 -> 0; exponents of omega for x=1..6:',[log[u]%3 for u in range(1,7)])
print('charge support:',support,'size=',len(support))
z=s.Symbol('z'); phi=s.Poly(s.cyclotomic_poly(21,z),z)
fourier=[]
for b in range(7):
    # 7*(log mod 3) is the embedding omega=zeta_21^7.
    v=sum(z**((7*(log[u]%3)+3*b*u)%21) for u in range(1,7))
    fourier.append(not s.Poly(v,z).rem(phi).is_zero)
print('Fourier charge support size:',sum(fourier))
assert len(support)==sum(fourier)==6

M=s.Matrix([[5,-5],[1,0]]); O=s.Matrix([[0,1],[-1,0]])
print('rank counterexample characteristic polynomial:',M.charpoly().as_expr())
assert M.T*O*M==5*O
print('rank counterexample similitude residual:',list(M.T*O*M-5*O))

# O11 norm-seven calculation in an exact cyclotomic ring, rather than the
# lane's floating complex arithmetic. pi=-2-3*omega, omega mod pi = 4.
ph42=s.Poly(s.cyclotomic_poly(42,z),z)
def red(p):return s.Poly(p,z).rem(ph42).as_expr()
ch={}
for sign in (1,-1):
    for j in range(3):ch[sign*pow(4,j,7)%7]=red(sign*z**(14*j))
def gauss(j):
    # All nonzero values have order 6; use exponents mod 6 instead of inversion.
    return red(sum(red(ch[u]**(j%6))*z**((18*u)%42) for u in range(1,7)))
pi=-2-3*z**14;barpi=-2-3*z**28;barc4=red(ch[4]**5)
G={j:gauss(j) for j in (1,2,3,5)}
res=red(-barc4*G[5]*G[3]-ch[6]*barpi*G[2])
assert res==0
assert red(G[2]**3+7*pi)==0
assert red(G[1]*G[2]+pi*barc4*G[3])==0
assert red(G[1]*G[5]-7*ch[6])==0
wrong=red(-ch[4]*G[5]*G[3]-ch[6]*pi*G[2])
assert wrong!=0
print('O11 four exact Gauss identity residuals: 0,0,0,0')
print('O11 unbarred identity exact nonzero residual:',wrong)

# O7 endpoint identity: use E=13R/16-5/6+delta*(2/3+x/6),
# derived by collecting the source's relative exponent before substitution.
delta,y=s.symbols('delta y');x=s.Rational(1,2)-y
D=3-s.Rational(17,9)*x;P=(2-s.Rational(8,9)*x)*(1-x)
J=(s.Rational(5,6)-delta)*D+delta*P
R=1-delta+(s.Rational(5,6)-delta)*delta*P/(2*J)
E=s.Rational(13,16)*R-s.Rational(5,6)+delta*(s.Rational(2,3)+x/6)
v=51+41*y
cert=(3+5*y)*((4*v*delta-79)**2+49)+4*y*(4*v*delta*((1+3*y)*(15+32*y)*delta+9-13*y)+265+3485*y)
assert s.cancel(10368*v*J*(-E)-cert)==0
print('O7 endpoint expanded identity residual: 0; margin=',s.Rational(49,440640))
Pbad=2-s.Rational(8,9)*x*(1-x)
Jbad=(s.Rational(5,6)-delta)*D+delta*Pbad
Rbad=1-delta+(s.Rational(5,6)-delta)*delta*Pbad/(2*Jbad)
Ebad=s.Rational(13,16)*Rbad-s.Rational(5,6)+delta*(s.Rational(2,3)+x/6)
point={delta:s.Rational(2,5),y:0}
good=s.cancel(E.subs(point));bad=s.cancel(Ebad.subs(point))
assert good<0<bad
print('Q1 prose P_x error, at delta=2/5,x=1/2: correct E=',good,'printed E=',bad)
print('Kintali central margin:',s.Rational(47,48)-s.Rational(29,30))
print('PASS: exact algebra and root isolation; no floating decision or L-zero input.')
