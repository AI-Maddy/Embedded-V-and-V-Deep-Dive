Concept Note — Day30 Final Capstone
=====================================

🟢 **Domain-Specific Mnemonic Acronym:** HILSPECT (Hardware-In-the-Loop Safety and Performance Evaluation Criteria Toolkit)

Purpose
-------

.. important:: 
    This concept note is designed to provide a quick recall and evidence-driven application in **HIL**.

Core Concept
------------

🔴 **Critical Failure Mode:** Define the primary mechanism and expected behavior.
🟡 **Boundary Condition:** Identify assumptions and boundary conditions.
🟢 **Nominal Behavior:** State what failure looks like and how it should be detected.

Verification Mapping
-------------------

🔗 **Verification Requirements:**

| Requirement ID | Verification Method | Required Evidence Artifact |
| --- | --- | --- |
|  | Analysis | Logs |
|  | Simulation/Test | Traces |
|  | Inspection | Summary Table |

Patterns
--------

🧭 **Safety and Mission Intent:** Start from safety/mission intent and decompose to checks.
🔴 **Measurable Signal/State:** Anchor each claim to a measurable signal/state.
🟡 **Nominal + Stress Perspective:** Capture nominal + stress perspective in a single note.

Anti-Patterns
-------------

🚫 **Intuition Without Artifact Evidence:** Relying on intuition without artifact evidence.
🟡 **Ignoring Coupling Between Interfaces and Timing:** Ignoring coupling between interfaces and timing.
🔴 **Recording Outcomes Without Requirement References:** Recording outcomes without requirement references.

Pitfalls
--------

⚠️ **Hidden Assumptions:** Hidden assumptions reducing reproducibility.
🟡 **Boundary Behavior Left Uncharacterized:** Boundary behavior left uncharacterized.
🔴 **Traceability Gaps:** Traceability gaps between concept and test.

Examples
--------

📚 **Good Practice:** Requirement-linked concept with explicit thresholds.
🟡 **Weak Practice:** Broad statement with no observable acceptance signal.
🔴 **Critical Practice:** Concept that fails under a specific fault mode.

Best Practices
--------------

✅ **One Concept Note Per Topic Decision Point:** Keep one concept note per topic decision point.
🟡 **Highlight Uncertainty and Confidence:** Highlight uncertainty and confidence explicitly.
🔴 **Update Note When Assumptions Change:** Update note whenever assumptions change.

Heuristics
----------

🧪 **What Must Always Remain True?:** What must always remain true?
🟡 **What Fails First Near Limits?:** What fails first near limits?
🔴 **What Artifact Proves the Verdict?:** What artifact proves the verdict?

Checklist
---------

☐ **Boundaries Are Clear:** Boundaries are clear.
☐ **Failure Criteria Are Explicit:** Failure criteria are explicit.
☐ **Evidence Hooks Are Identified:** Evidence hooks are identified.
☐ **Reviewer Can Reproduce the Reasoning:** Reviewer can reproduce the reasoning.

Phase Focus
-----------

🔴 **Real-Time Integration Behavior:** This day emphasizes: **real-time integration behavior, interface timing, and hardware realism**.

Pre-Review Checklist
---------------------

☐ **Domain-Specific Mnemonic Acronym:** HILSPECT is used throughout the document.
☐ **Domain Standards References:** Relevant domain standards references are included (e.g., DO-178C, DO-254, ISO 26262, IEC 62304, ARP4754A/4761, ASPICE).
☐ **RST Admonitions:** RST admonitions (.. note::, .. warning::, .. important::, .. admonition::) are used throughout the document.
☐ **GIVEN / WHEN / THEN Scenario Templates:** GIVEN / WHEN / THEN scenario templates (nominal 🟢, boundary 🟡, fault 🔴) are used throughout the document.
☐ **List-Table:: for Tabular Content:** List-table:: is used for tabular content.
☐ **Severity / Priority Colour Legend:** Severity / priority colour legend (🟢🟡🔴) is used throughout the document.
