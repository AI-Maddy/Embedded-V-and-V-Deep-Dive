GIVEN / WHEN / THEN Scenarios 📜
-------------------------------
.. note:: Use the following templates to define scenarios for testing.

- **Nominal (🟢)**:  
  **GIVEN** a vehicle in adaptive cruise mode,  
  **WHEN** the traffic is flowing normally,  
  **THEN** the vehicle maintains a safe distance and speed.

- **Boundary (🟡)**:  
  **GIVEN** a vehicle in stop-and-go traffic,  
  **WHEN** the lead vehicle suddenly brakes,  
  **THEN** the vehicle responds appropriately without collision.

- **Fault (🔴)**:  
  **GIVEN** a vehicle experiencing sensor dropout,  
  **WHEN** an invalid CAN frame is injected,  
  **THEN** the vehicle enters a safe state without unintended acceleration.

.. important:: Always ensure that all scenarios are tested thoroughly to maintain safety and compliance with relevant standards.

