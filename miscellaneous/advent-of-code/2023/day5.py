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

if False:
    ans = 0
    seeds = get_ints(input())
    next_seeds = seeds[:]
    inps = []
    maps = []

    while True:
        try:
            i = input()
            if i.strip() == '':
                seeds = next_seeds
                next_seeds = seeds[:]
                continue
                
            if i.split()[-1] == 'map:':
                continue
            d, s, l = get_ints(i)
            for j, seed in enumerate(seeds):
                if s <= seed < s+l:
                    next_seeds[j] = d + seed-s
        except EOFError:
            break
    
    print(min(seeds))
else:
    pass
    ans = 0
    seeds = get_ints(input())
    ranges = []
    for i in range(0, len(seeds), 2):
        ranges.append((seeds[i], seeds[i] + seeds[i+1]-1))
    next_ranges = []
    while True:
        try:
            i = input()
            print(ranges, next_ranges)
            print(i)
            if i.strip() == '':
                ranges += next_ranges
                next_ranges = []
                continue
            if i.split()[-1] == 'map:':
                continue
            d, s, l = get_ints(i)
            temp_ranges = []
            for j, (left, right) in enumerate(ranges):
                if right < s or left >= s+l:
                    temp_ranges.append((left, right))
                    continue
                source_start = max(left, s)
                source_end = min(right, s+l-1)
                next_ranges.append((d + source_start-s, d + source_end-s))
                if source_start > left:
                    temp_ranges.append((left, source_start-1))
                if source_end < right:
                    temp_ranges.append((source_end+1, right))
            ranges = temp_ranges
        except EOFError:
            break
    

    print(min(ranges))