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

outgoing_calls = set([row[0] for row in calls])
incomming_calls = set([row[1] for row in calls])
sending_text = set([row[0] for row in texts])
receiving_text = set([row[1] for row in texts])
telemarketers = sorted(outgoing_calls - incomming_calls - sending_text - receiving_text)
print("These numbers could be telemarketers: ")
for number in telemarketers:
    print(number)