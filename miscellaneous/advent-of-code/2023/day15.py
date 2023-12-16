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

if False:
    ans = 0
    inps = []
    while True:
        try:
            inps = input().split(',')
        except EOFError:
            break
    def f(s):
        cur = 0
        for c in s:
            cur += ord(c)
            cur *= 17
            cur %= 256
        return cur
    for x in inps:
        ans += f(x)



    print(ans)
else:
    ans = 0
    inps = []
    while True:
        try:
            inps = input().split(',')
        except EOFError:
            break
    def f(s):
        cur = 0
        for c in s:
            cur += ord(c)
            cur *= 17
            cur %= 256
        return cur
    boxes = [[] for i in range(256)]
    for x in inps:
        if '=' in x:
            h = f(x[:-2])
            l = x[:-2]
            j = int(x[-1])
            for i in range(len(boxes[h])):
                if boxes[h][i][0] == l:
                    boxes[h][i] = (l, j)
                    break
            else:
                boxes[h].append((l, j))
        else:
            h = f(x[:-1])
            l = x[:-1]
            for i in range(len(boxes[h])):
                if boxes[h][i][0] == l:
                    boxes[h].pop(i)
                    break
    for i in range(256):
        for j in range(len(boxes[i])):
            ans += boxes[i][j][1] * (i+1) * (j+1)
        
    



    print(ans)