Scenario 🧩
-----------
GIVEN a representative **MIL** model setup:
- 🟢 Nominal: Standard operation within expected parameters.
- 🟡 Boundary: Near-limit conditions for timing, value, or mode.
- 🔴 Fault: Negative stimulus with expected detection and recovery.

WHEN executing the test cases:
- 🟢 Nominal: The model operates as intended without deviations.
- 🟡 Boundary: The model approaches its operational limits.
- 🔴 Fault: The model encounters an error condition.

THEN validate the following:
- 🟢 Nominal: Outputs match baseline expectations.
- 🟡 Boundary: Divergences are captured and analyzed.
- 🔴 Fault: Safe handling and recovery are confirmed.

