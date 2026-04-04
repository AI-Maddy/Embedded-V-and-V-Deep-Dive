# :material-tools: Tools Reference

!!! abstract "Overview"
    This page catalogues the key tools used across MIL, SIL, and HIL phases, organized by function. Each entry notes the tool's role, typical phase, and applicable standards context.

## :material-cube-outline: MIL Tools

<div class="grid cards" markdown>

-   **MATLAB / Simulink**

    ---
    Model-based design environment. Plant and controller modeling, MIL simulation, closed-loop analysis.

    *Phase: MIL | Standard: ISO 26262 Pt6, DO-178C*

-   **Simulink Test**

    ---
    Test case management and execution within Simulink. Links test cases to requirements via Requirements Toolbox.

    *Phase: MIL | Standard: ISO 26262 Pt6 Sec9*

-   **Simulink Coverage**

    ---
    Model coverage measurement (condition, decision, MC/DC at model level). Reports coverage gaps in Stateflow charts.

    *Phase: MIL | Standard: DO-178C Sec6.4*

-   **Simulink Requirements**

    ---
    Bidirectional traceability between requirements documents and Simulink model elements.

    *Phase: MIL | Standard: ISO 26262 Pt6 Sec7*

</div>

## :material-code-braces: SIL Tools

<div class="grid cards" markdown>

-   **Embedded Coder**

    ---
    Production C code generator from Simulink/Stateflow. Generates MISRA-compliant, traceable code with ERT target.

    *Phase: SIL | Standard: DO-178C Sec12.2 (TQ3)*

-   **Polyspace Code Prover**

    ---
    Abstract interpretation-based static analyzer. Proves absence of runtime errors (green/orange/red). Checks MISRA C:2012.

    *Phase: SIL | Standard: ISO 26262 Pt6 Sec9, DO-178C Sec6.3*

-   **VectorCAST**

    ---
    Unit and integration test framework with coverage measurement (statement, branch, MC/DC). Automates test harness generation.

    *Phase: SIL | Standard: DO-178C Sec6.4, IEC 62304 Sec5.5*

-   **LDRA TBvision**

    ---
    Static and dynamic analysis platform. Code complexity, MISRA checking, structural coverage. Supports DO-178C and ISO 26262 workflows.

    *Phase: SIL | Standard: DO-178C, ISO 26262*

-   **PC-lint / FlexeLint**

    ---
    MISRA C static analysis tool. Fast, command-line driven. Integrates with CI pipelines.

    *Phase: SIL | Standard: MISRA C:2012*

-   **AbsInt aiT**

    ---
    Static WCET analysis tool using abstract interpretation. Provides provable WCET upper bounds for ARM and PowerPC.

    *Phase: SIL/HIL | Standard: DO-178C Sec6.4.4 (DAL A)*

</div>

## :material-cpu-64-bit: HIL Tools

<div class="grid cards" markdown>

-   **dSPACE SCALEXIO**

    ---
    Real-time HIL simulator platform. Supports automotive, aerospace, and industrial ECU testing. FPGA-based I/O with < 1 μs latency.

    *Phase: HIL | Domain: Automotive, Aerospace*

-   **NI VeriStand**

    ---
    National Instruments HIL platform. Supports FPGA real-time I/O, customizable models, Python scripting.

    *Phase: HIL | Domain: All*

-   **Vector CANoe / CANalyzer**

    ---
    CAN/LIN/Ethernet bus analysis and simulation. CAPL scripting for bus stimulation and ECU response testing. DBC/ARXML import.

    *Phase: HIL | Standard: ISO 11898, AUTOSAR*

-   **Lauterbach TRACE32**

    ---
    JTAG debugger and execution trace tool. ARM ETM trace for WCET measurement, code coverage on target, hardware breakpoints.

    *Phase: HIL | Standard: DO-178C DAL A OCV*

-   **dSPACE FIU**

    ---
    Fault Insertion Unit for hardware-level fault injection. Short circuit, open circuit, and resistive fault injection on any ECU pin.

    *Phase: HIL | Standard: ISO 26262 Pt9*

-   **CANdb++ / Vector DBC Editor**

    ---
    CAN communication matrix editor. Defines message IDs, DLCs, signal encoding (factor, offset, range). Source of truth for bus analysis.

    *Phase: HIL | Domain: Automotive*

</div>

## :material-file-document: Documentation & Management Tools

<div class="grid cards" markdown>

-   **IBM DOORS / DOORS Next**

    ---
    Requirements management tool. Stores SwRS, traces requirements to test cases, generates RTM exports. Used in aerospace and automotive.

    *Phase: All | Standard: DO-178C Sec11.9, ISO 26262 Pt6*

-   **PTC Integrity / Windchill**

    ---
    ALM (Application Lifecycle Management) platform. Requirements, defects, test management in one tool.

    *Phase: All | Domain: Industrial, Aerospace*

-   **JIRA + Confluence**

    ---
    Agile project management with test tracking. Used in automotive and medical for defect management and review records.

    *Phase: All | Domain: Automotive, Medical*

-   **Git / GitLab / GitHub**

    ---
    Version control for models, code, test scripts, and documentation. Essential for configuration management per all standards.

    *Phase: All | Standard: ISO 26262 Pt8, DO-178C Sec7*

</div>

## :material-table: Tool Quick Reference

| Tool | Phase | Function | Standard |
|------|-------|----------|----------|
| Simulink Test | MIL | Test case management | ISO 26262 Pt6 |
| Embedded Coder | SIL | Code generation | DO-178C Sec12 |
| Polyspace | SIL | Static analysis (runtime errors) | ISO 26262 Pt6 Sec9 |
| VectorCAST | SIL | Unit test + coverage | DO-178C Sec6.4 |
| LDRA | SIL/HIL | MISRA + coverage | DO-178C, ISO 26262 |
| AbsInt aiT | SIL/HIL | Static WCET | DO-178C DAL A |
| dSPACE SCALEXIO | HIL | Real-time simulation | ISO 26262 Pt4 |
| CANoe | HIL | Bus analysis + scripting | ISO 11898 |
| TRACE32 | HIL | Execution trace + WCET | DO-178C DAL A |
| DOORS | All | Requirements management | All |
| Git | All | Version control | All |
