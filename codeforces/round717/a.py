T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    xs = [int(x) for x in input().split()]
    l = 0
    r = n-1
    while k > 0 and l != r:
        amount = min(xs[l], k)
        k -= amount
        xs[l] -= amount
        xs[r] += amount
        if xs[l] == 0:
            l +=1
    print(*xs)