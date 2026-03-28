Pattern 3 — 🔌 Avionics Bus Interface Model (ARINC 429 / AFDX)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: What It Models

All sensor and cross-channel data arriving via ARINC 429 labels or AFDX Virtual
Links must be modelled with explicit **data validity**, **SSM (Sign/Status Matrix)**
decoding, **frame-age monitoring**, and **NCD (No Computed Data)** handling.

.. rubric:: ARINC 429 Label Validity State Machine

.. code-block:: text

   ┌────────────────────────────────────────────────────────────┐
   │             LABEL VALIDITY MONITOR (per label)             │
   │                                                            │
   │  INIT ──first valid word──► VALID                          │
   │          ◄──────────────────────  ◄── word within timeout  │
   │  VALID ──timeout exceeded──► STALE                         │
   │  VALID ──SSM = NCD/FW──────► INVALID                       │
   │  STALE ──valid word rcvd───► VALID  (if recovery enabled)  │
   │                                                            │
   │  Outputs: data_value · validity_flag · age_counter         │
   └────────────────────────────────────────────────────────────┘

.. rubric:: Modeling Rules

+----------------------------+------------------------------------------------------------+
| Rule                       | Detail                                                     |
+============================+============================================================+
| 🕐 Frame-age counter       | Increment every execution frame; reset on fresh label.     |
|                            | Declare stale when counter > ``MAX_AGE_FRAMES``.           |
+----------------------------+------------------------------------------------------------+
| 🚦 SSM decoding            | Decode SSM field explicitly: ``00`` = FW (failure warning),|
|                            | ``01`` = NCD, ``10`` = FT (functional test), ``11`` = NO   |
|                            | (normal operation).  Only ``NO`` may drive control law.    |
+----------------------------+------------------------------------------------------------+
| 🛡️ Downstream protection   | Gate every control-law input behind a validity check;      |
|                            | use last-valid-value (LVV) hold for ≤ ``T_HOLD`` duration. |
+----------------------------+------------------------------------------------------------+
| 🔢 Scaling / BNR encoding  | Apply ARINC 429 BNR resolution formula:                    |
|                            | ``value = raw_29bit × 2^(MSB_weight - 28)``               |
|                            | Verify against ICD before integration.                     |
+----------------------------+------------------------------------------------------------+
| 📋 ICD traceability        | Every decoded label must reference the ICD document,       |
|                            | revision, and label number in the block annotation.        |
+----------------------------+------------------------------------------------------------+

----

