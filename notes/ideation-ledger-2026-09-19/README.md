# Ideation ledger, 2026-09-19

TJO asked for every idea explored and every lead obtained in the notebook's history to be collected,
with 100% coverage so that no small but consequential idea is lost. This directory is the result.

## Read this first

- `LEDGER.md`: the clean summary. One page, then ideas explored by theme, ranked leads, all remaining
  leads, small-but-consequential items, dead routes, bookkeeping issues, audit.
- `digests/G1..G4`: the deduplicated middle tier (492 items). Each item carries an `Absorbs:` list of
  lane entry IDs, so every line of the summary can be traced to its sources.
- `lanes/L01..L17`: the raw tier (1509 entries), one file per source slice, each entry with an exact
  `file:line` pointer, who raised it, its status at last mention, content, and the implied lead.

## Method

Three tiers, all Claude Opus subagents orchestrated by Claude Fable 5.1, 2026-09-19 afternoon.

1. Seventeen lane agents, each given a disjoint slice of the sources and told to read every line and
   ledger every idea, lead, conjecture, reviewer suggestion, prover aside and dead route in a fixed
   schema. Sources: the founding transcript, HANDOFF, README, all worklogs, all 46 lab book shards
   (plus `db/claims.tsv` for open/conjectured/assumed/sketched rows), every note and campaign file
   under `notes/` (briefs, prover proofs, refuter reviews, source extracts, the CCM sidequest and its
   five lane reports, the 2026-09-19 RH strategy review), the `zst` and `ihz` READMEs, and the
   plaintext-recoverable parts of every codex rollout of this repository since 2026-09-12
   (orchestrator briefs, assistant messages, every file write and calculation; tool outputs excluded).
2. Four digest agents, each over three to six lanes, deduplicating into themed items with exact
   `Absorbs:` lists.
3. One synthesis agent over the four digests, producing `LEDGER.md`.

## Coverage audit

| tier | files | entries | check |
|---|---|---|---|
| sources | 138 repo prose files + 20 codex transcripts | - | every file named in some lane's coverage table (script: `coverage_check.py` in the session scratchpad; 0 missing) |
| lanes | 17 | 1509 | every entry has a source pointer |
| digests | 4 | 492 | every lane entry absorbed exactly once, no invented IDs (verified by script) |
| LEDGER | 1 | - | audit section inside the file |

Digest item classes: 209 explored and registered, 71 explored with a negative result, 15 dead,
99 partially explored, 98 leads never pursued.

## Caveats

- The inter-agent briefs of the 2026-09-19 astra ideation session (the orchestrator's instructions
  to its five subagents and their replies) are stored end-to-end encrypted in the codex rollouts and
  the local codex databases, with no key on disk. They are unrecoverable. The subagents' final
  reports, every file they wrote, and the orchestrator's messages to TJO are plaintext and were
  ledgered (lane L17). Both "stopped" subagents had finished writing their reports before the stop.
- Codex reasoning traces are not stored; only messages, commands and file writes were available.
- The one codex transcript deliberately skipped is an automated sandbox-approval reviewer.
- The codex prover transcripts of 2026-09-12 to 09-16 were diffed against the final files: the
  provers wrote almost linearly, so the transcript residue is brief-level (drafted statements later
  shown false) and message-level, not abandoned mathematics (lanes L14 to L16).
- Nothing here is a registered claim. Statuses are "status at last mention" as read by the lane
  agents, not gate-derived statuses; `db/claims.tsv` remains authoritative for those.
