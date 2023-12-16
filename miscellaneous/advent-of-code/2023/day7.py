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

def convert(hand):
    hand = list(hand)
    for i in range(len(hand)):
        if hand[i] == 'T':
            hand[i] = 10
        elif hand[i] == 'J':
            hand[i] = 0 # 11 in part 1
        elif hand[i] == 'Q':
            hand[i] = 12
        elif hand[i] == 'K':
            hand[i] = 13
        elif hand[i] == 'A':
            hand[i] = 14
        else:
            hand[i] = int(hand[i])
    # hand.sort(reverse=True)
    return hand

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    hands = []
    for inp in inps:
        hand, bid = inp.split()
        hand = convert(hand)
        bid = int(bid)
        c = Counter(hand)
        if 0 in c:
            # This whole conditional is for part 2 only
            most_common = c.most_common()
            if most_common[0][0] == 0:
                if len(most_common) == 1:
                    mc = most_common[0][0]
                else:
                    mc = most_common[1][0]
                    c[mc] += c[0]
                    c[0] = 0
            else:
                mc = most_common[0][0]
                c[mc] += c[0]
                c[0] = 0
        
        c = list(c.values())
        if 5 in c:
            hands.append((6, hand, bid))
        elif 4 in c:
            hands.append((5, hand, bid))
        elif 3 in c and 2 in c:
            hands.append((4, hand, bid))
        elif 3 in c:
            hands.append((3, hand, bid))
        elif 2 in c and c.count(2) == 2:
            hands.append((2, hand, bid))
        elif 2 in c:
            hands.append((1, hand, bid))
        else:
            hands.append((0, hand, bid))
    
    hands.sort(reverse=True)
    for i in range(len(hands)):
        x = len(hands) - i
        ans += x * hands[i][2]

    print(ans)
else:
    pass