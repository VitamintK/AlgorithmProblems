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
            grid.append([0 if x=='.' else 1 for x in input()])
        except EOFError:
            break
else:
    pass

ds = {'u': (-1, 0), 'r': (0, 1), 'd': (1, 0), 'l': (0, -1)}
seen = set()
while True:
    if str(grid) in seen:
        break
    seen.add(str(grid))
    newgrid = [[i for i in r] for r in grid]
    for r in range(len(newgrid)):
        for c in range(len(newgrid[r])):
            neighbs = 0
            for dr, dc in ds.values():
                nr, nc = r+dr, c+dc
                if nr<0 or nr>=len(grid) or nc<0 or nc>=len(grid[0]):
                    continue
                neighbs += grid[nr][nc]
            if grid[r][c] and neighbs!=1:
                newgrid[r][c] = 0
            if grid[r][c] == 0 and neighbs in [1,2]:
                newgrid[r][c] = 1
    grid = newgrid

x = 0
ans = 0
for i in range(len(newgrid)):
    for j in range(len(newgrid[0])):
        ans += grid[i][j] * pow(2, x)
        x += 1
print(ans)