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

def man(x,y,xx,yy):
    return abs(x-xx)+abs(y-yy)

if False:
    # PART 1
    Y=2000000
    ans = 0
    inps = []
    while True:
        try:
            x,y,xx,yy = get_ints(input())
            inps.append([x,y,xx,yy])
        except EOFError:
            break
    intervals = []
    for x,y,xx,yy in inps:
        distance = man(x,y,xx,yy)
        y_dist = abs(y-Y)
        if y_dist > distance:
            continue
        dx = distance-y_dist
        intervals.append((x-dx, x+dx))
    intervals.sort()
    n_intervals = []
    for l,r in intervals:
        if len(n_intervals)==0 or l>n_intervals[-1][1]:
            n_intervals.append((l,r))
            continue
        r = max(r,n_intervals[-1][1])
        ll,rr = n_intervals.pop()
        n_intervals.append((ll,r))
    print(n_intervals)
    for l,r in n_intervals:
        ans += r-l+1
    print(ans)
else:
    # PART 2
    ans = 0
    inps = []
    while True:
        try:
            x,y,xx,yy = get_ints(input())
            inps.append([x,y,xx,yy])
        except EOFError:
            break
    for i in range(4000000):
        intervals = []
        for x,y,xx,yy in inps:
            distance = man(x,y,xx,yy)
            y_dist = abs(y-i)
            if y_dist > distance:
                continue
            dx = distance-y_dist
            intervals.append((x-dx, x+dx))
        intervals.sort()
        n_intervals = []
        for l,r in intervals:
            if len(n_intervals)==0 or l>n_intervals[-1][1]:
                n_intervals.append((l,r))
                continue
            r = max(r,n_intervals[-1][1])
            ll,rr = n_intervals.pop()
            n_intervals.append((ll,r))
        if len(n_intervals) > 1:
            print(i, n_intervals)
