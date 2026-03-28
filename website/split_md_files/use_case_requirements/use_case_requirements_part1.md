# 🩺 Requirements --- Medical 🩺

## 🎯 Purpose 🎯

Document **Medical**-specific details for Day02 Traceability and
TestDesign with focus on use-case intent, assumptions, and acceptance
criteria.

::: note
::: title
Note
:::

This document aligns with **Model-in-the-Loop (MIL)** phase objectives,
ensuring traceability and robust test design for medical systems per IEC
62304 and ISO 14971 guidelines.
:::

## 🌐 Domain Alignment 🌐

-   **Standards Reference**:
    -   IEC 62304: Software lifecycle processes
    -   ISO 14971: Risk management for medical devices
    -   IEC 60601: Safety and performance of medical electrical
        equipment
-   **Critical Hazards**:
    -   Incorrect dosage delivery 🔴
    -   Missed alarm 🟡
    -   Unsafe therapy continuation 🔴
-   **Relevant Interfaces**:
    -   Device buses 🟢
    -   Sensor links 🟡
    -   Alarm/event channels 🔴

::: important
::: title
Important
:::

Ensure all hazards are mitigated per IEC 62304 and ISO 14971 guidelines,
with traceable links to requirements and test artifacts.
:::

## 🧪 Examples 🧪

\### 🟢 Nominal Scenario 🟢

GIVEN validated sensor feedback WHEN therapy control is initiated THEN
the system delivers accurate therapy dosage within specified limits.

\### 🟡 Boundary Scenario 🟡

GIVEN near-threshold dosing conditions WHEN alarm escalation timing is
triggered THEN the system raises an alarm within the prescribed response
time.

\### 🔴 Fault Scenario 🔴

GIVEN a sensor spike/dropout WHEN an actuator command is issued THEN the
system rejects unsafe commands and logs the fault for further analysis.

## 📐 Patterns 📐

-   **Requirement-Linked Checks**:
    -   Ensure every test scenario is tied to a specific requirement.
-   **Timing and Functional Outcomes**:
    -   Track both timing behavior and functional correctness in test
        results.
-   **Setup Reproducibility**:
    -   Maintain explicit constraints for reproducible test setups.

## 🚫 Anti-Patterns 🚫

-   Domain-agnostic statements without measurable criteria.
-   Ignoring interface constraints during analysis.
-   Closing findings without residual risk statement.

⚠️ Pitfalls ⚠️ \-\-\-\-\-\-\-\-\-\-\-\--

-   Missing sensor/actuator fault variants 🔴
-   Weak traceability from objective to artifact 🟡
-   Non-repeatable reruns from uncontrolled configuration drift 🔴

## ✅ Checklist ✅

☐ Scope and assumptions are explicit. ☐ Acceptance criteria are
quantitative. ☐ Evidence set is complete and auditable. ☐ Follow-up
actions are prioritized. ☐ Residual risks are documented. ☐ Ownership
and next actions are assigned for unresolved items.

## 📘 Additional Deep-Dive Notes 📘

-   **Domain Focus**: Medical 🩺
-   **Phase Focus**: MIL 🧩
-   **Evidence Priorities**:
    -   Functional correctness 🟢
    -   Timing behavior 🟡
    -   Robustness 🔴
    -   Traceability 🟢
-   **Patterns**:
