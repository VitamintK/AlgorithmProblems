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
import numpy as np

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

INTERVAL_TYPE_INCLUSIVE = 0
INTERVAL_TYPE_EXCLUSIVE = 1
# def make_interval_class(start_type=INTERVAL_TYPE_INCLUSIVE, end_type=INTERVAL_TYPE_EXCLUSIVE):
#     class Interval:
#         start_type = start_type
#         end_type = end_type
#         def __init__(self, start, end):
#             self.start = start
#             self.end = end
# def merge(interval_a, interval_b):
#     interval = (min(interval_a[0], interval_b[0]), max(interval_a[1], interval_b[1]))
#     if interval[0] > interval[1]:
#         return None
####################################

PART = 1
PART = 2
if PART == 1:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    # R, C = len(inps), len(inps[0])
    outs = dict()
    ins = defaultdict(list)
    ts = dict()
    ffmem = dict()
    cjmem = defaultdict(dict)
    for inp in inps:
        a, bs = inp.split('->')
        a = a.strip()
        t = None
        if a != 'broadcaster':
            t, a = a[0], a[1:]
        ts[a] = t
        ffmem[a] = 0
        
        bs = [b.strip() for b in bs.split(',')]
        outs[a] = bs
        for b in bs:
            ins[b].append(a)
            cjmem[b][a] = 0

    print(outs, ins, ts, ffmem, cjmem)
    print(len(ts))
    hi = 0
    lo = 0
    def print_state():
        bitstring = []
        for k in ts:
            if ts[k] == '%':
                bitstring.append(str(ffmem[k]))
            elif ts[k] == '&':
                bitstring.append(str(int(all(cjmem[k]))))
        return ''.join(bitstring)
    for i in range(1000):
        lo += 1
        queue = deque([(b, 0, 'broadcaster') for b in outs['broadcaster']])
        # ans += len(queue)
        while len(queue) > 0:
            a, p, x = queue.popleft()
            if p:
                hi += 1
            else:
                lo += 1
            if a not in ts:
                if p == 0:
                    print(i+1)
                    exit()
                continue
            if ts[a] == '%':
                if p == 1:
                    continue
                ffmem[a] = int(not ffmem[a])
                pp = ffmem[a]
            elif ts[a] == '&':
                cjmem[a][x] = p
                if all(cjmem[a].values()):
                    pp = 0
                else:
                    pp = 1
            else:
                raise ValueError('')
            for b in outs[a]:
                queue.append((b, pp, a))
            # print(queue)
        print(print_state())
    print(lo, hi)
    print(lo * hi)
else:
    ans = 0
    inps = []
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    # R, C = len(inps), len(inps[0])
    outs = dict()
    ins = defaultdict(list)
    ts = dict()
    ffmem = dict()
    cjmem = defaultdict(dict)
    for inp in inps:
        a, bs = inp.split('->')
        a = a.strip()
        t = None
        if a != 'broadcaster':
            t, a = a[0], a[1:]
        ts[a] = t
        ffmem[a] = 0
        
        bs = [b.strip() for b in bs.split(',')]
        outs[a] = bs
        for b in bs:
            ins[b].append(a)
            cjmem[b][a] = 0

    print(outs, ins, ts, ffmem, cjmem)
    print(len(ts))
    print(ins['rx'])
    print(ins['zh'], ts['zh'])
    hi = 0
    lo = 0
    def print_state():
        bitstring = []
        for k in ts:
            if ts[k] == '%':
                bitstring.append(str(ffmem[k]))
            elif ts[k] == '&':
                bitstring.append(str(int(not all(cjmem[k]))))
        return ''.join([' ' if x=='0' else 'X' for x in bitstring])
    def print_pt():
        bitstring = []
        for k in ts:
            if k in ['vd', 'ns', 'bh', 'dl']:
                bitstring.append('V')
            else:
                bitstring.append(' ')
        print(''.join(bitstring))
    print_pt()
    patterns = defaultdict(list)
    for i in range(100000):
        lo += 1
        queue = deque([(b, 0, 'broadcaster') for b in outs['broadcaster']])
        # ans += len(queue)
        while len(queue) > 0:
            a, p, x = queue.popleft()
            if p:
                hi += 1
            else:
                lo += 1
            if a not in ts:
                if p == 0:
                    print(i+1)
                    exit()
                continue
            if ts[a] == '%':
                if p == 1:
                    continue
                ffmem[a] = int(not ffmem[a])
                pp = ffmem[a]
            elif ts[a] == '&':
                cjmem[a][x] = p
                if all(cjmem[a].values()):
                    pp = 0
                else:
                    pp = 1
            else:
                raise ValueError('')
            for xxx in ['vd', 'ns', 'bh', 'dl']:
                if cjmem['zh'][xxx] == 1:
                    if i in patterns[xxx]:
                        continue
                    patterns[xxx].append(i)
            for b in outs[a]:
                queue.append((b, pp, a))
            # print(queue)
        # print(print_state())
    for k in patterns:
        arith = []
        for i in range(1, len(patterns[k])):
            arith.append(patterns[k][i] - patterns[k][i-1])
        print(k, patterns[k], arith)

    print(lo, hi)
    print(lo * hi)