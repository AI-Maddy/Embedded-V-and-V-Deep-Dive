Medical Focus — Day23 RealTime IO
=================================

Objective
---------
Apply this day in **Medical** context with explicit safety, compliance, and evidence expectations.

Phase Context
-------------
Phase: **HIL**
Primary focus: **hardware-integrated timing and interface confidence**.
Section focus: **medical verification workflow**.

Domain Constraints
------------------
- Compliance baseline: **IEC 62304 + ISO 14971 + IEC 60601 context**
- Key hazard profile: incorrect dosage delivery, missed alarm, unsafe therapy continuation
- Interface landscape: device buses, sensor links, alarm/event channels

Domain-Specific Examples
------------------------
- Nominal: therapy control with validated sensor feedback.
- Boundary: near-threshold dosing and alarm escalation timing.
- Fault: sensor spike/dropout and actuator command rejection path.

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
