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
octdirs = ['E', 'SE', 'S', 'SW', 'W', 'NW', 'N', 'NE']
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)
def sign_of(x):
    if x==0:
        return 0
    return x/abs(x)

def print_grid(elves):
    for r in range(-5, 15):
        x = []
        for c in range(-5, 20):
            if (r,c) in elves:
                x.append('#')
            else:
                x.append('.')
        print(''.join(x))
    print('')

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    elves = []
    for r, inp in enumerate(inps):
        for c, x in enumerate(inp):
            if x=='#':
                elves.append((r,c))
    rules = [
        ('U', ['N', 'NE', 'NW']),
        ('D', ['S', 'SE', 'SW']),
        ('L', ['W', 'NW', 'SW']),
        ('R', ['E', 'NE', 'SE'])
    ]
    # for i in range(10):
    for i in range(1000000):
        print(i)
        any_movement = False
        proposals = defaultdict(int)
        new_elves = []
        for j, elf in enumerate(elves):
            elves_set = set(elves)
            r,c = elf
            any_neighbors = False
            for dr,dc in octs:
                nr,nc = r+dr, c+dc
                if (nr,nc) in elves_set:
                    any_neighbors = True
            if not any_neighbors:
                new_elves.append((r,c))
                continue
            for rule in rules:
                go, check = rule
                good = True
                for cc in check:
                    dr, dc = octs[octdirs.index(cc)]
                    nr, nc = r+dr, c+dc
                    if (nr, nc) in elves_set:
                        good = False
                if good:
                    dr,dc = dirs[directions.index(go)]
                    nr, nc = r+dr, c+dc
                    proposals[(nr,nc)] += 1
                    new_elves.append((nr,nc))
                    break
            else:
                assert not good
                new_elves.append((r,c))
        for j, elf in enumerate(elves):
            if proposals[new_elves[j]] > 1:
                new_elves[j] = elf
            if new_elves[j] != elf:
                any_movement = True
        if not any_movement:
            break
        elves = new_elves
        rules = rules[1:] + [rules[0]]
        # print(rules)
        # print_grid(elves)
    print(elves)
    # ans = (max(r for r,c in elves)+1 - min(r for r,c in elves)) * (max(c for r,c in elves)+1 - min(c for r,c in elves)) - len(elves)
    # print(max(r for r,c in elves)+1- min(r for r,c in elves), (max(c for r,c in elves)+1 - min(c for r,c in elves)))
    ans = i+1
    print(ans)
else:
    pass