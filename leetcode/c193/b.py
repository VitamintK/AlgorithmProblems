from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        nums = Counter(arr)
        cnts = [v for k,v in nums.items()]
        cnts.sort(reverse=True)
        while k > 0:
            if cnts[-1] <= k:
                k -= cnts[-1]
                cnts.pop()
            else:
                break
        return len(cnts)