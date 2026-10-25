#!/usr/bin/env python3
"""Execute Q2's unmodified main, saving only in this lane."""
from pathlib import Path
import os,runpy,sys
H=Path(__file__).resolve().parent
os.environ['NUMBA_CACHE_DIR']=str(H/'numba_cache_q2')
sys.dont_write_bytecode=True
p=H.parents[2]/'astra-2026-10-23/qrh-transpose/checks/qrh_ff_family.py'
ns=runpy.run_path(str(p))
ns['set_num_threads'](12)
ns['main']()
