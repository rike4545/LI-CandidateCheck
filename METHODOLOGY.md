# Methodology

Both reviews use the same process and the same rating scale, so their results can be read side by side.

| Review | Subject | Captured |
|---|---|---|
| [kassay/](kassay/) | https://www.kassayforassembly.com/rebecca-delivers ("Paid for by Friends of Kassay for Assembly 2026"): intro plus all 13 community tabs | October 24, 2026 |
| [murray/](murray/) | https://chrismurrayforstatesenate.com/: Home, [About](https://chrismurrayforstatesenate.com/about/), [Priorities](https://chrismurrayforstatesenate.com/priorities/) ("Paid for by Chris Murray for State Senate") | November 26, 2026 |

## Process

1. **Inventory.** Every factual statement on the pages in scope was extracted, then deduplicated into unique claims. The `communities` column (Kassay) or `pages` column (Murray) records every place a claim appears. Pure promises ("I will…") are not rated, but factual premises inside them are, e.g. "the state share of the sales tax is 4%."
2. **Source hierarchy.**
   1. Official records: NYS Senate/Assembly bill pages, state agency decisions (e.g., DEC), Governor's releases, Division of the Budget, Department of Taxation and Finance, Comptroller, EPA.
   2. The candidate's own official materials, such as Assembly office releases and law-firm profiles. These are official but self-reported.
   3. Independent news (TBR News Media, News12, RiverheadLOCAL, The Suffolk Times, 27east, City & State, etc.).
   4. Supporter letters and advocacy sites, used only as weak corroboration.
3. **Rating.** Each claim is rated on whether the evidence supports it *as worded on the page*. See the key below.

## Ratings

- ✅ **Verified**: matches the source.
- 🟡 **Verified with caveat**: accurate or plausible, but omitted context (shared credit, outcome, an outdated title, missing math) would change a reasonable reader's takeaway.
- 🟠 **Overstated / partly accurate**: a material part is inflated, conflated with someone else's work, or contradicted by the candidate's own records or statements.
- ⚪ **Unverified**: no public record found. This is *not* a finding that the claim is false.
- 🔵 **Activity claim**: ongoing work, attendance or campaigning that public records can't confirm or refute.
- ❌ **False**: contradicted by evidence.

## Comparing the two reviews

The two pages are different kinds of documents. *Rebecca Delivers* is an incumbent's record of funding and legislation. Murray's site is a challenger's biography plus a platform. Raw counts are therefore not a like-for-like score of either candidate's honesty. The useful comparison is the *pattern* of problems in each.

## Limits

- Kassay: the NYSED state-aid portal was unreachable, so the five school-aid totals were checked for magnitude only. Legislative-initiative grants are often not published per member.
- Murray: Citizens Campaign for the Environment's board page and one news article (Dan's Papers) could not be retrieved. Bio roles listed without dates were checked against the most recent public record found.
- A candidate's own releases or firm profile count as confirmation that something was *announced* or *claimed*, not that it was independently verified.
- Pages may change after capture; claim wording here is paraphrased unless quoted.

## Reproducing / updating

Each folder's `claims.csv` is the source of truth. Regenerate the ledgers with:

```bash
python3 build.py            # both reviews
python3 build.py murray     # one review
```

The script refuses to build if a row has a missing column, an unknown rating, or an unknown category.
