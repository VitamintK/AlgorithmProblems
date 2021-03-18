ans = []
for n in range(3,40):
    for k in range(3,n+1):
        ans.append((n,k))
print(len(ans))
for x in ans:
    print(*x)