T = int(input())
for t in range(T):
    n,m,k = map(int,input().split())
    ans = n-1 + (m-1)*n
    # print(ans, k)
    if ans == k:
        print("YES")
    else:
        print("NO")