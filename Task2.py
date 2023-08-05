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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phones_spent_time = {};
for i in calls:
    phones_spent_time[i[0]] = phones_spent_time.get(i[0], 0) + int(i[-1])
    phones_spent_time[i[1]] = phones_spent_time.get(i[1], 0) + int(i[-1])

max_value = list(phones_spent_time.values())
max_key= list(phones_spent_time.keys())

max_phones_spent_time = max(max_value)

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(max_key[max_value.index(max_phones_spent_time)], max_phones_spent_time ))