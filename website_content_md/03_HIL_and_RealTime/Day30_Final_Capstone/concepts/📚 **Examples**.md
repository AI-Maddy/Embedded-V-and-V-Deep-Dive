# 📚 **Examples**

\### Nominal Behavior Walkthrough with Expected Signal Evolution

-   Nominal behavior is the expected behavior of the system under normal
    operating conditions.
-   A walkthrough of the nominal behavior should include the expected
    signal evolution.

\### Boundary Condition Where One Constraint is Intentionally Stressed

-   Boundary conditions are the limits within which the system operates.
-   A boundary condition where one constraint is intentionally stressed
    can help identify potential issues.

\### Failure Case Showing Detection Path and Safe Response

-   Failure cases are the ways in which the system can fail.
-   A failure case should show the detection path and safe response.

✅ **Best Practices** \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\### Keep Concept Notes Short, Testable, and Requirement-Linked

-   Concept notes should be short and to the point.
-   They should be testable and linked to requirements.

\### Record Confidence Level and Known Limitations

-   Confidence level and known limitations should be properly recorded.
-   This information is essential for understanding the verification
    process.

\### Use Consistent Naming for Artifacts and Verdicts

-   Consistent naming is essential for ensuring that artifacts and
    verdicts are properly understood.
-   A consistent naming convention should be used throughout the
    verification process.

🧪 **Heuristics** \-\-\-\-\-\-\-\-\-\-\-\-\--

\### If It Cannot Be Measured, It Is Not Yet Review-Ready

-   If something cannot be measured, it is not yet review-ready.
-   Measurability is essential for verification.

\### If Two Reviewers Interpret Differently, Refine Wording

-   If two reviewers interpret differently, refine wording.
-   Clear and concise language is essential for ensuring that the
    verification process is properly understood.

\### If a Failure Is Possible, Define Detection Evidence

-   If a failure is possible, define detection evidence.
-   Detection evidence is essential for ensuring that failures are
    properly detected and addressed.

🔎 **GIVEN / WHEN / THEN Scenario Templates**
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\### Nominal 🟢

-   GIVEN: The system is operating under normal conditions.
-   WHEN: The system receives a valid input.
-   THEN: The system produces the expected output.

\### Boundary 🟡

-   GIVEN: The system is operating at the boundary of its operating
    range.
-   WHEN: The system receives an input that stresses one of its
    constraints.
-   THEN: The system produces an output that is within its acceptable
    limits.

\### Fault 🔴

-   GIVEN: The system has failed in a specific way.
-   WHEN: The system receives an input that triggers the failure.
-   THEN: The system produces an output that indicates the failure.

🔎 **Pre-Review Checklist**
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

☐ Concept definitions are precise and testable. ☐ Assumptions and limits
are documented. ☐ Verification signals and metrics are identified. ☐
Evidence references are present and reproducible. ☐ The system\'s
behavior is properly understood. ☐ The system\'s operating boundaries
are properly understood. ☐ The system\'s failure modes are properly
understood. ☐ The system\'s observable indicators are properly
understood.
