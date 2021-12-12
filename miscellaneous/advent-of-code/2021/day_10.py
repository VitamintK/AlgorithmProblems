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

a = '[{(<'
b = ']})>'
mp = dict()
score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
for x,y in zip(a,b):
    mp[x] = y
    mp[y] = x
if True:
    ans = []
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    for inp in inps:
        d = defaultdict(int)
        stk = []
        for x in inp:
            if x in '[{(<':
                stk.append(x)
            else:
                if stk[-1] == mp[x]:
                    stk.pop()
                else:
                    # ans += score[x]
                    break
        else:
            stk.reverse()
            s = 0
            for y in stk:
                x = mp[y]
                s *= 5
                if x == ')':
                    s += 1
                elif x==']':
                    s += 2
                elif x=='}':
                    s += 3
                else:
                    s += 4
            ans.append(s)
        # for x in inp:
        #     if x in '[{(<':
        #         d[x] += 1
        #     else:
        #         d[mp[x]] -=1
        #         if d[mp[x]] < 0:
        #             ans += score[x]
        #             break
    ans.sort()
    print(ans[len(ans)//2])
else:
    pass