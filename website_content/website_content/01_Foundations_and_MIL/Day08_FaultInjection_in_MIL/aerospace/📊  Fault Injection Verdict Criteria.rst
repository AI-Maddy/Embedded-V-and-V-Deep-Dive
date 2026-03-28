📊  Fault Injection Verdict Criteria
--------------------------------------

Every fault injection scenario must evaluate **all five** of these criteria:

.. list-table::
   :widths: 5 25 35 35
   :header-rows: 1

   * - #
     - Criterion
     - What Is Checked
     - Typical Threshold
   * - 1
     - 🔍 **Detection**
     - Did the monitor detect the fault?
     - Detection flag asserted = True
   * - 2
     - ⏱️  **Latency**
     - How fast was the fault detected?
     - T_detect − T_inject ≤ FHA budget (50–200 ms)
   * - 3
     - 🔄 **Isolation / Reconfig**
     - Did the system isolate the fault and reconfigure?
     - Correct mode-transition within reconfig budget
   * - 4
     - 🛡️  **Safe State**
     - Did the system reach a safe state?
     - No loss of positive control; transient within limits
   * - 5
     - 🔁 **Recovery**
     - Can the system recover after fault is cleared?
     - Tracking error returns to nominal within T_recovery

.. code-block:: python

   # === Fault injection verdict engine (Python) ===
   import numpy as np, json

   log = load_mat("evidence/FI-ACT-01/raw_log.mat")
   scenario = json.load(open("scenario.json"))

   T_inject = scenario["faults"][0]["t_inject"]
   T_detect = first_true_time(log["jam_detect_flag"])
   T_reconfig = first_true_time(log["standby_active_flag"])

   verdict = {}

   # 1. Detection
   verdict["detection"] = T_detect is not None
   # 2. Latency
   verdict["latency_ms"] = round((T_detect - T_inject) * 1000, 1) if T_detect else None
   verdict["latency_pass"] = verdict["latency_ms"] is not None and verdict["latency_ms"] <= 200
   # 3. Reconfig
   verdict["reconfig_ms"] = round((T_reconfig - T_inject) * 1000, 1) if T_reconfig else None
   verdict["reconfig_pass"] = verdict["reconfig_ms"] is not None and verdict["reconfig_ms"] <= 500
   # 4. Safe state
   max_pitch_err = np.max(np.abs(log["pitch_error"][log["time"] > T_inject]))
   verdict["safe_state"] = max_pitch_err < 5.0  # degrees
   # 5. Recovery
   recovery_window = log["pitch_error"][(log["time"] > T_reconfig + 2) & (log["time"] < T_reconfig + 10)]
   verdict["recovery_rms"] = round(float(np.sqrt(np.mean(recovery_window ** 2))), 3)
   verdict["recovery_pass"] = verdict["recovery_rms"] < 1.0

   overall = all([verdict["detection"], verdict["latency_pass"],
                   verdict["reconfig_pass"], verdict["safe_state"], verdict["recovery_pass"]])
   verdict["overall"] = "PASS" if overall else "FAIL"
   print(f"{'✅' if overall else '❌'} FI-ACT-01: {verdict['overall']}")
   json.dump(verdict, open("verdict.json", "w"), indent=2)

----

