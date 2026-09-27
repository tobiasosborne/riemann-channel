/* demos-graphs.js -- worker G: the classical Ihara–Bass station (regular graphs).
 * A (q+1)-regular graph read as an MPS: bond space C^{2|E|} (directed edges), one Kraus operator per
 * directed edge, A_e = sum_{e' follows e} |e'><e|, so the transfer matrix is the Hashimoto matrix B and the
 * ring norm Tr B^L counts closed non-backtracking walks. Every Weil form below is built from the matrix
 * powers of B (counts); eigenvalues appear only in panels marked "comparison".
 * Numerics live in WT.graphNum (callable without a DOM). Demos: WT.demos.graphWalk, WT.demos.graphs. */
(function(){
'use strict';
const WT = window.WT = window.WT || {};
WT.demos = WT.demos || {};

// ---------- the graphs, all built by code ----------
const cyc = (n, o=0) => Array.from({length:n}, (_,i) => [o+i, o+(i+1)%n]);
const prism = n => ({n: 2*n, edges: cyc(n).concat(cyc(n,n), Array.from({length:n}, (_,i)=>[i, i+n])), layout:'rings'});
const complete = n => { const E=[]; for(let i=0;i<n;i++) for(let j=i+1;j<n;j++) E.push([i,j]); return {n, edges:E, layout:'circle'}; };
const circulant = (n, S) => { const seen=new Set(), E=[]; for(let i=0;i<n;i++) for(const s of S){ const a=Math.min(i,(i+s)%n), b=Math.max(i,(i+s)%n), k=a+','+b; if(!seen.has(k)){ seen.add(k); E.push([a,b]); } } return {n, edges:E, layout:'circle'}; };
const petersen = () => ({n:10, edges: cyc(5).concat(Array.from({length:5},(_,i)=>[5+i, 5+(i+2)%5]), Array.from({length:5},(_,i)=>[i, i+5])), layout:'rings'});
const heawood = () => { const E = cyc(14); for(let i=0;i<14;i+=2) E.push([i, (i+5)%14]); return {n:14, edges:E, layout:'circle'}; }; // LCF [5,-5]^7
const k33 = () => { const E=[]; for(const i of [0,2,4]) for(const j of [1,3,5]) E.push([i,j]); return {n:6, edges:E, layout:'circle'}; };
const octa = () => { const E=[]; for(let i=0;i<6;i++) for(let j=i+1;j<6;j++) if(j!==i+3) E.push([i,j]); return {n:6, edges:E, layout:'circle'}; };
const LIST = [
  ['K4', 'K4 (q = 2)', ()=>complete(4)], ['Q3', 'cube Q3 = C4 × K2 (q = 2)', ()=>prism(4)], ['Petersen', 'Petersen (q = 2)', petersen],
  ['K33', 'K3,3 (q = 2)', k33], ['Heawood', 'Heawood (q = 2)', heawood], ['C6xK2', 'prism C6 × K2 (q = 2)', ()=>prism(6)],
  ['C16xK2', 'prism C16 × K2 (q = 2)', ()=>prism(16)], ['C21xK2', 'prism C21 × K2 (q = 2)', ()=>prism(21)],
  ['K5', 'K5 (q = 3)', ()=>complete(5)], ['Oct', 'octahedron K2,2,2 (q = 3)', octa], ['C8_12', 'circulant C8(1,2) (q = 3)', ()=>circulant(8,[1,2])]
];
const KT = 24;   // counts Tr B^l are kept for l = 0..KT (exact integers in double precision for q <= 3)
const cache = {};

/* everything on the counting side: B, its powers, Tr B^l, the trivial part, nu_l and h_k */
function analyse(key){
  if (cache[key]) return cache[key];
  const spec = LIST.find(g => g[0]===key); if (!spec) throw new Error('unknown graph '+key);
  const g = spec[2](), n = g.n, m = g.edges.length;
  const A = Array.from({length:n}, () => new Array(n).fill(0));
  g.edges.forEach(([u,v]) => { A[u][v] = A[v][u] = 1; });
  const deg = A.map(r => r.reduce((s,v)=>s+v, 0));
  if (deg.some(d => d!==deg[0])) throw new Error('the construction needs a regular graph');
  const q = deg[0]-1, D = 2*m;
  const darts = g.edges.map(e=>[e[0],e[1]]).concat(g.edges.map(e=>[e[1],e[0]]));   // dart i+m is the reverse of dart i
  const B = Array.from({length:D}, (_,i) => Array.from({length:D}, (_,j) => (darts[i][1]===darts[j][0] && j!==(i+m)%D) ? 1 : 0));
  const succ = B.map(r => r.reduce((s,v,j)=>(v? s.concat([j]) : s), []));
  const col = new Array(n).fill(-1); col[0] = 0; const st = [0]; let bip = true;   // bipartite by 2-colouring (structure, not spectrum)
  while (st.length){ const u = st.pop(); for (let v=0; v<n; v++) if (A[u][v]){ if (col[v]<0){ col[v] = 1-col[u]; st.push(v); } else if (col[v]===col[u]) bip = false; } }
  const P = [WT.eye(D)], trB = [D];
  for (let k=1; k<=KT; k++){ P.push(WT.matmul(B, P[k-1])); trB.push(WT.trace(P[k])); }
  const trA = WT.powerTraces(A, 12), ex = m - n, sg = l => (l%2 ? -1 : 1);
  const triv = trB.map((_,l) => Math.pow(q,l) + 1 + ex*(1+sg(l)) + (bip ? sg(l)*Math.pow(q,l) + sg(l) : 0));
  const nu = trB.map((t,l) => (t - triv[l]) / Math.pow(q, l/2));
  const h = nu.map(v => nu[0] - v);
  return cache[key] = {key, name: spec[1], n, m, q, D, ex, bip, A, B, darts, succ, P, trB, trA, triv, nu, h, layout: g.layout};
}

/* comparison only: adjacency eigenvalues (Jacobi) and the retained Hashimoto modes via Ihara–Bass */
function spectra(G){
  if (G.spec) return G.spec;
  const q = G.q, a = WT.jacobiEig(G.A).values.slice().reverse();
  const nontriv = a.slice(), drop = t => { let b=0; nontriv.forEach((x,i)=>{ if (Math.abs(x-t) < Math.abs(nontriv[b]-t)) b=i; }); nontriv.splice(b,1); };
  drop(q+1); if (G.bip) drop(-(q+1));
  const modes = [];
  nontriv.forEach(x => { const d = x*x - 4*q; if (d < 0){ const s = Math.sqrt(-d)/2; modes.push([x/2, s], [x/2, -s]); } else { const s = Math.sqrt(d)/2; modes.push([x/2+s, 0], [x/2-s, 0]); } });
  const amax = Math.max(...nontriv.map(Math.abs)), ram = amax <= 2*Math.sqrt(q) + 1e-9;
  let pw = modes.map(() => [1,0]), err = 0;
  for (let l=0; l<=16; l++){ const s = pw.reduce((acc,p)=>WT.C.add(acc,p), [0,0]), sc = Math.pow(q, l/2);
    err = Math.max(err, Math.hypot(s[0] - G.nu[l]*sc, s[1]) / sc); pw = pw.map((p,i) => WT.C.mul(p, modes[i])); }
  const muMax = Math.max(...modes.map(z => Math.hypot(z[0], z[1])));
  return G.spec = {a, nontriv, modes, amax, ram, err, muMax};
}

/* a random closed non-backtracking walk of length L: randomized depth-first search, pruned by the
   counts (B^k)[e][e1] > 0 so that no branch is a dead end; null if Tr B^L = 0 */
function closedWalk(G, L, rnd){
  rnd = rnd || Math.random; const P = G.P, starts = [];
  for (let e=0; e<G.D; e++) if (P[L][e][e] > 0) starts.push(e);
  if (!starts.length) return null;
  const e1 = starts[Math.floor(rnd()*starts.length)], w = [e1];
  const dfs = () => { if (w.length === L) return G.B[w[L-1]][e1] === 1;
    const c = G.succ[w[w.length-1]].slice(); for (let i=c.length-1; i>0; i--){ const j = Math.floor(rnd()*(i+1)); [c[i],c[j]] = [c[j],c[i]]; }
    for (const j of c){ if (P[L-w.length][j][e1] <= 0) continue; w.push(j); if (dfs()) return true; w.pop(); } return false; };
  return dfs() ? w : null;
}
const toeplitzMins = (G, K) => WT.toeplitzMins(G.nu, K+1);   // entry K' = lambda_min of (nu_|j-k|), j,k = 0..K'
WT.graphNum = {LIST, KT, analyse, spectra, closedWalk, toeplitzMins};

// ---------- drawing helpers ----------
const S = (...a) => WT.svg.el(...a), T = (...a) => WT.svg.text(...a);
const dlab = (G, e) => G.darts[e][0] + '→' + G.darts[e][1];
function positions(G, W, H){
  const cx = W/2, cy = H/2, R = Math.min(W,H)/2 - 20, pos = [];
  if (G.layout === 'rings'){ const h = G.n/2; for (let i=0; i<G.n; i++){ const t = -Math.PI/2 + 2*Math.PI*(i%h)/h, r = i<h ? R : 0.58*R; pos.push([cx + r*Math.cos(t), cy + r*Math.sin(t)]); } }
  else for (let i=0; i<G.n; i++){ const t = -Math.PI/2 + 2*Math.PI*i/G.n; pos.push([cx + R*Math.cos(t), cy + R*Math.sin(t)]); }
  return pos;
}
function arrow(svg, p, q, rv, color, w){
  const dx = q[0]-p[0], dy = q[1]-p[1], d = Math.hypot(dx,dy), ux = dx/d, uy = dy/d;
  const a = [p[0]+ux*rv, p[1]+uy*rv], b = [q[0]-ux*rv, q[1]-uy*rv], s = 4 + w;
  S('line', {x1:a[0], y1:a[1], x2:b[0], y2:b[1], stroke:color, 'stroke-width':w, 'stroke-linecap':'round'}, svg);
  S('polygon', {points: [b, [b[0]-ux*2*s - uy*s, b[1]-uy*2*s + ux*s], [b[0]-ux*2*s + uy*s, b[1]-uy*2*s - ux*s]].map(z=>z[0].toFixed(1)+','+z[1].toFixed(1)).join(' '), fill:color}, svg);
}
function drawGraph(svg, G, walk, pos, C){
  WT.svg.clear(svg); const P = positions(G, 320, 320), rv = G.n > 16 ? 6 : 9;
  G.darts.slice(0, G.m).forEach(([u,v]) => S('line', {x1:P[u][0], y1:P[u][1], x2:P[v][0], y2:P[v][1], stroke:C.line, 'stroke-width':1.4}, svg));
  if (walk) for (let i=0; i<pos; i++){ const [u,v] = G.darts[walk[i]]; if (i === pos-1) arrow(svg, P[u], P[v], rv, C.bond, 3.2); else arrow(svg, P[u], P[v], rv, C.orbit, 2.2); }
  P.forEach((p,i) => { S('circle', {cx:p[0], cy:p[1], r:rv, fill:C.bg2, stroke:C.ink, 'stroke-width':1.2}, svg);
    T(svg, p[0], p[1]+(rv>6?3.5:2.5), String(i), {'text-anchor':'middle', 'font-size': rv>6 ? 9 : 7, fill:C.ink}); });
}
function drawRing(svg, G, walk, pos, L, C){
  WT.svg.clear(svg); const cx = 160, cy = 160, R = 112;
  if (!walk){ T(svg, cx, cy, 'no closed non-backtracking walk of length '+L, {'text-anchor':'middle', fill:C.spec}); T(svg, cx, cy+18, 'Tr B^'+L+' = 0: every word of length '+L+' has Tr = 0', {'text-anchor':'middle', 'font-size':10}); return; }
  S('circle', {cx, cy, r:R, fill:'none', stroke:C.bond, 'stroke-width':1.6}, svg);
  for (let i=0; i<L; i++){ const t = -Math.PI/2 + 2*Math.PI*i/L, x = cx + R*Math.cos(t), y = cy + R*Math.sin(t), cur = i === pos-1, done = i < pos;
    S('line', {x1:x + 14*Math.cos(t), y1:y + 12*Math.sin(t), x2:x + 30*Math.cos(t), y2:y + 28*Math.sin(t), stroke:C.orbit, 'stroke-width':1.4}, svg);
    S('rect', {x:x-19, y:y-11, width:38, height:22, rx:3, fill: cur ? C.bondSoft : C.bg2, stroke: cur ? C.bond : C.ink, 'stroke-width': cur ? 2.4 : 1.2, opacity: done ? 1 : 0.45}, svg);
    T(svg, x, y+3.5, dlab(G, walk[i]), {'text-anchor':'middle', 'font-size':9, fill:C.ink, opacity: done ? 1 : 0.45});
    T(svg, x + 40*Math.cos(t), y + 37*Math.sin(t) + 3, 'e'+(i+1), {'text-anchor':'middle', 'font-size':9}); }
  T(svg, cx, cy-8, 'ring of '+L+' Kraus boxes A_e', {'text-anchor':'middle', 'font-size':10});
  T(svg, cx, cy+10, pos >= L ? 'Tr(A_eL ⋯ A_e1) = 1' : 'reading e1 … e'+pos, {'text-anchor':'middle', fill: pos >= L ? C.orbit : C.ink2});
}

// ---------- demo 1: a closed non-backtracking walk and its ring ----------
WT.demos.graphWalk = function(root){
  const id = 'demo-graphWalk', st = {key:'Petersen', L:5, walk:null, pos:0, timer:null};
  const ctr = WT.div(root, 'controls');
  WT.select(ctr, id+'-graph', 'graph', LIST.map(g=>[g[0], g[1]]), st.key, v => { st.key = v; fresh(); });
  WT.slider(ctr, id+'-L', 'length L', 3, 12, 1, st.L, v => { st.L = v; fresh(); });
  WT.button(ctr, id+'-new', 'new walk', () => fresh());
  const playB = WT.button(ctr, id+'-play', 'play', () => play());
  const grid = WT.div(root, 'grid2'), gsvg = WT.svgIn(grid, '0 0 320 320', id+'-svgGraph'), rsvg = WT.svgIn(grid, '0 0 320 320', id+'-svgRing');
  const out = WT.div(root, 'readout'); out.id = id+'-readout';
  const tbl = WT.div(root, ''); tbl.id = id+'-counts'; tbl.style.overflowX = 'auto'; tbl.style.marginTop = '10px';
  function stop(){ if (st.timer) clearInterval(st.timer); st.timer = null; playB.textContent = 'play'; }
  function play(){ if (st.timer){ stop(); return; } if (!st.walk) return;
    if (WT.reducedMotion()){ st.pos = st.walk.length; render(); return; }
    st.pos = 1; render(); playB.textContent = 'pause';
    st.timer = setInterval(() => { if (st.pos >= st.walk.length){ stop(); return; } st.pos++; render(); }, 650); }
  function fresh(){ stop(); const G = analyse(st.key); st.walk = closedWalk(G, st.L); st.pos = st.walk ? st.L : 0; render(); table(G); }
  function render(){
    const G = analyse(st.key), C = WT.col(), L = st.L;
    drawGraph(gsvg, G, st.walk, st.pos, C); drawRing(rsvg, G, st.walk, st.pos, L, C);
    const word = st.walk ? st.walk.map(e => dlab(G,e)).join(', ') : '—';
    out.textContent = G.name + ': |V| = ' + G.n + ', |E| = ' + G.m + ', bond dimension 2|E| = ' + G.D + ' (one Kraus operator A_e per directed edge)\n'
      + (st.walk ? 'word e1 … e' + L + ' = ' + word + (st.pos < L ? '   [step ' + st.pos + ' of ' + L + ']' : '') + '\n'
        + 'Tr(A_{e_L}...A_{e_1}) = 1 for this word; ring norm Tr B^' + L + ' = ' + G.trB[L] + ' closed non-backtracking walks of length ' + L
      : 'no closed non-backtracking walk of length ' + L + ' exists on this graph (Tr B^' + L + ' = 0), so every word of length ' + L + ' has Tr(A_{e_L}...A_{e_1}) = 0')
      + ' (each counted from every starting edge); all closed walks, backtracking allowed, Tr A^' + L + ' = ' + G.trA[L];
  }
  function table(G){
    const ls = Array.from({length:12}, (_,i)=>i+1), td = v => '<td class="num">' + v + '</td>';
    tbl.innerHTML = '<table class="tbl"><tr><th>l</th>' + ls.map(td).join('') + '</tr><tr><th class="orbit" style="text-transform:none">Tr B^l</th>' + ls.map(l=>td(G.trB[l])).join('')
      + '</tr><tr><th style="text-transform:none">Tr A^l</th>' + ls.map(l=>td(G.trA[l])).join('') + '</tr></table>';
  }
  fresh();
};

// ---------- demo 2: spectrum (comparison) versus the counting side ----------
function badge(svg, W, C){ T(svg, W-6, 26, 'comparison', {'text-anchor':'end', 'font-size':10, fill:C.ink2, 'font-style':'italic'}); }
function groups(vals, tol){ const g = []; vals.forEach(v => { const f = g.find(x => Math.abs(x.v[0]-v[0]) < tol && Math.abs(x.v[1]-v[1]) < tol); if (f) f.m++; else g.push({v, m:1}); }); return g; }
function drawAdj(svg, G, sp, C){
  WT.svg.clear(svg); const q = G.q, lo = -(q+1)-0.6, hi = q+1+0.6, X = x => 20 + (x-lo)/(hi-lo)*420, y0 = 92, b = 2*Math.sqrt(q);
  T(svg, 6, 12, '(a) adjacency spectrum a_i (Jacobi on A)', {fill:C.ink}); badge(svg, 460, C);
  S('rect', {x:X(-b), y:28, width:X(b)-X(-b), height:y0-28, fill:C.bg3, stroke:C.ink2, 'stroke-dasharray':'3 3'}, svg);
  T(svg, X(-b), y0+24, '−2√q', {'text-anchor':'middle', 'font-size':10}); T(svg, X(b), y0+24, '2√q', {'text-anchor':'middle', 'font-size':10});
  T(svg, X(0), 40, 'Ramanujan band', {'text-anchor':'middle', 'font-size':10});
  WT.svg.axis(svg, 14, y0, 446, y0);
  for (let k = -(q+1); k <= q+1; k++){ S('line', {x1:X(k), y1:y0, x2:X(k), y2:y0+4, stroke:C.ink2}, svg); T(svg, X(k), y0+13, String(k), {'text-anchor':'middle', 'font-size':9}); }
  const triv = [q+1].concat(G.bip ? [-(q+1)] : []);
  groups(sp.nontriv.map(x=>[x,0]), 1e-6).forEach(g => { for (let k=0; k < Math.min(g.m,6); k++) S('circle', {cx:X(g.v[0]), cy:y0-6-7*k, r:3.2, fill:C.spec}, svg);
    if (g.m > 6) T(svg, X(g.v[0]), y0-6-7*6-2, '×'+g.m, {'text-anchor':'middle', 'font-size':9}); });
  triv.forEach(t => { S('circle', {cx:X(t), cy:y0-6, r:4.5, fill:C.pole}, svg); T(svg, X(t), y0-14, t > 0 ? 'q+1' : '−(q+1)', {'text-anchor':'middle', 'font-size':9, fill:C.pole}); });
}
function drawPlane(svg, G, sp, C){
  WT.svg.clear(svg); const q = G.q, r = Math.sqrt(q), sc = 118/(q+0.4), P = WT.svg.plane(svg, 150, 158, sc, r, C);
  T(svg, 6, 12, '(b) Hashimoto spectrum, μ² − aμ + q = 0', {fill:C.ink}); badge(svg, 300, C);
  WT.svg.axis(svg, P.X(-q-0.35), P.Y(0), P.X(q+0.35), P.Y(0), 'grid');
  T(svg, P.X(r*0.72)+4, P.Y(r*0.72)-4, '|μ| = √q', {'font-size':10});
  const gm = groups(sp.modes, 1e-6); gm.forEach(g => { S('circle', {cx:P.X(g.v[0]), cy:P.Y(g.v[1]), r:4, fill:C.spec, opacity:.9}, svg);
    if (g.m > 1 && gm.length <= 12) T(svg, P.X(g.v[0])+6, P.Y(g.v[1])-5, '×'+g.m, {'font-size':9}); });
  const triv = [[q,'q'],[1,'1']].concat(G.bip ? [[-q,'−q'],[-1,'−1']] : []);
  triv.forEach(([x,s]) => { S('circle', {cx:P.X(x), cy:P.Y(0), r:5, fill:'none', stroke:C.pole, 'stroke-width':2.2}, svg); T(svg, P.X(x), P.Y(0)-9, s, {'text-anchor':'middle', 'font-size':10, fill:C.pole}); });
  [-1, 1].forEach(x => S('rect', {x:P.X(x)-3, y:P.Y(0)+10, width:6, height:6, fill:C.pole}, svg));
  T(svg, 150, 292, '■ ±1 × ' + G.ex + ' each: the (1−u²)^(|E|−|V|) factor', {'text-anchor':'middle', 'font-size':9, fill:C.pole});
}
function drawBars(svg, vals, from, K, title, signed, C, refLine){
  WT.svg.clear(svg); const n = vals.length - from, w = 420/n, x0 = 30, y0 = 110, vm = Math.max(1e-9, ...vals.slice(from).map(Math.abs), refLine||0), hs = 82/vm;
  T(svg, 6, 12, title, {fill:C.ink}); WT.svg.axis(svg, x0, y0, x0 + n*w, y0);
  const v = vals.slice(from).map(x => Math.abs(x) < 1e-9 ? 0 : x), inW = v.map((_,i) => i+from <= K);
  v.forEach((x,i) => WT.svg.bars(svg, [x], x0 + i*w, y0, w, hs, C, {color: signed ? (x >= 0 ? C.orbit : C.spec) : C.orbit, opacity: inW[i] ? .9 : .3}));
  for (let i=0; i<n; i+=4) T(svg, x0 + i*w + w/2, y0 + 96, String(i+from), {'text-anchor':'middle', 'font-size':9});
  if (refLine){ S('line', {x1:x0, y1:y0 - refLine*hs, x2:x0 + n*w, y2:y0 - refLine*hs, stroke:C.ink2, 'stroke-dasharray':'4 3'}, svg); T(svg, x0-4, y0 - refLine*hs + 3, 'ν₀', {'text-anchor':'end', 'font-size':10}); }
  T(svg, x0 + (K-from+1)*w, 26, '← window 0..K', {'font-size':9});
}
function drawMins(svg, mins, K, C){
  WT.svg.clear(svg); const lo = Math.min(0, ...mins), hi = Math.max(1e-9, ...mins), X = k => 40 + k*(240/Math.max(1,K)), Y = v => 40 + (hi - v)/(hi - lo || 1)*220;
  T(svg, 6, 12, 'λ_min of the window 0..K′ (Jacobi)', {fill:C.ink}); WT.svg.axis(svg, 36, Y(0), 284, Y(0));
  T(svg, 32, Y(0)+3, '0', {'text-anchor':'end', 'font-size':9}); if (lo < -1e-6) T(svg, 32, Y(lo)+3, WT.fmt(lo,3), {'text-anchor':'end', 'font-size':9}); if (hi > 1e-6) T(svg, 32, Y(hi)+3, WT.fmt(hi,3), {'text-anchor':'end', 'font-size':9});
  WT.svg.polyline(svg, mins.map((v,k) => [X(k), Y(v)]), C.line, 1.2);
  mins.forEach((v,k) => { S('circle', {cx:X(k), cy:Y(v), r: k===K ? 5 : 3.4, fill: v >= -1e-9 ? C.orbit : C.spec}, svg); if (k%2===0 || k===K) T(svg, X(k), 292, String(k), {'text-anchor':'middle', 'font-size':9}); });
  T(svg, 284, 280, 'K′', {'text-anchor':'end', 'font-size':9});
}
WT.demos.graphs = function(root){
  const id = 'demo-graphs', st = {key:'Petersen', K:12};
  const ctr = WT.div(root, 'controls');
  WT.select(ctr, id+'-graph', 'graph', LIST.map(g=>[g[0], g[1]]), st.key, v => { st.key = v; render(); });
  WT.slider(ctr, id+'-K', 'window K', 2, 16, 1, st.K, v => { st.K = v; render(); });
  const g1 = WT.div(root, 'grid2'), col1 = WT.div(g1, ''), sA = WT.svgIn(col1, '0 0 460 130', id+'-adj'), sB = WT.svgIn(g1, '0 0 300 300', id+'-hash');
  const sN = WT.svgIn(col1, '0 0 460 216', id+'-nu'), sH = WT.svgIn(col1, '0 0 460 216', id+'-huang');
  const g3 = WT.div(root, 'grid2'), sT = WT.svgIn(g3, '0 0 300 300', id+'-heat'), sM = WT.svgIn(g3, '0 0 300 300', id+'-mins');
  const out = WT.div(root, 'readout'); out.id = id+'-readout';
  function render(){
    const G = analyse(st.key), sp = spectra(G), C = WT.col(), K = st.K, q = G.q;
    drawAdj(sA, G, sp, C); drawPlane(sB, G, sp, C);
    drawBars(sN, G.nu, 0, K, '(c) ν_l = q^(−l/2)(Tr B^l − trivial_l), from counts', false, C, G.nu[0]);
    drawBars(sH, G.h, 1, K, 'Huang h_k = ν₀ − ν_k (≥ 0 for all k ⇔ Ramanujan)', true, C);
    WT.svg.clear(sT); const cell = Math.floor(256/(K+1));
    WT.svg.heat(sT, WT.toeplitz(G.nu, K+1), 30, 30, cell, C, {numbers: cell >= 26, digits:1}); T(sT, 6, 12, '(d) Weil matrix (ν_|j−k|), j,k = 0..' + K, {fill:C.ink});
    const mins = toeplitzMins(G, K), lm = mins[K], hmin = G.h.slice(1).reduce((b,v,i) => v < b.v ? {v, k:i+1} : b, {v:Infinity, k:0});
    drawMins(sM, mins, K, C);
    const trivS = '{q, 1}' + (G.bip ? ' ∪ {−q, −1}' : '') + ' ∪ {+1, −1} × ' + G.ex;
    out.innerHTML = G.name + ':  |V| = ' + G.n + ', |E| = ' + G.m + ', |E|−|V| = ' + G.ex + ', q = ' + q + ', bipartite: ' + (G.bip ? 'yes' : 'no') + '\n'
      + 'trivial set S = ' + trivS + ' = {' + q + ', 1' + (G.bip ? ', −' + q + ', −1' : '') + '} ∪ {±1 × ' + G.ex + '};  critical radius r = √q = ' + WT.fmtF(Math.sqrt(q), 6) + '\n'
      + 'ν_0 = 2|V| − ' + (G.bip ? 4 : 2) + ' = ' + WT.fmtF(G.nu[0], 0) + ';  ν_l = q^(−l/2)(Tr B^l − q^l − 1 − (|E|−|V|)(1+(−1)^l)' + (G.bip ? ' − (−q)^l − (−1)^l' : '') + ')\n'
      + 'λ_min of the Toeplitz window (ν_|j−k|), j,k = 0..' + K + ':  <span class="' + (lm >= -1e-9 ? 'orbit' : 'spec') + '">' + WT.fmtF(lm, 4) + (lm >= -1e-9 ? '  (positive semidefinite)' : '  (negative: Weil positivity fails)') + '</span>\n'
      + 'min h_k over k = 1..' + KT + ':  <span class="' + (hmin.v >= -1e-9 ? 'orbit' : 'spec') + '">' + WT.fmtF(hmin.v, 4) + ' at k = ' + hmin.k + '</span>\n'
      + 'comparison: ' + (sp.ram ? '<span class="orbit">Ramanujan</span> (max nontrivial |a| = ' + WT.fmtF(sp.amax, 4) + ' ≤ 2√q = ' + WT.fmtF(2*Math.sqrt(q), 4) + ')'
        : '<span class="spec">not Ramanujan (a = ' + WT.fmtF(sp.amax, 4) + ' > 2√q = ' + WT.fmtF(2*Math.sqrt(q), 4) + ')</span>')
      + ';  max retained |μ| = ' + WT.fmtF(sp.muMax, 6) + ';  max over l ≤ 16 of |Σ retained μ^l − q^(l/2) ν_l| / q^(l/2) = ' + WT.fmt(sp.err, 2) + '\n'
      + 'the Weil form is positive semidefinite iff every retained mode lies on |μ| = √q (thm:weil-duality-pairing); '
      + 'the retained set is invariant under μ → q/μ because every edge has a reverse (inverse pairing).';
  }
  render();
};
})();
