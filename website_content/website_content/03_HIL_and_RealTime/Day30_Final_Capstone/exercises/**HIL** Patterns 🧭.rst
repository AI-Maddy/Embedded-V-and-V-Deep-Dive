**HIL** Patterns 🧭
-------------------

*   Define thresholds before execution.
*   Capture one baseline and one stressed comparison artifact.
*   Tie each exercise result to requirement IDs.

**HIL** Anti-Patterns 🚫
----------------------

*   Running tests without fixed configuration snapshots.
*   Declaring pass/fail without quantitative criteria.
*   Logging summaries without raw evidence references.

.. warning:: Running tests without fixed configuration snapshots, declaring pass/fail without quantitative criteria, and logging summaries without raw evidence references are all anti-patterns that can lead to poor evidence quality.

**HIL** Pitfalls ⚠️
------------------

*   Timebase mismatch across tools/interfaces.
*   Incomplete negative-path coverage.
*   Non-deterministic reruns due to hidden setup changes.

**HIL** Examples 📚
-----------------

### Boundary Timing Overrun Scenario 🟡

GIVEN a set of near-limit timing conditions,
WHEN the system is executed with boundary inputs,
THEN the system shall produce the expected outputs and meet the requirement IDs.

*   Define near-limit timing conditions.
*   Capture stressed comparison artifact.
*   Verify that each exercise result meets the requirement IDs.

### Invalid Input Sequence 🔴

GIVEN an invalid input sequence,
WHEN the system is executed with faulty inputs,
THEN the system shall detect and recover from the fault and meet the requirement IDs.

*   Introduce invalid input sequence.
*   Capture expected detection and recovery behavior.
*   Verify that each exercise result meets the requirement IDs.

### Regression Rerun 🟢

GIVEN a consistent setup,
WHEN the exercise is rerun,
THEN the system shall produce the same outputs and meet the requirement IDs.

*   Rerun the exercise with consistent setup.
*   Verify that each exercise result meets the requirement IDs.

