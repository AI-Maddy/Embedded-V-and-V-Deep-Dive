---
title: "Pattern 4   Safety Monitor   Cross Channel Comparator 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# Pattern 4 --- 🛡️ Safety Monitor / Cross-Channel Comparator

**What It Models**

Dual/triple redundant channel comparison logic that detects disagreement
between redundant sensors or computation lanes and triggers a fault flag
within the latency budget defined by the FHA.

**Pattern Variants**

**🔵 Dual-Channel Comparator (2oo2)**

``` text
Channel_A ─┐
           ├──► |ΔA−B| > THRESHOLD? ──YES──► DISAGREE_FLAG
Channel_B ─┘                          │
                                     NO
                                      └──► AGREE (use average or Channel_A)
```

**🟣 Triple-Voting Median Select (2oo3)**

``` text
Ch_A ─┐
Ch_B ─┼──► Sort(A,B,C) → median value ──► Control Law Input
Ch_C ─┘
       └──► |max−min| > THRESHOLD? ──YES──► MONITOR_FLAG + log outlier
```

**Critical Modeling Rules**

-   Monitor computation must be in a **separate subsystem** from the
    control law --- never share state variables between the monitor and
    the monitored function.
-   Latency budget: monitor must assert flag within the time defined in
    the System Safety Assessment (SSA); model the worst-case execution
    path explicitly.
-   All thresholds must be parametric (`Simulink.Parameter`); justify
    threshold values with reference to sensor accuracy budget from the
    SSA.

------------------------------------------------------------------------
