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

INTERVAL_TYPE_INCLUSIVE = 0
INTERVAL_TYPE_EXCLUSIVE = 1
# def make_interval_class(start_type=INTERVAL_TYPE_INCLUSIVE, end_type=INTERVAL_TYPE_EXCLUSIVE):
#     class Interval:
#         start_type = start_type
#         end_type = end_type
#         def __init__(self, start, end):
#             self.start = start
#             self.end = end
# def merge(interval_a, interval_b):
#     interval = (min(interval_a[0], interval_b[0]), max(interval_a[1], interval_b[1]))
#     if interval[0] > interval[1]:
#         return None
####################################

PART = 1
PART = 2
if PART == 1:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    R, C = len(inps), len(inps[0])
    inps2 = []
    for inp in inps:
        xs, vs = inp.split('@')
        xs, vs = get_ints(xs), get_ints(vs)
        inps2.append((xs, vs))
    # L, H = 7, 27
    L = 200000000000000
    H = 400000000000000
    for i in range(len(inps2)):
        for j in range(i+1, len(inps2)):
            xs1, vs1 = inps2[i]
            xs2, vs2 = inps2[j]
            m1 = vs1[1]/vs1[0]
            m2 = vs2[1]/vs2[0]
            if m1 == m2:
                continue
            x = (m1*xs1[0] - m2*xs2[0] + xs2[1] - xs1[1])/(m1-m2)
            y = xs1[1] + m1*(x-xs1[0])
            if (x - xs1[0]) / vs1[0] > 0 and (x - xs2[0]) / vs2[0] > 0 and L <= x <= H and L <= y <= H:
                ans += 1

    

    print(ans)
else:
    from sympy.solvers import solve
    from sympy import Symbol
    ns = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    R, C = len(inps), len(inps[0])
    inps2 = []
   
    eqs = []
    variables = []
    base_symbs = [
        Symbol('x', integer=True),
        Symbol('y', integer=True),
        Symbol('z', integer=True),
        Symbol('vx', integer=True),
        Symbol('vy', integer=True),
        Symbol('vz', integer=True)]
    x, y, z, vx, vy, vz = base_symbs

    for j, inp in enumerate(inps):
        if j > 7:
            break
        xs, vs = inp.split('@')
        xs, vs = get_ints(xs), get_ints(vs)
        t = Symbol(f't{j}', integer=True, nonnegative=True)
        variables.append(t)
        for i in range(3):
            l = [x,y,z][i]
            v = [vx,vy,vz][i]
            symbs = []
            eqs.append(l + t * (v - vs[i]) - xs[i])
    # L, H = 7, 27
    print(eqs)
    ans = solve(eqs, base_symbs + variables)
    print(ans)
    print(ans[0][0] + ans[0][1] + ans[0][2])

    # didn't solve this until going to bed and checking other's solutions.
    # When I read others' solutions, I realized I didn't need all gazillion equations,
    # only the first 6 or so. So I just added the `if j > 7: break` line and it worked instantly
    # instead of running interminably.
