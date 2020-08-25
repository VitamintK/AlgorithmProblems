class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        doubles = 0
        for n in nums:
            d = 0
            while n > 1:
                ans += n%2
                d += 1
                n//=2
            if n > 0:
                ans += 1
            doubles = max(doubles, d)
        return ans + doubles