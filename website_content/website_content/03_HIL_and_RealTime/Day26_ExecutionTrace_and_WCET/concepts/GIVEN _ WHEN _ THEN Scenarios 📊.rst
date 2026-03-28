GIVEN / WHEN / THEN Scenarios 📊
---------------------------------
- **Nominal (🟢)**: 
  - **GIVEN** a properly configured HIL setup,
  - **WHEN** the system executes a standard operation,
  - **THEN** the execution trace should reflect expected timing and behavior.

- **Boundary (🟡)**: 
  - **GIVEN** the system is operating at its maximum load,
  - **WHEN** a critical operation is performed,
  - **THEN** the execution time should remain within defined limits.

- **Fault (🔴)**: 
  - **GIVEN** an unexpected fault occurs in the system,
  - **WHEN** the system attempts to recover,
  - **THEN** the execution trace should log the fault and recovery attempts accurately.

.. important::
   Adhere to relevant domain standards such as ISO 26262 for automotive systems and IEC 62304 for medical device software to ensure compliance and safety.

.. warning::
   Misalignment with standards can lead to severe consequences in safety-critical applications. Always verify compliance before proceeding.

.. note::
   Continuous improvement of processes and documentation is essential for maintaining high-quality V&V practices in embedded systems.
