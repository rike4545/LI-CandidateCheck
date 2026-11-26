# KassayCheck

Independent, source-by-source reviews of the claims Long Island candidates make on their own campaign websites. Every review uses the same method and rating scale.

> Scope: these reviews test whether each claim is **verifiable** and **accurate as stated**. They do not rate candidates, endorse anyone, or judge policy positions.

## Reviews

| Candidate | Office | Page reviewed | Captured | Claims | ✅ | 🟡 | 🟠 | ⚪ | 🔵 | ❌ |
|---|---|---|---|---|---|---|---|---|---|---|
| [Rebecca Kassay (D)](kassay/) | NYS Assembly, AD 4 (incumbent) | *Rebecca Delivers* | 2026-10-24 | 64 | 20 | 9 | 3 | 24 | 8 | 0 |
| [Chris Murray (D, WF)](murray/) | NYS Senate, SD 1 (Senator-elect) | Home, About, Priorities | 2026-11-26 | 25 | 14 | 5 | 1 | 4 | 1 | 0 |

### What each review found

- **Kassay:** Nothing tested was false. The page inflates credit on big dollar figures, overreaches on one cannabis bill, and states one volunteer number higher than her own office reported. It also omits one outcome, and 19 small grants have no public paper trail. [Full summary →](kassay/README.md)
- **Murray:** Nothing tested was false. Past board chairmanships are listed as if current. The "top 8%" income-tax figure conflicts with his own "$600,000" description of the same group. The site describes cap-and-invest as a program already in place, and three bio roles have no public trail. [Full summary →](murray/README.md)

The two pages are different kinds of documents: an incumbent's record versus a challenger's biography and platform. The counts are not a like-for-like score; see [METHODOLOGY.md](METHODOLOGY.md#comparing-the-two-reviews).

## Repo layout

```
kassay/   README (summary + scorecard), CLAIMS.md (ledger), claims.csv (data)
murray/   same structure
METHODOLOGY.md   shared process, source hierarchy, ratings key, limits
build.py         regenerates each CLAIMS.md from its claims.csv
```

Corrections are welcome. Open an issue with a source.

## License

Text and data are licensed under [CC BY 4.0](LICENSE).
