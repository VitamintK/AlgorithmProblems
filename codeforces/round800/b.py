T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    ans = n
    for i in range(1,n):
        if s[i] == s[i-1]:
            continue
        ans += i
    print(ans)