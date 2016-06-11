k, m, n = map(int, input().split())
from collections import defaultdict
d = defaultdict(int)
for i in range(n):
    d[input()]+=1
print('\n'.join([i[0] for i in sorted(d.items(), key = lambda x: (x[1], -int(x[0])), reverse=True)[:k]]))