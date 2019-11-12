import datetime
import time

def get_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def is_time_formatted(string_time):
    try:
        time.strptime(string_time, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False