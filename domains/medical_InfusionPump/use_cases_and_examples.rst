Medical Infusion Pump Use Cases and Examples
==============================================

🟢 **Domain-Specific Mnemonic:** MIPUSE (Medical Infusion Pump Use Scenarios and Evidence)

Purpose
-------
🟢 **Nominal** (Expected Behavior) 🟡 **Boundary** (Edge Cases) 🔴 **Fault** (Error Conditions)
Provide domain-tailored use cases with evidence expectations aligned to **IEC 62304 + ISO 14971 + IEC 60601 context**.

Representative Use Cases
------------------------
### 1. Nominal Mission/Profile Operation 🟢

*   GIVEN: Infusion pump is calibrated and configured correctly.
*   WHEN: User initiates therapy control with validated sensor feedback.
*   THEN: Pump delivers accurate and consistent medication dosages.

### 2. Boundary-Condition Operation near Limits 🟡

*   GIVEN: Infusion pump is operating near its capacity limits (e.g., maximum flow rate).
*   WHEN: User attempts to initiate therapy control with near-threshold dosing.
*   THEN: Pump alerts user with timely and relevant alarm escalation.

### 3. Fault Detection, Containment, and Recovery 🔴

*   GIVEN: Infusion pump detects a sensor spike or dropout.
*   WHEN: Pump initiates actuator command rejection path.
*   THEN: Pump safely halts therapy and alerts user with error message.

### 4. Degraded-Mode Continuation with Safety Constraints 🟢

*   GIVEN: Infusion pump experiences a partial failure (e.g., reduced flow rate).
*   WHEN: User continues therapy with safety constraints in place.
*   THEN: Pump maintains safe and consistent medication delivery.

### 5. Regression Stability after Fixes 🟡

*   GIVEN: Infusion pump has undergone software updates or hardware modifications.
*   WHEN: User verifies therapy control with validated sensor feedback.
*   THEN: Pump demonstrates stable and accurate performance.

Domain-Specific Examples
------------------------
### Example A (Nominal) 🟢

*   Therapy control with validated sensor feedback.
*   Evidence: Pump calibration and configuration records.
*   Compliance: IEC 60601-1:2012, Clause 8.2.1.

### Example B (Boundary) 🟡

*   Near-threshold dosing and alarm escalation timing.
*   Evidence: Pump performance data and user feedback.
*   Compliance: IEC 60601-1:2012, Clause 8.2.2.

### Example C (Fault) 🔴

*   Sensor spike/dropout and actuator command rejection path.
*   Evidence: Pump error logs and user feedback.
*   Compliance: IEC 60601-1:2012, Clause 8.2.3.

Patterns
--------
### 1. Map each scenario to requirement and hazard identifiers 🟢

*   Use a single, standardized notation for requirement and hazard IDs.
*   Ensure clear and concise descriptions for each ID.

### 2. Use one baseline artifact set for comparison across variants 🟡

*   Establish a common reference point for artifact comparison.
*   Ensure artifacts are properly version-controlled and tracked.

### 3. Preserve raw captures alongside interpreted findings 🔴

*   Store raw data and logs alongside interpreted results.
*   Ensure data integrity and availability for future reference.

Anti-Patterns
-------------
### 1. Broad “pass” claims without scenario-level evidence 🔴

*   Avoid making general claims without specific evidence.
*   Provide detailed scenario-level evidence to support claims.

### 2. Missing boundary/fault test depth for high-risk functions 🟡

*   Ensure thorough testing of high-risk functions.
*   Identify and address any gaps in testing coverage.

### 3. Compliance references without concrete verification links 🟢

*   Provide clear and direct links to compliance evidence.
*   Ensure evidence is properly documented and accessible.

Pitfalls
--------
### 1. Underestimating interface timing effects 🟡

*   Consider the potential impact of interface timing on system behavior.
*   Ensure thorough testing of interface timing effects.

### 2. Incomplete alarm/fallback path verification 🔴

*   Verify that alarm and fallback paths are properly implemented.
*   Ensure that these paths are thoroughly tested and validated.

### 3. Weak ownership for unresolved risks 🟢

*   Clearly assign ownership for unresolved risks.
*   Ensure that owners are properly trained and equipped to address these risks.

Best Practices
--------------
### 1. Keep scenario definitions deterministic and reproducible 🟢

*   Ensure that scenario definitions are clear and concise.
*   Use standardized notation and formatting for scenario definitions.

### 2. Use quantitative pass/fail thresholds 🟡

*   Establish clear and objective pass/fail criteria.
*   Ensure that these criteria are properly documented and communicated.

### 3. Review residual risk before release recommendation 🔴

*   Thoroughly review residual risk before releasing a product.
*   Ensure that owners are properly trained and equipped to address these risks.

Checklist
---------
☐ Nominal/boundary/fault scenarios are covered.
☐ Evidence is traceable and auditable.
☐ Compliance mapping is explicit.
☐ Open issues include priority and owner.

Additional Deep-Dive Notes
--------------------------
### Domain Focus: Medical 🟢

*   Focus on medical infusion pump use cases and evidence.

### Phase Focus: Cross-Phase 🔴

*   Consider use cases and evidence across multiple phases.

### Evidence Priorities: functional correctness, timing behavior, robustness, and traceability 🟡

*   Prioritize evidence collection and analysis based on these criteria.

### Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns 🟢

*   Use these patterns to ensure consistency and reproducibility.

### Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks 🔴

*   Avoid these anti-patterns to ensure thorough and accurate testing.

### Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage 🟡

*   Consider these pitfalls when designing and testing use cases.

### Example Expansion: include one nominal, one boundary, and one fault scenario per objective 🟢

*   Use these scenarios to demonstrate use case coverage.

### Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional 🔴

*   Use this heuristic to ensure that claims are properly supported.

### Checklist Extension: capture residual risk, ownership, and next action for each unresolved item 🟡

*   Use this checklist to track and address open issues.

.. note::
    This document is intended to provide guidance and best practices for use case development and evidence collection. It is not a substitute for regulatory requirements or industry standards.

.. warning::
    Failure to properly develop and test use cases may result in product failures or safety issues.

.. important::
    Use case development and evidence collection should be performed in accordance with relevant regulatory requirements and industry standards.

.. admonition::
    This document is intended for use by medical infusion pump developers and testers. It is not intended for use by the general public.

Table of Compliance References
-----------------------------

| Reference | Description |
|-----------|-------------|
| IEC 60601-1:2012 | Medical electrical equipment - Part 1: General requirements for basic safety and essential performance |
| IEC 62304 | Medical device software - Software life cycle processes |
| ISO 14971 | Medical devices - Application of risk management to medical devices |

Table of Evidence Priorities
---------------------------

| Priority | Description |
|----------|-------------|
| Functional Correctness | Ensure that the system performs its intended functions correctly |
| Timing Behavior | Ensure that the system behaves correctly in terms of timing and synchronization |
| Robustness | Ensure that the system can withstand various types of faults and errors |
| Traceability | Ensure that the system can provide clear and unambiguous evidence of its behavior |

Table of Patterns and Anti-Patterns
-----------------------------------

| Pattern/Anti-Pattern | Description |
|---------------------|-------------|
| Baseline-First Comparison | Compare artifacts against a common baseline |
| Fixed Acceptance Thresholds | Use fixed thresholds for acceptance criteria |
| Deterministic Reruns | Ensure that reruns of scenarios are deterministic and reproducible |
| Post-Hoc Threshold Tuning | Avoid adjusting thresholds after the fact |
| Missing Raw Artifacts | Ensure that raw data and logs are properly captured and stored |
| Incomplete Negative-Path Checks | Ensure that all possible negative paths are thoroughly tested |

Table of Pitfalls
-----------------

| Pitfall | Description |
|--------|-------------|
| Hidden Assumptions | Avoid making assumptions about system behavior without clear evidence |
| Interface Timing Drift | Consider the potential impact of interface timing on system behavior |
| Weak Requirement-to-Test Linkage | Ensure that requirements are properly linked to test cases |

Table of Best Practices
-----------------------

| Best Practice | Description |
|--------------|-------------|
| Keep Scenario Definitions Deterministic and Reproducible | Ensure that scenario definitions are clear and concise |
| Use Quantitative Pass/Fail Thresholds | Establish clear and objective pass/fail criteria |
| Review Residual Risk Before Release Recommendation | Thoroughly review residual risk before releasing a product |
