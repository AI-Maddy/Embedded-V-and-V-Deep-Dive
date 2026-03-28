# Functional Requirements --- Day01

## 🎯 Goal

Define observable system behavior so each requirement is clear,
testable, and traceable from Day01 onward.

## 🌈 Quality Legend (Color Cues)

-   🟢 **Ready**: measurable, bounded, and independently verifiable.
-   🟡 **Needs work**: intent is clear, but criteria or conditions are
    incomplete.
-   🔴 **Risky**: ambiguous wording or no objective verification path.

## 🧭 What a Good Functional Requirement Contains

-   **Behavior**: what the system shall do.
-   **Trigger**: when the behavior must occur.
-   **Condition**: under what state/constraints it applies.
-   **Output**: expected result/state change.
-   **Bound**: timing/threshold/range limits.
-   **Verification**: analysis, test, inspection, or demonstration.

## ✍️ Writing Rules (Simple + Strong)

-   Use measurable language (ranges, thresholds, timing limits).
-   State preconditions and interfaces explicitly.
-   Prefer "shall" statements with one clear behavior each.
-   Avoid vague words: *optimize*, *quickly*, *properly*, *normal*.
-   Keep units explicit (ms, Nm, V, %, °C).

## 🧠 Make It Memorable: `S.M.A.R.T-E`

-   **S --- Specific** behavior
-   **M --- Measurable** criteria
-   **A --- Achievable** within system limits
-   **R --- Relevant** to hazard/risk or mission intent
-   **T --- Time-bounded** response/latency defined
-   **E --- Evidence-linked** verification method planned

## 🧩 Requirement Template (Copy/Paste)

-   **ID**:
-   **Function intent**:
-   **Trigger condition**:
-   **Preconditions / system state**:
-   **Expected output/state**:
-   **Timing/performance bound**:
-   **Interfaces/signals involved**:
-   **Verification method** (analysis/test/inspection):
-   **Pass/fail criteria**:

## ✅ Good vs ❌ Weak Example

-   ❌ Weak: "The controller shall respond quickly to speed errors."
-   ✅ Good: "When speed error exceeds 3 km/h, the controller shall
    command corrective torque within 120 ms and reduce speed error below
    1 km/h within 2.0 s under nominal road-load conditions."

## 🔍 Verification Method Difference (Quick View)

-   🧮 **Analysis**: prove by model/math/logical reasoning.
-   🧪 **Test**: execute with inputs and verify measured outputs.
-   📋 **Inspection**: review artifacts against checklist/standard.

## 📌 Day01 Quality Check

-   Is each requirement independently testable?
-   Is pass/fail quantitative and unambiguous?
-   Are dependencies on external interfaces explicit?
-   Is at least one nominal, one boundary, and one fault scenario
    identified?
-   Does each critical requirement have an evidence owner and next
    action?

## 🧩 Review Heuristic

If a requirement cannot be verified objectively, classify it as 🟡 draft
and refine before downstream design.
