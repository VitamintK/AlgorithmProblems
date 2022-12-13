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

def cmp(l,r):
    # 0 for =
    # 1 for l<r
    # -1 for l>r
    if type(l) != type(r):
        if type(l)==int:
            l = [l]
        else:
            r = [r]
    if type(l)==int and type(r)==int:
        if l==r:
            return 0
        elif l < r:
            return 1
        else:
            return -1
    elif type(l)==list and type(r)==list:
        n,m = len(l), len(r)
        for i in range(min(n,m)):
            res = cmp(l[i], r[i])
            if res==-1:
                return -1
            elif res==1:
                return 1
            else:
                continue
        if n==m:
            return 0
        elif n<m:
            return 1
        else:
            return -1

class C:
    def __init__(self, x):
        self.x = x
    def __lt__(self, r):
        res = cmp(self.x, r.x)
        return res==1

        

if True:
    ans = 0
    pairs = []
    alls = []
    i = 1
    while True:
        try:
            x = eval(input())
            y = eval(input())
            pairs.append((x,y))
            alls.append(x)
            alls.append(y)
            if cmp(x,y) == 1:
                ans += i
            input()
            i += 1
        except EOFError:
            break

    print(ans)
    alls.append([[2]])
    alls.append([[6]])
    alls = [C(x) for x in alls]
    alls.sort()
    ans = 1
    for i in range(len(alls)):
        if str(alls[i].x) in ['[[2]]', '[[6]]']:
            ans *= (i+1)
    

    print(ans)
else:
    pass