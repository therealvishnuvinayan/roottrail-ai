from order_fixtures import ORDER_NS_1042, ORDER_NS_1042_REVERSED, count_units

def summarize_order(order):
    order_id = order["order_id"]
    status = order["status"]
    item_count = len(order["items"])
    total_units = count_units(order)
    latest_event = max(order["events"], key=lambda event: event["time"])["type"]

    return {
        "order_id": order_id,
        "status": status,
        "item_count": item_count,
        "total_units": total_units,
        "latest_event": latest_event,
    }


if __name__ == "__main__":
    order_summary = summarize_order(ORDER_NS_1042)
    order_summary_reversed = summarize_order(ORDER_NS_1042_REVERSED)
    print(order_summary)
    print(order_summary_reversed)
