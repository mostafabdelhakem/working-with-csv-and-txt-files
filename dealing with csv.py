"""
Dealing with CSV Files Using Pandas

This script demonstrates how to read a CSV file using pandas,
display the first few rows, and generate descriptive statistics
for the numerical columns.
"""

# Import needed library
import pandas as pd

# Read CSV file using pandas
salaries = pd.read_csv('salaries.csv')

# Display the first few rows of the DataFrame
print(salaries.head())

# Display descriptive statistics for numerical columns
print(salaries.describe())

print('Done ✔')