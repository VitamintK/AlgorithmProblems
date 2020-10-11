from collections import Counter
T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    c = Counter(xs)
    ans = 0
    double = 0
    for k in c:
        if c[k] == 1:
            ans += 1
        else:
            ans += c[k]
            double = 1
    if double == 0:
        print("First")
    else:
        ans -= 1
        print("Second" if ans%2 == 1 else "First")