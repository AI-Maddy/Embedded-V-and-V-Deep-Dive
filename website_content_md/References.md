# References

-   ISO 26262:2018 - Road vehicles \-- Functional safety
-   ISO 21434:2020 - Road vehicles \-- Cybersecurity engineering
-   DO-178C:2012 - Software considerations in airborne systems and
    equipment certification
-   DO-254:2010 - Design assurance guidance for airborne electronic
    hardware
-   ARP4754A:2010 - Guidelines for development of civil aircraft and
    systems
-   ARP4761:2010 - Guidelines and methods for conducting the failure
    modes, effects and criticality analysis (FMECA) of a system
-   IEC 62304:2006 - Medical device software \-- Software life cycle
    processes
-   IEC 60601:2005 - Medical electrical equipment \-- Part 1: General
    requirements for basic safety and essential performance
-   ISO 14971:2019 - Medical devices \-- Application of risk management
    to medical devices

::: note
::: title
Note
:::

This cheat sheet is intended to provide a quick reference for embedded
systems verification and validation. It is not a comprehensive guide and
should be used in conjunction with relevant domain standards and
guidelines.
:::

::: warning
::: title
Warning
:::

Failure to follow domain standards and guidelines may result in
non-compliance and potential safety risks.
:::

::: important
::: title
Important
:::

This cheat sheet is subject to change and may not reflect the latest
updates to domain standards and guidelines.
:::

::: admonition
This cheat sheet is intended for informational purposes only and should
not be used as a substitute for professional advice or guidance.
:::

Table of Evidence Expectations
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

| Evidence Type \| Description \| Priority \|
| \-\-- \| \-\-- \| \-\-- \|
| Requirement Traceability \| Trace requirements from system intent to
  test verdict \| 🟢 \|
| Verification Artifacts \| Verification artifacts with timestamps, tool
  versions, and ownership \| 🟢 \|
| Defect Triage History \| Track failed/blocked tests to corrective
  action \| 🟡 \|
| Baseline-First Comparison \| Compare changes against baseline \| 🟡 \|
| Fixed Acceptance Thresholds \| Establish clear acceptance thresholds
  \| 🟡 \|
| Deterministic Reruns \| Ensure repeatable and reliable tests \| 🟢 \|

Table of Patterns and Anti-Patterns
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

| Pattern/Anti-Pattern \| Description \| Priority \|
| \-\-- \| \-\-- \| \-\-- \|
| Baseline-First Comparison \| Compare changes against baseline \| 🟡 \|
| Fixed Acceptance Thresholds \| Establish clear acceptance thresholds
  \| 🟡 \|
| Deterministic Reruns \| Ensure repeatable and reliable tests \| 🟢 \|
| Post-Hoc Threshold Tuning \| Avoid adjusting thresholds after the fact
  \| 🔴 \|
| Missing Raw Artifacts \| Ensure all raw artifacts are available \| 🔴
  \|
| Incomplete Negative-Path Checks \| Ensure all negative paths are
  tested \| 🔴 \|
