# Methodology

Every review uses the same process and the same rating scale, so results can be read side by side. The scope is every 2026 New York State Senate (SD1–SD9) and Assembly (AD1–AD22) race in Nassau and Suffolk. Each race has both major-party candidates. Third-party candidates are not reviewed.

## Process

1. **Find the page.** We review the candidate's own campaign website: home, about/bio and issues pages. If the campaign site is gone, we try an archived copy. If neither exists, the candidate is marked `site-unavailable`, with a note on what was searched. Official legislative member pages are used as sources, not as the page under review.
2. **Inventory.** We extract the factual statements on the pages in scope and deduplicate them into unique claims. The `pages` column records where each claim appears. Pure promises ("I will…") are not rated, but factual premises inside them are, e.g. "the state share of the sales tax is 4%."
3. **Depth.** Each review records its depth in `meta.json`:
   - **full** reviews every factual claim on the pages in scope.
   - **core** reviews the checkable claims a voter is most likely to rely on: biography and credentials, the record (bills, votes, funding, offices held), and every number. Generic statements of values are left out.
4. **Source hierarchy.**
   1. Official records: NYS Senate/Assembly bill and member pages, state agency decisions, Governor's releases, Division of the Budget, Department of Taxation and Finance, Comptroller, Board of Elections, EPA.
   2. The candidate's own official materials, such as legislative office releases and employer profiles. These are official but self-reported.
   3. Independent news (Newsday, TBR News Media, RiverheadLOCAL, The Suffolk Times, 27east, LI Herald, Long Island Press, City & State, etc.).
   4. Supporter letters and advocacy sites, used only as weak corroboration.
5. **Rating.** Each claim is rated on whether the evidence supports it *as worded on the page*. See the key below.

## Ratings

- ✅ **Verified**: matches the source.
- 🟡 **Verified with caveat**: accurate or plausible, but omitted context (shared credit, outcome, an outdated title, missing math, an unstated condition) would change a reasonable reader's takeaway.
- 🟠 **Overstated / partly accurate**: a material part is inflated, conflated with someone else's work, or contradicted by the candidate's own records or statements.
- ⚪ **Unverified**: no public record found. This is *not* a finding that the claim is false.
- 🔵 **Activity claim**: ongoing work, attendance or campaigning that public records can't confirm or refute.
- ❌ **False**: contradicted by evidence.

## Comparing reviews

Campaign pages are different kinds of documents. An incumbent's page is usually a record of funding and legislation. A challenger's is usually a biography and a platform. Pages also vary from a few lines to dozens of claims. Raw counts are therefore not a like-for-like score of any candidate's honesty, and party-level totals say little while coverage is partial. The useful comparisons are within a race, and the *pattern* of problems.

## Results

Winners appear only where a cited source names them, and results are unofficial unless marked certified. The source for each result is in `races.json`.

## Limits

- Pages change. Each review records its capture date, and claim wording is paraphrased unless quoted.
- Legislative-initiative grants and pro bono or volunteer roles often have no public record, which is why ⚪ is common.
- A candidate's own releases or employer profile confirm that something was *announced* or *claimed*, not that it was independently verified.
- The site's district view is a grid grouped by county, not a geographic map.
- Only campaign websites are reviewed. Candidates whose only presence is social media or an official legislative page are marked "no site"; so are sites that block automated retrieval, which can be captured by hand later.


## Reproducing / updating

`races.json` and each `candidates/<slug>/meta.json` and `claims.csv` are the source of truth. Regenerate the candidate READMEs, the coverage table and the live site with:

```bash
python3 build.py
```

The build validates every row and stops on errors.
