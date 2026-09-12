import sympy as sp, itertools, random, numpy as np
u = sp.symbols('u')
exec(open('/home/tobiasosborne/Projects/riemann-channel/notes/reviews/scratch_thm1_indep.py').read().split('# ---------- instance 1')[0])

# --- discrimination test: does a WRONG ordering fail? (confirms tests are sensitive) ---
def rhs_swapped(Es, bar, N, D):
    I = sp.eye(N); seen=set(); pref=sp.Integer(1)
    for i in range(D):
        p=frozenset((i,bar[i]))
        if p in seen: continue
        seen.add(p); pref *= (I - u**2*Es[bar[i]]*Es[i]).det()
    A=sp.zeros(N,N); Dop=sp.zeros(N,N)
    for i in range(D):
        P=(I-u**2*Es[i]*Es[bar[i]]).inv()      # WRONG order inside inverse
        A += u*Es[i]*P; Dop += u**2*Es[bar[i]]*Es[i]*P
    return sp.together(sp.expand(pref*(I+Dop-A).det()))
def rhs_rightmult(Es,bar,N,D):
    I=sp.eye(N); seen=set(); pref=sp.Integer(1)
    for i in range(D):
        p=frozenset((i,bar[i]))
        if p in seen: continue
        seen.add(p); pref *= (I-u**2*Es[bar[i]]*Es[i]).det()
    A=sp.zeros(N,N); Dop=sp.zeros(N,N)
    for i in range(D):
        P=(I-u**2*Es[bar[i]]*Es[i]).inv()
        A += u*P*Es[i]; Dop += u**2*P*Es[bar[i]]*Es[i]   # inverse on the LEFT
    return sp.together(sp.expand(pref*(I+Dop-A).det()))
random.seed(3)
def rmat(N): return sp.Matrix(N,N, lambda i,j: sp.Rational(random.randint(-4,4), random.randint(1,5)))
Es4 = [rmat(2) for _ in range(4)]; bar4=[1,0,3,2]
L = lhs(Es4,bar4,2,4)
print('control (correct rhs)      :', sp.simplify(L-rhs(Es4,bar4,2,4))==0)
print('wrong order inside inverse :', sp.simplify(L-rhs_swapped(Es4,bar4,2,4))==0, '(expect False)')
print('inverse multiplied on left :', sp.simplify(L-rhs_rightmult(Es4,bar4,2,4))==0, '(push-through identity => may be True)')

# --- edge cases ---
Z = sp.zeros(2,2)
Nil = sp.Matrix([[0,1],[0,0]])
Jor = sp.Matrix([[2,1],[0,2]])/5     # non-diagonalisable
cases = {
 'u=0 (both sides at u=0)': None,
 'all E = 0, D=4':            ([Z]*4, [1,0,3,2], 2, 4),
 'nilpotent E (E_ibar E_i=0), D=4': ([Nil,Nil,Nil,Nil], [1,0,3,2], 2, 4),
 'non-diagonalisable Jordan, D=4':  ([Jor,Jor,Jor,Jor], [1,0,3,2], 2, 4),
 'one E singular (rank 1), D=2':    ([sp.Matrix([[1,2],[2,4]]), rmat(2)], [1,0], 2, 2),
 'E_i = 0 for one index, D=4':      ([Z, rmat(2), rmat(2), rmat(2)], [1,0,3,2], 2, 4),
 'nilpotent, D=2':                  ([Nil, Nil], [1,0], 2, 2),
}
for tag,c in cases.items():
    if c is None:
        continue
    Es,bar,N,D = c
    L=lhs(Es,bar,N,D); R=rhs(Es,bar,N,D)
    print(f'{tag:36s}: {sp.simplify(sp.together(L-R))==0}   lhs={sp.factor(L)}')
# u = 0
Es,bar,N,D = [rmat(2) for _ in range(4)],[1,0,3,2],2,4
print('u=0: lhs =', lhs(Es,bar,N,D).subs(u,0), ' rhs =', sp.simplify(rhs(Es,bar,N,D).subs(u,0)))

# --- Corollary 3 (E_ibar = E_i^{-1}) ---
for D in (2,4,6):
    N=2; random.seed(D)
    half=[]
    while len(half)<D//2:
        M=rmat(2)
        if M.det()!=0: half.append(M)
    Es=[]; bar=[]
    for k in range(D//2):
        Es += [half[k], half[k].inv()]
    bar = [i^1 for i in range(D)]
    Sig = sum(Es, sp.zeros(2,2))
    L=lhs(Es,bar,N,D)
    C3=(1-u**2)**sp.Rational(N*(D-2),2)*(sp.eye(N)-u*Sig+(D-1)*u**2*sp.eye(N)).det()
    print(f'Cor3 D={D}: thm-rhs ok {sp.simplify(L-rhs(Es,bar,N,D))==0}; cor3 formula ok {sp.simplify(sp.expand(L-C3))==0}')
