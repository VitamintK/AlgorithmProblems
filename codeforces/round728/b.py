# n = 100000
# ans = 0
# for i in range(1,n):
#     ans += (n-i)/(i+1)
# print(ans)
# >>> 1009026.7031324713

T = int(input())
for t in range(T):
    n = int(input())
    ans = 0
    xs = [None] + [int(x) for x in input().split()]
    for i in range(1,n+1):
        x = xs[i]
        m = (i%x)
        compl = x-m
        cand = x*(i//x) + compl
        if cand <= i:
            cand += x
        for j in range(cand, n+1, x):
            if i+j == xs[i]*xs[j]:
                ans += 1
    print(ans)