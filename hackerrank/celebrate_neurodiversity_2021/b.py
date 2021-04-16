# diversity day marathon
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxClockwiseRuns' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER circumference
#  2. INTEGER_ARRAY dist
#
import itertools
def maxClockwiseRuns(circumference, dist):
    # Write your code here
    s = sum(dist)
    offset = s%circumference
    ans = -1
    for r in range(len(dist)+1):
        for comb in itertools.combinations(dist, r):
            if (s-2*sum(comb))%circumference == 0:
                ans = max(ans, len(dist)-r)
    return ans
if __name__ == '__main__':