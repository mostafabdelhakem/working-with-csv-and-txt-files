"""
Dealing with CSV Files

This script demonstrates how to write to and read from CSV files using Python's csv module.
It writes a list of movies to a CSV file and then reads and prints the contents.
"""

import csv

# Writing to a CSV file
with open('movies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # writer = csv.writer(file, delimiter = '_') # To change the default delimiter (separator)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Bagging"])
    writer.writerow([2, "Harry Porter", "Harry Potter"])
    writer.writerow([3, "The God Father", "Al Pacino"])
    writer.writerow([4, "Top Gun", "Tom Cruse"])

print('\nWriting Done ✔')

# Reading from the CSV file
print('\nReading:')
with open('movies.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print('\nReading Done ✔')