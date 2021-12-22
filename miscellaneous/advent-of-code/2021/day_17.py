# from collections import defaultdict, deque, Counter
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
    targx = (144,179)
    targy = (-100, -75)
    # targy = -76
    # targx = 144
    # for i in range(19):
    trianglecache = set()
    t = 1
    for i in range(2, 1000000):
        t += i
        trianglecache.add(t)
    def istriangle(x):
        return x in trianglecache
    anss = set()
    def f(yvel):
        # yv = yvel
        # xv = 18
        y = 0
        x = 0
        ans = 0
        # for i in range(18):
        times = yvel
        ans = (times * (times + 1)) // 2
        for d in range(targy[0], targy[1]):
            dist = -d + ans
            if istriangle(dist):
                print(ans)
                anss.add((17,yvel))
                anss.add((18,yvel))
        # while y >= targy[0] and x < targx[1]:
        #     # print(x, y, xv, yv)
        #     y += yv
        #     x += xv
        #     if xv > 0:
        #         xv -= 1
        #     yv -= 1
        #     ans = max(ans, y)
        
        # print(x, y)
    for xvel in range(17,200):
        for yvel in range(-100,100):
            x,y = 0,0
            xv, yv = xvel, yvel
            while y >= targy[0] and x < targx[1]:
                y += yv
                x += xv
                if xv > 0:
                    xv -= 1
                elif xv < 0:
                    xv += 1
                yv -= 1
                if x in range(*targx) and y in range(*targy):
                    anss.add((xvel, yvel))
            print(x, y, xvel, yvel)
            
    for i in range(18,10000):
        f(i)
    print(len(anss))



else:
    pass