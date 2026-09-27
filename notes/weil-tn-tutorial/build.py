#!/usr/bin/env python3
"""build.py -- inline theme.css and the JS modules into index.html, producing the single-file page
weil-positivity-contracted.html that is published as the artifact. Run from this directory or the repo root."""
import os, re, sys
here = os.path.dirname(os.path.abspath(__file__))
def rd(name):
    with open(os.path.join(here, name), encoding='utf-8') as f: return f.read()
html = rd('index.html')
parts = {
    '/*__THEME_CSS__*/': rd('theme.css'),
    '/*__DATA_JS__*/': rd('data-riemann.js'),
    '/*__CORE_JS__*/': rd('core.js'),
    '/*__TN_JS__*/': rd('tn.js'),
    '/*__DEMOS_CORE_JS__*/': rd('demos-core.js'),
    '/*__DEMOS_GRAPHS_JS__*/': rd('demos-graphs.js'),
    '/*__DEMOS_KRAUS_JS__*/': rd('demos-kraus.js'),
    '/*__DEMOS_AS_JS__*/': rd('demos-as.js'),
}
for k, v in parts.items():
    assert k in html, k
    assert '</script>' not in v, 'a module contains </script>'
    html = html.replace(k, v)
out = os.path.join(here, 'weil-positivity-contracted.html')
with open(out, 'w', encoding='utf-8') as f: f.write(html)
print(out, len(html.encode('utf-8')), 'bytes')
