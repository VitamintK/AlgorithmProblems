N = 1001
ans = 1
c = 1
for i in range(1,N, 2):
    for _ in range(4):
        c += i+1
        ans += c
        # print(c)
print(ans)