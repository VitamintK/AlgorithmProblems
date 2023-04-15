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
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    
    hors = defaultdict(set)
    vers = defaultdict(set)
    def check(r,c, t):
        C = len(inps[0])-2
        R = len(inps) - 2
        cc = (c-1 - t)%C + 1
        if (1, cc) in hors[r]:
            # print(cc, hors[r])
            return False
        ccc = (c-1 + t)%C + 1
        if (-1,ccc) in hors[r]:
            # print(-1, ccc, hors[r])
            return False
        rr, rrr = (r-1-t)%R + 1, (r-1+t)%R + 1
        if (1,rr) in vers[c] or (-1,rrr) in vers[c]:
            # print(1,rr, -1, rrr, vers[c])
            return False
        return True


    for r, inp in enumerate(inps):
        for c, symb in enumerate(inp):
            if symb=='v':
                vers[c].add((1, r))
            elif symb=='^':
                vers[c].add((-1,r))
            elif symb=='>':
                hors[r].add((1,c))
            elif symb=='<':
                hors[r].add((-1,c))
    q = deque([(0, (0,1), 0, 0)])
    seen = set()
    end = (len(inps)-1, len(inps[0])-2)
    while len(q) > 0:
        i, (r,c), endreached, startreached = q.popleft()
        print(i,r,c)
        if (r,c) == end:
            if endreached and startreached:
                ans = i
                break
            if not endreached:
                endreached = 1
        if (r,c) == (0,1) and endreached:
            startreached = 1
        for dr, dc in dirs+[(0,0)]:
            nr, nc = r+dr, c+dc
            if not is_grid_valid(len(inps), len(inps[0]), nr, nc):
                continue
            if inps[nr][nc]=='#':
                continue
            if not check(nr,nc, i+1):
                # print('did not pass', i+1, nr, nc)
                continue
            key = ((i+1), (nr,nc), endreached, startreached)
            if key in seen:
                continue
            seen.add(key)
            q.append(key)

    print(ans)
else:
    pass