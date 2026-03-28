---
title: "safety requirements"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# Safety Requirements --- Day01

## 🎯 Goal

Translate identified hazards into enforceable, testable technical safety
requirements that reduce risk to an acceptable level.

## 🌈 Safety Readiness Legend

-   🟢 **Strong safety requirement**: hazard-linked, measurable, and
    verifiable.
-   🟡 **Partial safety requirement**: intent is present, but
    timing/criteria/ownership is incomplete.
-   🔴 **Unsafe draft**: vague wording, missing safe state, or no
    verification path.

## 🧭 Safety Requirement Structure (Must-Have Elements)

-   **Hazard reference** and severity/criticality context.
-   **Safety function**: protective behavior the system shall perform.
-   **Detection logic**: what fault/condition is detected and how.
-   **Reaction timing**: maximum detection + mitigation latency.
-   **Safe state**: explicitly defined degraded/shutdown behavior.
-   **Recovery rule**: controlled transition back to normal operation.
-   **Verification method**: analysis/test/inspection for each claim.

## 🛡️ Make It Memorable: `S.A.F.E.R`

-   **S --- Source hazard linked** (trace to hazard ID)
-   **A --- Action defined** (what protection occurs)
-   **F --- Fault timing bounded** (how fast to detect/react)
-   **E --- End state safe** (deterministic safe-state behavior)
-   **R --- Residual risk recorded** (owner + next action)

## 🧩 Requirement Template (Copy/Paste)

-   **ID**:
-   **Linked hazard ID(s)**:
-   **Safety objective**:
-   **Trigger/fault condition**:
-   **Required protective action**:
-   **Detection time bound**:
-   **Mitigation/reaction time bound**:
-   **Safe-state definition**:
-   **Recovery conditions**:
-   **Verification method + pass/fail criteria**:

## ✅ Good vs ❌ Weak Example

-   ❌ Weak: "If sensor fails, system should become safe quickly."
-   ✅ Good: "If wheel-speed sensor disagreement exceeds 15% for more
    than 50 ms, the controller shall disable closed-loop torque control
    within 100 ms and enter limp-home mode with torque limited to 30%
    until fault clear criteria are satisfied."

## 🔍 Verification Focus

-   🧪 Detection coverage under nominal, boundary, and representative
    fault injections.
-   ⚖️ False-positive/false-negative limits for fault monitors.
-   ⏱️ Deterministic transition timing to safe state.
-   🔁 Repeatability of protection behavior across reruns.

⚠️ Common Anti-Patterns \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- 🔴
Safety requirements without linked hazard IDs. - 🔴 Missing time bounds
for detection or mitigation. - 🟡 Safe state described qualitatively
(not measurable). - 🟡 Residual risk left without owner or closure
action.

## ✅ Review Questions

-   Does every hazard have at least one linked safety requirement?
-   Can the safety mechanism be bypassed unintentionally?
-   Are detection/mitigation latencies measurable and tested?
-   Is residual risk disposition documented with owner and due action?

## 🧩 Review Heuristic

If you cannot point to a hazard link, time bound, and verification
artifact, classify the requirement as 🟡 draft and refine before design
freeze.
