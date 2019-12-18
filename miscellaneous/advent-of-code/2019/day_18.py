grid = []
if True:
    while True:
        try:
            grid.append(input())  
        except EOFError:
            break
else:
    pass
doors = dict()
keys = dict()
start = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            start = (i,j)
        elif 'a' <= grid[i][j] <= 'z':
            keys[grid[i][j]] = (i,j)
        elif 'A' <= grid[i][j] <= 'Z':
            doors[grid[i][j]] = (i,j)

from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
# >>> heap = []
# >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# >>> for item in data:
# ...     heappush(heap, item)
# heap[0] is the smallest item

ds = {'u': (-1, 0), 'r': (0, 1), 'd': (1, 0), 'l': (0, -1)}
keys['@'] = start
edges = {k:dict() for k in keys}
def bfs(k1, k2):
    q = deque()
    ex = set()
    q.append((keys[k1], 0, set()))
    while len(q) > 0:
        pos, d, needs = q.popleft()
        r, c = pos
        if grid[r][c] == '#':
            continue
        if grid[r][c] in doors:
            needs = needs.copy()
            needs.add(grid[r][c].lower())
        if grid[r][c] == k2:
            return d, needs
        for dr, dc in ds.values():
            nr, nc = r+dr, c+dc
            if (nr, nc) in ex:
                continue
            ex.add((nr, nc))
            q.append(((nr, nc), d+1, needs))

for k1 in keys:
    for k2 in keys:
        if k1 <= k2:
            continue
        a, needs = bfs(k1, k2)
        edges[k1][k2] = (a, needs)
        edges[k2][k1] = (a, needs)

explored = set()
pq = [(0, set('@'), '@')]
while len(pq) > 0:
    d, collected, cur = heappop(pq)
    print(d, collected, cur)
    if len(collected) == len(keys):
        print(d, collected, cur)
        break
    fr = frozenset(collected)
    if (fr, cur) in explored:
        continue
    explored.add((fr, cur))
    for k in keys:
        if k in collected:
            continue
        if len(edges[cur][k][1] - collected) > 0:
            # print("can't go to", k, "because it needs", edges[cur][k][1])
            continue
        c = collected.copy()
        c.add(k)
        if (frozenset(c), k) in explored:
            continue
        heappush(pq, (d + edges[cur][k][0], c, k))

