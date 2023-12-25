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
# PART = 2
if PART == 1:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    R, C = len(inps), len(inps[0])
    edges = defaultdict(list)
    for inp in inps:
        x = inp.split(':')[0]
        ys = inp.split()[1:]
        for y in ys:
            edges[x].append(y)
            edges[y].append(x)
    import random

    def bfs(start, end, rm_edges):
        q = deque()
        q.append(start)
        been = {start}
        prev = dict()
        while q:
            u = q.popleft()
            if u == end:
                break
            for v in edges[u]:
                if v not in been and ((u, v) not in rm_edges) and ((v, u) not in rm_edges):
                    been.add(v)
                    prev[v] = u
                    q.append(v)
        if end not in been:
            return []
        path = []
        u = end
        while u != start:
            v = prev[u]
            path.append(u)
            u = v
        return path

    def dfs2(start, rm_edges, been):
        y = 1
        for x in edges[start]:
            if (start, x) in rm_edges or (x, start) in rm_edges:
                continue
            if x not in been:
                been.add(x)
                y += dfs2(x, rm_edges, been)
        return y

    while True:
        rm_edges = []
        u, v = random.sample(list(edges.keys()), 2)
        if u == v:
            continue
        if u in edges[v]:
            continue
        while len(rm_edges) < 3:
            path = bfs(u, v, rm_edges)
            # print(rm_edges, path)
            r = random.randint(1, len(path)-1)
            if (path[r-1], path[r]) in rm_edges or (path[r], path[r-1]) in rm_edges:
                continue
            rm_edges.append( (path[r-1], path[r]))
        sz = dfs2(u, rm_edges, {u})
        if sz != len(edges):
            print(sz, len(edges))
            print(sz * (len(edges) - sz))
            break
    
    # goddammit... I didn't have a min-cut python ready to go in python, so I tried to ask github copilot and chatgpt to write one for me
    # both of which failed terribly. Eventually just went with this BFS approach instead, which worked. But way too late to get on the leaderboard :(
    # and unfortunately that means I missed the overall leaderboard for this year :'(
    # I actually originally tried this approach immediately, but with a DFS instead of BFS, and it did not work :(
else:
    pass