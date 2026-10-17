"""
 Syntax Revision
"""

# 1. Variables and data types
store_name = "Campus Store"
target_sales = 1000.0
is_open = True
daily_sales = [250, 180, 320, 150]

# 2. Dictionary: one product record
product = {
    "name": "Notebook",
    "category": "Stationery",
    "price": 60,
    "units_sold": 12
}

# 3. Conditions
total_sales = sum(daily_sales)

if total_sales >= target_sales:
    performance = "Target achieved"
else:
    performance = "Target not achieved"

# 4. Loop through product records
products = [
    {"name": "Notebook", "price": 60, "units_sold": 12},
    {"name": "Pen", "price": 15, "units_sold": 30},
    {"name": "Folder", "price": 40, "units_sold": 8}
]

print(f"Store: {store_name}")
print(f"Store open: {is_open}")
print(f"Daily sales: {daily_sales}")
print(f"Total sales: {total_sales}")
print(f"Performance: {performance}")

print("\nProduct revenue:")

grand_total = 0

for item in products:
    revenue = item["price"] * item["units_sold"]
    grand_total += revenue

    print(f'{item["name"]}: Rs. {revenue}')

print(f"Total product revenue: Rs. {grand_total}")

# 5. List comprehension
high_sales_days = [
    amount for amount in daily_sales if amount >= 200
]

print(f"Days with sales >= 200: {high_sales_days}")
