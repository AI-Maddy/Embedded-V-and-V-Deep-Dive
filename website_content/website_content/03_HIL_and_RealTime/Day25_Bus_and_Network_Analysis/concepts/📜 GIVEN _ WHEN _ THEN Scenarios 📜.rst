📜 GIVEN / WHEN / THEN Scenarios 📜
-----------------------------------
### 📝 Nominal, Boundary, Fault 📝

#### 🟢 Nominal Scenario 🟢
GIVEN a properly configured bus,
WHEN data is transmitted,
THEN the expected signal integrity is maintained.

#### 🟡 Boundary Scenario 🟡
GIVEN a bus operating at maximum load,
WHEN data is transmitted,
THEN latency should not exceed the defined threshold.

#### 🔴 Fault Scenario 🔴
GIVEN a fault in the communication interface,
WHEN data is transmitted,
THEN the system should detect the failure and trigger an appropriate response.

### 📊 GIVEN / WHEN / THEN Scenarios 📊

.. list-table::
   :widths: 20 40 20 20
   :stub-columns: 1

   * - **Scenario**
     - **Description**
     - **GIVEN**
     - **WHEN**
     - **THEN**
   * - Nominal Scenario
     - Properly configured bus
     - Data is transmitted
     - Signal integrity is maintained
   * - Boundary Scenario
     - Bus operating at maximum load
     - Data is transmitted
     - Latency does not exceed threshold
   * - Fault Scenario
     - Fault in communication interface
     - Data is transmitted
     - System detects failure and responds
