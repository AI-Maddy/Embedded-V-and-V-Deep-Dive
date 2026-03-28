---
title: "Pitfalls"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# ⚠️ Pitfalls

::: caution
::: title
Caution
:::

Capstone-specific traps:

-   🕳️ **Time management** --- You have \~4 hours; if setup takes \> 1
    hour, you won\'t finish all 12 scenarios. Use pre-built templates.
-   🕳️ **Scope creep** --- Resist adding a 13th scenario for \"extra
    credit.\" Cover the 12 requirements first; extras only if time
    permits.
-   🕳️ **Fault injection breaks the model** --- A poorly configured
    fault (e.g., elevator jam at 90°) may crash Simulink. Use guarded
    fault values.
-   🕳️ **Report generation fails** --- If `generate_report.py` crashes,
    you lose the traceability artifact. Test the report script on canary
    output first.
-   🕳️ **Git commit forgotten** --- The evidence package references a
    commit hash; if you didn\'t commit before the run, the hash is
    wrong.
:::

