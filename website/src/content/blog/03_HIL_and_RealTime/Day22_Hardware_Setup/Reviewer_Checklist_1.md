---
title: "Reviewer Checklist"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🔍 Reviewer Checklist

-   [ ] Are pass/fail rules explicit and reproducible?
-   [ ] Is each key claim backed by a concrete artifact?
-   [ ] Are failures triaged with severity and owner?
-   [ ] Is handoff quality sufficient for the next phase?
-   [ ] Have residual risks and next actions been documented?

::: note
::: title
Note
:::

Use the following severity/priority color legend for issues identified
during testing: - 🟢 Nominal (Low Severity) - 🟡 Boundary (Medium
Severity) - 🔴 Fault (High Severity)
:::

**Scenario Templates**: - **Nominal** 🟢: - **GIVEN** the system is
powered on and configured, - **WHEN** a valid input signal is
received, - **THEN** the system should respond within the specified
timing profile.

-   

    **Boundary** 🟡:

    :   -   **GIVEN** the system is operating at the edge of its input
            range,
        -   **WHEN** a boundary condition is applied,
        -   **THEN** the system should maintain performance without
            failure.

-   

    **Fault** 🔴:

    :   -   **GIVEN** a simulated fault is injected into the system,
        -   **WHEN** the fault condition is triggered,
        -   **THEN** the system should enter a safe state or recover as
            defined by the requirements.
