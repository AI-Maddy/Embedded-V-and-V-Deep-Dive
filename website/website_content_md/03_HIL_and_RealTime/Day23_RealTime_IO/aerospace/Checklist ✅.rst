Checklist ✅
-----------
.. note::
   Ensure the following items are checked before proceeding with the review:

- [ ] Domain hazard coverage is explicit.  
- [ ] Compliance references are mapped to evidence.  
- [ ] Nominal/boundary/fault results are all documented.  
- [ ] Residual risks and next actions are assigned.  

GIVEN / WHEN / THEN Scenarios 📊
------------------------------
.. important::
   Use the following templates to structure your test scenarios:

- **Nominal** 🟢:  
  **GIVEN** a stable flight-control system,  
  **WHEN** expected disturbances occur,  
  **THEN** the system maintains control authority.

- **Boundary** 🟡:  
  **GIVEN** a high-workload transition near stability margins,  
  **WHEN** the workload increases,  
  **THEN** the system should remain stable without loss of control.

- **Fault** 🔴:  
  **GIVEN** a bus label corruption event,  
  **WHEN** a sensor disagreement occurs,  
  **THEN** the system should trigger a fault response and log the event.

