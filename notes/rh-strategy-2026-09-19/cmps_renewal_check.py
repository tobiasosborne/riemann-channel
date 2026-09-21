"""Offline finite renewal/cMPS checks. Synthetic parameters; no zeta zeros."""
import json
import os
from pathlib import Path
import numpy as np


def supermatrix(action, n):
    columns = []
    for k in range(n*n):
        x = np.zeros(n*n, dtype=complex)
        x[k] = 1
        columns.append(action(x.reshape((n, n), order="F")).reshape(-1, order="F"))
    return np.column_stack(columns)


def spectrum(matrix):
    return sorted([[float(z.real), float(z.imag)] for z in np.linalg.eigvals(matrix)])


H = np.array([[0, 1], [1, 0]], dtype=complex)
E = np.diag([1., 0.])
B = -1j*H-E/2
assert np.max(np.linalg.eigvals(B).real) < 0
A = supermatrix(lambda x: B@x+x@B.conj().T, 2)
records = []
for omega in (np.eye(2)/2, E):
    W = np.linalg.solve(A, -omega.reshape(-1, order="F")).reshape((2,2), order="F")
    sigma = W/np.trace(W)
    r = np.trace(E@sigma).real
    M = -(B@sigma+sigma@B.conj().T)
    L = A+supermatrix(lambda x: omega*np.trace(E@x), 2)
    eig_w, vec_w = np.linalg.eigh(omega)
    eig_e, vec_e = np.linalg.eigh(E)
    jumps = [np.sqrt(w*e)*np.outer(v, u.conj())
             for w, v in zip(eig_w, vec_w.T)
             for e, u in zip(eig_e, vec_e.T) if w*e > 0]
    gauge = B+B.conj().T+sum(R.conj().T@R for R in jumps)
    reset = sum(supermatrix(lambda x, R=R: R@x@R.conj().T, 2) for R in jumps)
    residuals = {
        "stationarity": float(np.linalg.norm(L@sigma.reshape(-1,order="F"))),
        "inverse_reset": float(np.linalg.norm(M/r-omega)),
        "canonical_gauge": float(np.linalg.norm(gauge)),
        "kraus_reset": float(np.linalg.norm(A+reset-L)),
        "renewal_flux": float(abs(np.trace(E@W)-1))}
    assert max(residuals.values()) < 1e-12
    assert np.min(np.linalg.eigvalsh(sigma)) > 0
    assert np.count_nonzero(abs(np.linalg.eigvals(L)) < 1e-10) == 1
    records.append({"reset_eigenvalues": eig_w.tolist(),
                    "stationary_eigenvalues": np.linalg.eigvalsh(sigma).tolist(),
                    "nojump_spectrum": spectrum(B), "transfer_spectrum": spectrum(L),
                    "residuals": residuals})

# Exact determinant: for sigma=diag(p,1-p), det M=-(1-2p)^2.
obstructions = []
for p in (.2, .5, .8):
    sigma = np.diag([p, 1-p])
    M = -(B@sigma+sigma@B.conj().T)
    assert abs(np.linalg.det(M)+(1-2*p)**2) < 1e-12
    obstructions.append({"p": p, "M_eigenvalues": np.linalg.eigvalsh(M).tolist(),
                         "reset_feasible": bool(np.linalg.eigvalsh(M).min() > -1e-12)})

result = {"status": "PASS", "model": "H=X, E=diag(1,0), B=-iH-E/2",
          "renewal_examples": records, "biased_diagonal_targets": obstructions,
          "scope": "Finite cMPS reset feasibility; no arithmetic or RH inference"}
path = Path(__file__).with_suffix(".json")
temporary = path.with_suffix(".json.partial")
with temporary.open("w") as f:
    json.dump(result, f, indent=2)
    f.write("\n")
    f.flush()
    os.fsync(f.fileno())
os.replace(temporary, path)
print(json.dumps(result, indent=2))
