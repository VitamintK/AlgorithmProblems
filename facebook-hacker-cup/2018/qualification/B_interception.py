T = int(input())
for t in range(T):
    n = int(input())
    for i in range(n+1):
        input()
    if n%2 == 1:
        print("Case #{}: 1".format(t+1))
        print("0.0")
    else:
        print("Case #{}: 0".format(t+1))
