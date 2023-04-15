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
            while w in backtrace and backtrace[w] != u:
                w = backtrace[w]
            next_step[u][v] = w


    @lru_cache(maxsize=None)
    def get_flow(bitset):
        flow = 0
        for v, i in v_to_i.items():
            bit = bitops[i]
            if (bit & bitset) == 0:
                flow += flows[v]
        return flow
    came_from = dict()
    
    counter = 0
    seen = set()
    def dead_end(vw,t,bitset,dests):
        # for tt in range(0,t+1):
        #     if (vw,tt,bitset,dests) in seen:
        #         return True
        return False
    @lru_cache(maxsize=None)
    def dfs(vw,t,bitset, dests):
        if dead_end(vw,t,bitset,dests):
            return 0
        seen.add((vw,t,bitset,dests))
        global counter
        v,w = vw
        vdest, wdest = dests
        flow = get_flow(bitset)
        if t==T:
            counter += 1
            if counter%100000==0:
                print(counter)
            return 0
        if bitset==0:
            print('got em all')
            return dfs(vw, t+1, bitset, dests) + flow
        # if flow < 50 and t > 8:
            # print('dull')
            # return 0
        best = 0
        for a,b in [(0,1), (1,0), (1,1), (0,0)]:
            bitset2 = bitset
            if a:
                can_turn_on = False
                if flows[v]!=0 and ((bitops[v_to_i[v]]) & bitset) != 0:
                    can_turn_on = True
                    bit = (1<<v_to_i[v])
                    bitset2 ^= bit
                if not can_turn_on:
                    continue
            if b:
                can_turn_on = False
                if flows[w]!=0 and ((bitops[v_to_i[w]]) & bitset) != 0:
                    can_turn_on = True
                    bit = (1<<v_to_i[w])
                    bitset2 ^= bit
                if not can_turn_on:
                    continue
            
            if a:
                vvvs = [(v, None)]
            else:
                if vdest is not None:
                    destinations = [vdest]
                else:
                    destinations = next_step[v]
                vvvs = []
                for destination in destinations:
                    if ((bitops[v_to_i[destination]])&bitset2)!=0:
                        vvvs.append((next_step[v][destination], destination))
                if len(vvvs)==0:
                    vvvs=[(v, None)]
            if b:
                wwws = [(w, None)]
            else:
                if wdest is not None:
                    destinations = [wdest]
                else:
                    destinations = next_step[w]
                wwws = []
                for destination in destinations:
                    if ((bitops[v_to_i[destination]])&bitset2)!=0:
                        wwws.append((next_step[w][destination], destination))
                if len(wwws)==0:
                    wwws=[(v, None)]
            # cfv,cfw = None,None
            # if (vw,t,bitset) in came_from:
            #     cfv, cfw = came_from[(vw,t,bitset)]
            for vvv,vvvdest in vvvs:
                for www,wwwdest in wwws:
                    # if vvv==cfv or www==cfw:
                    #     continue
                    vx, wx = vvv,www
                    # if vx > wx:
                    #     vx,wx = wx,vx
                    # came_from[(vx,wx),t+1,bitset2] = vw
                    xx = dfs((vx,wx),t+1,bitset2, (vvvdest, wwwdest)) + flow
                    # xx = dfs(v,t+1,bitset) + flow
                    best = max(best, xx)
        return best
        
    ans = dfs(('AA', 'AA'), 0, (bitops[len(v_to_i)])-1, (None,None))
    print(ans)
    # start = 'AA'
    # v = start
    # i = 0
    # cur_flow = 0
    # while i < T:
    #     print(cur_flow)
    #     ans += cur_flow
    #     time_remaining = T-i
    #     backtrace = dict()
    #     q = deque([(v,0)])
    #     seen = set()
    #     best = 0
    #     argbest = None
    #     while len(q) > 0:
    #         print(q)
    #         ex, t = q.popleft()
    #         time = (time_remaining - t - 1)
    #         score = time * flows[ex]
    #         if score > best:
    #             best = score
    #             argbest = ex
    #         for u in edges[ex]:
    #             if u in seen:
    #                 continue
    #             q.append((u,t+1))
    #             seen.add(u)
    #             backtrace[u] = ex
    #     if argbest == v:
    #         cur_flow += flows[v]
    #         flows[v] = 0
    #     else:
    #         while argbest in backtrace and backtrace[argbest] != v:
    #             argbest = backtrace[argbest]
    #         if argbest is not None:
    #             v = argbest
    #     i += 1

    # print(ans)
else:
    pass