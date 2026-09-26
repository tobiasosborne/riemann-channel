/* core.js -- shared helpers for "Weil Positivity, Contracted" (global window.WT).
 * Plain ES2020, no build step, no libraries. Every module reads colours through WT.col() so both
 * themes render correctly. Numerics: real symmetric eigenproblems by cyclic Jacobi; Hermitian ones
 * through the real 2n x 2n embedding; general complex eigenvalues (small matrices only) by the
 * Faddeev-LeVerrier characteristic polynomial and Durand-Kerner iteration with Newton polishing. */
(function(){
'use strict';
const WT = window.WT = window.WT || {};
WT.demos = WT.demos || {};

// ---------- DOM / SVG ----------
const $ = id => document.getElementById(id);
WT.$ = $;
const NS = 'http://www.w3.org/2000/svg';
const S = (tag, attrs, parent) => { const e = document.createElementNS(NS, tag); for (const k in (attrs||{})) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; };
const clear = el => { while (el && el.firstChild) el.removeChild(el.firstChild); };
const txt = (parent, x, y, s, attrs) => { const t = S('text', Object.assign({x, y}, attrs||{}), parent); t.textContent = s; return t; };
const polyline = (svg, pts, stroke, w, extra) => S('polyline', Object.assign({points: pts.map(p=>p[0].toFixed(2)+','+p[1].toFixed(2)).join(' '), fill:'none', stroke, 'stroke-width': w||1.5, 'stroke-linejoin':'round'}, extra||{}), svg);
const axis = (svg, x0, y0, x1, y1, cls) => S('line', {x1:x0, y1:y0, x2:x1, y2:y1, class: cls||'axis'}, svg);
WT.svg = { el: S, clear, text: txt, polyline, axis,
  /* a complex plane with the unit-ish circle of radius r (world units), scale sc px/unit, centre (cx,cy) */
  plane(svg, cx, cy, sc, r, C){ axis(svg, cx-1.4*r*sc, cy, cx+1.4*r*sc, cy, 'grid'); axis(svg, cx, cy-1.4*r*sc, cx, cy+1.4*r*sc, 'grid'); S('circle',{cx, cy, r: r*sc, fill:'none', stroke: C.line, 'stroke-dasharray':'4 3'}, svg); return {X: x=>cx+x*sc, Y: y=>cy-y*sc}; },
  /* signed heat map of a real matrix M (array of rows) at (x0,y0) with cell size; labels optional */
  heat(svg, M, x0, y0, cell, C, opts){ opts = opts||{}; const m = M.length; const vmax = opts.vmax || Math.max(1e-300, ...M.flat().map(Math.abs));
    for (let i=0;i<m;i++) for (let j=0;j<M[i].length;j++){ const v = M[i][j]/vmax; S('rect',{x:x0+j*cell, y:y0+i*cell, width:cell-1, height:cell-1, rx:2, fill: v>=0?C.orbit:C.spec, opacity: Math.min(1,Math.abs(v))*0.9+0.06}, svg);
      if (opts.numbers && cell>=26) txt(svg, x0+j*cell+2, y0+i*cell+cell/2+3, WT.fmtF(M[i][j], opts.digits==null?2:opts.digits), {'font-size':'8', fill:C.ink}); }
    if (opts.rowLabels) opts.rowLabels.forEach((s,i)=>txt(svg, x0-4, y0+i*cell+cell/2+3, s, {'font-size':'9','text-anchor':'end'}));
    if (opts.colLabels) opts.colLabels.forEach((s,j)=>txt(svg, x0+j*cell+cell/2, y0+m*cell+11, s, {'font-size':'9','text-anchor':'middle'}));
    if (opts.title) txt(svg, x0, y0-6, opts.title, {fill:C.ink}); return vmax; },
  /* vertical bars of values v[i] at baseline y0; colours by sign unless opts.color */
  bars(svg, v, x0, y0, w, hscale, C, opts){ opts = opts||{}; v.forEach((val,i)=>{ const h = val*hscale; S('rect',{x:x0+i*w, y: h>=0? y0-h : y0, width: Math.max(1,w-2), height: Math.abs(h), fill: opts.color || (val>=0?C.orbit:C.spec), opacity: opts.opacity||.9}, svg); if (opts.labels) txt(svg, x0+i*w+w/2, y0+11, String(opts.labels[i]), {'font-size':'9','text-anchor':'middle'}); }); }
};
const css = v => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
WT.col = () => ({ orbit: css('--orbit'), spec: css('--spec'), pole: css('--pole'), arch: css('--arch'), bond: css('--bond'), metric: css('--metric'), ink: css('--ink'), ink2: css('--ink2'), line: css('--line'), bg: css('--bg'), bg2: css('--bg2'), bg3: css('--bg3'), orbitSoft: css('--orbit-soft'), specSoft: css('--spec-soft'), poleSoft: css('--pole-soft'), bondSoft: css('--bond-soft'), metricSoft: css('--metric-soft') });
WT.CYC = ['#0b7a76','#c4461c','#5f4bb6','#9a6f05','#1d4ed8','#b0348a','#3a7d2c','#7c5a3a','#4f6b7a','#c2185b','#2e7d9c','#8d6e00'];
WT.fmt = (x, d=6) => (Math.abs(x) < 1e-300 ? '0' : Number(x).toPrecision(d)).replace(/e\+?(-?\d+)/, 'e$1');
WT.fmtF = (x, d=4) => (Math.abs(x)<0.5*Math.pow(10,-d) ? 0 : x).toFixed(d);
WT.fmtC = (re, im, d=4) => Math.abs(im) < 0.5*Math.pow(10,-d) ? WT.fmtF(re,d) : (WT.fmtF(re,d) + (im<0?' − ':' + ') + WT.fmtF(Math.abs(im),d) + 'i');
WT.typeset = el => { if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise(el?[el]:undefined).catch(()=>{}); };
WT.reducedMotion = () => window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* controls: label + range slider with live value; returns the input */
WT.slider = (parent, id, label, min, max, step, value, onInput, fmt) => { const lab = document.createElement('label'); lab.innerHTML = `${label} <input type="range" id="${id}" min="${min}" max="${max}" step="${step}" value="${value}"><span class="val" id="${id}v"></span>`; parent.appendChild(lab); const inp = lab.querySelector('input'), val = lab.querySelector('.val'); const f = fmt || (v=>String(v)); val.textContent = f(+value); inp.addEventListener('input', e => { val.textContent = f(+e.target.value); onInput(+e.target.value); }); return inp; };
WT.button = (parent, id, label, onClick) => { const b = document.createElement('button'); b.id = id; b.type='button'; b.textContent = label; b.addEventListener('click', onClick); parent.appendChild(b); return b; };
WT.select = (parent, id, label, options, value, onChange) => { const lab = document.createElement('label'); lab.innerHTML = `${label} <select id="${id}"></select>`; parent.appendChild(lab); const sel = lab.querySelector('select'); options.forEach(o => { const opt = document.createElement('option'); opt.value = o[0]; opt.textContent = o[1]; if (o[0]===value) opt.selected = true; sel.appendChild(opt); }); sel.addEventListener('change', e => onChange(e.target.value)); return sel; };
WT.checkbox = (parent, id, label, checked, onChange) => { const lab = document.createElement('label'); lab.innerHTML = `<input type="checkbox" id="${id}" ${checked?'checked':''}> ${label}`; parent.appendChild(lab); lab.querySelector('input').addEventListener('change', e => onChange(e.target.checked)); return lab.querySelector('input'); };
WT.div = (parent, cls, html) => { const d = document.createElement('div'); if (cls) d.className = cls; if (html!=null) d.innerHTML = html; parent.appendChild(d); return d; };
WT.svgIn = (parent, viewBox, id) => { const s = S('svg', {viewBox, class:'plot'}); if (id) s.id = id; parent.appendChild(s); return s; };

// ---------- real linear algebra ----------
WT.eye = n => Array.from({length:n}, (_,i) => Array.from({length:n}, (_,j) => i===j?1:0));
WT.matmul = (A, B) => { const n=A.length, m=B[0].length, k=B.length; const C=Array.from({length:n},()=>new Array(m).fill(0)); for(let i=0;i<n;i++) for(let l=0;l<k;l++){ const a=A[i][l]; if(!a) continue; const Bl=B[l], Ci=C[i]; for(let j=0;j<m;j++) Ci[j]+=a*Bl[j]; } return C; };
WT.trace = A => { let t=0; for(let i=0;i<A.length;i++) t+=A[i][i]; return t; };
WT.transpose = A => A[0].map((_,j)=>A.map(r=>r[j]));
/* traces of powers Tr A^k for k = 0..K by repeated multiplication (A real) */
WT.powerTraces = (A, K) => { const out=[A.length]; let P=A; for(let k=1;k<=K;k++){ out.push(WT.trace(P)); if(k<K) P=WT.matmul(P,A); } return out; };
/* cyclic Jacobi for real symmetric A: {values ascending, vectors[i] = eigenvector of values[i]} */
WT.jacobiEig = A => { const n=A.length; const a=A.map(r=>r.slice()); const V=WT.eye(n);
  for(let sweep=0; sweep<80; sweep++){ let off=0; for(let p=0;p<n;p++) for(let q=p+1;q<n;q++) off+=a[p][q]*a[p][q]; if(off<1e-28) break;
    for(let p=0;p<n;p++) for(let q=p+1;q<n;q++){ if(Math.abs(a[p][q])<1e-300) continue; const th=(a[q][q]-a[p][p])/(2*a[p][q]); const t=Math.sign(th||1)/(Math.abs(th)+Math.sqrt(th*th+1)); const c=1/Math.sqrt(t*t+1), s=t*c;
      for(let k=0;k<n;k++){ const akp=a[k][p], akq=a[k][q]; a[k][p]=c*akp-s*akq; a[k][q]=s*akp+c*akq; }
      for(let k=0;k<n;k++){ const apk=a[p][k], aqk=a[q][k]; a[p][k]=c*apk-s*aqk; a[q][k]=s*apk+c*aqk; }
      for(let k=0;k<n;k++){ const vkp=V[k][p], vkq=V[k][q]; V[k][p]=c*vkp-s*vkq; V[k][q]=s*vkp+c*vkq; } } }
  const ev=a.map((r,i)=>r[i]); const idx=ev.map((_,i)=>i).sort((i,j)=>ev[i]-ev[j]);
  return { values: idx.map(i=>ev[i]), vectors: idx.map(i=>V.map(r=>r[i])) }; };
/* Hermitian matrix given as (Re, Im) arrays: eigenvalues ascending via the real embedding [[Re,-Im],[Im,Re]] (each doubled) */
WT.hermEigvals = (Re, Im) => { const n=Re.length; const M=Array.from({length:2*n},()=>new Array(2*n).fill(0)); for(let i=0;i<n;i++) for(let j=0;j<n;j++){ M[i][j]=Re[i][j]; M[i+n][j+n]=Re[i][j]; M[i][j+n]=-Im[i][j]; M[i+n][j]=Im[i][j]; } const v=WT.jacobiEig(M).values; return v.filter((_,k)=>k%2===0); };
/* Toeplitz matrix from a sequence t[0..K-1] (real): T[j][k] = t[|j-k|] */
WT.toeplitz = (t, K) => Array.from({length:K},(_,j)=>Array.from({length:K},(_,k)=>t[Math.abs(j-k)]));
/* Hermitian Toeplitz from complex t (tRe, tIm), t_{-k} = conj t_k: returns {Re, Im} */
WT.toeplitzC = (tRe, tIm, K) => { const Re=[], Im=[]; for(let j=0;j<K;j++){ Re.push([]); Im.push([]); for(let k=0;k<K;k++){ const d=k-j; Re[j].push(tRe[Math.abs(d)]); Im[j].push(d>=0? tIm[d] : -tIm[-d]); } } return {Re, Im}; };
/* minimal eigenvalue of the Toeplitz form of a real sequence for each window size 1..K */
WT.toeplitzMins = (t, K) => { const out=[]; for(let n=1;n<=K;n++) out.push(WT.jacobiEig(WT.toeplitz(t,n)).values[0]); return out; };

// ---------- complex arithmetic (re, im pairs) and complex matrices {re: [][], im: [][]} ----------
const C = WT.C = {
  mul: (a,b) => [a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]],
  add: (a,b) => [a[0]+b[0], a[1]+b[1]], sub: (a,b) => [a[0]-b[0], a[1]-b[1]],
  div: (a,b) => { const d=b[0]*b[0]+b[1]*b[1]; return [(a[0]*b[0]+a[1]*b[1])/d, (a[1]*b[0]-a[0]*b[1])/d]; },
  abs: a => Math.hypot(a[0],a[1]), conj: a => [a[0],-a[1]], expi: t => [Math.cos(t), Math.sin(t)],
  pow: (a,n) => { let r=[1,0]; for(let i=0;i<n;i++) r=C.mul(r,a); return r; },
  sqrt: a => { const r=Math.hypot(a[0],a[1]); const re=Math.sqrt((r+a[0])/2), im=Math.sign(a[1]||1)*Math.sqrt(Math.max(0,(r-a[0])/2)); return [re,im]; }
};
const cm = WT.cmat = {
  zeros: (n,m) => ({re: Array.from({length:n},()=>new Array(m==null?n:m).fill(0)), im: Array.from({length:n},()=>new Array(m==null?n:m).fill(0))}),
  eye: n => { const Z=cm.zeros(n); for(let i=0;i<n;i++) Z.re[i][i]=1; return Z; },
  fromReal: A => ({re: A.map(r=>r.slice()), im: A.map(r=>r.map(()=>0))}),
  mul: (A,B) => { const n=A.re.length, k=B.re.length, m=B.re[0].length; const Z=cm.zeros(n,m); for(let i=0;i<n;i++) for(let l=0;l<k;l++){ const ar=A.re[i][l], ai=A.im[i][l]; if(!ar&&!ai) continue; for(let j=0;j<m;j++){ const br=B.re[l][j], bi=B.im[l][j]; Z.re[i][j]+=ar*br-ai*bi; Z.im[i][j]+=ar*bi+ai*br; } } return Z; },
  add: (A,B) => ({re: A.re.map((r,i)=>r.map((v,j)=>v+B.re[i][j])), im: A.im.map((r,i)=>r.map((v,j)=>v+B.im[i][j]))}),
  scale: (A,s) => ({re: A.re.map((r,i)=>r.map((v,j)=>A.re[i][j]*s[0]-A.im[i][j]*s[1])), im: A.im.map((r,i)=>r.map((v,j)=>A.re[i][j]*s[1]+A.im[i][j]*s[0]))}),
  dagger: A => ({re: A.re[0].map((_,j)=>A.re.map(r=>r[j])), im: A.im[0].map((_,j)=>A.im.map(r=>-r[j]))}),
  conjT: A => cm.dagger(A),
  kron: (A,B) => { const n=A.re.length, m=B.re.length; const Z=cm.zeros(n*m); for(let i=0;i<n;i++) for(let j=0;j<n;j++) for(let k=0;k<m;k++) for(let l=0;l<m;l++){ const a=[A.re[i][j],A.im[i][j]], b=[B.re[k][l],B.im[k][l]]; const p=C.mul(a,b); Z.re[i*m+k][j*m+l]=p[0]; Z.im[i*m+k][j*m+l]=p[1]; } return Z; },
  trace: A => { let r=0,i=0; for(let k=0;k<A.re.length;k++){ r+=A.re[k][k]; i+=A.im[k][k]; } return [r,i]; },
  frob: A => Math.sqrt(A.re.flat().reduce((s,v)=>s+v*v,0)+A.im.flat().reduce((s,v)=>s+v*v,0)),
  /* Tr A^k for k=0..K as complex pairs */
  powerTraces: (A,K) => { const out=[[A.re.length,0]]; let P=A; for(let k=1;k<=K;k++){ out.push(cm.trace(P)); if(k<K) P=cm.mul(P,A); } return out; },
  /* Ad(B) on End(V) in column-stacking convention: vec(B X B^dagger) = (conj(B) kron B) vec X  (n^2 x n^2) */
  ad: B => cm.kron({re:B.re, im:B.im.map(r=>r.map(v=>-v))}, B),
  /* inverse by Gauss-Jordan with partial pivoting (small n) */
  inv: A => { const n=A.re.length; const M=A.re.map((r,i)=>r.map((v,j)=>[v,A.im[i][j]])); const I=WT.eye(n).map(r=>r.map(v=>[v,0]));
    for(let c=0;c<n;c++){ let p=c; for(let r=c+1;r<n;r++) if(C.abs(M[r][c])>C.abs(M[p][c])) p=r; [M[c],M[p]]=[M[p],M[c]]; [I[c],I[p]]=[I[p],I[c]]; const piv=M[c][c]; if(C.abs(piv)<1e-300) return null;
      for(let j=0;j<n;j++){ M[c][j]=C.div(M[c][j],piv); I[c][j]=C.div(I[c][j],piv); }
      for(let r=0;r<n;r++){ if(r===c) continue; const f=M[r][c]; if(!f[0]&&!f[1]) continue; for(let j=0;j<n;j++){ M[r][j]=C.sub(M[r][j],C.mul(f,M[c][j])); I[r][j]=C.sub(I[r][j],C.mul(f,I[c][j])); } } }
    return {re: I.map(r=>r.map(v=>v[0])), im: I.map(r=>r.map(v=>v[1]))}; },
  /* characteristic polynomial coefficients c[0..n] of det(x - A) = sum c[k] x^k, by Faddeev-LeVerrier (complex) */
  charpoly: A => { const n=A.re.length; const c=new Array(n+1).fill(null).map(()=>[0,0]); c[n]=[1,0]; let M=cm.zeros(n); const I=cm.eye(n);
    for(let k=1;k<=n;k++){ // M_k = A M_{k-1} + c_{n-k+1} I ; c_{n-k} = -Tr(A M_k)/k
      const AM = cm.mul(A,M); const s=c[n-k+1]; M = {re: AM.re.map((r,i)=>r.map((v,j)=>v+(i===j?s[0]:0))), im: AM.im.map((r,i)=>r.map((v,j)=>v+(i===j?s[1]:0)))};
      const t=cm.trace(cm.mul(A,M)); c[n-k]=[-t[0]/k, -t[1]/k]; }
    return c; },
  /* all eigenvalues (complex pairs) of a small complex matrix via charpoly + Durand-Kerner + Newton polish */
  eigvals: A => WT.polyRoots(cm.charpoly(A))
};
/* roots of sum c[k] x^k (c[k] complex pairs, c[n] leading) by Durand-Kerner, then Newton polishing */
WT.polyRoots = c => { let n=c.length-1; while(n>0 && C.abs(c[n])<1e-300) n--; if(n<=0) return []; const a=c.slice(0,n+1).map(v=>C.div(v,c[n]));
  const ev = x => { let v=[0,0]; for(let k=n;k>=0;k--) v=C.add(C.mul(v,x),a[k]); return v; };
  const dv = x => { let v=[0,0]; for(let k=n;k>=1;k--) v=C.add(C.mul(v,x),[k*a[k][0],k*a[k][1]]); return v; };
  let R=Math.max(1, ...a.slice(0,n).map(v=>C.abs(v)))+1; const roots=[]; for(let k=0;k<n;k++) roots.push(C.mul([0.4*R+0.9,0],C.expi(2*Math.PI*k/n+0.4)));
  for(let it=0; it<600; it++){ let mx=0; for(let i=0;i<n;i++){ let den=[1,0]; for(let j=0;j<n;j++) if(j!==i) den=C.mul(den,C.sub(roots[i],roots[j])); if(C.abs(den)<1e-300) den=[1e-300,0]; const d=C.div(ev(roots[i]),den); roots[i]=C.sub(roots[i],d); mx=Math.max(mx,C.abs(d)); } if(mx<1e-15) break; }
  for(let i=0;i<n;i++) for(let it=0; it<6; it++){ const d=dv(roots[i]); if(C.abs(d)<1e-14) break; const step=C.div(ev(roots[i]),d); roots[i]=C.sub(roots[i],step); if(C.abs(step)<1e-16) break; }
  return roots; };

// ---------- movie player: a scrubbable animation with captions ----------
/* WT.movie(root, {viewBox, duration (s), frames: [{t: fraction, caption}], draw(svg, t, C)})
   draw is called with t in [0,1]; captions switch at frame boundaries. Returns {svg, setT, play, pause}. */
WT.movie = (root, opts) => { const C = WT.col(); const wrap = WT.div(root, 'movie'); const svg = WT.svgIn(wrap, opts.viewBox || '0 0 940 300'); const cap = WT.div(wrap, 'caption', ''); const bar = WT.div(wrap, 'bar');
  const id = opts.id || ('mv'+Math.random().toString(36).slice(2,7)); const play = WT.button(bar, id+'_play', 'play', ()=>toggle()); const rng = document.createElement('input'); rng.type='range'; rng.min='0'; rng.max='1000'; rng.value='0'; rng.id=id+'_t'; rng.setAttribute('aria-label','timeline'); bar.appendChild(rng); const step = WT.button(bar, id+'_step', 'next scene', ()=>{ const fr=opts.frames||[]; const t=state.t; const nx=fr.find(f=>f.t>t+1e-6); setT(nx? nx.t : 0); });
  const state = { t: 0, timer: null, last: 0 }; const dur = (opts.duration||12)*1000;
  function setT(t){ state.t = Math.max(0, Math.min(1, t)); rng.value = String(Math.round(state.t*1000)); clear(svg); try { opts.draw(svg, state.t, WT.col()); } catch(e){ txt(svg, 10, 20, 'draw error: '+e.message, {fill:'red'}); }
    const fr = opts.frames||[]; let c = ''; for (const f of fr) if (state.t >= f.t-1e-9) c = f.caption; cap.innerHTML = c; }
  function tick(now){ if(!state.timer) return; const dt = now - state.last; state.last = now; let t = state.t + dt/dur; if (t >= 1){ t = 1; pause(); } setT(t); if(state.timer) state.timer = requestAnimationFrame(tick); }
  function playFn(){ if (state.timer) return; if (state.t >= 1) state.t = 0; play.textContent = 'pause'; state.last = performance.now(); state.timer = requestAnimationFrame(tick); }
  function pause(){ if (state.timer) cancelAnimationFrame(state.timer); state.timer = null; play.textContent = state.t>=1 ? 'replay' : 'play'; }
  function toggle(){ state.timer ? pause() : playFn(); }
  rng.addEventListener('input', e => { pause(); setT(+e.target.value/1000); });
  setT(opts.start!=null ? opts.start : 0); if (opts.autoplay && !WT.reducedMotion()) playFn();
  return { svg, setT, play: playFn, pause, state }; };

// ---------- mounting ----------
WT.mountAll = () => { for (const name in WT.demos){ const root = document.getElementById('demo-'+name); if (!root) continue; try { WT.demos[name](root); } catch (e){ const d = document.createElement('div'); d.className='readout'; d.textContent = 'demo "'+name+'" failed: '+e.message+'\n'+(e.stack||''); root.appendChild(d); console.error(e); } } };
})();
