Automotive Focus — Day05 Simulation Tools Setup
===============================================

Objective
---------
Apply this day in **Automotive** context with explicit safety, compliance, and evidence expectations.

Phase Context
-------------
Phase: **MIL**
Primary focus: **model behavior realism and requirement intent validation**.
Section focus: **automotive verification workflow**.

Domain Constraints
------------------
- Compliance baseline: **ISO 26262 (ASIL) + ISO 21434**
- Key hazard profile: unintended acceleration/deceleration, loss of stability, braking faults
- Interface landscape: CAN, LIN, FlexRay, Automotive Ethernet

Domain-Specific Examples
------------------------
- Nominal: adaptive cruise and speed regulation under normal traffic.
- Boundary: dense stop-and-go with tight headway and timing limits.
- Fault: sensor dropout and invalid CAN frame injection.

Patterns
--------
- Derive acceptance thresholds from hazard-linked requirements.
- Keep interface timing contracts explicit and reviewable.
- Compare nominal and stressed traces against the same baseline.

Anti-Patterns
-------------
- Generic test claims without domain hazard mapping.
- Pass/fail decisions without quantitative thresholds.
- Evidence summaries without raw artifact references.

Pitfalls
--------
- Hidden assumptions in environment or calibration setup.
- Missing negative-path scenarios for high-criticality behavior.
- Incomplete traceability from requirement to verdict.

Best Practices
--------------
- Tag every artifact with domain requirement IDs.
- Capture timing + functional evidence in the same run package.
- Record residual risk and ownership before closure.

Heuristics
----------
- If a domain hazard is untested, confidence is provisional.
- If rerun differs unexpectedly, investigate determinism first.
- If evidence is indirect, reduce verdict confidence level.

Checklist
---------
- Domain hazard coverage is explicit.
- Compliance references are mapped to evidence.
- Nominal/boundary/fault results are all documented.
- Residual risks and next actions are assigned.
