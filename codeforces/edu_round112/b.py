T = int(input())
for t in range(T):
    w,h = map(int, input().split())
    x,y,xx,yy = map(int, input().split())
    ww,hh = map(int, input().split())

    ans = 1123456789
    if ww + xx-x <= w:
        ans = min(ans, max(0, ww-x), max(0, ww-(w-xx)))
    if hh + yy-y <= h:
        ans = min(ans, max(0, hh-(h-yy)), max(0, hh-y))
    if ans == 1123456789:
        print(-1)
    else:
        print(ans)