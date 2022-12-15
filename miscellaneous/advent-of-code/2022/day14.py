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
    return int(x/abs(x))

if True:
    ans = 0
    inps = []
    low = 0
    while True:
        try:
            inp = input()
            inps.append(inp)
            inp = inp.split(' -> ')
            for i in inp:
                x,y = i.split(',')
                y = int(y)
                low = max(y,low)
        except EOFError:
            break
    print(low)
    grid = defaultdict(int)
    # for c in range()
    for inp in inps:
        inp = inp.split(' -> ')
        prev = None
        for point in inp:
            point = [int(x) for x in point.split(',')]
            if prev is None:
                prev = point
                continue
            pc,pr = prev
            c,r = point
            if pr==r:
                for cc in range(pc,c,sign_of(c-pc)):
                    # print(r,cc)
                    grid[(r,cc)] = 1
            else:
                for rr in range(pr,r,sign_of(r-pr)):
                    grid[(rr,c)] = 1
            grid[(r,c)] = 1
            prev = point
    # for r in range(10):
        # print(grid[(r,494:504)])
    while True:
        sand_abyss = False
        r,c = 0,500
        ans += 1
        while True:
            if r == low+1:
                grid[(r,c)] = 2
                break
            if grid[(r+1,c)] == 0:
                r += 1
            elif grid[(r+1,c-1)] == 0:
                r += 1
                c -= 1
            elif grid[(r+1,c+1)] == 0:
                r+=1
                c += 1
            else:
                grid[(r,c)] = 2
                if r==0 and c==500:
                    sand_abyss=True
                break
            # if r > 590:
            #     sand_abyss = True
            #     break
        if sand_abyss:
            break
    print(ans)
else:
    pass