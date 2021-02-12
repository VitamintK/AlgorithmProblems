MOD = 1000000007
n = int(input())
grid = []
for i in range(n):
    grid.append(input())
dp = [[None for i in row] for row in grid]
for i in reversed(range(len(grid))):
    for j in reversed(range(len(grid[i]))):
        treasure = 1 if grid[i][j] == '1' else 0
        cands = []
        if i+1 < len(grid):
            cands.append(dp[i+1][j])
        if j+1 < len(grid[i]):
            cands.append(dp[i][j+1])
        if len(cands) == 0:
            dp[i][j] = (treasure, 1)
        else:
        # elif len(cands) == 1:
        #     dp[i][j] = (cands[0][0]+treasure, cands[0][1])
        # else:
            if len(cands) > 1 and cands[0][0] == cands[1][0]:
                dp[i][j] = cands[0][0]+treasure, cands[1][1]+cands[0][1]
            else:
                value, count = max(cands)
                dp[i][j] = value+treasure, count
        dp[i][j] = (dp[i][j][0], dp[i][j][1]%MOD)
print(*dp[0][0])