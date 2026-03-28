🔎 Checklist
------------
.. list-table:: Pre-Review Checklist
   :header-rows: 1

   * - Item
     - Status
   * - Pass/fail thresholds are unambiguous.
     - ☐
   * - Nominal + stress + fault evidence is present.
     - ☐
   * - Traceability and residual risk are documented.
     - ☐

**Mnemonic Acronym**: **SILVER** - **S**oftware **I**ntegration, **L**oops, **V**alidation, **E**vidence, **R**obustness

**Severity/Priority Legend**:
- 🟢 Nominal (Green): Expected behavior
- 🟡 Boundary (Yellow): Near limits
- 🔴 Fault (Red): Error conditions

.. note::
   This document serves as a guide for conducting SIL exercises effectively, ensuring that all aspects of verification and validation are covered comprehensively.

.. important::
   Always refer to relevant domain standards such as **DO-178C**, **DO-254**, **ISO 26262**, and **IEC 62304** for compliance and best practices in embedded systems V&V.

**GIVEN / WHEN / THEN Scenarios**:
- **Nominal Scenario** 🟢:
  - **GIVEN** the software is in a normal operational state,
  - **WHEN** a valid input is received,
  - **THEN** the software should produce the expected output.

- **Boundary Scenario** 🟡:
  - **GIVEN** the software is operating at its limit,
  - **WHEN** an input value approaches the threshold,
  - **THEN** the software should handle the input without failure.

- **Fault Scenario** 🔴:
  - **GIVEN** a fault is introduced in the system,
  - **WHEN** the fault occurs,
  - **THEN** the software should detect the fault and initiate recovery procedures.

.. warning::
   Ensure that all scenarios are thoroughly documented and evidence is collected for each test case to maintain compliance with industry standards.
