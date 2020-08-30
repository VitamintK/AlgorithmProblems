def dfs(grid, delete):
    g = [[x for x in r] for r in grid]
    if delete is not None:
        r, c = delete
        g[r][c] = 0
    o = 0
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j]:
                o += 1
                dfs2(g, i,j)
    return o != 1

def dfs2(g, r, c):
    for dr, dc in [(-1, 0), (1,0), (0,1), (0,-1)]:
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= len(g) or nc < 0 or nc >= len(g[0]):
            continue
        if g[nr][nc] == 1:
            g[nr][nc] = 0
            dfs2(g, nr, nc)

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        if dfs(grid, None):
            return 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dfs(grid, (r,c)):
                    return 1
        return 2
                        