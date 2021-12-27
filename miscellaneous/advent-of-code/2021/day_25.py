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

def print_(inps):
    for inp in inps:
        print(''.join(inp))
    print()

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(list(input()))
        except EOFError:
            break
    ans = 0
    C = len(inps[0])
    R = len(inps)
    any_movement = True
    while any_movement:
        new_inps = [[x for x in r] for r in inps]
        any_movement = False
        # for movement in [0,1]:
        #0 is right, 1 is down
        for r in range(len(inps)):
            for c in range(len(inps[r])):
                if inps[r][c] != '>':
                        continue
                if inps[r][(c+1)%C]=='.':
                    new_inps[r][c] = '.'
                    new_inps[r][(c+1)%C] = '>'
                    any_movement = True
        inps = new_inps
        new_inps = [[x for x in r] for r in inps]

        # print_(inps)
        for c in range(C):
            for r in range(R):
                if inps[r][c] != 'v':
                        continue
                if inps[(r+1)%R][c]=='.':
                    new_inps[r][c] = '.'
                    new_inps[(r+1)%R][c] = 'v'
                    any_movement = True
        inps = new_inps
        ans += 1
        # print_(inps)
    print(ans)
else:
    pass