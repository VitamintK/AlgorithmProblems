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

def play_game(p1, p2):
    # print('playing a new game with: {}, {}'.format(p1, p2))
    visited = set()
    while len(p1) > 0 and len(p2) > 0:
        if str(p1)+str(p2) in visited:
            return True, p1
        visited.add(str(p1)+str(p2))
        x, y = p1.pop(), p2.pop()
        if x <= len(p1) and y<= len(p2):
            p1win, cards = play_game(p1[-x:], p2[-y:])
        else:
            p1win = x > y
        if p1win:
            p1 = [y] + [x] + p1
        else:
            p2 = [x] + [y] + p2
    if len(p1) == 0:
        return False, p2
    else:
        return True, p1

if True:
    ans = 0
    inps = []
    cards =[[], []]
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    p = 0
    for i in inps:
        if i.strip() == '':
            continue
        if i.strip() == 'Player 1:':
            continue
        if i.strip() == 'Player 2:':
            p = 1
            continue
        cards[p].append(int(i))
    cards[0].reverse()
    cards[1].reverse()


    p1win, cards = play_game(cards[0], cards[1])
    for i,x in enumerate(cards):
        ans += (i+1)*x
    print(ans)
else:
    pass