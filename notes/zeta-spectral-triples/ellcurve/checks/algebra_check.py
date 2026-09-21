#!/usr/bin/env python3
"""Numerical checks of newly derived odd-radical algebra and scalar shifts.

This does not certify eigenvalues; it cross-checks the identities in the report.
"""
import sys
sys.dont_write_bytecode=True
from mpmath import mp
import ell_check as ec

mp.dps=80
N=16
L,a,b,_,_=ec.build('37a1',13,N)
ev=mp.eigsy(ec.parent.even_block(a,b,N),eigvals_only=True)
ov,U=mp.eigsy(ec.parent.odd_block(a,b,N))
assert ov[0]<ev[0] and ov[0]<ov[1]
inds=list(range(-N,N+1))
T=mp.matrix([[ec.parent.tau_entry(a,b,i,j)-(ov[0] if i==j else 0)
              for j in inds] for i in inds])
D=mp.diag(inds)
xi=mp.matrix([(-1 if j<0 else 1)*U[abs(j)-1,0]/mp.sqrt(2) if j else 0 for j in inds])
beta=mp.matrix([(-1 if j<0 else 1)*b[abs(j)] for j in inds])
eta=mp.matrix([1]*(2*N+1))
B=(beta.T*xi)[0]
Dp=D-(D*xi)*(beta.T/B)
e0=mp.matrix([int(j==0) for j in inds])
dinvxi=mp.matrix([xi[k]/j if j else 0 for k,j in enumerate(inds)])
print('37a1 x=13 N=16 dps=80 odd minimum=',mp.nstr(ov[0],35),'next odd=',mp.nstr(ov[1],35))
print('B=<beta,xi>=',mp.nstr(B,35))
errors={
    'T xi':mp.norm(T*xi),
    'T D xi-B eta':mp.norm(T*D*xi-B*eta),
    'T Dprime-Dprime.T T':mp.norm(T*Dp-Dp.T*T),
    'Dprime xi':mp.norm(Dp*xi),
    'Dprime V0':mp.norm(Dp*e0),
    'Dprime Dinvxi-xi':mp.norm(Dp*dinvxi-xi),
}
for name,err in errors.items():
    print(name,mp.nstr(err,8)); assert err<mp.mpf('1e-65')
for s in [mp.mpf('.37'),mp.mpf('2.31')]:
    g=sum(beta[k]*xi[k]/B/(j-s) for k,j in enumerate(inds))
    rhs=-s*mp.fprod(j-s for j in inds)*g
    err=abs(mp.det(Dp-s*mp.eye(2*N+1))-rhs)/max(1,abs(rhs))
    print('odd determinant identity relative error at s=',s,mp.nstr(err,8)); assert err<mp.mpf('1e-65')

L,a,b,_,_=ec.build('11a1',13,N)
E=ec.parent.even_block(a,b,N)
delta=mp.log(mp.mpf(389)/11)
vals,U=mp.eigsy(E); shifted,V=mp.eigsy(E+delta*mp.eye(N+1))
err=max(abs(shifted[k]-vals[k]-delta) for k in range(N+1))
v=U[:,0]; u=V[:,0]
if (v.T*u)[0]<0: u=-u
print('conductor shift log(389/11)=',mp.nstr(delta,40))
print('all even eigenvalue shift residual=',mp.nstr(err,8),'unit eigenvector residual=',mp.nstr(mp.norm(v-u),8))
assert err<mp.mpf('1e-65') and mp.norm(v-u)<mp.mpf('1e-65')
print('ALL ALGEBRA CHECKS PASS')
