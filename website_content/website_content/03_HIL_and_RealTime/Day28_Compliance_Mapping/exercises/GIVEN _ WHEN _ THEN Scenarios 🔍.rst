GIVEN / WHEN / THEN Scenarios 🔍
--------------------------------
- **Nominal (🟢)**:
  - **GIVEN** a stable system configuration,
  - **WHEN** the nominal scenario is executed,
  - **THEN** all outputs should match the baseline.

- **Boundary (🟡)**:
  - **GIVEN** a system operating at its limits,
  - **WHEN** the boundary variant is executed,
  - **THEN** any divergences should be documented and analyzed.

- **Fault (🔴)**:
  - **GIVEN** a fault is introduced into the system,
  - **WHEN** the fault variant is executed,
  - **THEN** the system should demonstrate proper detection and recovery mechanisms.

.. important::
   Ensure that all findings are documented thoroughly to maintain compliance with standards such as ISO 26262 and IEC 62304. This documentation is crucial for audits and future reference.

.. warning::
   Be cautious of hidden dependencies that may affect the outcome of the tests. Always validate the setup before execution to mitigate risks.

.. note::
   This exercise is crucial for ensuring that the system meets the required safety and performance standards in embedded systems. Compliance with DO-178C and DO-254 is paramount for certification.

.. admonition::
   Regularly review and update your compliance mapping to reflect any changes in system design or requirements. This proactive approach will help maintain alignment with industry standards.

.. list-table:: Compliance Mapping References
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Description
   * - DO-178C
     - Software Considerations in Airborne Systems and Equipment Certification
   * - DO-254
     - Design Assurance Guidance for Airborne Electronic Hardware
   * - ISO 26262
     - Road Vehicles – Functional Safety
   * - IEC 62304
     - Medical Device Software – Software Life Cycle Processes
   * - ARP4754A
     - Guidelines for Development of Civil Aircraft and Systems
   * - ASPICE
     - Automotive SPICE Process Assessment Model

This comprehensive approach ensures that all aspects of the HIL exercise are covered, promoting a robust verification and validation process for embedded systems.
