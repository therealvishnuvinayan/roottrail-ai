ORDER_NS_1042 = {
    "order_id": "NS-1042",
    "status": "delayed",
    "items": [
        {"sku": "LAPTOP-01", "quantity": 2}, 
        {"sku": "MOUSE-01", "quantity": 1},
    ],
    "events": [
        {"name": "EV-001", "type": "order_created", "time": "2026-10-16T21:24:45Z"},
        {"name": "EV-002", "type": "supplier_delay", "time": "2026-10-16T21:26:45Z"},
    ],
}

ORDER_NS_1042_REVERSED = {
    "order_id": "NS-1042",
    "status": "delayed",
    "items": [
        {"sku": "LAPTOP-01", "quantity": 2}, 
        {"sku": "MOUSE-01", "quantity": 1},
    ],
    "events": [
        {"name": "EV-002", "type": "supplier_delay", "time": "2026-10-16T21:26:45Z"},
        {"name": "EV-001", "type": "order_created", "time": "2026-10-16T21:24:45Z"},
    ],
}


def count_units(order):
    total_quantity_count = 0
    for item in order["items"]:
        total_quantity_count += item["quantity"]

    return total_quantity_count

if __name__ == "__main__": 
    print(count_units(ORDER_NS_1042))