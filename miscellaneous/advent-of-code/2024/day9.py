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
    inp = input()
    l = []
    flag = True
    for i, x in enumerate(inp):
        x = int(x)
        if flag:
            for j in range(x):
                l.append(i//2)
        else:
            for j in range(x):
                l.append(-1)
        flag = not flag
    
    # print(l)

    pt = 0
    while l[pt] != -1:
        pt += 1
    for i in reversed(range(len(l))):
        if l[i] == -1:
            l.pop()
            continue
        if i <= pt:
            break
        l[pt] = l[i]
        l.pop()
        while l[pt] != -1:
            pt += 1
            if pt >= len(l):
                break
    # print(l)
    for i, x in enumerate(l):
        ans += i * x

    print(ans)
else:
    ans = 0
    inp = input()
    l = []
    flag = True
    orig_nums = []
    blanks = []
    for i, x in enumerate(inp):
        x = int(x)
        if flag:
            orig_nums.append((x, i//2))
        else:
            blanks.append(x)
        flag = not flag
    # lengths = dict()
    # blanks = []
    # for i, x in enumerate(inp):
    #     x = int(x)
    #     if flag:
    #         for j in range(x):
    #             l.append(i//2)
    #             lengths[i//2] = x
    #     else:
    #         if len(blanks) == 0 or blanks[-1] < x:
    #             blanks.append((len(l), x))
    #         for j in range(x):
    #             l.append(-1)
    #     flag = not flag
    #     max_id = i//2

    # left, right = 0, len(l)-1
    # def update(blanks, old_value, new_value):
    #     index = blanks.index(old_value)
    #     if index > 0 and new_value[1] < blanks[index-1][1]:
    #         blanks.remove(old_value)
    #     for i in range(new_value[0], len(l)):
    #         if 

    # while right > blanks[0][0]:
    #     length = lengths[l[right]]
    #     for i, blank_len in blanks:
    #         if blank_len >= length:
    #             for j in range(length):
    #                 l[i+j] = l[right]
    #                 l[right] = -1
    #             update(blanks, (i, blank_len), (i+length, blank_len-length))

    # I'm 28 and my brain has officially atrophied to the point where it's too much work
    # to do the linear-time solution. Instead I'll do the worst-case quadratic solution:

    new_nums = [[] for _ in blanks]
    for i in reversed(range(len(orig_nums))):
        length, id = orig_nums[i]
        for j, blank in enumerate(blanks):
            if j >= i:
                break
            if blank >= length:
                new_nums[j].append((length, id))
                blanks[j] -= length
                orig_nums[i] = (length,0)
                # blanks[i-1] += length
                break
        
    # print(orig_nums, new_nums, blanks)
    i = 0
    for orig,news,blank in zip(orig_nums, new_nums, blanks):
        for j in range(orig[0]):
            ans += i * orig[1]
            i += 1
        for new in news:
            for j in range(new[0]):
                ans += i * new[1]
                i += 1
        i += blank
            


    
    
    

    print(ans)