n, sx, sy = map(int, input().split())
u, r, d, l = 0, 0, 0, 0
for i in range(n):
    x, y = map(int, input().split())
    if x < sx:
        l += 1
    if x > sx:
        r += 1
    if y < sy:
        u += 1
    if y > sy:
        d += 1

ans = max(u,r,d,l)
print(ans)
if u == ans:
    print(sx, sy-1)
elif r == ans:
    print(sx+1, sy)
elif d == ans:
    print(sx, sy+1)
elif l == ans:
    print(sx-1, sy)