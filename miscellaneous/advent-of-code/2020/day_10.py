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

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

if True:
    ans = 0
    ins = []
    while True:
        try:
            ins.append(int(input()))
        except EOFError:
            break
    ins.append(0)
    ins.append(max(ins)+3)
    ins.sort()
    ones = 0
    threes = 0
    for i in range(len(ins)):
        if i == 0:
            continue
        if ins[i]-ins[i-1] == 1:
            ones+=1
        elif ins[i]-ins[i-1] == 3:
            threes+=1
    print(ones*threes)

    # part 2
    dp = [0 for i in range(len(ins))]
    dp[0] = 1
    for i in range(len(ins)):
        if i ==0:
            continue
        a = 0
        for j in range(1,4):
            if i-j<0:
                continue
            if ins[i]-ins[i-j]<=3:
                a += dp[i-j]
            dp[i] = a
    print(dp[-1])
    print(ins[-1])
    print(ans)
else:
    pass