# Reviewer claude:opus-5.  T2.1 example, T0.3 counterexamples.
import numpy as np, itertools
print("=== T2.1 <1>4: y^2 = x^3 + x over F_5 ===")
pts=1
for x in range(5):
    r=(x**3+x)%5
    pts+=sum(1 for y in range(5) if (y*y)%5==r)
print("  #E(F_5) =", pts, "  a = 5+1-#E =", 6-pts, "  pi = roots of z^2-2z+5:", np.roots([1,-(6-pts),5]))
# Frobenius roots 1 +- 2i ?
print("  1+2i, 1-2i are the roots:", np.allclose(sorted(np.roots([1,-2,5]).imag), [-2,2]))
# O/(pi-1) = O/(2i)
pi=complex(1,2)
def classes(mod):
    # Z[i]/(mod): enumerate residues by brute force over a big box
    seen=set()
    for a in range(-30,31):
        for b in range(-30,31):
            z=complex(a,b)
            # canonical rep: search small representative
            best=None
            for u in range(-6,7):
                for v in range(-6,7):
                    w=z-(complex(u,v)*mod)
                    if best is None or (abs(w),w.real,w.imag)<(abs(best),best.real,best.imag): best=w
            seen.add((round(best.real),round(best.imag)))
    return seen
cl=classes(pi-1)
print("  O/(pi-1) = O/(2i): canonical residues found:", sorted(cl), " -> |O/(pi-1)| =", len(cl), "(astra: 4)")
def red(z,mod):
    best=None
    for u in range(-6,7):
        for v in range(-6,7):
            w=z-(complex(u,v)*mod)
            if best is None or (abs(w),w.real,w.imag)<(abs(best),best.real,best.imag): best=w
    return (round(best.real),round(best.imag))
D=[0,1,-1,2,-2]
print("  digits D =",D," reduce mod (pi-1) to:", sorted({red(complex(d,0),pi-1) for d in D}), "-> only", len({red(complex(d,0),pi-1) for d in D}),"of",len(cl),"classes")
print("  D distinct mod pi?", len({red(complex(d,0),pi) for d in D})==5, sorted({red(complex(d,0),pi) for d in D}))
print("  |1-pi^2|^2 =", abs(1-pi**2)**2, " > q^2 = 25 :", abs(1-pi**2)**2>25)
print("  N_2 = #E(F_25) =", 1+25-2*(pi**2).real)
# carry bound
C_D=max(abs(complex(d)-complex(e)) for d in D for e in D)
print("  C_D =", C_D, " bound C_D/(|pi|-1) =", C_D/(abs(pi)-1))

print("\n=== T0.3 <1>2 counterexamples ===")
for D_ in (2,3):
    al=[(i,j) for i in range(D_) for j in range(D_)]
    Mx=np.zeros((D_*D_,D_*D_))
    for p,(i,j) in enumerate(al):
        for r,(k,l) in enumerate(al): Mx[p,r]= (j==k)*(i==l)
    print(f"  matrix-unit alphabet D={D_}, n=2: flattening rank {np.linalg.matrix_rank(Mx)} (= D^2 = {D_*D_})")
A0=np.array([[1,1],[0,0]],float); A1=np.array([[0,0],[1,-1]],float)
As=[A0,A1]
for n in (4,6):
    amp={}
    for w in itertools.product((0,1),repeat=n):
        t=np.trace(np.linalg.multi_dot([As[i] for i in w]))
        sgn=(-1)**sum(w[k]*w[(k+1)%n] for k in range(n))
        amp[w]=(t,sgn)
    print(f"  n={n}: amplitude == (-1)^sum s_i s_(i+1) for all words:", all(abs(t-s)<1e-12 for t,s in amp.values()))
    k=n//2
    Mt=np.zeros((2**k,2**k))
    for a_ in range(2**k):
        u=tuple((a_>>i)&1 for i in range(k))
        for b_ in range(2**k):
            v=tuple((b_>>i)&1 for i in range(k))
            Mt[a_,b_]=amp[u+v][0]
    print(f"        contiguous {k}|{k} cut flattening rank = {np.linalg.matrix_rank(Mt)}  (D^2 = 4)")
