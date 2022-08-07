class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = [x for x in nums if x > 0]
        return len(set(l))