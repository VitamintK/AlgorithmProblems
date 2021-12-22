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

class X:
    def __init__(self, s):
        self.s = s
        self.ans = 0
    def parse(self, s):
        # returns (bits_eaten, return_value)
        if len(s) == 0:
            return (0, 0)
        if all(x=='0' for x in s):
            return (len(s), 0)
        version = s[:3]
        self.ans += int(version, base=2)
        type_id = s[3:6]
        if type_id == '100':
            # literal value
            ptr = 6
            val = 0
            while ptr < len(s) and s[ptr]=='1':
                # print(f'{val=}')
                val *= 16
                val += int(s[ptr+1:ptr+5], base=2)
                ptr += 5
            val *= 16
            val += int(s[ptr+1:ptr+5], base=2)
            if ptr < len(s):
                # print(f'{val=}')
                return (ptr+5, val)
            else:
                raise ValueError('shouldnt happen')
                return ptr
        else:
            subcomps = []
            # something else
            LTID = s[6]
            if LTID == '0':
                # next 15 bits are the length of sub-packets
                l = int(s[7:22], base=2)
                # self.parse(s[22:22+l])
                # self.parse(s[22+l:])
                parsed = 0
                while parsed < l:
                    # print(parsed, l, s)
                    bits_eated, ret = self.parse(s[22+parsed:])
                    parsed += bits_eated
                    subcomps.append(ret)
                assert parsed == l
                parsed = parsed+22
            else:
                # next 11 bits are the number of sub-packets
                num = int(s[7:18], base=2)
                parsed = 0
                for i in range(num):
                    bits_eated, ret = self.parse(s[18+parsed:])
                    parsed += bits_eated
                    subcomps.append(ret)
                parsed = parsed+18
            my_ret = None
            if type_id == '000':
                my_ret = sum(subcomps)
            elif type_id == '001':
                my_ret = 1
                for r in subcomps:
                    my_ret *= r
            elif type_id == '010':
                my_ret = min(subcomps)
            elif type_id == '011':
                my_ret = max(subcomps)
            elif type_id == '101':
                my_ret = int(subcomps[0] > subcomps[1])
            elif type_id == '110':
                my_ret = int(subcomps[0] < subcomps[1])
            elif type_id == '111':
                my_ret = int(subcomps[0] == subcomps[1])
            # print(subcomps)
            # print(s, parsed, my_ret)
            return (parsed, my_ret)



             

if True:
    ans = 0
    inp = input()
    bitstring = bin(int(inp, base=16))[2:]
    # bitstring = '110100101111111000101000'
    while len(bitstring)%4 != 0:
        bitstring = '0' + bitstring
    if inp[0] == '0':
        bitstring = '0000' + bitstring
    x = X(bitstring)
    print(bitstring)
    ans = x.parse(bitstring)
    print(x.ans)
    print(ans)



    # print(ans)
else:
    pass