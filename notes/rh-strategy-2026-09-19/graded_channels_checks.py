#!/usr/bin/env python3
"""Deterministic finite checks for the 2026-09-19 graded-channel strategy lane.
Purely local: no network and no input zero ordinates. These checks support,
not replace, the proofs in graded-channels.md.
"""
import json
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(20260919)
records = []

def check(name, error, tol=2e-10):
    error = float(error)
    assert error < tol, (name, error)
    records.append({"name": name, "error": error})

def dissipator(rs, x):
    ans = np.zeros_like(x, dtype=complex)
    for r in rs:
        k = r.conj().T @ r
        ans += r @ x @ r.conj().T - (k @ x + x @ k)/2
    return ans

# Paired nonnormal jumps make the total dissipator unital, checking the
# commutator identity beyond Hermitian or individually normal jumps.
for dplus, dminus in [(1,1), (1,2), (2,2), (2,3)]:
    d = dplus+dminus
    p = np.diag([1]*dplus+[-1]*dminus)
    rs = []
    for sign in [1,-1]:
        r = rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        r = (r+sign*p@r@p)/2
        rs += [r, r.conj().T]
    check(f"unital_{dplus}_{dminus}", np.linalg.norm(dissipator(rs,np.eye(d,dtype=complex))))
    for trial in range(5):
        x = rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        x = (x-p@x@p)/2
        lhs = -np.vdot(x,dissipator(rs,x)).real
        rhs = sum(np.linalg.norm(r.conj().T@x-x@r.conj().T)**2 for r in rs)/2
        check(f"Dirichlet_identity_{dplus}_{dminus}_{trial}", abs(lhs-rhs))
    # Linear commutant equations for ALL complex odd matrix units.
    eqs=[]
    for i in range(d):
        for j in range(d):
            if p[i,i] != p[j,j]:
                e = np.zeros((d,d),complex); e[i,j]=1
                eqs.append(np.kron(e.T,np.eye(d))-np.kron(np.eye(d),e))
    rank = np.linalg.matrix_rank(np.vstack(eqs),tol=1e-9)
    assert d*d-rank == 1
    records.append({"name":f"odd_commutant_dimension_{dplus}_{dminus}","value":int(d*d-rank)})

# Constructive alternative: distribute the damping budget across X/Y jumps.
i2=np.eye(2,dtype=complex)
x=np.array([[0,1],[1,0]],complex)
y=np.array([[0,-1j],[1j,0]],complex)
z=np.diag([1,-1]).astype(complex)
g=1/8
omega=np.sqrt(2)  # Arbitrary algebraic frequency, not a fitted zeta ordinate.
h=omega*z/2
rs=[np.sqrt(g)*x,np.sqrt(g)*y]
def generator(a):
    return -1j*(h@a-a@h)+dissipator(rs,a)
basis=[i2,z,x,y]
mat=np.array([[np.vdot(b,generator(a))/2 for a in basis] for b in basis])
check("balanced_qubit_even_block",np.linalg.norm(mat[:2,:2]-np.diag([0,-.5])))
odd=mat[2:,2:]
check("balanced_qubit_odd_hermitian_part",np.linalg.norm((odd+odd.conj().T)/2+.25*np.eye(2)))
check("balanced_qubit_stationary_density",np.linalg.norm(generator(i2/2)))
assert np.count_nonzero(np.abs(np.linalg.eigvals(mat))<1e-10)==1
for t in [.1,.5,1.,2.,5.]:
    a=expm(t*mat)
    supertrace=np.trace(a[:2,:2])-np.trace(a[2:,2:])
    expected=abs(1-np.exp((-.25+1j*omega)*t))**2
    check(f"balanced_qubit_supertrace_{t}",abs(supertrace-expected))
# This toy is finite-norm cMPS data but violates finite kinetic-energy CAR
# regularity; record the defect, do not silently upgrade it to a regular cMPS.
kinetic_defect=np.linalg.norm(rs[0]@rs[0])
assert kinetic_defect > 0
records.append({"name":"kinetic_regularity_defect_Rx_squared", "value":float(kinetic_defect)})

# Approaching a Hashimoto endpoint: positive metrics can degenerate.
endpoint=[]
for n in [10,100,1000,10000]:
    s=2-1/n
    c=np.array([[s,1],[-1,0.]])
    metric=np.array([[1,s/2],[s/2,1.]])
    check(f"companion_metric_identity_{n}",np.linalg.norm(c.T@metric@c-metric))
    endpoint.append({"n":n,"lambda_min":float(np.linalg.eigvalsh(metric)[0]),"condition_number":float(np.linalg.cond(metric))})
limit=np.array([[2.,1],[-1,0]])
check("endpoint_nonzero_nilpotent_squared",np.linalg.norm((limit-np.eye(2))@(limit-np.eye(2))))
assert np.linalg.norm(limit-np.eye(2))>0
print(json.dumps({"status":"PASS","checks":len(records),"records":records,"endpoint_metrics":endpoint},indent=2))
