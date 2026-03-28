---
title: "automotive README part2 8"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

## Pitfalls ⚠️

-   Hidden assumptions in environment or calibration setup that may lead
    to erroneous conclusions.
-   Missing negative-path scenarios for high-criticality behavior, which
    could result in untested failure modes.
-   Incomplete traceability from requirement to verdict, risking
    non-compliance with ISO standards.

Awareness of these pitfalls can significantly enhance the effectiveness
of the V&V process.

## Best Practices 🌟

-   Tag every artifact with domain requirement IDs to maintain clear
    traceability.
-   Capture timing + functional evidence in the same run package to
    streamline validation efforts.
-   Record residual risk and ownership before closure to ensure
    accountability and transparency.

Implementing these best practices fosters a culture of thoroughness and
diligence in V&V activities.

## Heuristics 🧠

-   If a domain hazard is untested, confidence is provisional;
    prioritize testing to enhance assurance.
-   If rerun differs unexpectedly, investigate determinism first to
    identify potential issues.
-   If evidence is indirect, reduce verdict confidence level to reflect
    uncertainty in the findings.

These heuristics serve as guiding principles for effective
decision-making during the V&V process.

## Checklist ✅

::: note
::: title
Note
:::

Ensure all items are checked before proceeding to the next phase.
:::

-   \[ \] Domain hazard coverage is explicit.
-   \[ \] Compliance references are mapped to evidence.
-   \[ \] Nominal/boundary/fault results are all documented.
-   \[ \] Residual risks and next actions are assigned.

## GIVEN / WHEN / THEN Scenarios 📋

-   **Nominal (🟢)**:
    -   **GIVEN** the system is operating under normal conditions,
    -   **WHEN** the adaptive cruise control is activated,
    -   **THEN** the vehicle maintains a safe distance from the vehicle
        ahead.
-   **Boundary (🟡)**:
    -   **GIVEN** the vehicle is in a stop-and-go traffic situation,
    -   **WHEN** the headway is less than 1 meter,
    -   **THEN** the system should respond within 100 milliseconds to
        avoid collision.
-   **Fault (🔴)**:
    -   **GIVEN** a sensor dropout occurs,
    -   **WHEN** an invalid CAN frame is injected,
    -   **THEN** the system should enter a safe state to prevent
        unintended acceleration.

::: important
::: title
Important
:::

Remember to refer to the relevant domain standards (ISO 26262, ISO
21434) throughout the verification process to ensure compliance and
safety in automotive systems.
:::

::: note
::: title
Note
:::

**Mnemonic for V&V in Automotive: SAFE**
:::

-   **S**afety
-   **A**ccountability
-   **F**unctionality
-   **E**vidence

This mnemonic encapsulates the core principles of our verification and
validation efforts, reminding us to prioritize safety, maintain
accountability, ensure functionality, and provide robust evidence
throughout the process.

::: note
::: title
Note
