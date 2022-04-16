facs = [1]
f = 1
for i in range(1,10):
    f *= i
    facs.append(f)

ans = 0
for i in range (3, 4000000):
    agg = 0
    x = i
    while x != 0:
        agg += facs[x%10]
        x //= 10
    if agg==i:
        print(i)
        ans += i
print(ans)