from incident_summary import summarize_incidents

#original check
incidents = [
    {"id": "INC-001", "severity": "high", "resolved": False},
    {"id": "INC-002", "severity": "low", "resolved": True},
    {"id": "INC-003", "severity": "medium", "resolved": False},
    {"id": "INC-004", "severity": "high", "resolved": True},
    {"id": "INC-005", "severity": "high", "resolved": False},
]

# An empty list returns zero totals and an empty ID list

incidents_test_empty = []

# A list containing only resolved incidents returns zero unresolved incidents.

incidents_test_all_resolved = [
    {"id": "INC-001", "severity": "high", "resolved": True},
    {"id": "INC-002", "severity": "low", "resolved": True},
    {"id": "INC-003", "severity": "medium", "resolved": True},
    {"id": "INC-004", "severity": "high", "resolved": True},
    {"id": "INC-005", "severity": "high", "resolved": True},
]

# A list containing high-severity incidents includes only unresolved high-severity IDs,
# in their original order.

incidents_test_high_severity_unresolved = [
    {"id": "INC-001", "severity": "high", "resolved": False},
    {"id": "INC-002", "severity": "high", "resolved": False},
    {"id": "INC-003", "severity": "high", "resolved": False},
    {"id": "INC-004", "severity": "high", "resolved": False},
    {"id": "INC-005", "severity": "high", "resolved": False},
]

incidents_test_empty_result = summarize_incidents(incidents_test_empty)


assert incidents_test_empty_result["total"] == 0
assert incidents_test_empty_result["resolved"] == 0
assert incidents_test_empty_result["unresolved"] == 0
assert incidents_test_empty_result["high_unresolved_ids"] == []

incidents_test_all_resolved_result = summarize_incidents(incidents_test_all_resolved)

assert incidents_test_all_resolved_result["total"] == 5
assert incidents_test_all_resolved_result["resolved"] == 5
assert incidents_test_all_resolved_result["unresolved"] == 0
assert incidents_test_all_resolved_result["high_unresolved_ids"] == []

incidents_test_high_severity_unresolved_result = summarize_incidents(incidents_test_high_severity_unresolved)

assert incidents_test_high_severity_unresolved_result["total"] == 5
assert incidents_test_high_severity_unresolved_result["resolved"] == 0
assert incidents_test_high_severity_unresolved_result["unresolved"] == 5
assert incidents_test_high_severity_unresolved_result["high_unresolved_ids"] == [
    "INC-001",
    "INC-002",
    "INC-003",
    "INC-004",
    "INC-005",
]

original_values_result = summarize_incidents(incidents)

assert original_values_result["resolved"] == 2
assert original_values_result["unresolved"] == 3
assert original_values_result["high_unresolved_ids"] == ["INC-001", "INC-005"]