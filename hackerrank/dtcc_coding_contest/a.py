#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def getMin(s):
    # Write your code here
    cnt = 0
    ans = 0
    for x in s:
        if x == '(':
            cnt += 1
        else:
            if cnt <= 0:
                ans +=1 
            else:
                cnt -=1
    ans += max(0,cnt)
    return ans

if __name__ == '__main__':