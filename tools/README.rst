🧰 Tools Playbook
================

🎯 Purpose
----------
Standardize tool usage so outputs are **repeatable, comparable, and auditable** across MIL/SIL/HIL.

🔗 Tool Tracks
--------------
- `CANoe <CANoe/README.rst>`_
- `CANalyzer <CANalyzer/README.rst>`_
- `Wireshark <Wireshark/README.rst>`_
- `TRACE32 <TRACE32/README.rst>`_
- `Ballard ARINC <Ballard_ARINC/README.rst>`_

🧭 Universal Workflow
---------------------
1. Freeze test objective, assumptions, and acceptance criteria.
2. Version-control the tool configuration and runtime options.
3. Execute nominal and edge/fault scenarios.
4. Export raw outputs and derived summaries.
5. Link findings to requirement/objective references.

📦 Minimum Evidence Bundle
--------------------------
- Versioned configuration snapshot
- Timestamped raw output
- Interpreted findings and verdict
- Open issue list with owner/priority

✅ Quality Gates
----------------
- Repeatability verified via rerun comparison.
- Data integrity checked (timestamps and interfaces consistent).
- Findings mapped to objective IDs and risk statements.

⚠️ Cross-Tool Pitfalls
----------------------
- Timebase mismatch across tools and ECU clocks.
- Non-deterministic setup not captured in artifacts.
- Summary conclusions without raw evidence retention.


Additional Deep-Dive Notes
--------------------------
- Domain Focus: General
- Phase Focus: Cross-Phase
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.

Additional Deep-Dive Notes
--------------------------
- Domain Focus: General
- Phase Focus: Cross-Phase
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.
