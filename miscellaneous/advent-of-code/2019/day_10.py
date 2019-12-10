from collections import defaultdict, deque, Counter
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
grid = []
asts = []
if True:
    while True:
        try:
            grid.append(list(input()))
        except EOFError:
            break
else:
    pass

for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == '#':
            asts.append((r,c))

maxans = 0
for main in asts:
    r, c = main
    slopes = defaultdict(lambda: [0, 0]) # MIGHT NEED FRACTIONS not floats
    ans = 0
    for a in asts:
        if a == main:
            continue
        ar, ac = a
        if ac == c:
            slope = 10000000000000
        else:
            slope = (ar - r)/(ac - c)
        parity = (ac < c) or ((ac == c) and (ar < r))
        if slopes[slope][parity] == 0:
            ans += 1
            slopes[slope][parity] = True
    if ans > maxans:
        print(r, c)
    maxans = max(ans, maxans)
print(maxans)

#23, 17
# part 2
from math import atan2, pi
main = (23, 17)
r, c = main
asts2 = []
for ast in asts:
    ar, ac = ast
    if ast == main:
        continue
    # if ac == c:
    #     if ar < r:
    #         rads = 3 * pi/2
    #     else:
    #         rads = pi/2
    # else:
    #     slope = (ar - r)/(ac - c)
    # haha didn't realize there was a two-argument atan function :'D
    asts2.append((atan2(ar -r, ac - c)%(2 * pi), (ast)))
asts2.sort(key = lambda x: (x[0] + pi/2)%(2*pi))
cnt = {z: [y for y in asts2 if y[0] == z] for z in [x[0] for x in asts2]}
for cn in cnt:
    cnt[cn].sort(key = lambda x: (r - x[1][0]) * (r - x[1][0]) + (c - x[1][1]) * (c-x[1][1]), reverse=True)
for p in cnt:
    print(cnt[p])
print(asts2)
i = 0
while True:
    for p in cnt:
        if len(cnt[p]) > 0:
            g = cnt[p].pop()
            print("vaporizing {}".format(g))
            i += 1
            if i == 200:
                print(100 * g[1][1] + g[1][0])
                break
    else:
        continue
    break