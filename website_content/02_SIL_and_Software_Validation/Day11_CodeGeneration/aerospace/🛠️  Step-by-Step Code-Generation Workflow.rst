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

