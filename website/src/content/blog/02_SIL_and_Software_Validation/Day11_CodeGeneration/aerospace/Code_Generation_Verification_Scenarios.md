---
title: "Code Generation Verification Scenarios"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---


  **CG-VER-01**   Generated code compiles with Cross-compilation       `compiler_output.log` has
                  zero warnings on target                              0 warnings
                  compiler at -O1, -Werror.                            

  **CG-VER-02**   No `double` type, `malloc`,  `codegen_verify.py`     0 prohibited constructs
                  `free`, `goto`, or           script                  found
                  `system()` in generated                              
                  code.                                                

  **CG-VER-03**   MISRA C:2012 mandatory       Polyspace / PC-lint /   MISRA report clean
                  rules: zero violations.      LDRA                    
                  Required rules: zero                                 
                  violations or formal                                 
                  deviation.                                           

  **CG-VER-04**   Codegen report maps every    `codegen_report.html`   100 % block → code
                  Simulink block to a C source review                  coverage
                  line. No unmapped blocks.                            

  **CG-VER-05**   SIL back-to-back: generated  SIL vs MIL comparison   `max|MIL - SIL| < 1e-6`
                  C produces identical output  (Day 13)                per signal
                  (within ε) to MIL model for                          
                  all nominal scenarios.                               

  **CG-VER-06**   Stack usage of generated     Static stack analysis   Stack depth ≤ 8192 bytes
                  code fits within FCC stack   (compiler report)       
                  allocation (e.g., 8 KB).                             

  **CG-VER-07**   WCET of `FCS_step()`         Static timing analysis  WCET ≤ 4.5 ms (90 % of
                  function fits within 200 Hz  (Day 26)                frame)
                  frame budget (5 ms).                                 
