T = int(input())

def manhattan(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return abs(x2-x1) + abs(y2-y1)

for t in range(T):
    n,m,i,j = map(int, input().split())
    corners = [(0,0), (0,m-1), (n-1, 0), (n-1,m-1)]
    argbest = None
    best = 0
    anton = (i-1, j-1)
    for pt1 in corners:
        for pt2 in corners:
            dist = manhattan(pt1, pt2) + manhattan(pt1, anton) + manhattan(anton, pt2)
            # print(pt1, pt2, anton, dist)
            if dist >= best:
                best = dist
                argbest = (pt1[0], pt1[1], pt2[0], pt2[1])
    # print(best)
    print(*[x+1 for x in argbest])