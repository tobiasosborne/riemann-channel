t=ffgen(5^2,'t); E=ellinit([0,0,0,4,0],t); pts=List();
{for(a=0,4,for(b=0,4, x=a+b*t; r=x^3+4*x; for(c=0,4,for(d=0,4, y=c+d*t; if(y^2==r, listput(pts,[x,y]))))));}
nbad=0;
{for(i=1,#pts, P=pts[i]; F=[P[1]^5,P[2]^5]; J=[-P[1],2*P[2]]; R=elladd(E, ellneg(E,P), ellmul(E,J,-2)); if(F!=R, nbad++));}
print("affine points over F_25: ", #pts, "  Frobenius != -1 - 2 iota at ", nbad, " points");
print("#E(F_5) = ", ellcard(ellinit([0,0,0,4,0],ffgen(5,'u))), "  #E(F_25) = ", ellcard(E));
