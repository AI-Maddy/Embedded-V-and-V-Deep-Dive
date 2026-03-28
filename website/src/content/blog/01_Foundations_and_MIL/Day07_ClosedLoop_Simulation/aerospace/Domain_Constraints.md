---
title: "Domain Constraints"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# ⚖️ Domain Constraints

::: warning
::: title
Warning
:::

⚠️ Closed-loop MIL must satisfy all open-loop constraints (Day 06)
**plus** the additional stability and coupling constraints below.
:::

  📜 Compliance         DO-178C / DO-254 + ARP4754A / ARP4761            
  baseline                                                               

  🔁 Loop closure       Plant, sensor, actuator, and bus models must     
  fidelity              represent the same frequency range as the        
                        controller bandwidth. \|                         

  ⏱️ Timestep coherence All models in the loop must share the same fixed 
                        timestep (typ. 5 ms / 200 Hz) or use             
                        co-simulation with explicit rate-transition      
                        blocks.                                          

  📐 Solver             Fixed-step `ode4` only --- variable-step         
                        introduces non-deterministic phase lag that      
                        corrupts stability data.                         

  🌪️ Disturbance model  Dryden turbulence per MIL-F-8785C with fixed     
                        seed; severity levels: light / moderate / severe 
                        per scenario.                                    
