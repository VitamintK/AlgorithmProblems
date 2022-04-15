N = 5
ans = 0
for i in range(10,1123456):
    sm = 0
    x = i
    while x != 0:
        dig = x%10
        sm += pow(dig, N)
        x//=10
    if sm == i:
        ans += sm
print(ans)