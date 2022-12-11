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

def make_operation(s):
    return lambda old: eval(s)

if True:
    ans = 0
    inps = []
    monkeys = []
    bigmod = 1
    while True:
        try:
            inp = input()
            if inp == '':
                continue
            inp = inp.split()
            if inp[0] == 'Monkey':
                items = get_ints(input())
                operation = input().split()
                operation = make_operation(' '.join(operation[-3:]))
                mod = get_ints(input())[0]
                bigmod *= mod
                nexts = (get_ints(input())[0], get_ints(input())[0])
                monkeys.append((items, operation, mod, nexts))
        except EOFError:
            break
    counts = defaultdict(int)
    for i in range(10000):
        print(i)
        for id, monkey in enumerate(monkeys):
            items, operation, mod, nexts = monkey
            for item in items:
                counts[id] += 1
                new_item = operation(item)
                # new_item //= 3 # part 1
                new_item %= bigmod # part 2
                if new_item%mod==0:
                    monkeys[nexts[0]][0].append(new_item)
                else:
                    monkeys[nexts[1]][0].append(new_item)
            items.clear()
    print(ans)
    counts = list(counts.values())
    counts.sort()
    print(counts[-1] * counts[-2])
else:
    pass