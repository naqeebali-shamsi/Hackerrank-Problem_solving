#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    d = defaultdict(int)
    for stick in arr: # Map sticks with their initial lengths
        d[stick] += 1
    d = sorted(list(d.items())) # sort the sticks in increasing oerder of their lengths
    res = [len(arr)]
    for _, n in d[:-1]: # reverse loop
        res.append(res[-1] - n)
    return res

            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
