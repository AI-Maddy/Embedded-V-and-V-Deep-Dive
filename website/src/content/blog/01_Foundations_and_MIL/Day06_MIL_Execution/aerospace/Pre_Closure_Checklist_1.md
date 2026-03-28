---
title: "Pre Closure Checklist"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 📋 Pre-Closure Checklist

**Gate: Must be 100 % complete before MIL execution evidence is
submitted**

-   [ ] All scenarios in the Verification Plan matrix have been executed
    and have verdicts.
-   [ ] 🟢 Nominal, 🟡 Boundary, and 🔴 Fault scenario categories each
    have ≥1 completed run.
-   [ ] Environment manifest (`env_manifest.json`) hashes match CI
    baseline --- no drift.
-   [ ] Deterministic re-run (10 % sample) confirms bit-for-bit
    identical logs.
-   [ ] Every verdict is **quantitative** --- numeric value vs.
    threshold, not visual.
-   [ ] Evidence folders are **read-only**; no post-run modifications.
-   [ ] Traceability CSV maps every requirement ID → scenario ID →
    verdict → artifact path.
-   [ ] Summary plots include title, axis labels, units, req ID, and
    verdict stamp.
-   [ ] Canary check scenario passes --- toolchain sanity confirmed.
-   [ ] Coverage report (Simulink Coverage or equivalent) archived in
    evidence folder.
-   [ ] Residual risks and next actions are assigned to named owners
    with due dates.

