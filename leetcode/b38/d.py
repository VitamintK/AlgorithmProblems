from collections import Counter
MOD = 1000000007
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        letters = [Counter(word[i] for word in words) for i in range(len(words[0]))]
        print(letters)
        dp = [0 for x in range(len(target)+1)]
        dp[0] = 1
        for i in range(len(words[0])):
            for j in reversed(range(len(dp))):
                if j == len(target):
                    continue
                dp[j+1] += dp[j]*letters[i][target[j]] 
                dp[j+1]%=MOD
            # print(dp)
        return dp[-1]