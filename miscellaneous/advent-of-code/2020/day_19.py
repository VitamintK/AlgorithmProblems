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

import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

@lru_cache(maxsize=None)
def get_re(i):
    print(i)
    s = ''
    res = []
    for dis in rules[i]:
        if i not in dis:
            st = ''
            for seq in dis:
                if isinstance(seq, str):
                    st += seq
                else:
                    st += get_re(seq)
            res.append('({})'.format(st))
        else:
            if i == 8:
                res.append('({}+)'.format(get_re(dis[0])))
            elif i == 11:
                left = get_re(dis[0])
                right = get_re(dis[2])
                for j in range(1,20):
                    res.append('({}{{{}}}{}{{{}}})'.format(left, j, right, j))
                print(res)
    return '(' + '|'.join(res) + ')'

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    rules = dict()
    for i in inps:
        try:
            k, v = i.split(':')
        except:
            break
        rs = []
        for j in v.split('|'):
            j = j.strip()
            rs.append([eval(x) for x in j.split()])
        rules[int(k)] = rs
    r = get_re(0)
    r += '$'
    r = re.compile(r)
    print(r)
    for i in inps:
        print(i)
        if i.count(':') > 0:
            continue
        if r.match(i):
            ans +=1
    print(ans)
else:
    pass