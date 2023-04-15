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

bitops = dict()
for i in range(60):
    bitops[i] = (1<<i)

@lru_cache(maxsize=None)
def get_flow(bitset):
    flow = 0
    for v, i in v_to_i.items():
        bit = bitops[i]
        if (bit & bitset):
            flow += flows[v]
    return flow

if True:
    T = 30
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    edges = defaultdict(list)
    flows = dict()
    v_to_i = dict()
    c = 0
    for inp in inps:
        s = inp.split()
        v = s[1]
        x = get_ints(inp)[0]
        es = inp.split('valve')[1]
        if es[0] == 's':
            es = es[1:]
        es = es.split(',')
        es = [e.strip() for e in es]
        edges[v] = es
        flows[v] = x
        if x != 0:
            v_to_i[v] = c
            c += 1
    T = 26
    # dp = dict()
    # dp['AA'][(1<<len(v_to_i))-1] = (0,0)
    # for i in range(T):
    #     newdp = defaultdict(lambda: defaultdict(int))
    #     for u in dp:
    #         for bitset in dp[u]:
    #             best_so_far = dp[u][bitset]
    #             can_turn_on = False
    #             if flows[u]!=0 and ((1<<v_to_i[u]) & bitset) != 0:
    #                 can_turn_on = True
    #                 bit = (1<<v_to_i[u])
    #             if can_turn_on:
    #                 newdp[u][bitset ^ bit] = 
    next_step = defaultdict(dict)
    distance = defaultdict(dict)
    for u in flows:
        backtrace = dict()
        q = deque([u])
        while len(q) > 0:
            v = q.popleft()
            for w in edges[v]:
                if w in backtrace:
                    continue
                backtrace[w] = v
                q.append(w)
        for v in v_to_i:
            w = v
            x = 1
            while w in backtrace and backtrace[w] != u:
                w = backtrace[w]
                x += 1
            next_step[u][v] = w
            distance[u][v] = x
    count = 0
    def get_score(p1, p2):
        # debug = False
        # if p2 ==('AA', 'BB', 'JJ', 'CC'):
        #     debug=True
        score = 0
        for p in (p1,p2):
            t = 0
            for i in range(1,len(p)):
                d = distance[p[i-1]][p[i]]
                t += d + 1
                score += flows[p[i]] * (T-t)
        return score

    @lru_cache(maxsize=None)
    def dfs(t, p1, bits):
        if t >= T:
            return 0
        global count
        count += 1
        best = 0
        if count%10000==0:
            print(bin(bits))
            print(count)
        for v in v_to_i:
            if (bitops[v_to_i[v]] & bits):
                continue
            d = distance[p1][v]
            if t+d+1 >= T:
                continue
            best = max(best, dfs(t+d+1, v, bits | bitops[v_to_i[v]]) + (T-t-d-1)*flows[v])
        # best = max(best, dfs(t+1, p1, bits))
        best = max(best, dfs2(0, 'AA', bits))
        # print(t,p1,bin(bits), best)
        return best

    @lru_cache(maxsize=None)
    def dfs2(t, p2, bits):
        if t >= T:
            return 0
        global count
        count += 1
        best = 0
        if count%10000==0:
            print(bin(bits))
            print(count)
        for v in v_to_i:
            if (bitops[v_to_i[v]] & bits):
                continue
            d = distance[p2][v]
            if t+d+1 >= T:
                continue
            best = max(best, dfs2(t+d+1, v, bits | bitops[v_to_i[v]]) + (T-t-d-1)*flows[v])
        # best = max(best, dfs(t+1, p1, bits))
        # print(t,p2,bin(bits), best)
        return best

    ans = dfs(0, 'AA', 0)
    print(ans)



else:
    pass