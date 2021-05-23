#!/bin/python3

# FOR SOME REASON, THIS SEGFAULTS ON A SPECIFIC TESTCASE?
# MAYBE RECURSION USES TOO MUCH MEMORY OF THE STACK??
# TRANSLATING TO C++ INSTEAD

import math
import os
import random
import re
import sys



#
# Complete the 'findMinimumPathLength' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER_ARRAY visitNodes
#
sys.setrecursionlimit(112345)

def dfs(start, edges, visitNodes, visited):
    tot_dist = 0
    visited.add(start)
    for v in edges[start]:
        if v not in visited:
            relevant_distance = dfs(v, edges, visitNodes, visited)
            if relevant_distance > 0 or v in visitNodes:
                tot_dist += relevant_distance + 1
    return tot_dist

def findMinimumPathLength(n, edges, visitNodes):
    # Write your code here
    ed = [[] for i in range(n)]
    visitNodes = {v-1 for v in visitNodes}
    for u,v in edges:
        ed[u-1].append(v-1)
        ed[v-1].append(u-1)
    straight = dfs(0, ed, {n-1}, set())
    al = dfs(0,ed,visitNodes|{n-1}, set())
    return straight + (al-straight)*2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    edges_rows = int(input().strip())
    edges_columns = int(input().strip())

    edges = []

    for _ in range(edges_rows):
        edges.append(list(map(int, input().rstrip().split())))

    visitNodes_count = int(input().strip())

    visitNodes = []

    for _ in range(visitNodes_count):
        visitNodes_item = int(input().strip())
        visitNodes.append(visitNodes_item)

    result = findMinimumPathLength(n, edges, visitNodes)

    fptr.write(str(result) + '\n')

    fptr.close()