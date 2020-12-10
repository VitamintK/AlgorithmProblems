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

def f(l, x):
    for i in l:
        if x-i in l:
            return True
    return False

if True:
    ans = 0
    pre = 25
    ins = []
    while True:
        try:
            i = int(input())
            ins.append(i)
        except EOFError:
            break
    for i in range(pre, len(ins)):
        if not f(ins[i-pre:i], ins[i]):
            y = (ins[i])
            break
    
    print(y)
    pres = [0]
    for i in ins:
        pres.append(pres[-1]+i)
        if pres[-1]-y in pres:
            # print(pres)
            yy = pres[-1]-y
            a,b = ins.index(i), pres.index(yy)
            a,b = min(a,b), max(a,b)
            print(a,b)
            rng = ins[a:b]
            print(max(rng)+min(rng) )
            break 
        
else:
    pass