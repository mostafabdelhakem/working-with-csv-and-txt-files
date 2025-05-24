"""
Using pandas describe() Function

This script demonstrates how to use the pandas Series.describe() method
to generate descriptive statistics for numeric and object (string) data.
"""

# Import needed library
import pandas as pd

print('\nDescribing the list [2, 3, 4]:')
s = pd.Series([2, 3, 4])
print(s.describe())

print('\nDescribing the list [1, 3, 5, 7, 9]:')
s = pd.Series([1, 3, 5, 7, 9])
print(s.describe())

print("\nDescribing the list ['p', 'p', 'q', 'r']:")
s = pd.Series(['p', 'p', 'q', 'r'])
print(s.describe())