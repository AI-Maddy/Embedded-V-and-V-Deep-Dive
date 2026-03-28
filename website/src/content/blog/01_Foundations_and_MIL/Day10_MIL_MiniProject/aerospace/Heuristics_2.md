---
title: "Heuristics 2"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  3 scenarios fail on first run       Don\'t panic --- check canary      
                                      first; if canary passes,           
                                      investigate scenario config.       

  DER asks about a requirement you    Acknowledge the gap, add it to the 
  forgot                              residual-risk register, assign an  
                                      owner, and proceed.                

  Evidence folder is 2 GB             Raw logs are large; that\'s        
                                      expected. Archive to network       
                                      store; keep verdict + trace in     
                                      Git\|                              

  Report generation takes 10 min      Profile: usually a slow            
                                      `read_mat()` call. Pre-extract     
                                      verdict JSONs, skip raw re-parse.  

  Determinism check fails for 1       Investigate: solver tolerance,     
  scenario                            random seed, or Fast Restart       
                                      cache. Document finding.           
