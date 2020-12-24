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
    flipped = defaultdict(int)
    for inp in inps:
        buff = ''
        coords = [0,0]
        for l in inp:
            buff += l
            if buff == 'e':
                coords[0] += 1
                coords[1] += -1
            elif buff == 'se':
                coords[1] += -1
            elif buff == 'sw':
                coords[0] += -1
            elif buff =='w':
                coords[0] -= 1
                coords[1] +=1
            elif buff =='nw':
                coords[1] +=1
            elif buff=='ne':
                coords[0]+=1
            else:
                continue
            buff = ''
        flipped[tuple(coords)] += 1
    blacks = set()
    for k, v in flipped.items():
        if v%2 == 1:
            ans +=1
            blacks.add(k)
    print(ans)

    #part 2
    for i in range(100):
        newd = set()
        blackneighbors = defaultdict(int)
        for b in blacks:
            x,y = b
            cnt = 0
            for dx, dy in [(1,-1), (0,-1), (-1,0), (-1,1), (0,1), (1,0)]:
                nx, ny = x+dx, y+dy
                blackneighbors[(nx,ny)] += 1
                if (nx,ny) in blacks:
                    cnt += 1
            if cnt in [1,2]:
                newd.add(b)
        for b in blackneighbors:
            x,y = b
            if b in blacks:
                continue
            if blackneighbors[b] == 2:
                newd.add(b)
        blacks = newd
    print(len(blacks))
else:
    pass