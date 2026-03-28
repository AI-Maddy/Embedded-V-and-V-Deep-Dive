# 🔧 DO-330 Tool Qualification for Code-Generation Tools

+-----------------+-------+--------------------------------------------+
| Tool            | TQL   | Rationale                                  |
+=================+=======+============================================+
| 🔀 **Embedded   | TQL-1 | Development tool: output (C code) is part  |
| Coder**         | *or*  | of the software. If output is              |
| (Simulink → C)  | ver   | independently verified (review + SIL       |
|                 | ified | test + static analysis), TQL-1             |
|                 | o     | qualification is avoided. Most DAL-A       |
|                 | utput | programs choose verification.              |
+-----------------+-------+--------------------------------------------+
| 🔀 **SCADE      | TQL-1 | KCG has existing DO-330 TQL-1              |
| KCG** (SCADE →  | (pre- | qualification kit. No additional           |
| C)              | quali | verification of the *translation* is       |
|                 | fied) | needed; model-level verification still     |
|                 |       | required.                                  |
+-----------------+-------+--------------------------------------------+
| 🔨              | TQL-1 | Object Code Verification (Day 18) can      |
| **C             | *or*  | substitute for compiler qualification at   |
| ross-compiler** | OCV   | DAL-A. At DAL-B/C, review of compiler      |
| (C → object     |       | warnings                                   |
| code)           |       |                                            |
|                 |       | -   exhaustive testing may suffice.        |
+-----------------+-------+--------------------------------------------+
| 📋 **MISRA      | TQL-5 | Verification tool: can fail to detect      |
| checker**       |       | violations but cannot insert errors. TQL-5 |
| (Polyspace /    |       | = operational requirements only.           |
| PC-lint)        |       |                                            |
+-----------------+-------+--------------------------------------------+
| 📊 **Simulink   | TQL-5 | Verification/measurement tool.             |
| Coverage**      |       |                                            |
+-----------------+-------+--------------------------------------------+

------------------------------------------------------------------------
