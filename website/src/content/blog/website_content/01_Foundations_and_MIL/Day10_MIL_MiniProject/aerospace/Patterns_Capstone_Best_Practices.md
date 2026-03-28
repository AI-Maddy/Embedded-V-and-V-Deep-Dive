---
title: "Patterns Capstone Best Practices"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# ✅ Patterns --- Capstone Best Practices

::: tip
::: title
Tip
:::

💡 Patterns distilled from successful DAL-A MIL capstone submissions.
:::

1.  **🏁 Start with the traceability matrix, not the model** --- If you
    know which requirements you must cover, the scenario matrix writes
    itself. Starting with the model leads to \"test what\'s easy, miss
    what\'s hard.\"
2.  **🐦 Canary-first, always** --- A 30-second canary that fails saves
    you from a 90-minute wasted batch run. Never skip the canary.
3.  **🔢 Quantitative verdicts only** --- \"The pitch response looks
    OK\" is not a verdict. `RMS_error = 0.31° < 0.50° → PASS` is a
    verdict.
4.  **📋 Evidence folder = single source of truth** --- Everything the
    DER needs is inside `evidence/`. If an artifact is referenced but
    not in the folder, it doesn\'t exist.
5.  **🔒 Hash everything** --- Model, parameters, scripts, and evidence.
    If a hash doesn\'t match between the manifest and the file, the
    whole campaign is suspect.
6.  **📝 Write the residual-risk register before the review** --- A DER
    who finds uncovered risks before you do will question your entire
    analysis.

