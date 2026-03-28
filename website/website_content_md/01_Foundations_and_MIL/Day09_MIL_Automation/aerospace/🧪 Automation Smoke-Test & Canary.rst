🧪 Automation Smoke-Test & Canary
------------------------------------

.. rubric:: 🐦 Canary Scenario

Before running the full campaign, execute a single known-good scenario as a sanity
gate:

.. code-block:: python

   def canary_check(eng, evidence_root):
       """Run minimal scenario to verify toolchain health."""
       print("🐦 Running canary check ...", flush=True)
       eng.eval("simOut = sim('FCS_MIL_Harness', 'StopTime', '5');", nargout=0)
       pitch_err = eng.workspace["pitch_error_rms"]
       assert pitch_err < 1.0, f"Canary FAILED: pitch_err={pitch_err}"
       print("✅ Canary passed — toolchain healthy")

.. rubric:: 🔁 Determinism Verification

After the campaign, re-run a random 10 % sample and compare logs bit-for-bit:

.. code-block:: python

   import random, filecmp

   def verify_determinism(evidence_root, sample_pct=0.1):
       scenarios = list(evidence_root.glob("*/raw_log.mat"))
       sample = random.sample(scenarios, max(1, int(len(scenarios) * sample_pct)))
       for orig_log in sample:
           # Re-run and save to temp
           rerun_log = rerun_scenario(orig_log.parent / "scenario.json")
           if not filecmp.cmp(str(orig_log), str(rerun_log), shallow=False):
               raise AssertionError(f"❌ Non-determinism detected: {orig_log.parent.name}")
           print(f"  ✅ {orig_log.parent.name} — bit-for-bit match")
       print(f"🧬 Determinism verified for {len(sample)} scenarios")

----

