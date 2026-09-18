#!/usr/bin/env python3
"""Independent finite/clock critic computations; copied finite red mutations."""
from pathlib import Path
from itertools import product
import subprocess
import sys
import tempfile
import sympy as s

CONJUGATE_FEATURES = True  # RED_CLOCK
VALID_AUTOMATON = True  # RED_UNARY
COUNT = 0


def check(value, name):
    global COUNT
    COUNT += 1
    if not value:
        raise RuntimeError(name)


def equal(a, b, name):
    check(a.shape == b.shape and all(s.simplify(v) == 0 for v in a-b), name)


def vec(a):
    return s.Matrix.vstack(*[a[:, j] for j in range(a.cols)])


def unary():
    q, n = 3, 4
    z = s.diag(1, s.I, -1)
    similarity = s.Matrix([[1, 1, 0], [0, 1, 1], [0, 0, 1]])
    transfer = similarity*z*similarity.inv()
    projectors = []
    for a in range(q):
        e = s.zeros(q)
        e[a,a] = 1
        projectors.append(similarity*e*similarity.inv())
    zero = s.zeros(q)
    one = s.eye(q)
    m1 = z.row_join(zero).col_join(zero.row_join(zero))
    m0 = zero.row_join(one).col_join(zero.row_join(one))
    if not VALID_AUTOMATON:
        m0[q, 0] = 1
    left = s.ones(1,q).row_join(s.zeros(1,q))
    for word in product((0,1), repeat=n):
        state = left
        for bit in word:
            state = state*(m1 if bit else m0)
        output = s.zeros(q)
        for a,p in enumerate(projectors):
            output += (state[a]+state[q+a])*p
        good = tuple(sorted(word, reverse=True)) == word
        target = transfer**sum(word) if good else s.zeros(q)
        equal(output,target,"unary exact word "+str(word))
    print("PASS independent unary automaton: 16 words, nonorthogonal spectral idempotents")


def clock():
    k,d = 4,2
    e=s.diag(1,s.I)
    powers=[e**j for j in range(k)]
    v=[vec(p) for p in powers]
    gram=s.Matrix(k,k,lambda j,l:(v[j].conjugate().T*v[l])[0])
    features=[x.conjugate() for x in v] if CONJUGATE_FEATURES else v
    amplitudes=s.Matrix.vstack(*[x.T for x in features])
    equal(amplitudes*amplitudes.conjugate().T,gram,"conjugated clock Gram")
    history=s.Matrix.vstack(*features)
    step=s.kronecker_product(s.eye(d),e.conjugate())
    h=s.zeros(k*d*d)
    for j in range(k-1):
        ell=s.zeros(d*d,k*d*d)
        ell[:,j*d*d:(j+1)*d*d]=-step
        ell[:,(j+1)*d*d:(j+2)*d*d]=s.eye(d*d)
        h+=ell.conjugate().T*ell
    equal(h*history,s.zeros(k*d*d,1),"FK history")
    controlled=s.diag(*[step**j for j in range(k)])
    path=s.zeros(k)
    for j in range(k-1):
        path[j,j]+=1;path[j+1,j+1]+=1
        path[j,j+1]-=1;path[j+1,j]-=1
    equal(controlled.conjugate().T*h*controlled,s.kronecker_product(path,s.eye(d*d)),"FK path conjugacy")
    check(path.eigenvals()=={0:1,2:1,2-s.sqrt(2):1,2+s.sqrt(2):1},"FK exact gap")
    check(len(h.nullspace())==d*d,"FK degeneracy")
    w=vec(s.eye(d))/s.sqrt(d)
    pin=s.zeros(k);pin[0,0]=1
    pinned=h+s.kronecker_product(pin,s.eye(d*d)-w*w.T)
    check(len(pinned.nullspace())==1,"pinned FK unique ground line")
    equal(pinned*history,s.zeros(k*d*d,1),"pinned history")
    print("PASS independent conjugated clock/FK: K=4, gap 2-sqrt(2), degeneracy 4, pinned nullity 1")


def pauli():
    e=s.Matrix([[0,-5],[1,-2]])/s.sqrt(5)
    g=s.Matrix([[1,-1],[-1,5]])
    equal(e.T*g*e,g,"Pauli metric")
    check(s.trace(e.T*e)==6,"Pauli native mismatch")
    u=s.symbols('u')
    def edge_det(weights):
        t=s.Matrix(6,6,lambda i,j:weights[i] if j!=(i^1) else 0)
        return s.factor((s.eye(6)-u*t).det())
    trivial=edge_det([1]*6)
    others=[edge_det([1,1,-1,-1,-1,-1]),edge_det([-1,-1,1,1,-1,-1]),edge_det([-1,-1,-1,-1,1,1])]
    check(trivial==(u-1)*(5*u-1)*(u-1)**2*(u+1)**2,"Pauli trivial edge block")
    check(all(s.cancel(p-(1-u*u)**2*(1+2*u+5*u*u))==0 for p in others),"Pauli other edge blocks")
    check(s.cancel(others[0]*others[1]/(trivial*others[2])-(1+2*u+5*u*u)/((1-u)*(1-5*u)))==0,"Pauli net graded zeta")
    print("PASS independent six-letter Pauli Hashimoto determinants and retained metric")


def obstructions():
    # Three cube roots have t0=3,t1=0, so the two-length fit is 3I.
    w=3*s.eye(2); shifted=w-3*s.eye(2); xi=s.Matrix([1,-s.Rational(1,2)])
    equal(shifted*xi,s.zeros(2,1),"degenerate fitted vector null")
    check(xi[0]+2*xi[1]==0,"degenerate fitted vector off-circle root")
    gamma=s.Matrix([1,0])
    check(len(gamma.nullspace())==0 and len(gamma.T.nullspace())==1,"physical parent uses adjoint kernel")
    e=s.diag(1,s.I)
    vs=[vec(e**j) for j in range(3)]
    omega=s.Matrix.vstack(*vs)
    xi=s.Matrix([s.I,-1-s.I,1]);proj=xi*xi.conjugate().T/(xi.conjugate().T*xi)[0]
    residual=s.kronecker_product(proj,s.eye(4))*omega
    check(s.simplify((residual.conjugate().T*residual)[0])==2,"unconjugated history wrong kernel projector")
    equal(s.kronecker_product(proj.conjugate(),s.eye(4))*omega,s.zeros(12,1),"conjugated kernel projector")
    print("PASS independent obstruction fixtures: repeated fit minimum, physical parent adjoint, clock conjugation")


def red():
    source=Path(__file__).read_text()
    for old,new,marker in [("CONJUGATE_FEATURES = True  # RED_CLOCK","CONJUGATE_FEATURES = False  # RED_CLOCK","conjugated clock Gram"),("VALID_AUTOMATON = True  # RED_UNARY","VALID_AUTOMATON = False  # RED_UNARY","unary exact word")]:
        check(source.splitlines().count(old)==1,"unique red target")
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent,prefix='red-') as temp:
            copied=Path(temp)/'probe.py';copied.write_text(source.replace(old,new,1))
            process=subprocess.run([sys.executable,'-O',str(copied),'--probe'],text=True,capture_output=True)
        check(process.returncode!=0 and marker in process.stdout+process.stderr,"copied finite red mutation")
        print("PASS copied red mutation:",marker,"exit",process.returncode)


def main():
    unary();clock();pauli();obstructions()
    if '--probe' not in sys.argv:
        red()
    print("PASS independent conditions",COUNT)


if __name__=='__main__':
    main()
