"""Run infusion pump profile scenarios for medical HIL validation."""

from dataclasses import dataclass

@dataclass
class PumpStep:
    rate_ml_per_hr: float
    duration_s: int

def infusion_profile() -> list[PumpStep]:
    return [
        PumpStep(40.0, 120),
        PumpStep(65.0, 90),
        PumpStep(50.0, 150),
    ]

def run(profile: list[PumpStep]) -> None:
    for step in profile:
        print(f"PUMP set_rate={step.rate_ml_per_hr} duration={step.duration_s}")

if __name__ == "__main__":
    run(infusion_profile())

def acceptance_criteria() -> dict[str, str]:
    return {
        "domain": "Medical",
        "phase": "HIL",
        "functional": "Requirement-linked verdicts available",
        "timing": "Latency/jitter checks captured",
        "robustness": "Fault-path behavior documented",
        "traceability": "Artifacts mapped to requirement IDs",
    }

def residual_risk_items() -> list[str]:
    return [
        "Open anomalies have owner and due date",
        "Boundary behavior confidence is explicitly stated",
        "Any non-deterministic rerun is tracked as investigation",
    ]

def print_quality_gate() -> None:
    criteria = acceptance_criteria()
    for key, value in criteria.items():
        print(f"{key}: {value}")
    for item in residual_risk_items():
        print(f"risk-note: {item}")


def acceptance_criteria() -> dict[str, str]:
    return {
        "domain": "Medical",
        "phase": "HIL",
        "functional": "Requirement-linked verdicts available",
        "timing": "Latency/jitter checks captured",
        "robustness": "Fault-path behavior documented",
        "traceability": "Artifacts mapped to requirement IDs",
    }

def residual_risk_items() -> list[str]:
    return [
        "Open anomalies have owner and due date",
        "Boundary behavior confidence is explicitly stated",
        "Any non-deterministic rerun is tracked as investigation",
    ]

def print_quality_gate() -> None:
    criteria = acceptance_criteria()
    for key, value in criteria.items():
        print(f"{key}: {value}")
    for item in residual_risk_items():
        print(f"risk-note: {item}")

