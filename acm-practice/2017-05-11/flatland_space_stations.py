#https://www.hackerrank.com/challenges/flatland-space-stations

import sys

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]

lefts = [-1]*n
for i in c:
    lefts[i] = 0
for j in range(len(lefts)):
    if lefts[j] != 0 and j > 0 and lefts[j-1] != -1:
        lefts[j] = lefts[j-1] + 1

rights = [-1]*n
for i in c:
    rights[i] = 0
for j in reversed(range(len(rights))):
    if rights[j] != 0 and j < len(rights) -1 and rights[j+1] != -1:
        rights[j] = rights[j+1] + 1

print(max(min(x) for x in zip([i if i!=-1 else 100000000 for i in lefts], [j if j != -1 else 1000000000 for j in rights])))