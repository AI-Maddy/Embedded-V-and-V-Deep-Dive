---
title: "Tool Setup Quick Start Checklist"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 🔧 Tool Setup Quick-Start Checklist

Before executing the first MIL run, verify all of the following:

-   [ ] **MATLAB/Simulink** version pinned in `environment.lock` (e.g.
    `R2025a`).
-   [ ] **Aerospace Blockset & Simulink Coverage** toolboxes installed
    and license-checked.
-   [ ] **JSBSim** XML aircraft definition validated against published
    aerodynamic data.
-   [ ] **ARINC 429 bus timing** confirmed: word rate, label set, and
    SSM encoding.
-   [ ] **VectorCAST / LDRA** TQL data package version matches tool
    version in CI.
-   [ ] **RT-Tester / TPT** script parameter file committed to version
    control.
-   [ ] Tool configuration snapshot (hash) captured in the Configuration
    Index (CI).
-   [ ] Smoke test `sldemo_f14` (or equivalent) passes with zero
    warnings on current host.
-   [ ] All tool outputs directed to `evidence/YYYY-MM-DD_run-NNN/`
    folder structure.
-   [ ] Independent reviewer has signed off on tool setup record before
    evidence runs begin.

