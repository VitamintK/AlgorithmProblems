T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    if len(set(xs)) == 1:
        print(len(xs))
    else:
        print(1)