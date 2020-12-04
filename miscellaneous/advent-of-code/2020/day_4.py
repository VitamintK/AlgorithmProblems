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
import sys

sys.setrecursionlimit(100000)

def get_ints(s):
    return list(map(int, re.findall(r"-?\d+", s)))  # copied from mcpower from mserrano on betaveros' recommendation

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
def is_grid_valid(n,m, r,c,):
    return (0<=r<n) and (0<=c<m)

def err(b, k):
    print("{}!: {}".format(k,b[k]))

if True:
    ans = 0
    batches = []
    batch = dict()
    fields = 'byr iyr eyr hgt hcl ecl pid'.split()
    while True:
        try:
            a = input()
            if a.strip() == '':
                batches.append(batch)
                batch = dict()
            else:
                for i in a.split():
                    k,v = i.split(':')
                    batch[k] = v
        except EOFError:
            break
    batches.append(batch)
    for b in batches:
        missing = False
        for i in fields:
            if i not in b:
                missing = True
        if missing:
            continue
        print(b)
        if len(b['byr']) != 4 or int(b['byr']) < 1920 or int(b['byr']) > 2002:
            err(b,'byr')
            continue
        if len(b['iyr']) != 4 or int(b['iyr']) < 2010 or int(b['iyr']) > 2020:
            err(b,'iyr')
            continue
        if len(b['eyr']) != 4 or int(b['eyr']) < 2020 or int(b['eyr']) > 2030:
            err(b,'eyr')
            continue
        hgt = b['hgt']
        m = re.match(r"(\d+)(in|cm)$",hgt)
        if m is None:
            err(b,'hgt')
            continue
        hgtv = int(m.group(1))
        if m.group(2) == 'in':
            if hgtv < 59 or hgtv > 76:
                err(b,'hgt')
                continue
        else:
            if hgtv < 150 or hgtv > 193:
                err(b,'hgt')
                continue
        m = re.match(r"#([0-9]|[a-f]){6}$", b['hcl']) 
        if m is None:
            err(b,'hcl')
            continue
        ecl = b['ecl']
        if ecl not in 'amb blu brn gry grn hzl oth'.split():
            err(b,'ecl')
            continue
        pid = b['pid']
        if re.match(r"\d{9}$", pid) is None:
            err(b,'pid')
            continue
        ans += 1

    print(ans)
else:
    pass