from common import *

def run_dirichlet(p,m,modulus,name):
    c=Checks(name); F=Field(p,m,modulus); order=F.order-1
    w=s.symbols('w'); cyclo=s.cyclotomic_poly(order,w)
    def red(v): return s.rem(s.cancel(s.expand(v)),cyclo,w)
    g=F.primitive(); logs={F.power(g,k):k for k in range(order)}
    chi=s.Matrix([[0 if j==0 else w**logs[j] for j in range(F.order)]])
    letters=[]
    for digit in range(p):
        A=s.zeros(F.order)
        for j in range(F.order): A[F.add(F.mul(p,j),digit),j]=1
        letters.append(A)
    T=sum(letters,s.zeros(F.order)); initial=s.zeros(F.order,1); initial[1]=1
    coeff=[red((chi*T**n*initial)[0]) for n in range(7)]
    for n in range(m,7): c.equal(coeff[n],0,f'monic coefficient degree {n} vanishes')
    alpha=red(-coeff[1]-(1 if p==2 else 0))
    alphabar=red(alpha.subs(w,w**(order-1)))
    c.equal(red(alpha*alphabar),p,'RH by exact cyclotomic arithmetic')
    if p==2: c.equal(red(1+sum(coeff[1:m])),0,'even character has factor 1-u')
    else: c.equal(red(w**logs[p-1]),-1,'odd character is nontrivial on -1')
    L=sum(coeff[n]*u**n for n in range(m))
    expected=(1-u)*(1-alpha*u) if p==2 else 1-alpha*u
    c.equal(red(L-expected),0,'explicit L polynomial from monic words')
    N=[red(-alpha**n-(1 if p==2 else 0)) for n in range(1,7)]
    x=s.symbols('x'); prime_polys={d:[] for d in range(1,7)}
    for d in range(1,7):
        for digits in itertools.product(range(p),repeat=d):
            poly=x**d+sum(digits[i]*x**i for i in range(d))
            if s.Poly(poly,x,modulus=p).is_irreducible:
                value=1
                for digit in reversed(digits): value=F.add(F.mul(p,value),digit)
                prime_polys[d].append(value)
        weighted=0
        for e in s.divisors(d):
            weighted+=e*sum(0 if v==0 else w**((logs[v]*(d//e))%order) for v in prime_polys[e])
        c.equal(red(weighted-N[d-1]),0,f'irreducible-polynomial Euler logarithm degree {d}')
    # All nontrivial characters; over F3 only odd k have the stated degree one and radius.
    for k in range(1,order):
        ak=red(alpha.subs(w,w**k))
        if p==2 or k%2:
            c.equal(red(ak*ak.subs(w,w**(order-1))),p,f'character k={k} RH')
        else:
            chik=s.Matrix([[0 if j==0 else w**((k*logs[j])%order) for j in range(F.order)]])
            c.equal(red((chik*T*initial)[0]),-1,f'even character k={k} has only 1-u')
    # Horner letters are permutations, but multiplication of the bond by g does NOT commute.
    U=s.zeros(F.order)
    for j in range(F.order): U[F.mul(g,j),j]=1
    c.check(U*T!=T*U,'Horner sum is not the Galois-commuting Frobenius transfer')
    scalar=complex(np.exp(2j*np.pi/order))
    num=lambda v: complex(s.N(v.subs(w,scalar),14))
    open_norm=[p**n-(p**(n-m) if n>=m else 0) for n in range(1,7)]
    # Direct open-word contraction, including the killed modulus word.
    for n in range(1,m+1):
        tot=0
        for digits in itertools.product(range(p),repeat=n):
            v=1
            for d in digits: v=F.add(F.mul(p,v),d)
            tot+=int(v!=0)
        c.equal(tot,open_norm[n-1],f'physical open-chain norm n={n}')
    Fodd=s.diag(1,alpha) if p==2 else s.Matrix([[alpha]])
    matrices={**{f'H_{j}':v for j,v in enumerate(letters)},'Pi_open':s.eye(F.order),
              'right_boundary_e1':initial,'left_character_row':chi,
              'multiplication_by_generator':U,'amplitude_F_odd':Fodd,'Pi_amplitude':-s.eye(Fodd.rows)}
    return c.finish(matrices,{'L_monic_coefficients_0..6':coeff,'log_N_1..6_exact':N,
                    'log_N_1..6_decimal':[num(v) for v in N],
                    'formal_a_1..6_exact':[red(v) for v in primes(N)],
                    'formal_a_1..6_decimal':[num(red(v)) for v in primes(N)],'physical_open_norm_1..6':open_norm},
                    {'L':s.factor(expected),'alpha':alpha,'alpha_decimal':num(alpha),
                     'w':f'exp(2*pi*i/{order})','primitive_generator_digits':F.digits(g),
                     'odd_character_k':1},
                    ['The formal a_d are Mobius exponents, not the character sums over degree-d primes.',
                     'The displayed character row is linear; a bra ket for it uses the conjugate ket.'])
