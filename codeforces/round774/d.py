# oops, this approach was WRONG.
# I tried 2-coloring, but the correct solution was to find the max independent set which is 
# a simple tree DP.

import sys


n = int(input())
edges = [[] for i in range(n)]
for _ in range(n-1):
    u,v = map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
weights = [1 for i in range(n)]
sys.setrecursionlimit(200010)
ans = 0

dontchange = [0 for i in range(n)]
def set_leafneighbor_dfs(u, parent):
    global ans
    for v in edges[u]:
        if v==parent:
            continue
        is_leaf = set_leafneighbor_dfs(v,u)
        if is_leaf:
            dontchange[u] = 1
    if len(edges[u])==1:
        dontchange[u]=1
        ans += 1
    return len(edges[u])==1
set_leafneighbor_dfs(0, 0)
if len(edges[u])==1:
    dontchange[edges[u][0]]=1

change = []
for i in range(n):
    if dontchange[i]==0:
        change.append(i)

def get_colors(u, parent, color):
    coloring[u] = color
    colored.add(u)
    colors = [0,0]
    colors[color] += 1
    for v in edges[u]:
        if v==parent:
            continue
        if dontchange[v]:
            continue
        res = get_colors(v,u,1-color)
        colors[0]+=res[0]
        colors[1]+=res[1]
    return colors

coloring = dict()
colored = set()
for i in change:
    if i not in colored:
        coloring = dict()
        colors = get_colors(i, i, 0)
        ans += max(colors)
        if colors[0] > colors[1]:
            color = 0
        elif colors[1]>colors[0]:
            color = 1
        else:
            one = sum(len(edges[index]) for index in coloring if coloring[index]==1)
            zero = sum(len(edges[index]) for index in coloring if coloring[index]==0)
            if one < zero:
                color = 1
            else:
                color = 0 
        for index, c in coloring.items():
            if c!=color:
                continue
            weights[index] = len(edges[index])

print(ans, sum(weights))
print(' '.join(str(x) for x in weights))