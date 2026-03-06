Exercises — Day20 SIL MiniProject
=================================

🎯 Exercise Goal
----------------
Practice **Day20 SIL MiniProject** using reproducible tasks that demonstrate **SIL** evidence quality.

🛠️ Practical Focus
------------------
Primary focus: **software correctness, fault robustness, and structural evidence quality**.

📋 Exercise Pack
----------------
1. Nominal scenario with explicit pass/fail criteria.
2. Boundary scenario near limits (timing, value, or mode transitions).
3. Fault/negative scenario with expected detection and recovery behavior.
4. Rerun consistency check for repeatability.

🧭 Patterns
-----------
- Define thresholds before execution.
- Capture one baseline and one stressed comparison artifact.
- Tie each exercise result to requirement IDs.

🚫 Anti-Patterns
----------------
- Running tests without fixed configuration snapshots.
- Declaring pass/fail without quantitative criteria.
- Logging summaries without raw evidence references.

⚠️ Pitfalls
------------
- Timebase mismatch across tools/interfaces.
- Incomplete negative-path coverage.
- Non-deterministic reruns due to hidden setup changes.

📚 Examples
-----------
- Boundary timing overrun scenario with mitigation evidence.
- Invalid input sequence demonstrating robust handling.
- Regression rerun proving fix stability.

✅ Best Practices
----------------
- Keep artifact names stable across reruns.
- Record environment/version metadata every run.
- Include residual risk with each unresolved finding.

🧪 Heuristics
-------------
- One failing test without root cause is incomplete work.
- Repeatability is required for confidence.
- If evidence is missing, result is provisional.

🔎 Checklist
------------
- Pass/fail thresholds are unambiguous.
- Nominal + stress + fault evidence is present.
- Traceability and residual risk are documented.

Additional Deep-Dive Notes
--------------------------
- Domain Focus: General
- Phase Focus: SIL
- Evidence Priorities: functional correctness, timing behavior, robustness, and traceability.
- Patterns: baseline-first comparison, fixed acceptance thresholds, deterministic reruns.
- Anti-Patterns: post-hoc threshold tuning, missing raw artifacts, incomplete negative-path checks.
- Pitfalls: hidden assumptions, interface timing drift, weak requirement-to-test linkage.
- Example Expansion: include one nominal, one boundary, and one fault scenario per objective.
- Review Heuristic: if a claim cannot be tied to an artifact, mark confidence as provisional.
- Checklist Extension: capture residual risk, ownership, and next action for each unresolved item.
