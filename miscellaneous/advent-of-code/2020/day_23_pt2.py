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
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)



if True:
    ans = 0
    inps = []
    
    cups = [int(x) for x in '389125467']
    # cups = [int(x) for x in '871369452']

    cups = [x-1 for x in cups]
    for i in range(len(cups), 1000000):
        cups.append(i)
    nexts = [None for i in cups]
    prevs = [None for i in cups]
    for i in range(len(cups)):
        nexts[cups[i]] = cups[(i+1)%len(cups)]
        prevs[cups[i]] = cups[(i-1)%len(cups)]
    ITS = 10000000
    # ITS = 10
    cur = cups[0]
    for i in range(ITS):
        if i%100000 == 0:
            print(i)
        out = []
        n = cur
        for i in range(3):
            n = nexts[n]
            out.append(n)
        # print(out)
        dest = (cur-1)%len(cups)
        while dest in out:
            dest = (dest-1)%len(cups)

        nexts[cur] = nexts[out[-1]]
        # prevs[nexts[cur]] = cur

        temp = nexts[dest]
        nexts[dest] = out[0]
        # prevs[out[0]] = dest
        nexts[out[-1]] = temp
        # prevs[temp] = out[-1]
        cur = nexts[cur]
    # cups = [x+1 for x in cups]
    a, b = nexts[0]+1, nexts[nexts[0]]+1
    print(a,b)
    print((nexts[0]+1) * (nexts[nexts[0]]+1))
    # print(cups)
    print(ans)
else:
    pass