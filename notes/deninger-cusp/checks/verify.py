# Author: codex:gpt-6-astra
"""Reproducible checks; all output is stdout, no generated data files."""
import mpmath as mp
import sympy as sp
mp.mp.dps = 45

def character(q, k, generator=None):
    g = generator or int(sp.primitive_root(q))
    c = [mp.mpc(0)] * q
    for j in range(q-1):
        c[pow(g,j,q)] = mp.exp(2j*mp.pi*k*j/(q-1))
    # make exact zeros and real signs stable
    return [mp.mpc(0) if abs(z)<mp.mpf('1e-40') else
            mp.mpc(mp.nint(z.real),0) if abs(z.imag)<mp.mpf('1e-40') and abs(z.real-mp.nint(z.real))<mp.mpf('1e-40') else z for z in c]

def L(u,c):
    if u == 1:
        # Cancel the common Hurwitz-zeta pole analytically, not numerically.
        q=len(c)
        return -sum(c[r]*mp.digamma(mp.mpf(r)/q) for r in range(1,q))/q
    return mp.dirichlet(u,c)

def lam(u,c):
    q=len(c); a=int(mp.nint((1-c[q-1].real)/2))
    return (q/mp.pi)**((u+a)/2)*mp.gamma((u+a)/2)*L(u,c)

def eps(c):
    q=len(c); a=int(mp.nint((1-c[-1].real)/2))
    return sum(c[r]*mp.exp(2j*mp.pi*r/q) for r in range(q))/(1j**a*mp.sqrt(q))

def A(s,c):
    return len(c)**(mp.mpf('.5')-s)*lam(2*s-1,c)/lam(2*s,c)

def Phi(s,c):
    cb=[mp.conj(v) for v in c]
    return mp.matrix([[0,A(s,c)],[A(s,cb),0]])

def theta(v,c,a=0):
    q=len(c)
    return sum((mp.mpf(n)**a)*c[n%q]*mp.exp(-mp.pi*n*n*v/q) for n in range(-65,66))

def theta_constant(y,t,c):
    return theta(t/y,c),mp.sqrt(y/t)*theta(t*y,c)

def phi0(s,q):
    def L0(u): return mp.pi**(-u/2)*mp.gamma(u/2)*mp.zeta(u)
    r=L0(2*s-1)/L0(2*s)
    d=q**(2*s)-1
    return r/d*mp.matrix([[q-1,q**s-q**(1-s)],[q**s-q**(1-s),q-1]])

def show(z): return mp.nstr(z,22)

if __name__=='__main__':
    pts=[mp.mpc('.7','.3'),mp.mpc('1.2','.4')]
    for q,k in [(5,2),(5,1),(7,2),(13,2)]:
        c=character(q,k);cb=[mp.conj(v) for v in c]
        print('character',q,k,'generator',sp.primitive_root(q),'parity',show(c[-1]),'epsilon',show(eps(c)))
        for s in pts:
            mat=Phi(s,c)
            err=mp.norm(mat*Phi(1-s,c)-mp.eye(2))
            print('s',show(s),'Phi_12',show(mat[0,1]),'Phi_21',show(mat[1,0]),'FE_error',show(err))
            assert err < mp.mpf('1e-38')
        y=mp.mpf('1.3');t=mp.mpf('.7')
        aa,bb=theta_constant(y,t,c)
        print('theta_CT_in_out',show(aa),show(bb))
        if c[-1].real > 0:
            err=abs(theta(t/y,c)-eps(c)*(t/y)**(-mp.mpf('.5'))*theta(y/t,cb))
            assert err<mp.mpf('1e-38')
            print('A_at_1',show(A(mp.mpf(1),c)),'residue',0)
            for w in [mp.mpc('.2','.4'),mp.mpc('2','.3')]:
                th=lam(1+2j*w,c)/lam(1-2j*w,cb)
                print('inner_point',show(w),'Theta',show(th),'modulus',show(abs(th)))
                assert abs(th)<1
        else:
            print('WARNING: Phi above is a formal completion-ratio matrix; weight-zero odd-character scattering does not exist.')
            print('odd_GL1_theta',show(theta(t/y,c,1)))
    q=5
    for s in pts:
        ph=phi0(s,q)
        print('trivial',q,'s',show(s),'diag',show(ph[0,0]),'offdiag',show(ph[0,1]),'FE',show(mp.norm(ph*phi0(1-s,q)-mp.eye(2))))
    print('residue_Gamma0_5_entry',show(3/(6*mp.pi)))
    print('residue_Gamma1_5_entry',show(6/(24*mp.pi)))
    c=character(5,2)
    def hardy(t): return mp.re(lam(mp.mpc('.5',t),c))
    roots=[]
    last=mp.mpf('0');lastv=hardy(last)
    for j in range(1,201):
        t=mp.mpf(j)/10; v=hardy(t)
        if lastv*v<0:
            rt=mp.findroot(hardy,(last,t))
            if not roots or abs(rt-roots[-1])>mp.mpf('1e-20'): roots.append(rt)
            if len(roots)==2: break
        last=t;lastv=v
    for gam in roots:
        rho=mp.mpc('.5',gam);w=mp.mpc(gam/2,'.25')
        print('quadratic5_zero',show(rho),'L_residual',show(abs(mp.dirichlet(rho,c))),'w',show(w),'mode_at_y_1.3',show(mp.mpf('1.3')**(-mp.mpf('.25')-1j*gam/2)))
    zeta=mp.exp(2j*mp.pi/5)
    for p in (2,3):
        e=1 if p==2 else 3
        vals=[mp.mpf(p+1)]
        for k in range(1,5):vals.extend([1+p*zeta**(e*k),p+zeta**(e*k)])
        print('Eis_N11_p',p,'eigenvalues',[show(v) for v in vals])
