---
title: "Pattern 1   Hierarchical Mode Logic State Machine"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


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
