---
title: "GIVEN   WHEN   THEN Scenarios"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# GIVEN / WHEN / THEN Scenarios 📋

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
:::

By adhering to the SAFE principles, we can enhance the quality and
reliability of automotive systems, ultimately ensuring a safer driving
experience for all.
:::

::: important
::: title
Important
:::

**Severity / Priority Legend**
:::

-   🟢 **Green**: Nominal scenarios with expected outcomes.
-   🟡 **Yellow**: Boundary scenarios that test limits.
-   🔴 **Red**: Fault scenarios that simulate failures.

This legend serves as a quick reference for assessing the criticality of
various scenarios and their implications on safety and compliance.
