T = int(input())
for t in range(T):
    n = int(input())
    ans = []
    for i in range(1,n+1):
        if i%2 == 1:
            ans.append(i+1)
        else:
            ans.append(i-1)
    if n%2 == 1:
        ans[-3] = n
        ans[-2] = n-2
        ans[-1] = n-1
    print(*ans)