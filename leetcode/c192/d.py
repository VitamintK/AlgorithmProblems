class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[9999999999999 for k in range(n+1)] for i in range(0,m+1)] for j in range(0,m)]
        #DP[house #][neighborhoods][house # color]
        for house in range(m):
            for neighborhoods in range(1,m+1):
                for last_color in range(1,n+1):
                    if houses[house] != 0:
                        color = houses[house]
                        if house == 0:
                            dp[house][1][color] = 0
                            break
                        if color == last_color:
                            dp[house][neighborhoods][color] = min(dp[house][neighborhoods][color], dp[house-1][neighborhoods][color])
                        else:
                            dp[house][neighborhoods][color] = min(dp[house][neighborhoods][color], dp[house-1][neighborhoods-1][last_color])
                        continue
                    for color in range(1,n+1):
                        if house == 0:
                            dp[house][1][color] = cost[house][color-1]
                            continue
                        if color == last_color:
                            # print('beep')
                            dp[house][neighborhoods][color] = min(dp[house][neighborhoods][color], dp[house-1][neighborhoods][color] + cost[house][color-1])
                        else:
                            # print('boop')
                            dp[house][neighborhoods][color] = min(dp[house][neighborhoods][color], dp[house-1][neighborhoods-1][last_color] + cost[house][color-1])
                    # print(house, neighborhoods, last_color, dp[house][neighborhoods][color])
        ans = min(dp[-1][target])
        # print(dp)
        if ans == 9999999999999:
            return -1
        return ans