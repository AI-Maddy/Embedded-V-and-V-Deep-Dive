Aerospace Focus — Day23 RealTime IO 🚀
=======================================

Objective 🎯
-----------
Apply this day in **Aerospace** context with explicit safety, compliance, and evidence expectations. The goal is to ensure that all hardware-in-the-loop (HIL) activities meet the stringent requirements of the aerospace industry, providing a solid foundation for safety-critical systems.

Phase Context 🛠️
-----------------
Phase: **HIL**  
Primary focus: **hardware-integrated timing and interface confidence**.  
Section focus: **aerospace verification workflow**.  

Domain Constraints 📜
----------------------
- Compliance baseline: **DO-178C/DO-254 + ARP4754A/ARP4761**  
- Key hazard profile: loss of control authority, unstable mode transition, stale avionics data  
- Interface landscape: ARINC 429/664, AFDX, discrete I/O  

Domain-Specific Examples 🛩️
------------------------------
- **Nominal** 🟢: stable flight-control mode tracking with expected disturbances.  
- **Boundary** 🟡: high-workload transition envelope near stability margins.  
- **Fault** 🔴: bus label corruption and sensor disagreement event.  

Patterns 🔍
----------
- Derive acceptance thresholds from hazard-linked requirements.  
- Keep interface timing contracts explicit and reviewable.  
- Compare nominal and stressed traces against the same baseline.  

Anti-Patterns 🚫
----------------
- Generic test claims without domain hazard mapping.  
- Pass/fail decisions without quantitative thresholds.  
- Evidence summaries without raw artifact references.  

Pitfalls ⚠️
-----------
- Hidden assumptions in environment or calibration setup.  
- Missing negative-path scenarios for high-criticality behavior.  
- Incomplete traceability from requirement to verdict.  

Best Practices 🌟
-----------------
- Tag every artifact with domain requirement IDs.  
- Capture timing + functional evidence in the same run package.  
- Record residual risk and ownership before closure.  

Heuristics 🧠
-------------
- If a domain hazard is untested, confidence is provisional.  
- If rerun differs unexpectedly, investigate determinism first.  
- If evidence is indirect, reduce verdict confidence level.  

Checklist ✅
-----------
.. note::
   Ensure the following items are checked before proceeding with the review:

- [ ] Domain hazard coverage is explicit.  
- [ ] Compliance references are mapped to evidence.  
- [ ] Nominal/boundary/fault results are all documented.  
- [ ] Residual risks and next actions are assigned.  

GIVEN / WHEN / THEN Scenarios 📊
------------------------------
.. important::
   Use the following templates to structure your test scenarios:

- **Nominal** 🟢:  
  **GIVEN** a stable flight-control system,  
  **WHEN** expected disturbances occur,  
  **THEN** the system maintains control authority.

- **Boundary** 🟡:  
  **GIVEN** a high-workload transition near stability margins,  
  **WHEN** the workload increases,  
  **THEN** the system should remain stable without loss of control.

- **Fault** 🔴:  
  **GIVEN** a bus label corruption event,  
  **WHEN** a sensor disagreement occurs,  
  **THEN** the system should trigger a fault response and log the event.

Domain-Specific Mnemonic Acronym: **HIL-CATS** 🐱
-------------------------------------------------
- **H**azard coverage  
- **I**nterface confidence  
- **L**ogging evidence  
- **C**ompliance mapping  
- **A**cceptance thresholds  
- **T**iming contracts  
- **S**cenario testing  

.. warning::
   Ensure all documentation aligns with the compliance standards to avoid regulatory issues.
