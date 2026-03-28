⚙️ Aerospace Focus — Day 11: Code Generation
===============================================

.. image:: _images/badge_phase_sil.svg
   :alt: Phase: SIL

.. image:: _images/badge_standard_do178c.svg
   :alt: Standard: DO-178C / DO-331

.. image:: _images/badge_criticality_dal.svg
   :alt: Criticality: DAL-A

.. image:: _images/badge_focus_codegen.svg
   :alt: Focus: Code Generation

.. note::
   🔀 **The Transition Point** — Today the model stops being a simulation
   artifact and becomes a **source of production code**.  In DO-178C terms, the
   model is now a "design representation" (DO-331 §MB.6.3) and the generated
   code must satisfy **every** objective in Table A-5 (software coding standards)
   and Table A-7 (verification of outputs).  A single unverified code-generation
   setting can propagate a latent fault from a Simulink block into the flight
   computer.  This day ensures that the code-generation pipeline itself is
   trustworthy, traceable, and evidence-ready.

----

🎯 Objective
------------

Establish an **aerospace-grade code-generation pipeline** from a verified MIL
model to production-ready C code, with full traceability from Simulink blocks →
generated source → requirements, verified against DO-178C / DO-331 objectives
for DAL-A software.

----

🔭 Phase Context
----------------

.. list-table::
   :widths: 30 70
   :header-rows: 0

   * - 🏗️ **Phase**
     - SIL (Software-in-the-Loop) — code generation entry point
   * - 🎯 **Primary Focus**
     - Model → C code translation with DO-178C compliance
   * - 🔬 **Section Focus**
     - Aerospace code-generation pipeline, settings, and evidence
   * - 📋 **Lifecycle Standard**
     - DO-178C Tables A-4/A-5 + DO-331 (MBDV) + DO-330 (tool qual)
   * - 💾 **Key Artifact**
     - Generated C source + code-gen report + traceability matrix

----

🏗️  Code-Generation Pipeline Architecture
--------------------------------------------

.. code-block:: text

   ┌─────────────────────────────────────────────────────────────────────────────┐
   │              AEROSPACE CODE-GENERATION PIPELINE                            │
   │                                                                            │
   │  ┌──────────────────┐                                                      │
   │  │  Verified MIL     │  ← model.slx (hash-locked, MIL-passed)              │
   │  │  Model (Simulink) │  ← params.mat (calibration data)                    │
   │  └────────┬─────────┘                                                      │
   │           │                                                                │
   │           ▼                                                                │
   │  ┌──────────────────────────────────────────────────┐                      │
   │  │  ① CODE-GENERATION SETTINGS REVIEW                │                      │
   │  │     • Solver: fixed-step, discrete or ode4                              │
   │  │     • Target: Embedded Coder → ert.tlc                                  │
   │  │     • Data types: single / int32 (no double on target)                  │
   │  │     • Overflow: Saturate on overflow (no wrap)                          │
   │  │     • Optimizations: constrained by traceability                        │
   │  └────────┬─────────────────────────────────────────┘                      │
   │           │                                                                │
   │           ▼                                                                │
   │  ┌──────────────────────────────────────────────────┐                      │
   │  │  ② CODE GENERATION (Embedded Coder / SCADE KCG)   │                      │
   │  │     • rtwbuild('FCS_Pitch_Autopilot')                                   │
   │  │     • or: scade -codegen -config dal_a.cfg                              │
   │  │     • Output: src/*.c + src/*.h + codegen_report                        │
   │  └────────┬─────────────────────────────────────────┘                      │
   │           │                                                                │
   │           ▼                                                                │
   │  ┌──────────────────────────────────────────────────┐                      │
   │  │  ③ CODE REVIEW & STANDARDS CHECK                   │                      │
   │  │     • MISRA C:2012 compliance (mandatory, DAL-A)                        │
   │  │     • Naming conventions, file structure                                │
   │  │     • Dead code / unreachable path analysis                             │
   │  │     • Traceability: block ↔ source line mapping                         │
   │  └────────┬─────────────────────────────────────────┘                      │
   │           │                                                                │
   │           ▼                                                                │
   │  ┌──────────────────────────────────────────────────┐                      │
   │  │  ④ BUILD & COMPILE (Cross-compiler)                │                      │
   │  │     • Target: PowerPC / ARM Cortex-R (FCC HW)                           │
   │  │     • Compiler: GHS MULTI / Wind River Diab / GCC                       │
   │  │     • Warnings: -Wall -Werror -Wextra                                  │
   │  │     • Optimization: -O1 or -O0 (DAL-A: limited)                         │
   │  └────────┬─────────────────────────────────────────┘                      │
   │           │                                                                │
   │           ▼                                                                │
   │  ┌──────────────────────────────────────────────────┐                      │
   │  │  ⑤ EVIDENCE PACKAGING                              │                      │
   │  │     • codegen_report.html (block → .c traceability)                     │
   │  │     • MISRA report (zero violations for DAL-A)                          │
   │  │     • compiler_output.log (zero warnings)                               │
   │  │     • SHA-256 hashes for model + generated code                         │
   │  └──────────────────────────────────────────────────┘                      │
   └─────────────────────────────────────────────────────────────────────────────┘

----

⚖️  Domain Constraints
-----------------------

.. warning::
   ⚠️ For DAL-A software, the code generator is a **development tool** under
   DO-330.  If its output is not independently verified (review + test + static
   analysis), the tool must be qualified to **TQL-1** — the most demanding level.
   Most projects choose to verify the output instead.

+----------------------------+------------------------------------------------------------+
| Constraint                 | Detail                                                     |
+============================+============================================================+
| 📜 Compliance baseline     | DO-178C §6.3 (coding standards) + DO-331 §MB.6.3 (MBDV    |
|                            | code gen) + DO-330 §12 (tool qualification)                |
+----------------------------+------------------------------------------------------------+
| 🔧 Code-gen tool class     | **Development tool** — output must be verified, or tool     |
|                            | qualified to TQL-1.                                        |
+----------------------------+------------------------------------------------------------+
| 🎯 Target compliance       | MISRA C:2012 (all mandatory + required rules) for DAL-A.   |
|                            | Advisory rules reviewed and justified.                     |
+----------------------------+------------------------------------------------------------+
| 🔢 Numeric constraints     | No ``double`` on target (single-core FCC with no FPU       |
|                            | double support).  All floating-point is ``float``          |
|                            | (single) or fixed-point ``int32``.                         |
+----------------------------+------------------------------------------------------------+
| 🔒 Optimization limits     | Compiler optimization ≤ **-O1** for DAL-A to preserve      |
|                            | source–object traceability (DO-178C §6.3.4.c).             |
+----------------------------+------------------------------------------------------------+
| 📂 Traceability            | Every generated C function must trace back to a Simulink   |
|                            | block and forward to a requirement ID.                     |
+----------------------------+------------------------------------------------------------+

----

🛠️  Code-Generation Settings — Critical Decisions
---------------------------------------------------

.. rubric:: 🎛️ Embedded Coder Configuration (``ert.tlc``)

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Setting
     - DAL-A Recommended Value
     - Rationale
   * - **System target file**
     - ``ert.tlc``
     - Embedded Real-Time — no OS dependencies, bare-metal.
   * - **Solver**
     - Fixed-step, ``ode4`` or Discrete
     - Variable-step solvers generate unpredictable timing.
   * - **Fixed-step size**
     - 0.005 s (200 Hz) or 0.01 s (100 Hz)
     - Must match FCC frame rate exactly.
   * - **Data type replacement**
     - ``double → single`` globally
     - Target FCC has no double-precision FPU.
   * - **Overflow action**
     - ``Saturate on integer overflow``
     - ``Wrap`` masks range errors silently.
   * - **Signal storage reuse**
     - ``Off`` for DAL-A
     - Preserves 1:1 block → variable traceability.
   * - **Code interface packaging**
     - ``Reusable function``
     - Allows unit testing of individual subsystems.
   * - **Generate code only**
     - ``On``
     - Separate build step with project cross-compiler.
   * - **Code-gen report**
     - **Always generate**
     - Primary traceability evidence artifact.
   * - **MISRA C:2012 checks**
     - ``On`` (Model Advisor)
     - Pre-generation compliance validation.

.. rubric:: 🔧 SCADE KCG Configuration (Alternative)

.. code-block:: text

   scade -codegen                          \
     -config dal_a.cfg                     \
     -target c                             \
     -root FCS_Pitch_Controller            \
     -output_dir generated_code/           \
     -integration_code on                  \
     -traceability on                      \
     -misra_c_2012 mandatory+required      \
     -proof_obligations on

.. tip::
   💡 SCADE KCG is a **qualified code generator** (DO-330 TQL-1) — its output
   does not require independent verification of the translation.  However,
   the *model* still requires full verification (DO-331).  This is why many
   DAL-A programs choose SCADE: it eliminates the code-review-of-generated-code
   burden, saving hundreds of engineering hours.

----

🗂️  Generated Code Structure
-------------------------------

.. code-block:: text

   generated_code/
   ├── 📄 FCS_Pitch_Autopilot.c              ← main step function
   ├── 📄 FCS_Pitch_Autopilot.h              ← public interface
   ├── 📄 FCS_Pitch_Autopilot_private.h      ← internal types
   ├── 📄 FCS_Pitch_Autopilot_types.h        ← data type definitions
   ├── 📄 FCS_Pitch_Autopilot_data.c         ← calibration constants
   ├── 📄 rtwtypes.h                         ← Simulink base types
   ├── 📄 rt_nonfinite.c                     ← NaN/Inf guard (if any)
   │
   ├── subsystems/
   │   ├── 📄 PitchRateLimiter.c             ← rate-limiter subsystem
   │   ├── 📄 ModeLogic.c                    ← mode state machine
   │   ├── 📄 SensorVoting.c                 ← triplex sensor voter
   │   ├── 📄 EnvelopeProtection.c           ← limit checking
   │   └── 📄 ActuatorCommand.c              ← elevator servo output
   │
   ├── integration/
   │   ├── 📄 FCS_step.c                     ← 200 Hz cyclic entry point
   │   ├── 📄 FCS_init.c                     ← power-on initialization
   │   └── 📄 FCS_terminate.c                ← shutdown sequence
   │
   └── reports/
       ├── 📊 codegen_report.html            ← block ↔ code traceability
       ├── 📋 misra_report.html              ← MISRA C:2012 compliance
       └── 🔒 file_manifest.sha256           ← integrity hashes

----

🔀  Model → Code Traceability
-------------------------------

.. code-block:: text

   ┌──────────────────────────────────────────────────────────────────────────┐
   │                    TRACEABILITY CHAIN                                    │
   │                                                                          │
   │  Requirement        Simulink Block          Generated C Code              │
   │  ─────────────      ──────────────          ────────────────              │
   │                                                                          │
   │  PA-REQ-001   ──►   PID_Pitch/Sum1    ──►   FCS_Pitch_Autopilot.c:142   │
   │  (pitch track)      PID_Pitch/Gain1          rtb_Sum1 = ...              │
   │                                                                          │
   │  PA-REQ-003   ──►   ModeLogic/         ──►   ModeLogic.c:87             │
   │  (mode trans)       Stateflow Chart          switch(mode_state) { ...    │
   │                                                                          │
   │  PA-REQ-005   ──►   EnvProtect/        ──►   EnvelopeProtection.c:54    │
   │  (saturation)       Saturation Block         if (cmd > 25.0f) cmd=25.0f; │
   │                                                                          │
   │  PA-REQ-006   ──►   SensorVoting/      ──►   SensorVoting.c:31          │
   │  (IMU switch)       Voter Logic              median_select(imu, 3);      │
   │                                                                          │
   └──────────────────────────────────────────────────────────────────────────┘

   Evidence artifact:  codegen_report.html  →  every block ↔ line mapping
   Anchored to:        Git commit hash + model SHA-256

----

🛠️  Step-by-Step Code-Generation Workflow
-------------------------------------------

.. rubric:: Step ① — Pre-Generation Model Checks (30 min)

.. code-block:: matlab

   %% === PRE-GENERATION MODEL ADVISOR CHECKS ===
   % Run the DO-178C/DO-331 Model Advisor checks before generating code.

   model = 'FCS_Pitch_Autopilot';
   load_system(model);

   % Run Embedded Coder checks
   maObj = Simulink.ModelAdvisor.getModelAdvisor(model);
   maObj.run();

   % Check for MISRA compliance readiness
   misra_results = slcheck.runMISRA(model, 'MISRA C:2012');
   fprintf('MISRA pre-check: %d violations found\n', misra_results.numViolations);

   if misra_results.numViolations > 0
       error('❌ Fix MISRA violations before code generation');
   end
   fprintf('✅ Model passes pre-generation checks\n');

.. rubric:: Step ② — Code Generation (15 min)

.. code-block:: matlab

   %% === CODE GENERATION ===
   model = 'FCS_Pitch_Autopilot';

   % Lock configuration
   cs = getActiveConfigSet(model);
   set_param(cs, 'SystemTargetFile',    'ert.tlc');
   set_param(cs, 'SolverType',          'Fixed-step');
   set_param(cs, 'FixedStep',           '0.005');       % 200 Hz
   set_param(cs, 'DefaultParameterBehavior', 'Inlined');
   set_param(cs, 'GenerateReport',      'on');
   set_param(cs, 'LaunchReport',        'off');
   set_param(cs, 'SupportNonFinite',    'off');         % No NaN/Inf in flight code
   set_param(cs, 'PurelyIntegerCode',   'off');         % single-precision float OK
   set_param(cs, 'LifeSpan',            'inf');         % No counter overflow
   set_param(cs, 'SaturateOnIntegerOverflow', 'on');

   % Generate code (do not build — separate cross-compile step)
   set_param(cs, 'GenCodeOnly', 'on');
   rtwbuild(model);

   fprintf('✅ Code generated to: %s\n', ...
       fullfile(pwd, model, 'generated_code'));

.. rubric:: Step ③ — Post-Generation Integrity Check (Python)

.. code-block:: python

   #!/usr/bin/env python3
   """codegen_verify.py — Verify generated code integrity and traceability."""
   import hashlib, json, os, re
   from pathlib import Path

   GEN_DIR = Path("generated_code")

   # --- 1. Hash all generated files ---
   hashes = {}
   for f in sorted(GEN_DIR.rglob("*")):
       if f.is_file():
           hashes[str(f.relative_to(GEN_DIR))] = hashlib.sha256(
               f.read_bytes()).hexdigest()

   json.dump(hashes, open(GEN_DIR / "file_manifest.json", "w"), indent=2)
   print(f"🔒 {len(hashes)} files hashed")

   # --- 2. Check for prohibited constructs ---
   prohibited = [
       (r'\bdouble\b',        "double-precision type found (target has no double FPU)"),
       (r'\bmalloc\b',        "dynamic allocation found (prohibited in flight code)"),
       (r'\bfree\b',          "dynamic deallocation found"),
       (r'\bsystem\b',        "system() call found (prohibited)"),
       (r'\bgoto\b',          "goto found (MISRA C:2012 Rule 15.1)"),
       (r'#pragma\s+pack',    "pragma pack may cause alignment issues on target"),
   ]

   violations = []
   for c_file in sorted(GEN_DIR.rglob("*.c")):
       code = c_file.read_text()
       for pattern, message in prohibited:
           matches = list(re.finditer(pattern, code))
           for m in matches:
               line_no = code[:m.start()].count('\n') + 1
               violations.append(f"  ❌ {c_file.name}:{line_no} — {message}")

   if violations:
       print(f"\n🚨 {len(violations)} prohibited constructs found:")
       for v in violations:
           print(v)
   else:
       print("✅ No prohibited constructs in generated code")

   # --- 3. Verify traceability completeness ---
   # Check that codegen_report.html exists and has block mappings
   report = GEN_DIR / "reports" / "codegen_report.html"
   if report.exists():
       html = report.read_text()
       block_refs = len(re.findall(r'slwebview', html))
       print(f"📊 Traceability report: {block_refs} block references found")
   else:
       print("⚠️  codegen_report.html not found — traceability gap!")

.. rubric:: Step ④ — Cross-Compilation (20 min)

.. code-block:: bash

   #!/bin/bash
   # cross_compile.sh — Build generated code for FCC target
   set -euo pipefail

   TARGET_ARCH="powerpc-eabispe"          # or arm-none-eabi
   COMPILER="powerpc-eabispe-gcc"         # GHS: ccppc, Diab: dcc
   OPT_LEVEL="-O1"                        # DAL-A: max -O1
   WARNINGS="-Wall -Werror -Wextra -Wpedantic -Wconversion"
   STD="-std=c99"                         # MISRA C:2012 subset

   SRC_DIR="generated_code"
   BUILD_DIR="build/${TARGET_ARCH}"
   mkdir -p "$BUILD_DIR"

   echo "🔨 Cross-compiling for ${TARGET_ARCH} ..."

   $COMPILER $STD $OPT_LEVEL $WARNINGS    \
       -I"$SRC_DIR"                        \
       -I"$SRC_DIR/subsystems"             \
       -c "$SRC_DIR"/*.c                   \
       -c "$SRC_DIR/subsystems"/*.c        \
       -c "$SRC_DIR/integration"/*.c       \
       -o "$BUILD_DIR/FCS_Pitch.o"         \
       2>&1 | tee "$BUILD_DIR/compiler_output.log"

   # Check for warnings (should be zero with -Werror)
   WARNS=$(grep -c "warning:" "$BUILD_DIR/compiler_output.log" || true)
   if [ "$WARNS" -gt 0 ]; then
       echo "❌ $WARNS compiler warnings — must resolve for DAL-A"
       exit 1
   fi

   echo "✅ Cross-compilation successful — zero warnings"

   # Capture object size
   size "$BUILD_DIR/FCS_Pitch.o" | tee "$BUILD_DIR/size_report.txt"

.. rubric:: Step ⑤ — MISRA C:2012 Static Analysis

.. code-block:: python

   #!/usr/bin/env python3
   """misra_check.py — Run MISRA C:2012 analysis on generated code."""
   import subprocess, json, sys

   # Using Polyspace (example — adapts to PC-lint, LDRA, etc.)
   result = subprocess.run([
       "polyspace-bug-finder",
       "-sources", "generated_code/",
       "-results-dir", "misra_results/",
       "-checkers", "misra-c-2012-mandatory,misra-c-2012-required",
       "-report-format", "json",
   ], capture_output=True, text=True)

   report = json.load(open("misra_results/report.json"))

   mandatory_violations = [v for v in report["violations"]
                           if v["category"] == "mandatory"]
   required_violations  = [v for v in report["violations"]
                           if v["category"] == "required"]

   print(f"📋 MISRA C:2012 Results:")
   print(f"  Mandatory violations: {len(mandatory_violations)}")
   print(f"  Required violations:  {len(required_violations)}")

   if mandatory_violations:
       print("\n🚨 MANDATORY violations (must fix for DAL-A):")
       for v in mandatory_violations:
           print(f"  ❌ Rule {v['rule']}: {v['file']}:{v['line']} — {v['message']}")
       sys.exit(1)

   if required_violations:
       print("\n⚠️  REQUIRED violations (must fix or formally deviate):")
       for v in required_violations:
           print(f"  ⚠️  Rule {v['rule']}: {v['file']}:{v['line']} — {v['message']}")

   print("\n✅ MISRA C:2012 analysis complete")

----

🔧  DO-330 Tool Qualification for Code-Generation Tools
---------------------------------------------------------

.. list-table::
   :widths: 25 12 63
   :header-rows: 1

   * - Tool
     - TQL
     - Rationale
   * - 🔀 **Embedded Coder** (Simulink → C)
     - TQL-1 *or* verified output
     - Development tool: output (C code) is part of the software. If output
       is independently verified (review + SIL test + static analysis), TQL-1
       qualification is avoided. Most DAL-A programs choose verification.
   * - 🔀 **SCADE KCG** (SCADE → C)
     - TQL-1 (pre-qualified)
     - KCG has existing DO-330 TQL-1 qualification kit. No additional
       verification of the *translation* is needed; model-level verification
       still required.
   * - 🔨 **Cross-compiler** (C → object code)
     - TQL-1 *or* OCV
     - Object Code Verification (Day 18) can substitute for compiler
       qualification at DAL-A. At DAL-B/C, review of compiler warnings
       + exhaustive testing may suffice.
   * - 📋 **MISRA checker** (Polyspace / PC-lint)
     - TQL-5
     - Verification tool: can fail to detect violations but cannot insert
       errors. TQL-5 = operational requirements only.
   * - 📊 **Simulink Coverage**
     - TQL-5
     - Verification/measurement tool.

----

🧪  Code-Generation Verification Scenarios
--------------------------------------------

.. list-table::
   :widths: 12 40 25 23
   :header-rows: 1

   * - Scenario
     - Description
     - Verification Method
     - Acceptance Criterion
   * - **CG-VER-01**
     - Generated code compiles with zero warnings on target
       compiler at -O1, -Werror.
     - Cross-compilation
     - ``compiler_output.log`` has 0 warnings
   * - **CG-VER-02**
     - No ``double`` type, ``malloc``, ``free``, ``goto``, or
       ``system()`` in generated code.
     - ``codegen_verify.py`` script
     - 0 prohibited constructs found
   * - **CG-VER-03**
     - MISRA C:2012 mandatory rules: zero violations.
       Required rules: zero violations or formal deviation.
     - Polyspace / PC-lint / LDRA
     - MISRA report clean
   * - **CG-VER-04**
     - Codegen report maps every Simulink block to a C source line.
       No unmapped blocks.
     - ``codegen_report.html`` review
     - 100 % block → code coverage
   * - **CG-VER-05**
     - SIL back-to-back: generated C produces identical output
       (within ε) to MIL model for all nominal scenarios.
     - SIL vs MIL comparison (Day 13)
     - ``max|MIL - SIL| < 1e-6`` per signal
   * - **CG-VER-06**
     - Stack usage of generated code fits within FCC stack
       allocation (e.g., 8 KB).
     - Static stack analysis (compiler report)
     - Stack depth ≤ 8192 bytes
   * - **CG-VER-07**
     - WCET of ``FCS_step()`` function fits within 200 Hz frame
       budget (5 ms).
     - Static timing analysis (Day 26)
     - WCET ≤ 4.5 ms (90 % of frame)

----

📊  Embedded Coder vs SCADE KCG Comparison
--------------------------------------------

.. list-table::
   :widths: 25 37 38
   :header-rows: 1

   * - Criterion
     - Embedded Coder
     - SCADE KCG
   * - 🔀 Input model
     - Simulink / Stateflow
     - SCADE Suite (Lustre-based)
   * - 🏷️ Target language
     - C, C++, HDL
     - C (deterministic subset)
   * - 📜 DO-330 status
     - **Not pre-qualified** — output must be verified
     - **TQL-1 pre-qualified** — translation exempt from review
   * - 🎯 MISRA compliance
     - Generated code needs external MISRA check
     - Generated code is MISRA-C:2012 compliant by construction
   * - 🔢 Data types
     - Configurable (may produce ``double`` if not constrained)
     - Strictly typed from model; no implicit promotions
   * - 🔧 Traceability
     - codegen_report.html (block ↔ C line)
     - Built-in proof obligations + traceability report
   * - 💰 Verification cost
     - High (code review + MISRA + SIL back-to-back)
     - Lower (model verification sufficient for translation)
   * - 🏗️ Industry usage
     - Wide (transport, defense, industrial)
     - Primarily aerospace / rail (Airbus, Thales)

----

📂  Evidence Folder Structure
-------------------------------

.. code-block:: text

   Day11_CodeGeneration/
   └── evidence/
       ├── 📋 codegen_settings.json         ← frozen Embedded Coder config
       ├── 📋 env_manifest.json              ← MATLAB version + model hash
       │
       ├── generated_code/
       │   ├── *.c, *.h                      ← generated source
       │   ├── reports/
       │   │   ├── 📊 codegen_report.html    ← block ↔ C traceability
       │   │   ├── 📋 misra_report.html      ← MISRA C:2012 compliance
       │   │   └── 🔒 file_manifest.sha256   ← integrity hashes
       │   └── subsystems/ + integration/
       │
       ├── build/
       │   ├── 📄 FCS_Pitch.o                ← cross-compiled object
       │   ├── 📋 compiler_output.log        ← zero-warning build log
       │   └── 📊 size_report.txt            ← code/data size
       │
       └── traceability/
           ├── 🗺️  req_to_block.csv           ← requirement ↔ block mapping
           ├── 🗺️  block_to_code.csv          ← block ↔ C function mapping
           └── 🗺️  codegen_traceability.csv   ← full chain: req → block → C line

----

✅ Patterns — What Works for Code Generation
-----------------------------------------------

.. tip::
   💡 Patterns from successful DAL-A code-generation campaigns.

1. **🔒 Lock settings before generation** — Export the Embedded Coder
   configuration set to a ``.mat`` file and hash it.  Any change to code-gen
   settings triggers a full re-generation cycle.

2. **🔀 Generate-then-freeze** — Once code is generated and verified, ``chmod
   444`` the directory.  No manual edits to generated code, ever.

3. **📋 Run Model Advisor *before* generation** — Catching a ``double`` type or
   a missing saturation at model level is 10× cheaper than finding it in
   generated C.

4. **🧪 SIL back-to-back immediately** — Don't wait for Day 13; run a quick
   nominal comparison right after generation.  If MIL ≠ SIL, something is wrong
   with the settings.

5. **📊 Measure code size early** — If generated code is 200 KB and the target
   has 256 KB flash, you have a 78 % budget problem that will only get worse.

6. **🔧 Use ``Reusable function`` packaging** — This generates subsystem functions
   with explicit I/O, enabling independent unit testing at SIL level.

----

🚫 Anti-Patterns
------------------

.. danger::
   ❌ These code-generation mistakes have caused program-level rework:

- 🚩 **Manual edits to generated code** — Breaks the model ↔ code traceability.
  If the generated code needs a fix, fix the *model* and re-generate.
- 🚩 **Generating with ``double`` types on a single-precision target** — Silent
  promotion to software emulation, blowing the WCET budget.
- 🚩 **Compiler optimization > -O1** — At DAL-A, aggressive optimization
  (-O2, -O3) can reorder or eliminate code, breaking source-to-object
  traceability and requiring Object Code Verification (OCV).
- 🚩 **Skipping MISRA analysis on generated code** — "The tool generated it,
  so it's fine" is not a valid DO-178C argument unless the tool is TQL-1 qualified.
- 🚩 **No codegen report** — Without the block ↔ code traceability report, there
  is no evidence that the generated code implements the model.
- 🚩 **Wrap on integer overflow** — In flight code, a wrapped 32-bit counter can
  silently invert a control command sign.

----

⚠️  Pitfalls
-------------

.. caution::

   Code-generation-specific traps for aerospace:

   - 🕳️ **Signal storage reuse** — Embedded Coder's optimization can alias two
     signals to the same variable.  This saves RAM but destroys 1:1 traceability.
     Disable for DAL-A.
   - 🕳️ **Fixed-point scaling errors** — If the model uses floating-point but the
     target is fixed-point, the autoscaling step can introduce truncation errors
     exceeding the MIL-SIL tolerance.  Verify scaling with ``fxptdlg``.
   - 🕳️ **Inlined parameters** — Inlining calibration constants into generated code
     means a parameter change requires re-generation + re-compilation.  Consider
     ``Tunable`` parameters for values that change in calibration.
   - 🕳️ **Non-finite support** — The default ``SupportNonFinite = 'on'`` generates
     NaN/Inf guard code.  Flight code should never produce NaN — disable this and
     ensure the model itself is NaN-free.
   - 🕳️ **Licensing during CI** — Embedded Coder requires a license for each
     generation run.  CI pipelines running parallel jobs can exhaust the license
     pool, causing silent generation failures.

----

🏆 Best Practices
------------------

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 🔒
     - Hash the model, parameters, and generated code together in a single
       ``env_manifest.json``.  Any hash mismatch triggers full re-generation.
   * - 📋
     - Include the code-generation report as a **mandatory** artifact in the
       Software Accomplishment Summary (SAS).
   * - 🧪
     - Run a quick 3-scenario SIL back-to-back immediately after generation
       (before committing).  Catch settings errors early.
   * - 📊
     - Track generated code size (text + data + BSS) over time.  A sudden jump
       means a model change introduced unexpected complexity.
   * - 🔒
     - Store generated code in a separate Git branch (``codegen/v4.2``) — never
       mix generated and hand-written code in the same directory.
   * - 📄
     - Document every MISRA deviation with a formal rationale form signed by the
       DER.  "Advisory — not applicable" is not sufficient for DAL-A.

----

🔮 Heuristics
--------------

+-----------------------------------------------+----------------------------------------------+
| Situation                                     | 💡 Action                                    |
+===============================================+==============================================+
| MIL and SIL outputs differ by > 1e-4          | Check: solver step size, data type           |
|                                               | replacement, optimization level.             |
+-----------------------------------------------+----------------------------------------------+
| MISRA checker reports 50+ "required" viols    | Likely a code-gen setting issue — check      |
|                                               | Model Advisor pre-gen report first.          |
+-----------------------------------------------+----------------------------------------------+
| Generated code is 3× the expected size        | Check: dead-code branches from unused        |
|                                               | model variants or unconditional logging.     |
+-----------------------------------------------+----------------------------------------------+
| Compiler warns about implicit type conversion | Model has a type mismatch (e.g., int → float)|
|                                               | — fix at model level, re-generate.           |
+-----------------------------------------------+----------------------------------------------+
| Stack analysis shows 12 KB for an 8 KB target | Flatten deeply nested subsystems or reduce   |
|                                               | local array sizes.  Re-generate and re-check.|
+-----------------------------------------------+----------------------------------------------+

----

📋 Pre-Closure Checklist
--------------------------

.. rubric:: Gate: Must be 100 % complete before proceeding to SIL Setup (Day 12)

- ☐ Embedded Coder / SCADE KCG configuration settings documented and hash-locked.
- ☐ Code generated from verified MIL model (MIL campaign passed — Day 10).
- ☐ ``codegen_report.html`` shows 100 % block → code traceability.
- ☐ Prohibited constructs check (``codegen_verify.py``) passes with 0 findings.
- ☐ MISRA C:2012 mandatory rules: 0 violations.
- ☐ MISRA C:2012 required rules: 0 violations or formal deviation record.
- ☐ Cross-compilation at -O1 succeeds with 0 warnings (``-Werror``).
- ☐ Code size (text + data + BSS) fits within target flash/RAM budget.
- ☐ Stack usage within FCC allocation.
- ☐ Generated code directory write-locked (``chmod 444``), SHA-256 manifest created.
- ☐ DO-330 tool qualification assessment complete for code generator and compiler.
- ☐ Traceability CSV: requirement → Simulink block → C function → C line number.
- ☐ Quick SIL back-to-back sanity (3 nominal scenarios) confirms MIL ≈ SIL.

----

🔗 Related Standards & References
------------------------------------

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Standard
     - Relevance to Code Generation
   * - **DO-178C §6.3**
     - Software coding standards — generated code must comply.
   * - **DO-178C Table A-5**
     - Source code objectives (traceability, accuracy, consistency).
   * - **DO-178C §6.3.4.c**
     - Source-to-object traceability — limits compiler optimization.
   * - **DO-331 §MB.6.3**
     - Model coverage and code-generation requirements for MBDV.
   * - **DO-330 §12**
     - Tool qualification process — code generator and compiler.
   * - **MISRA C:2012**
     - Coding standard for safety-critical C; mandatory for DAL-A.
   * - **ARP4754A §5.4**
     - Development assurance — software as part of system development.
   * - **CAST-32A**
     - Multi-core considerations — relevant if target is multi-core FCC.

----

.. admonition:: 🔀 Remember

   Code generation is not a "push button" step — it is a **design decision**
   with certification consequences.  Every setting in the code-generation
   configuration becomes a line item in the Plan for Software Aspects of
   Certification (PSAC).  Lock the settings, verify the output, hash the
   artifacts, and treat the generated code as what it is: the software that
   will fly.
