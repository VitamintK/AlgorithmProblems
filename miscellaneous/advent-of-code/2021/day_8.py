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
    outs = []
    for inp in inps:
        # out = inp.split('|')[1].strip().split()
        out = inp.split('|')
        out = out[0].split() + out[1].split()
        nd = defaultdict(set)
        outdict = dict()
        for o in out:
            o = ''.join(sorted(list(o)))
            if len(o) == 2:
                outdict[1] = o
            elif len(o) == 3:
                outdict[7] = o
            elif len(o) == 4:
                outdict[4] = o
            elif len(o) == 7:
                outdict[8] = o
            else:
                nd[len(o)].add(o)
        # print(nd[5])
        for x in nd[5]:
            if len(set(x) & set(outdict[1])) == 2:
                outdict[3] = x
            elif len(set(x) & set(outdict[4])) == 2:
                outdict[2] = x
            else:
                outdict[5] = x
        
        for x in nd[6]:
            if len(set(x) & set(outdict[5])) != 5:
                outdict[0] = x
            elif len(set(x) & set(outdict[1])) == 2:
                outdict[9] = x
            else:
                outdict[6] = x
        # print(nd[6])
        # a,b = nd[6]
        # if len(set(a) & set(outdict[1])) == 2:
        #     a,b = b,a
        # outdict[6] = a
        # outdict[9] = b
        

        inv = dict()
        for k,v in outdict.items():
            inv[v] = str(k)
        realout = inp.split('|')[1].strip().split()
        x = ''
        for i in realout:
            i = ''.join(sorted(list(i)))
            x += inv[i]
        ans += int(x)

            # if len(o) in [2,3,7,4]:
            #     ans +=1
            # if len(o) == 2:
            #     nd[
                

    print(ans)
else:
    pass