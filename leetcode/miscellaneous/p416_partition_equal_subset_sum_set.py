class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        half = sum(nums)//2
        if half*2 != sum(nums):
            return False
        
        DP = {0}
        for i in range(len(nums)):
            n = {x for x in DP}
            for j in DP:
                n.add(j + nums[i])
            DP = n

        return half in DP