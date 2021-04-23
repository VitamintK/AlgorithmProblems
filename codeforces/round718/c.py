n = int(input())
xs = [int(x) for x in input().split()]
grid = [[-1 for i in range(j+1)] for j in range(n)]
for i in range(len(xs)):
    grid[i][-1] = xs[i]
def fill(grid, num, left, start):
    if left == 0:
        return 0
    r, c = start
    if c > 0 and grid[r][c-1] == -1:
        grid[r][c-1] = num
        fill(grid, num, left-1, (r,c-1))
    else:
        assert grid[r+1][c] == -1
        grid[r+1][c] = num
        fill(grid, num, left-1, (r+1, c))
for i in range(n):
    fill(grid, xs[i], xs[i]-1, (i, i))
for r in grid:
    print(*r)