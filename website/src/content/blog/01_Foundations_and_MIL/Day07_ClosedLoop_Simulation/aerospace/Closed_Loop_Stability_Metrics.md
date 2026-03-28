---
title: "Closed Loop Stability Metrics"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  1    📉 **Gain Margin  How much gain increase the   GM ≥ 6 dB (ARP4754A
       (GM)**            loop tolerates before        typical)
                         instability                  

  2    📐 **Phase Margin How much phase lag the loop  PM ≥ 45° (ARP4754A
       (PM)**            tolerates before instability typical)

  3    ⏱️ **Settling     Time to reach and stay       T_s ≤ 2 s (pitch); ≤
       Time (T_s)**      within ±2 % of commanded     1.5 s (roll)
                         value                        

  4    📈 **Overshoot    Peak transient exceedance    %OS ≤ 15 % (normal
       (%OS)**           above commanded value        law)

  5    🔄 **Steady-State Residual error after         e_ss \< 0.1°
       Error (e_ss)**    transient decays             (attitude); \< 0.5 kt
                                                      (speed)

  6    🌀 **PIO          Pilot-Induced Oscillation    Category I (no PIO
       Susceptibility    tendency (Neal-Smith,        tendency)
       Index**           bandwidth)                   

  7    🔒 **Limit-Cycle  Sustained oscillation        Zero (no limit cycle
       Amplitude**       amplitude (if any)           permitted)

  8    🛡️ **Monitor      Time from injected fault to  ≤ 100 ms (per FHA
       Detection         monitor flag assertion       latency budget)
       Latency**                                      
