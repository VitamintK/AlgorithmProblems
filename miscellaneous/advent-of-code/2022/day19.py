from collections import defaultdict, deque, Counter, namedtuple
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

 

if True:
    ans = 0
    inps = []
    blueprints = []
    while True:
        try:
            inp = input()
            inp = get_ints(inp)
            blueprint = [
                [inp[1],0,0],
                [inp[2],0,0],
                [inp[3], inp[4], 0],
                [inp[5], 0, inp[6]],
            ]
            blueprints.append(blueprint)
        except EOFError:
            break
    print(blueprints)
    for i, blueprint in enumerate(blueprints):
        i = i+1
        best = 0
        @lru_cache(maxsize=None)
        def dfs(t, material, bots, newbots):
            # print(t, material, bots, newbots)
            # if material[0] > 5:
            #     return 0
            if t==24:
                return 0
            bots = list(bots)
            material = list(material)
            myans = 0
            for j, bp in reversed(list(enumerate(blueprint))):
                if all(bp[k] <= material[k] for k in range(3)):
                    newmaterial = list(material)
                    for k in range(3):
                        newmaterial[k] -= bp[k]
                    newnewbots = list(newbots)
                    newnewbots[j] += 1
                    myans = max(myans, dfs(t, tuple(newmaterial), tuple(bots), tuple(newnewbots)))
                    if j==3:
                        return myans
                    # return myans
            newmaterial = list(material)
            for j,num in enumerate(bots):
                if j < 3:
                    newmaterial[j] += num
                else:
                    geodes = num
            nbots = list(bots)
            for j in range(4):
                nbots[j] += newbots[j]
            nbots = tuple(nbots)
            myans = max(myans, dfs(t+1, tuple(newmaterial), nbots, (0,0,0,0)) + geodes)
            global best
            if myans > best:
                print('new best', myans)
            best = max(best, myans)
            return myans
        myans = dfs(0, (0,0,0), (1,0,0,0), (0,0,0,0)) 
        print(myans)
        ans += i * myans
    

    print(ans)
else:
    pass