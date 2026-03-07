Automotive Use Cases and Examples 🚗💻
=====================================

Purpose 📝
---------

Provide domain-tailored use cases with evidence expectations aligned to **ISO 26262 (ASIL) + ISO 21434** 📚.

Representative Use Cases 📊
---------------------------

### Nominal Mission/Profile Operation 🟢

.. note:: This scenario represents the normal operating conditions of the system.

.. important:: Ensure that the system is functioning as expected in nominal conditions.

*   Given: normal traffic conditions
*   When: adaptive cruise control is engaged
*   Then: speed regulation is maintained within acceptable limits

### Boundary-Condition Operation Near Limits 🟡

.. warning:: This scenario represents the boundary conditions of the system.

.. important:: Ensure that the system is functioning as expected near the limits of its operating conditions.

*   Given: dense stop-and-go traffic with tight headway and timing limits
*   When: adaptive cruise control is engaged
*   Then: speed regulation is maintained within acceptable limits, but near the boundary of acceptable behavior

### Fault Detection, Containment, and Recovery 🔴

.. admonition:: This scenario represents a fault condition in the system.

.. important:: Ensure that the system is functioning as expected in fault conditions.

*   Given: sensor dropout and invalid CAN frame injection
*   When: adaptive cruise control is engaged
*   Then: fault detection and containment mechanisms are triggered, and recovery is successful

### Degraded-Mode Continuation with Safety Constraints 🟢

.. note:: This scenario represents the degraded mode of the system.

.. important:: Ensure that the system is functioning as expected in degraded mode.

*   Given: reduced system functionality due to hardware failure
*   When: adaptive cruise control is engaged
*   Then: degraded-mode operation is maintained within safety constraints

### Regression Stability after Fixes 🟡

.. warning:: This scenario represents the regression stability of the system after fixes.

.. important:: Ensure that the system is functioning as expected after fixes.

*   Given: multiple fixes applied to the system
*   When: adaptive cruise control is engaged
*   Then: regression stability is ensured, and no new faults are introduced

Domain-Specific Mnemonic Acronym: **ADAS** (Advanced Driver Assistance Systems)

Domain-Specific Examples 📚
---------------------------

### Example A (Nominal): Adaptive Cruise and Speed Regulation under Normal Traffic 🟢

.. important:: This example represents the normal operating conditions of the system.

*   Given: normal traffic conditions
*   When: adaptive cruise control is engaged
*   Then: speed regulation is maintained within acceptable limits

### Example B (Boundary): Dense Stop-and-Go with Tight Headway and Timing Limits 🟡

.. warning:: This example represents the boundary conditions of the system.

*   Given: dense stop-and-go traffic with tight headway and timing limits
*   When: adaptive cruise control is engaged
*   Then: speed regulation is maintained within acceptable limits, but near the boundary of acceptable behavior

### Example C (Fault): Sensor Dropout and Invalid CAN Frame Injection 🔴

.. admonition:: This example represents a fault condition in the system.

*   Given: sensor dropout and invalid CAN frame injection
*   When: adaptive cruise control is engaged
*   Then: fault detection and containment mechanisms are triggered, and recovery is successful

Patterns 📝
----------

### Map Each Scenario to Requirement and Hazard Identifiers

.. note:: This pattern ensures that each scenario is mapped to the corresponding requirement and hazard identifiers.

*   Map each scenario to the corresponding requirement and hazard identifiers
*   Use a consistent mapping approach across all scenarios

### Use One Baseline Artifact Set for Comparison Across Variants

.. important:: This pattern ensures that a single baseline artifact set is used for comparison across all variants.

*   Use a single baseline artifact set for comparison across all variants
*   Ensure that the baseline artifact set is consistent and reproducible

### Preserve Raw Captures Alongside Interpreted Findings

.. note:: This pattern ensures that raw captures are preserved alongside interpreted findings.

*   Preserve raw captures alongside interpreted findings
*   Use a consistent naming convention for raw captures and interpreted findings

Anti-Patterns 🚫
--------------

### Broad “Pass” Claims without Scenario-Level Evidence

.. warning:: This anti-pattern represents making broad “pass” claims without scenario-level evidence.

*   Avoid making broad “pass” claims without scenario-level evidence
*   Provide explicit evidence for each scenario

### Missing Boundary/Fault Test Depth for High-Risk Functions

.. admonition:: This anti-pattern represents missing boundary and fault test depth for high-risk functions.

*   Ensure that boundary and fault test depth is sufficient for high-risk functions
*   Use a risk-based approach to determine test depth requirements

### Compliance References without Concrete Verification Links

.. important:: This anti-pattern represents compliance references without concrete verification links.

*   Provide concrete verification links for compliance references
*   Use a consistent naming convention for compliance references and verification links

Pitfalls 🚨
---------

### Underestimating Interface Timing Effects

.. warning:: This pitfall represents underestimating interface timing effects.

*   Avoid underestimating interface timing effects
*   Use a timing analysis tool to determine interface timing effects

### Incomplete Alarm/Fallback Path Verification

.. admonition:: This pitfall represents incomplete alarm and fallback path verification.

*   Ensure that alarm and fallback path verification is complete
*   Use a consistent naming convention for alarm and fallback paths

### Weak Ownership for Unresolved Risks

.. note:: This pitfall represents weak ownership for unresolved risks.

*   Assign clear ownership for unresolved risks
*   Use a risk-based approach to determine ownership requirements

Best Practices 📚
----------------

### Keep Scenario Definitions Deterministic and Reproducible

.. important:: This best practice ensures that scenario definitions are deterministic and reproducible.

*   Use a deterministic approach to define scenario definitions
*   Ensure that scenario definitions are reproducible

### Use Quantitative Pass/Fail Thresholds

.. note:: This best practice ensures that quantitative pass/fail thresholds are used for scenario evaluation.

*   Use quantitative pass/fail thresholds for scenario evaluation
*   Ensure that pass/fail thresholds are consistent and reproducible

### Review Residual Risk before Release Recommendation

.. admonition:: This best practice ensures that residual risk is reviewed before making a release recommendation.

*   Review residual risk before making a release recommendation
*   Use a risk-based approach to determine release requirements

Checklist 📝
------------

### Nominal/Boundary/Fault Scenarios are Covered ☐

*   Ensure that nominal, boundary, and fault scenarios are covered
*   Use a consistent naming convention for scenario types

### Evidence is Traceable and Auditable ☐

*   Ensure that evidence is traceable and auditable
*   Use a consistent naming convention for evidence types

### Compliance Mapping is Explicit ☐

*   Ensure that compliance mapping is explicit
*   Use a consistent naming convention for compliance references

### Open Issues include Priority and Owner ☐

*   Ensure that open issues include priority and owner
*   Use a consistent naming convention for open issues

Additional Deep-Dive Notes 📝
---------------------------

### Domain Focus: Automotive

*   The domain focus is automotive
*   Use a consistent naming convention for domain-specific terms

### Phase Focus: Cross-Phase

*   The phase focus is cross-phase
*   Use a consistent naming convention for phase-specific terms

### Evidence Priorities: Functional Correctness, Timing Behavior, Robustness, and Traceability

*   The evidence priorities are functional correctness, timing behavior, robustness, and traceability
*   Use a consistent naming convention for evidence priorities

### Patterns: Baseline-First Comparison, Fixed Acceptance Thresholds, Deterministic Reruns

*   The patterns are baseline-first comparison, fixed acceptance thresholds, and deterministic reruns
*   Use a consistent naming convention for patterns

### Anti-Patterns: Post-Hoc Threshold Tuning, Missing Raw Artifacts, Incomplete Negative-Path Checks

*   The anti-patterns are post-hoc threshold tuning, missing raw artifacts, and incomplete negative-path checks
*   Use a consistent naming convention for anti-patterns

### Pitfalls: Hidden Assumptions, Interface Timing Drift, Weak Requirement-to-Test Linkage

*   The pitfalls are hidden assumptions, interface timing drift, and weak requirement-to-test linkage
*   Use a consistent naming convention for pitfalls

### Example Expansion: Include One Nominal, One Boundary, and One Fault Scenario per Objective

*   Include one nominal, one boundary, and one fault scenario per objective
*   Use a consistent naming convention for scenario types

### Review Heuristic: If a Claim Cannot be Tied to an Artifact, Mark Confidence as Provisional

*   Use a review heuristic to mark confidence as provisional if a claim cannot be tied to an artifact
*   Use a consistent naming convention for review heuristics

### Checklist Extension: Capture Residual Risk, Ownership, and Next Action for Each Unresolved Item

*   Capture residual risk, ownership, and next action for each unresolved item
*   Use a consistent naming convention for checklist extensions

Severity/Priority Colour Legend:
🟢 Nominal
🟡 Boundary
🔴 Fault

ARP4754A/4761, ASPICE, DO-178C, DO-254, IEC 62304, ISO 26262, ISO 21434
