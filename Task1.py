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

tells = set()

for row in texts:
    tells.add(row[0])
    tells.add(row[1])

for row in calls:
    tells.add(row[0])
    tells.add(row[1])


print("There are {} different telephone numbers in the records.".format(len(tells)))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
