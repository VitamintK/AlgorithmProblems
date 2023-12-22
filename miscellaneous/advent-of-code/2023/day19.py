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
import numpy as np

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
####################################

global ans
PART = 1
PART = 2
if PART == 1:
    ans = 0
    wfs = []
    pts = []
    inps = [wfs, pts]
    i = 0
    while True:
        try:
            x = input()
            if x.strip() == '':
                i += 1
                continue
            inps[i].append(x)
            
        except EOFError:
            break
    print(inps)
    wfss = dict()
    for wf in wfs:
        name, rest = wf.split('{')
        rest = rest[:-1]
        ws = []
        for w in rest.split(','):
            if ':' in w:
                cond, res = w.split(':')
                ws.append((cond, res))
            else:
                ws.append(('True', w))
        wfss[name] = ws
    print(wfss)
    print(pts)
    for pt in pts:
        x,m,a,s = get_ints(pt)
        name = 'in'
        while name not in ['A', 'R']:
            print(name)
            wf = wfss[name]
            for w in wf:
                if eval(w[0]):
                    name = w[1]
                    break
        
        if name == 'A':
            ans += x+m+a+s

    print(ans)
else:
    ans = 0
    wfs = []
    pts = []
    inps = [wfs, pts]
    i = 0
    while True:
        try:
            x = input()
            if x.strip() == '':
                i += 1
                break
            inps[i].append(x)
            
        except EOFError:
            break
    wfss = dict()
    for wf in wfs:
        name, rest = wf.split('{')
        rest = rest[:-1]
        ws = []
        for w in rest.split(','):
            if ':' in w:
                cond, res = w.split(':')
                ws.append((cond, res))
            else:
                ws.append(('True', w))
        wfss[name] = ws
    
    def trace(name, ranges):
        global ans
        if name == 'R':
            return
        if name == 'A':
            x = 1
            for k in ranges:
                x *= ranges[k][1] - ranges[k][0] + 1
            ans += x
            return
        wf = wfss[name]
        for w in wf:
            cond = w[0]
            if cond == 'True':
                trace(w[1], ranges)
                return
            v = cond[0]
            cmp = cond[1]
            val = int(cond[2:])
            # print(v, cmp, val)
            if cmp == '>':
                if val < ranges[v][1]:
                    new_range = [max(val+1, ranges[v][0]), ranges[v][1]]
                    trace(w[1], {k:(r if k!=v else new_range) for k,r in ranges.items()})
                if val > ranges[v][0]:
                    new_range = [ranges[v][0], min(val, ranges[v][1])]
                    ranges = {k:(r if k!=v else new_range) for k,r in ranges.items()}
                else:
                    break
            else:
                if val > ranges[v][0]:
                    new_range = [ranges[v][0], min(val-1, ranges[v][1])]
                    trace(w[1], {k:(r if k!=v else new_range) for k,r in ranges.items()})
                if val < ranges[v][1]:
                    new_range = [max(val, ranges[v][0]), ranges[v][1]]
                    ranges = {k:(r if k!=v else new_range) for k,r in ranges.items()}
                else:
                    break

    trace('in', {k: [1, 4000] for k in 'xmas'})

    print(ans)

# BOUGHT IN-FLIGHT WIFI FOR THIS ONE, didn't even make the leaderboard :(