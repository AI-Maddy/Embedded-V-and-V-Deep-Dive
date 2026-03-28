---
title: "Checklist"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🔎 Checklist

::: checklist
\- \[ \] Concept definitions are precise and testable. - \[ \]
Assumptions and limits are documented. - \[ \] Verification signals and
metrics are identified. - \[ \] Evidence references are present and
reproducible.
:::

**Mnemonic Acronym**: **HIL-VERB** (HIL Verification, Evidence, Review,
Boundaries) This acronym serves as a reminder of the key elements to
focus on during the HIL regression and automation process.

**Severity / Priority Legend**: - 🟢 Nominal (Green): Normal operation
scenarios. - 🟡 Boundary (Yellow): Edge cases and limits. - 🔴 Fault
(Red): Failure scenarios requiring immediate attention.

**GIVEN / WHEN / THEN Scenarios**: - **Nominal** 🟢: - GIVEN a properly
configured HIL setup, - WHEN the system receives a standard input
signal, - THEN the expected output should be generated within the
defined time frame.

-   **Boundary** 🟡:
    -   GIVEN a HIL setup operating at its maximum input limits,
    -   WHEN the system processes the input,
    -   THEN it should maintain stability without failure.
-   **Fault** 🔴:
    -   GIVEN a HIL setup with a simulated hardware failure,
    -   WHEN the failure occurs,
    -   THEN the system should trigger a safe response and log the
        incident for review.

::: note
::: title
Note
:::
:::

Refer to DO-178C for guidelines on software considerations in airborne
systems, and DO-254 for hardware aspects in safety-critical systems.
These standards provide essential frameworks for ensuring compliance and
safety in embedded systems development. Additionally, ISO 26262 provides
guidance for functional safety in automotive systems, which is relevant
to HIL testing processes.
