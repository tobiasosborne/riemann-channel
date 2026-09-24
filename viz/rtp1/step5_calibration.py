"""Step 5 of viz-brief.md: the calibration case (lane B2) (lane V; claude:opus).

Lane B2 had not reported: placeholder only (see step4_commutant.py).
"""
import common as C
from step4_commutant import placeholder

STEP = "step5"
SCRIPT = "viz/rtp1/step5_calibration.py"
WANTED = ("The learning curves of Step 1 for a Ramanujan graph or the genus-one curve next to those of zeta.")


def run():
    e = placeholder("s5_placeholder", "Step 5", "The calibration case (pending lane B2)", WANTED)
    e["script"] = SCRIPT
    C.register(STEP, [e])
    return [e]


if __name__ == "__main__":
    run()
