Worked Example — Day30 Final Capstone 🎉
=====================================

🔍 Domain-Specific Mnemonic Acronym
------------------------------------

**HIL** - Hardware-in-the-Loop

🟢🟡🔴 Severity / Priority Colour Legend
------------------------------------------

| Severity | Priority | Colour |
| --- | --- | --- |
| Critical | High | 🔴 |
| Major | Medium | 🟡 |
| Minor | Low | 🟢 |

📝 Scenario Template
--------------------

### Nominal Scenario 🟢

* GIVEN: Representative nominal operation for this day topic.
* WHEN: Run the nominal scenario.
* THEN: Record baseline outputs.

### Boundary Scenario 🟡

* GIVEN: Boundary condition near timing/value/mode limits.
* WHEN: Run the boundary variant.
* THEN: Capture divergences.

### Fault Scenario 🔴

* GIVEN: Fault/negative stimulus with expected detection and recovery.
* WHEN: Run the fault variant.
* THEN: Validate safe handling/recovery.

📝 Procedure
-------------

### Step 1: Run Nominal Scenario 🟢

1. Run the nominal scenario and record baseline outputs.

### Step 2: Run Boundary Variant 🟡

1. Run the boundary variant and capture divergences.

### Step 3: Run Fault Variant 🔴

1. Run the fault variant and validate safe handling/recovery.

### Step 4: Repeat Key Run 🟢

1. Repeat the key run to confirm repeatability.

📝 Patterns
------------

### Compare Every Stressed Run Against a Baseline Artifact 🟢

* Compare every stressed run against a baseline artifact.

### Keep Pass/Fail Logic Requirement-Driven, Not Tool-Driven 🟢

* Keep pass/fail logic requirement-driven, not tool-driven.

### Separate Observation from Interpretation in Reports 🟢

* Separate observation from interpretation in reports.

🚫 Anti-Patterns
----------------

### Tuning Thresholds After Seeing Failing Results 🔴

* Avoid tuning thresholds after seeing failing results.

### Mixing Multiple Uncontrolled Changes in One Run 🔴

* Avoid mixing multiple uncontrolled changes in one run.

### Summarizing Outcomes Without Raw Evidence Pointers 🔴

* Avoid summarizing outcomes without raw evidence pointers.

⚠️ Pitfalls
------------

### Hidden Dependencies in Setup Scripts 🔴

* Be aware of hidden dependencies in setup scripts.

### Missing Failure Classification Severity 🔴

* Ensure failure classification severity is not missing.

### Incomplete Handoff Notes for Unresolved Issues 🔴

* Ensure incomplete handoff notes for unresolved issues are addressed.

📚 Examples
-----------

### Example 1: Nominal Pass with Complete Traceability Chain 🟢

* Example 1: Nominal pass with complete traceability chain.

### Example 2: Boundary Fail Revealing Timing Jitter Limit Breach 🟡

* Example 2: Boundary fail revealing timing jitter limit breach.

### Example 3: Fault Recovery Success with Documented Residual Risk 🟢

* Example 3: Fault recovery success with documented residual risk.

✅ Best Practices
----------------

### Keep Rerun Steps Deterministic 🟢

* Keep rerun steps deterministic.

### Store Artifacts with Version/Time Metadata 🟢

* Store artifacts with version/time metadata.

### Review Findings with Risk Owner Before Closure 🟢

* Review findings with risk owner before closure.

🧪 Heuristics
-------------

### If Rerun Differs Unexpectedly, Treat as Investigation Trigger 🟡

* If rerun differs unexpectedly, treat as investigation trigger.

### If Claim Lacks Artifact, Downgrade Confidence 🟡

* If claim lacks artifact, downgrade confidence.

### If Risk is Unresolved, Status Cannot be Final Pass 🔴

* If risk is unresolved, status cannot be final pass.

☐ Pre-Review Checklist
----------------------

☐ Functional, timing, robustness evidence captured.
☐ Requirement-linked verdict table completed.
☐ Residual risk and next actions documented.

🔎 Phase Focus Note
------------------

This day emphasizes: **real-time integration behavior, interface timing, and hardware realism**.

References
----------

* ARP4754A/4761: Guidelines and Methods for Conducting the Safety Assessment Process on Civil Aircraft and Complex Systems
* ASPICE: Automotive SPICE Process Assessment and Improvement for Embedded Systems
* DO-178C: Software Considerations in Airborne Systems and Equipment Certification
* DO-254: Design Assurance Guidance for Airborne Electronic Hardware
* IEC 62304: Medical Device Software - Software Life Cycle Processes
* ISO 26262: Road Vehicles - Functional Safety

Note
----

This document is intended to provide a comprehensive guide to the HIL exercise for Day30 Final Capstone. The content is based on the domain-specific mnemonic acronym **HIL** and the severity/priority colour legend. The document includes a scenario template, procedure, patterns, anti-patterns, pitfalls, examples, best practices, heuristics, and a pre-review checklist. The document also includes references to relevant domain standards.
