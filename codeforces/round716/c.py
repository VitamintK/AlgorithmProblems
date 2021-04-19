import math
n = int(input())
ans = []
acc = 1
for i in range(1,n):
    if math.gcd(n,i) != 1:
        continue
    ans.append(i)
    acc = (acc*i)%n
if acc != 1:
    ans = [x for x in ans if x!=acc]
print(len(ans))
print(*ans)