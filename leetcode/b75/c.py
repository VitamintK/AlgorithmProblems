class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        tot1 = s.count('1')
        tot0 = s.count('0')
        left1 = 0
        ans = 0
        for i in range(len(s)):
            # we've already processed i on the left
            left0 = i - left1
            right1 = tot1 - left1 - (s[i] == '1')
            right0 = (n - i - 1) - right1
            if s[i]=='1':
                ans += left0 * right0
            else:
                ans += left1 * right1
            
            left1 += (s[i] == '1')
        return ans

            