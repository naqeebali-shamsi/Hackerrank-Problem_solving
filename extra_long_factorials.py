#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#
def factorial(n):
    if n <=1 :
        return 1
    else:
        return n*factorial(n-1)
def extraLongFactorials(n):
    # Write your code here
    if n<=1:
        print(1)
    else:
        print(n * factorial(n-1))

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
