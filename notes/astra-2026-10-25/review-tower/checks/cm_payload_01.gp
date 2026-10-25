
setrand(20261006);
\\ l-primary part of E(F_{p^k}): invariants o1 >= o2 and a basis (random points; independence by the Weil pairing)
lpart(E,l)={my(cyc=ellgroup(E),Nn=ellcard(E),co,os,g1,x,P,z);
  os=select(o->o>1, apply(d->l^valuation(d,l), cyc)); co=Nn/l^valuation(Nn,l);
  until(ellorder(E,g1)==os[1], g1=ellmul(E,random(E),co));
  if(#os==1, return([os,[g1]]));
  P=ellmul(E,g1,os[1]/os[2]);
  while(1, x=ellmul(E,random(E),co); if(ellorder(E,x)!=os[2], next); z=ellweilpairing(E,P,x,os[2]); if(fforder(z)==os[2], break));
  [os,[g1,x]]};
frob(P,q)=if(#P<2,P,[P[1]^q,P[2]^q]);
\\ coordinates of R in the basis gs (orders os), brute force
coords(E,R,os,gs)={my(S,T);
  if(#os==1, T=[0]; for(a=0,os[1]-1, if(T==R, return([a])); T=elladd(E,T,gs[1])); error("nc1"));
  S=[0]; for(a=0,os[1]-1, T=S; for(b=0,os[2]-1, if(T==R, return([a,b])); T=elladd(E,T,gs[2])); S=elladd(E,S,gs[1])); error("nc2")};
dlogmu(z,w,N)={for(j=0,N-1, if(w^j==z, return(j))); error("dlog")};
\\ omega_N.  nm = 7: w8 + 1/w8 = 3, w4 = w8^2, w2 = -1, w3 = 4.  nm = -7: w8 + 1/w8 = 4.  else: a power of ffprimroot
omg(t,N,nm)={my(Q=t.p^t.f,g=ffprimroot(t),w,z);
  if(N==2, return(-1*t^0));
  if(nm==7 && (N==8 || N==4), z=g^((Q-1)/8); w=0;
     forstep(j=1,7,2, if(z^j+z^(-j)==3, w=z^j; break)); return(w^(8/N)));
  if(nm==-7 && N==8, z=g^((Q-1)/8); forstep(j=1,7,2, if(z^j+z^(-j)==4, return(z^j))));
  if(nm==7 && N==3, return(4*t^0));
  if(nm==7 && N==16, w=omg(t,8,7); z=g^((Q-1)/16); for(j=1,15, if((z^j)^2==w, return(z^j))));
  g^((Q-1)/N)};
\\ [invariants, Frobenius columns, Tate exponents m[i][j] = log t_N(p_i, g_j) (reduced), Weil exponent log e_N(p_1, p_2) or -1, ellgroup, check w+1/w]
cdata(ai,p,k,l,N,nm)={my(t=ffgen(p^k,'t),E=ellinit(ai,t),LP=lpart(E,l),os=LP[1],gs=LP[2],r=#os,F,ps,w,Tm,We=-1,Q=p^k);
  F=vector(r,j,coords(E,frob(gs[j],p),os,gs));
  ps=vector(r,i,ellmul(E,gs[i],os[i]/min(os[i],N)));
  w=omg(t,N,nm);
  Tm=if((Q-1)%N==0, vector(r,i,vector(r,j, dlogmu(elltatepairing(E,ps[i],gs[j],N)^((Q-1)/N),w,N))), -1);
  if(r==2 && os[1]>=N && os[2]>=N, We=dlogmu(ellweilpairing(E,ps[1],ps[2],N),w,N));
  [os,F,Tm,We,ellgroup(E),fforder(w)]};
E=ellinit([1, -1, 1, -20, 46]); t=ffgen(2^1,'t); Et=ellinit(vector(5,i,E[i]),t); print("grp|", ellgroup(Et)); print("card|", ellcard(Et));