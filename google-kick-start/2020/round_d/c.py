T = int(input())
for t in range(T):
    n = int(input())
    n, a, b = map(int, input().split())
    ps = [int(x) for x in input().split()]
    
    print("Case #{}: {}".format(t+1, ans))