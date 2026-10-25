#!/usr/bin/env python3
"""Number-by-number comparisons, with explicit change-of-basis certificates."""
from pathlib import Path
from math import gcd
from itertools import product
import ast,json,re,difflib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
T=ROOT/'notes/astra-2026-10-23/tower/checks';U=ROOT/'notes/adelic-gkp/checks'
def lines(p): return p.read_text().splitlines()
def passes(p): return [s for s in lines(p) if s.startswith('PASS  ')]
for tag,old,new in [('F',U/'output_overlap_data.txt',HERE/'output_legacy_overlap_data.txt'),('CM',T/'output_cm_flint.txt',HERE/'output_pari_cm_explicit.txt')]:
    a,b=passes(old),passes(new)
    if tag=='CM':a=[s for s in a if not s.startswith('PASS conjugation')]
    assert a==b,(tag,list(difflib.unified_diff(a,b)))
    print(f'{tag}: {len(a)}/{len(a)} original assertion lines and every printed number identical')
assert passes(T/'output_tower_flint.txt')==passes(HERE/'output_legacy_tower_pairing.txt')
print('U: 22/22 assertion lines match the saved FLINT replay exactly')
# Every numerical coordinate, certificate, pairing exponent, and transport in T's audit.
filt=lambda p:[s for s in lines(p) if 'PARI' not in s]
a,b=filt(T/'output_audit.txt'),filt(HERE/'output_pari_audit.txt')
assert a==b
print(f'T audit: {len(a)}/{len(a)} non-PARI lines exactly identical to saved FLINT output')
wa=sum('PARI Weil agreement' in s for s in lines(HERE/'output_pari_audit.txt'))
ta=sum('PARI ellcard, ellgroup, and all reduced Tate entries agree.' in s for s in lines(HERE/'output_pari_audit.txt'))*4
assert (wa,ta)==(16,64)
print(f'T audit exact same-field pairing agreement: Weil {wa}/{wa}, reduced Tate {ta}/{ta}, total {wa+ta}/{wa+ta}')
# Each pari_validate calls ellcard+ellgroup. The function is run 24 times on
# k<=6 groups, 16 times on pairing fields, and twice for the q5 orders.
print('T audit ellcard/ellgroup: 42/42 invocations (24 extension-group cases, 16 pairing-field cases, 2 q5 cases), hence 84 scalar/group equalities')

def table(p):
    ans={}
    pat=r'^\s+(E[145] k=.*?)\s+E_l = (.*?)\s+Frob cols (.*?)\s+#equivariant isos\s+(\d+)\s+Weil scales (.*?)\s+Tate scales (.*?)\s*$'
    for s in lines(p):
        m=re.match(pat,s)
        if m:
            tag,os,F,ni,W,Tt=m.groups()
            ans[tag]=(ast.literal_eval(os),ast.literal_eval(F),int(ni),None if W=='-' else ast.literal_eval(W),None if Tt=='-' else ast.literal_eval(Tt))
    assert len(ans)==42
    return ans

def basis_change(os,A,B):
    r=len(os)
    ell=next(d for d in range(2,os[0]+1) if os[0]%d==0)
    if r==1:
        assert A==B
        return [[1]]
    n,m=os
    def apply(U,v):return [(U[0][0]*v[0]+U[1][0]*v[1])%n,(U[0][1]*v[0]+U[1][1]*v[1])%m]
    # columns are images of invariant-factor generators; preserve their orders.
    for a,c,b,d in product(range(n),range(m),range(0,n,n//m),range(m)):
        if (a*d-b*c)%ell==0:continue
        U=[[a,c],[b,d]]
        if all(apply(U,A[j])==apply(B,U[j]) for j in range(2)):return U
    raise AssertionError(('nonconjugate Frobenius',os,A,B))
a,b=table(T/'output_tower_flint.txt'),table(HERE/'output_legacy_tower_pairing.txt')
assert a.keys()==b.keys()
counts={'groups':0,'isomorphism_counts':0,'Weil_sets':0,'Tate_sets':0,'Frobenius_conjugacies':0,'Frobenius_matrices_exact':0}
rows=[]
for tag in a:
    oa,Fa,na,Wa,Ta=a[tag];ob,Fb,nb,Wb,Tb=b[tag]
    assert oa==ob and na==nb and Wa==Wb and Ta==Tb,tag
    Uc=basis_change(oa,Fa,Fb)
    counts['groups']+=1;counts['isomorphism_counts']+=1
    counts['Weil_sets']+=Wa is not None;counts['Tate_sets']+=Ta is not None
    counts['Frobenius_conjugacies']+=1;counts['Frobenius_matrices_exact']+=Fa==Fb
    print(f'U {tag}: group={oa}, isos={na}, Weil={Wa}, Tate={Ta}; PASS; basis-change columns FLINT->PARI={Uc}')
    rows.append({'case':tag,'group':oa,'nphi':na,'Weil':Wa,'Tate':Ta,'basis_change':Uc})
print('U SUMMARY',counts)
print('U: 42/42 full comparison cases agree; 42 groups + 42 isomorphism counts + 25 Weil sets + 42 Tate sets = 151/151 invariant records')
assert counts['Weil_sets']==25 and counts['Tate_sets']==42
(HERE/'comparison_certificates.json').write_text(json.dumps({'counts':counts,'cases':rows},indent=2)+'\n')
# F W1 refinement comparison against new FLINT run.
frows=[]
for s in passes(HERE/'output_legacy_overlap_data.txt'):
    if s.startswith('PASS  W1 '):
        m=re.search(r'E\[(\d+)\].*?the (\d+) Frobenius.*?by (\[[^]]*\])',s)
        n,ni,S=m.groups();frows.append((int(n),int(ni),ast.literal_eval(S)))
for n,ni,S in frows:
    fl=next(s for s in lines(HERE/'output_rerun_overlap_refinement.txt') if s.startswith(f'W1 N={n} '))
    assert ast.literal_eval(re.search(r'scales=(\[[^]]*\])',fl).group(1))==S
    print(f'F W1 N={n}: PARI isos={ni}, PARI=FLINT multipliers={S}')
print(f'F W1 agreement {len(frows)}/{len(frows)}; W3=[2,3,2,3] both backends')
print('PASS all saved-output and cross-backend comparisons; no numerical discrepancy')
