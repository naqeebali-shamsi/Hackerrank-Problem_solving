#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    equals = {}
    for i in range(len(a)):
        try:
            equals[a[i]].append(i)
        except KeyError:
            equals[a[i]] = []
            equals[a[i]].append(i)
    min_dist = -1
    distances = []
    for k,v in equals.items():
        if len(v) == 2:
            distances.append(min([abs(v[x]-v[x+1]) for x in range(0,len(v)-1)]))
    if len(distances) > 0:
        min_dist = min(distances)
    return min_dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
