Description — Automotive
========================

🎯 Purpose
----------
Define Automotive Day01 use-case intent in a way that is **safety-linked, measurable, and verifiable** across MIL activities.

🌈 Readiness Legend
------------------
- 🟢 **Ready**: requirement and scenario are measurable with clear pass/fail.
- 🟡 **Partial**: intent exists, but assumptions/timing/ownership are incomplete.
- 🔴 **Risky**: ambiguous behavior or no traceable verification path.

🧭 Domain Alignment (Automotive)
-------------------------------
- 📘 Standards: **ISO 26262 (ASIL)** and **ISO 21434** (cybersecurity context).
- ⚠️ Hazard themes: unintended acceleration/deceleration, loss of stability, braking faults.
- 🔌 Interfaces: CAN, LIN, FlexRay, Automotive Ethernet.

🚗 Scenario Set (Memorable 3-Pack)
----------------------------------
- ✅ **Nominal**: adaptive cruise tracks target speed and gap under normal traffic.
- ⚖️ **Boundary**: stop-and-go with tight headway, latency limits, and noisy sensor edges.
- 🧨 **Fault**: radar dropout, implausible wheel-speed values, or malformed CAN frame.

🧠 Make It Memorable: ``D.R.I.V.E``
-----------------------------------
- **D — Define trigger**: exact event that starts behavior.
- **R — Range-bound output**: limits/units explicitly stated.
- **I — Interface-aware**: bus timing and signal validity constraints captured.
- **V — Verify method**: analysis/test/inspection selected per requirement.
- **E — Evidence trace**: requirement ↔ scenario ↔ result ↔ review.

📋 Practical Example (ACC)
-------------------------
- Requirement: “When lead-vehicle distance error exceeds 8 m, ACC shall reduce commanded torque within 150 ms and restore time-gap to 1.8 ± 0.2 s within 3.0 s under nominal road-load conditions.”
- Verification plan:
	- 🧮 Analysis: control-law and timing budget feasibility.
	- 🧪 Test: nominal/boundary/fault MIL scenarios with logged latency.
	- 📋 Inspection: requirement wording, units, assumptions, and trace links.

⚠️ Anti-Patterns to Avoid
------------------------
- 🔴 Domain-agnostic statements without measurable criteria.
- 🔴 Ignoring bus/interface timing while claiming functional compliance.
- 🟡 Closing findings without residual-risk statement and owner.

✅ Day01 Checklist
-----------------
- Are assumptions and operational design domain limits explicit?
- Are acceptance criteria quantitative (time, range, thresholds)?
- Is each scenario linked to requirement IDs and expected artifacts?
- Is at least one fault scenario tied to safe/degraded behavior?
- Are unresolved risks tagged with owner and next action?

🧩 Review Heuristic
------------------
If an Automotive claim cannot be tied to a requirement ID, a scenario result, and a timestamped artifact, confidence remains 🟡 provisional.
