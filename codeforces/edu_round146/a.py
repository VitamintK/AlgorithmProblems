T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    if n%2 == 0:
        print("YES")
        continue
    if k%2 == 0:
        print("NO")
        continue
    if k > n:
        print("NO")
        continue
    print("YES")