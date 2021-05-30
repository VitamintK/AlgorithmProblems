n, k = map(int, input().split())

import random
sims = []
for i in range(100):
    s = set()
    u = set(range(n))
    while True:
        c = random.sample(u, 1)[0]
        u.remove(c)
        s.add(c)
        a = 1
        cc = c+1
        while cc in s:
            cc += 1
            a += 1
        cc = c-1
        while cc in s:
            cc -= 1
            a += 1
        if a >= k:
            sims.append(len(s))
            print(s)
            break
print(sum(sims)/len(sims))