T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    x1,y1,x2,y2 = map(int, input().split())
    ans = 4
    for (x,y) in [(x1,y1), (x2,y2)]:
        num = 4
        if x == 1 or x==n:
            num -= 1
        if y==1 or y==m:
            num -= 1
        ans = min(ans, num)
    print(ans)