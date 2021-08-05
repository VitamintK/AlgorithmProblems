import math
storage = dict()
ans = 0
for i in range(1,10000):
    sm = 1
    for j in range(2,int(math.sqrt(i))+1):
        if i%j == 0:
            sm += j
            if i//j > j:
                sm += i//j
    if sm < i and storage[sm] == i:
        ans += sm + i
        print(i, sm)
    storage[i] = sm
print(ans)