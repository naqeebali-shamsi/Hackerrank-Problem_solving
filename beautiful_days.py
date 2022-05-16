#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def reverseNum(num):
    return int((str(num)[::-1]))

def checkCondition(num, k):
    condNum = float(abs(num-reverseNum(num)))/float(k)
    if condNum - int(condNum) > 0:
        return False
    return True

def beautifulDays(i, j, k):
    # Write your code here
    beautifuldays = 0
    for x in range(i,j+1):
        if checkCondition(x,k):
            beautifuldays += 1
    return beautifuldays
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
