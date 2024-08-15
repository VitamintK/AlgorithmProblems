T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    xs = [int(x) for x in input().split()]
    xs.sort(reverse=True)
    makeup = 0
    score = 0
    for i in range(n):
        if i%2 == 1:
            makeup += xs[i-1] - xs[i]
            score -= xs[i]
        else:
            score += xs[i]
    score -= min(makeup, k)
    print(score)
