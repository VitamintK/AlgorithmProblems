class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        print([nums.count(x) for x in nums])
        n = list(sorted(nums, key = lambda x: (nums.count(x), -x)))
        # print(list(sorted(nums, key= lambda x: (nums.count(x)))))
        return n
        # APPARENTLY nums.sort(key=lambda x: nums.count(x)) DOES NOT WORK
        # because nums gets set to [] as an implementation detail of cpython >:(
