/* demos-kraus.js -- worker K: the quantum Ihara-Bass station and the Kraus dichotomy (WT.demos.kraus, #demo-kraus).
 * Setting (notes/quantum-ihara-general.md, report/sections/08b_weil_positivity.tex): n = 2, D = 4 Kraus operators
 * B_1..B_4 with the reversal 1<->3, 2<->4 (0-based INV = [2,3,0,1], as in scripts/weil_positivity.py), E_i = Ad(B_i)
 * = conj(B_i) (x) B_i (column stacking), edge space W = C^4 (x) M_2 (dim 16), T(v (x) |i>) = sum_{j != ibar} E_i v (x) |j>.
 * Side A: the ring sums Tr T^l = sum_w |Tr B_w|^2 (cor:qihara-kraus). Every Weil form is built from these traces;
 * eigenvalues (of Sigma = sum_i E_i, Phi = Sigma/4, and T) appear only in panels marked "comparison".
 * Conventions fixed in lanes/kraus.md. The numerics are exported as WT.demos.kraus.model for the node/Python check. */
(function(){
'use strict';
const WT = window.WT, cm = WT.cmat, C = WT.C;
const D = 4, Q = 3, RQ = Math.sqrt(3), INV = [2, 3, 0, 1], KMAX = 14, LT = 16, HB = 2 * Math.sqrt(3) / 4, TOL = 1e-9;
const V = { orbit:'var(--orbit)', spec:'var(--spec)', pole:'var(--pole)', bond:'var(--bond)', ink:'var(--ink)', ink2:'var(--ink2)',
  line:'var(--line)', bg2:'var(--bg2)', orbitSoft:'var(--orbit-soft)', bondSoft:'var(--bond-soft)', metric:'var(--metric)' };

// ---------- seeded randomness: mulberry32, Box-Muller, complex Gaussian 2x2, Haar U(2) by Gram-Schmidt ----------
const mulberry32 = a => () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
const gauss = rnd => { const u = 1 - rnd(), v = rnd(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); };
const M2 = (re, im) => ({ re, im });
const cgauss = rnd => { const g = () => gauss(rnd) / Math.SQRT2; const re = [[g(), g()], [g(), g()]]; const im = [[g(), g()], [g(), g()]]; return M2(re, im); };
const haar = rnd => { const Z = cgauss(rnd); const col = j => [[Z.re[0][j], Z.im[0][j]], [Z.re[1][j], Z.im[1][j]]];
  const unit = v => { const s = Math.hypot(v[0][0], v[0][1], v[1][0], v[1][1]); return v.map(z => [z[0] / s, z[1] / s]); };
  const a = unit(col(0)); let b = col(1); const p = C.add(C.mul(C.conj(a[0]), b[0]), C.mul(C.conj(a[1]), b[1]));
  b = unit(b.map((z, k) => C.sub(z, C.mul(p, a[k]))));
  return M2([[a[0][0], b[0][0]], [a[1][0], b[1][0]]], [[a[0][1], b[0][1]], [a[1][1], b[1][1]]]); };
const rs = (B, s) => cm.scale(B, [s, 0]);
const h = Math.SQRT1_2;
const PRESETS = { // unitary presets; the family is [U1, U2, U1^dagger, U2^dagger]
  sqrt: [M2([[h, 0], [0, h]], [[0, -h], [-h, 0]]), M2([[h, 0], [0, h]], [[-h, 0], [0, h]])],   // (1 - iX)/sqrt2, (1 - iZ)/sqrt2
  pauli: [M2([[0, 1], [1, 0]], [[0, 0], [0, 0]]), M2([[1, 0], [0, -1]], [[0, 0], [0, 0]])] };  // X, Z (self-inverse: B_3 = B_1)

/* the family for a state {regime, seed, eps, preset}; raw (before the adjoint-only rescaling) */
function family(st){
  const rnd = mulberry32(st.seed);
  if (st.regime === 'unitary'){
    let U = st.preset ? PRESETS[st.preset] : [haar(rnd), haar(rnd)]; const R = [cgauss(rnd), cgauss(rnd)];
    if (st.eps > 0) U = U.map((u, k) => cm.add(u, rs(R[k], st.eps)));
    return [U[0], U[1], cm.dagger(U[0]), cm.dagger(U[1])]; }
  if (st.regime === 'inverse'){ const B = [cgauss(rnd), cgauss(rnd)].map(b => rs(b, Math.SQRT2)); return [B[0], B[1], cm.inv(B[0]), cm.inv(B[1])]; }  // NOT |det| = 1: see lanes/kraus.md
  if (st.regime === 'adjoint'){ const B = [cgauss(rnd), cgauss(rnd)]; return [B[0], B[1], cm.dagger(B[0]), cm.dagger(B[1])]; }
  const d12 = M2([[1, 0], [0, 2]], [[0, 0], [0, 0]]); return [d12, cm.eye(2), d12, cm.eye(2)];   // prop:kraus-no-duality-example
}

// ---------- the operators ----------
const buildT = Es => { const T = cm.zeros(16); for (let i = 0; i < D; i++) for (let j = 0; j < D; j++) if (j !== INV[i])
  for (let a = 0; a < 4; a++) for (let b = 0; b < 4; b++){ T.re[4 * j + a][4 * i + b] = Es[i].re[a][b]; T.im[4 * j + a][4 * i + b] = Es[i].im[a][b]; } return T; };
/* Perron root of T: T preserves blockwise positivity, so its spectral radius is an eigenvalue (the Perron root) */
const perron = T => Math.max(...eigQR(T).map(C.abs));
/* spectrum of T from its power sums: Newton's identities -> characteristic polynomial -> WT.polyRoots */
function newtonRoots(tr){ const n = tr.length - 1, e = [[1, 0]];
  for (let k = 1; k <= n; k++){ let s = [0, 0]; for (let i = 1; i <= k; i++){ const t = C.mul(e[k - i], tr[i]); s = i % 2 ? C.add(s, t) : C.sub(s, t); } e.push([s[0] / k, s[1] / k]); }
  const c = []; for (let k = 0; k <= n; k++){ const sg = k % 2 ? -1 : 1; c[n - k] = [sg * e[k][0], sg * e[k][1]]; } return WT.polyRoots(c); }
/* all eigenvalues of a complex matrix: Householder reduction to Hessenberg form, then shifted QR (Givens, Wilkinson shift) */
function eigQR(M){ const n = M.re.length, A = M.re.map((r, i) => r.map((v, j) => [v, M.im[i][j]])), ev = [];
  for (let k = 0; k < n - 2; k++){ const v = []; for (let i = k + 1; i < n; i++) v.push(A[i][k].slice()); const al = Math.hypot(...v.flat()); if (al < 1e-300) continue;
    const a0 = C.abs(v[0]), ph = a0 > 0 ? [v[0][0] / a0, v[0][1] / a0] : [1, 0]; v[0] = C.add(v[0], [ph[0] * al, ph[1] * al]); const vn = v.reduce((s, z) => s + z[0] * z[0] + z[1] * z[1], 0);
    for (let j = 0; j < n; j++){ let s = [0, 0]; v.forEach((z, i) => { s = C.add(s, C.mul(C.conj(z), A[k + 1 + i][j])); }); s = [2 * s[0] / vn, 2 * s[1] / vn]; v.forEach((z, i) => { A[k + 1 + i][j] = C.sub(A[k + 1 + i][j], C.mul(z, s)); }); }
    for (let i = 0; i < n; i++){ let s = [0, 0]; v.forEach((z, j) => { s = C.add(s, C.mul(A[i][k + 1 + j], z)); }); s = [2 * s[0] / vn, 2 * s[1] / vn]; v.forEach((z, j) => { A[i][k + 1 + j] = C.sub(A[i][k + 1 + j], C.mul(s, C.conj(z))); }); } }
  let hi = n - 1, it = 0;
  while (hi >= 0){ let l = hi; while (l > 0 && C.abs(A[l][l - 1]) > 1e-15 * (C.abs(A[l - 1][l - 1]) + C.abs(A[l][l]) || 1)) l--;
    if (l === hi || it > 400){ ev.push(A[hi][hi]); hi--; it = 0; continue; }
    const a = A[hi - 1][hi - 1], b = A[hi - 1][hi], c = A[hi][hi - 1], d = A[hi][hi], tr = C.add(a, d), dt = C.sub(C.mul(a, d), C.mul(b, c));
    const sq = C.sqrt(C.sub(C.mul(tr, tr), [4 * dt[0], 4 * dt[1]])), l1 = [(tr[0] + sq[0]) / 2, (tr[1] + sq[1]) / 2], l2 = [(tr[0] - sq[0]) / 2, (tr[1] - sq[1]) / 2];
    let mu = C.abs(C.sub(l1, d)) < C.abs(C.sub(l2, d)) ? l1 : l2; if (++it % 11 === 10) mu = C.add(d, [C.abs(c), 0]);
    for (let i = l; i <= hi; i++) A[i][i] = C.sub(A[i][i], mu);
    const G = [];
    for (let k = l; k < hi; k++){ const x = A[k][k], y = A[k + 1][k], r = Math.hypot(C.abs(x), C.abs(y)); if (!r){ G.push(null); continue; }
      const cc = [x[0] / r, x[1] / r], ss = [y[0] / r, y[1] / r]; G.push([cc, ss]);
      for (let j = k; j <= hi; j++){ const p = A[k][j], q = A[k + 1][j]; A[k][j] = C.add(C.mul(C.conj(cc), p), C.mul(C.conj(ss), q)); A[k + 1][j] = C.sub(C.mul(cc, q), C.mul(ss, p)); } }
    for (let k = l; k < hi; k++){ const g = G[k - l]; if (!g) continue; const [cc, ss] = g;
      for (let i = l; i <= Math.min(k + 2, hi); i++){ const p = A[i][k], q = A[i][k + 1]; A[i][k] = C.add(C.mul(p, cc), C.mul(q, ss)); A[i][k + 1] = C.sub(C.mul(q, C.conj(cc)), C.mul(p, C.conj(ss))); } }
    for (let i = l; i <= hi; i++) A[i][i] = C.add(A[i][i], mu); }
  return ev; }
const quadRoots = a => { const d = C.sqrt(C.sub(C.mul(a, a), [4 * Q, 0])); return [[(a[0] + d[0]) / 2, (a[1] + d[1]) / 2], [(a[0] - d[0]) / 2, (a[1] - d[1]) / 2]]; };
/* remove, for each s in S, the nearest not-yet-removed element (scripts/weil_positivity.py remove_nearest) */
function removeNearest(ev, S){ const left = ev.map((z, k) => ({ z, k })), gone = new Set();
  for (const s of S){ let bi = -1, bd = Infinity; left.forEach((o, i) => { const d = C.abs(C.sub(o.z, s)); if (d < bd){ bd = d; bi = i; } }); if (bi >= 0){ gone.add(left[bi].k); left.splice(bi, 1); } }
  return { kept: left.map(o => o.z), trivialIdx: gone }; }
const hausdorff = (A, B) => { const one = (P, R) => Math.max(0, ...P.map(a => Math.min(...R.map(b => C.abs(C.sub(a, b)))))); return Math.max(one(A, B), one(B, A)); };
/* cyclically non-backtracking words of length l and sum_w |Tr B_{w_l} ... B_{w_1}|^2 */
function wordSum(Bs, l){ let tot = 0, cnt = 0; const w = new Array(l).fill(0);
  for (let code = 0; code < Math.pow(D, l); code++){ let c = code; for (let k = 0; k < l; k++){ w[k] = c % D; c = Math.floor(c / D); }
    let ok = true; for (let k = 0; k < l; k++) if (w[(k + 1) % l] === INV[w[k]]) { ok = false; break; } if (!ok) continue;
    let P = cm.eye(2); for (const i of w) P = cm.mul(Bs[i], P); const t = cm.trace(P); tot += t[0] * t[0] + t[1] * t[1]; cnt++; }
  return { sum: tot, count: cnt }; }
const weilMins = (nu, K) => { const out = []; for (let k = 1; k <= K; k++) out.push(WT.jacobiEig(WT.toeplitz(nu, k)).values[0]); return out; };
const nuSeq = (tr, S, r, L) => Array.from({ length: L }, (_, l) => (tr[l][0] - S.reduce((s, z) => s + C.pow(z, l)[0], 0)) / Math.pow(r, l));
const hastingsOf = sig => { const phi = sig.map(a => [a[0] / D, a[1] / D]); const nt = phi.filter(z => C.abs(C.sub(z, [1, 0])) >= 1e-8 && C.abs(C.add(z, [1, 0])) >= 1e-8);
  const mx = Math.max(0, ...nt.map(C.abs)); return { phi, max: mx, holds: mx <= HB * (1 + 1e-9) }; };
const sigSpec = (Sig, herm) => herm ? WT.hermEigvals(Sig.re, Sig.im).map(x => [x, 0]) : cm.eigvals(Sig).sort((a, b) => b[0] - a[0]);

/* everything the panels and the readout show, for a state {regime, seed, eps, preset} */
function model(st){
  const raw = family(st); let Bs = raw;
  const errs = B => ({ inv: Math.max(...B.map((b, i) => cm.frob(cm.add(cm.mul(B[INV[i]], b), rs(cm.eye(2), -1))))),
                       adj: Math.max(...B.map((b, i) => cm.frob(cm.add(B[INV[i]], rs(cm.dagger(b), -1))))) });
  const pe = errs(raw), invP = pe.inv < 1e-9, adjP = pe.adj < 1e-9;
  const kind = st.regime === 'nodual' ? 'nodual' : invP && adjP ? 'unitary' : invP ? 'inverse' : adjP ? 'adjoint' : 'none';
  let scale = 1, mu0raw = null;
  if (kind === 'adjoint'){ mu0raw = perron(buildT(raw.map(cm.ad))); scale = Math.sqrt(Q / mu0raw); Bs = raw.map(b => rs(b, scale)); }
  const Es = Bs.map(cm.ad), T = buildT(Es), Sig = Es.reduce(cm.add);
  const sig = sigSpec(Sig, adjP), hast = hastingsOf(sig);
  const tr = cm.powerTraces(T, LT), specQ = eigQR(T), specN = newtonRoots(tr);
  const pm1 = [...Array(4).fill([1, 0]), ...Array(4).fill([-1, 0])];
  let ref = null, S = [], r = RQ, Sname = '';
  if (invP) ref = pm1.concat(...sig.map(quadRoots));                                    // thm:kraus-inverse-pairing-duality
  if (kind === 'unitary'){ S = pm1.slice(); Sname = '{+1×4, −1×4}';                      // thm:kraus-weil-criterion (ii)
    hast.phi.forEach(z => { if (C.abs(C.sub(z, [1, 0])) < 1e-8){ S.push([Q, 0], [1, 0]); Sname += ' ∪ {3, 1}'; } else if (C.abs(C.add(z, [1, 0])) < 1e-8){ S.push([-Q, 0], [-1, 0]); Sname += ' ∪ {−3, −1}'; } }); }
  else if (kind === 'inverse'){ const a0 = sig.reduce((m, a) => C.abs(a) > C.abs(m) ? a : m); S = pm1.concat(quadRoots(a0));
    Sname = '{+1×4, −1×4} ∪ Perron pair {' + WT.fmtF(S[8][0], 4) + ', ' + WT.fmtF(S[9][0], 4) + '} (α₀ = ' + WT.fmtF(a0[0], 4) + ')'; }
  else if (kind === 'adjoint' || kind === 'none'){ S = [[Q, 0]]; Sname = '{3} (the Perron root of T, rescaled to q)'; }
  else { ref = []; [1, 2, 2, 4].forEach(a => { const d = Math.sqrt((a + 1) * (a + 1) + 12 * a); ref.push([a, 0], [1, 0], [(a + 1 + d) / 2, 0], [(a + 1 - d) / 2, 0]); });
    S = [1, 1, 1, 1, 1, 2, 2, 4, 3, -1].map(x => [x, 0]); r = (5 + Math.sqrt(73)) / 2; Sname = '{1×5, 2×2, 4, 3, −1} (prop:kraus-no-duality-example)'; }
  const base = ref || specQ, ret = removeNearest(base, S).kept, trivQ = removeNearest(specQ, S).trivialIdx;
  const J = z => { const m = z[0] * z[0] + z[1] * z[1]; return [r * r * z[0] / m, r * r * z[1] / m]; };
  const Jinv = ret.every(z => ret.some(w => C.abs(C.sub(w, J(z))) < 1e-6));
  const circle = Math.max(0, ...ret.map(z => Math.abs(C.abs(z) - r))), maxRet = Math.max(0, ...ret.map(C.abs));
  const nu = nuSeq(tr, S, r, KMAX), mins = weilMins(nu, KMAX), nuScale = Math.max(1, ...nu.map(Math.abs));
  const words = [1, 2, 3, 4].map(l => { const w = wordSum(Bs, l); return { l, sum: w.sum, count: w.count, tr: tr[l][0], rel: Math.abs(w.sum - tr[l][0]) / Math.max(1, Math.abs(tr[l][0])) }; });
  const trMinRel = Math.min(...tr.slice(1).map(z => z[0] / Math.max(1, C.abs(z)))), trImRel = Math.max(...tr.slice(1).map(z => Math.abs(z[1]) / Math.max(1, C.abs(z))));
  const disc = { qr: ref ? hausdorff(specQ, ref) : null, newton: hausdorff(specN, ref || specQ) };
  const mins3 = kind === 'nodual' ? weilMins(nuSeq(tr, S, RQ, KMAX), KMAX) : null;
  return { st, kind, raw, Bs, pe, invP, adjP, scale, mu0raw, sig, hast, tr, specQ, specN, ref, S, Sname, r, ret, trivQ, Jinv, circle, maxRet,
           nu, mins, nuScale, words, trMinRel, trImRel, disc, mins3, sigReal: Math.max(...sig.map(a => Math.abs(a[1]))) < 1e-9 };
}
/* the default family: the first seed in 1..50 whose Haar pair meets Hastings' bound (else the sqrt(X), sqrt(Z) preset) */
function defaultState(){ for (let s = 1; s <= 50; s++){ const st = { regime: 'unitary', seed: s, eps: 0, preset: null };
    const B = family(st), Sig = B.map(cm.ad).reduce(cm.add); if (hastingsOf(sigSpec(Sig, true)).holds) return st; }
  return { regime: 'unitary', seed: 1, eps: 0, preset: 'sqrt' }; }
/* entering the inverse-paired regime: the first seed >= from whose Sigma-spectrum is non-real (about half are) */
function inverseSeed(from){ for (let s = from; s < from + 50; s++){ const Sig = family({ regime: 'inverse', seed: s }).map(cm.ad).reduce(cm.add);
    if (Math.max(...sigSpec(Sig, false).map(a => Math.abs(a[1]))) > 1e-6) return s; } return from; }

// ---------- drawing ----------
const SV = WT.svg.el, TX = WT.svg.text;
const sl = x => Math.sign(x) * Math.log10(1 + Math.abs(x));
const dot = (svg, x, y, r, fill, stroke, tip) => { const c = SV('circle', { cx: x, cy: y, r, fill: fill || 'none', stroke: stroke || 'none', 'stroke-width': 1.4 }, svg); if (tip) SV('title', {}, c).textContent = tip; return c; };
function plane(svg, ext, title, sub){ const cx = 220, cy = 166, sc = 116 / ext, X = x => cx + x * sc, Y = y => cy - y * sc;
  SV('line', { x1: X(-1.08 * ext), y1: cy, x2: X(1.08 * ext), y2: cy, class: 'axis' }, svg); SV('line', { x1: cx, y1: Y(1.08 * ext), x2: cx, y2: Y(-1.08 * ext), class: 'axis' }, svg);
  TX(svg, 8, 16, title, { fill: V.ink, 'font-size': '12' }); if (sub) TX(svg, 8, 30, sub, { 'font-size': '9.5' });
  TX(svg, 432, 16, 'comparison', { 'text-anchor': 'end', 'font-size': '10', 'font-style': 'italic' });
  TX(svg, X(ext), cy + 13, WT.fmtF(ext, 1), { 'text-anchor': 'middle', 'font-size': '9' }); TX(svg, X(-ext), cy + 13, WT.fmtF(-ext, 1), { 'text-anchor': 'middle', 'font-size': '9' });
  return { X, Y, sc, cx, cy }; }
/* points beyond the plotted range are pinned to its edge (value in the label), so a Perron outlier does not shrink the circle */
const pin = (svg, P, ext, z, draw) => { const a = C.abs(z); if (a <= 1.05 * ext) return draw(z); const w = [z[0] * ext / a, z[1] * ext / a]; draw(w);
  TX(svg, P.X(w[0]), P.Y(w[1]) - 9, '→ ' + WT.fmtC(z[0], z[1], 2), { 'text-anchor': 'end', 'font-size': '9' }); };
function drawSigma(svg, M){ WT.svg.clear(svg); const b = 2 * Math.sqrt(Q), a0 = M.kind === 'inverse' ? M.sig.reduce((m, a) => C.abs(a) > C.abs(m) ? a : m) : null,
    ext = Math.max(5, 1.12 * Math.max(0, ...M.sig.filter(a => a !== a0).map(C.abs)));
  const P = plane(svg, ext, '(a) spec Σ, Σ = Σᵢ Ad(Bᵢ)  (4 values)', 'band |α| ≤ 2√3; pole colour: trivial (Φ = ±1, Perron α₀)');
  SV('rect', { x: P.X(-b), y: P.cy - 5, width: P.X(b) - P.X(-b), height: 10, rx: 3, fill: V.bondSoft, stroke: V.bond, 'stroke-width': 0.8 }, svg);
  TX(svg, P.X(b), P.cy - 9, '2√3', { 'text-anchor': 'middle', 'font-size': '9', fill: V.bond }); TX(svg, P.X(-b), P.cy - 9, '−2√3', { 'text-anchor': 'middle', 'font-size': '9', fill: V.bond });
  dot(svg, P.X(D), P.cy, 8, 'none', V.pole, 'D = 4'); TX(svg, P.X(D), P.cy + 24, 'D', { 'text-anchor': 'middle', 'font-size': '9', fill: V.pole });
  M.sig.forEach(a => { const triv = (M.kind === 'unitary' && (Math.abs(a[0] - D) < 1e-8 * D || Math.abs(a[0] + D) < 1e-8 * D)) || (a0 && a === a0);
    pin(svg, P, ext, a, w => dot(svg, P.X(w[0]), P.Y(w[1]), 4.5, triv ? V.pole : V.spec, V.bg2, 'α = ' + WT.fmtC(a[0], a[1], 4))); }); }
function drawT(svg, M){ WT.svg.clear(svg); const big = M.kind === 'inverse' ? Math.max(...M.S.map(C.abs)) : Infinity,
    ext = Math.max(1.3 * M.r, 1.1 * Math.max(...M.specQ.map(C.abs).filter(a => a < 0.999 * big)));
  const P = plane(svg, ext, '(b) spec T, 16 modes' + (M.kind === 'nodual' ? '' : '; circle |μ| = √3'), 'filled: eigenvalues of T (QR)' + (M.ref ? '; hollow: ' + (M.kind === 'nodual' ? 'closed form (prop)' : 'Ihara–Bass') : ''));
  SV('circle', { cx: P.cx, cy: P.cy, r: M.r * P.sc, fill: 'none', stroke: V.metric, 'stroke-dasharray': '4 3', 'stroke-width': 1.2 }, svg);
  TX(svg, P.X(M.r * 0.72), P.Y(M.r * 0.72) - 4, 'r = ' + WT.fmtF(M.r, 4), { 'font-size': '9', fill: V.metric });
  if (M.ref) M.ref.forEach(z => pin(svg, P, ext, z, w => dot(svg, P.X(w[0]), P.Y(w[1]), 6.5, 'none', V.ink2)));
  M.specQ.forEach((z, k) => { const a = C.abs(z), w = a > 1.05 * ext ? [z[0] * ext / a, z[1] * ext / a] : z; dot(svg, P.X(w[0]), P.Y(w[1]), 3.2, M.trivQ.has(k) ? V.pole : V.spec, 'none', 'μ = ' + WT.fmtC(z[0], z[1], 4) + '  |μ| = ' + WT.fmtF(a, 4)); }); }
function drawCount(svg, M){ WT.svg.clear(svg); TX(svg, 8, 16, '(c) side A: ring sums and the retained sequence', { fill: V.ink, 'font-size': '12' });
  const L = 12, lg = M.tr.slice(1, L + 1).map(z => Math.log10(1 + Math.max(0, z[0]))), hs = 86 / Math.max(1, ...lg), x0 = 44, w = 31, y0 = 128;
  TX(svg, 8, 32, 'log₁₀(1 + Tr Tˡ) ≥ 0, l = 1..12; hollow: Σ_w |Tr B_w|², l ≤ 4', { 'font-size': '9.5' });
  SV('line', { x1: x0 - 4, y1: y0, x2: x0 + L * w, y2: y0, class: 'axis' }, svg);
  WT.svg.bars(svg, lg, x0, y0, w, hs, null, { color: V.orbit, labels: lg.map((_, i) => i + 1) });
  M.words.forEach(o => dot(svg, x0 + (o.l - 1) * w + (w - 2) / 2, y0 - Math.log10(1 + o.sum) * hs, 4, 'none', V.ink2, 'Σ_w |Tr B_w|² = ' + WT.fmt(o.sum, 8) + ' over ' + o.count + ' words'));
  const ys = 238, sn = M.nu.map(sl), hn = 46 / Math.max(0.3, ...sn.map(Math.abs)), w2 = 27;
  TX(svg, 8, 164, 'νₗ = r⁻ˡ(Tr Tˡ − Σ_S μˡ), l = 0..13 (signed log scale)', { 'font-size': '9.5' });
  SV('line', { x1: x0 - 4, y1: ys, x2: x0 + KMAX * w2, y2: ys, class: 'axis' }, svg);
  WT.svg.bars(svg, sn, x0, ys, w2, hn, { orbit: V.orbit, spec: V.spec });
  M.nu.forEach((v, l) => TX(svg, x0 + l * w2 + w2 / 2 - 1, 296, String(l), { 'text-anchor': 'middle', 'font-size': '9' })); }
function drawWeil(svg, M, K){ WT.svg.clear(svg); TX(svg, 8, 16, '(d) Weil matrix (ν_{k−j}) and its λ_min', { fill: V.ink, 'font-size': '12' });
  const cell = Math.min(22, 196 / K), Wm = WT.toeplitz(M.nu, K);
  WT.svg.heat(svg, Wm, 12, 44, cell, { orbit: V.orbit, spec: V.spec, ink: V.ink }, { title: 'K = ' + K + ' (teal ≥ 0, red < 0)' });
  const x0 = 236, w = 14, y0 = 150, v = M.mins.map(x => Math.abs(x) < TOL * M.nuScale ? 0 : x), s = v.map(sl), hs = 100 / Math.max(0.3, ...s.map(Math.abs));
  TX(svg, x0 - 4, 36, 'λ_min(K), K = 1..14 (signed log)', { 'font-size': '9.5' });
  SV('line', { x1: x0 - 3, y1: y0, x2: x0 + KMAX * w, y2: y0, class: 'axis' }, svg);
  s.forEach((val, i) => { const hh = Math.max(1.5, Math.abs(val) * hs); SV('rect', { x: x0 + i * w, y: val >= 0 ? y0 - hh : y0, width: w - 3, height: hh, fill: v[i] < 0 ? V.spec : V.orbit, opacity: 0.9 }, svg);
    if (i + 1 === K) SV('rect', { x: x0 + i * w - 1.5, y: y0 - 104, width: w, height: 208, fill: 'none', stroke: V.ink, 'stroke-width': 1, 'stroke-dasharray': '2 2' }, svg);
    if (i % 2 === 1 || i === 0) TX(svg, x0 + i * w + (w - 3) / 2, y0 + 118, String(i + 1), { 'text-anchor': 'middle', 'font-size': '9' }); });
  TX(svg, x0 + KMAX * w / 2, 290, 'λ_min(' + K + ') = ' + fmtW(M.mins[K - 1], M.nuScale), { 'text-anchor': 'middle', 'font-size': '10', fill: M.mins[K - 1] < -TOL * M.nuScale ? V.spec : V.orbit }); }

// ---------- readout ----------
const fmtW = (x, sc) => Math.abs(x) < TOL * sc ? '0' : WT.fmt(x, 5);   // lambda_min: 5 significant digits (cancellation in nu_l)
const e1 = x => x === 0 ? '0' : x.toExponential(0).replace('e+', 'e');
function verdict(M, K){ const neg = M.mins.findIndex(x => x < -TOL * M.nuScale), pos = neg < 0;
  const at = pos ? 'λ_min ≥ 0 for K = 1..14' : 'λ_min < 0 from K = ' + (neg + 1);
  if (M.kind === 'unitary') return 'positive iff Hastings\' bound (thm:kraus-weil-criterion (ii)). Bound ' + (M.hast.holds ? 'holds' : 'fails') + '; Weil form: ' + at +
    (M.hast.holds === pos ? '.  Consistent.' : '.  (Finite window: a mode just off the circle only shows at larger K.)');
  if (M.kind === 'inverse') return 'duality holds, Σ-spectrum ' + (M.sigReal ? 'real' : 'non-real') + ': retained modes ' + (M.circle < 1e-6 ? 'on' : 'off') + ' the circle, form ' + (pos ? 'positive' : 'indefinite') + ' (' + at + ').';
  if (M.kind === 'nodual') return 'no duality (prop:kraus-no-duality-example): positivity is the one-sided bound |μ| ≤ r only (thm:kraus-weil-criterion (i)); at r = p₄ one mode sits on the circle, the rest inside: ' + at +
    '.  At r = √3 instead: λ_min(' + K + ') = ' + fmtW(M.mins3[K - 1], M.nuScale) + '.';
  return 'no duality: positivity is the one-sided bound |μ| ≤ √3 only (thm:kraus-weil-criterion (i)); modes inside the disc pass.  Here max |μ| off S = ' + WT.fmtF(M.maxRet, 4) +
    (M.maxRet <= M.r * (1 + 1e-9) ? ' ≤ √3' : ' > √3') + '; ' + at + (M.maxRet > M.r * (1 + 1e-9) && pos ? ' (finite window: the outside mode shows at larger K)' : '') + '.'; }
function readout(el, M, K){ const k = s => '<span class="k">' + s + '</span>', yes = b => b ? 'yes' : 'no';
  const st = M.st, fam = st.regime === 'unitary' ? (st.preset === 'sqrt' ? 'unitary preset (1 − iX)/√2, (1 − iZ)/√2' : st.preset === 'pauli' ? 'unitary preset X, Z (self-inverse: B₃ = B₁, B₄ = B₂)' : 'unitary Haar pair, seed ' + st.seed) + (st.eps > 0 ? ', deformed Uᵢ + ε Rᵢ, ε = ' + st.eps.toFixed(2) + ' (adjoint pairing kept)' : '')
    : st.regime === 'inverse' ? 'inverse-paired B₃ = B₁⁻¹, B₄ = B₂⁻¹ (B₁, B₂ complex Gaussian), seed ' + st.seed : st.regime === 'adjoint' ? 'adjoint-paired B₃ = B₁†, B₄ = B₂†, seed ' + st.seed : 'B₁ = B₃ = diag(1,2), B₂ = B₄ = 1';
  const L = [];
  L.push(k('family    ') + fam);
  L.push(k('pairings  ') + '‖B_ī Bᵢ − 1‖ = ' + e1(M.pe.inv) + ', ‖B_ī − Bᵢ†‖ = ' + e1(M.pe.adj) + '  →  inverse-paired ' + yes(M.invP) + ', adjoint-paired ' + yes(M.adjP) + ', unitary ' + yes(M.invP && M.adjP));
  if (M.kind === 'adjoint') L.push(k('scale     ') + 'Bᵢ → s·Bᵢ with s = ' + WT.fmtF(M.scale, 6) + ' so that the Perron root of T is q = 3 (raw Perron root ' + WT.fmtF(M.mu0raw, 6) + ')');
  L.push(k('Φ = Σ/4   ') + M.hast.phi.map(z => WT.fmtC(z[0], z[1], 4)).join(', ') + '   (comparison)');
  L.push(k('Hastings  ') + 'max |λ| off ±1 = ' + WT.fmtF(M.hast.max, 4) + ' vs 2√3/4 = ' + WT.fmtF(HB, 4) + ': bound ' + (M.hast.holds ? 'holds' : 'fails') + (M.kind === 'unitary' ? '' : '  (the criterion (ii) needs a unitary family)'));
  L.push(k('trivial S ') + M.Sname + ';  r = ' + (M.kind === 'nodual' ? 'p₄ = (5+√73)/2 = ' : '√3 = ') + WT.fmtF(M.r, 4));
  L.push(k('side A    ') + 'Tr Tˡ = Σ_w |Tr B_w|²: ' + M.words.map(o => 'l=' + o.l + ': ' + WT.fmtF(o.tr, 4) + ' (' + o.count + ' words)').join(', ') + ';  max rel. diff ' + e1(Math.max(...M.words.map(o => o.rel))));
  L.push(k('          ') + 'all Tr Tˡ ≥ 0 for l ≤ 16: ' + yes(M.trMinRel >= -1e-12) + ';  max |Im Tr Tˡ|/|Tr Tˡ| = ' + e1(M.trImRel) + ' (conjugation symmetry)');
  L.push(k('side B    ') + 'spec T by QR' + (M.ref ? ' vs ' + (M.kind === 'nodual' ? 'closed form' : 'Ihara–Bass') + ': ' + e1(M.disc.qr) : '') + ';  from the 16 power sums (Newton identities): off by ' + e1(M.disc.newton) +
    ' (ill-conditioned: a root of multiplicity m moves by δ^{1/m}, small roots drown under the largest)');
  L.push(k('retained  ') + M.ret.length + ' modes;  J-invariant (μ ↦ r²/μ̄): ' + yes(M.Jinv) + ';  max ||μ| − r| = ' + WT.fmtF(M.circle, 4) + ';  max |μ| = ' + WT.fmtF(M.maxRet, 4));
  L.push(k('Weil form ') + 'λ_min(K = ' + K + ') = ' + fmtW(M.mins[K - 1], M.nuScale) + ';  K = 4, 8, 12: ' + [4, 8, 12].map(q => fmtW(M.mins[q - 1], M.nuScale)).join(', '));
  L.push(k('verdict   ') + verdict(M, K));
  el.innerHTML = L.join('\n'); }

WT.demos.kraus = function(root){
  const st = Object.assign(defaultState(), { K: 12 }); let M = null;
  const ctl = WT.div(root, 'controls');
  const sel = WT.select(ctl, 'demo-kraus-family', 'family', [['unitary', 'unitary U, U†'], ['inverse', 'inverse-paired (non-unitary)'], ['adjoint', 'adjoint-paired (non-unitary)'], ['nodual', 'no-duality example']], st.regime, v => { st.regime = v; st.preset = null; if (v === 'inverse') st.seed = inverseSeed(st.seed); update(true); });
  WT.button(ctl, 'demo-kraus-reroll', 'reroll', () => { st.seed++; st.preset = null; update(true); });
  WT.button(ctl, 'demo-kraus-ram', 'Ramanujan pair', () => { st.regime = 'unitary'; sel.value = 'unitary'; st.preset = 'sqrt'; update(true); });
  WT.button(ctl, 'demo-kraus-pauli', 'Pauli pair', () => { st.regime = 'unitary'; sel.value = 'unitary'; st.preset = 'pauli'; update(true); });
  const eps = WT.slider(ctl, 'demo-kraus-eps', 'noise ε', 0, 1, 0.01, 0, v => { st.eps = v; update(true); }, v => v.toFixed(2));
  WT.slider(ctl, 'demo-kraus-K', 'window K', 1, KMAX, 1, st.K, v => { st.K = v; update(false); });
  WT.div(root, 'legend', '<span><i style="background:var(--orbit)"></i>ring sums / positive</span><span><i style="background:var(--spec)"></i>eigenvalues / negative</span>' +
    '<span><i style="background:var(--pole)"></i>trivial set S</span><span><i style="border:1.5px solid var(--ink2)"></i>reference (Ihara–Bass / closed form)</span><span><i style="background:var(--metric)"></i>circle |μ| = r</span>');
  const g1 = WT.div(root, 'grid2'), g2 = WT.div(root, 'grid2');
  const sA = WT.svgIn(g1, '0 0 440 300', 'demo-kraus-sigma'), sB = WT.svgIn(g1, '0 0 440 300', 'demo-kraus-spec');
  const sC = WT.svgIn(g2, '0 0 440 300', 'demo-kraus-count'), sD = WT.svgIn(g2, '0 0 440 300', 'demo-kraus-weil');
  const ro = WT.div(root, 'readout'); ro.id = 'demo-kraus-readout';
  function update(recompute){ if (recompute || !M) M = model(st); eps.disabled = st.regime !== 'unitary';
    drawSigma(sA, M); drawT(sB, M); drawCount(sC, M); drawWeil(sD, M, st.K); readout(ro, M, st.K); }
  update(true);
};
WT.demos.kraus.model = { model, eigQR, buildT, readout, family, defaultState, inverseSeed, newtonRoots, wordSum, PRESETS, INV, KMAX };
})();
