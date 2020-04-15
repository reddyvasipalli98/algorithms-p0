"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

telephones = []

for row in texts:
    countFrom = 0
    countTo = 0
    for item in telephones:
        if item == row[0]:
            countFrom = countFrom + 1
        if item == row[1]:
            countTo = countTo + 1
    if countFrom == 0:
        telephones.append(row[0])
    if countTo == 0:
        telephones.append(row[1])

for row in calls:
    countFrom = 0
    countTo = 0
    for item in telephones:
        if item == row[0]:
            countFrom = countFrom + 1
        if item == row[1]:
            countTo = countTo + 1
    if countFrom == 0:
        telephones.append(row[0])
    if countTo == 0:
        telephones.append(row[1])

print("There are {} different telephone numbers in the records.".format(len(telephones)))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
