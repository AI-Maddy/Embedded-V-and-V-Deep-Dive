Theory — Day01 V-Model and Requirements
=======================================

🎯 Learning Goal
----------------
Understand how requirement intent, verification strategy, and evidence evolve across the V-model so that every claim can be proven with artifacts.

🌈 Visual Legend (Color Cues)
----------------------------
- 🟢 **Confident**: requirement is clear, testable, and traceable.
- 🟡 **Watch**: partially defined (missing criteria, owner, or method).
- 🔴 **Risk**: ambiguous requirement or no valid verification path.

🧭 V-Model in One View
---------------------

.. list-table::
	 :header-rows: 1
	 :widths: 28 32 40

	 * - Left Side (Definition)
		 - Right Side (Verification)
		 - Key Evidence Question
	 * - User/System Requirements
		 - Validation at system level
		 - “Did we build the right thing?”
	 * - Architecture / Subsystem Design
		 - Integration testing
		 - “Do interfaces and behaviors match design intent?”
	 * - Component / Unit Design
		 - Unit testing + static checks
		 - “Did we build each unit right?”

🧱 Core Concepts
---------------
- ✅ **Verification** asks: “Did we build it right?”
- ✅ **Validation** asks: “Did we build the right thing?”
- 🔁 **Decomposition** flows requirements downward into implementable detail.
- 🔗 **Integration evidence** must roll back upward to original intent.

🛡️ Safety-Critical Framing
-------------------------
- A strong requirement is **testable, bounded, and unambiguous**.
- Hazard/risk-linked requirements need explicit rationale and measurable thresholds.
- Traceability protects confidence when change, defects, or rework happens.

🧠 Make It Memorable: ``V.E.R.I.F.Y``
-------------------------------------
- **V — Value intent**: why this requirement matters.
- **E — Evidence path**: analysis/test/inspection planned.
- **R — Risk linkage**: hazard or failure mode connected.
- **I — Inputs bounded**: ranges, preconditions, interfaces defined.
- **F — Fail criteria clear**: explicit pass/fail thresholds.
- **Y — Yield traceability**: requirement ↔ test ↔ result ↔ review.

🧪 Practical Output for Day01
----------------------------
- Requirement intent notes with assumptions captured.
- Verification method map (analysis/test/inspection/demonstration).
- Initial trace links for nominal, boundary, and fault scenarios.
- Open-risk list with owner and next action.

🔍 Analysis vs Test vs Inspection (with Example)
-----------------------------------------------
- 🧮 **Analysis**: prove behavior using models, equations, timing budgets, or logical reasoning.
	Use when direct execution is costly, early, or unsafe.
- 🧪 **Test**: execute the software/system with defined inputs and observe outputs against pass/fail criteria.
	Use when runtime behavior must be demonstrated.
- 📋 **Inspection**: human review of requirements, design, code, or test artifacts against a checklist/standard.
	Use to catch ambiguity, omissions, and compliance gaps early.

**One requirement, three methods**

- Requirement: “Braking torque command shall be limited to 0..2000 Nm.”
- 🧮 Analysis example: verify control-law equations and scaling prove command never exceeds 2000 Nm under modeled bounds.
- 🧪 Test example: run MIL scenarios (nominal, boundary, fault) and assert output always stays within 0..2000 Nm.
- 📋 Inspection example: review requirement wording and test cases to ensure units, bounds, and pass/fail thresholds are explicit.

⚠️ Common Anti-Patterns
----------------------
- 🔴 “Shall be robust” without measurable boundaries.
- 🔴 Tests defined without linking to requirement IDs.
- 🟡 Verification deferred until implementation is complete.
- 🟡 Evidence artifacts missing raw data or reproducibility context.

✅ Knowledge Check
-----------------
- Which requirement is currently 🟡 or 🔴, and what is missing?
- Which assumption creates the highest residual risk if false?
- Can every high-criticality requirement be traced to a planned verification artifact?

🧩 Review Heuristic
------------------
If a claim cannot be tied to a concrete artifact, confidence stays 🟡 provisional until evidence exists.
