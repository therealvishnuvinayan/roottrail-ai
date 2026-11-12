"""Summarize synthetic orders without changing their records."""

from datetime import datetime

from order_fixtures import ORDER_NS_1042, ORDER_NS_1042_REVERSED, count_units


def _event_time(event: dict) -> datetime:
    """Parse an ISO 8601 timestamp with an explicit UTC offset or Z suffix."""
    timestamp = datetime.fromisoformat(event["time"])
    if timestamp.utcoffset() is None:
        raise ValueError("Event timestamps must include a UTC offset or Z suffix")
    return timestamp


def summarize_order(order: dict) -> dict:
    """Return counts and the latest event type, or None when events is empty.

    Timestamps are compared as instants, including offsets and fractional seconds.
    Invalid or timezone-free timestamps raise ValueError. Equal timestamps keep
    the first event in input order. Required record fields must be present.
    """
    order_id = order["order_id"]
    status = order["status"]
    item_count = len(order["items"])
    total_units = count_units(order)
    latest_event = max(order["events"], key=_event_time, default=None)

    return {
        "order_id": order_id,
        "status": status,
        "item_count": item_count,
        "total_units": total_units,
        "latest_event": latest_event["type"] if latest_event is not None else None,
    }


if __name__ == "__main__":
    order_summary = summarize_order(ORDER_NS_1042)
    order_summary_reversed = summarize_order(ORDER_NS_1042_REVERSED)
    print(order_summary)
    print(order_summary_reversed)
