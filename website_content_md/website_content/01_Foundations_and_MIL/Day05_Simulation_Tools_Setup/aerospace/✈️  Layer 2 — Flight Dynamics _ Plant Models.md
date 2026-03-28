# ✈️ Layer 2 --- Flight Dynamics / Plant Models

Aerospace MIL requires a high-fidelity aerodynamic environment to close
the loop around the Flight Control System (FCS) model.

**JSBSim**

Open-source, multi-platform flight dynamics model (FDM) used in UAV and
GA aircraft certification simulation environments.

-   **Interface:** C++ API, Python bindings (`jsbsim` PyPI package),
    Simulink S-Function wrapper.
-   **Aircraft configs:** XML-based aerodynamic coefficient tables (CLα,
    CDβ, CMq ...).
-   **MIL integration:** wrap as a Simulink S-Function or call via
    co-simulation bus.
-   **⚠️ TQL note:** JSBSim itself is TQL-5; validate accuracy against
    flight-test data before claiming it supports a qualification
    argument.

**FlightGear Flight Dynamics Model (FDM)**

Open-source simulator with JSBSim or YASim FDMs. Useful for
pilot-in-the-loop (PIL) closed-loop scenarios and visualisation during
MIL runs.

-   **Interface:** FlightGear Generic Protocol (UDP), FGNetFDM struct,
    or JSBSim direct.
-   **MIL integration:** pipe FCS model outputs to FG over loopback UDP;
    log state vector.
-   **⚠️ Gotcha:** FlightGear rendering adds non-deterministic latency
    --- disable it (`--fdm=null --fog-fastest`) for headless regression
    runs.

**Simulink Aerospace Blockset**

MathWorks-native 6-DOF equations of motion, atmosphere models (ISA,
US76), and actuator / sensor models tightly integrated in a Simulink
diagram.

-   **Key blocks:** `6DOF (Euler Angles)` · `COESA Atmosphere Model` ·
    `Dryden Wind Turbulence` · `Discrete Wind Gust Model`
-   **⚠️ Pitfall:** Default Dryden turbulence uses a random seed ---
    always fix the seed in the model workspace for deterministic
    regression.

------------------------------------------------------------------------
