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
            a = get_ints(input())
            b = get_ints(input())
            p = get_ints(input())
            inps.append((a,b,p))
            input()
        except EOFError:
            break
    R, C = len(inps), len(inps[0])
    for inp in inps:
        a,b,p = inp
        # print(a, b, p)
        ax, ay = a
        bx, by = b
        px, py = p
        best = 10000000
        for A in range(101):
            for B in range(101):
                if A*ax+B*bx == px and A*ay+B*by == py:
                    best = min(best, A * 3 + B)
        if best != 10000000:
            ans += best

    print(ans)
else:
    def is_coprime(n,m):
        while m:
            n,m = m,n%m
        return n == 1
    def crt(xs, ns):
        n = 1
        for x in ns:
            n *= x
        ans = 0
        for i in range(len(xs)):
            a = xs[i]
            n_i = n // ns[i]
            m_i = pow(n_i, -1, ns[i])
            ans += a * n_i * m_i
        return ans % n
    ans = 0
    inps = []
    while True:
        try:
            a = get_ints(input())
            b = get_ints(input())
            p = get_ints(input())
            inps.append((a,b,p))
            input()
        except EOFError:
            break
    R, C = len(inps), len(inps[0])
    for inp in inps:
        a,b,p = inp
        # print(a, b, p)
        ax, ay = a
        bx, by = b
        px, py = p
        px += 10000000000000
        py += 10000000000000

        # ax * A + bx * B = px
        # ay * A + by * B = py

        # A = (px - bx * B) / ax
        # ay * ((px - bx * B) / ax) + by * B = py
        # ay * px / ax - ay * bx * B / ax + by * B = py
        # - ay * bx * B / ax + by * B = py - ay * px / ax
        # B * (- ay * bx / ax + by) = py - ay * px / ax
        # B = (py - ay * px / ax) / (- ay * bx / ax + by)
        B = ((ax * py - ay * px) // (-ay * bx + by * ax))
        A = ((px - bx * B) // ax)
        # print(A, B)
        # assert (A.is_integer() and B.is_integer()) == (int(A) * ax + int(B) * bx == px and int(A) * ay + int(B) * by == py), (A, B, ax, bx, px, py)
        # if A.is_integer() and B.is_integer():
            # ans += A * 3 + B
        if A * ax + B * bx == px and A * ay + B * by == py:
            ans += A * 3 + B

    print(ans)