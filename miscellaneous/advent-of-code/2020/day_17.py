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

import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

def make_new():
    return defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: '.'))))

def get_next(grid, it):
    ngrid = make_new()
    cnts = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
    for z in grid:
        for y in grid[z]:
            for x in grid[z][y]:
                for w in grid[z][y][x]:
                    cnt = 0
                    if grid[z][y][x][w] == '.':
                        continue
                    for dz in (-1,0,1):
                        for dy in (-1,0,1):
                            for dx in (-1,0,1):
                                for dw in (-1,0,1):
                                    if dz==dy==dx==dw==0:
                                        continue
                                    nz, ny, nx, nw = z+dz, y+dy, x+dx, w+dw
                                    # if nw in grid[nz][ny][nx] and grid[nz][ny][nx][nw] == '#':
                                    #     cnt +=1
                                    cnts[nz][ny][nx][nw] +=1
    for z in cnts:
        for y in cnts[z]:
            for x in cnts[z][y]:
                for w in cnts[z][y][x]:
                    cnt = cnts[z][y][x][w]
                    if grid[z][y][x][w] == '#':
                        if cnt in (2,3):
                            ngrid[z][y][x][w] = '#'
                        else:
                            ngrid[z][y][x][w] = '.'
                    else:
                        if cnt == 3:
                            ngrid[z][y][x][w] = '#'
                        else:
                            ngrid[z][y][x][w] = '.'
    return ngrid

def count(grid):
    cnt = 0
    for z in grid:
        for y in grid[z]:
            for x in grid[z][y]:
                for w in grid[z][y][x]:
                    if grid[z][y][x][w] == '#':
                        cnt +=1
    return cnt

if True:
    ans = 0
    inps = []
    grid = make_new()
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    
    for y, inp in enumerate(inps):
        for x, v in enumerate(inp):
            grid[0][0][y][x] = v
    print(count(grid))
    for i in range(6):
        grid = get_next(grid, 25)
        print(count(grid))
    
else:
    pass