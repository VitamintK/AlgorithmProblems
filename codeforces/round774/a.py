T = int(input())
for t in range(T):
    n, s = map(int, input().split())
    ns = n*n
    ans = s//ns
    print(ans)