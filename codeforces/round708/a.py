from collections import Counter
T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    c = Counter(xs)
    ans = []
    for x in range(105):
        if x not in c:
            break
        else:
            ans.append(x)
            c[x] -=1
    for x, occurence in c.items():
        for i in range(occurence):
            ans.append(x)

    print(*ans)