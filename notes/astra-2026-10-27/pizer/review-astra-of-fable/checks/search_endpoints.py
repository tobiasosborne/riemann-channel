from cypari2 import Pari
P=Pari(); P.allocatemem(300000000, silent=True)
x=P('x')
for p in range(5,1000):
 if not P.isprime(p): continue
 mf=P.mfinit([p,2],1)
 for l in (2,3,5,7):
  if l==p: continue
  c=P.charpoly(P.mfheckemat(mf,l))
  d=P.gcd(c,x*x-4*l)
  if P.poldegree(d)>0:
   print('ENDPOINT',p,l,c,d,flush=True)
 print('done',p,flush=True)
