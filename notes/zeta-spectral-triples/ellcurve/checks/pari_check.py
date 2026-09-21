#!/usr/bin/env python3
"""PARI references and independent affine counts; writes only in checks/."""
import json
from pathlib import Path
from cypari2 import Pari

CURVES = {
    '11a1': ([0,-1,1,-10,-20],11),
    '14a1': ([1,0,1,4,-6],14),
    '37a1': ([0,0,1,-1,0],37),
    '389a1': ([0,1,1,-2,0],389),
}

def count(a,p):
    a1,a2,a3,a4,a6=a
    affine=sum((y*y+a1*x*y+a3*y-x*x*x-a2*x*x-a4*x-a6)%p==0
               for x in range(p) for y in range(p))
    return p-affine

def main():
    p=Pari(); p.set_real_precision(85)
    print('PARI version:',p('version()'))
    print('precision decimal:',p.get_real_precision(),'; lfunzeros precision=288 bits (explicit cypari2 argument)')
    out={'version':str(p('version()')),'digits':p.get_real_precision(),'curves':{}}
    for name,(a,conductor) in CURVES.items():
        E=p.ellinit(a); red=p.ellglobalred(E)
        primes=[q for q in range(2,101) if p.isprime(q)]
        if conductor not in primes and p.isprime(conductor): primes.append(conductor)
        aps={str(q):int(p.ellap(E,q)) for q in primes}
        errors=[(q,count(a,q),aps[str(q)]) for q in primes if count(a,q)!=aps[str(q)]]
        print(name,'model=',a,'conductor=',red[0],'rootno=',p.ellrootno(E),flush=True)
        print('a_p for p=2,3,5,7,11,13:',[aps[str(q)] for q in [2,3,5,7,11,13]])
        print('affine+infinity vs ellap, primes<=100 plus large bad prime:',errors or 'PASS')
        for q in [2,3]+[q for q in primes if conductor%q==0]:
            print('count detail p=',q,'#projective=',q+1-count(a,q),'ap=',aps[str(q)],'localred=',p.elllocalred(E,q))
        assert not errors
        L=p.lfuncreate(E)
        zeros=[str(z) for z in p.lfunzeros(L,20,precision=288)]
        rank=int(p.lfunorderzero(L))
        print('lfunorderzero=',rank,'lfunzeros(lfuncreate(E),20)=',zeros,flush=True)
        out['curves'][name]={'model':a,'conductor':int(red[0]),'rootno':int(p.ellrootno(E)),
                              'rank':rank,'aps':aps,'zeros':zeros}
    # The four requested curves have no additive prime and no bad reduction at 3.
    for a in [[0,0,0,-1,0],[0,0,0,0,1]]:
        E=p.ellinit(a)
        print('supplemental small-characteristic model=',a,'conductor=',p.ellglobalred(E)[0])
        for q in [2,3]:
            ap=int(p.ellap(E,q)); got=count(a,q)
            print('p=',q,'affine+infinity=',q+1-got,'ap=',ap,'localred=',p.elllocalred(E,q),'PASS' if ap==got else 'FAIL')
            assert ap==got
    Path(__file__).with_name('pari_refs.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__': main()
