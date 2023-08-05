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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
numbers_texts = [row[0] for row in texts] + [row[1] for row in texts]

numbers_calls = [row[0] for row in calls] + [row[1] for row in calls]
numbers_set = set(numbers_texts + numbers_calls)
print("There are {0} different telephone numbers in the records.".format(len(numbers_set)))