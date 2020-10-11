T = int(input())
for t in range(T):
    xs = [int(x) for x in input().split()]
    g = sum(xs)
    print(g-1)