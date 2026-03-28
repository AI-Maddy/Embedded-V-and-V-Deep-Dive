🏆 Best Practices
-----------------

.. list-table::
   :widths: 10 90
   :header-rows: 0

   * - 🏷️
     - Tag every subsystem with the Pattern ID (e.g. ``PAT-04-MODE``, ``PAT-04-MONITOR``).
   * - 📐
     - Enforce MAAB / DO-331 modelling guidelines via ``modeladvisor`` check on every commit.
   * - 🔒
     - Protect all parameter files with CI hash; reject runs with hash mismatch.
   * - 🗂️
     - Maintain a **Model Architecture Document (MAD)** that maps each subsystem to its
       ARP4754A allocation and DO-178C software component.
   * - 🧬
     - Run Simulink Design Verifier (SDV) for reachability and dead-logic checks as a
       supplement to manual review — flag all unreachable states for justification.
   * - 📊
     - Capture model-level coverage (Simulink Coverage) alongside source-code coverage;
       gaps at model level predict gaps at code level.

----

