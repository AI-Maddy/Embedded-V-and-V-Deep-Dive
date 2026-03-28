# Test Design Depth 🧪

Test design must address **three key dimensions**:

-   **Nominal Tests 🟢**: Validate intended behavior under normal
    conditions.
-   **Boundary Tests 🟡**: Assess system sensitivity to edge cases and
    limits.
-   **Negative/Fault Tests 🔴**: Confirm safe degradation and recovery
    mechanisms.

**Scenario Templates**:

  **Scenario Type**   **GIVEN**                                      **WHEN**                                      **THEN**
  ------------------- ---------------------------------------------- --------------------------------------------- ----------------------------------------------------
  Nominal 🟢          System is operating under normal conditions.   A valid input is provided.                    The system produces the expected output.
  Boundary 🟡         System is operating near its limits.           An edge-case input is provided.               The system handles the input without failure.
  Fault 🔴            System encounters an error condition.          An invalid or unexpected input is provided.   The system degrades gracefully or recovers safely.

  : Test Design Scenarios
