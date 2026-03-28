---
title: "Severity Priority Legend"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 🟢🟡🔴 Severity / Priority Legend 🔍


  : Severity / Priority Legend

🔍 Why This Tool Matters 🔍
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Use this tool for **instruction trace, object-code debug, and timing
evidence**. This tool is crucial for ensuring the reliability and
performance of embedded systems.

::: note
::: title
Note
:::

The use of TRACE32 is a key aspect of the V&V process, as it provides a
comprehensive view of system behavior.
:::

🔍 **TRACE** Domain-Specific Mnemonic Acronym 🔍
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

TRACE stands for **T**iming **R**eliability **A**ssessment
**C**onfirmation **E**valuation.

🔩 Setup Baseline 🔩 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\### GIVEN 🟢

-   Tool version
-   Project/profile
-   Interface mapping

\### WHEN 🟡

-   Define trigger points
-   Set logging granularity

\### THEN 🔴

-   Validate synchronization source before formal runs

🔍 Execution Pattern 🔍 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\### Nominal Scenario 🟢

1.  Run nominal scenario and store baseline artifacts.

\### Boundary Scenario 🟡

2.  Inject edge/fault conditions relevant to day objective.

\### Fault Scenario 🔴

3.  Re-run with controlled variation to confirm repeatability.
4.  Summarize deltas and risk implications.

📊 Key Metrics 📊 \-\-\-\-\-\-\-\-\-\-\-\-\--


  : Key Metrics

✅ Deliverables ✅ \-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   Configuration snapshot
-   Raw capture/trace/log files
-   Analyst summary with verdict
-   Follow-up action tracker

🔍 Quality Controls 🔍 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

-   Scenario-to-requirement traceability verified
-   Artifact naming/versioning consistency enforced
-   Review notes include residual risk and next experiment

🔎 Review Criteria 🔎 \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\### Severity Legend


  : Severity Legend

-   Is evidence reproducible across reruns?
-   Are anomalies linked to objective requirements?
-   Is residual risk clearly described?

Additional Deep-Dive Notes 🔍
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\### Domain Focus

-   Embedded systems

\### Phase Focus

-   V&V

\### Evidence Priorities

-   Functional correctness
-   Timing behavior
-   Robustness
-   Traceability

\### Patterns

-   Baseline-first comparison
-   Fixed acceptance thresholds
-   Deterministic reruns

\### Anti-Patterns

-   Post-hoc threshold tuning
-   Missing raw artifacts
-   Incomplete negative-path checks

\### Pitfalls

-   Hidden assumptions
-   Interface timing drift
-   Weak requirement-to-test linkage

\### Example Expansion

-   Include one nominal, one boundary, and one fault scenario per
    objective

\### Review Heuristic

-   If a claim cannot be tied to an artifact, mark confidence as
    provisional

\### Checklist Extension

-   Capture residual risk
-   Ownership
-   Next action for each unresolved item

Pre-Review Checklist ☐ \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

☐ Review scope and objectives ☐ Verify scenario-to-requirement
traceability ☐ Ensure artifact naming/versioning consistency ☐ Review
notes include residual risk and next experiment ☐ Verify deliverables ☐
Review criteria met

References 📚 \-\-\-\-\-\-\-\-\--

-   ARP4754A/4761: Guidelines and Methods for Conducting the Safety
    Assessment Process on Commercial Off-The-Shelf (COTS) Software
-   ASPICE: Automotive Spice
-   DO-178C: Software Considerations in Airborne Systems and Equipment
    Certification
-   DO-254: Design Assurance Guidance for Airborne Electronic Hardware
-   IEC 62304: Medical device software - Software life cycle processes
-   ISO 26262: Road vehicles - Functional safety

GIVEN / WHEN / THEN Scenario Templates 📝
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\### Nominal Scenario 🟢


  : Nominal Scenario

\### Boundary Scenario 🟡


  : Boundary Scenario

\### Fault Scenario 🔴


  : Fault Scenario

::: {.admonition .checklist header="Checklist"}
V&V Checklist

☐ Review scope and objectives ☐ Verify scenario-to-requirement
traceability ☐ Ensure artifact naming/versioning consistency ☐ Review
notes include residual risk and next experiment ☐ Verify deliverables ☐
Review criteria met
:::

::: important
::: title
Important
:::

Review the V&V phase checklist and ensure all items are met.
:::
