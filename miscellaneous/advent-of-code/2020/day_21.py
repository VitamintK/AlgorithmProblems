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
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    
    lines = []
    all_to_line = defaultdict(list)
    all_all = set()
    for inp in inps:
        a, b = inp.split('(')
        b = [x.strip() for x in b.split('contains')[1][:-1].split(',')]
        a = a.split()
        all_all |= set(a)
        lines.append((a, b))
        for allerg in b:
            all_to_line[allerg].append(len(lines)-1)
    could_be = set()
    candss = []
    for allerg in all_to_line:
        cands = set(all_all)
        for line in all_to_line[allerg]:
            line = lines[line]
            cands &= set(line[0])
        print(allerg, cands)
        candss.append((allerg, cands))
        could_be |= cands
    cant_be = all_all - could_be
    print(all_all, could_be, cant_be)
    for line in lines:
        a, b = line
        for allerg in a:
            if allerg in cant_be:
                ans +=1
    for i in range(100):
        for cands in candss:
            ing, algs = cands
            if len(algs) == 1:
                delet = list(algs)[0]
                for cands2 in candss:
                    ing2, algs2 = cands2
                    if ing2 == ing:
                        continue
                    algs2.discard(delet)
    print(candss)
    # for c in candss:
    candss = [(x,list(y)[0]) for x,y in candss]
    candss.sort()
    print(','.join(y for x,y in candss))
    print(ans)
else:
    pass