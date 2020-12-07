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

import sys

sys.setrecursionlimit(100000)

def dfs(children, k):
    ans = 1
    for child, num in children[k]:
        # print(k, child, num)
        ans += num*dfs(children, child)
    return ans    

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation
alphabet='abcdefghijklmnopqrstuvwxyz'
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

if True:
    ans = 0
    parents = defaultdict(set)
    children = defaultdict(set)
    while True:
        try:
            k, v = input().split(' contain ')
            
            if v.strip() == 'no other bags.':
                continue
            v = v.split(',')
            k = ' '.join(k.split()[:-1])
            for child in v:
                child = child.strip()
                num = child.split()[0]
                child = ' '.join(child.split()[1:-1])
                parents[child].add(k)
                children[k].add((child, int(num)))
        except EOFError:
            break
    frontier = ['shiny gold']
    print(parents)
    visited = set()
    while len(frontier) > 0:
        ex = frontier.pop()
        print(ex)
        if ex in visited:
            continue
        visited.add(ex)
        for p in parents[ex]:
            if p in visited:
                continue
            frontier.append(p)
    print(len(visited))

    #part 2
    print(dfs(children, 'shiny gold'))

else:
    pass