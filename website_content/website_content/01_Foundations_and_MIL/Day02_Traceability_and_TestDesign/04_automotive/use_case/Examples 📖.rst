Examples 📖
-----------
.. note::
   **Scenario Templates** for MIL Verification:

   **Nominal Scenario 🟢**:
   GIVEN: Adaptive cruise control is activated under normal traffic conditions.
   WHEN: The lead vehicle decelerates gradually.
   THEN: The system adjusts speed smoothly to maintain a safe distance.

   **Boundary Scenario 🟡**:
   GIVEN: Stop-and-go traffic with tight headway constraints.
   WHEN: The lead vehicle stops abruptly and resumes movement within 2 seconds.
   THEN: The system avoids collision and resumes speed regulation within 1 second.

   **Fault Scenario 🔴**:
   GIVEN: A sensor dropout occurs during operation.
   WHEN: An invalid CAN frame is injected into the network.
   THEN: The system enters a fail-safe mode and alerts the driver.

