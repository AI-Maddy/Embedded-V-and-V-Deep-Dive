---
title: "traceability matrix"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---



  : Recommended Columns

## 📚 Usage Rules 📖

::: important
::: title
Important
:::

No test scenario without requirement reference.
:::

::: important
::: title
Important
:::

No requirement marked complete without evidence artifact.
:::

::: important
::: title
Important
:::

Any requirement change triggers matrix review.
:::

## 🔍 Quick Audit Checks 🔎

::: admonition
Are failed tests linked to corrective actions?
:::

::: admonition
Are all critical requirements covered by at least one negative-path
test?
:::

::: admonition
Are artifact links still valid and reproducible?
:::

## 📝 GIVEN / WHEN / THEN Scenario Templates 📊

\### Nominal Scenario 🟢

-   GIVEN: A requirement with a criticality level of High
-   WHEN: The test scenario is executed with nominal inputs
-   THEN: The test scenario passes, and the evidence artifact is
    generated

\### Boundary Scenario 🟡

-   GIVEN: A requirement with a criticality level of Medium
-   WHEN: The test scenario is executed with boundary inputs
-   THEN: The test scenario passes, and the evidence artifact is
    generated

\### Fault Scenario 🔴

-   GIVEN: A requirement with a criticality level of Low
-   WHEN: The test scenario is executed with fault inputs
-   THEN: The test scenario fails, and the issue is reported

## 📝 Pre-Review Checklist 📊

☐ Are all requirements tied to test scenarios? ☐ Are all test scenarios
linked to evidence artifacts? ☐ Are all evidence artifacts reproducible?
☐ Are all critical requirements covered by at least one negative-path
test? ☐ Are all failed tests linked to corrective actions?

## 📝 Additional Deep-Dive Notes 📊

::: note
::: title
Note
:::

Domain Focus: General
:::

::: note
::: title
Note
:::

Phase Focus: MIL
:::

::: note
::: title
Note
:::

Evidence Priorities: functional correctness, timing behavior,
robustness, and traceability.
:::

::: note
::: title
Note
:::

deterministic reruns.
:::

::: warning
::: title
Warning
:::

incomplete negative-path checks.
:::

::: important
::: title
Important
:::

requirement-to-test linkage.
:::

::: admonition
Example Expansion: include one nominal, one boundary, and one fault
scenario per objective.
:::

::: note
::: title
Note
:::

Review Heuristic: if a claim cannot be tied to an artifact, mark
confidence as provisional.
:::

::: note
::: title
Note
:::

Checklist Extension: capture residual risk, ownership, and next action
for each unresolved item.
:::
