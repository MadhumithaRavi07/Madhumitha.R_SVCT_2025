#!/usr/bin/env python3

import math
import os
import random
import re
import sys

# Complete the 'findPoint' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER px
#  2. INTEGER py
#  3. INTEGER qx
#  4. INTEGER qy

def findPoint(px, py, qx, qy):
    rx = 2 * qx - px
    ry = 2 * qy - py
    return [rx, ry]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for _ in range(n):
        px, py, qx, qy = map(int, input().split())
        result = findPoint(px, py, qx, qy)
        fptr.write(' '.join(map(str, result)) + '\n')

    fptr.close()
