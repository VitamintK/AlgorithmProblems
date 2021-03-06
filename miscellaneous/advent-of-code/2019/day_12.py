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
vel = [[0,0,0] for i in range(4)]
poss = ((0, 6, 1), (4, 4, 19), (-11, 1, 8), (2, 19, 15))
# poss = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]
# poss = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
poss = [list(x) for x in poss]

def pretty(vel, poss):
    grid = [[0 for i in range(-100, 100)] for j in range(-100, 100)]
    for i in range(3):
        grid[poss[i][0]][poss[i][1]] = 1
    print('.......')
    for r in grid:
        print(''.join('#' if x else ' ' for x in r))

for i in range(1000):
    for j in range(4):
        for k in range(j+1, 4):
            for m in range(3):
                if poss[k][m] > poss[j][m]:
                    vel[k][m] -= 1
                    vel[j][m] += 1
                elif poss[k][m] < poss[j][m]:
                    vel[k][m] += 1
                    vel[j][m] -= 1
    for j in range(4):
        for m in range(3):
            poss[j][m] += vel[j][m]
    #pretty(vel, poss)
    print(vel, poss)

pot = [sum(abs(y) for y in x) for x in poss]
kin = [sum(abs(y) for y in x) for x in vel]
print(pot, kin, sum(a*b for a,b in zip(pot, kin)))


# pt 2
# ah, finally - a problem that isn't just implementation!
# actually, I'm not sure how to do this!
# ok I ended up just going on reddit and finding the answer
ans = []
ogposs = [[0, 6, 1], [4, 4, 19], [-11, 1, 8], [2, 19, 15]]
for m in range(3):
    vel = [0 for i in range(4)]
    ogp = [x[m] for x in ogposs]
    poss = [x[m] for x in ogposs]
    for i in range(1000000):
        for j in range(4):
            for k in range(j+1, 4):
                if poss[k] > poss[j]:
                    vel[k] -= 1
                    vel[j] +=1
                elif poss[k] < poss[j]:
                    vel[k] += 1
                    vel[j] -= 1
        for j in range(4):
            poss[j] += vel[j]
        if poss == ogp and not any(vel):
            print(i+1)
            ans.append(i+1)
            break

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return (a*b)/gcd(a,b)
print(lcm(lcm(ans[0], ans[1]),ans[2]))



