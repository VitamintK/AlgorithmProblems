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

if True:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    def go(inps, model):
        mem = defaultdict(int)
        i = 0
        for step, inp in enumerate(inps):
            inp = inp.split()
            if len(inp) == 2:
                x,y = inp
            else:
                x,y,z = inp
                if z in string.ascii_lowercase:
                    z = mem[z]
                else:
                    z = int(z)
            if x=='inp':
                print(mem)
                mem[y] = int(model[i])
                i += 1
            elif x=='add':
                ans = mem[y] + z
                mem[y] = ans
            elif x=='mul':
                mem[y] = mem[y] * z
            elif x=='div':
                mem[y] = mem[y]//z
            elif x=='mod':
                mem[y] = mem[y] % z
            elif x=='eql':
                mem[y] = int(mem[y] == z)
            else:
                raise ValueError("x")
        return 'z' in mem and mem['z'] == 0
    base = 11111111111111
    bigy = 99999999999995
    import random
    for _ in range(1):
        # i = random.randint(base, bigy)
        i = bigy
        s = f'{i:014}'
        if go(inps, s):
            print(s)
        # print(go(inps, s))
    ls = [6,2,13,8,13,8,3,11,10,8,14,6,8,2]
    assert len(ls) == 14
    ks = [12, 10, 10, -6, 11, -12, 11, 12, 12, -2, -5, -4, -4, -12]
    ms = [1,1,1,26,1,26,1,1,1,26,26,26,26,26]
    assert len(ms) == 14
    assert len(ks) == 14
    def go():
        w = 0
        x = 0
        y = 0
        z = 0
        ans = []
        for i in range(14):
            x = z%26
            z = z//ms[i]
            x += ks[i]

            # print(x,y,z)
            if i == 0:
                w = 7
            elif i == 1:
                w = 3
            elif i == 2:
                w = 1
            # elif i == 3:
            #     w = 9
            else:
                if 0 < x < 10:
                    if random.random() < 0.1:
                        w = random.randint(1,x)
                    else:
                        w = x
                else:
                    if i < 13 and 1 <= (35 - ls[i] - ks[i+1])%26 < 10:
                        if random.random() < 0.1:
                            w = random.randint(1,8)
                        else:
                            w = (35 - ls[i] - ks[i+1])%26
                    elif i==13:
                        w = 1
                    else:
                        w = random.randint(1,9)

            if x==w:
                x,y = 0, 1
            else:
                x,y = 1, 26
            z *= y
            y = (w+ls[i]) * x
            z += y
            ans.append(w)
            # print(z)
        if z== 0:
            print(ans)
        if z != 0:
            return None
        return int(''.join(str(x) for x in ans))
    ans = 99999999999999999999
    for i in range(10000000):
        x = go()
        if x is not None:
            ans = min(ans, x)
            print(ans)
    # print(ans)
else:
    pass