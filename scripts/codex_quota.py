#!/usr/bin/env python3
"""Read the codex account rate limits through `codex app-server` (JSON-RPC over stdio) and print one line:
   <utc time>  used=<percent>%  window=<mins>  resets_at=<utc>  (reset=<yes|no>)
Exit 0 normally, 2 if a reset of the primary window is detected against the recorded baseline
(notes/rtp-round-2/quota-baseline.json: resetsAt changed, or usedPercent fell by more than 15 points),
3 if the query failed. Usage: scripts/codex_quota.py [--baseline]  (record the current reading as baseline)."""
import json, os, subprocess, sys, time, select, datetime

BASE = os.path.join(os.path.dirname(__file__), "..", "notes", "rtp-round-2", "quota-baseline.json")

def read():
    p = subprocess.Popen(["codex", "app-server"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.DEVNULL, text=True)
    def send(o):
        p.stdin.write(json.dumps(o) + "\n"); p.stdin.flush()
    send({"jsonrpc": "2.0", "id": 1, "method": "initialize",
          "params": {"clientInfo": {"name": "claude-orchestrator", "version": "0.1"}}})
    send({"jsonrpc": "2.0", "method": "initialized", "params": {}})
    send({"jsonrpc": "2.0", "id": 2, "method": "account/rateLimits/read", "params": {}})
    t0 = time.time(); res = None
    while time.time() - t0 < 30:
        r, _, _ = select.select([p.stdout], [], [], 1)
        if not r: continue
        line = p.stdout.readline()
        if not line: break
        try: o = json.loads(line)
        except Exception: continue
        if o.get("id") == 2: res = o.get("result"); break
    p.kill()
    return res

def main():
    res = read()
    if not res:
        print("codex quota: query failed"); sys.exit(3)
    rl = res["rateLimits"]; pr = rl["primary"]
    used, mins, resets = pr["usedPercent"], pr["windowDurationMins"], pr["resetsAt"]
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    rs = datetime.datetime.fromtimestamp(resets, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    reset = False
    if "--baseline" in sys.argv:
        json.dump({"usedPercent": used, "resetsAt": resets, "recorded": now}, open(BASE, "w"))
    elif os.path.exists(BASE):
        b = json.load(open(BASE))
        if resets != b["resetsAt"] or used < b["usedPercent"] - 15: reset = True
    extra = f"  reached={rl.get('rateLimitReachedType')}" if rl.get("rateLimitReachedType") else ""
    print(f"{now}  used={used}%  window={mins}min  resets_at={rs}  reset={'yes' if reset else 'no'}{extra}")
    sys.exit(2 if reset else 0)

if __name__ == "__main__":
    main()
