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
import numpy as np
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
    pattern = []
    patterns = [pattern]
    while True:
        try:
            x = input()
            if x.strip() == '':
                pattern = []
                patterns.append(pattern)
            else:
                pattern.append(list(x))
        except EOFError:
            break
    if patterns[-1] == []:
        patterns.pop()
    for og_pattern in patterns:
        # print(pattern)
        pattern = np.array(og_pattern)
        for r in range(1, len(pattern)):
            good = True
            for rr in range(r):
                mirror = r + r - rr - 1
                if mirror >= len(pattern):
                    continue
                if list(pattern[rr]) != list(pattern[mirror]):
                    good = False
            if good:
                # print(list(pattern[rr]), list(pattern[mirror]))
                # ans += r * 100
                # print('r', r)
                line = ('r', r)
                break
        for c in range(1, len(pattern[0])):
            good = True
            for cc in range(c):
                mirror = c + c - cc - 1
                if mirror >= len(pattern[0]):
                    continue
                # print(pattern, cc, mirror, pattern[:])
                if list(pattern[:, cc]) != list(pattern[:, mirror]):
                    good = False
            if good:
                # ans += c
                # print('c', c)
                line = ('c', c)
                break
        found = False
        for R in range(len(og_pattern)):
            if found:
                break
            for C in range(len(og_pattern[0])):
                if found:
                    break
                pattern = np.array(og_pattern)
                pattern[R][C] = {'#': '.', '.': '#'}[pattern[R][C]]
                for r in range(1, len(pattern)):
                    good = True
                    for rr in range(r):
                        mirror = r + r - rr - 1
                        if mirror >= len(pattern):
                            continue
                        if list(pattern[rr]) != list(pattern[mirror]):
                            good = False
                    if good and ('r', r) != line:
                        # print(list(pattern[rr]), list(pattern[mirror]))
                        ans += r * 100
                        print('r', r)
                        found = True
                        break
                for c in range(1, len(pattern[0])):
                    good = True
                    for cc in range(c):
                        mirror = c + c - cc - 1
                        if mirror >= len(pattern[0]):
                            continue
                        # print(pattern, cc, mirror, pattern[:])
                        if list(pattern[:, cc]) != list(pattern[:, mirror]):
                            good = False
                    if good and ('c', c) != line:
                        ans += c
                        print('c', c)
                        found = True
                        break
            
    raise ValueError(ans)
    print(ans)
else:
    pass