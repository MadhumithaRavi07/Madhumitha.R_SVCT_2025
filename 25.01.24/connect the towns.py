#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectingTowns' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY routes
#

def connectingTowns(n, routes):
    # Write your code here
    total_routes = 1
    
    for route in routes:
        total_routes *= route
        total_routes %= 1234567

    return total_routes
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()
