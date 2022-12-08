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
    stack = []
    i = 0
    sizes = defaultdict(int)
    seen = set()
    while i < len(inps):
        inp = inps[i]
        inp = inp.split()
        assert inp[0] == '$'
        if inp[1] == 'cd':
            if inp[2] == '..':
                stack.pop()
            elif inp[2] == '/':
                stack = ['']
            else:
                stack.append(stack[-1] + '/' + inp[2])
        elif inp[1] == 'ls':
            key = '/'.join(stack)
            new = key not in seen
            while i+1 < len(inps) and inps[i+1][0] != '$':
                i += 1
                x,y = inps[i].split()
                if x=='dir':
                    pass
                else:
                    if new:
                        size = int(x)
                        for d in stack:
                            sizes[d] += size
            seen.add(key)
        else:
            assert False
        i += 1
    total_size = sizes['']
    min_size = total_size - (70000000-30000000)
    best = 70000000 
    for d in sizes:
        # if sizes[d] <= 100000:
        if sizes[d] >= min_size:
            best = min(best, sizes[d])
            # ans += sizes[d]
    print(best)
        

    

    print(ans)
else:
    pass