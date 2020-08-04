#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countCups' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY balls
#  3. 2D_INTEGER_ARRAY swaps
#  4. 2D_INTEGER_ARRAY queries
#
import bisect
n, m, s, q = map(int, input().split())
balls = [int(x) for x in input().split()]

revballs = {x for x in balls}
for i in range(s):
    u,v = map(int, input().split())
    if u in revballs:
        if v in revballs:
            continue
        revballs.add(v)
        revballs.remove(u)
    else:
        if v in revballs:
            revballs.add(u)
            revballs.remove(v)
        else:
            continue
balls = [x for x in sorted(revballs)]
ans = []
for i in range(q):
    l, r = map(int, input().split())
    L = bisect.bisect_left(balls, l)
    R = bisect.bisect_right(balls, r)
    ans.append(str(R-L))
print(' '.join(ans))
    