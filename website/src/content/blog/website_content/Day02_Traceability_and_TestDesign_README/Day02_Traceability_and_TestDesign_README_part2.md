---
title: "Day02 Traceability and TestDesign README part2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

::: title
Warning
:::

Hidden assumptions in MIL tests can lead to **system-level failures**
during later phases. Ensure **IEC 62304 compliance** for medical devices
and **ISO 26262 Part 9** for automotive safety.
:::

## ✅ Required Deliverables 📂

-   **Scenario Matrix**: Objective mapping for all test cases.
-   **Raw Logs/Traces/Plots**: Timestamped and version-controlled.
-   **Requirement-Linked Verdict Summary**: Pass/fail results tied to
    requirements.
-   **Residual Risk List**: Document unresolved issues and next actions.

## 🔍 Reviewer Checklist ✅

-   [ ] Are pass/fail rules explicit and reproducible?
-   [ ] Is each key claim backed by a concrete artifact?
-   [ ] Are failures triaged with severity and owner?
-   [ ] Is handoff quality sufficient for the next phase?

::: admonition
Pre-Review Checklist - ☐ Verify traceability links for all test cases. -
☐ Confirm artifact completeness (logs, plots, etc.). - ☐ Validate
residual risk ownership and next actions.
:::

## 🧠 Mnemonic Acronym: TRACE 🌟

**T** - **Traceability**: Link every test to a requirement. **R** -
**Robustness**: Test edge cases and invalid inputs. **A** -
**Artifacts**: Ensure completeness and version control. **C** -
**Criteria**: Define explicit pass/fail thresholds. **E** -
**Evidence**: Consolidate results with traceability.

## GIVEN / WHEN / THEN Scenarios 🧪

-   **Nominal Scenario** 🟢 GIVEN a model configured with baseline
    assumptions, WHEN the nominal signal is applied, THEN the system
    meets requirement R1 with latency \< 10ms.
-   **Boundary Scenario** 🟡 GIVEN a model under high computational
    load, WHEN the signal approaches the jitter threshold, THEN the
    system meets requirement R2 with jitter \< 5ms.
-   **Fault Scenario** 🔴 GIVEN a model with invalid input, WHEN the
    signal exceeds the expected range, THEN the system violates
    requirement R3, and residual risk is logged.

## Additional Deep-Dive Notes 📘

-   **Domain Focus**: Embedded Systems
-   **Phase Focus**: MIL
-   **Evidence Priorities**: Functional correctness, timing behavior,
    robustness, and traceability.
-   **Patterns**: Baseline-first comparison, fixed acceptance
    thresholds, deterministic reruns.
-   **Anti-Patterns**: Post-hoc threshold tuning, missing raw artifacts,
    incomplete negative-path checks.
-   **Pitfalls**: Hidden assumptions, interface timing drift, weak
    requirement-to-test linkage.
-   **Example Expansion**: Include one nominal, one boundary, and one
    fault scenario per objective.
-   **Review Heuristic**: If a claim cannot be tied to an artifact, mark
    confidence as provisional.
-   **Checklist Extension**: Capture residual risk, ownership, and next
    action for each unresolved item.

::: note
::: title
Note
:::

For compliance with **ARP4761**, ensure safety analysis artifacts are
linked to MIL test results to validate system-level risk mitigation.
:::
