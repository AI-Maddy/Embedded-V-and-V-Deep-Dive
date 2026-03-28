# Heuristics 🧠

-   **AIM**:
    -   **A**ssess domain hazard coverage explicitly.
    -   **I**dentify determinism issues during reruns.
    -   **M**itigate indirect evidence by reducing verdict confidence.
-   If a domain hazard is untested, confidence is **provisional**.
-   If rerun results differ unexpectedly, investigate **determinism**
    first.
-   If evidence is indirect, reduce **verdict confidence level**.
