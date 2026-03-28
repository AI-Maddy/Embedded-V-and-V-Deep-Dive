---
title: "Heuristics 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  Mode transition fires unexpectedly  Check guard condition for implicit
                                      priority or missing inhibit
                                      condition.

  Gain table boundary test fails      Verify break-point alignment and
                                      BNR quantisation; recheck ICD
                                      scaling formula.

  Monitor asserts spuriously at       Add `INIT` state to debounce first
  startup                             frame; document in Requirements.

  Coverage hole in protection logic   Add explicit test for hysteresis
                                      band; check both entry and exit
                                      conditions independently.

  Reconfiguration test flaky between  Fix random seed; check for timing
  runs                                dependency on host OS scheduler
                                      jitter.
