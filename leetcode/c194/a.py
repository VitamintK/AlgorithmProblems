# solved at 0:01:07
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2*i for i in range(n)]
        accum = 0
        for i in nums:
            accum ^= i
        return accum