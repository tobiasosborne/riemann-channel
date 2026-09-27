/* tn.js -- worker TN for "Weil Positivity, Contracted": a small tensor-network diagram renderer on SVG
 * (WT.tn) and four storyboard movies (WT.demos.movieRing, movieGram, movieMetric, movieCircle).
 * Plain ES2020, no libraries. Colours only through theme.css classes (.tn-*) or var(--token).
 * Every movie draws as a pure function of t in [0,1]; WT.movie clears the SVG before each frame.
 * Maths: report/sections/03g_ccm_tensor_gram.tex (prop:ccm-tn-operator-gram), 02i (def:ccm-tn-feature),
 * 08b (thm:weil-positivity-finite, thm:weil-duality-pairing), 08c (prop:hp-inner-product-discrete). */
(function(){
'use strict';
const WT = window.WT = window.WT || {};
WT.demos = WT.demos || {};
const E = (tag, a, p) => WT.svg.el(tag, a, p);
const T = WT.tn = {};

// ---------- interpolation helpers ----------
T.clamp = x => x < 0 ? 0 : x > 1 ? 1 : x;
T.ease = s => s*s*(3-2*s);
/* eased progress of t through the window [a,b]: 0 before, 1 after */
T.seg = (t, a, b) => T.ease(T.clamp((t-a)/(b-a)));
T.lerp = (a, b, s) => a + (b-a)*s;
T.lerpPt = (p, q, s) => [T.lerp(p[0], q[0], s), T.lerp(p[1], q[1], s)];
T.g = (p, attrs) => E('g', attrs || {}, p);
const opv = o => (o && o.op != null) ? o.op : 1;
const f1 = v => (+v).toFixed(1);

// ---------- primitives ----------
/* text; "^{..}" and "_{..}" become raised / lowered tspans. o: {cls, op, size, anchor, fill, weight} */
T.label = (p, x, y, s, o = {}) => { const op = opv(o); if (op <= 0.004) return null;
  const fs = o.size || (/tn-dim/.test(o.cls || '') ? 10 : 12);
  const t = E('text', {x: f1(x), y: f1(y), class: o.cls || 'tn-label', 'text-anchor': o.anchor || 'middle', opacity: op,
    style: 'white-space:pre;font-size:'+fs+'px' + (o.fill ? ';fill:'+o.fill : '') + (o.weight ? ';font-weight:'+o.weight : '')}, p);
  let cur = 0; const put = (str, lev) => { if (!str) return; const sp = E('tspan', {}, t); const d = (cur-lev)*0.38*fs;
    if (d) sp.setAttribute('dy', d.toFixed(1)); if (lev) sp.setAttribute('style', 'font-size:'+(0.72*fs).toFixed(1)+'px'); sp.textContent = str; cur = lev; };
  const re = /([\^_])\{([^}]*)\}/g; let i = 0, m;
  while ((m = re.exec(s))) { put(s.slice(i, m.index), 0); put(m[2], m[1] === '^' ? 1 : -1); i = re.lastIndex; }
  put(s.slice(i), 0); return t; };
/* tensor box centred at (x,y); cls '' | 'bar' (conjugate layer) | 'metric' (G seams) | 'trivial' */
T.box = (p, x, y, w, h, label, cls, o = {}) => { const op = opv(o); if (op <= 0.004 || w <= 0.5) return;
  E('rect', {x: f1(x-w/2), y: f1(y-h/2), width: f1(w), height: f1(h), rx: Math.min(5, w/4).toFixed(1), class: 'tn-box '+(cls || ''), opacity: op}, p);
  if (label && w > 14) T.label(p, x, y+4, label, {op, size: o.size}); };
/* leg between anchors a, b; cls 'bond' | 'phys' | 'doubled' */
T.leg = (p, a, b, cls, o = {}) => { const op = opv(o); if (op <= 0.004) return;
  E('line', {x1: f1(a[0]), y1: f1(a[1]), x2: f1(b[0]), y2: f1(b[1]), class: 'tn-leg '+(cls || ''), opacity: op}, p); };
/* dangling leg from a by (dx,dy), open end marked with a small hollow dot */
T.dangle = (p, a, dx, dy, cls, o = {}) => { const op = opv(o); if (op <= 0.004) return; const b = [a[0]+dx, a[1]+dy];
  T.leg(p, a, b, cls, o); E('circle', {cx: f1(b[0]), cy: f1(b[1]), r: 2.6, class: 'tn-leg '+(cls || ''), style: 'fill:var(--bg2)', opacity: op}, p); };
/* any path as a leg; o.draw in [0,1] draws it progressively */
T.path = (p, d, cls, o = {}) => { const op = opv(o); if (op <= 0.004 || (o.draw != null && o.draw <= 0.002)) return;
  const at = {d, class: 'tn-leg '+(cls || ''), opacity: op}; if (o.draw != null && o.draw < 1) { at.pathLength = 1; at['stroke-dasharray'] = o.draw.toFixed(4)+' 2'; }
  E('path', at, p); };
/* a chain of site tensors: o = {xs | x0,dx,n, y, w, h, label (string | i=>string), cls, phys (-1 up, +1 down, 0 none), pl, ends, bond, op} */
T.chain = (p, o) => { const n = o.xs ? o.xs.length : o.n, xs = o.xs || Array.from({length: n}, (_, i) => o.x0 + i*o.dx);
  const w = o.w || 44, h = o.h || 34, y = o.y, op = opv(o), bc = o.bond || 'bond', en = o.ends || 0;
  for (let i = 0; i+1 < n; i++) T.leg(p, [xs[i]+w/2, y], [xs[i+1]-w/2, y], bc, {op});
  if (en) { T.dangle(p, [xs[0]-w/2, y], -en, 0, bc, {op}); T.dangle(p, [xs[n-1]+w/2, y], en, 0, bc, {op}); }
  if (o.phys) xs.forEach(x => T.dangle(p, [x, y+o.phys*h/2], 0, o.phys*(o.pl || 26), 'phys', {op: op*(o.physOp == null ? 1 : o.physOp)}));
  xs.forEach((x, i) => T.box(p, x, y, w, h, typeof o.label === 'function' ? o.label(i) : o.label, o.cls, {op}));
  return {xs, L: [xs[0]-w/2-en, y], R: [xs[n-1]+w/2+en, y], w, h}; };
/* ket chain over bra chain with contracted physical legs; merge in [0,1] fuses each column into one tall E box
   and moves the two bond lines together into a doubled leg. o = {xs, yK, yB, w, h, op, braOp, braDy, contract, merge, ends} */
T.doubled = (p, o) => { const xs = o.xs, n = xs.length, w = o.w || 44, h = o.h || 34, op = opv(o), m = o.merge || 0, en = o.ends || 0;
  const ym = (o.yK+o.yB)/2, yB = o.yB + (o.braDy || 0), bo = o.braOp == null ? 1 : o.braOp, W = T.lerp(w, w+14, m);
  const y1 = T.lerp(o.yK, ym-4, m), y2 = T.lerp(yB, ym+4, m);
  const wire = (y, a, ww) => { for (let i = 0; i+1 < n; i++) { T.leg(p, [xs[i]+ww/2, y], [xs[i+1]-ww/2, y], 'bond', {op: a*(1-m)}); T.leg(p, [xs[i]+ww/2, y], [xs[i+1]-ww/2, y], 'doubled', {op: a*m}); }
    if (en) for (const [x0, s] of [[xs[0]-ww/2, -1], [xs[n-1]+ww/2, 1]]) { T.leg(p, [x0, y], [x0+s*en, y], 'bond', {op: a*(1-m)}); T.leg(p, [x0, y], [x0+s*en, y], 'doubled', {op: a*m}); } };
  wire(y1, op, W); wire(y2, op*bo, W);
  xs.forEach(x => T.leg(p, [x, o.yK+h/2], [x, yB-h/2], 'phys', {op: op*(o.contract || 0)*(1-m)}));
  xs.forEach((x, i) => { T.box(p, x, o.yK, w, h, o.labelK ? o.labelK(i) : 'A_{s}', '', {op: op*(1-m)}); T.box(p, x, yB, w, h, o.labelB ? o.labelB(i) : 'Ā_{s}', 'bar', {op: op*bo*(1-m)}); });
  xs.forEach(x => T.box(p, x, ym, W, T.lerp(h, o.yB-o.yK+h, m), 'E', '', {op: op*m, size: 15}));
  return {L: [xs[0]-W/2-en, ym], R: [xs[n-1]+W/2+en, ym]}; };
/* closes a chain into a ring: from the right end (xr,y) around below at depth Y back to the left end (xl,y) */
T.ring = (p, xl, xr, y, Y, k, cls, o = {}) => T.path(p, `M${f1(xr)},${f1(y)} C${f1(xr+k)},${f1(y)} ${f1(xr+k)},${f1(Y)} ${f1(xr)},${f1(Y)} L${f1(xl)},${f1(Y)} C${f1(xl-k)},${f1(Y)} ${f1(xl-k)},${f1(y)} ${f1(xl)},${f1(y)}`, cls, o);
/* glue arc joining the end a of one strip to the end b of another, bulging to side (-1 left, +1 right); returns its apex */
T.glue = (p, a, b, side, bul, cls, o = {}) => { T.path(p, `M${f1(a[0])},${f1(a[1])} C${f1(a[0]+side*bul)},${f1(a[1])} ${f1(b[0]+side*bul)},${f1(b[1])} ${f1(b[0])},${f1(b[1])}`, cls, o);
  return [(a[0]+b[0])/2 + side*0.75*bul, (a[1]+b[1])/2]; };
/* a closed ring of n transfer boxes drawn small: doubled circle with n beads (t_n = Tr E^n) */
T.loop = (p, cx, cy, R, n, o = {}) => { const op = opv(o); if (op <= 0.004) return;
  for (const d of [-3, 3]) E('circle', {cx: f1(cx), cy: f1(cy), r: R+d, class: 'tn-leg doubled', opacity: op}, p);
  for (let i = 0; i < n; i++) { const a = -Math.PI/2 + 2*Math.PI*i/n; T.box(p, cx+R*Math.cos(a), cy+R*Math.sin(a), 12, 12, '', '', {op}); } };
/* visibility of an item living on [a,b] of the timeline: short fade in and out, no overlap with its neighbours */
T.live = (t, a, b) => (a <= 0 ? 1 : T.seg(t, a-0.015, a))*(b >= 1 ? 1 : 1-T.seg(t, b-0.035, b-0.015));
/* right-hand "blackboard" of formula lines */
const board = (p, x, y, lines, op, size) => lines.forEach((s, i) => T.label(p, x, y+i*(size+10), s, {op, size, anchor: 'start'}));
const sceneCaps = (frames) => frames.map(([t, caption]) => ({t, caption}));

// ================= movie 1: the ring norm =================
WT.demos.movieRing = function(root){
  const xs = [250, 360, 470, 580, 690], yK = 112, yB = 202, w = 46, h = 36, ym = (yK+yB)/2;
  WT.movie(root, {id: 'movieRing', viewBox: '0 0 940 300', duration: 14, autoplay: false, frames: sceneCaps([
    [0, 'An MPS on <b>L = 5</b> sites: every site tensor A<sub>s</sub> is a D×D matrix for each physical letter s (green legs), multiplied along the bond legs (blue). The amplitude of the word s<sub>1</sub>…s<sub>L</sub> is Tr A<sub>s<sub>L</sub></sub>⋯A<sub>s<sub>1</sub></sub>.'],
    [0.2, 'Put the complex-conjugate copy Ā<sub>s</sub> underneath (the bra layer) and contract the physical legs pairwise. Per site what remains is the <b>transfer matrix E = Σ<sub>s</sub> A<sub>s</sub> ⊗ Ā<sub>s</sub></b>, acting on the doubled bond ℂ<sup>D</sup> ⊗ ℂ̄<sup>D</sup> ≅ End(ℂ<sup>D</sup>) (violet doubled legs).'],
    [0.45, 'Join the two ends (a periodic boundary): the closed network is the squared norm <b>‖ψ<sub>L</sub>‖² = Tr E<sup>L</sup> = Σ<sub>w</sub> |Tr A<sub>s<sub>L</sub></sub>⋯A<sub>s<sub>1</sub></sub>|²</b>, a sum over all words w = s<sub>1</sub>…s<sub>L</sub> of squared ring amplitudes, hence ≥ 0.'],
    [0.7, 'Shrink each ring to a circle: <b>t<sub>L</sub> = Tr E<sup>L</sup></b>, L = 1, 2, 3, …. The counting side is the sequence of ring norms, and it assembles into the zeta function <b>ζ<sub>E</sub>(u) = exp(Σ<sub>L≥1</sub> t<sub>L</sub> u<sup>L</sup>/L) = 1/det(1 − uE)</b>.']]),
    draw(svg, t){
      const a1 = T.seg(t, 0.2, 0.29), c = T.seg(t, 0.27, 0.34), m = T.seg(t, 0.34, 0.43), cl = T.seg(t, 0.46, 0.62);
      const shrink = T.seg(t, 0.71, 0.83), row = T.seg(t, 0.82, 0.95);
      const g = T.g(svg), tx = T.lerp(0, 638-470, shrink), ty = T.lerp(0, 150-190, shrink), sc = T.lerp(1, 0.13, shrink);
      g.setAttribute('transform', `translate(${f1(470+tx)},${f1(190+ty)}) scale(${sc.toFixed(3)}) translate(-470,-190)`);
      g.setAttribute('opacity', (1-T.seg(t, 0.74, 0.83)).toFixed(3));
      const opk = i => T.seg(t, 0.01+0.025*i, 0.05+0.025*i)*(1-a1), lk = i => 'A_{s'+(i+1)+'}';
      xs.forEach((x, i) => { T.dangle(g, [x, yK-h/2], 0, -30, 'phys', {op: opk(i)}); T.label(g, x, yK-h/2-38, 's_{'+(i+1)+'}', {cls: 'tn-dim', op: opk(i), size: 12}); });
      T.label(svg, 470, 30, 'ψ_{L} = Σ_{w} Tr(A_{sL}⋯A_{s1}) |s_{1}…s_{L}⟩', {op: T.seg(t, 0.08, 0.14)*(1-a1), size: 14});
      if (a1 <= 0) { // scene 1: the ket chain alone, sites appearing one by one, physical legs up
        T.chain(g, {xs, y: yK, w, h, label: '', ends: 26, op: opk(4)}); xs.forEach((x, i) => T.box(g, x, yK, w, h, lk(i), '', {op: opk(i)})); }
      else { const r = T.doubled(g, {xs, yK, yB, w, h, braOp: a1, braDy: (1-a1)*70, contract: c, merge: m, ends: 26, labelK: lk, labelB: i => 'Ā_{s'+(i+1)+'}'});
        // scene 3: close into a ring (two lines of the doubled leg, outer and inner)
        T.ring(g, r.L[0], r.R[0], ym-4, 272, 34, 'doubled', {draw: cl}); T.ring(g, r.L[0], r.R[0], ym+4, 264, 26, 'doubled', {draw: cl}); }
      T.label(svg, 470, 30, 'E = Σ_{s} A_{s} ⊗ Ā_{s}   on the doubled bond', {op: m*(1-cl), size: 14});
      T.label(svg, 470, 30, '‖ψ_{L}‖^{2} = Tr E^{L} = Σ_{w} |Tr A_{w}|^{2} ≥ 0', {op: cl*(1-shrink), size: 14});
      // scene 4: the row of ring norms t_1..t_6
      for (let L = 1; L <= 6; L++) { const cx = 470 + (L-3.5)*112, op = L === 5 ? shrink : row;
        T.loop(svg, cx, 150, 26, L, {op}); T.label(svg, cx, 205, 't_{'+L+'} = Tr E^{'+L+'}', {op, size: 13}); }
      T.label(svg, 470, 262, 'the counting side:  t_{L} = Tr E^{L},   ζ_{E}(u) = exp(Σ t_{L} u^{L}/L) = 1/det(1 − uE)', {op: row, size: 14});
    }});
};

// ================= movies 2 and 3: open strips glued into a Gram entry =================
const GG = {yT: 100, yB: 200, xs: [150, 220, 290, 360], w: 46, h: 34, xl: 100, xr: 410, bul: 46};
/* q = {flip, glue, kill, tight, seam, split, op}: the top strip E^j (j=2) and the bottom strip E^k (k=4) */
function glued(p, q){ const {yT, yB, xs, w, h, bul} = GG, j = 2, op = q.op == null ? 1 : q.op;
  const flip = q.flip || 0, glue = q.glue || 0, kill = q.kill || 0, seam = q.seam || 0, split = q.split || 0;
  const xl = T.lerp(GG.xl, xs[2]-w/2-24, q.tight || 0), xr = GG.xr, ym = (yT+yB)/2;
  const pf = i => i < j ? 1 - T.seg(kill, i/j, (i+1)/j) : 1, caps = T.seg(split, 0.45, 0.9), tl = caps > 0.5;
  const cT = (xs[0]+xs[1])/2, cf = Math.cos(Math.PI*flip), topR = T.lerp(xs[1]+w/2+27, xr, glue);
  // wires (each one a doubled-bond index), glue arcs, dangling ends
  T.leg(p, [xl, yT], [topR, yT], 'bond', {op}); T.leg(p, [xl, yB], [xr, yB], 'bond', {op});
  for (const e of [[xl, yT], [topR, yT], [xl, yB], [xr, yB]]) E('circle', {cx: f1(e[0]), cy: f1(e[1]), r: 2.6, class: 'tn-leg bond', style: 'fill:var(--bg2)', opacity: op*(1-glue)}, p);
  const aL = T.glue(p, [xl, yT], [xl, yB], -1, bul, 'bond', {draw: glue, op}), aR = T.glue(p, [xr, yT], [xr, yB], 1, bul, 'bond', {draw: glue, op});
  // bottom strip E^k
  xs.forEach((x, i) => { const o = op*pf(i); T.box(p, x, yB, w, h, tl ? 'Ẽ' : 'E', '', {op: o, size: 14});
    for (const s of [-1, 1]) T.box(p, x+s*(w/2+4), yB, 6, h-6, '', 'metric', {op: o*caps}); });
  // top strip: flips about its centre (order reversed), becoming the adjoint (E^j)^*
  [xs[0], xs[1]].forEach((x, i) => { const X = cT + (x-cT)*cf, o = op*pf(Math.abs(cf) > 0 && cf < 0 ? 1-i : i);
    T.box(p, X, yT, w*Math.max(0.04, Math.abs(cf)), h, flip > 0.5 ? (tl ? 'Ẽ^{*}' : 'E^{*}') : 'E', flip > 0.5 ? 'bar' : '', {op: o, size: 14});
    T.label(p, X, yT-h/2-7, String(i+1), {cls: 'tn-dim', op: o*(1-q.glue*0.999)*(1-caps)});
    for (const s of [-1, 1]) T.box(p, X+s*(w/2+4), yT, 6, h-6, '', 'metric', {op: o*caps}); });
  // metric seams: G on the left glue (where (E^j)^* meets E^k), G^{-1} on the right; they split into G^{1/2} halves that slide in
  const so = op*seam*(1-T.seg(split, 0.05, 0.25));
  T.box(p, aL[0], aL[1], 38, 26, 'G', 'metric', {op: so}); T.box(p, aR[0], aR[1], 38, 26, 'G^{−1}', 'metric', {op: so});
  const tok = op*seam*T.seg(split, 0.02, 0.2)*(1-T.seg(split, 0.55, 0.8)), f = T.seg(split, 0.1, 0.55);
  for (const [a, tgt, lab] of [[aL, [xs[0]-w/2-10, yT], 'G^{½}'], [aL, [xs[0]-w/2-10, yB], 'G^{½}'], [aR, [xs[1]+w/2+10, yT], 'G^{−½}'], [aR, [xs[3]+w/2+10, yB], 'G^{−½}']]) {
    const P = T.lerpPt([a[0], a[1] + (tgt[1] < ym ? -16 : 16)], tgt, f); T.box(p, P[0], P[1], 32, 20, lab, 'metric', {op: tok, size: 10}); }
  return {aL, aR}; }

WT.demos.movieGram = function(root){
  WT.movie(root, {id: 'movieGram', viewBox: '0 0 940 320', duration: 16, autoplay: false, frames: sceneCaps([
    [0, 'From here on E is the rescaled retained transfer operator (trivial modes removed, divided by the critical radius r), and t<sub>l</sub> = Tr E<sup>l</sup>. Leave its bond legs open: the <b>open strips E<sup>j</sup></b> (top, j = 2) and <b>E<sup>k</sup></b> (bottom, k = 4) are operators, each wire one doubled-bond index.'],
    [0.18, 'Flip the top strip into its adjoint <b>(E<sup>j</sup>)<sup>*</sup> = (E<sup>*</sup>)<sup>j</sup></b>: every box is conjugate-transposed (shaded) and the order of the boxes is reversed.'],
    [0.36, 'Glue the ends: left end to left end, right end to right end. Both open indices are contracted and the closed network is the Hilbert–Schmidt overlap <b>⟨E<sup>j</sup>, E<sup>k</sup>⟩<sub>HS</sub> = Tr((E<sup>j</sup>)<sup>*</sup>E<sup>k</sup>)</b>.'],
    [0.56, 'If E is unitary, <b>E<sup>*</sup>E = 1</b>: at the seam each E<sup>*</sup> cancels one E, pair by pair, j times. A ring of k − j boxes is left: <b>Tr((E<sup>j</sup>)<sup>*</sup>E<sup>k</sup>) = Tr E<sup>k−j</sup> = t<sub>k−j</sub></b>.'],
    [0.78, 'Over all pairs of strips E<sup>0</sup>, …, E<sup>K−1</sup> (K = 5) the <b>Toeplitz matrix T<sub>jk</sub> = t<sub>k−j</sub></b> (t<sub>−l</sub> = t̄<sub>l</sub>) is the <b>Gram matrix of the strips</b>: c<sup>*</sup>Tc = ‖Σ<sub>j</sub> c<sub>j</sub>E<sup>j</sup>‖²<sub>HS</sub> = W(c). A Gram matrix is positive semidefinite (prop:ccm-tn-operator-gram).']]),
    draw(svg, t){
      const flip = T.seg(t, 0.2, 0.33), glue = T.seg(t, 0.38, 0.52), kill = T.seg(t, 0.58, 0.72), tight = T.seg(t, 0.72, 0.77), grid = T.seg(t, 0.8, 0.95);
      glued(svg, {flip, glue, kill, tight});
      T.label(svg, GG.xs[0]-GG.w/2-40, GG.yT+4, 'E^{j}', {op: T.live(t, 0, 0.2), anchor: 'end', size: 14});
      T.label(svg, GG.xs[0]-GG.w/2-40, GG.yT+4, '(E^{j})^{*}', {op: T.live(t, 0.2, 0.38), anchor: 'end', size: 14});
      T.label(svg, GG.xs[0]-GG.w/2-40, GG.yB+4, 'E^{k}', {op: T.live(t, 0, 0.38), anchor: 'end', size: 14});
      board(svg, 520, 110, ['open strips:', 'E^{j}: j = 2 boxes, two open ends', 'E^{k}: k = 4 boxes, two open ends'], T.live(t, 0, 0.2), 15);
      board(svg, 520, 110, ['adjoint strip:', '(E^{j})^{*} = E^{*}E^{*}  (order reversed)'], T.live(t, 0.2, 0.38), 15);
      board(svg, 520, 110, ['glued:', 'Tr((E^{j})^{*} E^{k}) = ⟨E^{j}, E^{k}⟩_{HS}'], T.live(t, 0.38, 0.57), 15);
      board(svg, 520, 110, ['unitary: E^{*}E = 1', 'Tr((E^{j})^{*} E^{k}) = Tr E^{k−j} = t_{k−j}', 'here: Tr E^{2} = t_{2}'], T.live(t, 0.57, 0.8), 15);
      if (grid > 0) { const K = 5, x0 = 540, y0 = 44, cw = 74, chh = 50;
        for (let jj = 0; jj < K; jj++) { const ro = T.seg(grid, jj*0.12, jj*0.12+0.5);
          T.label(svg, x0-8, y0+jj*chh+chh/2+4, 'E^{'+jj+'}', {op: ro, anchor: 'end', size: 12});
          for (let kk = 0; kk < K; kk++) { const cx = x0+kk*cw+cw/2, cy = y0+jj*chh+chh/2;
            E('rect', {x: x0+kk*cw+1, y: y0+jj*chh+1, width: cw-2, height: chh-2, rx: 4, fill: jj === kk ? 'var(--bond-soft)' : 'none', stroke: 'var(--line)', opacity: ro}, svg);
            T.path(svg, `M${cx-26},${cy-19} H${cx+26} V${cy+1} H${cx-26} Z`, 'bond', {op: ro*0.8});
            for (let i = 0; i < jj; i++) T.box(svg, cx-(jj-1)*5+i*10, cy-19, 7, 7, '', 'bar', {op: ro});
            for (let i = 0; i < kk; i++) T.box(svg, cx-(kk-1)*5+i*10, cy+1, 7, 7, '', '', {op: ro});
            T.label(svg, cx, cy+18, 't_{'+(kk-jj < 0 ? '−'+(jj-kk) : kk-jj)+'}', {op: ro, size: 11}); } }
        for (let kk = 0; kk < K; kk++) T.label(svg, x0+kk*cw+cw/2, y0-8, 'E^{'+kk+'}', {op: grid, size: 12});
        T.label(svg, x0+K*cw/2, 312, 'T_{jk} = Tr((E^{j})^{*}E^{k}) = t_{k−j}:  a Gram matrix, so T ⪰ 0', {op: T.seg(grid, 0.6, 1), size: 13}); }
    }});
};

WT.demos.movieMetric = function(root){
  WT.movie(root, {id: 'movieMetric', viewBox: '0 0 940 320', duration: 16, autoplay: false, frames: sceneCaps([
    [0, 'The same glued strips, but now E is <b>not unitary</b> (E<sup>*</sup>E ≠ 1). The naive gluing still computes Tr((E<sup>j</sup>)<sup>*</sup>E<sup>k</sup>), and nothing cancels: this is <b>not</b> t<sub>k−j</sub>.'],
    [0.2, 'Put the metric on the seams: <b>G &gt; 0</b> where (E<sup>j</sup>)<sup>*</sup> meets E<sup>k</sup>, G<sup>−1</sup> on the other glue. The network is now <b>Tr((E<sup>j</sup>)<sup>♯</sup>E<sup>k</sup>)</b> with the metric adjoint <b>(E<sup>j</sup>)<sup>♯</sup> = G<sup>−1</sup>(E<sup>j</sup>)<sup>*</sup>G</b>, the Hilbert–Schmidt product in the metric G.'],
    [0.42, 'Split each seam, G = G<sup>½</sup>G<sup>½</sup>, and slide the halves along the strips, inserting G<sup>−½</sup>G<sup>½</sup> = 1 between neighbours: every E becomes <b>Ẽ = G<sup>½</sup>EG<sup>−½</sup></b> (metric caps). The condition <b>E<sup>*</sup>GE = G is exactly Ẽ<sup>*</sup>Ẽ = 1</b>: the whitened strips are unitary and the cancellation of the previous movie applies, Tr((E<sup>j</sup>)<sup>♯</sup>E<sup>k</sup>) = t<sub>k−j</sub>.'],
    [0.66, 'Such a G exists <b>iff E on the retained space is diagonalisable with every eigenvalue of modulus r</b> (prop:hp-inner-product-discrete; E is already divided by r, so modulus 1 here). The metric is then a <b>Hilbert–Pólya inner product</b>. Positivity of the Weil form cannot see a Jordan block: r·(1 1; 0 1) has ν<sub>l</sub> = 2 for all l, a positive definite sequence, yet no G exists (prop:weil-blind-jordan).'],
    [0.86, 'For the Riemann zeta function <b>the strips are known</b> (the explicit formula gives every t) <b>and G is the unknown</b>.']]),
    draw(svg, t){
      const seam = T.seg(t, 0.22, 0.34), split = T.seg(t, 0.44, 0.64), kill = T.seg(t, 0.68, 0.78), tight = T.seg(t, 0.78, 0.84);
      const out = T.seg(t, 0.86, 0.92), q = T.seg(t, 0.88, 0.96);
      glued(svg, {flip: 1, glue: 1, seam, split, kill, tight, op: 1-out});
      board(svg, 510, 100, ['E^{*}E ≠ 1:', 'Tr((E^{j})^{*} E^{k}) ≠ t_{k−j}'], T.live(t, 0, 0.2), 15);
      board(svg, 510, 100, ['metric seams:', 'Tr((E^{j})^{♯} E^{k}),  (E^{j})^{♯} = G^{−1}(E^{j})^{*}G'], T.live(t, 0.2, 0.42), 15);
      board(svg, 510, 100, ['whitened: Ẽ = G^{½} E G^{−½}', 'E^{*}GE = G  ⇔  Ẽ^{*}Ẽ = 1', 'Tr((E^{j})^{♯}E^{k}) = Tr((Ẽ^{j})^{*}Ẽ^{k}) = t_{k−j}'], T.live(t, 0.42, 0.66), 15);
      board(svg, 510, 90, ['G exists  ⇔  E|_{retained} diagonalisable,', '   all eigenvalues of modulus r', 'G = a Hilbert–Pólya inner product', 'Jordan block r(1 1; 0 1): ν_{l} = 2 for all l,', '   positive definite, but no G'], T.live(t, 0.66, 0.86), 14);
      // scene 5: the unknown metric
      T.box(svg, 470, 150, 120, 84, '', 'metric', {op: q}); T.label(svg, 470, 162, 'G ?', {op: q, size: 34});
      T.chain(svg, {xs: [150, 205, 260], y: 150, w: 40, h: 30, label: 'E', ends: 20, op: 0.45*q});
      T.label(svg, 205, 205, 'strips: known', {op: q, size: 13}); T.label(svg, 205, 225, 't_{l} from the explicit formula', {op: q, cls: 'tn-dim', size: 12});
      T.label(svg, 470, 220, 'metric: unknown', {op: q, size: 13}); T.label(svg, 745, 150, 'E^{*}GE = G  ?', {op: q, size: 16});
    }});
};

// ================= movie 4: positivity, the disc and the circle =================
/* the mode set at time t: three fixed conjugate pairs on |mu| = 1, one movable pair at angle 1.3, and
   (from t = 0.6) its reflected partners J(mu) = 1/conj(mu) with weight ramping 0 -> 1. [re, im, weight, kind] */
T.circleModes = t => { const out = []; for (const a of [0.7, 1.9, 2.6]) out.push([Math.cos(a), Math.sin(a), 1, 'fixed'], [Math.cos(a), -Math.sin(a), 1, 'fixed']);
  const R = t <= 0.3 ? T.lerp(1, 0.55, T.seg(t, 0.02, 0.28)) : t <= 0.6 ? T.lerp(0.55, 1.35, T.seg(t, 0.32, 0.58)) : T.lerp(1.35, 1, T.seg(t, 0.86, 0.98));
  const pw = t > 0.6 ? T.seg(t, 0.6, 0.68) : 0, a = 1.3;
  out.push([R*Math.cos(a), R*Math.sin(a), 1, 'move'], [R*Math.cos(a), -R*Math.sin(a), 1, 'move']);
  if (pw > 0) out.push([Math.cos(a)/R, Math.sin(a)/R, pw, 'partner'], [Math.cos(a)/R, -Math.sin(a)/R, pw, 'partner']);
  return {modes: out, R, pw}; };
/* t_l = sum_mu w mu^l (real: the set is conjugation-closed) for l < K, and the minimal eigenvalue of each window 1..K */
T.circleData = (t, K = 14) => { const st = T.circleModes(t), tl = [];
  for (let l = 0; l < K; l++) { let s = 0; for (const [x, y, w] of st.modes) s += w*Math.pow(Math.hypot(x, y), l)*Math.cos(l*Math.atan2(y, x)); tl.push(s); }
  return Object.assign(st, {tl, mins: WT.toeplitzMins(tl, K)}); };

WT.demos.movieCircle = function(root){
  WT.movie(root, {id: 'movieCircle', viewBox: '0 0 940 320', duration: 16, autoplay: false, frames: sceneCaps([
    [0, 'Left: the retained modes μ (r = 1), three conjugate pairs on the circle and one movable pair. Right: t<sub>l</sub> = Σ<sub>μ</sub> μ<sup>l</sup> (real, since the set is closed under conjugation) and the smallest eigenvalue of the window T<sub>jk</sub> = t<sub>k−j</sub>, K = 1…14. <b>A mode inside the disc passes: positivity alone is the one-sided bound |μ| ≤ r</b> (thm:weil-positivity-finite).'],
    [0.3, '<b>A mode outside the disc makes the sequence unbounded and the form indefinite</b>: at |μ| = 1.35 the smallest eigenvalue is negative from K = 8 on.'],
    [0.6, 'Add the reflected partners <b>J(μ) = r²/μ̄</b> (hollow, radius 1/1.35). If the retained set is J-invariant, <b>W(c) = Σ<sub>μ</sub> p<sub>c</sub>(μ/r) · conj p<sub>c</sub>(Jμ/r)</b>, the mode pairing, and <b>positivity forces every mode onto the circle</b> (thm:weil-duality-pairing): the off-circle orbit {μ, Jμ} still makes W negative.'],
    [0.85, 'Only when every partner is the mode itself, |μ| = r, is the form positive again: the pair and its partners merge on the circle (a double mode) and λ<sub>min</sub> ≥ 0 for every K.']]),
    draw(svg, t, C){
      const d = T.circleData(t), K = d.mins.length, P = WT.svg.plane(svg, 215, 168, 82, 1, C);
      T.label(svg, 215+82*0.72+8, 168-82*0.72-8, '|μ| = r', {cls: 'tn-dim', anchor: 'start', size: 11});
      T.label(svg, 20, 24, '● modes μ    ○ partners J(μ) = r^{2}/conj(μ)', {anchor: 'start', size: 12});
      const mv = d.modes.filter(m => m[3] === 'move'), pt = d.modes.filter(m => m[3] === 'partner');
      pt.forEach((m, i) => E('line', {x1: f1(P.X(m[0])), y1: f1(P.Y(m[1])), x2: f1(P.X(mv[i][0])), y2: f1(P.Y(mv[i][1])), stroke: 'var(--ink2)', 'stroke-dasharray': '3 3', opacity: m[2]}, svg));
      for (const m of d.modes) { const big = m[3] !== 'fixed';
        if (m[3] === 'partner') E('circle', {cx: f1(P.X(m[0])), cy: f1(P.Y(m[1])), r: 7, fill: 'none', stroke: 'var(--spec)', 'stroke-width': 1.8, opacity: m[2]}, svg);
        else E('circle', {cx: f1(P.X(m[0])), cy: f1(P.Y(m[1])), r: big ? 5.5 : 4, fill: 'var(--spec)', stroke: big ? 'var(--ink)' : 'none', 'stroke-width': 1}, svg); }
      T.label(svg, P.X(mv[0][0])+10, P.Y(mv[0][1])-6, 'μ', {anchor: 'start', size: 13});
      if (pt.length) T.label(svg, P.X(pt[0][0])-9, P.Y(pt[0][1])+4, 'Jμ', {anchor: 'end', size: 12, op: pt[0][2]*(1-T.seg(t, 0.86, 0.95))});
      // right: minimal eigenvalue of T_K on a signed log scale
      const x0 = 520, x1 = 915, yT = 40, yBt = 262, gmin = -2.15, gmax = 1.15, gs = v => Math.sign(v)*Math.log10(1+Math.abs(v));
      const Y = v => yBt - (gs(v)-gmin)/(gmax-gmin)*(yBt-yT), X = k => x0+22+(k-1)*(x1-x0-34)/(K-1);
      T.label(svg, x0, 22, 'λ_{min}(T_{K}),  T_{jk} = t_{k−j}   (signed log scale)', {anchor: 'start', size: 12});
      for (const v of [10, 1, -1, -10, -100]) { E('line', {x1: x0, y1: f1(Y(v)), x2: x1, y2: f1(Y(v)), class: 'grid'}, svg); T.label(svg, x0-4, Y(v)+3, String(v).replace('-', '−'), {cls: 'tn-dim', anchor: 'end'}); }
      E('line', {x1: x0, y1: f1(Y(0)), x2: x1, y2: f1(Y(0)), stroke: 'var(--ink2)', 'stroke-width': 1}, svg); T.label(svg, x0-4, Y(0)+3, '0', {cls: 'tn-dim', anchor: 'end'});
      const tol = 1e-9*Math.max(1, d.tl[0]), ok = v => v >= -tol;
      for (let k = 1; k < K; k++) E('line', {x1: f1(X(k)), y1: f1(Y(d.mins[k-1])), x2: f1(X(k+1)), y2: f1(Y(d.mins[k])), stroke: ok(d.mins[k-1]) && ok(d.mins[k]) ? 'var(--orbit)' : 'var(--spec)', 'stroke-width': 2}, svg);
      d.mins.forEach((v, i) => { E('circle', {cx: f1(X(i+1)), cy: f1(Y(v)), r: 3.2, fill: ok(v) ? 'var(--orbit)' : 'var(--spec)'}, svg); T.label(svg, X(i+1), yBt+16, String(i+1), {cls: 'tn-dim'}); });
      T.label(svg, x1, yBt+29, 'window size K', {cls: 'tn-dim', anchor: 'end'});
      const neg = d.mins.findIndex(v => !ok(v));
      T.label(svg, x0, 311, '|μ| = '+d.R.toFixed(3)+'    λ_{min}(T_{14}) = '+WT.fmtF(Math.abs(d.mins[K-1]) < tol ? 0 : d.mins[K-1], 4).replace('-', '−')+(neg >= 0 ? '   negative from K = '+(neg+1) : '   ≥ 0 for all K ≤ 14'), {anchor: 'start', size: 12});
    }});
};
})();
