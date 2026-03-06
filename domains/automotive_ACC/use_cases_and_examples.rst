Automotive Use Cases and Examples
=================================

Purpose
-------
Provide domain-tailored use cases with evidence expectations aligned to **ISO 26262 (ASIL) + ISO 21434**.

Representative Use Cases
------------------------
1. Nominal mission/profile operation
2. Boundary-condition operation near limits
3. Fault detection, containment, and recovery
4. Degraded-mode continuation with safety constraints
5. Regression stability after fixes

Domain-Specific Examples
------------------------
- Example A (Nominal): adaptive cruise and speed regulation under normal traffic.
- Example B (Boundary): dense stop-and-go with tight headway and timing limits.
- Example C (Fault): sensor dropout and invalid CAN frame injection.

Patterns
--------
- Map each scenario to requirement and hazard identifiers.
- Use one baseline artifact set for comparison across variants.
- Preserve raw captures alongside interpreted findings.

Anti-Patterns
-------------
- Broad “pass” claims without scenario-level evidence.
- Missing boundary/fault test depth for high-risk functions.
- Compliance references without concrete verification links.

Pitfalls
--------
- Underestimating interface timing effects.
- Incomplete alarm/fallback path verification.
- Weak ownership for unresolved risks.

Best Practices
--------------
- Keep scenario definitions deterministic and reproducible.
- Use quantitative pass/fail thresholds.
- Review residual risk before release recommendation.

Checklist
---------
- Nominal/boundary/fault scenarios are covered.
- Evidence is traceable and auditable.
- Compliance mapping is explicit.
- Open issues include priority and owner.

Additional Deep-Dive Notes
--------------------------
- Domain Focus: Automotive
- Phase Focus: Cross-Phase
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.
