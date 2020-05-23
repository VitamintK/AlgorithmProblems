# solution for the easy test set:
# BFS from source to node A (on the subset of the graph that does not include B...Z)
# the edges along this path -- assign length 1.  Let's say size of path is X
# BFS again from source to node B (on subset of graph that does not include C..Z)... etc.
# all edges are length 1 except the very last edge, which is set to an amount that causes B > A
#
# UNFINISHED
from collections import deque
T = int(input())

DEBUG = 0
def debug(*args):
    if DEBUG:
        print(*args)

# dmap = {'W': (-1,0), 'E': (1,0), 'N': (0,1), 'S':(0,-1)}
for t in range(T):
    C, D = map(int, input().split())
    cs = [int(x) for x in input().split()]
    edges = [[] for i in range(C+1)]
    edge_map = []
    edges[0] = None # let's index starting from 1
    for d in range(D):
        u, v = map(int, input().split())
        edge_map.append((u,v))
        edges[u].append(v)
        edges[v].append(u)
    edge_lengths = [[i for i in range(C+1)] for j in range(C+1)]
    cs_sorted = [(-num, i+2) for i,num in enumerate(cs)]
    cs_sorted.sort()
    for order, c in cs_sorted:
        pre = [None for i in range(C+1)]
        q = deque([(1,)])
        # (node_number, traverse_cost_to_get_there, )
        while len(q) > 0:
            ex = q.popleft()
            (nodenum,) = ex
            if nodenum == c:
                break
            for v in edges[nodenum]:
                if cs[v-2] >= cs[c-2]:
                    continue
                if pre[v] is not None:
                    continue
                pre[v] = nodenum
                q.append((v,))
        print(pre)
        print(c)
        v = pre[c]
        existing = 0
        while v != 1:
            el = edge_lengths[pre[v]][v]
            if el is None:
                edge_lengths[pre[v]][v] = 1
                edge_lengths[v][pre[v]] = 1
                el = 1
            existing += el
            v = pre[v]
        needs = order - existing
        assert(needs > 0)
        edge_lengths[c][pre[c]] = needs
        edge_lengths[pre[c]][c] = needs

    ans = []
    for i in range(D):
        u, v = edge_map[i]
        ans.append(edge_lengths[u][v])
    print("Case #{}: {}".format(t+1, ' '.join(str(x) for x in ans)))