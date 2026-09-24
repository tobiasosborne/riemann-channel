"""Step 4 of viz-brief.md: the kinematic commutant (lane B2) (lane V; claude:opus).

Lane B2 had not reported (no lane file) when this package was built.  The brief says: skip with a placeholder
page that says so.  This script checks for lane
B2's lane file and outputs and registers a placeholder entry (rendered as a card in index.html and README.md and
as figures/rtp1/s4_placeholder.html).  Nothing is drawn, and nothing of lane B2 is anticipated or recomputed.
"""
import glob
import os

import common as C

STEP = "step4"
SCRIPT = "viz/rtp1/step4_commutant.py"
B2 = os.path.join(C.REPO, "notes", "rtp-round-1", "lane-B2.md")

WANTED = ("A 3-dimensional slice of the window's positive cone with the kinematic subspace, the maximum-determinant "
          "element from pole and archimedean data only, and the true form.")


def b2_state():
    pats = [os.path.join(C.OUT, "rtp1_b2*"), os.path.join(C.OUT, "rtp1_commutant*"), os.path.join(C.OUT, "rtp1_calibration*"),
            os.path.join(C.REPO, "scripts", "rtp1_commutant*"), os.path.join(C.REPO, "scripts", "rtp1_calibration*")]
    outs = sorted(set(p for pat in pats for p in glob.glob(pat)))
    return os.path.exists(B2), [C.rel(p) for p in outs]


def placeholder(fid, step, title, wanted):
    has, outs = b2_state()
    if has:
        why = ("lane B2's lane file exists, but this package has no drawing for it yet; re-run lane V after lane B2 "
               "(and its review) to draw it.")
    elif outs:
        why = ("lane B2 had not reported when this build ran: notes/rtp-round-1/lane-B2.md does not exist. In-progress "
               "files were present (%s) and were not used." % ", ".join(outs))
    else:
        why = "lane B2 has not run: notes/rtp-round-1/lane-B2.md and its outputs do not exist."
    return dict(id=fid, step=step, title=title, placeholder=True,
                caption="Placeholder: not drawn. " + why + " Wanted (viz-brief.md): " + wanted,
                panels=[], kind="placeholder", sources=["notes/rtp-round-1/lane-B2.md (absent)"], script=SCRIPT)


def run():
    e = placeholder("s4_placeholder", "Step 4", "The kinematic commutant (pending lane B2)", WANTED)
    C.register(STEP, [e])
    return [e]


if __name__ == "__main__":
    run()
