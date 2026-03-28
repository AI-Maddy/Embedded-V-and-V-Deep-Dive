---
title: "theory part1"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# Theory --- Day02 Traceability and Test Design 🌟

## Learning Goal 🎯

**Mnemonic: TRACE** **T**est designs **R**obustly **A**ligned to
**C**hangeable **E**vidence

The primary goal is to construct test designs that are: - **Traceable**:
Directly linked to requirements. - **Robust**: Resilient to requirement
changes and system evolution. - **Comprehensive**: Cover nominal,
boundary, and fault scenarios.

::: note
::: title
Note
:::

This aligns with industry standards such as **DO-178C** (Software
Considerations in Airborne Systems) and **ISO 26262** (Functional Safety
for Road Vehicles).
:::

## Traceability Principles 🔗

Traceability ensures every requirement is verified and no test is
orphaned.

-   **Forward Trace**: Requirement → Test/Design/Artifact.
-   **Backward Trace**: Artifact/Verdict → Originating Requirement.
-   **Bidirectional Trace**: Reduces audit and regression risks.

::: important
::: title
Important
:::

According to **ARP4754A**, bidirectional traceability is critical for
ensuring system-level requirements are met and verified across all
development phases.
:::

## Test Design Depth 🧪

Test design must address **three key dimensions**:

-   **Nominal Tests 🟢**: Validate intended behavior under normal
    conditions.
-   **Boundary Tests 🟡**: Assess system sensitivity to edge cases and
    limits.
-   **Negative/Fault Tests 🔴**: Confirm safe degradation and recovery
    mechanisms.

**Scenario Templates**:

  **Scenario Type**   **GIVEN**                                      **WHEN**                                      **THEN**
  ------------------- ---------------------------------------------- --------------------------------------------- ----------------------------------------------------
  Nominal 🟢          System is operating under normal conditions.   A valid input is provided.                    The system produces the expected output.
  Boundary 🟡         System is operating near its limits.           An edge-case input is provided.               The system handles the input without failure.
  Fault 🔴            System encounters an error condition.          An invalid or unexpected input is provided.   The system degrades gracefully or recovers safely.

  : Test Design Scenarios

## Review Triggers 🔍

Review processes must identify critical issues early.

-   **Requirement Change 🟡**: A requirement changes without
    corresponding test updates.
-   **Orphaned Tests 🔴**: A test exists without linkage to any
    requirement.
-   **Undefined Criteria 🟡**: Pass/fail thresholds are missing or
    unclear.

::: warning
::: title
Warning
:::

Unlinked tests or missing thresholds can lead to **audit failures**
under standards such as **ASPICE** and **IEC 62304**.
:::

## Deliverable Expectations 📦

Key deliverables for MIL traceability and test design include:

-   **Traceability Matrix Baseline**: Mapping requirements to tests and
    artifacts.
-   **Scenario Set**: Comprehensive test cases with coverage rationale.
-   **Gap List**: Identification of unverified requirements.

::: admonition
Standards Alignment Ensure deliverables meet the traceability
requirements of **DO-254** (Design Assurance Guidance for Airborne
Electronic Hardware) and **ISO 26262**.
:::

## Pre-Review Checklist ✅

Use this checklist to ensure readiness for review:
