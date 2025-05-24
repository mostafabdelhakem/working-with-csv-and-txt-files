"""
Working with Pandas DataFrames

This script demonstrates how to create a pandas DataFrame with different data types,
and how to use the describe() method to generate descriptive statistics for various columns.
"""

# Import needed library
import pandas as pd

# Create a DataFrame with categorical, numeric, and object columns
data_frame = pd.DataFrame({
    'categorical': pd.Categorical(['s', 't', 'u']),
    'numeric': [2, 3, 4],
    'abject': ['p', 'q', 'r']
})

print('\nData Frame:')
print(data_frame)  # Print the entire DataFrame

print('\nNumeric Data Describe:')
print(data_frame.describe())  # Describe only numeric columns

print('\nData Frame Describe:')
print(data_frame.describe(include='all'))  # Describe all columns

print('\nCategorical Describe:')
print(data_frame.describe(include=['category']))  # Describe only categorical columns

print('\nDescribe Without Object:')
print(data_frame.describe(exclude=[object]))  # Describe all columns except object type