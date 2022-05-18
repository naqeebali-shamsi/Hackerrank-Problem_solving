#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
        
def jumpingOnClouds(c, k):
    # Uncomment this code if n%k == 0 (The constraints are incorrect)
    # thunderclouds = [i for i in range(len(c)) if c[i]==1]
    # path = [i for i in range(k,len(c)+k,k)]
    # print("Path => {}".format(path))
    # print("Thunderclouds => {}".format(thunderclouds))
    # # energy = 100
    # for cloud in path:
    #     if cloud in thunderclouds:
    #         energy -= 3
    #     else:
    #         energy -= 1
    energy = 100 #initial energy
    i = k % n #initial jump from 0
    energy -= c[i] * 2 + 1 #initial energy loss
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
    return energy
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
