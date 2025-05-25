"""
Dealing with CSV Files Using Pandas

This script demonstrates how to read a CSV file using pandas,
display the first few rows, and generate descriptive statistics
for the numerical columns.  If the file isn't found, a small
sample CSV is generated automatically.
"""

import os
import pandas as pd

CSV_FILE = "salaries.csv"

# ------------------------------------------------------------------
# 1) Ensure the CSV exists (create a tiny demo one if it doesn’t)
# ------------------------------------------------------------------
if not os.path.exists(CSV_FILE):
    sample_df = pd.DataFrame({
        "Employee"  : ["Ali", "Sara", "Hisham", "Nour"],
        "Department": ["IT",  "HR",   "Finance", "Marketing"],
        "Salary"    : [12000, 9500,   13500,     11000],
    })
    sample_df.to_csv(CSV_FILE, index=False)
    print(f"'{CSV_FILE}' not found → sample file created with demo data.\n")

# ------------------------------------------------------------------
# 2) Read the file and inspect its contents
# ------------------------------------------------------------------
salaries = pd.read_csv(CSV_FILE)

print("First five rows:")
print(salaries.head(), end="\n\n")

print("Descriptive statistics:")
print(salaries.describe(), end="\n\n")

print("Done ✔")
