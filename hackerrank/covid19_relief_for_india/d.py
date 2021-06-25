# pretty interesting problem.  I'm surprised my solution works: I thought it might time out on a star graph.
# problem: given a tree, remove up to `k` leaves, one at a time.  Minimize the diameter of the resulting tree.

# my solution: binary search for the answer: given a diameter `d`, can we prune `k` leaves from the tree to make a tree with that diameter?
# For each check, I try rooting the tree at each of the `n` possible nodes.  Then I check what the size of the tree is if we truncate the
# tree at height `d/2`.  If `d` is odd, I check all possible branches from the root and allow 1 of them to be `d//2 + 1`.

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'treeCut' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. 2D_INTEGER_ARRAY edges
#

# def get_farthest(nodes, edges, seen, node):
#     seen.add(node)
#     ans_node = node
#     ans_distance = 0
#     for n in edges[node]:
#         if n in nodes and n not in seen:
#             f,d = get_farthest(nodes, edges, seen, n)
#             d += 1
#             if d > ans_distance:
#                 ans_distance = d
#                 ans_node = f
#     return ans_node, ans_distance    
    
def dfs(n, edges, maxheight, node, parent, heightsofar):
    if heightsofar == maxheight:
        return 0
    ans = 0
    for v in edges[node]:
        if v != parent:
            ans += dfs(n,edges,maxheight,v,node,heightsofar+1) + 1
    return ans
    
def can(n,k,edges,max_diam):
    ans = 0
    for root in range(n):
        if max_diam%2 == 0:
            ans = max(ans, 1+dfs(n,edges,max_diam//2, root, root, 0))
        else:
            max_diff_for_one_more = -1
            subans = 0
            for subroot in edges[root]:
                nodes_for_small = 1 + dfs(n,edges,max_diam//2, subroot, root, 1) if max_diam//2 > 0 else 0
                nodes_for_large = 1 + dfs(n,edges,1+max_diam//2, subroot, root, 1)
                max_diff_for_one_more = max(max_diff_for_one_more, nodes_for_large - nodes_for_small)
                subans += nodes_for_small
            ans = max(ans, 1+subans + max_diff_for_one_more)
            print('ans', ans, subans)
    print('we want a max diam of', max_diam, ', we can keep', ans, 'nodes')   
    print(ans >= n-k)
    return ans >= n-k
    
def treeCut(n, k, edges):
    # Write your code here
    edge_list = [[] for i in range(n)]
    for u,v in edges:
        u-=1
        v-=1
        edge_list[u].append(v)
        edge_list[v].append(u)
    edges = edge_list
    nodes = set(range(n))
    lo = -1
    hi = n
    while hi-lo > 1:
        mid = ((lo+hi)+1)//2
        if can(n, k, edges, mid):
            hi = mid
        else:
            lo = mid
    return hi
        # init = next(iter(nodes))
        # farthest, dist = get_farthest(nodes, edges,set(), init)
        # farthest, dist = get_farthest(nodes, edges,set(), farthest)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    edges_rows = int(input().strip())
    edges_columns = int(input().strip())

    edges = []

    for _ in range(edges_rows):
        edges.append(list(map(int, input().rstrip().split())))

    result = treeCut(n, k, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
