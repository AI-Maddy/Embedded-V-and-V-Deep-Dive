---
title: "Patterns  What Works During MIL Execution 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# ✅ Patterns --- What Works During MIL Execution

::: tip
::: title
Tip
:::

💡 These execution patterns are specifically about **running** the
model, not designing it (Day 04) or setting up tools (Day 05).
:::

1.  **🔒 Pre-run gate** --- Automate environment validation (hashes,
    versions, seeds) as a mandatory pre-condition; reject any run that
    fails the gate.
2.  **📊 Log-everything-at-full-rate** --- Storage is orders of
    magnitude cheaper than re-running a campaign. Trim logs only in the
    analysis phase, never at capture.
3.  **🤖 Headless batch execution** --- Run the entire scenario matrix
    in a single scripted batch (`sim()` loop or `parsim()` for
    parallel); never rely on manual point-and-click for evidence runs.
4.  **📐 Quantitative verdicts** --- Every pass/fail is a numeric
    comparison against a threshold defined in the scenario file;
    subjective \"looks good\" is never acceptable.
5.  **📦 Atomic evidence folders** --- One folder per run, with a unique
    monotonic ID. Folder is **write-once, read-many** --- never modify
    after run completion.
6.  **🔁 Deterministic re-run proof** --- After every campaign, randomly
    re-run 10 % of scenarios and verify bit-for-bit identical logs. Any
    diff triggers investigation.

------------------------------------------------------------------------
