---
title: "Heuristics 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  Monitor fails to detect injected    Check injection point --- is it
  fault                               upstream of the monitor\'s
                                      observation point?

  Detection latency exceeds FHA       Verify bus timing + frame-age
  budget by 10 ms                     counter resolution; 1-frame jitter
                                      may explain.

  Multi-fault scenario causes model   Add saturation / integrator reset
  divergence                          on mode transition; verify
                                      anti-windup fires.

  Same fault, different severity →    Investigate non-linear monitor
  wildly different latency            threshold; small faults may
                                      straddle detection boundary.

  Regression run detects fault 5 ms   Check if trim state or turbulence
  faster                              seed changed --- both shift the
                                      detection baseline.

  DER asks \"why no combined sensor + Point to FTA cut set analysis; if
  actuator fault?\"                   no such cut set exists, justify; if
                                      it does, add it.
