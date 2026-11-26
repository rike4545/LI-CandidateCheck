"""Regenerate each review's CLAIMS.md from its claims.csv and print the rating tallies.

Usage: python3 build.py            # all reviews
       python3 build.py murray     # one review
"""
import collections
import csv
import sys

RATINGS = ["✅", "🟡", "🟠", "⚪", "🔵", "❌"]

REVIEWS = {
    "kassay": {
        "intro": "Every distinct claim on the *Rebecca Delivers* page (reviewed 2026-10-24), "
                 "deduplicated across community tabs.",
        "where_col": "communities",
        "where_label": "Tabs",
        "order": ["Statewide", "Biography", "Legislation", "Funding", "State aid",
                  "Volunteer events", "Constituent service", "Advocacy"],
    },
    "murray": {
        "intro": "Every distinct factual claim on chrismurrayforstatesenate.com "
                 "(Home, About, Priorities; reviewed 2026-11-26), deduplicated across pages. "
                 "Pure policy promises are not rated.",
        "where_col": "pages",
        "where_label": "Pages",
        "order": ["Biography", "Record", "Election", "Policy facts"],
    },
}


def build(name):
    cfg = REVIEWS[name]
    rows = list(csv.DictReader(open(f"{name}/claims.csv", encoding="utf-8")))
    bad = [r["id"] for r in rows if None in r or r["rating"] not in RATINGS or r["category"] not in cfg["order"]]
    if bad:
        sys.exit(f"{name}: malformed rows {bad}")
    tally = collections.Counter(r["rating"] for r in rows)
    print(name, len(rows), "claims", {k: tally[k] for k in RATINGS if tally[k]})

    out = ["# Claims ledger\n",
           f"{cfg['intro']} Ratings key is in [METHODOLOGY.md](../METHODOLOGY.md#ratings).\n"]
    for cat in cfg["order"]:
        rs = [r for r in rows if r["category"] == cat]
        if not rs:
            continue
        out.append(f"\n## {cat}\n\n| ID | Claim (paraphrased) | {cfg['where_label']} | Rating | Finding | Sources |\n"
                   "|---|---|---|---|---|---|")
        for r in rs:
            urls = [u.strip() for u in r["sources"].split("|") if u.strip()]
            src = " ".join(f"[{i + 1}]({u})" for i, u in enumerate(urls)) or "—"
            out.append(f"| {r['id']} | {r['claim']} | {r[cfg['where_col']]} | {r['rating']} | {r['finding']} | {src} |")
    open(f"{name}/CLAIMS.md", "w", encoding="utf-8").write("\n".join(out) + "\n")


for name in sys.argv[1:] or REVIEWS:
    build(name)
