MOD = 1000000007
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        return (pow(pow(2,p)-2, pow(2,p-1) - 1, MOD) * (pow(2,p)-1))%MOD