# Dijkstra's. Could have used A* but forgot how it works.

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

import copy

# inp = ((),(), ('c', 'd'), (), ('a', 'b'), (), ('a', 'd'), (), ('c', 'b'),(), ())
# inp = ((),(), ('c', 'd', 'd', 'd'), (), ('a','b', 'c', 'b'), (), ('a', 'a', 'b', 'd'), (), ('c', 'c', 'a', 'b'),(), ())
inp = ((),(), ('a', 'b'), (), ('d', 'c'), (), ('c', 'b'), (), ('a', 'd'),(), ())
addon = ['dd', 'bc', 'ab', 'ca']
# inp = ((),(),('a','b'),('b',),(),('d',),('c','c'),(),('a','d'),(),())
if True:
    inp = list(inp)
    inp[2] = inp[2][:1] + tuple(addon[0]) + inp[2][1:]
    inp[4] = inp[4][:1] + tuple(addon[1]) + inp[4][1:]
    inp[6] = inp[6][:1] + tuple(addon[2]) + inp[6][1:]
    inp[8] = inp[8][:1] + tuple(addon[3]) + inp[8][1:]
    inp = tuple(inp)
    print(inp)


percost = {'a':1, 'b':10, 'c':100, 'd':1000}
waits = [0,1,3,5,7,9,10]
target = {'a':2, 'b':4, 'c':6, 'd':8}
def pop_one(layout, i):
    newlayout = list(layout)
    if i in waits:
        ans = layout[i][0]
        newlayout[i] = ()
    else:
        ans = layout[i][-1]
        newlayout[i] = newlayout[i][:-1]
    return ans, newlayout

def get_heuristic(layout):
    ans = 0
    for i, x in enumerate(layout):
        for amphipod in x:
            ans += abs(i-target[amphipod]) * percost[amphipod]
    return ans

if True:
    ans = 0
    inps = []
    # while True:
    #     try:
    #         inps.append(input())
    #     except EOFError:
    #         break
    stack = [(0, inp)]
    seen = dict()
    traceback = dict()
    while len(stack) > 0:
    # for i in range(6):
        cost, layout = heappop(stack)
        # if layout in seen:
        #     continue
        seen[layout] = cost
        if cost%2000 == 0:
            print(cost, layout)
        if len(layout[0]) == 0 and len(layout[1])==0 and len(layout[3]) == 0 and len(layout[5])==0 and len(layout[7])==0 and len(layout[9])==0 and len(layout[10])==0:
            if all(x=='a' for x in layout[2]) and all(x=='b' for x in layout[4]) and all(x=='c' for x in layout[6]) and all(x=='d' for x in layout[8]):
                print(cost)
                print(layout)
                ans = layout
                break
        for i in range(len(layout)):
            if len(layout[i]) == 0:
                continue
            
            for dx in [-1,1]:
                dest = i
                while dest+dx >= 0 and dest+dx<len(layout):
                    if i in waits:
                        movement = 0
                    else:
                        movement = 5 - len(layout[i])
                    dest += dx
                    amphipod, newlayout = pop_one(layout, i)
                    if dest < 0:
                        break
                    if dest in waits:
                        if len(layout[dest]) > 0:
                            break
                        if i in waits:
                            continue
                        newlayout[dest] = (amphipod,)
                        movement += abs(dest-i)
                    else:
                        if target[amphipod] != dest:
                            continue
                        if all(x==amphipod for x in newlayout[dest]):
                            newlayout[dest] = newlayout[dest] + (amphipod,)
                            movement += abs(dest-i)
                            movement += 5 - len(newlayout[dest])
                            # if len(newlayout[dest]) == 1:
                            #     movement += 2
                            # else:
                            #     movement += 1
                        else:
                            continue
                    newcost = movement * percost[amphipod] + cost
                    # if tuple(newlayout) == ((),(),('a','b'),(),('b',),('d',),('c','c'),(),('a','d'),(),()):
                    #     print(i,dx,dest, movement, newcost)
                    key = tuple(newlayout)
                    if key not in seen or newcost < seen[key]:
                        seen[key] = newcost
                        heappush(stack, (newcost, key))
                        traceback[key] = layout

    while layout in traceback:
        print(layout)
        layout = traceback[layout]


    print(ans)
else:
    pass