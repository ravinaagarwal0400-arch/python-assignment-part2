# =========================================
# ASSIGNMENT PART 2 - DATA STRUCTURES
# Theme: Restaurant Menu & Order Management
# =========================================

import copy


# -----------------------------------------
# PROVIDED DATA
# -----------------------------------------

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price": 40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price": 90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price": 80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock": 8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock": 6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock": 5, "reorder_level": 2},
    "Rasgulla":       {"stock": 4, "reorder_level": 3},
    "Ice Cream":      {"stock": 7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1, "items": ["Paneer Tikka", "Garlic Naan"], "total": 220.0},
        {"order_id": 2, "items": ["Gulab Jamun", "Veg Soup"], "total": 210.0},
        {"order_id": 3, "items": ["Butter Chicken", "Garlic Naan"], "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4, "items": ["Dal Tadka", "Garlic Naan"], "total": 220.0},
        {"order_id": 5, "items": ["Veg Biryani", "Gulab Jamun"], "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
        {"order_id": 7, "items": ["Butter Chicken", "Veg Biryani"], "total": 570.0},
        {"order_id": 8, "items": ["Garlic Naan", "Gulab Jamun"], "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9, "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"], "total": 270.0},
    ],
}


# -----------------------------------------
# TASK 1 - Explore Menu
# -----------------------------------------

print("\nTASK 1 OUTPUT\n")

categories = ["Starters", "Mains", "Desserts"]

for category in categories:
    print(f"===== {category} =====")
    for item, details in menu.items():
        if details["category"] == category:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{item:<18} ₹{details['price']:.2f}   [{status}]")
    print()

total_items = len(menu)
available_items = sum(1 for item in menu.values() if item["available"])

most_expensive = max(menu.items(), key=lambda x: x[1]["price"])

print("Total items:", total_items)
print("Available items:", available_items)
print(f"Most expensive: {most_expensive[0]} - ₹{most_expensive[1]['price']}")

print("\nItems below ₹150:")
for item, details in menu.items():
    if details["price"] < 150:
        print(f"{item} - ₹{details['price']}")


# -----------------------------------------
# TASK 2 - Cart Operations
# -----------------------------------------

print("\n\nTASK 2 OUTPUT\n")

cart = []


def add_to_cart(item_name, quantity):
    if item_name not in menu:
        print(f"{item_name} does not exist in menu")
        return

    if not menu[item_name]["available"]:
        print(f"{item_name} is currently unavailable")
        return

    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return

    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })
    print(f"Added {item_name} x{quantity}")


def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"Removed {item_name}")
            return
    print(f"{item_name} not found in cart")


def print_cart():
    print("\nCurrent Cart:")
    for item in cart:
        print(item)


# simulation
add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)
print_cart()

add_to_cart("Mystery Burger", 1)
add_to_cart("Chicken Wings", 1)

remove_from_cart("Gulab Jamun")
print_cart()


# order summary
print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    item_total = item["quantity"] * item["price"]
    subtotal += item_total
    print(f"{item['item']:<18} x{item['quantity']}   ₹{item_total:.2f}")

gst = subtotal * 0.05
total_payable = subtotal + gst

print("-" * 36)
print(f"Subtotal:           ₹{subtotal:.2f}")
print(f"GST (5%):           ₹{gst:.2f}")
print(f"Total Payable:      ₹{total_payable:.2f}")
print("=" * 36)


# -----------------------------------------
# TASK 3 - Inventory Tracker
# -----------------------------------------

print("\n\nTASK 3 OUTPUT\n")

inventory_backup = copy.deepcopy(inventory)

# proving deep copy
inventory["Paneer Tikka"]["stock"] = 5

print("Modified Inventory:", inventory["Paneer Tikka"])
print("Backup Inventory:", inventory_backup["Paneer Tikka"])

# restore original
inventory = copy.deepcopy(inventory_backup)

# order fulfilment
for item in cart:
    name = item["item"]
    qty = item["quantity"]

    available_stock = inventory[name]["stock"]

    if qty > available_stock:
        print(f"Warning: Only {available_stock} available for {name}")
        inventory[name]["stock"] = 0
    else:
        inventory[name]["stock"] -= qty

# reorder alerts
print("\nReorder Alerts:")
for item, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(
            f"⚠ Reorder Alert: {item} — Only {details['stock']} unit(s) left "
            f"(reorder level: {details['reorder_level']})"
        )

print("\nCurrent Inventory:", inventory["Paneer Tikka"])
print("Backup Inventory:", inventory_backup["Paneer Tikka"])


# -----------------------------------------
# TASK 4 - Sales Log Analysis
# -----------------------------------------

print("\n\nTASK 4 OUTPUT\n")

daily_revenue = {}

for date, orders in sales_log.items():
    revenue = sum(order["total"] for order in orders)
    daily_revenue[date] = revenue
    print(f"{date} : ₹{revenue}")

best_day = max(daily_revenue, key=daily_revenue.get)
print("\nBest selling day:", best_day)

# most ordered item
item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

most_ordered = max(item_count, key=item_count.get)
print("Most ordered item:", most_ordered)

# add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nUpdated Revenue Table:")
updated_revenue = {}

for date, orders in sales_log.items():
    revenue = sum(order["total"] for order in orders)
    updated_revenue[date] = revenue
    print(f"{date} : ₹{revenue}")

best_day_updated = max(updated_revenue, key=updated_revenue.get)
print("\nUpdated Best Selling Day:", best_day_updated)

# enumerate all orders
print("\nAll Orders:")
all_orders = []

for date, orders in sales_log.items():
    for order in orders:
        all_orders.append((date, order))

for index, (date, order) in enumerate(all_orders, start=1):
    items_text = ", ".join(order["items"])
    print(
        f"{index}. [{date}] Order #{order['order_id']} — "
        f"₹{order['total']} — Items: {items_text}"
    )