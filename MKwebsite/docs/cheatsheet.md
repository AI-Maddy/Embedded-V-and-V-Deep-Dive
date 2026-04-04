# :material-lightning-bolt: V&V Quick Reference Cheatsheet

!!! abstract "How to Use This Cheatsheet"
    This is your **single-page memory aid** for the entire 30-day course. Bookmark it and refer to it during phase reviews, before audits, and when you need to quickly recall a key concept.

---

## :material-format-list-numbered: The 5-Step V&V Workflow (TRACE)

!!! success "Universal V&V Checklist"
    1. **Define** acceptance criteria and measurable pass/fail thresholds (BEFORE execution)
    2. **Configure** baseline scenario with explicit assumptions and version-controlled configuration
    3. **Execute** nominal run and capture primary artifacts (logs, plots, verdicts)
    4. **Execute** stress/fault variants and record divergence behavior
    5. **Consolidate** verdicts with traceability links in the RTM

---

## :material-grid: Three Phases at a Glance

=== "Phase 1: MIL"
    | Day | Key Output | Critical Rule |
    |-----|-----------|---------------|
    | 01 | SwRS with ASIL tags | SMART-V requirements |
    | 02 | RTM populated | Bidirectional coverage |
    | 03 | Plant model validated | ±5% vs. measured data |
    | 04 | Mode manager state machine | Safe state from all modes |
    | 05 | Simulation config baseline | Fixed-step solver, O0 |
    | 06 | MIL test report | Criteria defined before run |
    | 07 | Closed-loop test | Phase margin > 30° |
    | 08 | Fault injection report | FMEA-linked faults |
    | 09 | Automated regression | CI gate on critical tests |
    | 10 | Phase gate package | 100% RTM + zero open critical |

=== "Phase 2: SIL"
    | Day | Key Output | Critical Rule |
    |-----|-----------|---------------|
    | 11 | Generated C code | ERT target, MISRA enabled |
    | 12 | SIL harness | Initialize before first step |
    | 13 | MIL-SIL comparison | Max diff < 1e-5 |
    | 14 | Unit tests | 3 classes per function (nominal, boundary, fault) |
    | 15 | Static analysis | Zero Mandatory violations |
    | 16 | SW fault injection | NULL, watchdog, allocation |
    | 17 | Robustness tests | Every invalid input has a specified response |
    | 18 | Stack analysis | WCET < 70% of budget |
    | 19 | MC/DC report | 100% for DAL A / ASIL D |
    | 20 | SIL phase gate | All criteria above met |

=== "Phase 3: HIL"
    | Day | Key Output | Critical Rule |
    |-----|-----------|---------------|
    | 21 | HIL architecture plan | RT model < 70% of step |
    | 22 | Rig config record | Smoke test PASS before proceeding |
    | 23 | I/O latency report | Criteria >= 2x ADC step |
    | 24 | Automated test scripts | Polling with timeout, not sleep |
    | 25 | Bus analysis report | All signals within comm matrix |
    | 26 | WCET evidence | >= 30% margin per task |
    | 27 | HIL fault injection | HW faults + recovery tested |
    | 28 | Compliance map | No gaps before submission |
    | 29 | Regression suite | P1 < 30 min, zero flaky tests |
    | 30 | Final package | Complete audit trail |

---

## :material-table: Standards Quick Map

| Standard | Domain | Key Phase | Critical Section |
|----------|--------|-----------|-----------------|
| ISO 26262 Pt3 | Auto | HARA/Concept | ASIL determination |
| ISO 26262 Pt6 | Auto | SIL/HIL | Sec 9 (testing), Sec 10 (coverage) |
| ISO 26262 Pt9 | Auto | SIL | FMEDA, PMHF, DC |
| DO-178C Sec 6 | Aero | SIL/HIL | Testing + coverage objectives |
| DO-178C Sec 12 | Aero | SIL | Tool qualification |
| ARP4754A | Aero | MIL | System DAL assignment |
| IEC 62304 Sec 5 | Medical | All | Software development lifecycle |
| IEC 62304 Sec 7 | Medical | All | Risk control measure verification |
| ISO 14971 | Medical | All | Risk management process |
| ASPICE SWE.4 | Auto | SIL | Unit verification |
| ASPICE SWE.6 | Auto | HIL | Qualification test |

---

## :material-brain: Memory Mnemonics

!!! abstract "Core Mnemonics"
    | Mnemonic | Stands For | Used For |
    |----------|-----------|----------|
    | **TRACE** | Traceable, Robust, Artifacts, Criteria, Evidence | Every V&V phase |
    | **SMART-V** | Specific, Measurable, Achievable, Relevant, Traceable, Verifiable | Requirements quality |
    | **HIL-SAFE** | Hardware, Integration, Linked, Safety, Acceptance, Fault, Evidence | HIL completeness |
    | **MILESTONE** | Model, Invariants, Lifecycle, Evidence, Standards, Traceability, Object code, Nominal, Evidence | MIL phase reminder |

---

## :material-help-circle: Common Audit Questions

!!! question "Top Audit Questions and Short Answers"

    **Q: How do you prove requirement SWR-X-001 is tested?**
    A: RTM row for SWR-X-001 → test case IDs → execution report → PASS verdict + log file

    **Q: What is your MC/DC coverage for ASIL D functions?**
    A: Coverage report shows 100% MC/DC for all ASIL D functions (VectorCAST report v1.0)

    **Q: How is your code generator qualified?**
    A: Embedded Coder TÜV-certified qualification kit (TQP v1.0) demonstrates TQ3 compliance with DO-178C Sec 12.2

    **Q: What is your WCET for the ACC task and what is the margin?**
    A: Measured WCET 4.8 ms, budget 7 ms, margin 31%. Measured on production firmware at 168 MHz.

    **Q: Show me a fault that was found at MIL that would have been expensive at HIL.**
    A: DEF-MIL-001: mode transition to DEGRADED took 820 ms, requirement 500 ms. Fixed at MIL (model change) vs. hardware ECU firmware rework at HIL.

---

## :material-format-quote-close: Key Principles to Remember

!!! tip "The Golden Rules"
    1. **Define pass/fail BEFORE execution** — never after seeing results
    2. **Every artifact needs a version** — "test_report_final_REAL.pdf" is not a version
    3. **Traceability is bidirectional** — forward (req → test) AND backward (test → req)
    4. **The defect cost multiplier** — 1x at MIL, 10x at SIL, 100x at HIL
    5. **Static analysis is not optional** — it finds bugs that testing will never reach
    6. **Recovery is as important as detection** — test the return to normal, not just the fault response
    7. **Coverage gaps require action** — add a test OR justify as dead code; never ignore
