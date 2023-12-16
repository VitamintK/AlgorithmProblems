from collections import defaultdict, deque, Counter
# d = deque()
# d.append(5)
# x = d.popleft()
import re
# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist") 
# # or re.search
# >>> m.group(0)       # The entire match
# 'Isaac Newton'
# >>> m.group(1)       # The first parenthesized subgroup.
# 'Isaac'
# >>> m.group(2)       # The second parenthesized subgroup.
# 'Newton'
# >>> m.group(1, 2)    # Multiple arguments give us a tuple.
# ('Isaac', 'Newton')
from heapq import heappush, heappop
# >>> heap = []
# >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# >>> for item in data:
# ...     heappush(heap, item)
# heap[0] is the smallest item
import string
# string.ascii_lowercase == 'abcde...'
# string.ascii_uppercase == 'ABCDE...'
from functools import lru_cache
# @lru_cache(maxsize=None)

import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
directions = 'RDLU'
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)
def sign_of(x):
    if x==0:
        return 0
    return x/abs(x)

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    for inp in inps:
        s, xs = inp.split()
        s = [s] * 5
        s = '?'.join(s)
        xs += ','
        xs *= 5
        xs = get_ints(xs)
        ys = [0]
        c = 0
        for x in xs:
            c += x
            ys.append(c)
        dp = [[0 for i in range(ys[-1]+1)], [0 for i in range(ys[-1]+1)]]
        # dp[0] = last was empty, dp[1] = last was full
        dp[0][0] = 1
        for x in s:
            new_dp = [[0 for i in range(ys[-1]+1)], [0 for i in range(ys[-1]+1)]]
            if x in '.?':
                for i in range(0, ys[-1]+1):
                    if i in ys:
                        new_dp[0][i] += dp[0][i] + dp[1][i]
                    else:
                        new_dp[0][i] += dp[0][i]
            if x in '#?':
                for i in range(1, ys[-1]+1):
                    if i-1 in ys:
                        new_dp[1][i] += dp[0][i-1]
                    else:
                        new_dp[1][i] += dp[1][i-1]
            dp = new_dp
        print(dp[0][-1] + dp[1][-1])
        ans += dp[0][-1] + dp[1][-1]

    print(ans)
else:
    pass