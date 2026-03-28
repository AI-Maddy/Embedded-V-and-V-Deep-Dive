# ⚖️ Domain Constraints

::: warning
::: title
Warning
:::

⚠️ Every modeling pattern applied in this domain must satisfy the
constraints below --- they are **DER-observable** and form the basis of
SOI-2 model review.
:::

  -------------------------------------------------------------------------
  Constraint            Detail                                           
  --------------------- ------------------------------------------------ --
  📜 Compliance         DO-178C / DO-254 + DO-331 + ARP4754A / ARP4761   
  baseline              \|                                               

  ☠️ Key hazard profile Loss of control authority · Unstable mode        
                        transition · Stale avionics data · Latent sensor 
                        disagreement                                     

  🔌 Interface          ARINC 429 · ARINC 664 (AFDX) · Discrete I/O \|   
  landscape                                                              

  🎛️ Model coverage     DO-331 requires model-level MC/DC coverage       
                        evidence in addition to (not instead of)         
                        source-code coverage.                            

  📐 Modelling standard All blocks must comply with MAAB (MathWorks      
                        Automotive Advisory Board) or equivalent         
                        internal modelling guideline.                    
  -------------------------------------------------------------------------

------------------------------------------------------------------------
