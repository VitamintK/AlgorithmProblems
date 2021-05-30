T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    print(6 * n//2)
    for i in range(n//2):
        a = i*2 + 1
        b = a+1
        print(1,a,b)
        print(1,a,b)
        print(2,a,b)
        print(1,a,b)
        print(1,a,b)
        print(2,a,b)
