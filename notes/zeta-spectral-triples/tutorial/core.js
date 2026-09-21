/* core.js — "Zeros From Counts": numerics + drawing helpers.  Global: window.ZT.
   Worker A.  Plain ES2020, no modules, no libraries.  Colours only via CSS custom
   properties of theme.css.  Safe to load under node (nothing touches `document`
   at load time), which is how the numerics are unit-tested. */
(function (global) {
  'use strict';

  var ZT = global.ZT = global.ZT || {};
  ZT.demos = ZT.demos || {};

  /* ===================================================================== */
  /*  permutations                                                          */
  /* ===================================================================== */

  /* "(1 2)(3 4 5)" on n points -> 0-based array perm[i] = sigma(i).
     1-based input, letters not mentioned are fixed points. */
  function parseCycles(str, n) {
    n = Math.round(Number(n));
    if (!(n >= 1 && n <= 64)) throw new Error('n must be a whole number between 1 and 64');
    var perm = [], i;
    for (i = 0; i < n; i++) perm[i] = i;
    var s = String(str == null ? '' : str).trim();
    if (s === '' || s === 'e' || s === 'id' || s === '1') return perm;
    if (!/^[()\d\s,]+$/.test(s))
      throw new Error('only digits, spaces, commas and parentheses are allowed');
    var stripped = s.replace(/\s+/g, '');
    if (!/^(\([^()]*\))+$/.test(stripped))
      throw new Error('write cycles as (1 2)(3 4 5) — each ( must be closed before the next one opens');
    var seen = {}, re = /\(([^()]*)\)/g, m;
    while ((m = re.exec(s)) !== null) {
      var body = m[1].trim();
      if (body === '') continue;
      var toks = body.split(/[\s,]+/), pts = [], t, v;
      for (i = 0; i < toks.length; i++) {
        t = toks[i];
        if (!/^\d+$/.test(t)) throw new Error('"' + t + '" is not a whole number');
        v = parseInt(t, 10);
        if (v < 1 || v > n) throw new Error('the point ' + v + ' is outside the range 1…' + n);
        if (seen[v]) throw new Error('the point ' + v + ' appears in two cycles');
        seen[v] = 1;
        pts.push(v - 1);
      }
      for (i = 0; i < pts.length; i++) perm[pts[i]] = pts[(i + 1) % pts.length];
    }
    return perm;
  }

  function permPower(perm, k) {
    var n = perm.length, out = [], i, j;
    k = Math.max(0, Math.round(k));
    for (i = 0; i < n; i++) { j = i; for (var c = 0; c < k; c++) j = perm[j]; out[i] = j; }
    return out;
  }

  function fixedPoints(perm) {
    var out = [];
    for (var i = 0; i < perm.length; i++) if (perm[i] === i) out.push(i);
    return out;
  }

  /* N_k = #Fix(sigma^k) for k = 1..K */
  function countsOf(perm, K) {
    var out = [], p = perm.slice(), i, c;
    for (var k = 1; k <= K; k++) {
      c = 0;
      for (i = 0; i < p.length; i++) if (p[i] === i) c++;
      out.push(c);
      if (k < K) { var q = []; for (i = 0; i < p.length; i++) q[i] = perm[p[i]]; p = q; }
    }
    return out;
  }

  /* cycles as arrays of 0-based points, in order of smallest element */
  function cyclesOf(perm) {
    var n = perm.length, seen = new Array(n).fill(false), out = [], i, j, c;
    for (i = 0; i < n; i++) {
      if (seen[i]) continue;
      c = []; j = i;
      do { seen[j] = true; c.push(j); j = perm[j]; } while (j !== i);
      out.push(c);
    }
    return out;
  }

  /* multiset of cycle lengths, descending */
  function cycleType(perm) {
    return cyclesOf(perm).map(function (c) { return c.length; })
      .sort(function (a, b) { return b - a; });
  }

  /* every l-th root of unity, once per cycle of length l */
  function eigenvaluesOfPerm(perm) {
    var cyc = cyclesOf(perm), out = [];
    for (var c = 0; c < cyc.length; c++) {
      var l = cyc[c].length;
      for (var j = 0; j < l; j++) {
        var th = 2 * Math.PI * j / l;
        out.push({ re: Math.cos(th), im: Math.sin(th), cycleIndex: c, cycleLength: l, k: j });
      }
    }
    return out;
  }

  /* distinct points of a complex multiset, with multiplicities */
  function distinctEigs(eigs, tol) {
    tol = tol || 1e-9;
    var out = [];
    for (var i = 0; i < eigs.length; i++) {
      var e = eigs[i], hit = null;
      for (var j = 0; j < out.length; j++)
        if (Math.abs(out[j].re - e.re) < tol && Math.abs(out[j].im - e.im) < tol) { hit = out[j]; break; }
      if (hit) hit.mult++;
      else out.push({ re: e.re, im: e.im, mult: 1 });
    }
    return out;
  }

  /* N_k = sum_lambda lambda^k, k = 1..K (imaginary parts cancel for a conjugate-closed set) */
  function powerSums(eigs, K) {
    var out = [], k, i, re, im, r, th;
    for (k = 1; k <= K; k++) {
      re = 0; im = 0;
      for (i = 0; i < eigs.length; i++) {
        r = Math.pow(Math.hypot(eigs[i].re, eigs[i].im), k);
        th = k * Math.atan2(eigs[i].im, eigs[i].re);
        re += r * Math.cos(th); im += r * Math.sin(th);
      }
      out.push(re);
    }
    return out;
  }

  /* ===================================================================== */
  /*  series and Newton's identities                                        */
  /* ===================================================================== */

  /* Newton: from the power sums N_1..N_M (M <= n) the elementary symmetric e_1..e_M,
     returned as the coefficient array of prod_lambda (1 - lambda u) = sum (-1)^j e_j u^j,
     i.e. [1, -e_1, e_2, -e_3, ...].  For M < n this is the truncated recovery. */
  function newtonToPoly(counts, n) {
    var M = counts.length;
    if (n != null) M = Math.min(M, Math.max(0, Math.round(n)));
    var e = [1], k, i, s;
    for (k = 1; k <= M; k++) {
      s = 0;
      for (i = 1; i <= k; i++) s += (i % 2 === 1 ? 1 : -1) * e[k - i] * counts[i - 1];
      e[k] = s / k;
    }
    var c = [];
    for (k = 0; k <= M; k++) c[k] = (k % 2 === 0 ? 1 : -1) * e[k];
    return c;
  }

  /* Taylor coefficients c_0..c_K of exp(sum_{k>=1} N_k u^k / k) */
  function zetaTaylor(counts, K) {
    var c = [1], k, j, s;
    for (k = 1; k <= K; k++) {
      s = 0;
      for (j = 1; j <= k; j++) s += (counts[j - 1] || 0) * c[k - j];
      c[k] = s / k;
    }
    return c;
  }

  /* Taylor coefficients c_0..c_K of prod_l 1/(1 - u^l) */
  function zetaProductTaylor(cycleLengths, K) {
    var a = new Array(K + 1).fill(0), i, t;
    a[0] = 1;
    for (t = 0; t < cycleLengths.length; t++) {
      var l = cycleLengths[t];
      for (i = l; i <= K; i++) a[i] += a[i - l];
    }
    return a;
  }

  /* ===================================================================== */
  /*  linear algebra                                                        */
  /* ===================================================================== */

  /* Hermitian (real symmetric) Weil/Toeplitz form, (M+1)x(M+1), T[j][k] = N_{|j-k|}. */
  function toeplitz(counts, M, N0) {
    if (N0 == null) N0 = Math.max.apply(null, counts.map(function (x) { return x; }));
    var T = [], j, k, d;
    for (j = 0; j <= M; j++) {
      T[j] = [];
      for (k = 0; k <= M; k++) {
        d = Math.abs(j - k);
        T[j][k] = d === 0 ? N0 : (counts[d - 1] !== undefined ? counts[d - 1] : 0);
      }
    }
    return T;
  }

  function jrot(a, s, tau, i, j, k, l) {
    var g = a[i][j], h = a[k][l];
    a[i][j] = g - s * (h + g * tau);
    a[k][l] = h + s * (g - h * tau);
  }

  /* cyclic Jacobi for real symmetric matrices (robust for tiny eigenvalues).
     Returns {values: ascending, vectors: V with V[i][j] = i-th entry of the j-th
     eigenvector (eigenvectors are the COLUMNS)}. */
  function symEig(Ain) {
    var n = Ain.length, i, j, ip, iq;
    var a = Ain.map(function (r) { return r.slice(); });
    var v = [];
    for (i = 0; i < n; i++) { v[i] = new Array(n).fill(0); v[i][i] = 1; }
    var b = [], z = [], d = [];
    for (i = 0; i < n; i++) { b[i] = d[i] = a[i][i]; z[i] = 0; }
    for (var sweep = 1; sweep <= 100; sweep++) {
      var sm = 0;
      for (ip = 0; ip < n - 1; ip++) for (iq = ip + 1; iq < n; iq++) sm += Math.abs(a[ip][iq]);
      if (sm === 0) break;
      var tresh = sweep < 4 ? 0.2 * sm / (n * n) : 0;
      for (ip = 0; ip < n - 1; ip++) {
        for (iq = ip + 1; iq < n; iq++) {
          var g = 100 * Math.abs(a[ip][iq]);
          if (sweep > 4 && Math.abs(d[ip]) + g === Math.abs(d[ip]) &&
                           Math.abs(d[iq]) + g === Math.abs(d[iq])) {
            a[ip][iq] = 0;
          } else if (Math.abs(a[ip][iq]) > tresh) {
            var h = d[iq] - d[ip], t;
            if (Math.abs(h) + g === Math.abs(h)) t = a[ip][iq] / h;
            else {
              var theta = 0.5 * h / a[ip][iq];
              t = 1 / (Math.abs(theta) + Math.sqrt(1 + theta * theta));
              if (theta < 0) t = -t;
            }
            var c = 1 / Math.sqrt(1 + t * t), s = t * c, tau = s / (1 + c);
            h = t * a[ip][iq];
            z[ip] -= h; z[iq] += h; d[ip] -= h; d[iq] += h;
            a[ip][iq] = 0;
            for (j = 0; j < ip; j++) jrot(a, s, tau, j, ip, j, iq);
            for (j = ip + 1; j < iq; j++) jrot(a, s, tau, ip, j, j, iq);
            for (j = iq + 1; j < n; j++) jrot(a, s, tau, ip, j, iq, j);
            for (j = 0; j < n; j++) jrot(v, s, tau, j, ip, j, iq);
          }
        }
      }
      for (ip = 0; ip < n; ip++) { b[ip] += z[ip]; d[ip] = b[ip]; z[ip] = 0; }
    }
    var idx = d.map(function (_, q) { return q; })
      .sort(function (p, q) { return d[p] - d[q]; });
    var values = idx.map(function (q) { return d[q]; });
    var V = [];
    for (i = 0; i < n; i++) { V[i] = []; for (j = 0; j < n; j++) V[i][j] = v[i][idx[j]]; }
    /* deterministic sign: largest-magnitude entry of each column is positive */
    for (j = 0; j < n; j++) {
      var best = 0, bi = 0;
      for (i = 0; i < n; i++) if (Math.abs(V[i][j]) > best) { best = Math.abs(V[i][j]); bi = i; }
      if (V[bi][j] < 0) for (i = 0; i < n; i++) V[i][j] = -V[i][j];
    }
    return { values: values, vectors: V };
  }

  function column(V, j) { return V.map(function (row) { return row[j]; }); }

  /* Durand-Kerner.  coeffs low-to-high (real), returns [{re, im}]. */
  function polyRootsDK(coeffs) {
    var c = coeffs.slice(), i, k;
    var scale = 0;
    for (i = 0; i < c.length; i++) scale = Math.max(scale, Math.abs(c[i]));
    if (scale === 0) return [];
    while (c.length > 1 && Math.abs(c[c.length - 1]) <= 1e-13 * scale) c.pop();
    var zeros = 0;
    while (c.length > 1 && Math.abs(c[0]) <= 1e-13 * scale) { c.shift(); zeros++; }
    var d = c.length - 1, roots = [];
    for (i = 0; i < zeros; i++) roots.push({ re: 0, im: 0 });
    if (d <= 0) return roots;
    var lead = c[d], a = c.map(function (x) { return x / lead; });
    var cauchy = 0;
    for (i = 0; i < d; i++) cauchy = Math.max(cauchy, Math.abs(a[i]));
    cauchy = 1 + cauchy;                       /* every root lies inside this disc */

    function peval(zr, zi) {                   /* Horner, high to low, monic */
      var rr = 0, ri = 0, bound = 0, az = Math.hypot(zr, zi);
      for (var q = d; q >= 0; q--) {
        var tr = rr * zr - ri * zi + a[q];
        ri = rr * zi + ri * zr;
        rr = tr;
        bound = bound * az + Math.abs(a[q]);   /* Sum |a_q| |z|^q: the roundoff scale */
      }
      return [rr, ri, bound];
    }

    /* Weierstrass/Durand-Kerner from one starting configuration */
    function attempt(radius, offset) {
      var z = [], i2, k2, it;
      for (i2 = 0; i2 < d; i2++) {
        var th = 2 * Math.PI * i2 / d + offset;
        z.push({ re: radius * Math.cos(th), im: radius * Math.sin(th) });
      }
      for (it = 0; it < 600; it++) {
        var move = 0;
        for (i2 = 0; i2 < d; i2++) {
          var p = peval(z[i2].re, z[i2].im), dr = 1, di = 0;
          for (k2 = 0; k2 < d; k2++) {
            if (k2 === i2) continue;
            var ur = z[i2].re - z[k2].re, ui = z[i2].im - z[k2].im;
            var t2 = dr * ur - di * ui; di = dr * ui + di * ur; dr = t2;
          }
          var den = dr * dr + di * di;
          if (den < 1e-300 || !isFinite(den)) continue;
          var qr = (p[0] * dr + p[1] * di) / den, qi = (p[1] * dr - p[0] * di) / den;
          if (!isFinite(qr) || !isFinite(qi)) continue;
          z[i2].re -= qr; z[i2].im -= qi;
          move = Math.max(move, Math.hypot(qr, qi));
        }
        if (move < 1e-15) break;
      }
      var res = 0;                             /* worst backward error of the batch */
      for (i2 = 0; i2 < d; i2++) {
        var e = peval(z[i2].re, z[i2].im);
        res = Math.max(res, Math.hypot(e[0], e[1]) / (e[2] || 1));
      }
      return { z: z, res: res };
    }

    /* Weierstrass is not globally convergent — a root can stall far from the others.
       Verify the batch by its backward error and restart from a different ring if it
       is bad; keep the best attempt. */
    var best = null, tries = [[cauchy * 0.75, 0.37], [cauchy * 0.5, 1.13], [1, 0.71],
                              [cauchy, 2.41], [cauchy * 0.25, 0.05]];
    for (i = 0; i < tries.length; i++) {
      var got = attempt(tries[i][0], tries[i][1]);
      if (!best || got.res < best.res) best = got;
      if (best.res < 1e-11) break;
    }
    for (i = 0; i < d; i++) {
      var zi2 = best.z[i];
      if (Math.abs(zi2.im) < 1e-11) zi2.im = 0;
      roots.push({ re: zi2.re, im: zi2.im });
    }
    return roots;
  }

  /* p(z) and p'(z) by Horner, coefficients low-to-high; returns [pr, pi, qr, qi] */
  function polyEvalD(c, zr, zi) {
    var pr = 0, pi = 0, qr = 0, qi = 0, t;
    for (var k = c.length - 1; k >= 0; k--) {
      t = qr * zr - qi * zi + pr; qi = qr * zi + qi * zr + pi; qr = t;
      t = pr * zr - pi * zi + c[k]; pi = pr * zi + pi * zr; pr = t;
    }
    return [pr, pi, qr, qi];
  }

  /* Durand-Kerner spreads a root of multiplicity m over a disc of radius ~eps^(1/m),
     so a repeated root comes back as a little ring.  Group the ring back together
     (single linkage at `tol`) and, if the coefficients are supplied, polish the
     centroid with the modified Newton step z - m p(z)/p'(z) — which is well
     conditioned at a multiple root — accepting a step only while |p| decreases.
     Returns [{re, im, mult}], multiplicities summing to roots.length. */
  function clusterRoots(roots, tol, coeffs) {
    tol = tol == null ? 1e-6 : tol;
    var lab = roots.map(function () { return -1; }), nc = 0, i, j;
    for (i = 0; i < roots.length; i++) {
      if (lab[i] >= 0) continue;
      var stack = [i]; lab[i] = nc;
      while (stack.length) {
        var a = stack.pop();
        for (j = 0; j < roots.length; j++)
          if (lab[j] < 0 && Math.hypot(roots[a].re - roots[j].re, roots[a].im - roots[j].im) < tol) {
            lab[j] = nc; stack.push(j);
          }
      }
      nc++;
    }
    var out = [];
    for (var c = 0; c < nc; c++) {
      var g = roots.filter(function (_, q) { return lab[q] === c; });
      var zr = 0, zi = 0;
      g.forEach(function (z) { zr += z.re; zi += z.im; });
      zr /= g.length; zi /= g.length;
      if (coeffs && coeffs.length > 1) {
        var best = polyEvalD(coeffs, zr, zi), bz = [zr, zi];
        var bestAbs = Math.hypot(best[0], best[1]);
        for (var it = 0; it < 40; it++) {
          var e = polyEvalD(coeffs, bz[0], bz[1]);
          var den = e[2] * e[2] + e[3] * e[3];
          if (den < 1e-300) break;
          var wr = (e[0] * e[2] + e[1] * e[3]) / den, wi = (e[1] * e[2] - e[0] * e[3]) / den;
          var nz = [bz[0] - g.length * wr, bz[1] - g.length * wi];
          var f = polyEvalD(coeffs, nz[0], nz[1]), fa = Math.hypot(f[0], f[1]);
          if (!(fa < bestAbs)) break;
          bz = nz; bestAbs = fa;
          if (Math.hypot(g.length * wr, g.length * wi) < 1e-16) break;
        }
        zr = bz[0]; zi = bz[1];
      }
      if (Math.abs(zi) < 1e-11) zi = 0;
      out.push({ re: zr, im: zi, mult: g.length });
    }
    return out;
  }

  /* ===================================================================== */
  /*  formatting                                                            */
  /* ===================================================================== */

  function fmt(x, digits) {
    digits = digits == null ? 4 : digits;
    if (x == null || typeof x !== 'number' || !isFinite(x)) return String(x);
    if (x === 0) return '0';
    var a = Math.abs(x);
    if (a < 1e-4 || a >= 1e6) return x.toExponential(Math.max(0, digits - 1));
    if (Math.abs(x - Math.round(x)) < 1e-11 * Math.max(1, a)) return String(Math.round(x));
    var dec;
    if (a >= 1) dec = Math.max(0, digits - (Math.floor(Math.log10(a)) + 1));
    else dec = Math.min(12, digits - 1 - Math.floor(Math.log10(a)));
    return x.toFixed(dec);
  }

  function fmtC(z, digits) {
    var re = fmt(z.re, digits), im = fmt(Math.abs(z.im), digits);
    if (Math.abs(z.im) < 5e-12) return re;
    return re + (z.im < 0 ? ' − ' : ' + ') + im + 'i';
  }

  var SUP = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
    '-': '⁻', '−': '⁻', '+': '⁺'
  };
  function sup(k) { return String(k).split('').map(function (ch) { return SUP[ch] || ch; }).join(''); }

  /* coefficient array (low to high) -> "1 − u² − u³ + u⁵" */
  function polyString(coeffs, v, digits) {
    v = v || 'u';
    var out = '', any = false;
    for (var k = 0; k < coeffs.length; k++) {
      var c = coeffs[k];
      if (Math.abs(c) < 1e-11) continue;
      var sign = c < 0 ? ' − ' : (any ? ' + ' : '');
      var mag = Math.abs(c), ms = fmt(mag, digits == null ? 4 : digits);
      var body = k === 0 ? ms : ((Math.abs(mag - 1) < 1e-11 ? '' : ms) + v + (k === 1 ? '' : sup(k)));
      out += sign + body;
      any = true;
    }
    return any ? out : '0';
  }

  /* ===================================================================== */
  /*  DOM helpers                                                           */
  /* ===================================================================== */

  function h(tag, attrs, children) {
    var e = document.createElement(tag);
    applyAttrs(e, attrs);
    appendKids(e, children);
    return e;
  }

  function applyAttrs(e, attrs) {
    if (!attrs) return;
    Object.keys(attrs).forEach(function (k) {
      var val = attrs[k];
      if (val == null || val === false) return;
      if (k === 'text') e.textContent = val;
      else if (k === 'html') e.innerHTML = val;
      else if (k === 'style' && typeof val === 'object') Object.assign(e.style, val);
      else if (typeof val === 'function' && k.slice(0, 2) === 'on') e.addEventListener(k.slice(2), val);
      else e.setAttribute(k, val === true ? '' : String(val));
    });
  }

  function appendKids(e, children) {
    if (children == null) return;
    (Array.isArray(children) ? children : [children]).forEach(function (c) {
      if (c == null || c === false) return;
      e.appendChild(typeof c === 'string' || typeof c === 'number'
        ? document.createTextNode(String(c)) : c);
    });
  }

  /* input + change on every element, then one initial call */
  function onChange(elements, fn) {
    (Array.isArray(elements) ? elements : [elements]).forEach(function (el) {
      if (!el) return;
      el.addEventListener('input', fn);
      el.addEventListener('change', fn);
    });
    fn();
  }

  function clear(el) { while (el.firstChild) el.removeChild(el.firstChild); return el; }

  /* ===================================================================== */
  /*  SVG helpers                                                           */
  /* ===================================================================== */

  var NS = 'http://www.w3.org/2000/svg';

  function el(tag, attrs, children) {
    var e = document.createElementNS(NS, tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      var v = attrs[k];
      if (v == null || v === false) return;
      e.setAttribute(k, String(v));
    });
    if (children != null) {
      (Array.isArray(children) ? children : [children]).forEach(function (c) {
        e.appendChild(typeof c === 'string' || typeof c === 'number'
          ? document.createTextNode(String(c)) : c);
      });
    }
    return e;
  }

  /* fresh <svg viewBox="0 0 w h"> inside container (container is cleared).
     maxw caps how wide a square figure grows in a wide column. */
  function newSvg(container, w, h2, maxw) {
    clear(container);
    var s = el('svg', {
      viewBox: '0 0 ' + w + ' ' + h2, width: '100%',
      preserveAspectRatio: 'xMidYMid meet', role: 'img',
      style: maxw ? 'max-width:' + maxw + 'px;margin-left:auto;margin-right:auto' : null
    });
    container.appendChild(s);
    return s;
  }

  function normPad(pad) {
    if (pad == null) pad = 28;
    if (typeof pad === 'number') return { l: pad + 22, r: pad * 0.6, t: pad * 0.5, b: pad };
    return { l: pad.l || 0, r: pad.r || 0, t: pad.t || 0, b: pad.b || 0 };
  }

  function tickValues(t, a, b) {
    if (Array.isArray(t)) return t;
    var n = (typeof t === 'number' ? t : 5), out = [];
    for (var i = 0; i <= n; i++) out.push(a + (b - a) * i / n);
    return out;
  }

  /* draws the frame and returns the mapper {X, Y} */
  function axes(svg, o) {
    var w = o.w, ht = o.h, p = normPad(o.pad);
    var x0 = o.x0, x1 = o.x1, y0 = o.y0, y1 = o.y1;
    function X(x) { return p.l + (x - x0) / (x1 - x0 || 1) * (w - p.l - p.r); }
    function Y(y) { return ht - p.b - (y - y0) / (y1 - y0 || 1) * (ht - p.t - p.b); }
    var g = el('g', { 'font-size': 10, fill: 'var(--ink-3)' });
    var xs = tickValues(o.xticks, x0, x1), ys = tickValues(o.yticks, y0, y1), i, v;
    for (i = 0; i < ys.length; i++) {
      v = typeof ys[i] === 'object' ? ys[i].v : ys[i];
      g.appendChild(el('line', {
        x1: X(x0), x2: X(x1), y1: Y(v), y2: Y(v),
        stroke: 'var(--bg-3)', 'stroke-width': 1
      }));
      g.appendChild(el('text', {
        x: X(x0) - 5, y: Y(v) + 3.5, 'text-anchor': 'end'
      }, typeof ys[i] === 'object' ? ys[i].label : fmt(v, 3)));
    }
    for (i = 0; i < xs.length; i++) {
      v = typeof xs[i] === 'object' ? xs[i].v : xs[i];
      g.appendChild(el('line', {
        x1: X(v), x2: X(v), y1: Y(y0), y2: Y(y0) + 4, stroke: 'var(--ink-3)', 'stroke-width': 1
      }));
      g.appendChild(el('text', {
        x: X(v), y: Y(y0) + 15, 'text-anchor': 'middle'
      }, typeof xs[i] === 'object' ? xs[i].label : fmt(v, 3)));
    }
    g.appendChild(el('path', {
      d: 'M' + X(x0) + ' ' + Y(y1) + 'V' + Y(y0) + 'H' + X(x1),
      fill: 'none', stroke: 'var(--ink-3)', 'stroke-width': 1
    }));
    if (o.xlabel) g.appendChild(el('text', {
      x: (X(x0) + X(x1)) / 2, y: ht - 2, 'text-anchor': 'middle', fill: 'var(--ink-2)'
    }, o.xlabel));
    if (o.ylabel) g.appendChild(el('text', {
      x: 10, y: (Y(y0) + Y(y1)) / 2, 'text-anchor': 'middle', fill: 'var(--ink-2)',
      transform: 'rotate(-90 10 ' + (Y(y0) + Y(y1)) / 2 + ')'
    }, o.ylabel));
    svg.appendChild(g);
    return { X: X, Y: Y, pad: p };
  }

  var CLS = {
    accent: 'var(--accent)', pole: 'var(--pole)', bad: 'var(--bad)',
    ink: 'var(--ink-2)', ink3: 'var(--ink-3)', soft: 'var(--accent-soft)'
  };
  function colorOf(cls) { return CLS[cls] || cls || CLS.accent; }

  /* unit circle with filled points and hollow reference markers */
  function circlePlot(container, o) {
    o = o || {};
    var size = o.size || 260, c = size / 2, R = size / 2 - 26;
    var svg = newSvg(container, size, size, o.maxWidth || 330);
    svg.appendChild(el('line', { x1: c - R - 12, x2: c + R + 12, y1: c, y2: c, stroke: 'var(--bg-3)' }));
    svg.appendChild(el('line', { x1: c, x2: c, y1: c - R - 12, y2: c + R + 12, stroke: 'var(--bg-3)' }));
    svg.appendChild(el('circle', {
      cx: c, cy: c, r: R, fill: 'none', stroke: 'var(--rule)', 'stroke-width': 1.25
    }));
    var lab = el('g', { 'font-size': 10, fill: 'var(--ink-3)' });
    lab.appendChild(el('text', { x: c + R + 4, y: c - 5, 'text-anchor': 'start' }, '1'));
    lab.appendChild(el('text', { x: c - R - 4, y: c - 5, 'text-anchor': 'end' }, '−1'));
    lab.appendChild(el('text', { x: c + 5, y: c - R - 5 }, 'i'));
    svg.appendChild(lab);
    function P(z) { return { x: c + R * z.re, y: c - R * z.im }; }
    (o.ref || []).forEach(function (z) {
      var q = P(z);
      svg.appendChild(el('circle', {
        cx: q.x, cy: q.y, r: 7, fill: 'none', stroke: 'var(--ink-2)', 'stroke-width': 1.4
      }));
    });
    (o.points || []).forEach(function (z) {
      var q = P(z), col = colorOf(z.cls);
      svg.appendChild(el('circle', {
        cx: q.x, cy: q.y, r: z.r || 4.2, fill: col, stroke: 'var(--panel)', 'stroke-width': 0.8
      }));
      if (z.label) {
        var out = Math.hypot(z.re, z.im) < 1e-9 ? { re: 0, im: 1 } : z;
        svg.appendChild(el('text', {
          x: q.x + 11 * out.re, y: q.y - 11 * out.im + 3.5,
          'text-anchor': out.re > 0.3 ? 'start' : (out.re < -0.3 ? 'end' : 'middle'),
          'font-size': 10, fill: col
        }, z.label));
      }
    });
    if (o.caption) svg.appendChild(el('text', {
      x: c, y: size - 4, 'text-anchor': 'middle', 'font-size': 10, fill: 'var(--ink-3)'
    }, o.caption));
    return svg;
  }

  /* one or more polylines with dots; series: [{points:[{x,y,cls}], cls, dots}] */
  function linePlot(container, o) {
    var w = o.w || 300, ht = o.h || 200;
    var svg = newSvg(container, w, ht);
    var m = axes(svg, {
      w: w, h: ht, pad: o.pad, x0: o.x0, x1: o.x1, y0: o.y0, y1: o.y1,
      xlabel: o.xlabel, ylabel: o.ylabel, xticks: o.xticks, yticks: o.yticks
    });
    if (o.hline != null && o.hline >= o.y0 && o.hline <= o.y1)
      svg.appendChild(el('line', {
        x1: m.X(o.x0), x2: m.X(o.x1), y1: m.Y(o.hline), y2: m.Y(o.hline),
        stroke: 'var(--ink-2)', 'stroke-width': 1, 'stroke-dasharray': '3 3'
      }));
    (o.series || []).forEach(function (s) {
      var pts = s.points.filter(function (p) { return isFinite(p.y); });
      if (pts.length > 1) svg.appendChild(el('polyline', {
        points: pts.map(function (p) { return m.X(p.x) + ',' + m.Y(p.y); }).join(' '),
        fill: 'none', stroke: colorOf(s.cls), 'stroke-width': 1.6,
        'stroke-linejoin': 'round', opacity: s.faint ? 0.55 : 1
      }));
      if (s.dots !== false) pts.forEach(function (p) {
        svg.appendChild(el('circle', {
          cx: m.X(p.x), cy: m.Y(p.y), r: p.r || 3.4, fill: colorOf(p.cls || s.cls),
          stroke: 'var(--panel)', 'stroke-width': 0.8
        }));
      });
    });
    return { svg: svg, map: m };
  }

  /* small matrix as an HTML grid, diverging cell background */
  function matrixGrid(container, matrix, o) {
    o = o || {};
    var f = o.fmt || function (v) { return fmt(v, 3); };
    var m = matrix.length, n = matrix[0].length, i, j, big = 0;
    for (i = 0; i < m; i++) for (j = 0; j < n; j++) big = Math.max(big, Math.abs(matrix[i][j]));
    var scale = o.colorScale || function (v) {
      if (!(big > 0) || Math.abs(v) < 1e-12 * Math.max(1, big)) return 'var(--panel)';
      var p = Math.min(100, Math.round(100 * Math.pow(Math.abs(v) / big, 0.6)));
      var soft = v >= 0 ? 'var(--accent-soft)' : 'var(--bad-soft)';
      return 'color-mix(in srgb, ' + soft + ' ' + p + '%, var(--panel))';
    };
    clear(container);
    var fs = Math.max(8, Math.min(12.5, 120 / n));
    var dig = n > 9 ? 2 : 3;
    if (!o.fmt) f = function (v) { return fmt(v, dig); };
    var grid = h('div', {
      class: 'num', style: {
        display: 'grid', gridTemplateColumns: 'repeat(' + n + ', minmax(0, 1fr))',
        gap: '2px', fontSize: fs.toFixed(1) + 'px', lineHeight: '1.5', minWidth: (n * 34) + 'px'
      }
    });
    for (i = 0; i < m; i++) for (j = 0; j < n; j++) {
      var v = matrix[i][j];
      grid.appendChild(h('div', {
        text: f(v), title: 'T[' + i + ',' + j + '] = ' + fmt(v, 6),
        style: {
          background: scale(v), color: 'var(--ink)', textAlign: 'center',
          padding: '3px 1px', borderRadius: '3px', border: '1px solid var(--bg-3)',
          overflow: 'hidden', whiteSpace: 'nowrap'
        }
      }));
    }
    var wrap = h('div', { style: { overflowX: 'auto' } }, grid);
    container.appendChild(wrap);
    return grid;
  }

  /* ===================================================================== */
  /*  mounting                                                              */
  /* ===================================================================== */

  function mountAll() {
    Object.keys(ZT.demos).forEach(function (name) {
      var root = document.getElementById('demo-' + name);
      if (!root) return;
      try {
        ZT.demos[name](root);
      } catch (err) {
        var pre = document.createElement('pre');
        pre.className = 'err';
        pre.textContent = 'demo "' + name + '" failed: ' + ((err && err.stack) || err);
        root.appendChild(pre);
      }
    });
  }

  /* ===================================================================== */

  ZT.parseCycles = parseCycles;
  ZT.permPower = permPower;
  ZT.fixedPoints = fixedPoints;
  ZT.countsOf = countsOf;
  ZT.cyclesOf = cyclesOf;
  ZT.cycleType = cycleType;
  ZT.eigenvaluesOfPerm = eigenvaluesOfPerm;
  ZT.distinctEigs = distinctEigs;
  ZT.powerSums = powerSums;
  ZT.newtonToPoly = newtonToPoly;
  ZT.zetaTaylor = zetaTaylor;
  ZT.zetaProductTaylor = zetaProductTaylor;
  ZT.toeplitz = toeplitz;
  ZT.symEig = symEig;
  ZT.column = column;
  ZT.polyRootsDK = polyRootsDK;
  ZT.clusterRoots = clusterRoots;
  ZT.polyEvalD = polyEvalD;
  ZT.fmt = fmt;
  ZT.fmtC = fmtC;
  ZT.sup = sup;
  ZT.polyString = polyString;
  ZT.h = h;
  ZT.clear = clear;
  ZT.onChange = onChange;
  ZT.mountAll = mountAll;
  ZT.svg = {
    el: el, newSvg: newSvg, axes: axes, circlePlot: circlePlot,
    linePlot: linePlot, matrixGrid: matrixGrid, colorOf: colorOf, NS: NS
  };
  ZT.matrixGrid = matrixGrid;

})(typeof window !== 'undefined' ? window : globalThis);
