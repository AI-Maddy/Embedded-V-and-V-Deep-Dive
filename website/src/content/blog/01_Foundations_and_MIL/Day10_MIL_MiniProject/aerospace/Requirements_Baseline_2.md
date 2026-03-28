---
title: "Requirements Baseline 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  **PA-REQ-001**   Pitch-axis controller shall     H-001: loss of    A       Nominal
                   track θ_cmd within ±0.5° RMS in pitch control             
                   steady flight (ATT mode).                                 

  **PA-REQ-002**   Settling time for a 5° step     H-001             A       Nominal
                   command shall be ≤ 3.0 s with ≤                           
                   10 % overshoot.                                           

  **PA-REQ-003**   Mode transition ATT → VS shall  H-002: unstable   A       Boundary
                   complete within 200 ms with no  mode change               
                   transient \> 2° deviation.                                

  **PA-REQ-004**   Mode transition VS → ALTS shall H-002             B       Boundary
                   track altitude reference within                           
                   ±50 ft within 15 s.                                       

  **PA-REQ-005**   Pitch-axis controller shall     H-003: surface    A       Boundary
                   saturate elevator command at    over-deflection           
                   ±25° and produce a crew alert                             
                   within 500 ms.                                            

  **PA-REQ-006**   Upon single IMU failure, the    H-004: sensor     A       Fault
                   controller shall switch to      failure                   
                   backup IMU within 100 ms and                              
                   maintain ≤ 1° transient.                                  

  **PA-REQ-007**   Upon ADC loss, controller shall H-005: air-data   A       Fault
                   revert to ATT hold using last   failure                   
                   valid altitude; crew alert                                
                   within 200 ms.                                            

  **PA-REQ-008**   Elevator actuator jam at        H-006: actuator   A       Fault
                   current position shall trigger  failure                   
                   OVRD mode within 300 ms.                                  

  **PA-REQ-009**   ARINC 429 label stale-data (no  H-007: bus data   A       Fault
                   update \> 50 ms) shall trigger  loss                      
                   sensor-disagreement monitor.                              

  **PA-REQ-010**   In moderate turbulence          H-001             B       Boundary
                   (MIL-F-8785C Cat B), tracking                             
                   error shall remain ≤ 1.5° RMS.                            

  **PA-REQ-011**   Simultaneous IMU failure +      H-004 + H-001     A       Multi-fault
                   turbulence shall not cause                                
                   pitch divergence \> 5° within                             
                   10 s.                                                     

  **PA-REQ-012**   All mode transitions shall be   Audit requirement C       Traceability
                   logged with timestamps and mode                           
                   IDs on the bus (ARINC 429 label                           
                   320).                                                     
