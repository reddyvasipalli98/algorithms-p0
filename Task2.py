"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

my_dict = {}

for item in calls:
    if item[0] in my_dict:
        value = my_dict[item[0]]
        my_dict[item[0]] = value + int(item[3])
    else:
        my_dict.update([(item[0], int(item[3]))])

    if item[1] in my_dict:
        value = my_dict[item[1]]
        my_dict[item[1]] = value + int(item[3])
    else:
        my_dict.update([(item[1], int(item[3]))])
    

print(max(my_dict))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

