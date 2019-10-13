r, c = map(int, input().split())
grid = []
for i in range(r):
    grid.append(list(input()))

ans = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'L':
            #then DFS and color all reachable L and C with value -1
            ans+=1
            stack = [(i,j)]
            while len(stack) > 0:
                ex = stack.pop()
                grid[ex[0]][ex[1]] = -1
                for dr, dc in [(-1,0), (0,1), (1,0), (0,-1)]:
                    nr, nc = dr+ex[0], dc+ex[1]
                    if nr < 0 or nr >= r or nc < 0 or nc >= c:
                        continue
                    if grid[nr][nc] in ['L','C']:
                        stack.append((nr, nc))
print(ans)
