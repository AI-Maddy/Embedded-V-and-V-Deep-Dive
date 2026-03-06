"""Execute medical HIL fault cases focused on alarm and safe-state behavior."""

from dataclasses import dataclass

@dataclass
class FaultCase:
    name: str
    trigger_s: int
    expected_alarm: str

def medical_faults() -> list[FaultCase]:
    return [
        FaultCase("sensor_dropout", 35, "SENSOR_FAIL"),
        FaultCase("occlusion_alarm_delay", 70, "OCCLUSION"),
        FaultCase("invalid_dose_command", 95, "COMMAND_REJECT"),
    ]

def run() -> None:
    for fault in medical_faults():
        print(f"INJECT {fault.name} at={fault.trigger_s}s expect={fault.expected_alarm}")

if __name__ == "__main__":
    run()

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

