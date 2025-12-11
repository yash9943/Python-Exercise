'''
Take two datetimes from user start_time and end_time. Calculates the difference between 
start_time and end_time by removing night intervals (12 AM to 6 AM). (Hint: You can use 
python intervals module) 
'''

import datetime

date_time1 = datetime.datetime(2025, 12, 1, 00, 00, 00)
date_time2 = datetime.datetime(2025, 12, 10, 00, 00, 00)

difference = date_time2 - date_time1

# subtract 6 hours for each full day in the difference
res =   datetime.timedelta(hours=6 * difference.days)
# print(res)
final_res = difference - res

print("Original difference:", difference)
print("Final result:", final_res)
