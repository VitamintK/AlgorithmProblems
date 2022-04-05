class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x = 1
        ans = 0
        while x < 1123456789:
            if (x&start) != (x&goal):
                ans += 1
            x *= 2
        return ans
        