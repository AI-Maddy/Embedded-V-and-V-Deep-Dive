🔬  Layer 4 — Verification & Coverage Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: VectorCAST / C++ (Vector Informatik)

Automated unit and integration test framework with DO-178C MC/DC coverage reporting.

+----------------------------+-------------------------------------------------------------+
| Aspect                     | Detail                                                      |
+============================+=============================================================+
| 📋 Qualification            | Certified TQL-1 data package available for DO-178C DAL-A/B  |
+----------------------------+-------------------------------------------------------------+
| 📊 Coverage types           | Statement · Branch · MC/DC · Function call                  |
+----------------------------+-------------------------------------------------------------+
| 🔧 MIL link                 | Import Simulink code-gen output (``ert_main.c``) as a       |
|                            | VectorCAST component; map Simulink test cases to VC scripts.|
+----------------------------+-------------------------------------------------------------+
| ⚠️  Pitfall                 | Coverage holes in generated code are often in               |
|                            | ``rtwtypes.h`` cast macros — exclude with documented        |
|                            | deactivated code justification.                             |
+----------------------------+-------------------------------------------------------------+

.. rubric:: LDRA Testbed

Long-established static + dynamic analysis suite used by avionics OEMs for DO-178C
objective satisfaction (Objectives 4, 5, 6 coverage + data coupling).

- **Key features:** MISRA C:2012 checking · data/control coupling analysis · test
  case management · CI integration via Jenkins plugin.
- **TQL-1** qualification kit available for DAL-A programs.

.. rubric:: Polyspace Bug Finder / Code Prover (MathWorks)

Formal static analysis tool; Code Prover can **prove absence** of certain run-time
errors (division-by-zero, overflow, NULL deref) — accepted as analysis evidence
under DO-178C Table A-7 objectives.

- **⚠️  Note:** Polyspace results supplement but do **not** replace structural coverage.
- **Integration:** Run as post-build step; pipe Orange/Red findings to JIRA for triage.

.. rubric:: Reactis (Reactive Systems)

Model-based test generation and coverage measurement directly on Simulink/Stateflow
models — generates test vectors that exercise condition/decision coverage at the
model level.

- **MIL role:** Generate model-level MC/DC test vectors automatically; replay on
  compiled code to confirm coverage transfers.
- **TQL:** TQL-1 qualification data package available.

----

