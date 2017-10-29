x = int(input())
i = input()
from collections import defaultdict
parents = dict()
while i != '-1':
    l = [int(j) for j in i.split()[1:]]
    for j in l:
        parents[j] = (int(i.split()[0]))
    i = input()

print(x)
while(x in parents):
    x = parents[x]
    print(x)

