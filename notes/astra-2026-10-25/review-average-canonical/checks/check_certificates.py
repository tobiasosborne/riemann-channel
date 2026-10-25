#!/usr/bin/env python3
"""Verify every printed finite certificate with independent Hermite moment matrices.
Input coefficients are the exact A2 outputs; this root test is not the lane's Sturm test.
"""
from pathlib import Path
import re
import sympy as s
H=Path(__file__).resolve().parent;ROOT=H.parents[3];x,u,w=s.symbols('x u w');lines=[]
def emit(*a):v=' '.join(map(str,a));print(v,flush=True);lines.append(v)
def reduce_reciprocal(coeff,q):
 g=(len(coeff)-1)//2;S=[s.Integer(2),x]
 for k in range(2,g+1):S.append(s.expand(x*S[-1]-q*S[-2]))
 return s.Poly(coeff[g]+sum(coeff[i]*S[g-i] for i in range(g)),x)
def certificate(P,R2):
 n=P.degree();a=P.monic().all_coeffs();powers=[s.Integer(n)]
 for k in range(1,2*n+1):
  v=-sum(a[j]*powers[k-j] for j in range(1,min(k,n)+1) if j<k)
  if k<=n:v-=k*a[k]
  powers.append(s.cancel(v))
 Hm=s.Matrix(n,n,lambda i,j:powers[i+j]);Km=s.Matrix(n,n,lambda i,j:R2*powers[i+j]-powers[i+j+2])
 hd=[s.factor(Hm[:j,:j].det()) for j in range(1,n+1)];kd=[s.factor(Km[:j,:j].det()) for j in range(1,n+1)]
 assert all(v>0 for v in hd+kd)
 return hd[-1],kd[-1]
count=[0,0]
for line in (ROOT/'notes/astra-2026-10-23/average/checks/output_extended.txt').read_text().splitlines():
 m=re.match(r'q=(\d+) g=(\d+) average=(.*)',line)
 if m:
  q,g=int(m[1]),int(m[2]);A=s.Poly(s.sympify(m[3]),u);b=[A.nth(2*j)/q**j for j in range(g+1)]
  assert all(A.nth(j)==0 for j in range(1,2*g,2)) and b==b[::-1]
  assert all(b[j]>=b[j+1]>0 for j in range(g//2))
  B=sum(c*w**j for j,c in enumerate(b))
  if g%2:B=s.div(B,1+w,w)[0]
  cc=s.Poly(B,w);P=reduce_reciprocal(list(reversed(cc.all_coeffs())),1)
  result=certificate(P,4) if P.degree()>0 else ('empty','empty')
  emit('odd',q,g,'Hhalf=True','Hermite determinants H,K=',result);count[0]+=1
 m=re.match(r'even q=(\d+) g=(\d+) completed_average=(.*?) exact_Sturm_band=True',line)
 if m:
  q,g=int(m[1]),int(m[2]);A=s.Poly(s.sympify(m[3]),u);P=reduce_reciprocal([A.nth(j) for j in range(2*g+1)],q)
  emit('even',q,g,'Hermite determinants H,K=',certificate(P,4*q));count[1]+=1
assert count==[26,14];emit('ALL independent Hermite certificates PASS:',count)
# Trace moments cannot distinguish semisimple from Jordan realization.
I=s.eye(2);J=s.Matrix([[1,1],[0,1]])
assert all(s.trace(I**k)==s.trace(J**k)==2 for k in range(10))
emit('same moments for I2 and Jordan(1): c0..9=[2]*10; alpha0=1; Jordan structures differ')
(H/'output_certificates.txt').write_text('\n'.join(lines)+'\n')
