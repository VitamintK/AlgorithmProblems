T = int(input())
for t in range(T):
    n = input().split()[1]
    oc = int(n,8) if all(x < '8' for x in n) else 0
    print(t+1, oc, int(n), int(n,16))
