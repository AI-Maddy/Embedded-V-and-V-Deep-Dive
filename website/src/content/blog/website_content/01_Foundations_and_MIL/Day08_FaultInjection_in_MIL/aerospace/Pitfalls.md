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

Subtle fault-injection pitfalls specific to aerospace MIL:

-   🕳️ **Injection point too late in the chain** --- injecting at the
    bus-decoded output skips the SSM/BNR decoding path; inject at the
    raw bus interface to test the full detection chain.
-   🕳️ **Fault clears itself** --- if the injection uses `sim_time` but
    the model resets time on reconfig, the fault disappears; use a
    persistent fault flag.
-   🕳️ **Monitor tested with the fault it was designed for** --- the
    monitor passes, but a slightly different fault (same sensor,
    different failure mode) escapes; test every FMEA variant, not just
    the design-case fault.
-   🕳️ **Actuator fault model ignores aerodynamic load** --- a jammed
    actuator in reality sees aerodynamic hinge moment; if your model
    holds position with zero force, the plant response is
    unrealistically benign.
-   🕳️ **Windshear injection without pilot model** --- windshear
    recovery requires TOGA thrust; if the pilot/autoland model doesn\'t
    respond, the scenario is invalid.
-   🕳️ **Transient masking** --- a fault injected during a manoeuvre
    transient may be masked by the normal dynamics; inject at both
    steady-state and transient operating points.
:::

