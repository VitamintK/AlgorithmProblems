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
x = 4
y = 9
# x,y=3,7

dice = 0
if False:
    ans = 0
    # inps = []
    # while True:
    #     try:
    #         inps.append(input())
    #     except EOFError:
    #         break
    p1 = 0
    p2 = 0
    p = 0
    count = 0
    while True:
        roll = 0
        for i in range(3):
            roll += 1+dice
            count += 1
            dice = (dice+1)%100
        if p==0:
            x = (x+roll)%10
            p1 += x+1
        else:
            y = (y+roll)%10
            p2 += y+1
        p = 1-p
        if p1 >= 1000 or p2 >= 1000:
            print(min(p1,p2) * count)
            break
            

    print(ans)
else:
    rolls = defaultdict(int)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                rolls[i+j+k+3] += 1
    print(rolls)
    @lru_cache(maxsize=None)
    def dfs(x,y,xscore,yscore,turn):
        if xscore >= 100:
            return 1,0
        if yscore >= 100:
            return 0,1
        a,b = 0,0
        for roll in rolls:
            if turn==0:
                newpos = (x+roll)%10
                aa,bb = dfs(newpos, y, xscore+newpos+1, yscore, 1-turn)
                a+=aa*rolls[roll]
                b+=bb*rolls[roll]
            else:
                newpos = (y+roll)%10 
                aa,bb = dfs(x, newpos, xscore, yscore+newpos+1, 1-turn)
                a+=aa*rolls[roll]
                b+=bb*rolls[roll]
        return a,b
    # print(x,y)
    a,b=dfs(x,y,0,0,0)
    print(max(a,b))