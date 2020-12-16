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
    rules = dict()
    ans = 0
    inps = []
    zone = 0
    while True:
        try:
            inps.append(input())
        except EOFError:
            break
    tickets = []
    for i in inps:
        if i.strip() == '':
            zone +=1
            continue
        if zone == 0:
            k, v = i.split(': ')
            v = v.split(' or' )
            nums = [int(x) for x in  v[0].split('-')]
            nums[1] += 1
            v0 = range(*nums)
            nums = [int(x) for x in  v[1].split('-')]
            nums[1] += 1
            v1 = range(*nums)
            rules[k] = (v0,v1)
        elif zone == 1:
            if i[0] == 'y':
                continue
            yours = [int(x) for x in i.split(',')]
            valids = [set(range(len(rules))) for x in yours]
        else:
            if i[0] == 'n':
                continue
            vals = [int(x) for x in i.split(',')]
            for val in vals:
                passed = False
                for rule in rules:
                    for r in rules[rule]:
                        if val in r:
                            passed = True
                if not passed:
                    break
            else:
                tickets.append(vals)

    for ticket in tickets:
        vals = ticket
        for i, val in enumerate(vals):
            for j, rule in enumerate(rules):
                valid = False
                for r in rules[rule]:
                    if val in r:
                        valid = True
                if not valid:
                    valids[i].discard(j)
    print(valids)

    for i in range(100):
        for valid in valids:
            if len(valid) == 1:
                for v2 in valids:
                    if v2 == valid:
                        continue
                    v2.discard(list(valid)[0])
    print(valids)
    rule_to_index = dict()
    for j, valid in enumerate(valids):
        for i, rule in enumerate(rules):
            if list(valid)[0] == i:
                rule_to_index[rule] = j
    ans = 1
    for i, rule in enumerate(rules):
        if rule.split()[0] == 'departure':
            ans *= yours[rule_to_index[rule]]

    print(ans)
else:
    pass