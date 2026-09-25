# Author: codex:gpt-6-astra
"""Exact symbolic checks of the trivial cavities; finite-degree counts for all blocks."""
import sys
sys.dont_write_bytecode = True
import sympy as s
from finite_graph import quotient,CASES
z=s.symbols('z')
for q,N in CASES:
    g=quotient(q,N,0);d=len(N)-1;n=sum(len(x) for x in g['V'][:-1]);T=s.zeros(n);C=s.zeros(n)
    offs=[0]
    for layer in g['V'][:-1]:offs.append(offs[-1]+len(layer))
    for j,edges in enumerate(g['E']):
        for a,b,se in edges:
            i=offs[j]+a
            if j<d-1:
                k=offs[j+1]+b
                T[i,k]+=s.Rational(g['st'][j][a],se)/s.sqrt(q)
                T[k,i]+=s.Rational(g['st'][j+1][b],se)/s.sqrt(q)
            else:C[i,i]+=s.Rational(g['st'][j][a]*g['st'][j+1][b],q*se*se)
    p=s.factor(((1+z*z)*s.eye(n)-z*T-C).det())
    cd=sum(z**(2*(d-1-j))*s.Rational(1,q)**j for j in range(d))
    predicted=z**(4*d-4)*(z*z-q)*cd
    assert s.cancel(p-predicted)==0
    print('q,d,n',q,d,n,'p=',p)
    r=(q**d-1)//(q-1);ar=4*(d-2)*(r-1) if d>1 else 0
    delay=4*(d-1)*r;local=2*d-2
    print('Gamma1: arithmetic, local nonzero, delays, total, exits',ar,local,delay,ar+local+delay,2*r)
