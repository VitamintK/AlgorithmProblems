class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dppos = [[0 for i in r] for r in grid]
        dpneg = [[0 for i in r] for r in grid]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0 and c == 0:
                    if grid[r][c] > 0:
                        dppos[r][c] = grid[r][c]
                    elif grid[r][c] < 0:
                        dpneg[r][c] = grid[r][c]
                    continue
                ancestor_coords = []
                if r > 0:
                    ancestor_coords.append((r-1, c))
                if c > 0:
                    ancestor_coords.append((r, c-1))
                if grid[r][c] == 0:
                    dppos[r][c] = 0
                    dpneg[r][c] = 0
                elif grid[r][c] < 0:
                    dppos[r][c] = min(dpneg[i][j] for i,j in ancestor_coords)*grid[r][c]
                    dpneg[r][c] = max(dppos[i][j] for i,j in ancestor_coords)*grid[r][c]
                else:
                    dppos[r][c] = max(dppos[i][j] for i,j in ancestor_coords)*grid[r][c]
                    dpneg[r][c] = min(dpneg[i][j] for i,j in ancestor_coords)*grid[r][c]
        ans = dppos[-1][-1]
        if ans == 0:
            if any(any(x==0 for x in r) for r in grid):
                return 0
            else:
                return -1
        MOD = 1000000007
        return ans%MOD