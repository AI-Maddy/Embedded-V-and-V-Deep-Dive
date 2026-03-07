Tools and Frameworks Guide
==========================

🔍 **Domain-Specific Mnemonic Acronym:** EASE (Embedded Systems Engineering)

🟢 **Severity/Priority Legend:**
🟢 **Nominal (Green):** Expected behavior, normal operation
🟡 **Boundary (Yellow):** Expected behavior, but with some constraints or limitations
🔴 **Fault (Red):** Unexpected behavior, error, or failure

Pre-Review Checklist
--------------------

☐ Review the catalog for completeness and accuracy
☐ Verify the tools and frameworks are up-to-date and relevant
☐ Ensure the catalog is organized and easy to navigate
☐ Check for consistency in formatting and style
☐ Verify the catalog includes relevant domain standards references

Tools and Frameworks Guide
==========================

### 1. Programming Languages (Embedded-Critical)

🔍 **Programming Languages (Embedded-Critical)**

| Language | Explanation | Where Used | Severity/Priority |
|---------|-------------|------------|-------------------|
| **C** | Deterministic, low-level systems programming for MCUs and safety-critical code. | Automotive ECUs, Aerospace DAL-A/B, Medical Class C; SIL/HIL | 🟢 |
| **C++ (Modern C++14/17/20)** | High-performance embedded systems with stronger abstractions; used with AUTOSAR C++14. | Automotive ADAS, Aerospace mission systems, Medical devices | 🟢 |
| **Ada** | Strongly typed language designed for safety-critical avionics. | Aerospace DAL-A/B flight control, mission computers | 🟢 |
| **SPARK Ada** | Formal-verification subset of Ada for mathematically provable correctness. | DO-178C DAL-A verification | 🔴 |
| **Python** | Automation, test scripting, data analysis, HIL orchestration. | All domains; MIL/SIL/HIL automation | 🟢 |
| **Rust** | Memory-safe systems programming gaining traction in safety-critical embedded. | Automotive safety, Medical cybersecurity | 🟡 |
| **MATLAB** | Algorithm development, modeling, simulation. | MIL/SIL across all domains | 🟢 |
| **Simulink** | Graphical modeling for control systems and plant models. | MIL/SIL/HIL across all domains | 🟢 |
| **Assembly** | Low-level deterministic control, bootloaders, interrupt routines. | Aerospace DAL-A, Medical Class C | 🟢 |

### 2. Simulation & Modeling Tools (MIL/SIL/HIL)

🔍 **Simulation & Modeling Tools (MIL/SIL/HIL)**

| Tool | Explanation | Where Used | Severity/Priority |
|------|-------------|------------|-------------------|
| **MATLAB/Simulink** | Industry standard for model-based design, control systems, and code generation. | Automotive, Aerospace, Medical (MIL/SIL/HIL) | 🟢 |
| **Stateflow** | State machine modeling for embedded logic. | All domains (MIL/SIL) | 🟢 |
| **OpenModelica** | Open-source modeling and simulation environment. | MIL for all domains | 🟢 |
| **Scilab/Xcos** | Free alternative to MATLAB/Simulink. | MIL for education and prototyping | 🟢 |
| **GT-SUITE** | Multi-physics simulation for powertrain, thermal, and controls. | Automotive MIL/HIL | 🟡 |
| **IPG CarMaker** | Vehicle dynamics and ADAS simulation. | Automotive MIL/HIL | 🟡 |
| **CARLA** | Open-source autonomous driving simulator. | Automotive ADAS MIL | 🟢 |
| **NVIDIA DRIVE Sim** | Sensor-accurate simulation for autonomous systems. | Automotive ADAS MIL/SIL | 🟡 |
| **Ansys Twin Builder** | Multi-domain simulation for aerospace and medical. | Aerospace MIL, Medical MIL | 🟡 |
| **QEMU** | CPU/board emulation for SIL. | All domains SIL | 🟡 |
| **Renode** | Embedded system emulation for IoT and MCUs. | Medical SIL, Automotive SIL | 🟡 |
| **Simics** | Full-system virtual platform for SIL. | Aerospace SIL | 🟡 |
| **ModelSim** | HDL simulation for FPGA-based systems. | Aerospace DO-254, Medical hardware | 🟡 |
| **PSpice/TINA-TI** | Analog circuit simulation. | Medical sensors, Aerospace analog front-ends | 🟡 |

### 3. Bus, Network & Protocol Tools

🔍 **Bus, Network & Protocol Tools**

| Tool | Explanation | Where Used | Severity/Priority |
|------|-------------|------------|-------------------|
| **CANoe** | Comprehensive simulation, SIL/HIL automation, CAPL scripting. | Automotive SIL/HIL | 🟡 |
| **CANalyzer** | Bus analysis, signal tracing, diagnostics. | Automotive HIL | 🟡 |
| **CANape** | Calibration and measurement tool for ECUs. | Automotive powertrain | 🟡 |
| **Astronics Ballard CoPilot** | ARINC 429/708/717/615/603 simulation, monitoring, scripting. | Aerospace HIL | 🟡 |
| **Ballard ARINC Hardware** | Rugged avionics databus interfaces. | Aerospace HIL | 🟡 |
| **Wireshark** | Packet capture for Ethernet, ARINC-UDP, medical cybersecurity. | All domains (debugging) | 🟡 |
| **Vector VN Series** | CAN/LIN/FlexRay/Ethernet hardware interfaces. | Automotive HIL | 🟡 |
| **dSPACE MicroAutoBox** | Real-time ECU prototyping. | Automotive HIL | 🟡 |
| **NI VeriStand** | Real-time test environment for HIL. | Aerospace/Medical HIL | 🟡 |
| **Speedgoat** | Real-time hardware for Simulink Real-Time. | All domains HIL | 🟡 |

### 4. Debugging, Trace & Profiling Tools

🔍 **Debugging, Trace & Profiling Tools**

| Tool | Explanation | Where Used | Severity/Priority |
|------|-------------|------------|-------------------|
| **Lauterbach TRACE32** | Industry-standard debugger for object-code testing, WCET, RTOS awareness. | Aerospace DAL-A, Automotive ASIL-D, Medical Class C | 🔴 |
| **GDB** | Open-source debugger for embedded systems. | All domains SIL | 🟡 |
| **Segger J-Link** | SWD/JTAG debugging for ARM MCUs. | Automotive/Medical HIL | 🟡 |
| **Ozone** | Segger’s performance analyzer and debugger. | Medical/Automotive | 🟡 |
| **ARM DS-5** | ARM debugging and trace tools. | Aerospace/Automotive | 🟡 |
| **Valgrind** | Memory analysis for Linux-based embedded systems. | Automotive infotainment, Medical devices | 🟡 |
| **Perf/Ftrace** | Linux kernel tracing. | Automotive IVI, Medical Linux-based systems | 🟡 |

### 5. RTOS & Embedded Operating Systems

🔍 **RTOS & Embedded Operating Systems**

| RTOS | Explanation | Where Used | Severity/Priority |
|------|-------------|------------|-------------------|
| **AUTOSAR OS** | Automotive safety-critical OS standard. | Automotive ASIL-D | 🔴 |
| **VxWorks 653** | Partitioned avionics RTOS supporting ARINC 653. | Aerospace DAL-A/B | 🔴 |
| **INTEGRITY-178B** | DO-178C certifiable RTOS. | Aerospace DAL-A | 🔴 |
| **FreeRTOS** | Lightweight RTOS for MCUs. | Medical, Automotive | 🟢 |
| **safeRTOS** | IEC 61508/62304 certifiable RTOS. | Medical Class C | 🟡 |
| **ThreadX / Azure RTOS** | Deterministic RTOS for MCUs. | Medical/Automotive | 🟡 |
| **Zephyr** | Open-source RTOS with safety certification roadmap. | IoT/Medical | 🟡 |
| **QNX Neutrino** | POSIX-compliant safety OS. | Automotive IVI, Medical | 🟡 |

### 6. Static Analysis, Coverage & Compliance Tools

🔍 **Static Analysis, Coverage & Compliance Tools**

| Tool | Explanation | Where Used | Severity/Priority |
|------|-------------|------------|-------------------|
| **LDRA Tool Suite** | DO-178C/ISO 26262 static analysis, MC/DC coverage. | Aerospace DAL-A, Automotive ASIL-D | 🔴 |
| **VectorCAST** | Automated testing and coverage for embedded C/C++. | Aerospace/Medical | 🟡 |
| **Parasoft C/C++test** | Static analysis and unit testing. | Medical IEC 62304 | 🟡 |
| **QA-MISRA** | MISRA C/C++ compliance checker. | Automotive | 🟡 |
| **CppCheck** | Open-source static analysis. | All domains | 🟡 |
| **TESSY** | Unit testing and coverage for embedded C. | Automotive/Medical | 🟡 |
| **BullseyeCoverage** | Code coverage tool. | Aerospace/Automotive | 🟡 |
| **Cantata** | Unit testing for safety-critical systems. | Medical/Aerospace | 🟡 |

### 7. Build Systems, CI/CD & DevOps

🔍 **Build Systems, CI/CD & DevOps**

| Tool | Explanation | Where Used | Severity/Priority |
|------|-------------|------------|-------------------|
| **CMake** | Cross-platform build system. | All domains | 🟢 |
| **Make** | Traditional build automation. | All domains | 🟢 |
| **Bazel** | Scalable build system for large embedded projects. | Automotive ADAS | 🟡 |
| **GitHub Actions** | CI/CD automation. | All domains | 🟡 |
| **GitLab CI** | Enterprise CI/CD. | Automotive/Aerospace | 🟡 |
| **Jenkins** | Customizable CI pipelines. | Aerospace DO-178C toolchains | 🟡 |

### 8. Hardware Platforms & MCUs

🔍 **Hardware Platforms & MCUs**

| Hardware | Explanation | Where Used | Severity/Priority |
|----------|-------------|------------|-------------------|
| **ARM Cortex-M Series** | Low-power MCUs for control loops. | Medical, Automotive | 🟢 |
| **ARM Cortex-A Series** | High-performance processors. | Automotive ADAS, Aerospace mission systems | 🟢 |
| **NXP S32K/S32G** | Automotive MCUs for safety-critical ECUs. | Automotive ASIL-D | 🔴 |
| **NVIDIA DRIVE AGX** | AI compute platform for autonomous vehicles. | Automotive ADAS | 🔴 |
| **TI C2000** | DSP-based control MCUs. | Automotive powertrain, Medical pumps | 🟡 |
| **Microchip PIC/AVR** | Low-cost MCUs. | Medical/Industrial | 🟡 |
| **UEI Avionics I/O** | ARINC/MIL-STD-1553 hardware. | Aerospace HIL | 🟡 |
| **dSPACE HIL Racks** | Real-time hardware for ECU testing. | Automotive/Aerospace | 🟡 |

### 9. Safety, Compliance & Certification Standards

🔍 **Safety, Compliance & Certification Standards**

| Standard | Explanation | Where Used | Severity/Priority |
|----------|-------------|------------|-------------------|
| **ISO 26262** | Functional safety for road vehicles. | Automotive | 🔴 |
| **DO-178C** | Software certification for airborne systems. | Aerospace | 🔴 |
| **DO-254** | Hardware certification for airborne systems. | Aerospace | 🔴 |
| **ARP4754A** | System development process for aircraft. | Aerospace | 🔴 |
| **IEC 62304** | Software lifecycle for medical devices. | Medical | 🔴 |
| **FDA 21 CFR Part 820** | Quality system regulation. | Medical | 🔴 |
| **ISO 14971** | Risk management for medical devices. | Medical | 🔴 |

### 10. Scripting & Automation Languages

🔍 **Scripting & Automation Languages**

| Language | Explanation | Where Used | Severity/Priority |
|----------|-------------|------------|-------------------|
| **CAPL** | CANoe scripting language for bus simulation. | Automotive HIL | 🟡 |
| **Python** | Automation, data analysis, HIL orchestration. | All domains | 🟢 |
| **PRACTICE (TRACE32)** | Scripting for object-code testing and trace automation. | Aerospace DAL-A | 🔴 |
| **Lua** | RTOS scripting (VxWorks). | Aerospace | 🟡 |
| **Bash** | Automation in embedded Linux. | Automotive IVI, Medical | 🟡 |

### 11. Communication Protocols

🔍 **Communication Protocols**

| Protocol | Explanation | Where Used | Severity/Priority |
|----------|-------------|------------|-------------------|
| **CAN** | Robust automotive bus. | Automotive | 🟢 |
| **LIN** | Low-speed automotive bus. | Automotive | 🟢 |
| **FlexRay** | High-speed deterministic bus. | Automotive safety | 🔴 |
| **Automotive Ethernet** | High-bandwidth ADAS networks. | Automotive ADAS | 🔴 |
| **ARINC 429** | Unidirectional avionics bus. | Aerospace | 🟢 |
| **ARINC 708** | Weather radar bus. | Aerospace | 🟢 |
| **ARINC 717** | Flight data recorder bus. | Aerospace | 🟢 |
| **ARINC 615/603** | Data loading protocols. | Aerospace | 🟢 |
| **MIL-STD-1553** | Redundant avionics bus. | Aerospace | 🟢 |
| **I2C/SPI/UART** | MCU peripheral buses. | All domains | 🟢 |

This catalog is now ready to be inserted into your repository as:

- `Tools_and_Frameworks_Guide.rst`
- `resources/tools_catalog.rst`
- Or split by domain into `/tools/automotive.rst`, `/tools/aerospace.rst`, `/tools/medical.rst`

.. note::
    This catalog is a living document and will be updated as new tools and frameworks emerge.

.. warning::
    The information provided in this catalog is for general guidance only and may not be applicable to specific use cases.

.. important::
    It is the user's responsibility to ensure that any tools or frameworks used in their projects meet the necessary safety and regulatory requirements.

.. admonition::
    This catalog is not a substitute for professional advice or guidance.

### Pre-Review Checklist

☐ Review the catalog for completeness and accuracy
☐ Verify the tools and frameworks are up-to-date and relevant
☐ Ensure the catalog is organized and easy to navigate
☐ Check for consistency in formatting and style
☐ Verify the catalog includes relevant domain standards references

### Tools and Frameworks Guide

### 1. Programming Languages (Embedded-Critical)

| Language | Explanation | Where Used | Severity/Priority |
|---------|-------------|------------|-------------------|
| **C** | Deterministic, low-level systems programming for MCUs and safety-critical code. | Automotive ECUs, Aerospace DAL-A/B, Medical Class C; SIL/HIL | 🟢 |
| **C++ (Modern C++14/17/20)** | High-performance embedded systems with stronger abstractions; used with AUTOSAR C++14. | Automotive ADAS, Aerospace mission systems, Medical devices | 🟢 |
| **Ada** | Strongly typed language designed for safety-critical avionics. | Aerospace DAL-A/B flight control, mission computers | 🟢 |
| **SPARK Ada** | Formal-verification subset of Ada for mathematically provable correctness. | DO-178C DAL-A verification | 🔴 |
| **Python** | Automation, test scripting, data analysis, HIL orchestration. | All domains; MIL/SIL/HIL automation | 🟢 |
| **Rust** | Memory-safe systems programming gaining traction in safety-critical embedded. | Automotive safety, Medical cybersecurity | 🟡 |
| **MATLAB** | Algorithm development, modeling, simulation. | MIL/SIL across all domains | 🟢 |
| **Simulink** | Graphical modeling for control systems and plant models. | MIL/SIL/HIL across all domains | 🟢 |
| **Assembly** | Low-level deterministic control, bootloaders, interrupt routines. | Aerospace DAL-A, Medical Class C | 🟢 |

### 2. Simulation & Modeling Tools (MIL/SIL/HIL)

| Tool | Explanation | Where Used | Severity/Priority |
|------|-------------|------------|-------------------|
| **MATLAB/Simulink** | Industry standard for model-based design, control systems, and code generation. | Automotive, Aerospace, Medical (MIL/SIL/HIL) | 🟢 |
| **Stateflow** | State machine modeling for embedded logic. | All domains (MIL/SIL) | 🟢 |
| **OpenModelica** | Open-source modeling and simulation environment. | MIL for all domains | 🟢 |
| **Scilab/Xcos** | Free alternative to MATLAB/Simulink. | MIL for education and prototyping | 🟢 |
| **GT-SUITE** | Multi-physics simulation for powertrain, thermal, and controls. | Automotive MIL/HIL | 🟡 |
| **IPG CarMaker** | Vehicle dynamics and ADAS simulation. | Automotive MIL/HIL | 🟡 |
| **CARLA** | Open-source autonomous driving simulator. | Automotive ADAS MIL | 🟢 |
| **NVIDIA DRIVE Sim** | Sensor-accurate simulation for autonomous systems. | Automotive ADAS MIL/SIL | 🟡 |
| **Ansys Twin Builder** | Multi-domain simulation for aerospace and medical. | Aerospace MIL, Medical MIL | 🟡 |
| **QEMU** | CPU/board emulation for SIL. | All domains SIL | 🟡 |
| **Renode** | Embedded system emulation for IoT and MCUs. | Medical SIL, Automotive SIL | 🟡 |
| **Simics** | Full-system virtual platform for SIL. | Aerospace SIL | 🟡 |
| **ModelSim** | HDL simulation for FPGA-based systems. | Aerospace DO-254, Medical hardware | 🟡 |
| **PSpice/TINA-TI** | Analog circuit simulation. | Medical sensors, Aerospace analog front-ends | 🟡 |

### 3. Bus, Network & Protocol Tools

| Tool | Explanation | Where Used | Severity/Priority |
|------|-------------|------------|-------------------|
| **CANoe** | Comprehensive simulation, SIL/HIL automation, CAPL scripting. | Automotive SIL/HIL | 🟡 |
| **CANalyzer** |
