#!/usr/bin/env python3
"""Checks for 'Which overlaps of the code determine the lattice?' (notes/adelic-gkp/overlap-data.md), lane F.

The class-number-two pair of curve-bridge.md: q = 7, a = 2, pi^2 - 2 pi + 7 = 0, Z[pi] = Z[sqrt(-6)] (maximal, h = 2).
E4: y^2 = x^3 + 3x + 3 (j = 4) and E5: y^2 = x^3 + x + 3 (j = 5) over F_7.  Lattice classes (1,0,6), (2,0,3).
The Pauli-six pair (q = 5, a = -2): y^2 = x^3 + 4x (End Z[i]) and y^2 = x^3 + 4x + 1 (End Z[2i]); lattices (2,0,2), (1,0,4).

Blocks:
 C  the two curves, their isogenies, the Hilbert class polynomial, the epsilon-dependence of "which curve is principal";
 R  the overlap function <Theta_K, 1_D> = q^{h^0(D)} by brute-force linear algebra = Riemann-Roch + Abel-Jacobi;
 O  the overlap data of E4 and E5 agree: trace-fibre statistics at levels F_7, F_49, F_343, and an explicit
    Frobenius-equivariant group isomorphism Phi: E4(F_{7^m}) -> E5(F_{7^m}) glued from the 2- and 3-isogenies;
 T  lattice side: the Z[M]-modules Z^2/N are isomorphic for every N, but not as polarised modules (det of intertwiners);
 W  curve side: Frobenius-equivariant isomorphisms E4[n] -> E5[n] and the Weil pairing (the genus at 2 and 3);
 P  the Pauli-six pair: the overlaps see the order.

Needs PARI/GP as the binary /usr/bin/gp (subprocess) and sympy.  Run:  python3 check_overlap_data.py > output_overlap_data.txt
"""
import itertools
import math
import subprocess
import sympy as sp

npass = nfail = 0


def check(name, ok, detail=""):
    global npass, nfail
    npass += bool(ok)
    nfail += (not ok)
    print(("PASS  " if ok else "FAIL  ") + name + ("  " + detail if detail else ""))


GP_LIB = r"""
setrand(20261006);
pp=7;
\\ points of y^2 = x^3 + A x + B over F_{7^m} (affine), and the field generator
allpts(A,B,m)={my(t=ffgen(pp^m,'t),g=ffprimroot(t),x=0*t,L=List(),f,y);
  for(i=0,pp^m-1, if(i==1,x=g, if(i>1,x=x*g)); f=x^3+A*x+B; if(f==0, listput(L,[x,0*t]), if(issquare(f,&y), listput(L,[x,y]); listput(L,[x,-y]))));
  [t,Vec(L)]};
frobk(P,k)=if(#P<2,P,[P[1]^(pp^k),P[2]^(pp^k)]);
degF7(P,m)={my(e);fordiv(m,d, if(frobk(P,d)==P, return(d)));};
\\ fibre sizes of the trace map from places of degree d over F_{7^k} to Pic^d = E(F_{7^k}), from all points over F_{7^m}
fibres(A,B,m,k,d,R)={my(t=R[1],E=ellinit([A,B],t),M=Map(),e,dd,T,Q,key,c,v,nE,nplaces=0);
  foreach(R[2],P, e=degF7(P,m); dd=e/gcd(e,k); if(dd!=d, next);
    T=P; Q=P; for(i=1,d-1, Q=frobk(Q,k); T=elladd(E,T,Q)); key=Str(T);
    if(mapisdefined(M,key,&c), mapput(M,key,c+1), mapput(M,key,1)); nplaces++);
  if(d==1, key=Str([0]); if(mapisdefined(M,key,&c), mapput(M,key,c+1), mapput(M,key,1)); nplaces++);
  v=apply(z->z/d, Vec(Mat(M)[,2])); nE=ellcard(ellinit([A,B],ffgen(pp^k,'s)));
  [nplaces/d, nE, vecsort(concat(v, vector(nE-#v,i,0)))]};

\\ places of E/F_7 of degree <= dmax (affine), each as the list of its geometric points, from all points over F_{7^m}
places(R,m,dmax)={my(L=List(),seen=Map(),e,orb,Q);
  foreach(R[2],P, e=degF7(P,m); if(e>dmax || mapisdefined(seen,Str(P)), next);
    orb=vector(e); Q=P; for(i=1,e, orb[i]=Q; mapput(seen,Str(Q),1); Q=frobk(Q,1)); listput(L,orb));
  Vec(L)};
\\ h^0(nO - E) by linear algebra: basis x^i y^e of L(nO) (2i+3e <= n), vanishing at every geometric point of E (E reduced)
h0bf(n,pts)={my(mons=List(),Mt);if(n<0,return(0));
  for(e=0,1,for(i=0,n, if(2*i+3*e<=n, listput(mons,[i,e]))));
  if(#pts==0, return(#mons));
  Mt=matrix(#pts,#mons,r,c, pts[r][1]^mons[c][1]*pts[r][2]^mons[c][2]);
  #mons-matrank(Mt)};
\\ Riemann-Roch + Abel-Jacobi prediction
h0rr(E,n,pts)={my(dg=#pts,S=[0]);if(n>dg,return(n-dg));if(n<dg,return(0));
  foreach(pts,P,S=elladd(E,S,P)); S==[0]};
rcheck(A,B,R,m)={my(t=R[1],E=ellinit([A,B],t),pl=places(R,m,3),cnt=0,bad=0,zero=0,prin=0,Ds=List(),pts,dg);
  for(i=1,#pl, listput(Ds,pl[i]));
  for(i=1,#pl,for(j=i+1,#pl, if(#pl[i]+#pl[j]<=4, listput(Ds,concat(pl[i],pl[j])))));
  foreach(Ds,pts, dg=#pts; for(n=dg-1,dg+1, cnt++; if(h0bf(n,pts)!=h0rr(E,n,pts),bad++); if(n==dg,zero++; prin+=h0rr(E,n,pts))));
  [#pl, vector(3,d,#select(z->#z==d,pl)), cnt, bad, zero, prin]};

\\ ---- the two isogenies E4 -> E5 over F_7 (Velu, kernels E4(F_7)[2] and E4(F_7)[3]), as integer rational maps
E4m=ellinit([3,3]*Mod(1,7)); E5m=ellinit([1,3]*Mod(1,7));
iso2=ellisogeny(E4m,[Mod(1,7),Mod(0,7)]); iso3=ellisogeny(E4m,ellmul(E4m,ellgroup(E4m,,1)[3][1],2));
applyisog(I,P)={my(f=lift(I[2][1]),g=lift(I[2][2]),h=lift(I[2][3]),H);
  if(#P<2,return([0])); H=subst(h,'x,P[1]); if(H==0,return([0]));
  [subst(f,'x,P[1])/H^2, subst(subst(g,'y,P[2]),'x,P[1])/H^3]};
u4(P)=if(#P<2,P,[4*P[1],P[2]]);   \\ y^2=x^3+4x+3  ->  y^2=x^3+x+3
PhiMake(m)={my(t=ffgen(7^m,'t),E4=ellinit([3,3],t),E5=ellinit([1,3],t),N=ellcard(E4),a=valuation(N,2),No=N>>a,e2,eo);
  e2=lift(chinese(Mod(1,2^a),Mod(0,No))); eo=lift(Mod(1-e2,N));
  [t,E4,E5,N,e2,eo]};
Phi(D,P)={my(E4=D[2],E5=D[3]); elladd(E5, applyisog(iso2,ellmul(E4,P,D[6])), u4(applyisog(iso3,ellmul(E4,P,D[5]))))};
\\ a basis of E(F)[l^e] (r = its rank, 1 or 2), by random points; the pair is a basis iff the Weil pairing is primitive
lbasis(E,N,l,e,r)={my(co=N/l^valuation(N,l),y=vector(r),x,o,k=0);
  while(k<r, x=ellmul(E,random(E),co); o=ellorder(E,x); if(o<l^e, next); x=ellmul(E,x,o/l^e);
    if(k==1 && ellweilpairing(E,y[1],x,l^e)^(l^(e-1))==1, next); k++; y[k]=x);
  y};
\\ test of Phi over F_{7^m}: injective (Phi nonzero on every line of E(F)[l], every prime l), Frobenius-equivariant and additive on random points
PhiTest(m)={my(D=PhiMake(m),E4=D[2],E5=D[3],N=D[4],cyc=ellgroup(E4),c5=ellgroup(E5),ok=1,P,Q,ninj=0,r,b);
  if(#cyc<2,cyc=concat(cyc,[1]));
  for(i=1,6, P=random(E4); Q=random(E4);
     if(Phi(D,elladd(E4,P,Q))!=elladd(E5,Phi(D,P),Phi(D,Q)), ok=0);
     if(Phi(D,frobk(P,1))!=frobk(Phi(D,P),1), ok=0));
  foreach(factor(N)[,1],l, r=if(cyc[2]%l==0,2,1); b=lbasis(E4,N,l,1,r);
     ninj++; if(Phi(D,b[1])==[0], ok=0);
     if(r==2, for(a=0,l-1, ninj++; if(Phi(D,elladd(E4,ellmul(E4,b[1],a),b[2]))==[0], ok=0))));
  [m, N, cyc, c5, ninj, ok]};
\\ pointwise test over a small field: Phi is a bijection E4(F_{7^m}) -> E5(F_{7^m}) commuting with Frobenius
PhiPointwise(m)={my(D=PhiMake(m),R4=allpts(3,3,m),pts=concat(R4[2],[[0]]),img=Map(),ok=1,P2);
  foreach(pts,P, P2=Phi(D,P); if(!ellisoncurve(D[3],P2),ok=0); mapput(img,Str(P2),1); if(Phi(D,frobk(P,1))!=frobk(P2,1),ok=0));
  [#pts, #img, ok]};

\\ ---- Weil pairing and Frobenius on E[n] (n = l^e), E[n] inside E(F_{7^k})
tors(A,B,t,n)={my(E=ellinit([A,B],t),N=ellcard(E),f=factor(n),b,P,Q,Am=matrix(2,2),z,fr);
  b=lbasis(E,N,f[1,1],f[1,2],2); P=b[1]; Q=b[2];
  for(col=1,2, fr=frobk(if(col==1,P,Q),1);
     for(a=0,n-1,for(c=0,n-1, if(elladd(E,ellmul(E,P,a),ellmul(E,Q,c))==fr, Am[1,col]=a;Am[2,col]=c))));
  z=ellweilpairing(E,P,Q,n); [E,P,Q,Am,z]};
\\ all scalings c (e5(gx,gy) = e4(x,y)^c) of Frobenius-equivariant isomorphisms E4[n] -> E5[n]
pairscal(k,n)={my(t=ffgen(7^k,'t),T4=tors(3,3,t,n),T5=tors(1,3,t,n),w5=-1,S=Set(),g,nint=0);
  for(j=0,n-1, if(T4[5]^j==T5[5], w5=j));
  forvec(v=vector(4,i,[0,n-1]), g=Mod([v[1],v[2];v[3],v[4]],n);
     if(matdet(g)==0 || gcd(lift(matdet(g)),n)>1, next); if(g*T4[4]!=T5[4]*g, next);
     nint++; S=setunion(S,[lift(w5*matdet(g))]));
  [n, k, T4[4], T5[4], nint, S]};
\\ scaling by the explicit isogenies: e5(phi P, phi Q) = e4(P,Q)^c
isogscal(k,n,which)={my(t=ffgen(7^k,'t),T4=tors(3,3,t,n),D=PhiMake(k),X,Y,z5,c=-1);
  X=if(which==2,applyisog(iso2,T4[2]),u4(applyisog(iso3,T4[2]))); Y=if(which==2,applyisog(iso2,T4[3]),u4(applyisog(iso3,T4[3])));
  z5=ellweilpairing(D[3],X,Y,n); for(j=0,n-1, if(T4[5]^j==z5, c=j)); c};

"""


def gp(body):
    r = subprocess.run(["gp", "-q", "-f", "-s", "1000000000"], input=GP_LIB + body, capture_output=True, text=True,
                       timeout=600)
    if r.returncode != 0 or "***" in r.stderr + r.stdout:
        raise RuntimeError(r.stderr + r.stdout)
    return r.stdout


def gpval(s):
    """parse a gp vector printed with print(); no matrices"""
    return eval(s.replace("~", ""))


def lines(out):
    d = {}
    for ln in out.splitlines():
        if "|" in ln:
            k, v = ln.split("|", 1)
            d.setdefault(k, []).append(v)
    return d


OM = sp.Matrix([[0, 1], [-1, 0]])


def form_to_step(f, a):
    """Latimer-MacDuffee (curve-bridge.md D3): the integer step of trace a whose Weil form (1/2) Omega (M - V) is f"""
    A, B, C = f
    return sp.Matrix([[(a - B) // 2, -C], [A, (a + B) // 2]])


def weil_form(M, a):
    V = a * sp.eye(2) - M
    G = (OM * (M - V)) / 2
    return (int(G[0, 0]), int(2 * G[0, 1]), int(G[1, 1]))


def reduce_form(f):
    """reduce a positive definite binary form (A,B,C) (Gauss)"""
    A, B, C = f
    while True:
        if C < A:
            A, B, C = C, -B, A
        k = (A - B) // (2 * A)          # bring B into (-A, A]
        if not (-A < B <= A):
            B, C = B + 2 * k * A, A * k * k + B * k + C
            continue
        if A == C and B < 0:
            B = -B
        if C < A:
            continue
        return (A, B, C)


def reduced_forms(D):
    out = []
    A = 1
    while 3 * A * A <= -D:
        for B in range(-A + 1, A + 1):
            if (B * B - D) % (4 * A):
                continue
            C = (B * B - D) // (4 * A)
            if C < A or (B < 0 and A == C):
                continue
            out.append((A, B, C))
        A += 1
    return out


def intertwiner_dets(M1, M2, N):
    """{det g mod N : g in GL2(Z/N), g M1 = M2 g mod N}"""
    a1 = [[int(M1[i, j]) % N for j in range(2)] for i in range(2)]
    a2 = [[int(M2[i, j]) % N for j in range(2)] for i in range(2)]
    dets = set()
    for g00, g01, g10, g11 in itertools.product(range(N), repeat=4):
        d = (g00 * g11 - g01 * g10) % N
        if math.gcd(d, N) != 1:
            continue
        # g M1
        l00 = (g00 * a1[0][0] + g01 * a1[1][0]) % N
        l01 = (g00 * a1[0][1] + g01 * a1[1][1]) % N
        l10 = (g10 * a1[0][0] + g11 * a1[1][0]) % N
        l11 = (g10 * a1[0][1] + g11 * a1[1][1]) % N
        r00 = (a2[0][0] * g00 + a2[0][1] * g10) % N
        r01 = (a2[0][0] * g01 + a2[0][1] * g11) % N
        r10 = (a2[1][0] * g00 + a2[1][1] * g10) % N
        r11 = (a2[1][0] * g01 + a2[1][1] * g11) % N
        if (l00, l01, l10, l11) == (r00, r01, r10, r11):
            dets.add(d)
    return dets


q, a = 7, 2
F106, F203 = (1, 0, 6), (2, 0, 3)
M1, M2 = form_to_step(F106, a), form_to_step(F203, a)

# ------------------------------------------------------------------------------------------------------------
print("== C. The two curves over F_7 with a = 2, and which lattice class each carries")
out = gp(r"""
for(A=0,6,for(B=0,6,if((4*A^3+27*B^2)%7==0,next);E=ellinit([A,B]*Mod(1,7));if(ellap(E)==2,print("TR|",[A,B,lift(E.j),ellgroup(E)]))));
print("CL|",[quaddisc(-24),qfbclassno(-24)]);
foreach([[3,3],[1,3]],c, E=ellinit(c*Mod(1,7)); print("DIV|",[c, #polrootsmod(c[2]+c[1]*'x+'x^3,7), #polrootsmod(elldivpol(E,3),7)]));
for(w=2,3, Ei=ellinit(if(w==2,iso2,iso3)[1]); print("ISO|",[w, lift(Ei.a4), lift(Ei.a6), lift(Ei.j)]));
G5=ellgroup(E5m,,1)[3][1]; J2=ellisogeny(E5m,ellmul(E5m,G5,3)); J3=ellisogeny(E5m,ellmul(E5m,G5,2));
print("BACK|",[lift(ellinit(J2[1]).j), lift(ellinit(J3[1]).j)]);
print("U4|",[lift(Mod(4,7)^2*4), lift(Mod(4,7)^3*3)]);
H=polclass(-24); print("HCP|",[Vec(H), Vec(lift(polrootsmod(H,7))), poldisc(H)%7]);
default(realprecision,50);
print("JNUM|",[abs(ellj(I*sqrt(6))-(2417472+1707264*sqrt(2)))<1e-30, abs(ellj(I*sqrt(6)/2)-(2417472-1707264*sqrt(2)))<1e-30, round(real(ellj(I*sqrt(6)))), round(real(ellj(I*sqrt(6)/2)))]);
print("RED|",[lift(Mod(2417472,7)),lift(Mod(1707264,7)), Vec(lift(polrootsmod('x^2-2,7)))]);
""")
d = lines(out)
tr = [gpval(s) for s in d["TR"]]
js = sorted(set(t[2] for t in tr))
check("C1 the curves y^2 = x^3 + Ax + B over F_7 with trace a = 2 have j in {4, 5}, three models each, all with E(F_7) = Z6",
      js == [4, 5] and all(t[3] == [6] for t in tr) and sum(t[2] == 4 for t in tr) == 3 and sum(t[2] == 5 for t in tr) == 3,
      "models " + ", ".join(f"{t[:2]} j={t[2]}" for t in tr))
cl = gpval(d["CL"][0])
check("C2 disc Z[pi] = a^2 - 4q = -24 is fundamental (Z[pi] = Z[sqrt(-6)] maximal), class number 2, reduced forms (1,0,6), (2,0,3)",
      cl == [-24, 2] and reduced_forms(-24) == [F106, F203], f"reduced forms {reduced_forms(-24)}")
dv = [gpval(s) for s in d["DIV"]]
check("C3 each curve has exactly one F_7-rational subgroup of order 2 and one of order 3 (one root of the 2- and of the 3-division polynomial)",
      all(x[1] == 1 and x[2] == 1 for x in dv), f"{dv}")
iso = [gpval(s) for s in d["ISO"]]
back = gpval(d["BACK"][0])
u = gpval(d["U4"][0])
check("C4 the 2-isogeny with kernel E4(F_7)[2] lands on y^2 = x^3 + x + 3 = E5; the 3-isogeny with kernel E4(F_7)[3] lands on y^2 = x^3 + 4x + 3 (j = 5), "
      "and (x,y) -> (4x,y) maps it onto E5", iso[0][1:] == [1, 3, 5] and iso[1][1:] == [4, 3, 5] and u == [1, 3], f"{iso}")
check("C5 the rational 2- and 3-isogenies from E5 land on j = 4: the class group (order 2, generated by [p2] = [p3]) swaps the two curves",
      back == [4, 4])
hcp = gpval(d["HCP"][0])
check("C6 Hilbert class polynomial H_{-24} = x^2 - 4834944 x + 14670139392; its roots mod 7 are 4, 5, simple (canonical lifts in Z_7 by Hensel)",
      hcp[0] == [1, -4834944, 14670139392] and sorted(hcp[1]) == [4, 5] and hcp[2] != 0)
jn = gpval(d["JNUM"][0])
red = gpval(d["RED"][0])
jO = {s: (red[0] + red[1] * s) % 7 for s in red[2]}
check("C7 j(sqrt(-6)) = 2417472 + 1707264 sqrt2 (lattice O, form (1,0,6)) and j(sqrt(-6)/2) = 2417472 - 1707264 sqrt2 (lattice p2, form (2,0,3)), numerically",
      jn[0] == 1 and jn[1] == 1, f"j(O) = {jn[2]}, j(p2) = {jn[3]}")
check("C8 j(O) = 1 - sqrt2 mod 7: it reduces to 5 if the 7-adic sqrt2 = 3 mod 7 is sent to +sqrt2 by epsilon, to 4 if sqrt2 = 4 mod 7 is; "
      "so which curve is principal depends on epsilon", red[:2] == [1, 6] and jO == {3: 5, 4: 4}, f"{{sqrt2 mod 7: j(O) mod 7}} = {jO}")


def stable_sublattices(M, l):
    """M-stable sublattices of index l (prime) in Z^2, with the reduced Latimer-MacDuffee form of the induced step"""
    bases = [sp.Matrix([[l, j], [0, 1]]) for j in range(l)] + [sp.Matrix([[1, 0], [0, l]])]
    res = []
    for B in bases:
        Mp = B.inv() * M * B
        if all(x.is_integer for x in Mp):
            res.append(reduce_form(weil_form(Mp, a)))
    return res


s1 = {l: stable_sublattices(M1, l) for l in (2, 3, 5)}
s2 = {l: stable_sublattices(M2, l) for l in (2, 3, 5)}
check("C9 lattice side: the (1,0,6) lattice has exactly one M-stable sublattice of index 2 and one of index 3, each of class (2,0,3); "
      "and conversely from (2,0,3) back to (1,0,6)",
      s1[2] == [F203] and s1[3] == [F203] and s2[2] == [F106] and s2[3] == [F106],
      f"index 5: {s1[5]} from (1,0,6), {s2[5]} from (2,0,3)")

# ------------------------------------------------------------------------------------------------------------
print("\n== R. The overlap function <Theta_K, 1_D> = 7^{h^0(D)}: brute-force h^0 versus Riemann-Roch + Abel-Jacobi (level F_7)")
out = gp(r"""
foreach([[3,3],[1,3]],c, R=allpts(c[1],c[2],6); print("RC|",concat([c],rcheck(c[1],c[2],R,6))));
""")
rc = [gpval(s) for s in lines(out)["RC"]]
for r in rc:
    check(f"R1 E{4 if r[0] == [3, 3] else 5}: h^0(nO - E) by linear algebra on L(nO) = Riemann-Roch + Abel-Jacobi on all {r[3]} divisors "
          f"(E = one or two places, degrees <= 3, deg E <= 4; n = deg E - 1, deg E, deg E + 1)",
          r[4] == 0, f"places of degree 1,2,3 (affine): {r[2]}; degree-0 divisors {r[5]}, of which principal {r[6]}")
check("R2 the two curves have the same number of affine places of each degree <= 3 and the same number of principal divisors in the sample",
      rc[0][2] == rc[1][2] and rc[0][6] == rc[1][6])

# ------------------------------------------------------------------------------------------------------------
print("\n== O. The overlap data of E4 and E5 agree at every level tested")
out = gp(r"""
R4=allpts(3,3,4); R5=allpts(1,3,4);
foreach([[1,1],[1,2],[2,1],[2,2]],kd, print("FB|",[4,kd[1],kd[2],fibres(3,3,4,kd[1],kd[2],R4),fibres(1,3,4,kd[1],kd[2],R5)]));
R4=allpts(3,3,6); R5=allpts(1,3,6);
foreach([[1,3],[2,3],[3,1],[3,2]],kd, print("FB|",[6,kd[1],kd[2],fibres(3,3,6,kd[1],kd[2],R4),fibres(1,3,6,kd[1],kd[2],R5)]));
""")
for s in lines(out)["FB"]:
    m, k, dd, f4, f5 = gpval(s)
    pairs = sum(x * x for x in f4[2])
    check(f"O1 over F_(7^{k}), places of degree {dd}: same number of places, same multiset of fibre sizes of Pic^{dd} = E(F_(7^{k})) (classes of effective"
          f" places), so the same number of pairs P ~ Q",
          f4 == f5, f"{f4[0]} places, #Pic^{dd} = {f4[1]}, ordered pairs (P,Q) with h^0(P-Q) = 1: {pairs}")
out = gp(r"""
print("PW|",PhiPointwise(4));
for(m=1,12, print("PT|",PhiTest(m))); print("PT|",PhiTest(18));
""")
d = lines(out)
pw = gpval(d["PW"][0])
check("O2 Phi = (2-isogeny on the odd part) + (3-isogeny on the 2-part) is a bijection E4(F_(7^4)) -> E5(F_(7^4)) commuting with Frobenius, pointwise",
      pw[0] == pw[1] and pw[2] == 1, f"{pw[0]} points")
pts = [gpval(s) for s in d["PT"]]
check("O3 for m = 1..12 and 18: E4(F_(7^m)) = E5(F_(7^m)) as groups, and Phi is injective (nonzero on every line of every E4(F)[l]), additive and "
      "Frobenius-equivariant on random points", all(p[5] == 1 and p[2] == p[3] + [1] * (2 - len(p[3])) for p in pts),
      "groups " + "; ".join(f"m={p[0]}: {p[3]}" for p in pts[:4]) + "; ...; m=18: " + str(pts[-1][3]))

# ------------------------------------------------------------------------------------------------------------
print("\n== T. Lattice side: Z^2/N as Z[M]-modules, with and without the symplectic form (genus theory)")
NS = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 25, 27]
tdets = {}
for N in NS:
    tdets[N] = intertwiner_dets(M1, M2, N)
check("T1 for every N in " + str(NS) + " there is g in GL2(Z/N) with g M_(1,0,6) = M_(2,0,3) g: the two lattices are locally isomorphic as Z[F]-modules",
      all(tdets[N] for N in NS))
iso_plus = {N: (1 % N) in tdets[N] for N in NS}
iso_minus = {N: ((-1) % N) in tdets[N] for N in NS}
exp_plus = {N: not (N % 3 == 0 or N % 8 == 0) for N in NS}
exp_minus = {N: not (N % 8 == 0) for N in NS}
check("T2 a symplectic intertwiner (det g = 1, i.e. g^T Omega g = Omega) exists mod N exactly when 3 does not divide N and 8 does not divide N",
      iso_plus == exp_plus, "det sets: " + ", ".join(f"N={N}: {sorted(tdets[N])}" for N in (3, 4, 8, 9, 16)))
check("T3 an anti-symplectic intertwiner (det g = -1) exists mod N exactly when 8 does not divide N (so mod 3^k they differ only by the sign of Omega)",
      iso_minus == exp_minus)
v1 = {x * x + 6 * y * y for x in range(-12, 13) for y in range(-12, 13)}
v2 = {2 * x * x + 3 * y * y for x in range(-12, 13) for y in range(-12, 13)}
g1 = ({n % 8 for n in v1 if n % 2}, {n % 3 for n in v1 if n % 3})
g2 = ({n % 8 for n in v2 if n % 2}, {n % 3 for n in v2 if n % 3})
check("T4 the forms (1,0,6) and (2,0,3) are in different genera: odd values are {1,7} versus {3,5} mod 8, values prime to 3 are {1} versus {2} mod 3",
      g1 == ({1, 7}, {1}) and g2 == ({3, 5}, {2}), f"{g1} versus {g2}")

# ------------------------------------------------------------------------------------------------------------
print("\n== W. Curve side: Frobenius-equivariant isomorphisms E4[n] -> E5[n] and the Weil pairing")
cases = [(4, 2), (3, 3), (4, 4), (4, 5), (8, 8), (9, 9), (16, 16)]
out = gp("".join(f'print("PS|",pairscal({k},{n}));\n' for k, n in cases)
         + 'print("IS|",[isogscal(3,3,2),isogscal(8,8,3),isogscal(4,5,2),isogscal(4,5,3)]);\n')
d = lines(out)
ps = {}
for s in d["PS"]:
    # printed as [n, k, A4, A5, nint, S] with A4, A5 matrices "[a, b; c, d]": parse n, k first and nint, S last
    parts = s.split(", ")
    n, k = int(parts[0].strip("[")), int(parts[1])
    S = sorted(int(x) for x in s[s.rindex("[") + 1:s.rindex("]") - 1].split(",") if x.strip())
    nint = int(s[:s.rindex("[")].rstrip(", ").split(", ")[-1])
    ps[n] = (k, nint, S)
for n in [c[1] for c in cases]:
    k, nint, S = ps[n]
    check(f"W1 E[{n}] (rational over F_(7^{k})): the {nint} Frobenius-equivariant isomorphisms E4[{n}] -> E5[{n}] scale the Weil pairing by {S}; "
          f"equal to the lattice-side det set", set(S) == tdets[n] and nint > 0,
          ("no isometry" if 1 % n not in S else "isometries exist") + ("; no anti-isometry" if (-1) % n not in S else "; anti-isometries exist"))
check("W2 E[3]: every equivariant isomorphism scales e_3 by 2 = -1 (no isometry); E[8], E[16]: scalings are 3, 5 mod 8 (neither +1 nor -1)",
      ps[3][2] == [2] and ps[8][2] == [3, 5] and ps[16][2] == [3, 5, 11, 13])
isg = gpval(d["IS"][0])
check("W3 e5(phi x, phi y) = e4(x, y)^(deg phi): 2-isogeny on E[3] gives 2, 3-isogeny on E[8] gives 3, both on E[5] give 2 and 3",
      isg == [2, 3, 2, 3], f"{isg}")

# ------------------------------------------------------------------------------------------------------------
print("\n== P. The Pauli-six pair (q = 5, a = -2): different orders, and the overlaps see it")
out = gp(r"""
pp=5;
foreach([0,1],b, E=ellinit([4,b]*Mod(1,5)); print("E2|",[b, ellap(E), lift(E.j), ellgroup(E), #polrootsmod('x^3+4*'x+b,5)]));
{foreach([0,1],b, R=allpts(4,b,1); Ef=ellinit([4,b],R[1]); pr=0; bad=0; np=0;
  for(i=1,#R[2],for(j=i+1,#R[2], np++; h=h0bf(2,[R[2][i],R[2][j]]); if(h!=h0rr(Ef,2,[R[2][i],R[2][j]]),bad++); pr+=h));
  print("PR|",[b,#R[2],np,pr,bad]));}
""")
d = lines(out)
e2 = {x[0]: x for x in (gpval(s) for s in d["E2"])}
check("P1 y^2 = x^3 + 4x (j = 1728 = 3 mod 5) has E(F_5) = Z2 x Z4; y^2 = x^3 + 4x + 1 (j = 1) has Z8; both have trace -2",
      e2[0][1:4] == [-2, 3, [4, 2]] and e2[1][1:4] == [-2, 1, [8]])
check("P2 E[2] is F_5-rational for b = 0 (x^3 + 4x has 3 roots) and not for b = 1 (1 root): (pi - 1)/2 is an endomorphism only for b = 0",
      e2[0][4] == 3 and e2[1][4] == 1)
pr = {x[0]: x for x in (gpval(s) for s in d["PR"])}
check("P3 overlap statistic at level F_5: the number of pairs {P,Q} of distinct affine rational points with h^0(2O - P - Q) = 1 is 2 for b = 0 and 3 for b = 1 "
      "(brute-force linear algebra, agreeing with Riemann-Roch + Abel-Jacobi): the degree-0 overlaps distinguish the pair",
      pr[0][3] == 2 and pr[1][3] == 3 and pr[0][4] == 0 and pr[1][4] == 0, f"{pr}")
qa, aa = 5, -2
P104, P202 = form_to_step((1, 0, 4), aa), form_to_step((2, 0, 2), aa)
half = lambda M: (M - sp.eye(2)) / 2
check("P4 lattice side: (M - 1)/2 is integral on the (2,0,2) lattice (multiplier ring Z[(pi-1)/2] = Z[i]) and not on (1,0,4) (multiplier ring Z[pi] = Z[2i])",
      all(x.is_integer for x in half(P202)) and not all(x.is_integer for x in half(P104)))
dE2 = {N: intertwiner_dets(P104, P202, N) for N in (2, 3, 4, 5, 7, 9)}
check("P5 the Z[M]-modules of (1,0,4) and (2,0,2) are non-isomorphic mod 2 and mod 4, isomorphic mod 3, 5, 7, 9: the difference is local, at the conductor 2",
      not dE2[2] and not dE2[4] and all(dE2[N] for N in (3, 5, 7, 9)))

print(f"\n{npass} of {npass + nfail} pass")
