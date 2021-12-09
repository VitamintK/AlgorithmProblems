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

def dfs(coord, grid, visited):
    ans = 1
    r,c = coord
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if (nr,nc) in visited:
            continue
        if not is_grid_valid(len(grid), len(grid[0]), nr, nc):
            continue
        if int(grid[nr][nc]) > int(grid[r][c]) and int(grid[nr][nc])!=9:
            visited.add((nr,nc))
            ans += dfs((nr,nc), grid, visited)
    return ans

if False:
    # part 1
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    for line in range(len(inps)):
        for c in range(len(inps[line])):
            for dr, dc in dirs:
                nr, nc = line+dr, c+dc
                if not is_grid_valid(len(inps), len(inps[line]), nr, nc):
                    continue
                if int(inps[nr][nc]) <= int(inps[line][c]):
                    break
            else:
                ans += 1 + int(inps[line][c])

    print(ans)
else:
    # part 2
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    lowpoints = []
    for line in range(len(inps)):
        for c in range(len(inps[line])):
            for dr, dc in dirs:
                nr, nc = line+dr, c+dc
                if not is_grid_valid(len(inps), len(inps[line]), nr, nc):
                    continue
                if int(inps[nr][nc]) <= int(inps[line][c]):
                    break
            else:
                ans += 1 + int(inps[line][c])
                lowpoints.append((line, c))
    basinsizes = []
    for lowpoint in lowpoints:
        basinsize = dfs(lowpoint, inps, set())
        print(basinsize)
        basinsizes.append(basinsize)
    basinsizes.sort()
    a,b,c = basinsizes[-3:]
    print(a*b*c)

    # print(ans)