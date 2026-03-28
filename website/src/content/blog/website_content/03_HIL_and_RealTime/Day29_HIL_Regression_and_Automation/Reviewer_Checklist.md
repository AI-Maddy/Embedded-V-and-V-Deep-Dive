---
title: "Reviewer Checklist"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---



# 🔍 Reviewer Checklist

::: note
::: title
Note
:::

Pre-review checklist - \[ \] Are pass/fail rules explicit and
reproducible? - \[ \] Is each key claim backed by a concrete artifact? -
\[ \] Are failures triaged with severity and owner? - \[ \] Is handoff
quality sufficient for the next phase?
:::

**Severity / Priority Colour Legend** - 🟢 Nominal (Green): Standard
operations, expected outcomes. - 🟡 Boundary (Yellow): Edge cases,
potential for unexpected behavior. - 🔴 Fault (Red): Critical failures,
immediate attention required.

**GIVEN / WHEN / THEN Scenarios** - **Nominal (🟢)** - **GIVEN** the
system is configured correctly, - **WHEN** a valid input is provided, -
**THEN** the system should respond within the specified latency.

-   **Boundary (🟡)**
    -   **GIVEN** the system is operating at the edge of its limits,
    -   **WHEN** an edge input is provided,
    -   **THEN** the system should maintain stability without failure.
-   **Fault (🔴)**
    -   **GIVEN** a critical component fails,
    -   **WHEN** the system attempts to process a request,
    -   **THEN** it should trigger the recovery protocol without
        crashing.
