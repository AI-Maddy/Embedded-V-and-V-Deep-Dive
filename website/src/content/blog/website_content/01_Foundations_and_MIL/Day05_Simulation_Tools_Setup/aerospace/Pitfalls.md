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

Watch for these subtle failure modes that survive internal review but
fail SOI:

-   🕳️ **Hidden calibration assumptions** --- environment constants
    hard-coded in the model instead of injected through a qualified
    parameter set.
-   🕳️ **Missing negative-path coverage** --- every HIGH/CATASTROPHIC
    hazard needs at least one explicitly failed-state scenario with
    measured recovery behaviour.
-   🕳️ **Broken traceability chains** --- a requirement that traces to a
    test but the test does not trace back to a verification result is a
    gap, even if the test passes.
-   🕳️ **Float precision drift** --- parameter rounding across tool
    boundaries can introduce sub-LSB errors that accumulate into
    mode-transition timing issues.
:::

