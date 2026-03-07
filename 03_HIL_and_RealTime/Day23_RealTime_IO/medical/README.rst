Medical Focus — Day23 RealTime IO 🩺
======================================

Objective 🎯
-----------
Apply this day in **Medical** context with explicit safety, compliance, and evidence expectations. The goal is to ensure that all verification and validation activities align with the stringent requirements of the medical domain, thereby safeguarding patient health and ensuring device efficacy.

Phase Context 🔄
----------------
Phase: **HIL** (Hardware-in-the-Loop)  
Primary focus: **hardware-integrated timing and interface confidence**.  
Section focus: **medical verification workflow**. This phase emphasizes the integration of hardware components with simulation environments to validate real-time performance and safety.

Domain Constraints 🚧
---------------------
- Compliance baseline: **IEC 62304** (Software Life Cycle Processes), **ISO 14971** (Risk Management), and **IEC 60601** (Medical Electrical Equipment).
- Key hazard profile: incorrect dosage delivery, missed alarm, unsafe therapy continuation.
- Interface landscape: device buses, sensor links, alarm/event channels, which must be rigorously tested to ensure reliability and safety.

Domain-Specific Examples 📊
----------------------------
- **Nominal** 🟢: therapy control with validated sensor feedback, ensuring that the system operates within expected parameters.
- **Boundary** 🟡: near-threshold dosing and alarm escalation timing, where the system must respond accurately to critical limits.
- **Fault** 🔴: sensor spike/dropout and actuator command rejection path, simulating failure modes to assess system robustness.

Patterns 🔍
----------
- Derive acceptance thresholds from hazard-linked requirements to ensure that all testing is grounded in real-world risks.
- Keep interface timing contracts explicit and reviewable, facilitating clear communication among stakeholders.
- Compare nominal and stressed traces against the same baseline to identify discrepancies and ensure system reliability.

Anti-Patterns 🚫
----------------
- Generic test claims without domain hazard mapping, which can lead to oversight of critical risks.
- Pass/fail decisions without quantitative thresholds, resulting in ambiguous outcomes.
- Evidence summaries without raw artifact references, making it difficult to trace back to original data.

Pitfalls ⚠️
-----------
- Hidden assumptions in environment or calibration setup that can compromise test validity.
- Missing negative-path scenarios for high-criticality behavior, which may overlook potential failure modes.
- Incomplete traceability from requirement to verdict, hindering accountability and compliance.

Best Practices 🌟
-----------------
- Tag every artifact with domain requirement IDs to ensure traceability and accountability.
- Capture timing + functional evidence in the same run package, providing a comprehensive view of system performance.
- Record residual risk and ownership before closure to maintain awareness of outstanding issues.

Heuristics 💡
-------------
- If a domain hazard is untested, confidence is provisional; prioritize testing to mitigate risks.
- If rerun differs unexpectedly, investigate determinism first to understand the source of variability.
- If evidence is indirect, reduce verdict confidence level to reflect uncertainty in the findings.

Checklist ✅
-----------
.. list-table:: Pre-Review Checklist
   :widths: 20 80
   :header-rows: 1

   * - Item
     - Description
   * - ☐ Domain hazard coverage is explicit.
     - Ensure that all identified hazards have corresponding test cases.
   * - ☐ Compliance references are mapped to evidence.
     - Verify that all compliance requirements are linked to test results.
   * - ☐ Nominal/boundary/fault results are all documented.
     - Confirm that all test outcomes are recorded and categorized.
   * - ☐ Residual risks and next actions are assigned.
     - Identify any remaining risks and outline steps for mitigation.

.. note::
   Remember to maintain a clear focus on the safety and efficacy of medical devices throughout the verification process.

.. important::
   Compliance with IEC 62304, ISO 14971, and IEC 60601 is critical to ensure patient safety and device reliability.

.. warning::
   Failure to adequately address domain-specific hazards can result in severe consequences, including patient harm and regulatory non-compliance.

**Mnemonic Acronym: SAFE**  
**S**afety, **A**ccuracy, **F**unctionality, **E**vidence
