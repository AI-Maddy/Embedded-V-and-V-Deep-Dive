Tabular Summary 📊
------------------
.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - **Category**
     - **Description**
     - **Examples**
   * - 🟢 Nominal
     - Expected behavior under standard conditions.
     - Stable flight-control mode tracking.
   * - 🟡 Boundary
     - Edge-case scenarios near operational limits.
     - High-workload transition envelope.
   * - 🔴 Fault
     - Failure modes or hazardous conditions.
     - Bus label corruption and sensor disagreement.

.. admonition:: Final Note
   :class: important
   Aerospace systems demand rigorous **Model-in-the-Loop** validation to ensure safety and compliance. Follow the **AIM** mnemonic and severity legend to guide your verification workflow effectively.
