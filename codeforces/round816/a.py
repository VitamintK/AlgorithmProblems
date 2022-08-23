T = int(input())
for t in range(T):
    n,m = map(int, input().split())
    print(n+m-1-1 + min(n,m)-1 + (0 if max(n,m)==1 else 1))