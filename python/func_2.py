"""
WEEK 3 — Data Cleaning and Summaries with Functions
"""


# 1. Clean text
def clean_product_name(name):
    """Remove extra spaces and standardise capitalisation."""

    if not isinstance(name, str):
        return ""

    return " ".join(name.strip().split()).title()


# 2. Convert values to numbers safely
def to_number(value):
    """Convert a value to float, or return None if invalid."""

    try:
        return float(value)

    except (TypeError, ValueError):
        return None


# 3. Clean one record
def clean_record(record):
    """Clean and validate one product record."""

    name = clean_product_name(record.get("product"))
    price = to_number(record.get("price"))
    units = to_number(record.get("units_sold"))

    # Reject missing or invalid values
    if not name or price is None or units is None:
        return None

    # Reject negative values
    if price < 0 or units < 0:
        return None

    # Reject fractional units sold
    if not units.is_integer():
        return None

    units = int(units)

    return {
        "product": name,
        "price": price,
        "units_sold": units,
        "revenue": price * units
    }


# 4. Clean an entire dataset
def clean_dataset(raw_records):
    """Return cleaned records and the number of rejected records."""

    cleaned = []
    rejected_count = 0

    for record in raw_records:
        cleaned_record = clean_record(record)

        if cleaned_record is None:
            rejected_count += 1
        else:
            cleaned.append(cleaned_record)

    return cleaned, rejected_count


# 5. Summarise cleaned data
def summarise_dataset(records):

    if not records:
        return {
            "record_count": 0,
            "total_units": 0,
            "total_revenue": 0,
            "average_revenue": 0
        }

    total_units = sum(
        row["units_sold"] for row in records
    )

    total_revenue = sum(
        row["revenue"] for row in records
    )

    return {
        "record_count": len(records),
        "total_units": total_units,
        "total_revenue": round(total_revenue, 2),
        "average_revenue": round(
            total_revenue / len(records), 2
        )
    }


# 6. Main program
if __name__ == "__main__":

    # Imagine these records came from a CSV file or API.
    raw_sales = [
        {"product": "  notebook ", "price": "60",
         "units_sold": "12"},

        {"product": "PEN", "price": "15",
         "units_sold": "30"},

        {"product": "Folder", "price": "-5",
         "units_sold": "8"},

        {"product": "Marker", "price": "not available",
         "units_sold": "4"},

        {"product": "Sticky   Notes", "price": "25",
         "units_sold": "10"}
    ]

    cleaned_sales, rejected = clean_dataset(raw_sales)

    summary = summarise_dataset(cleaned_sales)

    print("Cleaned records:")

    for record in cleaned_sales:
        print(record)

    print(f"\nRejected records: {rejected}")

    print("\nSummary:")

    for key, value in summary.items():
        print(f"{key}: {value}")


