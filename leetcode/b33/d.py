def dfs(r, c, labels, grid, oldr, oldc):
    labels[r][c] = 1
    for dr, dc in [(-1,0), (0,1), (0,-1), (1,0)]:
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= len(grid):
            continue
        if nc < 0 or nc >= len(grid[0]):
            continue
        if nc == oldc and nr == oldr:
            continue
        if grid[nr][nc] == grid[r][c]:
            if labels[nr][nc]:
                print(nr, nc, r, c)
                return True
            if dfs(nr, nc, labels, grid, r, c):
                return True
    return False

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        labels = [[0 for i in r] for r in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print(labels)
                if not labels[i][j]:
                    if dfs(i,j,labels, grid, -1, -1):
                        return True
        return False