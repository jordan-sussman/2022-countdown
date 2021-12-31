import datetime
import time

def countdown(future_datetime, date_format):
    print('Countdown to New Years 2022')
    seconds_left = -1
    while seconds_left:
        current_time = datetime.datetime.now()
        future_time = datetime.datetime.strptime(future_datetime, date_format)
        remaining_time = future_time - current_time
        print("{0: >3d} days, {1:0>2d}:{2:0>2d}:{3:0>2d}".format(
                remaining_time.days, # remaining days
                remaining_time.seconds // 3600, # remaining hours
                remaining_time.seconds // 60 % 60, # remaining minutes
                remaining_time.seconds % 60), # remaining seconds
            end='\r')
        time.sleep(1)
        seconds_left = remaining_time.total_seconds()
    print('Happy New Year!')
countdown('2022-01-01', '%Y-%m-%d')
