n = int(input())
xs = [int(x) for x in input().split()]
while all(x%2==0 for x in xs):
    xs = [x//2 for x in xs]
sm = sum(xs)
if sum(xs)%2 == 1:
    print(0)
    exit()
dp = set([0])
good = True
for x in xs:
    toadd = set()
    for s in dp:
        num = x + s
        if num == sm//2:
            good = False
            break
        toadd.add(num)
    dp = dp.union(toadd)
if good:
    print(0)
else:
    print(1)
    for i,x in enumerate(xs):
        if x%2 == 1:
            print(i+1)
            break