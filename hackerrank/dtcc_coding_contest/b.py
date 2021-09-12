#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY processorTime
#  2. INTEGER_ARRAY taskTime
#

def minTime(processorTime, taskTime):
    # Write your code here
    ans = -1
    processorTime.sort()
    taskTime.sort()
    for i in processorTime:
        for j in range(4):
            t = taskTime.pop()
            ans = max(ans, i+t)
    return ans
if __name__ == '__main__':