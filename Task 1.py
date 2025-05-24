"""
Task 1 - Collect, Save, and Analyze Person Data

This script lets the user enter details (name, age, salary) for 10 persons,
saves the dataset into a CSV file, then reads it back to:
1. Display the first 3 and last 3 persons.
2. Print the 25th percentile, mean, standard deviation, max, and min of ages.
"""

import pandas as pd
import numpy as np
import csv

# Collect user input and write to CSV
with open('persons.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'Salary'])
    for num in range(10):
        name = input(f'Enter name number {num + 1}: ')
        age = int(input(f'Enter age {num + 1}: '))
        salary = float(input(f'Enter salary {num + 1}: '))
        writer.writerow([name, age, salary])

# Read the CSV file into a DataFrame
df = pd.read_csv('persons.csv', usecols=['Name', 'Age', 'Salary'])

# Display the first 3 and last 3 persons
print('\nFirst 3 persons:')
print(df.head(3))
print('\nLast 3 persons:')
print(df.tail(3))

# Calculate and display statistics for the 'Age' column
age_desc = df['Age'].describe()
percentile_25 = df['Age'].quantile(0.25)
mean_age = age_desc['mean']
std_age = age_desc['std']
max_age = age_desc['max']
min_age = age_desc['min']

print('\nAge Statistics:')
print(f"25th percentile: {percentile_25}")
print(f"Mean: {mean_age}")
print(f"Standard deviation: {std_age}")
print(f"Max: {max_age}")
print(f"Min: {min_age}")