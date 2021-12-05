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

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    N = 1000
    grid = [[0 for i in range(N)] for j in range(N)]
    for inp in inps:    
        x1,y1, x2,y2 = get_ints(inp)
        if x1==x2:
            y1, y2 = min(y1,y2), max(y1,y2)
            for i in range(y1, y2+1):
                grid[x1][i] +=1
        elif y1==y2:
            x1,x2 = min(x1,x2), max(x1,x2)
            for i in range(x1, x2+1):
                grid[i][y1] +=1
        else:
            x, y = x1, y1
            dx = abs(x2-x1)//(x2-x1)
            dy = abs(y2-y1)//(y2-y1)
            while True:
                grid[x][y] +=1
                x+=dx
                y+=dy
                if x==x2 and y==y2:
                    break
            grid[x][y] +=1
        # print(x1,y1,x2,y2)
    for i in range(N):
        for j in range(N):
            if grid[i][j] > 1:
                ans +=1
    # print(grid)
    print(ans)
else:
    pass