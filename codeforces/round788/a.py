T = int(input())
for t in range(T):
    n = int(input())
    xs = [int(x) for x in input().split()]
    negatives = 0
    for x in xs:
        if x < 0:
            negatives += 1
    good = True
    for i in range(negatives):
        if i == 0:
            continue
        if abs(xs[i]) > abs(xs[i-1]):
            good = False
            break
    for i in range(negatives, n):
        if i == negatives:
            continue
        if abs(xs[i]) < abs(xs[i-1]):
            good = False
            break
    if good:
        print("YES")
    else:
        print("NO")