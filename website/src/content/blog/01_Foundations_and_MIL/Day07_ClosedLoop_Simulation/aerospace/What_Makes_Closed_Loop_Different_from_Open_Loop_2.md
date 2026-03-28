---
title: "What Makes Closed Loop Different from Open Loop 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  🏗️   Controller receives             Controller receives **live plant
       **pre-recorded** stimuli        feedback**

  🔁   No feedback path; response is   Full feedback: command → actuator →
       one-shot                        plant → sensor → bus → command

  🧪   Tests individual I/O mappings   Tests **emergent system behaviour**
                                       (stability, oscillation, coupling)

  ⚠️   Cannot detect PIO, limit-cycle, **Can** detect PIO, limit-cycling,
       or feedback instability         gain-margin violations

  📊   Pass/fail: \"does signal X      Pass/fail: \"does the **system**
       match expected value?\"         remain stable, converge, and
                                       track?\"
