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

set_calls = set()
set_texts = set()
set_teles = []

for item in calls:
    set_calls.add(item[0])

for item in texts:
    set_texts.add(item[0])

for item_call in set_calls:
    tester = 0
    for item_text in set_texts:
        if item_call == item_text:
            tester = tester + 1
    if tester == 0:
        set_teles.append(item_call)

print(set(set_teles))

        

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

