.. _TRACE32:

TRACE32
================

🔍 **TRACE**: **T**iming **R**eliability **A**ssessment **C**onfirmation **E**valuation
=====================

🟢🟡🔴 Severity / Priority Legend
--------------------------------

| Color | Severity | Priority |
| --- | --- | --- |
| 🟢 | Nominal | High |
| 🟡 | Boundary | Medium |
| 🔴 | Fault | Low |

🔍 Why This Tool Matters
------------------------

Use this tool for **instruction trace, object-code debug, and timing evidence**. This tool is crucial for ensuring the reliability and performance of embedded systems.

.. note::
    The use of TRACE32 is a key aspect of the V&V process, as it provides a comprehensive view of system behavior.

🔍 **TRACE** Domain-Specific Mnemonic Acronym
-----------------------------------------

TRACE stands for **T**iming **R**eliability **A**ssessment **C**onfirmation **E**valuation.

🔩 Setup Baseline
-----------------

### Given 🟢

* Tool version
* Project/profile
* Interface mapping

### When 🟡

* Define trigger points
* Set logging granularity

### Then 🔴

* Validate synchronization source before formal runs

🔍 Execution Pattern
--------------------

### Nominal Scenario 🟢

1. Run nominal scenario and store baseline artifacts.

### Boundary Scenario 🟡

2. Inject edge/fault conditions relevant to day objective.

### Fault Scenario 🔴

3. Re-run with controlled variation to confirm repeatability.

4. Summarize deltas and risk implications.

📊 Key Metrics
--------------

| Metric | Description | Priority |
| --- | --- | --- |
| Execution-path confidence | Confidence in the execution path of the system | 🟢 |
| WCET evidence | Worst-case execution time evidence | 🟡 |
| Breakpoint determinism | Determinism of breakpoint behavior | 🔴 |

✅ Deliverables
---------------

* Configuration snapshot
* Raw capture/trace/log files
* Analyst summary with verdict
* Follow-up action tracker

🔍 Quality Controls
-------------------

* Scenario-to-requirement traceability verified
* Artifact naming/versioning consistency enforced
* Review notes include residual risk and next experiment

🔎 Review Criteria
------------------

### Severity Legend

| Color | Severity | Priority |
| --- | --- | --- |
| 🟢 | Nominal | High |
| 🟡 | Boundary | Medium |
| 🔴 | Fault | Low |

* Is evidence reproducible across reruns?
* Are anomalies linked to objective requirements?
* Is residual risk clearly described?

Additional Deep-Dive Notes
-------------------------

### Domain Focus

* Embedded systems

### Phase Focus

* V&V

### Evidence Priorities

* Functional correctness
* Timing behavior
* Robustness
* Traceability

### Patterns

* Baseline-first comparison
* Fixed acceptance thresholds
* Deterministic reruns

### Anti-Patterns

* Post-hoc threshold tuning
* Missing raw artifacts
* Incomplete negative-path checks

### Pitfalls

* Hidden assumptions
* Interface timing drift
* Weak requirement-to-test linkage

### Example Expansion

* Include one nominal, one boundary, and one fault scenario per objective

### Review Heuristic

* If a claim cannot be tied to an artifact, mark confidence as provisional

### Checklist Extension

* Capture residual risk
* Ownership
* Next action for each unresolved item

Pre-Review Checklist
--------------------

☐ Review scope and objectives
☐ Verify scenario-to-requirement traceability
☐ Ensure artifact naming/versioning consistency
☐ Review notes include residual risk and next experiment
☐ Verify deliverables
☐ Review criteria met

References
----------

* ARP4754A/4761: Guidelines and Methods for Conducting the Safety Assessment Process on Commercial Off-The-Shelf (COTS) Software
* ASPICE: Automotive Spice
* DO-178C: Software Considerations in Airborne Systems and Equipment Certification
* DO-254: Design Assurance Guidance for Airborne Electronic Hardware
* IEC 62304: Medical device software - Software life cycle processes
* ISO 26262: Road vehicles - Functional safety

Table: Key Metrics
================

| Metric | Description | Priority |
| --- | --- | --- |
| Execution-path confidence | Confidence in the execution path of the system | 🟢 |
| WCET evidence | Worst-case execution time evidence | 🟡 |
| Breakpoint determinism | Determinism of breakpoint behavior | 🔴 |

.. admonition:: V&V Checklist
   :class: checklist
   :header: Checklist

   ☐ Review scope and objectives
   ☐ Verify scenario-to-requirement traceability
   ☐ Ensure artifact naming/versioning consistency
   ☐ Review notes include residual risk and next experiment
   ☐ Verify deliverables
   ☐ Review criteria met

GIVEN / WHEN / THEN Scenario Templates
--------------------------------------

### Nominal Scenario 🟢

| Given | When | Then |
| --- | --- | --- |
| Tool version | Define trigger points | Validate synchronization source before formal runs |
| Project/profile | Set logging granularity | Store baseline artifacts |
| Interface mapping | Run nominal scenario | Verify execution-path confidence |

### Boundary Scenario 🟡

| Given | When | Then |
| --- | --- | --- |
| Tool version | Inject edge/fault conditions | Verify WCET evidence |
| Project/profile | Set logging granularity | Verify breakpoint determinism |
| Interface mapping | Run boundary scenario | Verify execution-path confidence |

### Fault Scenario 🔴

| Given | When | Then |
| --- | --- | --- |
| Tool version | Re-run with controlled variation | Verify WCET evidence |
| Project/profile | Set logging granularity | Verify breakpoint determinism |
| Interface mapping | Run fault scenario | Verify execution-path confidence |

V&V Phase Checklist
--------------------

☐ Review scope and objectives
☐ Verify scenario-to-requirement traceability
☐ Ensure artifact naming/versioning consistency
☐ Review notes include residual risk and next experiment
☐ Verify deliverables
☐ Review criteria met

V&V Phase Review Criteria
-------------------------

### Severity Legend

| Color | Severity | Priority |
| --- | --- | --- |
| 🟢 | Nominal | High |
| 🟡 | Boundary | Medium |
| 🔴 | Fault | Low |

* Is evidence reproducible across reruns?
* Are anomalies linked to objective requirements?
* Is residual risk clearly described?

V&V Phase Evidence Priorities
-----------------------------

* Functional correctness
* Timing behavior
* Robustness
* Traceability

V&V Phase Patterns
-----------------

* Baseline-first comparison
* Fixed acceptance thresholds
* Deterministic reruns

V&V Phase Anti-Patterns
----------------------

* Post-hoc threshold tuning
* Missing raw artifacts
* Incomplete negative-path checks

V&V Phase Pitfalls
-----------------

* Hidden assumptions
* Interface timing drift
* Weak requirement-to-test linkage

V&V Phase Example Expansion
---------------------------

* Include one nominal, one boundary, and one fault scenario per objective

V&V Phase Review Heuristic
-------------------------

* If a claim cannot be tied to an artifact, mark confidence as provisional

V&V Phase Checklist Extension
-----------------------------

* Capture residual risk
* Ownership
* Next action for each unresolved item

Table: V&V Phase Key Metrics
=============================

| Metric | Description | Priority |
| --- | --- | --- |
| Execution-path confidence | Confidence in the execution path of the system | 🟢 |
| WCET evidence | Worst-case execution time evidence | 🟡 |
| Breakpoint determinism | Determinism of breakpoint behavior | 🔴 |

.. admonition:: V&V Phase Review
   :class: important
   :header: Review

   Review the V&V phase checklist and ensure all items are met.

Table: V&V Phase Review Criteria
===============================

| Criteria | Description | Priority |
| --- | --- | --- |
| Evidence reproducibility | Is evidence reproducible across reruns? | 🟢 |
| Anomaly linkage | Are anomalies linked to objective requirements? | 🟡 |
| Residual risk | Is residual risk clearly described? | 🔴 |

Table: V&V Phase Evidence Priorities
=====================================

| Priority | Description |
| --- | --- |
| Functional correctness | Functional correctness is the highest priority. |
| Timing behavior | Timing behavior is the second-highest priority. |
| Robustness | Robustness is the third-highest priority. |
| Traceability | Traceability is the lowest priority. |

Table: V&V Phase Patterns
=========================

| Pattern | Description |
| --- | --- |
| Baseline-first comparison | Compare the baseline to the current implementation. |
| Fixed acceptance thresholds | Set acceptance thresholds and verify they are met. |
| Deterministic reruns | Run the test multiple times to ensure repeatability. |

Table: V&V Phase Anti-Patterns
=============================

| Anti-Pattern | Description |
| --- | --- |
| Post-hoc threshold tuning | Adjust thresholds after the fact. |
| Missing raw artifacts | Fail to capture raw artifacts. |
| Incomplete negative-path checks | Fail to check negative paths. |

Table: V&V Phase Pitfalls
=========================

| Pitfall | Description |
| --- | --- |
| Hidden assumptions | Make assumptions without verifying them. |
| Interface timing drift | Fail to account for timing drift. |
| Weak requirement-to-test linkage | Fail to link requirements to tests. |

Table: V&V Phase Example Expansion
=====================================

| Example | Description |
| --- | --- |
| Nominal scenario | Run a nominal scenario and store baseline artifacts. |
| Boundary scenario | Run a boundary scenario and verify WCET evidence. |
| Fault scenario | Run a fault scenario and verify execution-path confidence. |

Table: V&V Phase Review Heuristic
=====================================

| Heuristic | Description |
| --- | --- |
| Provisional confidence | Mark confidence as provisional if a claim cannot be tied to an artifact. |

Table: V&V Phase Checklist Extension
=====================================

| Checklist | Description |
| --- | --- |
| Residual risk | Capture residual risk and describe it clearly. |
| Ownership | Assign ownership to each unresolved item. |
| Next action | Describe the next action for each unresolved item. |
