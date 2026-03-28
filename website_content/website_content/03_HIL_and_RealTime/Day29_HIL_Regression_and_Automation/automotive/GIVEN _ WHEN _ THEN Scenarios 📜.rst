GIVEN / WHEN / THEN Scenarios 📜
-------------------------------
- **Nominal Scenario** 🟢:
  - **GIVEN** the vehicle is in adaptive cruise mode,
  - **WHEN** the traffic conditions are normal,
  - **THEN** the vehicle maintains a safe distance and speed.

- **Boundary Scenario** 🟡:
  - **GIVEN** the vehicle is in stop-and-go traffic,
  - **WHEN** the headway is minimal,
  - **THEN** the system must respond without unintended acceleration.

- **Fault Scenario** 🔴:
  - **GIVEN** a sensor dropout occurs,
  - **WHEN** an invalid CAN frame is injected,
  - **THEN** the system should enter a safe state without loss of control.

.. note::
   This document aligns with the following standards: ISO 26262, ISO 21434, and other relevant automotive safety standards. Always ensure compliance with these guidelines during the HIL testing phase.

.. important::
   Remember that thorough documentation and traceability are essential for compliance and safety in automotive systems. Each test must be backed by clear evidence and linked to specific requirements.

.. warning::
   Failing to address high-criticality scenarios can lead to severe safety risks. Always prioritize testing for unintended behaviors and ensure that all potential hazards are accounted for in your verification strategy.
