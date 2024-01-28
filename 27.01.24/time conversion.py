import os
from datetime import datetime

def timeConversion(s):
    # Parse the input time string using datetime
    time_obj = datetime.strptime(s, '%I:%M:%S%p')

    # Format the time object in 24-hour format
    result = time_obj.strftime('%H:%M:%S')

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
