N = int(input())
edges = [[] for i in range(N)]
for i in range(N-1):
    u, v = map(int, input().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)
root = int(input()) - 1
#stack = []
#stack.append(root)
parents = [None]*N
#while(len(stack) > 0):
#    v = stack.pop()
#    for u in edges[v]:
#        if u != parents[v]:
#            stack.append(u)
#            parents[u] = v
ds = [None]*N
def dfs(start):
    mdepth = 0
    n1 = 0
    n2 = 0
    best_child = 0
    for neighbor in edges[start]:
        if neighbor != parents[start]:
            parents[neighbor] = start
            d, m = dfs(neighbor)
            #print(start+1, neighbor+1, d, m)
            if m+1 > n1:
                n2 = n1
                n1 = m+1
            elif m+1 > n2:
                n2 = m+1
            best_child = max(best_child, d)
    #if(start+1 == 2):
    #    print(best_child)
    diameter = max(n1+n2, best_child)
    mdepth = max(n1, n2)
    ds[start] = diameter
    return diameter, mdepth
dfs(root)
Q = int(input())
for q in range(Q):
    qq = int(input())
    print(ds[qq-1])
