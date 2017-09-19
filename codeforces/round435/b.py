n = int(input())
edges = [[] for i in range(n)]
for i in range(n-1):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

colors = [-1 for i in range(n)]
dfs = [(0,0)]
while len(dfs) > 0:
    node, color = dfs.pop()
    colors[node] = color
    for neighbor in edges[node]:
        if colors[neighbor] == -1:
            dfs.append((neighbor, 1-color))

blue = len([x for x in colors if x==0])
red = n - blue

total_graph_edges = blue*red
print(blue*red - (n-1))