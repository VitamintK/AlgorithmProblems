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

if True:
    # PART 2
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    visited = set()
    R = len(inps)
    C = len(inps[0])
    for r in range(R):
        for c in range(C):
            if inps[r][c]=='S':
                start = (r,c)
    q = deque([(start, 0)])
    while len(q) > 0:
        ex, x = q.popleft()
        r,c = ex
        # visited.add(ex)
        if inps[r][c] == 'E':
            ans = x
            break
        start = inps[r][c]
        if start=='S':
            start='a'
        for dr, dc in dirs:
            nr,nc = r+dr,c+dc
            if not is_grid_valid(R,C,nr,nc):
                continue
            if (nr,nc) in visited:
                continue
            letter = inps[nr][nc]
            if letter=='E':
                letter='z'
            if ord(letter) - ord(start) > 1:
                continue
            visited.add((nr,nc))
            q.append(((nr,nc), x+1))

    print(ans)
else:
    # PART 1
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    visited = set()
    R = len(inps)
    C = len(inps[0])
    for r in range(R):
        for c in range(C):
            if inps[r][c]=='E':
                start = (r,c)
    q = deque([(start, 0)])
    while len(q) > 0:
        ex, x = q.popleft()
        r,c = ex
        # visited.add(ex)
        if inps[r][c] == 'a':
            ans = x
            break
        start = inps[r][c]
        if start=='E':
            start='z'
        for dr, dc in dirs:
            nr,nc = r+dr,c+dc
            if not is_grid_valid(R,C,nr,nc):
                continue
            if (nr,nc) in visited:
                continue
            letter = inps[nr][nc]
            if letter=='E':
                letter='z'
            if ord(letter) - ord(start) < -1:
                continue
            visited.add((nr,nc))
            q.append(((nr,nc), x+1))



    print(ans)