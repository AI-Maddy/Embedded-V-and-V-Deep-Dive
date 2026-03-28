# Pattern 5 --- ✋ Envelope Protection

**What It Models**

Hard and soft envelope protection that prevents the aircraft from
exceeding structural, aerodynamic, or operating limits --- e.g. AOA
protection, load-factor (Nz) protection, bank-angle protection,
pitch-attitude protection.

**State Logic**

``` text
┌─────────────────────────────────────────────────────────┐
│              ENVELOPE PROTECTION BLOCK                  │
│                                                         │
│  Measured_AOA ──► AOA_PROTECTION subsystem              │
│                                                         │
│  Soft Zone: α_warn ≤ α < α_max                          │
│    → Stick force gradient increases (haptic cue)        │
│    → Pitch-up authority reduced                         │
│                                                         │
│  Hard Zone: α ≥ α_max                                   │
│    → Control law overrides pilot input                  │
│    → Pitch-down command injected                        │
│    → PROT_ACTIVE status broadcast on ARINC 429          │
│                                                         │
│  Recovery: α < α_warn − HYSTERESIS for T_RECOV          │
│    → Protection deactivated; pilot authority restored   │
└─────────────────────────────────────────────────────────┘
```

**⚠️ Hazard-Linked Test Obligations**

  ------------------------------------------------------------------------
  FHA Hazard                    Required MIL Test Scenario              
  ----------------------------- --------------------------------------- --
  Unintended protection         Nominal manoeuvre --- assert protection 
  activation                    = OFF                                   

  Failure to activate at limit  Ramp α to α_max --- assert protection   
                                activates \| before structural limit    

  Oscillatory protection        Simulate α near threshold with noise    
  (hunting)                     --- assert hysteresis prevents          
                                chattering                              

  Protection stuck active       Recovery scenario --- assert pilot      
                                authority restored within T_RECOV       
  ------------------------------------------------------------------------

------------------------------------------------------------------------
