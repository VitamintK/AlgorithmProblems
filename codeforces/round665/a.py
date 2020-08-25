T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    if k <= n:
        if (n%2 == 0) == (k%2 == 0):
            print(0)
            continue
        else:
            print(1)
            continue
    else:
        print(k - n)