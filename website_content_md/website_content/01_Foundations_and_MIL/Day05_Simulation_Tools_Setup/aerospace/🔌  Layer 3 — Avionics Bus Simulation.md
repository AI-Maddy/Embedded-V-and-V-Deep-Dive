# 🔌 Layer 3 --- Avionics Bus Simulation

ARINC 429 / AFDX bus simulation is essential for aerospace MIL because
the flight computer communicates exclusively over certified data buses.

**Ballard Technology ARINC 429 / MIL-STD-1553**

Hardware-in-the-loop and pure-software ARINC 429 simulation cards and
APIs.

+------------------+---------------------------------------------------+
| Feature          | Detail                                            |
+==================+===================================================+
| Bus protocols    | ARINC 429 · MIL-STD-1553 B · ARINC 717 \|         |
+------------------+---------------------------------------------------+
| Software         | BTI DLL/API (Windows) · LabVIEW driver · MATLAB   |
| interface        | MEX wrapper                                       |
+------------------+---------------------------------------------------+
| MIL usage        | Inject ARINC 429 label sequences as plant         |
|                  | outputs; monitor FCS command bus labels for FCS   |
|                  | output verification.                              |
+------------------+---------------------------------------------------+
| ⚠️ Timing note   |                                                   |
|  \| ARINC 429 wo |                                                   |
| rd rate is 12.5  |                                                   |
| kbps (low-speed) |                                                   |
|  or 100 kbps; \| |                                                   |
|                  |                                                   |
| :   | verify     |                                                   |
|       simulation |                                                   |
|       timestep   |                                                   |
|       is ≤ one   |                                                   |
|       word       |                                                   |
|       period.    |                                                   |
+------------------+---------------------------------------------------+

**AIM GmbH --- AFDX / ARINC 664 Analyzer**

Software-only AFDX network emulator widely used in commercial aircraft
MIL/SIL.

-   **Capabilities:** Virtual Link (VL) configuration, BAG enforcement,
    jitter injection, end-system frame capture.
-   **Tools:** AIM AFDX Configurator + AFDX Analyzer (Wireshark plugin
    variant).
-   **MIL integration:** Run AFDX emulator as a co-process; stimulate
    FCS model over loopback Ethernet with VL-constrained frames.
-   **⚠️ Gotcha:** BAG timer resolution is 1 ms; ensure host OS timer
    resolution is set to ≤ 1 ms (`timeBeginPeriod(1)` on Windows;
    `PREEMPT_RT` patch on Linux).

**DDC (Data Device Corporation) --- BU-65590 / BU-67118**

Industry-standard 1553 and ARINC 429 PMC/PCI cards with certified API.

-   **Relevant for:** legacy military avionics (MIL-STD-1553B)
    simulation scenarios.
-   **Python API:** `bcTestNode` example via NAIBRD SDK.

------------------------------------------------------------------------
