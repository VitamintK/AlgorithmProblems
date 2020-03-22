# Divide Array in Sets of K Consecutive Numbers
from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        if len(nums)%k != 0:
            return False
        for i in range(0, len(nums), k):
            start = min(k for k,v in c.items() if v != 0)
            for j in range(k):
                x = start+j
                if c[x] <= 0:
                    return False
                c[x] -= 1
        return True