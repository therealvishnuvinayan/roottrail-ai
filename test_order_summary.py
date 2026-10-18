# Your test should:
# 1. Import summarize_order() and ORDER_NS_1042.
# 2. Execute summarize_order(ORDER_NS_1042).
# 3. Define the expected summary dictionary containing all five fields.
# 4. Use assert to compare the actual result against the expected dictionary.
from order_summary import summarize_order
from order_fixtures import ORDER_NS_1042

expected_summary = {
    "order_id": "NS-1042",
    "status": "delayed",
    "item_count": 2,
    "total_units": 3,
    "latest_event": "supplier_delay",
}

def test_summarize_order_returns_expected_summary():
    actual = summarize_order(ORDER_NS_1042)
    # assert order_summary["order_id"] == "NS-1042"
    # assert order_summary["status"] == "delayed"
    # assert order_summary["item_count"] == 2
    # assert order_summary["total_units"] == 3
    # assert order_summary["latest_event"] == "supplier_delay"
    assert actual == expected_summary
