Representative Use Cases 📊
---------------------------

### Nominal Mission/Profile Operation 🟢

.. note:: This scenario represents the normal operating conditions of the system.

.. important:: Ensure that the system is functioning as expected in nominal conditions.

*   **GIVEN**: normal traffic conditions
*   **WHEN**: adaptive cruise control is engaged
*   **THEN**: speed regulation is maintained within acceptable limits

### Boundary-Condition Operation Near Limits 🟡

.. warning:: This scenario represents the boundary conditions of the system.

.. important:: Ensure that the system is functioning as expected near the limits of its operating conditions.

*   **GIVEN**: dense stop-and-go traffic with tight headway and timing limits
*   **WHEN**: adaptive cruise control is engaged
*   **THEN**: speed regulation is maintained within acceptable limits, but near the boundary of acceptable behavior

### Fault Detection, Containment, and Recovery 🔴

.. admonition:: This scenario represents a fault condition in the system.

.. important:: Ensure that the system is functioning as expected in fault conditions.

*   **GIVEN**: sensor dropout and invalid CAN frame injection
*   **WHEN**: adaptive cruise control is engaged
*   **THEN**: fault detection and containment mechanisms are triggered, and recovery is successful

### Degraded-Mode Continuation with Safety Constraints 🟢

.. note:: This scenario represents the degraded mode of the system.

.. important:: Ensure that the system is functioning as expected in degraded mode.

*   **GIVEN**: reduced system functionality due to hardware failure
*   **WHEN**: adaptive cruise control is engaged
*   **THEN**: degraded-mode operation is maintained within safety constraints

### Regression Stability after Fixes 🟡

.. warning:: This scenario represents the regression stability of the system after fixes.

.. important:: Ensure that the system is functioning as expected after fixes.

*   **GIVEN**: multiple fixes applied to the system
*   **WHEN**: adaptive cruise control is engaged
*   **THEN**: regression stability is ensured, and no new faults are introduced

Domain-Specific Mnemonic Acronym: **ADAS** (Advanced Driver Assistance Systems)

