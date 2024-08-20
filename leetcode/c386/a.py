class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for x in c:
            if c[x] > 2:
                return False
        return True