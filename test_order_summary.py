# Your test should:
# 1. Import summarize_order() and ORDER_NS_1042.
# 2. Execute summarize_order(ORDER_NS_1042).
# 3. Define the expected summary dictionary containing all five fields.
# 4. Use assert to compare the actual result against the expected dictionary.
from order_summary import summarize_order
from order_fixtures import ORDER_NS_1042, ORDER_NS_1042_REVERSED
import copy


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


# Requirements:
# 1. Start with ORDER_NS_1042.
# 2. Use deepcopy() to protect the original fixture.
# 3. Reverse the copied order's events list.
# 4. Call summarize_order() with the reversed order.
# 5. Assert that latest_event is still "supplier_delay".

def test_summarize_order_handles_reversed_events():
     copied_order = copy.deepcopy(ORDER_NS_1042)
     copied_order["events"].reverse()
     copied_order_summarised = summarize_order(copied_order)
     assert copied_order_summarised["latest_event"] == expected_summary["latest_event"]


