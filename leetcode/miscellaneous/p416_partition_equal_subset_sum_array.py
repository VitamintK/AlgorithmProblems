class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        half = sum(nums)//2
        if half*2 != sum(nums):
            return False
        
        DP = [0 for i in range(half+1)]
        DP[0] = True
        newDP = [x for x in DP]
        
        for i in range(len(nums)):
            for j in range(half+1):
                if j - nums[i] >= 0:
                    newDP[j] = DP[j]
                    newDP[j] = DP[j-nums[i]] or newDP[j]
            DP, newDP = newDP, DP
        return bool(DP[half])