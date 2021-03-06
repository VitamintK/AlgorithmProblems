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

def get_addrs(addr, mask):
    addrs = set([addr])
    n=1
    for i, v in enumerate(reversed(mask)):
        if v =='X':
            newaddrs = set()
            for a in addrs:
                newaddrs.add(a)
                newaddrs.add(a^n)
            addrs = newaddrs
        elif v=='0':
            pass
        else:
            newaddrs = set()
            for a in addrs:
                newaddrs.add(a|n)
            addrs = newaddrs
        n*=2
    return addrs

def apply_mask(vals, addr, mask, val):
    # print(num, mask)
    addrs = get_addrs(addr,mask)
    for a in addrs:
        vals[a] = val

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    vals = dict()
    mask = None
    for inp in inps:
        x, y = inp.split('=')
        x = x.strip()
        y = y.strip()
        if x == 'mask':
            mask = y
        else:
            addr = get_ints(x)[0]
            apply_mask(vals, addr, mask, int(y))
    # print(vals)
    print(sum(vals.values()))
    print(ans)
else:
    pass