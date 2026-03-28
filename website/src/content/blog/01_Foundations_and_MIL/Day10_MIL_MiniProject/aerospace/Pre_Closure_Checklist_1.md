---
title: "Pre Closure Checklist"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 📋 Pre-Closure Checklist

**Gate: Must be 100 % complete before capstone sign-off**

-   [ ] All 12 requirements mapped to ≥ 1 scenario in
    campaign_manifest.json.
-   [ ] All 12 scenarios executed with quantitative verdicts (no manual
    overrides).
-   [ ] Canary scenario (SC-NOM-01) passed before full campaign.
-   [ ] Determinism verification (10 % re-run) confirms reproducibility.
-   [ ] Evidence folder write-locked (`chmod 444`), SHA-256 manifest
    generated.
-   [ ] Traceability CSV links every Req → Scenario → Verdict →
    Artifact.
-   [ ] HTML/PDF report generated automatically --- no manual edits.
-   [ ] DO-330 TQL assessment exists for batch executor + verdict
    engine.
-   [ ] Residual-risk register populated with ≥ 3 identified items +
    owners.
-   [ ] Git tag applied: `mil_capstone_{date}_{hash}`.
-   [ ] DER review defence prepared (answers for 7 standard questions).
-   [ ] Handoff summary written: what MIL proved, what defers to
    SIL/HIL.

