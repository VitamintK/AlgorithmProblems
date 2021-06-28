#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'changeTasks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY tasks as parameter.
#

def changeTasks(tasks):
    # Write your code here
    ts = list(set(tasks))
    ts.sort()
    m = dict()
    for i in range(len(ts)):
        m[ts[i]] = i
    ans = []
    for i in tasks:
        ans.append(m[i] + 1)
    return ans
    
if __name__ == '__main__':