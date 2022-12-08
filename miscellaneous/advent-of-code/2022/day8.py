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
            inps.append([int(x) for x in input()])
        except EOFError:
            break
    visible = [[0 for x in row] for row in inps]
    for r in range(len(inps)):
        for c in range(len(inps[r])):
            xs = [
                inps[r][:c],
                inps[r][c+1:],
                [inps[rr][c] for rr in range(0,r)],
                [inps[rr][c] for rr in range(r+1,len(inps))]
            ]
            good = False
            for x in xs:
                if len(x) == 0 or max(x) < inps[r][c]:
                    good = True
            ans += good
    

    print(ans)
else:
    ans = 0
    inps = []
    while True:
        try:
            inps.append([int(x) for x in input()])
        except EOFError:
            break
    visible = [[0 for x in row] for row in inps]
    for r in range(len(inps)):
        for c in range(len(inps[r])):
            print(r,c)
            x = inps[r][c]
            cur = 1
            for dr, dc in dirs:
                i = 1
                ddr = dr * i
                ddc = dc * i
                nr, nc = r+ddr, c + ddc
                while is_grid_valid(len(inps), len(inps[r]), nr, nc):
                    if inps[nr][nc] >= x:
                        i+=1
                        break
                    i += 1
                    ddr = dr * i
                    ddc = dc * i
                    nr, nc = r+ddr, c + ddc
                # print(i)
                cur *= (i-1)
            ans = max(ans, cur)
    print(ans)
    pass