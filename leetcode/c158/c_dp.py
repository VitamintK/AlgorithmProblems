class Solution:
    def dieSimulator(self, n, rollMax):
        dp = [[0 for i in range(x)] for x in rollMax]
        dp[0][0] = 1
        for i in range(n):
        	new_dp = [[0 for _ in range(x+1)] for x in rollMax]
        	for roll in range(6):
        		for prev_roll, consecs in enumerate(dp):
        			for consec, amt in enumerate(consecs):
        				if prev_roll != roll:
        					new_dp[roll][1] += amt
        				else:
        					if consec != rollMax[roll]:
        						new_dp[roll][consec+1] += amt
        	dp = new_dp
        ans = 0
        for i in dp:
        	for j in i:
        		ans += j
        return ans % 1000000007

# b = Solution()
# print(b.dieSimulator(3, [1,1,1,2,2,3]))