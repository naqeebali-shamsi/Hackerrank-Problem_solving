#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def getindexof(elem, p):
   return p.index(elem)

def permutationEquation(p):
    # Write your code here
    n = len(p)
    ans = []
    for i in range(1,n+1):
        temp = getindexof(i,p)+1
        ppy = getindexof(temp,p)+1
        # print("x=> {} | pos(x) => {} | pos(pos(x)) => {}".format(i,temp,ppy))
        ans.append(ppy)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
