"""Summarize a small set of synthetic incidents."""

incidents = [
    {"id": "INC-001", "severity": "high", "resolved": False},
    {"id": "INC-002", "severity": "low", "resolved": True},
    {"id": "INC-003", "severity": "medium", "resolved": False},
    {"id": "INC-004", "severity": "high", "resolved": True},
    {"id": "INC-005", "severity": "high", "resolved": False},
]


def summarize_incidents(incidents: list[dict]) -> dict:
    """Count incidents and retain unresolved high-severity IDs in input order.

    Records must have an id, a severity string, and a boolean resolved value.
    The input records are not modified.
    """
    total = len(incidents)
    resolved = 0
    unresolved = 0
    high_unresolved_ids = []
    for incident in incidents:
        if incident["resolved"]:
            resolved += 1
        else:
            unresolved += 1
        if not incident["resolved"] and incident["severity"] == "high":
            high_unresolved_ids.append(incident["id"])

    return {
        "total": total,
        "resolved": resolved,
        "unresolved": unresolved,
        "high_unresolved_ids": high_unresolved_ids,
    }


if __name__ == "__main__":
    print(summarize_incidents(incidents))
