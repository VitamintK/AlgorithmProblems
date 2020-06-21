from heapq import heappush, heappop

def prims(n, adj, must = None):
    """takes n, adjacency list `adj`, and optionally a (u,v,weight) edge `must`. 
    If `must` is given, start prim's with that edge and those two vertices already present.
    Returns the size of the MST (or a really really big number if impossible i.e. graph is disconnected)."""
    frontier = []
    vs = set()
    ans = 0
    def process_vertex(ve):
        for edge in adj[ve]:
            if edge[0] in vs:
                continue
            heappush(frontier, (edge[1], edge[0]))
        vs.add(ve)
    if must is not None:
        ans += must[2]
        process_vertex(must[0])
        process_vertex(must[1])
    else:
        process_vertex(0)
    while len(vs) < n:
        if len(frontier) == 0:
            return 100000000000000000
        w, u = heappop(frontier)
        if u in vs:
            continue
        ans += w
        process_vertex(u)
    return ans
    
def make_adj(n, edges):
    adj = [[] for i in range(n)]
    for edge in edges:
        u, v, w = edge
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj

def remove_edge(edges, i):
    return [edge for j, edge in enumerate(edges) if j!=i]

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # first, find the size of the MST
        adj = make_adj(n, edges)
        minimum = prims(n, adj)
        crit = []
        pseu = []
        print(minimum)
        # now, for each edge, check an MST which must use that edge, and check an MST that can't use that edge.
        # for each, if the size of the MST matches the size of the original MST, we know if the edge is critical and/or pseudocritical
        for i in range(len(edges)):
           # get size of MST that must use this edge. If as small as original, this edge is pseudocritical.
            if prims(n, adj, edges[i]) == minimum:
                pseu.append(i)
            # get size of MST on the graph that has this edge removed.  If it's not as small as original, this edge is critical.
            e = remove_edge(edges, i)
            adj_p = make_adj(n, e)
            if prims(n, adj_p) > minimum:
                crit.append(i)
        return [crit, list(set(pseu) - set(crit))]
