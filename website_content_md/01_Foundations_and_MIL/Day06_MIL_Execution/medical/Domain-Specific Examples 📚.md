# Domain-Specific Examples 📚

🟢 **Nominal Scenario**:

:   GIVEN therapy control with validated sensor feedback WHEN the system
    operates under normal conditions THEN therapy delivery aligns with
    prescribed parameters

🟡 **Boundary Scenario**:

:   GIVEN near-threshold dosing and alarm escalation timing WHEN sensor
    feedback approaches critical thresholds THEN the system escalates
    alarms within compliance timing

🔴 **Fault Scenario**:

:   GIVEN sensor spike/dropout or actuator command rejection WHEN the
    system encounters unexpected input or failure THEN therapy halts
    safely, and alarms notify the operator
