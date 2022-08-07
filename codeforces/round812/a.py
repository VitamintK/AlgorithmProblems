T = int(input())
for t in range(T):
    n = int(input())
    xmax, xmin, ymax, ymin = 0,0,0,0    
    for i in range(n):
        x,y = map(int, input().split())
        xmax = max(xmax, x)
        xmin = min(xmin, x)
        ymax = max(ymax, y)
        ymin = min(ymin, y)
    print(2 * (xmax-xmin + ymax-ymin))