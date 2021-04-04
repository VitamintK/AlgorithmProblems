h, w = map(int, input().split())
grid = []
for i in range(h):
    grid.append(input())
r,c = 0,0
ans = 0
for i in range(h+w-2):
    # print(r,c)
    if grid[r][c] == '*':
        ans += 1
    if r==h-1:
        c += 1
        continue
    if c == w-1:
        r+=1
        continue
    right = (111111,111)
    for row in range(r, h):
        if '*' in grid[row][c+1:]:
            right = min(right, (grid[row][c+1:].index('*'),row-r))
    down = (11111,111)
    for col in range(c, w):
        column = [grid[r][col] for r in range(r+1,h)]
        if '*' in column:
            down = min(down, (column.index('*'),col-c))
    # print('right, down:', right, down)
    if down < right:
        r += 1
    else:
        c += 1
if grid[r][c] == '*':
    ans +=1
print(ans)