---
title: "Pattern 1 Hierarchical Mode Logic State Machine"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---




# Pattern 1 --- 🔄 Hierarchical Mode-Logic State Machine

**What It Models**

Flight-control law mode transitions: Normal Law → Alternate Law → Direct
Law (Airbus-style) or Normal / Secondary / Direct (Boeing-style). Also
applies to autopilot engagement/disengagement logic, envelope-protection
activation, and TCAS/ACAS mode arbitration.

**Structure**

``` text
┌──────────────────────────────────────────────────────────┐
│                   MODE SUPERVISOR (Stateflow)            │
│                                                          │
│  [NORMAL_LAW] ──fault──►  [ALTERNATE_LAW]               │
│       ▲                        │  ──severe fault──►      │
│       │ recovery (if safe)     ▼                         │
│       └────────────── [DIRECT_LAW]                       │
│                                                          │
│  Entry actions  : latch gain set, arm monitors           │
│  During actions : execute active law, update status bus  │
│  Exit actions   : freeze integrators, log transition     │
└──────────────────────────────────────────────────────────┘
```

**DO-178C / DO-331 Obligations**

  📊 Decision coverage (MC/DC)    Every mode-transition condition must   
                                  be independently exercised (DAL-A      
                                  requirement).                          

  🔗 Requirement traceability     Each transition guard maps to ≥1       
                                  system requirement ID (e.g.            
                                  `FCS-MODE-REQ-017`).                   

  🔒 Transition inhibit           Must be modelled explicitly --- not    
  conditions                      implied by absence of a trigger.       

  🧪 Reachability proof           Every state must be reachable by ≥1    
                                  test case; unreachable states are dead 
                                  code.                                  
