#!/usr/bin/env python3
"""Symbolic Casoratian and constructive finite-cylinder Poisson inversion."""
import math
import numpy as np
import sympy as sp


def symbolic():
    p,lam=sp.symbols('p lambda',real=True)
    a,b=sp.symbols('alpha beta')
    Om=sp.Matrix([[0,1],[-1,0]])
    M=sp.Matrix([[lam,-p],[1,0]])
    V=p*M.inv()
    Q=sp.simplify(Om*(M-V)/2)
    assert M.T*Om*M==p*Om
    print('Binding convention M=',M,'Omega=',Om,'V=',V,'Weil Q=',Q)
    print('det(Q)=',sp.factor(Q.det()))
    C=sp.Matrix([[a,b],[1,1]])
    print('Characteristic-coordinate Omega=',sp.simplify(C.T*Om*C))
    Qchar=sp.simplify(C.T*Q.subs({lam:a+b,p:a*b})*C)
    print('Characteristic-coordinate Q=',Qchar)
    assert sp.simplify(Qchar-sp.Matrix([[0,-(a-b)**2/2],[-(a-b)**2/2,0]]))==sp.zeros(2)
    print('General Casoratian p^-n*(f_(n+1)g_n-f_n g_(n+1)) is constant; for alpha^n,beta^n it is alpha-beta.')
    endpoint=Q.subs({p:3,lam:2*sp.sqrt(3)})
    print('Endpoint p=3, lambda=2sqrt(3): Q=',endpoint,'rank=',endpoint.rank(),'det=',endpoint.det())


def tree_paths(adj,R):
    levels=[[(0,)]]
    for n in range(R):
        lev=[]
        for path in levels[-1]:
            for v in adj[path[-1]]:
                if len(path)==1 or v!=path[-2]:
                    lev.append(path+(v,))
        levels.append(lev)
    return levels


def height(path,leaf):
    common=0
    for a,b in zip(path[1:],leaf[1:]):
        if a!=b:
            break
        common+=1
    return 2*common-(len(path)-1)


def kernel(paths,leaves,a):
    return np.array([[a**height(path,leaf) for leaf in leaves] for path in paths],complex)


def cylinder_data(F,a,levels):
    R=len(levels)-1
    return np.array([a**(-(R-1))*(F[path[-1]]-F[path[-2]]/a)/(a-1/a) for path in levels[-1]],complex)


def check_poisson(adj,p,lam,F,R=4):
    a,b=np.roots([1,-lam,p]).astype(complex)
    if a.imag<b.imag:
        a,b=b,a
    levels=tree_paths(adj,R)
    paths=[path for lev in levels for path in lev]
    leaves=levels[-1]
    ma=cylinder_data(F,a,levels)
    mb=cylinder_data(F,b,levels)
    Ka,Kb=kernel(paths,leaves,a),kernel(paths,leaves,b)
    expected=np.array([F[path[-1]] for path in paths])
    err=max(np.max(np.abs(Ka@ma-expected)),np.max(np.abs(Kb@mb-expected)))
    masserr=max(abs(sum(ma)-F[0]),abs(sum(mb)-F[0]))
    add_err=0.0
    for n in range(1,R):
        for path in levels[n]:
            actual=sum(ma[j] for j,leaf in enumerate(leaves) if leaf[:n+1]==path)
            target=a**(-(n-1))*(F[path[-1]]-F[path[-2]]/a)/(a-1/a)
            add_err=max(add_err,abs(actual-target))
    assert err<1e-11 and masserr<1e-11 and add_err<1e-11
    print(f'Poisson inverse: p={p}, lambda={lam:.17g}, alpha={a}, beta={b}, radius={R}, leaves={len(leaves)}, tested vertices={len(paths)}')
    print(f'reconstruction error={err:.18g}; root mass error={masserr:.18g}; cylinder additivity error={add_err:.18g}')
    # The normalised visual measure has equal mass on depth-R cones.
    visual=np.ones(len(leaves))/len(leaves)
    spherical_a=Ka@visual
    spherical_b=Kb@visual
    spherical_error=float(np.max(np.abs(spherical_a-spherical_b)))
    ray=leaves[0]
    fa=[]
    fb=[]
    for n in range(R+1):
        i=paths.index(ray[:n+1])
        fa.append(p**n*spherical_a[i])
        fb.append(p**n*spherical_b[i])
    wronskians=[p**(-n)*(fa[n+1]*fb[n]-fa[n]*fb[n+1]) for n in range(R)]
    plane=[p**(-n)*(a**(n+1)*b**n-a**n*b**(n+1)) for n in range(R)]
    assert spherical_error<1e-11 and max(abs(w) for w in wronskians)<1e-10
    assert max(abs(w-(a-b)) for w in plane)<1e-10
    print(f'Spherical P_alpha(visual)=P_beta(visual) error={spherical_error:.18g}')
    print('Radial spherical Casoratians (zero)=',wronskians)
    print('Horocyclic plane-wave Casoratians=',plane,'expected alpha-beta=',a-b)
    return a,b,levels,ma,mb


def in_band():
    p=3
    adj=[[j for j in range(5) if i!=j] for i in range(5)]
    e=np.array([1,-1,0,0,0],float)/math.sqrt(2)
    f=np.array([1,1,-2,0,0],float)/math.sqrt(6)
    F=e+1j*f
    a,b,levels,ma,_=check_poisson(adj,p,-1,F)
    ray=levels[-1][0]
    for n in range(5):
        heights=np.array([height(ray[:n+1],leaf) for leaf in levels[-1]])
        l2_squared=float(np.mean(p**heights.astype(float)))
        l1=float(np.mean(p**(heights.astype(float)/2)))
        formula=(1+(p-1)*n/(p+1))*p**(-n/2)
        assert abs(l2_squared-1)<1e-12 and abs(l1-formula)<1e-12
        print(f'Boundary kernel depth={n}: L2 norm squared={l2_squared:.17g}; L1 norm={l1:.17g}; exact L1 formula={formula:.17g}')
    norms=[]
    for n in range(1,5):
        mass=cylinder_data(F,a,levels[:n+1])
        norms.append(float(len(mass)*np.vdot(mass,mass).real))
    print('Squared L2 norms of depth-n conditional boundary densities for this graph mode, n=1..4=',norms)
    mb=cylinder_data(F.conjugate(),b,levels)
    reps=[(0,)]+[(0,j) for j in range(1,5)]
    Ka=kernel(reps,levels[-1],a)
    Kb=kernel(reps,levels[-1],b)
    boundary_pair=ma@(Ka.T@Kb)@mb
    x=a*F+b*F.conjugate()
    y=F+F.conjugate()
    direct=float(np.real(np.dot(x,x)+np.dot(x,y)+3*np.dot(y,y)))
    transported=-(a-b)**2*boundary_pair
    assert abs(direct-22)<1e-11 and abs(transported-22)<1e-11
    print(f'K5 nontrivial lambda=-1: 4p-lambda^2=11, ||F_plus||^2=2, direct Weil Q={direct:.17g}, boundary Q={transported}, exact expected=22')


def out_of_band():
    # The 4-regular graph C_12 square C_3; nontrivial eigenvalue 2+sqrt(3).
    vertices=[(i,j) for i in range(12) for j in range(3)]
    ids={v:i for i,v in enumerate(vertices)}
    adj=[]
    for i,j in vertices:
        adj.append([ids[((i+1)%12,j)],ids[((i-1)%12,j)],ids[(i,(j+1)%3)],ids[(i,(j-1)%3)]])
    F=np.array([math.cos(2*math.pi*i/12) for i,j in vertices])
    F=F/np.linalg.norm(F)
    lam=2+math.sqrt(3)
    assert abs(sum(F))<1e-12
    assert max(abs(sum(F[j] for j in adj[i])-lam*F[i]) for i in range(36))<1e-12
    a,b,levels,ma,mb=check_poisson(adj,3,lam,F)
    x=(a+b)*F
    y=2*F
    direct=float(np.real(np.dot(x,x)-lam*np.dot(x,y)+3*np.dot(y,y)))
    exact=5-4*sp.sqrt(3)
    assert abs(direct-float(exact))<1e-11 and direct<0
    print('Nontrivial counterexample to automatic boundary positivity: C12 x C3, vertices=36, degree=4, lambda=2+sqrt(3)=',f'{lam:.17g}')
    print('Weil value for F_plus=F_minus=unit eigenvector: exact=',exact,'decimal=',f'{direct:.17g}')


if __name__=='__main__':
    symbolic()
    in_band()
    out_of_band()
