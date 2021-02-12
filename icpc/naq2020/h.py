x, y = map(int, input().split())
key = input()
grid = []
for i in range(y):
    grid.append(input())

grid.reverse()

max_int = 1234567898654
# key = 0 means used 0 digits
# key = n means used all n digits
dp = [[[max_int for i in range(len(key)+1)] for r in range(x)] for c in range(y)]
for i in range(y):
    for j in range(x):
        val = int(grid[i][j])
        if i == 0 == j:
            dp[i][j][0] = val
            continue
        for k in range(len(key)+1):
            if i > 0:
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k] + val)
            if j > 0:
                dp[i][j][k] = min(dp[i][j][k], dp[i][j-1][k] + val)
            if k > 0:
                k_index = k-1
                margin = int(key[k_index])+1
                if i >= margin:
                    dp[i][j][k] = min(dp[i][j][k], dp[i-margin][j][k-1] + val)
                if j >= margin:
                    dp[i][j][k] = min(dp[i][j][k], dp[i][j-margin][k-1] + val)
# for r in grid:
#     print(r)
# for r in dp:
#     print(r)
print(min(dp[-1][-1]))