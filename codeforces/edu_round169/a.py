T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    if n == 1:
        print("YES")
    elif n == 2:
        if abs(xs[0] - xs[1]) == 1:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
    