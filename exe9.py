'''
Take two datetimes from user start_time and end_time. Calculates the difference between 
start_time and end_time by removing night intervals (12 AM to 6 AM). (Hint: You can use 
python intervals module) 
'''
import datetime

date_time1 = datetime.datetime(2025, 12, 9, 00, 00, 00)
date_time2 = datetime.datetime(2025, 12, 10, 00, 00, 00)

night_start = datetime.time(0, 0, 0)  # 12 AM
night_end = datetime.time(6, 0, 0)    # 6 AM

diff = date_time2 - date_time1

for time in range(date_time1.hour, date_time2.hour):
    if time >= 0 and time < 6:
        # diff -= datetime.timedelta(hours=6)
        diff -= datetime.timedelta(hours=1)
        
print("Difference after removing night intervals (12 AM to 6 AM):", diff)