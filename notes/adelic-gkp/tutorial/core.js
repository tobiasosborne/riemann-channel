// Numerical core for "Super Ihara Zeta Primer". No DOM. Every number on the page is computed here.
const Core = (() => {
  // ---------- graphs ----------
  function completeEdges(n) { const e = []; for (let a = 0; a < n; a++) for (let b = a + 1; b < n; b++) e.push([a, b]); return e; }
  function prismEdges(m) { const e = []; for (let i = 0; i < m; i++) { e.push([i, (i + 1) % m]); e.push([m + i, m + (i + 1) % m]); e.push([i, m + i]); } return e; }
  function petersenEdges() { const e = []; for (let i = 0; i < 5; i++) { e.push([i, (i + 1) % 5]); e.push([i, i + 5]); e.push([5 + i, 5 + (i + 2) % 5]); } return e; }
  function ring(n, r, off = -Math.PI / 2, start = 0) { const p = []; for (let i = 0; i < n; i++) { const t = off + 2 * Math.PI * i / n; p.push([r * Math.cos(t), r * Math.sin(t)]); } return p; }
  function makeGraph(name, n, edges, pos, label) {
    const A = Array.from({ length: n }, () => Array(n).fill(0));
    for (const [a, b] of edges) { A[a][b] = 1; A[b][a] = 1; }
    const deg = A[0].reduce((s, v) => s + v, 0);
    return { name, label, n, edges, A, q: deg - 1, pos };
  }
  const GRAPHS = {
    K4: () => makeGraph('K4', 4, [[0, 1], [0, 2], [0, 3], [1, 2], [2, 3], [3, 1]], [[0, 0.05], ...ring(3, 1)], 'K₄ (tetrahedron)'),
    K5: () => makeGraph('K5', 5, completeEdges(5), ring(5, 1), 'K₅'),
    cube: () => makeGraph('cube', 8, prismEdges(4), [...ring(4, 1, -Math.PI / 4), ...ring(4, 0.5, -Math.PI / 4)], 'cube (bipartite)'),
    petersen: () => makeGraph('petersen', 10, petersenEdges(), [...ring(5, 1), ...ring(5, 0.5)], 'Petersen'),
    prism6: () => makeGraph('prism6', 12, prismEdges(6), [...ring(6, 1), ...ring(6, 0.55)], 'prism C₆ × K₂'),
    prism21: () => makeGraph('prism21', 42, prismEdges(21), [...ring(21, 1), ...ring(21, 0.7)], 'prism C₂₁ × K₂'),
  };
  function graph(name) { return GRAPHS[name](); }

  // ---------- linear algebra ----------
  function eigSym(A0) {
    const n = A0.length; const A = A0.map(r => r.slice());
    for (let sweep = 0; sweep < 60; sweep++) {
      let off = 0; for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) off += A[i][j] * A[i][j];
      if (off < 1e-24) break;
      for (let p = 0; p < n; p++) for (let q = p + 1; q < n; q++) {
        if (Math.abs(A[p][q]) < 1e-300) continue;
        const th = (A[q][q] - A[p][p]) / (2 * A[p][q]);
        const t = (th >= 0 ? 1 : -1) / (Math.abs(th) + Math.sqrt(th * th + 1));
        const c = 1 / Math.sqrt(t * t + 1), s = t * c;
        for (let k = 0; k < n; k++) { const akp = A[k][p], akq = A[k][q]; A[k][p] = c * akp - s * akq; A[k][q] = s * akp + c * akq; }
        for (let k = 0; k < n; k++) { const apk = A[p][k], aqk = A[q][k]; A[p][k] = c * apk - s * aqk; A[q][k] = s * apk + c * aqk; }
      }
    }
    return A.map((r, i) => r[i]).sort((a, b) => a - b);
  }
  function matmul(X, Y) { const n = X.length, m = Y[0].length, k = Y.length; const Z = Array.from({ length: n }, () => Array(m).fill(0)); for (let i = 0; i < n; i++) for (let l = 0; l < k; l++) { const x = X[i][l]; if (x === 0) continue; for (let j = 0; j < m; j++) Z[i][j] += x * Y[l][j]; } return Z; }
  function matvec(X, v) { return X.map(r => r.reduce((s, x, j) => s + x * v[j], 0)); }
  function identity(n) { return Array.from({ length: n }, (_, i) => Array.from({ length: n }, (_, j) => (i === j ? 1 : 0))); }
  function trace(X) { let t = 0; for (let i = 0; i < X.length; i++) t += X[i][i]; return t; }
  // det(xI - A) coefficients c[j] of x^j (Faddeev-LeVerrier; exact for small integer matrices)
  function charpoly(A) {
    const n = A.length; const c = Array(n + 1).fill(0); c[n] = 1;
    let M = Array.from({ length: n }, () => Array(n).fill(0));
    for (let k = 1; k <= n; k++) {
      const AM = matmul(A, M); for (let i = 0; i < n; i++) AM[i][i] += c[n - k + 1];
      M = AM; c[n - k] = -trace(matmul(A, M)) / k;
    }
    return c.map(x => Math.round(x));
  }
  function polyMul(a, b) { const out = Array(a.length + b.length - 1).fill(0); for (let i = 0; i < a.length; i++) for (let j = 0; j < b.length; j++) out[i + j] += a[i] * b[j]; return out; }
  function polyAdd(a, b) { const out = Array(Math.max(a.length, b.length)).fill(0); a.forEach((v, i) => out[i] += v); b.forEach((v, i) => out[i] += v); return out; }
  // ascending coefficients of det(1 - A u + q u^2)
  function iharaPoly(A, q) {
    const n = A.length, c = charpoly(A); let out = [0];
    let pw = [1];
    const pows = [pw]; for (let j = 1; j <= n; j++) { pw = polyMul(pw, [1, 0, q]); pows.push(pw); }
    for (let j = 0; j <= n; j++) { const term = polyMul(Array(n - j).fill(0).concat([c[j]]), pows[j]); out = polyAdd(out, term); }
    return out.map(x => Math.round(x));
  }
  function polyEval(p, u) { let s = 0; for (let i = p.length - 1; i >= 0; i--) s = s * u + p[i]; return s; }
  function polyFormat(p, v = 'u') { // ascending coefficients -> string
    const parts = [];
    p.forEach((c, i) => { if (c === 0) return; const sgn = c < 0 ? '−' : '+'; const a = Math.abs(c); const coef = (a === 1 && i > 0) ? '' : String(a); const mono = i === 0 ? '' : (i === 1 ? v : v + '^' + i); parts.push([sgn, coef + mono]); });
    if (!parts.length) return '0';
    return parts.map(([s, t], i) => (i === 0 ? (s === '−' ? '−' : '') : ' ' + s + ' ') + t).join('');
  }
  // real roots of a polynomial with all-real simple roots (ascending coefficients), by sign scanning
  function realRoots(p, lo, hi, grid = 4000) {
    const roots = []; let x0 = lo, f0 = polyEval(p, x0);
    for (let i = 1; i <= grid; i++) { const x1 = lo + (hi - lo) * i / grid, f1 = polyEval(p, x1); if (f0 === 0) roots.push(x0); else if (f0 * f1 < 0) { let a = x0, b = x1, fa = f0; for (let it = 0; it < 60; it++) { const m = (a + b) / 2, fm = polyEval(p, m); if (fa * fm <= 0) b = m; else { a = m; fa = fm; } } roots.push((a + b) / 2); } x0 = x1; f0 = f1; }
    return roots;
  }

  // ---------- non-backtracking operator ----------
  function directed(edges) { const d = []; edges.forEach(([a, b]) => { d.push([a, b]); d.push([b, a]); }); return d; } // rev(e) = e ^ 1
  function hashimoto(g, signs) { // signs: array over undirected edges (+1/-1) or null
    const d = directed(g.edges), m = d.length; const B = Array.from({ length: m }, () => Array(m).fill(0));
    for (let e = 0; e < m; e++) for (let f = 0; f < m; f++) if (d[e][1] === d[f][0] && f !== (e ^ 1)) B[e][f] = signs ? signs[f >> 1] : 1;
    return { d, B };
  }
  function traces(B, kmax) { const out = [B.length]; let P = identity(B.length); for (let k = 1; k <= kmax; k++) { P = matmul(P, B); out.push(trace(P)); } return out; }
  function primeCounts(N) { // N[k] = Tr B^k -> number of (oriented) prime cycles of each length
    const pi = [0]; for (let l = 1; l < N.length; l++) { let s = N[l]; for (let d = 1; d < l; d++) if (l % d === 0) s -= d * pi[d]; pi.push(s / l); } return pi;
  }
  // "lines": eigenvalues mu of M (mu^2 - lambda mu + q = 0) for each adjacency eigenvalue lambda
  function lines(lams, q) { const out = []; for (const l of lams) { const D = l * l - 4 * q; if (D >= 0) { const r = Math.sqrt(D); out.push({ re: (l + r) / 2, im: 0, lam: l }); out.push({ re: (l - r) / 2, im: 0, lam: l }); } else { const r = Math.sqrt(-D); out.push({ re: l / 2, im: r / 2, lam: l }); out.push({ re: l / 2, im: -r / 2, lam: l }); } } return out; }
  function isRamanujan(lams, q, n) { const band = 2 * Math.sqrt(q) + 1e-9; const nontriv = lams.filter(l => Math.abs(Math.abs(l) - (q + 1)) > 1e-9); return nontriv.every(l => Math.abs(l) <= band); }
  function negIndexQ(lams, q) { return lams.filter(l => l * l > 4 * q + 1e-9).length; }

  // ---------- flux ----------
  function spanningTree(g) { const seen = new Set([0]), stack = [0], tree = new Set(); while (stack.length) { const v = stack.pop(); g.edges.forEach(([a, b], i) => { const w = a === v ? b : (b === v ? a : -1); if (w >= 0 && !seen.has(w)) { seen.add(w); tree.add(i); stack.push(w); } }); } return tree; }
  function cotree(g) { const t = spanningTree(g); return g.edges.map((_, i) => i).filter(i => !t.has(i)); }
  function signedA(g, signs) { const A = g.A.map(r => r.slice()); g.edges.forEach(([a, b], i) => { A[a][b] = signs[i]; A[b][a] = signs[i]; }); return A; }
  function* fluxClasses(g) { const co = cotree(g); const m = co.length; for (let bits = 0; bits < (1 << m); bits++) { const s = Array(g.edges.length).fill(1); co.forEach((ei, j) => { if (bits & (1 << j)) s[ei] = -1; }); yield { bits, signs: s }; } }
  function matchingPoly(g) { // ascending coefficients in x of sum_k (-1)^k m_k x^{n-2k}
    const E = g.edges, m = E.length; const counts = Array(Math.floor(g.n / 2) + 1).fill(0);
    function rec(i, used, k) { if (i === m) { counts[k]++; return; } rec(i + 1, used, k); const [a, b] = E[i]; if (!used.has(a) && !used.has(b)) { used.add(a); used.add(b); rec(i + 1, used, k + 1); used.delete(a); used.delete(b); } }
    rec(0, new Set(), 0);
    const p = Array(g.n + 1).fill(0); counts.forEach((c, k) => { p[g.n - 2 * k] = (k % 2 ? -1 : 1) * c; }); return p;
  }
  function fluxAverageCharpoly(g) { let tot = null, cnt = 0, inBand = 0; for (const { signs } of fluxClasses(g)) { const As = signedA(g, signs); const c = charpoly(As); tot = tot ? tot.map((v, i) => v + c[i]) : c; cnt++; if (isRamanujanSigned(eigSym(As), g.q)) inBand++; } return { avg: tot.map(v => v / cnt), count: cnt, inBand }; }
  function isRamanujanSigned(lams, q) { const band = 2 * Math.sqrt(q) + 1e-9; return lams.every(l => Math.abs(l) <= band); }
  function fermionicQmin(lams, q) { return Math.min(...lams.map(l => ((q + 1) - Math.sqrt((q - 1) * (q - 1) + l * l)) / 2)); }

  // closed non-backtracking walks of K4 (centre vertex 0, spokes = tree) by homology class in Z^3
  function homologyWalks(g, co, k) { // co: cotree edge indices (oriented as in g.edges)
    const { d, B } = hashimoto(g, null); const m = d.length;
    const cls = d.map(([a, b]) => co.map(ei => (g.edges[ei][0] === a && g.edges[ei][1] === b) ? 1 : ((g.edges[ei][0] === b && g.edges[ei][1] === a) ? -1 : 0)));
    const hist = new Map();
    for (let e0 = 0; e0 < m; e0++) {
      let states = new Map(); states.set(e0 + '|' + cls[e0].join(','), { e: e0, x: cls[e0].slice(), c: 1 });
      for (let j = 1; j < k; j++) { const nxt = new Map(); for (const st of states.values()) for (let f = 0; f < m; f++) if (B[st.e][f]) { const x = st.x.map((v, i) => v + cls[f][i]); const key = f + '|' + x.join(','); const o = nxt.get(key); if (o) o.c += st.c; else nxt.set(key, { e: f, x, c: st.c }); } states = nxt; }
      for (const st of states.values()) if (B[st.e][e0]) { const key = st.x.join(','); hist.set(key, (hist.get(key) || 0) + st.c); }
    }
    return [...hist.entries()].map(([key, c]) => ({ x: key.split(',').map(Number), c }));
  }

  // ---------- one mode: M = [[0,-1],[q,lam]] on the torus ----------
  function mat2pow(M, k) { let P = [[1, 0], [0, 1]]; for (let i = 0; i < k; i++) P = [[P[0][0] * M[0][0] + P[0][1] * M[1][0], P[0][0] * M[0][1] + P[0][1] * M[1][1]], [P[1][0] * M[0][0] + P[1][1] * M[1][0], P[1][0] * M[0][1] + P[1][1] * M[1][1]]]; return P; }
  function periodicPoints(q, lam, k) { // points (a,b)/N on the torus with M^k e = e mod Z^2, grouped into orbits of M
    const M = [[0, -1], [q, lam]]; const P = mat2pow(M, k); const C = [[P[0][0] - 1, P[0][1]], [P[1][0], P[1][1] - 1]];
    const N = Math.abs(C[0][0] * C[1][1] - C[0][1] * C[1][0]);
    const pts = []; const mod = (x, n) => ((x % n) + n) % n;
    for (let a = 0; a < N; a++) for (let b = 0; b < N; b++) if (mod(C[0][0] * a + C[0][1] * b, N) === 0 && mod(C[1][0] * a + C[1][1] * b, N) === 0) pts.push([a, b]);
    const idx = new Map(pts.map((p, i) => [p[0] + ',' + p[1], i])); const orbit = Array(pts.length).fill(-1); const orbits = [];
    pts.forEach((p, i) => { if (orbit[i] >= 0) return; const o = []; let cur = p; while (true) { const j = idx.get(cur[0] + ',' + cur[1]); if (orbit[j] >= 0) break; orbit[j] = orbits.length; o.push(j); cur = [mod(-cur[1], N), mod(q * cur[0] + lam * cur[1], N)]; } orbits.push(o); });
    return { N, pts, orbit, orbits, h: pts.length, det: C[0][0] * C[1][1] - C[0][1] * C[1][0] };
  }
  function pointCounts(q, lam, kmax) { // h_k = 1 - (mu^k + conj) + q^k via the recursion s_k = lam s_{k-1} - q s_{k-2}
    const s = [2, lam]; for (let k = 2; k <= kmax; k++) s.push(lam * s[k - 1] - q * s[k - 2]); const h = [0]; for (let k = 1; k <= kmax; k++) h.push(Math.pow(q, k) + 1 - s[k]); return { s, h };
  }

  function detInt(A0) { // exact integer determinant (Bareiss, BigInt) returned as a Number string-safe integer
    const n = A0.length; const A = A0.map(r => r.map(v => BigInt(Math.round(v)))); let sign = 1n, prev = 1n;
    for (let k = 0; k < n - 1; k++) { if (A[k][k] === 0n) { let sw = -1; for (let i = k + 1; i < n; i++) if (A[i][k] !== 0n) { sw = i; break; } if (sw < 0) return 0; [A[k], A[sw]] = [A[sw], A[k]]; sign = -sign; }
      for (let i = k + 1; i < n; i++) for (let j = k + 1; j < n; j++) A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) / prev; prev = A[k][k]; }
    const d = sign * A[n - 1][n - 1]; return Number(d) === Number(d) && Math.abs(Number(d)) < 9e15 ? Number(d) : d.toString();
  }
  function detLU(M0) { const n = M0.length; const M = M0.map(r => r.slice()); let det = 1; for (let k = 0; k < n; k++) { let p = k; for (let i = k + 1; i < n; i++) if (Math.abs(M[i][k]) > Math.abs(M[p][k])) p = i; if (Math.abs(M[p][k]) < 1e-300) return 0; if (p !== k) { [M[k], M[p]] = [M[p], M[k]]; det = -det; } det *= M[k][k]; for (let i = k + 1; i < n; i++) { const f = M[i][k] / M[k][k]; if (f === 0) continue; for (let j = k; j < n; j++) M[i][j] -= f * M[k][j]; } } return det; }
  function transpose(X) { return X[0].map((_, j) => X.map(r => r[j])); }
  function liftMaps(g) { // sigma, tau: V -> E (2|E| x n), F: edge reversal (2|E| x 2|E|)
    const d = directed(g.edges), m = d.length; const sigma = d.map(([a]) => Array.from({ length: g.n }, (_, v) => (v === a ? 1 : 0))); const tau = d.map(([, b]) => Array.from({ length: g.n }, (_, v) => (v === b ? 1 : 0))); const F = Array.from({ length: m }, (_, e) => Array.from({ length: m }, (_, f) => (f === (e ^ 1) ? 1 : 0))); return { d, sigma, tau, F }; }
  function iharaBassCheck(g, u) { // numerical verification of each step of the vectorised proof
    const n = g.n, { d, B } = hashimoto(g, null), m = d.length; const { sigma, tau, F } = liftMaps(g); const sT = transpose(sigma), tT = transpose(tau);
    const maxAbs = X => Math.max(...X.map(r => Math.max(...r.map(Math.abs))));
    const sub = (X, Y) => X.map((r, i) => r.map((v, j) => v - Y[i][j]));
    const out = {};
    out.B_vs_tausigmaF = maxAbs(sub(B, sub(matmul(tau, sT), F)));
    out.sigmaT_tau_vs_A = maxAbs(sub(matmul(sT, tau), g.A));
    const D = identity(n).map(r => r.map(v => v * (g.q + 1))); out.tauT_tau_vs_D = maxAbs(sub(matmul(tT, tau), D)); out.sigmaT_sigma_vs_D = maxAbs(sub(matmul(sT, sigma), D));
    out.F_tau_vs_sigma = maxAbs(sub(matmul(F, tau), sigma)); out.F2_vs_1 = maxAbs(sub(matmul(F, F), identity(m)));
    if (n <= 10) { // the vectorised form B = P_A (K (x) 1) F on V (x) V, built as explicit n^2 x n^2 matrices
      const N = n * n, idx = (a, b) => a * n + b; const P = Array.from({ length: N }, (_, i) => Array.from({ length: N }, (_, j) => (i === j && g.A[Math.floor(i / n)][i % n] ? 1 : 0)));
      const K1 = Array.from({ length: N }, (_, i) => Array.from({ length: N }, (_, j) => { const a = Math.floor(i / n), b = i % n, x = Math.floor(j / n), y = j % n; return (b === y && a !== x) ? 1 : 0; }));
      const Fv = Array.from({ length: N }, (_, i) => Array.from({ length: N }, (_, j) => (idx(j % n, Math.floor(j / n)) === i ? 1 : 0)));
      const M = matmul(matmul(matmul(P, K1), Fv), P); let md = 0; for (let e = 0; e < m; e++) for (let f = 0; f < m; f++) md = Math.max(md, Math.abs(M[idx(d[e][0], d[e][1])][idx(d[f][0], d[f][1])] - B[e][f])); out.vectorised_vs_B = md; out.vectorised_dim = N; }
    // the determinant steps at u
    const I_E = identity(m), I_V = identity(n);
    const left = detLU(I_E.map((r, i) => r.map((v, j) => v - u * B[i][j])));
    const detF = detLU(I_E.map((r, i) => r.map((v, j) => v + u * F[i][j])));
    const inv = I_E.map((r, i) => r.map((v, j) => (v - u * F[i][j]) / (1 - u * u))); // (1+uF)^{-1}
    const X = matmul(inv, tau).map(r => r.map(v => u * v)); const XY = matmul(X, sT), YX = matmul(sT, X); const edgeSide = detLU(I_E.map((r, i) => r.map((v, j) => v - XY[i][j])));
    const vertexSide = detLU(I_V.map((r, i) => r.map((v, j) => v - YX[i][j])));
    const closed = Math.pow(1 - u * u, g.edges.length - n) * detLU(I_V.map((r, i) => r.map((v, j) => v - u * g.A[i][j] + (i === j ? g.q * u * u : 0))));
    out.det = { left, detF, edgeSide, vertexSide, closed, pow: Math.pow(1 - u * u, g.edges.length) };
    const trF = trace(F); out.F_plus = (m + trF) / 2; out.F_minus = (m - trF) / 2; // F^2 = 1 (checked above) so the eigenvalues are +-1 and the trace fixes the counts
    return out;
  }
  return { GRAPHS, graph, detInt, detLU, transpose, liftMaps, iharaBassCheck, eigSym, matmul, matvec, identity, trace, charpoly, polyMul, iharaPoly, polyEval, polyFormat, realRoots, directed, hashimoto, traces, primeCounts, lines, isRamanujan, negIndexQ, spanningTree, cotree, signedA, fluxClasses, matchingPoly, fluxAverageCharpoly, isRamanujanSigned, fermionicQmin, homologyWalks, mat2pow, periodicPoints, pointCounts };
})();
if (typeof module !== 'undefined') module.exports = Core;
