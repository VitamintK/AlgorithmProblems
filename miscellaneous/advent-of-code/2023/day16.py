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

"""
Got on the leaderboard today for both parts! Github Copilot helped a decent amount with this one. Is that wrong to the other leaderboard-chasers?
  Maybe, so I should be up-front about my Copilot usage.
I wrote the instructions for '|' and copilot pretty much filled out '-'. Same with '/' and '\\'.
It also inferred what I was going for with the part 2 code after I only wrote a couple lines of it, and finished the rest.
"""

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    def go(r, c, dr, dc):
        energized = set()
        en = [[0 for _ in range(len(inps[0]))] for _ in range(len(inps))]
        been = set()
        def dfs(r, c, dr, dc):
            if not is_grid_valid(len(inps), len(inps[0]), r,c):
                return
            if (r,c,dr,dc) in been:
                return
            been.add((r,c,dr,dc))
            energized.add((r,c))
            en[r][c] = 1
            x = inps[r][c]
            if x =='.':
                dfs(r+dr, c+dc, dr, dc)
            elif x == '|':
                if dc != 0:
                    dfs(r+1, c, 1, 0)
                    dfs(r-1, c, -1, 0)
                else:
                    dfs(r+dr, c+dc, dr, dc)
            elif x == '-':
                if dr != 0:
                    dfs(r, c+1, 0, 1)
                    dfs(r, c-1, 0, -1)
                else:
                    dfs(r+dr, c+dc, dr, dc)
            elif x == '\\':
                if dr == 0:
                    dfs(r+dc, c, dc, 0)
                else:
                    dfs(r, c+dr, 0, dr)
            elif x == '/':
                if dr == 0:
                    dfs(r-dc, c, -dc, 0)
                else:
                    dfs(r, c-dr, 0, -dr)
        dfs(r,c,dr,dc)
        # for e in en:
        #     print(''.join(map(str, e)))
        return len(energized)
    
    for r in range(len(inps)):
        ans = max(ans, go(r,0,0,1))
        ans = max(ans, go(r,len(inps[0])-1,0,-1))
    for c in range(len(inps[0])):
        ans = max(ans, go(0,c,1,0))
        ans = max(ans, go(len(inps)-1,c,-1,0))
    print(ans)
else:
    pass