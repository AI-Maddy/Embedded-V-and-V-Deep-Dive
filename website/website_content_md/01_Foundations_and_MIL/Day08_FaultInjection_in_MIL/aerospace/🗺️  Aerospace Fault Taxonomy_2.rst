🗺️  Aerospace Fault Taxonomy
------------------------------

.. tip::
   💡 Map every fault you inject to **at least one** of these categories.
   If a category has no linked injection test, the safety assessment has a gap.

.. list-table::
   :widths: 5 20 40 35
   :header-rows: 1

   * - #
     - 💥 Fault Category
     - Description
     - Example Injection
   * - 1
     - 📡 **Sensor Fault**
     - Sensor output deviates from truth: bias, drift, noise spike, stuck, NaN
     - IMU gyro stuck at last value; ADC α = NaN
   * - 2
     - 🔌 **Bus / Comms Fault**
     - ARINC 429 / AFDX data corruption, frame loss, stale label, SSM error
     - ARINC 429 label SSM forced to NCD; AFDX VL dropped
   * - 3
     - ⚙️ **Actuator Fault**
     - Actuator jam, runaway, rate-limit degradation, free-float
     - Elevator jammed at +3°; aileron runaway at max rate
   * - 4
     - 🧮 **Computation Fault**
     - Overflow, division-by-zero, mode-logic corruption, memory bit-flip
     - Gain table index out of range → clamped or wrapped?
   * - 5
     - ⚡ **Power / Discrete Fault**
     - Power bus dropout, discrete I/O stuck high/low, relay weld
     - Hydraulic system A → OFF at T = 30 s
   * - 6
     - 🌡️ **Environment Fault**
     - Icing, extreme temperature, windshear, volcanic ash
     - Sudden 30-kt windshear at 200 ft AGL during approach
   * - 7
     - 🔄 **Redundancy Fault**
     - Simultaneous or cascading faults across redundant channels
     - ADC-1 stale + ADC-2 NCD + ADC-3 bias drift (triple fail)

----

