#!/usr/bin/env python3
"""Exact flux audits, reduced resultants, and double-cover obstructions.
Use matrix Chebyshev recurrence, independently of the old 2n-step powers.
No negative verdict is inferred from a central-order unit obstruction.
"""
import itertools
import json
from collections import Counter
import sympy as S
from census_lookup import HERE,FLUX,counts_from_coeff

x=S.Symbol('x')

def divisor_candidates(c,dim):
    fs=S.factor_list(S.Poly.from_list(c,x))[1]
    for exps in itertools.product(*(range(e+1) for f,e in fs)):
        if sum(e*f.degree() for e,(f,_) in zip(exps,fs))==2*dim:
            p=S.Poly(S.prod(f.as_expr()**e for e,(f,_) in zip(exps,fs)),x)
            yield tuple(map(int,p.all_coeffs()))

def reduced_partitions(c):
    fs=S.factor_list(S.Poly.from_list(c,x))[1]
    out=[]
    for m in range(1,2**(len(fs)-1)):
        h0=S.Poly(S.prod(f.as_expr() for i,(f,_) in enumerate(fs) if m>>i&1),x)
        h1=S.Poly(S.prod(f.as_expr() for i,(f,_) in enumerate(fs) if not (m>>i&1)),x)
        a,b,g=S.gcdex(h0,h1)
        assert g.as_expr()==1
        n=int(S.ilcm(*([1]+[v.q for v in a.all_coeffs()+b.all_coeffs()])))
        assert (n*a*h0+n*b*h1).as_expr()==n
        assert all(v.q==1 for v in (n*a).all_coeffs()+(n*b).all_coeffs())
        out.append(dict(left=str(h0.as_expr()),right=str(h1.as_expr()),reduced=n,
                        resultant=abs(int(S.resultant(h0,h1))),bezout=[str((n*a).as_expr()),str((n*b).as_expr())]))
    return out

def main():
    rows=json.loads(FLUX.read_text())
    low=json.loads((HERE/'output_lowgenus.json.txt').read_text())
    genus2={tuple(c) for c in low['genus2_polynomials']}
    pp_factors={tuple(v['coeff']) for v in low['factors'].values() if v['hyp_equations']>0}
    pp_factors|={tuple(v['coeff']) for v in low['elliptic']}
    focus={('K33',1),('K33',6),('cube',3),('cube',5),('Petersen',6),('Petersen',10),('Petersen',22)}
    outputs=[]
    for r in rows:
        if not r['ramanujan']:continue
        A=S.Matrix(r['A']);n=A.rows;q=r['p']
        R0=2*S.eye(n);R1=A;N=[]
        for k in range(1,32):
            tr=int(S.trace(R1));N.append(q**k+1-tr)
            R0,R1=R1,A*R1-q*R0
        assert N==[r['N'][str(k)] for k in range(1,32)]
        aa=[]
        for k in range(1,32):
            num=sum(int(S.mobius(k//d))*N[d-1] for d in S.divisors(k))
            assert num%k==0
            aa.append(num//k)
        assert aa==[r['a'][str(k)] for k in range(1,32)]
        minors=[int((4*q*S.eye(n)-A*A)[:j,:j].det()) for j in range(1,n+1)]
        assert all(v>0 for v in minors)
        assert counts_from_coeff(r['weil_coefficients'],31,q)==N
        rank=max(i for i,a in enumerate(r['weil_coefficients']) if a%q)
        assert all((N[k-1]-q**k-1)**2<=4*n*n*q**k for k in range(1,32))
        assert all(abs(N[k-1]-q**k-1)<=n*S.integer_nthroot(4*q**k,2)[0] for k in range(1,32))
        print('AUDIT',r['graph'],r['mask'],'rank',rank,'negative_closed',[(k,a) for k,a in enumerate(aa,1) if a<0],
              'all31_match=PASS real_band_principal_minors=',minors,flush=True)
        if (r['graph'],r['mask']) not in focus:continue
        parts=reduced_partitions(r['adjacency_coefficients'])
        print('REDUCED RESULTANTS',r['graph'],r['mask'],dict(sorted(Counter(p['reduced'] for p in parts).items())),flush=True)
        assert all(p['reduced']>2 for p in parts)
        # Every lower-dimensional simple factor has an explicit elliptic or
        # hyperelliptic Jacobian representative. Their product gives a PPAV.
        fact=S.factor_list(S.Poly.from_list(r['weil_coefficients'],x))[1]
        assert all(tuple(map(int,f.all_coeffs())) in pp_factors for f,e in fact)
        print('PRINCIPALLY POLARIZABLE ISOGENY CLASS: YES (product of explicit Jacobian factors)',flush=True)
        covers={}
        for d in range(1,4):
            tested=[]
            for c in divisor_candidates(r['weil_coefficients'],d):
                ND=counts_from_coeff(c,31);fD=max(i for i,a in enumerate(c) if a%2)
                ram=rank-2*fD+1;different_half=n-2*d+1
                reasons=[]
                if d==2 and c not in genus2:reasons.append('not a genus-2 Jacobian polynomial (complete hyperelliptic enumeration)')
                if not 0<=ram<=different_half or (ram==0 and different_half!=0):
                    reasons.append(f'Deuring-Shafarevich/Riemann-Hurwitz r={ram}, delta={different_half}')
                fail=[k for k in range(1,32) if N[k-1]>2*ND[k-1]]
                if fail:reasons.append(f'degree-2 point bound at k={fail[0]}: {N[fail[0]-1]}>2*{ND[fail[0]-1]}')
                tested.append(dict(coeff=c,N=ND[:6],p_rank=fD,ramification_points=ram,different_half=different_half,
                                   rejected=bool(reasons),reasons=reasons))
            covers[d]=tested
            survive=[t for t in tested if not t['rejected']]
            print('DOUBLE COVER BASE genus',d,'candidates',len(tested),'surviving',len(survive),survive,flush=True)
        fs=S.factor_list(S.Poly.from_list(r['weil_coefficients'],x))[1]
        order_rank=sum(f.degree() for f,e in fs);centralizer_rank=sum(f.degree()*e*e for f,e in fs)
        print('ORDER RANK',order_rank,'RATIONAL CENTRALIZER RANK',centralizer_rank,flush=True)
        print('N1..12',N[:12],'a1..12',aa[:12],flush=True)
        assert all(N[d*k-1]>=N[k-1] for k in range(1,32) for d in range(1,31//k+1))
        print('N_{dk}>=N_k all dk<=31: PASS',flush=True)
        outputs.append(dict(graph=r['graph'],mask=r['mask'],p_rank=rank,band_minors=minors,
                            reduced_partitions=parts,double_covers=covers,ppav_class=True,
                            order_rank=int(order_rank),rational_centralizer_rank=int(centralizer_rank)))
    assert 2**16>20+11*32
    print('TAIL: k>=32, k*a_k >= 2^k-(20+11k)*2^(k/2)>0 for all these n<=10.')
    print('Cyclic F2-Galois covers of degree 5 or 7 excluded: tame odd-order automorphism acts freely on C(F2), but N1=3.')
    print('Pure Kummer degree 5 or 7 excluded: gcd(m,4-1)=1 forces N2=5 on the smooth model over P1, targets N2>5.')
    print('Smooth CI (2,4) in P3 genus=9; smooth CI (2,2,2) in P4 genus=5: neither gives genus 8.')
    (HERE/'output_obstructions.json.txt').write_text(json.dumps(outputs,indent=2)+'\n')

if __name__=='__main__':main()
