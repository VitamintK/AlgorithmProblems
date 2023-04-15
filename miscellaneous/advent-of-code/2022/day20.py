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
from functools import lru_cache
# @lru_cache(maxsize=None)

import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
directions = 'RDLU'
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)
def sign_of(x):
    if x==0:
        return 0
    return x/abs(x)

if True:
    key = 811589153
    ans = 0
    inps = []
    i = 0
    while True:
        try:
            inps.append((int(input()) * key, 0, i))
            i += 1
        except EOFError:
            break
    n = len(inps)
    i = 0
    for _ in range(10):
        print([inp[0] for inp in inps])
        inps = [(x,0,z) for x,y,z in inps]
        for idx in range(n):
            for i in range(n):
                if inps[i][2] == idx:
                    break
            x,y,idx = inps[i]
            # if y == 1:
            #     continue
            assert y == 0
            # adjustment = 1 if x >= 0 else 0
            
            inps.pop(i)
            spot = (i + x)%(n-1)
            # if x < 0 and spot==0:
            #     spot = n
            inps = inps[:spot] + [(x,1,idx)] + inps[spot:]
            if i < spot:
                pass
            else:
                i += 1
            # print([inp[0] for inp in inps])
    inps = [inp[0] for inp in inps]
    print(inps)
    z = inps.index(0)
    ans = inps[(z+1000)%n] + inps[(z+2000)%n] + inps[(z+3000)%n]
    print(ans)
else:
    pass