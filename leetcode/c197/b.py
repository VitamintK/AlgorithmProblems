class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        cur = 0
        for i in range(len(s)):
            if s[i] == '1':
                cur += 1
                ans += cur
            else:
                cur = 0
        return ans%1000000007