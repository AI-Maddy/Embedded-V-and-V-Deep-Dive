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

Closed-loop-specific traps:

-   🕳️ **Algebraic loop** --- Simulink may insert a unit-delay to break
    an algebraic loop; this adds 1× Ts of phase lag that shifts the real
    phase margin by several degrees --- check the model diagnostics for
    implicit delays.
-   🕳️ **Sensor-model fidelity mismatch** --- an ideal sensor (zero
    noise, zero bias) makes the closed loop look better than the real
    system; always include at least the noise and bias from the sensor
    datasheet.
-   🕳️ **Trim-state dependency** --- a closed-loop run must start from a
    trimmed equilibrium. If the model is not trimmed, the first few
    seconds are a transient artefact, not a design response. Use
    `operspec()` + `findop()` to compute trim.
-   🕳️ **Turbulence correlation** --- if pitch and roll turbulence
    channels use the same seed, cross-coupling appears artificially low.
    Use independent seeds per axis.
-   🕳️ **Co-simulation rate mismatch** --- plant at 100 Hz, controller
    at 200 Hz without a proper rate-transition block causes
    sample-and-hold glitches that masquerade as instability.
:::

------------------------------------------------------------------------
