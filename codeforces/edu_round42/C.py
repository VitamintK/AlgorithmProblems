squares = []
for i in range(1,100000):
    squares.append(str(i*i))
    if int(squares[-1]) > 2000000000:
        break

n = input()

ans = 1000

def deletions(source, target):
    """returns 1000 if impossible, otherwise number of deletions to make s to t"""
    pt = 0
    for i in source:
        if i == target[pt]:
            pt+=1
        if pt == len(target):
            break
    if pt == len(target):
        return len(source)-len(target)
    else:
        return 1000

for i in squares:
    ans = min(ans, deletions(n, i))

if ans < 1000:
    print(ans)
else:
    print(-1)
