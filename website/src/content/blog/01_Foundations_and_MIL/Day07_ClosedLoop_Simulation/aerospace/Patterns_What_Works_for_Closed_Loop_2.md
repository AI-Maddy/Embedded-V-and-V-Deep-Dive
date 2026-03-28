---
title: "Patterns  What Works for Closed Loop 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# ✅ Patterns --- What Works for Closed-Loop

::: tip
::: title
Tip
:::

💡 These patterns are specific to **closed-loop** simulation --- they
build on open-loop patterns from Day 06.
:::

1.  **🔄 Loop-break linearisation** --- Insert `getlinio()` break points
    at the actuator output *before* the first evidence run; extract
    GM/PM automatically after every closed-loop scenario. Store margins
    in `verdict.json`.
2.  **📉 Multi-axis coupling check** --- Run simultaneous pitch + roll
    commands to verify that cross-coupling stays below the spec limit.
    Many bugs only appear when two axes are active.
3.  **🌪️ Progressive turbulence escalation** --- Run the same scenario
    at light, moderate, and severe turbulence; plot RMS tracking error
    vs. turbulence intensity to identify the stability cliff.
4.  **⏱️ Transport-delay sweep** --- Add artificial bus delay (0, 5, 10,
    15 ms) to the ARINC 429 feedback path and measure how gain/phase
    margin degrades; find the maximum tolerable delay.
5.  **🔒 Freeze-frame assertion** --- At the instant of fault injection,
    log the complete state vector; use it as the initial condition for a
    targeted re-run that tests recovery from that exact configuration.
6.  **📊 Spectral noise floor check** --- After a nominal run, FFT the
    tracking error tail; any peak \> noise floor indicates an undamped
    mode or limit cycle.

------------------------------------------------------------------------
