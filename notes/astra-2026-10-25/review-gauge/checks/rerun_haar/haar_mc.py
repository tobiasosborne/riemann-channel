#!/usr/bin/env python3
"""Reproducible Monte Carlo, coefficient SEs and correlated root uncertainty.

Run python3 checks/haar_mc.py --samples 100000 (default); up to 1000000 supported.
The Gaussian coefficient bootstrap uses the full covariance of the sample mean.
Its 95% root coordinate intervals are statistical approximations, NOT certified
root enclosures, simultaneous confidence regions, or a proof of real-rootedness.
"""
import argparse
import time
import json
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.optimize import linear_sum_assignment
from haar_common import graph, tree_edges, quaternion_matrices, spin_one, batch_adjacency, eigen_polynomials, matching_d, su2_average

def haar_blocks(rng,batch,g,kind):
    if kind.startswith('SU2'):
        a=rng.normal(size=(batch,g,4));a/=np.linalg.norm(a,axis=-1)[...,None]
        return spin_one(a) if kind=='SU2-spin1' else quaternion_matrices(a)
    d=int(kind[-1]);z=rng.normal(size=(batch,g,d,d))+1j*rng.normal(size=(batch,g,d,d))
    q,r=np.linalg.qr(z);di=np.diagonal(r,axis1=-2,axis2=-1);phase=di/np.abs(di)
    return q*phase[...,None,:]

def run(name,kind,samples,batch,seed,boot):
    rng=np.random.default_rng(seed);G=graph(name);g=len(tree_edges(G)[1]);d=3 if kind in ['U3','SU2-spin1'] else 2;N=len(G)*d
    avg=np.zeros(N+1,dtype=np.longdouble);m2=np.zeros((N+1,N+1),dtype=np.longdouble);count=0;t0=time.monotonic()
    for start in range(0,samples,batch):
        b=min(batch,samples-start);A=batch_adjacency(G,haar_blocks(rng,b,g,kind))
        ev=np.linalg.eigvalsh(A);c=eigen_polynomials(ev)
        # Known deterministic coefficients and centre symmetry as exact control variates.
        c[:,0]=1;c[:,1]=0;c[:,2]=-G.number_of_edges()*d
        if kind!='SU2-spin1': c[:,1::2]=0
        bm=c.mean(axis=0);centered=c-bm;delta=bm-avg
        m2+=centered.T@centered+np.outer(delta,delta)*(count*b/(count+b))
        avg+=delta*(b/(count+b));count+=b
    mean=np.asarray(avg,float)
    cov=np.asarray(m2/(samples*(samples-1)),float)
    cov=(cov+cov.T)/2
    se=np.sqrt(np.maximum(np.diag(cov),0))
    print(f'\n{name} {kind}: samples={samples} seed={seed} elapsed={time.monotonic()-t0:.2f}s',flush=True)
    print('coefficients descending powers; SE is pointwise sample-mean SE')
    for j,(v,err) in enumerate(zip(mean,se)):print(f'x^{N-j:2d} {v:.12g} SE {err:.12g}')
    exact=None
    for filename in ['output_finite.json','output_limit.json']:
        path=Path(__file__).with_name(filename)
        if path.exists():
            coefficients=json.loads(path.read_text()).get(name,{}).get(kind)
            if coefficients is not None:exact=np.array([float(Fraction(c)) for c in coefficients])
    if exact is None:
        target=None
        if kind=='SU2-half':target=su2_average(G)[0]
        elif kind in ['U2','U3'] and (d==2 or name=='K4'):target=matching_d(G,d)
        if target is not None:exact=np.asarray(target.all_coeffs(),float)
    if exact is not None:
        mask=se>1e-10
        print('max absolute standardized coefficient deviation from exact:',np.max(np.abs(mean-exact)[mask]/se[mask]))
    roots=np.roots(mean);order=np.lexsort((roots.imag,roots.real));roots=roots[order]
    # Scale covariance before diagonalization to avoid losing small coefficient directions.
    scale=np.maximum(se,1e-25);corr=cov/np.outer(scale,scale)
    vals,vecs=np.linalg.eigh(corr);L=(vecs*np.sqrt(np.maximum(vals,0)))*scale[:,None]
    draws=[]
    for _ in range(boot):
        coeff=mean+L@rng.normal(size=N+1);r=np.roots(coeff)
        ri,ci=linear_sum_assignment(np.abs(roots[:,None]-r[None,:]));aligned=np.empty(N,complex);aligned[ri]=r[ci]
        draws.append(aligned)
    draws=np.asarray(draws)
    print(f'Roots of estimated polynomial with {boot}-draw correlated Gaussian bootstrap 95% coordinate intervals:')
    for j,r in enumerate(roots):
        re=np.quantile(draws[:,j].real,[.025,.975]);im=np.quantile(draws[:,j].imag,[.025,.975])
        print(f'{r.real:.12f}{r.imag:+.12f}i Re95=[{re[0]:.12f},{re[1]:.12f}] Im95=[{im[0]:.12f},{im[1]:.12f}]')
    print('ESTIMATE only: max |Im root| =',float(np.max(np.abs(roots.imag))),'; max |Re root| =',float(np.max(np.abs(roots.real))),'; band =',2*np.sqrt(2))
    print('Uncertainty excludes floating-point error; coefficients accumulated in long double after double-precision Hermitian eigensolves. Root intervals may be unreliable near collisions.')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--samples',type=int,default=100000);ap.add_argument('--batch',type=int,default=1000);ap.add_argument('--bootstrap',type=int,default=500)
    ap.add_argument('--graphs',nargs='+',default=['K4','Petersen']);ap.add_argument('--groups',nargs='+',default=['U2','SU2-half','SU2-spin1','U3']);args=ap.parse_args()
    print('NUMERICAL, NOT A PROOF. All random seeds fixed. Odd coefficients removed only when exact centre symmetry justifies it.',flush=True)
    for i,name in enumerate(args.graphs):
        for j,kind in enumerate(args.groups):run(name,kind,args.samples,args.batch,20261023+101*i+j,args.bootstrap)

if __name__=='__main__':main()
