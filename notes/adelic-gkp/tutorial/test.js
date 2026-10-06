const C = require('./core.js');
const eq = (a,b)=>JSON.stringify(a)===JSON.stringify(b);
let fails=0; const chk=(name,ok,detail='')=>{ if(!ok) fails++; console.log((ok?'PASS ':'FAIL ')+name+(detail?'  '+detail:'')); };
const r=(x,d=4)=>Math.round(x*10**d)/10**d;
// spectra
const K4=C.graph('K4'); chk('K4 spectrum', eq(C.eigSym(K4.A).map(x=>r(x)),[-1,-1,-1,3]));
const P=C.graph('petersen'); chk('Petersen spectrum', eq(C.eigSym(P.A).map(x=>r(x)),[-2,-2,-2,-2,1,1,1,1,1,3]));
const K5=C.graph('K5'); chk('K5 q=3', K5.q===3);
const cube=C.graph('cube'); chk('cube spectrum', eq(C.eigSym(cube.A).map(x=>r(x)),[-3,-1,-1,-1,1,1,1,3]));
const pr=C.graph('prism21'); const lp=C.eigSym(pr.A); chk('prism21 largest nontrivial |lambda| = 2.9777', r(Math.max(...lp.filter(x=>Math.abs(Math.abs(x)-3)>1e-9).map(Math.abs)))===2.9777, String(r(lp[0]))+' '+String(r(lp[lp.length-2])));
chk('prism21 negIndex 5', C.negIndexQ(lp,2)===5);
// Hashimoto traces
const {B}=C.hashimoto(K4,null); const N=C.traces(B,8); chk('K4 N_k', eq(N.slice(1),[0,0,24,24,0,96,168,168]), N.join(','));
chk('K4 primes', eq(C.primeCounts(N).slice(3),[8,6,0,12,24,18]));
// Ihara poly
const ip=C.iharaPoly(K4.A,2); const expect=C.polyMul(C.polyMul([1,-1],[1,-2]), C.polyMul(C.polyMul([1,1,2],[1,1,2]),[1,1,2])); chk('K4 det(1-Au+2u^2)=(1-u)(1-2u)(1+u+2u^2)^3', eq(ip,expect), C.polyFormat(ip));
// Ihara-Bass: sum mu^k + (|E|-|V|)(1+(-1)^k) = N_k
const mus=C.lines(C.eigSym(K4.A),2); let ok=true; for(let k=1;k<=8;k++){ let s=0; for(const m of mus){ // mu^k real part sum
 const rr=Math.hypot(m.re,m.im), th=Math.atan2(m.im,m.re); s+=Math.pow(rr,k)*Math.cos(k*th);} s+=2*(1+(-1)**k); if(Math.abs(s-N[k])>1e-6) ok=false;} chk('Ihara-Bass K4 trace formula',ok);
// signed K4 one negative edge (edge index 3 = [1,2])
const signs=[1,1,1,-1,1,1]; const As=C.signedA(K4,signs); chk('K4 one neg edge spectrum', eq(C.eigSym(As).map(x=>r(x)),[-2.2361,-1,1,2.2361]));
const {B:Bs}=C.hashimoto(K4,signs); const Ns=C.traces(Bs,8); const ev=[],od=[]; for(let k=3;k<=8;k++){ev.push((N[k]+Ns[k])/2); od.push((N[k]-Ns[k])/2);} chk('K4 even/odd counts', eq(ev,[12,8,0,48,84,72])&&eq(od,[12,16,0,48,84,96]), ev+' | '+od);
chk('fermionic Qmin 0.2753', r(C.fermionicQmin(C.eigSym(As),2))===0.2753);
// all negative -> cube spectrum
const Aneg=C.signedA(K4,[-1,-1,-1,-1,-1,-1]); chk('K4 all negative spectrum -3,1,1,1', eq(C.eigSym(Aneg).map(x=>r(x)),[-3,1,1,1]));
// matching polynomial & flux average
const mp=C.matchingPoly(K4); chk('K4 matching poly x^4-6x^2+3', eq(mp,[3,0,-6,0,1]), mp.join(','));
const fa=C.fluxAverageCharpoly(K4); chk('K4 flux avg = matching, 8 classes, 6 in band', eq(fa.avg.map(Math.round),mp)&&fa.count===8&&fa.inBand===6, fa.avg+' '+fa.count+' '+fa.inBand);
const faP=C.fluxAverageCharpoly(P); const mpP=C.matchingPoly(P); chk('Petersen flux avg = matching 64 classes 62 in band', eq(faP.avg.map(Math.round),mpP)&&faP.count===64&&faP.inBand===62, mpP.join(',')+' '+faP.inBand);
chk('Petersen matching largest root 2.6314', r(Math.max(...C.realRoots(mpP,-4,4)))===2.6314);
const fa5=C.fluxAverageCharpoly(K5); const mp5=C.matchingPoly(K5); chk('K5 matching x^5-10x^3+15x, 62/64', eq(mp5,[0,15,0,-10,0,1])&&eq(fa5.avg.map(Math.round),mp5)&&fa5.inBand===62, mp5.join(',')+' '+fa5.inBand);
// homology walks on K4 (centre 0; cotree = outer triangle)
const co=C.cotree(K4); chk('K4 cotree has 3 edges', co.length===3, co.join(','));
const hw=C.homologyWalks(K4,co,6); const tot=hw.reduce((s,p)=>s+p.c,0); chk('k=6: 96 walks on 20 points', tot===96&&hw.length===20, tot+' '+hw.length);
// Z2 flux = half period: signs on cotree edges a=(1,0,1)
const a=[1,0,1]; const sg=Array(6).fill(1); co.forEach((ei,j)=>{ if(a[j]) sg[ei]=-1; }); const {B:Bsa}=C.hashimoto(K4,sg); const Nsa=C.traces(Bsa,8); let okh=true; for(let k=3;k<=8;k++){ const h=C.homologyWalks(K4,co,k); const s=h.reduce((t,p)=>t+p.c*((a[0]*p.x[0]+a[1]*p.x[1]+a[2]*p.x[2])%2?-1:1),0); if(s!==Nsa[k]) okh=false;} chk('sign of walk = (-1)^(a.x)', okh);
// periodic points of the E mode
const pc=[1,2,3,4,5,6,7].map(k=>C.periodicPoints(2,-1,k).h); chk('E mode periodic points 4,8,4,16,44,56,116', eq(pc,[4,8,4,16,44,56,116]), pc.join(','));
const o6=C.periodicPoints(2,-1,6).orbits.map(o=>o.length).sort((x,y)=>x-y); chk('E mode k=6 orbits 1x4,2x2,6x8', eq(o6,[1,1,1,1,2,2,6,6,6,6,6,6,6,6]), o6.join(','));
chk('E mode h_k recursion', eq(C.pointCounts(2,-1,8).h.slice(1),[4,8,4,16,44,56,116,288]));
const p5=[1,2,3,4].map(k=>C.periodicPoints(5,-2,k).h); chk('Pauli six 8,32,104,640', eq(p5,[8,32,104,640]), p5.join(','));
const ph=[1,2,3,4,5].map(k=>C.periodicPoints(5,5,k).h); chk('hyperbolic 1,11,76,451,2501', eq(ph,[1,11,76,451,2501]), ph.join(','));
// prism21 Hashimoto traces feasibility and echo
const t0=Date.now(); const {B:Bp}=C.hashimoto(pr,null); const Np=C.traces(Bp,14); console.log('prism traces time ms', Date.now()-t0, Np.slice(1,8).join(','));
console.log(fails? fails+' FAILED':'all passed');
