class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        h = [n-r for r in right]
        left.extend(h)
        return max(left)