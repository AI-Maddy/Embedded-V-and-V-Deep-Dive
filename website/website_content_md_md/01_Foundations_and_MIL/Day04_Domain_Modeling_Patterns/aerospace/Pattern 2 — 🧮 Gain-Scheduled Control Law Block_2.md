# Pattern 2 --- 🧮 Gain-Scheduled Control Law Block

**What It Models**

Continuous variation of controller gains (pitch / roll / yaw channels)
as a function of flight envelope parameters: Mach number, dynamic
pressure (Q), altitude band, flap configuration, and CG range.

**Key Implementation Rules**

  ------- ---------------------------------------------------------------
  📐      Store gain tables as **parameter objects**
          (`Simulink.Parameter` or SCADE `const` blocks) --- never as
          magic numbers in subsystem masks.

  🗃️      Version-control the gain dataset separately from the algorithm
          model; require a configuration item (CI) entry for every gain
          table change.

  🌡️      Include an **atmosphere model** (COESA or ISA) to derive
          dynamic pressure from altitude + TAS inputs --- do not use raw
          sensor values without validation.

  🔒      Clamp all gain outputs to physical limits before they reach
          actuator commands; clamping logic must be separately verified,
          not absorbed into the gain table.

  📏      Define gain scheduling break-points at flight-envelope boundary
          conditions to ensure test vectors hit every table segment.
  ------- ---------------------------------------------------------------

**🟡 Boundary Condition Pattern**

``` text
Gain table break-points must be tested at:
  ├── Exactly at break-point value          (interpolation edge)
  ├── 1 LSB below break-point               (lower segment)
  ├── 1 LSB above break-point               (upper segment)
  └── Minimum and maximum table extent      (clamping)
```

------------------------------------------------------------------------
