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

@lru_cache(maxsize=None)
def get_nums(a,b, k):
    # how many new nums, dont count original a and b
    if a+b not in edges or k==0:
        return dict()
    mid = edges[a+b]
    sub = get_nums(a,mid,k-1)
    sub2 = get_nums(mid,b, k-1)
    ans = defaultdict(int)
    for k,v in sub.items():
        ans[k] += v
    for k,v in sub2.items():
        ans[k] += v
    ans[mid] += 1
    return ans


if True:
    ans = 0
    inps = []
    s = input()
    input()
    edges = dict()
    while True:
        try:
            u,v = input().split(' -> ')
            edges[u] = v
        except EOFError:
            break
    c = Counter(s)
    for i in range(1, len(s)):
        sub = get_nums(s[i-1], s[i], 40)
        for k, v in sub.items():
            c[k] += v
    
    # for i in range(40):
    #     news = []
    #     for j in range(1, len(s)):
    #         a,b = s[j-1], s[j]
    #         if a+b in edges:
    #             news.append(a)
    #             news.append(edges[a+b])
    #         else:
    #             news.append(a)
    #     news.append(s[-1])
    #     s = ''.join(news)
    # c = Counter(s)
    print(c)
    vs = c.values()
    print(max(vs) - min(vs))
else:
    pass