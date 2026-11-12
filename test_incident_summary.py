"""Tests for incident aggregation and input preservation."""

from copy import deepcopy

import pytest

from incident_summary import incidents, summarize_incidents


@pytest.mark.parametrize(
    ("records", "expected"),
    [
        ([], {"total": 0, "resolved": 0, "unresolved": 0, "high_unresolved_ids": []}),
        (
            incidents,
            {"total": 5, "resolved": 2, "unresolved": 3,
             "high_unresolved_ids": ["INC-001", "INC-005"]},
        ),
        (
            [{**incident, "resolved": True} for incident in incidents],
            {"total": 5, "resolved": 5, "unresolved": 0, "high_unresolved_ids": []},
        ),
        (
            [{**incident, "severity": "high", "resolved": False}
             for incident in incidents],
            {"total": 5, "resolved": 0, "unresolved": 5,
             "high_unresolved_ids": [incident["id"] for incident in incidents]},
        ),
        (
            [{"id": "INC-006", "severity": "low", "resolved": False}],
            {"total": 1, "resolved": 0, "unresolved": 1, "high_unresolved_ids": []},
        ),
    ],
    ids=["empty", "mixed", "all-resolved", "all-high-unresolved", "low-unresolved"],
)
def test_summarize_incidents(records, expected):
    assert summarize_incidents(records) == expected


def test_high_unresolved_ids_preserve_input_order():
    records = [
        {"id": "INC-009", "severity": "high", "resolved": False},
        {"id": "INC-002", "severity": "high", "resolved": True},
        {"id": "INC-001", "severity": "high", "resolved": False},
    ]
    assert summarize_incidents(records)["high_unresolved_ids"] == ["INC-009", "INC-001"]


def test_summarize_incidents_does_not_mutate_input():
    records = deepcopy(incidents)
    before = deepcopy(records)
    summary = summarize_incidents(records)
    summary["high_unresolved_ids"].append("INC-NEW")
    assert records == before
