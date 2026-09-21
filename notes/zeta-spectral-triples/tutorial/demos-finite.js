/* demos-finite.js — stations 1-4: permutations, Newton, the Weil form, Pisarenko.
   Worker A.  Loads after core.js; fills ZT.demos.  Plain ES2020, no libraries. */
(function (global) {
  'use strict';

  var ZT = global.ZT;
  if (!ZT) throw new Error('core.js must be loaded before demos-finite.js');
  var h = ZT.h, S = ZT.svg, fmt = ZT.fmt, sup = ZT.sup;

  var DEF_CYCLES = '(1 2)(3 4 5)', DEF_N = 5, KMAX = 12;

  /* ---------- small chrome helpers ------------------------------------- */

  function head(root, eyebrow, title) {
    ZT.clear(root);
    root.appendChild(h('p', { class: 'demo-eyebrow', text: eyebrow }));
    root.appendChild(h('h3', { class: 'demo-title', text: title }));
  }
  function ctlRow(root) { var d = h('div', { class: 'demo-controls' }); root.appendChild(d); return d; }
  function stage(root) { var d = h('div', { class: 'demo-stage' }); root.appendChild(d); return d; }
  function figure(st, caption) {
    var body = h('div');
    st.appendChild(h('figure', {}, [body, h('figcaption', { html: caption })]));
    return body;
  }
  function readout(root) { var d = h('div', { class: 'demo-readout' }); root.appendChild(d); return d; }
  function note(root, html) { root.appendChild(h('p', { class: 'demo-note', html: html })); }
  function lab(id, text, control, after) {
    return h('label', { for: id }, [text, control].concat(after || []));
  }
  function rangeIn(id, min, max, val) {
    return h('input', { type: 'range', id: id, min: min, max: max, step: 1, value: val });
  }
  function textIn(id, val, size) {
    return h('input', { type: 'text', id: id, value: val, size: size || 13, spellcheck: 'false', autocomplete: 'off' });
  }
  function numIn(id, min, max, val) {
    return h('input', { type: 'number', id: id, min: min, max: max, step: 1, value: val, style: { width: '4.4em' } });
  }
  function btn(id, text) { return h('button', { id: id, class: 'btn', type: 'button', text: text }); }
  function out(id, txt) { return h('span', { id: id, class: 'num', text: txt }); }

  function table(cols, rows) {
    var thead = h('tr', {}, cols.map(function (c) {
      return h('th', c && typeof c === 'object' ? c : { html: String(c) });
    }));
    var body = rows.map(function (r) {
      return h('tr', {}, r.map(function (c) {
        if (c && typeof c === 'object') return h('td', Object.assign({ class: 'num' }, c));
        return h('td', { class: 'num', html: String(c) });
      }));
    });
    return h('div', { class: 'table-wrap' }, h('table', {}, [h('thead', {}, thead), h('tbody', {}, body)]));
  }
  function cell(html, opt) {
    var o = { class: 'num', html: html };
    if (opt && opt.hi) o.style = { background: 'var(--accent-soft)', fontWeight: '600' };
    if (opt && opt.cls) o.class = 'num ' + opt.cls;
    if (opt && opt.color) o.style = Object.assign(o.style || {}, { color: opt.color });
    return o;
  }

  /* ---------- the shared permutation control group ---------------------- */

  function permControls(ctl, name) {
    var cy = textIn('demo-' + name + '-cycles', DEF_CYCLES);
    var nn = numIn('demo-' + name + '-n', 1, KMAX, DEF_N);
    var rb = btn('demo-' + name + '-random', 'random σ');
    ctl.appendChild(lab('demo-' + name + '-cycles', 'σ =', cy));
    ctl.appendChild(lab('demo-' + name + '-n', 'n =', nn));
    ctl.appendChild(rb);
    return { cycles: cy, n: nn, random: rb, els: [cy, nn] };
  }
  function randomCycles(n) {
    var pts = [], i, j, t;
    for (i = 0; i < n; i++) pts.push(i + 1);
    for (i = n - 1; i > 0; i--) { j = Math.floor(Math.random() * (i + 1)); t = pts[i]; pts[i] = pts[j]; pts[j] = t; }
    var s = '', k = 0;
    while (k < n) {
      var len = 1 + Math.floor(Math.random() * Math.min(4, n - k));
      if (len > 1) s += '(' + pts.slice(k, k + len).join(' ') + ')';  /* 1-cycles stay implicit */
      k += len;
    }
    return s || '()';
  }
  function readPerm(pc) {
    var n = Math.round(Number(pc.n.value));
    if (!(n >= 1 && n <= KMAX)) n = DEF_N;
    try { return { ok: true, n: n, perm: ZT.parseCycles(pc.cycles.value, n) }; }
    catch (e) { return { ok: false, n: n, msg: e.message }; }
  }
  function errLine(ro, msg) {
    ZT.clear(ro);
    ro.appendChild(h('span', { class: 'bad', text: '⚠ ' + msg }));
  }
  function r1(x) { return Math.round(x * 10) / 10; }

  /* ---------- the σ-diagram (station 1) --------------------------------- */

  function arcArrow(svg, p, q, cx, cy, trim, col) {
    var mx = (p.x + q.x) / 2, my = (p.y + q.y) / 2;
    var dx = q.x - p.x, dy = q.y - p.y, L = Math.hypot(dx, dy) || 1;
    /* pull towards the centre, then bow consistently to one side, so that i -> j and
       j -> i (a transposition) are two visibly separate arcs */
    var kx = mx + (cx - mx) * 0.30 - dy / L * L * 0.11;
    var ky = my + (cy - my) * 0.30 + dx / L * L * 0.11;
    function unit(ax, ay, bx, by) { var dx = bx - ax, dy = by - ay, L = Math.hypot(dx, dy) || 1; return { x: dx / L, y: dy / L }; }
    var u1 = unit(p.x, p.y, kx, ky), u2 = unit(kx, ky, q.x, q.y);
    var sx = p.x + u1.x * trim, sy = p.y + u1.y * trim, ex = q.x - u2.x * trim, ey = q.y - u2.y * trim;
    svg.appendChild(S.el('path', {
      d: 'M' + r1(sx) + ' ' + r1(sy) + ' Q' + r1(kx) + ' ' + r1(ky) + ' ' + r1(ex) + ' ' + r1(ey),
      fill: 'none', stroke: col, 'stroke-width': 1.5, opacity: 0.85
    }));
    var ah = 7, aw = 3.6, px = -u2.y, py = u2.x;
    svg.appendChild(S.el('polygon', {
      points: [r1(ex) + ',' + r1(ey),
        r1(ex - u2.x * ah + px * aw) + ',' + r1(ey - u2.y * ah + py * aw),
        r1(ex - u2.x * ah - px * aw) + ',' + r1(ey - u2.y * ah - py * aw)].join(' '),
      fill: col
    }));
  }

  var CYCCOL = ['var(--accent)', 'var(--pole)', 'var(--ink-2)', 'var(--ink-3)'];

  function permDiagram(container, perm, k, size) {
    size = size || 300;
    var n = perm.length, c = size / 2, R = size / 2 - 34;
    var nodeR = Math.max(9, Math.min(16, 100 / n + 5));
    var svg = S.newSvg(container, size, size, 340);
    var pk = ZT.permPower(perm, k), cycOf = [];
    ZT.cyclesOf(perm).forEach(function (cy, ci) { cy.forEach(function (p) { cycOf[p] = ci; }); });
    function pt(i) {
      var a = -Math.PI / 2 + 2 * Math.PI * i / n;
      return { x: c + R * Math.cos(a), y: c + R * Math.sin(a), a: a };
    }
    var i, p, col;
    for (i = 0; i < n; i++) {
      col = CYCCOL[cycOf[i] % CYCCOL.length];
      if (perm[i] === i) {
        p = pt(i);
        svg.appendChild(S.el('circle', {
          cx: r1(p.x + Math.cos(p.a) * (nodeR + 7)), cy: r1(p.y + Math.sin(p.a) * (nodeR + 7)),
          r: 7.5, fill: 'none', stroke: col, 'stroke-width': 1.5, opacity: 0.85
        }));
      } else arcArrow(svg, pt(i), pt(perm[i]), c, c, nodeR + 3, col);
    }
    for (i = 0; i < n; i++) {
      p = pt(i);
      var fix = pk[i] === i;
      svg.appendChild(S.el('circle', {
        cx: r1(p.x), cy: r1(p.y), r: r1(nodeR),
        fill: fix ? 'var(--accent-soft)' : 'var(--panel)',
        stroke: fix ? 'var(--accent)' : 'var(--rule)', 'stroke-width': fix ? 2.2 : 1
      }));
      svg.appendChild(S.el('text', {
        x: r1(p.x), y: r1(p.y + 4), 'text-anchor': 'middle',
        'font-size': Math.min(13, nodeR * 1.05), fill: 'var(--ink)'
      }, String(i + 1)));
    }
    return svg;
  }

  /* ===================================================================== */
  /*  Station 1 — permCounts                                                */
  /* ===================================================================== */

  ZT.demos.permCounts = function (root) {
    head(root, 'Demo 1 · Fixed points', 'Count the fixed points of σ, σ², σ³, …');
    var ctl = ctlRow(root), pc = permControls(ctl, 'permCounts');
    var kEl = rangeIn('demo-permCounts-k', 1, KMAX, 1), kOut = out('demo-permCounts-kv', '1');
    ctl.appendChild(lab('demo-permCounts-k', 'power k =', kEl, [kOut]));

    var st = stage(root);
    var figA = figure(st, 'σ as arrows (one colour per cycle). Filled dots: the fixed points of σ<sup>k</sup>.');
    var figB = figure(st, 'N<sub>k</sub> = #Fix(σ<sup>k</sup>). The column for the current k is highlighted.');
    var figC = figure(st, 'First Taylor coefficients: the product over cycles against exp(Σ N<sub>k</sub>u<sup>k</sup>/k).');
    var ro = readout(root);
    note(root, 'A point comes back to itself after k steps exactly when the length of its cycle divides k — ' +
      'so N<sub>k</sub> = Σ<sub>l | k</sub> l, summed over the cycles, and the counting function of σ is ' +
      'the zeta function Z(u) = Π<sub>cycles</sub> (1 − u<sup>l</sup>)<sup>−1</sup>.');

    function draw() {
      var st0 = readPerm(pc);
      var k = Math.min(KMAX, Math.max(1, Math.round(Number(kEl.value))));
      kOut.textContent = String(k);
      if (!st0.ok) { ZT.clear(figA); ZT.clear(figB); ZT.clear(figC); errLine(ro, st0.msg); return; }
      var perm = st0.perm, n = st0.n, lens = ZT.cycleType(perm), i;
      var counts = ZT.countsOf(perm, KMAX);

      permDiagram(figA, perm, k, 300);

      ZT.clear(figB);
      for (var half = 0; half < 2; half++) {
        var ks = [{ html: 'k' }], ns = [{ html: 'N<sub>k</sub>' }];
        for (i = 1 + 6 * half; i <= 6 + 6 * half; i++) {
          ks.push(cell(String(i), { hi: i === k }));
          ns.push(cell(String(counts[i - 1]), { hi: i === k }));
        }
        figB.appendChild(table(ks, [ns]));
      }

      var KZ = 6, prod = ZT.zetaProductTaylor(lens, KZ), expo = ZT.zetaTaylor(counts, KZ), rows = [], dmax = 0;
      for (i = 0; i <= KZ; i++) {
        dmax = Math.max(dmax, Math.abs(prod[i] - expo[i]));
        rows.push([{ html: 'u' + sup(i) }, fmt(prod[i], 6), fmt(expo[i], 6)]);
      }
      ZT.clear(figC);
      figC.appendChild(table(['', 'Π (1−u<sup>l</sup>)<sup>−1</sup>', 'exp Σ N<sub>k</sub>u<sup>k</sup>/k'], rows));

      var divs = lens.filter(function (l) { return k % l === 0; });
      ZT.clear(ro);
      ro.innerHTML =
        'cycle type ' + lens.join(' + ') + ' &nbsp;·&nbsp; ' + lens.length +
        ' cycle' + (lens.length === 1 ? '' : 's') + ' on n = ' + n + ' points<br>' +
        'N<sub>' + k + '</sub> = <b>' + counts[k - 1] + '</b>' +
        (divs.length ? ' = ' + divs.join(' + ') + '  (the cycle lengths dividing ' + k + ')'
                     : '  (no cycle length divides ' + k + ')') +
        '<br>Fix(σ<sup>' + k + '</sup>) = {' +
        ZT.fixedPoints(ZT.permPower(perm, k)).map(function (p) { return p + 1; }).join(', ') + '}' +
        '<br>the two series agree to ' + fmt(dmax, 2) + ' — <b>Z(u) = Π (1−u<sup>l</sup>)<sup>−1</sup> = exp Σ N<sub>k</sub>u<sup>k</sup>/k</b>';
    }

    ZT.onChange(pc.els.concat([kEl]), draw);
    pc.random.addEventListener('click', function () {
      pc.cycles.value = randomCycles(Math.max(1, Math.min(KMAX, Math.round(Number(pc.n.value)) || DEF_N)));
      draw();
    });
  };

  /* ===================================================================== */
  /*  Station 2 — newton                                                    */
  /* ===================================================================== */

  ZT.demos.newton = function (root) {
    head(root, 'Demo 2 · Counts ↔ spectrum', 'Counts are power sums of eigenvalues');
    var ctl = ctlRow(root), pc = permControls(ctl, 'newton');
    var mEl = rangeIn('demo-newton-M', 1, DEF_N, DEF_N), mOut = out('demo-newton-Mv', String(DEF_N));
    ctl.appendChild(lab('demo-newton-M', 'counts used M =', mEl, [mOut]));

    var st = stage(root);
    var figA = figure(st, 'Eigenvalues of the permutation matrix: the l-th roots of unity of each cycle. ' +
      'Orange: the eigenvalue 1, once per cycle — the <em>pole</em>.');
    var figB = figure(st, 'The counts, twice: from fixed points, and as the power sums Σ λ<sup>k</sup>.');
    var figC = figure(st, 'Roots of the polynomial recovered from N<sub>1</sub>…N<sub>M</sub> (filled) ' +
      'against the true eigenvalues (hollow).');
    var ro = readout(root);
    note(root, 'Newton’s identities invert the map spectrum → counts. With all n counts the recovery is exact; ' +
      'with M &lt; n counts you get a polynomial of degree M whose roots leave the circle. ' +
      'Counts determine the spectrum — but you need a window at least as long as the spectrum.');

    function draw() {
      var s0 = readPerm(pc);
      if (!s0.ok) { [figA, figB, figC].forEach(ZT.clear); errLine(ro, s0.msg); return; }
      var perm = s0.perm, n = s0.n;
      if (Number(mEl.max) !== n) { mEl.max = n; if (Number(mEl.value) > n) mEl.value = n; }
      var M = Math.min(n, Math.max(1, Math.round(Number(mEl.value))));
      mOut.textContent = String(M);
      var eigs = ZT.eigenvaluesOfPerm(perm), counts = ZT.countsOf(perm, Math.max(KMAX, n));
      var dist = ZT.distinctEigs(eigs), nCyc = ZT.cycleType(perm).length;

      S.circlePlot(figA, {
        size: 260,
        points: dist.map(function (z) {
          var isOne = Math.abs(z.re - 1) < 1e-9 && Math.abs(z.im) < 1e-9;
          return {
            re: z.re, im: z.im, cls: isOne ? 'pole' : 'accent', r: 5,
            label: z.mult > 1 ? '×' + z.mult : ''
          };
        })
      });

      var ps = ZT.powerSums(eigs, 8), rows = [], i, dmax = 0;
      for (i = 1; i <= 8; i++) {
        dmax = Math.max(dmax, Math.abs(ps[i - 1] - counts[i - 1]));
        rows.push([{ html: '<b>' + i + '</b>' }, String(counts[i - 1]), fmt(ps[i - 1], 3)]);
      }
      ZT.clear(figB);
      figB.appendChild(table(['k', '#Fix(σ<sup>k</sup>)', 'Σ<sub>λ</sub> λ<sup>k</sup>'], rows));

      var poly = ZT.newtonToPoly(counts.slice(0, M), M);
      /* a repeated root comes back from Durand-Kerner as a tiny ring; group it back.
         Half the smallest gap between distinct eigenvalues is a safe radius, and a
         high multiplicity needs many cycles, which leaves few (hence well separated)
         distinct eigenvalues — the two scales never collide.  Below M = n the roots
         are not eigenvalues at all, so only exact duplicates are merged. */
      var minsep = Infinity, a, b;
      for (a = 0; a < dist.length; a++) for (b = a + 1; b < dist.length; b++)
        minsep = Math.min(minsep, Math.hypot(dist[a].re - dist[b].re, dist[a].im - dist[b].im));
      var roots = ZT.clusterRoots(ZT.polyRootsDK(poly),
        M >= n ? (isFinite(minsep) ? 0.45 * minsep : 0.5) : 1e-6, poly);
      S.circlePlot(figC, {
        size: 260,
        ref: dist,
        points: roots.map(function (z) {
          var onCircle = Math.abs(Math.hypot(z.re, z.im) - 1) < 1e-2;
          return {
            re: z.re, im: z.im, cls: onCircle ? 'accent' : 'bad', r: 4.6,
            label: z.mult > 1 ? '×' + z.mult : ''
          };
        })
      });

      var offMax = 0;
      roots.forEach(function (z) { offMax = Math.max(offMax, Math.abs(Math.hypot(z.re, z.im) - 1)); });
      ZT.clear(ro);
      ro.innerHTML =
        'n = ' + n + ' eigenvalues, <b>' + dist.length + ' distinct</b>; ' +
        '<span class="pole">λ = 1 with multiplicity ' + nCyc + ' = number of cycles</span> ' +
        '— one pole of Z per cycle, the rest are the “zeros”.<br>' +
        'power sums reproduce the counts to ' + fmt(dmax, 2) + ' &nbsp;·&nbsp; ' +
        'Newton from N<sub>1</sub>…N<sub>' + M + '</sub>: &nbsp; 1/Z(u) ≈ <b>' + ZT.polyString(poly) + '</b><br>' +
        'roots: ' + roots.map(function (z) {
          return ZT.fmtC(z, 4) + (z.mult > 1 ? ' (×' + z.mult + ')' : '');
        }).join(' , ') +
        '<br>' + (M >= n
          ? 'M = n: <b>exact</b> — the roots are the eigenvalues, with their multiplicities ' +
            '(max ||z|−1| = ' + fmt(offMax, 2) + ').'
          : '<span class="bad">M = ' + M + ' &lt; n = ' + n + ': truncated.</span> Only ' + M +
            ' roots, and they sit off the unit circle by up to ' + fmt(offMax, 3) + '.');
    }

    ZT.onChange(pc.els.concat([mEl]), draw);
    pc.random.addEventListener('click', function () {
      pc.cycles.value = randomCycles(Math.max(1, Math.min(KMAX, Math.round(Number(pc.n.value)) || DEF_N)));
      draw();
    });
  };

  /* ===================================================================== */
  /*  Station 3 — toeplitz                                                  */
  /* ===================================================================== */

  /* replace the conjugate pair e^{±iθ} of the longest cycle by r e^{±iθ} */
  function breakEigs(eigs, r) {
    var set = eigs.map(function (e) { return { re: e.re, im: e.im, moved: false }; });
    var l = 0, ci = 0;
    eigs.forEach(function (e) { if (e.cycleLength > l) { l = e.cycleLength; ci = e.cycleIndex; } });
    var want = l >= 2 ? 1 : 0, chosen = [];
    eigs.forEach(function (e, i) {
      if (e.cycleIndex === ci && (e.k === want || (l >= 3 && e.k === l - want))) chosen.push(i);
    });
    if (!chosen.length) chosen = [0];
    chosen.forEach(function (i) { set[i].re *= r; set[i].im *= r; set[i].moved = true; });
    var th = Math.atan2(eigs[chosen[0]].im, eigs[chosen[0]].re);
    return { set: set, theta: th, l: l, pair: chosen.length > 1 };
  }

  ZT.demos.toeplitz = function (root) {
    head(root, 'Demo 3 · Positivity', 'The Weil form: positivity is the Riemann hypothesis of the window');
    var ctl = ctlRow(root), pc = permControls(ctl, 'toeplitz');
    var mEl = rangeIn('demo-toeplitz-M', 1, KMAX, 6), mOut = out('demo-toeplitz-Mv', '6');
    ctl.appendChild(lab('demo-toeplitz-M', 'window M =', mEl, [mOut]));
    var rEl = h('input', { type: 'range', id: 'demo-toeplitz-r', min: 0.5, max: 1.5, step: 0.01, value: 1 });
    var rOut = out('demo-toeplitz-rv', '1.00');
    ctl.appendChild(lab('demo-toeplitz-r', 'break RH: r =', rEl, [rOut]));
    var reset = btn('demo-toeplitz-reset', 'back to r = 1');
    ctl.appendChild(reset);

    var st = stage(root);
    var figA = figure(st, 'T<sub>jk</sub> = N<sub>|j−k|</sub>, j,k = 0…M, with N<sub>0</sub> = n. ' +
      'Green: positive entries, red: negative.');
    var figB = figure(st, 'Smallest eigenvalue of T against the window size M. ' +
      'Red dots are negative: positivity has failed.');
    var figC = figure(st, 'The counts that build T. They are the power sums of the (possibly moved) eigenvalues.');
    var ro = readout(root);
    note(root, 'For eigenvalues <em>on</em> the circle, T = Σ<sub>λ</sub> v<sub>λ</sub>v<sub>λ</sub>* with ' +
      'v<sub>λ</sub> = (1, λ, …, λ<sup>M</sup>), so f<sup>T</sup>Tf = Σ<sub>λ</sub> |Σ<sub>j</sub> f<sub>j</sub>λ<sup>j</sup>|² ≥ 0 — ' +
      'automatically. Push an eigenvalue off the circle and that identity is gone; ' +
      'a long enough window sees a negative eigenvalue. That is the Weil positivity criterion in miniature.');

    function draw() {
      var s0 = readPerm(pc);
      if (!s0.ok) { [figA, figB, figC].forEach(ZT.clear); errLine(ro, s0.msg); return; }
      var perm = s0.perm, n = s0.n;
      var M = Math.min(KMAX, Math.max(1, Math.round(Number(mEl.value))));
      var r = Number(rEl.value);
      mOut.textContent = String(M); rOut.textContent = r.toFixed(2);
      var eigs = ZT.eigenvaluesOfPerm(perm), br = breakEigs(eigs, r);
      /* at r = 1 the power sums are integers; clear the 1e-15 roundoff so that the
         matrix and the table show the counts, not the noise (a genuinely broken
         count is O(1) away from an integer and is left alone) */
      var counts = ZT.powerSums(br.set, KMAX).map(function (v) {
        return Math.abs(v - Math.round(v)) < 1e-9 ? Math.round(v) : v;
      });

      S.matrixGrid(figA, ZT.toeplitz(counts, M, n), { fmt: function (v) { return fmt(v, 3); } });

      var pts = [], firstNeg = null, lo = 0, hi = 0;
      for (var m = 1; m <= KMAX; m++) {
        var v = ZT.symEig(ZT.toeplitz(counts, m, n)).values[0];
        if (v < -1e-9 && firstNeg === null) firstNeg = m;
        lo = Math.min(lo, v); hi = Math.max(hi, v);
        pts.push({ x: m, y: v, cls: v < -1e-9 ? 'bad' : 'accent', r: m === M ? 5.2 : 3.4 });
      }
      var pad = 0.08 * (hi - lo || 1);
      S.linePlot(figB, {
        w: 300, h: 210, x0: 0.5, x1: KMAX + 0.5, y0: lo - pad, y1: hi + pad,
        xticks: [1, 3, 5, 7, 9, 11].map(function (q) { return { v: q, label: String(q) }; }),
        yticks: 5, hline: 0, xlabel: 'window M', ylabel: 'min eig T',
        series: [{ points: pts, cls: 'ink3' }]
      });

      var rows = [], cmax = Math.min(KMAX, Math.max(M, 6));
      for (var k = 0; k <= cmax; k++)
        rows.push([{ html: 'N<sub>' + k + '</sub>' }, k === 0 ? String(n) : fmt(counts[k - 1], 5)]);
      ZT.clear(figC);
      figC.appendChild(table(['k', 'N<sub>k</sub>'], rows));

      var eps = ZT.symEig(ZT.toeplitz(counts, M, n)).values[0];
      ZT.clear(ro);
      ro.innerHTML =
        'moved: ' + (br.pair ? 'the conjugate pair e<sup>±iθ</sup>' : 'the eigenvalue e<sup>iθ</sup>') +
        ' of the longest cycle (l = ' + br.l + ', θ = ' + (br.l >= 2 ? '2π/' + br.l : '0') + ') → ' +
        (br.pair ? 'r·e<sup>±iθ</sup>' : 'r·e<sup>iθ</sup>') + ' with r = <b>' + r.toFixed(2) + '</b><br>' +
        'M = ' + M + ':  T is ' + (M + 1) + '×' + (M + 1) + ',  λ<sub>min</sub>(T) = ' +
        (eps < -1e-9 ? '<span class="bad">' + fmt(eps, 5) + '</span>'
                     : '<b>' + fmt(eps, 5) + '</b>' + (Math.abs(eps) < 1e-9 ? ' ≈ 0' : '')) + '<br>' +
        (firstNeg === null
          ? (Math.abs(r - 1) < 1e-9
            ? 'r = 1: every eigenvalue is on the circle and λ<sub>min</sub>(T) ≥ 0 for every M — <b>no negative eigenvalue up to M = 12</b>.'
            : 'r &lt; 1: <b>no negative eigenvalue up to M = 12</b>. Pulling a zero <em>inside</em> the disc alone keeps ' +
              'N<sub>d</sub> = 2r<sup>d</sup>cos dθ — the Fourier coefficients of a Poisson kernel, still a positive measure. ' +
              'It is the <em>outside</em> partner that the functional equation forces (λ ↔ 1/λ̄) which destroys positivity: push r above 1.')
          : 'first window with a negative eigenvalue: <b class="bad">M = ' + firstNeg + '</b>');
    }

    ZT.onChange(pc.els.concat([mEl, rEl]), draw);
    reset.addEventListener('click', function () { rEl.value = 1; draw(); });
    pc.random.addEventListener('click', function () {
      pc.cycles.value = randomCycles(Math.max(1, Math.min(KMAX, Math.round(Number(pc.n.value)) || DEF_N)));
      draw();
    });
  };

  /* ===================================================================== */
  /*  Station 4 — pisarenko                                                 */
  /* ===================================================================== */

  ZT.demos.pisarenko = function (root) {
    head(root, 'Demo 4 · The critical window', 'The minimal eigenvector knows the spectrum');
    var ctl = ctlRow(root), pc = permControls(ctl, 'pisarenko');
    var mEl = rangeIn('demo-pisarenko-M', 1, KMAX, 3), mOut = out('demo-pisarenko-Mv', '3');
    ctl.appendChild(lab('demo-pisarenko-M', 'window M =', mEl, [mOut]));
    var crit = btn('demo-pisarenko-crit', 'jump to the critical window');
    ctl.appendChild(crit);

    var st = stage(root);
    var figA = figure(st, 'Roots of ξ(z) = Σ<sub>j</sub> ξ<sub>j</sub>z<sup>j</sup> (filled) ' +
      'against the distinct eigenvalues (hollow).');
    var figB = figure(st, 'ε = λ<sub>min</sub>(T) against M, log scale. It collapses to 0 at the critical window.');
    var figC = figure(st, 'The minimal eigenvector ξ of T. Read it as the coefficients of a polynomial.');
    var ro = readout(root);
    note(root, 'T is the moment matrix of the measure Σ<sub>λ</sub> δ<sub>λ</sub> on the circle, so its kernel is ' +
      'exactly the polynomials of degree ≤ M vanishing at every eigenvalue. There is none until the window is ' +
      'long enough to hold such a polynomial: <b>a kernel appears exactly when M ≥ #distinct eigenvalues</b>, ' +
      'and at that first M it is one-dimensional — one vector, whose roots are the spectrum. ' +
      'This is Pisarenko’s method, and stations 5–7 run the same move on the zeta zeros.');

    var lastKey = '';

    function draw() {
      var s0 = readPerm(pc);
      if (!s0.ok) { [figA, figB, figC].forEach(ZT.clear); errLine(ro, s0.msg); return; }
      var perm = s0.perm, n = s0.n;
      var eigs = ZT.eigenvaluesOfPerm(perm), dist = ZT.distinctEigs(eigs), D = dist.length;
      var key = perm.join(',');
      if (key !== lastKey) { lastKey = key; mEl.value = Math.max(1, Math.min(KMAX, D - 1)); }
      var M = Math.min(KMAX, Math.max(1, Math.round(Number(mEl.value))));
      mOut.textContent = String(M);
      var counts = ZT.countsOf(perm, KMAX);

      var T = ZT.toeplitz(counts, M, n), e = ZT.symEig(T);
      var eps = e.values[0], gap = (e.values[1] === undefined ? Infinity : e.values[1] - eps);
      var scale = Math.max(1e-300, Math.abs(e.values[e.values.length - 1]));
      var degenerate = gap < 1e-8 * scale;
      var xi = ZT.column(e.vectors, 0);

      /* eps against M */
      var pts = [], lo = 0;
      for (var m = 1; m <= KMAX; m++) {
        var v = ZT.symEig(ZT.toeplitz(counts, m, n)).values[0];
        var y = Math.log10(Math.max(Math.abs(v), 1e-18));
        lo = Math.min(lo, y);
        pts.push({ x: m, y: y, cls: m >= D ? 'pole' : 'accent', r: m === M ? 5.2 : 3.4 });
      }
      var yt = [];
      for (var q = 0; q >= Math.floor(lo); q -= 4) yt.push({ v: q, label: '10' + sup(q) });
      S.linePlot(figB, {
        w: 300, h: 210, x0: 0.5, x1: KMAX + 0.5, y0: Math.floor(lo) - 0.5, y1: 1.2,
        xticks: [1, 3, 5, 7, 9, 11].map(function (t) { return { v: t, label: String(t) }; }),
        yticks: yt, xlabel: 'window M', ylabel: 'ε = λmin(T)',
        series: [{ points: pts, cls: 'ink3' }]
      });

      /* palindromy and roots */
      var pal = 0, apal = 0, j;
      for (j = 0; j <= M; j++) {
        pal = Math.max(pal, Math.abs(xi[j] - xi[M - j]));
        apal = Math.max(apal, Math.abs(xi[j] + xi[M - j]));
      }
      var anti = apal < pal, dev = Math.min(pal, apal);

      var roots = degenerate ? [] : ZT.polyRootsDK(xi);
      var offMax = 0;
      roots.forEach(function (z) { offMax = Math.max(offMax, Math.abs(Math.hypot(z.re, z.im) - 1)); });
      if (degenerate) {
        ZT.clear(figA);
        figA.appendChild(h('p', {
          class: 'demo-note',
          html: 'λ<sub>min</sub>(T) is <b>degenerate</b> here (multiplicity ≥ 2), so “the” minimal eigenvector ' +
            'is not defined — any vector of the eigenspace would do and its roots carry no meaning. Nothing drawn.'
        }));
      } else {
        S.circlePlot(figA, {
          size: 260, ref: dist,
          points: roots.map(function (z) {
            var on = Math.abs(Math.hypot(z.re, z.im) - 1) < 1e-6;
            return { re: z.re, im: z.im, cls: on ? 'accent' : 'bad', r: 4.6 };
          })
        });
      }

      var rows = [];
      for (j = 0; j <= M; j++) rows.push([{ html: 'ξ<sub>' + j + '</sub>' }, fmt(xi[j], 5)]);
      ZT.clear(figC);
      figC.appendChild(table(['j', 'ξ<sub>j</sub>'], rows));

      ZT.clear(ro);
      ro.innerHTML =
        'n = ' + n + ' eigenvalues, <b>' + D + ' distinct</b> → critical window <b>M = ' + D + '</b> ' +
        '(T is then ' + (D + 1) + '×' + (D + 1) + ' of rank ' + D + ')<br>' +
        'M = ' + M + ':  ε = λ<sub>min</sub>(T) = <b>' + fmt(eps, 4) + '</b>' +
        (Math.abs(eps) < 1e-9 ? ' ≈ 0' : '') + ', gap to the next eigenvalue ' +
        fmt(gap, 4) + (degenerate ? ' <span class="bad">(degenerate)</span>' : '') + '<br>' +
        (degenerate ? '' :
          'ξ is ' + (anti ? '<b>anti-palindromic</b> (ξ<sub>j</sub> = −ξ<sub>M−j</sub>)' :
            '<b>palindromic</b> (ξ<sub>j</sub> = ξ<sub>M−j</sub>)') + ' to ' + fmt(dev, 2) +
          ' — self-inversive, so its roots come in pairs z, 1/z̄ and land <em>on</em> the circle ' +
          '(max ||z|−1| = ' + fmt(offMax, 2) + ')<br>' +
          'roots: ' + (roots.length ? roots.map(function (z) { return ZT.fmtC(z, 4); }).join(' , ') : '— (constant)') + '<br>') +
        (M < D
          ? 'below the critical window: ε &gt; 0, no kernel; the ' + M + ' roots only <em>bracket</em> the ' + D + ' eigenvalues.'
          : (M === D
            ? '<b>at the critical window</b>: ε = 0, the kernel is one-dimensional and the roots of ξ are <b>exactly</b> the ' + D + ' distinct eigenvalues.'
            : 'past the critical window: the kernel has dimension ' + (M + 1 - D) +
              ', so the minimal eigenvector is degenerate — the spectrum is read off at M = ' + D + '.'));
    }

    ZT.onChange(pc.els.concat([mEl]), draw);
    crit.addEventListener('click', function () {
      var s0 = readPerm(pc);
      if (!s0.ok) return;
      mEl.value = Math.min(KMAX, ZT.distinctEigs(ZT.eigenvaluesOfPerm(s0.perm)).length);
      draw();
    });
    pc.random.addEventListener('click', function () {
      pc.cycles.value = randomCycles(Math.max(1, Math.min(KMAX, Math.round(Number(pc.n.value)) || DEF_N)));
      draw();
    });
  };

})(typeof window !== 'undefined' ? window : globalThis);
