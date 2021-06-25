T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    if sum(xs) <= 0:
        print(1)
    else:
        if sum(xs) - len(xs) < 0:
            print(1)
        else:
            print(sum(xs) - len(xs))