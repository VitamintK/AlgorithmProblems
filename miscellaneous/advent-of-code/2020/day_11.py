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
import string
# string.ascii_lowercase == 'abcde...'
# string.ascii_uppercase == 'ABCDE...'

import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

def ser(g):
    return ''.join(''.join(l) for l in g)
def get_next(g):
    n = len(g)
    m = len(g[0])
    nxt = [[i for i in r] for r in g]
    for r in range(len(g)):
        for c in range(len(g[0])):
            # print(r,c)
            cn = 0
            if g[r][c] == '.':
                continue
            for dr, dc in octs:
                for i in range(1,1000):
                    nr, nc = r+dr*i, c+dc*i
                    if not is_grid_valid(n,m,nr,nc):
                        break
                    if g[nr][nc] == '#':
                        cn +=1
                        break
                    elif g[nr][nc] == 'L':
                        break
            # print(c)
            if g[r][c] == '#':
                if cn >= 5:
                    nxt[r][c] = 'L'
            elif g[r][c] == 'L':
                if cn == 0:
                    nxt[r][c] = '#'
    return nxt
                    

if True:
    ans = 0
    g = []
    while True:
        try:
            g.append(list(input()))
        except EOFError:
            break
    
    while True:
        ng = get_next(g)
        if ser(ng) == ser(g):
            break
        g = ng
    print(sum(r.count('#') for r in g))
    # print(ans)
else:
    pass