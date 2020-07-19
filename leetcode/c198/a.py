class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        b = 0
        while numBottles > 0:
            ans += numBottles
            b += numBottles
            numBottles = 0
            x = b//numExchange
            b -= x*numExchange
            numBottles += x
        return ans