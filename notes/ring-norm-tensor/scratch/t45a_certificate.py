# Author: codex:gpt-6-astra
import mpmath as mp
mp.mp.dps=110
base_text="0.26071183 -0.77630597 0.1256142 0.57129743 0.23357458 -0.48921698 -1.34760956 -0.05591677 -0.94940643 -0.38739751 -0.67840262 -1.61862569 0.09572017 -0.36950433 -0.80102781 0.32500101 -1.0690133 -0.50378403 0.0903946 -0.85610066 -0.89848953 -0.00971177 -0.9517933 -0.63028434 0.30058661 1.43919288 0.38038457 -1.21909557".split()
sel=[18,15,11,19,14,2,22,4,3]
pos=[(s,i,j) for s in range(3) for i in range(3) for j in range(3) if (s<2)==((i==0)==(j==0))]
idxs=([0,4,5,7,8],[1,2,3,6]); ns=(5,4);target=[6,26,126,626,3126,3,-5,9,7]
active = [
    '0.0903946022326197086918581936003652642108422681757834121198569509935751292079285209190880028',
    '0.325001015712151197553026743073611383028909263869300480901353211781331926553983584722142652',
    '-1.61862568848573412561085612335033964354282729706378489347434769629526938804341538871295182',
    '-0.856100671883734631506405289461842300801039252464833047343784570879130428726933907333213827',
    '-0.80102781481057057826927943665335609983310469191396383065095317561795085119201793039066329',
    '0.125614201299343247797946104304359812581511668431930091377412797232085492448163457526247418',
    '-0.951793304521566588362992674206553375775973049960369410863894719514069329407054372830229032',
    '0.233574566527024915170370648357379441749679527579971848850435885749412325417262635189600452',
    '0.571297437238715211680159923446246584732241927298292338354479377560643476028340257150472248'
]
from fractions import Fraction as F
zero=(F(0),F(0));one=(F(1),F(0))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def matmul(a,b):
 out=[[zero for _ in b[0]] for _ in a]
 for i in range(len(a)):
  for k in range(len(b)):
   if a[i][k]==zero:continue
   for j in range(len(b[0])):
    if b[k][j]!=zero:out[i][j]=add(out[i][j],mul(a[i][k],b[k][j]))
 return out
def trace(a):
 z=zero
 for i in range(len(a)):z=add(z,a[i][i])
 assert z[1]==0
 return z[0]
def traced_product(a,b):
 z=zero
 for i in range(len(a)):
  for j in range(len(a)):z=add(z,mul(a[i][j],b[j][i]))
 assert z[1]==0
 return z[0]
x=list(map(F,base_text))
for l,v in zip(sel,active):x[l]=F(v)
As=[[[zero]*3 for _ in range(3)] for _ in range(3)]
for l,(s,i,j) in enumerate(pos):As[s][i][j]=(x[2*l],x[2*l+1])
Es=[]
for idx in idxs:
 E=[]
 for r in idx:
  row=[]
  for c in idx:
   z=zero
   for A in As:z=add(z,mul(A[r//3][c//3],conj(A[r%3][c%3])))
   row.append(z)
  E.append(row)
 Es.append(E)
ps=[]
for E,n in zip(Es,ns):
 p=[[[one if i==j else zero for j in range(len(E))] for i in range(len(E))]]
 for _ in range(n):p.append(matmul(p[-1],E))
 ps.append(p)
f=[trace(p[n])-t for (p,n),t in zip(((p,n) for p,nn in zip(ps,ns) for n in range(1,nn+1)),target)]
J=[[F(0)]*9 for _ in range(9)]
for col,l in enumerate(sel):
 s,i,j=pos[l//2];d=[[zero]*3 for _ in range(3)];d[i][j]=one if l%2==0 else (F(0),F(1));A=As[s]
 des=[[[add(mul(d[r//3][c//3],conj(A[r%3][c%3])),mul(A[r//3][c//3],conj(d[r%3][c%3]))) for c in idx] for r in idx] for idx in idxs]
 vals=[n*traced_product(p[n-1],de) for p,de,nn in zip(ps,des,ns) for n in range(1,nn+1)]
 for row,v in enumerate(vals):J[row][col]=v
print("exact F,J evaluated",flush=True)
to_mp=lambda z:mp.mpf(z.numerator)/z.denominator
BM=mp.inverse(mp.matrix([[to_mp(z) for z in row] for row in J]))
B=[[F(mp.nstr(BM[i,j],60)) for j in range(9)] for i in range(9)]
bn=max(sum(map(abs,row)) for row in B)
eta=max(abs(sum(B[i][j]*f[j] for j in range(9))) for i in range(9))
eps=max(sum(abs(F(i==j)-sum(B[i][k]*J[k][j] for k in range(9))) for j in range(9)) for i in range(9))
radius=F(1,10**30);H=F(10**16);kappa=eps+bn*81*H*radius
assert max(map(abs,x))<2
assert bn<2
assert eta<F(1,10**70)
assert eps<F(1,10**50)
assert kappa<F(1,4)
assert eta+kappa*radius<radius
print("CERTIFIED", "B norm",float(bn),"eta",float(eta),"eps",float(eps),"kappa",float(kappa),flush=True)
