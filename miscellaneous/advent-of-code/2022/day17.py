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

shapes = [
'####',
'''.#.
###
.#.''',
'''###
..#
..#''',
'''#
#
#
#''',
'''##
##'''
]

coords = []
for shape in shapes:
    coord = []
    for r,line in enumerate(shape.split()):
        for c,symb in enumerate(line):
            if symb=='#':
                coord.append((r,c))
    coords.append(coord)

def printgrid():
    print('')
    print(height)
    for r in grid[::-1]:
        print(r)
T = 2022
direction = {'>': 1, '<': -1}
seen = dict()
height_by_time = dict()
if True:
    ans = 0
    inp = input()
    grid = [[0] * 7]
    t = 0
    height = -1
    for i in range(len(coords) * len(inp)):
        shape = coords[i%len(coords)]
        while len(grid) < height+8:
            grid.append([0]*7)
        track = []
        
        for r,c in shape:
            track.append((height+4+r, c+2))
            # print(height+4+r, c+2)
            grid[height+4+r][c+2] = 1
        while True:
            # printgrid()
            movement = direction[inp[t%len(inp)]]
            for dr, dc in [(0,movement), (-1, 0)]:
                good_to_move = True
                for r,c in track:
                    nr,nc = r+dr, c+dc
                    if not is_grid_valid(len(grid), len(grid[0]), nr, nc):
                        good_to_move = False
                        break
                    if grid[nr][nc] == 2:
                        good_to_move = False
                        break
                if good_to_move:
                    newtrack = []
                    for r,c in track:
                        nr,nc = r+dr,c+dc
                        newtrack.append((nr,nc))
                    for r,c in track:
                        grid[r][c] = 0
                    # print('newtrack', newtrack)
                    for r,c in newtrack:
                        grid[r][c] = 1
                    track = newtrack
            t+=1

            if not good_to_move:
                for r,c in track:
                    height = max(height, r)
                    grid[r][c] = 2
                break
        hsh = (''.join([str(r) for r in grid[-10:]]), i%len(coords), t%len(inp))
        if hsh in seen:
            ii, hh = seen[hsh]
            print(i,ii,height,hh, i-ii)
            iii = 1000000000000
            addendum = height+1-hh
            print(f'after an offset of {ii}, we repeat every {i-ii} with a height difference of {addendum}')
            ans = hh
            times_after = iii-ii
            ans += times_after//(i-ii) * addendum
            print(f'and we repeat {times_after//(i-ii)} times')
            ans += height_by_time[times_after%(i-ii) + ii]-hh-1
            print(ans)
            break
        seen[hsh] = (i, height+1)
        height_by_time[i] = height+1

        # printgrid()
            


        print(height+1)
else:
    pass