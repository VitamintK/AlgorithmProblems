#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fillBarrels' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#  3. INTEGER X
#

def fillBarrels(A, B, X):
    # Write your code here
    A.sort()
    B.sort()
    ans = 0
    tot = 0
    ra = len(A)-1
    rb = len(B)-1
    la, lb = 0,0
    print(A, B, X)
    for i in range(len(A)):
        # x = A[ra]
        # y = B[rb]
        print(la, ra, lb, rb)
        if ra > la and (rb <= lb or A[ra]+B[lb] > B[rb]+A[la]):
            z = A[ra] + B[lb]
            ra -= 1
            lb += 1
            tot += z
            ans = max(ans, z)
        else:
            z = B[rb] + A[la]
            la += 1
            rb -= 1
            tot += z
            ans = max(ans, z)
        # print(z)
    # print(sum(A) + sum(B), tot)
    # print(ans)
    if ans <= X:
        return 1, len(A) * X - sum(A)-sum(B)
    else:
        return -1, ans
            
if __name__ == '__main__':