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

Code-generation-specific traps for aerospace:

-   🕳️ **Signal storage reuse** --- Embedded Coder\'s optimization can
    alias two signals to the same variable. This saves RAM but destroys
    1:1 traceability. Disable for DAL-A.
-   🕳️ **Fixed-point scaling errors** --- If the model uses
    floating-point but the target is fixed-point, the autoscaling step
    can introduce truncation errors exceeding the MIL-SIL tolerance.
    Verify scaling with `fxptdlg`.
-   🕳️ **Inlined parameters** --- Inlining calibration constants into
    generated code means a parameter change requires re-generation +
    re-compilation. Consider `Tunable` parameters for values that change
    in calibration.
-   🕳️ **Non-finite support** --- The default `SupportNonFinite = 'on'`
    generates NaN/Inf guard code. Flight code should never produce NaN
