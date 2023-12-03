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

if False:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    num_limits = {'red': 12, 'green': 13, 'blue': 14}
    for l in inps:
        i = int(l.split(':')[0].split()[1])
        parts = l.split(':')[1].split(';')
        fail = False
        for part in parts:
            cols = part.split(',')
            for col in cols:
                num, c = col.split()
                if int(num) > num_limits[c]:
                    fail = True
                    break
        if not fail:
            ans += i
            # print(i)
    print(ans)
else:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    
    for l in inps:
        i = int(l.split(':')[0].split()[1])
        parts = l.split(':')[1].split(';')
        fail = False
        num_limits = {'red': 0, 'green': 0, 'blue': 0}
        for part in parts:
            cols = part.split(',')
            for col in cols:
                num, c = col.split()
                num_limits[c] = max(num_limits[c], int(num))
        # print(num_limits['red'] * num_limits['green'] * num_limits['blue'])
        ans += num_limits['red'] * num_limits['green'] * num_limits['blue']
    print(ans)