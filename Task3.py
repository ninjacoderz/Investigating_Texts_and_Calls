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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def get_telephone_type(tel_num):
  if tel_num.startswith('(0') and tel_num.find(')') != -1:
    return 'fixed'
  elif (tel_num.startswith('7') or tel_num.startswith('8') or tel_num.startswith('9')) and ' ' in tel_num:
    return 'mobile'
  elif tel_num.startswith('140'):
    return 'telemarketers'
  else:
    return None

def get_area_code(tel_num, tel_type):
  if tel_type == 'fixed':
    return tel_num[0: tel_num.find(')') + 1]
  elif tel_type == 'mobile':
    return tel_num[0:4]
  elif tel_type == 'telemarketers':
    return '140'
  else:
    return None

area_codes = []
number_of_bangalore_caller = 0
number_of_bangalore_callee = 0
for call in calls:
  if(call[0].startswith('(080)')):
    tel_type = get_telephone_type(call[1])
    area_code = get_area_code(call[1], tel_type)
    area_codes.append(area_code)
    number_of_bangalore_caller += 1
    if(area_code == "(080)"):
      number_of_bangalore_callee += 1
    
area_codes_set = sorted(set(area_codes))

print("The numbers called by people in Bangalore have codes:")
for code in area_codes_set:
	print(code)

percentage =(number_of_bangalore_callee / number_of_bangalore_caller) * 100  

message = "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."

print(message.format( "%.2f" % percentage))