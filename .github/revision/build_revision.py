#!/usr/bin/env python3
"""Builds REVISION.md from the revision plan and this repo's git history.

A problem counts as revised once NeetCode's GitHub sync has pushed a new
submission for it ("Add: <slug> - submission-N" commit) on or after the
revision start date in plan.json. "Bulk sync" commits are ignored, so a bulk
re-sync of old solutions never ticks anything.

Run from the repo root:  python3 .github/revision/build_revision.py
"""
import json
import os
import subprocess
from datetime import datetime, timedelta, timezone
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DSA = "Data Structures & Algorithms"
OUT = os.path.join(ROOT, "REVISION.md")

cfg = json.load(open(os.path.join(HERE, "plan.json"), encoding="utf-8"))
start = datetime.fromisoformat(cfg["revision_start"])
sign = -1 if cfg["timezone_offset"].startswith("-") else 1
hh, mm = cfg["timezone_offset"].lstrip("+-").split(":")
TZ = timezone(sign * timedelta(hours=int(hh), minutes=int(mm)))


def git_history():
    """slug -> list of (datetime, is_bulk, path) for every commit touching it."""
    log = subprocess.run(
        ["git", "log", "--format=@@%aI|%s", "--name-only", "--", DSA],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    hist = {}
    when = bulk = None
    for line in log.splitlines():
        if line.startswith("@@"):
            date, _, subject = line[2:].partition("|")
            when = datetime.fromisoformat(date)
            bulk = subject.lower().startswith("bulk sync")
            continue
        if not line.strip() or not line.startswith(DSA + "/"):
            continue
        parts = line.split("/")
        if len(parts) < 3:
            continue
        hist.setdefault(parts[1], []).append((when, bulk, line))
    return hist


def file_link(path):
    return quote(path)


def bar(done, total, width=20):
    filled = round(width * done / total) if total else 0
    return "█" * filled + "░" * (width - filled)


def fmt(dt):
    return dt.astimezone(TZ).strftime("%d %b, %H:%M")


hist = git_history()
plan = cfg["problems"]
planned = {p["slug"] for p in plan}

rows = []
for p in plan:
    commits = hist.get(p["slug"], [])
    revisions = sorted(c for c in commits if not c[1] and c[0] >= start)
    before = [c for c in commits if c[0] < start or c[1]]
    old = max(before, key=lambda c: c[0])[2] if before else None
    new = revisions[-1][2] if revisions else None
    rows.append(dict(p, done=bool(revisions),
                     first=revisions[0][0] if revisions else None,
                     times=len(revisions), old=old, new=new))

done_total = sum(r["done"] for r in rows)
total = len(rows)

L = []
L.append("# 🔁 NeetCode Revision Tracker\n")
L.append(f"Re-solving all {total} problems I'd solved before "
         f"{start.astimezone(TZ).strftime('%d %b %Y')}. A box ticks itself when NeetCode "
         "syncs a new submission for that problem to this repo.\n")
L.append(f"**Overall: {done_total} / {total}** &nbsp; `{bar(done_total, total)}` "
         f"&nbsp; {round(100 * done_total / total)}%\n")

L.append("| Day | Focus | Progress |\n|---|---|---|")
for d, focus in cfg["days"].items():
    dr = [r for r in rows if str(r["day"]) == d]
    dd = sum(r["done"] for r in dr)
    L.append(f"| [Day {d}](#day-{d}) | {focus} | {dd} / {len(dr)} `{bar(dd, len(dr), 10)}` |")
L.append("")

nxt = next((r for r in rows if not r["done"]), None)
if nxt:
    L.append(f"**Up next:** [{nxt['title']}](https://neetcode.io/problems/{nxt['slug']}) "
             f"· {nxt['topic']} · {nxt['difficulty']} (Day {nxt['day']})\n")
else:
    L.append("**🎉 All done. Every problem revised.**\n")

DIFF = {"Easy": "🟢 Easy", "Medium": "🟡 Medium", "Hard": "🔴 Hard"}
n = 0
for d, focus in cfg["days"].items():
    dr = [r for r in rows if str(r["day"]) == d]
    dd = sum(r["done"] for r in dr)
    L.append(f"## Day {d}\n")
    L.append(f"_{focus}_ · **{dd} / {len(dr)}** done\n")
    L.append("| | # | Problem | Topic | Difficulty | Revised on | Code |")
    L.append("|:-:|--:|---|---|---|---|---|")
    for r in dr:
        n += 1
        box = "✅" if r["done"] else "⬜"
        title = f"[{r['title']}](https://neetcode.io/problems/{r['slug']})"
        if r["done"]:
            title = f"**{title}**"
        when = fmt(r["first"]) + (f" (×{r['times']})" if r["times"] > 1 else "") if r["done"] else ""
        code = []
        if r["old"]:
            code.append(f"[old]({file_link(r['old'])})")
        if r["new"]:
            code.append(f"[new]({file_link(r['new'])})")
        L.append(f"| {box} | {n} | {title} | {r['topic']} | {DIFF.get(r['difficulty'], r['difficulty'])} "
                 f"| {when} | {' · '.join(code)} |")
    L.append("")

# Problems first solved after the revision started (not part of the plan)
extra = []
for slug, commits in hist.items():
    if slug in planned:
        continue
    first = min(c[0] for c in commits)
    extra.append((first, slug))
if extra:
    L.append("## ➕ New problems solved since revision started\n")
    L.append("| Problem | First solved |\n|---|---|")
    for first, slug in sorted(extra):
        L.append(f"| [{slug.replace('-', ' ').title()}](https://neetcode.io/problems/{slug}) | {fmt(first)} |")
    L.append("")

L.append("## By topic\n")
L.append("| Topic | Revised |\n|---|---|")
topics = []
for r in rows:
    if r["topic"] not in topics:
        topics.append(r["topic"])
order = ["Arrays & Hashing", "Two Pointers", "Sliding Window", "Stack", "Binary Search",
         "Linked List", "Trees", "Heap / Priority Queue", "Backtracking", "Tries", "Graphs",
         "Advanced Graphs", "1-D Dynamic Programming", "2-D Dynamic Programming", "Greedy",
         "Intervals", "Math & Geometry", "Bit Manipulation"]
for t in sorted(topics, key=lambda t: order.index(t) if t in order else 99):
    tr = [r for r in rows if r["topic"] == t]
    td = sum(r["done"] for r in tr)
    L.append(f"| {t} | {td} / {len(tr)} `{bar(td, len(tr), 10)}` |")
L.append("")
L.append("<sub>Auto-updated by `.github/workflows/revision-tracker.yml` on every push · "
         "to change the plan or start date, edit `.github/revision/plan.json`</sub>")

open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
print(f"REVISION.md written: {done_total}/{total} revised")
