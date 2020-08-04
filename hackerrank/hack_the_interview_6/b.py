#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'maxSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. 2D_INTEGER_ARRAY edges
#

# def maxSum(N, edges):
#     # Write your code here
#     dfs(edges)

    
    

N, M = map(int, input().split())
edges = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)
distances = [None for i in range(N)]
q = deque([(0, 0)])
while len(q) > 0:
    ex, d = q.popleft()
    if distances[ex] is not None:
        continue
    distances[ex] = d
    for e in edges[ex]:
        if distances[e] is None:
            q.append((e, d+1))
# print(distances)
high = distances[-1]
ans = 0
for d in reversed(distances):
    g = min(high, d)
    ans += g
    high = g
print(ans)