Aerospace Focus — Day27 HIL FaultInjection 🚀
==========================================

Objective 🎯
---------
Apply this day in **Aerospace** context with explicit safety, compliance, and evidence expectations. The goal is to ensure that all hardware-in-the-loop (HIL) testing adheres to the highest standards of verification and validation, ensuring safety and reliability in aerospace systems. This is crucial for maintaining the integrity of flight operations and ensuring passenger safety.

Phase Context 🛠️
-------------
Phase: **HIL**  
Primary focus: **hardware-integrated timing and interface confidence**.  
Section focus: **aerospace verification workflow**.  

Domain Constraints 📜
------------------
- Compliance baseline: **DO-178C/DO-254 + ARP4754A/ARP4761**  
- Key hazard profile: loss of control authority, unstable mode transition, stale avionics data  
- Interface landscape: ARINC 429/664, AFDX, discrete I/O  

Domain-Specific Examples 📝
------------------------
- **Nominal (🟢)**: stable flight-control mode tracking with expected disturbances.  
- **Boundary (🟡)**: high-workload transition envelope near stability margins.  
- **Fault (🔴)**: bus label corruption and sensor disagreement event.  

Patterns 🔍
--------
- Derive acceptance thresholds from hazard-linked requirements to ensure that safety margins are met.  
- Keep interface timing contracts explicit and reviewable to facilitate traceability and accountability.  
- Compare nominal and stressed traces against the same baseline to identify deviations and ensure system resilience.

Anti-Patterns 🚫
-------------
- Generic test claims without domain hazard mapping can lead to oversight of critical risks.  
- Pass/fail decisions without quantitative thresholds undermine the rigor of the validation process.  
- Evidence summaries without raw artifact references fail to provide a complete picture of compliance.

Pitfalls ⚠️
--------
- Hidden assumptions in environment or calibration setup can lead to unexpected failures during testing.  
- Missing negative-path scenarios for high-criticality behavior may result in untested vulnerabilities.  
- Incomplete traceability from requirement to verdict can compromise the integrity of the V&V process.

Best Practices 🌟
--------------
- Tag every artifact with domain requirement IDs to facilitate easy tracking and retrieval.  
- Capture timing + functional evidence in the same run package to streamline the validation process.  
- Record residual risk and ownership before closure to ensure accountability and transparency.

Heuristics 🧠
----------
- If a domain hazard is untested, confidence is provisional; prioritize testing to mitigate risks.  
- If rerun differs unexpectedly, investigate determinism first to identify potential issues in the system.  
- If evidence is indirect, reduce verdict confidence level to account for uncertainty.

Checklist ✅
---------
.. note:: Pre-review checklist for HIL Fault Injection
   - [ ] Domain hazard coverage is explicit.  
   - [ ] Compliance references are mapped to evidence.  
   - [ ] Nominal/boundary/fault results are all documented.  
   - [ ] Residual risks and next actions are assigned.  

GIVEN / WHEN / THEN Scenarios 📊
-------------------------------
- **Nominal (🟢)**:  
  - **GIVEN** the aircraft is in stable flight mode,  
  - **WHEN** a disturbance occurs,  
  - **THEN** the flight-control system maintains control within specified parameters, ensuring safe operation.

- **Boundary (🟡)**:  
  - **GIVEN** the aircraft is near the stability margin,  
  - **WHEN** workload increases significantly,  
  - **THEN** the system should transition smoothly without loss of control, demonstrating robustness under stress.

- **Fault (🔴)**:  
  - **GIVEN** a bus label corruption event occurs,  
  - **WHEN** the sensor data is inconsistent,  
  - **THEN** the system should trigger a fault response and revert to a safe state, ensuring safety is prioritized.

.. important:: Remember to document all findings and ensure traceability to requirements as per DO-178C and DO-254 standards.  
.. warning:: Failure to adhere to compliance standards may result in severe safety implications, potentially endangering lives.  
.. admonition:: Always review the interface landscape and ensure all components are functioning as intended to maintain system integrity.

Domain Standards References 📚
------------------------------
- DO-178C: Software Considerations in Airborne Systems and Equipment Certification  
- DO-254: Design Assurance Guidance for Airborne Electronic Hardware  
- ARP4754A: Guidelines for Development of Civil Aircraft and Systems  
- ARP4761: Guidelines and Methods for Conducting the Safety Assessment Process  

.. list-table:: Domain Constraints Overview
   :widths: 20 40
   :header-rows: 1

   * - Constraint Type
     - Description
   * - Compliance Baseline
     - DO-178C/DO-254 + ARP4754A/ARP4761
   * - Key Hazards
     - Loss of control authority, unstable mode transition, stale avionics data
   * - Interface Landscape
     - ARINC 429/664, AFDX, discrete I/O

Mnemonic Acronym: **HIL-SAFE** (Hardware-In-the-Loop - Safety Assurance for Flight Evaluation)
