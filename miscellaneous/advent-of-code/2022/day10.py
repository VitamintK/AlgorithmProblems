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
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    reg = 1
    effect = dict()
    cycle = 0
    pixels = []
    for i in range(len(inps)):
        inp = inps[i]
        if inp == 'noop':
            cycle %= 40
            cycle += 1
            if abs(cycle-1-reg) <= 1:
                pixels.append('#')
            else:
                pixels.append('.')
            # if cycle%40==20 and cycle>0:
            #     print(cycle, reg, cycle*reg)
            #     ans += cycle * reg
        else:
            _, x = inp.split()
            x = int(x)
            for j in range(2):
                cycle %= 40
                cycle += 1
                if abs(cycle-1-reg) <= 1:
                    pixels.append('#')
                else:
                    pixels.append('.')
                # if cycle%40==20 and cycle>0:
                #     print(cycle, reg, cycle*reg)
                #     ans += cycle * reg
            reg += x
    print(pixels)
    for i in range(6):
        print(''.join(pixels[40*i:40*i+40]))

    

    print(ans)
else:
    pass