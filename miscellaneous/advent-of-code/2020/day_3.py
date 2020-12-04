from collections import defaultdict, deque, Counter
# d = deque()
# d.append(5)
# x = d.popleft()
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
import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

if False:
    ans = 0
    grid = []
    i = 0
    while True:
        try:
            a = input()
            # grid.append(a)
            if a[i%len(a)] == '#':
                ans +=1
                # print(a)
            i += 3
        except EOFError:
            break
    
    print(ans)
else:
    grid = []
    while True:
        try:
            a = input()
            grid.append(a)
        except EOFError:
            break
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    anss = 1
    for dx,dy in slopes:
        c = 0
        ans = 0
        for i,row in enumerate(grid):
            if i%dy != 0:
                continue
            if row[c%len(row)] == '#':
                ans += 1
            c += dx
        anss *= ans

   
    
    print(anss)