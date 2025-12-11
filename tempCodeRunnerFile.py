import datetime

date_time1 = datetime.datetime(2020, 5, 17, 10, 15, 30)
date_time2 = datetime.datetime(2021, 8, 25, 12, 45, 50)

difference = date_time2 - date_time1

# subtract 6 hours for each full day in the difference
final_res = difference - datetime.timedelta(hours=6 * difference.days)

print("Original difference:", difference)
print("Final result:", final_res)