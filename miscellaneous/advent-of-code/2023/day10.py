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
"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

...

How many tiles are enclosed by the loop?
"""

PIPES = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(0,1), (-1,0)],
    'J': [(0,-1), (-1,0)],
    '7': [(0,-1), (1,0)],
    'F': [(0,1), (1,0)],
    'S': [(0,1), (0,-1), (1,0), (-1,0)],
    '.': [],

}

DS = []

def dfs(inps, r,c, d, distances, pr, pc, n):
    if distances[r][c] != -1:
        return
    distances[r][c] = d
    symb = PIPES[inps[r][c]]
    cnt = 0
    for dr, dc in symb:
        nr, nc = r+dr, c+dc
        if nr == pr and nc == pc:
            continue
        if is_grid_valid(len(inps), len(inps[0]), nr, nc):
            sym2 = inps[nr][nc]
            sym2 = PIPES[sym2]
            if (-dr, -dc) in sym2:
                if pr is None and pc is None and cnt != n:
                    cnt += 1
                    continue
                if pr is None and pc is None:
                    DS.append((dr, dc))
                cnt += 1
                dfs(inps, nr, nc, d+1, distances, r, c, n)
            else:
                pass

def dfs2(inps, r,c, distances, pr, pc, fill, s):
    """dfs around the loop again, and do a dfs3 to floodfill everything on the right side of the loop"""
    # -1 for unvisited, 0 for visited loop, 1 for filled.
    if fill[r][c] == 0:
        return
    fill[r][c] = 0
    symb = PIPES[inps[r][c]]
    for dr, dc in symb:
        nr, nc = r+dr, c+dc
        if nr == pr and nc == pc:
            continue
        if is_grid_valid(len(inps), len(inps[0]), nr, nc):
            if distances[nr][nc] != s+1:
                continue
            sym2 = inps[nr][nc]
            sym2 = PIPES[sym2]
            if (-dr, -dc) in sym2:
                right_turn = dirs[(dirs.index((dr, dc))+1)%4]
                mr, mc = r+right_turn[0], c+right_turn[1]
                if is_grid_valid(len(inps), len(inps[0]), mr, mc):
                    dfs3(inps, mr, mc, distances, fill)
                mr, mc = nr+right_turn[0], nc+right_turn[1]
                if is_grid_valid(len(inps), len(inps[0]), mr, mc):
                    dfs3(inps, mr, mc, distances, fill)
                dfs2(inps, nr, nc, distances, r, c, fill, s+1)



def dfs3(inps, r, c, distances, fill):
    """fill in the parts that are enclosed by the loop"""
    if distances[r][c] != -1:
        return
    if fill[r][c] != -1:
        return
    fill[r][c] = 1
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if is_grid_valid(len(inps), len(inps[0]), nr, nc):
            dfs3(inps, nr, nc, distances, fill)


def process(inps, distances, fill):
    """visualization"""
    def better_unicode_pipe(x):
        if x == '|':
            return '│'
        elif x == '-':
            return '─'
        elif x == 'L':
            return '└'
        elif x == 'J':
            return '┘'
        elif x == '7':
            return '┐'
        elif x == 'F':
            return '┌'
        elif x == 'S':
            return '┼'
        elif x == '.':
            return ' '
        else:
            return x
    for r in range(len(fill)):
        x = []
        for c in range(len(fill[0])):
            i = better_unicode_pipe(inps[r][c])
            if fill[r][c] == 1:
                x.append(f'\033[92mI\033[0m')
            elif distances[r][c] != -1:
                x.append(f'\033[94m{i}\033[0m')
            else:
                x.append(i)
        print(''.join(x))

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    for row in range(len(inps)):
        for col in range(len(inps[0])):
            if inps[row][col] == 'S':
                start = (row, col)
                break
    distances = [[-1 for _ in range(len(inps[0]))] for _ in range(len(inps))]
    dfs(inps, start[0], start[1], 0, distances, None, None, 0)
    distances2 = [[-1 for _ in range(len(inps[0]))] for _ in range(len(inps))]
    dfs(inps, start[0], start[1], 0, distances2, None, None, 1)

    for r in range(len(inps)):
        for c in range(len(inps[0])):
            ans = max(ans, min(distances[r][c], distances2[r][c]))
    print(ans) # PART 1

    fill = [[-1 for _ in range(len(inps[0]))] for _ in range(len(inps))]
    dfs2(inps, start[0], start[1], distances2, None, None, fill, 0)
    process(inps, distances, fill)
    ans = 0
    for r in fill:
        for c in r:
            if c == 1:
                ans += 1
    print(ans) # PART 2

else:
    pass