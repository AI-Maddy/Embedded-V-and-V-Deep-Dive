🤖  Layer 5 — Test Automation & Reporting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: RT-Tester (Verified Systems International)

Platform-independent test automation tool designed specifically for DO-178C and
EN 50128 SIL-4; widely used in Airbus, Boeing, and Embraer programs.

- **Capabilities:** Time-triggered test scripts · TTCN-3 test suite import · hardware
  abstraction layer for HIL transition · automated verdict generation.
- **MIL integration:** Drive Simulink model via MATLAB Engine API; collect verdict
  and evidence in RT-Tester report format accepted by DERs.

.. rubric:: TPT — Time Partition Testing (PikeTec)

Graphical test modelling tool for embedded control software; especially strong for
time-series-based signal assertions.

+---------------------------+--------------------------------------------------------------+
| Feature                   | Detail                                                       |
+===========================+==============================================================+
| Test modelling            | State-machine-based test cases with signal stimuli + checks  |
+---------------------------+--------------------------------------------------------------+
| Simulink integration      | Direct SL block interface — no code generation required      |
+---------------------------+--------------------------------------------------------------+
| Reporting                 | HTML + PDF report with requirement traceability table        |
+---------------------------+--------------------------------------------------------------+
| DO-178C support           | Qualification kit targeting DAL-A; TQL-1 certificate        |
+---------------------------+--------------------------------------------------------------+

.. rubric:: pytest + MATLAB Engine API (Open-Source Stack)

Lightweight, CI-friendly alternative for teams that cannot afford commercial TQL-1
tools at the MIL phase (qualification is still required before SIL use as evidence).

.. code-block:: python

   # Example: headless Simulink MIL run from pytest
   import matlab.engine, pytest

   @pytest.fixture(scope="session")
   def eng():
       e = matlab.engine.start_matlab()
       e.addpath("models/FCS", nargout=0)
       yield e
       e.quit()

   def test_fcs_nominal_tracking(eng):
       eng.workspace["scenario"] = "NOM_01"
       eng.sim("FCS_MIL_Harness", nargout=0)
       pitch_err = eng.workspace["pitch_error_rms"]
       assert pitch_err < 0.5, f"Pitch RMS {pitch_err:.3f}° exceeds 0.5° threshold"

- **⚠️  TQL warning:** This stack is **not** qualified; all MIL results produced with
  it are engineering data only until the stack is assessed per DO-330.

----

