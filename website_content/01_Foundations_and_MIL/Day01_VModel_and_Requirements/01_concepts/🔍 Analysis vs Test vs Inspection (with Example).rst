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

