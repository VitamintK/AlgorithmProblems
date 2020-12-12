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

if True:
    # PART 1
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    
    dind = 1
    x,y = 0,0
    for i in inps:
        j = i[0]
        amt = int(i[1:])
        if j == 'N':
            y+=amt
        elif j =='S':
            y-=amt
        elif j=='W':
            x-=amt
        elif j=='E':
            x+=amt
        elif j=='L':
            deg = amt//90
            dind = (dind-deg)%len(dirs)
        elif j =='R':
            deg = amt//90
            dind = (dind+deg)%len(dirs)
        elif j=='F':
            dx,dy = dirs[dind]
            x += dx*amt
            y+= dy*amt
    print(x,y,abs(x)+abs(y))
    print(ans)
else:
    # PART 2
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    
    dind = 1
    x,y = 0,0
    tx, ty = 10,1
    for i in inps:
        j = i[0]
        amt = int(i[1:])
        if j == 'N':
            ty+=amt
        elif j =='S':
            ty-=amt
        elif j=='W':
            tx-=amt
        elif j=='E':
            tx+=amt
        elif j=='L':
            deg = amt//90
            for _ in range(deg):
                tx, ty = -ty, tx
        elif j =='R':
            deg = amt//90
            for _ in range(deg):
                tx, ty = ty, -tx
        elif j=='F':
            
            x += tx*amt
            y+= ty*amt
    print(x,y,abs(x)+abs(y))
    print(ans)
    