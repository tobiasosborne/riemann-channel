#!/usr/bin/env python3
"""Fresh raw-model enumeration and BFS under group generators, not minshift.
Smoothness uses FLINT polynomial gcd; points use explicit (x,y) enumeration.
"""
from pathlib import Path
from collections import Counter
import json
from flint import nmod_poly
from review_k4 import field

HERE=Path(__file__).resolve().parent

def poly(code,length):return nmod_poly([(code>>i)&1 for i in range(length)],2)

def translate(code):
    ans=0
    for i in range(code.bit_length()):
        if code>>i&1:
            for j in range(i+1):
                if j&i==j:ans^=1<<j
    return ans

def reverse(code,degree):return sum(((code>>i)&1)<<(degree-i) for i in range(degree+1))

def main():
    fs=[poly(i,11) for i in range(2048)]
    df2=[f.derivative()**2 for f in fs]
    smooth=set()
    for h in range(1,64):
        H=poly(h,6);dh2=H.derivative()**2
        for f in range(2048):
            if not(h>>5&1) and not(((f>>9)&1)^(((h>>4)&1)*((f>>10)&1))):continue
            if H.gcd(df2[f]+dh2*fs[f]).degree()==0:smooth.add((h,f))
    raw=len(smooth);remaining=set(smooth);models=[];sizes=[]
    th=[translate(i) for i in range(64)];tf=[translate(i) for i in range(2048)]
    rh=[reverse(i,5) for i in range(64)];rf=[reverse(i,10) for i in range(2048)]
    while remaining:
        seed=min(remaining);remaining.remove(seed);orbit={seed};todo=[seed]
        while todo:
            h,f=todo.pop()
            neighbors=[(h,f^(1<<(2*j))^(h<<j)) for j in range(6)]
            neighbors += [(th[h],tf[f]),(rh[h],rf[f])]
            for v in neighbors:
                assert v in smooth
                if v not in orbit:orbit.add(v);remaining.remove(v);todo.append(v)
        models.append(seed);sizes.append(len(orbit))
    hist=Counter();N1=Counter();N2=Counter();records=[]
    fields=[field(k)[1] for k in range(1,5)]
    for h,f in models:
        Ns=[]
        for m in fields:
            q=len(m)
            def ev(c,x):
                r=0
                for i in range(c.bit_length()-1,-1,-1):r=int(m[r,x])^((c>>i)&1)
                return r
            N=0
            for x in range(q):
                H=ev(h,x);F=ev(f,x)
                N+=sum((int(m[y,y])^int(m[H,y]))==F for y in range(q))
            N+=sum((int(m[y,y])^int(m[(h>>5)&1,y]))==((f>>10)&1) for y in range(q))
            Ns.append(N)
        # Coefficients from k c_k = sum (N_i-q^i-1)c_{k-i}.
        c=[1]
        for k in range(1,5):
            num=sum((Ns[i-1]-2**i-1)*c[k-i] for i in range(1,k+1));assert num%k==0;c.append(num//k)
        c += [2**(k-4)*c[8-k] for k in range(5,9)]
        hist[tuple(c)]+=1;N1[Ns[0]]+=1;N2[Ns[1]]+=1
        records.append(dict(h=h,f=f,N=Ns,L=c))
    target=(1,0,2,0,5,0,8,0,16)
    print('raw_smooth_equations='+str(raw)+' y_shift_classes='+str(raw//32)+' full_isomorphism_classes='+str(len(models)))
    print('orbit_size_histogram='+str(sorted(Counter(sizes).items())))
    print('distinct_L_polynomials='+str(len(hist))+' K4_matches='+str(hist[target]))
    print('N1_histogram='+str(sorted(N1.items()))+' N2_histogram='+str(sorted(N2.items())))
    source=HERE.parents[2]/'astra-2026-10-23'/'jacobian'/'checks'/'output_hyperelliptic.json.txt'
    old=json.loads(source.read_text())
    assert records==old
    print('All 264 canonical representatives, point counts and L-polynomials equal original JSON: PASS')
    (HERE/'output_independent_hyperelliptic_f2.json.txt').write_text(json.dumps(records,indent=2)+'\n')

if __name__=='__main__':main()
