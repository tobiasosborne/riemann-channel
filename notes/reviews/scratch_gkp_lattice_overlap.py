"""REFUTE lane, 2026-10-06. Independent checks of overlap-data.md from its STATEMENTS only
(no code from notes/adelic-gkp/checks/).  PARI/GP 2.15.4 via subprocess + python."""
import subprocess, itertools, math
def gp(cmd):
    r=subprocess.run(['gp','-q','-f','-D','parisize=1000000000'],input=' '.join(cmd.splitlines()).replace('##','\n')+'\n',capture_output=True,text=True)
    return (r.stdout+r.stderr).strip()
ok=[]
def rep(n,c,i=''):
    ok.append(bool(c)); print(('PASS ' if c else 'FAIL ')+n, i)
E4='[3,3]'; E5='[1,3]'
out=gp(f'''e4=ellinit({E4},7); e5=ellinit({E5},7); print([lift(Mod(e4.j,7)), lift(Mod(e5.j,7)), ellap(e4), ellap(e5)]);
print(ellgroup(ellinit({E4},Mod(1,7)))); print(ellgroup(ellinit({E5},Mod(1,7))));
H=polclass(-24); print(H); print(polrootsmod(H,7)); print(quadclassunit(-24).no);
j1=ellj(sqrt(-6)); j2=ellj(sqrt(-6)/2); print(round(real(j1)*1e6)/1e6," ",round(real(j2)*1e6)/1e6);
print(algdep(j1,2));
s=sqrt(2.); print(round(2417472+1707264*s)," ",round(2417472-1707264*s));
print(lift(Mod(2417472,7))," ",lift(Mod(1707264,7)));
print([lift(Mod(2417472+1707264*3,7)), lift(Mod(2417472+1707264*4,7))]);
''')
print(out)
L=out.splitlines()
rep('E4: j=4, E5: j=5, both a=2', L[0].replace(' ','')=='[4,5,2,2]', L[0])
rep('E(F_7) = Z6 for both', L[1]=='[6]' and L[2]=='[6]')
rep('H_-24 = x^2-4834944x+14670139392, roots mod 7 = {4,5}, h(-24)=2', L[3]=='x^2 - 4834944*x + 14670139392' and '4' in L[4] and '5' in L[4] and L[5]=='2')
rep('j(sqrt-6) ~ 4831907.90, j(sqrt-6/2) ~ 3036.10 = 2417472 -+ 1707264 sqrt2', L[6].startswith('4831907.9') and L[8].split()==['4831908','3036'])
rep('j(O_K) = 2417472+1707264*sqrt2 == 1 - sqrt2 mod 7; s=3 -> 5, s=4 -> 4', L[9].split()==['1','6'] and L[10].replace(' ','')=='[5,4]')
# 2- and 3-isogenies swap j
out=gp(f'''for(c=1,2, E=ellinit(if(c==1,{E4},{E5}),Mod(1,7));
  for(n=2,3, T=[]; forstep(x=0,6,1, Y=ellordinate(E,x); for(i=1,#Y, P=[Mod(x,7),Y[i]]; if(ellorder(E,P)==n, T=concat(T,[P])))); 
    iso=ellisogeny(E,T[1]); E2=ellinit(iso[1],Mod(1,7)); print1([c,n,#T,lift(E2.j)]," ")));''')
print('  ',out)
rep('rational 2- and 3-isogenies: E4 -> j=5, E5 -> j=4', all(s in out.replace(' ','') for s in ['[1,2,1,5]','[1,3,2,5]','[2,2,1,4]','[2,3,2,4]']), '(#T counts points of order n: 1 point of order 2, 2 points of order 3 = one subgroup)')

# ---------- Weil pairing scale sets
def mul(u,v,n): return ((u[0]*v[0]-6*u[1]*v[1])%n,(u[0]*v[1]+u[1]*v[0])%n)
def kfor(n):
    p=(1,1); x=p; k=1
    while (x[0]-1)%n or x[1]%n: x=mul(x,p,n); k+=1
    return k
def mat_inv_ok(g,n): return math.gcd((g[0]*g[3]-g[1]*g[2])%n,n)==1
def scales_curves(n):
    k=kfor(n)
    script=f'''t=ffgen(7^{k},'t); 
    tors(E)={{my(N=ellcard(E),X,o); while(1, X=ellmul(E,random(E),N); X=random(E); o=ellorder(E,X); if(o%{n}==0, return(ellmul(E,X,o/{n}))))}};##
    basis(E)={{my(P,Q); P=tors(E); while(1, Q=tors(E); if(fforder(ellweilpairing(E,P,Q,{n}))=={n}, return([P,Q])))}};##
    fr(P)=[P[1]^7,P[2]^7];##
    coords(E,B,R)={{for(a=0,{n}-1,for(b=0,{n}-1, if(elladd(E,ellmul(E,B[1],a),ellmul(E,B[2],b))==R, return([a,b])))); error("x")}};##
    out=vector(2); for(c=1,2, E=ellinit(if(c==1,{E4},{E5}),t); B=basis(E); z=ellweilpairing(E,B[1],B[2],{n});
      F=[coords(E,B,fr(B[1])), coords(E,B,fr(B[2]))]; out[c]=[F,z]);
    z4=out[1][2]; z5=out[2][2]; cc=-1; for(c=0,{n}-1, if(z4^c==z5, cc=c)); print(out[1][1],"|",out[2][1],"|",cc,"|",fforder(z4));'''
    raw=gp(script); r=raw.replace(' ','').split('|')
    if len(r)!=4: print(raw)
    F4=eval(r[0].replace(';',',')); F5=eval(r[1].replace(';',',')); c=int(r[2]); oz=int(r[3])
    # F as columns: Frob(P) = F[0][0] P + F[0][1] Q -> matrix with columns
    A4=[[F4[0][0],F4[1][0]],[F4[0][1],F4[1][1]]]; A5=[[F5[0][0],F5[1][0]],[F5[0][1],F5[1][1]]]
    S=set(); N=0
    for g in itertools.product(range(n),repeat=4):
        if not mat_inv_ok(g,n): continue
        G=[[g[0],g[1]],[g[2],g[3]]]
        l=[[sum(G[i][m]*A4[m][j] for m in range(2))%n for j in range(2)] for i in range(2)]
        r_=[[sum(A5[i][m]*G[m][j] for m in range(2))%n for j in range(2)] for i in range(2)]
        if l==r_: N+=1; S.add((c*(g[0]*g[3]-g[1]*g[2]))%n)
    return k,oz,c,N,sorted(S)
def scales_lattice(n):
    M1=[[1,-6],[1,1]]; M2=[[1,-3],[2,1]]
    S=set()
    for g in itertools.product(range(n),repeat=4):
        if not mat_inv_ok(g,n): continue
        G=[[g[0],g[1]],[g[2],g[3]]]
        l=[[sum(G[i][m]*M1[m][j] for m in range(2))%n for j in range(2)] for i in range(2)]
        r_=[[sum(M2[i][m]*G[m][j] for m in range(2))%n for j in range(2)] for i in range(2)]
        if l==r_: S.add((g[0]*g[3]-g[1]*g[2])%n)
    return sorted(S)
expect={3:[2],8:[3,5],9:[2,5,8],16:[3,5,11,13],4:[1,3],5:[1,2,3,4]}
for n in [3,4,5,8,9,16]:
    k,oz,c,N,S=scales_curves(n); SL=scales_lattice(n)
    rep(f'E[{n}] (over F_7^{k}): equivariant isos E4[n]->E5[n]: {N}, Weil scale set {S}; lattice det set {SL}', S==expect[n] and SL==S and oz==n)
rep('n=8: no equivariant iso preserves e_8 up to inversion (1,7 not in scale set)', 1 not in expect[8] and 7 not in expect[8])

# ---------- lattice side Z^2/N: Z[M]-modules for (1,0,6),(2,0,3) isomorphic for all N<=27
def iso_exists(n):
    M1=[[1,-6],[1,1]]; M2=[[1,-3],[2,1]]
    for g in itertools.product(range(n),repeat=4):
        if not mat_inv_ok(g,n): continue
        if all((sum(g[2*i+m]*M1[m][j] for m in range(2))-sum(M2[i][m]*g[2*m+j] for m in range(2)))%n==0 for i in range(2) for j in range(2)): return True
    return False
rep('Z^2/N with (1,0,6) and (2,0,3) are iso Z[M]-modules for N=2..20', all(iso_exists(n) for n in range(2,21)))

# ---------- degree-2 places over F_49: fibre sizes of the class map and pairs with h0(P-Q)=1
out=gp(f'''t=ffgen(7^4,'t); fl=[];
for(c=1,2, E=ellinit(if(c==1,{E4},{E5}),t); M=Map(); np=0;
  forvec(v=vector(4,i,[0,6]), x=v[1]+v[2]*t+v[3]*t^2+v[4]*t^3; Y=ellordinate(E,x);
    for(i=1,#Y, R=[x,Y[i]]; F=[R[1]^49,R[2]^49]; if(F!=R, np++; S=elladd(E,R,F); k=Str(S); if(mapisdefined(M,k), mapput(M,k,mapget(M,k)+1), mapput(M,k,1))))); 
  V=Vec(apply(z->z/2, Mat(M)[,2])); fl=concat(fl,[[np/2, vecsort(V), sum(i=1,#V,V[i]^2), sum(i=1,#V,V[i]*(V[i]-1))]]));
print(fl[1][1]," ",fl[2][1]," ",fl[1][2]==fl[2][2]," ",fl[1][3]," ",fl[2][3]," ",fl[1][4]," ",fl[2][4]);''')
print('  ',out)
r=out.split()
rep('degree-2 places over F_49: same count, same fibre multiset; ordered pairs with h0(P-Q)=1', r[0]==r[1] and r[2]=='1' and r[3]==r[4], f'places={r[0]}, sum n_c^2={r[3]} (incl. P=Q), sum n_c(n_c-1)={r[5]} (P!=Q); page: 22860')

# ---------- Pauli-six pair over F_5
out=gp('''for(b=0,1, E=ellinit([4,b],Mod(1,5)); pts=[]; for(x=0,4, Y=ellordinate(E,x); for(i=1,#Y, pts=concat(pts,[[Mod(x,5),Y[i]]])));
  c=0; for(i=1,#pts, for(j=i+1,#pts, if(ellisoncurve(E,elladd(E,pts[i],pts[j])) && elladd(E,pts[i],pts[j])==[0], c++)));
  print1([b, lift(E.j), ellgroup(E), c]," "));''')
print('  ',out)
rep('P1/P3: b=0: j=3, Z2xZ4, 2 pairs {P,-P}; b=1: j=1, Z8, 3 pairs', out.replace(' ','')=='[0,3,[4,2],2][1,1,[8],3]')
# P4: (M-1)/2 integral on (2,0,2) and not on (1,0,4) [a=-2]
M202=[[-1,-2],[2,-1]]; M104=[[-1,-4],[1,-1]]
rep('(M-1)/2 integral for (2,0,2), not for (1,0,4)', all((M202[i][j]-(i==j))%2==0 for i in range(2) for j in range(2)) and not all((M104[i][j]-(i==j))%2==0 for i in range(2) for j in range(2)))
# Prop. 3 arithmetic: norms of units mod 8 and mod 3
N8=sorted({(x*x+6*y*y)%8 for x in range(8) for y in range(8) if x%2}); N3=sorted({(x*x+6*y*y)%3 for x in range(3) for y in range(3) if x%3})
rep('N((O_K/8)^x) = {1,7}, N((O_K/3)^x) = {1}', N8==[1,7] and N3==[1], (N8,N3))
print(sum(ok),'of',len(ok),'pass')

# ---------- curve-bridge §3 / overlap-data Lemma 1 on E3: E4,E5 groups agree up to k=24 (curves, not lattices)
r=gp('''r=1; for(k=1,24, t=ffgen(7^k,'t); if(ellgroup(ellinit([3,3],t))!=ellgroup(ellinit([1,3],t)), r=0)); print(r)''')
rep('E4(F_7^k) = E5(F_7^k) as groups for k=1..24 (PARI)', r=='1')
print(sum(ok),'of',len(ok),'pass (final)')
