#!/usr/bin/env python3
"""Prime-only direct double quadrature, no FFT, spline, zero input or lane imports.
Autocorrelation is integrated directly on its piecewise-smooth overlap intervals.
Uses the archimedean subtraction at exp(-2x), distinct from the lane's exp(-x).
Convergence estimates are numerical, not rigorous enclosures.
"""
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre,expit
H=Path(__file__).resolve().parent;lines=[]
L=.4;tau=.1
knots=np.array([-.2,-.1,.1,.2])
def g(x):
 a=np.abs(2*x/L);v=np.zeros_like(a);flat=a<=.5;v[flat]=np.exp(-x[flat]**2/(2*tau*tau));use=(a>.5)&(a<1)
 t=2*a[use]-1;v[use]=np.exp(-x[use]**2/(2*tau*tau))*expit(1/t-1/(1-t));return v

def run(order):
 nodes,weights=roots_legendre(order)
 def quad(fun,breaks):
  val=np.longdouble(0)
  for a,b in zip(breaks[:-1],breaks[1:]):
   if b>a:
    xx=(a+b)/2+(b-a)/2*nodes;val+=np.dot(weights.astype(np.longdouble),fun(xx).astype(np.longdouble))*(b-a)/2
  return val
 def h(x):
  x=np.atleast_1d(x).astype(float);ans=np.zeros_like(x)
  # Evaluate all node sets in batches, with every transition split exactly.
  for k,v in enumerate(x):
   if abs(v)>=L:continue
   a=max(-L/2,v-L/2);b=min(L/2,v+L/2)
   breaks=sorted(set([a,b]+[p for p in np.r_[knots,knots+v] if a<p<b]))
   ans[k]=quad(lambda s:g(s)*g(s-v),breaks)
  return ans
 lap=quad(lambda x:g(x)*np.exp(x/2),list(knots));c=[]
 for shift in [0,np.log(2.)]:
  U=L+shift;hzero=float(h(np.array([shift]))[0]);pole=2*np.cosh(shift/2)*lap*lap
  # For these two cells, exp(U)<3: either no prime or just n=2, exponent one.
  prime=0. if shift==0 else np.log(2.)/np.sqrt(2.)*float(h(np.array([0.]))[0])
  def integrand(x):
   pair=h(x-shift)+h(-x-shift)
   return (np.exp(-x/2)*pair-2*np.exp(-2*x)*hzero)/(-np.expm1(-2*x))
  breaks=sorted(set([0.,U]+[abs(shift+k*.1) for k in range(-4,5) if 0<abs(shift+k*.1)<U]))
  arch=(np.log(np.pi)+np.euler_gamma)*hzero+quad(integrand,breaks)+hzero*np.log(-np.expm1(-2*U))
  value=pole-prime-arch;c.append(value)
  emit(f'order={order} shift={shift:.17g} pole={pole:.17g} prime={prime:.17g} arch={arch:.17g} c={value:.17g}')
 emit(f'order={order} c0={c[0]:.17g} c1={c[1]:.17g} alpha0={c[1]/c[0]:.17g}')
 return c

def emit(v):print(v,flush=True);lines.append(v)
prev=None
for n in [48,72,108,160]:
 c=run(n)
 if prev is not None:emit('max moment change='+str(max(abs(a-b) for a,b in zip(prev,c))))
 prev=c
assert abs(c[0]-.0343767341909677)<2e-12
assert abs(c[1]+.0282307228929465)<2e-12
(H/'output_zeta_independent.txt').write_text('\n'.join(lines)+'\n')
