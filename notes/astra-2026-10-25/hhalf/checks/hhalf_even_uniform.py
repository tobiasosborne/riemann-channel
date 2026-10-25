#!/usr/bin/env python3
"""Uniform completed-even RH through genus seven; exact sign brackets.
Polynomiality and degree bounds (including odd raw degrees) are proved in the note.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import sympy as sp
from exact_core import raw_series

def sign_sqrt3(expr):
    val=sp.simplify(expr)
    if val==0:return 0
    return 1 if val>0 else -1

def interpolate(nodes,vals,q):
    dd=list(map(sp.Rational,vals));ans=0;prod=1
    for k in range(len(nodes)):
        ans+=dd[0]*prod;prod*=q-nodes[k]
        dd=[(dd[j+1]-dd[j])/(nodes[j+k+1]-nodes[j]) for j in range(len(dd)-1)]
    return sp.Poly(ans,q)

def main():
    q,t,x=sp.symbols('q t x');nodes=list(sp.primerange(3,98));D=16
    brackets={1:[-2,2],2:[-2,0,2],3:[-2,-1,1,2],4:[-2,sp.Rational(-6,5),0,1,2],5:[-2,sp.Rational(-3,2),sp.Rational(-1,2),sp.Rational(1,2),sp.Rational(7,5),2],6:[-2,sp.Rational(-8,5),-1,0,sp.Rational(4,5),sp.Rational(3,2),2],7:[-2,sp.Rational(-33,20),sp.Rational(-11,10),sp.Rational(-2,5),sp.Rational(2,5),1,sp.Rational(8,5),2]}
    with Path(__file__).with_name('output_even_uniform.txt').open('w') as log:
        def emit(s):print(s,flush=True);print(s,file=log,flush=True)
        data={}
        for p in nodes+[101,103,9]:
            data[p]={n:[int(z) for z in raw_series(int(p),n,D)[0]] for n in range(1,8)}
            emit(f'computed_node={p}')
        for g,ys in brackets.items():
            d=2*g+2;S=[(q-1)*q**(d-1)]
            for n in range(1,g+1):
                P=interpolate(nodes,[data[p][n][d] for p in nodes],q)
                assert P.degree()<=d+n
                for p in [101,103,9]:assert P.eval(p)==data[p][n][d],(g,n,p)
                S.append(P.as_expr())
            C=[sum(S[:i+1]).subs(q,t*t) for i in range(g+1)]
            sk=[sp.Integer(2),x]
            for i in range(2,g+1):sk.append(sp.expand(x*sk[-1]-sk[-2]))
            N=sp.expand(C[g]+sum(C[i]*t**(g-i)*sk[g-i] for i in range(g)))
            emit(f'g={g} raw_sum_polynomials={S}')
            emit(f'  normalized_y_brackets={ys}')
            for i,y in enumerate(ys):
                want=(-1)**(g-i);P=sp.Poly(want*N.subs(x,y),t)
                shifted=sp.Poly(P.as_expr().subs(t,t+sp.sqrt(3)).expand(),t,extension=sp.sqrt(3))
                signs=[sign_sqrt3(c) for c in shifted.all_coeffs()]
                if all(s>=0 for s in signs) and sign_sqrt3(shifted.nth(0))>0:
                    emit(f'  y={y} required_sign={want} method=positive_shifted_coefficients degree={P.degree()} zero_coefficients={signs.count(0)} minimum_positive=True')
                else:
                    seq=sp.sturm(P.as_expr(),t)
                    lower=[sign_sqrt3(f.subs(t,sp.sqrt(3))) for f in seq]
                    upper=[int(sp.sign(sp.Poly(f,t).LC())) for f in seq]
                    def variations(v):
                        v=[s for s in v if s];return sum(a!=b for a,b in zip(v,v[1:]))
                    assert variations(lower)==variations(upper) and sign_sqrt3(P.eval(sp.sqrt(3)))>0,(g,y)
                    emit(f'  y={y} required_sign={want} method=Sturm_on_[sqrt3,infinity) signs_at_sqrt3={lower} signs_at_infinity={upper} no_roots=True')
            emit(f'PROVED even g={g} all odd prime powers q: {g} distinct real normalized roots in (-2,2).')
        emit('PROVED: COMPLETED EVEN-DEGREE AVERAGE RH FOR ALL ODD PRIME POWERS AND g=1..7.')
if __name__=='__main__':main()
