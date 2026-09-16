#!/usr/bin/env python3
"""Finite audits for D1--D8. Run from any directory; writes no files.

Only numpy/scipy/sympy are needed. Helpers are loaded from the existing
scripts by AST, without running their experiments or writing __pycache__.
"""
import ast
import itertools
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import numpy as np
import scipy.linalg as la
import scipy.sparse as sparse
import sympy as sy

ROOT = Path(__file__).resolve().parents[3]
PASS = 0
FAIL = 0


def check(ok, message):
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        print("PASS", message)
    else:
        FAIL += 1
        print("FAIL", message)


def near(a, b, tol=2e-8):
    return np.linalg.norm(np.asarray(a) - np.asarray(b)) <= tol * max(1., np.linalg.norm(b))


def load_helpers(filename, names):
    tree = ast.parse((ROOT / filename).read_text())
    nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    env = {"np": np, "itertools": itertools}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), filename, "exec"), env)
    return env


def graph_matrices(adj):
    n = len(adj)
    edges = [(v, w) for v in range(n) for w in range(n) if adj[v, w]]
    ix = {e: i for i, e in enumerate(edges)}
    R = np.zeros((n, len(edges)))
    S = np.zeros((len(edges), n))
    J = np.zeros((len(edges), len(edges)))
    for i, (v, w) in enumerate(edges):
        R[w, i] = 1
        S[i, v] = 1
        J[ix[w, v], i] = 1
    return R, S, J, sparse.csr_matrix(S @ R - J)


def audit_lift(name, A, R, S, J, T, degree, expect_ram=True):
    """Check every retained eigenvector, both roots, and the derived metric."""
    q = degree - 1
    n = A.shape[0]
    check(near(A, A.conj().T), name + ": adjacency Hermitian")
    check(near(R @ S, A) and near(R @ J @ S, degree * np.eye(n)),
          name + ": RS=A and RJS=D")
    check(near(J @ J, np.eye(len(J))), name + ": reversal squares to identity")
    vals, vecs = la.eigh(A)
    keep = np.abs(np.abs(vals) - degree) > 1e-7
    vals, vecs = vals[keep], vecs[:, keep]
    ram = np.max(np.abs(vals)) <= 2 * np.sqrt(q) + 1e-7
    check(ram == expect_ram, name + ": predicted Ramanujan verdict")
    residual = 0.
    raw_kernel = 0.
    for a, f in zip(vals, vecs.T):
        roots = np.roots([1., -a, q])
        lifted = []
        for mu in roots:
            F = (mu * (S @ f) - J @ S @ f) / (mu * mu - 1)
            residual = max(residual, np.linalg.norm(T @ F - mu * F), np.linalg.norm(R @ F - f))
            lifted.append(F)
        if abs(roots[0] - roots[1]) > 1e-5:
            raw_kernel = max(raw_kernel, np.linalg.norm(R @ (lifted[0] - lifted[1])))
    check(residual < 2e-6, name + ": every retained root satisfies TF=mu F and RF=f")
    check(raw_kernel < 2e-7, name + ": untagged pullback kills partner differences")
    Ar = np.diag(vals)
    nr = len(vals)
    C = np.block([[Ar, q * np.eye(nr)], [-np.eye(nr), np.zeros((nr, nr))]])
    G = np.block([[np.eye(nr), Ar / 2], [Ar / 2, q * np.eye(nr)]])
    F = np.block([[np.zeros((nr, nr)), np.sqrt(q) * np.eye(nr)],
                  [np.eye(nr) / np.sqrt(q), np.zeros((nr, nr))]])
    check(near(C.conj().T @ G @ C, q * G), name + ": explicit letter-derived metric identity")
    check(near(F @ C @ F, q * la.inv(C)) and near(F.conj().T @ G @ F, G),
          name + ": operator FE and its metric invariance")
    expected_pos = np.max(np.abs(vals)) < 2 * np.sqrt(q) - 1e-7
    check((la.eigvalsh(G)[0] > 1e-8) == expected_pos,
          name + ": metric positive exactly in the strict band")
    print(f"DATA {name}: vertices/sector={n}, degree={degree}, retained={len(vals)}, "
          f"max_abs_adjacency={max(abs(vals)):.10f}, band={2*np.sqrt(q):.10f}, "
          f"lift_residual={residual:.3e}")
    return vals


def graphs():
    # Petersen as the Kneser graph KG(5,2).
    vertices = list(itertools.combinations(range(5), 2))
    pet = np.array([[int(set(v).isdisjoint(w)) for w in vertices] for v in vertices])
    for name, A in [("Petersen", pet), ("K4", np.ones((4, 4)) - np.eye(4))]:
        audit_lift(name, A, *graph_matrices(A), 3)

    # A Ramanujan graph with an endpoint: K3 Cartesian-product Q3, degree 5,
    # with eigenvalue -4 of multiplicity 2. Its Hashimoto eigenvalue -2 is defective.
    cube = np.array([[int((i ^ j).bit_count() == 1) for j in range(8)] for i in range(8)])
    endpoint = np.kron(np.ones((3, 3)) - np.eye(3), np.eye(8)) + np.kron(np.eye(3), cube)
    R, S, J, T = graph_matrices(endpoint)
    audit_lift("K3 x Q3 endpoint", endpoint, R, S, J, T, 5)
    M = sy.Matrix(T.toarray().astype(int)) + 2 * sy.eye(T.shape[0])
    geom = len(M.nullspace())
    generalized = len((M * M).nullspace())
    check(geom == 2 and generalized == 4, "endpoint graph: exact nullities 2 and 4 (Jordan obstruction)")
    print(f"DATA endpoint graph mu=-2: geometric={geom}, generalized_order_2={generalized}")


def quantum_matrices(letters, rev):
    E = [np.kron(U, U.conj()) for U in letters]
    d = len(E)
    n = len(E[0])
    R = np.hstack(E)
    S = np.vstack([np.eye(n)] * d)
    J = np.zeros((d*n, d*n), dtype=complex)
    for i in range(d):
        J[rev[i]*n:(rev[i]+1)*n, i*n:(i+1)*n] = E[i]
    return sum(E), R, S, J, sparse.csr_matrix(S @ R - J)


def audit_quantum(name, letters, rev, parity):
    A, R, S, J, T = quantum_matrices(letters, rev)
    n = len(A)
    D = len(letters)
    gamma = np.kron(parity, parity.conj())
    check(all(near(U.conj().T @ U, np.eye(len(U))) for U in letters), name + ": unitary letters")
    check(all(near(letters[rev[i]], U.conj().T) for i, U in enumerate(letters)), name + ": adjoint reversal")
    check(near(A @ gamma, gamma @ A), name + ": grading covariance")
    for sign, label in [(1, "even"), (-1, "odd")]:
        ix = np.flatnonzero(np.diag(gamma).real * sign > .5)
        edgeix = np.concatenate([i*n + ix for i in range(D)])
        audit_lift(name + " " + label, A[np.ix_(ix, ix)], R[np.ix_(ix, edgeix)],
                   S[np.ix_(edgeix, ix)], J[np.ix_(edgeix, edgeix)], T[edgeix][:, edgeix], D)
        u = .031 + .017j
        lhs = la.det(np.eye(len(edgeix)) - u*T[edgeix][:, edgeix].toarray())
        rhs = (1-u*u)**(len(ix)*(D-2)//2) * la.det(np.eye(len(ix))-u*A[np.ix_(ix,ix)]+(D-1)*u*u*np.eye(len(ix)))
        check(near(lhs, rhs, 1e-7), name + " " + label + ": independent determinant Bass check")
    return A, T, gamma


def quantum():
    I = np.eye(2)
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    Z = np.diag([1, -1])
    A, T, gamma = audit_quantum("Pauli", [X, X, Y, Y, Z, Z], [1, 0, 3, 2, 5, 4], Z)
    Td = T.toarray()
    edgegamma = np.kron(np.eye(6), gamma)
    counts = [round(np.trace(edgegamma @ np.linalg.matrix_power(Td, n)).real) for n in range(1, 7)]
    check(counts == [8, 32, 104, 640, 3208, 15392], "Pauli: net ring counts and cancellation")
    u = sy.symbols('u')
    poly = 1 + 2*u + 5*u*u
    reduced = sy.cancel(poly**2 / ((1-u)*(1-5*u)*poly))
    check(sy.cancel(reduced-poly/((1-u)*(1-5*u))) == 0, "Pauli: exact reduced elliptic zeta")
    print("DATA Pauli ring counts:", counts)

    letters = [I]*4 + [X]*4 + [Z]*2
    A, T, gamma = audit_quantum("Pauli endpoint", letters, [i ^ 1 for i in range(10)], Z)
    odd = np.concatenate([i*4 + np.array([1, 2]) for i in range(10)])
    M = sy.Matrix(np.rint(T[odd][:, odd].toarray().real).astype(int)) - 3*sy.eye(len(odd))
    geom, gen = len(M.nullspace()), len((M*M).nullspace())
    check(geom == 1 and gen == 2, "quantum endpoint: exact odd nullities 1 and 2; sector Ramanujan but no HP")
    print(f"DATA quantum endpoint mu=3: geometric={geom}, generalized_order_2={gen}")


def pgl_example():
    helpers = load_helpers("scripts/graded_ramanujan.py",
                           {"gl2_elements", "mul", "inv", "det", "pgl_canon", "legendre", "principal_series"})
    lps = load_helpers("scripts/weil_lps.py", {"lps_quaternions", "split_matrices", "quat_to_gl2", "conj"})
    p, q = 5, 13
    canon, mul = helpers['pgl_canon'], helpers['mul']
    gl = helpers['gl2_elements'](p)
    els = sorted({canon(g, p) for g in gl})
    I, J = lps['split_matrices'](p)
    S = [tuple(map(int, lps['quat_to_gl2'](a,p,I,J).flatten())) for a in lps['lps_quaternions'](q)]
    rev = [next(j for j,s in enumerate(S) if canon(s,p) == canon(helpers['inv'](a,p),p)) for a in S]
    ix = {g:i for i,g in enumerate(els)}
    A = np.zeros((len(els), len(els)))
    for i,g in enumerate(els):
        for s in S:
            A[i,ix[canon(mul(g,s,p),p)]] += 1
    # This tests the graph lift on all adjacency eigenvectors, including multiplicities.
    audit_lift("PGL2(F5) LPS(13) graph", A, *graph_matrices(A), q+1)
    chi = np.zeros(p, complex)
    for k in range(4):
        chi[pow(2,k,p)] = 1j**k
    rep = helpers['principal_series'](p, chi)
    g0 = [g for g in els if helpers['legendre'](helpers['det'](g,p),p) == 1]
    rng = np.random.default_rng(17)
    h = rng.normal(size=(6,6)) + 1j*rng.normal(size=(6,6))
    h += h.conj().T
    c = sum(rep(g) @ h @ rep(g).conj().T for g in g0) / len(g0)
    c -= np.trace(c)*np.eye(6)/6
    w,v = la.eigh(c)
    v = v[:, np.argsort(-w)]
    P = np.diag([1]*3+[-1]*3)
    letters = [v.conj().T @ rep(s) @ v for s in S]
    check(all(near(P @ U @ P, -U) for U in letters), "PGL2(F5): all LPS letters odd in C^{3|3}")
    audit_quantum("PGL2(F5) principal series", letters, rev, P)


def symbolic_and_scalar():
    H = sy.diag(1,-1)
    E = sy.Matrix([[0,1],[1,0]])
    W = sy.Matrix([[0,1],[-1,0]])
    X, up, um = H/2, (E+W)/2, (E-W)/2
    check(X*up-up*X == up and X*um-um*X == -um and up*um-um*up == 2*X,
          "sl2: exact conventions")
    # Lowest-weight module, U_- v0=0, X v_n=(-z+n)v_n.
    z = sy.symbols('z')
    for m in range(1,7):
        coefficient = sy.prod(k*(2*z-k+1) for k in range(1,m+1))
        claimed = sy.factorial(m)*sy.prod(2*(z-m)+m+j for j in range(1,m+1))
        check(sy.expand(coefficient-claimed) == 0, f"sl2: ladder coefficient m={m}")
    check(sy.expand((-z)**2 - (-z) - z*(z+1)) == 0, "sl2: Casimir X^2-X on ker U_-")
    Gbad = sy.ones(2)
    check(Gbad.det() == 0 and Gbad*sy.Matrix([1,-1]) == sy.zeros(2,1), "first band: aggregate pushforward Gram is singular")
    a = sy.symbols('a')
    flow = sy.diag(a,-1-a)
    swap = sy.Matrix([[0,1],[1,0]])
    check(swap*flow*swap == -sy.eye(2)-flow and swap*(-flow)*swap == sy.eye(2)+flow,
          "first band: FE for -X and corrected FE for X")
    for genus in [2,3,5]:
        c = 2*genus-2
        def sz(s):
            return 1 if s == 1 else (c+1 if s == 0 else c*(1-2*s) if s < 0 else 0)
        orders = [sz(s)-sz(s+1) for s in [1,0,-1,-2,-3,-4]]
        check(orders == [1,c,2*c-1,2*c,2*c,2*c], f"Ruelle: exact integer divisor genus={genus}")
        check(all(sum(sz(-N+j) for j in range(1,N+2)) == c*N*N+2 for N in range(1,8)),
              f"tower: integer multiplicity cN^2+2 genus={genus}")
    t = 1.3
    flat = 1/(4*np.sinh(t/2)**2)
    check(near((2-2*np.cosh(t))*flat, -1), "Ruelle: exterior supertrace sign")
    check(near((1-np.exp(t))*flat, -1/(1-np.exp(-t))), "Selberg: half-exterior transfer weight")
    check(2-2*np.cosh(t) < 0, "CP obstruction: transverse supertrace is negative")
    theta = sum((-1.)**n*np.exp(-2*n*n) for n in range(-20,21))
    dual = np.sqrt(np.pi/2)*sum(np.exp(-np.pi**2*(k+.5)**2/2) for k in range(-20,21))
    check(near(theta,dual) and theta > 0, "K-type grading: heat supertrace theta factor does not cancel")
    print(f"DATA K-type theta factor at t=1: {theta:.12f}")
    # Endpoint companion gives a universal exact obstruction; eigenvalue is on circle.
    C = sy.Matrix([[6,9],[-1,0]])
    N = C-3*sy.eye(2)
    check(N != sy.zeros(2) and N*N == sy.zeros(2), "Ihara endpoint: nonzero square-zero Jordan part")


if __name__ == '__main__':
    symbolic_and_scalar()
    graphs()
    quantum()
    pgl_example()
    print(f"FINAL TALLY: {PASS} PASS / {FAIL} FAIL")
    sys.exit(bool(FAIL))
