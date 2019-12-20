from collections import defaultdict, deque, Counter
import re
# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist") 
# # or re.search
# >>> m.group(0)       # The entire match
# 'Isaac Newton'
# >>> m.group(1)       # The first parenthesized subgroup.
# 'Isaac'
# >>> m.group(2)       # The second parenthesized subgroup.
# 'Newton'
# >>> m.group(1, 2)    # Multiple arguments give us a tuple.
# ('Isaac', 'Newton')
from heapq import heappush, heappop
# >>> heap = []
# >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# >>> for item in data:
# ...     heappush(heap, item)
# heap[0] is the smallest item
grid = []
if True:
    while True:
        try:
            grid.append(list(input()))
        except EOFError:
            break
else:
    pass

portals = dict()
portdict = {"AA": 0, "ZZ": 1}
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if 'A' <= grid[r][c] <= 'Z':
            portal = None
            if c>=1 and grid[r][c-1] == '.':
                portal = grid[r][c] + grid[r][c+1]
            elif c+1 < len(grid[r]) and grid[r][c+1] == '.':
                portal = grid[r][c-1] + grid[r][c]
            elif r - 1 >= 0 and grid[r-1][c] == '.':
                portal = grid[r][c] + grid[r+1][c]
            elif r+1 < len(grid) and grid[r+1][c] == '.':
                portal = grid[r-1][c] + grid[r][c]
            else:
                continue
            print(portal)
            if portal in portals:
                portals[portal].append((r,c))
            else:
                portals[portal] = [(r,c)]
                if portal not in portdict:
                    portdict[portal] = len(portdict)
            grid[r][c] = portdict[portal]

def is_outer(r, c):
    if r <= 4 or r >= len(grid)-5:
        return True
    if c <= 4 or c >= len(grid[r]) -5:
        return True
    return False

invdict = dict()
for k in portals:
    for v in portals[k]:
        invdict[v] = k

ds = {'u': (-1, 0), 'r': (0, 1), 'd': (1, 0), 'l': (0, -1)}

# q = deque()
q = []
heappush(q, (0, portals["AA"][0], 0))
exp = set()
for r in grid:
    print(r)
while len(q) > 0:
    ex = heappop(q)
    d, pos, l = ex
    print(pos, d, l)
    r, c = pos
    exp.add((pos, l))
    for dr, dc in ds.values():
        nr, nc = r + dr, c + dc
        if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[nr]):
            pass
        else:
            continue
        if grid[nr][nc] in [' ', '#']:
            continue
        if type(grid[nr][nc]) is int:
            if grid[nr][nc] == 0:
                continue
            if grid[nr][nc] == 1:
                if l == 0:
                    print(d - 1)
                    exit()
                else:
                    continue
            portlocs = portals[invdict[(nr, nc)]] 
            if is_outer(nr, nc):
                if l == 0:
                    continue
                goto = portlocs[portlocs.index((nr, nc)) - 1]
                if (goto, l-1) in exp:
                    continue
                q.append((d, goto, l-1))
            else:
                goto = portlocs[portlocs.index((nr, nc)) - 1]
                if (goto, l+1) in exp:
                    continue
                q.append((d, goto, l+1))
        if ((nr, nc), l) in exp:
            continue
        q.append((d+1, (nr, nc), l))



