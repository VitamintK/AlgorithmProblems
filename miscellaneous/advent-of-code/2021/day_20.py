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
# octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
octs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

def print_grid():
    print(rmin, rmax, cmin, cmax)
    for r in range((rmin-12), (rmax)+12):
        for c in range((cmin-12), (cmax)+12):
            if grid[(r,c)]:
                print('#', end='')
            else:
                print('.', end='')
        print()

if True:
    ans = 0
    inps = []
    grid = defaultdict(lambda: False)
    rules = input()
    input()
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    
    # rs = set()
    # cs = set()
    rmin = 0
    rmax = len(inps)
    cmin = 0
    cmax = len(inps[0])
    for r in range(len(inps)):
        for c in range(len(inps[r])):
            if inps[r][c] == '#':
                grid[(r,c)] = True
                # rs.add(r)
                # cs.add(c)
    for i in range(50):
        newgrid = defaultdict(lambda: True if i%2==0 else False)
        nrs, ncs = set(), set()
        for r in range(rmin-3, rmax+3):
            for c in range(cmin-3, cmax+3):
                num = 0
                for dr, dc in octs:
                    nr, nc = r+dr, c+dc
                    num *= 2
                    if grid[(nr,nc)] == True:
                            num +=1
                if rules[num] == '#':
                    newgrid[(nr,nc)] = True
                    # nrs.add(r)
                    # ncs.add(c)
                else:
                    newgrid[(nr,nc)] = False
        rmin = min(rmin, r)
        rmax = max(rmax, r)
        cmin = min(cmin, c)
        cmax = max(cmax, c)
        grid = newgrid
        # if i != 1:
        #     rmin = min(nrs)
        #     rmax = max(nrs)
        #     cmin = min(ncs)
        #     cmax = max(ncs)
        print_grid()
    print(len([x for x in grid if grid[x]]))


    print(ans)
else:
    pass