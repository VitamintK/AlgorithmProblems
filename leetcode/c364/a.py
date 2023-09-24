# 2864. Maximum Odd Binary Number
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zs = s.count('0')
        return '1' * (ones-1) + '0' * zs + '1'