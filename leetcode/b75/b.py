class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nums = [(nums[i-1]+nums[i])%10 for i in range(1, len(nums))]
        return nums[0]