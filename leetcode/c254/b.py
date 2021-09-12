class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(2,len(nums),2):
            nums[i-1],nums[i] = nums[i], nums[i-1]
        return nums