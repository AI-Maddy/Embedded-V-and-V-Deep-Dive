---
title: "Layer 1  Modelling Environments"
description: "Auto-generated from filename."
pubDate: 2026-03-24
---

# 🏗️ Layer 1 --- Modelling Environments

**MATLAB / Simulink (MathWorks)**

The industry-standard block-diagram environment for flight-control MIL.

+---------------------+------------------------------------------------+
| Aspect              | Detail                                         |
+=====================+================================================+
| 📦 Relevant         | Simulink · Aerospace Blockset · Simulink       |
| toolboxes           | Design Verifier · Simulink Requirements ·      |
|                     | Simulink Coverage · Embedded Coder             |
+---------------------+------------------------------------------------+
| 🔧 Setup steps      | 1.  Install via MathWorks license server       |
|                     |     (version-locked).                          |
|                     | 2.  Enable `slprj/` build artefact capture in  |
|                     |     SLX project.                               |
|                     | 3.  Configure `sl_customization.m` for company |
|                     |     standards.                                 |
|                     | 4.  Validate environment with `sldemo_f14`     |
|                     |     smoke test.                                |
+---------------------+------------------------------------------------+
| ⚠️ DO               |                                                |
| -178C gotcha \| Sim |                                                |
| ulink Design Verifi |                                                |
| er results are **no |                                                |
| t** a substitute \| |                                                |
|                     |                                                |
| :   | for           |                                                |
|       structural    |                                                |
|       coverage data |                                                |
|       from          |                                                |
|       qualified     |                                                |
|       execution.    |                                                |
+---------------------+------------------------------------------------+
| 📜 Qualification    | DO-330 TQL-1 via MathWorks IEC Certification   |
| path                | Kit + DO Qualification Kit (requires separate  |
|                     | purchase + SOI review).                        |
+---------------------+------------------------------------------------+
| 🔗 Version control  | Use `.slx` binary diff with `matlab.unittest`  |
|                     | CI hooks.                                      |
+---------------------+------------------------------------------------+

**Ansys SCADE Suite**

Formally-proven synchronous dataflow environment targeting DAL-A
avionics software.

+---------------------+------------------------------------------------+
| Aspect              | Detail                                         |
+=====================+================================================+
| 📦 Modules          | SCADE Suite · SCADE Display · SCADE Test · KCG |
|                     | code gen                                       |
+---------------------+------------------------------------------------+
| 🔧 Setup steps      | 1.  Install with avionics profile; lock KCG    |
|                     |     version in CI.                             |
|                     | 2.  Configure qualification data package (QDP) |
|                     |     path.                                      |
|                     | 3.  Validate via official Ansys DO-178C QDP    |
|                     |     smoke test.                                |
+---------------------+------------------------------------------------+
| ✅ Advantage        | KCG code generator ships with a pre-qualified  |
|                     | DO-330 TQL-1 data package accepted by major    |
|                     | certification authorities.                     |
+---------------------+------------------------------------------------+
| ⚠️ Pitfall \| SC    |                                                |
| ADE model tests do  |                                                |
| **not** automatical |                                                |
| ly satisfy MC/DC \| |                                                |
|                     |                                                |
| :   | at            |                                                |
|       source-code   |                                                |
|       level ---     |                                                |
|       still need    |                                                |
|                     |                                                |
|     LDRA/VectorCAST |                                                |
|       on KCG        |                                                |
|     | output if     |                                                |
|       structural    |                                                |
|       coverage is   |                                                |
|       explicitly    |                                                |
|       required.     |                                                |
+---------------------+------------------------------------------------+

------------------------------------------------------------------------
