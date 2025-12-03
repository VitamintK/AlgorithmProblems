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
import numpy as np

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

INTERVAL_TYPE_INCLUSIVE = 0
INTERVAL_TYPE_EXCLUSIVE = 1
# def make_interval_class(start_type=INTERVAL_TYPE_INCLUSIVE, end_type=INTERVAL_TYPE_EXCLUSIVE):
#     class Interval:
#         start_type = start_type
#         end_type = end_type
#         def __init__(self, start, end):
#             self.start = start
#             self.end = end
# def merge(interval_a, interval_b):
#     interval = (min(interval_a[0], interval_b[0]), max(interval_a[1], interval_b[1]))
#     if interval[0] > interval[1]:
#         return None
####################################

# PART = 1
PART = 2
if PART == 1:
    ans = 0
    inps = []
    while True:
        try:
            inp = input().split(',')
            for i in inp:
                if i == '':
                    continue
                ints = [int(x) for x in i.split('-')]
                if len(ints) == 2:
                    inps.append(ints)
        except EOFError:
            break
    for a,b in inps:
        for x in range(a, b+1):
            if len(str(x))%2 == 1:
                continue
            if str(x)[:len(str(x))//2] == str(x)[len(str(x))//2:]:
                ans += x
    print(ans)
else:
    ans = 0
    inps = []
    while True:
        try:
            inp = input().split(',')
            for i in inp:
                if i == '':
                    continue
                ints = [int(x) for x in i.split('-')]
                if len(ints) == 2:
                    inps.append(ints)
        except EOFError:
            break
    for a,b in inps:
        for x in range(a, b+1):
            for i in range(1, len(str(x))//2 + 1):
                prefix = str(x)[:i]
                if str(x) == prefix * (len(str(x))//i):
                    ans += x
                    break
    print(ans)