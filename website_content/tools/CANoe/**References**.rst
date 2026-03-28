**References**
--------------

* DO-178C: Software Considerations in Airborne Systems and Equipment Certification
* DO-254: Design Assurance Guidance for Airborne Electronic Hardware
* ISO 26262: Functional Safety for Road Vehicles
* IEC 62304: Medical Device Software - Software Life Cycle Processes
* ARP4754A/4761: Guidelines for Development of Civil Aircraft and Systems
* ASPICE: Automotive Spice

**CANoe Verification & Validation (V&V) Patterns and Anti-Patterns**
----------------------------------------------------------------

.. list-table::
   :header-rows: 1

   * - Pattern/Anti-Pattern
     - Description
   * - Baseline-first comparison
     - Compare system behavior with a known baseline.
   * - Fixed acceptance thresholds
     - Set fixed thresholds for system performance.
   * - Deterministic reruns
     - Run tests with deterministic inputs.
   * - Post-hoc threshold tuning
     - Adjust thresholds after testing.
   * - Missing raw artifacts
     - Fail to capture raw test data.
   * - Incomplete negative-path checks
     - Fail to test system behavior under fault conditions.

**CANoe Verification & Validation (V&V) Pitfalls**
------------------------------------------------

.. list-table::
   :header-rows: 1

   * - Pitfall
     - Description
   * - Hidden assumptions
     - Fail to verify assumptions with evidence.
   * - Interface timing drift
     - Fail to account for timing drift between interfaces.
   * - Weak requirement-to-test linkage
     - Fail to link test cases to objective requirements.
