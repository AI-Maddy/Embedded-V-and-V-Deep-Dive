"""Compute coverage statistics for aerospace regression runs."""

from pathlib import Path

def summarize(lines: list[str]) -> dict[str, float]:
    values = [float(item.split("=")[-1]) for item in lines if item.startswith("coverage=")]
    if not values:
        return {"min": 0.0, "max": 0.0, "avg": 0.0}
    return {"min": min(values), "max": max(values), "avg": sum(values) / len(values)}

def load(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines() if path.exists() else []

if __name__ == "__main__":
    summary = summarize(load(Path("coverage.log")))
    print(summary)

def acceptance_criteria() -> dict[str, str]:
    return {
        "domain": "Aerospace",
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
        "domain": "Aerospace",
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

