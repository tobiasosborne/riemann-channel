/* demos-core.js -- orchestrator's stations: permutations (perm), subshifts (subshift), the Gram/metric
 * construction (gram), the Riemann lattice Gram (riemann) and the CCM window (ccm). Uses core.js (WT). */
(function(){
'use strict';
const WT = window.WT; const S = WT.svg.el, txt = WT.svg.text, clear = WT.svg.clear, poly = WT.svg.polyline, axis = WT.svg.axis;
const fmt = WT.fmt, fmtF = WT.fmtF, C = WT.C, cm = WT.cmat;

/* ---------- shared: minimal-eigenvalue-vs-window plot ---------- */
function minPlot(svg, mins, Col, title){ clear(svg); const K = mins.length; const lo = Math.min(0, ...mins), hi = Math.max(1e-9, ...mins); const X = k => 40 + (k-1)*(400/Math.max(K-1,1)), Y = v => 22 + (hi - v)/(hi - lo + 1e-12)*196; axis(svg, 30, Y(0), 452, Y(0)); txt(svg, 438, Y(0)-4, '0');
  poly(svg, mins.map((v,i)=>[X(i+1), Y(v)]), Col.ink, 1.4); mins.forEach((v,i)=>{ S('circle',{cx:X(i+1), cy:Y(v), r:4, fill: v < -1e-9 ? Col.spec : Col.orbit}, svg); if (K<=16 || i%2===0) txt(svg, X(i+1)-3, 246, String(i+1), {'font-size':'9'}); }); txt(svg, 34, 14, title || 'λ_min of the Toeplitz form (T_{jk} = t_{k−j}) against the window size K', {fill: Col.ink}); txt(svg, 420, 258, 'K'); }
function modePlot(svg, modes, r, Col, opts){ opts = opts||{}; clear(svg); const sc = 110/(1.35*Math.max(r, ...modes.map(m=>C.abs(m)), ...((opts.partners||[]).map(m=>C.abs(m))), 1e-9)); const P = WT.svg.plane(svg, 150, 150, sc, r, Col);
  (opts.trivial||[]).forEach(z => S('circle',{cx:P.X(z[0]), cy:P.Y(z[1]), r:5, fill:Col.pole, stroke:Col.bg2,'stroke-width':1}, svg));
  modes.forEach(m => { const on = Math.abs(C.abs(m) - r) < 1e-6*Math.max(1,r); S('circle',{cx:P.X(m[0]), cy:P.Y(m[1]), r:6, fill: on ? Col.spec : Col.ink, stroke:Col.bg2, 'stroke-width':1.5}, svg); });
  (opts.partners||[]).forEach(z => S('circle',{cx:P.X(z[0]), cy:P.Y(z[1]), r:6, fill:'none', stroke:Col.ink2, 'stroke-width':1.5, 'stroke-dasharray':'2 2'}, svg));
  txt(svg, P.X(r)+4, 146, opts.rlabel || ('r = '+fmtF(r,3))); if (opts.title) txt(svg, 8, 14, opts.title, {fill:Col.ink}); return P; }

/* =====================================================================================
   Demo: permutation MPS with point letters (shard 03b, def:graded-permutation-mps)
   ===================================================================================== */
WT.demos.perm = function(root){
  const st = { n: 6, sig: [1,2,0,4,5,3], sel: -1, L: 3, K: 8, odd: new Set(), mode: 'poles', timer: null };
  const ctr = WT.div(root, 'controls');
  WT.slider(ctr, 'perm_n', 'points n', 3, 8, 1, st.n, v => { st.n = v; st.sig = [...Array(v).keys()].map(i=>(i+1)%v); st.odd.clear(); st.sel=-1; draw(); });
  WT.button(ctr, 'perm_shuffle', 'shuffle', () => { const a=[...Array(st.n).keys()]; for(let i=st.n-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } st.sig=a; st.odd.clear(); st.sel=-1; draw(); });
  WT.button(ctr, 'perm_preset', '(1 2)(3 4 5)', () => { st.n=5; WT.$('perm_n').value=5; WT.$('perm_nv').textContent='5'; st.sig=[1,0,3,4,2]; st.odd.clear(); st.sel=-1; draw(); });
  WT.slider(ctr, 'perm_L', 'ring length L', 1, 10, 1, st.L, v => { st.L = v; draw(); });
  WT.slider(ctr, 'perm_K', 'window K', 2, 14, 1, st.K, v => { st.K = v; draw(); });
  WT.select(ctr, 'perm_mode', 'closure', [['poles','untwisted: t_k = Tr P^k'],['twisted','parity supertrace: t_k = Tr(Π P^k) (a bond supertrace, not a ring norm)']], st.mode, v => { st.mode = v; draw(); });
  const g = WT.div(root, 'grid3'); const svgP = WT.svgIn(WT.div(g,''), '0 0 300 300', 'perm_circle'); WT.div(g.lastChild, 'small', 'σ as arrows; click two points to swap their images; click a cycle label to grade it odd (twisted closure)');
  const svgE = WT.svgIn(WT.div(g,''), '0 0 300 300', 'perm_E'); WT.div(g.lastChild, 'small', 'E = Σ_x |σx⟩⟨x| ⊗ |σx⟩⟨x| on the doubled bond ℂⁿ⊗ℂⁿ: P on the diagonal pairs (a,a), zero elsewhere');
  const svgT = WT.svgIn(WT.div(g,''), '0 0 300 300', 'perm_T'); WT.div(g.lastChild, 'small', 'the Weil matrix T_{jk} = t_{|j−k|} from ring norms, and its eigenvalues');
  const g2 = WT.div(root, 'grid2'); const svgM = WT.svgIn(WT.div(g2,''), '0 0 460 260', 'perm_min'); const read = WT.div(g2, 'readout', ''); read.id = 'perm_read';
  function cycles(sig){ const n=sig.length, seen=new Array(n).fill(false), out=[]; for(let i=0;i<n;i++){ if(seen[i]) continue; const c=[]; let j=i; while(!seen[j]){ seen[j]=true; c.push(j); j=sig[j]; } out.push(c); } return out; }
  function draw(){
    const Col = WT.col(), n = st.n, sig = st.sig, cs = cycles(sig); const cycOf = new Array(n); cs.forEach((c,ci)=>c.forEach(v=>cycOf[v]=ci));
    const par = x => st.odd.has(cycOf[x]) ? -1 : 1;
    // permutation picture
    clear(svgP); const R=105, cx=150, cy=150; const pos = i => [cx+R*Math.cos(2*Math.PI*i/n-Math.PI/2), cy+R*Math.sin(2*Math.PI*i/n-Math.PI/2)];
    S('circle',{cx,cy,r:R,fill:'none',stroke:Col.line},svgP);
    for(let i=0;i<n;i++){ const j=sig[i]; const [x1,y1]=pos(i), [x2,y2]=pos(j); const col = WT.CYC[cycOf[i]%12]; if(i===j){ S('circle',{cx:x1+(x1-cx)*0.18, cy:y1+(y1-cy)*0.18, r:9, fill:'none', stroke:col,'stroke-width':1.5},svgP); continue; } const mx=(x1+x2)/2, my=(y1+y2)/2, qx=cx+(mx-cx)*0.5, qy=cy+(my-cy)*0.5; const dx=x2-x1, dy=y2-y1, Ln=Math.hypot(dx,dy); S('path',{d:`M${x1},${y1} Q${qx},${qy} ${x2-dx/Ln*13},${y2-dy/Ln*13}`, fill:'none', stroke:col, 'stroke-width':1.6},svgP); S('circle',{cx:x2-dx/Ln*13, cy:y2-dy/Ln*13, r:2.5, fill:col},svgP); }
    for(let i=0;i<n;i++){ const [x,y]=pos(i); const c=S('circle',{cx:x, cy:y, r:11, fill: WT.CYC[cycOf[i]%12], stroke: st.sel===i?Col.ink:Col.bg2, 'stroke-width':2, class:'pt'},svgP); c.style.cursor='pointer'; c.addEventListener('click',()=>{ if(st.sel<0) st.sel=i; else if(st.sel===i) st.sel=-1; else { const a=sig[st.sel]; sig[st.sel]=sig[i]; sig[i]=a; st.sel=-1; st.odd.clear(); } draw(); }); txt(svgP, x-3.5, y+4, String(i+1), {fill:'#fff','font-size':'10','font-weight':'600','pointer-events':'none'}); }
    cs.forEach((c,ci)=>{ const t = txt(svgP, 8, 20+ci*15, `(${c.map(v=>v+1).join(' ')})${st.odd.has(ci)?' odd':''}`, {fill: WT.CYC[ci%12], 'font-size':'11', style:'cursor:pointer'}); t.addEventListener('click',()=>{ if(st.odd.has(ci)) st.odd.delete(ci); else st.odd.add(ci); if(st.odd.size && st.mode==='poles'){ st.mode='twisted'; WT.$('perm_mode').value='twisted'; } draw(); }); });
    // E on the doubled bond
    clear(svgE); const N2=n*n, cell = Math.min(10, 270/N2); const x0 = 150 - N2*cell/2, y0 = 150 - N2*cell/2; for(let a=0;a<n;a++) for(let b=0;b<n;b++) for(let c2=0;c2<n;c2++) for(let d=0;d<n;d++){ // E[(c,d),(a,b)] = delta_ab delta_{c,sig a} delta_{d,sig a}
      const v = (a===b && c2===sig[a] && d===sig[a]) ? 1 : 0; const row=c2*n+d, col=a*n+b; S('rect',{x:x0+col*cell, y:y0+row*cell, width:Math.max(cell-0.6,0.8), height:Math.max(cell-0.6,0.8), fill: v? WT.CYC[cycOf[a]%12] : Col.bg3, opacity: v?1:0.6},svgE); }
    txt(svgE, x0, y0-6, `E on ℂ^${n}⊗ℂ^${n} (${N2}×${N2}): rank ${n}, one entry per letter A_x`, {fill:Col.ink,'font-size':'10'});
    // ring norms
    const fix = k => { let f=0, fs=0; for(let x=0;x<n;x++){ let j=x; for(let t=0;t<k;t++) j=sig[j]; if(j===x){ f++; fs+=par(x); } } return [f, fs]; };
    const t = []; for(let k=0;k<=Math.max(st.K,14);k++){ const [f,fs]=fix(k); t.push(st.mode==='poles'? f : fs); }
    const T = WT.toeplitz(t, st.K); const eig = WT.jacobiEig(T);
    clear(svgT); const cT = Math.min(22, 210/st.K); WT.svg.heat(svgT, T, 150-st.K*cT/2, 30, cT, Col, {numbers:true, digits:0, title:`T_{jk} = t_{|j−k|}, K = ${st.K}`});
    txt(svgT, 20, 285, 'eigenvalues: '+eig.values.map(v=>fmtF(v,2)).join(', '), {'font-size':'9', fill: eig.values[0] < -1e-9 ? Col.spec : Col.ink2});
    const mins = WT.toeplitzMins(t, 14); minPlot(svgM, mins, Col);
    // words of length L
    const words=[]; for(let x=0;x<n;x++){ let j=x; const w=[x]; for(let s=1;s<st.L;s++){ j=sig[j]; w.push(j); } if(sig[j]===x) words.push(w); }
    const oddc = [...st.odd].map(ci=>`(${cs[ci].map(v=>v+1).join(' ')})`);
    read.innerHTML = `<span class="k">letters:</span> A_x = |σx⟩⟨x|, x = 1..${n}; bond ℂ^${n}; physical index x ∈ {1..${n}}\n<span class="k">ring of length L = ${st.L}:</span> the words w with Tr(A_{w_L}⋯A_{w_1}) ≠ 0 are the orbits of the points fixed by σ^${st.L}:\n  ${words.length? words.map(w=>'('+w.map(v=>v+1).join(',')+')').join(' ') : 'none'}\n  ‖ψ_${st.L}‖² = Σ_w |Tr A_w|² = ${words.length} = #Fix(σ^${st.L}) = Tr E^${st.L}\n<span class="k">ring norms t_k = Tr P^k, k = 1..12:</span> ${Array.from({length:12},(_,k)=>fix(k+1)[0]).join(', ')}${st.mode==='twisted'? `\n<span class="k">twisted t_k = Tr(Π P^k) with odd cycles ${oddc.join('')||'none'}:</span> ${Array.from({length:12},(_,k)=>fix(k+1)[1]).join(', ')}`:''}\n<span class="k">zeta:</span> 1/det(1−uP) = 1/${cs.map(c=>`(1−u^${c.length})`).join('')}${st.mode==='twisted'? `;  graded: 1/sdet(1−uP_Π) = ${oddc.length?cs.filter((c,ci)=>st.odd.has(ci)).map(c=>`(1−u^${c.length})`).join(''):'1'}/${cs.filter((c,ci)=>!st.odd.has(ci)).map(c=>`(1−u^${c.length})`).join('')||'1'}`:''}\n<span class="k">Weil form at K = ${st.K}:</span> λ_min = ${fmt(eig.values[0],4)}  ${eig.values[0] < -1e-9 ? '<span class="spec">indefinite: the odd cycles\' modes enter the bond supertrace with a minus sign; they are zeros of the graded zeta, not poles, and a positive form for zeros needs the sign reversed (as T_k = q^{k/2}+q^{-k/2} − N_k q^{-k/2} does for a curve); with point letters the ring norm itself stays Tr P^k (shard 03b)</span>' : (st.mode==='poles' ? 'positive semidefinite: P is unitary in the native metric, so T_{jk} = Tr((P^j)†P^k) is the Gram matrix of the open strips' : 'positive semidefinite')}\n<span class="k">kernel:</span> ${eig.values.filter(v=>Math.abs(v)<1e-9).length} zero eigenvalue(s) at K = ${st.K}; the strips P^0..P^{K−1} become dependent once K exceeds the number of distinct eigenvalues (${new Set(cs.flatMap(c=>Array.from({length:c.length},(_,m)=>(m/c.length).toFixed(9)))).size}).`;
  }
  draw();
};

/* =====================================================================================
   Demo: subshift of finite type (a 0/1 transfer matrix), the pole and the one-sided bound
   ===================================================================================== */
WT.demos.subshift = function(root){
  const presets = { golden: {n:2, M:[[1,1],[1,0]], name:'golden mean shift'}, cyc4: {n:4, M:[[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]], name:'4-symbol cyclic rule (I + C₄)'}, full2: {n:2, M:[[1,1],[1,1]], name:'full 2-shift'}, cycle3: {n:3, M:[[0,1,0],[0,0,1],[1,0,0]], name:'3-cycle (a permutation)'}, tri: {n:3, M:[[0,1,1],[1,0,1],[1,1,0]], name:'K₃ walks (J − I)'} };
  const st = { n: 2, M: presets.golden.M.map(r=>r.slice()), K: 10 };
  const ctr = WT.div(root, 'controls');
  WT.select(ctr, 'sub_preset', 'preset', Object.entries(presets).map(([k,v])=>[k,v.name]), 'golden', v => { st.n = presets[v].n; st.M = presets[v].M.map(r=>r.slice()); WT.$('sub_n').value = st.n; WT.$('sub_nv').textContent = st.n; draw(); });
  WT.slider(ctr, 'sub_n', 'symbols n', 2, 5, 1, st.n, v => { const M = Array.from({length:v},(_,i)=>Array.from({length:v},(_,j)=> (st.M[i]&&st.M[i][j]!=null)? st.M[i][j] : (i===j?1:0))); st.n=v; st.M=M; draw(); });
  WT.button(ctr, 'sub_random', 'random 0/1', () => { st.M = Array.from({length:st.n},()=>Array.from({length:st.n},()=>Math.random()<0.55?1:0)); draw(); });
  WT.slider(ctr, 'sub_K', 'window K', 2, 14, 1, st.K, v => { st.K=v; draw(); });
  const g = WT.div(root, 'grid3'); const svgM = WT.svgIn(WT.div(g,''), '0 0 300 300', 'sub_M'); WT.div(g.lastChild,'small','transition matrix M (click a cell to toggle); the MPS has one letter A_e = |b⟩⟨a| per allowed transition a→b');
  const svgZ = WT.svgIn(WT.div(g,''), '0 0 300 300', 'sub_modes'); WT.div(g.lastChild,'small','<span class="pill spec">comparison</span> eigenvalues of M; dashed circle |μ| = √λ_max; pole λ_max in ochre; hollow: reflected partners λ_max/μ̄');
  const svgW = WT.svgIn(WT.div(g,''), '0 0 460 260', 'sub_min'); WT.div(g.lastChild,'small','λ_min of the Weil form built from the counts, T_{jk} = ν_{|j−k|}');
  const read = WT.div(root, 'readout', ''); read.id='sub_read';
  function draw(){ const Col = WT.col(), n = st.n, M = st.M;
    clear(svgM); const cell = Math.min(46, 240/n), x0 = 150-n*cell/2, y0 = 150-n*cell/2; for(let i=0;i<n;i++) for(let j=0;j<n;j++){ const r = S('rect',{x:x0+j*cell, y:y0+i*cell, width:cell-3, height:cell-3, rx:4, fill: M[i][j]? Col.orbit : Col.bg3, stroke: Col.line}, svgM); r.style.cursor='pointer'; r.addEventListener('click',()=>{ M[i][j]=1-M[i][j]; draw(); }); txt(svgM, x0+j*cell+cell/2-3, y0+i*cell+cell/2+4, String(M[i][j]), {fill: M[i][j]?'#fff':Col.ink2}); } for(let i=0;i<n;i++){ txt(svgM, x0-14, y0+i*cell+cell/2+4, String.fromCharCode(97+i)); txt(svgM, x0+i*cell+cell/2-3, y0-6, String.fromCharCode(97+i)); } txt(svgM, 8, 292, 'M_ab = 1: the letter a may be followed by b', {'font-size':'10'});
    const tr = WT.powerTraces(M, 14); const ev = cm.eigvals(cm.fromReal(M)); let lmax = 0, li=-1; ev.forEach((z,i)=>{ if (Math.abs(z[1])<1e-7 && z[0]>lmax){ lmax=z[0]; li=i; } });
    if (lmax < 1e-9){ read.innerHTML = 'M is nilpotent (no closed walks at all): no pole, nothing to count.'; clear(svgZ); clear(svgW); return; }
    const r = Math.sqrt(lmax); const retained = ev.filter((z,i)=>i!==li && C.abs(z)>1e-9); const zeros = ev.filter((z,i)=>i!==li && C.abs(z)<=1e-9).length;
    const nu = tr.map((v,l)=> (v - Math.pow(lmax,l))/Math.pow(lmax,l/2)); nu[0] = n - 1; // nu_0 = number of retained modes incl. zero modes; traces use 0^0 = 1
    const mins = WT.toeplitzMins(nu, 14); minPlot(svgW, mins, Col);
    const partners = retained.map(z => C.div([lmax,0], C.conj(z)));
    modePlot(svgZ, retained, r, Col, {trivial:[[lmax,0]], partners, title:`λ_max = ${fmtF(lmax,4)} (the pole); r = √λ_max = ${fmtF(r,4)}`});
    const bound = retained.every(z => C.abs(z) <= r+1e-9), onCircle = retained.every(z => Math.abs(C.abs(z)-r) < 1e-7);
    const Jinv = retained.every(z => retained.some(w => C.abs(C.sub(w, C.div([lmax,0], C.conj(z)))) < 1e-6));
    read.innerHTML = `<span class="k">ring norms (closed walks) t_l = Tr M^l, l = 1..10:</span> ${tr.slice(1,11).join(', ')}\n<span class="k">growth:</span> t_l ~ λ_max^l with λ_max = ${fmtF(lmax,6)} (Perron root; the pole). <span class="k">trivial set:</span> {λ_max}${zeros?` ∪ {0^[${zeros}]} (nilpotent part, contributes to no trace)`:''}\n<span class="k">rescaled retained sequence</span> ν_l = λ_max^{−l/2}(t_l − λ_max^l), l = 0..8: ${nu.slice(0,9).map(v=>fmtF(v,3)).join(', ')}\n<span class="k">Weil form at K = ${st.K}:</span> λ_min = ${fmt(mins[st.K-1],4)} → ${mins[st.K-1] < -1e-9 ? '<span class="spec">indefinite</span>' : 'positive'}  (thm:weil-positivity-finite: positive iff every retained |μ| ≤ √λ_max: ${bound?'yes':'<span class="spec">no</span>'})\n<span class="k">RH for this shift (comparison, from eigenvalues)</span> (every retained nonzero |μ| = √λ_max): ${onCircle?'<span class="orbit">holds</span>':'<span class="spec">fails</span>'}   <span class="k">retained moduli:</span> ${retained.map(z=>fmtF(C.abs(z),4)).join(', ')||'none'}\n<span class="k">duality μ ↦ λ_max/μ̄ maps retained to retained (comparison):</span> ${Jinv?'yes (thm:weil-duality-pairing applies: positivity ⇔ RH)':'<span class="spec">no</span> — positivity alone is only the one-sided bound; a mode inside the disc passes without being on the circle'}`;
  }
  draw();
};

/* =====================================================================================
   Demo: the Gram construction and the metric (prop:ccm-tn-operator-gram, prop:hp-inner-product-discrete)
   ===================================================================================== */
WT.demos.gram = function(root){
  const st = { kappa: 1.0, rho: 1.0, jordan: false, K: 6, th: [0.6, 2.1, -1.4] };
  const ctr = WT.div(root, 'controls');
  WT.slider(ctr, 'gram_kappa', 'non-normality κ', 0, 2, 0.05, st.kappa, v => { st.kappa=v; draw(); }, v=>v.toFixed(2));
  WT.slider(ctr, 'gram_rho', '|λ₂| (radius of one mode)', 0.5, 1.5, 0.01, st.rho, v => { st.rho=v; draw(); }, v=>v.toFixed(2));
  WT.checkbox(ctr, 'gram_jordan', 'replace λ₁,λ₂ by a Jordan block on the circle', st.jordan, v => { st.jordan=v; draw(); });
  WT.slider(ctr, 'gram_K', 'window K', 2, 10, 1, st.K, v => { st.K=v; draw(); });
  const g = WT.div(root, 'grid3');
  const svgA = WT.svgIn(WT.div(g,''), '0 0 300 300', 'gram_A'); WT.div(g.lastChild,'small','Toeplitz from traces: T_{jk} = t_{k−j}, t_k = Tr E^k (real part shown)');
  const svgB = WT.svgIn(WT.div(g,''), '0 0 300 300', 'gram_B'); WT.div(g.lastChild,'small','naive gluing: Tr((E^j)†E^k) in the native Hilbert–Schmidt metric');
  const svgC2 = WT.svgIn(WT.div(g,''), '0 0 300 300', 'gram_C'); WT.div(g.lastChild,'small','with the metric seam: Tr(G^{-1}(E^j)†G E^k), G = (V^{-1})†V^{-1}');
  const g2 = WT.div(root, 'grid2'); const svgZ = WT.svgIn(WT.div(g2,''), '0 0 300 300', 'gram_modes'); WT.div(g2.lastChild,'small','<span class="pill spec">comparison</span> eigenvalues of E, circle r = 1'); const read = WT.div(g2, 'readout', ''); read.id='gram_read';
  function draw(){ const Col = WT.col(); const d = 3; const Nm = [[0,1,0.4],[0,0,1],[0,0,0]];
    const V = cm.fromReal(WT.eye(d).map((r,i)=>r.map((v,j)=>v + st.kappa*Nm[i][j]))); const Vi = cm.inv(V);
    let Lam = cm.zeros(d); const lam = [C.mul([st.rho,0], C.expi(st.th[0])), C.expi(st.th[1]), C.expi(st.th[2])];
    if (st.jordan){ Lam.re[0][0]=Math.cos(st.th[0]); Lam.im[0][0]=Math.sin(st.th[0]); Lam.re[1][1]=Math.cos(st.th[0]); Lam.im[1][1]=Math.sin(st.th[0]); Lam.re[0][1]=1; Lam.re[2][2]=Math.cos(st.th[2]); Lam.im[2][2]=Math.sin(st.th[2]); }
    else lam.forEach((z,i)=>{ Lam.re[i][i]=z[0]; Lam.im[i][i]=z[1]; });
    const E = cm.mul(cm.mul(V, Lam), Vi); const G = cm.mul(cm.dagger(Vi), Vi); const Gi = cm.inv(G);
    const K = st.K; const pw = [cm.eye(d)]; for(let k=1;k<K;k++) pw.push(cm.mul(pw[k-1], E));
    const tr = cm.powerTraces(E, K); const T = WT.toeplitzC(tr.map(z=>z[0]), tr.map(z=>z[1]), K);
    const naive = cm.zeros(K), met = cm.zeros(K); for(let j=0;j<K;j++) for(let k=0;k<K;k++){ const a = cm.trace(cm.mul(cm.dagger(pw[j]), pw[k])); naive.re[j][k]=a[0]; naive.im[j][k]=a[1]; const b = cm.trace(cm.mul(cm.mul(cm.mul(Gi, cm.dagger(pw[j])), G), pw[k])); met.re[j][k]=b[0]; met.im[j][k]=b[1]; }
    const diff = (A,B) => Math.max(...A.re.flat().map((v,i)=>Math.abs(v-B.re.flat()[i])), ...A.im.flat().map((v,i)=>Math.abs(v-B.im.flat()[i])));
    const evT = WT.hermEigvals(T.Re, T.Im); const vmax = Math.max(...T.Re.flat().map(Math.abs), ...naive.re.flat().map(Math.abs));
    clear(svgA); WT.svg.heat(svgA, T.Re, 150-K*22/2, 40, 22, Col, {numbers:true, digits:1, vmax, title:'T (traces)'}); txt(svgA, 12, 285, 'eig: '+evT.map(v=>fmtF(v,2)).join(', '), {'font-size':'9', fill: evT[0] < -1e-7 ? Col.spec : Col.ink2});
    clear(svgB); WT.svg.heat(svgB, naive.re, 150-K*22/2, 40, 22, Col, {numbers:true, digits:1, vmax, title:'naive Gram'}); txt(svgB, 12, 285, 'max |naive − T| = '+fmt(diff(naive, {re:T.Re, im:T.Im}),3), {'font-size':'9'});
    clear(svgC2); WT.svg.heat(svgC2, met.re, 150-K*22/2, 40, 22, Col, {numbers:true, digits:1, vmax, title:'metric Gram'}); txt(svgC2, 12, 285, 'max |metric Gram − T| = '+fmt(diff(met, {re:T.Re, im:T.Im}),3), {'font-size':'9'});
    const resid = cm.frob(cm.add(cm.mul(cm.mul(cm.dagger(E), G), E), cm.scale(G, [-1,0])))/cm.frob(G);
    const modes = st.jordan ? [lam[0].map((v,i)=>i? Math.sin(st.th[0]) : Math.cos(st.th[0])), [Math.cos(st.th[0]), Math.sin(st.th[0])], lam[2]] : lam;
    modePlot(svgZ, modes, 1, Col, {title: st.jordan ? 'Jordan block at e^{iθ₁} (double) and e^{iθ₃}' : 'three modes, |λ₂| = '+fmtF(st.rho,2)});
    const onC = !st.jordan && Math.abs(st.rho-1) < 1e-9;
    read.innerHTML = `<span class="k">E = V Λ V^{-1}</span>, V = 1 + κN (κ = ${st.kappa.toFixed(2)}: κ = 0 is normal), Λ = ${st.jordan ? 'diag(e^{iθ₁}, e^{iθ₁}, e^{iθ₃}) + E₁₂ (a Jordan block)' : 'diag('+fmtF(st.rho,2)+'e^{iθ₁}, e^{iθ₂}, e^{iθ₃})'}\n<span class="k">traces t_k = Tr E^k, k = 0..${K-1}:</span> ${tr.map(z=>WT.fmtC(z[0],z[1],3)).join(', ')}\n<span class="k">Toeplitz eigenvalues:</span> ${evT.map(v=>fmt(v,4)).join(', ')} → ${evT[0] < -1e-7 ? '<span class="spec">indefinite</span>' : 'positive semidefinite'}\n<span class="k">E†GE = G residual with G = (V^{-1})†V^{-1}:</span> ${fmt(resid,3)}   ${st.jordan ? '<span class="spec">no positive G with E†GE = G exists for a Jordan block (prop:hp-inner-product-discrete); the traces t_k = 2e^{ikθ₁} + e^{ikθ₃} are those of the diagonalisable matrix with the same spectrum, so the Toeplitz form is positive semidefinite (rank 2) and cannot tell them apart: positivity is blind to Jordan blocks.</span>' : (onC ? 'E is unitary in the metric G, so (E^j)^♯ = E^{-j} and Tr((E^j)^♯E^k) = Tr E^{k−j} = t_{k−j}: the Toeplitz matrix is the Gram matrix of the strips E^0..E^{K−1} in the G-twisted Hilbert–Schmidt product, hence ≥ 0 (prop:ccm-tn-operator-gram). The naive gluing fails unless κ = 0.' : `|λ₂| = ${fmtF(st.rho,2)} ≠ 1: no metric makes E unitary, so no Gram identity; the Toeplitz form is ${st.rho<1 ? 'still positive (the mode is inside the disc: the one-sided bound of thm:weil-positivity-finite)' : '<span class="spec">indefinite once K is large enough (a mode outside the disc)</span>'}.`)}`;
  }
  draw();
};

/* =====================================================================================
   Demo: the Riemann case, lattice bumps (Weil functional from primes) as a Gram matrix
   ===================================================================================== */
const NMAX = 300000; let PP = null; const LOGPI = Math.log(Math.PI);
function primes(){ if (PP) return PP; const sieve = new Uint8Array(NMAX+1); const out=[]; for (let i=2;i<=NMAX;i++){ if(!sieve[i]){ const lp=Math.log(i); for(let j=i*2;j<=NMAX;j+=i) sieve[j]=1; let q=i; while(q<=NMAX){ out.push([q, lp/Math.sqrt(q), Math.log(q), i]); q*=i; } } } out.sort((a,b)=>a[0]-b[0]); PP = out; return PP; }
/* W(g) for g(x) = A exp(-(x-D)^2/2s^2): pole - primes - archimedean (normalisation of the parent page) */
function weilGauss(D, s, A){ const g = x => A*Math.exp(-(x-D)*(x-D)/(2*s*s)); const simpson=(f,a,b,n)=>{ const h=(b-a)/n; let acc=f(a)+f(b); for(let i=1;i<n;i++) acc+=f(a+i*h)*(i%2?4:2); return acc*h/3; };
  const pole = simpson(x=>g(x)*2*Math.cosh(x/2), D-9*s, D+9*s, 1600); const xmax = Math.abs(D)+8*s; let prime=0; for (const [n,w,ln] of primes()){ if (ln>xmax) break; prime += w*(g(ln)+g(-ln)); }
  const g0=g(0), rho = y => Math.exp(y/2)/(Math.exp(y)-Math.exp(-y)); const integrand = y => y<1e-7 ? 2.5*g0 : (g(y)+g(-y))*rho(y) - g0*Math.exp(-2*y)/y; const Y = Math.max(Math.abs(D)+9*s, 30);
  const arch = g0*LOGPI + simpson(integrand, 0, 1, Math.max(400, 2*Math.ceil(25/s))) + simpson(integrand, 1, Y, Math.min(60000, Math.max(4000, 2*Math.ceil(25*(Y-1)/s))));
  return {pole, prime, arch, W: pole-prime-arch}; }
WT.demos.riemann = function(root){
  const ZEROS = window.WT_RIEMANN13 ? window.WT_RIEMANN13.gamma : []; const Z100 = WT.ZEROS100 || ZEROS;
  const st = { ns: new Set([1,2,3,4,6]), s: 0.08, primes: true };
  const ctr = WT.div(root, 'controls'); const box = WT.div(ctr, '', 'strips at x = log n for n = '); for (let n=1;n<=12;n++){ const l=document.createElement('label'); l.style.marginRight='4px'; l.innerHTML=`<input type="checkbox" id="rie_n${n}" ${st.ns.has(n)?'checked':''}> ${n}`; box.appendChild(l); l.querySelector('input').addEventListener('change', e => { if(e.target.checked) st.ns.add(n); else st.ns.delete(n); if (st.ns.size>8){ e.target.checked=false; st.ns.delete(n); return; } draw(); }); }
  WT.slider(ctr, 'rie_s', 'width s', 0.03, 0.25, 0.01, st.s, v => { st.s=v; draw(); }, v=>v.toFixed(2));
  WT.checkbox(ctr, 'rie_primes', 'include the prime term', true, v => { st.primes=v; draw(); });
  const g = WT.div(root, 'grid2'); const svgH = WT.svgIn(WT.div(g,''), '0 0 460 300', 'rie_heat'); WT.div(g.lastChild,'small','G_{ij} = W(g_i ∗ g̃_j) from the primes (left) and Σ_γ 2 ĝ_i(γ)ĝ_j(γ) over the first 100 zeros (right, <span class="pill spec">comparison</span>)'); const read = WT.div(g, 'readout', ''); read.id='rie_read';
  function draw(){ const Col = WT.col(); const ns=[...st.ns].sort((a,b)=>a-b), m=ns.length, s=st.s, cs=ns.map(n=>Math.log(n)); if(!m){ read.textContent='choose at least one strip'; return; }
    const G=[], Z=[]; for(let i=0;i<m;i++){ G.push([]); Z.push([]); for(let j=0;j<m;j++){ if(j<i){ G[i].push(G[j][i]); Z[i].push(Z[j][i]); continue; } const D=cs[i]-cs[j]; const t=weilGauss(D, s*Math.SQRT2, s*Math.sqrt(Math.PI)); G[i].push(st.primes? t.W : t.pole-t.arch); let z=0; for(const gm of Z100){ z += 2*2*Math.PI*s*s*Math.exp(-s*s*gm*gm)*Math.cos(gm*D); } Z[i].push(z); } }
    const eg = WT.jacobiEig(G), ez = WT.jacobiEig(Z); clear(svgH); const cell=Math.min(200/m, 36); const vmax=Math.max(1e-12, ...G.flat().map(Math.abs), ...Z.flat().map(Math.abs));
    WT.svg.heat(svgH, G, 40, 30, cell, Col, {vmax, numbers:true, digits:2, title: st.primes? 'W(g_i ∗ g̃_j) from the primes' : 'pole + archimedean only', rowLabels: ns.map(String), colLabels: ns.map(String)});
    WT.svg.heat(svgH, Z, 250, 30, cell, Col, {vmax, numbers:true, digits:2, title:'from the zeros (comparison)', colLabels: ns.map(String)});
    const tol = 1e-7*Math.max(1e-300, ...G.flat().map(Math.abs)); const neg = eg.values[0] < -tol;
    read.innerHTML = `<span class="k">strips:</span> g_n(x) = exp(−(x − log n)²/2s²), s = ${s.toFixed(2)}, n ∈ {${ns.join(', ')}}; g_i ∗ g̃_j is a Gaussian at log(n_i/n_j) of width s√2\n<span class="k">Gram entries</span> G_{ij} = W(g_i ∗ g̃_j) = pole − primes − archimedean, each a finite computation (primes below e^{|log(n_i/n_j)| + 8s√2})\n<span class="k">eigenvalues of G (primes):</span> ${eg.values.map(v=>fmt(v,5)).join(', ')}\n<span class="k">eigenvalues from the zeros:</span> ${ez.values.map(v=>fmt(v,5)).join(', ')}\n${neg ? `<span class="spec">λ_min < 0.</span> ${st.primes ? 'Below the quadrature tolerance this is numerical; a genuine negative eigenvalue would refute RH.' : 'The pole and the archimedean place alone do not give a positive form (Yoshida/Bombieri: the unconditional positivity below support width log 2 is pole plus archimedean together with the primes absent from that range; here the strips are far apart).'}` : 'positive semidefinite: consistent with G being the Gram matrix of the smeared strips E^{g_i} in a metric that would make the dilation semigroup unitary on the retained (zero) modes; the metric is the unknown.'}\n<span class="k">TN reading:</span> t(x) ↔ "Tr E^x" is the explicit-formula distribution; G_{ij} ↔ Tr((E^{g_i})^♯ E^{g_j}); positivity for every finite family ⇔ RH (cit:weil-criterion).`;
  }
  draw();
};

/* =====================================================================================
   Demo: the CCM window at x = 13, N = 20 (precomputed): the Gram matrix of the Fourier-mode strips
   ===================================================================================== */
WT.demos.ccm = function(root){ const R = window.WT_RIEMANN13; if(!R){ WT.div(root,'readout','data-riemann.js missing'); return; }
  const g = WT.div(root, 'grid3'); const svgE = WT.svgIn(WT.div(g,''), '0 0 300 300', 'ccm_E'); WT.div(g.lastChild,'small','the even block of the window matrix Q_N (21×21), the Gram matrix of the Fourier-mode strips, from primes ≤ 13');
  const svgX = WT.svgIn(WT.div(g,''), '0 0 300 300', 'ccm_xi'); WT.div(g.lastChild,'small','its minimal eigenvector ξ (log₁₀|ξ_j|, sign by colour): the near-kernel direction, ε = λ_min');
  const svgR = WT.svgIn(WT.div(g,''), '0 0 300 300', 'ccm_roots'); WT.div(g.lastChild,'small','the secular roots z_k of D − |Dξ⟩⟨η| (dots) against the zeros γ_k (<span class="pill spec">comparison</span>, hollow)');
  const read = WT.div(root, 'readout', ''); read.id='ccm_read';
  const Col = WT.col(); const E = R.E, n = E.length; const cell = 260/n; const vmax = Math.max(...E.flat().map(Math.abs)); WT.svg.heat(svgE, E, 20, 28, cell, Col, {vmax, title:`x = 13, N = 20: entries in [${fmtF(Math.min(...E.flat()),3)}, ${fmtF(vmax,3)}]`});
  const xl = R.xiLog10Abs, xs = R.xiSign; const mx = Math.max(...xl); const X = j => 30 + j*(250/n), Y = v => 270 - v/mx*230; axis(svgX, 25, 270, 290, 270); xl.forEach((v,j)=>{ S('rect',{x:X(j), y:Y(v), width: 250/n-2, height: 270-Y(v), fill: xs[j]>0 ? Col.orbit : Col.spec}, svgX); }); txt(svgX, 30, 16, `ε = ${R.eps.toExponential(3)}; ξ spans ${fmtF(mx,1)} decades`, {fill:Col.ink}); txt(svgX, 30, 288, 'j = 0'); txt(svgX, 255, 288, 'j = 20');
  const gam = R.gamma, zk = R.zk; const ymax = 85; const Yr = v => 280 - v/ymax*260; axis(svgR, 60, 280, 60, 20); for (let v=0; v<=80; v+=20){ txt(svgR, 30, Yr(v)+4, String(v)); S('line',{x1:56,y1:Yr(v),x2:64,y2:Yr(v),stroke:Col.line},svgR); }
  gam.forEach((gv,i)=>{ if(gv<=ymax){ S('circle',{cx:150, cy:Yr(gv), r:5, fill:'none', stroke:Col.ink2, 'stroke-width':1.5}, svgR); } }); zk.forEach((z,i)=>{ if (z<=ymax) S('circle',{cx:150, cy:Yr(z), r:3.5, fill: Col.spec}, svgR); }); txt(svgR, 170, Yr(14.13)+4, 'γ₁ = 14.1347…'); txt(svgR, 170, Yr(56.4)+4, '|z_k − γ_k| grows'); txt(svgR, 70, 16, 'ordinates recovered from the kernel direction', {fill:Col.ink});
  read.innerHTML = `<span class="k">the window channel (Connes–Consani–Moscovici; shard 08g, 08i):</span> strips E^{u_n} with u_n(x) = L^{-1/2} e^{2πinx/L} on [0, L], L = log 13, |n| ≤ 20; Gram matrix (Q_N)_{nm} = Ψ(u_n^* ∗ u_m), computed from the prime powers ≤ 13, the pole and the archimedean term — the certified \`zst\` pipeline\n<span class="k">positivity:</span> the even block is positive definite with λ_min = ε = ${R.eps.toExponential(4)} (next even eigenvalue ${R.evenNext}, odd minimum ${R.oddMin}): the strips are very nearly dependent in one direction\n<span class="k">the spectrum from the near-kernel:</span> the CCM rank-one correction D′ = D − |Dξ⟩⟨η| has real spectrum; its values z_k = 2π s_k/L reproduce the zeros: |z_1 − γ_1| = ${R.err[0].toExponential(2)}, |z_5 − γ_5| = ${R.err[4].toExponential(2)}, |z_10 − γ_10| = ${R.err[9].toExponential(2)}, |z_12 − γ_12| = ${R.err[11].toExponential(2)} (comparison)\n<span class="k">TN reading:</span> the near-kernel vector ξ of the Gram matrix is the polynomial p_ξ(E) of strips that almost vanishes; in the finite examples the kernel polynomial's roots ARE the spectrum (Pisarenko); here the window is finite and the spectrum infinite, so ε > 0 and the roots approximate the low zeros, with the prime powers ≤ 13 pinning γ₁ to within 2.3·10⁻³⁵ (about 35 significant digits). Nothing here assumed RH; the zeros enter only in the comparison column.`;
};
})();
