"""
WEEK 3 — Functions for Data Processing
"""

# 1. Function with parameters and return value
def calculate_revenue(price, units_sold):
    """Calculate revenue for one product."""
    return price * units_sold


# 2. Function with a default parameter
def apply_discount(price, discount_percent=0):
    """Calculate price after discount."""
    discount = price * discount_percent / 100
    return price - discount


# 3. Validate a sales record
def is_valid_sale(record):
    """Check whether price and units sold are valid numbers."""

    return (
        isinstance(record.get("price"), (int, float))
        and not isinstance(record.get("price"), bool)
        and isinstance(record.get("units_sold"), (int, float))
        and not isinstance(record.get("units_sold"), bool)
        and record["price"] >= 0
        and record["units_sold"] >= 0
    )


# 4. Process multiple sales records
def process_sales(records):
    """Return valid records with a calculated revenue field."""

    processed = []

    for record in records:
        if is_valid_sale(record):
            new_record = record.copy()

            new_record["revenue"] = calculate_revenue(
                new_record["price"],
                new_record["units_sold"]
            )

            processed.append(new_record)

        else:
            print(f"Skipping invalid record: {record}")

    return processed


# 5. Main program
if __name__ == "__main__":

    sales = [
        {"product": "Notebook", "price": 60, "units_sold": 12},
        {"product": "Pen", "price": 15, "units_sold": 30},
        {"product": "Folder", "price": -5, "units_sold": 8}
    ]

    print("Notebook revenue:",
          calculate_revenue(60, 12))

    print("Price after 10% discount:",
          apply_discount(100, 10))

    print("Price without discount:",
          apply_discount(100))

    results = process_sales(sales)

    print("\nProcessed sales:")

    for row in results:
        print(row)

    total_revenue = sum(
        row["revenue"] for row in results
    )

    print("Total valid revenue:", total_revenue)


# PRACTICE:
# A. Create a function to calculate average revenue.
# B. Apply a 5% discount to the Notebook price.
# C. Add another valid product to the sales list.