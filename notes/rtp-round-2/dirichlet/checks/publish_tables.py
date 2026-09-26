#!/usr/bin/env python3
"""Author codex:gpt-6-astra. Refresh only the marked D5 extraction in the report."""
from pathlib import Path
import subprocess,sys
HERE=Path(__file__).resolve().parent
s=subprocess.check_output([sys.executable,str(HERE/'summary.py')],text=True)
(HERE/'summary.md').write_text(s)
p=HERE.parent/'astra-proofs.md';report=p.read_text()
a='<!-- D5_TABLES_BEGIN -->';b='<!-- D5_TABLES_END -->'
body=s[s.index('# D5. Saturation'):].replace('# D5. Saturation','### Saturation').replace('\n# ','\n### ')
block=a+'\n'+body+'\n'+b
if a in report:
    start=report.index(a);end=report.index(b,start)+len(b);report=report[:start]+block+report[end:]
else:report+='\n'+block+'\n'
p.write_text(report)
