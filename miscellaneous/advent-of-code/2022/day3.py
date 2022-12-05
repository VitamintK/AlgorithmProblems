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
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

if False:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    for inp in inps:
        l = len(inp)
        a = inp[:l//2]
        b = inp[l//2:]
        s = set(a) & set(b)
        assert len(s) == 1
        x = list(s)[0]
        print(x)
        if ord(x) < ord('a'):
            y = ord(x) - ord('A') + 27
        else:
            y = ord(x) - ord('a') + 1
        ans += y
        print(y)
    

    print(ans)
else:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    for x in range(0,len(inps), 3):
        strings = inps[x:x+3]
        s = set(strings[0]) & set(strings[1]) & set(strings[2])
        assert len(s) == 1
        x = list(s)[0]
        print(x)
        if ord(x) < ord('a'):
            y = ord(x) - ord('A') + 27
        else:
            y = ord(x) - ord('a') + 1
        ans += y
        print(y)
    

    print(ans)