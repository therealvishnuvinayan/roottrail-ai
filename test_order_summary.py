"""Tests for unit counting, event chronology, and input preservation."""

from copy import deepcopy

import pytest

from order_fixtures import ORDER_NS_1042, ORDER_NS_1042_REVERSED, count_units
from order_summary import summarize_order


@pytest.fixture
def order():
    return deepcopy(ORDER_NS_1042)


@pytest.mark.parametrize("example", [ORDER_NS_1042, ORDER_NS_1042_REVERSED])
def test_summarize_order_returns_expected_summary(example):
    assert summarize_order(example) == {
        "order_id": "NS-1042",
        "status": "delayed",
        "item_count": 2,
        "total_units": 3,
        "latest_event": "supplier_delay",
    }


def test_summarize_order_handles_reversed_events(order):
    order["events"].reverse()
    assert summarize_order(order)["latest_event"] == "supplier_delay"


def test_summarize_order_handles_empty_events(order):
    order["events"] = []
    summary = summarize_order(order)
    assert summary["latest_event"] is None
    assert summary["total_units"] == 3


def test_summarize_order_handles_empty_items(order):
    order["items"] = []
    summary = summarize_order(order)
    assert summary["item_count"] == 0
    assert summary["total_units"] == 0
    assert summary["latest_event"] == "supplier_delay"


@pytest.mark.parametrize(
    ("earlier", "later"),
    [
        ("2026-10-16T23:00:00+04:00", "2026-10-16T20:00:00Z"),
        ("2026-10-16T20:00:00Z", "2026-10-16T20:00:00.100Z"),
        ("2026-10-17T00:30:00+04:00", "2026-10-16T21:00:00+00:00"),
    ],
    ids=["offsets", "fractional-seconds", "date-boundary"],
)
def test_summarize_order_compares_actual_instants(order, earlier, later):
    order["events"] = [
        {"type": "later", "time": later},
        {"type": "earlier", "time": earlier},
    ]
    assert summarize_order(order)["latest_event"] == "later"


def test_equal_timestamps_keep_first_event(order):
    order["events"] = [
        {"type": "first", "time": "2026-10-16T20:00:00Z"},
        {"type": "second", "time": "2026-10-17T00:00:00+04:00"},
    ]
    assert summarize_order(order)["latest_event"] == "first"


@pytest.mark.parametrize(
    "timestamp", ["invalid", "2026-02-30T20:00:00Z", "2026-10-16T20:00:00", "2026-10-16"]
)
def test_invalid_or_timezone_free_timestamps_are_rejected(order, timestamp):
    # A single event must still have its timestamp checked.
    order["events"] = [{"type": "created", "time": timestamp}]
    with pytest.raises(ValueError):
        summarize_order(order)


def test_summarize_order_does_not_mutate_input(order):
    order["events"].reverse()
    before = deepcopy(order)
    summarize_order(order)
    assert order == before


@pytest.mark.parametrize(
    ("quantities", "expected"), [([], 0), ([0], 0), ([2, 1], 3), ([0, 4, 2], 6)]
)
def test_count_units(quantities, expected):
    order = {"items": [{"quantity": quantity} for quantity in quantities]}
    assert count_units(order) == expected
