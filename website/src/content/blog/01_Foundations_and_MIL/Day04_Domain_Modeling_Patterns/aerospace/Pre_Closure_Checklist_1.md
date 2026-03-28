---
title: "Pre Closure Checklist"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 📋 Pre-Closure Checklist

**Gate: Must be 100 % complete before model baseline is submitted for
SOI-2**

-   [ ] All seven domain modeling patterns applied where required are
    tagged in the model.
-   [ ] Every pattern has ≥1 nominal, ≥1 boundary, and ≥1 fault-scenario
    test case.
-   [ ] All model parameters are `Simulink.Parameter` objects with
    CI-controlled values.
-   [ ] `modeladvisor` check passes with zero errors against MAAB /
    DO-331 profile.
-   [ ] Simulink Coverage report shows ≥ 100 % decision coverage at
    model level.
-   [ ] Safety monitors are in independent subsystems; independence
    justified in MAD.
-   [ ] All ARINC 429 / AFDX label SSM fields decoded explicitly (no
    boolean collapse).
-   [ ] Reconfiguration latency verified against FHA latency budget in
    test log.
-   [ ] Model Architecture Document (MAD) updated and peer-reviewed.
-   [ ] Residual risks identified, assigned, and tracked to closure.

