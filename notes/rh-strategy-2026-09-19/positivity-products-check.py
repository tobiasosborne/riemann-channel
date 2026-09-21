#!/usr/bin/env python3
"""Offline reproducible diagnostics; numerical outputs are NOT interval certificates.

Primary formula: refs/src/2206.03682/screwz_15.tex, Eq_101.
No zero tables and no network are used. Output checkpoints after each grid.
Run from any working directory: python3 /path/to/this/file.py
"""
from fractions import Fraction
from pathlib import Path
import json
import time
import mpmath as mp

OUT = Path(__file__).with_name('positivity-products-check.json')
results = {'status': 'running', 'started_unix': time.time(), 'mpmath_version': mp.__version__,
           'qualification': 'High precision numerical checks, not rigorous interval certificates.',
           'exact_checks': [], 'grids': []}

def checkpoint():
    temp = OUT.with_suffix('.json.tmp')
    temp.write_text(json.dumps(results, indent=2) + '\n')
    temp.replace(OUT)

def hinge(t, a):
    return max(abs(t)-a, 0)

# Exact rational checks of the hinge algebra; w is a positive scalar.
a, A, w = Fraction(3), Fraction(2), Fraction(5, 7)
d = w*(2*A-a)
assert -w*(hinge(A,a)+hinge(A,a)-hinge(0,a)) == 0
assert -w*(hinge(A,a)+hinge(-A,a)-hinge(2*A,a)) == d
results['exact_checks'].append({'name': 'prime_atom_indefinite', 'eigenvalues': [str(d), str(-d)]})
for h, a in [(Fraction(1,4), Fraction(17,20)), (Fraction(1,3), Fraction(2))]:
    L = int(a//h)
    theta = a/h-L
    for m in range(-12,13):
        got = hinge((m+1)*h,a)+hinge((m-1)*h,a)-2*hinge(m*h,a)
        wanted = h*((1-theta)*(abs(m)==L)+theta*(abs(m)==L+1))
        assert got == wanted, (h,a,m,got,wanted)
results['exact_checks'].append({'name': 'sparse_second_difference', 'cases': 50, 'passed': True})
checkpoint()

def prime_powers(cutoff):
    sieve = bytearray(b'\1')*(cutoff+1)
    sieve[0:2] = b'\0\0'
    for p in range(2,int(cutoff**.5)+1):
        if sieve[p]:
            sieve[p*p:cutoff+1:p] = b'\0'*len(range(p*p,cutoff+1,p))
    answer=[]
    for p in range(2,cutoff+1):
        if sieve[p]:
            n=p
            while n<=cutoff:
                answer.append((n,p)); n*=p
    return sorted(answer)

for digits in [40,70]:
    mp.mp.dps=digits
    for half_count in [8,16]:
        h=mp.mpf(1)/4
        cutoff=int(mp.ceil(mp.exp(2*half_count*h)))
        pp=[(mp.log(n),mp.log(p)/mp.sqrt(n)) for n,p in prime_powers(cutoff)]
        psi0=mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi)
        C=mp.pi**2+8*mp.catalan
        vals=[mp.mpf(0)]
        for j in range(1,2*half_count+1):
            t=j*h
            prime=mp.fsum(w*(t-a) for a,w in pp if a<=t)
            # A direct absolutely convergent Lerch series, t >= 1/4.
            z=mp.exp(-2*t); zpow=mp.mpf(1); lerch=mp.mpf(0); k=0
            while True:
                term=zpow/(k+mp.mpf(1)/4)**2
                lerch+=term
                if term < mp.eps: break
                zpow*=z; k+=1
            vals.append(4*(mp.exp(t/2)+mp.exp(-t/2)-2)-prime+t*psi0/2+(C-mp.exp(-t/2)*lerch)/4)
        idx=[j for j in range(-half_count,half_count+1) if j]
        K=mp.matrix([[vals[abs(i)]+vals[abs(j)]-vals[abs(i-j)] for j in idx] for i in idx])
        cij=lambda m: vals[abs(m+1)]+vals[abs(m-1)]-2*vals[abs(m)]
        T=mp.matrix([[cij(i-j) for j in range(2*half_count)] for i in range(2*half_count)])
        # K=B*T*B.T where B sums increments from origin, oriented negatively on left.
        B=mp.matrix(2*half_count)
        for row,j in enumerate(idx):
            if j>0:
                for l in range(0,j): B[row,l+half_count]=1
            else:
                for l in range(j,0): B[row,l+half_count]=-1
        residual=mp.norm(K-B*T*B.T,mp.inf)
        kvals=mp.eigsy(K,eigvals_only=True)
        tvals=mp.eigsy(T,eigvals_only=True)
        # Schur pivot for adding the last (rightmost) node in this fixed order.
        prev=K[:-1,:-1]; col=K[:-1,-1]
        # Explicit slicing avoids mpmath's negative-index column interpretation.
        col=mp.matrix([K[i,K.cols-1] for i in range(K.rows-1)])
        pivot=K[K.rows-1,K.cols-1]-(col.T*mp.lu_solve(prev,col))[0]
        entry={'digits':digits,'h':'0.25','A':str(half_count*h),'nodes':len(idx),
               'prime_integer_cutoff':cutoff,'prime_powers':len(pp),
               'psi_1':mp.nstr(vals[4],32),'psi_2':mp.nstr(vals[8],32),
               'kernel_min_eigenvalue':mp.nstr(kvals[0],32),
               'increments_min_eigenvalue':mp.nstr(tvals[0],32),
               'congruence_max_row_sum_residual':mp.nstr(residual,8),
               'last_schur_pivot':mp.nstr(pivot,32)}
        results['grids'].append(entry); checkpoint()
        print(json.dumps(entry),flush=True)
results['status']='complete'; results['finished_unix']=time.time(); checkpoint()
