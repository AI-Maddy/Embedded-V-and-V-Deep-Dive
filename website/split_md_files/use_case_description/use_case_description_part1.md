# 🌟 Description --- Medical

## 🎯 Purpose

Document **Medical**-specific details for Day01 VModel and Requirements
with focus on use-case intent, assumptions, and acceptance criteria.

## 🔗 Domain Alignment

-   **Standard References**:
    -   IEC 62304 (Medical Device Software Lifecycle Processes)
    -   ISO 14971 (Risk Management for Medical Devices)
    -   IEC 60601 (Medical Electrical Equipment Safety)
-   **Critical Hazards**:
    -   Incorrect dosage delivery 🟡
    -   Missed alarm 🔴
    -   Unsafe therapy continuation 🟢
-   **Relevant Interfaces**:
    -   Device buses 🟢
    -   Sensor links 🟡
    -   Alarm/event channels 🔴

## 📖 Examples

**Nominal Scenario** 🟢 GIVEN validated sensor feedback WHEN therapy
control is initiated THEN the system delivers therapy within specified
parameters.

**Boundary Scenario** 🟡 GIVEN a near-threshold dosing configuration
WHEN alarm escalation timing is triggered THEN the system ensures proper
alarm activation without delay.

**Fault Scenario** 🔴 GIVEN a sensor spike/dropout or actuator command
rejection WHEN the system detects an anomaly THEN it halts therapy and
raises a critical alarm.

## 🔍 Patterns

-   **Requirement-Linked Checks**: Ensure every scenario is tied to
    specific requirements.
-   **Timing and Functional Outcomes**: Simultaneously track timing
    behavior and functional correctness.
-   **Reproducibility Constraints**: Explicitly define setup conditions
    for repeatable tests.

## 🚫 Anti-Patterns

-   **Domain-Agnostic Statements**: Avoid generic claims without
    measurable criteria.
-   **Interface Constraints Ignored**: Always analyze interface timing
    and data integrity.
-   **Unresolved Risks**: Do not close findings without a residual risk
    statement.

## ⚠️ Pitfalls

-   **Sensor/Actuator Fault Variants**: Missing coverage for edge cases.
-   **Weak Traceability**: Ensure objectives are clearly linked to
    artifacts.
-   **Configuration Drift**: Prevent non-repeatable reruns due to
    uncontrolled setup changes.

## ✅ Pre-Review Checklist

☐ Scope and assumptions are explicit. ☐ Acceptance criteria are
quantitative and measurable. ☐ Evidence set is complete and auditable. ☐
Follow-up actions are prioritized and documented. ☐ Residual risks are
captured with ownership and next steps.

## 💡 Additional Deep-Dive Notes

::: note
::: title
Note
:::

**Domain Focus**: Medical **Phase Focus**: MIL (Model-in-the-Loop)
:::

::: important
::: title
Important
:::

**Evidence Priorities**: - Functional correctness 🟢 - Timing behavior
🟡 - Robustness 🔴 - Traceability 🟢
:::

::: admonition
Patterns to Follow - Baseline-first comparison methodology. - Fixed
acceptance thresholds for predictable outcomes. - Deterministic reruns
to ensure repeatability.
:::

::: warning
::: title
Warning
:::

**Anti-Patterns**: - Post-hoc threshold tuning 🟡 - Missing raw
