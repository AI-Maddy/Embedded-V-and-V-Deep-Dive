# :material-certificate: Compliance Standards Cheatsheet

!!! abstract "Quick Reference"
    This page is your **one-page reference** for ISO 26262, DO-178C, and IEC 62304 compliance requirements across the MIL, SIL, and HIL phases. Use it during phase reviews and before certification audits.

---

## :material-car: ISO 26262 — Automotive Functional Safety

### ASIL Determination (Part 3)

!!! info "ASIL Matrix"
    Determined by HARA: **Severity × Exposure × Controllability**

    | S\E | E1 | E2 | E3 | E4 |
    |-----|----|----|----|----|
    | S1 | QM | QM | QM | A |
    | S2 | QM | A | B | C |
    | S3 | A | B | C | D |

    Controllability C3 (Difficult to control) raises ASIL by one level.

### Software Testing Requirements (Part 6)

!!! success "Key Sections"
    - **Section 7**: Software requirements specification — unambiguous, measurable, traceable
    - **Section 9**: Software testing — requirement-based, error guessing, equivalence classes, boundary values, fault injection
    - **Section 10**: Software coverage — ASIL D requires MC/DC

!!! warning "Coverage by ASIL Level"
    | Coverage Type | ASIL A | ASIL B | ASIL C | ASIL D |
    |---------------|--------|--------|--------|--------|
    | Statement | + | ++ | ++ | ++ |
    | Branch | o | + | ++ | ++ |
    | MC/DC | - | o | + | ++ |

    Legend: ++ Highly Recommended, + Recommended, o Not recommended, - Not required

### PMHF Targets (Part 9)

!!! warning "Hardware Metrics"
    | ASIL | PMHF Target |
    |------|-------------|
    | A | < 10^-6 /hour |
    | B | < 10^-7 /hour |
    | C | < 10^-7 /hour |
    | D | < 10^-8 /hour |

---

## :material-airplane: DO-178C — Airborne Software

### DAL and Coverage Requirements

!!! info "Development Assurance Levels"
    | DAL | Failure Effect | Coverage Required | Obj. Code Analysis |
    |-----|---------------|-------------------|-------------------|
    | A | Catastrophic | MC/DC 100% | **Required** |
    | B | Hazardous | Decision 100% | Recommended |
    | C | Major | Statement 100% | Not required |
    | D | Minor | None | Not required |
    | E | No Safety Effect | None | Not required |

### Key Objectives (Section 6)

!!! success "Testing Objectives"
    - **6.4.2**: Low-level requirements-based testing (normal range)
    - **6.4.3**: Robustness testing (beyond normal range, invalid inputs)
    - **6.4.4**: Structural coverage analysis (per DAL level)
    - **6.4.4.1**: Statement coverage (DAL C)
    - **6.4.4.2**: Decision coverage (DAL B)
    - **6.4.4.3**: MC/DC coverage (DAL A)

### Tool Qualification (Section 12)

!!! warning "Tool Classes"
    | Class | Description | Qualification Required |
    |-------|-------------|----------------------|
    | TQ1 | Tool output cannot be incorrect | Not required |
    | TQ2 | Error could remain undetected | Validation required |
    | TQ3 | Tool replaces development activity | Full qualification required |

    Embedded Coder generating production code = **TQ3** — full qualification kit required.

---

## :material-hospital-box: IEC 62304 — Medical Device Software

### Software Safety Classes

!!! info "Class Requirements"
    | Class | Risk Level | Requirements | Design | Unit Test | Integration | System Test |
    |-------|-----------|--------------|--------|-----------|-------------|-------------|
    | A | None | Basic | Basic | Not req. | Not req. | Basic |
    | B | Non-serious | Full | Full | Required | Required | Full |
    | C | Death/Serious | Full | Full | Required | Required | Full |

    Class C additionally requires: architectural design, risk management integration, change management, problem resolution.

### Key Sections

!!! success "Development Process (Section 5)"
    - **5.1**: Software development planning
    - **5.2**: Software requirements analysis — all hazard mitigations must be requirements
    - **5.3**: Software architectural design
    - **5.5**: Software unit implementation
    - **5.6**: Software integration and integration testing
    - **5.7**: Software system testing
    - **5.8**: Software release

!!! warning "Risk Management Integration (Section 7)"
    - **7.1**: Risk management file identification
    - **7.2**: Software risk analysis (link to ISO 14971 FMEA)
    - **7.3**: Risk control measures verification — every risk control measure must have a test case

---

## :material-table: Cross-Standard Summary

| Concept | ISO 26262 | DO-178C | IEC 62304 |
|---------|-----------|---------|-----------|
| Requirements traceability | Part 6 Sec 7 | Sec 11.9 | Sec 5.2 |
| Unit testing | Part 6 Sec 9 | Sec 6.4 | Sec 5.5 |
| Integration testing | Part 6 Sec 9 | Sec 6.4 | Sec 5.6 |
| Fault injection | Part 9 Sec 7 | Sec 6.4.3 | Sec 7.3 |
| Coverage (highest) | MC/DC (ASIL D) | MC/DC (DAL A) | Not specified |
| Static analysis | Part 6 Sec 9.4.2 | Sec 6.3.4 | Sec 5.5.3 |
| Tool qualification | Part 8 Sec 11 | Sec 12.2 | Sec 7.1 |
| Configuration management | Part 8 Sec 7 | Sec 7 | Sec 8 |

---

## :material-brain: Memory Tricks

!!! abstract "TRACE — Universal V&V Mnemonic"
    **T**raceable · **R**obust · **A**rtifacts-complete · **C**riteria-explicit · **E**vidence-based

    Applies to MIL, SIL, and HIL equally.

!!! abstract "HIL-SAFE — HIL Completeness Mnemonic"
    **H**ardware · **I**ntegration · **L**inked · **S**afety · **A**cceptance · **F**ault · **E**vidence

!!! abstract "SMART-V — Requirements Quality Mnemonic"
    **S**pecific · **M**easurable · **A**chievable · **R**elevant · **T**raceable · **V**erifiable
