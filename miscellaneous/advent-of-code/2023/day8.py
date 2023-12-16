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

"""After doing all this work and writing all this code and debugging for ~1 hr, I realized that
due to the particular setup of the input, the solution is just the LCM, so I used wolfram alpha to get the answer.
"""

# Chinese remainder theorem
def chinese_remainder(nums, rems):
    print(nums, rems)
    prod = 1
    for n in nums:
        prod *= n
    ans = 0
    for n, r in zip(nums, rems):
        p = prod//n
        ans += r*mul_inv(p, n)*p
    return ans%prod

def mul_inv(a, b):
    assert a > b
    assert math.gcd(a,b) == 1
    print('a,b', a,b)
    b0 = b
    x0, x1 = 0, 1
    if b==1:
        return 1
    while a>1:
        q = a//b
        # print(q, a, b)
        a, b = b, a%b
        x0, x1 = x1-q*x0, x0
    if x1<0:
        x1 += b0
    return x1

import math
if True:
    ans = 0
    inps = []
    inst = input()
    m = {'R': 1, 'L': 0}
    net = dict()
    input()
    while True:
        try:
            x = input()
            k = x.split()[0]
            v = x.split('=')[1]
            v = v.split(',')
            v = [v[0].strip()[1:], v[1].strip()[:-1]]
            net[k] = v
        except EOFError:
            break
    # k = 'AAA'
    ks = [k for k in net.keys() if k[-1] == 'A']

    cycle_offsets = []
    cycle_lengths = []
    z_points = []
    for kk in ks:
        k = kk
        i = 0
        been = dict()
        zp = set()
        # while not k[-1] == 'Z':
        while (k, i%len(inst)) not in been:
            if k[-1] == 'Z':
                # if len(zp) == 0:
                    # hack bc it's always 0 in the real case, and this makes it work for the example
                zp = {i}
            been[(k, i%len(inst))] = i
            k = net[k][m[inst[i%len(inst)]]]
            i += 1
        assert len(zp) == 1
        z_points.append(zp.pop())
        cycle_offsets.append(been[(k, i%len(inst))])
        cycle_lengths.append(i-been[(k, i%len(inst))])
        print('cycled at:', i, i-been[(k, i%len(inst))])
        print('zp', z_points)
    

        # x = cycle_offsets[0] + i*cycle_lengths[0] + z_points[0]
        # good = True
        # for j in range(1, len(cycle_offsets)):
        #     if (x-cycle_offsets[j])%cycle_lengths[j] != z_points[j]:
        #         good = False
        #         break
        # if good:
        #     print(x)
        #     break
    rems = [cycle_offsets[i] + z_points[i] for i in range(len(cycle_offsets))]
    rems = [rem%cycle_lengths[i] for i, rem in enumerate(rems)]
    print(cycle_lengths, rems)

    for i in range(len(cycle_lengths)):
        gcd = math.gcd(cycle_lengths[i], rems[i])
        cycle_lengths[i] //= gcd
        rems[i] //= gcd
    # assert math.gcd(*rems) == 1
    # assert math.gcd(*cycle_lengths) == 1
    x = chinese_remainder(cycle_lengths, rems)
    # while not all([k[-1]=='Z' for k in ks]):
        
    #     ks = [net[k][m[inst[i%len(inst)]]] for k in ks]
    #     i += 1
    # print(i)

    # print(ans)
    
else:
    pass