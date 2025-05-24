"""
Dealing with TXT Files

This script demonstrates how to read from and write to a text file in Python.
It shows how to read all lines at once, read line by line, check if a file is closed,
read the entire file content, and append new content to the file.
"""

# Reading the file all at once
file = open('G:\\Projects\\ITI - AI\\Session3 - Data Science\\data.txt', "r")
print('Read file all in one:')
lines = file.readlines()
print(lines)  # Read file all in one

# Attempting to read again (will return empty since pointer is at EOF)
print('Read file line by line:')
lines = file.readlines()
for line in lines:
    print(line + '\n')  # Read file line by line

file.close()

# Another method: using 'with' to read the entire file content
with open('G:\\Projects\\ITI - AI\\Session3 - Data Science\\data.txt', "r") as file:
    fileContent = file.read()
    print('Reading file content:\n', fileContent)

print(file.closed)  # Check if file is closed

# Appending to the file
with open('G:\\Projects\\ITI - AI\\Session3 - Data Science\\data.txt', 'a') as file:
    file.write('Hi there!')
print('The new element has been added ✔')