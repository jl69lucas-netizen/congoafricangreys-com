#!/usr/bin/env python3
"""board_gate.py <slug> [--release]
The Page Board gate: refuses to build (or release) a page whose board.json is not
approved as it stands. Reads live headings from dist/ (build first). Exit 1 on any FAIL.
Prints its examined counts — a gate that examines nothing is not a pass
(skills/cag-gate-integrity.md)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import pageboard as PB


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit("usage: board_gate.py <slug> [--release]")
    slug, stage = args[0], ("release" if "--release" in sys.argv else "build")
    board = PB.load_board(slug)
    ont, ledger = PB.load_ontology(), PB.load_ledger()
    live = PB.live_headings() if PB.DIST.exists() else {}
    live.pop("/" + slug + "/", None)
    if not live:
        print("WARN header pre-check examined 0 live pages — run `npx astro build` first")
    f = PB.gate_findings(board, ont, ledger, live, stage=stage)
    n_head = len(PB.all_headings(board))
    print(f"board-gate {slug} [{stage}] — {len(board['sections'])} sections, {n_head} headings, "
          f"{len(live)} live pages, {sum(len(s['entities']) for s in board['sections'])} entity refs examined")
    for x in f:
        print(f"  {x['sev']:4s} {x['check']:24s} {x['msg']}")
    fails = [x for x in f if x["sev"] == "FAIL"]
    print(f"{len(fails)} FAIL · {len(f) - len(fails)} WARN")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
