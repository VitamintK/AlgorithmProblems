T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    if n%2==0:
        smallest_pile = min(xs)
        for i in range(n):
            if xs[i] == smallest_pile:
                if i%2==0:
                    print("Joe")
                    break
                else:
                    print("Mike")
                    break
    else:
        print("Mike")