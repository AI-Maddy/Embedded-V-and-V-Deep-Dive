---
title: "Fault Injection Verdict Criteria"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# 📊 Fault Injection Verdict Criteria

Every fault injection scenario must evaluate **all five** of these

  1    🔍 **Detection**  Did the monitor detect   Detection flag asserted
                         the fault?               = True

  2    ⏱️ **Latency**    How fast was the fault   T_detect − T_inject ≤
                         detected?                FHA budget (50--200 ms)

  3    🔄 **Isolation /  Did the system isolate   Correct mode-transition
       Reconfig**        the fault and            within reconfig budget
                         reconfigure?             

  4    🛡️ **Safe State** Did the system reach a   No loss of positive
                         safe state?              control; transient
                                                  within limits

  5    🔁 **Recovery**   Can the system recover   Tracking error returns
                         after fault is cleared?  to nominal within
                                                  T_recovery
