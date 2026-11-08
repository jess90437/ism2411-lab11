"""
Reflection:
1. When working with dictionaries, I realized there is a clear distinction between using .get() and bracket notation. My rule of thumb is to use .get() whenever a key might be missing and I want the program to safely handle it with a default value instead of crashing. I only use bracket notation when the key must exist for the program to work properly, where a missing key represents a critical bug that needs to halt execution with a KeyError.

2. Writing the summary dictionary loop in Exercise 8 reminded me directly of creating an Excel Pivot Table or using SUMIF formulas to group rows and total up numbers. The Python approach feels much more powerful and useful for large datasets because it is not restricted by spreadsheet row limits, can easily process messy files automatically, and handles data aggregation cleanly through code instead of breaking formulas.
"""

# --- Exercise 1 ---
customer = {
    "name": "Alice Smith",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

print("--- Exercise 1 ---")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# --- Exercise 2 ---
customer["phone"] = "555-0198"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier:", customer)

del customer["email"]
print("After deleting email:", customer)


# --- Exercise 3 ---
# Safe lookup with .get()
email_result = customer.get("email", "no email on file")
print("Safe lookup (.get):", email_result)

# Bracket notation lookup (raising and catching KeyError)
try:
    print(customer["email"])
except KeyError:
    print("Caught KeyError: 'email' key no longer exists in dictionary.")


# --- Exercise 4 ---
for key, value in customer.items():
    print(f"{key}: {value}")

# Explanation of iterating without .items():
# If I iterate over a dictionary directly (e.g., 'for key in customer:'), 
# Python only loops through the keys, which means I would have to manually 
# look up the value using bracket notation for every single iteration.


# --- Exercise 5 ---
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}

current_tier = customer["tier"]
discount_rate = tier_discounts.get(current_tier, 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print(f"Tier: {current_tier} · Discount Rate: {discount_rate * 100}% · Final Price: ${final_price:.2f}")


# --- Exercise 6 ---
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "bronze"}
]

purchase_amount = 300
for c in customers:
    tier = c["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = purchase_amount * discount
    print(f"Name: {c['name']} · Tier: {tier} · Discount Amount: ${discount_amount:.2f}")


# --- Exercise 7 ---
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
    "Thingamajig B": {"price": 19.99, "stock": 5}
}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK ALERT: {product} has only {info['stock']} items left!")


# --- Exercise 8 ---
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
    {"region": "East", "amount": 450},
    {"region": "North", "amount": 50}
]

sales_summary = {}
for tx in transactions:
    reg = tx["region"]
    amt = tx["amount"]
    sales_summary[reg] = sales_summary.get(reg, 0) + amt

# Print final summary sorted by region name
for reg in sorted(sales_summary.keys()):
    print(f"{reg}: {sales_summary[reg]}")