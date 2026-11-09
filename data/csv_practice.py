# csv_practice.py
# Author: Phoebe Robinson
# Module 12 Lab: Read a Sales CSV, Write a Cleaned Report

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
