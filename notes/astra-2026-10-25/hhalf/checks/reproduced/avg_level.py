#!/usr/bin/env python3
"""Level averages: orthogonality, explicit finite fields, and exact Ramanujan sums."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from common import *


def field_log(q,f):
    d=len(f)-1;mod=nmod_poly(list(f),q);Q=q**d
    prime_div=[int(p) for p in sp.factorint(Q-1)]
    for code in range(2,Q):
        v=nmod_poly([(code//q**i)%q for i in range(d)],q)
        if all(v.pow_mod((Q-1)//p,mod)!=1 for p in prime_div):break
    else:raise AssertionError('No generator')
    table={};a=nmod_poly([1],q)
    for i in range(Q-1):
        key=tuple(int(a[j]) for j in range(d))
        assert key not in table
        table[key]=i;a=(a*v)%mod
    return table


def ramanujan(N,k):
    return sum(int(r*sp.mobius(N//r)) for r in sp.divisors(math.gcd(N,k)))


def order_sum(q,f,N,logs):
    d=len(f)-1
    return [sum(ramanujan(N,logs[tuple(a)+(0,)*(d-len(a))]) for a in monics(q,n)) for n in range(d)]


def main():
    u=sp.Symbol('u')
    with Path(__file__).with_name('output_level.txt').open('w') as out:
        def emit(s):print(s,flush=True);print(s,file=out,flush=True)
        for q,d in [(3,2),(3,3),(5,2),(5,3),(7,2),(7,3)]:
            f=irreducibles(q,d)[0];Q=q**d;logs=field_log(q,f)
            sums=[Q-2]+[-q**n for n in range(1,d)]
            N=Q*u**d-(q**(d+1)-q)*u+(Q-2)
            assert sp.expand((1-q*u)*expr(sums)-N)==0
            direct=[sum((Q-1 if logs[tuple(a)+(0,)*(d-len(a))]==0 else 0)-1 for a in monics(q,n)) for n in range(d)]
            assert direct==sums
            avg=[F(x,Q-2) for x in sums]
            emit(f'q={q} d={d} f={expr(f,"x")} nontrivial_count={Q-2} raw_sum={expr(sums)} rational_function_check=True direct_orthogonality_check=True')
            root_report(avg,q,'all nontrivial raw',emit)
            comp=[F(Q-2)]+[F(Q-q**(k+1),q-1) for k in range(1,d-1)]
            emit(f'  sum_of_completed_members={expr(comp)}')
            root_report(comp,q,'all nontrivial completed',emit)
            total=[0]*d;completed_total=[0]*(d-1)
            for order in sp.divisors(Q-1):
                if order==1:continue
                s=order_sum(q,f,order,logs)
                total=[a+b for a,b in zip(total,s)]
                even=((Q-1)//(q-1))%order==0
                c=[sum(s[:k+1]) for k in range(d-1)] if even else s
                if even:assert sum(s)==0
                if len(completed_total)<len(c):completed_total += [0]*(len(c)-len(completed_total))
                for j,v in enumerate(c):completed_total[j]+=v
                den=int(sp.totient(order))
                emit(f'  exact_order={order} count={den} even={even} raw_average={expr([F(x,den) for x in s])} completed_average={expr([F(x,den) for x in c])}')
                root_report([F(x,den) for x in c],q,f'order {order} completed',emit)
            assert total==sums
            while completed_total and completed_total[-1]==0:completed_total.pop()
            assert completed_total==comp
        emit('ALL LEVEL ORTHOGONALITY, RATIONAL-FUNCTION AND EXACT-ORDER CHECKS PASS.')


if __name__=='__main__':main()
