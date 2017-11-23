# https://leetcode.com/problems/continuous-subarray-sum/description/
class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1] == 0:
                    return True
            return False
        k = abs(k)
        s = set() #keeps track of what running sums mod k we've seen so far
        s.add(0)
        running= 0

        for i in range(len(nums)):
            running += nums[i]
            running %= k
            if running in s and i > 0:
                #if we've seen this running sum mod k before, then the interval from there to here is divisible by k
                return True
            s.add(running)
        return False