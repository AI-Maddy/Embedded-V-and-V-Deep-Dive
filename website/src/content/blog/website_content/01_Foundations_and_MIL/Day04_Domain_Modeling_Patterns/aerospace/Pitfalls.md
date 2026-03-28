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

Subtle issues that pass informal review but fail formal SOI-2 model

-   🕳️ **Undocumented implicit ordering** --- Simulink evaluates
    subsystems in topological order; if execution order is not explicit,
    timing anomalies appear only in code generation, not at model level.
-   🕳️ **Fixed-point overflow in gain scheduling** --- BNR scaling
    applied before fixed-point quantisation can cause silent saturation
    at extreme envelope corners.
-   🕳️ **SSM decoded as boolean** --- collapsing `NCD`, `FW`, `FT` into
    a single `invalid` boolean loses information needed by the monitor
    logic.
-   🕳️ **Hysteresis parameter not requirement-linked** --- protection
    hysteresis values require a safety justification traced to the SSA;
    \"chosen by test\" is not acceptable.
-   🕳️ **Reconfiguration latency untested** --- the model may switch
    correctly in steady state but exceed the FHA latency budget under
    high computational load.
:::

