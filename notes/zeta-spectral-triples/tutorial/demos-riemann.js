/* demos-riemann.js -- stations 5, 6, 7 of the "Zeros From Counts" tutorial (worker B).
 *
 *   ZT.demos.secular    (5) the secular function g(s) = sum_j xi_j/(j - s) and D' = D - |D xi><eta|
 *   ZT.demos.riemann    (6) the precomputed Riemann realisation (needs riemann-data.js)
 *   ZT.demos.algorithm  (7) the five steps, permutation and zeta side by side
 *
 * Helpers from core.js are used when they exist and match the contract's signature:
 * ZT.svg.el, ZT.fmt, ZT.onChange, ZT.symEig, ZT.polyRootsDK, ZT.parseCycles, ZT.countsOf,
 * ZT.toeplitz.  Each call is guarded (for the permutation pipeline, by checking the documented
 * convention counts[0] = n and T[0][0] = n) and falls back to the private implementations at the
 * top of this file, so the demos also run if core.js is missing or changes.  ZT.svg.axes is NOT
 * used: the contract gives its return value ({X, Y}) but no argument list, so axes are drawn by
 * the local `plot()` below rather than guessed at.
 *
 * Colours only through the CSS custom properties of theme.css.
 */
(function () {
  'use strict';

  var ZT = window.ZT = window.ZT || {};
  ZT.demos = ZT.demos || {};
  var SVGNS = 'http://www.w3.org/2000/svg';
  var SUB = ['\u2080', '\u2081', '\u2082', '\u2083', '\u2084', '\u2085', '\u2086', '\u2087', '\u2088', '\u2089'];
  function sub(n) { return String(n).split('').map(function (d) { return SUB[+d]; }).join(''); }

  /* ================= generic helpers (core.js when available) ================= */

  function elLocal(tag, attrs) {
    var e = document.createElementNS(SVGNS, tag);
    for (var k in attrs) if (attrs[k] !== null && attrs[k] !== undefined) e.setAttribute(k, attrs[k]);
    return e;
  }
  function el(tag, attrs) {
    if (ZT.svg && typeof ZT.svg.el === 'function') { try { return ZT.svg.el(tag, attrs); } catch (e) { /* fall through */ } }
    return elLocal(tag, attrs);
  }
  function txt(x, y, s, attrs) {
    var t = el('text', Object.assign({ x: x, y: y, fill: 'var(--ink-2)', 'font-size': 11 }, attrs || {}));
    t.textContent = s;
    return t;
  }
  function h(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html !== undefined) e.innerHTML = html;
    return e;
  }
  function fmt(x, d) {
    if (typeof ZT.fmt === 'function') { try { var s = ZT.fmt(x, d); if (typeof s === 'string') return s; } catch (e) { /* fall through */ } }
    if (!isFinite(x)) return String(x);
    if (x !== 0 && (Math.abs(x) < 1e-4 || Math.abs(x) >= 1e6)) return x.toExponential(Math.max(0, (d || 6) - 1));
    return x.toFixed(Math.max(0, d === undefined ? 6 : d));
  }
  function onChange(els, fn) {
    if (typeof ZT.onChange === 'function') { try { return ZT.onChange(els, fn); } catch (e) { /* fall through */ } }
    els.forEach(function (e) {
      e.addEventListener('input', fn);
      e.addEventListener('change', fn);
      if (e.tagName === 'BUTTON') e.addEventListener('click', fn);
    });
  }
  function reducedMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  /* ---- symmetric eigenproblem (Jacobi): fallback for ZT.symEig ---- */
  function jacobiEig(Ain) {
    var n = Ain.length, A = Ain.map(function (r) { return r.slice(); }), V = [], i, j, k, p, q;
    for (i = 0; i < n; i++) { V.push(new Array(n).fill(0)); V[i][i] = 1; }
    for (var sweep = 0; sweep < 60; sweep++) {
      var off = 0;
      for (p = 0; p < n; p++) for (q = p + 1; q < n; q++) off += A[p][q] * A[p][q];
      if (Math.sqrt(off) < 1e-16) break;
      for (p = 0; p < n; p++) for (q = p + 1; q < n; q++) {
        if (A[p][q] === 0) continue;
        var th = (A[q][q] - A[p][p]) / (2 * A[p][q]);
        var t = (th >= 0 ? 1 : -1) / (Math.abs(th) + Math.sqrt(th * th + 1));
        var c = 1 / Math.sqrt(t * t + 1), s = t * c, a1, a2;
        for (k = 0; k < n; k++) { a1 = A[k][p]; a2 = A[k][q]; A[k][p] = c * a1 - s * a2; A[k][q] = s * a1 + c * a2; }
        for (k = 0; k < n; k++) { a1 = A[p][k]; a2 = A[q][k]; A[p][k] = c * a1 - s * a2; A[q][k] = s * a1 + c * a2; }
        for (k = 0; k < n; k++) { a1 = V[k][p]; a2 = V[k][q]; V[k][p] = c * a1 - s * a2; V[k][q] = s * a1 + c * a2; }
      }
    }
    var idx = A.map(function (r, m) { return m; }).sort(function (a, b) { return A[a][a] - A[b][b]; });
    return { values: idx.map(function (m) { return A[m][m]; }),
             vectors: V.map(function (r) { return idx.map(function (m) { return r[m]; }); }) };
  }
  function eigOK(A, r) {           // values ascending, vectors in COLUMNS, and A v = lambda v
    var n = A.length, i, j, s, scale = 0, m = 0;
    if (!r || !r.values || !r.vectors || r.values.length !== n || !r.vectors[0] ||
        r.vectors[0].length !== n) return false;
    for (i = 0; i < n; i++) for (j = 0; j < n; j++) scale = Math.max(scale, Math.abs(A[i][j]));
    for (i = 1; i < n; i++) if (r.values[i] < r.values[i - 1] - 1e-9 * (scale + 1)) return false;
    for (i = 0; i < n; i++) {
      for (s = 0, j = 0; j < n; j++) s += A[i][j] * r.vectors[j][0];
      m = Math.max(m, Math.abs(s - r.values[0] * r.vectors[i][0]));
    }
    return m < 1e-8 * (scale + 1);
  }
  function symEig(A) {
    if (typeof ZT.symEig === 'function') {
      try {
        var r = ZT.symEig(A);
        if (eigOK(A, r)) return r;
      } catch (e) { /* fall through */ }
    }
    return jacobiEig(A);
  }

  /* ---- unsymmetric eigenvalues: Householder-Hessenberg + Wilkinson-shifted QR ----
     Used only in station 5, on the (2N+1)x(2N+1) matrix D'.  Complex pairs are reported as
     such: with mixed signs in xi the roots need not be real, and that is the point of the demo. */
  function qrEigen(Ain) {
    var n = Ain.length, A = Ain.map(function (r) { return r.slice(); }), i, j, k, s;
    for (k = 0; k < n - 2; k++) {
      var nrm = 0;
      for (i = k + 1; i < n; i++) nrm += A[i][k] * A[i][k];
      nrm = Math.sqrt(nrm);
      if (nrm < 1e-300) continue;
      var alpha = A[k + 1][k] > 0 ? -nrm : nrm, v = new Array(n).fill(0), vv = 0;
      v[k + 1] = A[k + 1][k] - alpha;
      for (i = k + 2; i < n; i++) v[i] = A[i][k];
      for (i = k + 1; i < n; i++) vv += v[i] * v[i];
      if (vv < 1e-300) continue;
      for (j = 0; j < n; j++) {
        for (s = 0, i = k + 1; i < n; i++) s += v[i] * A[i][j];
        s = 2 * s / vv;
        for (i = k + 1; i < n; i++) A[i][j] -= s * v[i];
      }
      for (i = 0; i < n; i++) {
        for (s = 0, j = k + 1; j < n; j++) s += A[i][j] * v[j];
        s = 2 * s / vv;
        for (j = k + 1; j < n; j++) A[i][j] -= s * v[j];
      }
    }
    var out = [], hi = n - 1, iter = 0, since = 0;
    while (hi >= 0) {
      if (hi === 0) { out.push({ re: A[0][0], im: 0 }); break; }
      var lo = hi;
      while (lo > 0 && Math.abs(A[lo][lo - 1]) >
             1e-15 * (Math.abs(A[lo][lo]) + Math.abs(A[lo - 1][lo - 1]) + 1e-300)) lo--;
      if (lo === hi) { out.push({ re: A[hi][hi], im: 0 }); hi--; since = 0; continue; }
      var a = A[hi - 1][hi - 1], b = A[hi - 1][hi], c = A[hi][hi - 1], d = A[hi][hi];
      var tr = a + d, det = a * d - b * c, disc = tr * tr / 4 - det, r;
      if (lo === hi - 1) {
        if (disc >= 0) { r = Math.sqrt(disc); out.push({ re: tr / 2 + r, im: 0 }); out.push({ re: tr / 2 - r, im: 0 }); }
        else { r = Math.sqrt(-disc); out.push({ re: tr / 2, im: r }); out.push({ re: tr / 2, im: -r }); }
        hi -= 2; since = 0; continue;
      }
      if (++iter > 300 * n) {
        for (i = lo; i <= hi; i++) out.push({ re: A[i][i], im: 0, unconverged: true });
        hi = lo - 1; continue;
      }
      var mu;
      if (++since % 17 === 0) mu = Math.abs(A[hi][hi - 1]) + Math.abs(hi > 1 ? A[hi - 1][hi - 2] : 0);
      else if (disc >= 0) { r = Math.sqrt(disc); var e1 = tr / 2 + r, e2 = tr / 2 - r; mu = Math.abs(e1 - d) < Math.abs(e2 - d) ? e1 : e2; }
      else mu = d;
      var cs = [], sn = [];
      for (i = lo; i <= hi; i++) A[i][i] -= mu;
      for (k = lo; k < hi; k++) {
        var x = A[k][k], y = A[k + 1][k], rr = Math.hypot(x, y);
        var cc = rr < 1e-300 ? 1 : x / rr, ss = rr < 1e-300 ? 0 : y / rr;
        cs.push(cc); sn.push(ss);
        for (j = k; j <= hi; j++) {
          var t1 = A[k][j], t2 = A[k + 1][j];
          A[k][j] = cc * t1 + ss * t2; A[k + 1][j] = -ss * t1 + cc * t2;
        }
      }
      for (k = lo; k < hi; k++) {
        var c2 = cs[k - lo], s2 = sn[k - lo];
        for (i = lo; i <= Math.min(hi, k + 2); i++) {
          var u1 = A[i][k], u2 = A[i][k + 1];
          A[i][k] = c2 * u1 + s2 * u2; A[i][k + 1] = -s2 * u1 + c2 * u2;
        }
      }
      for (i = lo; i <= hi; i++) A[i][i] += mu;
    }
    return out.sort(function (p, q) { return p.re - q.re || p.im - q.im; });
  }

  /* ---- Durand-Kerner: fallback for ZT.polyRootsDK (coefficients ascending) ---- */
  function dkLocal(coeffs) {
    var c = coeffs.slice();
    while (c.length > 1 && Math.abs(c[c.length - 1]) < 1e-12) c.pop();
    var d = c.length - 1, k, j;
    if (d < 1) return [];
    var zr = [], zi = [];
    for (k = 0; k < d; k++) { zr.push(Math.cos(0.4 + 2.3 * k)); zi.push(Math.sin(0.4 + 2.3 * k)); }
    for (var it = 0; it < 500; it++) {
      var move = 0;
      for (k = 0; k < d; k++) {
        var nr = 0, ni = 0, t;
        for (j = d; j >= 0; j--) { t = nr * zr[k] - ni * zi[k] + c[j]; ni = nr * zi[k] + ni * zr[k]; nr = t; }
        nr /= c[d]; ni /= c[d];
        var dr = 1, di = 0;
        for (j = 0; j < d; j++) {
          if (j === k) continue;
          var ar = zr[k] - zr[j], ai = zi[k] - zi[j];
          t = dr * ar - di * ai; di = dr * ai + di * ar; dr = t;
        }
        var den = dr * dr + di * di;
        if (den < 1e-300) continue;
        var qr = (nr * dr + ni * di) / den, qi = (ni * dr - nr * di) / den;
        zr[k] -= qr; zi[k] -= qi; move += Math.abs(qr) + Math.abs(qi);
      }
      if (move < 1e-15) break;
    }
    return zr.map(function (v, m) { return { re: v, im: zi[m] }; });
  }
  function polyRoots(coeffs) {
    if (typeof ZT.polyRootsDK === 'function') {
      try {
        var r = ZT.polyRootsDK(coeffs);
        if (r && r.length && typeof r[0].re === 'number') return r;
      } catch (e) { /* fall through */ }
    }
    return dkLocal(coeffs);
  }

  /* ---- permutation pipeline (guarded reuse of core.js) ---- */
  function permOf(str, n) {
    if (typeof ZT.parseCycles === 'function') {
      try {
        var p = ZT.parseCycles(str, n);
        if (Array.isArray(p) && p.length === n && p.every(function (v) { return v >= 0 && v < n; })) return p;
      } catch (e) { /* fall through */ }
    }
    var q = []; for (var i = 0; i < n; i++) q.push(i);
    (String(str).match(/\(([^)]*)\)/g) || []).forEach(function (cs) {
      var els = cs.replace(/[()]/g, '').trim().split(/[\s,]+/).filter(function (s) { return s.length; })
        .map(function (s) { return parseInt(s, 10) - 1; }).filter(function (v) { return v >= 0 && v < n; });
      for (var k = 0; k < els.length; k++) q[els[k]] = els[(k + 1) % els.length];
    });
    return q;
  }
  function countsLocal(perm, K) {
    var n = perm.length, out = [n], q = perm.slice(), k, i, f;
    for (k = 1; k <= K; k++) {
      for (f = 0, i = 0; i < n; i++) if (q[i] === i) f++;
      out.push(f);
      q = q.map(function (v) { return perm[v]; });
    }
    return out;                                    // out[k] = #Fix(sigma^k), out[0] = n
  }
  function countsOf(perm, K) {
    if (typeof ZT.countsOf === 'function') {
      try {
        var c = ZT.countsOf(perm, K);
        if (Array.isArray(c) && c[0] === perm.length && c.length >= K + 1) return c;
      } catch (e) { /* fall through */ }
    }
    return countsLocal(perm, K);
  }
  function toeplitzOf(counts, M) {
    var U = [], i, j;
    for (i = 0; i <= M; i++) { U.push([]); for (j = 0; j <= M; j++) U[i].push(counts[Math.abs(i - j)]); }
    if (typeof ZT.toeplitz === 'function') {
      try {
        /* Only reuse core's matrix if it agrees entry by entry with the documented convention
           T_jk = N_{|j-k|}, N_0 = n.  core.countsOf returns N_1..N_K (no N_0), so core.toeplitz
           reads a differently indexed array than the one built here: checking T[0][0] alone is
           not enough, the off-diagonals come out shifted by one. */
        var T = ZT.toeplitz(counts, M), ok = !!T && T.length === M + 1;
        for (i = 0; ok && i <= M; i++) {
          if (!T[i] || T[i].length !== M + 1) { ok = false; break; }
          for (j = 0; j <= M; j++) if (T[i][j] !== U[i][j]) { ok = false; break; }
        }
        if (ok) return T;
      } catch (e) { /* fall through */ }
    }
    return U;
  }

  /* ---- secular function, its roots, and D' ---- */
  function secG(xi, N, s) {                        // xi is the even half xi_0..xi_N
    var v = -xi[0] / s;
    for (var j = 1; j <= N; j++) v += 2 * s * xi[j] / (j * j - s * s);
    return v;
  }
  function secRoots(xi, N, smax) {
    smax = smax || 20 * (N + 2);
    var roots = [], ramp = [], k;
    for (k = 0; k <= 60; k++) ramp.push(Math.pow(10, -13 + (Math.log10(0.5) + 13) * k / 60));
    function bisect(a, b) {
      var fa = secG(xi, N, a), fm;
      for (var it = 0; it < 200; it++) {
        var m = 0.5 * (a + b);
        if (!(m > a && m < b)) break;
        fm = secG(xi, N, m);
        if (fm === 0) return m;
        if (fa * fm < 0) b = m; else { a = m; fa = fm; }
      }
      return 0.5 * (a + b);
    }
    function scan(grid) {
      var prev = grid[0], fprev = secG(xi, N, prev);
      for (var i = 1; i < grid.length; i++) {
        var s = grid[i], f = secG(xi, N, s);
        if (f === 0) roots.push(s);
        else if (fprev * f < 0) roots.push(bisect(prev, s));
        prev = s; fprev = f;
      }
    }
    for (var j = 0; j < N; j++) {                  // one pass per pole interval (j, j+1)
      var g = [];
      ramp.forEach(function (d) { g.push(j + d); });
      for (k = 1; k < 96; k++) g.push(j + k / 96);
      ramp.forEach(function (d) { g.push(j + 1 - d); });
      g.sort(function (a, b) { return a - b; });
      scan(g);
    }
    var outer = [];                                // and one beyond the last pole s = N
    ramp.forEach(function (d) { outer.push(N + d); });
    for (k = 1; k <= 64 * 4 * (N + 1); k++) outer.push(N + k / 64);
    var t = N + 4 * (N + 1);
    while (t < smax) { outer.push(t); t *= 1.02; }
    outer.push(smax);
    scan(outer);
    return roots.sort(function (a, b) { return a - b; });
  }
  function dPrime(xi, N) {                         // D' = diag(j) - (D xi) eta^T, j = -N..N
    var n = 2 * N + 1, M = [], r, c;
    for (r = 0; r < n; r++) {
      var i = r - N, w = -i * xi[Math.abs(i)], row = [];
      for (c = 0; c < n; c++) row.push(w);
      row[r] += i;
      M.push(row);
    }
    return M;
  }

  /* ---- a minimal plotting frame (viewBox + width 100%, colours via CSS variables) ---- */
  function plot(w, hh, xdom, ydom, pad) {
    pad = Object.assign({ l: 34, r: 8, t: 10, b: 22 }, pad || {});
    var svg = el('svg', { viewBox: '0 0 ' + w + ' ' + hh, width: '100%',
                          preserveAspectRatio: 'xMidYMid meet', role: 'img' });
    var x0 = pad.l, x1 = w - pad.r, y0 = hh - pad.b, y1 = pad.t;
    function X(v) { return x0 + (v - xdom[0]) / (xdom[1] - xdom[0]) * (x1 - x0); }
    function Y(v) { return y0 + (v - ydom[0]) / (ydom[1] - ydom[0]) * (y1 - y0); }
    var P = { svg: svg, X: X, Y: Y, w: w, h: hh, box: { x0: x0, x1: x1, y0: y0, y1: y1 } };
    P.add = function (e) { svg.appendChild(e); return e; };
    P.axes = function (xt, yt, xlab, ylab) {
      svg.appendChild(el('line', { x1: x0, y1: Y(0) >= y1 && Y(0) <= y0 ? Y(0) : y0, x2: x1,
                                   y2: Y(0) >= y1 && Y(0) <= y0 ? Y(0) : y0, stroke: 'var(--rule)' }));
      svg.appendChild(el('line', { x1: x0, y1: y0, x2: x0, y2: y1, stroke: 'var(--rule)' }));
      (xt || []).forEach(function (t) {
        var v = typeof t === 'object' ? t.v : t, s = typeof t === 'object' ? t.s : String(t);
        svg.appendChild(el('line', { x1: X(v), y1: y0, x2: X(v), y2: y0 + 4, stroke: 'var(--rule)' }));
        svg.appendChild(txt(X(v), y0 + 15, s, { 'text-anchor': 'middle', 'font-size': 10 }));
      });
      (yt || []).forEach(function (t) {
        var v = typeof t === 'object' ? t.v : t, s = typeof t === 'object' ? t.s : String(t);
        svg.appendChild(el('line', { x1: x0 - 4, y1: Y(v), x2: x0, y2: Y(v), stroke: 'var(--rule)' }));
        svg.appendChild(txt(x0 - 6, Y(v) + 3.5, s, { 'text-anchor': 'end', 'font-size': 10 }));
      });
      if (xlab) svg.appendChild(txt(x1, hh - 2, xlab, { 'text-anchor': 'end', 'font-size': 10, fill: 'var(--ink-3)' }));
      if (ylab) svg.appendChild(txt(0, 0, ylab, { 'font-size': 10, fill: 'var(--ink-3)',
        'text-anchor': 'middle', transform: 'translate(8.5,' + ((y0 + y1) / 2) + ') rotate(-90)' }));
      return P;
    };
    return P;
  }
  function figure(caption) {
    var f = document.createElement('figure');
    var cap = document.createElement('figcaption');
    cap.innerHTML = caption || '';
    f._cap = cap;
    f.appendChild(cap);
    f.mount = function (svg) {
      while (f.firstChild && f.firstChild !== cap) f.removeChild(f.firstChild);
      f.insertBefore(svg, cap);
      return f;
    };
    return f;
  }
  function head(root, n, eyebrow, title) {
    root.innerHTML = '';
    root.appendChild(h('p', 'demo-eyebrow', 'Demo ' + n + ' \u00b7 ' + eyebrow));
    root.appendChild(h('h3', 'demo-title', title));
  }
  function fail(root, e) {
    var p = h('p', 'err', 'demo error: ' + (e && e.message ? e.message : e));
    root.appendChild(p);
    if (window.console) console.error(e);
  }
  function commonPrefix(a, b) {
    var i = 0;
    while (i < a.length && i < b.length && a[i] === b[i]) i++;
    return i;
  }
  function matchedDigits(zs, gs) {               // z_k with the digits it shares with gamma_k in accent
    var i = commonPrefix(zs, gs);
    return '<b style="color:var(--accent)">' + zs.slice(0, i) + '</b>' + zs.slice(i);
  }

  /* ============================ station 5: secular ============================ */

  ZT.demos.secular = function (root) {
    try {
      head(root, 5, 'Secular function', 'From a polynomial\u2019s roots to a secular function\u2019s roots');
      var id = 'demo-secular-';
      var ctl = h('div', 'demo-controls');
      ctl.innerHTML =
        '<label for="' + id + 'N">N <select id="' + id + 'N">' +
        '<option value="4" selected>4</option><option value="6">6</option><option value="8">8</option>' +
        '</select></label>' +
        '<button class="btn" id="' + id + 'rand" type="button">Randomise (positive)</button>' +
        '<button class="btn" id="' + id + 'mixed" type="button">Randomise (mixed signs)</button>' +
        '<button class="btn" id="' + id + 'flat" type="button">All equal</button>';
      var sliders = h('div', 'demo-controls');
      sliders.id = id + 'sliders';
      sliders.style.marginTop = '-8px';
      root.appendChild(ctl);
      root.appendChild(sliders);

      var stage = h('div', 'demo-stage');
      var figG = figure('g(s) = &Sigma;<sub>j</sub> &xi;<sub>j</sub>/(j &minus; s) on [&minus;N&minus;1.5, N+1.5]. ' +
                        'Dashed lines: the poles at the integers. Dots: the 2N real roots.');
      var figM = figure('D&prime; = diag(j) &minus; (D&xi;)&eta;<sup>T</sup> and its eigenvalues (QR) against the roots of g.');
      var pairs = h('div', 'table-wrap');
      pairs.style.marginTop = '8px';
      figM.appendChild(pairs);
      stage.appendChild(figG); stage.appendChild(figM);
      root.appendChild(stage);
      var readout = h('div', 'demo-readout');
      root.appendChild(readout);
      root.appendChild(h('p', 'demo-note',
        'The roots of a polynomial become the roots of a secular function: same story, Fourier modes instead of ' +
        'powers. With all &xi;<sub>j</sub> &gt; 0 the function climbs from &minus;&infin; to +&infin; on every pole ' +
        'interval, so all 2N roots are real \u2014 that is the interlacing that positivity of the Weil form buys you. ' +
        'Try the mixed-sign button: roots leave the real line and D&prime; grows complex eigenvalues.'));

      var raw = [], N = 4;
      function defaults(n, kind) {
        var v = [], j;
        for (j = 0; j <= n; j++) {
          if (kind === 'flat') v.push(60);
          else if (kind === 'mixed') v.push(Math.round((Math.random() * 2 - 1) * 90) || 20);
          else v.push(Math.max(6, Math.round(90 * Math.exp(-j / 2) * (0.5 + Math.random()))));
        }
        return v;
      }
      function buildSliders() {
        sliders.innerHTML = '';
        raw.forEach(function (v, j) {
          var lab = document.createElement('label');
          lab.setAttribute('for', id + 'xi' + j);
          lab.innerHTML = '&xi;' + sub(j);
          var inp = document.createElement('input');
          inp.type = 'range'; inp.min = -100; inp.max = 100; inp.step = 1; inp.value = v;
          inp.id = id + 'xi' + j;
          inp.style.width = '92px';
          inp.addEventListener('input', function () { raw[j] = +inp.value; draw(); });
          lab.appendChild(inp);
          sliders.appendChild(lab);
        });
      }

      function draw() {
        var j, k;
        var sumRaw = raw[0];
        for (j = 1; j <= N; j++) sumRaw += 2 * raw[j];
        var xi = raw.map(function (v) { return sumRaw === 0 ? 0 : v / sumRaw; });
        var nnz = raw[0] !== 0 ? 1 : 0;
        for (j = 1; j <= N; j++) if (raw[j] !== 0) nnz += 2;
        var expected = Math.max(0, nnz - 1);

        var roots = sumRaw === 0 ? [] : secRoots(xi, N);
        var full = roots.map(function (r) { return -r; }).reverse().concat(roots);
        if (sumRaw !== 0 && raw[0] === 0) full = full.concat([0]).sort(function (a, b) { return a - b; });
        var ev = sumRaw === 0 ? [] : qrEigen(dPrime(xi, N));
        var evReal = ev.filter(function (e) { return Math.abs(e.im) <= 1e-7 * (1 + Math.abs(e.re)); });
        var nComplex = ev.length - evReal.length;

        /* ---- g(s) ---- */
        var S = N + 1.5, YC = 3, P = plot(470, 240, [-S, S], [-YC, YC], { l: 36, r: 10, t: 12, b: 24 });
        var xt = [], yt = [{ v: -YC, s: '\u2212' + YC }, { v: 0, s: '0' }, { v: YC, s: '+' + YC }];
        for (k = -N; k <= N; k++) if (N <= 4 || k % 2 === 0) xt.push(k);
        P.axes(xt, yt, 's', 'g(s)');
        for (k = -N; k <= N; k++) {
          P.add(el('line', { x1: P.X(k), y1: P.box.y1, x2: P.X(k), y2: P.box.y0,
                             stroke: 'var(--pole)', 'stroke-width': 1, 'stroke-dasharray': '3 3', opacity: 0.75 }));
        }
        var segs = [], cur = [];
        var steps = 1400;
        for (k = 0; k <= steps; k++) {
          var s = -S + 2 * S * k / steps;
          var nearPole = Math.abs(s - Math.round(s)) < 1e-4 && Math.abs(Math.round(s)) <= N;
          var v = nearPole ? NaN : secG(xi, N, s);
          if (!isFinite(v) || Math.abs(v) > YC) { if (cur.length > 1) segs.push(cur); cur = []; }
          else cur.push(P.X(s).toFixed(2) + ',' + P.Y(v).toFixed(2));
        }
        if (cur.length > 1) segs.push(cur);
        segs.forEach(function (sg) {
          P.add(el('polyline', { points: sg.join(' '), fill: 'none', stroke: 'var(--ink)', 'stroke-width': 1.6 }));
        });
        full.forEach(function (r) {
          if (r < -S || r > S) return;
          P.add(el('circle', { cx: P.X(r), cy: P.Y(0), r: 3.4, fill: 'var(--accent)' }));
        });
        figG.mount(P.svg);

        /* ---- D' and its spectrum ---- */
        var n = 2 * N + 1, mw = 470, cell = Math.min(34, (mw - 8) / n);
        var gridH = n * cell + 26;
        var M = dPrime(xi, N);
        var maxAbs = 0;
        M.forEach(function (r) { r.forEach(function (v) { maxAbs = Math.max(maxAbs, Math.abs(v)); }); });
        var G = el('svg', { viewBox: '0 0 ' + mw + ' ' + (gridH + 4), width: '100%',
                            preserveAspectRatio: 'xMidYMid meet' });
        var ox = (mw - n * cell) / 2;
        for (var r0 = 0; r0 < n; r0++) for (var c0 = 0; c0 < n; c0++) {
          var v2 = M[r0][c0], op = maxAbs > 0 ? Math.min(1, Math.abs(v2) / maxAbs) : 0;
          G.appendChild(el('rect', { x: ox + c0 * cell, y: 14 + r0 * cell, width: cell - 1, height: cell - 1,
                                     fill: v2 >= 0 ? 'var(--accent)' : 'var(--bad)',
                                     opacity: (0.08 + 0.72 * Math.pow(op, 0.45)).toFixed(3) }));
          if (N === 4) {
            var t2 = txt(ox + c0 * cell + cell / 2 - 0.5, 14 + r0 * cell + cell / 2 + 3,
                         Math.abs(v2) >= 100 ? v2.toFixed(0) : v2.toFixed(1),
                         { 'text-anchor': 'middle', 'font-size': 8.5, fill: 'var(--ink)' });
            G.appendChild(t2);
          }
        }
        G.appendChild(txt(ox, 10, 'rows and columns indexed by j = \u2212' + N + ' \u2026 ' + N,
                          { 'font-size': 10, fill: 'var(--ink-3)' }));
        figM.mount(G);
        figM._cap.innerHTML = 'D&prime; = diag(j) &minus; (D&xi;)&eta;<sup>T</sup>, j = &minus;' + N + '\u2026' + N +
          (N === 4 ? ' (entries shown)' : ' (shading = magnitude; numbers shown at N = 4)') +
          '. Its eigenvalues are the roots of g together with a single 0, the eigenvalue of &xi; itself.';

        /* ---- readout ---- */
        var maxRes = 0;
        roots.forEach(function (r) { maxRes = Math.max(maxRes, Math.abs(secG(xi, N, r))); });
        var evr = evReal.map(function (e) { return e.re; }).sort(function (a, b) { return a - b; });
        var zi = 0;
        for (k = 1; k < evr.length; k++) if (Math.abs(evr[k]) < Math.abs(evr[zi])) zi = k;
        var zeroEv = evr.length ? evr[zi] : NaN;
        var evrest = evr.slice(); evrest.splice(zi, 1);
        var maxDiff = 0;
        for (k = 0; k < Math.min(evrest.length, full.length); k++)
          maxDiff = Math.max(maxDiff, Math.abs(evrest[k] - full[k]));
        var okCount = full.length === expected;

        var rows = '<table><thead><tr><th>i</th><th>eigenvalue of D\u2032</th><th>root of g</th>' +
                   '<th>difference</th></tr></thead><tbody>';
        var ri = 0;
        ev.forEach(function (e2, i2) {
          var isZero = evReal.indexOf(e2) >= 0 && evr.length && e2.re === zeroEv && Math.abs(e2.im) < 1e-12;
          var cplx = Math.abs(e2.im) > 1e-7 * (1 + Math.abs(e2.re));
          var evs = cplx ? (fmt(e2.re, 4) + (e2.im > 0 ? ' + ' : ' \u2212 ') + fmt(Math.abs(e2.im), 4) + ' i')
                         : fmt(e2.re, 6);
          var rt = (!cplx && !isZero && ri < full.length) ? full[ri++] : null;
          rows += '<tr><td class="num">' + (i2 + 1) + '</td><td class="num' + (cplx ? ' bad' : '') + '">' + evs +
                  '</td><td class="num">' + (isZero ? '\u2014 (the vector \u03be)' : (rt === null ? '\u2014' : fmt(rt, 6))) +
                  '</td><td class="num">' + (rt === null ? '' : fmt(Math.abs(e2.re - rt), 3)) + '</td></tr>';
        });
        pairs.innerHTML = rows + '</tbody></table>';
        readout.innerHTML =
          '&Sigma;<sub>j</sub> (raw &xi;<sub>j</sub>) = <b>' + fmt(sumRaw, 3) + '</b> &rarr; after normalisation ' +
          '&Sigma;<sub>j</sub> &xi;<sub>j</sub> = <b>1</b> (&xi;<sub>0</sub> = ' + fmt(xi[0], 5) + ')<br>' +
          'real roots found: <b class="' + (okCount ? '' : 'bad') + '">' + full.length + '</b> of 2N = ' + (2 * N) +
          (expected !== 2 * N ? ' <span class="pole">(a zero weight removes a pole: only ' + expected + ' roots exist)</span>' : '') +
          (okCount ? '' : ' <span class="bad">\u2014 the missing ones have left the real line</span>') +
          '<br>max |g(root)| = <b>' + fmt(maxRes, 3) + '</b>' +
          ' &nbsp; eigenvalues of D&prime;: ' + evReal.length + ' real' +
          (nComplex ? ', <span class="bad">' + nComplex + ' complex</span>' : '') +
          '<br>the eigenvalue for &xi; itself: <b>' + fmt(zeroEv, 3) + '</b>' +
          ' &nbsp; max |eigenvalue &minus; root| = <b>' + fmt(maxDiff, 3) + '</b>';
      }

      function reset(kind) {
        N = +document.getElementById(id + 'N').value;
        raw = defaults(N, kind);
        buildSliders();
        draw();
      }
      document.getElementById(id + 'N').addEventListener('change', function () { reset('decay'); });
      document.getElementById(id + 'rand').addEventListener('click', function () { reset('decay'); });
      document.getElementById(id + 'mixed').addEventListener('click', function () { reset('mixed'); });
      document.getElementById(id + 'flat').addEventListener('click', function () { reset('flat'); });
      N = 4; raw = [90, 46, 25, 14, 8]; buildSliders(); draw();
    } catch (e) { fail(root, e); }
  };

  /* ============================ station 6: riemann ============================ */

  function caseOf(x, N) {
    var R = window.ZT_RIEMANN;
    if (!R) return null;
    for (var i = 0; i < R.cases.length; i++) if (R.cases[i].x === x && R.cases[i].N === N) return R.cases[i];
    return null;
  }

  ZT.demos.riemann = function (root) {
    try {
      head(root, 6, 'Riemann', 'The Riemann zeros recovered from primes up to 13');
      var R = window.ZT_RIEMANN;
      if (!R) throw new Error('riemann-data.js is not loaded');
      var id = 'demo-riemann-';
      var opts = R.cases.map(function (c) {
        return '<option value="' + c.x + ',' + c.N + '"' + (c.x === 13 && c.N === 20 ? ' selected' : '') + '>' +
               'x = ' + c.x + ', N = ' + c.N + '</option>';
      }).join('');
      var ctl = h('div', 'demo-controls');
      ctl.innerHTML = '<label for="' + id + 'case">window and truncation <select id="' + id + 'case">' +
                      opts + '</select></label>' +
                      '<span style="color:var(--ink-3)">x = &lambda;<sup>2</sup>, primes p &le; x, L = log x</span>';
      root.appendChild(ctl);

      var stage = h('div', 'demo-stage');
      var figXi = figure('');
      var figLine = figure('');
      var figConv = figure('');
      stage.appendChild(figXi); stage.appendChild(figLine); stage.appendChild(figConv);
      root.appendChild(stage);
      var readout = h('div', 'demo-readout');
      root.appendChild(readout);
      var tw = h('div', 'table-wrap');
      root.appendChild(tw);
      root.appendChild(h('p', 'demo-note',
        'Nothing here is fitted to the zeros: the matrix is built from the prime powers k &le; x and the ' +
        'archimedean factor alone. The zeros are what its minimal eigenvector says they are; the ' +
        'coloured digits are the ones that happen to be right.'));

      function drawXi(c) {
        var lo = Math.min.apply(null, c.xiLog10Abs), hi = Math.max.apply(null, c.xiLog10Abs);
        lo = Math.floor(lo) - 0.5; hi = Math.ceil(hi) + 0.5;
        var P = plot(470, 210, [-0.8, c.N + 0.8], [lo, hi], { l: 40, r: 8, t: 12, b: 24 });
        var yt = [], step = Math.ceil((hi - lo) / 6);
        for (var v = Math.ceil(lo); v <= hi; v += step) yt.push(v);
        var xt = [];
        for (var j = 0; j <= c.N; j += (c.N > 20 ? 8 : 4)) xt.push(j);
        P.axes(xt, yt, 'j', 'log\u2081\u2080|\u03be\u2c7c|');
        var bw = Math.max(2, (P.box.x1 - P.box.x0) / (c.N + 2) - 1.5);
        c.xiLog10Abs.forEach(function (v2, j2) {
          var y = P.Y(v2);
          P.add(el('rect', { x: P.X(j2) - bw / 2, y: y, width: bw, height: Math.max(0.5, P.box.y0 - y),
                             fill: c.xiSign[j2] >= 0 ? 'var(--accent)' : 'var(--bad)' }));
        });
        figXi.mount(P.svg);
        figXi._cap.innerHTML = 'The minimal eigenvector &xi;<sub>0</sub>&hellip;&xi;<sub>N</sub> on a log scale ' +
          '(<span style="color:var(--accent)">positive</span>, <span style="color:var(--bad)">negative</span>). ' +
          'It spans ' + Math.round(Math.max.apply(null, c.xiLog10Abs) - Math.min.apply(null, c.xiLog10Abs)) +
          ' orders of magnitude, yet &Sigma;<sub>j</sub> &xi;<sub>j</sub> = 1.';
      }

      function drawLine(c) {
        var P = plot(470, 120, [0, 60], [0, 1], { l: 10, r: 10, t: 26, b: 26 });
        var xt = [];
        for (var v = 0; v <= 60; v += 10) xt.push(v);
        P.axes(xt, [], 'z', null);
        var y = P.box.y0;
        R.zeros.forEach(function (g2) {
          if (g2 > 60) return;
          P.add(el('circle', { cx: P.X(g2), cy: y - 14, r: 5, fill: 'none', stroke: 'var(--ink-2)', 'stroke-width': 1.3 }));
        });
        c.zk.forEach(function (z, k) {
          if (z > 60) return;
          P.add(el('circle', { cx: P.X(z), cy: y - 14, r: 2.6, fill: 'var(--accent)' }));
          void k;
        });
        P.add(txt(P.box.x0, 14, 'hollow: true zeros \u03b3\u2096   solid: recovered z\u2096',
                  { 'font-size': 10, fill: 'var(--ink-3)' }));
        figLine.mount(P.svg);
        var inrange = c.zk.filter(function (z) { return z <= 60; }).length;
        figLine._cap.innerHTML = 'The first ' + inrange + ' recovered eigenvalues sitting on the zeros. ' +
          'The dots leave the ticks only where the window runs out of resolution.';
      }

      function slope(pts) {                       // least squares of log10err against x
        var n = pts.length, sx = 0, sy = 0, sxx = 0, sxy = 0;
        pts.forEach(function (p) { sx += p.x; sy += p.log10err; sxx += p.x * p.x; sxy += p.x * p.log10err; });
        return (n * sxy - sx * sy) / (n * sxx - sx * sx);
      }

      function drawConv(c) {
        var law = R.firstZeroLaw;
        var xs = law.map(function (p) { return p.x; }), ys = law.map(function (p) { return p.log10err; });
        var P = plot(470, 210, [Math.min.apply(null, xs) - 2, Math.max.apply(null, xs) + 2],
                     [Math.min.apply(null, ys) - 6, Math.max.apply(null, ys) + 6], { l: 44, r: 10, t: 12, b: 24 });
        var yt = [], lo = Math.ceil((Math.min.apply(null, ys) - 6) / 20) * 20;
        for (var v = lo; v <= Math.max.apply(null, ys) + 6; v += 20) yt.push(v);
        P.axes(xs.filter(function (v2, i) { return xs.indexOf(v2) === i; }), yt, 'x = \u03bb\u00b2', 'log\u2081\u2080 |z\u2081 \u2212 \u03b3\u2081|');
        [20, 40].forEach(function (Nv) {
          var pts = law.filter(function (p) { return p.N === Nv; }).sort(function (a, b) { return a.x - b.x; });
          P.add(el('polyline', { points: pts.map(function (p) { return P.X(p.x) + ',' + P.Y(p.log10err); }).join(' '),
                                 fill: 'none', stroke: 'var(--ink-2)', 'stroke-width': 1,
                                 'stroke-dasharray': Nv === 20 ? '4 3' : null }));
          pts.forEach(function (p) {
            var on = p.x === c.x && p.N === c.N;
            P.add(el('circle', { cx: P.X(p.x), cy: P.Y(p.log10err), r: on ? 5 : 3.2,
                                 fill: Nv === 40 ? 'var(--accent)' : 'none',
                                 stroke: 'var(--accent)', 'stroke-width': 1.4 }));
          });
          if (pts.length) P.add(txt(P.X(pts[pts.length - 1].x) - 4, P.Y(pts[pts.length - 1].log10err) - 9,
                                    'N = ' + Nv, { 'text-anchor': 'end', 'font-size': 10, fill: 'var(--ink-2)' }));
        });
        figConv.mount(P.svg);
        var s20 = slope(law.filter(function (p) { return p.N === 20; }));
        var s40 = slope(law.filter(function (p) { return p.N === 40; }));
        var near = law.filter(function (p) { return p.N === 40 && p.x <= 13; });
        var sNear = slope(near);
        figConv._cap.innerHTML = 'Accuracy of the first zero against the window. Fitted slope over x = 9\u202630: ' +
          '<b class="num">' + Math.abs(s20).toFixed(2) + '</b> digits per unit x at N = 20, ' +
          '<b class="num">' + Math.abs(s40).toFixed(2) + '</b> at N = 40 (' + Math.abs(sNear).toFixed(1) +
          ' over x = 9\u202613, where N is not yet the bottleneck). At N = 120 the prototype gives the ' +
          'asymptotic 5.5 digits per unit x: here the truncation N caps the gain, not the primes.';
      }

      function drawTable(c) {
        var rows = Math.min(20, c.N), i;
        var html = '<table><thead><tr><th>k</th><th>z\u2096 = 2&pi;s\u2096/L</th><th>\u03b3\u2096</th>' +
                   '<th>|z\u2096 \u2212 \u03b3\u2096|</th></tr></thead><tbody>';
        for (i = 0; i < rows; i++) {
          var zs = c.zkStr[i].slice(0, 24), gs = (R.zerosStr[i] || '').slice(0, 24);
          html += '<tr><td class="num">' + (i + 1) + '</td><td class="num">' + matchedDigits(zs, gs) +
                  '</td><td class="num" style="color:var(--ink-3)">' + gs + '</td><td class="num">' +
                  c.err[i].toExponential(2) + '</td></tr>';
        }
        tw.innerHTML = html + '</tbody></table>';
      }

      function update() {
        var v = document.getElementById(id + 'case').value.split(',');
        var c = caseOf(+v[0], +v[1]);
        if (!c) throw new Error('no data for x = ' + v[0] + ', N = ' + v[1]);
        drawXi(c); drawLine(c); drawConv(c); drawTable(c);
        var agree = 0;
        for (var i = 0; i < c.N; i++) if (c.err[i] < 1e-9) agree++;
        readout.innerHTML =
          'x = <b>' + c.x + '</b> (prime powers k &le; ' + c.x + ': ' +
          (c.x === 13 ? '2, 3, 4, 5, 7, 8, 9, 11, 13' : 'all k &le; ' + c.x) + ')' +
          ' &nbsp; L = log x = <b class="num">' + c.L.toFixed(8) + '</b>' +
          ' &nbsp; N = <b>' + c.N + '</b> (' + (2 * c.N + 1) + ' Fourier modes)<br>' +
          '&epsilon;<sub>N</sub> = min spec E = <b class="num">' + c.epsStr + '</b>' +
          ' &nbsp; next even eigenvalue ' + c.evenNext + ', smallest odd ' + c.oddMin +
          ' <span style="color:var(--ink-3)">(even-simple holds)</span><br>' +
          'secular roots found: <b>' + c.nroots + '</b> of N = ' + c.N +
          ' &nbsp; first zero to <b class="num">' + c.err[0].toExponential(2) + '</b>' +
          ' &nbsp; zeros reproduced to 9 digits or better: <b>' + agree + '</b><br>' +
          '<span style="color:var(--ink-3)">computed with mpmath at ' + c.dps +
          ' digits; x = 13, N = 20 agrees with the certified arb run to every printed digit.</span>';
      }
      onChange([document.getElementById(id + 'case')], update);
      update();
    } catch (e) { fail(root, e); }
  };

  /* ============================ station 7: algorithm ============================ */

  ZT.demos.algorithm = function (root) {
    try {
      head(root, 7, 'The algorithm', 'The whole algorithm, side by side');
      var id = 'demo-algorithm-';
      var R = window.ZT_RIEMANN, c13 = caseOf(13, 20);
      var ctl = h('div', 'demo-controls');
      ctl.innerHTML = '<button class="btn primary" id="' + id + 'run" type="button">Run</button>' +
        '<label for="' + id + 'perm">permutation <input type="text" id="' + id + 'perm" value="(1 2)(3 4 5)" size="12"></label>' +
        '<span style="color:var(--ink-3)">left: 5 points, right: &zeta;, x = 13</span>';
      root.appendChild(ctl);
      var steps = h('div');
      steps.style.cssText = 'display:flex;flex-direction:column;gap:12px';
      root.appendChild(steps);
      var readout = h('div', 'demo-readout');
      root.appendChild(readout);
      root.appendChild(h('p', 'demo-note',
        'The two columns are the same five steps. Only the input distribution differs: fixed-point counts of ' +
        '&sigma;<sup>k</sup> on the left, the von Mangoldt weights of the prime powers in the window plus the ' +
        'archimedean term on the right.'));

      var titles = ['Counts in the window', 'Weil form matrix', 'Positivity: \u03b5',
                    'Minimal eigenvector', 'Roots = spectrum'];
      var panels = [];
      titles.forEach(function (t, i) {
        var box = h('div');
        box.id = id + 'step' + (i + 1);
        box.style.cssText = 'border:1px solid var(--rule);border-radius:var(--radius);padding:8px 10px 6px';
        box.appendChild(h('p', 'demo-eyebrow', 'Step ' + (i + 1) + ' \u00b7 ' + t));
        var grid = h('div');
        grid.style.cssText = 'display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px';
        var left = h('div'), right = h('div');
        [[left, 'permutation (1 2)(3 4 5)'], [right, 'Riemann zeta, x = 13']].forEach(function (p) {
          var lab = h('div', null, p[1]);
          lab.style.cssText = 'font:500 12px var(--font-mono);color:var(--ink-3);margin-bottom:4px';
          p[0].appendChild(lab);
        });
        grid.appendChild(left); grid.appendChild(right);
        box.appendChild(grid);
        steps.appendChild(box);
        panels.push({ box: box, left: left, right: right });
      });
      function cell(p, side, node) {
        var host = p[side];
        while (host.childNodes.length > 1) host.removeChild(host.lastChild);
        host.appendChild(node);
      }
      function mini(caption, svg) {
        var f = figure(caption);
        f.mount(svg);
        f.style.margin = '0';
        return f;
      }

      function build() {
        var permStr = document.getElementById(id + 'perm').value || '(1 2)(3 4 5)';
        var n = 5, m;
        for (m = 1; m <= 12; m++) if (new RegExp('\\b' + m + '\\b').test(permStr)) n = Math.max(n, m);
        var perm = permOf(permStr, n);
        var counts = countsOf(perm, 12);
        var distinct = {}, cyc = [], seen = new Array(n).fill(false);
        for (var i0 = 0; i0 < n; i0++) {
          if (seen[i0]) continue;
          var len = 0, j0 = i0;
          do { seen[j0] = true; j0 = perm[j0]; len++; } while (j0 !== i0);
          cyc.push(len);
          for (var q = 0; q < len; q++) distinct[Math.round(1e9 * ((q / len) % 1)) / 1e9] = 1;
        }
        var nDistinct = Object.keys(distinct).length;
        var Mcrit = nDistinct;
        var T = toeplitzOf(counts, Mcrit);
        var eT = symEig(T);
        var kern = eT.vectors.map(function (r) { return r[0]; });
        var big = 0;
        kern.forEach(function (v) { if (Math.abs(v) > Math.abs(big)) big = v; });
        if (big !== 0) kern = kern.map(function (v) { return v / big; });
        var proots = polyRoots(kern);
        var trueEv = [];
        cyc.forEach(function (len, ci) {
          for (var q = 0; q < len; q++) trueEv.push({ re: Math.cos(2 * Math.PI * q / len), im: Math.sin(2 * Math.PI * q / len), c: ci });
        });

        /* ---- step 1: counts ---- */
        var P1 = plot(300, 150, [-0.6, 12.6], [0, Math.max.apply(null, counts.slice(1, 13)) + 1], { l: 34, r: 8, t: 10, b: 22 });
        P1.axes([1, 3, 6, 9, 12], [0, n], 'k', '#Fix(\u03c3\u1d4f)');
        for (var k1 = 1; k1 <= 12; k1++) {
          P1.add(el('rect', { x: P1.X(k1) - 6, y: P1.Y(counts[k1]), width: 12,
                              height: Math.max(0.6, P1.box.y0 - P1.Y(counts[k1])), fill: 'var(--accent)' }));
        }
        cell(panels[0], 'left', mini('N\u2096 = #Fix(\u03c3\u1d4f) = ' + counts.slice(1, 7).join(', ') + ', \u2026', P1.svg));

        var atoms = R ? R.window13.atoms : [];
        var Lw = R ? R.window13.L : Math.log(13);
        var P2 = plot(300, 160, [0, Lw * 1.04], [-0.95, 0.12], { l: 36, r: 10, t: 10, b: 22 });
        P2.axes([{ v: 0, s: '0' }, { v: Lw, s: 'L' }], [{ v: 0, s: '0' }, { v: -0.5, s: '\u22120.5' }],
                'log k', '\u2212\u039b(k)k^{\u22121/2}');
        atoms.forEach(function (a, ai) {
          P2.add(el('line', { x1: P2.X(a.logk), y1: P2.Y(0), x2: P2.X(a.logk), y2: P2.Y(a.weight),
                              stroke: 'var(--accent)', 'stroke-width': 2 }));
          P2.add(el('circle', { cx: P2.X(a.logk), cy: P2.Y(a.weight), r: 2.4, fill: 'var(--accent)' }));
          P2.add(txt(P2.X(a.logk), P2.Y(a.weight) + (ai % 2 ? 13 : -6), String(a.k),
                     { 'text-anchor': 'middle', 'font-size': 9, fill: 'var(--ink-3)' }));
        });
        cell(panels[0], 'right', mini('The ' + atoms.length + ' prime powers k \u2264 13, at position log k with weight ' +
          '\u2212\u039b(k)k<sup>\u22121/2</sup>. The last one sits exactly on the edge: log 13 = L.', P2.svg));

        /* ---- step 2: the matrices ---- */
        var nT = T.length, cw = Math.min(34, 280 / nT);
        var G1 = el('svg', { viewBox: '0 0 300 ' + (nT * cw + 6), width: '100%', preserveAspectRatio: 'xMidYMid meet' });
        var maxT = 0;
        T.forEach(function (r) { r.forEach(function (v) { maxT = Math.max(maxT, Math.abs(v)); }); });
        for (var r1 = 0; r1 < nT; r1++) for (var c1 = 0; c1 < nT; c1++) {
          G1.appendChild(el('rect', { x: 4 + c1 * cw, y: 3 + r1 * cw, width: cw - 1.5, height: cw - 1.5,
                                      fill: 'var(--accent)', opacity: (0.08 + 0.7 * T[r1][c1] / (maxT || 1)).toFixed(3) }));
          G1.appendChild(txt(4 + c1 * cw + cw / 2, 3 + r1 * cw + cw / 2 + 3.5, String(T[r1][c1]),
                             { 'text-anchor': 'middle', 'font-size': 10, fill: 'var(--ink)' }));
        }
        cell(panels[1], 'left', mini('T\u2c7c\u2096 = N<sub>|j\u2212k|</sub>, j,k = 0\u2026M with M = ' + Mcrit +
          ' (the critical window: as many counts as distinct eigenvalues).', G1));

        var E = c13 ? c13.E : null;
        var G2 = el('svg', { viewBox: '0 0 300 300', width: '100%', preserveAspectRatio: 'xMidYMid meet' });
        if (E) {
          var nE = E.length, ce = 290 / nE, maxE = 0;
          E.forEach(function (r) { r.forEach(function (v) { maxE = Math.max(maxE, Math.abs(v)); }); });
          for (var r2 = 0; r2 < nE; r2++) for (var c2 = 0; c2 < nE; c2++) {
            var v3 = E[r2][c2];
            G2.appendChild(el('rect', { x: 5 + c2 * ce, y: 5 + r2 * ce, width: ce, height: ce,
                                        fill: v3 >= 0 ? 'var(--accent)' : 'var(--bad)',
                                        opacity: (0.06 + 0.8 * Math.pow(Math.abs(v3) / maxE, 0.4)).toFixed(3) }));
          }
        }
        cell(panels[1], 'right', mini('The even block E of the Loewner matrix &tau;<sub>nm</sub> = ' +
          '(b<sub>n</sub> \u2212 b<sub>m</sub>)/(n \u2212 m), 21 \u00d7 21 at N = 20 ' +
          '(<span style="color:var(--accent)">+</span>, <span style="color:var(--bad)">\u2212</span>).', G2));

        /* ---- step 3: positivity ---- */
        var minT = eT.values[0];
        var l3 = h('div', 'demo-readout');
        l3.style.margin = '0';
        l3.innerHTML = 'min spec T = <b>' + (Math.abs(minT) < 1e-10 ? '0' : fmt(minT, 4)) + '</b>' +
          (Math.abs(minT) < 1e-10 ? ' <span style="color:var(--ink-3)">(' + minT.toExponential(1) + ', i.e. zero to machine precision)</span>' : '') +
          '<br>at M = ' + (Mcrit - 1) + ' it was still ' + fmt(symEig(toeplitzOf(counts, Mcrit - 1)).values[0], 4) +
          '<br><span style="color:var(--ink-3)">positive semidefinite, with a kernel exactly at the critical window</span>';
        cell(panels[2], 'left', l3);
        var r3 = h('div', 'demo-readout');
        r3.style.margin = '0';
        r3.innerHTML = c13 ? ('&epsilon;<sub>N</sub> = min spec E = <b>' + c13.epsStr + '</b>' +
          '<br>next even ' + c13.evenNext + ', smallest odd ' + c13.oddMin +
          '<br><span style="color:var(--ink-3)">positive, but only just: the Weil form is ' +
          'almost singular on this window \u2014 that near-kernel is the zeros</span>') : 'no data';
        cell(panels[2], 'right', r3);

        /* ---- step 4: minimal eigenvector ---- */
        var P4 = plot(300, 140, [-0.6, kern.length - 0.4], [-1.2, 1.2], { l: 34, r: 8, t: 10, b: 22 });
        P4.axes(kern.map(function (v, i2) { return i2; }), [{ v: -1, s: '\u22121' }, { v: 0, s: '0' }, { v: 1, s: '1' }],
                'j', '\u03be\u2c7c');
        kern.forEach(function (v, i2) {
          P4.add(el('rect', { x: P4.X(i2) - 7, y: Math.min(P4.Y(0), P4.Y(v)), width: 14,
                              height: Math.max(0.8, Math.abs(P4.Y(v) - P4.Y(0))),
                              fill: v >= 0 ? 'var(--accent)' : 'var(--bad)' }));
        });
        cell(panels[3], 'left', mini('The kernel vector, normalised: &xi; = (' +
          kern.map(function (v) { return (Math.abs(v) < 1e-9 ? 0 : v).toFixed(2).replace(/\.00$/, ''); }).join(', ') +
          '). Its entries are the coefficients of &xi;(u) = &Sigma;<sub>j</sub> &xi;<sub>j</sub>u<sup>j</sup>.', P4.svg));

        if (c13) {
          var lo4 = Math.min.apply(null, c13.xiLog10Abs) - 0.5, hi4 = Math.max.apply(null, c13.xiLog10Abs) + 0.5;
          var P5 = plot(300, 140, [-0.8, c13.N + 0.8], [lo4, hi4], { l: 38, r: 8, t: 10, b: 22 });
          P5.axes([0, 5, 10, 15, 20], [Math.ceil(lo4), Math.round((lo4 + hi4) / 2), Math.floor(hi4)],
                  'j', 'log\u2081\u2080|\u03be\u2c7c|');
          c13.xiLog10Abs.forEach(function (v4, j4) {
            P5.add(el('rect', { x: P5.X(j4) - 4, y: P5.Y(v4), width: 8,
                                height: Math.max(0.6, P5.box.y0 - P5.Y(v4)),
                                fill: c13.xiSign[j4] >= 0 ? 'var(--accent)' : 'var(--bad)' }));
          });
          cell(panels[3], 'right', mini('&xi;<sub>0</sub>&hellip;&xi;<sub>20</sub> of the Loewner matrix, log scale, ' +
            'signs in colour. &xi;<sub>0</sub> &asymp; 2.17&middot;10<sup>18</sup> while &Sigma;<sub>j</sub>&xi;<sub>j</sub> = 1.', P5.svg));
        }

        /* ---- step 5: roots ---- */
        var Pc = plot(240, 240, [-1.35, 1.35], [-1.35, 1.35], { l: 8, r: 8, t: 8, b: 8 });
        Pc.svg.style.maxWidth = '250px';
        Pc.add(el('circle', { cx: Pc.X(0), cy: Pc.Y(0), r: Math.abs(Pc.X(1) - Pc.X(0)),
                              fill: 'none', stroke: 'var(--rule)' }));
        Pc.add(el('line', { x1: Pc.X(-1.3), y1: Pc.Y(0), x2: Pc.X(1.3), y2: Pc.Y(0), stroke: 'var(--bg-3)' }));
        Pc.add(el('line', { x1: Pc.X(0), y1: Pc.Y(-1.3), x2: Pc.X(0), y2: Pc.Y(1.3), stroke: 'var(--bg-3)' }));
        trueEv.forEach(function (e2) {
          Pc.add(el('circle', { cx: Pc.X(e2.re), cy: Pc.Y(e2.im), r: 6.5, fill: 'none',
                                stroke: 'var(--ink-2)', 'stroke-width': 1.3 }));
        });
        proots.forEach(function (e2) {
          Pc.add(el('circle', { cx: Pc.X(e2.re), cy: Pc.Y(e2.im), r: 3, fill: 'var(--accent)' }));
        });
        var maxOff = 0;
        proots.forEach(function (e2) { maxOff = Math.max(maxOff, Math.abs(Math.hypot(e2.re, e2.im) - 1)); });
        cell(panels[4], 'left', mini('The ' + proots.length + ' roots of &xi;(u) (solid) on the unit circle, ' +
          'against the ' + nDistinct + ' distinct eigenvalues of the permutation matrix (hollow). ' +
          'max ||root| \u2212 1| = ' + maxOff.toExponential(1) + '.', Pc.svg));

        if (c13) {
          var t5 = h('div', 'demo-readout');
          t5.style.margin = '0';
          var rows = '';
          for (var i5 = 0; i5 < 5; i5++) {
            var zs = c13.zkStr[i5].slice(0, 22), gs = (R.zerosStr[i5] || '').slice(0, 22);
            rows += 'z' + sub(i5 + 1) + ' = ' + matchedDigits(zs, gs) +
                    ' <span style="color:var(--ink-3)">(' + c13.err[i5].toExponential(1) + ')</span><br>';
          }
          t5.innerHTML = rows + '<span style="color:var(--ink-3)">z\u2096 = 2&pi;s\u2096/L, s\u2096 the roots of ' +
            'g(s) = &Sigma;<sub>j</sub>&xi;<sub>j</sub>/(j\u2212s); coloured digits agree with \u03b3\u2096</span>';
          cell(panels[4], 'right', t5);
        }

        readout.innerHTML =
          'left: ' + n + ' points, cycle type (' + cyc.join(', ') + '), ' + nDistinct +
          ' distinct eigenvalues, critical window M = ' + Mcrit +
          ', &xi;(u) = ' + polyLabel(kern) + '<br>' +
          'right: 2N+1 = 41 Fourier modes on [1/\u221a13, \u221a13], 9 prime powers, ' +
          '&epsilon;<sub>N</sub> = ' + (c13 ? c13.epsStr : '?') + ', 20 roots, first zero to ' +
          (c13 ? c13.err[0].toExponential(2) : '?') + '<br>' +
          '<span style="color:var(--ink-3)">same five steps, same theorem: the minimal eigenvector of a ' +
          'positive-semidefinite form built from counts has the spectrum as its roots.</span>';
      }

      function polyLabel(k) {                     // pretty-print a small integer-ish coefficient vector
        var s = '', any = false;
        k.forEach(function (v, j) {
          var r = Math.round(v);
          if (Math.abs(v - r) > 1e-6 || r === 0) { if (Math.abs(v) > 1e-6) { s += (v > 0 && any ? ' + ' : ' ') + v.toFixed(2) + (j ? 'u' + (j > 1 ? sup(j) : '') : ''); any = true; } return; }
          s += (r > 0 ? (any ? ' + ' : '') : (any ? ' \u2212 ' : '\u2212')) + (Math.abs(r) === 1 && j ? '' : Math.abs(r)) +
               (j ? 'u' + (j > 1 ? sup(j) : '') : '');
          any = true;
        });
        return s.trim();
      }
      function sup(j) {
        var S = ['\u2070', '\u00b9', '\u00b2', '\u00b3', '\u2074', '\u2075', '\u2076', '\u2077', '\u2078', '\u2079'];
        return String(j).split('').map(function (d) { return S[+d]; }).join('');
      }

      function highlight(i) {
        panels.forEach(function (p, k) {
          p.box.style.outline = (i < 0 || k === i) ? (i < 0 ? 'none' : '2px solid var(--accent)') : 'none';
          p.box.style.background = (i >= 0 && k === i) ? 'var(--bg-2)' : 'transparent';
          p.box.style.opacity = (i < 0 || k <= i) ? '1' : '0.45';
        });
      }
      var timer = null;
      function run() {
        if (timer) { clearTimeout(timer); timer = null; }
        if (reducedMotion()) { highlight(-1); return; }
        var i = 0;
        highlight(0);
        (function step() {
          timer = setTimeout(function () {
            i++;
            if (i >= panels.length) { highlight(-1); timer = null; return; }
            highlight(i);
            step();
          }, 1100);
        })();
      }
      document.getElementById(id + 'run').addEventListener('click', run);
      document.getElementById(id + 'perm').addEventListener('change', function () { build(); highlight(-1); });
      build();
      highlight(-1);
    } catch (e) { fail(root, e); }
  };

  /* If core.js (and its mountAll) is missing, still mount these three demos. */
  document.addEventListener('DOMContentLoaded', function () {
    if (typeof ZT.mountAll === 'function') return;
    ['secular', 'riemann', 'algorithm'].forEach(function (name) {
      var r = document.getElementById('demo-' + name);
      if (r && r.childElementCount === 0) ZT.demos[name](r);
    });
  });
})();
