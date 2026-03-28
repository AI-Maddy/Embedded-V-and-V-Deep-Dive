---
title: "standards and compliance"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# Standards and Compliance --- Day01

## 🎯 Objective

Map early requirement work to the compliance language used in each
domain, so every requirement is **auditable, testable, and
safety-linked** from Day 1.

## 🚦 Compliance Signal Legend

-   🟢 **Strong**: clear safety/risk linkage and measurable verification
    criteria.
-   🟡 **Partial**: intent exists, but acceptance criteria or ownership
    is incomplete.
-   🔴 **Weak**: no traceable linkage to hazard/risk or no verification
    path.

## 🧭 Domain Mapping at a Glance

+-----------+
| Domain    |
|           |
| -   Core  |
|           |
|  Standard |
|     Focus |
| -   Re    |
| quirement |
|           |
|  Emphasis |
| -   Day01 |
|           |
|  Priority |
+===========+
| 🚗        |
| A         |
| utomotive |
|           |
| -   ISO   |
|     26262 |
|           |
|    (ASIL, |
|           |
|    safety |
|           |
|    goals) |
| -   ASIL  |
|     decom |
| position, |
|     inh   |
| eritance, |
|     and   |
|     tra   |
| ceability |
| -   Haza  |
| rd-linked |
|     re    |
| quirement |
|           |
|   clarity |
+-----------+
| ✈️        |
| Aerospace |
|           |
| -         |
|   DO-178C |
|           |
|   (object |
| ive-based |
|           |
| evidence, |
|     DAL)  |
| -   V     |
| erifiable |
|     lo    |
| w-level/h |
| igh-level |
|     re    |
| quirement |
|           |
|    intent |
| -   Ob    |
| jective + |
|           |
|  evidence |
|           |
| alignment |
+-----------+
| 🏥        |
| Medical   |
|           |
| -   IEC   |
|           |
|   62304 + |
|     ISO   |
|     14971 |
| -         |
|  Software |
|           |
|    safety |
|     class |
|     and   |
|     ris   |
| k-control |
|           |
|   linkage |
| -   Ris   |
| k-control |
|     ver   |
| ification |
|           |
|    intent |
+-----------+

## 📌 What to Capture Now (Minimum Evidence Pack)

-   🧾 **Rationale**: why the requirement exists, with hazard/risk
    reference.
-   🧪 **Verification method**: analysis, test, inspection, or
    demonstration.
-   📏 **Acceptance criteria**: measurable pass/fail condition.
-   👤 **Owner**: who produces and reviews the evidence.
-   🕒 **Lifecycle stage**: MIL/SIL/HIL target for first formal
    verification.

## 🧠 Make It Memorable: `H.E.A.R.T` Rule

-   **H --- Hazard linked**: each requirement ties to a safety/risk
    concern.
-   **E --- Evidence planned**: define artifact(s) expected at review.
-   **A --- Acceptance measurable**: avoid vague terms like "works
    well".
-   **R --- Responsibility assigned**: clear producer and approver.
-   **T --- Traceability complete**: requirement ↔ test ↔ result ↔
    review.

⚠️ Common Mistakes (and Fast Fixes)
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- 🔴
Treating all requirements with equal criticality → apply domain
criticality tags early (ASIL/DAL/Class). - 🔴 Missing
hazard-to-verification linkage → add one explicit trace row per safety
objective. - 🟡 Deferring traceability until implementation → create
requirement IDs and verification placeholders now. - 🟡 Vague acceptance
wording → convert to numeric thresholds and conditions.

## ✅ Day01 Review Checklist

-   Does each critical requirement have a domain criticality tag?
-   Is the verification intent explicit and realistic for MIL?
-   Can a reviewer find hazard/risk origin in one hop?
-   Is there at least one nominal, one boundary, and one fault scenario
    for key objectives?
-   Are unresolved items tagged with owner, residual risk, and next
    action?

## 🧩 Practical Heuristic

If a compliance claim cannot be tied to a concrete artifact, mark
confidence as 🟡 provisional and log the missing evidence.
