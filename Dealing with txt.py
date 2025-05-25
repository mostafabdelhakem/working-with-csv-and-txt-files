"""
Dealing with TXT Files

This script demonstrates how to read from and write to a text file in Python.
It shows how to read all lines at once, read line by line, check if a file is closed,
read the entire file content, and append new content to the file.
"""

import os

# Ensure the file exists before trying to read it
if not os.path.exists('data.txt'):
    with open('data.txt', 'w') as file:
        file.write("This is the initial content of the file.\nLine two here.")

# Reading the file all at once
with open('data.txt', 'r') as file:
    print('Read file all in one:')
    lines = file.readlines()
    print(lines)

# Reading line by line
print('Read file line by line:')
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Reading entire content
with open('data.txt', "r") as file:
    fileContent = file.read()
    print('Reading file content:\n', fileContent)

# Check if file is closed (this checks the last used `file`, which is now out of scope)
print('Is file closed:', file.closed)  # This will always be True when using `with`

# Appending to the file
with open('data.txt', 'a') as file:
    file.write('\nHi there!')

print('The new element has been added ✔')
