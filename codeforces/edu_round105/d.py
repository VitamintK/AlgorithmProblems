from collections import defaultdict
n = int(input())
leaves = []
for i in range(n):
    xs = [int(x) for x in input().split()]
    leaves.append(xs)
parent = dict()
children = defaultdict(list)

node_number = n
# def dfs(leaves, parent):
#     global node_number
#     node = node_number
#     node_number +=1
#     segmentation = defaultdict(list)
#     for leaf in leaves:
#         ...

dfs(leaves, None)