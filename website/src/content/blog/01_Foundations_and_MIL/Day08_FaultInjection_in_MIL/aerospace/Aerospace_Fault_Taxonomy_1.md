---
title: "Aerospace Fault Taxonomy"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  1    📡 **Sensor     Sensor output deviates from  IMU gyro stuck at last
       Fault**         truth: bias, drift, noise    value; ADC α = NaN
                       spike, stuck, NaN            

  2    🔌 **Bus /      ARINC 429 / AFDX data        ARINC 429 label SSM
       Comms Fault**   corruption, frame loss,      forced to NCD; AFDX VL
                       stale label, SSM error       dropped

  3    ⚙️ **Actuator   Actuator jam, runaway,       Elevator jammed at +3°;
       Fault**         rate-limit degradation,      aileron runaway at max
                       free-float                   rate

  4    🧮              Overflow, division-by-zero,  Gain table index out of
       **Computation   mode-logic corruption,       range → clamped or
       Fault**         memory bit-flip              wrapped?

  5    ⚡ **Power /    Power bus dropout, discrete  Hydraulic system A → OFF
       Discrete        I/O stuck high/low, relay    at T = 30 s
       Fault**         weld                         

  6    🌡️              Icing, extreme temperature,  Sudden 30-kt windshear
       **Environment   windshear, volcanic ash      at 200 ft AGL during
       Fault**                                      approach

  7    🔄 **Redundancy Simultaneous or cascading    ADC-1 stale + ADC-2
       Fault**         faults across redundant      NCD + ADC-3 bias drift
                       channels                     (triple fail)
