# Author: Phoebe Robinson
# Module 12 Lab: Read a Sales CSV, Write a Cleaned Report
# Reflection Answers:
# 1. Unlike Excel where formulas and data transforms are done manually or via graphical menus, Python's programmatic ETL pipeline allows us to reproduce, scale, and automate data manipulation identically across thousands of files. Excel is superior for rapid visual checks and ad-hoc charting, whereas Python excels at robust, repeatable, and automated data processing.
# 2. A real business process that benefits from an append-mode log file is an automated nightly database backup or point-of-sale transaction logging. Append mode is the right tool because it preserves historical audit logs by safely adding new execution timestamps and metrics to the bottom of the file without ever overwriting past records.

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

print("---Exercise 1---")

with open(SALES_FILE, "r") as f:
   print(f"Opened {SALES_FILE}.")

print("---Exercise 2---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("---Exercise 3---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)

print("---Exercise 4---")

total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_stri, qty_str = row
        price = float(price_stri)
        quantity = int(qty_str) 
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

print("---Exercise 5---")

high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        rows_read += 1
        product, price_stri, qty_str = row
        price = float(price_stri)
        quantity = int(qty_str) 
        total = price * quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"${total:.2f}"])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Quantity", "Total"])
    for row in high_value:
        writer.writerow(row)

print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")

print("---Exercise 6---")

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${dict_total:.2f}")

print("---Exercise 7---")

product_summary = {}
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        revenue = float(row["price"]) * int(row["quantity"])
        product_summary[product] = product_summary.get(product, 0) + revenue

for product, total_revenue in product_summary.items():
    print(f"{product}: ${total_revenue:.2f}")

print("---Exercise 8---")

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"Run timestamp: {current_time} | Total Revenue: ${dict_total:.2f}\n"

with open(LOG_FILE, "a") as f:
    f.write(log_entry)

print(f"Appended run log entry to {LOG_FILE}.")