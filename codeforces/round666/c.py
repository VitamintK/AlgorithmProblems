n = int(input())
xs = [int(x) for x in input().split()]
ans = []
for i in range(len(xs)-1):
    c = (n-1) * xs[i]
    ans.append(c)
if n == 1:
    print(1, 1)
    print(0)
else:
    print(1, n-1)
    print(' '.join(str(x) for x in ans))
print(n, n)
print((n-1) * xs[-1])
print(1, n)
ans = []
for x in xs:
    c = -n * x
    ans.append(c)
print(' '.join(str(x) for x in ans))