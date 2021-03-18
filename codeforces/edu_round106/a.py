T = int(input())
for t in range(T):
    n, k1, k2 = map(int, input().split())
    w, b = map(int, input().split())
    if w*2<=k1+k2 and b*2<=n*2-k1-k2:
        print("YES")
    else:
        print("NO")