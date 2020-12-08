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
    insG = []
    while True:
        try:
            i, v = input().split()
            v = int(v)
            insG.append((i,v))
        except EOFError:
            break
    
    trans = {'jmp':'nop', 'nop':'jmp', 'acc':'acc'}
    for i in range(len(insG)):
        ins = insG[:]
        ins[i] = (trans[ins[i][0]], ins[i][1])
        visited = set()
        acc = 0
        i = 0
        while i not in visited:
            if i == len(ins):
                print(acc)
                print("!!!!")
                break
            if i > len(ins):
                break
            visited.add(i)
            if ins[i][0] == 'nop':
                i +=1
                continue
            elif ins[i][0] == 'acc':
                acc += ins[i][1]
                i += 1
            else:
                i += ins[i][1]
        

else:
    pass