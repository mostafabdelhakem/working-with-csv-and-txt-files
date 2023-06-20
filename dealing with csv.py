#### Data Science ####
# dealing with scv using pandas,
# reading from txt file methods

# import needed libraries
import pandas as pd
import numpy as np
import csv

### reading CSV file using pandas ####
salaries = pd.read_csv('salaries.csv')

# head of the csv file will be printed
print(salaries.head())

# only numerical values will be described
print(salaries.describe())

print('Done ✔')

####### Reading from txt file #########
file = open('file.txt', "r")

# read file all in one
lines = file.readlines()
print(lines)

# read file line by line
lines = file.readlines()
for line in lines:
    print(line + '\n')

# another method   
with open('file.txt', "r") as file:
    fileContent = file.read()
    print('Reading file content:\n',fileContent)
# is file closed
print(file.closed)

# the second method used to append
with open('file.txt', 'a') as file:
    file.write('Hi there!')
print('The new element has added ✔')