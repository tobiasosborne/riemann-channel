/* demos-as.js -- worker AS: the Artin–Schreier transfer-matrix station of "Weil Positivity, Contracted".
 * WT.demos.artinSchreier (mount id demo-artinSchreier). Quadratic family g(x) = sum_j a_j x^{1+q^j}, a_J != 0,
 * psi(t) = exp(2 pi i t/q). E (q^J x q^J; rows = output bond state (s_2..s_J,x), columns = input (s_1..s_J),
 * states in lexicographic order with s_1 most significant) has E_{s->s'} = psi(a_0 x^2 + sum_j a_j s_{J+1-j} x)
 * (notes/artin-schreier-mps.md, eq:as-transfer-entries). Counting side: the exact sign law of thm:as-sign-law /
 * cor:as-periodic-sign, S_n = (1 - 2[2h | n]) Tr E^n, and the affine count N_n = q^n + sum_{a != 0} S_n(a g).
 * Weil form t_k = Tr (E/sqrt q)^k, T[j][k] = t_{k-j}: the Gram matrix of the open strips (prop:ccm-tn-operator-gram).
 * Spectra (comparison only) by a local complex Hessenberg-QR, not WT.cmat.eigvals: charpoly + Durand-Kerner loses
 * ~5 digits at dim 25 on these unitaries (repeated eigenvalues); the QR is backward stable at every dim <= 49.
 * Numerics are exposed as WT.demos.artinSchreier.num for the node cross-check (lanes/check_as.py). */
(function(){
'use strict';
const WT = window.WT, cm = WT.cmat, Cx = WT.C;
const V = {orbit:'var(--orbit)', spec:'var(--spec)', pole:'var(--pole)', bond:'var(--bond)', metric:'var(--metric)', arch:'var(--arch)', ink:'var(--ink)', ink2:'var(--ink2)', line:'var(--line)', bg2:'var(--bg2)', bg3:'var(--bg3)'};
/* brute-force affine counts #{(x,y) in F_{q^n}^2 : y^q - y = g(x)}, precomputed by lanes/check_as.py (direct enumeration) */
const PINNED = {'3|0,1':[3,3,27,27], '3|1,1':[3,9,27,81], '3|0,1,1':[3,9,27], '3|1,0,1':[3,15,27]};
const NMAX = 8, KMAX = 14, TOL = 1e-9;

// ---------- numerics ----------
const digitsOf = (s, q, J) => { const d = []; for (let i = 0; i < J; i++){ d.unshift(s % q); s = Math.floor(s / q); } return d; };
function transfer(q, a){ const J = a.length - 1, d = q ** J, E = cm.zeros(d);
  for (let s = 0; s < d; s++){ const sp = digitsOf(s, q, J);            // sp[0] = s_1 (oldest) ... sp[J-1] = s_J (newest)
    for (let x = 0; x < q; x++){ const r = (s * q + x) % d; let w = a[0] * x * x; for (let j = 1; j <= J; j++) w += a[j] * sp[J - j] * x;
      const th = 2 * Math.PI * (w % q) / q; E.re[r][s] += Math.cos(th); E.im[r][s] += Math.sin(th); } }
  return E; }
/* the perturbed entry: row 0, first column c >= 1 with E[0][c] != 0 (c = 1 for J = 1; for J = 2 E[0][1] is structurally 0, c = q) */
function perturb(E, eps){ const d = E.re.length; let c = 1; while (c < d && Math.hypot(E.re[0][c], E.im[0][c]) < 1e-12) c++;
  const P = {re: E.re.map(r => r.slice()), im: E.im.map(r => r.slice())}; const z = Cx.mul([E.re[0][c], E.im[0][c]], Cx.expi(eps));
  P.re[0][c] = z[0]; P.im[0][c] = z[1]; return {E: P, col: c}; }
/* v_- = order of z = -1 as a root of f(z) = z^J P_g(z), P_g(z) = sum_j (a_j/2)(z^j + z^-j), over F_q; h = least power of q > v_- */
function vMinus(q, a){ const J = a.length - 1, h2 = (q + 1) / 2; let c = new Array(2 * J + 1).fill(0);
  a.forEach((aj, j) => { c[J + j] = (c[J + j] + aj * h2) % q; c[J - j] = (c[J - j] + aj * h2) % q; });
  let v = 0; const md = t => ((t % q) + q) % q;
  while (c.some(x => x) && md(c.reduce((s, x, k) => s + (k % 2 ? -x : x), 0)) === 0){ const out = new Array(c.length - 1).fill(0); let carry = 0;
    for (let k = c.length - 1; k > 0; k--){ carry = md(c[k] + carry); out[k - 1] = carry; carry = md(-carry); } c = out; v++; }
  return v; }
const hPer = (q, v) => { let h = 1; while (h <= v) h *= q; return h; };
/* eigenvalues of a complex matrix: Givens Hessenberg reduction + Wilkinson-shifted QR with deflation */
function eigQR(A){ const n = A.re.length; const H = A.re.map((r, i) => r.map((v, j) => [v, A.im[i][j]])); const ab = Cx.abs, out = [];
  const giv = (a, b) => { const r = Math.hypot(ab(a), ab(b)); if (r < 1e-300) return [1, [0, 0]]; if (ab(a) < 1e-300) return [0, [1, 0]];
    const u = [a[0] / ab(a), a[1] / ab(a)]; return [ab(a) / r, Cx.mul(u, [b[0] / r, -b[1] / r])]; };
  const rowRot = (i, j, c, s, k0, k1) => { for (let k = k0; k <= k1; k++){ const x = H[i][k], y = H[j][k];
    H[i][k] = Cx.add([c * x[0], c * x[1]], Cx.mul(s, y)); H[j][k] = Cx.add(Cx.mul([-s[0], s[1]], x), [c * y[0], c * y[1]]); } };
  const colRot = (i, j, c, s, k0, k1) => { for (let k = k0; k <= k1; k++){ const x = H[k][i], y = H[k][j];
    H[k][i] = Cx.add([c * x[0], c * x[1]], Cx.mul(y, Cx.conj(s))); H[k][j] = Cx.add(Cx.mul([-x[0], -x[1]], s), [c * y[0], c * y[1]]); } };
  for (let k = 0; k < n - 2; k++) for (let i = n - 1; i > k + 1; i--){ const [c, s] = giv(H[i - 1][k], H[i][k]); rowRot(i - 1, i, c, s, 0, n - 1); colRot(i - 1, i, c, s, 0, n - 1); }
  let hi = n - 1, it = 0;
  while (hi >= 0){ if (hi === 0){ out.push(H[0][0]); break; }
    let lo = hi; while (lo > 0 && ab(H[lo][lo - 1]) > 1e-15 * (ab(H[lo][lo]) + ab(H[lo - 1][lo - 1]))) lo--;
    if (lo === hi){ out.push(H[hi][hi]); hi--; it = 0; continue; }
    const a = H[hi - 1][hi - 1], b = H[hi - 1][hi], c = H[hi][hi - 1], d = H[hi][hi]; const m = [(a[0] + d[0]) / 2, (a[1] + d[1]) / 2];
    const disc = Cx.sqrt(Cx.add(Cx.mul(Cx.sub(a, m), Cx.sub(a, m)), Cx.mul(b, c))); let mu = ab(Cx.sub(Cx.add(m, disc), d)) < ab(Cx.sub(Cx.sub(m, disc), d)) ? Cx.add(m, disc) : Cx.sub(m, disc);
    if (++it % 11 === 0) mu = Cx.add(d, [ab(c), 0.7 * ab(c)]); if (it > 3000) break;
    for (let k = lo; k <= hi; k++) H[k][k] = Cx.sub(H[k][k], mu); const G = [];
    for (let k = lo; k < hi; k++){ const g = giv(H[k][k], H[k + 1][k]); G.push(g); rowRot(k, k + 1, g[0], g[1], k, hi); }
    for (let k = lo; k < hi; k++) colRot(k, k + 1, G[k - lo][0], G[k - lo][1], lo, Math.min(k + 2, hi));
    for (let k = lo; k <= hi; k++) H[k][k] = Cx.add(H[k][k], mu); }
  return out; }
const cache = {};
function tracesOf(q, a, K){ const key = q + '|' + a.join(','); if (!cache[key]) cache[key] = cm.powerTraces(transfer(q, a), K); return cache[key]; }
/* everything the panels show, from (q, a, eps) */
function analyse(q, a, eps){ const J = a.length - 1, d = q ** J, sq = Math.sqrt(q); let E = transfer(q, a), col = null;
  if (eps){ const p = perturb(E, eps); E = p.E; col = p.col; }
  const EEd = cm.mul(E, cm.dagger(E)); for (let i = 0; i < d; i++) EEd.re[i][i] -= q; const resid = cm.frob(EEd) / q;
  const Ei = cm.inv(E); const FE = Ei ? cm.add(E, cm.scale(cm.dagger(Ei), [-q, 0])) : null; const fe = FE ? cm.frob(FE) / q : NaN;   // E - q E^{-dagger}
  const tr = cm.powerTraces(E, Math.max(NMAX, KMAX)); const v = vMinus(q, a), h = hPer(q, v);
  const sgn = n => (n % (2 * h) === 0 ? -1 : 1), S = [], N = [], Nim = [];
  for (let n = 1; n <= NMAX; n++){ S.push([sgn(n) * tr[n][0], sgn(n) * tr[n][1]]); let re = q ** n, im = 0;
    for (let b = 1; b < q; b++){ const t = b === 1 ? tr[n] : tracesOf(q, a.map(x => (x * b) % q), NMAX)[n]; re += sgn(n) * t[0]; im += sgn(n) * t[1]; }
    N.push(re); Nim.push(im); }
  const tRe = [], tIm = []; for (let k = 0; k < KMAX; k++){ tRe.push(tr[k][0] / q ** (k / 2)); tIm.push(tr[k][1] / q ** (k / 2)); }
  const mins = []; for (let K = 1; K <= KMAX; K++){ const T = WT.toeplitzC(tRe, tIm, K); mins.push(WT.hermEigvals(T.Re, T.Im)[0]); }
  const ev = eigQR(cm.scale(E, [1 / sq, 0])).map(z => [z[0] * sq, z[1] * sq]);
  const mods = ev.map(Cx.abs), dev = Math.max(...mods.map(r => Math.abs(r - sq)));
  return {q, a, J, d, E, col, resid, fe, tr, v, h, sgn, S, N, Nim, tRe, tIm, mins, ev, mods, dev, P1: (a.reduce((s, x, j) => s + x * (j % 2 ? -1 : 1), 0) % q + q) % q}; }

// ---------- rendering ----------
const S = WT.svg.el, T = WT.svg.text;
const f4 = x => WT.fmtF(x, 4), fC = z => WT.fmtC(z[0], z[1], 2).replace(/ ([+−]) /, '$1'), fE = x => (Math.abs(x) < 1e-300 ? '0' : x.toExponential(1));
function mount(root){
  const st = {q: 3, J: 1, a: [0, 1], eps: 0, K: 8};
  const ctr = WT.div(root, 'controls'), coef = WT.div(root, 'controls');
  const redoCoef = () => { coef.innerHTML = ''; st.a = st.a.slice(0, st.J + 1); while (st.a.length < st.J + 1) st.a.push(1); st.a = st.a.map(x => x % st.q); if (!st.a[st.J]) st.a[st.J] = 1;
    for (let j = 0; j <= st.J; j++){ const opts = []; for (let c = j === st.J ? 1 : 0; c < st.q; c++) opts.push([String(c), String(c)]);
      WT.select(coef, 'demo-artinSchreier-a' + j, 'a<sub>' + j + '</sub>' + (j === st.J ? ' (≠ 0)' : ''), opts, String(st.a[j]), v => { st.a[j] = +v; draw(); }); } };
  WT.select(ctr, 'demo-artinSchreier-q', 'q', [['3', '3'], ['5', '5'], ['7', '7']], '3', v => { st.q = +v; redoCoef(); draw(); });
  WT.select(ctr, 'demo-artinSchreier-J', 'range J', [['1', '1'], ['2', '2']], '1', v => { st.J = +v; redoCoef(); draw(); });
  WT.slider(ctr, 'demo-artinSchreier-eps', 'perturb ε', 0, 0.5, 0.01, 0, v => { st.eps = v; draw(); }, v => v.toFixed(2));
  WT.slider(ctr, 'demo-artinSchreier-K', 'window K', 2, KMAX, 1, 8, v => { st.K = v; draw(); });
  const g1 = WT.div(root, 'grid2'), g2 = WT.div(root, 'grid2');
  const svgE = WT.svgIn(g1, '0 0 380 400', 'demo-artinSchreier-phase'), svgP = WT.svgIn(g1, '0 0 380 400', 'demo-artinSchreier-spec');
  const cBox = WT.div(g2, ''), wBox = WT.div(g2, ''); cBox.style.minWidth = wBox.style.minWidth = '0';
  const svgC = WT.svgIn(cBox, '0 0 380 190', 'demo-artinSchreier-count'); const tbl = WT.div(cBox, '', ''); tbl.style.overflowX = 'auto';
  const svgW = WT.svgIn(wBox, '0 0 380 250', 'demo-artinSchreier-weil'), svgM = WT.svgIn(wBox, '0 0 380 206', 'demo-artinSchreier-mins');
  const out = WT.div(root, 'readout'); out.id = 'demo-artinSchreier-readout';
  redoCoef();

  function drawPhase(R){ WT.svg.clear(svgE); const d = R.d, x0 = 44, y0 = 40, cell = Math.floor(320 / d), p = R.q;
    T(svgE, 8, 16, 'E: phase of each entry ψ(k) = e^{2πik/' + p + '}', {'font-size': '12', fill: V.ink});
    const lab = s => digitsOf(s, R.q, R.J).join('');
    for (let i = 0; i < d; i++) for (let j = 0; j < d; j++){ const re = R.E.re[i][j], im = R.E.im[i][j], r = Math.hypot(re, im);
      const X = x0 + j * cell, Y = y0 + i * cell; if (r < 1e-12){ S('rect', {x: X, y: Y, width: cell - 1, height: cell - 1, fill: V.bg3}, svgE); continue; }
      const th = Math.atan2(im, re), k = ((Math.round(th * p / (2 * Math.PI)) % p) + p) % p;
      S('rect', {x: X, y: Y, width: cell - 1, height: cell - 1, rx: 1.5, fill: WT.CYC[k], opacity: d <= 25 ? 0.42 : 0.8, stroke: (i === 0 && j === R.col) ? V.spec : 'none', 'stroke-width': 2.5}, svgE);
      if (d <= 25){ const cx = X + cell / 2 - .5, cy = Y + cell / 2 - .5, L = cell * 0.36; S('line', {x1: cx, y1: cy, x2: cx + L * Math.cos(th), y2: cy - L * Math.sin(th), stroke: V.ink, 'stroke-width': cell > 20 ? 1.6 : 1, 'stroke-linecap': 'round'}, svgE);
        S('circle', {cx: cx + L * Math.cos(th), cy: cy - L * Math.sin(th), r: cell > 20 ? 2 : 1, fill: V.ink}, svgE); } }
    const fs = d <= 9 ? 10 : d <= 25 ? 7 : 5.5;
    for (let i = 0; i < d; i++){ T(svgE, x0 - 3, y0 + i * cell + cell / 2 + fs / 3, lab(i), {'font-size': fs, 'text-anchor': 'end'}); T(svgE, x0 + i * cell + cell / 2, y0 - 3, lab(i), {'font-size': fs, 'text-anchor': 'middle'}); }
    T(svgE, x0, y0 + d * cell + 14, R.J === 1 ? 'rows: out x   cols: in s₁' : 'rows: out (s₂, x)   cols: in (s₁, s₂)', {'font-size': '9.5'});
    for (let k = 0; k < p; k++){ S('rect', {x: x0 + k * 44, y: y0 + d * cell + 22, width: 10, height: 10, fill: WT.CYC[k], opacity: .7}, svgE); T(svgE, x0 + k * 44 + 13, y0 + d * cell + 31, 'ψ(' + k + ')', {'font-size': '9.5'}); } }

  function drawSpec(R, R0){ WT.svg.clear(svgP); const sq = Math.sqrt(R.q), sc = 128 / sq; const P = WT.svg.plane(svgP, 190, 212, sc, sq, {line: V.ink2});
    T(svgP, 8, 16, 'spectrum of E  (comparison)', {'font-size': '12', fill: V.ink}); T(svgP, 8, 32, 'dashed circle |λ| = √q = ' + f4(sq), {'font-size': '10'});
    if (R0) R0.ev.forEach(z => S('circle', {cx: P.X(z[0]), cy: P.Y(z[1]), r: 5.5, fill: 'none', stroke: V.ink2, 'stroke-width': 1.2}, svgP));
    R.ev.forEach(z => { const off = Math.abs(Cx.abs(z) - sq) > 1e-6; S('circle', {cx: P.X(z[0]), cy: P.Y(z[1]), r: 3.4, fill: V.spec, opacity: .85, stroke: off ? V.ink : 'none', 'stroke-width': .8}, svgP); });
    T(svgP, 8, 392, R0 ? 'filled: perturbed E; hollow: the true E (ε = 0)' : dimNote(R), {'font-size': '10'}); }
  const dimNote = R => 'dim E = ' + R.d + ' eigenvalues (with multiplicity)';

  function drawCount(R){ WT.svg.clear(svgC); const x0 = 34, y0 = 104, w = 40; let mx = 1; for (let n = 1; n <= NMAX; n++) mx = Math.max(mx, Cx.abs(R.tr[n]) / R.q ** (n / 2)); const hs = 78 / mx;
    T(svgC, 8, 16, 'counting side: Tr Eⁿ/q^(n/2)  (Re dark, Im light)', {'font-size': '11.5', fill: V.ink});
    WT.svg.axis(svgC, x0 - 4, y0, x0 + NMAX * w, y0); T(svgC, x0 - 6, y0 - 78 + 4, '+' + WT.fmtF(mx, 1), {'font-size': '9', 'text-anchor': 'end'}); T(svgC, x0 - 6, y0 + 78 + 4, '−' + WT.fmtF(mx, 1), {'font-size': '9', 'text-anchor': 'end'});
    for (let n = 1; n <= NMAX; n++){ const s = R.q ** (n / 2), re = R.tr[n][0] / s, im = R.tr[n][1] / s, X = x0 + (n - 1) * w;
      [[re, 1], [im, .45]].forEach(([v, op], k) => S('rect', {x: X + 4 + k * 15, y: v >= 0 ? y0 - v * hs : y0, width: 13, height: Math.max(.5, Math.abs(v) * hs), fill: V.orbit, opacity: op}, svgC));
      T(svgC, X + 18, y0 + 80, 'n=' + n, {'font-size': '9', 'text-anchor': 'middle'}); }
    let rows = '<table class="tbl" style="font-size:.78rem;white-space:nowrap"><tr><th>n</th><th>Tr Eⁿ</th><th>S<sub>n</sub></th><th>N<sub>n</sub> transfer</th><th>brute†</th><th>|N<sub>n</sub>−qⁿ| ≤ band</th></tr>';
    const pin = PINNED[R.q + '|' + R.a.join(',')];
    for (let n = 1; n <= NMAX; n++){ const Nn = R.N[n - 1], ok = Math.abs(R.Nim[n - 1]) < 1e-6 && Math.abs(Nn - Math.round(Nn)) < 1e-6 && Nn > -1e-6;
      const band = R.d * (R.q - 1) * R.q ** (n / 2), dv = Math.abs(Nn - R.q ** n);
      rows += `<tr><td>${n}</td><td class="num">${fC(R.tr[n])}</td><td class="num">${fC(R.S[n - 1])}</td><td class="num ${ok ? 'orbit' : 'spec'}">${ok ? Math.round(Nn) : WT.fmtC(Nn, R.Nim[n - 1], 3) + ' ✗'}</td>` +
        `<td class="num">${pin && pin[n - 1] != null ? pin[n - 1] + (ok && Math.round(Nn) === pin[n - 1] ? ' ✓' : ' ✗') : '—'}</td><td class="num">${ok ? Math.round(dv) : f4(dv)} ≤ ${WT.fmtF(band, 1)}</td></tr>`; }
    tbl.innerHTML = rows + '</table><p class="small" style="margin:4px 0">† brute force (precomputed): direct count of (x, y) ∈ F<sub>q<sup>n</sup></sub><sup>2</sup> with y<sup>q</sup> − y = g(x), lanes/check_as.py; pinned for q = 3 only. Band = q<sup>J</sup>(q−1)q<sup>n/2</sup>. N<sub>n</sub> is the affine count (the projective curve adds 1).</p>'; }

  function drawWeil(R){ WT.svg.clear(svgW); WT.svg.clear(svgM); const K = st.K, T0 = WT.toeplitzC(R.tRe, R.tIm, K), cell = Math.floor(200 / K);
    T(svgW, 8, 16, 'Weil form Re t_(k−j), t_k = Tr(E/√q)^k, K = ' + K, {'font-size': '11.5', fill: V.ink});
    WT.svg.heat(svgW, T0.Re, 90, 32, cell, V, {vmax: R.d, numbers: cell >= 26 && K <= 7, digits: 1});
    T(svgW, 8, 244, 'Gram matrix of the open strips E⁰..E^{K−1} (native metric)', {'font-size': '9.5'});
    const x0 = 46, y0 = 100, w = 300 / KMAX, tf = v => Math.asinh(v / 0.05), ymax = Math.max(tf(Math.max(...R.mins.map(Math.abs))), tf(1)), hs = 70 / ymax;
    T(svgM, 8, 16, 'λ_min of the K × K Weil form, K = 1..' + KMAX + '  (asinh scale)', {'font-size': '11.5', fill: V.ink});
    WT.svg.axis(svgM, x0, y0, x0 + KMAX * w, y0); [0.1, 1, 10].forEach(v => { if (tf(v) <= ymax) [v, -v].forEach(u => { const y = y0 - tf(u) * hs; S('line', {x1: x0, y1: y, x2: x0 + KMAX * w, y2: y, class: 'grid'}, svgM); T(svgM, x0 - 4, y + 3, (u > 0 ? '+' : '−') + v, {'font-size': '8.5', 'text-anchor': 'end'}); }); });
    R.mins.forEach((m, i) => { const neg = m < -TOL, X = x0 + (i + .5) * w, Y = y0 - tf(neg ? m : Math.max(m, 0)) * hs;
      S('circle', {cx: X, cy: Y, r: i + 1 === K ? 5 : 3.5, fill: neg ? V.spec : V.bond, stroke: i + 1 === K ? V.ink : 'none'}, svgM); if ((i + 1) % 2 === 0) T(svgM, X, y0 + 84, String(i + 1), {'font-size': '8.5', 'text-anchor': 'middle'}); });
    T(svgM, x0, 200, 'x axis: K.  blue: ≥ 0 (within ' + TOL + ');  orange: negative', {'font-size': '9'}); }

  let memo = {};
  function draw(){ const key = st.q + '|' + st.a.join(','); if (memo.key !== key) memo = {key, R0: analyse(st.q, st.a, 0)};
    const R = st.eps ? analyse(st.q, st.a, st.eps) : memo.R0, R0 = st.eps ? memo.R0 : null, sq = Math.sqrt(st.q);
    drawPhase(R); drawSpec(R, R0); drawCount(R); drawWeil(R);
    const L = [], mn = Math.min(...R.mins), kmin = R.mins.indexOf(mn) + 1, kneg = R.mins.findIndex(m => m < -TOL) + 1;
    const gs = 'g(x) = ' + R.a.map((c, j) => c ? (c === 1 ? '' : c) + 'x^' + (1 + st.q ** j) : null).filter(Boolean).join(' + ');
    L.push(`${gs} over F_${st.q};  curve y^${st.q} − y = g(x)`);
    L.push(`dim E = q^J = ${R.d}: bond (s₁..s_J) ∈ F_${st.q}^${R.J}, physical index x ∈ F_${st.q}`);
    if (R.J === 1) L.push(`J = 1: E_{s→x} = ψ(${R.a[0]}x² + ${R.a[1]}sx) is a ${st.q}×${st.q} chirp-modulated Fourier matrix: the DFT at frequency a₁ = ${R.a[1]}, times the output chirp ψ(a₀x²)`);
    L.push(`unitarity residual ‖EE† − qI‖_F / q = ${fE(R.resid)};  functional equation ‖E − q E^{−†}‖_F / q = ${fE(R.fe)}`);
    L.push(`eigenvalue moduli (comparison): [${f4(Math.min(...R.mods))}, ${f4(Math.max(...R.mods))}], √q = ${f4(sq)}, max ||λ| − √q| = ${fE(R.dev)}`);
    L.push(`sign law (thm:as-sign-law): v₋ = ${R.v}, h = ${R.h}; S_n = (1 − 2[${2 * R.h} | n]) Tr Eⁿ` + (R.v === 0 ? '  (= −(−1)ⁿ Tr Eⁿ, since P_g(−1) ≠ 0)' : `  (P_g(−1) = 0: the law −(−1)ⁿ Tr Eⁿ fails at every even n with ${2 * R.h} ∤ n)`));
    if (!st.eps){
      L.push(`E/√q unitary: the Toeplitz form is the Gram matrix Tr((Eʲ)† Eᵏ)/q^{(j+k)/2} of the open strips; RH manifest.  λ_min over K = 1..${KMAX}: ${fE(mn)} (≥ −${TOL})`);
      L.push(`why unitary: in (EE†)_{s's''} the oldest spin s₁ couples only linearly, a_J s₁(x' − x''), so Σ_{s₁} ψ(a_J s₁(x' − x'')) = q δ_{x'x''} (a_J = ${R.a[R.J]} ≠ 0; Parseval for additive characters)`);
      L.push(`no pole to subtract for the sum itself: every eigenvalue of E is a zero (deg L = q^J = ${R.d}); the pole qⁿ enters only in N_n = qⁿ + Σ_a S_n(ag)`);
    } else {
      const off = R.mods.filter(r => Math.abs(r - sq) > 1e-6), outN = R.mods.filter(r => r > sq + 1e-6).length;
      L.push(`perturbed entry E[0][${R.col}] (in ${digitsOf(R.col, st.q, R.J).join('')} → out ${digitsOf(0, st.q, R.J).join('')}) × e^{i·${st.eps.toFixed(2)}}: not arithmetic, N_n stops being a count`);
      L.push(`unitarity broken by ${f4(R.resid)}: ${off.length} eigenvalues off the circle (${outN} outside, ${off.length - outN} inside), ` + (kneg ? `λ_min = ${f4(mn)} at K = ${kmin} (first negative at K = ${kneg})` : `λ_min = ${fE(mn)} at K = ${kmin}`));
      if (!kneg) L.push(outN ? `an eigenvalue is outside the disc, so a larger window than K = ${KMAX} will turn the form negative (T1)` : `no eigenvalue left the closed disc (${off.length} moved inside, ${R.d - off.length} still on the circle): T1 is one-sided, so the Weil form stays ≥ 0 and cannot see this break; the counting side can (N_n is no longer an integer)`);
    }
    out.textContent = L.join('\n'); }
  draw();
}
mount.num = {transfer, perturb, vMinus, hPer, eigQR, analyse, PINNED};
WT.demos.artinSchreier = mount;
})();
