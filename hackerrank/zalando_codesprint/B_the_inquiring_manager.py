n = int(input())
from collections import defaultdict
d = defaultdict(lambda: -1)
for i in range(n):
    inp = input().split()
    if(inp[0] == '1'):
        b, a = int(inp[1]), int(inp[2])
        d[a] = max(d[a], b)
    else:
        a = int(inp[1])
        maxmax = -1
        for j in range(60):
            maxmax = max(maxmax, d[a-j])
        print(maxmax)