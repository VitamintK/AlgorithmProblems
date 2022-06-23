T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    grid = []
    max_num = -9999999999
    for i in range(n):
        xs = [int(x) for x in input().split()]
        max_num = max(max_num, max(xs))
        grid.append(xs)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == max_num:
                w = max(j+1, m-j)
                h = max(i+1, n-i)
                ans = w*h
    print(ans)