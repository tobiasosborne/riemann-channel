#!/usr/bin/env python3
"""Algebraic/numerical diagnostics for cusp-bridge.md; no zero-location oracle.
Synthetic on/off-line parameters test identities, not the Riemann hypothesis.
"""
import json
from pathlib import Path
import numpy as np

def audit_case(name, poles):
    s = np.asarray(poles, dtype=complex)
    n = len(s)
    K = 1 / (1 - s.conj()[:, None] - s[None, :])
    A = np.diag(s - 1)
    C = A + 0.5 * np.eye(n)
    R = A + 0.75 * np.eye(n)
    ones = np.ones((n, n))
    identity_err = np.linalg.norm(A.conj().T @ K + K @ A + K + ones)
    exit_err = np.linalg.norm(C.conj().T @ K + K @ C + ones)
    center_err = np.linalg.norm(R.conj().T @ K + K @ R - (0.5 * K - ones))
    # Lower-Hardy kernels tau_i = i conj(C_i): <k_i,k_j>=i/(conj(tau_j)-tau_i).
    tau = 1j * np.conj(np.diag(C))
    hardy_K = 1j / (tau.conj()[None, :] - tau[:, None])
    hardy_err = np.linalg.norm(K - hardy_K)
    # Reindexed rho' = 1-conj(rho) realizes C_i=-conj(rho'_i)/2.
    rho_prime = 1 - np.conj(2 * s)
    affine_err = np.max(np.abs(np.diag(C) + np.conj(rho_prime) / 2))
    Y = 11.0
    coeff = np.array([complex(1+i, 0.2*i) for i in range(n)])
    scale = coeff * Y ** (0.5-s)
    gram_Y = scale.conj()[:,None] * K * scale[None,:]
    normalized = gram_Y / (scale.conj()[:,None] * scale[None,:])
    normalization_err = np.linalg.norm(normalized-K)
    centered_defect = R.conj().T @ K + K @ R
    positive_eigenvalues, eigvecs = np.linalg.eigh(K)
    Rroot = (eigvecs * np.sqrt(positive_eigenvalues)) @ eigvecs.conj().T
    Rinv = (eigvecs / np.sqrt(positive_eigenvalues)) @ eigvecs.conj().T
    B = Rroot @ C @ Rinv
    j = np.ones((1,n)) @ Rinv
    H = 0.5j * (B-B.conj().T)
    Q = np.zeros((n+1,n+1), complex)
    Q[1:,1:] = B
    L = np.zeros_like(Q)
    L[0,1:] = j
    gauge_err = np.linalg.norm(Q+Q.conj().T+L.conj().T@L)
    hamiltonian_err = np.linalg.norm(B+1j*H+0.5*j.conj().T@j)
    assert max(gauge_err, hamiltonian_err) < 1e-11
    nonnormality = np.linalg.norm(B.conj().T@B-B@B.conj().T)
    assert min(positive_eigenvalues) > 0
    assert max(identity_err, exit_err, center_err, hardy_err, affine_err, normalization_err) < 1e-11
    if n >= 2:
        assert np.linalg.norm(centered_defect) > 1e-4
    return dict(case=name, parameters=[[z.real,z.imag] for z in s],
                gram_eigenvalues=positive_eigenvalues.tolist(),
                lyapunov_residual=float(identity_err), exit_residual=float(exit_err),
                centered_identity_residual=float(center_err),
                hardy_gram_residual=float(hardy_err), affine_residual=float(affine_err),
                truncation_normalization_residual=float(normalization_err),
                centered_defect_norm=float(np.linalg.norm(centered_defect)),
                cmps_gauge_residual=float(gauge_err),
                hamiltonian_exit_residual=float(hamiltonian_err),
                nonnormality=float(nonnormality))

def main():
    rows = [audit_case('on_line', [.25+1j, .25+2j, .25+3j]),
            audit_case('off_line_FE_pair', [.15+1j, .35+1j, .25+2j]),
            audit_case('one_on_line', [.25+1j]),
            audit_case('one_off_line', [.15+1j])]
    beta, gamma, t = .5, 14.0, 1.0
    lam = gamma/2 - 1j*beta/2
    wrong = np.exp(-1j*t*np.conj(lam))
    correct = np.exp(1j*t*np.conj(lam))
    assert abs(wrong) > 1 and abs(correct) < 1
    result = {'status':'all assertions passed', 'interpretation':'synthetic finite diagnostics; no RH evidence',
              'cases':rows, 'old_formula_modulus':float(abs(wrong)),
              'correct_formula_modulus':float(abs(correct))}
    out = Path(__file__).with_name('cusp_bridge_diagnostic.json')
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__': main()
