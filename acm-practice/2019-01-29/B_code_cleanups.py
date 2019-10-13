thresh = 20
days = int(input())
xs = [int(x) for x in input().split()]
xs.reverse()
n = 0
s = 0
ans = 0
for day in range(1,366):
    if len(xs) > 0 and xs[-1] == day:
        n += 1
        xs.pop()
    s += n
    if s >= thresh:
        n = 0
        s = 0
        ans += 1
if n > 0 or s > 0:
    ans += 1
print(ans)