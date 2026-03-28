⚠️ Cross-Tool Pitfalls
----------------------

### 1. Timebase mismatch across tools and ECU clocks. 🔴

*   ☐ Timebase mismatch across tools and ECU clocks
*   ☐ Non-deterministic setup not captured in artifacts
*   ☐ Summary conclusions without raw evidence retention

### Domain Standards
-------------------

*   DO-178C (Software Considerations in Airborne Systems and Equipment Certification) 🟢
*   DO-254 (Design Assurance Guidance for Airborne Electronic Hardware) 🟢
*   ISO 26262 (Functional Safety for Road Vehicles) 🟡
*   IEC 62304 (Medical Device Software - Software Life Cycle Processes) 🟡
*   ARP4754A/4761 (System and Software Integrity Plans) 🔴
*   ASPICE (Automotive Safety Integrity Level Process for E/E Systems) 🔴

### Patterns and Anti-Patterns
---------------------------

### Patterns
-----------

*   Baseline-first comparison 🟢
*   Fixed acceptance thresholds 🟢
*   Deterministic reruns 🟢

### Anti-Patterns
--------------

*   Post-hoc threshold tuning 🔴
*   Missing raw artifacts 🔴
*   Incomplete negative-path checks 🔴

### Review Heuristic
------------------

*   If a claim cannot be tied to an artifact, mark confidence as provisional. 🟢

### Checklist Extension
---------------------

*   Capture residual risk
*   Ownership
*   Next action for each unresolved item

### Example Expansion
-------------------

*   Include one nominal, one boundary, and one fault scenario per objective. 🟢

### Evidence Priorities
----------------------

*   Functional correctness 🟢
*   Timing behavior 🟡
*   Robustness 🔴
*   Traceability 🔴

### Pitfalls
---------

*   Hidden assumptions 🔴
*   Interface timing drift 🔴
*   Weak requirement-to-test linkage 🔴

### Example Use Cases
-------------------

### Nominal Scenario
-----------------

*   GIVEN: The system is in a normal operating state. 🟢
*   WHEN: The user inputs a valid command. 🟢
*   THEN: The system responds correctly. 🟢

### Boundary Scenario
-----------------

*   GIVEN: The system is in a normal operating state. 🟡
*   WHEN: The user inputs an invalid command. 🟡
*   THEN: The system responds with an error message. 🟡

### Fault Scenario
----------------

*   GIVEN: The system is in a faulty state. 🔴
*   WHEN: The user inputs a valid command. 🔴
*   THEN: The system responds with an error message. 🔴

