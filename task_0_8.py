import math
import sys
def convert_to_time(number):
    one_hour = "hour"
    two_or_more_hours = "hours"
    one_minute = "minute"
    two_or_more_minutes = "minutes"
    output = ""

    if number < 0:
        sys.exit("Invalid Input")

    if number % 60 != 0:
        hours = math.floor(number/60)
        minutes = number % 60
    else:
        hours = math.floor(number/60)
        minutes = 0

    if hours == 0 or hours > 1:
        if minutes == 0 or minutes > 1:
            output += f'{hours} {two_or_more_hours}, {minutes} {two_or_more_minutes}'
        else:
            output += f'{hours} {two_or_more_hours}, {minutes} {one_minute}'
    else:
        if minutes == 0 or minutes > 1:
            output += f'{hours} {one_hour}, {minutes} {two_or_more_minutes}'
        else:
            output += f'{hours} {one_hour}, {minutes} {one_minute}'

    return output
        
