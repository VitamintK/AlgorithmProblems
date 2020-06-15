class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        presum = []
        accum = 0
        for n in nums:
            accum += n
            presum.append(accum)
        return presum