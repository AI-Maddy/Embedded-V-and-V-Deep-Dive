---
title: "Pattern 5   Envelope Protection"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  Unintended protection         Nominal manoeuvre --- assert protection 
  activation                    = OFF                                   

  Failure to activate at limit  Ramp α to α_max --- assert protection   
                                activates \| before structural limit    

  Oscillatory protection        Simulate α near threshold with noise    
  (hunting)                     --- assert hysteresis prevents          
                                chattering                              

  Protection stuck active       Recovery scenario --- assert pilot      
                                authority restored within T_RECOV       
