# GIVEN / WHEN / THEN Scenarios 📝

::: important
::: title
Important
:::

Use the following templates to structure your test cases effectively.
:::

-   **Nominal** 🟢:
    -   **GIVEN**: The vehicle is in adaptive cruise mode.
    -   **WHEN**: The traffic ahead is moving at a constant speed.
    -   **THEN**: The vehicle maintains a safe following distance
        without acceleration.
-   **Boundary** 🟡:
    -   **GIVEN**: The vehicle is in stop-and-go traffic.
    -   **WHEN**: The lead vehicle comes to a sudden stop.
    -   **THEN**: The vehicle should respond within the defined timing
        limits to avoid collision.
-   **Fault** 🔴:
    -   **GIVEN**: The vehicle\'s speed sensor is malfunctioning.
    -   **WHEN**: An invalid CAN frame is injected.
    -   **THEN**: The system should enter a safe state or alert the
        driver.
