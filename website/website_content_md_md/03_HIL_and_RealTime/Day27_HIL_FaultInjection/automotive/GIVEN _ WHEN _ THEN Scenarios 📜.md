# GIVEN / WHEN / THEN Scenarios 📜

-   **Nominal** 🟢:
    -   **GIVEN** the vehicle is in adaptive cruise mode,
    -   **WHEN** the traffic is flowing normally,
    -   **THEN** the vehicle maintains a safe distance and speed.
-   **Boundary** 🟡:
    -   **GIVEN** the vehicle is in stop-and-go traffic,
    -   **WHEN** the headway is less than 1 meter,
    -   **THEN** the vehicle responds without unintended acceleration.
-   **Fault** 🔴:
    -   **GIVEN** a sensor dropout occurs,
    -   **WHEN** an invalid CAN frame is injected,
    -   **THEN** the system enters a safe state without loss of control.
