n = int(input())
xs = [int(x) for x in input().split()]
a = []
b = []
for i in range(len(xs)):
    if i%2 == 0:
        a.append(xs[i])
    else:
        b.append(xs[i])

print(min(sum(a), sum(b))*2)